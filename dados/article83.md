Title: IOTA-Assisted Self-Sovereign Identity Framework for Decentralized Authentication and Secure Data Sharing

ABSTRACT The Internet of Things (IoT) demands robust mechanisms for secure communication
and trust establishment among connected devices. Traditional Public Key Infrastructure (PKI) solutions
face limitations in scalability, centralization and single points of failure. These limitations hinder their
effectiveness in dynamic IoT environments. To address these challenges, this paper introduces a new
decentralized authentication protocol for secure identity management and data exchange in IoT, called
ISIF (IOTA-Assisted Self-Sovereign Identity Framework). This framework is based on Self-Sovereign
Identity (SSI) principles and leverages Decentralized Identifiers (DIDs) and Verifiable Credentials (VCs)
to enable mutual authentication without relying on centralized authorities. DIDs ensure decentralized
identity management and VCs provide verifiable context-specific claims. This dual-layer approach enables
robust and attribute-based authentication, which reduces the risk of unauthorized access and improving
interoperability in decentralized IoT environments. ISIF employs the IOTA Tangle as a distributed ledger
to manage and verify DIDs and VCs. This offers a decentralized, immutable record that supports efficient
and tamper-resistant identity management. ISIF ensures that all interactions within the IoT network are
securely authenticated and resilient to tampering. The experimental results show that the framework
maintains efficient DID generation and VC issuance times even as network size scales, overcoming the
bottlenecks inherent in PKI-based systems. Experimental results demonstrate that ISIF maintains efficient
DID generation and VC issuance, even as network size scales. Experimental results show that DID generation
time increases from 1.85 ms (for 50 nodes) to 10.81 ms (for 250 nodes), while VC issuance time ranges from
2.66 ms to 13.21 ms. Similarly, VC verification time increases from 3.54 ms to 22.27 ms as the network
scales. Despite these increases, the overall end-to-end (E2E) delay remains low (0.16–0.33 ms), ensuring
efficient real-time authentication. These findings confirm ISIF’s feasibility for large-scale IoT authentication
without performance degradation. Furthermore, the IOTA Tangle’s performance in handling varied payload
sizes affirms its suitability for managing block generation and retrieval in IoT, ensuring practical processing
times that uphold security and decentralization.
INDEX TERMS IOTA tangle, IoT, SSI, DID, VC.
I. INTRODUCTION
IoT is connecting countless devices worldwide and transforming how we interact with technology in everyday life.
IoT nodes or sensors continuously gather, process, and share
data to support applications across smart cities, healthcare,
industrial systems, and more [1]. However, as more IoT
devices are deployed, securing them becomes a major challenge [2]. Traditional identity and authentication methods
struggle to keep up with the scale and security demands of IoT
networks. Issues such as data privacy, device authentication,
and communication security require special attention [3], [4].
SSI is emerging as a promising solution to the
above-mentioned security concerns. SSI allows entities to
generate and control their own DIDs without relying on
centralized authorities [5]. While DIDs are self-issued and
anchored in a decentralized Verifiable Data Registry (VDR),
VCs may still involve trusted issuers for credential issuance.
By using DIDs and VCs, entities in an SSI framework can
securely authenticate each other [6]. This also allows sharing
of data in a privacy-preserving manner [7]. This model is
particularly valuable for IoT, where decentralization and lowpower, lightweight protocols are often essential [8].
PKI systems face significant limitations when applied to
large-scale IoT networks. They rely on centralized Certificate
Authorities (CAs) to issue and validate certificates. This
results in creating single points of failure, which increase
vulnerability to attacks [9], [10]. This centralization not
only introduces scalability issues but also raises trust
concerns [11], [12]. This can be attributed to the fact
that any compromise of the CA can affect the entire
network. Additionally, PKI systems require extensive management and maintenance. These systems constantly need
to renew, revoke, and update certificates [13]. IoT devices
are constrained by limited power and processing capabilities.
However, this process is resource-intensive and impractical
for IoT devices [14]. These limitations highlight the need
for a more decentralized, scalable, and efficient identity
management model suitable for the unique demands of IoT.
This paper introduces a new SSI-based scheme for mutual
authentication and secure data sharing specifically for IoT
environments, called ISIF. Each IoT node and user in
ISIF has a unique identifier registered on a IOTA Tangle.
This identifier supports cryptographic verification, making
it possible to authenticate each device and user securely.
Additionally, VCs issued by a trusted credential issuer (T CI)
provide proof of identity and permissions, allowing nodes and
users to trust each other without needing to contact a central
authority every time. Multiple T CIs can exist within the system, enabling a distributed and scalable credential issuance
process. Once issued, VCs are cryptographically signed and
can be verified in a fully decentralized manner using the
IOTA Tangle, ensuring that authentication does not rely on
the TCI. This preserves decentralization while maintaining
trust in identity issuance [15], [16]. Authentication and secure
data sharing occur in several phases, each with specific steps
that contribute to the overall security of the system. First,
both IoT nodes and users generate DIDs. Then, the concerned
trusted authorities issue VCs to these entities. Finally, the
mutual authentication and secure data-sharing processes
use these credentials and a shared session key to protect
communications. This setup provides end-to-end encryption,
data integrity, and privacy for sensitive information.
While DIDComm offers a robust solution for secure and
decentralized messaging [17], our approach takes a more
tailored path to address specific challenges in the ISIF framework. DIDComm primarily focuses on peer-to-peer communication, ensuring secure data transmission without reliance
on intermediaries [18]. However, it is not inherently designed
to manage the authentication and authorization processes
within large-scale IoT environments. In ISIF, we utilize VSs
and DIDs to establish a scalable and efficient authentication
mechanism. Unlike DIDComm, which is predominantly used
for secure communication between established entities, ISIF
introduces a comprehensive trust management framework.
This framework supports key rotation, prevents malicious
activities, and maintains resilience against various attacks.
Furthermore, DIDComm’s reliance on message-based interactions introduces challenges in scenarios where real-time
verification and validation are required. Our approach
mitigates this by leveraging the immutable nature of the IOTA
Tangle for transparent and verifiable credential management.
The decentralized storage of credentials ensures data integrity
and enables seamless verification without requiring continuous connectivity. ISIF’s focus on session-based authentication through established DIDs ensures robust identity
verification. This approach reduces reliance on continuous
messaging protocols, minimizing overhead and enhancing
the overall system performance.
The goal of this research is to present a decentralized,
scalable model for IoT security that minimizes reliance on
central servers and increases user control over their data.
By combining SSI principles with the unique requirements
of IoT networks, this approach improves the resilience and
security of IoT deployments across various sectors. The
contributions of this research are given below.
• This paper overcomes the challenges faced by centralized PKI architecture and introduces a novel decentralized mechanism for authentication of IoT devices.
• We propose a novel lightweight mutual authentication
mechanism between IoT devices and users for resourceconstrained devices.
• A secure data sharing mechanism allows establishing a
session key and secure sharing of sensitive data between
different entities in the system.
• ISIF gives the owners full control over their identities
by generating DIDs and VCs for node identification and
verification.
• We integrate IOTA Tangle in the identity authentication
mechanism for decentralization, immutability, confidentiality and integrity.
The rest of the paper is organized as follows. Recent
literature has been reviewed in Section II. The proposed
methdology for ISIF is given under Section III. In Section IV,
we evaluate ISIF in terms of computation cost. Finally,
we conclude the study under Section V.
II. LITERATURE REVIEW
In this section, we summarize the literature review. The
literature has been divided into three categories: PKI-based,
DLT-based and SSI-based authentication schemes.
A. PKI-BASED AUTHENTICATION
Mahmood et al. in [19] address the challenge of secure
data exchange in an IoT-enabled Maritime Intelligent Transportation System (MTS), where unauthorized access risks
compromise critical maritime data. The proposed solution is a
Physically Unclonable Function (PUF)-based authentication
and key agreement scheme that authenticates mobile users
and IoT nodes through a cloud gateway. The methodology
comprises multiple phases, including initialization by the
Big Data Registration Center to set system parameters, predeployment of IoT node credentials by the cloud gateway, and
a mutual authentication phase between mobile users and IoT
nodes via the cloud gateway. A key strength of this scheme is
its resilience against physical security threats, ensuring secure
authentication and communication with reduced overhead.
Enhancing drone communication security through PKI
addresses vulnerabilities like eavesdropping and unauthorized access[20]. The PKI-based solution secures drone communication channels using asymmetric encryption and digital
certificates issued by CAs to validate drone identities. The
protocol includes mutual authentication between drones and
ground control, data integrity checks via digital signatures,
and data confidentiality through TLS encryption. Additional
security layers, like certificate and key pinning, fortify the
scheme against spoofing and man-in-the-middle attacks. This
approach leverages elliptic curve cryptography (ECC) for
efficient key management, offering robust protection with
low computational requirements, making it well-suited for
resource-constrained drone environments.
An efficient authentication protocol for resource-constrained
devices in IIoT has been proposed in [21], called REAPIIoT. REAP-IIoT employs a lightweight cryptographic
algorithm, AEGIS [22], for authenticated encryption with
associated data (AEAD). This ensures secure session key
establishment while minimizing computational overhead.
The protocol is divided into six phases: device and user
registration, authenticated key exchange, biometric-based
password change, revocation, and dynamic device deployment. Security validations use the random-or-real model and
Scyther for resilience against attacks such as replay and manin-the-middle. REAP-IIoT’s strengths are its low resource
requirements, robust defense against various attack vectors,
and effective session key management, making it highly
suited for IIoT environments where efficiency is crucial.
B. BLOCKCHAIN-BASED AUTHENTICATION
Zhaofeng et al. address the security vulnerabilities of
centralized authentication in IoT and edge environments
in [23]. They propose a blockchain-based decentralized
scheme called BlockAuth. This scheme uses each edge
device as a blockchain node to establish a distributed
network, enhancing fault tolerance and security. The scheme
starts with secure registration, where users generate certificates with cryptographic signatures that are validated
through a decentralized network. The authentication phase
involves transaction verification by blockchain nodes, using
Practical Byzantine Fault Tolerance (PBFT) as the consensus mechanism. BlockAuth incorporates multiple cryptographic techniques, such as the Elliptic Curve Digital
Signature Algorithm (ECDSA) for signature validation and
Hyperledger Fabric for platform deployment. The strengths
of BlockAuth include high fault tolerance, suitability for
various authentication types (e.g., biometric, certificatebased), and scalability due to decentralized verification,
making it a robust choice for secure authentication in IoT.
The study in [24] tackles issues of centralized trust in
IoT security by proposing a blockchain-based distributed
architecture for authentication and key management. The
scheme eliminates the need for a trusted third party, instead
using hash chains and blockchain’s inherent immutability
for secure authentication. The framework operates across
three layers—device, fog, and cloud. Devices are managed by access-managing nodes in the fog layer, which
handle authentication and key distribution within domains,
while manager nodes in the cloud layer oversee interdomain communications. Through hash chains, the system
generates and validates keys efficiently without needing
direct device-to-device verification. A notable strength is the
system’s scalability and improved security over traditional
centralized solutions, confirmed through Ethereum-based
implementation.
Garba et al. [25] highlight the challenges of traditional PKI in IoT due to high resource demands
and inefficiencies. LightCert4IoTs presents a blockchainbased, lightweight self-signed certificate model tailored
for resource-constrained IoT environments. The scheme
leverages local registration authorities (LRAs) at the edge
to verify certificates and utilizes the Ethereum blockchain
as a global notary, storing certificates on the immutable
ledger. The system eliminates dependency on conventional
CAs, and self-signed certificates allow for reduced certificate
size, memory, and processing demands. Methodologically,
LightCert4IoTs enables IoT devices to issue self-signed certificates, which LRAs validate and record on the blockchain,
streamlining certificate management. This approach achieves
lower operational complexity and cost, making it ideal
for IoT devices with limited resources. Key strengths
include reduced processing overhead, independence from
centralized authorities, and streamlined authentication suited
for IoT.
IoT security has been enhanced in [26] by addressing
vulnerabilities in PUF (Physical Unclonable Function)-based
authentication. It introduces a lightweight PUF-PKI scheme
for secure authentication on cloud-based IoT systems. The
method employs dual CAs for added security and uses
PUF-generated keys for device identity verification. The
scheme involves two main phases: setup, where initial
credentials and challenges are generated, and authentication,
where mutual verification between the device and server
occurs through PUF and PKI credentials. Security validation
via the Tamarin prover supports its robustness against threats
like impersonation, replay, and tampering. Key strengths
include strong resistance to cloning and impersonation
attacks, robust mutual authentication, and reduced CPU
usage, making it highly suitable for IoT applications requiring
lightweight security solutions.
TABLE 1. Comparative Analysis of SSI-based Authentication Approaches.
C. SSI-BASED AUTHENTICATION
Smart DID addresses the challenge of privacy-preserving
identity management in IoT, where conventional centralized
identity solutions fall short due to security and resource limitations [27]. The paper proposes SmartDID, a blockchainbased identity system that uses a dual-credential model,
comprising plaintext and cryptographic credentials, along
with zero-knowledge proofs to protect sensitive data and
thwart identity linkages. The system’s DIDs allow users
privacy while resisting Sybil attacks, and a systematic proof
system ensures privacy without relying on central authorities.
SmartDID’s approach balances privacy, transparency, and
low resource demands, making it suitable for diverse IoT
environments.
In [28], Fathalla et al. seek to enhance the security
and resilience of SSI in digital identity management for
IoT, focusing on frequent data integrity and share-refresh
mechanisms. PT-SSIM improves on previous models by
using proactive share refreshing and decentralized storage
capsules, enabling identity information to resist tracking and
tampering. The system incorporates zero-knowledge proof
and secret-sharing techniques, allowing users to manage
identity credentials securely while reducing the need for
repeated issuer involvement. This dynamic management
model strengthens SSI’s protection against attacks and
supports robust data integrity, confidentiality, and compliance
in IoT environments.
The work done in [29] addresses the trust and security
challenges in edge-enabled IoT systems where malicious
attacks, such as replay and man-in-the-middle, can severely
impact device interactions. TACAS-IoT introduces a layered
trust model (local, semiglobal, and global) to secure data
exchanges from IoT devices to edge devices and up to cloud
servers. Each trust layer aggregates certificates and trust
values, supporting mutual authentication and session key
establishment between devices. The system comprises five
key phases: system initialization, registration, authentication
and key establishment, dynamic device addition, and trust
evaluation. Through elliptic curve cryptography, hash functions, and temporal credentials, TACAS-IoT ensures robust
mutual authentication and low computation overhead. The
scheme’s strengths lie in its structured trust hierarchy, low
communication overhead, and effective resistance to various
attacks.
Battah et al. proposed a scalable, decentralized framework
that combines distributed ledger technology (DLT) and
reputation mechanisms to address the need for computational
trust among IoT services [30]. The framework utilizes
smart contracts (SCs), decentralized storage, and oracles
to facilitate transparent and scalable reputation assessments
among IoT service providers (SPs) and requestors (SRs).
IoT devices register using unique identifiers verified by
their manufacturers, and their interactions and feedback are
stored immutably on the blockchain, allowing a flexible trust
evaluation. This system supports access control, anonymous
feedback submission, and customizable trust calculations
based on feedback. Key strengths of this system include modularity, privacy-preserving trust evaluations, and resistance to
manipulation and single points of failure through DLT-based
transparency and decentralized validation mechanisms.
The authors of [31] propose an extension to the TLS 1.3
handshake to integrate SSI authentication for IoT systems. They introduce two new authentication modes that
incorporate SSI alongside the existing X.509 certificatebased authentication. The proposed solution extends the
TLS handshake with additional messages for negotiating
SSI authentication, exchanging VCs, and verifying DIDs
stored on a DLT. The framework allows a hybrid authentication mode, which supports gradual adoption of SSI
while ensuring backward compatibility with traditional TLS
implementations. The experimental results validate its performance in terms of handshake latency and computational
overhead. However, the work could be further optimized
by reducing the overhead of DID resolution and exploring
more efficient revocation mechanisms for VCs in real-world
deployments.
Table 1 provides a detailed comparison of these authentication schemes. The table evaluates these schemes across eight
key dimensions:
• Privacy: Reflects how well the approach protects user
identity and data confidentiality. SSI-based approaches
excel in privacy due to DIDs and zero-knowledge proofs.
• Computational Overhead: Assesses the resource consumption during authentication and credential management. Blockchain approaches have higher overhead
compared to PKI and SSI.
• Scalability: Evaluates the ability to handle increasing numbers of users and devices. Blockchain and
SSI frameworks demonstrate better scalability through
decentralized management.
• Decentralization: Represents the reliance on distributed networks. Blockchain and SSI approaches
ensure decentralization, while PKI remains dependent
on centralized CAs.
FIGURE 1. Entities and flow of data in the proposed system model.
• Data Integrity: Highlights the resilience of data against
tampering or unauthorized alterations. Blockchain and
SSI solutions provide robust data integrity through
immutable ledgers and cryptographic verification.
• Attack Resilience: Analyzes protection against various
cyberattacks, including replay, man-in-the-middle, and
Sybil attacks. SSI and blockchain-based approaches
offer stronger attack resilience due to cryptographic
security and consensus mechanisms.
• Flexibility: Indicates the adaptability of the system to
diverse use cases and environments. SSI-based systems
provide high flexibility due to the independence of DIDs
and VCs.
The proposed ISIF is also included in the table to show
its advantages over existing approaches. ISIF achieves high
privacy, low computational overhead, and robust attack
resilience by employing a decentralized, self-sovereign identity framework. These strengths together make it well-suited
for large-scale and resource-constrained IoT environments.
III. ISIF: IOTA-ASSISTED SELF-SOVEREIGN IDENTITY
FRAMEWORK
The proposed system model is given in Figure 1. This figure
shows the entities in the system: IoT Sensor Node (ISN),
Remote User (RU), a set of TCIs (Trusted Credential Issuers),
Verifier and IOTA Tangle. ISNs are the devides that collect
and share data in the network. RUs are individuals who
interact with ISNs using smartphones to use ISNs. TCIs issue
VCs to both ISN and RU, and a verifier verifies their VCs. The
DIDs are distributedly and securely stored on IOTA Tangle.
The designed protocol consists of three parts: initialization,
mutual authentication, and secure data sharing, as given in the
subsequent subsections. Table 2 provides a list of notations
used in this section.
A. INITIALIZATION
In the Initialization Phase, the foundational setup required
for secure mutual authentication and data sharing in the
TABLE 2. List of notations.
IoT ecosystem is established. This phase includes generating
unique identities for all entities involved and setting up the
cryptographic infrastructure necessary to maintain trust and
integrity across the network.
1) STEP 1: ISNI DID GENERATION
Each node ISN i begins by generating a unique DID, denoted
DIDISNi
. This identifier DIDISNi
serves as the globally unique
identifier for each ISN i
in the network and is designed to
support secure and verifiable interactions.
a: DID DOCUMENT CREATION
Once DIDISNi
is generated, ISN i creates an associated
DID Document, denoted DID_DOCISNi
. This document is
essential as it holds key information that other entities in the
IoT network will use to verify the identity and authenticity
of ISN i
. The DID Document DID_DOCISNi
for each ISN i
includes:
• Public Keys: Each ISN i
is assigned a unique public
key PKISNi
, which is part of a key pair (PKISNi
, SKISNi
).
This public key enables cryptographically secure communication and signature verification. The public key
PKISNi
is derived from a private key SKISNi
as follows:
PKISNi = g
SKISNi mod p (1)
where g is a generator of a prime-order group G, and p is
a large prime. This setup enables secure authentication
without relying on a central authority.
• Service Endpoints: These endpoints define the communication methods and protocols by which other
entities in the IoT network can interact with ISN i
.
Service endpoints provide connection details, such as IP
Algorithm 1 Initialization Phase: DID Generation and
Cryptographic Setup
Input: ISN = {ISN1, ISN2, . . . ,ISNn}, RU = {RU1, RU2, . . . , RUm}
Output: DIDISNi
, DIDRUi
, DID_DOCISNi
, DID_DOCRUi
, PKTCI
1: Select p
2: Select g ∈ G
Phase 1: ISN i DID Generation
3: for each ISNi ∈ ISN do
4: Generate DIDISNi
5: SKISNi ← Random(Zp)
6: PKISNi ← g
SKISNi mod p
7: DID_DOCISNi ← {PKISNi
, EndpointsISNi
, AuthMethodsISNi
}
8: Publish DID_DOCISNi
to IOTA Tangle
9: end for
Phase 2: RUi DID Generation
10: for each RUi ∈ RU do
11: Generate DIDRUi
12: SKRUi ← Random(Zp)
13: PKRUi ← g
SKRUi mod p
14: DID_DOCRUi ← {PKRUi
, EndpointsRUi
, AuthMethodsRUi
}
15: Publish DID_DOCRUi
to IOTA Tangle
16: end for
Phase 3: TCI Key Pair and Cryptographic Parameters
17: SKTCI ← Random(Zp)
18: PKTCI ← g
SKTCI mod p
19: DID_DOCTCI ← {PKTCI , EndpointsTCI , AuthMethodsTCI}
20: Publish DID_DOCTCI to IOTA Tangle
addresses or URIs, allowing authorized entities to send
requests and receive responses securely.
• Authentication Methods: The authentication methods
specify the verification procedures for authenticating
ISN i
. In this setup, authentication is achieved through
public key cryptography, where the authenticity of
ISN i can be verified using its public key PKISNi
.
b: PUBLICATION OF THE DID DOCUMENT:
To make DID_DOCISNi
available for public verification,
it is published on the IOTA Tangle. This decentralized
publication ensures that the identity and cryptographic details
of each ISN i are accessible to other entities within the
network. Consequently, this setup creates a trust model
where identities are verifiable without relying on a single,
centralized authority.
Similarly, RUi creates DIDRUi
and DID_DOCRUi
. Once
complete, DID_DOCRUi
is published on IOTA Tangle to
enable other IoT entities to verify RUi’s credentials.
2) STEP 3: CRYPTOGRAPHIC SETUP BY T CI
The cryptographic setup by T CI is essential for secure credential issuance and authentication within the IoT ecosystem.
T CI acts as the credential issuer, responsible for creating and
signing VCs for both ISN i and RUi
.
a: PUBLIC-PRIVATE KEY PAIR GENERATION:
T CI generates a public-private key pair (PKTCI , SKTCI ),
which is essential for signing and verifying credentials within
the network:
• PKTCI : The public key of T CI, made publicly accessible on the IOTA Tangle within the DID Document
DID_DOCTCI . This public key is used by other entities
to verify signatures on credentials issued by T CI.
• SKTCI : The private key of T CI, securely stored to
prevent unauthorized access. This key is exclusively
used to sign VCs for ISN i and RUi
, providing proof
that these credentials are issued by a trusted authority.
b: CRYPTOGRAPHIC PARAMETER SELECTION:
For secure operations, T CI selects cryptographic parameters
as follows:
• Elliptic Curve or Prime-Order Group Selection:
T CI may choose an elliptic curve E(Fp), where p is
a large prime, or a prime-order cyclic group G with
generator g for cryptographic operations. This group
choice supports efficient public key cryptography.
• Hash Function: A secure hash function H : {0, 1}
∗ →
G is employed for mapping arbitrary-length data to the
group G. This function ensures that identity representation and data integrity checks are secure.
c: PUBLISHING CRYPTOGRAPHIC DETAILS ON THE TANGLE:
The public key PKTCI and relevant cryptographic details are
included in DID_DOCTCI and published on the IOTA Tangle.
This publication process enables all network entities to access
T CI’s cryptographic parameters, facilitating transparent and
decentralized verification of credentials.
It is important to note that while the cryptographic
setup in this framework utilizes a PKI-based signature
generation and verification method, it eliminates reliance on
a centralized CA for issuing certificates. Instead, public keys
are securely published on the IOTA Tangle through DID
Documents. This decentralized approach ensures transparent
and tamper-resistant public key distribution, enhancing trust
and security in the network.
Algorithm 1 summarizes the initialization phase. This
phase sets up the foundational cryptographic infrastructure
and decentralized identity framework for secure, authenticated, and privacy-preserving interactions between ISN i
,
RUi
, and T CI within the IoT environment.
B. CREDENTIAL ISSUANCE
With the cryptographic parameters in place and the key pair
securely managed, T CI is now ready to issue VCs. It defines
the schema for VCs, including required fields DIDISNi
,
DIDRUi
, permissions associated with the entity (e.g., access
rights, device type, or ownership details), and expiration dates
or revocation status for managing credential validity. Our
implementation uses a W3C-compliant VC format to ensure
interoperability and standard compliance.
1) STEP 1: CREDENTIAL ISSUANCE TO ISNI
The T CI generates a VCISNi
for each ISN i
, which includes:
VCISN = {DIDISNi
, metaISNi
, Texp} (2)
Algorithm 2 Credential Issuance Phase: VC Generation
Input: ISN = {ISN1, ISN2, . . . ,ISNn}, RU =
{RU1, RU2, . . . , RUm}, (PKTCI , SKTCI )
Output: VCISNi
and VCRUi
Phase 1: VC Issuance for ISNi
1: for each ISNi ∈ ISN do
2: Gather metadata MetaISNi
3: VCISNi ← {DIDISNi
, MetaISNi
, Texp}
4: σTCI_ISNi ← Sign(SKTCI , VCISNi
)
5: VCISNi ← VCISNi
∥σTCI_ISNi
6: Store VCISNi
in secure memory of ISNi
7: end for
Phase 2: VC Issuance for RUi
8: for each RUi ∈ RU do
9: Define permissions PermRUi
10: VCRUi ← {DIDRUi
, PermRUiTexp}
11: σTCI_RUi ← Sign(SKTCI , VCRUi
)
12: VCRUi ← VCRUi
∥σTCI_RUi
13: Store VCRUi
in secure wallet of RUi
14: end for
where metaISNi
includes metadata about the ISN i and Texp
denotes the expiration time.
T CI configures the system to automatically sign each
VC with its private key. This embeds cryptographic proof of
authenticity and integrity. It digitally signs VCISNi
using its
secret key SKTCI to produce a signature σTCI_ISNi
that can
later be used for verification independent of any involvement
from T CI. This process involves retrieving T CI’s public
key from its DID document DID_DOCTCI and verifying
σTCI_ISNi
.
σTCI_ISNi = Sign(SKTCI , VCISNi
) (3)
The signed credential is now VCISNi
∥σTCI_ISNi
.
2) STEP 2: CREDENTIAL ISSUANCE TO RUI
Similarly, for each RUi
, VCRUi
is generated by the T CI.
VCRUi
looks like:
VCRUi = DIDRUi
, permissionsRUi
(4)
T CI signs this credential, producing the signature
σTCI_RUi
:
σTCI_RUi = Sign(SKTCI , VCRUi
) (5)
This yields the signed credential VCRUi
∥σTCI_RUi
.
Each ISN i stores VCISNi
∥σTCI_ISNi
in its secure memory,
and each RUi securely stores VCRUi
∥σTCI_RUi
in their digital
wallet.
The credential issuance phase has been summarized in
Algorithm 2. This algorithm shows steps for VC generation
for ISN and RU. These VCs contain each entity’s DID,
metadata, permissions and expiration time. The respective
T CI signs the credentials to provide a cryptographic proof
of its authenticity, and securely stores it with the respective
entities.
Algorithm 3 Mutual Authentication Phase: Authentication
and Session Key Derivation
Input: ISN = {ISN1, ISN2, . . . ,ISNn}, RU =
{RU1, RU2, . . . , RUm}, VCISNi
, VCRUi
Output: Ksession
Phase 1: Authentication Request by RUi
1: for each RUi ∈ RU do
2: N1 ← Random(Zq) ▷ Generate nonce N1
3: Send {DIDRUi
,N1} to ISNi
4: end for
Phase 2: Authentication Challenge by ISNi
5: for each ISNi ∈ ISN do
6: Retrieve VCRUi
from IOTA
7: Verify σRUi
using PKRUi
8: if verification successful then
9: N2 ← Random(Zq) ▷ Generate nonce N2
10: Send {N2,Challenge} to RUi
11: end if
12: end for
Phase 3: Credential Presentation by RUi
13: for each RUi ∈ RU do
14: σRUi ← Sign(SKRUi
,{VCRUi
,N2})
15: Send {VCRUi
, σRUi
, N3} to ISNi
16: end for
Phase 4: Verification by ISNi
17: for each ISNi ∈ ISN do
18: Verify σRUi
using PKRUi
19: if verification successful then
20: σISNi ← Sign(SKISNi
,{VCISNi
,N3})
21: Send {VCISNi
, σISNi
,N4} to RUi
22: end if
23: end for
Phase 5: Session Key Generation
24: for each pair (RUi, ISNi) do
25: s ← (PKISNi
)
SKRUi mod p
26: Ksession ← H(N1∥N2∥N3∥N4∥s)
27: end for
C. MUTUAL AUTHENTICATION
The goal of this phase is to establish mutual trust between
the RUi and the ISN i by verifying their respective DIDs
(DIDRUi
, DIDISNi
) and VCs (VCRUi
, VCISNi
). We use a combination of public key cryptography, nonces for freshness,
and digital signatures to achieve this.
1) STEP 1: INITIATION OF AUTHENTICATION REQUEST
BY RUI
RUi
initiates the mutual authentication process by sending an
authentication request to the ISNi
.
The request includes the following elements:
AuthReqRUi = {DIDRUi
,N1} (6)
where N1 is a random nonce generated by RUi
to ensure the
freshness of this authentication session.
The nonce N1 ∈ Zq (where q is a large prime number) is
generated randomly:
N1 = Random(Zq) (7)
This nonce is used later in session key derivation to prevent
replay attacks.
2) STEP 2: ISNI VERIFIES RUI
’S IDENTITY
Upon receiving the authentication request AuthReqRUi
,
ISN i retrieves DIDRUi
from IOTA Tangle and obtains the
associated DID: DID_DOCRUi
.
ISN i
then sends a challenge to RUi
to verify his/her
identity:
ChallengeISNi = {N2} (8)
where N2 ∈ Zq is another random nonce generated by ISNi
:
N2 = Random(Zq) (9)
3) STEP 3: PRESENTATION OF VCS BY RUI
The RUi responds to the challenge by presenting VCRUi
signed with their private key SKRUi
.
The signed response includes both the credential and a
fresh nonce N3:
ResponseRUi = {VCRUi
, σRUi
,N3} (10)
where:
• VCRUi
contains information about RUi (DIDRUi
, permissions).
• σRUi = Sign(SKRUi
,{VCRUi
,N2}) is the digital signature of RUi
, providing proof of ownership of VCRUi
and
ensuring that the response is fresh.
• N3 is an additional nonce generated by RUi
, which will
also contribute to the session key generation.
ISN i
then verifies the RUi’s signature σRUi
using the
public key PKRUi
retrieved from DID_DOCRUi
:
Verify(PKRUi
, σRUi
,{VCRUi
,N2}) = True (11)
If the verification fails, the authentication process is terminated.
4) STEP 4: VERIFICATION OF ISNI BY RUI
To complete mutual authentication, ISNi sends VCISNi
and
a challenge message, which is signed with its private
key SKISNi
:
ChallengeRUi = {VCISNi
, σISNi
,N4} (12)
where:
• VCISNi
is the VC of ISN i
.
• σISNi = Sign(SKISNi
,{VCISNi
,N3}) provides proof of
ownership.
• N4 is a new nonce generated by ISNi
to ensure the
authenticity of the response.
RUi verifies σISNi
using ISN i’s public key PKISNi
retrieved from the its DID Document DID_DOCISN .
Verify(PKTCIi
, σISNi
,{VCISNi
,N3}) = True (13)
If successful, mutual authentication is established.
5) STEP 5: SESSION KEY GENERATION
After both parties verify each other, they derive a session key
Ksession for secure communication. This key is derived using
the nonces N1, N2, N3, and N4 and the Diffie-Hellman (DH)
keys from each entity’s public-private key pairs.
The session key Ksession is derived as follows:
Ksession = H(N1∥N2∥N3∥N4∥PKISNi
∥PKRUi
) (14)
where H is a SHA-256 hash function, which ensures that the
key derivation is secure.
For additional security, both parties compute a shared
Diffie-Hellman secret s using their private-public key pairs:
s = (PKISNi
)
SKRUi = (PKRUi
)
SKISNi (15)
The session key Ksession can be further strengthened by
incorporating s:
Ksession = H(N1∥N2∥N3∥N4∥s) (16)
Algorithm 3 summarizes the mutual authentication phase.
This algorithm allows ISN i and RUi
to authenticate each
other using their VCs. Through a series of nonce exchanges,
digital signatures, and verification steps, both entities confirm
each other’s identities. Upon successful authentication, a session key Ksession is derived from the exchanged nonces and
a Diffie-Hellman shared secret, providing secure, sessionbased communication.
D. SECURE DATA SHARING
With Ksession securely established, ISN i encrypts data D for
secure transmission to RUi
.
The data D to be sent by ISN i
is first converted
into a message M, which includes necessary metadata,
including timestamp T , identifier IDD, and the intended
recipient’s DID:
M = {D, T , IDD, DIDRUi
} (17)
1) STEP 1: DATA ENCRYPTION
ISN i encrypts M using a symmetric encryption scheme,
using AES in GCM mode, with Ksession as the encryption key:
Ciphertext = EncKsession (M) (18)
where EncKsession (·) denotes encryption using Ksession.
The resulting ciphertext is transmitted to RUi
. Upon
receiving it, RUi decrypts the message using the session key:
M = DecKsession (Ciphertext) (19)
where DecKsession (·) denotes decryption using Ksession.
Algorithm 4 Secure Data Sharing Phase: Encrypted Data
Transmission and Verification
Input: Ksession, Data D, RUi
, ISNi
Output: Encrypted and authenticated data transmission
between RUi and ISNi
Phase 1: Data Preparation and Encryption
1: T ← Timestamp()
2: M ← {D, T , IDD, DIDRUi
} ▷ Prepare message with
data, timestamp, and metadata
3: Ciphertext ← EncKsession (M) ▷ Encrypt message with
Ksession
4: Send Ciphertext to RUi
Phase 2: Data Integrity and Non-Repudiation
5: hD ← H(D) ▷ Compute hash of data D
6: σD ← Sign(SKISNi
, hD) ▷ Sign hash hD with SKISNi
7: Send Ciphertext∥σD to RUi
Phase 3: Verification by RUi
8: M ← DecKsession (Ciphertext) ▷ Decrypt ciphertext with
Ksession
9: h
′
D ← H(D) ▷ Recompute hash of received data D
10: Verify σD using PKISNi
: Verify(PKISNi
, σD, h
′
D
)
Phase 4: Selective Disclosure
11: Mreq ← {IDD,{L, V}} ▷ RUi requests specific fields
(e.g., location L, sensor value V)
12: Msel ← {L, V} ▷ ISNi prepares minimal disclosure
message
13: σsel ← Sign(SKISNi
, H(Msel))
14: Ciphertextsel ← EncKsession (Msel∥σsel)
15: Send Ciphertextsel to RUi
16: Msel ← DecKsession (Ciphertextsel)
17: Verify(PKISNi
, σsel, H(Msel))
To ensure that data is received as intended and has not been
tampered with during transmission, ISN i signs the data to
provide integrity and non-repudiation guarantees.
Before sending, ISN i computes a hash of the data D using
the secure hash function H:
hD = H(D) (20)
ISN i
then creates a digital signature σD by signing hD
with its private key SKISNi
:
σD = Sign(SKISNi
, hD) (21)
The signature σD is appended to the encrypted message
before transmission as (Ciphertext∥σD).
2) STEP 2: DATA DECRYPTION
Upon receiving Ciphertext∥σD, RUi verifies the integrity by
checking the signature using ISN i’s public key PKISNi
:
Verify(PKISNi
, σD, hD) = True (22)
where hD is recalculated by RUi from the decrypted data D
to confirm that the data has not been altered.
3) SELECTIVE DISCLOSURE
Selective disclosure allows RUi
to request specific parts of
ISN i’s data while minimizing unnecessary data exposure,
thereby preserving privacy.
RUi
initiates a selective request for specific attributes of
data D, such as location L or sensor value V, by constructing
a request message Mreq:
Mreq = {IDD,{L, V}} (23)
Upon receiving Mreq, ISN i prepares a minimal disclosure
message Msel that contains only the requested fields:
Msel = {L, V} (24)
ISN i signs Msel to ensure that the disclosed data is
verifiable:
σsel = Sign(SKISNi
, H(Msel)) (25)
ISNi
then encrypts Msel∥σsel using Ksession and transmits it
to RUi
:
Ciphertextsel = EncKsession (Msel∥σsel) (26)
After receipt, RUi decrypts and verifies the integrity of
Msel by checking σsel against PKISNi
:
Verify(PKISNi
, σsel, H(Msel)) = True (27)
This cryptographic framework ensures that all communications in the SSI-based IoT environment are secure,
authenticated, and privacy-preserving.
The Secure Data Sharing algorithm (Algorithm 4) enables
encrypted data exchange between RUi and ISN i
. The data
D is encrypted with the session key Ksession to maintain
confidentiality. A digital signature is appended to ensure
data integrity and non-repudiation. Additionally, selective
disclosure allows RUi
to request specific data fields, ensuring
privacy-preserving communication.
E. FORMAL SECURITY ANALYSIS
To rigorously evaluate ISIF’s security, we use formal methods
like BAN logic [32] to demonstrate that essential security
properties are met, including mutual authentication, data
integrity, and confidentiality.
1) AUTHENTICATION VERIFICATION USING BAN LOGIC
Using BAN logic, we show that RUi and ISN i can verify
each other’s identities. For example:
• RUi believes ISN i possesses Ksession.
• ISN i believes RUi possesses Ksession.
Upon exchanging nonces N1, N2, N3, and N4 and
deriving Ksession:
• RUi concludes ISNi has authenticated identity through
VCISNi
and
• ISNi concludes RUi has authenticated identity through
VCRUi
confirming mutual authentication.
2) SESSION KEY CONFIDENTIALITY
The confidentiality of Ksession is ensured by the DiffieHellman exchange, where s = (PKISNi
)
SKRUi mod p
guarantees that:
Ksession = H(N1∥N2∥N3∥N4∥s) (28)
without access to SKISNi
and SKRUi
, an attacker cannot
derive Ksession.
3) RESISTANCE TO KNOWN ATTACKS
Through formal analysis, the protocol resists impersonation,
interception, and forgery:
• Impersonation Resistance: An attacker cannot impersonate entities without access to their private keys,
as each interaction relies on valid cryptographic signatures.
• Message Integrity: Data integrity is ensured by hD and
σD, where altered data would produce invalid σD.
4) ACHIEVED SECURITY GOALS
The analysis confirms that the following goals are met:
• Goal 1: RUi and ISN i share a session key Ksession
known only to them.
• Goal 2: Both entities verify the session’s freshness,
ensuring that Ksession is unique to each session, mitigating replay attacks.
• Goal 3: Selective disclosure supports privacy, revealing
only required information and preserving unlinkability.
IV. RESULTS AND DISCUSSIONS
In this section, we analyze the performance of ISIF within
IoT. The simulations have been carried out in NS31 on an
Ubuntu platform. The subsequent subsection describes the
simulation setup and parameters.
A. SIMULATION SETUP
ISIF has been evaluated using comprehensive simulations
in NS3. The simulations have been configured to emulate
IoT network with a set of sensors and users. The simulation
parameters have been chosen carefully to mimic real-world
IoT systems to effectively evaluate ISIF. Table 3 shows the
detailed overview of the simulation parameters.
B. DID GENERATION AND VERIFICATION COST
Figure 2 shows the time taken by ISIF to generate and
verify DIDs. This cost has been measured against different
network sizes. The computational cost of DID generation
and verification is directly influenced by the scale of the
network, as depicted by the relationship between network size
(x-axis) and computational time (y-axis). Larger networks
require generating more DIDs, which places greater demands
on computational resources. This increase in computational
overhead is evident in Figure 2, where the time taken grows
consistently with the network size.
1https://www.nsnam.org
TABLE 3. Simulation parameters.
FIGURE 2. DID generation and verification cost against the network size.
As the number of entities in the network rises, each entity’s
DID generation process involves cryptographic operations
that cumulatively increase the total computational time.
Thus, larger networks face higher costs, reflecting the need
for additional processing to handle a greater volume of
unique identifiers. These results underline the scalability
requirements of DID generation and verification in IoT
environments, as efficient DID generation and verification is
crucial for maintaining the responsiveness of the system in
expanding IoT networks.
DID verification is a crucial step in ensuring the authenticity and integrity of DIDs. When an entity receives a DID,
it must verify its validity by retrieving the corresponding DID
Document from the IOTA Tangle. The verification process
involves the following steps:
TABLE 4. DID Generation Time Across Different Network Sizes
for 1000 Iterations.
TABLE 5. VC Issuance Time for Different Network Sizes
for 1000 Iterations.
• DID Document Retrieval: Using the DID as a unique
reference, the verifier queries the IOTA Tangle to obtain
the associated DID Document.
• Signature Verification: The verifier checks the digital
signature within the DID Document using the issuer’s
public key. This ensures the document has not been
tampered with and confirms its authenticity.
• Data Integrity Check: The retrieved DID Document’s
hash is compared with the expected hash stored on the
Tangle, guaranteeing the document’s integrity.
Table 4 presents the DID generation time for different
network sizes, measured over 1000 iterations. For a small
network of 50 nodes, the average DID generation time is
1.84 ms, with a minimum of 1.56 ms and a maximum of
5.17 ms. As the network grows to 250 nodes, the average
time increases to 10.13 ms, with a minimum of 7.79 ms and
a peak of 23.01 ms. The variation between the minimum
and maximum values is attributed to fluctuations in network
conditions and system load. These results indicate that as
the number of nodes increases, the average, minimum, and
maximum DID generation times also rise due to higher
computational and communication overhead.
To evaluate the efficiency of our verification process,
we measure the verification time for different network sizes.
As shown in our results, the verification time remains low
even as the number of nodes increases. Specifically, for a
network with 50 nodes, the DID verification time is 0.17 ms,
and for a network with 250 nodes, the DID verification time
is 1.79 ms. These results demonstrate the scalability of the
proposed scheme, making it well-suited for large-scale IoT
environments.
C. VC ISSUANCE COST
Table 5 presents the time required to generate VCs in
a network of varying sizes. The average generation time
increases with the number of nodes, showing a rise from
2.65 ms (50 nodes) to 20.56 ms (250 nodes). The minimum
time required follows a similar trend but fluctuates slightly at
200 nodes, where it drops to 6.84 ms before increasing again.
The maximum time shows more variation, with significant
spikes at 150 nodes (49.25 ms) and 200 nodes (639.35 ms).
This suggests that at higher node counts, sporadic delays
TABLE 6. VC Verification Time for Different Network Sizes
for 1000 Iterations.
may occur due to factors such as congestion or cryptographic
overhead.
The observed results indicate that the time required for
VC generation remains within a feasible range even after
a significant growth in the network size. For instance,
as the network scales from 50 to 250 nodes, the VC
issuance time gradually increases from 2.648 milliseconds
to 20.564 milliseconds. This trend is largely attributed to the
increased number of cryptographic operations necessary to
securely generate VCs as the number of nodes grows. Each
VC issuance includes a series of cryptographic calculations
to ensure that each credential is valid and secure, and the
cumulative processing time increases proportionally to the
number of nodes.
The relationship between network size and VC issuance
time is therefore relatively linear. Each increase in node count
produces a slight rise in processing time due to the additional
payload size and the cryptographic requirements. Notably,
the generation times remain within acceptable parameters,
which demonstrates that the framework is capable of scaling
to larger network sizes without significant delays.
D. VC VERIFICATION COST
Table 6 illustrates the time taken to verify VCs across
different network sizes. The average verification time starts
at 3.53 ms (50 nodes) and increases steadily to 22.43 ms
(250 nodes). The minimum verification time follows a
consistent pattern, starting at 3.10 ms (50 nodes) and
increasing to 17.43 ms (250 nodes). The maximum time
fluctuates significantly, with a peak at 150 nodes (55.00 ms),
but drops at 200 nodes before rising again at 250 nodes.
These variations indicate that while VC verification scales
predictably on average, peak delays may occur due to
network load or cryptographic operations.
Similar to VC generation, the time required for VC
verification shows a gradual rise, ranging from 3.534 milliseconds to 22.431 milliseconds, but remains within a range
that does not impede network performance or scalability.
This is because an increased network size requires more
cryptographic operations, including signature verification
and integrity checks. With growing number of nodes, the
system handles additional public key lookups and cryptographic operations, which contribute to a gradual increase
in verification time. However, since these operations remain
computationally efficient, the increase does not significantly
impact performance or scalability.
These results support the feasibility of the framework in
handling large-scale IoT environments while maintaining
efficient and reliable VC issuance and verification processes.
FIGURE 3. The cost of attaching and retrieving blocks on IOTA Tangle.
E. IOTA BLOCK GENERATION AND RETRIEVAL COST
Figure 3 presents an analysis of the time required to anchor
cryptographic proofs of VCs to the IOTA Tangle, as well
as the cost of retrieving these cryptographic proofs from
the Tangle. This evaluation examines how varying payload
sizes impact the time taken for block generation and retrieval,
crucial factors in assessing the efficiency of ISIF.
In the experiment, block generation times exhibit stability
across most payload sizes. This indicates that the process is
generally unaffected by moderate increases in data volume.
Specifically, for payload sizes up to 8KB, block generation
time remains largely constant. This suggests that IOTA’s protocol can handle moderate payloads without significant delay.
However, when the payload size is increased from 8KB to
10KB, a noticeable but modest rise in block generation time is
observed. This increase reflects the additional computational
and data-handling demands placed on the IOTA Tangle as
payloads grow larger. Despite this rise, the overall block
generation times are well within acceptable performance
limits, even at higher payload sizes. This consistency across
varied payloads demonstrates that the IOTA Tangle remains a
feasible option for applications requiring frequent attachment
of VCs and DIDs in IoT environments, where scalability and
low-latency are essential.
Furthermore, the retrieval time of blocks from the IOTA
Tangle is analyzed as a separate metric to evaluate how
quickly stored VCs and DIDs can be accessed when needed.
Similar to block generation, retrieval times were tested
against different payload sizes to determine the efficiency of
data access in larger networks. The block retrieval time is
largely influenced by the following key factors:
1) Network Congestion: Increased network activity
leads to longer retrieval times due to higher competition
for tip selection and transaction confirmation.
2) Tip Selection Algorithm: The Monte Carlo Markov
Chain (MCMC) algorithm used in IOTA affects
retrieval efficiency, as transactions referencing unconfirmed tips experience slight delays [33].
Despite these factors, retrieval times remain efficient across
payloads, ensuring timely access to identity data even as data
volumes increase. This aspect of performance is vital for
applications where real-time access to identity and credential
data is necessary, as in secure IoT and identity management
systems.
F. COMPARISON WITH STATE-OF-THE-ART
1) COMPUTATION COST COMPARISON
Table 7 provides a comparative analysis of various state-ofthe-art schemes in terms of computational overhead across
different ends. Each scheme’s computation time is broken
down based on the cryptographic primitives used, such as
SHA hash functions, ECC operations, and fuzzy extractors,
with total time calculations shown for comparison. The time
taken by each cryptographic operation is given below [21].
• Hash function TSHA: 0.311 ms
• ECC point multiplication (TECC): 4.12 ms
• ECC point addition (TECA): 0.273 ms
• AEGIS (TAE): 0.3363 ms
• Symmetric encryption (TECN ): 0.413 ms
• Physical unclonable function (TPU ): 0.51 µ
• Fuzzy extractors (TB): 4.12 ms
The table reveals that schemes vary significantly in their
total computation costs:
• Low-Overhead Schemes: [21] demonstrates a relatively low computation cost of 8.942 ms, benefiting
from fewer cryptographic operations, i.e. only 5 SHA
and 9 AEGIS operations.
• Moderate-Overhead Schemes: Schemes such as [34]
and [35] have computation costs of 23.546 ms and
17.885 ms, respectively, with higher costs primarily due
to additional encryption and fuzzy extraction operations.
• High-Overhead Schemes: At the upper end, schemes
like [36] and [37] incur substantial computational costs,
reaching 64.369 ms and 68.178 ms, respectively, due
to the extensive use of ECC operations and fuzzy
extractors.
Table 7 shows that the computation cost of ISIF is
significantly lower than [34], [36], [39], and [41]. However,
this cost is slightly higher than [21], [38], and [40], which
can be attributed to the fact that generation of VCs, DIDs and
DID documents requires additional cryptographic operations,
including generation of keys and digital signatures, and hash
functions.
2) COMMUNICATION COST COMPARISON
We compare ISIF with a number of schemes proposed in
the recent literature in terms of communication cost in
Table 8. In this table, the number of bits represents the bits
transferred from one entity to another during initialization,
credential issuance, mutual authentication and data sharing.
Lower communication overhead indicates higher efficiency,
especially for resource-constrained IoT environments.
TABLE 7. Comparison of ISIF with state-of-the-art in terms of computation overhead [19], [21].
TABLE 8. Comparison of ISIF with state-of-the-art in terms of
communication overhead.
During the initialization phase, ISIF uses lightweight
cryptographic operations, namely hashing and ECC, which
require fewer bits compared to traditional approaches like
RSA. A single message or public key exchange results in
256 bits of data being transferred. This value aligns with
standard ECC key sizes for 128-bit security.
The credential issuance phase involves transferring more
data due to the inclusion of digital signatures, credential
details, and metadata necessary for secure authentication.
Using ECC-based signatures, this phase transfers 512 bits of
data, which corresponds to the size of two elliptic curve points
for secure validation.
For mutual authentication and data sharing, ISIF uses
an optimized design with minimal data exchange, relying
again on ECC or symmetric cryptography. This involves the
exchange of a secure token, challenge-response data and a
hashed message. This results in a data transfer of 256 bits.
The analysis and comparison of ISIF with state-of-theart schemes highlight its superior efficiency in terms of
communication cost. The total communication overhead of
1024 bits for ISIF demonstrates a significant reduction
compared to existing schemes, such as [36] (3200 bits)
and [37] (3360 bits). The low communication overhead
makes ISIF particularly suitable for resource-constrained
IoT environments, where minimizing communication cost
is critical for preserving bandwidth, energy, and processing
power. Moreover, this reduction does not compromise
security, as ISIF retains robust security properties like mutual
authentication, data integrity, and confidentiality, as given
under Section IV-G.
G. INFORMAL SECURITY ANALYSIS
In the informal analysis, we examine the ISIF’s resilience
against common IoT security threats, including replay attack,
man-in-the-middle attacks, attacks against confidentiality.
The security features including anonymity and unlinkablity
and decentralization are also analyzed under this section.
1) RESISTANCE AGAINST REPLAY ATTACKS
To prevent replay attacks, each communication session
involves unique nonces. When RUi
initiates an authentication session with ISN i
, it generates a random nonce N1 ∈ Zq
and sends it to ISN i
. Similarly, ISN i generates its own
nonce N2.
The uniqueness of N1 and N2 ensures that each session key
Ksession is unique to the session:
Ksession = H(N1∥N2∥N3∥N4∥s) (29)
where s = (PKISNi
)
SKRUi mod p. This prevents replay
attacks as any reuse of messages would produce invalid
nonces.
2) RESISTANCE AGAINST MAN-IN-THE-MIDDLE ATTACKS
Mutual authentication between RUi and ISN i relies
on cryptographic signatures. Each entity verifies the
other’s identity through VCs. For instance, ISN i verifies
σTCI_RUi = Sign(SKRUi
, VCRUi
) using PKTCIi
.
Verification implies:
Verify(PKTCIi
, σTCI_RUi
, VCRUi
) = True (30)
ensuring any altered message results in failed verification,
protecting against Man-in-the-Middle (MitM) attacks.
3) DATA INTEGRITY AND CONFIDENTIALITY
The session key Ksession is used to encrypt data D between
ISN i and RUi
:
Ciphertext = EncKsession (D) (31)
A hash hD = H(D) is also computed and signed by ISN i
to
produce σD = Sign(SKISNi
, hD). Integrity is verified as:
Verify(PKISNi
, σD, hD) = True (32)
where any modification of D by an attacker invalidates σD.
4) PSEUDONYMOUS IDENTITY GENERATION
Pseudonymity ensures that an entity can interact within
a system without revealing its true identity, while still
maintaining accountability using a pseudonymous identifier.
In ISIF, pseudonymity is achieved using DIDs, VCs, and
cryptographic signatures.
Each entity RUi and ISN i generates a public-private key
pair, (SKRUi
, PKRUi
) and (SKISNi
, PKISNi
).
A pseudonymous identity is established by binding the
public key to the DID:
DIDRUi = H(PKRUi
∥Meta)
Where:
• H = Cryptographic hash function
• Meta = Metadata related to the entity
Since hashing is a one-way function, reversing H to
retrieve PKRUi without knowledge of its input is computationally infeasible.
5) DECENTRALIZATION AND ELIMINATION OF SINGLE
POINTS OF FAILURE
The IOTA Tangle ledger eliminates single points of failure,
decentralizing DID and VC management. By storing these
elements on the Tangle, the system’s trust model remains
unaffected even if a single node is compromised.
V. CONCLUSION
The rapid expansion of the Internet of Things (IoT) has introduced significant challenges in ensuring secure, efficient,
and scalable communication between interconnected devices.
This paper presents ISIF, a novel framework designed
to address these challenges by leveraging SSI principles,
DIDs, and VCs. ISIF employs lightweight cryptographic
operations, including ECC and efficient hashing mechanisms,
to provide robust security while minimizing computational
and communication overhead. ISIF’s methodology comprises
four key phases: initialization, credential issuance, mutual
authentication, and secure data sharing. Each phase has
been carefully designed to balance security and performance,
ensuring that the framework meets the stringent requirements
of resource-constrained IoT environments. The integration
of the IOTA Tangle as a distributed ledger enhances
decentralization, eliminates single points of failure, and supports tamper-resistant identity management. Comprehensive
performance evaluations demonstrate that ISIF significantly
outperforms existing state-of-the-art schemes in both computation and communication efficiency. ISIF reduces resource
consumption while maintaining strong security guarantees,
such as resistance to replay attacks, man-in-the-middle
attacks, and data tampering. These results underscore ISIF’s
suitability for large-scale IoT networks requiring lightweight
and secure identity management solutions.
Future work will focus on enhancing ISIF by incorporating
quantitative trust evaluation mechanisms for each entity in
the IoT ecosystem. This will involve assigning dynamic trust
scores to IoT devices based on their past behavior, interaction
patterns, and compliance with security policies. Such trust
evaluation will further strengthen ISIF’s ability to support
secure and reliable IoT networks by enabling fine-grained
trust management and adaptive decision-making.
