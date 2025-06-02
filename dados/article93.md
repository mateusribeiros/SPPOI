Title: Digital ecosystem for FAIR time series data management in environmental system science

Abstract
Addressing the challenges posed by climate change, biodiversity loss, and environmental pollution requires comprehensive monitoring and effective data management strategies that support real-time analysis and applicable across various scales in environmental system science. This paper introduces a versatile and transferable digital ecosystem for managing time series data, designed to adhere to the FAIR principles (Findable, Accessible, Interoperable, and Reusable). The system is highly adaptable, cloud-ready, and suitable for deployment in a wide range of settings, from small-scale projects to large-scale monitoring initiatives. The ecosystem comprises three core components: the Sensor Management System (SMS) for detailed metadata registration and management; time.IO, a platform for efficient time series data storage, transfer, and real-time visualization; and the System for Automated Quality Control (SaQC), which ensures data integrity through real-time analysis and quality assurance. With its modular and scalable architecture, the ecosystem enables automated workflows, enhances data accessibility, and supports seamless integration into larger research infrastructures, including digital twins and advanced environmental models. The use of standardized protocols and interfaces ensures that the ecosystem can be easily transferred and deployed across different environments and institutions. This approach enhances data accessibility for a broad spectrum of stakeholders, including researchers, policymakers, and the public, while fostering collaboration and advancing scientific research in environmental monitoring.
Previous article in issue
Next article in issue
Keywords
Environmental data managementTime series dataSensor managementAutomated quality controlData integrationMetadataFAIR principlesData infrastructureScalable data infrastructureCloud-ready infrastructure
Metadata
Nr	Code metadata description	Please fill in this column
C1	Current code version	SMS: 1.17.1
time.IO: 0.1
SaQC: 2.6
C2	Permanent link to code/repository used for this code version	SMS: https://github.com/sensor-management-system
time.IO: https://github.com/time-IO
SaQC: https://github.com/saqc
C3	Permanent link to reproducible capsule	SMS: https://zenodo.org/doi/10.5281/zenodo.13329925
time.IO: https://zenodo.org/doi/10.5281/zenodo.8354839
SaQC:https://zenodo.org/doi/10.5281/zenodo.5888547
C4	Legal code license	SMS: EUPL-1.2
time.IO: EUPL 1.2
SaQC: GNU GPL 3.0
C5	Code versioning system used	GIT
C6	Software code languages, tools and services used	SMS: Docker, Elasticsearch, MinIO, nginx, PostGIS Python, TypeScript
time.IO: Alpine, CAdvisor, Django, django-helmholtz-aai, Docker CE, Docker Compose, FastAPI, FROST, Grafana, MinIO, Mosquitto MQTT Broker, nginx, NumPy, Pandas, Python Click, TimescaleDB, Tomcat
SaQC: Python
C7	Compilation requirements, operating environments and dependencies	SMS: Docker, Docker Compose
time.IO: Docker, Docker Compose
SaQC: Python 3.8+
C8	If available, link to developer documentation/manual	SMS:https://hdl.handle.net/20.500.14372/SMS-Readme
https://hdl.handle.net/20.500.14372/SMS-Wiki
time.IO: https://codebase.helmholtz.cloud/ufz-tsm
SaQC: https://rdm-software.pages.ufz.de/saqc/index.html
C9	Support email for questions	SMS: sms-core-team@listserv.dfn.de
time.IO: rdm-contact@ufz.de
SaQC: saqc-support@ufz.de
1. Motivation and significance
Climate change, biodiversity loss, environmental pollution and related anthropogenic impacts are leading to significant pressures on the world's ecosystems and their functions, requiring a comprehensive quantification of these impacts [1,2]. To address this, large-scale and standardised monitoring observatories such as NEON [3], eLTER [4,5] and TERENO [6,7] have been established to provide essential data for the long-term monitoring with sensor systems and modelling of environmental systems. In addition, e.g. MOSES [8] investigates the evolution and impacts of highly dynamic, often extreme events (e.g., heat waves or hydrological extremes) using a systemic monitoring approach including sensor systems. These event-oriented, cross-compartment datasets are needed to understand the impacts of climate change, biodiversity loss and pollution, and to develop effective adaptation strategies and address the development of a federated Global Ecosystem Research Infrastructure [9]. These observation networks are continuously expanding in terms of sensor density and geographical coverage. However, the resulting increase in data volumes poses challenges in handling and processing these continuously growing data streams in real-time while adhering to FAIR principles (Findable, Accessible, Interoperable, Reusable) and leveraging standardised interfaces along with associated sensor- and datastream-related metadata [10,11]. The integration of sensor data into such data infrastructures ensures subsequent real-time availability for further analysis, application of advanced data science methods, quantification of earth observation-based indicators, and integration into environmental models as well as digital twins and information systems [[12], [13], [14], [15]]. Therefore, sensor management, effective storage and automatic quality assurance of time series data require the development of scalable, high-performance, and transferable data infrastructures to support real-time availability and handling of the rapidly increasing volume of sensor data [11,[16], [17], [18], [19], [20]].
1.1. Challenges in data management and existing solutions
In the field of geoinformatics, data management infrastructures for in-situ sensing are often considered an integral part of Spatial Data Infrastructures (SDI) or Geospatial Information Systems (GIS). As such, they are rarely addressed independently in the literature [11,12]. In environmental system sciences, however, there are solutions specifically tailored to the handling of sensor data, some of which offer reusable frameworks [17,[21], [22], [23], [24]]. These solutions prioritize the standardization of data and metadata flows to ensure the subsequent reuse of data. In contrast, data infrastructures for sensors within the Internet of Things (IoT) domain are often designed for short-term data storage and/or operational control and are predominantly used in industries such as manufacturing or automation. Moreover, these systems are typically metric-oriented, focusing on derived values rather than the original measurement data [25,26]. Historically, such data management infrastructures have often been developed independently within institutions and integrated into existing IT frameworks, which complicates their scalability and promotion. The rapid growth of sensors and observatories has surpassed the scalability of these legacy systems. As a result, interdependencies have emerged that make comprehensive system overhauls resource-intensive, often limiting progress to incremental improvements rather than holistic redevelopment [11,12]. Cloud-based solutions that can be implemented universally have begun to emerge, offering a promising alternative to these traditional approaches. However, these solutions are often domain-specific, such as those used in Critical Zone Observatories or hydrology [23,24]. Furthermore, robust time series data infrastructures facilitate the integration of data from diverse sources into distributed data infrastructures at institutional, regional, national and continental levels. These solutions also enable real-time applications in digital twins, integration into Spatial Data Infrastructures, and assimilation into environmental models. Such capabilities ensure the dissemination of data to a wide range of stakeholders, including scientists, policymakers, resource managers and the general public.
1.2. Towards a holistic framework for sensor data management
In response, we have pursued an innovative approach to collaboratively design and systematically develop a user-centric comprehensive data infrastructure specifically for time series data management of sensors in environmental science with the following characteristics and requirements. These are:
•
Interoperability: Use of standardised interfaces and metadata standards as well as standard protocols for sensor integration, enabling compatibility with geospatial infrastructures for seamless spatial data handling
•
Modularity: Application of Sensor management components with persistent identifiers, sensor data infrastructure component with the ability to connect different storage solutions, and quality assurance/data processing component, each independently deployable, and extendable to geospatial systems
•
Transferability and cloud readiness: Use open source solutions in a microservice architecture, and container-based deployment for easy scalability and integration with existing IT infrastructures
•
Authentication system: Leverage cross-institutional identity management to enable collaboration and the ability to use own authentication systems
•
User-friendly: With simple responsive web interfaces for operation and integrated data viewers for data dissemination
•
Generic application: Applicable to all domains using sensor-based data, to go beyond environmental system science
2. Digital ecosystem for FAIR time series data management
The conception of the digital ecosystem for FAIR time series data management began in 2019, building on the experience gained in the development of an interoperable data infrastructure for the TERENO observatories since 2009 [6,7,22]. Particular emphasis was placed on ensuring that both the (meta)data and the data flows meet the FAIR criteria [10]. Furthermore, the digital ecosystem and its software components were designed to comply with the FAIR principles for research software [27], establishing a state-of-the-art solution. This approach was intended to develop a reference model for research infrastructures in Environmental System Science. The adherence to the FAIR criteria for (meta)data as outlined by Wilkinson et al. [10] is detailed in Appendix 1. A key highlight is the enrichment of metadata during data processing, which ensures comprehensive reproducibility. Further attention has been paid to the modularity of the overall system and to the ability of the components to operate independently. One of the key innovations of this integrated system is its transferability and usability by other research institutions, authorities, companies and organizations worldwide. It has been designed to be easily deployable and adaptable to diverse needs, significantly improving the accessibility and usability of time series data for end users, operators, system integrators, and maintainers. The digital ecosystem for FAIR time series data management has been designed under specific conditions and requirements and consists of three core components or independently usable systems:
(i)
Sensor Management System (SMS): Facilitates the detailed registration of sensors with an internal and globally available persistent identifier (EUDAT B2INST1) and the management of sensor metadata using international standards (OGC SensorML2). Authentication is managed by the Helmholtz AAI3, which allows all users from institutions connected to GÉANT EduGAIN4 to log in. It also includes the option to use an alternative institutional or other identity provider system.
(ii)
Data Infrastructure (time.IO): Provides the infrastructure for storing and managing time series data. Standard input protocols ((S-)FTP and MQTT5) are used for data ingestion, while the standardised OGC SensorThings API (OGC STA6) is used for data access. Authentication is handled by the Helmholtz AAI3, enabling all users from institutions connected to GÉANT EduGAIN4 to log in. Additionally, it offers the option to use an alternative institutional or other identity provider system.
(iii)
System for Automated Quality Control (SaQC): Enables real-time analysis, annotation, and processing of data using predefined or custom quality schemes in real-time, including end-to-end metadata enrichment for each data point. This can be done using pre-configured standard procedures and user-configured methods for a variety of environmental variables.
The integration of the three primary components into a comprehensive digital system for sensor-based time series data (Fig. 1) is achieved through specific strategies. For example, SaQC is directly embedded within the time.IO orchestration framework as a dedicated subsystem operating in a separate container. In contrast, the connection between the Sensor Management System (SMS) and time.IO is established via a REST API. This modular design streamlines the integration process: time.IO orchestration inherently includes SaQC, while the linkage between an active SMS instance and time.IO is managed entirely through time.IO configuration settings.
Fig 1
Download: Download high-res image (161KB)
Download: Download full-size image
Fig. 1. Software architecture of the digital ecosystem for FAIR time series data management with the three main components for the management of sensor metadata (SMS), data (time.IO), and analysis or automated quality control of the data (SaQC).

