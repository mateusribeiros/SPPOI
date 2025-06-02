Title: An Ethnographic Study on the CI of A Large Scale Project

Abstract:
Continuous Integration (CI) is the foundation for achieving rapid
iteration and short-cycle delivery. To achieve CI, a series of best
practices and solutions have been proposed, which are referred
to as patterns. However, there is a natural contradiction between
the speed and continuity pursued by CI and the ever-expanding
project scale and complexity. Various factors such as project size,
outdated system architecture, complex organizational structure, or
limited server resources can all lead to deviations from patterns
in CI practices, resulting in anti-patterns. We conducted an ethnographic research to investigate the current state, anti-patterns, and
challenges in resolving anti-patterns of the CI process within a
large communication project at a globally leading IT company. We
conducted a deep observation and participation in the project for
seven months and conducted multiple rounds of interviews with
related developers in the company. The project adopts a CI pipeline
that has a three-level hierarchical structure. We evaluated the company’s software development practices based on the pattern list.
We identified three anti-patterns that contradicted the patterns
listed, and we also discovered three new anti-patterns that were
not on the list. Further, we analyzed the challenges of solving these
anti-patterns. Additionally, we found seven better practices and
analyzed why they are better.

Keywords:
continuous integration, ethnographic study, anti-patterns, best practice

1 INTRODUCTION
The demand and requirements for software are constantly increasing. In order to quickly launch commercial software, many development teams have started delivering value by reducing delivery
cycles and accelerating version iterations [1, 2]. In this context,
agile principles and DevOps are gaining popularity, and companies
are seeking optimized end-to-end processes that provide feedback
on what is being built. Continuous Integration (CI) has become a
mainstream software development approach for these concepts.
Continuous Integration is a development approach where code
changes are frequently submitted to the main branch. This requires
developers to submit multiple code changes daily, which triggers
automated testing and building tasks on the integration server [3].
CI has the potential to speed up development and help maintain
code quality [4]. CI is a key component of DevOps practices and
helps improve software delivery efficiency by reducing risks, providing timely feedback, accelerating product iteration, boosting
morale for development teams, as well as reducing repetitive work
for personnel. Consequently, applying CI leads to improvements in
both software quality and delivery efficiency simultaneously.
With the development of DevOps and related automation tools,
CI has become increasingly easier. However, there are still challenges in implementing it for system development. Best practices,
known as CI patterns, have been proposed to help leverage this approach [5]. However, developers often deviate from these practices
and create anti-patterns that can have unintended consequences [6].
Anti-patterns are not necessarily bad practices but can produce adverse effects compared to implementing the pattern correctly [5].
Duvall [5] proposed 37 specific patterns and corresponding antipatterns in 2010. With the continuous development of DevOps,
some patterns have been well adhered to, and the corresponding
anti-patterns have been well solved. For example, Duvall [5] mentioned that having multiple copies of the same JAR dependency
in each project is an anti-pattern, but this anti-pattern has been
well solved by the maven tool. However, some anti-patterns remain
difficult to solve due to the complexity of large-scale systems and
their development models. To investigate the current industry practices of continuous integration patterns, we derived three Research
Questions (RQs) as follows:
• RQ1: What is the CI process of the large-scale software
development project? We try to fully grasp the project’s
continuous integration practices, which helps us better understand the background and reasons for the emergence of
anti-patterns.
• RQ2: Compared to patterns, what are the practices in
the project that are the same, better, or worse (antipatterns)? Compared to the list of patterns from Duvall [5],
We try to figure out which practices are the same, which
practices are better, and which practices are worse (antipatterns).
• RQ3:What are the challenges and practical constraints
of addressing the anti-patterns that currently exist?
Our ultimate goal is to address anti-patterns. However, due
to the system’s scale, complexity, and the challenging nature of optimizing the software architecture, there are still
many challenges in resolving these anti-patterns. We try
to refine and analyze these challenges.
The research aims to investigate the current state, anti-patterns,
and challenges of solving anti-patterns in CI processes in large
complex projects. We conducted an ethnographic research. One
of the authors of this article joined the project team as an intern
and carried out an internship for seven months. During the internship, he closely observed the project development process and
participated in the project development. In addition, to further confirm his observations, we conducted five rounds of interviews with
relevant developers. In the large-scale communication software
development project studied in this paper, it takes a week to complete one end-to-end integration of the system. This is far from
Fowler’s recommendation to keep CI within 10 minutes1
and also
deviates greatly from our usual understanding of the “continuity”
of CI. Obviously, there are some anti-patterns in the development
of this project that have not yet been solved. The contributions of
this article are as follows:
(1) We assessed the company’s software development practices based on the authoritative pattern list. We identified
three anti-patterns as listed and discovered three new antipatterns that were not on the list.
(2) Furthermore, we found six better practices and analyzed
the reasons for their effectiveness.
(3) Additionally, we analyzed the challenges addressed by these
anti-patterns. We considered two of the anti-patterns to be
painless, as they did not increase the developer’s burden
or are unavoidable. We then analyzed the challenges of
1http://martinfowler.com/articles/continuousIntegration.html
resolving the remaining four anti-patterns and summarized
the lessons learned.
The remainder of this paper is structured as follows. Sec. 2 introduces related literature on CI empirical studies and CI anti-pattern
studies. Sec. 3 discusses the overview of the methodology. The process of CI in this project is depicted in Sec. 4. Sec. 5 gives the specific
practice in the project based on the pattern proposed by Duvall [5],
identifies the anti-pattern and describes the details. Sec. 6 then discusses what challenges exist in solving these anti-patterns. Sec. 7
discusses lessons we learned from our research, and points out the
directions of the future research. Sec. 8 discusses possible threats
to the validity of the study, followed by the conclusions in Sec. 9.

