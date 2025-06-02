Title: Edge Computing Cybersecurity Standards: Protecting Infrastructure and Applications

ABSTRACT The advent of MEC (Multi-access Edge Computing), as a natural evolution of cloud
computing, can enable innovative services and applications, with many opportunities for end users. Hosting
applications at the edge could also address privacy and security issues inherent to the traditional cloud-based
deployment model, e.g., keeping regional regulatory compliance. However, shifting workloads to the edge
of the network warrants the consideration of new security risks. Separately, the recent specification of MEC
federations (as result of the GSMA’s Telco Edge Cloud) underscores the importance of security and trust due
to the heterogeneity of edge systems in global MEC deployments. Edge cybersecurity solutions must adopt
international standards for interoperability. Accordingly, ETSI MEC has endeavored to study edge security
threats and craft solutions, oftentimes based on existing standards from other industry groups. This paper
discusses the security challenges that arise from shifting workloads to the edge of the network with particular
emphasis on international standards and aims to provide a tutorial for developers and architects to navigate
the complexities in achieving edge computing security.
INDEX TERMS 5G, edge computing, edge native, MEC, cybersecurity.
I. INTRODUCTION
Edge computing is an emerging technology that improves the
performance, operating cost, and reliability of traditional
cloud-based applications and services by shortening network
hops between devices and the services they consume thereby
reducing network latency. The benefits of edge computing [1]
are widely recognized for end-to-end performance
improvements, and for the valuable context information that
can be gleaned from data collected at edge locations and
exposed to developers. This latter benefit is key to unlock the
innovation of new services and applications that can also be
edge aware and provide customized services, for example
location-aware or context-aware advertisements, personalized
contents (upon user consent), and tailored processing of local
data, from IoT (Internet of Things) devices and sensors. To
foster global adoption and interoperability of edge
deployments and applications, the European
Telecommunications Standards Institute (ETSI) created the
ISG (Industry Specification Group) MEC (Multi-access Edge
Computing) [2] to pioneer international standards on edge
computing, and support edge application developers and the
ecosystem. Upon launch in 2014 by ETSI, it was initially
focused on edge deployments in cellular networks (as the first
meaning of the MEC acronym was indeed Mobile Edge
Computing); however, since 2017, the group rebranded itself
as Multi-access Edge Computing, thereby broadening its
scope to include Wi-Fi and fixed access technologies. It
should be noted that cellular environments, especially with the
advent of 5G networks are a convenient deployment option for
MEC [3] due to the progressive virtualization of the network
infrastructure. MEC applications have been trending towards
running on a virtualized infrastructure, and thus the MEC
standard leverages much of the work of the ETSI NFV
(Network Function Virtualization) standards.
FIGURE 1. Edge Computing from a software developer perspective.
MEC introduced a three-tier application development
paradigm (depicted in Figure 1), adding an intermediate
workload located between the two traditional Client and
Server Application endpoints, where the server is usually
remote, e.g., in the private/public cloud. This led to a pivotal
shift in the telecommunications and networking sectors by
widening the scope of applications and services to be
integrated near the end user, with additional workloads,
services, and application endpoints at the edge of the network.
The ETSI MEC architecture includes the following elements:
• The MEC host, a physical or virtual entity that hosts
both the MEC platform and the virtualization
infrastructure. The host provides compute, storage,
and network resources for MEC applications,
• The MEC platform, which is responsible for
creating an environment where MEC applications
can be instantiated and run. It enables the discovery,
advertisement, and consumption of MEC services
• MEC applications, which are software applications
that run as virtual machines (VMs) on the MEC
host's virtualization infrastructure. These
applications can interact with the MEC platform to
consume and provide MEC services.
The MEC paradigm has enabled a flexible and programmable
network edge, but it has also rendered it vulnerable to new
cybersecurity risks and vulnerabilities in comparison to
remote servers in cloud data centers that have traditionally
been designed to be more resistive to cyber-attacks. Moreover,
distributing application workloads throughout the network
makes the protection from external threats less manageable
(although it can be acknowledged that a single edge server
containing a limited amount of local data can be less appetible
to adversaries). Furthermore, edge deployments may be
comprised of a large number of IoT and constrained devices,
which can be exposed to physical attacks [4].
On the other hand, edge computing can help companies and
systems overcome the conventional challenges of maintaining
compliance with divergent privacy regulations for managing
personal data (e.g., GDPR [5]). Edge computing provides the
opportunity to enforce privacy policies by placing certain
localized proxy policies that will disallow certain types of data
to leave that legal jurisdiction. These concepts are also
investigated by initiatives like Gaia-X, the European
Association for Data and Cloud, whereby a federated model
of cloud infrastructure aims to allow national governments to
apply local laws to cloud-hosted data. The solutions present in
literature [6] offer ways to leverage edge computing in the
automotive domain for guaranteeing privacy and access to
sensitive data, while also applying local laws.
Various standardization bodies, most notably ETSI MEC (in
alignment with other groups and fora, 3GPP, ETSI NFV, ETSI
TC CYBER, GSMA) have extensively addressed security
provisions for MEC infrastructure and MEC applications [7],
while considering regulatory compliance for data privacy.
This paper presents an analysis of existing edge security
standardization, with specific reference to the latest outcome
of MEC Phase 3 work (2021–2023) and outlines the need for
consistent security frameworks and protocols that cater to the
growing edge computing landscape. This paper is further
motivated by a scarcity of edge security tutorials in literature
to assist edge developers and architects.
The rest of the paper is organized as follows. Section 2
discusses some of the challenges of edge computing
cybersecurity. Section 3 reviews some related works and
standardization activities around MEC security. Section 4
describes some key security aspects related to MEC
environments together with best practices to address those
challenges. Section 6 draws some concluding remarks.
II. CHALLENGES OF EDGE SECURITY
Edge computing is a heterogeneous network environment
involving several systems and architectures. Fortifying this
type of environment to withstand a multitude of threats, while
maintaining a harmonized system of systems is a challenging
task.
In [8], the authors provide a good overview of edge
computing–assisted IoT security threats and solutions, but do
not consider ETSI MEC architecture and other related
standards. A more recent study [9] conducted an analysis
based on ETSI MEC architectural elements that was also
reused by GSMA as a reference methodology for identifying
and categorizing threat vectors in the Telco Edge Cloud
[10][11]. However, that study focused on the MEC integration
with 5G networks, while the ETSI MEC architecture is not
limited to cellular networks. Also, many threats in that survey
are out of scope of ETSI ISG MEC (e.g., those related to User
Equipment (UE)s, mobile access network, and core network,
all of which are in scope of 3GPP).
The white paper published by ETSI [7] analyzes the various
components of a MEC system, based on their standardized
architectures, and the survey in [9] identifies the threat vectors
for typical MEC deployments.
FIGURE 2. Security in MEC environments (ref. ETSI [8]).
Figure 2 (based on the MEC architecture defined in ETSI GS
MEC 003 [12]) shows the harmonized MEC architecture
supported by 3GPP (more specifically the EDGEAPP
architecture defined by WG SA6): here, both an EAS (Edge
Application Server) and a MEC application are “edge
application instances” and can provide similar
application-specific functionalities, and similarly the EES
(Edge Enabler Server) and MEC platform are functionally
aligned in the implementation of edge platforms. Figure 2 also
includes the supporting MEC management entities, at the host
level (MEC platform manager and VIM (Virtualization
Infrastructure Manager)), and at the system level (MEC
orchestrator, NFV Orchestrator and OSS (Operations Support
System)). Interactions between the Client App and the MEC
App (and related traffic routing and packet redirections) are
managed by a Data Plane functional element (not shown in
figure 2) and is usually implemented as a SDN (Software
Defined Network) controller. Security vulnerabilities can be
identified at various layers and interfaces, and thus call for
solutions from the related domain (i.e., from virtualization
security of NFV and SDN, to the telco domain security of 5G
Core (5GC) and Radio Access Network (RAN), and finally, to
the MEC application, MEC platform, and MEC management
system). This naturally poses a challenge in converging on a
holistic approach to edge computing cybersecurity. In this
respect, the ETSI Group Report (GR) MEC 041 [13], further
elaborated upon in Section 4, has identified a few potential
threats and vulnerabilities in MEC with technical solutions.
The introduction of MEC federations (the interested reader
can consult the architectural variant for MEC federation,
specified in ETSI GS MEC 003 [12]) is an additional driver
for securing edge environments. It is derived by the industry
need to interconnect multiple MEC systems (and MEC to
clouds). Securing these environments is business critical, as
multiple MEC systems and clouds operate in different security
domains that are owned and managed by multiple
stakeholders, wherein security levels can vary, from an
implementation and operational point of view
Figure 3 depicts the various entities involved in automotive
scenarios; wherein multiple cars are connected to different
MEC systems that are running in Data Networks of different
5G networks. This exemplifies a MEC federation, which also
includes the possibility for mobile operators to collaborate
with cloud providers (indicated as DN, Data Networks), to
host MEC applications.
FIGURE 3. Typical federated MEC environments for automotive
scenarios (ref. 5GAA MEC4AUTO [14]).
This architecture has been studied by the 5GAA
gMEC4AUTO work item [25] from a security perspective, by
analyzing threats at various levels:
• Security threats in gMEC4AUTO architecture
• Malware injection attacks (e.g., SQL)
• Man-in-the-middle attacks
• DoS attacks
• Advanced persistent threat
• Ransomware
• Privacy threats in gMEC4AUTO architecture
• Data privacy
• Identity privacy
• Location privacy during service migration
• Trust concerns in gMEC4AUTO architecture
• Establishment of trust among different application
servers
• Secure and “stateful” application migration
• Data location and lifecycle
• Continuous authorization and authentication
III. INDUSTRY EFFORTS SUPPORTING EDGE
SECURITY
It is reasonable to consult current industry best practices and
standards, which are applicable to MEC systems, to protect
both infrastructure and applications at the edge. In our
approach, we primarily consider the solutions available in the
space of IT security for cloud and internet technologies, as a
baseline “toolbox” to address the new challenges posed by the
edge computing paradigm. Since edge environments may in
principle introduce additional specific issues (over and above
the general case of cloud security), the present work also
captures the main insights from the ETSI White Paper [7] and
the ETSI Group Report MEC 041 [13].
A. Available standards applicable to edge computing
As a starting point, modern standards for Internet security are
directly applicable to ETSI MEC systems [2][15][16][17]. For
example, to secure REST APIs, the Transport Layer Security
(TLS) version 1.3 is used between the two communicating
endpoints based on, for example, digital certificates. TLS
tunnels achieve both confidentiality and integrity protection of
data exchanged between MEC entities. Mutual authentication
is indispensable for scenarios where the server needs
assurance of the identity of the client, such as whenever the
authorization is expected to be granted based on client
identities. In addition, authorization for access to resources can
rely on OAuth 2.0 standard.
Besides communication security, other security features
should be employed, relating to the lifecycle of MEC
components, from onboarding and execution, to monitoring
and management. Some of these features are listed in a GSMA
Fraud and Security Group document FS.31 Baseline Security
Controls [18]: MEC application installation and execution
(including isolation) security, MEC platform monitoring,
workload scanning, Network Function Virtualization
Infrastructure (NFVI) boot integrity, and others. For
attestation, IETF frameworks like the Remote Attestation
(RATS)[20] can be adapted to MEC system.
The security measures defined by ETSI NFV-SEC (SECurity)
specifications form the foundation of virtualized infrastructure
security and can be directly applicable to MEC. These
measures relate to several aspects of NFV: Management and
Orchestration security, Security Management and Monitoring,
API security, isolation and trust domains, and identity
management.
B. ETSI MEC (Multi-access Edge Computing)
ETSI ISG MEC specifies RESTful APIs for MEC services
using HTTP. The primary security consideration in the current
normative MEC specifications is API security. ETSI MEC GS
009 [15] and ETSI MEC GS 011 [16] mandate TLS for
encryption between MEC applications with a means to secure
the access to services. Over HTTPS, the MEC specifications
require OAuth 2.0 authorization to control access to services.
ETSI GS MEC 016 [17] also prescribes a gateway for MEC
hosts for mediating security and access control (among other
functions) from external devices to trigger application
lifecycle management operations.
As edge deployments constitute a complex multi-vendor
ecosystem, it is reasonable to assume an adversary (internal or
external) has already breached the system, which is a premise
of “zero trust” principles. The ETSI MEC architecture could
thus benefit from a zero-trust architecture model with practices
that assess and continuously verify the integrity of edge
computing applications and infrastructure over their
lifecycles.
IV. KEY SECURITY ASPECTS IN ETSI MEC
This section presents the security aspects from the perspective
of MEC applications and services which are critical from a
developer’s point of view. These can be categorized as below:
• Data Privacy and Confidentiality: Ensuring that
sensitive data is protected from unauthorized access and
breaches, especially when processed or stored at the edge.
• Authentication and Authorization: Verifying the
identities of devices, users, and applications accessing the
MEC platform and ensuring they have the appropriate
permissions.
• Network Security: Protecting the communication
between edge devices, MEC platforms, and the central
cloud from attacks such as eavesdropping, man-in-themiddle, and denial-of-service (DoS) attacks.
• Device and Platform Integrity: Ensuring that edge
devices and the MEC platform are secure from tampering
and malware, maintaining the integrity of both hardware
and software.
• Secure APIs and Interfaces: Protecting the APIs and
interfaces used for communication between MEC
components and external systems to prevent exploitation
and unauthorized access.
• Resilience and Availability: Ensuring that MEC
applications and services remain available and resilient
against attacks and failures.
ETSI GR MEC 041 [13] thus studies the security threats
related to MEC applications in relation to the MEC specified
procedures for application onboarding/instantiation,
authentication and authorization. For each key issue, the GR
offers remedial actions that draw from other industry
standards and methods to drive towards a new norm of
heightened application security in the MEC standards.
A. Stolen access tokens
Software vulnerabilities are routinely exploited by
attackers to steal sensitive data such as credentials or access
tokens. While data may be stored in encrypted form,
compromised encryption keys by a malicious insider or a
privilege escalation attack in the edge cloud would break
the assumed protections.
FIGURE 4. Illicit service requests using stolen access token.
Figure 4 illustrates the risk of REST servers conferring access
to protected resources to an adversary that presents a stolen
OAuth 2.0 access token as the bearer token over requests. This
could be prevented by adopting OAuth 2.0 Mutual-TLS Client
Authentication and Certificate-Bound Access Tokens (RFC
8705 [19]). As the TLS handshake provides proof-ofpossession of the client’s private key, it would follow that a
mutually authenticated client carrying an identity bound to the
presented token is most likely the authorized party. Thus, a
stolen access token would alone be insufficient to authorize
requests.
B. Stolen credentials
As suggested above, software vulnerabilities expose a large
attack surface making it hard to identify and track the leakage
of sensitive data such as authentication credentials. A limited
interface to an application’s identity and cryptographic keys is
thus crucial.
FIGURE 5. Threat of impersonation, identity theft.
Figure 5 illustrates the threat of stolen identity by an attacker
who can successfully authenticate to the REST server by
masquerading as the REST client while negotiating a TLS
session, and access protected resources. This threat may be
mitigated by maintaining a single secure instance of the
application’s credential in a hardened environment from
which keys cannot be hijacked by application software. This
environment could be tightly bound to the application and
authenticated by a hardware root of trust. Attestation
procedures could then convey signed evidence to a relying
party about the protection of the application’s credential.
(note: in the figure, the application software is also the TLS
endpoint; Confidential Computing technologies such as Intel
Trust Domain Extensions (TDX) or AMD Secure Encrypted
Virtualization (SEV) provide isolation of a TLS endpoint and
secure access to private keys)
C. Integrity and provenance
Spear phishing attacks by adversaries, misconfigurations in
cloud services, and password/access token disclosure through
code repositories are a few instances of leaking access to
virtualized workloads such as MEC applications. Having
obtained such access, an attacker may install rootkits or
persistent malware into a virtual machine for exfiltrating
sensitive data.
FIGURE 6. Attack through a compromised MEC service.
Figure 6 depicts an example of user data/asset theft by an
attacker through an undetected compromise of a virtual
machine that is executing a MEC service (i.e., the REST
Server in the above figure).
This threat could be mitigated by performing cryptographic
attestations (based on roles and patterns defined in RFC 9334
[20]) for collecting evidence over a trust chain from the MEC
application layer down to its Operating System (OS),
bootloader, firmware and ultimately a root of trust entity. A
verifier could evaluate this evidence against reference
measurements that represent the trusted baseline state of the
MEC application and its underlying components to issue a
verdict on the trustworthiness of the MEC application. Any
unauthorized change to the MEC application would result in a
mismatch of its component measurements with their reference
values and could trigger a termination of the MEC application.
As the MEC Orchestrator (MEO) on-boards and instantiates
applications, the MEO could be a relying party that assesses
trustworthiness of MEC applications. Accordingly, the MEO
may request attestations prior to or following application
instantiation and periodically at runtime based upon a policy.
D. Securing MEC application lifecycle
management (LCM)
The MEO is responsible for MEC application LCM that
broadly covers application onboarding, instantiation, update,
and deletion. MEC applications are subject to threats prior to
onboarding, for example due to a lack of secure development
processes whereby malicious code may be inserted into a
MEC application package. Figure 7 depicts an example of
secure MEC application package onboarding process. Here,
based on the security requirements, trustworthiness checks
may be performed over a MEC application package (for
example, sandbox testing, scanning for vulnerabilities).
Additionally, MEC application packages must be integrity
protected with a signature supplied by the application
provider. Therefore, to secure the onboarding process, the
OSS could assume the responsibility of carrying out
trustworthiness checks and verifying that the MEC application
package is untampered and reasonably expected to resist
compromise, and consequently sign the application package
to signify its approval. The MEO may then verify both 
signatures by the OSS and the application provider prior to
onboarding the MEC application as depicted below.
FIGURE 7. Secure MEC App package onboarding process.
When vulnerabilities are discovered in an instantiated
application, all instances of the application must be deleted in
a timely manner to limit the scope of the exploit. The MEC
host should clear all cryptographic and privacy-sensitive data
from memory resources used by terminated application
instances and release all their compute, storage, and network
resources. Application package updates should follow the
secure processes above for package deletion of the old version
followed by on-boarding/instantiation of the new version.
E. Detecting anomalous behaviors
A MEC system is likely to become a target of cyber-attacks.
A Security Monitoring and Management (SMM) system may
be used to identify compromised MEC entities. An SMM
system [13][21] would employ behavioral monitoring to
identify MEC entities that are taking actions outside
expectations for proper and secure operation of the identified
entity. The monitored behaviors may include excessive
resource usage, unusual traffic patterns, unauthorized data
access, connection attempts to grey-listed URLs, etc. Once
identified, an SMM system, through its management
component, may take steps to limit the operation (and hence
potential incurred damage) of the identified entity. This
functionality is in line with the zero-trust principle of
continuous monitoring. As an important note, the adoption of
SMM-based security controls can enable a system-wide
monitoring of the whole infrastructure, thus not limited to
MEC applications, services and platforms, but also including
the management entities and underlying NVFI and VIM
components leveraged by MEC systems. In this perspective,
while there are solutions and proprietary SMM
implementations adopted by the industry. Given the
heterogeneous nature of MEC deployments (involving
multiple stakeholders), a standardized solution for the SMM
interfaces might be beneficial for interoperability and global
adoption of security measures. Current work of MEC Phase 4
includes discussions on the need for standardization in this
area.
F. Aspects on regulations
Various standardization bodies and agencies, i.e., ENISA
(European Union Agency for Cybersecurity),
CEN/CELENEC (European Committee for Standardization/
European Committee for Electrotechnical Standardization)
have drafted reports and studies on the cybersecurity aspect of
the edge, covering both risks, open challenges, and current
mitigation practices. CEN/CENELEC, has released the
“Definition of Cybersecurity” [22], mainly providing
definitions and listing relevant organizations in the
cybersecurity field. On the other hand, ENISA in its report on
Fog and Edge Computing [23] carried out an overview of
industry standards for fog and edge architectures and systems.
The report outlined the close connection of Edge Computing
with 3GPP and ETSI standards bodies, which are the primary
source of security requirements for edge architectures,
whereas in the case of Fog Computing, Industrial-Internet-ofThings (I-IoT) bodies, i.e., Industrie 4.0, Industry IoT
Consortium (IIC), provide key directives and contributions.
The relevant reports focus on the definition of interfaces
among the defined Fog and Industry entities, their
intercommunication, and how they can be protected against a
set of defined attack vectors. ENISA’s report identifies
common security threats to edge and fog computing, such as
IP spoofing, DoS attacks, and information leaks. It provides a
comprehensive set of countermeasures, including strong
encryption, authentication protocols, secure boot processes,
and continuous monitoring. The report stresses the importance
of adopting a multi-layered security approach, combining
technical, organizational, and procedural measures to enhance
the overall security posture of edge and fog computing
systems. Furthermore, ENISA’s involvement in
standardization efforts ensures that the security measures for
edge and fog computing align with the latest industry
standards and best practices.
Industrie 4.0 and the Industry IIC play pivotal roles in defining
the security landscape for I-IoT environments, which are
closely related to fog computing. ENISA’s report
acknowledges their contributions in several key areas:
• Endpoint Security: Industrie 4.0 and the IIC provide
extensive guidelines on securing endpoints in industrial
environments. This includes recommendations for
implementing robust authentication protocols, secure
communications, and continuous monitoring. The focus
is on ensuring that every device connected to the network
is authenticated and that data transmitted between devices
is protected against interception and tampering.
• Interoperability and Standards: These bodies
emphasize the importance of interoperability between
different devices and systems in I-IoT environments.
They advocate for the use of standardized protocols and
interfaces to ensure that devices from different
manufacturers can communicate securely and effectively.
This is crucial for the seamless integration of fog
computing solutions in industrial settings.
• Risk Management and Mitigation: Industrie 4.0 and the
IIC provide frameworks for assessing and managing risks
in I-IoT environments. They recommend conducting
thorough risk assessments to identify potential
vulnerabilities and implementing appropriate mitigation
measures to address these risks. This includes the use of
firewalls, intrusion detection systems, and regular
security audits to ensure that the network remains secure.
• Physical Security Measures: In addition to
cybersecurity measures, these bodies also highlight the
importance of physical security in I-IoT environments.
This includes securing access to physical devices and
infrastructure, using tamper-evident seals and locks, and
implementing surveillance and monitoring systems to
detect and respond to physical security breaches.
• Collaboration and Information Sharing: Industrie 4.0
and the IIC encourage collaboration and information
sharing among stakeholders in the I-IoT ecosystem. They
promote the sharing of best practices, threat intelligence,
and incident-response strategies to enhance the overall
security posture of I-IoT environments. This
collaborative approach helps organizations stay ahead of
emerging threats and vulnerabilities.
For Edge Computing, 3GPP mainly targets 5GC and MEC
interfacing, defining relevant interfaces and their respective
security controls. The reports [24] include technical details
and some key use cases on edge security, along with respective
mitigation measures. The security aspects, under study, focus
on the enhancements for User Plane Function (UPF)
(re)selection with reducing impact on central 5GC Network
Functions, enhancement of Edge Application Servers (EASs)
and local UPF (re)selection, and Traffic Routing between local
and central part of the data network and the Edge Hosting
Environment information management.
Overall, Edge computing security remains an important and
evolving domain that different standardization bodies tackle,
each one from its own perspective.
V. FINAL REMARKS AND WAY FORWARD
The advent of MEC as a natural evolution of cloud computing,
can enable innovative services and applications. However, the
shifting of workloads to the edge calls for a study of new
security threats. Edge cybersecurity solutions must adopt
international standards for interoperability whenever possible.
This paper provided an overview of security challenges within
MEC environments, with the consideration of international
standards such as those from ETSI, 3GPP, and GSMA. It also
summarized the outcome of the MEC Phase 3 (2021–2023)
standardization efforts to address threats to MEC applications
and services. Further work on edge cybersecurity will be
carried out in ETSI MEC Phase 4, possibly in collaboration
with other standards groups (for example, with respect to EU
regulations, and/or the EU AI Act, and in alignment with
3GPP evolutions [26]), Distributed Ledger Technologies, and
Quantum Key Distribution.
