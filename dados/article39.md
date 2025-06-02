Title: BSM-6G: Blockchain-Based Dynamic Spectrum Management for 6G Networks: Addressing Interoperability and Scalability

ABSTRACT The radio frequency spectrum serves as a fundamental resource for wireless communication,
encompassing various frequency bands allocated for diverse services and applications. Dynamic spectrum
management (DSM) is essential to optimise the utilisation of this limited and valuable natural resource, with
the aim of improving performance and adapting to changing wireless communication demands. Traditional
static spectrum allocation methods have shown inefficiencies, leading to spectrum scarcity and underutilisation. To address these challenges, the integration of blockchain and Cognitive Radio (CR) technologies
has emerged as a promising approach. Blockchain, with its decentralised and secure attributes, can improve
transparency and trust in spectrum allocation processes, while CR enables intelligent spectrum sensing and
allocation to maximise utilisation. However, this promising approach comes with its own critical challenges,
especially when dealing with the 6th Generation (6G) mobile communication. These challenges are related
to the fact that the blockchain ecosystem needs to be interoperable and scalable enough to be compatible with
the 6G high-demand and substantial resources. Specifically, integrating blockchain with CR requires efficient
interoperability techniques where blockchain can easily and effectively interact with the CR platforms as well
as radio spectrum environments. Furthermore, the spectrum management system over 6G networks needs
to be designed in a way where massive 6G resources can be accommodated and managed without having
any service performance degradation. This paper introduces a novel radio spectrum management model in
6G networks, named as BSM-6G, which integrates blockchain technology with CR where interoperability
is preserved and scalability is maximised. Specifically, the proposed BSM-6G model merges blockchain’s
transparent record keeping with CR’s intelligent spectrum management capabilities. To overcome the
interoperability issue, BSM-6G provides an interoperable blockchain Oracle approach which facilitates the
real-time interaction among the blockchain platform, the CR, and any data sources off-chain. This paper
details all the technical and procedural challenges when implementing the proposed interoperability Oracle
approach. To address the scalability challenge, BSM-6G utilizes the Proof-of-History (PoH) consensus
protocol to align with the requirements of DSM in advanced networks like Beyond 5th Generation (B5G) and
6G. Evaluation results indicate that BSM-6G offers viable and less complex blockchain Oracle integration
architecture measured by the technical implementation of BSM-6G, as well as low interoperability cost
measured by transaction response time and transaction fee cost. Compared to state-of-the-art spectrum-based
blockchain systems, BSM-6G shows a high scalable DSM-based blockchain in 6G networks measured by
transactions per second (TPS).
INDEX TERMS 6G mobile communication, blockchains, cognitive radio, interoperability, radio spectrum
management, scalability.
I. INTRODUCTION
The radio frequency spectrum encompasses the range of electromagnetic frequencies used for wireless communication
and includes various frequency bands allocated for different
services and applications [1]. The process of controlling and
managing the use of the radio frequency spectrum is known
as Spectrum Management, which is a limited and valuable
natural resource [1]. Within the spectrum landscape, there are
two primary categories: licensed and unlicensed bands [1],
[2]. Licensed bands are allocated to specific Primary Users
(PU)s, such as broadcasters, government agencies, and
cellular and Citizens Broadband Radio Service (CBRS)
operators networks [1], [3], [4]. These PUs have exclusive
rights to operate within their assigned frequency ranges.
On the other hand, unlicensed bands are open for use by
Secondary Users (SU)s, who can leverage these frequencies
for innovative applications and experimentation [1].
Dynamic Spectrum Management (DSM) has introduced
to address the traditional static spectrum allocation methods
which have proven to be inefficient, leading to spectrum
scarcity and underutilization [1]. DSM refers to the techniques and strategies employed to dynamically allocate radio
frequencies based on real-time demand and availability [5].
The goal of DSM is to enhance spectrum utilization,
optimize performance, and accommodate diverse wireless
communication services and applications [1], [5].
Cognitive Radio (CR) have emerged as a promising
approach to enhance the radio spectrum sensing in DSM [1],
[6]. CR is an intelligent wireless communication technology
that enables devices to sense their environment, learn
from it, and autonomously make decisions about spectrum
utilization [7]. By leveraging CR, DSM aims to maximize
spectrum utilization by allowing SUs to opportunistically
access underutilized frequency bands while ensuring minimal
interference to PUs in the landscape of 6G networks [4].
Blockchain offers several capabilities such as immutability,
transparency, security, smart contracts, interoperability, and
cost efficiency makes blockchain technology well-suited for
adoption across multiple life sectors, offering innovative
solutions to address various challenges and opportunities [8],
[9], [10]. Due to blockchain technology capabilities, many
DSM systems-based blockchain have been introduced to
support the automation, transparency, trust, and accountability in spectrum allocation processes within the dynamic
Beyond 5th Generation (B5G) and future 6th Generation (6G)
networks [4], [11]. Recently, the integration of blockchain
and CR have emerged as a promising approach where
blockchain offers a trusted and transparent record for CR’s
intelligent spectrum sensing data [1], [6]. This integration
improves the DSM performance as CR sensing data will be
easily accessed and accurately retrieved to the blockchain
using Oracles in blockchain-based process.
In this paper, we address the following problem. How
can blockchain characteristics be combined with the existing
intelligent spectrum techniques of CR in a way that offers
both cost-effective interoperability and scalability within
the framework of 6G networks? We hypothesize that a
solution addressing this problem statement should consist
of 1) a conceptual radio spectrum management framework
which is based on blockchain and CR; 2) the use of
novel mechanisms as part of this framework to enable the
interoperability Oracle with blockchain and CR. The Oracle
will enable the connection between the blockchain and the
6G radio spectrum sensing data maintained by CR, which
needs to be interoperable with the blockchain platform
that enables automated, trusted, and accurate decisions on
the sensing data; and, finally, 3) the use of Proof-ofHistory (PoH) consensus mechanism within the blockchain
model as a scalability strategy which contributes towards
faster automated radio spectrum decisions in 6G networks.
This paper introduces a novel radio spectrum management
framework which incorporates blockchain and CR into 6G
DSM systems. To the best of our knowledge, this is the first
work in the context of DSM in 6G networks that focuses on
designing a cost-effective and less complex interoperability
technique using Oracle which facilitates the interaction
between blockchain and CR.
II. MOTIVATION
Despite the promising potential of DSM using blockchain
and CR, two primary challenges stand out: interoperability
and scalability. As the number of connected devices and
wireless services continues to increase in the context of
future 6G networks [4], [11], developing scalable DSM
systems capable of handling numerous users and real-time
spectrum transactions with the ability to exchange data
between different entities remains a significant challenge.
On the other hand, applying a DSM model which employs
blockchain technology and CR to enhance the management
of the radio spectrum assets in 6G networks requires a
proper framework that facilitates the interoperability among
blockchain, CR, and spectrum assets in 6G networks.
To ensure scalability and performance in 6G spectrum management, many previous DSM-based blockchain methods
were designed in a way where blockchain integration with
external platforms and services is facilitated with the goal
of reducing the overhead caused by significant spectrum
resources [12], [13]. This integration is achieved in various
ways, including smart contracts and consensus protocols.
However, these integration methods do not consider an
interoperability framework which enables fast and uninterrupted spectrum service, as well as to facilitate seamless
cooperation and coexistence between PUs and SUs. This
requires blockchain protocols that can connect to external
data, ensuring minimal interference to PUs while maximizing
spectrum access for SUs, enabling effective spectrum sharing
and utilization. Overcoming these challenges will be crucial
to realizing the widespread implementation of DSM using
blockchain and CR, ultimately, leading to more scalable and
optimized spectrum utilization in wireless communication
systems.
III. CONTRIBUTIONS
Aiming to mitigate the scalability and interoperability
challenges in the context of DSM-based blockchain and CR
in 6G networks, a novel DSM framework is introduced in
this paper. Specifically, the DSM framework, named as BSM6G, uses a new interoperability technique which allows the
blockchain platform within BSM-6G to securely retrieve 6G
radio spectrum assets using a blockchain Oracle. In addition,
the interoperability technique ensures that the CR within
BSM-6G enriches the radio spectrum sensing data which,
on the other hand, contributes towards fast and accurate radio
spectrum management decisions. BSM-6G aims to provide
a cost-effective and less complex blockchain interoperability
technique where all massive spectrum sensing data will be
stored in an off-chain database. This means, the blockchain
platform will exclusively be used for automated and fast
decisions through making use of smart contracts.
To provide a scalable radio spectrum management system,
PoH consensus mechanism [14] is employed as a mechanism
to accommodate massive radio spectrum processes among
numerous users in 6G networks. Specifically, BSM-6G
employs PoH to boost the number of TPS, which leads to
faster decisions on radio spectrum assets. This remarkable
capacity aligns seamlessly with the data intensive demands of
6G networks, facilitating rapid and efficient decision-making
in spectrum allocation.
We summarise our contributions as follows:
• We propose a dynamic radio spectrum management
model, named as BSM-6G system, which preserves crucial spectrum management features: (i) Fast, accurate,
and dynamic radio spectrum management in the context
of 6G network through making use of an interoperability
mechanism that facilitates the interaction between
several platforms within BSM-6G which are blockchain,
Oracles, and CR; and (ii) scalable radio spectrum
management system where massive spectrum resources
in the context of 6G networks can be managed without
having any service performance degradation.
• We propose a comprehensive modular architecture for
blockchain Oracles integration with the blockchain
platform and the CR. The integration of Oracles aims to
facilitate off-chain data interaction adds a crucial dimension to the DSM system. The system gains flexibility and
real-world applicability by allowing secure retrieval and
modification of off-chain data. This enables connections
beyond the boundaries of the blockchain. Furthermore,
this paper offers comprehensive technical insights into
the implementation of the proposed integration of
blockchain and Oracles.
• We provide an in-depth exploration of the PoH consensus protocol as a potential mechanism for high
scalability, security, and low latency in BSM-6G. PoH is
considered as an alternative mechanism to the previously
investigated traditional consensus methods, aligning
with the demanding real-time requirements of spectrum
management in 6G networks.
Compared to existing work, the BSM-6G spectrum management system has several benefits, which we emphasize
here: (i) it supports low-cost and less complex interoperability
technique between DSM complex platforms; (ii) the system
scalability and security is supported by a new blockchain
design based on PoH consensus protocol; and (iii) the system
is verifiable by all parties.
IV. PAPER ORGANIZATION
The structure of this paper is outlined as follows: Section V
explores DSM techniques for enhanced spectrum utilization.
Section VI reviews related works and highlights contributions
to DSM in 6G networks using blockchain technology and CR.
Section VII introduces the proposed system model, whereas
Section VIII presents the system design, detailing the architecture’s key components, including blockchain modules,
CR modules, User Interface, and regulatory module interplay.
Section IX covers radio spectrum allocation and sharing in
the BSM-6G system, focusing on the interaction with the
dApp module and various processes across system modules.
Section X assesses Oracle interoperability by exploring
Oracle’s functionality and evaluating it through consensus
mechanisms. Section XI addresses scalability evaluation by
setting up a blockchain network, and quantifying transaction
processing capabilities. Section XII focuses on the evaluation
of spectrum resource utilization. Section XIII emphasizes
the security evaluation aspect of the blockchain system for
DSM, emphasizing its role as an immutable and open ledger
for spectrum transactions. Section XIV discusses research
challenges and opportunities to inspire future methodologies
for advancing DSM in wireless networks. Finally, Section XV
summarizes research contributions, achievements, and the
significance of the proposed blockchain-based DSM model.
V. BACKGROUND KNOWLEDGE
For many years, spectrum management followed traditional
static approaches [1], [15]. In this conventional system, specific frequency bands were assigned to particular services and
users for extended periods, resulting in limited flexibility [1].
The inherent inflexibility of static management approaches
proved to be a major drawback. As technology advances
and the demand for wireless services grew exponentially, the
static allocation of spectrum became increasingly inefficient,
scarce and hindered further development [15], [16].
A. DSM TECHNIQUES: ENHANCING SPECTRUM
MANAGEMENT
DSM techniques encompass a range of approaches, some of
them developed and used by CR, including spectrum sensing,
spectrum sharing, and spectrum access policies [1], [17].
Spectrum sensing involves the detection and identification
of available spectrum opportunities through techniques
like energy detection, cyclostationary feature detection,
or cooperative sensing [18]. Spectrum sharing techniques
enable the simultaneous use of spectrum by multiple users
or services, ensuring efficient coexistence and interference
management [16]. Spectrum access policies define the rules
and regulations for accessing and using spectrum resources,
including considerations of interference management, quality
of service, and fairness among users [17].
In the context of 6G networks, DSM plays a pivotal
role in addressing the spectrum scarcity challenges and
accommodating the diverse requirements of various wireless
services [11], [19]. CR techniques are often employed
in DSM, allowing intelligent spectrum sensing, decisionmaking, trading, and access [19]. By dynamically adapting to
the changing radio environment, CR-enabled DSM optimizes
spectrum utilization, minimizes interference, and enhances
the quality of service for different users and applications[11],
[20]. Looking ahead to 6G networks, DSM is expected to
become even more critical due to the anticipated exponential
growth in connected devices, data rates, and emerging
applications [4]. DSM approaches will be essential in
assuring effective spectrum allocation and access due to
the anticipated ultra-high data rates, ultra-low latency, and
widespread connection of 6G [4], [19].
B. SPECTRUM MANAGEMENT USING BLOCKCHAIN
AND CR
One of the most important books that encompasses the topics
of DSM, blockchain-based and CR-based DSM is the book
titled ‘‘Dynamic Spectrum Management: From Cognitive
Radio to blockchain and Artificial Intelligence’’ by [1]. This
book is a systematic overview of the technologies used
for DSM and focuses on the need for efficient spectrum
utilization. It emphasizes the shortcomings of traditional
static spectrum allocation and highlights the benefits of
DSA. The author, Y.-C. Liang, discusses the concepts of the
methods and theories to intelligently sense the spectrum, the
techniques to allow different communication systems on
the same frequency, called spectrum access, and discusses the
importance of new technologies for DSM such as blockchain
and Artificial Intelligence.
Addressing blockchain technology offers the potential
for decentralized, reliable, resilient and secure spectrum
management by providing a transparent and tamper resistant
ledger for recording spectrum transactions and ensuring trust
among users [1], [2]. On the other hand, CR can identify
underutilized or unused spectrum bands and opportunistically
access them without causing harmful interference to PUs,
who have primary rights to use those bands [1], [21].
Through comprehensive research and analysis, [1] sheds
light on the technologies for DSM. Y.-C. Liang mentions that
DSM enables more effective and flexible use of the scarce
radio frequency spectrum resources and ultimately supports
the rising demand for wireless communication services,
represents a paradigm shift in spectrum allocation and
utilization. It provides valuable insights into the complexities
of DSM and serves as a foundation for developing efficient
and flexible approaches to spectrum utilization, which will
serve as the basis for the system modelling.
C. REGULATORY LANDSCAPE FOR DSM USING
BLOCKCHAIN
Furthermore, regulations play a crucial role in governing
spectrum management practices in countries [2], [22], [23].
These regulations are designed to ensure efficient and
fair utilization of the limited spectrum resources while
also addressing various technical, economic, and policy
considerations. Several countries and research organizations
worldwide have undertaken projects to explore the potential
of DSM using blockchain and CR. Some notable examples
include:
In the United Kingdom, the Office of Communications
(Ofcom) has undertaken research projects that delve into
the fusion of blockchain and CR for DSM. Their efforts
centre around ensuring equitable and efficient spectrum
allocation [1], [24]. Likewise, within the European Union,
there has been active support for diverse research initiatives
and consortiums, including the 5G-EVE project. These
efforts span multiple member states and aim to explore the
potential of utilizing blockchain for DSM applications [25].
Alternatively, in the United States, the Federal Communications Commission (FCC) has taken proactive steps
by initiating projects and establishing test beds. These
endeavours are aimed at assessing the feasibility and efficacy
of DSM techniques, particularly in enhancing spectrum
utilization and addressing interference challenges [1], [2].
VI. RELATED WORK
This section presents a condensed overview of the relevant
related works that form the foundation of the BSM-6G. The
integration of blockchain and CR technologies within DSM
are explored for their potential applications, focusing on
emphasizing interoperability and scalability challenges.
A. CONVERGING TECHNOLOGIES IN DSM: BLOCKCHAIN
AND CR
Firstly, [15] conducted a comprehensive survey on
blockchain-based DSM in wireless networks, discussing its
potential for decentralized spectrum sharing and allocation.
The study suggests using blockchain for securely storing
spectrum management data and utilizing smart contracts to
establish secondary spectrum markets; this suggests a unified
strategy whereby spectrum sensing methods and geolocation
database technology may be utilized as additives to one
another for a more reliable DSM framework for our BSM6G model. Additionally, [16] presented a techno-economic
analysis of spectrum sharing using blockchain and smart
contracts, proposing a model for swapping access rights
within a well-known band and estimating usage costs, which
transaction fees will be a basis of comparison for the costs
associated with our system. Furthermore, [26] introduced
a multi-blockchain scheme for Dynamic Spectrum Sharing
(DSS) in the Citizens Broadband Radio Service (CBRS)
system, addressing scalability and interference issues through
a multi-blockchain architecture and cross-chain mechanism
that help to address the issues for our BSM-6G model.
It is also necessary to discuss smart contracts in the DSM
framework, which offer automated interactions in spectrum
markets. [23] investigated smart contracts for dynamic
spectrum marketplaces, proposing an approach for automated
spectrum transactions and marketplaces. Furthermore, [27]
proposed a smart contract-based approach for distributed
spectrum sensing, using a reputation-based incentive mechanism to improve spectrum sensing involvement. Both papers
on smart contracts present important characteristics such as
blockchain networks, programming languages, and model
flow, for the creation of an intelligent system with secure
and dynamic blockchain-user access for future 6G wireless
networks.
Additionally, within Distributed Ledger Technologies
(DLT), there are consensus mechanisms to ensure blockchain
validity. Reference [28] developed an interference-based
consensus mechanism for DSM, promoting spectrum sharing
and efficient transactions, by using this approach, detrimental interference brought on by spectrum merchants
can be avoided. Moreover, [29] explored the Practical
Byzantine Fault Tolerance (PBFT) consensus protocol
for high-frequency spectrum management in IoT systems, addressing scalability and non-cooperative competition
issues. Additionally, [30] proposed a Proof-of-Trust (PoT)
consensus mechanism for DSM in IoT networks, enhancing
cooperative sensing and trustworthiness [30]. These consensus mechanisms will facilitate a direct comparison with our
BSM-6G model.
A DSS using Hyperledger Fabric (HLF) was implemented
by [31], enabling cross-user trading of spectrum access
rights. Reference [32] proposed a blockchain verification
protocol for secure spectrum sharing in moving Cognitive
Radio Networks (CRNs). Furthermore, [18] developed a
blockchain-based security enhancement and spectrum sensing method for CRNs. The integration of DSS, spectrum
access tokenization, along with CR sensing and sharing
protocols, underscores its significance for the future of
spectrum trading and management.
When examining the spectrum management dynamics in
the blockchain-based DSM framework, it is essential to take
into account the methods and procedures that PUs and SUs
employ to establish transaction fees for the use of spectrum.
The market appeal and financial sustainability of spectrum
trading are significantly influenced by these costs. In order
to address this feature, our study explores a variety of
models and methods, referencing important studies in the
area.
An ideal non-cooperative game theory approach to spectrum management was developed by [33], in which the major
user or service provider sets the dynamic pricing for each
channel. Through the implementation of a bid-price system,
secondary users will be able to request spectrum access based
on their ability to pay; the highest bidders will be given
preference for channel access.
Reference [34] went into further detail about spectrum
pricing approaches and stressed the significance of taking
market and economic variables into account in addition to
technology aspects when setting prices for spectrum. They
put up a number of guidelines for spectrum pricing, including
distributing spectrum according to its best value, encouraging
adaptability in utilisation, and guaranteeing pricing equity.
Last but not least, [35] provided a thorough analysis of
pricing and economic models for resource management,
especially as they relate to 5G networks. Their classification
of economic models for user association, spectrum allocation,
and other resource management problems helped us better
grasp how the BSM-6G framework’s possible pricing mechanisms would work.
We explored various pricing models, including auctionbased, fixed, and dynamic pricing, and assess their impact on
the economic dynamics within DSM. This holistic approach
ensures that the model not only addresses the market demands
but also aligns with regulatory standards, ensuring viability
and compliance across different market scenarios.
B. B5G AND 6G: ADVANCING WITH DSM
The role of blockchain in 6G spectrum resource sharing and
allocation has been discussed and highlighted, has attracted
several recent research studies. In [36], the integration of
blockchain and 6G network spectrum sharing and resource
management is analysed and discussed in details, as well
as future research directions were provided. Furthermore,
[4] reviewed blockchain-enabled DSA and network slicing
for B5G and 6G, addressing challenges and trade-offs such
as ultra-high data rates, ultra-low latency, and widespread
connection of 6G. Moreover, [20] surveyed blockchain
integration with 5G networks, highlighting challenges and
opportunities for blockchain technology. Additionally, [19]
explored blockchain’s role in addressing challenges of
6G networks and identifying application opportunities like
virtual reality, holographic communications, and massive
machine type communications. These studies collectively
establish a robust foundation for a resilient, adaptable, and
forward-looking DSM framework.
In the context of 6G spectrum management using
blockchain, several models and techniques have been proposed with the aim of providing dynamic and secure spectrum
sharing and allocation. A blockchain-based spectrum allocation scheme for 6G communications was proposed by [3],
which employs blockchain to enhance trust among spectrum
operators within 6G networks. Specifically, the proposed
model gathers telecom operators, bidders, and government
regulates in a blockchain platform in which smart contract
are run among them as auctioneers. Given the 6G substantial
resources and demand, there is a serious concern arises in
relation to the scalability of this proposed model. On the
other hand, a new dynamic 6G spectrum management model
is proposed in [12] which integrates blockchain and hybrid
cloud services with the goal of building a public engagement
platform for IoT devices registration and management. This
model employs reinforcement learning for spectrum sharing
and management, including resource scheduling and classification. Similarly, a hybrid blockchain is utilised in DSM
in 6G, where spectrum resources of Ubiquitous IoT (UIoT)
devices can be subdivided into multiple dimensions with the
goal of enabling random and reliable access to massive UIoT
data [13]. Moreover, a DSM based multi-layer blockchain
architecture is proposed in [37] where IoT distributed devices
can engage with distributed local blockchains, aiming to
overcome the scalability challenge. However, blockchain
integration with IoT external platforms and services requires
an efficient and well-designed interoperability technique
which facilitates cost-effective and scalable integration.
Other studies have taken an alternative approach, focusing
on smart contract and consensus protocols to enhance the
performance and security of DSM. Reference [38] proposed
a blockchain-based framework for decentralized network
management in 6G mobile networks, including three types
of smart contracts are introduced. These smart contracts aim
to facilitate dynamic Mobile Network Operators (MNOs) for
end users. In the same context, a new consensus protocol,
named as proof-of-strategy, is proposed in [39] which is
integrated with the spectrum allocation process. According
to the proof-of-strategy consensus protocol, each node needs
to figure out the optimal strategy in an existing strategy group
with the goal of protecting the system in case of single point
of failure. However, these models add an extra overhead on
blockchain platform where massive 6G spectrum resources
which are used for the dynamic selection and allocation are
stored on the blockchain.
In summary, there have been several previous attempts
to address scalability, security, and performance challenges
of DSM using blockchain technology in 6G networks.
These attempts considered either integrating blockchain with
6G external platforms and services to enhance scalability
and trust, or designing new consensus protocols and smart
contracts to improve DSM performance and security. However, these attempts have not considered a cost-effective
interoperability technique when integrating blockchain with
external spectrum services. Furthermore, the Proof of History
(PoH) consensus protocol has not been considered as a
mechanism to overcome the scalability issue and enhance
overall DSM performance. Therefore, it is evident that there
is a room for improvement in the area of DSM-based
blockchain in 6G networks. Table 1 presents a compilation of
the related works that explore and propose models of DSM
within the context of B5G, and 6G networks.
VII. BLOCKCHAIN-BASED DSM FOR 6G NETWORKS
(BSM-6G)
Expanding on the thorough examination offered in the
previous section, it is clear that there are serious issues
with the combination of blockchain technology and 6G
DSM, especially regarding scalability and interoperability.
To satisfy the increased capacity demands of 6G resources,
the dynamic spectrum-based blockchain that is envisioned
for 6G requires efficient and rapid processes for blockchain
transaction verification and block formation. In addition,
a simpler and more affordable interoperability strategy
is desperately needed to enable smooth communication
between the spectrum blockchain, 6G network resources, and
cognitive sensing data.
Our study presents a novel Blockchain-based DSM model
called BSM-6G that is optimised for 6G networks, addressing
these issues head-on. By highlighting the contributions of
numerous academics in the industry and introducing a
revolutionary Oracle interoperability design that is carefully
engineered to enable effective integration between CR and
the blockchain platform, the BSM-6G model expands on
recent advancements in blockchain technology. This interface
allows 6G cognitive sensing data to be integrated onto the
blockchain platform, going beyond traditional paradigms.
Moreover, the Proof of History (PoH) consensus process,
an advanced technique intended to improve the blockchain
platform’s scalability, is incorporated into the BSM-6G
architecture. By using PoH, transactions are validated at the
best possible latency times, which promotes equitable and
effective spectrum sharing in the dynamic 6G environment.
The BSM-6G model gains a critical layer from this novel
consensus process, improving its ability to manage an
increasing number of devices and services.
In essence, the BSM-6G model is a ground-breaking
strategy that advances the capabilities of 6G spectrum
management by introducing a symbiotic interaction between
blockchain and CR technologies, in addition to addressing
the recognised issues of scalability and interoperability. The
combination of blockchain and CR technologies paves the
way for an all-encompassing and cutting-edge solution made
specifically to meet the demands of 6G networks.
A. MODEL OVERVIEW
The BSM-6G system has the following main components,
as pictured in Figure 1: Cognitive Radio, Blockchain module,
Regulators module, and dApp. The details of how these
components work are deferred until Section VIII.
• Cognitive Radio (CR) module: The CR module is
responsible for collecting the radio spectrum status
from the 6G networks and making them available in
databases.
• Blockchain module: an interoperability mechanism
(IM) is maintained in this module to allow interaction
and spectrum data exchange between Oracles and the
blockchain platform. More explanations on how the IM
works and the spectrum decision-making in blockchain
platform are deferred to Section VIII
• Regulator module: This component is responsible for
radio spectrum regulations in relation to radio spectrum
usage and sharing. This module has a direct contact with
the CR, where radio spectrum availability is finalised
based on the regulation and compliance data.
• End user interaction layer: This layer is a Decentralized Application (dApp). The dApp has a direct
interaction with the blockchain and CR modules, with
the goal of allowing SUs and PUs to securely access and
share the available radio spectrum.
In order to make sense of the process of sharing spectrum
resources between PUs and SUs, certain standards and
protocols must be established. This includes setting up an
open pricing system that is dependent on the availability of
spectrum and the state of the market. The price structure
may be fixed or dynamic. Moreover, it is imperative to
provide a comprehensive explanation of all transaction
processes, such as bidding, negotiation, and finalisation
of spectrum allocation. The dApp should automate these
processes to guarantee effectiveness and compliance with
legal requirements. Through the provision of an intuitive
interface, the dApp plays a crucial role in enabling PUs
and SUs to publish, bid, negotiate, and complete spectrum
resource transactions in a transparent and controlled manner.
By incorporating these detailed steps within the dApp, the
BSM-6G model ensures a clear and structured approach to
spectrum resource exchange, maintaining the integrity and
efficiency of the DSM system.
VIII. SYSTEM DESIGN
The following subsections explain each phase of the BSM-6G
protocol more in depth.
A. COGNITIVE RADIO (CR)
The CR module is a crucial part of the DSM system
for 6G networks. By offering capabilities for intelligent
decision-making, spectrum sensing, and allocation, this
module is essential for maximizing spectrum efficiency
and adaptability. The CR gives the system the ability to
allocate spectrum intelligently and dynamically because of
its innovative approaches like real-time spectrum detection
and Artificial Intelligence (AI) based algorithms. The CR
module provides efficient spectrum usage and improves
overall network performance in the complex and varied 6G
radio environment.
Advanced spectrum sensing methods, energy detection,
sequential energy detection, cyclostationary detection, and
cooperative sensing, are available in the CR Module. This
module is inspired by the CR module presented in [21].
It continuously scans various frequency bands for signals
while monitoring the radio environment. The CR learns about
the status of spectrum band availability and occupancies
using real-time spectrum sensing. It can identify transient
changes brought on by DSS arrangements and can detect
variations in spectrum availability caused by the presence
or absence of PUs. Additionally, the CR module uses
machine learning and AI algorithms to make wise spectrum
allocation choices. The CR can identify patterns, trends, and
correlations in spectrum occupancy, interference, and user
behaviour by examining historical and real-time spectrum
sensing data.
Furthermore, the CR follows rules and procedures to
reduce interference with other wireless devices and PUs of
the spectrum. The CR may cooperate with other devices to
maximize spectrum use while avoiding contention thanks to
cooperative spectrum sharing techniques as [40] described
in the paper. DSA enables the CR to flexibly access unused
frequency bands without interfering with the activities of
its PUs. Lastly, the CR module’s AI and Machine Learning
algorithms assist in locating and reducing interference
with PUs’ CRs and SUs’ CRs. To maximize spectrum
consumption, the module separates hazardous interference
from regular radio signals and works cooperatively with other
equipment.
B. BLOCKCHAIN MODULE
The proposed system’s Blockchain module is a key component in enabling scalable, safe, open, and decentralized
spectrum management for 6G networks. The consensus
mechanism and the Oracles make up its two primary
parts, each of which enhances the system’s scalability,
interoperability, and security.
Regarding the consensus mechanism, it is a crucial feature
of the Blockchain module that secures network participants’
agreement on the truthfulness of transactions and the status
of the blockchain ledger. The proposed model prominently
integrates PoH mechanism as a foundational element within
its framework. The innovative PoH consensus mechanism
was designed and developed by Anatoly Yakovenko, the
founder of Solana Labs [41]. Within the context of BSM6G, validators play a crucial role in ensuring the integrity and
accuracy of the blockchain. Validators are entities selected
based on their staked tokens, and they are responsible for
transaction processing and block validation. Their active
participation is fundamental to the functioning of the PoH
mechanism. In BSM-6G, validators are typically organizations or nodes that hold a stake in the network, usually in
the form of tokens specific to the blockchain platform being
used (such as SOL tokens in the case of Solana) [41]. These
validators are incentivized to perform effectively through the
prospect of earning rewards for high performance and facing
potential penalties for underperformance.
Block validation is achieved through PoH, which allows
validators to verify the sequence of events and the passage
of time without external timestamps. Validators follow
a rigorous process to validate a block, which includes
confirming the signature of a legitimate leader node and
ensuring the validity of all transactions by respecting the
rules of the protocol. Valid blocks are voted on by validators
and, once a large majority of votes is reached, the block is
confirmed and becomes part of the blockchain, where all
contained transactions are executed seamlessly.
The PoH consensus mechanism, tailored for DSM,
is meticulously designed to ensure precise event sequencing
within the blockchain while obviating the necessity for
external timestamps. Central to this mechanism is the
Verifiable Delay Function (VDF), a cryptographic tool
characterized by its time-intensive computation yet rapid
validation capability [14]. In routine network operations,
each node performs the VDF at intervals, resulting in a
distinctive time-stamped hash. This hash, appended to the
local blockchain copy along with the current time, represents
the outcome of the VDF calculation. Validators play a critical
role in the confirmation of valid blocks, and once a substantial
majority of votes is secured, the block is confirmed and
seamlessly integrated into the blockchain, triggering the
execution of all contained transactions [14]. Through the
consistent execution of the VDF on the previous block’s
hash and its comparison with the timestamp of the new
block, nodes confidently establish the validity of the block,
contributing to the robustness and reliability of our DSM
blockchain system.
For the BSM-6G model, the objective is to establish
a secure and reliable system, necessitating a diverse set
of entities to act as validators. These entities encompass
regulatory bodies, PUs, SUs, blockchain network nodes, and
community nodes. The aspiration is to achieve a robust and
decentralized system by encouraging an increased number of
active participants. The broader the engagement of members,
the higher the level of security and decentralization inherent
in the system. The adoption of PoH within the proposed DSM
system, BSM-6G, carries profound implications, generating
a strategic synergy that offers an array of invaluable
advantages. These benefits play a pivotal role in shaping
the system’s scalability and its adeptness at addressing the
intricate landscape of 6G networks.
Foremost among these advantages is the exceptional
throughput that PoH bestows upon the system. Empowered
by PoH, the system exhibits an unprecedented transaction
processing potential, in theory capable of reaching an
astonishing 710,000 TPS [41]. This remarkable capacity
aligns seamlessly with the data-intensive demands of 6G
networks, facilitating rapid and efficient decision-making in
spectrum allocation. Including the PoH mechanism in our
DSM system is a carefully thought-out decision that brings
numerous benefits. This combination makes the system
perfect at being superfast, using resources wisely, staying
safe, and responding quickly. As a result, it’s all set to make
a big difference in how the complex world of 6G networks is
managed.
Oracle blockchain interoperability is essential to the BSM6G system because it maintains scalability and reduces
complexity while facilitating smooth real-time communication between off-chain data sources and the blockchain
platform, Cognitive Radio (CR). Serving as an essential
conduit between the blockchain network and outside systems,
the Oracle component gives the blockchain access to current
data, enabling a flexible and adaptable spectrum management
environment.
Additionally, the Oracle uses the dApp to ease trade
exchanges. The Oracle makes sure that transactions made
by Primary Users (PU) or Secondary Users (SU) within
the dApp are automatically updated on the blockchain. This
helps to the accuracy and effectiveness of spectrum management inside the BSM-6G system, in addition to improving the transparency and traceability of spectrum trading
activities.
Through the utilisation of real-time data obtained from
the Oracles, the BSM-6G system’s blockchain network may
make well-informed, intelligent, and reliable decisions, thus
improving the overall precision and efficacy of spectrum
management procedures. In addition to ensuring the accuracy
of spectrum-related data, this combination of Oracle-based
blockchain interoperability helps to foster the dynamic
adaptation needed in a 6G environment that is changing
quickly.
The functionality of the Oracles is depicted in Algorithm 1,
providing essential data access between the blockchain
network and external data sources.
Algorithm 1 Oracles Component
1: procedure Spectrum_Availability_Oracle
2: Search Spectrum Availability database with
spectrum information
3: Include band details
4: end procedure
5: procedure dApp_Trading_Oracle
6: Facilitate trading between the blockchain network
and Spectrum Availability
7: Allow seamless transfer of information
8: Updates Spectrum Availability database
9: end procedure
C. REGULATORS MODULE
In the context of DSM, the BSM-6G framework’s Regulators
Module is crucial to guaranteeing smooth compliance with
6G regulatory norms. The rules and regulations controlling
spectrum utilisation that are prescribed by regulatory agencies are actively monitored and enforced by this module,
which is meticulously constructed to go beyond simple
observation. The Regulators Module’s complex functionality
includes a deep comprehension of 6G specification standards,
which allows it to operate through the complexities of
spectrum allocation in the developing 6G environment.
This module carefully analyses and considers the particular
details specified in 6G regulatory requirements to go deeper
into compliance. This entails a detailed analysis of usage
procedures, guidelines for spectrum distribution, and any
developing standards that specify what constitutes acceptable
spectrum transactions and deployments in the 6G spectrum.
The proactive approach of the module guarantees that all
aspects of spectrum utilisation in the BSM-6G system comply
strictly with the laws, hence reducing the possibility of any
deviations.
Moreover, the Regulators Module is made to be flexible
and open in recognition of the wide range of regulatory frameworks found in many nations. Any regulatory agency may
alter and customise it in accordance with their regulations,
covering every facet of DSM. Because of its flexibility, the
BSM-6G framework can be easily integrated with a wide
range of regulatory settings, considering local differences and
DSM rules. The system facilitates inclusion and collaboration
between regulatory authorities globally and the BSM-6G
framework by promoting an open and customisable approach.
This allows for a harmonious alignment with various regulatory landscapes. By achieving this, the BSM-6G system turns
into a flexible and globally applicable solution for efficient,
legal, and localised spectrum management in the context of
the global 6G paradigm.
D. DAPP
The functionality of the dApp is to serve as the user interface
and interaction layer for the overall system. It acts as a
bridge between the blockchain network and the end-users,
enabling them to access and interact with the blockchain’s
functionalities in a user-friendly manner, making the process
efficient, transparent, and secure.
The dApp facilitates various operations related to the
trading within the DSM system. Users can use the dApp
to perform tasks such as listing, and purchasing available
frequency bands, checking real-time spectrum information,
and monitoring their transactions on the blockchain.
IX. BSM-6G RADIO SPECTRUM ALLOCATION AND
SHARING
The BSM-6G system provides PUs and SUs an opportunity
to allocate and share available radio spectrum in 6G networks
throughout interacting with the dApp module, which is
considered as a frontend system. Upon interacting with the
dApp, several processes need to take place across all BSM6G system’s modules. The following steps, as shown in
Figure 2, describe the flow of processes and interaction within
the BSM-6G system to deal with PUs and SUs spectrum
allocation and sharing requests:
1) User Authentication: Users who wish to participate in
the DSM system must access the system through the
dApp. The dApp serves as the user interface, allowing
users to verify available frequency bands and interact
with the blockchain network seamlessly.
2) User Authorization: Upon authentication, the dApp
determines whether the user is a PU or a SU. Based
on this classification, the dApp grants appropriate
permissions. PUs are granted listing permissions,
allowing them to list their frequency bands for sale,
while SUs are granted purchase permissions, enabling
them to buy available frequency bands.
3) Regulatory Compliance Check: The Blockchain
communicates with the Regulations Database. This
database contains the latest spectrum regulations
and updates provided by regulatory authorities. The
blockchain verifies whether the user’s actions comply
with the applicable regulations.
4) Spectrum Availability Verification: The Blockchain,
through the Spectrum Availability Oracle, checks the
real-time spectrum availability in the dApp. This
information is previously updated by the CR, which
employs advanced spectrum sensing techniques to
monitor the radio environment and detect changes in
spectrum availability.
5) User Decision: Based on the real-time spectrum
availability displayed in the dApp, the user can make
one of two choices: (1) Use the spectrum if they
have already been authorized, proceeding to Spectrum
Allocation and Coordination, or (2) Engage in trading
activities, such as listing or purchasing frequency
bands.
6) Smart Contract Execution: If the user chooses to
engage in trading, the blockchain executes the corresponding smart contract. The smart contract stores the
transaction parameters on the blockchain and provides
access credentials to the dApp.
7) Spectrum Allocation and Coordination: The dApp
shares the access parameters with the CR, which
verifies the user’s access credentials to the spectrum.
If validated, the CR performs spectrum allocation and
coordination to assign the user their allocated spectrum, updating the real-time spectrum availability in
the dApp.
The access credentials for PUs and SUs can be granted
by the designated regulatory entity responsible for providing
such access. These credentials are directly provided to the
user’s wallet address, thus ensuring the system’s incorruptibility and security. The cycle continues until the user’s access
FIGURE 2. BSM-6G spectrum accessing and sharing. PUs are granted
listing permissions, allowing them to list their frequency bands for sale,
while SUs are granted purchase permissions, enabling them to buy
available frequency bands.
credentials expire or are no longer valid for spectrum usage.
In such cases, the user must repeat the trading process through
the dApp to obtain new access credentials. Furthermore, the
system must be regularly monitored. System administrators
can use monitoring tools to identify areas of improvement
and make necessary adjustments to reduce latency. Potential
bottlenecks can help in optimizing performance and latency.
In the subsequent two sections, an evaluation of Interoperability (Section X) and Scalability (Section XI) will be
conducted. For detailed information on the configurations,
a dedicated GitHub repository has been established and can
be accessed at https://github.com/davidcuellard/BSM-6G.
X. INTEROPERABILITY EVALUATION
This section presents the evaluation experiment, which aims
to verify the cost and feasibility of applying the BSM6G interoperability. The evaluation methodology involves
the development of a prototype system which represent the
BSM-6G. Specifically, the prototype is used to conduct
several experiments which focuses on measuring the time and
resource costs associated with the proposed interoperability
technique. The time cost will be depicted through the
distribution of time differences among different transaction
types, whereas the resource’s cost is measured by both
the Gas price, and the transaction fee. Comparing BSM6G with other DSM solutions based on time and cost
of spectrum operations is crucial to verify whether BSM6G is cost effective and scalable interoperability solution.
In comparison to existing spectrum management systems,
integrating DSM based blockchain with external services
(e.g. Oracle) often adds layers of complexity due to the
adopted interoperability techniques. This can sometimes
result in longer processing times and increased operational
costs, particularly during the initial setup phase or when
executing complex transactions. The interoperability evaluation aims to verify whether BSM-6G can offer cost-effective
operations measured by time and cost of these automated
transactions. In real-world applications, the implications of
these metrics can vary depending on the specific use case and
operational requirements. For instance, in scenarios where
real-time spectrum allocation is critical, longer processing
times associated with blockchain-based systems may be less
desirable.
On the other hand, the feasibility of BSM-6G’s interoperability is tested by developing the prototype system
which illustrates all relevant technical details of the proposed
interoperability implementation. Furthermore, this section
explores various aspects, including the experiment’s setup,
accompanied by its results, and a discussion that covers user
connectivity from the blockchain to off-chain data through
the utilization of an Oracle.
Extensive and multi-layered technical features and
methodology of the evaluation ensure a comprehensive
investigation of the cost-effective interoperability of the
BSM-6G model. The creation and implementation of a
prototype system that closely resembles the functional and
technical aspects of the BSM-6G model served as the
centrepiece of our evaluation procedure. This prototype
played a key role in carrying out controlled experiments,
which were essential in measuring the costs in terms of
resources and time related to the suggested interoperability
mechanism.
A careful examination of transaction durations was a key
component of our methodology in order to precisely estimate
the time expenses. This was accomplished by keeping track
of how long it took for different kinds of transactions to
finish, with a particular emphasis on the exchanges made
possible by the blockchain’s smart contract. Using the
BSM-6G framework, this approach enabled us to obtain a
comprehensive picture of the latency associated with various
transactional activities.
The gas price and transaction fee served as the two main
criteria that drove the resource cost analysis concurrently.
With the help of this two-pronged strategy, we were able to
comprehend the financial effects of carrying out transactions
inside the BSM-6G system as well as the effectiveness
of resource usage. Through analysing these expenses in
conjunction with transaction durations, we were able to
obtain a comprehensive comprehension of the financial and
functional effectiveness of our interoperability method.
Additionally, the prototype system, which was created to
accurately capture the technical nuances of our interoperability proposal, was used to test the practical feasibility of BSM6G interoperability. This evaluation component was essential
to confirm the practical applicability of our model and
ensure that the suggested technical solutions are theoretically
and practically sound. Included in the prototype was a full
description of the system’s features, such as the seamless
fusion of blockchain technology with off-chain data sources,
with an emphasis on the role of Oracles in filling this
gap.
A thorough knowledge of the interoperability of the BSM6G model was made possible by the findings and understandings obtained from this holistic evaluation technique. These
results validate the model’s promise as a reliable solution for
6G networks by proving its ability to provide efficient and
economical communication between blockchain platforms
and external data systems.
A. PROTOTYPE MODEL
Figure 3 illustrates the interoperability testing model, showcasing three primary entities: regulator, smart contract owner,
and user. It is postulated that the spectrum availability
database undergoes continuous updates facilitated by the CR
module through automated processes employing the technologies expounded upon in Section VIII-A. Simultaneous
activities occur between these entities, which contributes
to the comprehensive evaluation of interoperability. A brief
description of Figure 3 is as follows:
FIGURE 3. Interoperability: Testing model.
• Smart Contract Owner: undertakes the deployment of
the intelligent contract, equipped with the functions
named in Section X-B3. Additionally, the Smart Contract Owner is responsible for funding the smart contract
with LINK tokens and incorporating the addresses of
both PUs and SUs.
• Regulator: updates the Regulations Database, a pivotal trigger for band availability adjustments. This is
achieved by configuring the regulatory rules to enable
bands categorized as ‘‘Secondary’’ and relevant to
6G networks. This setup facilitates the activation of
39 distinct frequency bands, all encompassed within the
frequency spectrum spanning 7GHz to 24GHz.
• User: who may function as either a PU or SU, interacts
with the dApp and gains access to the comprehensive Spectrum Availability database, encompassing its
diverse properties. Upon identifying a suitable band,
the User can initiate interactions with the blockchain
through their digital wallet. The system verifies their
eligibility to either list or purchase a band. If the
requirements are met, trading can commence.
In instances where the prerequisites are not fulfilled,
the User can still attempt to proceed, but the smart
contract’s functionality prevents invalid transactions,
thereby conserving transaction fees. Upon triggering a
listing or purchase request, the blockchain establishes
communication with the Oracle Operator. This entity
subsequently retrieves off-chain data from the Spectrum
Availability database updated by the CR. The Oracle
Operator returns a response, as outlined in TABLE 2 and
TABLE 3.
Each of the 39 available bands will be tested. Firstly,
a category request, then the listing request, and finally the
purchasing request. In the testing process, a user initiates
a request to the Oracle, which then communicates with
the configured Chainlink Operator. This testing process
provided valuable insights into the system’s interoperability,
showcasing its ability to handle various transaction types and
interactions with the Oracle.
B. PROTOTYPE IMPLEMENTATION
The BSM-6G prototype system is implemented in this section
with the goal of highlighting the key technical implementation details of the proposed interoperability approach. The
exploration encompasses a range of crucial components:
1) DATABASES IMPLEMENTATION
1) Rest API endpoints:
a) Spectrum Availability: This endpoint enables the
display of bands that have been chosen for further
analysis.
b) Listing: This endpoint, employing the unique
identifier, state, and address associated with
the query, effects changes in the ‘‘bands.listed’’
attribute, thereby listing the specific band.
TABLE 2 presents different scenarios of listing
a band based on the combination of ‘‘To List’’
(whether the band should be listed), ‘‘Listed
State’’ (current listed state of the band), and
‘‘Purchased State’’ (current purchased state of
the band). The ‘‘Response’’ column provides the
corresponding response for each scenario.
TABLE 2. Listing scenarios.
c) Purchasing: Similarly to the listing endpoint,
the purchasing endpoint utilizes specific identifiers, state, and addresses to modify the
‘‘bands.purchased’’ and ‘‘bands.listed’’ attributes.
This process effectively facilitates the purchase of
the designated band.
TABLE 3 outlines various scenarios of purchasing a band based on the combination of
‘‘To Purchase’’ (whether the band should be
purchased), ‘‘Listed State’’ (current listed state
of the band), and ‘‘Purchased State’’ (current
purchased state of the band). The ‘‘Response’’
column provides the corresponding response for
each scenario.
TABLE 3. Purchasing scenarios.
2) Regulators Trigger Creation: To ensure regulatory
compliance, a trigger was established for the regulators’ rules. Changes in the states of these conditions
within the regulators’ rules database are automatically
reflected in the ‘‘bands.regulatorsPermission’’ attribute
for each respective band.
2) ORACLE IMPLEMENTATION
For the Oracle module, the Chainlink Foundation services
were employed, needing the setup of a custom node and
the creation of an ‘‘External Adapter’’ for interfacing with
off-chain data and executing queries endpoint.
1) Metamask: Metamask was utilized to make transactions and contract interactions.
2) Blockchain Network: In this context, SeopilaETH
was chosen due to its compatibility with Chainlink.
Consequently, it was also necessary to have LINK
tokens.
3) Running a Chainlink Node, to enable communication
between the smart contract and the Oracle. It was
necessary to set up an Ethereum client in Alchemy
(SeopilaETH) and run an Oracle Node.
4) External Adapter: To enable the communication
between the API and the Chainlink node using JSON
format.
5) Operator Jobs: These jobs initiate off-chain data
requests from the Spectrum Availability database.
3) SMART CONTRACT FUNCTIONALITIES
Using Remix IDE to create the smart contract, which forms
the backbone of the DSM system that interacts through the
Oracle.
a: TRANSACTIONS
• Set and Remove PUs and SUs: The smart contract
provides the functionality for the contract owner to set
and remove addresses for PUs and SUs. This feature
ensures that only authorized PUs have the ability to
list and purchase bands, while only authorized SUs can
purchase bands.
By managing these authorized addresses, the contract
owner maintains control over the participants who can
engage in the respective activities.
• Request Category of a Band (requestCat): Any user can
query the smart contract to obtain the category of a
specific band.
• Request Listing (requestListing) and request Purchase
(requestPurchase): Only authorized users are empowered to execute the listing and purchasing processes by
running these functions.
b: CALLS
• Check Authorized Addresses for Listing and Purchase.
• Get message Category (requestCat response).
• Get message Listing (requestListing response).
• Get message Purchasing (requestPurchasing response).
With the successful implementation of these smart contract
functionalities, the system is now poised for comprehensive
testing and a further discussion.
4) DECENTRALIZED APPLICATION (DAPP)
Figure 4 depicts a React-based application that was developed. The dApp was deployed using Netlify and can be
accessed at https://bsm-6g.netlify.app/
Within this interface, iframes containing charts generated
from MongoDB are displayed. These iframes have been
configured to refresh automatically every 30 seconds. The
application showcases three distinct charts, each serving a
specific purpose:
• Spectrum Availability Table: Presents a table detailing
the Spectrum Availability. Users have the option to sort
the table based on their preferred column, allowing for
easy access to relevant information.
• Pie Chart of Band Availability: Provides an illustrative
representation of available and unavailable bands. This
visual representation offers quick insights into the
distribution of bands within the spectrum.
• Regulators Rules Table: Displays the status of various
regulatory rules. This information serves to verify which
rules are currently active and which ones are not,
providing a comprehensive overview of the regulatory
landscape.
Furthermore, a button to request a category and establish
a connection to the Metamask wallet was included. Because
the Operator Node is local, a response can only be received
if it is active; if not, the request will be sent out, but no
answer will be received. These charts, embedded within
the React application, offer a dynamic and user-friendly
interface that facilitates the visualization and understanding
of critical information related to spectrum availability, band
status, and regulatory rules. The automatic refresh of the
charts enhances the usability and real-time relevance of the
application, ensuring users are equipped with up-to-date
insights for informed decision-making.
C. RESULTS AND DISCUSSIONS
While the evaluation methodology primarily aimed at
validating the technical implementation of the proposed
interoperability design as well as testing the off-chain data
retrieval and successful interaction, it also encompassed an
in-depth analysis of critical parameters such as time, gas
price, and transaction fee. This analysis is achieved by a
series of controlled experiment scenarios using the developed
testing model.
1) TIME ANALYSIS
To assess the response time, capturing the duration from
contract interaction approval in Metamask to result appearance, crucial data from each interaction was collected. Two
significant aspects were tracked for each interaction:
1) The Timestamp was taken from the Block Explorer at
https://sepolia.etherscan.io/.
2) Using the Operator GUI transaction’s timestamp.
Figure 5 depicts the distribution of time differences across
various transaction types. Additionally, Table 4 presents the
relevant statistics for time difference. The average total time
was observed to be 31.40 seconds. It’s worth noting that
extended durations were encountered, reaching up to 63.617,
50.660, and 51.522 seconds for requestCat, requestListing,
and requestPurchasing, respectively. Conversely, minimum
times of approximately 25.5 seconds were noted for each
transaction type.
TABLE 4. Summary statistics for time difference.
This analysis highlights the transaction response times that
were observed. The results show relatively similar response
times across various transaction types, where RequestListing
and requestPurchasing show the highest response times.
2) GAS PRICE ANALYSIS
The evaluation of interoperability in the context of DSM
for 6G networks also encompassed an analysis of gas
fees incurred during various transaction types within the
blockchain-based system. Gas fees, denoted in Gwei (1 Gwei
is 10−9 ETH), represent the amount of cryptocurrency users
need to pay to miners to process and include their transactions
in a block.
To ascertain the gas prices, the transactions were verified
using https://sepolia.etherscan.io/. As gas prices are dynamic
and can vary based on factors such as transaction complexity,
pending transactions on the blockchain, and time of day,
FIGURE 6. Interoperability: Gas fees distribution across transaction types.
the analysis considered a range of gas prices over the
testing period. The results, displayed in Figure 6, depict the
distribution of gas fees across transaction types, while Table 5
provides summary statistics for gas prices.
The observed gas fees exhibited a relatively narrow range,
spanning from 2.810 to 4.217, with a total average of 3.18.
Notably, the transaction type requestPurchasing incurred
the highest gas fees. This could be attributed to the larger
response size required when the Chainlink Operator adjusts
both ‘‘listed’’ and ‘‘purchased’’ values. The highest gas fee
recorded was almost twice the lowest observed gas fee,
suggesting the greater computational requirements of the
requestPurchasing transaction type. Conversely, requestListing transactions showed consistent gas fee values with a
minimal standard deviation of 0.034.
3) TRANSACTION FEE ANALYSIS
The transaction fee directly correlates with the gas price, as it
is calculated as the product of gas price and gas used by the
transaction. This fee is paid by the user to the blockchain in
exchange for executing the contract interaction.
In Figure 7, the Time Difference Distribution Across
Transaction Types is illustrated, and in Table 6, Summary
Statistics for Transaction Fees are provided.
FIGURE 7. Interoperability: Transaction fees distribution across
transaction types.
The results for different transaction types vary between
0.0008 and 0.0005, with an overall average of 0.000610.
Further dissection of the data reveals the minimum and
maximum transaction fee values, shedding light on the range
TABLE 6. Summary statistics for Tx fees.
of fees users might encounter for each transaction type.
Remarkably, ‘‘requestCat’’ emerges with the lowest minimum transaction fee at 0.000520 SepoilaETH, portraying the
cost efficiency associated with obtaining information about
band categories. In contrast, ‘‘requestPurchasing’’ boasts the
highest maximum transaction fee at 0.000823 SepoilaETH,
hinting at potential scenarios where the acquisition cost for
purchasing a band can be relatively higher.
Among the transaction types, it is notable that ‘‘requestPurchasing’’ demonstrates the highest mean transaction
fee, amounting to 0.000677 SepoilaETH. Conversely, the
transaction type ‘‘requestCat’’ exhibits the lowest mean
transaction fee, measured at 0.000562 SepoilaETH, implying
a relatively lower cost associated with acquiring information
about the category of a particular band. In summary, related
to Gas and transaction fees, it can be deducted that these
costs are realistic as it is attributed to the selected blockchain
network (Ethereum) and the smart contract type and the
connection with the Oracle.
XI. SCALABILITY EVALUATION
The evaluation of scalability stands as a critical endeavour
to thoroughly scrutinize the efficiency and suitability of
the consensus mechanism inherent to the proposed system
model. In this context, PoH consensus mechanism takes
centre stage, with its theoretical capacity of 710,000 TPS
warranting empirical validation within the context of our
DSM for 6G. This assessment is of paramount importance
as it delves into how the consensus mechanism performs
under augmented workloads while upholding its operational
efficiency. The process encompasses meticulous system
setup and strategic tool selection, ensuring a comprehensive
examination of the system’s scalability capabilities.
Turbine block propagation, an advanced implementation
technique, is a crucial component of our scalability evaluation [42]. By dividing transaction batches until the bandwidth
used by header information surpasses that of the transaction
data itself, this technique greatly improves scalability. Scalability can be extended to potentially hundreds of thousands
of validators by utilising this strategy. By ensuring that every
participating node adopts the same methodology as the leader
node, this strategy effectively addresses scalability on a far
wider scale than that of typical blockchain systems.
The scalability evaluation was based on a rigorous
experiment model in terms of methodology. In order to
replicate real-world DSM transactions, the experiment started
500,000 smart contract interactions, simulating a high volume
of transactions. This particular scenario was created with the
express purpose of simulating how off-chain data is retrieved
and interacted with, much as it would be in actual DSM
interactions involving the Spectrum Availability database.
Because there were so many transactions, the system was put
through a rigorous stress test, which let us see how well the
PoH consensus mechanism performed under heavy strain.
Numerous preliminary procedures were carefully followed
in order to guarantee the accuracy of this scalability
study. These included creating keypairs for account access,
coordinating batches of transactions, and making sure there
were enough resources for these keypairs by utilising funders
with SOL tokens from faucets. One important aspect of
data gathering was the ‘Start Sampling’ transaction, which
was started every second by the client demo. Together,
these efforts produced a simulation that successfully reflected
the spectrum allocation requirements of a 6G network,
offering an accurate and thorough evaluation of the system’s
scalability.
A customised configuration of the Solana cluster, selected
for its high-performance and quick transaction processing
capabilities, added assistance to the experiment’s implementation. In this configuration, a validator node was launched,
a test environment was initialised, and regular expressions
were used for data extraction and cleaning. Because of this
careful methodology, the average TPS for all samplers could
be computed, providing a useful overview of the system’s
overall transaction processing effectiveness.
Our scalability examination was distinguished by a
thorough and multifaceted methodology that included both
realistic simulations and theoretical approaches. We conducted a thorough test of the PoH consensus process by
using sophisticated propagation techniques and simulating
a large volume of transactions. This thorough approach
guaranteed a solid evaluation of the suggested BSM-6G
model’s scalability, which is essential for its use in the
demanding and dynamic world of 6G DSM.
A. EXPERIMENT MODEL
As depicted in Figure 8, the benchmarking process commences by the client demo initiating an extensive influx of
500,000 transactions (smart contract interactions) to the local
testnet validator. This strategic approach essentially treats
these transactions as implicit contract interactions with the
Oracle, intended to replicate the process of retrieving and
engaging with off-chain data. To contextualize this scenario
within our proposed DSM framework for 6G networks, these
interactions would closely resemble the mechanisms involved
in accessing and interacting with the Spectrum Availability
database.
For the effective execution of this benchmarking, several
preparatory steps are undertaken. Firstly, the client demo
orchestrates the creation of transaction batches, adhering
to the predefined transaction count. This transaction count
determines the number of transactions grouped within
each batch, facilitating streamlined processing. Furthermore,
FIGURE 8. Scalability: testing model.
keypairs, each comprising a public key and its corresponding
private key for account access, are generated in multiples
of the transaction count. These keypairs are integral for
accessing the system’s various functionalities.
To ensure the operational capacity of these keypairs,
the validator node initiates funding requests to the funder
using faucet SOL tokens. The funder supplies the necessary
resources for these keypairs, enabling their seamless integration into the benchmarking process. Once funded, the
benchmarking process advances to the subsequent phase,
where the client demo commences the ‘‘Start Sampling’’
transaction every one second. This transaction type plays
a pivotal role in gathering the required benchmarking data.
Through the combination of these orchestrated steps, the
benchmarking process effectively simulates and evaluates
the system’s responsiveness and performance under varying
transaction loads, providing valuable insights into the scalability of the proposed DSM framework for 6G networks.
B. EXPERIMENT IMPLEMENTATION
The chosen blockchain platform for this study is Solana,
a high-performance blockchain known for its scalability and
fast transaction processing capabilities, which uses PoH as its
consensus mechanism.
For the experiment, it was necessary to configure the
Solana cluster as follows:
1) Set up a Solana Cluster and configure it in local
2) Initialize Test
a) Start the faucet service.
b) Launch a validator node.
c) Initialize Benchmarking Test
d) Run the test with different number of transaction
counts (tx count) to send per batch.
3) Data Extraction and Cleaning: To extract the relevant
data, regular expressions were employed to go through
the text and isolate the TPS values associated with each
sampler.
4) Calculating the average TPS across all samplers and
the overall efficiency of the system’s transaction
processing capacity. Additionally, the total number of
transactions processed and the count of failed samplers
were derived from the extracted data.
C. RESULTS AND DISCUSSIONS
1) TRANSACTIONS PER SECOND (TPS) ANALYSIS
In Figure 9, the benchmarking results of the cluster are
displayed, showcasing various tx count. An interesting
observation is that lower tx counts tend to exhibit fewer
sampler failures. This phenomenon can be attributed to the
nature of the testing environment. Specifically, during the
benchmarking process, the tx count values of 50, 500, 1,000,
and 3,000 were utilized to gauge the local node’s response to
the load.
FIGURE 9. Scalability: TPS Distribution over samplers – Cluster
benchmarking.
TABLE 7. Summary statistics for different tx count.
Solana’s claim of achieving up to 710,000 TPS is
noteworthy [41]. However, it’s essential to highlight that
real-world results have shown slightly different figures.
In BSM-6G based Solana blockchain has demonstrated a
peak TPS of just over 5,000, while during testing, it reached
up to 65,000 TPS [43]. Within the testing, Table 7 shows
the benchmarking principal statistics, a compelling result was
achieved where 49,720 TPS was sent with a tx count of 3,000.
It’s worth noting that this specific scenario had the highest
sampler failures, totalling 33.
Interestingly, the scenario with the fewest sampler failures was observed at a tx count of 50, registering zero
failures. Nevertheless, its minimum and maximum TPS
were 19,249.41 and 23,601.18 respectively. This outcome
remains impressive when compared to the capabilities of
other prominent blockchain networks. For instance, Bitcoin,
Ethereum, Ripple, and Avalanche networks typically handle
3-7, 15-25, 1,500, and 5,000 TPS, respectively [44].
Table 8 presents a comparison of the mechanisms proposed
by various authors in Section VI. It is evident that even
though PoF and PBFT achieve up to 10,000 TPS, this
number falls short of both our PoH test result of 49,720
TPS and the theoretical ceiling of 710,000 TPS. Furthermore,
it’s important to note that PBFT’s fault tolerance is 33%,
indicating lower security. Additionally, PoT boasts a TPS of
100,000, which is impressive, yet lacks information regarding
its fault tolerance and doesn’t surpass the 710,000 TPS
offered by PoH.
TABLE 8. TPS comparison.
In Figure 9 the overall average was 22,882.90. The
substantial TPS demonstrated by BSM-6G based Solana
positions it as a viable candidate for a scalable DSM system.
The blockchain network’s capacity to handle a significant
number of transactions within a short timeframe aligns well
with the demands of DSM. Swift transaction processing is a
fundamental requirement in managing the dynamic allocation
of spectrum resources efficiently.
It was noted that up to 3,000, the local node managed
the benchmarking tasks effectively. Beyond this threshold,
however, the local node’s performance began to deteriorate.
This degradation in performance beyond 3,000 transactions
can be attributed to the increased strain on system resources,
leading to slower processing speeds and potential bottlenecks
that hindered the node’s ability to handle the high transaction
load efficiently.
Additionally, it’s worth mentioning that BSM-6G based
Solana has demonstrated remarkable scalability in terms
of TPS. Furthermore, these testing outcomes contribute
significantly to the DSM initiative. The high TPS achievable
with BSM-6G based Solana implies that complex DSM
operations can be executed rapidly. For instance, in spectrum management tasks involving real-time decision-making
and allocation adjustments, the network’s responsiveness
becomes a critical factor.
2) TRANSACTION FEES ANALYSIS
Transaction fees represent the nominal charges imposed
to process instructions within the Solana blockchain network [14]. With each transaction potentially containing multiple instructions, the process involves routing the transaction
through the current leader validation-client. Once confirmed
and integrated into the global state, the corresponding
transaction fee is paid to the network. This fee structure
functions to uphold the Solana blockchain’s economical
design.
In Figure 10, the transaction fees are displayed. Within the
specific case being considered, the validator node initiated
requests to the funder, aligning with distinct tx counts:
50, 500, 1,000, and 3,000; These requests resulted in the
validator imposing transaction fees amounting to 1,366.21,
5,465.87, 2,1864.48, and 87,458.95, respectively, to facilitate
the execution of the complete benchmarking process.
Transaction fees serve as a mechanism for preserving
the network’s integrity. By attaching fees to transactions,
the network guards against potential misuse and spam,
ensuring optimal resource utilization. This aligns with DSM
operations, where efficient resource allocation is vital for
effective spectrum utilization.
It’s important to recognise that transaction fees not only
improve general efficiency and discourage misuse, but they
also contribute to the network’s sustainability. These fees
serve as a safeguard against unfair usage and support system
stability in situations where transactions are frequent or
intense. In the context of DSM, transaction fees play a crucial
role in encouraging responsible usage, especially in situations
where high-frequency real-time modifications are necessary
to meet dynamic spectrum demands.
The system’s ability to adapt to different transaction sizes
and meet a range of operational needs is demonstrated by
the observed linear increase in transaction fees. The tiered
structure of transaction fees gives users a way to make
decisions based on their individual needs as the system
changes and adapts. In addition to promoting a just and
flexible environment and assisting in the sustainability of the
BSM-6G system, this dynamic pricing model makes sure that
the network is resilient and effective even in situations where
demand is high.
While transaction fees foster network sustainability, they
entail associated costs for participants. In scenarios involving
frequent or intensive transactions, these costs can accumulate.
In the context of DSM, particularly if operations necessitate a
high frequency of real-time adjustments, the cumulative cost
factor warrants consideration.
In summary, the benchmarking results provide a significant
insight into the scalability potential of the BSM-6G based
PoH consensus mechanism, particularly within the realm
of DSM. The network’s exceptional throughput capabilities,
as demonstrated in the benchmarking process, are notably
relevant to the real-time spectrum allocation requirements
of next-generation communication networks such as 6G.
The inherent scalability of PoH mechanism positions it as
a promising candidate for supporting a more efficient and
effective DSM system.
This mechanism’s ability to handle a substantial number
of transactions within a short time frame aligns well with
the dynamic nature of spectrum management in rapidly
evolving communication environments. As the demands for
real-time decision-making and resource allocation intensify
in 6G networks, the benchmarking outcomes highlight the
significance of adopting a consensus mechanism that can
accommodate the high transaction volumes required for
optimal DSM operations.
XII. EVALUATION OF RESOURCE UTILIZATION
The evaluation of spectrum utilisation and cost is carried
out in this section. Stackelberg game scenario is considered
while calculating the payoffs and cost, following the strategy
adopted in [45] and [46]. Specifically, the payoffs of the
spectrum buyer are calculated based on the identification
of optimal resource allocation through making use of two
factors, utility performance of the buyer, and the payment
of the purchased resource. On the other hand, the seller
payoffs are defined based on the price of the spectrum
resources requested by the buyers. According to Stackelberg
game, the spectrum network elects a leader which is the
regulator in Stackelberg game, making decisions on how
to allocate or utilize spectrum resources. The other players,
often secondary users or spectrum licensees, then make their
decisions based on the leader’s actions. The leader is elected
based on a reputation mechanism proposed in [47]. Precisely,
the reputation scheme is run independently by all spectrum
followers to finalise the reputation score for each spectrum
leader candidate at the end of every epoch. The reputation
score is calculated based on several reputation parameters
such as number of transactions, and reputation scaling factor.
A. EXPERIMENT IMPLEMENTATION
In this section, simulations were carried out to evaluate the
performance of the system of the Stackelberg game in terms
of payoffs (demand relationship between the buyer and seller)
and spectrum resource cost. The simulation network was
implemented following the simulator design proposed in [48]
and [49]. Specifically, the simulation model is developed
in Python for object-oriented structure and modularity.
Based on the concept of discrete event simulation, the
behavior of the spectrum buyer and seller is modeled as
an ordered sequence of well-defined events. These events,
which take place at discrete points in simulation time,
comprise a specific change in the system’s state. Regarding
the blockchain system, Solana blockchain is employed in
the simulation configuration. We set the coverage area to
500 meters, 10 mobile virtual network operators (MNVOs)
with 450 users randomly distributed. Random user mobility
model is adopted to capture the spectrum user mobility [50].
We set the simulation to have 1000 trading epochs. A trading
epoch is the time where spectrum resources are requested by
spectrum users.
B. RESULTS AND DISCUSSIONS
Figure 11 shows the total payoff for the buyers and sellers
over a varying number of trading epochs. The trading epoch
represents the time where buyers requests spectrum resources
and a level of interactions is initiated between the buyers
and sellers. Results indicate that the our proposed system
achieves higher payoffs compared to the HDFLNS-BC [45].
This means that BSM-6G achieves higher level of interactions
FIGURE 11. Comparison of the empirical distribution of payoffs
measured in the BSM-6G with the empirical distribution of payoffs
measured for the HDFLNS-BC protocol.
where the number of transaction handled per epoch is
significantly improved. The reason behind this improvement
is the fact that BSM-6G uses PoH consensus protocol which
facilitates a significant volume of transactions, allowing
for the optimization of payoff functions to enhance overall
performance.
On the other hand, Figure 12 shows the average cost across
each trading epoch. The results indicate two main findings:
1) cost resources in BSM-6G increase gradually as the
number of epochs increases; 2) BSM-6G provides fewer cost
resources compared to HDFLNS-BC. The price of spectrum
resources is crucial as it has a great impact on the level of
payoffs. Specifically, a low spectrum price encourages buyers
to request more resources, which leads to higher payoffs. This
means BSM-6G improves spectrum trading by providing a
low cost of resources, which contributes towards enhancing
payoff functions.
FIGURE 12. Comparison of the empirical distribution of average cost
measured in the BSM-6G with the empirical distribution of average cost
measured for the HDFLNS-BC protocol.
XIII. SECURITY EVALUATION
The blockchain system for DSM is essential to keeping
an immutable and open ledger of spectrum transactions.
All network transactions involving spectrum are tracked
by the blockchain, which functions as a digital ledger.
Each transaction made by users when using the dApp is
cryptographically recorded as a block in the blockchain.
The parties involved, the particular spectrum band, the
parameters of the transaction, and other pertinent information
are all included in these transactions. The system enforces
stringent access control mechanisms, ensuring that only
authorized addresses have the privilege to initiate listing or
purchase actions. This restriction adds a layer of security,
mitigating the risk of unauthorized manipulation of the
system’s spectrum availability data. The owner of the system
retains the exclusive capability to designate and modify
authorized addresses, thus preserving the integrity of the
system’s operations.
To further enhance security, a proactive approach was
adopted by creating distinct Operator’s jobs for each individual user. This stratified approach minimizes the scope
of access, ensuring that only users with specific authorized
addresses can utilize their designated jobs. By segregating
jobs in this manner, the system safeguards against potential
data breaches or unauthorized interactions with the off-chain
data, thereby fortifying the overall security posture.
Furthermore, the blockchain’s consensus mechanism,
driven by PoH, ensures the integrity and security of each
transaction before its inclusion in the blockchain. With PoH,
the system cryptographically verifies the passage of time
between events, providing a tamper-proof historical record.
This robust verification process ensures that transactions
are valid and legitimate, bolstering the overall security
of the network. The sequential execution of cryptographic
functions guarantees that events occur in the intended order
and cannot be manipulated, thereby preventing unauthorized
modifications and ensuring the reliability of the Blockchain.
Due to the transparency of the blockchain, an open and
auditable system is provided by allowing all network users
to access and observe the whole transaction history. Users
can track the movement of spectrum resources, ensuring that
band usage and distribution are fair and legal. The integrity
and immutability of records, along with this transparency,
help to foster a sense of confidence among network
users.
PUs and SUs can trade spectrum with confidence, knowing
that every transaction is securely documented and cannot
be altered. In addition, the PUs receive incentives (tokens)
to enable unused band spaces, expanding the use of the
spectrum to the interested SUs. The blockchain’s elimination
of middlemen increases trust and lowers transaction costs.
The blockchain module, which keeps an unchangeable log
of spectrum transactions, is the foundation of the DSM
system. The blockchain fosters confidence among users of
6G networks and makes efficient and dependable spectrum
trade possible by guaranteeing the integrity, transparency, and
security of records.
XIV. RESEARCH CHALLENGES AND OPPORTUNITIES
This paper opens up new possibilities for research and
development in the field of DSM in the context of changing
6G networks. While the current work provides valuable
insights and contributions, there are several challenges and
limitations that warrant exploration and refinement in future
studies.
• Enhancing Oracle Automation: One avenue for future
work involves the optimization of the Oracle’s automation process. This could involve the development of
a mechanism that periodically updates the state of
purchased bands, thereby revoking access and ensuring
timely and accurate data representation.
• Refined Band Listing and Purchase Mechanism: The
existing approach facilitates the listing and purchase of
entire frequency bands. To further enhance spectrum
utilization and accommodate a larger number of users,
future work could involve the design of a system
that subdivides frequency bands into smaller portions,
allowing for the sale and usage of specific segments
of a band. This approach could potentially increase the
efficiency of resource allocation.
• Development of a Custom Blockchain Network: Exploring the creation of a dedicated blockchain network
utilizing the PoH consensus mechanism presents an
interesting avenue for future research. This custom
blockchain could incorporate its Oracle system for
off-chain data retrieval and interaction, potentially leading to even more optimized and tailored performance for
DSM within advanced networks.
XV. CONCLUSION
We proposed a DSM system based on blockchain and CR,
called BSM-6G. The primary advantage of this system is
that it preserves scalability and cost-effective, as well as
less complex blockchain interoperability in the context of
6G spectrum management. It achieves this by using oracle
blockchain interoperability to ensure the real-time interaction
among the blockchain platform, the CR, and any data
sources off-chain, and to preserve blockchain scalability.
An additional feature of BSM-6G is that it uses Proof of
History (PoH) consensus protocol to support faster spectrum
decisions, meeting the significant resources and demands in
the 6G networks. In this paper, the blockchain interoperability
within BSM-6G was implemented where comprehensive
technical details were provided and discussed with the goal
of testing the level of complexity of the proposed Oracle
interoperability design. To demonstrate that the provision
of these features is achieved by BSM-6G, we provided a
detailed evaluation and analysis of BSM-6G to establish how
it preserves cost-effective interoperability and scalability.
Empirical evidence of the performance characteristics of
BSM-6G was then provided. We evaluated its performance
on a prototype system, by measuring the time and cost
of spectrum operations, in particular the time and cost
required for the Request Category of a Band, Request Listing
(requestListing) and request Purchase (requestPurchase).
In summary, the average time required by BSM-6G to
perform spectrum operations (Request Category, list and
purchase a Band) was 31.40 s and the associated average
cost of gas was 3.18 for each contract. The scalability
of the system was then investigated by examining the
number of transactions that BSM-6G can process per second
(TPS) as well as the average transactions fees as the
transactions size increased. We provided evidence that the
transaction fees were an approximately linear function of
the transactions’ population size over the range of population
sizes examined. In summation, BSM-6G delivers the following key features: cost-effective and less complex Oracle
interoperability, and initial results suggest that the system is
scalable.