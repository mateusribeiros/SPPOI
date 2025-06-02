Title: An urgent computing oriented architecture for dynamic climate
risk management framework

ABSTRACT
The Computing Continuum drives holistic system integration, especially in the road sector, where there’s a growing need for comprehensive Decision Support Systems in operation and maintenance
strategies based on sensor data. These systems offer dynamic assessments, critical for managing road assets vulnerable to climate
change and extreme weather events. The resulting data uncertainties, including variations in data veracity and variability require
timely decision-making for coordination and adaptiveness of the
system as a whole. We introduce an urgent computing architecture
for a dynamic risk management framework, discussing its related
challenges and software design patterns.
ACM Reference Format:
Shahrzad Pour, Daniel Balouek, Amir Masoumi, and Martin Brynskov. 2023.
An urgent computing oriented architecture for dynamic climate risk management framework. In (UCC ’23). ACM, New York, NY, USA, 4 pages.
https://doi.org/10.1145/3492323.3495590
1 INTRODUCTION
The impact of climate change heavily influences operation and
maintenance activities of critical infrastructure at strategic, tactical,
and operational decision levels [13], [11]. Extreme weather events
impact transportation systems, including roads, rails, and electrical
lines, to a significant degree. An illustration of this can be seen in
the trends of economic losses caused by climate-related events in
EEA member states from 1980 to 2020, which total over 500 million
euros. A substantial 80% of this sum is attributable to severe weather
phenomena, whereas insured losses comprised a mere 25% to 33% of
the total losses [7]. Although the financial implications of climate
change are well understood, there is still a lack of information
concerning its operational implications, particularly with regard to
precautionary measures against the inevitable changes that arise.
The Internet of Things has been one of the enablers of smart
services across various domains. At a higher level of abstraction, it
encourages a holistic approach to software design by fostering the
integration of multiple isolated systems. In practice, the physical
division of these systems into distinct sub-units systems results
in the management of separate silos, to the detriments of crossdomain decision making. At the same time, modern applications
are moving in the direction of the Continuum Computing, a distributed approach where Cloud, Edge and IoT aim to collaborate for
publishing, cleaning and computing data while managing aspects
of performance, security and QoS [6, 9].
A class of time-sensitive systems and applications known as
Urgent Computing makes use of distributed data sources to speed
up the making of important decisions [3]. Similar requirements
apply to risk assessment for road infrastructure, specifically for
predictive models, reactive/adaptive planning, and KPI monitoring,
as outlined in [10]. In order to avoid or mitigate the adverse effects
of climate change on road infrastructure, there is an opportunity to
use distributed resources throughout the Computing Continuum
and leverage urgent computing principles to predict the outcomes
of scenarios [3]. In the context of road safety, the wide array of
system capacities and varying service capabilities, alongside the
significant uncertainty stemming from disparities in data quality
and availability, present the primary challenges in constructing
an adaptive Decision Support System (DSS) [21]. Addressing the
vulnerability of road assets to weather conditions, the authors have
incorporated a climate risk management framework in line with the
definition provided in [18]. This comprehensive risk management
framework is typically recognized as either an independent module
or an essential component within a DSS, often implemented through
iterative processes as outlined in [18].
In this paper, we propose a proactive, holistic architecture for
risk management and road safety. This is a major shift in the way
transport networks function, and it requires the ability to effectively
estimate road conditions risk as a function of operating conditions
and information technology. By integrating IoT and climate risk
data into all decision-making levels, we move away from current
approaches. Our method combines an architecture for data-driven
workflows across systems with the needs of a big data pipeline for a
risk management framework. The goal is to address the uncertainty
surrounding climate data (veracity) and the demanding time and
quality constraints when making decisions based on significant
variations in data patterns (variability).
The remainder of the paper is organized as follows. Section 2
discusses the motivation, background, and challenges for this work.
Section 3 proposes an architectural vision for the risk management
framework. Finally, in Section 4, we summarize this paper and
discuss future works.
2 MOTIVATION, BACKGROUND AND
CHALLENGES
2.1 Motivating Use Case
During severe weather events, there’s a significant surge in data
from diverse sensors and weather stations, especially upon surpassing specific thresholds. Urgent data preprocessing becomes
crucial due to immediate actions required during these events and
uncertainties regarding the number of interoperable subsystems
necessitating data exchanges. This surge affects operation and maintenance activities, presenting two primary challenges: insufficient
coordination and adaptiveness among agencies.
2.2 Background
Holistic Decision Support Systems in road sector The integration of decision-making processes within road domain literature
has been relatively underexplored. Early studies, like [15], focused
on integrating maintenance into Pavement Management Systems.
Recent research, such as [16], delves into real-time GPS and GIS
technology integration. While [19] offers a comprehensive survey
of advancements in the road sector, rarely studies [21] explicitly addresses the vital requirement for adaptation mechanisms to handle
uncertainties within Decision Support Systems (DSSs).
Architecture-oriented approaches for addressing the Continuum. Architectural approaches are vital for managing the Computing Continuum, introducing unique challenges concerning subcomponent control and adaptation. The aggregation of architectural
and algorithmic challenges within individual components [6, 9]
poses complexities as these subcomponents inherently influence
each other while conducting urgent analytics [1]. Predicting infrastructure volatility and meeting the demands of urgent analytics
is challenging due to their unpredictable ature [5].To best of our
knowledge, leveraging the Computing Continuum for this application constitutes a novel direction in the field.
Dynamic Risk Management framework A dynamic risk management framework involves five iterative steps: context establishment, risk assessment using various techniques and algorithms,
exploration of mitigation strategies (often in consultation with
stakeholders), implementation of these measures, and continuous
monitoring and review through KPI dashboards. This comprehensive definition is part of an overview paper on adaptive decision
support systems in the context of climate change [18] and is depicted in Figure 1. Bayesian Believe Network (BBN) as a bottom-up
approach [18] has been the chosen approach[21]. However, the
details of risk assessment model is not the focus this paper,the risk
assessment model can continually mature over time using the BBN
model, integrating stakeholders’ beliefs or new inputs whenever
necessary
2.3 Challenges
Urgent data-driven workflows must be efficiently coordinated by developers and service providers in order to construct time-sensitive
decision-making pipelines. Accommodating the considerable infrastructure heterogeneity, this coordination must address uncertainties
related to data source dependability and availability [17]. In the
realm of road safety, three specific challenges stand out:
Automated data collection Currently, operational technologies
in this domain are functionally silo applications [21]. Edge technologies can provide incentives to sanitize data and respect the
privacy of individual systems while allowing for the sharing of
information to make the system unbiased and flexible.
Autonomics Programming abstractions that allow the specification of application behaviors that can react to unforeseen events
during runtime are therefore critical to the overall performance of
applications deployed throughout the continuum [12, 14]. Furthermore, to enable resource and execution path adaptability across the
continuum, autonomic runtime techniques are required [20].
Integration of Smart Solvers: Decision Systems are essentially
alike to solving combinatorial problems. Constraint programming
(CP), particularly in the form of Constraint Satisfaction Problem
(CSP), is well-suited for generating feasible planning solutions and
strategies swiftly in scenarios involving real-time uncertainties
across various resource classes. Additionally, Constraint Optimization Problem (COP) is a viable option when time and resources
permit for plan optimization.
Online/Real-time Communication: Modern data services and
messaging protocols allows and simplifies the development of a
holistic DSS [8]. The current state of the management systems
used in the road sector (PMSs & MMSs) do not utilize direct data
exchange and communication between the systems. Introducing
online and real-time communication between systems in a unified
architecture that includes both management components, will allow
for knowledge-oriented communication.
3 ARCHITECTURE
3.1 Architecture Goals: Functionality and
Interoperability Design
The design goals of this architecture are as follows:
3.1.1 Functional Requirement: The architecture should consider the required data sources, end-to-end process, actors, and
deployment:
Data sources: Various static and dynamic data sources are involved
in the use case, including the meteorological and hydrological data,
flood-sensitive areas (blue spot data model [2]), and road infrastructure condition data.
End-to-end Process: The pipeline should address the data collection, orchestrating operations, and demanded data operations i.e.
modules of the risk management framework in uncertainty situations, including extreme weather events and climate changes.
Actors: Actors include infrastructure owners or maintainers, with
road authorities and municipalities being predominant in the former category and consulting companies in the latter. Additional
actors could include citizens, particularly if the system is used as
an early warning system to notify them about extreme weather
events.
Deployment: The system as an infrastructure as code per stakeholder or per region, while most subsystems are partly autonomous
on the device edges or fog but able to receive the task upon decision
by the system.
3.1.2 Interoperability as quality attribute: The required architecture for the dynamic risk management framework demands
interoperability. As shown in Figure 2, there are three interoperability aspects involved in the problem:
Level 3 - Horizontal interoperability (Over Actors – orange dotted
line): Infrastructure owners, road authorities, municipalities, and
consulting companies are key actors in the domain, with a focus
on their involvement in the problem.
Level 2 - Horizontal interoperability (Over systems in various
geographical regions – violet dotted line): The architecture must
support cross-sectorial applications in environmental and mobility/-
transport domains across different geographical regions, ensuring
Continuum software abstraction.
Level 1 - Vertical interoperability (Over data spaces – blue dotted
lines): The system should seamlessly integrate within a broad spectrum of digital solutions and sub-systems, particularly addressing
urgent computing demands
3.1.3 Urgent Services: The architecture should address the necessary services required for fulfilling urgent tasks, including identifying available computing resources and data sources within the
computing environment as well as ensuring that resources are
allocated efficiently to meet the immediate computation demand.
3.2 Proposed Architecture
Figure 3 depicts our software architecture, responsible for gathering data from diverse sources such as road asset conditions, floodsensitive areas, and various climatological data including precipitation, zero-crossing (indicating fluctuations around zero degrees),
and sea-level rise. This data is fed into the pipeline, triggering an
’event receiver’ for extreme weather events and data changes. Orchestration manages essential services, communicating through a
message broker. The resulting information is utilized by applications.
3.2.1 Addressing Functional requirements. We endorse an
event-driven microservice architecture as our chosen architectural
style, wherein ’event-driven’ characterizes our coordination/communication model, and ’microservices’ define the pattern for allocating responsibilities.
Microservice architecture for allocation of responsibilities:
The module of orchestration service, and all the modules of Interaction, Discovery, and Optimization as part of urgent computing
modules plus the modules of dynamic risk assessment are developed each as one separate microservice.
Event-Driven Architecture as coordination/communication
model: Event-driven architecture utilizes a message broker to reduce coupling between producers and consumers. This intermediary element effectively handles high volumes of data at different
speeds by storing data or notifications in a queue until resources
are available for processing.
3.2.2 Interoperability tactics. Among two main categories of
interoperability tactics i.e. locate and manage interfaces [4], we use
below tactics:
Urgent Discovery Service: a locate tactic: When it comes to
addressing urgent requirements for processing extreme weather
events, the initial step involves activating a discovery service. This
service is tasked with identifying and pinpointing accessible data
sources residing in edge, fog, or cloud as data spaces.
Interaction Service: an Interface tactic This service acts as an
interface to interact with multiple external subsystems and various
actors. A RESTful API is designed for minimal interdependency
between clients and servers. It is worth mentioning the efforts
made to establish minimal interoperability standards and tools for
enhancing data, system, and service interoperability between cities
and supplier stakeholders [22].
Orchestration Service: an interface tactic The orchestrator
acts as a middleware enabling the composition of services based
on specific goals and content, rather than directly engaging with
devices or names. In this scenario, the architecture becomes domainagnostic, and interoperability is enhanced through the use of discovery services and optimization services to address resource uncertainty and data availability.
Optimization Service: a locate tactic: This service plays a
crucial role in efficiently and effectively managing computational
resources to meet the urgent demands of tasks in the whole data
space environment to make sure all the systems and subsystems are
interoperable resource-wise towards a common goal. The service
is modeled as CSP, in case of urgency and is run as a COP upon
having enough resources time-wise.
4 CONCLUSION AND FUTURE WORKS
In this study, we’ve integrated an urgent computing architecture
into a dynamic risk management framework to manage time-sensitive
tasks during extreme weather events. This approach addresses big
data challenges posed by variability and reliability across IoT-EdgeCloud resources. The architecture’s implementation and evaluation
will be based on real data from the Danish Meteorological and Hydrological Institutes (DMI, and DHI), coupled with road condition
data from authorities. Furthermore, our plan includes enhancing the
risk assessment model by integrating pavement bearing capacity
data to evaluate pavement structure functionality.
ACKNOWLEDGMENTS
Thanks to the ELEXIA (Horizon Europe No. 101075656) and IEA
EBC - Annex 81 - Data-Driven Smart Buildings (EUDP Project No.
64019-0539) projects, which have supported partly this research.
This research is supported in part by the NSF under OAC 2238064
