Title: Building Domain-Specific Machine Learning Workflows: A
Conceptual Framework for the State-of-the-Practice

Abstract Domain experts are increasingly employing
machine learning to solve their domain-specific problems. This article presents six key challenges that a domain expert faces in transforming their problem into a
computational workflow, and then into an executable
implementation. These challenges arise out of our conceptual framework which presents the “route” of options that a domain expert may choose to take while
developing their solution.
To ground our conceptual framework in the stateof-the-practice, this article discusses a selection of available textual and graphical workflow systems and their
support for these six challenges. Case studies from the
literature in various domains are also examined to highlight the tools used by the domain experts as well as
a classification of the domain-specificity and machine
learning usage of their problem, workflow, and implementation.
The state-of-the-practice informs our discussion of
the six key challenges, where we identify which challenges are not sufficiently addressed by available tools.
We also suggest possible research directions for software engineering researchers to increase the automation
of these tools and disseminate best-practice techniques
between software engineering and various scientific domains.
1 Introduction
The past two decades have seen the learning algorithms,
especially deep learning, permeate throughout every
scientific, engineering, and business domain to enable
new techniques and solve complex challenges. One example of many is the recent solving of the long-standing
protein folding problem, which focuses on how a protein will fold in three-dimensional space given it’s onedimensional representation [58].
The enormous power offered by current machine
learning techniques is therefore of great interest to stakeholders across all domains. However, utilising these techniques often requires a user who is an expert in their
own domain to gain proficiency in not only the concepts
of machine learning but also the programming abilities
used to call the low-level libraries. This is undesirable as
the domain expert would like to reason about concepts
and terms that are in their own domain. For example,
the literature on domain-specific languages shows that
solving a problem in the problem domain is more efficient than solving it in the solution domain [59, 110].
Recently, the rise of low-code platforms partially
addresses this issue by raising the level of abstraction
from writing code to interactively defining procedures
and GUIs [14, 11]. A domain expert (or “citizen developer”) is thus assisted to build applications or computations using an easy-to-use and easy-to-deploy interface.
The domain expert may also be able to select domainspecific components which directly address concerns in
their domain such as IoT [53], or machine learning components to simplify machine learning tasks.
Research Problem
In this article, we focus on this intersection of domain
experts, low-code solutions, and machine learning. Specif
ically, we are interested in the flow-based [80] nature of
workflows, which are the typical presentation of computations in low-code platforms and scientific computing frameworks. That is, these workflows are composed
of computational blocks arranged in a graph structure
with the edges denoting data or control dependencies.
We note that this representation perfectly matches with
the common notion of a machine learning pipeline where
data is ingested, cleaned, and trained upon to produce
a machine learning model.
The research question that naturally arises is thus:
Given a domain expert and a domain-specific (DS) problem, what are the tools and techniques needed such that
this problem can be: a) mapped to a machine learning (ML) representation, b) constructed as a workflow
which utilises ML techniques and libraries, and c) deployed from that workflow into an executable implementation?
For instance, to address the first sub-question, we
have identified that a domain-specific problem can be
mapped to a ML representation either formal reasoning or expert mapping. Huang et al. describe such an
expert mapping in the domain of genomics [52]. Their
work assists genomics researchers by mapping drug and
tissue structures from the domain into forms suitable
for ML, defining the problem as a ML problem, and
recommending suitable ML techniques for solving the
ML problem.
Contributions
Our main contribution is a conceptual framework to
map out the tools and techniques for solving a DS
problem using a workflow which involves ML, where
that workflow is then deployed into an executable implementation. This framework illustrates that there are
multiple choices or routes that a domain expert may
choose from to obtain an executable implementation
from their problem. For example, a domain expert may
wish to first consult an expert mapping to determine
how the problem should be structured in a ML representation, before they construct a workflow by manually
selecting suitable components from a repository.
These three layers are divided into regions, where
problems, workflows, and implementations are organised by the dimensions of domain-specificity and presence of machine learning. The choices of the domain
expert can then be seen as transformations between
different regions of our conceptual framework. These
transformations are phrased as interesting software engineering challenges which directly impact a domain
expert who wishes to use machine learning. In other
words, we attempt to organise a) the meaning of, and
b) tools and techniques such that a domain expert can:
– Map a DS problem to a form suitable for ML
– Obtain a solution workflow for a DS and/or ML
problem
– Experiment with ML tools and techniques within a
workflow
– Add DS knowledge to improve ML performance (e.g.,
feature engineering)
– Produce an implementation from a workflow which
is well-suited for a domain expert (in terms of scalability, DS tooling, etc.)
– Extract a workflow from an existing implementation
(code, Jupyter notebook)
To ground the above framework and challenges, this
article discusses some state-of-the-practice tools and
techniques which address these questions. A selection
of case studies also provides recent examples of domain
experts utilising machine learning as framed in the context of our framework. We also provide a detailed discussion of the benefits of structuring the research problem into our conceptual framework, along with an examination of challenges and research directions.
Overall, our intention with this article is to provide
a starting point for those readers who are interested in
overcoming these challenges such that domain experts
can more efficiently utilise machine learning to solve
their problems. This involves cross-discipline efforts to
apply best practices and insights across software engineering, machine learning, and other scientific fields.
Article Structure
As our framework relates topics from different disciplines, Section 2 provides background on the topics of
domain-specificity, machine learning, and workflows.
Our three-layer conceptual framework relating problems, solution workflows, and implementations is presented in an overview in Section 3. Section 4 discusses
each layer of this framework in turn including the transformations within each layer. Section 5 then presents
the transformations between layers. These inter-layer
transformations involve turning problems into workflows, and from workflows into an implementation.
Section 6 provides a brief selection of state-of-thepractice tools which implement the transformations found
in our framework. Representative case studies are presented in Section 7 to detail how practitioners from various fields are employing these tools and executing these
transformations on their own problems.
Section 8 then uses the framework as a basis for a
discussion of the opportunities and challenges for im-
plementing and automating the transformations in the
framework. Section 9 presents our concluding thoughts.
2 Background
This section provides a brief background in three core
topics of this article: the concept of domain-specificity,
machine learning, and computational workflows.
2.1 Domain-Specificity
In this article, we discuss the idea of domain-specificity
as relating to the concepts of a particular domain. This
is relevant throughout our framework as a) a domain
expert had specific experience and insights into that
domain and is less familiar with concepts outside that
domain, b) the problem the domain expert has is (partially) expressed using those domain concepts, and c)
the technical considerations for a solution such as computing platforms and tools may be specific to that domain. In this article, domain-specificity is manifested as
a cross-cutting dimension of the framework as discussed
in Section 3.1. In particular, we specify that problems,
workflows, and implementations can be more or less
domain-specific.
For example, consider the domain of neuroscience
which is the study of the nervous system. Relevant concepts to a neuroscientist include neurons, signals, behaviour, activation, brain hemispheres, neural circuits,
and brain damage, with more according to the sub-field
of the neuroscientist. These concepts may be formalised
in an ontology1
, allowing for more precise or (semi-)
automated reasoning about the concepts and their connections.
Along with these concepts, the data examined by
this expert is highly specific to the domain. In neuroscience, this can include processing of functional Magnetic Resonance Imaging (fMRI) files requiring specialised techniques to handle motion correction (correcting the movement of the subject within the scanner) and smoothing of the data (to average out the noise
present in the measurement). Finally, the datasets, tools,
and computational platforms available to a neuroscientist are highly domain-specific such as repositories of
mouse brain scans2
.
As a domain expert is most knowledgeable about
concepts from their domains, we follow the approach of
domain-specific modelling in declaring that problems
should be solved at a high level of abstraction using
1 See https://github.com/SciCrunch/NIF-Ontology for
an example.
2 For example: https://neuinfo.org/.
domain-specific concepts [59, 110]. That is, the domain
expert should use domain-specific languages instead of
general programming languages, and there should be a
layered approach when possible to hide technical and
implementation details. This approach has been shown
to lower the cognitive workload of learning new concepts and resulting in increased productivity [110]. In
the context of this article, we are interested in improving support such that the domain expert can describe
their problem and workflow using domain-specific concepts.
2.2 Machine Learning
Machine learning (ML) can be summarised as “programming computers to optimise a performance criterion using example data or past experience” [4]. That
is, based on a collection of data and experiences, ML
seeks to automatically create models capable of relating output for particular inputs without requiring a programmer to directly implement the steps for computing
such outputs. These definitions therefore capture many
applications ranging from interpolating based on a simple linear regression up to automated driving by using
visual data interpreted using neural networks.
One way of categorising ML approaches is into three
approaches: supervised learning, unsupervised learning,
and reinforcement learning. In supervised learning, the
supervisor provides inputs and labelled outputs, and
the technique must learn the mapping between inputs
and outputs. An example would be to train a linear regression of variables, producing a classifier which can
predict whether a tissue sample is a tumor or not [39],
or constructing a similarity function such that related
objects can be found. In unsupervised learning, the technique learns without provided labels. This can offer insights into the structure of the domain such as uncovering related clusters of data or outliers. In reinforcement
learning, the intelligent agent is rewarded with a defined reward function. This allows the agent to explore
possible actions and receive automated feedback.
A ML model must be trained before it can be used
for reasoning. For example, consider the scenario of
training a model for a “line-of-best-fit” (linear regression). Once the data points have been loaded and any
cleaning necessary performed, the data is then commonly divided into training and test sets. This allows
for an unbiased measure of error when testing, as the
model has not “seen” the testing data beforehand. The
linear regression is then learned by a suitable algorithm,
and the linear regression is the produced ML model
ready for use. When this model is used it is fed a new
piece of data as input, and it will predict a particular
output.
Many libraries are available which implement some
form of ML. For example, scikit-learn3
is a popular
Python module which offers a high-level API for ML
techniques, while Keras4 provides an API for directly
creating neural networks by constructing each layer into
a model. ML techniques are also available directly within
academic and scientific tools such as the MATLAB Statistics and Machine Learning toolbox5
.
2.3 Computational Workflows
General workflows have existed for many years, especially in the manufacturing domain. In this article, we
focus on computational workflows which define the steps
that a computational device follows to produce results.
In particular, we are interested in workflows which
represent flow-based programming by containing discrete steps representing computational steps [80]. This
can be represented by a directed-acyclic graph (DAG)
of computational nodes connected by control and data
dependencies. Note that in current workflow systems
(Section 6) this restriction on acyclic graphs is relaxed,
as tools may wish to encode control flow structures such
as loops over input files.
This concept of data “flowing” through a workflow
is quite a natural structure for many computations we
examine in this article. Indeed, some domains may lean
into the plumbing metaphor and refer to the workflow
as a “pipeline”. Lamprecht et al. state that, “Another
common, more differentiating view is that pipelines are
purely computational and as such a subset of the more
general notion of workflows, which can also involve a
human element” [69]. To clarify the terminology in this
article, we only discuss computational workflows. That
is, the term ‘workflow’ in this article do not contain human elements and can therefore be equated to pipelines.
Scientific Workflow Management
The large scale of scientific data and the reproducibility
requirements of scientific processes have encouraged the
growth of workflow management systems within various scientific domains. For example, ensuring that data
sources and computations follow the well-known principles of Findable, Accessible, Interoperable, Reusable
(FAIR) [114] demands a comprehensive management
3 https://scikit-learn.org
4 https://keras.io
5 https://www.mathworks.com/products/statistics.
html
system. The life sciences in particular have a rich history of workflow systems [73, 115, 88, 69], a few of which
are discussed in our sections on tools (Section 6) and
case studies (Section 7).
As workflows explicitly declare the sequence of computations they perform, they assist in the production
of reproducible results [105, 115]. That is, they assist
to reproduce the results of another experiment [54].
For example, the discrete nature of workflow components means that components can be tagged with provenance information [94] and placed into containers such
as Docker containers 6
. This allows for easily accessible, self-contained units which can be accessed through
repositories and placed into dependency management
systems [26].
Many factors can influence whether a computational
process is reproducible, and workflows are only one step
towards full reproducibility. For example, Digan et al.
discuss 40 reproducibility features sourced from recommendations and clinical usages of workflows in the
natural language processing (NLP) domain [28]. MoraCantallops et al. discuss reproduciblity in the context
of artifical intelligence/ML [79].
Machine Learning Pipelines
In ML, the term pipeline is commonly used to denote
the steps involved in the training and reasoning processes. For example, data can be involved in a linear
flow of loading, filtering, cleaning, splitting (into a training and testing set), and trained upon.
A similar linear flow is also present for the neural
networks used in deep learning. The input data passes
through layers in this network which recognise patterns
in the input data, store relationships in the weights between nodes in inner layers, and then produce output
values or categories.
Thus, ML pipelines are a one-to-one match to the
workflow formalism we examine in this article. This unification of structure is important when we discuss workflows which involve components from both a particular
scientific domain as well as ML components.
3 Overview of Our Framework
This section will provide an overview of our conceptual
framework by discussing its structure, two dimensions,
and relating the framework to our challenge questions
introduced in Section 1.
As a summary, our conceptual framework maps out
the options for a domain expert to choose from to develop a workflow-based solution to their problem using
machine learning, and ultimately obtain a usable implementation. The framework is seen in Figure 1, separated into twelve regions through the division of three
layers and two dimensions. The three horizontal layers define the problem space, workflow solution space,
and the implementation space. The problem space layer
contains the problem of the domain expert. For example, a neuroscientist may wish to classify brain scan
data as belonging to a depressed patient or not. The
solution workflow space layer contains workflows which
solve the problems from the upper layer. The implementation space contains the implementation details for the
workflows in the middle layer. Section 4 addresses these
layers in detail.
Each layer is decomposed into four regions, defined
by the domain-specific and machine learning dimensions. Section 4 also discusses the mappings and transformations between the regions in a layer. For example, one transformation would map a problem in the
domain-specific problem space (DSP) to the machine
learning problem space (MLP). This represents all techniques to transform the domain-specific problem to a
machine learning problem such as an expert mapping [52].
Section 5 will then discuss the mappings and transformations between layers. That is, from a problem to
a workflow, and then from a workflow to an implementation.
3.1 Dimensions of the Space
This framework defines two dimensions for each layer.
First is the notion of domain specificity which captures
how many domain-specific concepts an artefact contains. Second, the machine learning dimension captures
how many machine learning (ML) concepts the artefact
contains.
For example, consider an artefact from the first layer:
a problem to be solved. This problem could be very
generic such as “finding the clusters for a table of data”.
Adding domain specificity comes from adding domain
knowledge to the problem, such as clustering related
genes or molecules which may change the solutions available for the problem. Similarly, ML concepts such as
clustering, unsupervised/supervised learning, or convolutional filters may be present in the problem description or not, affecting how far the problem is along the
machine learning dimension.
In the problem space layer, the problems are categorised based on the domain-specific or ML concepts
present. For the solution workflow layer, this categorisation depends on the proportion of components in the
workflow. In the implementation space layer, this categorisation depends on the use of domain-specific or ML
APIs or libraries. Section 4 further discusses how the
dimensions divide up each layer in the framework.
Note that by necessity, these categorisations are fuzzy
and we intentionally do not provide boundaries to these
regions. Instead, we provide these dimensions to provoke reflection about the mappings and transformations
along these dimensions. That is, what does it mean
to make a problem, workflow, or implementation more
domain-specific or involve more machine learning, and
what are the techniques to do so?
Let us also note that these two dimensions are certainly not orthogonal. Specifically, machine learning is
itself a domain of interest and these two dimensions
may overlap significantly depending on the problem of
interest. Therefore, let us state here that when this ar-
ticle refers to domains or domain experts, we refer to a
non-machine learning domain.
3.2 Relation to Software Engineering Challenges
As expressed in our framework, the domain expert wishes
to transform their problem from their domain (the DSP
region on the top layer in Figure 1) all the way into an
implementation using machine learning libraries (the
BI or MLI regions on the bottom layer). Through these
transformations, the domain expert is able to move
around through different regions as shown by the case
studies in Section 7, though support may be lacking for
some operations in various tools as discussed in Section 8. In particular, we are interested in determining
tool support for transformations enabling the most direct route from the domain-specific problem (DSP) to a
blended workflow (BW) down to a blended implementation (BI).
Here we recall the challenge questions from Section 1
and relate them to specific transformations. Note that
other transformations are indeed possible and may be
relevant to a domain expert. However, we have chosen
these transformations to focus on as they seem most
relevant to the tools and case studies discussed in this
article.
Mapping a DS problem to a form suitable for ML : This
challenge refers to how domain-specific problems in the
problem space can be mapped or transformed to include
more ML concepts. That is, moving the problems along
the ML dimension in the problem space.
Providing a solution workflow for a DS and/or ML
problem : This challenge refers to the mapping between
a problem in the problem space and a workflow in the
solution workflow space. That is, moving from the top
to the middle layer in the workflow.
Allowing the domain expert to experiment with appropriate ML components in a DS workflow : This challenge refers to moving solution workflows on the middle
layer along the ML dimension through the integration
of more ML components.
Adding DS knowledge to improve ML performance :
This challenge refers to moving solution workflows on
the middle layer along the DS dimension by adding new
DS information or components.
Producing an implementation from a workflow which is
well-suited for a domain expert : This transformation is
between the middle and bottom layers, as the workflow
of the domain expert is mapped or transformed to an
executable implementation.
Extracting a workflow from an existing implementation
(code or notebook : This challenge is an inverse to the
previous one, as the implementation on the bottom
layer of the framework is instead transformed into a
solution workflow on the middle layer.
4 Layers and Intra-Layer Transformations
This section details the three layers of our framework
as shown in Figure 3: the problem space, the solution
workflow space, and the implementation space. The regions and relevant transformations within each layer
are then presented.
4.1 Problem Space
The problem space is where the problem of the domain
expert is formulated. For example, the running example
presented in Section 1 can be expressed in two ways. In
the domain-specific space (DSP), the problem is to predict whether a drug will work well with a sample of tissue [52]. As a machine learning representation (MLP),
this problem becomes a numerical prediction for efficacy of the graph structure (for the drug) versus a linear string of characters (for the genes present in the
tissue). A blended version of this problem (BP) is visualised in Figure 2 where the structures for the drug
and gene are fed into ML encoders and used to make
a numerical prediction related to how the drug affects
the gene.
4.1.1 Artefact Representation
The artefact for this layer is a problem composed of concepts. This problem may be specified in multiple ways
ranging from a simple informal statement to a complex formal representation. For example, the problem
could be specified as natural language research questions, in an ontological manner, in a textual or graphical domain-specific language (DSL), or in a templatebased, requirement-like manner.
4.1.2 Layer Regions
In our framework, we define four regions for the problem space: General Problems (GP), Domain-Specific
Problems (DSP), Machine Learning Problems (MLP),
and Blended Problems (BP) as shown in Figure 3. These
regions are defined by the domain-specificity and machine learning dimensions as discussed in Section 3.1.
Fig. 3 A representation of the problem space, with intralayer transformations.
A general problem is one which does not refer to
any domain-specific concepts, nor does it refer to any
machine learning concepts. This region is provided for
completeness as this article focuses on the other three
regions.
Domain-specific problems are those that are specified in the domain of interest by experts. They involve concepts which are specialised to that domain.
In this article, the domain-specific problem is the starting point from which the expert wishes to solve with a
workflow and finally an executable implementation.
A machine learning problem is a problem which involves a high proportion of machine learning concepts.
For example, learning how to classify objects by ingesting data from a table. The machine learning problem
may also delve into high-level workflow steps, such as
referring to concepts such as convolutional layers or optimising of meta-parameters in training.
A blended problem is one that contains both domainspecific and machine learning concepts. For example,
the problem represented in Figure 2 contains both DS
and ML concepts. This type of problem may be ideal for
the domain expert to begin with instead of a domainspecific one, as the ML concepts can be directly conceptualised and/or operationalised in the workflow layer.
However, it already implies that the practitioners has
access to both domain and machine learning knowledge,
and has studied the problem from both domains.
4.1.3 Layer Transformations
As discussed in Section 3.1, it is interesting to reason
about how to transform an artefact on each layer to
make it more domain specific or involve more machine
learning components. In other words, to make these
problems more DS/ML specific and less general.
To increase domain specificity, a domain expert will
have to encode more domain knowledge into the problem. This could be in the form of an ontology representing formal knowledge, or by directly specifying features
of interest in the domain and their interaction with
other features. For example, consider the drug molecule
and gene running example. As this molecule is a chemical structure, this restricts the possible forms it may
take, which may make the solving of this problem easier or enable the use of domain-specific tools for the
workflow.
Increasing the proportion of ML concepts is similar.
A ML domain expert will identify structures and techniques from the ML domain to cast the problem into.
This may be to specify the technique used for classification or learning, or the representation that the problem
should take. This is the transformation which represents our challenge question: mapping a DS problem to
a form suitable for ML.
Direct Mapping Transformations are also possible directly between the domain-specific and machine learning problem regions. This transformation is how to take
a problem which exists in the domain and map it to a
problem in the machine learning space, or to create a
many-to-many mapping. This opens up further possibilities for insights and implementation.
Here we identify two possible techniques for mapping: expert mapping and ontological/formal mapping.
In expert mapping, a group of experts from both the
domain of interest and the machine learning domain
issue recommendations about how to map the problem. This is shown by Huang et al. where problems in
genomics are mapped to machine learning representations [52]. This is a high effort technique, but could
greatly assist with workflow and implementation creation.
This expert mapping is of course possible in other
domains. Aneja et al. provide a table mapping the problems addressed in the neuro-oncology literature with
the ML approach used in those papers [6]. Jablonka et
al. provide another detailed review with mention of how
problems in material science were mapped to ML [55].
Another technique is to perform formal or ontological reasoning. In this technique, the two domains would
be modelled and a reasoner would perform the mapping. An example would be performing ontological reasoning. This may offer more potential for automation.
However, the domains themselves would have to be explicitly modelled [100].
Reversing the Transformation In principle, these transformations could be reversed. That is, a problem could
be made more general with the same techniques, and a
machine learning problem could be mapped to a domainspecific one. Improving the generalisation and mapping
possibilities for problems would increase the workflow
and implementations options available to practitioners.
4.2 Solution Workflow Space
In the second layer of our framework, we define a space
of solution workflows. These workflows detail the actions required to solve the problem defined on the upper
layer.
4.2.1 Artefact Representation
The representation of these workflows is based on those
described in Section 2.3 with some available standards
presented in Section 6.1. The core aspect is that these
workflows consist of a directed sequence of components
with explicit control and/or data flow. These components represent a step or action in the workflow, and
they can be typed to enforce structure on the accepted
inputs and outputs and define their semantics.
Figure 4 shows a few components from a workflow
defined in the Galaxy workflow management tool [57].
Galaxy is further discussed in both Section 6.2.2 and
Section 7.3.3.
The idea with this representation is to have a unified, graph-like structure amenable for modularity, reuse, modification, and sharing. As mentioned in Section 2.3, workflows are already common in scientific
domains and structured “pipelines” are in place in the
data science/machine learning world. Therefore our conceptual framework solely focuses on graph-like workflows as the representation for this middle layer.
4.2.2 Layer Regions
In this space, we again roughly classify workflows into
four regions as shown in Figure 5.
A general workflow is one where there are very few
domain-specific or machine learning components within
the workflow. Thus it is a catch-all category comprising
those workflows not discussed below.
In our framework, a domain-specific workflow is one
that has many components from the domain of interest. These components must address a domain-specific
concept which is not of interest to a general user outside of that domain. Examples include loading a file
or database with a domain-accepted structure, a computation performing a specific task of interest to the
domain, or communication with domain entities such
as robotic arms.
We also consider a rough spectrum where some workflows have more domain-specific components than others. For example, one workflow may simply load data
from an EEG file and visualise it, while another may
perform filtering or spectrum analysis on the data. This
second workflow is thus more domain-specific than the
first.
Similar to our category of domain-specific workflows,
a machine learning workflow is one that contains ML
components. Again, we state that there is a rough spectrum of these workflows from not including machine
learning components to heavily relying on these components.
The blended workflow is one that contains numerous
domain-specific and machine learning components. As
well, a component itself may be labelled as blended, as
it may address a domain specific concern but heavily
utilise machine learning “within” the execution of the
component. We propose that this blended type of workflow is desired for a domain expert to arrive at, since
the presence of these components should raise the level
of abstraction and increase the modularity and reuse
of the workflow. However, it may be preferable for a
domain expert not familiar with ML to begin working
with a DS workflow, and have the workflow ‘adjusted’
to become more blended over time as they gain familiarity with ML concepts and components. This offers the
domain expert further experimentation, customisation,
and optimisation possibilities.
4.2.3 Layer Transformations
We have posed two interesting questions in the introduction of this article of how to transform a workflow
along these two dimensions. That is, to identify the
techniques to: a) increase the domain-specificity, and/or
b) usage of machine learning in a workflow. These correspond to our challenge questions of: a) adding DS
knowledge to improve ML performance, and b) exper-
imenting with ML tools and techniques within a workflow.
A first approach is to ask a domain or machine learning expert to study the workflow and identify where
components should be added or improved. Their knowledge could then be modelled and implemented for automated approaches to detect and suggest components
for use, such as that implemented by Kumar et al. [65].
These recommender systems could therefore shift the
workflow along the domain-specific or machine learning dimensions.
For example, a workflow may load genomic data
from a table provided in a spreadsheet for further processing. Depending on the requirements of the user, the
loading components may be better replaced with a component which is able to download up-to-date genomic
data directly from a cloud repository as is available in
tools like Galaxy.
Domain-specific workflows can also be utilised as
a sub-workflow. For example, Sections 6.2.1 and 7.3.1
discuss the fMRIPrep workflow which is for performing
specific pre-processing for neuroscience data. Thus, a
domain expert’s workflow becomes more DS when fMRIPrep is used.
The error of ML techniques may also be lowered
when DS information is used. One aspect of this is the
field of feature engineering where new data is extracted
from the old to reduce the error of machine learning
algorithms such as deep learning [12]. For example, Fan
et al. study the problem of marking reported software
bugs as ‘valid’ or ‘invalid’ [37]. From the bug data, they
extract new features such as recent number of bugs by
reporter, does the bug have a code patch attached, and
bug text readability scores.
Reversing the Transformation Just as with the layer
transformations for the problem space (Section 4.1.3),
these transformations could indeed be reversed to increase the generality of the workflows. That is, to make
a workflow less DS and involve fewer ML components.
This may help to increase the applicability of the workflow across domains, however we do not consider it further.
4.3 Implementation Space
Similar to the above layers, the implementation space is
also a rough categorisation of possibilities. In our conceptual framework, the implementation space defines
the low-level result which runs on a computational device, such as produced code or the execution of a workflow engine. For example, some workflow management
tools are directly implemented in Python, or the Orange
editor (Section 6) can directly execute the workflow inside the tool.
4.3.1 Artefact Representation
In this space, the artefacts are represented as code or
another machine executable format. This may be Python
code which contains calls to ML APIs, or may be the
machine code executed by a workflow engine which is
directly interpreting and executing the instructions within
a workflow.
These two examples are not at the same level of
abstraction. However, the intention with this representation is that: a) this code directly calls upon domainspecific and machine learning APIs, and b) this code
should not be written directly by a domain expert as
the level of abstraction is too low.
Fig. 6 A representation of the implementation space, with
intra-layer transformations.
4.3.2 Layer Regions
Similar to the above layers, the implementation space
layer is defined by the same two dimensions. The domainspecific dimension defines the proportion of the code
which calls upon domain-specific APIs or libraries. The
machine learning dimension defines the proportion for
machine learning APIs or libraries.
A general implementation contains a small proportion of calls to DS or ML APIs or libraries. Thus it is
general code.
In a domain-specific implementation the code makes
calls into an API or library which provides domainspecific computation. For example, the nipype library
(Section 6) offers a neuroscience-specific Python library.
Thus the more calls to libraries like these, the more
domain-specific the implementation.
Likewise, a machine learning implementation has
a high proportion of machine learning API or library
calls. An example would be directly calling Tensorflow
or other ML library from Python.
A blended implementation is one which uses both
domain-specific and machine learning APIs and libraries.
Thus the ML learning libraries are wrapped in a domainspecific interface, and potentially optimised for each
domain-specific task. Clearly it would be desirable for
the domain expert to produce this form of implementation to achieve the most specific implementation. However, the domain expert should not write the implementation by hand, and instead generate an implementation from their workflow.
4.3.3 Layer Transformations
Again, the same transformations as the solution workflow layer occur in this layer. Code can be mapped
manually or automatically to either a domain-specific
library call or a machine learning one.
These tasks could be useful for addressing legacy
code and updating it (called “cognification”). However,
as argued in Section 8, it is not be efficient to focus on
mapping and recommendations at the implementation
level. Instead, a more efficient approach would be to
extract the workflow from the code and apply analyses
at the workflow level.
5 Inter-layer Transformations
This section defines the possible transformations used
to transform an artefact in one of the layers in our
framework to another layer. Section 6 then provides
examples of state-of-the-practice tools which support
these transformations.
The transformations discussed here are: a) from the
problem space to the solution workflow space, and b)
from the solution workflow space to the implementation space. Note that transforming a problem from the
problem space to the implementation space is classical
programming, which we do not elaborate further in this
section but appears in case studies in Section 7.
5.1 Problem Space to Solution Workflow Space
Transformations
The transformation between the first two layers of our
framework transforms problems from the problem space
into workflows in the workflow space. This transformation corresponds to our challenge question of obtaining
a solution workflow for a DS and/or ML problem. Practically, this transformation is most likely a combination
of a domain expert building and/or finding workflows
and workflow components.
That is, a domain expert could: a) find an existing workflow or components in a repository, b) rely on
formal or informal mappings or recommendations to assemble a workflow, or c) build the workflow themselves
either from a component library.
Here we will summarise a few of the techniques
available in the tools from Section 6 to assist a domain
expert in obtaining or building a workflow.
Component Libraries Many of the graphical workflow
tools (see Section 6.2.2) use a library of components for
the domain expert to select from when building their
workflow. Plugins or extensions can extend this component palette with domain-specific components, allowing
for easier selection of these components. For example,
the Galaxy tool offers workflow components which directly obtain data from biology databases. This aids
biologists to efficiently obtain up-to-date data directly
into their workflows.
Domain-specific Tutorials and Sample Workflows The
documentation surrounding a workflow tool often provides numerous examples for using the tool and for solving real-world problems. For example, the Nipype tool
discussed in Section 6.2.1 offers over 30 neurosciencespecific examples on its website. This allows users to get
started quickly to solve their domain-specific problems.
Workflow Repositories Some of the workflow tools discussed in Section 6 have explicit repositories for searching and obtaining workflows, or have multiple tutorial workflows for demonstrating the use of their components. These repositories allow for experts to select
whole workflows and their component parts for use in
solving their problem.
However, a brief glance at these repositories suggests usability issues. For example, one Galaxy workflow repository7
contains hundreds of workflows, yet
the only search options available cover free text, user
rating, and keyword search. This may make it quite difficult for a domain expert to find a suitable workflow
unless techniques are used to further recover semantic
information [27]. Reproducibility issues may also hamper this search as computations may not be consistent
between runs or user machines [105].
Automated Recommendations Recent work by Wen et
al. suggests that it may be possible to automatically
determine similarity of workflows in repositories [113].
This could allow for enhanced discoverability of workflows.
Workflow tools can also recommend next components to be placed automatically. This allows for domain experts to be assisted by the tool to build their
workflow. For example, the excellent article of Kumar
et al. presents a recommendation engine for the Galaxy
framework [65]. This engine integrates into Galaxy itself to provide component recommendations based on
the existing components and the recent usage of that
component in the data set. Figure 7 shows the tool providing a list of recommended next components for the
user to select from.
7 https://usegalaxy.eu/workflows/list_published
Fig. 7 Automated recommendation of a component. Modified from [65].
Automated Creation An interesting technique to create
the whole workflow at once is to use machine learning
techniques themselves to create workflows. This is the
field of AutoML [51], which uses accuracy metrics to
create a machine learning pipeline for the domain expert’s data. A partial or full workflow for the expert can
also be provided based on their problem and/or their
data [45, 44]. As a recent example of this AutoML approach, we point to Dunn et al. who use a benchmarking
set in materials science as the basis for creating material
science-specific workflows [29].
5.1.1 Region Transformation
Figure 8 diagrams some of the possible transformations
between regions on the problem space layer into the solution workflow layer. That is, a domain-specific problem (DSP) could be solved with a machine learning
workflow (MLW). As indicated in the figure with bolded
arrows, the two preferable transformations are to take
the original domain-specific problem and directly create a domain-specific or blended workflow. This retains
the domain-specific nature of the problem and adds the
required machine learning components.
5.1.2 Reversing the Transformation
As mentioned above, it can be challenging for domain
experts to search a workflow repository and find suitable workflows for their problem. One direction to address this issue is to automatically ‘mine’ the workflow
itself and extract the problem that workflow solves, or
at least extract some tags and other semantic information [27].
5.2 Solution Workflow Space to Implementation Space
Transformations
The transformations between the middle and bottom
layers of the framework transform a workflow in the
solution workflow space into some form of code in the
implementation space (Section 4.3). This corresponds
to our challenge question of producing an implementation from a workflow which is usable for a domain
expert.
The techniques examined here are: a) re-implement
the workflow manually (not discussed below), b) code
generation / Model-Driven Engineering (MDE) techniques, or c) workflow execution directly performed by
the workflow tool.
Fig. 9 Transformations between the solution workflow space
(inner boxes) and the implementation space (outer boxes.
5.2.1 Model-Driven Engineering Techniques
From a workflow defined in a DSL or as components, it
can be a straightforward process to perform MDE techniques such as code generation [7]. Due to the modular
nature of the workflows, executable code could be generated for each component.
This code generation may also take place over a
number of intermediate languages, such as using workflow middleware to handle concerns such as scalability
(Section 6).
5.2.2 Direct Execution
Another way of executing the workflow is to run it inside the workflow tool itself. This relieves the domain
expert from running the final code themselves, though
it may be more difficult to optimise if needed. Many
of the tools in Section 6 execute the workflow in this
way, either through the host language such as Python
or within the tool itself such as Galaxy. This execution
may also be local on the domain expert’s machine or
run on another machine.
5.2.3 Reversing the Transformation
An interesting direction of research is to consider taking legacy code and extracting the workflow from it as
in our challenge question: extract a workflow from an
existing implementation. This could be a manual inspection or an automatic process. Once completed, the
workflow could then become the source of truth and
could be moved into a workflow repository for further
dissemination and development [15].
6 Workflow Standards and Tools
This section provides another contribution of this paper: an introductory (and therefore non-comprehensive)
selection of workflow standards and tools available to
experts from various domains. The intention is for readers to gain a quick understanding of the diversity and
features of what is available today.
Limitations The primary limitation of this section is
that no delve into the literature can reasonably cover
the overwhelming number of workflow systems available. As a lower bound, Amstutz et al. maintain an incomplete listing of more than 300 workflow systems [5].
Instead, the selection in this report is to focus on
open-source scientific workflow tools reported in the
literature. That is, the standards and tools selected
are not targeted towards business, application development, or those workflows which are built within a
tool or platform8
. In this article, the field of biological sciences is very well-represented. This is due to the
combination of big data and reproducibility concerns
which motivated the creation of such tools [115, 91].
This report also aims to be a general introduction
and does not touch on many of the “ilities” relevant
for domain experts to use these tools. For example,
Wratten et al. evaluate twelve bioinformatic workflow
managers using the categories of ease of use, expressiveness, portability, scalability, learning resources, and
pipeline initiatives [115]. Admed et al mention modularity and reproducibility amongst others [2], while Kortelainen adds the important characteristics of licensing and maturity [63]. Other factors may be connection to specialised tools or computing platforms such
as the Hermes middleware platform for increased scalability [61].
6.1 Workflow Formalisms and Standards
Workflows can be represented in the simplest form as
a connected and directed graph, where nodes in the
graph are computations and the edges are dependencies
of data or control. Extending beyond this representation are well-known formalisms which can also represent
workflows.
For example, Petri Nets [95] can allow for formal
verification of properties such as liveness for the system,
or a Formalism Transformation Graph + Process Model
(FTG+PM) can record the formalisms and transformations employed in the workflow [17]. Another wellknown workflow standard is the Business Process Model
and Notation (BPMN) [18] to formalise both automatic
and manual workflows within an organisation.
Bringing together both Petri Nets and BPMN is Yet
Another Workflow Language (YAWL)9
. This workflow
language from the 2000’s takes Petri Nets as a starting
point and adds extensions for commonly-seen workflow
patterns [108]. The formal semantics of YAWL allow
for verification of workflow properties such as soundness
(ensuring an option to complete, proper completion, and
no dead transitions) [116].
More recently, a number of workflow standards have
been developed in various sub-fields but none has yet
established dominance over the others [97]. This may
soon change with convergence on the Common Workflow Language (CWL)10
.
CWL originated in the bioinformatics community
and offers a declarative workflow definition language
(a DSL) that can be written in JSON or YAML to be
executed by a workflow execution engine [21]. Of particular interest to this report is that DS attributes can be
added to workflows and their steps as needed by users,
allowing for a great deal of flexibility and discoverability
for domain experts. The standard is becoming established throughout multiple domains and has a number
of implementing tools, including upcoming support in
the graphical Galaxy workflow tool discussed below.
9 https://yawlfoundation.github.io/
10 https://www.commonwl.org
6.2 Workflow Tools and Management Systems
Workflow tools and management systems can be related
and considered as descendants from programming build
systems [73] such as make [101] and SCons [62]. The objective is to record and manage the dependencies of each
component, such that the computation can be correctly
executed.
However, the wide variety of workflow management
tools and systems available today have an expanded set
of concerns beyond compilation steps [98, 88, 91]. This
can include automatic versioning and provenance concerns, deployment to computational resources, and providing components for use in workflows. In particular,
there is a strong usage of these systems on containerisation and package management to ensure that workflows
can be re-executed in the same context that they were
first developed in. The strong focus of these systems on
the scientific requirement for reusability and reproducability is further discussed in Section 8.
This section will touch upon some workflow systems
found in use today and report some of the interesting
features and considerations implemented.
6.2.1 Text-Based
Current text-based workflow systems seem to follow two
approaches: either the system is implemented as a module/library for a general programming language such as
Python, or the system ingests a standard markup language/DSL.
Language Module A common implementation strategy
for workflow tools is to leverage the user’s knowledge
of a general programming language. Commonly, this is
Python due to its widespread usage.
For example, luigi is a tool from Spotify11 which allows a user to build up a dependency graph of Tasks
which interact with Target files. These concepts are
defined within Python code and the Luigi API offers
access to common database/cloud tools. A web-based
scheduler and visualiser is also available for monitoring
long-running workflows.
Luigi was extended by Lampa et al. into SciLuigi [67]
for scientific workflow requirements such as a separation
of the workflow and the tasks, audit support, and support for high-performance computing. The authors then
developed SciPipe12 in the Go programming language
for enhanced type-safety and performance [68].
Workflow systems defined as language modules can
also be tailored to particular domains, further reducing
the amount of code a domain expert must write to use
the workflows.
For example, the automate tool13 for computational
materials science [76] offers workflows to copy and customise based on specific analysis of materials, and an
API to the analysis tools themselves. atomate uses the
FireWorks workflow software which provides provence
and reporting support for high-throughput computations [56].
Another example of a domain-specific library for
workflows is the nipype Python software package14 to
define workflows in neuroimaging [48]. The intention
here is to define components commonly used in neuroscience and have them as part of the same workflow. This allows domain experts who know Python to
quickly build a workflow of neuroscience-specific tools.
Moving one level of abstraction higher, fMRIPrep15
is an automated workflow built on top of nipype [32,
31]. fMRIPrep adapts to the input data automatically
to performing the appropriate preprocessing steps for
functional magnetic resonance imaging (fMRI), such as
head motion correction and skull stripping. This assists
in providing replicable results for neuroimaging studies
both in terms of computation and by providing “boilerplate” natural language text for insertion into a research article’s method section.
Replicable results are also important when considering the development of ML models. The emerging field
of Machine Learning Ops (MLOps) tackles the automation, provenance, performance, and other aspects of ML
in a workflow-based form [92]. The ZenML Python library16 provides a high-level API to machine learning
tasks and tools, while offering workflow management
features such as versioning, scheduling, and visualisation.
Markup or Domain-Specific Language The other workflow specification commonly seen in workflow management systems is to have a definition written in either
a markup language (such as XML YAML) or a custom
DSL for the workflow itself.
Compi 17 is a framework to not only build and run
workflows, but also deploy the workflows as commandline applications or containerised as Docker containers [74]. That is, once a domain expert has built a workflow, Compi packages the workflow and its dependencies
can be easily shared to other domain experts to use as
a command-line application. Compi uses the markup
13 https://atomate.org
14 https://nipype.readthedocs.io/en/latest/
15 https://fmriprep.org/en/stable/
16 https://zenml.io/
17 http://sing-group.org/compi/
language XML to define the workflows as the creators
L´opez-Fern´andez et al. argue that a DSL for defining
workflows is “less interoperable, being difficult to produce or consume from languages other than the one on
which the DSL is based”, and that XML is “easy to validate syntactically and semantically through schemas” [74].
A repository of Compi workflows is available through
the Compi hub project18 which aims to provide community exploration of the workflow, including automatic
visualisation of the workflow tasks and links to sample
input data [84].
Nextflow19 is a workflow management system “designed specifically for bioinformaticians familiar with
programming” [26]. Workflows are designed in a Bash
script-like DSL to manage data flow between different
workflow components. The Nextflow tool itself has support for obtaining and setting up Docker containers to
allow for greater reproducibility of workflows.
Nextflow also has an active ecosystem providing validated open-source pipelines. In particular, the nf-core
effort20 is a community-maintained effort to develop
“collaborative, peer-reviewed, best-practice analysis pipelines”[34].
Only one pipeline per data type/analysis is allowed, and
all pipelines require quality checks such as a common
structure, MIT licensing, continuous integration tests,
linting, and appropriate documentation.
6.2.2 Graphical
With the rise of “low-code” platforms, there are an increasing number of graphical workflow systems available [11]. A prominent example of this is the domain
of business applications, where providers such as outsystems21 and Mendix22 provide graphical interfaces to
create applications which can involve ML.
A workflow system straddling the domain-specific
and business domains is the Konstanz Information Miner
(KNIME) [10]. From the University of Konstanz circa
2007, this framework originally focused on pharmaceutical applications23 but has now scaled up for use within
large-scale enterprises. KNIME is based on the Eclipse
platform and offers a component library and canvas for
drag-and-drop connection of nodes. KNIME also offers
a repository for hundreds of components and workflows
available for use with a selection of curated components available24. Also relevant to this article is a feature within KNIME called the “Workflow Coach”. From
KNIME community usage statistics, this panel is able
to recommend the next component to use in the workflow25
.
The Workflow Instance Generation and Selection
tool (WINGS) 26 focuses on semantic workflows, where
each input and component has semantic information attached [45]. This information is represented in the form
of triples which allows for domain-specific information
to be used to select workflow components. WINGS can
use this semantic information to select components, input datasets, and parameter values [44].
Focusing on more domain-specific workflow systems,
we select three commonly-used graphical platforms: NodeRED, Orange, and Galaxy.
Node-RED The Node-RED tool is a web-based editor
for creating Internet of Things (IoT) workflows [20].
Nodes provide built-in functionality or can be customised
by adding Javascript code. Figure 10 shows an example
flow to remind a user to exercise. A node communicates
with a weather service to obtain the temperature. If this
value is above 15, then the flow communicates with an
activity tracker. If this reports that a user’s step count
is low, then an email is sent. Flows can be deployed either to the user’s local machine or many other embedded devices such as Raspberry PIs27. Nodes and workflows can be shared in an online repository28, allowing
users to enhance their workflows with new nodes29 and
sub-workflows.
Orange The Orange tool offers visual scripting of data
mining techniques including machine learning operators and visualisation capabilities [25, 24]. Originating
out of a bioinformatics research group, Orange focuses
on providing an easy-to-learn data science tool. A canvas is provided for users to drag-and-drop nodes from
a node library, where typed connections then aid users
in assembling a workflow. Figure 11 shows an example workflow where data is visualised before clustering
occurs with K-Means [87]. Note the option pane for
K-Means allowing a user to tune the parameters. The
clustering is then visualised.
Orange has two features which improve the reuse
of the tool and its workflows. First is the selection of
25 See https://www.knime.com/blog/
the-wisdom-of-the-knime-crowd-the-knime-workflow-coach
26 https://www.wings-workflows.org/
27 https://projects.raspberrypi.org/en/projects/
getting-started-with-node-red/
28 https://flows.nodered.org/
29 For example, ML nodes: https://flows.nodered.org/
node/node-red-contrib-machine-learning.
workflows available on the Orange website30. This offers 20 sample workflows for performing common data
science tasks such as performing principal component
analysis. The second feature is the robust add-on support which provides new nodes for workflows (which
are called “widgets” in Orange). For example, currently
there are add-ons for bioinformatics, education, and explainable AI available from within Orange itself. Users
can also create their own nodes to create DS workflows [46, 107].
Galaxy The Galaxy project is a web-based entire computational workbench for developing biomedical workflows [57]. It has spread to other fields as well with
over 5000 publications citing Galaxy31. The workbench
heavily focuses on concerns such as reproducability, provenance of data and tools, and sharing of workflows and
learnings.
Figure 12 shows the Galaxy interface from an online tutorial [19]. On the left is a pane for selecting tools
which in this example focus on genomics. The centre
pane is for displaying website, tool, or dataset information. The right pane details the history of the analysis.
These histories correspond to inputs and outputs of the
tools to be recorded and shared. These histories can also
be visualised on a canvas.
An interesting aspect of the Galaxy project is a
focus on community and specialisation. For example,
there is a main publicly-available Galaxy instance online32. However, to spread out computation costs and
offer the possibility of specialising the datasets and tools
available, Galaxy can run on a user’s local or cloud machine. Furthermore, these other Galaxy instances can
be customised into different workspaces.
We highlight three recent DS specialisations of Galaxy
which are publicly available online. Vandenbrouck et al.
developed a Galaxy instance for proteomics research [109],
Tekman et al. provide one for “single cell omics” [104],
and Gu et al. offer a ML focus [49]. These specialisations
each offer targeted DS tools, workflows, and computational resources, allowing domain experts to quickly
develop workflows.
6.3 Relation to Framework
The above tools focus on managing workflows for a user.
In this section, we provide general comments relating
these tools to the six questions specified in Section 1.
This is not intended to be a comprehensive analysis
and comparison of the tools, but instead suggest which
challenges are currently addressed, and which are not
yet addressed by these tools.
Mapping a DS problem to a form suitable for ML : For
the first question, none of the tools or their documentation address the issue of mapping a domain-specific
problem to a ML one. This is understandable, as the
workflow management systems focus on the workflow
and implementation layers of our framework. However,
further integration of problem specification and mapping into these tools may assist domain experts.
Providing a solution workflow for a DS and/or ML
problem :
This challenge is the core focus of these workflow
management systems as they provide the domain expert with the formalisms and assistance to build up the
workflow. However, it is clear that tools have different
ways of assisting the user, as described in Section 5.1.
This includes assisted workflow composition, domainspecific examples, component libraries, and workflow
repositories. Not yet fully addressed in all tools is automation techniques for constructing workflows such as
recommending components.
Allowing the domain expert to experiment with appropriate ML components in a DS workflow :
This challenge relates to the ease of which a domain
expert can modify their workflow to include ML components. The workflow tools described here do not offer
automated support for such a modification. However,
tools such as Orange attempt to ease the experimentation process for domain experts through its use of
typed component connectors, rich component library,
and visualisation support.
Adding DS knowledge to improve ML performance :
Only the WINGS tool was seen to improve the performance of ML techniques by utilising DS knowledge.
This is possible due to semantic reasoning of domain
knowledge which is used to select appropriate components and parameters. More ML-specific techniques
such as feature extraction are possible but there does
not seem to be integrated support for this challenge n
the tools examined here.
Producing an implementation from a workflow which is
well-suited for a domain expert :
This challenge is very well addressed by the tools
mentioned here. In particular, Galaxy offers powerful
computational resources in a web-based platform. This
allows bioinformatics experts to run their workflows on
specialised platforms.
Extracting a workflow from an existing implementation
(code or notebook :
None of the tools offer support for extracting workflows from existing code. However, the light-weight nature of the Python module-based tools could be seen
as an easy way to “lift” existing code into an explicit
workflow.
Summary Table 1 offers a general analysis on whether
the tools discussed in this section addressed the challenge questions. For each question, a summary of the
techniques from Sections 4 and 5 is presented. Symbols
then provide an indication whether the challenge is not,
partially, or more fully addressed by the tools. The last
column then highlights the best examples which address
each challenge.
From Table 1 it is clear that there are a number
of challenge questions which are not addressed in current workflow tools or their ecosystems. We also identify that while most tools offer support for constructing
workflows from problems, this is not yet an automated
process. Thus there are ample opportunities for improving the experience of domain experts to create solution
workflows as discussed in Section 8.
7 Case Studies
This section examines the use of the tools from Section 6 in various domains. Cases studies selected from
the scientific literature provide a sample of how experts
in each domain are building domain-specific workflows
utilising machine learning. This section thus serves to:
a) ground our framework in the state-of-the-practice,
and b) highlight research challenges and opportunities
where the modelling community can assist domain experts.
As a caveat, these case studies have been selected
in an ad-hoc and non-systematic manner. Instead, the
informal criteria was based on recent publication, available artefacts, and variety of domain. The intention is
to provide a flavour of the heterogeneity of the domains
and the recent use of tools for discussion, not an extensive literature survey.
We focus on three sets of case studies in this section.
The first set is where the case study has an implicit
workflow. That is, there is no explicit workflow graph
in one of the standards or tools reported in Section 6,
and the workflow is expressed in code. The second set of
case studies contains explicit workflow artefacts, where
the workflow is explicitly defined using a workflow standard/tool. The third set is one case study where the
high-level workflow itself is implicit, but it relies on a
sub-workflow defined using a workflow framework.
7.1 Case Study Overview
Table 2 lists the case studies examined in this report
and discussed throughout this section. Each case study
is provided an identifier based on the primary tool used
and a short description. The second column in Table 2
denotes whether the case study has an implicit, explicit,
or hybrid workflow, and the third column lists whether
the workflow is created textually or graphically. The last
column reports the regions through our framework that
the case study has artefacts in. That is, what “path”
the authors took through our framework from Section 3.
This can be ML, DS, or B for blended. The Kaggle case
also shows that a blended workflow can have a strong
lean towards one dimension. In this case the lean is
towards the ML dimension, represented by BML.
For each case study, the domain-specific problem is
described. Then, the regions and transformations from
Question Techniques Addressed Best Supporting Tool(s)
Mapping DS → ML Expert mapping, ontologies None
Problem → Workflow Workflow composition, examples, repos, libraries
WINGS, Nextflow, Nipype, KNIME,
Node-RED, Orange, Galaxy
Increasing workflow ML Suggestions, experimentation KNIME, Orange
Increasing workflow DS Knowledge representation, feature
extraction
WINGS
Workflow → implementation Containerisation, deployment, run
within tool
automate, nipype, Compi, KNIME,
Node-RED, Orange, Galaxy
Implementation → workflow Code mining, language integration Nipype
Table 1 Broad analysis of tool support for answering challenge questions.
Label Description Repres. Workflow Regions
Expression
CS PyTorch Detecting peaks in metabolomic data Textual Implicit B-B-B
CS MATLAB Classifying rock origin based on molecular structure (geochemistry)
Textual Implicit B-B-B
CS Kaggle Crowd-sourcing ML solution to marine biology challenge Textual Implicit ML-BML-BML
CS nipype Detecting depression from MRI images (neuroscience) Textual Hybrid B-DS-DS
CS Orange Data mining analysis for smart school Internet traffic. Graphical Explicit ML-ML-ML
CS Galaxy Classification of urothelial cancer (bioinformatics) Graphical Explicit DS-DS-DS
Table 2 Summary of the case studies.
our framework (Section 3) which are relevant are presented.
7.2 Implicit Workflow Case Studies
The first four case studies presented focus on implicit
workflows where there is not a workflow explicitly defined in one of the standards or tools from Section 6.
These case studies presented therefore cover cases where
the domain expert directly writes an implementation of
their problem, skipping the workflow layer of our framework (Section 3). A discussion of these implicit versus
explicit workflows is found in Section 8.
7.2.1 CS PyTorch
The first case study we examine represents the situation
where a domain expert encodes their problem directly
upon a ML library such as PyTorch or sklearn.
As a Suggested Practice Directly writing code on an
ML library is at a low-level of abstraction requiring a
great deal of ML knowledge. However, we have found
two recent publications from 2020 and 2021 where this
approach is suggested.
For chemistry students, Lafluente et al. present an
introductory workshop focusing on utilising Python and
visualisation/ML libraries [66]. The example Jupyter
notebooks 33 lead students through an introduction to
33 https://github.com/ML4chemArg/
Intro-to-Machine-Learning-in-Chemistry
Python, basic statistics, exploratory data analysis, classification, and regression.
In the field of materials science, Wang et al. suggest
that utilising Python code and the PyTorch library is
considered ‘best practice’ [111]. The example Jupyter
notebooks34 walk a domain expert through an example application to highlight ML techniques and considerations at a very granular level of detail. For example, the reader is taken through constructing the layers of a neural network in PyTorch, along with calling
the prediction/back-propagation functions. While this
work is very comprehensive and suggests many useful
and concrete suggestions for utilising ML in materials
science, we (kindly) suggest that this is the wrong level
of abstraction for a domain expert to utilise ML at.
While the libraries themselves already abstract the lowlevel details, raising the level of abstraction further may
be more appropriate for non-programmers.
Many factors may require utilising ML techniques at
this low level of abstraction may be required for functional properties. For example, obtaining high degrees
of parallelism is cited by Zhou et al. as one reason for
building a material science library upon PyTorch [117].
The PYSEQM library35 implements functions applicable for semi-empirical quantum mechanics models, offering a high-level and domain-specific interface which
is able to compute over the wide variety of GPUS which
PyTorch supports, offering a speedup over other tools.
Case Study As the publications from Lafluente et al.
and Wang et al. are targeted toward chemical science
researchers just beginning to utilise ML, we also present
here a case study of a chemical analysis tool peakonly
utilising ML.
Melnikov et al. present an application of deep learning to classifying and integrating peaks in raw liquid
chromatography-mass spectrometry (LC-MS) data [78].
The problem studied in the work is how to detect regions of interest (peaks) which occur in the noisy LCMS data. Figure 13 shows how the data is first classified by a convolutional neural network (CNN) as a)
noise, b) one or more peaks, or c) needs manual classification36. A second CNN then provides the integration
boundaries. The results from the CNN are validated
against another tool. The authors provide a graphical
tool peakonly to perform these actions and visualise the
output.
Problem Layer The DS problem specified in the case
study is to detect and integrate the peaks in the data.
The authors have transformed this into a blended problem by utilising the expert mapping given by prior work,
where deep learning is used to perform peak detection
and noise filtering.
Solution Workflow Layer Figure 13 displays a highlevel view of the paper’s approach to peak classification and integration. This forms the basis of the workflow components which we extract in Table 3. Note that
these steps are performed by a user interacting with the
peakonly graphical interface, though a runner script is
available.
Table 3 is our attempt at extracting the steps in the
workflow from the publication and tool of Melnikov et
al. The first column is the high-level step which summarises the individual steps in the second column. The
description column details what the step performs, with
the quoted text copied from the code to explain the DS
steps. The last column in Table 4 is our rough classification of whether the step is general (generic programming code), domain-specific (DS), machine learning (ML), or blended.
First, the DS file format is loaded into the tool.
Then an algorithm runs to detect the regions of interest (ROIs). These two steps are highly domain-specific.
The two CNNs are executed to first classify the ROIs
and then to integrate the ones with detected peaks. We
classify these as ML-intensive steps. Finally, the user is
presented with the ROIs in a list where they are able to
36 Figure reprinted (adapted) with permission from [78].
Copyright 2020 American Chemical Society.
visually inspect the plot. The data can then be exported
to a CSV file.
From our classification of these steps, it is fair to
say that this is a blended implicit workflow. There is a
balance of DS and ML components.
Implementation Layer The implementation for the peakonly
tool is in the Python language, with usage of common
data science/ML libraries (matplotlib, numpy, pandas,
scipy, PyTorch) as well as the DS library pymzML for
mass spectrometry data. This code can be classified as
blended due to the extensive mixed use of these libraries
within the tool.
Remarks The peakonly tool is an excellent example of
domain experts utilising ML to solve a DS problem and
providing an easy-to-use graphical interface to it. This
lowers the barriers to entry for other domain experts to
utilise ML on their similar problems.
7.2.2 CS MATLAB
For the second case study which focuses on using the
common MATLAB tool which combines data processing and ML techniques, we have selected a publication
from Hasterok et al. in the field of geochemistry [50].
The studied problem is to use the chemical composition
of metamorphic rocks to classify whether the origins of
the rocks were sedimentary or igneous. The resulting
MATLAB code is available on GitHub37
.
Problem Layer On the problem layer, there is a clear
DS problem of classifying rocks on their chemical structures.
However, the authors venture further into the ML
domain to determine which available ML classifiers are
best suited for their problem. They describe investigation of principal component analysis (PCA) to filter
the data before classification, as well as comparing Knearest neighbour, decision trees, ensemble trees, and
testing various parameters within these classifiers.
A robust knowledge about applying ML to their DS
problem is shown. Thus we can classify this paper as
addressing a blended problem. The method of transforming the DS problem into a blended problem is not
detailed, but based on the extensive related work cited
we surmise that the authors gained this knowledge by
reading past work which is a form of expert mapping.
Solution Workflow Layer As mentioned, the solution
provided by the authors does not contain an explicit
workflow. Instead, the MATLAB code forms an implicit
workflow operating on the input data and resulting in
a classification or prediction. The authors provide their
code in separate MATLAB scripts with comments, allowing us to reconstruct the predictor workflow and divide the scripts into DS and ML. Note that this table
contains workflows for both the training and prediction
processes.
From this overview of the workflow, we can conclude
that there is a mix of both DS and ML components.
Thus this is a blended workflow.
Implementation Layer Following the classification of
the implicit workflow as blended, it is clear that the
implementation is also blended.
This code was (presumably) hand-written by the authors. The exception is the code in the training step38
.
This code seems to have been generated by the MATLAB Classification Learner app39
.
Remarks From reading the publication of Hasterok et
al, it is clear that the authors have obtained a great deal
of ML knowledge in addition to their domain expertise.
They discuss pre-processing the data through principal component analysis (PCA) and perform a comparison between multiple ML classification techniques. This
38 train RUSBoost Classifier 30l 1000s 20190222.m.
39 https://www.mathworks.com/help/stats/
classificationlearner-app.html
knowledge of both domains is reflected by the classifications given by our framework, where all of the problem,
solution workflow, and implementation are blended.
The authors also leverage the ML functions builtinto MATLAB for performing the training and classification, including the use of a MATLAB app to generate
the appropriate training code.
The code provided contains an implicit workflow defined in MATLAB code. However, the authors have
taken the time to modularise this code into various
functions. This improves the usability and reproducibility of the code amongst other researchers.
7.2.3 CS Kaggle
Kaggle40 is an online data science platform allowing
data scientists to share models and code. Kaggle is wellknown for its “challenges”, where an organisation posts
their data and an evaluation metric, and asks the Kaggle community to come up with a solution to that metric. For example, the “NFL Big Data Bowl” challenge
asked for a prediction of how far one team will advance
on the field during one play [47]. The data provided
contained position, speed, and rotation information for
each player on the field, weather information such as
temperature, humidity, and wind velocity, and other
data points. Once the competition has ended, the organisation sometimes contact the winners to explain
their solution.
There are challenges in utilising Kaggle as a crowdsourcing tool to provide ML solutions for DS prob
lems [13]. Briefly, the benefits of this approach is that
domain experts can directly interface with ML experts
on Kaggle-hosted forums to share best practices and
domain-specific information. The hope is that this will
lead to knowledge transfer and provide high-quality insights for the domain experts, and offer money, prestige,
and valuable skill training for the ML experts [103].
There are a number of drawbacks, however. The domain experts have to spend effort to set up the contest
by providing prize money and accurate problem data.
Also, the solution provided by the ML experts may
not be immediately applicable to the DS problem and
lessons learned must be transferred back to the domain
experts.
For example, in the Killer Shrimp Challenge a trivial solution was found by participants. The data was
organised such that all data points with an index value
greater than or equal to 2917769 had the presence of the
killer shrimp. Thus the solutions of participants could
simply test the index of each data point to obtain perfect accuracy on the predictions.
As an example of the effort required to transfer the
ML lessons learned back to the domain experts, we
point to the excellent article of Sutton et al. [102]. This
article examines the top three solutions of a materials
science challenge to determine the impact of the representation versus the learning method on the final accuracy. They describe how the first-place solution was a
novel representation for material property ML.
Problem Layer Returning to the Killer Shrimp Challenge, the underlying problem is to detect the presence
of the species Dikerogammarus villosus (also known as
the “Killer Shrimp”) which causes environmental damage and is invasive in Europe. The specific Kaggle challenge is to take data points on water salinity, temperature, depth, wave exposure, and the presence of sand,
and predict whether the Killer Shrimp will be present
or not 41. We refer readers to the article of Bumann et
al. [13] for a full description of the challenge set-up and
interactions between the domain experts and challenge
participants.
It is interesting to note that the DS problem of predicting the presence of Killer Shrimp was effectively
turned into a problem of predicting 1 or 0 in a particular column of a spreadsheet. Thus we classify this as a
DS problem being mapped into a ML problem due to
the lack of DS concepts in the problem statement.
Solution Workflow Layer In this report, we will attempt to extract the (implicit) workflow from the publicallyavailable second-place solution [106]. The solution is
available as a Jupyter notebook which aids in the reconstruction of the workflow.
Table 5 displays our extraction of the workflow in
the solution. Note that similar to other workflows, we
define the loading and saving of CSV files as rather
general steps. Most of the remaining steps are solely
ML-focused. However, the author of the notebook has
also added two DS columns. The first added feature is
water density which is calculated from the temperature,
salinity, and depth values. The second column is a classification of the wave exposure value to record whether
the point is extremely or very exposed to waves.
In summary, this workflow is mostly comprised of
ML components. However, due to the presence of these
added DS features, one could say it is a blended workflow with a heavy focus towards the ML side.
Implementation Layer The Jupyter notebook solution
contains Python code and imports the expected data
science/ML libraries (numpy, pandas, matplotlib, sklearn,
xgboost). As the workflow is blended (though tilted
towards ML), the implementation can be said to be
blended as well.
Remarks It was surprising to see features added to the
data which were DS. Our expectation was that this sort
of DS knowledge would not be as present in Kaggle solutions, based on the expertise focuses of the challenge
organisers and the ML experts. For example, we wish
to highlight this quote from the analysis of Gordeev
and Singer on their winning entry for the football challenge [47]:
Don’t worry about having domain knowledge to
attempt a specific problem. The main thing we
learned in this competition is that you don’t necessarily need domain knowledge or industry [sic]
to successfully tackle the data science challenge.
Sometimes it even can be an advantage, as you
go in blindly without many prior assumptions
that might wrongly steer your exploratory analyses.
Thus, providing a transformation from the DS problem to a ML representation may have to be balanced
between prior DS knowledge and ML analyses.
7.3 Hybrid and Explicit Workflow Case Studies
The remaining case studies presented here are those
which explicitly represent the workflow (or a sub-workflow)
in one of the standards or tools from Section 6. As discussed in Section 8, an explicit workflow aids with reproducibility, modularisation, collaboration, re-use, etc.
We also note that the explicit workflows tend to
have a strong focus on enabling plugins or extensions for
domains. This means that users are able to customise
the workflows for their domains easily.
7.3.1 CS nipype
Practitioners may use workflow management systems
such as nipype to develop reproducible workflows focusing on particular domain processing tasks. For example,
Celestine et al. present a Python module42 for performing pre-processing workflows such as DS file conversion and skull stripping for small mammal MRI brain
data [16].
These pre-processing tasks are essential for transforming the data such that it can be treated with ML.
In this case study, we analyse a workflow which uses
fMRIPrep as a sub-workflow to process MRI data before it is used to predict whether the person in question has depression [81]. As mentioned in Section 6.2.1,
this fMRIPrep automated workflow is built on top of
nipype to perform pre-processing of fMRI data [32, 31].
As such, the fMRIPrep tool itself is an explicitly defined workflow. However, the authors of Mousavian et
al. have defined an implicit workflow in Python to orchestrate the usage of the fMRIPrep tool. Thus this is
an interesting hybrid workflow case study which utilises
an explicit tool workflow.
Problem Layer The specified problem of Mousavian et
al. is to classify MRI images on whether the subject
has Major Depression Disorder (MDD) or not. There
are three major challenges addressed in the article. The
first is to investigate different correlation measures of
the voxels (essentially three-dimensional pixels) of the
MRI data. These correlation measures relate different
areas of the brain together, and are used as features
for the ML classification task. The second challenge is
to handle imbalanced data sets where many subjects
within the set do not have depression which can cause
issues with classification. The third major challenge is
to determine which of 14 ML classifiers performs best
on the dataset.
From the problem and these specified challenges, it
is clear that this is a blended problem which combines
DS and ML concepts. Specifically, the correlation challenge is DS, while the imbalanced datasets and choice
of classifier challenges are ML-specific.
Solution Workflow Layer The case study implicitly defines a workflow through its use of Python scripts43
.
However, Mousavian et al. represent the workflow as explicit blocks in the article [81]. Therefore it is straightforward to classify each task in the workflow as DS or
ML as done for the other case studies.
Table 6 shows the workflow as defined in the article of Mousavian et al.. The steps present in the article
clearly identify that the majority of the workflow is DS.
In particular, only the feature selection and actual classification steps are ML.
Implementation Layer As the workflow of this case study
is mostly DS, it follows that the implementation is also
very DS. In particular, heavy use of DS libraries and
tools are used such as dcm2niix for format conversion,
PyDeface for removing facial structure from the images,
and the fMRIPrep implementation itself44
.
7.3.2 CS Orange
The case study for the Orange tool focuses on data mining analysis for Internet traffic from a smart school [1].
Problem Layer The article from Adekitan et al. is an
exploratory analysis on using machine learning techniques for prediction of Internet traffic at an educational institution. The specific problem is to predict a
classification for both download traffic and upload traffic among low, slight, moderate, and heavy data traffic.
The input information is a numerical day, week, and
43 https://github.com/moosavianmz/
DetectingDepression
44 https://github.com/nipreps/fmriprep
month, along with the previous day’s traffic and an average of the previous two days.
Multiple ML classifiers are used and compared in
this analysis from both the Orange and KNIME tools
mentioned in Section 6.2.2. As the intention was to compare ML classifiers of two different workflow tools, we
classify this problem as a blended problem.
Solution Workflow Layer Figure 14 shows the workflow of Adekitan et al. in the Orange tool, while the
workflow for KNIME is found in their article [1]. The
three general components at the bottom (File, Data
Table, and Box Plot) are used to load the data and visualise it. The Test & Score component takes the five
ML learners and the loaded data, and performs the ML
classification task. The results are then passed to the
four evaluation components on the right. We classify the
Test & Score component, the learners, and the evaluation components as all ML components. There are no
DS components in this workflow, however the feature
engineering described in the article means that domain
knowledge concerning the academic calendar of the institution has been encoded into the source data. Therefore, this workflow can be classified as mostly ML-based
with a DS feature engineering step.
Implementation Layer The execution for the Orange
tool can be performed within the editor itself, or by calling the underlying Python code defined for each component45. In Orange, the code for the components used is
built upon the scipy and scikit-learn modules. Therefore
we classify this implementation as mostly ML-based.
Remarks This case study represents an exploratory usage of ML techniques within a workflow. The authors
performed some DS feature extraction on the data and
then applied different classifiers to determine the performance. The classification performance found was quite
low (55 to 63% accuracy), indicating that further DS
feature extraction may be required to improve classification performance.
7.3.3 CS Galaxy
The last case study for this report details a workflow for
the Galaxy framework. The article of F¨oll et al. tackles
supervised classification of urothelial (bladder) cancer
using mass spectrometry imaging (MSI) [39].
Problem Layer The input data studied by F¨oll et al.
is obtained using MSI. This imaging technique is performed on a slice of tissue. For each region in the sample, the instrument provides a spectrum of the masses
of present biomolecules. That is, for each “pixel” of the
sample image a one-dimensional spectrum is created
where peaks correspond to a particular biocompound.
This can be used to visualise and classify regions of the
sample where a particular biomolecule is present.
In the problem of F¨oll et al., this MSI data is manually labelled by an expert as containing either tumor tissue or stroma (connecting tissue). Tumor tissue is then
further classified into invasive or non-invasive. Therefore the problem statement is to develop a classification
workflow which can pre-process and classify this unique
spectral data. This problem can be said to be DS as it
does not refer to the classification techniques used.
Solution Workflow Layer An extract from the Galaxy
workflow of F¨oll et al. is seen in Figure 4 on page 9. In
particular, these components are in the workflow which
classifies tissue as a tumor or stroma. The MSI classification component on the right-hand side of Figure 4
takes the MSI data and parameters and outputs a classification.
Similar to the other case studies, we present a broad
analysis of the case study workflows46 in Table 7. For
each workflow created by the authors, we classify each
component within as general, domain-specific without
ML concepts, or domain-specific with ML concepts47. A
percentage of the components which are DS is reported
in a column on the right-hand side of Table 7 along
with a classification of the workflow.
Table 7 indicates that the workflows for this case
study range from moderately DS to strongly DS. General components are used for dataset loading and manipulation while the DS components perform the nontrivial work. There are no non-domain-specific ML components in these workflows, and the component MSI
Classification performs the domain-specific classification computations. Thus it is clear that this is a DS
workflow.
Implementation Layer Workflows are run by Galaxy
through the web-based tool on either a public or private
server. The individual components are defined through
XML wrappers which define how to run the underlying
tool.
For these particular workflows, the majority of the
DS components are specific to MSI as they have been
created by the authors in a previous work [38]. These
components are wrappers around the Cardinal tool,
which is a R language module specifically for analysing
mass spectrometry-based imaging [9]. Thus the implementation of this workflow is mostly DS.
8 Discussion
This section provides discussion for the main research
topic of this article: what are the ways in which domain
experts can use workflow-based tools and techniques to
to solve their domain-specific problems using machine
learning. For this discussion, we first present the benefits and drawbacks for structuring this research topic
using our three-layer framework organised into two dimensions. Then we examine each of the challenge questions introduced in Section 1 and present what we see
to be remaining research and integration challenges for
the software engineering community.
8.1 Benefits and Drawbacks of the Three-Layer
Framework
This section discusses some benefits and drawbacks of
organising this research topic as a three-layer framework with inter- and intra-layer transformations.
8.1.1 Benefits
Separation of Concerns The main benefit of our framework is the separation of concerns into the three layers: problem, workflow, and implementation. Similar to
domain-specific languages, this ensures that the domain
expert first addresses the problem space which they are
familiar with, rather than dealing with the accidental
complexity of the workflow and implementation spaces.
The framework defines transformations between these
layers, offering the domain expert a structured way of
progressing their solution.
This separation of concerns is also present in the
workflow literature. For example, Lamprecht et al. [69]
define six stages of workflows over time: question or
hypothesis, conceptual workflow, abstract workflow (sequences of tools but not fully configured), concrete workflow (ready to run), production workflow (ready for
reuse), and scientific results. The first two stages of
question/hypothesis and conceptual workflow thus map
onto our notion of domain-specific problem.
Implicit versus Explicit Workflows Explicit workflows
are both conceptually (and literally) at the centre of
our framework. This is because we see numerous benefits with this formalism for domain experts to use in
combination with ML.
First, it is obvious that there is compatibility between the use of scientific workflows and ML pipelines.
They share the same underlying formalism due to the
same concept of control and data flow, as well as concerns about modularity and reuse. A workflow-based
approach also seems to be very amenable to visualisation and manipulation in graphical tools, allowing nonexperts to quickly build a workflow for their problem.
Second, these standalone components are a useful
abstraction over the technical details and complexity
of ML approaches. The domain expert does not have
to become familiar with the ML libraries or in some
cases even a programming language to orchestrate the
workflow. Again, this is in concordance with the principles of domain-specific engineering where the domain
expert should focus on manipulating concepts within
their domain.
Third, providing explicit components to the domain
expert allows for enhanced traceability, reuse, scientific
replication. As seen with the Galaxy tool, input and
output history can be kept for every component in a
workflow, along with explicit versioning and supporting
information.
Fourth, a standardised workflow system can offer
enhanced benefits for deployment on cloud or highperformance systems. For example, Lehmann et al. discuss the scalability benefits gained when porting an
implicit workflow orchestrated with the Bash shell language to the Nextflow workflow system [72].
In some domains, the use of explicit workflows is a
best practice. For example, Poldrack et al. discuss the
use of nipype for reproducible and scalable workflows in
neuroscience [89], while Reiter et al. provide a detailed
article of techniques for biology experts to get started
with workflows[91]. However, other fields may not have
such a strong culture of workflows and still recommend
coding for problem solving. As an illustrative example,
Wang et al. recently suggest for material scientists to
use PyTorch in Python for ML purposes [111].
Focus on Transformations Another benefit of our framework is the focus on transformations between regions of
layers, as well as between the layers themselves. These
transformations can be phrased as challenge questions
which are relevant to both software engineers and the
domain experts who must use these transformations.
This provides a clear intent for each transformation
and allows for analysis and identification of current approaches and new techniques.
8.1.2 Drawbacks
There are a number of drawbacks to our organisation of
the research problem onto this three-layer framework.
The first is that the two dimensions selected of domainspecific and employing machine learning are not orthogonal as mentioned in Section 3.1. The divisions of these
dimensions into regions is also crude as we are unable
to provide specific metrics to divide problems, workflows, or implementations due to the qualitative nature
of these dimensions. In particular, the classifications of
the problem, workflows, and implementations for the
case studies in Section 7 are very ad-hoc.
Second, restricting these complex systems onto three
layers is a gross simplification. In particular, we acknowledge that the implementation layer is most likely
made up of numerous layers of domain-specific or general programming languages. We have classified implementation code in some case studies as domain-specific
when this is just the top layer of what may be machine
learning or general code at the lowest layer.
Lastly, we also acknowledge the incompleteness of
this article to cover the research topic. It is impossible to fairly cover all domains or to give an impression
of how prevalent the usage of any tool or technique is
within a domain. This lack of comprehensiveness may
render our framework less applicable when applied to a
particular domain.
8.2 Challenges and Future Research Directions
In this section, we again present the challenge questions
from the introduction in Section 1. For each question we
then present our thoughts on how this challenge question has been addressed by the tools and case studies
seen in this article. We present the challenges and potential research directions for each question.
8.2.1 Mapping a DS problem to a form suitable for ML
The first challenge we have selected focuses on the problem layer. That is, how to assist the domain expert to
choose the machine learning techniques which may assist them.
Our analysis in Section 6.3 indicates that none of
the workflow frameworks discussed in this article tackle
this challenge. This may be expected as the challenge
is at the problem level, not the workflow layer.
This challenge is however very relevant to a domain
expert. For example, most of the case studies examined in Section 7 directly define a ML or blended problem. This could indicate that domain experts are having to gain sufficient machine learning knowledge to begin their study, instead of leaving the problem as a DS
problem. In particular, the case study of Kaggle (Section 7.2.3) shows that domain experts will go to great
lengths to obtain ML expertise on their problem.
Addressing this challenge involves bringing together
semantic information from the DS and ML domains.
In particular, ontological information could be used to
match problems in a particular domain with a ML specification [69].
8.2.2 Providing a solution workflow for a DS and/or
ML problem
The second challenge we observe is for the domain expert to efficiently discover and/or build a workflow which
solves their problem.
Many frameworks use a repository approach to improve the discoverability of workflows. That is, they
provide a website for domain experts to search for a
workflow which suits their needs 48. We also point to
the impressive Collective Knowledge framework [40] for
a repository focusing on AI, ML, and system research49
.
However there still remains a challenge to connect
the workflow solutions present in the repository with
the problem faced by the domain expert [41]. The literature discusses manual and automatic semantic extraction techniques which can assist domain experts in
finding workflows [27, 88]. However, enabling this atscale across multiple domains and tools will continue
to be a challenge.
As an example of the rich information to extract
from workflows, we point to the work of Lamprecht
et al. who discuss automatic discovery and the static
analysis of workflows [69]. This includes technical parameters (versioning, FAIRness metrics, usage, etc.),
domain-specific considerations (relevance of components
to a domain, similarity to existing workflows, type and
format of results, etc.), and community influence (citations, comments, ratings, etc.).
Automated workflow composition can also assist domain experts in building their workflows. A promising
approach is to combine the techniques of AutoML [51]
with domain knowledge about required domain-specific
components [60, 43].
Whether a workflow is found or not, the domain
expert is likely to want to add their own components.
Thus another sub-challenge is to improve the suggestion
possibilities for domain experts. Recommendations are
found in the KNIME, Galaxy, and low-code tools [3,
65], but we see further potential in this research area.
For example, suggesting larger pieces of workflows, improved semantic reasoning such that components relate directly to the domain [77], and employing machine learning techniques themselves to suggest components [85].
8.2.3 Allowing the domain expert to experiment with
appropriate ML components in a DS workflow
An interesting challenge is to encourage and assist a
domain expert with experimenting with ML techniques
within a workflow. For example, the Orange tool (Section 7.3.2 makes it simple to add ML components to
a workflow and visualise the results. This sort of visual experimentation fits perfectly with the componentbased nature of workflows and ties in well with the challenge of improving the automatic recommendation systems. This experimentation step can also be partially
automated by integrating AutoML techniques [51] or
recommender systems [65] into the workflow tool to dynamically react to workflow changes.
8.2.4 Adding DS knowledge to improve ML
performance
Another research challenge is how to utilise the DS
knowledge of a domain expert to directly improve the
performance of ML techniques. This is seen in some
case studies (such as in Section 7.2.3 and Section 7.3.1)
where the features themselves were modified to take
into domain knowledge. As with other challenges described here, one approach may be to combine domain
knowledge represented in an ontology with suggestions
for features to extract, such as provided by unsupervised feature extraction [99] or ontology embeddings [64].
8.2.5 Producing an implementation from a workflow
which is well-suited for a domain expert
Once a domain expert has created their workflow they
must be able to run it in a scalable manner. This is addressed in multiple tools from Section 6, but there will
always be further challenges to ensure that a domain expert can deploy their solution on the correct infrastructure. For example, code could be generated or parameterised based on the domain-specific tasks or data operated on, such as image- or voxel-based datasets [23].
The rise of containerisation also opens up many challenges to ensure that these containers are distributed
for optimal scalability and security [89].
8.2.6 Extracting a workflow from an existing
implementation (code or notebook)
The final challenge we highlight in our article is to convert the existing implementations a domain expert may
have into workflows. Amongst other benefits, this would
improve the modularisation and dissemination of these
solutions [15].
For example, Jupyter notebooks 50 are a well-known
paradigm for storage, dissemination, and reproduction
of experimental results [86]. Each cell in a notebook
contains text or executable code, where the results of
code are shown directly underneath. This format thus
provides a narrative to provide context for the code,
which is useful for disseminating results or tutorials on
a topic.
Rule et al. suggest that scientists spend time to
make Jupyter notebooks themselves form part of a workflow [93]. An interesting line of research is therefore to
develop tooling and techniques to automate this process, such that the legacy notebooks of domain experts
or machine learning experts51 can be automatically promoted to explicit workflows [15].
8.2.7 External Challenges
Beyond the challenges related to the framework itself,
we also identify two other challenges which are important to increase the impact of addressing the problems specified in this article. These challenges are: a)
strengthening the workflow community as a whole, and
b) proposing tools and techniques to guide a domain
expert in solving their problems.
Strengthening the Workflow Community For domain
experts to be able to effectively use workflows to solve
their problems using ML, there must be a strong crossdomain workflow community. This community will then
be able to pool knowledge and resources to best solve
domain problems.
The excellent article of da Silva et al. suggests current challenges and proposed activities in a workflow
community context [97]. The challenges they see are:
FAIR computational workflows, AI workflows, exascale
challenges and beyond, APIs, reuse, interoperability and
standards, training and education, and building a workflows community.
We also see other avenues to strengthen the workflow community. In particular, we note the recent research and commercial interest of low-code platforms
which are in some cases workflow management tools [53,
11]. It may be possible to leverage this interest into
further developing workflow management systems by
providing support for commercial domains. For example, the KNIME tool (Section 6.2.2 started development
for solving pharmaceutical applications, but has now
evolved to offer a commercial solution.
Crowdsourcing knowledge is also another possibility to build up the workflow community. For example,
Paul-Gilloteaux et al. suggest the organisation of regular “taggathons” to annotate tools, workflows, components, databases, and training materials with terms
from an ontology [88].
We also point towards Kaggle (Section 7.2.3) as an
interesting community of domain and ML experts. Despite the issues with crowdsourcing [103, 13], it may be
possible to further utilise this pool of knowledge. In
particular, we suggest that offering incentives for competition participants to include explicit workflows and
reusable components in their solution may assist with
reuse of their efforts.
Bringing in further expertise from software engineering sub-fields could also bring benefits to the workflow community. In particular, we draw from our own
expertise in model-driven engineering to suggest that
there are many research avenues to explore.
For instance, the multi- view/formalism/level of abstraction approach of multi-paradigm modelling may
assist in reducing the cognitive complexity of domain
experts [42]. A concrete example is providing views on
a workflow such that the domain expert can focus on
different aspects of the workflow as needed.
Another research avenue would be integration of
model management approaches such as modelling variability and uncertainty techniques into workflow management tools [36]. The last research avenue we propose would be the integration of verification and validity techniques such as recording performance metrics [22], enhancing type safety [33], and checking for
formal properties such as reachability [35].
8.2.8 Guiding the Domain Expert
The last challenge we mention in this article is how
to guide the domain expert in both finding the best
practices and tools for their domain, as well as their
path in the framework.
Recently there have been articles in multiple domains walking a domain expert through the best tools
and techniques available to employ ML [52, 75, 111, 66,
92]. For example, Nakhle and Harfouche provide four
detailed Jupyter notebooks52 walking domain experts
in phenomics (plant sciences) through four steps of a
ML task [82].
These four steps ([image] dataset selection, data preprocessing, data analysis, and performance analysis and
explanation) are representative of most ML workflows.
Therefore we suggest that similar dissemination efforts
in different domains may assist domain experts. In particular, collaborative knowledge bases for a domain expert to navigate the tools and resources available in
their domain may be useful.
Another tooling effort could be to dynamically assist the domain expert in producing template workflows
based on their domain-specific problem [71, 83]. However, this raises the question of how to assist the domain expert through the regions of our framework in
Section 3.
For example, consider three approaches to take a DS
problem and arrive at a blended workflow. The first approach is on the problem level, where the domain expert
is provided with basic ML knowledge to assist them in
refining the DS problem to include ML concepts. The
second approach is to immediately build a workflow,
and then use AutoML [51] techniques, assist the user
in experimentation (as in the Orange tool), or use ontological recommendations [77] to complete the workflow.
The last approach is to follow principles from humanguided machine learning to iteratively build out the
workflow [96, 43, 30]. In these three approaches, more
or less automation may be appropriate depending on
the task and user [112].
A further consideration is whether to hide or expose the ML concepts and components based on the
ML knowledge of the domain expert. This could allow
a user to work with a mostly DS workflow, and over
time adjust the workflow towards a blended workflow
as they gain insight and familiarity with the ML components.
9 Conclusion
This article presents a conceptual framework to structure the process and tools whereby domain experts can
utilise machine learning to solve their problems. In particular, we focus on the computational workflow representation of solutions where executable components are
connected by control and data flow edges. Examining
the state-of-the-practice, we identify six key challenges
that a domain expert may face in developing an executable workflow:
– Map a DS problem to a form suitable for ML
– Obtain a solution workflow for a DS and/or ML
problem
– Experiment with ML tools and techniques within a
workflow
– Add DS knowledge to improve ML performance (e.g.,
feature engineering)
– Produce an implementation from a workflow which
is well-suited for a domain expert (in terms of scalability, DS tooling, etc.)
– Extract a workflow from an existing implementation
(code, Jupyter notebook)
These challenges are represented by transformation
within regions of our conceptual framework. This framework has three layers, consisting of the problem layer,
workflow solution layer, and implementation layer. Each
layer is further structured with two dimensions representing the domain specificity and machine learning usage of the artefacts on that layer.
This conceptual framework structures our investigation of the state-of-the-practice of how domain experts
are employing machine learning. In particular, a selection of textual and graphical workflow tools are presented to illustrate tool support for the challenges we
have identified. Case studies selected from recent works
in various domains further explore how the problems,
workflows, and implementations created by domain experts are heterogeneous in terms of the amount of domain specificity and machine learning usage. We also
provide a short discussion on each challenge to indicate
possible research directions.
This article thus forms a basis for further discussion and research into assisting domain experts with
developing workflow solutions which employ machine
learning. Integrating best practices from software engineering and across tools will reduce the friction for domain experts to utilise these powerful techniques and
unlock new possibilities in their application to pressing
scientific issues.
Acknowledgements The authors would like to thank our
colleagues Jessie Galasso-Carbonnel and Istv´an D´avid for their
insightful discussions on this article.
Conflict of interest
The authors declare that they have no conflict of interest.