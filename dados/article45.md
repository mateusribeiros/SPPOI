Title: Scalable and Sustainable Blockchain: Architecting Infrastructure and Developing a Platform for Efficient Management and Exploration

ABSTRACT The application of blockchain technology in the health and healthcare sector is considered
disruptive, thus requiring trust, integrity, and value of data. In addition, this document analyses the potential
of permissioned blockchain, more specifically Hyperledger Fabric, to improve the security, integrity, and
efficiency of healthcare systems. It examines ways in which this can be done in a manner that has both
scalability and sustainability prospects in the long-term. This, by reaching the optimal compromise between
efficiency of resources and its ease of use, management and upscaling. The ability to be as lightweight as
possible, while being able to quickly expand the infrastructure and seamlessly integrate new functionalities,
maintaining operational efficiency.
The research developed involves a review of the literature, the development of three different blockchain
implementations/architectures where the practical assessment of performance metrics is performed. Finally,
a blockchain management platform is presented. This was developed to ensure long-term usability and
maintenance of blockchain solutions in the healthcare industry.
This work aims to advance the application of blockchain in healthcare, addressing both immediate and longterm needs for security and efficiency.
INDEX TERMS Blockchain, Blockchain in Healthcare, Healthcare Systems, Hyperledger Fabric,
Kubernetes.
I. INTRODUCTION
The healthcare industry, an industry with exclusive
requirements, where data integrity, flexibility, collaboration,
and confidence are key to its daily operations. In order to
combat the needs present in the industry arises blockchain
technology as a transformative solution.
For this sector, there is currently a need for reliable
solutions that protect patient data, optimise workflows and
improve teamwork. This article explores the search for a
private blockchain system that benefits the sector by
providing greater data integrity, security, flexibility, and
trust.
Data manipulation and privacy breaches are increasingly
becoming a threat to the security and efficiency of the
healthcare sector where data integrity is paramount.
Hyperledger Fabric has become a solution for building trust
in the accuracy of health information. With its immutable
ledger and cryptographic techniques, it provides a robust
solution that ensures transactions are secure and inviolable.
It also has a modular architecture that allows it to be flexibly
integrated into existing systems and adapted to future
advances, thus facilitating innovation and smooth
transitions.
In order to maximise the application of blockchain in this
environment, it is important to develop a solution that meets
the immediate needs of efficiency and security and
guarantees long-term scalability and sustainability. For this
to happen, it is necessary to create an approach that allows 
this technology to be expanded easily and efficiently to the
various areas present in the ecosystem. This ensures that the
infrastructure grows and adapts to future demands without
compromising performance or data integrity.
Scalability must be considered from two main points of
view: infrastructure and utilisation. Regarding the
infrastructure aspect, the solution must allow for the addition
of more components or servers as demand increases, using a
platform and scripts specifically developed to facilitate this
expansion. In terms of utilisation, scalability involves the
ability to add new chaincodes for different areas in the
hospital ecosystem. The platform must provide a dedicated
space for installing these chaincodes, allowing for the
continuous integration of new functionalities.
As mentioned, in addition to scalability, sustainability
must also be considered. It is important to adopt practices
that minimize the economical and environmental impact
while ensuring that the technology remains robust and
reliable in the long-term. It is aimed to find an ideal balance
between security and resource consumption by optimizing
the number of components, processing power and
consequently machines. Additionally, the solution should be
easy to manage and grow in usability to ensure its long-term
viability, avoiding rapid abandonment that could
compromise its future value and effectiveness.
Throughout this article, it is explored the application of
HLF with different approaches, in local networks. Initially,
a literature review was conducted to contextualize the topic,
addressing blockchain technology and its application in the
healthcare sector, as well as the methodology adopted and
the tools/frameworks used. In the subsequent practical phase,
a set of architectures were implemented, upon which tests
were conducted, evaluating four key metrics: CPU variation
and Disk, Ledger and RAM usage. The comparison between
these architectures is discussed based on their distinct
components and the mentioned metrics, so to help identify
the most suitable architecture for the case study. Then, it is
presented a platform that provides an overview of the
network in terms of resources, transaction information, and
also with the ability of easily managing and interacting with
the components of the network. Finally, the conclusions are
presented, along with directions for future work to be
developed.
II. BLOCKCHAIN IN HEALTHCARE
The health and care sector faces different challenges.
Challenges with the intensive use and demand for data,
unauthorised sharing, breaches and bad practices. Because of
these problems, patient trust in this sector is jeopardised,
which leads to the need to consider alternative approaches to
improving data access, security, and integrity [1], [2]. Thus,
blockchain technology has emerged as an alternative
approach to current systems. With its properties such as
access control, provenance, integrity and immutability of
data, it has emerged as a potential solution for improving the
sector. Its aim is to create and maintain trust between all
stakeholders [3].
Blockchain’s immutability protects health records and
supports regulatory compliance. Smart contracts enable realtime patient monitoring, secure data exchange, and privacy.
They also aid in managing pharmaceutical supply chains,
combating counterfeit drugs, and improving informed
consent, identity management, and data quality, ultimately
enhancing patient privacy and data management [3], [4].
Based on a study carried out by IBM, 70% of world
leaders in the sector predict that the most significant impact
of this technology will be in improving the management of
clinical trials, ensuring regulatory compliance and
establishing a decentralised framework for sharing electronic
health records [1].
A. TYPES OF BLOCKCHAIN
Blockchain technology can be divided into three types:
public (permissionless), consortium (public permissioned)
and private (permissioned). Each of these three types has
different characteristics [1]. To understand each of them, it
is important to explore the specific characteristics of each
type.
Public blockchains are open and transparent and allow
anyone to participate, contribute to consensus and verify
records. Transactions are publicly visible and anyone on the
internet can access this information [1], [5]. Examples of this
type of blockchain include cryptocurrencies such as Bitcoin
and Ethereum [6].
Private blockchains, on the other hand, are controlled by
an organisation, with centralised write permissions and
flexible read access. They offer high privacy, controlled
transactions and the possibility of modifying rules.
Advantages include known validators, easier fault
correction, manageable block size and lower processing
costs [1], [5]. Hyperledger Fabric is one of the most popular
private blockchains [7].
Finally, consortium blockchain is presented. These are
partially decentralized, with the power shared between a
group of organisations rather than a single entity. Only
selected entities can check and add transactions through a
consensus process. For example, if five nodes are involved,
at least three must validate one block before it is added to the
chain [1], [5]. R3CEV is an example of a consortium
blockchain [6].
For each of the types of blockchains presented,
depending on their application, there are vantages. The
choice of which type of blockchain to implement ultimately
depends on the specific service or application for which it is
needed [6].
After presenting the three types of blockchain, it is
important to emphasise that for the case study presented in
this article, a private blockchain is used. This choice is due
to the fact that the project is located in a healthcare
environment, where it is essential to guarantee the privacy
and security of patient data, provide strict access control and
maintain regulatory compliance.
B. KEY BLOCKCHAIN BENEFITS/FEATURES WHEN
APPLIED TO THE HEALTHCARE SECTOR
Blockchain technology has a number of attributes and
characteristics that have allowed it to make inroads into
different industries and sectors, one of which is the health
sector. With the constant evolution of the health sector, more
problems arise, and in this sense this technology plays an
increasingly important role, as it provides innovative
solutions to meet these needs. To understand why this
technology is an asset to the sector, the main benefits it
provides are presented below [8], [9].
A. Authentication. In order to protect records, the
blockchain uses a private key linked to a public key to
create, modify or visualise data.
B. Immutability. Blockchain only allows data creation
and reading, making alterations difficult. It uses
consensus among nodes to validate transactions,
ensuring data integrity and security.
C. Provenance. Blockchain allows only owners to change
ownership and ensures traceable, verifiable asset
origins, ideal for managing patient consent records.
D. Robustness/Availability. Each node in the chain stores
a complete copy of the data history, which ensures
availability and continuous redundancy. This makes it
ideal for storing electronic health records.
E. Security. In order to improve security, blockchain with
advanced encryption, distributed consensus and
immutability guarantees data integrity and protection
against potential threats.
F. Privacy. The blockchain enables controlled access to
data. Using a pseudonym allows secure sharing
between authorised parties.
C. IMPLEMENTATION REQUIREMENTS
In order to implement a blockchain system in the
healthcare environment, a number of requirements are
needed. According to Kumar et al. [10], there is a set of main
requirements that must be considered when implementing
this technology in this environment. The authors emphasise
that the main requirements are interoperability, security,
consistency, integrity, data immutability, trust and
transparency and complexity. The requirements presented by
the authors are fundamental to laying the foundations for a
resilient and efficient blockchain system that adapts to needs.
Below, a detailed analysis of each requirement will be
carried out to provide information on the considerations
required for a successful implementation in this
environment.
A. Interoperability. Interoperability is presented as one
of the indispensable requirements when blockchainbased healthcare systems are to be implemented.
Currently, healthcare systems lack interoperability,
which becomes a major obstacle to management. This
is where blockchain comes in, as it enables the
interoperability of electronic health systems with the
systems present within the hospital. This integration
facilitated by this technology improves the exchange of
information between the different systems, which
promotes an interconnected and efficient ecosystem
system.
B. Data Security. The security of confidential patient data
is one of the indispensable requirements when looking
to implement this technology. With various
organisations and areas involved, security must be the
main objective. By implementing blockchain
technology, it is expected to guarantee data security,
privacy, and trust when compared to current systems in
operation. The transparency offered by this technology
increases the security of patient data by promoting a
system in which each transaction is traceable and
verified by the entire network.
C. Data Consistency/Integrity/Immutability. One of the
current challenges in healthcare management systems
is the incoherence and fragmentation of medical data.
These inconsistencies cause delays and higher costs in
finalising the user's overall process. Given these
problems, by implementing a blockchain-based system,
it ensures that health data becomes consistent, integral
and is not altered by unauthorised entities. In this way,
it makes it possible to maintain a secure and unalterable
history of each patient's medical data.
D. Trust and Transparency. In today's healthcare
systems, there is a need to create trust between the
various stakeholders so that data storage and sharing
processes can take place. Maintaining this trust and
transparency in operations becomes a significant
challenge, as data is shared and stored between various
parties and in various places. With a blockchain-based
system, intermediaries are eliminated. With this
elimination, the blockchain establishes a system in
which each transaction is traceable, verifiable, and
transparent to users with permission to view this
information. In this way, the creation of trust between
interested parties is consummated, as well as
guaranteeing the integrity of the data.
E. Complexity. Today's healthcare systems involve
multiple stakeholders and are complex in terms of
storing, sharing and processing medical data and other
billing-related information. Therefore, one of the
requirements for a blockchain-based healthcare system
is process complexity. Simplifying processes in this
system optimises the overall workflow. It reduces
complexity and increases efficiency. This ensures
smoother interactions between stakeholders and
minimises delays in critical phases of healthcare
processes.
D. IMPLEMENTATION CHALLENGES/ISSUES
Implementation issues and challenges must be considered
when looking to implement blockchain systems in the
healthcare environment. The challenges identified by various
authors are listed and detailed below.
A. Security and Privacy Concerns. To protect medical
records, it is crucial to guarantee access control,
authentication and non-repudiation. The methods that
currently exist are insufficient. This is why blockchain
technology has emerged. It improves security and
privacy, but requires careful implementation to manage
risks and guarantee secure access and sharing of data
[12].
B. Interoperability. Healthcare maintaining centralised
data storage leads to fragmented records, slow access
and problems with data quality. The ledger offered by
blockchain technology can address these needs and also
facilitates the secure and efficient exchange of data
between healthcare systems. This improves
interoperability between systems [9].
C. Data Sharing. Sharing data, health records, is a
challenge because the data is scattered in various
places, requiring a unified view of it for both patients
and providers. When data is centralised, it lacks
common identifiers and stakeholders are reluctant to
share it. Blockchain technology offers a solution by
providing a secure approach to storing and sharing data.
In this way it increases transparency and allows
controlled access to up-to-date information [9], [10].
D. Mobility. As patients use smart devices, there is a
growing need for portable and secure health records.
Blockchain technology has a decentralised and secure
platform that supports real-time data access and
portability. In this way, it meets the challenges of
maintaining data security and compliance [9].
E. Transparency and Confidentiality. When carrying
out a transaction, transparency of information is seen as
an inconvenience. In a blockchain, everyone has access
to all the information or people with authorisation have
access to the information, which results in greater
transparency and therefore less confidentiality.
Furthermore, despite the use of hash values for
anonymity, users can be identified by analysing
publicly available transaction information on the
network. This is particularly critical for healthcare
applications, where patient-related data is sensitive and
confidential [8].
F. Speed and Scalability. When it comes to developing
scalable, real-time blockchain-based solutions, speed
and scalability is an important aspect. Depending on the
protocol used, transaction times can vary, and speed
restrictions can limit the scalability of applications. In
other words, the trade-off between available computing
capacity and the volume of medical transactions can
limit the scalability of these healthcare systems. [8],
[10].
G. High Development Costs. Healthcare systems based
on blockchain can incur high development and
operation costs. The government and the healthcare
sector still need to define the different types of
development, operations, and total deployment costs
for all stakeholders involved. Therefore, it is crucial to
find optimal ways to reduce overall costs and resources
for building such systems [10].
H. Standardisation. For a successful deployment in
healthcare applications, standardisation bodies must
define appropriate standards. For example, regarding
health information stored on the blockchain, it should
be clear which data, size, and format can be sent to the
blockchain. Thus, the medical data stored within or
outside the blockchain should be well-defined.
Establishing clear standards is crucial to ensure the 
smooth integration of blockchain technology into
healthcare systems [10].
I. Cultural Resistance. Most people are used to health
records being accessible via paper procedures or
electronic health records and other online services.
Most of the time, user data is not shared by several
parties. Therefore, this cultural shift from the current
paradigm will be one of the main challenges, since
changing people's behaviour towards distributed data
sharing will require some effort [10].
D. APPLICATIONS OF BLOCKCHAIN TECHNOLOGY IN
THE HEALTHCARE SECTOR
Blockchain technology has become vital to the
development of the health sector and this environment. It
offers significant benefits as a distributed ledger for both data
storage and access. It allows data to be shared, exchanged,
analysed, validated and recorded between all interested
parties [8]. There are several applications for this
technology, however, the one that is most discussed is its use
as a framework for the exchange and transaction of
information between patients, providers, payers and other
important parties. This has the potential to be applied in a
variety of applications in the sector [8] [10].
Due to the significant potential and practical applicability
that blockchain technology offers to the sector, several
researchers are exploring application cases. A list of different
areas in the healthcare sector where this technology is
applied is presented below.
A. Electronic Medical Records
One notable use case of blockchain technology in
healthcare is for the management of Electronic Medical
Records, which include personal health records. By using
blockchain technology, it helps in the creation, storage, and
management of patient data [8], [10], [11].
One example of blockchain technology being used in
EMR is MedRec, a system developed by Azaria, Ekblaw,
Vieira and Lippman. MedRec allows patients to access and
manage their medical information in real time across
different services. They have control over the information
and can securely share their records, deciding who can access
them. Blockchain technology supports authentication,
confidentiality, and data sharing through integration with
local data storage, thus improving interoperability and
communication between doctors and patients [12].
B. Clinical Data Sharing
Sharing clinical data is an important application of
blockchain technology in the health sector. It enables the
secure exchange of data between different organisations. It
addresses the need for secure access, processing and storage
of information in patient records [8], [10], [11].
An example of using blockchain technology to share
clinical data is HealthVerity. It addresses challenges related
to data access, interoperability, privacy, supporting research,
analysis and data-driven innovation. Blockchain technology
is used to ensure the secure and transparent sharing of
clinical data between stakeholders [13], [14].
C. Global Data Sharing
Global data sharing is crucial in healthcare, especially for
patients travelling abroad or receiving medical treatment
abroad. For treatments to take place smoothly and without
jeopardising the patient, it is important that doctors and
providers have access to the patient's medical information to
ensure that the care is as good as possible [8], [10], [11].
Health Wizz is an example of blockchain technology for
global data sharing. It allows users to manage their health
information, including medical history, test results and
doctors with immutable and inviolable records that guarantee
the reliability and authenticity of the data. In this way,
blockchain technology is used to securely and transparently
store and share patient health data around the world,
guaranteeing its integrity and privacy [15], [16].
D. Medical History Maintenance
By using blockchain technology, patients' medical
histories can be stored and managed effectively. This is
particularly beneficial for patients who visit several
hospitals. It ensures that records are accessible and up-todate in all healthcare institutions, thereby reducing
unnecessary procedures such as repeated medical
examinations or analyses due to disconnected data [8], [10],
[11].
Doctors find it difficult to manage and authenticate large
volumes of data. By using Medicalchain, which uses
blockchain technology to create a centralised electronic
health record, where a single, accurate and securely updated
record of patients' medical history is kept. Blockchain
technology helps maintain data privacy, security and
authenticity [16].
E. Health Data Access Control
With technological advances, access control is
increasingly important. Users must be aware of who, when
and why they have accessed their data, as well as realising
whether that access is legitimate. In the case of health
records, patients must be informed about who accesses their
data and what data is shared and stored [8], [10], [11].
Coral Health is an example of blockchain technology used
to simplify the sharing of and access to patient information
in the healthcare system. It connects all stakeholders in a
distributed ledger, allowing patients to share their records
securely and easily, while simultaneously monitoring
privacy [16].
F. Billing/Payments
The healthcare sector finds traditional payment systems
complex and prone to fraud, often requiring considerable
resources and time. Blockchain solutions are expected to
simplify payments significantly, reducing invoice processing
from days or weeks—especially when insurers are
involved—to a much quicker and more efficient process [8],
[10], [11].
PokitDok, through its private network, DokChain, uses
blockchain to simplify payments and transactions in
healthcare. DokChain employs smart contracts to handle
claims and payment processing in real time. Details of the
healthcare provided are recorded for patients and visible to
all interested parties, as well as calculating liability and
payment amounts. PokitDok also provides APIs to assess
payment risks and allows patients to book and pay for
services [13].
G. Biomedical Research and Education
The use of blockchain improves clinical trials. It increases
transparency, auditability and accountability, helps prevent
data falsification and underreporting of results and
guarantees their integrity through immutability. Its
transparent nature allows for the seamless replication of
research results [8], [10], [11].
The Shivom project uses blockchain technology to
revolutionise genomics and healthcare. It creates a global
ecosystem to securely store, share and monetise genetic
information. By taking advantage of large genomic datasets,
it promotes medical research and new treatments, while
allowing individuals to control access to their data [17].
H. Pharmaceutical Supply Chain
Blockchain can also be applied to managing the health
supply chain, especially in the pharmaceutical industry. It
helps combat the delivery of counterfeit or substandard
drugs, addressing a significant issue that can adversely affect
patients [8], [10], [11].
To improve the pharmaceutical supply chain, companies
like IBM have launched pilot projects with manufacturers,
distributors, and hospitals to test blockchain solutions.
Internal and external factors drive collaboration among
supply chain participants to implement blockchain
effectively. IBM Blockchain for Pharmaceuticals offers
essential solutions for traceability and cost-efficiency in the
supply chain [18].
I. Equipment tracking
By using blockchain technology, healthcare institutions
can make significant savings in the process of tracking
equipment. Given its immutability and inviolability
characteristics, it guarantees a credible location history.
Implementing this approach helps combat the growing issue
of theft and loss of medical devices [8], [10], [11].
Chronicled Blockchain is a platform specialising in the
authentication and traceability of products and equipment. It
uses blockchain technology to provide the integrity and
authenticity of information, creating immutable and
transparent records, as well as a reliable audit trail for each
product along its chain [19].
J. Health Data Analysis
Implementing blockchain technology transforms
healthcare systems and offers the chance to integrate
emerging technologies like machine learning and artificial
intelligence. This combination facilitates predictive analysis
of health data, advancing precision medicine [8], [10], [11].
Nebula Genomics revolutionises the genomic data market
by building the Nebula Network on blockchain. Thus
creating a market where sequencing facilities,
pharmaceutical companies, health organizations and other
relevant institutions can buy genetic information. By using
the Nebula Network, individuals pay to know their genetic
variants and predisposition to diseases, but they allow their
data to be shared with third parties [20].
III. RESEARCH METHODOLOGY AND TOOLS
This section presents the research methodology used
along with a set of essential tools for the development of the
project.
A. METHODOLOGY DESIGN SCIENCE RESEARCH
The methodology used is Design Science Research
(DSR). This is a methodology that focuses on creating
innovative artifacts to solve real problems or challenges. It is
based on the premise that academic research should not only
contribute to theoretical knowledge, but also produce
practical solutions that can be applied to improve situations
in a given field.
At its core, DSR combines elements of both design and
science, drawing on principles from engineering, computer
science, management, and other disciplines to develop novel
artifacts, such as systems, processes, models, or frameworks.
These artifacts are designed to solve specific problems or
fulfill particular needs within a given context, with an
emphasis on practical utility, effectiveness, and relevance.
The DSR process typically involves several key stages,
including problem identification, artifact design and
development, demonstration and evaluation, and
communication of results. Researchers engage in a
systematic and iterative process of problem-solving, guided
by principles of design thinking and scientific inquiry, to
create artifacts that address identified needs or opportunities
[26][27][28].
B. TOOLS
The main tools used in the development of the project will
be presented below. It is worth highlighting, however, that
several other frameworks and tools, in addition to those
mentioned, were also used.
Ø Kubernetes
Kubernetes, also known as K8s, is an open source system
for automating deployment, scaling, and management of
containerised applications [29].
Kubernetes is an open-source container orchestration
system. It manages containerised applications across
multiple hosts, enabling the deployment, monitoring, and
scaling of these containers. Originally developed by Google,
it was donated to the Cloud Native Computing Foundation
(CNCF) in March 2016. Kubernetes, also known as "k8s" or
"kube," enables users to define the desired state of an
application using concepts like "deployments" and
"services." For instance, a user can specify running three
instances of a Tomcat web application. Kubernetes then
manages these containers, ensuring they stay in the desired
state by automatically restarting, re-scheduling, and
replicating as needed. Kubernetes can be installed as a
standalone system or accessed through various distributions,
including Red Hat OpenShift, Pivotal Container Service,
CoreOS Tectonic, and Canonical Kubernetes [29]–[31].
Ø Prometheus
Effective monitoring and alerting are paramount for
ensuring the reliability, performance, and availability of
applications and infrastructure. Prometheus, an open-source
monitoring and alerting toolkit originally built at
SoundCloud and now a part of the Cloud Native Computing
Foundation (CNCF), has emerged as a leading solution for
monitoring dynamic, containerised environments.
At its core, Prometheus is designed to collect, store, and
query time-series data, allowing users to gain insights into
the behavior of their systems over time. With a focus on
simplicity, reliability, and scalability, Prometheus provides a
robust framework for monitoring a wide range of
infrastructure components, including servers, containers,
databases, and application metrics.
Key features of Prometheus include its time-series data
collection capabilities, flexible query language (PromQL),
support for service discovery, built-in alerting and
notification system, and seamless integration with other
cloud-native technologies.
As organisations embrace cloud-native architectures and
adopt containerised environments, Prometheus plays a
crucial role in ensuring the observability and operational
excellence of their systems. By providing a scalable, reliable,
and flexible platform for monitoring and alerting,
Prometheus empowers users to gain insights into the
performance and health of their applications and
infrastructure [32]–[34].
Ø Grafana
Grafana has established itself as a leading open-source
platform for monitoring and analytics. Originally created by
Torkel Ödegaard in 2014, Grafana has evolved into a
versatile and powerful tool used by organisations worldwide
to visualise and analyse metrics, logs, and traces from
various data sources.
At its core, Grafana provides a unified interface for
creating, exploring, and sharing dynamic dashboards and
visualisations. Leveraging its intuitive user interface and
extensive plugin ecosystem, users can connect Grafana to a
wide range of data sources, including time-series databases,
log aggregators, cloud monitoring services, and more.
Key features of Grafana include its visualisation
capabilities, seamless integration with diverse data sources,
support for templating and variables, built-in alerting and
notification functionality, and a vibrant community and
ecosystem of users and contributors.
As organisations embrace cloud-native architectures and
adopt distributed systems, Grafana plays a crucial role in
enabling observability and insights into complex
environments. By providing a flexible, customizable, and
extensible platform for monitoring and visualisation,
Grafana empowers users to gain actionable insights into their
systems and applications [32], [34], [35].
Ø Hyper Ledger Fabric (HLF)
In the rapidly evolving landscape of blockchain
technology, HLF stands out as a powerful and versatile
framework for building distributed ledger solutions.
Developed under the umbrella of the Linux Foundation's
Hyperledger project, Fabric offers a robust, modular, and
enterprise-grade platform tailored for businesses and
organisations seeking to harness the transformative potential
of blockchain.
At its core, HLF is designed to address the unique
requirements and challenges faced by enterprises in
deploying blockchain-based solutions. Unlike public
blockchains such as Bitcoin or Ethereum, which are open and
permissionless, Fabric provides a permissioned network
model, enabling organisations to maintain control over
access, governance, and privacy.
One of the key distinguishing features of HLF is its
modular architecture, which allows for flexibility and
customisation to meet diverse use cases and requirements.
Fabric leverages a pluggable consensus mechanism,
allowing organisations to choose the consensus algorithm
that best suits their needs, whether it be practical Byzantine
fault tolerance (PBFT), Raft, or others.
Another notable aspect of HLF is its support for smart
contracts, known as chaincode. Chaincode in Fabric is
written in familiar programming languages such as Go,
JavaScript, or Java, offering developers a familiar
environment for building and deploying business logic on
the blockchain. Additionally, Fabric's support for private
data collections enables organisations to store sensitive
information off-chain, ensuring confidentiality while still
benefiting from the transparency and immutability of the
blockchain [28], [36], [39].
Ø Hyperledger caliper
Hyperledger Caliper emerges as a pivotal tool for
evaluating the scalability, throughput, and latency of
blockchain networks. Developed under the Hyperledger
umbrella, Caliper provides a robust framework for
conducting comprehensive performance tests on various
blockchain platforms, including HLF, Hyperledger Besu,
and Ethereum.
At its core, Hyperledger Caliper offers a versatile and
extensible platform for executing performance benchmarks
on blockchain networks. Leveraging Caliper, developers and
researchers can design and execute custom test scenarios to
assess the performance characteristics of blockchain
networks under different conditions, such as varying
transaction loads, network configurations, and consensus
algorithms.
Key features of Hyperledger Caliper include its modular
architecture, multi-platform support, scalability,
comprehensive metrics, and integration with Hyperledger
benchmarks. These features enable users to customise and
scale the testing environment, collect detailed performance
metrics, and integrate with existing benchmarking tools
seamlessly.
As organisations explore the potential of blockchain
technology and deploy blockchain-based solutions in
production environments, Hyperledger Caliper plays a
crucial role in ensuring the performance and scalability of
these systems. By providing a comprehensive framework for
performance testing and benchmarking, Caliper enables
users to make informed decisions about the design,
deployment, and optimisation of blockchain networks [38],
[39].
IV. INFRASTRUCTURE ARCHITECTURES
In this chapter, the developed architectures will be
presented, accompanied by a series of tests conducted on
them, along with a detailed analysis of the results obtained.
A. ARCHITECTURES CONSIDERED
To understand the best architecture to be used, three
scenarios are considered for each of the architectures
developed, which will be presented and described below.
Ø Architecture 1 – Docker
This network is composed of several key components,
each running in Docker containers: Peers (one per machine),
Orderer (One per machine), couchdb (one per peer) and
chaincode (one per peer). To streamline the configuration
and management of this Docker-based network, a
comprehensive set of scripts are developed. These include:
Bash Scripts and Expect Scripts. This automated approach
significantly speeds up the configuration and reloading of the
network, which is essential for benchmarking and testing
purposes. By taking advantage of these scripts, it becomes
possible to perform repetitive tasks efficiently, quickly clean
up and reload Docker containers, and maintain consistent
configurations across different configurations.
Ø Architecture 2 - Kubernetes
In this project, a transition was performed to a
Kubernetes-based networking configuration, replacing the
previous Docker-only setup. This approach leverages
Kubernetes for enhanced resource management, high
availability, and scalability. This architecture contains the
same components as the Docker network, the difference is in
the sidecontainers for admin config communication, which
allow access from a single point of failure (multi-client).
Also, the chaincode here is a chaincode-as-service which
means that it works as another micro-service. The use of
Jenkins, scripts, multi-client and the Kubernetes API allows
cleaning and creating a new network instance for
benchmarking.
Ø Architecture 3 - Kubernetes with Load
Balancer
This architecture is similar to the one presented above,
differing in access. Where instead of communication being
carried out individually with each component, it is carried
out only with the single point of failure that loads the balance
evenly between the pairs.
In this project, to achieve load balancing for peers, a
NodePort service or a more advanced solution such as
MetalLB is used. When using a NodePort, services can be
exposed on specific nodes, but it has limitations:
customisation of the load balancer type is not allowed, and
the IPs must be in the range of 30000-32767, which prevents
defining a common IP or port such as port 80. This can be
impractical, as it requires specifying the exact machine
where the component will run.
On the other hand, MetalLB offers greater flexibility by
allowing the deployment of load balancers in either Layer 2
(L2) or BGP mode. With MetalLB, it is possible to define a
range of IP addresses and configure a common port, such as
port 80, which provides a more robust and predictable setup.
This approach avoids the randomness associated with
NodePort and ensures that the load balancing process is not
dependent on the specific node allocation.
However, there are still some aspects that require further
testing, particularly how the system behaves when querying
a channel that is not present on one of the peers behind the
load balancer. If the system fails in such a scenario, it may
necessitate assigning a unique address for each channel. This
would not be ideal as the cluster was designed with the
assumption that all peers participate in the same channel.
This design aligns with the goal of managing components in
a way that supports consensus across multiple organisations,
which is the fundamental purpose of using a blockchain.
While the current setup is focused on scenarios where
multiple organisations contribute to the consensus, it is
theoretically possible to create a cluster that includes
components from both this organisation and others. This
approach is valid for the implementation but would require
further consideration and planning.
B. EVALUATION
In order to understand/evaluate which of the presented
architectures is the best for the case study, four key metrics
were evaluated: CPU, RAM, DISK, and LEDGER variation.
For each test, a load environment in a hospital context was
simulated, with 10820 insertions carried out at a throughput
of 45 transactions per second (TPS), over 23 periods. During
this process, the errors recorded were deemed negligible, as
only one case was observed in 10820 insertions per test,
rendering them insufficient for a valid comparative analysis.
Therefore, it was decided not to consider them for
comparison purposes.
The results will be distinguished between Architecture 1,
with Docker, and the subsequent Architectures with
Kubernetes. The two technologies (Docker and Kubernetes)
are distinguished by their different applications, which
depend on the size, scale, and complexity of the network
under consideration.
Ø Evaluation: Architecture 1
The following image shows the results of the analysed
metrics regarding the architecture that uses Docker,
architecture 1.
In the image presented above it is possible to observe the
results of the metrics analysed for architecture 1. Starting the
analysis with the CPU variation, this shows a sharp initial
growth, followed by oscillations and a slight drop before
growing again until the end where it reaches the peak with a
value of 242.0.
Disk usage on this architecture starts at a low level and
shows steady growth until it peaks at 0.08 GB. After this,
there is a small reduction before growing again at the end of
the period.
Analysing the metric, use of the ledger grows gradually
over time, with some fluctuations until reaching a maximum
value of 0.01 at the end of the period.
Finally, analysing the use of RAM, it shows several
fluctuations. In the graph it is possible to observe specific
variations, but the trend is for growth over time, reaching its
maximum peak at the end of the period with a value of 1.66
GB.
Ø Evaluation: Architecture 2 and 3
The following image shows the results of the metrics
analysed in both architectures. The analysis is carried out
comparatively between both because they both use
Kubernetes. They differ from each other, while architecture
2 uses Kubernetes, architecture 3 uses Kubernetes with load 
In the image presented above, it is possible to observe that
architecture 2 shows a sharp increase in CPU variation,
reaching higher peaks, with a maximum value of 1571.50
while architecture 3 presents a maximum peak of 1515.10.
Analysing disk usage, both grow consistently, however,
architecture 2 has a higher disk usage with a peak of 0.75 GB
when compared to architecture 3 which has a peak of 0.72
GB. At the end of the analysis period, both showed a decline
and subsequently stabilised.
The use of the ledger in both architectures is practically
identical throughout the analysis. Both follow a similar
growth trajectory, with a maximum peak of 0.01 GB.
Finally, in relation to the RAM usage metric, both grow
consistently, however, architecture 3 has a slightly higher
RAM usage than architecture 2 throughout the analysis
period, reaching its peak at 5.63 GB.
C. DISCUSSION
Throughout this section, the different architectures will be
discussed, considering the test results in terms of scalability
and sustainability.
Firstly, the discussion will begin with an evaluation of the
results obtained from benchmarking, which are presented in
the following table.
TABLE 2
MAX/PEAK VALUES OF PERFORMANCE METRICS
CPU (Max
Variation)
DISK
(Peak Usage
(GB))
LEADGER
(Peak Usage
(GB))
RAM
(Peak
Usage
(GB))
Architecture 1 242,00 0,08 0,01 1,66
Architecture 2 1571,50 0,75 0,01 5,44
Architecture 3 1515,10 0,72 0,01 5,63
According to the results, Docker is observed to be more
performant due to the relatively small scale of the
environment. Docker’s lightweight architecture and
straightforward design make it an ideal choice in scenarios
where performance and resource efficiency are critical. Its
less abstract nature simplifies the learning curve and allows
for rapid deployment, making it particularly well-suited for
the current setup.
However, there is a certain degree of leverage Kubernetes
to power the UI tool developed in this project. Kubernetes’
robust API significantly streamlines the process of linking
and managing components, enabling the automatic listing,
addition, or removal of elements without compromising the
overall functionality of the platform. This flexibility is
crucial for maintaining the efficiency and reliability of the
UI tool, allowing for seamless updates and modifications as
the project evolves.
There are key differences between using Docker
exclusively and adopting a Kubernetes-oriented solution.
There are solutions where a simple Docker implementation
is sufficient. However, Kubernetes becomes more
advantageous and even essential as environments grow in
complexity and scale. It is designed to manage large-scale,
sophisticated deployments, offering features such as built-in
load balancing, comprehensive resource management, and a
strong API for managing complex resources. These
capabilities make Kubernetes a strong candidate for
environments where high availability, seamless scaling, and
resilience across multiple nodes are essential.
The following table presents some of the main
characteristics and distinctions between the two solutions.
TABLE 3
CHARACTERISTICS COMPARASION BETWEEN DOCKER AND
KUBERNETES
Characteristic Docker Kubernetes
More performance for smaller environments X
Less abstract and easier to learn X
Incorporated load balancer X
Resource management X
Robust API for managing resources X
High availability X
Built-in mechanism for horizontal scaling X
Higher resource overhead X
While Kubernetes does come with a steeper learning
curve and a higher resource overhead, these complexities are
justified in larger, more complex environments. In this case,
the smaller environment favors Docker for its performance
and ease of use. However, as the project expands and the
environment scales, Kubernetes will likely become the more
beneficial option due to its advanced features and ability to
handle larger workloads.
Regarding the comparison between Architecture 2 and 3,
even though the implementation of a load balancer had only
residual benefits in some of the metrics and that its
implementation may introduce complexity to the
development of the network, it provides several advantages
that, in the long-term, can be very beneficial. It can ensure
better scalability, reliability, resource allocation and
performance, contributing for the solution sustainability over
time [40, 41].
In summary, Docker has proven to be the more
performant solution for the current, smaller environment.
Yet, this project relies on Kubernetes for specific aspects,
such as the UI tool, due to its powerful API and management
capabilities. As growth is anticipated, the robust
management and high availability offered by Kubernetes by
deploying a load balancer will become increasingly valuable,
making it the preferred choice in larger, more complex
deployments.
Ø Final Architecture
In this final architecture it was implemented the same
setup as the one verified in the kubernetes with load balancer.
Here, the architecture is presented with additional
components that are essential to a production environment.
With this in mind, besides the core components, there are
also: prometheus (for fetching the data from all the cadvisors
and also components of the network), cadvisor (measures
collector for prometheus), cpp-rest-service (to wrap the data
from prometheus and serve it to the admin web server; it is a
good practise to not expose entirely the prometheus API),
keycloak (for users management), blockexplorerlistener (a
developed implementation of a block explorer listener to
grab the data from events and store it on a database),
postgresql-block-explorer (database for the blockexplorer
listener) and quarkus rest for serving this blockexplorer data
to the admin web server. Note that the multi-client now
serves the admin web server.
Figure 6. Chosen Architecture – Kubernetes with Load Balancer
V. PLATFORM FOR EFFICIENT BLOCKCHAIN
MANAGMENTE AND EXPLORATION
Throughout this section, all components related to the
developed platform will be presented and described. The
platform is divided into four main components: Block
Explorer, General Network, Order, and Peer Configuration.
Each of these four components will be presented along with
their features.
A. BLOCK EXPLORER
This first main component designed was the Block
Explorer, to monitor and manage network transactions. It
collects and stores data through a custom implementation
that captures all relevant details from the network. This data
is securely stored in a database, granting easy access and
analysis. Data is later processed by a backend architecture
that makes it available to the administrative web interface.
This system allows administrators to perform a number of
administrative functions over most parts of the Blockchain.
These include viewing the network activities by channel, the
performance of the network in considerable details, and the
inspection of blocks, transactions, and other related network
objects. It also enables the supervision and administration of
the components, as well as the channels they form part of,
which are necessary for the network to operate.
In the dashboard, users can access detailed metrics,
including the number of blocks, transactions, nodes,
chaincodes, and peers within the system. Additionally, the
dashboard provides insights into the percentage of
transactions categorized by organization, allowing for a clear
understanding of activity distribution. A timeline-ordered
block list is also available, offering a chronological view of
block creation and updates. All of this information is
meticulously organized by channel, enabling users to easily
navigate and analyze data specific to each channel.
In the network section, users can access a comprehensive
list of nodes currently participating in the channel. This list
is similar to the one found in the dashboard but offers more
detailed information for each peer. For instance, it includes
the peer’s IP address, type, Membership Service Provider
(MSP), the number of transactions it has processed, the
number of chaincodes it supports, and its current status
(whether it is active or not). As with the dashboard, all of this
data is organized by channel, allowing users to focus on
specific channels as needed.
Figure 4. Block Explorer – Network
In the blocks section, detailed information about each
block is provided, including the channel it belongs to (which
is obvious since it is possible to select the channel to inspect),
its data hash, the number of transactions it contains and its
size within the ledger.
Figure 5. Block Explorer – Blocks
In the Transactions section, users can access a
comprehensive overview of all transactions, each
accompanied by detailed information organised by channel.
This includes the creator of the transaction, the name of the
channel in which the transaction occurred, the transaction ID
(TX ID) for unique identification, the type of transaction
performed, the name of the chaincode invoked, and the
precise timestamp when the transaction was executed. This
detailed breakdown, organised per channel, allows users to
thoroughly analyse and track each transaction, ensuring
complete transparency and traceability within the system.
Figure 6. Block Explorer – Transactions
In the Chaincodes section, users can view detailed
information related to the chaincodes within a given channel,
including the chaincode name, associated channel, number
of transactions, and the version of each chaincode.
Figure 7. Block Explorer – Chaincodes
In the Channels section, users can access detailed
information about each channel, including the chaincode
name, associated channel, the number of transactions per
chaincode, the version, and the timestamp.
Figure 8. Block Explorer – Channels
B. GENEREAL NETWORK
This part analyses the resource utilization of the network.
It provides monitorization of several performance metrics:
CPU, RAM, disk usage, ledger activity, I/O operations, and
network performance. Also, it presents the resources within
each cluster, a graphical representation of the network’s
structure, and allows for an examination on their
configurations and how they are organized within each
component’s directory.
In the “Dashboard” section it is possible to have a
glance of all the network like: checking number of nodes,
alive nodes, dead nodes,CPU variation %,Disk usage per
machine GB, Disk usage machine %,Ram per machine
GB,Ram per machine %. Relatively to the network scheme
thats a probable future feature of changing between clusters
because this is cluster oriented.
Figure 9. General Network – Dashboard
The “Resources” section provides a list of the services
residing in that cluster, each corresponding to the DNS name
of that service.
Figure 10. General Network – Resources
The “Network Visualization” section includes a
cluster-oriented representation of the current components.
This is cluster-oriented, as it groups resources according to
what is in the cluster and not to any particular network
channel. If it were based on a network channel, the
visualization could include components outside of cluster.
Figure 11. General Network – Network Visualization
C. PEER CONFIG
This section deals with peer management and provides a
comprehensive user interface for performing all standard
peer operations, like: uploading configurations, querying,
fetching and joining channels, installing, querying, aproving
and committing chaincode, checking chaincode approvals,
invoking chaincode for testing, and executing custom
commands for more advanced operations.
The following images present some of these operations,
namely: ”Upload Configs”, where peer configurations can
be uploaded, such as the chaincode package for installation.
Figure 12. Peer Config – Upload Configs
”Fetch Channels”, where the user can fetch a channel
from the orderer. To achieve this, they must provide the
channel name, the TLS CA file path, the certificate file path,
the key file path, and the IP address of the orderer from
which they want to fetch the channel.
Figure 17. Peer Config – Fetch Channel
”Install Chaincode”, where a list of the uploaded files
from the ”Upload Configs” section can be found, allowing
the user to easily select the desired chaincode .tar.gz file for
installation.
Figure 18. Peer Config – Install Chaincode
”Custom Commands”, where the user have all the
necessary tools to create a custom command with a peer,
which can be valuable in unexpected situations.
Figure 19. Peer Config – Custom Commands
D. ORDERER CONFIG
This section focuses on the management of the orderer
and provides a comprehensive set of tools for efficiently
handling all regular duties. Users can create new channels,
join existing ones, and execute custom commands for more
complex configurations.
The following images present some of these operations,
namely:
”Creating Channel”, where the user is able to create a
channel on a selected orderer. To do this, they need to select
an orderer, attach a channel configuration file
(configtx.yaml), name the channel, and submit the request.
Figure 20. Oderer Config – Creating Channel
”Query Channel”, where channels associated with a
given orderer can be queried. To perform the query, the user
must provide the orderer IP, TLS CA path, client key path,
and client certificate path.
Figure 21. Oderer Config – Query Channels
”Custom Commands”, where the user can run custom
commands in the orderer component when custom
interactions are needed with the networks’ orderer.
Figure 2213. Oderer Config – Custom Commands
VI. CONCLUSION
To summarize, in terms of Infrastructure Architectures,
three implementations were developed during the project:
one using Docker, other using Kubernetes and a third one
using Kubernetes alongside with a load balancer. This
implementations evolved as we developed further in time,
aiming to firstly create the most basic network (docker),
secondly to present a more robust architecture that could also
be used to manage better a infrastructure that could evolve in
number of components with time (kubernetes) and lastly to
a infrastructure where we could balance traffic within a same
channel contained in a certain number of components
(kubernetes with load balancing). Docker is suitable for
small businesses due to its greater simplicity and ease of use
although more work overhead around setting how
components must communicate, while Kubernetes is better
for treating components as simple resources designed for
larger, more complex environments, more scalable,more
incremental and easier to maintain architectures. We also
benefit of features provided by the kubernetes API, that we
can use to obtain information about concrete resources that
we can use to create analysis tools like the ones mentioned
in our project. With kubernetes, regardless of the number of
components we have we will be able to use this analysis tool
without further configurations than the resource itself. The
Kubernetes with load balancer (K8 with LB) approach was
chosen. This makes sense because of all of the characteristics
mentioned so far that are very suited for a infrastructure for
the healthcare industry—a sector that demands a large,
resilient infrastructure and advanced features to manage and
monitor the network for its administrators, aligning with the
primary goal.
Speaking about the platform itself, the system developed
provides a robust and comprehensive solution for monitoring
and managing the HLF network. This is only possible due to
the selected solution. The system guarantees continuous
access and analysis through its design architecture, where
various critical statistics are consolidated. This system not
only replicates but also improves on the functionality of
previous solutions, allowing administrators to perform a
wide range of tasks with greater efficiency and precision all
in one single place, reducing errors as common network tasks
are successfully automated and monitoring is provided.
More concretely, the system provides more than a basic
network management. It offers information about resource
utilization, peer management and orderer operations. It also
provides a user-friendly interface to easily handle complex
tasks such as monitoring network activity, managing
resources or adjusting settings. This is a solution that offers
everything that an administrator needs to control its network.
VII. FUTURE WORK
When it comes to future work, we have several ideas to
improve several aspects of the developed architecture. This
improvements range from creating automatic components
from existing templates using the UI, creating recovery
plans,improving the documentation,improving the current
UI,develop security protocols and search about current
regulation for private ledgers. The idea is to create
mechanisms that support the platform in the long term.
A. AUTOMATING NETWORK COMPONENT
GENERATION
This will focus on automating the generation of network
components, such as peers and orderers, directly in a user
interface (UI). This automation will be possible by using
scripts and a standard template to the creation process,
reducing the need for manual configuration which results in
a reducing of errors. By integrating this directly in the the UI,
we can significantly improve operational efficiency by
enabling rapid deployment and management of HLF
components. This approach will allow network
administrators to create new components with ease, which
will give them more time to plan how exactly they want their
network to be because creating it by themselves creates a
huge overhead due to the number of configurations that can 
result in unexpected behavior, which may cause a very huge
loss of time.
B. CREATING RECOVERY PLANS FOR HLF
COMPONENTS
Because the HLF is a complex infrastructure, developing
recovery plans for components is of much importance. With
this in mind, it is planned to actually create a set of detailed
plans for given situations that outline the steps necessary to
quickly identify, contain, and recover from failures in these
components. These recovery plans will be essential to know
exactly what to do when some unknown behavior happens,
which is something that we should give special attention due
to the importance of the probable use case. By implementing
this recovery strategies, organizations can feel confident to
use our solution for their HLF networks and know for sure
that the system remains resilient to a vast number of
situations, preserving data integrity and service continuity.
In case some new case occurs, we have also plans to create a
community that communicates faced challenges, that later
one could be added to this recovery plans because this work
must be continuous.
C. IMPROVING DOCUMENTATION PRACTICES
Documentation often lacks in clarity and accessibility,
which can lead to misunderstandings and inefficiencies
while working with the given product. Because we have our
own documentation for this project, it is important to refactor
it in order to create well-formatted documentation that is
easy to use and clearly explains how to certain tasks that may
be required depending of the objective of the Administrator.
Improving the documentation is something that we see as
very important, as it will be the basis for current and future
administrators and programmers to take advantage of the
created features in our project making it easier to work with.
It also helps with onboarding new team members and
ensuring consistent practices across the organization. The
point of access to our documentation is still under work but
it is expected to be available in our UI.
D. IMPROVING THE CURRENT UI
Despite being very composed, our current UI must be
even more improved. There are features to be added and
others that must have further modification as for now it is
still in a beta version. With this in mind we want to: Add a
menu for documentation, which we already discussed in the
section before, develop a mechanism that allows
administrators to select and manage multiple clusters
simultaneously in order to address the increasing complexity
of network infrastructures. This multi-cluster management
capability will be a good ally for managing multiple clusters
which may be a big ally for bigger organizations improving
scalability and reducing administrative burden. In addition to
what was previously mentioned, a new menu option will be
introduced precisely to provide a tree model view of the
component structure. This feature is meant to understand the
current position of given artifacts needed for certain
operations within the network (certificates,config
blocks,etc..).Finally, the development of a geopositioning
map that aims to display the physical location of network
components. This feature will allow administrators to view
the geographic distribution of components, which can be
something valuable for physical interaction with components
of the cluster (like a node for example), although not as much
relevant as the other ideas discussed before it remains as a
very good feature for this project.
E. DEVELOPING PROTOTYPES FOR ENHANCED
SECURITY PROTOCOLS
Because security is so important, especially in the context
of service authentication within the network there is a need
to strengthen the procedures to this effect. With this in mind,
there is future work that must involve the development of
prototypes for security protocols. The idea is to implement
optional extra steps for authentication that secure even more
our platform. This is what will enable those services that
collect block explorer data, manage peer connections, and
manipulate Prometheus data servers. These new protocols
will focus on strengthening the security of those services,
ensuring that they are protected against unauthorized access
and potential threats. There are ideas that got discussed
already about this matter, like for example creating a
structure such that does not allow the access if one of the
steps gets compromised. Also something that will evolve
more and more with the time.
F. GATHERING REGULATORY INFORMATION ON
PRIVATE LEDGERS AND HORIZONTAL SCALING
As private ledgers are being developed, remaining
informed about the regulatory landscape will be very crucial.
It therefore follows that there is future work related to
collecting and analyzing information about regulations
related to private ledgers. Such regulations make it easier to
shape the network architecture for it to meet the legal
impositions that exist around different countries or even use
common standards to have broad acceptance of the platform.
This work is also incremental, especially in view of the
emergent nature of the matter discussed, where more and
more standards come into play.
G. HORIZONTAL SCALING
Horizontal scaling, or scale-out, is a critical optimization
of the system to manage more workload—notably within
containerized environments—into one node, while 
horizontal scaling will increase the number of nodes to share
a load over more than one machine.
This means that in the case of Hyperledger Fabric (HLF),
which is a commonly used distributed ledger platform for
blockchain-based solutions, there is a potential application of
horizontal scaling. It would be quite interesting, to say the
least. In the case of Hyperledger Fabric (HLF), since a
network often involves the co-existence of multiple
organizations, which are usually referred to as consortiums,
the potential key issue of effective performance optimization
may lie in the ability to scale horizontally when the size and
complexity of this kind of network grows. Horizontal scaling
will allow the number of instances in the system to bend with
real-time traffic demands, or surges in computational
work—things that normally accompany every organization
in an HLF network. Every organization within an HLF
network operates its own set of peers including services for
ordering and many other components.
In this regard, we will predict for subsequent work how
much horizontal scaling can be done with an HLF network.
We will look especially at when it can be pushed forward—
when no diminishing returns from the system's architecture
meet a bottleneck. This will comprise the evaluation of
different factors like latency, throughput, and resource usage
under different scaling scenarios. We also want to verify if
the application of horizontal scaling in such networks offers
real advantages for large consortiums, mainly those
operating with a high volume of transactions or in need of
high fault tolerance.
This is significant potential for research, as it could bring
insight that is useful to organizations running large-scale
HLF networks. With this, architectural teams would then
have the knowledge of whether horizontal scaling really
yields measurable improvement in performance and
resilience that is satisfying to their operational needs.
Finally, findings emerging from this work may help
consortiums understand the trade-offs involved and make a
decision on whether horizontal scaling could really be a
feasible and beneficial approach for the considered
blockchain projects.