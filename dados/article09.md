Title: Measuring Technical Debt in AI-Based Competition Platforms

ABSTRACT
Advances in AI have led to new types of technical debt in
software engineering projects. AI-based competition platforms
face challenges due to rapid prototyping and a lack of adherence
to software engineering principles by participants, resulting in
technical debt. Additionally, organizers often lack methods to
evaluate platform quality, impacting sustainability and
maintainability. In this research, we identify and categorize types
of technical debt in AI systems through a scoping review. We
develop a questionnaire for assessing technical debt in AI
competition platforms, categorizing debt into various types, such
as algorithm, architectural, code, configuration, data etc. We
introduce Accessibility Debt, specific to AI competition platforms,
highlighting challenges participants face due to inadequate
platform usability. Our framework for managing technical debt
aims to improve the sustainability and effectiveness of these
platforms, providing tools for researchers, organizers, and
participants.
CCS CONCEPTS
• Software and its engineering → Software creation and management; • Computing methodologies→Artificial Intelligence;
• Applied computing → Education.
KEYWORDS
Technical Debt, AI-Based Systems, AI-Based Competition
Platforms, SE4AI, SE4ML, AI-Training, AI-Education
1 INTRODUCTION
In recent years, progress in Artificial Intelligence (AI) has led to
the integration of AI components into an increasing number of
software engineering projects, now known as AI-based systems
[14, 23]. Even though experienced development teams deliver
these projects, they present several new challenges [24].
A most significant challenge is the emergence of new types of
technical debt related to AI, which accumulate alongside those
already present in traditional software systems [3], negatively
impacting their sustainability and maintainability.
Technical Debt in AI systems refers to the long-term maintenance
challenges and hidden costs caused by rapid development and
deployment. It includes issues like boundary erosion,
entanglement, hidden feedback loops, and data dependencies [1],
as well as the need for robust abstractions, modular design, and
continuous monitoring, which complicate system updates and
maintenance over time.
There is a considerable body of recent research on determining,
describing, and classifying the types and characteristics of
technical debt in AI systems [25], with the primary aim to come
up with principles, guidelines, patterns and tests that will ensure
the sustainability and maintainability of these systems [30].
A particularly interesting category of such projects are AI-based
competition platforms, commercial, academic – research or
hybrid, which are utilized by organizations, companies, and
universities [21, 25-29] to competitively identify solutions to a
problem, while at the same time training participants, either on
technical aspects or on soft aspects of AI [16]. Such platforms can
vary significantly depending on the scientific field they focus on
(medical, robotics, public health, environmental science, ethical
AI, computer Vision, NLP, training, etc.), on the community they
target (researchers, academics, students, professionals, AI
developers and hobbyists), on the infrastructure utilised (open
source, closed source, cloud computing), on the specific features
they offer (code sharing, custom metrics), and on the cost of using
them (free, paid). Monetary prizes, recognition, job opportunities,
or academic credits may be offered as incentives [25].
Competitions remain active for a predetermined period, ranging
from a few hours to several months [15], during which
participants can submit their proposals to solve the given problem. 
During the competition, participants emphasize rapid prototyping
and iterative design processes. They quickly iterate on their ideas
for the problem and experiment with mechanics and game
elements to find what works best within the given timeframe. The
focus is on creating playable prototypes rather than polished, final
products.
After the submission deadline, organizers evaluate the proposed
solutions, and the winner is determined [15]. The criteria for
rewarding the winner are defined based on the nature of the
problem, with the most common being the efficiency of the
algorithm (fast response, low resource usage, etc.). Based on
frequency and organizational details, competitions can be further
classified as One-time, Recurring, Continuous, Series, or
Tournaments.
AI-based gaming competitions have gained significant ground in
recent years within the academic community [31]. Due to their
engaging approach of interacting with students, they accelerate
research while simultaneously serving as a premier tool for
instruction [15, 16, 33].
Despite their success and student participation, it is observed that
within the context of a competition hosted on a university
platform, it is common for students to engage only once, primarily
driven by the objective to fulfill course requirements. During this
process, participants develop algorithms without a clear indication
of their adherence to established programming practices or the
fundamental principles of software engineering for AI (SE4AI) [3,
4, 32, 34]. This lack of adherence may lead to the gradual
accumulation of technical debt within the platform itself.
Furthermore, competition organizers currently lack a quantifiable
method to evaluate the quality of their platform. This deficiency
hampers their ability to prevent the accrual of long-term technical
debt, which could undermine the sustainability and
maintainability of the platform, thereby diminishing the
competition's credibility.
Motivated by the aforementioned objectives, we sought to address
the research gap observed in managing technical debt through the
application of best practices and fundamental software
engineering principles [4], specifically within AI-based
competition platforms in the university setting.
This is achieved as follows: for researchers, by identifying new
types of technical debt; for organizers and participants, by
enriching the available technical debt detection tools; for
educators, by offering a straightforward and direct method to train
their students in identifying and combating technical debt; and for
the student participants, by providing the opportunity to evaluate
their proposals before submission.
The objective of this research is to identify the principal factors
that contribute to the accrual of technical debt in AI-based
systems. This is done through a scoping literature review, then, by
classifying all identified factors according to the type of debt they
represent. Based on this classification, a questionnaire will be
developed to serve as an assessment instrument for organizers and
participants of AI competitions to help them assess the extent of
technical debt present either on their platforms or within their
submissions, respectively.
2 RELATED WORK
As developers incorporated AI into applications, they encountered
unique challenges, highlighting the need to redefine software
engineering. This spurred researchers to investigate AI-specific
issues, adapt existing methods, and innovate within the field,
leading to the development of new areas such as SE4AI. Equally
significant proves to be the contribution of AI-based competition
platforms to AI research and education, as well as to the
development of soft skills such as collaboration, communication
and soft aspects such as ethics and human-centered design.
2.1 Technical Debt in AI-based Systems
Sculley et al. [1] introduced the concept of "Hidden Technical
Debt" in machine learning (ML) systems, highlighting the unique
challenges of managing such debts. Subsequent research by Liu et
al. [2] identified extensive technical debt in leading deep learning
frameworks, particularly within design, requirements, and
algorithms. A. Stewart [3] and Recupito et al. [4] further explored
ML-specific technical debts and introduced Artificial Intelligence
Technical Debt (AITD) to address gaps in managing code and
architectural debts.
Code smells are a primary factor contributing to technical debt.
Gesi et al. [5] in 2022 identified five new smells affecting the
maintainability of deep learning systems, while Zhang, Cruz, and
Deursen [6] uncovered 22 distinct smells across different pipeline
stages. Additionally, Foidl, Felderer, and Ramler [7] explored data
smells, providing detection methods.
Significant strides in understanding technical debt in AI systems
were made by Bogner et al. [8], who identified types such as data
and model debts and described 72 antipatterns with 46 solutions.
H. Washizaki et al. [9, 35] applied software engineering design
patterns to enhance ML system architecture and efficiency, and
Heiland, Hauser, and Bogner [10] categorized 70 design patterns
for various applications.
Nascimento et al. [11] and Serban et al. [12] reviewed software
engineering practices tailored for ML systems, emphasizing the
need for methodologies specific to ML. V. Lenarduzzi et al. [13]
and Martínez-Fernández et al. [14] highlighted the evolving
nature of software quality metrics and synthesized SE practices,
examining numerous studies to better integrate software
engineering in AI development.
2.2 AI-based Competition Platforms
AI competition platforms are key in advancing software
engineering methodologies and provide essential training in AIrelated soft skills. Togelius [15] discusses the organization of
successful AI game competitions, emphasizing their role in
spurring innovation and rapid development, albeit sometimes at
the expense of long-term sustainability. D. Kalles [16] explores
how integrating AI and software engineering in education can
mitigate document debt and develops soft skills using platforms like RLGame. The RoboCup, as analyzed by Genter, Laue, and
Stone [17], exemplifies how such competitions train robotics and
AI students, enhancing teamwork skills in AI systems without
pre-coordination.
Competitions like Project Malmo [18], built on Minecraft,
highlight how AI challenges can advance rigorous research and
develop skills in strategic planning and real-time collaboration.
Similarly, Giagtzoglou and Kalles [19] and Salta, Prada, and Melo
[20] demonstrate how gaming ecosystems like RLGame and
Geometry Friends contribute to AI education and research. Konen
[21] introduces the General Board Game (GBG) framework,
promoting its use in educating diverse AI agents across various
games. Pavao et al. [22] propose using CodaLab in competitive AI
settings to manage technical debt, thus bolstering the training of
AI professionals and ensuring the sustainability of AI systems in
dynamic environments.
3 RESEARCH METHODOLOGY & FINDINGS
3.1 Goal and research questions
The integration of artificial intelligence components into software
engineering systems has catalyzed the formation of specialized
research domains such as SE4AI and SE4ML [35]. These domains
dedicate their focus to applying the principles from one
specialized area to another, which in turn, expands the range of
sources and causes of technical debt associated with these
advancements. This expansion necessitates the formulation of
novel categories of technical debt that encapsulate these new
factors and causes, thereby enhancing their classification and
analysis. Motivated by this need, we opted for a scoping review as
our research methodology. This approach enables a thorough
examination of the varied facets by systematically mapping out
the current body of literature. The organization of our study
involved multiple stages, the specifics of which are detailed in the
Appendix A.
The objectives of our study were defined as follows:
1. To systematically identify, classify, and categorize the
factors contributing to technical debt in AI-based systems,
drawing upon extant scholarly works.
2. To elucidate each type of technical debt by providing a
succinct definition, a brief description of its impacts and an
illustrative example of its application
3. To ascertain the types of technical debt prevalent in current
AI-based competition platforms.
4. To develop a custom questionnaire for each identified type of
technical debt, aimed at quantifying its presence in AI-based
competitive environments.
5. To propose methodologies for the quantification of technical
debt and to explore the potential benefits of addressing it in
the context of an AI-based competition platform.
Based on our goal, we defined the following research questions
(RQs):
RQ1: What are the most significant types of technical debt
recorded in AI-based systems?
RQ2: How can we measure the technical debt of an AI – based
competition platform?
3.2 Findings
From the research and study of the articles we identified, we
found that the management of technical debt is associated with
several factors. Therefore, to answer RQ1, we categorized these
factors into 18 distinct types. For each type, we provided a
definition, a brief description of its implications, and a
hypothetical scenario tailored for AI competition platforms, to
facilitate study and interpretation. An initial classification of
studies by type of technical debt and year of publication identified
is presented in Table 1. Subsequently, we utilized the
categorization from RQ1 to develop the measurement approach
for technical debt, as required by RQ2. Thus, we defined the types
shown in Table 1.
Table 1. Types of Technical Debt in AI-based Systems
S/N Type Number of
Documents
Publication Span
Period
1 Algorithm 4 2020 - 2023
2 Architectural 10 2016 - 2023
3 Build 6 2012 - 2022
4 Code 7 2019 - 2022
5 Configuration 4 2015 - 2021
6 Data 9 2017 - 2022
7 Defect 5 2017 - 2021
8 Design 4 2014 - 2021
9 Documentation 4 2020 - 2022
10 Ethics 5 2018 - 2022
11 Infrastructure 3 2019 - 2021
12 Model 13 2015 - 2022
13 People 3 2017 - 2022
14 Process 2 2014 - 2021
15 Requirements 5 2019 - 2023
16 Self-Admitted (SATD) 6 2016 - 2023
17 Test 4 2017 - 2023
18 Versioning 6 2017 – 2021
Total 100
In this section, we present the nine most significant types of
technical debt in the context of AI-based competition platforms.
We identified eight out of the nineteen proposed categories as the
most significant, based on their prevalence in the literature [8, 14].
The integration of artificial intelligence components into software
has compelled the scientific community to examine new aspects
of technical debt. These aspects include Data, Model,
Configuration, and Ethics of AI-based systems, as well as
modifications in existing technical debt factors of traditional
software, such as Architecture, Testing, and Infrastructure [8].
Moreover, the examination of technical debt factors related to the
Algorithms used in Deep Learning systems has become essential 
[2]. Additionally, diverging from our primary criterion, we
deemed the examination of Accessibility Debt essential due to its
significant impact on participant engagement and the overall
success of AI-based competition platforms.
From the organizers' perspective, focusing on these types of
technical debt helps ensure that the technical environment of the
competition provides a straightforward and efficient method of
participation and is optimized for the development and
advancement of artificial intelligence. This optimization enhances
both the experience and the performance of the participants'
models. Additionally, these priorities help maintain a fair and
competitive atmosphere, which is vital for the success of an AIbased competition. For participants, these types reflect the direct
impact on their ability to compete seamlessly, promptly,
effectively and innovate within the given platform. This ensures
that their solutions are not only technically correct but also
ethically and practically robust.
The remaining types of technical debt identified, are presented in
the Appendix B.
3.2.1 Algorithm debt
Definition: Algorithm debt refers to technical debt arising from
the choice, implementation, and maintenance of algorithms within
AI systems [2], excluding issues directly related to the model's
structure or data handling. This debt encompasses challenges
associated with selecting appropriate algorithms, optimizing their
performance, and ensuring they remain suitable as the system
scales or as requirements evolves.
Problem: The problem of algorithm debt in AI-based systems
often stems from the use of algorithms that are either too
simplistic or overly complex for the task at hand, poorly
optimized, or inefficient in terms of computational resources.
Such choices may initially simplify development but can lead to
increased costs and reduced system performance in the long run.
For instance, an algorithm that is not scalable might handle initial
data volumes well but becomes a bottleneck as data grows,
requiring costly re-engineering efforts.
Example: In the context of AI-based competition platforms, an
example of algorithm debt could occur when an algorithm
designed for matchmaking in online games does not effectively
adapt to changes in player skills and behaviors over time. Initially,
the algorithm may work well, but as the variety of players
increases, its inability to adapt could result in poor matchmaking,
increased wait times, and player dissatisfaction. The platform may
then face significant technical debt as the original algorithm
requires substantial modification or replacement to meet the
evolved needs of its user base.
This example highlights how crucial it is to anticipate the longterm needs of the system when choosing algorithms, and to plan
for their evolution as part of the platform's ongoing development
strategy to avoid accruing algorithm debt. This example illustrates
how the need for rapid development in competitive AI platforms
can lead to significant algorithm debt, impacting the platform's
long-term capability to perform reliably and accurately.
Stakeholder: Participants must address any potential glitches or
incompatibilities in the frameworks or algorithms they use. This is
crucial to prevent issues that could impair the performance of their
AI solutions, such as slower processing times or errors during
execution.
3.2.2 Architectural Debt
Definition: Architectural debt refers to the complexities arising
from the intricate integration of architectural components with
their foundational data within AI-based systems [8].
Problem: This type of debt can precipitate intricate and
indeterminate dependencies between system components and their
corresponding datasets. It often results in architectures that are
challenging to evaluate due to their complex compositions.
Moreover, it can lead to the emergence of undeclared entities that
utilize AI models, further complicating the governance and
maintenance of these systems.
Example: At a global AI-based game development competition,
architectural debt in gaming platforms posed significant
challenges. The systems were designed to adapt dynamically to
user behaviors using complex architectures that integrated
multiple data sources and AI components. This complexity led to
unpredictable game behaviors, where player input changes
unexpectedly altered AI responses due to hidden architectural
dependencies. Additionally, undocumented consumption of extra
data by some components caused inconsistencies and performance
issues, complicating the assessment and modification of games by
developers. This severely impacted the competition experience
and the performance of AI models, highlighting how architectural
debt can undermine functionality and innovation in AI-driven
competitions.
Stakeholder: Organizers. Ensuring a well – structured system
architecture allows organizers to maintain and scale the platform
efficiently. This involves good practices in separating concerns,
managing dependencies, and avoiding tightly coupled
components, which collectively ensure that the system remains
flexible and manageable as it evolves.
3.2.3 Configuration Debt
Definition: Configuration debt encapsulates the deficiencies
prevalent within the configuration frameworks of AI-based
systems. This term specifically refers to the complexities and
shortcomings of configuration processes, including the use of
convoluted, insufficiently documented, unversioned, or untested
configuration files [1, 3, 8].
Problem: Configuration debt introduces significant vulnerabilities
to machine learning systems by fostering errors in configuration
that can deplete valuable time and computational resources and
cause delays in production. This debt hampers the ability to
accurately modify and understand configurations, complicating
the evaluation of the effects of changes and the comparison of
configurations across different iterations. Moreover, poor
management of configuration settings intensifies these issues by
obstructing the precise specification, tracking, and reproducibility
of configuration alterations. This results in difficulties in
replicating experiments and ensuring system reliability. Effective
management of configuration settings is crucial to alleviate these 
problems and enhance the efficiency, reproducibility,
maintainability, and transparency of AI-based systems.
Example: During a high-profile AI-based game competition, one
team struggled with significant configuration debt. Their gaming
AI had multiple configuration files that were complex and poorly
documented, making it difficult for new team members to
understand and modify the settings efficiently. As the competition
progressed, the need to adapt to opponents' strategies became
critical. However, due to unversioned and untested configurations,
changes made under pressure led to errors that were not detected
until too late. This resulted in the AI performing unpredictably,
costing the team crucial matches and demonstrating the impact of
configuration debt on competitiveness and system reliability.
Effective configuration management allows rapid iteration and
model improvement, which are essential in a competitive AI
environment. Organizers need to ensure that configurations can be
easily managed and modified to accommodate diverse models and
strategies that participants might employ.
Stakeholder: Organizers: Effective configuration management
allows rapid iteration and model improvement, which are essential
in a competitive AI environment. Organizers need to ensure that
configurations can be easily managed and modified to
accommodate diverse models and strategies that participants
might employ.
3.2.4 Data Debt
Definition: Data debt pertains to the shortcomings in the
collection, management, and application of data within AI-based
systems [8], characterized by issues such as poor data quality,
unregulated data dependencies, and inadequate data relevance [7].
Problem: These deficiencies can compromise the efficiency and
precision of AI models, posing challenges to the system's
reliability and future adaptability. Data debt introduces risks that
may impede the ongoing development and operational
effectiveness of AI systems, potentially leading to erroneous
outputs and strategic misalignments in long-term system
evolution.
Example: In a high-profile AI-based gaming competition, a team
faced setbacks from data debt. Their AI model, designed to
dynamically adapt strategies, used outdated and poorly curated
datasets, compromising data relevance and quality. This affected
the model's decision-making, often resulting in ineffective
strategies and failure to anticipate opponent moves. Unmanaged
data dependencies, only discovered during the competition,
highlighted the need for real-time data processing and
underscored the importance of rigorous data management to
maintain AI effectiveness and system scalability in dynamic
settings.
Data quality is paramount in AI competitions. Organizers must
ensure that the data used is accurate, complete, and relevant.
Managing data debt effectively prevents issues such as overfitting
or poor generalization, which can severely affect the outcomes of
the competition.
Stakeholder: Organizers: Data quality is paramount in AI
competitions. Organizers must ensure that the data used is
accurate, complete, and relevant. Managing data debt effectively
prevents issues such as overfitting or poor generalization, which
can severely affect the outcomes of the competition.
Participants: Quality and integrity of data are paramount in
training effective and reliable AI models. Participants must ensure
their data is accurate, complete, relevant, and trustworthy to avoid
issues like overfitting, underfitting, or biased results, which could
severely affect their model's performance.
3.2.5 Model Debt
Definition: Model debt refers to the accumulation of suboptimal
practices within the lifecycle of artificial intelligence models,
encompassing the design, training, and management phases. This
encompasses issues related to inadequate feature selection,
improper tuning of hyperparameters, and ineffective strategies for
model deployment [1, 2, 8].
Problem: Model debt manifests through several challenges, such
as poorly chosen features, neglected adjustments of
hyperparameters, and deficient deployment architectures. Such
deficits may complicate the maintenance of models and diminish
their predictive accuracy, thereby undermining the system's
overall effectiveness and reliability.
Example: In an AI-based game competition, one team faced
significant model debt issues. Their AI model, initially promising,
suffered from too narrow feature selection focused on short-term
gains and lacked strategic depth. Additionally, the
hyperparameters were not tuned to the game's dynamic nature,
and the deployment strategy failed to adapt to evolving scenarios.
These shortcomings led to the model underperforming in critical
matches, unable to accurately predict or counter the diverse
strategies of competitors.
This is critical because it directly affects the quality and
performance of the AI models used in the competition. Ensuring
that models are well-validated, free from bias, and perform
robustly across different scenarios is key to maintaining the
integrity and fairness of the competition.
Stakeholder: Organizers: This is critical because it directly affects
the quality and performance of the AI models used in the
competition. Ensuring that models are well-validated, free from
bias, and perform robustly across different scenarios is key to
maintaining the integrity and fairness of the competition.
Participants: Participants need to ensure that their models are
robust and validated correctly before serving. This includes
avoiding feedback loops and ensuring that the model can be
debugged and tested comprehensively. This type of debt is vital to
prevent deploying models that might perform well in training but
fail in practical scenarios.
3.2.6 Ethics Debt
Definition: Ethics debt refers to the shortcomings concerning the
ethical dimensions of AI-based systems, including issues such as
algorithmic fairness, prevalent prediction biases, and a lack of
transparency and accountability [8].
Problem: The realm of AI ethics encounters multiple challenges
that stem from a diminished influence over decision-making
processes, insufficient enforcement mechanisms, and an overreliance on ethical guidelines rather than binding legal standards. 
This often results in the neglect of broader social contexts and
relationships, contributing to a lack of diversity within the AI
community and the exclusion of vital ethical considerations. The
ramifications of ethics debt are manifold, encompassing
unintended harmful effects and the malicious use of AI
technologies. Such consequences include job displacement,
unsupervised experimental applications, and significant data
breaches. Moreover, there exists a substantial risk of developing
biased algorithms and unsafe products, precipitously deploying
immature applications, and the potential exploitation of AI
technologies by malicious entities, such as criminal hackers.
Example: In an AI-based game competition, a team deployed an
AI model designed to predict and counter opponents’ moves.
Unfortunately, the model exhibited significant ethics debt due to
overlooked issues like algorithmic fairness and transparency. The
model, trained predominantly on data from games played by a
non-diverse group, failed to fairly assess strategies used by a
wider range of competitors. This bias led to inaccurate predictions
and strategic blunders, compromising the team's performance. The
incident highlighted the consequences of neglecting ethical
considerations in AI development, demonstrating how ethics debt
can undermine fairness and effectiveness in competitive
environments.
Stakeholder: Participant: Understanding and adhering to ethical
guidelines set by the competition is essential. This includes
knowing the rules, how to raise questions, and how to handle
potentially conflicting interpretations of the competition's terms.
Ethical considerations are crucial to ensure that the competition is
fair and that all participants operate on a level playing field.
3.2.7 Infrastructure Debt
Definition: Infrastructure debt encapsulates the inadequacies
inherent in the implementation and operational management of
artificial intelligence (AI) pipelines and models [1, 8, 11, 30].
Problem: This type of debt introduces significant operational and
reproducibility challenges within AI systems. It frequently
manifests as overly complex infrastructures that integrate multiple
AI pipelines, leading to suboptimal resource distribution for the
training and testing of AI models. Additionally, it exacerbates the
difficulty in effectively monitoring and debugging AI systems,
thereby compromising their reliability and performance.
Example: During a high-profile AI-based game competition,
infrastructure debt became evident as teams struggled with the
systems set up for training and testing their game-playing models.
The competition's infrastructure was initially designed to handle
multiple concurrent AI pipelines efficiently. However, as the
competition progressed, it became clear that there were significant
deficiencies in resource allocation and system integration. Some
teams experienced delays in model training due to limited GPU
resources, while others faced challenges in consistently
reproducing game strategies due to varying system performances.
Additionally, the lack of robust monitoring and debugging tools
meant that identifying and resolving these issues was timeconsuming, leading to uneven playing fields and questioning the
fairness and integrity of the competition. This scenario highlights
how infrastructure debt can severely impact the operational
success of AI-driven initiatives in competitive environments.
Stakeholder: Organizer: Reliable and scalable infrastructure is
crucial for handling the computational demands of AI models,
especially when multiple participants are involved. Organizers
must manage infrastructure debt by ensuring the system is robust,
scalable, and capable of supporting the high concurrency levels
typically seen in competitions.
3.2.8 Test Debt
Definition: Test debt encompasses the shortcomings in testing
practices within AI systems, particularly highlighting the
insufficient testing of AI models and pipelines, as well as a
deficiency in advanced testing methodologies necessary for
evaluating data quality and distribution [8, 30] .
Problem: The probabilistic characteristics of certain AI
algorithms add a layer of complexity to the testing processes.
These complexities make it especially challenging to ensure
comprehensive testing coverage and reliability, thereby increasing
the risk of undetected issues in AI system behavior under varied
operational conditions. This type of debt may lead to less
predictable and potentially unreliable AI system performance.
Example: In an AI-based game competition, various AI models
were pitted against each other in a strategy game. However, due to
existing test debt, the competition faced challenges. The AIs had
not been adequately tested for their ability to handle the stochastic
elements of the game, such as random events and unpredictable
opponent strategies. This lack of rigorous testing resulted in some
AI models performing inconsistently, displaying erratic behavior,
or failing to adapt to new scenarios presented during the
competition. The event highlighted critical gaps in testing
practices, emphasizing the need for more robust testing
frameworks to ensure AI reliability and effectiveness in dynamic
environments.
Stakeholder: Participant: Ensuring that their model and its
components, such as hyperparameters and training environments,
are thoroughly tested is crucial. This includes validating the
reproducibility of results and the stability of the model in the
competition’s game environment, which is essential for
demonstrating effectiveness and reliability.
In the context of AI/ML competition platforms, a critical factor
for their successful operation is the ease and speed with which
potential participants can utilize the platform's components to
engage with the assigned tasks. Consequently, we have defined a
new type of technical debt, specific to AI-Based Competition
Platforms, as Accessibility Debt. This definition addresses the
challenges associated with the ease and speed of immediate use of
the platform technologies, which, if not adequately addressed,
discourage participants, thereby devaluing the competitions.
3.2.9 Accessibility Debt
Definition: Accessibility Debt refers to the barriers that
participants encounter due to the lack of immediate usability of
platform technologies.
Problem: The primary issue with Accessibility Debt is that it can
dissuade potential participants from engaging with AI/ML
competition platforms. This is due to the challenges they face in
utilizing the platform's components quickly and efficiently. If
these barriers are not addressed, the competitive value and
attractiveness of such platforms diminish, leading to decreased
participation and devalued competitions.
Example: Consider an AI-based competition platform where
participants must navigate a complex setup process before they
can begin working on their assigned tasks. If the process involves
multiple steps, unclear instructions, or requires significant
troubleshooting, participants may become frustrated and
disengaged. This scenario exemplifies Accessibility Debt, as the
immediate usability of the platform is compromised, hindering
participant involvement and satisfaction.
Stakeholder: Organizer: They are responsible for ensuring that the
platform is accessible and user-friendly, providing necessary tools
and resources to participants efficiently. By addressing
Accessibility Debt, organizers can enhance participant
engagement and the overall success of the competitions.
4 PROPOSED METHOD FOR MEASURING
TECHNICAL DEBT
Technical debt is a multifaceted concept that affects all stages of
the software development lifecycle. The unique challenge
presented by AI-based systems, to be "just like" traditional
software until they’re not [13], exacerbates the difficulty in
identifying and addressing technical debt. This issue is especially
pronounced on platforms for AI/ML competitions, where
applications might only be deployed once. It is crucial that
participants are informed about the importance of technical debt
and are able to identify its manifestations. Such awareness is
fundamental for their training in best practices and equips them
sufficiently to excel as proficient practitioners in their future
professional endeavors.
In an effort to aid both participants and organizers in recognizing
and quantifying technical debt, we devised a questionnaire
detailed in the Appendix C, which categorizes technical debt
according to the types identified in RQ1, as well as the new
proposed type and answers to RQ2. To our knowledge, there are
no comparable initiatives. The endeavor documented in [30]
focuses solely on ML applications, with an emphasis primarily on
testing and monitoring. Although we incorporated some of these
questions, our questionnaire has been expanded to encompass all
debt types that surfaced in RQ1 and [8].
The questionnaire employs a rating scale ranging from 1
(minimal) to 5 (maximum), though these ratings are not disclosed
to users, along with the response options 'Not Applicable' and
'Don't Know/Don't Answer':
1. This allows participants to quantitatively assess the level of
technical debt in their proposed implementations while
simultaneously developing soft skills [16, 31] and
familiarizing themselves with the nuanced aspects [19] -
which are increasingly critical - of AI applications.
2. This enables organizers to evaluate their platforms in order to
prevent the accrual of long-term technical debt resulting from
suboptimal implementation decisions (poor SE4AI choices),
thereby enhancing the viability and maintainability of their
platforms.
In the questionnaire designed to quantify technical debt, each
response plays a specific role in the scoring system that ultimately
reflects the level of technical debt associated with a given
proposal or platform. A "YES" response, which signifies
adherence to practices known to mitigate technical debt, results in
a negative score, thereby indicating a reduction in technical debt.
Conversely, a "NO" response suggests a deviation from these
practices, and is consequently assigned a positive score, indicating
an increase in technical debt. Responses marked as "Not
Applicable" receive a score of 0, reflecting their neutrality in
terms of impacting the technical debt calculation. Similarly,
responses of "I Don’t know/I Don't answer" are treated the same
as "NO" responses, as they both imply the presence or potential
accumulation of technical debt. The rationale for this scoring
method is founded on the assumption that affirmative answers
demonstrate compliance with best practices that lower technical
debt, whereas negative or uncertain responses indicate areas
where technical debt could either be present or likely to
accumulate. The cumulative score derived from all responses thus
provides a quantitative measure of the total technical debt
associated with the entity being evaluated.
In our approach to quantifying technical debt, we delineate the
following components for each type of debt assessed:
1. Question: This represents the specific query posed to
stakeholders, aimed at gauging their practices related to
technical debt.
2. Stakeholder: This identifies the individual or group
responsible for responding to the question, thereby ensuring
that the query is directed to those with the most relevant
experience or decision-making authority.
3. Score: Assigned on a scale from 0 to 5, this quantifies the
response, with different scores reflecting varying degrees of
adherence to best practices in technical debt management.
4. Justification: This provides the rationale behind the
necessity of posing the question, linking it to its potential
impact on technical debt.
5. Example: A typical scenario or case is presented to clarify
the question and assist the stakeholder in understanding and
responding appropriately.
An aggregated presentation of the questions categorized by type
of technical debt is included in Table 2 of our document. Due to
the extensive range of questions developed for this assessment, we
highlight five representative questions in the main text. The
complete set of questions, however, is detailed in the Appendix C
for interested readers seeking comprehensive insights into the
questionnaire framework and its applications.
Table 2. Number of Questions by Technical Debt Type
Type Number of Questions
Accessibility 3
Algorithm 1
Architectural – Design 5
Build 2
Code 1
Configuration 3
Data 6
Defect 5
Documentation 5
Ethics 2
Infrastructure 4
Model 3
People – Social 2
Process 3
Requirements 5
Self-Admitted (SATD) 10
Test 7
Versioning 3
Sum 68
5 DISCUSSION
By exploring the multidimensional nature of technical debt in AIbased competition platforms, we have highlighted a multitude of
debt types that are important to both organizers and participants.
These debts highlight the complexity of managing AI systems and
span the following aspects: algorithms, architecture,
configuration, data, model, accessibility, ethics, infrastructure, and
testing. Notably, algorithm and architecture debts profoundly
affect system performance and scalability. For example, algorithm
debt, resulting from the selection and maintenance of suboptimal
algorithm libraries, can severely hinder the adaptability of AI
systems. Similarly, architectural debt, with its complex
dependencies and integration challenges, hinders system
evaluation and flexibility, thereby degrading user experience and
system robustness. Ethical debt can also undermine competitive
success when competitions prioritize technical robustness
exclusively, disregarding other crucial factors. For example,
competitions which fail to provide reliable test and training data
eventually, compromise fairness and trust. Additionally,
insufficiently training for participants to adhere to legal standards
[36], which complement ethical guidelines, when the domain so
requires, and inadequate instruction on implementation rules or
conflict resolution, can further jeopardize clarity and fairness.
For organizers, understanding and prioritizing these types of
technical debt is crucial in maintaining a fair and competitive
atmosphere essential for the success of AI-based competitions.
This involves a meticulous focus on not just the immediate
functionality but also the long-term sustainability of the
competition platform. Organizers must adopt proactive strategies
to mitigate these debts, such as refining system architecture,
ensuring robust configuration management, and fostering ethical
practices to support diverse AI models and strategies efficiently.
Participants, on the other hand, face direct consequences of these
technical debts, influencing their capacity to innovate and
compete effectively. Addressing algorithm, configuration and
ethical debts, for instance, is crucial for participants to ensure their
AI solutions are not only technically adept but also fair,
transparent and adaptable to the evolving competitive landscape.
5.1 Accessibility Debt: A New Liability
Our study introduces a novel category – Accessibility Debt,
specific to AI-Based Competition Platforms – which highlights
the barriers participants encounter due to the lack of immediate
usability of platform technologies. This form of debt is
particularly detrimental as it can dissuade potential participants,
thus diminishing the competitive value and attractiveness of AIbased platforms. Organizers need to address this by simplifying
access to necessary tools and resources, ensuring that participants
can engage with the platform effectively and without undue
delays.
5.2 A Questionnaire as a Quantifiable
Assessment Tool
The proposed questionnaire, derived from an initial pool of about
160 questions from our research, comprehensively covers the
types of technical debt predominant in AI-based systems, as
outlined in RQ1. These questions, grouped by type of technical
debt, assess stakeholder actions from the highest (abstract) level,
such as AI system architecture and design, to the lowest (detailed)
level, like code writing and system configuration, measuring their
impact on reducing technical debt. Given the potential challenges
posed by the large number of questions, we prioritized them by
selecting those with a significance weight of 3 and above, while
keeping the score hidden. This approach reduces users' cognitive
load with a simpler, more substantial questionnaire, avoiding
confusion while focusing on the most critical checks.
To enhance the reader's understanding of the questionnaire's
application, we will provide an example for each stakeholder,
using two of the nine technical debt categories listed in the article.
Table 3. Organizer Accessibility Debt Example
Question Score Answer Calculated
Score
Have you conducted
usability testing to
identify and address
potential barriers in the
platform setup process?
5 YES -5
Have you integrated
adaptive user interfaces
that personalize the setup
experience based on
participants' skill levels
4 NO 4
and preferences?
Have you implemented
feedback mechanisms for
participants to report
accessibility issues and
suggest improvements?
3 I Don't
Know/I
Don't
Answer
3
Overall Rating 2
Table 4. Participant Model Debt Example
Question Score Answer Calculated
Score
Are you detecting
direct feedback loops
or hidden feedback
loops?
4 NO 4
Is model quality
validated before
serving?
5 YES -5
Does the model allow
debugging by
observing the stepby-step computation
of training or
inference on a single
example?
3 I Don't
Know/I
Don't
Answer
3
Overall Rating 2
According to the stakeholder responses depicted in the examples
from Tables 3 and 4, the platform assessment for the specified
types reveals a quantifiable technical debt of 2 units each. Each
interested party will independently replicate the example process
for each question (Organizers: 41, Participants: 41) in Appendix C
relevant to their context. The cumulative results from both
Organizers and Participants will indicate the degree (percentage)
of technical debt identified on the platform. A total final sum less
than or equal to 0 signifies that the platform adheres to SE4AI
best practices, indicating zero debt. Conversely, a positive sum
indicates a high level of technical debt on the platform.
6 THREATS TO VALIDITY
In all phases of our research we tried to mitigate potential threats
to validity that are very common in this type of research.
However, our research is subject to limitations.
Internal validity. To reduce potential bias due to the subjective
interpretation of researchers, we defined during our research
(RQ1), a comprehensive set of keywords related to technical debt
in AI-based systems and competing platforms. We selected five
datasources for our search to broaden the results by sticking
mainly to peer-reviewed papers. We also performed snowballing
to ensure inclusion of papers that may have been missed in the
original search.
In the first selection phase we studied the title, abstract and
keywords of the results obtained. Each article was read by the first
author in its entirety in detail and comments were made regarding
content, key points and findings relevant to our research.
The second author reviewed these comments, assessed the quality
of the findings while the authors discussed any papers in doubt
and made a joint decision thus ensuring that the papers were
suitable for inclusion in the final results. These studies were
selected based on the criteria they set, while a similar procedure
was followed for data extraction and analysis.
Despite faithful adherence to the protocol, due to subjectivity
there is a possibility that other researchers who wish to use our
strategy may come up with slightly different results.
External validity. The area of technical debt in AI-based systems
is an area that is constantly evolving and changing dynamically
either by modifying existing ones or by including new categories.
Several times, issues that have already been highlighted are reexamined under a different perspective or different framework of
application, highlighting new dimensions.
As a consequence, nuanced findings may emerge on the
definition, scope, and impact of technical debt in AI-based
systems as they mature and are increasingly adopted in software
engineering. Especially in an unexplored area like that of AIbased competition platforms, we think that's to be expected.
7 CONCLUSION & FUTURE RESEARCH
In this study, we collected, classified, and analyzed the dominant
types of technical debt for AI-based systems. Utilizing these
classifications, we developed a questionnaire as a self-assessment
tool for measuring technical debt on AI-based competition
platforms. Our aim is to bridge the observed measurement gap of
technical debt on such platforms.
We have discovered that managing technical debt in AI-driven
platforms necessitates a comprehensive strategy tailored to every
unique phase of the platform's lifecycle. The intricacy of these
systems arises not only from the incorporation of AI elements but
also from the enhanced interplay with human factors, exerting a
more significant influence than observed in conventional software
engineering contexts.
We have identified a new type of technical debt, accessibility
debt, which highlights the steepness of the learning curve for
some competition platforms, thus diminishing their competitive
value and attractiveness. Our findings resonate well with and
extend the current literature on technical debt in software
engineering, by contextualizing these debts within the unique
demands of AI competition platforms.
As the next step in our research, we plan to test the effectiveness
of the questionnaire in practice by having it evaluated: a) by
organizers (professors) who teach AI software engineering and
use competition platforms to educate their students, b) by
participants (undergraduate students of computer science
departments), who are taught AI software engineering and use
competition platforms to develop their proposals. We expect to
empirically determine: a) the percentage of technical debt that can 
be detected on a competition platform (by organizers and
participants), b) the extent to which it can train students to identify
technical debt, c) the degree to which it contributes to reducing
the long-term debt of the platform itself.
Additionally, as the creators of the questionnaire, we will have the
opportunity to a) assess whether the nine most significant types of
technical debt identified in this article are equally important
across various competition platforms and among diverse
stakeholders who will use the questionnaire, b) observe variations
in the use and outcomes of the questionnaire under two
conditions: i) when the characteristics of the stakeholders are
known in advance but control variables have not been defined, ii)
when the characteristics of the stakeholders are not known in
advance, but appropriate control variables, such as education,
years of coding experience, frequency of participation in
competition platforms, dedicated training time, have been defined.
Furthermore, we will endeavor to determine to what extent it is
possible to assess similar systems in commercial environments,
including both proprietary and closed-source platforms such as
Azure and Kaggle.


