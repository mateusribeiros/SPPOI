Title: The Environmental Cost of Engineering Machine Learning-Enabled Systems: A Mapping Study

Abstract
The integration of Machine Learning (ML) across public and
industrial sectors has become widespread, posing unique
challenges in comparison to conventional software development methods throughout the lifecycle of ML-Enabled
Systems. Particularly, with the rising importance of ML platforms in software operations and the computational power
associated with their frequent training, testing, and retraining, there is a growing concern about the sustainability of
DevOps practices in the context of AI-enabled software. Despite the increasing interest in this domain, a comprehensive
overview that offers a holistic perspective on research related
to sustainable AI is currently lacking. This paper addresses
this gap by presenting a Systematic Mapping Study that thoroughly examines techniques, tools, and lessons learned to
assess and promote environmental sustainability in MLOps
practices for ML-Enabled Systems.
Keywords: Machine Learning-Enabled Systems, DevOps,
MLOps, Environmental Cost, Sustainability.
1 Introduction
Climate change poses one of the greatest challenges of our
time, affecting ecosystems and the well-being of communities worldwide. Estimating and reducing carbon emissions
is crucial in mitigating its effects. Recent estimates suggest
that the Information and Communications Technology (ICT)
sector contributes ∼2% to global CO2 emissions [41].
As traditional software gets integrated with large Machine
Learning (ML) components to create ML-Enabled Systems
(MLES), ICT’s CO2 emissions are expected to grow even
further. Large ML models repeatedly process vast amounts
of data through complex algorithms–often requiring multiple iterations to optimize model parameters for accuracy.
This computational demand typically necessitates the use
of powerful hardware, such as GPUs or TPUs, which consume substantial amounts of electricity. Additionally, training large-scale ML models, such as those used in natural
language processing or image recognition, can take days,
weeks, or even months to complete, further exacerbating energy consumption. Therefore, there has been a growing call
within the artificial intelligence (AI) community to emphasize the mitigation of environmental footprint linked to the
development, deployment, and maintenance of AI models,
especially in industrial contexts [53].
Since 2008, the software industry has witnessed the rise
of DevOps, promoting collaborative synergy between development and operations teams of traditional software. This
methodology optimized workflows, nurtured efficiency and
effectiveness in software development and operations [20].
Nevertheless, the conventional DevOps approach is not viable for ML-Enabled Systems (MLES) due to the unique challenges associated with such systems (e.g., data dependencies,
boundary erosion, continuous learning) that require specialized deployment and maintenance processes [54]. Therefore,
as application development progresses, the need for an updated methodology arises, driving a necessary evolution in
DevOps. This evolution, crucial in the ML domain, has led
to the emergence of MLOps, essentially DevOps customized
for ML. MLOps plays a vital role in operationalizing ML in
production by automating the entire ML lifecycle, speeding
up model development and deployment, and facilitating innovation delivery. This shift has not only enhanced software
accuracy but also streamlined development processes.
In this work, we analyze how the energy footprint of
MLES is assessed through the lens of MLOps pipeline. We
also review the approaches and the lessons put forward to
minimize it at each of the MLOps phases.
The primary contributions of this study are: (i) Reviewing
existing research on the environmental impact of MLES. (ii)
Conducting a Systematic Mapping Study (SMS) that identifies and examines proposed software engineering practices to
evaluate and reduce the environmental cost of MLES within
the MLOps methodology. Our study offers a comprehensive
overview of community efforts to understand/reduce the
environmental impact of MLOps in MLES and contributes
towards sustainable engineering of such systems.
The subsequent sections of the paper are organized as follows. Section 2 summarises the background and work related
to our study. Section 3 outlines the research methodology.
Section 4 presents the results and engages in discussions.
Finally, Section 5 concludes this work.
2 Background and Related Work
This section describes the background of our study and reviews existing related literature.
Sustainability in software engineering: The United Nations
defines Sustainability as meeting the needs of the present
without compromising the ability of future generations to
meet their own needs [4]. In software engineering, sustainability encompasses five key dimensions: environmental,
economic, technical, social, and individual [5, 47, 49]. The
environmental aspect focuses on minimizing the software’s
impact on the environment, while the economic aspect emphasizes cost-effective development and deployment aligned
with long-term business goals. The technical aspect ensures
software resilience, adaptability, and maintainability, while
the social aspect promotes equity, justice, and trust through
software design. Finally, the individual aspect focuses on
user and developer well-being and satisfaction.
Machine Learning-Enabled Systems (MLES): ML revolutionizes the software industry, integrating AI into everyday applications as MLES. These systems improve software
functionality by incorporating ML components. However,
transitioning from a prototype ML model to a robust, scalable production system poses a significant challenge. Despite
ML’s popularity, deploying MLES often faces a high failure
rate, with nearly 90% failing to reach production [45]. The
MLES life cycle progresses through a coordinated sequence
of interconnected processes. Key processes include configuration, data collection, feature extraction, ML code, data
verification, ML resources, analysis tools, serving infrastructure, and monitoring [54].
DevOps and MLOps: DevOps integrates cultural philosophies, operational practices, and advanced tools to elevate an
organization’s capability for rapid application and service delivery. This holistic approach accelerates product evolution
and improves efficiency. It optimizes the software development lifecycle through practices like Continuous Integration
and Continuous Delivery (CI/CD) [36]. However, as ML gains
prominence in software development, the demand for innovative approaches has led to the emergence of MLOps [33],
which aligns with DevOps principles, MLOps provides a
structured approach for managing data and models in ML
systems alongside the codes. Google’s MLOps framework,
highlighted in [58], stands out for its focus on automating
steps in ML operations. It starts with a basic manual process at level 0 and progresses to level 2, aligning with DevOps principles like Continuous Integration and Continuous
Delivery[25]. To handle challenges in ML models tied to
changing datasets, MLOps introduces Continuous Training
(CT). This means models are automatically updated based
on new data, ensuring they stay effective in real-world scenarios [50].MLOps manages ML model lifecycles through
phases: Data Management for collection and preparation,
Experimentation/Design for iterative model development,
Testing for performance validation, Deployment for production, Continuous Monitoring for post-deployment checks,
Retraining for model effectiveness over time, and Inference
for making predictions based on new data, forming a continuous MLOps cycle. [28].
Related Work: Several surveys and literature reviews focus on sustainable MLES, examining best practices, tools,
and challenges. However, these efforts often concentrate
on technical aspects, especially emphasizing the training
stage in the MLOps lifecycle. Carole-Jean et al. [65] explore
how the rapid growth of AI impacts the environment. They
look at data, algorithms, and hardware in a holistic manner, specifically focusing on Meta’s large-scale ML applications. Their analysis covers the carbon footprint throughout
the entire process of developing AI models, emphasizing
potential reductions through smart hardware-software design and optimization to make AI more environmentally
friendly. Verdecchia et al. [62] identify 13 distinct topics with
a focus on energy-efficient practices such as monitoring,
hyperparameter-tuning, model benchmarking, and deployment. The study highlights less-explored areas, including
data-centric approaches and considerations related to emissions and estimation. Notably, it underscores the significant
energy savings demonstrated by Green AI but raises concerns about the predominance of laboratory studies, advocating for more field experiments to develop practical and
measurable green strategies. The study also emphasizes the
maturation of the field and urges the translation of academic
results into industrial practices.
3 Methodology
The mapping study was conducted through a structured fourstep process: 1) Clearly defining the Research Questions, 2)
Conducting a comprehensive search for relevant literature,
3) Selecting high-quality studies meeting the established
criteria 4) Extracting and synthesizing data from the selected
studies to identify themes and patterns.
3.1 Research Questions (RQs)
The research is conducted based on the following five RQs.
• RQ1: What MLES domains are typically considered when
assessing the environmental impact?
• RQ2: In which MLOps phases have environmental costs
been studied?
• RQ3: What strategies have been proposed to assess and reduce the environmental impact associated with MLES
development and operations?
• RQ4: What metrics have been developed and utilized to
monitor the environmental cost across MLOps?
• RQ5: What sustainability practices and lessons can be
drawn from prior research?
3.2 Search Strategy
To search for relevant studies, we formulate a search query
that combines terms related to three categories and we require our search to return works that include at least one
term from each category:
• ‘Sustainabilty’: ‘Sustainab*’, ‘Green’, ‘Ecolog*’, ‘Energy
Consumption’.
• ‘DevOps’: ‘Development and Operation’, ‘MLOps’, ‘AIOps’,
‘Development Life Cycle’, ’End-to-End pipeline’, ‘CI/CD’,
‘Software Development’, ‘Software Deployment’, ‘Software Maintenance’.
• ‘MLES’: ‘Machine Learning-Enabled System’, ‘ML-Based
System’, ‘Machine Learning System’, ‘Machine Learning Software’, ‘Software Engineering’,‘Machine Learning’,‘artificial Intelligence’.
We conducted a comprehensive search for scientific articles across four databases (i.e., Scopus, IEEE Xplore, ACM,
and Web of Science) which returned 745, 551, 17, and 422
papers respectively. Following the application of inclusions
and exclusions criteria in Table 1 and snowballing, we have
selected 52 relevant and unique papers that we use to answer
our above research questions.
Table 1. Inclusion/Exclusion criteria.
Inc./Exc. Criteria
Inclusion - Addressing 1 or more DevOps/MLOps phases
- Discussing MLES environmental impact
Exclusion - Not available in the English language
- Out of topic (using terms for other purposes)
- Dissertations, tutorials, editorials, magazines
4 Results and Discussion
This section presents the findings from the SMS, with a
breakdown of quantitative results and their corresponding
analysis for each Research Question.
RQ1: What MLES demains are typically considered
when assessing the environmental impact?
In analyzing the distribution of data types depicted in Figure 1, it becomes evident that textual data stands out as the
Figure 1. Number of papers per data modularity over years.
most prevalent, being utilized in half of the studies within
the existing literature. Following closely, image data emerges
as the second most utilized type, albeit appearing roughly as
frequently as textual data. Other data types, such as numeric
data, attribute data, video, and audio data, are less commonly
utilized, with only a few studies incorporating them into
their analyses.
Our observation indicates that the widespread use of textual
and image data in evaluating the environmental impact of
ML systems is not necessarily a deliberate choice in research
design. Instead, we hypothesize that this preference largely
stems from convenience. This convenience could be due
to historical trends where research naturally gravitated towards these data types, or it could be because of the current
accessibility of text and image ML models/libraries.
Regardless of the specific reasons, this observation highlights the importance of incorporating a broader range of
data types to fully assess the environmental impact of MLES.
Rather than solely concentrating on these particular data
modalities, a more comprehensive evaluation necessitates
the inclusion of diverse data types.
After examining the distribution of ML model types, it
is evident that numerous studies utilize a combination of
models. Notably, supervised learning algorithms stand out
as the predominant choice. This dominance is further underscored by the widespread utilization of convolutional
neural network (CNN) based models like ResNet50, VGG,
and MobileNet in assessing the environmental implications
of ML systems. Additionally, the adoption of Transformerbased models such as BERT emphasizes the pressing need
to reduce carbon emissions, particularly concerning large
language models (LLM) and large multimodal models (LMM),
throughout both their developmental and operational phases.
Nevertheless, there exists a gap in research concerning the
comprehension and mitigation of the environmental impact
associated with unsupervised learning algorithms and automated machine learning (AutoML), with only five papers
dedicated to this domain. Similarly, there is only very few papers exploring the carbon footprint implications of Federated
Learning, with only three papers addressing this aspect.
RQ2: In which MLOps phases have environmental
costs been studied?
To gain a deeper understanding of the search results, we
have created a bubble chart (Figure 2) that connects the
contribution type facet to the focus type facet. The key areas of focus within the environmental cost aspect of MLES
generally revolve around "Frameworks" in the "Experimentation/Design" phase (13 out of 52), and "Lessons learned" in
both the "Experimentation/Design" (17 out of 52) and "Inference" stages (10 out of 52), respectively. The figure indicates
that the majority of the frameworks should be viewed as
proposed solutions (16 out of 52), with many of them addressing multiple stages of the MLOps pipeline. Likewise,
approximately half of the total papers, specifically 7 out of 52
included guidelines, and 18 out of 52 included lessons learned.
i.e., lessons learned are insights that are derived from discussions or investigations conducted in artificial or laboratory
settings. Furthermore,5 papers introduced novel metrics for
quantifying power consumption and/or CO2 emissions at
one or multiple stages of the pipeline by monitoring resource
utilization in both CPUs and GPUs, although the majority
concentrate on tracking power consumption during the design stage and retraining phase. On the other hand, there is
a notable scarcity of research focusing on the environmental
costs associated with data management, testing, deployment,
and inference. Furthermore, we contend that this scarcity
extends to the stages of retraining and monitoring.
Based on review of the collected papers, we can identify two
predominant trends: an inclination towards suggesting novel
solutions, primarily revolving around frameworks or tools,
and a significant focus on sharing lessons learned. These
patterns persist both within the final result. Notably, the majority of proposed frameworks center on the experimentation
stage, while approximately 75% of reported lessons learned
pertain to either the experimentation or inference stages.
In essence, this section portrays a continuously evolving
research landscape marked by the emergence of innovative
approaches and the accumulation of valuable insights.
RQ3: What strategies have been proposed to assess
and reduce the environmental impact associated with
MLES development and operations?
In the examination of the contributions, we were able to
pinpoint the primary phases that authors emphasize in their
research. Table 2 illustrates the MLOps phases encompassed
in the analyzed papers. It is important to note that a paper
may cover multiple stages.
The majority of primary studies addressing environmental impact primarily propose frameworks, constituting approximately 31% (seventeen out of fifty-two studies) of the
total [3, 7, 9, 16, 18, 19, 27, 31, 34, 35, 37, 38, 44, 52, 68] such
as IrEne, Clover, LLMCARBON, Zeus, GEECO, ECO2AI, and
Carburacy. The majority of these solutions offer ways aimed
at handling, quantifying, monitoring, and decision-making
within a MLOps pipeline. In order to accomplish these tasks,
they primarily employ techniques like modeling, estimations
to approximate the intricate workings of real-world systems.
This enables them to effectively evaluate the environmental
cost of ML-based systems, utilizing energy consumption as
a proxy to gauge carbon emissions.
The next research focus proposes high-level strategies [6,
11, 12, 29, 48, 56, 60, 69], these approaches encompass various
strategies for reducing the carbon footprint in MLES. They
propose the integration of carbon-aware computing principles, Bringing together Incremental Learning and Green AI
fields, and the introduction of innovative concepts such as
Green Federated Learning. Finally, some Techniques were
Table 2. Contributions per MLOps Phase.
MLOps Phase Frameworks High-Level Strategies Techniques
Data Management [1, 27, 35, 43] [48]
Experimentation / Design [3, 7, 9, 16, 19, 27, 31, 34, 35, 37, 52, 68] [11, 12, 60, 69] [21, 32, 52]
Testing [27, 35, 37]
Monitoring [3, 7, 9, 27, 44, 68] [29, 56]
Retraining [7, 16, 27, 31, 34, 35, 37] [12] [26, 52]
Inference [9, 18, 19, 27, 31, 35, 37, 38] [6]
Table 3. Metrics Proposed to Assess Environmental Cost.
MLOps Phase Metric Description Ref
End-to-End An extension of the metric defined in [22]. [17]
Introducing Software Carbon Intensity (SCI) for real-time cloud instance carbon
emissions.
[16]
Experimentation and Retraining Total power consumption estimated by combining GPU, CPU, and DRAM usage,
multiplied by Power Usage Effectiveness (PUE).
[57]
Training and Inference Deep Learning metrics gauge accuracy and energy usage. [30]
Experimentation, Retraining
and Inference
Using CodeCarbon [53] to estimate energy consumption by CPU and GPU. [44]
proposed [21, 26, 32, 52] have been suggested to develop
models, train, and retrain them effectively while minimizing
carbon emissions.
RQ4: What metrics have been developed and utilized
to monitor the environmental cost across MLOps?
Metrics for assessing energy consumption and CO2 emissions play a vital role in monitoring and managing environmental impact. These metrics enable us to quantify the
performance of systems and technologies aimed at reducing
carbon footprint and optimizing energy usage.
Given the diverse range of tasks and contexts in which
these systems operate, these metrics provide valuable insights for comparing and selecting the most effective approaches for minimizing energy consumption and CO2 emissions. Selecting the right metrics is pivotal as it influences
decision-making and policy formulation, ensuring that efforts are directed towards the most effective solutions in
mitigating the carbon footprint.
Out of 52 selected studies, 5 papers ([57], [17], [30], [16],
[44]) have introduced or expanded on metrics aimed at tracking or computing the carbon footprint across one or more
ML pipelines as shown in Table 3. This indicates a growing awareness and effort within the research community
to develop metrics that go beyond traditional performance
evaluations, addressing the environmental impact of machine learning processes. These specialized metrics not only
contribute to the broader understanding of the ecological
footprint of ML applications but also provide valuable insights for developing more sustainable and environmentally
conscious machine learning practices.
RQ5: What sustainability practices and lessons can
be drawn from prior research?
Table 4 provides a thorough compilation summarizing
the various guidelines and valuable lessons learned derived
from the works identified in our mapping study. It offers a
detailed overview of the insights and strategies relevant to
our research.
5 Conclusion
As traditional software gets integrated with large ML components to form MLESes, ICT’s CO2 emissions are expected
to grow even further. While there has been an increased
recognition of the environmental cost of MLES, a unified
approach towards ensuring sustainability remains elusive.
This mapping study presented a thorough examination of
methodologies, tools, and metrics employed to assess and
mitigate MLES environmental cost and their mapping onto
the MLOps pipeline. By analyzing 52 primary studies from
2019 to 2023, our study offered insights into the growing
landscape of this field, laying the groundwork for future
investigations into eco-friendly strategies for MLES MLOps.
The main findings reveal a critical gap in the current practices and strategies for managing the environmental impact
of MLES within the MLOps pipeline. Despite the availability
of strategies and metrics aimed at assessing the environmental impact of these systems, the study shows that there is no
optimal practices for integrating these assessments into the
development and operation of MLES. Moreover, our analysis
indicates that the majority of existing research is focused
on controlled, in vitro environments. Hence, there is a pressing need for more in vivo studies, i.e., field experiments and
studies in an industrial settings. As future work, we plan to
develop foundational concepts and techniques for improving,
monitoring, and optimizing the efficiency and sustainability
of MLES MLOps pipelines over time.
Acknowledgment: This work was supported with the financial support of the Science Foundation Ireland grant
13/RC/2094_P2.
Table 4. Mapping MLOps Phases to Key Papers: Lessons Learned and Guidelines
MLOps
Phase
Description of Lessons Learned and Guideline Ref
End-to-end Hardware energy consumption meters reveal 20% error. We need more precise measurement tools. [8]
There is a disparity between efficient and sustainable ML, and nuances between sustainability metrics
and operational emissions. Proposed systems thinking.
[64]
Devised guidelines to help understand the environmental implications of AI computing and mitigate its
carbon footprint through optimizations in hardware, software, and operational practices.
[65]
Data Reducing data input size through methods like random sampling enhances ML energy efficiency. [2]
Management Stratified sampling decreases input data features and yields energy savings. [61]
Traininig Recommends using random optimization over Bayesian optimization for hyperparameters as accuracy
gains diminish with increased energy usage in neural network architectures.
[67]
During multilayer perceptron classifier hyperparameter optimization, there is a point where increased
energy consumption minimally improves accuracy.
[6]
Current deep learning models are unsustainable due to their high data and computational demands. We
need more efficient methods in ML to address sustainability challenges.
[59]
Selecting energy-efficient architectures for deep learning training lowers energy usage while maintaining
accuracy. The study highlights how training environments impact energy consumption and recommends
factoring this in when selecting models.
[14]
Only a minority of the 170,000 Hugging Face (HF) models report CO2 emissions from training. Factors
such as model and dataset size correlate with CO2 emissions. Fine-tuning shows similar emissions
compared to full pretraining.
[10]
Hyperparameters in transformer models affect power consumption and model quality. Lower hidden
dropout probabilities improve perplexity with minimal energy impact. While top-performing models
face a trade-off between perplexity reduction and energy minimization. And increasing hidden layers
increases energy usage and lowers perplexity.
[13]
There is a link between carbon emissions, CNN architecture, and uncontrollable factors like cloud
hosting location. Experimental design influences CNN training energy efficiency.
[66]
THETA guidelines to reduce carbon emissions in model development through hyperparameter optimization, energy-efficient hardware, training logistics, and automatic mixed precision training.
[55]
97% of the overall CO2 emissions in Federated Learning (FL) come from client compute and client-server
communications. We need energy-efficient and high-performance production FL systems.
[69]
Inference Evaluate LLMs, examines inference performance and energy usage in distributed settings. It shows how
input complexity affects performance with specific settings and hardware.
[51]
Performance of ML models can be improved without increasing energy usage, but overall system
integration/adoption may raise energy consumption (akin to better roads yielding more cars).
[15]
GPT models have a significant environmental impact. We should prioritize sustainability in their
deployment; addressing embodied carbon, and seek sustainable solutions for large model inference
[18]
Examined energy consumption of LLMs. Identified significant variations in efficiency influenced by task,
modality, model size, and architecture. stressed the trade-off between the advantages of multi-purpose
systems, their energy expenditure, and resulting carbon emissions
[39]
Training and GPU energy use varies greatly. Inference with large models is energy intensive. Important to select
CO2-friendly cloud regions.
[46]
Inference Hardware and datacenter optimization yield substantial reduction in energy consumption for training
and inference of natural language processing(NLP) apps.
[42]
Knowledge distillation consumes 50% more energy than pre-training. Energy usage scales primarily
with time and token count. In BERT-based models, inference energy costs vary with sequence lengths.
[63]
Energy use and run-time differ for PyTorch and TensorFlow; better documentation on energy costs is
needed.
[24]
Guidelines for the ML community with established methods to estimate energy cost. [23]
Training
and Retraining
BigScience Large Open-science Open-access Multilingual Language Model (BLOOM) training accounts
for about 22% of emissions, with the rest coming from intermediate training and evaluation. Estimates
of future embodied emissions will become the dominant source of emissions in ML.
[40]