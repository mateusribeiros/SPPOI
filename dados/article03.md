Title:A Comprehensive Analysis of Ontologies Related to Safety
Related Traffic Information for Road Traffic

ABSTRACT
Ontologies within the Semantic Web represent a transformative
advancement, offering standardized data schemes that seamlessly
interconnect with diverse vocabularies and facilitate efficient information exchange globally. This paper explores the intersection of
ontologies and road safety, a domain critical to public well-being.
The analysis focuses on existing ontologies related to Safety Related
Traffic Information, delving into their implications for enhanced
road safety, optimized traffic management, and streamlined safetyrelated data exchange. The study discerns common patterns, best
practices, and areas for improvement across various ontological
models, thereby contributing to the development of standardized
solutions for managing road safety information. Using an ad hoc
metrics system for this type of information will assist us in determining which ontology is most suitable and/or the need for its
adaptation or utilization. Acknowledging the vital role of ontologies in promoting data interoperability, knowledge sharing, and
informed decision-making, this research underscores the potential
of integrating Semantic Web technologies and ontological models to
revolutionize safety-related information management. The findings
advocate for the transformative impact of ontologies in reducing
road accidents and safeguarding human lives, emphasizing their
significance in advancing the evolution of safer and more efficient
road networks.
CCS CONCEPTS
• Information systems → Graph-based database models; Semantic web description languages; Service discovery and interfaces; • Computing methodologies → Ontology engineering
KEYWORDS
Traffic Ontology, Safety Road, Knowledge Representation, Semantic
Web, Linked Data, Intelligent Transport.
ACM Reference Format:
Julián Gutiérrez Moret, J. Javier Samper-Zapater, Ana M. Delgado, J. Macario
Rocha, Gustavo Tena, and Francisco.R.Soriano. 2024. A Comprehensive
Analysis of Ontologies Related to Safety Related Traffic Information for
Road Traffic. In Proceedings of ACM EATIS conference (EATIS 2024). ACM,
New York, NY, USA, 8 pages. https://doi.org/10.1145/3685243.3685291
1 INTRODUCTION
The implementation of the ITS Directive 2010/40/EU [10] since
August 2010 has laid a foundational framework for the widespread
integration of Intelligent Transport Systems (ITS) across the European Union. This directive, originating from Action 6.1 of the
Action Plan, coordinates ITS deployment in the road sector by
addressing four Priority Areas aligned with key Action Areas.
Complementing this directive, Commission Delegated Regulations (EU) No 885/2013 [23], (EU) No 886/2013 [24], (EU) No
2015/962 [25], and (EU) 2017/1926 [26] establish specifications crucial for ensuring the compatibility, interoperability, and continuity
of various ITS services, including safe parking, road safety-related
traffic information, EU-wide real-time traffic information, and multimodal travel information services.
A pivotal component created under this regulatory framework
is the DATEX II [28] standard format, designed to facilitate the
exchange of traffic data among EU countries. DATEX II, employing
Recommended Reference Profiles (RRPs) [27] for Safety Related
Traffic Information (SRTI), plays a vital role in enhancing the publication of relevant information about incidents, adverse weather,
and geographical locations.
This study builds upon this regulatory foundation by conducting
a detailed analysis of existing vocabularies and ontologies related
to SRTI. By employing metrics and tools, the study aims to enhance
our understanding of semantic solutions and promote the effective
use of ontologies in the realm of ITS research and applications.
This article delves into the ontological analysis conducted within
the CEF LOD-RoadTran18 project [29], a venture co- financed by
the European Union. The project centers around examining the data
type "Priority C" or SRTI, with its primary aim being to facilitate the
reuse of dynamic road traffic data in two Member States, namely
the Czech Republic and Spain.
The methodology employed in this ontology analysis is structured, selecting ontologies based on their relevance to SRTI and
their adoption within the intelligent transportation domain. Results,
presented using metrics and tools, not only contribute insights but
also serve as a guide for similar research in diverse contexts, fostering a more comprehensive understanding of semantic solutions
and encouraging the utilization of ontologies in ITS research and
applications.
This document is organized as follows: Section 2 details the
scope of Safety Related Traffic Information. Section 3 discusses the
evaluation process and the metric used. Section 4 describes the
analysis and results using the metric described for each ontology
and finally, Section 5 concludes with key observations.
2 SCOPE OF SAFETY RELATED TRAFFIC
INFORMATION (SRTI)
Under Commission Delegated Regulation (EU) No 886/2013, the
minimum universal traffic information service related to road safety
encompasses specific categories of events or conditions crucial for
ensuring road safety.
To foster efficient data exchange and interoperability, both data
and service providers are mandated to furnish information in the
DATEX II (CEN/TS 16157) format or any other fully compatible
and interoperable machine-readable format accessible through an
access point.
The DATEX II UML model within the SRTI profile is intricately
crafted to accommodate the diverse categories outlined in Commission Delegated Regulation (EU) No 886/2013. This profile establishes a clearly defined hierarchy of classes, ensuring the seamless
exchange of harmonized data for road safety-related information.
By strictly adhering to the DATEX II UML model within the
SRTI profile, data and service providers not only ensure compliance
with regulations but also actively contribute to the enhancement of
road safety through the standardized exchange of traffic information. This adherence facilitates a unified approach to disseminating
critical road safety data, ultimately supporting safer road networks.
3 EVALUATION PROCESS
In the evaluation of various semantic models, we have considered
a set of indicators, detailed below.
3.1 Schema Metrics
3.1.1 Relationships richness of the Ontological model based on OntoQA. The “Relationships Richness” metric, employing OntoQA
[20] , serves as a valuable tool to assess the diversity and distribution of relationships within an ontological model. This metric
aids in evaluating the complexity of the ontology and assessing
the extent to which relationships go beyond basic class subclass
(SC) associations. The formula for calculating the “Relationships
Richness” (RR) is as follows:
RR =
P
P + SC
P represents the total number of non-subclass relationships defined in the schema. SC represents the total number of class subclass
relationships in the ontology.
The result of RR is expressed as a percentage. If the RR value is
close to zero, it indicates that most relationships in the ontology
are class subclass relationships, making it more of a taxonomy.
Conversely, an RR value close to one indicates that the ontology
contains diverse relationships beyond just class-subclass relationships, making it richer [20].
Based on the calculated RR value, we can categorize the “Relationships Richness” as follows:
• RR > 0.66 and RR <= 1: HIGH level.
• RR > 0.33 and RR <= 0.66: MEDIUM level.
• RR >= 0 and RR <= 0.33: LOW level.
3.1.2 Relationship Information Quality of the Ontological Model
based on OntoQA. The metric for “Relationship Information Quality” focuses on appraising the thoroughness of domain and range
definitions in the object properties (OP) within the ontology. This
information is crucial for modeling class relationships, precisely
outlining the classes linked through these properties. Object properties lacking defined domain or range, or with incomplete domain
and range information, may impede the ontology’s precision in
representing relationships between classes.
To gauge the quality of relationship information, we scrutinize
the percentage of object properties with a defined domain and
range in the ontology. The calculation is derived from the following
formula:
RIC =