The overall system includes all essential components, such as user-centric web-based front-ends for the sub-components, a versatile data integration layer, robust time-series database, efficient object storage, real-time quality control, and comprehensive real-time data visualization functions. It supports modern and legacy data transfer protocols ((S-)FTP and MQTT) and ensures compliance with OGC standards for data access and sensor metadata. In addition, the fully integrated containerized solution offers the convenience of rapid deployment and seamless integration with existing institutional services such as databases, identity providers, and object stores. The following sections will provide detailed descriptions of the three main components of the Digital Ecosystem for FAIR Time Series Data Management.
2.1. Sensor management system (SMS)
The Sensor Management System (SMS) is the foundation for sensor metadata handling. It allows detailed registration and management of sensors and specific measurement parameters, documenting changes over time. Additionally, the SMS supports the planning and management of complex measurement setups and campaigns over time. A controlled vocabulary ensures metadata consistency. Following the JSON:API7 specification and adhering to international standards, such as OGC SensorML, SMS ensures that data sources are discoverable and accessible through standardized interfaces (Fig. 2). The SMS uses the EUDAT B2Inst identifier as its PID system to ensure metadata integrity throughout the data lifecycle. This is particularly important for integration into larger data infrastructures and for providing consistent metadata management. It uses a container-based deployment model for easy integration and scalability within existing IT infrastructures.
Fig 2
Download: Download high-res image (1MB)
Download: Download full-size image
Fig. 2. Front-End SMS. The sensor management system (SMS) is designed to handle the acquisition and management of metadata from various sensors.