2 BACKGROUND AND RELATED WORK
In this section, we discuss the background and related work on
patterns and anti-patterns. Then we highlight the value and significance of this study compared with previous studies.
2.1 Background
Patterns are identifiable and reoccurring phenomena that regularly occur on all levels of software engineering as characteristic
sequences of specific activities, traditionally supporting the software process [7] [8] [9]. In the CI context, patterns refer to the
best practices summarized during integration. The ideal CI practice
requires all developers to integrate their work into the main code
repository every day. Each integration triggers corresponding build
and test tasks to ensure that the system can still run normally after
changes [10].
However, in recent years, relevant survey results have shown
that there are still many challenges in the application of CI in the
industry [11]. Some practices that do not follow the best practices
are defined as anti-patterns. Anti-patterns may seem helpful on the
surface, but they can actually have the opposite effect. With the
rise of DevOps, many scholars have summarized the patterns and
anti-patterns in CI.
2.2 Related Work
Duvall [5] proposed 37 specific patterns and corresponding antipatterns, covering seven directions: version control, build management, build practices, build configuration, database, testing and
code quality, and deployment. Tighilt et al. [12] conducted a systematic literature review of 27 papers related to microservices and
analyzed 67 open-source microservice-based systems. Based on the
analysis, they reported 16 microservice anti-patterns in this paper,
which are divided into four categories. Zampetti et al. [13] conducted the investigation by leveraging semi-structured interviews
of 13 experts and mining more than 2,300 Stack Overflow posts. As
a result, they compiled a catalog of 79 CI bad smells belonging to
seven categories related to different dimensions of a CI pipeline
management and process.
There were also some attempts to propose tools for detecting
and removing anti-patterns. Gallaba et al. [14] conducted a study on
the use of Travis CI features in open source software development.
After, investigated 9321 open source systems and defined four antipatterns in the Travis CI specification document, They proposed
HANSEL, a tool to detect anti-patterns, and GRETEL, a tool to
Figure 1: Ethnographic Study Process
remove anti-patterns; Vassallo et al. [15] built CI-ODOR, a reporting
tool for CI processes that detects the existence of four relevant antipatterns by analyzing regular build logs and repository information.
Based on a study of the 18,474 build logs from 36 popular JAVA
projects, they reveal the presence of 3,823 high-severity warnings
spread across projects.
Although past researchers have summarized anti-patterns and
proposed some tools to solve them, they lack the experience to
actually examine the challenges of CI in actual large companies.
Compared to previous research, we conduct an empirical study
of anti-patterns in large-scale software projects and explore the
challenges of addressing these anti-patterns in depth. Compared to
Tighilt et al. [12] and Zampetti et al. [13], Duvall’s research focuses
on the CI process and emphasizes the patterns and anti-patterns.
Additionally, Duvall’s research is considered more authoritative.
Therefore, we based our study on the list presented by Duvall [5].

