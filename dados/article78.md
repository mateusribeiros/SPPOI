Title: Management of the Chain of Custody of Digital Evidence Using Blockchain and Self-Sovereign Identities: A Systematic Literature Review

ABSTRACT Digital evidence plays an increasingly crucial role in judicial proceedings due to the exponential
growth in the creation, storage, and transmission of digital data. However, its inherent volatility and
susceptibility to tampering necessitate robust mechanisms to ensure integrity and authenticity, making an
effective chain of custody (CoC) a fundamental requirement. While state-of-the-art reviews identify various
aspects, it is necessary to include the use of Self-Sovereign Identity (SSI) systems within the scope of
research. To address this challenge, this article conducts a systematic review of the literature on the use
of blockchain and SSI in managing the chain of custody of digital evidence. The review began with 9,178
studies, which, after a rigorous process applying inclusion and exclusion criteria, resulted in 39 studies
directly related to the research topic. The study maps and reviews techniques, tools, methods, approaches,
and security components for managing the chain of custody of digital evidence. The findings confirm the
widespread adoption of blockchain for preserving digital evidence while indicating that SSI remains an
emerging and underexplored concept in forensic applications. The results highlight the need for further
research on off-chain storage mechanisms, privacy-preserving techniques such as Zero-Knowledge Proofs
(ZKPs) to enhance security, auditability, and interoperability when combined with Verifiable Credentials
(VCs). By mapping the current state of research, this study provides valuable insights into CoC, Blockchain,
and SSI in forensic-based proposals, identifying research gaps, limitations, and opportunities for developing
more robust and scalable evidence management systems.
INDEX TERMS Blockchain, digital evidence, chain of custody management, self-sovereign identities,
systematic literature review.
I. INTRODUCTION
Digital information is present in everyday life and business,
significantly impacting the way data are created, stored, and
shared. In the judicial context, such data have become more
prevalent in civil and criminal proceedings [1], being referred
to as digital evidence [2].
Each piece of digital evidence produced has its own
characteristics, and each electronic device generates digital
evidence in different ways, as there is no standardization [3].
Digital evidence is considered to be traces that, after analysis,
relate in some way to the case and that are in digital
form [4]. It should be noted that data submitted to the
courts may be invalidated, as digital evidence is volatile and
susceptible to manipulation or alteration throughout its life
cycle. Therefore, it is important to track the history of the
data, keeping them intact and authenticated during digital
evidence validation [5]. To achieve this, forensic science
employs the chain of custody, which is the chronological
cataloging or historical documentation of digital evidence [6].
To contextualize the use of chronological cataloging,
it is essential to recognize that the chain of custody
is a cornerstone of forensic and legal procedures across
multiple domains. In forensic medicine, it ensures the proper
collection, handling, and analysis of biological samples and
toxicology reports, safeguarding their integrity for judicial
and investigative purposes. In legal drug testing, particularly
in sports and clinical trials, it plays a pivotal role in
maintaining sample authenticity and preventing tampering [7]. Additionally, the chain of custody is fundamental
in environmental forensics, where it enables the accurate
tracking of contamination sources, and in financial crime
investigations, where the integrity of digital transactions must
be preserved to prevent fraud and ensure legal accountability.
While traffic accidents represent a significant application
of digital evidence, with thousands of cases investigated
annually across different countries, forensic techniques
must also address data collected from vehicles, electronic
devices, and surveillance systems to reconstruct accident
dynamics [8], [9]. Regardless of the domain, maintaining the
integrity and authenticity of digital evidence is paramount
to ensuring its legal admissibility and reliability in judicial
proceedings [2].
In order to obtain an overview of the current state of the
art concerning the management of the digital evidence chain,
this systematic review was carried out. This type of study,
with a well-defined research strategy, allows the work to be
reproduced or replicated and its integrity assessed. From this
study, the main research gaps related to the theme will be
presented. The research questions are precisely described in
Section IV and can be summarized by the following question:
‘‘Which approaches have been proposed to manage the chain
of custody of evidence in digital forensics using blockchain
and self-sovereign identities?’’.
Contributions. The main contributions of this article are:
1) To describe the main approaches and techniques for
preserving the chain of custody of digital evidence using
blockchain and SSI;
2) To cite the main contributions provided by previous
works;
3) To present the main gaps in digital evidence preservation
and chain of custody management using blockchain and
SSI;
4) To indicate the main areas for future research involving
forensic techniques, blockchain and SSI.
The remainder of this work is organized as follows: in
Section II presents the fundamental concepts required to
understand blockchain, SSI, and their applications in digital
forensics; Section III introduces the existing review works
in this research area; Section IV presents the systematic
review, as well as the planning and execution steps; in
Section V, we present the results obtained in response to the
research questions; and the discussion of the selected articles
is presented in Section VI. Finally, Section VII concludes this
article.
II. BACKGROUND
This section presents the basic concepts necessary to understand the terms used in this article. First, in Subsection II-A,
the concept of forensic computing is introduced.
Subsection II-B presents basic information related to
blockchain technology and smart contracts. Finally,
Subsection II-C discusses identity technologies based on
blockchain, referred to as Self-Sovereign Identity (SSI).
A. FORENSIC COMPUTING
Forensic computing is an area of forensic science and a
branch of criminalistics that aims to elucidate how a given
crime or punishable civil action occurred [6], encompassing
the computing elements related to the case [10]. Unlike
other areas of forensic science, forensic computing deals
with digital data, which can be instantly altered due to their
perishable nature over time [11].
Digital evidence refers to information in digital format
that provides concrete data about a particular occurrence [5].
It may be found in different types of media and locations,
regardless of format or application [6].
Electronic or computational resources leave digital traces
that can be used to identify the materiality, dynamics,
authorship [6], and even the motivation behind an event [12].
These digital traces essentially consist of a combination of
binary numbers that represent various types of information,
including images, texts, audio, and video, which, after
detailed analysis, result in digital evidence [10].
1) TERMINOLOGIES AND CONCEPTS
During the execution of a forensic investigation, certain terms
arise that must be clarified. First, regarding digital artifacts,
which consist of the creation of information and data due to
the use of electronic devices and that reveal past activities,
we refer to the Glossary of the Scientific Working Group on
Digital Evidence (SWGDE) [13]. Specifically, in the forensic
context:
• Trace1
: any raw material, which may be a device, data,
signal, or mark on an object that has or may have
a relationship with an investigated event and can be
extracted for subsequent analysis [5], [6], [14];
• Evidence: any object, element, or information that is
related to the investigation; thus, evidence is a trace that
has already been analyzed [4], [15];
For digital evidence to be admissible in court, it must be
preserved throughout all phases of forensic processing [16].
In other words, preserving evidence is linked to the evidence
management life cycle [17]. This life cycle is carried out
by forensic processes defined by phases: identification,
collection, and acquisition, as per ABNT NBR ISO/IEC
27037:2013 [16]. The NIST’s Guide to Integrating Forensic
Techniques into Incident Response [18], published in 2006,
distinguishes the following basic phases of a forensic process:
collection, examination, analysis, and reporting. In the
collection and examination phases, data are extracted from
media or obtained from sources, and in the analysis phase,
information that answers forensic inquiries is obtained. The
report is the record of the process and results in a forensic
document, where the status of some data/trace as evidence is
established.
2) TECHNICAL STANDARDS AND LEGISLATION
The main requirements for digital evidence to be legally
admissible are related to integrity, relevance, and authenticity [19], [20]. For evidence to have these characteristics, there
must be a chain of custody (CoC) containing the transactional
history of the digital evidence. Other authors, such as Richter
et al. [21] and Velho [6], also define that digital evidence will
only be considered admissible in court if it meets the criteria
of authenticity, completeness, reliability, and credibility.
In countries such as Brazil, legal provisions of the
Code of Criminal Procedure have recently been amended,
including those concerning forensic examinations, chain of
custody, and expert reports, to better align with the reality
of digital traces [22]. Specifically regarding the chain of
custody, the tracking of traces was defined through a set of
steps: recognition, isolation, fixation, collection, packaging,
transport, receipt, processing, storage, and disposal [23].
In summary, these are the requirements for a chain of custody
organized into records documenting the chronological history
of the collected trace [20].
3) CHAIN OF CUSTODY
As mentioned earlier, collected data must remain intact to
ensure their integrity. However, transfers of possession or
handling of these traces may occur, and based on this, the
term chain of custody was created to record the procedures.
The chain of custody is a procedure that ensures the protection and safekeeping of materials found in investigations
or provided in legal proceedings[10]. It is necessary to ensure
that the original characteristics and information remain intact,
leaving no doubt about their origin or the handling they
underwent [1].
An appropriate chain of custody should monitor and
document the chronological history of digital evidence [24],
i.e., how it was discovered, obtained, transported, investigated
or analyzed, preserved, and handled among the different
parties involved in the investigation [25]. It should be maintained throughout the entire lifespan of the evidence [16].
In short, the chain of custody is a process created to document
the chronological history of digital evidence, ensuring its
traceability [26].
The data recorded in a chain of custody should answer a set
of questions known as the 5WH (5 W’s and 1 H), i.e., Who,
What, When, Where, Why, and How [27], [28]. The data
and information needed to answer these questions must be
recorded in the chain of custody. The following is a list of
these questions [16]:
• Who had contact with, handled, or discovered the
evidence;
• What changes or procedures were performed on the
evidence;
• When and at what time the evidence was discovered,
accessed, examined, or transferred;
• Where or which locations are associated with the
discovery, collection, examination, and storage of
evidence;
• How the circumstances of the discovery, collection,
examination, and storage of evidence occurred; and
• Why the evidence was collected, i.e., the motivation and,
if possible, the authority determining the collection.
The metadata—data about data—stored in a digital
chain of custody must ensure certain security properties,
as defined by Bonomi et al. [29]: integrity, traceability,
authentication, verifiability, and security (tamper-evidence).
These requirements are essential, considering that the digital
documentation of evidence presents the inherent issues of
information in electronic format [30]. An important part of
the chain of custody’s life cycle is related to the different
actors who interact with it. They typically belong to different
organizational security domains and essentially include [6]:
the agent/person who first contacted the evidence, the
forensic investigator (expert), the parties involved in the
case (plaintiff and defendant), the judicial court, and law
enforcement [28].
B. BLOCKCHAIN
The NIST, through the work of Yaga et al. [31], defines
blockchain as a digital ledger of records whose blocks are
immutable and tamper-proof, implemented in a distributed
manner without a central managing authority. The primary
purpose of blockchain is to enable users to record transactions
in a decentralized and secure manner, ensuring that once a
transaction is published, it becomes immutable. Each block
contains one or more executed transactions and is linked
cryptographically to the hash of the previous block, forming
a continuous and verifiable chain of records, known as a
blockchain.
While earlier cryptographic techniques laid the foundation
for blockchain technology, its modern conceptualization is
attributed to Nakamoto’s seminal work, ‘‘Bitcoin: A Peerto-Peer Electronic Cash System’’ [32]. Nakamoto introduced
the first fully realized implementation of a blockchain
as the underlying infrastructure of Bitcoin, incorporating
cryptographic proof-of-work mechanisms to establish decentralized consensus. Prior to this, in 1991, Scott Stornetta
and Stuart Haber proposed a method for timestamping
digital documents to ensure their integrity over time [33].
Although this early work introduced essential cryptographic
principles, it did not include the decentralized consensus
mechanisms that characterize blockchain technology today.
Thus, Nakamoto’s proposal is widely recognized as the first
comprehensive definition of blockchain as it is known today.
Blockchains can be implemented according to three
models:
• Public (permissionless): there are no restrictions
to access the blockchain, and any entity/user can
read/verify transactions as well as write/insert
transactions;
• Private (permissioned): only qualified users have
access; and
• Hybrid (consortium): a closed group of entities defines
the consensus process and works collectively toward
a common goal. In some cases, entities can be either
public or private.
The operation of different blockchain technologies is
similar. Thus, let us consider the example shown in Figure 1.
It receives a transaction request from a user, creates a block,
disseminates it across the network, all nodes approve it, and
finally, the block becomes valid in the blockchain [34]. The
process of adding a block to the chain is executed by a
protocol that, via a consensus mechanism among participants,
confirms the new block [35]. The most common consensus
algorithms vary among Proof of Work (PoW), Proof of
Stake (PoS), Practical Byzantine Fault Tolerance (PBFT), and
others [34].
FIGURE 1. Operation of blockchain technologies, adapted
from 101 Blockchains [34].
Blockchain uses cryptographic components to ensure data
immutability. One of these components is one-way functions,
also known as cryptographic Hash Functions. They map
input data of variable length to a fixed-length hexadecimal
sequence [36]. Another cryptographic component is the
cryptographic Nonce, defined as an arbitrarily generated
number used to produce different data Hashes [31].
The main characteristics of blockchain include: decentralization, anonymity, autonomy, security, non-repudiation,
resilience, implementation via smart contracts, auditability,
immutability, and a public state [37].
Specifically, it is possible to achieve verifiability and traceability of actions and transactions executed on a blockchain.
Permissioned blockchain implementations can also provide
additional security properties such as confidentiality and
privacy, as authentication and authorization mechanisms can
be included to control participants’ access to the blockchain
network [31].
1) BLOCKCHAIN TECHNOLOGIES
Various blockchain technologies emerge daily in the market, each designed for specific purposes. To provide a
clearer distinction between these technologies, we classify
them into three main categories: Blockchain Networks,
Tokens/Cryptocurrencies, and Blockchain Frameworks.
• Blockchain Networks: These are decentralized infrastructures that operate as public or permissioned distributed ledgers, supporting the execution of smart
contracts and decentralized applications (DApps) [38],
[39]. The main blockchain networks identified in the
reviewed literature include:
- Ethereum [40] - A widely adopted smart contract
platform that provides the foundation for DApps,
tokenization, and decentralized finance (DeFi).
- Polygon Network [41] - A Layer 2 scaling solution
for Ethereum that improves transaction throughput and reduces costs using technologies such
as sidechains, rollups, and Proof-of-Stake (PoS)
consensus.
- Hyperledger Fabric [38], [42] - A permissioned
blockchain framework designed for enterprise applications, featuring modular consensus mechanisms
and strict access control policies.
- Hyperledger Indy [43] - A blockchain specifically
designed for self-sovereign identity (SSI), supporting Decentralized Identifiers (DIDs) and Verifiable
Credentials (VCs).
- Exonum [39] - A permissioned blockchain framework developed for high-performance and auditable
applications.
- Scrybe [44] - A custom blockchain-based ledger
system designed to ensure digital data integrity and
evidence preservation.
• Tokens and Cryptocurrencies: These are digital assets
issued on blockchain networks, serving as store of value,
transaction fees, or governance mechanisms [33], [41].
The main tokens identified in the literature include:
- Bitcoin (BTC) [32], [33] - The first and most widely
recognized cryptocurrency, primarily used as a store
of value and medium of exchange.
- Ether (ETH) [40] - The native cryptocurrency of
Ethereum, essential for gas fees, smart contract
execution, and network security.
- Polygon (MATIC) [41] - The utility token of the
Polygon Network, used for transaction fees, staking,
and network governance.
• Blockchain Frameworks: These frameworks provide
foundational tools for developing custom or private
blockchain networks, often used in enterprise or regulatory environments [39], [45]:
- Hyperledger Fabric [45], [46] - A modular and
highly configurable blockchain framework, designed
for enterprise-grade private networks.
- Exonum [39] - A permissioned blockchain framework that prioritizes auditability, regulatory compliance, and high-performance applications.
This refined typology classification ensures a clear distinction between blockchain networks, tokens, and infrastructure
frameworks, avoiding misclassification and improving the
understanding of blockchain components within forensic and
chain of custody contexts.
C. SELF-SOVEREIGN IDENTITY
Self-sovereign identities (SSI) extend the concept of digital
identity, which is defined as a finite set of attributes allowing
a person, animal, object, or process to be uniquely identifiable
and electronically authenticated by others [47].
The self-sovereign identity model is based on the principle
that the user is the central authority over their identity [43].
Unlike traditional identity management models—where identity data is stored and controlled by centralized institutions—
SSI leverages decentralized technologies, such as blockchain,
to ensure user control and enhance privacy.
The SSI framework is based on two core standards defined
by the World Wide Web Consortium (W3C):
• Decentralized Identifiers (DIDs): Unique, resolvable,
and persistent identifiers that do not rely on a centralized
registry. Each DID consists of three parts: the scheme,
the DID method, and a method-specific identifier,
as illustrated in Figure 2.
FIGURE 2. Structure of a Decentralized Identifier (DID), showing its
components: scheme, method, and method-specific identifier [48].
• Verifiable Credentials (VCs): Cryptographically
signed credentials issued by trusted entities to verify
specific claims about a subject. These credentials can be
selectively disclosed, enhancing privacy while ensuring
authenticity [49], as illustrated in Figure 3.
1) DID ARCHITECTURE AND RESOLUTION PROCESS
The DID architecture allows for resolving a DID into a DID
Document, which contains metadata such as public keys,
service endpoints, and authentication mechanisms [48]. The
resolution process, illustrated in Figure 4, follows these key
steps:
1) A DID subject is an entity (a person, organization,
or device) to which a DID is assigned.
2) The DID itself (e.g., did:example:123) serves as a
reference that can be resolved to a corresponding DID
document.
FIGURE 3. Verifiable credential linked to a verification method of type
JsonWebKey2020 [48].
3) The DID document includes authentication mechanisms, cryptographic keys, and service endpoints, and
is recorded in a Verifiable Data Registry (e.g., a
blockchain).
4) A DID URL extends a DID with additional information
to reference specific resources.
5) A DID controller has permission to modify or revoke
the DID document.
FIGURE 4. DID architecture and resolution process [48].
2) DID DOCUMENT AND AUTHENTICATION
A DID document is a JSON or JSON-LD object containing
public keys and metadata necessary for authentication and
verification [48]. Figure 5 shows an example of a DID
document, where the authentication mechanism is based on
the Ed25519 cryptographic key pair.
This DID document contains:
• A reference to the DID itself.
• An authentication method allowing the DID owner to
prove control.
• A cryptographic public key for signature verification.
• A DID controller responsible for managing the DID.
It is important to highlight that the DID Document,
presented in Figure 5, is generated after resolving the DID.
This resolution process varies depending on the DID method,
FIGURE 5. Example of a DID document containing authentication
information, a public key, and the DID controller [48].
as each method has its own resolver, which can be explored
through the Universal Resolver.2
In contrast, the Verifiable Credential (VC), shown in
Figure 3, is typically stored in a digital wallet or another
trusted repository owned by the credential holder. Most
analyzed Verifiable Credentials store only the cryptographic
proof of the credential on the blockchain, ensuring that
the private data remains under the exclusive control of the
credential owner.
3) THE ROLE OF SSI IN DIGITAL EVIDENCE MANAGEMENT
In the forensic process of digital evidence preservation and
management, the use of SSI and Blockchain introduces key
security improvements [50], [51]:
• Access control and Authentication: SSI ensures that
only authorized individuals have access to digital
evidence;
• Integrity: SSI ensures that information is not altered;
• Interoperability: Standardized DID and VC protocols
allow different actors (e.g., law enforcement, courts,
forensic analysts) to securely exchange verifiable identity data;
• Decentralization: the use of SSI with Blockchain
eliminates single points of failure and reduces the risk
of data manipulation or corruption;
• Traceability and Auditing: SSI facilitates the creation of immutable and auditable records, ensuring
transparency regarding who accessed or modified the
evidence.
III. RELATED WORK
This section presents previous works addressing research,
reviews, and systematic literature mappings within the context of this study. At the end, the contributions, difficulties,
and differences of these works in relation to the present study
will be presented.
Before conducting a Systematic Literature Review (SLR),
as presented in this work, it is necessary to ensure that it is
indeed needed, i.e., to verify that there is no similar, highquality work already available in the literature. This study
2https://resolver.identity.foundation/
followed the terms and definitions used by Kitchenham [52]
and the methodology presented by Oriol [53] to make the
systematic study process reproducible.
It is important to distinguish different literature research
methods by considering their level of formality, purpose,
and methodology [52], [53]: a Survey, State-of-the-Art,
or Review (traditional/narrative review) provides a less
formal and systematic overview, highlighting main concepts
without adhering to a strict protocol; a Bibliometric Review
(BR) quantitatively evaluates publication patterns, impact,
and collaboration; a Systematic Literature Mapping (SLM)
classifies and organizes the literature, offering an overall
map of the field and indicating gaps, often serving as
a preliminary step for a more in-depth SLR analysis.
Finally, a Systematic Literature Review (SLR) adopts
well-defined and reproducible protocols for searching, selecting, evaluating, synthesizing, and meta-synthesizing studies,
following rigorous guidelines, seeking to answer specific
research questions with maximum transparency, quality, and
reliability.
In order to encompass more results, the following nomenclatures and terms were included as systematic studies:
Survey; Systematic Literature Review; and Systematic Literature Mapping. In addition, the research protocol defined in
Section IV was followed, with the addition of terms: ‘‘state
of the art’’, ‘‘survey’’, ‘‘review’’, ‘‘bibliometric review’’,
‘‘systematic mapping’’, and ‘‘systematic review’’.
After these considerations, the search string remained as
follows: ((‘‘evidence*’’ OR ‘‘forensic*’’) AND (‘‘blockchain’’
OR ‘‘distributed ledger’’ OR ‘‘smart contracts’’ OR ‘‘decentralized identifiers’’ OR ‘‘self-sovereign’’ OR ‘‘verifiable
credentials’’)) AND (‘‘survey’’ OR ‘‘state of the art’’ OR
‘‘review’’ OR ‘‘bibliometric review’’ OR ‘‘systematic mapping’’ OR ‘‘systematic review’’).
The search string was structured to ensure a broad
retrieval of relevant studies on blockchain-based forensic
chain of custody (CoC) management. While using AND
between blockchain-related terms and SSI-related terms
(e.g., decentralized identifiers, self-sovereign identity, verifiable credentials) would emphasize SSI, preliminary tests
showed that this approach would severely limit the number
of retrieved articles. Since SSI is still an emerging concept
in forensic applications, many relevant studies focus on
blockchain for evidence management but do not explicitly
mention SSI, despite incorporating similar authentication and
access control mechanisms. To maintain inclusivity, OR was
used, allowing the identification of works that indirectly align
with SSI principles.
A. REVIEW DATABASES
Searches were conducted in four major scientific article
databases, as outlined in Table 1: ACM, IEEE, ScienceDirect,
and Springer. All searches focused on articles published
between 2019 and 2024, and were carried out on May 21,
2024.
TABLE 1. Databases used in this review for article searches.
1) ACM
The following search parameters were applied to the ACM
Digital Library:
• Period: 2019 to 2024;
• Content Type: ‘‘Survey’’.
2) IEEE
For the IEEE Xplore database, the search was configured as
follows:
• Period: 2019 to 2024;
• Types of works: ‘‘Conferences’’, ‘‘Journals’’, and
‘‘Early Access Articles’’;
• Publication Topics: ‘‘Systematic Review’’.
3) SCIENCEDIRECT
For ScienceDirect, the following search parameters were
used:
• Period: 2019 to 2024;
• Article Type: ‘‘Review articles’’;
• Subject Areas: ‘‘Computer Science’’.
Given ScienceDirect’s limitation of handling only eight
logical connectors in search queries, the search was split into
multiple queries. Each query combined the primary search
string with specific terms using the logical connector AND,
as follows:
- ((‘‘evidence’’ OR ‘‘forensic’’) AND (‘‘blockchain’’ OR
‘‘distributed ledger’’ OR ‘‘smart contracts’’ OR ‘‘decentralized identifiers’’ OR ‘‘self-sovereign’’ OR ‘‘verifiable
credentials’’)) AND ‘‘survey’’
- ((‘‘evidence’’ OR ‘‘forensic’’) AND (‘‘blockchain’’ OR
‘‘distributed ledger’’ OR ‘‘smart contracts’’ OR ‘‘decentralized identifiers’’ OR ‘‘self-sovereign’’ OR ‘‘verifiable
credentials’’)) AND ‘‘state of the art’’
- ((‘‘evidence’’ OR ‘‘forensic’’) AND (‘‘blockchain’’ OR
‘‘distributed ledger’’ OR ‘‘smart contracts’’ OR ‘‘decentralized identifiers’’ OR ‘‘self-sovereign’’ OR ‘‘verifiable
credentials’’)) AND ‘‘review’’
- ((‘‘evidence’’ OR ‘‘forensic’’) AND (‘‘blockchain’’ OR
‘‘distributed ledger’’ OR ‘‘smart contracts’’ OR ‘‘decentralized identifiers’’ OR ‘‘self-sovereign’’ OR ‘‘verifiable
credentials’’)) AND ‘‘bibliometric review’’
- ((‘‘evidence’’ OR ‘‘forensic’’) AND (‘‘blockchain’’ OR
‘‘distributed ledger’’ OR ‘‘smart contracts’’ OR ‘‘decentralized identifiers’’ OR ‘‘self-sovereign’’ OR ‘‘verifiable
credentials’’)) AND ‘‘systematic mapping’’
- ((‘‘evidence’’ OR ‘‘forensic’’) AND (‘‘blockchain’’ OR
‘‘distributed ledger’’ OR ‘‘smart contracts’’ OR ‘‘decentralized identifiers’’ OR ‘‘self-sovereign’’ OR ‘‘verifiable
credentials’’)) AND ‘‘systematic review’’
4) SPRINGER
For Springer, the search parameters were as follows:
• Period: 2019 to 2024;
• Content Type: ‘‘Article’’, ‘‘Research article’’, ‘‘Conference paper’’, and ‘‘Review article’’;
• Disciplines: ‘‘Computer Science’’.
B. SEARCH STRATEGY CONSIDERATIONS
In the case of ScienceDirect and Springer, it was possible to
apply the ‘‘Computer Science’’ discipline filter, which helped
to refine the results and focus on relevant studies. For ACM
and IEEE, such specific filtering was not available directly in
the search interface; however, a thorough manual screening
was conducted based on the research questions defined in
Section IV to ensure the relevance and quality of selected
studies.
We also addressed limitations in ScienceDirect’s search
capabilities by running multiple queries to ensure comprehensive coverage.
This detailed search strategy enhances the transparency
and reproducibility of the systematic review process, as recommended in best practices for evidence-based research.
C. EXECUTION AND CONSIDERATIONS
The searches returned a total of 1,171 articles that met the
criteria. After including these works in the StArt tool (State
of the Art through Systematic Review) [54], 593 duplicates
were identified, leaving 578 articles for Stage 1. In Stage 2,
by reading the title, abstract, and keywords, those that did
not answer the following question were excluded: ‘‘Does
the review work address the use of blockchain or SSI in
the preservation of evidence in digital forensics?’’ Ten (10)
articles were accepted at this stage.
In Stage 3, the extraction phase, where full readings
were conducted, some articles were rejected. The article by
Edward and Ojeniyi [55] was rejected for not considering
the use of blockchain in its gaps and trends, since the
focus of the review was the admissibility of digital evidence
in the forensic context. The authors Casino et al. [56]
presented a review considering cloud, network, mobile, and
IoT forensics. They identified issues such as the lack of CoC
preservation mechanisms in cloud and mobile devices, as well
as confidentiality problems across different jurisdictional
domains for cloud and IoT. They made considerations about
ISO/IEC standards applicable to investigative activities and
processes, but did not address the use of blockchain as an
investigative resource for storing and managing the CoC. The
article by Javed et al. [57] provided a review of tools and areas
in digital forensics but did not address the use of blockchain.
In Table 2, the seven selected articles are compared
in terms of the type of review conducted and the subjects/characteristics addressed: Forensics (For), Evidence
(Evid.), Chain of Custody (CoC), Blockchain (Block.), and
Self-Sovereign Identity (SSI).
Regarding the accepted works, a brief assessment is
presented. Akinbi et al. [58] identified certain issues in IoT
TABLE 2. Comparison with related works.
cloud forensics: security aspects, such as access control,
blockchain infrastructure resilience against attacks, problems
with authentication, and vulnerabilities in identity management. Bakhshi [59], when presenting solutions, indicated
blockchain as a means to continuously preserve evidence
integrity, considering the IoT environment. This author also
mentioned that blockchain could address the issue of data
movement across different jurisdictions. The authors of [64]
acknowledged that blockchain could be a useful tool for
challenges in cloud forensics but only presented a review of
the problems and issues.
It can be concluded from the accepted articles that
only one study, [58], conducted an extensive systematic
literature review, while the remaining works [59], [60], [62],
[63] can be classified as traditional reviews and studies
with a more limited scope. The work by [61] provided
a more comprehensive literature survey, yet it did not
deeply explore authentication and authorization mechanisms,
which are crucial for forensic chain of custody (CoC)
applications.
Despite the increasing number of reviews on blockchain
applications in digital forensics, several challenges and gaps
persist. Most of the existing systematic studies focus on
blockchain’s potential for evidence integrity and traceability
but lack in-depth discussions on authentication, access
control, and privacy-preserving mechanisms, particularly
Self-Sovereign Identity (SSI) solutions. Furthermore, while
some reviews highlight blockchain’s role in securing digital
forensic evidence, few studies examine its integration across
the entire CoC lifecycle, leaving open questions regarding real-world feasibility, scalability, and interoperability.
Another critical limitation observed in previous works
is the lack of empirical validation and implementation
details, as most studies propose conceptual models without
practical demonstrations or case studies. Additionally, offchain storage mechanisms remain an underexplored topic,
with limited discussions on how to securely manage and
retrieve digital evidence stored outside the blockchain.
Given these limitations, this study aims to conduct a
systematic literature review focused on blockchain-based
CoC solutions, explicitly addressing the integration of SSI
for decentralized authentication and the challenges associated
with off-chain storage and access control mechanisms.
By systematically mapping the current state of research, this
review seeks to identify existing gaps, highlight promising
directions, and provide a structured foundation for future
research on forensic CoC management using blockchain
technology.
IV. METHODOLOGY
As discussed in Section III, there is a need to conduct a
systematic review on the preservation and management of
digital evidence in forensic environments, using techniques
and methods provided by blockchain and mechanisms of
Self-Sovereign Identity.
The systematic review process was divided into three
stages: planning and protocol development, review execution, and results synthesis. Thus, in Subsection IV-A,
the review protocol for the articles will be presented, and
Subsection IV-B will provide information on the execution
stage of the search and selection of works, concluding with a
table of the selected articles. The summarization of the results
is presented separately in Sections V, and VI.
A. PLANNING
This subsection presents the protocol of the systematic review
carried out for this research. A well-defined research strategy
allows the work to be reproduced or replicated and its
integrity assessed. Thus, the following sections present the
objectives, research questions, article sources, search string,
and inclusion and exclusion criteria.
1) OBJECTIVE AND RESEARCH QUESTIONS
The objective of the systematic review is to identify,
analyze, and classify the state of the art regarding methods,
techniques, and approaches that address the preservation
and management of the digital evidence chain of custody
using blockchain and self-sovereign identity. Based on this
objective, the Research Questions (RQs) to be answered by
this review are defined in Table 3.
TABLE 3. Research questions defined for the systematic review.
2) SEARCH SOURCES
The state of the art related to the research objective of this
systematic review was obtained by searching for articles
in relevant scientific databases in the field of computing.
Certain criteria guided the choice of these research databases,
namely:
• Coverage: the number of conference proceedings,
journals, indexed books, and the type of areas covered
were evaluated;
• Content update: the publications indexed in the
database should be updated regularly;
• Availability: the databases must be available internally
at Federal University of Santa Catarina (UFSC);
• Versatility in exporting results: given the large volume
of results returned by the databases, it is important that
they can be exported automatically;
• Quality of results: accuracy of the results returned by
the databases; and
• Usability: the search tool should be understandable and
easy to operate.
Thus, four different electronic databases where the articles
were searched are presented in Table 1.
3) SEARCH STRING
Initially, we conducted an exploratory study focused
exclusively on the relationship between Forensics and
Self-Sovereign Identities (SSI). However, this search yielded
only one directly related article, highlighting that this intersection remains underexplored in the academic literature.
Given this limitation, we expanded our search to include
Blockchain, as SSI implementations often rely on blockchain
platforms for storing Decentralized Identifiers (DIDs) and
the proofs of Verifiable Credentials (VCs). Therefore,
to construct the search string, three key research areas were
identified: Forensics and Digital Evidence, Blockchain,
and Self-Sovereign Identities. Keywords were derived from
these areas as follows:
• Forensics: ‘‘evidences’’, ‘‘evidence’’, ‘‘forensic’’, and
‘‘forensics’’;
• Blockchain: ‘‘blockchain’’, ‘‘distributed ledger’’, and
‘‘smart contracts’’;
• Self-Sovereign Identities: ‘‘decentralized identifiers’’,
‘‘self-sovereign’’, and ‘‘verifiable credentials’’.
We used a wildcard character (*) in the search string
to account for variations of terms like ‘‘evidence’’,
‘‘evidences’’, ‘‘forensic’’, and ‘‘forensics’’. In cases where
the wildcard could not be used due to database limitations,
we opted for singular terms, resulting in the following
structure: (‘‘evidence’’ OR ‘‘forensic’’).
Considering these keywords, the finalized search string
used across databases was:
(‘‘evidence*’’ OR ‘‘forensic*’’) AND (‘‘blockchain’’
OR ‘‘distributed ledger’’ OR ‘‘smart contracts’’ OR
‘‘decentralized identifiers’’ OR ‘‘self-sovereign’’
OR ‘‘verifiable credentials’’)
4) PARAMETERS USED FOR SEARCHING DATABASES
First, it is important to highlight that the databases used in this
study are listed in Table 1: ACM, IEEE, ScienceDirect, and
Springer. Below, we describe the specific parameters applied
to each database.
a: ACM
The following search parameters were applied to the ACM
Digital Library:
• Period: 2019 to 2024;
• Content Type: no filter was applied.
b: IEEE
For the IEEE Xplore database, the search was configured as
follows:
• Period: 2019 to 2024;
• Types of works: ‘‘Conferences’’, ‘‘Journals’’, ‘‘Magazines’’, and ‘‘Early Access Articles’’.
c: SCIENCEDIRECT
For ScienceDirect, the following search parameters were
used:
• Period: 2019 to 2024;
• Article Type: ‘‘Review articles’’, and ‘‘Research articles’’;
• Subject Areas: ‘‘Computer Science’’.
d: SPRINGER
For Springer, the search parameters were as follows:
• Period: 2019 to 2024;
• Content Type: ‘‘Article’’, ‘‘Conference proceedings’’,
and ‘‘Conference paper’’;
• Languages: ‘‘English’’,
• Disciplines: ‘‘Computer Science’’.
5) INCLUSION AND EXCLUSION CRITERIA
The articles retrieved from the four databases were subjected
to inclusion and exclusion criteria to obtain a set of works that
truly belong to the state of the art on the topic. The following
inclusion criteria were applied:
• Conference or journal articles: The selection was
restricted to conference and journal articles, ensuring
that only works with scientific rigor and innovative
contributions were included.
• Publications from 2019 onward: The review considered only recent works (2019-2024) to capture the latest
advancements in blockchain and Self-Sovereign Identity
(SSI) applied to the chain of custody (CoC) of digital
evidence.
• Works addressing blockchain, SSI, and digital evidence in CoC: The selection included studies that:
- Propose a method or approach for preserving and
managing CoC of digital evidence using blockchain;
- Propose a method or approach for preserving and
managing CoC of digital evidence using SSI.
To further refine the selection and exclude irrelevant works,
the following exclusion criteria were used:
• Tutorial/demo papers: Excluded works that only
demonstrate technologies or tools without a structured
scientific contribution.
• Whitepapers or industry reports: Excluded documents that lack theoretical and scientific grounding,
typically focusing on practical implementations without
formal validation.
• Books or book chapters: Excluded as they often lack
empirical validation and structured scientific models,
architectures, or frameworks.
• Works not written in English: The study was limited
to English-language publications due to its status as the
universal scientific language, ensuring a broader impact
and accessibility.
• Inaccessible articles: Works that could not be retrieved
through the Federal University of Santa Catarina
(UFSC) library system were excluded.
• Review, mapping, or survey papers: The study
excluded secondary studies, such as systematic reviews,
systematic mappings, and surveys, since the focus is on
primary research contributions.
• Incomplete papers or extended abstracts: Works that
did not present a full paper were excluded, as they lack
complete methodological and experimental details.
• Works without relevant keywords in the title,
abstract, or keywords: Articles were excluded if they
did not contain any of the defined search keywords in
their title, abstract, or keywords section, as this indicates
a lack of direct relevance to the research scope.
• Works addressing digital evidence but not
blockchain or SSI: Excluded articles that discussed
digital evidence CoC but did not incorporate blockchain
or SSI.
• Works using blockchain or SSI without applying it
to the CoC of digital evidence: Excluded articles that
discussed blockchain or SSI but did not incorporate CoC
or Forensics.
• Works using blockchain for evidence storage but not
implementing CoC preservation: The primary focus
of this study is CoC preservation. Therefore, studies
that only store evidence on blockchain for integrity and
immutability purposes but do not implement a structured
CoC model were excluded.
The exclusion criteria were explicitly defined to differentiate studies that merely store data on blockchain for integrity
from those that actively implement structured CoC mechanisms. This research specifically focuses on blockchain
applications for managing and maintaining CoC, which
involves storing metadata associated with the sequential
stages of digital evidence handling.
Articles that primarily propose forensic methodologies,
digital investigation techniques, or IoT-related forensic
approaches were excluded if they did not integrate blockchain
or SSI for CoC management.
6) SLR DESIGN AND MITIGATION STRATEGIES
Some threats to the validity of this systematic review were
identified. According to Silva [65], the review protocol allows
us to verify the methodology but does not guarantee how it
was executed, which may introduce biases. The main threats
and the measures adopted to minimize them are described
below:
• Biased evaluation by the researchers: To mitigate
researcher bias, the evaluation involved two additional
reviewers: two senior researchers with extensive experience. Their involvement helped ensure impartiality in
the analysis of the articles.
• Publication bias: To reduce this threat, four widely
recognized academic databases (SpringerLink, ScienceDirect, IEEE Xplore, and ACM Digital Library)
were used. Only articles published in conferences and
journals were included, ensuring the academic quality
of the sources.
• Threats to primary study selection: The risk of
overlooking relevant articles was mitigated through
careful planning of the search string, which included
broad keywords related to the topic. Additionally, the
inclusion and exclusion criteria were wide-ranging
enough to cover different aspects of the review scope.
• Threats to data extraction and result consistency:
Data extraction was carried out collaboratively and
discussed among the researchers to ensure consistency
in the results. Whenever necessary, the protocol was
adjusted to correct inconsistencies and avoid bias during
analysis.
B. EXECUTION
The article searches in the databases presented in Table 1 were
conducted on March 28, 2024, and updated on November
12, 2024, prior to publication. The search string described
in Section IV-A3 was applied to all databases based on
the parameters outlined in Subsection IV-A4, except for the
ScienceDirect database, which does not support the wildcard
character ‘‘*’’.
In the ScienceDirect search interface, to address the
limitation of supporting only eight logical connectors and
the inability to use the wildcard character ‘‘*’’, we used
singular term variations. Exploratory searches revealed that
using singular terms also retrieves results containing plural
FIGURE 6. Stages of the SLR execution and respective numbers of included and excluded articles.
forms. Therefore, the adapted search string for ScienceDirect
was as follows:
(‘‘evidence’’ OR ‘‘forensic’’) AND (‘‘blockchain’’
OR ‘‘distributed ledger’’ OR ‘‘smart contracts’’ OR
‘‘decentralized identifiers’’ OR ‘‘self-sovereign’’
OR ‘‘verifiable credentials’’)
1) EXECUTION PROCEDURE BY RESEARCHERS
To efficiently manage the large volume of articles retrieved,
we employed the StArt tool (State of the Art through
Systematic Review) tool, version 3.0.3 Beta,3
to assist in the
classification process. This tool facilitated semi-automated
scoring based on predefined keywords found in titles,
abstracts, and keywords, streamlining the selection process.
It is important to note that StArt does not utilize artificial
intelligence; all inclusion and exclusion decisions were
made manually by the reviewers to ensure accuracy and
consistency.
The review process involved two researchers (Leandro and
Gerson) who independently conducted parallel screenings
from March to June 2024, following the established inclusion
and exclusion criteria. After completing their individual
assessments, the results were consolidated and reviewed by
a third researcher (Cristiano), who acted as a mediator to
resolve discrepancies. Cristiano determined that Leandro’s
selection was the most comprehensive, which served as the
foundation for manuscript development.
The manuscript underwent further refinement through
reviews by two senior researchers (Carlos and Carla), who
suggested additional updates. This led to a second round of
searches and refinements conducted on November 12, 2024,
following the original search parameters.
2) EXECUTION STAGES
Six stages were employed for the inclusion and exclusion
of articles during the review process. The complete process
is illustrated in Figure 6. The resulting articles are listed in
Table 4. Each stage will be detailed in the following sections.
Stage 1 consisted of searching the databases listed in
Table 1. All database searches were refined using the filters
described in Subsection IV-A4.
The search in the ACM database was performed in the
initial search box, returning a total of 1,467 articles. The IEEE
search returned 739 articles, while ScienceDirect reported
the existence of 2,054 articles. Finally, the Springer search
returned a total of 2,191 articles. Therefore, in the first stage,
6,451 articles were selected from the four databases.
Stage 2 began with the inclusion of the resulting articles
into the StArt. The next stages were performed using this tool.
It should be noted that after inclusion in the tool, only 6,409
articles could be loaded. After analysis, it was found that the
42 articles that were not loaded were duplicates or without
content. In this study, they are considered duplicates.
Also in Stage 2, an analysis of titles, keywords, and
abstracts was carried out in order to classify the articles
according to the inclusion and exclusion criteria presented in
Section IV-A5. The tool has a feature that assigns scores to
articles based on the keywords found in the title, keywords,
and abstract. As a result, 87 articles were accepted for the
next phase.
Stage 3 involved excluding articles that were not available
for internal access at the Federal University of Santa Catarina
(UFSC) or via the CAPES Journals Portal.4 Eight articles that
were unavailable for consultation or full-text download were
excluded, resulting in 79 articles at the end of this phase.
Stage 4 was the phase where a full reading of all the articles
accepted in the previous phase, and for which the full text
was available, was performed. The inclusion and exclusion
criteria were reapplied, and data related to extraction fields
were collected to compare the various works. After applying
the inclusion and exclusion criteria to the full-text reading, 34
articles remained included.
Stage 5 took place on November 12, 2024, the date on
which the update regarding articles published after March
28, 2024, occurred. For this stage, an update was conducted
based on the previously performed Stages 2, 3, and 4, but
focusing only on articles published in 2024 and those marked
for publication in 2025 as of the search date.
To do this, a new search was performed in the databases
presented in Table 1 and the results were imported into the
StArt tool. The search in ACM returned a total of 607 articles,
of which 97 were duplicates, i.e., they had already been
analyzed previously on March 28, 2024. In IEEE, the
search returned 276 articles, resulting in 64 duplicates. The
ScienceDirect database reported the existence of 900 articles,
yielding 254 duplicates. Finally, the search in Springer
returned a total of 944 articles, resulting in 329 duplicates.
Therefore, during the update, 2,727 articles were selected
from the four databases, with a total of 746 duplicated articles
that had already been previously analyzed. Thus, the analysis
of the newly obtained, unclassified articles begins with a total
of 1,981 articles.
In Stage 6, after applying the inclusion and exclusion
criteria from Stages 2, 3, and 4 to the 9,178 retrieved articles,
39 articles remained included, 8,328 were rejected, and
811 were duplicates.
TABLE 4. Selection of resulting works from applying the SLR
methodology.
Table 4 shows the resulting articles from the systematic
review protocol execution process. It lists the authors (in
alphabetical order), the year of publication, the reference
number in the article (citation), and the Data Extraction
Form (DEF) Id. The number in the last column refers to the
application of the protocol using the StArt tool. The complete
DEF with all stages and comments is available for viewing in
an ‘‘xls’’ file posted on IEEE Xplore under the tab ‘‘media’’.
V. RESULTS-ANSWERS TO THE RESEARCH QUESTIONS
By executing the systematic review protocol presented in the
previous section, it was possible to obtain a set of 39 articles
that address preserving and managing the chain of custody of
evidence in digital forensics through blockchain or SSI architectures. In this section, these works are analyzed with respect
to the four research questions defined in Section IV. Each one
is discussed in a specific subsection: V-A, V-B, V-C, and V-D.
Additionally, Subsection V-E presents some other properties
that are directly related to all the research questions. Finally,
Subsection V-F provides a general comparison in table form.
A. RQ1: WHICH BLOCKCHAIN TECHNOLOGIES ARE
ADOPTED TO PRESERVE THE CHAIN OF EVIDENCE?
To answer RQ1, extraction properties related to blockchain
technologies were defined, including:
• Blockchain model (Figure 7): public (permissionless),
private (permissioned), or hybrid (consortium);
• Blockchain platform (Figure 8): Ethereum, Hyperledger Fabric, Hyperledger Indy, Polygon, among
others.
Analyses and results are presented below.
1) BLOCKCHAIN MODELS
Blockchain models were categorized into three main types:
public (permissionless), private (permissioned), and hybrid
(consortium). The distribution of these models across the
analyzed works is illustrated in Figure 7.
As depicted in Figure 7, the majority of studies (66.7%)
implemented private blockchain models, corresponding to
26 works. This approach was preferred in systems involving
predefined entities, such as forensic experts, police, and
judiciary bodies, due to its ability to ensure higher levels of
confidentiality and controlled access. Five studies employed
public blockchain models, predominantly using the Ethereum
network. Meanwhile, six works adopted hybrid models,
combining features of public and private blockchains to
balance accessibility and security. Notably, two studies did
not specify the blockchain model used.
a: SMART CONTRACTS
An important aspect to highlight is the use of smart contracts,
which were addressed in 36 studies. Only three works [50],
[72], [77] did not specify the use of smart contracts. In the
case of [50], smart contracts were not employed because
FIGURE 7. Blockchain platform model.
the study utilized ACA-Py,5 which provides a complete
architecture for the intended functions. In contrast, the works
by Black et al. [72] and Cosic et al. [77] did not explicitly
clarify whether smart contracts were used, but left it for
future work. This widespread adoption demonstrates the
growing interest in leveraging smart contracts to automate the
registration and preservation of digital evidence, as well as to
implement robust access control mechanisms.
It is worth emphasizing that the choice of blockchain model
is often influenced by the platform utilized. However, individual authors may adapt or customize standard approaches
to meet the specific requirements of their proposals.
2) BLOCKCHAIN PLATFORMS
The choice of blockchain platforms used in the projects
provides valuable insights into the properties anticipated by
the studies. For example, if Ethereum is used, it is expected
that the issue of access control will be addressed. On the other
hand, if Hyperledger Fabric is used, it is expected that the
deployment of a private network will be planned and carried
out.
The Figure 8 shows the distribution between the works and
the following is an analysis of one of the proposals:
• Hyperledger Fabric: Thirteen proposals utilized
Hyperledger Fabric, highlighting its adaptability for
private networks and robust support for smart contracts.
One study [76] mentioned using Hyperledger without
specifying the exact project employed.
• Ethereum: Twelve proposals implemented Ethereum,
traditionally associated with public blockchain models.
However, some studies also employed it in hybrid and
private contexts, reflecting its versatility [66], [83], [84],
[85], [93], [99].
• Polygon6
: One proposal [41] adopted Polygon,
an Ethereum-based solution noted for its multichain
architecture designed to enhance scalability and reduce
costs.
• Scrybe: One study [72] used Scrybe, a private
blockchain platform designed specifically for traceability in clinical trials, leveraging a lightweight consensus
algorithm to optimize performance.
• Hyperledger Sawtooth7
: One work [81] employed
Hyperledger Sawtooth, which is now discontinued.
• Hyperledger Composer8
: Three studies relied on
Hyperledger Composer, a tool designed for rapid
blockchain application development, although it is no
longer actively maintained [67], [78], [88].
• Hyperledger Indy9 and Aries10: One study [50] utilized these platforms to implement self-sovereign identity (SSI), enabling decentralized identity management.
• Spidernet: One study [79] introduced Spidernet,
a hybrid solution integrating Polkadot and Cosmos
frameworks for IoT forensic applications, combining
interoperability and scalability.
FIGURE 8. Blockchain platforms.
In Figure 8, a significant portion of studies is categorized under ‘No information’ regarding the blockchain
platforms used. This classification reflects studies that propose conceptual models or architectures without specifying
a particular blockchain network or infrastructure. These
works often focus on the design and theoretical aspects of
blockchain-based chain of custody (CoC) management but
stop short of detailing the technical implementation. As a
result, the proposed models are considered generic and can
potentially be adapted to various blockchain technologies,
such as Ethereum, Hyperledger Fabric, or Exonum, if practically implemented.
B. RQ2: WHICH APPROACHES AND/OR TECHNIQUES
ARE USED TO MANAGE A CHAIN OF CUSTODY OF
EVIDENCE IN DIGITAL FORENSICS?
The management of the chain of custody in digital forensics
is fundamental to ensure the integrity and authenticity
of evidence throughout the entire investigative process.
To answer RQ2, the content was divided into two subsections:
the first addresses the approaches and techniques advocated
by the authors, while the second discusses the evaluations and
experiments carried out with these techniques.
1) APPROACHES AND TECHNIQUES
The approaches and techniques proposed by the authors were
classified and organized according to their abstraction, from
the most concrete to the most conceptual. The distribution
of the works is illustrated in Figure 9, which presents the
categories and the number of articles in each of them, and
then presents an individual analysis:
• System: A system represents the practical implementation of a proposal, encompassing an operational context that integrates architecture, frameworks,
programs, and data, as defined by Tanenbaum and
Bos [103]. Twelve articles presented their solutions
at this level, demonstrating complete and operational
implementations.
• Framework: A framework provides a systematic guide
for implementing solutions, promoting interoperability,
security, and consistency across systems built on a
common foundation [104]. Eleven studies proposed
frameworks, offering sufficient detail to serve as
reusable and adaptable solutions.
• Architecture: An architecture offers a functional
and descriptive representation of a solution, often
illustrated through block diagrams and supported by
libraries. Seven studies were classified in this category,
although some architectures exhibited characteristics
of frameworks, such as the proposal by Philip and
Saravanaguru [94].
• Model: A model provides an abstract, conceptual overview of a solution, describing functional
blocks and their interactions with external systems.
Nine articles proposed models as their primary
approach, emphasizing the conceptual foundation over
implementation.
In summary, the analyzed proposals varied in levels
of detail and implementation, ranging from conceptual
descriptions to fully implemented systems, as illustrated in
Figure 9.
FIGURE 9. Approaches and techniques for chain of custody management.
2) EVALUATIONS AND EXPERIMENTS CONDUCTED ON THE
TECHNIQUES
The evaluations and experiments in the analyzed articles were
conducted using different approaches, such as specification
and construction of prototypes, simulations, and definition
of use cases. The distribution of the types of evaluations
performed is illustrated in Figure 10.
FIGURE 10. Types of evaluations performed.
Among the analyzed articles, seven did not present
practical experiments or clear information about evaluations, although some discussed theoretical challenges and
potential solutions. On the other hand, twenty-two studies
conducted experiments with prototypes to evaluate aspects
such as latency, number of supported transactions, scalability,
security, and privacy. In the works that used the public
Ethereum network, gas/energy cost was frequently addressed
as a relevant concern [84], [94], [96]. In contrast, other studies
that also employed Ethereum did not explore this aspect [86],
[93], [99].
Philip and Saravanaguru [94] used the Rinkeby test
network of Ethereum, which was discontinued in 2022.11 Li
et al. [83] presented LEChain, which prioritized privacy and
security, employing post-quantum cryptography. They evaluated performance in various stages of the evidence lifecycle,
including registration, collection, upload, verification, and
access.
In general, the experiments performed can be categorized
into:
• Prototypes: Evaluated the practical feasibility of the
solutions, with tests in controlled environments to verify
performance and functionality. Twenty-two works were
presented in this category.
• Simulations: Used to model scenarios with high
transaction volume, evaluating aspects such as latency,
security, and scalability. Ten works were included in this
category.
• Use Cases: Practical applications in specific scenarios,
aiming to validate the applicability of the proposed
solutions. This category included five works.
It is relevant to highlight that some studies [50], [70],
[79], [80], [95] combined prototypes and simulations in their
experiments.
The tools widely used in the evaluations include:
• Hyperledger Caliper: A tool for testing performance
in private networks and analyzing smart contracts,
preferably in Hyperledger Fabric. Six studies used
Hyperledger Caliper.
• Rinkeby and Mumbai Testnet Networks: Test environments for Ethereum networks, used to measure gas
costs and efficiency. Both tools were employed in one
work each.
• Fuzzy Hashing: A tool used to detect changes and verify
the integrity of evidence. One work presented results
with this approach.
• Hyperledger Playground: An environment used to
simulate and debug smart contracts before practical
implementations. One work used this tool.
The results indicated that blockchain technology significantly contributes to improving transparency, authenticity,
and security in the management of the chain of custody
of forensic evidence. However, challenges such as high
computational cost, implementation complexity, and interoperability problems between platforms still need to be
overcome to enable wider adoption in practical applications.
It is important to clarify that the ‘No information’ category
in Figure 10 refers to studies that did not provide explicit
details about how their proposed models, architectures,
frameworks, or systems were evaluated. These studies
often focus on presenting theoretical models or conceptual
architectures without implementing them or conducting
practical validations such as simulations or prototype testing.
11https://blog.ethereum.org/2022/06/21/testnet-deprecation
As a result, it was not possible to determine the type of
evaluation applied, leading to their classification under ‘No
information’.
This categorization does not imply that these studies lack
value but rather highlights that they are primarily conceptual
and may require future work for empirical validation. In many
cases, authors suggest that practical implementation and evaluation are intended as part of their future research directions.
C. RQ3: WHICH CHAIN OF CUSTODY COMPONENTS ARE
PRESERVED USING BLOCKCHAIN?
Before examining the results related to this question, it is
necessary to define and differentiate some fundamental
terms. Preserving digital evidence throughout its entire life
cycle requires proof that it has not been altered, or if it
has, that it occurred for a justified reason. Well-established
forensic procedures are applied to address this concern [16].
In particular, preserving the chain of custody, especially
in the digital context, calls for specific techniques and
procedures [105]. This study takes into account attributes and
properties associated with preserving the chain of custody.
To answer RQ3, the following aspects were considered:
• Phases of digital forensics, according to NIST
SP 800-86 [18]: collection, examination, analysis, and
reporting.
• Essential metadata that answer the questions related to
the Chain of Custody (CoC): who, what, when, where,
why, and how.
• Types of supported evidence: data and information
related to ‘‘Generic Digital Evidence’’, ‘‘Evidence from
Judicial/Police Systems’’, ‘‘IoT Device Data, Mobile
Phones, Multimedia and Cloud Logs’’.
1) PHASES OF DIGITAL FORENSICS
The analyzed proposals address different phases of the digital
evidence life cycle. Some cover specific stages, whereas
others encompass the entire process. The distribution of
works across each phase is shown in Figure 11. For better
visualization of the image, the category is displayed over two
lines.
The digital forensics phases include:
• Data Collection: Covered by all thirty-nine analyzed
articles, this phase involves the identification, labeling,
logging, and acquisition of data from relevant sources,
following rigorous procedures to ensure data integrity
from its origin to initial storage.
• Examination: Involves processing the collected data
using both automated and manual methods to assess and
extract relevant information. This stage is addressed in
fifteen articles.
• Analysis: At this stage, the processed data are examined
using legally justifiable methods and techniques to
identify and correlate people, objects, events, locations,
and actions. The goal is to answer the investigative
questions that motivated the collection and examination.
Twenty-six articles address this phase.
FIGURE 11. Digital forensics phases.
• Reporting: This phase consists of presenting the results
obtained in the previous phases. Reports may include
a detailed description of the procedures performed,
justification of the tools and processes used, attached
evidence, and recommendations to enhance forensic
policies and processes. Eighteen works discuss this
phase.
According to NIST SP 800-86 [18], a complete forensic
system should cover all the aforementioned phases. Among
the analyzed articles, only fourteen address all stages of
the evidence life cycle, with special emphasis on ensuring
continuity and transparency in each phase.
2) CHAIN OF CUSTODY METADATA
Trace-tracking steps in a chain of custody (CoC) are
fundamental to ensuring the integrity and authenticity of
evidence throughout its life cycle. Brazilian Law No. 13,964
[23], in Article 158-B, precisely details the elements that must
be documented in a chain of custody. These elements translate
into essential metadata that support the chronological history
of evidence. As discussed in Section II-A3, this metadata
should address questions such as: who, what, when, where,
why, and how [27], [105].
This analysis examined whether the authors included
storage of the metadata necessary to manage the chain of
custody. When adding a digital trace, the following aspects
should be recorded, as illustrated in Figure 12:
• Who: Identification of the individual, system, or entity
responsible for collecting, analyzing, or transferring the
evidence; mentioned by 37 articles.
• What: Nature of the evidence (data, logs, files, etc.);
addressed by 32 articles.
• When: Exact date and time of collection, analysis,
or transfer; reported by 32 studies.
• Where: The physical or digital location from which
the evidence was extracted, analyzed, or transferred;
mentioned by 24 articles.
• Why: Justification for the collection, analysis, or transfer (judicial warrant, automated monitoring, etc.);
addressed by 11 articles.
• How: Collection, analysis, or transfer method (manual
or automated); contextualized in 16 articles.
Although most proposals (37 articles) record information
on ‘‘who’’ interacted with the evidence, comprehensive CoC
management requires all the aforementioned metadata. Only
FIGURE 12. Chain of custody metadata.
ten articles thoroughly addressed all metadata, as shown in
Figure 12. This gap is especially noteworthy because incomplete metadata recording may compromise the traceability
and validity of evidence in judicial proceedings.
A critical point observed is that many proposals associate
the moment of collection with the timestamp of block
creation in the blockchain. However, this record might not
accurately reflect the reality of systems collecting evidence
from different types and sources, such as IoT devices,
network logs, or multimedia files [106].
Another significant challenge involves storing additional
CoC-related information, which requires substantial storage
capacity. This issue is particularly critical in permissionless
blockchains, where storage costs are higher. As more
metadata are incorporated, the complexity of data management in the blockchain likewise increases, potentially
FIGURE 13. Types of supported evidence.
explaining why many authors opt to record only essential
metadata, such as ‘‘who’’ and ‘‘when.’’
3) TYPES OF SUPPORTED EVIDENCE
The types of supported evidence can be grouped into three
main categories, as illustrated in Figure 13, and the following
aspects should be exposed:
• Generic Digital Evidence: Ten articles addressed
digital evidence without specifying exact sources or
data types. This approach covers a broad range of
information, such as system logs, digital files, and other
electronic traces. The generality of this classification
reflects the versatility of forensic methods, applicable
to diverse forms of digital data regardless of origin or
nature.
• Evidence from Judicial/Police Systems: Nine articles
discuss the use of evidence extracted from integrated
systems employed by judicial and law enforcement
authorities. These systems are designed to collect, store,
and analyze data related to investigations, such as
crime scene records, procedural information, and other
sensitive data. Although many studies did not specify
the exact type of data analyzed, they highlight the
challenges faced in managing large volumes of sensitive
information and in processes requiring evidence traceability and integrity.
• IoT Device Data, Mobile Phones, Multimedia, and
Cloud Logs: Eighteen articles examine the collection
and use of data originating from IoT devices, mobile
devices (phones), cloud logs, and multimedia systems.
This category also includes evidence obtained from
social networks, such as videos, audio, images, and
posts. These data are crucial for investigations because
they shed light on behaviors, communications, and
activities that may be relevant to identifying suspects or
reconstructing events.
Two articles did not provide sufficient details about the
types of evidence or data analyzed, limiting themselves to
discussing general aspects of the forensic process [98], [102].
These works focused more on frameworks or methods for
chain of custody management rather than on categorizing the
evidence itself.
The diversity of evidence types addressed in the analyzed
articles reflects the complexity and dynamism of modern
forensic investigations. Digital evidence, in its various forms,
plays a critical role in investigations, ranging from generic
logs to more specialized data.
D. RQ4: WHICH SECURITY REQUIREMENTS ARE
PROVIDED BY THE AUTHORS’ PROPOSALS?
A chain of custody (CoC) is the record of actions taken
on digital traces and evidence that may support judicial
proceedings or investigations related to malicious conduct,
such as in cybersecurity incident response procedures.
The IETF Request for Comments 3227 (RFC 3227) [107]
describes the characteristics that a digital trace must possess
in order to be considered digital evidence:
• Admissibility
• Authenticity
• Completeness
• Reliability
• Credibility
These characteristics are ensured by specific security
properties. Thus, in this work, properties were considered
that fulfill the requirements of a CoC admissible in court,
in addition to others relevant in specific contexts, such as
privacy. Figure 14 shows the number of articles that reference
or use each property, described below:
• Authorization: Only agents or individuals with the
appropriate access level can manage the CoC, for
instance, to include information on the movement
of digital traces. Authorization is the mechanism
that restricts access according to policies defined
internally. Nineteen proposals used this security
property.
• Authentication: Requires all entities interacting with
the evidence to prove their identity irrefutably. In public
blockchains (e.g., Ethereum), there are no native authentication mechanisms, whereas private or consortium
blockchains require authentication before any transaction. Twenty-three proposals employed this property.
• Integrity: Ensures that event data and evidence are
not altered during transfer or analysis. This property
is guaranteed by using hash functions on the input
data. Thirty-four proposals took this property into
consideration.
• Traceability: Makes it possible to record all information
related to the history of the evidence, from collection
to destruction. The blockchain logs this information
through the world state component, which retains the
FIGURE 14. Types of security requirements.
current values of the keys in the transaction log. Thirtytwo proposals adopted this property.
• Confidentiality: Ensures that only authorized individuals or systems can access sensitive information,
implemented through access control mechanisms.
Twenty-seven proposals addressed this requirement.
• Privacy: Complies with legal regulations such as the
GDPR and Brazil’s LGPD, ensuring that personal
and sensitive data are handled securely. In public
blockchains, this may conflict with the principle of
open access, but solutions such as anonymization and
multi-layered blockchains are employed to address
the issue [83], [84]. Twelve proposals provided this
property.
• Verifiability: Allows all transactions and interactions recorded in the CoC to be verifiable, ensuring
compliance with domain requirements. Twenty-seven
proposals employed this property.
• Immutability: Guarantees that the metadata associated
with the evidence history cannot be altered. This is one
of the crucial aspects provided by blockchain technology, which is why all thirty-nine studies presented this
security requirement.
Authentication is fundamental to ensuring that only
identified users or systems can interact with the blockchain,
whereas authorization defines the different levels of access
for various actors, such as in the judicial context, where
multiple entities require distinct degrees of access [41], [68],
[83].
Confidentiality and privacy rely directly on robust access
control [72], [84]. However, public blockchains face additional challenges, given that the goal of free access may
conflict with privacy requirements. In contrast, private or
consortium blockchains offer greater flexibility to implement
access restrictions aligned with applicable regulations.
Finally, immutability, an intrinsic characteristic of
blockchain technology, stands out as the most widely adopted
property, reflecting its importance in chain of custody
management [101], [102]. Nevertheless, achieving a balance
among all the listed properties remains a technical and
practical challenge in forensic systems.
E. OTHER PROPERTIES FOR CHARACTERIZING THE
PROPOSALS
Some other properties are important to characterize proposals
and also to define the scopes of the work areas. We divided
them into four subsections to talk about Operationalization of
evidence (Subsections V-E1), Storage of evidence (Subsections V-E2), and Collection of evidence (Subsections V-E3).
1) OPERATIONALIZATION OF EVIDENCE
How the system operationalizes the evidence is a crucial
aspect of chain of custody management, particularly in
forensic contexts. Figure 15 provides an overview of the
operationalization models identified in the analyzed articles.
Generally, when collection is carried out in response
to specific events–such as cyber incidents, court warrants,
or vehicular accidents–the system is organized around
cases [91], [100]. This model, addressed by twenty-six
proposals, primarily supports manual collection, although
it may also include additional methods for automated data
acquisition. These proposals highlight the importance of a
structured forensic cycle in which the collection, analysis,
and preservation of evidence occur sequentially and are
thoroughly documented.
In contrast, thirteen proposals addressed the collection and
storage of evidence without following a clearly defined, endto-end forensic cycle consisting of collection, examination,
analysis, and reporting. In these approaches, the focus is on
preserving the immutability and integrity of records, ensuring
that data remain available for analysis or future use, even
if their specific purpose is not established at the time of
collection [69], [90], [98].
The results suggest that both approaches play complementary roles in forensic contexts. Case-based operationalization is ideal for structured investigations, whereas generic
approaches provide the flexibility to capture and preserve
data that may be relevant in unpredictable situations.
2) EVIDENCE STORAGE
The storage of evidence is a fundamental aspect of digital
forensics and the evidence life cycle, especially when
blockchain is employed. Blockchain platforms have security
FIGURE 15. Operationalization of evidence.
properties, such as immutability, that are highly suitable for
the forensic context. However, they present limitations in
terms of storage capacity. For this reason, digital evidence
is often stored externally, while the blockchain records
metadata, cryptographic hashes, or references to the original
data.
To ensure the integrity and availability of digital evidence,
different storage mechanisms have been proposed in the
literature. The analyzed articles highlight the following
storage media, as summarized in Figure 16:
• Cloud: Cloud computing platforms provide varying
levels of security, redundancy, and scalability, making
them a common choice for forensic evidence storage.
The integration of secure cloud services enables greater
flexibility for handling large datasets. However, cloudbased storage introduces trust dependency on third-party
providers and requires cryptographic guarantees. This
approach was used in 12 proposals.
• IPFS (Interplanetary File System): A distributed and
decentralized storage system that eliminates the need
for a central entity, such as a database. In IPFS,12 data
are split into blocks and stored on a peer-to-peer (P2P)
network, ensuring resilience and availability. However,
data persistence is not natively guaranteed, requiring
services from third-party providers to prevent data loss.
This technique was found in 9 proposals.
• Swarm: Similar to IPFS, Swarm13 is a distributed
storage system designed for blockchain interoperability.
Unlike IPFS, Swarm integrates built-in incentivization
mechanisms for data permanence, ensuring long-term
availability of forensic records. This approach was used
in only one study [81].
• Blockchain: Some works attempted to store digital
evidence directly on-chain due to its immutability
and decentralized nature. However, due to storage
limitations and high transaction costs, this approach
is not feasible for large forensic datasets. The three
works in this category did not specify external storage
mechanisms, assuming the blockchain as the primary
storage location.
• Other: This category includes centralized storage
solutions such as traditional databases, hard drives, and
local storage servers, called off-chain system. These
systems offer advantages such as better transaction
performance, access control policies, and compliance
12https://ipfs.tech/
13https://www.ethswarm.org/
with existing legal frameworks. Centralized storage is
often used in hybrid blockchain architectures, where
sensitive forensic information is stored off-chain while
cryptographic proofs or hashes are anchored on-chain
for integrity verification [108]. This approach was
identified in 14 proposals.
FIGURE 16. Evidence storage.
a: ENSURING THE INTEGRITY OF OFF-CHAIN EVIDENCE
STORAGE
Ensuring the integrity and authenticity of off-chain stored
evidence is a major challenge in forensic applications. The
reviewed works propose various cryptographic techniques to
address these issues:
• Hash Anchoring: The most common technique
involves storing cryptographic hashes (SHA-256, SHA3) of the original evidence on the blockchain. This
approach allows forensic investigators to verify that the
evidence has not been altered without including the full
on-chain data [72], [89].
• Merkle Trees and Merkle Proofs: Some works
leverage Merkle trees to generate compact and efficient
integrity proofs. A Merkle root is stored on-chain,
while the original data remains off-chain. Investigators
can provide Merkle proofs to confirm the integrity of
evidence without revealing the full dataset [68], [95].
• Decentralized Identifiers (DIDs) and Verifiable Credentials (VCs): DIDs enable a decentralized and
tamper-resistant method for uniquely identifying forensic evidence stored off-chain. When combined with
Verifiable Credentials (VCs), VCs allow trusted forensic
authorities to issue cryptographic attestations about
the validity, origin, and integrity of stored evidence.
FIGURE 17. Evidence collection.
These credentials can be verified independently without
relying on centralized trust anchors [48], [50].
The choice of off-chain storage mechanism depends on
multiple factors, including evidence sensitivity, regulatory
requirements, and scalability needs. Hybrid approaches,
which combine decentralized identifiers (DIDs), cryptographic hash anchoring, and verifiable credentials (VCs),
have demonstrated strong potential as a next-generation way
to protect off-chain forensic evidence while maintaining
privacy, scalability, and legal compliance.
3) EVIDENCE COLLECTION
An essential aspect highlighted in the analyzed proposals
is the type of evidence collection, which is often closely
tied to the goals and application context of each system.
For instance, in systems designed for collecting cloud-based
evidence, automatic data collection through APIs or logs
is typically the most suitable approach, ensuring efficiency
and scalability. Conversely, forensic systems tailored for
judicial applications, where processes are clearly defined
and controlled, often rely on manual collection or online
methods, including APIs, to ensure compliance with legal and
procedural standards.
Figure 17 illustrates the categorization of the types of
evidence collection identified in the reviewed articles. The
analyzed articles were classified into five main categories of
collection:
• Manual: Used in 29 proposals, generally associated
with judicial forensic systems or situations in which
collection must be carried out by a trained operator.
• Application (App): Includes automatic data collection
through specific applications, adopted by 9 proposals.
• Online (Capturing records and logs): Involves automatic capture of events and logs directly from systems,
used in 12 proposals.
• Online (Via API): Refers to data inclusion through
APIs, with support for integration and automation,
identified in 16 proposals.
On the other hand, it should be mentioned that 3 proposals
did not provide details on the collection method used.
It should be noted that 22 works support multiple collection
types. For example, the proposal by Li et al. [84] included
different collection methods to meet the needs of a forensic
system focused on vehicular accidents.
The results indicate diverse collection approaches, reflecting the different needs and forensic contexts. While manual
collection is widely used in systems with strict control
requirements, such as judicial applications, automatic and
API-based methods have proven advantageous in scenarios
involving large data volumes or integration needs, such
as cloud and IoT environments. Ultimately, the choice of
method directly depends on the system’s characteristics and
the type of evidence to be collected.
F. COMPARISON OF THE WORKS
Below is a summary comparing the works resulting from
the systematic mapping, taking into account the research
questions in Subsections V-A, V-B, V-C, and V-D, in addition
to the further analyses presented in Subsection V-E.
Table 5 presents a summary of all the selected works
resulting from the review and the corresponding fields
referenced by the research questions. Where any data are
missing, it is reported as No Information (NI) or marked with
‘‘-’’. For better visualization in summarizing all the articles,
some identifiers and uses have been defined, as described
below:
• Research Question 1 [RQ1] – Blockchain Technologies:
- Blockchain Model [BlMod]:
∗ Private (Priv);
∗ Public (Pub);
∗ Hybrid (Hyb).
- Blockchain Platform [BlPlat]:
∗ Ethereum (ETH);
∗ Hyperledger Fabric (HFa);
∗ Hyperledger Sawtooth (HSa);
∗ Hyperledger Composer (HCo);
∗ Hyperledger Indy (HIn);
∗ Hyperledger Aries (HAr);
∗ Spidernet (Spi);
∗ Polygon (Pol);
∗ Scrybe (Scr).
• Research Question 2 [RQ2] – Approaches/Techniques
for Evidence Management:
- Approaches/Techniques [Appr.]:
∗ System (Sys);
∗ Framework (Fra);
∗ Architecture (Arc);
∗ Model (Mod).
- Type and Features of Experiments [Exper.]:
∗ Prototype (Prot);
∗ Use Case (UseC);
∗ Simulation (Simu);
TABLE 5. Comparison between works.
∗ Fuzzy Hash (Fuzz);
∗ Hyperledger Caliper (HCal);
∗ Hyperledger Composer (HCo);
∗ Rinkeby Network (Rink);
∗ Mumbai Testnet Network (Mumb);
∗ Hyperledger Playground (HPlay).
• Research Question 3 [RQ3] – Chain of Custody
Components Preserved:
- Phases of Digital Forensics (digital evidence management) [Phases]:
∗ Collection (C);
∗ Examination (E);
∗ Analysis (A);
∗ Reporting (R).
- Chain of Custody Metadata (CoC) [Chain of Custody]:
∗ Who (Wo);
∗ What (Wa);
∗ When (We);
∗ Where (Wr);
∗ Why (Wy);
∗ How (H).
- Types of Evidence Supported [TpEvid]:
∗ Generic Digital Evidence (Gen);
∗ Evidence from Judicial/Police Systems (Jud);
∗ IoT Device Data, Mobile Phones, Multimedia,
and Cloud Logs (Data).
• Research Question 4 [RQ4] – Security Requirements
[Security Requirements]:
- Immutability (Imm);
- Verifiability (Ver);
- Privacy (Prv);
- Confidentiality (Con);
- Traceability (Tra);
- Integrity (Int);
- Authentication (Atn);
- Authorization (Atz).
• Other Properties of the Works:
- Type of Chain of Custody Operationalization
[OpCoC]:
∗ By Evidence (Evi);
∗ By Cases (Cas).
- Storage of Evidence [Stor.]:
∗ Cloud (Cld);
∗ IPFS (IPFS);
∗ Swarm (Swa);
∗ Blockchain (Blo);
∗ Other (Oth).
- Type of Evidence Collection [TpColl]:
∗ Manual (Man);
∗ Application (App);
∗ Online (logs) (Log);
∗ Online (via API) (API).
VI. DISCUSSION
In this section, we present a systematic analysis of the
selected articles, highlighting their main contributions, characteristics, and limitations. In Subsection VI-A, we generally
discuss the strengths and weaknesses of the analyzed works.
Subsection VI-B presents the identified gaps for future
research, while Subsection IV-A6 addresses threats to the
validity of this study. Finally, Subsection VI-C and VI-D
discusses this work’s limitations.
A. GENERAL CONTRIBUTIONS AND LIMITATIONS OF THE
WORKS
The analysis of the selected articles revealed relevant
contributions to understanding the state of the art in preserving and managing the chain of custody (CoC) of digital
evidence using blockchain and Self-Sovereign Identities
(SSI). An initial distinction concerns the choice of blockchain
model (public, private, or consortium) employed in each
approach.
The choice of a particular blockchain model directly
impacts the security requirements of the proposals. Properties
such as privacy, verifiability, and confidentiality depend on
the chosen architecture [108]. For example, Li et al. [84] used
Ethereum blockchain with a consortium among entities to
address the forensic context of vehicular accidents, covering
requirements such as authentication and access control.
Works like Li et al. [86] and Philip and Saravanaguru [94]
used Ethereum blockchain with public network, but needed
additional cryptographic mechanisms to provide privacy and
access control.
Solutions based on permissioned blockchains offer built-in
support for authentication and authorization, facilitating
the implementation of confidentiality and access control
requirements [68], [69], [78], [89]. These platforms allow for
more efficient access policies, especially in contexts where
evidence privacy is essential.
The results suggest that private networks present advantages over public and consortium-based blockchains by
eliminating transaction fees and reducing the need for extra
cryptographic measures for security, particularly regarding
privacy and access control requirements related to evidence.
Scalability and transaction costs are critical factors,
especially in public blockchains such as Ethereum [70],
[86], [94], [96], [100]. While they provide transparency
and auditability, their high costs and processing times limit
large-scale applications. Works like that of Rana et al.
[41] aimed to circumvent these limitations by using the
Polygon blockchain, known for its reduced fees and greater
scalability, though it has seen little use in the academic
community.
Another critical factor that must be taken into consideration
is the use of off-chain storage strategies in digital evidence
chain of custody (CoC) applications [50], [68], [89], [90],
[95]. Works such as those by Akbarfam et al. [68], Lusetti
et al. [89] and Lv et al. [90] propose hybrid platforms that use
off-chain storage combined with blockchain to ensure data
integrity, recording only metadata on the chain.
The authors highlight that storing all data directly on the
blockchain presents major challenges, especially in relation
to real-time data management, due to the bottleneck of
commits in the network. This problem can compromise
the performance and scalability of the system, making
the exclusive use of on-chain storage unfeasible for large
volumes of data.
This analysis highlights the need for robust and scalable
approaches for off-chain storage in digital evidence chain
of custody applications. Such solutions must consider not
only data integrity, but also the security of off-chain storage
and performance in environments with large volumes of
information.
Integrating with technologies such as decentralized storage
systems (e.g., IPFS) and artificial intelligence tools for
evidence analysis can increase the effectiveness of the
proposals. Some works explored decentralized storage to
ensure availability and integrity of evidence [74], [75], [80],
[87], [88], [90], [92], [94], [96]. However, the application
of artificial intelligence remains incipient and represents a
promising field for future research [69], [86], [98].
As analyzed in Subsections V-E1 and V-C1, some works
focus on CoC management around specific cases, supporting
all phases of the forensic process (collection, examination,
analysis, and reporting – C/E/A/R). Fourteen works provided
full support to the forensic process phases [67], [68], [72],
[78], [81], [83], [84], [85], [86], [88], [89], [93], [94], [100].
On the other hand, approaches centered on individual
digital traces generally restrict themselves to the initial steps,
such as collection and secure storage, or do not fully address
the forensic process phases.
Regarding comprehensive chain of custody management,
eight works proposed approaches covering all phases
of the forensic process (C/E/A/R) and meeting security
requirements [67], [68], [78], [81], [83], [84], [85], [89].
Nevertheless, the following challenges and limitations stand
out among the analyzed proposals:
• Use of discontinued or not widely available blockchain
platforms [81];
• Application of advanced cryptographic protocols
(e.g., CP-ABE, TRS) to provide security, which can
increase managerial and computational complexity [83],
[84], [85];
• High transaction costs in blockchains like Ethereum [83],
[84];
• Narrow focus on specific contexts, limiting the generalization of solutions [84], [85];
• Absence of certain essential metadata needed to preserve
the chain of custody [67], [68], [81], [85].
Only two works [78], [89] presented a comprehensive,
secure, and complete approach to preserving and managing
the CoC of digital evidence. However, neither addressed the
use of Self-Sovereign Identity (SSI).
On the other hand, among all the analyzed works, only the
one by Dos Santos, Loffi, and Westphall [50] incorporated the
use of SSI, Decentralized Identifiers (DIDs), and Verifiable
Credentials (VCs) to enhance authentication and access
control mechanisms, increasing security and privacy in
CoC management. Their proposal introduces a gateway
architecture for IoT environments, where DIDs uniquely
identify IoT devices and VCs certify the authenticity of the
data emitted by these devices.
This approach brings significant advancements by:
• Utilizing Hyperledger Indy and Aries to implement SSIbased authentication;
• Establishing DIDs for IoT devices, ensuring traceability
and immutability in forensic evidence;
• Issuing VCs that attest to data integrity and ownership,
enabling verifiable digital evidence;
• Proposing a cloud-based agent system for issuing and
managing verifiable credentials.
Despite these contributions in Dos Santos, Loffi, and
Westphall [50], the study still presents some limitations in
the context of forensic chain of custody:
• The focus is primarily on IoT forensic evidence, not
covering the full forensic lifecycle;
• The approach does not integrate access control to
manage forensic actors dynamically with Verifiable
Credentials (VCs);
• The metadata coverage in the CoC process is not
fully addressed, missing key elements such as evidence
transfer and regulatory compliance.
Although significant progress has been made in using
blockchain for CoC preservation and management, challenges such as scalability, interoperability, and metadata completeness remain open issues. The integration of SSI, DIDs,
and VCs presents promising opportunities to strengthen
existing solutions and explore new possibilities in digital
forensics.
B. GAPS
The analyzed works reveal several open research directions
and unresolved challenges in applying blockchain and related
technologies to the management of digital evidence. These
gaps highlight both the limitations of current approaches
and the inherent complexities of integrating decentralized
technologies into forensic environments.
1) LACK OF PRACTICAL IMPLEMENTATION AND
EVALUATION IN REAL ENVIRONMENTS
One of the main identified gaps is the absence of practical
implementations or evaluations in real environments. Works
such as those by Elgohary et al. [78] and Li et al. [85]
developed conceptual models without practical validation,
raising questions about the feasibility and performance
of their proposals. This limitation hinders the translation
of solutions into operational contexts and reduces their
applicability in the real world.
2) CRYPTOGRAPHIC COMPLEXITY AND IMPACT ON
PERFORMANCE
The integration of advanced cryptographic mechanisms, such
as ciphertext-policy attribute-based encryption (CP-ABE)
and zero-knowledge proofs (ZKPs), increases security but
also introduces computational overhead. These techniques
demand significant resources, which may affect system
performance, particularly in high-throughput forensic environments [83], [84].
3) CONFIDENTIALITY IN PUBLIC BLOCKCHAINS
The use of public blockchains presents confidentiality
challenges, as transactions are visible to any user. While
works like that of Rana et al. [41] acknowledge this
issue, effective privacy-preserving mechanisms—such as zkSNARKs, ring signatures, or trusted execution environments
(TEEs)—remain underexplored in the forensic domain.
4) ENTITY MANAGEMENT AND ROLE-BASED ACCESS
CONTROL
Managing different entities with distinct access levels
to forensic evidence is another challenge. While some
works [85], [90] explore granular access control, they lack
dynamic role-based models capable of handling multi-actor
environments with evolving permissions.
5) COMPREHENSIVE COVERAGE OF THE FORENSIC
PROCESS
An important gap is the lack of full coverage of the forensic
process phases, including collection, examination, analysis,
and reporting (C/E/A/R). Studies such as those by Olukoya
et al. [91], Ottakath et al. [92], and Rana et al. [41] focus only
on isolated aspects, neglecting the integration of the entire
digital evidence lifecycle.
6) PRIVACY AND DOCUMENTATION OF THE FORENSIC
PROCESS
Documenting all forensic process phases without compromising the privacy of the parties involved also proved to be a
significant challenge. Proposals like that of Zhang et al. [102],
which use ring signatures with traceability, offer promising
solutions; however, the associated cryptographic complexity
can hinder large-scale implementation.
7) ACCESS CONTROL IN DECENTRALIZED STORAGE
SYSTEMS
The reliance on InterPlanetary File System (IPFS) and other
decentralized storage solutions for evidence management
raises concerns regarding access control, data retention
policies, and confidentiality [93], [94]. There is a need for
robust privacy-preserving mechanisms in distributed forensic
architectures.
8) OFF-CHAIN SECURE EVIDENCE STORAGE
A major research gap is the lack of secure off-chain
storage solutions for forensic evidence. Instead of storing
raw evidence directly on-chain, only cryptographic hashes
and unique identifiers should be publicly accessible. The
actual data should reside in secure, owner-controlled storage
protected by Verifiable Credentials (VCs), ensuring that only
authorized entities can retrieve and verify the evidence.
9) INTEROPERABILITY AND CROSS-BLOCKCHAIN
COMMUNICATION
Interoperability among different blockchain platforms
remains an unsolved challenge. Current forensic frameworks
lack mechanisms to exchange forensic data between
multiple blockchain networks in a seamless and standardized
manner [41], [77], [91]. Without interoperability, forensic
collaboration across jurisdictions and organizations is
significantly hindered.
10) METADATA MANAGEMENT FOR DIGITAL EVIDENCE
Fully managing evidence metadata also presents important
gaps. Although some articles address the essential 5W1H
(Who, What, When, Where, Why, and How) metadata [79],
[96], there is a growing need to include new elements, such
as ‘‘Context’’, which can encompass stages like ‘‘collection’’, ‘‘received’’, ‘‘after analysis/examination’’, ‘‘transfer’’,
‘‘return’’, and ‘‘disposal’’ [26]. These elements are essential
for ensuring comprehensive and reliable traceability in the
daily activities of forensic institutes and agencies.
11) SCALABILITY AND PERFORMANCE IN PERMISSIONED
BLOCKCHAINS
While permissioned blockchains provide better security and
governance, scalability remains a challenge. There is a
lack of detailed studies analyzing how to handle large
volumes of forensic data and transactions without compromising efficiency, especially in high-demand environments
[77], [81].
12) INTEGRATING SELF-SOVEREIGN IDENTITIES (SSI)
A key gap is the lack of research on the integration of
Self-Sovereign Identity (SSI) into the forensic evidence
lifecycle. Only one study [50] explored SSI, but its focus
was limited to individual digital traces rather than a
comprehensive CoC framework incorporating authentication,
access control, and metadata validation.
13) DEFINING DECENTRALIZED IDENTIFIERS (DIDS) FOR
DIGITAL EVIDENCE
There is an urgent need to define a standardized Decentralized Identifier (DID) framework specifically for forensic
evidence. Additionally, separate DIDs for entities involved in
the forensic process (e.g., investigators, institutions, and regulatory bodies) must be established to ensure accountability
and traceability.
14) ACCESS CONTROL WITH VERIFIABLE CREDENTIALS
The development of Verifiable Credentials (VCs) tailored for
forensic access control is another unexplored area. Specific
credentials should be created to regulate:
• Who can access, analyze, and modify evidence.
• Under what conditions access permissions are granted
or revoked.
• How evidence access logs can be verified for forensic
audits.
15) VERIFIABLE CREDENTIALS FOR EVIDENCE METADATA
Finally, there is a need to create dedicated Verifiable Credentials (VCs) to manage 5W1H-related forensic metadata.
These credentials should provide cryptographically verifiable
attestations regarding the integrity, origin, and handling of
digital evidence throughout its lifecycle.
16) FUTURE RESEARCH DIRECTIONS
While significant advancements have been made in applying
blockchain to digital evidence management, these gaps
highlight the need for further research into scalable, interoperable, and privacy-preserving solutions. The integration
of Self-Sovereign Identity (SSI), Decentralized Identifiers
(DIDs), and advanced cryptographic techniques presents a
promising avenue for strengthening forensic investigations
and ensuring the integrity of the chain of custody.
C. LIMITATIONS OF THIS SYSTEMATIC REVIEW
This study has certain limitations inherent to the systematic
review process. Among them are:
• Limitation to selected databases: The research was
conducted solely in electronic academic databases such
as SpringerLink, ScienceDirect, IEEE Xplore, and ACM
Digital Library. Although these are widely recognized,
other academic databases may contain relevant articles
that were not considered.
• Use of specific keywords: The investigation used keywords such as ‘‘evidence’’, ‘‘forensic’’, ‘‘blockchain’’,
‘‘distributed ledger’’, ‘‘smart contracts’’, ‘‘decentralized
identifiers’’, ‘‘self-sovereign’’, and ‘‘verifiable credentials’’. Despite encompassing essential terms, there is a
possibility of excluding relevant works that use different
terminology.
• Exclusion of publications in languages other than
English: Only articles published in English were
included, which may have led to the omission of relevant
studies in other languages, especially in languages such
as Chinese, Spanish, or Portuguese.
• Focus on academic literature: Practical studies, technical reports, or industry publications were not considered,
limiting the review’s scope to works published in purely
academic settings.
• Access restrictions: Some relevant works may not have
been included due to access limitations in the institutional subscription to academic databases, preventing
the review of potentially important contributions.
• Variability in methodological rigor: The reviewed
studies exhibit varying degrees of methodological rigor,
with some lacking empirical validation, real-world
implementations, or comprehensive evaluations, which
may introduce biases in the findings.
Despite these limitations, rigorous measures were implemented to ensure the quality and relevance of the selected
works. Future studies could expand the scope of this review
by incorporating additional databases, refining keyword
selection, and including a broader range of publication
types and languages. This would provide a more comprehensive and representative view of the state of the
art in blockchain-based forensic chain of custody (CoC)
management.
D. LIMITATIONS OF THE REVIEWED EVIDENCE AND
IMPLICATIONS FOR FUTURE RESEARCH
Beyond the constraints of the systematic review process,
the analyzed works themselves present several challenges
and limitations that impact the feasibility and adoption of
blockchain and Self-Sovereign Identity (SSI) in forensic
chain of custody (CoC) management. The main limitations
identified in the reviewed studies are summarized as follows:
• Lack of Empirical Validation: Many proposals remain
at a conceptual stage, lacking real-world implementations or comparative analyses with existing forensic
frameworks. This limits the ability to assess their
practical feasibility and effectiveness.
• Methodological Inconsistencies: Several studies do not
provide clear justifications for their choice of blockchain
models, consensus mechanisms, or cryptographic techniques, introducing potential biases in the reported
findings.
• Absence of Standardized CoC Metadata Structures: The lack of standardization affects interoperability across forensic systems. Most reviewed works
propose isolated solutions without considering crossjurisdictional applications, raising concerns about regulatory compliance and scalability.
• Limited Adoption of Self-Sovereign Identity (SSI):
While some studies explore SSI for authentication and
access control, its application in forensic environments
remains underdeveloped, with only one concrete implementation identified.
• Scalability and Transaction Costs: Public blockchains
such as Ethereum introduce high transaction fees and
processing times, restricting their use in large-scale
forensic operations [70], [86], [94], [96], [100].
Alternative solutions, such as permissioned blockchains
or layer-2 scaling mechanisms, require further
investigation.
• Challenges in Off-Chain Storage Strategies: Several studies propose hybrid architectures that store
metadata on-chain while keeping raw evidence offchain [50], [68], [89], [90], [95]. However, ensuring the
integrity, confidentiality, and accessibility of off-chain
data remains an open research challenge.
Addressing these challenges will be crucial for advancing
the field and enabling robust, scalable, and legally compliant blockchain-based forensic frameworks. Future research
should focus on standardizing forensic metadata structures,
optimizing blockchain scalability, improving interoperability
across forensic systems, and enhancing off-chain storage
security.
VII. CONCLUSION
A systematic literature review was conducted, following the
method described in Section IV, with the aim of obtaining
a broad overview of the state of the art. This type of study,
based on a well-defined research strategy, allows for the work
to be reproduced or replicated and enables the evaluation of
its integrity and methodological rigor.
The review initially identified 9,178 articles across multiple databases, which were refined through systematic
filtering, resulting in a final selection of 39 studies. Data
extracted from these articles allowed us to answer the
predefined research questions, highlight relevant findings,
and uncover unresolved challenges and research gaps.
A key contribution of this study is the identification
of blockchain-based models, architectures, and frameworks
for digital evidence CoC management. Additionally, some
studies suggest that Self-Sovereign Identity (SSI) could
enhance authentication and access control in forensic environments. Decentralized Identifiers (DIDs) provide unique,
verifiable identities for forensic actors and digital evidence,
while Verifiable Credentials (VCs) enable the secure and
privacy-preserving exchange of forensic metadata. However,
the reviewed literature contains limited discussions on the
adoption and practical implementation of SSI in forensic
workflows.
Although SSI has been proposed as a mechanism for
decentralized authentication and access control, its application in forensic chain of custody management remains
largely unexplored. The limited number of studies addressing SSI in this domain highlights the need for further
research to assess its feasibility, security implications,
and practical integration with blockchain-based forensic
workflows.
Despite these advancements, challenges remain, particularly regarding scalability, interoperability, metadata
standardization, and real-world implementation. Moreover,
mechanisms for off-chain evidence storage and access
management require further investigation.
This study consolidates current knowledge on blockchainbased forensic chain of custody management, while also
identifying potential research directions for integrating SSI
into forensic projects.
Future research should explore privacy-enhancing techniques, such as zero-knowledge proofs (ZKPs), to safeguard sensitive forensic information while maintaining transparency and auditability. Additionally, further
studies should focus on the preservation and management of digital evidence from IoT devices, leveraging
blockchain and SSI as a foundational technology for
authentication, integrity verification, and secure access
control.
The convergence of blockchain, SSI, and advanced
cryptographic techniques presents a potential pathway for
improving digital forensics, forensic chain of custody, and
regulatory compliance in an increasingly decentralized and
interconnected environment.
