Title: Blockchain Technology for Global Supply Chain Management: A Survey of Applications, Challenges, Opportunities and Implications

ABSTRACT Supply chain management depends on a complex, interconnected network of suppliers,
manufacturers, transportation companies, distributors and customers with the goal of predicting, monitoring
and controlling operations and processes. Globalization has introduced fierce competition, forcing supply
chains to innovate and enhance their performance and capabilities. Centralized management systems are
prone to attacks, disruptions and malfunctions. A potential solution to these known issues is the adoption of
blockchain technology. The blockchain offers an immutable ledger that allows for a trustless, decentralized
system without reliance on third parties. It can provide new features, improve performance, advance network
visibility and strengthen the four flows of a supply chain. To survive and compete on the global stage, supply
chains must adopt emergent technologies to develop new business strategies. In this paper, a comprehensive
survey of academic literature and research works relating to blockchain platforms for global supply chain
management is presented. This survey will provide an overview of blockchain technology for supply
chain management, summarize industry applications, highlight persistent challenges, and identify research
opportunities to enhance the current state of research in the past six years. The contribution of this survey is
to also provide a list of available blockchain solutions for global supply chain management and to elaborate
on future advancements in the field. New solutions will be proposed and explained.
INDEX TERMS Blockchain, blockchain applications, blockchain technology, global supply chain management, literature review, supply chain management, survey.
I. INTRODUCTION
Supply chain (SC) management is defined as a proactive measure of four flows: materials flow, process flow, case flow and
information flow. Logistics form the backbone of the SC and
are responsible for planning, implementing and controlling
the flow and storage of goods, services and information [1].
Today’s globalized markets have created tighter competition due to the elimination of international boundaries [2].
To survive and maintain sustainability, it is necessary for
organizations to identify and develop new business strategies
based on the adoption of emerging digital technologies [3].
Global supply chains need to find new ways to design their
supply chains to take advantage of opportunities that offer
more flexibility [4]. Systematic smart implementations must
be made to remain competitive. Today’s SC applications follow the Industry 4.0 concept to expand internal processes and
to promote the digitalization of products and processes [5].
Blockchain technology (BCT) has seen a proliferation
in current literature as it transforms business processes
by building trust without an intermediary, providing stakeholders with enhanced visibility, applying smart contracts
to oversee applications, introducing disintermediation and
simplifying digitalization and optimization of supply chain
operations [6]. Blockchain technology has expanded to
include cryptocurrency, healthcare, advertising, insurance,
copyright protection and energy [7]. Most industries today
have a supply chain with facilities distributed across the
globe. Despite technological advancements and recent developments, globalized SCs have seen a plethora of challenges
before, during or after blockchain adoption. These categories
are laws & regulations, data management & provenance,
governance & traceability, interoperability & standardization,
lack of awareness, education & innovation, performance &
scalability, trust & stakeholder management and transparency
& visibility.
This survey will present a deep dive into the available
literature spanning from 2018 to 2023. The purpose is to
provide a detailed overview of blockchain applications, adoptions and implementations in global SCs. A strong emphasis
was placed on the current challenges and research gaps that
hinder BC progression. Solutions were organized into tables
that are meant to provide a roadmap for future researchers.
The survey is a one-stop shop for all current industrial
researchers to pick and choose which parts may be necessary
for their own research, while adding to the literature regarding blockchain solutions for supply chain management. This
paper also serves as a basis to create a conceptual framework
that will be used in a future implementation. The survey
is split into sub-categories and these sections follow this
structure. Section I introduces blockchain technology. Next,
Section II lists applications by industry. Section III presents
the challenges and open issues that exist in today’s global
market. It also contains any notable gaps in research and
opportunities to correct them. Blockchain solutions will be
briefly proposed in Section IV. Lastly, Section V summarizes
the research implications of successful implementations and
proposes future work.
II. BLOCKCHAIN TECHNOLOGY
Blockchain is a digital ledger technology (DLT) that provides
a tamper-proof ledger that utilizes cryptographic mechanisms
to improve resiliency without the use of a central authority.
These ledgers contain cryptographically signed transactions
that are organized into blocks that are chained to one another
with their own unique hash. Modification becomes more difficult for older units as newer chains are added and resistance
is increased [8]. The blockchain uses two kinds of encryption:
asymmetric and symmetric. Asymmetric uses public or private keys, while symmetric uses a one-time generated code
for decoding and encoding. Blockchains have three different
types of nodes: simple, full and mining. Simple nodes send
and receive transactions. Full nodes store copies on the ledger
process of generating a new block [9]. A node initiates a
transaction by employing a digital signature using private
key cryptography. A single transaction represents a transfer
of digital assets which include the timestamp, block ID and
address. Once transactions are verified and confirmed by
miners, they are included in the block. Each miner competes
against each other to solve a computational problem. Incentives are given to the miner and network peers to verify the
new block using consensus mechanisms [10].
Once on the block, the transactional data is safely stored
and easily retrieved for future examination. The immutable
ledger eliminates the need for a trust authority, as trust is
created through the blockchain’s architecture. The key characteristics of blockchain architecture are decentralization,
immutability, transparency, traceability, trustless, persistency,
anonymity, auditability, automatic contract execution, validity and tamper-resistance.
• Decentralization: Blockchain transactions do not
require the assistance of a trusted central agency for
transaction verification [10]. Consensus mechanisms
ensure transactions are processed and validated by the
nodes. Each node is equivalent and stores the data on
the digital ledger.
• Immutability: Blockchain transactions are verified and
stored in the ledger. It provides a record of all previous transactions on the chain, increasing visibility and
auditability.
• Transparency: Once majority of nodes reach consensus, transactions are stored, and the ledger is updated.
Any changes to the network are publicly visible ensuring
transparency [9].
• Traceability: Records are permanently stored on the
blockchain along with transaction information [11].
Each update can be traced back to its origin, resulting
in a more efficient and transparent network [9].
• Trustless: Blockchain provides transactions between
unfamiliar parties who don’t trust one another. Consensus mechanisms ensure the validity of transactions through the distribution and updating of the
ledger [9].
• Persistency: Blockchain’s infrastructure ensures network data is authentic and not modified [10]. Transactions recorded on the ledger are considered persistent
as they spread across the network, where each node
maintains and controls its records [12].
• Anonymity: Each actor on the network can be
assigned a virtual identity [13]. No outside agency is
responsible for monitoring sensitive data. A certain
amount of anonymity is provided through the trustless
environment [10].
• Auditability: All recorded transactions are timestamped
and stored on the immutable ledger which can be traced
at any time due to the fact the information is considered
persistent. The degree of auditability depends on the
type of blockchain [12]. Public has the highest, while
private has the lowest.
• Automatic Contract Execution: Smart contracts can
be programmed to start when a certain number of
conditions are met. The blockchain will automatically
determine when these conditions occur and enforce the
terms of the contract [14].
• Validity: Broadcasted transactions are validated by
nodes and do not require executions from each. Falsification or inconsistencies can be easily detected [12].
• Tamper-resistance: Transactions are considered
tamper-proof during and after the block generation process [13]. Since all blocks are linked to the previous in
a chain, alteration would change too many parameters
which would be easily detectable.
There are three types of blockchain; permissioned, permissionless and consortium/federated. In a permissionless
(public) blockchain, anyone can run a node, participate
in mining, access a wallet and write transactions. Public
blockchain is the most common digital currency application [15]. A permissioned (private) blockchain is a closed
platform where only certain actors are granted permission to
perform specific tasks. These systems are often owned by
a corporation or person [15]. In a consortium or federated
blockchain, power is divided between a group of people or a
person who forms groups called federated or consortium [15].
Blockchain technology uses consensus models to enable
a group of mutually distrusting users to work together [8].
When a new user joins, they must agree to a predetermined
set of principles. Consensus models remove the need for a
trusted outside agency to maintain the system, as anyone
can verify the blockchain’s integrity by verifying each block
independently.
Forks make changes to permissionless blockchain data or
protocols. Forks are divided into two categories, soft and hard
forks. A soft fork is a change to a blockchain implementation that is backwards compatible, while a hard fork is not
backwards compatible [8]. In soft forks, upgraded nodes can
communicate with those non-updated nodes. In hard forks,
there is no communication, nodes will be severely impacted,
and a diversion will occur from the existing technology [16].
Smart contracts are implemented on top of the blockchain,
where contracts are deployed through cryptographically
signed transactions. Hence, smart contracts are self-enforcing
and autonomous executable programs that enforce the terms
and conditions of an agreement or contract using code
and computational infrastructure. The key features of smart
contracts are decentralization, immutability, transparency,
accuracy and availability [17]. Smart contracts extend and
leverage blockchain technology, as they are tamper resistant
and can be used without a trusted third party [8].
Smart contracts ensure appropriate access control and
contract enforcement. The life cycle of smart contracts
follows four steps: creation, deployment, execution and
completion. During deployment, execution and completion,
a sequence of transactions will be executed and stored on the
blockchain [18].
III. GLOBAL SUPPLY CHAIN MANAGEMENT
Global supply chain and logistics management have been
focused on the performance of business operations. They
focus on similar concepts but are two separate ideas. Logistics focused on the work required to enhance inventory
management, while SCM focuses on integration of activities
to increase the operating efficiency [1].
The growth of international business has led to enhanced
supply chains, capable of using sustainable SC practices.
Large supply chain networks today are efficient operations
and able to standardize their processes. They are able use current developments to their advantages and use new forms of
technology as new options appear as technology evolves [2].
Globalization had to led to a rise in having a distributed
SC that has facilities and suppliers from across the world.
Offshore suppliers have lowered the overall price suppliers
can offer their products. Corporations can keep their prices
high while always looking to gain competent, low-wage
workers [3].
Operations Management (OM) research and applications
have given researchers the ability to formulate new models satisfying supply chain strategies and allowing SCs to
adapt to change or the introduction of new government policy. Strategies allow for a global division of an SC to plan
accordingly by considering goals, flows, capacities and capabilities[4]. OM has evolved strategies into what supply chains
are known for, well-oiled machines that are more than capable
of handling global demand.
The digital age has taken previous advancements and transformed them into what we call today as smart production.
Smart systems have the necessary personnel and processes to
comply with demand and remain ahead of the competition.
To succeed, they must maintain the four attributes: production
connectivity, performance visualization, process optimization and system autonomy [5]. A current supply chain is a
complex network that generates, monitors and controls the
four flows. It is the complete pathway of a product from raw
material to a consumer good on the marketplace. The goal
is to consistently compete against other global SCs, lower
expenses and augment daily operations to produce goods
quicker & cheaper [19].
A supply chain is a system of people, events, data,
resources and departments with the sole objective of moving products to generate capital. Supply Chain Management
(SCM), in a global sense, is complete real-time monitoring
of every division’s operation within the SC, no matter where
they may be in the world [20].
IV. RELATED LITERATURE
Blockchain technology for supply chain management
research is in its infancy. Consequently, there is a lack of
peer-reviewed sources and most focus on conceptual rather
than practical implementation. Each source will be summarized along with their key contributions to this field of
research in Table 2.
Chang and Chen [21] provided an overview of the use of
blockchain and smart contracts in the field of supply chain
management (SCM). The purpose of their research was to
bridge the gap between the existing knowledge regarding
blockchain applications and future work.
TABLE 1. Acronyms.
The work Dutta et al. [22] focused on blockchain technology for supply chain operations. The blockchain can be
applied to major SC functions such as provenance, resilience,
SC reengineering, security enhancement, business process
management and product management. Kawaguchi [20]
emphasized that blockchain technology needs to be studied more extensively and listed the top adoption challenges:
organizational requirements, company readiness, data collection & management, interoperability, transition & integration
costs, security, privacy and legal concerns.
Gonczol et al. [23] sorted the existing literature into three
large groups; theoretical analyses, conceptual systems, and
implemented systems. They concluded there was a lack of
technical papers due to limited knowledge and not enough
interest from sectors outside of business and finance. Their
work sorted challenges into two types: technical limitations
and digitalization issues.
Wan et al. [24] identified industries in which BCT can
have a significant impact on information sharing, investigated current challenges or deployment barriers and classified
the future development of information sharing using BCT
within a SC. Their work focused on understanding the nature
of the supply chain as a part of the future development
of blockchain and emphasized the need for more research
regarding blockchain-based information sharing in SCs.
Pournader et al. [25] investigated blockchain applications across supply chains, transportation and logistics. Four
clusters were included to provide a picture of each sector: technology, trust, trade & traceability/transparency. The
authors distinguished the lack of combination technology
available despite the increased interest from literature.
Lim et al. [26] gave a comprehensive analysis of
blockchain technology applications in SCs. Their work
encompassed agriculture, forestry, fishing, manufacturing,
construction, and mining industries. Four research gaps hinder the combination of blockchain and supply chains were
mentioned: ignored themes in supply chains, applied methodologies in research, academic theory and practice in different
industrial sectors.
Shakhbulatov et al. [27] reviewed six challenges hindering
supply chain management and linked their solutions with
blockchain frameworks in the available literature. These challenges were provenance, performance improvement, quality
assurance, quality control, sustainability transparency, data
privacy and confidentiality. Their work identified new opportunities and challenges of blockchain for supply chain
management highlighting the need for new solutions.
Paliwal et al. [28] investigated the role of blockchain technology in sustainable supply chain management using the
What, Who, Where, When, How and Why (5W+1H) pattern.
Their research indicated there is a strong trend in awareness for blockchain technology due to increased academic
attention.
Juma et al. [29] provided a detailed overview of blockchain
technology in international trade supply chains. They discussed the practicality of using blockchain technology from
a customs perspective.
The following survey is a comprehensive compilation of
literature reviews published in the last six years that provides
a detailed map of today’s global landscape. It differentiates
itself by organizing challenges, opportunities and solutions
that could be potentially enhanced using blockchain technology as a tool. Table 2 categorizes each literature review
or survey by their key contributions to the advancement of
blockchain technology for global supply chain management.
V. MATERIALS & METHODS
The purpose of this survey is to assimilate current literature
centered around blockchain technology for global supply
chain management. The survey aims to provide answers to
the following research questions:
RQ1: What challenges & vulnerabilities in global supply
chain management need to be addressed?
RQ2: What gaps in research exist?
RQ3: What opportunities exist for future research based on
the current gaps in research?
RQ4:What successful solutions can be built upon to
advance blockchain implementations for global supply chain
management?
To better understand the current state of research and
future research opportunities, a survey paper was employed
with a three-step methodology to gather relevant cited
works that directly relate to the research questions. The
TABLE 2. Related literature.
last six years were selected, 2018 through 2023, to focus
on current advancements. IEEE Xplore & Google Scholar
were utilized to promote robust research, capable of reproduction & repeatability. The three steps are as follows;
selection criteria, source evaluation and full text read
& interpretation.
A. STEP 1: SELECTION CRITERIA
Journal selection criteria used a group of keywords relating
to blockchain models, applications & challenges for global
supply chain management (SCM). The goal was to include
meaningful sources while excluding ambiguous references.
Academic journals and conference articles are compared to
inclusion/exclusion parameters. If one exclusion condition
existed, the journal was removed. Strings were used to narrow sources based on keywords or phrases. The full list of
selection criteria can be found in Table 3.
String 1 (‘‘blockchain’’ OR ‘‘industry’’ OR ‘‘applications’’ OR ‘‘logistics’’ OR ‘‘manufacturing’’ OR ‘‘supply
chain management’’)
TABLE 3. Selection criteria.
String 2 (‘‘global’’ or ‘‘supply chain’’ OR ‘‘blockchain’’
OR ‘‘challenges’’ OR ‘‘research gaps’’ OR ‘‘opportunities’’)
B. STEP 2: JOURNAL EVALUATION
Sources that passed inclusion criteria and contained no exclusion criteria were gathered into a database for review. During
the journal evaluation phase, each paper’s abstract, discussion
and conclusion were assessed for compatibility. Unreliable
sources were removed to prevent scope creep and encourage
a cohesive body of work.
C. STEP 3: FULL LITERATURE READING &
INTERPRETATION
Each source was thoroughly reviewed, findings were generalized and results analyzed. Research questions were aligned
to each selected journal’s contents. Sources were then categorized and labelled for future examination. Selected journals
were grouped by section or keyword and inserted into the
literature review. Figure 1 summarizes the outcome of the
selection criteria.
FIGURE 1. Outcome of selection criteria.
VI. RESULTS
Figure 2 displays the distribution of total number of sources
per each section of the survey. It is meant to show how many
journals went into each part of this research paper. Figure 3
shows publication by year. Figure 4 references publication by
type of research. Figure 5 sorts publications by application
industry. Figure 6 splits publications by challenge with their
corresponding opportunities while Figure 7 focuses on the
solutions derived from said challenges and opportunities.
Table 3 groups blockchain applications by industry. Table 4
organizes sources by their challenges and opportunities for
future research. They are meant to show the overall distribution of sources and which sections were given the most
attention. Blockchain models, applications and challenges
received the most sources to highlight the current state of
blockchain in the supply chain management field in the past
six years.
TABLE 4. Blockchain applications by industry.
TABLE 5. Blockchain challenges & solutions.
VII. DISCUSSION
A. INDUSTRY APPLICATIONS
Today’s blockchain systems can be tailored to fit a specific
sector using a combination of available options such as type
of BCT, consensus algorithm and what characteristics a company hopes to gain. Blockchain applications will be presented
for different sectors with emphasis on global supply chain
management, logistics and transportation. A minimum of ten
FIGURE 2. Publication distribution by survey section.
sources were applied to each section to provide a current view
of the global landscape.
1) AGRICULTURE & FOOD
The agriculture and food industry has evolved from traditional processes to precision-based systems. Smart agriculture dominates the industry making it possible for blockchain
to be used as a tool for promising solutions, but network performance problems need to be addressed prior to
adoption. Latency, bandwidth, physical storage limit, power
consumption, and communication speed between devices
play a critical role in the development of new BCT solutions.
Blockchain, used in combination with IoT devices, can maintain a secure, transparent, and tamperproof system [30]. BCT
can be used to solve technical problems and optimize communication and SC processes. Currently, BCT solutions exist
for agricultural insurance, smart farming, traceability, land
registration, food supply chain governance, farm security and
agriculture product e-commerce safety [31]. Ferrag et al. [32]
focused on green, sustainable practices for IoT devices, developing them into smart systems capable of making decisions
on the fly with RT data. This was accomplished by separating
the network into layers with each layer serving a specific purpose such as the quick transport of data and the coordination
FIGURE 3. Publication by year.
FIGURE 4. Publication by type.
of electronic devices across the entire SC. Demestichas et al.
[33] provided a detailed overview of traceability applications
FIGURE 5. Publication by application industry.
FIGURE 6. Publication by challenge & opportunity.
in the agri-food industry. Traceability can provide agriculture
SCs with higher levels of visibility, real-time location and
inventory data and product provenance [34].
FIGURE 7. Solutions by challenge category.
Lin et al. [35] defined smart agriculture by expanding on
the work of Demestichas et al. [33] and Tripoli and Schmidhuber [34]. Smart agriculture is defined as the application
of technologies such as IoT, Big Data, Global Positioning
Systems (GPS), Cloud Computing, and Artificial Intelligence
(AI) into a smart system that can predict outcomes, make
intelligent decisions, and amalgamate numerous technologies
into a single, unified platform [35].
Zhao et al. [36] focused on creating solutions to worldwide
challenges from a holistic perspective. The agriculture and
food sector’s primary objectives are the circulation of products from creation to consumption. The work emphasized the
need for agri-food value chain management that adopts new
technologies to streamline operations and overcome barriers.
Feng et al. [37] stressed the importance of sustainable standards & practices that can operate throughout
the agri-production process. Real time data must be available twenty-four seven to make informed decisions through
human interaction and automation, which can be addressed
through traceability in blockchain applications.
Khan et al. [38] linked IoT and BCT to ensure product
provenance which is critical when dealing with perishable
food. A BCT-IoT platform can enhance provenance, payment
methods and management practices. The goal of IoT applications in the agri-food industry is incorporation of automation
and intelligence into a smart system. Kim and Laskowski [39]
classified the major agriculture applications into three categories: food safety, sustainable agriculture practices to foster
relationships with co-op farmers and agriculture finance.
Food safety is a combination of provenance and tracing.
Sustainability leaves a smaller carbon footprint and supports
local co-ops by contributing to smaller farms. FarmShare is
an Ethereum-based platform that provides a communication
platform for farmers and consumers. Tokens are exchanged
between parties when a transaction is finished and posted on
the network. In finance, smart contracts can be employed to
keep contractual agreements between parties through automated actions.
An example of a use case in the agri-food industry is worldwide fishing (WWF) seafood traceability. The BC-based
system regulates rules and regulations regarding fishing and
ecosystem conservation. Items are scanned and important
data attributes are stored with their respective ID tags, which
prevents the purchase of illegally caught seafood. A second
use case is the Walmart & IBM food safety solution that
utilizes BCT to upload SC information and retail data. The
tracing of food helps detect contaminated food and prevent E.
coli outbreaks, as well as providing data for risk prevention
and management [40].
Uddin et al. [19] presented a model for blockchain in the
food supply chain. The proposal helps managers determine if
BCT is appropriate (or not) for their business. It works for SC
networks of all sizes and has a solid framework.
2) HEALTHCARE & MEDICINE
The healthcare (HC) industry has a need for blockchain
technology. Electronic health records (EHRs), data management, access control, auditing, medical billing and
anti-counterfeiting are applications in industry. All sensitive
data must be secured and consolidated to promote interoperability between different systems [41].
Farouk et al. [42] focused on three major applications in
healthcare and pharmaceuticals: intelligent healthcare systems for patients, enhancing the protection of patients’ personal data and strengthening drug credibility in the pharma
industry. The blockchain improves security, management and
the analysis of big data.
Dimitrov [43] examined big data management, the evolution of records and pharma research and development.
BCT is responsible for maintaining all three types of patient
data records: electronic medical records (EMR), electronic
health records (EHR) and personal health records (PHR).
The Ethereum framework was implemented for management
and access control through virtual private networks (VPNs)
since blockchains can easily manage and abide by environmental protections & regulations. Decentralized applications
(dApps) allow doctors to conduct telemedicine with low fees
and IoT sensors can ensure patient data is up to date to ensure
an accurate history of health.
Konstantinidis et al. [44] discussed effective Blockchain
applications in HC. High data volumes and throughput transaction processing are two benefits of a decentralized system.
Current efforts focus on patient data management and record
keeping. Doctors and healthcare providers have access to
patient information, stored on a distributed ledger, for monitoring and alerts.
Zhao et al. [45] emphasized the importance of blockchain
applications in the healthcare industry to create a smart
healthcare system. A patient can maintain their personal
records, while the blockchain can store, monitor, and distribute sensitive information via wireless sensors. The result
is a comprehensive, personalized summary of a single
patient’s health records that are available to any medical
center, physician’s office or hospital with patient permission
to protect privacy [45].
Leeming et al. [46] introduced numerous early-stage solutions to audit private data and to give patients the power
to manage consent of their private information. A linkage
between records, insurances and medical centers will streamline consumer applications and create a data repository.
A patient’s record will form the basis of the health plan while
smart contracts can be utilized to tweak meta-information.
Agbo et al. [47] summarized BCT applications in the
healthcare & pharmaceutical sectors. In pharma, fraud and
counterfeit detection are two pillars to maintaining and controlling drug authenticity. Applications to healthcare include
record management, insurance claim reporting, patientcentered health plans and uniformity among major medical
management software. The decentralized nature of BCT
allows for a distributed system without the need for an
authoritative.
Khatoon [48] stressed the use of BCT with smart contract applications in medical workflows and healthcare
management systems. Multi-organizational data exchanges
rely on easily accessible information that is interoperable
with research initiatives and physician requests. Ethereum
smart contract development & applications for healthcare
& medicine were discussed. Smart contracts conditions are
programmed and offer many options including stakeholder
access, data authorization & ownership, viewership permissions and actor credentials.
Siyal et al. [49] analyzed six applications of BCT for
HC: EHR, clinical research, medical fraud detection, neuroscience, pharmaceutical & research. The blockchain can
provide SCs with more functionality than legacy systems. It is
used for digitalization, highly sensitive information storage &
retrieval, record immutability, smart contract facilitation, data
accessibility, transparency, confidentiality, system integration, medical product validity and research and development.
Haq and Esuka [50] reviewed applications in the pharmaceutical industry. Application areas include drug discovery &
pharmaceutical research, SC & counterfeit drugs detection,
prescription management and billing claims management.
Telemedicine, with BCT, enforces trust between HC professionals & patients. Combined with AI, remote diagnostic
services use medical data derived from quantitative and qualitative statistical methods.
Uddin et al. [19] displayed another model for blockchain in
the vaccine supply chain, which combines machine learning,
IoT and BCT with SCM. This combination of technologies
gives customers increased security, opens up the SC to be
completely transparent and network maintenance.
3) LOGISTICS & CROSS-BORDER TRADE
The logistics and transportation industry is reliant on integration of activities across suppliers, distributors, wholesalers,
and retailers. Current literature shows that the logistics industry is employing BCT applications.
Al-Jaroodi and Mohamed [51] addressed blockchain applications for logistics management and synchronization of
multiple companies’ actions including planning, scheduling,
coordinating, monitoring and validating performed activities.
Logistics traceability gives stakeholders the ability to trace
goods with BCT adoption with consistent and reliable sets of
data. Vehicles can be optimized by providing the best route
and energy saving techniques. Collaborative logistics across
companies can reduce freight costs and maximize capacity
and utilization [52].
Dobrovnik et al. [53] presented the blockchain framework
with IoT and big data for logistics management. The key
applications are logistics traceability, vehicle routing, energy
saving management and collaborative logistics.
Blockchain technology applications for logistics provide a link between the physical & digital world, using
IoT for device integration [54]. BCT-IoT applications
include logistics management; food traceability, solving
logistics inefficiencies, product management and commercial
implementation [55].
In the transportation industry, BC can protect reputation when validating a message’s authenticity and or
protect expensive items from being stolen and duplicated.
Blockchain applications are mandatory for product traceability and the integration of SC processes transactions to create
dynamic business interactions [56].
Majeed et al. [40] introduced the Intelligent Transport System (ITS) for supply chains with transportation vehicles. This
smart platform combines automation, RT monitoring and
management systems to streamline operations and coordinate
SC activities.
Miglani et al. [57] focused on two separate use case studies:
logistics and transportation. The logistics study addressed the
success implementation of IoT and BCT integration, while
transportation looked at ride-sharing apps.
Blockchain can be a useful tool for cross border trade and
e-commerce. It provides a trustless platform which removes
the need for third party involvement. Majeed et al. [40]
proposed smart electronic commerce and the benefits of
adoption, such as proof of delivery for tangible assets, dispute
settlement and the removal of third parties for the authentication of transactions. Zhang et al. [58] provided a recap of
three distinct applications that are being utilized in finance
and economics: cryptocurrency, cross-border payments and
digital asset registries.
Chang et al. [59] posed international applications of BCT
via smart contracts in cross border trade. IBM, Maersk
& Hyundai Merchant Marine have designed and deployed
applications on the global stage. Two successful implementations of global applications of BCT for SCM include
IBM & Maersk’s TradeLens and the blockchain development
transaction system (BDTS) from CargoX [60]. Other examples are VGM portal, Agility and Blockchain in Transport
Alliance [61].
Ganne [62] posed the question, ‘‘Can blockchain revolutionize international trade?’’ Many applications have had an
influence on trade, including business to government (B2G)
initiatives, inter-agency coordination, streamlining certification and licensing practices, enhancing customs clearance
processes, improving temporary admission of goods, protecting the accuracy of trade data, and allowing advanced
auditing methods.
Okazaki [63] concluded that trade-related applications
can be developed and implemented with BCT, such as RT
exchange of information (EOI), data driven customs programs and financial crimes detection. Two use cases were
presented: the IBM-Maersk joint venture for global trade
digitalization and Singapore’s Global Trade Connectivity
Network (GTCN). Uddin et al. [19] talked about logistics
for retail SCs. An inventory item can be tracked from start
to end point, which guarantees trust, openness and veracity
within the SC. It encompasses the shipping pathway from
manufacturer to final customer.
4) ENERGY & POWER CONSERVATION
Cohen and Lee [4] summarized prominent BCT applications
in the energy industry; renewable energy resource management, token-based energy trading, local energy market
scenarios and power gird distribution and intervention.
Al-Jaroodi and Mohamed [51] discussed BCT in energy
related applications. Microgrid technology, infused with
BCT, not only controls and monitors the electric grid to
distribute power to those who need it but also provides
surplus credits to those who do not. Smart contracts in the
power industry enable constant communication between all
devices on the smart grid. Smart home prosumers, small
scale prosumers, primary energy source and smart vehicle
prosumers are all P2P energy trading that uses a BCTbased system. The two major use cases that are currently
seeing commercial implementations are PowerLedger and
Bankymoon [55].
Treiblmaier et al. [64] focused on smart energy or the
energy related to individuals or groups of organizations. The
blockchain is used to protect the privacy of users, deter malicious acts and promote green practices for more sustainable
practices.
BCT can be employed to upgrade an existing grid to
optimize reliability and efficiency, providing RT sensing
and monitoring to the energy management system. It can
be used with renewable energy sources, energy trading
infrastructures, power distribution systems and analytical
software [40].
Bao et al. [65] reviewed how blockchain is applied in
the energy sector. Decentralized storage, power grid control,
smart grid P2P energy trading, electric vehicles and carbon
emissions trading are implementations that have advanced
BCT. These applications intend to save energy, provide a
decentralized architecture, decrease fossil fuel consumption
and reduce the impact of climate change.
BCT can also assist in energy operations with billing,
sales & marketing, trading, automation, data transfers and
smart grid management. BCT can improve wholesale energy,
imbalance settlements, digitalization, IoT integration and
P2P energy trading. The Brooklyn MicroGrid is an example
of a use-case that utilizes a blockchain-based P2P energy
platform. Other areas in the energy sector include metering & billing, tokens & investment, decentralized energy
trading, grid management, automation, asset management,
electric e-mobility, and general-purpose initiatives and consortia [66].
Kufeoglu et al. [67] analyzed applications in the power
industry including AI, machine learning, deep learning and
digitalization. In combination, these apps simplify business
operations and provide a link between physical and digital
objects. Their work indexes global companies that have BCT
applications implemented as of today, such as Conjoule,
from Germany, a P2P marketplace for renewable energy,
and Dajie, a P2P-IoT-BCT trading platform from the UK.
Other applications for blockchain in the energy sector are a
secure payment mechanism for EV charging/discharging, for
P2P energy trading, providing green energy certificates and
to advocate for Demand Response Planning. The modern,
decentralized architecture allows for expanded security and
privacy while having flexibility [57].
Musleh et al. [68] examined decentralized technologies
for smart grid applications. The BC is used in P2P energy
trading to set a fair price for both seller and buyer, to integrate electric vehicle (EV) charging stations, to control a
trustworthy electrical grid and to monitor smart contracts to
improve grid resiliency. Additional use cases for BC include
competition between P2P power utilities and managing RT
supply & demand, energy trading and microgrid maintenance. Currently, there are close to 140 start-ups in the energy
sector [69].
5) OTHER INDUSTRIAL APPLICATIONS
Blockchain has uses for both large and small industries. The
industries listed below are small-scale sectors with fewer
references in the literature:
• Government: Blockchain technology fosters innovative
applications and handles digitalization of assets, transaction integrity and P2P exchanges. The objective of DLTs
in government is to provide transparency while reducing
security risks. E-government applications include digital
ID management, tax fraud prevention, data access control and voting protocols. The Estonian Blockchain strategy is a use case of an e-government application [40].
• Manufacturing: Technical records and other paperwork can be uploaded to the distributed ledger. BCT can
be employed as an inventory management tool, displaying the availability of spare parts in RT. In conjunction
with IoT, security and privacy techniques will become
more fortified [55]. Smart factories are dynamic environments and BC can provide flexibility, which assists
with planning and scheduling, making SCs able to adapt
on the fly. An autonomous manufacturing system links
with IoT devices to make RT decisions that result in
smart products [64].
• Smart Applications: An application’s goal is to provide security and privacy to the homeowner [56]. Smart
devices, using BCT, provide homeowners with comfort
& convenience by offering new options to better integrate their IoT devices and home security [64].
Smart home refers to the complex consolidation of
information and communications technology (ICT). IoT
devices communicate through the router via servers and
the local network to prevent privacy leakage. Architecture follows a three-layered taxonomy to ensure
security [38]. A use case is the Dubai Blockchain strategy, which is the first smart city power by the Blockchain
in 2020, to establish a business ecosystem [40].
B. CHALLENGES, OPEN RESEARCH ISSUES & SOLUTIONS
Current literature outlines key issues that global SCs
encounter before, during or after blockchain adoption: laws &
regulations, data management & provenance, governance &
traceability, interoperability & standardization, lack of awareness, education & innovation, performance & scalability, trust
& stakeholder management and transparency & visibility.
1) LAWS & REGULATIONS ISSUES
Blockchain does not have a set of general legal regulations
and standards to follow.
Chang et al. [70] recommends a comprehensive compliance profile to advance the use of standardized regulatory
mechanisms. The researchers presented four areas for future
research opportunities: distributed jurisdiction and laws, legal
framework to ensure validity, responsibility/accountability,
and data privacy.
Zhao et al. [36] stressed the necessity to introduce new
standards to regulate BC applications. Large SCs have multiple manufacturing facilities with their own set of laws and
regulations. Regulation authorities must stay vigilant and
continuously improve regulatory measures to strengthen the
international supervision of the SC [51]. Governments need
to draft new laws to allow innovative technologies to thrive
and not be slowed by barriers due to legal constraints in the
implementation of a blockchain-based system [38].
Haq and Esuka [50] identified one of the biggest challenges as integrating BCT solutions with existing regulations
and compliance with global standards. Stringent requirements hinder advancements but smart contracts can write and
enforce rules which automate SC processes and reduce costs.
Kassem et al. [71] cautioned that mistakes and vulnerabilities in smart contracts due to human error can be rescinded
but waste resources and time and present unforeseen risks.
On the other hand, not all the smart contract stipulations are
being followed and may be overregulated [60]. All facets of
the smart contract must be followed to avoid issues regarding
regulations from different countries and unclear jurisdiction.
Bekrar et al. [72] summarized legal and regulatory issues that
arise from lack of jurisdiction or when localized regulations
limit certain SC actions.
Other barriers for BCT adoption are issues during transformation related to regulation, efficiency and security. These
are focus areas for current and future research initiatives.
Creating and redefining business models that incorporate an
official legal framework is an effective way to cope with the
transformation process [73].
Okazaki [63] emphasized the use of Application Programming Interfaces (APIs) for the creation of BC solutions for
technical challenges and regulatory disparities. Lack of standardization is prevalent in world trade and disrupts digital
solution development and application.
Laws and regulations need to be updated in consideration
of the current global landscape. Protecting user’s rights and
their data poses a gap in research [74]. Katsikouli et al. [75]
called for action plans to reveal gaps in legal regulations
regarding fair trade. The implementation of fair-trade strategies in BCT is immature and presents a research gap.
Tezel et al. [76] identified the need for blockchain-based
systems compliance with existing accounting systems, regulations, frameworks, standard contracts, and laws. New
models are needed to address regulatory structure compliance
and its challenges in blockchain adoption. Policy development and regulation is mandatory and a barrier to BCT
adoption, practices, and strategies due to the lack of a regulatory framework [77].
Gohil and Thakker [78] detailed blockchain implementations challenges in handling and maintaining legal contracts
and document security. An opportunity is present for future
research in the storage and retrieval of secure legal documents
and legal compliance requirements. Legal and regulatory
uncertainties can cloud managerial involvement and decision
making in adopting BCT in SCs. Serious effort must be put
into the development of new standards capable of dealing
with risks [79].
2) LAWS & REGULATIONS SOLUTIONS
Etemadi et al. [90] introduced a solution that aims to increase
supply chain resilience. It can help monitor various laws,
threats and regulations to avoid disruption and keep a SC
running smoothly despite outside interference. An example
presented by these authors [90] discussed Cryptocontract,
a solution to create, maintain, disclose and dispute contracts.
It is a three-fold design using BCT, IoTs, and Smart Contracts. Smart contracts are traditional contracts 2.0, capable
of contract enforcement automation.
Polyviou et al. [96] noticed that studies indicated that
certain inventory items may have a regulation placed on it.
The food industry has many requirements for shipping and
receiving meat. If a product doesn’t meet these requirements,
suppliers will be notified and recommended to increase the
quality of their materials.
Mazlan et al. [105] highlighted the lack of innovative
operations, procedures and logistics in the maritime industry.
Digitalization is a promising solution in this field which
serves as the development backbone of the smart technology,
such as smart ships or smart logistics with globalization.
3) DATA MANAGEMENT & PROVENANCE ISSUES
Global SCs must manage their data effectively to provide accessibility, authenticity, availability, digitalization,
integrity, privacy, protection, provenance, security, sharing and storage. Blockchain and data storage problems in
IoT-precision agriculture networks were discussed by Torky
and Hassanein [30]. Blockchain-based storage options can
alleviate many of the issues associated with cloud-based
storage and can improve data availability and security. Other
researchers have investigated technical challenges for data
accessibility and protection. A lack of standardization has
led to unclear rules on how data should be shared and stored
between public and private BCs, leading to the need for
creating new data management standards [34].
Konstantinidis et al. [44] mentioned privacy as one of their
primary issues for BC-SC systems. Data sharing concerns
have negatively affected medical organizations as current
encryption methods can’t fully protect an actor’s identity.
Users’ identity protection is a chief concern and an area
for future research. Similarly, malicious attacks, security
breaches and compromised data jeopardizes the integrity of
patient data and diminishes privacy. Secure solutions are
needed that protect users’ identities [47].
Siyal et al. [49] indicated that without a trusted third
party, data privacy can be compromised if multiple parties
are responsible for authorization. Another challenge is the
total capacity of data storage. Future efforts should focus
on scalability and resiliency to refine record keeping and
retrieval speed.
Ahmad et al. [56] discussed identity protection as a barrier
to full privacy in IoT networks and suggested that more
in-depth research is required to tackle privacy issues by mixing available techniques.
Data provenance can increase customer satisfaction and
trust. Smart cities, for example, are dependent on efficient
SCs with dynamic business interactions. Track and traceback
procedures can upgrade BC solutions by optimizing management processes and ensuring legitimacy of information across
the SC [64].
Okazaki [63] raised concerns about the privacy and security of the data storage and accessibility on the shared ledger
as transactions are linked to identities.
Traditional logistics systems are outdated and incapable
of handling complex situations. Upgrading legacy platforms
with new forms of technology, such as BC, IoT or RFIDs,
is an important area of research [78].
Chang et al. [70] highlighted the disruption of information
flows in global SCs due to the large volume of documents, from bills of lading to certifications. Digitalization
is a promising opportunity to streamline administrative practices along with provenance to ensure legitimacy and detect
counterfeiting.
Rejeb et al. [85] indicated that human manipulation of data
or information in non-IoT scenarios remains an industry challenge and new BC solutions should focus on identification
verification and device authentication. The paper emphasizes
the importance of data quality and provenance and identified
three challenges: data control, authenticity, and monetization.
The lack of aggregate IoT data is a gap and potential area for
future research.
Bodkhe et al. [84] identified areas that need further
development to address security challenges, including data
modification and unauthorized access, in HC. Other areas
include increased data volume and information processing
complexity, data provenance and integrity, and protection of
users’ data when stored in a centralized database.
Different privacy policies relating to information and data
usage, sharing and release may hinder successful implementations of BCT in SC. New IT tools are necessary to mitigate
limitations in RT information accessibility and to enhance
storage management [86].
Two major technical challenges to modern SCs, access
control and data retrieval, were outlined by Wu et al. [87].
New approaches are required to pull the desired data efficiently and reliably from the BC while preserving data
privacy. Kumar et al. [88] indicated another storage challenge
was deciding which data gets stored on the blockchain or
off-chain.
Blockchain transactions are not well suited for sensitive data since they are transparent and irreversible. New
approaches need to be flexible enough to change transaction
parameters using smart contracts and be versatile enough to
oversee large amounts of data [83]. Kamilaris et al. [77] listed
accessibility as an open issue to agriculture blockchains. The
information infrastructure required to operate and maintain
BC systems might prevent access to markets for new users.
Etemadi et al. [90] focused on authentication security
protocols in blockchain to ensure department privacy and
security from potential attacks. New solutions need to focus
on safeguarding privacy while enabling connectivity, increasing the effectiveness of IoT devices. More attention needs to
be devoted to data storage methods in BC implementations
in end-to-end SCs. Other authors have cited privacy risks
as a main barrier to BC adoption. More secure consensus
algorithms are required to improve system security and
privacy [79].
4) DATA MANAGEMENT & PROVENANCE SOLUTIONS
Zhao et al. [36] looked at the challenges in applying BCT
in agri-food value chains. Privacy leakage is a significant
barrier to transparency and trust building, thus encryption (i.e., obfuscation) is a promising area for BC solution
research.
Al-Farsi et al. [80] presented three solutions that have been
created from academic efforts. The first solution’s target was
to preserve information privacy. It allowed for auditability,
ownership and authenticity of goods. Potential attack mechanisms, such as breach of data integrity, can be prevented and
stopped altogether with this option. The second solution is
secure data sharing which introduces a decentralized file system, BCT integration and storage schemes. The third and final
solution’s topic was data provenance, which allows accurate
product tracing and enables provenance. Both solutions two
and three prevent attacks such as data integrity breach, tampered input data and false data reports.
Chang et al. [70] presented a solution regarding port
container operations. Data access and control is limited by
credentials, digital rights exist between parties, rights can be
transferred, and operations can be digitized without a thirdparty source.
Afanasev et al. [83] examined Blockchain as a Service
(BaaS) as a solution for data management. Supply chains
can build and operate applications and their functions, which
increases flexibility. Cloud-based storage is the best option
for databases within the BaaS since companies wanting to
adopt this service will pay and sign a contract for a certain
amount of time.
Litke et al. [89] proposed a data management solution for
data exchange. Input data is mandatory and must be entered
to give a larger level of detail than most solutions. The system boasts better tracking methods and faster identification
processes.
Etemadi et al. [90] proposed a solution for product provenance for cyber risk identification & mitigation. Essential
product information, credentials, rights are stored on many
IoT devices in case of a security issue.
Everledger, part of the Hyperledger Fabric framework,
is an implementation that tracks the provenance of assets with
high costs [99].
5) GOVERNANCE & TRACEABILITY ISSUES
Traceability and governance are key challenges in global
SC due to increasingly complex systems. Katsikouli et al.
[75] indicated that when traceability is decreased, vulnerabilities appear, and compliancy becomes lax. Agarwal et al.
[91] mentioned traceability as a major challenge which
can become an industry inefficiency causing delays, errors
and increased costs. Demestichas et al. [33] concluded that
complex SCs tend to have issues with traceability. Opportunities exist by leveraging big data and machine learning to
yield a more efficient production process.
Feng et al. [37] addressed five major challenge areas
in blockchain for sustainable traceability practices, including technical challenges, blockchain infrastructure, social,
institutional and system performance. A blockchain-based
traceability system lacks the public key infrastructure needed
for quality control, inter-domain policies, and to authenticate
products.
Friedman and Ormiston [92] looked at the possibilities
for blockchain to approach food traceability sustainability
issues. Contamination and spoilage occur frequently due to
lack of safety and quality standards which negates public
health. BCT promotes trust in an environment with strangers
by keeping data secure, verifiable and manageable. Track
and trace methodologies can become more effective via
blockchain intervention.
Haq and Esuka [50] discussed four challenges to BC adoption: technical, legal, business and trust. Governance is the
establishment of trust without the need for a central authority.
Regulatory and legal requirements can slow governing models by forcing stakeholders to perform the role of regulator.
The work of Ariningsih and Sundara [93] partially examined
the traceability and governance of SC flows during natural
disasters. The new model uses blockchain implementation,
along with Vendor Managed Inventory (VMI) to create an
alliance among SCs and to provide trust when it is lacking.
Information sharing and consensus are two BCT features that
are suitable for disaster relief efforts in the future.
Bodkhe et al. [84] stated a key challenge to traceability is the lack of total number of implementations.
Current approaches have drawbacks such as no hardware
compatibility, lack of privacy, supervision, and transaction
speed. Ahmed and MacCarthy [94] noted the lack of standards for traceability in blockchain adoption efforts and
the lack of guidance in application implementations. Limited understanding stifles robust initiatives, making business
requirements unclear and often confusing. Different SC configurations have different requirements and each project
should be looked at differently. The granularity of data and
diversity of scope are two areas that need further research to
better understand blockchain initiatives and the effects they
have on global SCs.
Rogerson and Parry [97] examined issues of governance
surrounding BCT. More research is needed to address the lack
of standards which creates data inconsistency.
Reliance on centrality and lack of trusted information
among SC actors are two gaps in current research [90].
Despite the new frameworks proposed, there are opportunities available for creation and enhancements.
6) GOVERNANCE & TRACEABILITY SOLUTIONS
Venkatesh et al. [14] discussed a BCT solution called the
Product Service System (PSS) that combines BCT & IoT. The
PSS has been used in many industrial applications including
RFIDs and aircraft engines. Offers three services in one
package; product, use, result.
Gohil and Thakker [78] talked about practical implementations used today. Hyperledger Sawtooth offers open source
solutions to businesses and has seen success in the seafood
supply chain. It enforces traceability by recording daily information and storing it in case of review or audit. Research
projects have been implemented that focus on IoT integration
and the use of open-source frameworks for DLTs. Al-Farsi
et al. [80] introduced many BCT solutions. The solution for
governance gave SCs ownership rights, compliance directives, data privacy and policy design & analysis. Potential
attack mechanisms include data integrity breach and tampered input data can be halted with this promising solution.
Chang et al. [70] reviewed a Just-in-Time (JIT) production solution that aims to monitor a system accurately by
using RFIDs, notifications, warnings, and provide visibility
through IoT devices. Bodkhe et al. [84] advanced Chang
et al.’s [70] philosophy by further advancing operational control. also proposed a solution for operation control which aims
to eliminate bottlenecks, optimize planning & scheduling
The compromise between confidentiality and traceability
is a significant challenge in BCT [95]. A gap in research exists
in finding a balance between the two through the development
of new solutions capable of RT updates and tracing. Kamilaris
et al. [77] indicated that the long-term impact of blockchain
on governance still needs to be assessed. SC monitoring
with IoT relies on two main functions, tracking and tracing. Data integrity, tampering and centrality affect tracing.
BC implementations can eliminate gaps by reducing human
intervention, ensuring data reliability and information system
integration [96].
Wu et al. [87] examined Everledger. Their top priority is
the transparency of global supply chains. They offer provenance and asset tracking in this digital transparency company.
Etemadi et al. [90] briefly discussed anti-counterfeiting to
enforce governance over a worldwide SC. Tracing drugs can
make it near impossible for dishonest people to sell counterfeit medicines or prescriptions. Finding counterfeit products
keeps your supply chain uncompromised.
The authors [90] also recognized Counterchain as a solution for drug governance and origin traceability. Authenticity
is protected through this platform through automation, monitoring and regulating.
Walmart, Kroger and other department conglomerates use
BCT solutions to keep products unadulterated, erase fraud
and getting more suppliers involved in their SC network to
achieve better product traceability [104].
7) INTEROPERABILITY & STANDARDIZATION ISSUES
The lack of standardization or a common set of standards has
limited blockchain interoperability and a unified set of standards is necessary to streamline interoperability in SCs [34].
A research opportunity is closing the interoperability gap
between ledger types.
Another area of research is the formulation of standards
and regulations to reduce investment cost and human resource
allocation in international trade [36]. Agbo et al. [47] focused
part of their work on interoperability difficulties. Without
standards, industrial applications experience operation issues.
The need for open standards is a promising area for new
research projects. An international set of standards is needed
to unify services and ensure data integrity when implementing blockchains in HC [49].
Interoperability and standardization challenges have led to
integration issues in BCT adoption [50]. The creation of new
standards is a research opportunity that could assuage the
integration issues between multiple devices. When manufacturers integrate multiple blockchains, there is a heightened
need for interoperable systems [55]. The authors noted the
significant challenge of interoperability and called for implementations to become standardized.
Kassem et al. [71] summarized interoperability challenges
for blockchain applications where requirements differ. Future
work could focus on the access layer, developing applicationspecific functions. Lack of interoperability has also caused
issues with data retrieval, resolving collaboration and crosschain interaction, and wider BCT adoption. An opportunity
for future research is the creation of industry-wide standards
and practices [98].
Lack of standardization has led to technical incompatibility
between large and small suppliers in food SCs[99]. Similarly,
in the agricultural industry, a major challenge is the lack of
standardization in data format, lending itself to research in
the creation of protocols, shared among actors [100].
As with other researchers, Katsikouli et al. [75] promotes
standardization as a key issue in BCT adoption. This issue
presents a research gap, as there is no common standard
for all regions and countries. Mann et al. [101] cited lack
of industry standards in mining has disrupted intellectual
property (IP) property patents. Opportunities exist in the
development and refinement of standard technology for BCT
implementation.
8) INTEROPERABILITY & STANDARDIZATION SOLUTIONS
Al-Farsi et al. [80] introduced three distinct solutions for
interoperability: between heterogenous systems, seamless
operation and among cross-border entities. These solutions
allow for secure party interaction, dispute settlement, access
control privileges and transparent finances. They prevent
attacks like the breach of data integrity, falsified information
or results reports and tampered input data.
Afanasev et al. [83]summarized real examples of solutions
available to SCs using blockchain. The CONNECT project
allows IoT networks to interact with each other without using
a network address. Suggested solutions aim to enhance IoT
heterogeneity and interoperability. Other practical examples
include Ethereum, IOTA and Hyperledger. R3 Corda is a
smart contract solution to assist with creating an interoperability network with regulated privacy [86].
Jabbar et al. [98] summarized three blockchain solutions
that help increase interoperability. Notary schemes, hash
locking, side chains and relays are all examples. These items
have limited use & functionality and can be used as a foundation for future work & improvements.
Rauniyar et al. [104]spoke about Skuchain, a company that
allows banks to trade digital financial services to their customers or to conduct business. Establishing interoperability
between various trade platforms is their main objective and
contribution to interoperable solutions development using
emergent technologies.
9) LACK OF AWARENESS, EDUCATION & INNOVATION
ISSUES
Duan et al. [74]suggested the lack of understanding of BCT’s
true potential hinders solutions since companies are looking
for an easy fix instead of addressing organizational issues.
It may be more challenging for SMEs to flourish from the
lack of financial resources, skills, and expertise [102].
Chen et al. [99] discussed that unfamiliarity and lack of
knowledge of BC adoption has held back and postponed
initiatives. Labor and skill shortage are also a factor. Lack of
innovation is a challenge for advanced industries that utilize
new forms of technology [103]. Operations, procedures, and
logistics need improvements to be able to support critical
infrastructures to remain globally connected and distributed.
Saberi et al. [86]summarized lack of awareness challenges,
like resource allocation and financial decisions. Organizations need to reform old policies, adopt new technology and
transform workplace culture for personnel to accept BCT.
Lack of managerial commitment to blockchain implementation is a significant barrier as effective SCM relies on support
from top management [79]. Sustainable practices are becoming more common as environmental regulations force global
SCs to rectify practices and conform to societal rules [86].
Industry sectors, corporate cultures and the behavior of users
can be detrimental to the decision to adopt BCT [90].
10) LACK OF AWARENESS, EDUCATION & INNOVATION
SOLUTIONS
Blockchain solutions need to be appreciated by all employees
to benefit from the technology and to foster confidence in
future efforts. Al-Farsi et al. [80] briefly mentioned lack
of awareness solutions that ensure the secure exchange of
information. These solutions are excellent at detecting any
compromises or anomalies. Stakeholders haven’t fully committed to the solution since it involves complete trust and no
credibility when an error occurs. Improvements need to be
made to push the solution to its full potential.
Rauniyar et al. [104] noticed that many implementations
lack innovation and awareness to detail. The airline industry
has shown interest in using BCT. Airbus, Lufthansa and
British Airways all have projects underway but many lack the
ability to fully complete the objective. Manual efforts must be
made to ensure complexity, which conflicts with automation.
11) PERFORMANCE & SCALABILITY ISSUES
Performance is a primary concern in today’s global market,
adversely affecting bandwidth, efficiency, latency, throughput, and scalability. Torky and Hassanein [30] discussed the
challenges of IoT networks and blockchain solutions. IoT
device & sensor communication rules, energy conservation,
complex network scaling and limited storage solutions are
opportunities for future BC research projects. Several technical, regulatory, institutional, infrastructure and capacity
development related challenges that need to be addressed
before scalability reaches maturity [34]. A gap in research
exists in the trade-off between anonymity and identity.
Challenges for IoT devices in BC include scalability, security, and stability [37]. Rauniyar et al. [104] examined BCT
integration with IoT devices. Their findings proved that risk
mitigation plays a pivotal role in SC performance through
innovation by creating new sub-categories like dispute resolution and fraud prevention. Performance indicators, like
storage capacity, and processing ability need more research
to improve quality traceability systems.
Latency and scalability are two performance challenges [42]. A barrier to scaling is the response time and
system latency that increases with the number of users. Lack
of network latency is an opportunity for future BC infrastructure research.
Latency is the biggest limitation of all consensus protocols.
Current protocols address the issue, but more work is necessary to speed up the confirmation process [44]. Scalability is
a significant barrier to BC in HC. The large volume of data
involved introduces latency into the network, affecting transaction speed. Validation mechanisms need to be optimized to
store large amounts of transactional data without degrading
performance [47].
Jovic et al. [60] explained blockchain challenges due to
performance and scalability issues. Conserving processing
power since all nodes in a chain must process all transactions
is an area of investigation.
BC faces challenges such as scalability, efficiency, and
complexity in the use of smart devices in intelligent transportation systems. Architectures need to be flexible enough
to deal with large numbers of devices. Future work must
focus on adding functionality, such as scalability and simplicity [106]. Rejeb et al. [85] proposed combining IoT with BCT.
Scalability is an issue due to the limited number of nodes and
the ability of IoT devices. Existing proposals lack the ability
to combine decentrality, scalability and security. Refusal to
share information, effective incentive mechanisms and lack
of trust and collaborative activities are identified as major BC
barriers [102]. Bodkhe et al. [84] also explored scalability
obstacles. RT scenarios require millions of transactions to
be executed posing a significant research gap for scalable
transactions.
A prime challenge in BC for SCM is how systems scale
and operate with an increasing number of stakeholders and
large amounts of transactional data. Reparameterization of
the block size and inter-block interval can improve the system, but without a fundamental redesign of the blockchain
paradigm, scalability issues will always occur [87].
Jabbar et al. [98] divided scalability into four approaches:
on-chain, off-chain, consensus mechanisms, distributed
acyclic graph-based. It was noted that a fundamental change
is required in BCT architecture to modify protocols and
optimize algorithms.
Litke et al. [89] focused on bandwidth constraints due to a
network’s physical limit. Scalability is limited by the number
of transactions each block can take.
Kamilaris et al. [77] concluded that blockchain protocols
face serious obstacles since the system is limited by network
parameters like transaction block size & interval. Bekrar
et al. [72] indicated that BC immaturity has led to a major
concern with scalability. The authors supported Wu et al. [87]
and Jabbar et al. [98] in reasoning that newer developments
and protocols must be designed with scalability in mind.
Future work must focus on sharding without losing security.
Venkatesh et al. [14] summarized past scalability challenges.
Network changes result in slow processing speeds and block
size limitations. Future research initiatives must focus on
enhancing performance parameters.
12) PERFORMANCE & SCALABILITY SOLUTIONS
Agbo et al. [47] and Alladi et al. [55] looked at the scalable
implementation of BC for HC. The large size of data is a
practical issue for feasibility and scalability. Data storage
and retrieval is a current gap in research, as solutions need
to be scalable but efficient. Huge amounts of data increase
computation and time, constricting scalable solutions within
IoT networks. Storage optimization is a future research area
in network infrastructure and node behavior [56].
Block size, high volume, transactions, number of nodes
and protocols are barriers to scalable solutions [105].
Redesigning the blockchain and storage optimization are
two areas of research needed to gain insight on system performance.
Innovative and scalable solutions are under development
and need more work. Additionally, developers are working
to find a better to solution to extend BC scalability while
keeping high security and decentralization within the food
SC [74].
Saberi et al. [86] suggested that improvements are needed
in storage management and advanced cloud computing to
have viable storage options for scalable solutions, an area that
needs further investigation.
Rejeb et al. [85] and Jabbar et al. [98] both discussed a
scalability solution that is termed off-chain scaling. It runs
alongside the blockchain, or in parallel. The primary purpose is to exchange data between both chains. A concern is
the compatibility of off-chain scaling with existing business
infrastructure.
Jabbar et al. [98] also talked about on-chain scaling too.
It requires companies to change their current structures.
Sharding is an example of an on-chain scaling solution.
The blockchain is separated into smaller pieces instead of
a singular system. The authors also focused on consensus
mechanism scaling. VeChain and NEO are two examples of
blockchains that utilize consensus-mechanism scaling.
Bekrar et al. [72] and Jabbar et al. [98] discussed distributed acyclic graph-based scaling which is a distributed
ledger technology that can process transactions much quicker
making them more scalable than other solutions. IOTA and
NANO Hashgraph & Byteball are all examples of DAG
scaling.
Hyperledger Fabric is a scalable solution that uses smart
contracts to with excellent community support [86]. It has
been adopted by IBM, Cisco and SAP for its ability to handle
financial applications and aims to unify all developments of
blockchain technology that crosses industries [104].
Wu et al. [87] briefly mentioned reparameterization as a
scalability solution. It causes the inter-block interval speed to
increase and block size expansion.
Sharding is a scalability solution. Data partitioning is used
to lower transactions fees and wait times. Memory storage is
done via horizontal data partitioning [97].
Haque et al. [112] presented a comprehensive framework for addressing scalability issues. Scalable Edge IoT
Blockchain (SEB) aims to enhance IoT performance & efficiency within a blockchain network using a combination of
sharding, Interplanetary File System (IPFS) and the Delegated Proof of Stake (DPoS) protocol. Resource utilization,
latency and throughput are all metrics that improved as a
result of EOSIO BC implementation.
13) TRUST & STAKEHOLDER MANAGEMENT ISSUES
Stakeholder management is essential to establishing trust
without intermediaries and coordination in global SCs. Poor
infrastructure has led to a lack of digital skills and trust.
Stakeholder collaboration is crucial to maintaining trust &
full interoperability [37]. A considerable level of skepticism
exists among stakeholders in the agri-food value chain [36]
More work is needed to resolve technical BCT issues by
instilling trust in stakeholders.
Chang et al. [70] recognized trust as one of the most
important factors in a committed and collaboration environment between stakeholders. Current stakeholders rely heavily
on central intermediaries for transactions. The removal of
intermediaries is an opportunity for research with BCT. The
lack of infrastructure uniformity and stakeholder awareness
are two obstacles to BC implementations and SC innovation.
The replacement of policy and lack of methodology is a gap in
research that must be addressed [95]. Litke et al. [89] realized
the significance of stakeholders (actors) relationships to the
nurturing of trust. The shift from relational to technological
trust is occurring in the construction industry and creates
opportunities for future work in policy making. Poor information flow among stakeholders is major challenge across a
global SC. A platform for coordinating multiple stakeholders
is another research opportunity [108].
Complex SCs have many stakeholders, so RT access of
operational data is key to making informed decisions. Accessibility is an area for future work, as it directly correlates
to trust in blockchain-based systems [78]. High levels of
trust can be more quickly established through digital trust as
opposed to traditional SC relationships[102]. Other problems
commonly experienced by stakeholders have been articulated [90]. Information sharing, digitalization, response time
and low collaboration are obstacles that need further research
initiatives. These issues diminish the value of trust in BCT.
14) TRUST & STAKEHOLDER MANAGEMENT SOLUTIONS
The incentivization of current operational and business
models is an opportunity for new BC solutions in HC. Stakeholders are more likely to participate if there is a reward for
their work [50].
Ahmad et al. [56] split their research into research
challenges and future directions. Trust and reputation management is a difficulty for IoT devices. Blockchain solutions
can play a pivotal role in node recommendation and reputation, but more research is needed in this area. Lack of
trust and limited collaboration is a key issue that hinders
BCT adoption. Increased collaboration and trust are needed
to ensure all parties are fair and use the same, transparent
data [71]. The establishment of BC solutions for developing
countries or SMEs is an opportunity for future work [74].
Rauniyar et al. [104] discussed a solution to increase stakeholder management and increase trust. The stakeholders have
a complete view of all data as product flows. Moyee Coffee
uses tokens to represent the commodity’s value. It is created
when the product begins and increases in value as it travels
toward the end of production.
The authors [104] also summarized the Hyundai Merchant
Maritime (HMM) initiative, which utilized the BC to allow
secure sharing of data between many stakeholders throughout shipment. The project proved that new solutions, that
combine various forms of technology like IoT, can improve
maritime vessel monitoring and management.
As the number of stakeholders increases, so does the need
for trustworthy, transparent frameworks that allow companies
to have successful BCT implementations [107]. New governing policies are essential to changing workplace culture and
fostering cross-organizational communication.
15) TRANSPARENCY & VISIBLITY ISSUES
Transparency is a growing concern for global SCs. Transparency is a feature SCs hope to gain from BCT adoption.
Accurate data is a challenge that needs to be addressed to
keep product information complete. Historical and performance data must be made available in the BC to safeguard
sustainable practices while creating new ones [92]. Barriers
stand in the way of the acceptance of blockchain technology
in supply chains. Organizations need to be fully prepared
prior to implementation, infrastructure and expertise must
be solved before integration. The blockchain will increase
visibility by keeping records transparent for all stakeholders
TABLE 6. Challenges & research gaps.
TABLE 7. Blockchain solutions for global supply chain management.
in the SC network [109]. Orenstein’s [110] research looked
at creating transparency in SC networks. Using a dashboard,
a visualization tool, Key Performance Indicators (KPIs) were
used to identify several information dimensions to a particular
business process. Once a layered map is created, network
metrics can be acquired and analyzed to see the impact of
removing or redistributing key nodes [110]. It can theoretically be used to examine a traditional system versus a new
blockchain-based platform to a before and after look of the
implementation process.
IoT devices experience open issues including lack of transparency in blockchain deployment. An opportunity exists for
the establishment of BC solutions to improve infrastructures.
When systems have issues, visibility is decreased across the
SC. Future work should spotlight ways to improve policies,
regulations and tracking systems for connectivity [84]. Lack
of transparency has led to low trust among SC members.
A major opportunity is present to overcome trust within an
organization prior to adoption [95]. End-to-end visibility is
the chief concern for SCs. The visibility of the complete product lifecycle is an opportunity for future research work [78].
Etemadi et al. [90] briefly analyzed adoption, benefits and
challenges in SCs. The main issues were visibility and transparency of SC assets.
16) TRANSPARENCY & VISIBILITY SOLUTIONS
A promising research area is the use of collaborative,
open-source platforms with new, transparent solutions [34].
Blockchain solutions can allow global supply chains to
address challenges and overcome obstacles. Table 7 lists
30 potential solutions that provide a distinct research opportunity. The objective is to advance blockchain technology for
global supply chain management applications.
Riva [81] introduced the Privacy by Layers approach which
combines the need for a transparent SC with the protection of
individual privacy rights using a side chain. The objective is to
install a data controller, to govern the e-ledger, be responsible
for accessibility and to grant permissions to access block
content.
Sunny et al. [82] focus on supply chain transparency
enabled by BCT. One section of their research focused on the
food and agricultural SC. Specifically, traceability solutions
that are focus on the quality of food, stringent food requirements for religion or by government and origin tracing.
The authors [82] also showed that there is a common
combination of IoT, RFID, GPS & BCT in the literature. It has
a multitude of uses by has been seen to have success in advocating the adhered to environment and social sustainability
standards, RT tracking and tracing, counterfeiting items and
preventing food safety hazard.
VIII. IMPLICATIONS, LIMITATIONS & FUTURE WORK
A. THEORETICAL IMPLICATIONS
The effectiveness of smart contracts can be improved by
expanding functionality and improving accuracy. SCs have
undergone a transformation in recent years, combining BCT
with other technologies such as machine learning, AI, IoT
devices, APIs, big data, GPS, and advanced cloud computing.
Blockchain has gained attention in recent years due to its
applicability in a variety of industries. Current infrastructures
need to be renovated with flexible frameworks and uniform
architectures [79]. BC’s true potential has yet to be reached
and current literature is mainly conceptual.
The concept of globalization has become more prevalent in
supply chains and logistics. With the advent of new forms of
technology, monitoring and controlling becomes mandatory,
as processes become more complex and geographically dispersed. A collaborative network is difficult to achieve [34],
[90], [108] due to stringent requirements, lack of resources
and financial constraints. Developing nations and SMEs lack
the capability, expertise or monetary support to compete
effectively. Empirical studies leave out smaller SCs purporting disproportionate growth, inequality and trade imbalances.
B. PRACTICAL IMPLICATIONS
The most promising areas in BCT for immediate applicability are governance, traceability, performance and scalability.
In BC-based global supply chains, IoT devices are used in
conjunction with RFIDs to provide RT product tracing and
governance. They increase visibility by increasing the level
of operational control. Situation reports provide accurate
alerts and warnings. IoT devices control processing capacity,
throughput and set-up time to optimize production planning
and scheduling in Just-in-Time (JIT) production operations.
These solutions have experienced success but can be further
advanced by focusing on productivity, operational costs and
customer satisfaction [85]. Additional devices can be used
to increase accuracy pertaining to inventory management,
replenishment and delivery.
Off-chain scaling solutions, or sidechains, are transactions
that are done privately, off the blockchain network. They run
in parallel to normal operations and transfer value between
them [85]. The data stored off-chain has reference numbers
tied to them and can be pulled at any time and sent to the
main blockchain. Adding functionality to this solution can
decrease congestion, increase throughput [98] and diminish
storage complexity.
Sharding is a blockchain solution that partitions data
to shorten confirmation time and lower transaction fees.
It partitions data horizontally to assign storage in memory [72]. Ethereum aims to increase security by distributing
both system storage and smart contract executions. Anticounterfeiting solutions have been applied in the pharmaceutical industry to enhance medicine traceability. Using a
combination of BCT and encrypted quick response (QR), all
information is transmitted to the chain, where smart contracts
examine and diagnose medicine properties [90].
C. POLICY-MAKER IMPLICATIONS
Policymakers must encourage the use of blockchain technology as a singular technology or combined with new forms of
technologies to enhance global supply chains. From the policy perspective, launch plans and initiatives must have BCT
implementations, promoting the shift toward decentralized
technologies [111].
There are many benefits of training and planning programs
for employee opportunity & advancement. Costs can be offset
or replaced completely if the relevant resources are there.
Employees will be more comfortable with the switch to BC
and have confidence from the hours of education.
D. RESEARCH LIMITATIONS & FUTURE WORK
Limitations in blockchain technology research are immaturity, globalization infancy, blockchain implementations
restrictions, lack of specialty sources, sources published
within the last six years and lack of practical solutions for
open issues and gaps in research. Global SCs must innovate to
remain relevant while facing fierce competition and demanding customers. There are also additional limitations within
this survey research. First is the lack of sources that specialize
in a single topic. Research needs to shift from including a
multitude of concepts to concentrating on a specific area.
Second, the survey’s scope was confined to papers published
in the last six years. Older papers that contain pertinent
information will be left out in favor of up-to-date sources.
Blockchain implementations are restricted to supply chain
management, logistics and manufacturing. Sources that did
not meet the selection criteria were eliminated from the
survey, creating an environment where exclusions limit the
breadth of work. The final limitation is the lack of practical
solutions with working examples that are applicable to global
SCs. Tools are needed to solve many problems associated
with BCT adoption. Conceptual papers provide a blueprint
for future implementations but lack the ability to propose and
construct solutions.
The lack of practical solutions is also a limitation to this
survey leaving a significant gap in the understanding applications. The lack of practical solutions with working examples
was included in this survey but more examples could have
been reviewed to provide a bigger picture of current and
future implementations. The lack of case studies, proof of
concept and good examples has placed a constraint on the
overall body of work.
Future research should promote extensive deployment
strategies, detailed case studies and open code repositories.
Explicit implementations are needed for researchers to gain a
better understanding of what blockchain solutions offer and
how they can affect industry applications and practitioners.
It will aid in the creation of new materials that will assist
with education and awareness of emergent technologies while
allowing for more advanced solutions from academia.
The aim of the survey was to provide a detailed summary
of the most relevant and current research articles pertaining to
BC applications, challenges and vulnerabilities in SCM. The
objectives were to find opportunities for future work, based
on known research gaps, to define available opportunities,
to list successful approaches and to make suggestions for
future research projects to advance the global landscape in
blockchain technology development.
Future research will focus on the use of blockchain technology as a tool for improvement. Researchers look for new
applications within the sphere of supply chain management.
A prospect for future research involves the improvement of
current ERP systems. Enterprise Resource Planning (ERP)
software uses closed, centralized systems to conduct business and maintain their databases. Ethereum allows for dApp
development and can be applied to an existing ERP system to
provide a decentralized option for data storage. Using Tryton
ERP, an open source ERP available for all operating systems
(OS), a new model is required to provide ERP systems with
decentralized options. The new framework will be developed
and proposed to provide equivalent parts between both systems and to see if there are any benefits over a centralized
system.
A decentralized version of Tryton ERP will be modified
to insert a new application programming interface (API) and
smart contracts to replace the traditional, centralized clientserver database. Web3 API will replace the base Tryton ERP
due to its decentralized nature. It communicates between the
ERP and the BC by calling smart contracts or parts of smart
contracts. It also sends data to the metrics GUI, which will be
developed to show a visual representation of the data during
testing.
Smart contracts will be developed and deployed to an
Ethereum Test Network database. There are two programming languages that will be used in the experiment. Python is
used for Tryton modifications, API operation and GUI data
display. Solidity is responsible for smart contract mediation
using the Truffle framework.
A group of metrics will be collected during the experiment for a comparative study. Each metric is a mathematical
formula that is directly derived from the data acquired. The
metrics will determine which system performs better. Once
enough tests have been run to acquire a large enough sample
size, conclusions can be inferred to see which system is the
better option. Decentralized databases can offer companies
more options with data security and storage.