Its main features include:
•
Sensor Registration and management: Allows for the detailed registration and management of sensors and specific measurement parameters, documenting changes over time. The permanent registration of the instruments is done with the globally available persistent identifier (EUDAT B2INST) to ensure metadata integrity throughout the data lifecycle.
•
Standard interfaces: Uses JSON:API and follows international standards (OGC SensorML) for the provision of sensor metadata and measurement parameters.
•
Accessibility: Ensures that all sensors with their metadata are findable and accessible through standardized interfaces.
•
Deployment: Provides a container-based deployment model for easy integration and scalability within existing IT infrastructures.
For more details, see Brinckmann et al. [28] and/or https://hdl.handle.net/20.500.14372/SMS-Wiki
2.2. time.IO
Building on the foundation of sensor metadata using SMS, time.IO provides the infrastructure for storing and managing time series data. It supports the entire lifecycle of time series data, providing efficient data transfer and storage, real-time data visualisation using Grafana, and integrated data analysis and quality control with SaQC. The container-based deployment model facilitates easy integration and scalability within existing IT infrastructures, including seamless connection to geospatial infrastructures such as spatial.IO [29] for advanced spatial data analyses. time.IO also links to the SMS for consistent and standardised metadata management, ensuring a cohesive data management process (Fig. 3). For data access, the standardised OGC SensorThings API (OGC STA) is used and utilises the FROST-Server as a reference implementation for the OGC STA interface [30].
Fig 3
Download: Download high-res image (429KB)
Download: Download full-size image
Fig. 3. Front-End time.IO. The time.IO is developed to handle the entire lifecycle of sensor based data streams.

