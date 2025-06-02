Title: A Digital Twin Driven Human-Centric Ecosystem for Industry 5.0

Abstract— Industry 5.0 embodies the vision for the future of
factories, emphasizing the importance of sustainable industrialization and the role of industry in society, through the key
concept of placing the well-being of workers at the center of the
production process. Building upon this vision, we propose a new
paradigm to design human-centric industrial applications. To this
end, we exploit Digital Twin (DT) technology to build a digital
replica for each entity on the shop floor and support and augment
interaction among workers and machines. While so far DTs in
automation have been proposed for machine digitalization, the
core element of the proposed approach is the Operator Digital
Twin (ODT). In this scenario, biometrics allows to build a reliable
model of those operator’s characteristics that are relevant in
working contexts. Biometric traits are measured and processed
to detect physical, emotional, and mental conditions, which are
used to define the operator’s state. Perspectively, this allows to
manage and monitor production and processes in an operatorin-the-loop manner, where not only is the operator aware of the
state of the plant, but also any technological agent in the plant
acts and reacts according to the operator’s needs and conditions.
In this paper, we define the modeling of the envisioned ecosystem,
present the designed DT’s blue-print architecture, discuss its
implementation in relevant application scenarios, and report an
example of implementation in a collaborative robotics scenario.
Note to Practitioners—This paper was motivated by the
problem of designing human-cyber-physical systems, where production processes are managed by concurrently taking into
account operators, machines and plant status. This answers the
needs of the novel Industry 5.0 paradigm, which aims to enhance
social sustainability of modern factories. To this end, we propose
an architecture based on digital twins that allows to develop a
digital layer, detached from the physical one, where the plant can
be monitored and managed. This allows the creation of a digital
ecosystem where machines, operators, and the interactions among
them are represented, augmented, and managed. We discuss
how the proposed architecture can be applied to three relevant
scenarios: remote training and maintenance, line operation and
line supervision. Moreover, the implementation in a collaborative
robotics scenario is presented, to provide an example of the
proposed architecture can be implemented in industrial scenarios.
Index Terms— Industry 5.0, digital twins, human-centric
automation.
I. INTRODUCTION
I
N RECENT years, technological progress and changes in
the economy have significantly changed the manufacturing
industry, in terms of processes, products and market needs,
thus opening to new technological challenges and opportunities. In this challenging context, a significant change in the
human operator’s role has been observed. Low-skilled laborers
who perform simple and repetitive tasks have been displaced,
while the demand for higher-skilled labor has increased to
manage the plant, coordinate flexible production and control
complex and diversified technologies.
This has led to the introduction of the concept of
Operator 4.0 understood as a smart, skilled operator who
collaborates with machines and robots and can deal with
human-cyber-physical systems, advanced interaction technologies and adaptive automation. In such a symbiosis,
operators are assisted by automated systems, monitoring
their biometric signals, and providing a sustainable relief
of physical and mental stress and allowing them to utilise
and develop their creative, innovative and improvisational
skills, without compromising production objectives [1]. Moving along these lines, human-centricity of factories has been
elaborated further in the more recent paradigm of Industry 5.0, where the wellbeing of the worker is placed at
the centre of the production process and new technologies
are used to provide prosperity beyond jobs and growth,
while respecting the production limits of the planet [2], [3].
In this scenario, we envision a novel approach to design
human-centric industrial applications by exploiting Digital
Twin (DT) based technology [4], [5].
In Industrial Internet of Things (IIoT), the Asset Administration Shell (AAS) serves as a standardized representation
of industrial assets and processes, bridging the physical and
digital worlds. Through encapsulating relevant information in
a standardized format, it enables seamless integration and communication across industrial components. Our work embrace
this vision and the challenging goal of decoupling physical
complexity from digital applications via structured and flexible
intermediaries. We propose leveraging DTs as a Software
approach to encapsulate AAS functionalities and extend its
adoption in Industry 5.0 including cyber-physical relationships
and interactions for human operators as well, as depicted in
Figure 1 (left).
Our aim is to facilitate and make more efficient the interaction among human operators and technological systems in
the plant, including information about the operator, such as
their capabilities, their current status and workload, in the
management of the plant. To achieve this goal, we resort to
DTs, which allow to decouple the physical and the digital layers, solving the challenge of managing heterogeneous devices
and data (e.g., associated with industrial equipment, wearable
sensors, reality enhancement devices) through the creation of
a new uniform and standard abstraction layer. Data collected
by DTs can flow in a control room for the real-time analysis
of production procedures to help operators in taking decisions
and managing complex technologies depending not only on
available information and measurements of machines, processes and productivity, but also an accurate model of human
operators measured via wearable sensors. Hence, we build a
blueprint architecture for the digital representation of operators
and machines and the relationships among them through DTs,
as discussed in Section III. We then discuss its application in
the context of industrial automation in Section IV and propose
an experimental implementation in a scenario of collaborative
robotics (Section V).
A. Proposed Contribution
The proposed approach consists of the design of an ecosystem for industrial automation scenarios that supports and
augments interactions among humans and machines, thanks to
digital replicas of each agent, either human or technological,
on the shop floor. Specifically, the proposed contributions of
this work are the following:
• we propose a blueprint architecture for DTs in industrial automation and discuss its general application to
operators, resulting in operator digital twin (ODT), and
machines (machine digital twin, MDT);
• we combine ODTs and MDTs to shape an ecosystem
for human-centric cyber-physical systems, where agents,
either operators or machines, are abstracted, together
with their relationships and interactions, thus allowing an
orchestrated management of operations;
• we analyze the application of the proposed ecosystem in
different automation systems, providing guidelines for its
implementation in relevant scenarios.
Ultimately, the proposed ecosystem allows to comply with
the increasing design complexity of the next generation of
industrial human-cyber-physical systems, while taking the
most out of technology and human capabilities. Thanks to
the proposed approach, on the one side, the operator’s role
and peculiar characteristics (e.g., tasks, profile, behaviors,
expertise, real-time condition) can be taken into account as
a core input for production planning, process operation, productivity enhancement and the overall plant efficiency. On the
other side, it allows to effectively handle and manage the
massive heterogeneity and fragmentation of existing systems
characterized by a plethora of different devices, platforms,
communication protocols and data formats. The use of DTs
turns out to be useful in this regard, as detailed in the next
section.
II. STATE OF THE ART
With the advent of Industry 4.0, a striking feature of
modern manufacturing systems is the focus on advanced
automation. This combines technological progress and diversified needs of market, such as product customization and
small batches production. As a result, physical and digital
assets are integrated through the creation of smart products
and processes capable of transforming the conventional value
chains in cyber-physical systems [6]. To achieve this, the
use of disruptive enabling technologies has been fostered,
which include advanced autonomous and collaborative robots,
IoT (Internet of Things) and IIoT devices, cloud computing
and analytics, and artificial intelligence and machine learning.
As a consequence, one of the challenges of this paradigm
relates to the integration of these technologies. Reference
architecture models have been proposed, that provide technical
description and standards [7]. The main initiatives in this
regard are the 5C Architecture [8], the RAMI model [9] and
the IIRA model [10]. Although from different points of view,
these models focus on technological systems and consider
the human component in terms of technological management
of human-machine interaction. However, one of the major
requirements for such systems to work properly and efficiently
is the presence of reliable human operators, who cooperate
and work in symbiosis with advanced automated systems.
Some works has been recently presented in this regard. For
example, in [11] the authors have presented a human asset
administration shell (HAAS) as an analogous to AASs for
machinery and apply it to human-machine interaction and
ergonomics. More recently, the work in [12] have extended
this concept including a comprehensive understanding of an
individual’s cognitive state, physical wellness, and skill set in
the HAAS.
In this context, Romero et al. [1] introduced the term
Operator 4.0, to refer to operators of human-cyber-physical
systems who perform work aided by machines if and when
needed. Building upon these ideas, this concept has evolved
in the next industrial paradigm, namely Industry 5.0, which
has put focus on the importance of human-centricity of the
factories of the future [2]. Human operators are being placed
in the center of attention, in the sense that automation is
seen as a complement and enhancement of the cognitive
capabilities of humans by advanced sensing and the higher
precision of machines [13]. The idea of Operator 4.0 has
evolved into Operator 5.0 defined as a smart and skilled
operator who uses human creativity, ingenuity, and innovation, aided by information and technology, to develop new,
cost-effective and sustainable manufacturing solutions [14],
[15]. Additionally, Industry 5.0 has introduced the concept of
Healthy Operator [16], such that it is necessary to consider the
physical and mental well-being of skilled operators working in
highly automated industrial settings. The aim and the results
are more flexible, inclusive and safe workplaces, as well as
better work conditions, increased productivity and improved
quality. Moreover, this means increased worker satisfaction
and wellbeing, more empowered and engaged workers and
increased interest towards factory work as a career, attracting
young talented people.
Fig. 1. On the left side a schematic representation of the extension of the Industry 4.0 vision toward the native integration of human operators. On the right
side, the abstraction of the physical layer through the adoption of the Operator Digital Twin (ODT) and the Machine Digital Twin (MDT) as digitalization
tools for administration shells.
To enhance human-machine interactions, the analysis of
biometric information has been deeply analyzed in the state of
the art in order to investigate and understand how physiological
signals can be used to analyze affective states, focus, attention
and intent. Physiological patterns and cognitive workload can
be found in brain, cardiac, respiratory, electrodermal, muscular, skin temperature and eye (pupil dilation) signals [17].
An extensive review on methods for affect recognition, either
emotions or stress, from the analysis of physiological signals
has been recently presented in [18], with specific focus on
wearable devices. While there has been recent exploration
of biometric analysis from an architectural perspective [19],
the application of these methods to create a comprehensive,
synchronized representation of an operator by combining
production, environmental, and biometric factors over time is
a novel and interesting research opportunity. This approach
could foster fresh collaborative models within industrial
applications.
The scientific and industrial communities identified the role
of DTs to enable new interaction forms between physical
and digital layers [20], in particular in relation with IoT and
IIoT [21]. Traditionally DTs have been massively adopted in
different machine-oriented production stages and use cases [5],
in particular related to manufacturing [22], [23], [24] and
product design [25]. Only recently the idea of adopting DTs to
build a human replicas has been investigated both as general
concept in [26] and in specific domains such as industrial
training [27], health [28], fitness [29] and ambient assisted
living [30]. However, in current industrial applications, DTs
are mostly considered as tools for high-fidelity simulations,
thus not leveraging their potential to represent and augment
physical assets [31]. In [32] the high level notion of human DT
for Operator 4.0 has been discussed, while the work in [33]
and [34] has introduced a meta-model for a human DT in
the shape of a UML class diagram. Therein, the attributes
of such DT are presented, including worker’s medical, emotional and psychophysical condition, together with context
and environment features. However, it is not discussed how
the proposed human DT can interact with the surrounding
automation setting, for a human-in-the-loop management of
cyber-physical systems.
The current limitations of the existing approaches are
related to the fact that they are mainly focused on the
machine digitalization without investigating how DTs can
be also effectively exploited to digitalize an operator and
how it can cooperate and interact with equipment, colleagues
and production processes. Furthermore, there is also the
need to provide a comprehensive analysis and definition
of how to characterize and build a model specific to the
operator, taking into account not only static and production oriented information but also (and maybe primarily)
biometric signals in order to build a realistic and adaptive
representation. While some attempts in this regard have been
proposed with human-centric AASs and HAASs [11], [12],
[35], they have not been fully integrated with DTs. As a
result, without the encapsulation and abstraction capabilities
provided by DTs, managing this complexity within software
systems becomes challenging. DTs provide a structured way
to model, interact and augment physical assets, making it
easier to handle the intricacies of industrial environments and
providing a flexible way to enhance capabilities by adding
new functionalities. Hence, we believe that the availability
of a human-centric DT-based ecosystem would represent
a concrete step into human-centricity of factories of the
future.
III. THE PROPOSED DIGITAL ECOSYSTEM
In the IIoT, the AAS plays a crucial role as a standardized representation of industrial assets and processes.
It acts as a bridge between the physical world of industrial
machinery, equipment, and processes, and the digital world of
data analytics, automation, and control systems. As schematically depicted in Figure 1 (left), by encapsulating relevant
information about industrial assets and processes in a standardized format, the administration shell enables interoperability,
seamless integration, and efficient communication between
different components of the industrial ecosystem, such as
sensors, actuators, controllers, edge devices, cloud platforms,
and software applications. In this work, we foster this vision
by aiming for the effective decoupling between physical
complexity and digital applications through a structured intermediary. We propose, on the one hand, DTs as an effective
way to encapsulate AAS functionalities and potentially also
submodelling [36], and, on the other hand, to extend in an
Industry 5.0 vision the adoption of AAS through DTs for
the comprehensive digitalization of industrial operators and
Fig. 2. The representation of the abstract blueprint architecture of a DT (left) and its hierarchical branching to ODT and MDT (right) with their cyber-physical
relationships.
the enabling of simplified coordination between humans and
machines in industrial environments.
Figure 1 (right) depicts an overview of the proposed
approach. More specifically, each human operator working
on the shopfloor is represented in the digital space by an
ODT responsible for building and maintaining a digital replica
and interacting with both physical assets and colleagues.
Each ODT collects the user’s data and simplifies interaction
with the physical environment, abstracting from the existing
heterogeneity of deployed devices and processing all relevant
data that may impact productivity, wellbeing and working
behavior. As a result, it is possible to build a dynamic and
evolving profile associated to operator’s capabilities and physical, emotional and cognitive states. Additionally, technological
agents, such as automatic machines, robots, tooling machines
and sensors, are represented in the digital layer by MDTs,
which collect relevant information and behavior and share
them with the other agents. Relationships among operators and
machines are not only reproduced in the digital layer, but are
also actually supported by merging and processing information
coming from the field. As a result, production processes can
be managed by concurrently taking into account operators,
machines and plant status.
In order to simplify and uniform the creation of ODTs
and MDTs in the envisioned ecosystem, we have structured a
common blueprint architecture (depicted in Figure 2) built on
top of the recent state of the art principles [37], [38]. Thanks
to such an architecture, ODTs and MDTs share a set of core
abstract properties and modules that can be then characterized
to digitalize operators and connected machines, together with
their relationships over time. The first identified capability that
we model into our reference DT architecture is related to the
concept of Representativeness & Contextualization. Each DT
should be independent and autonomous to model and represent
as much as possible its physical counterpart within the context
where it is operating, in terms of attributes (e.g. biometric
information, assigned tasks, profile, etc . . . ), behaviors (e.g.,
actions that can be performed by the operator or on one of its
associated devices) and relationships (e.g., a coworker and a
machine within the same production process). From a technical
point of view, this fundamental capability has been associated
to the core component denoted as Digital Twin Model. It is
responsible to decide at the same time how and when variation
of the physical world should be mapped into the digital
replica or inputs and actions performed on the twin should
be propagated to the associated physical entity. On the one
hand, the model works side-by-side with the Digital Twin State
with the specific responsibility to structure, store and expose to
other components all the computed attributes and relationships,
together with their changes over time. On the other hand,
the model receives inputs from the physical layer through a
set of Shadowing Module(s) in charge of implementing the
second core DT’s capability, called Shadowing. It refers to
the accurate measurment of the physical counterpart over time.
Each physical attribute (e.g., biometry from wearable devices)
can be reflected from the physical environment without any
changes or it can be transformed during the process in order to
properly match the modeled state (e.g., re-sampling the signal
or adapting its representations). Nevertheless, the shadowing
process involves also the possibility to retrieve or automatically detect physical relationships involving the target DT with
other external entities or DTs, as detailed in Section III-C (e.g.,
a robot inside a plant, belonging to a production line and used
by an operator).
The capability of a DT to interact with the physical layers
has been modeled through a set of Physical Adapters in charge
of communicating with connected devices reading data and
triggering actions according to the adopted protocols and data
formats and following the behaviours implemented through the
shadowing functionality and the internal DT’s model.
Furthermore, since physical objects come with well-defined
functionalities and services that are fixed for the entire life
cycle of the object, the modeled abstract DT architecture
can leverage its digitalization capabilities in order to modify,
update and improve its representation over time by implementing the Augmentation capability. In other words, a physical
asset can be functionally augmented through its DT (and a
set of Augmentation Modules) extending its capabilities and
defining new attributes or relationships that were not originally
available on the physical counterpart.
Since the aim of a DT is to bridge the cyber and the
physical worlds through a simplified digitalization process,
an additional fundamental functionality for the designed DT’s
architecture is the possibility to interact with the digital layer
(e.g., applications, services and other DTs) through multiple interoperable and standard interfaces, protocols and data
formats at the same time in order to realize an effective
DT-driven ecosystem. Following this principle, each DT can
instantiate one or multiple Digital Adapters allowing at the
same time the exposition of the current DT’s state together
with the possibility to receive commands to execute actions
or dynamically adapt the implemented behaviours. Moreover,
the combination of DT’s augmentation capabilities with the
structure of digital adapters offers a versatile approach to facilitate and empower the mapping of AAS submodelling [36],
enabling the extension of functionalities, structure, and characteristics of the digital replica, as well as the representation
of assets in the digital realm through an interoperable and
standardized approach. This expansion is achieved without
compromising the modularity of the software instance, which
remains modular due to the architecture of the DT.
Relying on the presented abstract architecture, in the following sections we present its characterization for the definition of
ODTs and MDTs. We provide a specific and detailed focus on
the ODT and the interactions and collaboration between ODTs
and MDTs, since MDTs have been already analyzed in the
scientific literature and implemented in production solutions.
A. ODT Modeling
The ODT aims to represent those characteristics that
are relevant from the point of view of interaction with
complex systems, according to [39]. Other human characteristics and capabilities that do not affect the interaction
with socio-technological systems and the operator’s working
scenario are out of the scope of the ODT modeling.
From a technical point of view, following [33] and [39],
to implement the Representativeness & Contextualization
capability of the ODT, the attributes of the ODT’s state are:
• Profile: a set of static values associated to the operator,
such as their role or training level.
• Task: the list of production related assignments or duties
useful to check or identify the type of actions performed
or detect anomalies and dangerous situations.
• Biometrical: attributes associated to biometric signals
(e.g., electrocardiogram (ECG), electrodermal activity
(EDA), electroencephalogram (EEG), eelctromyiogram
(EMG), etc . . . ), collected through wearable devices worn
by the operator.
• Behavioral: parameters related to actions performed
by the operator, for example while interacting with a
machine (e.g., driving a vehicle or using a specific tool)
or with other colleagues through the production line.
• Situational: characteristics based on the current operator’s
context and the detected circumstances. These are typically represented by specific conditions computed through
the analysis of multiple biometrics signals and associated
to the detection or prediction of a specific operator status
(e.g., an increase of fatigue while interacting with a
machine).
Fig. 3. A schematic mapping between physical and digital attributes through
the shadowing process able to compute both biometric signals and enrich the
ODT state evaluating additional situational attributes (e.g., the stress status).
• Environmental: attributes associated to the environment
where the operator is working and useful to support both
local awareness (e.g., current detected temperature) and
interactions patterns (e.g., the presence of an actuator to
control a functionality).
• Time & Location: attributes useful to support the contextualization of the ODT, properly tag received data and
computed attributes and enable both historical and future
analysis (e.g., predict the value of a stress condition).
Figure 3 depicts this idea. On the one hand, it illustrates the
relationships between physical and digital attributes through
biometric shadowing, which is responsible to mirror the current state of the operator through measured signals. On the
other hand, the same attributes can be used and processed to
evaluate new augmented attributes enriching the ODT’s state
and the awareness of its counterpart.
B. MDT Modeling
The design and development MDTs has been massively
studied in the literature and recently revamped following
both industrial specifications and scientific contributions [40],
[41], [42]. In this section, we analyze, on the one hand,
how the proposed DT’s architecture is aligned with existing
requirements and, on the other hand, how it is able to extend
MDTs supporting the collaboration with operators through
their ODTs.
The fundamental responsibility of an MDT is to digitalize its industrial machine’s physical counterpart through a
mapping over time of its core attributes and properties, with
respect to the target operational context (e.g., rotation speed,
joint position, or operational parameters). At the same time,
the MDT is responsible for the management of incoming
actions from the digital layer (e.g., reducing robot speed
or changing target task) and the associated actuation on
the physical machine. Furthermore, each MDT can augment
original physical attributes and capabilities by integrating
new data coming from external data sources (e.g., production scheduling information from the manufacturing execution
system or details about maintenance procedures) or extending
provided functionalities (e.g., introducing anomaly detection
skills or increased interoperability with the support of multiple
application protocols).
An MDT exploits the same blueprint architectural modules
adopted in the ODT. As weel, it builds its behaviors through
Fig. 4. An illustrative representation of the digitalized relationships between operators and machines through their DTs counterparts together with their
exploitation supporting direct and indirect interactions.
the combination of the internal DT’s model and the interaction with the Shadowing and Augmentation components.
Communication with the physical and the digital worlds are
enabled and supported through the dedicated adapters. Such
adapters enable the management of the massive fragmentation
of deployed IoT and IIoT devices and allow a uniform and
interoperable interaction with digitalized machines through
standard protocols and data formats.
The exploitation of this homogeneity and interoperability, combined with a structured characterization of ODTs
and MDTs, represent the pillars for the envisioned Industry
5.0 extension, where machines and operators can effectively
collaborate by means of DTs.
C. ODT & MDT Relationships and Interaction Patterns
A fundamental contribution of the proposed DT-based
approach is the possibility to map and keep updated the knowledge of the relationships between operators and machines.
This information can then be leveraged to improve intelligent
and secure cooperation while simplifying coordination, thus
alleviating the challenges linked to directly managing physical
assets. Figure 4 schematically illustrates both the digitalized
knowledge maintained by each DT together with direct and
indirect observation and interaction patterns among active
entities.
On the one hand, in its internal state, each DT maintains a structured digital representation of the list of all the
relationships coming from the physical world in which it is
involved. Relationships can involve at the same time both
ODTs and MDTs according to the nature of the tie and are
stored on the two sides of the link. For example, the use case
of an operator working with a robot on a specific task (t)
generates a relationship between ODT (e.g., ODT-1) and MDT
(e.g., MDT-1) that is mapped at the same time on the two
independent DTs modeling the following associations: i) on
ODT-1: working with MDT-1 for task t; and ii) on MDT-1:
used by ODT-1 for task t. On the other hand, the knowledge
of the existing relationships in the physical environment combined with the uniform interaction capabilities provided by
DTs enables the simplified cooperation between operators and
machines, achievable both directly and indirectly according to
the use case.
In a direct approach, ODTs and MDTs can observe and
interact with each other without any intermediate component
to retrieve specific properties (e.g., the stress/fatigue level of
an operator or the telemetry of the robot’s joint) and/or to
invoke target capabilities or behaviors (e.g., reduce robot speed
or assign a new task). For example, with reference to the
middle panel of Figure 4, considering a simplified use case
with a robot (MDT-1), a senior operator (ODT-1), and a junior
operator (ODT-1), we can easily enable a scenario where: i)
ODT-1 assigns tasks to both MDT-1 and ODT-2; and i) MDT-1
is aware of the collaboration with ODT-1 and ODT-2, observes
their stress level to automatically reduce its execution speed
if an anomaly condition is detected.
On the opposite side, observation and interaction can be
managed by adopting one or more intermediate entities that
are aware of deployed DTs and their relationships and are
in charge of managing and orchestrating the deployment,
while keeping a centralized and synchronized view. With
respect to the same illustrative example, in the right panel
of Figure 4 we introduce a Manager/Orchestrator responsible
for observing stress levels and task execution of ODTs and
interacting with the MDT to change the target assigned task or
modify the machine’s speed according to the detected context
(e.g., reduce speed in case of a detected stress condition
involved operators). Direct and indirect patterns are not meant
to be necessarily independent but they can be combined and
adopted following application scenario specifications, security
targets, and autonomy requirements while preserving the same
abstraction capabilities on top of the physical layer.
IV. RELEVANT SCENARIOS
In this section, we discuss three relevant scenarios where
to apply the proposed digital ecosystem. These scenarios
have been selected since they are representative of different
interactions among agents on the shopfloor. In particular, while
the use of DTs in such contexts has been largely explored (see,
e.g., [43]), here we discuss how the concept of ODT and the
whole proposed digital ecosystem can be applied to shopfloor
organization, information management, and operator’s task
assignment. We provide guidelines about how the ecosystem
can be instantiated in the different scenarios, presenting the
corresponding functional modules to be implemented in the
digital layer.
A. Remote Training and Maintenance
In this first scenario, we refer to training and customer
service provided by manufacturers to remote plants and
machinery at customer’s premises. Remote service allows
manufacturer’s expert engineers and technicians to provide
remote assistance and training for troubleshooting in the event
Fig. 5. Analyzed Use Case are the following: (a) Application of the proposed ecosystem to remote training and maintenance.; (b) Application of the proposed
ecosystem to line operation.; and (c) Application of the proposed ecosystem to line supervision.
failures, periodic maintenance and continuous monitoring.
While some services can be provided automatically and fully
remotely, on-site presence of an operator for local intervention
is often required. In addition, remote service can be leveraged
to train local operators.
In this context, real-time decision support, remote monitoring, and training capabilities can be provided through
the use of DTs and interactive display technologies, such as
Augmented Reality (AR) and Virtual Reality (VR).
Figure 5(a) schematically illustrates the scenario. A technician interacting with the industrial equipment is supported
in real-time by an AR system, which provides contextualized
information, such as visual feedback (e.g., real-time data
from the machine or production specifications) and operational
instructions (e.g., videos, 3D models). Displayed information
and data are dynamically generated and adapted according to
the type of technician and their experience and a set of biometric and environmental parameters (e.g., eye activity, fatigue,
ergonomy assessment, room temperature, etc.) collected from
the field.
Training and maintenance can be remotely controlled and
supported by a remote service manager who guides the
technician, validates their actions, provides customized AR
feedback, and prevents wrong or dangerous operations. Interaction between on-site technician and remote service can be
managed at an abstract digital layer, which contains a digital
representation of the on-site scenario and where the technician’s ODT, MDT, and training material lie. With reference
to Figure 4, the considered remote assistance scenario can be
seen as an example of hybrid observations and interactions
patterns, since the interaction between ODT and MDT is not
direct but is managed by the remote service support, through
a Control Room, which has the role of Manager/Orchetrator.
As shown in Figure 5(a), the architecture of the digital representation of on-site relationships can be organized into three
different modules. First, the Assistance Procedures Manager
(APM) module defines each step of training and maintenance
processes. Such steps can be completely autonomous and
handled by the industrial machine or require manual intervention or configuration from the operator. The Augmented
Reality Engine (ARE) module is responsible for the interaction with any AR wearable device worn by the technician.
By communicating with the associated ODT, it provides realtime multimedia content supporting the operator during each
phase of training or maintenance. It can also interact with
the Assistance Manager (AM) module to receive feedback
and contents from the remote specialist in order to adapt
the AR behavior with respect to the selected procedure, the
status of the equipment, and the actions of the technicians.
AM provides an interface to design and execute AR-driven
training or service sessions through a remote expert operator
and a technician in the plant. Each training can be associated with one or more procedures defined through the APM
module. AM interacts also with ARE and ODT in order
to dynamically adapt contents and information for the AR
module and to support a bidirectional effective communication
with the operator.
B. Line Operation
This scenario refers to an operator responsible for a single
production step. To keep the discussion general, we consider an operator working at a collaborative workstation,
where different pieces of equipment, such as sensors, automatic machines, and/or robots, are installed. The workstation
receives input (i.e., raw material or preprocessed pieces) from
previous cells and provides processed pieces as output to the
following workstation.
By applying the proposed ecosystem to this scenario,
we envision the workstation represented at the digital level
as the collection of the ODT and the MDTs of the M IoT
devices in the workstation, and their relationships. Operator’s
interactions can be sketched as 1 ODT → {M MDT}. Workstation operation is, then, managed considering not only events
occurring in the physical layer, but also augmented information
brought in the digital layer by each DT. The production
process can be then orchestrated to seamlessly account for
any specific request or need coming from human and technological agents. Examples in this regard are atypical sensor
readings, lacking or queuing input materials, and machine
failures. In the presence of any of these events, their effect
can be mitigated by reprogramming the way the workstation
operates. Additionally, information about the operator’s state,
extracted from biometric measurements and processed by
ODT biometric shadowing, can be included to workstation
management. As discussed in Sec. III-A, information about
fatigue, discomfort, posture or user’s skills is made available
by the ODT and can be used to influence the behavior of the
workstation, as well. Workstation operation and management
can be then optimized including such information and leveraging the operator’s skills and compensating for any (temporary)
decline. When needed, appropriate assistive strategies can
be implemented to meet operators’ needs and relieve their
discomfort.
A possible architecture for this scenario is shown in
Figure 5(b). The operator and the workstation are mapped in
M MDTs and an ODT and the way they collaborate and interact is managed by a Manager/Orchestrator. Specifically, the
Manager/Orchestrator takes into account information regarding the operator’s status (mapped in the ODT), workstation
operation (mapped in the MDTs), production planning (coming from industrial digital services, such as ERP), and other
workstations in the same line. These pieces of information
are merged to manage the production of the workstation,
through a Production Manager (PM) module. This module
defines the sequence of production processes for the operator
and the workstation, with the details of operational steps.
To this end, PM interacts with the Production Procedure Manager (PPM), which stores production recipes and instructions.
PM interacts also with the Assistive Strategies (AS) module, where the assistive strategies are defined as algorithmic
policies that determine the abstract behavior of each agent
in the workstation. Such policies consist of hardware and
application-independent rules and methods that describe how
the workstation can be adapted to the current situation and
measured the operator’s state. Each agent’s MDT is then in
charge to instantiate them depending on the specific physical
features of its agent. Implementing any of these strategies
requires collecting information from ODT and MDTs and
coordinating the operator and the agents in the workstation
to reconfigure the production process according to PPM.
With reference to Figure 4, this architecture implements an
indirect observation and interaction pattern, since the collaboration among agents is managed by the Manager/Orchetrator,
which observes them and coordinates their interactions.
C. Line Supervision
Another use case where we envision the proposed ecosystem
refers to the supervision of production lines. The typical
setting for this scenario consists of an operator responsible
for overseeing the operation of a production line. The line
is operated by several operators, each assigned to a specific
production step, as in the case discussed in Subsec. IV-B, and
is composed of different interconnected workstations. High
variability can be found among operators and equipment: this
last often includes devices from different manufacturers, while
operators have different expertise, skills, and plant knowledge.
Line supervisor’s responsibilities consist in coordinating operations, ensuring that all workers are doing their jobs correctly,
machinery is operating as expected and production goals are
met. To achieve this, supervisors rely on a control panel, which
runs on a dedicated human-machine interface (HMI) and is
connected to equipment in the line. Specifically, while monitoring production processes, the supervisor’s role is to take
proper intervention when displacement from nominal behavior
occurs, isolating causes, identifying strategies to solve them,
and reorganizing the line in the short term. To this end,
different pieces of information are needed: on the one side,
an overview of line status is constantly required, to monitor
production processes. This includes raw and/or processed data
about the availability of input materials, line throughput and
other key performance indicators, and major equipment status.
On the other side, a detailed view of each stage of the line
might be necessary, especially in the presence of alarms or
specific needs of the corresponding operator.
Applying the proposed ecosystem to this scenario results in
the architecture depicted in Figure 5(c). Therein, we consider
the general case where the line is operated by N workstations,
and the i−th workstation has Oi operators and Mi pieces of
equipment, where i = 1, . . . , N. Line management is enabled
by a digital layer, where a replica of the line is represented in
the Line Overview (LO) module. In such a replica, each agent
is mapped in the corresponding DT, and relationships among
agents (e.g., who is working with each piece of equipment)
are mapped as well. In other words, LO presents a functional
hardware-independent abstraction of the production line and
provides access to raw or processed information of each agent
operating the line, through the Shadowing and Augmentation
modules of each ODT and MDT. Line management is enabled
through a Line Controller (LC) module that provides an
interface to the line supervisor. LC interacts with LO and
coordinates all the workstations assigning them production
tasks depending on information coming from PM about production scheduling. Additionally, LC allows to tackle of faults
and undesired events: these are shadowed in LC and can be
detected by either LC itself, through the Augmentation module
of DTs or PM. Once detected, the Troubleshooting module
provides instructions and procedures to solve them. In terms
of the interactions patterns in Figure 4, this scenario can
be implemented in either direct or indirect mode, since the
line supervisor might interact directly with each single DT or
with the Manager/Orchestrator of a workstation (not shown
in Figure 5(c).
D. Security & Privacy Considerations
The direct management of raw biometric signals and personal information by the ODT potentially opens to privacy
and security critical issues and threats. Although the aim
of this paper is not directly related to these challenging
aspects, we believe that a few considerations on the topic are
fundamental in order to better contextualize the role of DTs
with respect to the security of their physical counterparts.
A DT (and in our specific case an ODT) defines a trusted
relationship and a strong linkage between a physical object
and its digital replica. Extending this concept, we can envision
the DT as the unique digital gateway allowing the communication between the two worlds. In our application scenario,
this means that a connected operator can exploit their own
ODT as the unique entry point for any connected digital
services in the factory; on the other hand, those services
Fig. 6. Timeline and setup of the considered case study.
can observe and interact with the operator only passing
through its digital replica. Therefore, the ODT is in charge of
securely communicating with the operator and their devices
(e.g., wearable and augmented reality headset), processing
incoming information and directly controlling who car read
or modify available attributes, or invoking specific methods
according to their role and authorization level. Side by side
with secured communication technologies, the ODT can also
introduce data anonymization and obfuscation techniques to
support interoperability and guarantee service operation while
preserving privacy. Exchange of operator’s data and their
interaction with machines and cyber-systems can be then managed implementing security protocols and following formally
specified and analyzed security ceremonies [44], [45].
Relying on these considerations, the extension and detailed
definition of ODT security modules and behaviours are currently out of the scope of this work and will represent an
appealing research opportunity of next future activities.
V. CASE STUDY
We implemented the proposed ecosystem in a collaborative
assembly use case, where a human worker and a collaborative
robot work together in a shared workspace. With reference to
the relevant scenarios described in Sec. IV, this use case is
a laboratory implementation of line operation, where, for the
sake of simplicity, we considered L = 1 machines, namely
the robot. Considering a prototypical scenario, the robot is in
charge of presenting different pieces to the worker, who is
in charge of assembling them. We assume that the parts to
assemble are variable and, hence, human cognitive flexibility
is required to assemble the final pieces. As a consequence,
it can be expected that the task induces mental fatigue and a
decrease in cognitive capabilities during the shift. Consequent
adaptation of the robot’s behavior is beneficial for the worker
if the robot is informed when the worker feels tired and slows
down the pace of the assembly task, as an assistive strategy.
The timeline of the experiment is shown in the left panel
of Figure 6. The upper panel shows robot’s and operator’s engagement in picking pieces and assembling them,
respectively. At the beginning, they are synchronized and the
operator is ready to assemble any new piece just provided by
the robot. In this condition, the operator is not fatigued and the
robot moves with nominal speed. However, after some time
(left red dashed line in Figure 6(a)), the task requires longer
assembly time to the operator, who is no more able to keep
robot’s pace. This reflects in an increase in operator’s fatigue,
which is detected by the corresponding ODT, as presented in
Sec. V-A. As a result, the Manager/Orchestrator is informed
and commands the MDT to reduce robot’s pace as an assisitve
strategy. In the following assembly tasks, the operator is, then,
given more time to assemble new pieces and, as a resut,
their fatigue is decreased. When this is detected by the ODT,
the Manager/Orchestrator commands the robot to restore its
nominal pace (right red dashed line in the figure).
The scenario was reproduced in a laboratory setting,
as shown in Figure 6(b). To this end, we used the Nyrio Ned1
collaborative robot and operator’s fatigue was detected with
the BITalino (r)evolution Plugged Kit BLE/BT device,2
shown
in the right of Figure 6(b). It is a wearable device specifically
designed for recording several different biosignals, namely
ECG, EMG, EEG, and EDA, together with accelerations. The
device supports Bluetooth connection and can be arranged in
a modular manner with different configurations. As a consequence, its digitalization in a DT allows it to deal transparently
with multiple configurations and provide a standard output to
any consumer agent.
In the rest of the section, we first discuss how the ODT was
implemented with specific focus on mental fatigue detection
(Sec. V-A). Then, the implementation of the MDT is presented
(Sec. V-B), together with an analysis of how physical complexity can be reduced by resorting to the proposed DT based
framework (Sec. V-C) and the implementation of the digital
orchestration layer (Sec. V-D).
A. ODT
As regards the ODT, the proposed validation focused on the
Shadowing and Augmentation modules of biometric attributes.
Such modules are responsible for receiving and processing
the operator’s activity and estimating their current status,
as depicted in Figure 3. In particular, we here focused on
estimating mental fatigue, which is the condition that typically
arises over prolonged working shifts. The use of physiological markers is an established tool for the quantitative and
objective detection of mental fatigue. In particular, variations
in electrodermal and cardiac activity can be observed during
either moderate and intense cognitive load [17], [46]. To record
such physiological activites, sensors were placed as shown in
Figure 6(b), considering standard positions used in clinical
practice.
The ODT was implemented leveraging the open source
project WLDT,3
a modular Java software stack to effectively
implement DTs through their communication capabilities,
shadowing procedures, and augmentation functionalities [47].
The library was also extended to introduce a BITalino Physical
Adapter to retrieve data from the board via Bluetooth Low
Energy (BLE) and properly parse the adopted proprietary data
format. Furthermore, a specific module was introduced to run
Python scripts within the DT logic to support the execution
of data analysis algorithms and machine learning models and
support the estimation of mental fatigue conditions. Specifically, the Augmentation module of the ODT was in charge
of data filtering, feature extraction, and affect estimation. It
can be implemented according to the methodology presented
in [48], which consists of an unsupervised machine learning
pipeline to discover patterns and groups in physiological signals recorded under the different fatigue conditions. However,
in the considered experimental validation, fatigue occurrence
and estimation (second and third panels in Figure 6(a)) were
simulated. A Digital Adapter was also created and integrated
into the ODT with the aim to expose the computed state to the
external world and to allow a simplified observation of monitored stress conditions. The designed adapter uses the MQTT
protocol [49] for asynchronous Pub/Sub communication and
implements a traditional IoT topic structure composed by the
following topic: i) Info: publishing the description of the ODT
with its structure and capabilities; Telemetry: notifying any
variation of the state’s properties (e.g., raw biometric signals);
Event: sending messages and notification when a specific
situation occurs (e.g., a detected stress condition); and Action:
supporting the reception of incoming messages associated,
for example, with alert notification for the operator or the
variation of the execution task (visualized on its personal or
wearable device). Outgoing and incoming messages were also
uniformed and standardized through the adoption of SenML
data format [50] and serialized through the JavaScript Object
Notation (JSON) [51].
B. MDT
In the considered case study, the MDT has the responsibility
to digitalize the collaborative robot allowing bidirectional
communication by reading the telemetry (e.g., joints position,
execution speed, and effector status) and enabling the execution of specific actions on the machine (e.g., task assignment,
speed variation, and movement coordinates). This physical
interaction was designed and implemented on the MDT
through the creation of a dedicated Physical Adapter in charge
of mapping the communication with the robot through the
Robot Operating System (ROS)4 protocol by using the Niryo
Ned custom library PyNiryo25
together with RosLibPy6
and
3White Label Digital Twin - GitHub - https://github.com/wldt.
4ROS - The Robot Operating System - https://www.ros.org/.
5PyNiryo2 - https://docs.niryo.com/dev/pyniryo2/v1.0.0.
6Python ROS Bridge library - https://roslibpy.readthedocs.io/en/latest/.
TABLE I
DETERMINING THE PCI FOR THE SPECIFIC USE CASE ASSESSING
THE ADVANTAGES, ACHIEVED THROUGH THE VARIOUS IDENTIFIED
PARAMETERS AND THEIR CORRESPONDING CIF VALUES
Fig. 7. Schematic representation of the physical complexity in the target
use case considering results with and without the adoption of DTs and the
Importance Factor (IF).
ROSBridge module7
allowing clients to publish or subscribe to
ROS topics and call ROS services through a variety of transport layers, including WebSockets and TCP. The developed
adapter has been integrated into the WLDT library with the
aim to use the same code structure adopted for the ODT and
focus on the peculiarities of the MDT only.
A dedicated Digital Adapter was designed and integrated
into the MDT in order to expose the computed state and to
enable the external digital invocation of actions on the robot
related to changes of its operational speed (e.g., when a stress
condition has been detected). Following the same approach
adopted for the ODT, this adapter uses the MQTT protocols
for an asynchronous and Pub/Sub communication approach
and is aligned with the same topic structure (info, telemetry,
event and action). Nevertheless, both outgoing and incoming
messages are homogeneous and based on the SenML data
format serialized through JSON.
C. Physical Complexity
In our experimental evaluation, we also estimated the impact
of digitization and decoupling of responsibilities by estimating
the scenario’s complexity with and without the adoption of
DTs. In order to assess the effectiveness of the management
of physical heterogeneity and complexity according to the proposed approach, we exploited the indicator denoted Physical
Complexity Indicator (PCI) presented in [52].
The PCI measures the perceived complexity associated with
an application working with the physical layer (e.g., the
coordinator of the production line) and considers criteria such
Fig. 8. Sequence diagram of the considered case study where physical and digital world are bridged through DTs, which are exploited by the control room
to orchestrate operations.
as: i) Required Protocols (p): the number of protocols required
by a digital application or service to interact with the deployed
physical devices to collect data and to send commands;
ii) Communication Patterns (c): the number of communication
patterns needed to interact with involved devices and platforms
(e.g., Publisher/Subscriber or Request/Response); iii) Data
Formats (d): the number of different data formats, serialization, and information representation techniques required to
read and send data from and to deployed devices; iv) Interaction Points (n): the number of different modules, services,
or platforms that an application should interact with to retrieve
all the target data or consume services; and v) Aggregation
Points (a): the number of aggregation or composition levels
required to abstract the physical world into the right level of
complexity with respect to the observers’ typologies and their
application goals (e.g., merging information and telemetry data
from machines in the same production line). Each parameter
is then associated with a specific Criteria Importance Factor
(C I F) ranging from 1 (lower) to 3 (higher), used to weight
specific criteria considering their impact on the development,
deployment, and maintenance of the solution. The current CIF
values draw from established scientific references employing
similar principles [52], [53], as well as from the experience
in the IoT and IIoT domains, emphasizing reliability and
relevance in assessing application complexity interacting with
the physical layer. Specifically, they underscore the technological complexity’s impact and the associated management
costs regarding communication protocols, data formats, and
interaction/aggregation points. In the current IoT and IIoT
landscape [54], [55], characterized by ongoing standardization
efforts, these interoperability aspects remain the most challenging to navigate, demanding specialized knowledge of the
physical world and dedicated implementations for bidirectional
information disambiguation with physical entities. While these
values may vary in well-structured, interoperable deployments,
the prevalent fragmentation in real-world scenarios makes such
homogeneity currently unlikely.
The evaluation of physical complexity for our experimental
use case, taking into account the identified PCI and comparing the exposed physical complexity with and without the
use of DTs (reported in Table I), is presented in Figure 7.
We have assigned a high significance level (C I F = 3) to
effectively manage diverse data formats (criterium d) and
determine the number a of aggregation points required for
constructing robust data structures. These factors play a critical
role in enabling distributed coordination between operators
and robots. On the other hand, a medium level of impact
(C I F = 2) has been attributed to the adoption of heterogeneous data protocols (p) and engagement with multiple
active entities (n). This assessment is due to their potential influence on overall complexity, especially in scenarios
involving an increased number of active entities. We have
assigned a lower level of importance (C I F = 1) to simultaneously adopting multiple communication patterns (c). This is
because, in contemporary applications, it is quite common and
widely accepted to utilize various communication techniques
concurrently, particularly within intricate distributed environments. As regards PCI values, in our application scenario,
on the one hand, we have the physical robot communicating
using ROS and custom data formats and communication
patterns (Pub/Sub with Nyrio topics), and, on the other hand,
a BITalino device connected through low energy Bluetooth
connectivity and using platform-specific messages and interaction flows monitoring the operator (p = c = d = 2).
An intelligent industrial orchestrator should directly handle
this fragmentation in terms of protocols and data structures
and also manage the interaction with active entities together
with the associated required modules (ROS architecture and
Bluetooth adapter). This results in a scenario with n = a =
2 and an overall PCI equal to PC I = 10 and PC IC I F = 22,
considering the correction of impact factors. On the opposite,
the introduction of DTs allows the creation of a uniform
digital layer where a single protocol (MQTT), communication
pattern, and a unique data format (the standard SenML [50]
with JSON serialization) are adopted. As a result, p = c =
d = n = a = 1 and PCI reduces to PC I = 4 and a final
PC IC I F = 8 applying identified impact factors.
The depicted values demonstrate how DTs can effectively
reduce physical complexity, enabling an intelligent service to
interact with a uniform digital interface and focus solely on
data processing and generating intelligent insights. Provided
advantages can be limited in the simplified reference use case
while can be significantly augmented by taking into account
complex production lines with multiple robots and operators
cooperating together on the same task through different technologies, implementations, and communication approaches.
D. Digital Orchestration
The coordination between the operator and the robot is
managed by a digital Orchestrator responsible for synchronizing, scheduling, and monitoring the robot’s and operator’s
actions, tasks, and conditions. Thanks to the availability of
a homogeneous digital layer hosting ODT and MDT, for the
Orchestrator it is not relevant on the one hand if the robot
is from a specific manufacturer or connected through a target
required protocol or on the other hand if operator’s wearables
and HMI assets belong to a specific group of supported
devices. The only requirement is that there are DTs responsible
for the robot’s and operator’s digitalization and for maintaining
the same agreed level of abstraction and interaction.
The implementation sequence of the proposed coordination is depicted in Figure 8, which shows how information
about the process is shared between the robot and the
worker, through their DTs. They initially authenticate to the
Orchestrator, which starts the process of assigning tasks
and publishing them on the topics /operator/id/action
and /robot/id/action. Task assignment can be managed by
matching the operator’s capabilities and the robot’s characteristics (retrieved from their topic id) with production planning.
During task execution, the Orchestrator is constantly informed
about robot movements, actions, and events since the robot
publishes such information on the corresponding topics. When
the Augmentation module of the ODT detects arousal of mental fatigue, this information is forwarded to the Orchestrator on
the topic /operator/id/event. Hence, the Orchestrator commands the robot to adapt its behavior and implement proper
assistive strategy, by changing task execution features through
the topic /robot/id/action. If mental fatigue decreases to
normal workload, this information is shared again through
the topic /operator/id/event, and assistive strategies are
deactivated through /robot/id/action to restore the nominal
behavior of the robot. When the task is completed, the robot (in
the case of Figure 8) or the operator informs the Orchestrator
through the corresponding topic action and the information
is forwarded to the other agent.
VI. CONCLUSION
In this paper, we introduced a novel human-centric approach
for human-cyber-physical systems in industrial scenarios. The
proposed architecture relies on the concept of DTs to develop
a digital layer, detached from the physical one, where the
plant can be monitored and managed. This allows the creation
of a digital ecosystem where machines, operators, and the
interactions among them are represented, augmented, and
managed. A pivotal component of such an architecture is
the ODT. This is a digital replica of each human operator
working in the plant and collects relevant human attributes
that affect, or are affected by, interactions and collaborations
with the automation system. Specifically, the ODT includes
static features, and most importantly, dynamic features that
summarize the current condition of the operator. Among such
features, biometric traits allow to have a detailed understanding
of their affect, such as attention, physical or mental fatigue,
and engagement in working tasks. The ODT allows collecting
such data directly handling the heterogeneity and fragmentation of the physical layer and augmenting them to get an
objective, broad and implicit estimate of the operator’s state.
Ultimately, this allows to manage, operate and monitor the
plant in an operator-in-the-loop approach, thus contributing to
the creation of human-centric factories of the future. In the
paper, we presented a blueprint architecture for MDTs and
ODTs, where cyber-physical relationships among machines
and operators are mapped among DTs. We discussed the application of such an architecture to typical scenarios of industrial
automation. Additionally, we experimentally validated the
proposed approach in a collaborative robotics application,
showing how physical complexity can be reduced by resorting
to the proposed architecture.