3 OVERVIEW OF THE METHODOLOGY
We conducted an ethnographic study to investigate the CI process in a large-scale communication software development project.
Ethnographic study is a research method that originated in sociology and was developed by anthropologists and sociologists to
study human behavior and culture through participation in daily
activities and observation of people’s behaviors [16]. This approach
helps researchers gain a deep understanding of a particular culture,
including the habits, knowledge, and activities of its members [17].
In software engineering, ethnographic studies help to understand
why collaboration and cooperation support are more problematic
than anticipated [16]. The deployment of ethnographic methods
can provide a strong foundation for elucidating the rationales behind software development practices and thus establish a basis
for developing and devising appropriate processes, tools, and techniques [16]. The overview of the research process of this study is
shown in Figure 1.
3.1 Access to Ethnographic Field
We chose a prominent global company in Information and Communications Technology (ICT) infrastructure and smart devices as
our research target. The company has more than 200,000 employees working in more than 170 countries and regions, serving over
three billion people worldwide. With the increasing popularity of
DevOps, more and more development teams are seeking technical
cooperation and exploring new ways to improve their DevOps capabilities in order to enhance research and development efficiency.
The team at this company is representative of this trend.
The large communication project we investigated provides services for the telecommunications fields in many countries around
the world. It is an enormous system with tens of millions of lines
of code. Currently, the system has achieved a service-oriented and
containerized product architecture.
In this paper, one of the authors was an intern at the company
and conducted an in-depth ethnographic study of the company’s CI
activities. After a seven-month internship, he successfully became a
full-time employee of the company due to his excellent performance
during the internship. He was a second-year master‘s student majoring in Software Engineering, and he also had an outstanding
academic record during his undergraduate studies in Computer
Science. He was admitted to the graduate program through recommendation. He had over six years of programming experience and
had systematically studied courses related to empirical software
engineering, including methods from ethnographic research. He
focused on research in software processes and DevOps and had
gained experience conducting interviews.
3.2 Data Collection
Our ethnographic research process mainly consists of the following
two steps.
3.2.1 Participant observations. The intern worked in the company
for a total of seven months. During this period, the intern focused on
using artificial intelligence technology to enhance the company’s
continuous integration process. To achieve this, he closely observed
and actively participated in the execution of the third-level continuous integration pipeline, gaining insights into and documenting
the advantages and shortcomings of continuous integration in the
project.
3.2.2 Interviews. In order to understand the integration operation
mechanism and existing problems, We first conducted several interviews with the persons in charge of code access control, daily
integration, and weekly integration, respectively. After the intern
became a full-time developer and gain experience, based on the CI
patterns proposed by Duvall [5], we interviewed the developers, trying to obtain the anti-patterns in practice and solve the challenges
of the anti-patterns. The interview configuration information is
shown in Table 1. In the following sections, we present our findings
to answer three research questions.