Its functionalities include:
•
Data transfer and storage: Efficiently handles the transfer and storage of large volumes of time series data. time.IO provides transfer endpoints such as (S-)FTP servers or MQTT and supports the integration of existing data transfer infrastructures. For data access, the OGC SensorThings API is used, utilizing the FROST-Server as a reference implementation.
•
Data visualisation: Uses Grafana8 to provide real-time visualizations of time series data within automatically setup, preconfigured and shareable dashboards.
•
Quality control: Integrates seamlessly with SaQC to ensure data quality and integrity.
•
Metadata management: Uses the SMS for consistent and standardized metadata management.
•
Deployment: Provides a container-based deployment model for easy integration and scalability within existing IT infrastructures.
For more details, visit Schäfer et al. [31] and/or https://codebase.helmholtz.cloud/ufz-tsm
2.3. System for automated quality control (SaQC)
Completing the ecosystem, SaQC automates the quality control of time series data, improving traceability and reproducibility. It supports detailed data analysis based on a catalogue of state-of-the-art time series analysis, data processing, and annotation of data using predefined or custom quality schemes (Fig. 4). The meticulous collection of metadata throughout all operations ensures that resulting data meets quality standards such as traceability and reproducibility. This automated quality control is essential to maintain the integrity of data used in environmental research [32].
Fig 4
Download: Download high-res image (517KB)
Download: Download full-size image
Fig. 4. Front-end SAQC (GUI): Users can add tests for their data in the panel on the left and see the resulting flags on the right side. These configurations can then be used for automated testing, allowing for continuous monitoring and quality assurance of the data.

SaQC is designed to automate the quality control of time series data, improving traceability and reproducibility. Key features include:
•
Data Analysis: Provides state of the art algorithms for detailed analysis of time series data.
•
Data Processing: Exposes a large set of data processing features
•
Data Annotation: Supports the annotation of time series data using predefined or custom quality schemes.
•
End-to-end metadata enrichment: Enrich metadata from initial data collection to final use, ensuring metadata integrity throughout the data lifecycle.
•
User interfaces: Provides flexibility through a Python API, text-based configuration, and a web application.
For more details, visit Schmidt et al. [32], Schäfer et al. [33] and/or https://git.ufz.de/rdm-software/saqc.
3. Illustrative example
The presented toolchain encompasses every stage of the typical sensor data lifecycle through user-friendly frontends, which include (i) metadata registration during sensor deployment, (ii) the setup of data transmission, including the automatic generation of endpoints, accounts, and credentials, (iii) real-time monitoring and provisioning of incoming data streams, and (iv) the configuration and parameterization of quality control pipelines. This self-service approach is designed specifically for data producers, data managers, and technicians, abstracting the technical complexities of underlying technologies such as data transfer and storage (see Fig. 5).
Fig 5
Download: Download high-res image (666KB)
Download: Download full-size image
Fig. 5. The toolchain for implementing a CRNS sensor into the digital ecosystem and the necessary workflow steps.

