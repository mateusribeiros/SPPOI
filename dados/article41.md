Title: BlockMEDC: Blockchain Smart Contracts System for Securing Moroccan Higher Education Digital Certificates

ABSTRACT Morocco’s Vision 2030, known as Maroc Digital 2030, aims to position the kingdom as a
regional leader in digital technology by boosting digital infrastructure, fostering innovation, and advancing
digital skills. Complementing this initiative, the Pacte ESRI 2030 strategy, launched in 2023, seeks to
transform the higher education, research, and innovation sectors by integrating state-of-the-art digital
technologies. In alignment with these national strategies, this paper introduces BlockMEDC, a blockchainbased system for securing and managing Moroccan educational digital certificates. Leveraging Ethereum
Layer 2 (zk-Rollups) smart contracts and the InterPlanetary File System, BlockMEDC automates the
issuance, management, and verification of academic credentials across Moroccan universities. The proposed
system addresses key issues such as document authenticity, manual verification, and lack of interoperability,
delivering a secure, transparent, and significantly low-cost solution that aligns with Morocco’s digital
transformation goals for the education sector.
INDEX TERMS Blockchain (BC), digital certificate, digital signature, higher education, Ethereum zkRollups, InterPlanetary file system (IPFS), smart contracts (SCs).
I. INTRODUCTION
Morocco’s Digital 2030 (MD2030) Vision aims to harness
global digital advancements to transform the kingdom into
a prominent producer of digital solutions and a regional
leader in technology and innovation. Officially launched
on September 25, 2024 [1], the National Strategy Digital
Morocco 2030 outlines a strategic initiative focused on
advancing digital infrastructure by digitizing public services,
supporting and enhancing start-ups, developing digital skills,
providing high-quality internet coverage across Morocco,
emphasizing computing and artificial intelligence, and promoting international collaboration [2].
In alignment with the MD2030 Vision, Morocco’s Pacte
ESRI 2030, launched in 2023, aims to modernize higher
education, research, and innovation sectors by integrating
advanced digital technologies and innovative practices to better align with global advancements and address contemporary
challenges and pandemics (e.g., COVID-19) [3], [4].
Recently, e-learning platforms have become pivotal in
Moroccan higher education, complementing face-to-face
teaching with advanced digital tools, e.g., Moodle and
Rosetta Stone [5], [6], [7]. Moodle provides tools for
course creation, assignment management, and communication between students and instructors. Rosetta Stone is used
primarily for foreign language learning, which helps learners
develop their skills through interactive lessons and exercises.
As digital technologies continue to evolve, several Moroccan universities are transitioning to digital certifications,
including Mohammed First University of Oujda, Mohammed
V University of Rabat, Sultan Moulay Slimane University of
Beni Mellal, and Ibn Zohr University of Agadir. These certifications ensure document validity through digital signatures
and can be easily accessed, shared, and verified online [8].
A. OVERVIEW OF DIGITAL CERTIFICATES
Moroccan universities’ adoption of digital certificates (e.g.,
registration certificates, official academic transcripts, and
diplomas) aims to modernize and streamline the process
of obtaining and verifying academic certificates. In what
follows, we overview the current state of Moroccan higher
education’s digital certificate system. Firstly, we outline the
procedures for requesting and issuing digital certificates.
Next, we highlight the digital signature process. Finally,
we discuss the digital certificate system’s benefits and issues.
1) PROCESS OF REQUESTING AND ISSUING
Figure 1 illustrates the stages involved in processing digital
certificate requests in the current Moroccan system, from
submitting a request to reviewing the document.
FIGURE 1. Stages involved in the issuance of digital certificates in the
current Moroccan system.
1. Submitting a request: A student can use their platform
account to request a document, except for the diploma,
which is issued automatically upon validation for all
semesters.
2. Previewing the request: The administrator of digital
certificates inspects the received request.
3. Sending a document: The administrator sends the
required document for signing.
4. Signing the document: Before signing the documents,
an administrator or vice-head verifies the students’
grades. The authorized signatory (e.g., the university
president and/or dean) receives the document electronically and applies their digital signature. This electronic
signature is typically appended to the end of the
document, as illustrated in Figure 2.
5. Delivering the document: The student receives the
stamped document through their account on the platform.
6. Reviewing the document: Signed documents are stored
on the university’s central servers, while the signatures
are stored at Barid eSign. Anyone can verify the authenticity of the document issuance using a special link and
verification code (e.g., link: https://esign.ump.ac.ma
and code: J1mRR5i4, see Figure 2).
FIGURE 2. A diploma electronically signed by the president and the dean
in the current Moroccan system.
2) DIGITAL SIGNATURE
Digital signatures are a crucial element in ensuring the
authenticity and integrity of digital certificates [52], [53].
They rely on cryptographic algorithms, specifically using a
pair of keys:
• Private Key: Kept confidential by the signer (e.g.,
university president).
• Public Key: Made available for verification purposes.
Morocco’s Law n◦ 43-20 (Dahir n◦ 1-20-100 of December
31, 2020) mandates the use of confidence services, including
digital signatures, to secure digital transactions [9]. Barid
eSign [10], the sole state-approved certification authority
(CA), provides essential services such as digital signatures,
strong authentication, timestamps, and SSL certificates to
ensure the integrity and trustworthiness of digital communications in Morocco.
Each signer receives a SecurID key from Barid eSign,
which contains certified keys. The signing process is as
follows:
1) Authorized signers (e.g., presidents, deans, and directors) use their RSA-2048 [11] private keys, which are
stored securely in a SecurID key and accessed with a
PIN, to create a digital signature.
2) The signature incorporates both the SHA-256 and
SHA-512 hash algorithms v [12], [13] to ensure data
integrity, offering enhanced security against collision
vulnerabilities.
3) This digital signature is embedded into the digital
certificate.
The missing link in current Moroccan digital certificates
is the secure verification process, which depends on the
following:
1) Entering the certificate’s reference number on the
institution’s e-sign platform to initiate verification.
2) Contacting Barid eSign to confirm the signer’s identity
details (name, public key, hash function).
3) Utilizing the provided public key and hash function
to independently verify the integrity of the signed
certificate.
3) BENEFITS
Digital certificates offer a range of benefits to both individuals and organizations in the Moroccan higher education
sector, including:
• Accelerated processes: By automating many administrative tasks, the digital certificate system enables educational institutions to issue certificates more quickly than
traditional paper-based systems. These tasks include
submitting online requests, verifying student requests,
digitally signing certificates, and delivering the certificates electronically.
• Reduced costs: Using digital certificates can significantly reduce costs for both students and educational
institutions in terms of time and money, as they eliminate
the need for printing (except diplomas), in-person
delivery, and physical storage of paper certificates.
Furthermore, students will no longer need to cast
certified copies of the original certificates because the
current system has set up an online central server to
verify certificate authenticity.
• Environmentally friendly: Digital certificates help promote sustainable practices by reducing the use of paper,
ink, energy, and transportation.
4) ISSUES
Despite the many advantages that digital certificates offer
over their paper-based counterparts, there are still a number
of security and efficiency-related issues that require attention,
including:
• Security threats: Both digital and traditional certificate systems are susceptible to forgery because the
administrators have access to all student grades and
can potentially manipulate them. Once the grades are
submitted to the administrator, it becomes challenging
for the professors to monitor the integrity of the grades.
On the other hand, the central server, which stores
all signed documents, is vulnerable to various attacks,
including denial-of-service attacks and ethical breaches.
• Hand-to-hand distribution: It requires students to physically visit the institution to obtain a printed and stamped
copy of their digital diplomas. This process is costly for
both students and the diploma desk, as it consumes a
significant amount of time and resources, resulting in a
lengthy and inefficient distribution process.
• Manual verification: This is an issue with the current
digital certificate system. Verifying the authenticity of a
digital certificate requires downloading it from a central
server using a special link and verification code. This
manual process can be time-consuming and prone to
errors.
• Semi-automated: The current digital certificate system
does not fully automate the issuance process. Students
must request the required documents (except diplomas),
and administrators must review any received requests.
• Not instantaneous: The issuance of official academic
transcripts and diplomas is not an instantaneous process;
it can take more than a month after the announcement of
regular session results.
• Non-uniform profile: The current Moroccan digital certificate system lacks consistency in creating academic
accounts for students, as each university generates
accounts independently. This can lead to students having
multiple accounts if they receive certificates from
different universities, resulting in a fragmented and
potentially confusing digital profile.
B. RESEARCH MOTIVATION
The urgent need to improve the security, efficiency, and
interoperability of the current digital certificate system in
Moroccan higher education, while aligning with MD2030
Vision and Pacte ESRI 2030 objectives, motivates this
research. The integration of blockchain smart contracts [14],
[15], [16], [17], [18], [19], [20], [21], [22], [23], [24], [25]
offers a decentralized, secure, and tamper-proof framework
that has the potential to revolutionize the educational digital
certificate system, enhancing several key aspects:
• Security and Integrity: BC offers a robust defense
against forgery and unauthorized alterations, ensuring
that digital certificates remain secure and trustworthy.
• Transparency and Traceability: The transparent nature
of BC allows for real-time verification of certificates,
creating a clear audit trail and fostering trust among
stakeholders.
• Efficiency and Automation: SCs automate the issuance
and verification processes, reducing administrative burdens and expediting operations.
• Interoperability and Standardization: A BC-based platform enables standardized digital certificates, promoting
consistency and interoperability across different educational institutions.
• Cost Reduction and Environmental Sustainability: By
automating processes and eliminating paper-based documents, BC technology reduces costs and supports
environmentally sustainable practices for educational
institutions, students, and professors.
C. MAIN CONTRIBUTIONS
This research, for the first time, proposes a system based on
Ethereum SCs designed for securing and managing digital
education certificates within the Moroccan context. This
novel system, referred to as BlockMEDC, presents several
original contributions, outlined below:
• Remote Deliberation: BlockMEDC facilitates the
remote deliberation of student grades across both regular
and catch-up exam sessions, leveraging a decentralized
Ethereum network. By transcending geographical
constraints, this approach enhances the efficiency and
accessibility of the certification process.
• Automation and Real-Time Issuance: BlockMEDC uses
Ethereum zk-Rollups SCs to automate digital certificate
issuance and management. Once the conditions for
their issuance are met, all documents—such as reg
istration certificates, official academic transcripts, and
diplomas—are generated and issued automatically and
in real time.
• Issuing Digital Certificates for Professors: It is a feature
of BlockMEDC that extends the platform’s functionality to include the secure issuance, management, and
verification of digital certificates for professors, such
as university qualifications and teaching credentials.
This approach simplifies the verification process for
employment, promotions, and academic collaborations,
empowering professors to manage and share their
credentials easily.
• Ensuring Integrity:BlockMEDC guarantees the integrity
of students’ grades, as well as both students’ and
professors’ certificates, making them resistant to
tampering and unauthorized alterations. Additionally,
the system enables professors to monitor the integrity of
students’ grades both before and after the deliberation
process.
• Standardization Across Institutions: The BlockMEDC
system introduces standardization across Moroccan educational institutions by providing each student/professor
with a single, unified academic account. This approach
eliminates account fragmentation, simplifies record
management, and enhances the integration and usability
of students’ and professors’ academic information
across different universities.
• Interoperability: BlockMEDC can efficiently interact
with different platforms, facilitating and automating
the secure verification of digital certificates across
diverse institutions. For example, to participate in the
master’s or Ph.D. entrance exam, a student can simply
provide their BlockMEDC_ID, allowing stakeholders to
securely access and verify their academic records.
• Economic and Environmental Benefits: The proposed
system promotes cost reduction and environmental
sustainability by automating certificate issuance and
verification processes, eliminating physical documentation, and reducing energy consumption.
This paper is structured as follows: Section II provides a
comprehensive review of existing blockchain-based digital
certificate systems, analyzing their features, strengths, and
limitations, with a focus on scalability, cost-efficiency,
and privacy challenges. Section III introduces the foundational concepts and technologies underlying the proposed
BlockMEDC system, including Ethereum zk-Rollups, smart
contracts, and off-chain storage using IPFS. Section IV
details the design and architecture of BlockMEDC, highlighting its components, workflow, security mechanisms,
and the integration of zk-Rollups for scalability and cost
reduction. Section V discusses the implementation setup
and results, covering the deployment environment, the
ZKsync Era test network, and a detailed evaluation of the
system’s performance, including transaction cost analysis
and scalability metrics. Finally, Section VI concludes the
paper, summarizing the contributions and outlining future
directions for extending system functionality and improving
interoperability.
II. RELATED WORK
Recent years have seen the proposal and development of
several BC-based certificate platforms and systems, such as
those at the University of Nicosia [26], MIT [27], [28], and
Open University [29]. These platforms and systems leverage
the security and transparency of the BC technology to address
the challenges faced by traditional and digital certificate
systems, such as fraud, forgery, and inefficiency. This section
reviews the existing literature and related work on BC-based
digital certificate systems for education, highlighting their
strengths and weaknesses.
In [30], the authors proposed a novel BC-based education records verification solution aimed at enhancing the
efficiency and security of managing educational credentials. By utilizing a decentralized architecture, the system
allows individuals to control their educational data while
facilitating seamless sharing among authorized institutions,
thereby eliminating the need for intermediaries and reducing
verification costs. The proposed solution incorporates a
consensus algorithm to ensure the validity of transactions,
enabling secure access to records through individual private
keys.
The authors of [31] proposed a BC-based system using
Ethereum and Solidity to securely manage academic records
and automate the issuance of degree certificates in Brazil.
The system employs three SCs—authority, curriculum,
and diploma—to prevent fraud and inefficiencies, ensuring
that only authorized institutions can validate and issue
certificates. The study highlights the potential of BC to
improve the security and transparency of academic credential
management, address privacy concerns and costs, and offer a
model for global application.
In [32], the authors proposed a decentralized system
for managing educational certificates using the Ethereum
BC and SCs. The system securely manages certificate
issuance, verification, and revocation through SCs, ensuring transparency, tamper resistance, and decentralization.
It employs multiple specialized contracts, each responsible
for a different role in the certificate lifecycle. The integration
of cryptographic algorithms and SC logic enhances security,
eliminating reliance on third-party systems and preventing
unauthorized access. The system’s design also allows for
compatibility with existing protocols, making it flexible for
broader applications.
The authors of [33] proposed a BC-based framework
for the verification of educational certificates to address
significant security gaps in existing solutions, specifically
focusing on themes such as authentication, authorization,
confidentiality, privacy, and ownership. Through a comprehensive review of current certification solutions, they identified that many inadequately addressed these critical aspects,
leaving certificates vulnerable to fraud. By leveraging the
Hyperledger Fabric framework, the proposed system aims to
enhance the verification process.
The authors of [34] proposed a novel architecture called
HEDU-ledger, utilizing Hyperledger Fabric technology to
create a private permissioned BC network aimed at enhancing
the security and traceability of degree attestation and
verification processes in higher education. This architecture
addresses critical issues such as data tampering, forgery,
and the inefficiencies of traditional centralized systems by
providing a decentralized, immutable ledger for storing
academic credentials.
The authors of [35] proposed an implementation model
for an academic degree certification system utilizing BC
technology, specifically through the start-up BeCertify. This
model aims to address the challenges of data management and
accessibility in higher education by providing a decentralized, secure, and transparent method for issuing and verifying
academic credentials. The paper outlines the various stages of
development for the platform, including system architecture
and REST API operations, while also discussing the multisignature authorization capabilities that enhance security and
user control.
In [36], the authors proposed a BC-based certification
system for academic degrees through the start-up BeCertify,
aiming to enhance the transparency, security, and accessibility of educational records. They outlined the various stages
of development necessary for the platform, including system
architecture and REST API operations, while addressing
challenges encountered during implementation. The study
highlighted the importance of multi-signature authorization
and the decentralized nature of blockchain, which empowers
students and educational institutions to manage academic
records more effectively.
In [37], the authors proposed a comprehensive BCbased solution named Cerberus for efficient verification of
academic credentials, addressing the pervasive issue of credential fraud in higher education. By integrating seamlessly
with existing credential management ecosystems, the system
utilizes a permissioned BC maintained by accreditation
bodies and universities, allowing for real-time verification
through QR codes linked to graduates’ records.
The authors of [38] proposed a BC-based framework
for the secure and efficient verification of educational
credentials, utilizing Ethereum smart contracts and the IPFS
for decentralized data storage. This model aims to address
prevalent issues in the education sector, such as the risk
of academic fraud and the inefficiencies associated with
traditional verification processes. By implementing a method
that randomizes credential attribute values and constructs a
verification tree, the system enhances privacy and allows for
selective disclosure of information.
The authors of [39] proposed a pilot project aimed at
verifying student ID information and transcripts of records
between KU Leuven and UniversitÃ di Bologna, utilizing
the European Blockchain Services Infrastructure (EBSI) to
enhance the digital exchange of educational credentials.
This initiative is part of the Una Europa network, which
seeks to streamline and secure the verification process for
exchange students by issuing verifiable digital identities and
transcripts. Through action research, the study assessed the
institutional and technical conditions necessary for scaling
the pilot, revealing that while the EBSI framework met initial
design principles, additional capabilities are required for full
production implementation.
Table 1 provides a comparative analysis of existing
BC-based educational credential systems, highlighting their
proposed solutions, key features, strengths, weaknesses, and
the integration of SCs.
III. PROPOSED BLOCKMEDC SYSTEM
This section details the design and architecture of
BlockMEDC, a decentralized system based on Ethereum zkRollups and IPFS technologies. The following subsections
provide a comprehensive overview of the various components
and modules that constitute BlockMEDC, highlighting how
each element contributes to the system’s overall functionality
and security.
A. SYSTEM OVERVIEW
We designed the BlockMEDC system to enhance the
security, efficiency, and accessibility of digital certificate
issuance and verification within Morocco’s higher education
institutions using Ethereum zk-Rollups Layer 2 BC technology, BlockMEDC automates the management and real-time
issuance of academic digital documents, such as registration
certificates, transcripts, and diplomas. The system allows for
remote deliberation of student grades, thereby addressing
the impact of geographical constraints on the certification
process. BlockMEDC ensures the integrity of academic
records by making them resistant to tampering and unauthorized alterations. It also introduces a standardized approach
across educational institutions, providing each student with a
unified academic account to streamline record management.
Additionally, the proposed system offers interoperability with
other platforms, enabling secure verification of certificates
across diverse institutions. In the BlockMEDC system, six
key actors play essential roles in ensuring the secure and
efficient management of digital certificates, including the
Moroccan certificate authority (MCA) (e.g., Barid eSign),
president, dean/director, administrator, professor, and student, as well as an external checker responsible for verifying
that the digital certificates provided to other parties are
accurate, correct, and tamper-proof, as illustrated in Figure 3.
Table 2 outlines the roles and responsibilities of each of
BlockMEDC’s seven actors.
Once the BlockMEDC accounts for presidents,
deans/directors, and administrators are created, they can
oversee the process of issuing digital certificates. Figure 4
illustrates the process of managing professor and student
accounts, including their creation and updates by administrators at each institute. It also details the step-by-step
process of generating, approving, validating, and issuing
FIGURE 3. The key actors in the BlockMEDC system include six internal
actors (the MCA, the university president, the dean/director,
administrators, professors, and students) and one external actor (the
checker).
academic digital certificates within the BlockMEDC system;
the following steps are involved:
1) The administrator generates all necessary digital certificates, except for students’ transcripts and diplomas, after creating or updating student and professor
accounts using smart contracts. All generated certificates are pending approval.
2) Students have the option to request additional course
units or to change their academic path/major.
3) Professors who serve as department heads or master’s
program heads are responsible for validating specific
academic certifications; the validation can be done
using a smart contract.
4) Professors have the option to request extra certifications.
5) Each professor submits the grades of their students.
The system allows professors to ensure that these
grades remain immutable and protected against any
unauthorized alterations.
6) Professors participate in remote deliberation sessions
for each semester, including both regular and catchup sessions. To manage student grade deliberation,
the BlockMEDC system uses a smart contract that
identifies instances where grades necessitate redemption and alerts the concerned teachers for further
action. During a normal session, the smart contract
detects students who require additional marks to obtain
honors. In contrast, during the catch-up session, the
smart contract detects all cases where students require
additional marks to validate the semester or obtain
honors.
7) If a student successfully completes a degree, a smart
contract generates the associated transcripts and diplomas. Otherwise, the smart contract generates only the
associated transcripts. All generated certificates are
pending for approval.
8) In parallel, the administrator submits the list of students
referred to the disciplinary council, as well as the
sanctions taken against them. The penalties can include
removing some student grades and depriving students
of the opportunity to pass certain sessions.
9) Students can submit a request to the professors to
review and correct their exam papers if they believe that
an error has occurred. If the professors detect errors,
they resubmit the corrected student grades for remote
deliberation.
10) Before sending the digital certificates to the BlockMEDC
network, both the institution head and the university
president digitally sign the certificates using smart
contracts, with each signing according to their
respective responsibilities.
11) The Ethereum network validates all approved transactions to issue the certificates, with the hash of the issued
certificates being added to the Ethereum BC, while the
actual files are stored on the IPFS network.
IV. ETHEREUM-BASED SMART CONTRACTS
ARCHITECTURE
This section details the prototype implementation of our
proposed solution, which leverages the Ethereum Layer 2
blockchain platform and Solidity to create the SCs introduced
in the preceding section.
A. ETHEREUM NETWORK FOR BLOCKCHAIN
INTEGRATION
We discuss the rationale for selecting the Ethereum zkRollups network as the underlying blockchain technology
for our digital certification system and present a comparative
analysis of Ethereum against other prominent BC platforms
to highlight its suitability.
Ethereum is a decentralized, open-source BC platform
that empowers developers to create and deploy decentralized applications (dApps) and smart contracts [40], [41].
Introduced in 2015 by Vitalik Buterin, Ethereum introduced
a programmable blockchain model that goes beyond simple transactions. With its built-in programming language,
Solidity, Ethereum enables the development of self-executing
smart contracts, which automate and enforce agreements
without the need for intermediaries.
Operating on a peer-to-peer network, Ethereum guarantees
data transparency and integrity across its decentralized
ledger. Recently, Ethereum Layer 1 transitioned from the
energy-intensive Proof of Work (PoW) consensus mechanism
to a more eco-friendly and scalable Proof of Stake (PoS)
model [42]. To address scalability challenges, Ethereum
Layer 2 solutions have been developed to offload transaction
processing from the main chain while maintaining robust
security guarantees. Technologies such as zk-Rollups and
Optimistic Rollups aggregate multiple transactions into a
single batch, significantly increasing throughput and reducing gas fees [54], [55]. This evolution has further solidified
Ethereum’s position as a leading platform for a wide range
of use cases, including digital identity management, supply
chain tracking, and digital certification systems.
The InterPlanetary File System is a decentralized storage
solution designed to store and share data across a distributed
network [43], [45]. Unlike traditional centralized servers,
IPFS uses a peer-to-peer model, where data is broken into
smaller chunks, stored on multiple nodes, and linked together
through unique cryptographic hashes called Content Identifiers (CIDs) [44]. This decentralized architecture ensures data
integrity, reduces reliance on centralized storage providers,
and enables seamless access to data even if some nodes are
offline.
IPFS is particularly beneficial for blockchain applications
like Ethereum, as it allows for off-chain storage of large files
and data while only storing critical reference information
on the blockchain. This combination helps optimize storage
costs, improve performance, and enhance the scalability of
BC-based systems.
1) WHY WE CHOSE ETHEREUM LAYER 2 FOR OUR DIGITAL
CERTIFICATION SYSTEM?
After a thorough evaluation of several blockchain platforms,
we selected Ethereum as the foundation for our digital
certification system, specifically leveraging Ethereum zkRollups, due to the following key reasons:
• Decentralization and Trust: Ethereum’s decentralized
structure ensures that no single entity has control over
the entire network, which is critical for maintaining trust
and transparency in a digital certification system. This
decentralized nature eliminates the risk of tampering
and ensures that digital certificates remain authentic and
secure.
• Immutability and Security: Data recorded on the
Ethereum blockchain cannot be modified or deleted,
making it an ideal platform for storing digital certificates. This immutability guarantees the long-term
integrity and authenticity of the certificates, ensuring
they are verifiable and resistant to forgery or unauthorized alterations.
• Smart Contract Automation: Ethereum supports smart
contracts, which enable us to automate processes like
certificate issuance, validation, and revocation. This
automation reduces the need for manual intervention,
minimizes errors, and ensures that all transactions are
executed transparently and according to predefined
rules.
• Scalability: Ethereum Layer 2 solutions, particularly zkRollups, significantly enhance transaction throughput
by processing multiple transactions off-chain and submitting a single proof to the main chain. zk-Rollups
can handle 2,000–20,000 transactions per second (TPS),
a substantial improvement over Ethereum Layer 1’s 15–
30 TPS [56]. This scalability ensures that our digital
certification system can handle a high volume of certificate issuances and verifications without congestion or
delays.
• Lower Costs: Compared to Layer 1 operations on
Ethereum, leveraging zk-Rollups significantly reduces
transaction fees. Depending on the complexity of the
transaction, zk-Rollups can achieve fee reductions of up
to 100x [56]. This is because they can bundle hundreds
of transactions into a single batch, thereby minimizing
gas consumption and enhancing scalability. This cost
efficiency is critical for making our digital certification
system accessible and sustainable, especially for educational institutions with limited budgets.
• Integration with Off-Chain Solutions: Ethereum’s compatibility with off-chain storage solutions like the
IPFS allows us to store large datasets off-chain while
keeping only critical information on the blockchain.
This approach reduces the storage burden and enhances
system performance and scalability. IPFS ensures that
even the largest files, such as complete academic
transcripts, are stored securely and can be accessed
efficiently without overwhelming the blockchain.
• Robust Ecosystem and Community Support: Ethereum’s
extensive ecosystem provides a wide range of development tools, libraries, and resources, which simplifies our
development process and ensures that we build a secure
and reliable system. The active developer community
also means that we have access to ongoing support,
updates, and improvements to the platform.
• Proven Track Record: As one of the earliest blockchain
platforms to implement smart contracts, Ethereum has
a proven history of supporting complex applications.
Its maturity and stability make it a reliable choice
for deploying a digital certification system that meets
the security and transparency needs of educational
institutions.
2) COMPARATIVE ANALYSIS OF BLOCKCHAIN PLATFORMS
To substantiate our choice, we conducted a comparative
analysis of Ethereum zk-Rollups against other blockchain
platforms such as Hyperledger Fabric [46], Stellar [47], and
EOS [48]. The comparison is based on criteria essential
for digital certification systems, including consensus mechanisms, decentralization, transaction speed, cost efficiency,
data privacy, and more (see Table 3).
After evaluating the features, advantages, and suitability of
various blockchain platforms, we have chosen Ethereum as
the foundational technology for our digital certification system. Its combination of decentralization, immutability, smart
contract functionality, integration with IPFS, and a strong
developer ecosystem provides the optimal environment for
building a secure, scalable, and reliable digital certification
platform.
B. SMART CONTRACTS DESIGN
1) SMART CONTRACT AUTHORITY OF THE MOROCCAN
CERTIFICATE AUTHORITY
The smart contract MC_Authority is responsible for
managing the approval and authorization of trusted entities
(e.g., universities) to participate in the proposed network.
Figure 5 illustrates the workflow of this smart contract,
highlighting the interactions between different actors within
the Ethereum blockchain.
In Figure 5, rectangles marked with ‘‘MCA’’ in steps 1,
2, and 3 denote actions taken by the Moroccan Certificate
Authority, while ‘‘AA’’ in steps 4 and 5 represents actions that
can be performed by any actor (AA) within the blockchain
network.
The MC_Authority smart contract is initially deployed
on the Ethereum blockchain by MCA. Once deployed and
confirmed, MCA can interact with the contract using its
unique address. To register a new digital certificate, MCA
invokes the RegisterCert() function, providing the
university’s address, public key, and certificate expiration
date. This function can only be called by MCA. Additionally,
MCA can revoke certificates using the revoke() function
as needed.
Internally, the smart contract MC_Authority utilizes
the PKI_Certificate struct (see Listing 1) to maintain
information about each registered certificate. The struct
includes fields such as identity, publicKey, expiry,
revoked, and registered, which are mapped to the
respective Ethereum addresses of the entities being certified.
The contract also utilizes events to log every addition or
modification to the blockchain, providing transparency and
traceability. Listing 2 shows an example of the Certified
event log generated whenever MCA successfully registers a
new certificate. This log contains details such as the sender’s
LISTING 1. The Struct PKI_Certificate.
and recipient’s addresses and the timestamp of the event,
making it accessible for any listener applications to monitor
the status of certificates on the blockchain.
The smart contract also includes two public functions:
isCertificateValid(address university) and
Crt_revo_List(). These functions can be called by any
user on the blockchain to verify the status of registered
certificates. Specifically:
• The isCertificateValid(address university) function returns a Boolean value indicating
whether a certificate is still valid (true) or has been
expired/revoked (false).
• The Crt_revo_List() function provides an array
of Ethereum addresses corresponding to the entities
whose certificates have been revoked. This enables easy
verification and tracking of any changes to the status of
trusted entities within the network.
By utilizing these smart contract functionalities, the
MC_Authority ensures a transparent and secure environment for managing digital certificates on the Ethereum
blockchain.
2) SMART CONTRACT UNIVERSITY OF UNIVERSITIES
A university is the second SC published in our workflow.
The university constructor defines the trusted entity (e.g.,
university) as the owner of SC by using the address of the
Authority contract previously published and the address of
the trusted entity. The MCA allows each university to identify
its affiliated institutions in BC. Figure 6 shows the functions
in the SC along with the actors involved.
The digital certificate of the contract owner (university)
must be valid to execute the functions in SC. The university
contract maintains three primary mappings (see Listing 3).
The first mapping is dedicated to managing records of its
affiliated institutions, ensuring each institution is properly
registered and tracked within the system. The remaining
two mappings are specifically designed for storing academic
certificates: one mapping handles student certificates, and the
other manages professor certificates.
LISTING 3. University’s maps.
The university can invoke the AddInstitution()
function to register a new institution to the mapping. The university uses the institution’s address as well as the addresses
of the head and vice-head for inclusion in the mapping.
Additionally, the CheckInstitution() is used to verify
whether an institution has already been registered. If this is
the case, the system generates a log indicating ‘Institution
already exists.’ Administrators can be added to the system,
expanding the university’s capacity to manage academic
certifications and institutions. The AddAdmin() function
allows the university (owner) to add an administrator to the
system. The event Administrator Added is triggered upon
adding a new admin. The certificates issued within the system
can be validated through the blockchain, ensuring authenticity and preventing fraud. The Checker can invoke the
CheckCertificate() function to check the validity of
a given diploma by referencing the Certifs_Students
contract deployed for the diploma of students and the
Certifs_Profs contract deployed for the diploma of
professors. It indicates whether the diploma is valid.
3) SMART CONTRACT INSTITUTION OF UNIVERSITIES
An institution is the third SC published in our workflow. The
institution constructor defines the institution (Dean) as the
owner of SC by using the address of the university contract
previously published, the address of the institution, and the
address of the head. It provides for each institution approved
by the university to add its actors (authorized administrators,
professors, and students) and record transcripts and academic
degree certificates for its students and other certificates for its
professors. Figure 7 shows the functions in the SC along with
the actors involved.
Indeed, the contract owner requires validation from the
university to execute functions within the smart contract. The
institution contract oversees six mappings (refer to Listing 4).
The first three mappings contain records for professors,
administrators, and students. The fourth and fifth mappings
are designated for storing transcripts and diplomas. The final
mapping is for adding authorized administrators.
LISTING 4. Institution’s maps.
The Institution smart contract can invoke the
addAuthorized() function to add new authorized
administrators and use the removeAuthorized() to
remove authorized administrators. Indeed, the
AddProfessor(), AddAdmin(), and AddStudent()
functions to register new entities such as professors, admins,
and students to the mapping are facilitated through the
invocation of the AddProfessor(), AddAdmin(),
and AddStudent() functions, respectively. In addition,
to register a new transcript for a student, the institution
uses the AddTranscript() function. More precisely, this
function checks if the transcript has already been registered;
if that is the case, we get a log ‘‘Transcript already exists’’.
If not, an internal function to ‘‘SC-Institution’’ is executed
(see Listing 5), creating a new instance of SC TranscriptCert.
In fact, each degree certificate has a certain number of
semesters. For example, to get a degree certificate in General
University Studies (Associate’s Degree), students must
validate four semesters (S1, S2, S3, and S4). Therefore, the
AddDiploma() function verifies whether the student has
been granted the number of semesters (validated transcripts)
required for each degree certificate. If that is the case, an internal function to SC Institution is executed (see Listing 6),
creating a new instance of SC Certs_Students; if not,
we get a log for each degree certification; for example, for
Associate’s Degree Certification, we get the message ‘‘The
student has not validated the Diploma of General University
Studies.’’
LISTING 6. Issuance of a new instance SC academic Certs_Students.
For the professor certificate, an internal function of the SC
Institution is executed (see Listing 7), creating a new instance
of SC Certs_Profs.
LISTING 7. Issuance of a new instance SC academic Certs_Profs.
The deleberate() function allows a professor to
deliberate and update a student’s grade in a secure, transparent manner while maintaining academic integrity and
accountability.
The Checker can invoke the CheckCertificate()
function to check the validity of a given diploma by
referencing the Certifs_Students contract deployed
for the diploma of the student and the Certifs_Profs
contract deployed for the diploma of the professor. It indicates
whether the diploma is valid.
Following a successful transaction, the certificate hash
is recorded on the Ethereum network, while a pre-defined
template for a specific academic certificate is saved in the
student portfolio via the IPFS network, facilitated by the
storage smart contract.
4) SMART CONTRACT CERTIFS_STUDENTS
When a student successfully completes a degree, the
authorized university institution creates a new instance
of the SC Certifs_Students contract. This contract
takes the student’s address, the trusted entity’s address
(as issuer_president), and the institution’s address
(as issuer_dean) as inputs. The emit function in SC
Certifs_Students records the current timestamp as the
date the student completes their degree. Diploma and degree
certification data are stored in the form of the Diploma
struct, as shown in Listing 8.
LISTING 8. The struct academic diploma.
In fact, the trusted entity can call the revoke() function
in SC Certifs_Students to refuse a Diploma Instance
when we have an error in student enrollment by using a
special function, which is selfdestruct(); this function
definitively deletes an SC by clearing its code and data.
5) SMART CONTRACT TRANSCRIPTCERT
The trusted entity creates a new instance of the SCTranscriptCert contract to issue a TranscriptCert to a
student. This contract takes the student’s address and the
trusted entity’s address (as issuer_dean) as inputs. The
emit function in TranscriptCert records the current
timestamp as the date when the student receives their
transcript. Transcript data is stored in the form of the
TranscriptCert struct, as shown in Listing 9.
LISTING 9. The struct student TranscriptCer.
In fact, the trusted entity can use the same function in SC
Certifs_Students to refuse a diploma instance.
6) SMART CONTRACT CERTIFS_PROFS
The trusted entity creates a new instance of the SC
Certifs_Profs contract to issue a certificate to a
professor. This contract takes the professor’s address, the
trusted entity’s address (as issuer_president), and the
institution’s address (as issuer_dean) as inputs. The emit
function in Certifs_Profs records the current timestamp
as the date when the professor receives their certificate.
Diploma and certification data are stored in the form of the
PrDiploma structure, as presented in Listing 10.
LISTING 10. The struct professor diploma.
In fact, the trusted entity can use the same function in SC
Certifs_Students to refuse a diploma instance.
7) SMART CONTRACT STORAGE OF UNIVERSITIES
The trusted entity creates a new instance of SC Storage.
In fact, it can call the store function to upload a file to the IPFS
network and add a Content Identifier, or CID (cryptographic
hash of file), to the Ethereum network. More precisely, store
the IPFS hash in an Ethereum contract that associates the
user’s Ethereum account with the IPFS file hash. The SC
Storage uses a set of functions, which are:
• setUser(address _add): set user.
• getLastUserID (address _add): get last
file id.
• getLast (address _add): get the last stored file
of an address using the last file id.
• getAll(): get all files of the user.
Figure 8 shows the functions in the SC along with the actors
involved.
In fact, the contract storage maintains tree mappings (see
Listing 11). The first used to link an address with the stored
files; second, used to check if an address already stores some
files; third, used the address to track the number of stored
files.
LISTING 11. Storage’s maps.
V. IMPLEMENTATION RESULTS AND DISCUSSION
In this section, we elaborate on the integration of smart
contracts into our proposed system.
Figure 9 displays the account balance. Figures and graphs
offer visual insights into the test transactions and other
pertinent data.
A. IMPLEMENTATION SETUP
The implementation of the BlockMEDC system was carried
out on ZKsync the Sepolia Ethereum test network using the
Atlas ZK IDE and Solidity for smart contract development.
The setup began by configuring the MetaMask wallet and
connecting it to the ZKsync Sepolia network, where network
parameters such as the RPC URL, Chain ID, and ETH faucet
were established. This enabled seamless interaction with the
blockchain during testing and deployment.
Algorithm 1 illustrates the step-by-step procedure followed
to implement our system. This algorithm covers the entire
implementation pipeline, from initializing the MetaMask
wallet to interacting with the deployed smart contracts.
After deploying the contracts, Python (version 3.8) scripts
were used to interact with the smart contracts, enabling
operations such as certificate issuance, management, and
verification within the system. The smart contracts, including
MC_Authority, University, Institution, and Storage, were
deployed using the Atlas ZK IDE (Version 2.0.8) on the
ZKsync Sepolia network. The system leveraged Infura’s
RPC nodes to facilitate remote interactions and IPFS for
decentralized off-chain storage of academic documents,
ensuring efficient and scalable data management. MetaMask,
a trusted Ethereum wallet, was used to fund test accounts
and execute transactions on the blockchain, while the
ETH token was used to cover gas fees during contract
interactions.
Table 4 presents the details of the tools and technologies
utilized in the implementation process. This setup ensured a
secure and efficient deployment, enabling real-time testing
and validation of smart contracts within the proposed
system.
Algorithm 1 Implementation Setup for Our System
1: Initialize Metamask and Connect to ZKsync Sepolia
network
2: Set network parameters:
• Network Name: ZKsync Sepolia Testnet
• RPC URL: https://sepolia.era.zksync.dev
• Chain ID: 300
• Currency Symbol: ETH
• Explorer URL: https://sepolia.explorer.zksync.io
3: Use a faucet to fund our ZKsync Sepolia testnet account
and transfer test ETH to our MetaMask wallet.
4: Deploy Smart Contracts on the ZKsync Sepolia
Network
5: Open Atlas ZK IDE, compile Solidity smart contracts,
and deploy them to the ZKsync Sepolia network.
6: Configure smart contracts for seamless operation with
the ZKsync Sepolia network.
7: Use Python libraries to connect to the ZKsync Sepolia
network.
8: Use Python to interact with the smart contracts.
9: Run all smart contracts
10: Get data: certificates, transcripts, student diplomas,
professor diplomas.
11: Analyze results to evaluate the effectiveness of smart
contracts for securing educational digital certificates.
B. RESULTS
1) SMART CONTRACT MC_AUTHORITY OF MCA
Figure 10 presents the transaction details for deploying an
instance of the MC_Authority smart contract. It highlights
key elements, such as the transaction status, contract address,
sender address, and destination, which refers to the contract’s
constructor.
Once the smart contract is published on the Ethereum
BC, MCA can invoke the contract’s functions using the
address shown in Figure 10. Specifically, to add a digital
certificate representation to the blockchain, MCA calls the
RegisterCert() function.
To verify the authenticity of a university certificate,
the isCertificateValid() function is called. Additionally, the contract allows MCA to revoke a digital
certificate using the revoke() function. A certificate is
also automatically marked as invalid upon expiration. The
cert_revo_list() function returns a list of addresses
associated with entities whose certificates have been revoked,
ensuring transparency and traceability of the certification
status.
The breakdown of transaction fees for deploying and
interacting with the MC_Authority smart contract on the
ZKsync Era Sepolia network is detailed in Table 5. This
table provides an overview of the transaction fees for various
operations, including deploying the smart contract, registering digital certificate representations, and revoking these
representations. The deployment of the MC_Authority smart
contract incurs a cost of 0.000051408175 ETH, equivalent
to approximately 0.16 USD. In contrast, registering a digital
certificate representation is significantly less costly, requiring
0.0000070533 ETH, which corresponds to approximately
0.02 USD. Similarly, the revocation process consumes
0.0000043863 ETH, which equates to roughly 0.01 USD.
2) SMART CONTRACT UNIVERSITY OF UNIVERSITIES
Figure 11 displays the transaction details for creating an
instance of the university smart contract. It also includes
the specific transaction information for adding an affiliated
institution.
The process of adding an institution to the blockchain,
where ownership is restricted to a university approved by
the MCA, is managed through the AddInstitution()
function. The university head can also assign administrators
to the system using the addAdministrator() function.
Additionally, the issueDiploma() function allows the
university head to issue academic diplomas for students and
professors, secured with a hashed signature (barcode data) for
enhanced authenticity.
For verification purposes, the CheckInstitution()
function confirms the accreditation status of affiliated
institutions, while the validateCertStudent() and
validateCertProf() functions enable a checker to
validate academic certifications for students and professors,
respectively.
Table 6 presents the transaction fee details for deploying and interacting with the university smart contract on
the ZKsync Era Sepolia network. The table provides a
detailed overview of the cost usage for three primary
operations: deploying the smart contract, adding affiliated
institutions, and assigning administrators. Specifically, the
deployment of the university smart contract incurs a
cost of 0.00013763365 ETH, equivalent to approximately
0.42 USD. In contrast, the operation of adding an affiliated
institution is significantly less resource-intensive, requiring
only 0.000003532975 ETH, which corresponds to approximately 0.01 USD. Similarly, assigning administrators to the
system incurs a cost of 0.000002120425 ETH, or roughly
0.006 USD. The transaction links for each operation are
provided for reference and verification.
3) SMART CONTRACT INSTITUTION OF UNIVERSITIES
Figure 12 illustrates the transaction details involved in creating an instance of the Institution smart contract. Furthermore,
it presents the specific transaction information for adding
students to the system.
The institution contract offers various functions to manage
authorized entities and academic records. Key functionalities include adding and removing authorized users with
the addAuthorized() and removeAuthorized()
functions. It also facilitates the addition of professors, administrators, and students through the AddProfessor(),
AddAdmin(), and AddStudent() functions, respectively. Academic achievements, such as transcripts and
diplomas, can be recorded using functions such as
AddTranscript(), issueDiploma(), issue
Transcript(), and issueProfessorDiploma()
for issuing professor diplomas. Additionally, official documents such as doctoral diplomas can be issued through the
issueDocDiploma() function.
The Deliberate() function enables professors to
participate in grade deliberations and update student grades.
Users can interact with the contract to verify permissions and retrieve information using functions like
isStudentRegistered(), getStudentBasic
Details(), isProfessorRegistered(), get
ProfessorDetails(), isAdminRegistered(),
getAdminDetails(), and isAuthorized(). The
contract also provides methods to verify the existence of academic documents such as transcripts and
diplomas through getStudentTranscript() and
getStudentDiploma().
Table 7 illustrates the transaction fees and cost usage
associated with deploying and interacting with the institution
smart contract on the ZKsync Era Sepolia network. It provides a detailed breakdown of costs for various operations.
The deployment of the institution smart contract incurs a
cost of 0.00028218065 ETH, equivalent to approximately
0.85 USD. Other operations, such as routine interactions—
adding students, professors, administrators, and authorized personnel—demonstrate transaction fees ranging from
0.006 to 0.02 USD. Similarly, the removal of authorized
personnel incurs a fee of about 0.006 USD.
On the other hand, issuing a transcript costs 0.000002
282075 ETH, approximately 0.007 USD, while the issuance
of a diploma and transcript together requires 0.000007
824575 ETH, costing around 0.02 USD. Issuing other
certificates, such as professor diplomas, and performing
deliberation processes incur costs ranging from 0.006 to
0.008 USD.
4) SMART CONTRACT STORAGE OF DATA
Figure 13 illustrates the transaction details for creating an
instance of the Storage smart contract. It also details the
specific transaction information for storing both student and
professor data.
The storage contract provides a variety of functions for
handling academic records. These include setUser() and
updateUser(), which enable the addition and modification of user data, and store(), which facilitates the storage
of academic documents.
Additionally, users interact with the contract through
functions such as getLastUserID(), getLast(), and
getAll(), which allow retrieval of the user’s ID, the latest
file associated with the user, and all files stored in the user’s
IPFS, respectively.
Table 8 provides a detailed breakdown of the transaction
costs associated with deploying and interacting with the
smart contract for storage purposes on the ZKsync Era
Sepolia network. The deployment of the smart contract
Storage is a straightforward process, incurring a cost of
0.00000495615 ETH, equivalent to approximately 0.01 USD.
Storing specific data, such as diplomas, slightly increases
the transaction cost, requiring 0.00000559065 ETH, which
corresponds to approximately 0.02 USD. Similarly, storing
other certificates, including non-diploma credentials, incurs
a minimal fee of 0.000004499175 ETH, equating to around
0.01 USD. The provided transaction links offer detailed
verification and transparency for each operation.
5) DISCUSSION
The cost analysis of deploying and interacting with smart contracts, as summarized in Tables 5, 6, and 7, highlights the efficiency and cost-effectiveness of BlockMEDC (Ethereum zkRollups smart contracts)-based operations on the ZKsync Era
Sepolia network. A key observation is that the deployment of
smart contracts typically incurs the highest transaction fees
compared to subsequent interactions, due to the cost-intensive
nature of constructors. Constructors handle larger input sizes,
initialize state variables, and execute essential setup operations, making them inherently costlier. However, it is crucial
to emphasize that these costs are a one-time expense, as constructors are only executed during the initial deployment of
the contract. This makes the cost of deployment an upfront
investment, with subsequent operations such as registering
entities, adding roles, or storing data incurring significantly
lower fees.
Routine interactions with the deployed contracts, such
as adding institutions, students, and administrators, or issuing certificates and storing digital records (see Table 8),
demonstrate minimal gas usage and costs. These findings
highlight the scalability and practicality of smart contracts
for frequent operations, ensuring cost-efficiency in real-world
applications. The additional analysis from Table 8 further
supports this trend by detailing the negligible costs associated
with storing and managing digital records.
The goal of this paper is to evaluate the transaction
costs of BlockMEDC using Ethereum zk-Rollups (Layer 2)
for issuing and storing higher education degree certificates
in Morocco. As shown in Table 9, the costs associated
with various degree levels, including Associate, Bachelor’s,
Master’s, and Ph.D. degrees, demonstrate the affordability of
the BlockMEDC system. The estimated cost for an Associate
degree is 0.133 USD (1.34 MAD), calculated as follows:
2 × 0.006 USD for issuing other certificates (1st and 2nd
years), 3 × 0.007 USD for issuing transcripts, 1 × 0.02 USD
for issuing a transcript and diploma, 6 × 0.01 USD for storing
other certificates, and 1 × 0.02 USD for storing the diploma.
Similarly, the cost for a Bachelor’s degree is 0.083 USD
(0.84 MAD), which includes 1 × 0.006 USD for issuing
other certificates, 1 × 0.007 USD for issuing a transcript, 1 ×
0.02 USD for issuing a transcript and diploma, 3 × 0.01 USD
for storing other certificates, and 1 × 0.02 USD for storing the
diploma.
For a Master’s degree, the estimated cost is 0.133 USD
(1.34 MAD). This is broken down into 2 × 0.006 USD for
issuing other certificates (4th and 5th years), 3 × 0.007 USD
for issuing transcripts, 1 × 0.02 USD for issuing a transcript
and diploma, 6 × 0.01 USD for storing other certificates,
and 1 × 0.02 USD for storing the diploma. Finally, the cost for
a Ph.D. degree is 0.074 USD (0.75 MAD), which includes 3 ×
0.006 USD for issuing other certificates (6th, 7th, and 8th
years), 1 × 0.007 USD for issuing a transcript and diploma,
3 × 0.01 USD for storing other certificates, and 1 × 0.02 USD
for storing the diploma.
These results highlight the cost-efficiency of BlockMEDC
in managing academic credentials through blockchain
technology. The uniformity and affordability of costs
across all degree levels further demonstrate the practicality of the system for higher education institutions in
Morocco.
C. SECURITY ANALYSIS OF BLOCKMEDC SYSTEM
The security of the BlockMEDC system is critical to ensuring
the integrity, confidentiality, and authenticity of digital
certificates issued within the Moroccan higher education
system. This subsection outlines the key security aspects of
the system, focusing on the underlying Ethereum blockchain,
the security mechanisms of the MCA, and the roles and
responsibilities of the system’s users.
• Ethereum zk-Rollups Blockchain Layer 2 Security:
BlockMEDC leverages the security features of the
Ethereum blockchain to ensure the integrity and
immutability of digital certificates. Ethereum’s decentralized architecture and consensus mechanism make
it highly resistant to data tampering or alteration.
Additionally, the use of robust cryptographic techniques, such as elliptic curve digital signature algorithm
(ECDSA) [58] and cryptographic hash functions [13],
enhances security. These techniques generate a unique
‘fingerprint’ for each block, making any unauthorized
modifications easily detectable.
• Zero-Knowledge Proofs (ZKPs) for Privacy: Block
MEDC employs zk-Rollups not only for scalability
but also for privacy preservation. ZKPs ensure that
sensitive information, such as certificate details or
student identifiers, is verified without exposing the
actual data. This provides an additional layer of privacy
while maintaining trust and verifiability. The level
of privacy provided by Ethereum zk-Rollups-based
systems like BlockMEDC is not 100% private. While
ZKPs are highly effective at ensuring that sensitive data,
such as certificate details or student identifiers, is not
exposed during verification, the underlying blockchain
infrastructure still retains certain transparency characteristics.
• Tamper-Proof zk-Rollup Batches: zk-Rollups aggregate
multiple transactions into a single batch, and any unauthorized modifications to the batch would render the
zero-knowledge proof invalid. This prevents tampering
with data during off-chain aggregation and submission
to Layer 1.
• Immutability of Records: All certificate-related operations, such as issuance, updates, and revocation, are
securely logged on Layer 2 and validated through zkRollups. Once recorded, these operations cannot be
altered without invalidating the corresponding proof,
ensuring the immutability of data.
• Moroccan Certificate Authority: The MCA (e.g.,
Barid esign) functions as a trusted entity responsible
for issuing and managing digital certificates within
BlockMEDC. The MCA meticulously verifies the identities of participating educational institutions, ensuring
strict adherence to established regulations and standards.
The MCA implements robust security measures to
ensure the integrity of the system and offers users secure
storage options, such as SecurID keys or hardware
wallets, to protect their private keys.
• Role-Based Access Control: Smart contracts on Layer
2 implement robust role-based access controls, assigning
specific permissions to administrators, students, and
authorized personnel. This ensures that sensitive operations, such as certificate issuance or revocation, are only
performed by authorized users.
D. SCALABILITY ANALYSIS OF THE BLOCKMEDC
Scalability is a critical consideration for any blockchainbased system, particularly for one designed to manage
academic credentials at a national scale. Here, we evaluate the
scalability of the BlockMEDC system within the context of
the Moroccan higher education system, analyzing its ability
to handle realistic loads and transaction volumes.
BlockMEDC is implemented on Ethereum zk-Rollups,
which under typical conditions processes approximately
172.8 to 1, 728 million transactions per day, corresponding
to a throughput of 2, 000 to 20, 000 transactions per second
[57]. This capacity is sufficient for many decentralized
applications and aligns well with the requirements of the
BlockMEDC system.
Since academic certificates do not require immediate
issuance, the system leverages its non-real-time requirements to queue transactions during peak periods, effectively avoiding performance bottlenecks. Even in a scenario where all Moroccan universities issued certificates
simultaneously, the resulting transaction volume spanning
thousands of operations over a few minutes would still fall
comfortably within Ethereum’s zk-Rollups daily processing
limits.
E. LIMITATION OF THE BLOCKMEDC SYSTEM AND
POTENTIAL SOLUTION
1) LIMITATION
While the current version of the BlockMEDC system
demonstrates promising potential, it also presents a limitation
that need to be addressed:
• Higher Education Focus: The BlockMEDC system is
currently designed to serve higher education institutions
exclusively and does not yet support other levels of the
Moroccan education system.
2) POTENTIAL SOLUTION
Potential solution to address the current limitation of the
BlockMEDC system include:
• Expanding the Scope of Education: An effective solution
to address the limitation of BlockMEDC is to extend
its functionality to pre-university levels (primary, lower
secondary, and upper secondary education) by integrating the MASSAR system (Morocco’s pre-university
management system [59]). Additionally, extending the
system to other education levels (e.g., CPGE, BTS,
and OFPPT), enabling a unified and comprehensive
management of student and professor records across all
educational stages in Morocco.
VI. CONCLUSION AND FUTURE WORK
This paper introduced BlockMEDC, an Ethereum zk-Rollups
Layer 2-based system designed to enhance the security,
efficiency, and scalability of managing Moroccan higher
educational digital certificates. The proposed system offers
a cost-effective and scalable solution for issuing, verifying,
and storing academic credentials. BlockMEDC addresses
key challenges in traditional digital certification methods,
including forgery, inefficiencies in manual verification, and
the need for robust interoperability. This work demonstrates
the value of adopting blockchain technology to create
a transparent, tamper-proof, and efficient framework for
managing educational records. Our results highlight that
the proposed system significantly reduces transaction costs
while maintaining high scalability and performance. The
integration of smart contracts and off-chain storage solutions
ensures data security, immutability, and privacy, making
BlockMEDC a practical and impactful contribution to
the digital transformation of education in Morocco. The
proposed system not only delivers technical efficiency but
also aligns with national strategies for digital advancement,
reflecting the broader potential of blockchain in educational
governance. Future work will explore extending the system
to support primary, secondary, and vocational education
while improving its interoperability with global educational
platforms.
