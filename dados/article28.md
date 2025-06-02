Title: Fairness and Bias in Algorithmic Hiring:
A Multidisciplinary Survey

Employers are adopting algorithmic hiring technology throughout the recruitment pipeline. Algorithmic
fairness is especially applicable in this domain due to its high stakes and structural inequalities. Unfortunately, most work in this space provides partial treatment, often constrained by two competing narratives,
optimistically focused on replacing biased recruiter decisions or pessimistically pointing to the automation
of discrimination. Whether, and more importantly what types of, algorithmic hiring can be less biased and
more beneficial to society than low-tech alternatives currently remains unanswered, to the detriment of
trustworthiness. This multidisciplinary survey caters to practitioners and researchers with a balanced and integrated coverage of systems, biases, measures, mitigation strategies, datasets, and legal aspects of algorithmic
hiring and fairness. Our work supports a contextualized understanding and governance of this technology by
highlighting current opportunities and limitations, providing recommendations for future work to ensure
shared benefits for all stakeholders.
CCS Concepts: • General and reference → Surveys and overviews; • Information systems → Data
management systems; • Social and professional topics → Computing / technology policy.
Additional Key Words and Phrases: Algorithmic hiring, Online recruitment, Algorithmic fairness, Bias, Antidiscrimination
1 INTRODUCTION
New algorithms for Human Resources (HR) are developed and deployed every year. By one count,
there are over 250 Artificial Intelligence (AI) tools for HR on the market [99], with entire manuals for
HR professionals available on the topic [80]. The average job posting yields more than 100 candidates
[101, 206]. These mutually reinforcing factors were accelerated by the COVID-19 pandemic and
recent advances in AI [170, 207]. As a result, prospective job applicants and their chances of success
are increasingly influenced by algorithmic hiring technology, including automated job descriptions,
resume parsers, and video interviews.
Workplaces and labor markets are fraught with biases, imbalances, and patterns of discrimination
against vulnerable groups, including women, ethnic minorities, and people with disabilities [15,
23, 215]. While algorithmic hiring represents an opportunity to mitigate these biases, it also runs
the risk of reinforcing and amplifying them, causing harm and hindering trustworthiness [168].
The debate on this topic is often polarized between techno-enthusiasm [139, 177] and pessimism
[9, 132] due to partial perspectives on a field that is large and complex. In this paper, we offer a
multidisciplinary survey of fairness and bias in algorithmic hiring centered on computer science
(focused on systems, algorithms, metrics, and datasets) and informed by related disciplines. We
critically analyze available resources and methods, highlight common challenges, and identify
opportunities to advance the field.
Related work. Bogen and Rieke [30] presented a technical report that described algorithmic hiring
tools available in 2018, together with selected sources of bias, and provided a US-centric review of
relevant laws and policies. Köchling and Wehner [149] conducted a review of algorithms in HR
from a business research perspective, focused on non-empirical articles. Their qualitative discussion
raises awareness on discrimination in HR algorithms without delving into measures and mitigation
strategies. The prior work most closely aligned to ours is Rieskamp et al. [217], surveying nine
articles on bias mitigation for algorithmic hiring. Our survey expands on this work by presenting
more bias mitigation techniques, covering fairness measures, describing available datasets, and
by situating them in the broader social and legal context characterizing algorithmic hiring. In
concurrent work, Kumar et al. [154], survey the literature on fair recommender systems in the
recruitment domain. While similar in spirit, their work focuses on ranking; our work presents
a broader view of algorithmic hiring across different tasks and hiring stages, covering many
technologies and bias conducive factors throughout the algorithmic hiring pipeline.
Contributions and audience. This work provides a contextualized treatment of fairness and bias
in algorithmic hiring. It was carried out by a team with mixed backgrounds in computer science,
law, and philosophy, and with input from practitioners developing algorithmic hiring products.
Our contributions, catering especially to practitioners and researchers, can roughly be divided
as follows. Practitioners such as data scientists, engineers, and product managers, will find (1) a
detailed list and description of domain-specific factors that lead to biases in their systems (Sec. 3),
(2) methods to mitigate these biases (Sec. 5), (3) guidance on their applicability in practice (Sec.
7), and (4) pointers to key legal references in the EU and the US (Sec. 8). Researchers will benefit
from (4) an up-to-date description of hiring technology (Sec. 2), (5) a unified treatment of fair
hiring measures (Sec. 4), and (6) a collection of datasets in this space (Sec. 6). Overall, an integrated
coverage of these topics provides (7) a gentle primer for readers who are not experts in the field
and (8) highlights important gaps and promising directions for future work in computer science
at the intersection with law and policy (Sec. 10). Considering a broader audience, Sections 2, 3,
8, 10, and 11 cover a shared background which should be relevant for all readers, including HR
professionals and legal scholars.
Structure. The remainder of this work is organized as follows. Section 2 introduces the main
stages and systems in the algorithmic hiring pipeline. Section 3 focuses on bias, summarizing the
most important factors in the labor market, the recruitment sector, and the tech industry that can
lead to unfair recruitment systems. Sections 4–6 result from a systematic review of the literature
with methods described in Appendix A. Sections 4 and 5 describe the main fairness measures
and mitigation approaches, while Section 6 presents the datasets used in the algorithmic hiring
literature. Section 7 discusses practical aspects of anti-discrimination in algorithmic hiring guiding
the choice of fairness measures and mitigation strategies. Sections 8 and 9 widen the perspective
beyond computer science by outlining the main legal frameworks and situating algorithmic hiring in its broader socio-technical context. Section 10 summarizes opportunities, limitations, and
recommendations for future work; Section 11 provides concluding remarks.
2 THE ALGORITHMIC HIRING PIPELINE
Algorithmic hiring comprises algorithms, tools, and systems to automate or assist HR decisions
on candidate recruitment and evaluation. Elaborating on previous work from civil society [30],
regulatory bodies [84], and academia [209], we distinguish four stages in the algorithmic hiring
pipeline, reported in Figure 1.
Sourcing
The first stage of the hiring pipeline provides employers with a large pool of candidates for a
given position. Historically, this is the hiring stage where algorithms are most prominent and
well-researched. The main technological solutions and systems are summarized below.
• Job advertisement consists of tools to describe a vacancy and make it visible. Job descriptions
[128], possibly written by language models [207], are optimized and shared through suitable
channels, including employer websites [43], dedicated platforms [198], and ad delivery
services [4, 158].
• Search, ranking, and recommendation algorithms favor matches between jobs and job
seekers by ranking candidates for openings [103] and vice versa: recommending openings
to job seekers [185], based on a combination of machine learning, boolean matching, and
sorting (e.g. skills, location, industry), supported by information extraction systems [47].
Fairness is a critical and well-studied property for these systems [154, 265].
• Social networks, especially those embedded in job platforms, play an important role in the
visibility of candidates [239] and their awareness of opportunities [96], favoring professional
connections [39], contributing to the dissemination of information, and facilitating referral
[284].
It is worth noting that stage categorization is elastic and usage-dependent. For example, algorithms that extract information from CVs to score employees against job descriptions are central to
the sourcing stage, but may also be used for screening [58].
Screening
After sourcing, employers must narrow down large pools of candidates into manageable subsets
that can be more thoroughly evaluated by HR specialists and other employees.
• Gameplay is used for psychometric assessment and soft skills measurement. Companies
develop proprietary suites of games and make them available to candidates, e.g. through a
mobile app. Models analyze their gameplay to explicitly estimate competency scores [189] or
implicitly look for similarities with desirable candidates such as current employees [271].
• Asynchronous Video Interviews (AVI) are recordings of candidates’ answers to a specific
set of questions in front of a camera. AVI models rely on different data modalities, including
visual (e.g. facial expressions), verbal (e.g. length of sentences) and paraverbal features (e.g.
tone) to infer a variety of traits related to personality and hireability [33, 120].
• Questionnaires in hiring cover a wide range of purposes, such as personality assessment
[129], job performance inference [38, 95] or explicitly asking information about job requirements to filter candidates (e.g. Driver’s license ownership) or prioritize them (e.g. years of
experience).
• Chatbots can mediate interactions between employers and employees by asking basic screening questions for job seekers and scheduling interviews [30, 44]. Advancements in large
language models [190] are likely to increase the influence of this technology on hiring processes, broadening its reach to other stages of recruitment, including sourcing and evaluation
[170, 224].
Selection
After screening, candidates are interviewed by HR specialists or other employees. These interviews
can include technical and cultural questions influenced by previous stages, e.g. by questionnaire
answers. Several tools are available at this stage to help employers select the most desirable job
seekers and extend them a suitable offer.
• Compensation and benefit optimization allows employers to target their offers to each
candidate, thanks to tools that estimate the likelihood of acceptance based on salary, bonus,
stock options, and other benefits [30, 176].
• Background checks, primarily focused on criminal records [59, 66, 157], are used by employers to obtain additional information on candidates before hiring them. Background checks
can also target social media [127].
• Team placement concerns the assignment of a selected candidate to a specific role within a
team or project [107, 202].
Evaluation
The hired employees are managed and evaluated on their career progression. While, strictly
speaking, these are post-hiring processes, it is fundamental to consider them due to their feedback
loops on algorithmic recruitment.
• Performance and career management tools facilitate employee development and monitoring. Technology in this area supports training assignment [36], work allocation [253], career
development [188], along with monitoring and estimation through increasingly available
tracking technology [64, 140, 232, 236].
• Engagement analytics measures employee satisfaction, commitment, and retention probability, often leveraging dedicated questionnaires and surveys [149, 277].
• Career progression deals with promotion and dismissal of employees. Succession plans and
promotions can be partially automated [169, 188]. Turnover prediction is an active area of
research, typically presented as part of analytics to favor retention [204]. It is worth noting
that turnover data, frequently used to improve hiring systems [38], can also be repurposed
towards employee termination. Indeed 98% of 300 HR leaders from US companies interviewed
in a 2023 survey, report that software and algorithms will assist them with layoff decisions
throughout the year [259].
The progression of candidates through the stages of the hiring pipeline is accompanied by a
feedback loop in which the decisions at each stage generate data that influence the remaining stages
in subsequent interactions. Evaluation, for example, can lead to job termination impacting tenure,
which, in turn, represents a key desideratum and prediction target for sourcing and screening
algorithms. These data are influenced by a diverse and complex set of factors, many of which can
lead to undesirable discrimination, as described in the next section.
3 BIAS CONDUCIVE FACTORS
Hiring data and algorithms can display undesirable groupwise patterns caused by Bias Conducive
Factors (BCFs) affecting the employment domain. These patterns put some job seekers at a systematic disadvantage based on sensitive attributes such as age, disability, gender, religion or belief,
racial or ethnic origin, or sexual orientation. Overall, disparities may exist in data sample composition and feature values across sensitive groups that reflect and amplify problematic structural
differences in society. First, hiring datasets display measurement errors whose severity varies with
protected groups, most critically in target variables related to employability, reflecting current
biases in human ratings. Moreover, biased decisions at early stages result in downstream samples
misrepresenting certain groups. Finally, there are some higher-order effects caused by technological
blindspots and biases in external tools integrated into the hiring pipeline. Some of these biases are
reported in Figure 1; at their root there are two overarching BCFs that are worth highlighting from
the outset.
Stereotypes are widely held beliefs about groups of individuals with a common trait, including
their propensity and ability to perform a given job [118]. Stereotypes are sustained by culture,
socialization, and experience [50, 50]. They are often acquired at an early age [134] and can be
activated unconsciously [181]. Even when outspokenly rejected, stereotypes affect the lives of
individuals both descriptively and prescriptively based on coarse categories [76]. In turn, this ends
up shaping expectations about the qualities, priorities, and needs that people have about themselves
and others, including, and perhaps especially, about work [29, 50, 118, 248]. For example, agency
(orientation towards leadership and goal attainment) is stereotypically associated with men, while
communion (warmth and propensity for care) is frequently associated with women [72, 118], with
far-reaching effects of gender roles and expectations in employment [118, 215].
Sensitive attribute proxies. Stereotype activation and entrenchment is not always direct; stereotypes about a group can be activated by proxies [211]. This is especially true for algorithms trained
to make inferences from inputs that are strongly correlated with sensitive attributes. For instance,
video interviews and resumes contain a wealth of information on gender, race, and other sensitive
attributes [63, 69, 189, 218, 222], which can lead algorithms to learn stereotypical associations
between sensitive and target variables encoded in the data. More specifically, voice timbre and
physical appearance in videos may be used as proxies for gender, while names and spoken languages
in CVs may correlate heavily with certain migration backgrounds. Sensitive attribute proxies allow
models to learn and reflect the diverse BCFs described in the following section.
3.1 Institutional biases
The first family of BCFs we introduce are institutional biases. These are practices, habits, and norms
shared at institutions, such as companies and societies, which reflect negatively on the probability
of positive algorithmic hiring outcomes for disadvantaged groups.
Direct discrimination takes place when disparate outcomes are explicitly caused by sensitive
attributes. This type of bias can be difficult to prove, as it requires careful control over non-sensitive
attributes to keep them as constant as possible, while only varying sensitive attributes. Famous
correspondence studies have shown that black applicants are less likely to be contacted after
applying for a job compared to otherwise identical white candidates [23, 147]. Similar results
have been found in interview evaluations provided by US-based judges, showing a preference for
standard American accents over international ones [67, 164, 205]. Numerous field experiments
using matched pairs of applicants have highlighted discrimination against women and non-whites;
experiments also point to a risk of direct discrimination against disabled and older applicants
[208, 215]. This is the most obvious BCF; a variety of more subtle ones are listed below.
Horizontal segregation. Job segregation (i.e. the world today) plays a fundamental role in hiring
decisions (i.e. the world tomorrow). Prior experience is considered a fundamental predictor of
suitability for a given position [101]. Horizontal segregation concerns differences in employment
rate across industry sectors associated with sensitive attributes, such as gender and race [28, 243].
Strong gender patterns in diverse regions of the world are linked to persistent gender stereotypes
about agency and communion that shape our perception and expectations [42, 83, 109]. Most field
experiments, for example, demonstrate discrimination against women in men-dominated jobs and
vice versa [215, 216].
Vertical segregation summarizes differences in career progression to leadership positions. Predominantly analyzed with respect to binary gender [53, 82], recent studies have also highlighted
glass ceiling effects for non-binary workers [62], racial minorities [117], and intersectional identities
[273]. When translated into data and dignified with a ground truth status, vertical segregation leads
to models that reinforce wage gaps [222] and lack of diversity in high-status positions.
Cultural fit is often considered predictive of a candidate’s ability to conform and adapt to the core
values and collective behaviors of an organization. Evaluations of cultural fit by recruiters, subjective
or objective, can contribute to maintaining a uniform workforce in the company, especially in more
senior positions, reinforcing horizontal and vertical segregation [3, 219].
Elitism in recruiter evaluations favors candidates educated at prestigious institutions who can also
list specific extracurricular accomplishments correlated with socioeconomic status [218], further
entrenching family status and social class [51, 184].
Biased employee evaluation has different forms and derives from multiple causes. Two key
drivers are stereotypes and employee-manager relationships. Gender and race stereotypes about
competence drive people’s perception on the workplace and potentially bias supervisor evaluations
against female and black employees [116, 229, 233, 242]. Furthermore, a combination of vertical
job segregation and homophily entails that minority employees who are not well represented in
management positions may receive lower ratings when manager-employee personal relationships
have a positive influence on evaluations and promotions [26, 31, 152]
Stereotype violation has a disparate effect on the “transgressor”, depending on their gender.
Women are frequently penalized for gender norm violations that make them appear more agentic
(e.g. competent and self-confident) and less communal (e.g. kind and warm) than stereotypically
expected [115, 195, 247]. This is especially problematic in the hiring domain, where agency is
deemed important for leadership positions and it is harder to demonstrate for women without
giving an impression of low communion [160].
Workplace proximity and availability of reliable commutes can influence job satisfaction [201]
and candidate-employer interactions [262], with amplifying effects introduced by technology [142].
Since discrimination has shaped residential patterns and influenced public transportation, this
factor may have disproportionate impacts along racial and ethnic lines [144].
Wage gaps are a key part of power differences between genders and races [40, 81, 121, 269]. This
BCF has several concurrent causes, including expectations reinforced by the status quo and lower
success in salary negotiation [68, 110, 163]. Models that predict the likelihood that candidates will
accept an offer can reinforce existing wage gaps.
Social networks topology influences job seekers’ awareness of openings [96], and their likelihood
of being successfully screened by recruiters due to a successful referral [136, 284]. Well-connected
candidates have an inherent advantage over candidates with lower centrality; this advantage may
be amplified by algorithms for link prediction [264]. The connection recommender system in a
professional social network was found to underperform for women, recommending them less
frequently for professional connections than men with similar success rates [39]. This effect may
be exacerbated by homophily and biased preferential attachment [14].
3.2 Individual preferences
Next, we consider BCFs that are an apparent consequence of individual preferences, but represent
generalized patterns for protected groups. Listing a bias under this category does not make it an
individual responsibility and a reasonable ground for discrimination. On the contrary, we aim to
highlight the fact that some seemingly individual choices operated by candidates actually result
from wider and recurrent patterns associated with protected attributes. Therefore, employers and
providers of algorithmic hiring models should carefully consider these BCFs.
Job satisfaction influences job commitment [20, 228]. Historically disadvantaged groups such
as transgender, nonbinary, female, black, and disabled workers are more likely to experience
discrimination and harassment on the job [225, 228, 261]. This fact may be reflected in data sets as
a lower tenure for these groups, which can be penalized by algorithms trained to maximize tenure
in order to reduce hiring costs and retain human capital.
Self-promotion gaps related to gender have been documented in the hiring domain [5] and
beyond; men tend to self-evaluate higher than women even without intrinsic incentives [87]. This
reflects on the visibility and perceived competence of candidates at the different stages of the hiring
pipeline; it can be especially difficult to subvert for women due to the social and economic penalties
incurred for violating female gender stereotypes [182].
Willingness to commute is another individual factor with gender-related patterns. Women tend
to be more restrictive in their choice of job search area [78, 161]. This difference may be related to
gender roles with respect to household and childcare responsibilities. Furthermore, people with a
migration background are less likely to own a motor vehicle [146].
Salary negotiation differences between men and women are documented, including in propensity
[163] and strategy [110]. Different interpretations have been advanced, including lower risk aversion
and the perceived chance of success [110, 122]. Although ostensibly a personal outcome of female
candidates, unsuccessful salary negotiation is also based on an unfair status quo that influences
group expectations [110].
Culture-based avoidance or attraction, is a self-selection BCF that influences mainly the sourcing
stage. Explicitly mentioning requirements such as community outreach can signal the posture of an
employer and act as a pull factor for minority job seekers [192, 234]. On the contrary, job descriptions
with unrealistic requirements discourage job seekers who lack one or more requirements, with a
repulsive effect that can be stronger for candidates from vulnerable groups [101, 179]. Wording
itself can also sustain inequality: gendered wording in job advertisements that makes use of
stereotypically agentic (male) language, such as “leadership” or “delivery”, can make a position
less attractive for women [102]. The same alienating effect can occur by signaling an unwelcoming
workplace culture at other stages of the hiring pipeline [274].
Work gaps, i.e. periods without formal employment, often reflect negatively on a candidate’s
probability of securing a job [101]. Gender asymmetries in caregiving responsibilities put women
at a systematic disadvantage [93, 162].
3.3 Technology blindspots
Finally, we describe the biases introduced by biased components integrated into larger algorithmic hiring pipelines. This non-exhaustive list aims at demonstrating the need for proactive biaspreventing reasoning also (and perhaps especially) when using off-the-shelf tools.
Ad delivery optimization can skew the audiences reached by job advertisements. Multiple
studies have shown that maximization of cost-effectiveness based on ad delivery metrics, such
as impressions or clicks, makes delivery skewed in accordance with gender and race stereotypes
in jobs [4, 10, 61, 158]. Ad text and images can further skew the audience [4]. This happens even
though advertisers design neutral campaigns and is exacerbated if they target specific attributes
[258], increasing the opportunity for bias and opacity at the sourcing stage. It should be noted that
the platform(s) chosen to run a campaign can introduce a further bias in favor of its predominant
demographics; campaigns run on platforms that cater to younger users, for example, are less likely
to reach older segments of the population.
Accessibility issues and ableist norms can discourage disabled people from job applications
[226] and tilt evaluations against them [245, 246]. Asynchronous video interviews can produce
specific patterns from candidates with speech impairment (e.g. short answers) or mismeasure
input from candidates with sight impairment (e.g. eye contact), which are judged unfavorably by
algorithmic recruitment models [189].
Disparate performance of language processing and computer vision tools has been widely
demonstrated with respect to gender, race, and other sensitive attributes [27, 37, 241]. Off-the-shelf
algorithms from these domains integrated into hiring pipelines [141] are likely to underserve
minority candidates for feature extraction and negatively affect algorithms that are based on these
feature.
Differences in platform engagement broadly divide people into frequent and infrequent users.
This causes an overrepresentation of the former in the training data, leading to rich-get-richer
dynamics in job platforms [185]. Note that minority job seekers may suffer a lower quality of
service, leading to disengagement and triggering a negative feedback loop by iteratively lowering
training representation, quality of service, and engagement. Moreover, platforms are more likely to
have rich profiles and metadata for their common users, while lacking information for less engaged
job seekers, who are penalized due to missing data.
Biased psychological assessment performance for minorities can result in systematic disadvantages [212]. Systematic differences in the results of psychometric tests between subgroups
[52, 130], caused by low discriminant validity [133] or construct contamination [8], can be especially problematic for tests embedded in larger resource allocation processes, such as hiring
systems.
Background check tools allow employers to obtain additional information on candidates from
public records [244]. These databases contain a wealth of pre-conviction information, such as arrest
data [157] whose validity as a proxy for crime is questionable [97]. Among other critical aspects,
criminal background checks before employment run the risk of feeding the racial disparity of
policing [203] and other areas of the criminal justice system [151] into hiring systems.
Interaction biases between employers and hiring technology can amplify tiny differences in
algorithmic output [16]. During the sourcing stage, for instance, recruiters tend to focus on very
specific credentials, certifications, and keywords that exclude atypical individuals from the initial
pool of candidates, despite having the right skills [101]. More general examples include position
bias that causes underexposure risks for candidates that are not at the top of a ranking [60] and
automation bias leading to over-reliance on technology and reduced human oversight [106, 156].
3.4 Overlaps and Interactions
In the analysis above, we identified and described how the workings of key BCFs contribute to
algorithmic discrimination within a digital and non-digital hiring context. It is important to note
that these factors are interlocking and overlapping insofar as BCFs are mutually reinforced by the
structure of institutions (Section 3.1), individual preferences (Section 3.2), and technological blind
spots (Section 3.3).
Intersectional identities are particularly vulnerable as they are likely to be affected by multiple
BCFs. Let us consider the case of JS, a woman with children and a migration background looking
for a job in the hospitality industry. Her chances of securing suitable employment is hindered
from the outset as (1) her connections to the local industries are weak and advertisements do not
reach her, keeping her unaware of certain possibilities; (2) she finds out about certain openings but
is discouraged from applying by a difficult commute based on public transport. Through public
employment services, her data is entered into a shared database accessed by human resources
companies. (3) Her profile is hastily filled in and lacks important metadata; this fact pushes her
down in rankings every time her profile matches recruiters’ queries, also because the time of last
login influences job-seekers’ rankings. (4) Recruiters seek a catering and hospitality degree that JS
does not have, making matches with her profile infrequent. (5) Due to a lack of leadership roles in
her profile, the only matches she receives are at the apprentice level and (6) she is screened out
from openings employing AVI models that do not recognize her accent. She is interviewed by few
businesses; most turn her down because (7) they deem her a poor cultural fit and (8) are afraid that
she will apply for parental leave. One business is finally willing to hire her through an HR company.
(9) Despite a mid-level payment agreement between the employer and the HR company, the latter
estimates that JS will accept the minimum wage (which she does) and pockets the difference.
This fictitious, yet plausible story sketches how multiple biases compound and reinforce each
other. However, even if intersectional discrimination occurs, there are still reasons why the right
approach to technological design can reduce bias. One upshot of understanding bias as an inherently
intersectional process is that it also offers a way to reduce discrimination. Since the factors that
create bias are interrelated and mutually reinforcing, by halting or ameliorating one BCF, we may
introduce positive feedback loops on other BCFs. By removing the discriminatory effect of any
one factor, we can hope to reduce its influence on the other factors that reinforce each other in a
discriminatory way. For example, an increased representation of a minority group in a company
can improve job satisfaction, increase their importance and visibility, and encourage other minority
applicants in future hiring rounds. With time, this contributes to reducing vertical segregation,
with minority employees in key positions shaping company culture, and attracting more candidates
with a similar background. This optimistic view reflects positive spillover effects [155, 174].
4 MEASURES
Fairness measures for algorithmic hiring consider different types of systems, including AVI scoring,
CV ranking, and advertising algorithms, operating at different stages and on different data modalities.
In this section, we present them in a unified notation (Table 1) and discuss their key dimensions,
summarized in Table 2. It is worth noting that the next three sections are based on a systematic
review of the literature summarized in Appendix A.
4.1 Dimensions of Fairness Measures
We begin with a summary of dimensions that are important in the algorithmic fairness literature;
some are established in the literature, such as flavor [178] and conditionality [275], others are
highlighted as important in the hiring domain, such as granularity and interpretability. It should be
noted that we focus on group fairness; we found a single article treating individual fairness [172].
Flavor. Fairness measures can target different properties of an algorithmic decision-making system.
The main notions of fairness in hiring are the following.
• Outcome fairness [114] is the most common. It looks at predictions from the perspective
of candidates, measuring differences in their preferred outcome, such as being screened
in, typically corresponding to a positive prediction 𝑦ˆ. Systems are deemed fair from an
outcome perspective if quantities such as acceptance rates (Pr(𝑦ˆ = 1)) or true positive rates
(Pr(𝑦ˆ = 1|𝑦 = 1)) are similar between groups.
• Accuracy fairness [24] takes a closer perspective on the decision maker, requesting equalization
of accuracy-related properties between groups, such as the average absolute error. Measures
in this family lack the notion of preferable outcomes and candidate benefits.
• Impact fairness relates algorithmic outcomes to downstream benefits or harms for individuals.
These measures are rare in the literature, as they require a broader understanding and
modeling of the sociotechnical system around the decision-making algorithm.
• Process fairness [111] is a notion that considers the equity of the procedure leading to a
decision. Related to procedural justice [235], process fairness has been operationalized for
algorithmic decision-making based on people’s approval for the use of a given feature in
a specific scenario. In hiring, this has been associated with the predictability of sensitive
attributes from non-sensitive ones [33], implying that the absence of information on sensitive
attributes in the data will lead to fair decision-making.
• Representational fairness [1] relates to stereotyping and biases in representations. In the
context of algorithmic hiring, it is especially relevant for the wording of job descriptions
which can skew the probability of application for different demographics [102].
Conditionality. Conditional fairness measures accept group differences, as long as they can be
attributed to a set of variables deemed acceptable grounds for differentiation. This dimension is
strongly connected to world views [100, 123], and the extent to which differences in variables
between sensitive groups are influenced by measurement errors and unjust social structures.
Granularity. The same model can lead to different results if used in different ways, including
the use of different thresholds for classifiers or different cutoffs for rankers. Measures with fine
granularity take this fact into account by measuring the fairness of a system across different
operating conditions, as opposed to coarse-granularity measures which consider a single point of
operation.
Normativity. Measures with explicit normative reasoning set a precise target for groupwise
quantities, either in absolute terms or relative to each other. Implicit normative reasoning, on the
other hand, is typical of measures introduced without a complete discussion of desiderata. Strong
normative reasoning is, in general, preferable, but it is not a guarantee on its own. For example,
while a measure providing a contextualized and accurate operationalization of a construct defined
in the law displays normativity, the measure will inherit all the limitations of the underlying law.
Interpretability. We consider the interpretability of group fairness along two dimensions. Directioninterpretability allows us to immediately understand whether a group is at an advantage or disadvantage by comparing the measure against a threshold. Magnitude-interpretability lets us quantify
the (dis)advantage by evaluating the distance from a threshold.
Native Multinarity. A measure is multinary if it accounts for more than two sensitive attribute
values. Binary measures can sometimes be extended to the multinary case, whereas truly multinary
measures natively account for this occurrence.
4.2 Notation
Let 𝑥 ∈ X denote a vector containing non-sensitive features and let 𝑦 ∈ Y be an unknown target
variable, inferred at test time as 𝑦ˆ = 𝑓 (𝑥). Furthermore, let 𝑓soft(𝑥) denote a scoring function supporting estimates 𝑦ˆ via thresholding and item ranking 𝜏 = argsort(𝑓soft(𝑥)) via sorting. Furthermore,
let 𝑠 ∈ S indicate a vector of sensitive attributes, so that 𝑠 = 𝑔 defines a specific protected group,
and 𝑠 = 𝑔
c
represents its complement. Overall, a data point or item 𝑖 is indicated as 𝑖 = (𝑥𝑖
, 𝑠𝑖
, 𝑦𝑖)
and 𝑖 = 𝜏 (𝑘) denotes the item at position 𝑘 in ranking 𝜏. For cardinality, let 𝑁 denote the total
number of data points in a sample of interest, let 𝑁𝑔 indicate the number of items in group 𝑔, and
let 𝑁
𝑘
𝑔
be the number of items in 𝑔 among the top 𝑘 of a ranking 𝜏. Additionally, let 𝐷𝑔 ∈ [0, 1]
denote the desired representation for items in 𝑔 among the ones receiving a favorable algorithmic
outcome, e.g., the top-ranked items or the positively classified ones. Finally, let ℎ : X → S denote
a classifier issuing predictions in S and let ℎsoft(𝑥) indicate its soft scoring version (e.g., issuing
posterior membership probabilities).
4.3 Measures
4.3.1 Outcome Fairness. These measures summarize the perspective of candidates by focusing on
their preferred outcome; they are the most common.
Skew at 𝑘 (skew@k) [103] evaluates a ranking at a specific rank 𝑘. It computes the logarithm of
the ratio between the desired representation of a sensitive group 𝐷𝑔 and the actual representation
This measure exhibits strong normativity, as it requires a precise definition of target representation
𝐷𝑔 for each sensitive group. It is direction-interpretable, as values above zero indicate an advantage
for group 𝑔, while the presence of the log function hinders its magnitude-interpretability. As a
summary for multiple groups, Geyik et al. [103] consider the maximum and minimum skew values,
e.g. max-skew@k = max𝑔∈S skew@k𝑔
.
Normalized Discounted cumulative KL Divergence (NDKL) [11, 103] computes a divergence
between the desired distribution of the representation (𝐷 = {𝐷𝑔, ∀𝑔 ∈ S}) and the actual one
at rank 𝑘 (𝑁
𝑘 = {𝑁
𝑘
𝑔
/𝑘, ∀𝑔 ∈ S}). The measure consists of KL divergences, calculated at each
rank, and aggregated with a logarithmic discount, making it granular. Notice that KL divergence is
another way to summarize skew@k for multiple groups, weighted with a logarithmic discount. It
is defined as
NDKL =
1
𝑍
∑︁
𝐾
𝑘=1
1
log2
(𝑘 + 1)
𝑑KL (𝐷, 𝑁𝑘
) (2)
where 𝑍 is a normalization constant. Note that several factors contribute to making NDKL difficult
to interpret. First, advantages and disadvantages for a group 𝑔 at some rank 𝑘 can yield the same
KL divergence value. Second, advantages and disadvantages at different ranks do not compensate
each other; if a group is underrepresented at low ranks, its overrepresentation at high ranks leads
to even worse values of NDKL, despite being a form of compensation.
Acceptance Rate Ratio, better known as Disparate Impact (DI) [33, 38, 120, 148] is a measure
of disparity in classification with a fixed threshold. Note that this measure is also used in rankings
by translating a threshold (or percentile) into a cutoff rank 𝑘. This measure is related to US labor
law, adverse impact, and the 80% rule (Section 8.2). Below, we report its popular min-over-max
version, computing the selection rate ratio between the worst-off and best-off groups:
DI =
min𝑔∈S 𝑁
𝑘
𝑔
/𝑁𝑔
max𝑔∈S 𝑁
𝑘
𝑔 /𝑁𝑔
=
min𝑔∈S Pr(𝑦ˆ = 1|𝑠 = 𝑔)
max𝑔∈S Pr(𝑦ˆ = 1|𝑠 = 𝑔)
(3)
We consider this measure interpretable, so long as the best and worst-off groups are reported.
Acceptance Rate Difference better known as Demographic Disparity (DD) [222], focuses
on disparities in groupwise acceptance rates, similarly to DI, but computes the difference instead of
the ratio. We define it below for classifiers and ranking algorithms, implicitly assuming a cutoff
point at rank 𝑘 for the latter:
DD = 𝑁
𝑘
𝑔
/𝑁𝑔 − 𝑁
𝑘
𝑔
c/𝑁𝑔
c
= Pr(𝑦ˆ = 1|𝑠 = 𝑔) − Pr(𝑦ˆ = 1|𝑠 = 𝑔
c
) (4)
This approach may be easier to interpret [286], but fails to capture large disparities when acceptance
rates are small. If, for example, Pr(𝑦ˆ = 1|𝑠 = 𝑔) = 10e−02 and Pr(𝑦ˆ = 1|𝑠 = 𝑔
c
) = 10e−07, we
measure a low value DD ≃ 10e−02, despite a difference of five orders of magnitude in acceptance
rates.
Representation in Positive Predicted (RPP) [4, 132, 199] is a measure used in noncooperative
audits, where the overall population of interest for an algorithm is unknown. In online advertising,
campaigners are informed about the size and composition of the audience reached by an ad (positive
predicted class) but have no information on platform users and users who were active and thus
candidates for an ad impression. This makes it impossible to compute groupwise acceptance rates
(Pr(𝑦ˆ = 1|𝑠 = 𝑔)), but allows for estimates of groupwise representation in the positive predicted
class (Pr(𝑠 = 𝑔|𝑦ˆ = 1)) and, trivially, its difference with respect to the complementary group:
RPP𝑔 = Pr(𝑠 = 𝑔|𝑦ˆ = 1) (5)
RPPD = RPP𝑔 − RPP𝑔
c = 2 RPP𝑔 −1 (6)
True Positive Rate Difference (TPRD) [63, 119] measures disparities in true positive rates
(also known as recall) between different sensitive groups. This measure is closely related to equal
opportunity [114] and separation [17] and presupposes the availability of a ground-truth variable 𝑦
to condition on:
TPR𝑔 = Pr(𝑦ˆ = 1|𝑦 = 1, 𝑠 = 𝑔)
TPRD = TPR𝑔 − TPR𝑔
c (7)
A closely related measure is the False Negative Rate Ratio (FNRR) [148], defined as
FNR𝑔 = Pr(𝑦ˆ = 0|𝑦 = 1, 𝑠 = 𝑔)
FNRR =
FNR𝑔
FNR𝑔
c
(8)
As an aggregate measure for non-binary sensitive attributes, Hemamou and Coleman [119]
propose the Root Mean Square (RMS) of the vector containing all TPRD components:
RMS =
√︄
1
|S|
∑︁
𝑔∈S
TPRD2
𝑔
(9)
Nandy et al. [185] propose an eXtended Equality of Opportunity (xEO) measure, which is a
granular version of TPRD. They consider a soft classifier with a variable threshold and compute the
Kolmogorov-Smirnov distance between the resulting score distributions for positives in different
sensitive groups.
xEO = max
𝑥
[| Pr(𝑓soft(𝑥) ≤ 𝑡|𝑦 = 1, 𝑠 = 𝑔) − Pr(𝑓soft(𝑥) ≤ 𝑡|𝑦 = 1, 𝑠 = 𝑔
c
)|] (10)
Discounted Representation Difference (DRD) [283] is a granular measure of demographic
disparity focused on rankings. It measures the difference in acceptance rates with a variable cutoff
rank 𝑘 by observing the sensitive attribute of the item 𝜏 (𝑘) and applying a logarithmic rank-based
discount before updating a counter. In other words, DRD measures groupwise representation as
DRD =
∑︁
𝐾
𝑘=1
1
log2
(𝑘 + 1)
[1(𝑠𝜏 (𝑘) = 𝑔) − 1(𝑠𝜏 (𝑘) = 𝑔
c
)] (11)
This measure is interpretable since it conveys the difference in candidates’ exposure across groups
under a recruiter browsing model with logarithmic decay. See Carterette [41] for an introduction
to browsing models.
Score KL Divergence (SKL) [199] considers the distribution of scores (𝑓soft(𝑥𝑖)) in different
groups and measures unfairness by computing their KL divergence. Let 𝐷
𝑓
𝑔 define the probability
distribution of continuous scores 𝑓soft(𝑥𝑖) for group 𝑔, then SKL is defined as
SKL = KL(𝐷
𝑓
𝑔
, 𝐷𝑓
𝑔
c ) (12)
Log Rank Regression (LRR) [48] is a measure defined for search engines by fitting a linear
model on the logarithm of rank 𝑘 = 𝜏
−1
(𝑖) at which candidates are presented on the result page.
Independent variables comprise both sensitive 𝑠 and non-sensitive attributes 𝑥, where the latter
include skills and education. LRR reports the coefficient (and 𝑝 value) associated with the sensitive
attribute. Fitting models to quantify the influence of a sensitive feature on an outcome variable
is typical of situations with limited access to the model(s) responsible for the outcomes. This is a
common setting for external noncooperative audits.
log(𝜏
−1
(𝑖)) = 𝛽𝑥𝑥𝑖 + 𝛽𝑠𝑠𝑖 + 𝜇 + 𝜖
LRR = ˆ𝛽𝑠
(13)
A similar approach is proposed in Lambrecht and Tucker [158] to estimate the influence of sensitive
attributes such as age and gender in advertisement delivery optimization. This measure considers
differences in outcomes acceptable, so long as they can be explained by non-sensitive attributes 𝑥.
Mean Error Difference (MED) [231] focuses on regression, measuring systematic groupwise
biases. Following a more general paradigm, MED caters to the multinary case by considering the
maximum and minimum (signed) bias.
MED = max
𝑔∈S
1
𝑁𝑔
∑︁
𝑖∈𝑔
(𝑦𝑖 − 𝑓soft(𝑥𝑖)) − min
𝑔∈S
1
𝑁𝑔
∑︁
𝑖∈𝑔
(𝑦𝑖 − 𝑓soft(𝑥𝑖)) (14)
4.3.2 Accuracy fairness. These measures study model accuracy across sensitive groups, aligning
more closely with the perspective of decision makers. They are all conditional on the target variable
𝑦, inheriting the biases encoded in the ground truth.
Mean Absolute Error (MAE) [231, 276] targets regression problems similarly to MED (Eq. 14).
It compares groupwise accuracy by measuring the absolute error for each individual and computing
the average for items in the same sensitive group.
MAE =
1
𝑁𝑔
∑︁
𝑖∈𝑔
|𝑦𝑖 − 𝑓soft(𝑥𝑖)| − 1
𝑁𝑔
c
∑︁
𝑖∈𝑔
c
|𝑦𝑖 − 𝑓soft(𝑥𝑖)| (15)
Balanced Classification Rate Difference (BCRD) [148] is a measure of the disparity in classification accuracy between groups. It targets the balanced classification rate, defined as the average
between the true positive and the true negative rate:
BCR𝑔 =
TPR𝑔 + TNR𝑔
2
BCRD = BCR𝑔 − BCR𝑔
c (16)
Mutual Information Difference (MID) [148] is another measure of classification accuracy
fairness. It computes model accuracy within a group 𝑔 as the mutual information between the
target 𝑦 and the prediction 𝑦ˆ for the items in 𝑔 and compares it against the mutual information for
the remaining items.
MI𝑔 = MI{𝑖∈𝑔} (𝑦ˆ𝑖
, 𝑦𝑖)
MID = MI𝑔 − MI𝑔
c (17)
4.3.3 Impact fairness. This flavor of fairness models the impact of algorithmic outcomes on data
subjects, measuring differences in harms and benefits between populations.
Salary Difference (SD) [222] is the only measure of this family proposed in the literature.
Considering an embedding-based model, each candidate is matched to the closest vacancy in the
embedding space. Based on the average wage for the role described in the vacancy, an average salary
is calculated for male and female candidates in the same industry, and their difference quantifies
the gender impact of the model on earnings in that industry.
𝑓 (𝑥𝑖) : closest job match for candidate 𝑖
𝑊 (𝑓 (𝑥𝑖)) : average wage for job 𝑓 (𝑥𝑖)
SD =
1
𝑁𝑔
∑︁
𝑖∈𝑔
𝑊 (𝑓 (𝑥𝑖)) − 1
𝑁𝑔
c
∑︁
𝑖∈𝑔
c
𝑊 (𝑓 (𝑥𝑖)) (18)
4.3.4 Representational fairness. Measures to quantify stereotypes and representational harms are
relatively understudied [1, 92], despite being a fundamental driver in the reinforcement of societal
biases.
Gender Bias Score (GBS) [128] is a coarse measure of bias toward “masculine” or “feminine
language” in job descriptions. It takes advantage of the word inventory from Konnikov et al. [150],
which comprises traits associated with gender roles in labor, so that each term 𝑡 in a job description
can theoretically be coded as belonging to a set of stereotypically masculine, feminine, or neutral
traits. The measure is defined as
GBS = sign(𝑥𝑚 − 𝑥𝑓 ) · max 
𝑥𝑚 − 𝑥𝑓
𝑥𝑚
,
𝑥𝑓 − 𝑥𝑚
𝑥𝑓

