Title: Unlocking the Potential of Interconnected Blockchains: A Comprehensive Study of Cosmos Blockchain Interoperability

ABSTRACT The Cosmos blockchain is a decentralized network of independent blockchains that addresses
scalability and interoperability difficulties in blockchain architecture. Through the use of the Tendermint
consensus mechanism and the Inter-Blockchain Communication (IBC) protocol, the Cosmos blockchain
enables transactions that are both safe and smooth across a variety of blockchain platforms. One of the
most important aspects of its design is the Atom token, which is responsible for ensuring the safety
and governance of the network and, as a result, improving interactions across different chains. This
comprehensive study covers various topics, including analyzing the techniques that facilitate communication
between different blockchain systems. Exploring the subtleties of Cosmos blockchain’ architecture and
assessing the usefulness and efficiency of the system through a review of transaction data and Atom token
volume in the cryptocurrency market. The results contribute to the discussion on blockchain interconnectivity
by highlighting the Cosmos blockchain’s potential to revolutionize engagement with distributed ledger
technologies. The study also emphasizes the Cosmos blockchain’s strategic importance in developing
blockchain ecosystems and their impact on digital commerce and governance.
INDEX TERMS Blockchain, validators, ledgers, interoperability, cross-chains, inter-chain communication,
internet of chains, tendermint, cosmos blockchain.
I. INTRODUCTION
The landscape for blockchain is an ever-evolving region
with innovations happening in real-time. Several solutions
are being created to cater to specific challenges faced by
blockchain. Where a chain is particularly focused on a singleton application, improving its performance and maintaining
its components is a separate task in itself [1]. A step further
on this, one of the key areas that today’s businesses and
developers are actively trying to unravel is how different
blockchains can interact and pass information from one kind
of data domain to another [2], [3]. This is a challenging
area regarding blockchain since the entire concept of the
ledger was to limit how data can be altered as little as
possible. Therefore, this pursuit of interconnectivity presents
an interesting problem to solve. With its unique features,
the Cosmos blockchain [4] stands at the forefront of this
endeavor. This research paper aims to explore the intricacies
of the Cosmos blockchain’s interoperability, examining its
main features, architectural design, and role in addressing
the pressing need for an inter-operable blockchain ecosystem,
commonly referred to as an inter-chain [5]. Byzantine Fault
Tolerant (BFT) consensus algorithm [6] to its innovative
Inter-Blockchain Communication (IBC) protocol, we will
explore how Cosmos blockchain has engineered a robust
foundation for interconnectivity. To assist in reading, we have
included a list of acronyms used throughout this paper in
Table 1.
One of the earliest proposals for inter-blockchain communication was made by Jae Kwon in 2014, who introduced the
concept of Cosmos blockchain, an “Internet of Blockchains”
that would allow heterogeneous chains to interoperate using
a hub-and-spoke model [4]. The Inter-Blockchain Communication Protocol (IBC) was later developed as an open-source
protocol for relaying messages between separate distributed
ledgers, which could support a variety of network topologies
and applications [7]. IBC was launched in March 2021,
enabled on 22 networks as of November 2021, and reached
107 networks by the end of 2023 with more than 2 million
monthly active users [8]. With this expanding landscape, the
need for interoperability becomes increasingly apparent. The
second section of our analysis will explore the fundamental
requirement for an interoperable blockchain, shedding light
on the challenges posed by isolated networks and the potential
benefits a well-connected blockchain ecosystem can bring.
To better understand the inner workings of the Cosmos
blockchain, the next section of this paper will conduct a
thorough review of its architecture. Figure 1 shows various
FIGURE 1. Infrastructure of interoperable Cosmos blockchain.
Cosmos blockchain-based infrastructures connecting key
operational areas such as transport, inventory, energy, and
customer support through a central hub. It integrates security,
payments, data, and analytics chains to provide a selfsufficient, decentralized ecosystem for enhanced efficiency
and user experience. We can see how a business enterprise
can utilize an interoperable blockchain network to unify
its infrastructure into a single customer experience. The
main advantage is that all the to-and-from communication
is secured and encrypted end-to-end inside one self-reliant
ecosystem. From the hub-and-zone model to the mechanisms facilitating communication between independent
blockchains, this section will unveil the intricacies that make
the Cosmos blockchain a standout solution in the pursuit
of interoperability. We will further compare the Cosmos
blockchain and other Interchain blockchains. By combining
its features, scalability, and security measures with those
of other prominent platforms, we aim to comprehensively
understand the Cosmos blockchain’s position in the broader
blockchain landscape [9]. To enhance supply chain transparency and facilitate cross-border financial transactions,
we will examine how the Cosmos blockchain’s interoperability contributes to solving real-world problems [10].
Figure 2 illustrates various blockchain technologies’ TPS
capability. Bitcoin and Ethereum have the lowest TPS at
7 and 15, respectively, while Cosmos and Hyperledger
show much higher capacities at 10000 and 20000 TPS,
respectively. This visualization is crucial for assessing the
scalability and efficiency of these blockchains in handling
transactions. This paper explores the connections made
by the Cosmos blockchain. By dissecting its features,
addressing the imperative need for interoperability, reviewing
its architecture, comparing it with peers, and presenting realworld applications. Figure 3 shows a simple illustration of
cross-chain communication. It can be imagined as an island
with different communication channels for each component
to transfer information from one part to another. From a user’s
perspective, we can see that there are several ways that data
can flow from one chain to another.
FIGURE 2. Comparison of transaction per second (TPS) across different
blockchain technologies.
A. ORGANIZATION OF PAPER
The paper is organized into sections that help explore
the features and application of the Cosmos blockchain
effectively. The first section, Section I holds the introduction
to this study. We illustrate the problem scope of interoperable
blockchains and define a domain where their application
is needed. In Section II, we explain our motivation for
exploring the Cosmos blockchain. In Section III, we explore
other solutions made to make blockchains interoperable.
Various solutions implemented in this direction have different
perspectives and views on the same problem and, hence,
different, innovative solutions. A review of these prior works
is presented in this section. The application layer of the
Cosmos blockchain is explained in subsection IV-A, where
we see how Tendermint is working behind the scenes to
power the entire Atom blockchain. The third and final
subsection “Governance Mechanism” helps us understand
the consensus used in the Cosmos blockchain. Section IV
we zoom in to see each component separately, such as the
Tendermint Core, and then place all the pieces together to
build a clear big-picture understanding of the working of
Cosmos blockchain in technical aspects. Section V provides
a broader look into the structure and architecture of the
Cosmos blockchain and how it applies to the interoperable
world of blockchains. Its subsection V-A, showcases the
key characteristics and highlights of this system and their
attributes. Section VI is an individual-level comparison of the
Cosmos blockchain with other production-grade solutions.
We see how it performs compared to sidechains, Smart
Contracts, and Routers. Later, we compare and analyze the
data to see where Cosmos blockchain stands in industry-wide
use cases. At the end of this section, we provide a
Strengths, Weaknesses, Opportunities, and Threats (SWOT).
Section VI-E analysis of the Cosmos blockchain. Section VII
focuses on the Use Cases and Applications of the Cosmos
blockchain. We see where the Cosmos blockchain is already
being applied and shows great potential. We see how it can
propose the idea of a Central Banking for Digital Currency
and its possibilities in gaming. Section VIII discusses
what lies ahead for interoperable blockchains and Cosmos
blockchain, considering its strengths. The Section IX holds
the conclusion of this study. We see what we can use the
Cosmos blockchain for and what the prospects are for the
Cosmos blockchain to be used in the industry. We also explore
the advantages and disadvantages of the Cosmos blockchain
and the possibilities it can offer businesses. The detailed
structure of this paper is presented in Figure 4, which shows
the distribution of the paper and key areas covered in each
section.
FIGURE 3. Cross-chain communication island.
B. NOVELTY AND CONTRIBUTION
The novelty of this paper lies in its in-depth analysis of
the Cosmos blockchain as a revolutionary platform for
blockchain interoperability. Cosmos introduces a unique
solution for one of the most pressing challenges in blockchain
technology: the difficulty of cross-chain communication
and scalability. This review highlights Cosmos’s Tendermint
BFT consensus mechanism and IBC protocol, facilitating
secure, scalable, and fast interactions between heterogeneous
blockchain platforms [11]. The innovative hub-and-zone
architecture sets Cosmos apart, enabling various blockchains
to operate autonomously while maintaining the ability
to exchange data and assets efficiently. This research
positions Cosmos as a significant player in creating an
interconnected blockchain ecosystem, thereby addressing the
limitations of isolated chains and promoting the broader
adoption of Decentralized Applications (DApps) and digital
commerce.
The contributions of this paper focus on the technical and
practical aspects of Cosmos blockchain and its potential to
revolutionize blockchain interoperability. First, it comprehensively reviews the Cosmos architecture, analyzing key
features such as Tendermint BFT, the IBC protocol, and the
Atom token for governance. Further, it explores how Cosmos
ensures secure and efficient communication between diverse
blockchains without sacrificing decentralization. The paper
compares Cosmos against other blockchain interoperability
solutions, such as Polkadot and ICON, showcasing its
FIGURE 4. Section-wise paper organization showing topics covered.
scalability, security, and governance strengths. The contributions of the paper are shown in Figure 5 and discussed as
follows:
i. Comprehensive Architectural Review: The paper reviews
the analysis of the Cosmos blockchain’s architecture, emphasizing its novel hub-and-zone model for
achieving cross-chain communication while maintaining
decentralization and scalability.
ii. Inter-Blockchain Communication (IBC) Protocol: The
research explores the IBC protocol’s capabilities,
which allow the transfer of data and tokens between
independent blockchains, promoting interoperability.
iii. Tendermint BFT Consensus Mechanism: The paper
discusses how the Tendermint BFT consensus mechanism enhances scalability, security, and transaction
finality, providing resilience against potential malicious
attacks.
iv. Governance Model: The paper explores Cosmos’s
decentralized governance model, which allows for
flexible upgrades and parameter adjustments while
maintaining the network’s security.
v. Comparison with Other Blockchain Solutions: The
review compares Cosmos with other blockchain solutions like Polkadot and ICON, highlighting Cosmos’s
superior performance in transaction speed, scalability,
and decentralized governance.
vi. Real-World Applications: The paper discusses various
real-world use cases of Cosmos, including Decentralized Finance (DeFi), supply chain management, and
gaming, demonstrating its practical relevance across
industries.
vii. Security Enhancements: The review identifies potential
security vulnerabilities within the Cosmos ecosystem
and suggests improvements to enhance its overall
robustness.
viii. Future Implications: The paper concludes by discussing
the future potential of Cosmos in fostering a fully
interconnected blockchain ecosystem, which is crucial
for advancing decentralized technologies globally.
II. MOTIVATION
The motivation for this paper is rooted in the transformative
potential of blockchain technology and its capacity to revolutionize how we conceive of and interact with digital trust
systems. The need for a cohesive and interoperable ecosystem
becomes increasingly apparent as the blockchain landscape
matures. This research focuses on the Cosmos blockchain,
a platform that epitomizes the quest for seamless inter-chain
communication for the next generation of blockchain applications. The impetus for this study is the recognition that,
while blockchain technology has made significant strides, the
siloed nature of existing chains hinders the realization of a
fully integrated digital economy. Cosmos blockchain offers
a solution to this fragmentation with its innovative approach
to scalability and interoperability [12]. By exploring the
Cosmos blockchain’s architectural nuances and operational
mechanics, this paper seeks to illuminate the path toward a
more interconnected blockchain environment. IBC protocol
and BFT consensus mechanism, the Cosmos blockchain network presents a compelling case study for overcoming these
challenges. This paper aims to provide a granular analysis
of the technical and strategic implications of the Cosmos
blockchain’s design choices. We will examine how these
decisions enable the platform to facilitate communication
between diverse blockchains and preserve the core principles
of decentralization and security fundamental to blockchain
technology [13].
FIGURE 5. Overview of the paper contributions, including architectural
review, Tendermint consensus, IBC protocol, governance model, security
enhancements, real-world applications, blockchain comparisons, and
future implications.
III. STATE OF ART
Blockchain technology, in its entirety, has proven to be a
great solution to improve our information systems. Although
it offers many features, it lacks several important ones,
such as interoperability. Since blockchains are rather closed
structures with complete transparency, interoperability is
difficult to achieve. This section briefly reviews and discusses
work done in this direction. Table 2 relate the concise
comparison of different blockchain interoperability solutions,
detailing their approaches, features, scalability, security, and
applicable use cases [14]. It showcases various strategies,
from smart transaction-based communication to specialized
architectures like Agri-SCM-BIoT, offering insights into the
evolving landscape of blockchain interoperability and its
diverse applications across industries [15]. Pillai et al. [16],
communication between multiple blockchains is achieved
with the help of transactions. These transactions led to a
mechanism that could smartly explore transactions and send
data from one type of blockchain to another. For example, the
chain that contains only information regarding the inventory
of a warehouse will now be able to communicate with
the chain responsible for its purchase. The mechanism
provided solely relied on data transfer that was taking
place among the blockchains. The changes made to the
database, or simply transactions, led to how these changes
can be used to communicate among various blockchains.
The solution provided by Ding et al. [17] is a new
interoperability framework called Inter-Chain. Inter-chain
supports scalable and secure interactions between any pair
of blockchains, reliably enabling cross-chain transactions.
The framework includes a three-handshaking method for
achieving asset transfers between separated blockchains.
Its architecture involves subchains, gateway nodes, and
validating nodes. This facilitates the seamless exchange
of assets and data between different networks. InterChain
addresses scalability issues faced by existing solutions for
blockchain interoperability and emphasizes the importance
of privacy and security in cross-chain transactions [20].
The proposed framework aims to provide a comprehensive
and efficient solution for enabling interoperability between
diverse blockchain ecosystems. Another work motivated by
the idea of MultiChain was presented by Wang [5]. The
authors introduced a router for blockchains that allows
blockchains to communicate with each other in the form of a
network similar to the Internet. The internet itself inspires the
design concept. Like internet routers in a network, blockchain
routers dynamically maintain information registered on
sub-chains and link them to the chain network. This allows
sub-chains to communicate with each other via a cross-chain
communication protocol. Major components of this architecture are a routing mechanism, connectors, a consensus
algorithm, and cross-chain communication. Connectors are
vital in linking different chains bi-directionally, sending
information between sub-chains and the blockchain router.
Connectors from a consensus system within each sub-chain
collect information on sub-chain blocks for validators. The
consensus algorithm this architecture uses is the Practical
Byzantine Fault Tolerance (PBFT) Castro and Liskov [21],
which involves reliable nodes that package new blocks and
participate in voting [22]. These components ensure that the
blockchain router acts as a bridge between different chains,
ultimately maximizing the potential for interoperability.
Performance isolation and scalability again lie as one of the
biggest challenges to overcome. The architecture presented
in this work enhances the user experience by allotting
a private blockchain to each of its users (tenants). This
ensured excellent scalability at both the individual level and
the multi-user level. With these versatile solutions, interblockchain communication seems a lot more approachable.
Still, most of the solutions presented have kept scalability
at their core. In various use cases, a large-scale user base
may not be intended; thus, a targeted service through
inter-blockchain communication is required. Blockchain
interoperability also aims to reduce the massive sizes of
blockchains that have to store different types of information
that are sometimes irrelevant to their original purpose.
In this direction, Lafourcade and Lombard-Platet [18] sheds
more light on an inter-blockchain model’s structure. This
work addresses the theoretical and practical challenges of
making two blockchains interoperable. It further explains
that the practical implications of blockchain interoperability
are limited to exchanging tokens that already exist on
both blockchains rather than enabling direct token transfers
between the two networks. Blockchain can be interoperable
when creating a two-in-one chain with both ledgers. This
way, inter-chain communication can be established, which,
in reality, is simply those two ledgers interacting with each
other and residing in the same domain of the chain. Also,
the entire system will have to maintain the balance of tokens
in both ledgers and see if there is any imbalance or a
missing token. Agriculture is an area where blockchain is
now gaining popularity. In the various stages of growing,
maintaining, tracking, selling, and securing crops, blockchain
has seen several use cases yet to be explored elsewhere.
Thus, Bhat et al. [19] has developed a new system that
streamlines the whole process of food crop production.
Since consumers demand safe, equitable, and sustainable
production, many new technologies, such as blockchain,
have been utilized. Therefore, processes that maintain food
processing, tracking, and supply chain mechanisms are
bound to use their separate blockchains. The proposed
Agriculture Supply Chain Management using blockchain
and the Internet of Things, referred to as (Agri-SCM-BIoT)
is an architecture that can help unify the idea of two or
more blockchains having different roles. It aims to address
the storage, security, interoperability, and privacy concerns
with the help of an IoT infrastructure with blockchain as
its backbone. Table 3 shows the comparative analysis of
Cosmos’ performance and attributes, as evaluated by various
authors in the Section III. It highlights key factors such as
throughput, interoperability, scalability, governance, security,
latency, and other parameters, indicating which aspects each
author addresses. Figure 6 shows a hierarchical dendrogram
that visualizes the methodology and disadvantages, with
color coding based on interoperability. It effectively organizes performance and author metrics, providing a better
understanding of the data relationships. The dendrogram
highlights key connections and categories, making it easier
to analyze the used references in Section III for better
performance analysis. This structure enables more informed
decision-making by visually representing the relationships
between various factors. The following section will discuss
the architecture and components that give the Cosmos
blockchain its shape.
IV. TECHNICAL REVIEW - COMPONENTS OF COSMOS
BLOCKCHAIN
For a system to be resilient enough to sustain the varied
requirements of its users, it requires a strong foundation
base with a brilliantly designed architecture that caters to
concurrency. The Cosmos blockchain network can effectively
harness the power of its underlying components to deliver
scalability and cross-chain communication [26]. These components were previously built individually to solve singular
problems, but the Cosmos blockchain provides a generic
solution for several problems. We will explore the different
components in this section and illustrate where each of these
components lies in action and how these come together to
power a unified solution.
A. TENDERMINT CORE
It is the core component of the Cosmos blockchain Network
and is used to power the various zones within the network. It is
a consensus engine that provides a high-performance, consistent, and secure PBFT-like consensus algorithm. Figure 7
shows the structural representation of Tendermint Core.
It performs well, particularly based on the BFT. The Application Blockchain Interface (ABCI) acts as a bridge between
Tendermint Core and the application layer [27]. It defines
a clear, standardized interface separating the blockchain
consensus engine from the application logic. This separation
allows developers to implement their applications or smart
contracts independently of the consensus algorithm. It is an
asynchronous protocol with fault tolerance. The participants
in this protocol are called validators. These validators take
part in voting. Validators wait a relatively short time until they
receive a complete block from an applicant before voting for
it to go to the next round. This time limit makes Tendermint a
less synchronous protocol. Only in this situation is the rest of
the protocol asynchronous. Figure 8 will help to understand
how all these components work together inside the Cosmos
blockchain network. The validators only move forward when
a block gets 2/3 of the votes [28]. The miner nodes are
responsible for solving the crypto puzzle so that the block
to be added to the chain can be owned. The sync nodes
perform all the synchronous functions. With the help of
BFT, Tendermint Core can tolerate up to 1/3
rd of a network’s
machines failing arbitrarily. It is language agnostic and can
be programmed using any programming language. It is
unlike other consensus algorithms that come pre-packaged
with built-in state machines. Through Tendermint BFT, state
machines can be replicated onto general computers around
the world [29]. It provides prompt confirmations that help
finalize a transaction once included in a block. Secure and
consistent replication is a fundamental problem in distributed
systems, and Tendermint provides all the necessary services
to perform replication.
B. BYZANTINE FAULT TOLERANT (BFT)
BFT is a class of consensus algorithms designed to achieve
agreement among a distributed network of nodes, even in
the presence of faulty or malicious nodes. “Byzantine” refers
to the Byzantine Generals’ Problem. This classic computer
science problem illustrates the challenges of achieving
consensus in a distributed system when some nodes may
behave arbitrarily or maliciously [30], [31]. The Byzantine
Generals’ Problem describes the problem where a common
enemy is at focus, and all the attackers (King’s generals) must
agree to a single strategy to ensure a win. The problem arises
when one or more attackers behave unusually or become
corrupt. This problem becomes particularly challenging
when communication is asynchronous, meaning there is no
FIGURE 6. Dendrogram visualizes hierarchical relationships using methodology used and disadvantages, with color representing interoperability and
labels showing author names and performance metrics.
FIGURE 7. Structure of the tendermint core.
guarantee about the time it takes for messages to be delivered,
and therefore, the uncertainty about the number and behavior
of faulty components [21].
i. Fault Tolerance: BFT algorithms are designed to tolerate
a certain number of faulty or malicious nodes within
the network without compromising the overall consensus
process. This fault tolerance ensures that the network
can continue to operate and reach agreement even in the
presence of adversarial behavior [32].
ii. Decentralization: BFT algorithms typically operate
decentralized, with no single point of control or authority. This decentralization helps prevent a single point of
failure and enhances the security and resilience of the
network.
iii. Security Guarantees: BFT algorithms provide strong
security guarantees, ensuring the network can operate
correctly and reach consensus, even in adversarial
behavior or network disruptions.
FIGURE 8. Visualizing the interaction between cosmos blockchain components, this flow illustrates nodes collaborating as a network of interconnected
chains.
iv. Consensus Mechanism: BFT algorithms use a consensus
mechanism to achieve agreement among the nodes in
the network. This mechanism involves a series of rounds
of communication and voting, during which nodes
exchange messages and agree on the state of the network.
C. ZONE AND HUBS
Zone and Hubs are independent blockchains powered by
Tendermint BFT and can be plugged into the Cosmos
blockchain Hub. Each zone can have its own constitution
and governance mechanism, allowing users to experiment
with different policies and governance models. A zone is
an independent blockchain powered by Tendermint BFT
plugged into the Cosmos blockchain hub. Each zone can have
its own constitution and governance mechanism, allowing
users to experiment with different policies and governance
models. Zones can be used to create specialized blockchains
for specific use cases, such as gaming, supply chain
management, or identity verification [33]. A hub, such as
the Cosmos blockchain hub, is a blockchain that can host
a multi-asset distributed ledger. This way, the tokens that
exist can be transported between chains. In Figure 8, the
Cosmos blockchain Hub chain includes each new block upon
validation completion.
D. INTER-BLOCKCHAIN COMMUNICATION (IBC)
PROTOCOL
The IBC protocol is a communication protocol that enables
different zones within the Cosmos blockchain Network to
communicate with each other and transfer tokens securely
and quickly without the need for exchange liquidity between
them. Blockchains’ primary communication issues are Interoperability, Scalability, and a Consensus Mechanism [34].
The IBC protocol handles these issues of islands of redundant
and inconsistent information in blockchain systems by
enabling different blockchain systems to communicate and
transact without intermediaries. IBC uses efficient routing
algorithms to dynamically update routing paths between
nodes in different blockchain systems, allowing for the
seamless transfer of data and transactions [35], [36]. When
a transaction involving two different blockchain systems is
generated, IBC analyzes and packs the transaction into a
specific form to adapt to the destination blockchain system.
This approach ensures that all relevant parties validate and
agree upon transactions and that data is stored consistently
and securely across different blockchain systems [37]. The
Algorithm 1 will help understand the working of the IBC
protocol. The algorithm illustrated gives more clarity on
how IBC powers the core functionality of the Cosmos
blockchain. In the first step, we select a leader known as the
proposer for a specific height and round. Height indicates
the progression of the state of the blockchain. And round
allows for another attempt at achieving consensus [38]. The
proposer is responsible for initiating the consensus process
for the given transaction. Followed by the next Block is
processed. If the current node is the leader, it processes
the transaction to create a block. This block contains the
relevant transaction data and is prepared for broadcasting
to the network. After this, the leader broadcasts the created
block to the network, allowing other nodes to receive and
validate the block. Upon receiving the block, Vote Verification
takes place, verifying the validity and casting a vote to
approve or reject the block. This voting process ensures
that consensus is reached regarding the transaction’s validity.
The algorithm then counts if sufficient nodes either approve
or reject the block. The algorithm stores the validated
transactions and the corresponding block, ensuring that
the agreed-upon transactions are securely recorded in the
blockchain.
E. COSMOS BLOCKCHAIN SDK
The Cosmos blockchain SDK is a framework for building
custom blockchain applications that can be integrated with
the Cosmos blockchain Network. It provides a modular architecture that allows developers to customize their
blockchain applications to meet their specific needs [39],
[40]. The key aspects of Cosmos blockchain SDK are the
following:
i. Modular Architecture: The Cosmos blockchain SDK is
modular, allowing developers to customize and assemble various modules to create blockchain applications
tailored to their specific use cases. This modular
approach provides flexibility and extensibility, enabling
developers to build applications with the desired
functionality.
ii. Customize Application Logic: Developers can define
custom application logic using the Cosmos blockchain
SDK, including creating custom tokens, governance
mechanisms, staking, and more. This allows for creating
blockchain applications that meet specific business
requirements and use cases [41].
iii. Developer Friendly: The Cosmos blockchain SDK
is designed to be developer-friendly, with extensive
documentation, tutorials, and resources to support
developers in building blockchain applications. It also
provides a testing framework for writing and running
automated tests to ensure the reliability and correctness
of applications.
iv. Security: The Cosmos blockchain SDK provides tools
and features to ensure the security and scalability of
blockchain applications built using the framework. This
includes support for Tendermint BFT consensus, which
provides a high-performance, consistent, and secure
consensus algorithm.
F. COSMOS BLOCKCHAIN GOVERNANCE
Cosmos blockchain Governance makes and implements
decisions within the Cosmos blockchain Network. It is
a decentralized decision-making process involving a distributed organization of validators responsible for voting
on proposals [33]. The governance mechanism is primarily
based on the Tendermint Core, where its nodes act rule-based
to select or reject the entry of a block into the network,
as shown in Figure 8.
V. OVERVIEW OF COSMOS BLOCKCHAIN
Blockchain interoperability is an important feature that
many businesses and teams are interested in, as it allows
different blockchain networks to communicate and function together smoothly, enabling more efficient processes
and broader applications of blockchain technology. Interconnected blockchains can ensure a secure tunnel environment for all the services owned by an organization. They
can practically pursue their operations normally and remain
highly secure with minimum chances of data mutation and
unauthorized access. As discussed in the literature review
section, some limitations must be overcome to have an
effective network of blockchains, each responsible for its
functions. To address this problem, Jae Kwon and Ethan
Buchman created the Cosmos blockchain in 2016 [42].
Cosmos blockchain originated from Tendermint, the underlying service that powers interoperability features. It aimed
to address Bitcoin’s proof-of-work consensus algorithm’s
speed, scalability, and environmental issues. The goal of
Tendermint was to provide a high-performance, consistent,
and secure consensus engine for blockchain applications.
Tendermint utilizes a BFT consensus algorithm to turn
any deterministic black box application into a distributed
replicated blockchain. In 2016, the Tendermint team created
a new blockchain network called Cosmos blockchain, using
the existing capabilities to allow multiple parallel blockchains
to interoperate while retaining their security properties [42].
In the Cosmos blockchain, many independent blockchains
work in zones. Tendermint BFT, a high-performance,
reliable, secure, and practical BFT-like consensus engine,
provides the power behind these zones. Further details
on this architecture are explained in Section IV. In this
direction, the Cosmos blockchain network is designed to
be an open-source network of distributed ledgers that can
serve as a new foundation for future financial systems based
on principles of cryptography, sound economics, consensus
theory, transparency, and accountability. The Tendermint
BFT consensus algorithm powers the Cosmos blockchain
hub, the first public blockchain in the network. One of the
key purposes of the Cosmos blockchain hub is to facilitate
interoperability and communication between different zones
through the IBC protocol. This protocol allows tokens to
be transferred securely and quickly between zones without
the need for exchange liquidity between them [43]. Cosmos
Blockchain Hub tracks the total amount of tokens held by
each zone, thereby isolating each zone from the failure of
other zones. In the following discussion, we have listed the
key features and capabilities.
A. COSMOS BLOCKCHAIN KEY CHARACTERISTICS
In this subsection, we mention some key characteristics of the
Cosmos blockchain drawn from its core capabilities, which
bring much value to the end user.
i. Multi-Asset Proof-of-Stake Cryptocurrency: The Cosmos blockchain Hub is a multi-asset proof-of-stake
cryptocurrency that allows users to hold and transfer
different types of tokens. The Cosmos blockchain Hub
is designed to be a simple governance mechanism that
enables the network to adapt and upgrade [44].
ii. Inter-Blockchain Communication: The Cosmos
blockchain allows for the secure and fast transfer of
tokens between different zones through the IBC protocol.
This protocol enables different zones to communicate
with each other and transfer tokens without the need for
exchange liquidity between them.
iii. Scalability: The Cosmos blockchain is designed to be
highly scalable, allowing for many parallel blockchains
to interoperate while retaining their security properties.
This is achieved through Tendermint BFT, which
provides a high-performance, consistent, and secure
consensus engine [23].
iv. Decentralization: The Cosmos blockchain is designed
to be decentralized, with no single point of failure. The
network is secured by a globally decentralized set of
validators that can withstand severe attack scenarios[45].
v. Governance: The Cosmos blockchain offers high flexibility. It allows different zones to have their governing
mechanisms. Thus, customization is offered at an atomic
level in the entire network of chains.
B. APPLICATION LAYER OF COSMOS BLOCKCHAIN - THE
COSMOS BLOCKCHAIN SDK
This part of the Cosmos blockchain contributes to overcoming challenges faced with usability. With multiple chains
to handle and integrate, there is an imminent challenge
of interacting with the interface of these chains. Thus,
a governing mechanism to which all chains can abide
will be required to act as a universal interface. The
Cosmos blockchain Software Development Kit (SDK) is a
package of modules that enables developers to create and
deploy apps seamlessly [46]. This provides the required
level of abstraction needed so that they can focus more
on application logic. This way, Cosmos Blockchain SDK
allows developers to create and launch new blockchains
and connect different blockchains. This SDK offers several
features.
i. Modular: Comsos provides different modules to suit the
specific requirements of your project. Thus, creating a
blockchain with tailor-made features targeting a specific
or generic use case is easier [6]. This allows developers
and users to handle the changing use cases, thus making
maintaining dependencies easier.
ii. Scalable: To match the desired throughput of transactions and data flow, we can run parallel chains inside the
Cosmos blockchain SDK. Thus, this can adjust to the
ever-growing demands of the user base. This offers to
apply Continuous Integration/Continuous Deployment
(CI/CD) to some extent, thus becoming a viable solution
for the cloud-based delivery of services [47].
iii. Open Source: If developers of a specific community or
organization feel the need for a capability or a feature
that will benefit their use-case or is an existing problem
in the existing Cosmos blockchain architecture, they can
contribute to adding these changes to the code base [48].
With an open source developer community. It allows the
creation of better applications with collaboration. There
are discussion forums that allow any bug or an open issue
to be drawn to stakeholders’ notice so that it can be fixed.
This also drives worldwide support through ideas and
suggestions from the Cosmos Open Source repository.
Algorithm 2 Cosmos Blockchain Governance
Input: Gaming Tokens from Zone A, TA; Destination Zone, ZB
Output: Equivalent DeFi Tokens (Zone B)
Step 1: Zone A initiates transfer
begin
Read total Tokens of Zone A: tokenA = getToken(ZA);
Create a model for tokens;
Step 2: Inside Cosmos blockchain Hub
begin
Get model for tokens from Zone A: getModel(tokenA, ZA);
if tokenA > TA then
Create model for Zone B;
Get model for tokens from Zone B: MB = getModel(tokenA, ZB);
Broadcast to Zone B: broadcastIBC(ZoneB);
Zone B mints DeFi tokens: TD = minter(MB);
Transfer DeFi tokens to the user.
In Algorithm 2, we detail the inter-zone token transfer
algorithm as follows:
Zone A Initiates Transfer to Alice, a user in Zone A,
who wants to transfer her gaming tokens to Zone B (DeFi
blockchain [25]). Alice initiates the transfer by specifying the
number of gaming tokens she wants to move. The Cosmos
blockchain hub acts as the central router, connecting different
zones within the blockchain network. The transaction is
verified when Alice’s request reaches the Cosmos blockchain
Hub. It ensures that Zone A has enough tokens to back the
transfer. The Hub then creates a representation of Alice’s
gaming tokens in Zone B. Using the IBC protocol, also
mentioned in Algorithm 1, the Cosmos blockchain Hub
communicates with Zone B. Zone B creates actual DeFi
tokens that are equivalent to the Hub’s representation. Alice
now holds her DeFi tokens in Zone B, bridging the gap
between gaming and DeFi ecosystems.
C. ADDRESSING VULNERABILITIES IN THE COSMOS
BLOCKCHAIN
Cosmos blockchain offers significant advancements in scalability and interoperability through its Tendermint consensus
FIGURE 9. Highlighting the various security vulnerabilities in the cosmos
blockchain using word cloud diagram.
mechanism and IBC Protocol [49], [50]. It is essential to
acknowledge and address its vulnerabilities. This section
objectively analyzes the pros and cons of its consensus
mechanism, security vulnerabilities, and overall complexity.
It proposes suggestions to solve these issues and enhance the
robustness of the Cosmos blockchain. Figure 9 shows a word
cloud diagram highlighting the key issues and vulnerabilities
in the Cosmos blockchain. The diagram visually represents technical and operational challenges such as network
scalability, security concerns, interoperability issues, and
governance complexities. This visual representation helps
to identify and prioritize areas that require attention and
improvement to ensure the robustness of the blockchain
network.
1) CONSENSUS MECHANISM: PROS AND CONS
Pros:
i. Byzantine Fault Tolerance: The Tendermint consensus
mechanism provides high fault tolerance, ensuring the
network remains operational even if some nodes are
compromised.
ii. Finality: Transactions achieve finality quickly, reducing
the risk of forks and double-spending attacks.
iii. Energy Efficiency: Compared to proof-of-work mechanisms, Tendermint is more energy-efficient, which
makes it more environmentally friendly.
Cons:
i Validator Centralization: The consensus mechanism can
lead to centralization if a few validators control a
significant portion of the voting power.
ii Sybil Attacks: Without adequate security, the network
may be vulnerable to Sybil attacks, where an attacker
could create numerous identities to gain disproportionate
influence.
2) SECURITY VULNERABILITIES
Potential Attack Vectors: Despite its robust design, the
Cosmos blockchain is not immune to security threats.
Potential attack vectors include:
i. Double-Spending: Although Tendermint provides finality, double-spending attacks could still occur if validators
are compromised.
ii. DDoS Attacks: The network could be susceptible to
Distributed Denial-of-Service (DDoS) attacks to disrupt
validator operations.
iii. Smart Contract Exploits: As with any blockchain,
vulnerabilities in smart contracts could be exploited,
leading to significant financial losses.
3) COMPLEXITY AND INTEROPERABILITY CHALLENGES
i. Complex Architecture: The interconnected nature of
the Cosmos ecosystem, while beneficial, introduces
complexity that can pose challenges in maintenance and
scalability.
ii. Inter-Blockchain Communication: While the IBC Protocol facilitates seamless transactions across different
blockchains, ensuring secure and efficient communication remains challenging, particularly as the network
grows.
4) SECURITY VULNERABILITIES IN COSMOS BLOCKCHAIN:
EXAMPLES
The Cosmos blockchain has encountered several notable
security vulnerabilities that highlight the unique challenges
within its ecosystem [26]. One significant example is the
Redelegation Attack, where malicious actors exploit the
delegation mechanism to quickly change their validator,
gaining undue influence over the network and potentially
manipulating consensus decisions [51]. Another crucial issue
is the Denial of Service (DoS) Attack, wherein attackers
flood the network with excessive transactions, overwhelming validators and disrupting legitimate activity [52]. The
Reentrancy Vulnerability, specifically the Dragonberry Vulnerability, exploits recursive calls in smart contracts, allowing
attackers to withdraw more funds than intended [24]. The
Slow Convergence in Mathematical Operations can lead to
inefficiencies in transaction validation, while Authentication
Bypass Vulnerabilities allow unauthorized access to critical
functions [53]. Vulnerabilities in the IBC protocol, such as
Proof of Absence Manipulation (PAM), enable attackers to
falsely claim the absence of transactions, undermining the
trust between chains [54]. Packet Forgery and exploits within
IBC channels can allow malicious actors to inject harmful
transactions into the network [55]. Figure 10 shows examples
of security weaknesses in the Cosmos blockchain. We found
these weaknesses in blog posts and discussions from the
Cosmos blockchain’s Discord community, giving a clearer
understanding of the network’s security challenges.
i. Dragonberry Vulnerability (Repeated Action Attack):
The Dragonberry Vulnerability, known as the Repeated
FIGURE 10. Illustrative examples of security vulnerabilities in cosmos, derived from blog posts and discussions on the
discord community of cosmos blockchain.
Action Attack, involved a critical flaw in how Cosmos verified the validity of transactions between
blockchains [12], [62], [63]. The vulnerability allowed
bad actors to send fake proofs, exploiting the system’s
lack of proper checks [64], [65]. This could have led to
attackers successfully tricking the system into accepting
false information repeatedly, potentially resulting in fund
theft or confusion across different blockchains. The
Cosmos team implemented a software patch to add
extra verification layers to resolve the issue, ensuring
that false proofs are detected [66]. They collaborated
with key stakeholders to deploy this fix across multiple
blockchains, effectively preventing such attacks before
they could occur [51].
ii. IBC Timeout Attack (Fake Timeout Trick): The IBC
Timeout Attack, often called the Fake Timeout Trick,
targeted Cosmos’s IBC protocol, facilitating token transfers between different blockchains [11]. The protocol
included a built-in timer that refunded tokens if the transfer was not completed within a certain time frame [67].
This mechanism is vulnerable to manipulation. Attackers
could send false messages to make it appear that a
transfer had failed when, in fact, it had succeeded [68].
By doing so, they could retrieve their tokens while keeping the tokens they had received, effectively doubling
their assets. To address this vulnerability, the developers
introduced more robust checks to verify the validity
of timeout messages, thereby preventing attackers from
exploiting the system’s refund mechanism [69].
iii. ICS-23 Proof Forgery (Fake Proof Attack): Another
significant issue is ICS-23 Proof Forgery, also known as
the Fake Proof Attack (FPA). This vulnerability is tied
to the system Cosmos used to confirm the occurrence or
non-occurrence of transactions, a system that relied on
proofs [70]. An exploitable flaw in this proof mechanism
allowed attackers to create fake proofs. Such fake proofs
could falsely claim that a transaction occurred or did not
occur, allowing attackers to manipulate the network and
steal funds. To solve this risk, the team improved the
proof verification system, ensuring that all proofs were
authentic and valid, thereby preventing any acceptance
of forged proofs within the network [51].
iv. Staking Vulnerability (Penalty Trick): The Staking Vulnerability, referred to as the Penalty Trick, exploited
Cosmos’s validator mechanism, in which validators
secure the network by staking tokens [71]. Misbehaving
validators could be penalized through a process called
slashing [72]. There is a loophole that allows attackers
to falsely frame honest validators for misbehavior,
causing them to lose their staked tokens. This vulnerability also allowed malicious validators to exploit the
system, evading penalties and potentially destabilizing
the network [73]. To counteract this, the developers
enhanced the checks surrounding validator actions,
ensuring that penalties were only applied in cases of
genuine misbehavior, making the network fairer and
more secure [74].
v. Authentication Bypass (Skipping Login Attack): The
Authentication Bypass, or Skipping Login Attack,
exposed a flaw in the role-based permission system
of Cosmos, where some critical tasks required specific
permissions. Attackers discovered a way to bypass the
login process, gaining unauthorized access to sensitive
roles within the network [75]. This allowed them
to make unauthorized changes, disrupt the network,
or steal funds. To address this issue, the Cosmos team
reinforced the security checks. It introduced additional
security, including Multi-Factor Authentication (MFA),
making it more challenging for attackers to bypass the
authentication process [76].
vi. Double-Spend Attack (Using the Same Tokens Twice):
The Double-Spend Attack (DSA) involved tricking the
blockchain system into using the same tokens more than
once, undermining the basic principle of blockchain—
that each token can only be spent once [77], [78].
An attacker could potentially control multiple validators,
thereby splitting the network and using the same tokens
on different versions of the blockchain [79]. This
effectively allowed them to spend the same tokens twice.
To prevent this attack, Cosmos implemented stringent
requirements for validator consensus, ensuring that a
majority of validators must agree on every transaction.
The network imposed strict rules and penalties for
misbehavior, thus reducing the chances of a successful
double-spend attempt [80].
5) SUGGESTIONS FOR IMPROVEMENT
i. Decentralization Measures: To reduce validator centralization, the Cosmos network could implement measures
such as random validator selection or increased validator
incentives for smaller participants.
ii. Enhanced Security Protocols: Implementing advanced
security protocols, such as multi-signature wallets and
hardware security modules, can help protect against
attacks [36], [81].
iii. Regular Audits and Upgrades: Conducting regular
security audits and system upgrades can identify and
rectify vulnerabilities promptly.
iv. Simplifying Architecture: Streamlining the blockchain
architecture and improving documentation can reduce
complexity and make it easier for developers to build on
the Cosmos platform.
D. GOVERNANCE MECHANISM - A UNIVERSAL
INTERFACE
An interesting aspect of this network is the governance
mechanism that has been implemented, keeping in mind the
actual nature of a blockchain. This governance mechanism
enables the network to adapt, upgrade, and coordinate
changes to the blockchain, such as variable parameters of the
system, software upgrades, and constitutional amendments.
The key aspects that this mechanism delivers are:
i. Decentralized Decision-Making: The governance mechanism involves a distributed organization of validators
responsible for voting on proposals. This decentralized
decision-making process ensures that no single entity has
unilateral control over the network [86], [87].
ii. Proposal Process: Any changes to the Cosmos
blockchain Hub, such as parameter adjustments, software upgrades, or constitutional amendments, are proposed and voted upon by validators. Proposals require
a deposit of tokens, and voters can choose to take the
deposit if the proposal is deemed spam.
iii. Voting and Decision-Making: Validators and delegators
can vote on proposals using options such as Yea,
YeaWithForce, Nay, NayWithForce, or Abstain [88].
A strict majority of Yea or YeaWithForce votes (or Nay
or NayWithForce votes) is required for a proposal to be
decided as passed or failed. A veto mechanism allows a
minority to veto a majority decision, but this action has
penalties.
iv. Parameter Changes and Inflation: Parameters of
the Cosmos blockchain Hub, such as block times,
transaction fees, and inflation rates, can be changed
by passing ParameterChangeProposals. This includes
inflation and reserve pool funds that can be spent by
passing BountyProposals [38].
VI. COMPARATIVE ANALYSIS
In this section, a review of all the available inter-blockchain
communication solutions is discussed. We have classified the
available solutions into four categories: sidechain solutions,
blockchain routers, smart contracts, and industrial solutions.
Table 4 shows a comparative overview of blockchain
systems and highlights key metrics such as type, consensus
mechanism, block time, and transaction time for blockchains
like Bitcoin, Ethereum, and Cosmos, illustrating their varied
performance and application potential. It includes public
and private blockchains such as Bitcoin, Ethereum, and
Hyperledger. A noteworthy inclusion is Cosmos, a public
blockchain that employs the BFT consensus mechanism [74].
Unlike Bitcoin and Ethereum, which do not guarantee finality
and require longer block times (600s and 15s, respectively),
Cosmos achieves transaction finality, has a block time of
just 6 seconds, and requires only one block for confirmation,
resulting in a specific average transaction time of approximately 55.448 seconds. This makes Cosmos an interesting
case of efficiency and speed in transaction processing
compared to other blockchains, showcasing its potential for
high-speed applications [89]. We have conducted empirical
research and consulted several reputable sources to determine
the average transaction time, reviewed existing literature
and studies for each blockchain, provided insights into
transaction times under typical network conditions, and
analyzed transaction data from the respective blockchain
networks to ensure accuracy and relevance of transaction
time. There are various ways in which interoperability can
be achieved. Sidechains and Cross-Chains are the broad
categories that have shown promising results. We compare
the Cosmos blockchain extensively with other available
industrial solutions and sidechains to understand how they
differ from full-fledged blockchain networks and what led to
the need for networks.
A. COMPARISON WITH SIDECHAINS
Sidechains were introduced as chains pegged for asset
transfer between Bitcoin chains and other cryptocurrencies.
Sidechains are limited to a one-to-one transfer relationship,
and the asset count does not increase, which means for a fixed
number of assets, we can do a single chain-to-chain transfer
of assets using sidechains [90]. The following table explores
various side-chain solutions. Table 5 has shown that the various sidechain projects had a variety of implementations even
when running on either the Bitcoin or Ethereum blockchain.
RSK [91], Plasma [83], and POA Network [84] all have
their architecture based on miners and nodes and still follow
different consensus mechanisms. POA only drives the complexity of the process to a higher level, and while it allows the
inter-chain transfer of assets, it is still a transfer between the
same types of blockchains. This is where sidechains fell short
on functionalities [92]. Cosmos and Sidechain blockchain
interoperability exhibit distinct architectural approaches to
connecting multiple blockchains[9], [12], [37], [93]. Cosmos
follows a hub-and-zone model, where numerous independent
blockchains, called zones, communicate through a central
Cosmos Hub using the IBC protocol [54]. This model allows
for decentralized and secure exchanges of tokens and data
between the zones and emphasizes decentralized governance.
In contrast, sidechain blockchain interoperability operates
through a main blockchain (such as Ethereum or Bitcoin)
connected to various sidechains using smart contracts or a
two-way peg mechanism [92]. The sidechain model relies on
a more centralized structure, where the main blockchain is
crucial in coordinating and managing asset transfers between
itself and the sidechains [94]. This architectural difference
highlights how Cosmos focuses on decentralization with
secure communication, while sidechains maintain a more
centralized control through the main blockchain. Figure 11
shows a detailed comparison of the architecture of these two
interoperability models, highlighting their structure and differences. Table 6 shows the architectural and protocol-based
comparison between Cosmos and sidechain blockchain
interoperability. It highlights key differences in architecture,
interoperability protocols, centralization, security models,
scalability, and trust models, providing a comprehensive
overview of their distinct approaches to blockchain interoperability. Figure 12 compares transaction finality time
between Cosmos and Sidechain networks as Transactions
per Second (TPS) increase. Cosmos consistently achieves
lower finality times, making it more efficient, especially at
higher TPS, due to its faster consensus mechanism and better
scalability. Figure 13 shows the CPU utilization of Cosmos
and Sidechain networks across different transaction costs (gas
fees). Cosmos consistently exhibits lower CPU utilization,
especially at higher transaction costs. For instance, at a gas
fee of 0.6, Cosmos utilizes around 45% CPU, while Sidechain
reaches 55%, indicating that Cosmos is more resourceefficient. Figure 14 shows the latency comparison between
Cosmos and Sidechain networks as block sizes increase.
Cosmos consistently demonstrates lower latency, with 150 ms
at a 6 MB block size, compared to Sidechain’s 250 ms. This
lower latency across all block sizes indicates that Cosmos
offers faster processing, making it more efficient in handling
larger block sizes. Figure 15 compares consensus algorithm
efficiency between Cosmos and Sidechain networks as
memory usage increases. Cosmos consistently demonstrates
higher efficiency, maintaining around 85% efficiency across
all memory levels, while Sidechain efficiency peaks at about
70%. This indicates that Cosmos is more effective at utilizing
memory to achieve better consensus, making it more efficient,
especially under higher memory usage conditions.
B. COMPARISON WITH OTHER BLOCKCHAIN
INTEROPERABILITY STUDIES
Comparing Cosmos with other prominent blockchain interoperability solutions is crucial to understanding its unique
advantages and positioning in the field [95]. Notable studies
in this area include Polkadot, Interconnected Network
(ICON), and Alliance of Interoperable Networks (AION).
Polkadot employs the Nominated Proof-of-Stake (NPoS)
mechanism and Cross-Chain Message Passing (XCMP)
protocol to achieve high scalability and near-instantaneous
transaction finality [12]. ICON utilizes the Loop Fault
Tolerance (LFT) consensus and Blockchain Transmission
Protocol (BTP) to enhance connectivity among multiple
blockchains, focusing on Decentralized Finance (DeFi)
applications [59]. AION uses the BFT mechanism and AION
FIGURE 12. Comparison of transaction finality time between cosmos and
sidechain networks as transactions Per Second (TPS) increase.
Interchain Communication (AIC) protocol, targeting enterprise applications with high security and near-instantaneous
transaction finality [96]. Each of these solutions contributes
uniquely to the field of blockchain interoperability. Still,
Cosmos stands out with its Tendermint consensus mechanism
and IBC protocol, ensuring high scalability, security, and
seamless cross-chain transactions, thus positioning itself as
a pivotal player in revolutionizing blockchain ecosystems
and their impact on digital commerce and governance [9].
Table 7 below compares these key features across different
blockchain interoperability solutions.
C. SMART CONTRACTS AND ROUTERS
A different approach is using blockchain nodes to act as
routers between different chains that can direct requests
to each other. There were a few proposed solutions; an
analysis of these and a side-by-side comparison are presented
below. Wang proposes a multiple-chain structure for the
robust transfer of assets [5]. The architecture had four layers.
The basic layer is, for application purposes, a blockchain
layer, a multi-chain communication layer, and an application
layer. The paper also introduced the model for packaging
transactions and routing. Mohanty et al. [97] have shown an
approach that used Delegated Stake-PBFT consensus. This
enterprise blockchain architecture allows multiple chains
to connect using a centralized protocol that enables crosschain communication. The proposed router was formed as an
Artificial Neural Network Chain (ANNChain) combined with
other chain systems.
D. INDUSTRIAL SOLUTIONS: NETWORK OF BLOCKCHAINS
We also need to consider the industry-ready solutions
that have evolved from sidechains and smart contracts
and are now present before us in the form of actual
systems solutions. The Polkadot project [98] is used for
heterogeneous blockchains. In this project, the chosen token
is Dot. The structure of Polkadot revolves around three
primary categories: Parachains, Relay chains, and Bridges.
Parachains function as diverse blockchains, relay chains
oversee transaction consensus and delivery, and bridges
connect parachains to their consensus. Within the Polkadot
network, participants can take on one of four roles: Validators,
nominees, Collators, or Fishermen. Using its platform, the
FIGURE 15. Comparison of consensus algorithm efficiency between
cosmos and sidechain networks for different memory usage (MB).
ICON Project fosters connections among various blockchain
entities and communities, including financial institutions,
government offices, hospitals, and universities. This platform
comprises Nexus and ICON Republic. Nexus is a collection
of independent blockchain entities linked through ICON
Republic portals [99]. ICON employs Loop Fault Tolerance
(LFT) as its consensus algorithm, and its official token
is ICX. LFT enhances BFT consensus algorithms using
tendermint [100]. A notable constraint of the project is its
specific focus and design tailored for Korea, aligning with the
regulatory policies governing blockchain and crypto companies in the country [101]. Table 8 shows the ratio between
the circulating supply and the total supply of tokens in all
the above-mentioned chains. Circulating Supply refers to the
number of tokens currently participating in transactions. The
Total Supply refers to the total number of a specific cryptocurrency’s coins or tokens in circulation on a blockchain and
publicly available for the market to trade. We can see that even
in its initial form, the Cosmos blockchain has a ratio of 1 as
compared to other chains, depicting a complete adoption rate
and resilience in the total amount of tokens produced. And
thus, a viable solution. Block Collider [103] is a multi-chain
platform built on a group of existing exported blocks from
other blockchains in the network, integrating the chains
to provide cross-chain features. Peer-to-peer decentralized
miners collect the block from the connected blockchains
with no centralized validators. Block collider uses a proof
of distance consensus mechanism, a modified version of the
proof of work consensus algorithm. The Aion Project [39]
sets out to facilitate communication and foster cross-chain
interoperability among various blockchain platforms. The
Aion architecture forms a multi-tier blockchain network
with four key components: Connecting Networks, Interchain
Transactions, Bridges, and Participating Networks. Connecting Networks serve as protocols enabling different and
independent blockchains to communicate within the AION
Platform. Interchain transactions facilitate data transfer
between connected blockchains within the ecosystem [50].
Bridges, a group of validators, validate these interchain
transactions. Any blockchain network can become a Participating Network if it meets specific requirements defined
by the Aion ecosystem. The consensus algorithm employed
by the Aion ecosystem is a hybrid staking and proof-ofintelligence system. The native token of the Aion blockchain
is called AION [104]. Metronome is a project that aims
to create a better cryptocurrency solution by enhancing
current cryptosystems. Along with enhancing the throughput,
Metronome enables cross-blockchain transfer, where a user
can transfer its token from one blockchain to another using
a proof-of-exit receipt. The token used in this project is the
Masternode Token Network (MTN). Ripple introduced the
Interledger Protocol (ILP), a framework to facilitate atomic
swaps between diverse blockchain platforms [49]. Unlike
a blockchain platform, the Interledger protocol does not
necessitate a consensus mechanism. Instead, it enables secure
transactions without being tied to a specific blockchain. The
protocol ensures sender and receiver isolation, mitigating
risks associated with intermediary failures. Security in the
transfer process is maintained through hash locking, wherein
the payment is conditionally locked until the transfer is
successfully secured. Figure 16 shows how the number
of transfers has varied over a year. This trend is shown
between a time of one year (Horizontal Axis) and the total
number of tokens transferred in multiples of 1000 (Vertical
Axis). Both trends show an increase in the total transfer
counts, which is fairly high from December 2023. This
shows how the adoption of the Cosmos blockchain has
increased for first-time and regular users. It also highlights the
number of senders and receivers on the Cosmos blockchain
over the years. This also portrays the Cosmos blockchain’s
consistent behavior. The trend is shown between a time
of one year (Horizontal Axis) and the number of tokens
transferred (Vertical Axis). The steady increase in these
trends is not a spike but a composition of variations with an
overall increase. New chains joining the network are being
sustained and remain stable. There are three data points
colored with blue, green, and orange. Green represents the
unique receivers, orange represents unique senders, and blue
represents the total number of unique users on the chain.
The transactions using blockchain being personalized and
anonymized gives consumers the power to use it according
to their convenience [105].
E. ANALYSIS BASED ON SWOT
Cosmos blockchain has a lot to offer. It is not a different
kind of blockchain. Instead, it is an extension or an evolution
of blockchain as a domain [95]. For a system relying on
blockchain for its security, there will be a time when a
cross-network request needs to be sent, or a data transfer
needs to be made [106]. This is where an inter-chain network
will come into use. For that, it is not just about the presence
of a solution but also the functionality these systems will
require. A high-performance and reliable system is always
easier to adopt and use. This also builds consumer trust if it
is in the form of a product [107]. Cosmos blockchain delivers
on these parameters to the best extent. The flexibility with
distributed governance and interoperability makes it a viable
candidate for a cross-chain solution [12].
i. Scalability: The Cosmos blockchain ecosystem’s focus
on scalability through the use of Tendermint BFT
consensus and the IBC protocol could enable the development of high-performance blockchain applications
that can handle large transaction volumes and support a
wide range of use cases.
ii. Governance: The Cosmos blockchain ecosystem’s governance mechanisms, including those at the hub and zone
levels, present an opportunity to develop more inclusive and democratic decision-making processes. This
could lead to the creation of more community-driven
blockchain applications and services.
iii. Interoperability: The Cosmos blockchain ecosystem’s
focus on interoperability between different blockchain
networks presents a significant opportunity to develop
cross-chain applications and services. The ability to
transfer value and data seamlessly between different
blockchain networks could unlock new use cases and
business models.
iv. Modular Architecture: The Cosmos blockchain SDK is
modular, allowing developers to customize and assemble
various modules to create blockchain applications tailored to their specific use cases. This modular approach
provides flexibility and extensibility, enabling developers to build applications with the desired functionality.
1) COSMOS DEVELOPMENT OPPORTUNITIES
Cosmos offers many development opportunities for those
interested in blockchain. Its unique design allows different blockchains to work together, making creating new
decentralized applications and services easier [95]. The
growing community encourages collaboration and invites
developers to contribute to open-source projects, providing a great platform for improving skills and building useful solutions. The following explores specific
areas within Cosmos where developers can exploit these
opportunities.
i. Partnership: Building of two or more services can be
done by keeping the Cosmos blockchain as a platform.
It can act as a platform that lays common rules in the form
of a protocol so that different kinds of blockchains can
communicate with each other, similar to the World Wide
Web (WWW) that connects different devices, networks,
and data centers by bringing them on the same platform,
irrespective of the end-user platform, whether it is a
laptop, smartphone, smart TV. The same tokens are
accessible everywhere through a common channel.
ii. Customized: Another major area for the Cosmos
blockchain to become a viable application is customized
solutions for a network of blockchains. Customization
is a major opportunity for the Cosmos blockchain to
flourish since it has smaller individual blockchains in the
form of zones that can have their own custom rules and
mechanisms.
iii. Independent Networks: This leads us to another possibility of the Cosmos blockchain in independent private
networks. This is very suitable for smaller consumers just
starting to use blockchain as a security solution and want
only specific features.
2) LIMITATIONS OF THE COSMOS BLOCKCHAIN
There are a few places where the Cosmos blockchain falls
short and might showcase its weaknesses that are sometimes
not in its full control, but surely, some measures can be taken
to mitigate them.
1) Smart Contract Vulnerabilities: Smart contracts are an
essential component of many blockchain applications,
including those built on the Cosmos blockchain. Attackers could exploit the vulnerabilities in smart contracts to
steal funds or compromise the network’s security.
2) Network Infrastructure Attacks: The infrastructure
that supports the Cosmos blockchain, including
nodes and validators, could be targeted by attackers
seeking to disrupt the network or compromise its
security.
3) Governance Attacks: The governance mechanisms
within the Cosmos blockchain ecosystem, including
those at the hub and zone levels, could be targeted
by attackers seeking to manipulate decision-making
processes or compromise the network’s security.
VII. USE CASES AND APPLICATIONS
Some effective and real-life applications are listed below
that will help understand the potential of cross-chain
communication. Figure 17 will help illustrate this further
by describing various aspects of society where the Cosmos
blockchain finds its application.
A. IDENTITY MANAGEMENT
There are several places where organizations are in contact
with employees of other organizations. The identity credentials of these employees are difficult to track and manage.
Even in a large organization, many sub-organizations may
host several people working and communicating with different teams. This can be facilitated and monitored with the help
of Cosmos blockchain [63].
B. CENTRAL BANKING DIGITAL CURRENCY (CDBC)
Currently, there are studies on CBDC with a blockchainbased distributed ledger. This paper proposes Cosmos
blockchain-based CBDC (Cos-CBDC), which enables communication between blockchains using the IBC protocol
to ensure interoperability. We analyze the requirements
of Cos-CBDC and design and implement it using Cosmos blockchain-SDK. The group of key management
systems for Cos-CBDC gives different user privileges,
and privacy-preserving is possible in the key generation
process [108].
C. PROTECTION OF LIQUIDATION
Cross chains can help protect positions held in DeFi
protocols across multiple chains by automatically sending
assets from one chain to DeFi protocols on another to
prevent liquidations [109]. With Industry 4.0 standards,
data protection is being given more importance than
ever. New Quantum-based solutions are emerging for data
protection [40].
D. ETHEREUM AND BITCOIN TRANSACTIONS
The current technologies through which you store and
transfer your Ethereum and Bitcoins are done through
Cross-Chain communication. Polkadot and Chainlink
tokens can manage most of this [110]. Wormhole and
other non-token solutions should also get the job done,
keeping more data on your device and less in the
cloud [111].
E. GAMING
Cross-Chain by ChainLink allows gamers playing on a
chain to interact with gamers on another chain. It enables
interoperability between Web3 games across networks [112].
VIII. FUTURE WORK
Exploring the Cosmos blockchain’s potential in addressing
global challenges presents a promising avenue for future
research. In DeFi, the Cosmos blockchain stands to revolutionize financial ecosystems by fostering interoperability
across diverse blockchains, thus enabling a more inclusive
financial landscape. Solutions are being developed specifically for connected vehicles that use blockchain as their
communication medium [113]. The implications for supply
chain management are equally transformative, with the
Cosmos blockchain poised to enhance transparency and efficiency through blockchain integration, potentially reshaping
global logistics. Transport and logistics, the way we currently
travel by roads, is bound to be transformed by the internet
of vehicles [114]. Cosmos blockchain could be instrumental
in unifying medical records in healthcare, thereby improving
patient care and accelerating research collaboration. The
digital identity and authentication domain could also see a
paradigm shift with the Cosmos blockchain, offering a secure
and private identity management framework. The unfinished
point on climate change and sustainability suggests a research
trajectory where the Cosmos blockchain could support
environmental initiatives, possibly through tracking carbon
footprints or facilitating green economies. Each of these areas
not only represents a significant stride in their respective
fields but also underscores the multifaceted capabilities of
the Cosmos blockchain as a tool for innovation and societal
advancement.
IX. CONCLUSION
This paper explored various blockchain interoperability
solutions, focusing on the Cosmos blockchain and its innovative approach to cross-chain communication. By exploring
the Tendermint consensus mechanism and IBC protocol,
Cosmos facilitates secure and scalable interactions between
independent blockchains, addressing key limitations of
isolated blockchain systems. The paper highlighted Cosmos’s
strengths, including its decentralized governance model
and modular architecture, allowing flexible upgrades and
customized blockchain applications. These features make
Cosmos highly adaptable for use in industries such as finance,
healthcare, gaming, and supply chain management, where
secure cross-chain transactions are crucial. Despite these
strengths, the paper also acknowledged challenges such as
potential security vulnerabilities and architectural complexity
that require further research. Cosmos presents a promising
framework for the future of blockchain technology, with its
scalability and decentralized approach positioning it as a key
player in fostering blockchain interoperability. While there
are areas for improvement, particularly in security, Cosmos
has the potential to drive the evolution of decentralized
applications and enable a more interconnected blockchain
ecosystem.