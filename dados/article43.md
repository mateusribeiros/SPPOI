Title: A Review of Intelligent Configuration and Its Security for Complex Networks

Abstract — Complex networks are becoming more complex because of the use of many components with diverse
technologies. In fact, manual configuration that makes each component interoperable has breed latent danger to system security. There is still no comprehensive review of these studies and prospects for further research. According to
the complexity of component configuration and difficulty of security assurance in typical complex networks, this paper systematically reviews the abstract models and formal analysis methods required for intelligent configuration of
complex networks, specifically analyzes, and compares the current key technologies such as configuration semantic
awareness, automatic generation of security configuration, dynamic deployment, and verification evaluation. These
technologies can effectively improve the security of complex networks intelligent configuration and reduce the complexity of operation and maintenance. This paper also summarizes the mainstream construction methods of complex
networks configuration and its security test environment and detection index system, which lays a theoretical foundation for the formation of the comprehensive effectiveness verification capability of configuration security. The whole
lifecycle management system of configuration security process proposed in this paper provides an important technical
reference for reducing the complexity of network operation and maintenance and improving network security.
Keywords — Complex networks, Intelligent configuration, Configuration security, Software defined network,
Lifecycle management.
Citation — Yue ZHAO, Bin YANG, Fei TENG, et al., “A Review of Intelligent Configuration and Its Security
for Complex Networks,” Chinese Journal of Electronics, vol. 33, no. 4, pp. 920–947, 2024. doi: 10.23919/cje.2023.00.001.
I. Introduction
Complex network is a common network architecture of distributed artificial intelligence (AI) systems. It
is composed of many network nodes with autonomous
learning and processing functions. The computing resources and communication resources of each network
node are different. The AI systems need to make full use
of distributed node resources to calculate massive data,
and flexibly expand and dynamically configure node resources according to the tasks performed.
Complex networks are faced with a series of new
problems. On the one hand, the current network scale
construction is increasingly complex, and the types and
quantities of device and components are also increasing,
which brings great pressure to the development of network operation and maintenance (O&M), making intelligent network configuration a new O&M demand [1]. On
the other hand, with the development of network security technology, the network threat attacks have also been
greatly developed, mainly manifested in the endless
emergence of attack methods and the complexity and variety of attack means. It is urgent to ensure the security
of intelligent network configuration and reduce configuration vulnerabilities and network attack paths [2].
In addition to providing support to intelligent configuration and fast response, configuration security also
plays a very important role in the secure operation of
complex networks [3]. At present, the network management plane still relies on the original manual configuration management [1]–[3]. According to the statistics of
Gartner, a technical consulting company, 80% of the network configuration work is still completed through manual changes based on command-line interface (CLI). The
improper configuration has become a major hidden danger to network security. According to the data provided
by DARPA in 2018 [4], 61% of the operation failures in
the networked control power grids in the United States
are caused by improper configuration. In addition, 67%
of security vulnerabilities in general Internet technology
systems are related to improper configuration. The statistics of similar systems published in China are similar.
For example, Alibaba made a statistical analysis of network failures [5], and found that 65% of network accidents and security vulnerabilities were caused by improper configuration, including 10% of initial configuration
errors and 56% of configuration update errors. So far, a
lot of research work has been devoted to the intelligent
transformation of network configuration. We believe that
the research on intelligent configuration and its security
also faces the following new technical challenges.
1. The abstract of complex network configuration
and the theoretical model that can effectively
describe the configuration requirements
At present, although there are only a few tools help
achieve intelligent network configuration in some aspects,
a comprehensive intelligent configuration is still waited
to achieve. Taking the famous scholars Douglas E. Comer
and Wu Jianping as representatives [6]–[8], it is believed
that the root cause is the lack of scientific abstraction
and theoretical modeling of network configuration. The
traditional network configuration is equivalent to the
network administrator directly using machine language
to complete the development of high-level applications,
which lacks multiple levels of abstraction. Abstraction
can effectively hide the details of different manufacturers, different devices, different software versions, and different CLI commands, and clarify the constraints between the configuration parameters of different components. It is a prerequisite for intelligent configuration.
For each specific target of intelligent configuration, there
should be corresponding configuration parameter abstraction, configuration rule abstraction, or configuration task
abstraction to help the machine recognize configuration
semantics. As Douglas E. Comer asserts, it is impossible
to realize a comprehensive and automatic configuration
system until an appropriate configuration abstract model is developed [7]. This view has also been widely recognized [9]–[11], so it is a difficulty to break through in the
theoretical research of intelligent configuration security.
2. An in-depth analysis of the completeness of
complex network configuration
Network configuration has a complex process. Even
after the initial configuration is completed, the configuration needs to be updated frequently with the changes of
network environment and bearer services. However, the
existing research and development work is often only
aimed at a certain link in the network configuration. For
example, Propane focuses on the automatic generation
of high-level intentions to device configurations; Ansible
focuses on realizing automatic network deployment and
task scheduling; Batfish focuses on network configuration verification; Napalm focuses on the abstraction of
network management and configuration operations and
providing a unified application programming interface
(API) to shield the differences between multiple manufacturers [5], [7]. Obviously, the existing solutions lack
the whole lifecycle management of network configuration and the closed loop of intelligent configuration. The
completeness of configuration management, however, is
critical to the security of complex networks [12]. According to the secure bucket principle, network security always
depends on the weakest link of the network, and the
place where each link connects often becomes the blind
spot of network security [13]–[15]. Hence, the closed-loop
automation of network configuration security must be
realized in a unified, coordinated, and seamless manner.
3. Building a unified configuration management
platform
In addition to the above process-oriented O&M
chimneys, i.e., O&M islands, there are also regional, hierarchical, and functional O&M chimneys. Complexity often
spans multiple regions, different management levels, and
different functional domains, let alone information processing, storage, networks, and even networks of different scales. [16], [17]. They often conduct configuration
management independently, thus forming O&M islands,
which makes the configuration change cycle uncontrollable, new businesses take a long time to be online, and
cross domain network configuration failures cannot be
quickly repaired [18], [19]. The introduction of software
defined network (SDN) only realizes the logical and unified configuration management in each domain [20].
Cross domain network configuration involves the consistency between distributed controllers, and there is no
ready-made solution [21]–[23]. The unified configuration
platform can centralize configuration errors. Modifying
an error means that the error will be fixed forever. The
unified configuration platform is easier to ensure consistency, and can perform repeated configuration operations
repeatedly and consistently. In addition, the platform
can display its own indicators through more and more
visual means to help network administrators find details
in the process and measure these details and indicators
in the process [24], [25].
4. Improving the universality of network
configuration methods
An ideal network intelligent configuration scheme
should be able to handle various types of components and
various levels of information services in a unified way.
However, the current intelligent configuration and verification methods are not universal. For example, for physical components, there are relatively mature configuration
methods due to fewer configurable parameters, but for
virtual components with higher flexibility, these methods
are not applicable. For components without status, only
static analysis methods are needed to verify the configuration, but these methods cannot handle components
with their own status. Even because components from
different manufacturers are based on different abstract
methods [26]–[28], it is hard for network administrators
to find unified API. The operating environment and mission of complex networks are constantly changing, so the
ideal configuration platform should be designed to adapt
to emerging hardware and software technologies. However, the poor universality of the configuration method
will seriously affect the adaptability of intelligent configuration, and introduce security risks.
5. Providing an effective verification environment
and testing methods for network configuration
security
It is theoretically impossible to fully guarantee the
configuration security of distributed networks [29]. Even
if the network has passed the formal verification, because the verification is based on an abstract model, it
cannot detect the bug in the software implementation
and hardware firmware, nor can it anticipate the unexpected accidents in the configuration execution. Therefore, it is necessary to build a configuration security test
environment, develop test evaluation technology, and
comprehensively test and evaluate the proposed security
configuration methods in practice. Taking the Configuration Security (ConSec) project of DARPA as an example, in order to ensure that the complex network achieves
the expected effect, nearly 2/3 of the project implementation cycle is spent on network testing and verification
[4], which also reflects the necessity of the verification
environment and testing methods and the lack of capacity at this stage.
Many efforts have been made on overview, comparison, and summarization for the network configuration by
research and industrial communities. In [30], Tao et al.
presented the algorithm-based configuration for AI systems. Experiments had verified that intelligent configuration can reduce the O&M costs of complex networks and
improve robustness and reusability. In [31], Dharmapriya
et al. provided the review of network configuration literatures under the two categories, drivers of complex network configuration decisions, and the key parameters
considered in network configuration. In [32], Sayagh et al.
found how network configuration engineering comprises 9
activities, and is impacted by 22 open challenges. Then,
they discussed 24 recommendations to overcome or avoid
the challenges, which were derived from practitioners’ experience and academic literature. In [33], Schede et al.
described the automated algorithm configuration problem and features of configuration methods, respectively.
They outlined relevant design choices of configuration
approaches, contrast methods, and problem variants
against each other, and described the state of algorithm
configuration for complex networks. Most existing surveys only focus on the selection and configuration of algorithms used in complex networks, rather than the lifecycle management of network configuration generation,
verification, and deployment. Perhaps more importantly,
the shortcomings of the existing surveys are that the
technologies introduced in some surveys are slightly outdated, and AI technologies are not used in network configuration. In addition, some surveys do not fully consider the problem that improper network configuration will
lead to network security risks.
Compared with the existing surveys, this paper
deeply discusses the abstract model and formal analysis
method required by network intelligent configuration and
its security. Moreover, this paper also describes key technologies such as configuration semantic awareness, automatic configuration generation, dynamic deployment,
and verification evaluation in detail. To our knowledge,
this is the first systematical review about the security
problems faced by intelligent configuration and effective
solutions.
The remainder of this paper is organized as follows:
Section II introduces the related work on intelligent configuration. Section III presents the research system of intelligent configuration security. Section IV gives an
overview of theoretical approaches of intelligent configuration security. Section V comprehensively reviews key
technologies of intelligent configuration security. Section
VI describes the system integration and verification of
intelligent configuration security. Finally, future research
direction and conclusion are summarized in Sections VII
and VIII, respectively.
II. Related Work on Intelligent
Configuration and Its Security
The section first introduces the background on automatic configuration and complex networks, then discusses
the relevance and difference between automatic configuration and intelligent configuration, and then summarizes
the current research status around the generation, correctness, and security verification, as well as the deployment and implementation of intelligent configuration
for complex networks.
1. The background on automatic configuration
and complex networks
Manual configuration seriously affects network agility and the ability to support key services [2], [3]. Moreover, manual configuration process is prone to errors,
and improper configuration will lead to serious network
operation failures and security vulnerabilities, which are
mainly caused by the following three aspects.
The first is the spatial complexity of network config-
uration. The manual configuration can only interact with
a single network component each time, and complete the
configuration of network components one by one. The
correctness of configuration of each component depends
on configuration of other components and the overall behavior characteristics of the network formed by these
configurations, which requires the network administrator
to establish a mapping relationship between the configuration parameters of a single component and the overall
behavior of the network to correctly infer the impact of a
change in a configuration parameter on the entire network. That is a very hard mission [34].
The second is the time complexity of network configuration. When manually configuring network component parameters, the time dimension should also be considered. The consequences of each parameter setting cannot be completely determined now, but also consider the
changes in network behavior over time under new external conditions, business requirements, and network status. Considering the time factor, even different component configuration order may lead to different network
behaviors, thus affecting the correctness of configuration.
The complex inference behind this is a long job even for
well-trained and knowledgeable network administrators
[35], [36].
The third is the diversity of network components,
operating environments and carrying services confront
the network configuration. The network will contain a
variety of physical/virtual components, and the components need to be configured with a variety of parameters,
so various protocols and services need to be configured.
What is more, the choice of all these configurations needs
to consider the diversified operating environment and requirements of carrying services. It is almost impossible
for network administrators to master so many details and
correctly configure thousands of network parameters [34].
Automatic configuration means that the network administrator establishes a mapping relationship between
the configuration parameter settings and the network
status information as network configuration policies. The
complex network preprocesses the collected network status information to form formatted data, and automatically performs corresponding configuration operations according to the policies formulated by the network administrator. The network configuration that can be generated by automatic configuration is often the one already in
the prior knowledge. For complex networks, the abovementioned configuration security issues will become more
prominent because of two main reasons.
First, since the special components constituting the
complex network are replaced by general components,
more potential configuration security vulnerabilities have
been created. In order to reduce the construction cost of
complex networks, customized and single purpose special components used in complex networks are being replaced by commercial off-the-shelf (COTS) device with
low price and excellent performance. This also means
that these common components must be properly configured to shield some unnecessary states or functions before they can be securely used in complex networks.
Second, the dynamicity of complex networks under
strong confrontation conditions increases the difficulty of
configuration security. Network configuration updates
often cause network outages or security vulnerabilities.
Therefore, for general information systems, network administrators will try their best to avoid configuration updates or only do incremental updates without modifying
existing network configurations [37]. Complex networks
are varied, and frequent updates of network configuration
will become an inevitable norm. If manual configuration
is still relied on, the probability of errors will be greatly
increased, and the harm caused will be more serious.
2. Automatic configuration and intelligent
configuration
Intelligent configuration is to take the existing complex network configuration scheme as prior knowledge
through natural language processing, and analyze and
model it through classic AI technologies until the configuration system can intelligently understand the operating environment and mission of complex networks, and
automatically propose a configuration scheme that meets
the requirements of mission tasks according to the prior
knowledge. The security of the network configuration
is independently verified before configuration through
formal methods or simulation methods. It can fully and
automatically respond to the changes of the task and
network during the task execution process and conduct
dynamic configuration, and conduct closed-loop security
evaluation and monitoring of the overall network configuration. The network configuration that can be generated
by intelligent configuration may be one that is not available in prior knowledge.
Automatic configuration is the premise and foundation for intelligent configuration, and intelligent configuration is the development direction of complex network
configuration. Compared with automatic configuration,
intelligent configuration is more difficult to study, and
there are few references available at present. The intelligent configuration technologies of complex network summarized in this paper mainly refer to automatic configuration and intelligent configuration technology based on
classic AI. This paper does not discuss the network configuration based on deep learning much, because the existing research shows that the new AI technology represented by deep learning is not suitable for the configuration of complex networks [38], [39]. The experimental
analysis given in relevant literature shows that the classical AI is better than deep learning in the case of small
data sets, multiple configuration parameters, and changing design models. This fact also shows that it is advisable to use classic AI technologies such as semantic
awareness, expert system, and knowledge reasoning for
intelligent configuration of complex networks.
The purpose of intelligent network configuration is,
on the one hand, to reduce human operation, as well as
network support and maintenance, on the other hand, to
prevent security risks caused by improper configuration.
Therefore, security is of great significance for the whole
lifecycle management of network configuration. Specifically, the automatic generation and formal verification of
network configuration are used to ensure the security of
network configuration, so that the generated configuration scheme can effectively resist network attacks. The
dynamic deployment and implementation of network
configuration is used to ensure that once a security problem is found in the process of network configuration, it
can be diagnosed and automatically recovered through
rapid rollback. The telemetry and monitoring of network
configuration is used to collect the network security status information in real time. Once the network security
is abnormal or the network performance is degraded, the
configuration update will be started.
3. Research status of network configuration
generation
The network configuration generation is to automatically realize the mapping relationship from the high-level
management and business intention to the configuration
of each specific component of the network under the constraints of the specific network operation environment [14],
[15]. The difficulty of automatic configuration generation
is to calculate the corresponding relationship between abstract configuration behavior and specific configuration
operations of components, and objectively reflect the related dependencies of configurations among different
components [40], [41]. The current network configuration
automatic generation methods are mainly divided into
two types, i.e., task encapsulation-based methods and
model-based search methods. The ideal automatic configuration generation method should be simple, efficient,
and scalable. However, the two types of configuration automatic generation methods known at present do not
have all these characteristics at the same time [42], [43].
1) Task encapsulation method
The essence of the task encapsulation method is to
encapsulate configuration tasks into configuration templates. The network administrator inputs high-level configuration policies and triggers variables in the configuration templates to generate corresponding specific configuration schemes. The configuration template contains not
only the configuration commands required to implement
a function of a component, but also the basic control
logic structures such as iteration and condition. Network
administrators can combine configuration templates to
complete complex configuration tasks.
The method based on task encapsulation requires
network administrators to manually build new configuration templates for new or improved configuration tasks.
In addition, when components are replaced or the network is upgraded, the configuration commands encapsulated in the configuration template also need to be redesigned. Therefore, the automation level, flexibility, and
scalability of this method are poor. The method based on
task encapsulation is generally applicable to the basic
configuration of the network, because these configurations
are relatively mature in technology, have few changes in
requirements, and are easy to encapsulate [44].
2) Model search method
Complex networks have specific requirements for
connectivity, security, performance, and fault recovery of
end-to-end information services [45]–[47]. There is a big
gap among these high-level requirements and the related
components of the network and the specific configuration parameters of the components. There is a large
space for change, which is not covered by a few configuration templates. For the policy and dependency-based
configuration behavior that is not supported by the configuration template, a configuration generation method
with a higher level of automation needs to be used [48].
The model search method is a real automatic configuration generation method [49], [50]. First of all, the network configuration objects and the requirements for realizing network configuration functions are described abstractly. Then, through the analysis of the description
language, the description is replaced with Boolean logic
expressions to find the solution that satisfies all Boolean
logic expressions as true. The set of solutions will be regarded as the model that satisfies the configuration task,
i.e., a feasible configuration scheme.
The difficulty of implementing the model search
method is how to effectively describe the requirements.
Since the requirements involve many aspects, such as
connectivity, reliability, and security, the requirements
description should first cover all aspects, in addition, the
requirements description should be as concise as possible.
In addition, appropriate description language and solution method should be selected. Therefore, it is still
difficult to implement the model-based search method.
The model-based search method also needs to describe
new requirements for new or improved configuration
tasks, and then seek new configuration schemes through
reasoning and calculation. With many abstract requirements descriptions that can be reused, this method, in
terms of scalability, is better than the task encapsulation method [51], [52].
4. Research status of network configuration
verification
Because small changes in network configuration may
cause the whole network to be abnormal or interrupted,
it is necessary to verify the correctness of the configuration scheme [27], [28]. Due to the diversity of complex
network configuration commands, it is inevitable that
some unexpected configuration states can be exploited by
attackers, resulting in security vulnerabilities, and becoming hidden dangers of network operation [53]. Hence,
it is also necessary to verify the security of the configur-
ation scheme. According to different configuration verification scenarios, it can be divided into simulation verification, actual verification, and theoretical verification.
1) Simulation verification method of network
configuration
Simulation verification refers to the verification of
the generated configuration operations in a virtual or experimental system environment after the configuration
scheme is generated. If the configuration scheme is correct
and secure, then configure the actual running network.
Simulation verification can also be divided into three
levels: simulation verification, emulator verification, and
physical experiment network verification [54].
2) Actual verification method of network configuration
Actual verification means that when the configuration has been run in the actual network environment, the
configuration can be verified by observing the network
operation status or analyzing the data in the control
plane and data plane. If a configuration error is found,
the configuration of the device can be quickly restored to
the latest valid state, i.e., configuration rollback. The actual verification can also be divided into three categories
as follows [28].
i) Observe the network operation. The configuration
effect of components can be observed through the key
performance index of transmission link, including transmission rate, utilization, throughput, delay, packet loss
rate, and so on. If an anomaly is found, the configuration
file of the component can be restored to the latest valid
state. Of course, network anomalies are not necessarily
caused by configuration errors, such as link physical failures, so this observation method is generally applicable to
the case where new configurations have just been issued.
If the expected effect is not achieved or anomalies occur,
it can be considered as improper configuration. However,
in other cases, the observed network anomaly requires indepth analysis of its causes.
ii) Observe the configuration data of the control
plane. The configuration files of components can be
backed up periodically, and the configuration data can
be extracted for configuration consistency verification.
The configuration consistency verification can not only
find the recently issued configuration errors, but also verify the possible errors in the historical configuration. This
verification process is like the automatic configuration
research based on the model search.
iii) Control data of observation data plane. The control data in the data plane mainly refers to the data in
the route forwarding table. This verification method cannot directly reflect the configuration errors, but it can
infer some errors in the network, such as routing loops
and packet loss. The network administrator can locate
some configuration errors based on these feedbacks. In
network research, invariants are generally used to represent the correct conditions of network forwarding behavior. Violation of these conditions usually indicates that
problems exit in the network. The data of the route forwarding table collected by the data plane can be used to
verify whether the invariants are broken.
At present, the method of configuring the system to
obtain the above three kinds of data is mainly based on
SDN telemetry technology [55], [56]. Telemetry technology is the basis of network research such as configuration
status monitoring, performance management, and security defense. The separation of data plane and control
plane inspired the design and implementation of a universal and flexible measurement architecture. The standardized programming interface enables the rapid development and deployment of measurement tasks. The
centralized network control can optimize the hardware
configuration and forwarding strategy of the data plane
in real time based on the feedback measurement results.
The processing mechanism of the data plane based on
flow table rules supports more refined measurement of
traffic. However, the resource overhead caused by the additional measurement mechanism deployed in SDN measurement conflicts with the limited computing resources,
storage resources, and bandwidth resources in the network. The centralized control plane also has certain performance bottlenecks, which are the main problems and
challenges faced by telemetry technology [19].
3) Theoretical verification method of network
configuration
The theoretical verification method is based on
strict mathematical expressions and models to verify the
correctness and security of the automatically generated
network configuration [57]–[59]. For automatic generation of configuration based on task encapsulation, network administrators need to check the error of the constructed template with their rich domain knowledge and
some automated software analysis tools. This is not only
a high requirement for administrators, but also there is
possibility of errors [60]. For automatic generation of
configuration based on model search, iterative requirements verification can be performed. First, we need to
fully consider the problems that may occur during the
operation of the network, then, convert the problems
into requirements and describe them, and conduct ruleanalysis on both these requirements and the requirements that have already obtained configuration scheme.
If a feasible configuration scheme can be found, it means
that the previous requirement description has defects and
needs to be modified to avoid unexpected problems. This
method needs to fully consider various problems that
may exist in the network operation process, which in fact
is difficult [61]–[64].
The current formal verification method is still in the
academic research stage [65], [66], mainly because the
computational complexity of verification is too large, and
it is only applicable to the static analysis of stateless
components. For network elements with their own state,
such as firewalls and intrusion detection system (IDS), it
cannot be effectively verified [57], so it is not practical.
5. Research status of network configuration
deployment and implementation
The network configuration deployment and implementation are to automatically send the verified configuration scheme to specific components, and automatically
complete the component configuration task. The current
mainstream implementation methods are mainly divided
into two types, i.e., the methods based on script encapsulation and the method based on network protocols, such
as network configuration protocol (NETCONF) [5], [67].
In addition, there is a dynamic configuration method
based on SDN [18], [23].
1) Automatic configuration method based on script
encapsulation
The method based on script encapsulation is to encapsulate the configuration commands recognized by the
device into the script, such as CLI and simple network
management protocol (SNMP) commands, and then directly distribute the configuration scheme to specific
components with the help of tools that can directly interact with components, such as expect. The configuration
template can be constructed in the form of a script, and
combined with tools such as expect, the batch configuration of multiple devices can be realized. Most of the
automatic configuration generation methods based on
task encapsulation combine script encapsulation to build
automatic configuration systems, where a task is encapsulated into a script. The configuration information generated by the automatic configuration generation method
based on model search is still an abstract description.
It is necessary to build general processors, convert the
abstract configuration information into specific configuration commands, and then build corresponding configuration scripts [9], [37].
In terms of execution efficiency, the script encapsulation method can configure components if the script is
directly run on the network management servers. In addition, the multithreading mechanism can be used to
configure multiple devices at the same time to improve
the execution efficiency. Scripts are closely related to
templates, so the automatic configuration implementation method of script encapsulation is suitable to be
combined with the automatic configuration generation
method based on task encapsulation. For some simple
batch configuration tasks, the combination of the two is
practical and efficient. However, the script encapsulation
method has poor scalability, because the core of this
method is to build a script for each configuration function. When the device model, manufacturer, and operating system version are different, the configuration commands may be different, so the configuration scripts for
the same function are different.
2) Automatic configuration method based on network
configuration protocol
Aiming at solving problems in configuration management, the IETF (Internet Engineering Task Force)
Working Group established the Network Configuration
Protocol (NETCONF) [68]. Since NETCONF does not
involve data modeling, in order to fill the gap between
high-level network strategy and low-level network configuration data, the IETF Working Group has proposed a
standard data modeling language YANG for NETCONF.
YANG language not only supports powerful syntax and
semantic verification rules, but also is simple and easy to
understand. It can model the data structure, data relationship, and constraint integrity of configuration information [10].
The NETCONF adopts the C/S architecture, uses
XML to describe the configuration data, uses remote procedure call (RPC) model for communication coding [69],
and uses YANG language to model the underlying configuration data, so that the configuration management
system can interact with physical devices through agents
to perform various basic configuration operations, such
as adding, deleting, modifying, querying, and storing
configuration data.
The method based on NETCONF has good scalability. The core of this method is to interact with devices
through agents. A series of configuration models can be
built based on YANG language. One model realizes the
configuration of one function. This configuration model
hides the details of configuration commands. Therefore,
the configuration model can be reused for devices of different models, manufacturers, and operating system versions [70]. In addition, configuration models can also be
combined and some control logic can be added to meet
the requirements of complex configuration functions [71].
3) Dynamic configuration deployment & implementation
of software definition networks
The centralized control of SDN also brings new
problems. The first is the consistency of network control
logic and forwarding logic. Although in SDN, it is the
control plane that grasps the global network information,
parses the high-level control plane logic description into
the low-level data plane forwarding behavior, and uniformly configures the data plane, which can theoretically
ensure the consistency of the network configuration
scheme [72]. However, there is also a certain hidden danger that the data plane may not completely follow the
rules issued by the controller to perform the correct behavior. When multiple SDN applications deployed in the
control plane are executed concurrently, the distributed
flow table rules may have potential logic conflicts, or
when some errors occur in the controller and the switch,
the forwarding logic of the control plane may be inconsistent with the actual behavior of the data plane, and the
controller itself cannot actively perceive this exception.
The second is about the consistency in the configuration
update process. There is configuration update delay from
the controller to the switch, and the update delay time
to different switches is also different. This may cause
some switches on the forwarding path to have new rules
while others use old rules during the configuration update process, resulting in inconsistent configuration updates [21]. These problems make the dynamic configuration deployment and verification of SDN more difficult,
especially when network functions virtualization (NFV)
also needs to be supported [48]. If configuration errors
and omissions often occur during the execution of intelligent configuration, because the configuration scheme of
complex networks is complicated, the implementation
difficulty of the configuration scheme is considered big. If
the configuration scheme of a complex network does not
require manual configuration by the network administrator, consumes fewer computing resources, and has less latency during the intelligent configuration process, this
configuration scheme is considered to have good execution efficiency. The network configuration time includes
configuration generation time, resolution time, and execution time. If a configuration scheme can automatically
process new configuration scenarios or migrate from old
configuration scenarios to new configuration scenarios, instead of designing separate configuration methods for each
scenario, the scheme is considered to have good scalability. Table 1 summarizes and compares the representative
studies in terms of generation, verification, deployment,
and implementation of network configurations.
Table 1  Comparison of studies on network configuration
Comparison
item
Network configuration
generation Network configuration verification Network configuration deployment
and implementation
Task
encapsulation
method
Model search
method
Simulation
verification
Actual
verification
Theoretical
verification
Script
encapsulation
Network
configuration
protocol
SDN-based
Related work PACMAN,
PRESTO [45]
ConfigAssure,
COOLAID
[46], [47]
OPNET,
NetSim, and
GNS [54]
SDN-based
telemetry
technology
[55], [56]
Static
analysis of
stateless
components
[65], [66]
PRESTO
[9], [45]
NETCONF
[68], [70]
OF-CONFIG
[72]
Implementation
difficulty Small Big Small Big Small Small Big Medium
Execution
efficiency Efficient Inefficient Medium Inefficient Efficient Efficient Efficient Medium
Scalability Poor Good Good Poor Poor Poor Medium Good
Scope of
application
Basic
configuration
Policy-based
advanced
configuration
Preliminary
verification
The verification
of important
configurations
Only
applicable to
stateless
network
components
Simple and
batch
configuration
Support
dynamic but
infrequent
configuration
Fully support
dynamic
configuration
III. The Research System of Intelligent
Configuration Security
At present, complex networks mainly rely on manual configuration, which is high in complexity, poor in
timeliness, and easy to make mistakes. Moreover, security vulnerabilities caused by improper manual configuration have become the main source of network security
risks. According to the review of the related work at
home and abroad in Section II, although the intelligent
configuration security has accumulated research for a few
years and there are some local intelligent configuration
tools, some key problems are still unsolved. First, there is
a lack of scientific abstraction and theoretical model of
configuration security. Second, there is a lack of in-depth
research on configuration completeness. Third, the fragmentation of configuration management is serious. Fourth,
there is no unified configuration management method.
Finally, there is a lack of security verification environment
and effective testing means for network configuration.
Aiming at the high risk and low efficiency caused by
complex network manual configuration, the paper analyzes the latest research results of intelligent configuration security in recent years, and proposes a research
system of intelligent configuration security. The architecture of intelligent configuration security research system
is shown in Figure 1, which specifically covers three levels:
theoretical research, key technology breakthrough, and
system integration and verification.
In the aspect of intelligent configuration security
theory research, this paper mainly analyzes the abstract
modeling method of network security configuration. The
goal is to provide a unified configuration model for various network components, ensure consistent configuration
semantics for each link in the configuration management
process, and give the theoretical description of the global consistency (configuration association among different
components) and transition consistency (timing association during component configuration update) of the configuration. It provides a solid theoretical basis for the
correctness and security verification of the configuration.
In terms of breakthroughs in key technologies of intelligent configuration security, four aspects of research
were carried out around the key functions in the net
work configuration management process.
i) Automatic generation of configuration, including
the initial configuration generation and configuration update generation of the network, is responsible for analyzing the configuration goals or policies of network managers, generating target network models, and generating
corresponding configuration scripts in combination with
predefined configuration templates.
ii) Formal verification of security configuration. In
order to eliminate the risk of issuing wrong configuration schemes, the configuration scheme automatically
generated in the previous step is formally verified to ensure that the high-level semantics of the configuration
meet the consistency conditions, correctness, and security requirements. Before and after the implementation of
the configuration security scheme, the network connectivity, execution efficiency, and security metrics are tested quantitatively. If the configuration scheme fails to
pass the formal verification, a mismatch counterexample
will be returned to illustrate the problem in the scheme
and the configuration will automatically generate the
module to redesign the configuration scheme. The generation and formal verification of configuration security are
completed at the configuration decision point, forming
the first security control loop when making decisions on
network configuration.
iii) Dynamic deployment and implementation of configuration includes translating high-level configuration
scripts into configuration instructions that can be executed by components on the orchestrator and controller,
and then issuing them in an orderly manner under the
constraints of global consistency and transition consistency. Components execute configuration instructions in an
atomical manner. In order to avoid risks, the configuration execution process generally adopts gradual configuration update or deployment. Once problems are found,
configuration diagnosis is performed immediately and automatic recovery is performed through rapid rollback to
ensure that the network operation is not affected. The
above operations belong to the function of configuration
execution point, and the second security control loop is
formed during the specific execution of the configuration
command.
iv) Telemetry and monitoring of security configuration. By collecting real-time configuration and performance measurement information of components, the actual state of the network is generated to confirm that the
network configuration is correctly issued and that the
network operation state is consistent with the abstract
description. When the network operation status changes
and exceptions are found, the configuration update will
also be automatically started, thus realizing the third
closed loop for the whole lifecycle management of the entire network configuration.
In terms of integration and verification of intelligent configuration security system, it mainly summarizes the construction methods of network security configuration verification environment, index system, and
security testing methods of intelligent configuration. In
addition to forming systematic configuration security
testing and vulnerability mining capabilities, this part of
the research work also forms a complete closed loop for
intelligent configuration. Through constant feedback iteration, theoretical methods and technical solutions are improved to reduce network failures and security vulnerabilities caused by configuration errors, reduce the complexity of O&M, and improve the overall security of
complex networks.
IV. Theoretical Approaches of Intelligent
Configuration Security
The abstract modeling of network security configuration firstly provides semantic unity for various network
components, which can match the configuration models
of different abstract levels, effectively shielding the diversity of manufacturers and technologies; then gives the theoretical description of global consistency and transition
consistency of configuration, which provides a unified
analysis method for model driven closed-loop management of network configuration throughout its lifecycle.
1. Research object of network configuration
abstract modeling
A qualified configuration model needs to meet the
following four elements [73], [74]:
i) Interpretability
The descriptiveness of the network configuration
model should go deep into all aspects of the network, including connectivity and protocol layer. Only when the
information is complete enough, can it be a high-quality
model.
ii) Interoperability
The network configuration model should be able to
be easily converted into the executable network configuranalysisation instructions of components, and vice versa.
This is the basic requirement for model driven method.
iii) Flexibility
The operation granularity should be atomized, and
support operations such as issuing and rollback. Only by
deconstructing the configuration process into atomized
operations with enough detail, can we ensure smooth
switching of intelligent work.
iv) Independence
The network configuration model should be able to
shield the differences among multiple manufacturers and
different technology implementations. The degree and
level of abstraction of the configuration model are determined by the specific requirements of each link of configuration management.
The biggest advantage of model driven method is to
realize the online or update of new business by combining or changing models without modifying the network
code [75]. It is generally implemented by modifying some
scripts and dynamically loading some plug-ins or drivers.
Taking SDN as an example, the control function is entrusted to the control layer, and a standard interface is
provided between the data layer and the control layer to
ensure that the switch completes the task of identifying
and forwarding data [76], [77]. The control layer needs to
abstract the distribution state of the switch into the
whole network view, so that many applications can uniformly configure the network through the whole network
information. The network administrator can automatically complete the unified deployment of forwarding devices along the path by simply configuring the network
through the application interface provided by the control layer [14]. Therefore, configuration abstraction must
be combined with function abstraction and state abstraction to describe and control network behavior.
2. Research approach of network configuration
abstract modeling
The existing configuration abstract modeling methods can be divided into two types, i.e., top-down method
and bottom-up method [9], [67]. 1) The top-down configuration abstract modeling starts from some basic requirements, draws up detailed design abstractions that can
solve problems, and then creates a configuration management platform that can realize these abstractions. Topdown method does not require designers to have a comprehensive understanding of the entire network, but needs
to have a certain theoretical background. 2) Bottom-up
configuration abstract modeling starts from network
components, interfaces, and technologies to create new
management tools to configure, monitor, and control existing networks. The bottom-up design is not limited to the
underlying hardware devices, and designers can also add
high-level services and other software mechanisms to the
managed object collection. Like top-down method, bottomup method can only focus on some aspects of network
configuration management while ignoring others [78].
3. Network configuration model based on
multi-layer structure
The multi-layer structure is the key of network configuration model. As shown in Figure 2, the basic idea of
the multi-layer structure is to divide the network into
multiple layers from bottom to top. The bottom layer is
the physical layer, which contains the physical link relationship of network devices, including device name, Link
Layer Discovery Protocol (LLDP), and ETH-Trunk information. Above the physical layer is the IP layer,
which contains the IP address information of the interface. Up further are various protocol layers, such as Border Gateway Protocol (BGP), open shortest path first
(OSPF), and multi-protocol label switching (MPLS). The
model will build a separate layer for all routing protocols [22], [79]. The association between different layers is
realized through entities shared among layers such as the
device interface and the device itself. BGP and OSPF
layers are associated through the three-layer IP interface
of the IP layer [80]. In terms of attribute definition, all
attributes are dependent on various entities in the network layer. This multi-layer graph structure is easy to
understand and can achieve good interpretability.
In order to meet the abstract requirements of network
configuration for different levels, it is also necessary to
build corresponding business models, conceptual models,
data models, object instances (physical data models), and
meta models to represent different levels of abstraction
from the physical world to the information world [81].
4. Correlation complexity analysis of network
configuration
Although the management interface of general network components allows network administrators to configure parameters independently, many parameters are
semantically related. Changing only one item without
changing the protocol to find related items of other layers may result in an overall configuration error [44]. The
configuration parameters among different components
will form a complex relationship network through semantic association, and the dependency relationship among
some parameters also introduces an implicit selection order, which greatly increases the complexity of the configuration work. This requires research tools to effectively
analyze the global consistency and transition consistency
of configuration.
In terms of timing correlation of component configuration update, some configuration parameters only specify initial conditions. Once the network runs, these parameters will change. Once the data packet is transmitted, other configuration parameters can control the operation of the network. For example, the initial routing
configuration indicates the path of data packets after the
network starts running. However, choosing whether to
configure a routing update protocol determines whether a
network can detect link failures and route around them
[82]. It requires the network administrator to imagine how
the network will operate in the future, so the concept of
changing over time makes the configuration more complex. In fact, the network administrator may need to
think backwards, first imagine a workable network, and
then imagine how to make the network operational
through a series of steps. In order to imagine these steps,
the network administrator must understand the impact
of each configuration choice on the real-time network.
Then, the network administrator must select the appropriate value to generate the initialization condition and
finally reach the required running state. In other words,
the network administrator must consider the temporary
results generated by each configuration selection.
In addition to considering temporary changes, network administrators must also understand the interaction
between configuration choices, which means the network
administrator must imagine the global state of a network, rather than consider each configuration parameter
separately. In other words, the network administrator
must understand how the values stored in each network
element ensure that the network realizes the required
functions. For example, in the case of forwarding, in order
to provide the connection between the Internet and each
host, the network administrator cannot consider the configuration of a router alone, but needs to consider the
forwarding status across the entire set of routers. Although the network administrator configures each network element separately, all routes must maintain global consistency to ensure that all hosts can connect to the
Internet. It indicates that the network administrator
must consider the state requirements of the entire network when selecting configurations. Configuration is just
a mechanism that allows people to set initial state details and control network state changes in real time.
5. Difference analysis between model driven and
intention driven methods
The design goal of intelligent configuration is to realize model driven automatic management of system configuration. The configuration model is used as the basic
information carrier for automatic generation, formal verification, dynamic deployment, and execution of configuration. Different from the intent-based networking (IBN)
[83]–[85], model driven method is based on business and
technical models and cannot directly support the understanding and matching of business intentions. The network administrator needs to express, design, and update
the configuration intent through the defined model. However, the intelligent network configuration based on intent driven method needs to realize the semantic recognition and analysis of the network configuration intention
in the form of text, and expand it to support the formal
intention of language, action, and so on. Through further decomposition and refinement of the network configuration intention, it can be understood and operated by
human and computer [86]. Network configuration intent
description needs to design and develop a general description format of network configuration management in
combination with network device management mode and
configuration description requirements. According to the
identified network configuration intent, a standard configuration intent description document is formed to describe and express the general network configuration
management mode.
Intelligent configuration based on deep learning will
become a trend of network configuration in the future.
Its technical essence is to use deep learning and knowledge graph to semantically identify different defense intentions of network administrators (including language,
text, action, etc.) into network configuration requirements
that can be understood by the machine. With the help of
the automatic translation of the knowledge base of network security specialty into corresponding security defense strategies, the intent of network defense can be fully intelligently transformed into network defense strategies. Intent recognition technology can make full use of
the advantages of capsule network in text modeling.
Compared with other methods, it can effectively distinguish the similarity and dependency between multiple intents, and can achieve more accurate semantic recognition and resolution of defensive intents [87].
Configuration security knowledge system based on
knowledge graph can use the triple knowledge representation which is widely used in the semantic network [88],
[89], and complete the model construction of security intent and configuration security policy through knowledge inference, knowledge mining, and other technologies, to achieve automatic translation of configuration security intent to configuration security policy.
V. Key Technologies of Intelligent
Configuration Security
The key technologies of intelligent configuration security include configuration generation, verification, deployment, and telemetry, forming real-time closed-loop
management of intelligent configuration security throughout its lifecycle.
1. Research on automatic generation of network
configuration
As the first module of intelligent closed-loop management of network configuration, automatic configuration generation studies how to automatically convert
the target network model into machine readable configuration scripts. Configuration automatic generation is a
function of configuration decision point, which is to complete the design and creation of network configuration
scheme, including the definition of configuration script,
initialization configuration, and configuration update, as
well as more complex stateful data plane configuration
and service chain configuration.
1) Definition and design of configuration script
As shown in Figure 3, the definition of configuration
script is mainly to fill the semantic gap between the target network model and the specific configuration instructions. On the one hand, the configuration decision point
realizes the correct decomposition and translation of the
configuration intent based on the grasp of the global network state information. On the other hand, it reduces
the complexity of the configuration decision analysis by
simplifying and abstracting the underlying components.
The key here is to automatically generate configuration
scripts that meet global consistency.
The configuration intention is often described by
combining XML and RDF(S)/OWL to provide basic
support for automatic translation of configuration security for complex networks. The configuration script specifies the semantics of configuration, deployment, and orchestration. The configuration script describes the hosts
of managed components and one or more configuration
tasks that are executed on these hosts in sequence. Each
configuration task calls a module that performs specific
functions, such as collecting useful information, backing
up network files, managing network configuration, or
verifying connections. The configuration script can be
shared and reused by multiple network administrators to
automate repetitive configuration tasks. The configuration scripts can also be combined to support complex
automated configuration processes [90].
The configuration script obtains all relevant component models and generates corresponding component
configurations in combination with the manufacturer’s
relevant configuration templates. The code description of
network components is realized through infrastructure
coding. The configuration script uniformly operates on
these code objects. The configuration script is based on
model abstraction and decouples the parameter definition of the object from the execution code, to achieve the
effect of defining once and applying multiple times, and
maximize the reuse level of the configuration script. Parameter definitions contain specific data information
(value) and relationships among objects. An object is an
abstract class that defines objects to be managed or acted upon, and can be inherited or extended in different
levels [91].
Most of the current configuration management uses
the agent mode, which is based on the pull mode by de
fault. After the agent is installed on the managed component, the agent service will periodically check the service
of the controller and get the configuration information
from the controller. By default, the configuration script
is based on push. Once the configuration script is designed at the decision point and formally verified, it will
be pushed to the component for remote execution [9].
Based on the great advantages of the push mode, the
network administrator can control when to make configuration changes to the remote managed components,
without the need for the managed components to wait
until the periodic query time.
2) Initialize automatic generation and updates of
configuration
It is a characteristic of network intelligent configuration to separate the automatic generation of initialization configuration from the automatic generation of configuration update. In the initial planning stage of the
network, it is necessary to evaluate the possible use
needs, evaluate the traffic, design the topology, and select the implementation technology. Usually, the input to
the planning process comes from subjective assumptions,
and the initial design choices do not require detailed
knowledge. An automatic initial configuration planning
will start from the planning set of an ordinary network,
and select the most suitable network planning scheme
and corresponding network configuration for a given environment. However, the complexity of configuration update comes from the opposite situation of the planning
stage: Not because there is too little data, but because a
large amount of data increases the difficulty of updating
the configuration. Therefore, it is necessary to filter management data based on abstract function, state, and configuration models and extract key information to guide
configuration updates from many detailed information.
In the process of automatic generation of initial configuration, the core problem is to extract the semantics
of the network administrator’s configuration intent and
policy, and effectively use reusable software assets, existing configuration scripts or templates, to complete the
design task of system configuration. First, it is necessary
to reasonably choose the description language for configuration rules. Common formal description languages, including Prolog, cannot correctly describe quantifiers such
as negation, ownership, and existence. Their weak expression ability determines that they are not suitable for
the description of complex network configuration tasks.
Second, it is necessary to select an appropriate rule parsing method to calculate a feasible configuration scheme.
Different description languages may choose different
parsing methods, such as obtaining feasible solutions
through recursive queries or seeking feasible configuration schemes through SAT parsing tools [92]. Choosing
an appropriate parsing method according to the characteristics of the description language is not only a prerequisite for obtaining solutions, but also a prerequisite
for ensuring the correctness of solutions. Third, the configuration requirements should be fully specified. The network administrator needs to comprehensively describe
the requirements of configuration tasks in terms of connection requirements, security requirements, reliability
requirements, performance requirements, etc. Among them,
the connection requirement is the basic requirement,
which requires a path between two nodes. Security requirements are mainly to ensure the credibility, integrity,
authentication, and access control of data. Reliability requirements are mainly to ensure that the network can
operate normally in the case of node or link failure. Per
formance requirements mainly include priority processing of messages and controlling the transmission of messages of some protocols [93].
In the automatic generation process of configuration
update, different from the initial configuration, the
closed-loop control scenario is emphasized. This is triggered by events, that is, when a specific event or fault
occurs, it is processed in a real-time closed loop according to the preset dynamic strategy. At this point, the
configuration update decision module needs to extract
the semantics of events according to the data fed back
by the configuration monitoring module, and then redesign the system configuration script according to the
preset dynamic configuration strategy. Taking the optimal
configuration of network traffic paths as an example, the
automatic configuration network automatically executes
some dynamic tuning algorithms based on feedback information. The selection of tuning algorithms depends on
specific needs, and the tuning results will be executed on
the corresponding network configuration items [94]. The
dynamic feedback mechanism will feed back the adjusted operation information to the automatic configuration
system. The system will judge whether the adjustment is
effective, whether it needs to continue to adjust, whether
it is wrong, or whether it needs to restore to the previous
state according to the feedback results. After repeated
adjustments, the network performance can reach the best.
3) Configuration automatic generation of stateful data
plane
The research of SDN and NFV shows that it is necessary to introduce some stateful operations into network components, which can reduce the excessive delay
caused by real-time participation of remote controllers.
The stateful data plane contains two main principles
[13], [48]. i) The state information of the flow is saved in
the component (such as forwarding device), allowing the
state transformation of the packet level to be instantiated programmatically. ii) Give the component the right to
forward the status update, based on the status information of the local flow without communicating with the
controller.
The main idea of NFV is to decouple physical network devices and network functions running on them,
which means that a network function can be regarded as
an example of common software. In this way, many network devices can be merged into high-capacity servers. A
given service can be decomposed into multiple virtual
network functions (VNFs). These VNFs can be implemented in software and run on general servers, which
can be easily deployed in different parts of the network
without purchasing and installing new hardware. These
VNFs are generally stateful, and they are implemented
by software with high flexibility, but at the same time,
the configuration complexity is greatly increased.
Therefore, it is necessary to build general models of
stateful components as shown in Figure 4 to lay a foundation for automatic generation of configuration of stateful data planes. The pre-installed state machine is stored
in each stateful component, and each stateful component may have multiple state machine instances, each of
which has a specific application. The stateful component
includes several independent tables: state machine filter
table, state table, state transition table, and operation
table. All instances of the state machine share a state
machine filter table, but each state machine has its own
state table, state transition table, and operation table.
The state machine filter table is used to select the corresponding state machine related to the data packet. The
state table is a hash table that maps each data packet
header to the stream state. Each state value is stored in
a variable. As for a number, some high bits are used to
store the state, and others represent the corresponding
value. Finally, the operation table specifies the forwarding device to perform corresponding operations on the
data packet according to the data packet header and its
new state.
State
machine
search
Stream state search
State machine filter
table matching
Status table index
Next status
search
Status
update
State transition table
matching
Operation search
Operation table
matching
Figure 4  General models of stateful components.
The control plane has two components: compiler and
forwarding device proxy. The former is an offline component, which is responsible for converting the state machine into a forwarding device proxy. The latter is an online component i) to manage the state machine inside the
forwarding device; ii) to perform some local calculations
based on the updates received from the forwarding device; iii) to achieve state machine inside the forwarding
device at local level; iv) to process the communication
between the forwarding device and the controller, and
update the local state of the switch on the controller.
4) Automatic generation of security service chain
configuration
Service chain is a forwarding technology that guides
network service messages to pass through service nodes
in order [95]. Based on overlay technology and SDN centralized control theory, the service chain can be configured through the SDN controller [96].
As shown in Figure 5, the typical network model of
the service chain includes the following parts: i) Access
point. The access point is the virtual extensible local
area network (VXLAN) tunnel end point (VTEP). It
judges whether the message enters the service chain according to the drainage rules issued by SDN, and encapsulates the message entering the service chain. ii) Service
node. A service node is a device in the network that processes a certain business. It can be a physical device or
an NFV device. A service chain can have multiple service
nodes, each of which has a unique number. The service
node processes the message according to the service type
specified in the service list.
The service chain is a key technology supporting virtualization and business network programming. As shown
in Figure 6, based on VXLAN and EVPN protocols, with
the SDN controller, the service chain realizes the centralized management and unified scheduling of security device resources, becomes definable and arrangeable, and
achieves elastic expansion of on-demand delivery of security services and automatic and rapid deployment of
security services.
Because the service chain needs to pass through
multiple network elements, the configuration is more
complex. Further coordination may be required between
the configuration of network elements and the configuration of services. At present, there are roughly two solutions: One is recursion, in which each element will make
a request to other elements until the whole transaction is
implemented; The other is iteration. In this scheme, the
management system will contact all network elements required by the transaction. Recursive methods can hide
dependencies between elements, but may form rings and
deadlocks, while the iterative method eliminates the loop,
but requires the configuration management system to understand the dependencies of all network elements and
internal connections.
2. Research on formal verification method of
network configuration
The formal verification of network security configuration is also a function of configuration decision point.
Before the configuration is activated, in order to eliminate the risk of wrong configuration scheme issuing, the
configuration scheme automatically generated in the
previous step is formally verified to ensure that the highlevel semantics of the configuration meet the consistency
conditions, correctness, and security requirements. If the
configuration scheme fails to pass the formal verification,
a mismatch counterexample will be returned to illus
trate the problem of the scheme and the configuration
will automatically generate the module to redesign the
configuration scheme. The automatic generation and formal verification of security configuration form the first
security control loop when making decisions on network
configuration.
The ability to verify that the actual configuration
matches the high-level intent is the key to realizing intelligent configuration [97]. Formal verification is a method
that is different from traditional test environment. It is
based on reasoning of network design, configuration, and
analysis of current network state. It does not view realtime traffic or test scenarios to determine network activity. Therefore, validation can do something that traditional tests rarely do, i.e., prove negative by confirming
that something will not happen. Formal verification
transforms configuration management from a passive
method to a proactive method. Formal verification of
configuration schemes can avoid configuration errors
from the beginning. However, formal verification covers a
limited scope and is based on some assumptions that
cannot be verified. Therefore, it cannot guarantee that
the configuration scheme passing formal verification will
not have problems during the execution process. It is still
necessary to combine with other verification and testing
methods to give play to their respective strengths.
1) Verification of correctness of network configuration
The correctness verification of network configuration
is the ability to verify whether the end-to-end behavior
of the network conforms to higher level intentions. More
specifically, formal verification can perform mathematical analysis on all possible end-to-end paths in the network, and then compare this end-to-end behavior analysis with high-level intentions to see whether it conforms
to [98].
The first problem of network verification is to ensure
the completeness of configuration description. The correctness combination analysis of complex network configuration is shown in Figure 7. Because the configuration
task may involve complex logic relations, the configuration description language should have rich expression
ability and support the combination operation of the system. Thus, the complex configuration tasks can be divided into atomic tasks to reduce the complexity of configuration description. The second problem of network verification is to establish a completeness verification model,
which should be divided into two levels. The one is to
model the configuration object to describe the composition and topological connection of the configuration object to ensure the consistency of the description of the
configuration object. The other is to model the device behavior to describe the behavior specification of the configuration object and ensure the consistency of the device behavior description. The configuration object may
be a subnet or a service, which contains one or more configuration entities, such as switches or routers. Each entity has multiple configuration ports, and there is a connection relationship between the ports. In addition, we
need to define some functions to describe the input and
output of the configuration entity. The device behavior
represents the constraint specification of the configuration entity. An entity implementation form may have
multiple methods, which can be represented as an implementation space. The configuration object includes many
configuration entities, and each configuration entity corresponds to an implementation space. The final configuration scheme is not only to take a method in each implementation space, but also to consider the constraint
relationship between the entity methods.
2) Configuration security verification of human-computer
cooperation
Even if the network configuration is correct, due to
the complexity of the network and the diversity of configuration commands, it is inevitable that some unexpected configuration states can be exploited by attackers,
resulting in security vulnerabilities and becoming hidden
dangers in network operation. Therefore, it is also necessary to verify the security of the configuration scheme [4].
The security verification of network configuration is
mainly to reduce network vulnerabilities and attacked
paths while maintaining the expected functions and performance of the network [99]. Common components contain many states or functions that are not needed in
complex networks. If not masked in the configuration
process, attackers can design new and effective attack
paths and expand the attack surface of the network by
taking advantage of these unnecessary states or functions that exist in the default configuration [100]. In the
process of component composition, the attack surface
and attack path will grow exponentially, and it is difficult to conduct effective analysis and control.
Therefore, human-machine cooperation is required to
verify the configuration security. Automatic verification
of object legitimacy is embedded in the network. Before
generating component configuration objects, the network will show users the changes of the design to the
network, and users can check them. The network will
record all network configuration change logs for tracking
errors and bugs. At the same time, it also records the ID
of the network administrator, through which the history
of the network administrator’s changes to the network
configuration can be find.
By designing and maintaining a security search
model, the relationship among attack sub-graph, component dependency sub-graph, and configuration sub-graph
is formalized. Combined with model checking and symbolic execution with variable symbols in the program,
the system behavior verification tool is used to detect potential security vulnerabilities in network applications
and configuration rules. The network state and configuration script are used as input, and the state space is
searched by using model check to verify the behavior
characteristics under each state and find the existing
security vulnerabilities.
3) Complexity control technology in formal verification
Formal verification constructs the network as a finite state machine, and checks whether the given network meets the specification and whether the network
meets the required invariants through an effective search
method of state space retrieval.
Currently, three methods can be used to effectively
reduce the complexity of formal verification. i) Symbolic
model checking method uses binary decision diagrams instead of independent state lists to express the state space
[101]. Further reduced ordered binary decision diagrams
can alleviate the problem of state explosion. ii) Bounded
model checking uses the Boolean reliability solver to find
counterexamples under certain boundary conditions
[102]. For example, the network can be divided into multiple sub-parts, and each sub-part can be described and
reasoned separately. The number of network components
can also be reduced by optimizing the network design.
iii) Using the idea of local optimization [103], configuration parameters with certain values no longer participate
in the operation, which can reduce the scope of state
space search to a certain extent.
3. Research on dynamic deployment and
implementation of network configuration
The dynamic deployment and implementation of
configuration is to translate high-level configuration
scripts into configuration instructions that can be executed by components in the orchestrator and controller, and
then issued in order under the constraints of global consistency and transition consistency. Components execute
configuration instructions in an atomical manner. In order
to avoid risks, the configuration execution process generally adopts gradual configuration update or deployment.
Once problems are found, configuration diagnosis is performed immediately and automatic recovery is performed
through rapid rollback to ensure that the network operation is not affected. The above operations belong to the
function of configuration execution point, and a second
security control loop is formed during the specific execution of configuration instructions.
Even if the configuration script made by the configuration decision point is correct, the final configuration
on the component cannot be guaranteed [104]. First,
there are configuration installation delay and execution
order problems in the configuration execution process.
Even if the final configuration can converge to the expected configuration, new and old configurations will coexist in the intermediate transition phase, leading to network exceptions and security vulnerabilities. Second, it
cannot be ruled out that there are software and firmware
errors in the components, resulting in incorrect execution of the configuration instructions. These problems
deeply reflect the fundamental contradiction between
centralized decision-making and step-by-step implementation in network configuration, and need to be effectively solved in the implementation phase of configuration.
1) Hierarchical implementation of configuration
arrangement and control
Orchestration is described as the automatic arrangement, coordination, and management of complex networks
and services. Its difference from automation is that automation usually focuses on one task, while orchestration
usually refers to the automatic scheduling capability unrelated to specific tasks, i.e., the automation of processes
and workflows. Relevant workflows are defined through a
description language, and the orchestrator is responsible
for executing corresponding actions according to the
loaded workflow.
The configuration update of complex networks involves many devices and protocols, so a smooth incremental change scheme is required, which involves scheduling, such as the sequence of configuration changes to
devices, so that changes do not affect the current network.
As shown in Figure 8, the orchestrator calculates the interdependence of all network configuration modules
based on the configuration script. Each configuration module is a basic atomization operation, which can ensure
the smooth progress of incremental network changes.
Based on computing, storage resources and networks, the controller translates high-level configuration
scripts into configuration commands that can be executed by components, and then controls the issuance and
implementation of configuration commands on the data
plane. It is necessary to complete the comparison and
confirmation of the initial status of components, atomization of configuration tasks, configuration problem diag-
nosis, rapid rollback of configuration, and network recovery. The network status will be detected every time the
configuration is released. If it is abnormal, it will be
rolled back, to quickly respond to possible failures in the
configuration update.
In order to ensure the scalability of the network, it
is necessary to deploy multiple controllers to complete
the configuration control of components nearby, and the
organization among controllers becomes a problem. By
using hierarchical control, the controllers are classified
according to their purposes. The local controller is relatively close to the components, responsible for the components contained in the region, and only knows the network status of the region. The global controller is responsible for the maintenance of the whole network information, and can complete the operations that require the
whole network information. There are two ways for hierarchical controller interaction. The one is the interaction
between local controllers and global controllers, and the
other is the interaction among global controllers. The hierarchical control architecture is more in line with the
needs of complex networks. Table 2 shows the main investigated security orchestration solutions for SDN/NFV,
which are classified in terms of policy support, integrated detection, and autonomic reaction mechanisms. Furthermore, since the integration of heterogeneous security
mechanisms is crucial, we provide corresponding execution environment respectively, namely SDN, cloud,
ETSI NFV MANO, and Internet of things (IoTs).
2) Atomization implementation of configure transaction
To help network administrators control the complexity of configuration operations, a series of configuration
instructions need to be considered as an atomic level
unit. All the commands in the set are either applied or
not applied. We use the concept of transaction to describe a collection of indivisible atomic operations. When
the command line interface provides incremental commands, each command can only complete one operation,
so a transaction is a collection of several commands.
When the command line interface provides complex commands, each command can complete multi-step operations, so a transaction can contain only one command.
The interface specifications for network equipment generally include reporting, issuing, and querying interfaces.
For example, we can imagine a router whose management interface provides only one command to enable all
interfaces. If this command is executed in a transaction
mode, the interface enabling process will be interrupted
once a hardware problem occurs. Also, the command reports an error and does not enable any interfaces.
The transaction interface of the configuration operation is important because it relieves the administrator of
the responsibility of revoking some operations. The management interface divides many operations into transactions, which is convenient for use and reduces the possibility of people making mistakes.
In order to support atomic configuration transactions and prevent some switches on the forwarding path
from having new rules while others use old rules during
the update process, which causes inconsistent forwarding
rule configuration updates, a two-phase commit method
is required to update the configuration. In the first stage,
when a rule needs to be updated, the controller asks each
switch whether it has processed the flow corresponding
to the old rule, and updates the rules for all switches
that have processed the flow. In the second stage, the
update is only completed when all switches are updated,
otherwise the update operation will be canceled.
4. Research on telemetering and monitoring
methods of network configuration
As the last module of network configuration automation closed-loop management, the research of configur
ation monitoring, like other system monitoring, needs to
answer three basic questions. They are what indicators
need to be monitored; how to get the monitoring results,
and how to analyze and process the monitoring results.
Focusing on these three issues, this part will study the
architecture design of configuration monitoring, the
telemetry method of configuration, and the security baseline maintenance technology.
1) Architecture design of configuration monitoring
Configuration monitoring is inseparable from other
system management-oriented monitoring, and the monitoring architecture should be designed in an integrated
way. As far as the monitored objects are concerned, they
include network status parameters, network performance
parameters, and network traffic parameters. Network
status parameters include the configuration information
of network nodes, the status information of network
links, and the topology of the network. They are the basic
parameters of the network. Network performance parameters include throughput, packet loss rate, delay, etc.
This parameter requires high real-time measurement and
reflects the instantaneous operation state of the network.
The network traffic parameter is generally obtained by
collecting and analyzing the network traffic within a certain period. It is a statistical parameter, such as the statistics of the number of messages and the statistics of the
flow length. The network potential information can be
obtained by deeply mining the traffic parameter. It seems
that only the network state parameters are directly related to the configuration. But in fact, because the network
performance parameters and network traffic parameters
can more accurately reflect the configuration parameters
and the real behavior of the networks, they are more
helpful for configuration diagnosis and prediction.
Considering the different characteristics of different
monitoring objects, the following three monitoring mechanisms can be used to timely, accurately, and comprehensively understand the actual operation status of the
network.
Passive monitoring records network traffic on links
or devices, such as routers and switches, in the network
by means of packets captured by probes, analyzes traffic,
and gets the performance status of the network. Passive
monitoring detects some events, such as device configuration updates, route flipping, and device restart events.
Syslog monitoring is based on the passive mode. For the
monitored log information and combined with regular expression matching, it can flexibly filter out the key information to trigger the alarm notification when abnormal
log information is found.
The active monitoring is initiated by the detection
instrument to collect the performance, such as CPU and
memory usage, and monitor the device status. Active
monitoring is divided into three parts: task manager,
monitoring engine, and back-end. The task manager is
used to manage and distribute monitoring tasks. These
tasks involve the collection interval, the type of the collected data, and the backend to which they are stored.
After receiving the task, the monitoring engine will collect data from the corresponding devices through various
interfaces and protocols. The back-end will convert the
collected data into the corresponding format for storage.
Configuration monitoring uses both active and passive monitoring technologies to monitor the configuration running on the current device [112]. When there is a
configuration update, the passive monitoring detection
will detect the newly generated syslog log, and then trigger to issue an active task to collect the current configuration of the device. The configuration collected each
time will be backed up to the version management warehouse to track the configuration history update of each
device.
The amount of data obtained by monitoring is very
large, which cannot directly reflect the running state of
the system. Therefore, we will input the monitoring data
into the model generator in a unified format, and abstract the various types of data of the current network
into the network model, which can be used for fault diagnosis, comparison of key attribute configuration, etc.
2) Telemetry method of intelligent configuration
Telemetry is a technology to measure the parameters of the measured object remotely. The network itself
can also conduct telemetering, providing more real-time,
more comprehensive, and more sophisticated network
awareness through remote high-speed collection, and
monitoring of data from network device. Network telemetry is the basis of configuration deployment, fault monitoring, and fault prediction. SDN also brings new development opportunities for network telemetry. On the one
hand, the emergence of SDN makes real-time network
telemetry more important, because if the control plane
cannot accurately grasp the state of the data plane, the
separation of the data plane and the control plane and
the control of logic concentration will be meaningless; On
the other hand, SDN also provides a new technical approach to the realization of network telemetry.
Traditional supervision methods, such as SNMP/
CLI, use the pull mode of network management querying the device response to collect data. Each query has a
response. The device needs to handle many repeated
queries. SDN telemetry adopts the push mode of network management customization and real-time push of
device to collect data. One customization can correspond to multiple responses, reducing the pressure on the
device to process query messages. The key point is that
the data structure of SDN telemetry adopts standard
structure and standard coding. It is convenient to interface with third-party device, which is conducive to the
improvement of network monitoring efficiency and monitoring quality.
At present, the most promising network measurement technology is in-band network telemetry (INT) [113].
INT uses SDN to control network flow to enable detection device to obtain accurate network data of observation points, thus greatly expanding the active or passive
detection capability of the network. At the same time,
INT uses programmable data plane technology to directly write network applications such as network measurement through high-level languages such as P4 that program the packet processing behavior of the underlying
network devices, and then configures the underlying network devices through compilation to meet the users’ network measurement functional requirements.
As shown in Figure 9, INT can directly realize network measurement through the data plane without
adding additional burden to the control plane. By embedding instructions in the packet header of the network
flow, the detection device tells the network device what
status information it needs to collect. Through the end of
the network flow, the results of these instructions can be
retrieved, to accurately detect the status of the data
plane. The information interaction in network measurement is completed through the packet header of network
flow, so it is called INT.
The design of INT needs to deal with two balance
relations. The first is the balance between measurement
resources and measurement accuracy. The flow in SDN
can be divided into two types, control flow and data
flow. Control flow is the flow transmitted between SDN
controller and SDN switch, and data flow is the flow
transmitted between SDN switches. The normal operation of the network cannot be separated from the normal transmission of control traffic, but SDN measurement tasks often require additional communication between the controller and the switch, or carry additional
measurement information in the control traffic, which
brings some pressure to the limited bandwidth resources
between the controller and the switch, especially when
the controller is deployed in the band. In addition, the
use of large-scale detection packets in the active measurement method may also affect the production traffic
in the network. The second is the balance between realtime measurement and measurement accuracy. SDN
measurement supports real-time analysis and feedback of
traffic, and the controller rapidly adjusts and optimizes
network configuration according to the measurement results to meet the dynamic requirements of network services. Due to the complexity of the measurement mechanism and algorithm, traffic processing needs to consume
a certain amount of time. Hence, when measuring the linear speed of large-scale traffic, it is necessary to balance
the real-time measurement and measurement accuracy.
3) Security baseline maintenance technology
Traditional fault and security monitoring is threshold-driven. Once some network measurement results exceed the threshold, the network monitoring system will
alarm the network administrator. Because the data flow
in the network will change significantly over time, the
monitoring system using absolute threshold will generate
many false alerts. The security baseline maintenance
technology can make the network no longer set an absolute threshold, but use a baseline measurement method
[114], and set it after a long-term observation. Once the
baseline is established, the measurement results of the
network can be compared with the baseline. In order to
monitor the network more effectively, the monitoring
system will only alert the administrator when the traffic
is significantly different from the baseline measurement
results.
Security baseline refers to the standards that network security configuration must meet in order to meet
the requirements of security specifications. It is generally measured by checking whether the security configuration parameters meet the standards. It mainly includes
account configuration security, password configuration
security, authorization configuration, log configuration,
IP communication configuration, etc. These security configurations directly reflect the security vulnerability of
the network itself. The significance of the security baseline is to conduct various security inspections on the target network at different stages of the network lifecycle,
find out the security configuration items that do not conform to the baseline definition, select, and implement security measures to control security risks, and obtain the
network security status and change trend through the
analysis of historical data. Therefore, based on the rich
network security and O&M data in the early stage, the
monitoring system needs to establish a security baseline
for the main network components through big data analysis and expert system [115], to verify and maintain the
security baseline.
VI. Integration and Verification of
Network Configuration Security
The integration and verification of network configuration security is critical. For example, the ConSec project of DARPA spends two-thirds of its R&D time on
network testing and evaluation.
1. Construction of configuration security test
environment
The basic concept of the built configuration security test environment is a hybrid system that combines a
limited scale actual verification system with a large-scale
high fidelity cloud environment simulation [116].
In order to adapt to the real security configuration
needs, we should fully consider the configuration services,
network node size, network topology, and other real system attributes, and use real network components to
build the configuration security test environment. Different from the running system, the test environment can
be configured with out-of-band measurement devices to
conduct comprehensive data collection and verification of
the network without considering the cost. The test environment includes three parts.
1) Network operation test
The effect of network configuration can be observed
through the transmission rate, utilization, throughput,
delay, and packet loss rate of the link. If an exception is
found, the network configuration file can be restored to
the latest valid state. The network exceptions are not
necessarily caused by configuration errors, so this test
method is generally applicable to new configurations
that have just been issued. By comparing the network
operation status before and after the distribution, if the
expected effect is not achieved or an exception occurs
after the distribution, it will be considered as improper
configuration.
2) Control plane test
The network configuration files are periodically back
up and the configuration data are extracted from these
files to carry out configuration consistency verification,
which can not only find the recently issued configuration
errors, but also verify the possible errors in the historical configuration. The control plane test generally includes the following four modules as follows: i) the acquiring configuration information module that extracts
the information of the network configuration file and
saves it in a device-independent data format; ii) the establishing requirement database module that records the
end-to-end requirements under the optimal situation; iii)
the formal description module that selects the description language and simplifies the standardized description
of requirements; iv) the requirement verification module
that verifies the requirements, giving modification suggestions for incorrect configurations, and shows the logical
connection relationship of the device.
3) Data plane test
Through the analysis of the data in the data plane,
we test and analyze the network. Although it cannot directly reflect the configuration errors, it can infer some
errors in the network, such as routing loops and packet
loss. The network administrator can locate some configuration errors based on these feedbacks. The forwarding
information module is responsible for obtaining forwarding information tables (FIBs) of routing devices. This information may be simple longest matching rules or complex access control and message encapsulation policies
[117]. Invariants represent the correct conditions for forwarding behavior. Violation of these conditions usually
indicates that there may be vulnerabilities in the network.
Script language or formal language is used to describe
these invariants. The verification module converts FIBs
information and invariants into SAT instances and submits them to the SAT parser for processing. If the processing results violate the invariants, it indicates that
there may be vulnerabilities in the network; At the same
time, the verification module gives a counterexample to
guide the modification of the error.
The flexibility and scalability of the actual test is
not high, and it needs to be combined with the simulation system to play a better role. Traditional simulation
systems cannot detect the bugs of components, because
these errors are unknown to the device supplier itself and
cannot be included in the simulation. Moreover, the simulation workflow is different from the actual workflow,
which means that it is not suitable for discovering human
errors, but human error factors are also important.
Therefore, a large-scale, high fidelity network configuration simulator is needed to accurately verify any configuration changes or evaluate the impact of various failure scenarios. High fidelity means that the simulator can
accurately simulate the behavior of the actual system,
especially in the control plane. In addition, it allows network administrators to use the same tools and workflows as the actual network. We do not require full fidelity. It is not feasible to create a complete digital copy of
the actual network. Therefore, our goal is not to simulate the network data plane nearly realistically. The emphasis of the research is to accurately simulate the control plane. To accurately simulate the control plane, we
run the real component device firmware in the virtual
sandbox [118]. Most major router vendors can provide
such virtual machines or containers. The device sandbox
and virtual link are connected to each other to simulate
the real topology. It loads the real configuration into the
simulation device and injects the real routing state into
the simulation network.
The network administrators can interact with the
simulation test platform using the same tools and scripts
used to interact with the production network. We can
also inject data packets and monitor their paths in the
simulation test platform. Network devices including real
hardware can even be extended in the simulation test
platform. The simulation test platform is designed to run
in the public cloud. If necessary, we can even use multiple public and private clouds at the same time. Because
virtual machine failures can occur in any large-scale deployment, the simulation test platform allows to save
and restore the simulation state, and quickly incrementally change it. The simulation test platform can handle
a variety of device firmware, and can scale in a few minutes to simulate thousands of network devices. While ensuring the correctness of network change propagation,
the simulation test platform carefully selects the simulation boundary to reduce resource consumption.
2. Index system and evaluation method of
configuration security test
In combination with the above configuration security test environment, it is necessary to develop the indicator system and evaluation method of configuration security test to form a formal system security configuration
test and evaluation capability.
In order to meet the security requirements of complex network intelligent configuration, it is necessary to
design a multi-level security configuration efficiency evaluation index system and security risk evaluation index
system [119]. The rough set theory is used to reduce the
multi-attribute of the multi-dimensional evaluation data,
design a security index measurement mechanism based
on the level quantification and association rules, and calculate various index values quantitatively. Knowledge
reasoning, risk prediction, comprehensive evaluation, and
other methods are used to realize the risk comprehensive
evaluation of security configuration.
The deep mining and identification technology of
configuration vulnerabilities is to deeply mine hidden
dangers in security configuration by simulating vulnerability discovery technology and attack means commonly
used by hackers [120]. Test the robustness and security
of security configuration program by generating many
malformation test data. A variety of tools, technologies,
and procedures need to be developed to exploit typical
configuration-based vulnerabilities in complex composite
systems. Evaluate the possibility of using configuration
vulnerabilities to attack the target system, generate an
initial configuration set with set vulnerabilities, and test
the ability of the security configuration platform to independently discover and improve vulnerabilities.
VII. Prospects
Even though complex networks have achieved success in intelligent configuration security, it needs more
investigation in some aspects. As a result, we will discuss some prospects with the peers who are interested in
promoting their research in this area.
i) It is necessary to propose an abstract modeling
method suitable for network security configuration, complete the functional abstraction, distributed state abstraction and configuration abstraction of system components,
form a component configuration model that supports
composite analysis, including physical/virtual components and stateless/stateful components, and build a distributed configuration method that meets global consistency and transition consistency for typical application
scenarios and business requirements to provide a unified
theoretical basis for model driven network security configuration automation.
ii) It is necessary to build a comprehensive, universal,
scalable, and adaptive network configuration platform
architecture which is conducive to achieve seamless management of the whole lifecycle of the network configuration process, global unified arrangement of configuration
deployment, and real-time closed-loop automation under
configuration monitoring, significantly reduce manual
intervention, improve work efficiency and configuration
security, and form a near real-time agile configuration
capability.
iii) It is necessary to propose a three-dimensional
network configuration verification method which uses formal
verification, simulation verification, and actual verification methods to form a global verification capability for
configuration consistency, an accurate detection capability for configuration security vulnerabilities, and a rapid
recovery capability for configuration errors, in order to
greatly improve the security of complex networks and
the ability to resist network attacks.
iv) It is necessary to build a complete network configuration security testing environment and testing index
system to develop the ability to discover and verify the
vulnerability of network configuration and the ability to
quickly mine configuration security vulnerabilities, possess real time monitoring of network configuration parameters and automatic maintenance of security baseline,
and realize visual human-computer cooperation configuration security analysis interface.
VIII. Conclusion
This paper introduces the latest achievements in
complex network intelligent configuration theory and
methods, key technologies, system integration and verification, and uses intelligent means to overcome the limitations of human cognition and behavior and solve the
problems such as network failures and security vulnerabilities caused by complex network configuration errors.
This paper systematically describes the abstract model
and formal analysis method required by intelligent configuration, which can provide a theoretical basis for model driven configuration security. The key technologies,
such as configuration semantic awareness, automatic configuration generation, dynamic deployment, and verification evaluation, are discussed in depth, which is helpful
to achieve global unified orchestration and real-time agile configuration. The configuration security test environment and the construction method of the detection index system are analyzed in detail, which supports the
formation of the comprehensive effectiveness verification
capability of the security configuration. The whole lifecycle management system of security configuration process
proposed in this paper provides important technical support for reducing the complexity of operation and maintenance and improving network security.