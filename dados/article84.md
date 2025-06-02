Title: Toward Building a Digital Twin for Network Operations and Management

ABSTRACT With the growth of telecommunication networks driven by resource-intensive applications,
the expansion of IoT, the rise of data centers, and the advancements of 5G and future 6G networks,
monitoring and maintenance are becoming increasingly important for network operators. In this sense,
the Network Digital Twin (NDT) is emerging as a promising technology to mirror a network’s whole
operational and management lifecycle to optimize its performance without compromising the real network.
In this work, we propose an NDT solution supported by a new data integration methodology and
a prototypical architecture for translating information from the network management domain into a
knowledge-based interoperable model. Our case study shows how this NDT can be used to reveal the
capabilities of real networks in terms of configuration and operational status, providing benefits for network
control and management to facilitate the application of closed-loop network automation systems.
INDEX TERMS Data integration, model-driven telemetry (MDT), network automation, network digital
twin (NDT), and network management.
I. INTRODUCTION
T O DEAL with the complexity, cost, heterogeneity, and
dynamics of modern telecommunication networks, the
Digital Twin (DT) concept has been extended as a promising
technology and key enabler for efficient network control
and management [1], [2]. A Network Digital Twin (NDT) is
thus conceived as a dynamic virtual model or representation
of a real network that can be used to analyze, diagnose,
simulate, and control the behavior of the network. NDT
technology facilitates the rapid deployment of innovative
network solutions with a wide range of applications such as
network operation, maintenance, optimization, visualization,
or intent verification [3].
The creation of NDT has already raised the interest of
standards development organizations such as ITU-T and
IETF, which identify the requirements, propose architectures,
and discuss use cases [4], [5]. In the future, NDT can
become an indispensable part of overall network management, covering the entire lifecycle of real-world networks
without compromising their daily operations, by serving
the application of innovative technologies, and increasing
their level of automation and intelligence. However, several
challenges have been identified in the design and implementation of NDT systems for efficient control and management
of modern telecommunication networks. These challenges
include dynamically reflecting real-world network behavior
within the NDT representation [6], providing an adequate
mapping mechanism of data retrieved from the real-world
network to unified data models used by the NDT considering
the heterogeneity and idiosyncrasies of network monitoring
data sources [7], [8], and designing mechanisms for data
collection, storage, and management, taking into account that
data is the cornerstone of NDT construction [2].
To overcome these challenges, we present a new methodology for modeling an NDT by translating data from
network management sources into a knowledge-based data
integration system that facilitates the interaction with the
configuration and operational status of real networks. The
proposed solution builds on the NGSI-LD standard specification defined within ETSI’s Industry Specification Group
on Context Information Management (ETSI CIM), which
enables the modeling of Digital Twins [9]. The three key
elements of our solution are:
1) the integration of network data sources supporting the
Model-Driven Telemetry (MDT) paradigm based on
the YANG data modeling language and network management protocols such as NETCONF or gNMI [10]
2) the use of the NGSI-LD standard to represent network
configuration, operational status, and telemetry data in
NGSI-LD meta-models
3) the use of the NGSI-LD API as an interface between
network management applications and the NDT.
The remainder of the paper is organized as follows. First,
insights into research activities related to using Digital Twins
in the network management domain are introduced. This
is followed by the description of a new methodology, a
high-level architecture, and a prototype implementation to
accomplish an NDT solution for network management purposes. Then, a case study is presented to showcase different
examples of network management requirements that can be
covered by this NDT solution. In addition, experimental
performance results of the prototype implemented for the
proposed solution are included. Finally, the conclusions and
future steps of this research are presented.
II. BACKGROUND
This section provides some background on the application
of the Digital Twin concept within the network management
domain.
A. DIGITAL TWINS IN THE NETWORK MANAGEMENT
DOMAIN
The use of the NDT paradigm has become increasingly
relevant in network management as the basis for advanced
emulation solutions for optimization, troubleshooting, and
network upgrade planning. Once an NDT is defined, it
can be configured to operate independently of the real
network to perform what-if analysis or optimization tests,
which can then be run in real-time on the virtual network
model without compromising the real network [2]. Unlike
conventional network emulation solutions, NDT offers an
interactive virtual-real mapping mechanism and data-driven
approach to enable closed-loop network management and
automation. NDT leverages real-time network data for highfidelity condition simulation, minimizes the risk of applying
configuration changes, and enhances network reliability for
automated fault detection and repair. This makes NDT
a powerful tool for network management compared to
traditional emulation approaches that have low fidelity and
lack interactive interfaces with the real network [5]. Thus, an
NDT solution can foster efficient management of networks,
enabling the application of data-driven network models and
machine learning technologies.
However, several challenges need to be addressed. The
current amalgam of monitoring data sources makes it
necessary to define standard interfaces and representations
to be used for the NDT [2], [11]. Additionally, both
accuracy in the network data collection process and complete
synchronization between the real network and its NDT are
required [12].
Within the network management domain, the YANG data
modeling language and network management protocols such
as NETCONF or gNMI are the standards for managing
configuration and obtaining telemetry data from network
devices [10]. However, with the proliferation of YANG data
models in the network industry, a new approach is needed
to have a standard representation that encompasses not only
the network data but also its semantics. In this regard,
knowledge graphs are a promising solution that combines
data integration with knowledge representation [13]. In
addition, by linking different data sources, knowledge graphs
enable intelligent automation systems to explore the causes
and effects of network behavior [14]. Several works propose
using knowledge graphs in NDT [6], [15], [16], but they
are not based on formal and standardized data models for
network management.
Network management systems also require a data integration technology capable of consolidating data from diverse
sources into a unified view, providing a comprehensive
data infrastructure with an interoperable interface for data
consumption [17], [18]. In previous work, we introduced
CANDIL [19], a federated data fabric for integrating data
from distributed systems, mainly focused on networking
aspects. CANDIL defines an ontology that captures network
concepts originally modeled with YANG, along with a
reference architecture for ingesting and integrating data in a
federated knowledge graph.
Therefore, a data integration approach simplifies data
access and management by abstracting consumers from
the location and underlying complexities of the monitoring
sources, such as protocols, data schemas, and encoding
formats, becoming an ideal solution for NDT data representation. In this sense, the authors in [6] propose an NDT data
integration solution based on a knowledge graph to provide
topological, device, and network statistics information, but
tightly dedicated to the management of SDN-based networks.
Alternatively, NetGraph [8] presents a data integration
NDT platform for the automated and intelligent operation
and management of data center networks with network
devices supporting YANG and non-YANG based monitoring
mechanisms. However, when integrating data from network
devices, NetGraph uses the data accessible in configuration
files as the knowledge baseline, regardless of the formal data
models followed by the network data sources. The authors
of NetGraph highlight the challenges of data modeling for
NDT due to the vast amount of data sources and the need for
accurate data mapping solutions between the real network
and its Digital Twin representation. The authors in [20], [21]
present a prototype NDT solution that covers the exchange of
network management data between real networks and their
Digital Twin emulations to partially mimic the real network
status and operation, also based on YANG models and using
the gNMI management protocol, but the solution focuses on
direct data exchange without providing formal representation
and integration mechanisms for network management data.
In this work, we propose a data integration solution
for MDT network data sources based on the low-level
analysis of standardized YANG data models. The solution
integrates automatic data parsing and mapping mechanisms
that allow the digital representation of data modeled in
YANG into an interoperable NDT system for network
management purposes. To the best of our knowledge,
this is the first Digital Twin proposal focused on the
network management domain that proposes a high-fidelity
data integration mechanism through the use of standard
representations and communication interfaces, which is a
crucial task to adequately reflect real network behavior in
the NDT paradigm.
B. NDT ELEMENTS AND DIGITAL MAP PROCESS
An NDT can be described as a digital counterpart of
a real network that captures its attributes, behavior, and
interactions and is continually updated with the network’s
performance, maintenance, and health status data throughout
its life cycle [5]. The NDT is considered to be founded on
four core elements:
1) historical and real-time data from real-world networks
2) models for comprehensive representation of the data
3) communication interfaces between the NDT and the
real network, and between the NDT and external
applications
4) an interactive, real-time data mapping process between
the NDT and the real network.
These four pillars provide the information needed to
implement the logic of the NDT to analyze, diagnose,
emulate, and control the real network during its whole life
cycle with the help of optimization algorithms, management
methods, machine learning models, and expert knowledge. In
consequence, an NDT should be able to correlate all models
and data to topological entities in the twin network. In this
regard, the Digital Map concept aims to provide a topological
model representing the mapping between the real network
and its NDT, facilitating a comprehensive and up-to-date
view of the entire network [7], [22]. The Digital Map defines
the key topological entities within the network (e.g., network,
nodes, links, termination points), their role and particular
properties in the network, and the relationships between the
different entities. Figure 1 depicts the Digital Map process,
highlighting in red the mapping for a router device and one
of its network links along with the termination points, all
within a network topology.
The NDT solution presented in this work covers the
aforementioned core elements and a digital mapping mechanism to integrate monitoring data from real networks
FIGURE 1. General insight on Digital Map process.
into a knowledge-based interoperable model for efficient
management purposes.
C. NGSI-LD STANDARD AND DIGITAL TWINS
Digital Twins rely heavily on data, both consumed and
produced by them, to provide a digitalized, augmented,
and actionable view of real-world assets. In line with
this view, recent reports from ETSI CIM analyze the
feasibility of building Digital Twins and propose different
use cases and applications [9]. ETSI CIM considers the
exchange of context information across systems as a crucial
enabler for smart applications and has standardized the
NGSI-LD specification to allow these applications to gather
information from multiple sources, integrate the information,
and eventually generate derivative information or make
decisions. To this end, the NGSI-LD standard specification
comprises two main features:
1) the NGSI-LD information model [23] as a means to
represent and describe context information
2) a REST-based application programming interface
(API) [24] as a means to exchange context information
between systems.
The NGSI-LD standard does not define a reference
architecture, but it does suggest prototypical architectures
such as centralized, distributed, or even federated. The
NGSI-LD standard introduces multiple architectural roles
that exchange context information by using the NGSILD API. The Context Broker is the main architectural
role that stores and exposes context information and can
also register itself as a Context Source for other Context
Brokers, enabling federated architectures. Depending on the
architectural approach, the Context Producer and Context
Source roles register, provide, and update the context
information they can offer through the Context Broker.
Meanwhile, the Context Consumer role discovers and queries
relevant context information and subscribes to notifications.
The choice of architectural criteria depends on the scale
and specific requirements of the application environment
from which context information needs to be extracted.
Given the support of the NGSI-LD standard for integrating
context information from multiple data sources, this paper
FIGURE 2. General insight on ETSI CIM compliant Descriptive Twin for network
management domain.
proposes its use to cover monitoring sources of the network
management domain, considering the nature of the sources
and the scale of the network infrastructure.
In addition, Digital Twins have been systematically classified by ETSI CIM depending on their capabilities. The
main twin case is the Descriptive Twin, in which the DT
serves as an interface that informs about the past and current
state of real-world assets. In addition, when bidirectional
communication between the real-world assets and the DT is
possible, not only the real-world state can be represented in
the DT, but changes in the DT can also be applied to the realworld assets. Thus, the DT can be queried and configured
as if it were a real-world element. Transferring this DT
case to the network management domain, as illustrated by
Figure 2, then the asset is a real-world network and the
NDT is a digitalized representation of the network topology
with its operational status and configuration. Thus the
Descriptive NDT functions as a conceptual map of the realworld network asset, providing continuous representation of
network management data according to a knowledge-based
model. The Descriptive NDT can also offer added value
through computational capabilities, such as the calculation of
network key performance indicators (KPIs) using time-series
aggregation functions on the monitored data.
Other DT cases that would add value to network management, such as providing predictions, running what-if
scenarios, or diagnosing possible malfunctions, are based
on the Descriptive Twin vision. The Descriptive NDT using
the NGSI-LD standard is therefore the starting point on
which this paper focuses. As far as we know, there are no
proposals in the literature that attempt to delve into the use
of the NGSI-LD standard for the construction of Digital
Twin solutions focused on the field of network management,
which highlights the novelty in the proposal of this work.
III. A NEW METHODOLOGY FOR MODELING NETWORK
DIGITAL TWINS
This section proposes a new methodology for modeling a
Descriptive NDT using the NGSI-LD standard. First, we
FIGURE 3. Data materialization with the NGSI-LD standard.
introduce data integration approaches to integrate YANG
data from the network management domain using NGSI-LD.
Then, we propose the use of generic rules for translating
between YANG and the NGSI-LD meta-model to provide a
mapping mechanism between network management data and
its representation in the NDT. Finally, we present a reference
architecture and a prototypical implementation for modeling
a Descriptive NDT.
A. DATA INTEGRATION USING NGSI-LD
Data materialization and data virtualization are two of
the main approaches used to integrate data from different
sources [17], [18]. On the one hand, the data materialization
approach proposes a target data store that is synchronized
with the data sources and provides consumable historical data. When there is a need for a high-performance
information backend for data integration, such as in NDT
systems, this data materialization approach could be the
ideal solution. On the other hand, data virtualization offers a
suitable interface for querying and manipulating information
without concerns about the physical location of data sources,
providing the most up-to-date results without replicating
information. It could be the more efficient solution when
the data does not need additional preprocessing mechanisms
and can be directly accessible and consumable.
Figure 3 depicts the workflow for addressing the data
materialization approach with the NGSI-LD standard. In this
approach, the architectural roles that are used are compatible
with the vision of a centralized architecture that is reflected in
the NGSI-LD standard. The Context Producer is responsible
for collecting data from a Data Source, translating it into the
NGSI-LD meta-model representation, and then replicating
the data within a Context Broker. The Context Broker stores
the data and provides access to interested Data Consumers
that can either query for new data or subscribe to data
changes using the NGSI-LD API. The main drawbacks of
this approach are potential synchronization issues with the
Data Source to ensure that the data remains up to date,
and the limitation of Context Broker storage due to data
replication. However, the approach benefits from both the
support for historical data records within the Context Broker
and low end-to-end latency from data collection to data
integration.
FIGURE 4. Data virtualization with the NGSI-LD standard.
Figure 4 depicts the workflow for addressing the data
virtualization process for querying and subscribing to virtualized data through an NGSI-LD Context Broker. In this
approach, the use of architectural roles is compatible with
the distributed architecture vision of the NGSI-LD standard.
The Context Source acts as an intermediary system that
implements the NGSI-LD API to provide context information
from particular Data Sources. The Context Broker redirects
requests from Data Consumers to the Context Source so
that the Context Source provides the virtualized representation of the data collected from the Data Sources to
the Data Consumers without storing the resulting data in
the Context Broker. The main advantage of this approach
is that it provides efficient access to data, avoiding data
replication. The main disadvantage of this approach is the
additional delay in processing consumer requests to deliver
the data.
The Descriptive NDT solution proposed in this work
can mirror the operational status and configuration of real
networks using both data integration approaches to support
an advanced network management system implementing
closed-loop automation. The data materialization approach
is identified as an ideal option for collecting network
configuration and operational data over time that can be
used, for example, to train and feed external machine learning systems to capture network behavior for performance
analysis. Meanwhile, the data virtualization approach is an
efficient solution to retrieve monitoring data on demand and
request network management actions.
B. YANG TO NGSI-LD TRANSLATION CONVENTIONS
The translation conventions, based on [25], provide the
rules for mapping YANG data node types to the elements
of the NGSI-LD meta-model. The YANG data modeling
language specifies different types of data nodes [26],
where each node is represented in a schema tree and can
be instantiated in a data tree. Meanwhile, the NGSI-LD
information model [23] builds on the Labelled Property
Graph model, where entities have relationships with other
TABLE 1. High-level mapping from YANG to NGSI-LD.
entities, and entities and relationships can have properties
providing additional characteristics.
The transformation process between YANG and NGSI-LD
takes as input the effective YANG schemas, which is the
compiled set of YANG data models, so the mapping rules
are defined at the YANG level. This allows for seamless
translation of any YANG data to NGSI-LD regardless
of the encoding format (e.g., XML or JSON) and the
network management protocol (i.e., NETCONF or gNMI)
used for transporting YANG data. Table 1 shows a highlevel mapping of the main YANG data node types to the
core elements of the NGSI-LD meta-model.
In general, YANG container maps to NGSI-LD entity
type whenever the container contains child data nodes and
does not have a YANG list as its only child. If the latter
is fulfilled, the container can be omitted since it has no
semantic meaning, so it is not mapped to the NGSI-LD entity
type. As a result, this design choice makes the graph more
compact, which improves usability. In a similar way, YANG
list maps to NGSI-LD entity type, where there will be an
NGSI-LD entity for every member of the YANG list. In both
cases of YANG data node types, if the YANG container or
YANG list is the child of another YANG data node (either
container or list), the resulting NGSI-LD entity type will
include an NGSI-LD relationship pointing to the NGSI-LD
entity type of the parent YANG data node, thus capturing
the hierarchical connection between both YANG data nodes.
Meanwhile, YANG leaf and YANG leaf-list will map
either to NGSI-LD attribute (i.e., NGSI-LD relationship or
NGSI-LD property), but in the case of YANG leaf-list the
mapping NGSI-LD attribute is an array. The corresponding
NGSI-LD attribute will be part of an NGSI-LD entity type
that represents the parent YANG data node (either container
or list) of the child YANG leaf or YANG leaf-list. When
the YANG leaf or YANG leaf-list uses the leafref data type,
it references to another YANG data node type, and it will
map to an NGSI-LD relationship pointing to the resulting
NGSI-LD entity type that contains the NGSI-LD attribute
corresponding to the target YANG data node type. However,
when the data type of the YANG leaf or YANG leaf-list
is considered a literal, then it is mapped to an NGSI-LD
property.
Table 2 captures the main data types considered in NGSILD when translating from the different YANG built-in data
types. In YANG, there are several Integer built-in types that
represent signed and unsigned integers of different sizes,
TABLE 2. Data type conversion from YANG to NGSI-LD.
and all of them map to the Integer data type in NGSILD. Decimal numbers, boolean values, and string data types
in YANG have their corresponding data type in NGSILD, emphasizing that if a YANG string contains a regular
expression pattern, the mapping to NGSI-LD will also
contain the same string pattern. Note that for representing
bit sets and binary data, the candidates in NGSI-LD are
lists of strings and strings, respectively, and for enumeration
data types in YANG representing a set of bounded values,
the corresponding data type in NGSI-LD is a string with
the determined value. Note also that the empty YANG data
type maps to a literal in NGSI-LD represented by an empty
string, since the null value is reserved for deleting NGSI-LD
attributes. In addition, there are custom data types defined in
YANG for representing timestamps, which require a special
mapping to a string with date-time format in NGSI-LD.
The details of the YANG to NGSI-LD translation process,
covering both the mapping rules and the data type conversion, are available in [25]. To cover these YANG to NGSI-LD
translation conventions, there is a need for a solution capable
of parsing YANG modeled data and matching it with its own
YANG model to identify its schema and data tree structures
in order to apply the mapping rules accordingly. In the
following subsections, a prototypical NDT framework for
performing these mapping rules automatically is described in
detail. Then, our solution can be seen as a first approximation
or reference implementation to cover the translation process
from YANG to NGSI-LD for a new model-driven network
management proposal based on NGSI-LD standard.
C. DESCRIPTIVE NDT ARCHITECTURE
One of the main concerns in implementing an NDT system
is the management and knowledge of real-world network
data. We address this by defining a Descriptive NDT solution
that provides automatic mechanisms for mapping data that
is related to the network management domain to a common,
formal, and interoperable knowledge model based on the
NGSI-LD standard. By applying the translation conventions
and the data integration approach mentioned in the previous
subsections in a fully automatic way, this solution can
provide a programmatic system for building a Descriptive
NDT.
Figure 5 depicts the reference and high-level architecture
of the proposed Descriptive NDT solution. This architecture
encompasses the four core components considered for NDT
solutions, providing
1) real-time and historical NDT data
2) models for characterizing the NDT data
3) interfaces to establish communication with the real
network and with the NDT system
4) mapping mechanisms for the exchange of data between
the real network and the NDT system.
Support for MDT and management mechanisms based
on YANG is achieved by the proposed architecture using
a data integration approach. Once the YANG Data Models
that characterize the configuration and operation of the
real networks are selected, the Descriptive NDT Generator
component will automatically generate the models and
mapping mechanisms to cover the Descriptive NDT solution
for performing the translation between real network data and
NDT data.
The resulting Descriptive NDT includes the following
architectural components:
• Network Operator: The Network Operator enables the
application of network automation processes for both
network monitoring and configuration purposes. For
monitoring purposes, the Network Operator enables the
collection of management data such as topology, configuration, and operational data from real-world networks
using network management interfaces based on the
YANG data modeling language, such as NETCONF or
gNMI. On the other hand, for configuration purposes,
the Network Operator allows the application of desired
configuration changes into the real network using the
network management interfaces.
• YANG to NGSI-LD Data Mapping: This data mapping
mechanism allows parsing the YANG Modeled Data
collected by the Network Operator and mapping it to
the NGSI-LD Modeled Data by applying the translation
conventions and following the NDT Data Models
accordingly.
• NDT Data Models: These models are automatically
generated data schemas that provide the knowledge
baseline for the NGSI-LD information models associated with each YANG data model. Depending on the
element of the NGSI-LD meta-model (i.e., whether it
is an entity, property, or relationship), a specific type
of data schema is defined, including any particularities
specified within the associated YANG data nodes, such
as descriptions, data types, mandatory field selection,
regular expressions, formats, units, thresholds, or default
values. Finally, this component generates the base
models to address the complete pipeline of the data
translation between the real network and the NDT.
• NGSI-LD to RPC Data Mapping: This data mapping
mechanism allows parsing the NGSI-LD Modeled Data
provided by a Data Consumer to update the real
FIGURE 5. Descriptive NDT architecture compliant with NGSI-LD standard and NDT core elements.
network configuration or to start the monitoring of a
telemetry data source. The parsed data is then mapped
to RPC (Remote Procedure Call) commands which are
orchestrated by the Network Operator component to
apply the desired configuration on a network node or
to set up the telemetry data source.
• NGSI-LD Data Integration: This is the core component
for integrating the NDT data using either a data materialization approach or a data virtualization approach.
For management data collected from real networks,
after the data is retrieved and translated to NGSI-LD
by the YANG to NGSI-LD Data Mapping mechanism,
the NGSI-LD Data Integration component validates the
translated data against the corresponding NDT Data
Models and forwards the resulting NDT Data to the
NGSI-LD Context Broker. Using a data materialization
approach, the NDT data is stored in the Context Broker,
while using a data virtualization approach, the data
is sent through the Context Broker directly to the
requesting consumers. For network configuration or
monitoring instructions provided by a consumer, once
the NGSI-LD data is uploaded to the Context Broker,
the NGSI-LD Data Integration component receives and
validates the data as NGSI-LD Modeled Data. The
NGSI-LD Modeled Data can then be processed by the
NGSI-LD to RPC Data Mapping mechanism to apply
the requesting action.
Therefore, through this Descriptive NDT, consumers, such
as analytics applications from a network management system
(i.e., NMS Apps), can interact with the real network and
then consume and manipulate the integrated NDT data using
the NGSI-LD API.
D. A PROGRAMMATIC DIGITAL MAPPING SYSTEM FOR
MDT NETWORK ASSETS
Figure 6 depicts the detailed prototypical architecture for
implementing the aforementioned Descriptive NDT for data
collection purposes. There is an open-source prototype
implementation publicly available on GitHub [27] which
is built on a Docker microservices-based solution. The
prototype covers the process of collecting telemetry and
configuration data from the network for its integration in
a Descriptive NDT. Since the current NGSI-LD Context
Broker implementations do not fully support the registration
of Context Sources, the validated prototype adopts an
approach based on data materialization rather than data
virtualization. The methodology is targeted to MDT network
assets based on the YANG data modeling language. The
system separates its functionality into two main planes:
1) Descriptive NDT Generator Plane
2) Data Materialization Pipeline Plane.
The Descriptive NDT Generator Plane general functionality consists of processing the native data models of the
network assets (i.e., YANG Data Models in Figure 6) to
generate different programmed artifacts that allow performing the YANG to NGSI-LD translation in an autonomous
way. Then, the Data Materialization Pipeline Plane makes
use of the programmed artifacts to be able to parse the raw
configuration and operational data coming from the network
assets and generate NGSI-LD modeled data.
The programmed artifacts from the Descriptive NDT
Generator Plane are generated automatically by processing
YANG Schemas (i.e., the different schemas provided by
the YANG Data Models). For this purpose, an open-source
tool named pyang [28] has been used. Pyang is a YANG
FIGURE 6. A prototypical implementation of the Descriptive NDT architecture based on a programmatic digital mapping system for MDT network assets. The programmatic
digital mapping solution is validated for network management data collection purposes and is based on a data materialization approach using the NGSI-LD standard.
validator, transformer, and code generator written in the
Python programming language, which includes features that
make it an ideal solution to be able to code the necessary
programmed artifacts. These artifacts are the following:
• OpenAPI Schemas Generator: Given one or more
YANG schemas, it dynamically generates OpenAPI
Schemas compliant with the NGSI-LD OpenAPI
Specification (NGSI-LD OAS) [29]. The generated
schemas represent the knowledge baseline for the resulting NGSI-LD meta-model associated with the input
YANG schemas. Then, the OpenAPI Generator [30]
tool is used to generate the stub code to manipulate the information modeled in the schemas in an
object-oriented programming form based on the Python
language (i.e., Schemas Code in Figure 6). In addition,
the OpenAPI Generator tool allows to automatically
generate source code from the NGSI-LD OAS for a
Python-based NGSI-LD API client, which provides the
different operations and options of the NGSI-LD API
in a programmatic way. By using the Python classes
for the particular schemas associated with an MDT
network asset, we can build data instances that are used
as payloads in the operations defined by the NGSI-LD
API client to manage the instantiation of the required
NGSI-LD modeled data.
• XML/JSON Parser & Mapper Generator: Given one
or more YANG schemas, it generates the Python code
of XML and JSON parsers that read data modeled
by these schemas and generate the corresponding
NGSI-LD meta-model data structures. Then, this plugin addresses the translation conventions described in
Section III-B for covering the YANG to NGSI-LD
mapping process. For the prototype implementation,
we developed generators for data retrieved by query
and subscription RPCs using the NETCONF and gNMI
network management protocols.
• NGSI-LD Context Generator: NGSI-LD uses context
entries to map URIs (Uniform Resource Identifiers)
from expanded full versions to compacted short versions
for the NGSI-LD elements represented in particular information models. Given one or more YANG
schemas, the NGSI-LD Context Generator produces the
corresponding NGSI-LD context files. These context
files are structured as key-value dictionaries, where each
key is the NGSI-LD element type that matches the
corresponding YANG data node, and each value is a
URN (Uniform Resource Name) in XPath notation that
allows navigation within the YANG data model to locate
the associated YANG concept.
Based on the functionality of the Descriptive NDT
Generator Plane components, the Data Materialization
Pipeline Plane can handle the full data integration process
required to complete the YANG to NGSI-LD translation.
Figure 6 considers that configuration and telemetry data
coming from MDT network assets are collected from a
Data Collector component. This Data Collector is built
on a Python microservice that uses NETCONF and gNMI
protocol clients as network management interfaces. The
data is modeled according to YANG models and need
to be mapped to the corresponding representation of the
NGSI-LD meta-model. To cover this translation process, the
XML/JSON Data Parsers & Mappers components perform
the parsing of the YANG modeled data encoded in XML
or JSON encoding format and the mapping process to the
corresponding NGSI-LD modeled data in the form of Python
dictionary data structures.
The NGSI-LD Instantiator component is then responsible
for receiving the NGSI-LD modeled data and validating it
against the Python classes of the source schemas. During the
data validation process, the NGSI-LD Instantiator ensures
the data compatibility and consistency within the appropriate
NGSI-LD model. The exchange of streaming data between
the aforementioned components of the pipeline is carried
out by using a message-bus system based on Apache
Kafka [31]. Finally, the NGSI-LD Instantiator uses the
instantiated Python objects with the NGSI-LD API client
to materialize the resulting NGSI-LD modeled data within
a compatible NGSI-LD Context Broker, where it can be
accessed by interested data consumers.
IV. CASE STUDY: DESCRIPTIVE NDT FOR NETWORK
MANAGEMENT
In this section, we present a case study for applying the
Descriptive NDT solution for network management purposes.
The validation use case involves the discovery and exposition
of data related to network topology and node interfaces.
Network topology and node interfaces are characterized
using YANG models, which are automatically converted to
NGSI-LD information models for the Descriptive NDT. We
analyze the case study with standardized YANG models
from both IETF and OpenConfig consortium. In addition,
we illustrate the usability of the Descriptive NDT solution
in this particular network management case.
A. IETF-BASED DESCRIPTIVE NDT MODEL
Figure 7 shows a high-level UML diagram of the NGSI-LD
meta-model provided by the Descriptive NDT to represent
data from network topologies and node interfaces based
on IETF Requests For Comments (RFCs) 8345 [32] and
8343 [33].
On the left hand of the diagram, we can find the different
NGSI-LD entities for modeling the network topology. The
different entities have a mandatory property to identify the
network, node, link, and termination point within the network
topology. To determine the source and destination of a
network link, there are two separate entities to indicate the
corresponding node and termination point at each end. In
addition, we define the isPartOf NGSI-LD relationship to
represent compositional relationships between entities (e.g.,
a termination point is part of a network node). This case
of relationships is automatically inferred in the process of
parsing the YANG data models.
On the right hand of the diagram, there are the two
NGSI-LD entities modeling node network interfaces. The
Interface entity has NGSI-LD properties representing the
configuration and operational data of a network interface,
while the InterfaceStatistics entity has NGSI-LD properties
representing the interface statistics relative to traffic counters. The Interface entity type has two optional NGSI-LD
relationships, lowerLayerIf and higherLayerIf, that target
other Interface entities to reference interfaces that are either
layered below or on top of an interface in the case of underlay
or overlay networks.
In addition, there is a special NGSI-LD relationship
named isSubclassOf, which is defined to establish inheritance
relationships between entities. This case of relationships
is also automatically inferred and is used to unify
the concept of network interface between Interface and
NetworkNodeTerminationPoint entities.
B. OPENCONFIG-BASED DESCRIPTIVE NDT MODEL
Figure 8 depicts the resulting NGSI-LD meta-model provided by the Descriptive NDT to represent data regarding
network node interfaces, but modeled according to the
OpenConfig consortium [34].
Again, the isSubclassOf relationship is used to represent that an Interface is a subclass of the entity
NetworkNodeTerminationPoint used in the network topology
model standardized by IETF. And, similar to the model
derived from IETF RFC 8343, there is an entity representing interface statistics, InterfaceStateCounters, to collect
interface traffic counters. However, the resulting NGSI-LD
meta-model for OpenConfig differs from the IETF model in
that configuration data (i.e., InterfaceConfig) and operative
state data (i.e., InterfaceState) are separated into different
entities, although certain properties are found in both the
configuration and state entities.
Furthermore, this model differentiates the concept of
subinterface with its entities dedicated to configuration, status, and telemetry statistics information. These subinterface
entities model a concept equivalent to that of higher and
lower-layer interfaces within the IETF model, but with
separate entities. In addition, the InterfaceHoldTimeConfig
and InterfaceHoldTimeState entities represent the configuration and state information to adjust hold-time used
for dampening advertisements when the interface state
changes from up to down and vice versa, with a
value of zero meaning that dampening is disabled (i.e.,
immediate notifications about the state of the interface).
There are also the InterfacePenaltyBasedAiedConfig and
InterfacePenaltyBasedAiedState entities, which represent the
configuration and state of the interface link transition
settings.
C. APPLICATION OF DESCRIPTIVE NDT FOR NETWORK
MANAGEMENT PURPOSES
The aforementioned NGSI-LD meta-models characterize the
NDT models and associated data, allowing their consumption
and manipulation. Thanks to the NGSI-LD API, the following use cases demonstrate the usability of the Descriptive
NDT for efficient network management purposes.
These use cases illustrate functionalities that help
network management systems analyze and estimate network
performance, supporting complex network automation tasks
such as network planning, detecting anomalies, identifying potential problems or risks, troubleshooting purposes,
FIGURE 7. UML diagram of NGSI-LD meta-model for network topology and interfaces based on IETF RFCs 8345 and 8343.
predicting future conditions, or recommending optimization
policies.
1) DISCOVERING NODE ADJACENCIES IN NETWORK
TOPOLOGY
Given a network device, determine the devices connected
to the other edge of its links to discover adjacencies and
find neighboring nodes within a network topology. First,
the interested consumer needs to discover the network links
where the given node (e.g., an entity of type NetworkNode
identified by the id node1) is the source or the destination
by using the following request:
The response to the previous query provides a list of entities of type NetworkLinkSource and NetworkLinkDestination
where the node1 is the source or destination of a link
(i.e., the sourceNode or the destNode relationships point
to the name node1), and where the isPartOf relationship
points to object identifiers that reference entities of type
NetworkLink. In addition, the received NetworkLinkSource
and NetworkLinkDestination entities provide the source
or destination interface of the node node1 which is the
termination point of the link (i.e., the sourceTp or the destTp
relationship objects).
Let’s imagine that the response provided indicates that
node1 has three links where the node is the source or
destination, and that those links have the object identifiers
link1, link2, and link3. Now the consumer needs to identify
the nodes adjacent to node1 on the other side of those links.
To do this, the consumer would perform the following query:
As a result, the query response will provide the list of entities of type NetworkLinkSource and NetworkLinkDestination
with the information of adjacent nodes to node1 and
their termination point interfaces within the network link
that joins them to node1. The consumer could then
determine and select network links between specific node
pairs to measure, for example, their traffic occupancy or
throughput.
FIGURE 8. UML diagram of NGSI-LD meta-model for network interfaces according to OpenConfig consortium.
2) OBTAINING HISTORY ABOUT THE CONFIGURATION
AND STATUS OF NETWORK INTERFACES
This use case consists of obtaining the configuration and
status of network interfaces along the time using the
Temporal API offered by the NGSI-LD API. It means
that consumers can obtain different instances of the
Interface, InterfaceConfig, and InterfaceState entities along
the time, depending on whether they follow the IETF
or the OpenConfig compliant NGSI-LD meta-model. The
following request is an example of retrieving the instance
history of Interface, InterfaceConfig, and InterfaceState
entities materialized within the NGSI-LD Context Broker
during the 24 hours of January 15th using the NGSI-LD
Temporal API:
As a result, the query response will retrieve the history
of configuration and state changes from the interfaces. In
addition, by using the sysAttrs query parameter, the consumer
can declare that system-generated temporary properties be
included in the response to indicate the date and time when
the changes were established and materialized in the context
broker.
This test case can be useful for troubleshooting purposes,
allowing network administrators to review or revert changes
to previous configurations.
3) SUBSCRIBING TO TELEMETRY DATA AND
CALCULATING NETWORK LINK PERFORMANCE
In this use case, a network administrator needs to evaluate the performance of network links along a monitored
network. To do this, the consumer could create a NGSI-LD
subscription operation to entities of type InterfaceStatistics
or InterfaceStateCounters to receive performance statistics
about the network link interfaces periodically over time.
In addition, the consumer could rely on a network
analytics application to calculate valuable network KPIs on
demand by using aggregation functions on the telemetry
data. Using particular options of NGSI-LD Subscription
API to receive notifications about the value of particular
NGSI-LD properties and the date and time on which they
were obtained, the application could calculate KPIs, such as
throughput, from the materialized telemetry data.
Let’s imagine that the network administrator needs to
monitor the network link performance between the nodes
node1 and node2. By subscribing to traffic statistics from
the network link interfaces, the consumer could periodically
receive notifications of incoming or outgoing bytes and then
calculate the traffic rate. Figure 9 shows an example of the
required subscription request body, which is used in an HTTP
POST operation as follows:
In the body of the request, we can see as the target of
the subscription the entities of type InterfaceStatistics and
FIGURE 9. NGSI-LD subscription to traffic telemetry statistics.
InterfaceStateCounters with identifiers that determine the
target nodes and their interfaces within a given network
to obtain notifications of the inOctects and outOctets
properties. The attributes parameter allows consumers to
specify the properties and relationships to include in the
notifications to be received when the subscription operation is triggered. Once the subscription is realized, the
notifications will contain the latest value of the inOctets
and outOctets properties, as updated in the context broker
with the periodic telemetry data received from the network
nodes.
In addition, the data parsing solution implemented in the
Descriptive NDT for data retrieved by NETCONF or gNMI
protocols allows including the measurement of time in which
the notifications were received from the network nodes,
being included as metadata of each property of the telemetry
statistics thanks to the native observedAt temporal property
facilitated by the NGSI-LD API. Then, if the consumer
keeps a record of the last measurement value and time
that comes within the notifications received, determining the
increment between the current and previous measurement
values divided by the increment between their measurement
times, the network analytics application could calculate the
traffic rate at each given moment as illustrated by the
following expression (1):
Traffic Rate (t)(Mbps) = (inOctets(t) + outOctets(t)) × 8
t × 106 ,(1)
where t represents the observation time of the counters,
recorded by the observedAt parameter. The time interval
t corresponds to the difference between two consecutive
observation instants.
4) SUBSCRIBING TO OPERATIONAL STATUS OF
NETWORK INTERFACES FOR FAULT DETECTION
For this use case, a network administrator wants to detect
link failures that may affect the network operation. To
this end, the consumer could rely on a network analytics
application that notifies about the operational status of the
network interfaces within the whole network topology. In
this sense, the network analytics application can detect
FIGURE 10. NGSI-LD subscription to the operational status of network interfaces.
an unexpected link fault and determine its impact on the
network.
Let’s imagine that the network administrator needs to
monitor failures on a network link between the nodes node1
and node2. For this case, the consumer needs to subscribe
to changes on entities of type Interface and InterfaceState
with identifiers that determine the target linked nodes and
their interfaces within a given network to obtain notifications
about the operation status of the corresponding network
interfaces.
Figure 10 shows an example of the required subscription request body. The watchedAttributes parameter allows
consumers to subscribe to particular properties such as
operStatus and lastChange, which will allow them to get
notifications about the change of the operational status of
the interfaces as well as the date and time when this change
occurs.
This example demonstrates that the Descriptive NDT
could provide information about the operational status
of a monitored network, allowing the network analytics
application to identify possible link failures.
V. EVALUATION AND EXPERIMENTAL RESULTS
In this section, we describe the evaluation testbed and
the performance experiments carried out for validating the
Descriptive NDT prototype solution based on a data materialization approach presented in this work. The validation
has been particularized for the YANG models proposed in
the previous case study.
Initially, the testbed designed for the functional evaluation
of the Descriptive NDT solution consists of virtual network
emulation scenarios composed of router devices supporting
NETCONF and gNMI. For NETCONF, a CISCO IOS XE
CSR1000V router model supporting telemetry subscriptions
based on YANG Push is employed. For gNMI, a CISCO
IOS XRv9K router model is used, which is capable of
handling gNMI subscription RPCs. For a NETCONF client
working as a data collector component, a Python library
called ncclient [35] is adopted, which supports all RPC
operations and capabilities defined by the NETCONF management protocol. Meanwhile, for gNMI, a CLI client called
gNMIc [36] is used, which provides full support for all RPC
operations and capabilities defined by the gNMI management
protocol.
The virtualized scenarios consist of the deployment of
simple point-to-point network topologies with the aforementioned routers by using the Containerlab [37] virtualization
tool, which enables the specification of container-based
networking scenarios consisting of network devices with
network operating systems of different vendors and models.
However, since the containerized network devices used in
these scenarios consume a lot of computational resources,
and in order not to limit the performance of the machine
on which the experiments are conducted, the testbed was
adapted for generating synthetic data similar to those
collected from the functional tests using NETCONF and
gNMI within the Containerlab networking scenarios, thus
analyzing the experimental performance of the Descriptive
NDT framework under better and more flexible conditions.
Note that these synthetic but realistic data were also the
ones initially used to perform unit tests during the initial
validation phases of the proposed framework for testing
the mapping between YANG modeled data and NGSI-LD
modeled data. In addition, Orion-LD [38] was selected as
the implementation of the NGSI-LD Context Broker during
the functional and experimental phases.
The experimentation allows determining the performance
of the Descriptive NDT prototype in terms of latency and
throughput. The first experiment measures the latency of
XML and JSON Data Parsers & Mappers components
for translating from YANG modeled data to NGSI-LD
modeled data, covering the data parsing and data mapping
subprocesses. The second experiment measures the combined
latency of the YANG to NGSI-LD translation process plus
the data materialization process within the NGSI-LD Context
Broker using the corresponding NGSI-LD Instantiator functionality. It is important to highlight that the data validation
operation performed by the NGSI-LD Instantiator, which
is needed to achieve the compatibility within the target
NGSI-LD model, is included after the YANG to NGSILD translation process and before the data materialization
process during the latency measurements performed for the
second experiment. The combination of the data validation
and data materialization stages performed by this NGSI-LD
Instantiator component is referred to as data instantiation
hereinafter. Finally, there is a third type of experiment for
measuring the throughput of both the YANG to NGSILD translation phase and the data instantiation phase. All
experiments have been performed for telemetry statistics
from network interfaces encoded in both XML and JSON
formats according to notifications received by the NETCONF
and gNMI management protocols.
The results of these experiments and the definition of
the functional virtualization scenarios mentioned above are
available on GitHub along with the code of the Descriptive
FIGURE 11. YANG to NGSI-LD translation latency.
NDT prototype [27]. The testbed used for conducting these
performance experiments and functional evaluation has been
deployed on a single machine running Ubuntu 20.04.4 LTS,
with 32 GB RAM and 8 CPU cores.
In the latency experiments, the number of network
interfaces of a router device from which telemetry statistics
notifications arrive was considered as a variable of interest.
The experiments are carried out according to numbers of
network interfaces that are common for routers, considering
sets of 12, 24, 36, and 48 interfaces. The time between
notification arrivals is considered to be 5 seconds.
As a result, in each type of latency experiment, the
average delay time of a total of 1,000 notifications measured
based on the number of network interfaces is obtained. It
should be noted that in NETCONF, notifications from all
interfaces come wrapped in a single notification event, while
in gNMI each event from each interface comes in a separate
notification. This means, for example, that in the case of
obtaining notifications from 48 interfaces, 1,000 notifications
will come for NETCONF and 48,000 for gNMI. Therefore,
in the case of gNMI, the sum of the delay times of the
sequential notification events associated with each set of
interfaces is combined until the total number of notification
events is covered to obtain the overall average delay time
for each interface set category.
Figure 11 depicts the latency results of the first experiment, representing the distribution of average processing
latency as a function of the number of interfaces. It can be
seen that a linear function with a smooth slope is obtained
and that the time to perform the data parsing and data
mapping processes is minimal. We also observe that the
average latency with gNMI notifications for each interface
set is higher than with NETCONF, due to the aggregation
of notification events considered in gNMI. In any case, the
average delay does not exceed units of milliseconds for each
set of interfaces.
Figure 12 depicts the latency results of the second
experiment, representing again the distribution of the average
FIGURE 12. YANG to NGSI-LD translation and instantiation latency.
processing latency as a function of the number of interfaces.
It is notable how this latency time is more affected by the
number of interfaces in this experiment. This is due to the
materialization stage during the data instantiation by using
the NGSI-LD API, which requires either more requests in
the case of gNMI, or requests with higher payload in the
case of NETCONF. This results in increased processing
time within the NGSI-LD Context Broker service. Even
so, the average delay does not exceed 300 milliseconds. It
should be noted that the processing time for instantiating
the data also depends on the implementation of the chosen
NGSI-LD Context Broker, with Orion-LD providing the best
performance.
For the throughput experiments, we compare the throughput of the YANG to NGSI-LD translation and the data
instantiation phases considering the maximum throughput
rate of incoming notifications on the Kafka message bus
during the data extraction phase. These experiments consider notification events using NETCONF and gNMI with
telemetry statistics from 48 interfaces for a period of
600 seconds. Figure 13 depicts the throughput results for
NETCONF, representing the average throughput resulting
from the translation of YANG to NGSI-LD and the data
instantiation phases considering the maximum event rate for
the extraction of telemetry notifications. We can see that
the maximum event rate for notification extraction is on the
order of 111 events per second and that the YANG to NGSILD translation phase supports this service rate. However, the
data instantiation phase limits the integration of the NDT
data to less than 6 events per second, which means servicing
telemetry notifications from less than 288 network interfaces
per second.
Figure 14 depicts the throughput results for gNMI. In such
a case, the maximum event rate for notification extraction is
on the order of 1,240 events per second and the YANG to
NGSI-LD translation phase also supports that service rate.
However, once again, the data instantiation phase limits the
integration of the NDT data to a maximum of 250 events
FIGURE 13. Throughput experiments for NETCONF notifications.
FIGURE 14. Throughput experiments for gNMI notifications.
per second. Since each notification event in gNMI has data
from only one network interface, this would mean servicing
telemetry notifications from approximately 250 interfaces per
second.
Then we can observe that the data instantiation phase
adds a significant delay and is a bottleneck in the NDT
data integration pipeline due to the high number of requests
made via the NGSI-LD API during the data materialization
process that cannot be serviced in time by the NGSI-LD
Context Broker. It should be noted that the limitations of
the results obtained may be exacerbated by the working
environment used, consisting of a single machine without
excessive computing resources running the prototype of the
Descriptive NDT solution based on Docker microservices. It
is expected that in a production environment based on servers
with more computing capabilities and a prototype solution
based on Kubernetes, the results could be significantly better.
There are also some additional proposals that could be
explored in the future to overcome these limitations. One
of them is to take advantage of the distributed or federated
architectures proposed by the NGSI-LD standard to improve
the scalability and performance of the solution. Deploying
different instances of Context Brokers and segmenting the
scope of the Descriptive NDT solution across the target
managed network would allow balancing the demands
of requests so that they can be served efficiently. For
this purpose, the NGSI-LD Context Broker implementation
of Scorpio [39] can be analyzed due to its support of
distributed NGSI-LD operations. Another proposal would
be to work on a variant of the Descriptive NDT prototype
solution where the data integration mechanism is based on
a data virtualization approach. As previously analyzed, this
alternative data integration approach can be more efficient
by eliminating the need to replicate and store the data in
the NGSI-LD Context Broker and sending it directly to
the interested consumers, thus improving the performance
benefits.
VI. CONCLUSION AND FUTURE WORK
This work introduces a new knowledge-based data integration system for modeling Network Digital Twin (NDT)
solutions. By relying on automated mechanisms, standard
interfaces, and standard data models, network management
can benefit from a comprehensive NDT platform for
network data integration, thereby facilitating uniform access
to network management data while abstracting from the
heterogeneity and complexity of the underlying real-world
networks. The Descriptive NDT solution proposed in this
work is a model-driven network management system that
can mirror the operational status and configuration of real
networks using both a data materialization approach and
a data virtualization approach. Our experimental prototype
allows to expose the capabilities of real networks by defining
representations of monitoring and configuration data in a
formal and interoperable model based on the NGSI-LD
standard, showing how an NDT can solve an important
challenge in telecommunications network management to
adequately reflect network behavior.
During this work, different challenges have been identified, which can become the starting point for future lines
of research. These include analyzing how to efficiently
handle the request overhead to integrate data from largescale networks into the NDT solution, which addresses the
requirements for massive data storage and high availability, as well as scalability and performance improvements.
Another area of interest would be to apply and analyze the
proposed digital mapping process methodology to translate
real network data into its NDT representation taking into
account other network management protocols and diversity
of monitoring data. In addition, we are investigating how
to extend the proposed NDT prototype to support actuation
mechanisms to apply configuration changes in the real
network and request telemetry data on demand by using data
integration approaches, thus closing the loop for network
automation.