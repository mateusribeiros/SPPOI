Title: IoMT and Blockchain Synergy: A Novel Approach to Health Data Validation and Storage

ABSTRACT The increasing adoption of Internet of Medical Things (IoMT) devices is revolutionizing
healthcare, facilitating enhanced remote patient monitoring and data-driven clinical decision-making.
However, a significant challenge remains: the fragmentation of sensitive medical data across diverse
healthcare infrastructures. This separation of medical data seriously hinders seamless data exchange and
interoperability, preventing healthcare providers from obtaining a comprehensive understanding of patient
health and limiting the scope of data-driven research for improved treatments. To address this critical
issue, we have developed a novel blockchain-based framework carefully designed to unify separate IoMT
data sources within a secure platform. This framework aims to enhance data accessibility, ensure robust
data security and patient privacy, and significantly improve the depth of clinical understanding, ultimately
leading to enhanced patient care. Our system employs Hyperledger Fabric, a permissioned blockchain
architecture, selected for its security, scalability, and suitability for handling sensitive healthcare data.
We further integrate edge computing principles to optimize data processing efficiency and reduce network
latency, establishing a decentralized architecture that prioritizes data integrity and confidentiality. This
innovative approach to IoMT data integration aims to enable secure, real-time data sharing and improve
interoperability across diverse healthcare ecosystems. By facilitating seamless data flow and establishing a
trustworthy and auditable data infrastructure, our framework supports enhanced clinical decision-making
in crucial areas such as remote patient monitoring, chronic disease management, and preventative care.
Rigorous performance evaluations demonstrate the potential of our framework to transform healthcare
workflows, improve operational efficiency, and maximize the utility of IoMT data for improved healthcare
delivery and patient-centric models of care. This research represents a significant step toward realizing more
interconnected, secure, and efficient healthcare systems for the future.
INDEX TERMS Blockchain, edge computing, health data, IoMT, monitoring system, pulse oximeter.
I. INTRODUCTION
The Internet of Things (IoT) has emerged due to the growing
number of linked devices, which are improving many facets
of human existence, including healthcare. The Internet of
Medical Things (IoMT) [1], which uses IoT to deliver
intelligent and widespread healthcare services, is the result of
this evolution. These systems usually consist of a cloud-based
data center, an internet gateway, and wearable sensing
devices. Wearable devices connected to a wireless body area
network (WBAN) create personal health data, which can be
analyzed locally on the gateway device or forwarded to the
data center for further in-depth analysis[2]. Despite the benefits of real-time data processing, in-depth data analysis is still
critical for achieving a better understanding [3]. Digitization
of patient records and physiological data, including heart
rate, EKG, blood sugar level, etc., for remote monitoring,
decision-making, and medical research. The development
of information technology and IoT health devices has
completely revolutionized the health system. The fragmented
storage and management of clinical data hamper large-scale
health data research and smooth information interchange. The
Internet of Medical Things (IoMT) segment includes smart
devices, like wearables and medical/vital surveillance, that
are only used in the healthcare sector at home, in clinics,
hospitals, telemedicine, and other services [4]. IoMT makes
it possible to handle data reliably, streamline processes,
reduce waste, and lower the possibility of errors. IoMT
provides medical treatment in real-time, reducing the need
for physicians to be physically present [5]. Among the
most critical issues that must be addressed in IoMT data
management are data privacy regulations, communication
blockages needed due to unusual physical conditions, the
increasing likelihood of security breaches, and the usage of
blockchain technology in delicate situations [6]. Networks
in many medical facilities are not stable enough to support
IoMT devices. Doctors may encounter problems retrieving
patient information due to the large volume of data being
transferred [7]. With blockchain technology, patients can
establish guidelines for who can access their medical records,
giving certain researchers temporary access to specific
parts of their records [8]. Blockchain technology allows
patients to connect to their institutions and automatically
collect their medical information. Smart contracts maintain
the blockchain’s security and privacy. Wireless networks
and blockchain technology enhance data transmission efficiency and security. Wireless networks support real-time
communication and the Internet of Things (IoT), while
blockchain ensures data integrity through decentralization
and cryptography. [9] Their integration can transform sectors
like finance and healthcare by enabling secure transactions
and addressing challenges in data security and privacy,
driving innovation in an interconnected world [10].
A. THE SIGNIFICANCE OF IoMT DURING THE
CORONAVIRUS ERA
In response to COVID-19, several medical technologies
have shown promise in lowering the need for hospital visits
through remote patient monitoring, especially for patients
with chronic illnesses. For instance, pulse oximeters detect
heart rate and blood oxygen levels, sending data via regular
connections for extensive health monitoring. Urgent care is
prioritized, and quick therapy modifications are supported
by such technology. Combined with smartphone apps and
smart thermometers, these techniques improve public health
responses by enabling real-time tracking of flu trends across
demographics [11].
Decentralization of IoMT health monitoring devices paired
with blockchain-based storage can provide secure and
scalable access to data with remote data management
to advance health data research and healthcare delivery.
A gateway device collects sensitive health data from health
monitoring device users and uploads the data to a centralized
cloud storage service to analyze the data. Data access for
other stakeholders via a web service (API) [12]. Centralized
cloud health service is a content approach for users to utilize;
however, it has a challenge in data interchange [13].
To protect user privacy, processes must ensure sensitive health data is secure, as cloud services managed by
third-party providers may limit users’ control over access.
Also, for critical health decisions, data should be preserved
still and not subject to any change while transmitted or stored.
However, most centralized cloud systems cannot provide
good data integrity and confidentiality guarantees [14].
As a solution to these problems, permissioned blockchain
can provide an effective platform for secure storage and
scalability due to its characteristics with its data integrity
and decentralized peers. A blockchain is a distributed ledger
where numerous nodes preserve a ledger that records changes
to an asset through transactions. A validation process that
ensures that there is no discrepancy of data in the database
when a transaction is initiated on any of the nodes.
Unlike public blockchains (such as Ethereum or Bitcoin),
which are open to anyone, permissioned blockchains —
like Hyperledger — limit network membership to approved
nodes. Hyperledger also provides private channels, i.e.,
it allows specific node sets read access to particular ledger
data [15]. Using a simpler Byzantine Fault Tolerance (BFT)
consensus instead of the complex Proof-of-Work (PoW)
consensus in public blockchains, Hyperledger Fabric can
handle sensitive information better, making it ideal for private
medical data produced by IoT medical devices.
The proposed framework utilizes the Internet of Medical
Things (IoMT) for the secure recording and storage of health
metrics (including body temperature, pulse rate, oxygen
saturation, and Photoplethysmography (PPG)). Wearable
data is processed in different steps to prepare for secure
storage in a distributed ledger. Besides assuring data integrity
and security, the system facilitates real-time access and
visualization of data for persistent, reliable health status monitoring. It delivers a holistic, multi-disciplinary, decentralized
tool for continuous, secure, readily available access to vital
health information.
B. MOTIVATIONS
Although the current IoMT healthcare systems focus on
data collection and remote monitoring, they fail to consider
transaction latency, device connectivity, scalability, and
optimized patient service. We present a novel framework
to implement the IoMT with edge computing for real-time
processing of the data collected by the IoMT devices,
reducing unnecessary resource usage, less network traffic,
and improving performance to provide the best possible
service to the patients. A blockchain-based system enhances
data privacy, accessibility, and integrity by providing a secure,
decentralized, and transparent system for storing and sharing
health data among parties transparently.
C. CONTRIBUTIONS
The contributions of this proposed effort are best summarized
as follows:
• The proposed Framework combines IoMT devices with
edge computing and blockchain technology, enabling
efficient real-time processing and secure storage of
healthcare data, such as pulse rate and oxygen levels.
This integration minimizes latency and improves data
handling.
• By utilizing Hyperledger Fabric’s blockchain, the system ensures that healthcare data is stored securely
and immutable. This decentralized approach enhances
patient privacy and trust, preventing unauthorized access
and ensuring data integrity through a robust consensus
mechanism.
• The Framework provides real-time data visualization
through an intuitive frontend, allowing healthcare professionals to monitor patients effectively. This feature
facilitates immediate insights into patient conditions,
improving responsiveness in care.
• Designed to accommodate a growing number of IoMT
devices, the system optimizes resource management.
It reduces network traffic, ensuring sustained performance and shorter patient wait times as the healthcare
network expands.
II. BACKGROUND
A. BLOCKCHAIN
Blockchain, a distributed ledger introduced in 2008
[16], combines consensus algorithms, cryptography, and
distributed technologies. Its unique chain structure provides immutability and traceability, making it a secure,
tamper-resistant platform that ensures data privacy without third-party involvement. Blockchain can potentially
address significant IoT platform management and security
issues [17]. In medical research, blockchain can create a
universal platform for securely tracking personal information,
storing health data, and enabling accurate access, benefiting
patients, researchers, and healthcare providers [18].
Blockchain applications for secure transactions include:
• Asset transfer [19].
• Supply chain management for asset and product traceability [20].
• Protection of private information [21], [22], [23].
The global COVID-19 pandemic emphasized the crucial
need for effective data exchange across healthcare stakeholders to speed up research. The massive gathering of medical
data yielded insightful information for tackling the challenges
related to the virus. However, it is crucial to safeguard patient
privacy and ensure adherence to international regulations like
HIPAA. Monitoring data access and changes throughout its
lifecycle while guaranteeing safe and effective user sharing
is a major challenge [24], [25], [26], [27], [28].
IoT-enabled Patient Health Monitoring: A fast-developing
technology like IoT can easily be blended into patient health
monitoring because of its applicability to measure vital
signs like blood pressure, temperature, oxygen saturation,
and heart rate. Integrating blockchain with these devices
improves patient privacy by decentralizing control over
globally exchanged data and gives patients more power. The
decentralized nature of blockchain also means that the data is
protected from fraud and unauthorized manipulation because
of the clear visibility, which also gives the data privacy
and transparency. Together, these two simplify the confident
collection, sharing, and storing of medical information and
are a game-changer in how we handle healthcare.
1) BLOCKCHAIN FEATURES
Features of Blockchain include: Decentralization: Blockchain technology ensures trust through decentralized validation, eliminating third-party supervision while maintaining
transaction integrity [29].
Transparency: The immutable nature of blockchain enables
permanent record-keeping and universal access to transaction
history, facilitating comprehensive financial tracking and
verification [30].
Security: Blockchain’s distributed architecture and
immutability provide robust protection against data theft in
healthcare systems. Research demonstrates its effectiveness
in enhancing healthcare security and privacy [31], [32],
particularly in IoT-enabled healthcare applications [33].
2) BLOCKCHAIN TYPES
Blockchain can be classified into four types:
Public: A fully decentralized network allowing unrestricted
global participation without permissions. It operates on peerto-peer architecture, enabling universal read-write access
and audit capabilities. Transactions are timestamped and
validated through collective voting, ensuring transparency
through distributed ledger visibility, with incentivized participation [31].
Private: A controlled-access network requiring authorization, typically used within organizations prioritizing privacy
and efficiency over decentralization. The central authority
manages data access and transaction validation, offering
enhanced scalability compared to public blockchains [32].
Consortium: A hybrid solution between private and public
blockchains, operated by select organizations controlling
network access. It is primarily utilized when multiple entities,
such as banks or government institutions, require secure data
exchange within a regulated framework. Consensus participation is limited to authorized entities with configurable data
visibility policies [33].
Hybrid: Combines private and public blockchain features,
offering greater flexibility than consortium models. Maintains selective privacy while enabling public verification of
specific data, making it suitable for applications like supply
chain tracking and healthcare systems requiring varied data
accessibility [34].
TABLE 1. Blockchain types.
B. IoMT
The IoMT devices function with smart, low-energy, wirelessly enabled, effective, secure media. IoMT devices are
typically employed to determine, modify, gather, examine,
and safeguard a patient’s biometric information. These tiny
sensors normally gather data on a patient’s position, body
weight, measurements, sleep patterns, oxygen saturation,
temperature, and heart rate. The IoMT has emerged due to
IoT, and examples of ‘‘medical things’’ include different
medical things like beds, ambulances, and devices with
sensors built into them.
III. RELATED WORKS
IoMT-based smart healthcare systems are developing rapidly,
demanding greater stability and robustness regarding privacy,
lower latency, higher reliability, and security. In this section,
we present several papers related to smart healthcare systems
and health monitoring systems.
Jabbar et al. [20] describe a framework that uses the
Internet of Medical Things (IoMT) for safe patient health
monitoring with blockchain to assure data confidentiality.
To address concerns about medical confidentiality, the system
uses smart sensors to gather important health measurements
and an embedded Raspberry Pi 4 platform to process them.
Arul et al. [33] describe integrating blockchain, cloud
computing, and IoMT to extend healthcare by providing
improved patient care and data management. However,
there have been reports of issues with cost calculation
and coordination between servers and suppliers, which may
impact the system’s effectiveness. Furthermore, because of
the sensitivity of medical data and the lack of server trust,
implementing clinical route inquiry services may present
major privacy issues for patients.
Mallick and Sharma [34] propose the Electronic Medical
Record Infrastructure (EMRI) framework that addresses
scalability, security, and privacy in the Internet of Medical
Things (IoMT) through a decentralized blockchain approach.
It ensures secure healthcare data transactions and efficient
communication while protecting patient privacy. The system
uses a consensus mechanism for block verification, where
miner nodes validate the transactions and add new blocks.
Also, the smart contract feature of EMRI protects and
safeguards patient’s sensitive information from unauthorized
access.
Garg et al. [35] present a lightweight and efficient
authentication and key agreement protocol tailored for
IoT environments, particularly in Industry 4.0. The implementation utilizes elliptic curve cryptography and other
lightweight operations to ensure security while minimizing
computational overhead. The protocol was evaluated using
automated validation tools, demonstrating resilience against
common security threats such as denial of service and
spoofing attacks.
Alabdulatif et al. [36] propose the Privacy-Preserving
Edge of Things (EoT) framework (PPEOTF) for secure
Edge of Things and Smart Healthcare Surveillance. One
major challenge is how the Cloud of Things will manage
the data generated by billions of connected IoT devices.
Edge computing is a potential method that acts as a bridge
between IoT devices and cloud computing. They developed
a privacy-preserving Edge of Things (EoT) Framework
(PPEOTF) for smart healthcare surveillance.
Dai et al. [37] present a framework combining blockchain
technology with edge intelligence to enhance Internet of
Medical Things (IoMT) systems for addressing challenges
posed by COVID-19. The proposed architecture integrates
blockchain and A.I. at three levels—device, edge, and
cloud—to provide trusted intelligence for IoMT applications.
Key techniques include using blockchain for secure data
management and edge computing for low-latency A.I.
processing near IoMT devices. The paper discusses applying
this Framework to COVID-19 use cases like contact tracing,
aerosol surveillance, vaccine supply chain tracking, and
telemedicine. It leverages IoMT devices, edge nodes, cloud
servers, and blockchain’s immutability and security to enable
privacy-preserving, real-time analytics and decision-making
for pandemic response.
Uddin et al. [38] present a blockchain-based privacypreserving architecture to monitor patient health continuously. The blockchain includes a Patient-Centric Agent
(PCA) for remote monitoring. The PCA is responsible for
sorting stored data depending on its criticality, which benefits
drillers.
Cui et al. [39] propose a multi-wireless sensor network
authentication system based on blockchain technology for the
Internet of Things. The system divides the IoT nodes into
base stations, cluster heads, and normal nodes based on their
capacities and in separate chains.
Guo et al. [40] merge the advantages of edge computing
and blockchain technology to offer a distributed authentication system for Internet of Things terminals. An edge-based
caching technique was used to improve the hit ratio.
Egala et al. [41] propose a novel architecture for
decentralized healthcare systems that leverages blockchain
technology, hybrid computing, and distributed data storage
systems (DDSS). It addresses critical issues such as high
latency and security vulnerabilities by introducing a selective
ring-based access control mechanism and algorithms for
patient anonymity and device authentication. This approach
enhances privacy and security while enabling real-time
patient monitoring and low-latency services in Internet of
Medical Things (IoMT) environments.
TABLE 2. Summary of key contributions and methodologies in IoMT
security.
IV. RESEARCH GAP
While extensive research is being done in remote healthcare monitoring with IoMT devices, a fundamental gap
exists in maintaining patient data’s complete security and
privacy. Existing solutions tend to concentrate on data
transmission and device functionality while overlooking the
critical importance of data integrity and privacy protection
mechanisms. In addition, blockchain technology and smart
contracts for data privacy, transparency, and security in
healthcare data monitoring are largely untapped areas. This
disparity emphasizes the need for a special framework
that tackles confidentiality and data integrity issues and
strengthens patient data security by utilizing cutting-edge
technology.
FIGURE 1. High-level architecture diagram.
V. THE PROPOSED DESIGN
This section proposes a system architecture that leverages the
Internet of Medical Things (IoMT) devices, edge computing
nodes, middleware for data validation, and a Hyperledger
Fabric blockchain network for secure, decentralized health
data storage. Figure 1 shows the flow of our overall system
architecture.
The system is designed to ensure real-time data monitoring, immutability of health records, and secure data
transmission through cryptographic techniques, including
one-way cryptographic hash functions and decentralized
storage. The system consists of the following components and
processes:
A. IoMT DEVICE AND DATA COLLECTION
The IoMT-based pulse oximeter enables real-time peripheral
arterial blood oxygenation monitoring through spectral
analysis of oxygenated and total hemoglobin. As illustrated
in Figure 2, the system architecture centers on an MCU
with integrated DAC functionality for LED control. The
signal processing chain comprises a low-pass filter (0-5 Hz)
for noise reduction and multiplexed segregation of red,
I.R., and ambient signals, followed by sample-and-hold
circuitry and bandpass filtering (0.5-5 Hz). Subsequently,
the amplified signals undergo analog-to-digital conversion,
separating AC/DC components before MCU processing.
These hardware signals constitute the main system inputs
for real-time SpO2 and PR-critical metrics analysis, with
integrated algorithms managing emergency responses. These
algorithms embody the core technology ensuring monitoring
accuracy and timeliness, while onboard Wi-Fi facilitates edge
node data communication.
As illustrated in Figure 3, the signal processing chain
encompasses sequential stages for precise SpO2 and pulse
rate measurements, progressing from initial filtering and peak
detection through standard deviation acquisition and RED/IR
normalization to state distinction. The parameter calculation
phase employs a two-stage computation approach to derive
FIGURE 2. Pulse oximeter system configuration.
final SpO2 and pulse rate measurements from the processed
state data.
1) DIGITAL FILTERING
By using a bandpass filter with the low cut-off frequency of
flow = 0.1 Hz and a high cut-off frequency of fhigh = 9 Hz
with a sample rate of 160 Hz, the filtered signal Sf (t) can be
represented as:
2) PEAK DETECTION
Once filtered, the algorithm detects the peaks, P, in Sf (ti).
Peaks can be extracted by identifying local maxima that
exceed a specified threshold.
P = {Sf (ti) | Sf (ti) > Sf (ti−1) and
Sf (ti) > Sf (ti+1) and
Sf (ti) > threshold} (1)
3) STANDARD DEVIATION FILTERING
The peaks are then filtered based on their dispersion; hence,
the noise decreases. Considering the set of peaks detected, P,
compute the standard deviation, σP, and retain peaks that are
within one standard deviation of the mean.
P¯ =
1
N
X
N
i=1
Pi, σP =
vuut
1
N
X
N
i=1
(Pi − P¯)
2
(2)
Filter peaks based on:
Pfiltered = {Pi
| |Pi − P¯| ≤ σP} (3)
FIGURE 3. Visualizing biosignal data. An HTML view built with Express.js
and ejs for real-time monitoring of PR, SpO2
.
4) NORMALIZATION OF RED AND I.R. SIGNALS
Normalize the red and infrared signals to align both signals
in range. Let R and IR represent the red and infrared signals:
Rnorm =
R − min(R)
max(R) − min(R)
,
IRnorm =
IR − min(IR)
max(IR) − min(IR)
(4)
5) SPO2 PARAMETER AND PULSE PERIOD CALCULATION
Let the amplitude A be calculated for each peak component:
Ared = max(Rnorm) − min(Rnorm)
AIR = max(IRnorm) − min(IRnorm) (5)
For SpO2, the red and I.R. amplitudes are related to direct
current (D.C.) and alternating current (A.C.) components for
each signal:
Ratio =
Ared
DCred
AIR
DCIR
(6)
6) PULSE RATE AND SPO2 CALCULATION
The pulse rate (P.R.) is calculated by identifying the time
interval T between consecutive peaks:
PR =
60
T
where T = ti+1 − ti (7)
SpO2 is calculated using an empirical formula (usually
derived experimentally):
SpO2 = a − (b × Ratio) (8)
where a and b are calibration constants typically provided by
the sensor manufacturer.
7) SIGNAL STATE CLASSIFICATION
The final state S is classified based on signal stability and
noise level:
S = f (x) =



