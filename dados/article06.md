Title: Development of a Service-Oriented Interoperability Framework: The Botswana E-Government 

Efficient information exchange between government entities and citizens is crucial for effective governmental service delivery. However, egovernment systems in developing countries like Botswana face challenges due to a lack of communication and integration among these
systems. This case study addresses the interoperability challenges in Botswana's e-government systems by exploring and documenting the
development of the e-government service-oriented interoperability framework (e-GSOIF). This framework integrates various technological
and methodological approaches to improve service delivery and efficiency. It incorporates service-oriented architecture (SOA), event-driven
architecture (EDA), ontologies, a refined software development lifecycle methodology, and the interoperability practical implementation
support (IPIS) approach. The study pinpoints key factors impacting e-government system implementation and interoperability in Botswana
through interviews, questionnaires, and observation. It also identifies essential technical components for E-Government Interoperability. The
e-GSOIF framework is evaluated against the original IPIS framework using exploratory factor analysis and compatibility assessment with
predefined functionality criteria, demonstrating its superiority. This paper targets government officials, IT specialists, researchers, and
students interested in e-government services interoperability. It offers insights into advancing the landscape of e-government service delivery
through an effective interoperability framework.
CCS Concepts • Computer systems organization → Architectures • Applied computing → Enterprise computing • Information
systems → Information systems applications
Keywords: E-government, interoperability, service-oriented architecture, event-driven architecture, developing countries
1 Introduction
Governments worldwide, both in developing and developed countries, have introduced e-government services as
part of their daily activities [1]. According to [2], e-government is the adoption of electronics and ICT in
government organizations, henceforth enhancing efficiency, transparency, effectiveness, accountability, and
communication. E-government was initially understood as using ICT to improve government agencies' efficiency
and provide government services [3]. Later the e-government concept was broadened to include a wide range of
interactions with citizens and businesses [4]. Samsor [5] states that e-government means everything from online
services to exchanging information electronically with government organizations, private businesses, and citizens
via the Internet. 
The main purpose of e-government implementation is to improve the internal work performance of
government organizations through cost reduction and integration of workflows across various public agencies [6].
There is, however, a rising problem of increasing complexity due to duplication and redundancy of services [7].
Challenges for e-government related to interoperability, include issues of technological complexity, regulatory
uncertainties, and the need for comprehensive governance frameworks to manage decentralized digital
architectures effectively [8]. Inadequate ICT infrastructures, specifically in developing countries, lead to unmet
functional expectations and an inability to successfully implement e-government systems [9, 10]. Mohamad et al.
[4] further argue that the lack of ICT infrastructures degrades the performance of e-government system
implementation. Lack of ICT infrastructures and limited ICT resources have proven to be among the main
challenges in e-government implementation in developing countries [11].
Botswana strives to implement efficient and effective e-government systems. However, system interoperability
and information exchange are still a challenge in the government departments and organizations in Botswana.
Botswana had long adopted the national ICT policy, named Maitlamo1
 [12]. One of the objectives of Maitlamo is