, (19)
where 𝑥𝑚 (𝑥𝑓
) represents the number of stereotypically male (female) words in a job description.
4.3.5 Process fairness. These notions of fairness operationalize desiderata about decision-making
beyond outcomes. Frequently, they derive from judgments of admissibility for specific variables 𝑥
in a given scenario. In algorithmic hiring, the literature focuses on the amount of information on
sensitive attributes 𝑠 encoded by non-sensitive features 𝑥 and the target variable 𝑦, with the goal of
minimizing it.
Sensitive AUC (sAUC) [33, 119, 120, 194, 196, 222] is a widely used measure of the information
about sensitive attributes stored in (proxy) non-sensitive attributes. It is based on training a
classifier ℎ(𝑥) for the sensitive attribute 𝑠 on non-sensitive features 𝑥; its accuracy is evaluated as
the Area Under the receiver operating characteristic Curve (AUC). If little information on sensitive
attributes can be recovered from the variables employed in the decisions, then the decision is
deemed procedurally fair according to this definition.
sAUC = AUC(ℎsoft(𝑥)) (20)
Hemamou et al. [120] extend (sAUC) to the multi-class case by training one-vs-all classifiers and
reporting their maximum AUC value.
Ground Truth Regression (GTR) [196] regresses (𝑥, 𝑠) on𝑦, and focuses on the latter coefficient
(
ˆ𝛽𝑠
) similarly to LRR (Eq. 13), with the key difference that the target of the regression is the target
variable. This measure estimates the importance of the sensitive attribute to predict the target,
conditional on non-sensitive attributes. In other words, GTR audits the biases encoded in the target
variable, recognizing it as a key factor for the decision-making process, regardless of the predictive
model employed:
log 
𝑦𝑖
1 − 𝑦𝑖