stable if |PR − PRnorm| < ϵ and |σ| < δ
unstable if σ > δ
otherwise (if neither condition is met)
(9)
where PRnorm is a baseline pulse rate, and ϵ and δ are
threshold values for stable detection. This Framework provides a step-by-step, quantitative methodology for extracting
SpO2 and P.R. in consideration of noise and stability for
precise measurement.
B. EDGE COMPUTING NODE: DATA PROCESSING AND
PREPARATION
Edge nodes facilitate real-time data processing and analysis,
optimizing system performance for IoMT-generated biosignal management. In the proposed system, these nodes
incorporate Python-based servers that decode ASCII streams
into structured metrics (PR, SpO2, and temperature) and
JSON objects. TCP/IP socket connections, which include
device identification, command coding, and cyclic redundancy check (CRC) verification, are used in the suggested
approach to enable dependable data transmission. According
to Table 3, the wireless communication protocol comprises
two ASCII bitstream packets intended to send raw signal
information and vital sign data.
TABLE 3. Packet Structure for IoMT device communication.
The data storage mechanism for biosignals measured
by IoMT pulse oximeters requires robust technology that
manages high-volume, real-time data processing. As the
FIGURE 4. Visualizing biosignal data. An HTML view built with Express.js
and ejs for real-time monitoring of PR, SpO2
.
IoT pulse oximeter measures biosignals over time, the data
collection must be handled efficiently. The biosignal data is
sent to our middleware (Express.js) via REST API to do this.
It manages and integrates the data efficiently.
TABLE 4. Data types and descriptions for IoMT device data.
C. MIDDLEWARE: VALIDATION AND API MANAGEMENT
The proposed system uses express.js, a server-side framework, to create the middleware layer to enable REST API
communication between the blockchain and the edge node.
The middleware layer implements an event-driven architectural pattern coupled with Server-Sent Events (SSE) for
real-time data propagation. This approach enables efficient
data flow while maintaining system reliability. The express
server examines the data packet’s structure to verify that all
necessary fields (PR, SpO2, etc.) are present and structured
correctly. The packet, after verification, is then sent to the
Hyperledger fabric blockchain for storage after successful
verification.
D. BLOCKCHAIN INTEGRATION WITH HYPERLEDGER
FABRIC
Hyperledger Fabric is an open-source blockchain framework
supporting different types of nodes and consensus mechanisms (Byzantine Fault Tolerance, Raft, Kafka, and Solo),
of which the Raft is the most decentralized. The Framework
consists of orderer nodes responsible for transaction ordering
and block creation, followed by specialized peer nodes
(endorsement, committer, and anchor nodes) responsible for
transaction proposal validation, ledger storage, and communication across organizations. The implemented system
is based on a permissioned network architecture consisting
of three nodes that tolerate faults and achieve a higher
throughput designed for IoMT healthcare data management.
FIGURE 5. Real-Time PPG visualization.
FIGURE 6. Blockchain’s architecture diagram.
1) NETWORK ARCHITECTURE
The blockchain network is structured as a three-node
architecture, where each node maintains a copy of the
distributed ledger. Figure 6 shows the architecture diagram of
the proposed blockchain network. This architecture provides:
• Fault tolerance: The system maintains operational
integrity even if one node fails, ensuring continuous data
availability.
• High throughput: The system efficiently processes multiple transactions concurrently, meeting the
real-time requirements of IoMT data streams.
2) DATA FLOW AND CHAIN CODE INTEGRATION
To ensure secure and validated data storage on the blockchain,
our implementation utilizes Hyperledger Fabric chaincode
(smart contracts) engineered for critical functionalities. Foremost is rigorous Data Validation: confirming the consistency,
format, and integrity of incoming healthcare data transmitted
via API requests from our Express.js server. Prior to ledger
persistence, the system mandates strict Access Control
through a token-based authorization system, employing
AuthTokens. Participation necessitates organizational registration within the Hyperledger Fabric network, a process
involving provision of essential organizational details and
establishment of secure credentials for AuthToken acquisition. Subsequently, all API data submission requests must
incorporate this AuthToken, which is validated by the chaincode for authorization. Upon successful authorization and
validation, the healthcare data is processed by the chaincode
and immutably recorded on the permissioned Hyperledger
Fabric blockchain. This architecture guarantees controlled
access, data privacy, and tamper-proof data storage, alongside
FIGURE 7. Off-chain and on-chain data storage in blockchain.
inherent blockchain benefits such as decentralization and
enhanced traceability, crucial for healthcare applications.
3) DATA STORAGE ARCHITECTURE IN HYPERLEDGER
FABRIC NETWORK
Our proposed system follows the hybrid data storage
architecture for IoMT device-generated data. Biosignals
from the pulse oximeter are divided into strategic off-chain
and on-chain storage. To this effect, the various off-chain
data components include PR, SpO2, and edge-node identity
coupled with transaction hash values. At the same time, the
blockchain network holds only the transaction metadata in
the form of timestamps and corresponding transaction hashes.
This Architecture allows for the assurance of data privacy and
efficiency of the system by embedding secure links between
off-chain medical data and on-chain transaction records,
as shown in Figure 7.
4) SECURITY AND PRIVACY CONSIDERATIONS
A multi-layered approach to data protection ensures that
security and privacy considerations are deeply ingrained
in the system’s architecture. The system uses distinct
channels for various healthcare data to provide strong data
isolation and access control. While the Membership Service
Provider (MSP) precisely controls identification and access,
a thorough encryption framework guards data in transit and
at rest.
Security Infrastructure and TLS implementation: The network security is reinforced through a robust TLS (Transport
Layer Security) implementation
1) Certificate Authority (C.A.) configuration:
• Deployment of a dedicated Fabric CA for managing TLS certificates.
• Implementation of separate root C.A.s for each
organization.
• Generation and management of TLS certificates
for all network components.
2) TLS Certificate Management
• Issuance of unique TLS certificates for each
network node.
• Implementation of certificate rotation policies.
• Maintenance of Certificate Revocation Lists
(CRLs).
FIGURE 8. IoMT device authorization in blockchain.
This algorithm formalizes the registration of IoMT devices
onto a blockchain, generates secure device credentials,
and establishes access policies to ensure controlled and
authorized data sharing across the network.
5) ENHANCED SECURITY AND ACCESS CONTROL
MECHANISMS IN IoMT DATA HANDLING
Hyperledger Fabric ensures data integrity, secure access, and
streamlined management of IoMT data and metadata by
recording essential metadata on the blockchain. This design
guarantees that the data from IoMT devices is immutable,
securely managed, and accessible only by authorized entities. Through smart contracts, access policies are defined,
enforced, and updated on the blockchain, which enables
secure, decentralized control of medical data and supports the
integrity of the IoMT data lifecycle.
Figure 8 illustrates the process of IoMT device authorization in the blockchain network. These devices collect medical
data and then transmit this data to the network for secure
storage and access management. We will now discuss how
these devices are registered and accessed in the blockchain.
6) SYSTEM PHASES AND FUNCTIONS
The following stages outline the system’s blockchain workflow, encompassing setup: registration, data encryption,
storage, and access to the data.
7) SYSTEM INITIALIZATION
To provide safe and automated interactions with IoMT
data, this phase deploys smart contracts, or chaincode, and
initializes the Fabric blockchain network.
Algorithm 1 Registration and Access Policy Definition
Phase 1: Registration
Procedure RegisterDevice(deviceID, FabricCA)
Step 1: Blockchain Registration
CALL FabricCA.register(deviceID)
ASSIGN (Certu, pku,sku) = FabricCA.issueCertificate(deviceID)
Step 2: Store registration info
CALL Blockchain.storeRegistration(deviceID, Certu, pku,sku)
Return (Certu, pku,sku)
End Procedure
Phase 2: Access Policy Definition
Procedure DefineAccessPolicy(dataOwnerID, targetIDs,
dataCategories, validityPeriod)
Step 1: Policy Creation
POLICY = {"targetIDs" : targetIDs, "dataCategories" :
dataCategories, "validityPeriod" : validityPeriod}
Step 2: Policy Signing
policySignature = Sign(POLICY ,sku)
Step 3: Policy Upload
CALL Blockchain.storePolicy(dataOwnerID, POLICY , policySignature)
Return Policy uploaded successfullÿ ¨
End Procedure
Procedure Main()
deviceCredentials = CALL RegisterDevice(deviceID, FabricCA)
CALL DefineAccessPolicy(dataOwnerID, targetIDs, dataCategories,
validityPeriod)
PRINT Registration complete ¨ d.¨
End Procedure
END
8) REGISTRATION
This phase includes dual registration within the Fabric
network and the secure enclave, enabling identity-based
access control for the edge node and IoMT device.
• Blockchain Registration: Each device registers with
the Fabric CA using its unique device I.D., obtaining a
digital certificate and an associated public-private key
pair.
Blockchain(UserID) → (Certu, pku,sku)
Upon registering on the Fabric network, an IoMT device
obtains a digital certificate and public key (pku) from the C.A.
using its distinct user I.D.
9) ACCESS POLICY DEFINITION
Policies are created to control data access rights, guaranteeing
that only individuals with permissions can access particular
data.
• Policy Creation: The IoMT data owner creates access
policies outlining target I.D.s, data categories, and
validity periods.
• Policy Signing: A digital signature σ is created when
the device uses its private key (sku) to sign the policy.
This signature guarantees the authenticity and integrity
of the policy.
• Policy Upload: To provide transparent policy management, the signed policy and its accompanying information are stored on the blockchain as a management
record.
The proposed system meets the essential needs for privacy,
data integrity, and scalability in healthcare data management
FIGURE 9. Blockchain transaction flow.
by integrating IoT data collection, real-time visualization, and
secure blockchain storage. This comprehensive Framework
ensures the safe and efficient handling of sensitive medical
information.
The sequence diagram in Figure 9 represents our
blockchain network’s end-to-end transaction life cycle,
showing interactions between certificate authority, peer
Node, Orderer, Ledger, and chaincode components. The flow
progresses through several important phases, from initial
setup-issuance of certificates to processing, ordering, and
validation of the transaction, up to a final commitment to the
ledger. Key elements include:
• Security management through TLS certificates and
transaction validation.
• Consensus-driven ordering process to develop and
validate blocks.
• State management that allows for consistent updates in
the distributed ledger.
By ensuring that each peer in the network receives
transactions in the same order, this mechanism produces
consistent updates to the state of every ledger throughout the
network.
VI. PERFORMANCE EVALUATION
To rigorously evaluate the performance and scalability of
our proposed framework, we employed a comprehensive
set of performance metrics. These metrics were carefully
chosen to assess key aspects of the system’s behavior under
load and to address the requirements of healthcare data
management. Specifically, we utilized the following metrics
for performance evaluation:
• Blockchain Network Stability and Consensus Metrics: Including Blockchain Height, Block Synchronization Rate, and Consensus Deviation to assess the
reliability of the underlying blockchain infrastructure
under load.
• Processing Latency Distribution: Measured via Mean
Processing Time, Standard Deviation, and Percentile
Distribution to quantify the system’s responsiveness in
data processing.
• Network Throughput Metrics: Evaluated using Server
Stream Request Rates (Peak and Sustained) and Transaction Success Rate to determine the system’s data
handling capacity.
• End-to-End Latency Metrics: Decomposed into
Network Latency, Processing Latency, and Commit
FIGURE 10. Blockchain height.
Latency, along with P90, P95, and P99 Latency
percentiles, to assess overall system responsiveness and
identify latency contributors.
In the subsections that follow, a comprehensive analysis
of the findings for these metrics can be seen.
A. BLOCKCHAIN NETWORK STABILITY AND CONSENSUS
ANALYSIS
To assess the fundamental stability and reliability of the
underlying Hyperledger Fabric blockchain network, which
is crucial for consistent system operation, we analyzed
blockchain height and consensus metrics. Statistical observations from the Figure 10. Blockchain height graph:
• Consistent block height: 18 blocks
• Observation period: 23:17:00 to 23:19:45
• Block synchronization rate: 100%
• Consensus deviation: 0%
These metrics indicate a highly stable and robust
blockchain infrastructure, providing a reliable foundation for
our healthcare data management framework. The consistently
maintained block height, high block synchronization rate,
and low consensus deviation observed over the testing
period strongly suggest the network’s capability to maintain
consensus effectively as the network scales.
B. PROCESSING LATENCY DISTRIBUTION
To quantify the processing speed and identify potential
bottlenecks in the data pipeline, we measured the distribution
of processing times for individual data transactions. Block
processing latency follows a multi-modal distribution across
different percentile buckets:
P(t) =



