Title: Securing Software Defined Networks: A Comprehensive Analysis of Approaches, Applications, and Future Strategies Against DoS Attacks

ABSTRACT Software Defined Networks (SDN) offer advantages over traditional networks, such as
programmability, flexibility, and scalability, making them ideal for implementing and managing new
networks while lowering associated expenses. In this article, we will examine and assess various approaches,
looking at the benefits and limitations of each solution based on factors such as efficiency, user satisfaction,
delay, and other relevant factors. In addition, we have conducted extensive analysis on SDN technology,
including the most recent research and applications in areas such as 5G, Wi-Fi networks, IoT-based
automated vehicle technology, satellite networks, smart grids, green and renewable energy, and AI. However,
we should remember that even with all these applications, these networks are still susceptible to Denial
of Service (DoS) and Distributed DoS (DDoS) attacks, which can cause serious disruption to network
operations. This article also provides a thorough overview of the threat landscape for SDN and DoS attacks,
highlighting the various attacks and their potential impact on network operations and sensitive data security.
To mitigate the risks associated with these attacks, it is crucial to have effective solutions in place. We must
constantly research and develop new strategies and approaches to counter DoS attacks in SDN as attackers
continually discover new vulnerabilities in these networks. Furthermore, we highlight various detection and
mitigation strategies for DoS attacks in SDN and emphasize the importance of constantly innovating and
developing new approaches to secure SDN. Moreover, we delve into the future of SDN security and provide
valuable insights for network administrators, security professionals, and researchers in devising effective
strategies to protect SDNs from DoS attacks.
INDEX TERMS SDN, OpenFlow, DoS, DDoS, detection, mitigation.
I. INTRODUCTION
SDN is a modern networking archetype that attempts to
overcome the limitations of traditional network architectures
by physically separating network control and forwarding. The
SDN offers us cross-product integration, open-source support, deep network service sharing, centralized app management, and multivendor interoperability as an open networking
ecosystem for rapidly developing networking technologies.
Scalability, elasticity, flexibility, fault tolerance, resource
management, virtualization, traffic management, efficiency,
consistency, abstraction, and security are the pillars of
SDN technology. It has the potential to reduce network
complexity, streamline network management, and enable the
much-anticipated upheavals in the future of networking [1],
[2], [3], [4], [5], [6], [7].
The future of the internet is driven by ever-increasing
demands for complex and sophisticated applications and
services [8]. SDN is viewed as a granular solution to the
security issues, manageability, robustness, and optimization
in dynamic computer networks for the end-user benefit.
It has logically centralized intelligence that provides an
open programming interface where applications can actively
regulate and manage the network elements. It is a promising
solution for internet security issues, and with its higher
flexibility and efficient configuration, it can accommodate
innovative network designs.
Although SDN has numerous advantages, it is still
in its infancy, and many issues are still unsolved. Its
centralized, automated management and control, global
view, and consistent policy enforcement help to minimize
configuration errors. Automated network maintenance is
facilitated by designing comprehensive network diagnosis
or prognosis mechanisms. However, concerns about its
reliability, standardization, and interoperability with legacy
networks have been raised. SDN’s decoupled architecture and
software-based management approach can increase network
processing latency, leading to faults and defects across
multiple layers, limited processing capability, spoofing and
tampering attacks, information disclosure, privilege elevations, or repudiation. This article systematically classifies
threats and attacks[9] on SDNs with a category-wise analysis
of their recently proposed solutions.
A. ORGANIZATION OF THE PAPER
The remainder of the paper is laid out as follows: Section II
briefly discusses the background of SDN, SDN architecture
and its working, and OpenFlow-SDN. Section III compares
existing surveys and the survey scope. Section IV briefly
discusses layer-wise security threats in SDN. Next, we have
an analysis of their detection and mitigation strategies in
Section V. Sections VI, VII, VIII, IX, and X provide a
review and analysis of various DoS/ DDoS attack solutions
for SDN, including architectural, ML-based, statistical, and
hybrid solutions. Sections XI and XII shed light on the
interaction of SDN with blockchain, IoT, IDS, and load
balancing. Some new and ongoing innovations with SDN
are explored in Section XIII. Lastly, Section XIV provides
a conclusion and future research directions. Figure 1 shows
the road map for the same. Figure 2 depicts the domains of
this article’s literature review.
B. CONTRIBUTIONS
In this paper, we introduce the fundamental concepts of
traditional networking, Software-Defined Networking (SDN)
architecture, and their operational mechanisms. We also
provide a thorough review of key surveys that have significantly advanced our understanding of SDN networks, such
as detection and mitigation strategies for DoS and DDoS
attacks.
Next, we explore potential security threats at each layer
of SDN–data plane, control plane, and application plane.
We also examine the impact of DoS/DDoS attacks on network
performance and review various strategies for detecting and
mitigating them in the SDN environment.
Additionally, we propose a taxonomy of solutions for
DoS/DDoS detection and mitigation, categorized as follows: architecture-based, table entry and scheduling-based,
statistics and entropy-based, machine learning-based, and
networking and hybrid-based approaches, with each category
mapped to corresponding sections in this paper. We then look
at how SDN security and efficiency can be improved by
integrating with emerging technologies like blockchain and
the Internet of Things (IoT).
Furthermore, we discuss the role of SDN in intrusion
detection systems, as well as load balancing strategies for
improving intrusion detection capabilities. Finally, we provide insights into ongoing innovations and future research
directions aimed at securing SDNs, which will help network
administrators and security professionals develop effective
strategies against evolving threats.
II. BACKGROUND
This section provides a concise overview of the traditional
networks, the architecture of SDN with layer description, and
Open Flow-SDN.
A. TRADITIONAL NETWORKS
A traditional hardware-centric network includes multiple
configurable network devices such as switches, routers,
and firewalls that facilitate packet transfer within and
outside the network. These autonomous systems can form
their forwarding tables, information bases, and network
topologies by exchanging neighbor information. This is
done using the configurations and network policies the
network administrator sets. Based on these information
dynamics and control logic, they operate distributed and
decide how and where to forward a packet. This, however,
hinders network device maintenance, software updates,
network protocol management, and innovations due to vendor
dependence. Such an architecture is unsuitable for complex
networks with numerous devices, leading to scalability issues
[10], [11].
Modern internet has networking devices with intent-driven
Application Specific Integrated Circuits (ASICs) as an
FIGURE 1. Organization of the article.
infrastructure supporting hardware-centric networking [12].
The devices only support limited commands and restricted
configurations based on their embedded OS or firmware.
ForCES is the interface between the control plane (CP) and
the data plane (DP). The network is controlled by protocols
like Rate Control Protocol (RCP), Path Computation Element
(PCE), SoftRouter, Intelligent Route Service Control Point
(IRSCP), and further OpenFlow Random Host Mutation
(OFRHM) techniques are proposed to hide network assets
from scanners longing for an attack.
The significant dissimilarity between the legacy networks
and the SDN is in handling the data packets [13]. In a
traditional network, the firmware tells the switch how to
handle an incoming packet. The OpenFlow switches have
FIGURE 2. Domain-wise solutions for SDN.
flow tables that store the flow rules rendered by the controller
to forward the packets. Without a matching flow rule for an
incoming packet, the SDN switch sends the packet header to
the controller as a Packet-In message. The controller receives
this message and uses a Packet-Out message to set the new
flow rule. These tables are limited, often creating a bottleneck
during DoS and DDoS attacks by exhausting all the network
resources and bandwidth.
B. SDN ARCHITECTURE AND ITS WORKING
SDN has a split architecture in which most of the network
control logic is placed in the control plane, and the data plane
merely performs the forwarding decisions initiated by the
control plane. There is the application plane (AP), the control
plane (CP), and the data planes (DP) connected by the internal
northbound and southbound interfaces. SDN also consists
of an admin plane that communicates to all the planes.
It has a physical or virtual network device implemented using
hardware + OS (NetFPGA or Pica8 3920) or software (Open
vSwitch) on the servers that perform network operations
like packet forwarding. Such an architecture has numerous
advantages over traditional network architecture. These
features of SDN are being further studied, standardized,
and implemented by standard organizations like the Internet
Research Task Force (IRTF), the Internet Engineering
Task Force (IETF), Open Networking Foundation (ONF),
and industrial consortia such as ONOS3. The comparison
between traditional network and SDN architectures can be
found in Figure 3. Figure 4 shows SDN architecture with all
its components.
FIGURE 3. Traditional hardware-centric network VS SDN network.
1) CONTROLLER
A controller is software for management functions, topology,
synchronization, and application interaction through northbound APIs for their control logic deployment. A C++
implementation of a Network Operating System (NOS)
evolves into a multithreaded SDN controller called NOSMT. POX is a popular OpenFlow-SDN controller that
supports Python and McNettle in Haskell. Project Floodlight, an open-source SDN community, is committed to
open-source standards and APIs. It controls Floodlight,
an enterprise-class, Java-based OpenFlow Controller with
Apache licensing. A group of programmers, including
several engineers from Big Switch Networks, support it–
OpenFlow-SDN controller for supporting Java language over
Linux platforms. Beacon, Ryu, OVS, OpenDayLight, and
FlowVisor are more commonly used SDN controllers that
generally deal with network controlling and monitoring
objects.
2) DATA PLANE
A DP is a collection of network devices at the bottom
layer of SDN, which forwards the packets as per the flow
instructions. The devices communicate to the controller using
southbound APIs while abstracting the devices as the flow
tables. The communication can be in-band, in which the
controller-device traffic follows the flow rules, or out-ofband, where the flow rules are not followed by the traffic,
depending on the OpenFlow rules.
3) CONTROL PLANE
A CP is a logically centralized assemblage of controllers
and a network OS for managing network devices in
the DP. The CP is regarded as the brain of the SDN
network and deals with its state and resource information
to help decision-making in the AP. It manages the traffic
flow, policies regarding data handling, network information, and abstracting the network logic with an ability
to add new functionality through interfaces. Its primary
design challenge lies in the efficient use of onboard
memory.
4) SOUTHBOUND INTERFACE
Southbound Interface (SBI) uses APIs to communicate
between the controller and forwarding devices for dynamic,
real-time demand fulfillment and functionality abstraction
to the CP. Examples of such APIs include List Processing (LISP), Multiprotocol Label Switching (MPLS), and
Network Configuration Protocol (NETCONF) by IETF.
OpenFlow protocol is the most common Southbound API.
It interfaces between CP and DP for configuration, performance querying, and notifications defined by southbound
protocols. Through the southbound interface, the CP installs
the control logic regarding flow labels into the DP, which
helps control traffic forwarding (OpenFlow and ForCES).
A hypervisor with a management module is placed at the SBI
to handle flow table control messages [14].
5) NORTHBOUND INTERFACE
Northbound APIs provide an interface between controller and
management planes so that device information can be used
for application development. Northbound Interfaces (NBIs),
primarily through REST APIs, are offered by controllers and
programming languages, and controllers provide high-level
APIs for application development. NBI specifies network
FIGURE 4. SDN architecture.
control logic and serves as a communication interface
between AP and CP to support SDN applications built with
REST, Onix, or Java APIs.
6) EAST AND WESTBOUND INTERFACES
In a physically distributed CP, Eastbound and Westbound
Interfaces (EBI and WBI) are used for controller interaction, coordination, and topology exchange. WBI interconnection between SDN and traditional network communications and its supporting protocols are RouteFlow,
SDN-IP, BTSDN, etc., EBI interconnection between different SDN domains or SDN to SDN communications
and its supporting protocols are SDNi, hyperFlow, ONIX,
etc.
7) APPLICATION PLANE
AP includes end-user applications for managing the network
by exploiting SDN services provided by the controller, like
load balancing, traffic engineering, network security, access
control, QoS, and virtualization.
8) DATA AGENT
A data agent (OpenFlow or ForCES forwarding elements)
for controller interaction is defined by SDN southbound
protocols.
9) APPLICATIONS
Applications that define network control logic are implemented in AP or CP as application modules or control
programs, like plugins in OpenDaylight. They can access
network resources using underlying protocols, making it
possible to inject desired policies into the network through
NBIs. They are responsible for network mobility and
measurement, traffic engineering, security, and data center
networking. Programming primitives like Frenetic, Pyretic,
and Nettle can be used to provide high-level abstraction in application development. Through the NBI, they
can use Application-Layer Traffic Optimization (ALTO)
or extensible Session Protocol (XSP) to get an instantaneous status and a global network view. SDN provides a Platform as a Service (PaaS) networking model.Application performance can be boosted by using adaptive
routing.
10) SWITCHES
Switches have flow tables that control the packets as per
the packet-handling rules. They have a software agent called
OpenFlow Agent (OFA). Depending upon the controller
policy, the OpenFlow switch acts as a router or firewall.
As a southbound protocol, OpenFlow has an OpenFlow
agent in the switches responsible for packet-in and barrier
messages and controller rule installation. Open vSwitch
supports SDN protocols and is used for network automation
through software extensions. It has security and monitoring
processes, QoS, and automated control. It can use a cache
replacement policy in the flow table cache to improve
the forwarding rule hit rates and efficiently utilize limited
memory. The OpenFlow-SDN switch architecture can be seen
in Figure 5.
FIGURE 5. OpenFlow-SDN switch.
11) SDN WORKING
For incoming traffic, the switch checks the packet header with
its flow table entries. The respective action is performed if a
match is detected, i.e., the packet gets forwarded to the next
hop. In case of new incoming flow requests whose matching
entries are not present in the flow table, the Packet-In
messages, consisting of its headers for new flow installation,
are sent to the controller while the packet sits in the switch’s
buffer. Its buffer may get filled up due to many incoming
requests, after which it forwards all buffered packets to the
controller, which checks for the match i. Then, accordingly,
the controller establishes a new flow path and creates a
corresponding table entry. This overhead can overwhelm the
controller, disrupting its processing capability and making it
unreachable. Controller Performance Benchmarking (CPB),
such as Controller Bench Marker (Cbench) or OFCBenchmark tools, can be used to increase the processing capability
and identify the performance bottlenecks of a controller.
ClosedFlow technique can incorporate SDN into an
existing traditional network or proprietary hardware [15].
It uses Open Shortest Path First algorithm (OSPF), Teletype
Network Protocol (Telnet), or Secure Socket Shell (SSH)
protocols over Virtual Local Area Network (VLAN) channels
and employs Access Control Lists (ACL) for packet matching
to provide OpenFlow like features. A hybrid network
consisting of traditional and Open Flow-enabled devices can
also be used. Several virtual SDNs (vSDNs) over a physical
network can share the network resources such as nodes
or links. The entire physical network can be abstracted as
a single virtual node in higher-level virtualization. Crosslayer strategies developed in SDN as an application can
easily access information on network status, thus achieving
QoS. The SDN and switching devices’ reconfigurability
can be exploited with a cross-layer technique for runtime
configuration of the network based on significant data
application dynamics. Hadoop helps achieve job scheduling
with lower configuration overhead to accommodate the
dynamic network configuration in a hybrid network.
A new approach to reducing energy consumption in SDN
networks can be a heuristic algorithm that considers network
traffic and node status information to switch off underutilized
network devices and minimize energy consumption dynamically [16]. The algorithm is evaluated through simulations,
and the outcomes show that it effectively reduces energy
consumption compared to existing methods. The algorithm
can become a practical tool to reduce energy costs and
increase the sustainability of SDN networks.
Some of the most common issues are packet forwarding
issues such as reachability failure, loop and black hole
formation, waypoint routing, host isolation, and enlarged path
lengths[17]. There can also be issues leading to packet header
modification, encapsulation and decapsulation errors, and
packet replication under transformation issues. Then, there
are also dynamic issues like unpredictable packet loss, link
latency and congestion, intermittent connectivity, and load
imbalance. There is always a concern about unauthorized
access to controllers or network resources, data leaks, and
fake rules installed by malicious applications [18]. Network
configuration may be more straightforward, but solving
cross-layer configuration issues can become very complex in
SDNs.
C. OPENFLOW-SDN
SDN is the traditional hardware-centric network architecture
that is detached into a data plane (DP) with programmability,
a logically centralized control plane (CP), and an application
plane (AP) rather than integrating them all as a single
entity. The controlling unit handles the control functions,
and switches perform data forwarding. Thus, managing
and maintaining the network and enhancing the control
process becomes easy. It provides simple, programmable
network devices rather than the complex ones found in active
networking, allowing network control independent of data
flows. The software can externally control the switching
devices without onboard intelligence. This provides more
freedom to define the network behavior.
OpenFlow (OF) is a standard southbound protocol with
which the controller and switches communicate with each
other through the control channel [19], [20]. It standardizes
how an SDN controller communicates with network devices
by providing a specification for migrating control logic
from the switch to the controller. Thus, switches can be
controlled without exposing their codes. There is an exchange
of control messages, like Packet-In, Packet-Out, and FlowAdd, that TLS encrypts over a TCP connection between
them. They are transmitted over an in-band or an out-ofband channel, depending upon the availability of dedicated
interfaces. Packet forwarding and link tuning are at switching
and data link levels that break the layering barrier. The
control plane can help define isolated virtual networks and
offers a convenient platform for experimenting with new
techniques. SDN allows the control plane to configure the
network devices through software control.
OpenFlow is a practical enabler of SDN that focuses
on creating a separate software-controllable network that
controls packet forwarding. It is the original and most widely
adopted SDN technology. The protocol enables convenient
flow table manipulation services like inserting, deleting,
modifying, and looking up through a secure TCP channel.
In an OpenFlow switch, flow entries have a header to match
the received packets, an action field to define the action for
the packet, and a statistics field to store information about the
matched traffic flow. OpenFlow is continually evolving and
has opened up an opportunity to have a network with
logically centralized control and programmability, which is
the key concept behind SDN. As SDN gains more stability,
functionality, and security, it influences future advancements
in OpenFlow [21]. Recent advancements in the area of SDN
focus on the advancements from OpenFlow to P4 [22], [23].
P4 is a more advanced and flexible SDN technology that
overcomes OpenFlow limitations, such as scalability and
programmability, by providing a high-level programming
language for specifying network behavior. The article [22]
also provides a comprehensive overview of P4 architecture,
features, and programming models. P4 and OpenFlow are
compared in terms of performance, programmability, and
ease of use, and we discuss the challenges and opportunities
of P4 in the context of SDN and the future of networking.
P4 has the potential to revolutionize networking by providing
a more flexible and scalable way to program network
devices. Similarly, the Forwarding and Control Element
Separation (ForCES), an Internet Engineering Task Force
(IETF) standard, attempts to separate the CP-DP architecture
but is not as suitable as OpenFlow. Its network element (NE)
has multiple forwarding elements (FE) and control elements
(CE), and they follow protocols defined by the ForCES
protocol layer. It still has the functionalities of a conventional
network and is not progressive. It has a flexible forwarding
model but a disruptive business model, which isn’t widely
adopted and fails to satisfy the current networking demands.
After OpenFlow standardization, vendors like IBM,
Juniper, Cisco, HP, Huawei, and Arista, among others,
released their OpenFlow switches using open network
hardware, such as NetFPGA. Similarly, multiple OpenFlow
controllers flooded the markets, making network deployment possible. SDN is an information-centric network that
originates from the OpenFlow project. It is under constant
development and enjoys significant attention from several
researchers while actively exploring academia, industries,
enterprises, governments, and data centers. An SDN-based
network can quickly evolve to satisfy the network users’
rapidly changing demands for network resources and configurations, with great scope in emerging technologies like 5G,
Cloud Computing, IoT, and NFV scenarios. IT companies
have successfully implemented SDN in projects such as
Microsoft Ananta, Google B4, and the NTT Cloud Gateway.
The first SDN controller was NOS, which was introduced
with OpenFlow in 2008. After that, SDN controllers like
POX, ONIX, Beacon, Floodlight, ODL, and ONOS were
developed. Some controllers are no longer under active
maintenance, primarily due to difficulty scaling. Only a
few of these controllers are presently under functional
development.
III. RELATED SURVEY
This section establishes the context for the current study,
highlighting the gaps, advancements, and key findings in
the realm of the fundamentals of the SDN environment
and attacks such as DoS and DDoS attacks associated with
the SDN environment. Additionally, we aim to present a
thorough review of relevant surveys, papers, and studies that
have contributed to the understanding of SDN networks and
DoS and DDoS attack detection and mitigation policies, and
the same is provided in Tables 1 and 2. The Comparative
Analysis of SDN Surveys is given in Table 3.
In [24], authors dedicated to enhancing non-functional
aspects of SDN, including reliability, scalability, performance, load balancing, and hybrid solutions. They were
assessed according to key metrics like performance optimization, security, platform provisioning, mitigating attacks,
detecting attacks, and load balancing.
In [25], Dedicated to SDN security, the review addresses
vulnerabilities and defense mechanisms against DDoS
attacks within SDN architecture. It also focuses on NFV and
ML mechanisms, along with relevant datasets, engaging in a
detailed discussion on challenges within these areas.
The review explores ML sensors, secondary servers, and
redirection rules in [26], dedicated to Moving Target Defense
(MTD) Mechanisms. It also focuses on DDoS detection and
mitigating techniques within the MTD approach.
In [27], prioritized the examination of DoS and DDoS
attacks, excluding an analysis of alternative attacks.
Furthermore, the paper delves into solutions for table
entry management, scheduling, architecture, statistics,
entropy, machine learning, and hybrid models. Additionally,
it explored the application of SDN in domains such as load
balancing, IoT, and blockchain. Classification is based on the
type & target of attack tools used and does not present the
detailed nature and types of attacks in SDN.
In [28], the focus of the study was on DoS and DDoS
attacks, excluding consideration of other attack types. The
paper presented and discussed solutions for table entry
management, scheduling, architecture, statistics, entropy,
machine learning, and hybrid models. Intrinsic and extrinsic
approaches, classification for SDN, DoS/DDoS detection,
prevention, mitigation, and graceful degradation.
In [29], it concentrated solely on DDoS attacks and other
attack types but did not address DoS attacks. It provided and
discussed solutions for statistics, entropy, machine learning,
and hybrid models.
In [17], concentrated on all attacks, encompassing both
DoS and DDoS attacks. It partially discussed solutions for
these attacks. Provides security challenges and solutions
specific to CP, DP, and AP, as well as cross-layer security.
This paper covered topics such as DoS and DDoS attacks
in SDN, encompassing detection, mitigation, attack overview,
classification, and SDN fault management. Additionally,
our exploration includes solutions based on architecture,
table entry, scheduling, statistics, and entropy. We discuss
machine learning (ML)-based solutions, network-based and
hybrid applications, and SDN integration with blockchain
and IoT applications. Furthermore, the paper discusses load
balancing, intrusion detection systems, and current research
challenges.
A. SCOPE OF SURVEY
• Control data flow path and ensure data sovereignty.
• Facilitate Network-as-a-Service (NaaS) and Infrastructure-as-a Service (IaaS).
• Provide virtualization technology (NFV).
• Increase efficiency of energy-aware data centers.
• Implement fail-over mechanism and load balancing in
Smart grid networks.
• Ensure secure and efficient communication in home
networks (HAN) and wireless video streaming
• Provide centralized network control, configuration,
enforcement of policies, and abstracted programming
for extensive IoT and Wireless Sensor Networks
• Enable boundless mobility and seamless wireless connection handover in User-centric networks [30].
• Provide Quality of Service (QoS) in IoT applications.
• Develop steering frameworks for multi-path big data
transfer applications
• Real-time, portable, secure communication between
SDN-enabled vehicles and Vehicle To Everything (V2X)
communications [31], [32], [33].
• Facilitate Software Defined Satellite Networks (SDSN)
in varying network conditions
• Detect ARP spoofing attack in fat-tree topology networks.
• Develop steering frameworks (MPTCP) for multi-path
big data transfer applications.
IV. LAYER WISE SECURITY THREATS IN SDN
The security threats at different SDN layers is shown in
Figure 6. SDN also suffers from packet injection and attacks
such as Know Your Enemy (KYE), in which multiple packets
with forged header fields are injected, and the switch is forced
to send Packet-In messages over to the controller [27]. It gets
overloaded with such messages, consuming its resources
and bandwidth. In a KYE attack, the attacker gathers SDN
configuration and security information. Then, in the probing
phase, it triggers the new flow rule installations on the
entry switch; then, in the interference phase, it analyses the
correlation between this crafted traffic and the installed flow
rules. This helps the attacker gather information about the
DoS detection methods employed in the network and plan and
execute the attack accordingly.
FIGURE 6. Layer-wise security threats in SDN.
SDNs also suffer from DoS and DDoS attacks, which can
flood all the CP, DP, or communication channels, i.e., all its
layers can be the attack target. It is the most severe attack
on SDN networks that can disabling the whole network [19].
The impacts vary according to the target of the attack,
ranging from packet drop due to overflowing flow tables in
the case of DP or communication channel to the failure of
the entire network in the case of CP. Software bugs in CP,
custom switch optimization, or in-policy conflicts can induce
complex and difficult-to-diagnose faults in the network, such
as CP-DP state inconsistency, forwarding loops, or black
holes. [34] These attacks lead to bandwidth consumption,
resource exhaustion, disabling of services, and performance
degradation, thereby intentionally preventing legitimate hosts
from communicating with the controller or accessing the
required services. It is launched by filling the switch flow
tables or flooding the network with attack packets that drain
TABLE 1. Summary of related surveys.
TABLE 2. Comparison of related surveys.
the CP bandwidth [27]. It can be targeted to the data layer,
control layer, or application layer in SDN. The attacks can
be aimed at bandwidth or resource saturation or exploit
switch vulnerabilities at a low, high, or stealthy rate to
cause a local or a global impact [36]. Multiple table miss
messages from the attackers exceed the processing capacity
of the controller, causing a DoS attack. The CP suffers a
DDoS attack called the Amplified Control Plane Saturation
Attack (CPSA). It quickly generates new flow rules, forcing
a switch to route the packet through other switches.
Thus, each switch can request a new flow rule from the
controller. Figure 7 shows the DoS attack targeting the SDN
switch.
A. SDN SPECIFIC DOS ATTACKS
DoS/ DDoS is a highly destructive and initiative attack
in which an attacker intrudes on vulnerable nodes in the
network, converts them into botnets, and uses them to create
fake packet traffic, often with falsified IP addresses, to launch
an attack on the server [37]. It is a simple yet powerful attack
TABLE 3. Comparative analysis of SDN surveys.
FIGURE 7. DoS attack in SDN.
that ceases the network’s availability from a single source in
the case of DoS or multiple sources in the case of DDoS.
An attack explicitly attempts to prevent a service’s legitimate
usage. The impacts may range from a minor inconvenience
or lagging for a website user to heavy financial losses
to companies by temporarily bringing down their online
presence [38]. The main targets are high-profile bank servers,
payment gateways, search engines, and government web
servers. Such attacks are increasing, and many IT giants like
Apple, Amazon, etc., have all suffered from them, leading
to massive economic loss for the companies and a threat to
society. A DDoS attack [39] does not occur suddenly but
emerges from a series of these steps:
• Discovery of the agent vulnerabilities by the intruder,
usually by sending emails containing attack code
• Intruder starts to compromise geographically separated
agent machines through their vulnerabilities using
malicious programs like Trojan Horse.
• The malicious file is replicated in multiple (thousands
or millions) agents that now come under the intruder’s
control.
• The attacker or a bot-primary can remotely order the
botnet (group of bots) can initiate a large-scale DDoS
attack without getting noticed
• A large amount of useless traffic is generated, which
overwhelms the victim resources in a short interval, thus
slowing down the system services and network’s ability
to respond to legitimate users.
The DP suffers from two varieties of DoS attacks: DoS
attacks with single flow entry (S-DoS) and DoS attacks
with multiple flow entries (M-DoS) [40]. S-DoS overwhelms
the target link while M-DoS exhausts the switch’s Ternary
Content Addressable Memory (TCAM), triggering multiple
new flow entries. Crosspath is an example of an S-DoS
attack in which a single, well-defined entry blocks the shared
link. In M-DoS, a target switch must install multiple fake
flow rules in its limited TCAM. The OpenFlow switches are
highly vulnerable to DDoS attacks because of their reactive
caching mechanism, in which large packets with different
flows are flooded to them. They must be buffered, and
queries must be sent to the controller. They have limited
memory for storing flow rules, which may get filled due to
an attack, after which they can no longer accommodate new
flow requests. The attackers load it with rules for malicious
requests, thus leading to packet drops because of the lack
of space for new regulations. In such cases, the buffered
packets cannot be forwarded to the controller because of a
DoS attack targeted over the DP. Multiple new flows may also
be generated for which there are no flow table entries. Such
packets get forwarded to the controller after the switch buffer
is full, leading to delays and bandwidth consumption due to
a successful attack. The attacker enters the network through
the weakest link or a device and, using that, propagates
the attack to the entire network. All the switches routed
to the controller get infected and carry the malicious flows
to the controller, bringing down the network. Figure 8 shows
the attack propagation starting at a device.
The DP also suffers from functional defects or hardware
faults due to network misconfiguration and inconsistent
rule installations [27]. Similarly, information mistranslation
or policy violations can cause faults in the CP, and
incorrect implementations can affect the AP. Significant
challenges include heterogeneity, language specifications,
and vendor-specific network elements. Other types of attacks
are:
• Buffer saturation attack: The attacker generates multiple
fake packets with forged IP addresses so that the buffer
runs out of memory and legitimate packets get no buffer
space
• Flow table overflow: Flow tables are stored in Ternary
Content Addressable Memory (TCAM), and each entity
has an idle timeout: a measure of time when the flow
entry is removed from the table when there is no
matching and a hard timeout: the amount of time the
flow stays in the table before removal. The attacker sends
a large volume of unmatched flow to exploit this, and all
flow entities get replaced by fake entries, and memory
overflows with useless rules. Switch fails to service the
legitimate users and drops all received flow.
• Link flooding attack: when the buffer is full, entire packets are sent to the controller, consuming the bandwidth,
and a bottleneck gets created for the legitimate traffic
FIGURE 8. Malicious traffic propagation in SDN.
• Controller saturation: the controller is also an application installed on a VM with RAM, processing power,
and some resources. Its resources can become saturated,
overwhelmed, and degraded due to extensive processing
as multiple new flows are flooded from the botnets
• Low rate reflection-based attacks through low rate flow
of Packet-In flood or Spoofed packet injection along
with TCP SYN, UDP, ICMP floods.
B. DDOS ATTACK CLASSIFICATION
DDoS attacks can cause resource or bandwidth depletion
and further exploit the packets or protocols, leading to many
problems in the network [41]. Figure 9 shows a possible
classification of DDoS attacks. It can be a TCP, UDP SYN,
FIGURE 9. DDoS attack classification.
HTTP, or ICMP flood targeting host, OS, or application [27].
The attack can be volumetric or non-volumetric, and a SYN
flood is a type of volumetric DDoS attack. Some widespread
DoS attacks are Smurf attacks, raffle attacks, amplification
of SNMP, or Cormelt attacks. In a TCP SYN flood attack,
the attacker sends numerous SYN requests. The server keeps
replying to them while waiting for an ACK, which never
comes; thus, the entire buffer queue of the server is consumed.
This results in new legitimate SYN requests being dropped.
In an ICMP flood or a Smurf attack, a spoofed source IP
overloads the server with ICMP echo requests, exhausting
target resources during the reply. A Fraggle attack is when
UDP packets are flooded in the same way, while in a
Cormelt attack, multiple spoofed bots communicate with
each other, generating massive network traffic [35], [38].
The attacks can be bug or infrastructure level [42], [43].
E.g. a ping-of-death attack. In this case, the ping packet
size exceeds the allowed IPv4 packet size. Infrastructurelevel DDoS attacks can be caused only by knowing the
victim’s IP address. In direct attacks, the victim is flooded
with bogus packets through zombie machines at network
(TCP, UDP, ICMP, SYN) or application (HTTP, HTTPS,
FTP) layers. In reflector attacks, zombie machines send
messages to the reflector machine, spoofing the victim’s IP
address. BlackNurse-SC is a type of DDoS attack that is
hard to detect and targeted at the SDN controller [44]. The
attacker damages the network topology view, thus leading
to the controller malfunctioning. It is an evolution of the
BlackNurse attack that targets firewalls in legacy networks.
Bots are employed within the controller’s reach, generating
ICMP error messages, because of which the controller gets
overwhelmed and incorrectly updates its topology view [45].
Like wormhole attacks in WSN, an attacker can exploit
Link Layer Discovery Protocol (LLDP) vulnerabilities’
vulnerabilities by fabricating the packets to declare false links
between distant switches, leading to DoS, eavesdropping, and
hijacking attacks. In SDNs, it can cause a DoS attack on data
or control plane saturation in legacy networks.
V. DOS/DDOS ATTACKS DETECTION AND MITIGATION
Detection is necessary to determine where and how the
attack can be detected, what and where is the response
mechanism used, and where is the control center to be
able to address how a defense method should be designed
and deployed. There are survival, proactive, or reactive
techniques to deal with the attacks. The mitigation strategies
are classified based on methodologies for dealing with
malicious traffic, such as blocking, delaying, or resource
management. DDoS attacks are hard to detect because
we can’t use signature-based techniques for detection over
encrypted data, and the Statistics based methods can be
easily bypassed through forged traffic patterns [37], [46].
Some approaches can’t determine the attack trace and affect
the service to legitimate users. Others can’t distinguish
between attack and legitimate traffic or employ additional
overhead in delays, resource consumption, cost, efficiency,
or architectural constraints.
The programmable data planes in SDNs make DDoS
attacks increasingly fatal [16], [47], [48]. A detection
mechanism involving Spatial-Temporal Graph Convolutional
Network (ST-GCN) for DP-programmable SDNs with Inband Network Telemetry is used in the network mapped
as a graph. It employs whitelisting or packet-dropping
strategies for DDoS mitigation. It helps to obtain fine-grained
temporal and static network features and topology to
detect attack traces and use defense strategies. As a result,
an attacker cannot easily bypass these detection mechanisms
by forging traffic patterns. The effectiveness of the mitigation
mechanism is assessed using a ratio of regular packets to
total packets received after starting the mitigation module.
The defense cost is distributed as the defense strategy
is distributed cooperatively and works simultaneously on
multiple switches. As a result, it provides high-performance
detection and accurate mitigation. Configuration verification,
formal probe testing, network debugging, and data agent
testing are all methods used to detect faults in DP. Similarly,
we have conflict and translation verification, software-based
debugging, testing, and evaluation in the CP. In AP, we have
white box verification and black box testing [12], [49].
Securing the communication channels [28] between DP and
CP using (Internet Protocol Security) IPSec, (Advanced
Encryption Technique) AES, and (Transport Layer Security)
TLS can also address the problem but comes with an overhead
cost.
The application layer can perform Deep Packet Inspection
(DPI) on incoming traffic, redirecting it to the server for
priority scheduling and limiting DP-CP communication [49],
[50]. This approach is highly efficient and involves a little
delay due to DPI. Similarly, the virtual machine approach,
as proposed in [51] and [52], would help combat the attack
by efficient resource allocation during attack times but incurs
high maintenance and does not address the root cause of
the problem. An attacker can send malicious traffic to its
connected switch through an infected device, propagating to
the controller and bringing down the entire network. The
network snapshot prepared using the control messages is not
reliable. Hence, specialized probe packets can be injected into
the DP for the resulting analysis. The traffic statistics are
collected using Netflow, sFlow, and SNMP and stored locally
in switches to be studied by the controllers to determine
the location of a faulty device, estimate the traffic matrix,
detect network anomalies, and verify the configuration.
Reference [12] says that we can monitor the end hosts
and install specific port or flow mirroring rules in the
switches to divert the matching packets to analysis agents
[53], [54], [55].
State rollback is commonly used in distributed systems for
fault recovery and repair. The rollback process is much like
the record-and-replay mechanism used in fault diagnosis but
with recovery purposes. It mitigates the impact of difficultto-diagnose and repair faults. Fault tolerance can be generally
achieved through hardware, software, or information redundancy, but it comes with an overhead. Under fault tolerance
for data and control traffic, conflict resolution, operation
isolation, policy composition, and module coordination
mechanisms have been proposed. Some source-based (SB)
and destination-based (DB) techniques are used to prevent the
onset of a DDoS attack and attack the target, respectively. The
controller located in the network affects the effectiveness of
DDoS attack detection. The existing methods are
• Using self-organizing mapping networks to get early
alerts about the occurrence of packets in a malicious
event for TCP/UDP traffic
• Identification of the path that suffered an attack, overcoming the limitation of fixed detection loop approach
for rapid DDoS detection
• Flow statistics process for collection and analysis of data
in switches tables
• Entropy-based detection on the controller for flash
crowd events
• Using multiple packet header features in the joint
entropy method instead of depending on a single packet
feature.
• Using information theory for detection of both spoofed
and non-spoofed DDoS attacks
• Statistical data and algorithm selection for low-rate
DDoS detection
An overview of the defense mechanisms against DDoS
attacks in SDN environments has been provided in [56]
and [57]. Well-known existing solutions, along with various
challenges and opportunities in the field, and a detailed
analysis of the various defense mechanisms that can be used
to mitigate DDoS attacks in SDN environments, including
filtering, rate limiting, and traffic management techniques,
are discussed. Each defense mechanism’s key advantages
and disadvantages are provided, along with insights into
potential future directions. It provides a valuable resource for
researchers and practitioners interested in security in SDN
environments. There is a balanced view of each defense
mechanism’s advantages and disadvantages, helping readers
understand the trade-offs and make informed decisions about
which mechanisms are best suited for their needs. This
article summarizes the main findings and highlights the key
challenges and opportunities for SDN in the context of DDoS
attacks.
Several DoS and DDoS mitigation techniques in SDNs
such as table-entry or scheduling-based, Machine Learning,
Flow statistics, Entropy-based, Architectural, and Hybrid are
discussed in [26], [27], and [58]. It performs a Comparison
of various solutions, an Overview of DoS/DDoS mitigation
solutions in SDNs, and an Overview of testing tools such as
OPNET, and NetFPGA. The testbeds used were Objective
Modular Network Testbed in C++ (OMNet++), Future
Internet Testbed for Security (FITS), and Spirent contracting
tools. They evaluated DoS/DDoS mitigation techniques using
a variety of datasets and framework emulations. There is also
an overview of the most recent advances in the field and a
discussion of the advantages and disadvantages of various
mitigation strategies. The summary of all the detection and
mitigation approaches we discussed can be found in Table 4.
A. POPULAR DETECTION TECHNIQUES
The popular DoS/DDoS detection techniques are given in this
section.
1) FLOODDEFENDER
In [24], [25], [59], and [71], present a scalable and protocolindependent mitigation approach, FloodDefender framework
for SDN. It is employed between the CP and AP, utilizing
the frequency features for DoS attack identification. There
are alert, active, and blocked states, trying to handle
packet bouncing, import loss, and detoured traffic problems.
Flood Defender uses table-miss engineering, packet filtering,
and flow rule management to conserve communication
bandwidth, identify potential attack traffic while saving
CP’s computational resources, and discard useless flow table
entries respectively. It achieves just an 18ms delay, 96%
accuracy, and 5% packet loss rate during attacks. Better
than previous approaches, it is easy to deploy and is highly
efficient at identifying attack traffic. It demonstrates precise
identification and efficient mitigation of DoS attacks targeted
over SDN with negligible overhead than other similar
approaches such as AvantGuard, FloodGuard, FlowKeeper,
TopoGuard, and SDNShield.
2) ORCHSEC
A DDoS detection as well as a mitigation strategy, OrchSec,
uses attack correlations and monitoring sensors dispersed
across a network [27]. It is orchestrator-based and has control
functions, data and control layers, an orchestrator agent,
and network monitoring for developing security applications.
SDN controller has this agent in the form of an application
connecting the orchestrator and controller.
3) HGB-FPA ALGORITHM
A method for detection and mitigation of Low-Rate DoS
(DDoS) attacks in SDN using a hybrid Gaussian-binomial
(HGB) algorithm combined with a false positive rate (FPA)
mechanism to detect LDoS attacks in real-time accurately
is used by [72]. The HGB-FPA algorithm utilizes traffic
characteristics and flow statistics to detect LDoS attacks, and
the FPA mechanism is used to reduce false positive alarms.
The working of the HGB-FPA algorithm is assessed through
simulations and experiments and compared with existing
methods. The outcome shows that the HGB-FPA algorithm
can accurately detect LDoS attacks and can effectively
mitigate their impact. The HGB-FPA algorithm is a valuable
contribution to the field of security in SDN and can be used
to enhance the robustness of SDN against DDoS attacks.
4) SELECTIVE PACKET INSPECTION
A selective packet inspection method for detecting DoS
flooding attacks in SDN environments reduces the amount of
traffic required for attack detection, improving the efficiency
and accuracy of the detection process [73]. Simulated
evaluations show that it can effectively detect DoS flooding
attacks while minimizing the overhead of the detection
process. This article provides a valuable contribution to SDN
security, demonstrating how selective packet inspection can
detect DoS flooding attacks in SDN environments.
TABLE 4. Attack detection and mitigation strategies in SDN.
5) SDN-BASED CONGESTION CONTROL
The traditional DDoS defense methods, such as firewalls
and IDS, are no longer sufficient in SDN environments [74].
The system takes advantage of SDN’s centralized control
and visibility to enhance network security by using its
ability to control network flow tables to filter out malicious
traffic dynamically. Additionally, the system uses congestion
control algorithms to manage network resources and limit
the amount of attack traffic. Finally, the system employs
rate limiting to control the rate at which traffic is processed,
effectively reducing the impact of DDoS attacks on the
network, resulting in a promising solution for SDN networks
facing DDoS attacks.
6) CHANGE POINT THEORY
Using the Change Point (CP) theory for DoS detection in
SD assumes that a change in monitored network metrics can
alert an anomaly [75]. The detection can be centralized or
distributed, and distributed detection, in which every node
detects a change in its local metrics, is unexplored in SDNs.
The centralized detector runs on the controller and can
identify high-rate attacks. They experimented with various
scenarios and reached a resulting trade-off between detection
rate and resources required for DoS attack detection.
B. ATTACK MITIGATION TECHNIQUES
A DoS attack solution can be intrinsic, which handles the
SDN functional elements, or extrinsic, which deals with the
network flow characteristics[28]. An intrinsic solution can be
table-entry-based, architecture-based, or scheduling-based,
while an extrinsic solution is usually statistics- or machinelearning-based. The attack mitigation by using Mininet can
be seen in Figure 10. The commonly used tools that aid in
attack simulation, detection, and mitigation are:
FIGURE 10. Attack mitigation by using mininet.
Scapy is a packet manipulation program to sniff, dissect,
probe, trace, and forge network packets. It helps researchers
to build their packets and emulate a DDoS attack. Similarly,
the Distributed Internet Traffic Generator (DITG) assists in
creating IPv4 and IPv6 traffic.
The TCP replay tool is used to replay previously captured
network traffic by resending the captured packets at the rate
of capture. It helps test firewalls, NetFlow, network intrusion
and risks, etc. and provides resulting Flow statistics.
BoNesi helps in the simulation of Botnet DDoS attacks by
generating TCP SYN, UDP, and ICMP floods.
Other commonly used tools are Tcpdump, Nping, Httperf,
Hping3, BigFlows Trace, sFlow-RT, sFlowTrend, and Static
Flow Pusher API.
1) SDNTRUTH SYSTEM
Mitigation using statistical analysis and traffic entropy
(SDNTruth system) Entropy variation is calculated based
on source IP, destination IP, source port, and destination
port, and then the Z test is used for the flow behavior
assessment. This system is implemented as a centralized SDN
architecture, making use of network global information from
the centralized controller. It is easier to obtain information
from, as compared to SNMP or sFlow protocols [76] The
controller calculates flow entropy using packet-in messages
and detects attacks using the proposed mechanism. Then, all
switches are sent a flow table update message to block the
detected attack. Global analysis is possible irrespective of
the instantaneous bot position, so it is useful in both cases
whether the attack is performed from inside or outside the
network.
There are separate capture, decision, and enforcement
components discussed in this approach:
• Capture: analyzing flows and storing flow parameters in
the database
• Decision: tests are performed to detect attack evidence
• Enforcement: checks destination IPs with numerous
flows and stops their forwarding
• Test environment: Mininet using PCAP files for TCP
Increased false negatives are seen in the case of 4 parameters as flows become more diverse with more parameters,
affecting entropy. The accuracy of this approach can be
verified over naive Bayesian, logistic regression, or decision
tree evaluations. It records fewer false positives.
Limitations: architectural scalability, less reliable in
real-world scenarios if multiple users suffer different attacks
from different sources simultaneously. Extensive testing and
validation of the proposals can help.
2) SD-ANTI-DDOS
SD-Anti-DoS has four modules: attack trigger, detection,
traceback, and the mitigation [19]. A Back Propagation
Neural Network (BPNN) is used for detection, following
which traceback is performed to find the attack source and
block it by revising the flow rules.
3) MITIGATION OF TOPOLOGY POISONING ATTACK
[77] addresses the issue of topology poisoning attacks in
hybrid SDNs. It is an attack that manipulates the topology
information in the network, leading to incorrect routing
decisions and communication disruptions. A comprehensive
analysis of topology poisoning attacks in hybrid SDNs
is presented, and several mitigation techniques to prevent
these attacks are highlighted. They categorize the mitigation
techniques based on their approach, including the use of
secure routing protocols, secure topology discovery, and
secure network configuration. The effectiveness of these proposed mitigation techniques is measured through simulation
experiments, and they show they can effectively prevent
topology poisoning attacks in hybrid SDNs. They also discuss
the limitations and challenges of their proposed techniques,
including the need for secure key management and effective
methods for detecting and responding to topology poisoning
attacks. Figure 2 depicts the various DoS/DDoS solutions
discussed in this article, arranged by timeline.
VI. ARCHITECTURE BASED SOLUTIONS
Architecture-based solutions [28] deal with monitoring and
controlling the properties and architecture, such as packet
migrator and FloodGuard proactive flow analyzer to install
flow rules into the switches during the attack and forward
table-miss information in DP cache [78]. It cannot detect the
attack but provides network stability and attack resistance
once it is somehow identified. Adding security privileges
and policy characteristics to SDN architecture [79] can
enhance access control management. Shirali-Shahreza and
Ganjali [80] use random sampling of incoming packets to
identify malicious traffic. Once detected, an attack source can
be traced back and blocked, improving the mitigation process.
Multiple distributed controllers or backup controllers [81],
[82] along with load balancers can be used, keeping at
least one controller operational at a time, which causes
better reliability and attack protection but with management
overheads. Avant guard states Host IP verification and other
proof-of-work techniques, such as puzzles, can be set by the
controller, which will also affect legitimate users. Adding a
Fresco framework layer between switches and the controller
can help.
A. MOVING TARGET DEFENSE
Researchers have proposed Moving Target Defense (MTD)
[83], [84] in a multi-controller pool or hierarchical role-based
controller architectures to reduce flow processing capacity
while boosting the controller’s capacity. There is an online
primary controller and several offline controllers, and configuration instructions are sent to the switches upon detection
of a passive DDoS attack. MTD methodology, also known
as mutation of an OpenFlow random host, changes the host
IP addresses at random and aids in the defense against DoS
attacks. These mutations take place frequently without host
knowledge, thereby going untracked by the attackers. The
IP spoofing problem can also be solved using IP address
binding, and attacks can be identified through the C-SVM
algorithm. This enables SDN to handle single-point failures
through network information and use rules to block attacks.
B. SOLVING ONE-PACKET DDOS ATTACK
An SDN-based architecture for mitigating one-packet DDoS
attacks uses numerous single packets transmitted into the
target network [65]. The architecture uses SDN to Detect
one-packet DDoS attacks in real-time, control network traffic
flow to block the attack packets, and provide network-wide
protection against one-packet DDoS attacks. It can effectively detect and mitigate one-packet DDoS attacks while
maintaining the normal traffic flow. This can provide a
valuable contribution to SDN security, demonstrating how
SDN can help protect networks against one-packet DDoS
attacks.
C. SDN GUARD
SDN-Guard is a two-tier architecture that protects both
infrastructure- and application-level DoS attacks [60]. The
first tier is a rate-limiting mechanism that restricts the amount
of traffic that can be sent to the controller, and the second tier
is a traffic filtering mechanism that inspects and filters the
incoming traffic flow to detect and block malicious traffic.
The evaluation of the effectiveness of SDN-Guard is carried
out through simulations, showing that it can significantly
reduce the consequences of DoS attacks on the SDN network
and prove that it outperforms existing solutions in terms of
both effectiveness and efficiency.
D. HYPERVISOR ARCHITECTURE
A distributed hypervisor architecture has been proposed for
scalability in SDN to handle flow table messages from
multiple tenants. Each tenant is given an illusion of its
topology with the controller using database technology.
It suggests keeping the entire traffic temporarily in the DP,
and selectively directing the packets through switches to
avoid the controller bottleneck, thereby scaling up SDN.
There is dynamic load shifting across the controllers or traffic
management. Third-party development in the OpenFlow
applications raises security concerns in SDN. Some talk
about role-based authorization and enforcement of a security
constraint in the NOS OpenFlow controller. The load on the
controller could be reduced by implementing a monitoring
function in the switches.
E. COMPONENT REDUNDANCY
Component redundancy is a practical solution for a single
point of failure caused by multiple controllers without
clustering or backup. This enhances the CP performance, but
may cause problems such as route flapping and convergence
delays. This takes us to the controller placement problem, i.e.,
deciding the optimal location of the controller(s) in a network
while ensuring traffic control, network services, and resilient
performance.
In the same context, [27] talks about using a backup
controller pool to be used when any of the working
controllers undergo an attack. A backup controller backs each
primary controller, and they communicate using heartbeat or
synchronization messages, mapping algorithms, or takeover
process, and protective mode. The proposed approach is
efficient in handling the attacks, but at a cost of architectural
overhead and is not very practical as the backup controllers
are also equally susceptible to the attack.
F. SWITCH MODIFICATION
Switch modification involves empowering the switches [28]
to be able to detect botnets performing the DoS attacks
through their spoofed IP addresses. There is often a mismatch
seen in the source address of the attack packet, through which
it can be detected. This is a lightweight solution to protect the
controller before the attack and prevent it from propagating
in the entire SDN, but it is restricted by the capacity of
the switch and the level of attack. The edge switches can
be manipulated as TCP proxies, involving the attackers in
a 3-way TCP handshake, after which they can connect to
the controller or get blocked [85]. In [86], discussed a port
hopping technique in which they are dynamically mapped to
unused ports, increasing the attack cost as well as incurring
delay in serving the legitimate hosts.
G. CONTROLLER MODIFICATION
A controller modification approach that can be modified
to install parallel flow rules instead of linear is discussed
in [27]. The module that handles the incoming packets is
altered to note down all the switches on the route to the
destination and send back Flow-Add messages. It solves the
problems of additional hardware requirements, delays, loss of
information, and overload due to control packets.
H. TIME-SHARING SWITCH MIGRATION
The performance and scalability of SDN in large-scale
networks can be achieved through a time-sharing switch
migration mechanism for load balancing among multiple
SDN controllers [87]. The mechanism enables switches
to dynamically migrate between controllers based on their
current load and processing capabilities, ensuring a balanced
distribution of network traffic. The proposed solution is
designed to increase the efficiency and stability of SDN
networks by reducing the burden on individual controllers
and avoiding network congestion. It distributes the network
traffic evenly and reduces the burden on individual controllers, leading to a more efficient and stable SDN network.
The proposed solution is evaluated through simulations and
experiments, and it outperforms traditional methods in terms
of network performance. It proves that the time-sharing
switch migration mechanism effectively balances the loads
of distributed SDN controllers in large-scale networks.
I. INTEGRATION WITH ML
ML identifies low-rate DDoS attacks and automatically
adjusts network defense mechanisms [88]. It can effectively
identify and mitigate low-rate DDoS attacks while maintaining the normal traffic flow in the network. This is a valuable
contribution to the field of SDN security, demonstrating how
ML can be integrated with SDN to provide a flexible and
effective defense against low-rate DDoS attacks.
J. OPENFLOW SECURITY ANALYSIS
An OpenFlow security analysis creates a Data Flow Diagram
(DFD) of a target system using Microsoft’s STRIDE
(Spoofing, Tampering, Repudiation, Information Disclosure,
DoS, and Elevation of Privilege) and attack trees [89].
For DoS attack mitigation, it considers rate limitation,
flow aggregation, attack detection, randomization, proactive
strategies, and access control. It talks about a lightweight
enhancement of rate limit imposition on the switch, preventing it from getting flooded. Direct switch-controller
communication can also ease the overhead, but at the cost
of extra processing and management. These solutions mainly
deal with flow table or bandwidth management, handling
table-miss, or implementation-based.
VII. TABLE-ENTRY AND SCHEDULING-BASED
SOLUTIONS
The table-entry-based solution aims at attacks that exploit the
limited sizes of the OpenFlow switch buffering or forwarding
flow tables.
A. TABLE ENTRY SOLUTIONS
1) SDN-GUARD
In [60], SDN-Guard is a novel scheme that dynamically
reroutes the malicious traffic, adjusts flow timeouts, and
aggregates the flow rules to protect SDN against DoS attacks.
It aims to mitigate their impact on controller performance and
bandwidth usage and prevent TCAM memory overflow. It has
flow management, rule aggregation, and monitoring modules,
working together with an IDS. It significantly reduces the rate
of packet loss, round-trip time, switch memory, and network
bandwidth consumption and can be further enhanced for a
more realistic and large-scale deployment.
2) CACHING
Switch caches can temporarily store table miss flows,
separating packet headers and payloads in the cache queue
when a threshold is reached [90]. The controller is later
informed about a suspected attack, alerting it to apply the
necessary rules and investigate further. This approach may be
useless if the attack magnitude is beyond the cache’s capacity.
3) FLOODGUARD
FloodGuard is a scalable, lightweight, protocol-independent,
and efficient DoS prevention framework that manages flow
rules and table entry replacement policies [78]. It adds the
packet migration and proactive flow rule analyzer modules
to the CP [27]. The new proactive flow rules are generated
and dynamically loaded into the flow tables using a controller
status-based policy. The packet migration module handles the
flooded packets without affecting the service for legitimate
packets. Only the proactive rules are installed on the detection
of an attack, and the unknown flows are temporarily cached.
An additional device is needed to store table-miss traffic. The
article also discusses how SDN can mitigate DoS attacks in
other network environments, including data centers, legacy
networks, cloud computing, and IoT.
4) PACKET CHECKER AND FLOW TABLE OVERFLOW
PREVENTION
Packet Checker allows the controller to distinguish normal
packets from malicious ones, dropping them before being
processed by controller modules. For this, it has a dynamic,
real-time mapping table of MAC addresses against port
numbers. It validates a received packet by querying this
table, marking it legitimate if an entry is found in the table,
or dropping it, treating it maliciously. The packet drop occurs
using idle and hard timeouts associated with the flow rules.
A mitigation approach for flow table overflow adopts general
strategies such as rate-limitation and timeout adjustment
for controlling the flow table entries. A reactive, dynamic,
and event-driven eviction algorithm also queries the logs to
validate the traffic. If the traffic source fails this validation,
it is denylist, and all its flows exceeding the rate-limited
threshold are removed.
5) MIGRATION STRATEGY
Another table entry-based mitigation strategy states that when
a particular switch is under attack, it can use the vacant space
in the flow tables of other switches [91]. A DDoS solution
emerges from the flow table space during normal conditions
as a queuing theory-based mathematical model. There are
separate databases for flow table status that stores the current
status of all network switches, and the denylist database has
records of attack sources that have attempted to launch an
attack in the past. The redirection rules are installed on the
victim switch by the controller, resulting in the legitimate
flow being redirected to the nearest switch with unused flow
table space. Similarly, wildcard rules installed at the victim
switch help it to drop the malicious flow.
6) DOSDEFENDER
DosDefender is a table-based online DoS prevention mechanism that includes port management, attack detection, and
flow rule modules. It is a lightweight extension to the
OpenFlow controller that performs real-time analysis of
malicious packet-in messages [92]. It has port management,
flow rule installation, and Attack detection modules. The port
management module sends the incoming packet information
for attack detection, where the packet is validated. It sends
an early warning signal and Flow-Mod messages to the
administrator and the switches. The malicious packets are
dropped, and the flow rule module installs and updates the
flow rules at the switches connected to the malicious hosts.
They have also implemented SDN in a floodlight controller
for testing in a physical environment. Experiments prove that
Dos Defender can easily mitigate SDN-aimed DoS attacks.
B. SCHEDULING BASED SOLUTIONS
Scheduling-based solutions deal with SDN resource management and prevent it from overwhelming [28]. The hash
functions can be used to distribute the incoming packets into
different queues defined using them [93], [94]. The approach
would control traffic by traversing the queues in either a
round-robin or priority-based fashion, serving the purpose
at the cost of some delay to the legitimate users. The trust
values can be assigned to the users based on their history and
used as priorities [95]. Similarly, all hosts can be assigned a
value based on their usage of network resources, leading to
dynamic resource allocation. This approach fails when new
hosts are inserted after link verification, becoming vulnerable
to attacks. Inserting delays between the incoming requests
would also significantly limit the impact of the DoS attack.
1) FLOODSHIELD
FloodShield combines source address validation and stateful packet supervision techniques for mitigating DoS
attacks targeted on SDN networks [67]. It works on the
drawbacks of popular switch modification techniques like
AVANT-GUARD and FloodGuard, which mostly focus
on the CP by covering the entire infrastructure. It is a
lightweight and easy-to-deploy mechanism in the real world
that efficiently protects DP and CP with minimal overhead
and resource consumption as compared to other solutions.
2) ACTIVE QUEUE MANAGEMENT
Active Queue Management (AQM)-based Deterministic Fair
Sharing (DFS) for mitigating congestion-based DoS attacks
employs a B-Tree structure for storing and managing flow
information and considers a flow’s fairness as a legitimacy
factor [96]. The weighted fair share technique assures that
the buffer is optimally allocated to competitive flows. It gives
better performance and DoS mitigation, among other AQMbased techniques.
3) SLOT-BASED ASSIGNMENT
There are also slot-based flow assignments for the communication channels based on multiple parameters. As a result
of monitoring the flow, the flows identified as malicious can
be dropped, and bubble burst [97] can be used. This solution
dynamically allocates additional resources to the attacked
application without detecting or mitigating the attack. [98]
makes use of SDN and Network Functions Virtualization
(NFV) for DDoS defense. It is highly scalable and responsive, and it outperforms many previous implementations,
enabling resilient defenses against dynamic adversaries. Its
full-featured prototype has been implemented on standard
SDN platforms.
4) MULTILAYER QUEUING AND SCHEDULER MODULE
Multilayer fair queuing methods maintain a queue with a
threshold size corresponding to every switch. A single queue
can be logically divided into multiple sub-queues for every
corresponding switch, isolating the processing capacity of
each switch. Or, if the queue size grows beyond thresholds,
it dynamically expands into multiple sub-queues until the
collective size remains beyond thresholds, after which it
can be aggregated back to a single queue. In [27], reviews
various solutions that implement a scheduler module to
manage flow requests in the control layer. A time slicebased multi-queue scheduling method uses DDoS detection
and MultiSlot algorithm modules. The flow requests of a
switch are enqueued into their logical queues, and once the
corresponding module detects the DDoS attack, the time slice
allocation strategy is activated. The processing power of each
logical queue is determined based on the decisions of the
DDoS detection modules.
VIII. STATISTICS AND ENTROPY-BASED SOLUTIONS
Statistics-based solutions [28] collect, monitor, and analyze
statistical flow data [99] by employing edge switches, that
can detect abnormal traffic and mitigate attacks.
A. STATISTICS BASED
1) DAISY
A straightforward and lightweight DoS attack detection
and mitigation system (DAISY) analyzes the statistics and
blocks malicious traffic from attackers [19], [100]. Instead
of blocking an entire port or a host, it only blocks the
specific malicious traffic that causes saturation of resources
in the switches and controller. It is not hardware/ architecture/
or switch modification-based. The proposed system has
experimentally resulted in resource conservation, controlling
CPU utilization, bandwidth, packet drop rate, flow rate,
and faster response time during an attack. Subsequently,
the blocked flow rules are removed from the system using
parameters and functions. The iteration interval, flow request
limit, warning and blocking thresholds, and idle and hard
timeouts are set before startup. It then collects data, detects
threats, prevents, and reduces value. This statistics-based
approach lacks a signature database and does not require OF
switch statistics for attack detection.
2) SEQUENTIAL PROBABILITY RATIO TEST
Statistics can be used to classify normal and abnormal traffic
and evaluate the Sequential Probability Ratio Test (SPRT)
with DARPA Intrusion Detection datasets [62]. This is an
effective, lightweight approach, with an application hosted on
some third-party servers, designed to block attack-launching
botnets [101], [102]. A computational hurdle such as a
CAPTCHA can be added for the suspicious traffic to prevent
the bots from surpassing and dropping their packets. Even
legitimate hosts would experience some delays because of
puzzles and dependencies. Some approaches are filtering
based on the threshold values related to certain events and
network traffic, which, if exceeded, then new rules are
installed for packet redirection to the DP cache; as a result,
only the filtered packet-in messages go to the controller. Once
the source IP of the attack is detected, steps can be taken to
drop the traffic originating from that source based on specific
features such as destination address, traffic flow rate, volume,
pattern, number of invalid packets per window, and spoof IP
prediction through MAC and port number mapping [103],
[104], [105] suggests a mitigation approach in which false
host information can be provided to the attackers and firewall
activation for network defense and protection. There is a
management-related headache with integrating firewalls into
the SDNs.
3) OTHER STATISTICAL SOLUTIONS
The packet statistics collected from the switches and controller and a ratio of packet-in and total messages sent by the
host are calculated [19]. When this ratio exceeds a predefined
threshold, the controller instructs the switch to send fewer
messages. It provides a detection mechanism that inspects the
statistics stored in a table after fixed intervals to detect the
abnormality. New flow rules are used to block specific traffic
from the attacker. In [27], discussed flow statistics-based
DoS defense mechanisms: FlowSec and Blackbox. Using
FlowSec, the controller bandwidth usage is monitored, and
rate limitations are imposed on the switches for DoS detection
and mitigation. Similarly, finite state machines (FSM) are
used to fool and block the attackers for a suitable response
selection in Blackbox. The summary of the Architecture,
Table-Entry, Scheduling, and statistics-based technique we
discussed can be found in Table 5.
B. ENTROPY-BASED SOLUTIONS
Entropy is a measure of randomness in a specific data set,
with higher values meaning a more dispersed probabilistic
distribution and low values denoting a concentrated distribution. A decrease in the destination IP and port entropies is
suggestive of a DDoS attack. Some lightweight, thresholdbased mechanisms consuming fewer resources, but have a
considerable FPR [39] have been discussed. A combination
of entropy and Ensemble learning techniques with the help of
Shannon entropy can be used for SDN DDoS detection and
mitigation. A Generalized Entropy based metric can be more
helpful for low-rate DDoS detection in the CP. Application
layer DDoS attacks are difficult to detect, as they are almost
indistinguishable from regular traffic.
Variations in entropy can be used as a DDoS defense mechanism, with thresholds as incoming packet flow, entropy, and
count. If the flow rate differs significantly from incoming
packet flow, it may signal unusual traffic. The count is
maintained for the packets, and those with a higher count are
marked, suggesting that they have been involved in an attack.
It can further perform mitigation functions as well using
entropy and ensemble training in SDN in which detection
tasks are shifted over to the data plane. Edge node entropy
is evaluated and trained during the ensemble phase and thus
helps detect ICMP and SYN flood attacks.
An experimental setup for attack detection, identification,
and mitigation using OpenFlow-enabled sFlow switches
implemented in NOS applications consists of reduced data
gathering with sampling [61]. It is implemented with
the sFlow protocol, the anomaly migration unit is used
with OpenFlow, and the anomaly detection functionality is
implemented with the entropy-based algorithm. The solution
emulates a large enterprise environment and uses TCPreplay
to inject traffic in a specific Ethernet port and play trace
files using Scapy. The DDoS attack was emulated through
SYN packets having a predefined set of IP addresses/ports
and injecting them for the Portscan scenario. It demonstrated successful attack and anomaly detection in small to
medium-sized networks. An entropy-based DoS detection
algorithm that combines entropy with a statistical method:
KL divergence, beats the existing entropy and ML-based
methods [106]. Using entropy measurement to determine the
randomness of incoming traffic flows in the network, as a
low entropy indicates that a botnet generates the flow and
is part of a DDoS attack [107]. Based on this information,
the controller in an OpenFlow-enabled SDN can take
appropriate action to mitigate the attack. The performance
is evaluated using real-world DDoS attack scenarios, and
the results of comparison with traditional DDoS detection
methods show that the entropy-based approach is effective
in detecting DDoS attacks with high accuracy and low
FPR. Additionally, the approach can mitigate DDoS attacks
in real time, helping maintain network service availability.
The entropy-based solution in OpenFlow-enabled SDN is
promising for overcoming the challenges posed by DDoS
attacks as it is effective, efficient, and provides real-time
protection, making it a valuable addition to the arsenal of
techniques used to defend against these types of attacks.
Distributed Entropy variation detection in edge switches
is also a popular, lightweight statistical approach, reducing
the controller overhead [108]. Attack source can be identified
based on the variation between entropies of different hosts,
where entropy must be set according to parameters involving
the number of hosts and the network size.
1) RENYI ENTROPY WITH PACKET DROP
A DDoS detection technique using Renyi Entropy with
Packet Drop (REPD) considers information distance metric
for evaluating the fluctuation of network traffic and performs
packet drop as a mitigation strategy for low rate DDoS
attacks [1]. The experimental results are promising as they
perform better than Shannon, Hartley, Collision, Min, and
Generalized entropies. Combining Shannon (SE) and Renyi
(RE) entropies can effectively deal with heavy malicious
traffic by utilizing a Snort-Ryu implementation [109].
Adding Generalized Entropy (GE) for Information Distance
(ID) further increases the accuracy of DL models like
Stacked Auto Encoder (SAE) and Convolutional Neural
Networks (CNN). The summary of attack, prevention, and
Entropy-based techniques we discussed can be found in
Table 6.
FIGURE 11. DeepAir approach.
IX. ML BASED SOLUTIONS
ML-based solutions [28] provide a defense mechanism using
attack-free flows trained algorithms for malicious DoS traffic
and anomaly detection. Support Vector Machines (SVM),
Self-Organizing Maps (SOM), Gated Recurrent Units (GRU)
[68] or Neural Networks (NN) are widely used with K
nearest neighbor (KNN) algorithms that classify and drop the
malicious flows with the help of an application. This requires
a strong and accurate classification algorithm that can make
decisions even from uncertain information, using supervised
and unsupervised techniques based on prediction models of
suspicious network connections. It takes time to train the ML
models against several attacking patterns, and they will likely
cause delays while serving even legitimate requests. It has
proposed a graphical method [110] to store the known traffic
patterns and check them against new traffic to determine if
they can be malicious. These algorithms involve clustering
and flow grouping that consumes high resources, making it
less efficient [29], [111].
For the high bandwidth required for data transmission,
federation learning has evolved as a distributed ML method,
wherein, under server supervision, multiple clients can
collaboratively train a model using their local data. Hence,
there is no data transmission but of the training parameters
between clients and servers while overcoming synchronization issues. A system model uses an SDN-enabled,
context-aware, proactive client selection algorithm based on
local information [112], [113]. It calculates link utilization,
discards those above 70%, and updates the network topology.
Different ML algorithms and techniques like Recursive
Feature Elimination (RFE), Principal Component Analysis (PCA), Random Forest (RF), K Nearest Neighbors
(KNN), and DL solutions like Artificial Neural Networks
(ANN), GRU, Naive Bayes Graph and clustering based,
Support Vector Machines (SVM) have been employed and
tested for DoS and DDoS attacks in SDN. An ML-based
approach for detecting malicious packets in SDN, called
OpenFLow-enabled DPI (OF-DPI), uses classifiers like
KNN, SVM, and MLP. It calculates precision, recall, F1-
score of the model as evaluation metrics [70]. RF and
XGBoost classifiers can achieve 90% average detection
accuracy [114], [115].
SVM is a supervised learning method for classification
that optimally separates the considered classes after learning
from samples. ANN has no task-specific rules, and it learns
from training instances. It has connected units called artificial
neurons that help detect DoS and DDoS in conventional
and SDN networks. A structured classifier built upon this
and all the classification methods helps compare the traffic
flow against existing modeled patterns and classify those
connections as legitimate or malicious [116].
A. DEEPAIR
In [117], DeepAir is an adaptive Intrusion Response System
(IRS)-based solution for defense against cyberattacks in
SDNs based on Deep Reinforcement Learning. It uses the
Markov decision process and Double Deep Q-Network.
An ML-based IDS forwards the system information to the
IRS upon detection of an anomaly. The IRS coordinates
the information collector, data storage, control agent, and
response policy placement modules to defend against cyberattacks while minimizing the cost of benign traffic forwarding
and policy deployment in SDNs. Results show that DeepAir
effectively prevents malicious packets from reaching the
victim in all DoS attack scenarios. The DeepAir architecture
can be seen in Figure 11.
B. LINKGUARD
The traditional security mechanisms for SDN are inadequate for link discovery, which is crucial for network
management and configuration. In [118], a new framework
called LINK-GUARD uses signature-based and machine
learning-based methods to detect security threats during
link discovery. The framework is designed to be efficient
and scalable, as well as able to identify threats accurately.
The evaluation results of the framework demonstrate its
effectiveness in detecting attacks, with a low false positive
rate (FPR) and high accuracy, while also being able to handle
large-scale networks. This framework provides a promising
solution for improving security in SDN networks during link
discovery and shows that their proposed framework outperforms existing methods regarding accuracy and scalability.
C. ANN
Under ANN, a Back Propagation Neural Network (BPNN)
works on error information backpropagation and computed
information forward propagation principle, using error correction learning. It can be used in modules of attack detection,
triggering and traceback, and attack mitigation, such that an
abnormal flow triggers the detection process. The attack path
is then traced, and the mitigation process is applied. Another
ANN approach is the Self-Organizing Map (SOM), which
TABLE 5. Statistical, table, scheduling and architecture based solutions.
TABLE 6. Attack simulation, prevention, and entropy-based solutions.
uses unsupervised learning with access control and classical
mechanisms. It forwards only the legitimate flows and is
highly accurate because of the ranking of flows based on their
representative features. The result is a low dimensional space
formed by incorporating competitive learning, that secures
the SDN.
D. GRU AND NN
An anomaly detection and mitigation system using GRU, NN,
and fuzzy logic can detect anomalies when the forecasting by
NN, which is trained to forecast future traffic, fails. It utilizes
SDN capabilities to gather flow information and periodically
feed it to the DL model for anomaly detection and mitigation.
There are six NN for each dimension: bits and packets
per second, source and destination port entropy, and source
and destination IP entropy. The resulting predictions are
compared with actual traffic in a fuzzy membership function,
and the flow is classified as normal or malicious based on the
defuzzification threshold. Shannon’s entropy has been used to
convert the qualitative IP and port information into numbers
for the NN. As a result, the DoS attack, which usually lowers
the destination entropy, can easily get detected [119].
They aim to design an autonomous system to detect and
immediately mitigate an attack when alarmed, with no human
interference. This can be achieved in part by using SDN’s
centralized control plane and a safe list to prevent legitimate
traffic from being dropped due to FPR. It blocks an IP address
for 20 seconds if it is identified as malicious and is not present
in the same list. The proposed solution efficiently mitigates
the DDoS and port scan attacks.
E. DNN AND LSTM
The botnet, or a set of connected, unauthorized, and
unauthenticated infected systems that are directed to perform
malicious activities, can harm our systems or steal sensitive
data through phishing, spamming, and a multitude of other
techniques [120]. SDN can help detect botnet attacks and
devise anti-malware strategies by utilizing a hybrid DL
approach that integrates DNN and LSTM. They propose a
deep learning-based system for detecting and distinguishing
benign from malicious behaviors. DNN provides efficiency,
accuracy, and reliability and increases the algorithm’s predictive capability, while LSTM effectively learns long data
sequences. They train the model with 90% of the dataset and
use 10% as the test set.
SDN-based fog computing architectures, the trending networking paradigms for IoT infrastructure-based applications,
are also vulnerable to botnet attacks, creating a need to
formulate a security framework for monitoring the network
against them. DL-based IDS detects botnet attacks in an
SDN-enabled IoT system like Fog computing. This system
consists of a botnet dataset and a training and detection
paradigm, efficiently demonstrating and achieving the task
with high accuracy.
DL-based attack classification methods use Python
libraries like Pandas, Numpy, sci-kit Learn, seaborn, and
Tensorflow [121]. The anomaly detection techniques used
in the research are Random Forest (RF) and Convolutional
Neural Network (CNN). They develop and consolidate
multiple decision trees for an accurate estimation model in
RF. In CNN, they aim to reduce the information parameter
more than in ANN and diminish the data boundaries. This is
achieved by parameter sharing and equivalent representations
in sparse connections, which extend CNN adaptability.
It achieves 99.95% accuracy with the IDS-2018 dataset.
F. SUPERVISED LEARNING APPROACH
A supervised learning (SL) model can detect flooding
DDoS attacks targeted to SDN controllers by flow fluctuations [122]. It provides training to a predictor with
enough data to calculate and return a class with the highest
probability, and later uses it for making decisions. They
use standard techniques like KNN, generalized linear model,
decision tree (DT), FeedForward Neural Network, Naive
Bayes, SVM, bagging tree (BT), and discriminant analysis.
They use the APRF (Accuracy, Precision, Recall, F-measure)
metrics to compare the performance of their model with
the existing solutions and achieve a successful prediction
rate with a 95% confidence interval for both standard and
attack states. Increasing the training set size further decreases
output fluctuation. They use a validation holdout method by
reserving 20% samples for validation purposes. KNN, DT,
and BT show promising results with DARPA and SDN-based
training sets with more than 90% detection accuracy. The
framework successfully detects flooding DDoS attacks on the
SDN control plane but has limited scope for non-volumetric
attacks such as Low-rate DDoS.
G. P&F FRAMEWORK
In [66], LDoS or low-rate DoS has a lower attack rate
but is performed periodically under concealment. For LDoS
mitigation in SDNs, an ML-based, real-time lightweight
framework called Performance and Features (P & F) has been
discussed. It locates attack sources and victims using flow
features from time-frequency analysis and sets appropriate
mitigation schemes. It has high accuracy in detection and a
low false-positive rate.
H. FFCNN AND MFF
An anomaly-based DL scheme FFCNN (Feed Forward
Convolutional Neural Network) can detect signs of LR DoS in
the arriving flow when hosted in the application layer of SDN
architecture [123]. Single-feature methods suffer from low
recognition and false alarms, as they have insufficient feature
extraction. This can surpass LDoS attacks, which can be
solved by the Multi-Feature Fusion (MFF) approach by using
the K-nearest neighbor (KNN) classifier and by analyzing
changes in traffic and the router queues during LDoS attacks.
The Random Early Detection (RED) algorithm helps test the
LDoS attacks and feature extraction, by which it can estimate
the queue lengths and drop the packet in case of congestion.
Signal processing technologies cannot efficiently detect
LDoS attacks in real network environments. Hence, detection
using the packet queue size during the routing stage can
improve detection using an active queue management mechanism. We propose combining signal processing detection
and router queue detection technologies for LDoS attack
detection.
I. DETECTION
The phases in the detection framework are as follows:
• Data pre-processing: feature selection is performed on
flow statistics to create different datasets
• LR DoS detection: predictions can be made from the
trained and tested modules to help the decision-making
process. This helps trace the datasets and analyze the
ROC (Receiver Operating Characteristic) for different
dataset classes. It performs better than other ML models
like SVM, Random Forest, MLP, etc. in an IOT SDN
environment for real-time system performance analysis.
• Factor detection is based on KNN classifier that measures the Euclidean distance between different features
involving queue length, packets, and acknowledgment.
For a network system studied in both normal and
LDoS attack states, the KNN classifier returns a posteriori
probability through sigmoid functions. These results are
fused to classify the decision index based on the threshold.
The multiple-feature approach outperforms other detection
approaches due to its low false positive/negative probabilities
and higher, accurate identification probability. This approach
can be practically used with high-performance routers and
firewalls.
KNN classifier and cryptography can be used for
cross-domain DDoS detection, ensuring data security during
transmission. Some of the solutions adaptively redirect the
traffic across multiple resource replicas and thus succeed
in blocking botnet-based attacks and DoS detection and
TABLE 7. ML-based solutions.
mitigation against the cloud. For this, they use the centralized
control and programmable features of SDN and monitor the
flow tables. SDN-based Internet Service Providers (ISPs)
employ entropy-based methods and ML algorithms to get
the advantage of the security provided by SDN. An SVMbased network IDS to accurately detect a DDoS attack
suffers from low detection efficiency and long detection
time. A Moving Target Defence (MTD) technology regularly
changes host IP addresses with a combination of real and
virtual addresses [125].
J. RATE LIMITING
Limiting the rate at which packets are sent to the controller
can help in DoS prevention [126]. Flow aggregation and
optimal timeout values can be used to avoid flow table
overflow. This approach is efficient but can also lead to
the dropping of legitimate packets. Multilayer queuing of
Packet-In messages and Round-Robin fetching of queue
requests can be used. A trust value based on IP can be
assigned to new packets based on its historical behavior to
avoid DoS attacks [127].
K. AUTOENCODER
A DL-based IDS technique, Autoencoder, along with
Long Short Term Memory (LSTM), Random Forest (RF),
and Information Gain (IG) methods for feature selection
during pre-processing phase can help tackle the DDoS
attack problem in SDNs [39]. ML and DL techniques use
mathematical equations, requiring numerical data instead of
categorical through conversion using the OneHotEncoder
class. A DDoSnet model consisting of an Autoencoder,
LSTM, and Recurrent Neural Network (RNN) can detect
attacks more accurately and with a lesser FPR. A DL solution
can use the traffic collector and flow installer modules to
identify the flow type and extract features through their
headers. This goes as input into the DL model, and the traffic
is classified as legitimate or malicious. A 2-level approach
can have a course granularity level (at the attack source)
where suspicious components and ports are detected and A
fine granularity level where DL helps distinguish normal
traffic from suspicious traffic using the CNN model. The
summary of all the machine learning solutions we discussed
can be found in Table 7. A comparative statistical analysis
of these ML techniques can be found in Figure 12, and the
accuracy of ML and DL techniques for DDoS detection in
SDN (2023-2024) can be found in Figure 13.
L. CHALLENGES IN ADOPTING ML-BASED SOLUTIONS
While ML-based solutions offer significant advantages, they
are not immune to challenges in the context of DDoS
mitigation. These challenges include [128], [129], [130],
[131], [132]:
• Scalability Issues: Scalability is a critical factor in
SDN-based DDoS mitigation. During a DDoS attack,
network traffic volumes increase, so SDN controllers
and switches must handle increased workloads efficiently. However, SDN controllers may encounter
scalability issues, limiting their ability to effectively
manage large networks with rapidly changing traffic
patterns.
FIGURE 12. DoS/DDoS detection using ML algorithms.
FIGURE 13. Accuracy of ML and DL techniques for DDoS detection in SDN
(2023-2024).
• Controller Overload: The overload of SDN controllers
presents a significant challenge in DDoS mitigation.
When confronted with a massive influx of DDoS traffic,
SDN controllers may become overwhelmed, resulting in
attack detection and mitigation delays. Furthermore, it is
necessary to investigate the causes and consequences of
controller overload during DDoS attacks.
• Attack Signature Variability: DDoS attackers are constantly devising new ways to circumvent detection and
mitigation efforts. This variation in attack signatures
presents a significant challenge to SDN-based DDoS
mitigation systems, which rely on predefined patterns to
detect malicious traffic. The difficulties include attack
signature variability, the limitations of signature-based
detection in SDN, and the requirement for adaptive and
heuristic-based approaches to identify and respond to
emerging attack patterns.
• Network Visibility and Monitoring: Effective DDoS
mitigation requires full network visibility and monitoring. SDN provides greater visibility and granular
control, but it also complicates monitoring dynamic
network flows and policies while implementing MLbased solutions. The challenges include maintaining
real-time network visibility during DDoS attacks,
as well as monitoring a wide range of traffic sources and
destinations.
• Resource Allocation and Dynamic Provisioning:
Resource allocation and dynamic provisioning are
critical components of SDN-based DDoS mitigation.
During an attack, network resources must be allocated
carefully to mitigate the attack’s impact while not disrupting legitimate services. The challenges include the
possibility of misallocating resources or unintentionally
amplifying the attack.
X. NETWORKING AND HYBRID SOLUTIONS
IoT ecosystems are becoming more complex as networks
take on a larger role, making virtualization technologies
like NFV and SDN increasingly important for resource
management and security. Additionally, these technologies
integrate AI and machine learning to automate threat
detection and response, allowing hardware and software
to operate together efficiently. We will explore specific
advancements and applications related to network-based
solutions and hybrid solutions in the following subsections.
A. NETWORK FUNCTION VIRTUALIZATION
The ETSI Industry Specification Group (ISG) promotes NFV,
which combines networking resources into a software-based
virtual network entity that can be easily consolidated and
managed by commercial servers, off-the-shelf equipment,
and network switching gears for IT operations. NFV decouples software from the hardware and deals with virtualization
architecture, virtual network functions, management, and
orchestration. It is an IoT ecosystem with advanced virtual
monitoring tools like IDS and DPI. It imparts security
to virtualized networks [133] and separates the network
functions from hardware devices without requiring any
wiring/ configuration. This saves IT equipment costs and
resources while making the network flexible and scalable
with short orchestration cycles. NFV provides software-based
network functions to SDN, by running on the industry
standard servers to virtualize the functions of routing, load
balancing, and policy management [69].
SDN, NFV, and ML combined work in 2 planes: security
orchestration, enforcement, and implementing closed-loop
automation for threat detection and mitigation. The control
and management blocks include ETSI and MANO stack
modules along with SDN controllers, while the infrastructure
block implements IaaS and is responsible for traffic forwarding [134]. The security orchestration plane is responsible for
the run-time security policy configuration and their updates
through monitoring data and the enforcement of security
policies in the IoT domain. AI-based reaction agent dictates
the mitigation actions using ML models and IoT behaviors
and is assisted by the orchestrator, who has a system model
database with information about enforced policies, VNF
configurations, device information, etc.
B. NETWORK-BASED SOLUTIONS
Software-defined radio (SDR) technology integrated with
SDN maximizes spectrum utilization in wireless networks
and serves as a cost-effective advancement of radio
devices [21]. Integrating optical fiber technology with SDN
CP helps in achieving precise and efficient control over the
DP. A network status synchronization-based approach of
geographically separated multiple controllers was proposed
for addressing the scalability issue of SDN controllers.
An SDN programming language, Frenetic, eliminates asynchronous and event-driven interactions between switching
devices through a network query language that classifies
and aggregates the network traffic statistics. Wild card rules
can be used to match more packets than exact matches and
process them in the switches themselves without requesting
the controller. Nettle is used for improved responsiveness
to dynamic network changes [135], [136]. It returns specific usage rules for authentication or Traffic Engineering.
A switch-level parallelism is performed on multicore servers
for packets missing their entries in the flow table, thus it binds
the event processing loop and controllers thread memories
to the respective client switches. Pyretic makes it possible
to act based on a rule on packets possessed by another rule
through sequential composition and abstraction of topology
between physical and virtual switches. A packet is stamped
with a number indicating the rule set to be applied to it and
be processed accordingly [137]. HyperFlow helps to sustain
a consistent and global view across all controllers using a
publishing mechanism. A controller uses this publish and
subscribe system to notify users of a system status change
through an event for immediate action. SDNi can be used for
interconnectivity and to facilitate message exchange among
different SDN domains, i.e., a network slice managed by a
specific controller [138].
In the Moving Target Defense (MTD) strategy, the real
IP of a host remains static while virtual IPs associated
with hosts are randomly mutated [139]. AnonyFlow can be
added as a network endpoint anonymization service using
SDN implementation for user privacy through AnonID,
Network, and Machine IP [140]. SDN can be used in
Green Networking and can offer several economic and
environmental benefits and reduce network-wide energy
consumption. Also, the service provisioning model of IaaS
can be extended to accompany network services for more
flexible cloud computing.
Optimizing network resource allocation in SDN assists in
addressing the challenge of allocating network resources to
meet the diverse service requirements in large-scale SDN
deployments [141]. A scalable rate allocation algorithm optimizes network resource utilization while meeting the diverse
service requirements of different applications. The algorithm
considers factors such as traffic demand, link capacity, and
QoS requirements. Simulations are used to evaluate the
system’s performance and compare it to existing approaches,
leading to the conclusion that it can effectively allocate
network resources to meet diverse service requirements while
also improving network resource utilization. It is a scalable
solution for optimizing network resource allocation in SDN
while meeting the diverse service requirements in large-scale
deployments.
C. HYBRID SOLUTIONS
Hybrid solutions are those that combine multiple technologies to formulate an attack detection or mitigation mechanism. Some researchers combine ML and table entry-based
solutions to protect system resources by associating idle
timeouts for each flow entry. As a result, decisions are made
regarding forwarding, dropping, and deleting.
Two different ML models, Support Vector Machines
(SVM), which is a supervised learning technique, and
Self-Organizing Maps (SOM), which is an unsupervised
learning technique, can be combined [150]. SVM trained on
labeled data cannot detect new attacks as easily as SOM,
which has a high false positive rate. This hybrid model
overcomes both drawbacks and gives an improved detection
rate, accuracy, and lower false positives than separate
implementations of the used techniques. They establish a
TABLE 8. Hybrid solutions, NFV, blockchain, IoT and cloud.
96.77% accuracy, 90.45% detection rate, and 0.032% false
alarm rate.
A dynamic routing mechanism (DIFF) can be used in
networks with multiple paths and links. It differentiates
the flows according to their resource utilization selects the
routing paths that avoid flow table overflow, and ensures
efficient bandwidth distribution. There can be a centralized
control-based anomaly detection system for SDNs with
anomaly detection and pre-processing modules. The flow feature vectors are standardized, normalized, and then classified
as normal or malicious. Some researchers propose source
tracing methods using hop-by-hop backtracking algorithms
to find the port through which attack traffic passes.
CrossPath attacks exploit shared links in control and
data traffic paths, disrupting the SDN control channel
Xie et al. [156]. It employs the Adversarial Path Reconnaissance (APR) technique to identify attack target paths and proposes a lightweight CrossGuard defense system to counter the
crossPath attack. In [151], quantum Key Distribution (QKD)
is an efficient quantum-based approach to secure communications, but is vulnerable to-DoS attacks [152]. SDN was used
for DoS mitigation in QKD-enabled networked microgrids.
In [153], SDN enables the implementation and management
of resource allocation strategies, VM migration, topology
monitoring, and programmable interfaces in fog computing.
They propose an SDN fog network in which multi-fog nodes
optimize offloading decisions and resource allocation in
an observable environment. Inter-SDN communications are
used to provide interconnection among individual controllers,
maximizing system performance.
XI. SDN WITH BLOCKCHAIN AND IOT
The integration of SDN, blockchain, and IoT is transforming
how networks are managed and secured. SDN offers
centralized control, improving the flexibility and scalability
of IoT networks. It’s centralized nature raises security
concerns. Blockchain, with its decentralized and immutable
ledger, enhances security by distributing trust and preventing
single points of failure. Combining SDN and blockchain in
IoT environments ensures efficient, programmable networks
while maintaining data integrity, security, and resilience
against attacks, creating a more robust infrastructure for
future IoT applications.
A. SCOPE IN BLOCKCHAIN
A successful Eclipse, Memory flooding attacks, or zero-day
vulnerabilities can lead to a DoS attack in Blockchain-based
financial applications, causing enormous financial loss to
the stakeholders. These blockchain-based solutions save the
transaction details and share the IP addresses to be blocked
based on the trust and validation of the stakeholders. In the
case of a reflection attack, the spoofed traffic is sent to the
victim, which consumes the resources and saturates them.
This solution assumes that the originating IP address is not
spoofed and is mainly implemented using smart contracts.
Its future scope lies in the hybrid solutions using parallel
blockchain, X route, and Ethereum 2.0.
In a multi-controller architecture for network control,
we can cross-check the information coming from one
controller against others and then collectively decide if any
of them is under attack, using blockchain technology to
secure the control layer [142], [154], [155]. Here, it is to
be ensured that there is no communication between the
controllers, or else a malicious controller might impact the
other controllers. The anomalies are detected by observing
the controller activities in the case of a deterministic
controller. If non-deterministic controllers based on ML
algorithms are used, this method could not be deployed.
Using routing algorithms, a route can be verified to check
for consistency, flaws, or anomalies based on certain criteria
involving loops or dead nodes. The Hidden Markov Model
(HMM) could be used to determine the probability of attack
based on the observation sequence. This solution is based on
both performance and plane structure to improve observer
efficiency. HMM, when combined with KNN or SVM, could
perform even better.
B. ROLE OF SDN IN IOT
IoT devices deal with sensitive user information in a wide
multitude of devices, such as smart cars, homes, wearables,
healthcare, etc., and hence are at risk of integrity and confidentiality [133], [157], [158]. They deal with a three-layer
taxonomy that consists of IoT-oriented devices, cloud networks, platforms, and IoT applications. The IoT device
layer is vulnerable to hardware Trojan attacks, replication,
tampering, malicious code injection, and battery-draining
attacks. IoT-oriented platforms and cloud networks suffer
from attacks such as eavesdropping, DoS, spoofing, manin-the-middle, routing-based, service manipulation-based,
privilege escalation, or security inter-working. Similarly, the
security threats in IoT applications are viruses, worms, data
leaks, service logging failures, phishing, and inconsistent
software patches. SDN is helpful in IoT environments due
to its flexibility and programmability, along with solutions
like short-range meshed networks, WSNs, low-power cellular
networks, and 5G. SDN-based security solutions for IoT
environments are Traffic Isolation, Network Monitoring,
Dynamic Flow Control, Host and Routing Obfuscation, and
Network Programmability [144], [159], [160].
The article [161] surveys the current state of SDN for IoT
and examines various aspects such as architecture, network
management, security, and performance. They also highlight
the challenges and opportunities in the field, including
security and scalability. It provides insight into using SDN
for securing IoT and identifies areas for further research.
The article summarizes the main findings and highlights the
key challenges and opportunities in the field. It is a valuable
resource for researchers and practitioners interested in SDN
for IoT.
IoT has been shifting towards edge computing instead of
centralized cloud computing, and it can be further strengthened using distributed intelligence, with which it can extract
information and make edge-level decisions on whether to
actuate or outsource the tasks within the cloud [112]. SDNbased IoT architecture enables the gateways to perform
dynamic processing at the edge based on the current
network state, mitigating the edge computing complexity.
In [12], SDN implementation in the fog layer exploits the
programming capabilities of SDN and the mobility of fog.
In [106], uses an SDN approach in which the controllers are
logically centralized and physically distributed, improving
the efficiency of smart grid systems. A single controller can’t
handle a large network, creating a performance bottleneck,
and hence it is divided into centralized and distributed
structures. The controller topology used can be flat or
hierarchical.
A comprehensive overview of the relationship between
SDN and DDOS attacks in cloud computing environments is
given in [162], [163], and [164]. It reviews the latest advances
and examines the various challenges and opportunities in the
field. They provide a detailed analysis of the various DDoS
attack techniques and how they can be mitigated using SDN.
Key research issues and challenges in the field are identified,
and insights into potential future directions are provided.
The article concludes by summarizing the main findings
and highlighting the key challenges and opportunities for
SDN in the context of DDOS attacks in cloud computing
environments. In [165], SDN, NFV, and cloud computing
help solve the network management problems in smart grids.
1) IIOT
There are multitask learning-based algorithms for the
prediction of network traffic according to its spatial and
temporal features in SDN-enabled IIoT networks, which
have mutagenicity, long-range dependency, chaos, and selfsimilarity. citewang2022multitask. CNN and LSTM networks help deal with network traffic prediction, tomography,
and spatiotemporal features.
2) IOMT
A software-defined approach for managing resources on
the Internet of Multimedia Things (IoMT) has been given
in [143]. It provides an energy-efficient and load-balanced
resource management scheme for the IoMT, taking into
account the dynamic and heterogeneous nature of multimedia
devices and applications. The current resource management
approaches for the IoMT are not well-suited for managing
the diverse and changing requirements of multimedia devices
and applications. This software-defined approach leverages
the flexibility and programmability of SDN to dynamically
allocate resources based on the changing needs of multimedia
devices and applications. A simulation-based evaluation of
the resource management scheme is conducted, showing that
it can effectively balance resource utilization while reducing
energy consumption. It also discusses the limitations and
challenges of their approach, including the need for accurate
device and application characterization and the need for
efficient algorithms for resource allocation and energy
management. The scheme has the potential to significantly
improve the energy efficiency and load-balancing of the
IoMT. The summary of blockchain, NFV, IoT, and hybrid
solutions can be found in Table 8.
XII. ROLE OF SDN IN INTRUSION DETECTION SYSTEMS
AND LOAD BALANCING
Due to the voluminous increase and diversification of
network traffic and the increase in the number and types of
attacks, organizations need to deploy a Network Intrusion
Detection and Prevention System (NIDPS) [166]. IDS is any
software or hardware invented to detect intrusions or prevent
a network from getting hacked [167]. It is a standard security
solution for monitoring and detecting malicious activities in
an organizational network. An antivirus also monitors all
system activities but cannot detect buffer overflow attacks
on system memory or malicious process behavior. IDS can
detect inconsistencies in file system data, network events, and
system calls [168]. The detection engines can be classified
as anomaly-based and signature-based by detection method,
or host-based and network-based in the context of their
application areas [169].
IDS based on signatures uses a signature database for
monitoring and validation of the input stream and updating
the attack signatures. It searches the network traffic for a
series of malicious bytes or packet sequences using regular
expressions or string-matching algorithms. It can only detect
attacks whose signatures have already been stored in the
database. New signatures are to be created every time
it encounters an unseen type of attack. It can be easily
deceived by experimenting with behavioral patterns or using
encrypted channels, and the system efficiency depends upon
the difference in the rate of creation of new signatures
between the developers and attackers.
Anomaly-based IDS checks if network behavior is by
the predefined range by investigating commonly used ports,
protocols, and bandwidth and raising the alarm in case of any
deviations. Its protocol analysis module helps in increasing
the rule set to achieve lower false alarms. The way it is tested
according to the protocols and the extent to which it knows
about acceptable system behavior determine its efficiency.
It can detect even a novel attack whose attack signature
does not exist if it falls outside the normal traffic pattern or
expected system behavior, where the signature-based method
fails.
Host-based IDS(HIDS) performs internal monitoring.
They are placed on the devices to probe into the running
processes and audit trails or system logs for any malicious
activity. They are passive devices used to inform about
an attack in progress and are very useful in systems
where the resources are routinely, and remotely accessed.
It can’t see the network traffic and lacks cross-platform
interoperability [168].
Network-based IDS (NIDS) monitors and detects malicious network traffic [170]. It searches all inbound packets for
any suspicious pattern, and accordingly informs the network
administrator or blocks the malicious flow. It is also a passive
detection device but is confined to the entire network at once.
The Snort tool is used for such NIDS and NIPS systems as
a sniffer, packet-logger, or intrusion detector. The host and
network-based IDS can be seen in Figure 14.
A hybrid type is also possible, which flexibly combines
these approaches with advanced characteristics.
FIGURE 14. HIDS and NIDS.
Intrusion Detection System (IDS) trained with ML modules like REP tree, Multi-Layer perceptron (MLP), Support
Vector Machine (SVM), J48, and Random forest have
been proposed. The controller simply has to process the
incoming flows and make decisions on them, without dealing
with flow classification complexity. High-quality training
datasets offer more efficient anomaly detection, and such
network datasets are not readily available for public use and
evaluation of IDS in SDN environments, as it is illegal to
access sensitive customer information contained in them.
So outdated, anonymized payload data is generally used, and
it affects the classifier model’s performance.
A language-independent and technology-agnostic framework to mitigate low-rate DDoS attacks in SDN uses DL
techniques by utilizing GPU for faster classification. It can
be implemented to train various models for the identification
of DDoS attacks. In [88], the framework comprises two
individual systems: an Intrusion Prevention System (IPS) and
an Intrusion Detection System (IDS).
The Identification API in the system facilitates flow
processing and classification of flow statistics to distinguish
a legitimate flow from an attack using trained ML/ DL
models. It identifies a malicious flow in LR-DDoS attacks,
as the IDS API returns a 0 for normal flow and a number
corresponding to the type of detected attack otherwise.
The Attack management module is informed of a potential
attacker, the IP address is denylist, and its flow drop
probability is modified.
The architectural model of an IDS consisting of a collector
along with anomaly detection and mitigation modules is
considered in [61]. The flow information is collected using
sFlow-like monitoring mechanisms and is periodically fed
into the detection module, where all flow entries are inspected
to reveal a potential attacker or attack victim. The algorithms
used for the detection of DDoS attacks, Portscan, and Worm
propagation are ML, data mining, entropy-based, or statisticsbased. Once detected, all network metrics are passed to the
mitigation module, which neutralizes them by inserting or
modifying the flow entries by which malicious traffic is
blocked.
A typical NIDPS system has the following components [166]:
• Packet Capturing Module: acquires packets from the
network in inline or passive modes, for real-time
processing or buffering
• Packet decoder: applying protocol-specific rules
to decode packets and generating alerts for nonconforming packets
• Pre-processor: in low level pre-processing, it prepares
the packets for defragmentation, reassembly, and session
conformance; while at a high level, the application
protocols of the packets are validated
• Detection engine: applies rules for comparing incoming packets with defined malicious patterns through
signature-based, anomaly-based or hybrid engines
• Alerting module: generating an alert if a rule matches
the packet’s content. It creates log records and can also
block the malicious flow when employed in an IPS
• Output module: generates packet statistics after it passes
through the NIDPS system for further course of actions
IDS can detect immoderate bandwidth consumption,
ICMP DoS, SYN flooding, and ARP spoofing attacks [133].
The traffic is generally forwarded to a honeypot for further
inspection of potential attacks, as IoT devices don’t generally
meet the computational requirements of existing Deep Packet
Inspection (DPI) systems. Open sources IDS/IPS systems
and tools like Snort, Suricata, and Bro (Zeek) can set
the rules based on packet count thresholds and parse the
information for the investigation. Snort is a signature-based,
easy-to-configure IDPS tool that can monitor network traffic,
compare it against signatures, log attacks, and present attack
statistics for the matched packets using Libpcap [166].
It detects and generates alerts in IDS mode while also
blocking the malicious packets in IPS mode. Snort 3 was later
released as a multithreaded variant of Snort with advanced
features. Suricata is multithreaded and handles more traffic
across multiple detection engines. With a similar mechanism
as that of Snort, it generates the statistical output and stores it
in a text file or in JSON format. Zeek (Bro) only supports
the IDS mode and deploys worker agents on the network
devices to fetch the device logs. It has an event engine and
a policy script interpreter to create alerts upon detection of
any malicious activity.
It has been observed that suricata outperforms Snort in
both IDS and IPS modes and Zeek in IDS mode due to its
multithreaded architecture [171]. But all these suffer from
passive spots such as zero-day attacks, in which an unknown
attack packet damages the system. They target undisclosed
vulnerabilities, and it becomes impossible to respond immediately to the damage they cause until new countermeasures
are updated. Zero-Day Attack Packet Detection Protocol
(ZAPDP) and a system for internal systems communication
perform a DPI regression inspection on the flow packets,
which, after processing, results in information matching raw
data detected in a zero-day attack. It solves existing low-level
problems and provides raw data information for further
analysis of zero-day packets. For flow classification, there
are solutions applicable at both the transport and application
layers that use ML (methods: SVM, KNN, random forest)
and DL (models: MultiLevel Perceptron (MLP), CNN, GRU,
Long short term memory (LSTM), and Neural Networks
(NN).
OpenFlow technology can be used to implement firewalls,
network scans, IDS and IPS mechanisms, and abnormal
traffic detection without any additional hardware cost in an
SDN environment [172]. The program connects OpenFlow
with the Open Source IDS/IPS Suricata and provides an
automated IPS function to enhance the security problems of
SDN. It integrates Suricata’s IDS function and OpenFlow’s
IPS function so that OpenFlow can automatically implement
the intrusion-blocking functionality when Suricata detects an
intrusion.
Firewall Implementation: OpenFlow has packet forwarding and dropping facilities that can be exploited for SDN
applications supporting the security policies to bring about
the functionality of a firewall. Network scan detection:
Network scan attacks based on TCP can be easily controlled
by network flow monitoring during TCP sessions Similarly,
we can detect abnormal traffic and achieve enhanced security
by linking Suricata with OpenFlow.
A typical IDS works by analyzing the packet contents
to check for possible attacks, but this is possible by
sending the packet contents to the SDN controller. However,
packets matching the existing flow rules in the switches
are generally not forwarded to the controller in a standard
SDN implementation. Hence, a mirroring method is used
for such an IDS to work, in which the copies of all packets
going through the network devices are redirected to specific
servers.
SDN can intelligently route traffic, eliminate bottlenecks,
and optimally use underutilized network resources, thus
simplifying the complexities introduced by IoT devices[173].
The centralized intelligence controller facilitates the distribution of scalable flow rules and deters malicious traffic flows
through its forwarding tables.
In an IoT environment, SDN can rapidly react to malicious
flows and security breaches. It can provide authorized access
to the devices by manipulating the data flows, authentication
of flow rules, and effective network monitoring. An IDS/ IPS
approach for an SDN-IoT framework using three dynamic
architectures is not very effective for Suricata or Snort,
as they operate at level 2 of the OSI model. Detecting them
would require manually creating the OpenFlow rules for
each connected device, and the rules must comply with these
principles for protection against these spoofing attacks: the
devices must send packets with their interface MAC and IP
addresses and respond to the ARP requests with the same
addresses.
Integration of SDN with IDS results in the deployment of
a flexible firewall system and configuring flexible routes in
an organization [174]. IDS servers provide load balancing,
detect anomaly packets, and inform the SDN controller,
which then deploys rules and policies onto the SDN switches
to block the malicious traffic. They can also forward anomaly
packets to honeypots to gain the advantage of further security
analysis.
The SDN switches use port mirroring and copy the traffic
to IDS, delaying its forwarding to the destination. The
IDS sends alert messages such as syslog or SNMP trap
to OpenFlow switches in case of packet matching with
signatures. When the switches receive this alert message
via UDP, the Packet_In message is sent to the controller.
After this, the controller creates a flow entry and sends it
to the switch using the Flow_Mod message. The switch then
updates the flow table and processes the delayed packets. The
summary of all the IDS-based techniques we discussed can be
found in Table 9.
A. LOAD BALANCING TECHNIQUES
Load balancing predicts traffic bottlenecks and efficiently
distributes the load to provide a service that meets QoS
requirements [175]. Conventional methods are round-robin
algorithms and equal-cost multipath routing. Dynamic reduction of the server response time by finding the shortest paths
to reach the destination, such as Dijkstra’s algorithm, which
also focuses on single domain SDN can be utilized. In [175],
discussed other load balancing techniques in SDN, such
as fuzzy logic, rounding algorithm, game theory, or switch
migration, and states that the problem of controller and link
load balancing is NP-hard.
Load balancing and Quality of Transmission (QoT)
aware routing have applications in Wireless Mesh Networks
(WMN). Still, they suffer from traffic bottlenecks due to
an imbalance of traffic load [176], [177]. SDN helps in
the selection of load-balancing routes in QoT following a
technique called load-balancing routing under constraints of
quality of transmission (LBRCQT). They collect QoT and
link traffic load information for the constraints and objective
functions of the routing algorithm. When data transmission
routes require multiple hops, wide-area and dense WMNs
experience lower QoT and delays. The proposed solution
makes some effort to solve the problem.
In certain scenarios, load balancers can operate without
terminating TLS connections, ensuring end-to-end encryption for compliance and security purposes. A common use
case is in cellular networks, where Mobile Load Balancers
(MLBs) manage traffic at Layer 3 or Layer 4 of the
OSI model without decrypting encrypted TLS traffic. This
approach ensures that traffic remains secure while the load
balancer makes routing decisions based on IP addresses or
TCP/UDP connections. Another use case is in cloud-based
environments, where Application Load Balancers (ALBs)
[178] route traffic to backend services while preserving TLS
encryption. This is often used in highly secure environments
where the client-to-server encryption must remain intact,
such as healthcare (HIPAA) or financial institutions, where
regulatory compliance is critical. These load balancers cannot
inspect the content of traffic but rely on metadata, such as IP
addresses, to make routing decisions.
Transport Layer Security (TLS) is essential for ensuring secure communication between the Software-Defined
Networking (SDN) controller and network devices [179].
This encryption protocol protects against eavesdropping and
tampering, safeguarding the confidentiality of information
exchanged. Maintaining a secure communication channel is
vital for the SDN controller to make accurate load-balancing
decisions based on real-time data from different network
components. TLS authenticates both the controller and
network devices, ensuring that only authorized devices can
connect to the network and preventing unauthorized entities
from influencing load-balancing decisions or accessing
sensitive data. TLS guarantees data integrity during transmission, ensuring that load-balancing decisions and traffic
management instructions remain accurate and unaltered.
This security measure is crucial as the controller gathers
performance metrics and traffic statistics to make informed
decisions [180].
The management of security keys and certificates in TLS is
crucial for ensuring confidentiality, integrity, and availability
in secure communications. Key management involves secure
generation, storage, distribution, rotation, and revocation to
prevent unauthorized access. In TLS 1.3, critical keys include
the server’s long-term private key, ephemeral session keys
for Perfect Forward Secrecy (PFS), and session keys used
for encrypting data [181]. Additionally, server, intermediate,
and root certificates must be carefully managed, ensuring
validity and trustworthiness, along with proper revocation
handling through Certificate Revocation Lists (CRLs) or
Online Certificate Status Protocol (OCSP). By establishing
a trusted network environment through TLS, effective load
balancing is facilitated, meeting regulatory requirements for
data security and protection [181]. While TLS enhances
TABLE 9. Intrusion detection system solutions.
security, there may be some overhead due to encryption and
decryption processes. Balancing this overhead with the need
for timely load-balancing decisions is essential for optimal
network performance [182].
Load balancers often act as TLS termination points in
architectures. Load balancers decrypt encrypted traffic from
clients before forwarding it to backend servers. In this way,
load balancers can inspect content for routing purposes and
apply advanced load-balancing algorithms. The load balancer
reduces backend server computational load by handling TLS
decryption and encryption, allowing them to focus on serving
the application. Performance can be greatly improved with
offloading, but security keys and certificates need to be
carefully managed. TLS may be supported by different clients
in different versions. Load balancers must support a range
of TLS versions and cipher suites, ensuring compatibility
and security. It is especially important when migrating to
newer TLS versions or handling traffic from a diverse
client base [183]. Additionally, load balancers help protect
against SSL/TLS-based attacks, including DDoS attacks
that target the TLS handshake process. There are advanced
load balancers that include mechanisms for detecting and
mitigating these attacks, such as rate limiting or using
specialized hardware accelerators [184].
SSL/TLS-based attacks, such as Distributed Denial-ofService (DDoS) attacks, exploit the resource-intensive nature
of the TLS handshake. Attackers can overwhelm servers
by initiating multiple TLS handshakes, consuming server
resources [185]. Mitigating these attacks requires techniques
like rate limiting, where the number of handshake requests
from a single source is limited to reduce load. Specialized
hardware accelerators, such as cryptographic accelerators
or TLS offloaders, can handle encryption and decryption
operations, offloading the burden from the server’s CPU.
These accelerators are designed to manage large volumes of
encrypted traffic efficiently, ensuring that TLS handshakes
and encrypted communications do not become bottlenecks
in the network. Such solutions are particularly useful in
high-traffic environments like data centers or large-scale
cloud deployments, where performance and security are
paramount.
Load balancers communicate with backend servers
through various protocols based on system architecture
and the type of application. Commonly used protocols
include HTTP, HTTPS, TCP, UDP, gRPC, and WebSocket.
The selection of a protocol depends on the specific
requirements for performance and security. For example,
in environments where security is critical, HTTPS is used
to encrypt communication between the load balancer and
backend servers. Conversely, HTTP might be preferred in
a trusted, internal environment to reduce latency. Load
balancers inspect the HTTP headers, payload data, session
identifiers, cookies, and content types to make intelligent
routing decisions. For instance, based on content inspection,
load balancers can perform content-based routing, directing
different types of requests (e.g., media files vs. API requests)
to different backend servers. They may also apply session
affinity to ensure that subsequent requests from the same
user are routed to the same backend server, optimizing
performance and user experience [186].
In TLS 1.3, key management is a crucial aspect of
maintaining secure communication between clients and
servers [179]. Several types of keys are involved:
• Server’s Long-Term Private Key: This is used to
authenticate the server during the handshake.
• Ephemeral Session Keys: Generated through DiffieHellman key exchanges, these are used to ensure
Perfect Forward Secrecy (PFS), meaning that if a
session key is compromised, it does not affect previous
communications.
• Session Resumption Keys: Used to speed up the
handshake process by reusing an existing session
between the client and server.
• Certificates: Certificates verify the identity of the server
and must be carefully managed, including handling
of certificate revocations via Certificate Revocation
Lists (CRLs) or the Online Certificate Status Protocol
(OCSP).
In load-balanced environments, proper key and certificate
management is critical for ensuring secure communication.
Load balancers that terminate TLS connections must support
different versions of TLS and cipher suites to ensure
compatibility with a diverse range of clients. Mismanagement
of keys or certificates can lead to vulnerabilities, potentially
allowing attackers to compromise encrypted traffic [187].
Load balancers employ advanced algorithms to optimize traffic distribution, improving efficiency and ensuring resource utilization. Some commonly used algorithms
include:
• Least Response Time: This algorithm routes traffic
to the server with the lowest response time, reducing
latency for users [188].
• Weighted Round Robin: Servers with higher computational power or network bandwidth are assigned more
traffic compared to less capable servers.
• Geo-Location Based Routing: Users are routed to
the closest available server based on geographical
proximity, reducing network latency [188].
• Adaptive Load Balancing: This technique monitors
traffic and server performance in real-time, dynamically
adjusting load distribution based on network conditions
and backend server health [186].
• Content-Based Routing: Routes traffic based on specific parameters such as URLs, headers, or content types
(e.g., routing video traffic to media-optimized servers).
These algorithms significantly enhance application performance by ensuring that traffic is intelligently managed,
reducing the risk of bottlenecks, and improving user experiences.
1) COMPONENT MIGRATION
A preemptive data plane components migration strategy
for load balancing between distributed SDN controllers
supports the flow networks requiring low latency communications [189]. The idea is to prevent load imbalances and
schedule advance-optimized migrations under delay constraints. Prediction models associated are Auto-Regressive
Integrated Moving Average (ARIMA) and Long Short
Term Memory (LSTM) for controller load forecasting. The
problem is tried to be formulated as an NP-complete, nonlinear binary program with the use of a reinforcement
learning algorithm for its solution. This preemptive machine
learning solution minimizes migration time according to
latency requirements of delay-sensitive applications through
ARIMA (short-term predictions) and LSTM (long-term
predictions). The results are remarkable, with the proposed
algorithm outperforming recent benchmark algorithms. The
Two-Win-Stay-Lose-Shift (2WSLS) algorithm gives better
performance than benchmark algorithms at load balancing
and migration cost reduction.
2) ISMDA
An Improved Switch Migration Decision Algorithm
(ISMDA) for load balancing in SDN is inspired by Dynamic
and Adaptive Load Balancing (DALB) and Controller Adaptation and Migration Decision (CAMD) frameworks [190].
It can optimally manage the migration cost and ensure load
balancing from the set of underloaded controllers, proving
to be an efficient approach over the CAMD framework
with elephant flow incoming traffic load. A non-overloaded
controller is found using variance and mean load status, after
which heavily loaded switches are migrated over it. This is
more efficient than CAMD and DALB, and a topology-aware
switch migration can be implemented in the real world.
3) DOLPHIN
Dynamically Optimized and Load Balanced Path for
Inter-domain communication system (DOLPHIN) distributes
the traffic load evenly across multiple domain links, extending its applications to IoT and 5G vehicular networks [191].
Load balancing can be static or dynamic. In static, the fixed
route allocation takes place before traffic transmission. It has
poor flow scheduling or congestion during a large volume
of flow transmission, as the routes cannot be changed once
fixed. In dynamic, periodic updates are made to overcome
the problem. DOLPHIN is a dynamic approach where path
changes take place on the go, providing vertical extension
into the perception plane and horizontal inter-domain load
balancing.
4) HECSDN
Controllers help process flow signals at a rate of millions
per second in large-scale networks while satisfying the
network application’s QoS [192]. They proposed a multi-tier,
hierarchical edge cloud SDN controller system (HECSDN)
with a flexible mechanism that allows devices to allocate
computational tasks based on traffic loads, resulting in
the development of an efficient load-balancing algorithm
derived from the queuing model. For multiple controllers,
centralized or distributed load balancing can be performed.
In a centralized mechanism, a communication protocol is
implemented in the control plane to achieve a hierarchical
design and bottleneck elimination [193]. In distributed, the
controllers can be made to take load balancing decisions
locally.
5) SBLB
SDN architecture and virtualization provide a global network
view that can provide load-balancing routing and accelerate
data management between network clusters [194]. Integration of SDN and WSN creates a robust SDWSN network
created using fuzzy topology discovery protocol (FTDP).
SDN-based Load Balancing (SBLB) minimizes response
time and maximizes resource utilization while balancing
flow control granularity and communication overhead by the
controller. The mechanism uses a mean number of demands
per controller and links weight as a metric, decreasing the
number of sent messages, energy consumption, and efficient
load balance as compared to LEACH algorithms.
6) OTHER LOAD BALANCING TECHNIQUES
Wild card SDN packet forwarding rules can be used to
implement load balancing, assuming uniform traffic from
TABLE 10. Load balancing techniques.
all IP addresses. The assumption was not very practical,
and hence, a reactive migration of traffic from a heavily
loaded switch to a lightly loaded one was considered. There
are separate, specialized load balancers for web and email
traffic based on the workload and requirements of services.
A Plug-n-Serve (Aster*x) mechanism balances the load over
an arbitrary unstructured network, preventing the front-end
load balancer from becoming the bottleneck. It minimizes the
average response time of web services by controlling HTTP
request paths.
Existing dynamic load balancing solutions under a single
domain select transitory paths for the fresh flows and
divert them during unstable loads; thus, they can uselessly
oscillate between the paths even when the change was not
required. Researchers propose a solution DLPO for single
domain dynamic load balancing where congested path flows
are redirected to lighter paths and switch flow tables are
updated to combat packet loss risks. Another solution is
using a unified NBI and a multi-domain architecture with
a coordinator controller. It addresses the scalability issue
for multiple domains but fails on multiple paths among the
domains. It can also help increase SDN survival time. When
alternate paths are available to reduce the load, it splits the
overloaded paths with alternate routes between the switches.
A rounding-based algorithm reduces the controller’s response
time in SDNs having multiple controllers and optimizes
channel utilization [175]. Traditionally, to reduce response
time, increase throughput, and avoid network overloading,
expensive front-end load balancers were deployed in data
centres to direct clients’ requests to a server replica [21]. The
summary of all the load balancing techniques we discussed
can be found in Table 10.
The main point of attack remains the HSS, authentication
and authorization. These networks use SDN and NFV for
network slicing and demand regular security checks and
updates. These security issues in 5G networks must be
mitigated to secure 6G networks from existing challenges.
Cryptography as a solution has already failed, as it can easily
be exploited with quantum mechanics.
XIII. SDN NEW APPLICATIONS
SDN is revolutionizing various industries through its flexibility and programmable architecture. In Wi-Fi networks,
SDN is enhancing QoS by optimizing handover parameters
for seamless connectivity. It plays a vital role in protecting electrical power grids by enabling dynamic, real-time
management of network data. SDN-enabled WSNs improve
energy efficiency, while its integration with vehicles and
satellites supports advanced communication technologies.
Furthermore, SDN’s synergy with AI and MPTCP optimizes
energy-aware network management. Ongoing standardization efforts in SDN and NFV ensure compatibility and
innovation across networks globally.
A. QOS IN WI-FI NETWORKS
Improving the quality of service (QoS) in software-defined
Wi-Fi networks with high density uses load balancing
that considers various QoS parameters, such as network
congestion, channel interference, and client device type,
to ensure smooth and efficient network performance [195].
This research aims to improve the user experience in highdensity Wi-Fi environments, such as stadiums or public
spaces. It evaluates the proposed solution through simulations
and experiments and shows that it significantly improves
the QoS compared to existing load-balancing methods. The
results demonstrate that the proposed solution can effectively
address the challenges posed by high-density Wi-Fi networks,
such as decreased network efficiency and congestion. It can
enhance the performance of high-density Wi-Fi networks and
provide a better user experience.
B. HANDOVER PARAMETER OPTIMIZATION
Optimizing handover parameters in an SDN-enabled UserCentric Network environment helps improve the performance
of handovers, which are the transitions from one network to
another, by adapting the handover parameters to changing
network conditions [196]. This self-adapting handover optimization approach uses SDN to monitor network conditions
and adjust handover parameters accordingly. Handovers play
a critical role in maintaining connectivity and ensuring
seamless communication in UDN environments. Optimizing handover parameters can improve the performance of
handovers and enhance the user experience in these environments. It can address the challenges of handover optimization
in SDN-enabled UDN environments and provide a solution to
suboptimal handover performance.
C. ELECTRICAL POWER GRID PROTECTION SYSTEM
Improving the reliability and robustness of the protection system in electrical power grids aims to address the challenges
faced by traditional protection systems, such as slow response
time, false alarms, and vulnerability to cyber-attacks [197].
The method enhances the resilience of the pilot protection
system in power systems using data-driven approaches and
advanced algorithms, such as machine learning and artificial
intelligence, to process and analyze real-time power system
data. The performance is evaluated through simulations
and experiments and compared with traditional protection
systems. It can improve the response time and accuracy of the
protection system and enhance its overall resilience against
various types of disturbances and failures. It may prove to be
a promising solution for improving the protection of power
systems and ensuring their reliable and secure operation.
D. MPC ARCHITETURE
A hierarchical control architecture for interfacing renewable
energy sources and motor drives uses a Model Predictive
Control (MPC) based power module that enables the integration of renewable energy sources, such as wind turbines and
solar panels, with motor drives. The proposed architecture
is flexible and scalable and can be adapted to different
renewable energy sources and motor drives [198]. It provides
a robust and efficient interface between renewable energy
sources and motor drives. It can enhance energy systems’
efficiency and sustainability and can be used to improve
the integration of renewable energy sources with motor
drives.
E. SDN-ENABLED WSNS
Network administration and control logically fell to centralized SDN controller nodes. Protecting entity communication on WSNs with SDN is possible thanks to the
Lightweight Authentication and Key Agreement Protocol
(LAKP). By doing both informal and formal security
investigations utilizing the Scyther tool and Burrows-AbadiNeedham (BAN) logic, LAKP prevents known security
issues. 768 bits are used for communication, and there are
4 messages in total. The cost of computation is 20Th +
10Te/d ≈ 5.331 [199].
F. SDN-ENABLED VEHICLE AND SATELLITE TECHNOLOGY
To address the challenges of ensuring secure and reliable
communication in SDN-enabled vehicles subjected to high
mobility and varying network conditions, a secure timesensitive SDN architecture integrates time synchronization
and secure communication mechanisms to ensure the timely
and secure delivery of messages in SDN-enabled vehicles [200]. The results show that it can provide secure and
reliable communication in SDN-enabled vehicles, even under
challenging network conditions.
Research in software-defined satellite networks (SDSN)
thoroughly examines various challenges and opportunities in
SDSN, including network design and management, resource
allocation, and security [201]. The role of SDN in improving
satellite network performance and efficiency, as well as its
ability to support new and innovative services, are discussed,
as is SDSN integration with other emerging technologies such
as AI and ML. It provides a valuable resource for researchers,
engineers, and practitioners in satellite communication and
networking.
V2X (Vehicle-to-Everything) communication technology
in the field of transportation is an application-centric network
management approach to improve the safety and real-time
performance of V2X applications [202]. The current network
management practices are inadequate in addressing the
unique requirements of V2X applications, such as real-time
communication and safety-critical data exchange. SDN centralized controllers can manage the V2X network, prioritize
traffic based on application needs, and ensure the reliability
and security of the communication. An application-centric
network management approach is essential for realizing the
full potential of V2X technology in improving transportation
safety and efficiency.
A new DL model for monitoring drivers in autonomous
vehicles connected to an SDN using 5G technologies
improves the safety and efficiency of autonomous vehicles
by detecting drivers’ drowsiness and distraction levels in realtime [203]. DL techniques can analyze various physiological
signals, including facial expressions, eye movements, and
heart rate, through monitoring drivers and detecting drowsiness and distraction levels. The model is evaluated using a
dataset of drivers. Thus it outperforms existing methods in
terms of accuracy and efficiency in effectively monitoring
drivers and detecting drowsiness and distraction levels in realtime.
G. ENERGY AWARE NETWORK MANAGEMENT
Energy-aware routing in SDN-enabled data center networks
using a new routing algorithm considers both network
performance and energy efficiency [204]. The algorithm is
based on a novel metric that combines both performance
and energy efficiency and uses this metric to make dynamic
routing decisions in real-time. It can effectively balance the
trade-off between performance and energy efficiency and
lead to significant energy savings in SDN-enabled data center
networks.
The traffic matrix in SDN is a crucial input for network
management and optimization in SDN, and accurate estimation of the traffic matrix can significantly enhance the
performance of SDN networks [205]. Different measurement
and model-based techniques can be used to estimate the
traffic matrix in SDN. The challenges and limitations of
each technique are discussed to provide insights into the
selection of an appropriate technique for a given SDN
network. No single technique is ideal for all SDN networks,
and the choice of a traffic matrix estimation technique should
be based on the specific requirements and constraints of the
network.
Detecting ARP spoofing attacks in fat-tree topology
networks can use SDN by leveraging its centralized control
and programmability [10], [11], [206], [207], [208]. The
method is tested in a fat tree network and compared
to existing solutions, demonstrating its effectiveness and
efficiency in detecting ARP spoofing attacks. It outperforms
the existing solutions in terms of accuracy and speed of
detection.
SQBRP is a new switch quality-based routing protocol
for SDN that considers switch-level performance metrics in
routing decisions [209]. The protocol dynamically adjusts
routes based on the quality of switches to ensure efficient
and reliable network communication. It outperforms existing
SDN routing protocols in terms of network performance and
stability, and it could be a useful addition to the SDN routing
protocol ecosystem.
H. AI AND MPTCP
Artificial Intelligence (AI) in Software-Defined Wide Area
Networks (SD-WANs) along with Reinforcement Learning
(RL) can dynamically adjust network routes and policies
in SD-WANs to improve network performance [210]. The
approach is evaluated through simulations and compared to
traditional SD-WAN approaches. The application of RL in
SD-WANs can significantly enhance network performance
and reliability, and provide new opportunities for future
research in this area.
An SDN coordinated steering framework, Multipath
TCP protocol (MPTCP) for multipath big data transfer
applications uses a novel OpenFlow-Stats routing algorithm
in cost-effective OpenFlow networks [211]. The switch
port statistics are used to select transmission paths and
apply the topology pruning technique, implemented over the
Mininet emulator and ONOS controller. A Simple Multipath
OpenFlow controller, SMOC, was previously considered for
finding transmission paths in an MPTCP connection, but it
ignores the traffic distribution issue. Other controllers under
consideration were Multiflow, Heuristic Algorithm, SFO,
GCLR, and S-MPTCP. The data transmission takes place
in phases of data request and the actual transmission. First,
a data client generates a request message with metadata
and sends it to the data server through SDN. Then, the
associated switch for that client sends Packet-In to the
controller, which makes a routing decision. Upon receiving
the request, the main server assigns and notifies a sub-server
and the data client, after which, for connection establishment
for the data transfer, there is a negotiation between the
sub-server and the data client. The controller helps in the
detection and management of all incoming MPTCP traffic,
and together with the Multipath Transmission Manager,
Topology Manager, and OpenFlow Stats Analyzer, it delivers
the highest throughput with lesser complexity. MPTCP uses
multiple subflows for data transfer and increases the network
throughput, performance, and resilience to failure. It achieves
scalability and a 90% reduction in the data transfer time as
compared to traditional routing with disjoint paths. There is
35% more speed and 57% less overhead than the methods
proposed earlier.
I. OPEN STANDARDIZATIONS OF SDN AND NFV WITH
THEIR ACTIVITIES
Standards serve as the guiding force behind research,
development, innovation, policy establishment, and industry
practices. They regulate the execution of productive tasks and
the implementation of products while ensuring quality. Additionally, standards ensure interoperability among research
techniques or products. Various Standards Development
Organizations (SDOs) work towards proposing standards
within different verticals, including Software-Defined Networking (SDN) and Network Functions Virtualization (NFV)
as shown in Table 11. For this reason, standardization
initiatives must be coordinated by industry, academia, and
SDOs to promote interoperability [212].
In the near future, there may be a trend toward creating
standards that are specifically customized to the unique
architecture and operating models of Software-Defined
Networks (SDNs). This entails developing protocols and
frameworks to address the dynamic nature of SDN settings, as well as their inherent vulnerability to Denial of
Service (DoS) assaults. Standardization initiatives could
focus on developing recommendations for safeguarding
SDN controllers to ensure their resilience to attacks. Given
the ever-changing nature of Distributed Denial of Service
(DDoS) attacks, standards produced by organizations like
the Internet Engineering Task Force (IETF) must anticipate
future threats and include mechanisms for rapid updates or
fixes to SDN systems. As a result, standardization initiatives
may include incorporating artificial intelligence (AI) and
machine learning techniques into SDN security frameworks,
as well as developing standards for these technologies in
order to improve threat detection and response capabilities.
While standards are critical for guaranteeing security and
interoperability, they should not stifle innovation in the SDN
sector. Furthermore, network operators, equipment vendors,
and academics should work together to define common rules
for DDoS mitigation in SDNs, such as signaling protocols for
real-time DDoS detection and response across different SDN
implementations.
TABLE 11. Standardizations for SDN, NFV and their activities.
XIV. CONCLUSION AND FUTURE RESEARCH
We have analyzed the different approaches for detecting and
mitigating DoS/DDoS attacks in SDN technology. We have
provided an overview of the fundamental principles and
components of SDN architecture, including its workings and
applications. We have also discussed the role of SDN in load
balancing, IoT, blockchain, and intrusion detection strategies.
Additionally, we evaluated different solutions for addressing
DoS/DDoS attacks in SDN, including table entry, scheduling,
architecture, ML, statistics and entropy, network-based, and
hybrid. Based on their efficiency, service to legitimate users,
delay, and other relevant factors, we have analyzed the
solutions’ advantages, applications, drawbacks, and future
directions. Our analysis will help future researchers better
understand SDN technology, its operation, possible security
issues, and various solutions for mitigating them, and take
SDN technology to new heights. As SDN continues to grow
and evolve, it is important to remain vigilant and proactive in
addressing threats and ensuring the security and resilience of
these networks. The limitless potential of SDN across various
applications and industries highlights the significance of the
topic and the need for continued focus on this area of study.
This article underscores the importance of maintaining a
forward-looking approach in developing secure and effective
solutions for SDN against DoS/DDoS attacks. We hope this
article will inspire future researchers to devise new solutions
and continue advancing the SDN security field.
We have thoroughly analyzed prominent literature from
popular research libraries like Elsevier, IEEE, ACM,
Springer, etc. Based on that, we come across the following
future research directions for SDN:
• Evaluation, testing, and optimization of existing solutions to improve attack detection accuracy and security.
• Finding lightweight, cheap, effective, and fast solutions.
• Standardization of methodologies and consistent and
diverse datasets to form advanced self-healing networks.
• Data plane programming, scalability enhancement, platform independence, user-driven control, and intelligent
network management.
• Exploring programming language theory, formal methods, and distributed systems.
• Developing SDN-based solutions for DoS/DDoS attacks
in cloud, IoT, and ISP networks.
• Investigating new approaches to reduce the time for
identifying DDoS attacks in distributed SDN controller
architecture with COTS switches.
• Future research in the field should pay close attention to
the following aspects: dynamic threshold features, multiple packet header-based detection techniques, selecting
appropriate packet features, and deploying the detection
approach at a separate location other than the controller.
• Robustness in the case of sink failure. Design modifications of SBI to manage heterogeneous devices through
centralized control and intent-based interfaces, defining
CP and Open Flow-specific demands.
• Security issues and information leaks among blockchain
applications.
• Using better classification algorithms and training
datasets.
• Research on load balancing techniques for green optimization of data centers.
• Compare the scalability of these architectures with more
OpenvSwitch bridges and creating multiple clusters of
the SDN controller using multiple attackers to reach the
limit of the IDS/IPS and collapsing the bandwidth to
confirm the results obtained.
Among these directions, the key future research direction
for SDN is the development of SDN-based solutions to
mitigate DoS/DDoS attacks, particularly in cloud, IoT, and
ISP networks, where security continues to be a major concern.