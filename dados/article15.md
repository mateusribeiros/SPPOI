Title: Contract-based Validation of Conceptual Design Bugs for
Engineering Complex Machine Learning Software

ABSTRACT
Context. Modern software systems increasingly commonly contain
one or multiple machine learning (ML) components. Current development practices are generally on a trial-and-error basis, posing
a significant risk of introducing bugs. One type of bug is the “conceptual design bug,” referring to a misunderstanding between the
properties of input data and prerequisites imposed by ML algorithms (e.g., using unscaled data in a scale-sensitive algorithm).
These bugs are challenging to test at design time, causing problems
at runtime through crashes, noticeably poor model performance,
or not at all, threatening the system’s robustness and transparency.
Objective. In this work, I propose the line of research I intend to
pursue during my PhD, addressing conceptual design bugs in complex ML software from a prevention-oriented perspective. I intend
to build open-source tooling for ML engineers that can be used
to detect conceptual design bugs, enabling them to make quality
assurances about their system design’s robustness. Approach. We
need to understand conceptual bugs beyond the status quo, identifying their types, prevalence, impacts, and structural elements in
the code. We operationalize this knowledge into a tool that detects
them at design time, allowing ML engineers to resolve them before
running their code and wasting resources. We anticipate this tool
will leverage contract-based validation applied to partial ML software models. Evaluation. We plan to evaluate the built tool two-fold
using professional (industrial) ML software. First, we will study its
effectiveness regarding bug detection at design time, identifying
whether it fulfills its functional objective. Second, we will study its
usability, identifying whether ML engineers benefit when tools like
this are introduced into their ML engineering workflow.
CCS CONCEPTS
• Software and its engineering → Software design engineering; Software testing and debugging; • General and reference
→ Empirical studies; Verification; • Computing methodologies → Machine learning.
KEYWORDS
Machine Learning, Software Bugs, Software Design, Knowledge
Mining, Software Contracts, Empirical Software Engineering.
1 INTRODUCTION
Machine learning (ML) software components are increasingly commonly deployed in modern software systems, being applied in many
domains from healthcare to the automotive industry [73]. Where
traditional software comprises manually written program logic,
ML software is predominantly data-driven, automatically inferring
logic by seeking patterns in large amounts of data. Although the
final product of this process is an opaque model, the engineering
process to build ML models still involves writing traditional code;
commonly using Python notebooks [26].
The quality of a ML model is typically measured by observing
the final product’s performance. For example, by measuring its
accuracy or ROC after the model was trained [15]. These metrics
indicate how well the model identified relevant patterns in the data
and are used to update the model iteratively until a satisfactory
performance is reached. This process poses a significant challenge
to ML practitioners as many design alternatives could be used to
tackle one problem [28]. Although some heuristics exist to speed up
this process [3, 28], designing robust ML software in a time-efficient
manner remains challenging.
Unsurprisingly, ML software is prone to software quality issues
like bugs (e.g., [35, 41]) or technical debt [6, 47, 57, 61, 66]. Bugs are
commonly defined as “unintended side-effects of software,” which
can cause ML software to crash, run indefinitely, or output incorrect
results [31, 41, 78]. Although bugs are problematic in any software
type, they are especially troublesome in ML software as training
models is an inherently slow process due to the large amounts of
processed data. Consequently, the effects of the bug commonly only
arise after a large amount of computation is performed, ultimately
wasting resources [29, 31, 75, 76, 78]. Recent studies addressing
the errors ML software highlighted that they are prone to various
types of bugs and span the entire engineering process from data
collection to model deployment (e.g., [30, 31]).
One type of error is a “conceptual ML design bug,” referring to
“the unintended use of practices that violate principles of good ML
design leading to undesired side-effects” (a term inspired by software
engineering research on “technical debt” [5, 36]). Some evidence
has already been found on the existence of these errors in ML
software [4, 7, 74]. An example is a scale-sensitive algorithm (e.g.,
support vector machines; see Section 2) applied to an unscaled
dataset. Bugs like these are especially problematic to detect as the
code will execute without visible problems, while the operation
could output incorrect results. These bugs will only be detected
if the ML engineer notices the incorrect output by observing the
results directly or investigating the reason for poor model performance. Both are highly non-trivial tasks [35, 41], giving very few
assurances about the quality of the created models.
I propose a model-based solution to detect conceptual design
errors in ML software. We anticipate this tool to leverage contractbased validation [1, 21, 50] on partial models [39] of ML software
to identify bugs in the structure of ML code as well as the selection
and tuning of ML algorithms We believe model-driven solutions can
benefit ML engineers in sectors like healthcare or the automotive
industry as they are likely to employ more model-driven solutions
to improve their systems’ robustness [42]. To verify its impact,
we propose to evaluate the created solution with professional ML
practitioners.
The rest of the paper is structured as follows. Section 2 introduces
guiding examples. Section 3 lists the expected high-level contributions. Section 4 introduces a theoretical framework on bugs in
ML software and discusses related literature. Section 5 describes
the method of approach to achieve and evaluate the research goals.
Section 6 lists risks and ethical considerations. Finally, Section 7
describes the current status of the research.
2 GUIDING EXAMPLES
To illustrate the essence of the tackled problem, we give the following simple examples using Python.
Example 1: A logistic regression classifier.
1 from sklearn . linear_model import LogisticRegression
2 import numpy as np
3 X = np. array ([[1 , 2] , [3 , np. nan] , [7 , 6]])
4 y = np. array ([0 , 1, 0])
5 model = LogisticRegression ()
6 model . fit(X, y)
From the top to the bottom, the code first imports two libraries,
defines the predictor and outcome values, X and y, and finally fits
a LogisticRegression1 model on that data. Because this code is
syntactically correct, it is easy to presume it will run successfully.
However, because one of the data points in X is not a number (i.e.,
NaN), which is not supported, the program will crash when run. In
other words, the programmer made a conceptual error regarding
the algorithm’s supported input and should add additional preprocessing steps to remove the NaN values (e.g., by removing or
imputing the value).
Example 2: A support vector machine classifier.
1 import pandas as pd
2 from sklearn . svm import SVC
3 df = pd. read_csv ('./ my_dataset . csv ')
4 X = ['x1 ', 'x2 ']
5 svm_classifier = SVC( kernel ='linear ')
6 svm_classifier . fit(df[X] , df['y'])
From the top to the bottom, the code imports used libraries, loads a
dataframe (i.e., a dataset) from a file, and creates a support vector
machine classifier (SVC2
). When run, the code will terminate successfully, suggesting it is correct again. However, this might cause
1
sklearn.linear_model.LogisticRegression: https://scikit-learn.org/1.5/modules
/generated/sklearn.linear_model.LogisticRegression.html
2
sklearn.svm.SVC: https://scikit-learn.org/1.5/modules/generated/sklearn.svm.SVC.html
the SVC model to perform poorly when the predictor features in
the dataset have substantially different scales. Although the code is
syntactically and functionally correct, it fails conceptually. A simple
solution is to add a preprocessing step that scales each feature to a
similar range (e.g., using the StandardScaler3
).
Production-level ML software is never simple due to the large
amount of data, predictor variables, model prerequisites, and possible design alternatives. This, combined with the iterative nature
of ML software development (as ML software is most commonly
built through trial-and-error) makes it very easy for practitioners
to violate conceptual prerequisites, assumptions, and best practices
of the used ML algorithms with respect to the available data.
3 EXPECTED CONTRIBUTIONS
My research aims to detect and help prevent conceptual design errors in ML software by adapting model-based analysis techniques,
thus enabling ML engineers to give some fundamental assurances
about their system’s quality. The proposed research has four overarching goals: i) identify the types of conceptual design bugs in ML
software, ii) identify the prevalence of design bugs in ML software,
iii) provide bug detection techniques for design bugs, and iv) operationalize this knowledge for application by ML engineers and
evaluate its effectiveness in applied settings.
Conceptual Design Errors. To some extent, previous work has
identified that ML practitioners commonly make conceptual design
errors by studying student code [58, 80], question types on StackOverflow [4], and solutions offered in literature [7, 54]. Although
these studies are fundamental to this work, they give limited insights into the conceptual design errors made by ML practitioners
and how they impact ML engineering. I want to expand this foundation by determining theoretically and empirically whether ML
practitioners make conceptual design errors, when they make them,
how frequently they do so, what their impact is, and how these
errors are currently resolved (if they are). The anticipated results
will anchor the proposed research’s motivation and give valuable
insights for developing a solution. Therefore, the first research
question of this proposed line of work is:
RQ1 What are the types, impacts, and resolution methods of conceptual design errors encountered by ML engineers?
Contract Mining. One of the primary goals of this work is to
help ML practitioners prevent conceptual design errors. I drew
inspiration from previously proposed solutions that used API contracts [1, 21, 50] to identify bugs and inconsistencies between
datasets and ML algorithms in data science and deep learning
software. To do this, we need to identify the constraints and assumptions made by ML APIs. The documentation of ML APIs is
commonly a rich source of information on conceptual knowledge of
ML algorithms and functions. Previous work used API documentation already to build basic contracts, like valid input ranges [50, 72].
Although this is a promising source of conceptual knowledge, documentation is notorious for its incompleteness and inaccuracy [7, 59].
Therefore, we intend to explore other sources of information, like
StackOverflow [4]. Thus, our second research question is:
RQ2 How can API conceptual design constraints be mined from ML
documentation?
Contract-based Validation. The third step of our research is to put
the acquired conceptual knowledge into practice by translating API
constraints into contracts. This introduces a significant technical
challenge as software contracts are traditionally control-oriented,
whereas ML APIs also assume dataset properties. Therefore, beyond simple restrictions on hyperparameters (like restricting an
argument to a predefined list of options), we anticipate that partial models [39] could be used to infer partially defined data types/ranges and validate whether they match the prerequisites of ML
APIs without analyzing complete datasets. Because ML practitioners commonly combine functionalities from different ML libraries,
we intend to build library-agnostic tooling emphasizing compatibility between ML packages; i.e., by specifically addressing complex
ML software. The third research question is as follows:
RQ3 How can API contracts be used to detect conceptual errors in
complex ML software at design time?
Contract-based Validation in Practice. Successfully answering the
previous three research questions provides the necessary handhelds
to evaluate professional ML software. We intend to evaluate the
benefit of our work twofold: 1) by analyzing publicly available data
acquired from, e.g., GitHub or Kaggle, and 2) by performing case
studies with professional (industrial) ML practitioners. Evaluating
the tool in practice will yield results threefold: 1) we test the benefit
of our tool, 2) we generate further empirical evidence of conceptual
design errors made in professional ML software, and 3) we identify flaws in our approach that allow us to improve it over time.
Therefore, our fourth and final research question is:
RQ4 How useful are API contracts for (industrial) ML engineers to
detect conceptual design errors?
4 RELATED WORK
ML engineering has started to gain traction in recent years, taking
an interest in software engineering problems like project management [63], code quality [10, 11, 14, 23, 32, 34, 40, 43, 56, 62, 81], technical debt [6, 47, 57, 61, 66], running model training jobs [20, 22, 75],
or system integration [13, 33, 64, 76].
Design Errors in Deep and Machine Learning Software. There are
several problems specific to ML software, like errors made in the
software’s design. Various studies have explored different error
types made by students in ML courses [58, 80], by ML engineers [4],
and by deep learning engineers [29, 75]. These studies find that
practitioners commonly make conceptual errors while building
learning software. An example is when invalid data points are used
to train a model that does not support them, like NaN values inserted
into a sklearn’s LogisticRegression model. Conceptual misconceptions are problematic in learning software because although
the code is generally syntactically correct, it might crash at runtime [75, 76, 78], misbehave by outputting wrong/poor results, or
run unacceptably slow [29, 31, 75, 76, 78]. Large-scale and complex
systems suffer significantly from these bugs because they are hard
to detect (frequently at the engineer’s merit) and commonly waste
scarce computing resources.
In deep learning software, conceptual bugs commonly relate to
the shape of tensors [30, 31, 46, 53, 69–71, 75, 78], incorrect activation functions and feature transformations [29, 30, 46, 65, 75, 78],
model structure/configuration [29–31, 45, 75, 76], and faulty experimental setups [29, 46]. Such bugs commonly arise from misunderstanding ML APIs, such that the ML engineer misunderstands the
semantics of an API like its underlying assumptions or internal
behavior [31, 76, 78].
Conceptual errors are not unique to deep learning and have been
reported to some extent in “general ML engineering” as well. Alshangiti et al. [4] reported that questions asked by ML practitioners
more commonly require technical ML expertise (66%) than theoretical knowledge (31%) in StackOverflow posts. Comparatively,
Skripchuk et al. [58] and Zimmermann et al. [80] studied errors
commonly made by students following a foundational course in ML.
They report that students commonly struggle with ML software
engineering at a technical and conceptual level. Errors occur across
the entire ML pipeline, like poor data preprocessing and cleaning,
improper train and test data selections/usage, unfounded or ad hoc
model and hyperparameter selection, or selecting these based on
incorrect assumptions about ML APIs or their datasets. The last of
these is quintessential for conceptual errors in ML as they highlight
the close relationship between input data and algorithm selection/-
tuning. These findings are not restricted to students, as Bogner et al.
[7] concluded professionals make similar mistakes. For example,
using entangled features (i.e., dependent features) or poorly preprocessed data (e.g., unscaled data) to create new models. Dataset
quality issues have also been reported in previous studies [18, 49].
Contract-based API Validation in ML Software. Several attempts
have been made to tackle bugs in ML software, allowing practitioners to provide some quality assurances. Recent endeavors have
explored data cleaning and validation for ML datasets, like Budach
et al. [9] and Schelter et al. [52]. Respectively, they provide solutions to complement data with domain knowledge and data quality
constraints, treating it as a standalone task in the ML pipeline.
Table 1 summarizes the three recent studies on contract-based
API validation which should be detailed in particular: Ahmed et al.
[1], Reimann and Kniesel-Wünsche [50], and Gao et al. [21]. These
studies integrate data validation into the ML design process to verify the compatibility of input data with ML models. Ahmed et al.
[1] and Reimann and Kniesel-Wünsche [50] use API contracts to
verify their usage in learning software. Simply put, API contracts
are sets of constraints describing the limits of an API to prevent
misuse, like inserting NaN data into a logistic regression classifier.
To prevent this, you could create a contract for the function to limit
the input to valid numbers. Ahmed et al. [1] proposed “deep learning contracts,” implementing 15 API contracts for endpoints in the
Keras framework, without adding coding overhead for API users
and by adding very little performance overhead to evaluate the
contracts at runtime. They use handwritten contracts to evaluate a
method’s preconditions (e.g., validating hyperparameter combinations) and postconditions (e.g., testing the training convergence).
Through experiments on 272 buggy programs and several user surveys, they conclude that these contracts can be used effectively to
identify and repair bugs in deep learning software. Reimann and
Kniesel-Wünsche [50] present Safe-DS, a domain-specific language
Table 1: Studies on Contract-based ML API Validation, summarizing the method they use, the types of rules they introduce, the pipeline phase in which they are applied, and their
solution domain: deep learning (DL) or more general ML
Paper Method Constraints Pipeline Domain
[1] API Contracts Hyperparameters,
training results
Design DL
[50] DSL, Contracts Data, pipeline
structure
Design ML
[21] Refinement
types
Hyperparameters Pre-run DL
Ours API Contracts Pipeline structure, hyperparameters, data
Design ML
for statically safe data science software. Their framework ensures
various compatibility factors between input data and data science
functions, like the types and ranges of variables in a dataset (e.g., a
function that only accepts positive integers). Further, it can enforce
order of execution (e.g., to ensure a model is trained before it is
used to predict). Finally, Gao et al. [21] proposed Refty, a tool that
uses refinement types (types with additional constraints/predicates,
like data ranges, for more precise type-checking4
) to validate deep
learning operands. Before running deep learning jobs, they use
it to identify illegal/improper hyperparameters and unsupported
tensor shapes/types/formats.
These studies [1, 21, 50] increase the likelihood of detecting conceptual errors in learning software using API contracts. However,
I believe their applicability can be improved as they either 1) are
applied after designing the program [21], 2) require the adoption
of a new DSL [50], or 3) limit themselves to hyperparameters and
test results [1]. In contrast, 1) engineers benefit greatly when receiving feedback at design-time [37], 2) notebooks are the most
common medium used to develop ML code [26], and 3) a substantial
number of conceptual errors are a mismatch between input (both
hyperparameters and datasets) and API prerequisites [7, 18, 49].
The proposed research aims to combine these requirements.
5 PROPOSED RESEARCH AND EVALUATION
I propose a contract-based tool for conceptual bug detection in
ML software at design time. We expect ML engineers to use this
technology to optimize their ML development because conceptual
errors can be caught before running their code with limited to no
additional programming overhead.
I propose to complete the studies in Figure 1 which roughly
follows the research questions posed in Section 3. This timeline
presents the main line of research. I will likely pursue supporting
research projects to complement or verify the results of the main
studies. These are not detailed separately, however, they flow naturally from the primary line of work and are suggested in the
following paragraphs.
Proof of Concept. We will start working towards a simple proof
of concept of the proposed solution. This is imperative as it gives
4This is very similar to API contracts presented in this paper as contracts can be used
to enforce data types and the refinement types’ additional predicates [50].
a quick indication of the feasibility of the proposed research. We
intend to build a prototype of contract-based evaluation for conceptual design errors in Python notebooks and test the relevance of
several data sources used to write contracts (e.g., documentation or
platforms like GitHub and StackOverflow). Evaluating data sources
is important as API documentation is commonly incomplete [7, 59].
An ironic example of this is the StandardScaler component in the
sklearn library,3
an object that standardizes normally distributed
data using its mean and variance, which does not state it assumes
the input data is normally distributed, only that other ML estimators might assume “more or less standard normally distributed data.”
In this step, we leverage a dataset constructed in the continuation of previous work [67] to identify conceptual errors and the
combinations of libraries used by practitioners.
Systematic Literature Review. The first step of this research is a
systematic literature review on errors made in ML software. Various
other literature reviews and mapping studies have been published in
recent years, discussing themes like AI testing [8, 38, 48, 51, 77], challenges in AI engineering [17, 44], ML pipeline quality [19, 68, 79],
pipeline replicability [27], or ML maintainbility [55]. Although these
cover a range of themes related to the robustness and quality of ML
software, these tend not to address errors made by ML practitioners,
giving limited insights into our problem domain. The papers addressed in Section 4 are an early product of this review, indicating
its benefit already. I intentionally target ML errors in general (not
only conceptual design errors) to establish a firmer base for our
and other work without substantially increasing its scope (based
on the preliminary results, we anticipate this increases the number
of included papers by approximately 30%, which is reasonable).
Qualitative Empirical Study on Conceptual Errors. Beyond extracting common conceptual design errors from existing literature,
I intend to perform a finer-grained analysis of the types of conceptual errors made by ML practitioners. Previous work has indicated
the problem of conceptual design errors [4] and described them to
some extent [7, 54, 58, 80]. However, none perform a fine-grained
analysis of these errors in practice. I expect that conceptual design
errors are commonly complex, involving the code’s structure (e.g.,
the control/data flow), the input data (e.g., feature distributions),
and the selection of ML algorithms and hyperparameters. These
previous studies do not address this in great detail — especially for
complex ML software (i.e., ML software that composes multiple ML
libraries). We intend to leverage one or multiple data sources to
achieve this, like the notebooks acquired in the continuation of peer
work [67], or other promising platforms like StackOverflow or issue
tracking systems like GitHub and GitLab. These platforms have
yielded interesting insights in previous studies (e.g., [4, 30, 31, 74]).
API Contract Design. The previous steps will have given us a
firm foundation of conceptual errors in ML software. The expected
outcome of this study should highlight various technical considerations that must be made when detecting them at design time. Going
back to the guiding examples given in Section 2, an example of a
technical requirement is an efficient means to test the distribution
of a model’s input data at design time. Such a requirement translates to a substantial technical challenge as evaluating it accurately
and efficiently is non-trivial. First, I intend to operationalize these
requirements at a conceptual level, identifying the different facets
of an API contract for conceptual errors and the underlying models
(e.g., DSLs for datasets [24]) and technologies (e.g., PyContracts,5
used by Ahmed et al. [2], PyDeequ6 or TFDV,7 used by Schelter
et al. [52]) that can be leveraged to implement them. We can draw
inspiration from previous contract-based solutions applied to a
DSL [50] and deep learning software [1, 21]. These identified means
to validate input data and process structure statically. In addition,
because ML code is very flexible, we expect that partial models [39]
could be used to verify the properties of a dataset (e.g., range and
distribution) without substantial computational overhead. In the
meantime, we want to closely follow a recent thread of research
using runtime information to complement static analysis in Python
notebooks [67], which could benefit our work too. We want to push
these previous studies forward by pulling this validation process
into the ML modeling phase, actively evaluating compatibilities
between data properties and model constraints.
API Contract Mining. The previous steps will have given us insights into the types of conceptual errors in ML software and a
tool to detect them at design time. A big challenge in this solution’s operationalization is the array of ML libraries and versions
of those libraries practitioners use [16]. Consequently, the adoption
and impact of a tool that validates the use of interfaces in these
libraries depends on the support for previous, current, and future
library releases. This could be done manually (like Ahmed et al.
[1]), however, it can be automated as well. For example, this has
already been done to identify valid input ranges [50, 72]. I want to
identify how conceptual constraints can be mined automatically
and validate their accuracy. We anticipate that natural language
processing techniques, like large language models, can be leveraged in this process as they have shown promising results in similar
tasks (e.g., extracting facts from unstructured medical data [25]).
We expect these methods to improve in the coming years. The proof
of concept and the qualitative empirical study performed during
the earlier stages of this research should have given us insights into
the value and usage of different data sources. I want to execute this
research task in parallel with the design study for API contracts
because the contract’s design strongly depends on the data used to
generate them and the mining process depends on the contract’s input expectations. In other words: I expect both studies to co-evolve.
5PyContracts: https://andreacensi.github.io/contracts
6PyDeequ: https://github.com/awslabs/python-deequ
7TFDV: https://www.tensorflow.org/tfx/guide/tfdv
The combined results of these research steps will be a functional
prototype that can evaluate real ML software.
Quantitative Empirical Study in (Industrial) ML Software. My
research aims to provide ML engineers with a tool that assures
the conceptual design quality of their ML software. The preceding
research tasks will have given us the necessary theoretical and
technological artifacts to evaluate it in practice. The goal of this
research task is therefore two-fold: 1) I intend to evaluate the applicability and usability of the created tool in practice by performing
a user study with novice and experienced ML engineers, and 2) I
intend to acquire additional empirical evidence of the prevalence of
conceptual design errors in professional ML software. These results
will benefit the greater academic and industrial community who
want to evaluate or integrate similar and different quality assurance
methods into their ML engineering workflow.
6 RISKS AND ETHICAL ISSUES
A risk of tooling that makes quality assurances introduces the risk
of false confidence in a system. This is especially problematic for
conceptual design errors in ML software as these commonly persist
unnoticed [60] and can have big societal impacts. We therefore
explicitly include evaluations using professional ML software in
our research plan to identify the tool’s limitations. These will be
presented accordingly. We are unaware of any other risks or ethical
issues arising from this line of research.
7 CURRENT STATUS
The timeline presented in Figure 1 provides an overview of the
primary line of proposed research. At the time of writing, only four
months have passed since I started my PhD research for which we
stand at the start of the proposed timeline. In preparation for this
Doctoral Symposium, I performed a rapid literature review [12]
that mimics the proposed systematic literature review using less
stringent requirements to account for the limited amount of available time. For example, the search protocol only considered an
automated search on studies after 2017 combined with forward
snowballing to maximize the number of included recent papers,
however, reducing the included number of older papers. In direct
continuation of this work, we intend to continue with the systematic literature review as well as build a proof of concept that
validates the feasibility of the proposed research.
ACKNOWLEDGMENTS
I thank my PhD supervisors, Dániel Varró and Kristian Sandahl, and
my colleagues Yiran Wang and José Antonio Hernández López for
their support, insights, and feedback while writing this paper. This
work was partially supported by the Wallenberg AI, Autonomous
Systems and Software Program (WASP) funded by the Knut and
Alice Wallenberg Foundation.
