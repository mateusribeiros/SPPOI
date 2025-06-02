Title: PP-PQB: Privacy-Preserving in Post-Quantum Blockchain-Based Systems: A Systematization of Knowledge

ABSTRACT Blockchain technology has produced effective solutions and provides security by using
cryptographic tools for various applications, attracting attention from the academic community. Therefore,
researchers have taken advantage of the features of blockchain technology to increase the security of the
ecosystem. Recently, as the existence of quantum computers has been felt, researchers have started to benefit
from post-quantum cryptography to increase privacy and security. There has been an increase in data and
asset protection in post-quantum blockchain-based solutions. To the best of our knowledge, there is no
comprehensive review or taxonomy that provides a complete picture of post-quantum secure structures with
privacy-preserving techniques that have the potential to be used in blockchain. This paper aims to close this
gap by systematically examining these approaches and revealing the deficiencies in the existing literature
and the development potential in these areas. The taxonomy examines the role of blockchain technology in
post-quantum cryptography and emphasizes the potential of technologies such as zero-knowledge proof
to ensure privacy in post-quantum blockchain-based systems. We also review the existing literature on
addressing the performance overhead, interoperability, scalability, and security challenges in implementing
post-quantum cryptography in zero-knowledge proof-enabled blockchain architectures that protect against
quantum computing threats. The studies are collected from journal papers in widely used academic databases
between 2018 and 2024. The studies are subjected to certain elimination criteria, and 13 studies are reviewed
in detail. Our approach will facilitate discussions on future research directions by proposing the accessibility
of post-quantum cryptography against quantum threats to blockchain systems and solutions to the challenges
that arise in the integration phase.
INDEX TERMS Blockchain, post-quantum cryptography, post-quantum blockchain, zero-knowledge proof.
I. INTRODUCTION
The development of blockchain technology, using cryptographic protocols, plays an important role in ensuring
security and protecting confidentiality. Cryptography is a
way of converting text into scrambled information, that
is, into encrypted text, and whoever has the relevant key
(private key) can decrypt the encrypted message. Among
these, digital signatures are among the basic cryptographic
primitives used to strengthen blockchain, providing features
such as user privacy, account management, and consensus
efficiency. Blockchain is a distributed shared database that,
unlike a traditional database, stores hashes of data in
cryptographically interconnected blocks. Its decentralization
means that no person or group has the authority to change it,
and the data is immutable. This structure ensures reliability
in an untrusted environment with the immutability and
non-repudiation of transactions. It has been proposed as
an important technology in many areas, such as healthcare [1], supply chain [2], smart systems [3], e-voting [4],
and digital identity verification [5]. Moreover, it provides
various security mechanisms, including data protection and
authentication for IoT applications [6]. In the past decade,
various privacy-preserving blockchain models have been
introduced to provide security. However, newly developed
privacy analysis methods have reached a level that threatens
the security of the systems [7], [8]. Moreover, recent studies
have proposed innovative privacy-preserving mechanisms
using blockchain technology, such as blockchain integration
for privacy-preserving electric vehicle overhead prediction
with federated learning [9] and scalability for IoT systems
and solutions focusing on privacy-preserving mechanisms in
blockchain-based federated learning systems [10]. Although
this technology offers increasing advantages to address
security concerns, it is under serious threat with the
emergence of quantum computing technologies because
existing blockchain platforms are based on traditional
cryptosystems such as Rivest-Shamir-Adleman (RSA) [11]
and the Elliptic Curve Digital Signature Algorithm (ECDSA)
[12]. Advances in quantum computing make the resilience of
traditional cryptographic protocols against quantum attacks
questionable and pose a significant threat to the security of
blockchain systems. In addition, while the process regarding
the existence of Quantum computers remains uncertain,
recent studies conducted by Google [13] and IBM [14]
strengthen the opinion that post-quantum secure blockchain
systems are needed.
Post-quantum cryptography (PQC) is a cryptography based
on the assumption of a quantum computer [15]. The field of
research is fairly new, and there has been a recent increase
in work focusing on leveraging PQC to enhance privacy and
the need for quantum resilience in decentralized applications.
The main challenge here is to ensure cryptographic security
and usability. Cryptographic methods such as lattice-based,
code-based, multivariate, and isogeny-based play a role
in preparing the blockchain for the quantum age, and
post-quantum blockchain architectures are designed. Publickey cryptographic protocols such as RSA and Diffie-Hellman
are based on the assumption that factoring a large integer,
finding a sequence, and finding a discrete logarithm is
difficult. Quantum computers are known to be able to
solve any of these problems in polynomial time (O(n
2
)
complexity) [16]. Quantum computers have the potential
to break currently used schemes (such as elliptic curve
cryptography (ECC)) with algorithms such as Shor’s [17]
algorithm. The underlying features of PQC that make it
challenging include the following;
1) It is quantum resistant to quantum attacks with a
different approach than traditional algorithms.
2) Instead of relying on the challenge of solving the discrete logarithm problem, it has complex mathematical structures such as multivariate
polynomials, mixed basis structures, lattices, etc.,
and it relies on the challenging mathematical
problem.
The National Institute of Standards and Technology (NIST)
launched a standardization competition in 2016 to determine
cryptographic algorithms that will remain secure against
quantum computers. This competition, conducted in three
stages, reached its final phase between 2022 and 2024,
leading to the announcement of the following standards:
CRYSTALS-Kyber [18], Dilithium [19], FALCON [20], and
SPHINCS+ [21]. These algorithms are crucial for mitigating
potential threats posed by quantum computing. NIST’s
PQC Project [22] has concluded, with CRYSTALS-Kyber
selected as the post-quantum Key Encapsulation Mechanism
(KEM) and Dilithium, Falcon, and SPHINCS+ chosen as
post-quantum digital signature algorithms. Dilithium and
Falcon have also been tested by Hardware Security Module
(HSM) vendors to verify digital signature creation, key
import during authentication, and signature verification.
While standardization efforts continue, it has been concluded
that, for certain use cases, digesting the message before
passing it to the signing algorithm, or using pure PQ
signatures without digests, may be preferable.
The fact that blockchain technology has many application
areas indicates that there is a need for PQ secure structures due to the existence of known quantum computers.
Furthermore, the developments in integrating Big Data and
Artificial Intelligence (AI) with blockchain systems [23],
such as increasing data processing, scalability, and security,
play an important role in meeting the increasing demands of
PP-PQB solutions. To the best of our knowledge, there is no
Systematization of Information (SoK) that provides a complete picture of PQ secure structures with privacy-preserving
techniques that have the potential to be used in blockchain.
Therefore, this paper, the first we know of, fills this gap
by reviewing approaches used for privacy-preserving PQB
(PP-PQB) applications required by blockchain applications.
It also examines the existing literature on the current
challenges and proposes solutions.
This section addresses the need for integrating blockchain
technology with PQC. It discusses the vulnerability of
traditional cryptographic systems to quantum threats and
the potential for enhancing the security of PQB systems.
In addition, the aim of this study is to fill the gaps in the
literature.
A. RESEARCH MOTIVATION
In recent years, since quantum computing threatens the security of applications in traditional cryptography, blockchain
technology has emerged as a promising solution to ensure
the security of transactions. However, even if traditional
blockchain systems are robust, the existence of quantum computers, especially due to their computational power exceeding
classical computational methods, threatens their security
against quantum attacks. Since the basis of blockchain
technology is the existing classical cryptographic protocols,
quantum computers have a high potential to weaken the
security of blockchain networks. Therefore, the need for
post-quantum blockchain applications arises from the following reasons.
1) In blockchain systems, classical cryptographic protocols such as asymmetric encryption and hash functions
(RSA, SHA-256) pose a cryptographic security threat
because they can be easily broken by Shor’s and
Grover’s algorithms [24].
2) The ability to solve authentication schemes to prevent
unauthorized access and fraudulent transactions with
quantum computers [25].
3) Traditional blockchain systems, which block user identities and meet the need for anonymity and privacy, can
be solved in the presence of quantum computers [26].
4) Quantum computers negatively affect the permanent
data security and reliability of blockchain systems used
for sustainable systems [27].
PQB applications and the provision of structures such as
security, anonymity, privacy, and integrity are necessary to
ensure the sustainability of this technology. With the help
of PQC, new methods for digital signature schemes and
KEMs have appeared, relying on cryptographic structures
based on hard-to-solve mathematical problems, such as
lattice-based, hash-based, and code-based approaches. Due to
these main changes, post-quantum security can be provided
by applying them to blockchain applications. Therefore,
there is a need to develop blockchain architectures that
aim to provide quantum-resistant security and privacy
against quantum threats by taking advantage of advances
privacy-preserving techniques in PQC algorithms such as
lattice-based cryptography, code-based cryptography, and
hash-based cryptography. When looking at the PQB applications in the literature, although there is no full PQB
application, some studies have taken important steps in
this direction [28]. In [29], the authors designed a PQB
system for smart city applications. The study developed
a post-quantum Proof-of-Work (PoW) consensus algorithm
using multivariate quadratic equations and an identity-based
signature scheme for a lightweight and fast transaction
structure. However, it has been observed that the blockchain
transaction security and PoW consensus protocol components of the system have developed post-quantum, and the
basic structure of the system, such as data structures and
transaction verification process, have not been fully postquantum. In [30], the authors proposed a post-quantum
ring signature-based blockchain architecture for the Internet
of Social Things. The proposed management emphasized
its resistance to classical and quantum computers. In the
study, anonymity and privacy were provided by using ring
signatures, and security was provided by using ring signatures
and multivariate quadratic equations. The study designed
certain system components to provide post-quantum security
and observed that a complete PQB structure was not provided.
In [31], the authors proposed a lattice-based signature scheme
to secure the blockchain network. In the study, private and
public keys were generated using Bonsai Trees technology.
The current study also has designed certain components to
provide post-quantum security.
Therefore, while PQB-focused studies in existing surveys
focus on security, privacy-preserving methods (such as
ZKP) in PQB systems have not been thoroughly examined.
Furthermore, the performance of these methods and the
privacy-performance trade-off have not been discussed in
depth.
B. RESEARCH CONTRIBUTION
Various surveys have been conducted on post-quantum secure
blockchain structures [26], [32], [33], but there is a lack
of systematic analysis on privacy-preserving PQC-integrated
blockchain. In this study, we present a survey about PPPQB systems. This study, compared to other studies in the
literature, not only remains in the theoretical framework but
also fills the gap in the literature by analyzing how PP-PQB
solutions can be used in real-world applications. We propose
the optimization techniques to reduce the computational
load without compromising security for the balance between
performance and security, which is often overlooked in the
existing literature. We also provide a research contribution
analyzing the effects of ZKP on scalability and performance
in post-quantum systems, which is felt lacking in this field.
1) This is the first study focusing on the performance
overhead, interoperability, scalability, and security
(OISS) challenges of PP-PQB solutions.
2) We examine PP-PQB systems to fill the gap in the literature in this area and analyze the role and performance
of privacy-preserving techniques in providing privacy.
3) We analyze the usage cases of PP-PQB applications
and evaluate their efficiency.
4) We discuss the security constraints of the proposals and
the important application areas of the architectures.
5) We present a review of applications that include ZKP,
which ensures the confidentiality and integrity of transactions without compromising privacy in post-quantum
blockchain (PQB) applications.
6) We provide suggestions on the practical applicability of
post-quantum privacy-preserving protocols, especially
theoretical studies.
7) We propose new approaches to improve the security
and efficiency of PQC-integrated Blockchain architectures.
8) We give new research directions on the development
and improvement of privacy-preserving methods in
PQB, which are lacking in the literature.
9) We present a roadmap on quantum-resistant Layer2
solutions and integration of Multi-chain models to
solve scalability and efficiency problems.
C. ORGANIZATION
This review addresses the critical gap in blockchain systems by investigating the integration of quantum-resistant
cryptographic primitives and privacy-preserving techniques
(PP-PQB) to enhance security against quantum attacks.
We systematically collected and analyzed studies from major
academic databases, including Scopus, WoS, IEEE Xplore,
ScienceDirect, Springer Link, and ACM Digital Library, and
applied selection and elimination criteria to ensure relevance
to our research questions. The review provides an SoK as
follows:
In Section II, we discuss the systematic process for
the studies to be reviewed and summarize those selected.
In section III, we explain the basics of the PQC and
blockchain concept and the perspectives of the elements
that provide security. Then, we present the use of
privacy-preserving techniques (such as ZKP) in PQC
approaches and the modules that need to be changed in
the blockchain for PQB. In Section IV, we briefly review
proposed PP-PQB solutions from the systematic process
and solutions to several identified challenges to improve
security against quantum attacks. In Section V, we discuss
the vulnerability of selected reviews to quantum attacks of
cryptographic primitives used in blockchain systems, present
threats to validity, and future research directions. Finally,
we present the conclusion.
D. RELATED LITERATURE
This section examines post-quantum blockchain-based
review studies published between 2018-2024. We obtain
the review studies through specific filtering, which we
present in detail in the following sections. Although various
surveys and studies have been conducted on PQB [32],
[33], [34], it has been observed that PP-PQB studies
are quite new, and the applicability and comprehensive
discussion of privacy-preserving techniques are limited.
Focusing on privacy-preserving methods in PQB systems,
the existing literature is reviewed, and the gaps in this field
for post-quantum secure blockchain systems are addressed.
Table 1 presents existing reviews of PQB studies and their
main differences. We show different emphases of studies and
do not indicate superiority or inferiority.
Fernandez-Carames and Fraga-Lamas [32] examined how
PQC can be applied to blockchain applications, focusing
mainly on encryption and traditional signature schemes. They
analyzed the PQC systems most suitable for blockchain
and the challenges of these systems. In the study, the
authors investigated various technical aspects related to the
vulnerability of blockchain technology to quantum attacks.
To briefly state these, they examined how algorithms such
as Grover’s and Shor’s used by quantum computers pose
threats to traditional public-key cryptography and hash
functions such as RSA, ECDSA, and SHA-256 used in
blockchain. They also examined lattice-based, code-based,
multivariate, and hash-based post-quantum cryptography
methods designed to resist quantum attacks. They presented
comparisons of the performance, key sizes, and security
levels of post-quantum public-key cryptography and digital
signature schemes such as McEliece, NewHope and It
also focuses on the challenges posed by the key size, key
TABLE 1. Comparison to Review Studies.
generation time, and computational resource demands of
integrating PQC into blockchain systems.
Gomes et al. [34] used a systematic method to analyze PQ
solutions’ effects on blockchain consensus. They examined
the effects of improvements in security, scalability, trust, and
privacy on PQB consensus. In the study, the authors examined
how existing consensus protocols threaten quantum attacks,
detailed post-quantum blockchain consensus solutions, and
investigated PQC-based solutions such as quantum random
number generation, quantum entanglement, quantum key
distribution, and multivariate polynomial equations. They
discussed the development of consensus algorithms based on
quantum physical processes using random number generation
methods that ensure that random numbers in the blockchain
are verifiable and reproducible. They examined how quantum
entanglement and quantum measurement methods, which
transfer and verify data over quantum secure channels, can
improve blockchain security and verification processes.
Buser et al. [33] reviewed existing research in the
literature on post-quantum exotic signature schemes rather
than discussing specific post-quantum ordinary signature
proposals used in blockchain systems. They also examined
schemes that can be used to increase security and privacy
for blockchain systems. They also reviewed schemes that can
increase security and privacy for blockchain systems. In the
study, the authors specifically considered advanced signature
types: multi-aggregate, threshold, adaptor, blind, and ring
signatures. They evaluated how account management and
consensus efficiency can be used to increase privacy in
blockchain systems without smart contract support. They
detailed the security, efficiency, and impact of post-quantum
signature algorithms on blockchains and indicated shortcomings and future research directions.
Yang et al. [35] conducted comprehensive general literature research on post-quantum and quantum blockchains
and provided a comparative study. They also discussed the
cryptographic foundations used in post-quantum blockchains
against quantum attacks and investigated their vulnerabilities
and challenges. In the study, the authors examined how
systems using classical cryptographic protocols should
be strengthened against quantum computer attacks and
analyzed lattice, code-based, isogeny-based post-quantum
cryptographic protocols. They discussed how hybrid quantum
blockchains can be built based on quantum technologies
such as quantum key distribution, quantum signatures, and
quantum teleportation. They examined and analyzed the
studies on how existing blockchain systems can be protected
against quantum threats by focusing on PQB.
Thanalakshmi et al. [27] examined the inclusion of
post-quantum signature schemes in the blockchain system
into the ‘‘Interplanetary File System (IPFS)’’ integrated with
the blockchain system. They also discussed the comparison of
post-quantum signature schemes proposed by the ‘‘National
Institute of Standards and Technology (NIST)’’ with the
‘‘Elliptic Curve Digital Signature Algorithm (ECDSA)’’.
In the study, the authors examined the resistance of the
Dilithium, FALCON, and SPHINCS+ signature schemes
proposed by NIST against quantum attacks and their performance, such as key generation time, signing time, verification
time, and key/signature sizes. They also investigated how
IPFS can be used to reduce the overhead of these signature
schemes with large key and signature sizes in the blockchain.
Gharavi et al. [36] examined PQB types in blockchainbased IoT applications and discussed the current standard
foundations of PQB studies and their applicability in IoT.
In the study, the authors detailed how classical cryptographic
protocols such as RSA and ECDSA can be broken by quantum computers and how the resistance of existing systems
against quantum attacks can be changed. They analyzed
the integration and performance of various post-quantum
cryptographic methods, such as hash-based, lattice-based,
multivariate-based, and isogeny-based cryptographic systems
into IoT devices. They also investigated the integration of
PQB systems into IoT systems and examined their effects on
security and performance. Specifically, the authors emphasized that the lattice-based post-quantum cryptographic
method is more efficient in IoT devices.
This section presents a literature review of existing
PP-PQB techniques. The general trends, strengths, and
weaknesses of the studies are identified, and research gaps
in these areas are highlighted.
II. RESEARCH METHODOLOGY
This section includes selecting and filtering studies on a PPPQB between 2018 and 2024. Research questions (RQ) are
determined according to the research objectives. In detail,
it includes the RQ and the topics covered in the research field,
as well as their selection and elimination by filtering from
various academic databases. The RQ of the study is presented
in Table 2.
To identify research studies related to PP-PQB, Web of
Science (WoS), Scopus, IEEE Xplore, Springer Link, ScienceDirect, and ACM Digital Library databases are scanned.
The search array was run on each scientific repository
to execute the query expressions. Advanced search tools
of Scopus, WoS, IEEE Xplore, and ACM Digital Library
databases are used. The main search engine uses relevant
query expressions in Springer Link and ScienceDirect
databases. Query expressions used in databases are shown in
Table 3. It needs to be filtered to determine which study to
review. In filtering, certain selection and exclusion criteria
(EC) are defined. Firstly, we exclude PQB and all cheat
sheets after searching PP-PQB. To exclude the remainder,
we use other EC (Table 4). The first stage is about reading
the title and abstract of the papers. Then, the introduction and
conclusion parts of the papers are read, and finally, it is read in
its entirety and analyzed according to the research questions.
In the first step, 982 journal papers are obtained in
the field of PQB, including 92 articles in Scopus, 34 in
WoS, 43 in IEEE Xplore, 29 in ACM Digital Library,
301 in Springer Link, and 483 in ScienceDirect. 477 journal
papers related to PP-PQB are obtained, including 18 journal papers in WOS, 18 in Scopus, 14 in IEEE Xplore,
46 in ACM Digital Library, 134 in Springer Link, and
247 in ScienceDirect. The studies are evaluated according
to their suitability for post-quantum cryptographic methods,
(blockchain-based) privacy-preserving mechanisms, quantum resistance, blockchain performance, and scalability.
In the first screening, 505 journal papers are excluded
from papers lacking technical depth, studies focusing only
on classical cryptography, and papers published outside of
English.
The remaining 459 journal papers are excluded through
title and abstract reading analysis, and duplicate journal
papers are excluded in the subsequent elimination. These
studies do not directly answer our RQ or lack experimental
validation.
In the next stage, the introduction and conclusion are read
in the selected journal papers, and non-relevant journal papers
are excluded. As a result of all these processes, 13 journal
papers are reviewed in detail within the scope of Q1 and
Q2 journals, which present innovations focusing on privacy
and security in PQB systems. The contribution level of the
studies is analyzed based on factors such as case studies
and experimental results. In addition, some of the selected
studies offer solutions to ZKP, lattice-based cryptography,
and scalability problems. Figure 1 systematically shows the
filtering stages of the study.
III. POST-QUANTUM BLOCKCHAIN
A. POST-QUANTUM CRYPTOGRAPHY
PQC has been developed with quantum computers to protect
against attackers. PQC is also a classical cryptography
based on NP-hard mathematical problems [37]. Symmetric
Algorithms and hash functions provide relative security for
post-quantum. However, researchers in this field have to
look for new number theory problems that will base the
security of asymmetric algorithms, that is, new mathematical
TABLE 4. Exclusion criteria.
problems that quantum computers cannot easily solve. Shor’s
algorithm [17] is proposed to solve the discrete logarithm
problem on a quantum computer by executing parallel
operations on the processor. On the other hand, Grover’s
algorithm [38] can speed up search operations according to
the complexity of attacks √
n (n is the size of the brute force
search domain). This situation threatens the security of the
symmetric and hash functions.
The National Institute of Standards and Technology
(NIST) announced the PQC standard algorithms in 2022,
continuing a process it started in 2016 to prevent quantum
attacks. In the literature, different PQC approaches such
as lattice-based, code-based, isogeny-based, hash-based and
multivariate-based are discussed for data privacy and security
for post-quantum systems. Lattice-based systems, which
are especially prominent in signing and key encapsulation, and hash-based systems used in signing are used
for privacy-preserving in post-quantum secure blockchain
systems.
Lattice-based algorithms were firstly proposed by
Ajtai [39] for the development of reliable cryptosystems
based on the NP-hard [40] mathematical lattice problem.
While other cryptosystems include security based on averagecase problems, lattice-based algorithms have the feature of
providing security based on worst-case problems. Latticebased algorithms are based on the nearest (CVP) or shortest
vector (SVP) problem, which is a special arrangement
of points with a periodic structure in the n-dimensional
vector space. The cryptographic generators used in these
cryptographic systems provide security proof based on
worst-case hardness and are highly efficient [41]. Therefore,
lattice-based cryptography is considered highly promising
for post-quantum encryption. A special category of hard
problems, known as Learning With Errors (LWE), also forms
the basis of various lattice-based cryptosystems, such as
R-LWE and LP-LWE. In response to the NIST call, schemes
like Kyber [42], FALCON [20], and Dilithium [19] were
accepted as standards for key encapsulation and digital
signatures. In PQB applications, the ZKP structure can be
used on Short Integer Solution (SIS) and LWE problems
when using lattice-based structures, and Merkle Signature
Schemes (MSS) and their derivatives when using hashbased structures. Multivariate-based structures can be used to
protect the privacy of the signer, and isogeny-based structures
can be used in structures that require verification in secret
information sharing.
The hash-based digital signature scheme is a type of
post-quantum encryption scheme used as an alternative
to today’s digital signature schemes. Its security is based
on certain mathematical problems that provide collision
resistance and preimage resistance, which is different from
other cryptosystems. Finding collisions and preimages is a
challenging problem due to the underlying hash function.
Therefore, it is a signature scheme that can be used in
authentication. It takes advantage of the hash function,
which is widely used in cryptosystems, and protects against
quantum attacks due to its unidirectionality, preimage,
and collision resistance properties. The SPHINCS+ and
Gravity-SPHINCS schemes selected by NIST are based on
a stateless approach. Among the stateful class, there are also
variants such as Witernitz [43], Lamport’s given One-Time
Signature (OTS) scheme, WOTS+ [44], and WOTSPRF [45].
Although they attract attention with their structures resistant
to attacks by quantum computers, they have some limitations
regarding scalability, efficiency, and application flexibility.
A larger signature size than other PQC algorithms increases
storage and communication costs in IoT networks with
limited resources. Since these signature schemes require
stateful, a key must be used in each signature. Therefore,
if the key is reused, the security of the system is at risk.
In addition, due to its structure, intensive operations in
creating and verifying each signature complicate the key
management process and may have difficulty supporting high
transaction volumes in large-scale blockchain applications.
These lattice-based and hash-based algorithms, which are
discussed in the context of PQC, offer different security and
performance characteristics [46]. When choosing between
these approaches, key size, signature size, transaction time,
and energy efficiency should be considered. However, even
if the use of ZKP in symmetric and code-based structures
is theoretically possible, it is not possible to design and
implement due to limitations such as key management
challenges, ZKP complexity, key size, and performance cost.
Therefore, the use of ZKP in symmetric and code-based
structures is limited in the current literature, and there are
potential research opportunities.
This section examines hash-based and lattice-based cryptographic algorithms, comparing their performance metrics
and application areas. It details the strong security features
of hash-based algorithms and their impact on large data sets,
as well as the scalability and processing power advantages of
lattice-based algorithms.
B. POST-QUANTUM BLOCKCHAIN FEATURES
Blockchain technology is a distributed ledger technology that
provides immutability, transparency, and traceability of data
and distributed peer-to-peer trust [47]. Consensus algorithms,
distributed ledger technology, and decentralized structure
are the basic components of the system. The security of
blockchain technology is based on asymmetric cryptography
and hash functions. Data security and immutability in the
network are based on consensus protocols and classical
encryption techniques (such as RSA [11] and ECDSA [48])
[49]. Figure 2 shows the generation of the blockchain
and an example of a transaction in the generated chain.
Since transactions are open and transparent in blockchain,
ZKP technology ensures data confidentiality and proves
transaction accuracy. This method protects privacy and
secures the transaction verification process. It is an important
technique that increases the security and efficiency of the
system, especially in cases where private data needs to be
protected and verified. Digital signatures used in blockchain
systems are indispensable for identity verification, data
integrity, and transaction non-repudiation. They verify the
source of a transaction while ensuring that the data has
not been altered. Various signature schemes, such as MultiSignature [50], Blind Signature [51], Ring Signature [52], and
Threshold Signature, are applied to blockchain platforms to
meet the needs for security, anonymity, and scalability. These
schemes increase transaction security in blockchain systems
while providing higher levels of anonymity and privacy [53].
Algorithms such as RSA and ECC, which are widely used for
digital signatures and key exchange, and hash functions such
as SHA-256 and SHA-3 (Keccak), which form the basis of
block hash operations and Proof of Work (PoW) mechanisms,
are essential cryptographic tools in blockchain systems.
Additionally, symmetric encryption algorithms like AES are
used for data encryption in some blockchain applications,
and digital signatures such as ECDSA, which provide
authentication and non-repudiation, play a crucial role in
enhancing blockchain security. In these tools, SHA-256 is the
basic hash function used in many blockchains such as Bitcoin
and performs many tasks such as transaction verification,
creation of Merkle tree structures, and preservation of
data integrity by hashing the data. SHA-256 provides data
integrity and transaction verification processes by producing
a fixed-length digest (hash) regardless of the input size.
In addition, SHA-256 plays a critical role in transaction
verification and chain security in Bitcoin’s PoW mechanism,
and this function ensures that a unique hash value represents
each block in the blockchain chain.
The SHA-3 algorithm, selected as a standard by NIST in
2012, was designed to be secure the potential weaknesses
of SHA-256. SHA-3 provides faster transactions and higher
security by using sponge functions. It can be used in
many blockchain applications as an alternative to SHA256. ECDSA is a digital signature algorithm used to
meet the authentication and non-repudiation requirements of
blockchain transactions. It is widely used as a security layer,
especially in popular blockchain platforms such as Bitcoin
and Ethereum. Symmetric encryption algorithms such as
AES ensure data confidentiality in blockchain applications.
In particular, AES is preferred in IoT-based blockchain
applications due to its low processing power requirement
and high-speed advantage. Asymmetric encryption protocols such as Diffie-Hellman and RSA provide secure key
exchange between users in the blockchain network. These
protocols are critical for secure communication, especially
for smart contracts and decentralized applications. However,
quantum computers can quickly solve problems based on
these algorithms thanks to Shor’s and Grover’s algorithms,
and this threatens the security of cryptographic algorithms
used in the blockchain infrastructure [54]. Therefore, the
privacy-preserving techniques used in PQB both protect data
integrity and provide a structure resistant to future quantum
threats.
Real-world applications of PP-PQB systems highlight their
critical role in addressing privacy and security challenges.
In finance, ZKP-based protocols enable anonymous payment
systems and ensure regulatory compliance without compromising user privacy. In particular, zk-SNARKs provide
privacy and security for PP-PQB systems by allowing users to
verify the validity of transactions without revealing account
details. They are also used in financial applications such
as anonymous payment systems. It can also be used in
PP-PQB systems to provide regulatory authorities with the
necessary information to prove the authenticity of only the
required credentials in anti-money laundering processes [55].
Similarly, in healthcare, using ZKP protocols in PP-PQB
systems enables the secure sharing of medical data while
preserving privacy, allowing patients to verify their eligibility
for treatments or participate in research without disclosing
their full medical history [56]. This integration also addresses
scalability and computational cost challenges while providing opportunities for innovation. These specific examples
demonstrate the practical impact of integrating PP-PQB
systems into existing infrastructures.
Definition 1: PQB is a distributed ledger structure
designed to be resistant to attacks while preserving data
integrity and confidentiality. It provides enhanced security
against quantum attacks over pre-quantum methods such as
RSA and ECDSA by integrating post-quantum cryptographic
methods such as lattice-based and hash-based cryptography.
Definition 2: ZKP is a cryptographic technique built on
three key properties: completeness, soundness, and zeroknowledge, which allow a party to prove the validity of a
statement without revealing any additional information [53],
[57]. In PQB systems, ZKP guarantees transaction privacy
and data integrity while maintaining scalability and performance.
The main modules used in the blockchain, such as digital
signature, key exchange protocols, hash functions, consensus
mechanism, and smart contract protocols, need to be updated
to resist quantum attacks [36], [58]. Instead of classical
signature algorithms such as RSA and ECDSA used in
digital signatures, PQ secure signature schemes such as
NIST-approved Dilithium, FALCON, or SPHINCS+ should
be used [59]. Instead of classical key exchange protocols
such as Diffie-Hellman, PQ secure key exchange protocols
such as Kyber or NTRU should be used [32]. In case of
the possibility of breaking hash functions with Grover’s
algorithm, it is necessary to work with larger bit lengths in
hash functions such as SHA-256 or SHA-3. However, the
integration of post-quantum blockchain needs to integrate
with the following key challenges:
1) Signature and hash length [60]
2) Key size [60]
3) Computational complexity [61]
4) Execution and Energy consumption [62]
In PQB integration, features such as small signature and
hash length, small key size, low computational complexity,
fast execution, and low energy consumption are important
challenges in PQC [63]. These challenges manifest in many
areas, from standardization processes to efficient differentplatform implementation. Since lattice-based algorithms
require high processing power for intensive operations such
as matrix multiplications and modular arithmetic (complex
operations such as large key sizes, multiplication, and
modular reduction of large polynomials used in encryption/decryption), it causes the block verification process
to take a long time in large-scale blockchain networks
and reduce the transaction throughput of the network, thus
causing high computational costs. In addition, challenges
such as the large key size requiring more bandwidth
during transaction submission and increasing storage load
make integrating these lattice-based structures into existing
blockchain-based systems difficult. This causes compatibility
problems and, in this case, increased transaction time or
resource consumption and, thus, integration complexity.
In general, it is also critical to establish international
standards for the effective use of lattice-based algorithms.
Choosing among PQC algorithms such as Kyber and
Dilithium and adapting these algorithms to various use cases
is a complex process. Blockchain networks can be deployed
on different device types and hardware platforms, such as IoT
devices. To support this diversity, lattice-based algorithms
should be optimized. Small key pairs must be used to reduce
complexity and reduce storage space for limited Internet of
Things (IoT) end devices interacting in blockchain-integrated
systems. In blockchain architecture, user signatures and data
transactions in the data or block hash are stored. Therefore,
the blockchain size increases as the signature and hash length
increase. In such cases, a short signature and hash length
should be used. For transactions to be carried out quickly in
the blockchain, post-quantum cryptography must be as fast as
possible. Therefore, choosing the parameters used correctly
to ensure security and performance balance is a great
challenge. Wrong parameter selection can lead to security
vulnerabilities and negatively affect the transaction costs of
the algorithm. The selected parameters are important for
fast execution, to prevent resource-constrained devices from
being excluded from blockchain-integrated transactions, and
to provide low computational complexity and overhead.
In addition, the number of transactions performed, the
hardware used, and the security plans to be implemented
affect power consumption. Fast execution provides low
communication costs and overhead and impacts power
consumption. This contributes to the efficient operation of
the system. In addition, to enhance the privacy and security
of blockchain ecosystems, post-quantum cryptographic algorithms such as Kyber and Dilithium, which provide resistance
against quantum attacks by exploiting the difficulty of
problems such as LWE and MLWE, will be the alternatives
of traditional public-key cryptosystems such as ECDSA used
in blockchain ecosystems. The signature schemes ensure
data integrity and authentication processes in blockchain
networks. Algorithms such as Dilithium and Falcon provide
reliability in signing and verification processes and offer
faster and more efficient architecture with low processing
overhead. These features enable integrating IoT devices
with blockchain systems, especially those with energy
constraints [64]. However, implementing these algorithms at
the protocol level creates technical complexity, especially
in blockchain-based systems that require data privacy and
transaction security. Protocols must be designed securely and
scalable to achieve an optimal structure in transaction costs.
The hash-based and lattice-based cryptographic schemes
ensure data integrity and secrecy by resisting quantum
attacks, such as Shor’s algorithm for breaking RSA and ECC,
and Grover’s algorithm, which only weakens symmetric
systems by effectively halving the key length. Additionally,
using data blinding operations with lattice-based algorithms
enhances user privacy and helps protect sensitive data.
Such mechanisms support both decentralized authentication
processes and secure data sharing [32]. Moreover, postquantum cryptography enables secure consensus protocols
by providing robust digital signatures and key exchange
mechanisms in the blockchain ecosystem. Therefore, the
overall privacy and integrity of the system against future
threats posed by quantum computing is enhanced.
This section examines post-quantum security methods and
privacy mechanisms used in blockchain technology. It also
exemplifies the role of ZKP in system integration and the
applications of these mechanisms in various sectors.
C. THE USE OF ZKP IN POST-QUANTUM SIGNATURES
ZKP is the protocol that allows one party (the prover) to
convince the other party (the verifier) of the validity of
the relevant statement without informing the other party
(the verifier). It has the basic properties of completeness,
robustness, and zero-knowledge [65]. These properties can
be categorized into two main types based on interaction:
1) Interactive: Participating in an iterative protocol for
the engagement of the statement by the prover and
verifier, involving query-response requests through
multiple rounds of interaction.
2) Non-interactive: the case where the prover does not
require direct communication with the verifier to verify
the statement.
The remaining properties are defined as follows:
1) Completeness: in the truth of the statement, the prover
convinces the verifier.
2) Robustness: if the statement is untrue, the fraudulent
prover cannot convince the verifier.
3) Zero-knowledge: when the statement is true, the
verifier cannot learn any information other than the
truth of the statement.
The interactive-ZKP is recalled in Figure 3 [65]:
1) Step 1: The prover generates a random R to pass R =
±r
2
(modN) to the verifier.
2) Step 2: The verifier generates the binary string
(b0, b1, . . . , bm−1) to generate the challenge and sends
it to the prover along with the ki key corresponding to
the string.
3) Step 3: The prover calculates π
2
y = p (1 ≤ y ≤ n)
using the R ·
Qbi
ki
(modN) (1 ≤ i ≤ m − 1) formula and
sends it to the verifier.
4) Step 4: The verifier checks the validity using the
formula R
2 = p ·
Qbi
wi
(modN)(1 ≤ i ≤ m − 1), and if
the equation holds, the iteration is considered.
5) Steps 1-4 are repeated for n iterations for robust
verification.
There are non-interactive-ZKP protocols called ZeroKnowledge Short, Non-Interactive Information Argument
(zk-SNARK), and Zero-Knowledge Scalable Transparent
Information Arguments (zk-STARK), which have recently
been researched for use in PQB applications and are
widely used in Blockchain applications. These protocols
offer potential capabilities for robust privacy and security.
zk-SNARK utilizes ECC to generate keys and process
transactions, providing proof of the validity of transactions
while protecting user privacy. The working principle of
zk-SNARK is shown in Figure 4.
1) Step 1: KeyGen (pk , vk ), Proof (p), and verification (v)
keys are created in the given circuitC.
2) Step 2: Proof (pk , x, a) → π, to generate evidence
of the validity ofagiven statement xgiven pk given a
particular witness.
3) Step 3: Verify(vk, x, π) → b, verifying the validity of
the proof π on the given statement x. A boolean value
indicating the validity of the proof b is 1 if successful,
0 otherwise.
zk-STARK is a variant of ZKP that addresses some of
the limitations of zk-SNARK and provides scalable and
computational efficiency and secure verification. Its main
features, besides zk-SNARK, are that it is transparent and
does not require preprocessing. With zk-STARK, complex
calculations can be produced at a minimum cost. Since it
does not require a secure installation, it eliminates creating
secret parameters that can be captured during an attack.
This feature makes its use in open blockchain systems
more advantageous than zk-SNARK. It is also thought
to provide PQ-security [66]. zk-STARK is scalable and
uses advanced techniques such as polynomial evaluation
and error correction codes to reduce the proof size and
increase confirmability. It includes key components such
as the Fast Reed-Solomon Interactive Oracle Proofs of
Proximity (FRI) protocol and low-degree testing (used to
verify the correctness of the calculation efficiently), which is
an effective protocol for low-degree testing in validating the
evidentiary claim.
ZKP is used in real-world systems such as IoT, healthcare,
and supply chains to protect data authenticity, prove the
authenticity of medical data while preserving its confidentiality, or reduce the risk of data leakage in identity verification
[57]. In PQB systems, ZKP provides an important security
layer that strengthens user privacy at its core by allowing
the user to prove the authenticity of a transaction without
revealing their private key when signing a transaction.
In other words, it protects data integrity and transaction
security. It also helps to provide complete anonymity on
the blockchain by ensuring that only necessary information
is shared, minimizing users’ sensitive data disclosure, and
hiding data such as sender-receiver addresses, transaction
amounts, and transaction links [67]. Therefore, latticebased signature algorithms such as post-quantum secure
Dilithium can be combined with ZKP to protect the privacy
of transaction identities and optimize signature verification
processes. It can be strengthened in terms of both security
and privacy. Solutions such as ZKP-based zk-rollup minimize
the transaction load on the blockchain by producing a
single proof for many transactions and provide performance
in addition to privacy in PQB systems. In addition, zkSTARK protocols, which use hash-based and polynomial
commitments in their structure, can provide high performance and quantum resistance in addition to privacy in PQB
systems [68].
However, integrating these techniques into real-world systems brings practical challenges and considerations, such as
interoperability between networks and adapting to different
consensus mechanisms and cryptographic standards [53].
ZKP’s protocols affect the computational cost by imposing
overhead, especially in resource-constrained IoT systems.
In addition, integration into existing systems can require time
and resources to ensure compatibility with these infrastructures, which can cause compatibility challenges. Therefore,
integration processes should address these challenges in
providing ZKP-based PP-PQB systems.
This section discusses in detail the integration of ZKP
with post-quantum digital signatures. Its contributions to
data integrity and transaction verification processes in PQB
systems explain its privacy and security-enhancing role.
In addition, the advantages and limitations of ZKP protocols
in terms of scalability, transaction cost, and security are
evaluated.
IV. SYSTEMATIC REVIEW REPORT ON STUDIES
This section presents notes on the studies determined after
EC on the identified journal papers and the answers to
the RQs. The contributions, advantages, and limitations
of privacy-preserving techniques proposed for enhancing
blockchain reliability and resisting quantum attacks are
discussed. Figure 1 illustrates the recent upward trend in
research related to PP-PQB, highlighting the novelty of
this field. Table 5 briefly summarizes the contributions of
privacy-preserving studies in PQB-related studies in journal
papers obtained after specific filtering, as mentioned in
Table 4, such as conference papers, duplicate studies, and
abstract reading. Table 6 discusses the general advantages
and disadvantages of the obtained studies. Table 7 shows
a summary of the protocols used in the studies. Table 8
summarizes the methods used to increase confidentiality and
integrity in the studies. Table 9 provides the effects of the
techniques used in the studies on OISS. Table 10 discusses
the challenges arising from the methods used in the studies
and their impact on real-world usage.
A. REVIEW OF THE SELECTED PAPERS
In [69], the authors proposed the concept of Blockchain
Designated Verifier Proof (BDVP) and designed the scheme,
which was called the privacy-preserving zero-knowledge
proof (ZKP) scheme for blockchain applications. The scheme
emulates a false secret to simulate verifier proof. They also
proposed a post-quantum solution using the Lyubashevsky
scheme based on the SIS problem. This approach includes
innovative elements and methodologies, such as the use of the
chameleon hash function and techniques based on the discrete
logarithm problem (DLP), which contribute to the novelty of
the research.
In [70], the authors aimed to provide unbiased and
randomness through threshold verifiable random functions
(VRF) for proof-of-stake (PoS) blockchain. They provided
a compiler for achieving PQ-VRF from a classical VRF
solution using symmetric-key primitives, validated through
the quantum-safe zero-knowledge systems ZKBoo and
ZKB++. VRF satisfies several critical properties such
as consistency, domain range correctness, probability, and
uniqueness, making it robust and reliable even in the
presence of quantum computing threats. Their proposed
random beacon solution via VRF offers a secure concept of
randomness for properly integrating consensus protocols and
other cryptographic applications.
In [67], the author proposed a new post-quantum secure
lattice-based aggregate signature scheme specifically for
Bitcoin. The paper provided a scheme based on Dilithium
and zk-STARK protocol to minimize the increase in signature size. A lattice-based collective signature scheme was
developed using the zk-STARK protocol and the efficient
Dilithium implementation. The zk-STARK was used to
increase efficiency.
In [71], the authors presented a structure that uses
a post-quantum threshold algorithm resistant to quantum
attacks on private keys to manage blockchain data. The
threshold algorithm is based on NTRU (resistant to quantum
attacks due to the complexity of the problems in the lattice)
and is resistant to quantum attacks such as Grover’s and
Shor’s. A threshold algorithm was used in the system to
reduce the risk of centralization on a key basis. This method
ensured that the private key was divided into parts for
privacy protection and could be solved by participants. Thus,
it enabled the key management encryption to be completed
jointly and data authorization to be completed.
In [72], the authors presented an audit mechanism
using blockchain that eliminates certificate problems with
a lattice-based and identity-based cryptosystem (IBC) in
a cloud storage environment. The data audit mechanism
based on lattice-based cryptography provided data integrity
resistant to quantum attacks. With blockchain, the activities of
third-party controllers (TPA) were monitored, and the central
audit burden was reduced. An identity-based structure was
used for certificate complexity.
In [73], the authors proposed a new traceable lattice-based
traceable ring signature (TRS) scheme with the TripleRing
structure. In the scheme, the TRS structure was improved
and anonymized for resistance against quantum attacks. The
anonymous signature system is based on SIS/LWE problems.
The TripleRing structure was developed by improving the
DualRing structure with short signature sizes, achieving
shorter signature sizes and faster signature generation times.
In [74], the authors developed a post-quantum-based
privacy-preserving access control method for the Industrial
Internet of Things (IIoT). The dynamic access control method
uses the ERC721 smart contract non-fungible token (NFT).
A post-quantum encryption algorithm called NTRU is used
for user privacy, which is resistant to quantum attacks and
efficient for resource-limited IIoT devices. Malicious record
attacks are prevented by the integrated time interval on the
contract.
In [75], the authors presented a blockchain-integrated data
management system in logistics systems and designed a
lattice-based undeniable signature scheme against quantum
attacks. To prevent forgery or false declaration of user identities in the system, a signature-authentication mechanism
was developed, and data security was provided by using
post-quantum cryptographic problems such as SIS and LWE.
In [76], the authors designed a linkable ring signature
(LRS) scheme that provides post-quantum security. The
security of the verification was provided with lattice-based
problems such as SIS and LWE, and a structure resistant to adversary-chosen-key attacks and tamper-proof was
presented to prevent the creation of fake signatures. The
study does not include direct blockchain integration, but it
was designed as an easily integrated solution for security
problems such as manipulating signatures, forgery, and
privacy violations in blockchain-based systems.
In [77], the authors proposed a post-quantum secure
blind signature scheme against quantum computer attacks in
blockchain applications. The scheme used bimodal Gaussian
distribution and rejection sampling to protect sensitive
information. The security of the signature scheme was proven
using the random oracle model. It was proposed for signature
verification in blockchain-based systems.
In [78], the authors presented a configuration of the
zk-SNARK protocol to provide post-quantum security. In the
study, an analysis was presented on how to transform
zk-SNARK proofs into Rank-1 Constraint Satisfiability
(R1CS) relations to obtain efficient computations with
polynomial-based computations using single and multivariate
polynomial (Polaris, Spartan) encodings. It was stated that
the applied method improved the performance of R1CS
encodings. They stated that post-quantum secure zk-SNARK
was constructed with security based on symmetric key
schemes. Lagrangian interpolation was used for efficient
computation of polynomials and the efficiency of the
interpolation was increased by selecting the interpolation
sets as sub-domains. Although the study does not directly
integrate blockchain applications, the proposed polynomialbased zk-SNARK approach has been developed to provide
privacy-security in PQB systems.
In [79], the authors proposed a quantum-resistant
blockchain-based system that preserves privacy by developing the data deduplication protocol (QBDD). In the study,
R-LWE encryption, signcryption, and proxy re-encryption
techniques were used to provide data security, verify the
integrity of the message, reduce data redundancy, and create
a structure resistant to quantum attacks in the vehicular
crowdsensing system. They used a blockchain-based system
to increase the efficiency and fairness of the system.
In [80], the authors proposed a blockchain networkbased Self-Sovereign Identity system design that provides
post-quantum security integrated into the Open Radio
Access Networks (O-RAN) architecture. They presented
a BCN-based solution for a secure authentication and
resource-sharing mechanism between multiple mobile network operators (MNOs). Decentralized Identifiers (DIDs)
and verifiable credentials were used for authentication and
authorization in SSI. No specific PQC algorithm was used in
the system. However, it aimed to optimize PQC calculation
methods based on high-degree polynomial multiplication by
using the Toom-Cook multiplication method to accelerate
mathematical calculations of PQC algorithms.
B. ANSWERS TO THE RQS
1) RQ1 WHAT ARE THE MAIN METHODS FOR PP-PQB?
PQB aims to protect the privacy of users by meeting
both privacy and security requirements. Techniques such
as blind signature, bimodal Gaussian distribution, rejection
sampling, and ZKP that provide anonymity have been
developed and implemented to protect of users sensitive
information and perform secure transactions [81], [82].
In this context, it is expected that blind signature, ZKP,
hybrid cryptography, secure sharing of encryption keys
with quantum key distribution (QKD), data encryption
and anonymization methods, consensus mechanisms, and
smart contract security methods will be developed for
PP-PQB systems to provide resistance against quantum
attacks. Developing these technical methods is critical to
increasing the resilience of blockchain-based systems against
quantum attacks while preserving privacy. This section
provides an overview of the techniques employed for PP-PQB
in the reviewed studies and a summary of the methods
(Table 7).
In [69], the authors provided a method to verify the
proof of pre-determined validators and protect this process
from third parties. It allowed the verifier to verify and
simulate the authenticity of proof using the chameleon-hash
function. It provided post-quantum security by developing the
Lyubashevsky scheme based on the SIS problem and utilizing
lattice-based encryption techniques. In the method they
adopted, With the proposal of a Non-Interactive Quantum
Resistant (NIQR) protocol, they aimed to reduce the number
of interactions between the prover and verifier in the ZKP
process and increase security and privacy with a new protocol
design called BDVP.
In [70], a practical PQ-VRF for the quantum resistive PoS
consensus layer was presented. The work leverages ZKBoo
and ZKB++ with a quantum-resistant hash-based signature. These advanced encryption protocols used multi-party
computation (MPC) techniques (ZKBoo) and NIZK proofs
(ZKB++), which significantly reduce their size. The study
was combined cryptographic techniques with symmetric key
fundamentals to obtain PQ-VRF and integrates VRF into
PoS.
In [67], a new lattice-based aggregate signature scheme
(LAS) method was proposed by using Dilithium and zkSTARK. This method allowed for minimizing the increase
in signature size, which was significantly reduced compared
to using Dilimhium alone. With the zk-STARK integration,
which is a ZKP structure, user privacy was ensured, and
aggregate signature verification was simplified and accelerated. The method they adopted aims to increase post-quantum
security and transaction efficiency, in the case of Bitcoin.
In [71], the methods used are NTRU encryption, linear
secret sharing scheme (LSSS), and threshold algorithm.
The security of the modified NTRU encryption relies on
the difficulty of solving lattice-based problems, particularly
the shortest vector problem (SVP) in lattice cryptography,
which provides resilience against both classical and quantum
attacks. Data was encrypted by dividing it among multiple
participants, and threshold encryption was used to eliminate
the use of centralized management of private keys in
decryption and to cooperate with a certain number of
participants. LSSS was used to decrypt a certain threshold
number of participants, and the private key is shared with a
linear secret-sharing matrix.
In [72], the proposed method used lattice-based cryptography, SIS-based techniques, andIBC. These methods were
integrated to provide post-quantum security for data integrity
checking and secure key management.IBC was used for
secure key generation based on user identities. Blockchain
was used to audit the activities of TPA and cloud service
providers.
In [73], the proposed method introduced a novel
lattice-based TRS using a TripleRing structure, which was
designed to enhance privacy protection against quantum
attacks and implemented in a quantum-resistant blockchain
model. TRS was used to prevent the user from signing
more than once and to provide anonymity. DualRing was
used to make the signature size efficient by reducing it, and
TripleRing was used to make the signature more secure by
adding traceability. Blockchain was used as an access control
mechanism.
In [74], the proposed method employed NTRU encryption,
time interval functions (TIF), and smart contracts. NTRU
encryption provided post-quantum security to protect user
information against quantum attacks, while TIF was used to
prevent malicious registration attempts. Smart contracts were
utilized to manage various transactions. These methods aim
to provide post-quantum secure access to IIoT devices.
In [75], a lattice-based undeniable signature scheme was
designed using the NTRU lattice structure based on the SIS
problem. The method was supported by techniques such
as the bimodal Gaussian distribution and the randomized
nearest-plane algorithm, which are considered computationally hard problems.
In [76], the OrthoTrapGen algorithm, the NIWI proof
system, the OTS, and the SampleRight algorithm were
employed as key components in the post-quantum secure
LRS signature scheme. OrthoTrapGen was used to create
cryptographic trapdoors, enhancing the security of the
signature scheme. The NIWI proof system ensured signer
anonymity within the LRS framework, while OTS prevented
the reuse of signatures. Finally, the SampleRight algorithm
was used to securely generate random secret keys, further
securing the signature process.
In [77], an post-quantum blind signature scheme was
designed using a lattice-based blind signature, Bimodal
Gaussian distribution, rejection sampling, and random oracle
model methods. The blind signature was used for message
signing by hiding user identity. Gaussian distribution is
used to make the blinding process more secure. Rejection
sampling was used to prevent rejection and increase signature
security.
In [78], methods such as zk-SNARK structure, Uni/
Multivariate Polynomial Coding, Fast Reed-Solomon IOPs
(FRI), Lagrange Interpolation, and Fiat-Shamir Transform
were used to provide post-quantum security against quantum
attacks. In Spartan and Polaris schemes in zk-SNARK
structures, Polynomial operations, Hash functions, and
Fiat-Shamir transformation parts were optimized to provide post-quantum security. Collision-resistant hash (CRH)
functions were used to provide post-quantum security.
Uni/Multivariate Polynomial Coding was used to increase
computational efficiency for Boolean or subdomain circuits
by converting R1CS relations into polynomial equations.
FRI is used for fast checking in data verification. Lagrange
interpolation was used to represent the data array with
polynomials. These polynomials are accelerated with FFT
to obtain an efficient computational process. Fiat-Shamir
Transform is used to convert interactive proofs into noninteractive ones.
In [79], methods such as grid-based proxy re-encryption,
MLE, R-LWE, and RSU were used for the post-quantum
blockchain structure against quantum attacks. Grid-based
proxy re-encryption was used for data confidentiality
integrity and non-repudiation against quantum attacks. It was
used to prevent data duplication with MLE.
In [80], the Toom-Cook multiplication method, Hyperledger Indy, DIDComm messaging protocol, and Kubernetes
were utilized for O-RAN-integrated, post-quantum secure
blockchain. Hyperledger Indy and the DIDComm protocol
enabled secure authentication and data transmission within
the O-RAN architecture. Kubernetes CPU management policies improved the efficient use of computational resources.
2) RQ2 WHAT METHODS ARE USED TO IMPROVE
AUTHENTICATION, CONFIDENTIALITY, AND INTEGRITY IN
PP-PQB APPLICATIONS?
Integrating integrity-ensuring protocols like ZKP into PQB
applications significantly enhances the accuracy of computations and strengthens the confidentiality, integrity, and
authentication of inputs. This situation can be evaluated
in three key aspects: enhancing confidentiality (e.g., data
minimization), strengthening integrity (e.g., tamper-proof
proofs and non-repudiation), and improving authentication
(e.g., anonymous authentication). This section discusses the
existing methods and components replaced by techniques
used for PP-PQB in the reviewed studies, along with a
summary of the methods applied to improve authentication,
confidentiality, and integrity.
Table 8 lists the methods used to ensure these functions and provides details of protocols developed specifically to withstand quantum attacks, as utilized in current
research. Protocols such as ZKP, lattice-based encryption,
and NIQR-BDVP are used to strengthen confidentiality and
integrity functions. These methods aim to provide security
in data verification without disclosing identity information
and are particularly focused on post-quantum security.
However, integrating these protocols can increase system
complexity, potentially impacting energy efficiency and
performance.
3) RQ3 WHAT ARE THE EFFECTS OF THE METHODS APPLIED
TO PP-PQB APPLICATIONS ON OISS?
In terms of OISS, the impact on the overall architecture
of PP-PQB applications has been evaluated, particularly
considering the role of ZKP integration within the system.
ZKP, by its nature, can reduce overhead on the blockchain
by verifying the correctness of transactions without revealing
sensitive data. However, proof and verification are computationally intensive, and data related to the proof requires
storage, which can increase the computational overhead and
storage requirement. This may also affect the computational
complexity. Additionally, ZKP supports interaction between
networks and has the potential to facilitate interoperability,
thanks to the verification of incoming transactions without
sharing data. However, the standardization problem of
different systems can make integration difficult, and the
complexity of ZKP can cause difficulty in integrating into
blockchain protocols. If we consider ZKP integration in terms
of scalability, it can enable higher volume transactions on the
chain as it enables efficient transaction verification. It also
has the potential to reduce the overhead on the main chain
significantly, thanks to layer-2 solutions called zk-rollup,
which can verify multiple transactions with a single proof.
However, proof generation time can slow down processing
efficiency, and increased latency can affect the processing
speed of the overall system.
The evaluation of security, which is the last stage of OISS,
with the ZKP integration, ensures that the data is not rejected
and increases confidentiality, as its accuracy is verified
without being disclosed. However, ZKP is challenging
to implement correctly, and integration errors may cause
security vulnerabilities. ZKP integration in PQB provides
significant benefits for OISS. However, the concept to be
proposed will bring additional overhead and complexity and
requires careful evaluation and integration to balance these
effects. Table 9 shows the effects of the methods used in the
studies on OISS. We evaluate the studies we obtained from
the EC in terms of OISS;
Overhead: In PQB-based studies, the complexity of
cryptographic operations and the increase in data processing
times lead to higher transaction fees or reduced efficiency,
creating additional resource consumption.
Interoperability: In PQB-based studies, interoperability
refers to the seamless operation of different blockchain
networks or integrated systems. However, the encryption
standards, key management systems, and security protocols
used in PQB can make it challenging for different networks
to work in harmony with these systems, potentially requiring
additional protocols to ensure interoperability.
Scalability: In PQB-based systems, it is proportional to
the capacity of the network to effectively meet the increasing
demands and transaction volume in terms of managing large
transaction volumes and solving performance problems.
Security: Ensuring the post-quantum security of PQBbased systems against quantum attacks requires assessing
the security of key management, data integrity, signature
verification, and communication protocols used within the
network; this implies that new security vulnerabilities may
arise.
The methods used to solve these problems in classical
crypto-based blockchain systems differ from the methods
used to solve these problems in PBQ systems. In classical crypto-based blockchain systems, optimizations are
made by minimizing transaction times and memory usage
in asymmetric cryptosystems such as RSA and ECDSA.
Symmetric algorithms (such as AES) are combined with
asymmetric algorithms, parallelization is performed, or
low-cost lightweight cryptography is used for IoT devices.
Aggregate signature methods are used due to the PQ signature
size and transaction overhead used in PQB-based systems.
In addition, NIWI, OTS, Rejection sampling, quantum
compatibility layers, and efficient key management systems
such as bonsai tree technology or hybrid approaches are
used. Signatures such as blind signature, Multisignature,
and Threshold Signature are used to make transactions
more secure. Bridges and intermediate layers have been
developed for data and asset sharing between blockchain
networks. Standardized protocols, such as the ERC-20/ERC721 token standard, increase compatibility between smart
contract platforms. In addition, L2 solutions (such as Rollups
and Lightning Network) are used to reduce the overhead on
the main layer of the blockchain. In PQB, off-chain solutions
are used, just as classical blockchains.
4) RQ4 WHAT ARE THE KEY FUTURE CHALLENGES IN
ADOPTING AND IMPLEMENTING PRIVACY-PRESERVING
STRUCTURES, INCLUDING ZKP, IN PQB IMPLEMENTATIONS?
This section explores the limitations, future directions,
and real-world use cases associated with adopting privacypreserving structures within PQB applications. Beyond the
OISS aspects discussed earlier, major challenges include
computational efficiency, robustness, complexity, and usability, as detailed in Table 10.
Computational Efficiency: Computational efficiency is
assessed based on resource utilization, proof size, and proof
generation-verification times. Many studies identified in
Table 10 highlight that ZKP and lattice-based encryption,
despite providing privacy, introduce significant resource
consumption and computational overhead. For instance, [69]
shows that integrating ZKP with chameleon hash functions
enhances security but at a cost to computational efficiency,
while [70] achieves efficiency improvements using ZKB++
to optimize proof sizes and processing times. These examples
suggest a continued need for balancing computational efficiency with privacy requirements, particularly in large-scale
PQB systems.
Complexity, Usability, and Real-World Usage: Complexity
often arises from additional verification and encryption
stages, as seen in various studies within Table 10. In [67],
for instance, the zk-STARK integration adds complexity due
to enhanced storage requirements, while in [71], NTRUbased threshold encryption increases complexity yet ensures
secure key distribution. Real-world usability often depends
on designing user-friendly interfaces, especially for resourceconstrained environments. Practical applications, such as in
IoT or IIoT systems [74], require careful integration of
complex cryptographic techniques to maintain scalability
and usability. However, these methods often raise gas fees
and overhead, impacting the usability in high-transaction
environments.
Numerous studies in Table 10 show that optimizing
computational resources is critical. Methods like zk-rollup
for proof efficiency [70] and multivariable polynomial
optimizations [78] offer promising directions, but achieving a balance between performance and security remains
challenging. Future PQB systems should focus on simplifying complex cryptographic protocols without compromising security. Ensuring compatibility across different platforms [80] and developing user-friendly cryptographic tools
are essential to facilitate practical adoption. Applications like
smart transportation systems [79] and spectrum sharing in
next-generation wireless networks [80] illustrate the growing
demand for scalable, privacy-preserving solutions. However,
challenges remain in achieving efficient processing times
and managing large transaction volumes in real-world PQB
implementations.
These challenges underscore the need for ongoing research
to optimize computational efficiency, manage complexity,
and enhance usability in PQB systems.
V. DISCUSSION, THREATS, AND FUTURE RESEARCH
DIRECTIONS
The rapid development of quantum computers and their
accompanying communication and data management systems also pose security issues and a serious threat to existing
systems [83]. Although studies have been conducted that
have the potential to provide solutions resistant to quantum
attacks for PQB systems, significant challenges remain in
the PQ era. Some current problems that arise in the process
of adopting privacy-preserving structures include system
complexity, performance and energy efficiency, compatibility
issues, and secure data management. Although existing
solutions try to alleviate these problems, problems such as
the smooth interaction of blockchain networks in the PQ
era, the mathematical complexity of PQ signature schemes,
and the performance-security balance are still significant
challenges, and further research is needed in these areas [26].
The mathematical complexity of PQ-based signature schemes
and the computational costs they bring, especially the
transaction volume and verification times, negatively affect
the performance of blockchain systems. PQB-based systems
can cause performance problems, especially in large-scale
use of blockchain networks. There are also issues with integrating PQB systems with blockchain networks, especially
cross-chain compatibility between traditional blockchain
solutions and post-quantum robust structures. Moreover,
the scalability problem in blockchain becomes even more
complicated with the integration of PQC.
In Table 11, while some components have been made PQsecure, critical parts such as the consensus mechanism and
ZKP still work with classical methods. In addition, there
are no hybrid systems where metrics such as performance
and security are considered together. These two metrics
are mostly optimized separately, but structures such as the
security-performance relationship metric model should be
addressed in response to the security-performance tradeoff challenge for PQB-based systems. In addition, the
development of post-quantum secure ZKP schemes and their
integration into PQB systems is another important metric that
needs to be addressed.
Studies show that integrating post-quantum cryptography
into blockchain architectures and ZKP and LBC methods
into PQB systems presents various challenges. Lattice-based
cryptosystems such as Kyber and Dilithium have larger
key sizes than traditional public-key algorithms, leading to
more processing time and memory overhead. In addition,
key and signature sizes cause delays in data transfer on
the network. This can be a critical problem, especially in
resource-constrained IoT-based blockchain systems. It also
increases the need for data storage in the blockchain and
can lead to rapid growth in the total size of the chain.
Moreover, implementing PQC in smart contract mechanisms
and security protocols can cause delays due to long computational times in applications that require high transaction
capacity and result in increased processing power and energy
consumption, especially in transaction verification processes.
Complex operations in PQC can increase gas costs and make
it difficult for users to adopt these systems. Making smart
contract languages such as Solidity compatible with PQC
may require the development of new compilers or tools. High
computational costs can also affect the efficiency of consensus protocols in their working mechanisms. At this point,
solutions such as ZKP-based zk-rollup, which improves
privacy, can reduce the storage load on the blockchain by
compressing transactions. However, ZKP-integrated schemes
may increase transaction times when additional security
components are used, creating a high computational overhead, and the lack of complete security analysis may
pose a risk to system security. Although the ZKBoo and
ZKB++ structures, used to provide short signature keys and
randomness reliability, are promising, the complexity of these
techniques increases computational overhead and can pose
challenges in terms of applicability. In addition, NTRU-based
and threshold encryption techniques may cause performance
issues in large-scale structures and introduce vulnerabilities
against denial of service (DoS) attacks. Finally, lattice-based
blockchain integrations face cost and transaction overhead
challenges when confronted with high transaction volumes
and expanding network structures, which results in additional
costs and security risks in auditing processes.
In cryptographic methods, it is important to choose
the most suitable algorithm based on the needs of the
system and performance metrics such as computational cost,
processing times, and resource usage. Computational cost is
proportional to the power and time the selected algorithm
consumes during processing. This metric is especially
critical in resource-constrained IoT devices. Processing time
is an important metric in applications that require highspeed processing, such as real-time financial transactions.
Another metric, resource usage, is critical in environments
such as systems with large data processing capacity or
resource-constrained IoT devices. Since lattice-based algorithms require large processing power, they must be carefully
integrated for real-time applications due to the determined
metrics. In addition, large key and signature sizes can
create additional overhead in terms of both data transfer
and storage. Post-quantum secure lattice-based cryptosystems such as Kyber or Dilithium, which are integrated
into protocols optimized for such systems, are suitable.
In addition, in ZKP protocols that provide privacy, zkSNARK may be a disadvantage for large-scale systems that
perform more transactions than the zk-STARK structure.
Slower, more secure algorithms may be preferred in areas
with low transaction frequency, such as health records. The
proposed decision-making structure is detailed in Table 12
by classifying the algorithms according to their performance
metrics. However, NIST-approved post-quantum algorithms
such as Kyber, Dilithium, and FALCON are not yet optimized
for integration with blockchain frameworks like Ethereum
or Hyperledger. Ethereum has an EVM structure that
supports traditional cryptographic protocols for executing
transactions. This integration can significantly increase the
transaction time and data storage requirements on Ethereum.
Especially for smart contracts, using these algorithms can
increase the existing gas fees and negatively affect the
user experience. Hyperledger Fabric’s modular architecture
facilitates the integration of different algorithms. However,
in large-scale networks, the integration of these algorithms
can create an additional overhead on transaction throughput
and network performance. Therefore, challenges such as
the current determined transaction time or storage impact
continue to be the current challenges in this integration. Furthermore, these algorithms may be vulnerable to side-channel
attacks, especially in hardware-based implementations [84].
Such attacks aim to access sensitive information through
side channels such as power consumption, electromagnetic
leakage, or timing information. Moreover, in real-world
applications, there is a risk of being vulnerable to attacks
due to coding errors, verification processes, vulnerabilities
that may occur during key management, and non-optimized
application processes [85].
Considering the existing studies examined, they usually
focus on only certain components of PQB systems, such
as digital signatures or key exchange. These studies cannot
provide fully integrated solutions covering all components.
This leads to the lack of fully post-quantum secure blockchain
architectures. Moreover, it has been observed that hybrid
systems that combine traditional blockchain solutions with
post-quantum systems to ensure compatibility have not been
sufficiently investigated. It has also been observed that the
large key sizes and high computational requirements of
lattice-based and other post-quantum cryptographic algorithms create scalability problems, and existing studies do
not sufficiently address how to manage this balance. ZKP
plays a critical role in privacy in PQB systems. However,
the development of quantum-resistant ZKP protocols is
still in the early stages. Current implementations create a
computational burden that is too high to be used in large-scale
systems. It has been observed that most studies are theoretical
and do not offer a limited number of practical tests or realworld applications. It has also been observed that consensus
protocols have not been sufficiently addressed with quantumresistant innovations.
Considering all these situations, it has been concluded
that the solutions applied in the literature to provide this
performance-security balance can be improved. Based on
this, future research directions and open problems in the
existing literature regarding the integration of PP-PQB
applications have been identified.
1) Using the standardized protocols and developing
communication protocols that provide interoperability
across chains are important issues in PP-PQB studies
as a future research guideline.
2) Investigating optimization techniques to reduce computational overhead without compromising security
in architectures built using PQC techniques and
privacy-preserving structures (such as ZKP).
3) Production verification of integrated ZKP types can
also optimize the layer-based architecture for computational efficiency to reduce the overhead.
4) The use of ZKP in post-quantum symmetric and codebased structures is limited in the current literature and
has potential research opportunities for PP-PQB.
5) Developing user-friendly cryptographic tools and interfaces for usability in practical applications built using
PQC techniques and privacy-preserving structures can
contribute to adopting more effective integration in
blockchain applications.
6) Systems based on a single chain have limitations in
terms of scalability and efficiency. Therefore, integrating multi-chain models can contribute to efficiency and
scalability by enabling components in the system to
operate on different chains.
7) Post-quantum-resistant versions of bridges used in
post-quantum blockchains must be developed, and
hybrid protocols must be developed to integrate with
off-chain systems.
8) Layer2 solutions such as Lightning Network, which
are used for efficiency and performance in classical blockchain-based solutions, can be made
quantum-resistant in PQB systems. In cases requiring
high transaction volume, the security and performance
of the main chain can be maintained.
9) Integrating algorithms such as Kyber and Dilithium
in resource-constrained IoT environments can improve
Number Theoretic Transform (NTT) performance by
using reduced processing cycles and low-precision
computational methods to reduce the computational
overhead.
10) To implement the lattice-based cryptographic algorithms recommended by NIST securely, hardware and
software solutions resistant to side-channel attacks
should be developed, and formal verification techniques should be applied on an application basis.
11) In cases where more substantial key sizes are required
to integrate lattice-based algorithms in IoT environments, fully secure versions can be implemented on
central servers with a multi-layered structure that
allows the algorithm to choose different security levels
according to resource availability.
Future research should also address these issues, such
as ensuring cross-chain compatibility, increasing scalability
without compromising security, and developing new methods
for designing and compatibility with user-friendly systems
and post-quantum security. Further studies on how applications perform in real-world scenarios are also important.
This section discusses the challenges faced by current studies and future research directions. In particular, suggestions
are provided for optimizing post-quantum algorithms and
improving the performance of ZKP in resource-constrained
IoT devices.
VI. CONCLUSION
Traditional blockchain protocols, which are vulnerable to
quantum attacks, can significantly increase security and
trust with post-quantum cryptography. PQC techniques
and privacy-preserving structures in PQB applications,
which have attracted recent attention, have the potential
to strengthen privacy and security. Therefore, research on
privacy-preserving structures has become the new goal in
PQB applications. In our study, we present a systematic
review with RQ regarding using privacy-preserving structures in PQB applications. We specifically focus on ZKP
applications that provide enhancing features for PQB. In the
systematic report, we explain the main methods for PPPQB (RQ1), the impact of privacy-preserving structures on
confidentiality and integrity in PQB applications (RQ2), the
impact of the solutions on OISS (RQ3) and how they are
evaluated, and the future steps of using privacy-preserving
structures in PQB applications (RQ4). Our findings indicate
that research studies for using privacy-preserving structures
in PQB applications are new, and research addressing the
current issue has deficiencies in OISS solutions of PPPQB. We hope our study can help further research-adoption
of using privacy-preserving structures in PQB applications.
In future studies, we plan to implement layer-based architecture to solve OISS challenges and improve privacy when
using privacy-preserving structures in PQB applications.