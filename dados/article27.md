Title: Proxy Re-Encryption for Enhanced Data Security in Healthcare: A
Practical Implementation

ABSTRACT
In the rapidly evolving digital healthcare landscape, the imperative for robust, flexible, and scalable data protection solutions
has never been more critical. The advent of sophisticated cyber
threats, coupled with the increasing complexity of healthcare IT
infrastructures, underscores the necessity for advanced security
mechanisms that can adapt to a wide range of challenges without
compromising the accessibility or integrity of sensitive healthcare
data. Within this context, our work introduces the SECANT Privacy Toolkit, a pioneering approach that harnesses the power of
Proxy Re-Encryption (PRE) to redefine healthcare data security. We
present an implementation prototype that not only serves as a baseline for the quantitative evaluation of healthcare data protection
but also exemplifies the SECANT Toolkit’s capability to enhance
interoperability across disparate healthcare systems, strengthen
authentication mechanisms, and ensure scalability amidst the growing data demands of modern healthcare networks. This prototype
underscores our commitment to addressing the multifaceted security needs of the healthcare sector by providing a solution that
is both comprehensive and adaptable to the dynamic landscape
of digital health information security.By integrating cutting-edge
cryptographic technologies, including Attribute-Based Encryption
(ABE) and Searchable Encryption (SE), with the flexibility and control offered by PRE, the SECANT Privacy Toolkit stands at the
forefront of secure and efficient healthcare data management. This
integration facilitates not only the secure exchange of data across
decentralized networks but also empowers healthcare providers
with tools for fine-grained access control and privacy-preserving
data searches, thereby addressing key challenges such as data interoperability, cybersecurity threats, and regulatory compliance.Our
exploration reveals the toolkit’s potential to revolutionize the way
healthcare data is protected, shared, and accessed, providing a scalable, efficient, and user-friendly platform for healthcare providers,
patients, and stakeholders. The SECANT Privacy Toolkit not only
aligns with current healthcare data security requirements but also
anticipates future challenges, ensuring that it remains a vital asset
in the ongoing effort to safeguard sensitive healthcare information.
This work contributes significantly toward enhancing the security
and privacy of healthcare data, offering a robust framework for
interoperability, authentication, and scalability that responds to
the evolving needs of the healthcare industry. Through the deployment of our prototype and the subsequent evaluation, we aim to
demonstrate the practicality, effectiveness, and transformative potential of the SECANT Privacy Toolkit in advancing healthcare data
protection.
CCS CONCEPTS
• Security and privacy → Cryptography; Network security;
Security services; Database and storage security; Privacy protections; • Applied computing → Health care information
systems; Health informatics; • Networks → Data center networks; Storage area networks.
KEYWORDS
Healthcare Data Security, Proxy Re-Encryption (PRE), Cryptographic
Security, Data Privacy in Healthcare, SECANT Platform, Secure
Data Sharing, Encryption Technologies, Cybersecurity in Healthcare, Medical Data Protection, Advanced Encryption Methods, Interoperability in Healthcare Systems, Secure Data Delegation, Patient Data Confidentiality, Cryptographic Key Management, Digital
Health Information Security
1 INTRODUCTION
In the rapidly evolving domain of healthcare, securing sensitive
data represents a complex challenge. The landscape is marked by
the growing digitization of patient records, diagnostic information,
and treatment plans, all of which are invaluable and highly sensitive.
This digital shift necessitates not only robust security mechanisms
but also innovative approaches to protect against evolving threats
and vulnerabilities. Current methods often fall short in addressing
the complexities of secure data access across diverse systems and
the increased integration of digital technologies in healthcare. Despite significant advancements, current healthcare data security
methods often fall short in addressing interoperability, performance,
and scalability issues. This research aims to bridge these gaps by
introducing SECANT, a robust privacy toolkit leveraging Proxy
Re-Encryption (PRE). Against this backdrop, the SECANT project
aims to contribute to the ongoing efforts in enhancing healthcare
data protection. This project encompasses the SECANT privacy
toolkit, a specialized set of tools designed to enhance data security
in healthcare. Rather than redefining the landscape single-handedly,
SECANT introduces an innovative security framework that leverages Proxy Re-Encryption (PRE) among other technologies. This
approach is designed to complement existing security measures
by offering a more flexible and scalable solution to data protection
challenges in healthcare.
The integration of PRE within the SECANT platform is a deliberate choice, aimed at addressing specific vulnerabilities in healthcare
data security. By facilitating secure data sharing and access control
in a decentralized manner, PRE addresses the critical need for dynamic and efficient data protection strategies in complex healthcare
environments. This is achieved through:
• A strategic embedding of PRE into the SECANT ecosystem,
enabling secure and efficient data sharing across different
healthcare applications.
• An emphasis on practical applications, illustrating the realworld benefits and implementation scenarios of PRE within
healthcare settings.
Our analysis in this paper reveals that adopting PRE within the SECANT framework emerges as a significant step forward in tackling
the intricate challenges of healthcare data security. By dissecting
the architecture of PRE and its integration within SECANT, we
demonstrate how this approach not only complements but also
enhances existing security measures.
To provide a structured exploration of this topic, the paper is
organized as follows: After an initial review of the challenges in
healthcare data security and the limitations of traditional encryption methods in Sections 3 and 4 (now treated separately), we delve
into a comprehensive overview of the SECANT Privacy Toolkit and
its implementation of PRE. This examination allows us to articulate
the practical application and benefits of PRE in healthcare, culminating in a proof of concept that empirically validates the toolkit’s
effectiveness.
Through this investigation, we aim to illuminate the nuances of
deploying PRE in healthcare settings, addressing the core question
of why such an encryption approach is not just beneficial but essential for the future of healthcare data security. By doing so, we
not only highlight the innovative aspects of the SECANT project
but also underscore the critical need for advanced cryptographic
solutions in safeguarding sensitive healthcare information.
2 RELATED WORK
The landscape of healthcare data security is characterized by continuous evolution, with Proxy Re-Encryption (PRE) emerging as a key
technology for safeguarding sensitive information. This section
critically examines the progress in the field, emphasizing PRE’s
contributions and identifying areas where current strategies fall
short. Our research addresses these gaps, pushing the boundaries
of what’s possible in healthcare data security.
Proxy Re-Encryption, Key Management, and
Data Integrity:
Data integrity and key management are foundational to securing
healthcare systems. Research has explored PRE implementations
to strengthen these critical areas within cloud and fog computing environments. Efforts by Khan et al. (2020) [8] among others
towards lightweight PRE and improved key management have
advanced the field. However, these studies often overlook comprehensive assessments of computational demands, scalability, and
integration with healthcare IT infrastructures. Our research targets
these very gaps, proposing a framework that enhances scalability and ensures efficient integration with healthcare IT systems,
directly confronting the computational efficiency and scalability
concerns identified. Drawing from these insights, our work devises
a PRE-based framework that emphasizes lightweight operation,
streamlined key management, and meticulous evaluations of computational efficiency and scalability. Our approach, designed for
adaptability and interoperability across healthcare systems, aims
to surmount the noted limitations, offering a scalable and efficient
solution [8, 21].
Encryption Techniques and Secure Data
Transmission:
The importance of secure data transmission in healthcare cannot
be overstated. Recent studies have sought to improve encryption
techniques to ensure more secure data exchanges. Contributions
from Susilo et al. (2022) [15] and Zhang et al. (2022) [22] introduce
advanced encryption schemes for cloud and IoT services, yet face
challenges with computational intensity, scalability, and healthcare system integration. Our work proposes advanced encryption
techniques that alleviate computational burdens while facilitating
scalability and seamless integration with healthcare systems. Addressing the efficiency and integration challenges underscored by
these studies, our approach employs advanced encryption techniques within PRE, specifically crafted for the healthcare sector.
These techniques are aimed at reducing computational intensity
and ensuring scalability and ease of integration, effectively tackling
the issues outlined in prior research [15, 22].
Blockchain-Based Solutions and Federated
Learning in Healthcare:
Blockchain and federated learning represent cutting-edge approaches
to healthcare data security, offering decentralized solutions for enhanced cybersecurity and compliance. Research by Jiang et al. (2022)
[7] and Fan et al. (2022) [3] into these technologies highlights significant computational and integration hurdles. Our work strives
to integrate these innovative technologies within the healthcare
ecosystem efficiently, aiming to surmount these challenges. In our
research, PRE is incorporated within blockchain and federated learning frameworks, specifically addressing computational efficiency
and integration challenges. This strategy leads to a scalable, efficient framework that adeptly supports the nuanced requirements
of healthcare data security [3, 7].
Integrated Data Management Frameworks and
Orthogonal Access Control:
Effective data management and access control are pivotal in ensuring the privacy and security of healthcare data. Advances in
integrated frameworks and access control mechanisms aim to bolster these critical areas. Initiatives by Mittal and Ghosh (2023) [11]
and Wall and Walsh (2018) [17] toward enhanced access control and
data management in healthcare show promise but face scalability
and efficiency issues. Our research introduces a PRE-based method
that optimizes data management and access control, effectively
addressing these limitations without sacrificing scalability or efficiency. Through our work, we offer a novel data management and
access control solution using PRE, focusing on improving efficiency,
flexibility, and scalability. This directly addresses the challenges
highlighted in existing studies, presenting a sophisticated solution
that meets the contemporary demands of healthcare data security
[11, 17].
These studies collectively offer a detailed view of the evolving
landscape in healthcare data security, each presenting unique insights and solutions against a backdrop of significant challenges.
They underscore the importance of Proxy Re-Encryption (PRE) in
bolstering security across various computing environments, from
cloud and fog computing to federated learning, while also highlighting the ongoing need for scalable, efficient, and privacy-focused
solutions in modern healthcare data security frameworks.
Table 1 offers a comparative analysis of pivotal studies in the
healthcare data security domain, with a particular focus on Proxy
Re-Encryption (PRE) and associated technologies. Each study is
evaluated for its focal area, innovative contributions, limitations,
and its alignment with the objectives of the SECANT platform.
This comprehensive comparison is instrumental in identifying how
SECANT can significantly contribute by addressing existing limitations and capitalizing on the innovations outlined in these works.
These studies collectively provide a comprehensive overview of
the evolving landscape in healthcare data security, each offering
unique insights and solutions. They highlight the progressive role
of Proxy Re-Encryption (PRE) in enhancing security across varied
contexts, from cloud and fog computing to federated learning. Our
work builds upon these foundational contributions, integrating
PRE within the SECANT framework to address the challenges of
healthcare data security in a holistic manner. This integration underscores the need for scalable, efficient, and privacy-centric solutions,
aligning with the dynamic requirements of modern healthcare data
security.
3 CHALLENGES AND LIMITATIONS IN
ENSURING ROBUST HEALTHCARE DATA
SECURITY
3.1 Challenges in Healthcare Data Security
Data Interoperability. Achieving interoperability among diverse
healthcare systems and platforms is a pivotal challenge. The absence
of standardized formats and protocols significantly hampers effective data sharing and collaboration among healthcare providers.
Highlighted by [12], [8], [10], and further supported by insights
from [2], there is a critical need for standardized formats and protocols to ensure secure and efficient data exchange across healthcare
systems. The exploration of fog computing and anonymous key
generation by [10] introduces innovative approaches to bolster data
interoperability and security in healthcare, underlining the critical
role of advanced encryption techniques.
Increasing Volume and Variety of Data. The exponential growth
and diversification of data from electronic health records, medical
imaging, and wearable devices pose significant challenges. [19]
and [2] address the need for encryption methods capable of securely handling varied data formats and structures, pointing out
the necessity of content-aware DNA computing for medical image
encryption. Furthermore, [3] brings to light the challenges posed by
the increasing volume of healthcare data, advocating for PRE solutions that can effectively accommodate this diversity. This diversity
requires PRE solutions that are adaptable and capable of managing
the increasing volume and variety of healthcare data securely.
Cybersecurity Threats. Healthcare organizations face urgent challenges in combating evolving cybersecurity threats. References
such as [21], [20], [6], and [2] stress the necessity for robust encryption methods, like PRE, capable of defending against advanced
cyberattacks targeting healthcare data. These insights underscore
the critical need for advanced encryption methods to effectively
mitigate cybersecurity threats in the healthcare sector.
Regulatory Compliance. Navigating complex regulatory frameworks like HIPAA and GDPR presents significant challenges. [15]
and [2] discuss the adaptation needs of PRE solutions to different
legal frameworks, ensuring patient data remains secure and compliant. The flexibility and compliance with regulatory standards
are highlighted as crucial for developing encryption solutions that
can adapt to the evolving landscape of healthcare regulations.
Insider Threats. Mitigating risks associated with insider threats,
including employees and contractors who have access to sensitive
healthcare data, is critical. Discussions by [14] and [2] on the security of medical images using key-based encryption algorithms bring
attention to the need for addressing insider threats through stringent access controls and the application of advanced encryption
techniques.
Table 1: Comprehensive Analysis of PRE-Related Innovations and Their Integration in SECANT
Challenge: Interoperability, Key Management, and Data Integrity
• Khan et al. (2020) [8]: Lightweight PRE in fog computing. Limitations: Computational and scalability evaluation, certificate
management.
• Yang et al. (2016) [21]: Timing-enabled PRE for EHRs. Limitations: Time-based control, scalability, healthcare integration.
• Rahman et al. (2018) [12]: Blockchain for EHR. Limitations: Scalability, processing efficiency.
• Jabbar & Issa (2023) [6]: Cloud-suited PRE mechanism. Limitations: Data format adaptability, interoperability.
• Singh & Singh (2023) [10]: Key management in PRE framework. Limitations: Needs real-world validation.
PRE Aim: Enhanced PRE for improved interoperability, scalable key management, and data integrity.
Challenge: Cybersecurity Threats and Secure Data Transmission
• Susilo et al. (2022) [15]: Homomorphic PRE scheme. Limitations: Computational intensity, efficiency, integration.
• H.-Y. Lin and Y.-M. Hung (2021) [5]: Bidirectional multihop PRE. Limitations: IoT scalability, integration.
• Zhang et al. (2022) [22]: Secure IoT data transmission. Limitations: Computational, scalability, integration concerns.
• Wu et al. (2023) [14]: Encryption for IoT security. Limitations: Efficiency, applicability.
• Yang & Tian (2023) [18]: Quantum-resistant security measures. Limitations: Computational overhead, integration.
PRE Aim: Secure PRE methods for enhanced cybersecurity and efficient data transmission.
Challenge: Blockchain-Based Solutions and Federated Learning
• Jiang et al. (2022) [7]: Blockchain-based secure computation. Limitations: Computational efficiency, integration.
• Fan et al. (2022) [3]: PRE in federated learning. Limitations: Computational burden, integration.
• Rodrigues et al. (2023) [13]: Patient-centric PRE model. Limitations: Computational demands, scalability.
• Lin et al. (2023) [19]: Blockchain and federated learning. Limitations: Computational intensity, integration.
• Wang et al. (2023) [20]: Blockchain for data management. Limitations: Scalability, efficiency.
PRE Aim: Integration of PRE with blockchain to ensure privacy and security.
Challenge: Data Management and Access Control
• Mittal and Ghosh (2023) [11]: Integrated data management. Limitations: Scalability, efficiency, integration.
• Wall and Walsh (2018) [17]: Orthogonal access control. Limitations: Scalability, efficiency.
PRE Aim: PRE for advanced data management and access control, focusing on efficiency and integration.
3.2 Limitations in Traditional Encryption
Methods
Key Management Complexity. The complexity of managing encryption keys in large healthcare systems poses substantial logistical challenges. Works by [7], [13], and [2] delve into the intricacies
of key management and the need for simplified yet secure key
management solutions, underscoring the advantages of PRE methods that offer feasible key management solutions for healthcare
environments.
Granularity and Flexibility. Ensuring granularity and flexibility
in data access control is essential. Studies by [18], [11], and [2]
draw attention to the need for dynamic and fine-grained access
controls to suit complex healthcare workflows, pinpointing the
shortcomings of traditional encryption methods.
Performance Overhead. Performance overhead is a concern, especially in emergency medical services where response time is
critical. [17] and [2] address the need to optimize PRE to reduce
latency and ensure quick data access, highlighting efforts to address
performance concerns in time-sensitive medical services.
Limited Search & Analysis on Encrypted Data. Conducting searches
or analyses directly on encrypted data poses challenges with traditional encryption methods. The constraints of traditional encryption methods in this area, as discussed by [20], [3], and [2], highlight
the necessity for PRE solutions that enable advanced analytical capabilities without sacrificing data security.
4 LEVERAGING PRE IN SECANT’S SECURITY
STRATEGY
This section discusses the integration of Proxy Re-Encryption (PRE)
within the SECANT Privacy Toolkit, emphasizing its role in bolstering healthcare data security alongside the platform’s various
components. By deploying PRE, we effectively address critical challenges such as key management, access control, and encrypted data
analysis, enhancing the overall robustness of our security measures.
4.1 SECANT Privacy Toolkit Overview
The SECANT Privacy Toolkit is a central element of the broader
SECANT ecosystem. It serves as an advanced orchestrator of encryption technologies, playing a critical role in safeguarding information flowing through the Trusted Administration Module (TAM).
Challenge description Relevant
Works
Relevance to PRE Uses
Data Interoperability: The critical need for standardized
formats and protocols to enable secure and efficient data
exchange across healthcare systems.
[12], [8],
[10], [2]
PRE can offer interoperable security solutions, ensuring seamless
and secure data exchange across diverse healthcare IT ecosystems.
Increasing Volume and Variety of Data: Managing the diverse data types from electronic records to medical imaging
and wearable devices.
[19], [3],
[2]
PRE solutions can dynamically adapt to handle various data types
and volumes, ensuring robust data protection without sacrificing
accessibility.
Cybersecurity Threats: The urgency of defending against
sophisticated cyberattacks targeting healthcare data.
[21], [20],
[6], [2]
Demonstrates the importance of PRE in establishing resilient encryption frameworks capable of thwarting advanced cybersecurity
threats.
Regulatory Compliance: Adapting to evolving legal frameworks to ensure patient data is secure and compliant.
[15], [2] Highlights how PRE can be designed to be flexible and compliant
with regulatory standards, ensuring data protection aligns with
legal requirements.
Insider Threats: The risk posed by individuals with access
to sensitive healthcare data.
[14], [2] PRE enables fine-grained access controls and auditing capabilities
to mitigate the risk of insider threats effectively.
Key Management Complexity: The logistical challenge of
managing encryption keys in large systems.
[7], [13],
[2]
PRE simplifies key management challenges by enabling secure, delegated access without sharing private keys, improving usability in
complex healthcare environments.
Granularity and Flexibility: The need for dynamic access
controls in complex healthcare workflows.
[18], [11],
[2]
PRE facilitates the implementation of detailed access policies, allowing healthcare systems to finely tune who can access what data and
when.
Performance Overhead: Balancing encryption security with
optimal system performance.
[17], [2] PRE is designed to minimize latency, ensuring that data access and
transmission remain efficient even with strong encryption in place.
Limited Search & Analysis on Encrypted Data: The challenge of searching and analyzing encrypted data without
compromising security.
[20], [3],
[2]
PRE supports secure and efficient operations on encrypted data,
enabling meaningful analysis and search functionalities that respect
patient privacy.
Table 2: Integrated Synthesis of Challenges and Technical Requirements in Healthcare Data Security - A Direct Outcome of
Interactions with Healthcare and Security Stakeholders within the SECANT Project
This strategic positioning allows the toolkit to provide hybrid protection over data, combining various cryptographic techniques to
achieve critical security objectives:
Enhancing Device Security: The toolkit enhances device security by issuing a hardcoded, hardware-level symmetric key, addressing key management complexity. This symmetric key mechanism
fortifies device security, providing a secure foundation for device interactions and ensuring resilience within the SECANT framework.
Guaranteeing Data Integrity and Confidentiality: To ensure
data integrity and confidentiality, the toolkit utilizes a dual-layered
defense mechanism of symmetric encryption and HMAC. This
approach safeguards data integrity and maintains confidentiality,
providing a solid defense against unauthorized access and tampering, thereby addressing cybersecurity threats and regulatory
compliance concerns.
Expressive Data Sharing and Access Control: The toolkit
employs Attribute-Based Encryption (ABE) and symmetric encryption to facilitate fine-grained access control. This enables expressive
data sharing, allowing access based on specific attributes without
compromising confidentiality or flexibility. This capability is crucial
in overcoming the challenges of granularity and flexibility in access
control within healthcare systems.
Privacy-Preserving Search Over Encrypted Data: Implementing advanced Searchable Encryption (SE) techniques, the toolkit
offers both on-chain and off-chain searchable encrypted index structures. This design enhances privacy and security while also improving scalability and facilitating efficient storage of large volumes of
data. This approach directly addresses the challenge of performing
meaningful searches and analysis on encrypted data.
Decentralized Data Sharing with PRE: A key feature is the
Proxy Re-Encryption (PRE) module, introducing a novel mechanism
for encrypted data sharing. This decentralized approach, coupled
with robust key management capabilities, positions SECANT as
ideal for secure data sharing within decentralized network infrastructures, effectively managing performance overhead concerns.
4.2 SECANT PRE Module
The PRE module stands as the cornerstone of the toolkit’s data
sharing capabilities, enabling a proxy entity to transform ciphertext from one key to another without revealing the plaintext. This
section delves into the technical specifics, security measures, and
deployment types associated with the SECANT PRE module.
• Technical Information and Performance: The core components of the PRE module include PRE-SERVER, PRE-RESTCLIENT, and PRE-CLI, which are developed leveraging advanced technologies such as NestJS, PostgreSQL, and Node.js.
Deployment using Docker-compose highlights the toolkit’s
focus on scalability and reliability, crucial for overcoming
performance overhead in securing data.
• Communication with Other Modules: Integration with
SECANT’s other tools is achieved through REST HTTP APICDS interfaces, ensuring interoperability. This effective communication strategy is key to the toolkit’s ability to process
encryption and decryption requests efficiently, addressing interoperability challenges vital for comprehensive healthcare
data security.
5 ARCHITECTURAL APPROACH:
INTEGRATING PRE IN SECANT’S
ECOSYSTEM
Proxy Re-encryption (PRE) is a critical cryptographic method within
the SECANT system, uniquely designed to address the multifaceted
challenges of healthcare data security identified in our challenge
analysis. PRE enables secure data delegation, allowing a proxy to
convert ciphertext encrypted under one key into another, maintaining the confidentiality of the underlying plaintext. This mechanism
is particularly beneficial for scenarios requiring secure delegation
of access to encrypted data or for safely sharing and forwarding
information.
The process of key generation, where a data owner creates a
re-encryption key pair to authorize another user’s access, directly
tackles the challenge of key management complexity. The delegation and revocation of access, managed through the PRE system,
provide a controlled and efficient solution to the identified issues
of granularity, flexibility, and performance overhead in healthcare
data security.
5.1 Secure Transformation of Encrypted Data
In the SECANT PRE system, a rigorous process is employed for
securely transforming ciphertexts. The key components - PRE-CLI,
PRE-REST-CLIENT, and PRE-SERVER - are intricately designed to
address the performance overhead challenge by ensuring efficient
data encryption and decryption while maintaining high-level security. This workflow, illustrated in Figures 1, demonstrates the
SECANT platform’s capability to streamline secure data sharing,
aligning with the challenges of efficient and secure data transformation in healthcare environments.
The SECANT PRE system’s emphasis on directionality, interactivity, transitivity, collusion safety, and multi-use showcases its
comprehensive approach to addressing the challenge of maintaining data integrity and confidentiality in the complex landscape of
healthcare data sharing.
5.2 Sequence Diagrams
These sequence diagrams illustrate how the SECANT PRE module’s
functionalities align with and address the specific challenges identified in healthcare data security. The user setup keys, group management, and secure data flow processes demonstrate a thoughtful
and meticulous approach to overcoming challenges related to data
sharing, privacy, and security within healthcare systems.
User Setup Keys: Figure 2 shows the user key setup process,
critical for addressing the challenge of secure and efficient key
management in the SECANT system.
User Setup Consumers and Access Revocation: Figure 3
illustrates the process of creating groups and managing access,
showcasing the toolkit’s solution to the challenges of granularity
and flexibility in data access control.
Data Flow: Figure 4 encapsulates the secure data flow within
the system, highlighting the SECANT platform’s response to performance overhead concerns.
5.3 Privacy Toolkit Application in Use Cases
The application of the SECANT Privacy Toolkit in various use cases
demonstrates its capability to address the challenges identified
in the SOTA analysis. Each use case exemplifies how the toolkit,
particularly through the PRE module, offers solutions to specific
healthcare data security challenges, from patient-centric health
data management to cybersecurity in connected medical devices.
Use Case 1: Patient-Centric Health Data Management In
this use case, the SECANT PRE module transforms health data management, addressing interoperability challenges by enabling secure
information exchange between healthcare entities and patients.
Use Case 2: Cybersecurity for Connected Medical Devices
The PRE module’s role in securing connected medical devices and
mobile applications illustrates its effectiveness in mitigating cybersecurity threats and ensuring data integrity.
6 TECHNICAL IMPLEMENTATION OF PRE
WITHIN THE SECANT ECOSYSTEM
This section offers an in-depth look at the implementation of Proxy
Re-Encryption (PRE) within the SECANT ecosystem, bridging theoretical foundations with practical deployment. PRE is pivotal for
secure data sharing and access delegation, utilizing cryptographic
transformations that enable a proxy to re-encrypt data for different
users without revealing the plaintext.
Understanding the PRE Module Composition
The PRE module within SECANT includes several key components,
each tailored for specific roles within the encryption process:
- PRE-SERVER: Acts as the central node for handling encryption requests, built on NestJS for its scalability and ease of integration with other services. - PRE-REST-CLIENT: Facilitates communication between the PRE server and clients through RESTful
APIs, ensuring seamless data exchange. - PRE-CLI: A commandline interface for direct interaction with the PRE functionalities,
offering users flexibility in operation.
Deployment through Docker-compose highlights the emphasis
on scalability and reliability, key attributes for managing the
performance overhead in secure data handling.
Facilitating Communication and Interoperability
Communication with other modules of the SECANT platform is
achieved via REST HTTP API-CDS interfaces, underscoring the
PRE module’s adaptability and its role in enhancing the system’s
overall interoperability. This seamless integration is critical for
supporting the diverse encryption and decryption needs across the
healthcare data ecosystem.
PRE Algorithmic Framework
At the heart of PRE’s functionality within SECANT is its algorithmic
framework, designed for efficient and secure data delegation. The
process involves several stages, from key generation to the reencryption and decryption of data:
(1) Key Generation (PRE.KG): Initiates the encryption process
by generating a pair of keys for each user, consisting of a
public key (𝑝𝑘) for encrypting data and a private key (𝑠𝑘) for
decrypting data.
PRE.KG() → (sk, pk)
(2) Proxy Key Generation (PRE.ProK): Produces a proxy key
(𝑘𝑖→𝑗
) that allows the re-encryption of data from one user
to another, using the delegating user’s private key (𝑠𝑘𝑖
) and
the delegatee’s public key (𝑝𝑘𝑗
).
PRE.ProK(sk𝑖
, pk𝑗
) → 𝑘𝑖→�
(3) Encryption (PRE.Enc): Encrypts the plaintext message (𝑚)
using the recipient’s public key (𝑝𝑘𝑖
), producing the firstlevel ciphertext (𝐶
(1)
𝑖
).
𝐶
(1)
𝑖 ← PRE.Enc(𝑚, pk𝑖
)
(4) Re-encryption (PRE.Renc): Utilizes the proxy key to transform the ciphertext (𝐶
(𝑙)
𝑖
) from the original recipient to the
new recipient, incrementing the encryption level.
𝐶
(𝑙+1)
𝑗 ← PRE.Renc(𝐶
(𝑙)
𝑖
, 𝑘𝑖→𝑗)
(5) Decryption (PRE.Dec): Decrypts the re-encrypted ciphertext (𝐶
(𝑙+1)
𝑗
) using the intended recipient’s private key (𝑠𝑘𝑗
),
retrieving the original message (𝑚).
𝑚 ← PRE.Dec(𝐶
(𝑙+1)
𝑗
,sk𝑗)
This algorithmic approach allows SECANT to maintain data
confidentiality while facilitating the controlled sharing of encrypted
data, addressing key challenges in healthcare data security such as
fine-grained access control and secure data delegation.
Deployment and Practical Application
Further exploration of the PRE module’s deployment, including performance evaluation and real-world application scenarios, underscores its effectiveness in the SECANT ecosystem. The subsequent
sections will delve into these aspects, showcasing the practical
implications and benefits of implementing PRE for secure data
handling in healthcare environments.
7 PERFORMANCE EVALUATION AND
ANALYSIS
As of the time of composing this paper, the development of the
PRE module is still in progress. Consequently, the performance and
analysis section primarily focuses on the PRE library component,
which forms the core mechanism enabling the execution of the
re-encryption algorithm in the PRE module.
The PRE library underwent benchmark testing in a domestic
environment to gather basic performance metrics during cryptographic operations. The tests were conducted on a PC (Dell Inspiron
7386) equipped with an Intel Core i7-8565U CPU @ 1.80GHz, 1992
Mhz, 4 Core(s), 8 Logical Processor(s) and 16 GB RAM.
For detailed benchmarking procedures, refer to the documentation in references [16] and [4]. The library, primarily developed in
Rust, also features a NodeJS compilation [9] via a binding tool that
translates the Rust implementation into a binary NodeJS file. The
NodeJS version has been employed in the PRE module, and thus
the following benchmarks are pertinent to this implementation.
The Benchmark library [1] was used to evaluate the performance
of the cryptographic functions integrated into the PRE library. This
tool provides an effective means of quantifying the number of operations a function can handle per second. The summarized results
of this analysis are presented in Table 1, offering a comprehensive
view of the library’s performance.
Table 1 highlights that generating an Ed25519 key pair is the In
examining Table 1, we observe a notable distinction in performance
across the suite of cryptographic functions within the PRE library.
The ’Generate Ed25519 Key Pair’ function demonstrates exceptional
efficiency, leading the performance metrics with a significant margin. Conversely, the ’Decrypt level 2’ operation is characterized
by its extensive computational demand, representing the lower
bound of the performance spectrum. This contrast is indicative of
the heightened resource requirements for operations that entail
multiple re-encryptions, specifically when data is decrypted after
two successive re-encryption processes — initially from Group to
User, followed by User to Device. Such a pattern of performance
across these cryptographic functions underscores the substantial
computational resources necessitated by more complex decryption
activities.
The bar chart in Figure 5 succinctly depicts the variation in operations per second across different cryptographic functions, with the
generation of Ed25519 key pairs standing out as notably efficient.
On the opposite end, the level 2 decryption process is identified as
the most computationally demanding. The scatter plot in Figure 6
further reinforces these findings by showcasing the performance
of these functions against the backdrop of the sampled runs. Interestingly, the plot reveals no direct correlation between sampling
frequency and efficiency, suggesting that the performance of these
functions is influenced more by their computational complexity
than by the number of runs.
The data visualizations and the benchmark table collectively
accentuate a significant trend: the incremental increase in computational demand with each additional level of decryption. This trend
is not merely a metric of efficiency but also a critical factor affecting
the PRE library’s practical application, especially where multiple
decryption levels are obligatory, as elucidated by the decline in
performance to 15.61 operations per second upon introducing a
hypothetical third level of decryption.
Furthermore, the introduction of a third level in the decryption
process results in a performance of 15.61 operations per second,
indicating a significant time degradation compared to the second
level. This degradation is critical in scenarios where multiple levels
of decryption are required, such as in interconnected group settings
within the PRE module.
8 CONCLUSION
In our comprehensive exploration of the SECANT Privacy Toolkit,
with a particular emphasis on the pioneering Proxy Re-Encryption
(PRE) module, we have unveiled a significant paradigm shift in
confronting the multifaceted challenges of healthcare data security.
The toolkit emerges not only as a robust solution but as an innovative convergence of hybrid encryption mechanisms. These mechanisms amalgamate advanced cryptographic techniques, ensuring
the enhanced confidentiality, integrity, and controlled access of
sensitive healthcare information, a cornerstone for the privacy and
security of patient data. Our study has highlighted the toolkit’s exceptional capacity for facilitating decentralized data sharing within
healthcare networks. By leveraging the unique capabilities of Proxy
Re-Encryption, the SECANT Privacy Toolkit minimizes trust assumptions and revolutionizes key management. This advancement
is crucial for the secure sharing and accessing of encrypted healthcare data, effectively addressing the critical need for privacy and
security in digital healthcare environments. Moreover, the integration of Attribute-Based Encryption (ABE) within the SECANT
Privacy Toolkit empowers healthcare providers with fine-grained
access control. This feature is pivotal, ensuring that only authorized
personnel, identified through specific attributes, can decrypt and
access patient information. Such granularity in access control adds
a vital layer of security, safeguarding against unauthorized access
and ensuring compliance with stringent privacy regulations. The
toolkit’s implementation of Searchable Encryption (SE) techniques
further enhances its utility by enabling privacy-preserving keyword searches over encrypted data. In practical healthcare scenarios, where professionals must perform specific data searches, this
feature underscores the toolkit’s adaptability and user-centric design, facilitating efficient data management without compromising
on security. Additionally, the SECANT Privacy Toolkit’s dynamic
security measures, such as user delegation and the ability to modify
and revoke access permissions, provide healthcare administrators
with unparalleled flexibility. This adaptability ensures healthcare
organizations can respond to evolving access requirements while
maintaining stringent data security protocols, a testament to the
toolkit’s foresight in addressing future healthcare data security
needs. Looking forward, the toolkit’s development will continue
to focus on enhancing interoperability with existing healthcare
systems, strengthening user authentication mechanisms, ensuring
scalability, and further refining its cryptographic protocols. Implementing comprehensive user education and training programs will
also be crucial for maximizing the toolkit’s effectiveness and user
adoption. The SECANT Privacy Toolkit, with its cutting-edge Proxy
Re-Encryption module, represents a significant advancement in the
realm of healthcare data security. It provides a robust framework
for addressing current and future challenges in the protection of
sensitive healthcare information. As we move forward, the toolkit’s
continuous evolution will be instrumental in securing the digital
healthcare landscape, ensuring that patient data remains protected
in an increasingly complex and interconnected world. Future work
will involve rigorous testing and validation of the PRE module
within real-world environments, facilitated by partnerships with
leading healthcare institutions such as TIC-SALUT and POLARIS.
These collaborations will not only provide valuable insights but
also further affirm the practical applicability and impact of our
research on enhancing healthcare data security. Through these
endeavors, the SECANT Privacy Toolkit is set to remain at the
forefront of innovation, leading the charge towards a secure and
privacy-respecting digital healthcare future.
ACKNOWLEDGMENTS
This project has received funding from the European Union’s Horizon 2020 research and innovation program under grant agreement
No 101019645. The content of this article does not reflect the official
opinion of the European Union or any other institution. Responsibility for the information and views expressed therein lies entirely
with the authors.
