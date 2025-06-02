Title: Bridging Theory and Practice:
Addressing Current Cybersecurity Gaps
in Industry 5.0

ABSTRACT In the modern technological landscape, standardized practices are fundamental to ensuring
efficiency, quality, and seamless interoperability across various industries. The IEC 62443 series of standards
has become a critical benchmark for enhancing cybersecurity in Industrial Automation and Control Systems
(IACS). Nevertheless, a significant limitation of these standards is the lack of detailed implementation
guidance, which poses substantial challenges for organizations seeking compliance. This paper studies the
critical role of IEC 62443 standards series certification, emphasizing its importance and the diverse benefits
it offers. We emphasize the necessity of conducting thorough cybersecurity gap analyses to strengthen
security measures and enhance resilience against the evolving landscape of cyber threats. Using the IDUNN
project as a case study, we illustrate how aligning technological developments with the IEC 62443 standards
series can bridge the divide between existing cybersecurity guidelines and emerging threats. Furthermore,
we examine the lifecycle management of cybersecurity events in accordance with the IEC 62443 standards
series, explain methodologies for capturing security requirements, and discuss the integration of IDUNN’s
tools into current systems to fortify cybersecurity defenses. The findings highlight the imperative for
continuous collaboration and the ongoing enhancement of cybersecurity frameworks, culminating in best
practices and recommendations to ensure the effective implementation of advances derived from initiatives
like IDUNN.
INDEX TERMS Cybersecurity, IEC 62443, Industrial Automation, Industry 5.0, Vulnerability Detection,
standardization
I. INTRODUCTION
The rapid evolution of Industrial Automation and Control
Systems (IACS) has indeed ushered in the era of Industry 5.0,
which emphasizes the integration of advanced technologies
such as artificial intelligence (AI), robotics, and the Internet
of Things (IoT), alongside human-machine collaboration.
This integration aims to enhance manufacturing efficiency,
productivity, and innovation while simultaneously introducing significant cybersecurity challenges due to increased
connectivity and reliance on digital systems [25].
As industrial systems become more interconnected, they
create a complex network of devices, sensors, and control
systems that are increasingly vulnerable to cyber-attacks
[15]. Cybersecurity incidents in these environments can lead
to substantial operational disruptions, financial losses, and
threats to human safety [17], [23]. The growing number of
control devices, coupled with inadequate physical security
and the shift away from industry-specific communication
standards, exacerbates these vulnerabilities [6], [13]. Consequently, ensuring robust cybersecurity measures for IACS is
paramount, as the implications of cyber threats extend beyond mere data breaches to potentially catastrophic impacts
on physical systems and human lives [12], [24], [26].
The IEC 62443 standards series provides a comprehensive
framework for securing industrial automation and control
systems, addressing cybersecurity needs throughout the system lifecycle—from initial design to decommissioning [9].
However, despite the robustness of these standards, their
practical implementation in diverse and dynamic industrial
environments remains challenging. Factors such as the rapid
pace of technological change, the complexity of integrating
new systems with legacy infrastructure, and the necessity for
continuous workforce training complicate the effective application of these standards [16]. Moreover, the evolution of
cyber threats necessitates adaptive cybersecurity frameworks
that can respond to real-time threats, highlighting the need for
ongoing research and development in this critical area [19],
[27].
The IDUNN project, funded by the European Commission, aims to bridge this gap by developing a comprehensive
cybersecurity framework for industrial environments. This
framework integrates lifecycle management principles, aligning with IEC 62443 standards series, and encompasses tools,
processes, and microservices designed to be interoperable
with existing Information and Communication Technology
(ICT) supply chains. Key components of the IDUNN framework include HEIMDAL, AMORA, THOR, ODIN, and
FRIGG, each addressing specific aspects of cybersecurity,
such as threat detection, vulnerability management, automated response, and resilience actions.
This paper explores the cybersecurity challenges inherent in Industry 5.0 manufacturing operations and presents
the methodologies and tools developed under the IDUNN
project. We conduct a detailed cybersecurity gap analysis
aligned with the IEC 62443 standards series, propose enhancements to these standards based on our findings, and
demonstrate the practical application of the IDUNN framework through real-world use cases. By addressing the cybersecurity gaps and providing practical solutions, this paper
contributes to the ongoing efforts to secure industrial environments against evolving cyber threats, ensuring the resilience
and safety of critical infrastructure in the era of Industry 5.0.
Key Contributions: This paper presents an integrated cybersecurity framework for Industry 5.0 IACS, closely aligning
with the IEC 62443 standards. By combining vulnerability
detection, threat intelligence, automated response, and lifecycle management, the IDUNN project bridges theoretical
guidelines and practical implementation. This approach addresses challenges such as legacy integration and limited
resources in industrial settings.
II. BACKGROUND
Industry 5.0 emphasizes the collaboration between humans
and machines, integrating advanced technologies such as
artificial intelligence, robotics, and the Internet of Things.
This evolution enhances productivity and innovation but also
introduces new vulnerabilities and threats. Industrial Automation and Control Systems are critical to maintaining the
efficiency and safety of manufacturing operations [25]. However, the interconnected nature of these systems makes them
susceptible to cyber-attacks, necessitating robust cybersecurity measures [28]. The integration of cybersecurity measures
in IACS is crucial for ensuring the security and resilience of
critical infrastructure, especially in the context of Industry
5.0. The IEC 62443 standards series plays a fundamental
role in defining security protocols for IACS within various
industries, including power systems [18]. These standards
provide a comprehensive framework for implementing security requirements and controls to safeguard industrial control
systems from cyber threats [21]. By following the guidelines
outlined in the IEC 62443 standards series, organizations
can establish a defense-in-depth cybersecurity approach that
includes multiple layers of protection to effectively mitigate
risks [18].
The security maintenance of Industrial Internet of Things
(IIoT) systems and components is a critical area of focus
in the domain of the IIoT. In terms of industrial security,
the IEC 62443 standards series offers valuable insights into
managing security issues and software updates in the IIoT
era, providing guidelines for the implementation of robust security processes [21]. This emphasis on continuous security
maintenance aligns with the evolving nature of cyber threats
and the need for proactive security measures to safeguard
interconnected industrial systems.
The significance of cybersecurity in critical infrastructure
resilience is underscored by the identification of cybersecurity capabilities derived from frameworks such as COBIT®, CIS®, IEC 62443, ISO/IEC 27002, and NIST Special Publication 800-53. These capabilities, operationalized
through cybersecurity controls, play a vital role in fortifying
the security defenses of critical infrastructure systems [20].
Leveraging established cybersecurity frameworks such as
IEC 62443 enables organizations to strengthen their cybersecurity capabilities and enhance the resilience of critical
infrastructure against cyber threats.
In the context of DevSecOps practices, validating the
requirements of standards such as IEC 62443-4-2 in an
automated fashion presents challenges that necessitate expert
knowledge and the integration of security tools into the development pipeline [10]. Addressing these challenges requires
a comprehensive approach to automating the validation of
standard component requirements, ensuring compliance to
established cybersecurity standards throughout the development lifecycle.
Furthermore, the design and implementation of cybersecurityaware network architectures for industrial control systems
are guided by standards like the IEC 62443 series and
recommendations from the National Institute of Standards
and Technology (NIST). These guidelines emphasize the importance of designing secure network infrastructures to mitigate cyber risks and enhance the overall security posture of
industrial control systems [8]. By following the best practices
outlined in these standards, organizations can proactively
address cybersecurity concerns in industrial environments.
The division of industrial network environments into levels, as defined by the IEC 62443 standards series, facilitates
the implementation of role-based access control models in
systems like Modbus SCADA. This approach enables organizations to enforce granular access controls based on predefined roles, enhancing the security of industrial networks
and SCADA systems [7]. Leveraging role-based access control models that align with established standards enables
organizations to strengthen the security of their industrial
environments and control systems.
In the era of Industry 5.0, cybersecurity plays a pivotal
role in safeguarding data and ensuring the resilience of
embedded systems within industrial settings. The adoption
of robust cybersecurity measures is essential for protecting
industrial assets and maintaining the integrity of critical
processes [14]. Implementing cybersecurity frameworks such
as the IEC 62443 standards series empowers organizations to
navigate Industry 5.0 complexities and effectively mitigate
cyber risks.
Therefore, the integration of cybersecurity standards such
as the IEC 62443 standard series is paramount for enhancing the security stance of industrial automation and control
systems in the Industry 5.0 landscape. Adopting established
security frameworks empowers organizations to strengthen
their defenses against ever-changing cyber threats, safeguard
critical infrastructure, and ensure the resilience of industrial
systems in a connected digital ecosystem. This paper aims
to explore the cybersecurity challenges of Industry 5.0 and
present the methodologies and tools developed under the
IDUNN project. We will provide a detailed overview of the
IDUNN framework, discuss relevant cybersecurity standards,
conduct a gap analysis, and propose strategies for effective
implementation. Additionally, we will present best practices
and case studies to demonstrate the practical application
and effectiveness of the IDUNN framework in real-world
scenarios. Finally, we will propose specific adjustments to
the IEC 62443 standards series based on our findings and implementations, contributing to the ongoing efforts to enhance
cybersecurity in industrial environments. This paper intends
to improve the existing knowledge of industrial cybersecurity, offering valuable insights for researchers, practitioners,
and policymakers dedicated to enhancing the security of
industrial automation and control systems.
III. THE IDUNN PROJECT OVERVIEW
The IDUNN project, funded by the European Commission,
represents a significant effort to address the complex cybersecurity challenges facing the IACS in the era of Industry 5.0.
The primary objective of IDUNN is to enhance the security
and trustworthiness of industrial systems by developing a
comprehensive cybersecurity framework. This framework includes a suite of tools, processes, and microservices designed
to be interoperable with existing Information and Communication Technology (ICT) supply chains, thereby creating a
dynamic and secure barrier for complex ICT and Operational
Technology (OT) ecosystems.
The IDUNN project aims to achieve several key objectives:
• Enhance Cybersecurity: Develop advanced tools and
methodologies to detect, mitigate, and respond to cyber
threats in industrial environments.
• Interoperability: Ensure that the developed tools and
processes can seamlessly integrate with existing ICT
and OT systems.
• Resilience: Increase the Resilience of industrial systems
to cyber-attacks through proactive threat detection and
response mechanisms.
• Standardization: Align the developed solutions with
international cybersecurity standards, such as the IEC
62443 standard series, to facilitate widespread adoption
and compliance.
Key Components of the IDUNN Project: The IDUNN
project contains several key components, each addressing
specific aspects of Cybersecurity for industrial systems.
These components include:
A. HEIMDAL
HEIMDAL is an automated threat detection and identification tool. It manages software inventory and identifies
publicly reported vulnerabilities, alerting system operators to
potential threats. HEIMDAL consists of several subsystems:
• Scheduling Subsystem: Manages configurations and
schedules data acquisition from various threat sources.
• Threatfinder Subsystem: Collects and formats data
from online vulnerability sources, storing it in the Vulnerability Database.
• Interoperability Subsystem: Facilitates communication within the system.
• Logging Subsystem: Records all events and activities.
• Virtual Endpoint Detection and Response (vEDR):
Detects real-time anomalies in isolated operational environments.
HEIMDAL’s focus is on identifying known vulnerabilities
via software inventories and SBOM-based checks.
B. AMORA
AMORA is designed for fingerprinting OT components and
ensuring interoperability within the industrial environment.
It operates as a subscription, reporting, and alert system
that tests interoperability and traceability solutions. AMORA
simulates cyber-attack scenarios using attack scripts to identify potential vulnerabilities and generates alerts based on
predictive security analysis.
In contrast, AMORA focuses on testing interoperability and simulating attack scenarios to detect system-level
and configuration-based anomalies. This role complements
HEIMDAL’s software-centric approach.
C. THOR
THOR is an advanced platform with two key components:
THOR Cyber Threat Intelligence (CTI) and THOR Analytics. These components work together to enhance threat
detection and mitigation across various environments by
employing machine learning and advanced data processing
techniques.
1) THOR CTI
THOR CTI focuses on predicting and mitigating cyber
threats by analyzing vast amounts of data from diverse
sources, including social media, the dark web, and the clear
web. It processes data in real-time to organize and identify
critical threat intelligence, providing actionable insights for
cybersecurity operations. Key features of THOR CTI include:
• Large-Scale Data Processing: Uses AI, natural language processing (NLP), and rule-based algorithms to
efficiently process and extract Indicators of Compromise (IOCs) from large datasets.
• Real-Time Data Streaming: Utilizes Kafka for the
continuous ingestion and processing of threat intelligence data streams, ensuring up-to-date situational
awareness.
• Integration with Elastic Stack: Facilitates the indexing, searching, and visualization of processed threat
intelligence data through Elasticsearch and Kibana, allowing for efficient querying and analytics.
• Cross-Platform Data Sources: Gathers threat intelligence from open-source intelligence (OSINT) platforms, dark web monitoring, and social media channels
to provide a holistic view of emerging threats.
2) THOR Analytics
THOR Analytics complements the CTI component by providing anomaly detection and deep analytics for network
traffic and endpoint logs. It uses machine learning models to
detect abnormal patterns in network activities and performs
real-time analysis to identify potential threats. Key features
of THOR Analytics include:
• Anomaly Detection: Employs advanced machine learning models to detect network traffic anomalies and suspicious activities, offering real-time alerts and insights
into potential cyber incidents.
• Log Data Collection and Processing: Collects logs
from endpoints within OT/IOT networks, processes
them in a centralized system, and stores them for further
analysis.
• Synthetic Data Generation: Leverages Generative Adversarial Networks (GANs) to create synthetic datasets,
enhancing model training and reducing false positives
in anomaly detection.
• Explainable AI (XAI): Integrates XAI to provide transparency in the anomaly detection process, helping users
understand the reasoning behind detected anomalies and
machine-generated alerts.
• Interoperability of Explainability: Utilizes generative
AI methods to ensure that the reasoning behind IDS
decisions is consistently communicated across IDUNN
components, thereby improving transparency.
• Integration with Other IDUNN Tools: Collaborates
with tools like HEIMDAL and AMORA to create a
comprehensive threat detection ecosystem, providing
enriched security insights through collaborative data
sharing and analysis.
D. ODIN
ODIN is responsible for implementing resilience actions
based on threat intelligence. It manages security alerts and
transforms them into actionable insights to enhance decisionmaking in Resilience. ODIN’s tasks include:
• Case Escalation: Prioritizes and manages the severity
of security alerts.
• Alert Enrichment: Adds context to security alerts to
improve response strategies.
• Execution of Resilience Actions: Implements measures to mitigate and respond to security threats.
For smaller organizations, ODIN offers configurable playbooks that enable partial automation of incident response
without requiring highly specialized expertise.
E. FRIGG
FRIGG focuses on methodologies, metrics, and visualization. It collects Key Performance Indicators (KPIs), Key
Risk Indicators (KRIs), and Key Financial Indicators (KFIs)
from IDUNN-created microservices. FRIGG provides data
visualizations, dashboards, and widgets to communicate the
security posture of the organization. It also uses generative
ML models to create synthetic data for cybersecurity incident
simulations.
Integration and Interoperability
The IDUNN framework emphasizes interoperability, ensuring that each tool and component can seamlessly integrate
with existing systems and workflows. The tools are designed
to work together, providing a holistic approach to cybersecurity that covers detection, analysis, response, and Resilience.
One key aspect of limiting disruptions is the microservicesbased design. Components such as HEIMDAL or AMORA
can be introduced first in test environments and later transitioned into production with minimal changes. Standard communication interfaces (e.g., REST, AMQP) ensure compatibility with existing OT/IT security solutions. In addition, all
data flows are secured via encryption, and local deployment
options are available to protect sensitive data.
F. USE CASES AND APPLICATIONS
The IDUNN project has been applied and refined in various
real-world use cases to address specific challenges across different industries. These use cases demonstrate the practical
applicability and effectiveness of the IDUNN framework in
enhancing Cybersecurity for industrial systems. Notable use
cases include:
• Production of Gas Valves for Residential Use in the
Energy Industry: Ensures safety, dependability, and
compliance with industry standards for residential gas
valves.
• Manufacturer of Manufacturing Machinery: Automotive Hydraulic and Mechanical Presses: Guaran
tees precision and reliability in manufacturing processes
in the automotive sector.
• IoT Edge Computing Controller - Wind Energy
Plant Aviation Lighting: Validates compliance of IoT
controllers with industry standards for critical infrastructure projects.
G. COLLABORATION AND PARTNERSHIP
The success of the IDUNN project is built on collaboration
with prestigious partners that bring together knowledge and
expertise from top organizations. Key partners include:
• IKERLAN: is an R+D+I center owned by Mondragon
Corporation and is a premier technical hub for knowledge transfer that offers businesses competitive value.
• S21Sec: is a worldwide company that specializes in
cybersecurity technology and services, with an emphasis on ensuring business continuity and safeguarding
important digital assets in enterprises.
• Fagor Arrasate: is a global pioneer in the development
and production of customized material-forming technologies that make it possible to produce intricate pieces
composed of metal, composites, or thermoplastics.
• GAIA: is Basque Country’s Association of Knowledge
and Applied Technology Industries, which represents
more than 310 ICTA businesses, including cybersecurity firms in Spain.
• University of Oulu: A leading Finnish research university, excelling in technology, science, health, and
humanities, and driving innovation and sustainable development through global collaboration.
• Bittium: is a Finnish company that specializes in creating dependable, secure networking and communications
solutions by utilizing cutting-edge radio communication
technologies.
• Mondragon Assembly: is a global organization with a
focus on assembly and automation solutions development (France).
• OFFIS: is an internationally recognized information
technology research and development institute with an
emphasis on IT research and development, situated in
Oldenburg, Lower Saxony (Germany).
• DIN: The German Institute for Standardization is the
independent platform for standardization in Germany
and worldwide.
• CoSynth: A German spin-off firm specializing in embedded hardware/software system design.
H. FUTURE DIRECTIONS
The IDUNN project successfully refined and expanded its
capabilities to address emerging cybersecurity threats and
challenges in industrial environments. While the project has
concluded, its outcomes provide a strong foundation for future advancements in the field. Potential directions for further
development include:
• Enhancement of AI and ML Capabilities: Improving
the accuracy and efficiency of threat detection and response mechanisms.
• Scalability and Flexibility: Ensuring that the IDUNN
framework can adapt to different industrial contexts and
scale according to the size and complexity of the system.
• Standardization Efforts: Disseminating the outcomes
of the IDUNN project by transferring its findings to the
development of international cybersecurity standards,
promoting widespread adoption and compliance.
Therefore, the IDUNN project provides a comprehensive
and interoperable cybersecurity framework that addresses
the unique challenges of securing industrial automation and
control systems in the era of Industry 5.0. By leveraging
advanced tools and methodologies, the project enhances the
Resilience and security of industrial systems, ensuring their
safety and reliability in an increasingly connected and digital
world.
IV. CYBERSECURITY STANDARDS AND FRAMEWORKS
Adhering to industry-specific compliance frameworks is essential for harmonizing cybersecurity guidelines with the
unique requirements of OT systems. This section provides a
comprehensive description of key standards and frameworks
relevant to the IDUNN project.
A. IEC 62443 STANDARDS SERIES
The IEC 62443 standards series enhances the cybersecurity
of IACS through a comprehensive framework that protects
these systems against cyber threats throughout their lifecycle,
from design to maintenance. This standard series, consisting
of thirteen documents grouped into General, Policies and
Procedures, System, and Component sections [2], underscores a holistic strategy that integrates cybersecurity measures seamlessly at each stage of the industrial process and
associated devices. The IEC 62443 standards prioritize risk
assessment, security policies, and the deployment of robust
security controls customized to suit the needs of industrial
environments.
B. NIST CYBERSECURITY FRAMEWORK (CSF)
The NIST Cybersecurity Framework (CSF) [22] provides
guidelines and best practices to help organizations improve
their cybersecurity resilience through a structured approach
for evaluating and enhancing cybersecurity capabilities. The
framework encompasses core functions—Identify, Protect,
Detect, Respond, and Recover—and provides categories and
subcategories that outline precise cybersecurity activities and
outcomes [22].
C. ALIGNING NIST CSF DOMAINS WITH THE IEC 62443
STANDARDS SERIES
The Identify function within the NIST Cybersecurity Framework is focused on understanding an organization’s cybersecurity threats and vulnerabilities. This is in alignment with
IEC 62443-2-1 [1], which emphasizes the identification and
assessment of security risks in industrial automation and
control systems. The Protect function is dedicated to implementing protective measures to safeguard critical assets,
corresponding to the guidance provided by IEC 62443-3-3
[3] on the deployment of security controls in these systems.
Additionally, the Detect function prioritizes the swift identification of cybersecurity incidents, mirroring the requirements of IEC 62443-2-3 [4] for the timely detection of security events in industrial control environments. The Respond
function underscores the importance of having established
response plans for cybersecurity incidents, which aligns with
the directives of IEC 62443-3-2 [5] concerning incident
response and recovery in industrial automation and control
systems. Finally, the Recover function focuses on restoring
capabilities after a cybersecurity incident, consistent with the
recovery and restoration measures outlined in IEC 62443-3-3
[3] for industrial automation and control systems.
D. CYBERSECURITY CAPABILITY MATURITY MODEL
(C2M2)
The Cybersecurity Capability Maturity Model (C2M2), developed by the U.S. Department of Energy (DoE), serves
as a comprehensive tool to monitor cybersecurity practices
in both IT and OT within the energy sector. The C2M2
evaluates an organization’s cybersecurity capabilities across
ten distinct domains, identifying areas needing improvement
[29]. Aligning C2M2 with the IEC 62443 standards series
ensures that cybersecurity practices are tailored to the unique
requirements of industrial environments, enhancing defenses
against cyber threats.
E. ALIGNING C2M2 DOMAINS WITH THE IEC 62443
STANDARDS SERIES
To provide a clear understanding of how C2M2 domains map
to the IEC 62443 standards, Table 1 presents a comparative
analysis. This alignment illustrates how various cybersecurity capability domains are addressed within the IEC 62443
framework, facilitating integrated and comprehensive cybersecurity strategies.
V. CYBERSECURITY GAP ANALYSIS
This section provides a detailed analysis of the current gaps
in cybersecurity practices for IACS within Industry 5.0 manufacturing operations. The analysis is aligned with the IEC
62443 standards series and the C2M2 framework, ensuring a
comprehensive understanding of the deficiencies and areas
for improvement. As shown in Figure 1, addressing these
gaps requires a structured approach to analyze the current
state of cybersecurity, define the desired future state, and
identify the gap between them. Insights from previous cybersecurity efforts can guide the development of an action
plan to improve cybersecurity resilience, which is critical for
achieving compliance with standards like IEC 62443.
FIGURE 1: Cybersecurity gap analysis in the IDUNN project
A. IDENTIFICATION OF GAPS IN CURRENT
CYBERSECURITY PRACTICES
Despite significant advancements in cybersecurity measures,
several gaps persist in the practical implementation of secure
systems within industrial environments. These gaps are often
due to complex IT/OT integrations, evolving threat landscapes, and resource constraints. Key gaps identified include:
• Lack of Comprehensive Threat Intelligence: Many
industrial systems lack access to up-to-date and comprehensive threat intelligence, which is crucial for anticipating and mitigating emerging cyber threats.
• Inadequate Vulnerability Management: Existing
practices for identifying and managing vulnerabilities
are often insufficient, particularly in detecting and addressing zero-day vulnerabilities.
• Insufficient Automated Response Mechanisms:
There is a notable deficiency in automated response
mechanisms that can quickly and effectively neutralize
detected threats without significant human intervention.
• Integration Challenges: Integrating various cybersecurity tools and ensuring their interoperability remains
a significant challenge, leading to fragmented and less
effective security measures.
• Compliance with IEC 62443 standards series: While
the IEC 62443 standards series provides a robust framework, many organizations struggle with the practical aspects of implementing these standards comprehensively
across their operations.
B. COMPARATIVE ANALYSIS WITH IEC 62443
STANDARDS SERIES
The IEC 62443 standards series is designed to provide a comprehensive framework for securing industrial automation and
control systems. However, practical implementation often
reveals several gaps. This section compares current practices
with the requirements of the IEC 62443 standards, as shown
in Table 2.
C. RECOMMENDATIONS FOR BRIDGING IDENTIFIED
GAPS
To address these gaps and enhance the cybersecurity resilience of IACS in Industry 5.0, we propose the following
recommendations aligned with both the IEC 62443 standards
series and the C2M2 framework:
• Enhanced Threat Intelligence Integration: Develop
and integrate advanced threat intelligence platforms,
such as THOR, that leverage machine learning and data
analytics to provide real-time threat intelligence and
proactive threat detection.
• Improved Vulnerability Management: Implement
comprehensive vulnerability management tools like
HEIMDAL, which can automate the detection and remediation of vulnerabilities, including zero-day threats.
• Automated Response Mechanisms: Deploy automated
response systems like ODIN to execute resilience actions quickly and effectively, reducing reliance on manual intervention.
• Seamless Tool Integration: Ensure seamless integration of various cybersecurity tools through interoperable
frameworks, as demonstrated by the IDUNN project, to
enhance overall security posture.
• Practical Implementation of IEC 62443 standards
series: Provide detailed guidelines and practical steps
for implementing the IEC 62443 standards across all
aspects of industrial operations, supported by tools like
AMORA and FRIGG for continuous monitoring and
compliance.
• Alignment with C2M2: Utilize the alignment between
C2M2 and the IEC 62443 standards series to ensure comprehensive coverage of cybersecurity capabilities, enhancing risk management and incident response
strategies.
Addressing these gaps and implementing the proposed
recommendations can significantly enhance an organization’s
cybersecurity resilience. This approach ensures robust protection for industrial systems and contributes to the safety,
reliability, and trustworthiness of critical infrastructure in
Industry 5.0.
VI. METHODOLOGY
A. LIFECYCLE MANAGEMENT FOR CYBERSECURITY
EVENTS
The IEC 62443 standard series is paramount for cybersecurity in industrial automation and control systems. It provides
a comprehensive framework for protecting industrial systems
against a wide range of cyber threats. Within the IDUNN
project, lifecycle management principles from IEC 62443-
4-1 have been integrated to ensure compliance and enhance
security across all phases of system development and operation.
1) IEC 62443-4-1 Lifecycle
The lifecycle, as defined in IEC 62443-4-1, focuses on the
processes and practices that manufacturers must follow to
develop secure products, encompassing systems and components. This lifecycle is divided into several phases:
1) Specification of Security Requirements: Defining the
security needs of the product or system, identifying
potential threats and vulnerabilities, determining the
impact of security breaches, and setting security objectives.
2) Secure by Design: Incorporating security measures
during the design phase, including secure coding practices, threat modeling, and security reviews.
3) Secure Implementation: Developing the product with
security in mind, following secure coding guidelines,
using security tools, and ensuring third-party components do not introduce vulnerabilities.
4) Security Verification and Validation Testing: Testing
the product to ensure it meets the specified security
requirements through security testing, vulnerability assessments, and penetration testing.
5) Management of Security-Related Issues: Managing
and responding to security incidents and vulnerabilities
throughout the product lifecycle, including receiving
notifications, disclosing security-related problems, and
periodically reviewing security defect management
practices.
6) Security Update Management: Developing and releasing security updates to address known vulnerabilities, mitigate risks, and ensure continued security and
reliability.
7) Security Guidelines: Creating documentation and
guidelines to ensure consistent application of security
measures, including instructions for secure installation,
configuration, and operation.
2) Lifecycle Management in the IDUNN project
The IDUNN tools contain various stages of the cybersecurity
lifecycle, ensuring a continuous and comprehensive approach
to cybersecurity. The lifecycle management within IDUNN is
depicted in Fig. 2 and involves the following steps:
1) Asset Identification (AMORA): Identifying and documenting the system’s assets, including the software bill
of materials (SBOM).
2) Vulnerability Management (HEIMDAL): Conducting surveillance and assessing the impact of identified
vulnerabilities.
3) Vulnerability Testing (THOR): Detecting potential
weaknesses using techniques like smart fuzzing and
finding IoCs and network vulnerabilities.
FIGURE 2: Lifecycle of IDUNN tools
4) Incident Management and Response (ODIN): Mitigating incident impact by enriching, assessing, and
reacting to them.
These stages ensure that cybersecurity measures are maintained throughout the system’s lifecycle, addressing both
proactive and reactive measures.
B. APPROACHES AND METHODOLOGIES FOR
CAPTURING SECURITY REQUIREMENTS
Capturing security requirements is essential for developing
robust cybersecurity measures. IDUNN employs two primary
methodologies aligned with the IEC 62443 standards series:
1) Misuse Case (MUC) Template
The Misuse Case Template, aligned with the IEC 62559-2
standard [11], outlines fundamental principles for constructing risk scenarios that encapsulate security requirements
effectively. This template records potential attack scenarios
from the adversary’s perspective, considering the probability
of environmental disruptions that might result in unfavorable
consequences.
The primary emphasis is on promoting timely detection
and detailed analysis of cyber threats, facilitating the development and implementation of effective mitigation strategies.
This proactive approach minimizes risks to acceptable levels
during the system design phase. Additionally, the misuse
case methodology highlights non-functional requirements,
specifically safety requirements, emphasizing the identification and remediation of potential system vulnerabilities early
in development.
2) Distributed Simulation (DS)
Integrating Distributed Simulation (DS) into the IDUNN
project leverages advanced simulation techniques to enhance
performance and improve the quality of cybersecurity measures. This approach unfolds through three pivotal phases:
1) Planning Phase: Defining the components of the simulation environment and outlining their interactions to
establish an effective distributed simulation system.
2) Development Phase: Transforming simulation design
concepts into functional elements, integrating communication protocols, and ensuring the smooth operation
of the distributed simulation system.
3) Experimentation Phase: Verifying system performance, analyzing simulation data, and validating the
accuracy of results through various simulation scenarios.
3) Combined Methodologies: MUC and DS
The integration of Misuse Case Templates and Distributed
simulation techniques provides a comprehensive approach
to capturing and analyzing security requirements. The combined methodologies are summarized in Table 3.
C. INTEGRATION OF IDUNN TOOLS
The integration of IDUNN tools is essential for establishing a comprehensive cybersecurity framework. The IDUNN
project has developed a set of tools to address different aspects of cybersecurity, such as vulnerability detection, threat
intelligence, automated response, and resilience actions. The
tools are interconnected to facilitate smooth communication
and coordination across cybersecurity processes, improving
the overall security of the systems.
1) Components Functionality
The functionality of the IDUNN components can be roughly
divided into online and offline functionalities. Offline functionalities include IOC scraping, cataloging, analysis, system scraping, vulnerability detection, and analysis. Online
functionalities encompass anomaly detection and analysis in
live networks and systems, as well as subsequent analysis,
response to, and visualization of security events.
While ODIN, FRIGG, and SIEM focus solely on online
functionalities, THOR, HEIMDAL, and AMORA possess
both offline and online capabilities. Specifically:
• THOR: Focuses on IOCs and the detection and analysis
of network-based security events.
• HEIMDAL: Analyzes system components and detects
anomalies in both networks and systems.
• AMORA: Validates system and interoperability offline,
and detects system anomalies.
Comprehensive data flows between the IDUNN components are depicted in Fig. 3. THOR, AMORA, and HEIMDAL receive data from the monitored system and the Internet, while FRIGG, ODIN, and SIEM rely on data flows
refined by THOR, AMORA, and HEIMDAL.
2) Data Flows
Fig. 4 illustrates the data flows between the IDUNN components. Data originates from the Internet (IOCs) and the
monitored system (both online and offline network and system data). THOR, AMORA, HEIMDAL, and SIEM analyze
this data for potential vulnerabilities, anomalies, and security
events. The analyses are further sent to ODIN for decisionmaking on potential resilience actions and to FRIGG for
visualization.
VII. BEST PRACTICES AND CASE STUDIES
This section outlines industry best practices implemented
across various use cases and describes how these practices
were enforced in real-world scenarios. The practical application of cybersecurity measures is critical for ensuring
the robustness of industrial systems against evolving cyber
threats.
A. INDUSTRY BEST PRACTICES
The IDUNN consortium has leveraged the tools developed
throughout the project to implement a set of industry best
practices aimed at managing the cybersecurity event lifecycle
of industrial systems. These measures have been applied
across different real-world use cases, such as a gas valve
manufacturing line, an automobile parts production line, and
a wind turbine lighting system. The best practices common
to all these use cases include the following phases:
1) Identification and Protection Phase
• Initial Setup: Data collection of the system, including automatic collection of vulnerabilities from public
databases by HEIMDAL and web scraping by THOR
for Indicators of Compromise across the clear, dark, and
deep webs.
• System Configuration: Semi-automated steps include
setting up AMORA on system devices, inserting device
SBOMs into HEIMDAL’s asset management system,
and training HEIMDAL’s Virtual Endpoint Detection
and Response (vEDR) with normal operational network
traffic.
2) Detection Phase
• Host-Level Monitoring: AMORA monitors file integrity by checking for file tampering in directories and
evaluating telemetry data for anomalies.
• Vulnerability Detection: HEIMDAL analyzes host
components to detect new vulnerabilities.
• Network-Level Monitoring: HEIMDAL’s vEDR identifies anomalous packets using a machine learning
model trained on normal operational data.
• Anomaly Detection: THOR conducts anomaly detection and smart fuzzing attacks to uncover exploitable
vulnerabilities.
3) Response Phase
• Automated Incident Response: ODIN processes incoming alerts using Security Orchestration, Automation, and Response (SOAR) techniques to determine
necessary resilience actions.
TABLE 3: Misuse Case Template and Distributed Simulation
Misuse Case (MUC) Template Distributed Simulation (DS)
Scenario Construction Planning Phase
• Develop hypothetical attack scenarios that encompass various
levels of complexity, attacker expertise, intent, and capabilities.
• Consider potential environmental disruptions that might result in
unfavorable consequences.
• Define the components of the simulation environment and outline
their interactions.
• Establish a coherent and effective distributed simulation system.
Adversarial Perspective Development Phase
• Adopt the mindset of a potential attacker to identify vulnerabilities that may not be apparent from a defensive standpoint.
• Evaluate fictional attack scenarios such as phishing attacks, ransomware infections, DDoS attacks, insider threats, and social
engineering tactics.
• Transform simulation design concepts into functional elements.
• Integrate communication protocols and ensure the smooth operation of the distributed simulation system.
• Conduct hypothesis testing to explore any unexpected behaviors
during simulation execution.
Risk Analysis and Mitigation Experimentation Phase
• Perform timely detection and detailed analysis of cyber threats.
• Develop and implement effective mitigation strategies to minimize risks to an acceptable level during the design phase.
• Highlight non-functional requirements, specifically safety requirements, to identify and remedy potential system vulnerabilities early.
• Verify system performance, analyze simulation data, and validate
the accuracy of results.
• Execute different simulation scenarios to observe the system’s
behavior under various conditions.
• Mitigation Actions: Resilience actions carried out by
AMORA, HEIMDAL, and THOR include blocking network traffic, closing TCP or UDP ports, and restoring
filesystem integrity.
4) Monitoring and Evaluation
• Data Visualization: FRIGG provides a visual interface
for system administrators, collecting data from other
IDUNN tools and displaying it on dashboards.
• Performance Indicators: Dashboards include Key Performance Indicators (KPIs) and Key Risk Indicators
(KRIs) to monitor operational levels.
• Detailed Analysis: HEIMDAL and THOR interfaces
offer further details on detected vulnerabilities and
IoCs, with THOR featuring a specialized large language
model-based chatbot for cybersecurity interpretability
and explanations.
5) Self-Diagnosis and Testing
• Attack Scenario Simulation: FRIGG generates diverse
attack scenarios and test data using a data mutation
module powered by machine learning models to continuously evaluate the system’s resilience and functionality. This ensures the system operates as expected
and adapts to emerging threats by simulating various
cyberattack scenarios and testing the effectiveness of
intrusion detection and response mechanisms.
B. CASE STUDY: COSYNTH USE CASE
The CoSynth use case involves an Aviation Detection Lighting System (ADLS) installed in wind turbines. This system
marks turbines as obstacles during nighttime for nearby
aircraft, thereby preventing collisions. The architecture and
cybersecurity implementation using the IDUNN toolchain
are detailed below.
1) System Architecture
• Operational Zones: The ADLS operates in two main
zones: the turbine environment and the control center,
connected via a VPN.
• Control Center: Monitors and collects data from all
deployed ADLS systems, allowing operators to conduct
configurations and updates.
• ADLS Controller: In each turbine, an ADLS Controller
receives flight data and determines lighting needs, commanding the Light Controller to adjust lighting as necessary.
2) Cybersecurity Implementation
• SBOM Integration: Turbine devices’ SBOMs were
integrated into AMORA and HEIMDAL to prevent tampering and analyze software dependency vulnerabilities.
• Anomaly Detection: HEIMDAL’s Virtual EDR was
trained on normal operational traffic to detect network
anomalies.
• IOC Analysis: THOR was implemented to detect and
compare network IoCs with those collected via web
scraping.
• Automated Response: ODIN, installed in the control
center, receives alerts via AMQP queues, evaluates
severity, and instructs IDUNN tools in the turbine to
execute resilience actions.
• Visualization: FRIGG, deployed in the control center,
allows operators to monitor and evaluate security incidents in the ADLS systems.
C. ADDITIONAL CASE STUDIES
1) Production of Gas Valves for Residential Use in the
Energy Industry
In the energy sector, ensuring that gas valves used in residential applications meet stringent safety and quality standards is
critical. By implementing the IDUNN toolchain, manufacturers can automatically detect and respond to vulnerabilities in
their production systems, ensuring compliance with industry
standards and enhancing product safety.
2) Automobile Parts Production Line
Automotive manufacturing relies heavily on precision and
reliability. The integration of IDUNN tools in the production
line of hydraulic and mechanical presses ensures that any
cybersecurity threats are promptly detected and mitigated,
maintaining the integrity of the manufacturing process and
preventing potential disruptions. Therefore, the implementation of best practices within the IDUNN project ensures a
comprehensive approach to cybersecurity in industrial systems. By automating threat detection and response, maintaining continuous monitoring, and leveraging advanced analytics, IDUNN enhances the resilience and security posture of
industrial environments. These best practices not only align
with the IEC 62443 standards but also demonstrate practical
solutions to real-world cybersecurity challenges.
VIII. RECOMMENDATIONS FOR ENHANCING THE IEC
62443 STANDARDS SERIES
Based on the findings and initiatives of the IDUNN project,
we propose several recommendations to improve the usability and effectiveness of the IEC 62443 standards series in
modern industrial settings. These recommendations aim to
fill gaps in implementation guidance and ensure that the standards can adapt to the ever-changing nature of cybersecurity
threats in industrial systems.
1) Detailed Implementation Guidance
• Develop comprehensive guidelines for the practical application of the IEC 62443 standards series in industrial
environments, similar to the CLC/TS 50701:2021-07
Rail Cyber Security Solutions standard.
• Include step-by-step procedures and case studies to
illustrate best practices for implementing security controls and managing cybersecurity lifecycles.
2) Enhanced Risk Management Frameworks
• Integrate advanced risk management techniques and
tools like those developed in the IDUNN project
(AMORA, HEIMDAL, THOR, ODIN, FRIGG) to provide dynamic risk assessment capabilities.
• Provide frameworks for continuous monitoring and real
TABLE 4: IEC 62443 Standards Series Proposals for Adjustment
Document Number Section Relation to
IDUNN Proposal for Adjustments (changes or additions)
IEC 62443-2-1 Definition
of an IACS Security Program
Section 12 - SPE7 Event
and Incident Management ODIN
• 12.2 Event and Incident Management: Tools like SIEM and SOAR for
incident detection and incident response may be added as additional
guidance.
IEC 62443-4-2 Technical
Safety Requirements for
IACS Components
Section 10 – FR 6 Timely
Response to Events ODIN
• 10.4 – CR 6.2 – Continuous Monitoring:
– 10.4.2 Rationale and Supplemental Guidance: SIEM is mentioned, but additional tools like SOAR for incident response may
be added.
– Additional tools for automation and orchestration (SOAR) may
also be added as supplemental guidance.
IEC 62443-3-3 System Security Levels and Requirements
Section 10 – FR6 Timely
Response to Incidents ODIN
• 10.4 SR 6.2 – Continuous Monitoring:
– 10.4.1 Requirement: The control system shall provide the capability to continuously monitor all security mechanism performance using commonly accepted security industry practices
and recommendations to detect, characterize, and report security
breaches in a timely manner.
– 10.4.2 Rationale and Supplemental Guidance: SIEM is mentioned, but additional tools like SOAR for incident response may
be added.
time risk assessment to adapt to emerging threats, ensuring that risk management remains proactive and responsive.
3) Incorporation of Advanced Technologies
• Update the IEC 62443 standards series to reflect the
use of machine learning, artificial intelligence, and other
advanced technologies for threat detection and response.
• Include guidelines on integrating these technologies into
existing industrial control systems, ensuring compatibility and enhancing security measures.
4) Focus on Incident Response and Resilience
• Strengthen sections on incident response and resilience
by incorporating insights from the IDUNN project’s use
of Security Orchestration, Automation, and Response
(SOAR) techniques.
• Emphasize the importance of automated and coordinated response actions to mitigate the impact of cyber
incidents, reducing reliance on manual intervention.
5) Standardization of Tool Integration
• Provide frameworks for the integration of various cybersecurity tools and systems to ensure interoperability
and effective communication, as demonstrated by the
IDUNN project.
• Encourage the development and adoption of standardized APIs and data exchange formats to facilitate seamless tool integration and enhance overall security posture.
A. IEC 62443 STANDARDS SERIES PROPOSALS FOR
ADJUSTMENT
To provide a detailed analysis of how the IEC 62443 standards series can be augmented with advanced incident response tools, Table 4 presents specific proposals based on the
IDUNN project’s insights.
Table 4 highlights targeted adjustments to the IEC 62443
standards series, emphasizing the integration of advanced
incident response tools to enhance the effectiveness of event
and incident management procedures. The integration of advanced tools like ODIN within the IEC 62443 framework significantly enhances the standards’ ability to address modern
cybersecurity challenges. By integrating SIEM and SOAR
tools, the standards not only facilitate real-time incident
detection and response but also streamline the automation of
resilience actions. This augmentation ensures that industrial
systems can swiftly mitigate the impact of cyber threats,
thereby maintaining operational continuity and safeguarding
critical infrastructure. Furthermore, the emphasis on continuous monitoring aligns with the dynamic nature of cyber
threats, ensuring that security mechanisms remain practical
and up-to-date.
IX. CONCLUSION
X. CONCLUSION
This study examined the cybersecurity landscape for industrial automation and control systems within Industry 5.0
manufacturing environments, leveraging insights from the
IDUNN project. Funded by the European Commission, the
IDUNN project is a key case study showcasing the practical
deployment of advanced cybersecurity tools and methodologies such as AMORA, HEIMDAL, THOR, ODIN, and
FRIGG. These tools collectively strengthen the cybersecurity framework of industrial systems by addressing critical
areas, including vulnerability detection, threat intelligence,
automated response, and resilience actions. By aligning with
the IEC 62443 standards series, the IDUNN project enhanced
the cybersecurity resilience of industrial operations. The
real-world application, particularly illustrated through the
CoSynth Use Case, highlights the practical challenges and
effective solutions in implementing a comprehensive cybersecurity strategy for critical infrastructure. This highlights the
necessity of a proactive and integrated approach to cybersecurity, utilizing cutting-edge technologies to protect essential
assets. Although IDUNN focuses on cybersecurity measures,
it is important to note that industrial facilities should also
maintain robust physical security. Integrating cyber defenses
with physical security controls is essential for a comprehensive risk management strategy. The proposed enhancements
to the IEC 62443 standards series aim to bridge existing
gaps and ensure that these standards remain robust and
adaptive against evolving cyber threats. These recommendations contain detailed implementation guidance, advanced
risk management frameworks, incorporation of emerging
technologies, a focused approach to incident response and
resilience, and the standardization of tool integration. Eventually, this paper contributes to the ongoing efforts to secure
industrial environments by bridging the gap between current
cybersecurity guidelines and the emerging requirements of
Industry 5.0. The findings and recommendations presented
offer valuable insights for researchers, practitioners, and policymakers dedicated to enhancing the security and resilience
of industrial automation and control systems.
