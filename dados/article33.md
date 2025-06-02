Title: The Impact of Integrating Information
Technology With Operational Technology in
Physical Assets: A Literature Review

ABSTRACT The convergence of information technology (IT) with operational technology (OT), within
physical assets can enhance performance but also presents challenges due to higher performance expectations
and increased complexity. This study reviews the research that has been conducted to address these
convergence and integration challenges by using an in-depth review of academic papers, industry standards,
and reports published during the last three decades. Our investigation reveals that about a third of the
existing IT/OT research really focuses on the convergence of IT/OT, by including organizational aspects
into the study. Three key research domains were identified: maintenance, cybersecurity, and configuration
management. The introduction of IT in assets has necessitated changes in maintenance practices, as current
approaches are not suitable for these converged lifecycles. Cybersecurity risks have received the most
attention in the IT/OT domain. The integration requires the management of these changes; therefore,
configuration management has become more crucial than it already is to keep of actual configuration of both
the IT and the OT parts of the asset. This research hereby provides relevant observations for practitioners in
industry and academics in the IT and the physical asset management domain. The identified gaps suggest
the need for tools and methods to better align IT and OT standards, policies, tools, processes, and people
throughout the lifecycle of an IT/OT converged physical asset in a sustainable way.
INDEX TERMS Asset management, maintenance management, maintenance engineering, systems integration, critical infrastructure, software maintenance, configuration management, fault diagnosis, industrial
cybersecurity.