4 RQ1: THE STRUCTURE OF THE PIPLINES
Table 1: Interview Configuration Information
This system adopts a three-level integration pipelines to improve
the efficiency of CI. Since each integration consumes a lot of time
and resources, triggering a full integration for every commit is
not feasible. With the three-level integration pipelines, a largescale build task can be split into different stages of asynchronous
execution. This approach helps to reduce pipeline congestion and
improves the overall efficiency of CI.
The first level is the code access control stage, which monitors the
quality of code changes based on individual branches and feature
branches. This stage is triggered when developers create merge
requests (MRs) and primarily performs static code inspections, lowlevel test (LLT), and other quality assurance measures. Only after
passing these inspections can the code changes be merged into
trunk branches.
The second level is the daily integration stage. It compiles, builds,
and deploys based on the trunk branch of all code repositories
contained in the product subsystem and mainly performs productlevel integration testing.
The third level is the end-to-end integration stage, which conducts inter-system integration testing based on End-to-End (E2E)
integration branches. This stage is responsible for inter-product
adaptation, build, and integration test.
We use BPMN diagrams to depict the three-level integration
pipeline as shown in Figure 3, 4, 5. The legends of the BPMN diagrams are shown in Table 3.
4.1 Development Process Using Pipelines
The structure of the three-level pipeline in the CI process is illustrated in Figure 2. The company employs a development model
involving multiple repositories and branches. The developed system
comprises numerous subsystems, each with its own set of repositories. For instance, the intern’s project team manages a business
Figure 2: The Structure of Pipelines
subsystem that comprises over 60 different repositories. The largest
repository contains more than three million lines of code.
Initially, developers create a separate branch from the trunk
branch of the subsystem to work on their development tasks. As
the development work may involve multiple repositories, each
repository must create a branch with the same name to pull and
integrate changes made in other repositories.
During the development process, each developer works on their
own branch. Once they have completed their personal development
work, they create an MR to merge their changes into the trunk
branch of the subsystem, which will trigger the code access control
pipeline. If the updated code passes inspection, it will be merged
into the trunk branch.
There are two types of daily integration pipelines, namely incremental builds and full builds. Incremental builds occur every two
hours to build any updates made to the trunk branch. Full builds
happen daily at four a.m. and sequentially build all repositories in
the trunk branch of the subsystem. If successful, it is deployed for
parallel testing on a test platform.
System integration is performed every Monday, and all subsystems are pulled from the main branch of the subsystem and
merged into the end-to-end integration branch (i.e., the system’s
main branch) for adaptation and system testing.
4.2 Code Access Control Pipeline
The code access control pipeline ensures that code changes merged
into the trunk branch meet certain quality thresholds. It involves
control activities before code merging, such as static code inspection, coverage testing, unit testing, and so on. The basic flow of code
access control activities is shown in Figure 3, which involves three
roles, namely Developer, Reviewer, and Committer. After the developer completes local development and validation, the MR request
is created to merge the code into the repository and triggers the
access control inspection. If the inspection passes, the reviewer and
committer will further check the code to decide whether to merge
it. If the inspection fails, the developer will analyze the reason and
modify the code or the access control rules to block the alarm. If
the access control rules need to be modified and the Committer
agrees, the access control inspection will be performed again after
the modification to ensure that there are no other problems, and
then the code is merged.
We selected a repository with frequent changes as the observation object. Access control inspection items are divided into static
code inspection, compilation alarm inspection, and LLT test. These
inspection items are all executed in parallel.
4.3 Daily Integration Pipeline
Daily integration is mainly responsible for product-level builds
and integration tests and is executed based on the trunk branch of
all repositories that comprise the subsystem (product). The daily
integration process of the system is shown in Figure 4, which is
divided into two cases: incremental builds and full builds. Incremental builds are executed every two hours from 8:00 a.m. to 2:00 a.m.
the next day. Its responsibility is compile supervision, ensuring that
compilation problems are detected within two hours to pinpoint
who is responsible for the compilation errors as soon as possible. It
does not perform integration tests. In addition, incremental builds
are based on the commit hash of the trunk branch in the repositories and the version information of the dependent binaries to
determine whether a build is needed. These repositories are valid
only if there are detailed dependency relationships between the
repositories. The full build will be executed at 4 a.m. every day, and
it will pull the daily version branch from the trunk branch of all
code repositories corresponding to the product for full compilation
and build. If the compilation passes, the package will be deployed
to multiple environments, and integration tests will be executed in
a distributed manner. If there is a failure case, the CI Engineer (CIE)
will locate the relevant interface person according to the logs, and
when the defect is fixed, it will be merged into the daily version
branch and rebuilt to verify the failure case.
4.4 Weekly Integration Pipeline
The main process of weekly integration pipeline is shown in Figure 5. The weekly integration activity is divided into three phases:
integration strategy development and preparation, integration execution, and integration care. In the preparation phase, each product
will pull out the end-to-end integration branch from last week’s
daily release branch, i.e., an end-to-end integration branch will be
created in all repositories of all products, and then decompose the
change requirements in the end-to-end integration branch for merging. The change requirements are then broken down and merged
in on the end-to-end integration branch. The integration execution phase takes place on Tuesdays and Wednesdays, with multiple
rounds of builds, test verification, and defect location and repair to
fit the integration. The integration care phase takes place on Friday
when the integration tests have passed. The package is delivered
to the testing department for business testing and problem analysis. Finally the changes on the end-to-end integration branch are
merged back to the backbone branch.
Summary: We presented the CI process of the project, focusing
on its three-level pipeline. We first present the structure of the
pipelines and introduce the development process using pipelines.
Then we discussed each level of pipeline in detail.

