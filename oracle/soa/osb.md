[Data Sheet (2013)](https://www.oracle.com/docs/tech/service-bus-ds.pdf)
# Oracle Service Bus
A lightweight integration Enterprise Service Bus (ESB)
- code-free: configuration-based integration
  - policy-based service virtualization
  - visual debugging: message-level tracing, action-level metrics
- an integral part of Oracle SOA Suite
  - > It performs end-to-end governance by automatically synchronizing Oracle SOA Governance solution
# History
- born as AquaLogic Service Bus (BEA Systems, 2005)
- deprecated by container, API gateway (2016)


# Features
> Oracle Service Bus is the first solution to combine service integration, messaging, operational service management, and security-enforcement capabilities


Modern Service Patterns
- Modern stateless service architecture is based on REST. 
- future ready: With Oracle Service Bus, developers can easily transform existing services into REST style services thereby avoiding extensive programmatic changes.
- legacy facing: Oracle Service Bus can handle non-XML payloads with a host of datasources such as File, EJB, FTP, MQ, JMS and Tuxedo
- Enable mobile

Scalability
- Oracle Service Bus has the ability to scale easily to thousands of services, 
- Near linear scalability on clustered deployments.

Modern UI
- beyond own IDE, it also offers a Web-based design environment
- joint-edit collaboration is supported with version control

Performance
- memeory caching by embedded Oracle Coherence

Integration
- integrate EIS by Oracle JCA Adapters
- integrate with [IBM WebSphere MQ](https://www.oracle.com/docs/tech/middleware/osb-websphere-technical-brief.pdf) (2009)

# Install
For a development or evaluation distribution, download the [Oracle SOA Suite Quick Start for Developers](https://www.oracle.com/middleware/technologies/soasuite/downloads.html#)
- bundled together with [Oracle BPM](../bpm/README.md)

# For a production environment

Download the Oracle Fusion Middleware Infrastructure distribution from the [Oracle WebLogic Server download page].

Download the production distribution for Oracle Service Bus from the [Oracle Software Delivery Cloud].

