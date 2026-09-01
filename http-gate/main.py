import asyncio
import os

import redis.asyncio as aioredis
from fastapi import FastAPI, Query, Request
from fastapi.responses import JSONResponse, Response

app = FastAPI()

REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379")
GATE_CHANNEL_PREFIX = "gate-channel:"


def _gate_channel(nonce: str) -> str:
    return f"{GATE_CHANNEL_PREFIX}{nonce}"


async def get_redis() -> aioredis.Redis:
    return aioredis.from_url(REDIS_URL, decode_responses=True)


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=502, content={"detail": str(exc)})


@app.get("/sleep", status_code=204, response_class=Response)
async def sleep(seconds: float = Query(..., description="Number of seconds to wait")):
    """wait N seconds"""
    await asyncio.sleep(seconds)



@app.get("/pause", status_code=204, response_class=Response)
async def wait_until(
    nonce: str = Query(..., description="Unique identifier for this gate"),
):
    """set a gate in Redis, block until /resume clears it"""
    r = await get_redis()
    pubsub = r.pubsub()
    try:
        await pubsub.subscribe(_gate_channel(nonce))
        async for message in pubsub.listen():
            if message["type"] == "message":
                return Response(status_code=204)
    finally:
        await pubsub.aclose()
        await r.aclose()



@app.get("/resume", status_code=204, response_class=Response)
async def resume(nonce: str = Query(..., description="Nonce of the gate to clear")):
    """delete the gate key so /pause unblocks"""
    r = await get_redis()
    try:
        receivers = await r.publish(_gate_channel(nonce), "resume")
        if receivers == 0:
            return Response(status_code=404)
        return Response(status_code=204)
    finally:
        await r.aclose()


@app.delete("/reset")
async def reset_gates():
    """publish resume to all active gate channels and return how many were reset"""
    r = await get_redis()
    try:
        channels = await r.pubsub_channels(f"{GATE_CHANNEL_PREFIX}*")
        count = 0
        for ch in channels:
            receivers = await r.publish(ch, "resume")
            if receivers > 0:
                count += 1
        return JSONResponse(content={"reset": count})
    finally:
        await r.aclose()

@app.get("/list")
async def list_gates():
    """show all active (un-resumed) gates"""
    r = await get_redis()
    try:
        channels = await r.pubsub_channels(f"{GATE_CHANNEL_PREFIX}*")
        nonces = [ch.removeprefix(GATE_CHANNEL_PREFIX) for ch in channels]
        return JSONResponse(content={"gates": nonces})
    finally:
        await r.aclose()
