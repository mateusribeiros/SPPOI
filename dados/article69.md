Title: MICAAL: A Domain-Specific Language for Microservices in Ambient Assisted Living

ABSTRACT The rise of the Internet of Things (IoT) has driven innovation across various sectors, one of
its benefiting areas is healthcare. Within this domain, Ambient Assisted Living (AAL) aims to improve
the wellbeing and independence of vulnerable populations, particularly seniors, by using IoT technologies.
As AAL environments become increasingly complex and diverse, traditional monolithic architectures
struggle to offer the flexibility and scalability required for sustainable solutions. In response, paradigms
such as microservices architectures emerge as a powerful approach to overcome these challenges. This paper
presents MICAAL, a Domain-Specific Language (DSL), to model microservices-oriented architectures for
AAL environments. MICAAL empowers users to design modular, scalable systems by enabling the easy
selection and deployment of microservices ensuring that IoT devices in AAL environments are efficiently
supported and adaptable to changing needs. We demonstrate the practical usability of MICAAL through a
case study of a real-world AAL system. We also present an empirical evaluation, using the Technology
Acceptance Model (TAM), assessing user satisfaction and intention to adopt MICAAL for modeling
microservice-based architectures for AAL. The results confirm that MICAAL simplifies the modeling
process and promotes efficient, future-proof AAL systems.
INDEX TERMS Ambient assisted living, domain-specific language, microservices, Internet of Things.
I. INTRODUCTION
The Internet of Things (IoT) has revolutionized the way
to connect and interact with devices, creating a global
network where ‘Things’ can communicate, share data, and
autonomously perform tasks [1], [2]. Healthcare, particularly
Ambient Assisted Living (AAL), has benefited greatly, with
IoT-driven solutions offering intelligent environments that
support vulnerable populations, including older adults and
individuals with special needs [3], [4], [5]. AAL systems
depend on real-time data processing, reliable communication,
and adaptive infrastructures to meet the dynamic needs of
users and environments [4], [5], [6].
In response to the growing complexity of IoT applications,
driven by the increasing number of connected devices and the
need for high-speed, dedicated services in critical application
areas such as AAL, Service-Oriented Architecture (SOA)
emerged as an ideal foundation for developing distributed
solutions [7]. SOA provides a robust framework for structuring software systems as collections of loosely coupled,
interoperable services that can integrate Edge, Fog, and Cloud
Computing environments. This architecture enables efficient
handling of complex services and scalable operations across
distributed infrastructure. However, as IoT systems have
evolved and diversified, the demand for more granular,
modular solutions has led to the rise of microservices [8].
Derived from SOA principles, microservices emphasize
independently deployable services, minimal centralized
management, and enhanced development flexibility. This
modular approach is beneficial for critical applications
like AAL, where systems must be adaptive, scalable, and
capable of seamless communication between heterogeneous
components [9].
Beyond the advantages of microservices, developing
IoT applications that harness these architectures effectively
may require specialized tools to handle domain-specific
requirements. This is where Domain-Specific Languages
(DSLs) come up to bridge this gap. DSLs provide higherlevel abstractions that capture the common characteristics
that belong to particular application areas, simplifying the
design and development process [10], [11]. For example,
FOGAAL, a DSL designed to architect Fog Computing
(FC) solutions in AAL environments, demonstrates how
DSLs can facilitate the modeling of complex IoT solutions,
encapsulating domain-specific details [12]. In addition, the
DSLs have the advantage of being extensible and modular
and, therefore, capable of interconnecting with other modules
in the same context [11].
Building on the DSLs modularity concept, this paper
presents: i) MICAAL, a DSL that supports the modeling
of microservices architectures for IoT devices within AAL
environments. This DSL is a complementary module of
FOGAAL [12]. MICAAL is based on the Spring Cloud
Netflix microservices architecture [13], [14] to provide
a standardized framework for microservices components,
thus offering a comprehensive platform for developers
to design, deploy, and manage microservices tailored to
the needs of AAL applications; ii) an experimental use
case of MICAAL in AAL solutions; and iii) a controlled
quasi-experiment involving a group of software engineers
designing a proposed microservices architecture using
MICAAL [15], [16]. Following the use of the tool, user
perceptions were assessed using the Technology Acceptance
Model (TAM) [17].
The paper is organized as follows: The section II presents
the Background and section III the Related Work, Section IV
describes the MICAAL DSL, Section V showcases an
illustrative experimental scenario demonstrating the use of
the proposed approach for modeling an AAL environment,
Section VI presents the empirical evaluation of MICAAL,
Section VII states the advantages and limitations of
MICAAL, and finally Section VIII provides the conclusions
and outlines further research steps.
II. BACKGROUND
This section outlines the background for MICAAL DSL,
beginning with the role of Domain-Specific Languages in
simplifying IoT systems, particularly in areas like Ambient
Assisted Living. It introduces FOGAAL DSL as a foundational approach within the AAL context, from which
MICAAL DSL module is proposed. It examines the shift
from Service Oriented Architectures to Microservices in
healthcare, highlighting their benefits for AAL applications.
Finally, it presents the Spring Cloud Netflix microservices
architecture as the framework guiding MICAAL’s development.
A. DOMAIN-SPECIFIC LANGUAGES IN IOT
Domain-Specific Languages are key tools for simplifying
the design and deployment of IoT applications by providing
high-level abstractions shaped to specific domains. Unlike
general-purpose programming languages, DSLs encapsulate
domain-specific concepts such as sensors, actuators, and
data flows, enabling developers to focus on application logic
rather than low-level technical details [18]. This approach
reduces development time, enhances system standardization,
and helps collaboration between domain experts (usually
non-technical) and technical developers.
Although DSLs have been successfully applied in various
IoT and microservices-related contexts [12], [19], [20], [21],
[22], [23], [24], [25], [26], [27], [28], [29], [30], several
challenges persist in their development. These challenges
include interoperability issues among heterogeneous devices,
the lack of user-friendly visual interfaces, and reliance on
internal syntaxes that may alienate non-technical users [10],
[11]. Addressing these issues requires the creation of
DSLs aligned to specific domains, the incorporation of
visual syntaxes, and ensuring compatibility with diverse
communication protocols and the unique characteristics of
applied contexts. These aspects will be further discussed in
Section III.
DSLs are particularly impactful in domains where diverse
knowledge areas converge to create specialized solutions.
For instance, in the AAL domain, DSLs can facilitate the
rapid modeling of complex systems by integrating paradigms
such as Cloud Computing and IoT-related approaches like
Fog and Edge Computing within medical contexts [12], [19].
As IoT applications continue to grow in complexity, DSLs
will play a pivotal role in streamlining development and
fostering collaboration between technical and non-technical
stakeholders.
B. FOGAAL DSL
FOGAAL (Fog Computing for Ambient Assisted Living)
[12] is a DSL designed for the modelling and management
of Fog Computing infrastructures specifically within AAL
environments. It provides a specialized framework for
modeling IoT-based systems aimed at supporting elderly
or disabled individuals through real-time data processing,
resource allocation, and decision-making at the network edge.
By leveraging the decentralized and low-latency characteristics of Fog Computing, FOGAAL facilitates the creation
of adaptive and efficient AAL solutions, ensuring scalability,
energy efficiency, and responsiveness (see Figure1).
This DSL bridges the gap between high-level AAL system
design and the technical complexities of Fog Computing, enabling developers and domain experts to abstractly
define system behaviors and interactions while automating
the underlying infrastructure configurations. The tool was
developed in alignment with two key standards to ensure
robustness and ease of adoption by domain experts. First,
the SOPRANO Ontology, which defines the structure and
elements in AAL environments, and second, the NIST
standard for Fog Computing, which ensures consistency with
all components of a Fog Computing network. By integrating
these two standards, FOGAAL establishes a solid foundation
for the DSL, combining the strengths of both frameworks.
C. SERVICE ORIENTED ARCHITECTURES
Service Oriented Architecture is a design approach in
which software applications are composed of self-contained,
loosely coupled services that communicate through defined
interfaces to perform specific functions [7]. SOA introduces
modularity to application design by grouping components
into various services that exchange data or execute activities
collaboratively via defined interfaces and communication
protocols. This is often done within a multi-layered architecture aligned to the application’s scale and complexity [7],
[9]. SOA enables independent development, deployment, and
maintenance of services, which can be built in different
programming languages and deployed on various platforms.
These services can range from small, simple functionalities
to large, enterprise-grade solutions [9]. The SOA advantages
include:
• Flexibility and extensibility. SOA can be configured to
meet the needs of diverse users by allowing services to
be independently developed, updated and reused.
• Technology agnosticism. Services can be implemented
in various programming languages and platforms.
• Scalability and maintainability. Individual services
can be tested and deployed independently, reducing
complexity during upgrades and maintenance.
• Interoperability. SOA’s loosely coupled nature makes it
easier to integrate heterogeneous systems.
However, SOA also has limitations, such as increased
development complexity and potential performance degradation caused by interservice communication overhead.
These constraints become significant as systems grow in
size and interdependencies increase, sometimes leading to
monolithic-like challenges in complex architectures. Despite
these drawbacks, SOA laid the groundwork for the evolution
of more modern paradigms like microservices, addressing
key issues such as modularity and reusability in application
design [9].
D. MICROSERVICES
Microservices are an evolution of SOA designed to overcome
its limitations by emphasizing highly decentralized, finegrained services. Each microservice is a small, independently
deployable functional unit focused on performing a single
business capability, with its own database and communication
interface [8]. Microservices architectures emerged in the
late 2000s and gained widespread adoption in the 2010s
to address the scalability needs of cloud and IoT environments [31].
Microservices differ from monolithic and SOA-based
systems in several ways:
• Independence. Unlike monolithic architectures, where
tightly coupled components can hinder scalability and
flexibility, microservices are loosely coupled, enabling
independent development, deployment, and scaling.
• Agility. Microservices allow faster deployment, reducing time-to-market and enabling cross-functional teams
to work autonomously on specific services.
• Fault isolation. Failures in one service are contained and
do not cascade to the entire application.
• Scalability. Services can be scaled individually, which
is particularly beneficial for large-scale IoT applications
that involve heterogeneous devices and data sources.
In IoT and healthcare contexts, microservices bring
significant advantages. IoT systems, inherently modular and
data-intensive, align well with microservices’ decentralized
and scalable nature. In healthcare, where real-time data
processing, high availability, and fault tolerance are critical,
microservices support robust architectures [8], [31]. For
example, Remote Healthcare Monitoring Systems (RHMS)
may benefit from microservices’ ability to manage complex, heterogeneous datasets, enabling secure, scalable, and
adaptive solutions. In systems like RO-SmartAgeing [9],
microservices are used across Edge, Fog, and Cloud layers
to deliver high-quality, real-time healthcare monitoring while
ensuring privacy and data integrity.
Microservices thus provide the agility and robustness
required for modern IoT and healthcare applications,
addressing the challenges of scalability, fault tolerance, and
modularity in dynamic environments. This makes them an
ideal choice for extending AAL solutions to meet evolving
needs both from users and IoT devices.
1) SPRING CLOUD NETFLIX ARCHITECTURE
Netflix, a widely-used multimedia platform, exemplifies one
of the most successful implementations of microservices
architecture. Spring Cloud Netflix [14], which underpins
Netflix’s system, manages one-third of downstream internet
traffic in the U.S., processes over 2 billion requests daily, and
operates approximately 500 microservices. These features
enable high availability and scalability. Due to the significant
success achieved through this architecture, Netflix began
releasing the code that facilitated the development of its
microservices framework in 2012, which has since become
the foundation for numerous global projects.
The Spring Cloud Netflix architecture (see Figure 3),
is composed of five main elements, described as follows:
• Eureka. A server responsible for registering and locating microservices; it also manages load balancing and
fault tolerance [13], [14].
• Cloud-Config. A configuration server designed
for distributed systems, tasked with storing the
configuration properties of the ecosystem’s
microservices [13], [14].
FIGURE 1. FOGAAL DSL Overview and Graphical User Interface.
FIGURE 2. Overview of SOA in Microservices and IoT [31].
• Hystrix. A Circuit Breaker library that manages
interactions between services in distributed systems, providing latency control and fault tolerance
capabilities [13], [14].
• Ribbon. A library that facilitates communication
processes in the cloud, enabling client-side load
balancing. Each load balancer consists of components working together to connect to a remote
server [13], [14].
• Zuul. An edge service within the network, offering
dynamic routing, load balancing, monitoring, and
request sequencing [13], [14].
Overall, the introduced tools and concept, serve as key
reference foundations for understanding broader architectural
trends in modern IoT solutions. They provide the foundational framework for MICAAL’s development, setting the
stage for the advanced microservices architecture oriented to
AAL environments.
III. RELATED WORK
This section analyzes both microservices-oriented DSLs
and IoT-oriented DSLs, with special attention to those
related to healthcare domains, including AAL. A total of
12 studies were selected from IEEE Xplore, Springer Link,
ScienceDirect, and ACM Digital Libraries, covering the last
decade. The studies were identified using the following
search string:
(Domain-Specific Language OR DSL) AND (Internet of
Things OR IoT) AND Microservices AND (Ambient Assisted
Living OR AAL OR Healthcare).
Table 1 presents an overview of the selected articles, summarizing their key contributions and weaknesses compared
to the MICAAL DSL. The criteria analyzed include several
key characteristics: whether the proposed DSL solution is
based on graphical syntax (e.g., a graphical user interface),
considers IoT features, incorporates microservices for IoT,
focuses on the healthcare or AAL domain, aligns with a
technical standard or architectural reference, whether the tool
has been subjected to experimentation or evaluation, and
provides evidence or considerations for efficiency, scalability,
and usability of the DSL.
Qin and Li [19] emphasize the advantages of DomainSpecific Language Models (DSLMs) in healthcare, showcasing their precision and adaptability in improving clinical
decision-making and patient care through tailored data.
Similarly, Arcadela [20] introduces a textual DSL for
Clinical Pathways (CPs), demonstrating its expressiveness
and usability to capture complex workflows while fostering
collaboration between medical and technical experts.
In the context of microservices, works such as MaGiC [21]
and MSSL [22] highlights frameworks designed to streamline
FIGURE 3. Spring Cloud Netflix Microservices Architecture. Adapted [14].
TABLE 1. Related DSLs Features ( : addressed; $: partially-addressed; #: non-addressed).
development processes. MaGiC incorporates interconnected
DSLs to define microservices, interfaces, and communication
layers, simplifying application deployment. Meanwhile,
MSSL focuses on integrating microservices with low-code
development, enabling non-technical stakeholders to actively
contribute to software creation. Other contributions, such
as Silvera [24] and DSL4CMSD [23], further enhance
microservices design by supporting modularity, scalability,
and integration with established standards. Silvera excels
in architecture evaluation and code extensibility, while
DSL4CMSD simplifies domain-specific requirements in
automation systems, validated through industrial applications.
For IoT, DSL-driven frameworks like SimulateIoT [25]
and ML-SLA-IoT [27] show the versatility of DSLs in
managing complex multi-layered environments. SimulateIoT
and its extension, SimulateIoT-FIWARE [26], leverage
graphical metamodels and real-time processing for scalable
simulations, including some Microservices approaches. MLSLA-IoT innovatively integrates blockchain-based smart
contracts to manage SLAs, emphasizing modularity and
QoS compliance. Finally, Sneps-Sneppe and Namiot [30]
propose a web-based DSL oriented to IoT, focusing on
reducing complexity and improving modularity in Smart City
applications.
These works collectively demonstrate the adaptability of
DSLs across diverse domains. However, these DSLs for IoT
and microservices (i.e., [19], [20], [21], [22], [23], [24],
[25], [26], [27], [28], [29], [30]) have addressed use cases
ranging from general device management to cloud-centric
deployments, their release and presentation have skipped
certain aspects, as shown in Table 1.
A GUI is not common among these DSLs because they
generally rely on code, given their developer-centric focus
and direct applicability. However, providing a GUI can
be advantageous when presenting the tool to end users,
as it enhances adaptability and applicability. Alignment with
existing standards is another weak point in most of the
related work, despite the fact that standards can offer a solid
foundation for a DSL’s core architecture. Many of these
studies address efficiency primarily by reducing development
overhead (e.g., fewer code lines or simpler domain-specific
modeling).
Scalability tends to be addressed by highlighting how
the tools can support large numbers of devices or services,
or by discussing the potential to extend the presented
DSL, suggesting that most are capable of scaling. Finally,
usability is typically supported by limited evidence (e.g., code
reduction, simplified syntax, easier maintenance) or smallscale demonstrations; only a few works report user surveys,
and most do not carry out rigorous usability studies or employ
established evaluation frameworks. Consequently, the overall
evaluation process often centers on specific case studies,
omitting controlled experiments or in-depth user-centered
evaluations.
Therefore, none have specifically targeted the AAL
domain by leveraging a cohesive, industry-standard microservices architecture like Spring Cloud Netflix. Moreover, they
also tend to lack direct integration with other domain-specific
modeling tools aligned to AAL (i.e., FOGAAL [12]), nor
do they provide an empirical user-centric evaluation (e.g.,
a controlled quasi-experiment) to assess user acceptance.
MICAAL aims to fill these gaps by:
i) Adopting a metamodel aligned with Spring Cloud components (e.g., Eureka, Zuul, Ribbon), ensuring reusability,
scalability, and fault tolerance for microservices in AAL.
ii) Designing a tool that will later complement FOGAAL
in a unified ecosystem of DSLs for IoT/AAL, thereby
enabling developers to design both Fog and microservices
architectures in a single environment.
iii) Providing empirical evidence of its perceived usability
and acceptance via the TAM, distinguishing it from prior
approaches that usually skip systematic user feedback.
By combining these elements, MICAAL represents a
unique and comprehensive approach to designing, validating,
and deploying microservices architectures for AAL, bridging
the gap between existing IoT DSLs and the specialized needs
of healthcare-focused, multi-layered (Edge, Fog, Cloud)
environments. This paper therefore builds on existing efforts
by presenting MICAAL as a microservices-focused DSL
specifically tailored to address the demands of IoT devices in
AAL systems, while aligning with the Spring Cloud Netflix
microservices architecture.
IV. MICAAL: A DOMAIN-SPECIFIC LANGUAGE TOOL FOR
ARCHITECTING MICROSERVICES IN AAL
This section introduces the MICAAL DSL, designed to
model microservices architectures for IoT devices in AAL
solutions by leveraging the Spring Cloud Netflix framework. It simplifies the management of IoT microservices
components in AAL domains through a standardized architecture that ensures robust domain abstraction. Built using
Model-Driven Engineering (MDE) principles [32], [33],
MICAAL is developed in Java Eclipse IDE, complemented
by Obeo Designer from the SIRIUS project [34]. This
setup enables automatic code generation and graphical
representations [35], [36].
TABLE 2. MICAAL DSL graphical notation.
A. MICAAL METAMODEL
This subsection introduces the MICAAL metamodel, which
is central to constructing the DSL. Figure 4 illustrates
the metaclasses, attributes, and relationships of MICAAL’s
model, aligned with the Spring Cloud Netflix Microservices
Architecture [13], [14]. This alignment facilitates the integration of microservices for IoT devices within a cohesive
abstract syntax, covering devices, servers, connections and
core elements from the Spring Cloud Netflix. The primary
metaclasses are described below.
1) ARCHITECTURE
Represents the project containing the microservices architecture. See Figure 4 (1).
2) CONTAINER
Represents the infrastructure that hosts the microservice(s)
to be deployed. Also, the container class has been introduced
to facilitate the integration of containers with customizable
features defined by the user and specific libraries that enable
their efficient implementation. This class provides a flexible
structure that meets current needs and fosters continuous
innovation. By incorporating this capability, the DSL ensures
it is not bound to specific technologies at its creation,
allowing it to evolve and remain relevant in the long term.
See Figure 4 (2).
3) LOADBALANCER
Enables balanced consumption of a service among several
deployed instances of the same service. See Figure 4 (3).
FIGURE 4. MICAAL Metamodel.
4) CIRCUITBREAKER
An automatic switch that implements the circuit breaker
pattern, allowing for the construction of a resilient and faulttolerant system. It ensures correct operation even when key
services are unavailable or experience high latency due to
heavy demand. See Figure 4 (4).
5) LOGMANAGEMENT
Manages application logs. This component provides a unified
view of all log data, offering real-time insights into the
deployed applications. See Figure 4 (5).
6) EDGEFOGSERVER
A component that acts as a gateway, exposing the services to
be consumed. See Figure 4 (6).
7) MICROSERVICE
An abstract class that encompasses all components of a
microservice, including configuration, authorization, registry, and service domain. See Figure 4 (7).
8) CONFIGURATIONSERVICE
An element that centralizes and remotely provides configuration for each microservice. For example, configurations can
be stored in a cloud repository for centralized management
See Figure 4 (8).
9) AUTHORIZATIONSERVICE
An architectural component that implements the security
layer for services. See Figure 4 (9).
10) REGISTRYSERVICE
A centralized service providing the endpoints where services
can be consumed. See Figure 4 (10).
11) DOMAINSERVICE
A component dedicated to serving real-world elements,
such as IoT devices in AAL. The domain specifies the
requirements and acceptance criteria for the system to be
implemented by developers. See Figure 4 (11).
12) LINK
This abstract metaclass provides the path attribute and
properties for all its subclasses in the microservices
architecture (e.g., EdgeFogServer and ConfigurationService,
EdgeFogServer and AuthorizationService, EdgeFogServer
and RegistryService, EdgeFogServer and DomainService,
RegistryService and DomainService). The subclasses inherit
these attributes and relationships from Link, enabling communication between components. See Figure 4 (12-17).
13) DOMAIN DEVICE
Represents the domain device, i.e., the device in the assisted
living environment that requires microservices. Information
flows between devices and microservices via the Application
Protocol attribute, which can use specific types (e.g., MQTT,
CoAP, HTTP, WAMP, AMQP, XMPP) and data formats
(e.g., HTML, XML, Binary, HL7, JSON, OWL, RDF). See
Figure 4 (18, 20, 21).
14) DEVICE
Represents the physical device itself, which is associated
with the Domain Device class to utilize microservices. See
Figure 4 (19).
B. MICAAL DSL TOOL
Similar to FOGAAL DSL [12], the Graphical User Interface
(GUI) is a central feature of MICAAL DSL. Using Obeo
Designer, the required models are generated efficiently, and
the graphical syntax is implemented within the Graphical
Modeling Framework (GMF) [36]. The iconography of
MICAAL DSL components aligns with the design characteristics of FOGAAL, as detailed in Table 2, ensuring seamless
integration with the metamodel code for the GMF generation.
C. INTEGRATING MICAAL WITH FOGAAL
MICAAL DSL has been designed as a complementary
module for FOGAAL DSL. Both address different, but
complementary layers of AAL design: FOGAAL models
Fog and Edge devices resources (e.g., Fog Nodes, Devices,
and Cloud connectivity) [12], whereas MICAAL focuses on
modeling microservices oriented to IoT devices. Integrating
both DSLs, can provide developers advantages like to unify
the physical and network-level design (via FOGAAL) with
the microservices layer (via MICAAL).
Conceptually, FOGAAL’s IoT or FogDevice classes (see
Figure 3 in [12]) can align with MICAAL’s Device, DomainDevice or Container classes, ensuring that each Fog resource
has a corresponding microservice. In practice, this could be
achieved through model transformations that automatically
link the device specifications in FOGAAL to microservice
definitions in MICAAL. Although each DSL has been
developed independently, a future merging metamodel can
support consistent updates between the two. The aim is
to offer a modeling solution in which AAL architects can
specify hardware topology and network constraints with
FOGAAL, then model the required microservices using
MICAAL.
V. ARCHITECTING MICROSERVICES USING MICAAL
This subsection introduces the use of MICAAL for designing
microservices for IoT devices in the AAL context. It begins
with an extension of the process flowchart from [12], which
aligns with the Systems Process Engineering Metamodel
(SPEM) specification [37]. This extended flowchart (see
Figure 5) illustrates the steps involved in utilizing MICAAL.
Following this, an experimental scenario demonstrates the
practical application of MICAAL by adhering to this
process.
Figure 5 extends the original process for designing AAL
architectures with Fog Computing using the FOGAAL DSL
(highlighted in the dotted line) as presented in [12]. It incorporates additional stages specific to designing microservices
architectures based on the Spring Cloud Netflix framework,
related to the new MICAAL DSL module.
The process of designing AAL architectures using the
FOGAAL DSL consists of four key stages [12]. First, AAL
requirements are collected, encompassing main environmental features and sub-environments. These requirements
are then translated into technical specifications, identifying
necessary hardware (e.g., sensors, actuators) and network
needs. The third stage involves selecting and defining
hardware elements using the FOGAAL DSL tool palette
based on the specified requirements. Finally, the AAL
and network architecture is designed, integrating hardware
representations, network features, and data flows into a
cohesive output artifact facilitated by the FOGAAL DSL
tool [12].
The process for designing microservices architectures
in MICAAL follows a similar structure but introduces
significant distinctions. This process includes the following
stages:
• Stage 1: Collect AAL requirements. This stage
involves gathering AAL requirements, emphasizing critical needs that help identify the required
microservices.
• Stage 2: Translation to technical requirements. The
AAL architect translates the gathered requirements
into technical specifications, identifying hardware (e.g.,
IoT devices), network requirements, and microservicesspecific needs based on their expertise.
• Stage 3’: Selecting microservices elements in the
MICAAL DSL palette. At this stage, the defined
microservices requirements are used to select and
represent microservices elements within the MICAAL
DSL palette.
• Stage 4’: Designing Microservices Architecture for
AAL. In the final stage, the AAL architect uses the
microservices representations in MICAAL DSL to
design the microservices architecture. This step enables
specifying microservices features for the IoT devices
such as load balancers, circuit breakers, and containers.
A. EXPERIMENTAL SCENARIO: APPLYING MICAAL DSL TO
AN AMBIENT ASSISTED LIVING SOLUTION DESIGN
This subsection demonstrates the application of the MICAAL
DSL in a specific AAL experimental scenario. It highlights
the need for effective microservices architectural solutions
for IoT devices within an AAL environment. The experimentation follows the stages outlined in Figure 5, providing
FIGURE 5. Process to design AAL Microservices Architectures.
a structured roadmap to design a suitable microservices
architecture for the scenario, using MICAAL.
AAL Requirements Collection: The proposed AAL scenario involves a hospital that allocates a space to establish
an assisted living environment to support elderly patients
with various dementia and health issues. This elderly care
center requires three dedicated rooms: a general medical
department, a physiotherapy room, and a cognitive stimulation room. Each department is equipped with specialized
sensors and medical devices that require high-performance
services (i.e., microservices) to conduct the center’s medical
procedures and therapies. Figure 6 outlines the specific
technical requirements for each department.
Transformation to AAL Technical Requirements: After
collecting the AAL requirements specified in Figure 6, the
technical microservices requirements for for each environment are defined as follows:
1) MAIN ENVIRONMENT (M1)
The main environment (M1) represents the elderly care
center, encompassing the entire AAL architecture and
including three sub-environments: E1 (Medical Department),
E2 (Physiotherapy), and E3 (Cognitive Stimulation). The
required microservices components for M1 are:
• Main Service. Hosted on a primary edge server (e.g.,
Zuul), it acts as the core controller for all microservices
within M1.
• Authentication Service. This service ensures secure
access to the microservices in M1.
• Registry Service. The registry service (e.g., Eureka)
manages connections between IoT devices in E1, E2,
FIGURE 6. Experimental scenario, general requirements description.
and E3 and the microservices. It facilitates device
registration and directs requests to the edge server (i.e.,
Zuul).
2) ENVIRONMENT (E1)
The E1 environment represents a Medical Department and
includes the following IoT devices requiring dedicated
services for proper operation:
FIGURE 7. Microservices Architecture with MICAAL.
• Vital Signs Device. Monitors patients’ vital signs such
as blood pressure, electrocardiogram (ECG) signals, and
oxygen saturation.
• Medical Record Device. It is a computer system
managing patients’ Electronic Health Records (EHR).
• Medication Management System. Consists of a tablet
and an Intelligent Pillbox [38], [39], setting, monitoring
and tracking patient medication.
3) ENVIRONMENT (E2)
The E2 environment is a Physiotherapy Room equipped with
the following IoT devices and systems requiring dedicated
domain services:
• Balance Measurement System. Includes a Raspberry
Pi [40] and AALADIN [41] help medical staff analyze the Tinetti test’s balance sub-scale for elderly
patients.
• Vital Signs Measurement Devices. This system is
composed by three smartwatches monitoring vital signs
like blood pressure and oxygen saturation.
• Balance Therapy Device. A low-cost photo-podoscope
system [42], [43], [44] used to assist in balance therapy.
4) ENVIRONMENT (E3)
The E3 environment is a Cognitive Stimulation Room
containing the following IoT devices and systems requiring
dedicated domain services:
• Memory Training System. A Stroop-based device [45]
with eye trackers and visual boards for administering
tasks and analyzing responses [45], [46].
• Serious Games System. Consists of three tablets
providing access to memory training games [47] and
MOOCs designed for elderly patients [48].
• Attention Trainning System. This system is composed
by a device running VitaApp [49], [50], an augmentative
and alternative communication system using pictograms
oriented to older adults.
5) ADDITIONAL REQUIRED FEATURES
The following features are necessary for the containerized
microservices:
• Main Service Container includes components for load
balancing (Ribbon), circuit breaking (Hystrix), and log
management (Loggly).
• Register Service Container includes components for
load balancing (Ribbon), circuit breaking (Hystrix), and
log management (Loggly).
• Authentication Service Container. includes components for load balancing (Ribbon), circuit breaking
(Hystrix), and log management (Loggly).
• Sub-environment Containers (i.e., E1, E2, E3)
include load balancing (Ribbon) and circuit breaking
(Hystrix).
a: AAL AND NETWORK ARCHITECTURE DESIGN
Figure 7 illustrates the resulting AAL microservices architecture designed fot this experimental scenario by using the
MICAAL DSL, based on the specified requirements. The
tool palette elements were used to model the architecture
comprehensively, with each container configured to include
the required components and their respective connections.
b: THE IMPACT OF MICAAL IN REAL-WORLD AAL
As shown in this experimental real-world AAL scenario,
it integrates heterogeneous devices presenting challenges
such as: i) ensuring reliable communication across various
protocols, ii) managing data streams in diverse formats,
and iii) customizing services per device and environment.
The abstraction provided by a DSL simplifies modeling
this heterogeneity. While FOGAAL addresses the first two
aspects [12], MICAAL covers service customization (i.e.,
microservices).
MICAAL addresses this challenge providing a domainspecific abstraction that standardizes the design, configuration, and deployment of microservices aligned to each
device across different environments and sub-environments
in an AAL system. Leveraging standardized components, like
those in the Spring Cloud Netflix microservices architecture,
MICAAL enables rapid IoT devices modeling (e.g., prototypes and sensors) and critical microservices components
(e.g., load balancers, circuit breakers, and logging services).
This enhances scalability and interoperability in heterogeneous, fault-tolerant, and highly available environments,
essential for real-time monitoring.
MICAAL also facilitates defining a clear microservices
architecture, where each function (e.g., vital signs measurement, medical data analysis, user authentication) is modeled
as an independent service. This modular approach reduces
complexity and simplifies future device integration.
Although the presented scenario includes only three
sub-environments, MICAAL supports scalable solutions,
accommodating additional devices and sub-environments as
needed.
In summary, this experimental scenario highlights how
MICAAL reduces complexity and enhances interoperability
in practical AAL solutions.
VI. EMPIRICAL EVALUATION OF MICAAL DSL
Empirical evaluation is essential for determining the usability,
effectiveness, and user adoption of DSLs [51], [52], [53].
This section validates the MICAAL DSL tool, employing
a process similar to the one used for FOGAAL DSL [12].
The focus is on evaluating its ease of use, usefulness,
and end-users’ intention to adopt MICAAL for modeling
microservices architectures in AAL through a controlled
quasi-experiment based on the TAM framework [17].
TAM provides key constructs for understanding technology adoption (See Figure 8): Perceived Ease of Use
(PEOU), Perceived Usefulness (PU), Attitude (A), Behavioral Intention to Use (ITU), and actual Use [17]. PEOU
evaluates the effort required to use the tool, while PU assesses
its impact on performance. These factors influence user
attitudes, intentions, and behavior, forming the foundation for
analyzing MICAAL’s adoption potential.
FIGURE 8. TAM constructors [17].
A. DESIGN OF THE QUASI-EXPERIMENT
The quasi-experiment design to be applied to end-users
involves the following tasks: i) Defining the goals and
research questions; ii) Establishing hypotheses based on the
TAM perception variables or constructs; iii) Adapting the
questionnaire to measure these variables in the context of
MICAAL DSL; and iv) Defining the experimental scenario,
tasks, and materials. Each task is detailed below:
1) GOAL AND RESEARCH QUESTIONS
The main goal of the quasi-experiment is formulated following the Goal-Question-Metric (GQM) framework proposed
by Basili et al. [54] (See Table 3).
TABLE 3. Goal-Question-Metric for the quasi-experiment.
The research questions are defined based on the TAM’s
perception variables or constructs (see Table 4).
TABLE 4. Research questions for the quasi-experiment.
2) HYPOTHESES
The hypotheses are designed to evaluate the research
questions outlined in Table 4, and are presented in Table 5.
Hypotheses H10, H20, and H40 address the first research
question, while H30 and H50 pertain to the second. The
evaluation process involves testing the null hypotheses, each
of which incorporates the TAM perception variables (PEOU,
PU, ITU).
3) QUESTIONNAIRE TO MEASURE TAM PERCEPTION
VARIABLES
Table 6 presents the adapted questionnaire to measure the
TAM perception variables in MICAAL, as follows:
TABLE 5. Hypotheses for the experiment.
• Fourteen questions were designed to be answered
using a 5-point Likert scale (3 as neutral value).
Respondents use this scale to evaluate the technological
solution.
• The questionnaire includes five questions on PEOU, six
on PU, and three on ITU.
• Two open-ended questions are also included in the
questionnaire to gather participants’ feedback on the
technological solution.
• Additionally, some questions are intentionally reworded
or repeated to strengthen the reliability of our measurement instrument. This practice helps cross-check the
consistency of participants’ responses, detect potential
acquiescence or inattentive answering, and ultimately
reduce bias in the questionnaire’s results.
4) DEFINE THE EXPERIMENTAL SCENARIO, TASKS, AND
MATERIALS
The final phase of the quasi-experiment involves defining
the scenario, tasks, and materials required for its effective
execution with the experimental group.
• Participants. The experiment involved 30 software
engineers with expertise in MDE, IoT, and microservices. The selection of the sample size and type is similar
to the one used in the FOGAAL quasi-experiment [12].
The selection of domain experts strengthens the sample
selection, with the number of 30 falling within a
medium effect size while still providing reliable insights
into user perception and maintaining feasibility. This
approach offers a balance between practical constraints
to locate a large number of experts to perform the
quasi-experiment and statistical validity and statistical
validity [55], [56].
• Location. The experiment was conducted in a computer
lab at the Universidad de Cuenca, equipped with desktop
computers meeting the following minimum specifications: Intel Core i5-10500 processor or equivalent,
8-12 GB RAM, and Windows 10. Each computer
was pre-installed with the Eclipse IDE and Obeo
Designer plugins to support MICAAL’s deployment and
execution.
• Materials. All experimental materials were provided
digitally, including documentation on MICAAL’s technical concepts, a step-by-step microservices architecture
design guide following the Figure 5 process, a worksheet
detailing the requirements for the experimental scenario,
and a link to the final questionnaire (Table 6).
• Proposed Experimental Scenario. Participants were
tasked with modeling a microservices architecture for
IoT devices in an AAL environment oriented to children
with special needs, as detailed in Figure 9.
FIGURE 9. AAL scenario for the quasi-experiment, general needs.
Figure 9 presents the general needs of the main scenario of
the Special Needs Children’s Center (M1) containing three
sub environments: Physiotherapy (E1), Early Stimulation
(E2), and Autism Stimulation (E3). Each sub-environment
includes specific devices and services requiring dedicated
attention. The detailed microservices requirements provided
to the experimental subjects are shown in Figure 10.
A complete architecture is required, including an edge
server, load balancers, registry services, circuit breakers, log
management, and an authentication service. Additionally, the
AAL and each sub-environment must be summarized, with a
dedicated service for each device in the environment due to
their criticality.
B. EXECUTION OF THE QUASI-EXPERIMENT
The quasi-experiment session in Universidad de Cuenca
lasted two hours and was divided into two stages.
During the first hour, participants attended a class covering
foundational concepts such as Ambient Intelligence (AmI),
AAL, IoT, microservices (with a focus on the Spring Cloud
Netflix architecture), and DSLs. The MICAAL DSL tool was
then introduced, including its metamodel, design environment, and tools palette. Following this, the AAL scenario
described in Section V (see Figure 7) was demonstrated
as an example of the tool usage. Finally, a discussion
was held.
The second hour started with an overview of the microservices requirements for the AAL scenario to be developed
by the participants (see Figures 9, 10). The participants
proceeded to design the microservices architecture using
TABLE 6. Questionnaire adapted to MICAAL DSL.
FIGURE 10. General Microservices Requirements.
MICAAL DSL, following the process described in Figure 5.
The tasks were timed: 10 minutes to gather system requirements, 15 minutes to diagram components using the tool, and
10 minutes to complete the survey (see Table 6).
C. RESULTS OF THE QUASI-EXPERIMENT
This subsection details the outcomes of the quasi-experiment,
focusing on the TAM perception variables (e.g., PEOU,
PU, ITU) and their hypothesis tests. The analysis was
conducted in IBM’s SPSS v2.0 software. In line with
Moody’s guidelines [57], significance levels were employed
to evaluate the acceptance or rejection of the hypotheses.
1) ANALYSIS OF THE USER PERCEPTION
Figure 11 presents the box plots for the constructs (i.e.,
PEOU, PU, ITU). As shown, all variables are positioned
above 3, the neutral point on the Likert scale. The participant
4 as outlier is removed for further analysis.
FIGURE 11. Box diagram for TAM constructors: PEOU, PU, ITU.
Table 7 presents the descriptive statistics for the TAM
perception variables (i.e., PEOU, PU, ITU), along with
the results of the Shapiro-Wilk test (suitable for samples
under 50) and a one-tailed t-test. The Shapiro-Wilk test
confirmed that all three variables follow a normal distribution
(p>0.05). Consequently, a t-test was conducted to compare
the variables against the neutral value of three, evaluating the
null hypotheses H10, H20, and H30. The results, shown in
the last column, indicate the rejection of all null hypotheses,
suggesting that participants perceive the MICAAL DSL as
easy to use and useful, and are inclined to consider using
it in the future for designing microservices architectures
for AAL.
TABLE 7. Results of the TAM perception variables (PEOU, PU, ITU).
2) ANALYSIS OF CAUSAL RELATIONSHIPS
This subsection validates the TAM’s structural aspect by
analyzing the causal relationships between its perception
variables. Simple linear regression was used to test the
hypotheses H40, H50, and H60, as they involve causal
relationships between continuous variables. The analysis and
results results are presented below:
• Perceived Ease of Use vs Perceived Usefulness. The
simple linear regression model used to test hypothesis
H40 considers PEOU as the independent variable
(predictor) and PU as the dependent variable (predicted).
The resulting regression equation is:
PU = 0.057 + 0.970 ∗ PEOU (1)
The regression model was found very higly significant,
with p<0.001 (see Table 8). Furthermore, the R2
statistic
shows that the PEOU variable can explain 48.2%.
These results reject the H40 since PEOU determine
the PU.
TABLE 8. Simple linear regression model between perceived ease of use
and perceived usefulness.
• Perceived Ease of Use vs Intention to Use. The simple
linear regression model constructed to test hypothesis
H50 employs PEOU as the predictor and ITU as the
predicted. The resulting regression equation is:
ITU = 0.544 + 0.917 ∗ PEOU (2)
The regression model was found to be very highly significant, with p<0.001 (see Table 9). Furthermore, the
R
2
statistic indicates that the PEOU variable can explain
41.5% of the ITU variance, suggesting that PEOU
does not significantly influence participants’ future ITU.
Therefore, these results reject H50 and accepting its
alternative hypothesis. Thus, it is empirically confirmed
that PEOU influences the ITU.
TABLE 9. Simple linear regression model between perceived ease of use
and intention to use.
• Perceived Usefulness vs Intention to Use. The simple
linear regression model was constructed to examine
hypothesis H60, with PU as the independent variable and
ITU as the dependent variable. The resulting regression
equation is presented as follows.
ITU = 1.480 + 0.686 ∗ PU (3)
The regression model was found to be very highly
significant, with p < 0.001 (refer to Table 10).
Additionally, the R2
statistic indicates that the PU
variable accounts for 45.2% of the variance in ITU,
suggesting that the perceived usefulness by participants
influences on their intention to use the tool. These
findings lead to the rejection of H60 and acceptance of
its alternative hypothesis, indicating that PU does indeed
influences ITU.
TABLE 10. Simple linear regression model between perceived usefulness
and intention to use.
D. DISCUSSION
Based on the results from the quasi-experiment, the following
general conclusions are drawn for each research question
(e.g., RQ1, RQ2):
RQ1: ‘‘Is the MICAAL DSL perceived as easy to use
and useful?’’ Through the evaluation, alternative hypotheses
H1, H2 and H3 are validated through the rejection of them.
This provides support to determine that most participants
have found MICAAL DSL easy to use and useful when
designing microservices architectures for IoT devices in AAL
environments. Besides, there is intention to use this tool in the
future.
RQ2: ‘‘Is there an intention to use the MICAAL DSL
in the future? If so, is the intention to use the result of
the user perception.’’ The evaluation has shown that there is
influence between users’ perceived ease of use influences the
perceived usefulnes and the intenton to use (i.e., H4 and H5).
Similarly, the perceived usefulness influences the intention to
use MICAAL (i.e., H6).
Finally, the results concerning the empirical evaluation are
condensed in Figure 12.
E. THREATS TO THE VALIDITY OF THE
QUASI-EXPERIMENT
This subsection examines potential threats to the validity
of the evaluation results, categorized following Cook and
Campbell’s classification [58].
1) INTERNAL VALIDITY
Threats included participants’ experience, researchers’
biases, experimental material, and the MICAAL DSL tool.
FIGURE 12. MICAAL’s empirical evaluation results summary.
A pre-training exercise using MICAAL and a pilot test
involving domain experts mitigated these risks by addressing
ambiguities and errors.
2) EXTERNAL VALIDITY
The main threat was the representativeness of results,
influenced by the evaluation design and participant context.
This was mitigated by proposing a diverse AAL scenario and
involving software engineers experienced in microservices
architectures, Model-Driven Development, and IoT.
3) CONSTRUCT VALIDITY
The key threat was the reliability of the questionnaire.
Cronbach’s alpha reliability tests, with values above the
acceptance threshold (α = 0.70), confirmed reliability:
0.804 for PEOU, 0.754 for PU, and 0.793 for ITU.
4) CONCLUSION VALIDITY
Conclusion validity concerns primarily involved the quasiexperiment’s sample size. Selecting a homogeneous participant group and standardizing procedures to execute the
experimentation process as well as calculating dependent
variables mitigated this risk.
F. USER FEEDBACK AND INSIGHTS
As the last two questions in Table 6 were open-ended,
we gathered qualitative feedback from users regarding
their experiences and impressions of using MICAAL. The
following insights are drawn for each open question (e.g.,
OQ1, QQ2):
QQ1: ‘‘Do you have any suggestions to make the
MICAAL DSL tool for modeling microservices architectures for IoT devices in AAL easier to use?’’ Users
highlighted several areas where MICAAL could be improved
for ease of use. A key suggestion was enhancing the GUI with
more intuitive drag-and-drop functionalities, tooltips, icon
enlargement, and real-time validation to guide users during
model creation. Additionally, users expressed the need for
better documentation or a user manual, including step-by-step
tutorials. Some users recommended auto-generation features
(e.g., configuration files) to enhance implementation. The
integration of real-time feedback mechanisms, such as
warnings or suggestions for optimizing microservices composition, was also suggested to improve modeling efficiency.
Lastly, expanding the library of predefined microservice
components and offering adaptive customization options
would enhance flexibility and usability, particularly for
users new to microservices architecture design in AAL
environments.
OQ2: ‘‘What are your reasons for intending or not
intending to use the MICAAL DSL tool for modeling
microservices architectures for IoT devices in AAL in the
future?’’ Users intending to adopt MICAAL DSL highlighted its structured approach, intuitive interface, and modularity, which enhance microservices modeling efficiency.
Its alignment with Spring Cloud Netflix as a standardized
approach was also noted. However, concerns were raised
about its usability for non-experts and the lack of direct code
generation.
Overall, the user feedback and insights given by OQ1
and OQ2 serve as a guide of parameters that should be
carefully evaluated to incorporate for refining MICAAL by
incorporating user-driven improvements to enhance usability, functionality and the adoption of the tool for such
context.
VII. MICAAL DSL ADVANTAGES AND LIMITATIONS
MICAAL DSL is a notable contribution to the modeling
of microservices in AAL offering remarkable advantages.
As an extension of FOGAAL, it demonstrates the modularity
and extensibility of DSLs, providing a domain-specific
characterization aligned to microservices in AAL, ensuring
its features align with the unique requirements of IoT
devices in these environments. Built on the Spring Cloud
Netflix microservices framework, MICAAL provides a high
level of abstraction that allows domain experts to easily
design scalable, modular solutions. Its standardized language
fosters interoperability, streamlining communication among
developers of such solutions and supporting integration
across healthcare systems. This alignment with established
frameworks ensures reliability, coherence, and trust in the
solutions created. Besides, MICAAL design prioritizes costefficiency. Developed using free Modeling Tools, its implementation involves no licensing costs, making it accessible
to a wide range of developers. While the initial development
required considerable effort, the model-driven approach
ensures that subsequent modifications are straightforward
and cost-effective.
Beyond AAL, MICAAL’s modular design and standardized microservices framework make it adaptable to various
IoT-driven domains. Its current version can be extended
and adapted to model microservices in smart healthcare
applications (e.g., remote patient monitoring), as well as
other IoT domains such as industrial IoT (e.g., predictive
maintenance) and smart cities (e.g., intelligent transportation
systems), where scalable and interoperable microservices are
essential. Also, this DSL abstracts microservices for IoT
devices, allowing it to be complementary to other description
languages like FOGAAL in this case, but also to others like
TOSCA (Topology and Orchestration Specification for Cloud
Applications) [59] to extend its deployment capabilities
and enable the automated orchestration of microservices
architectures. In this regard, future efforts will be important in
exploring these extensions, ensuring that MICAAL remains
a versatile tool for IoT applications beyond its original scope
in AAL.
Despite its advantages, MICAAL faces certain challenges
and opportunities for refinement. Its high-level abstraction
currently omits support for specific IoT device artifacts,
limiting its application for highly specialized use cases.
Addressing this limitation will require extending the metamodel to incorporate specialized technologies tailored to
niche requirements. Another area for improvement lies in
enhancing code generation capabilities. By transforming
models into executable code, MICAAL could streamline the
development process further, eliminating the need for manual
coding and increasing its appeal to developers.
Finally, integrating MICAAL and FOGAAL into a
unified framework presents an opportunity to deliver a
comprehensive tool for modeling AAL solutions. Such an
integration would combine the strengths of Fog Computing
and microservices, offering a holistic approach to designing
scalable, adaptive, and efficient AAL environments.
VIII. CONCLUSION AND FURTHER WORK
This paper introduces MICAAL, a DSL designed to complement FOGAAL by focusing on modeling microservices architectures for IoT devices in AAL environments.
MICAAL incorporates the characteristics of IoT devices
in such contexts, integrating the Spring Cloud Netflix
microservices framework. By leveraging this framework,
MICAAL addresses challenges such as interoperability, heterogeneity, and scalability, enabling the seamless integration
of microservices into critical domains like AAL.
MICAAL has demonstrated its utility in designing adaptable microservices architectures aligned to the requirements
of AAL systems in two key instances. First, in Section V,
a case study illustrated how MICAAL successfully modeled
a microservices architecture solution for a given AAL scenario. Second, in Section VI, a controlled quasi-experiment
involving 30 participants with backgrounds in microservices,
and IoT showcased MICAAL’s user acceptance. The positive
outcomes from this quasi-experiment, evaluated through the
TAM, provided valuable insights for MICAAL developers,
highlighting its perceived ease of use, perceived usefulness,
and intention to use, and therefore its potential to impact
microservices modeling practices in the AAL domain.
It is important to emphasize that MICAAL complements
FOGAAL, and future work will focus on integrating these
two DSLs to develop comprehensive IoT solutions for AAL
by combining Fog Computing and microservices architectures. These integrations shall include an extended evaluation
model considering formal metrics of efficiency or effectiveness. Moreover, given MICAAL’s possibility to adapt to
other IoT-driven domains, future research will explore its
integration with other description languages such as TOSCA,
expanding its applicability beyond AAL. This extension will
also involve evaluating its scalability and interoperability
in diverse IoT environments. Additionally, as discussed
in the Related Work (Section III), a comparative analysis
against related solutions underscores MICAAL’s strengths in
addressing the specific challenges of this domain. However,
future efforts will aim to refine the current solution further,
particularly in developing model-to-code transformations to
facilitate integration and deployment of diverse architectural
solutions.
In conclusion, MICAAL represents a significant advancement in the field of AAL, bridging the gap between highlevel design and real-world implementation of microservices architectures. By focusing on modularity, scalability,
and interoperability, MICAAL offers a robust tool for
researchers and practitioners to design innovative solutions
in AAL environments. Moving forward, its integration with
FOGAAL will further enhance its capability to support
the evolving needs of IoT applications in critical domains
like AAL.
