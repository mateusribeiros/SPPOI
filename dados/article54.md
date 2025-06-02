Title: Methods for Standardizing Metadata at Pusdatinrenbang Bappenas

ABSTRACT Metadata interoperability remains a significant challenge for Indonesian government institutions, particularly at Pusdatinrenbang Bappenas, due to the lack of a unified metadata standard. Existing
standards, such as KUGI, cannot be implemented effectively across institutions because of differences in data
structure and spatial context. This study proposes a structured metadata standardization method based on the
MAFRA framework to address this issue. The method includes three main stages: Lifting and Normalization
to unify metadata formats, Metadata Mapping to identify relationships between metadata elements, and
Metadata Integration to create a consistent and interoperable metadata structure. The method was tested
on two datasets (public housing and fisheries production) from Bappenas, PUPR, and BPS. The results
show that the proposed method effectively improves data interoperability and consistency across institutions.
Validation through questionnaires confirmed that the method meets user expectations and can be applied
to other metadata domains with similar structural issues. The key contributions of this study include the
adaptation of the MAFRA framework for government metadata, the development of a structured metadata
standardization process, and the establishment of a scalable model for future metadata integration between
institutions with overlapping functions.
INDEX TERMS Metadata standards, metadata integration, data interoperability, lifting and normalization,
metadata mapping.
I. INTRODUCTION
Metadata is a crucial component within an organization [1],
[2], [3]. Metadata ensures that users interpret the data uniformly [2], [4]. Due to the diversity of metadata across
institutions, a metadata standard is required. Such a standard is essential for improving data interoperability, accurate
data interpretation, and consistency [5], [6]. The Ministry
of National Development Planning (PPN)/Bappenas interacts
with a wide range of metadata from various government
institutions in performing its duties [7].
The Ministry of National Development Planning
(PPN)/Bappenas is responsible for carrying out government
tasks in the field of national development planning [8].
To manage the data involved in development planning, a data
custodian system was established. A data custodian is a
unit tasked with collecting, verifying, managing, and disseminating data [7], which in this case is Pusdatinrenbang
Bappenas. To ensure the data custodian’s tasks align well with
development planning, Pusdatinrenbang developed a system
called the Datarenbang Portal.
The Datarenbang Portal is a system built by Pusdatinrenbang Bappenas to support the preparation of development
plans. Interviews revealed that the Datarenbang Portal is
currently unable to optimally support the preparation of
development plans. This poses risks for work units, such as
accessing outdated, unsynchronized, or invalid data during
planning, potentially leading to improperly formulated development plans.
Marchewka, in his research, stated that the causes of
project failure can be categorized into four factors: people,
process, technology, and organization [9]. The researcher
conducted interviews to explore these four factors in greater
depth regarding the failure of the Portal Datarenbang project
and further investigated to identify the dominant factor contributing to the failure, as shown in FIGURE 1.
Among the various contributing factors, the most dominant
issue identified by the respondents is that the existing metadata has not yet met the standards. This raises the question
of what method would be suitable for standardizing metadata
and enabling data exchange in Pusdatinrenbang Bappenas.
Metadata standards play a crucial role in ensuring the
smooth operation of a system [10], [11], [12]. Currently,
many methods are available for standardization [11]. However, these existing methods need to be adapted to meet the
specific needs of Pusdatinrenbang Bappenas.
II. RELATED RESEARCH
To develop a metadata standardization method, the researcher
conducted a Systematic Literature Review. A total of
5,454 pieces of literature related to government metadata
integration were collected. These were then filtered further,
resulting in 26 primary pieces of literature that served as the
basis for developing this metadata standardization method.
Among the 26, seven pieces of literature consist of government regulations that were added based on suggestions
from Pusdatinrenbang Bappenas. The following sections outline key topics derived from this literature relevant to this
research.
A. METADATA
Metadata is data about data. Proper data governance
must include robust metadata. Metadata informs users
whether the data meets their needs. Without metadata,
users might retrieve inaccurate data [4]. Additionally, metadata facilitates the searching, use, and management of data
information [13], [14].
Metadata standards are crucial when integrating data [12].
A metadata standard is a set of requirements aimed at establishing a shared understanding of the meaning or semantics
of data to ensure its correct use and interpretation by both
owners and users [6]. Standardized metadata is essential to
ensure that data, regardless of its source, remains consistent,
accessible, and meaningful. Metadata standards enhance data
interoperability, allowing data to be utilized effectively [5].
However, metadata standards suitable for one organization
may not necessarily fit another [10].
Metadata in Indonesian institutions must adhere to the
metadata standards established by central data stewards
responsible for their respective tasks and functions [15]. For
instance, data governance for national development planning
is overseen by Bappenas [16], housing-related data by the
Ministry of Public Works and Housing (PUPR) [17], and
statistical data by Statistics Indonesia [18].
Regarding how metadata is stored and exchanged, there
are three commonly used methods: Relational Databases
and Application Programming Interfaces (API), XML,
and Linked Data with Resource Description Framework
(RDF) [19]. The RDF format has several advantages over
other formats, including:
• It can describe relationships between data entities, which
is essential when structuring metadata [20],
• It simplifies semantic writing, which ensures that the
meaning of data remains unchanged, even when its format changes [21],
• It improves efficiency in decision-making
processes [22].
The Geospatial Information Agency (Badan Informasi
Geospasial, BIG) is the institution responsible for determining spatial metadata standards in Indonesia. BIG has
published the Indonesian Geographical Elements Catalog
(KUGI), which includes guidelines for coding, structure,
types, operations, attributes, associations, and documentation
for geographical data. The goal is to facilitate the exchange
and utilization of spatial data in Indonesia [13].
B. METADATA INTEROPERABILITY
According to Haslhofer, metadata interoperability is a qualitative property of metadata objects that enables systems
and applications using those objects to function beyond the
boundaries of a single system [11]. Nilsson defines metadata
interoperability as the ability of two or more systems or components to exchange descriptive data about something and
to interpret the exchanged descriptive data consistently, consistent with the data creator’s interpretation [23]. Achieving
metadata interoperability involves linking several processes,
including:
• Metadata Lifting and Normalization: Lifting is the process of converting different metadata schemas into a
unified schema. Normalization refers to the process of
standardizing or harmonizing metadata that has undergone lifting [11], [24].
• Metadata mapping: This is the process of reconciling
differences at the schema and instance levels among
metadata objects [11]. Metadata mapping involves several stages:
– Mapping Discovery: Identifying relationships
between metadata elements.
– Mapping Representation: Representing the mapping relationships in an understandable format.
– Mapping Execution: Applying the defined mappings to integrate metadata. This includes
re-querying the mapped metadata to capture the
required information.
– Mapping Maintenance: Updating the mappings as
metadata evolves.
• Metadata Integration: This is the process of organizing metadata within the same data domain by unifying
metadata with identical meanings but different element
names into a uniform framework. Metadata integration
also minimizes discrepancies between metadata while
preserving the conveyed data information [14].
FIGURE 1. Root causes of issues in the datarenbang portal.
Currently, automating these processes remains challenging [25]. Organizational involvement is crucial in each of
these processes [11], [26], [27].
Rahm and Bernstein, as well as Kalfoglou and Schorlemmer, have conducted surveys on the features available in
the market related to these processes [11] as described in
TABLE 1. Not all existing mapping solutions include all of
the features listed above. Each mapping solution is designed
with specific objectives, and the features provided align with
those objectives [11]. The list above serves as a benchmark
for features in the proposed method.
TABLE 1. Features in metadata interoperability processes.
C. MAFRA
Ontology is a system of concepts and relationships used to
describe and represent a specific domain of interest [22]. The
ontology mapping process is a series of activities required
to transform instances from one ontology to another [25].
By observing the similarities in transformation processes
across ontologies, the MAFRA framework was developed.
MAFRA, short for A Mapping Framework for Distributed
Ontologies, is a framework designed for mapping distributed
ontologies [24].
The MAFRA framework consists of two main dimensions: horizontal and vertical [24]. The horizontal dimension
includes several modules. The Lifting and Normalization
module aligns and normalizes data into a uniform format.
The Similarity module identifies similarities between entities in the source and target ontologies. Based on these
similarities, the Semantic Bridging module establishes relationships between the entities. The Execution module then
transforms instances from the source ontology to the target
ontology using the defined semantic bridging. Finally, the
Postprocessing module improves the quality of the transformation by evaluating the execution results. The vertical
dimension includes the Evolution module, which ensures
that the semantic bridging remains aligned with changes in
the ontologies. The Consensus Building module facilitates
agreement between users representing the source and target ontologies. The Domain Knowledge module builds an
understanding of the ontologies being transformed, while
the GUI module provides graphical support to simplify the
transformation process.
MAFRA was selected based on the results of a literature
study (TP2-M2) and a focus group discussion (TP2-M1) with
Bappenas. The components in MAFRA represent the results
of surveys conducted by Rahm and Bernstein as well as
Kalfoglou and Schorlemmer [11], [25], along with three additional components that are unique to MAFRA and required
by Bappenas, namely: Similarity, Evolution, and Domain
Constraints and Background Knowledge.
The MAFRA framework can be used as a reference for
developing a metadata standardization method to address the
research question. However, not all aspects of the framework
can be adopted, as it enforces metadata interoperability based
on predefined constants [24].
D. FRAMEWORK FOR METHOD DEVELOPMENT
After conducting a literature review and holding discussions
with Pusdatinrenbang Bappenas, the researcher concluded
that the proposed method would be constructed using elements derived from the MAFRA framework. These elements
were restructured by incorporating components from previous research literature as well as government regulations.
III. METHODOLOGY
As previously described, this research began with interviews
to explore issues at Pusdatinrenbang Bappenas (TP1). The
interviews examined expectations, realities, problems, and
the impact of the issues related to Datarenbang at Bappenas. The interviews also investigated the factors contributing
to these issues using a method based on the four factors
of project failure [9] (TP1-M2). These factors were then
visualized using an Ishikawa diagram to clarify the causal
relationships between the identified factors (TP1-M1). Based
on the interviews and analysis, research questions were formulated to align with the identified issues (TP1-O1).
From the research questions (TP1-O1), a focused group
discussion (TP2-M1) was conducted with Pusdatinrenbang
Bappenas to obtain feedback on the research questions. As a
result, the researchers were provided with several regulations
to include in the literature review, including:
• BIG Circular Letter No. 6 of 2021 [13]
• Statistics Indonesia Regulation No. 4 of 2020 [18]
• Regulation of the Minister of National Development
Planning/Head of Bappenas No. 18 of 2020 [7]
• Presidential Regulation No. 25 of 2004 [16]
• Law of the Republic of Indonesia No. 1 of 2011 [17]
• Presidential Regulation No. 39 of 2019 [15]
• Presidential Regulation No. 81 of 2021 [8]
These regulations, together with other literature, were then
studied (TP2-M2), resulting in a framework for developing
the method (TP2-O1).
Based on the framework (TP2-O1), a suitable research
method was developed (TP3-O1). The researcher adopted
a research action method, wherein the developed method
(TP3-O2) would be tested on user metadata. The results
would then be validated by the users to determine their
suitability.
To design the method for testing (TP3-O2), the researcher
conducted a focus group discussion with Pusdatinrenbang
Bappenas (TP3-M2). During the discussion, the framework
(TP2-O1) was presented, and feedback was sought to refine
the method for practical application.
The next stage involved developing research instruments
(INS), which included:
• A semi-structured discussion guide for metadata selection (INS3)
• A semi-structured discussion guide for metadata evaluation (INS4)
• A questionnaire for validating the method (INS5)
After the research instruments (INS) were prepared, the
next step was to determine the metadata samples for testing (TP5). At this stage, another focus group discussion
(TP5-M1) was conducted using the prepared discussion
instrument (INS3). The outcome was the selection of two
metadata samples ready for testing (TP5-O1).
The two samples (TP5-O1) were then processed using
the standardized method that had been developed (TP3-O2).
A focus group discussion (TP6-M2) was held with the guidance of research instrument INS4. The result was metadata
and a data exchange format that complies with the standard
(TP6-O1).
The results were subsequently validated (TP7) by distributing the INS5 questionnaire (TP7-M1). The outcome
determined whether the metadata and data exchange format
met or failed to meet the expectations of Pusdatinrenbang
Bappenas (TP7-O1).
The validation results (TP7-O1) demonstrated whether the
developed method (TP3-O2) could be implemented. If found
to be implementable, the research question was answered
(TP8-M1). This will be further elaborated in the conclusion
section of the research (TP8-O1).
IV. METADATA STANDARDIZATION METHOD
The development of this method utilized a literature review
(TP3-M1) and a focus group discussion (TP3-M2), leveraging the theoretical framework (TP2-O1) and the research
instrument (INS2). During the focus group discussion, users
were briefed on how the method would be developed and the
role of INS2 in its construction.
It was explained to the users that the proposed method
was derived from the MAFRA framework, with its elements
broken down and reprocessed by incorporating government
regulations and the findings from the literature review.
During the method development phase, users were also
provided with the research instrument INS2, which included a
checklist of existing mapping features available in the market.
Additionally, the definitions of each feature, as discussed in
Section II Part B, were explained to the users.
The following is a summary of the focus group discussion
on method development (TP3-M2). The MAFRA framework
is a robust foundation for metadata standardization; however,
in the case of Pusdatinrenbang Bappenas, the framework
requires modifications for the following reasons:
• The target metadata standard (KUGI) may not fully
align with the semantic meaning of the metadata being
standardized.
• The MAFRA framework requires the addition of new
classes such as Semantic Bridge, Service, Rule, and
other classes [24], whereas in this research, it is not
FIGURE 2. MAFRA.
FIGURE 3. Framework for method development.
FIGURE 4. Method for standardizing metadata in pusdatinrenbang
bappenas.
feasible to introduce new metadata classes beyond those
already recognized by the institution.
Based on these reasons, the elements of the MAFRA
framework that can be adopted are:
FIGURE 5. Changes to Bappenas rumah susun metadata during the
Lifting and Normalization phase.
TABLE 2. Rumah susun metadata standard.
• Lifting and Normalization: Metadata must be in the
same format to allow mapping [11]. In this method, RDF
is selected as the format.
FIGURE 6. Changes to Bappenas produksi perikanan metadata during the
lifting and normalization phase.
TABLE 3. Produksi perikanan metadata standard.
TABLE 4. Average score for each questionnaire question.
• Domain Knowledge and Constraints: KUGI serves as
the spatial metadata standard and acts as a constraint in
this research. However, its placement must align with
domain knowledge from Bappenas to position the metadata appropriately.
• Evolution: Metadata and data are continuously evolving,
so the metadata standard and data interoperability must
also be adaptable.
Unlike MAFRA, the Lifting and Normalization process
in this method allows an entity within the data or metadata
to shift its position to another data or metadata entity. This
adjustment is necessary because the placement of data and
metadata at Bappenas is sometimes inconsistent.
TABLE 5. Research Instrument: Semi-Structured discussion guide for
literature review (INS1).
In this method, metadata elements are kept unchanged,
so connecting one metadata to another requires identifying
relationships using the existing elements. To facilitate this,
metadata mapping needs to be created.
Metadata mapping in this method is limited to the mapping
discovery phase. The mapping representation phase is not
necessary as it has already been addressed in the Lifting
and Normalization phase. Similarly, the mapping execution
phase is unnecessary as it is replaced by the metadata integration phase, which will be explained later. The mapping
maintenance phase is also not needed, as it is replaced by
the Evolution phase derived from MAFRA. Thus, metadata
mapping in this method refers to the identification of relationships between metadata elements and their surrounding
elements until a bridging element is found that connects the
metadata.
Metadata integration in this method combines the concepts
of metadata integration and metadata execution. Therefore,
the steps involved in metadata integration in this method are:
• Applying metadata mapping to perform metadata
integration,
• Unifying metadata elements across institutions that
share the same meaning, and
• Requerying the mapped metadata to extract the required
metadata elements.
The results of the requery process will form new metadata
that can integrate data across systems. This new metadata can
then be reviewed by the relevant institutions to be adopted as
a standard. The final method diagram is shown in FIGURE 4.
V. METHOD IMPLEMENTATION
In this research, two groups of development planning metadata were selected: ‘‘rumah susun’’ (housing complexes) and
‘‘produksi perikanan’’ (fisheries production). The selection of
these metadata groups was conducted through a focus group
discussion (TP5-M1) and aligned with the criteria outlined in
the research instrument INS3.
A. RUMAH SUSUN GROUP
The rumah susun metadata group consists of metadata
sourced from Bappenas, metadata from the Ministry of Public
Works and Housing (PUPR), and metadata from BIG as
the metadata standard. Data from Bappenas pertains to the
FIGURE 7. Bappenas rumah susun metadata mapping.
FIGURE 8. PUPR rumah susun metadata mapping.
planning of rumah susun, data from the Ministry of PUPR
relates to the construction of rumah susun, while BIG standardizes the columns and metadata for rumah susun data.
During the pre-iteration phase, the metadata structure is
shown in TABLE 14 to 19 IN APPENDIX B. The metadata
then proceeds to the first phase, Lifting and Normalization,
with the results displayed in FIGURE 5. In this phase, several
attribute shifts are observed:
• For the rumah susun attributes from Bappenas,
‘‘mp’’, ‘‘durasi’’, ‘‘data_tot’’, ‘‘igt’’, ‘‘target_tot’’, and
‘‘instansi’’, which were initially part of the data, are now
moved to the descriptive metadata. This is because the
FIGURE 9. KUGI metadata mapping.
content of these attributes is identical across all records
in the rumah susun table.
• The ‘‘shape’’ attribute in the rumah susun data from
Bappenas, previously of type geometry (GeometryZM,
4326), changes to geometry (Geometry, 4326). This
adjustment is due to the rumah susun data consisting of
points without elevation or measurement values.
The data from the Ministry of Public Works and Housing
(PUPR) did not undergo any changes as it already has the
correct structure. Similarly, the metadata from KUGI remains
unchanged as it serves as the standard that must be adhered
to.
The metadata that have undergone Lifting and Normalization are then subjected to metadata mapping. In this phase,
additional metadata surrounding the existing metadata is
considered. The results are shown in FIGURE 7 to 9 in
APPENDIX B.
Through metadata mapping, several metadata elements
were identified for integration. The class ‘‘Rumah Susun’’
in PUPR is the same as the class ‘‘Realisasi Rumah Susun’’
in Bappenas. This class can incorporate data properties from
both KUGI and Bappenas. The data properties from KUGI in
this class are ‘‘name’’ and ‘‘total’’, while the data properties
from Bappenas are ‘‘name’’ and ‘‘target_tot.’’ These data
properties have identical values but are named differently.
Thus, the integration of Bappenas’ data with PUPR
are not integrated between Bappenas’ ‘‘Rencana rumah
susun’’ data and PUPR’s ‘‘Rumah Susun Tahun 2023’’
data, but rather between Bappenas’ ‘‘Rencana rumah
susun’’ data and PUPR’s ‘‘Rumah Susun’’ data. In PUPR’s
‘‘Rumah Susun’’ data, metadata such as ‘‘Rencana Rumah
Susun’’ from Bappenas, including planning names (‘‘name’’)
or other attributes, can be added to facilitate future
integration.
Here, the KUGI standard related to rumah susun belongs
to a different class compared to PUPR and Bappenas, making
the KUGI standard inapplicable to these data. Additionally,
in the KUGI standard, the spatial data specified is polygons
for rumah susun, whereas in Bappenas, the available spatial
data consists of province points.
The integration results can be seen in FIGURE 10 in
APPENDIX B. Thus, the metadata standard diagram for
rumah susun in Pusdatin is as shown in FIGURE 11 in
APPENDIX B, which corresponds in detail to TABLE 2.
The metadata standard was validated through discussions
with Bappenas. Bappenas then verified it with the relevant
institutions (PUPR and BIG). The results showed that the
metadata standard and data interoperability were satisfactory.
TABLE 8. Research Instrument: Semi-Structured discussion guide for
metadata selection (INS3) - metadata criteria section.
TABLE 9. Research Instrument: semi-structured discussion guide for
metadata evaluation (INS4) - discussion guide section.
TABLE 10. Research Instrument: Semi-Structured discussion guide for
metadata evaluation (INS4) - pre-iteration section.
Therefore, the iteration process was completed, and no further
iterations were necessary.
B. PRODUKSI PERIKANAN GROUP
The next group is the produksi perikanan metadata, consisting of metadata sourced from Bappenas and BPS. Bappenas
metadata pertains to fisheries production targets, while BPS
metadata relates to the realization of fisheries production.
During the pre-iteration phase, the metadata structure is
shown in TABLE 20 and 21 in APPENDIX C. The metadata
TABLE 13. Research methodology.
then underwent the Lifting and Normalization process, resulting in the form shown in FIGURE 6. Changes occurred in the
data and metadata from Bappenas, while the metadata from
BPS remained unchanged.
In the data from Bappenas, the attributes ‘‘turtahun’’ and
‘‘turvar’’ were removed from the structure because they
were unused and contained no information. Additionally,
the attribute ‘‘kode_iso’’ was moved from the data to the
TABLE 15. ‘‘Rumah Susun’’ Metadata by PUPR.
TABLE 16. ‘Rumah Susun Tahun 2023’’ Metadata by PUPR.
TABLE 17. ‘‘Lingkungan Terbangun‘‘ Metadata by KUGI.
TABLE 18. ‘‘Perumahan Area’’ Metadata by KUGI.
descriptive metadata. This adjustment was made because the
value of this attribute is identical across all records.
The metadata resulting from the Lifting and Normalization
process was then subjected to metadata mapping. During this
process, it was found that the class ‘‘Produksi Perikanan’’
from Bappenas could be directly integrated with the class
‘‘Produksi Perikanan Berdasarkan yang dijual di TPI Setiap
Tahun Setiap Provinsi’’ from BPS. These two classes are
FIGURE 12. Bappenas produksi perikanan metadata mapping.
FIGURE 13. BPS ‘‘produksi perikanan laut berdasarkan yang dijual di tpi
setiap tahunan setiap provinsi’’ metadata mapping.
essentially the same, differing only in their names. The results
are shown in FIGURE 12 and 13 in APPENDIX C.
Since these two classes are identical, the integration of
Bappenas data with BPS data related to produksi perikanan
can be implemented. The results are displayed in FIGURE 14
in APPENDIX C. Consequently, the metadata standard diagram for produksi perikanan in Pusdatin is as shown in
FIGURE 15 in APPENDIX C, which corresponds in detail
to table in TABLE 3.
The metadata standard and data interoperability were validated through discussions with Bappenas. Bappenas then
verified it with the relevant institutions (BPS). The results
confirmed that the metadata standard and data interoperability met the requirements. Thus, the iteration process was
completed, and no further iterations were necessary.
C. CONCLUSION OF ITERATION AND METHOD
VALIDATION
For the rumah susun data, it can be concluded that the issues
arose from the collection of irrelevant data, as the data referenced for integration was not suitable. Additionally, the
KUGI metadata standard could not be applied here due to
differences in spatial context. For the produksi perikanan
data, the problems were caused by outdated data due to the
use of an inappropriate data-sharing protocol.
Interpretations based on TABLE 4 are as follows:
• INS5-1 shows a negative average, indicating that
the majority of respondents lean towards answering
‘‘Yes.’’
• INS5-2 shows a negative average, indicating that
the majority of respondents lean towards answering
‘‘Yes.’’
• INS5-3 shows a negative average, indicating that
the majority of respondents lean towards answering ‘‘Yes,’’ although not as strongly as INS5-1 and
INS5-2.
• INS5-4 shows a negative average, indicating that
the majority of respondents lean towards answering ‘‘Yes,’’ although not as strongly as INS5-1 and
INS5-2.
Based on this, it can be concluded that:
• On average, respondents agree that the metadata standard is appropriate and its relationships with other
metadata are correct.
• On average, respondents agree that the data-sharing
standard is correct and aligns with the metadata.
• On average, respondents agree that the metadata
standard and data-sharing format can be implemented, although not as strongly as the first two
questions.
• On average, respondents agree that the method developed is suitable for standardizing metadata and data
exchange formats at Pusdatinrenbang Bappenas.
Based on the results above, it can be concluded that
the applied method has successfully standardized the
metadata.
In implementing this method, the iteration time to completion for each data group is approximately 5 hours, which
is relatively fast for standardizing metadata between government institutions. With standardized metadata, future data
interoperability will be more efficient, especially for largescale datasets.
VI. DISCUSSION
In Indonesian government institutions, large-scale data relies
heavily on metadata to help users understand data content.
Standardizing metadata facilitates easier data interoperability
for large datasets by ensuring consistency and uniformity in
metadata standards.
A. IMPACT ON GOVERNMENT DATA INTEROPERABILITY
The proposed method successfully standardizes metadata and
ensures data interoperability for rumah susun and produksi
perikanan datasets. By unifying metadata structures across
different institutions, this method allows more consistent data
interpretation and more reliable data exchange. The interoperability improvement is particularly significant for institutions
like Pusdatinrenbang Bappenas, which rely on data from
multiple sources for national development planning. The ability to integrate data from diverse sources will enhance the
accuracy of policy formulation, improve resource allocation,
and enable more informed decision-making processes. This
is especially relevant for complex national projects involving
multiple stakeholders and institutions.
B. CHALLENGES IN ADOPTING THE PROPOSED
FRAMEWORK
While the proposed method shows promising results, several
challenges remain in its adoption. First, technical differences in metadata structures between institutions present a
significant barrier to full interoperability. Some institutions
use legacy systems or non-standardized data formats, which
complicates the lifting and normalization process. Second,
institutional resistance to adopting new metadata standards
may arise due to a lack of technical capacity or conflicting
internal policies. Third, the metadata mapping phase may
face difficulties when metadata definitions are inconsistent
or incomplete. Overcoming these challenges will require
coordinated effort and support from both central and local
government agencies.
C. SCALABILITY TO OTHER METADATA DOMAINS
The method tested in this research focused on metadata for
public housing and fisheries production, but it demonstrates
the potential for application to other metadata domains. The
modular nature of the MAFRA-based framework makes it
adaptable to different metadata structures. For instance, this
method can be extended to healthcare data by modifying the
schema definitions and mapping rules to align with health
sector standards. Similarly, it can be applied to education data
where metadata definitions are often fragmented across institutions. However, scalability will depend on the complexity
of metadata relationships and the willingness of institutions
to adopt a unified standard. Future research should explore
methods to automate metadata mapping and integration to
improve scalability further.
D. LIMITATIONS AND FUTURE DIRECTIONS
Another limitation is the understanding of metadata within
government institutions. Currently, metadata standardization
has primarily been adopted by central government agencies, while local governments have yet to fully embrace it.
Bridging the gap in metadata standardization between central and local governments remains a challenge and will
require significant effort and coordination. Future research
should focus on developing a more flexible framework that
accommodates overlapping functions and complex metadata
relationships across institutions.