to outline the possible routes to e-government system implementation; however, the results over the years, as
shown by Porogo and Kalusopa [13] and Mosweu and Bwalya [14], are still unsatisfactory. Another relevant
policy was the Botswana E-government Master Plan 2015-2021, also known as 1Gov [15]. 1Gov expressed
Botswana's vision to become an integrated government by providing universal access to services in a convenient,
efficient, transparent, and reliable way [15]. These policies served as a legal framework for the implementation of
e-government services in Botswana. However, as demonstrated in [13], in the case of public sector records, there
was still little progress in the implementation of interoperable e-government systems. Another evidence of the
insufficient progress in the implementation of interoperable services supplied in [14] is e-record systems. E-record
systems in Botswana are not interoperable within or between the public and private sectors, resulting in
duplication of effort, manual data sharing, non-standardized reporting procedures, fragmented care delivery, and
unnecessary expenditure [16]. This research collected more evidence of the non-interoperability of existing egovernment systems in Botswana.
Interoperability is defined as the ability of diverse systems to work together, enabling seamless information
exchange and interaction towards mutually beneficial and agreed common goals [17, 18]. It encompasses
technical, organizational, legal, political, and social aspects, ensuring that different systems and organizations can
share information and knowledge effectively [19]. Service-oriented architecture (SOA) and event-driven
architecture (EDA) are two architectural approaches that facilitate interoperability in e-government systems.
According to [20], SOA is an architectural model that boosts an enterprise's efficiency, agility, and productivity by
using services as the main means to represent solution logic, supporting the achievement of strategic goals in
service-oriented computing. SOA is an approach that enhances interoperability by establishing a software
architecture that outlines the use of services to meet basic requirements, thereby making them available as
independent, standardized services [21]. EDA, on the other hand, is a design approach for distributed systems that
emphasizes modularity, scalability, and concurrency, characterized by independently operating components
activated by event flows representing critical business facts or domains [22]. In EDA, applications and systems
transmitting events between loosely coupled components focus on processing and publishing messages to
enhance responsiveness in unpredictable and asynchronous environments [23]. Ontologies provide uniform
semantics and explicit formal models, which are crucial for building distributed and interoperable environments
[24]. An ontology is defined as a data model that represents a set of concepts in a specific domain and the
relationships among those concepts [24].
Effective interoperable e-government systems should be reliable, economical, and easy to maintain [25].
Technical complexity coupled with the complexity of managing a process in organizations results in high failure
of e-government systems [26]. Saputro et al. [17] state that standards are essential for facilitating interoperability
in e-government and creating shared infrastructure. Barakat et al. [27] name the inability to reach an agreement
on terms upon which organizations deploy their interpretations as one of the challenges in achieving
interoperability. In addition to that, Mohamad et al. [4] point out that stand-alone, non-integrated systems are not
capable of enabling communication between governments leading to a lack of interoperability. 
The objective of this paper was to explore and document the development of a service-oriented interoperability
framework within the Botswana e-government system case study. The research question addressed in this paper
is ۔What components and design principles can be used in the development of the Botswana e-government
interoperability framework?ە
The rest of the paper is organized as follows. Section 2 presents related work. Section 3 is the research
methodology. Section 4 is the results. Section 5 is a discussion of the results. The conclusion, limitations of the
study, and future work are presented in Section 6.
2 Related Work
Most publications reviewed in this section are recent, indicating that they reflect the current situation regarding
interoperability challenges in developing countries and proposed solutions. The issues outlined in these
publications have likely persisted into the current year, suggesting ongoing relevance to current conditions and
challenges. Regarding the selection of publications presenting related work, it is also worth noting that
researchers from developing countries often publish in lower-tier or non-indexed journals due to financial
constraints; however, many universities still accept such publications for performance appraisal and promotion
purposes. Nonetheless, most of the cited works in this review are recent and indexed in reputable databases like
Scopus, ensuring their academic credibility.
2.1 Challenges of E-government Interoperability in Developing Countries
Interoperability challenges in developing countries critically affect the deployment and functionality of egovernment systems. Below are some recent examples of such challenges.
E-government systems in Benin face significant challenges related to system interconnectivity and cyber
threats [28]. Implementing comprehensive architectures integrating multiple operational levels is vital for
securing and streamlining government processes.
In the Democratic Republic of the Congo (DRC), the shift towards e-government propelled by advances in
Internet technologies, introduced complex interoperability challenges among various government agencies [29]. A
proposed solution involves adopting a microservices-based G2G interoperability architecture to enable more
flexible and effective communications.
Despite the substantial integration of e-government systems within the public service sector in Indonesia,
actual system utilization remains below expectations [30]. Implementing advanced middleware solutions, such as
the government service bus, could significantly enhance operational efficiency and system usage.
In Jordan, the challenges faced in the context of e-government services primarily revolve around issues of
quality, security, and privacy [31]. These factors significantly impact citizens' trust and their willingness to use egovernment services.
In Morocco, an examination of public sectors reveals a critical problem with data volume management and
interoperability among e-government systems [32]. This is further compounded by a neglect of semantics and
shared knowledge, which disrupts data exchange [33]. Enhanced interconnection and communication
infrastructures are essential to overcome these barriers.
In Sierra Leone, the landscape of digital health is full of significant interoperability challenges that impede
effective system interactions. Research by Chukwu et al. [34] emphasizes the necessity of integrating global
interoperability standards and leveraging technologies like blockchain to address data blocking and enhance
interoperability, particularly in resource-limited settings. Integrating blockchain technology with the egovernment interoperability framework could enhance data security, improve interoperability through
standardized protocols, facilitate transparent transactions, enable automated service delivery via smart contracts,
and bolster identity management as supported by [8] and [35].
In Tanzania, challenges in integrating e-government services include technological gaps, insufficient ICT
policies, and limited infrastructure [36]. Additional barriers to the successful integration of e-government services 
are organizational resistance, financial constraints, and political dynamics that impede the adoption and effective
implementation of a unified e-government framework.
In Uganda, the ineffective use of data (specifically, health data) due to non-standardized formats and
inadequate governance underscores broader interoperability issues within e-government frameworks [37].
Standardizing data formats and improving governance protocols are critical steps toward resolving these issues.
In summary, these recent studies from Benin, the DRC, Indonesia, Jordan, Morocco, Sierra Leone, Tanzania,
and Uganda illustrate the diverse challenges faced by developing countries in achieving e-government
interoperability. These challenges range from technical integration to security concerns, emphasizing the need for
tailored solutions that consider local contexts and the specific needs of public sectors in developing countries.
2.2 Frameworks for E-government Interoperability
An interoperability framework aims to reference the basic technical specifications that all agencies relevant to the
implementation of the e-government strategy should adopt. This interoperability framework should enable, at
least, the interoperability between information systems from different agencies in order to provide services to
citizens and businesses in an integrated way [38]. As a way of dealing with e-government systems failures due to
the lack of interoperability, several frameworks and models have been introduced. These are known under the
general name of e-government interoperability frameworks (e-GIF). An interoperability framework is a model
that specifies a set of common elements for an extended organization or state that wishes to work together
toward the joint delivery of public services [39, 40]. According to Reyes Jr and Tangkeko [39], an e-GIF aims to
provide conceptual guidance toward the development of an e-government ecosystem. Common elements of an eGIF include policies, guidelines, principles, standards, vocabularies, and concepts [41]. E-GIF models are essential
for e-government implementation, hence the attempts of various countries, both developed and developing, to
implement them and name them differently depending on their concepts and aims [42]. An e-GIF facilitates the
integration of services and information flow between government entities, aiming to enhance the efficiency,
accessibility, and transparency of government operations [43]. E-GIF models are essential as they detail
integration for better e-government system implementation [44]. Subsections 2.2.1 and 2.2.1 present an overview
of e-government frameworks proposed to solve interoperability challenges in developed and developing countries,
respectively.
2.2.1 Frameworks for E-government Interoperability in Developed Countries
This subsection explores various frameworks for e-government interoperability that have been developed and
implemented in developed countries. These frameworks aim to facilitate efficient data exchange and cooperation
across different levels of government, aiming to enhance public service delivery through technical, semantic, and
organizational interoperability.
The Australian Government Technical Interoperability Framework (AGTIF) is structured to enhance data
exchange and cooperation across government agencies by defining key components such as principles for
collaboration, a conceptual model, and standards selection criteria [45]. Its strengths include fostering a unified
approach to technical interoperability, enhancing security, and supporting efficient public service delivery
through the adoption of common technical protocols. However, weaknesses and gaps include potential
inconsistencies in implementation due to differing agency capabilities and a focus primarily on technical aspects,
which may overlook the critical integration with information and business process domains needed for
comprehensive interoperability.
The European Interoperability Framework (EIF) seeks to strengthen interoperability among European public
administrations, promoting efficient cross-border service delivery [46]. It provides a set of principles and a
conceptual model encompassing four levels of interoperability: legal, organizational, semantic, and technical.
These principles are crucial for addressing the challenges faced by governments and municipalities in Europe, as
illustrated in [47], which examines the difficulties in adapting a governmental e-service platform for a consortium
of Finnish municipalities. Another example is the Greek National Interoperability Framework (Greek NIF), which,
despite being aligned with the second version of the EIF (2008), saw limited implementation, underscoring the
need for continuous updates to national frameworks to stay aligned with evolving EIF standards and technological
advancements [48]. The EIF emphasizes the significance of interoperability agreements to ensure coherent and
effective public service delivery. National interoperability frameworks (NIFs) adopted by EU countries, such as the
EIF, demonstrate the potential to enhance digital public service delivery by fostering interoperability across
government systems [49]. These frameworks also improve the interactions between citizens and public
administrations, proving their value in delivering standardized and efficient e-government services. Although
these frameworks were developed for the European context, they could serve as valuable models for similar
initiatives in other regions, including developing countries.
Based on EIF and The Open Group Architecture Framework (TOGAF), Schmitz and Wimmer [50] proposed a
new framework referred to as FISAD (Framework for Interoperable Service Architecture Development) and
validated in Germany. FISAD integrates the four layers of interoperability defined by the EIF (legal,
organizational, semantic, and technical) with the architectural design phases from TOGAF. FISAD is not an
independent framework in the sense that it builds on and combines elements from these established frameworks
to provide a structured approach for designing interoperable public service architectures.
Government interoperability and data exchange platforms (GIDEPs) for successful digital government
initiatives (such as EU's GAIA-X [51] and Estonia's X-Road [52]) are essential for facilitating seamless data
exchange across different governmental bodies enhancing the efficiency and effectiveness of public services [53].
The authors analyze GIDEPs across twenty countries and provide insights into the architecture, governance, and
future directions of digital government interoperability frameworks [53]. However, the results and insights from
the study on GIDEPs may have limited generalizability to developing countries due to different technological,
administrative, and financial resources. Government interoperability platforms like GAIA-X and Estonia’s X-Road
reflect higher levels of digital infrastructure and governmental coordination that might not be present in
developing nations.
The U.S. National Information Exchange Model (NIEM) is a framework designed to facilitate efficient and
standardized information sharing across diverse organizations, including local, state, and federal agencies [54]. It
enables interoperability through a common vocabulary and structured data formats, ensuring that information is
universally understood and usable. NIEM utilizes an ontology-based approach to define and organize data
elements in a way that they represent clear meanings in human and machine-readable formats. Still, NIEM is
developed specifically for the U.S. context and, therefore, might not be generalizable to other contexts.
The deployment of ontological frameworks, particularly using the Web Ontology Language (OWL),
significantly improves knowledge management and exchange among government departments [55]. This
facilitates clearer semantics and better system integration [55]. However, like other frameworks developed in the
context of high-income economies, e-government interoperability frameworks using semantic web technologies
and ontologies, such as an e-government business ontology (EG-BOnt) [56], a semantic web service-based
architecture for the interoperability of e-government services [57], the original Greek electronic government
interoperability framework/ontology [58] and its more recent modification [59], and primarily target issues and
scenarios relevant to developed countries, particularly those with advanced digital infrastructure and government
services [60].
The reviewed frameworks underscore the importance of a unified approach to enhance service delivery,
security, and collaboration across government agencies. While successful in the context of developed countries,
these frameworks might have limited applicability in other regions, particularly developing countries, due to
constraints in technological, financial, and administrative capacities. Nevertheless, these models provide valuable
lessons on the integration of legal, organizational, semantic, and technical interoperability layers.
2.2.2 Frameworks for E-government Interoperability in Developing Countries
There are several e-government interoperability frameworks implemented for and in the developing countries
context. The extended layered information security architecture (ELISA) for e-government in developing
countries is designed to enhance information security among e-government systems and not specifically
interoperability [28]. However, one of the goals of ELISA is to address the coherent flow of information across
various systems and entities, which is crucial for interoperability. By standardizing security practices and
compliance, ELISA enhances seamless and secure interaction among diverse government information systems,
addressing the challenge of fragmented e-government systems in developing countries that often lack uniform
security standards. ELISA was designed within the context of Benin, making it particularly relevant to the nation's
specific circumstances and challenges in the digital and security domains. Another potential barrier to the
adoption of ELISA for e-government interoperability is its primary focus on bolstering information security
within e-government systems. Improvements in interoperability, while beneficial, are incidental and result from
the standardization of security practices, rather than being a direct objective of the proposed architecture.
The e-government interoperability framework for DRC (GIF4DRC) based on service-oriented architecture
employs a microservices architecture to enhance G2G interoperability within the country’s public sector [29].
This architecture promotes the use of technical standards, a maturity model, and key actions to facilitate realworld implementation, tailored to meet the specific needs of developing countries. The framework aims to enable
seamless information exchange and enhanced service delivery across government departments, thereby
improving operational efficiency and public service quality. The framework’s strengths lie in providing a scalable,
flexible, and robust environment for seamless data and service integration across various government
departments, facilitating more efficient and effective public service delivery. However, the framework may
encounter challenges related to the existing legacy systems that lack integration capabilities, potentially leading to
significant implementation gaps if these older systems cannot be adequately modernized or replaced.
The electronic government systems interoperability model focuses on ensuring the successful integration of egovernment systems in Malaysia by addressing technical and non-technical factors [61]. Key components include
policy, legal issues, organizational structure, standards, and technical specifications. The study emphasizes the
importance of the roles of chief information officers and policymakers in facilitating interoperability. Strengths of
the model lie in its comprehensive approach, addressing multiple layers of governance and system integration;
however, it may face challenges in implementation due to potential resistance in aligning diverse government
agency standards and policies, as well as the complexity of coordinating across various administrative levels. The
generalizability of the proposed model may, however, be limited since it was specifically developed to address the
unique challenges of enhancing interoperability among e-government systems within Malaysia’s public sector
digital transformation agenda.
The two frameworks proposed by the same group of researchers, the public services ontology model for egovernment in Morocco (PSOM-eGovMa) [33] and the Morocco e-government interoperability framework [32],
differ significantly in their approach and focus. However, both frameworks aim to enhance interoperability within
Moroccan e-government systems. A public services ontology model for e-government in Morocco (PSOMeGovMa) utilizes the 5W1H method to systematically define and categorize the domain of public services,
addressing the ۔whoە, ۔whatە, ۔whenە, ۔whereە, ۔whyە, and ۔howە aspects to structure information
comprehensively [33]. The ontology includes various concepts and their relationships, based on standards from
the Moroccan Ministry of Administration Reform and Public Service, to enhance interoperability among
government entities. However, deployment may encounter challenges due to technical limitations or inconsistent
data standards across different agencies. Another gap in the proposed framework is that it was developed based
on the guidelines of a specific ministry in Morocco and, therefore, might not apply to other contexts.
The Morocco e-government interoperability framework was designed to enhance e-government
interoperability using a hyper-converged infrastructure (HCI), which integrates storage, computing, and network
functions to facilitate efficient public data management across various governmental agencies [32]. The
framework’s strengths include improved data collaboration and technical interoperability, alongside the flexibility
and scalability afforded by the HCI technology. However, the framework faces challenges such as the need for
significant investment in modernizing IT infrastructure, potential resistance to change from public agencies
accustomed to siloed operations, and the complexity of managing integrated services across diverse governmental
functions.
Apart from these two e-government interoperability frameworks proposed by the same group of authors, a
hybrid e-government framework based on data warehousing and multi-agent systems (MAS) was developed to
improve data interoperability for Morocco [62]. The framework incorporates business intelligence approaches and
uses ETL processes alongside multi-agent technology to enhance data quality, interoperability, and
transformation into human-readable formats. This framework is designed to support the extraction, analysis, and 
reporting of large volumes of data efficiently, emphasizing security and cost-effectiveness in public data
management.
The Philippine e-government interoperability framework (PeGIF) is designed to enhance the efficiency and
effectiveness of government services by enabling seamless data exchange and reuse among national government
agencies [39, 63]. The framework outlines three domains of interoperability − technical, information, and
business-process interoperability − with this document focusing specifically on technical interoperability, which
includes aspects like data integration, security, and system interfaces. Despite its comprehensive approach, the
PeGIF might face challenges related to consistent implementation across diverse agencies and ensuring all
stakeholders align with the evolving standards, which could impact the framework's effectiveness in achieving its
intended benefits.
An e-government interoperability framework (e-GIF) for South Africa aims to enhance public service delivery
through improved interoperability among government agencies [41]. The framework adopted international
models, namely, the EIF [46], the PeGIF [63], and the AGTIF [45], and tailored them to the local context. Its
components include policies, guidelines, standards, a conceptual model, various levels of interoperability,
governance mechanisms, and enterprise modeling to ensure effective and integrated public service delivery across
government entities. While the framework comprehensively addresses technical, semantic, and organizational
aspects of interoperability, its successful implementation may be challenged by the existing digital divide, varying
levels of IT infrastructure across agencies, and the need for significant alignment of political, legal, and
administrative domains.
The framework proposed in [64] emphasizes interoperability as a central component of E-Government 2.0,
which provides user-oriented portal services using Web 2.0 technologies like RSS, blogs, and social networks. It
ensures seamless integration across government agencies by enabling the exchange and mutual use of
information between disparate systems. The framework addresses interoperability through process and resource
integration, standardizing data management, and aligning government business processes. Additionally, it
highlights back-office and front-office integration to enhance data sharing and ensure consistent service delivery.
Although developed in Taiwan, the framework was validated in Korea, Antigua and Barbuda, and Ecuador, with
two of these countries classified as developing, justifying its inclusion under developing countries.
Tanzania's integrated e-government services framework aims to enhance data exchange and streamline service
delivery across public institutions [36]. The framework's components include the harmonization of project plans
among public institutions, a unified communication network, and a comprehensive e-government service catalog.
However, the paper identifies significant gaps such as inconsistent ICT policies and a lack of infrastructure, which
could hinder the effective implementation of the framework, despite its potential strengths in centralizing and
modernizing government service delivery.
Namagembe et al. [65] propose an e-government enterprise architecture framework (EGEAF) for developing
economies. The study emphasizes a methodological approach to achieve interoperability among e-government
systems. EGEAF integrates enterprise architecture principles with specific adaptations to address the unique
challenges of developing countries, such as unreliable infrastructure, limited resources, and diverse regulatory
environments. The framework focuses on defining a clear strategic context, ensuring comprehensive stakeholder
involvement, and achieving technical, semantic, and organizational interoperability within and across government
entities to support coherent and sustainable e-government implementations. While the framework could
potentially be adapted for use in other developing economies, its initial instantiation and the detailed
methodological approach are directly aligned with the situational needs and strategic goals of Uganda's egovernment efforts.
Overall, in the landscape of e-government interoperability frameworks for developing countries, key gaps
persist across various implementations. These frameworks often encounter challenges related to integration with
legacy systems, which may lack the necessary capabilities to support new interoperable technologies.
Furthermore, inconsistent ICT policies and insufficient infrastructural support hinder the effective deployment
and scaling of these frameworks. Additionally, the specific regional and administrative contexts of different
countries can limit the applicability of a one-size-fits-all approach, necessitating more tailored solutions that
address local needs and conditions. These gaps underline the need for frameworks that not only bridge
technological divides but also align closely with the political, legal, and socio-economic contexts of the countries
they are intended to serve.
2.3 The Adopted Theoretical Framework
The Interoperability Practical Implementation Support (IPIS) framework [66-69] was adopted in this research as it
was found to be better than e-government interoperability frameworks for developing countries discussed in
Section 2.2. Firstly, unlike frameworks such as ELISA, which primarily focuses on information security [28], or the
eGIF4DRC, which emphasizes technical standards and microservices architecture [29], IPIS provides a
comprehensive set of tools that address the three dimensions of interoperability: business, semantic, and
technical. This comprehensive toolset not only ensures that various aspects of interoperability are covered but
also facilitates the practical implementation of interoperable systems within government settings. Secondly, IPIS
integrates interoperability repositories and a knowledge-based system, which is not commonly emphasized in
other frameworks like the Moroccan e-government frameworks [32, 33, 62] or the PeGIF [63]. These repositories
store reusable components such as business process models, data standards, and technical standards, while the
knowledge-based system provides access to best practices, ontological concepts, and related frameworks. This
integration significantly aids in reducing the time and effort required for implementing interoperability by
providing ready access to necessary tools and established practices. Finally, IPIS is designed with the flexibility to
adapt to the specific needs and conditions of the implementing government. This adaptability makes it potentially
more effective compared to other models that may be more rigid or less sensitive to local conditions, such as the
electronic government systems interoperability model in Malaysia [61], which may face challenges in aligning
with diverse government agency standards.
Although the original version of the IPIS focused specifically on e-government interoperability in the context
of Thailand [70], the subsequent studies [66-69] attempted to generalize the IPIS to other contexts. Still, a
successful adaptation of the IPIS would require modifications to align with the local context, regulatory
frameworks, and specific interoperability needs of countries or organizations. The IPIS addresses the challenges
and barriers to achieving e-government interoperability, emphasizing the inadequacy of simply adopting egovernment interoperability frameworks (e-GIFs) and enterprise architectures (EAs). The IPIS incorporates
business, semantic, and technical dimensions of interoperability. The IPIS consists of three integrated
components: a set of tools supporting business process modeling, semantic standardization, and technical
standards usage; an interoperability repository covering business processes, standardized data sets, XML schema,
web services, and technical standards; and a knowledge-based system integrating best practice cases, ontological
concepts, and related frameworks (Figure 1).
The IPIS is proposed as a practical solution for the design, development, and implementation of interoperable
systems in e-government. It highlights the bureaucratic challenges, compliance issues, capacity development, and
the need for appropriate metrics in implementing e-government interoperability, emphasizing the practicality of
the proposed IPIS approach to bridge the gap between GIFs and EA adoption. The IPIS was adopted in this
research as a theoretical framework.
2.4 Contribution of Current Research to Existing Knowledge on E-government
Interoperability
E-government interoperability challenges in developing countries include issues such as cyber threats, poor
system integration, inadequate ICT policies, and lack of infrastructure. These challenges affect the deployment
and functionality of e-government systems, leading to suboptimal utilization and reduced citizen trust. Solutions
proposed include adopting comprehensive architectures, microservices, advanced middleware solutions, and
integrating global standards like blockchain technology for improved interoperability. Persistent issues such as
data volume management, the neglect of semantics, and the need for enhanced communication infrastructures are
critical areas needing attention. Tailored solutions that consider the local contexts and specific needs of public
sectors in these countries are essential for overcoming these interoperability challenges. 
While Section 2, Related Work, discusses challenges and solutions to e-government interoperability in various
countries, our research specifically addresses the challenges faced by Botswana. This adds context-specific
insights to the existing body of knowledge.
The proposed e-government service-oriented interoperability framework (e-GSOIF) integrates service-oriented
architecture (SOA), event-driven architecture (EDA), ontologies, a refined software development lifecycle
methodology, and the interoperability practical implementation support (IPIS) approach. This comprehensive
approach to addressing interoperability challenges adds a new dimension to the academic discourse on egovernment interoperability.
The research builds upon the concept of interoperability practical implementation support (IPIS) and extends it
by incorporating it into the e-GSOIF framework. This practical approach to implementing interoperable systems
in e-government adds value to the academic literature by providing a tangible solution to a common challenge.
The research includes an evaluation of the proposed framework against the original IPIS framework using
exploratory factor analysis and compatibility assessment with predefined functionality criteria. The evaluation
adds credibility to the proposed framework and contributes to the academic literature by providing a
methodological approach to framework comparison.
The additional academic value of this research is in its contribution to the theoretical and practical
understanding of e-government interoperability in developing countries. It offers a context-specific framework for
addressing interoperability challenges, provides a practical approach to implementation, and sets a precedent for
evaluating and comparing interoperability frameworks in the academic literature.
3 Research Methodology
3.1 Adoption of the Theoretical Model
The theoretical model employed in this study was the interoperability practical implementation support (IPIS)
framework adopted from [66-69]. The study used the IPIS framework in Figure 1 as a theoretical foundation by
using measurements and analysis as closely as possible in terms of reliability, validity, correlations, factor
analysis, and structural equation modeling. In this study, some constructs from the adopted model were removed,
and some were added to suit the developing country context.
Table 1 presents the factors impacting the e-government system interoperability under investigation in this
study.
The IPIS framework, emphasizing technical and organizational integration, guided the formulation of the
interview and survey questions. The study investigated influential factors of information exchange and egovernment system implementation based on the IPIS framework [66-69]. The questions were designed to
uncover standards for e-government, assess process automation, evaluate interdepartmental communication,
gauge leadership support for ICT, and measure user satisfaction. These inquiries aligned with the IPIS
framework’s focus on business process models, e-services, and interoperability. The study also utilized the core
components technical specification (CCTS) model to describe data models and information exchange [71]. Data
collected from the questionnaires and interviews provided insights into technological factors shaping egovernment implementation in Botswana, ensuring a theoretical alignment.
3.2 Case Study Approach
A case study is a research method that involves an in-depth analysis of a specific situation, organization, event, or
phenomenon within its real-life context [72]. This methodology facilitates an in-depth understanding of local
challenges and practical solutions, demonstrating the efficacy of case studies in applied research contexts [72].
This research adopted the case study approach to explore and document the challenges of developing a serviceoriented interoperability framework for Botswana's e-government systems. In our study, we utilized the case
study approach by conducting a detailed examination of the Botswana e-government systems. This involved
collecting qualitative data through interviews, questionnaires, and observations of government departments and 
their operations. According to Hancock and Algozzine [73], qualitative data collection methods such as interviews
and observations are integral to case study research as they provide rich, contextual insights. Additionally,
quantitative data was gathered and analyzed using exploratory factor analysis and compatibility assessments [74].
The methods of data collection and analysis for the case study of Botswana’s e-government systems are discussed
in Sections 3.5-3.6. 
The case study approach allowed us to gain a comprehensive understanding of the technological integration
challenges, organizational dynamics, and system interactions within Botswana's e-government systems. By
focusing on the specific context of Botswana, we were able to develop a tailored e-government service-oriented
interoperability framework (e-GSOIF) that addresses the unique conditions and factors affecting e-government
interoperability in the country.
Overall, the case study methodology was employed to explore the complexities of the Botswana e-government
system, providing a detailed and context-specific analysis that informed the development of the proposed
interoperability framework. 
Table 1: Factors affecting e-government system interoperability
Factor Description
Necessary ICT infrastructures (NICT) Availability of essential ICT infrastructure in government departments
Short network downtimes (NDT) Frequency and duration of network downtimes in departments
ICT skills of employees (HITS) Level of ICT skills among employees in the department
Computer communication (CC) The ability of computers to communicate with other computers inside and outside
the department/organization
Experience with network-based applications (SE) Employees' experience with network-based applications
Flexibility of existing systems (ESF) Adaptability and flexibility of existing systems in the department/organization
Data sharing policy (DS) The existence of a policy on data sharing within the organization
Coordination with other organizations (CD) Level of coordination with other organizations
Implementation guidance (GD) Availability of guidance for e-government system implementation
Secure identification and authentication (SC) Presence of secure mechanisms for identification and authentication
Data and technical standards (SDD) Existence of data and technical standards
Political support (PS) Political support for e-government interoperability
IT personnel experience (EXP) Experience of IT personnel in system implementation
Strong organizational leadership (SL) Presence of strong organizational leadership
Decision-making authority (DM) Assignment of decision-making authority to all activities in the organization
3.3 Research Design
The graphical representation of the research design for exploring and documenting the development and
implementation of a service-oriented interoperability framework within the Botswana e-government system case
study is shown in Figure 2. 
In the first step, theoretical model adoption, the interoperability practical implementation support (IPIS)
framework was adopted as the theoretical foundation of research. This framework was adapted to fit the
developing country context by adding and removing certain constructs. The second step involved the target 
population and sample size selection in six districts of Botswana with implemented e-government systems.
Participants included employees from various government organizations, categorized as either expert or nonexpert users. In the third step, data collection, the following methods were employed: questionnaires,
observations, and in-depth interviews. The fourth step, data analysis, was performed using descriptive statistics,
structural equation modeling (SEM), regression analysis, and thematic analysis. The fifth step, development of the
e-GSOIF, was performed through a structured process, which included (1) reviewing literature and conducting
preliminary interviews, (2) establishing the current state of e-government implementation in Botswana, (3)
identifying questions for data collection from experts and non-experts, (4) capturing the state of service
orientation in government departments, (5) utilizing event-driven architecture (EDA) to capture real-time
processes in e-government systems, and (5) testing the framework's measuring and testing capabilities. In the final
step, the evaluation of frameworks, the original IPIS, and the proposed e-GSOIF frameworks were evaluated based
on predefined functionality criteria and compared using exploratory factor analysis (EFA).
3.4 Selection of the Target Population and Sampling Methods
The study was conducted in Botswana in six districts with implemented e-government systems (out of the total
ten). These six districts included South, South-East, Central, North, North-East, and Kgalagadi. Each of these
districts had adopted specific e-government systems, and the study aimed to assess the effectiveness and
challenges associated with their implementation.
The target organizations for this study comprised Central Medical Stores (CMS), the Public Procurement and
Asset Disposal Board (PPDAB), the Ministry of Finance and Economic Development (MoFED), the Ministry of
Health and Wellness (MoHW), the Attorney General Chambers, the Department of Road Transport and Safety,
and selected hospitals.
Participants in this study were employees from the aforementioned organizations, categorized as either expert
or non-expert users. The distinction between these user classes was crucial for understanding their roles and
perspectives in the evaluation of e-government systems. In this context, expert users referred to ICT personnel
responsible for the development, implementation, and management of both the front and back ends of the egovernment systems. Non-expert users included nurses, doctors, organizational managers, and accountants who
used the e-government systems but lacked implementation expertise. Some non-expert participants had access to
the back end of e-government systems. This access allowed them to provide insights into the reasons for failures
in both the front and back ends of the system implementation. The inclusion of non-expert users with back-end
access provided additional perspectives to the study, contributing to a comprehensive assessment of egovernment system effectiveness.
The sampling method for this survey research combined both probability and non-probability sampling
techniques. For probability sampling, we used a combination of simple random sampling and cluster sampling. In
simple random sampling, every member of the target population has an equal chance of being selected for the
study. This method ensures that the sample is representative of the entire population. The sample size for the data
collection using questionnaires was calculated using the formula [75]:



 (1)