3.1. Cosmic ray neutron sensing (CRNS)
CRNS - Cosmic Ray Neutron Sensing is a method for determining average soil moisture (non-contact technology) for areas of about 5-15 hectares [34]. This novel approach to soil moisture measurement is one of our reference use cases for time.IO and well established in the TERENO community.
A typical usage pattern begins with registering the CRNS sensor's metadata in the Sensor Management System, where detailed information about the device – such as type, manufacturer, model, and the quantities it measures, including air temperature, air pressure, and neutron counts – is provided (Fig. 6). Next, a 'Thing' is created in the time.IO frontend. The term 'Thing' is derived from the OGC SensorThings API data model and is best described as a data transmission unit. In practice, a Thing often corresponds directly to a data logger or sensor. The user is required to input information such as hostnames for (S-)FTP servers or MQTT brokers, as well as account settings and credentials (Fig. 7). Once the data transmission unit is operational, data monitoring can be conducted through Grafana. All incoming data becomes immediately visible in automatically set up and pre-configured dashboards. Subsequently, SaQC can be configured within the time.IO frontend to apply quality control and data processing directly within the data stream. Finally, data and metadata are provided both through the built-in Grafana dashboard (Fig. 8) for human users and via the OGC standard SensorThings API for machine-to-machine data exchange (Fig. 9).
Fig 6
Download: Download high-res image (152KB)
Download: Download full-size image
Fig. 6. SMS – Manage sensor metadata.

Fig 7
Download: Download high-res image (118KB)
Download: Download full-size image
Fig. 7. time.IO – Configure dataflows.

Fig 8
Download: Download high-res image (222KB)
Download: Download full-size image
Fig. 8. Grafana – Visualize sensor data.

Fig 9
Download: Download high-res image (355KB)
Download: Download full-size image
Fig. 9. STA – Access sensor data and metadata.

