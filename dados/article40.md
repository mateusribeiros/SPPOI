Title: Relayer Aggregation Using Chainless Multi-Layer Consensus

ABSTRACT The increasing adoption of blockchain technology has underscored the need for crosschain systems that enable seamless communication among multiple BC networks. Achieving crosschain interoperability, which ensures secure and efficient data storage and transfer across BCs, remains
a critical technical challenge. Among existing solutions, the Inter-Blockchain Communication (IBC)
protocol within the Cosmos ecosystem is a prominent framework that facilitates cross-chain communication
using light clients and continuous monitoring. However, IBC faces limitations due to its reliance on the
consensus algorithms and block generation intervals of participating blockchains. Cross-chain transactions
are processed sequentially, requiring approval at each stage, which reduces efficiency. Furthermore, the
increasing number of relayers introduces scalability and operational challenges. To address these issues,
this study proposes a novel framework called Relayer Aggregation (RA), which aims to enhance cross-chain
communication by employing a chainless multi-layer consensus mechanism. RA enables parallel transaction
processing to improve performance and scalability. Experimental nodes were developed, and comparative
performance evaluations of RA and IBC were conducted to validate the proposed approach. The results
demonstrate that RA significantly reduces the number of required relayer nodes and enhances processing
efficiency through parallelization. By overcoming the sequential processing limitations of IBC, RA offers
a scalable and efficient solution for cross-chain interoperability. This study contributes to advancing
blockchain ecosystems by addressing key bottlenecks in cross-chain systems and providing a foundation
for future optimization in distributed environments.
INDEX TERMS Chainless interoperability, consensus algorithm, decentralization, inter-blockchain
communication, latency time, parachain, relayer aggregation, scalability, shared security
I. INTRODUCTION
Since the initial appearance of Bitcoin, various blockchain
(BC) projects have been proposed. The diversification of
cryptocurrencies has led to a growing demand for decentralized finance (DeFi), a system that enables the exchange
of multiple cryptocurrencies even between different types of
BCs. To achieve DeFi, cross-chain interoperability [1], which
is the ability of BCs to read and write information from
each other securely, is considered crucial. Recently, there
has been a focus on achieving cross-chain interoperability
in projects such as DeFi and improving shared security [2],
[3], with particular emphasis on platforms, such as Polkadot
[4] and Cosmos [5]. These platforms aim to organize the
proliferation of various BCs into an ecosystem framework.
Polkadot is referred to as the blockspace ecosystem [6],
and Cosmos is known as the interchain ecosystem [7].
The interchain ecosystem, which supports cross-chain interoperability, operates in parallel across multiple BCs and
is expected to address the scalability issues of BCs by
cooperating in transaction processing. Furthermore, Polkadot
and Cosmos have a relay or hub chain that supports shared
security across multiple BCs, known as parachains or zone
chains.
Polkadot’s relay chain establishes a complete parent-child
relationship with child parachains within the ecosystem. This
parent-child relationship remains intact, contradicting the
characteristic of decentralization, making it more centralized
compared to individual BCs. In the interchain ecosystem in Cosmos, an individual BC operates independently
without any hierarchical relationships between them. This
ecosystem aims to achieve interoperability through InterBlockchain Communication (IBC), which enables communication among BCs [8]. In the current intercahin ecosystem,
Cosmos IBC is conducted through a relay node (or a relayer);
however, there is a lack of shared security among most
BCs. Within the Cosmos network, there is a distinction
between hub BCs, which generally have more influence and
are responsible for hub chain, and non-hub BCs, which are
referred to as zone chain. Cosmos IBC establishes temporary
parent-child relationships, allowing validators from the hub
chain to support the validation of the zone chain [9]. Since
this is not a complete parent-child relationship, emerging
zone chains can become hub chains in the future, making
them decentralized compared to Polkadot. To achieve BC
interoperability through Cosmos IBC, nodes responsible for
relaying the block data are essential. The relayer use a
light client to periodically monitor the block headers of the
destination BC and ensure their validity, thus serving as a
secure node. This relayers have similarity to bridges, which
facilitate token bridging between two BC networks [10].
Therefore, the required number of relayer nodes is similar
to that of bridges. A minimum of one relayer is required for
each connection between the two BC networks. To connect
N BC networks, a minimum of N(N − 1)/2 relayers are
necessary. Therefore, having numerous relayers could lead
to concerns regarding network congestion. For regarding
bridges, the idea of bridge aggregation has been introduced
to consolidate multiple bridges [11]. In the future, a similar
approach may be required for relayers to properly aggregate
them, similar to bridges. This will be necessary for avoiding
network congestion. Therefore, we propose the concept of
relayer aggregation to consolidate the relayers using IBC
in existing BC ecosystems. In addition, as one method to
realize relayer aggregation, we propose using chainless multilayer consensus [12]. Chainless multi-layer consensus in a
upper-layered and semi-permissioned network can provide
an aggregation of the relayers required for IBC. Unlike
existing BC ecosystems that aim to achieve cross-chain
interoperability, bridges or relayers are not required for IBC.
As there is no need for a relay chain to integrate multiple
BCs, we refer to this as chainless multi-layer consensus.
In a previous research, nodes implementing a chainless
multi-layer consensus were used to establish a large-scale
peer-to-peer (P2P) network with over 100 parachains. The
previous research conducted a statistical evaluation of the
consensus latency time in a uniform environment where block
generation time intervals of all BCs for mining blocks are the
same to achieve multi-layer consensus[12], [13], [14]. In this
paper, we report our experimental results of the statistical
evaluation of consensus latency time in a non-uniform
environment where the block generation time intervals among
BC networks are asynchronous. Based on the experimental
results, we propose a method for determining multi-layer
consensus time intervals. Furthermore, we discuss incentive
designs for enhancing the willingness of more nodes to
participate in multi-layer consensus, and also consider
potential attack countermeasures that may be necessary for
the relayer aggregation. The main contributions of this paper
are as follows:
1) Building on the chainless multi-layer consensus proposed in previous research [12], we introduce a novel
Relayer Aggregation (RA) method that aggregates
multiple relayers through IBC.
2) Experiments 1 and 2 demonstrated a peak consensus
latency time of approximately 31 s, with a maximum
latency time of 33 s. This distribution reflects the
influence of the slowest block generation interval. Using
mathematical equations, we calculated the required
block generation interval to safely achieve chainless
multi-layer consensus, illustrating the necessary consensus preparation time.
3) Based on equations derived from experiments 1 and 2,
we identified detailed temporal trends and established
safe execution methods for chainless multi-layer consensus. Consequently, we developed a formula to estimate consensus latency across multiple BCs, applicable
even in scenarios where all parachains use Proof of Work
(PoW) or where mixed consensus algorithms, such as
PoW and Proof of Stake (PoS), coexist.
4) In experiment 3, we simulated multi-hop channels in
IBC and estimated the completion time for a three-hop
scenario. The results indicate that when information is
shared among three BCs, multi-hop channels require
75 to 200 s to complete processing. In contrast, when RA
is applied, even when propagated across 70 parachains,
processing completes in approximately 25 to 40 s,
demonstrating a reduction of at least 30 s. As the number
of propagated BCs increases, the benefits of RA become
even more pronounced.
5) The results of experiment 3 suggest that the primary
cause of performance degradation in IBC multi-hop
channels is sequential processing. Relayers process
transactions one at a time and cannot proceed to the next
hop until the previous hop is completed, making them
highly susceptible to communication latency and block
generation time variations, which lead to cumulative
processing latency time. In contrast, RA significantly
improves overall throughput by enabling multiple relayers to process packets in parallel. This approach is
similar to sharding, allowing load balancing among
relayers and facilitating parallel transaction processing.
6) We conducted a comparative analysis of decentralization
and security in chainless multi-layer consensus. The
findings suggest that adopting relayer aggregation with
chainless multi-layer consensus across multiple BC
networks enhances overall network security.
The remainder of this paper is organized as follows.
Section II outlines the related works of other interoperable
BC projects, such as Polkadot and Cosmos. In Section III,
we explain the general description of relayer aggregation
using chainless multi-layer consensus as a realization of
cross-chain interoperability. In Section IV, we review the
performance evaluation of chainless multi-layer consensus
where the block generation time intervals between parachains
are uniform. In Section V, we explain some experimental
results of chainless multi-layer consensus where the block
generation time intervals between parachains are nonuniform. In Section VI, we present experimental results
on the performance of multi-hop channels in IBC, where
transactions are relayed across multiple parachains. This
experiment evaluates the completion time of token transfers
in a three-hop scenario and compares the efficiency of multihop channels with relayer aggregation. In Section VII, we discuss a method to determine a multi-layer consensus latency
time interval, introduce an incentive design to boost node
participation, and highlight essential security considerations
for relayer aggregation. In Section VIII, we conclude our
proposal of relayer aggregation using chainless multi-layer
consensus and mention some future work to be addressed.
II. RELATED WORKS
A. POLKADOT
Polkadot [4], [15], [16] aimed to connect various BCs
including existing BC projects such as Ethereum [17], to
build an Internet of BCs. The main technical goal is to
achieve cross-chain interoperability, which enables secure
communication between multiple BCs. By default, Polkadot
has two types of BCs, i.e., the relay chain and parachains. The
relay chain is a centralized BC that aggregates information
regarding consensus throughout the system. The parachains
periodically sends its status to the relay chain. Therefore, the
relay chain ensures the security of the entire Polkadot system.
In Polkadot Ecosystem, there is a token called DOT that
supports security based on a modified PoS consensus to
control all nodes in the network based on incentives. The
consensus algorithm for the relay chain is called Nominated
PoS [18]. Parachains are BCs that operate as a part of the
entire Polkadot ecosystem by connecting to an empty slot in
the relay chain. Polkadot users can create applications and
execute smart contracts on parachains.
The cross-consensus message (XCM) format was proposed
to for transferring messages between multiple parachains
[19]. There are three types of the primary nodes called validator, nominator, and collator. The validator is responsible
for validating the parachain blocks [20]. The nominator is
responsible for selecting a legitimate validator for the system
to work properly [21]. The collator maintains parachains by
collecting parachain transactions from users and producing
state transition proofs for validators in the relay chain.
[22] Proper operation of these nodes keeps the relay chain
secure.
There is another type of node called fisherman. Rather
than packaging the state transitions and producing the next
parachain blocks as collators do, fishermen monitor this
process and ensure that no invalid state transitions are
included [23]. As of February 2023, no plan for implementing
fishermen has been made, and its abolition has been specified.
The extra fishermen mechanism will be abolished in favor of
increasing transaction processing speeds rather than security.
Originally, the inclusion of a special fishermen-like role to
report fraud to an entity separate from the validator and
punish rogue nodes was considered necessary if the security
should be enforced.
However, a relay chain can be the single point of failure
because it ensures the security of the entire system. According
to a statement by Polkadot [24], on May 24, 2021, when
creating a block that contained a large election result,
the system crashed because of an out-of-memory error,
which affected the entire system. An empirical analysis
and verification of the validator election data collected
from Polkadot BC were also conducted [25]. Being a
validator of the relay chain network requires expensive DOT
funding and is reportedly structured such that the monetary
power is biased toward a small number of extensive DOT
holders. Therefore, some researchers have mentioned that
the governance in Polkadot is not decentralized and must be
improved [26], [27].
B. COSMOS
Cosmos [28] is a collective network of BCs operated by
Cosmos SDK [29]. Network communication between BCs
aims to establish cross-chain interoperability by communicating the Cosmos IBC (IBC [8]) with each other through
relayers that relay IBC packets. Cosmos creates a network
consisting of a hub chain and zone chains. The role of nodes
joining in the Cosmos ecosystem has not been determined
compared to that in the Polkadot ecosystem. Consequently,
a strong BC with relatively high security and numerous IBCs
became the hub chain, whereas other BCs became zone
chains. In the Cosmos hub chain, ATOM token is issued, and
the consensus algorithm is supported by the delegated PoS
[30] based on the ATOM token. The tokens are transferred
via the hub chain that tracks the total number of tokens held
by each zone. Zone chains connected to the same hub chain
can provide cross-chain interoperability. The current Cosmos
IBC specializes only in DeFi and lacks implementations
of shared security. The Cosmos hub announced replicated
security [31] (formerly known as interchain security v1 [32])
and is leading the development of Cosmos shared security.
Replicated security has been introduced and used in neutron
[33] and performs cross-chain validation (CCV [34]), which
doubles as a consumer chain [35] validator where all of the
Cosmos hub validators benefit from the security. This will
allow the newly launched BC to be as resilient based on thesecurity from the Cosmos hub. If a validator in Cosmos cheats
other validators, it will slash the staked ATOM token on the
Cosmos hub. In the Cosmos ecosystem, shared security will
continue to be developed as opt-in security to enhances the
security in both the zone and hub chains [9].
C. ANALYSIS OF IBC ON THE COSMOS MAINNET
Reference [36] provides an evaluation of the processing
performance of IBC token transfers within the Cosmos
Ecosystem. In the research, conducted over a 24-hour period
on June 1, 2022, analyzed 1,000 IBC token transfer Txs and
reported an average Tx interval of 86.4 s.
The analysis specifically focused on token transfers
between the Osmosis [37] mainnet and the Cosmos Hub
mainnet [5], examining the exchange of OSMO tokens for
ATOM tokens. These findings serve as a baseline for the
experiments conducted in this study, providing a comparative
reference point for evaluating the performance improvements
and changes observed in the IBC protocol since the previous
research.
D. ANALYSIS TOOLS AND EXPERIMENTAL RESULTS FOR
IBC IN PRIVATE TESTNETS
Reference [38] develops an analysis tool that operates in a
local network environment to evaluate the performance of
the IBC protocol under various scenarios and conduct experiments. Based on these experiments, three key performance
metrics throughput, latency time, and relayer scalability were
used to identify factors affecting IBC performance.
The experimental results revealed a critical issue: increased
latency time in IBC transaction confirmation due to the
relayer. Additionally, several other challenges were identified, including inefficiencies in RPC operations, limitations
in relayer scalability, transaction processing latency time,
and difficulties in maintaining data consistency during crosschain operation failures. These issues pose significant risks
to the performance and reliability of the IBC protocol.
III. GENERAL DESCRIPTION OF CHAINLESS
MULTI-LAYER CONSENSUS
In this section, we explain chainless multi-layer consensus
which is a method proposed in our previous research to realize
cross-chain interoperability. Chainless multi-layer consensus
consists of two network layers as illustrated in Fig. 1. These
two network layers comprise a two-layer network structure
with Layers 0 and 1 where BCs exist only in Layer 1 and
they are interconnected via Layer 0. We also conducted some
performance evaluations by comparing with Polkadot and
Cosmos which also have two-layer network structures.
A. CHAINLESS MULTI-LAYER CONSENSUS
As introduced in Section II-A, Polkadot has a centralized
BC called a relay chain. In this research, we refer to the
consensus algorithm to achieve cross-chain interoperability
in BC systems, such as Polkadot and Cosmos, as relaychain-based multi-layer consensus or simply relay-chain
FIGURE 1. Schematic diagram of multi-layer P2P network of a chainless
type.
FIGURE 2. Schematic diagram of multi-layer P2P network in relay-chain
type.
type. A schematic of the multi-layer P2P network in the
relay-chain type is shown in Fig. 2. In general, a relaychain-based multi-layer consensus has multiple BCs, called
parachains in the lower layer, called Layer 1, which are
integrated into the relay chain in the upper layer, called Layer
0. Consensus information between parachains is integrated
into the relay chain, as shown in Fig. 3, which is essential
not only to enhance cross-chain interoperability but also to
improve scalability.
B. COMPARISON WITH MULTI-LAYER CONSENSUS
In this section, we compare multi-layer consensus solutions
between the consensus algorithms in Polkadot and Cosmos,
and the chainless multi-layer consensus. At the end of 2022,
the consensus latency time for the Polkadot relay chain
was reportedly 6 s [39], whereas that for a Cosmos hub
chain is 7 s [40]. To facilitate a straightforward comparison,
we assume that the number of parachains and scalability
capabilities within each ecosystem are equal. Figs. 4 and 5
present diagrams comparing the decentralization of each
ecosystem in Fig. 4 and shared security in Fig. 5. The
Polkadot ecosystem relies on the relay chain to support the
security of the entire parachain. Therefore, it provides tamper
resistance with a security of relay chain and parachains
combined. The decentralization of Polkadot is achieved
through the complete parent-child relationship formed by
the relay chain with the child parachains within the parent
BC. This parent-child relationship remains unclear, and the
security of the relay chain is integral to the overall security
of the Polkadot ecosystem. This feature contradicts general
ideas that emphasize decentralization in BCs and results in
the centralization of BC.
In a Cosmos ecosystem, each BC operates independently
with its governance and security, and there are no dependencies between individual BCs. In the current Cosmos
ecosystem, there is minimal security sharing among most
BCs, and each BC’s security is self-contained. Temporary
parent-child relationships are established with allowing
validators from the hub chain to support validators from
zone chains [9]. Consequently, BCs that do not have such
relationships have tamper resistance equivalent to that of a
single BC. Since these relationships are not fully parent-child,
there is a possibility that emerging zone chains in the future
could become hub chains, making the Cosmos comparatively
less centralized compared to Polkadot. Chainless multilayer consensus, like the Cosmos ecosystem, operates
FIGURE 5. Security comparison of multi-Layer consensus.
TABLE 1. Comparison of Blockchain communication mechanisms.
independently with separate BCs without any hierarchical
dependencies to foster a cooperative relationship for shared
security. This security sharing does not depend on the security
of any specific strong BC, theoretically enhancing the security across all BCs. Therefore, unlike centralized ecosystems
that aggregate consensus information for the entire system
in a specific BC, such as Polkadot or Cosmos, this consensus
information is distributed and managed separately in each BC
using a shared multi-layer consensus part in each common
block in multiple BCs. Therefore, chainless multi-layer
consensus is a more decentralized ecosystem compared to
the Polkadot ecosystem, and cooperation with the Cosmos
ecosystem enhances tamper resistance.
Table 1 compares BC communication mechanisms in
Cosmos, RA (Relayer Aggregation), and Polkadot based
on their mediator type, decentralization, tamper resistance,
required mediator nodes, and parallel transaction processing.
Cosmos uses relayers to facilitate IBC, whereas RA introduces super relayers, which integrate relaying and consensus
functions. Polkadot employs a relay chain that combines
relaying and BC functionalities. Regarding decentralization,
Cosmos exhibits high decentralization, as each BC (Zone)
operates independently. RA achieves a moderate level of
decentralization due to its reliance on super relayers, while
Polkadot has low decentralization since parachains depend
on the relay chain for transaction finalization.
In terms of tamper resistance, RA provides strong protection, Polkadot offers a medium level, and Cosmos is
considered weak, mainly due to its reliance on independent
relayers. In terms of scalability, Cosmos requires O(N
2
)
mediator nodes due to its peer-to-peer relayer system,
whereas RA improves efficiency with O(N) nodes. Polkadot
is the most efficient in this aspect, requiring only O(1)
mediator node through its relay chain structure.
All three systems support O(N) parallel transaction
processing, enabling them to efficiently handle multiple
BC operations simultaneously. However, RA demonstrates
superior cross-chain communication efficiency compared to
Cosmos due to its optimized relayer aggregation mechanism,
which reduces redundant message transfers and improves
overall network responsiveness. While RA offers enhanced
tamper resistance compared to Polkadot, its dependence
on super relayers may introduce potential bottlenecks and
reduce overall decentralization compared to Cosmos’s fully
independent relayer network.
C. BLOCKCHAIN COMMUNICATION USING RELAYERS
To understand the benefits of our chainless multi-layer
consensus, it is essential to first examine Cosmos IBC
with existing relayers. This section describes how BC
communication occurs in Cosmos IBC using relayers.
Fig. 6 provides an overview of the Cosmos network.
Although numerous BCs operate within the Cosmos ecosystem, for simplicity, the illustration assumes communication
between three BCs. The token exchange process from Zone
Chain 1 to Zone Chain 2 via the Hub Chain follows the steps
below.
The token transfer process consists of two phases:
1) Transferring from Zone Chain 1 to the Hub Chain, and
2) Transferring from the Hub Chain to Zone Chain 2. The
detailed steps are as follows:
1) Transfer from Zone Chain 1 to the Hub Chain
Sequence 1: (1-A) A transaction request is initiated for
the transfer of tokens from Zone Chain 1. Zone Chain
1 records the request in a block. A relayer transfers
the request to the Hub Chain.
Sequence 2: (1-B) The Hub Chain verifies the request
and records it in a block. Tokens are issued on the
Hub Chain. An acknowledgment is sent from the Hub
Chain to Zone Chain 1 via the relayer.
2) Transfer from the Hub Chain to Zone Chain 2
Sequence 3: (2-A) A transaction request is initiated on
the Hub Chain for the token transfer. The Hub Chain
records the request in a block. A relayer transfers the
request to Zone Chain 2.
Sequence 4: (2-B) Zone Chain 2 verifies the request
and records it in a block. Tokens are issued on Zone
Chain 2. A confirmation response is sent from Zone
Chain 2 to the Hub Chain.
D. RELAYER AGGREGATION
The communication structure of Cosmos IBC relayers and
relayer aggregation using chainless multi-layer consensus
is illustrated in Fig. 7. Similar to bridges between BCs,
relayers are required whenever connecting two BCs, and at
FIGURE 6. Cosmos IBC using relayers.
FIGURE 7. Communication Overview Diagram of Relayer Aggregation
(RA).
least N(N − 1)/2 bridges or relayers are needed to connect
N different BCs. Consequently, the number of relayers
can become substantial, leading to concerns about network
congestion.
The concept of bridge aggregation, which aims to consolidate bridges, has been proposed [11]. However, no proposals
or considerations have been made regarding the organization
of relayers in the context of IBC. In the future, relayers
may also encounter network congestion issues, necessitating
improvements. Chainless multi-layer consensus can help
mitigate network congestion in communication between BCs.
By leveraging this consensus mechanism, relayer aggregation
can be achieved.
Although relayer aggregation is also possible within
the Cosmos ecosystem, a large number of relayers may
concentrate on the hub chain, particularly when it serves as a
central node for token exchanges. Additionally, an incentive
mechanism for relayers is under consideration [41]. If this
incentive is implemented, an influx of relayers into the
ecosystem could further exacerbate network congestion
unless relayer aggregation is effectively implemented.
E. MULTI-HOP CHANNELS IN IBC
Based on information from [42] (last updated in November
2023) and [43], we provide an explanation of multi-hop
channels in IBC. Currently, IBC connections operate on a
one-to-one basis through IBC channels. However, with multihop channels, IBC connections transition to a 1:N structure.
This enhancement is expected to improve network efficiency,
throughput, and processing capacity while enabling direct
communication with all BCs.
At present, multi-hop channels remain in the proposal stage
and aim to address several challenges. As the number of
IBC connections within the Cosmos Ecosystem increases,
the required number of relayer nodes also rises, potentially
leading to a decline in the ecosystem’s overall TPS.
Therefore, further modifications to the IBC protocol are
considered necessary to enhance performance, scalability,
and interoperability.
With the expansion of the Cosmos Ecosystem, the introduction of multi-hop channels has been proposed as a method
for routing messages between different IBC-compatible BCs
by leveraging multiple existing IBC connections. In IBC
with multi-hop channels, a mechanism is introduced to
define IBC channels using pre-existing IBC connections.
The primary advantages of this method include improved
inter-chain connectivity and a reduction in the number
of required IBC connections. As a result, it facilitates
connection aggregation and enables more efficient routing
within the Cosmos Ecosystem. Additionally, as the number
of connections and channels increases, the load on chains
such as OSMOSIS [37] and Cosmos Hub may also rise,
potentially impacting scalability. As the Cosmos Ecosystem
continues to expand, concerns arise that this could strain
the processing capacity for other transactions. Multi-hop
channels are expected to help mitigate this processing
load.
In this paper, Section VI presents a simplified implementation of multi-hop channels and compares the results with
those from experiment 2.
F. DETAILED DESCRIPTION OF CHAINLESS MULTI-LAYER
CONSENSUS
In the previous research, we have proposed a chainless multilayer consensus or a chainless type. A schematic diagram
of the multi-layer P2P network in the proposed consensus
between parachains without any relay chain is shown in
Fig. 1. Compared with a relay-chain-based multi-layer
consensus, the chainless type does not have centralized BC
that integrates the consensus information of the parachains.
The consensus information is managed in a decentralized
manner by the shared multi-layer consensus part in the blocks
of every parachain. In a chainless type, similar to the relaychain type, the P2P network structure consists of two layers:
Layer 0 and Layer 1. In Layer 1, the parachains from a local
consensus. In Layer 0, to realize interoperability, the leader
nodes elected from each parachain nodes form a P2P network.
A schematic diagram of multi-layer consensus blocks in a
chainless type is shown in Fig. 8. The block structure of
the multi-layer consensus block in a chainless type is shown
in Fig. 9. The block structure consists of two parts. Existing block structure part and shared multi-layer consensus
part.
A typical system with a chainless multi-layer consensus
was constructed using a combination of a public-type
FIGURE 8. Multi-layer consensus blocks in chainless type.
FIGURE 9. Block structure of chainless type.
consensus algorithm in Layer 1 and a consortium-type
algorithm in Layer 0. A chainless consensus algorithm is
possible because a consortium-type consensus algorithm
does not necessarily require a BC. Because there is no
relay chain in a chainless type, the multi-layer consensus
part in the blocks of the parachains shares the consensus
information of all parachains. For this reason, the size of
the BC tended to increase faster than that of the relay chain
type.
Furthermore, in the chainless type, a parachain does not
have to participate in every consensus to avoid deadlock
owing to a lack of quorum in the consensus process. The
shared multi-layer consensus part also contributed to an
improvement in the tamper resistance of the parachains.
To tamper with a parachain, malicious attackers must tamper
not only with the parachain but also with the shared consensus
part in the other parachains.
A chainless multi-layer consensus between two parachains
can also be interpreted as an extended concept of a bridge,
in which two BCs are directly interconnected without using a
relay chain. By extending the bridge or relayer to connect N
BCs, it is necessary to prepare N(N −1)/2 bridges or relayers
to interconnect any two BCs. Therefore, a chainless multilayer consensus between N parachains must be equivalent to
N(N − 1)/2 bridges or relayers placed together into a single
P2P network.
TABLE 2. The process used to create a consensus in chainless type.
G. HYSTERESIS SIGNATURE
A hysteresis signature [44], [45] is used to generate signatures
by nesting the previous signatures. The structure of the
hysteresis signature is given by Eq. (1).
Sm = Sig(H(Sm−1||H(B1)|| . . . ||H(BN ))) (1)
where H(B1), · · · , H(BN ) are the hash values of blocks
(B1, · · · , BN ) including a shared multi-layer consensus part
from N parachains, and H(Sm−1) is the hash value of
the previous hysteresis signature Sm−1. These hash values
were concatenated and signed to create the next hysteresis
signature.
H. RAFT CONSENSUS ALGORITHM
In the chainless type, leader nodes selected from the
parachains are required in Layer 0 to achieve a consensus.
In this paper, to implement our node program, we selected
the Raft consensus algorithm (Raft) [46] as a consortiumtype consensus algorithm in Layer 0. Raft is not resistant to
Byzantine damage, meaning that it is feasible to interfere with
the leader election for log tampering. If Byzantine resistance
is required, another consensus algorithm such as PBFT [47],
[48] must be selected.
I. NETWORK PROTOCOL
The process used to achieve a consensus consisted of two
phases, as shown in Table 2. We designed communication
protocols between parachains for a chainless multi-layer
consensus and introduced two latency times T1 and T2 as
evaluation measures in phases 1 and 2, as shown in Fig. 10.
J. PREPARATION PHASE (PHASE 1)
In the chainless type, the consensus information cannot be
aggregated into the relay chain, and must be distributed to the
parachains to be recorded in the shared multi-layer consensus
part of the blocks, as shown in Fig. 9. Therefore, crosschain communications used to prepare the shared multilayer consensus part and achieve consensus are required.
Therefore, we introduced consensus preparation time T1 to
evaluate the latency time for sharing consensus information.
Consensus preparation time T1 is directly linked to the
performance of the chainless multi-layer consensus.
FIGURE 10. Schematic overview of communication protocols between
parachainsand two latency times T1 and T2 as evaluation measuresin
phases 1 and 2.
K. CONSENSUS PHASE (PHASE 2)
In Polkadot and Cosmos, the consensus latency time of
the entire system largely depends on the block generation
time interval in PoS as shown in Fig. 3. In contrast, in the
chainless type, the shared multi-layer consensus part must
be fixed in the latest blocks of the parachains to complete
the consensus. Therefore, we define the consensus latency
time in the chainless type as the latency time required
to finish creating the latest blocks, including the shared
multi-layer consensus part, in all parachains that participate
in the consensus. Therefore, we introduce the consensus
latency time T2 to evaluate the latency time and finalize the
consensus information after Phase 1, as shown in Fig. 8. The
consensus latency time, denoted by T2, depends on the block
generation time intervals of the lower-layer BCs. Estimating
the consensus latency time for ecosystems consisting of PoSbased consensus algorithms, such as Polkadot and Cosmos,
are relatively easy because the block generation time intervals
are uniform and highly controlled to synchronize the time
intervals in general. However, it is not so easy to estimate the
consensus latency time in which PoW and PoS BCs coexist,
for example, when we consider to connect Bitcoin and
Ethereum 2 using relayer. Therefore, we must experimentally
evaluate relayer aggregation in an environment where PoW
and PoS BCs are mixed and estimate the time in a relayer
aggregation network with significant variations in block
generation time intervals. In this paper, to evaluate the
consensus latency time in any environment, experiments were
conducted under some worst-case scenarios that chainless
multi-layer consensus is realized between only multiple PoW
BCs.
L. PERFORMANCE EVALUATION MEASURE
We considered the latency times of the preparation and
consensus phases. We also introduced the total latency time
T1 + T2, which will be evaluated experimentally later. If the
total latency time is short, the chainless multi-layer consensus
can be safely completed in short time intervals, which also
results in a high transaction-processing speed. We ran a
single node for Layers 0 and 1, and established a P2P
network for Layer 0. In Layer 0, we implemented nodes
to mine blocks, including a shared multi-layer consensus
part, using PoW and recorded them in the BC, with the
consensus content transferred from Layer 1. To evaluate the
consensus in Layer 0 with multiple nodes experimentally,
we limited each Layer 1 to only one node. We conducted two
experimental evaluations to measure the latency times in a
chainless multi-layer consensus. To do this, we implemented
our experimental node using Python3 ,1 which can achieve a
consensus among numerous parachains.
IV. PERFORMANCE EVALUATION 1
The purpose of experiment 1 is to verify whether consensus
can be achieved between BCs when RA is implemented,
and to confirm whether the implemented nodes function
correctly. Performance evaluation 1 examines the trend in
consensus latency time as the number of network parachains
increases. In this section, we report the settings and results of
experiment 1.
A. SETTINGS OF EXPERIMENT 1
Details on the PC specifications used in the experiments are
shown in Table 3. If the number of parachains, N is large,
multiple nodes must coexist on the same machine. This means
that they compete to obtain computing resources, which
generally results in the degradation of the block-creation
process.
TABLE 3. PC performance, etc.
FIGURE 11. Schematic overview of network configuration in the
experiments.
A schematic of the network configuration used in the
experiments is shown in Fig. 11. Basically, one node is
representative of the parachain. A maximum of 26 PCs were
used for the experiments. When the number of parachains
1https://github.com/cit-fujihalab/Chainless-Interoperability-Node
exceeded N > 26 machines, multiple nodes were launched
simultaneously on the same machine. A maximum N of
216 parachains was used in the experiments. We adopted
PoW as the consensus algorithm to create a block in the
parachain. We attempted to create the same environment to
divide the nodes equally on each machine. Table 4 lists the
experimental parameters. Each node running both Layers
0 and 1 is executed, and a P2P network is established in
Layer 0. In addition, in Layer 0, nodes are implemented
to mine blocks, including the multi-layer consensus part,
using PoW for consensus content transfer from Layer 1,
and recording them in the BC. To experimentally evaluate
the Layer 0 consensus with multiple nodes, only one node
was assigned to each Layer 1. Table 4 lists values that
were changed for evaluation in the experiment, including the
number of nodes and the multi-layer consensus interval. The
block generation difficulty was set as the basic configuration
with a value of 1[0x], which implies setting the block
header with the first digit in the hexadecimal space as 0 as
the target value. Launching multiple nodes simultaneously
on the same PC involves sharing the processing capacity
of one PC among a several nodes being run, depending
on the processing capacity of the experimental machine.
Therefore, to minimize computational processing in block
mining, a lower value was set for the block generation
difficulty. A block non-generation interval was provided to
reduce the processing load on the experimental machine and
to distribute the mining of blocks as a distributed process.
This is equivalent to the block generation time interval and
can therefore be converted into a block generation time
interval. In addition, the effects of communication latency
depending on the geographical distance between nodes and
the heterogeneity of the communication infrastructure based
on machine specifications were not considered, and all nodes
were deployed in the same LAN. We compared the latency
times by changing the number of parachains and block nongeneration time intervals. The mining difficulty is set to
one, meaning that the first 16 digits in the hash value of a
block header become zero when it is set as the target value.
We also compared the performance under two scenarios:
one with a block non-generation time interval of 0.5 s for
fewer computing resources, and another with a block nongeneration time interval of 5 s for more computing resources.
TABLE 4. List of various setting values used in experiment 1.
B. RESULTS OF LATENCY TIME IN PHASE 1
In the first experiment, we evaluated the consensus preparation time, T1, as shown in Fig. 10. The measurement time of
T1 for a typical node is shown in Fig. 12, and the histogram
of the measured T1 for all the nodes, where N = 126, and
the block non-generation time interval was 5 s, as shown in
Fig. 13. As shown in Fig. 12, T1 remains at approximately
2.5 s. We also found that T1 showed a similar trend over
time, although the average values differed for each node. The
average varied between nodes, from 2.5−15 s. The histogram
in Fig. 13 confirms this result, showing significant variance.
We extracted the inflection point as well as the upper and
lower bounds of the histogram of T1 for each N, and show the
relationship between them in Fig. 14. The double-logarithmic
plot in Fig. 14 indicates that T1 increases superlinearly with
increasing N, that is,
T1 ∝ N
α
, (2)
where α > 1 is the power exponent and is equivalent
to a slope value with a double-logarithmic plot. We also
summarize the estimated value of α from the experiments in
Table 5.
C. RESULTS OF LATENCY TIME IN PHASE 2
In the experiment 2, we evaluated the consensus latency
time T2, as shown in Fig. 10, which shows a typical
FIGURE 14. Relationship between N and T1
in a double-logarithmic plot.
TABLE 5. Each power exponent of Phase 1 with a block non-generation
time interval of 0.5, 5 [s] by Evaluation 1 results.
FIGURE 15. Consensus latency time T2 distribution.
histogram of the measured T2 for all nodes in Fig. 15.
That distribution appears to have a single peak, as shown
in Fig. 15. We extracted the peak point as well as the
upper and lower bounds of the histogram of T2 for each
N, and show the relationship between them in Figs. 16
and 17. The double-logarithmic plot in Fig. 16 indicates that
T2 increases superlinearly with an increase in N if the block
non-generation time interval is 0.5 s, that is,
T2 ∝ N
β
, (3)
where β > 1 is the power exponent. By contrast, the
double-logarithmic plot in Fig. 17 indicates that T2 increases
sublinearly, that is, β < 1 with an increase in N if the block
non-generation time interval is 5 s. We also summarize the
estimated value of β from the experiments in Table 6. In
Fig. 17, the data points do not fit the slope line well, and the
trends appear to differ at approximately N = 30 parachains
as boundaries. Please recall that the number of machines was
26, which is close to 30. If N ≤ 26, each node can occupy
all computing resources of a single machines, resulting in a
sublinear trend. In contrast if N > 26 multiple nodes share
the computing resources of a single machine, resulting in
a superlinear trend. This phenomenon occurs because our
node program fixes the mining difficulty and does not have
difficulty adjusting the algorithm to generate blocks, which
is considered to significantly impact the relationship between
N and T2.
V. PERFORMANCE EVALUATION 2
The purpose of experiment 2 is to verify whether the
cross-chain interoperability processing speed increases when
using RA. In this experiment 2, we estimate the multi-layer
consensus time interval where the block generation time
intervals in lower-layer BCs, denoted as T2, are different.
TABLE 7. List of various setting values used in experiment 2.
FIGURE 18. Time series of T1
in a typical node.
To achieve this, we randomly select block generation time
intervals for each BC.
A. SETTINGS OF EXPERIMENT 2
The detailed specifications of the PCs used in the experiment
2 and the network configuration were the same as those used
in the previous experiment 1, as shown in Table 3 and Fig. 11.
The difficulty level for block mining was set to a low value to
minimize computational processing in block mining. A block
non-generation time interval was introduced to distribute the
block mining process to reduce the processing load on the
machines used in the experiment and was set to be equivalent
to the block generation time interval. Therefore, they can be
converted into block generation time interval. The settings
used in the experiment 2 are shown in Table 7.
B. RESULTS OF LATENCY TIME IN PHASE 1
Fig. 18 shows the consensus preparation time T1 for the
experimental 2 settings in section V-A. According to Figs. 18
and 19, we can observe that the consensus preparation time
for all nodes was generally approximately 1 − 7 s in terms of
the block non-generation time.
C. RESULTS OF LATENCY TIME IN PHASE 2
The results in this experimental 2 are represented by the
measured consensus latency time, T2 shown in Fig. 20.
The distribution of the consensus latency time, T2, showed
a peak around the center, resembling a mountain-shaped
distribution. In the experiment 2, the distribution was centered
around a block non-generation time interval of approximately
31 s, and the maximum consensus latency time T2 reached
approximately 33 s, which is influenced by the consensus
latency time of chainless multi-layer consensus in this
settings.
VI. PERFORMANCE EVALUATION 3
In this chapter, we implement a simplified version of multihop channels, as described in Section III-E, calculate the
completion time of IBC multi-hop channels proposed as an
additional feature of IBC, and compare the results with those
from experiment 2. The objective of this experiment is to
evaluate how processing time changes as the number of hops
increases and to compare it with RA.
The block generation time interval was set to 5 s for
OSMOSIS and 7 s for Cosmos Hub, based on [36].
In this experiment, we simulated the IBC of OSMOSIS
(OSMO) [37] and Cosmos Hub (ATOM) using the obtained
dataset.
A. SETTINGS OF EXPERIMENT 3
The detailed specifications of the PC and network configuration used in experiment 3 are the same as those in experiments
1 and 2 and are shown in Table 3. Additionally, the experimental conditions used in experiment 3 are summarized in
Table 8. In experiment 3, IBC was executed 1000 times,
and an approximate PoS model was adopted as the block
TABLE 8. Details of experimental conditions.
FIGURE 21. Time measurement and flow in IBC.
generation algorithm to measure the IBC completion time.
The time measurement interval in experiment 3 is as shown
in Fig. 21.
The IBC transaction transmission interval was set to 86.4 s
to ensure consistent time gaps between transactions. The
verification hop count J, representing the number of hops
involved in the verification process, was set to 1 and 3. The
experiments were conducted on a single PC, maintaining
a controlled environment for evaluating performance and
efficiency. These conditions were chosen to simulate a
realistic but manageable IBC environment while assessing
the impact of hop count on transaction processing.
B. RESULTS OF IBC MULTI-HOP CHANNELS
The experimental dataset accounts for communication
latency and the possibility of transactions remaining in the
Tx pool due to validator discretion. As a result of conducting
IBC under these conditions, we obtained the data shown in
Fig. 22. A comparison with Fig. 16 in [36] confirms that
Fig. 22 exhibits similar characteristics.
Using the same sampling method as in Fig. 22, we estimated the distribution of multi-hop channels processing times
for J = 3 between BCs with block processing performance
comparable to that of Cosmos Hub. The results are shown
in Fig. 23. For three hops, the average IBC completion time
is approximately 125 s, nearly twice as long as that for
a single hop, which takes around 60 s. Fig. 22 has been
confirmed to exhibit characteristics similar to Fig. 16 in [36].
Based on the parameter settings of this sampling analysis,
it was observed that the current mainnet IBC in Cosmos
is significantly affected by communication latency and the
latency time before validators accept block information.
Furthermore, when comparing the results of experiment 3
with those of RA, the block generation process for communication and information exchange between BCs follows
a sequential approach in IBC, as shown in Fig. 21.As the
number of hops and parachains increases, IBC transfer time
is expected to increase.
This issue leads to cumulative latency, suggesting that even
if multi-hop channels become feasible, significantly reducing
overall latency time would be challenging.
Based on this estimation, reducing the time required
for sequential processing across multiple BCs is difficult,
emphasizing the necessity of an IBC transaction parallel
processing mechanism like RA, as shown in Fig. 10.
VII. DISCUSSION
Previous researches conducted experimental evaluations
assuming mainly the environment of uniform block generation time intervals, such as the performance evaluation
1. In the previous experimental results, we confirmed that
the block generation time interval for the entire network
is influenced by the BC having the slowest block generation time interval, which requires to make the chainless
multi-layer consensus safely executed for all the BCs.
Therefore, chainless multi-layer consensus becomes slower
compared that of existing interoperable BC projects, such
as Polkadot and Cosmos. However, it is possible to make
consensus between completely different types of BC, such
as Bitcoin and Ethereum 2, in Layer 1 by estimating an
appropriate block generation time interval. We will explain
how to do this later.
A. MULTI-LAYER CONSENSUS INTERVAL IN THE CASE OF
NON-UNIFORM BLOCK GENERATION TIME INTERVALS
The process of selecting a leader and determining roles
at the initialization of the system, as well as setting the
multi-layer consensus time interval, is depicted in Fig. 24.
Fig. 25 illustrates the process of determining the multi-layer
consensus interval when new connecting nodes managing
their own BC are added to the same BC ecosystem. The
process in the event of leader failure, the expiration of
a leader’s term, or other circumstances requiring a new
election are shown in Fig. 26. Furthermore, all elections,
including leader selection, are conducted using the Raft
consensus algorithm mechanism, as described in Raft [46].
In Fig. 24, the roles determined at system start-up represent
the leader, follower, and observer, respectively. The leader is
crucial in the chainless multi-layer consensus by providing
leadership. However, followers have the role of cooperating
in a multi-layer consensus while monitoring the leader’s
availability and can become leaders themselves. Observers,
while able to participate in the multi-layer consensus, do not
influence participating in Raft elections or exert a significant
influence on the system. The determination of the multi-layer
consensus time interval is highly influenced by the block
generation time; therefore, when configuring the multi-layer
consensus time interval, a threshold is set with respect
to the block generation time interval I. When the block
generation time interval I is significantly slow, the nodes
are excluded in advance by the threshold G. Nodes that
have been excluded by the threshold can participate as
observers and may not participate in multi-layer consensus
every time, but they can sporadically participate in multilayer consensus, benefiting the improved tamper resistance
of Layer 1 BC. Observers can participate in the chainless
multi-layer consensus block but cannot receive incentives.
To receive the incentives mentioned in Section VII-A, the
nodes must improve to maintain the block generation time
interval within the threshold G during the trial period.
To become a core participant, new Layer 0 nodes must
initially join as observers, and to become a core participant,
they must participate in a certain number of multi-layer
consensus rounds. By verifying the time spent, one can
join the network’s core leader election and become either
a follower or leader. Therefore, while Polkadot requires
a significant investment in governance tokens (DOT) to
participate in the core, the chainless multi-layer consensus
prioritizes decentralization and provides incentives to BCs
that have contributed to multi-layer consensus for a certain
period.
B. INCENTIVE DESIGN FOR RELAYER AGGREGATION
The effectiveness of incentives stems from the need to
induce trustless entities, similar to the Bitcoin BC block
generation incentives, to maintain the system. In previous
research, there were no incentives designed for the creation of
multi-layer consensus blocks in Layer 0. Providing incentives
to generate a multi-layer consensus part in Layer 0 is
expected to encourage more multi-layer consensus parts
to be written to multiple BCs. When designing incentives
for Layer 0, there is a potential vulnerability to attacks
on nodes that receive incentives and the mechanism for
granting those incentives. Providing incentives to specific
designated nodes such as leaders may lead to competition for
more incentives, which could disrupt the cooperative state
of the multi-layer consensus. Therefore, it is desirable to
FIGURE 25. Action on newly connected nodes.
distribute the incentives equally for activities occurring in
Layer 0. In this discussion, we assume an equal distribution
for mining the multi-layer consensus blocks. We illustrate
the block structure with an added coin-base incentive block
part for equal distribution in Fig. 27. To safely share a
shared multi-layer consensus part, and trust is required in
the information handled by leaders and followers. If the
information within a network composed of Raft consensus
algorithms is not trusted, it may need to be replaced with a
consensus algorithm such as PBFT. If security is prioritized
over the transaction processing speed, even at the cost of
performance, we must consider changing the consensus
algorithm, such as by opting for a PBFT with Byzantine fault
tolerance. Selecting PBFT with Byzantine fault tolerance
increases communication overhead, sacrifices processing
capacity, and creates a trade-off between processing capacity
and security.
C. COMPARISON OF CONSENSUS TIME IN BLOCK
GENERATION
In the chainless multi-layer consensus, each BC multi-layer
consensus part holds consensus information for the entire
ecosystem, which implies that it is influenced by the
block generation time of Phase 2’s Layer 1 BC. The
block generation algorithms for multi-layer consensus in
the Cosmos hub and relay chain (Polkadot) use DPoS or
PoS with an average block generation time interval of 6 or
7 s [39], [40]. The block generation time interval of the
underlying BC consensus algorithm depends on this interval.
In Fig. 28 we show the distribution of block generation time
intervals for Ethereum 2, which has transitioned to PoS,
obtained from Etherscan [49], Fig. 28 shows, that the block
generation time interval in the PoS varies slightly, with values
ranging from approximately 12 to 13 s, with most being
approximately 12 s. Therefore, the block generation time
in a multi-layer consensus for PoS-based BCs is generally
stable and straightforward. In this experiment, we conducted
tests on a network composed of PoW-based BCs, which
are non-obvious and unstable. Additionally, in the chainless
multi-layer consensus Phase 2, adopting PoS is expected to
provide similar performance, with the trade-off of higher
resistance to tampering and greater decentralization of
FIGURE 27. A block structure that provides incentives.
FIGURE 28. Block generation time interval in PoS (Ethereum 2.0).
multi-layer consensus information compared with latency in
Phase 1. The formula estimating the consensus latency time
(CLT) is given in Eq. (4).
CLT = T1 + 2 × max{TPoW,1, · · · , TPoW,m1
,
TPoS,1, · · · , TPoS,m2
} [s], (4)
where TPoS,i and TPoW,i are latency times for finishing PoS
and PoW consensus safely, respectively. m1 and m2 are
the total numbers of BCs having the consensus algorithms
of which are PoW and PoS, respectively. In Eq. (4), the
coefficient of the second term is doubled (2×) because it
allows more buffer time to safely complete the consensus in
case that the block generation timing for the consensus shifts
asynchronously. The chainless multi-layer consensus uses
previous multi-layer consensus information; therefore, the
chainless multi-layer consensus block part must consistently
be synchronized. Considering the case in which complete
synchronization is not achieved, this factor is estimated
to be twice the block generation time interval. The block
generation time intervals in the block generation time interval
of PoW generally follow an exponential distribution [50],
making them more difficult to control than in PoS and
resulting in higher variability in block generation times.
Therefore, Eq.( 4) is often derived from Eq. (5).
CLT = T1 + 2 × max{TPoW,1, · · · , TPoW,m1
} [s]. (5)
Using the numerical results from experiments 1 and 2,
estimated CLT using Eq. (5). For experiment 1 with N =
126, based on Fig.13, where maximum T1 is 15 s, and Fig.15,
where maximum T2 is 17 s, it as 15 + 2 × 17 = 49 s. The
CLT for experiment 2 was set when N was fixed, value of
70 and the block generation time interval varied. Based on
Fig.13, where the maximum T1 is 7 s, and Fig.20, where
the maximum T2 is 33 s, we calculated it as 7 + 2 ×
33 = 73 s. The results of Experiments 1 and 2 confirmed
this consistency. Consensus was achieved without exceeding
the maximum value. The probability of incorrect block
information occurring, denoted as E, is calculated with the
number of trials represented as Z, it can be expressed by Eq. 6.
E =
1
Z
[%] (6)
Furthermore, if Z is set to 200 based on the experimental
value, the following result is obtained as follows:
E =
1
200
= 0.005% (7)
According to Eq. 7, we can theoretically estimate that the
failure rate of relayer aggregation using chainless multi-layer
consensus is only 0.005%, which is as small as the BC fork
probability in Bitcoin [51]. Even if the consensus fails with
0.005%, the next trial of chainless multi-layer consensus
would succeeded because the probability of the consensus
failure twice is estimated as 0.0052
, which is too small to
happen as well as Bitcoin eventually resolves BC fork.
D. SCALABILITY PERFORMANCE EVALUATION
Herein, we estimate the theoretical performance achievable
by our proposed method for an improvement in scalability
when the number of parachains N, average block generalization time interval I, and block size S are changed. Based
on the Bitcoin Core (BTC) [52], where the average block
generation time interval was 10 min (600 s) the block size was
1 [MB], and the maximum transaction processing capacity
was 7 transactions / s, the average number of approved
transactions per block were estimated to be 7 × 600 =
4, 200[tx]. Thus, the average transaction processing capacity,
V transactions/s, is described by
V ≃
4, 200 × SN
I
. (8)
From the results of the above experiments and Eq. (8),
we estimated the average transaction processing capacity V
in the chainless multi-layer consensus. When we assume
that blocks with a size of S = 16 [MB] are used in the
experiment, the required capacity of the block header and
the shared block is approximately 135 kB, which is still
sufficient to include numerous additional transaction hashes.
We also found that the success rate of a chainless multi-layer
consensus was 100% when we conducted experiments with
N = 216 parachains and a block generation time interval
I of 180 s from the settings of the experiment 1. In this
setting, transaction processing capacity V can be estimated
as follows:
V =
4, 200 × 16 × 216
180
= 80, 640 [TX/s], (9)
where TX is the abbreviation of transaction. From this
information, we theoretically expect that our proposed system
can improve the performance to exceed the transaction
processing capacity of VISA credit card system, i.e.,
65, 000 transactions/s [53]. Even in the settings of the
experiment 2, we can also calculate
V =
4, 200 × 16 × 70
81
≒ 58, 074 [TX/s], (10)
which is comparative to the transaction processing capacity
of VISA credit card system.
E. DECENTRALIZATION
In this research we define the decentralization in public BCs
as the ratio of the number of nodes that participates in block
generation and verification over the total number of nodes
participating in the P2P network. In relay-chain types such as
Polkadot or Cosmos, parachains in the lower layer (Layer 1)
are less likely to influence the entire system. In the chainless
type, however, every node in the parachains of Layer 1 has the
potential to participate in block generation and verification of
the shared multi-layer consensus part of Layer 0. Therefore,
the chainless type is considered more decentralized than the
relay chain type.
F. TAMPER RESISTANCE OF PARACHAINS
The chainless type can also improve the tamper resistance
of the parachains because the shared multi-layer consensus
part is distributed to the parachains, whereas the relay-chain
type is centralized to the relay chain. If attackers attempt
to alter a block in a parachain they must also modify the
shared multi-layer consensus in other parachains. This makes
the chainless type more tamper-resistant than the relay-chain
type. Our chainless multi-layer consensus can improve the
tampering resistance of BCs. We used tamper-resistanceimprovement ratio R to evaluate the tamper resistance [14].
Let the total number of core nodes in the distributed system
be N and the hash rate of core node be hi (1 ≤ i ≤ N).
Each hash rate hi
is the number of times a cryptographic hash
function can be computed per unit time in each node.
max {h1, h2, · · · , hN } (11)
Suppose the total number of parachains is k and the number
of nodes in each parachain is Pj (1 ≤ j ≤ k). The tampering
resistance of each parachain is given by the maximum hash
power of the nodes for each parachain:
A1 = max {h1,1, · · · , h1,P1
}, (12)
A2 = max {h2,1, · · · , h2,P2
}, (13)
.
.
.
Ak = max {hk,1, · · · , hk,Pk
}, (14)
where N = P1 + P2 + · · · + Pk . Since the BC having the
maximum hash rate becomes a relay chain or zone chain in
PoW, the tamper resistance of each parachain without the
chainless multi-layer consensus can be estimated as follows:
A = max {A1, A2, · · · , Ak } (15)
Eq. (15) evaluates the maximum hash rate as tamper
resistance. Applying chainless multi-layer consensus among
k parachains, the tamper resistance can be estimated by
the sum of all the highest hash rates in the parachains,
that is,
B =
X
k
j=1
Aj (16)
Similarly, Eq. (16) is an expression that evaluates the
maximum hash rate in the parachain as tamper resistance.
Therefore, R is defined as follows:
R =
B
A
(> 1) (17)
Therefore, the more parachains that are involved in the
chainless multi-layer consensus, the stronger the tamper
resistance of the parachains.
G. SECURITY OF THE RA
In the chainless multi-layer consensus, in Layer 0, the nodes
that aim to participate and obtain shared security must earn
the trust of other nodes. We consider the manner in which
each BC can establish trust in the information sent by
nodes from other BCs. From the results of experiment 2,
it can be observed that the block generation time intervals
of each BC affected the consensus latency time of the
chainless multi-layer consensus. The Layer 0 network is
open to anyone for participation, but if participation becomes
completely unrestricted, the network could risk collapsing.
Therefore, we must impose eligibility criteria for participation. Eligibility for participation may include consistent block
generation time or participation as an observer for a specific
period.
In chainless multi-layer consensus, a semi-permissioned
network is needed because pre-approved nodes can participate to perform multi-layer consensus. Communication
between permitted nodes is expected to establish a minimum
level of trust among them. This can be achieved using
common-key encryption or public-key encryption methods,
with the assurance that the nodes possess the necessary
key information. In addition, when sending consensus
information, nodes should consistently include an electronic
signature, which further enhancing trust in communication
between nodes within the P2P network. Furthermore, to prepare for situations such as the loss of a secret key, we have
a mechanism to share and handle the lost secret key phrases
across the entire network.
Other general security issues must also be considered for
chainless multi-layer consensus. Since nodes in a BC system
often communicate to replicate a ledger, the network’s weakest node often becomes a vulnerable entry point for attacks.
Therefore, it is necessary to increase security through mutual
security measures between the node managers. Attacks on
distributed systems are generally assumed to be (1) replays,
(2) impersonations, (3) Sybil, (4) man-in-the-middle, and
(5) false data injection attacks. In addition, attacks on BC
systems are (6) Hiding blocks, (7) 51%, and (8) block
with-holding attacks. Applying existing countermeasures is
expected to improve security to a certain extent [54]. Attack
(1) can be avoided by introducing one-time passwords for
each type of communication. Attacks (2) and (3) can be
avoided through the mutual authentication of the nodes using
electronic signatures while securely sharing their private
keys in advance. It is also important to securely manage
private keys. Attack (4) can be avoided by combining mutual
authentication and encryption in a data transfer between
nodes. Attack (5) can be expressed as followers: avoid error
handling in the node program. It is also important to apply
a security update to the node program as soon as possible
after a security patch against an attack is released. Attack
(6) can be prevented by regularly sharing block information
between parachains for monitoring and block verification.
Attack (7) can be avoided by enhancing decentralization, i.e.,
by increasing the number of nodes and parachains. Attack (8)
can be avoided by fixing the shared multi-layer consensus
part between parachains as quickly as possible by safely
shortening the block generation time.
H. STOP-FAULT TOLERANCE
In the above experiments, we used the Raft consensus
algorithm to avoid stop-fault tolerance in Layer 0. This makes
responding to an attack by injecting a false block candidate
from the leader node difficult. To avoid this, it is necessary
to examine other fault-tolerant consensus algorithms such as
PBFT to address data injection attacks.
It is important to reduce the number of node failures in
the process of a chainless multi-layer consensus because
a failed node in the parachain of Layer 1 can affect
the tamper resistance of the entire system. If a failure
occurs in the representative node handling the relationship
between parachains, the chainless multi-layer consensus
fails and the tamper resistance is degraded. This can
therefore drive the nodes in a parachain to eliminate a
failed representative node as quickly as possible to recover
the tampering resistance of the parachain and to properly
operate the chainless multi-layer consensus within the entire
system.
VIII. CONCLUSION AND FUTURE WORK
In this paper, we have proposed Relayer Aggregation (RA),
a mechanism based on a chainless multi-layer consensus
approach. This method has been shown to effectively reduce
network congestion in BC ecosystems, such as the interchain
ecosystem in Cosmos, where numerous relayer nodes operate. However, the proposed chainless multi-layer consensus
mechanism has certain limitations. Specifically, it relies
on a consortium-based network structure and assumes that
participating BCs share blocks, which limits its applicability
in environments where block-sharing is not feasible.
To address these challenges, we aim to develop mechanisms to mitigate the processing load on individual relayers,
which may increase as the number of relayers decreases. Furthermore, maintaining the public nature of BCs, especially in
comparison to the Cosmos interchain ecosystem, remains a
significant focus.
To overcome these issues, we plan to design and validate
an off-chain management system for relayer aggregation, particularly for environments where block-sharing is challenging
or not possible.