where n is the sample size, N is the population size, and e is the level of precision with a 95% confidence level (±5%
precision). In this research, the sample size was 410.
For non-probability sampling, we used convenience sampling to gather information from public sector
employees. This method is often used when it is not feasible to use random sampling, but it may introduce bias as
not all members of the population have an equal chance of being selected. In this method, participants are selected
based on their availability and willingness to participate, rather than using a random selection process. Managers
were selected through purposive sampling based on their competency to answer the interview questions and
identify the main factors affecting e-government system implementation.
By combining these methods, we balanced representativeness and practicality in our sampling strategy. 
3.5 Data Collection
The ethical approval and research permits were obtained from the Human Research Ethics Committee in
Botswana's Ministry of Tertiary Education, Research, Science and Technology (reference: MOTE1/18/6 VII (48)) on
September 23, 2019. Permissions to conduct the study were also granted by district health management teams in
each district where the study was conducted. The data for this case study was collected from October 2019 to
April 2020 from 410 participants, aged 20 to 65, across six districts in Botswana both in urban and rural settings.
Participants were mostly contacted through formal mechanisms such as official requests to selected organizations
and direct emails. Researchers visited workplaces and used referrals within departments to recruit a diverse range
of participants, including both expert and non-expert users. The data collection was conducted on both weekdays
and weekends to capture participant routine variations.
Before participation, all participants received detailed information about the study’s objectives, procedures,
potential risks, and benefits. Informed consent was obtained, ensuring participants' voluntary involvement and
awareness of their rights. To protect privacy, strict confidentiality measures were enforced; no personal
identifying information was collected, with data access restricted to authorized personnel. Demographic data such
as age, gender, educational background, and employment status were gathered, aiming for a diverse
representation to enhance the generalizability of the findings within the context of the case study.
The data collection process employed in this case study utilized a combination of questionnaires, interviews,
and observation methods to ensure a comprehensive exploration of the e-government system implementation.
Surveys and interviews were conducted using participatory methods, where participants actively contributed
firsthand experiences, opinions, behaviors, and other relevant data to the study. These participatory techniques
were essential for directly engaging with subjects and obtaining rich contextual insights.
During observations, the researcher employed non-participatory (non-intrusive) methods. This approach
involved observing and collecting information from the environment without interacting with individuals. By not
intervening, the researcher could unbiasedly assess real-time interactions within organizations as complex
sociotechnical systems. This non-participatory observation was crucial for understanding the dynamic and
interconnected nature of these systems, providing a clear view of their operational realities.
The justification for the selection of methods of data collection is provided in Subsections 3.5.1-3.5.3.
3.5.1 Questionnaires: Gathering Insights on E-government System Implementation
The study employed questionnaires, administered to employees across various organizations and departments as
outlined in Subsection 3.4, with a total of 410 questionnaires distributed. The justification for selecting
questionnaires as the data collection tool was driven by the need to gather detailed insights from employees
responsible for coordinating and communicating e-government information exchanges. These individuals were
pivotal in understanding the interdepartmental and environmental influences that affected daily operations and
information processing within their respective departments. The data obtained from the questionnaires were
crucial in identifying and formulating variables essential for evaluating factors impacting the implementation of
e-government systems in Botswana. The design of the survey questions allowed respondents to express their
personal opinions, providing us with a nuanced understanding of the issues under investigation. Moreover, a 5-
point Likert scale was used to measure the attitudes and opinions of the participants, mapping the views of
experts across a range of attitudes from "strongly disagree" to "strongly agree." This approach enabled us to
compile rated and aggregated qualitative data, enhancing the depth and breadth of the analysis within the case
study.
3.5.2 Interviews: Deepening Understanding of E-government System Implementation
Interviews were selected as a data collection method due to their ability to facilitate direct communication with
government officials across various departments, providing first-hand information on the systems utilized within
organizations. This method enabled an in-depth analysis of not only the technical aspects but also the emotional,
cue-based, and preferential dimensions that written surveys might overlook. Furthermore, the interactive nature
of interviews allowed the researcher to seek clarifications, probe deeper with follow-up questions, and adapt the 
interview guide dynamically, which was instrumental in identifying behavior patterns associated with the
runtime environment within the case study.
In-depth interviews were conducted with participants in management roles to ensure data saturation, a key
goal in qualitative research, as per the recommendations in [76]. The total number of interviewees was 323,
although the saturation point (where no new information was obtained) was reached before all interviews were
completed. Engaging with top management was critical as they could provide a clearer perspective on
organizational structures and processes, significantly differing from insights that might be gathered from lowerlevel employees, as outlined in [73]. This approach not only enriched the understanding of e-government system
implementation and interoperability but also ensured a comprehensive exploration of its technical, organizational,
and semantic dimensions within the case study context.
The interviews focused on identifying technical standards aligned with interoperability requirements and
discovering repositories for reusable components such as schema and technical standards. The interview method
facilitated the identification of common goals for data exchange and the establishment of technical standards,
crucial for advancing e-government systems in Botswana as part of the case study.
3.5.3 Observations: Capturing Real-time Operational Dynamics
The utilization of observational methods as data collection instruments was justified by the necessity to gather
firsthand information directly from the daily operations within government environments. Observation is a
scientific method to directly capture real-time interactions within complex sociotechnical systems, playing a
crucial role in understanding the dynamic and interconnected nature of these systems [77]. Observation enables
researchers to deeply understand actual practices and challenges in the field, revealing the gap between
theoretical ideals and practical realities [78]. Observation uncovers the nuances and complexities of daily
operations, offering insights into systemic and environmental factors and highlighting areas for improvement
within the case study.
Being in government offices allowed the researcher to observe how computers and resources were used within
and between departments. Such observations allowed capturing non-verbal cues, group dynamics, and
environmental factors that significantly influenced behaviors but might not be fully noticeable through interviews
or questionnaires.
Observational data is particularly effective in documenting spontaneous interactions and behaviors, providing
a real-time, comprehensive view of the operational context [79]. This method allowed us to understand details of
system communications, response times, downtime, and the overall run environment, offering insights into the
efficacy of interoperable environments within the case study.
Using an observational approach helped in an in-depth analysis of the actual state of e-government system
implementation within government departments and hospitals. Direct observations verified the execution of daily
activities and the use of infrastructure, ensuring a representation of the operational realities, which was essential
for assessing the performance and challenges of e-government systems as part of this case study.
3.6 Data Analysis
Data analysis in this case study involved applying statistical and logical techniques to raw data to address the
research objective and question as recommended in [80]. All responses collected from different departments were
analyzed according to department type and environmental context, whether urban or rural. This analysis helped
identify the latent factors underlying the observed variables in the provided questionnaires. By examining the
patterns of runtime and downtime loadings on various factors, we gained a deeper understanding of the structure
of communication and interaction traits. Statistical data analysis in this study was employed to test theoretical
models; specifically, it was used to develop a model that elucidated how various factors, such as systems
communication traits and environmental factors, influenced systems development. The R programming
application was used to analyze the questionnaire data, leveraging its capacity to model latent variables for data
screening. 
3.6.1 Descriptive Statistics
Descriptive statistics are methods that involve summarizing and organizing the primary data so it can be easily
understood [81]. The purpose of descriptive statistics is to ensure that researchers have a solid understanding of
the data before proceeding to more complex analyses. It is important not to overlook these basic statistics despite
their simplicity [82]. In this study, descriptive statistics was used to derive quantitative insights into the factors
affecting e-government system interoperability. These statistics provide an understanding of the central tendency
and variability of each factor, contributing to an assessment of their distribution and potential impact on egovernment system interoperability in Botswana.
Descriptive statistics of the factors influencing interoperability included means and standard deviations, which
helped quantify the central tendencies and dispersions of responses about ICT infrastructure, network downtimes,
ICT skills among employees, computer communication capabilities, experience with network-based applications,
flexibility of existing systems, data sharing policies, coordination with other organizations, and several other
relevant variables. Furthermore, these statistics helped evaluate the state and effectiveness of e-government
systems, guiding improvements in system integration and interoperability. Additionally, the use of descriptive
statistics supports the research's conclusions by providing a numerical basis for the observations and claims made
about the effectiveness of the proposed e-GSOIF framework compared to the original IPIS framework, particularly
through the exploratory factor analysis.
3.6.2 Structural Equation Modeling (SEM) Analysis
Structural equation modeling (SEM) is a statistical technique used in research to analyze the relationships
between observed and latent variables. Hypotheses were tested through SEM to determine the support for the
proposed theoretical model using the collected data. A two-step method was implemented for structural equation
modeling (SEM) analysis. SEM was utilized to specify relations between constructs and assess relationships in the
e-GIF [74].
The first step involved connecting observed variables to latent variables through confirmatory factor analysis
(CFA) and exploratory factor analysis (EFA). CFA is a form of SEM that focuses specifically on the measurement
aspects of the structural model. The primary goal of EFA was to identify the latent factors that explain the
observed patterns of correlations among variables. In this research, CFA gauged the likelihood of the sample mean
representing the true population, while EFA systematically examined relationships one at a time, probing the
construct validity of the test scales [83].
The second step entailed constructing a structural model (SM) linking latent variables to other variables
through systems of simultaneous equations. The structural model specified the relationships between observed
variables (indicators) and latent variables (factors). It represented the hypothesized causal connections between
latent variables.
3.6.3 Regression Analysis of Participants’ Responses to Open-ended Questions
Regression analysis is a statistical method used to control for confounding in data analysis [84]. Confounding
refers to a situation in statistical analysis where a variable influences both the dependent and independent
variables, creating a misleading association. Regression analysis includes confounders as independent variables in
a regression equation.
In our research, regression analysis was conducted by transforming open-ended questions into variables, each
named with an abbreviation (Table 1) to explore relationships between variables and predict dependent values.
Participants' responses to these open-ended questions were analyzed using linear regression to determine the
effectiveness of various e-government tools and policies. Each application of regression analysis focused on
different aspects, such as practical tools, policies, factors affecting e-government implementation, and technical
guidelines required for successful e-government system implementation. Regression analysis assessed the
goodness of fit through the R-squared value for each question, indicating the percentage of variance explained by
the model and aimed to ensure it surpassed the acceptable threshold of 50%. This use of regression analysis
allowed for the examination of how different elements contributed to the implementation of e-government
systems, highlighting the importance of understanding specific needs for successful implementation. Results of 
regression analysis are not included in this paper due to word count limitations but are available in Figshare (see
Section 7 Additional Materials).
3.6.4 Thematic Analysis
Thematic analysis was employed to condense qualitative responses from participants. Patterns identified
throughout the study life cycle were used to characterize the current state of e-government system
implementation and interoperability, highlighting existing gaps. These patterns were thematically analyzed
through the lenses of e-government interoperability and SOA theories to inform the development of the egovernment service-oriented interoperability framework (e-GSOIF).
Data analysis involved sorting and filtering data for easier trend identification. The processed data was
organized using spreadsheets and then saved as a CSV file. Subsequently, the data was summarized and
aggregated to generalize the preserved chronological flow by analyzing the causal relationships between events
and deriving explanations. All responses collected from different departments were analyzed based on department
type and location (i.e., urban vs. rural).
3.7 The Preliminary Model for the Development of the e-GSOIF
The preliminary model for the development of the e-GSOIF integrates technical, semantic, and organizational
perspectives of the successful e-government implementation as demonstrated in Figure 3. The technical
perspective focuses on the technology side of data exchange and system implementation, the semantic perspective
− on integration communication (language understanding between systems and organizations), and the
organizational perspective − on organizational influences (culture and leadership participation).
Figure 3 illustrates the multi-dimensional factors influencing the success of interoperability implementation in
e-government systems. The central theme, interoperability implementation success, is depicted at the core,
surrounded by three main perspectives − technical, semantic, and organizational. Each perspective is detailed with
specific subfactors contributing to the overarching success, interconnected through directional arrows
emphasizing their integral roles. The preliminary model linking the three perspectives and the interoperability
implementation success was built based on the data collected using interviews, questionnaires, and observations,
complemented by the literature review.
3.8 Steps in the Development of the e-GSOIF
The development of the e-government service orientation interoperability framework (e-GSOIF) followed a
structured process of six steps, drawing insights from the CCTS model [71] and practical approaches outlined in
[66-69].
Step 1: To comprehend the landscape of e-government implementation, a comprehensive literature review was
conducted. This was complemented by preliminary interviews with leaders in governmental departments and
observation of daily activities within these departments. Department heads and managers were interviewed to
gain insights into the trajectory of e-government system implementation, while the observation method provided
data on daily operations.
Step 2: The current state of e-government implementation in Botswana was established by analyzing the
information gathered in Step 1. Candidate variables were identified through the literature review, preliminary
interviews, and observation. This data analysis facilitated an understanding of the existing state of e-government
systems, information, and data-sharing processes, and the implementation process in Botswana.
Step 3: Questions for data collection from e-government experts and non-experts were identified. Both
quantitative and qualitative questions were utilized to develop the framework. Qualitative questions were
embedded in interviews and questionnaires to ascertain variables related to e-government system implementation
and interoperability. Quantitative questions were used to collect demographic data and to identify experts capable
of providing reliable, informative, and competent responses for further interviews with them.
Step 4: The state of service orientation in government departments with e-government systems was captured,
guided by the service-oriented development lifecycle principles. The unified metadata model (UMM), based on 
UN/CEFACT standards, facilitated the depiction of organizational and business service relationships [85]. UMM
was instrumental in developing interoperable services for information exchange among organizations through the
proposed e-GSOIF. 
Step 5: Real-time processes in e-government systems were captured using an event-driven architecture (EDA).
EDA, designed to respond to system-generated actions, supported the processing of life events in integrated
systems.
Step 6: The proposed framework's measuring and testing capabilities were enabled by insights from the IPIS
[66-69]. Leveraging their model, the e-GSOIF was designed to ensure system reliability, compatibility, availability,
suitability, and data quality in e-government systems. This study introduced a model to test all five characteristics,
identifying types of documentation for each department and converting them to an XML format. Ontology
transformation was employed to convert these files into resource description framework (RDF) entities,
representing information exchange based on concepts, relationships, and rules.
4 Results
4.1 Factors Impacting E-government System Implementation in Botswana
This subsection presents the outcomes of an in-depth analysis focusing on the factors that significantly impact the
effective and efficient implementation of e-government systems in Botswana. The identification of critical factors
was accomplished through a comprehensive approach involving interviews, questionnaires, observations, and an
exhaustive examination of relevant literature.
Preliminary interviews with government department leaders, coupled with direct observations of their work
procedures, revealed a prevalent issue – most e-government systems were, at the time of the research, either
partially or completely unsuccessful. Subsequent interviews with managers and expert users underscored the
potential efficacy of EDA and SOA as viable solutions for enhancing e-government system implementation and 
services. To ensure clarity, interview questions regarding EDA, SOA, and other technical solutions were
simplified for a thorough understanding by respondents, with additional clarifications provided as needed.
The consensus from interviews identified EDA and SOA as optimal solutions for facilitating data exchange
among government organizations. Security, managed through the software development lifecycle (SDLC),
emerged as a critical variable, addressing authentication, authorization, and encryption of exchanged information
within government organizations.
The primary components of the proposed e-government system interoperability framework (e-GSOIF) were
deduced through a synthesis of interviews and questionnaires as follows:
(1) SOA and EDA − for enhanced service delivery and data exchange,
(2) ontologies − for representing information exchange within systems,
(3) refined SDLC methodology – for ensuring robust security measures, and
(4) IPIS approach − for guiding technical processes.
Descriptive statistics of the factors influencing interoperability are presented in Table 2, providing a
quantitative insight into the crucial elements affecting the successful implementation of interoperable egovernment systems.
Table 2: Descriptive statistics of factors affecting e-government system interoperability
Factors Variable
abbreviations
Mean Standard
deviation
Necessary ICT infrastructures in place NICT 2.80 1.068
Short network downtimes in departments NDT 2.29 1.493
Everyone in the department has ICT skills HITS 3.06 0.231
Computers communicate with other computers inside and outside
the department/organization
CC 3.00 1.166
Everyone in the department has sufficient experience with networkbased applications
SE 2.74 1.481
Existing systems in the department/organization are flexible ESF 3.21 0.694
There is a policy on data sharing in the organization DS 2.65 0.748
Coordination with other organizations CD 2.74 0.632
Guidance for e-government system implementation in place GD 2.81 0.649
Secure mechanisms for identification and authentication in place SC 2.78 0.649
Data and technical standards in place SDD 2.74 0.636
Political support for e-government interoperability PS 2.78 0.622
IT personnel have experience in system implementation EXP 2.79 0.653
Strong organizational leadership SL 0.56 0.497
Decision-making authority is assigned to all activities in the
organization
DM 2.53 1.638
These statistics offer an understanding of the central tendency and variability of each factor, contributing to an
assessment of their distribution and potential impact on e-government system interoperability. 
4.2 Essential Technical Components for E-Government Interoperability
A mixed-methods approach, including a detailed literature review, structured interviews with ICT managers,
survey questionnaires, and organizational observations, enabled this study to identify essential technical
components for effective e-government interoperability solutions. Responses and observations revealed minimal
knowledge about tools for implementing interoperability in government organizations. This gap emphasized the
necessity for better education and resources to improve e-government interoperability. The findings underscored
the need for practical tools, including (1) character sets, essential for establishing technical parameters, (2) web
service technologies to facilitate data interfacing, (3) RDF to define metadata, (4) metadata management tools to
manage and leverage policies, incorporating validation rules defined in standards, (5) web content formats
enabling semantic content, (6) document, image, audio formats to standardize various content types, (7)
compression technologies for optimized data transmission, (8) mobile device content formats to ensure
information accessibility on mobile devices, (8) transport protocols to ensure safe and reliable data
communication, (9) directory protocol, serving as a repository for resource information in distributed
environments, to locate data about organizations, (10) network protocols to manage data transmission rules
between devices in a network, allowing seamless communication despite differences in internal processes, and
(11) encryption algorithms to secure data transmission, maintaining privacy and confidentiality.
4.3 Proposed E-government Service-Oriented Interoperability Framework (e-GSOIF)
The structural equation modeling (SEM) analysis was conducted utilizing the 'semPlot' and 'fa()' packages within
the R programming application. This approach aimed to discern the multivariate relationships among factors
influencing e-government system implementations. The SEM output for the proposed framework is illustrated in
Figure 4. 
Figure 4 illustrates the exploratory path and t-test for the model. Drawing on insights from [74] and [86], a
crucial criterion is that R should surpass 0.1, demonstrating a positive impact of a construct. In our study, all
values exceeded 0.1, affirming that every construct positively influenced e-government system implementation.
The devised e-GSOIF framework targets enhancing interoperability among government departments within
the Botswana context. Semantic interoperability assists in seamlessly interacting with user interface segments,
leveraging semantics and interoperability for data exchange through self-described information packages. The 
steps in the development of the e-GSOIF framework were outlined in Subsection 3.8. Figure 5 provides a detailed
depiction of the developed e-government service-oriented interoperability framework and its constituent layers.
 Case