5 RQ2: CI PRACTICES
Duvall [5] proposed 37 patterns and corresponding anti-patterns
in seven areas, which are version control, build management, build
practices, build configuration, database, testing and code quality,
and deployment. We conducted detailed interviews with engineers
and experts in the company to investigate if their software development process followed these patterns. If not, we investigated
their actual development practices and whether these practices
were better or worse than the recommended patterns. Due to the
interviewed developer’s limited understanding of the database, we
exclude the database-related patterns. The results of the interviews
are shown in Table 2.
We compared the current practices in the company with the
recommended best practices [5] to classify them into three categories: worse (anti), the same, and better patterns. We denoted them
as ª , ¬ , and © respectively in Table 2. We identified three
new anti-patterns through interviews, which are hard interfaces
changes (UA1), hard branch maintenance (UA2), and manual defect
location (UA3) in the table. The discussions of better patterns and
anti-patterns are as follows.
5.1 Reasons for Better Practices
As shown in Table 2, we identified 7 practices better than the original patterns. The reasons are explained below.
5.1.1 Containerization. Containerized environment variables
(BM2), docker for external release (BM3), image configuration
(BM6), image deployment (BM7), flexible container deployment
(BP1) and builds in container (BC3) use containerization to improve
the original patterns. Containerization technology is a lightweight,
efficient method of virtualization that allows applications and their
dependencies to be packaged and isolated in a single, self-contained
unit called a container [18]. The technology is one of the most breakthrough technologies of the past decade [19].
By containerizing an application and consolidating all its dependencies within a single package, developers can significantly
minimize the reliance on external dependencies. This is achieved
by utilizing of a container runtime, which offers a standardized
environment encompassing all the required dependencies. As a
result, containerization can lead to a more efficient deployment
process and quicker access to the software.
Besides, containers are significantly resource efficient compared
to traditional Virtual Machines (VMs) [20]. Containers are inherently smaller in capacity than VMs, allowing multiple containers
to run on a single host without excessive resources.
5.1.2 Gradle. Practice BC2 uses Gradle to organize and execute
builds. Gradle is an open-source build automation system primarily
used for managing and building software projects. First released
in 2007, it has become a popular choice for many programming
languages and platforms, especially in the Java and Android ecosystems [21] [22].
Gradle has several advantages as a build tool for developers.
Unlike other build tools like Maven, Gradle uses Groovy instead of
XML as the build script, which is declarative, readable, and expresses
its intention clearly, making it easy to write and maintain code [23].
Additionally, Gradle supports incremental builds by specifying task
inputs and outputs. It determines which tasks can be skipped, built,
or partially rebuilt, even in multi-module projects. With Gradle,
unnecessary clean builds are eliminated, improving efficiency [23].
5.2 Painless Anti-patterns
We define painless anti-patterns as anti-patterns that do not increase
the developer burden or are unavoidable. Different deployment
(D3) and manual documentation generation (BP5) are painless antipatterns. D3 is unavoidable for business reasons. BP5 cannot be
solved well with current tools and does not impose much burden
to developers. The detailed reasons are listed below.
5.3 Details of Anti-patterns
According to the results of the interviews, we learned many practices that violate the pattern, that is, anti-patterns. However, long
time tests (TCQ2) and manual defect location (UA3) are comparatively complex in practice and require further explanation. In this
section, we give details for them.
5.3.1 TCQ2: Long time tests. In current CI practices, the build
duration tend to be protracted, primarily due to the extensive assortment of tests when release software, which consumes considerable
time.
In the code access control pipeline, most static code inspection
items are executed incrementally, which generally takes one to five
minutes. Meanwhile, the LLT test is limited by the size of the test
case. Even if the test case is run in a distributed manner, it takes
more than 10 minutes.
In the daily integration pipeline, the incremental build process,
on average, takes approximately 30 minutes and achieves a success
rate of 67%. The total duration of the full build process is approximately 3 hours, with the build phase taking about 40 minutes,
deployment taking 40 minutes, and test case execution requiring
around 1.5 hours. The build task within the full build process has
a success rate of approximately 73%. In addition, some occasional
problems will be encountered in almost every test task, which requires re-running the CI (troubleshooting) process twice to confirm
the actual problem. It is known as flaky test and the troubleshooting
process commonly takes several hours. Although only a few out of
the 800 test cases tend to fail, the pipeline would be delayed by two
to five hours because the defect localization relies solely on manual
effort.
In the weekly integration pipeline, the bottlenecks in implementation are similar to daily integration. For example, it takes about
five hours to complete the build of each product and eight hours to
execute integration tests.
5.3.2 UA3: Manual defect location. According to the feedback,
there might be bugs in the three-level pipeline requiring manual troubleshooting for defect location. Various reasons can contribute to this problem, such as the engineering tool lacking userfriendliness or the test tool failing to generate proper exceptions.
Occasionally, failures occur due to issues like network anomalies or
restrictions, resulting in the inability to fetch system dependency
packages. Consequently, the CIEs need to engage in multiple discussions with developers associated with the pipeline to locate
the specific cause. These repeated discussions further prolong the
pipeline’s duration, leading to a poor work experience for the CIEs.
Summary: We compared the current practices in the company
with the recommended best practices[5] to classify them into three
categories: worse (anti), the same, and better. The results are showed
in Table 2. Then we discussed the reasons for better practices, and
present details for some anti-patterns.