4. Impact and discussion
This section provides a concise evaluation of the ecosystem's implications, divided into two primary dimensions: its limitations and constraints, and its broader impact on environmental research and practice. This approach highlights the system's strengths and areas for improvement, offering a balanced perspective for current and potential adopters.
4.1. Limitations and constraints
The ecosystem emphasizes strict data integrity by employing a design that stores both raw and processed data, ensuring that raw data remains unaltered. This approach inevitably increases storage requirements, particularly when managing large datasets. Despite the added storage demands, the system prioritizes data integrity and persistence over minimizing storage usage, underscoring its commitment to data reliability.
The integration of advanced in-stream data processing functionalities introduces potential challenges, such as increased server loads, particularly in scenarios involving large datasets or complex processing workflows. To address these challenges, the ecosystem supports horizontal scaling of the time.IO component, allowing dynamic resource allocation to mitigate bottlenecks. The ability to represent complete data flows from source to end-user within a unified software system is considered sufficient justification for the associated hardware adjustments.
The ecosystem does not include integrated backup and recovery mechanisms. Instead, it relies on well-established and widely used software systems, namely MiniIO and PostgreSQL, for data storage. These systems provide robust backup and failure management functionalities. Consequently, users are encouraged to leverage these built-in mechanisms to fulfill their backup and recovery requirements.
4.2. Impact
The digital ecosystem for managing time series data has significantly advanced research and practical applications in environmental system science. The integration of SMS, time.IO, and SaQC within this digital ecosystem has opened up new research opportunities, particularly in real-time applications and data visualization. Automated, real-time quality control and immediate data viewers allow researchers to monitor and respond to environmental changes as they occur. This capability supports the study of dynamic events and enhances iterative research designs, enabling precise exploration of complex environmental interactions. The system's standardized framework also facilitates cross-disciplinary research by seamlessly integrating diverse sensor data, broadening the scope of environmental studies.
Daily practices have evolved with the system's deployment. Automated workflows reduce manual data management, allowing researchers to focus on analysis rather than logistics. User-friendly interfaces make advanced data management accessible, boosting productivity and enabling more efficient handling of large datasets.
The system's modular and cloud-ready architecture ensures its broad applicability and transferability across diverse research environments. By adopting standardized methods and protocols, the ecosystem enables consistent and reliable data management practices, making it possible to deploy identical infrastructures across different institutions. This standardization facilitates not only consistent workflows and data sharing but also seamless integration with geospatial infrastructures such as spatial.IO [29], thereby enhancing spatial analyses, interdisciplinary collaboration, and the comparability of research outcomes globally. The system's versatility ensures that it can be effectively utilized in various scales of research, from localized projects to large-scale monitoring networks, driving innovation and efficiency in environmental data management.
5. Conclusions
The integration of the Sensor Management System (SMS), time.IO for storage, transfer, and real-time visualization, and the System for Automated Quality Control (SaQC) represents a significant advancement in the field of environmental data management. This digital ecosystem not only ensures the comprehensive management of time series data but also enhances data integrity, accessibility, and usability. By combining data acquisition, temporal alignment, and real-time quality control, the system supports robust environmental research and informed policy-making. Additionally, its capabilities to facilitate real-time applications, dynamic event monitoring, and cross-disciplinary research significantly broaden its impact in advancing environmental system science.
The modular, cloud-ready architecture and use of standardized protocols make the ecosystem highly adaptable and transferable across various research environments. This flexibility allows for consistent data management practices across institutions, fostering collaboration and enabling the comparability of research outcomes. Its integration into larger infrastructures, such as digital twins and environmental models, highlights its potential to transform data-driven research and decision-making processes.
The digital ecosystem's ability to handle increasing data volumes and provide real-time insights supports emerging research needs, particularly in the context of climate change and biodiversity loss. It can be effectively deployed in both small-scale projects and large-scale monitoring networks, making it a versatile tool for advancing environmental science. By addressing current gaps in data management, it enables researchers to adopt innovative approaches and respond dynamically to environmental changes, fostering the development of effective adaptation strategies.
In summary, this digital ecosystem offers a powerful, standardized solution for managing environmental sensor data, supporting the pursuit of new research questions and improving the efficiency and reliability of existing studies. Its widespread adoption will likely drive further innovation in environmental monitoring and data management, benefiting a broad range of stakeholders in both scientific and practical contexts. The system's capacity to support iterative research designs, improve interdisciplinary collaboration, and provide actionable insights marks a substantial step forward in addressing global environmental challenges.
CRediT authorship contribution statement
J. Bumberger: Writing – review & editing, Writing – original draft, Supervision, Project administration, Methodology, Conceptualization. M. Abbrent: Writing – review & editing, Software, Methodology, Conceptualization. N. Brinckmann: Writing – review & editing, Software, Methodology, Conceptualization. J. Hemmen: Writing – review & editing, Software, Methodology, Conceptualization. R. Kunkel: Writing – review & editing, Supervision, Methodology, Conceptualization. C. Lorenz: Writing – review & editing, Supervision, Software, Methodology, Conceptualization. P. Lünenschloss: Writing – review & editing, Software, Methodology, Conceptualization. B. Palm: Writing – review & editing, Software, Methodology, Conceptualization. T. Schnicke: Writing – review & editing, Supervision, Methodology, Conceptualization. C. Schulz: Writing – review & editing, Software, Methodology, Conceptualization. H. van der Schaaf: Writing – review & editing, Supervision, Methodology, Conceptualization. D. Schäfer: Writing – review & editing, Writing – original draft, Supervision, Software, Methodology, Conceptualization.
Declaration of competing interest
The authors declare that there are no conflicts of interest relevant to this work.
Acknowledgements
We thank the Helmholtz Association and the Federal Ministry of Education and Research (BMBF) for supporting the DataHub initiative of the Research Field Earth and Environment. The DataHub enables an overarching and comprehensive research data management, according to the FAIR principles, for all topics of the programme Changing Earth – Sustaining our Future.
The publication is a contribution in the context of the work of the NFDI4Earth – the consortium for the Earth System Sciences within the German National Research Data Infrastructure (NFDI) e. V.. The NFDI is financed by the Federal Republic of Germany and its 16 federal states, and the NFDI4Earth is funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – project number: 460036893. The authors would like to express their gratitude for the funding and support.
This research has been supported by the European Commission, Horizon 2020 (H2020 Project eLTER PPP, grant no. 871126, eLTER PLUS, grant no. 871128 and eLTER EnRich, grant no. 101131751) in the context of the development of the eLTER cyberinfrastructure.
Appendix 1
Criterion	Description	Implementation in the Paper
To be Findable
F1	(meta)data are assigned a globally unique and eternally persistent identifier.	Persistent identifiers (e.g., EUDAT B2INST) are used for sensor metadata, ensuring global uniqueness and persistence. SaQC workflows are version-controlled via Git, providing traceability for all processing steps.
F2	Data are described with rich metadata.	Detailed metadata is managed using international standards such as OGC SensorML in the Sensor Management System (SMS). SaQC enriches metadata during processing, adding details on quality flags, QC-tests performed, and versioning of workflows.
F3	(meta)data are registered or indexed in a searchable resource.	Metadata and data are indexed via searchable platforms enabled by SMS and time.IO components. SaQC outputs structured data (e.g., .csv or .parquet) with detailed metadata, facilitating integration into searchable systems.
F4	Metadata specify the data identifier.	Each dataset's metadata includes specific identifiers, ensuring clear referencing and traceability. SaQC metadata links data points to their processing history, including information on applied QC tests and configurations.
To be Accessible
A1	(meta)data are retrievable by their identifier using a standardized communications protocol.	Standardized OGC SensorThings API, MQTT, and (S-)FTP protocols are utilized for data retrieval and transfer. SaQC enables consistent, accessible QC workflows, ensuring retrievability through standardized outputs.
A1.1	The protocol is open, free, and universally implementable.	Open protocols like MQTT and OGC SensorThings API are implemented, ensuring universal accessibility. SaQC is open-source, available via Python Package Index (PyPI) and Git repositories.
A1.2	The protocol allows for an authentication and authorization procedure, where necessary.	Authentication is managed using Helmholtz AAI, supporting institutional and cross-institutional logins via EduGAIN. SaQC ensures that processing steps are documented, enabling access control to data derived from authenticated workflows.
A2	Metadata are accessible, even when the data are no longer available.	Metadata management ensures independent accessibility, maintained via the Sensor Management System (SMS). SaQC preserves metadata for all processed datasets, even if raw data is no longer available.
To be Interoperable
I1	(meta)data use a formal, accessible, shared, and broadly applicable language for knowledge representation.	The system adheres to standards like OGC SensorML for knowledge representation. SaQC's configuration uses simple, standardized syntax (e.g., YAML-like text files) for QC tests and workflows, ensuring accessibility and compatibility.
I2	(meta)data use vocabularies that follow FAIR principles.	Vocabularies conforming to FAIR standards, integrated within the system, ensure interoperability and standardization. SaQC uses customizable and standardized flagging schemes to represent data quality, enabling integration with other FAIR systems.
I3	(meta)data include qualified references to other (meta)data.	Metadata links within the system connect data points, provenance, and related datasets using qualified references. SaQC records and references data provenance explicitly, including information about QC tests and their results.
To be Re-usable
R1	(meta)data have a plurality of accurate and relevant attributes.	SMS and SaQC manage attributes accurately, enriching metadata during all stages of data handling. SaQC allows for detailed annotations of each data point, including quality flags and test results.
R1.1	(meta)data are released with a clear and accessible data usage license.	Licenses (e.g., EUPL-1.2 for SMS, GNU GPL 3.0 for SaQC) are clearly specified for software and data.
R1.2	(meta)data are associated with their provenance.	Provenance is documented throughout the data lifecycle, supported by SMS and SaQC for end- to-end metadata enrichment. SaQC maintains a complete log of all processing steps and metadata changes, ensuring full traceability.
R1.3	(meta)data meet domain-relevant community standards.	Domain standards, such as OGC SensorML, ensure compatibility with environmental and geoscience communities. SaQC's flexibility supports customization to meet community-specific QC needs, while adhering to widely accepted standards.