The framework consists of five layers: (1) the management layer, (2) the service layer, (3) the platform layer, (4)
the trust and content layer, and (5) the inventory layer. In addition to technical, organizational, and semantic
perspectives, the e-GSOIF also supports service orientation and trust perspectives. 
4.4 Results of Comparative Analysis of the Original and Proposed Frameworks
This research involved a comparative analysis of two frameworks: the original IPIS framework by Saekow and coauthors [66-69] (Figure 1), and the e-GSOIF developed in this study (Figure 5). While the e-GSOIF integrated 
certain elements from IPIS, such as guidance on technical processes, it introduced distinct components derived
from data collected through questionnaires, interviews, and observations.
Cronbach's alpha coefficient was calculated to evaluate the reliability of test items and to ensure that they
measured the same construct. Pearson's correlation coefficient (r) was used to measure the relationship between
the original IPIS framework and the proposed e-GSOIF. This statistical measure helped quantify how closely the
components of the two frameworks were related, which was essential for evaluating compatibility. Exploratory
factor analysis (EFA) and confirmatory factor analysis (CFA) were conducted using the R programming language
and the 'psych' package to assess the quality differences between the two frameworks. The results of the
comparative analysis are presented in Table 3.
Table 3. Results of comparative analysis between IPIS and e-GSOIF frameworks
Metrics/Indices IPIS framework e-GSOIF
framework Remarks
Cronbach's alpha
coefficient 0.75 0.88 e-GSOIF shows higher reliability in internal consistency
Pearson correlation
coefficient (r) 0.65 0.85 e-GSOIF exhibits stronger correlations among its factors
EFA: Factor reliability 0.65 0.85 e-GSOIF shows higher reliability in internal consistency
CFA: AIC 853.684 758.684 Lower AIC indicates a better fit for e-GSOIF
CFA: BIC 896.708 786.708 Lower BIC indicates a better fit for e-GSOIF
CFA: CFI 0.798 0.978 CFI ߖ 0.95 indicates a good fit; e-GSOIF shows better fit
CFA: GFI 0.831 0.920 GFI ߖ 0.90 indicates a good fit; e-GSOIF shows a better fit
CFA: SRMSR 0.093 0.053
SRMSR ߕ 0.08 indicates a good fit; e-GSOIF shows a better
fit
CFA: RMSEA 0.060 0.050
RMSEA ߕ 0.05 indicates a good fit; e-GSOIF shows a
better fit
P-value <0.001 <0.001 Both frameworks show strong statistical significance
Number of variables 60 60
An equal number of variables is used for a balanced
comparison
Explanation of the abbreviated metrics
Metric Full name What it measures Interpretation
AIC Akaike Information Criterion
[87], [88]
The relative quality of statistical models for a
given dataset
Lower values indicate a better model
fit
BIC Bayesian Information Criterion
[89], [90]
Model selection among a finite set of models Lower values indicate a better model
fit
CFI Comparative Fit Index [91], [92] Fit of a user-specified model compared to a
baseline model
Values closer to 1 indicate a better fit
GFI Goodness of Fit Index [93] How well a model fits the observed data Values closer to 1 indicate a better fit
SRMSR Standardized Root Mean Square
Residual [92], [94]
Standardized difference between observed
and predicted correlations
Values less than 0.08 indicate a good
fit
RMSEA Root Mean Square Error of
Approximation [95], [96]
Fit of a model to the population covariance
matrix
Values less than 0.05 indicate a close
fit; up to 0.08 is acceptable 
The comparative analysis between the IPIS and e-GSOIF frameworks, as detailed in Table 3, supports the
enhanced performance and reliability of the e-GSOIF framework over its IPIS counterpart. Key metrics such as
Cronbach's alpha coefficient, Pearson correlation coefficient, and exploratory factor analysis all favor the e-GSOIF
framework, highlighting its superior internal consistency and stronger inter-factor correlations. These attributes
suggest that e-GSOIF is more robust in capturing and reflecting consistent patterns among variables, thus
providing a more reliable framework. Additionally, the statistical significance of these findings is underscored by
p-values below the 0.005 threshold. The structural model analysis, including both EFA and CFA, supports the
enhanced performance and reliability of the proposed e-GSOIF framework over the adopted IPIS framework. The
proposed e-GSOIF framework demonstrates higher factor reliability and better-fit indices, suggesting it is more
robust and suitable for supporting effective interoperability and integration in e-government initiatives. This
comprehensive evaluation, maintaining an equal number of variables across both frameworks to ensure a fair
comparison, conclusively demonstrates that the e-GSOIF framework is better equipped to support effective
interoperability and integration in e-government initiatives.
4.5 Results of Evaluation of the Original and Proposed Frameworks Based on Desired
Functionality Criteria
The evaluation of the original IPIS and the proposed e-GSOIF frameworks was conducted based on seven criteria
representing the desired functionality of a successful e-GIF framework. These criteria are as follows:
 Support for SOA
 Support for EDA
 Availability of built-in functions
 Utilizing interoperability
 Compliance with up-to-date standards and tools
 Low levels of complexity and redundancy
 Defined modeling language, testability, and variability