P1 if t ≤ 5 ms
P2 if 5 ms < t ≤ 10 ms
P3 if 10 ms < t ≤ 15 ms
P4 if 15 ms < t ≤ 50 ms
1 − (P1 + P2 + P3 + P4) if t > 50 ms
(10)
Measured metrics from the graph Figure 11. Processing
Time Distribution:
Measured metrics from the graph:
• Mean processing time (µ): 12 ms
FIGURE 11. Processing time distribution.
FIGURE 12. Network throughput.
• Standard deviation (σ): 3.2 ms
• Processing time distribution: approximately log-normal
The measured mean processing time of 12ms, coupled with
a low standard deviation of 3.2ms and a predominantly
log-normal distribution concentrated below 15ms, demonstrates efficient and predictable processing of individual
healthcare data points within our system. This rapid processing is essential for timely data availability and responsiveness
in healthcare applications.
C. NETWORK THROUGHPUT ANALYSIS
To evaluate the system’s capacity to handle a significant
volume of data requests, we conducted a network throughput
analysis, measuring the server stream request rate and
transaction success rate. Server stream metrics indicate the
following from graph Figure 12. Network Throughput:
• λpeak = 72 requests/interval
• λsustained = 60 requests/interval
Transaction success distribution from the graph 12:
• Successful transactions: 95% ± 2%
• Canceled requests: 5% ± 1%
These throughput metrics demonstrate the system’s capacity to handle a peak request rate of 72 requests per interval
and a sustained rate of 60 requests per interval, with a high
transaction success rate of 95%. This indicates the system’s
potential to effectively handle data streams from multiple
devices or users concurrently, suggesting good scalability for
real-world healthcare deployments.
D. LATENCY ANALYSIS
To comprehensively evaluate the responsiveness of the
system from data acquisition to blockchain commit,
we performed an end-to-end latency analysis, decomposing
the total latency and examining its distribution. Based
on the combined analysis of processing time metrics
shown in Fig 10, 11 and 12: The end-to-end latency
decomposition:
Ltotal = LNetwork + Lprocessing + Lcommit (11)
where:
• Lnetwork = 0.005 s (±0.001 s)
• Lprocessing = 0.035 s (±0.003 s)
• Lcommit = 0.18 s (±0.012 s)
E. LATENCY DISTRIBUTION ANALYSIS
Derived from the block processing time buckets in Figure 11:
• P90 = 0.012 s
• P95 = 0.038 s
• P99 = 0.185 s
• Latency distribution follows a heavy-tailed distribution.
The latency distribution analysis, particularly the P90, P95,
and P99 percentile values, further characterizes the variability
in end-to-end latency. The heavy-tailed distribution and
higher percentile values (P95, P99) suggest occasional
latency spikes, which are important to consider for real-time
healthcare applications. This distribution implies that while
the system generally exhibits low latency, there can be
occasional delays.
F. PERFORMANCE IMPLICATIONS
• Network Propagation: Efficient with minimal latency
(≈ 5ms)
• Processing Overhead: Moderate and generally stable,
maintaining consistent performance metrics across periods
• Commit Phase: Dominates the total latency, accounting
for approximately 80% of the end-to-end processing
time
• Block Height Consistency: System shows good consistency across peers, with minimal divergence (1h ≤ 1)
• Optimization Potential: Opportunities exist in the
commit phase, particularly in consensus mechanism
efficiency
These results present a complete quantitative view of
network performance characteristics and exhibit the strength
of the system’s capability and operational efficiencies. The
network’s consistency and block propagation mechanisms are
strong, and processing overhead is well-managed. However,
the analysis also highlights that the blockchain commit phase
is the dominant contributor to end-to-end latency. Future
optimization efforts should therefore focus on enhancing
the efficiency of the blockchain consensus mechanism and
commit process to reduce overall latency and improve the
system’s suitability for highly time-sensitive healthcare applications. Overall, the system’s general architecture has proved
reliable and scalable in handling distributed healthcare
data.
G. POTENTIAL DEPLOYMENT CHALLENGES AT SCALE
While our framework demonstrates promising performance,
large-scale real-world deployment presents key challenges,
primarily in computational overhead, legacy system integration, and cost.
• Computational Overhead: Scaling IoMT devices
increases computational demands, especially blockchain
commit latency. Higher data streams may strain
servers and blockchain processing. Mitigation includes
chaincode optimization, server load balancing, and
Hyperledger Fabric tuning. Large-scale benchmarking
is needed to quantify overheads.
• Integration with Legacy Systems: Integrating with
hospital EHRs and legacy systems is complex due to data
format and interoperability issues. Custom APIs and
data transformation may be required. Phased integration,
starting with key use cases, is advisable.
• Cost Implications: Large-scale deployment incurs
substantial costs across infrastructure (servers, network,
storage), blockchain operation, ioMT devices, system
maintenance, and regulatory compliance. Cost optimization strategies should be explored, including cloud
infrastructure, efficient resource use, and cost-effective
blockchain configurations. A thorough cost-benefit
analysis is crucial for assessing economic viability
VII. CONCLUSION AND FUTURE WORK
This research presents an integrated framework effectively
merging blockchain and IoMT to enhance conventional
healthcare monitoring. The architecture establishes a secure,
decentralized healthcare data ecosystem via edge computing
nodes and a Hyperledger Fabric blockchain. Middleware
and edge computing optimize resource use and secure
IoMT-blockchain communication, ensuring data integrity and
effective remote monitoring. Crucially, our framework significantly improves key healthcare workflows, particularly data
sharing between hospitals and real-time patient monitoring.
Blockchain-enabled data sharing streamlines interoperability
across hospitals, enhancing care coordination, public health
monitoring, and administrative efficiency. Furthermore,
improved real-time IoMT data monitoring enables faster
detection of critical events, proactive personalized care, better
chronic disease management, and reduced readmissions.
These workflow enhancements highlight the practical value
of our framework in healthcare. Future work will focus
on key advancements in digital healthcare: optimizing edge
data processing for reduced latency, enhancing consensus
mechanisms for higher throughput, and integrating advanced
privacy technologies. Further research should also rigorously
evaluate large-scale deployment performance and explore
integration with existing healthcare systems to maximize
real-world impact.
DECLARATIONS
Conflict of interest The authors declare that they have no
known competing financial interests or personal relationships
that could have appeared to influence the work reported in this
paper.
LIST OF ABBREVIATIONS
The following abbreviations are used in this manuscript:
Abbreviation Definition
STX Start of Text: 0 × 02 indicates the start of
the packet.
I.D. Identifier: The terminal I.D. for the
device.
CMD Command: Specifies the packet type or
command.
LEN Length: Indicates the length of the data
field.
DATA Data: Contains raw data such as SpO2,
Pulse Rate (PR), etc.
ETX End of Text: 0 × 03 indicates the end of
the packet.
CRC Cyclic Redundancy Check: CRC16
checksum computed from I.D. to end of
the data field.
EDGE ID Edge Node ID: The identifier for the edge
node in the network.
PPG Photoplethysmogram: Readings related
to blood flow and oxygen saturation.
SpO2 Peripheral Oxygen Saturation: A measure
of blood oxygen saturation.
P.R. Pulse Rate: The number of heartbeats per minute
ECG Electrocardiogram: Measures the electrical activity of the heart.
IoMT Internet of Medical Things: Network of
medical devices for data exchange.
EoT Edge of Things: Edge layer where data
from IoT devices is processed.
IoHT Internet of Healthcare Things: IoT specific to healthcare applications.
SSL Secure Sockets Layer: Protocol
for secure, encrypted server-client
connections.
TLS Transport Layer Security: A protocol for
secure communication, succeeding SSL.
