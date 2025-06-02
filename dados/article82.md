Title: Roles of Blockchain in the Metaverse: Concepts, Taxonomy, Recent Advances, Enabling Technologies, and Open Research Issues

ABSTRACT The Metaverse platform offers 3D immersive experiences through virtual reality, artificial
intelligence, and blockchain technologies. Blockchain-based Metaverse has garnered recent interest due to
its decentralization, anonymity, and other security features. Integrating blockchain into Metaverse promotes
the formation of a shared ecosystem and provides digital asset tracking, privacy protection, and security in
both virtual and physical environments. This paper explores the role of blockchain in creating and managing
the Metaverse platform. It is intended to provide a helpful reference for researchers and practitioners in the
field of the blockchain-based Metaverse. The main topics covered include the concept and characteristics
of the Metaverse; its different use cases, architectures, and technologies; Metaverse as a service provider;
Metaverse management; Metaverse users and data; and blockchain-based Metaverse in terms of roles,
technologies, applications, and challenges. In addition, recent advances in the blockchain-based Metaverse
and challenges such as scalability, interoperability, and edge resource sharing will be discussed. The paper
will conclude by highlighting open research issues and future directions, including improving immersion,
scalability, security, and integration with existing systems.
INDEX TERMS Blockchain, metaverse, Internet of Things (IoT), big data, cybersecurity.
I. INTRODUCTION
The Metaverse is a new kind of internet application and
social structure based on an interconnected platform within
cyberspace [1]. The foremost apprehensions about the metaverse are associated with its feasibility and security because a
metaverse can consume a spectacular amount of information,
data, and computational resources that require a secure and
trusted environment.Moreover, security and privacy threats
deter the construction of an applied metaverse platform. For
example, at the beginning of 2022, the metaverse company
Meta was litigated for illegally aggregating facial information
without users’ permission [2]. In addition, the attack superficial of a metaverse is very largely regarding its diversity.
The emergence of Metaverse technologies derived from
blockchain is considered a digital realization that can securely
transfigure digital adoption to an astounding level and spread
the range of services beyond the standard systems with
online access. Using digital twin technology, the Metaverse reflects the real world, securely combines the virtual
world and the natural world into an economic system,
and generates a blockchain-based ecosystem encompassing many of life’s key aspects (e.g. business, healthcare,
state systems, education, e-commerce, entertainment, and
TABLE 1. Metaverse research statistics based on technologies.
smart industries). Metaverse systems and services have been
developed with the resources supplied by digital systems
and online storage and processing capabilities at remote
data centers and cloud platforms. The focus of Metaverse
development has moved towards the consumer experience,
with the service’s efficiency, performance, and quality as
paramount [3], [4]. However, Metaverse platform implementation poses diverse technical challenges. This can include
interoperability between applications, technologies, security,
privacy, and massive data sharing [4]. Blockchain is one of
the most critical technologies applied to Metaverse in order to
overcome these challenges, specifically, blockchain’s smart
contract, which efficiently controls and automates complex
operations between Metaverse applications, digital content,
services, and users [5]. From a wider perspective, Metaverse
platforms are supported by several technologies such as artificial intelligence (AI), big data, internet of things (IoT), virtual
reality (VR), augmented reality (AR), multi-reality (MR),
andextended reality (XR) [6], [7], [8]. However, Blockchain
has multiple capabilities that metaverse applications and technologies have not utilized more widely up-to-date.
A. MOTIVATION AND CONTRIBUTION
Research has been conducted to study the interconnection
technologies the Metaverse technology requires. Table 1
presents research statistics for these technologies from
2022 until 30 Jan 2023 [9].
These statistics show Blockchain is one of the most critical
pillar technologies enabling Metaverse platform implementation. Several researchers have previously studied Blockchain
as a Metaverse enabler, as shown in Table 2, where the specific aspects of metaverse and blockchain-based applications
are discussed. However, Blockchain has multiple capabilities
that have metaverse characteristics. Architecture, management, applications, and technologies have yet to be efficiently
utilized.
The motivation behind this study was the revolutionary
potential of blockchain in the dynamic environment of the
Metaverse. The Metaverse provides realistic 3D experiences
TABLE 2. Comparative analysis of blockchain impact on metaverse
research.
made possible by artificial intelligence and virtual reality. The Metaverse gains decentralization, anonymity, and
strong security characteristics by incorporating blockchain.
By establishing a shared ecosystem enabled by this combination, security, privacy protection, and tracking of digital
assets are made possible in both the virtual and real worlds.
The inherent benefits of blockchain technology, such as
TABLE 3. Comparative study of this research with other metaverse surveys.
transparency, safe data sharing, and data interoperability,
can revolutionize the creation and administration of the
Metaverse and provide users with a new level of trust and
cooperation inside this dynamic virtual world. In order to help
researchers and practitioners navigate the rapidly developing
field of blockchain-based Metaverse technology, this study
clarifies the varied role that blockchain plays in the Metaverse.
The main contributions of this work are shown in table 2
and are summarized below:
- Provide an overview of Metaverse and blockchain,
as well as the motivations for using blockchain metaverse. We demonstrate that Metaverse has enormous
potential for facilitating blockchain.
- Discuss all taxonomy elements by analyzing the main
Metaverse concepts, characteristics, and taxonomy
architecture.
- Provide an extensive discussion of the use of blockchainbased Metaverse technologies, which includes
blockchain roles, technical aspects, opportunities, and
challenges.
- Finally, we discuss several research challenges from
the state-of-the-art survey on using Metaverse for
blockchain. We also highlight open research opportunities that provide a future research
roadmap.
Table 2 shows a variety of research efforts dedicated to
integrating blockchain technology with metaverse enablers.
Studies have grown in this field over the years, exploring
intricate aspects of blockchain applications within the metaverse. The exploration jointly highlights the transformative
potential of blockchain in enhancing security, privacy, and
functionality within the metaverse. Notably, recent studies,
such as [14] and [15], emphasize the fusion of blockchain
with edge computing, offering a novel perspective on computational resource optimization. The variety of issues covered
is a distinguished feature of these studies. From addressing
privacy concerns to suggesting encrypted addressing models and exploring the fusion of blockchain with emerging
technologies like edge computing, the studies contribute to a
nuanced understanding of the connection between blockchain
and the metaverse.
Moreover, a study [17] focuses on blockchain applications within the metaverse for asset storage and service
mechanisms in the metaverse universe. They introduced
‘‘Metarepo.’’ For Transactions on Emerging Telecommunications Technologies. However, it is crucial to acknowledge
these studies’ varying depths of coverage. Although some
touch upon many dimensions, others focus on specific aspects
of the metaverse. This variance underscores the interdisciplinary nature of the topic, with diverse studies emphasizing
distinct elements based on their objectives and perspectives.
This paper studies blockchain as an enabler of the Metaverse. First, comparison analysis and related work are
conducted and summarized in Table 3. Then, a review of
Metaverse concepts, users, service providers, and characteristics will be discussed. Second, a Metaverse taxonomy is
presented based on architecture, technology, role as a service
provider, management, users, and data. Finally, blockchainbased Metaverse roles, challenges, and opportunities will
be discussed. In addition, Table 3 compares the current
study with previous metaverse surveys, revealing a comprehensive and balanced approach to understanding the
metaverse ecosystem and the role of blockchain within it.
The study stands out for its consistent coverage across various dimensions, including metaverse concepts, technologies,
architecture, management, taxonomy, users, and blockchain.
Unlike previous studies that show gaps in coverage, this
study provides a holistic understanding of the metaverse.
It balances by addressing technical and non-technical dimensions, confirming in-depth topic exploration. This inclusivity
is mainly evident in the study’s thorough discussion of the
opportunities and challenges of integrating blockchain into
the metaverse.
FIGURE 1. Road map of the paper’s sections.
B. PAPER OUTLINES
The paper is organized as follows: Section II introduces metaverse concepts, Section III shows metaverse characteristics,
Section IV presents metaverse taxonomy, Section V offers
blockchain-based metaverse, Section VI discusses the roles
of blockchain in metaverse technologies, Section VII provides metaverse applications based on blockchain challenges,
and Section VIII presents concluding remarks. Figure 1 provides a summary of the paper’s organization.
II. METAVERSE CONCEPTS
From a linguistic perspective, the term ‘‘Metaverse’’ consists
of two parts: the prefix ‘‘meta’’ which means far or beyond,
and the second term ‘‘verse,’’ which refers to the concept
of the universe. The term Metaverse has come to describe
innovative social systems within a novel digital living space,
a beyond-reality universe, and a permanent and cohesive
diverse-users environment combining physical reality with
digital virtuality [21], [22], [23], [24]. From a technical perspective, Metaverse is an innovative internet application that
provides human communication and interaction where new
technologies emerge within an era of internet-based social
interaction [25], [26]. From a business-related perspective,
Metaverse has revealed promising business opportunities.
Massive corporations, like Facebook in 2021, have committed themselves to creating the Metaverse as a new capital
export. User expectations of the freedom of the virtual world,
the content, and the internet’s interaction methods, among
other things, are continually rising [11], [27].
Several Technologies are involved in creating the Metaverse platform, such as virtual reality, IoT, and blockchain,
which enable users to take part in many applications in
real-time and in parallel. In his famous science fiction novel
Snow Cras, Neal Stephenson first introduced the concept of
Metaverse in 1992 [28]. In Stephenson’s novel, users exploit
digital avatars to operate and compete to enhance their status.
Arguably, the most crucial consideration in the Metaverse
is the economic system, where the token economy is established using blockchain [29]. Blockchain is the foundation
technology of digital cryptocurrency, considered the main
currency among commercial organizations in the Metaverse
space. Therefore, Metaverse characteristics, technologies,
architecture, service providers, and users will first be analyzed. Figure 2 shows the concepts of Metaverse.
III. METAVERSE CHARACTERISTIC’S
Metaverse is an internet application that virtually connects
diverse technologies with social interactivity. This section
provides the key characteristics of Metaverse, and Figure 3
illustrates these characteristics, which can be summarized as
follows:
A. DISTRIBUTED VIRTUAL UNIQUENESS
In the Metaverse, users distribute their virtual identity
because they must move across multiple systems and
applications with different accounts that record only some of
their personality characteristics and information. This virtual
identity is genuine, autonomous, and has its own roles in
different applications [30]. In the Metaverse, third parties are
avoided for activity management. Users can spontaneously
and openly articulate the Metaverse rules, endlessly convey
their views, and present themselves. Metaverse gives users a
unique custodian of their data and digital identity based on
blockchain confidentiality and privacy techniques [31].
B. ECONOMIC CREDIT
The Metaverse introduces an encouraging arena for economic purposes. Opportunities exist for legislators to set trade
rules for web3 technologies that maintain user security and
stimulate innovation. These rules should encourage greater
collaboration between public and private industries. The critical components for making the Metaverse an economic
success are interoperability and portability, cryptocurrencies or crypto exchanges, and financial services adopted
by blockchain methods. In addition, blockchain has broad
non-financial applications inspired by the Metaverse economy [32], [33].
C. 3D CONTENT
Metaverse is an internet-based 3D creation featuring virtual territory and physical objects. In the future, users can
act remotely, tour virtual museums, and attend virtual festivals at home. Organizations and businesses use innovative
technologies such as big data, blockchain, XR, MR, AR,
VR, 3D modernization, AI, and IoT to control the 3D
Metaverse [7], [34].
D. DISCRETIONARY
The Metaverse operates over various multifaceted physical
environments. In particular, heterogeneous hardware may
vary in the user interface, data format and classes, data
processing, communications, and application services, which
drives the need for Metaverse to handle diverse environments
flexibly and with discretion. In addition, interaction terminals
should be continuously compatible with connected persistent
devices [35].
E. SOCIAL INTERACTIVITY
The Metaverse is primarily an environment for social interaction where users play roles and connect in real time utilizing
avatars. It has a modern form of social standards. Metaverse
has its representative system, legal system, economic formation, and culture, which are close to but not equal to the real
world [36].
F. TECHNOLOGIES COLLECTION
Innovative and trending technologies are integrated into the
Metaverse platform, which implements blockchain to build
an economic system and offers an immersive experience
based on VR, AR, and MR technology. Metaverse uses digital
twin technology to create a mirror image of the real world,
and it collects, shares, and stores data using IoT, big data, and
cloud computing [37].
G. HYBER SPATIOTEMPORALLY
Metaverse encourages the virtual and physical worlds to
coexist. It transcends the confines of time and location and
offers consumers unrestricted, cost-free, immersive experiences [38].
H. PERPETUITY
The Metaverse platform was developed to be sustainable
and perpetual. Moreover, the evolution and upgrading of
Metaverse is autonomously accomplished. The appearance
of the Metaverse is due to the evolution of technology and
science within the growth of human civilization. It has unique
social associations, beliefs, ethical regulations, and industrial
society.
The Metaverse is simultaneously perpetual and evolutionary. With the collaborative innovation of artificial
intelligence and human inventors, the growth of Metaverse
is dynamic. It has been modernized to generate a new
lifestyle and to attract users with a superior dimensional
experience [39], [40].
IV. METAVERSE TAXONOMY
In this work, we introduce a new taxonomy for the Metaverse
environment. Studies [17], [20] have introduced a taxonomy for the Metaverse, which classifies it into five systemic
parts: sensors and physical devices, rendering and recognition, scenario generation, technical methods, user interaction,
and Metaverse applications. The taxonomy developed in this
work has the following systemic categories: architecture,
technologies, Metaverse as a service provider, management,
technologies, users, and data. The content of each category is
specified as presented in Figure 4.
A. METAVERSE ARCHITECTURES
Several architectures for Metaverse have been introduced.
Duan et al. [41] present an architecture of three layers: infrastructure, interaction, and ecosystem. Another candidate for
Metaverse architecture is proposed by Radoff, who defines
seven layers from bottom to top: human interface, decentralization, spatial computing, creator economy, discovery,
and experience. This sequence of layers depends on the market’s expected value [40]. Based on intelligence networking,
Yuchuan Fu et al. introduced a Metaverse architecture that
covers the physical and the virtual world [19].
An innovative architecture consisting of three main layers (physical space, enabled technology, and virtual space)
is developed here and presented in Figure 5. The physical space layer consists of two sub-layers, the first being
the Metaverse service layer, where shared services such as
healthcare, education, smart city, and others are provided.
The second sublayer is the gateway’s smart edges, which
contain the specific edges users need to access the Meta
FIGURE 2. Metaverse concepts.
FIGURE 3. Metaverse characteristics.
verse platform, such as wearable haptics, cloud resources,
and intelligent mobiles. The second layer in this Metaverse
architecture is the enabler technologies, which identify the
enabler technologies to transfer from physical space to virtual space, such as AI, DT, and IoT. The final layer is the
virtual layer, which encompasses two sub-layers: i) virtual
edges, which illustrate the common virtual objects obtained,
such as avatars and virtual products, and ii) virtual universe,
which the Metaverse platform gives the virtual Metaverse
environment.
B. METAVERSE TECHNOLOGIES
The Metaverse platform merges diverse, innovative technologies to achieve user-immersive experiences that connect real
and virtual space. These include IoT, blockchain, AI, big
data, VR / AR / XR / MR, digital twin, cybersecurity, cloud
computing and mobile intelligence. The following sections
will discuss the roles of these technologies in the Metaverse
platform.
1) INTERNET OF THINGS (IoT)
IoT is a digital network consisting of billions of everyday physical objects interconnected across wired or wireless
channels to share information, interact, and access data
resources. IoT is an integral part of the Metaverse infrastructure, which controls the link between the physical world
and the technological space. The combination of IoT and
Metaverse will likely open new opportunities for growth and
FIGURE 4. Metaverse taxonomy overview.
development within virtual and real space [43]. The
real-world data accumulated by IoT devices and sensors is
crucial for harmonizing the two worlds [44]. IoT allows the
Metaverse to gather information from the real world and
immerse it in the virtual one.
Moreover, it is vital to organize this data within the
Metaverse and guarantee its security and access for users.
Businesses invest substantial amounts of capital on Metaverse
projects featuring data intelligence solutions. Figure 6 shows
explains IoT in the Metaverse.
2) ARTTIFICIAL INTELLIGENCE
Artificial intelligence, used to integrate intelligence into the
Metaverse for a better user experience, is a crucial technology for Metaverse development. An AI simulation built
on a genuine image or 3D scan will look at user photographs on the fly and produce incredibly lifelike virtual
interpretations known as avatars. The realistic traits and
qualities of an avatar in the Metaverse affect the overall
quality of the user experience. In more concrete terms,
AI may create a variety of facial expressions, emotions,
styles, aging-related qualities, and other characteristics for
the avatar to make it more animated [45]. As a result,
despite linguistic limitations, anyone worldwide will be able
to access the Metaverse with significant artificial intelligence
training [46].
3) BIG DATA
The Metaverse will reduce the difference between virtual and
real-life interaction in the age of big data [40]. All users who
navigate the Metaverse work in a data-driven manner with
the virtual world. The data will continue to increase as more
and more Metaverse applications are developed, resulting
in the development of a big data system that will require
tremendous processing power. As a result, massive data processing technology is essential for putting the Metaverse into
practice [47]. Figure 7 presents the primary operations that
big data can process in Metaverse.
4) BLOCKCHAIN
In 2008, Satoshi Nakamoto [48] introduced Bitcoin, the
first decentralized digital currency and blockchain technology is now a vital component of the Metaverse platform.
Blockchain’s distributed and immutable ledger makes transparent transactions possible. Blockchain technology is a
model that combines very complex and diverse systems to
carry out data exchange, processing, transfer, and storage
space. These systems include peer-to-peer networks, cryptographic techniques, communication tools, distributed storage
with consistency, and smart contracts. Its greatest strength is
the decentralized consensus mechanism used by blockchain
to distinguish responsible and anonymous transactions that
are successfully suited for the Metaverse [49]. Blockchain is
FIGURE 5. Architectural frameworks in the metaverse.
FIGURE 6. Metaverse integration with IoT technology.
FIGURE 7. Big Data processes within the Metaverse.
a technology facilitator for all Metaverse technologies thanks
to these properties. Due to the significant implications of
blockchain in the Metaverse, its specific responsibilities will
be covered in detail later in this article.
5) VIRTUAL AUGMENTED, MULTI, AND EXTENDED REALITY
The Metaverse platform acquires inputs such as data from
participant-managed key elements, whereby the virtual world
is created, retained, and improved. AR and VR deliver an
immersive 3D experience. AR displays physical space along
with additional virtual objects, whereas VR is purely in digital
space. AR transforms the environment with digital visuals
and fictional characters [50].
It is more accessible than VR and can be used with almost
any smartphone or digital camera. A proactive Metaverse
is how AR and VR operate. Through physical simulations,
VR can improve the Metaverse [51]. Multi-reality (MR) is
like AR. However, MR facilitates the location of 3D objects
where users can interact with their environment, helping them
to add an authentic universe of 3D objects created by computers. Extended Reality (XR) is a technology vital for the
Metaverse’s growth. Existing AR, VR, and MR mechanisms
must be expanded to promote the complete assimilation of
virtual objects to a super-realistic level with increased ubiquity. AR, VR, MR, and XR enable users to encounter and
become involved in the Metaverse visually.
In contrast, haptics, such as haptic gloves, permit user
involvement in the Metaverse using further touch modality [52]. This improves user interactions and opens up the
possibility of providing physical services in the Metaverse,
such as transmitting a handshake across the globe or virtual
remote surgery. These technologies are created by guidelines
that promote interoperability, such as the Virtual Reality
Modelling Language (VRML), which controls the physics,
properties, computer graphics, and interpretation of virtual
assets. This allows users to move across the Metaverse easily [53]. Figure 8 shows AR, VR, MR, and XR in Metaverse.
6) DIGITAL TWIN TECHNOLOGY
One of the main enablers of a Metaverse is digital twin
technology (DT), which is used to model the physical system
virtually in real time [54]. The structure of the Metaverse
utilizes DT to twin the real world entirely into a virtual world.
The role of DT is achieved through developing and data
merging. In [55], researchers found a blockchain-empowered
federated learning framework running a trust scheme in
Digital Twin for Mobile Networks, which takes direct trust
evidence and recommended trust information into account.
Their evaluation method can evaluate the trust levels of
users with distinctive behavior models accurately. Furthermore, it presents better in avoiding attacks from clients
that alternately execute good and bad activities compared
with state-of-the-art schemes. The result obtained shows the
significance of using secure DW in a metaverse environmentbased blockchain.
The Metaverse’s pragmatism is combined with DT, which
opens up new possibilities for services and social interaction. For instance, Microsoft Mesh allows users operating
from several sites to cooperate simultaneously in real-time
digital versions of their office. Moreover, digital twins give
remote-controlled vehicles and robots better eyesight and
coordination while advancing transportation, military, and
industrial sectors. Applications like healthcare, education,
real estate, and entertainment gain from the prominence of
3D visualization with precision and context awareness [56].
Figure 9 illustrates the digital twin technology in the Metaverse, showing the relationship between physical and digital
space.
7) CYBERSECURITY
Implementing Metaverse as a service provider for many
industries, applications, and businesses increases cybersecurity threats and risks, where millions of cyber-attacks and
malicious activities may occur daily. Therefore, data security
in the Metaverse will remain challenging [57], [58], [59].
The main feature of blockchain is immutability, making all
Metaverse transaction records unchangeable and enhancing
secure sharing capabilities even in an insecure environment.
Privacy and security concerns such as network certification
theft, personal identity theft, avatar authentication issues,
unauthorized data access, phishing attacks, denial of service
attacks, misuse of user/avatar data, trusted and interoperable authentication, and ransomware attacks arise due to the
technologies that enable the Metaverse (i.e. big data, IoT,
blockchain, AR, VR, and DT). Cybersecurity countermeasures have emerged in Metaverse environments [60], [61],
[62], [63]. Figure 10 shows various security issues and their
corresponding countermeasures. Also shown are the roles of
cybersecurity in the Metaverse [64], [65].
8) CLOUD COMPUTING
Developing the Metaverse platform depends upon the growth
of cloud computing, whereby computational power may be
increased [66]. Moreover, the social and collaborative nature
of Metaverse applications results in significant amounts of
data being cooperatively and simultaneously disbursed by
numerous users [67].
Cloud networks facilitate the end-to-end optimization
and dynamic management of exclusively Metaverse applications across Next Generation networks. In Metaverse,
high-performance cloud storage, cloud computing, and cloud
rendering are required within user devices, along with server
reliability, flexibility, and resilience. With cloud computing,
Metaverse guarantees continuous rapid processing, complexity reduction, and reduced power consumption [68], [69].
9) MOBILE INTELLIGENCE
The growing number of mobile devices and clients has
affected the reality of wireless communication networks,
which must progress to handle the specific requirements of
superior data speed, latency, and device connection capacity [70], [71]. The emerging Metaverse requires 5G / 6G
generational communication networks with specific characteristics. Therefore, Metaverse services and applications need
a variety of users to meet this requirement.
5G / 6G networks enhance the working indicators of communication networks by a multiple of up to 100 and also
maintain a mechanism for transmitting innovative real-time
avatar information and compressed image data created by VR
devices and edge cloud servers.
This clearly augments the execution performance of
Metaverse technologies that encompass all reality and virtualization. For example, XR devices gather information,
including biometric information like fingerprints, handprints,
and iris signatures, plus the accumulation of user information
from other social media platforms [72], [73], [74], [75].
XR applications can also deliver combined wireless sensors
for immersive and real-time user connections. In addition,
other Metaverse technologies affected by the exponential
evolution of mobile intelligence in internet traffic have led
to a remarkable evolution in computing concepts [71]. Intelligent mobile applications have more rigorous demands that
cloud computing cannot satisfy, such as ultra-low latency,
ultra-high throughput, ultra-high stability, and high spectral
efficiency. Meanwhile, big data associated with Metaverse
applications and IoT devices contributes to massive growth
in overall traffic streams [76].
C. METAVERSE AS SERVICE PROVIDER
Metaverse as a service implies a contribution-based model
for using Metaverse platforms instead of acquiring a lifetime authorization. Private, public, and business sectors
are now adopting the model of Metaverse as a service provider, which allows different sectors to customize
their features and functionalities according to their audiences in a real-time immersive environment. The following sections demonstrate the most common sectors
that use Metaverse as a service provider, as illustrated
in Figure 12.
1) HEALTH CARE
Recently, healthcare demand has generated an urgent need for
digital transformation settings using AI, IoT, telecommunication networks, virtual platforms, and blockchain. In health
care, the introduction of Metaverse-connected online space,
with the interactive combination of VR, AR, MR, and XR,
presents a new era of immersive and real-time experiences to
improve social interaction and connection. This technology
allows for the conception of virtual environments with 3D
space and avatars, which could be significant on patientadjacent platforms. This technology includes telemedicine
platforms, remote operational practices, and simulated medical and surgical education [77], [78]. The execution and
acceptance of these emerging virtual healthcare technologies
will require complex and innovative methods that guarantee several attributes, which include interoperability between
real-world and virtual clinical situations; user-friendliness
of the new technologies; efficient compliance with medical
issues; health economics; governance, ethics, and cybersecurity [79], [80], [81], [82].
2) EDUCATION
During the COVID-19 period, examples of the mirror world
(i.e. video conferencing systems such as Zoom, Webex,
Google Meet, and Teams) were used for virtual education
delivery. The Metaverse is specified to mimic mirror world
function where Metaverse space has a great potential to
enlarge the information and roles required for knowledge
while showing the real world accurately as if it is a reflection in a mirror [83]. Nevertheless, a shortcoming of virtual
education is the difficulty of providing ‘‘on-hand’’ lessons.
With additional Metaverse users, data capital can be used
to improve AI tutors for customized lessons ‘‘on hand’’ further [84]. A continuous compromise between delivering the
required education services and using the Metaverse tools
with haptic technology is required. Moreover, practical learning can be achieved through virtual simulation platforms that
will reduce the real-world practical learning cost and risk, for
example, dangerous surgery simulation [85], [86], [87].
3) ECONOMICS
The Metaverse is an extension of the physical world, and both
worlds come together to generate an incorporated ecosystem [32], [87]. The economic systems within the Metaverse
are based on Blockchain, which has been developed to
carry out economic systems for various sectors, including
decentralized finance (DeFi), cryptocurrencies, non-fungible
tokens (NFT), the transaction platforms of digital assets,
money exchanges, and others [88], [89]. In the upcoming
decades, the Metaverse will be a virtual live territory where
all users generate a complete supply chain to deliver and
utilize digital content cooperatively. To protect the ownership
of digital assets, the owners should manage and follow their
flow process. Blockchain, as the practicable decentralized
infrastructure of Web 3.0, empowers users to market digital
assets with transparency and traceability. All stakeholders can
manage the ownership of digital assets through the smart
contract-enabled Web 3.0 ecosystem and distribute the economic value within the Metaverse [88]. In addition, digital
assets are the mechanism to sustain the development of the
Metaverse economic system [90], [91].
4) ENTERTAINMENT
Entertainment, which includes movies, virtual concerts,
games, and online sports, is currently the most popular
Metaverse service. Online multi-sensory interaction between
people is the focal point of the Metaverse, which provides
virtual ‘‘spaces’’ in which users act and communicate with
each other in real-time via digital representation of players
or ‘‘avatars’’ [92], [93]. With the increasing requirements for
realism in movies, virtual concerts, games, and online sports,
AI is applied to computer agents (or non-player characters)
to simulate people’s intelligent behavior to enhance players’
experience [94]. Several characteristics, such as self-control
strategy, realistic character animations, lifelike musical con
FIGURE 8. Exploring AR, VR, MR, and XR technologies in the metavers.
FIGURE 9. The role of digital twins in the metaverse.
FIGURE 10. Cybersecurity technologies in the metaverse.
cert, superior graphics and voice, and others, exhibit the
intelligence of these entertainments [95].
5) REMOTE WORK
Metaverse employee socialization involves immersive job
preparation, remote working, and virtual work business meetings. Switching to remote work generates enterprises that
prioritize virtual environments [96], [97]. Initial findings
show that workers in Metaverses experience excitement from:
1. The spirit, presence, and behaviour of worker avatars,
2. Pragmatism, innovation, and affordances of the virtual
environment and
3. Technological steering and resistance.
Smartphones, augmented reality glasses, virtual reality headsets, and PCs can all access this virtual workspace. The
Metaverse can adjust how workers cooperate with the technology they use and the people they must cooperate with
to carry out their work. The Metaverse potentially augments
relations and connections, reintroducing many human aspects
into otherwise two-dimensional virtual meetings. It can be
considered a step towards a future 3D workplace [98], [99].
6) COMMUNICATION
Communication in the real world is based on distinguishable identities and addresses. However, communication in the
Metaverse is different because each user needs a unique identity that fits them. No one can track or verify this identification, which could be an encrypted virtual address in the Metaverse. Reallocating virtual addresses to a person’s identity
and choosing a specific spectrum to improve address-based
communication is necessary to preserve anonymity in the
Metaverse. Thus, using blockchain-based Metaverse native
communications to connect things to their native encrypted
addresses directly could significantly improve current network services based on IP, cellular, HTTP, . . . etc. [100].
Additionally, without addressing the implementation-related
problems with communication and networking, the Metaverse faces a difficult time replacing the Internet, particularly
given that it is currently accessible to billions of users. A shift
from information to experience-based service communication is generally supported by Metaverse [71], [73], [101].
7) SOCIAL WORKS
Since Facebook’s 2021 transformation to a Metaverse platform, a modern era of social interaction has started. Because
of the Metaverse, online social networks have become
crucial to maintaining social connections. It has had a
near-revolutionary impact on the entire social network. The
Metaverse is anticipated to make users develop new social
service practices. Using Metaverse as a service provider
for social networks, a fundamentally new business model
depends on three sequential processes: creation, proposition,
and value capture [101]. Metaverse provides an integrated
stage and collaborative environment for users to design things
and integrate. The Metaverse would resemble expanding
current social interactions online into 3D or possibly into
the real world. Even when people cannot be together physically, it will enable everyone to share immersive experiences.
In addition, Metaverse delivers the cognitive and interactive
behavior of users in the collaborative design activities in the
virtual world [102].
8) SMART CITIES
The smart city concept transforms all city services into digital
form, using information technology in city services management. The notion of a smart city has evolved into a Metaverse
City. Implementing the Metaverse concept must adapt to
various technologies that assist it, for example, VR and AR,
loT, AI, internet, and blockchain [103]. These technologies
are very beneficial for emerging smart cities to enhance the
quality of life, considering sustainability, social objectives,
economics, and citizens’ luxuries [104], [105].
9) WEB 3.0
Web 3.0 is any technology that relies on blockchain, neural
networks, machine learning, AI, IoT, semantic web, cryptocurrency, and VR / AR. Therefore, Metaverse is considered
the 3D Internet or Web 3.0 [106], [107] and one of the most
feasible technologies to move forward with Web 3.0. Web 3.0,
the concept for the next generation of the Internet, embodies the potential for user-centric engagement and interaction
experiences in a decentralized manner. Metaverse is becoming one of the most promising technologies to expand Web
3.0 into a three-dimensional virtual environment because it
shows potential to support immersive services such as AR /
VR, healthcare and education, and remote work [108].
D. METAVERSE MANAGEMENT
Metaverse management refers to the administration, governance, and regulation of virtual world platforms. It involves
overseeing the activities and interactions within the Metaverse, including setting rules and policies, handling disputes,
and maintaining the technical infrastructure. Metaverse management aims to generate a safe and secure environment
for users to engage in virtual experiences while balancing
their freedom and enjoyment. The following sections present
some critical aspects of Metaverse management, as shown in
Figure 11.
1) TECHNOLOGY MANAGEMENT
The most vital technologies for Metaverse management are
those for linking and merging real space with virtual space,
primarily regarding network, sessions, mobility, and energy
management.
2) RESOURCES MANAGEMENT
Within the Metaverse, optimal strategies for digital resource
management and diverse objectives task scheduling are
necessary. In addition, resource management technology
must successfully find and share resources. Researchers are
continually investigating resource management solutions to
support the Metaverse’s implementation in heterogeneous
environments and to provide a dynamic resource allocation
framework to synchronize the Metaverse with IoT services
and data [109], [110]. On the other hand, developers have
also introduced cloud resource discovery mechanisms for the
Metaverse environment [111].
3) NETWORK MANAGEMENT
In the Metaverse, network and communication techniques
make data available to communicate efficiently between
partners, overcoming space, time, and service limitations.
Moreover, Metaverse applications, technologies, and services
in daily life, such as healthcare, education, entertainment,
smart cities, and social media, would also be replicated
and achieved in the Metaverse [19]. Moreover, methods
of networking and communication in the Metaverse must
provide secure and error-free data transmission, similar to
the role of the network layer in IoT architecture. The most
conventional techniques in the network layer incorporate
short-range wireless communication and mobile communication technologies, which are also appropriate in the Metaverse
for networking and communication [112]. As a universal
requirement for wireless data and voice communication,
Bluetooth technology provides short-distance wireless connectivity, allowing communication between immovable and
mobile devices. These short-range wireless networks are likewise substantial in the Metaverse and will be implemented
between devices and ‘‘avatars’’ [113], [114].
4) SESSION MANAGEMENT
Session management technology primarily incorporates technologies significant to security and privacy, and Metaverse
should prevent sessions from being attacked. Numerous
studies have attempted to develop a defensive technique to
avoid destructive authentication threats and encrypt asynchronous sessions, which are applied in the Metaverse
environment [115], [116]. In addition, session management
addresses the control of communications between users and
always available resources over heterogeneous networks.
Controlling continuous interactions with dynamic features is
essential in the Metaverse scenario, especially when sessions
involve many resources. The session environment is accessible to enhance the user’s immersion experience in real-time
with high-performance levels in 5G and 6G communication
wireless networks [117].
5) MOBILITY MANAGEMENT
5G and 6G network technology has provided considerable
advantages to people, including superior-speed data transmission with low latency, less cost, huge system capacity, and
large-scale device connection. These networks have evolved
from centralized mobile cloud computing to distributed fog
computing and mobile edge computing (MEC). The merging of MEC with Metaverse technologies and 6G wireless
communications addresses the limitations of mobile devices
regarding storage space, resource allocation, computational
performance, and efficiency [118]. Their revolutionary applications in several domains significantly impact nations,
customers, and businesses, leading to a future society of
brilliant and autonomous systems that support Metaverse’s
aims of affording immersive user experiences. However, this
makes increasingly greater demands on data communications, transmission, and processing. In addition, MEC runs
at the network’s edge and is suitable for security-crucial
applications. In addition, MEC servers often have a lot of processing power, making them particularly good for Metaverse
in analyzing and processing massive volumes of data received
by Metaverse applications [119].
6) ENERGY MANAGEMENT
Electric energy consumption is managed and facilitated
within the Metaverse architecture. Researchers have introduced several techniques to control energy [13], [120]. The
practices developed are based on IoT methods to examine
consumption in various efficient and recurrent neural network
designs and an exponential power estimate model to decrease
power loss and save costs. In addition, another technique
is reliant on the theory of harvesting energy and saving
electricity by converting the network energy efficiency as
an optimization problem into a stochastic problem [121].
The developed techniques applied time-scale energy-sharing
algorithms based on the Lyapunov framework [122]. Energy
management and sustainability are mandatory in Metaverse
and investment challenges.
E. METAVERSE USERS
As the Metaverse continues to grow in popularity and
usage, the user demographic will likely expand and diversify, offering opportunities for new and innovative uses and
experiences. However, it is also essential to ensure that Metaverse environments are safe, secure, and inclusive for all
users, regardless of their background, culture, or identity. The
following section will show how Metaverse affects users in
many ways, as shown in Figure 13.
1) WORKPLACE USERS
In Metaverse, the development of immersive workspaces
enables all workers from anywhere in the world to collaborate
and communicate without direct contact. Metaverse can help
increase worker productivity, facilitate flexible and customizable workspace, and provide a scalable social environment
for businesses and employees. Meanwhile, implementation of
the Metaverse faces many limitations, which include worker
unfamiliarity with Metaverse technologies and the expense of
the platform to build and control [123], [124].
2) ART AND LIVE ENTERTAINMENT USERS
In the Metaverse, users of entertainment services like
music, theme parks, festivals, video games, and movies use
immersive technology to live together in pleasing virtual
reality [125]. For example, VTR concerts by a favorite artist
can be experienced from users’ homes. The use of augmented
and virtual reality to generate effects like holographs can add
amazing immersive experiences to concerts. Similarly, users
can roam in virtual art galleries, attend festivals, and be in
motion technology to produce real-time show performances.
Users can play games in groups where digital animation
allows them to experience the world and custom app games
that feature AR characters and entertainment acts. Users can
create exhibitions with rooms featuring live and pre-recorded
streams of performances with opportunities for branding and
product placements [126], [127], [128].
3) EDUCATION USERS
Education over Metaverse can involve students and teachers
in a 3D virtual world. Learners can see and interact with their
peers and the surrounding 3D objects, much like in a real
classroom [129], [130].
4) ONLINE DATING AND SOCIALIZING
Social media in the Metaverse changes how users consume
daily content in the virtual world, where they can act together
with digital objects in a shared or private virtual environment
that is more immersive and lifelike. On the other hand, the
Metaverse social dating platform is an interface between
multiple users that facilitates sharing several complex experiences based on avatars. Users can create virtual spaces such
as restaurants, park benches, lakes, or parks for real-time
sharing [131], [132].
5) GAMES USERS
Gaming in the Metaverse provides a diversity of roles and
services highly relevant to users’ daily lives. The most famous
aspect of video games is 3D virtual games, which extend to
users’ strong relationships in the Metaverse [133], [134].
6) HEALTHCARE USHERS
The Metaverse can be applied within healthcare in various
ways, including training for healthcare professionals and
students, surgical procedures, patient experience, and digital
twins. Moreover, within the Metaverse, healthcare providers
may contact a patient for a regular check-up using a digital
twin to explain how a process will be carried out or to envision
the effects that their lifestyle preferences might have on the
health of their body [77], [78], [79], [134], [135].
F. METAVERSE DATA
In the Metaverse, applications can manipulate the data flow
within and across physical and virtual space. Blockchainbased database ledgers address emerging challenges,
including data interoperability, sharing, security, privacy,
engineering, and portability, as shown in Figure 14. The
following section will discuss issues related to Metaverse
data [136].
FIGURE 11. Metaverse management strategies.
1) DATA INTEROPERABILITY
In Metaverse, data interoperability is crucial for all innovative Metaverse capabilities. The Metaverse as an ecosystem
must control its interoperability from one point to another,
where successful virtual spaces require the sustainability of
assets at multiple locations [137]. Moreover, organizations
require undisrupted business data streams between systems
and users, customers, and suppliers. Also, consumers must
be confident that their data will be sustained across Metaverse
platforms without managing multiple identities [138], [139].
2) DATA SHARING
In the Metaverse, data gathered by one entity must flow
effortlessly between different applications, programs, consumers, and boards. Therefore, consumers are granted the
ability to move digital assets and avatars between Metaverse
platforms. Data-sharing techniques must be established to
process multilateral data-sharing arrangements and to satisfy
users [106]. In such situations, sharing data between diverse
users’ including data privacy and protection is challenging [140], [141].
3) DATA PRIVACY AND SECURITY
Organizations can monitor physiological responses and biometric information, including vital signs, facial expressions,
and voice inflections, in real time. This sensitive behavioral
data must be protected since it is of great value to marketers and advertisers. It is critical to ensure that data is
collected ethically and cannot be used for malpractice [142].
In the Metaverse, users can be anyone they want, but it
is still essential to protect them. Automated systems must
be introduced to protect data privacy and reputation, where
updating is vital in reputation management. It is typically
done by the Trusted Authority (TA) regularly after aggregation, decrypting, and authenticating a huge number of
reputation feedbacks, which leads to excessive computation
and communication overheads on the TA lateral and even
makes the TA generate the bottleneck of reputation management system in virtual worlds and to prevent users from
getting scammed. Therefore, standard regulations must be
followed [143], and organizations must be concerned about
their data security in all physical and virtual space stages. This
includes data ownership, dissemination, storage, processing,
tracking, and transition [144].
4) DATA ENGINEERING
Growth in Metaverse usage and innovation is predicted to
continue exponentially, with up to 20 times the present data
used in 2032 [145]. Therefore, Metaverse providers must
adopt diverse solutions to deal with all data transactions and
keep track of this massive amount of data. Processing and
using this data is challenging because the data stream will
become highly speedy, reflective, and extensive [146]. Hence,
the Metaverse data platforms must be equipped to cope so
that industry owners can accumulate and process internal or
third-party data to analyze perceptions, power other industry
processes, and keep up with the rapid pace of Metaverse
growth.
5) DATA PORTABILITY
Data portability defines how data can be transferred between
diverse applications and cloud storage services. Users, businesses, and organizations collect data in the cloud and require
the ability to transfer digital assets from one space to another
effortlessly. Consequently, data has a financial value, and
users must access it wherever they go. Industries using the
Metaverse must guarantee the portability of data that will
build flexibility for the future [147], [148].
V. BLOCKCHAIN-BASED METAVERSE
Many in the computing industry believe that the Metaverse is
the next internet iteration because its social network provides
a single, distributed, immersive, continual, 3D virtual space
where people can interact beyond the physical world. This
innovative technology became widely known when Facebook
rebranded itself as Meta in October 2021 and revealed plans
to invest at least $10 billion in the concept that year. Over
the coming decades, Metaverse will significantly impact
technologies such as IoT, big data, 6G, AI, 3D modeling,
and reconstruction: VR, spatial computing, and digital twins
(DT). However, the most critical technology is blockchain.
Widespread applications of the Metaverse are non-fungible
tokens (NFTs), digital real estate, video conferences, digital
arts, and using Metaverse for work collaboration [149], [150].
Blockchain has crucial roles in Metaverse applications [145],
[151], [152]. Firstly, blockchain guarantees data security
and privacy through cryptography techniques and consensus
protocols.
The Metaverse assembles massive amounts of sensitive
information to provide users with the ultimate potential
experience without revealing information and in an authentication manner. Second, blockchain guarantees data quality.
Since Metaverse collects information from diverse applications such as banking applications, healthcare information
systems, governmental services, and entertainment applications, it must examine and validate the quality of this sensitive information. Blockchain offers comprehensive appraisal
paths for all transactions, permitting users and organizations
to validate and approve all transactions. Thus, it can enhance
data quality in the Metaverse [153]. Third, blockchain
guarantees data integrity by the mechanism of immutability. Collecting information in a block copy and hashing
every block in the chain can only be edited or deleted
if all participants approve. Fourth, blockchain guarantees
data interoperability for Metaverse’s different virtual worlds
where stakeholders require data, diverse applications, asset
acquisition, and manipulation. There are limitations when
interoperating between different applications and data in virtual worlds since they exist in distinct environments, but this
is resolved by blockchain’s interoperability feature [151],
[152].
Moreover, blockchain’s other significant features (decentralization, transparency, tamper-proofing, transaction without third-party/fees) provide security, reduced costs, faster
performance, scalability, and the efficiency of millions of
transactions within Metaverse financial applications. In addition, the smart contract technology used by blockchain
guarantees the distribution of the operation of contracts in
an automated, autonomous, provable, perceptible, and reliable manner, therefore promoting Metaverse to common
use in financial, social, and gaming applications and effectively moderating the destructive and malicious activities
that may exist in these areas. Finally, Metaverse technology widely uses non-fungible tokens (NFTs) and federated
learning applications where digitization, privacy, decentralization, availability, scalability, and uniqueness features are
required. All these features are offered by blockchain [152],
[153]. Metaverse’s introduction into AI applications requires
federated learning (FL), which prevents privacy outflow by
allocating training tasks to numerous clients and isolating the
local devices from the main server.
Nevertheless, FL has many weaknesses, for instance,
single-point failure and malicious data. For the deployment
of FL, the benefits of incorporating blockchain technology
offer a secure and effective option [147]. However, for NFTs,
applications need digital storage and digital data exchange,
privacy, security, automation, lower transaction costs, and the
verification of participant and owner [147], [155].
VI. ROLES OF BLOCKCHAIN IN METAVERSE
TECHNOLOGIES
In the current and future decades, prospective Metaverse
applications and consolidated technologies will use the
blockchain features of anonymity, security, indisputability,
sharing data, privacy, traceability, immutability, decentralization, smart contract, and consensus to accomplish the
implementation [146], [152]. In addition, one of the most
notable developments in digital innovation and Metaverse
financial ecosystems is blockchain technology [156], [157],
[158]. Blockchain is a high-impact technology that can
modernize finance, economics, gaming, social media, smart
cities, entertainment, education, healthcare, and specifically
to enable the Metaverse, as presented in Figure 15. Table 4
summarizes the popular applications with case studies based
on the specific roles of blockchain that emerged with the
pillars of Metaverse and their effectiveness and importance.
A. INTERNET OF THINGS
IoT in Metaverse covers a great range of tasks where massive
data from diverse devices in IoT is gathered continuously to
guarantee that it functions well across many Metaverse applications. These applications include healthcare, education, and
smart cities where huge data, storage, hardware, and physical
devices need reliable and secure virtual environments. IoTbased blockchain allows the enormous number of devices in
the Metaverse to connect to data within the blockchain, where
shared transactions are delivered with corruption-resilient
records in virtual worlds. Additionally, IoT data will be
accessible to participants and applications without requiring
centralized management or control. Blockchain should scale
with the Metaverse in IoT, which will be a real challenge.
B. ARTIFICIAL INTELLIGENCE (AI)
AI in the Metaverse is by nature centralized, and the data is
managed centrally and accumulated, making it an object for
management and exploitation. However, integrity, privacy,
traceability, and decentralization of data in blockchain are
guaranteed. Therefore, combining blockchain and AI in the
Metaverse will help empower trustworthy digital analysis
and decision-making on massive data. Moreover, due to the
actions of numerous users, diverse and substantial amounts
of secondary and tertiary data are produced. This data has a
unique identification tag and is utilized as traceable data in
the blockchain-based Metaverse. Such information is developing into valuable AI applications within the Metaverse.
By contrast, the consensus process in blockchain requires
high speeds to add a new block. If a mistake due to any
vulnerability is detected in a smart contract, adding a new
block will be discouraged, motivating hackers to exploit the
vulnerability and losing hundreds of millions of dollars in
crypto-currencies. Thus, AI-Agent and federated learning are
crucial to correcting and repairing smart contracts, enhancing
blockchain application security, regulating active scalability parameters, and delivering operative personalization and
authority mechanisms.
C. BIG DATA
Big data management is one crucial technology required
to expand Metaverse applications where various data will
accumulate to establish a big data network. In fact, with big
data, massive data manipulation is crucial to the digital world,
which will raise awareness of innovative opportunities in
business models within the Metaverse. In contrast, extensive
data management in the Metaverse environment must deal
with heterogeneous, scalable data with speedy processing
requirements. Blockchain in Metaverse will support huge
data integrity without the intervention of a third party, high
data quality, classified data for users, reduced data retrieval
time and cost, and data accessibility.
D. EXTENTED REALITY(XR)
Extended reality (XR) technology combines real and virtual
worlds into an environment for human-computer interaction (HCI) using computer technologies and wearables.
XR applications are required as an enabler of the Metaverse
platform. However, VR, AR, and MR technologies should be
improved to fully support the combination of virtual objects
for super-realism and enhance its ubiquity. The emergence of
XR in the Metaverse raises additional concerns about social
and personal issues. Companies can gather huge and sensitive information from diverse XR systems to support their
production of innovative and recommended systems. The
Metaverse should guarantee the security, privacy, scalability,
and transparency of this sensitive information for users of
XR systems. Metaverse’s blockchain-based distributed ledger
would facilitate the authentication and the traceability of XR
application data, which would help to create a complementary
truthful recommendation system. Additionally, blockchain
techniques support data safety and the integrity of XR application file systems.
E. DIGITAL TWINS (DT) TECHNOLOGY
DT in the Metaverse means the modern digitalization of the
whole world within the Metaverse. Therefore, all the applications of the Metaverse are unable to work together correctly
unless an initial connection between the digital and the physical world is recognized and made. Digital twin applications
such as financial markets, healthcare, and social media should
collaborate and stay stable in changing virtual environments.
Moreover, digital twins must fix consistent communication
faults when sharing real-time data. Blockchain techniques
provide digital twins in the Metaverse ecosystem, specifically
the distributed Hyperledger, which maintains secure data
sharing, privacy, and transparency. In addition, all digital twin
transactions based on blockchain will be registered and made
unchangeable without consensus.
F. CYBERSECURITY
In the Metaverse, data is vital for successfully creating
systems by businesses and applications. Due to the management of huge data flows, pervasive user interest profiling, and unequal AI algorithm outputs, the Metaverse
may be subject to several security vulnerabilities and privacy attacks. Data storage, data sharing, data portability,
data interoperability, and, most importantly, data security
and privacy are the fundamental functions of blockchain
in the Metaverse. The authentication and access control
mechanisms used by the blockchain, and its consensus procedures preserve user data privacy. Blockchain uses hash
techniques and asymmetric-key encryption to secure data
in the Metaverse. Moreover, the use of blockchain technology to develop a decentralized and transparent-over-domain
authentication method for industrial devices is being considered. This scheme will recognize trust between domains and
identity-based encryption for device authentication. Additionally, certain accurate domain information is encouraged
to be stored off-chain to reduce storage obligations in
the blockchain system. An execution of proof-of-concept
simulation confirms its reliability and practicability as a
consensus protocol in blockchain to ensure privacy protection. For data management security, blockchain guarantees
trustworthy data dissemination over Metaverse services, high
reliability of data sources, and accurate representation of
digital footprints.
G. CLOUD COMPUTING
In the Metaverse, services and systems are expanded to
their highest potential with the facilities provided by digital systems and real-time storage/processing capabilities on
cloud platforms. Blockchain techniques, specifically peer-topeer networks, enhance cloud computing-based storage and
the processing infrastructure to host Metaverse applications.
Edge computing must be used to allow access capacity along
with context, secure access control, and location awareness
features. Additionally, network slicing can coordinate and
build the Metaverse applications stream among all enabler
technologies.
H. MOBILE INTELLIGENCE
In the Metaverse, the mobile computing paradigm has
evolved by using advanced blockchain, AI, IoT, and 5 / 6 G
wireless communications, where distributed fog computing
and mobile edge computing (MEC) are merged within the
Metaverse platform. MEC drives computer-intensive assignment to the edge of the network and allocates resources as
close to the endpoints as possible to overcome the drawbacks
of mobile devices, which are limited storage space, high
latency, resource optimization, computation performance,
high data rate, and efficiency. Based on 6G networks, intelligent mobile devices can be readily networked to leverage
blockchain, AI, Metaverse edge computing, and other technologies for data examination and interaction and discharging
judgments that allow production to self-organize. In the
Metaverse platform supported by blockchain technology,
consensus mechanisms based on mining enhance the MEC
system’s security. In addition, the resource allocation problem
can be solved in polynomial time using blockchain technology. Research is therefore concentrated on blockchain-based
technologies in the future to address the problem of scarce
resources in MEC.
VII. METAVERSE APPLICATION BASED ON BLOCKCHAIN
CHALLENGES
Metaverse has enhanced human life by providing expediency
and social-economic development. Moreover, the advent of
the Metaverse improves social interaction from the perception of technical revolution and collaboration.
Blockchain provides vital techniques for Metaverse development and provision. The fundamental characteristics of
Metaverse are realism, hyper-spatiotemporally, sustainability, and heterogeneity. In contrast, implementing Metaverse
applications based on Blockchain faces numerous challenges,
which are addressed and explained in the following subsections.
A. SECURITY AND PRIVACY
In the Metaverse, users and professionals are concerned with
evolving Metaverse security, threats, and risks, which can
include Blockchain and smart contracts; decentralization;
fraud, phishing, and social engineering; identity theft and
cybercrime; privacy, compliance, and ethics; non-fungible
tokens; and AI incorporated with virtual and augmented reality.
Metaverse spaces are the most crucial areas of concern, and
they relate to the future security of property and privacy from
the perspective of the most related security technologies:
Blockchain security, IoT cloud services and big data security,
interactive technology security, AI security, and digital twin
security. In privacy, the most critical issue associated with
Blockchain in Metaverse privacy is the crisis of multiple
addresses. The system developer can create a cluster of all
addresses associated with the same user.
B. SCALABILITY
Since Metaverse is a comprehensive internet transition, scalability is a critical technical challenge for the platform.
An early implementation of the Metaverse presents a limited
number of successful participants. When more participants
access workplaces, the consequent uploading and downloading requests rise consistently. The Metaverse platform may
suffer from processing delay or bottleneck problems in this
case. Hence, the required bandwidth must be exceptional
to ensure the scalability of Metaverse through sophisticated
networking techniques that Blockchain can grant.
C. EDGE RESOURCES SHARING
In the Metaverse network, participants may interact with
the virtual world using VR and AR technologies. To access
the providers of Metaverse services currently, participants
use Metaverse local devices such as head-mounted glasses.
Nevertheless, using Metaverse local devices for computing
faces two main challenges: firstly, the limitations of these
devices’ computing and communication resources. Second,
the dynamic and constant movement of devices with the distribution of the local computing devices. Blockchain can fill
this gap and optimize resource sharing in Metaverse securely
and with transparency to help Metaverse users finish more
offloading tasks in time.
D. INTEROPERABILITY AND INCENTIVE COMPATIBILITY
The interoperability within numerous Metaverse applications, particularly when participants shift from one platform
to another, should be seamless to facilitate the partici
FIGURE 12. Metaverse as a services provider.
FIGURE 13. Diverse users in the metaverse system.
FIGURE 14. Data within the metaverse.
FIGURE 15. Blockchain’s impact on metaverse technologies.
pants’ engagement and enrich their experience. Besides, data
interoperability across virtual / augmented reality is limited because of the different environments in which they
are developed, which requires compatibility. When using
blockchain, a cross-chain protocol, it is promising to transmit
data between two or more blockchains housed in different virtual worlds. Because of the interoperability of the blockchain,
users may transition between different virtual worlds more
readily.
E. ACCESSIBILITY FOR DATA DEVICES AND NETWORKS
In contrast to the Internet, where access does not need specific
devices, Metaverse operators are required to use specific
devices such as a headset, contact lens, and glass for higher
interactivity in the virtual world, leading to significant limitations in accessibility. In the future, the accessibility in
Metaverse must evolve and be accomplished with unwearable
and in-service devices. Furthermore, interaction techniques
must be developed where users can feel, smell, and taste
in the virtual world rather than only hear or see. Network
accessibility is an additional potential barrier in the Metaverse network, as are the interfacing devices issues of the
Metaverse. Sufficient bandwidth must grow with the increase
of diverse participants’ platforms, applications contents, and
data.
F. SHARING DATA
Metaverse participants and applications collaborate and share
data on the same platforms. The data gathered from diverse
applications and different AR/VR and IoT devices in the
Metaverse will be utilized to generate personalized systems
tailored to participants’ activities. Furthermore, Organizations can perform data analytics across the Metaverse by
distributing information across applications. Shared data will
help recognize customers’ behavior, assess advertising, customize the content, establish creative strategies, and build
products in the Metaverse. Alternative prospects in sharing
data in the Metaverse include several applications like healthcare, traffic optimization, mass media, and games, which
will produce a real-time environment with a large volume of
data, requiring more flexible data sharing and manipulation.
Regarding this issue, blockchain techniques can play valuable
roles in data sharing within the Metaverse:
1. In all applications, transactions are transparent and
accurate. The transaction records are immutable and
decentralized and can only be seen by the participants.
2. The block owner will have comprehensive control over
the block information.
3. Data inspections and validation are easy and with low
cost and time when using the blockchain Hyperledger.
4. Blockchain heterogeneous smart contracts can generate flexible data sharing when all participants
autonomously agree and execute a particular transaction without the need for a third party, hence reducing
the transaction cost.
G. DATA STORAGE
Every participant login within the Metaverse automatically
creates a data file, which continuously enlarges and contains more and more data due to social interactions between
Metaverse applications. Massive storage is required as huge
amounts of data generated by members in real-time require
data processing and retrieving. Hence, Metaverse developers
must consider data storage to be a high priority. Metaverse’s
physical central digital data storage faces many challenges:
limitations of capacity, corruption, risk of loss, and damage,
as revealed especially in health care, gaming, IoT, etc. When
Metaverse transactions are completed through a decentral
TABLE 4. Case studies of metaverse applications aligned with blockchain roles and platform pillars.
TABLE 4. (Continued.) Case studies of metaverse applications aligned with blockchain roles and platform pillars.
ized blockchain, the time it takes to detect and tag data
will be lower. Meanwhile, blockchain serves as a cooperative platform for data researchers. In addition, data backup,
trustworthiness, transparency, and availability are guaranteed
when blockchain is applied.
H. LATENCY AND ENERGY EFFICIENCY
In blockchain, cross-chain protocol expansion permits data
interchange, improving Metaverse interoperability between
spectrum resources of edge networks and wireless devices.
Unfortunately, the energy resources of these devices are
restricted and prone to challenging resource allocation problems for VR and AR streaming services. Considering the
energy expenditure of blockchain is also vital for the Metaverse, specifically for the telecommunication ecosystem,
since 5G systems are tailored towards ultimate energy efficiency. Blockchain developers are undertaking immense
changes in the direction of a significantly more efficient
technology solution, mainly in the mining and validation
methodology, which consumes energy. Also, a shift from simple averaging to fine-grained analysis is required to address
distribution and quality of service (QoS) issues among heterogeneous users in the performance analysis and optimization
of all Metaverse technologies, including AI, IoT, digital
twins, and extended reality, which are energy harvesters.
VIII. FUTURE RESEARCH DIRECTION
Future research can investigate deeper into scalability
solutions for blockchain-based Metaverse platforms. This
includes exploring innovative consensus mechanisms and
layer-2 solutions to ensure the efficient processing of a growing number of transactions and assets.
Interoperability challenges in the Metaverse can be overcome by developing standardized protocols that allow seamless asset transfer and communication between different
virtual worlds or platforms.
More extensive studies focused on edge computing and
resource-sharing techniques need to be conducted in order
to significantly increase the efficiency of Metaverse applications and reduce user latency. Conventionally centralized
cloud infrastructures are facing issues from the increasing
need for these immersive virtual environments. Edge computing is a significant way to address this problem since it
allows for more effective processing power deployment in
the Metaverse by putting it near end users and applications.
Edge computing in the Metaverse reduces latency and data
transit times by locating processing resources adjacent to
users, making the user experience responsive and seamless.
More advancements in AI, VR, and AR technologies
promise to enhance user experiences and virtual environments. These technologies will integrate AI algorithms with
VR and AR systems, creating more immersive and adaptive environments. AI-driven predictive systems and machine
learning could enhance VR and AR content creation. Future
research can focus on reducing computational requirements
and developing AI models for high-fidelity VR and AR
experiences. These technologies could be applied in various
domains, including education, entertainment, healthcare, and
training simulations.
Interdisciplinary collaboration between blockchain, VR,
and AI experts is crucial for creating a unified Metaverse.
This approach involves pooling knowledge from various
fields and establishing shared standards, protocols, and
frameworks for seamless interoperability. This approach can
drive advancements in AI algorithms, blockchain-based security, and immersive virtual experiences. It also involves
developing ethical and regulatory frameworks to ensure user
safety and privacy in the Metaverse.
For blockchain networks to be more sustainable in Metaverse applications, research must address the significant
energy consumption and environmental effects of these networks. The main goal is to figure out how to lessen the carbon
footprint that comes with blockchain technology. The goal
is to increase the energy efficiency of blockchain networks
by using novel algorithms, protocols, and hardware optimizations. Developing environmentally friendly and scalable
solutions for blockchain integration within the Metaverse
entails investigating consensus processes, data storage techniques, and computation algorithms. These initiatives aim to
minimize the environmental impact of blockchain technology
while supporting the long-term survival of Metaverse networks.
The investigation of how blockchain-based Metaverse platforms might transcend digital realms and transform a range
of industries is explored through the integration of these
platforms with real-world applications. The goal of research
is to determine how blockchain technology in the Metaverse
may be applied in real-world contexts to industries including entertainment, healthcare, and education. This entails
creating protocols and systems that allow for safe and decentralised data management, authentication, and transaction
procedures. The objective is to develop interoperable systems
that take advantage of the immutability and transparency
of blockchain technology to enhance security, privacy, and
trust in practical applications. Blockchain, for example, can
be used to safeguard patient data in healthcare and validate
credentials in education. It can verify the digital ownership
of assets in the entertainment industry. The study investigates these uses to highlight the possibilities of a numerous
blockchain-based Metaverse platforms to revolutionize of
industries, fostering an environment of innovation, transparency, and trust.
IX. CONCLUSION
Blockchain technology promises to reshape the development
and administration of virtual realms within the Metaverse.
Its role in creating a secure, decentralized infrastructure is
pivotal in fostering transparency and facilitating the seamless transfer of virtual assets and transactions among users.
In doing so, it addresses various challenges associated with
managing the Metaverse, including digital asset tracking,
privacy safeguarding, and security reinforcement. As the
blockchain-based Metaverse continues to evolve, there is a
growing need for research and innovation to address critical
concerns such as scalability, interoperability, and the efficient
allocation of edge resources.
Given the ongoing communication, computational needs,
and security challenges of metaverse development, we have
reviewed the latest advancements in blockchain and intelligent networking. The Metaverse must have a reliable
and trustworthy network to seamlessly bridge the virtual
and physical worlds. Hence, our investigation explores the
advantages of merging blockchain and intelligent networking
within the Metaverse. The goal is to unify the physical and
virtual domains, establishing a more reliable, secure, and
effective environment to deliver users an immersive experience. Finally, we presented the research gaps preventing
blockchain from becoming a significant innovation in the
Metaverse. The current focus in research circles involves
advancing blockchain technology and its application in the
Metaverse to elevate overall living standards. Despite the
ongoing efforts to employ blockchain in sustainable Metaverse initiatives, numerous challenges and limitations persist,
demanding further investigation and resolution.
COMPETING INTERESTS
The authors declare no competing interests within the last
three years that could be perceived as influencing the work
submitted to Applied Intelligence journal.