Title: GATEKEEPER Platform: Secure Processing Environment for European Health Data Space

ABSTRACT The European Health Data Space (EHDS) is a significant initiative within the European Union
aimed at improving healthcare through better use of health data and collaboration. This involves sharing and
utilization of health data in a secure and interoperable manner across EU member states. With the advent
of modern technology, different types of health data are being acquired ranging from traditional electronic
health records to real-time wearable signals for improved healthcare delivery and management. However,
there are certain challenges associated with compliance to EHDS, such as secure continuous integration
(CI) and continuous delivery (CD), scalability and adaptability towards new technologies and applications,
tolerance against IoT cyber-attacks, requirement of advanced data storage methods, processing power,
interoperability solutions for data analysis and connectivity. In order to address these, a flagship project of
the European Commission, GATEKEEPER, represents a pioneering effort designed to transform healthcare
delivery through the utilization of sophisticated digital technologies. The architecture of the GATEKEEPER
platform has been meticulously crafted, in compliance with the EHDS, to integrate a multitude of data
sources, deploying advanced analytical tools to enable the development of novel solutions for the effective
prediction, detection, and management of chronic health conditions. GATEKEEPER addresses the aforementioned challenges by integrating collaborative tools for data management and consistency, machine learning
modelling and management tool, activity feeds and issue tracking tools with developers authentication,
CI/CD tools allowing, among others scalability in multiple formats, tools for assessing security, vulnerability
and dependency for third party packages.
INDEX TERMS CI/CD, data scalability, data security, European health data space, healthcare platform,
SecDevOps.
I. INTRODUCTION
The advent of modern key enabling technologies allows
us to acquire different types of health-related data; leading
towards revolutionizing healthcare. The health sector generates and utilizes a vast amount of data for various purposes,
including patient care, research, policy development, and
healthcare administration. Some key types of health data
include i) Electronic Health Records (EHRs) which contain
individual patient information (including medical history,
diagnostics medication); ii) Health Surveys such as lifestyle,
demographics and health behaviors; iii) Genomics data;
iv) Wearables and IoT Data which are able to collect, among
others real-time vital signs, activity levels, sleep patterns;
v) Imaging Data from medical devices such as MRI, CT scan
etc. Several different technologies (e.g. smart watches) along
with electronic health records are being acquired to analyze
and understand the health trajectories of different chronic
subjects.
Different types of health data require the use of different
key enabling technologies (KET), information and communication systems, and EHR to enhance healthcare delivery,
management, and patient well-being; the phenomenon collectively known as Digital Health [1]. It encompasses a wide
range of applications and tools designed to improve various
aspects of healthcare, from patient care to administrative
and research functions. Digital Health requires secure and
accurate processing, integration and dissemination for end
user (such as clinical practitioners, data scientists) to analyze
the individualized data and to develop the data driven models
for efficient digital health solutions while preserving personalized data integrity. In order to ensure these, there had been
some initiatives based on regularizing the practices of data
security, data sharing, interoperability under secure processing environments for efficient collaboration and innovation.
One of the key initiatives towards this direction is the
European Health Data Space (EHDS) [2] which is a significant initiative within the European Union aimed at improving
healthcare through better use of health data and collaboration.
It involves the sharing and utilization of health data in a
secure and interoperable manner across EU member states.
Article 50 of the General Data Protection Regulation (GDPR)
places the significant emphasis on the security of personal
data and EHDS must adhere to these regulations for secure
and accurate processing of health data (incl. anonymization or
pseudonymization) before enabling the collaboration among
different governments, healthcare providers, and technology
companies. In this context, a secure processing environment would be pivotal which would typically involve secure
servers and data centers, encryption, access controls, and
other security measures to protect patient data [3]. To achieve
this, standards for data exchange and processing environments need to be defined. This results in the need of a
platform driven by DevOps approach that is a set of practices,
principles, and cultural philosophies that aim to improve
and streamline the collaboration between software development (Dev) and IT operations (Ops) teams [4]. In DevOps,
all collaborators (incl. data processors, data controllers) are
allowed to cooperate with each other to continuously deliver
the analytical results and software in a shorter time. It also
incorporates feedback sent by the end users based on their
evaluation of the applications as it evolves its whole lifecycle; resulting in quicker change placement in the production
environment based on modification commitment [5]. However, practice of continuous collaborations among different
‘‘actors’’ have brought new challenges which need to be
addressed while being compliant with the data integrity and
security in order to support novel research and innovation in
regards to digital health solutions [1].
One of the key objectives for DevOps to be compliant
with EHDS is the delivery of security of operations to stakeholders [6]. This results in coining the term SecDevOps
which is characterized by a ‘‘Security by Design’’ approach.
It joins security practices to the development and operations
activities, with the clear objective of defending not only the
infrastructure where the software runs, but also on offering a
high-level protection for the involved data and personal information. The goal of the enlarged team made up of the security,
development and operation people is to create applications
in the shortest possible time, guaranteeing high quality and
security standards [6]. There had been couple of challenges
associated with existing state-of-the-art SecDevOps design.
i. Current SecDevOps state-of-the-art do not allow
EHDS compliance which require data security [7]
driven continuous integration (CI) and continuous
delivery (CD) due to limited studies on CI/CD security
with up-to-date automation tools, flexibility towards
adapting compliance requirements along with sufficient training and awareness for end users [8].
ii. Existing multi-cloud SecDevOps applications face
challenges in terms of concatenating scalability and
adaptability towards new technologies and applications [9] with portability, interoperability, compatibility and testing [10].
iii. EHDS compliant SecDevOps systems are required to
be tolerant against IoT cyber-attacks as well as user
specific services hosting and segregation [11], [12]
iv. Existing SecDevOps are not compliant with advanced
data storage methods, high processing power,
interoperability solutions for data analysis and
connectivity [13].
Within the context of implementing SecDevOps complaint
with EHDS, GATEKEEPER [14], a flagship project of the
European Commission, represents a pioneering effort to
establish an innovative big data platform for primary and
secondary use of data. GATEKEEPER project was designed
to transform healthcare delivery through the utilization of
sophisticated digital technologies, with a particular focus
on enhancing the autonomy and well-being of the elderly.
GATEKEEPER’s focus on the elderly reflects its relevance
to the WHO’s high-priority goal of healthy aging, addressing challenges like chronic conditions and isolation [15].
However, while tested in this context, the platform is suitable to broader population needs. The architecture of the
GATEKEEPER platform is meticulously crafted to integrate
a multitude of data sources, deploying advanced analytical
tools to enable the development of novel solutions for the
effective prediction, detection, and management of chronic
health conditions. At the heart of this endeavor is the project’s
architecture, which is engineered to enable the efficient collection, analysis, and interpretation of vast quantities of health
data. GATEKEEPER platform aims to address aforementioned challenges via novel contributions as follows:
i. Open Web Application Security Project (OWASP)
driven CI/CD multimode orchestrator tool to monitor
service (e.g. data, software etc.) building, deployment and security while regular checks for service
integration vulnerability (incl. broken authentication,
sensitive data etc.)
ii. Open shift policy hosted RESTful API which can allow
scalable and high performance while tenant/services
containerization and segregation
iii. Role-Based Access Control (RBAC) defining services
access based on organizational role and Demilitarized
Zone (DMZ) for untrusted traffic.
iv. Kubernetes for tenant specific service deployment with
high performance computing, storage and scalability.
II. STATE OF THE ART OF SECURE AND EFFICIENT
TECHNICAL SOLUTIONS
We start our literature search utilizing ‘‘DevOps’’ search term
which identified review articles focused on DevOps features
(automation, continuous delivery and fast feedback) with
less attention on quality models and quality metrics [16].
Another study outlines the direction for the future research on
architectural level support for self-adaptive security systems
for large-scale open environments [17]. We further expanded
our studies towards ‘‘SecDevOps’’ in order to expand our
studies in terms of automation, continuous delivery along
with data security. One of them identified shift-left security
and continuous security assessment as key recommended
practices [9]. Another study identified several benefits of
integrating compliance in SecDevOps, such as improved
security posture, reduced costs and risks, increased customer
satisfaction, and enhanced collaboration and communication
among stakeholders [18]. However, these studies recognized
some challenges of integrating compliance in SecDevOps,
such as lack of automation tools, complexity of compliance requirements, resistance to change, and insufficient
training and awareness. Another challenge associated with
SecDevOps was IoT cyber-attacks which was addressed
utilizing machine learning tools [11], [12]. However, the
lack of standard datasets, the trade-off between accuracy
and complexity, the scalability and adaptability issues, and
the need for more empirical studies made the robustness
questionable. For scalability, availability, performance and
cost optimization, one study identified multi-cloud native
applications [10] which were designed, developed, deployed
and operated over multiple cloud services types (public, private, hybrid) from different providers. However, the study
found lack of architectural models that address the design
and development challenges of multi-cloud native applications, such as portability, interoperability, compatibility, and
testing.
We further expanded our literature survey with microservices which is an architectural style that structures collection
of services that are independently deployable, loosely coupled, organized around business capabilities and owned by
small team. However, majority of these services suffer from
the weak support for detecting and managing changes, the
lack of autonomy, the weak expressiveness in the managed
services’ descriptions, the weak support for planning and
decision-making mechanisms, the high complexity, the lack
of transparency when performing adaptation, and the performance problems [19]. In addition, cloud-native systems
may be subject to various compliance and regulatory requirements, such as HIPAA, PCI, and GDPR.
Considering the architecture and implementation of a
cloud-native system, general attacks that can occur due to
security flaws in cloud-native architectures [20] the results
revealed that unauthorized access, sensitive data exposure
and compromising individual microservices are the most
treated and addressed threats by contemporary studies for
IoT attacks [21]. Additionally, it was found that most proposed solutions are applicable at soft infrastructure layer of
microservices. Moreover, the diversity of attacks is basically
due to the adoption of Zero Trust model [22] that suggests
affording no default trust to users, devices, applications,
or packets; instead, every action and entity need to be authenticated and authorized appropriately. Much emphasis is put on
authentication and authorization techniques. Therefore, it is
challenging to effectively monitor the security and behavior of microservice settings due to the high complexity of
small services. As the IoT continues to expand and grow,
monolithic implementation becomes even larger and much
more complex in nature [23]. It results in weak scalability,
maintainability and extensibility. Another IoT’s challenges
concerns the resources needed to store and measure the enormous amount of data resulting from connections between
devices. Cloud computing may tackle IoT problems however
industrial IoT can be significantly affected by composition
of RESTFul APIs. Besides, implementation of IoT does
not reflect the dynamism and weaknesses of service-based
environments.
In contrast to aforementioned state-of-the-art, the
GATEKEEPER platform implements the microservices
architecture while addressing the challenges related to service adoption and security. Given challenges associated
with encapsulation and containerization of edge devices
and software [24], [25], Gatekeeper platform implements
RBAC which is one of OWASP principles [26] allowing
service security with tenant containerization and cybersecurity. In contrast to existing microservices approaches,
GATEKEEPER platform does not incorporate Zero Trust
Model due to over emphasis on authentication and authorization. Also existing research faced challenges in terms of
unified view of data in distributed systems [27], machine
learning algorithms [28] and Quality of Service (QoS)
management [29]. GATEKEEPER platform addresses these
challenges via Open shift policy driven RESTful APIs and
OWASP based CI/CD tools. Besides, platform’s Kubernetes
oriented network allow encapsulate manufacturing equipment for rendering network heterogeneity [30], [31]. Other
solutions include service discovery; data management and
consistency; testing; performance prediction, measurement
and Optimization; communication and integration; service
orchestration; security; monitoring, tracing and Logging
(MTL).
III. METHODOLOGY
The GATEKEEPER project, a European Multi-Centric Pilot,
forms the foundation of our research methodology, focusing
on the integration of advanced ICTs to transform healthcare.
The project aims to create a trust-based platform connecting
healthcare providers, businesses, entrepreneurs, elderly citizens, and communities, with a particular focus on enhancing
independent living for aging populations. Aligned with the
EHDS objectives, GATEKEEPER emphasizes interoperability and reliable data utilization, providing the framework
for the methodologies outlined in this research. Through
its large-scale pilot operations across nine regions, GATEKEEPER supports the development of AI-driven solutions
for early detection and intervention, forming the basis for our
innovative approach to tackling healthcare challenges.
In order to address challenges associated with the current
SecDevOps systems and microservices to be implemented in
the digital health context, we developed our novel architecture which takes CI and CD approach for effective service
discovery, data management and consistency while keeping
the robust and secure support environment for microservices.
Besides, our platform architecture also supports RESTful services for efficient scalability, extensibility and interoperability of the platform. The goal of the enlarged GATEKEEPER
team made up of the SecDevOps, development and operation
people, is to create digital health in the shortest possible time,
guaranteeing high quality and security standards while being
compliant with EHDS. Therefore, methodology overview
starts with the detailed description of the EHDS followed
by CI/CD architecture inspired by EHDS. The details are as
follows:
A. EUROPEAN HEALTH DATA SPACE: BACKGROUND,
PRINCIPLES AND PILOT
The EHDS [32] is a proposed regulation to promote health
data exchange and support research and innovation which the
European Council has urged to accomplish. It is intended to
become a system for data exchange and access, governed by
common rules, procedures, and technical standards to ensure
health data can be accessed within and between Member
States and it aims to provide more accessible, more affordable
and safer healthcare also introducing innovation in the health
care system. It is aimed to facilitate use of health records
for research, innovation and policy making while securing
personal information and prohibiting its usage for commercialization purposes. It approaches four specific objectives
i.e. i) data secondary use, ii) foster participation of users,
iii) define services that must be used and iv) detail the architecture for future implementation.
The EHDS implementation faces multiple challenges
spanning interoperability, technology, governance, and economic constraints. While the initiative aims to harmonize
and facilitate cross-border secondary use of health data,
its success depends on overcoming systemic differences
between Member States. The lack of standardized metadata
cataloging, secure processing environments (SPEs), and regulatory alignment across national frameworks hinders the
uniform application of EHDS principles. Additionally, the
costs and logistical demands associated with implementing
EHDS-compliant infrastructure, as well as discrepancies in
technical expertise between Member States, present significant obstacles. These challenges must be addressed through
a combination of policy coordination, technological improvements, and strategic investment to ensure the EHDS fulfills its
mission of enabling seamless and secure health data exchange
across the EU.
One of the most pressing challenges in EHDS implementation is achieving interoperability between health data
systems across different Member States. A fundamental
issue is the variation in national health data infrastructures, which use different formats, coding systems, and
cataloging approaches. The adoption of the HealthDCAT-AP
standard seeks to bridge these gaps, yet inconsistencies in
how metadata is structured and maintained across countries
create barriers to seamless integration. Moreover, fragmentation in dataset catalogues means that even when data is
available, discovering and accessing it efficiently remains
problematic. There is also a semantic interoperability issue—
terminologies and classifications for medical data differ
between nations, complicating data harmonization efforts.
Without a universally accepted framework for structuring and
accessing health data, researchers and policymakers will continue to face hurdles in leveraging EHDS to its full potential.
Beyond interoperability concerns, technological and political issues significantly hinder EHDS implementation. On the
technological side, the creation of SPEs is a major requirement to ensure data security and compliance with GDPR.
However, setting up these environments requires sophisticated infrastructure and expertise that not all Member States
possess. Additionally, ensuring data quality and compliance
across different jurisdictions is a complex challenge, as data
must be standardized, anonymized, and protected against
security threats. On the political front, national sovereignty
concerns regarding health data governance create resistance
to cross-border sharing. Some countries hesitate to allow
external access to their health data due to fears of misuse
or breaches in confidentiality. Moreover, while the EHDS
framework establishes Health Data Access Bodies (HDABs)
to manage and facilitate data access, discrepancies in national
legal interpretations create governance inconsistencies. The
lack of uniform enforcement mechanisms further exacerbates
the challenge, leading to potential regulatory loopholes that
could delay EHDS implementation. Addressing these issues
will require stronger political will, regulatory alignment, and
technological advancements to ensure a smooth and equitable
adoption of EHDS across all EU Member States.
The EHDS regulation aims to create a framework for the
exchange and use of health data in the European Union while
ensuring data protection and privacy. The regulation proposes
several technical and legal specifications to ensure secure
processing environments for health data:
• Privacy by design: incorporate data privacy into systems
and services using seven principles: proactive measures,
default privacy settings, embedded privacy, full functionality, end-to-end security, transparency, and user
respect.
• Trust by design: establish trust among stakeholders (patients, providers, researchers) with transparent
data processes, clear communication, and stakeholder
engagement.
• Security measures: Ensure health data confidentiality,
integrity, and availability with strong access controls,
encryption, and monitoring to prevent unauthorized
access and modifications.
• Interoperability standards: Ensure seamless data
exchange using standards like FHIR, HL7, DICOM, and
provide APIs for integration.
• Data quality: Support accurate decision-making with
mechanisms for data validation, cleansing, and profiling.
• Privacy and data protection: Adhere to data protection
principles like purpose limitation, data minimization,
and data subject rights, with features for data masking,
anonymization, and pseudonymization.
• Audit and accountability: Implement audit trails and
logging for tracking activities and system events, supporting violation detection and investigation.
• Legal compliance: Ensure compliance with legal frameworks (GDPR, eIDAS, MDR) through necessary features like electronic signatures and data processing
agreements.
The EHDS require a data infrastructure to fulfill the digital
needs of data holders and users, including data storage, processing power, interoperability solutions, secure processing
environments for data analysis and connectivity to support
cross border secondary use of health data. For this approach,
two infrastructures were proposed. Given the requirements of
the GATEKEEPER project, we opt to follow EHDS21
regulation which describes health data exchange for both primary
and secondary use (e.g. research & innovation, regulatory
decisions etc.). It has the federated/distributed network supported by common infrastructure with agreed interoperability
standards and tools for the harmonization of the semantic
and syntactic interoperability to ensure all participants have
the same capabilities to initiate and process data requests.
Each participating node requires local computing capabilities
to enable querying and local processing which are aligned
to the tenant isolation; resulting in processing large amount
of data. The main elements of EHDS22
include i) Nodes
1An NCPeH is an organizational and technical gateway for the provision
of cross-border digital health information services for primary use of electronic health data, under the responsibility of Member States. NCPeHs are
established within the framework MyHealth@EU, on the basis article 4 of
Directive 2011/24/EU (eHealth Network).
2Towards the European Health Data Space.
(interfaces to data users), ii) Centralized Services (central
node interacting with user nodes), iii) Data Users (tenants
using the data), iv) Data Controllers (data custodians), v) Data
Processors (agencies processing personal data), vi) Data Permit Authorities (designated bodies which have mandate to
grant or reject the access), vii) Data Managers (who provide
access to electronic health records, and viii) Secure Processing Environments (SPE).
To address legal and data security challenges, we aim to
deploy SPE to enable researchers to securely access and
analyze sensitive data in compliance with ethical and legal
standards. Measures such as encryption, access control, auditing, and anonymization safeguard data privacy and foster trust
among stakeholders, encouraging data sharing and collaboration. Additionally, SPE ensures adherence to Findable,
Accessible, Interoperable, Reusable (FAIR) principles by
documenting and tracking data processing and analysis workflows, enabling validation and scientific progression.
B. CONTINUOUS INTEGRATION/CONTINUOUS
DEPLOYMENT
In order to deploy EHDS principles based on distributed
approach following SPE and FAIR principles, we developed
the DevOps platform based on CI/CD. The term Continuous
Integration refers to the idea of frequently integrating programming source code distributed among different teams to
identify any problems preventing the delivery of the solution
as soon as it is ready from the developers. Code changes are
regularly built and tested to find any issue earlier to optimize
the stability of the solution, preventing undesired effects,
but still delivery new features as they are ready and stable.
The CI exploits software engineering tools and practices for
the PLAN-CODE-BUILD-TEST phases (see Fig 1(a) - left
Ops block). These include: i) Version Control, ii) Regular
Check-ins, iii) Comprehensive Automated Test Suite, and
iv) Ensured Concise Build/Test Process.
On the other hand, the term Continuous Deployment
refers to the developer-initiated automatic release of each
update to the software artifacts from the repository to
production, where they become available to end-user and customer. While exploiting RELEASE-DEPLOY-OPERATEMONITOR (see Fig 1(a) - right Ops block), this requires
a high degree of automation and discipline, but allows the
application to be deployed to the customer after a few minutes
of writing the code by the developer, being confident it will
work as expected.
The CI/CD introduces the concept of DevelopmentOperations pipeline, an automated implementation of the
application’s build, deploy, test, and release process as shown
in Fig 1 (b). The pipeline breaks down in stages that needs be
implemented which includes i) Development where the team
of developers write the source code needed to the business
logic of the application; ii) Source Control where different
versions of the application code are tracked and this allows
the team of developers to effectively collaborate to the overall design. This way when any change occur, you can still
FIGURE 1. SecDevOps CI/CD practice with (a) Overall SecDevOps picture
and (b) CI/CD pipeline.
access the previous revision; iii) Build where the application code is created by compiling or building the sources;
iv) Test where built code is tested with automate test suites to
avoid regressions and verifying system behaviors; v) Release
where validated applications from Build and Test phases are
published to repository that keeps history of all releases;
vi) Deployment or Operations where runnable application
codes are deployed from repository to operating environment.
The CI/CD for GATEKEEPER makes use of a set of
open source tools for implementing the stages of both
CI/CD pipelines. The tools have been selected based on the
experience of the consortium partners, tools used in other
EU funded projects or internal R&D factories, the fact of
being open source, and on public reviews and ratings (e.g.,
Synopsys Black Duck Open Hub site).3 The most relevant
tools used in the GATEKEEPER project were: 1) GitLab
Community Edition (CE)4
an open-source software to collaborate on source code development 2)Nexus OSS,
5
for
CI/CD pipelines publish; 3) Jenkins,
6
a CI server used to
automatically monitor source repositories, build software, run
and visualize unit and integration tests.
C. SECDEVOPS INFRASTRUCTURE
SecDevOps is an approach for integrating security principles and practices into DevOps methodology. The goal of
the SecDevOps is to build security shielding around software development and deployment. The key principles of
SecDevOps include i) Shift-Left which means moving security activities and testing to the left (pre-phase) of software
development process; ii) Automation which means automated security testing and compliance checks as the part
of CI/CD pipeline. These may include static and dynamic
application security testing and container security scanning;
iii) Collaboration which means promote collaboration among
3https://openhub.net/
4https://git-scm.com
5https://www.sonatype.com/products/sonatype-nexus-oss
6https://jenkins.io
development, operation and security to ensure security as a
shared responsibility; iv) Risk Assessment to continuously
assess and prioritize security risk, threats and vulnerabilities
to make informed decisions about where to focus security efforts; v) Continuous Monitoring which implements
continuous security monitoring to detect and respond to security incidents; vi) Security Code to treat security policies,
configurations and compliance requirements as code that
can be versioned, tested and automated; vii) Compliance
and Reporting involving automated compliance checks and
reporting to ensure security polices and regulatory requirements are met.
For SecDevOps we deploy tools such as 1) Semgrep,
7
for finding security bugs in the source code; 2) OWASP
Dependency-Check8
to detect publicly disclosed vulnerabilities contained within the dependencies of a developed
software artefact, 3) Anchore Grype,
9
a scanning tool that
inspects container images to unpack and analyze everything
inside and perform vulnerability scanning and 4) DefectDojo,
10 an open source application vulnerability management correlation and security orchestration tool.
D. EVALUATION FRAMEWORK
The methodology for evaluating the GATEKEEPER platform incorporates both quantitative and qualitative feedback
from end users. A comprehensive evaluation framework was
designed to assess the platform’s capabilities in key areas
such as user satisfaction, interface experience, and feature
utility. The framework includes a series of questions targeting
specific aspects of platform functionality, usability, and alignment with healthcare needs. The primary evaluation metrics
are based on user responses collected through open calls
and interviews, ensuring a broad representation of end-user
perspectives.
IV. RESULTS
A. IMPLEMENTED CI/CD PIPELINES
As reported in Section III, we used the Jenkins open
source tool as a CI/CD orchestrator tool to monitor source
repositories, build software, run tests and deploy software.
We realized a multi node infrastructure made up of one
Control Plane node and two Agent nodes: the Control Plane
node is designed to coordinate and provide the Web Access
for developers, while the Agent nodes are designed to perform
and balance the code build work. In particular, Agent 1 builds
the software artifacts in a container, such in a way that the
tools needed to build are part of the container instantiation
and not directly installed on the Agent. Agent 2 is identified
as the security node that analyses the code of the software
artifacts and performs different levels of security analyses.
By using Jenkins, we implemented the SecDevOps concepts
by defining three multi-staged pipelines.
As shown in Fig 2., the Build pipeline is triggered automatically at every push of source code to GitLab and it
automatizes the build of the project, the creation of the
Docker image and the store of the container image on
the Nexus Docker Registry. Then, if the previous pipeline
succeeds, the second Deploy pipeline is triggered and
automatically deploys the component to the development
environment. Finally, the Security pipeline is triggered if the
Build and the Deploy pipelines are succeeded.
To allow developers to create in a self-service way the three
pipelines for their software components, we automated the
setup process by using the Jenkins Seed Job concept. The
Seed Job has been configured to permit developers to simply
fill out a form by entering few parameters - such as the GitLab
URL of the source code, the name of the container image to
build, the deployment descriptors for Kubernetes - and the
three pipelines get automatically created and are ready to use.
B. GATEKEEPER BEYOND SECDEVOPS AND
MICROSERVICES
GATEKEEPER provides advanced tools for security assessment through a specific build phase included into the
automation pipeline. This is completely transparent to developers that do not need to evaluate manually the software
they write. Within the GATEKEEPER platform, IoT devices
are certified and connectors are passed through the security build phase before the software is deployed. Data are
only transmitted within the military zone through a VPN
site to site. GATEKEEPER uses RBAC mechanism over
VPN to connect to a Demilitarized Zone (DMZ). It does not
implement the new trends such as Context-aware access control, fine-grained access control, Zero-trust security, Artificial
intelligence (AI) and machine learning (ML), Multi-cloud
access control. GATEKEEPER provides technical measures
for security and privacy with methodologies that are validated and agreed and signed with the pilot legal entities
that trust in the adopted measures. How security and privacy
is addressed is described in the technical annex and DPIA
provided by the infrastructure provider. GATEKEEPER does
not assume a zero-trust model; no external traffic outside
the DMZ is allowed. Therefore zero-trust model threats
are not considered. Such approach provides other kinds of
limitations, mainly the degradation of user usability related
to the multi-factor authentication for instance. Also, communication within the infrastructure itself is still protected
in several ways (encryption, inner firewall, etc.). GATEKEEPER platform allows OWASP driven CI/CD to check
integration vulnerability in last phase of automation pipeline
(incl. broken authentication, sensitive data exposure, security
misconfiguration, etc.).
C. OPEN SHIFT POLICY FOR HIGH SCALABILITY
The OpenShift and Ezmeral solutions are platforms that are
able to provide scalable and high-performance services for
data management and data science. The techno-legal specification is the tool used to support and give confidence, through
FIGURE 2. Multi-staged CI/CD pipelines for SecDevOps.
the agreements between pilots-platform, of the secure mechanisms used on one hand by the pilots to share the data and
on the other hand implemented into the platform. For implementing OpenShift, we selected OKD [33] as the container
orchestration engine to host and run the GATEKEEPER
Platform services developed by the partners. OKD leverages
on the de-facto standard Kubernetes engine [34], but adds
many features including a stricter security environment (by
default containers cannot run with administrative privileges)
and a sophisticated but user-friendly graphical interface that
lets users interact with it without the need to go through
the command line. OKD has been configured to segregate
with separated tenants all the GATEKEEPER Pilots. This
makes use of the project and namespace concepts that allow to
isolate the deployed components. Additionally, the platform
uses REST (REpresentational State Transfer) services instead
of web services in order to address scalability, extensibility and interoperability. REST services are in general more
performant and lightweight than other web services. Service
descriptions have been done using semantic annotation and
Web of things that provide a high-level of expressiveness.
D. COMPONENT PACKAGING AND AUTHORIZATION
Components are packaged as containers and run-in so-called
Pods (the Kubernetes resource to host one or more containers). Pods in different projects cannot talk to each other
because we defined specific virtual network level policies
for isolation. The Fig 3. illustrates the isolation between
Project Pilots and their running components in the Pods.
Project Pilots can be accessed only to authorized Pilot users
and administrators. Accounts are defined on the centralized Data Centre Identity Management service and follows
a pre-defined authorization process. Also access to Pilots
tenants is granted via Multi-Factor Authentication to authorized people only. Similar to the Pods, also the Pilots’
data is segregated in different volumes (Kubernetes calls
them Persistent Volume Claims - PVC). These volumes are
maintained in the storage solution (HPE Nimble), which
guarantees a high-level of availability and also has been configured to use data encryption at rest as a technical security
measure. The pods are grouped by component, like TMS
(Thing Management Systems), Data Federation and the GTA
(GATEKEEPER Trusted Authority). In addition to the Pilots,
we have three special projects: gatekeeper-dev (services that
FIGURE 3. Multi-tenant multi-cluster control plane for containerized
applications with Segregation for GATEKEEPER pilots.
is under active development), gatekeeper-test: (for integration testing for the Pilots), and gatekeeper-prod (to host
some common components shared among all the pilots).
E. EVALUATION OF THE GATEKEEPER PLATFORM
The GATEKEEPER platform’s effectiveness is substantiated through its robust technical infrastructure and advanced
capabilities, designed to support diverse healthcare applications at scale. The platform operates on a hardware
ecosystem comprising 20 Linux servers, 7 switches, 3 storage racks, and 70 virtual machines (VMs), managed via a
Kubernetes v1.23 setup. This infrastructure enables the platform to serve multiple tenants and projects simultaneously,
ensuring reliability, security, and performance optimization
for mission-critical applications. GATEKEEPER supports
demanding workloads with 400 virtual CPUs (vCPUs),
16 virtual GPUs (vGPUs), 3 TB of RAM, and 20 TB of
storage. These resources enable high-performance data processing and advanced modeling, empowering users to handle
complex analytics challenges efficiently. The platform supports 26 AI models with a fully implemented deployment
pipeline. Comprehensive model lifecycle management capabilities streamline the development and deployment of AI
solutions, enhancing operational efficiency and accelerating
innovation.
From the end users’ validation, user satisfaction with
the GATEKEEPER platform was assessed through an open
call survey (Fig 4(a)), where respondents rated their overall
experience on a scale from 1 to 5, with 1 indicating the
lowest satisfaction and 5 representing the highest satisfaction.
A notable 33% of participants gave the platform a score of 4,
and another 33% rated it a perfect 5, indicating high satisfaction. However, 8% of users rated it 2, suggesting some room
for improvement. Additionally, 25% of respondents gave a
rating of 3. The platform’s ease of use was also evaluated
through user feedback on the interface experience (Fig 4(b)).
The results indicated that 33.3% of respondents found it
‘‘very easy to use,’’ while 25% considered it ‘‘somewhat
easy.’’ Another 25% felt it was ‘‘neither easy nor difficult,’’
and 16.7% found it ‘‘somewhat difficult to use.’’ These results
suggest that while most users found the interface accessible,
there is a significant portion of the user base who may require
additional improvements or guidance to enhance usability.
FIGURE 4. GATEKEEPER platform performance evaluation with (a) overall
experience and (b) interface experience from end user.
V. DISCUSSION: GATEKEEPER FINDINGS AND
EXPERIENCE
A. GATEKEEPER DATA HOLDER INFRASTRUCTURE
The GATEKEEPER infrastructure enables secure, standardized healthcare data sharing within the EU, promoting
interoperability, privacy, data protection, and regulatory compliance. It supports cross-border collaboration, enhances
healthcare outcomes, and fosters responsible data sharing
practices. This infrastructure is vital for seamless health data
exchange, ensuring privacy and security within the EHDS
ecosystem. Healthcare centers acting as Data Holders can
leverage the GATEKEEPER secure processing environment
by identifying necessary data, determining collection methods, implementing technical and organizational measures,
establishing a lawful basis for data processing, and monitoring for breaches. This ensures responsible data management
and quality patient care.
This infrastructure enables secure, standardized healthcare data sharing, promoting interoperability, privacy, and
regulatory compliance while supporting cross-border collaboration and enhancing healthcare outcomes. Data Holders can
leverage the GATEKEEPER secure processing environment
by identifying necessary data, implementing safeguards,
establishing a lawful processing basis, and monitoring for
breaches, ensuring responsible data management and quality
patient care.
The end-user feedback gathered on platform features and
interface experience provides valuable insights into user satisfaction and areas for improvement, further guiding the
refinement of the GATEKEEPER infrastructure to better
meet the needs of healthcare professionals.
B. GATEKEEPER SECURITY FRAMEWORK
Gatekeeper provides a robust security framework for IoT
ecosystems by ensuring encrypted communication, strict
authentication, real-time anomaly detection, and automated
security enforcement. It employs mutual TLS (mTLS) with
TLS 1.3 for end-to-end encryption, securing data transmission between devices and services. Authentication is
managed through JSON Web Tokens (JWT) and role-based
access control, ensuring only authorized devices access network resources. Real-time anomaly detection is achieved
through AI-driven monitoring tools integrated with GATEKEEPER’s observability stack, including Jaeger, Kiali, and
Elasticsearch. These tools analyze traffic patterns, detect
unusual behaviors such as excessive API calls or irregular
device activity, and trigger automated responses to mitigate potential security threats. GATEKEEPER also integrates
with firewalls and API gateways to filter malicious traffic
and enforce rate limits, preventing denial-of-service attacks.
Through automated policy enforcement, Istio dynamically
adjusts security rules and quarantines suspicious devices,
maintaining a zero-trust model where all interactions must
be authenticated. By integrating advanced encryption, access
control, and AI-powered real-time anomaly detection, Istio
offers a comprehensive security solution for protecting IoT
networks against modern cyber threats.
GATEKEEPER adheres to EU cybersecurity regulations,
such as EHDS Secure Processing Environments specification. It integrates stringent security protocols to ensure
compliance, data integrity, and resilience against cyber
threats in healthcare. It also incorporates strong encryption
for data in transit and at rest, strict identity and access management, and continuous monitoring to detect and mitigate
vulnerabilities. Its advanced security model, central to its
design, ensures that every access request, whether from users,
devices, or applications, is continuously verified based on
identity, behavior, and context. By implementing AI-driven
real-time anomaly detection, the platform proactively identifies threats and respond dynamically, isolating compromised
endpoints before damage occurs. Advanced automation and
security orchestration enables rapid adaptation to evolving
cyber risks, ensuring compliance with regulatory standards
while maintaining operational efficiency. By staying ahead
of emerging threats through predictive threat intelligence and
adaptive security policies, the platform provides a resilient
and future-proof solution for securing sensitive healthcare
data across distributed environments.
C. SPE FOR RESPONSIBLE AND ETHICAL USE OF AI
The GATEKEEPER infrastructure ensures responsible and
ethical data management through transparency and ethics
by design. It incorporates OWASP-driven CI/CD tools to
ensure data security and compliance with EHDS standards.
Real-time monitoring of AI systems, RESTful APIs powered
by OKD, and advanced algorithms enable the detection of
unethical behaviors and trigger alerts to stakeholders via
log monitoring. The platform emphasizes transparency and
explainability by leveraging tools such as Kubernetes for
scalability and SHAP dashboards for insight into AI decisionmaking [35]. User feedback mechanisms further promote
accountability, enabling individuals to report concerns and
share experiences.
Collaboration among researchers, developers, and policymakers is fostered through the sharing of best practices,
case studies, and research findings on ethical AI usage. This
supports continuous learning and improvement of AI systems while advancing the field through collective efforts.
Objectives include promoting ethical AI practices, mitigating harm, ensuring accountability, and addressing ethical
challenges. Organizations can monitor AI systems, detect
potential ethical issues, and take corrective measures. Key
steps to achieve these objectives include: i) Defining ethical guidelines for AI use based on EHDS principles and
best practices. ii) Conducting regular audits for compliance.
iii) Monitoring model performance to avoid bias using CI
tools like Jenkins. iv) Enforcing access controls via RBAC.
v) Maintaining audit logs through tools such as Anchore
Gripe and Defect Dojo. vi) Implementing alert mechanisms
for unexpected behavior and ethical issues.
D. NEEDS FOR EHDS TECHNO-LEGAL SPECIFICATION
Building trust with pilot organizations and the Gatekeeper
platform was crucial for facilitating data processing and interoperability. This trust required establishing legal agreements
that ensured Gatekeeper’s technical measures met robust privacy and security standards. Negotiating these agreements
was time-consuming and resource-intensive. To streamline
adoption, incorporating techno-legal specifications for secure
processing environments into standard legal clauses could
be beneficial. This would provide a predefined framework
aligning with security and privacy requirements, expediting
the agreement process and fostering quicker trust-building.
Techno-legal specifications for Gatekeeper included:
i) Encryption of all stored or transmitted data. ii) Access
control for restricting sensitive data access to authorized
personnel. iii) Auditing and logging for accountability.
iv) Regular vulnerability assessments. v) Incident response
plans for security breaches. vi) Data retention and disposal
policies. vii) Compliance with legal and regulatory requirements. viii) Continual monitoring and improvement.
Several solutions have emerged to address the ongoing challenges within the European Health Data Space
(EHDS), including the IDEA4RC platform11 and the newly
launched Protect-Child platform.12 Both initiatives were
funded through specific EU calls aimed at fostering EHDScompliant solutions. However, GATEKEEPER remains a
strong competitor, offering a mature and tested alternative
while these other platforms are still under development.
The IDEA4RC project is currently at its midpoint, having
completed two out of its four-year development cycle,
whereas Protect-Child is still in its early stages, with only
six months completed in a 48-month project timeline. In contrast, GATEKEEPER is already an established and validated
solution that fully meets the initial requirements for a Secure
Processing Environment (SPE) as outlined in THEDAS2’s
public consultation draft.13 This positions GATEKEEPER
as one of the leading candidates for early SPE certification,
reinforcing its relevance and competitiveness in the evolving
EHDS ecosystem.
VI. CONCLUSION
In conclusion, our manuscript addresses the pressing challenges of securely storing, managing, and exchanging healthcare data across different pilots located inside different
member states in the European Union. These challenges
are also in alignment with the European Health Data Space
(EHDS) regulation proposal. Within the GATEKEEPER
project, we have meticulously designed a platform to seamlessly integrate diverse data sources and deploy advanced
analytical tools, facilitating the development of novel solutions for predicting, detecting, and managing chronic health
conditions. Our platform architecture incorporates collaborative tools for data management and consistency, as well
as machine learning modeling and management tools. Furthermore, we have implemented authentication and CI/CD
mechanisms to ensure scalability, security, and the effective management of vulnerabilities and third-party package
dependencies. Specifically, the Data Holder infrastructure
within the GATEKEEPER platform is intricately aligned with
EHDS proposal, providing a secure framework for securely
storing, managing, and exchanging healthcare data across the
European Union. Through robust security measures, access
controls, and encryption techniques, it upholds the integrity
and confidentiality of healthcare data. Our quantitative evaluation reveals positive user perceptions, with the majority
finding the platform easy to use and highlighting its potential to enhance interoperability and data-driven healthcare
practices.
ACKNOWLEDGMENT
The authors would like to express their sincerest gratitude
to all the partners and participants of the GATEKEEPER
Project. The funder played no role in study design, data
collection, analysis and interpretation of data, or the writing
of this manuscript.
(Eugenio Gaeta and Muhammad Salman Haleem contributed equally to this work.)
Claudio Caimi, Christian Tamporale, and Chiara Bonferini
are with Hewlett-Packard Italiana, Milan, Italy;
Paolo Zampognaro and Federica Saca are with Engineering
Ingegneria Informatica S.p.A, Roma, Italy; Ioanna Drympeta
and Konstantinos Votis are with the Information Technologies
13https://tehdas.eu/wp-content/uploads/2025/01/2025-01-22-tehdas2-
milestone-7.1.pdf
Institute, Centre for Research and Technology Hellas, Thessaloniki, Greece; Dimitrios I. Fotiadis is with the Department
of Materials Science and Engineering, Unit of Medical Technology and Intelligent Information Systems, University of
Ioannina, Ioannina, Greece; Frans Folkvord is with PredictBy, Barcelona, Spain, and also with Tilburg School of
Humanities and Digital Sciences, Tilburg, The Netherlands;
Sergio Guillen is with Mysphera S.L., Paterna, Spain; and
Paula Curras, Jorge Posada, and German Gutierrez are with
Innova & European Projects Office, Integrated Health Solutions, Medtronic Ibérica S.A., Madrid, Spain.