6 RQ3: THE CHALLENGES OF SOLVING
ANTI-PATTERNS IN CI
Engineers are well aware of the anti-patterns given in the previous
section, but they have yet to be able to solve them. In this section,
we present the challenges of solving anti-patterns in the system
based on the results of our interviews. We summary six challenges,
as well as give a schematic diagram of the relationship between
anti-patterns and challenges shown in Figure 6.
6.0.1 D3: Different deployment. This large-scale software needs
to be released on a variety of different platforms, and the hardware
conditions of these platforms are different, including X86 architecture and ARM architecture. Therefore, using different deployment
scripts is unavoidable.
6.0.2 BP5: Manual documentation generation. While technologies are available for automated document generation, the
quality of the generated documents remains unsatisfactory, serving
only as supplementary tools. Currently, manual document writing does not impose excessive burden on developers and remains
irreplaceable.
6.1 Challenges of Solving Anti-patterns
Despite the system’s utilization of a service-oriented and containerized architecture, achieving independent release, deployment, and
testing has proven challenging with the existing technology. The
anti-patterns were a persistent source of frustration for project
engineers, impeding the development process. Consequently, we
conducted extensive interviews to delve deeper into the challenges
of resolving these anti-patterns. The results of these interviews are
outlined below.
6.1.1 Challenges of Solving TCQ2. TCQ2 describes scenarios
where tests take hours to run, leading to excessive wait times and
increased expense. The main difficulties in solving this anti-pattern
are as follows.
Figure 3: BPMN Flow of Access Control Process
Table 3: Component Information of BPMN Diagrams, i.e.
Legends for Figure 3, 4, 5.
(1) C1: Large scale of test cases. Some larger code repositories also have large test case sizes, resulting in longer LLT
testing times, which are the most time-consuming tasks in
gate inspections. When the code is submitted frequently,
there may be a situation of waiting due to insufficient resources.
(2) C2: Developer capabilities vary. Because the system is
too complex and developers have different levels of ability,
quite a few developers cannot understand logs, and CIE is
needed to assist developers in locating problems, which is
inefficient.
(3) C3: Inconsistent test results. The consistency between
local test results and access control test results is often lacking. For instance, due to machine performance limitations,
running a comprehensive set of test cases locally becomes
infeasible, resulting in some issues going undetected locally.
6.1.2 Challenges of Solving UA1. UA1 describes scenarios where
interdependence between components makes it difficult for microservices to identify when they change. The main difficulties in solving
this anti-pattern are as follows.
(1) C4: Extensive code repositories. The project adopts a
multi-repository development , and each component has a
separate code repository. This makes it time-consuming to
find the corresponding code repository when changing the
interface.
(2) C5: Code repositories coupling. Although this largescale system adopts the system architecture of microservices, there is still a lot of coupling between the code repositories.When the interface of a repository changes, the corresponding interfaces in all dependent code repositories
need to be changed.
6.1.3 Challenges of Solving UA2. UA2 describes scenarios where
maintaining and developing multiple branches increases the burden
on developers. The main difficulty in solving this anti-pattern is as
follow.
(1) C6: Multiple branch development. Due to the diversity
of user needs, the system does not follow the principle of
trunk release, resulting in the release of multiple branches
that need to be maintained, which greatly increases the
workload of developers
6.1.4 Challenges of Solving UA3. UA3 describes scenarios where
Inefficiency of manual defect location. The main difficulties in solving
this anti-pattern are as follows.
(1) C4: Extensive code repositories Defects may exist in different code repositories, making it difficult to locate defects.
(2) C6: Multiple branch development Defects may exist in
different branches, making it difficult to locate defects.
(3) C7: Missing detail error information Due to the lack
of detailed error message of the pipelines, engineers often
have to discuss repeatedly with several related colleagues
in order to locate the defect, which seriously affects the
efficiency of integration.
Summary: We discussed the challenges of solving anti-patterns in
CI. We first identify two painless anti-patterns. Then we discussed in
detail the challenges of addressing the remaining four anti-patterns
7 DISCUSSION
Multi-repository development divides a large system into smaller
components, each with a separate source code repository. With the
increasing complexity of modern software and the rise of microservices, multi-repository is becoming more and more popular among
companies [24].
The project investigated in this paper adopts a multi-repository
development. Despite the advantages mentioned above, it also
causes a lot of trouble for CI practice. Since the components are not
decoupled, complex repositories make it difficult to adapt interfaces
between components when requirements change. This enlightens
us to consider using full-text search tools, such as ElasticSearch [25],
to index the code, enabling efficient querying of API calls. In addition, since each repository has its own integrated pipeline, it
is particularly difficult to locate defects. This enlightens us to develop a high-performance logging system where logs from various
stages can be uniformly stored and managed, and to consider using
automated defect localization methods.
Besides, for situations of multi-branch parallel development, Software Product Line Engineering (SPLE) may be an excellent solution.
A software product line is a set of software intensive systems that
share a common, managed set of features satisfying the specific
needs of a particular market segment or mission and that are developed from a common set of core assets (artifacts) in a prescribed
way [26]. SPLE exploits the commonalities of the systems that belong to a product line and systematically handles the variation
among those systems, which can be divided into two parts: domain engineering process and application engineering process [27].
The domain engineering process is responsible for defining the
commonality and the variability of the product line, as well as for
developing the domain artifacts (platform); the application engineering process is responsible for deriving concrete applications
from the domain artifacts [27].
In addition, from this study, it can be observed that certain practices once deemed anti-patterns, such as the painless anti-pattern
we identified in this study, are not aligned with current software development trends and are impractical. This also serves as a reminder
that past best CI patterns and anti-patterns should be reevaluated
to adapt to the increasingly complex nature of software projects.