I. INTRODUCTION
Originally, physical assets consisted of physical electromechanical systems. In the last three decades, these systems
are often controlled by operational technology (OT) [1]. The
next step was the introduction of information systems (IT)
into these assets. Initially, these IT systems were used as an
addition to these assets, not impacting the availability of the
asset. However, with IT being increasingly entwined within
an asset, managing this IT integration becomes key. The
integration of IT is different from the integration of physical
or OT systems as IT consists of software and hardware for
information processing [2] which is different from controlling
physical processes. The focus of IT is on confidentiality,
integrity, and availability [3], whereas the focus of OT is on
safety and reliability. The OT that controls assets are also
known as ‘‘industrial control systems’’ (ICS) [3]. The differences between IT, OT and Physical systems are depicted in
Fig. 1. In this research when we talk about IT/OT converged
assets or systems we talk about assets that consist of all
three domains depicted in Fig 1. Furthermore, we view IT/OT
converged systems from a mechatronic perspective and see
them as a specific type of Cyber-physical system (CPS) [5].
This originates from Hehenberger [4], who describes that
mechatronic systems can evolve into CPS and eventually into
the Internet of Things (IoT). Notably, Bricogne et al. [6]
observe that mechatronics and CPS communities have limited
interaction but are both looking at the same thing from a
different perspective.
There are several benefits of this IT/OT integration, such as
improved performance, and lower costs [4]. System integration plays a role in several domains we have scoped system
integration specifically to IT/OT integration on large systems
and assets e.g., in railways, critical infrastructure etc. with an
industrial application where the focus is on the effects of the
integration in the physical system.
In this research, the following definitions are used:
IT/OT Integration: Focuses on bridging the gap between
IT systems (business processes, data analysis, etc.) and OT
systems (industrial operations, real-time control, etc.) within
an organization [5].
IoT: Involves creating a broad network of interconnected devices that can operate across various domains
and industries, extending beyond a single organization’s
boundaries [6].
FIGURE 1. Difference between IT, OT, and physical systems.
IT/OT converged systems have become more complex with
the introduction of IT in OT [7]. Therefore, traditional maintenance approaches aimed at managing OT do not always
fit digital problems. Moreover, the lifecycles of IT and OT
typically do not match. As a physical asset often has a lifecycle of multiple decades, an IT system is often replaced
after a few years [8]. Al though the lifecycle stages of IT and
OT might appear similar, they have two differences. Firstly,
the software part of IT has no formal ‘production stage’,
and instead quality assurance is essential [9]. Secondly, the
software part of IT evolves during the deployment and maintenance phase, while physical assets need maintenance to
counteract physical degradation [10]. Managing assets during
the various stages of their life cycles is known as physical
asset management. The objective of physical asset management is to optimize the usability and value of assets while
minimizing risk and cost, which is recorded in the standard
ISO 55000:2014 [11].
Although much has been written on IT/OT convergence,
to the best of our knowledge, no specific review has been
conducted on the integration of IT systems within OT systems
in physical assets. This research was used to identify and
group existing research gaps. Therefore, his research aims
to understand the specific challenges of IT/OT converged
systems through a literature review and to offer insights
into how to better manage the challenges that arise when
integrating IT within OT environments. In this review, the
data collection was performed using (amongst others) published peer-reviewed journal articles, industry guidelines and
standards.
II. METHODOLOGY
A. RESEARCH OBJECTIVES
This research aims to answer the following research question:
How can the impact of integrating IT systems within physical assets over their lifecycle be defined based on a literature
review on managing distinct aspects of IT and OT?
Consequently, the specific objectives of this research
are understanding the main challenges and differences in
managing IT and OT and defining the concept of ‘Asset
Management of IT/OT converged systems’.
B. RESEARCH MATERIALS AND METHODS
In this research, the studies were reviewed using a five-step
process depicted in Fig. 2. The first four steps are based on
the work of Seuring & Müller [12]. These steps have been
extended by adding a fifth step for making observations based
on the work of Garg & Deshmukh [13].
FIGURE 2. The research process that is adapted from Seuring and
Müller [12] and Garg and Deshmukh [13].
The following four search boundaries are used within this
research:
1. Keywords: The following keywords were used: ‘physical asset management’, ‘literature review maintenance’. After scanning and reading the initial
results closely, the following keywords were added:
‘cyber physical systems’, ‘IT/OT’, and ‘operational
technology’.
2. Database: This research was conducted using several databases, namely Google Scholar, Science Direct,
IEEE Xplore, ACM Digital Library, Web of Science
and Scopus. References cited in the relevant papers
were used to find related materials and perform backwards snowballing [14].
3. Analysis: This analysis uses (conference) papers from
scientific journals, dissertations, and theses, with a
focus on maintenance, engineering, and interfaces
within the domains of IT and OT. Interesting insights
are also emerging within the corporate domain. Therefore, several industry studies (e.g., whitepapers) and
industry standards are included in this research. This
type of inclusion of non-academic sources is supported
by a study by Dowdeswell et al. [15]. No restrictions
were placed on the date of publication when selecting
the studies.
4. Exclusion criteria: Studies, which only dealt with
in-depth mathematical modelling and software were
not within the scope of this research, it focusses not
only on technical aspects but also on organizational
ones. If the materials make bold claims about solutions,
but in practice only show problems with IT/OT convergence and give no solutions, they are excluded from the
review. Last, studies that did not fit within the content of
the specific section were excluded after a close reading
of the study.
This review investigates the trends within IT/OT converged
systems and their practical implications for managing them.
In each subsection of the results, a comparison between
IT/OT and OT will be made in the form of a table. At the
end of each results section observations will be presented.
III. RESULTS
Initially, 252 studies published till 2024 were identified using
the selected keywords mentioned above. 139 studies were
excluded based on the exclusion criteria. This brings the total
number of studies included in this review to 113. The database
containing the selected studies can be accessed via an online
data repository, see Kok [16].
The first study in this review was published in 1985 and is
about the management and maintenance of software systems.
This first study does not discuss IT/OT, but the software
management idea discussed here has many similarities with
the asset management of OT assets. With the introduction
of Industry 4.0 in 2010, research on these topics started to
emerge, and the scientific community became more interested in it. In 2012 the concept of IT/OT convergence was
introduced in a whitepaper by Chemdupati et al. [17]. Since
2015 the number of yearly publications within this field has
been steadily increasing, see Fig. 3. Four individual studies,
related to the history of IT/OT have been left out from Fig 3,
to increase the readability of the figure.
In Fig. 4 the distribution by source of the publications
can be found. In this figure, the category ‘‘other’’ represents
sources such as industry standards.
FIGURE 3. Distribution of reviewed publications by year, from
2003 onward.
FIGURE 4. Distribution of studies according to source.
We have classified the different studies into four distinct
categories.
1) IT only study, when the study is about IT-related
aspects.
2) OT only study, when the study is about OT-related
aspects.
3) IT/OT study, when the study is about IT and OT-related
aspects.
4) Others, who do not fit in the above-mentioned categories e.g. studies on knowledge management
FIGURE 5. Classification of studies in the review into the topics of IT, OT,
or IT/OT.
The high percentage of IT/OT studies in Fig 5 shows that
there is a lively debate on IT/OT convergence and that the
community is recognizing the struggles that are posed by this
convergence. However, only 29% of studies investigate how
IT/OT convergence affects processes and organizations. Most
of the studies focused on the technical requirements for IT/OT
convergence and often on a single issue, such as cybersecurity
aspects.
The differences between IT and OT lifecycles present
various challenges to be overcome to ensure the long-term
successful operation of IT/OT converged systems [18], [19],
[4], [20], [21]. Based on these challenges we identified three
key domains.
The first domain that we identified in the integration of IT
with OT in physical assets through this review is maintenance.
To ensure the performance and safety of an asset over its
lifetime, maintenance is essential. Therefore, maintenance
practices have evolved from unavoidable to a strategic concern [22]. Consequently, these maintenance practices need to
evolve due to IT/OT convergence [23].
The second domain in the integration of IT with OT in
physical assets is cybersecurity; in recent years, there have
been numerous cybersecurity incidents, which have often led
to financial and information losses. However, the effect of
cyberattacks on IT/OT systems is much more severe than
on IT assets since they can lead to physical injuries and
even casualties [24]. This makes cybersecurity one of the
main challenges during the lifecycle of an IT/OT converged
system, as pointed out by Corallo et al. [21].
The third domain in the integration of IT with OT in
physical assets is configuration management; to keep up with
changes in assets, configuration management is essential.
It provides traceability so that the locations of components,
systems and software are known [25]. Additionally, as IT/OT
convergence increases, so does the need for configuration
management, due to shorter development times and greater
product flexibility [26]. Unfortunately, the integration of configuration management practices of IT with those of OT
remains difficult [27].
The three domains above will be discussed in further detail
in the following subsections, see section A for maintenance,
section B for cybersecurity and section C for configuration
management.
A. MAINTENANCE
1) DIGITIZATION OF MAINTENANCE
During the operational phase of an asset lifecycle, maintenance of both the hardware and the software is needed for the
systems to continue to fulfil their functions. For hardware,
maintenance is needed to keep up with degradation [28].
Several differences influence the maintenance of OT and that
of IT systems, Table 1.
Maintenance practices can be improved due to IT/OT
convergence, because the added connectivity can add functionality to predict/report possible failures. This reduces the
need for corrective maintenance, which in return can increase
uptime and minimize energy and material consumption.
[28], [30]. So, to improve maintenance practices digitization
TABLE 1. Maintenance - differences between IT, OT, and IT/OT, adapted
from Pintelon & Parodi-Herz [22], Silvestri et al. [23] and Titu &
Stanciu [29].
of maintenance is needed, where remote monitoring and
the management of assets is made possible [31]. Unfortunately, within the industry, there are many older systems
without remote monitoring possibilities. Diaz-Elsayed et al.
[32] argue that with limited investments, legacy hardware can be retrofitted so that remote monitoring becomes
possible. Likewise, Sanchez-Londono et al. [33] provide
a review of performance, risk, and cost optimization of
assets by retrofitting legacy devices with remote monitoring
capabilities.
Digital maintenance concepts can support this digitization
process. Roda and Macchi [34] provide an overview and the
differences between such maintenance concepts and conclude
that these concepts will lead to better asset performance
and lower costs. Using information from the manufacturing
execution system (MES) is another way to improve maintenance activities as Skrzeszewska and Patalas-Maliszewska
[35] shows. The downside of this digitization is that the
maintenance practitioner’s role is becoming more difficult
since not all traditional OT maintenance principles can be
used in the IT/OT converged domain [18]. High level design
principles for IT/OT convergence can help in overcoming this
difficulty [36]; however, further work is needed to apply these
ideas in an systems integration setting. Finally, Kuusk and
Gao [37] suggest asset management companies to prepare
for IT/OT integration in four steps, beginning with IT/OT
convergence. In the next section, we will look at how the
introduction of software affects maintenance.
2) SOFTWARE MAINTENANCE AND PERFORMANCE
PREDICTION
On IT/OT converged systems not only the hardware needs
maintenance but also the software part. However, software
faults mostly occur due to defects that were introduced during
the development phase [38]. This is in contrast with hardware
faults, which often happen due to degradation [28]. In the
1970s the necessity of software maintenance was described
by Lehman and is summarized in ‘‘Lehman’s Laws of Software Evolution’’ [39]. One of the main points of this work
is that a software program cannot be fully specified, because
software requires constant evolution after it has been released.
Which is different from hardware design, which can be fully
specified.
Dvorak presents recommendations for software design
when integrating IT systems within assets and shows that
cultural aspects are hindering the implementation of these
recommendations [40]. However, Osborne [38] states that
software maintenance is frequently disregarded and managing the maintenance of software is a much broader practice
than correcting errors. A thorough overview of the challenges around software maintenance is provided by Grubb
and Takang [41].
Next, Koziolek [42] provides an overview of the characteristics of software architectures and explains that to maintain
and develop long-lasting software systems, a software architecture is required. Then, Wong et al. [43] provide an
overview of lessons learned from software bugs on software
failures. Interestingly software failures are often discovered
accidentally and usually resolved with troubleshooting e.g.,
by a system reset, instead of an in-depth investigation [44].
To counter software failures source code defects are often the
place to start, however, timing, configuration and the environment of the system are a much bigger source of software
failures in practice [45].
Due to the increased complexity of IT/OT converged systems, it is important to be able to predict the performance that
includes both the software and the hardware aspects of an
IT/OT converged system. During the development of physical assets, the Reliability, Availability, Maintainability, and
Safety (RAMS) methodology is commonly used to achieve
safe and reliable operation [46]. This OT approach to reliability evaluation, where failure modes are calculated along with
their probabilities, does currently not automatically include
IT/OT components [47].
However, there are examples of OT tools that do include
software. First, Carlson [48], suggests that software aspects
can be included in traditional failure mode and effect analysis
(FMEA) analyses. Second, Oveisi and Ravanmehr [49] suggest evaluating the software component of an IT/OT system
using both a software fault tree analysis (FTA) and software FMEA. Third, Medikonda and Ramiah [50] suggest
combining FTA and FMEA techniques to improve the fault
removal process of the software for systems that include
both hardware and software components. They point out that
these two methodologies are complementary to each other
and are compatible with existing system-level techniques.
Last, Zúñiga et al. [51] show that a traditional FMEA can be
used on an IT/OT converged system, however modifications
to the method seem necessary to improve risk prioritization.
To overcome this, Tafur et al. [52] suggest combining FMEA
with AutomationML, were the AutomationML is used to
model the digital components of a system. In the next section,
the effects of digitization on failure diagnosis are studied.
3) FAILURE DIAGNOSIS
During the life cycle of an asset, failure diagnosis helps
in finding the root causes of problems; however, as assets
become more digitized, finding faults becomes more difficult
as multiple faults can lead to similar symptoms. This was
observed by Kavulya et al. [53] who present an overview
of automated fault diagnosis techniques for industrial applications. Dowdeswell et al. [15] present a very thorough
overview of fault detection and diagnosis techniques of
industrial cyber-physical systems. It is important to note
that ‘‘cyber-physical interactions can yield unpredictable
cross-system failure propagations’’ [54, p. 3]. Thus, good
failure diagnosis is essential to discriminate between failures
originating from the IT part of the system and the physical
part of the system.
So, newly developed model-based and data-driven fault
diagnostics have proven to be effective in identifying faults,
not only in laboratories but also in real-world environments [15]. However, these models can only work correctly
if they are trained with correct dat. Herzig et al. [55] examined more than 7000 reports and show that 39% never
had a bug. This introduces bias in bug prediction models.
As always preventing faults is better than correcting them,
and this can be done by using prognostics, which involves
predicting emergent failures [56]. Failures of software within
IT/OT converged systems are still understudied as shown by
Amusuo et al. [57]. In the last section, we will look at the
organizational effects of this digitization of maintenance.
4) ORGANIZATIONAL ASPECTS
Simões et al. [58] provide a literature review into the performance of maintenance practices, they state that not only
technical but also organizational aspects should be monitored.
Then Villar-Fidalgo et al. [59], also point in this direction
as they state that the increased connectivity between assets,
plants, and processes will result in more stakeholders needing
to be managed and changes in the training of personnel are
needed. Similarly, Bhatia and Kumar [60] demonstrate that
companies that want to combine IT and OT should prioritize
cooperation and teamwork. Makama and Telukdarie [61] propose an approach to improve the asset lifecycle management
of an asset by improving the usage of data from these assets,
it is essential that this approach is aligned with the goals of
an organization.
Filz et al. [62] suggest that maintenance personnel can
be employed more effectively by using a real-time failure
mode and effect analysis (FMEA) to optimize maintenance
planning. The main advantage of this approach is that risk
assessment is no longer subjective. Similarly, He and Jin [63]
indicate that by combining Industry 4.0 and CPS, it should
be possible to create a self-organizing and self-maintaining
production system, however, this is a costly solution which
is only attainable for a handful of companies. However,
as Temelkova [64] shows CPS and IT/OT converged assets
are not the same, for example, a CPS consists often of an asset
and a digital twin of this asset.
Therefore, they suggest that investing in human and organizational aspects seems more favorable. Next to organizational
aspects Jantunen et al. [65] give an overview of technologies that can improve maintenance practices. Within this
overview, they also identify several other non-technical barriers that hinder the implementation of available technologies
e.g., uncertain return on investment.
5) OBSERVATIONS
By studying the literature on maintenance, several observations can be made that should be considered by the scientific
community and industry.
1. Digitization: IT/OT convergence can improve maintenance performance. However, the role of the maintenance practitioner is becoming more difficult as
traditional maintenance practices cannot always be
applied to IT/OT converged systems.
2. Performance prediction: Tools are necessary to predict
the reliability of IT/OT converged systems. Traditional
OT tools do not include software and the nature of
software faults is different from hardware faults.
3. Failure diagnosis: Failure diagnosis of IT/OT converged systems is only possible when a distinction
can be made between failures originating in the IT or
the OT components. More focus should be placed on
preventing failures, as failure diagnosis becomes more
complex due to the increasing complexity of IT/OT
converged systems.
4. Organizational aspects: The literature strongly focuses
on the technical aspects of asset digitization but indicates that organizational aspects also require attention
due to the increased interconnections between systems
and assets.
B. CYBERSECURITY
Cybersecurity refers to a set of techniques used to protect the
integrity of networks, programs, and data from attacks, damage, or unauthorized access. These techniques have received
increasing attention in recent years, due to the increasing
digitization within society and the growing convergence of
IT with OT systems [66]. There are cyber threats specific to
IT and OT. Combining IT and OT in an asset exposes the asset
to the risks of both, see Table 2.
Therefore, IT/OT converged systems have a higher risk of
suffering from unexpected failures due to increasing software
and cybersecurity incidents [67], [68]. Industry guidance on
how to control this risk can be found in a publication by
Stouffer et al. [69]. However, a collective understanding and
a standard principles on IT/OT converged system security
seems to be absent [70]. Preventing these failures can be done
by simulating cyber-attack and defense strategies by using
digital twins, which are a representation of the real world in
the cyber world [71]. The weak point in an IT/OT converged
system is the link between IT and OT [72]. Kanamaru [73]
shows that engineering measures are crucial to protect physical assets and that IT security measures are insufficient on
their own.
TABLE 2. Cybersecurity - differences between IT, OT, and IT/OT, adapted
from Sonkor & García de Soto [24].
In dealing with these increased cyber risks of IT/OT converged systems prevention is important, as described in the
next section.
1) PREVENTION
In the prevention of cyber security incidents within IT/OT
converged systems, several aspects are important. First,
Alladi et al. [74] recommend monitoring and improvement
of security practices to protect against cyber-attacks. Second,
Khan et al. [75] make the case that current cybersecurity
approaches are insufficient to protect IT/OT converged systems. Third intrusion detection using machine learning is a
current research trend in providing a partial solution to cyber
risks [76]. Besides the technical aspects of preventive action,
companies need to have an organizational culture dedicated
to cyber-security which should ensure that the company is
continuously learning about aspects of cybersecurity.
Interestingly most of the studies on cybersecurity within
the IT/OT context have a focus on the IT side and lack
managerial perspective [77]. Alladi et al. [74] underline this
by providing an overview of several major cybersecurity incidents which occurred during the last two decades on existing
OT assets and show that only 28% of organizations that had
security incidents believe that preventing cyber-attacks is to
be of high importance. This, as Annareli et al. [78] points
out, is not how it should be as cybersecurity should be at
the organization’s core even more so for IT/OT converged
systems. Nafees et al. [79] also emphasize the importance
of human factors in achieving cybersecurity. Stouffer et al.
[69] underline this by calling for a proactive collaboration
between operators, OT engineers and management. Last, also
Ani et al. [80] stress that the security of IT/OT integrated
assets can only be achieved with a combination of people, process, and technology factors. Next to these factors,
modelling can help in providing cybersecurity for IT/OT
converged systems as pointed out in the next section.
2) MODELING
An overview of several important research areas of the current
research on CPS security is provided by Alguliyev et al. [20].
One of these research areas is the modelling of CPS attacks.
To defend an asset against a cyber-attack it is essential to
understand how adversaries attack. Therefore, these models
can be used to better understand this. For example, Assante
and Lee [81] provide a model that helps defenders within the
industry to understand a hostile cyberattack strategy.
A specific case of modelling is the identification of cyber
risks, several authors have proposed frameworks for practitioners to help them manage those risks [82], [83], [84],
[85]. Although these frameworks were not developed with
IT/OT converged systems in mind, they are a useful place
to start because they were developed by practitioners. A step
towards IT/OT converged systems cyber risk management is
proposed by Kriaa et al. [86], in which a traditional failure
mode analysis is combined with a threat and vulnerability
assessment to minimize the impact of a cybersecurity breach.
A promising suggestion is made by Schmittner et al. [87]
who propose an FMVEA, which extends a traditional FMEA
analysis by including a vulnerability analysis.
3) OBSERVATIONS
By studying the literature on cybersecurity, three main observations can be made that should be considered by the
scientific community and/or industry.
1. Digitization: Increasing IT/OT connection leads to
more complex systems that pose a higher risk of
unexpected failures due to software and cybersecurity
incidents compared to unconnected systems.
2. Organizational culture: In addition to the technical
aspects, companies need to have an organizational culture dedicated to cyber-security which should ensure
that the company is continuously learning about aspects
of cybersecurity.
3. Models: Models can be used to increase understanding
of the risks and effects of cybersecurity incidents of
IT/OT converged systems.
C. CONFIGURATION MANAGEMENT
The configuration of an asset is the combination of the
requirements, architecture, and specific implementation of
these aspects into the actual system or asset [88]. Configuration management (CM) consists of several distinct steps:
planning, identification, change control, status accounting
and configuration audit [89], [90], [91], [92]. Managing
all this information during system development becomes
increasingly important and more difficult since multiple disciplines need to work together, as Capilla et al. show [93].
However, the different tools that support CM of IT and that
of OT do not match. There are two main differences between
those tools. First, OT CM tools focus on the production phase
whereas IT CM focuses on the development phase [94]. Second, IT CM tools need to be able to deal with more changes
as software is easier to change due to its digital nature [95],
[96]. Table 3 provides an overview of the differences between
the configuration management aspects of OT and IT.
TABLE 3. Configuration management - differences between IT, OT, and
IT/OT, adapted from Krikhaar et al. [26], Cline [25] and Barrios et al. [27].
In the case of IT/OT converged systems, the tools supporting configuration management should become more
integrated [94], [97]. To support this CM/SCM integration
harmonization and further development of existing industrial
standards are needed [98] and, requirements should be formulated to guide this development process [99]. Unfortunately,
this challenge is broader than the field of configuration management since it requires cross-sector collaboration between
the fields of IT and OT [100], [101].
However, this is not an easy task as Kuusk et al. [102]
emphasize that the IT and OT teams should work together
to deal with these integration problems. As this integration
can be difficult, Poliński and Ochociński [103] suggest that
partnerships between industry and educational providers are
needed. Along these lines, Roda and Macchi [34] suggest
that new interdisciplinary forms of education are required
to achieve and sustain the necessary level of knowledge to
maintain IT/OT converged systems. Last, traceability and
reuse of knowledge are crucial components for executing
shared design between OEM and supply chain partners within
the system integration context [104]. The next section will
discuss the importance of architecture to be able to keep track
of the configuration of an IT/OT converged system.
1) ARCHITECTURE
An architecture is a graphical representation of different (software) components of a system, and how they interact [105],
[106]. This architecture helps to manage the configuration of
a system during design and operation. Moreover, to develop
an electromechanical system, a set of requirements must be
fulfilled. However, in the development of large systems, like
IT/OT converged systems creating and maintaining an architecture is essential [106], [107], since IT becomes the core
of the system. Therefore, architecture becomes important to
manage the configuration and different architectural models
can be found in the literature to manage such architecture.
Multiple of these architectural models are created from
the IT or software perspective, where limited attention is
paid to the OT or hardware layer, such as [108], [109].
Others do include a hardware layer but mostly focus on the
different software layers [110], [111], [112], [113], [114].
One of the main challenges for IT/OT converged systems
is how to manage all those different layers, not only the
software layers but also the hardware layers. So that they
continue functioning during operation, especially when systems are interconnected. Therefore, Cardin [115] creates a
model which identifies two layers: In the first layer the IT
is clustered and in the second the OT is clustered, including
the hardware itself. Last, Nakagawa et al. [116] find that
interoperability and legacy industrial systems are not well
represented in the current body of literature. To achieve interoperability interfaces between the various parts are essential.
Therefore, in the next section, the importance of interface
management will be highlighted.
2) INTERFACE MANAGEMENT
An architecture consists of different elements connected via
interfaces. Francalanza et al. [117] state that interfaces form
the main challenges when designing the physical side of an
IT/OT converged system. Carlson [48] underscores this by
arguing that 50% of the problems within systems occur at
an interface. This generates a need to implement some type
of interface management approach. Davies [118] emphasizes
this and states that interface management is an essential
element of engineering systems. When building upon the
architecture, these interfaces need to be managed during
the subsequent design phases. Blyler [119] provides a general overview of how to design interfaces, and how to use
technical performance measurement as a tool for managing
interfaces during these phases. As this does not necessarily work for IT/OT converged systems, David et al. [120]
propose an architecture for the integration into existing production environments which includes physical, human and
data interfaces. Yasseri and Bahai [121] propose a more
cost-effective and efficient process method for interface management design, which involves decomposing the system
into subsystems and mapping the dependencies between
systems.
The methods mentioned above focus on the technical
aspects of managing interfaces. Penas [122] observes that not
only the physical interfaces should be considered, nonetheless it should also be considered that the organizational
aspects of interfaces are important. For example, there should
be a mutual understanding between system designers of
the implications of data when it is exchanged between
systems or software components [123]. When systems are
designed, the governance of these systems becomes important since data is the backbone of an IT/OT converged system.
Yebenes Serrano and Zorrilla [124] provide a data governance architecture for these types of systems. Kuusk [125]
emphasizes that holistic data governance is necessary for
successful IT/OT convergence, which can be regarded as one
of the building blocks for IT/OT asset management. Lastly,
Kääriäinen [126] underscores this by demonstrating that the
difficulty of CM practices increases during the lifecycles of
large, multisite hardware/software systems; they stress that
interface management is crucial in the development of complex systems.
3) OBSERVATIONS
Several observations can be made based on the studied literature on configuration management that should be considered
by the scientific community and/or industry.
1. Tool integration: CM of OT and CM of IT practices
have some essential differences. For example, the focus
on the production phase within OT CM tools. In case
of IT/OT converged systems, these OT and IT CM
practices and tools need to be integrated.
2. Architecture: Due to IT/OT convergence IT becomes
increasingly the core of the system, making good architecture more important for reliable performance.
3. Interfaces: During the operational phase of an IT/OT
converged system, interfaces need to be managed.
4. Organizational aspects: With the addition of IT to the
OT teams, the organizational and cultural aspects of
CM are increasingly important in addition to technical
ones.
IV. DISCUSSION AND RESEARCH GAPS
In each of the results sections, IT and OT development are
compared using the insights gained from the literature, see
Table 4 for an overview. The table shows that there are several
differences in managing IT, OT, and IT/OT systems.
TABLE 4. General observations - extended comparison between
managing IT, OT and IT/OT systems based on the observations from the
results sections.
This review investigated three key domains that require
attention when aligning IT/OT converged systems. First,
maintenance practices change since the lifecycles of IT and
OT do not necessarily match. This mismatch in lifecycles
needs to be effectively managed by the different responsibilities (operations, maintenance, financial etc.) within an asset
management organization. Therefore, asset management of
IT/OT converged systems should be seen as a specific subgroup of these physical assets that are interconnected using
IT components.
Second, these assets are prone to more failures because of
increasing software and cyber risks. Due to those risks, there
is increasing research interest in cybersecurity. Moreover,
the failures of IT systems are less visible than failures of
OT systems since failures of OT systems often give visual
feedback to the mechanic. This increases the severity of the
failures increasing the systems’ criticality which potentially
reduces the availability of these systems [127]. In addition,
the interconnection between IT and OT is a source of failures
and these failures are also often more resource-intensive to
diagnose [128], which also reduces the availability of these
systems.
Third, a system’s configuration management is changing
as IT becomes more dominant within the system, requiring
additional different configuration management. For example, architecture becomes even more essential to integrate
a system into an asset, for such an architecture technical
constraints and system performance criteria are key input
characteristics [129]. Therefore, research on configuration
management has received a focus on tools that support the
practitioner in managing the configuration of an IT/OT converged asset over its lifecycle.
Finally, more attention needs to be paid to organizational aspects, instead of focusing on technical aspects. For
example, managing the addition of IT within an OT team,
since the OT and IT departments have diverse cultural values [66], [130] and focus on improving the communication
between the different departments within an organization.
These results are consistent with the findings of several other
researchers who have indicated the need for more attention
to be paid to non-technical aspects of digitization, see for
example Annarelli et al. [78] or Sanchez-Londono et al. [33].
A. TAKE HOME MESSAGE FOR PRACTITIONERS
Three major takeaways for practitioners working in an industrial environment can be derived from this research.
1. Maintenance of IT/OT converged systems requires a
more mature digital organization to be able to diagnose and maintain these IT/OT converged systems.
Because part of the system’s performance is determined
by parts hidden from view. This requires specialized
data and monitoring to get insight into how the system
is performing and where to look in case of nonperformance. Considering that introducing IT elements
into a physical asset makes maintenance more difficult,
it can be argued that there should be more consideration on the necessity of these new or added digital
functionalities.
2. Cybersecurity is an emerging topic as risks of possible cyber events on IT/OT converged assets need
to be managed. To deal with these risks performance requirements on cyber aspects must be created
during system development, together with a validation plan that clarifies when required performance is
met.
3. The maintenance and configuration management of
an IT/OT converged system needs constant attention.
As opposed to OT & physical systems, IT is not static
and is constantly under development. Therefore, not
only should there be attention to the technical systems
integration, but management should also be aligned
with this integration. However, traditionally, IT and
engineering professionals come from different siloed
environments. It is needed to improve the understanding of each other’s views and interests in managing and
developing these converged systems.
B. IDENTIFIED GAPS FOR FURTHER RESEARCH
Even though we expected that the review would also find
studies relating to current social research themes, some topics
are missing or absent in this specific field. First, the maintenance processes around IT/OT converged systems impact
sustainability, both by the performance of the maintenance
itself and, by the effect of the maintenance on the product to
be maintained [131]. Moreover, Maletič et al. [132] show that
physical asset management can improve the social and environmental performance of companies. Also, Soori et al. [133]
state that sustainability involves using advanced technologies
while promoting social responsibility and minimizing impact
on the environment. However, sustainability is not a priority
that emerges from the review. During further research, the
effects of IT/OT convergence on sustainability can be investigated. Since digitization can increase the environmental
footprint.
Second, the lifecycle value, including financial, aspects of
managing IT/OT converged systems did thus far not seem to
play a role within the identified literature. Within the practice
of managing assets over its lifecycle, however, economic, and
commercial impact are important aspects [134].
Third, the primary focus of this research is on the physical
integration of IT/OT in assets; when it comes to integration,
topics like artificial intelligence (AI) and machine learning (ML) are not yet widely discussed in the maintenance
and configuration management domain. Within cybersecurity, there is attention to these topics, but the specific details
are beyond the research’s scope.
Finally, to define and manage the specific complexities
of the integration of IT within a physical asset in further
research, this study, proposes a definition of IT/OT converged
asset management, based on the observations from this literature review as well as the work of Pudney (2010):
‘‘The process of aligning maintenance challenges, cybersecurity aspects and configuration management tasks over an
IT/OT converged assets combined life cycle, cost-effectively,
to achieve a predefined performance level for its stakeholders, while mitigating risks.’’
Also, tools and methods are required to support practitioners in operationalizing this definition in practice and to
manage this complexity sustainably. Future work will aim to
create these tools and methods that help to integrate IT within
OT environments to increase cooperation between IT and OT
teams and demonstrate their application in practice.
V. CONCLUSION
A literature review was performed to study 113 studies from
the last 20 years with a focus on three important domains
regarding the integration of IT with OT in physical assets:
Maintenance, cybersecurity, and configuration management.
This literature review gives insight into the specific differences between IT, OT, and IT/OT converged systems.
The literature review reveals three aspects that pay more
attention in managing IT/OT converged systems. Firstly,
maintenance practices change as the life cycle of a system
changes more frequently with the introduction of IT. Secondly, there has been considerably more research interest in
cybersecurity due to the new risks that are introduced when
IT and OT are connected. Lastly, configuration management
has become even more important since the system’s design
changes as IT becomes the central element, making a system’s architecture more important. Moreover, gaps have been
identified together with some key messages for practitioners
in the industrial sector.
This research suggests further research is needed to deal
with the increased complexity of IT/OT converged systems.
It can be argued that for IT/OT converged systems, balancing
financial, technical, and organizational practices still needs
research attention. Therefore, research towards integrated
and sustainable approaches which deal with IT/OT-related
challenges is necessary. This should be combined with the
development of specific tools and methods for sustainably
managing IT/OT converged systems.
ACKNOWLEDGMENT
The first author thanks his colleagues Leo van Dongen and
Henrike Holwerda for their feedback and discussion on the
previous versions of this paper.