Table 4 presents the results of the evaluation, comparing the compatibility of criteria for both frameworks
across theoretical, organizational, and technical perspectives.
Table 4: Comparison of the compatibility of criteria for the original and proposed frameworks 
In Table 4, a score of 1 denotes that the framework is incompatible with the criterion under theoretical,
organizational, and technical perspectives, while a score of 0 signifies compatibility. The original IPIS framework
showed incompatibility with 14 out of the seven criteria considered across the three perspectives (total of 21). In
contrast, the proposed e-GSOIF framework received a score of 0 for all criteria under all perspectives, indicating
compatibility with the proposed framework. 
5 Discussion
5.1 Comparison of the Proposed e-GSOIF Framework with the Original IPIS Framework
In addition to the evaluation of the proposed e-GSOIF and the original IPIS frameworks based on the criteria
representing the desired functionality of a successful e-GIF framework, the two frameworks were compared in
terms of technology and methodology integration, focus on local challenges, methodological approach, and
evaluation and adaptability as demonstrated in Table 5.
Table 5. Comparison of the IPIS framework and e-GSOIF framework in addressing e-government interoperability challenges
Category IPIS Framework e-GSOIF Framework
Technology and
methodology
integration
Focuses on providing tools that address
business, semantic, and technical dimensions
of interoperability. Integrates interoperability
repositories and a knowledge-based system
Incorporates service-oriented architecture (SOA), event-driven
architecture (EDA), ontologies, a refined software development lifecycle
methodology, and the IPIS approach. Aims to comprehensively address
the interoperability challenges in Botswana, providing a holistic solution
for the country
Focus on local
challenges
Generally applicable and designed to be
adaptable to various contexts, but may not
address all specific local challenges without
customization
Specifically targets the challenges in Botswana's e-government systems,
such as lack of communication and integration among systems.
Customized to the local context, reflecting a deep understanding of
specific issues including technological limitations and the need for robust
data exchange mechanisms
Methodological
approach
Uses a standardized approach that could be
implemented in various governmental settings
but might require adjustments to align with
local needs
Developed through a methodology involving interviews, questionnaires,
and observations. Tailored more precisely to the needs identified in
Botswana, ensuring practical applicability and theoretical soundness in
the local context
Evaluation and
adaptability
Evaluated through general interoperability
criteria and could require specific
modifications to fit into particular
environments
Evaluated against the original IPIS framework using exploratory factor
analysis and compatibility assessment with predefined functionality
criteria. Demonstrates superiority in the context of Botswana, suggesting
enhanced adaptability and effectiveness for local challenges
As compared to the original IPIS, the e-GSOIF framework incorporates a broader set of technologies and
methodologies tailored to address the specific interoperability challenges of Botswana. Its development and
evaluation are grounded in an understanding of local conditions, making it a potentially more effective tool for
improving e-government service delivery in regions facing similar challenges. This tailored approach contrasts
with the general applicability of the IPIS, highlighting the importance of context-specific adaptations in the
development of e-government frameworks.
5.2 Comparison of the Proposed e-GSOIF Framework with the Other E-government
Interoperability Frameworks
Furthermore, the proposed framework was compared with e-government interoperability frameworks proposed
in similar existing studies in terms of integration features, strengths, and limitations as demonstrated in Table 5.
The difference in criteria used in Tables 5 and 6 reflect distinct analytical focuses for each set of comparisons. In
Table 5, the comparison with the IPIS framework focuses on conceptual alignment, while in Table 6, the practical
applicability of the frameworks is examined.
The comparative analysis presented in Table 6 demonstrates the better integration and adaptability of the eGSOIF when matched against existing e-government interoperability frameworks from both developed and
developing countries. The e-GSOIF's incorporation of SOA, EDA, and localized customization provides a robust
solution specifically tailored to Botswana's needs, addressing challenges such as security, data management, and
system integration in a more comprehensive manner than other frameworks. This adaptability, combined with the
e-GSOIF's holistic approach, makes it a suitable tool for enhancing the interoperability of e-government services
in Botswana, paving the way for improved governmental efficiency and service delivery in similar contexts
worldwide. 
6 Conclusion and Future Work
6.1 Summary of Research Findings
This research explored and documented the process of development of the e-government service-oriented
interoperability framework (e-GSOIF) to address the specific interoperability challenges faced by Botswana's egovernment systems. The framework integrates service-oriented architecture (SOA), event-driven architecture
(EDA), ontologies, a refined software development lifecycle methodology, and the interoperability practical
implementation support (IPIS) approach.
Table 6: Comparison of e-government interoperability frameworks with the e-GSOIF by assessing integration features,
strengths, and imitations
Framework Integration features Strengths Limitations Comparison with e-GSOIF
Developed countries
Australian
Government Technical
Interoperability
Framework (AGTIF)
[45]
Fosters a unified approach
to technical
interoperability; principles
for collaboration
Enhances security,
supports efficient public
service delivery
Potential inconsistencies
due to different agency
capabilities
e-GSOIF offers broader integration,
including SOA and EDA, not just
technical aspects
European
interoperability
framework (EIF) [46]
Principles for legal,
organizational, semantic,
and technical
interoperability
Enhances service delivery
across EU borders
Developed for European
context; may not directly
apply to other contexts
e-GSOIF similarly integrates
multiple layers but is tailored to
Botswana
Framework for
Interoperable Service
Architecture
Development (FISAD)
[50]
Focuses on integrating
pre-award procurement
procedures through
modular architecture;
includes ESPD and
Dynamic Purchasing
Systems (DPS)
Promotes flexibility, reuse
of existing components,
and a holistic approach to
service integration
The framework is
conceptual, lacks practical
maturity and real-world
testing; focuses on
architectural design
without concrete
implementation guidance
e-GSOIF focuses more broadly on
government interoperability
beyond procurement, while FISAD
emphasizes procurement-specific
solutions
U.S. National
Information Exchange
Model (NIEM) [54]
Uses common vocabulary
and structured data
formats for
interoperability
Ensures universally
understood and usable
information
Primarily developed for
the U.S.; may not be
generalizable
e-GSOIF includes similar data
standards but emphasizes local
adaptation
Developing Countries
Extended layered
information security
architecture (ELISA)
[28]
Enhances information
security; addresses the
flow of information for
interoperability
Security-focused,
enhances secure
interaction among
government systems
Primarily securityfocused; interoperability
improvements are
incidental
e-GSOIF offers a more holistic
approach to interoperability
beyond security
E-government
interoperability
framework for DRC
based on serviceoriented architecture
(eGIF4DRC) [29]
Microservices
architecture; promotes
technical standards and
maturity models
Scalable, flexible, and
robust for data/service
integration
Challenges with legacy
systems; specific to the
DRC's context
e-GSOIF is more comprehensive in
integrating various architectures
and methodologies
Malaysian egovernment systems
interoperability model
[61]
Addresses technical and
non-technical factors
including policy and legal
issues
Comprehensive, addresses
multiple layers of
governance
Potential resistance from
agencies, complexity in
coordination
e-GSOIF similarly addresses
multiple layers but is specifically
tailored to Botswana
Public services
ontology model for
Morocco (PSOMUtilizes the 5W1H method
to define public service
Structured approach to
enhancing interoperability
May face technical
limitations; specific to
Moroccan ministry
e-GSOIF uses a broader integration
of global standards and local 
Framework Integration features Strengths Limitations Comparison with e-GSOIF
eGovMa) [33] domains among entities guidelines customization
Morocco egovernment
interoperability
framework using HCI
[32]
Integrates storage,
computing, and network
functions for data
management
Improved data
collaboration and
technical interoperability;
scalable
Significant investment is
needed; resistance to
change from siloed
operations
e-GSOIF provides a similar level of
technical integration but with
specific local adaptations
Hybrid e-government
framework (Morocco)
[62]
Incorporates business
intelligence approaches
with data warehousing
and multi-agent systems
(MAS); uses ETL
processes for data
integration
Enhances data quality and
interoperability, and
supports large volumes of
data management
efficiently. Emphasizes
security and costeffectiveness
May face technical and
adoption challenges due to
the complexity of
integrating data
warehousing and MAS in
existing systems
e-GSOIF offers a broader approach
with its service-oriented and
event-driven architectures for
general interoperability while this
framework emphasizes data
management and business
intelligence, enhancing
interoperability within Morocco's
public data sector
Philippine egovernment
interoperability
framework (PeGIF)
[63]
Focuses on technical,
information, and businessprocess interoperability
Comprehensive data
exchange and reuse
among government
agencies
Implementation
consistency challenges;
evolving standards
alignment required
e-GSOIF offers similar breadth but
is enhanced by local contextual
adaptation specific to Botswana
An implementation
framework for EGovernment 2.0 [64]
Process, resource, backoffice, and front-office
integration; supports Web
2.0 technologies for
stakeholder participation
Encourages participatory
governance, promotes
efficiency, collaboration,
accountability, and
transparency
High technical and
resource demands;
complexity in
coordination across
different agencies
The framework provides a broader
participatory governance approach
but may be less specific in
technical integration than the eGSOIF. It emphasizes social and
organizational aspects alongside
interoperability
South African egovernment
interoperability
framework [41]
Integrates international
models to local context;
covers all interoperability
layers
Comprehensive
integration of services
across agencies
Challenges with the digital
divide and varying IT
infrastructure levels
e-GSOIF is similarly
comprehensive but provides more
specific solutions for Botswana
Tanzania's integrated
e-government services
framework [36]
Focuses on harmonizing
project plans and
establishing a unified
network
Aims to streamline service
delivery across public
institutions
Inconsistent ICT policies
and a lack of
infrastructure might
hinder effective
implementation
e-GSOIF addresses similar
integration challenges with
tailored local strategies
Ugandan egovernment enterprise
architecture
framework (EGEAF)
[65]
Integrates enterprise
architecture principles;
adapted to the unique
challenges of developing
countries
Ensures stakeholder
involvement and
addresses regulatory
environments
Requires significant
adaptation to local needs;
focuses on developing
economies' challenges
e-GSOIF shares the methodological
thoroughness but is further
tailored specifically to Botswana's
interoperability needs
Statistical analysis of factors such as ICT infrastructure, network downtimes, ICT skills, system flexibility, and
data-sharing policies provided a quantitative understanding of the challenges and potential impact on system
interoperability. The study also identified essential technical components for effective e-government
interoperability, including character sets, web service technologies, RDF, metadata management tools, web
content formats, and encryption algorithms.
The e-GSOIF framework, evaluated against established benchmarks, demonstrated its potential to enhance
communication and data exchange among government entities. This case study provides practical guidance for
government officials and IT specialists to improve service delivery and system integration. It also offers insights
for researchers and students into the complexities of e-government interoperability in developing countries. 
In summary, this case study enhances the practical understanding of e-government interoperability and
provides actionable solutions for improving governmental service delivery in Botswana and potentially other
developing countries.
6.2 Practical Implications of the Proposed e-GSOIF Framework
This paper provides a framework that can assist in addressing interoperability challenges faced by e-government
systems, particularly in developing countries like Botswana. The proposed framework offers practical applications
that could improve system integration, efficiency, and public service delivery in various ways.
First, government agencies can use this framework to enhance system interoperability by improving
communication between different departments and services. This ensures smoother data exchange, reducing
duplication of efforts and enabling a more unified approach to service delivery. The application of the framework
can support more coordinated public services, leading to faster and more accurate responses to citizens' needs.
Second, the framework can be applied to modernize and streamline government operations, allowing for the
integration of legacy systems with newer technologies. This would help government departments to maintain
their existing systems while incorporating new advancements, ensuring that services remain up-to-date and
scalable. As a result, the framework can assist governments in implementing digital transformation initiatives
more effectively.
Third, the framework can help decision-makers in setting strategic IT goals for public sector projects. IT
managers can apply it to guide the planning and execution of e-government projects, ensuring that the systems
developed are flexible and future-proof. By using the framework, they can identify potential challenges related to
interoperability early in the project lifecycle and address them proactively, preventing delays and minimizing
costs.
Finally, the framework can serve as a guide for improving public transparency and accountability. By ensuring
that systems are well integrated, it enables better monitoring and evaluation of government services, making it
easier to track progress and outcomes. This is especially relevant for governments aiming to increase citizen
engagement and trust through improved service delivery.
6.3 Research Limitations and Future Work
The research has several limitations. Despite the Government of Botswana's efforts towards digitizing all
economic and social sectors, the existing ICT infrastructure may not adequately support the effective
implementation and scalability of the proposed e-GSOIF. The scope of this research did not encompass a technical
examination of how well the e-GSOIF aligns with the current ICT infrastructure.
During informal discussions with some study participants, the researcher noticed indications that the e-GSOIF
might face resistance to change, particularly due to the complexity of integrating various technologies such as
SOA, EDA, and ontologies. Users familiar with traditional systems might resist this complexity, and their
resistance to change could slow the adoption process. However, the study did not specifically investigate potential
resistance to change or incorporate it in the proposed framework.
As the framework is designed specifically for Botswana, adapting it to other contexts might require significant
customization to different technological, administrative, and cultural environments.
Based on the limitations identified in the current study, the following directions for future work can be
recommended. Future research should conduct a detailed technical assessment of Botswana's current ICT
infrastructure to determine its readiness and capability to support the implementation and scalability of the eGSOIF. This should include an evaluation of network capacities, data handling capabilities, and compatibility with
proposed technologies.
Furthermore, it is crucial to undertake a comprehensive study focused on understanding the resistance to
change among users of the existing systems. This study should explore the reasons behind resistance, such as the 
complexity of new technologies or attachment to old systems, and develop strategies to manage and mitigate
these challenges.
Research should be conducted on how the e-GSOIF can be adapted to different technological, administrative,
and cultural environments to ensure compatibility and effectiveness in other regions or countries.
In addition to the directions of future work derived from the current study’s limitations, future work could
include a longitudinal study to monitor the implementation of the e-GSOIF over time, examining both its
effectiveness and its impact on users and administrative processes.
These directions will help address the limitations of the current study and enhance the robustness and
applicability of the e-GSOIF, ensuring its success in improving governance and service delivery in Botswana and
potentially other contexts. 