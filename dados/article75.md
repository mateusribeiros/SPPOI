Title: MLHOps: Machine Learning Health Operations

ABSTRACT Machine Learning Health Operations (MLHOps) is the combination of processes for reliable,
efficient, usable, and ethical deployment and maintenance of machine learning models in healthcare settings.
This paper provides both a survey of work in this area and guidelines for developers and clinicians to deploy
and maintain their own models in clinical practice. We cover the foundational concepts of general machine
learning operations and describe the initial setup of MLHOps pipelines (including data sources, preparation,
engineering, and tools). We then describe long-term monitoring and updating (including data distribution
shifts and model updating) and ethical considerations (including bias, fairness, interpretability, and privacy).
This work therefore provides guidance across the full pipeline of MLHOps from conception to initial and
ongoing deployment. We also include a checklist to ensure thorough verification of each step in the process.
INDEX TERMS Computational and artificial intelligence, machine learning, engineering in medicine and
biology, electronic healthcare, health information management, hospitals.
I. INTRODUCTION
Over the last decade, efforts to use health data for solving
complex medical problems have increased significantly.
Academic hospitals are increasingly dedicating resources to
bring machine learning (ML) to the bedside and to addressing
issues encountered by clinical staff. These resources are
being utilized across a range of applications including clinical
decision support, early warning, treatment recommendation,
risk prediction, image informatics, tele-diagnosis, drug
discovery, and intelligent health knowledge systems.
There are various examples of ML being applied to
medical data, including prediction of sepsis [265], in-hospital
mortality, prolonged length-of-stay, patient deterioration,
and unplanned readmission [240]. In particular, sepsis is
one of the leading causes of in-hospital deaths. A largescale study demonstrated the impact of an early warning
system to reduce the lead time for detecting the onset
of sepsis, and hence allowing more time for clinicians to
prescribe antibiotics [6]. Similarly, deep convolutional neural
networks have been shown to achieve superior performance
in detecting pneumonia and other pathologies from chest
X-rays, compared to practicing radiologists [241]. These
results highlight the potential of ML models when they are
strongly integrated into clinical workflows.
When deployed successfully, data-driven models can free
time for clinicians [118], improve clinical outcomes [239],
reduce costs [31], and provide improved quality care
for patients. However, most studies remain preliminary,
limited to small datasets, and/or implemented in select
health sub-systems. Integrating with clinical workflows
remains crucial [295], [307] but, despite recent computational
advances and an explosion of health data, deploying ML in
healthcare responsibly and reliably faces several operational
and engineering challenges, including:
• Standardizing data formats,
• Strengthening methodologies for evaluation, monitoring
and updating,
• Building trust with clinicians and hospital staff,
• Adopting interoperability standards, and
• Ensuring that deployed models align with ethical
considerations, do not exacerbate biases, and adhere to
privacy and governance policies
In this review, we articulate the challenges involved
in implementing successful Machine Learning Health
Operations (MLHOps) pipelines, specific to clinical use
cases. We begin by outlining the foundations of model
deployment in general, and provide a comprehensive study
of the emerging discipline [186], [279]. We then provide a
detailed review of the different components of development
pipelines specific to healthcare. We discuss data, pipeline
engineering, deployment, monitoring and updating models,
and ethical considerations pertaining to healthcare use cases.
While MLHOps often requires aspects specific to healthcare,
best practices and concepts from other application domains
are also relevant. This summarizes the primary outcome of
our review, which is to provide a set of recommendations
for implementing MLHOps pipelines in practice – i.e., a
‘‘how-to’’ guide for practitioners and also provide a checklist
(Section VII).
II. FOUNDATIONS OF MLOPS
A. WHAT IS MLOps?
Machine learning operations (MLOps) is a combination of
tools, techniques, standards, and engineering best practices
to standardize ML system development and operations [279].
It is used to streamline and automate the deployment,
monitoring, and maintenance of machine learning models,
in order to ensure they are robust, reliable, and easily updated
or upgraded.
B. MLOps PIPELINE
Pipelines are processes of multiple modules that streamline
the ML workflow. Once the project is defined, the MLOps
pipeline begins with identifying the inputs and outputs
relevant to the problem, cleaning, and transforming the data
towards useful and efficient representations for machine
learning, training, and evaluating model performance, and
deploying selected models in production while continuing to monitor their performance. Figure 1 illustrates
a general MLOps pipeline. Common types of pipelines
include:
• Automated pipelines: An end-to-end pipeline that is
automated towards a single task, e.g., a model training
pipeline.
• Orchestrated pipelines: A pipeline that consists of
multiple modules, designed for several automated tasks,
and managed and coordinated in a dynamic workflow,
e.g., the pipeline managing MLOps.
Recently, MLOps has become more well-defined and
widely implemented due to the reusability and standardization benefits across various applications [253]. As a result,
the structure and definitions of different components are
becoming quite well-established.
C. MLOps COMPONENTS
MLOps pipelines consist of different components and key
concepts [117], [148], stated below (and shown in Figure 1):
• Stores: Stores encapsulate the tools designed to centralize building, managing, and sharing either features
or models across different teams and applications in an
organization.
- Raw data source: A raw data store is a centralized
repository that stores data in its raw, unprocessed
form. It is a staging area where data is initially collected and stored before processing or transformation.
- Feature store: A centralized online repository
for storing, managing, and sharing features used
in ML models. These features are acquired by
processing the raw data and are made available for real-time serving through the feature
store.
- ML metadata store: A ML metadata store helps
record and retrieve metadata associated with an ML
pipeline including information about various pipeline
components, their executions (e.g. training runs), and
resulting artifacts (e.g. trained models).
• Serving: Serving is the task of hosting ML artifacts
(usually models) either on the cloud or on-premise so
that their functions are accessible to multiple applications through remote function calls (i.e., application
programming interfaces (APIs)).
- In batch serving, the artifact is used by scheduled jobs.
- In online serving, the artifact processes requests in
real-time. Communication and access point channels, traffic management, pre- and post-processing
requests, and performance monitoring should all be
considered while serving artifacts.
• Data query: The component queries the data, processes
it and stores it in a format that models can easily utilize.
• Experimentation: The experimentation component
consists of model training, model evaluation, and model
validation.
• Model registry: The model registry is a centralized
repository that stores trained machine learning models,
their metadata, and their versions.
• Drift-detection: The drift-detection component is
responsible for monitoring the AI system for potentially harmful drift and issuing an alert when drift is
detected.
• Workflow orchestration: The workflow orchestration
component responsible for the process of automating
and managing the end-to-end flow of the ML pipeline.
• Source repository: The source repository is a centralized code repository that stores the source code (and its
history) for ML models and related components.
• Containerization: Containerization involves packaging
models with the components required to run them; this
includes libraries and frameworks so they can run in
isolated user spaces with minimal configuration of the
FIGURE 1. Proposed MLOps pipeline.
underlying operating system [96]. Sometimes, source
code is also included in these containers.
D. LEVELS OF MLOps MATURITY
MLOps practices can be divided into different levels based
on the maturity of the ML system automation process [128],
[279], as described below.
• Level 0 – Manual ML pipeline: Every step in
the ML pipeline, including data processing, model
building, evaluation, and deployment, are manual processes. In Level 0, the experimental and operational
pipelines are distinct and the data scientists provide
a trained model as an artifact to the engineering
team to deploy on their infrastructure. Here, only the
trained model is served for deployment and there are
infrequent model updates. Level 0 processes typically
lack rigorous and continuous performance monitoring
capabilities.
• Level 1 – Continuous Model Training and Delivery:
Here, the entire ML pipeline is automated to perform
continuous training of the model as well as continuous
delivery of model prediction services. Software orchestrates the execution and transition between the steps in
the pipeline, leading to rapid iteration over experiments
and an automatic process for deploying a selected
model into production. Contrary to Level 0, the entire
training pipeline is automated, and the deployed model
can incorporate newer data based on pipeline triggers.
Given the automated nature of Level 1, it is necessary
to continuously monitor, evaluate, and validate models and data to ensure expected performance during
production.
• Level 2 – Continuous Integration and Continuous Delivery: This involves the highest maturity in
automation through enforcing combined practice of
continuous integration and delivery which enables
for a rapid and reliable update of the pipelines in
production. Through automated test and deployment
of new pipeline implementations, any rapid changes
in data and business environment can be addressed.
In this level, the pipeline and its components are
automatically built, tested, and packaged when new
code is committed or pushed to the source code repository. Moreover, the system continuously delivers new
pipeline implementations to the target environment that
in turn delivers prediction services of the newly trained
model.
Ultimately implementation of MLOps leads to many
benefits, including better system quality, increased scalability, simplified management processes, improved governance
and compliance, increased cost savings and improved
collaboration.
III. MLHOps SETUP
Operationalizing ML models in healthcare is unique among
other application domains. Decisions made in clinical
environments have a direct impact on patient outcomes and,
hence, the consequences of integrating ML models into
health systems need to be carefully controlled. For example,
early warning systems might enable clinicians to prescribe
treatment plans with increased lead time [118]; however,
these systems might also suffer from a high false alarm
rate, which could result in alarm fatigue and possibly worse
outcomes. The requirements placed on such ML systems
are therefore very high and, if they are not adequately
satisfied, the result is diminished adoption and trust from
clinical staff. Rigorous long-term evaluation is needed to
validate the efficacy and to identify and assess risks, and
this evaluation needs to be reported comprehensively and
transparently [294].
While most MLOps best practices extend to healthcare
settings, the data, competencies, tools, and model evaluation
differ significantly [18], [192], [200], [283]. For example,
the preference for using typical performance metrics (e.g.,
positive predictive value and F1-scores) may vary between
clinicians and engineers. Therefore, unlike in other industries,
it becomes necessary to evaluate physician experience
when predictions and model performance are presented to
clinical staff [301]. To build trust in the clinical setting, the
interpretability of ML models is also extremely important.
As more ML models are integrated into hospitals, new legal
frameworks and standards for evaluation must be adopted,
and MLHOp tools must comply with existing standards.
In the following sections, we explore the different
components of MLHOps pipelines.
A. DATA
Successfully digitizing health data has resulted in a prodigious increase in the volume and complexity of patient data
collected [240]. These datasets are now stored, maintained,
and processed by hospital IT infrastructure systems which in
turn use specialized software systems.
1) DATA SOURCES
There could be multiple sources of data, which are
categorized as follows:
Electronic health records (EHRs) record, analyze, and
present information to clinicians, including:
1) Patient demographic data: For example, age and sex.
2) Administrative data: For example, treatment costs and
insurance.
3) Patient observations records: For example, chart
events such as lab tests and vitals. These include
a multitude of physiological signals captured using
various methods such as heart rate, blood pressure, skin
temperature, and respiratory rate.
4) Interventions: These are steps that significantly
alter the course of patient care, such as mechanical
ventilation, dialysis, or blood transfusions.
5) Medications information: For example, medications
administered and their dosage.
6) Waveform data: This digitizes physiological signals
collected from bedside patient monitors.
7) Imaging reports and metadata: For example,
CT scans, MRI, ultrasound, and corresponding
radiology reports.
8) Medical notes: These are made by clinical staff on
patient condition. These can also be transcribed text of
recorded interactions between the patient and clinician.
Other sources of health data include primary care data,
wearable data (e.g., smartwatches), genomics data, video
data, surveys, medical claims, billing data, registry data, and
other patient-generated data [33], [48], [238].
Figure 2 illustrates the heterogeneous nature of health
data. The stratification shown can be extended further to contain more specialized data. For example,
genomics data can be further stratified into different
types of data based on the method of sequencing;
observational EHR data can be further stratified to
include labs, vital measurements, and other recorded
observations.
With such large volumes and variability in data, standardization is key to achieve scalability and interoperability.
Figure 3 illustrates the different levels of standardization that
need to be achieved with respect to health data.
2) COMMON DATA MODEL (CDM)
Despite the widespread adoption of EHR systems, clinical events are not captured in a standard format across
observational databases [216]. For effective research and
implementation, data must be drawn from many sources and
compared and contrasted to be fully understood.
Databases must also support scaling to large numbers of
records which can be processed concurrently. Hence, efficient
storage systems along with computational techniques are
needed to facilitate analyses. One of the first steps towards
scalability is to transform the data to a common data standard.
The extraction, transformation, and loading (ETL) process is
a data integration procedure utilized to convert information
into a standardized format. In addition to scale, patient
data require a high level of protection with strict data
user agreements and access control. A common data model
addresses these challenges by allowing for downstream
functional access points to be designed independent of the
data model. Data that is available in a common format
promotes collaboration and mitigates duplicated effort.
Specific implementations and formats of data should be
hidden from users, and only high-level abstractions need to be
visible.
The Systematized Nomenclature of Medicine (SNOMED)
was among the first efforts to standardize clinical terminology, and a corresponding dictionary with a broad
range of clinical terminology is available as part of
SNOMED-CT [75]. Several data models use SNOMED-CT
as part of their core vocabulary. Converting datasets to
a common data model like the Observational Medical
Outcomes Partnership (OMOP) model involves mapping
from a source database to the target content delivery manager.
FIGURE 2. Stratification of health data. Further levels of stratification can be extended as
the data becomes richer. For example, observational EHR data could include labs, vital
measurements, and other recorded observations.
FIGURE 3. The hierarchy of standardization that common data models and open
standards for interoperability address. The lowest level is about achieving
standardization of variable names such as lab test names, medications, and diagnosis
codes, as well as the data types used to store these variables (i.e. integer vs. character).
The next level is about having abstract concepts such that data can be mapped and
grouped under these concept definitions. The top level of standardization is about
data exchange formats, e.g. JSON, XML, protocols, along with protocols for information
exchange like supported RESTful API architectures. This level addresses questions on
interoperability and how data can be exchanged across sites and EHR systems.
This process is usually time-consuming and involves a
lot of manual effort undertaken by data scientists. Tools
to simplify the mapping and conversion process can save
time and effort and promote adoption. For OMOP, the
ATLAS tool [216] developed by Observational Health
Data Sciences and Informatics (OHDSI) provides such
a feature through their web based interactive analysis
platform.
3) INTEROPERABILITY AND OPEN STANDARDS
As the volume of data grows in healthcare institutions and
applications ingest data for different use cases, real-time
performance and data management is crucial. To enable
real-time operation and easy exchange of health data across
systems, an interoperability standard for data exchange
along with protocols for accessing data through easy-to-use
programming interfaces is necessary. Some of the popular
healthcare data standards include Health Level 7 (HL7),
Health Level 7 v2 (HL7v2), Fast Healthcare Interoperability
Resources (FHIR), and Digital Imaging and Communications
in Medicine (DICOM).
The FHIR standard [34] is a leading open standard
for exchanging health data. FHIR is developed by Health
Level 7 (HL7), a not-for-profit standards development
organization that was established to develop standards for
hospital information systems. FHIR defines the key entities
involved in healthcare information exchange as resources,
where each resource is a distinct identifiable entity. FHIR
also defines APIs which conform to the representational
state transfer (REST) architectural style for exchanging
resources, allowing for stateless Hypertext Transfer Protocol
(HTTP) methods, and exposing directory-structure like
URIs to resources. RESTful architectures are light-weight
interfaces that allow for faster transmission, which is
more suitable for mobile devices. RESTful interfaces also
facilitate faster development cycles because of their simple
structure.
DICOM is the standard for the communication and
management of medical imaging information and related
metadata. The DICOM standard specifies the format and
protocol for exchange of digital information between medical
imaging equipment and other systems. Persistent information objects which encode images are exchanged and an
instance of such an information object may be exchanged
across many systems and many organizational contexts,
and over time. DICOM has enabled deep collaboration
and standardization across different disciplines such as
radiology, cardiology, pathology, ophthalmology, and related
disciplines.
4) QUALITY ASSURANCE AND VALIDATION
Data collected in retrospective databases for analysis and ML
use cases need to be checked for quality and consistency. Data
validation is an important step towards ensuring that ML systems developed using the data are highly performant, and do
not incorporate biases from the data. Errors in data propagate
through the MLOps pipeline and hence specialized data quality assurance tools and checks at various stages of the pipeline
are necessary [246]. A standardized data validation framework that includes i) data element pre-processing, ii) checks
for completeness (structure assessment and value presence),
conformance (data representation aligning with internal or
external formatting, relational, or computational standards),
and plausibility (believability or correctness of data) [133],
and iii) a review process by clinicians and other stakeholders
should capture generalizable insight across various clinical
investigations [264].
B. PIPELINE ENGINEERING
Data stored in raw formats need to be processed to create
feature representations for ML models. Each transformation
is a computation, and a chain of these processing elements,
arranged so that the output of each element is the input of
the next, constitutes a pipeline [148] and using software tools
and workflow practices that enable such pipelines is pipeline
engineering.
There are advantages to using such a pipeline approach,
including:
• Modularization: The chain of transformations is broken
down into small steps.
• Testing: Each transformation step can be tested independently, which facilitates quality assurance and testing.
• Debugging: Version controlling the outputs at each
step makes it easier to ensure reproducibility, especially
when many steps are involved.
• Parallelism: If any step in the pipeline is easily parallelizable across multiple compute nodes, the overall
processing time can be reduced.
• Automation: Complex tasks are broken down into a
series of smaller tasks which can be automated using
continuous integration tools such as Jenkins, GitHub
actions and Gitlab CI.
In health data processing, the following steps are crucial:
1) Cleaning: Formatting values, adjusting data types,
checking and fixing issues with raw
data.
2) Encoding: Computing word embeddings for clinical
text, encoding the text and raw values into embeddings [16], [140]. Encoding is a general transformation
step that can be used to create vector representations
of raw data. For example, transforming images to
numeric representations can also be considered to be
encoding.
3) Aggregation: Grouping values into buckets, e.g., for
aggregating measurements into fixed time-intervals,
or grouping values by patient ID.
4) Normalization: Normalizing values into standard
ranges or using statistics of the data.
5) Imputation: Handling missing values in the data. For
various clinical data, ‘missingness’ can actually provide
valuable contextual information about the patient’s
health and needs to be handled carefully [50].
Multiple data sources such as EHR data, clinical notes
and text, imaging data, and genomics data can be processed
independently to create features and they can be combined
to be used as inputs to ML models. Hence, composing
pipelines of these tasks facilitates component reusability
[124]. Furthermore, since the ML development life-cycle
constitutes a chain of tasks, the pipelining approach becomes
even more desirable. Some of the high level tasks in the
MLHOps pipeline include feature creation, feature selection,
model training, evaluation, and monitoring. Evaluating
models across different slices of data, hyper-parameters,
and other confounding variables is necessary for building
trust.
Table 1 lists popular open-source tools and packages
specific to health data and ML processing. These tools
are at different stages of development and maturity. Some
examples of popular tools include MIMIC-Extract [302],
Clairvoyance [124] and CheXstray [272].
C. MODELLING
At this stage, the data has been collected, cleaned, and
curated, ready to be fed to the ML model to accomplish
the desired task. The modelling phase involves choosing
the available models that fit the problem, training &
testing the models, and choosing the model with the best
performance & reliability guarantees. Given the existence
of numerous surveys summarizing machine learning and
deep learning algorithms for general healthcare scenarios [1],
[83], as well as specific use cases such as brain tumor
detection [20], COVID-19 prevention [29], and clinical
text representation [140], we omit this discussion and let
the reader explore the surveys relevant to their prediction
problem.
D. INFRASTRUCTURE AND SYSTEM
Hospitals typically use models developed by their EHR
vendor which are deployed through the native EHR vendor
configuration. Often, inference is run locally or in a
cloud instance, and the model outputs are communicated
within the EHR [137]. Predominantly, these models are
pre-trained and sometimes fine-tuned on the specific site’s
data.
A feature store is a ML-specific data system used to
centralize storage, processing, and access to frequently used
features, making them available for reuse in the development
of future machine learning models. Feature stores operationalize and streamline the input, tracking, and governance
of the data as part of feature engineering for machine
learning [148].
To ensure reliability, the development, staging, and
production environments are separated and have different
requirements. The staging and production environments
typically consist of independent virtual machines with
adequate compute and storage, along with reliable and secure
connections to the databases.
The infrastructure and software systems also have to follow
and comply with cybersecurity, medical software design and
software testing standards [71].
1) ROLES AND RESPONSIBILITIES
Efficient and successful MLHOps requires a collaborative,
interdisciplinary team across a range of expertise and competencies commonly found in data science, ML, software,
operations, production engineering, medicine, and privacy
capabilities [148]. Similar to general MLOps practices,
data and ML scientists, data, DevOps, and ML engineers,
solution and data architects, ML and software fullstack
developers, and project managers are needed. In addition,
the following role are required, which are distinct to
healthcare (for more general MLOps roles see Table 5 in the
Appendix):
• Health AI Project Managers: Responsibilities include
planning projects, establishing guidelines, milestone
tracking, managing risk, supporting the teams and
governing partnerships with collaborators from other
health organizations.
• Health AI Implementation Coordinator: Liaison
that engages with key stakeholders to facilitate the
implementation of clinical AI systems.
• Healthcare Operations Manager: Oversees and coordinates quality management, resource management,
process improvement, and patient safety in clinical
settings like hospitals.
• Clinical Researchers & Scientists: Domain experts
that provide critical domain-specific knowledge relevant
to model development and
implementation.
• Patient-Facing Practitioners: Responsibilities include
providing system requirements, pipeline usage feedback, and perspective about the patient experience (e.g.
clinicians, nurses).
• Ethicists: Provides support regarding ethical implications of clinical AI systems.
• Privacy Analysts: Provides assessments regarding
privacy concerns pertaining to the usage of patient
data.
• Legal Analysts: Works closely with privacy analysts
and ethicists to evaluate the legal vulnerabilities of
clinical AI systems.
E. REPORTING GUIDELINES
Many clinical AI systems do not meet reporting standards
because of a failure to assess for poor quality or unavailable
input data, insufficient analysis of performance errors,
or a lack of information regarding code or algorithm
availability [230]. Systematic reviews of clinical AI systems suggest there is a substantial reporting burden, and
additions regarding reliability and fairness can improve
reporting [182]. As a result, guidelines informed by challenges in existing AI deployments in health settings have
become imperative [64]. Reporting guidelines including
CONSORT-AI [175], DECIDE-AI [294], and SPIRIT-AI
[249] were developed by a multidisciplinary group of
international experts using the Delphi process to ensure
complete and transparent reporting of randomized clinical
trials (RCT) that evaluate interventions with an AI model.
Broadly these guidelines suggest inclusion of the following
criteria [71]:
• Intended use: Inclusion of the medical problem and
context, current standard practice, intended patient
population(s), how the AI system will be integrated
into the care pathway, and the intended patient
outcomes.
• Patient and user recruitment: Well-defined inclusion
and exclusion criteria.
• Data and outcomes: The use of a representative
patient population, data coding and processing, missingand low-quality data handling, and sample size
considerations.
• Model: Inclusion of inputs, outputs, training, model
selection, parameter tuning, and performance.
• Implementation: Inclusion of user experience with the
AI system, user adherence to intended implementation,
and changes to clinical workflow.
• Modifications: A description protocol for changes
made, timing and rationale for modifications, and
outcome changes after each modification.
• Safety and errors: Identification of system errors
and malfunctions, anticipated risks and mitigation
strategies, undesirable outcomes, and worst-case
scenarios.
• Ethics and fairness: Inclusion of subgroup analyses,
and fairness metrics.
• Human-computer agreement: Report of user agreement with the AI system, reasons for disagreement, and
cases of users changing their mind based on the AI
system.
• Transparency: Inclusion of data and code availability.
• Reliability: Inclusion of uncertainty measures, and
performance against realistic baselines.
• Generalizability: Inclusion of measures taken to reduce
overfitting, and external performance evaluations.
F. TOOLS AND FRAMEWORKS
Understanding the MLOps pipeline and required expertise is just the first step to addressing the problem.
Once this has been accomplished, it is necessary to
create and/or adopt appropriate tooling for transforming
these principles into practice. There are seven broad
categories of MLOps tools as shown in Table 1,
whereby different tools to automate different phase of the
workflows involved in MLOps processes exist. A compiled list of tools within each category is shown in
Table 1.
IV. MLHOps MONITORING AND UPDATING
Once an MLHOps pipeline and required resources are
setup and deployed, robust monitoring protocols are crucial
to the safety and longevity of clinical AI systems. For
example, inevitable updates to a model can introduce various
operational issues (and vice versa), including bias (e.g., a new
hospital policy that shifts the nature of new data) and new
classes (e.g., new subtypes in a disease classifier) [317].
Incorporating expert labels can improve model performance;
however, the time, cost, and expertise required to acquire
accurate labels for very large imaging datasets like those
used in radiology- or histology-based classifiers makes this
difficult [153].
As a result, there exist monitoring frameworks with
policies to determine when to query experts for labels [329].
These include:
• Periodic Querying, a non-adaptive policy whereby
labels are periodically queried in batches according to
a predetermined schedule;
• Request-and-Reverify which sets a predetermined
threshold for drift and queries a batch of labels whenever
the drift threshold is exceeded [318];
• MLDemon which follows a periodic query cycle and
uses a linear estimate of the accuracy based on changes
in the data [100].
A. TIME-SCALE WINDOWS
Monitoring clinical AI systems requires evaluating robustness to temporal shifts. Since the time-scale used can change
the types of shifts detected (i.e., gradual versus sudden shifts),
multiple time windows should be considered (e.g., week,
month). Moreover, it is important to use both 1) cumulative
statistics, which use a single time window and updates at the
beginning of each window and 2) sliding statistics, which
retain previous data and update with new data.
B. APPROPRIATE METRICS
It is critical to choose evaluation and monitoring metrics
optimal for each clinical context. The quality of labels is
highly dependent on the data from which they are derived
and, as such, can possess inherent biases. For instance, sepsis
labels derived from incorrect billing codes will inherently
have a low positive predictive value (PPV). Moreover,
clinical datasets are often imbalanced, consisting of far
fewer positive instances of a label than negative ones.
As a result, measures like accuracy that weigh positive and
negative labels equally can be detrimental to monitoring.
For instance, in the context of disease classification, it may
be particularly important to monitor sensitivity, in contrast
to more time-sensitive clinical scenarios like the intensive
care unit (ICU) where false positives (FP) can have critical
outcomes [23].
C. DETECTING DATA DISTRIBUTION SHIFT
Data distribution shift occurs when the underlying distribution of the training data used to build an ML model differs
from the distribution of data applied to the model during
deployment [236]. When the difference between the probability distributions of these data sets is sufficient to deteriorate
the model’s performance, the shift is considered malignant.
In healthcare, there are multiple sources of data distribution
shifts, many of which can occur concurrently [86], [275].
Common occurrences of malignant shifts include differences
attributed to:
• Institution - These differences can arise when comparing teaching to non-teaching hospitals, governmentowned to private hospitals, or general to specialized
hospitals (e.g., paediatric, rehabilitation, trauma). These
institutions can have differing local clinical practices,
TABLE 1. List of tools supporting MLOps.
TABLE 2. List of open-source tools available on GitHub that can be used for ML monitoring and updating.
resource allocation schemes, medical instruments, and
data-collection and processing workflows that can lead
to downstream variation. This has previously been
reported in Pneumothorax classifiers when evaluated on
external institutions [144].
• Behaviour - Temporal changes in behaviour at the
systemic, physician and patient levels are unavoidable
sources of data drift. These changes include new
healthcare reimbursement incentives, changes in the
standard-of-care in medical practice, novel therapies,
and updates to hospital operational processes. An example of this is the COVID-19 pandemic, which required
changes in resource allocation to cope with hospital bed
shortages [146], [222].
• Patient demographics - Differences in factors like age,
race, gender, religion, and socioeconomic background
can arise for various reasons including epidemiological transitions, gentrification of neighbourhoods
around a health system, and new public health and
immigration policies. Distribution shifts due to demographic differences can disproportionately deteriorate
model performance in specific patient populations. For
instance, although Black women are more likely to
develop breast tumours with poor prognosis, many
breast mammography ML classifiers experience deterioration in performance on this patient population [313].
Similarly, skin-lesion classifiers trained primarily on
images of lighter skin tones may show decreased performance when evaluated on images of darker skin tones
[7], [78].
• Technology - Data shifts can be attributed to changes
in technology between institutions or over time. This
includes chest X-ray classifiers trained on portable
radiographs that are evaluated on stationary radiographs or deteroriation of clinical AI systems across
EHR systems (e.g., Philips Carevue vs. Metavision)
[209].
Although evaluated differently, data shifts are present
across various modalities of clinical data such as medical
images[108] and EHR data [79], [222]. In order to effectively
prevent these malignant shifts from occurring, it is necessary
to perform prospective evaluation of clinical AI systems[332]
in order to understand the circumstances under which they
arise, and to design strategies that mitigate model biases and
improve models for future iterations [320]. Broadly, these
data shifts can be categorized into three groups which can
co-occur or lead to one another:
1) COVARIATE SHIFT
Covariate shift is a difference in the distribution of input
variables between source and target data. It can occur due to
a lack of randomness, inadequate sampling, biased sampling,
or a non-stationary environment. This can be at the level
of a single input variable (i.e. feature shift) or a group of
input features (i.e. dataset shift). Table 3 contains a list of
commonly used methods used for covariate shift detection.
a: FEATURE SHIFT DETECTION
Feature shift refers to the change in distribution between the
source and target data for a single input feature. Feature shift
detection can be performed using two-sample univariate tests
such as the Kolmogorov-Smirnov (KS) test [237]. Publicly
available tools like TensorFlow Extended (TFX) apply univariate tests (i.e., L-infinity distance for categorical variables,
Jensen-Shannon divergence for continuous variables) to perform feature shift detection between training and deployment
data and provide users with summary statistics (Table 2). It is
also possible to detect feature shift while conditioning on
the other features in a model using conditional distribution
tests [149].
b: DATASET SHIFT DETECTION
Dataset shift refers to the change in the joint distribution
between the source and target data for a group of input
TABLE 3. Covariate shift detection methods c: categorical; n: numeric; 2-ST: Two-Sample test.
features. Multivariate testing is crucial because input to
ML models typically consist of more than one variable
and multiple modalities. In order to test whether the
distribution of the target data has drifted from the source
data two main approaches exist: 1) two-sample testing
and 2) model-based. These approaches often work better
on low-dimensional data compared to high-dimensional
data, therefore dimensionality reduction is typically applied
first [237]. For instance, variational autoencoders (VAE) have
been used to reduce chest X-ray images to a low-dimensional
space prior to two-sample testing [272]. In the context
of medical images, including chest X-rays [233], [319],
diabetic retinopathies [44], and histology slides [273],
classifier methods have proven effective. For EHR data,
dimensionality reduction using clinically meaningful patient
representations has improved model performance [209]. For
clinically relevant drift detection, it is important to ensure that
drift metrics correlate well with ground truth performance
differences.
2) CONCEPT SHIFT
Concept shift is a difference in the relationship (i.e., joint
distribution) of the variables and the outcome between the
source and target data. In healthcare, concept shift can arise
due to changes in symptoms for a disease or antigenic
drift. This has been explored in the context of surgery
prediction [35] and medical triage for emergency and urgent
care [121]. Concept Shift Detection: There are three broad
categories of concept shift detection based on their approach.
1) Distribution techniques which use a sliding window to
divide the incoming data streams into windows based
on data size or time interval and that compare the
performance of the most recent observations with a
reference window e.g. ADaptive WINdowing (ADWIN)
[93], [115].
2) Sequential Analysis strategies use the Sequential Probability Ratio Test (SPRT) as the basis for their change
detection algorithms e.g. CUMSUM [32].
3) Statistical Process Control (SPC) methods track
changes in the online error rate of classifiers and trigger
an update process when there is a statistically significant
change in error rate e.g. Drift Detection Method (DDM)
[26], [181].
3) LABEL SHIFT
Label shift is a difference in the distribution of class variables
in the outcome between the source and target data. Label shift
may appear when some concepts are under-sampled or oversampled in the target domain compared to the source domain.
Label shift arises when class proportions differ between the
source and target, but the feature distributions of each class
do not. For instance, in the context of disease diagnosis,
a classifier trained to predict disease occurrence is subject to
drift due to changes in the baseline prevalence of the disease
across various populations.
Label Shift Detection: Label shift can be detected using
moment matching-based estimator methods that leverage
model predictions like Black Box Shift Estimation (BBSE)
[167] and Regularized Learning under Label Shift (RLLS)
[25]. Assuming access to a classifier that outputs the
true source distribution conditional probabilities ps(y|x)
Expectation Maximization (EM) algorithms like Maximum
Likelihood Label Shift (MLLS) can also be used to detect
label shift [97]. Furthermore, methods using bias-corrected
calibration show promise in correcting label shift [15].
D. MODEL UPDATING AND RETRAINING
As the implementation of ML-enabled tools is realized in the
clinic, there is a growing need for continuous monitoring and
updating in order to improve models over time and adapt
to malignant distribution shifts. Retraining of ML models
has demonstrated improved model performance in clinical contexts like pneumothorax diagnosis [144]. However,
proposed modifications can also degrade performance and
introduce bias [164]; as a result it may be preferable to avoid
making a prediction and defer the decision to a downstream
expert [207]. When defining a model updating or retraining
strategy for clinical AI models there are several factors to
consider [308], we outline the key criteria in this section.
1) QUALITY AND SELECTION OF MODEL UPDATE DATA
When updating a model it is important to consider the
relevance and size of the data to be used. This is typically done
by defining a window of data to update the model: i) Fixed
window uses a window that remains constant across time. ii)
Dynamic window uses a window that changes in size due to
an adaptive data shift, iii) Representative subsample uses a
subsample from a window that is representative of the entire
window distribution.
2) UPDATING STRATEGIES
There are several ways to update a model including: i) Model
recalibration is the simplest type of model update, where
continuous scores (e.g. predicted risks) produced by the
original model are mapped to new values [57]. Some
common methods to achieve this include Platt scaling [231],
temperature scaling, and isotonic regression [212]. ii) Model
updating includes changes to an existing model, for instance,
fine-tuning with regularization [154] or model editing where
pre-collected errors are used to train hypernetworks that can
be used to edit a model’s behaviour by predicting new weights
or building a new classifier [203]. iii) Model retraining
involves retraining a model from scratch or fitting an entirely
different model.
3) FREQUENCY OF MODEL UPDATES
In practice, retraining procedures for clinical AI models have
generally been locked after FDA approval [155] or confined
to ad-hoc one-time updates [114], [290]. The timing of when
it is necessary to update or retrain a model varies across use
case. As a result, it is imperative to evaluate the appropriate
frequency to update a model. Strategies employed include:
i) Periodic training on a regular schedule (e.g. weekly,
monthly). ii) Performance-based trigger in response to a
statistically significant change in performance. iii) Databased trigger in response to a statistically significant data
distribution shift. iv) Retraining on demand is not based on
a trigger or regular schedule, and instead initiated based on
user prompts.
4) CONTINUAL LEARNING
Continual learning is a strategy used to update models when
there is a continuous stream of input data that may be subject
to changes over time without forgetting knowledge obtained
from previous tasks. Prior to deployment, it is crucial
to simulate the online learning procedure on retrospective
data to assess robustness to data shifts [55], [219]. When
models are retrained on only the most recent data, this can
result in ‘‘catastrophic forgetting’’ [155], [296], in which
the integration of new data into the model can overwrite
knowledge learned in the past and interfere with what the
model has already learned [153]. Contrastingly, procedures
that retrain models on all previously collected data can fail
to adapt to important temporal shifts and are computationally
expensive. In healthcare contexts like radiology, where the
labelling of new data can be a time-consuming bottleneck
multi-armed bandits can be utilized to select important
samples or batches of data for retraining [102], [110], [228],
[330].
Strategies for continual learning can broadly be categorized into: 1) Parameter isolation where changes to
parameters that are important for the previous tasks are
forbidden e.g. Local Winner Takes All (LWTA), Incremental Moment Matching (IMM) [289]; 2) Regularization
methods which builds on the observation forgetting can
be reduced by protecting parameters that are important for
the previous tasks e.g. elastic weight consolidation (EWC),
Learning Without Forgetting (LWF); and 3) Replay-based
approaches that retain some samples from the previous
tasks and use them for training or as constraints to reduce
forgetting e.g. episodic representation replay (ERR) [72].
Evaluation of continual learning methods on ICU data
indicates replay-based methods achieve more stable longterm performance, compared to regularization and rehearsal
based methods [21]. For chest X-ray classification, Joint
Training (JT) has demonstrated superior model performance,
with LWF as a promising alternative in the event that training
data is unavailable at deployment [156]. For sepsis prediction
using EHR data, a joint framework leveraging EWC and ERR
has been proposed [17].
5) DOMAIN GENERALIZATION AND ADAPTATION
Broadly, domain generalization and adaptation methods are
used to improve clinical AI model stability and robustness
to data shifts by reducing distribution differences between
training and test data [105], [323]. However, it is critical
to evaluate several methods over a range of metrics, as the
effectiveness of each method varies based on several factors
including the type of shift and data modality [315].
• Data-based methods perform manipulations based
on the patient data to minimize distribution shifts.
This can be done by re-weighting observations during
training based on the target domain [147], upsampling
informative training examples [169] or leveraging a
combination of labeled and pseudo-labeled [162].
• Representation-based methods focus on achieving
a feature representation such that the source classifier performs well on the target domain. In clinical data this has been explored using strategies
including invariant risk minimization (IRM), distribution matching (e.g. CORAL) and domain-adversarial
adaptation networks (DANN). DANN methods have
demonstrated a reduction on the impact of data
shift on cross-institutional transfer performance for
diagnostic prediction [325]. However, it has been
shown that for clinical AI models subject to real
life data shifts, in contrast to synthetic perturbations,
empirical risk minimization outperforms domain generalization and unsupervised domain adaptation methods
[107], [323].
• Inference-based methods introduce constraints on the
optimization procedure to reduce domain shift [147].
This can be done by estimating a model’s performance on the ‘‘worst-case’’ distribution [276] or
constraining the learning objective to enforces closeness between protected groups [263]. Batch normalization statistics can also be leveraged to build
models that are more robust to covariate shifts
[261].
6) DATA DELETION AND UNLEARNING
In healthcare there are two primary reasons for wanting to
remove data from models. Firstly, with the growing concerns
around privacy and ML in healthcare, it may become necessary to remove patient data for privacy reasons. Secondly,
it may also be beneficial to a model’s performance to delete
noisy or corrupted training data [38]. The naive approach
to data deletion is to exclude unwanted samples and retrain
the model from scratch on the remaining data, however this
approach can quickly become time consuming and resourceintensive [123]. As a result, more sophisticated approaches
have been proposed for unlearning in linear and logistic models [123], random forest models [39], and other non-linear
models [106].
7) FEEDBACK LOOPS
Feedback loops that incorporate patient outcomes and clinician decisions are critical to improving outcomes in future
model iterations. However, retraining feedback loops can
also lead to error amplification, and subsequent downstream
increases in false positives [5]. As a result, it is important
to consider model complexity and choose an appropriate
classification threshold to ensure minimization of error
amplification [5].
V. RESPONSIBLE MLHOps
AI has surged in healthcare, out of necessity and/or
curiosity [220], [320], but many issues remain unresolved,
such as bias in clinical data, the opacity of AI models, and
potential malicious attacks that damage or pollute the AI/ML
systems[22], [258]. In response, responsible AI and trustworthiness have together become a growing area of study [197],
[293]. Responsible AI, or trustworthy MLOps, is defined as
an ML pipeline that is fair and unbiased, explainable and
interpretable, secure, private, reliable, robust, and resilient
to attacks [243]. In healthcare, trust is critical to ensuring a
meaningful relationship between the healthcare provider and
patient [69].
In recent years, responsible and trustworthy AI have gained
a lot of attention in general as well as for healthcare due
to its implications on society [243]. Trustworthiness has
been defined in different ways [243], all emphasizing qualities that make the system robust, unbiased, generalizable,
reproducible, transparent, explainable, and secure. However,
the lack of standardized practices for applying, explaining,
and evaluating trustworthiness in AI for healthcare makes
this very challenging [243]. In this section, we discuss
components of responsible and trustworthy AI [157] and
how we can incorporate all these qualities into the MLHOps
pipeline.
Ethics in Healthcare: Ethics in healthcare primarily
consists of the following criteria [292]:
1) Nonmaleficence: Do not harm the patient.
2) Beneficence: Act to the benefit of the patient.
3) Autonomy: The patient (when able) should have the
freedom to make decisions about their body. More
specifically, the following aspects should be taken care
of:
• Informed Consent: The patient (when able) should
give informed consent for any medical or surgical
procedure, or for research.
• Truth-telling: The patient (when able) should receive
full disclosure to his/her diagnosis and prognosis.
• Confidentiality: The patient’s medical information
should not be disclosed to any third party without the
patient’s consent.
4) Justice: Ensure fairness to the patient.
To supplement these criteria, guiding principles drawn
from surgical settings [168], [252] include:
5) Rescue: A patient surrenders to the healthcare
provider’s expertise to be rescued.
6) Proximity: The emotional proximity to the patient
should be limited to maintain self-preservation and
stability in case of any failure.
7) Ordeal: A patient may have to face an ordeal
(i.e., go through painful procedures) in order to be
rescued.
8) Aftermath: The physical and psychological aftermath
that may occur to the patient due to any treatment must
be acknowledged.
9) Presence: An empathetic presence must be provided to
the patient.
While some of these criteria relate to the humanity of the
healthcare provider, others relate to the following topics in
ML models:
■ Fairness involves the justice component in the healthcare domain [54].
■ Interpretability & explainability relate to explanations
and a better understanding of the ML models’ decisions,
which can help in achieving nonmaleficence, beneficence, informed consent, and truth-telling principles in
healthcare. Interpretability can help identify the reasons
for a given model outcome, which can help inform
healthcare providers and patients on how to respond
accordingly [200].
■ Privacy and security relate to confidentiality. [139].
■ Reliability, robustness, and resilience addresses
rescue [251].
We discuss these concepts further in Sections V-A, V-B, V-C
and V-D.
A. BIAS & FAIRNESS
Bias in healthcare manifests as differences in model performance against or in favour of a sub-population, for
a given task. For instance, disproportionate performance
differences for disease diagnosis in Black versus White
patients [267]. The fairness of AI-based decision support
systems has been studied generally in a variety of applications including occupation classifiers [70], criminal risk
assessments algorithms [62], recommendation systems [80],
facial recognition algorithms [41], search engines [95], and
risk score assessment tools in hospitals [214]. In recent
years, the topic of fairness in AI models in healthcare
has received a lot of attention [53], [152], [214], [267],
[268], [307].
Different surveys, tests, and studies have found the following types of biases (conscious or unconscious) common in
healthcare [189]:
1) Racial bias e.g., Black, Hispanic, and Native American
physicians are underrepresented [218]. According to one
study, white males from the upper classes are preferred
by the admission committees [45] (although some other
sources suggest the opposite45).
2) Gender bias e.g., professional women in healthcare
being less likely to be invited to give talks [198], to be
introduced using professional titles [85], to experience
harassment or exclusion, to receive insufficient support
at work or negative comparisons with male colleagues,
and to be perceived as weak & less competitive [165],
[280].
3) Gender minority bias e.g., LGBTQ people receive
lower quality healthcare [250] and faced challenges to
get jobs in healthcare [257].
4) Disability bias e.g., people with disabilities receive
limited accessibility supports to all facilities and have
to work harder to be feel validated or recognized [196].
However, it should be noted that in some cases, defining
AI fairness is context- and problem-dependent. For instance,
if we build an AI model to support decision-making for
disease diagnosis with the goal of using it in the clinic,
then it is critical to ensure equal opportunity in the model is
provided; i.e., patients from different races should have equal
opportunity to be accurately diagnosed [267]. However, if an
AI model is to be used to triage patients, then ensuring the
system does not underdiagnose unhealthy patients of a certain
group may be of greater concern compared to the specific
disease itself because the patient will lose access to timely
care [268].
Next, we discuss various sources of bias in the MLHOps
pipeline and recommend best practices for mitigating them.
1) DATA & LABELING BIAS
Data and labeling bias in healthcare arise when training data
or label assignments misrepresent or under-represent specific
patient groups, often due to cultural sensitivities or data
collection methods [77]. The causes and interventions are
outlined below:
I) Causes
The process of a responsible and trustworthy MLOps
pipeline starts with data collection and preparation and
the impact of biased or polluted data propagates through
all the subsequent steps of the pipeline [54], [91]. This
can be even more important and challenging in the
healthcare domain due to the privacy and sensitivity of
the data [24]. In healthcare, data can be acquired through
multiple sources [285], which increases the chance of
the data being polluted by bias. Bias can concern, for
example, race [313], gender, sexual orientation, gender
identity, and disability. A lack of fairness in clinical AI
systems may be a result of various contributing causes
discussed below:
• Inclusion and exclusion: One of the causes of data
bias is the inclusion or exclusion of specific groups.
For instance, the Chest X-ray dataset [304] was
gathered in a research hospital that does not routinely
conduct diagnostic and treatment procedures.44 This
dataset therefore includes mostly critical cases, and
few patients at the early stages of diagnosis, resulting
in a lack of diversity in the dateset.
• Insufficient sample size: Insufficient sample sizes of
under-represented groups can also result in unfairness
[99]. For instance, patients of low socioeconomic
status may use healthcare services less, which reduces
their sample size in the overall dataset, resulting in
an unfair model [41], [53], [323]. In another instance,
an algorithm that can classify skin cancer [82]
with high accuracy will not be able to generalize
to different skin colors if similar samples have
not been represented sufficiently in the training
data [41].
• Missing essential representative features: Sometimes, essential representative features are missed
or not collected during the dataset curation process,
which prohibits downstream fairness analyses. For
instance, if the patient’s race has not been recorded,
it is not possible to analyze whether a model
trained on that data is fair with respect to that
race [268], which can generate discrimination and
reduce transparency [52].
• Social bias reflection on labels: Biases in healthcare systems widely reflect existing biases in society [188], [277], [298]. For instance, race and
sex biases exist in COPD underdiagnosis [188],
in medical risk score analysis (whereby there exists
a higher threshold for Black patients to gain access to
TABLE 4. List of tools specific to fairness in health.
clinical resources) [298], and in the time of diagnosis
for cardiovascular disease (whereby female patients
are diagnosed much later compared to the male
patients with similar conditions) [277]. These biases
are reflected in the labels used to train clinical AI
systems and, as a result, the model will learn to
replicate this bias.
• Bias of automatic labeling: Due to the high cost
and labour-intensive process of acquiring labels for
healthcare data, there has been a shift away from
hand-labelled data, towards automatic labelling [42],
[122], [130]. For instance, instead of expert-labeled
radiology images, natural language processing (NLP)
techniques are applied to radiology reports in order
to extract labels. This presents concerns as these
techniques have shown racial biases, even after they
have been trained on clinical notes [324]. Therefore, using NLP techniques for automatic labeling
may sometimes amplify the overall bias of the
labels [268].
II) Interventions
Bias in healthcare data can be mitigated against by
increasing diversity in data, e.g., by including underrepresented minorities (URMs), which can lead to better
outcomes [189]. Debiasing during data collection can
include:
a) Identifying & acknowledging potential real-world
biases: Bias in healthcare is introduced long before
the data collection stage. Although increasingly less
common in many countries,45 bias can still occur
in medical school admission, job interviews, patient
care, disease identification, research samples, and
case studies. Such biases lead to the dominance
of people from certain communities [189] or ingroup vs. out-group bias [101], which can result in
stereotyped and biased data generation and hence
biased data collection.
Bias can be unconscious or conscious [87], [189].
Unconscious bias stems from implicit or unintentional associations outside conscious awareness resulting from stereotypical perceptions and
experiences. On the other hand, conscious bias
is explicit and intentional and has resulted in
abuse and criminal acts in healthcare; e.g., the
Tuskegee study of untreated Syphilis in black men
demonstrated intentional racism [88]. Both conscious
and unconscious biases damage the validity of the
data. Since conscious bias is relatively more visible,
it is openly discouraged not only in healthcare but also
in all areas of society. However, unconscious bias is
more subtle and not as easy to identify. In most cases,
unconscious bias is not even known to the person
suffering from it.
Various tests identify the existence of unconscious
bias, such as the Implicit Association Test (IAT),
and have been reported to be useful. For example,
Race IAT results detected unintentional bias in 75%
of the population taking the test [28]. While debate
continues regarding the degree of usefulness of
these tests [37], they may still capture some subtle
human behaviours. Some other assessment tools (e.g.,
Diversity Engagement Survey (DES) [224]) have
also been built for successfully measuring inclusion
and diversity in medical institutes. According to
Marcelin et al. [189], the following measures can help
in reducing unintentional bias:
i) Using IAT to identify potential biases in admissions or hiring committee members in advance.
ii) Promoting equity, diversity, inclusion, and accessibility (EDIA) in teams. Including more people
from underrepresented minorities (URM) in the
healthcare profession, especially in admissions
and hiring committees.
iii) Conducting and analyzing surveys to keep track
of the challenges faced by URM individuals due
to the biased perception of them.
iv) Training to highlight the existence and need for
mitigation of bias.
v) Self-monitoring bias can be another way to
incorporate inclusion and diversity.
b) Debiasing during data collection and annotation:
In addition to human factors, we can take steps to
improve the data collection process itself. In this
regard, the following measures can be taken [171]:
i) Investigating the exclusion: In dataset creation,
an important step is to carefully investigate which
patients are included in the dataset. An exclusion
criterion in dataset creation may be conscious
and clinically motivated, but there are many
unintentional exclusion criteria that are not very
well visible and enforce biases. For instance,
a dataset that is gathered in a research hospital that
does not routinely provide standard diagnostic and
treatment services and select the patients only
because they have an illness being studied by
the Institutes have a different type of patients
compared to clinical hospitals that do not have
these limitations [268]. Alternatively, whether the
service delivered to the patient is free or covered
by insurance would change the distribution of the
patients and infect biases into the resulting AI
model [267].
ii) Annotation with explanation: Adding justification for choosing the label by the human
annotators not only helps them identify their
own unconscious biases but also can help in
setting standards for unbiased annotations and
avoid any automatic association and stereotyping
(e.g., high prevalence HIV in gay men led to
under-diagnosis of this disease in women and
children [189]. Moreover, these explanations can
be a good resource for training explainable AI
models [306].
iii) Data provenance: This involves tracking data
lineage through the data source, dependencies,
and data collection process. Healthcare data can
come from multiple sources which increases the
chances of it being biased [48]. Data provenance improves data quality, integrity, audibility, and transparency [312]. Different tools for
data provenance are available including Fast
Healthcare Interoperability Resources (FHIR)
[259], Atmolytics [312], and blockchain-based
system for managing EHR data [191].
iv) Data-sheet: Often, creating a dataset that represents the full diversity of a population is
not feasible, especially for very multi-cultural
societies. Additionally, the prevalence of diseases among different sub-populations may be
different [268]. If it is not possible to build an
ideal dataset with the above specifications, the
data needs to be delivered by a data-sheet. The
data-sheet is meta-data that helps to analyze and
specify the characteristics of the data, clearly
explain exclusion and inclusion criteria, detail
demographic features of the patients, and statistics
of the data distribution over sub-populations,
labels and features.
c) Data pre-processing: Data pre-processing involves
techniques, such as data quality assurance and performing data anonymization, which may help reduce
bias in certain cases. We discuss these techniques in
more detail below.
i) Data quality assurance: Sendak et al. [264]
argued that clinical researchers choose data for
research very carefully but the machine learning
community in healthcare does not follow this
practice. To overcome this gap, they suggest
that data points are identified by the clinicians
and extracted into a project-specific data store.
After this, a three-step framework is applied:
(1) use different measures for data pre-processing
to ensure the correctness of all data elements (e.g,
converting each lab measurement to the same
unit), (2) ensure completeness, conformance,
plausibility, and possible data shifts, and (3)
adjudicate the data with the clinicians.
ii) Data anonymization: Due to the sensitivity of
healthcare data preparation, data anonymization
should minimize the chances of it being deanonymized. Olatunji et al. [217] provide a
detailed overview of data anonymization models
and techniques in healthcare such as k-anonymity,
k-map, l-diversity, t-closeness, δ-disclosure
privacy, β-likeness, δ-presence, and (ϵ, δ)-
differential privacy. To avoid data leakage, many
tools for data anonymization and its evaluation
tools [297] such as SecGraph [126], ARX- tool
for anonymizing biomedical data [234], Amnesia46 [282], PySyft [254], Synthea [299] and
Anonimatron47 (open-source data anonymization
tool written in Java) can be incorporated in the
MLHOps pipeline.
iii) Removing subgroups indicators. Changing the
race of the patients can have a dramatic impact
on the outcome of an algorithm that is designed
to fill a prompt [324]. Therefore, the existence of
race attributes in the text can decrease the fairness
of the model dramatically. In some specific
problems, removing subgroup indicators such as
the sex of a job candidate from their application
has shown to have minimal influence on classifier
accuracy while improving the fairness [70]. This
method is applicable mostly in text-based data
where sensitive attributes are easily removable.
As a preprocessing step, one can estimate the
effect of keeping or removing such sensitive
attributes on the overall accuracy and fairness of
a developed model. At the same time, it is not
always possible to remove the sensitive attributes
from the data. For example, AI models can predict
patient race from medical images, but it is not yet
clear how they can do it [305]. In one study [305],
researchers did not provide the patient race during
model training, but they also could not find a
particular patch or region in the data for which AI
failed to detect race by removing that part.
iv) Differential privacy: Differential privacy [68]
aims to provide information about inherent groups
while withholding information about the individuals. Many algorithms and tools have been
developed for this, including CapC [60] and
PySyft [254]. However, it should be noted that
in their paper Suriyakumar et. al. [278] show
that differential privacy, may lead to a reduction
in accuracy that may disproportionately impact
smaller groups.
2) ALGORITHMIC BIAS
Algorithmic bias refers to systematic and unfair discrimination in the outcomes produced by algorithms [311].
I) Causes
a) Unfair objective functions: The initial objective
used in developing an ML approach may not consider
fairness. This does not mean that the developer
explicitly (or implicitly) used an unfair objective
function to train the model, but the oversimplification
of that objective can lead to downstream issues.
For example, a model designed to maximize
accuracy across all populations may not inherently
provide fairness across different sub-populations
even if it reaches state-of-the-art performance
on average, across the whole population [267],
[268].
b) Incorrect presumptions: In some instances, the
objective function includes incorrect interpretations
of features, which can lead to bias. For instance,
a commercial algorithm used in the USA used health
costs as a proxy for health needs [214]; however, due
to financial limitations, Black patients with the same
need for care as White patients often spend less on
healthcare and therefore have a lower health cost. As a
result, the model falsely inferred that Black patients
require less care compared to White patients because
they spend less [214]. Additionally, patients may be
charged differently for the same service based on their
insurance, suggesting cost may not be representative
of healthcare needs.
c) Limited computational resources: Not all centers
have enough labeled data or computational resources
to train ML models ‘from scratch’ and must use
pretrained models for inference or transfer learning.
If the original model has been trained on biased (or
differently distributed) data, it will unfairly influence
the outcome, regardless of the quality of the data at
the host center [242].
II) Interventions
Algorithmic fairness [92], [204], [226], [311] attempts
to ensure the unbiased output across the available
classes. Here, we discuss how we can overcome this
challenge at different stages of model training [204],
[311].
a) Pre-processing
• Choice of sampling, data augmentation & synthetic data generation: Making sure that the
dataset is balanced (having approximately an
equal number of instances from each class) and
all the classes get equal representation in the
dataset using simple under- or over-sampling
methods [311]. This can also be done by data
augmentation [90], [201] to improve the counterfactual fairness by counterfactual text generation
and using it to augment data. Augmentation methods include Synthetic Minority Oversampling
Technique (SMOTE) [49] and Adaptive Synthetic
Sampling (ADASYN) [116]. Since synthetic
samples may not be universally beneficial for
the healthcare domain, acquiring more data and
undersampling may be the best strategy [311].
In contrast, some studies on synthetic data
generation in healthcare have demonstrated its
effectiveness [77].
• Causal fairness using data pre-processing:
Causal fairness is achieved by reducing the impact
of protected or sensitive attributes (e.g., race
and gender) on predicted variables and different
methods have been developed to accomplish
this [92], [310]. Kamiran et al. [134] proposed
‘‘massaging the data’’ before using traditional
classification algorithms.
• Re-weighing: In a pre-processing approach, one
may re-weight the training dataset samples or
remove features with high correlation to sensitive attributes as well as the sensitive attribute
itself [135], learning representations that are
relatively invariant to sensitive attribute [180].
One might also adjust representation rates of
protected groups and achieve target fairness
metrics [47], or utilize optimization to learn a data
transformation that reduce discrimination [43].
b) In-processing
• Adversarial learning: It is also possible to enforce
fairness during model training, using adversarial
debiasing [244], [303], [321]. Adversarial learning refers to the methods designed to intentionally
confound ML models during training, through
deceptive or misleading inputs, to make those
models more robust. This technique has been
used in healthcare to create robust models [138],
and for bias mitigation, by intentionally inputting
biased examples [159], [225].
• Prejudice remover: Another important aspect is
prejudice injected into the features [136]. Prejudice can be (a) Direct prejudice: using a protected
attribute as a prediction variable, (b) Indirect
prejudice: statistical dependence between protected attributes and prediction variables, and (c)
Latent prejudice: statistical dependence between
protected attributes and non-protected attributes.
Kamishaima et al. [136] proposed a method to
remove prejudice using regularization. Similarly,
Grgic et al. [104] introduced a method using
constraints for classifier optimization objectives
to remove prejudice.
• Enforcing fairness in the model training: Fairness
can also be enforced by making changes to
the model through constraint optimization [177],
modifying loss functions to penalize deviation
from the general population for subpopulations [227], regularizing the loss function to
minimize mutual information between feature
embedding and bias [141], or adding regularizer to identify and treat latent discriminating
features [136].
• Up-weighing: It is possible to improve the
outcome on worst case group by up-weighting
the groups with the largest loss [193], [256],
[322]. However, all these methods need awareness
about the membership of the instance to sensitive
attributes. There are also group un-aware methods
where they try to weigh each sample with an
adversary that tries to maximize the weighted
loss [150], or trains an additional classier that
up-weights samples classified incorrectly in the
last training step [169].
• Resource efficiency: Resource-efficient methods
can be utilized to address the impact of biased data
in transfer learning when computational resources
are limited. However, many such approaches
prioritize model performance over bias reduction [56], [271]. Recently, model editing and
machine unlearning techniques have been used
to reduce bias by selectively updating parameters
without the need for full model fine-tuning,
offering a resource-efficient approach to mitigating social bias [74]. Similar strategies could be
explored for applications in healthcare.
c) Post-processing: The post-processing fairness mitigation approaches may target post-hoc calibration of
model predictions. This method has shown an impact
in bias mitigation in both non-healthcare [113], [232]
and healthcare [142] applications.
3) FLAWS IN BIAS EVALUATION
To evaluate the fairness of a model, we need to decide which
fairness metric to use and what sensitive attributes to consider
in our analysis.
I) Causes
a) Fairness metrics: Various fairness metrics have
been proposed in the literature [62], [113], utilizing
different fairness criteria and recommending error
rate balancing across subgroups[65], [322]. However,
it is not always possible to satisfy multiple fairness
constraints concurrently [268]. Jon Kleinberg et al.,
[145] showed that three fairness conditions evaluated
could not be simultaneously satisfied. As a result,
a trade-off between the different notions of fairness
is required, or a single fairness metric can be chosen
based on domain knowledge and the given clinical
application.
b) Sensitive attributes: Sensitive attributes are protected groups that we want to consider when evaluating the fairness of an AI model. Sex and race
are two commonly used sensitive attributes [267],
[268], [322], [324]. However, a lack of fairness in an
AI system with respect to other sensitive attributes
such as age [267], [268], socioeconomic status, [267],
[268], [324], and spoken language [324] are also
important to consider.
II) Interventions
a) Standardized evaluation framework: Research
should focus on developing standardized evaluation
frameworks that include metrics and benchmark
datasets for assessing the bias in the models[11], [51],
[94].
b) Regulatory guidelines:Regulatory guidelines should
be established to ensure and prioritize bias evaluation
[59], [195].
c) Patient input: Human evaluation, particularly
patient evaluation of bias, can aid in developing
best practices and metrics for bias assessment
[58], [151].
d) Interpretability & explainability: Making the models interpretable and explainable, can help in evaluating bias, ultimately reducing it and allowing for more
effective application of mitigation approaches [14].
Several software tools and libraries for fairness checks
in healthcare are available, as listed in Table 4, enabling
developers and end users to assess the fairness of AI model
outcomes.
B. INTERPRETABILITY & EXPLAINABILITY
In recent years, interpretability has received a lot of interest
from the ML community [192], [205], [281]. In machine
learning, explainability is defined as the ability to explain the
rationale for an ML model’s predictions in terms that a human
can understand [76] and interpretability refers to a detailed
understanding of the model’s internal representations, a priori of any decision. After other research in this area [190],
we use interpretability and explainability interchangeably.
Interpretability is not a pre-requisite for all AI systems [76], [205], including in low-risk environments (in
which miscalculations have very limited consequences) and
in well-studied problems (which have been tested and
validated extensively according to robust MLOps methods).
However, interpretability can be crucial in many cases,
especially for systems deployed in the healthcare domain [2],
[98], [176], [200], [243], [274].
In their systematic review, Jung et al. [132] categorized
interpretability & explainability objectives in healthcare
into five categories: (1) explainability to evaluate AI, (2)
explainability to justify AI, (3) explainability to improve AI,
(4) explainability to learn from AI, and (5) explainability to
manage AI. While the first four categories are well-studied,
the last category focusing on explainability deployment in
clinical settings, remains under-explored and requires further
investigation.
1) IMPORTANCE OF INTERPRETABILITY
The need for interpretability arises from the incompleteness
of the problem where system results require an accompanying
rationale. Interpretability applied to an ML model can be
useful for the following reasons:
• Trust: Interpretability enhances trust when all components are well-explained. This builds an understanding
of the decisions made by a model and may help integrate
it into the overall workflow.
• Reliability & robustness: Interpretability can help
in auditing ML models, further increasing model
reliability.
• Privacy & security: Interpretability can be used to
assess if any private information is leaked from the
results. While some researchers claim that interpretability may hinder privacy [112], [270] as the interpretable
features may leak sensitive information, others have
shown that it can help make the system robust against
adversarial attacks [160], [326].
• Fairness: Interpretability can help in identifying and
reducing biases discussed in Sec. V-A. However, the
quality of these explanations can differ significantly
between subgroups and, as such, it is important to test
various explanation models in order to carefully select
an equitable model with high overall fidelity [27].
• Better understanding and knowledge: A good interpretation of the model can lead to the identification of
the factors that most impact the model. This can also
result in a better understanding of the use case itself and
enhance knowledge in that particular area.
• Causality: Interpretability gives a better understanding
of the model decisions and the features and hence can
help to identify causal relationships of the features [46].
2) INTERPRETABILITY METHODS
Many methods have been developed for better interpretability
in ML, such as explainable AI for trees [183], Tensorflow
Lattice,48 DeepLIFT [158], InterpretML [213], LIME [247],
and SHAP [184]. Methods for interpretability are usually
categorized as:
1) Model-based
• Model-specific: Model-specific interpretability can
only be used for a particular model. Usually, this type
of interpretability uses the model’s internal structure
to analyze the impact of features, for example.
• Model-agnostic: Interpretability is not restricted to
a specific machine learning model and can be used
more generally with several.
2) Complexity-based
• Intrinsic: Relatively simple methods, such as
height-bound decision trees, are easier for humans to
understand.
• Post-hoc: After the model has produced output,
interpretation proceeds for more complex methods.
3) Scope-based
• Locally interpretable: Interprets individual or
per-instance predictions of the model.
• Globally interpretable: Interprets the model’s overall prediction set and provides insight into how the
model works in general.
4) Methodology-based approach
• Feature-based: Methods that interpret the models based on the impact of the features on that
model, for example, weight plot, feature selection,
etc.
• Perturbation-based: Methods that interpret the
model by perturbing the settings or features of the
model. For example, LIME [247], SHAP [184] and
anchors.
• Rule-based: Methods that apply rules on features to
identify their impact on the model e.g., MUsE [73],
and decision trees.
• Image-based: Methods where important inputs are
shown using images superimposed over the input e.g.,
saliency maps [8].
Interpretability methods in healthcare have been applied
across various use cases such as [255]: for diagnostic decisions and patient monitoring, decision trees, and
rule-based systems are used to provide insights; disease
prediction and risk stratification benefit from anchors
and counterfactuals, clarifying influential features and
alternative outcomes; clinical trials and radiology leverage SHAP and LIME to highlight impactful data points
and crucial image areas, aiding researchers, and radiologists; AI-assisted surgery, augmented reality overlays
offer interpretable guidance; while drug discovery uses
feature importance to prioritize key factors. In particular,
Abdullah et al. [2] reported that interpretability methods
(e.g., decision trees, LIME, SHAP) have been applied to
extract insights into different medical conditions including
cardiovascular diseases, eye diseases, cancer, influenza,
infection, COVID-19, depression, and autism. Similarly,
Meng et al. [200] performed interpretability of deep learning
mortality prediction models and fairness analysis on the
MIMIC-III dataset [129], showing connections between
interpretability methods and fairness metrics. Nasarian et al.
[208] discuss the use of explainability in various IoT-based
medical devices to enhance user trust and transparency.
Additionally, in the era of large language models, many
medical language models are now being developed to provide
interpretable and explainable results [172], [314]. These
approaches ensure ML insights are accessible and clinically
valuable.
3) CHALLENGES AND RECOMMENDATIONS
While the use of interpretability and explainability is widely
desired in healthcare, it comes with a variety of challenges
that must be addressed before becoming the part of MLHOps
pipeline, such as:
• Accuracy vs. explainability: The effectiveness of
explainability, especially in healthcare, is widely
debated due to the complexity involved and persistent
low confidence in ML for critical decisions [166],
[185], [187], [288]. ML models can vary, from highaccuracy black-box models to gray-box models with
average performance and white-box models with lower
accuracy [208], which essentially means a trade-off
between accuracy and explainability of the models.
Some argue that clinicians and patients need insight
into model decision factors, while others prioritize
model accuracy over explainability, given the potential
limitations of explainability methods.
Recommendations: Striking a balance is essential,
as accuracy is crucial in healthcare, but explainability
also offers benefits like bias identification [89], [173],
[255]. The trade-off should be openly discussed with
clinicians and end-users to fully evaluate the clinical and
human implications and establish priorities accordingly
[208], [255].
• User-friendly explainability: In healthcare, the level of
explainability must be tailored to different stakeholders
including AI regulators, machine learning practitioners,
clinicians, and patients, to be effective [166], [185],
[208]. Clinicians with their specific medical expertise,
may require explanations that are of clinical relevance. Patients’ motivation, on the other hand, is to
understand their specific condition, which differs from
the clinician’s motivation. Therefore, explainability in
healthcare should be adaptable, offering different levels
of explanations to address the unique understanding,
requirements, and situations of the stakeholders without
information overload. Research has shown explainability in healthcare has primarily targeted clinicians,
highlighting the need to enhance explanations for
patients [132].
Recommendations: The focus should be finding ways
to generate user-friendly explanations at varying levels.
ML practitioners and clinicians can collaborate to
develop such models that can offer clinically relevant
insights, while patients can be given simple text
summaries generated based on complex explanations.
Nasarian et al. [208] propose 3-level interpretability
process i.e., pre-processing interpretability, interpretable
processing, and post-processing interpretability for
user-focused explanations.
• Evaluating explainability: Although explainability has
been explored across domains, standardized evaluation methods remain challenging. Current approaches
include human evaluation and metrics-based evaluation,
each has limitations: human evaluation is often biased,
while metrics lack the complexity needed for comprehensive assessment [13]. According to Jung et al.
[132], in healthcare, the quality of explanations is
commonly evaluated based on criteria such as fidelity,
explanatory power, interpretability, comprehensibility,
plausibility, required effort, privacy, and fairness;
however, generalizability remains under-assessed. The
effectiveness of explanations is measured through
factors like mental model alignment, user satisfaction,
trust assessment, task performance, and correctability.
Similarly, research by Nasarian et al. [208] proposes
using customized scales suited to the unique dimensions
of each evaluation.
Recommendations: Explainability requirements should
be clearly defined early on, tailored to each user
category, and aligned with relevant regulatory standards. Metrics should be selected accordingly and
complemented with human evaluation to provide a
comprehensive assessment. User feedback gathered
through surveys and interviews, can further enhance
the evaluation by identifying practical aspects of interpretability and its usefulness in real-world applications.
• Over-reliance on explainability: Explainability in
healthcare ML models is essential, but excessive detail
provided by the models can lead to over-reliance on
the explanations, which may be error-prone and result
in harmful outcomes [166], [208]. While models can
effectively process data and offer insights, they are
meant to only complement, not replace, the expertise of
the domain experts like clinicians.
Recommendations: Model limitations should be communicated to the users and they should be trained to
use the information for assistance rather than a primary
decision-maker.
C. PRIVACY & SECURITY
While digitizing healthcare has led to centralized data and
improved access for healthcare professionals, it has also
increased risks to data security and privacy [210]. After
previous work [3], privacy is the individual’s ability to
control, interact with, and regulate their personal information,
and security is systemic protection of data from leaks or
cyberattacks. To ensure privacy and security, the following
requirements should be met [210]:
• Authentication: Strong authentication mechanisms for
accessing the system.
• Confidentiality: Access to data and devices should be
restricted to authorized users.
• Integrity: Integrity-checking mechanisms should be
applied to restrict any modifications to the data or to the
system.
• Non-repudiation: Logs should be maintained to monitor the system. Access to those logs should be restricted
and avoid any tampering.
• Availability: Quick, easy, and fault-tolerant availability
should be ensured at all times.
• Anonymity: Anonymity of the device, data, and communication should be guaranteed.
• Device unlinkability: An unauthorized person should
not be able to establish a connection between data and
the sender.
• Auditability and accountability: It should be possible
to trace back the recording time, recording person, and
origins of the data to validate its authenticity.
1) TYPES OF THREATS
Violation of privacy & security can occur either due to human
error (unintentional or non-malicious) or an adversarial attack
(intentional or malicious).
1) Human error: Human error can cause data leakage through the carelessness or incompetence of
authorized individuals. Most of the literature in this
context [84], [163] divides human error into two
types:
• Slip: the wrong execution of correct, intended
actions; e.g., incorrect data entry, forgetting to
secure the data, giving access of information
to unauthorized persons using the wrong email
address.
• Mistake: the right execution of incorrect, unintended
actions; e.g., collecting data that is not required, using
the same password for different systems to avoid
password recovery, giving access of information to
unauthorized persons assuming they can have access.
While people dealing with data should be trained to
avoid such negligence, some researchers have suggested
policies, frameworks, and strategies such as error
avoidance, error interception, or error correction to
prevent or mitigate these issues [84], [163].
2) Adversarial attacks: A primary risk for any digital data
or system is from adversarial attackers [109] who can
damage, pollute, or leak information from the system.
An adversarial attacker can attack in many ways; e.g.,
they can be remote or physically present, they can access
the system through a third-party device, or they can be
personified as a patient [210]. The most common types
of attacks are listed below.
• Hardware or software attack: Modifying the hardware or software to use it for malicious purposes.
• System unavailability: Making the device or data
unavailable.
• Communication attack: Interrupting the communication or forcing a device to communicate with
unauthorized external devices.
• Data sniffing: Illegally capturing the communication
to get sensitive information.
• Data modification: Maliciously modifying data.
• Information leakage: Retrieving sensitive
information from the system.
2) PRIVACY & SECURITY OF ML PIPELINE
Any ML model that learns from data can also leak
information about the data, even if it is generalized
well; e.g., using membership inference (i.e., determining
if a particular instance was used to train the model)
[120], [199] or using property inference (i.e., inferring properties of the training dataset from a given
model) [199], [221]. Adversarial attacks in the context of the MLOps pipeline can occur in the following
phases [109]:
• Data collection phase: At this phase, a poisoning
attack results in modified or polluted data, impacting
the training of the model and lowering performance on
unmodified data.
• Modelling phase: Here, the Trojan AI attack can
modify a model to provide an incorrect response for
specific trigger instances [300] by changing the model
architecture and parameters. Since it is now common to
use pre-trained models, these models can be modified or
replaced by attackers.
• Production and deployment phases: At these phases,
both Trojan AI attacks and evasion attacks can occur.
Evasion attacks consist, e.g., of modifying test data to
have them misclassified [229].
3) PRIVACY & SECURITY IN HEALTHCARE
Smart healthcare technologies have become a common
practice [48] and a wide variety of smart devices is
available, including wearable devices (e.g., smartwatches,
skin-based sensors), body area networks (e.g., EEG
sensors, blood pressure sensors), tele-healthcare (e.g.,
tele-monitoring, tele-treatment), digital healthcare systems
(e.g., electronic health records (EHR), electronic medical records (EMR)), and health analytics (e.g., medical
big-data).
More specifically healthcare components [215] can be
categorized as:
• Electronic health data: This data can be leaked due to
human mistakes or malicious attacks, which can result
in tampering or misuse of data. In order to overcome
such risks, measures such as access control, cryptography, anonymization, blockchain, steganography,
or watermarking can be used.
• Medical devices: Medical devices such as smartwatches
and sensors are also another source of information that
can be attacked. Secure hardware and software, authentication and cryptography can be used to avoid such
problems.
• Medical network: Data shared across medical professionals and organizations through a networks may be
susceptible to eavesdropping, spoofing, impersonating,
and unavailability attacks. These threats can be reduced
by applying encryption, authentication, access control,
and compressed sensing.
• Cloud storage: Cloud computing is becoming widely
adopted in healthcare. However, like any system, it is
also prone to unavailability, data breaches, network
attacks, and malicious access. Similar to those above,
threats to cloud services can be avoided through authentication, cryptography, and decoying (i.e., a method to
make an attacker erroneously believe that they have
acquired useful information).
4) PRIVACY & SECURITY APPROACHES
While the digitization of healthcare has improved access to
medical facilities, it has increased the risk of data leakage
and malicious attacks. Extra care should be taken to protect
healthcare data [4] and designing an MLOps pipeline to
avoid privacy and security risks, as it can lead to serious
life-threatening consequences. Other issues may include the
number of people involved in using the data and proper
storage for high volumes of data. Chaudhry et al. [48]
proposed an AI-based framework using 6G-networks for
secure data exchange in digital healthcare devices. Some
other state-of-the-art approaches include:
• Blockchain: In the past decade, the blockchain has
also emerged as a way of ensuring data privacy and
security. Blockchain is a distributed database with
unique characteristics such as immutability, decentralization, and transparency. This is especially relevant in healthcare because of security and privacy
issues [111], [211], [316]. Using blockchain can help
in more efficient and secure management of patient’s
health records, transparency, identification of false
content, patient monitoring, and maintaining financial
statements [111].
• Federated learning (FL): Federated learning ensures
that a general model can be trained on data from
various hospitals so that individual hospitals will not
be able to see data from others. This ensures that
the data of each hospital does not leave its premises.
There are various infrastructure options available, but
generally, setting up a federated learning infrastructure
requires having a central server that aggregates the local
updates from individual hospital’s models, and then
updates the global machine learning model. A survey
of federated learning in healthcare shows that federated
learning approaches perform just as well or even better
than the traditional centralized approach [19]. Federated
learning [248] has demonstrated success in the context
of healthcare; however, it has some limitations. These
include the difficulty in examining specific failure
cases, the challenge of memorizing information, and
susceptibility to adversarial attacks, which may result in
data re-identification. Research is ongoing to make federated learning approaches more robust, and approaches
such as confidential and private collaborative learning
(CaPC), which employs homomorphic encryption, [60]
are promising.
TABLE 5. Key roles in an MLOps team.
5) HEALTHCARE PRIVACY & SECURITY LAWS
Due to the sensitivity of healthcare data and communication, many countries have introduced laws and regulations
such as the Personal Information Protection and Electronic
Documents Act (PIPEDA) in Canada, the Health Insurance
Portability and Accountability Act (HIPPA) in the USA, and
the Data Protection Directive in the EU [309]. These acts
mainly aim at protecting patient data from being shared or
used without their consent while allowing them to access to
their own data.
D. RELIABILITY, ROBUSTNESS, AND RESILIENCE
A trustworthy MLOps system should be reliable, robust, and
resilient. These terms are defined as follows [331]:
• Reliability: The system performs in a satisfactory
manner under specific, unaltered operating conditions.
• Robustness: The system performs in a satisfactory
manner despite changes in operating conditions, e.g.,
data shift.
• Resilience: The system performs in a satisfactory manner despite a major disruption in operating conditions;
e.g., adversarial attacks.
Many researchers have explored these aspects within the
healthcare domain [18], [202], [235], proposing various
approaches, such as creating robust benchmark datasets,
improving evaluation methods, developing methods to
address data shift, applying interpretability & explainability
techniques, and implementing measures to ensure privacy &
security (discussed in Section IV, V-B, and V-C) However,
a trade-off often exists between accuracy, interpretability, and
robustness [243], [284], which arises because robust models
tend to learn feature representations in a different way, which
may reduce accuracy but are generally more understandable
to humans [284]. Careful consideration of all responsible
AI aspects is crucial when developing a trustworthy and
ethical MLHOps pipeline, which is essential for high-stakes
applications in healthcare.
VI. CONCLUDING REMARKS
Machine learning (ML) has been applied to many
clinically-relevant tasks and many relevant datasets in the
research domain but, to fully realize the promise of ML
in healthcare, practical considerations that are not typically
necessary or even common in the research community
must be carefully designed and adhered to. We have
provided a deep survey into a breadth of these ML
considerations, including infrastructure, human resources,
data sources, model deployment, monitoring and updating,
bias, interpretability, privacy and security. As there are
an increasing number of AI systems being deployed into
medical practice, it is important to standardize and to specify
specific engineering pipelines for medical AI development
and deployment, a process we term MLHOps. To this end,
we have outlined the key steps that must be put into practice
by multidisciplinary teams on the cutting edge of AI in
healthcare to ensure the responsible deployment of clinical
AI systems.
VII. CHECKLIST FOR IMPLEMENTING MLHOPS USE CASES
Teams
1) Clinical Team
• Objective: Automate hospital systems and improve healthcare processes.
• Team Members: Clinicians ( may consist of one or more of the following depending on the project type:
Physicians, Surgeons, Nurses, Clinical Informaticians, Healthcare Administrators, Clinical Researchers,
Pharmacists, Radiologists, Laboratory technologists)
• Responsibilities:
– Provide domain expertise and insights into healthcare processes.
– Collaborate with the AI/ML team to define the problem and data requirements.
– Validate and interpret the results of the ML model in a clinical context.
– Ensure that the model aligns with clinical standards and practices.
2) AI/Machine Learning (ML) Team
• Objective: Develop and implement ML models to address healthcare challenges.
• Team Members:
– Student AI researcher(s): Actively contribute to the research and development of ML models.
– University professor: Provide guidance and oversight for the research.
– Data engineer: Manage data collection, storage, and preprocessing.
– ML engineer: Focus on designing, building, and deploying machine learning models.
– Software engineer: Develop software for scalability and integrating ML models into hospital systems.
– Labelers: Annotate and validate data for training and evaluation.
– Responsible AI scientist: Ensure ethical considerations and responsible AI practices.
– Privacy and security specialists: Ensure the privacy and security of the data and system.
– Testers: Develop and run tests on the system.
• Responsibilities:
– Collaborate with the clinical team to understand the problem and data nuances.
– Develop, train, and evaluate ML models using healthcare data.
– Implement models into the hospital system with the help of the software engineer.
– Work with the data engineer to ensure data quality and integrity.
– Engage the Responsible AI scientist to address ethical considerations.
3) Policy/ethics Team
• Objective: Ensure ethical considerations and policy adherence in the development and deployment of ML
models in the hospital.
• Team Members:
– Ethics expert: Provide guidance on ethical implications and compliance.
– Policy expert: Provides guidance on policy.
• Responsibilities:
– Review and approve ethical guidelines for the project.
– Ensure that the ML models adhere to legal and regulatory standards.
– Provide ongoing oversight to address any ethical concerns that may arise.
4) Project Management (PM) Team
• Objective: Facilitate the timely execution of the project.
• Team Members:
– Project managers: Oversee project timelines, milestones, and resource allocation.
• Responsibilities:
– Develop and manage project timelines and milestones.
– Facilitate communication between different teams.
– Ensure that the project stays on track and within budget.
– Address any project management challenges and risks.
A. PHASE 1: EXPLORATORY STAGE
A partnership is initiated between a hospital lab and a university to leverage the collective expertise of both
institutions for the development of a machine learning (ML) model. The primary focus is on addressing a
healthcare-related challenge, and one (or more) AI researcher assistant/ postdoc is brought on board to advance the
project’s initial phase. This study starts with carefully considering ethics and fairness at every step. Collaboration
begins with a clear articulation of the problem the ML model aims to solve. The hospital lab and university
researchers work closely to define the project’s objectives, emphasizing the potential positive impact on healthcare
outcomes. Ethical considerations start at this stage, with a commitment to develop a model that aligns with patient
well-being and respects privacy.
Step 1.1: Project Planning and Management
1) Define project goals and success criteria. □
Responsible personnel: Clinical team, AI/ML team, Project management team.
a) What is the exact goal or clinical application? □
Responsible personnel: Clinical team.
b) What impact would it have? Explain explicit pain points and latent needs. □
Responsible personnel: Clinical team.
c) Who will benefit? □
Responsible personnel: Clinical team.
d) Is the goal feasible? Do you have all the resources to build the infrastructure for it? □
Responsible personnel: Clinical team, AI/ML team, Project management team.
e) Is the goal viable and scalable? □
Responsible personnel: Clinical team, AI/ML team.
f) How will the teams measure success? □
Responsible personnel: Clinical team, AI/ML team.
g) How cost-effective will it be in the long term? □
Responsible personnel: Clinical team, AI/ML team.
2) Identify stakeholders. □
a) Who are the users of the system? □
Responsible personnel: Clinical team.
b) Who are the beneficiaries or the receivers? □
Responsible personnel: Clinical team.
c) Have you collected enough data to support the need for the new system? □
Responsible personnel: AI/ML team.
3) Ensure project compliance with relevant healthcare data regulations (e.g., HIPAA in the United States). □
Responsible personnel: Responsible AI scientist (s), Policy/ethics team.
4) Establish the project timeline. Create a patient journey map [131] if needed. Milestones include □
Responsible personnel: Clinical team, Project management team.
a) Minimum Viable Product (MVP). □
Responsible personnel: AI/ML team, Project management team.
b) Pilot study. □
Responsible personnel: Clinical team, AI/ML team, Project management team.
c) Final deployment. □
Responsible personnel: AI/ML team.
5) Resource estimation and allocation. □
Responsible personnel: AI/ML team, Project management team.
a) Number of technical/non-technical staff involved. □
Responsible personnel: AI/ML team, Project management team.
b) Infrastructure and computing resources required (e.g., GPUs, TPUs). □
Responsible personnel: AI/ML team.
c) Model scalability resources e.g., cloud computing, data storage etc. □
Responsible personnel: AI/ML team.
d) Privacy and security resources (e.g., data encryption tools, data governance policies, etc.) □
Responsible personnel: Privacy and security experts.
Step 1.2: Data Management
1) Data reliability is ensured by properly □
Responsible personnel: Data engineers, Privacy and security expert, Responsible AI scientist.
a) collecting, □
Responsible personnel: Data engineers.
b) preprocessing/cleaning, □
Responsible personnel: Data engineers.
c) anonymizing, □
Responsible personnel: Data engineers.
d) labeling. □
Responsible personnel: Data engineers, labelers.
2) Data storage and archival system □
Responsible personnel: Data engineers.
3) Data versioning and lineage are ensured to track changes and history. □
Responsible personnel: Data engineers.
4) Data ethics is followed □
Responsible personnel: Responsible AI scientist(s), Policy/ethics Team.
a) Privacy and security: Ensure encryption and access control. □
Responsible personnel: Responsible AI scientist(s), Privacy and security experts.
b) Fairness: Equal and fair representation of different groups/communities □
Responsible personnel: Responsible AI scientist(s), Policy/ethics Team.
c) Transparency: Being transparent about the use when acquiring data. □
Responsible personnel: Responsible AI scientist(s), Policy/ethics Team.
d) Data governance: Following policies for data usage. □
Responsible personnel: Responsible AI scientist(s), Policy/ethics Team.
Step 1.3: Model Development and Training
1) Conduct comprehensive data exploration, analyzing data quality, and class distribution etc. □
Responsible personnel: Data engineers.
2) Model development planning □
Responsible personnel: AI/ML team.
a) Survey latest research. □
Responsible personnel: Researchers.
b) Choose a set of possible best techniques/approaches for the given problem. □
Responsible personnel: AI/ML team.
3) Start implementing the code. □
Responsible personnel: ML engineers, Software engineers.
a) Code versioning (e.g. Git) for collaboration and tracking. □
Responsible personnel: ML engineers, Software engineers.
b) Following software engineering best practices for refactoring and continuous development. □
Responsible personnel: ML engineers, Software engineers.
4) Model training, may include one or more of the following steps (if applicable): □
Responsible personnel: ML engineers, Software engineers.
a) Split data into training, validation, and testing. □
Responsible personnel: ML engineers, Software engineers.
b) Hyper-parameter tuning. □
Responsible personnel: ML engineers, Software engineers.
c) Using different metrics to evaluate the model. □
Responsible personnel: ML engineers, Software engineers.
5) Model versioning to capture configurations and hyperparameters used during training. □
Responsible personnel: Clinical team, AI/ML team, Project management team.
6) Model results tracking □
Responsible personnel: ML engineers, Software engineers.
a) Compare and contrast results from different models and settings. □
Responsible personnel: AI/ML team.
b) Quantitatively and/or qualitatively analyzing results using metrics, loss curves, and visualizations. □
Responsible personnel: Clinical team, AI/ML team.
Step 1.4: Model Evaluation and Testing
1) Use automated testing to evaluate model performance. □
Responsible personnel: ML engineers, Software engineers, Testers.
2) Test with different datasets and edge cases. □
Responsible personnel: ML engineers, Software engineers, Testers.
3) Responsible AI model testing: □
Responsible personnel: ML engineers, Software engineers, Testers, Responsible AI scientist.
a) Testing for model fairness, especially in sensitive healthcare decisions. □
Responsible personnel: Responsible AI scientist, Policy/ethics Team.
b) Use or develop interpretable models to explain models’ outcomes to healthcare providers. □
Responsible personnel: ML engineers, Responsible AI scientist.
c) Testing for privacy and security of the model such as data leakage. □
Responsible personnel: Privacy and security experts, Testers, Responsible AI scientist.
Step 1.5: Model Pipeline and Integration
1) Design and implement a pipeline: □
Responsible personnel: ML engineers, Software engineers, Testers.
a) Integrating different components. □
Responsible personnel: ML engineers, Software engineers.
b) Anticipate and plan for adaptability to handle diverse workloads, scale, and future changes. □
Responsible personnel: AI/ML team.
2) Automated testing: □
Responsible personnel: ML engineers, Software engineers, Testers.
a) Implement unit tests and integration tests for each pipeline component. □
Responsible personnel: Clinical team, AI/ML team, Project management team.
b) Include tests for data quality, model accuracy, and deployment stability. □
Responsible personnel: Clinical team, AI/ML team, Project management team.
3) Training and Documentation: □
Responsible personnel: AI/ML team.
a) Provide training to the clinical team on the pipeline and its components. □
Responsible personnel: Clinical team, AI/ML team.
b) Maintain comprehensive documentation for the entire pipeline. □
Responsible personnel: AI/ML team.
4) Monitoring and Logging □
Responsible personnel: ML engineers, Software engineers.
a) Integrate logging for tracking model predictions and performance. □
Responsible personnel: ML engineers, Software engineers.
b) Implement monitoring for model drift and concept drift. □
Responsible personnel: ML engineers, Software engineers.
c) Set up alerts for unusual model behavior or performance degradation. □
Responsible personnel: ML engineers, Software engineers.
B. PHASE 2: PILOT PROJECT STAGE
After the successful outcomes of the Exploratory Phase, the stakeholders from the hospital and university, carefully
evaluate the model and its outcomes. The decision is made after a thorough assessment to proceed with the
adoption of the ML model. To assess the impact and effectiveness of the deployed ML model, the team starts a
randomized control trial (RCT) to ensure a rigorous evaluation of the model’s performance. The team collaborates
to design a robust pilot study as the initial testing ground with clear objectives, outcome measures, and criteria
for success. It is ensured that the scope of the pilot study aligns with the eventual goals of the project. The team
recruits a diverse group of patients for the pilot study, considering factors such as demographic representation and
medical conditions relevant to the ML model’s intended application. Ethical aspects are used for the recruitment
process such as informed consent from each participant including a comprehensive explanation of the study’s
purpose, potential benefits, and any risks involved. An ethics checklist is meticulously followed that includes
considerations such as patient confidentiality, privacy protection, and adherence to regulatory standards. Regular
ethical review board consultations and approvals are obtained to maintain the highest standards of research ethics.
The pilot study phase is a crucial step in MLHOps providing valuable insights into real-world applicability and
possible improvements. By incorporating ethical considerations, patient engagement, and iterative feedback, the
collaborative effort between the clinician and professor lays a solid foundation for the subsequent stages of the
project.
Step 2.1: Pilot Study Design [143]
1) A thorough assessment to proceed with the adoption of the ML model for further testing and implementation. □
Responsible personnel: Clinical team, AI/ML team.
2) If the assessment is positive go to the next step else go back to Phase 0- Exploratory phase and revise the plan. □
Responsible personnel: Clinical team, AI/ML team.
3) Design a robust pilot study as the initial testing ground for the ML model. □
Responsible personnel: Clinical team, AI/ML team.
a) Establish objectives and outcome measures to assess the impact and effectiveness of the ML model. □
Responsible personnel: Clinical team, AI/ML team.
b) Aligning the pilot study with the goals of the project, real-world application, and improvements. □
Responsible personnel: Clinical team, AI/ML team.
c) Choose the locations, sample size, randomization, and blinding for the pilot study. □
Responsible personnel: Clinical team, AI/ML team.
d) Discussion with the clinical staff involved in the pilot study.
Responsible personnel: Clinical team, AI/ML team.
e) Training plan for clinical personnel. □
Responsible personnel: Clinical team, AI/ML team, Project management team.
f) Getting feedback from the clinical team, patients, and other stakeholders. □
Responsible personnel: Clinical team, Stakeholders.
4) Review the feasibility of the designed pilot study and revise if needed. □
Responsible personnel: Clinical team, AI/ML team.
Step 2.2: Responsible AI and ethics
1) Create and follow an ethics checklist, addressing considerations such as □
Responsible personnel: Responsible AI scientists, Policy/ethics Team.
a) Consent: Ensure getting consent from all the stakeholders involved. □
Responsible personnel: Responsible AI scientists, Policy/ethics Team.
b) Explainability: Ensure to share all details about the pilot study with all the stakeholders. □
Responsible personnel: Responsible AI scientists, Policy/ethics Team.
c) Privacy & security: Ensure that patient information is only accessible to authorized personnel. □
Responsible personnel: Responsible AI scientists, Policy/ethics Team.
d) Fairness: Ensure fairness by recruiting a diverse group of patients for the pilot study. □
Responsible personnel: Responsible AI scientists, Policy/ethics Team.
e) Adherence to regulatory standards: Ensure compliance with regulatory standards e.g., PIPEDA, HIPAA. □
Responsible personnel: Responsible AI scientists, Policy/ethics Team.
2) Regular ethical review board consultations and necessary approvals obtained to maintain the research ethics. □
Responsible personnel: Responsible AI scientists, Policy/ethics Team.
Step 2.3: Execute pilot study and get feedback
1) Start execution of the pilot study according to the plan. □
Responsible personnel: Clinical team, AI/ML team.
a) Engage with patients throughout the study, considering their perspectives and ensuring their well-being. □
Responsible personnel: Clinical team, AI/ML team.
b) Incorporate iterative feedback. □
Responsible personnel: Clinical team, AI/ML team.
2) Feedback for improvement, should consider:
a) Ethical considerations, □
Responsible personnel: Responsible AI scientists, Policy/ethics Team.
b) Patient engagement, □
Responsible personnel: Clinical team.
c) Iterative feedback. □
Responsible personnel: Clinical team, AI/ML team.
Step 2.4: Analysis of the pilot study
1) The clinical team and ML team analyze the study. □
Responsible personnel: Clinical team, AI/ML team.
2) An analysis report is presented to the board to decide whether to proceed to the deployment stage or not. □
Responsible personnel: Clinical team, AI/ML team.
C. PHASE 3: ADOPTION STAGE
During the adoption phase, continuous monitoring is done to address any issues that may arise. Regular feedback loops help
to facilitate continuous quality improvement and data shift. Healthcare professionals at the university hospital are educated
and trained to effectively use and integrate the ML model into their workflow. Model scalability is ensured. To support
the deployment and operation of the ML model, the collaborative team leverages technologies such as cloud computing
infrastructure and federated learning to provide a scalable and secure environment with ethical standards and regulations,
ensuring compliance with privacy laws and maintaining the confidentiality of patient information. Transparent communication
is needed to talk to the stakeholders. At this stage hospital lab, university, and stakeholders work together to focus on the live
implementation and evaluation of the ML model.
Step 3.1: Deployment and Serving
1) Scalability readiness: □
Responsible personnel: ML engineers, Software engineers.
a) Choosing the scalable infrastructure. □
Responsible personnel: ML engineers, Software engineers.
b) Optimize code and model architectures for scalability. □
Responsible personnel: ML engineers, Software engineers.
c) Package models into containers for consistency and portability. □
Responsible personnel: ML engineers, Software engineers.
2) Safety checks: □
Responsible personnel: ML engineers, Software engineers, Testers.
a) Implement A/B testing to compare different model versions. □
Responsible personnel: ML engineers, Software engineers, Testers.
b) Ensure privacy and security. □
Responsible personnel: Data engineers, Software engineers, Privacy and security specialists.
c) Robust backup and disaster recovery plans. □.
Responsible personnel: Data engineers, Software engineers.
d) Model Governance and Compliance. □
Responsible personnel: Clinical team, Responsible AI scientist, Policy/ethics Team.
3) Educating and training staff for the new system. □
Responsible personnel: Clinical team, AI/ML team.
4) Deployment: □
Responsible personnel: AI/ML team.
a) Model documentation for code, data, models, and running the system. □
Responsible personnel: AI/ML team.
b) Deploy models on the scalable infrastructure. □
Responsible personnel: Data engineers, Software engineers.
Step 3.2: Monitoring and Logging
1) Model monitoring framework for □
Responsible personnel: AI/ML team.
a) Model performance. □
Responsible personnel: AI/ML team.
b) Performance profiling and logs for important events and errors. □
Responsible personnel: Clinical team, AI/ML team, Project management team.
c) Data drift. □
Responsible personnel: AI/ML team.
d) Concept drift. □
Responsible personnel: AI/ML team.
2) Identify bottlenecks, threats, and anomalies. □
Responsible personnel: AI/ML team.
Step 3.3: Continuous Integration and Continuous Deployment (CI/CD)
1) Automate the build, test, and deployment processes. □
Responsible personnel: AI/ML team.
2) Regularly update dependencies and address potential security vulnerabilities. □
Responsible personnel: Software engineers.
3) Review and validate code changes and model deployments with the ML and clinical teams. □
Responsible personnel: Data engineers, Software engineers, Clinical team.
Step 3.4: Feedback Loop and Iteration
1) Feedback from healthcare professionals to iteratively improve the model’s usefulness. □
Responsible personnel: Clinical team, AI/ML team, Stakeholders.
2) Iterate on the MLOps process to address inefficiencies and optimize performance. □
Responsible personnel: Researchers, Data engineers, Software engineers.