= 𝛽𝑥𝑥𝑖 + 𝛽𝑠𝑠𝑖 + 𝜇 + 𝜖
GTR = 𝛽𝑠
(21)
Both sAUC and GTR are ex-ante measures, i.e. they can be computed from the data before the final
model is trained; therefore, the granularity dimension does not apply to them.
Mutual Information Amplification (MIA) [276] is another measure of process fairness, which
considers the process fair if it does not reveal more information about sensitive attributes than the
ground truth does. This metric computes the mutual information between first 𝑦ˆ and 𝑠, and second
between 𝑦 and 𝑠; positive differences between the two are considered an undesirable amplification
of information about sensitive attributes leaked through predictions.
MIA = MI(𝑦, 𝑠 ˆ ) − MI(𝑦, 𝑠) (22)
Differently from sAUC and GTR, MIA is an ex-post, model-dependent measure.
4.4 Discussion
In this section, we describe the main characteristics of the surveyed measures and how they inform
fairness measurement choices.
Choosing a measure. We introduce a made-up scenario to exemplify deliberation around fairness
monitoring. EquiHire, a fictitious HR company, is choosing a fairness measure to monitor its
candidate search systems for fairness with respect to ethnicity. For the sake of simplicity, they
restrict the realm of possibilities to Table 2. Since ethnicity is a multinary sensitive attribute,
they discard binary measures such as skew@k and DD. Moreover, EquiHire practitioners want
to describe their equity strategy in white papers and external communication. Therefore, they
prioritize an interpretable measure, excluding complex measures such as NDKL and SKL which
would be difficult to explain. Although they have access to signals related to candidate fitness (𝑦),
they become available with great delay after hiring decisions are taken. To assess system fairness
in a timely manner, they discard 𝑦-conditional measures such as TPR and RMS. Finally, since they
have visibility into the downstream hiring decisions, they can use a low-granularity measure. These
considerations lead EquiHire to choose DI as their primary fairness measure. For a complementary
angle focused on outcome fairness, they choose to monitor wage differences for employees hired
through their systems, adopting SD as an additional measure.
To reiterate, this is just one fictitious scenario and not a fixed recommendation for choosing the
right measure. It demonstrates the importance of key characteristics of the measures summarized
in Table 2 for practitioner decisions; in the paragraphs below, we expand on the factors driving
these decisions.
Fairness diagnostics vs. fairness optimization. Ease of interpretation is a desirable property,
especially for fairness measures, as confirmed by the popularity of DI. Nevertheless, several fairness
measures adopted in hiring are difficult to read in absolute terms, making it challenging to understand the severity of fairness violations based on their values. These values can only be interpreted
relative to one another, i.e. it is clear that one value is more desirable than another, making them a
possible target for optimization but less suited for diagnostics. This is especially true for measures
of accuracy fairness such as BCRD and MID. Measures of outcome and impact fairness, such as DD
and SD, tend to be more interpretable, since they are typically defined as differences between the
probability of obtaining desirable outcomes for different groups. This holds especially for binary
measures, while multinary measures, such as RMS, often sacrifice interpretability to summarize
disparities across multiple groups.
Blurred lines between ranking and classification. In the literature, classification and ranking
are typically considered separate tasks with separate algorithmic fairness measures. In hiring, we
find ranking systems evaluated according to classification measures such as DI [38], selection tasks
solved with rankers [38], and target variables of similar nature encoded as binary, multinary, or
continuous (Section 6). For this reason, the separation between classification and ranking is less rigid
than in other domains, and the question of which measures are best suited to evaluate these systems
arises. A fundamental part of the answer lies in the expected flexibility of use for these models.
If the key aspects of their usage are fixed, including the cutoff thresholds for different outcomes,
then a measure with coarse granularity, considering a single operating condition (typical of the
fair classification literature – e.g. DD, TPRD), is most suited for evaluation. On the contrary, for
models whose operating conditions are more uncertain, requiring human interaction or threshold
fine-tuning, it is preferable to adopt a measure with finer granularity (often derived from the fair
ranking literature – e.g. NDKL, DRD), which averages outcomes across multiple realizations of a
browsing model.
Diagnosing biases. Fairness measures are especially useful when they provide actionable diagnostics by highlighting specific biases described in Section 3. Measures of process fairness such
as sAUC and MIA detect the presence of sensitive attribute proxies. Dedicated proxy reduction
approaches (Section 5) can mitigate the resulting risk of discrimination. Representational fairness
(GBS) captures biases in representations; when applied to job descriptions, extreme values highlight
stereotypically gendered language, signaling a risk of culture-based avoidance. Impact fairness
can highlight nuanced aspects of hiring beyond selection rates; SD, for instance, captures wage
gaps and salary negotiation differences prompting further analysis into remuneration packages.
Measures of outcome (e.g. DI) and accuracy fairness (e.g. MAE) can serve as high-level metrics
by highlighting the effects of multiple factors acting together. To exemplify, a combination of job
segregation, work gaps, and disparate performance of language processing tools, even if relatively
weak on their own, may trigger a very low (unfair) value of DI when they compound.
Assorted fairness flavors. No single measure provides a complete picture. Different fairness
flavors have complementary strengths and weaknesses. Most of the fairness measures considered in
hiring focus on outcome equity; the field is strongly influenced by the 80% rule (Section 8.2), which
is appreciated as a quantitative rule of thumb, but also often criticized [74, 267]. Indeed, outcome
fairness is based on a narrow view of algorithmic hiring as a single decision point abstracted away
from its context, where equity is purely a function of algorithmic estimates and (sometimes) their
similarity to target variables approximating a ground truth. Similar criticism can be moved to
accuracy fairness, with the additional limitation that it is less interpretable and less aligned with
the desiderata of job seekers. Departing from this approach, process fairness is operationalized
with reference to the information on sensitive attributes encoded in the remaining variables. More
work is required to understand process fairness in hiring more broadly and to suitably (if at all)
operationalize it quantitatively. Impact fairness quantifies the downstream impacts of algorithmic
outcomes on different populations; modeling important aspects of the surrounding socio-technical
system, it goes beyond brittle algorithmic abstraction. Since these measures are exceedingly rare,
we highlight the need for more context-specific research to understand and model the benefits and
harms of decisions on job candidates at different stages of the hiring pipeline. Overall, practitioners
developing equity monitoring protocols should consider multiple fairness angles to gain a nuanced
and more complete picture.
Ignoring privileged and disadvantaged groups. The definition of sensitive attributes in antidiscrimination law is informed by the historical (dis)advantage of specific groups [230]. Gender and
race, for example, are considered sensitive attributes due to the recurrent structural disadvantages
incurred by women and black people. This is especially true in hiring, where surveys and metaanalyses find consistent biases against women and ethnic minorities [23, 147, 208]. Although it is
commonly held, especially in fairness research, that disparities against disadvantaged groups should
be mitigated, there is less consensus on how to treat algorithms that happen to favor historically
disadvantaged communities. In other words, should algorithmic fairness be symmetrical and reject
a priori notions of privileged and disadvantaged groups? This is an important normative question,
seldom acknowledged in the fairness literature, with immediate consequences on the choice of
measures. For example, the version of DI reported in Equation (3) computes the ratio between
the acceptance rates of the worse-off group (min) and the best-off group (max), ignoring prior
knowledge of structural inequality and affected communities.
5 MITIGATION STRATEGIES
Several algorithms have been proposed in the literature to improve model fairness; they are
summarized in Table 3. We present them distinguishing between pre-processing, in-processing,
and post-processing algorithms, depending on their applicability before, during, and after training.
5.1 Pre-processing
Rule-based approaches perform a set of manipulations, typically defined by experts, on text
data. They are related to process fairness (Section 4), as they focus on reducing the amount of
information on sensitive attributes contained in non-sensitive features, i.e. to remove sensitive
attribute proxies (Section 3). Rule-based Scraping [63] is a heuristic for text data focused on
gender, aimed at removing all words that explicitly refer to the gender of a person, including first
names and titles. In general, it acts as a feature transformation 𝑥
′ = scrp(𝑥). Under bag-of-words
representations, the scraping function is a feature selection mechanism that removes features in a
censored vocabulary V.
scrp : X → X′ ⊆ X
scrp(𝑥
𝑗
) =
(
𝑥
𝑗
, if 𝑥
𝑗 ∉ V
∅, if 𝑥
𝑗 ∈ V
De-Arteaga et al. [63] study the effectiveness of this approach in job classification from short
biographies. They find it to be moderately effective in reducing TPRD. Parasurama and Sedoc
[194] take this approach one step further on a CV screening application. They define several rules
for removing other strings related to gender, including email addresses, intrinsically gendered
words (e.g. “waitress”), and hobbies. Rule-based Substitution [222] is a closely related approach,
which replaces intrinsically gendered words with neutral words; for example, “his” is changed into
“theirs”. Due to redundant encoding of sensitive information in the data, rule-based approaches
often represent a weak baseline with limited impact on fairness.
Importance-based Scraping is an adversarial approach for feature removal based on a sensitive
attribute classifier. Parasurama and Sedoc [194] consider a resume screening system and exploit
contextualized word representations to train a gender classifier, and iteratively scrape the words
with the largest feature importance for gender classification. In other words, they train a sensitive
attribute classifier
𝑠ˆ = ℎ(𝑥)
and assess the importance of features by selectively removing them from the prediction task. Proxy
features P found to be most predictive of 𝑠 (highest marginal contribution to ℎ(·), e.g. measured
via SHAP) are scraped:
scrp(𝑥
𝑗
) =
(
𝑥
𝑗
, if 𝑥
𝑗 ∉ P
∅, if 𝑥
𝑗 ∈ P
Parasurama and Sedoc [194] show that SHAP-based scraping can achieve a sizeable sAUC drop
with a limited negative impact on performance. Booth et al. [33] develop an equivalent scheme for
iterative feature removal in asynchronous video interview analysis from multimodal data. They
confirm the suitability of this method to improve process fairness (sAUC); outcome fairness (DI)
also improves, but only for systems that were initially very unfair.
Subspace Projection is a common approach to reduce gender bias in text representations
based on word embeddings. Initially proposed by Bolukbasi et al. [32], this method is based on the
observation that most intrinsically gendered information in word embeddings, such as the difference
between the vectors for “mother” and “father”, is contained within a small gender subspace. The
algorithm is based on re-embedding each word by projecting it orthogonally to this space. Let 𝑤®
denote the embedding of a word and 𝐺 the gender subspace. Each word is re-embedded to
𝑤®
′ =
𝑤® − proj𝐺𝑤®
|| ®𝑤 − proj𝐺𝑤® ||
In the algorithmic hiring literature, subspace projection is used in Parasurama and Sedoc [194]
to reduce gender biases in a resume screening application. Although in theory this approach
is suitable to remove gender proxies and contrast the negative effects of stereotype violations, it
proves ineffective in reducing the amount of gender information contained in resumes, as measured
by sAUC, in alignment with prior art [108].
Balanced Sampling is a broadly applicable scheme to reduce correlations between sensitive
attributes and target variables in the training set. Arafan et al. [11] propose a down-sampling
scheme to achieve an equal representation of sensitive groups among positive and negative points
in the training set. For a binary sensitive attribute, this condition can be formulated as
Pr
𝜎
(𝑠𝑖 = 𝑔|𝑦𝑖 = 𝑦) = Pr
𝜎
(𝑠𝑖 = 𝑔
c
|𝑦𝑖 = 𝑦), ∀𝑦 ∈ Y,
where we let 𝜎 denote an algorithm’s training set. Yan et al. [276] propose an upsampling approach
to enforce the same condition before training a multimodal data fusion algorithm for the analysis
of asynchronous video interviews [141]. Overall, balanced sampling can reduce the influence of
job segregation on hiring algorithms.
Group Norming is a feature manipulation approach for tabular data enforcing a similar feature
distribution in all sensitive groups, through normalization. Booth et al. [33] propose Groupwise
z-Normalization, i.e. they divide data points based on their sensitive group membership, and
standardize each feature by subtracting the groupwise mean and dividing by the groupwise standard
deviation.
𝜇𝑔 =
1
𝑁𝑔
∑︁
𝑖∈𝑔
𝑥𝑖
std𝑔 =
1
𝑁𝑔
∑︁
𝑖∈𝑔
(𝑥𝑖 − 𝜇𝑔)
2
𝑥
′
𝑖 =
𝑥𝑖 − 𝜇𝑔
std𝑔
if 𝑖 ∈ �
This approach represents an intermediate view on conditional discrimination: it prohibitsinter-group
discrimination based on a specific feature, while allowing it as a basis for intra-group discrimination.
It is tested on multimodal data and found to decrease gender predictability (sAUC) for paraverbal
and visual data, while increasing predictability for verbal features and only marginally improving DI.
It is unclear how to generalize this method under multiple protected attributes (e.g. race and gender);
a separate application to each intersectional group (e.g. black women) is the most straightforward
extension, but increasingly smaller groups run the risk of unstable normalization. Considering its
limited impact on both process and outcome fairness, in conjunction with its controversy in US
employment law [22, 165], the use of Group Norming is not recommended.
5.2 In-processing
Adversarial Inference [120, 199, 222, 276] is an in-processing approach to remove sensitive
information from latent representations that can be applied across tasks (e.g. classification, ranking)
and data modalities (e.g. tabular, images). It leverages process fairness to reduce sensitive attribute
proxies in pursuit of outcome fairness [73]. This approach directly models an adversary trying
to infer an individual’s sensitive attributes 𝑠𝑖 from their latent representation 𝑙(𝑥𝑖). The latent
representation is typically derived in one or more layers of a neural architecture whose goal is to
predict the target variable 𝑦 associated with employability. The adversarial loss for inference is
defined as
𝐿
ADV
INF =
1
𝑁
∑︁
𝑖
dist(𝑠𝑖
, 𝑑 (𝑙(𝑥𝑖)))
where 𝑑 (·) represents the layer(s) in the adversarial branch, so that ℎ(𝑥) = 𝑑 (𝑙(𝑥𝑖)) = 𝑠ˆ𝑖
is the
inferred sensitive attribute value, and dist(·) computes its distance from the actual value 𝑠𝑖
. Rus
et al. [222] show the suitability of this method to improve selected process, outcome, and impact
fairness indicators in a job recommendation scenario, while Peña et al. [199] demonstrate SKL
improvements in a multimodal setting based on synthetic resume ranking.
Face Decorrelation [120] was proposed for asynchronous video interview systems and, more
generally, algorithms that process face images. This approach is based on the key assumption
that face data contain enough information on sensitive features such as gender and race, so that
successful debiasing can be achieved without explicit sensitive attribute information. More in detail,
let 𝑙(𝑥) denote a latent representation from a neural architecture used for employability prediction,
and let 𝑤(𝑥) denote a representation of the candidates’ face obtained from a state-of-the-art feature
extraction method for face recognition [65]. Hemamou et al. [120] propose two schemes based on
Mean Squared Error (MSE) and Negative Sampling (NS). Under MSE, the adversary branch tries to
leverage latent representations to reconstruct face features by minimizing
𝐿
ADV
MSE =
1
𝑁
∑︁
𝑖
[𝑑 (𝑙(𝑥𝑖)) − 𝑤(𝑥𝑖)]2
where 𝑑 (·) represents the final dense layer in the adversarial branch. Under NS, the adversary
exploits the latent representation 𝑙(𝑥𝑖) extracted from an interview to discriminate the respective
candidate from the remaining ones by maximizing the softmax
𝐿
ADV
NS (𝑥𝑖) =
exp(sim(𝑙(𝑥𝑖),𝑤(𝑥𝑖)))
Í
𝑗≠𝑖 exp(sim(𝑙(𝑥𝑖),𝑤(𝑥𝑗)))
where sim(·) represents a similarity function between the face recognition features 𝑤(𝑥𝑖) and
the representations 𝑙(𝑥𝑖) learnt by the main branch of the network. Both variants of Adversarial
Removal (NS, MSE) are shown reduce the sensitive information encoded in latent representations:
notably, their sAUC is on par with adversarial methods explicitly trained to predict gender and
ethnicity, and may be suited for settings where sensitive attributes are unavailable during training.
The effectiveness of Face Decorrelation for outcome fairness is more nuanced, showing positive
effects on DI for very unfair models based on the video modality and limited effects on more
equitable systems based on language and audio.
Name Decorrelation [119] is a similar approach proposed for text data, based on sensitive
information encoded in names. The goal of this method is to reduce the Mutual Information (MI)
between the representations of individuals, such as document embeddings extracted from their
resumes, and a word embedding of their name. To handle the complexity of MI estimation in highdimensional continuous spaces, the method focuses on the MI between the latent representation of
the input 𝑙(𝑥𝑖) and a low-dimensional projection of their name 𝑡˜
𝑖
. The adversarial loss function is
defined as
𝐿
ADV
name =
1
𝑁
∑︁
𝑖
MIˆ (𝑡˜
𝑖
,𝑙(𝑥𝑖))
This approach reduces the ability of adversaries to infer an individual’s gender and ethnicity from
their hidden representations as measured by sAUC in a job classification task. In terms of outcome
fairness, Name Decorrelation is found to improve TPRD and RMS with respect to gender but not
ethnicity. It is worth noting that the original disparities achieved by a vanilla model, measured by
RMS and TPRD, were smaller for ethnicity than for gender. Similarly to Hemamou et al. [120], this
result suggests that targeting this type of process fairness can improve outcome fairness in highly
imbalanced situations, while only providing limited benefits in situations with lower inequity.
Feature Weighting schemes learn to decrease the importance of a feature based on its likelihood
of increasing the unfairness of a model. Fair TF-IDF [69] is an in-processing approach for text
classification and ranking applications, such as resume filtering. As the name suggests, this
algorithm is an extension of TF-IDF [237], one of the most popular and influential algorithms in
text search engines. In response to a query describing a job, TF-IDF produces a score 𝑓soft(𝑥𝑖) for
each resume based on the count of query terms in item 𝑖 and on the specificity of the terms in the
entire resume collection. In other words, let 𝑡 denote a term (word), potentially present in a resume
𝑖 and in a query 𝑞 describing a job posting; TF-IDF(𝑖, 𝑡) is the product of a term frequency tf(𝑖, 𝑡)
and an inverse document frequency idf(𝑡). The tf(𝑖, 𝑡) factor summarizes the importance of 𝑡 in
resume 𝑖 by counting the occurrences of 𝑡 in 𝑖. The idf(𝑡) factor conveys the specificity of term 𝑡 by
counting how many resumes in the entire collection contain the term 𝑡 and defining idf(𝑡) as its
inverse; idf(𝑡) can be seen as a weight that increases (decreases) the importance of rare (common)
words. Deshpande et al. [69] propose a further weighting scheme based on penalizing terms that
are highly specific to a given group.
𝑝-ratio(𝑡) =
min𝑔∈S Pr(𝑡 ∈ 𝑖|𝑖 ∈ 𝑔)
max𝑔∈S Pr(𝑡 ∈ 𝑖|𝑖 ∈ 𝑔)
fair-tf-idf(𝑖, 𝑡) = tf(i,t) · idf(t) · 𝑝-ratio(t)
𝑓soft(𝑖, 𝑞) =
∑︁
𝑡 ∈𝑞
fair-tf-idf(𝑖, 𝑡)
The authors also propose more complex weighting schemes for the fairness factor 𝑝-ratio(𝑡), and
test their ability to improve system fairness as measured by DI.
5.3 Post-processing
DetGreedy [103] and its variants are post-processing methods for ranking algorithms targeting
NDKL. Given a desired representation of sensitive groups, expressed as a target distribution
𝐷 = {𝐷𝑔, ∀𝑔 ∈ S} (Eq. 2), Geyik et al. [103] seek to ensure this representation at different ranks.
Starting from the target distribution 𝐷, DetGreedy populates the ranking progressively from the
top to the bottom rank with the most relevant items from underrepresented groups. To do so, it
maintains a counter 𝑁
𝑘
𝑔
for the number of items from group 𝑔 that have already been placed in
the top 𝑘 positions of the ranking; this counter determines two priority sets from which items at
rank 𝑘 + 1 can be drawn. The high priority set G𝐻 consists of items from groups that are below the
desired quota. The low-priority set G𝐿 consists of groups that are above their desired quota, but
only by a small margin.
G𝐻 = {𝑖 ∈ 𝑔 : 𝑁
𝑘
𝑔 < ⌊𝐷𝑔 · (𝑘 + 1)⌋}
G𝐿 = {𝑖 ∈ 𝑔 : ⌊𝐷𝑔 · (𝑘 + 1)⌋ ≤ 𝑁
𝑘
𝑔 < ⌈𝐷𝑔 · (𝑘 + 1)⌉}
If G𝐻 is not empty, DetGreedy chooses the most relevant item from the groups in G𝐻 ; otherwise, it
samples one from G𝐿.
𝜏 (𝑘 + 1) =
(
argmax𝑖∈ G𝐻 ,𝑖∉{𝜏 (1),...,𝜏 (𝑘) } 𝑓soft(𝑥𝑖), if G𝐻 \ {𝜏 (1), . . . , 𝜏 (𝑘)} ≠ ∅
argmax𝑖∈ G𝐿,𝑖∉{𝜏 (1),...,𝜏 (𝑘) } 𝑓soft(𝑥𝑖), otherwise
By prioritizing items with higher scores in G𝐿, DetGreedy may end up violating some minimum
representation constraints at some rank, i.e. ∃𝑔 s.t. 𝑁
𝑘
𝑔 < ⌊𝐷𝑔 · 𝑘⌋. This happens when more than
one group is in G𝐻 . To mitigate this risk, Geyik et al. [103] propose two variants termed DetCons
and DetConsSort. DetCons tries to avoid this occurrence by prioritizing groups that are more
likely to enter G𝐻 at the next iteration, while DetConsSort is a non-greedy algorithm that can
re-order previous items dynamically to avoid constraint violations at the current rank. DetGreedy is
implemented in LinkedIn Recruiter to ensure equitable gender representation in candidate search;
the desired gender distribution 𝐷𝑔 is made query-dependent, and set to match the distribution of
qualified candidates for the search criteria.
CDF Rescoring [185] is a post-processing method targeting xEO for recommender systems.
xEO is a fine-granularity measure defined in Equation (10), studying the properties of the soft
classifier 𝑓soft(𝑥) at every possible threshold; it requires that the probability of positive items in a
group {𝑖 ∈ 𝑔 : 𝑦𝑖 = 1} achieving a score below a threshold 𝑡 should be the same for every group,
at every threshold 𝑡. This is achieved by re-mapping item scores to their groupwise Cumulative
Distribution Function (CDF) as:
𝑓
′
soft(𝑥𝑖) = Pr(𝑓soft(𝑥) ≤ 𝑓soft(𝑥𝑖)|𝑦 = 1, 𝑠 = 𝑠𝑖)
In other words, new soft scores are mapped to the [0, 1] interval, according to the CDF of old
scores for positive points in their group, ensuring xEO = 0. Nandy et al. [185] propose several
extensions to this approach, to achieve xEO across all target class values, to account for position
bias in the target, and to trade off fairness and accuracy. This method is tested on a friendship
recommendation engine in a live proprietary system (most likely LinkedIn), where sensitive
groups are defined based on the level of activity on the platform, mitigating potential differences in
platform engagement.
Spatial Partitioning [38] is a heuristic to select an optimal group of applicants 𝜎 from screening
tests, with the additional difficulty that sensitive attribute values are unknown during testing. First,
two estimators for the target (𝑓soft(𝑥)) and protected variable (ℎsoft(𝑥)) are developed on a training
set. These estimators are applied to the test set, which is ranked customarily as 𝜏 = argsort(𝑓soft(𝑥)).
The top candidates are selected from the ranking and put into 𝜎. Given the systematic groupwise
differences encoded in the data, the selected candidates tend to be mostly from the privileged
group. Spatial Partitioning mitigates this bias by replacing the candidates in 𝜎 who have the lowest
values of [𝑓soft(𝑥) + ℎsoft(𝑥)]–or some other linear combination of the two–with the candidates
who have the highest values of [𝑓soft(𝑥) + ℎsoft(𝑥)] among the ones that were originally not chosen.
This approach aims to rebalance the privileged and disadvantaged group in the final set 𝜎 while
maintaining good accuracy in the selection of high-performance candidates.
5.4 Discussion
In this section, we present the main trends for fairness enhancement in the algorithmic hiring
literature and describe important factors guiding these choices (summarized in Table 3). Section
7 will expand on this analysis presenting additional dimensions that guide fairness mitigation in
practice.
Mitigating biases. Some of the proposed approaches are suited to mitigate specific biases described
in Section 3. Balanced sampling, for example, can counter the effect of under-representation in
training sets caused by factors such as horizontal and vertical job segregation. Proxy reduction
methods (e.g. decorrelation, adversarial inference) target sensitive attribute proxies, reducing the
overreliance of models on sensitive information. Group norming seems applicable to counter
systematic biases encoded in input features against protected groups, such as biased employee
evaluations. However, it is certainly preferable to understand and improve the measurement system
that provides these biased features rather than simply matching the distribution of input features
across protected groups without a clear understanding of the underlying socio-technical system.
Finally, output re-ranking can mitigate the joint effect of different bias conducive factors. Its
application comes with risks and opportunities described below.
Opportunities and risks of post-processing. Post-processing approaches, such as DetGreedy,
are the easiest to integrate into existing systems, as they can be modularly added to algorithmic
pipelines [257]. Indeed, most post-processing methods in algorithmic hiring are proposed and
deployed at LinkedIn, a large company with an established platform powered by interactions
between complex data infrastructure and interdependent algorithmic modules [12, 104]. It is worth
noting that post-processing explicitly takes into account sensitive attributes to change algorithmic
outcomes for job candidates, which may be critical for disparate treatment and affirmative action
(US) as well as direct discrimination and positive action (EU) [22, 112]. Additionally, postprocessing
requires run-time access to the sensitive attributes of all data subjects, as described in the next
paragraph. These are likely two key factors explaining why post-processing is less popular and
why hybrid approaches combining different types of fairness interventions, e.g. mitigating via preand post-processing, remain under-explored [11].
Sensitive data. Different mitigation strategies have different requirements for sensitive attributes
𝑠. Post-processing methods, such as DetGreedy and CDF restoring, typically require knowledge
of sensitive attributes during runtime. Conversely, pre-processing and in-processing approaches,
such as importance-based scraping and adversarial inference, require access to sensitive attributes
only during training, not testing. Furthermore, specific data modalities, such as text and vision,
facilitate specialized methods like subspace projection and face decorrelation, which function
without sensitive attribute information about data subjects. Each of these methods has distinct data
requirements, ranging from highly restrictive to more lenient. Having access to sensitive attributes
at runtime enables precise and reliable interventions, whereas strategies that do not rely on this
data must be continuously monitored to ensure they are meeting their intended goals.
Outcome fairness through proxy reduction? A very clear trend in the literature is the popularity
of proxy reduction methods, such as adversarial inference, that target process fairness (sAUC) in
pursuit of outcome fairness (e.g. DI, TPRD). This approach probably gained popularity because
it aligns with legislation against disparate treatment (US) and direct discrimination (EU), which
prohibit basing hiring decisions on protected attributes [2, 158] and because it does not require
run-time access to sensitive attributes. This approach is also adopted by vendors, such as Pymetrics
and Hirevue, upon detecting violations of the 80% rule in pre-deployment audits [124, 209]. While
this method can mitigate large outcome disparities, it does not produce convincing improvements
when the inequity is less significant [33, 119, 120]. Moreover, it is worth noting that, in contrast to
post-processing, this approach achieves mitigation on a held-out test set during development, but
provides no guarantee at deployment. More general studies are required to understand the effects
of proxy removal on outcome fairness and ensure actual benefits for vulnerable candidates.
The problem with videos. Algorithmic screening can take advantage of data from multiple sources,
including gameplay, psychological assessments, and video interviews. The latter provide three
types of signals, namely visual, verbal, and paraverbal. Across multiple studies, systems trained
on video signals are shown to yield the largest disparities and disadvantages for protected groups
[33, 120, 276]. Visual signals have been removed from several products [175] because they inevitably
encode sensitive information such as race and gender while lacking a solid foundation to justify
their use in the hiring domain. Even if found to be accurate and fair in a specific evaluation, hiring
algorithms based on face analysis are unlikely to predictably generalize and maintain accuracy or
fairness under variable conditions, or at least they are less likely to do so than algorithms based
on more established data modalities and better-understood correlations with job performance.
Furthermore, it is worth noting regulation proposals against inference of emotions, states of mind,
or intentions from face images in the workplace [84, 85]. Given this evidence, we invite particular
caution against new proposals of hiring systems based on computer vision, advertised as capable
of inferring the motivation [139] and personality traits [183] of candidates, even if accompanied by
bias mitigation and fairness evaluation.
6 DATA
Datasets used in algorithmic fairness research for the hiring domain are summarized in Table 4.
The following sections present these resources divided into textual, visual, and tabular datasets. In
line with recent literature, we find no graph dataset on algorithmic hiring [46, 71].
6.1 Text-based datasets
Textual datasets consist of job descriptions and job seekers’ resumes or biographies, focusing on
professional experience, training, and skills. Resumes and biographies contain strong proxies for
sensitive attributes such as race and gender, including names and addresses.
Chinese Bios is a textual dataset generated by Zhang et al. [283] to study gender bias in
candidate rankings produced by BERT-based resume retrieval systems [70]. It consists of short
resumes containing a binary gender indicator (he/she) and a two-sentence description of job skills
for IT, finance, and administration.
Bias in Bios, [63] is composed of textual biographies written in English and extracted from the
Common Crawl dataset. It was initially proposed to study fairness in occupation classification.
Gender is automatically extracted based on the use of pronouns in the short biographies. Professions
are the target variables; they are self-reported in the descriptions.
Engineers & Scientists [58] results from a field study comparing human and algorithmic CV
screening in an unspecified company. It is composed of applications, i.e. pairs of resumes and
job postings for engineers (software and hardware) and technical scientists. The features were
parsed from resumes, including candidate education (institutions, degrees, majors, awards), work
experience (job titles and companies), skills, and relevant keywords. The target variable indicates
whether the candidates were interviewed and extended an offer.
IT Resumes [196] was used to study how men and women describe themselves on resumes
and whether the difference impacts hiring outcomes. The dataset comprises approximately 900,000
resumes (without names, emails, and URLs) in the historical hiring records of eight IT firms based
in the US, relevant to just over 6,000 job postings from the IT sector. The resumes were managed
through an applicant tracking system, where the applicants self-reported their gender. The target
variable encodes whether candidates received a callback after applying.
CVs from Singapore [69] was introduced to investigate ethnicity bias in automated resume
filtering. It contains 135 resumes of candidates of Chinese, Malaysian, and Indian origin (the
predominant ethnic groups in Singapore) who applied for vacancies in Singapore’s accounting
and finance sectors. The dataset curators annotated candidate ethnicity based on geographical
information on their education and early employment. For example, candidates who completed
their education in China were classified as ethnically Chinese. Nine job postings describing open
positions in the financial sector are considered. Three annotators annotated each posting-resume
pair with a binary variable indicating whether candidates appear qualified for a job based on their
CV.
DPG Resumes [222] contains over 10 million vacancies (including salary range, working hours,
and job descriptions) and just under 1 million resumes augmented with job categories of interest
and gender inferred from first names. Given the imbalance between vacancies and candidates, this
dataset is suitable for studying recommender systems that propose jobs to candidates. The data
is provided by DPG Recruitment in anonymized form, removing all names (including company
names), dates, addresses, telephone numbers, email addresses, and websites.
6.2 Visual datasets
Several datasets in the hiring space are multimodal, with a strong focus on videos of candidates
answering job interview questions in front of a camera [33, 139, 231], often called Automated Video
Interviews (AVI). This data modality is relatively new in the hiring domain. Similarly to CVs, AVIs
encode much information on sensitive attributes, including gender, race, age, and disability.
ChaLearn First Impression [79] contains 10,000 YouTube video clips of people facing a camera
and speaking in English. Amazon Mechanical Turk workers were hired to annotate each clip with
the personality traits of the speaker (openness, conscientiousness, extroversion, agreeableness,
neuroticism) and a “variable indicating whether the subject should be invited to a job interview or
not”. The gender and ethnicity of the speakers were annotated by two dataset curators.
Student Interviews [33] consists of video interviews with 733 upper-level undergraduate students, who were asked to participate in a simulated interview answering six questions. Verbal (e.g.,
n-gram frequencies), paraverbal (e.g., loudness, jitter, shimmer), and visual (e.g. facial expressions,
body motion) features were automatically extracted from videos using tools like OpenSmile [88],
FACET [238], or Motion Tracker [270]. Data were annotated by three research assistants who
assessed the candidates’ “hireability” on a 5-point Likert scale. Gender is self-reported, including a
non-binary option.
SHL Interviews [231] is a proprietary AVI dataset with more than 5,000 videos from 810 real
job seekers from the US, UK, India, and Europe answering behavioral and domain knowledge
questions. Videos were annotated by at least five assessors, who rated the presence of four social
skills: engagement, positive emotion, calmness, and confidence, using a scale of 0 to 4. The sensitive
attributes available with the dataset are country, age, gender, and race.
Oil Company Interviews [139] was curated to study the problem of predicting candidate
motivation in job selection processes. It comprises AVIs with 154 students from Utrecht University
carrying out a mock interview with a fictitious oil company. The participants self-reported their
motivation (“To what degree are you motivated to work for the company”) on a 10-point Likert scale,
which represents the target variable. Software tools like OpenFace and EMFACS [75] were used to
automatically create facial marker features and extract emotions from videos.
FairCVs [199] is a synthetic CV dataset combining short bios from Bias in bios [63], face images
taken from the DiveFace database [180], and numerical features emulating desirable aspects such
as availability or previous experience. Artificial target scores are generated for each CV, as a linear
combination of numerical features; biased scores are derived from these with an ethnicity- and
gender-dependent additive penalty emulating biases in the data. The dataset has been employed to
study the extent to which sensitive attribute proxies can contribute to discriminatory models when
the target variables on which they are trained exhibit biases against certain protected groups.
6.3 Tabular data
Tabular datasets encode structured data of a diverse nature, describing job-seekers and employees
at different stages of the algorithmic hiring pipeline.
Requirements and Candidates [172] is a synthetic dataset with numerical and boolean values
encoding both candidate skills and job requirements. Bias against certain candidates is deliberately
introduced in the data through additive noise.
Jobs and Candidates [11] is a tabular dataset describing candidates and job postings with realvalued, categorical, and binary features. For candidates, their education, experience, preferences
(minimum salary, preferred working hours, maximum travel distance), and self-reported gender are
included. Regarding job postings, the dataset contains information about the industry, company size,
and geographical location. Joint candidate-job features describing overlaps, such as the distance
of candidates’ residence from the place of work, are also present. The target variable indicates
whether a candidate was recruited or short-listed for a job.
Pymetrics Bias Group [271] is a test set used for pre-deployment audits at Pymetrics, a
company offering gameplay-based screening tools to clients. The gameplay of job seekers and
current employees of the client company are compared to find candidates who resemble highperforming incumbent employees. The covariates consist of gamified psychological measurements;
sensitive attributes, which can be self-reported on a voluntary basis, include gender and race.
IBM HR Analytics1
is a synthetic dataset curated by IBM data scientists to study employee
resignation, which is the target variable. Covariates include education, job satisfaction, income,
years of service in the company, and commuting distance, along with sensitive attributes such as
gender, age, and marital status.
Resume Search Engines [48] includes search results crawled from employment websites Indeed,
Monster, and CareerBuilder for 35 job titles in 20 cities of the US, collecting data on 855,000 job
candidates. Data were crawled in 2016 to study gender biases.
Walmart Employees was released as part of the Society for Industrial and Organizational
Psychology machine learning competition2
to study the problem of predicting employee retention
and performance from pre-employment tests with questions on work history, personality, and
behavioral scenarios. Target variables encode employee tenure and performance ratings. Each
instance has a synthetic binary variable that mimics a protected attribute.
Web Developers Field Study [13] summarizes the results of an experiment on the impact of
algorithmic hiring tools on gender diversity. The curators advertised a web developer position for
US residents; upon applying, candidates provided information on their education, experience, and
demographics, as well as free-form responses to selected questions. The responses were rated using
a recruitment tool with a score of up to 100. Each applicant was then rated by a human assessor
based on experience and education; assessors were divided into three groups based on whether
they had access to algorithmic scores and candidate names.
Chinese Job Recommendations [282] consists of job recommendations from four Chinese
boards to fictitious profiles that differ only by gender. Profiles are accessed programmatically every
two weeks to record job recommendations, which are then compared between different genders.
Several tabular datasets have been curated to measure discrimination in job ad delivery [4, 132,
158], using a common methodology. Facebook Ads Audiences [4] exemplifies this methodology by
running a job ad campaign on Facebook and studying differential delivery along gendered and racial
lines. They design advertising creatives (headline, text, and image) for different professions, using
them in a campaign that optimizes clicks, which are then broken down into different demographics.
Despite the fact that the Facebook Marketing API does not allow a breakdown by race, the curators
perform this analysis with a careful design of target audiences leveraging phone numbers and
racial information available from North Carolina voter records.
6.4 Discussion
Low diversity. English is by far the dominant language; datasets with geographical information
primarily represent US citizens (6 datasets) and the Netherlands (3 datasets). We offer two interpretations of these findings. On the one hand, they reflect the importance of both countries in the
recruitment industry.3 On the other hand, they are consistent with previous research reporting
that most efforts to improve fairness in artificial intelligence are influenced by the Global North
[187, 221], particularly the US [135], and focus on English language resources [210].
Missing stages. The vast majority of datasets describe the early stages of the hiring pipeline, i.e.
sourcing (11 out of 20) and screening (8 out of 20). We found no datasets (and consequently no
studies) for selection, and only one for evaluation (IBM HR Analytics). This is expected given the
industry’s tendency to use algorithms primarily for sourcing and screening [125, 166]. However,
given the growing push to adopt this technology in later stages [259], there is a tangible risk that
algorithms for selection and evaluation will be quietly deployed without a clear understanding
of risks and limitations. Indeed, datasets that target employee tenure and performance, such as
Walmart Employees and IBM HR Analytics, signal an interest from companies in understanding the
factors that predict future productivity and loyalty.
Lacking sensitive attributes. Most importantly, attributes such as disability, religion, and
sexual orientation are simply missing, despite the special legal status of these attributes and the
evidence of workplace discrimination [7, 191, 193]. Gender is by far the most common sensitive
attribute, overwhelmingly encoded as binary. Ethnicity and race are considered in 6 out of 20
datasets, making this the second most common attribute. They are frequently annotated, rather
than self-reported, in textual and visual datasets, due to these data modalities carrying strong
proxies for sensitive attributes.
Target multiplicity. HR management and recruitment tasks allow multiple formulations. Many
target variables can seem reasonable at face value; therefore, initial data curation and design choices
have a prominent role. As candidates move through the hiring pipeline, their digital record goes
through a data journey where they are marked as aware of a position, applying (or headhunted),
proposed to a client, screened-in, interviewed, hired, retained, promoted, and so on. Companies
interested in algorithmic hiring solutions pick one or more of these variables, balancing different
priorities such as efficiency and quality of hire, with unpredictable effects on algorithmic fairness,
a phenomenon called multi-target multiplicity [266]. Indeed, the target variables in Table 4 are
very diverse. On the one hand, this reflects the length of hiring pipelines and the diversity of
data journeys. On the other hand, it points to a lack of established best practices around target
variables. Focusing on screening datasets, we find different constructs (e.g. communication skills
vs. commitment) annotated by people with different competencies (AMT workers vs. experts) from
disparate data sources (YouTube videos vs. mock interviews). Since the validity of these estimates
and their connection with job performance has been called into question [19, 214], we call for
caution in handling these variables and granting them the status of ground truth. This can be
especially problematic when using conditional fairness measures whose very definition hinges on
this so-called ground truth.
7 MEASUREMENT AND MITIGATION IN PRACTICE
In this section, we present practical considerations on bias mitigation and measurement that emerge
from our review and from direct involvement in the industry. We focus on key technical factors
guiding measurement and mitigation choices.
7.1 Data modalities
First, different data modalities enable different bias mitigation strategies.
Textual data is a common data modality encountered in the sourcing stage, typically in the form
of textual CV or job description data, or in the screening stage, e.g. transcripts of video interviews.
Common bias mitigation methods that cater exclusively to textual data include rule-based scraping
or dictionary-based methods. These methods, also offered by vendors such as Textmetrics and
Textio, can be used for mitigating specific types of biases, e.g., age bias in job descriptions [98], or
gender bias in biographies [63]. These mitigation strategies tend to be technically straightforward
to implement, as they can be developed as standalone components and need not be integrated in
complex algorithmic hiring pipelines. In addition, collecting the required data (e.g. constructing
task-specific dictionaries) leans heavily on domain and context-specific knowledge, which is
typically available to practitioners in the HR domain. A drawback of these dictionary-based methods
is a different side of the same coin: due to reliance on domain, context, and task-specific data
(dictionaries) they do not transfer well over different problems (e.g., scraping gendered words
from resumes vs. substituting words associated with age discrimination in job descriptions require
wholly different sets of terms), languages, or geographies (where cultural or regulatory differences
may impose different requirements).
Additionally, when it comes to textual bias mitigation, the rapid uptake of LLMs has pulled into
focus biases that arise from LLM-based natural language generation. For example, Salinas et al. [224]
show how LLMs exhibit gender and nationality bias when generating job recommendations for job
seekers of different genders and nationalities. They find that the types of jobs recommended follow
common gender and nationality-based stereotypes. In a similar experiment, GPT-4 is found to morefrequently use female pronouns in reference letters generated for female-dominated occupations
(such as nannies), and male pronouns for male-dominated occupations (such as plumbers) [35]. A
simple yet effective mitigation strategy here is prompt engineering: by appending the phrase “in
an inclusive way” to the prompt, previously gendered pronouns are replaced with third person
pronouns (“they/their”). While novel bias mitigation strategies for LLMs are actively studied [167],
the previous examples show that being mindful of which information to include in a prompt (either
explicit or implicit), and understanding how to effectively construct prompts are important first
mitigation steps for leveraging LLMs in the context of algorithmic hiring.
Next, visual data, either through images or video, enable and require a different set of bias
mitigation methods and strategies. As shown in Section 5, video-based systems tend to yield more
disadvantageous effects for protected groups, also due to the strong encoding of sensitive information. In this light, EASYRECRUE present an adversarial method that removes sensitive information
from latent representations of neural networks that were trained for predicting ‘hireability’ given
(features that represent) facial expressions of candidates in job interviews [120]. This type of adversarial bias mitigation can, however, be applied over a wider set of data modalities. In the end, due
to video-based algorithms unreliability in the face of varying conditions, and incoming regulation
proposals that prohibit inference of emotions or intentions from facial data in workplace contexts
(discussed in more detail in Section 5.4), it is advisable for practitioners to approach video-based
hiring systems and tools with caution, irrespective of which mitigation strategy to choose.
Finally, tabular data is a common data modality in algorithmic hiring and machine learning
more broadly. Mitigating bias in tabular data can be done through pre-processing approaches
that directly intervene on the features, e.g. by removing features that are highly correlated with
sensitive attributes via importance-based scraping, or increasing the representation of vulnerable
populations in training sets with balanced sampling. These types of methods are widely available
in open-source bias mitigation software packages such as the Fairlearn Python package [268]
or the AI Fairness 360 toolkit (available in Python and R) [21]. In addition, we see practitioners
experiment with alternative pre-processing methods in algorithmic hiring, such as synthetic tabular
data generation [197] for measuring [256] and mitigating bias [11].
7.2 Tasks
Next to different types of data modalities, different downstream tasks can enable and call for
different measurement and bias mitigation strategies. The two most common tasks in algorithmic
hiring are classification and ranking.
For classification tasks, getting started with bias mitigation is relatively straightforward, as
there exist several open source or otherwise freely available software packages and libraries,
as mentioned above, that provide different implementations of bias measurement methods and
mitigation algorithms, specifically designed for classification tasks.
Ranking is a common task in the sourcing and screening stages of hiring, performed by search
engines or recommender systems. However, the prevalence of classification-based bias metrics in
algorithmic hiring (discussed in more detail in Section 4) is reflected in the aforementioned open
source packages, which means that measuring and mitigating bias in ranking systems tends to
follow the practice of re-purposing classification methods through, e.g., thresholding rankings
(i.e., cutting off at 𝑘). We recommend using fair ranking measures for an evaluation of ranking
systems that is more cognizant of user browsing behavior, although, of course, the latter needs to
be suitably modeled. While several mitigation methods apply to both classification and ranking
tasks (e.g. adversarial inference), practitioners should be aware of ranking-specific methods such
as DetGreedy.
7.3 Scalability and efficiency
Technical and infrastructural decisions further affect which bias mitigation methods to consider.
For example, Geyik et al. [103] decouple their post-processing method from specific model choices
and properties of input data, which means their method can naturally scale across the different
(ranking) systems at LinkedIn. This also means that such a method can be developed and deployed as
a standalone component or micro-service, which decreases development time, effort, and alignment,
when compared to pre-processing or in-processing methods that may need to be designed and
integrated in complex algorithmic hiring pipelines. In general, post-processing approaches offer
an advantage in terms of system integration, but they should be applied with care due to antidiscrimination law (Section 8).
In terms of algorithmic efficiency, Geyik et al. [103]’s re-ranking method for bias mitigation can
be considered computationally cheap as only a subset of a model’s output needs to be processed (i.e.,
top-𝑘 items). At the same time, while low, the additional computational costs will be incurred for each
ranker output. Bias mitigation through pre-processing, such as counterfactual data augmentation,
and in-processing, such as feature weighting, can be comparatively more resource intensive as they
involve (re-)training models. Adversarial inference methods, which have been applied to a variety
of data modalities and tasks, even require training multiple neural networks simultaneously, which
means they can incur substantially higher costs compared to their non-mitigated counterparts.
However, while these additional costs may be incurred at training time, the resulting models do not
incur additional costs at inference time. In the end, algorithmic efficiency and computational costs
will vary across bias mitigation methods in nature and magnitude, with simple rule-based scraping
methods that involve dictionary look-ups on the cheap end of the spectrum, and bias mitigation
methods that involve re-training LLMs at the resource-intensive end [167]. Aspects such as task,
model complexity, architecture, training parameters, dataset size, and composition influence the
scalability and efficiency of bias mitigation strategies.
7.4 Sensitive attribute data availability and usage
Different bias mitigation methods have different requirements around the availability of sensitive
data, which can further steer mitigation method selection.
The availability of sensitive data is affected by several factors in practice. First, as we identify in
Section 8, access to sensitive attributes may be at odds with privacy regulations such as the GDPR,
which is an important real-world constraint. Next, availability of and access to sensitive attributes
may require job seekers’ explicit consent, which can be difficult to acquire at the scale needed for
some bias mitigation methods. Finally, some sensitive attributes, such as age and gender, may have
to be recorded in the hiring process for identification purposes, and can hence be assumed to be
available for all job seekers. Many other sensitive attributes (e.g., religious beliefs) will not be easily
available, and will have to be explicitly requested for bias measurement and mitigation purposes.
This lack of access to sensitive attributes means some bias mitigation methods may be less suited
than others, as noted in Section 5.4; in particular, post-processing methods that require sensitive
attributes for all candidates at inference time can be unrealistic. Here, pre-processing bias mitigation
methods may prove more useful, as they (only) require access to sensitive attributes at training time,
and can operate on attributes even when available for only a subset of job seekers (e.g., those who
provided consent). Furthermore, this allows these methods to be deployed and run in isolation from
production systems in controlled batch scenarios, which can be another important practical benefit.
Examples of these bias mitigation methods used by practitioners include adversarial inference [222],
and re-balancing training data with synthetic data generation [11].
Finally, a third family of bias mitigation methods that can operate without requiring access to
sensitive attributes at all are the rule-based approaches described above, which are commonly used
for mitigating bias in textual data such as job descriptions or resumes. These methods rely solely on
domain and task-specific gazetteers or dictionaries, and hence can be used when access to sensitive
attributes of individuals is not available or desirable.
7.5 Fairness definitions and intervention targets
Once data modality, task, infrastructural and technical choices, and access to sensitive data are set,
one important practical challenge is that of defining “fairness” and formulating the intervention
target of a bias mitigation method–i.e. deciding “when to intervene” and “what to optimize for”.
In the case of LinkedIn’s Talent Search [103], the DetGreedy algorithm was implemented to have
the ranker’s top-𝑘 output reflect the gender distribution of job seekers that meet the requirements
of a recruiter-issued query, i.e. the desired distribution of the ranking is set to be equivalent
to that of the underlying population of job seekers. Here, alignment with the company’s goals
and values, interpretability (or ability to explain), and collaboration across different stakeholders
were mentioned as key factors in guiding the eventual target distribution. Defining fairness and
formulating an intervention target is not a one-off task, as algorithmic hiring components will be
deployed in different, product-specific contexts and stages of the hiring pipeline. Candela et al. [39]
present the (evolving) framework used at LinkedIn that guides definitions and operationalizations
of AI fairness across their different (types of) products.
In general, the challenge in defining fairness and formulating intervention targets in algorithmic
hiring is exacerbated by the multi-stakeholder nature of the hiring domain, where development
teams may need to consult legal and compliance teams, HR professionals and recruiters, product
managers, and executives, all of whom may need to be informed or provide input. Indeed, these
choices should be guided by ethical, social, and legal dimensions. This challenge may explain in
part the popularity of disparate impact as a fairness metric, due to its ease of interpretation across a
broad and diverse stakeholder group, or the popularity of complying with the EEOC’s 80% rule [77]
as a fairness target (adopted e.g. by Pymetrics [271]), as it appears, at least superficially, a legally
grounded target.
7.6 Fairness vs. utility trade-offs
In the sourcing or screening stages, depending on the intervention target, outcome fairness may
come at the cost of utility; this can happen, for example, when optimizing for gender parity in
heavily male or female-dominated industries. However, perhaps surprisingly, different experiments
by practitioners show that outcome fairness does not need to come at the cost of utility. First, in
their online A/B-testing experiments, Geyik et al. [103] find their DetGreedy method improves
their fairness metric, with no significant impact on utility. In addition, Arafan et al. [11] find that
their pre-processing mitigation method of rebalancing training data may even improve utility over
non-bias-mitigated methods, in an offline experiment using real data from an international HR
company. Moreover, with respect to impact fairness, Peng et al. [200] show that “overcompensation”
(i.e., artificially over-representing a gender in the output of a ranking system) as an intervention
strategy for a hiring algorithm can in some cases mitigate human bias further down the hiring
funnel. Overall, this section described several practical considerations constraining bias mitigation
interventions; desired utility levels are just one dimension, and often not the most restrictive.
8 LEGAL LANDSCAPE
In this section, we describe the main regulations and non-discrimination provisions concerning
algorithmic hiring in the EU and the US. We list the main legal sources in both regions, emphasizing
the former since it is less cited in the computer science literature on algorithmic hiring. We close this
section with remarks on open challenges and practical concerns at the intersection of technology
and policy.
8.1 European law
Non-discrimination law. We focus on rules that apply in the whole European Union (27 Member
States). In the absence of specific legal rules on non-discrimination in algorithmic hiring, general
non-discrimination law applies. The right to non-discrimination is protected as a human right in
Europe by the European Convention on Human Rights (1950) and the Charter of Fundamental
Rights of the European Union (2020). The EU also adopted a number of legal acts called directives,
prohibiting several types of discrimination in different contexts, which Member States implement
(give effect to) by adopting national law [153]. The four most relevant non-discrimination directives
are the following: the Racial Equality Directive (2000), the Employment Equality Directive (2000),
the Gender Goods and Services Directive (2004), and the Recast Gender Equality Directive (2006)
[54–56, 86]. Together, the directives offer protection against discrimination in hiring on the basis
of six grounds, also called protected characteristics, or protected attributes: age; disability; gender;
religion or belief; racial or ethnic origin; and sexual orientation. EU law distinguishes two categories
of prohibited discrimination: direct and indirect.
Direct discrimination means that the person is treated less favorably than another on the basis of
a protected characteristic, such as ethnicity [54]. For example, if a company says it will not recruit
people of a certain ethnicity, that is an example of direct discrimination [57]. Direct discrimination
is always prohibited, with a few narrowly defined and specific examples. For instance, a women’s
clothing brand is allowed to hire only female models for its advertising pictures.
The second category of prohibited discrimination is indirect discrimination, occurring when a
practice is neutral at first glance but ends up discriminating against people of a certain ethnicity (or
another protected characteristic) [54]. For indirect discrimination, the law focuses on the effects of
a practice; the intention of the alleged discriminator is not relevant. Hence, even if an organization
can prove that it did not know that its algorithmic system discriminated unfairly, that will not help
the organization.
There are three elements of indirect discrimination that can be summarized as follows [34, 54]. (1)
The practice must be neutral. For example, rejecting job applications coming from a certain postal
code would count as neutral. Rejecting applications from people with a certain ethnicity would not
be neutral; it would be direct discrimination. (2) This neutral practice puts people with a certain
ethnicity (or other sensitive attributes) at a “particular disadvantage compared with other persons”.
The word disadvantage must be interpreted in a wide way. (3) There is no objective justification
for such practice. The apparently neutral practice is not prohibited if the “practice is objectively
justified by a legitimate aim and the means of achieving that aim are appropriate and necessary”.
As a hypothetical example, suppose that people with an immigrant background make more
spelling errors in job application letters. A cleaning company never hires job applicants for cleaning
jobs if the application contains spelling errors. This practice seems neutral at first glance, but
results in the rejection of most applicants with an immigrant background. The cleaning company
cannot justify this no-spelling-errors rule because people can be good cleaners, even if they make
some spelling errors. Therefore, the cleaning company engages in illegal indirect discrimination.
However, the situation would be different for a law firm. The main job of many lawyers is writing
precise, and often official, documents. The law firm is allowed to reject applications with spelling
errors, even if it results in most people with an immigrant background not being hired.
The organization is also responsible if it uses an algorithmic system provided by, for instance, a
company. If the algorithmic system turns out to discriminate illegally, the organization using the
system is responsible and the victim can sue it for damages, for instance. (Later, the organization
could try to sue the AI developer, but the organization remains responsible towards the victim.) In
sum, general non-discrimination law applies to new forms of algorithmic discrimination, also if
that discrimination happens indirectly or accidentally.
Other relevant law. We briefly highlight some other relevant laws in the EU. The GDPR (the General
Data Protection Regulation) is, roughly summarized, a European-wide statute that aims to protect
fairness and human rights when personal data are used. The GDPR is long and detailed. Among
other things, GDPR bans the use of special categories of personal data (sometimes called sensitive
data). These are data on, for example, someone’s ethnicity, religion, trade union membership, health,
or sexual orientation (article 9 GDPR). There are some exceptions to the ban. For instance, hospitals
are allowed to use health data. Another exception is the individual’s explicit consent. Generally
speaking, consent is not freely given, and thus not valid, if an employer asks a job applicant or
employee for their consent, because of the unequal power relation. This GDPR rule makes it difficult
to use sensitive data to audit or train algorithmic systems [254].
There is a proposal for an AI Act in the EU, with many requirements for “high-risk” systems,
including algorithmic systems for HR [84]. Developers of high-risk AI systems must, for instance,
ensure that the training data are appropriate and do not lead to unlawful discrimination. At the
time of writing, the EU did not officially adopt the AI Act yet, and did not publish the final text
yet. The proposals in the AI Act also contain a new exception to the GDPR, to enable the use of
sensitive data for debiasing algorithmic systems.
8.2 US law
Federal law. US non-discrimination law is similar to EU law in many respects, but also decidedly
different in others. Like EU law, its sources are spread over different statutes, and case law plays
a crucial role. For example, Title VII of the Civil Rights Act of 1964 constitutes a federal law
prohibiting employment discrimination based on race, color, religion, sex, and national origin.
Significantly, the Equal Employment Opportunity Commission (EEOC) issues nonbinding, but
practically important guidelines to interpret Title VII. Other important sources of federal law are
the Age Discrimination in Employment Act of 1967, the Americans with Disabilities Act of 1990,
and the Genetic Information Nondiscrimination Act of 2008.
For all these acts, US law distinguishes between two fundamental types of discrimination:
disparate treatment and disparate impact. They resemble, but do not perfectly mirror, the difference
between direct and indirect discrimination in the EU. Importantly, disparate treatment requires not
only an adverse action based on a protected attribute, but also the proof of intent on the part of
the discriminating individual – unlike the EU variety of direct discrimination [254]. To actually
win in court, an injured person in the spelling mistake example would have to demonstrate that
the cleaning agency introduced the spelling requirement with the purpose of treating unfavorably
members of their protected group. In practice, this will often be difficult [251].
Disparate impact, in turn, closely resembles indirect discrimination. Intent is not required [249].
Rather, the disparate impact doctrine prohibits actions that are seemingly neutral, but significantly
disadvantage members of a protected group. In its guidelines, the EEOC suggested that such a
disadvantage usually occurs if the chance of a member of the protected group being positively
evaluated is 80% or less than that of a member of the privileged group (so-called 80% rule or
4/5 rule) [77]. Finally, disparate impact can be justified if there is a legitimate reason for the
practice [250], for example business necessity [18, 249]. Therefore, a law firm could arguably use
a model evaluating orthography and grammar to rank candidates even if this disproportionately
disadvantages members of one specific protected group.
Overall, unless intent can be shown, many cases of algorithmic discrimination will be argued
under the disparate impact prong. Therefore, many contributions to the literature on technical
algorithmic fairness have provided tools to ensure that this rule is not violated at the statistical level
[94, 278, 279]. However, courts will generally, both in the EU and in the US, look at factors beyond
mere scores and numbers to determine whether a legally relevant disadvantage exists [112, 260].
Other relevant law. Apart from the acts mentioned, federal legislation specifically addressing discrimination in AI systems is unlikely to emerge anytime soon. The Algorithmic Accountability
Act is stalled in a gridlocked Congress. Hence, several states and municipalities have taken the
initiative and enacted AI hiring laws themselves. For example, the city of New York passed a law
on automated employment decision tools [186]. From July 5, 2023, NYC Local Law 144 applies
to employers using AI to substantially assist or replace discretionary decision-making in hiring.
They are required to conduct and publish impartial bias evaluations by an independent auditor.
Furthermore, the state of Illinois enacted the AI Video Interview Act [131]. In force since the year
2020, the law requires employers to put candidates on notice, and obtain their consent, before
subjecting their video interview to AI analysis. Candidates may request deletion, and employers
that rely solely on AI need to collect and report candidates’ race and ethnicity.
Practitioners have to comply with these local rules if their model is applied in these jurisdictions.
Finally, further constraints may arise from affirmative action law, particularly if the fairness
intervention goes beyond what is necessary to remedy otherwise unjustified discrimination; this is
a complex topic in both the US [22, 145, 252] and the EU legal framework [112, 126].
8.3 Operational challenges
This outline of the EU and US legal landscapes provides some normative reference points for
practitioners and offers an opportunity to discuss some practical challenges in assessing the legal
compliance of algorithms.
In general terms, an algorithmic system does not cause indirect discrimination or disparate
impact if it pursues legitimate aims through appropriate means. In practice, several questions arise
about both elements at the base of this legal principle. Is inferring a candidate’s motivation, i.e. an
internal combination of their emotions, states of mind, and intentions, a legitimate aim? Moreover,
should estimates by algorithms trained on biased “ground truth” variables be considered appropriate
means? In the absence of precise guidelines, these questions have to be assessed contextually to
each algorithmic system, and algorithmic implementations should be compared, to the best extent
possible, to (hypothetical) outcomes under non-algorithmic alternatives [112].
Direct discrimination, in turn, is generally much more difficult to legally justify [2]. A natural
question arises about the compliance of bias mitigation approaches embedded in hiring algorithms.
More specifically, are post-processing algorithms legitimate only if they enforce inter-group parity
for equally qualified candidates, e.g. targeting TPR parity rather than DI? If so, what quantitative
criteria should be applied to assess candidate qualifications? And to what extent is human intervention and a comprehensive assessment of any re-ranking required? Here, the answers depend
on affirmative action (US) and positive action (EU) law, which are currently in flux after the US
Supreme Court’s decision against Harvard’s and UNC’s affirmative action programs. At a minimum,
human oversight of post-processing operations, and an evaluation of its effects both on groups
and on individuals particularly worthy of protection (single parents; chronically ill persons), seems
advisable.
9 THE REAL WORLD IS MESSY
Our previous discussion has focused on how discrimination can be exacerbated by algorithms.
Nevertheless, we have striven to point out the ways such discrimination can be mitigated and even
how algorithms can be designed to actively discourage discrimination. It should now be clear that
the design of technology plays a key role, either in creating discrimination or by reducing it. To
overly value the role of technology design in discrimination or anti-discrimination would also be
a mistake, however. This is because non-technological factors have been shown, on occasion, to
strongly influence decisions and amplify technological bias, as we will explore in this section.
9.1 Algorithmic Uptake
During the COVID-19 pandemic, delivery companies such as Amazon, Deliveroo, and DoorDash
rolled out algorithmic recruitment systems to avoid the danger of viral contagion in their HR teams,
as well as experiment with a new technology that had the potential to save millions of dollars in HR
bills [281]. One reason they were able to do this with ease was due to the regulatory environment,
which was laxer than usual due to the ongoing emergency conditions. We have explored some of
the ethical problems regarding discrimination in previous sections of this article, as well as some
of the potential technological solutions to designing algorithms with anti-discrimination in mind.
Each of these solutions is a technological response, however, so we need to remain aware of the
non-technological or reduced-technological options.
Although hiring technology can be more ethical than humans and reduce bias in decision-making
[138], it often reinforces bias and results in distinctly non-ethical outcomes. This means we should
at least consider the balance of ethical harms if we reintroduced a non-technological solution. The
recent pandemic necessitated social distancing, but once this danger had passed, non-technological
hiring procedures could be reintroduced. To understand why this has not happened, we must
consider the institutional incentives of tech companies. These companies have invested heavily in
their digital hiring technology as suppliers or customers, so are highly motivated to retain it, even
once there is no longer a strong need for it.
9.2 Algorithmic Fairness
Recalling the example from Section 3.4, suppose that appropriate technical solutions have been
deployed in hiring algorithms to counter the bias conducive factors against intersectional minorities.
Should she seek a new job, JS would have a sizeable probability of being sourced, screened-in,
and recruited – equal to natives (male and non-male alike) with similar skills and experience in
the hospitality industry. However, in the presence of an exogenous shock, such as the COVID-19
pandemic, workplaces are heavily affected, with large consequences on hiring and recruitment. The
hospitality industry receives a major blow. Food services stop hiring waitstaff and dismiss most of
the employees. Schools and childcare services become unavailable. All of a sudden, JS finds herself
unemployed, urgently in need of a new job, which is now more difficult to obtain since demand for
her skills has decreased and competition has surged. Sourcing algorithms place JS at the bottom
positions of rankings, granting her low visibility. Childcare duties demand much time from her
due to her gender [227]. She has fewer connections than native job seekers for recommendation
and referral [284]. Overall, her probability of successfully reaching the end of a hiring pipeline
has dropped substantially and more sharply than for privileged groups. In addition, her migration
background makes JS less likely to gain support from social safety nets [45, 171], increasing the
urgency of her need and the unfairness of the new status quo.
This section highlights two limitations of algorithmic fairness in hiring. On the one hand, by
restricting their scope to a single system at a precise point in time, fairness measurements run the
Table 5. Opportunities, limitations, and recommendations for algorithmic hiring and fairness research.
Opportunities Limitations Recommendations
Bias &
validity
consider large candidate pools, reduce human biases, and attract
minority candidates
risk of encoding individual biases along with inevitable societal biases; invalid target variables
focus on vulnerable populations beyond acceptance rates; study individual fairness and exploratory policies; carefully scrutinize new technologies
Broader
context
trigger positive feedback loops; consider
tech-recruiter collaboration
narrow focus on local outcomes
can overlook fairness in entire
hiring process; risk of repurposing for termination
center on job seeker impacts; identify leaks in pipelines; design for
recruiter-tech interaction; beware
of performance and tenure prediction
Data support evaluations of
diversity and inclusion
reduced geographical, linguistic,
and sensitive attribute coverage
design data collection for diversity;
develop IP-friendly audits
Law apply binding regulation to positively influence industry
legal restrictions on fairness approaches: concerns about discrimination and data protection
multidisciplinary research balancing fairness, privacy, and antidiscrimination; monitor EU AI Act
risk of missing the bigger picture, i.e. the broader socio-technical system in which hiring algorithms
are embedded, which can change quickly and profoundly. A model deemed accurate and fair in the
old context may perform poorly in the new one. On the other hand, these changes may be difficult
to detect and quantify. Fairness evaluations by practitioners on pre-deployment test sets, such
as Pymetrics Bias Group (Section 6.3), may quickly become obsolete. Strong shocks in the hiring
domain are an issue for data representativeness more broadly. Fresh data becomes necessary. This
is further complicated by changing incentive structures, by the complexity of handling sensitive
data, and by the frequent delay between decisions and feedback in hiring.
10 OPPORTUNITIES AND LIMITATIONS
Algorithmic hiring benefits from, and contributes to, fairness and anti-discrimination work, as
the previous sections have shown. In this section, we summarize the emerging opportunities and
limitations, from which we derive a set of recommendations for researchers and practitioners,
summarized in Table 5.
10.1 Bias and Validity
Opportunities. Algorithms for hiring can consider large pools of candidates, avoiding the preliminary exclusion of unusual profiles, as often done by human recruiters under time constraints.
Under-representation and sampling biases can be mitigated as a result. Algorithmic hiring also has
the potential to mitigate biases in imperfect human judgments. The simple fact of using algorithmic decision-making can reduce avoidance by vulnerable candidates [13]. Fair and trustworthy
algorithms can lead to a positive form of automation bias and attract minority candidates.
Limitations. Data-driven algorithms tend to encode individual and societal biases. Some algorithms
are explicitly trained and evaluated to “predict the competency scores candidates would have been
given by trained human reviewers” [189], inheriting individual biases from recruiters. Previous
experience is a preeminent feature for assessing candidates. In conjunction with current job
segregation, this means that the most important features are inevitably skewed against historically
disadvantaged groups. In addition to these biases, the epistemic validity of prediction targets such
as candidates’ employability and motivation is questionable. Job performance is famously difficult
to define and measure, let alone predict [220, 263]. Algorithms cloaked in objectivity can promote
bias while targeting and legitimizing ill-defined quantities.
Recommendations. Attention should be devoted not only to acceptance rates for vulnerable populations (DI) but also to their representation among applicants, as well as their progress downstream
of the algorithm and post-hiring. Job descriptions and organizational communication can play an
important role in attracting or repelling specific groups; automation attempts [207] should carefully
include fairness evaluations. To mitigate biases against unusual candidates, individual fairness
and exploratory policies should be studied. Individual fairness measures can surface problematic
situations for individuals that may go unnoticed when studying group fairness. Exploratory policies
based on partially stochastic mechanisms can provide new information in repeated decision-making
scenarios. However, the social acceptability and procedural justice of such policies in the hiring
domain remain to be studied. Finally, new technologies, including AVIs and personality prediction,
deserve additional scrutiny, especially through the lens of validity theory [213, 214].
10.2 Broader Context
Opportunities. It is worth highlighting that improving fairness does not require completely removing bias. Algorithmic hiring can reduce certain disparities and trigger deflating feedback loops
across bias conducive factors. These algorithms do not (and should not) operate autonomously.
Effective and equitable hiring can result from a fruitful interaction between technology and recruiters, leveraging complementary strengths. For example, HR professionals are better suited to
assess special cases and operate under changing conditions [166].
Limitations. Most fairness measures are focused on narrow algorithmic outcomes, neglecting the
wider socio-technical context around these algorithms. Some of these measures are completely
symmetric and consider advantages for vulnerable and privileged groups as equally problematic
(which is, however, generally required by the law). Zooming out from single-algorithm evaluations,
it is worth noting that outcome fairness at every stage does not guarantee fair outcomes for job
seekers throughout the hiring pipeline. Furthermore, fairness for employers is currently missing;
two-sided platforms would be well-positioned to study the performance of their algorithms across
employers, devoting special attention to small businesses. Finally, it is worth noting that the
discovery of patterns that predict job performance for hiring can open the way to models for
termination decisions.
Recommendations. We call for contextualized and integrated evaluations of decision-making
processes that go beyond the predictions of a single algorithm. This will help to address complex
problems, such as identifying leaks in the hiring pipeline that are most critical for vulnerable groups
and modeling impacts on job seekers, such as their efforts and benefits. To exemplify, rejected
candidates may still benefit to some extent from a specific type of explanation. Moreover, it will be
important to better understand the utility derived from these algorithms by different employers,
considering recruitment workflows and developing new fairness measures. The prevalent human
vs. algorithm evaluation framework is of limited utility; to overcome it, more research on recruitermachine interaction is required [240], including candidate screening models [6] leading to more
granular measures. Finally, we invite special caution in the development of predictive models for
job performance and tenure, due to a risk of exploitation for termination decisions [285]; such an
application of algorithms raises even stronger ethical and social concerns, which are only beginning
to be discussed [223].
10.3 Data
Opportunities. Algorithmic fairness research is contributing additional analysis into hiring practices from a perspective of diversity and non-discrimination. More data entails more scrutiny and
reflection, which can inform organizational frameworks, such as Diversity, equity, and inclusion,
and scholarly fields, such as applied psychology and economics.
Limitations. Research on fairness in algorithmic hiring is based on data with reduced geographical
and linguistic coverage. In addition, important sensitive attributes are missing from the data, making
it difficult or impossible to evaluate algorithms for specific vulnerable groups. Data and research
are constrained by a dual tension with the privacy of data subjects, on one side, and the intellectual
property (IP) of companies, on the other side.
Recommendations. Practitioners and researchers should seek more diverse data, with greater
geographical and linguistic diversity, and better coverage of sensitive attributes that are relevant in
hiring but are lacking, such as disability status and sexual orientation. Dedicated initiatives should
be undertaken, including optional surveys for job applicants and broader data donation campaigns
[25]. Innovative auditing protocols should be studied for employers and providers of algorithmic
hiring solutions, including IP-friendly data disclosure procedures.
10.4 Law
Opportunities. In practice, binding regulation shapes algorithmic development more than ethical
guidelines or self-regulation. Although clear guidance on algorithmic hiring is currently missing,
precise requirements set out in future regulation and case law, informed by research and practice
on fair algorithmic hiring, have the potential to influence the industry positively and profoundly.
Limitations. Most of the fairness approaches developed so far are restricted to proxy reduction
or removal, neglecting a wealth of solutions developed by the algorithmic fairness community.
This is most likely due to concerns of infringing regulation on disparate treatment and direct
discrimination. Furthermore, special categories of personal data are often lacking and difficult
to process, particularly in the EU under the current data protection law. Therefore, it is difficult
to assess hiring practices for certain vulnerable populations. Data protection law restricts these
analyses and should consider exceptions for algorithmic fairness, as now suggested in the EU AI
Act.
Recommendations. Algorithmic fairness can conflict with privacy and non-discrimination doctrine. The exact contours of legally compliant algorithmic fairness remain contested. The EU AI
Act may offer a (limited) solution by allowing certain types of sensitive data processing to remove
biases in high-risk scenarios. This guidance should be expanded to other areas and jurisdictions.
We advocate for further multidisciplinary research on this topic, studying technical solutions and
legal frameworks to reconcile these principles in light of their trade-offs. Promising technological
approaches include multiparty computation [143], sample-level estimators [89], and noise injection
mechanisms [137].
11 CONCLUSIONS
The social, technological, and legal landscape around algorithmic hiring is rapidly evolving; algorithmic fairness has become a necessary component for both business-as-usual product development
and frontier research. Practitioners and researchers in this field must understand bias conducive
factors, leveraging contextualized measures carried out on appropriate data to deploy suitable
bias mitigation strategies. Multidisciplinary work at the intersection with legal scholarship is
especially critical to implement and guide policy by defining technically achievable desiderata.
Only a contextualized and balanced understanding of fair algorithmic hiring can guide research
and practice to avoid the pitfalls of legitimizing questionable applications with misguided analyses
and to reap truly shared benefits for society.
ACKNOWLEDGMENTS
We are indebted to many researchers and practitioners for advice on this work, including Anisha
Nadkarni, Anna Via, Carlos Castillo, Clara Rus, Didac Fortuny Almiñana, Feng Lu, Ilir Kola, Justine
Devos, Marc Serra Vidal, and Volodymyr Medentsiy.
This work is supported by the FINDHR project, Horizon Europe grant agreement ID: 101070212
and by the Alexander von Humboldt Foundation.
