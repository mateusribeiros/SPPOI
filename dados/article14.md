Title: MARINE TRANSPORT BUSINESS A DATAMESH-BASED DATA
ASSET STRATEGY

ABSTRACT
Modern organisations increasingly view data as a valuable asset,
the management of which is essential due to its diminishing value
over time. However, implementing data management technologies
within various marine transportation systems, including vessels and
ports, presents significant challenges. These difficulties primarily
stem from issues such as unreliable data transmissions, incompatible programs, and the requirement to handle large volumes of data,
particularly geographic information, for advanced processing. As a
result, there is a pressing need to revise traditional data management methods to address these challenges effectively. The modern
solution of the Data Mesh has been attracting substantial interest
from various organisations. This innovative approach adopts an
in-house data management model that enhances the standard centralised team-based process and reduces the reliance on centralised
personnel. Under the Data Mesh paradigm, individual data management tasks are delegated to personnel within their specific business
domains, yielding several benefits such as improved data quality,
enhanced data utilisation, and better alignment with organisational
strategic goals. This study applies the Data Mesh model to construct
a comprehensive framework for marine transport organisations
and bulk carrier shipping companies. This framework encompasses
decentralised data management, data product development, and
the lifecycle of data assets and creates strategies for data assets.
CCS CONCEPTS
• Information systems; • Data management systems;
KEYWORDS
Data Management, Data Analytics, Data Products, Data Assets,
Marine Transport Business
1 INTRODUCTION
Today, organisations value data as a vital asset, needing ongoing maintenance for accessibility to internal users and external
customers. DAMA (Data Management Association) defines data
management as a cost-effective, secure, and efficient process encompassing data collection, storage, and utilisation. DAMA-DMBOK
(Data Management Body of Knowledge) Versions 1 and 2 highlight data management’s lifecycles, starting with understanding
the organisation’s data context and data management actions and
measures [1].
Data manipulation began in the 1950s, focusing on batchprocessing data files using tape and card recording. In the following
decade, applications operated independently and data files were
separated for enhanced functionality. However, exchanging data
between applications remained a significant challenge [2].
In the 1970s, Michael Stonebraker and Eugene Wong from UC
Berkeley researched relational databases to address the data exchange issue. Their work led to the development of INGRES (Interactive Graphics and Retrieval System), using the QUEL (Relational
Database Query Language) query language. IBM introduced SQL
(Structured Query Language) four years later, and it is now the
most widely used database management language [3].
Data management practices are crucial in establishing proper
data-use procedures and standards. These include documenting
data-use agreements, conducting compliance training, implementing data privacy measures, performing data cleaning and maintenance, and creating metadata. These efforts help organisations
better understand their data context [4]. Data management plays
a vital role in establishing credibility and transparency for organisations. It ensures ethical and legal monitoring of data-related
activities, helping users comprehend how their data is collected and
used. Data reliability requires reporting, validating data sources,
and maintaining accuracy and updates.
Organisations need assistance leveraging data for improved efficiency and embracing data-driven practices when facing data
management challenges. Business leaders must identify critical
data for their operations. Organisations must establish data standards, ensure consistency, and manage costs associated with data
activities to address data management difficulties. High-quality
data benefits decision-making while controlling risks associated
with low-quality data [1]. Organisations often need help with data
management issues from employee actions and technology challenges. Integrating various data sources for reporting and analysis
can be challenging, requiring a reliable data reproduction system
for accessing historical data [6].
Data management has evolved from the 1950s to the present.
Modern data management empowers organisations to address challenges by integrating cutting-edge technologies like Artificial Intelligence and IoT sensors. It enables them to make more informed
decisions based on available data and adapt to future data and
business challenges [7, 8].
In modern data management, organisations set goals to assess
data investment benefits, starting with a suitable platform or tool
and advanced technology to reduce costs [9]. Quality modern data
management offers numerous benefits, reducing human errors in
data operations, responding efficiently to customer needs, and enhancing data sharing and security against cyber threats [10]. However, modern data management faces challenges with the growth
of IoT, making data increasingly complex and time-consuming to
access and analyse [11]. Continuous improvement is crucial, especially for long-established organisations, to avoid inconsistencies
and ensure high-quality data. The lack of constant improvement
has made modern data management more challenging, leading
to inefficiencies in utilising data and infrequent updates in longrunning organisations, resulting in decreased data quality in recent
reports or dashboards [12].
Data Mesh, a decentralised modern data management concept,
involves restructuring data ownership, roles and responsibilities,
and adjusting architecture, technology, and security [13]. It effectively manages the increasing volume of data and platforms while
ensuring control over data transfer and user access [25].
PayPal utilizes Data Mesh to manage risks in its financial services,
handling credit, billing, seller data, and AI systems and organising
its data resources and platforms through mergers, acquisitions, and
external providers [14].
Netflix implements Data Mesh for a flexible data movement and
processing platform, improving real-time processing, addressing
pipeline issues like Change Data Capture (CDC), and enhancing
performance reporting and processing [15].
The marine transport business sector plays a crucial role in supporting the expansion of international trade. It offers advantages
like reduced transportation costs and the ability to carry large quantities of goods in a single trip, leading to significant economies of
scale and unit cost savings. Compared to rail transport, it can be
3.5 times more cost-effective; and when compared to car transport,
it can be up to 7 times more cost-effective. As a result, the marine
industry enhances the country’s competitiveness in industry and
services.
The marine transport business is an industry that faces similar
challenges, dealing with a vast amount of data in various formats.
This includes route data, weather forecasts, marine security, onboard equipment monitoring, vessel monitoring, vessel tracking,
port operations control, and other relevant information within the
marine transport sector. Data management in marine transport organisations needs significant improvement to handle vast amounts
of data from multiple sources [16]. Challenges primarily arise from
unreliable and slow data transmission, incompatibility among applications and devices, and complexities in processing massive data
for advanced processing and analysis [17].
The study aims to utilise the Data Mesh concept for decentralised
data management in marine transport organisations. Its objectives
include assisting organisations in using analytics for more efficient business strategies, accelerating data asset delivery to manage
business changes, maintaining competitiveness, and enhancing
business impact control. It also seeks to develop data management
techniques to address challenges like handling large data volumes,
faster data product delivery, and establishing data asset standards
and controls.
In the following section, we have reviewed relevant literature.
We aim to give readers insights into the context, challenges, and
potential solutions concerning data management in the maritime
transport business, specifically focusing on data asset strategies.
2 LITERATURE REVIEWS
2.1 Data Management
Data management is essential for all businesses, as organisations
increasingly recognise the value of data as an asset that requires
proper management for success and practical use. The first version of DMBOK was published in 2010, followed by the second in
2014. DAMA-DMBOK2 covers 11 knowledge areas corresponding
to critical topics in data management: Data Governance, Data Architecture, Data Modelling and Design, Data Storage and Operations,
Data Security, Data Integration and Interoperability, Documents
and content, Data Warehousing and Business Intelligence, Reference and Master Data, Metadata, and Data Quality [1]. Regarding
research data management, an organisation’s plan begins with data
collection, storage, analysis, and quality control. This includes regular data audits and consistency checks to ensure data accuracy and
reliability. It also establishes data-use procedures and standards,
covering agreements, compliance, privacy, backup policies, data
cleaning, accuracy, and metadata for data comprehension [4].
Data management offers numerous benefits to organisations,
including improved data flow, efficient time and cost management,
and enhanced data analysis, sharing, and security [18]. Patricia
Cupoli addresses data management challenges in DMBOK2. Organisations must assess data value, establish standards, identify business
benefits, and maintain consistency. Calculating data acquisition,
storage, update, and replacement costs is essential. Organisations
may need help with data acquisition, conversion, and ingestion
to uphold data quality. High-quality data is a valuable asset, and
organisations should avoid decisions based on unreliable data. Corporate data should be accessible, complete, consistent, accurate,
timely, and GDPR-compliant [1].
Zhang Guobao introduced an innovative framework aimed at
enhancing data quality in integration. Data quality (DQ) is defined
as the appropriateness of data for specific purposes, encompassing
completeness, validity, accuracy, consistency, availability, and timeliness. Poor DQ often results from manual errors, slow data entry,
and ETL-induced changes in a data model. The paper presents a
DQ framework that utilizes Domain-Specific Language (DSL) and
quality rules for system integration, enabling DQ’s measurement,
evaluation, and improvement as data changes. This approach also
supports efficient data quality visualization [28].
In the article ”Data Management Problems & Solutions,” organizations may encounter various challenges. These challenges encompass ensuring data accessibility throughout the organisation and
maintaining reliable and up-to-date corporate data for reporting
and analysis [6].
2.2 Modern Data Management
Modern data management empowers organisations to make better
decisions based on available data [7]. For organisations integrating
cutting-edge technologies, such as artificial intelligence and IoT
sensor devices, continuous improvement is essential to support
emerging data types effectively [8]. It focuses on understanding
data’s value and reducing costs for more efficient investments [9].
The Modern Data Management approach automates and streamlines data management, reducing errors, speeding up data retrieval,
and enhancing customer service [10]. Edward Segal highlights corporate data management challenges, especially for long-established
companies, as changes in data ownership can lead to outdated
catalogues, impacting analytics and data quality [12]. Challenges
include managing diverse data sources, types, storage, processing,
and security [11].
Hemn Barzan Abdalla’s research, ”A Brief Survey on Big Data,”
comprehensively addresses storage, processing, security, and related aspects of Big Data. It delves into Big Data terminology, techniques, and performance metrics while charting future research
directions, mainly focusing on processing frameworks [30].
D. I. George Amalarethinam and Lalu P. George introduced a
research paper titled Globus: An Enhanced Data Security Method
to Protect Numerical Data in Public Cloud Storage. The rapid evolution of the Internet has brought forth cloud technology and heightened security concerns. Cloud computing strongly emphasises
data access and security due to the increasing frequency of data
breaches. Data security safeguards personal data, while data protection measures ensure data remains secure even during disasters
[29].”
2.3 Data Mesh
In March 2022, Zhamak Dehghani published a book on data mesh,
focusing on its goal of creating a decentralised data architecture
for handling vast amounts of analytical data. Data Mesh is built
upon four key principles: domain-based decentralised data ownership, treating data as a product, implementing a self-service data
platform, and employing federated computational governance [13].
• Decentralised Data Ownership: In Data Mesh, data ownership is distributed to the business domains closest to the
data. Each data set within the data mesh should have a clear
domain team owner responsible for maintaining data quality.
• Data as a Product: Data is viewed as a product in a data
mesh, promoting active team collaboration. Data owners
take responsibility for maintaining quality, accessibility, discoverability, and usability. This approach facilitates the sharing of domain-specific data with multiple stakeholders.
• Self-Service Data Platform: These services facilitate seamless cross-functional data product sharing across domains,
streamlining the end-to-end process from source to consumption, including development, deployment, and maintenance.
• Federated Computational Governance: This approach
enhances domain engagement by enabling federated
decision-making and accountability. It balances domain autonomy and agility while ensuring interoperability within
the data mesh. It simplifies the interconnection of data products through a self-service platform, addresses cross-cutting
governance needs, and improves efficiency by reducing coordination time between domains and governance processes.
2.4 Marine Transport Business
The marine transport organisation’s primary goal is to provide shipping services by managing vessels and cargo operations, strongly
emphasising reducing transportation costs. It consists of two main
components: 1) Vessels, like production units, and 2) Shipping
Offices, serving as onshore infrastructure [19]. The maritime transport sector exhibits diversity and can be classified according to the
specific vessel types and the cargo’s nature [20]:
• Bulk Shipping Vessel: Designed for unpackaged bulk cargo
like steel, wood, cement, sugar, soy flour, scrap iron, coke,
salt, sulfur, and chemicals.
• Liner Shipping Vessel: Transported diverse cargoes simultaneously, with the total weight not exceeding the maximum
capacity. These cargoes often include high-value and highly
sensitive items.
• Special Transportation: Tailored for oversized cargo like
motor vehicles and steel products, typically carried individually rather than in bulk.
Challenges in marine transport organisations arise from internal
and external factors, including natural changes, human dynamics,
maritime technology, social and labor conditions, and financial
aspects. Adaptation and development of new strategies are essential to navigate these influences and adapt to evolving business
conditions [21].
2.5 Data Management in Marine Transport
Business
In the marine transport sector, data management faces challenges
with handling large datasets, implementing big data analytics, and
dealing with data from various sources and formats [16]. In 2021,
Herodotos Herodotou of the Cyprus University of Technology conducted research on marine data management. The research explores
issues like unreliable data transmission, incompatible programs (GeoMesa, SpatialSpark, and GeoSpark), and the need for processing
large volumes of data for advanced analysis. The goal is to obtain
valuable insights that can be used for critical operations, such as optimising port activities, route planning, and predictive maintenance
[17].
Savita Kumari Sheoran and Vinti Parmar researched Visual Analysis of Spatial Metadata, which is extensively used by both public
and private sectors for decision-making, planning, risk analysis,
and navigation. Their paper introduces Dense Pixel Display visualisation for metadata selection and analysis. They applied this
approach to Gurugram district spatial data using QGIS software,
enabling users to identify and analyse pertinent information from
extensive datasets. The outcomes of their research are beneficial
for tasks such as landfill site selection and finding applications
in experimental research and transportation, providing improved
result clarity [26].
2.6 Data Asset
Data assets play a crucial role in enhancing the effectiveness of data
analytics and insights, leading to significantly improved business
decision-making outcomes. It assists companies and business units
in generating operational data and creating value. With easily accessible data assets, enterprise data, and services, organisations can
realise their long-term objectives, boost productivity, and achieve
financial success [23]. Gaurav Agarwaal’s research on ’Data Asset
Evaluation’ presents method businesses use to assess and manage
their data products. It guides the development of procedures and
practices treating data as an asset and constructing a business case
for data quality and governance [22].
3 METHODOLOGY
This study aims to create a data asset strategy framework based on
the Data Mesh concept to enhance the data management of marine
transport organisations. The primary focus will be developing a
decentralised data team capable of delivering data assets to maintain
efficiency and competitiveness. The researcher utilised data from a
company with 24 Supermax vessels. These vessels have tonnage
between 48,000 and 60,000 DWT and average draft lengths of 12.2
m and 199 m. The scope of the study protocol is divided into four
parts as follows:
• Explore data in the marine transport business and ship
management strategies. This exploration was conducted
through a literature review and interviews with various
business units within marine transport organisations
and bulk carrier shipping companies.
• Design an accurate decentralised data management
(Data Mesh) for marine transport organisations, categorising the study based on ship characteristics and
fleet size.
• Design approaches for creating data products from domain teams to align with the strategies of marine transport organisations and bulk carrier shipping companies,
aiming to generate revenue and reduce operational costs
through data assets.
• Design the data asset cycle for marine transport organisations and bulk shipping carrier companies to understand better the process of creating data assets and
maintaining their efficiency.
• Design a data asset strategy framework for marine
transport organisations and bulk carrier shipping companies to create valuable data assets aligned with business and corporate strategies.
3.1 Design the data mesh concept for the
marine transport
This step aims to design a decentralised data management structure
(Data Mesh) within a maritime transport organisation. It involves
formulating data policies to govern data usage, creating data products, and exploring new data product possibilities aligned with the
organisation’s strategy [24, 25].
3.1.1 Domain-Oriented Ownership.
• Assign a technical leader and specialists to each domain
who can thoroughly understand the problems and provide
appropriate solutions. At this stage, three groups have been
formed:
• The first group comprises individuals who deeply understand the business and its problems, including the Managing
Director, Chartering Director, Marine Director, and other
executives with decision-making authority.
• The second group consists of data owners and users from
various departments, such as Marine Operation, Technical
Operation, Chartering Operation, Commercial Operation,
Safety & Quality, Insurance & Legal, and Vessels.
• The third group includes IT and data teams.
• Decompose the maritime transport business domain into
autonomous subdomains and assign data ownership to the
appropriate teams. At this stage, we divide it into two major
domains.
• In the onshore domain, we can divide subdomains based on
ship characteristics and fleet size.
• In the offshore domain, we focus on individual vessels.
• Define the scope of data products and identify data product
ownership in each domain.
3.1.2 Data as a Product.
• Assign individuals to oversee the domain’s data product
development and architectural design.
• Define responsibilities for data quality and availability and
establish methods for evaluating the correctness of data products.
• Define procedures for publishing and selecting data products
within the domain data team, considering their rights and
roles. This involves identifying product interfaces, assigning
data contracts, and establishing sharing agreements.
3.1.3 Self-Serve Data Platform. Design data consumption methods
and consumer types to determine appropriate data platforms and
share relevant data within the workplace. The platform should
allow for both manual and automatic data access.
3.1.4 Federated Computational Governance.
• Design a domain governance system for maritime transport
data networks to detect errors, recover data, record data
profiles, and identify problems within the data mesh, and
the provenance of a data product must be identified and
available from the domain.
• Design a centralised governance for creating and delivering
data products within each domain to meet organisation-wide
standards, including interoperability, security, documentation, privacy, and compliance —figure 1.
3.2 Design marine transport data products
using the data mesh concept
3.2.1 Define the maritime transport business case. Identify the
key factors affecting an organisation’s revenue and expenses by
analysing its strategy and consulting with middle and senior executives in departments such as Marine Operation, Technical Operation, Chartering Operation, Commercial Operation, Safety and
Quality, Insurance and Legal, and Vessels. Two pressing issues
impacting ship operations demand immediate attention: 1) Carbon Intensity Indicator (CII) Analysis and 2) RightShip inspection
Analysis. This case is an exclusive example within the organisation
the researcher has examined. To ensure the accuracy of data products, it is crucial to continuously study the organisation’s current
corporate strategies and business issues.
3.2.2 Develop Data Product. Carbon Intensity Indicator (CII) Analysis, introduced as an operational efficiency metric for vessels exceeding 5,000 GT starting in 2023, computes the annual average
CO2 emissions per nautical mile of ship capacity transport work.
Vessels receive ratings from A to E based on their CII performance,
with compliance being marked as ’C’ or better. Conversely, vessels
rated ’D’ or ’E’ are considered non-compliant, necessitating owners to devise improvement strategies integrated within their Ship
Energy Efficiency Management Plan (SEEMP). SEEMP, a regulatory requirement since 2013, serves to enhance energy efficiency
through the utilisation of tools such as Energy Efficiency Operational Indicators (EEOI).
To meet the CII standards, vessels must reduce their use of highcarbon fuels. As a result, it is crucial to develop data products that
can efficiently manage fuel consumption and calculate the best ship
speeds. Achieving this goal requires access to vital data sources
like ship fuel consumption data from flow meters, records detailing
ship engine performance and maintenance, and comprehensive
navigation and weather data. This valuable data is sent via satellite
to shore for processing via the ETL (Extract, Transform, Load)
method within a cloud-based system.
The dedicated vessel domain team is responsible for data processing and creating CII Analysis Data Products within vessel operations. These products, once generated, are disseminated to users
within the company domain and external data customers, which
may include charterers, through a structured API system. Internal
and external data customers’ access to these CII Analysis Data Products depends on the access rights specified in the data agreement—
figure 2.
RightShip Inspection Analysis, RightShip inspections comprehensively evaluate a ship’s condition, Safety Management System
(SMS) effectiveness, adherence to industry recommendations, and
the welfare of onboard seafarers. These inspections are vital for
enhancing maritime safety and offer independent assessments valuable to charterers, ship managers, terminal operators, and regulators.
These inspections are conducted by accredited inspectors who
employ standardised methods to ensure consistent and reliable
results. The outcomes of these inspections provide an accurate
snapshot of a vessel’s condition at the time of assessment. They
are crucial in assessing risk controls and offering due diligence to
clients and stakeholders, including charterers, ports, and terminals.
Creating RightShip inspection analysis data products enable
standardised to assess their vessels’ condition comprehensively.
Empower standardised and ship operation teams to continuously
monitor ship conditions, crew well-being, maritime safety, and
adherence to industry recommendations. This information is presented through the RightShip audit results, accessible via an interactive dashboard that provides real-time updates for every vessel
within the company.
RightShip inspection analysis data products are shared through
a user-friendly cloud-based platform interface. This advanced platform provides access to the data domain team and authorised data
users. It allows them to conveniently access, download, and review RightShip inspection analysis reports, including no actions,
in progress, pending, and completed pieces, all via the dashboard.
3.2.3 Defining the Responsibilities of the Domain Team in Developing Data Products. Creating compelling data products requires a
well-organised and knowledgeable domain team. Their responsibilities span various crucial phases, from gathering user requirements
to designing data product architecture and creating detailed implementation plans.
• Collecting and Analysing User Requirements: A deep understanding of user needs and objectives is the foundation of
any successful data product. The domain team begins this
journey by engaging with stakeholders across the organisation, including end-users, data scientists, analysts, and
decision-makers. Through a collaborative process, the team
identifies and documents specific user requirements. This
stage involves understanding what data is needed, why it is
needed, and how it will be used to drive business outcomes.
The domain team must also assess the quality and availability
of existing data sources and whether any new data collection
processes are required.
• Designing Data Product Architecture: Once user requirements are well understood, the domain team proceeds to
design the architecture of the data product. This phase is
akin to creating the blueprint for a building. It involves making critical decisions regarding data storage, processing, and
accessibility. Key considerations include data integration
methods, database design, data processing pipelines, and the
selection of appropriate data technologies. The team must
ensure that the architecture aligns with the scalability and
performance requirements of the data product while also
adhering to data security and privacy standards.
• Creating Implementation Plans: Implementation plans
should cover aspects like data collection and ingestion, data
processing and transformation, model development (if applicable), user interface design, and integration with existing systems. The team should also define project timelines,
resource allocation, and milestones to track progress effectively.
• Collaborating Throughout the Process: The domain team
must work closely with data engineers, scientists, and other
relevant stakeholders throughout the implementation phase.
Regular feedback loops and agile development methodologies can help refine the data product as it takes shape. Continuous testing and validation ensure the product aligns with
user expectations and delivers actionable insights.
• Post-Implementation Monitoring and Optimisation: Even
after a data product is successfully implemented, the responsibilities of the domain team continue. They must monitor
the product’s performance and user feedback, making necessary improvements and optimisations over time. Data
product usage metrics, user satisfaction, and real-world impact should be tracked and analysed. This information helps
refine the product, address emerging user needs, and ensure
long-term value to the organisation.
3.3 Design the marine transport data assets
cycle
Data products are distinct from data assets. Data products are
created with specific goals and have exact domains responsible for
creation, maintenance, and destruction. On the other hand, data
assets encompass various entities containing data, such as databases
or application output files. Data assets enhance the efficiency of
data analytics and insights, adding value to operational data and
generating business value.
The life cycle design for developing data assets for marine transportation organisations [1, 23] —figure 3.
Stage 1: Identify the marine transport company objectives based
on the business strategy.
Stage 2: Consider the data project requirements, both functional
and non-functional, in the marine transport company.
Stage 3: Identify critical success factors that enable data products
to create value for the organisation or its users and assess how the
development of data products will impact the workflow.
Stage 4: Ensure the data product development process aligns
with the company’s policies to prevent data security and privacy
breaches.
Stage 5: Think about the end-users of the data product and the
benefits they could get. Examine how data products can assist their
tasks and find efficient ways to meet their requirements.
Stage 6: Identify the person responsible for the data product. Establish priorities for testing, improving prototypes, documentation,
and requirements for building data products.
Stage 7: Define criteria for selecting data products, evaluate
their performance, and summarise the findings from assessing the
value of data products in the marine transport business.
Stage 8: After using the current data product, conduct an evaluation to gain valuable insights for developing the next version of
the data product.
3.4 Design a framework for the data assets
strategy in marine transport
In the context of a data asset strategy framework for marine transport organisations, it involves defining the processes and methodologies to create, manage, and utilise data assets effectively. The
data asset strategy framework for maritime transport is developed based on Maritime Transport Strategic Management and
Distributed Team Data Management (Data Mesh). The primary
focus is creating, utilising, and developing data products to produce
valuable data assets—figure 4.
The key elements to consider when developing a data asset strategy framework for marine transport organisations involve objectively scoping the comprehensive data asset strategy. The scope
encompasses identifying key areas where data assets can add significant value. Data governance and ownership entail establishing
robust practices to ensure data quality, security, and compliance, including defining data ownership, responsibilities, and access rights
throughout the lifecycle.
Data Product Identification involves identifying potential data
products aligned with specific business needs and opportunities.
This includes understanding end-user requirements to ensure the
relevance and value of developed data products. In Data Product Development, outline the end-to-end process for creating data
products, covering data collection, analysis, modelling, and implementation. Establish stringent guidelines for testing and validating
data products to meet quality standards. Data Integration and Interoperability address the seamless integration of data products
with existing systems and databases, ensuring a smooth data flow
across the organisation—Emphasise compatibility and interoperability among different data products. Finally, in Data Security and
Privacy, implement robust measures to safeguard sensitive data
from unauthorised access or breaches and ensure compliance with
data privacy regulations and industry best practices.
Define how data assets generate valuable insights, supporting
data-driven decision-making in Data Analytics and Insights. Data
Asset Lifecycle Management involves developing a comprehensive plan for continuously managing data assets throughout their
lifecycle, including updates, archiving, and retirement. In Risk Management, identify potential risks associated with data assets and
develop effective mitigation strategies to minimise their business
impact.
In Monitoring and Evaluation, establish vital metrics and performance indicators to measure the success and effectiveness of data
assets. Regularly monitor and evaluate the performance of data
products to ensure they consistently deliver value. Training and
Education provide extensive training and Education to employees
on data asset management practices, data product utilisation, and
best practices for data-driven decision-making. In Adaptability and
Flexibility, recognise the dynamic nature of the data asset strategy
framework, understanding that it may need adaptation over time as
the organisation evolves and new technologies and opportunities
emerge.
4 CONCLUSION
A robust data asset strategy relies on creating high-quality data
products aligned with evolving business requirements, emphasising the concept of Data Mesh. Continuous adaptation is crucial
in marine transport organisations’ dynamic operational life cycle, influenced by natural phenomena, human dynamics, and technological advancements. Our study finds that marine transport
organisations vary based on fleet size, complexity, and goals, necessitating a tailored strategy framework. In medium-sized organisations, cost-effectiveness is a priority, with data products supporting
profitability by reducing operational expenses. The challenges in
developing data products for Carbon Intensity Indicator (CII) and
Rightship inspection analyses are critical for regulatory compliance
and avoiding service disruptions. By systematically addressing
these elements, organisations can maximise data value, ensuring
compliance, security, and adaptability. This strategy serves as a
roadmap, enabling agility and effectiveness in navigating the complexities of the maritime industry.
5 RESEARCH RECOMMENDATION
This strategy is a roadmap for leveraging data as a strategic asset,
enabling companies to navigate the marine transport industry’s
complexities with agility and effectiveness.
Referring to the methodology in sections 3.1, 3.2, 3.3, and 3.4, the
researcher used data from a marine transport company operating
24 Supermax vessels. These medium-sized vessels have tonnage
between 48,000 and 60,000 DWT and typical draft lengths of 12.2
m and 199 m. Companies with similar fleet sizes or organisational
characteristics can adopt this design method as a model for developing data management and creating data assets within their
organisations.
Nevertheless, minor or sizeable marine transport organisations
and bulk carrier shipping companies may need to adjust based on
their fleet size and specific domain characteristics, including identifying key challenges impacting various aspects of their businesses.
However, by following these steps and tailoring them to the unique
needs of the marine transport industry, companies can effectively
leverage their data assets to drive operational efficiency, innovation,
and sustainable growth.
6 FUTURE WORK
Future marine transport data asset strategy research will likely
focus on several key areas. These include integrating emerging
technologies like IoT, blockchain, and AI to enhance operational
efficiency and safety. Sustainability and environmental impact will
remain crucial, with research exploring data-driven approaches to
reduce emissions and minimise the marine transport industry’s
ecological footprint.
Predictive analytics and risk management will be central, leveraging data for accident prevention, risk assessment, and improved
emergency response. Intermodal transportation and supply chain
integration will be vital, with data strategies facilitating seamless
coordination among various marine transport modes.
Ensuring data standardisation and interoperability and the adoption and impact of decentralised data management concepts like
Data Mesh will also be areas of interest. Data ethics and governance,
big data handling and analytics, and the influence of global events
and regulations on the industry will continue to drive research in
this field.