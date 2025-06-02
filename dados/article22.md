Title: Contemporary Software Modernization: Strategies, Driving Forces,
and Research Opportunities

Software modernization is a common activity in software engineering, since technologies advance, requirements change, and
business models evolve. Differently from conventional software evolution (e.g., adding new features, enhancing performance,
or adapting to new requirements), software modernization involves re-engineering entire legacy systems (e.g., changing
the technology stack, migrating to a new architecture style, or programming paradigms). Given the pervasive nature of
software today, modernizing legacy systems is paramount to provide customers with competitive and innovative products and
services, while keeping companies profitable. Despite the prevalent discussion of software modernization in gray literature,
and the many papers in the literature, there is no work presenting a “big picture” of contemporary software modernization,
describing challenges, and providing a well-defined research agenda. The goal of this work is to describe the state of the art
in software modernization in the past 10 years. We collect the state of the art by performing a rapid review (searching five
digital libraries), identifying potential 3,460 studies, leading to a final set of 127. We analyzed these studies to understand
which strategies are employed, the driving forces that lead organizations to modernize their systems, and the challenges that
need to be addressed. The results show that studies in the last 10 years have explored eight strategies for modernizing legacy
systems, namely cloudification, architecture redesign, moving to a new programming language, targeting reuse optimization,
software modernization for new hardware integration, practices to leverage automation, database modernization, and digital
transformation. Modernization is triggered by 14 driving forces, with the most common ones being reducing operational costs,
improving performance and scalability, and reducing complexity. In addition, based on the analysis of existing literature,
we present a detailed discussion of research opportunities in this field. The main challenges are providing tooling support,
followed by defining a modernization process and considering better evaluation metrics. The main contribution of our work
is to equip practitioners and researchers with knowledge of the current state of contemporary software modernization so that
they are aware of practices and challenges to be addressed when deciding to modernize legacy systems.
CCS Concepts: • Software and its engineering → Software evolution; Software architectures; • Computer systems
organization → Cloud computing.
Additional Key Words and Phrases: Software Evolution, Software Migration, Re-designing, Re-engineering
1 INTRODUCTION
Throughout the life of a software system, its architecture decays, its underlying technologies become obsolete,
the user requirements change, or the company’s business models evolve—ultimately, causing the software to
morph into what we call legacy systems [16]. The vast majority of software currently in operation is long-lived
systems that represent many years of competitive knowledge and business value [53]. Although fundamental for
the business operations, due to extensive maintenance and obsolete technology, legacy systems are costly to
maintain, more exposed to cybersecurity risks, less effective in meeting their intended purpose, and push up
costs of digital transformation [15, 66, 85]. For example, the US government spent more than $100 billion in fiscal
year 2023 on IT, of which about 80% was used to operate and maintain legacy systems [86]. In addition, the UK
government spends £4.7 billion a year on IT in all departments, and £2.3 billion goes on patching up systems,
some of which date back 30 years or more [66].
To remain competitive, companies must modernize their legacy systems [10]. Furthermore, with modernization,
companies can preserve the hard-earned knowledge acquired through many years of system development [53, 79,
90]. According to Seacord et al. [79] “Software modernization attempts to evolve a legacy system or elements of the
system, when conventionally evolutionary practices, such as maintenance and enhancement, can no longer achieve
the desired system properties.” Differently from conventional software evolution (e.g., add new features, enhance
performance, or adapt to new requirements), software modernization involves re-engineering1 or migrating2
entire legacy systems. Thus, software modernization refers to the conversion, rewriting, redesign, or porting of
a legacy system to a modern computer programming language, protocols, or hardware platform [54, 78]. The
process of modernizing a legacy system has benefits such as ease of engineering activities, satisfying user needs,
achieving new business goals, or reducing costs [79]. Furthermore, modernization is a means to leverage digital
transformation [15], as it allows the use of emerging and disruptive technologies such as artificial intelligence,
high-performance computing, cloud computing, the Internet of Things, industry 4.0, robotics, and big data [60].
Given the pervasive nature of software today, modernizing legacy systems is essential to provide customers
with competitive, innovative, and sustainable products and services and to support companies to benefit from
new technologies [20, 41, 53, 80]. In the literature, we can find different modernization strategies [60, 81]. For
example, restructuring systems using components, adopting aspect-oriented development, re-engineering system
variants into software product lines, migrating to microservices, and supporting new hardware (e.g., multicore
and GPU devices). Even the software development process has been modernized, with the adoption of agile
methods [62] and DevOps [25]. Additionally, modernization has different driving forces and impacts related to
organizational, operational, and technological aspects [90]. For instance, modernization can focus on independence
for agile teams, optimize the deployment, ease the inclusion of innovation, facilitate scalability, support new
hardware, or explore new market segments [81, 90].
Despite the prevalent discussion of software modernization in gray literature [66, 85, 86], and the pieces of
work in the literature [38, 49, 49, 53, 54, 60, 63, 81], there is no work presenting a “big picture” of contemporary3
software modernization. It is still unclear what are the current modernization strategies, driving forces that
trigger the modernizations, and well-defined research agenda with challenges to be addressed in the following
years. As pieces of work span across many years and focus on modernizing for different purposes, there is a
need for discussing modernization in the context of contemporaneous software development. The studies that
try to organize the existing literature have several limitations. They only present an overview of the state of
the art [60]; are based on few case studies or a subset of existing literature [49, 63, 81]; are outdated regarding
current emerging/disruptive technologies [38, 49, 53, 54]; partially cover the modernization life cycle, and rarely
take into account organizational, operational, and technological aspects [60, 90].
Based on the limitations of existing work, we conducted a study guided by three research questions. These
research questions aim to investigate the existing strategies to modernize legacy systems (RQ1: From>To Strategies), what are the common reasons and pains that lead to the modernizing (RQ2: Driving forces), and the open
challenges and research opportunities in the field (RQ3: Challenges). To answer these questions, the goal of this
work is to describe the current state of the art on software modernization, considering studies in the past 10 years.
By performing a rapid review [21, 22], we collect the pieces of work in five digital libraries, identifying ≈3.5k
studies. Guided by the research questions, after a careful analysis of the content of these papers, we selected a
final set of 127 used as a source for our analysis.
The results show that eight main strategies (RQ1) for modernizing legacy systems have been explored in the
last 10 years. These strategies are We found 14 distinct driving forces (RQ2) that are considered for starting
a modernization process, namely reduce operational costs, promote interoperability among systems, improve
performance and scalability, foster innovation, achieve better flexibility and efficiency, reduce complexity, enhance
agility, explore new business opportunities, reduce time to market, avoid duplications and inconsistency, leverage
reuse opportunities, allow better understanding of the system architecture, provide external services, and improve
the quality of data. In addition, based on the analysis of existing literature, we identified 16 challenges for software
modernization (RQ3), which allowed us to present a detailed discussion of 27 research opportunities in this field.
The main challenges are lack of tooling support, the need for better evaluation metrics, applying cost-benefit
analysis to align the modernization with the business goals, maintaining the consistency between legacy and
modern systems, and keeping the correctness of the modern system.
The main contributions of this work are:
• Review of the state of the art: We present a comprehensive and contemporaneous review of software
modernization in the last 10 years, with the goal of calling attention to advances in research and practice
towards dealing with legacy systems. We contextualize the different strategies, together with driving
forces for software modernization, and introduce a research agenda with 27 research opportunities to be
taken into account in the following years.
• Support the decision on the right modernization strategy: We describe the modernization strategies and
their driving forces. Based on specific reasons or pains, some approaches are more appropriate than
others. Thus, our work can help practitioners to make informed decisions, avoiding deciding only based
on technological “hypes”. Choosing the wrong approach can lead to inefficiency and frustration during
modernization. Our work motivates the discussion on software modernization and alerts companies about
challenges they may incur when choosing a specific modernization strategy.
• Train the workforce with skills for dealing with modernization: Our results reveal several strategies and
challenges that must be considered during modernization. Thus, educators can benefit from our work
as a basis for designing new courses in academia, with the goal of training the workforce in charge of
operationalizing the modernization of legacy systems.
2 BACKGROUND
Seacord et al. [79] presented software modernization as a remedy to face the legacy system crisis in the early
2000s. They discussed how to keep or add business value through modern technologies, reducing operational
costs, and dealing with technical aspects (e.g., allowing better reuse and easier maintenance) [79]. The focus on
software modernization is to preserve knowledge represented in legacy systems while employing disruptive and
emerging technologies to the benefit of users, companies, and society.
Disruptive and emerging technologies such as ubiquitous embedded computing, connectivity, and flexible
value streams are enablers of Digital Transformation, a technology-driven continuous change process [35, 70].
Modernization is a means to leverage the digital transformation [15, 60]. According to the report, “Shaping the
digital transformation in Europe” [37], from the European Commission, by 2030 the cumulative additional GDP
contribution of new digital technologies could amount to 2.2 trillion Euros. The same report points, for example,
that digital transformation (e.g., online interactions and monitoring, paperless data, workflow automation, decision
support, and appropriate patient self-care) in the EU health sector can achieve efficiencies of up to 120 billion
Euros. However, a survey revealed a staggering 88% of services companies that have had a digital project fail or
reduced in scope due to the cost of making changes to legacy technology, making companies spend twice the
industry average on digital transformation [15].
In the literature, we can see the three ways of moving a legacy system towards a modern system: (i) big bang
or cold turkey [29], which is the replacement of the legacy system with the modern one at once; (ii) incremental
modernization, following a strangler pattern [40], in which parts of the legacy systems are incrementally replaced
by modern parts [79, 90]; and (iii) the coexistence, in which legacy and modern parts operate together in one
system [75]. Furthermore, there are different types of modernization a company should decide on, which must be
based on a portfolio analysis. Figure 1 presents the portfolio analysis quadrant (extended from Seacord et al. [79])
to support the decision among the types of modernization. In addition to the technical quality and business value
dimensions, we introduce innovation as an additional dimension that is achieved by new disruptive and emerging
technologies (i.e., driving forces for modernization). The five quadrants in these three dimensions are:
• 1. Replace: legacy systems that have low business value and low technical quality, i.e., accumulated
technical debt, should be replaced by new systems, using generic solutions or off-the-shelf systems, instead
of undergoing a re-engineering or migration process.
• 2. Maintain: systems with high technical quality and low business value should not require modernization
effort, but traditional maintenance activities should be used, just to keep them operating and meeting
customers’ needs.
• 3. Evolve: high-quality legacies with high business value should be actively evolved using traditional
evolutionary development practices for introducing new features, new products, or even serving as a
third party for other systems.
• 4. Re-engineer: systems with high business value and low technical quality should be re-engineered to
preserve business value, i.e., external quality, and manage the technical debt, i.e., internal quality. This
type of modernization can be transparent to the end user.
• 5. Migrate: when the system has high business value and a company decides to drive innovation with
emerging or disruptive technologies, independently of the system’s technical quality, a migration to
the desired new technologies should take place. This is, for example, the case when companies foster a
digitalization initiative.
In the literature, we can find studies on software modernization to retain the business value of legacy systems [60, 81]. For example, restructuring systems using components [26, 36, 55], adoption of aspect-oriented
development [5, 43, 74], re-engineering of system variants into software product lines [8, 9, 59, 73], migration to
microservices [19, 23, 33, 57, 83, 87, 90], supporting new devices or pieces of hardware (e.g., from single-core to
multicore machines) [68, 72, 76], classical information systems to quantum computing [71, 92], and leveraging
the use of AI/ML/Foundation Models [3]. Even the software development process has been modernized, such
as the adoption of agile methods [62] and DevOps [18, 25]. Modernization also has different driving forces and
impacts related to organizational, operational, and technological aspects. The modernization can focus on the
independence of teams, optimizing deployment, adding innovation, facilitating scalability, or exploring new
market segments [81, 90].
Despite existing literature, the work on software modernization has several limitations: studies only present an
overview of the state of the art [60], are based on few case studies or a subset of existing literature [49, 63, 81], are
outdated regarding current emerging/disruptive technologies [38, 49, 53, 54], partially cover the modernization
life cycle, and rarely take into account organizational, operational, and technological aspects [60, 90]. Furthermore,
these studies are limited to exploring contemporary needs (e.g., digital transformation [60]). Thus, to have a
comprehensive view of the state of the art on software modernization, we conducted a study analyzing the pieces
of work published on this topic in the last 10 years. This study is presented in the next section.
3 STUDY DESIGN
To describe the state of the art and provide a research agenda on software modernization, we adopt a Rapid Review
(RR) protocol [46, 84]. RR is an emerging (considering software engineering) alternative to systematic literature
reviews (SLR) [56], focusing on more practical problems, while analyzing a comprehensive set of studies [21, 22].
Despite being different from traditional systematic mappings (SMS) and SLR, an RR still enforces a well-planned
and executed protocol to obtain the desired results. The first step of this protocol is to define the goal and RQs.
Given the aims of our study, the main goal of this study is:
Goal: Review the literature on software modernization for the purpose of identifying the existing strategies,
main driving forces to modernize legacy systems, and challenges that still need to be addressed.
3.1 Research Questions
The goal of our study originated three research questions (RQ), which guided the search strategy, selection of
primary sources, and data extraction, as follows:
• RQ1: (From>To Strategies) What are the contemporaneous strategies to modernize legacy
systems? In our study, we first focus on identifying which modernization strategies have been explored
in the literature. To understand the modernization strategies, we consider what was the legacy system and
what is the modern system for each study, meaning we investigated the “[From] legacy system [To] target
system” strategies explored in the literature. By answering this question, we have an overview of the
contemporaneous modernization strategies, since our study focuses on the last 10 years (i.e., 2014-2024).
• RQ2: (Driving forces) What are the common driving forces for modernizing a legacy system? As
important as knowing which modernization strategies have been explored in the literature, is to know
Table 1. Inclusion/Exclusion Criteria to Filter Relevant Studies.
Inclusion Criteria Exclusion Criteria
IC1. The paper’s main contribution must be related to
software modernization.
EC1. The paper has less than 6 pages.
IC2. The paper discusses/addresses a practical problem in
software modernization.
EC2. The paper is not written in English.
EC3. The paper was published before the year 2014.
EC4. The full text of the paper is not available online.
EC5. The paper is a conference version of a journal extended publication.
“why” this modernization took place. In this question, we aim to investigate what are the driving forces
that triggered software modernization. By understanding the reasons and pains that lead companies to
decide to modernize their legacy systems, we are able to know what are the main limitations of legacy
systems.
• RQ3: (Challenges) What are the challenges and research opportunities in the field of software
modernization? Given the paramount importance of legacy systems for users, companies, and society,
in this question we focus on providing a well-defined research agenda on the topic. We explore existing
literature to grasp what are the open challenges, observed limitations, and future work. Based on this
analysis, we present research opportunities to guide the advancement of knowledge on the topic of
software modernization in the following years.
3.2 Search Strategy
For the search of primary sources, we defined the relevant terms, and their synonyms, related to the goal and
RQs of our study. These terms and synonyms are used to establish our search string:
Search String: “(migrat* OR moderniz* OR transform* OR re-engineer* OR restructur*) AND (“legacy
software” OR “existing software” OR “legacy system” OR “existing system” OR “legacy program” OR “existing
program”) AND (practic* OR industr* OR real-world))”.
We then derive a specific search string for each of the used digital libraries (DL), namely Scopus, Springer, IEEE,
ACM, and Web of Science.4 These specific search strings were defined after executing, analyzing, and refining the
base search string (presented above) to the point they returned a satisfactory result. Additionally, when allowed
by the DL, we included keywords and filters in the strings that are related to the inclusion/exclusion criteria,
such as to search only papers published in English. Finally, for the screening of the studies returned from each
DL, according to the protocol of our RR, we defined these inclusion (IC) and exclusion criteria (EC) to select only
relevant papers, as presented in Table 1.
Two of the authors of this study applied the I/E criteria to all 2,902 papers. When there was a conflict between
these two authors (i.e., one author decided to include and the other to exclude), a third author also applied the
criteria, making the final decision about the inclusion/exclusion.
3.3 Search and Selection
Figure 2 presents the number of studies retrieved from each DL. The search was carried out in August 2024.
After performing the search in the five DLs, a total of 3,460 studies were retrieved. From these studies, 558 were
duplicates. We considered a study as a duplicate if this study was exactly the same paper found in different DLs
(e.g., Scopus and ACM). After removing the duplicates, 2,902 studies remained for the application of the I/E
Criteria, based on the criteria presented in Table 1. One important criterion is given by EC5, where we excluded
papers that were a conference version of a paper later extended to a journal (i.e., we included the journal version
of the paper as it contained a more complete version of the contributions). After applying these criteria, 127
studies remained. The complete list of primary sources is presented in Appendix A, and also available in our
supplementary material [44].
3.4 Data Extraction
Based on the guidelines for RR [21, 84], the typical analysis of primary sources employs a descriptive synthesis
approach rather than a quantitative meta-analysis. To extract the data required to address the three RQs of
our study, we conducted a manual review of the selected papers, aiming to classify and generate a descriptive
synthesis for each. The following fields were extracted from each paper: (i) Modernization strategies and origin
and target technology or architecture: we extract these strategies from the description of the approach and the
intended results; (ii) Description of the driving forces and the reasons to modernize: we extract this information
from the motivation and practical problems described in the studies; and (iii) Challenges and main research
opportunities: these pieces of information are extracted from limitations and future work described in each paper
analyzed.
4 RESULTS AND ANALYSIS
This section presents the strategies, driving forces, and challenges for the 127 primary sources, which are reported
in Appendix A. Table 2 lists the eight modernization strategies identified, which have been applied across various
domains of software engineering, such as moving systems to the cloud, improving the system architecture,
supporting digital transformation, focusing on the database, and enabling the integration of new hardware. For
the driving forces, shown in Table 3, we organize them into operational, technical, and organizational, with a
total of 14 distinct driving forces. Table 4 presents the 16 challenges identified in the set of studies analyzed. We
present details of the eight strategies in the following sections. We also discuss the driving forces related to each
strategy, namely the factors or goals for conducting such migrations. Despite the successful migration of many
projects and the introduction of novel migration procedures, both researchers and practitioners encountered
various challenges, which we present together with their respective research opportunities.
4.1 Cloudification
Cloudification stands out as the most adopted modernization strategy (41 studies). This was expected due to the
popularity of cloud providers.5 For this category, due to many primary sources, we describe three subcategories
targeting: (i) the migration of systems to the cloud without referring to any particular architectural style [S27,
S28, S32, S40, S43, S45, S55, S57, S68, S69, S90, S118, S127], (ii) the transition of legacy systems to Service
Oriented Architecture (SOA) [S1, S26, S30, S71, S72, S73, S121], and (iii) the migration of monolith systems to
microservices [S8, S9, S10, S12, S16, S21, S22, S23, S42, S51, S64, S74, S75, S89, S93, S108, S112, S114, S120, S123,
S125].
4.1.1 Migration to the Cloud. This strategy for modernization mainly refers to migrating legacy systems
operating on-premise to a cloud infrastructure. This process requires moving applications, data, security, and
other artifacts to a cloud computing environment. In this subcategory, it is not necessary to change the legacy
architecture (i.e., a monolith can be deployed on the cloud).
Driving Forces. The primary motivation to migrate a legacy system from on-premise to a cloud infrastructure
is to address scalability challenges arising from increasing system demands [S27, S28, S32, S40, S43, S90, S127].
For instance, a study discusses the migration of a real-time geo-social networking application to the cloud due to
the growth in data volume, complex search queries, and the absence of real-time features such as instantaneous
upload and download of frequently used resources [S28]. Similarly, another paper describes the migration of
a geospatial analytics system, initially developed for on-premises infrastructure, to the Siemens MindSphere
cloud platform to enable elastic scaling and large-scale data processing [S90]. Another major disadvantage of
on-premise infrastructure is the high operational cost [S28, S57, S69], primarily due to the expense of maintaining
the infrastructure and the need for extensive administrative oversight [S28]. In contrast, cloud providers offer a
pay-as-you-go model where costs are based on actual resource usage, and resource management is simplified [S69].
A study, which focused on migration to Function as a Service (FaaS), highlighted the reduction in system complexity
associated with cloud migration [S118]. According to the authors, the adoption of FaaS brings benefits such as
improved maintainability, testability, and reusability.
Research Opportunities. For this subcategory, we distilled five research opportunities.
Managing Consistency between legacy and modern systems: Among the types of transitions from legacy to
modern systems presented in Section 2, the big bang and incremental are explored in the literature, however,
little is discussed on how to establish a hybrid environment to allow the development and coexistence of legacy
and modern system [S45, S90]. One study suggests future research on scenarios where the legacy and modern
systems coexist continuously and in parallel (i.e., a hybrid architecture) for a certain period of time due to missing
functionality between target and legacy system [S55]. The authors also recommend exploring potential solutions
for situations where functionalities are missing in the new system or when data format incompatibilities arise.
Defining a Process for the Migration: Integrating new solutions into existing systems and the absence of
established migration practices are significant challenges. The authors of one paper recommend adopting a
multi-criteria decision-making (MCDM) framework for platform selection in the industry [S40]. This idea is
further expanded in another paper, where the authors propose a generic model to facilitate cloud migration in
terms of cost and quality estimation [S32].
Predicting and Optimizing Performance: One paper acknowledges the fact that pre-warming containers (by
using future function call prediction) is a way of addressing the issue of cold starting in FaaS [S118]. A similar
issue of cold start was raised in another study, when a company migrated its systems to a serverless architecture
(FaaS) [S40].
Providing Tooling Support for Migration to the Cloud: There are several concerns related to the development
and enhancement of tools for generating and visualizing architectures to support effective cloud migration
planning [S27]. A paper advocates for a tool that abstracts the cloud migration model, offering simple interfaces
to incorporate additional migration planning parameters and to track the decision-making process throughout
the migration [S90].
4.1.2 Transition to Service-Oriented Architecture (SOA). This modernization strategy primarily focuses on
transforming legacy systems into modular and loosely coupled services. These services within the application
can be invoked independently, each exposing specific functionality [S73]. In this way, SOA can be used to address
some of the inherent challenges of traditional monolithic legacy systems.
Driving Forces. Among the papers in this category, the primary goal for transitioning towards SOA is to
reduce costs for maintaining the legacy system [S72, S73]. In one study, the authors mention that SOA makes
easier the comprehension of the system’s architecture [S26]. The migration to SOA also leverages new business
opportunities [S121]. One paper asserts that migrating legacy applications to SOA enhances their robustness
and optimizes them to align with business objectives [S71]. A study emphasizes the utilization of relatively
independent and reusable services, which effectively address scalability challenges in legacy systems [S1]. Other
authors discuss the goal of the migration process as integrating core functionalities with other agencies to
improve the e-government model, thereby expanding interoperability among systems [S72]. They also note that
legacy systems, particularly those developed in COBOL, result in increased operational costs related to processing
power, difficulties in finding affordable programmers skilled in these technologies, and the lack of productive
development tools.
Research Opportunities. For this subcategory, we observed two research opportunities.
Exploring Diverse Methodologies for Service Identification: Researchers utilized clustering algorithms to identify
services for the target architecture [S26]. However, they note a significant challenge: in tightly coupled codebases
with limited modularity, these algorithms may struggle to decompose the system effectively into distinct services.
This limitation indicates a need for further research into alternative techniques for service identification that
are better suited to legacy systems migrating to SOA [S26]. This perspective is echoed in another study [S1],
where the authors propose experimenting with other algorithms as part of their future work. Exploring diverse
methodologies for service identification is crucial for improving the accuracy and efficiency of SOA migration
processes.
Tooling Support to Detect and Mitigate Antipatterns during the Modernization: In one study, the authors emphasize
that while adopting SOA through rapid and cost-effective means may seem appealing, it often results in suboptimal
service quality [S72]. They advocate for robust tooling support to facilitate the migration process, focusing on the
correctness of the modern system. For instance, they document a case where a code-first tool, used to generate ASP
Web Service interfaces, introduced antipatterns such as Redundant Port Types and Enclosed Data Models. This
highlights the need for sophisticated tools that can detect and mitigate such issues during migration. Similarly, a
paper discusses the need for the development of automatic packaging techniques to efficiently integrate identified
services into the target platform [S1]. This requirement underscores the importance of advanced tooling solutions
to streamline the migration and integration processes, enabling a smoother transition to SOA.
4.1.3 Monolith to Microservices. This strategy focuses on splitting a legacy system into small, autonomous,
and highly-independent services communicating by using lightweight network protocols [S9]. Though microservices is an evolution of SOA [S120], we present our findings on migration to microservices as a separate strategy
due to its wide adoption across adopt several industries [S125].
Driving Forces. The main driving forces to migrate from a legacy monolith system to a microservice-based
architecture is largely attributed to scalability issues [S114, S125], and faster time to market enabled by automated
cycles with continuous integration and deployments [S10, S21, S75]. We also found that the modernization
applied seeks to improve performance by reducing system latency [S125], and applying selective scaling to specific
resources and application instances [S89]. For example, a study highlighted that the system’s high coupling
negatively affected performance. When demand increased for a single module, the entire system had to be scaled
due to the interconnected nature of the components [S12]. We noted a similar scenario for a bank that needed to
attain rapid scalability in order to serve a high number of customers, having a high fluctuating behavior in terms
of application usage [S42]. At the operational level, the primary goals of modernization with microservices are
to enhance agility [S64], foster innovation [S16], and reduce the operation cost of maintenance [S8, S42], thereby
improving organizational flexibility and efficiency [S114]. For instance, a paper highlighted a case where different
departments within a police intelligence office faced challenges due to a lack of service interoperability among their
systems [S22]. Additionally, their legacy systems were difficult to maintain, resulting in operational inefficiencies
and data duplication and inconsistencies issues.
Research Opportunities. For this subcategory, we distilled three research opportunities.
Advancing the Techniques for Monolith Decomposition: Similarly to what was pointed as a challenge for the
transition to SOA, for microservices, deciding on how to decompose the legacy systems (i.e., service identification) is a prevalent challenge. The primary step for migrating a legacy system to microservices involves the
decomposition of the monolithic architecture [90]. This requires application of dynamic analysis techniques for
service identification [S51], allowing engineers to understand how the modern application can be impacted by
the network communication among microservices. Strategies for the identification of services in non-objectoriented code-base (e.g., COBOL systems) is also of key concern [S9, S74]. Additionally, automated refactoring
to microservices is essential [S23, S51] to reduce modernization costs/effort while maintaining the expected
quality. Authors advocate for a framework to support the prioritization of services in the context of incremental
migration [S75, S112]. This type of framework would particularly be useful in the migration of mission-critical
systems where rapid migration is needed or in the situation of constrained resources [S108]. There is an increasing
use of machine learning algorithms to identify microservices within monolithic applications. Specifically, a paper
advocates for the use of clustering algorithms [S114], while the implementation of graph neural networks is
recommended by other authors [S125]. Other pieces of work call for the exploration of alternative techniques
for identifying microservices from monoliths, moving beyond their prior use of static analysis methods and
search-based algorithms [S9, S12].
Designing New and Better Evaluation Metrics: There is an emphasis on introducing evaluation metrics for the
thorough analysis of target architecture [S22, S112]. These metrics should seek to quantify the level of reuse
among multiple services [S8] and provide means of assessing other decomposition methods, which is also related
to the previous challenge [S112, S120]. This can particularly enable efficient planning of the migration journey.
To continue with, legacy code-bases often exhibit poor quality and contain antipatterns. Thus, some authors
emphasize the need to assess the impact these may have on training machine learning algorithms to aid in service
identification [S42, S93]. Additionally, one paper highlights concerns regarding the effects that automatically
generated services could have on the future operations of the entire architecture [S16]. Furthermore, other pieces
of work address the challenges of preventing microservice antipatterns and accumulating technical debt during
the modernization process [S16, S21], which also deserves more attention in future research.
Tooling Support for Visualization and Reconfiguration of Microservices: Two papers discuss the need for effective
visualization of microservice architectures to bridge the gap between technical and business stakeholders, enabling
better alignment and communication [S16, S51]. Similarly, a paper emphasizes the importance of packaging
and deploying individual microservice units with the flexibility for dynamic reconfiguration [S108]. Addressing
these challenges requires robust tooling support that can integrate the requirements for both decomposition and
adaptability. Thus, developing such tools can significantly enhance the design, deployment, and management of
microservices, making this a critical area for research and innovation.
4.2 Architecture Redesign
Given the long lifespan of software in many industries, designing software with foresight is crucial. When the
legacy system has a high business value, it is a candidate for modernization, independently of its internal quality.
However, understanding and modernizing a legacy system with poor internal quality is a complex task. For
example, systems usually evolve in space, adding new features, and time, with features being revised [65], which
make their comprehension difficult. For such a situation, using refactoring strategies is a good way to improve the
legacy internal quality to face the modernization [17]. Architectural redesign is important for effective software
modernization, which is the focus of the studies in this section.
Driving Forces. There is a case of poorly designed software for certain bank’s departments that led to record
duplication, with each department assigning a different key to the same record [S14]. Similarly, a paper highlighted
several reasons for architectural redesign, such as the use of multiple servers for data management combined
with a rigid design structure, which led to data duplication and inconsistencies [S53]. Additionally, another study
noted duplicated business logic in the codebase, without proper encapsulation, hindering reusability [S86]. A
different paper used Amazon Simple Queue Service (SQS) as an example to illustrate the issue of broad coupling of
server functions, which limits reuse [S85]. Yet, to introduce interoperability in industrial applications, architectural
refactoring was employed to expose existing functionalities through APIs [S122]. Furthermore, advancements in
technology necessitate substantial investment in enhancing the security of existing systems. This is discussed in
one of the papers under the concept of Privacy-Oriented Software Development (POSD) [S11].
There are several additional examples in this category. A defense industry project had its legacy codebase
refactored into a component-oriented architecture to enable reusability while building prototypes [S62]. Another
interesting case involves introducing multi-tenancy in a legacy application solely through code refactoring,
with the goal of increasing profitability through the SaaS model [S44]. To enhance software design with reactive
programming, which reduces complexity of computations over data streams, static data flow analysis-based
refactoring was used to transform asynchronous code into reactive code [S56]. One study details a unique case of
software refactoring aimed at changing data representation to improve performance and data quality [S82].
Research Opportunities. Architecture redesign is one of the strategies in which we found several research
opportunities, mainly because it is strictly related to refactoring.
Improving General Architecture Recovery: One of the first steps for the redesign, is to recover the architecture of
the legacy system. Thus, architecture recovery is a prevalent challenge [27]. The authors of a paper propose, as part
of their future work, a Grounded-Theory-based approach for recovering the architectures of large-scale legacy
systems [S113]. Other researchers suggest the use of unsupervised learning techniques to assist in architectural
refactoring [S77]. Additionally, a study highlights the need of establishing a baseline for evaluating architecture
recovery approaches [S113].
Checking the Correctness of the New Architecture: While source-to-source transformations are used to support
the migration of architectures, a call was made to additional techniques such as the automatic generation of unit
tests to validate the correctness of the transformed code [S2, S124]. There are often negative effects on system
performance when extensive refactoring is carried out [S109]. Thus, it is worth researching how to ensure that
the restructured code achieves the intended purpose without incurring significant performance costs. The area of
code smell detection is not exempt from considerations during the redesign. It was mentioned as future work
to incorporate detection mechanisms for more design flaws that exhibit bad smells during refactoring [S109].
Additionally, other authors intend to utilize previous code changes and class complexity to aid in the detection
of code smells in refactored code [S2]. Also, a paper mentioned the opportunity of exploring the use of Large
Language Models to test smell detection and removal [S7].
Improving Architectural Refactoring Tools: A paper highlights that there is a lack of tools for architecture-driven
modernization in refactoring activities [S25]. As part of their future work, the authors propose that these tools
should be improved to incorporate developer feedback, rather than relying solely on code smells and other
code characteristics, as not all code smells necessarily trigger refactoring. Additionally, in the scenario of legacy
systems with missing architecture documentation, tools that assist in recovering software architectures through
direct code inspection would be highly beneficial [S113]. In a move to migrate skeletal implementation patterns
in legacy Java code to Java 8 default methods, the authors intend to explore techniques such as Javadoc merging,
transforming build scripts for migrations across modules, and using machine learning to disambiguate destination
interfaces [S54]. This can be envisioned through proper tooling support and development. In addition to the
primary sources, an additional research direction is to leverage Foundation Models (i.e., Large Language Models)
in tasks related to code understanding [67] and refactoring [4] during the modernization.
4.3 New Programming Language
This strategy for modernization mainly refers to the switch between programming languages while modernizing
legacy systems. The continuous evolving of some programming languages pushes other slow paced maintained
languages into the legacy zone (e.g., due to outdated documentation or technology advancements [S35]). Thus,
companies are forced to modernize their systems to use new programming language features. We recorded at
least eight different instances of language switch from COBOL to JAVA and C#. Others include C++ to JAVA, C to
C++, Java to C++ and C++ to Web Assembly. The main motivations for this strategy are discussed below.
Driving Forces. A number of the papers mentioned reducing complexity helps in better maintainability of the
software as part of their driving forces when switching between different languages [S18, S49, S63, S98, S103,
S104, S106]. For example, a group of authors transformed Oracle Forms to Java applications with the aim of
decreasing the workload required to understand the structure of Oracle Forms [S98]. The next underlying reason
is the lack of support for a given language or the underlying technology of a given system. For instance, after the
suspension of PACBASE in 2015, there was a need for migrating from PACBASE code to plain COBOL [S24].
With respect to maintainability and lack of maintenance support, a financial institution in Japan re-engineered
its COBOL based system to Java [S119]. Also, a group of authors stated that translation of Visual Basic to Python
is relevant as financial industries are adopting artificial intelligence solutions [S63]. Thus, modern technologies
facilitate this modernization strategy as they foster innovation. Additionally, other two driving forces of migration
to new languages are bigild times [S116] and adopting new technologies and growth [S79, S105].
Research Opportunities. There are three direction for future work in the modernization with new programming languages.
Supporting the Evaluation of Modern Applications: One study reported significant performance issues during
the re-engineering of a legacy system in the financial industry, which left business stakeholders dissatisfied [S18].
Meanwhile, another paper intends to focus on evaluating the performance of a system after its migration from
Google Web Toolkit to the Angular framework [S116]. This work aims to leverage Angular-specific features, such
as lazy loading and ahead-of-time compilation, to optimize performance. Thus, research on evaluating target
systems can is necessary to provide valuable insights for both researchers and practitioners, helping them assess
the broader applicability of their methodologies.
Cost-Benefit Analysis During Migration Planning: To avoid delays in decision-making during modernization, a
research opportunity is to quantify the cost-benefits of incremental migration [S119]. The authors plan to refine
their analysis by incorporating dependencies, such as database access, to enhance accuracy. They also aim to
extend their analysis to other target programming languages. Another challenge that needs to be addressed is
comparing the complexity and quality of both the legacy and target systems based on a specific modernization
strategy [S110].
Tools for Language Transformations: Similar to automatically generated code, there is a need for tools for
the automatic generation of unit tests [S124]. Another propose future work which can complement language
transformation tools is the fine-tuning of general Large Language Models for specification discovery from legacy
systems [S63]. In terms of transformations between the same language, there is the need for enhanced code
difference techniques and tools by incorporating semantic and structural characteristics of the code rather than
just treating code as text [S24].
4.4 Reuse Optimization
The studies on this strategy focus mainly on Software Product Line (SPL) engineering, as a way of addressing the
issues of opportunistic reuse (a.k.a., copy-and-paste or clone-and-own) [8]. Opportunistic reuse offers low initial
costs and simplicity, but results in high maintenance costs due to the need to propagate bug fixes and feature
updates across all clones [S60]. This makes the approach less sustainable in the long term. SPL engineering
focuses on systematically deriving new systems from existing artifacts rather than developing them from scratch.
Driving Forces. The authors of a paper applied SPLs to a framework consisting of over 20 software artifacts with
the primary goal to streamline the development of frequently used functionalities (e.g., security, file management,
and business-related activities) and reduce the time-to-market by leveraging reuse opportunities [S88]. Similarly, a
case study involving a seven-variant control unit software with over 13,000 lines of code highlighted the presence
of two variants that were essentially clones of each other [S99]. This situation underscored the need to modernize
the system and adopt a reuse strategy to avoid duplication and inconsistency. Another paper mentions the need of
managing features across different versions of product variants as a driving force to adopt SPLs [S78]. The authors
pointed out that locating feature revisions and composing variants with different feature revisions is essential for
organizations adopting this strategy, as it enables better management and leverages reuse opportunities across
product lines.
Research Opportunities. There are three research opportunities for the modernization of legacy system with
focus on optimizing the reuse among family of software products:
Providing Cost-Benefit Estimation Models: It is usually risky switching to a new development paradigm, such as
reuse-oriented software development, as this may lead to incurring severe cost. Hence, there is a call for cost
estimations to predict the benefits of alternate development approach, especially in the extractive approach for
SPLs [S59]. Similarly, the use of decision models or substantial empirical data to assess the cost and benefits of
alternative re-engineering methods is worthy of research [S58].
Improving Variability Modeling and Analysis with Business-Related Concerns: One study highlights the need
for inculcating business constraints to aid in defining products that match current market needs [S88]. Another
paper, which addressed the need to generate core requirements for reuse, seeks to include the dependencies and
constraints between variable parts to improve the reusability of the core requirements (i.e., features of high value
to the business) [S95].
Creating tools for SPL Extraction: One of the challenges we noticed is related to the difficulty in finding
appropriate tools for SPL extraction, which resulted in incomplete and inconsistent feature extractions, difficulties
in managing feature dependencies, and issues with feature constraints [S81]. Another paper recommends tool
development to facilitate multistaged product configuration, focusing on providing the necessary infrastructure
and resources to manage complex configurations [S88].
4.5 New Hardware Integration
Studies on this strategy pertain to the modernization of software in response to changes in underlying hardware.
Recently, certain low-level software computation and memory protection logics have been offloaded to new
multicore CPU architectures [S67]. As these multicore platforms have become more widespread, new programming
patterns have also been introduced to ensure efficient utilization of their computational power [S38]. This serves
as the foundation for modernizing software based on hardware advancements, facilitating the ability to meet
new business requirements [S39].
Driving Forces. In the realm of artificial neural network computation, Computing-in-Memory (CIM) architectures utilizing Non-volatile Memories (NVMs) aim to solve the “memory wall” issue that affects traditional
Von Neumann architectures. As a result, legacy systems must be re-engineered to effectively leverage these
advanced architectures [S48]. Additionally, the concept of reconfigurable hardware is emerging as a major driver
for transitioning existing software to heterogeneous reconfigurable architectures, offering better flexibility and
efficiency [S19]. The automotive industry is experiencing a shift towards multicore processors, which necessitates the modernization of legacy software to fully harness the computational power of these processors to
improve performance [S67]. Moreover, with the development of the Logical Execution Time (LET) programming
model, this approach has become a key paradigm for migrating legacy single-core applications to multicore
environments [S97].
Research Opportunities. In the analysis of the primary sources of our study, we identified two challenges that
should be addressed with further research to support modernization when the goal is to integrate new hardware.
Application of Sophisticate Evaluation Metrics: Identifying potential solutions (migrated versions) is both timeconsuming and critical to the migration process. One paper highlights the importance of performing a trade-off
analysis when selecting a solution from a set of potential options. Stakeholders must be cautious, as optimizing for
one requirement may negatively impact others [S101]. A related direction for future research is the mechanical
verification of whether the modeling constraints are sufficiently strong to ensure the preservation of sequential
program semantics after parallelization [S38].
Creating Tools to Support Program Transformation: In the process of designing a compilation tool based on CIM
architecture for code transformation, the authors of a paper observed that their original algorithm, particularly in
areas like graph processing and genome analysis, often required additional transformations. These transformations
were necessary to convert the problem into formats suitable for operations such as Matrix-Vector Multiplication
(MVM), Matrix-Matrix Multiplication (MMM), or bitmap logical operations [S48]. Another paper mentions that
while manual optimizations could yield further improvements, they would necessitate significant code rewrites
to align with their design methodologies [S19]. However, this would compromise the portability of the software
across different devices and platforms, while also significantly increasing the effort required for testing and
verification at every possible deployment stage. Another challenge pointed in one paper is the way dealing
with is the optimization of memory allocation in multicore LET-based system [S97]. A similar challenge raise is
about resource conflicts, race conditions, task synchronizations, guaranteed execution time and freedom from
interference [S67]. Given the complexity of the programming paradigms of these new pieces of hardware, new
tools are required to assist engineers when transforming the legacy systems to accommodate such hardware.
4.6 Leverage Automation
This migration strategy focuses on easing the development and deployment process through the introduction of
DevOps in the maintenance of legacy system management [S3]. The time spent on software maintenance could be
reduced if manual tasks are automated. Automatic capabilities could be applied to tuning system configurations
to optimize system performance and reduce human intervention [S65].
Driving Forces. One paper emphasized the integration of DevOps techniques into legacy system management,
noting that adopting DevOps can significantly lead to both faster time to market and reduce operational cost [S3].
However, as maintenance and operational costs continue to rise even with DevOps practices, another study
suggested the adoption of autonomic computing techniques to further reduce these expenses for better flexibility
and efficiency [S65]. Additionally, we came across an innovative approach in another paper, which proposed
applying automatic transformation techniques for cross-platform development [S13]. This method has the
potential to simplify the handling of device-specific characteristics, ultimately reducing development cost and
complexity [S3, S13, S65, S117].
Research Opportunities. We found out two directions for future work on this strategy:
Taking Advantage of Autonomic Computing Strategies: Autonomic computing systems can self-manage and adapt
with minimal human intervention. One paper highlights that incorporating autonomic computing capabilities
into existing software presents significant opportunities [S65]. By developing frameworks and techniques for
integrating these capabilities in a cost-effective manner, organizations can enhance system reliability, reduce
operational overhead, and improve responsiveness to business needs.
Providing Tools for Automation of Development: There is a need for sophisticated refactoring tools that can
effectively manage legacy codebases while ensuring alignment with modern practices such as Continuous Integration/Continuous Deployment (CI/CD) and containerization [S3]. These tools should automate the refactoring
process, helping to maintain code quality and streamline deployments, ultimately reducing technical debt.
4.7 Database Modernization
This strategy refers to modernization activities related to databases. Database modernization encompasses the
adoption of new database related technologies and the integration of data from multiple sources to enhance
performance and scalability. This is a crucial activity for efficient continuity of business operations, mostly in
cases when businesses merge or acquired [S94].
Driving Forces. The main driving forces for the modernization of databases is to optimize data integration
strategies, especially for the digitization of legacy systems, enabling effective communication and data exchange
across diverse platforms [S126]. Moreover, we noted that during business acquisitions and mergers, efficient
data migration becomes crucial for maintaining operational efficiency and ensuring interoperability among
systems [S94]. One paper mentioned that the issues associated with horizontally scaling traditional relational
databases have also prompted a shift towards more flexible and scalable alternatives, such as NoSQL databases,
which can better accommodate the demands of modern data-intensive applications [S20] for better flexibility and
efficiency [S126].
Research Opportunities. Among the set of primary sources, we identified two research opportunities for the
challenges of this strategy.
Data Migration Between Databases: Research into efficient data migration between relational databases and
NoSQL systems should be a high priority, especially given the increasing adoption of NoSQL databases. While
some authors have addressed aspects of this issue [S20], extensive work is still needed to explore additional
techniques and compare them in terms of security, performance, and implementation feasibility [S111].
Preparing Databases for Systems Interoperability: In the context of Industry 4.0, achieving seamless interoperability among different systems requires a unified and consistent database infrastructure. Thus, researchers must
focus on creating platforms or infrastructures that support data interoperability [S126]. In this context, it can
also become handy to recover models from database schemas, although this has been attempted with the use of
model-driven reverse engineering [S96], it is worth extending the previous implementation or introduce novel
approaches.
4.8 Digital Transformation
Digital transformation is currently a trend and is receiving great attention around the world. For example, the
European Union has the Digital Europe Programme,6 Australia has the Digital Economy Strategy,7
in North
America there are the Canada Digital Adoption Program8
and the Digital Strategy9 of the United States, and
in Asia 11 countries have joined forces in the Connecting Capabilities.10 Despite expected benefits, the digital
transformation is hampered by legacy systems [15]. In this context, modernization is a means to leverage the
digital transformation [15, 60].
For this strategy, we found studies related to modernization towards Industry 4.0. In the advent of new
technologies and new requirements in the field of Information Technology and Operational Technology [S36],
industries need to integrate existing components with modern components due to interoperability among modern
components. Thus, it is necessary to for industries to adopt modern technologies to remain competitive in the
long term [S76].
Driving Forces. One paper proposes a layer to integrate to the legacy devices, enabling interoperability among
systems, mapping field device data into an existing information model [S36]. Another study seeks to improve
performance, integration, and the overall streamlining of processes, safety, and system interoperability for legacy
systems [S76]. The goal is to provide an economical solution by allowing the continued use of existing facility
devices while transitioning to Industry 4.0. Also, for another group of authors, modernization of legacy systems
is key to remaining competitive and find new business opportunities [S115].
Research Opportunities. Given that we found only three papers addressing modernization for digital transformation, then we observed mainly two research directions.
Using Digital Twins to Analyze the Modernizations: In one paper, the authors proposed using digital twins
to enable the adaptation of legacy systems, intending to enable the simulation of the system’s behavior across
various operating conditions [S76]. This can give insights into performance optimization without the necessity of
physical prototyping or testing.
Automated Tooling Support for Reconfiguration: A challenge pointed out by a study is that to leverage interoperability, it is necessary to detect changes and reconfigure factory floor devices. Thus, there is a need to further
advance tools that allow devices to self-organize themselves using techniques like automated scaling and software
defined networks [S36].
5 DISCUSSIONS
Figure 3 presents a summary of the results with the relations between driving forces and modernization strategies,
as well as between modernization and challenges. This figure also allows us to analyze which driving forces and
challenges are common for different modernization strategies. Figure 3, together with Tables 2, 3, and 4, and the
results presented above; are the basis to answer the three RQs of our study.
RQ1: (From>To Strategies) What are the contemporaneous strategies to modernize legacy systems? Our
study identified eight modernization strategies (see Table 2) described in existing literature, namely modernization
with a focus on: Cloudification, Architecture Redesign, New Programming Language, Reuse Optimization, New
Hardware Integration, Leverage Automation, Database Modernization, and Digital Transformation. Cloudification
has the most number of studies (41, see Table 2), which we subcategorize into simple transition to the cloud,
adoption of SOA, and migration to microservices. According to Figure 3, we can see the decision to embrace
Cloudification based on several driving forces (10), followed by Architecture Redesign (five driving forces) and
New Programming Language (four driving forces). All strategies have been explored over the last 10 years (see
Column Pub. Trends in Table 2), with some differences for Database Modernization and Digital Transformation.
While the former has studies almost every other year, the latter has been more explored in the last year.
RQ2: (Driving forces) What are the common driving forces for modernizing a legacy system? Our
study identified 14 distinct driving forces (see Table 3) among the 127 primary sources. These driving forces
are grouped in three main categories. First, seven Technical driving forces: Architecture Understanding, Avoid
Duplications and Inconsistency, Improve Data Quality, Improve Performance and Scalability, Interoperability
Among Systems, Leverage Reuse opportunities, and Reduce Complexity. Second, we observed three Operational
driving forces: Better flexibility and Efficiency, Enhance Agility, and Reduce Operational Costs. Third, there
are four Organizational driving forces: Faster Time to Market, Foster Innovation, New Business Opportunities,
and Provide External Services. Among those, Reduce Operational Costs (related to five strategies), Improve
Performance/Scalability (four), and Interoperability Among Systems (four) are the most common across different
modernization strategies (see the number of relationships between strategies and driving forces in Figure 3). This
is a logical result, as the demand for software increases on a daily basis, and new pieces of software are developed,
performance, interoperability, and operational costs are critical concerns.
RQ3: (Challenges) What are the challenges and research opportunities in the field of software modernization? Despite many papers addressing software modernization, there are several open challenges and
research gaps. Based on them, we collected 16 challenges that motivate 27 research opportunities for future work
(see the relations between strategies and challenges in Figure 3). By far, the most prevalent opportunity is the
development of tooling support (mentioned in 45 papers in Table 4) for seven different types of strategies (see
Figure 3). Then, Define a Modernization Process (in 21 studies), Consider Better Evaluation Metrics (in 20 studies),
Explore Automatic Computing, and Prepare the Legacy Data/System (mentioned in 11 studies each) are the most
commonly mentioned challenges. For evaluation metrics, the papers describe the need for considering different
sources of information (e.g., databases and documentation). The research opportunity related to the correctness
of modern systems (mentioned in nine papers) refers to avoiding transferring problems from the legacy system
during modernization, such as antipatterns. Future work on Cost-Benefit Analysis (mentioned in eight papers)
should focus on to what extent a certain modernization strategy is beneficial for the company’s context.
5.1 Threats to Validity
In this section, we discuss the main threats to validity related to our study and present how we mitigated them
based on [7, 21, 89].
Construct Validity. Utilizing an RR protocol [22] can bring different biases to the study due to the possible
limitations compared to an SLR [56]. These limitations include a limited number of sources used (DLs), only one
reviewer analyzing the papers (selection bias), and a lack of quality assessment questions (quality bias) [21]. To
mitigate these threats, when planning the protocol for our RR, we incorporated recommendations from the SLR
protocol. For example, RRs commonly use only one source to retrieve the papers. In our case, we considered
five distinct DLs (as described in Section 3). This led to a total of 3,460 studies retrieved (a similar number found
in SMSs or SLRs). Furthermore, to avoid selection bias, all papers were analyzed by two of the authors, with a
third author resolving conflicts when required. Lastly, although we did not use quality assessment metrics we
mitigated the problem of low-quality or incomplete studies being analyzed by only considering published work
in peer-reviewed venues (e.g., no arXiv-only studies were included) where the number of pages was greater than
five for double-column papers and ten for single-column papers. These two criteria helped us avoid including
vision, incomplete, or low-quality studies in our result analysis.
Internal validity. Another potential threat is the limited number of studies analyzed, which may not fully
represent the broader field of software modernization. To address this, we mitigated the issue by selecting and
analyzing a substantial number of studies (127 primary sources). Compared to other related reviews (see Section 6),
our analysis includes studies from different domains of software modernization (e.g., cloud, microservices, and
software product lines), enhancing the comprehensiveness of our review and broadening its scope in comparison
to others.
External Validity. One potential external threat relates to the coherence of our results. We based our RR
protocol on established guidelines [22], even taking recommendations from SLR guidelines [56]. We argue that
this led to satisfactory outcomes in answering our RQs. When analyzing the data, we aimed for a broad perspective
that includes both academic and practical viewpoints. Another threat involves incorrectly identifying challenges
and research opportunities (RQ3). To mitigate this, we extracted limitations and future work highlighted by
authors in each study and examined their coverage across the other studies. We also noted common future work,
such as the development of supporting tools for managing the modernization across different modernization
strategies.
Conclusion Validity. Researchers are often unaware of their own biases during the analysis and classification
of studies, which can negatively impact the results of an RR. Additionally, data extraction inaccuracies pose
another threat. To mitigate these threats, two authors independently conducted the selection and data extraction
of the studies. In case of discrepancies, a third author was consulted to resolve them. Lastly, the “fishing and
error rate” issue could influence the conclusions. This potential threat was mitigated by forming conclusions and
answering RQs only after a full analysis of all primary studies.
6 RELATED WORK
There has been a focus on software modernization in the past years, with different methodologies being employed
to collect and analyze the state of the art and the practice [28, 32, 47, 90]. In this section, we describe how related
work has explored different faces of software modernization from both the literature and industrial perspectives,
while still falling short on covering the aspects that we present in our work.
6.1 The State of the Art
Since cloudification is prevalent in the practice of software engineering, the study by Zhao and Zhou [91]
investigates the migration of legacy systems to the cloud, addressing both the challenges and benefits of such
migration. The authors analyze existing literature and industrial applications, classifying migration methods into
three strategies based on cloud service models: Infrastructure as a Service (IaaS), Platform as a Service (PaaS), and
Software as a Service (SaaS). Besides the work by Zhao and Zhou, other studies have also focused on migration
to the cloud [32, 42, 47, 50, 69]. More recently, Hajlaoui, Trifa, and Brahmi [45] investigated how migration to a
cloud platform influences technical and business challenges that arise, particularly for small and medium-sized
enterprises (SMEs). Their study highlights the complexity and cost of migrating applications between cloud
providers, emphasizing the difficulty of selecting the best migration strategy, even with available guidelines. The
work by Abdellatif et al. [2] focuses on service identification approaches for migrating legacy systems to SOA.
The authors conducted an SLR analyzing 41 approaches, categorizing them based on inputs, processes, outputs,
and usability. This SLR was also validated by industry experts, highlighting that most approaches are still in the
early stages.
Still related to cloudification of legacy systems, one of the most extensively explored topics is the migration
to microservices [2, 12, 14, 64]. For instance, Wolfart et al. [90] highlights the complexity of the modernization
process, emphasizing the lack of comprehensive studies covering real-world scenarios that include organizational,
operational, and technical factors. While the roadmap in their work focuses specifically on microservices, our
work presents a more diverse analysis of modernization trends. Another study focusing on microservices maps
the entire modernization process, covering both technical and systemic organizational changes [64]. The authors
employ a grounded theory approach, analyzing 19 interviews and 215 Stack Overflow discussions to identify two
modes of change, 14 activities, and 53 solution outcomes. They emphasize that successful migration requires both
short- and long-term perspectives, addressing technical and business considerations.
Despite the major focus on cloud modernization, other aspects of software are also considered. The work
by Fritzsch et al. [39] explores the challenges of modernizing legacy systems in the domain of Cyber-Physical
Systems (CPS), focusing on analyzing how microservices and DevOps, widely studied in enterprise systems, apply
to CPS. By conducting a RR of 146 scientific papers and validating findings through interviews with nine CPS
professionals from Siemens AG, the study identifies the challenges and practices relevant to CPS modernization,
comparing them to those in enterprise applications. The findings reveal that, while some CPS-specific differences
exist, many challenges and practices are shared across both domains. Similarly, Jatain and Gaur [51] focus on
the re-engineering of object-oriented legacy systems, exploring the benefits of component-based systems over
traditional object-oriented approaches.
Amongst the other subdomains of software modernization, re-engineering legacy software to SPL aims at
maximizing reuse while minimizing maintenance costs [61]. In this context, the work by Assunção et al. [8]
explored how re-engineering can be adopted to modernize legacy systems, considering the process, tools, and
strategies used. Other approaches have also explored the processes of modernizing for different contexts, such
as considering the implementation phases [13, 82] and how to rank different software modernization solutions
based on the predetermined evaluation criteria [52].
In comparison to the aforementioned related work, our study aims to provide an understanding of modernization
trends across a wide range of systems, highlighting key challenges that span multiple domains, including enterprise
systems, cloud environments, transition between programming languages, new hardware devices, and beyond.
6.2 The State of practice
Software modernization is a topic closely related to industry. Thus, we also consider the several industrial-focused
studies contributing to the topic [14, 58]. Khadka et al. [53] investigate the practitioners’ perceptions of legacy
systems and their modernization, involving interviews with 26 practitioners and a survey with 198 respondents.
The authors conclude that modernization challenges are not solely technical, but also encompass business and
organizational dimensions. Similarly, the work by Abdellatif et al. [1] focuses on migrating legacy systems to
SOA, with a specific emphasis on the challenges of identifying services within the target application. In a survey
with 45 industry practitioners, the study reveals key drivers and methods for service identification, including the
frequent use of domain knowledge and source code. Additionally, the study highlights the limited automation of
service identification and offers recommendations and best practices for the migration process.
When focusing on migration to the cloud, the work by Aubé and Polacsek [11] investigates high-level requirements driving cloudification, based on insights from a qualitative study involving cloud migration experts.
The study identifies 11 key requirements that influence design decisions during migrations, alongside two
classifications aimed at guiding the elicitation and analysis of these requirements. For the modernization with
microservices [40], the work by Di Francesco et al. [34] investigates the challenges faced by companies migrating
to microservices. It reports findings from an empirical study based on interviews and questionnaires with practitioners. Once again, the study is not limited to technical problems but also organizational challenges during
the migration. In the same direction, Carvalho et al. [24] explore the criteria practitioners use for extracting
microservices during system migrations, reporting findings from an exploratory survey of 15 specialists. The
results highlight the importance of using multiple criteria (e.g., coupling and cohesion) for effective microservice
identification. This study also emphasizes a gap between academic methods and practical needs, particularly the
inadequacy of current tooling support. Another work investigates best practices, challenges, and solutions in
microservice-based application development [88]. Their investigation focuses on “mature” teams with over two
years of experience. The results, obtained from interviews and surveys, reveal that practitioners often deviate
from standard recommendations, such as splitting services by business capabilities, highlighting the importance
of robust infrastructural support.
Although these pieces of work bring several contributions to the understanding of practical aspects, they
are limited to a few modernization strategies. In our study, we have not included surveys or interviews with
practitioners, but our results can serve as a starting point for understanding current practices in software
modernization and for validating them with practitioners in future work.
7 CONCLUSIONS
Software modernization is a fundamental activity of software engineering, since requirements inevitably change,
technologies advance, and new business models emerge. Despite that, research on this topic has not followed
modern software development, and legacy systems still remain a problem. To fill this gap and to spark research
on this topic, we present an RR on software modernization in light of contemporary software modernization. We
reviewed 127 papers, of which we identified eight contemporaneous strategies, 14 different driving forces, and 27
research opportunities (based on 16 challenges) to be considered.
Our study relied on an RR to understand the existing literature, focusing on the practical concerns of software
modernization. Future work can investigate different aspects and perform more comparative and complementary
analysis among the primary sources by applying other methodologies such as systematic literature review or
systematic mapping. For instance, a future study can focus on identifying the steps performed in the studies to
conduct the modernization process, collecting what are the main artifacts used as input and produced as output
for different strategies, and exploring how the studies evaluate their proposed methods. Furthermore, research
on software modernization based on surveys and interviews with practitioners (as discussed in Section 6) can
enrich the understanding of the practices and challenges faced in the industry.
In addition, and based on our experience in the field of software modernization, we also envisage some research
directions not found in our RR. For example, in the background, we present five quadrants (i.e., replace, maintain,
evolve, re-engineer, or migrate) of the portfolio analysis to support companies in deciding which modernization
strategy to adopt. Choosing how to modernize a legacy system is a multi-criteria decision, so companies need
solutions to help them address this challenge. To this end, we expect future work to propose recommendation
approaches to support decision-making in terms of modernization options. Another direction of research is about
non-intrusive migration approaches. Practitioners usually have preferences for using certain technologies, tools,
and workflows. Based on that, researchers should propose modernization approaches and tools that take these
preferences into account. Non-intrusive approaches are easier to transfer to practice [30]. Finally, the existing
literature indicates that some software engineering activities should be performed differently in the context of
SMEs [31, 77]. This might also be the case for software modernization [6]. Hence, research needs to be conducted
on challenges faced by SMEs when modernizing their legacy systems in order to grow and expand their business.