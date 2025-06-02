Title: Information Retrieval for IoT and WoT: State-of-the-Art, Taxonomy Framework, and Evolutionary Directions

Abstract—The explosive growth of Internet of Things (IoT)
and Web of Things (WoT) technologies, characterized by a vast
diversity of devices and data formats, producing vast volumes of
information at a high pace in real time necessitates a paradigm
shift in information retrieval (IR) systems. Traditional IR struggles to navigate the dynamic landscapes of these interconnected
environments. This work proposes a multidimensional taxonomy
framework to bridge this critical gap. Our framework not only
unifies existing classification approaches but also delves into the
analysis of traditional IR subtasks, thereby establishing a cohesive
foundation for future advancements in IR tailored to the evolving
IoT/WoT landscape. We further contribute by identifying key
challenges and posing open research questions, thus propelling
the development of next-generation IR techniques specifically
tailored to the intricate search demands of the evolving IoT and
WoT cyber-world.
Index Terms—Information retrieval (IR), Internet of Things
(IoT), search engines, survey, Web of Things (WoI).
I. INTRODUCTION
T HE Internet of Things (IoT) drives new trends and
paradigms that enable close interaction between endusers and the real world. To promote universal adoption and
overcome scalability issues, the World Wide Web Consortium
(W3C) and research communities advocate the integration of
Web technologies. The Web of Things (WoT) provides Weblike access to advanced services while allowing interaction
and manipulation of physical objects through virtual representations known as Avatar Web [1] a.k.a Digital Twins. WoT
dynamics differ from the traditional Web due to real-time
human interaction with intelligent cyber environments. WoT
abstracts a massive number of physical and virtual objects in
the real world by generating a vast amount of information
at a high pace. As the WoT paradigm evolved, abstraction
layers became complex, and technologies merged to create
the Semantic WoT, leading to the vision of the Wisdom
WoT.
IoT and WoT-based applications are changing the way we
consume information. Information retrieval (IR) is one of the
most valuable forms of WoT-based applications, providing
cyber-search functionalities to boost the smart cities paradigm.
Next-Generation IR is a broad discipline that adds modern
theoretical tools, such as learning, causal inference analysis,
and interactive decision-making. IR systems seek relevant
information that satisfies a user’s information need within
extensive collections [2].
IoT Search Engine (IoTSE) and WoT Search Engine
(WoTSE) have been identified as one of the top 10 research
topics in the IoT spectrum [3]. IoTSE and WoTSE refer
to systems that allow humans and machines to retrieve IoT
content, such as sensory data and digital representations
of physical entities. While the terms are sometimes interchangeable, IoTSE focuses on finding physical entities and
searching for raw or linked data. In contrast, WoTSE can
find services and actions performed by digital representations of things. WoTSE can also search for things based
on social relationships and ideally provide universal search
capabilities.
Traditional IR systems have yet to be adequately tested
or evaluated in the constantly changing and dynamic environments of IoT and WoT, which present new risks and
challenges. Therefore, the search community must reconsider
the conventional IR systems, including their scope, architecture, and internal stages. In our survey on IoTSE/WoTSE,
we aim to classify different aspects of this field comprehensively. We analyze the evolution of the IoT/WoT-IR process,
characterizing the context of applying IR techniques to IoT
and WoT for searching any type of information that fulfills the
exact user needs in these environments. Our secondary goal
is to identify open research topics in the short and long term;
we suggest evolutionary directions for applying IR to IoT and
WoT.
The main contributions of this article can be summarized
as follows.
1) Identification of Challenges in IoT/WoT for IR: This
work recognizes the limitations of traditional IR systems
in the context of the IoT and WoT landscapes. It
highlights the need for a paradigm shift in IR to
accommodate the highly dynamic, interconnected nature
of IoT/WoT data.
2) Development of a Multidimensional Taxonomy
Framework: This work proposes a comprehensive,
multidimensional taxonomy framework designed
specifically for IR in IoT/WoT. This framework unifies
Fig. 1. SLR Protocol for IoT-IR and WoT-IR.
various classification methods already in use, providing
a cohesive structure to analyze and categorize IR within
these environments.
3) Detailed Analysis of Traditional IR Subtasks: The framework enables a deeper examination of traditional IR
subtasks (such as indexing, query processing, ranking,
and retrieval) and their adaptation to the requirements
of IoT/WoT. The framework offers a robust foundation
for future research.
4) Identification of Key Challenges and Open Research
Questions (RQs): Besides the taxonomy, this article
highlights specific challenges and unresolved questions within IR for IoT/WoT. These insights would
encourage further research and innovation, paving
the way for the development of next-generation IR
systems.
This article structure is as follows. Section II describes the
systematic literature review (SLR) performed, tracking the
maturity of the pioneer works from 2000 to the present
year 2024 related to IR’s applicability to the IoT and WoT
paradigms. Section III presents state-of-the-art details for each
of the main IR subtasks. We contrast previous Survey-like
works in Section IV, examining taxonomies and classification
frameworks for IoTSE and WoTSE systems. This section also
gives our proposed unified and holistic MultiTaxonomy
Framework for IoTSE and WoTSE. In Section V, we explore
the evaluation frameworks for IR-IoT/WoT. Section VI discusses open RQs, examining architectural and technical
challenges on IR for IoT and WoT; we present short and
long-term open research topics and evolutionary directions for
the IR field, such as progressive search and IR on the social
WoT. These insights can guide future research in the field. We
conclude with our final remarks, summarizing the essential
findings and contributions of our work.
II. SYSTEMATIC LITERATURE SELECTION, REVIEW,
AND ANALYSIS METHODOLOGY
This article provides a comprehensive review of search
engines for IoT and WoT; see Fig. 1. This section outlines the
process performed for collecting and selecting primary studies,
including the criteria for inclusion and exclusion. It delves
into the IR process for IoT and WoT scenarios, defining RQs
and selection strategies. Full details of the SLR can be found
on GitHub and IEEE Data Port(TM). Therefore, this article is
linked to SLR Protocol,1 and the final version of the extracted
data and analysis available as open dataset in GitHub.
Definition of Research Questions:We define the following
mapping questions (MQs), which support and guide the scope
of this SLR. MQ1: How many studies have been published
over the years? MQ2: Who are the most actives researchers
in the area? MQ3: How has the IR subtasks on IoT and WoT
evolved over the years? MQ4: Which challenges have been
identified, and which open RQ still require new advancements?
To pursue the objectives of this work, we define the following RQs. RQ1: Is/Are there any other SLR and taxonomies
developed for IR-IoT and IR-WoT? RQ2: Which IR subtasks
have been used, impacted by or proposed for the IoT/WoT
paradigms? RQ3: What are the basic foundations for IoT,
WoT and the applicability of IR subtasks on those paradigms?
RQ4: How the proposed solutions have been modelled and
algorithmically and technically structured to face IoT/WoT
challenges?
Definition of the SLR Scope (PICOC):To help answer the
RQs, we analysed the literature following the PICOC scope.
Population (P): “IoT” OR “Internet of Things” OR “WoT”
OR “Web of Things.”
Intervention (I): “IR” OR “Search Engine” OR “Crawling”
OR “Indexing” OR “Querying” OR “Retrieving” OR
“Ranking” OR “Discovery” OR “Presenting.”
Comparison (C): Not Applicable.
Outcomes (O): Paper on the state-of-the-art, taxonomy
framework and future directions for IR on IoT and WoT.
Context (C): Peer-reviewed and conference publications on
IR subtasks, models, algorithms and techniques.
Definition of the Inclusion (IC) and Exclusion Criteria
(EC) (IC1): Paper proposing at least one IR mechanism
(subtask, method, technique, model, algorithm, search engine);
AND IC2: The proposed solution is applied to IoT OR WoT
OR precursor; AND IC3: This article publication period must
be between 2000 and 2024. IC4: The study must be available
in full text in selected digital libraries. EC1: The study is
irrelevant to IoT/WoT or any of its precursor domains and the
field of IR. EC2: The study is a similar or reduced version of
a complete work. EC3: This article is a tertiary study or any
nonscientific report. EC4: The study is written in a language
other than English.
Our SLR approach uses ACM Digital Library, IEEE Xplore,
Google Scholar, ScienceDirect, and Springer Link. The SLR
process involves three phases.
1) In phase 1, the primary reviewer collects data from
primary studies, bibliometrics, demographics, taxonomics (if applicable), features, and research info. The
extracted data are tabulated for each study, and quality
and self-assessment questions generate data for each
paper.
2) In phase 2, our search strategy follows the methodology
described in [4] and consists of four stages: a) an
automatic search over the most relevant scientific digital
libraries; b) removal of duplicate papers; c) consideration of only papers related to the topic following
predetermined inclusion criteria; and d) further search
by forward snowballing.
3) In phase 3, we assess the quality of the results and
reports. We gather and structure the most outstanding
results to analyse and discuss. Using a checklist, the
researcher evaluates the aspects relevant to the SLR in
each paper. Each paper is either included or excluded in
the final phase for reporting, depending on the evaluation
score.
The output of the SLR is a survey on IR systems for IoT
and WoT. We review pioneer work and recent primary studies
reported between 2000 and 2024 to provide a comprehensive
analysis, see Figs. 2 and 3.
All in all, (4.3%) of works focus on pure data integration
or fusion, and (23.4%) of works are oriented to discovering
and crawling algorithms. We group them into one category
because of their similarities. However, we shall highlight that
both Search Scope/Space (3.3%) will advise using only one or
Fig. 2. Percentage of analysed studies by predominant IR subtask proposed
or presented for IoT—WoT.
both types of algorithms. A minority set of approaches (14.7%)
focuses on indexing mechanisms discussing data structures for
indices or strategies. Middlewares deals with device heterogeneity and with communications protocol requirements in the
form of translations or adaptions (what could be considered
WoT Binding Templates in W3C terminology). (13.6%) of
works have a predominant discussion on query processing
mechanisms, the majority of them biased toward SPARQLbased proposals. (14.7%) of analyzed studies have proposed
and presented ranking strategies or scoring methodologies
for improving query performance or information relevancy.
(13.6%) of research primarily aimed to provide semantic
enrichment to “simplify” other mechanisms, add a knowledge
base, link concepts, or enhance the abstraction models. Finally,
we count (4.9%) of recent studies researching the security,
privacy, and trust perspectives of search engines for IoT and
WoT. Only a tiny fraction (2.2%) proposes recommender
systems for IoT and WoT.
III. STATE-OF-THE-ART IN SEARCHING IOT-WOT
A. Evolution and Pioneers of IR for IoT and WoT
Fig. 4 showcases the conceptual evolution of IoTSE/WoTSE
and demonstrates the maturity achieved by the different
branches grouped according to the leading research lines,
including SPARQ/Non-IR approaches. Research on building search mechanisms for the predecessors of IoT/WoT
systems dates back to the early 2000s, which we refer to as
the precursors of IR-based IoTSE stage. The WoT concept
has been in development since 2006. However, complete
IoTSE/WoTSE systems were introduced at the end of the
decade, exploring different aspects of the problem and contributing to the development of new perspectives in the IR
field. Pioneering proposals, such as DYSER [5], SNOOGLE [6],
and MICROSEARCH [7] were introduced during this time.
These proposals helped pave the way for the advancement
of the WoT concept and have significantly contributed to
the development of the IR field. Fig. 4 shows the three
primary areas of research: 1) searching for entities like people,
places, and things using IR; 2) discovering and searching for
resources and services, such as data, events, and IoT devices
sensors/actuators without relying on IR; and 3) searching for
data, streams, and linked data using SPARQL.
Our analysis focuses on advanced and innovative components of complete IR systems.
Fig. 3. Percentage of analysed studies (a) by proposal type: IoTSE, WoTSE complete systems or specific components and (b) by scenario.
Fig. 4. Evolution of IR for IoT and WoT.
1) Wave One: We distinguish here those approaches that
adapt some IR-like methods and techniques to extended
or advanced versions of the predecessor systems of
IoT/WoT. We include here standalone adaptations.
2) Wave Two: IR Pioneers for semantic WoT enrichment.
3) Wave Three: Multimodal & context-aware search,
including distance-awareness.
Researchers on the front line are bringing new perspectives
and cutting-edge technology to IR. They are incorporating
artificial intelligence (AI) mechanisms into IoT and WoT
architectures. For instance, Cheng et al. [8] introduced neural
architecture search methodologies for IoT. These methodologies support a flexible search space and implement a
progressive coarse-to-grained search mechanism. Although
this study primary focus is not on IR, some new perspectives could be applied to new ranking or retrieving systems,
especially for ranking results considering IoT metrics. It is
important to note that, although the focus of this article is not
on SPARQL and Non-IR approaches, these approaches were
still considered when building the SLR dataset.
B. IR Subtasks and Approaches for IoT/WoT
The discussion of a dynamic IR system for IoT/WoT
has been divided into subtasks to present our findings and
insights based on the utilization, impact, and proposals of IR
subtasks for these paradigms. Key IoTSE/WoTSE-like works
published between 2002 and 2024 are listed in Table I. These
findings will undoubtedly provide valuable insights into the
development of IR systems for the IoT and WoT paradigms.
1) Crawling and Discovering for IoT/WoT: Crawling the
WoT is still a proceeding area of research [59]. Classically,
Crawler is a program that automatically scans websites by
following links from one webpage to another. A WoT Crawler
typically includes a Discovery mechanism and may be tailored
to a specific domain. WoT Crawling should be distinguished
from IoT Discovery. The architecture of the WoT Crawler
must remain protocol-independent, considering the nuances
of data exchange protocols used in IoT/WoT infrastructure.
Nath et al. [56] defended the idea that the WoT Crawler
might be application-specific to a domain and not generic. A
WoT Crawler has three primary functions [28]: 1) identifying
data sources; 2) finding and extracting metadata or semantic
elements; and 3) integrating, linking, and correlating them to
build an index system.
Discovery involves linking new data sources to existing
systems through crawling algorithms [17]. Discoverers can
be centralized or distributed, with a preference for decentralization; for example, recently, Chen et al. [12] proposed
vector symbolic architecture (VSA)-SD: a distributed service
discovery method for IoT devices based on VSA. VSA-SD
uses hyperdimensional vectors to describe services and calculates Hamming distance for service discovery. Centralized
TABLE I
COMPILATION OF KEY IOTSE/WOTSE-LIKE WORKS BETWEEN 2002 AND 2024
approaches build a registry of IoT resources and services,
while distributed approaches may be based on location or
infrastructure and use layered or clustered architecture. In
traditional Web crawlers, search engines identify the existence
of Web pages and continuously crawl for new and updated
resources. Automatic crawl mechanisms for WoT can be
likened to WoT crawling if the aim is to build a repository
collection. It is crucial to consider the impact of having
a central repository when assessing the scalability of any
solution. We must highlight the major crawling proposals
for WoT: IOTCRAWLER [17], [28], EASICRAWL [36] and
THINGSEEK [32]. Alternatively, a simple but less scalable
solution involves static registries where users manually enter
functionalities or IoT services [60]. Future research will
involve advancements in both crawler design and standardized
discovery mechanisms to bridge the gap between the WoT and
the Web of Data.
2) Indexing, Data Structures, and Strategies for IoT/WoT:
Indexing is a crucial subtask in IR systems, particularly for
the WoT. An IR system performs two primary functions:
1) indexing and 2) query processing. Indexing involves creating efficient data structures for retrieving information from
a collection of documents, mainly text. Query processing
uses these index data structures to generate a ranked list of
documents for a user’s query. Many studies have explored
the functions, benefits, and drawbacks of data structures in
the context of IoT and WoT, including multidimensional
approaches like R-tree, R*-tree, SR-Tree, X-tree, kD-tree, VAfile, and Pyramid. In [61], the advantages and disadvantages
of using data structures are presented.
IR solutions often rely on static indexes, which are not
well-suited for the dynamic nature of the WoT. To accommodate this dynamism, dynamic indexing for WoT must be
data-independent and scalable. Various dynamic indexing techniques have been proposed for both IoT and WoT, including
different data structures and strategies.
Dynamic indexing for WoT requires data independence
and affordable scalability. Tran et al. [2] classify the Index
Type as Text-based, Spatial Indexes, numerical Value Indexes,
Clustering mechanisms, Prediction Models, and Unspecified
Indexes. We can identify different directions in the dynamic
indexing techniques for IoT and WoT for both data structures
and strategies; some proposals include:
1) index relies on a centralized mechanism. Traditional or
specialized DB technologies, e.g., GeoDB, GraphDB;
2) index relies on a sort of Registry, Directory, or
Catalogue;
3) index is implemented as an Inverted file similar to
traditional Search Engines;
4) signature Indices based on hashing approaches; and
5) clustering Indices.
To achieve optimal efficiency and effectiveness, specialized indexing structures are necessary for different types of
data. While tree and hashing models are common, R-tree
is beneficial for geospatial data, R+/MDR+-tree for spatiotemporal data, and RtGR-tree for observation sensor data [62].
Other structures like PKR-tree and STK-tree have also been
studied. To meet user needs beyond conventional text or spatial
indexing, specialized index schemes have been proposed for
spatio-temporal, thematic, and near-real-time information.
These indexes can be distributed, multiindex, or hierarchical. However, constructing and maintaining these indexes can
be challenging, and few studies have focused on maintenance
strategies. Some proposed similarity scores and clustering
for thematic indexes, while others suggested strategies for
maximizing freshness while keeping computational costs minimal [63]. Recent research has explored various indexing
strategies for IoT streaming data. Doan et al. [64] introduced a
framework focusing on query optimization, comparing B-Plus
trees and hash tables while employing compression and
summarization techniques for efficiency. Similar optimization
approaches are presented in [65], utilizing dynamic time warping for data reduction. A categorization of indexing strategies
into full, centralized, and distributed hash tables (DHTs) is
proposed in [66]. Full indexing involves building a comprehensive data index table (DIT) across all IoT edge nodes,
potentially impacting freshness and scalability. Centralized
indexing addresses scalability but introduces a single point of
failure concerns. DHT-based approaches distribute the index
across nodes, improving fault tolerance but increasing query
complexity. Dynamic indexing for IoT data is explored in [67],
covering multidimensional and metric indexing techniques
within cloud-fog computing environments. The authors discuss partitioning strategies for index distribution across edge
nodes. In a different direction, Faheem et al. [13] proposed
a machine learning-based approach, combining indexing,
clustering, and semantic modeling to create a searchable
database for indoor things, enhancing efficiency and accuracy
in intelligent environments.
This overview highlights the diverse landscape of IoT
data indexing research, encompassing optimization techniques,
indexing structures, and deployment strategies.
3) Querying, Ranking, and Retrieving for IoT/WoT:
Standardization has been a guiding principle for the proposals
found in the literature. SPARQL and its extensions and derivatives play an important role in Semantic WoT by facilitating
an integrated IoT/WoT ecosystem. However, there has yet to
be an agreement on which ontologies should be utilised, and
a mechanism is still needed to allow end-users to interact
with WoT in a human-centric manner. While low-level queries
are possible, natural language or another approach should be
provided for high-level queries from the perspective of the
human end-user. We suggest a straightforward categorization
of query interpreters based on their query language and
capabilities.
1) Low-level those able to provide a coherent and straightforward search mechanism for RDF ontology-based
proposals at sensor and data layers. In this, we group
SPARQL, its derivatives and extensions, RDF2 data
query language (RDQL), or adaptations, and semantic
Web rule language (SWRL).3
2) High-level query interpreters and languages provide
richness in the specification of user expectations and
information needs. Some can receive the query in natural
language, while others provide an alternative synthetic
language. New approaches have been proposed during
the maturity of IoTSE/WoTSE research. Du et al. [68]
proposed an IoT-WS query as a tuple consisting of
distance, time and functionality. It provides a simple
mechanism, but in contrast, it can restrict the expressiveness and richness of the query itself.
Multiresolution queries, introduced in [25] and [69],
expanded the scope of IoT/WoT search beyond keyword-based
queries. Tang et al. proposed SMPKR for spatio-temporal
keyword-based search using PKR-tree indexing. Building upon
this, Tang et al. [70] introduced CECSE, a collaborative edgecloud cache-based WoTSE for mobile objects. While these
works advanced the field, challenges remain in integrating
diverse data sources and mechanisms for comprehensive
IoT/WoT search.
CECSE employed a three-tier cache architecture
and SKIN-tree indexing for efficient query processing.
Diamantini et al. [71] proposed a multiresolution, multigranularity, context-based approach. Complementarily, Ma
and Liu [27] focused on search progressiveness. A recent
contribution, ZION, described in [11], is an open-source W3C
Thing Description Directory that efficiently queries W3C
Thing Descriptions, offering scalable CRUDL operations and
JSONPath metadata search.
The richness of IoT/WoT data presents opportunities and
challenges for search. While prediction models can enhance
search accuracy, limitations in prediction accuracy and computational overhead persist. Zhang et al. [72] proposed a
dual-mode sensor search mechanism and improved prediction
models. Liu et al. [73] explored combinatorial-oriented feedback for data sensor search. These approaches aim to reduce
query processing overhead, optimize resource consumption,
and improve search efficiency by focusing on relevant sensor
data.
Overall, the field is evolving toward more sophisticated
search capabilities, combining diverse data sources, advanced
indexing techniques, and predictive models to address the
complexities of IoT/WoT environments.
4) Ranking and Retrieving in IoT—WoT: Sensor ranking
diverges significantly from traditional search engine relevance
ranking, prioritizing search engine performance over user
satisfaction. Perera et al. [40], [74] introduced semantic sensor
search, enabling users to query based on sensor parameters,
such as reliability, accuracy, location, and energy consumption.
Their proposed comparative-priority weighted index (CPWI)
ranks sensors by calculating a similarity score between user
preferences and sensor attributes, employing techniques like
fuzzy logic or weighted linear combination. Numerous subsequent studies have explored custom multicriteria scores
incorporating additional parameters, such as sensor precision,
latency, and cost-effectiveness.
Categorizing approaches by ordering and internal ranking methods reveals diverse techniques. DYSER [5] employs
predictive models, such as time series analysis or machine
learning, to forecast sensor performance and rank them
accordingly. SNOOGLE [6] utilizes a tf-idf weighting scheme
to assign relevance scores to IoT objects based on term
frequency and inverse document frequency, similar to traditional text retrieval. Microsearch [7] also leverages tf-idf
within a top-k retrieval framework to generate ranked lists of
sensors. LIVEWEB [75] adopts a Boolean model, matching
sensor attributes to query criteria using logical operators.
Mili-Rodin’s [15] WOTMAS2E introduces a probability-based
ranking process, considering sensor states and their associated
probabilities to determine rankings.
Despite these advancements, ranking remains a secondary
focus in the literature. Fathy et al. [76] defined data ranking
as prioritizing IoT resources based on Quality of Information
(QoI) and Value of Information (VoI), incorporating metrics,
such as accuracy, completeness, consistency, and relevance.
Recent work has expanded ranking methodologies.
Parreira et al. [77] proposed a multicriteria ranking
strategy using a weighted Quality of Experience (QoE)
score, considering factors like data freshness, accuracy,
completeness, and consistency. Truong et al. [78] introduced a
fuzzy-based similarity score, calculating the degree of match
between sensor attributes and query criteria. Additionally,
Krishankumar et al. [9] applied fuzzy logic to IoT Service
Provider (IoTSP) selection, considering factors like mobility,
security, and connectivity, and ranking providers based on
overall fuzzy membership values.
These approaches contribute to the evolving landscape
of IoT/WoT service and resource ranking in IoTSE/WoTSE
systems, with a growing emphasis on incorporating multiple
criteria, utilizing advanced ranking algorithms, and considering user preferences and system performance.
5) Presenting UI/UX for IoT/WoT: Different strategies have
been considered for presenting results in the world of WoTSE
research. These strategies have different formats and scopes
that can complement traditional IR systems facing end-users.
The presentation layer has been evaluated based on user type,
interface modality, query interface, and result interface [2].
One traditional approach of presenting is to use popular Web
browsers to navigate the IoT/WoT, but generic interfaces
restrict interoperability between ecosystems. Visual Search
for IoT and Map-based UI have also been proposed. Query
UI, Results UI, and Dual-integrated interfaces must be distinguished. Structured Web forms or map-based interfaces
are used for location-aware queries as input UI mechanisms.
RESTful API is commonly used in WoTSE systems for M2M
interactions. Other works suggest using specialised APIs,
like SOAP, while RDF API is highlighted for manipulating
semantic information in RDF graphs.
C. Semantic Enrichment for IoT/WoT
SPITFIRE [50] offers a complete semantic enrichment for
IoT/WoT scenarios through its search engine that utilises
a vocabulary integrating data with Linked Open Data, an
ontology describing entities and sensors, and a mechanism for
semi-automatic sensor description. Mietz et al. [79] semantic
model incorporates previous concepts for IoT search and
includes a base sensor model, its states, history, prediction
model, and placement. Various vocabulary models are available for enhanced search through relationships using RDF,
RDFa, OWL, OWL-DL, or OWL-S in IoTSE/WoTSE systems.
Several strategies have been proposed for discovering
semantically enabled smart things on the Web, including
DiscoWoT, a search mechanism with load-balancing and
query caching, the Web Avatar abstraction, and a user-system
view around the Things Description model. Other approaches
include a three-step search process with semantic profiles
and an OWL-DL model for the IoT Ecosystem. Sense2Web
provides an H2M interface for location-based search, while
WoTS2E is a search engine for the Semantic WoT.
All in all, semantic enrichment is used to address IoT
interoperability challenges. The eWoT approach extends the
W3C Thing Description model through semantic enrichment
using RDF triple stores. This approach avoids the need for
SPARQL support at IoT endpoints. Various ontologies have
been used, including FOAF, SSN Ontology, and O&M Sensor
Observation Ontology, to manage the vast amount of data
produced by sensors. Dolce Ultralite, GeoName, and Phenonet
Open loT Ontology have also been effective in this domain.
IV. TAXONOMIES OF SEARCH ENGINES FOR IOT—WOT
BY DIMENSIONS
Taxonomies categorise IR systems for IoT and WoT using
identification, characterisation, classification, and naming as
key factors. Multiple dimensions are usually considered to
propose the naming conventions.
From previous works, we highlight the taxonomy of
Tran et al. [2] containing (24) dimensions, including metapath. Tran et al. [2] added a fundamental analysis of
TABLE II
TAXONOMY FRAMEWORKS, DIMENSIONS, AND DIRECTIONS
approaches from a data/information flow viewpoint. One
cornerstone piece of their taxonomy is the meta-path: classification in the form of a naming convention of IoTSE/WoTSE
systems similar to a fingerprint with a strong focus on
capturing the expected data/information flow. Nevertheless,
it lacks an in-depth analysis from the IR perspective. The
extensive dimension granularity biases the features rather
than formulating a unified criterion and IR directions for
evolution. In contrast, Rather than spreading the granularity
of dimensions, our proposal aims to group them into IR stage
subtasks. Faheem et al. [80] consolidated four dimensions:
the use case (considered a dimension itself), thing schema,
indexing, and ranking. Here, the substantial consolidation does
not permit a precise characterization of the different works.
The other taxonomies are in the middle, with dimensions
covering the main IR subtask and experimental or prototype
features.
Our proposal groups dimension into IR stage subtasks for
precise characterization. The taxonomy aims to offer a holistic
view of all IR approaches and insights on future evolution.
In this section, we answer positively RQ1: Is/Are there any
other SLR and taxonomies developed for IR-IoT and IRWoT?, providing a list of existing taxonomies associated
with IoTSE/WoTSE research, see Table II. We also present a
perspective under the Type column, in which we group the
taxonomy framework closely related to its focus and caveats.
It contains the number of studied proposals reported (or the
number of references) and the assessed dimensions.
We have found inconsistencies between classification models, mostly due to the different lenses adopted for the creation
of these taxonomies while building the different perspectives
(listed as follows).
1) Function and principles-based [84], [88].
2) Search scope and things model-based [81], [84].
3) Flow-based and architecture [59], [85], [86].
4) Application-specific and use case-based [80].
There is neither a common language nor a common
understanding in classifying the IoTSE/WoTSE organisms and
their constitutive parts. Furthermore, there is no IR-oriented
perspective driving the classification. Even though previous
works have evaluated dozens of parameters and dimensions,
there is no holistic view that puts all the pieces together.
We compare all classifications in the primary studies dataset.
We also present a comparison between existing classification
models in Table II.
A. Proposed Unified and Holistic Multitaxonomy Framework
Our proposed framework (Table III) distinguishes between
IoTSE and WoTSE systems. The former is intended for
machine-to-machine interaction, while the latter is socially
aware and offers a Web abstraction to return geo-location and
perform predefined actions. Our taxonomy provides a precise
overview of IR possibilities aimed at providing accurate
information regardless of search techniques and models used.
IoTSE and WoTSE are two distinct proposals for taxonomy. Although IoTSE has been extensively studied, WoTSE
still requires sufficient identification and investigation. Recent
works have not been classified or included in previous taxonomies due to the publishing time. All previous taxonomies
universally include IoT data, stream, and content-based search.
However, context awareness is not explicitly considered in the
meta-path model in [2]. Another crucial aspect is the explicit
recognition of IoT Predictive Search as part of the taxonomy
framework. Although this could be understood as a technique
to reduce the search scope, we believe that the potential of
approaches in this category can shape the evolution of IR
research.
Location-based IoT search is a distinct category that
requires separate surveys and taxonomy due to its numerous
subbranches. It is important to consider temporal context separately from predictive search. WoTSE families can facilitate
thematic awareness and multiple search scopes. Thing-centred
or social-centred WoT Search is the next generation of search
engines that support end-users in finding multiple features and
functionalities concerning things based on social relationships
and providing sharing capabilities. Security, Privacy, and Trust
shall be integrated into all the IR subtasks. WoT Actions
Search involves virtual and physical actions triggered by
intangible virtual actions in the real world. WoT Progressive
Search is a promising research direction that can gradually
approach spatial-temporal dimensions. Ultimately, the ideal
WoT Everything Search is a species that can locate everything,
including synthetic emotions and sensations.
TABLE III
PROPOSED IOTSE/WOTSE TAXONOMY FRAMEWORK
B. Practical Applications and Real-World Scenarios
In this section, we describe several examples in the form of
case studies and real-world scenarios which provide practical
applications for the proposed taxonomy, helping validate the
taxonomy’s flexibility and effectiveness in real-world IoT/WoT
environments, while guiding the applicability, development
and research of new IR systems in IoT/WoT.
Some real-world scenarios are as follows.
1) Smart City Traffic Management:
a) Description: In a Smart City, real-time data from
traffic sensors, smart vehicles, IoT devices, and
User reports can be aggregated to manage traffic
flow automatically.
b) Taxonomy Usage: This application could employ
multiple taxonomy elements.
i) IoT Temporal Search for analyzing traffic patterns and changes over time.
ii) IoT Location Search to retrieve data based on
specific geographic areas (e.g., congestion in a
particular intersection).
iii) IoT Predictive Search to forecast potential congestion or traffic incidents based on historical
data and real-time updates.
c) Benefit: This approach could help city managers, end-users (citizens), or automated systems
proactively manage traffic, reduce congestion, and
enhance urban mobility.
2) Healthcare Monitoring and Assistance for Elderly
Patients:
a) Description: Healthcare providers can monitor
elderly patients through wearable sensors, environmental IoT devices, and medical records to provide
real-time assistance and support.
b) Taxonomy Usage: This application could employ
multiple taxonomy elements.
i) IoT Context-based Search to filter alerts relevant to each patient’s specific conditions and
current context (e.g., heart rate anomaly only
for patients with cardiac issues),
ii) IoT Data Stream Search for continuously monitoring real-time vital signs data,
iii) WoT Actions Search to trigger alerts or
automated interventions if certain thresholds
are breached (e.g., notifying caregivers) using
Healt WoT-like abstractions.
c) Benefit: This approach improves patient safety and
responsiveness by ensuring quick access to and
action on relevant patient data.
To illustrate the practical value and effectiveness of our
proposed taxonomy, we present two case studies, showcasing
its versatility and robustness. The first case study examines
energy management in smart grid systems, highlighting the
taxonomy’s role in predictive and resource-based searches to
optimize energy distribution and manage demand fluctuations
across IoT-enabled devices and WoT-integrated appliances.
The second case study focuses on personalized customer
support within IoT-enabled smart homes, demonstrating how
secure, proactive searches can enhance user satisfaction and
system efficiency. All in all, these case studies validate the
taxonomy’s adaptability and provide a foundation for developing advanced IR systems tailored to the dynamic needs of
IoT and WoT landscapes.
1) Case Study (Real-Time Energy Management in Smart
Grid Systems):
a) Objective: Test how the taxonomy aids in managing and optimizing energy distribution based on
demand patterns.
b) Scenario: A smart grid system with IoT-connected
meters and WoT-enabled appliances across residential and industrial areas is tasked with
optimizing energy use and responding to demand
fluctuations.
c) Taxonomy Demonstration:
i) IoT Predictive Search to forecast future energy
demand based on historical usage and current
conditions.
ii) IoT Resource Search to locate and allocate available energy resources across the
grid.
iii) WoT Multimodal Search to integrate data from
different sources (e.g., weather forecasts, usage
patterns).
d) Outcome: This study would measure how the
taxonomy enables efficient search and retrieval,
supporting demand-response strategies and
improving grid resilience.
2) Case Study (Personalized and Proactive Customer
Support in IoT-Driven Smart Homes):
a) Objective: Evaluate how the taxonomy supports
delivering timely, contextually relevant information
for proactive support in smart homes.
b) Scenario: In smart homes equipped with various
IoT devices, a support system provides assistance
based on device usage patterns and environmental
context.
c) Taxonomy Demonstration:
i) IoT Semantic Search to understand and
interpret the homeowner’s actions and potential needs (e.g., a power surge in a kitchen
appliance).
ii) WoT Actions Search to perform automated
actions or suggest solutions.
iii) WoT Secure Search to ensure safe handling and
retrieval of sensitive data for each user.
d) Outcome: This case study would test the
taxonomy’s ability to support intelligent, privacyrespecting, and proactive customer support,
providing insights into enhancing user satisfaction
and reducing costs.
V. IOTSE—WOTSE EVALUATION FRAMEWORKS
Measuring the effectiveness of an IR system depends mostly
on human evaluations of the usefulness of the information
found and its relevance. IR, as a highly empirical discipline,
requires careful and exhaustive evaluation to demonstrate the
performance of its models [89]. There are several measures of
interest that can be related to the quality of the responses in
terms of the efficiency and effectiveness of IR for IoT—WoT.
Traditionally: 1) precision and 2) completeness (Recall) are
quality metrics used in IR and other related fields [81], [89].
From a more technical point of view, 3) the speed of response
and 4) the size of the index are factors that can increase the
quality of a user’s experience with an IR system [33].
The importance of finding efficient and effective search
methods for WoT applications has been identified by [84] as a
commitment of all stages of IR. For example, Zhou et al. [84]
has proposed multiple qualitative variables as metrics to
evaluate search techniques in IoT—WoT applications: Query
Time, Query Precision. In terms of the response time of the
IR system (which includes sending a query and receiving the
results), as well as the precision of the results obtained. Thus,
in the application of IR in IoT—WoT, evaluation methods that
consider its multiple dimensions are also of vital importance.
A. Classical IR Evaluation by Test Collection
To measure the effectiveness of IR in an ad-hoc way,
traditionally, one has a collection of documents, a set of
information needs tests, expressible as queries, and a set of
relevance judgments, usually a binary evaluation of relevant or
not relevant for each query-document pair. The availability of
dynamic test collections focused on IoT—WoT paradigms [90]
has been widely identified as a challenge and current need.
None of the major IR evaluation forums, such as TREC,4
NTCIR,5 or FIRE6 contains some specific collection for IoT—
WoT paradigms.
In IR, it is possible to determine the effectiveness of a
system on a set of topics using a test collection in conjunction
with its respective specialized judgment of relevance [89].
From the results and the judgment, the following are determined: Precision (P) as the fraction of recovered documents
that are relevant, Recall (R) as the fraction of relevant
documents that are recovered and (F) as the harmonic mean
weighted between precision and recall [81], [89]
P = TP
TP + FP (1)
R = TP
TP + FN (2)
F(1) = 2 ∗ TP
2 ∗ TP + FP + FN (3)
where TP represents true positives, FP represents false positives, FN represents false negatives, and TN represents true
negatives. These can be adjusted to the type of recovery scheme, and there are variations, such as K-precision,
R-precision, and mean average precision (MAP).
B. Evaluation Frameworks, Datasets, and Test Collections
for IoT—WoT
The SLR has been extended to cover a fifth group of
questions related to the evaluation of IR systems in the IoT—
WoT field.
1) How have the solutions proposed in the analyzed SLR
studies evaluated the performance of IR-IoT and IRWoT systems?
a) What time performance measures have been used?
b) What index size measurements have been used?
c) What classical evaluation measures, such as
precision, completeness, and F-measure have been
used?
d) Are there datasets or open data for reproducibility
of experiments or reusability of data?
TABLE IV
EVALUATION FRAMEWORKS IN IR SYSTEMS FOR IOT-WOT
Table IV lists the main evaluation frameworks analyzed in
the context of proposals for IR systems or search engines in
IoT—WoT. Most datasets curated in the IoT sphere that have
been found have a focus toward application to a specific field,
such as testing security mechanisms. Such is the case of the
dataset BoT-IoT.7 This contains around 72 million records
with the respective categorization and/or automatic relevance
of attack type and other technical details. Another source
of information consulted is the Google data search system,
available at https://datasetsearch.research.google.com/. Where
you can find a few datasets created by recent research in the
WoT and IR field independently.
In the IoTSE evaluation presented by [91], IoTSEs underwent a query of IoT-enabled sensors that measure apparent
temperature in degrees Celsius. All instances achieved perfect
accuracy and completeness due to the use of a database to
store and resolve queries on the sensor metadata. The design of
efficiency evaluation methods in the implementation and use
of IoT search is a topic of vital importance [92]. Hatcher et al.
propose that the efficiency of the search system in IoT be
developed from two perspectives, increasing the effectiveness
in search of each component in processing time and the
scalability in the interactions between RI stages by increasing
the “Throughput” or capacity of processing given in queries
per second.
A significant majority of IoTSE—WoTSE proposals base
the evaluation of performance on real complexity in time and
space. The time measures are associated with the processing
of the index, queries, or the entire recovery stages until the
delivery of results to the end user. And the space measurements associated with the size of the index or the storage
used.
Recently, Cimmino and García-Castro [93] reported the
results of some experiments carried out for the semantic
discovery of WoT, framed in the WoT W3C initiative.
This uses the formal TD definitions and makes use of
ten SPARQL type queries to analyze the query time based
on the number of things (1–1000 TDs).8 Another open
dataset related to the W3C initiative is the one released by
Chapernay and Käbisch [94]. This work is based on the W3C
TD thing description model and proposes the construction
7Dataset BoT-IoT - https://research.unsw.edu.au/projects/toniot-datasets.
8Dataset and Open Experiment Data - https://doi.org/10.5281/zenodo.
6674151
of an ontology (W3C TD Ontology)9 for modeling the real
world from a collection of virtual things. The released dataset
comprises less than a hundred things modeled in JSON, with
sixty-five things in total.
C. Creating IR-IoT—IR-WoT Test Collection
Given the evaluation needs of IR systems for IoT—WoT
paradigms and the lack of open datasets as well as test collections focused on IoT—WoT paradigms, the following paths
are available in order to provide experiments reproducibility
mechanisms and data reusability in future work in the study,
analysis, and development of IR systems in the field. And
ultimately build an evaluation framework for RI-IoT and RIWoT systems.
1) Creating an IR-IoT—IR-WoT test collection.
a) Starting with the modification of Collections for
the evaluation of IR performance with a real-time
approach.
b) From IoT Dataset oriented to time series.
c) From WoT Dataset oriented to semantics.
2) Construction via active learning of an IR test collection [95].
3) IR evaluation as a search simulation, one of the proposals at the recent NTCIR 202210 and at [96].
D. Evaluation and Relevance Judgments
Creating a classical test IR collection requires great effort in
obtaining user evaluations and relevance judgments by experts.
Methodologically speaking, relevance assessments should be
compiled considering the following.
1) Information Needs expressed in the form of Queries.
Which determines a number of queries Q, on a certain
number of topics T.
2) A set of documents (N, K) retrieved by different IR
systems (A—B—C).
3) A relevance evaluation is given by Experts on the
topic(s) of the recovered documents (relevance judgments).
During the evolution of IR research, different measures have been proposed to characterize the agreement
between judges and their evaluation of the relevance of
the documents in the collection, using the so-called Kappa
statistics [89].
VI. OPEN RESEARCH DISCUSSIONS AND FUTURE WORK
Multiple challenges have been documented in the literature
during the last years; some persist, while others, through time,
have been diminished by novel solutions (Table V). Existing
state-of-the-art surveys have well-documented challenges and
future needs of IoTSE/WoTSE and their inherent retrieval
capabilities, focusing on a specific subject or the impact of the
challenges in some application fields or technical factors. This
section presents a review of the challenges from architectural
and technical perspectives.
A. Architectural Challenges
1) Dynamicity and Dynamics: The biggest architectural
challenge is the high pace of IoT/WoT data generation
and changes in things’ states and sensors’ data. Recently,
Faheem et al. [80] presented dynamic searching as the main
current challenge faced by IoTSE/WoTSE. Due to that, most
WoTSE approaches are based only on keyword-based search
or looking for static locations. In that way, it urges the
construction of dynamic indexing mechanisms and consideration of intent-based ranking techniques, which can positively
impact the dynamicity, adaptability, and scalability of WoTSE.
Meriem et al. [60] defended the idea that dynamicity is
core to finding the relevant service meeting the end-user
requirement in real-time. While Ma and Liu [27] expressesed
the dynamicity of search as guaranteed timely results in terms
of freshness. All in all, [2] in agreement with [80] points out
the open issues of dynamic searching resulting in a tradeoff
between indexing and freshness.
2) Adaptability of IR: It refers to the ability of a WoTSE
to adapt its behavior to different IoT/WoT scenarios, including
the modification of internal IR components to fulfill IoT/WoT
demands. Lately, Meriem et al. [60] and Aziez et al. [97]
addressed the IoT discovery problem by providing a classification of services based on technical features and relationships,
which is extensive, depicting a complete comparative study. It
highlights adaptability as an existing challenge because most
approaches do not address the widespread IoT requirements
that need to be met by classical IR techniques. Tran et al. [2]
agreed on the discussion reporting that every stage of the
IR process for an ideal WoTSE shall require some kind of
adaptation. One of the biggest steps would be to isolate the
heterogeneity of data and IoT technologies by middleware. IR
processing parallelism is identified as a useful strategy when
dealing with data analysis and IR, considering the amount of
generated data, if it is voluminous and independent [98].
3) Conceptual Heterogeneity: Four main obstacles shadow
the evolution of the field due to the heterogeneity of concepts.
Difficult-to-Reproduce due to the nonexistence of IoT/WoT
extended datasets [59], which in the majority of works are
proprietary or private. It is required to build open and public
datasets for IoTSE/WoTSE research. Some public and wellknown datasets are indeed being used; nevertheless, they are
more oriented toward sensing scenarios rather than providing
the whole picture. Moreover, full experiments can not be
replicated, whether due to a lack of datasets or problems with
the reproducibility of the experiments. The reproducibility
problem is related to three main factors.
1) Lack of Dataset: Use of proprietary dataset or use of
subsample of the publicly available dataset that has not
being published or for which the subsampling has not
been disclosed.
2) Lack of details about the evaluation pipeline (processing
of data) and protocol (tasks).
3) Lack of details about the system parameters.
Difficult-to-Evaluate/Compare is an implication of the
previous point, which shadows the evolution of IR systems,
given the divergence in the evaluation criteria of performance
metrics. A significant set of works takes as essential
time-based metrics for evaluating their approaches. However,
we should rely on adjusted or modified versions of IR metrics
for comparing the performance not only in terms of efficiency
(time and space complexity) but also in terms of effectiveness,
as offline and online IR metrics. As per our literature revision,
there are no documented efforts to standardize the evaluation
process by creating some evaluation protocols or adopting
some existing approaches.
Difficult-to-Access is another important point frequently
mentioned. We witness optimistically new collections of
datasets published in Public Clouds, such as Google Cloud
Platform11 with nearly 200 datasets. Some examples of live
and dynamic datasets are the Chicago Taxi Trips and the NYC
TLC Trips. Also, Amazon AWS provides open access to 175
datasets12 mainly oriented to medical and spatial purposes.
However, the availability of datasets is not the only blocking
point, as there are still many domains and data that are not
open to researchers.
Difficult-to-Reuse: Tran et al. [59] noticed different implementations for similar modular components: the difficulty of
reuse components comes from the use of not typical architectures and interfaces between components. Reusability can
be achieved through the construction of agreed architectures,
descriptors, and libraries. Standardization becomes a structural
pillar of the next generation IoTSE/WoTSE.
B. Technical Challenges
1) Scalability: It refers to adjusting the IoTSE/WoTSE
computing resources to handle the colossal amount of things
and produced data. Pattar et al. [81] and Zhang et al. [86]
identified the architectural design of IoTSE as the core component to be adapted with new solutions. Technically speaking,
scalability is seen as the ability of an IoT-related system to
adapt to changes in the real world environment and meet
future needs. An IoTSE/WoTSE must be capable of handling
the growing workload in terms of processing, storage, and
communications capacities.
2) Interoperability: refers to the ability of IoTSE/WoTSE
to interchange information with other systems, to be modular
with no dependencies between layers, facilitating innovation and evolution. Furthermore, to yield standards IoT/WoT
TABLE V
SHORT AND LONG-TERM RESEARCH TOPICS FOR IR-IOT AND IR-WOT
models [83], points to interoperability as an umbrella of issues
that slows down the evolution and prevents IoT emergence.
Interoperability is present at different levels: network, device,
syntactic, semantic, and platform. Some open challenges
permeate the creation of cross-domain and cross-platform
composited applications. It is mandatory to mature the protocol standardization for device-to-device communications, the
openness of API approaches, and the unification of testing and
evaluation frameworks. In the end, a lack of interoperability in
the IoT/WoT layer will undoubtedly impact the IoTSE/WoTSE
evolution as well. Interoperability remains an open issue
for IoT/WoT and Semantic WoT as well [24]. Even though
semantics promises to solve the interoperability issues of
multiple approaches, protocols, integration, and applications,
it involves defining the role of each entity and element in
the IoT/WoT. With no consensus about the ontologies and
knowledge representation, the interoperability advantage is
blurred and fuzzy. Silva et al. [24] presented a different
approach using a different language, SWOTPADL, rather than
OWL-S, extended from WSLM. SWOTPADL aims to provide
a service composition engine for SWoT apps and service
mashups.
3) Security, Privacy, and Trust: These are seen as critical
challenges as IoTSE/WoTSE data shall be protected, confidential, and private in all IR tasks. Security, Privacy, and
Trust have been relatively unexplored issues. Since 2020, we
recognize major efforts to cover security, privacy, and trust
on IoTSE/WoTSE. Yang et al. [21] proposed a Participant
Selection Strategy With Privacy Protection (PSSPP) for
IoTSE. It provides anonymity and mixed mechanisms for
end-users and requests at query time. The PSSPP system
evaluates participants’ trust value and credibility in the IoT
search at mobile crowdsensing scenarios. A minority of
works are increasing the research attention on adhering to
the security, privacy, and trust dimensions of IoTSE/WoTSE.
Barclay et al. [99] proposed discoverable trusted services
in highly dynamic workflows, like those used in 5G/WoTlike scenarios. It provides an enhanced semantic search
space for efficient and trusted 5G/WoT-like service discovery. Other recent works are specific to some IoT/WoT
industrial/health applications. Liu et al. [100] proposed a
multikeyword searchable encryption scheme for electronic
health files (EHFs) in the Medical IoT (MIoT). It provides
fine-grained access authorization and sharing mechanisms for
EHFs in MIoT. In the same context of MIoT, Bao et al. [101]
proposed a lightweight attribute-based searchable encryption
scheme with fine-grained access control and authorization,
allowing a keyword-based search. More recently, Hatcher
et al. [14] presented a study of security issues, challenges,
and vulnerabilities in IoTSE systems in conjunction with a
taxonomy of those. Recently, I-Recon [10], a new search
engine, addressed the limitations of existing public IoTSElike tools like Shodan and Censys by offering advanced
search capabilities, customizable scanning parameters, realtime incident response, and detailed error tracking. It enables
complex queries, aggregation searches, and efficient metadata
filtering, enhancing vulnerability analysis and threat detection
as a unique characteristic over the whole spectrum of IoTSE
systems.
C. Evolutionary Directions and Engineering
The modular architecture presented by [59] and the
proposed framework for component-based IoTSE in [90] constitute two consistent starting points for the design, engineering
and construction of evolutionary IoTSE/WoTSE systems.
Moreover, it is noticed that similar internal IR functional
blocks are being adapted to different types of IoT/WoT
content. We argue that design decisions are being affected by
the Thing description and the semantic mechanisms. From the
architectural point of view, a challenge is to build a generalised
WoTSE able to perform both local and global search. This
can be achieved with a distributed approach taken to the edge
and then interlinked through federation, integrating IoTSE
with edge network and computing techniques, co-designing
the evolution of Cloud and IoT. Through standardisation,
IoTSE/WoTSE shall be able to be extended to manage multiple
interactions with cyber-physical systems and not only be
application-specific to a unique scenario. There is room for
performance optimisation given the impact of IoT and WoT
on the heterogeneity, dynamicity, and scalability dimensions.
These remain significant challenges for the full development
and evolution of IoT/WoT systems [28]. Finally, but not least
important, security, privacy and trust should be fully integrated
and addressed by IoTSE/WoTSE.
VII. CONCLUSION
As the Internet and WoT become more pervasive, new
search mechanisms are needed to handle the real-time data collected by IoT devices. However, there is a lack of agreement on
how to model, name, and characterize these devices, hindering
interoperability. Semantic enrichment through ontologies can
help, but challenges remain due to multiple perspectives.
We analyzed the challenges of IoTSE and WoTSE and identified remaining issues in IR models for IoT and WoT. New
approaches are emerging to solve problems in discovering,
crawling, indexing, and ranking information. Our contribution
is a proposed taxonomy and survey of the state-of-the-art in IR
systems for IoT and WoT. Furthermore, we have zoomed in on
every IR stage with a separate discussion and subclassification.
It allows apprehending how the adaptation of IR techniques
and methodologies to specific application scenarios can be a
way to overcome the existing challenges and open issues.
A typical IoTSE+WoTSE architecture can contribute to the
development of new evolutionary directions for the following
generation of Search Engines. Our ultimate goal is to bring to
light the different perspectives and correlate them in a holistic,
360◦ panoramic of approaches that have been or are being
developed, homogenizing terms and shared understanding.
We firmly believe that dynamicity, adaptability, heterogeneity, and scalability directly impact IR and Search Engine
systems’ conception, as pointed out by the vast body of
research for IoT-IR/WoTSE-IR. The analysis of these studies
has pointed out a lack of standards and common directions
for IoTSE/WoTSE. Therefore, it is essential to fulfill the
requirements for a common taxonomy that will help to identify
the evolution of the IR field, with its main approaches and
relationships, and, in the future, to guide through comparative
analysis.