8 THREATS TO VALIDITY
Although ethnographic research can allow researchers to better
understand the software development process, there are also some
possible shortcomings.
As a master student, the intern may not have enough experience
in software development to have a precise and comprehensive
understanding of each pipeline. In order to reduce the impact of
this deficiency as much as possible, the intern did an internship
in the company for up to seven months, deeply participated in
the company’s development process, and finally became a fulltime employee. Furthermore, We conducted the interviews after he
became a full-time employee with experience.
Another possible threat is that, due to the highly technical and
industry-specific nature of the field of software engineering, research done on a particular system may not be appropriate for other
systems. In order to reduce this threat, we chose a large-scale communication system based on microservices and multi-repository
development model for research, and such a system architecture
is the mainstream of a software development at present. Therefore, our research conclusions can be applied to most software
development processes.

9 CONCLUSION
We investigated a large software project using ethnographic study.
One author observed the development process as an intern and
gained insights into the system’s CI practices. The system comprises three-level pipelines: code access control, daily integration,
and weekly integration. Interviews were conducted with project
developers and pipeline leaders, following the pattern list proposed
by Duvall [5]. Through these interviews, we identified seven better
practices and six worse practices (anti-patterns) compared to the
pattern list. We further categorized them into two painless antipatterns and four painful anti-patterns. We also identified and explained seven challenges associated with the painful anti-patterns.
During the research, we discovered that despite adopting a microservice architecture, the project exhibited high coupling, hindering independent modification of microservices when code changes
occur. Additionally, the system’s numerous code repositories and
complex branches contributed to some anti-patterns. Therefore, We
explored the possibility of using code indexing, log improvement,
and SPL techniques to address existing anti-patterns.