N.of OP with defined domain and range
Total number of OP 
× 100
Relationship Information Quality Categorization:
• HIGH: >66% domain/range defined.
• MEDIUM: >33% and <=66% domain/range defined.
• LOW: >=0% and <=33% domain/range defined.
3.1.3 Attribute Richness of the Ontological Model based on OntoQA. The Attribute Richness metric, originating from OntoQA,
assesses ontology design quality and the volume of information related to instance data. This metric gauges the quantity of attributes
(slots) designated for each class, reflecting the depth of knowledge
conveyed by the ontology. Formally, Attribute Richness (AR) is
calculated as the average number of attributes (slots) per class. This
computation involves dividing the total number of attributes (att)
by the number of classes C present in the ontology [9].
AR =
att
C
Attribute Richness Categories:
• HIGH: AR > 3 – Comprehensive attributes, high conveyed
knowledge.
• MEDIUM: 1.5 <= AR <= 3 – Moderate attributes, moderate
conveyed knowledge.
• LOW: AR < 1.5 – Limited attributes, potentially lower conveyed knowledge.
3.1.4 Attribute Information Quality. Attribute Information Quality
categorizes attributes based on the completeness and accuracy of
domain and range information in ontology data properties:
• HIGH: >66% domain and/or range information, indicating
high completeness for accurate data modeling.
• MEDIUM: 33%-66% domain and/or range information, representing a moderate level of completeness.
• LOW: 0%-33% domain and/or range information, signifying a
low level of attribute information quality with insufficient
details.
3.1.5 Degree of coverage with DATEX II model. The extent to which
the DATEX II model is covered is a crucial metric in evaluating the
ontology within the SRTI scope. This assessment focuses on the
incorporation of key DATEX II concepts and classes, including Accident, AnimalsPresenceObstruction, EnvironmentalObstruction,
GeneralObstruction, MaintenanceWorks, NonWeatherRelatedRoadConditions, PoorEnvironmentConditions, VehicleObstruction, and
WeatherRelatedRoadCondition.
These concepts are fundamental components in safety-related
traffic information and road conditions, emphasizing the significance of their inclusion in a comprehensive ontology in the SRTI
domain.
3.1.6 Spread of use of the ontology. The spread of use metric provides valuable insights into the adoption and utilization of the
ontology across various sites and vocabularies within the SRTI
domain.
By assessing the number of sites and vocabularies that incorporate the ontology, we can gauge its relevance and impact within the
field of traffic and safety-related information. A higher spread of
use indicates widespread recognition and acceptance of the ontology as a valuable resource for representing and exchanging critical
transportation data.
4 ANALYSIS AND RESULTS
This section delves into the analysis of diverse vocabularies and
ontologies relevant to traffic, with a specific focus on the Safety
Related Traffic Information (SRTI) Scope. To gauge their effectiveness, OntoQA-based metrics are employed, drawing insights from
the research of Megan Katsumi and Mark Stephen Fox [15] who
carry out an analysis of ontologies in the field of transportation.
These metrics serve as a crucial tool, fostering the consolidation of
semantic solutions that intelligently leverage existing ontologies.
By applying OntoQA-based metrics, a comprehensive and standardized evaluation of these ontologies occurs, allowing researchers
and practitioners to understand their strengths and limitations
thoroughly. This evaluative approach, particularly in transport, objectively measures the performance and relevance of each ontology,
advancing semantic solutions in the transportation domain. Recognizing the importance of reusing and consolidating ontologies
enhances knowledge sharing, integration, and overall interoperability, contributing to more efficient semantic systems in the traffic
field.
4.1 Ontology for Transportation Networks
The Ontology for Transportation Networks (OTN), a crucial element of the REWERSE [5] project, a distinguished “Network of
Excellence” in “Reasoning on the Web,” is funded by the EU Commission and Switzerland under the “6th Framework Programme.”
Focused on “Semantic-based knowledge systems,” the project
aims to advance understanding in the Information Society Technologies (IST) sector. OTN, also known as Ontology-based Traffic
Network, comprehensively addresses traffic network and transportation aspects, utilizing the ISO standard Geographic Data File
format (GDF). OTN signifies REWERSE’s commitment to semanticbased knowledge systems, laying a structured foundation for transportation system analysis despite limited online availability.
See the analysis summary in Table 1.
Table 1: Ontology Analysis Summary Table for OTN
Metric Value A.Value
Relationships richness 0,1074 LOW
Relationship information quality Approx 100 % HIGH
Attribute richness 0,4166 LOW
Attribute information quality 100 % HIGH
Coverage DATEXII No Datex classes LOW
Spread of use Not used LOW
4.2 Ontology Based Road Traffic Management
OSMonto is a meticulously crafted ontology [4] for representing
OpenStreetMap tags, developed by a collaborative effort led by
Mihai Codescu, Gregor Horsinka, Oliver Kutz, Till Mossakowski,
and Rafaela Rau. Decomposing tags into a hierarchical structure
based on keys, OSMonto enhances tag semantics and fosters interoperability by connecting with other ontologies. Accessible in
.owl format, it facilitates exploration and visualization of tag relationships through tools like Protégé. As an open-source project on
GitHub, OSMonto encourages community contributions, making
it a valuable resource for managing and comprehending OpenStreetMap tags. Its hierarchical organization, open accessibility,
and compatibility with widely used tools highlight its significance
in advancing tag semantics and data exploration.
See Table 2.
Table 2: OSMONTO Analysis Summary Table
Metric Value A.Value
Relationships richness 0,0473 LOW
Relationship information quality 100 % HIGH
Attribute richness 0,0579 LOW
Attribute information quality 100 % HIGH
Coverage DATEX II No Datex classes LOW
Spread of use Not used LOW
4.3 Road Accident Ontology
The Road Accident Ontology, initially drafted by Daniel Dardailler
for sharing during W3C Geek Week in July 2012, aims to provide a
structured representation of road accidents, encompassing information about involved parties, accident locations, causes, and effects
[6].
Despite its conceptual design, this ontology has not been practically utilized or implemented in real-world applications or datasets.
As a result, no existing resources have been found that make use of
this vocabulary.
See Table 3.
Table 3: Road Accident Ontology Analysis summary table
Metric Value A.Value
Relationships richness 0,4473 MEDIUM
Relationship information quality Approx 100 % HIGH
Attribute richness 1,875 MEDIUM
Attribute information quality Approx 100 % HIGH
Coverage DATEX II No Datex classes LOW
Spread of use Not used LOW
4.4 km4city, the DISIT Knowledge Model for
City and Mobility
The Km4City platform stands as a powerful Smart City tool designed to implement the city’s vision, monitor its evolution, and
provide new services aimed at enhancing the quality of life for city
users and fostering economic growth. By promoting user satisfaction and pride, Km4City aims to create attractive cities that thrive
and produce [16]. This platform serves as an interconnected and
versatile knowledge model enabling the description of smart cities,
drawing data from diverse sources such as portals of the Tuscan region (MIIC, Muoversi in Toscana, Osservatorio dei Trasporti), Open
Data, Linked Data, and contributions from individual municipalities,
notably Florence.
See Table 4.
Table 4: km4city Analysis summary table
Metric Value A.Value
Relationships richness 0,15 LOW
Relationship information quality Approx 100 % HIGH
Attribute richness 0,3928 LOW
Attribute information quality Approx 50 % MEDIUM
Coverage DATEX II No Datex classes LOW
Spread of use Not used LOW
4.5 Transport Disruption ontology
The Transport Disruption ontology [7] provides a robust framework for modeling travel and transport-related events that disrupt planned travel. Divided into two main sections, it comprehensively addresses disruptive event characteristics and their impact
on travel plans, offering a hierarchical structure for travel and
transport-related events. Developers and researchers benefit from
standardized representations, enabling insightful decision-making.
Applied in the Social Journeys project, it leverages social media to
disseminate real-time disruption information, enhancing passenger
experience. Its integration with Vocab.datex showcases versatility,
supporting seamless data integration. As a valuable contribution to
transport modeling, its structured representation fosters reliability,
efficiency, and resilience in evolving transportation systems.
See Table 5.
Table 5: Transport Disruption ontology Analysis summary
table
Metric Value A.Value
Relationships richness 0,1561 LOW
Relationship information quality Approx 100 % HIGH
Attribute richness 0,1210 LOW
Attribute information quality Approx 100 % HIGH
Coverage DATEX II No Datex classes LOW
Spread of use Not used LOW
4.6 Vocab.linkeddata.es
Vocab.linkeddata.es, developed by the Ontology Engineering Group
at the Polytechnic University of Madrid, is a valuable resource presenting a curated list of vocabularies for linked open data [11].
Focused on Spain’s cities, it promotes semantic interoperability and
standardization. Notably, it includes vocabularies for traffic and
transport, providing a structured framework for consistent open
data publication. Efficiently reusing elements from ontologies like
Naptan, it emphasizes data integration and representation quality.
This initiative empowers Spanish cities to embrace linked open
data principles, facilitating collaboration and data-driven decisionmaking. The Ontology Engineering Group’s dedication contributes
to advancing urban data management, fostering a connected ecosystem for innovative applications in transportation and urban planning [3].
See Table 6.
Table 6: Vocab.linkeddata.es Analysis summary table
Metric Value A.Value
Relationships richness 0,3461 MEDIUM
Relationship information quality Approx 50 % MEDIUM
Attribute richness 0,3552 LOW
Attribute information quality < 50 % LOW
Coverage DATEX II No Datex classes LOW
Spread of use Zaragoza Zaragoza
Spread of use Alcobendas Alcobendas
Spread of use CRTM Madrid CRTM Madrid
4.7 Vocabulary for representing traffic data
The “Vocabulary for Representing Traffic Data” is a potent tool
designed to efficiently capture and depict urban traffic situation
data. An extension of the Semantic Sensor Network Ontology [14],
it aligns with ongoing standardization, ensuring compatibility with
visualization tools and diverse processing systems. For optimal integration, it’s recommended to use this vocabulary alongside the city
street map ontology, enhancing the representation of road sections
key elements in urban traffic data [1]. Focused on traffic intensity, it
establishes a standardized framework for consistent citywide traffic
conditions, enabling valuable insights for stakeholders. Its flexibility
accommodates future expansion, ensuring long-term relevance and
adaptability to evolving traffic monitoring needs. This vocabulary
promotes harmonized, interoperable data representation, fostering
collaboration, accurate analysis, and innovative solutions in urban
traffic management. Crucial for smart city initiatives, it aligns seamlessly with the Semantic Sensor Network Ontology, unlocking the
full potential of urban traffic data. This forward-thinking ontology embodies a foundational resource for the pursuit of efficient,
sustainable, and data-informed urban transportation systems.
See Table 7.
Table 7: Vocabulary for representing traffic data Analysis
summary table.
Metric Value A.Value
Relationships richness 0,3758 MEDIUM
Relationship information quality < 33 % LOW
Attribute richness 0 LOW
Attribute information quality < 33 % LOW
Coverage DATEX II No Datex classes LOW
Spread of use Zaragoza Zaragoza
Spread of use Alcobendas Alcobendas
4.8 Vocabulary for the representation of data on
traffic made by motor vehicles
The “Vocabulary for the Representation of Data on Traffic Made by
Motor Vehicles” is a specialized ontology for detailing motor vehicle traffic within urban areas. Exclusively focusing on motorized
vehicles, it defines the scope, covering Traffic Equipment, encompassing measuring devices, types, specific measurements, and their
city locations. The vocabulary also includes Incidents, addressing
various traffic-related disruptions on public roads, providing a detailed representation of their impact. Sections consider locations of
equipment deployment and incident occurrences, facilitating precise, location-based data crucial for traffic management. Developed
as part of the “Open, Collaborative, and Interoperable Government
Platform” project, involving city councils like Madrid and Zaragoza,
the collaborative effort emphasizes intercity cooperation in smart
city initiatives [1]. Implementing this vocabulary empowers city authorities to efficiently collect, represent, and analyze motor vehicle
traffic data, enhancing capabilities in traffic management and incident response, and promoting open and interoperable data practices
within smart cities.
See Table 8.
4.9 Linked GTFS
The Linked General Transit Feed Specification (Linked GTFS) stands
as a pivotal transformation of the GTFS in CSV reference to RDF
(Resource Description Framework) [12]. This meticulous mapping
preserves the core structure and semantics of the original CSV reference while introducing minor enhancements for improved usability.
By representing GTFS data in RDF format, it unleashes the potential
Table 8: Vocabulary for the representation of data on traffic
made by motor vehicles Analysis summary table
Metric Value A.Value
Relationships richness 0,3758 MEDIUM
Relationship information quality > 66 % HIGH
Attribute richness 0,8 LOW
Attribute information quality Approx 100 % HIGH
Coverage DATEX II No Datex classes LOW
Spread of use Caceres Caceres
Spread of use Aragon Aragon
of Linked Data principles, fostering data integration, interlinking,
and semantic enrichment. While prioritizing compatibility with
existing GTFS datasets and tools, Linked GTFS [19] introduces enhancements for efficient exploration and analysis of transit data.
This community-driven initiative signifies a leap in data interoperability, revolutionizing transit planning, route optimization, and
passenger experiences.
See Table 9.
Table 9: Linked GTFS Analysis summary table
Metric Value A.Value
Relationships richness 0,7916 HIGH
Relationship information quality Approx. 100 % HIGH
Attribute richness 0,8 LOW
Attribute information quality Approx 100 % HIGH
Coverage DATEX II No Datex classes LOW
Spread of use Caceres Caceres
Spread of use Aragon Aragon
4.10 vocab.datex
The vocab.datex website,offers a valuable vocabulary for mapping
DATEX II to an OWL Ontology, instrumental in a Belgian research
program extending DATEX II’s standard scope. Developed collaboratively by entities such as the Biotope project, Open Transport Net
project, ITS Belgium, iMinds, and Open Transport at Open Knowledge, it originated from the open Summer of Code in 2016 [18].
Though currently offline, the ontology continues to be employed
in Spanish Open Data Portals, underlining its practical significance.
Despite its unavailability, vocab.datex has left a lasting impact,
exemplifying collaborative efforts enhancing data exchange and
interoperability in transportation.
Available at https://lov.linkeddata.es/dataset/lov/vocabs/datex
See Table 10.
4.11 MobiVoc
MobiVoc, a vital standardized vocabulary tailored for mobility data,
encompasses Electric Charging Points, Parking Facilities, and Highway Roadworks sites based on DATEX II standards [2]. In our
rapidly advancing world, the fusion of innovative mobility concepts and enhanced data networking plays a pivotal role in global
Table 10: Vocab.datex Analysis summary table
Metric Value A.Value
Relationships richness 0,8266 HIGH
Relationship information quality Approx. 0 % LOW
Attribute richness 1,6373 MEDIUM
Attribute information quality Approx. 0 % LOW
Coverage DATEX II HIGH (all classes) HIGH
Spread of use Caceres Caceres
economic development. The latest August 2023 update introduced
highway roadworks concepts, ensuring compliance with DATEX II
standards. This enriched dataset proves instrumental in the LIMBO
research project, optimizing routing for electric cars. By integrating
with DATEX II, MobiVoc enhances its utility, remaining adaptable
to future mobility advancements. Positioned as a valuable resource,
MobiVoc’s data-driven insights hold immense potential in shaping
a sustainable and efficient transportation ecosystem.
See Table 11.
Table 11: MobiVoc Analysis Summary Table
Metric Value A.Value
Relationships richness 0,6875 HIGH
Relationship information quality Approx. 100 % HIGH
Attribute richness 1,3389 LOW
Attribute information quality Approx. 100 % HIGH
Coverage DATEX II HIGH in Mobility HIGH
Spread of use Not used LOW
4.12 DATEX II Ontology, University of València
The DATEX II standard model encompasses a comprehensive set
of attributes and relationships related to traffic information, aiming to cover various real-world traffic scenarios. In response to
the complexity and diversity of traffic situations, the University
of Valencia undertook the development of an ontology focused
on accommodating any possible traffic event that could occur in
practical scenarios.
Within the DATEX II model, a hierarchy of situation types is
defined, including situations arising from the actions of operators
on the road, events unrelated to the road, and elements of situations
due to traffic. The latter category further subdivides into specific
types such as accidents and abnormal traffic. The University of
Valencia’s Ontology has considered these detailed subdivisions to
ensure it can effectively represent a wide range of traffic-related
situations.
While the University of Valencia has been actively involved in
various works and publications related to traffic and DATEX II, the
developed Ontology has not yet been officially published, and it
is not currently in use. However, the Ontology was presented at
the EATIS 2009 conference [21], indicating the team’s dedication
to advancing research in this domain.
See Table 12.
Table 12: DATEX II Ontology, Universitat de València Analysis summary table
Metric Value A.Value
Relationships richness 0,1567 LOW
Relationship information quality Approx. 100 % HIGH
Attribute richness 0,1576 LOW
Attribute information quality Approx. 100 % HIGH
Coverage DATEX II HIGH (all classes) HIGH
Spread of use Not used LOW
4.13 LOD SRTI DATEX II
In 2018, the European project LOD-RoadTran18 was initiated with
the collaborative efforts of institutions from the Czech Republic and
the General Directorate of Traffic (DGT) in Spain, aimed at facilitating the reuse of road traffic data with an SRTI (Safety Related Traffic
Information) scope in two Member States. The project’s primary
objective was to enable the constant publication of a comprehensive set of traffic data from both Spain and the Czech Republic
on the European Open Data Portal (https://data.europa.eu/ ). By
achieving this, the data became locatable, accessible, interoperable,
and reusable, fostering its connection with various other datasets
through Linked Open Data (LOD) principles.
A major impact of the LOD-RoadTran18 project was its significant improvement in providing basic access services to open
traffic data, complying with the requirements of the ITS Directive
(2010/40/EU) [10]. Not only did it enhance the visualization and
download of data, but it also enabled the extraction of valuable
meaning from the data, leading to the development of new types of
services made possible by LOD integration. The project was in line
with the call for Public Open Data of the European Commission
and was evaluated under the CEF Telecom 2018 Call – Public Open
Data (CEF-TC-2018-5).
During the EATIS 2022 conference, the project’s scope, including descriptions of its ontologies and solution architectures, was
presented [13]. These presentations shed light on the overall vision
of the project and its technical underpinnings.
One of the key accomplishments of the LOD-RoadTran18 project
was the development of a traffic ontology, the LOD SRTI DATEX
II, with a specific focus on SRTI [22]. This ontology not only encompassed the SRTI classes defined in the DATEX II model but also
established links with other relevant vocabularies and ontologies,
including that of the National Geographic Institute [9]. By incorporating such connections, the ontology achieved higher levels of
semantic interoperability and enriched the potential applications
of the data.
An important highlight is that the DGT [8] has already started
publishing its linked SRTI semantic data based on the ontology
developed within the LOD-RoadTran18 project [17]. This implementation demonstrates the practical relevance and success of the
project’s efforts in enabling effective data reuse and interoperability
within the traffic domain.
The degree of coverage with the DATEX II model is assessed as
high, meaning that the ontology aligns well with the entire DATEX
model related to road safety. This alignment enhances semantic
interoperability and facilitates the integration of traffic data with
other relevant datasets.
In terms of practical application, the ontology is currently being
utilized by significant transportation authorities. Specifically, it is
in use by the DGT [8] in Spain and the national traffic center of
the Czech Republic. This implementation in real-world scenarios
highlights the ontology’s relevance and successful adoption.
Overall, the analysis showcases both strengths and areas for
improvement in the ontological model. Its balanced relationship
richness, high information quality of P relationships, and high
degree of coverage with DATEX II demonstrate its effectiveness in
representing road traffic information. However, efforts can be made
to increase attribute richness to further enhance data representation
capabilities. The successful deployment of the ontology in traffic
authorities underscores its practical value and confirms its role in
supporting data exchange and interoperability in the context of
road traffic safety.
The analysis for this model can be seen in Table 13 and a summary of all vocabularies in Table 14.
Table 13: LOD SRTI DATEX II Analysis summary table
Metric Value A.Value
Relationships richness 0,4990 MEDIUM
Relationship information quality Approx. 86 % HIGH
Attribute richness Approx 0,328 LOW
Attribute information quality Approx 68,1 % HIGH
Coverage DATEX II HIGH (all classes) HIGH
Spread of use Spain HIGH
Spread of use Czech Republic HIGH
Table 14: Analysis summary table
5 DISCUSSION AND CONCLUSIONS
This study meticulously explores various road traffic ontologies,
focusing on their alignment with the DATEX II European traffic
information exchange model. Among the examined ontologies, four
demonstrate commendable coverage with the DATEX II model.
MobiVoc stands out for its robust alignment with DATEX II
Mobility, providing extensive coverage within the Mobility Scope.
Similarly, Vocab.datex shows significant alignment with the DATEX
II SRTI profile, as indicated in Table 14. However, its ontology design
reveals some incompleteness, particularly in modeling relationships
and attributes. The unavailability of the hosting website adds a layer
of concern regarding accessibility and usability.
The initial DATEX II ontology developed by the University of
Valencia achieves high coverage in the DATEX II SRTI profile, excelling in relationships and attribute quality. However, it falls short
in the richness of relationships and attributes, obtaining a low level
in these quality metrics. Its non-current usage poses a challenge to
practical applicability.
The LOD SRTI DATEX II ontology exhibits varying richness in
attributes, suggesting acceptable schema quality. While its adoption of the original UML class model justifies its richness in the
relationship’s metric, it presents limitations in attribute richness.
Notably, this ontology has found practical application in publishing
semantic data, successfully adopted by the Directorate General of
Traffic (DGT) in Spain and the Czech Republic. Its current usage
recommends it for publishing road traffic information with an SRTI
profile.
Key findings reveal alignments and deficiencies in several road
traffic ontologies concerning the DATEX II model. MobiVoc and
Vocab.datex show promise, albeit requiring refinement, especially
for Vocab.datex.
In summary, the recommendation to adopt the LOD SRTI DATEX II Ontology for publishing road traffic information is based on
its current usage and successful application, highlighting practical
applicability. Analyzing ontologies using metrics, as demonstrated,
is crucial for assessing quality, identifying strengths, and pinpointing areas of improvement. These metrics offer a systematic means
to ensure alignment with standards and richness in relationships
and attributes, fostering widespread adoption, as seen in successful
cases like LOD-RoadTran18.
Future research should prioritize refining and updating existing
ontologies, addressing identified deficiencies, and ensuring continuous accessibility. Adopting alternative approaches to ontology
development, coupled with exploration into emerging technologies,
can contribute to more comprehensive and effective road traffic
ontologies.
In conclusion, the dynamic nature of the semantic web landscape
necessitates ongoing efforts to align ontologies with evolving standards and technologies in road traffic management. By emphasizing
the practical importance of ontologies through thorough analysis
and fostering continuous refinement, this study lays the groundwork for advancements in data interoperability, knowledge sharing,
and decision-making processes within the domain of road traffic
safety.