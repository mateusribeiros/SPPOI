Title: A hybrid actor- and microservices-based platform for scalable
smart building application deployment

Abstract
Digitalisation is an effective means to achieve proper building operation and support global decarbonisation goals. Yet buildings’
heterogeneity, lack of interoperability, and vendor lock-in pose
challenges to deploying data-driven applications at scale. In the
current state of practice, there is no clear separation between system integration and the deployment of smart building applications,
resulting in inefficient and non-scalable software components. This
paper proposes a reference architecture towards decoupling system
integration from application deployment, enabling the development
of a platform that standardises data descriptions and exchanges,
fosters interoperability, and allows scalable, vendor-agnostic deployment of smart building applications. The platform uses actor-based
and microservice design patterns and leverages semantic models
built on open standards-based ontologies. This approach enhances
scalability in developing software components that integrate and
manage heterogeneous data sources and facilitates the portability
of third-party applications across multiple buildings. The paper
outlines the successful implementation of the platform in two buildings, detailing the deployment of analytical and control applications
while offering insights into benefits, limitations and challenges.
CCS Concepts
• Information systems → Information systems applications;
Graph-based database models; • Software and its engineering
→ Abstraction, modeling and modularity.
Keywords
Smart Buildings, Scalability, Platform, Semantics, Controls, Brick
ACM Reference Format:
Flavia de Andrade Pereira, Kyriakos Katsigarakis, Nikos Kostis, and Dimitrios Rovas. 2024. A hybrid actor- and microservices-based platform for
scalable smart building application deployment. In The 11th ACM International Conference on Systems for Energy-Efficient Buildings, Cities, and
1 Introduction
Several countries worldwide are committed to ambitious climate
goals for 2030 and 2050, which has driven a transition toward
the digitalisation of buildings to improve and decarbonise their
operation [1, 18]. However, current technological infrastructure
advancements have led to a rise in complexity and heterogeneity
within smart building ecosystems, often resulting in custom, noninteroperable, and building-specific solutions [6, 13]. This creates
challenges for scalability and the widespread adoption of applications that improve energy management and meet occupant needs,
including fault detection and diagnostics analytics, and demand
flexibility controls.
The industry and research community have acknowledged the
potential of semantic models to support the scalability of building
applications. Semantic models built on ontologies such as Brick,
SAREF, and the upcoming ASHRAE 223 standard can provide a
uniform representation of buildings, their systems, devices, data
points and relationships in a standardised and machine-readable
manner [7]. A consistent metadata description allows for improved
interoperability and usability by enabling a common understanding
of the building context, facilitating the use of data from heterogeneous sources [2]. Semantic models also facilitate applications to
use consistent query mechanisms to discover and map building
data points while abstracting building-specific intricacies, such as
ad-hoc naming conventions. This enables the automation of the configuration of applications and ultimately improves their portability
across heterogeneous buildings [17].
With the increasing interest in semantic models, several commercial platforms and open-source efforts have been developed
to support them. These include many contemporary Energy Management and Information Systems (EMIS) and Building Operating
System (BOS) products, which are software layers built on top of
Building Automation Systems (BAS) that employ semantic models to facilitate point mapping and configuration of applications
[3, 7, 12]. The challenge is that these models are often built on proprietary ontologies, which are rarely standardised across different
vendors. As a result, integrating a new application from a different
EMIS/BOS product, even within the same building, still requires custom integration, making the process non-scalable [14]. To address
this, community-driven efforts, such as BOSS [4], Mortar [8] and
SeeQ [10], have proposed semantics-driven approaches for portable
applications using well-established, open ontologies. However, they
primarily support analytical applications using historical data from
their platforms and lack proper integration with infrastructure to
communicate with real buildings.
Other studies introduced solutions using semantic models built
on Brick, emphasising control applications and real-time data access. [11] presented a software stack called OpenBOS, providing a
scalable method for the self-configuration and deployment of control applications in an actual building. Meanwhile, [5] presented
a semantics-driven framework for supporting the portability of
demand flexibility control applications across different buildings.
Nevertheless, these studies do not detail the main software architecture components needed to create a platform supporting their
applications nor provide interfaces that can abstract their complexities for end users, such as application developers. The unavailability
of such platforms or user-friendly means to interface easily with
buildings within the academic context is one of the reasons why
many of the current studies are performed in simulation and not
validated in the real world.
This paper addresses this gap by proposing a reference architecture for a platform that supports flexible and scalable deployment
of smart building applications. It also presents a prototype of the
platform, developed as part of BuildON1
, an EU-funded project
that aims to provide affordable solutions to support the digitalisation, automation, and control of buildings across Europe. The
platform supports the connection with distributed data sources
(both historical and real-time data), instantiates semantic models in
an automated and dynamic way, and provides a means for decoupling analytic and control applications from specific buildings. To
promote scalability and widespread adoption, the platform follows
actor and microservices architectural design patterns [9] and offers
a user-friendly Graphical User Interface (GUI). This paper provides
a detailed overview of the platform, highlighting the functionalities
and implementation of its core software architecture components.
The remainder of this paper is organised as follows. Section 2
describes the methodology devised for the reference architecture.
Section 3 presents a prototype platform based on the architecture.
Section 4 presents a case study implementing the platform in a real
building. Section 5 describes the current limitations and challenges
of the platform. Section 6 discusses the main findings and outlines
concluding remarks and future research directions.
2 Methodology
The methodology adopted to guide the reference architecture specification and platform development proposed in this paper was
inspired by the iterative design science research [19] and the interaction design [16] approaches. It involved the culmination of
iterative refinements developed over a longer horizon to accommodate the complexities of several real-world buildings and use cases.
The architecture comprises four key software components: data
ingestion, data storage, data integration, and data management.
The specific functionalities of each component, along with their
integration with one another and diverse data sources (bottom
layer) and applications (upper layer), are illustrated in Figure 1.
Each component is described in the following sections, and a more
detailed specification of them and their interactions can be found
in the BuildON technical report [15].
Overall, three aspects are covered by this reference architecture:
1) time series data access and persistence via the data ingestion
component, 2) metadata management via the data ingestion, storage
and integration components, and 3) third-party applications’ unified
access to data from sources across multiple buildings via the data
management component. Maintaining consistency across all three
aspects is crucial to ensuring high-quality data, especially when
building changes occur.
2.1 Data ingestion
The data ingestion component is designed to configure, load and
process static (metadata) and dynamic (time series) data from various sources. These include data from Building Automation Systems
(BAS), Building Information Modelling (BIM) authoring tools, Internet of Things (IoT) platforms and external data sources (e.g.,
weather stations). To enable connectivity across different buildings, data connectors should be instantiated according to specific
data access and processing mechanisms. This includes configuring
global parameters (e.g., building identification), setting up communication channels (e.g., gateways using MQTT pub/sub-topics), and
establishing uniform payload formats with corresponding parsing
methods.
Once data connectors are configured, relevant metadata from
each connected data point should be registered, including attributes
such as the unique identifier, type (e.g., temperature sensor), unit
and associated equipment (e.g., thermostat). This is essential for
enabling the discovery of connected points and setting up data
processing and logging functions that ensure data quality before
transmitting to upper-layer components (e.g., data storage). These
functions may involve data validation, transformation, and alert
generation. For example, data processing operations can normalise
incoming data to standard units pre-defined for a specific point type,
or logging mechanisms can set triggers to detect anomalies, such
as data values falling outside the acceptable range for a particular
point type.
2.2 Data storage
A data broker moves dynamic data from the data ingestion component to the data storage component. This storage component hosts
various cloud-deployed databases, including time series databases
that can subscribe to designated topics within the broker to receive
measurements from BAS and IoT field devices. This component also
offers storage solutions for object and graph databases. The object
database supports a wide range of structured and unstructured data
types, such as IFC models, while the graph database stores semantic
models generated by the data integration component.
2.3 Data integration
The data integration component generates, enriches, and validates
semantic models (also referred to as knowledge graphs or graphs)
to represent buildings and their data. These models are essential for
enabling the integration and discovery of data points from heterogeneous sources by providing a shared context and standardised
meaning of data in a machine-readable format. The generation
process involves populating a given set of ontologies using buildings’ metadata and incorporating operational staff knowledge. To
streamline this process, this component employs a series of Extract,
Transform, and Load (ETL) tools dedicated to automating the generation of partial graphs from specific input sources, including the
metadata register from the data ingestion component, but also CSV
files and IFC models (see Figure 2).
The first partial graph is automatically generated from the ETL,
which handles point metadata registered in the data ingestion component. It provides an initial graph, dynamically creating nodes
for each new data point. This graph can then be enriched with
additional metadata by merging with the outputs from other ETL
tools that represent spatial and topological relationships based on
instantiated CSV templates and IFC models. This approach supports a range of complementary templates and ETL tools, providing
a modular and scalable solution for instantiating and enriching
semantic models with any available data source.
2.4 Data management
With the semantic models and data broker in place and the dynamic data properly stored, the data management component can
respond to requests from third-party applications. To achieve this,
applications should begin by defining their data requirements (e.g.
historical building-level energy measurements with hourly intervals for a specified time range). By allowing these data needs to be
specified using templates based on SHACL statements and ontology
patterns (e.g., brick:Building, brick:hasPoint, brick:Energy_Meter),
this component facilitates applications’ data requirements to be
machine-readable. This, in turn, facilitates the automated configuration of applications across different buildings.
For each defined subset of data requirements, corresponding
data collections can be automatically generated and made accessible through universal API endpoints. This automation is provided
by a query generator subcomponent, which dynamically coordinates the sequential execution of queries based on specified data
needs. In most cases, the corresponding responses require data from
different data sources of the data storage and ingestion component.
The first request is often made to the graph database using SPARQL
queries to retrieve the list of points and the required metadata to
access their values (e.g., foreign key, time series identifier, pub-sub
topics). Then other requests are performed to retrieve corresponding historical measurements from the time series databases (e.g.,
with predefined influxQL queries) or real-time data from the data
ingestion component (e.g., with broker subscription).
3 Implementation
To instantiate the reference architecture, we developed a platform
following an actor and microservices design patterns. The data
ingestion, integration and management components were implemented using the Spring framework. This enabled the implementation of a collection of loosely coupled, independently deployable
microservices with enhanced scalability, maintainability, and flexibility potential. The data integration and management components
were also implemented using the Akka framework, which enabled
actor-based modelling to facilitate modular and scalable deployment of functions as actors. The data storage component, while not
based on the Spring-Akka framework but instead on a standalone
application tailored for specific target platforms (e.g., InfluxDB and
GraphDB), is capable of efficiently interacting with other platform
components via configurable synchronous and asynchronous interfaces, including the broker within the data ingestion component.
Figure 3 presents a snapshot of an intuitive drag-and-drop interface provided by the platform to implement the graph generator ETL
tools from the data integration component while leveraging actors.
Each actor is an extensible program-code template containing configurable parameters that allow them to interact with external components, execute specific logic functions, and forward responses to
other actors using a lightweight messaging system. Based on given
needs, predefined actors can be imported, customised and wired
together to perform complex data operations.
Due to its architectural design and the strategic selection of
underlying technologies, the platform exhibits high levels of modularity, interoperability, efficiency, and reliability. Each of these
attributes is detailed as follows.
Modularity. The platform leverages advanced Spring framework
technologies, including Spring Boot, Spring Model-View-Controller
(MVC), and Spring Integration, along with Akka, to support the
creation and configuration of dynamic multiple modules (e.g., data
connectors) without impacting the runtime environment. This is
achieved through an extensible metamodel that enables developers to define global attributes, payload parsers, and schema versioning for each module. The platform also automates the conversion of modules’ graphical representations into actors by adhering
to the Modelling Markup Language (MoML) specification. This
approach standardises module definitions through reusable code
blocks, which can be encapsulated and deployed across multiple
Java Virtual Machines (JVMs) that communicate within a larger
ecosystem. These features facilitate the smooth integration of new
data sources and functionalities, ensuring platform scalability and
performance across diverse buildings and applications.
Interoperability. The platform focuses on four key strategies to
promote seamless interoperability. First, it supports the creation of
multiple connectors to ensure compatibility with various communication protocols. Second, it enforces message exchanges with the
broker to adhere to a consistent structure for topics and payloads.
This facilitates uniform parsing methods when communicating
with different data sources. Then, it allows graphs built on ontologies to be dynamically generated to represent heterogeneous
building data points in a consistent manner. Finally, the platform
provides applications with unified access to data across different
buildings via endpoints. This is achieved through a combination of
the Akka framework and a set of libraries that handle HTTP-based
interactions and enable the creation of communication channels
between actors. These actors can query building graphs to retrieve
points’ accessing information (once) and use them to dynamically
configure interfaces with time series databases for historical data
or message brokers for real-time data.
Efficiency. The platform relies on a combination of Akka, Spring,
InfluxDB, GraphDB, and data brokers such as Kafka and AMQP to
effectively handle, process, store, and access large volumes of data.
These are well-established frameworks and technologies, highly capable of managing large-scale data with low-latency requirements.
The platform also relies on an infrastructure for asynchronous communication and message-passing that aims to minimise response
time during data requests from third-party applications. For example, the platform enables scheduled data collections for historical
data access, allowing applications to retrieve registered data needs
via endpoints without depending on database latency.
Reliability. The platform offers local short-term data storage and
baseline actuation commands during connectivity interruptions,
ensuring robust data persistence and minimising downtime for
essential building operations. It also supports dynamic data quality
checks through data cleaning and preprocessing techniques and
adopts protective measures for data writing to prevent issues such
as setting up values that exceed acceptable thresholds.
4 Case Study
The platform was demonstrated in a residential building (student
hall) and a commercial building (car dealership), which differed
in location, floor area, systems, and data sources. Data from both
buildings were integrated through the platform’s data ingestion
component. Apart from configuring the connectors and registering metadata, the topics and payloads from each building were
standardised.
After initial setup, the buildings’ graphs were generated via
the data integration component. Then, to demonstrate a streamlined configuration of third-party applications using the graphs,
two applications were developed: a dashboard tool and a Demand
Flexibility (DF) control. The dashboard tool was deployed in the
commercial building, querying historical datasets, while the DF control was deployed across 20 apartments in the residential building,
reading real-time data and writing commands.
Figure 4 presents the dynamic data flow and generated graphs
for both buildings, along with the configuration and deployment
processes of the two applications based on the platform’s data management subcomponents. These subcomponents include the app
register and query generator, which enable the automated instantiation of generic queries based on specific application requirements,
the buildings’ graphs metadata (retrieved via SPARQL queries) and
access mechanisms (e.g., via time series database queries or message broker clients). The figure also shows the universal API role,
ensuring a consistent data access mechanism by creating channels
and data collections. This allowed the applications to read and write
data in the buildings via endpoints aligned with their needs.
The commercial building graph comprises 311 triples, representing 257 data points, which include environmental sensors at the
zone level and electrical meters at the building level. The implemented dashboard tool supports the monitoring and analysis of key
variables such as temperature and humidity, providing data plots for
configurable periods (e.g., last 24 hours). Similarly, the residential
building graph consists of 436 triples, representing 360 data points,
including environmental and power sensors and controllers at the
zone level. In this case, the DF control required access to temperature and occupancy sensors, temperature setpoints, and grid signals,
and resulted in an average demand reduction of approximately 35%
during tested shed events.
5 Limitations and Challenges
While the proposed platform offers a solution that aims to automate
the configuration and deployment of building applications, it also
presents certain limitations and challenges. The automation of
graph generation and application self-configuration depends on the
accuracy and sufficiency of manual inputs during the initial setup,
as well as the capability of the graphs’ underlying ontologies to meet
the applications’ requirements. Although the platform attempts to
address this issue by implementing templates and norms that ensure
consistency and by adopting well-established ontologies, further
validation in large-scale buildings and more complex applications
is needed.
6 Discussion and Conclusions
This study presents a reference architecture designed to enhance the
scalability of smart building applications. By decoupling system integration from application deployment, the architecture empowers
third-party developers to create applications that can be consistently deployed across multiple buildings while seamlessly integrating with various data sources (both historical and real-time). This
approach can significantly reduce applications’ deployment time
and costs. The proposed platform implementing such an architecture demonstrates this by allowing the configuration of applications
in just a few hours using automated, building-agnostic methods,
which are applicable once the building’s semantic model (graph)
is generated and its data sources are connected to the platform.
In comparison, developers previously required a whole week to
configure and deploy a similar application using traditional workflows and platforms for the same residential building featured in the
case study. Although graph generation and data source integration
require a similar amount of time, these tasks are anticipated to be
one-time efforts. New applications can seamlessly integrate with
the building with minimal effort.
Future research aims to validate the platform’s robustness in
supporting more complex analytical and control applications while
connecting with various buildings. We also aim to establish suitable
methodologies for quantitatively assessing the platform’s benefits
compared to traditional workflows.
Acknowledgments
This work was supported by the Horizon Europe BuildON project
under contract No. 101104141, and co-funded by the UK Research
and Innovation (UKRI) under the UK government’s Horizon Europe
funding guarantee grant number 10069441. The authors would like
to thank George Korbakis and Nikolas Bellos from the National
Technical University of Athens for their support.