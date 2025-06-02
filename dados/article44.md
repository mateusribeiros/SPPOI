Title: Convergence of Blockchain, IoT, and AI for Enhanced Traceability Systems: A Comprehensive Review

ABSTRACT The need for sophisticated traceability systems has become essential in increasingly complex
and globalized supply chains. The convergence of Blockchain (BC), Internet of Things (IoT), and Artificial
Intelligence (AI) technologies offers promising solutions to enhance traceability systems across various
sectors, particularly supply chain management (SCM). This paper presents a bibliometric and systematic
literature review (SLR) to examine trends, research patterns, and methodologies in integrating BC IoT and
AI into traceability systems. Bibliometric analysis of 530 documents from SCOPUS (2014–2024) identified
key trends, while the SLR, conducted across multiple databases following PRISMA guidelines, refined
the dataset to 43 peer-reviewed studies based on inclusion criteria. Recent research output has notably
increased, focusing on agricultural supply chains and SCM, with India and China leading in publications. The
analysis shows a predominance of experimental and hybrid methodologies, using Ethereum and Hyperledger
Fabric as key platforms. Key trends include AI-driven analytics, real-time IoT data collection, and the need
for secure, tamper-proof data by BC. However, interoperability, scalability, and standardization challenges
hinder adoption. The paper proposes a four-layer framework for integrating BC, IoT, and AI to improve
transparency, security, and efficiency and highlights the need for more empirical studies, industry-specific
frameworks, and standardization to overcome existing limitations.
INDEX TERMS Artificial intelligence, bibliometric analysis, blockchain, Internet of Things (IoT), traceability, supply chain and systematic literature review.
I. INTRODUCTION
The growing complexity and globalization of supply chains
have intensified the need for enhanced traceability systems,
which are crucial in ensuring product quality, accountability,
and transparency throughout the entire supply chain (SC)
lifecycle [1]. Traceability encompasses tracking and tracing
products from their origin through processing, distribution,
and eventual disposal. It is crucial for businesses striving to
improve SC visibility and operational efficiency [2]. Access
to accurate traceability data enables informed decisionmaking, facilitates crisis management, and ensures transparency, which is essential for maintaining SC integrity and
fostering stakeholder trust [3], [4], [5]
Traceability systems, integral to various industries, allow
stakeholders to monitor products, components, and materials across different production, distribution, and consumption stages [6]. These systems capture and record
crucial data, such as product origin, location, and movement, giving stakeholders comprehensive visibility into
SC operations [7]. Traceability has evolved from a beneficial tool to a fundamental requirement, particularly in
food [8], healthcare [9], agri-food [10], and pharmaceuticals, where product quality, safety, and regulatory compliance
are paramount [11]. Incidents, such as Bovine Spongiform
Encephalopathy cases and the 2013 horsemeat scandal, highlight the critical need for robust traceability systems. Such
systems are essential for ensuring product safety, facilitating
the rapid recalling of contaminated products, and protecting
public health [12]. These systems also enhance accountability
by verifying product authenticity and preventing counterfeiting or unauthorized alterations. In addition, they streamline
SC processes, improve inventory management, and enable
rapid responses to market changes, making them essential for
modern SCs [10].
Despite the advantages of traditional centralized traceability systems, they encounter several significant challenges that
hinder their effectiveness. One primary concern is their vulnerability to single points of failure, as reliance on a central
authority can lead to systemic disruptions if the authority faces issues [13]. Additionally, these systems often rely
on siloed databases and fragmented communication, which
impede integrated data sharing and obscure critical information across the SC. Poor real-time monitoring capabilities
limit stakeholders’ ability to respond to changes or disruptions [14] promptly. As SCs expand, scalability challenges
emerge, and high implementation costs hinder the adoption
of more advanced systems[14]. Furthermore, the dependence
on intermediaries can foster a lack of trust and accountability,
complicating data integrity verification [15]. Lastly, traditional systems are also vulnerable to tampering, posing risks
to data authenticity and security [16].
These challenges, illustrated in Figure 1, underscore the
urgent need for more resilient, flexible, and scalable solutions to overcome the limitations of conventional traceability
models. Addressing these issues is critical for improving the overall functionality of traceability systems and
promoting their effectiveness in meeting the demands of
modern SCs [17], [18]. By developing innovative approaches
that mitigate these challenges, stakeholders can improve
operational efficiency, enhance transparency, and foster
greater trust within the SC [19].
The integration of emerging technologies, including
Blockchain (BC), the Internet of Things (IoT), and Artificial Intelligence (AI), has garnered significant attention in
response to these challenges [20]. These technologies provide novel ways to rectify the deficiencies of conventional
traceability systems, facilitating improved data management,
automation, and communication [21], [22], [23]. The convergence of Blockchain, IoT, and AI presents a transformative
approach to traceability, combining the strengths of each
technology to improve transparency, efficiency, and overall
SC performance [24].
With decentralized architecture and cryptographic security,
BC technology is the backbone for secure and transparent traceability systems. BC guarantees data immutability,
mitigates fraud risk, and obviates the necessity for a central authority by documenting information throughout a
distributed network [25], [26], [27], [28]. Each transaction within the SC is recorded in a secure, tamper-proof
ledger, providing stakeholders with verifiable, accurate data
regarding product origin, movement, and handling [29]. This
capability is crucial for maintaining product authenticity,
preventing counterfeiting, and complying with regulatory
requirements [30], [31].
Complementing BC, IoT enables the real-time monitoring and collection of data through interconnected devices
and sensors embedded in products and infrastructure [32].
IoT devices continuously gather and transmit asset location, condition, and status data, enhancing SC visibility and
responsiveness [33]. For instance, IoT can monitor the environmental conditions of products, such as perishable goods,
medical supplies, and more, alerting stakeholders to potential
risks before they compromise product quality [34], [35], [36].
The real-time data enhance decision-making and support
proactive management of SC disruptions [37].
AI enhances traceability systems by providing advanced
data analytics and decision-making functionalities. Machine
learning algorithms analyze vast amounts of data from IoT
devices, detecting trends and anomalies and forecasting
insights that enhance SC operations [38], [39]. AI-driven
analytics enable stakeholders to anticipate risks, forecast
demand, and streamline processes, ultimately improving efficiency and sustainability in the SC [31].
The convergence of BC, IoT, and AI technologies offers a
transformative framework designed to address the limitations
of traditional traceability systems. Each technology brings
unique advantages, but their integration creates a synergistic
effect that significantly improves the functionality and performance of these systems [40]. This comprehensive approach
tackles critical challenges, including transparency deficits,
security vulnerabilities, and restricted real-time connectivity often found in conventional methods [41]. By utilizing
BC’s decentralized and immutable ledger, IoT’s capability to gather real-time data through interconnected devices,
and AI’s ability to analyze extensive datasets for predictive
insights, this integrated solution empowers stakeholders to
optimize SC operations innovatively [42].
Furthermore, this synergy not only enhances transparency
by delivering real-time, verifiable data across the SC but also
strengthens security by maintaining the integrity of records
through BC’s cryptographic protections. When combined
with AI-driven analytics, real-time information captured by
IoT devices enables stakeholders to pinpoint potential risks,
anticipate disruptions, and make informed decisions that
boost operational efficiency [43], [44], [45]. As a result, this
integrated framework facilitates more effective risk mitigation strategies, enabling rapid responses to challenges, such
as disruptions, fraud, and product recalls.
While numerous review studies have focused on the impact
of individual BC, IoT, or AI technology or their dyadic combinations, such as BC with IoT or BC with AI, on traceability
across various sectors, such as, businesses [40], SCs [46], and
healthcare [47], there is a significant lack of comprehensive
literature reviews that quantify the existing knowledge and
provide an in-depth examination of the synergistic effects of
these technologies in enhancing traceability. Existing reviews
have largely overlooked the potential benefits of a holistic
integration approach [48]. The combination of bibliometric analysis and systematic literature review is essential
to address this knowledge gap. This dual approach will
enable a quantitative evaluation of publication trends, influential research, and emerging topics, along with a qualitative
synthesis of methodologies, implementation platforms, and
application areas. Such an integrative review will clarify the
current state of research and identify critical areas for future
investigation, offering valuable insights for academia and
industry practitioners seeking to leverage these technologies
for enhanced traceability systems.
This paper aims to provide a comprehensive bibliometric
analysis and systematic literature review to elucidate these
aspects and contribute to this field’s growing knowledge.
By examining the current state of research and identifying
key trends and gaps, the study seeks to offer valuable insights
into integrating these technologies into traceability systems.
Through this analysis, the paper will highlight the potential
for these technologies to revolutionize logistics and SCM,
paving the way for future research and development in this
dynamic area. The following are the research questions (RQ)
that guide the study:
RQ1: What are the emerging trends and patterns in publications within this domain, and which countries, articles,
authors, journals, and keywords have the greatest influence,
as determined by bibliometric analysis?
RQ2: What were the predominant research methodologies
employed by studies on the convergence of BC, IoT, and AI
in traceability systems?
RQ3: Which implementation platforms or environments
were commonly used in studies integrating BC, IoT, and AI
into traceability system?
RQ4: What areas were the Integration of BC, IoT, and AI
applied for traceability systems most frequently explored?
RQ5: What conceptual framework can be developed for
integrating BC, IoT, and AI into traceability systems, and how
does this improve traceability across key application areas?
The subsequent sections of this paper are structured as
follows: In Section II, related works are highlighted, while
the methodology employed for the bibliometric analysis and
systematic review are outlined in Section III. In Section IV,
the results and discussion are presented. Finally, in Section V,
the paper concludes by offering reflections on the findings,
acknowledging the study’s limitations, and proposing directions for future research.
II. RELATED WORKS
Several review studies have focused on different aspects and
sectors, providing valuable insights into the potential and
limitations of BC, IoT, AI, or their combination in traceability systems. For instance, [49] conducted a systematic
literature review (SLR) and bibliometric analysis on the
dairy industry, exploring AI and Industry 4.0 technologies
from 1999 to 2022. The study identified benefits, challenges,
and future directions, contributing a technological intervention wheel and a novel bibliometric analysis. It emphasized
the necessity for technological advancements in traceability
within the dairy industry. Similarly, [50] critically reviewed
traceability in the agriculture sector, presenting a taxonomy
of ideas and analyzing recent research activities. The study
underscored the importance of addressing food SC challenges
through technological interventions, particularly the increasing demand for certified products and the application of
distributed ledger technologies. Both studies highlighted the
critical need for robust traceability systems in the agriculture and dairy sectors, where BC and IoT can significantly
enhance transparency and accountability.
In [37], a SLR on the food SC was conducted, focusing on
models integrating BC technology from 2016 to 2023. Their
comprehensive overview highlighted BC’s growing use and
impact on enhancing transparency and efficiency. This work
aligns with [14], which reviewed BC technology for agrifood traceability from 2005 to 2019, identifying BC-based
solutions and their positive impact on sustainability. Both
studies emphasized the transformative potential of BC in
ensuring food safety and traceability, providing a clear pathway for future research in the agri-food sector. [51] examined
BC-based implementations for SC traceability, providing an
in-depth analysis of the technical features, maturity levels,
challenges, and unresolved issues from 2018 to 2021. The
detailed taxonomy of implementations clearly explained BC
adoption’s technical aspects and state in SCs. This study
is complemented by [52], where a bibliometric and content
analysis in the business sector was conducted, characterizing
the applications and advantages of integrating AI and BC
up to 2020. Their analysis is crucial for understanding the
intersection of AI and BC in business contexts and identifying research trends. In [40], a critical review of BC and
AI integration in SCs was presented, identifying relevant
studies from 2017 to 2022. The research highlighted the
importance of traceability in conventional SCs, proposed BCbased solutions, examined the potential of AI, and analyzed
multiple practical use cases. It highlighted the importance of
integrating AI and BC to enhance SC traceability, providing
practical insights into its applications.
While numerous studies have delved into the individual
and dyadic integration of BC, AI, and IoT technologies in various sectors, there remains a substantial gap in comprehensive
reviews that quantify and critically analyze the synergistic
effects of these technologies on traceability systems.
A. UNIQUENESS OF PRESENT STUDY
The present study distinguishes itself by conducting a
comprehensive review that examines the integration of
BC, IoT, and AI into traceability systems over a decade
from 2014 to 2024. This approach identified emerging
trends and uncovered key contributors, articles, journals,
and research methodologies. The study offers a holistic perspective, mapping these technologies’ intellectual structure
and practical applications in enhancing traceability, which
is critical for improving transparency and efficiency across
traceability systems. Previous literature reviews, such as
those by [49] and [50], generally focused on narrower traceability aspects, often restricted to specific industries, such
as the dairy or agri-food sectors. These works highlighted
the significance of BC in specific domains but did not provide a broad view of integrating multiple technologies, such
as AI and IoT, within traceability systems. For example,
[53] concentrated on BC-based models within the food SC,
emphasizing transparency and sustainability, but lacked comprehensive analysis beyond the sector.
This study stands out by incorporating a systematic review
protocol to address the limitations of prior research, which
often relied on subjective or critical reviews without robust
methodologies. Moreover, the study adopted a data-driven
bibliometric analysis, which offered a more objective insight
productivity and emerging themes in BC-IoT-AI integration
for traceability. Unlike [52], which explored AI and BC in
business contexts but did not focus on IoT or traceability, the
present study bridged that gap by examining the synergy of
these technologies across multiple sectors.
This study provides actionable insights by identifying
influential entities and examining research methodologies
and implementation platforms. Additionally, it proposes a
framework for future BC, IoT, and AI integration, setting
an agenda for ongoing research and development. This is a
critical contribution to the field, as it consolidates existing
knowledge and provides a foundation for future studies to
build on, furthering the development of BC-based traceability
systems across industries.
In conclusion, this study contributes to a deeper understanding of the current landscape. It offers a forward-looking
perspective, addressing unexplored areas and providing
recommendations for future research. By doing so, it establishes itself as a critical reference for advancing the integration of BC, IoT, and AI in traceability systems. Table 1
presents the overview and comparative analysis of previous
reviews and the present study.
III. METHODOLOGY
This study employed a structured seven-phase research
methodology to explore the integration of BC, IoT, and AI
in traceability systems. The process began with a research
design adopting a mixed-method approach. This approach
combined quantitative bibliometric analysis with qualitative
SLR to comprehensively understand the research landscape
and trends [54]. A rigorous search strategy was then developed, focusing on peer-reviewed articles published between
2014 and 2024. Explicit inclusion and exclusion criteria were
established to ensure the selection of relevant and highquality studies.
The selection and screening process involved a thorough
review of articles based on their titles, abstracts, and full-text
content, arriving at a final set of studies for detailed analysis. Quality assessment criteria were applied to evaluate the
studies, followed by data extraction to collect relevant information. This data was then synthesized to uncover emerging
trends, patterns, and gaps in the literature. This systematic and phased approach ensured that the study provided
a comprehensive and distinct understanding of how BC, IoT,
and AI are integrated into traceability systems, offering valuable insights for future research and practice.
A. RESEARCH DESIGN
This study employed a mixed-methods approach, integrating
bibliometric and SLR approaches to explore the integration
of BC, IoT, and AI in enhancing traceability systems. This
dual methodology leveraged the strengths of both quantitative
and qualitative analyses to provide a comprehensive understanding of the research landscape, identify key trends, and
synthesize existing knowledge [55]. Bibliometric analysis
involves quantitatively assessing academic literature through
statistical and mathematical methods. This approach aided
in mapping the research landscape by analyzing publication
trends, identifying influential authors, institutions, and journals, and uncovering collaboration patterns. By providing a
macro-level view, bibliometric analysis highlights key players and emerging trends within the field [56], [57].
Conversely, the SLR method involved a structured and
comprehensive review of the existing literature to answer
specific research questions. It included a detailed search
strategy, the application of inclusion and exclusion criteria,
data extraction, and critical appraisal of the selected studies.
This method provided an in-depth understanding and critical
evaluation of the literature, enabling the synthesis of findings
and identification of research gaps [58], [59].
The combination of bibliometric analysis and SLR offered
several advantages. Bibliometric analysis provided quantitative insights into the research landscape, identifying key
players and trends. This quantitative insight was complemented by the SLR, which delved into the qualitative aspects
of the literature, providing an in-depth understanding and critical evaluation of existing studies. Together, these methods
offered a holistic approach to exploring the integration of BC,
IoT, and AI in traceability systems.
The rationale behind selecting these methods was their
complementary strengths. Bibliometric analysis helped map
the research domain and identify influential works and
emerging trends, which were crucial for understanding the
current state of research. The SLR, on the other hand, allowed
for a detailed and critical examination of the identified
literature, enabling the synthesis of findings and identifying research gaps. By combining these methods, the study
aimed to provide a comprehensive and distinct understanding of how BC, IoT, and AI can be integrated to enhance
traceability systems. This approach ensured that the study
captured the breadth and depth of the research field, offering valuable insights for academics and practitioners alike.
Following the data collection phase, several bibliometric
software tools were employed to conduct a comprehensive
analysis, revealing publication trends, influential works, and
critical research themes related to integrating BC, AI, and
IoT technologies in traceability systems. VOSviewer [55]
was utilized for network-based visualization of citation data,
bibliographic details, and keywords, as in [32]. MS Excel
was used to organize data and create graphical illustrations,
such as publication trends over time and the distribution of
documents across different countries and institutions.
Additionally, Harzing’s Publish or Perish [56] was used
to calculate citation metrics and assess the impact of individual authors and publications within the dataset. This tool
facilitated understanding the influence and reach of specific
studies and researchers in the domain. The combination of
these tools, which allowed for a thorough and detailed analysis of the bibliometric data, revealed critical insights into the
emerging trends and patterns in integrating BC, IoT, and AI
into enhanced traceability systems.
1) BIBLIOMETRIC ANALYSIS
For the bibliometric analysis, the Scopus database was
selected due to its comprehensive coverage of peer-reviewed
literature and robust indexing of high-quality journals across
various disciplines. Scopus offers an inclusive dataset, making it ideal for examining the integration of BC, IoT, and
AI in traceability systems. The extensive metadata available
in Scopus, including citation counts, author affiliations, and
publication details, enhanced the depth and reliability of
the bibliometric analysis. This study followed the guidelines
proposed in [56] for conducting the bibliometric analysis.
Figure 2 illustrates the Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) diagram for
the bibliometric methodology used in this study. To ensure
comprehensive search, specific keywords related to BC, IoT,
AI, and traceability systems were used, with search strings
designed to include variations of critical terms and Boolean
operators to capture a broad range of relevant studies.
In April 2024, a TITLE-based search query was executed
on the Scopus database. The result was filtered according to
the inclusion and exclusion criteria based on time frame and
language, yielding 530 documents. Given the nascent stage
of the field, all documents were used for the bibliometric
analysis. The complete dataset was exported from Scopus in
both CSV and RIS formats, including metadata such as titles,
abstracts, keywords, author names, affiliations, and citation
information.
2) SLR
In this study, the SLR was based on recommendations
by [58] and [59]. The systematic nature of the SLR ensured
that the review was exhaustive and unbiased, providing a
robust synthesis of existing knowledge. The SLR approach
comprised research questions guiding the study, the search
strategy, paper screening and selection, and the inclusion
and exclusion criteria. The SLR aimed to provide a more
comprehensive and qualitative understanding of the existing
research in the domain.
B. SEARCH STRATEGY
The search strategy for this study was designed to comprehensively identify relevant literature on integrating BC,
IoT, and AI into enhanced traceability systems. Six academic
databases were selected, which were Scopus, IEEE Xplore,
Web of Science, Google Scholar, ScienceDirect, and ACM
Digital Library, to ensure coverage across various disciplines,
such as computer science, engineering, and logistics. The
selection of these databases was informed by their frequent
use among researchers, as recommended by Chen et al. [60].
An additional reason for choosing these databases was their
advanced search functionality, which supports the use of
Boolean operators. Moreover, their filtering feature enabled
the narrowing down of the results by publication year [61].
The search strings were carefully developed using core
keywords and synonyms related to BC, IoT, AI, and traceability systems. Boolean operators (AND and OR) were
employed to combine these terms, resulting in comprehensive
search queries that could capture the full scope of relevant
studies. The query used was as follows: (‘‘BC’’ OR ‘‘distributed ledger’’ OR ‘‘smart contract’’) AND (‘‘IoT’’ OR
‘‘Internet of Things’’ OR ‘‘RFID’’ OR ‘‘sensors’’) AND
(‘‘AI’’ OR ‘‘machine learning’’ OR ‘‘deep learning’’) AND
(‘‘logistics traceability’’ OR ‘‘supply chain traceability’’).
Specific search limits were applied to ensure the results’
relevance and quality. The timeframe for the search was
restricted to studies published between January 1, 2014, and
April 19, 2024, focusing on capturing recent advancements.
Additionally, only English-language publications were considered to maintain consistency in the review process.
Document types were limited to peer-reviewed articles. After
executing the search queries across the selected databases,
the results were filtered according to the inclusion and exclusion criteria. The inclusion criteria mandated that studies
explicitly addressed the integration of BC, IoT, and AI
into traceability systems. In contrast, the exclusion criteria
focused on eliminating irrelevant, non-English, or outdated
publications. The search process was precisely documented,
including the rationale behind the selection and exclusion
of studies, ensuring transparency and reproducibility in the
research methodology.
C. INCLUSION AND EXCLUSION CRITERIA
In this section, the criteria for selecting studies for bibliometric analysis and SLR are outlined. The goal was to ensure
that only relevant and high-quality studies were included,
providing a comprehensive understanding of this domain’s
current state of research.
1) INCLUSION CRITERIA
1. Articles must address the integration of BC (or related
terms such as ‘‘distributed ledger,’’ ‘‘Hyperledger,’’
‘‘Bitcoin,’’ ‘‘Ethereum,’’ or ‘‘smart contract’’), AI (or
terms such as ‘‘machine learning,’’ ‘‘neural network,’’
or ‘‘deep learning’’), and IoT technologies (or related
terms such as ‘‘QR code,’’ ‘‘RFID,’’ ‘‘barcode,’’ or
‘‘sensor devices’’) for traceability systems.
2. Only articles or reviews that explicitly addressed the
integration of BC, AI, and IoT in traceability systems.
3. Publications must be in English and published within
the years 2014 to 2024.
4. Articles must be peer-reviewed to ensure high quality
and reliability.
2) EXCLUSION CRITERIA
1. Articles that discussed BC, AI (or related terms such
as ‘‘machine learning,’’ ‘‘neural network,’’ or ‘‘deep
learning’’), and IoT technologies separately without
focusing on their integration.
2. Publications not available in English or published outside the timeframe of 2014–2024.
3. Articles with inaccessible full-text content, making it
impossible to verify the content.
4. Articles from journals with unverified indexing or
questionable reputations.
5. Records mislabeled as research articles, which, upon
verification, were found to be other types of publications, such as editorials.
By applying these inclusion and exclusion criteria, the
study ensured that the selected literature was highly relevant
and provided robust insights into integrating BC, IoT, and AI
into enhancing traceability systems.
D. PAPER SELECTION
The paper selection process was carefully structured to ensure
the inclusion of pertinent and high-quality studies. Initially,
a total of 132 research articles were identified through
comprehensive database searches, with an additional seven
records obtained from manual searches, resulting in a combined total of 139 articles. These articles were then processed
through the Mendeley reference manager to identify and
remove 23 duplicate records, leaving 116 unique articles
for further evaluation. The Rayyan AI-powered tool was
employed to streamline the screening process. The first phase
involved title screening, where 43 articles were excluded due
to their lack of relevance to the research topic, reducing the
pool to 73. Following this, abstract screening was conducted
using Rayyan, which led to the exclusion of 18 articles that
did not meet the predefined inclusion criteria. This process
narrowed the selection to 55 articles and subjected them to
full-text assessment. During the full-text assessment, 12 articles were excluded, as they failed to meet the inclusion
criteria, resulting in a final selection of 43 articles. These
articles were rigorously reviewed to ensure that they were
relevant and of high quality for SLR. Applying stringent
inclusion and exclusion criteria ensured that only the most
relevant literature was selected for SLR, facilitating a comprehensive and focused analysis of this domain’s current state
of research. Figure 3 presents the PRISMA diagram, which
demonstrates the paper selection process.
E. QUALITY ASSESSMENT CRITERIA (QAC)
The quality assessment criteria were designed to thoroughly
evaluate the studies’ contributions and methodologies concerning integrating BC, IoT, and AI into traceability systems.
The criteria emphasized the rigor of research methodologies,
ensuring that each study presented a detailed and critical
examination of its approach, including its suitability and
potential limitations. Additionally, the criteria evaluated the
adequacy of the implementation platforms used in the studies, ensuring that these platforms were thoroughly described
and critically analyzed. Furthermore, the depth analysis in
the application areas was closely examined, focusing on
how comprehensively each study explored the integration
of these technologies within various contexts of traceability
systems. The criteria also prioritized the clarity with which
specific technologies were identified and assessed, particularly regarding their effectiveness and relevance to enhancing
traceability systems. This comprehensive approach ensured a
distinct understanding of how BC, IoT, and AI are integrated
to advance the field of traceability systems.
F. DATA EXTRACTION
Data extraction for the bibliometric analysis and SLR was
conducted to ensure a comprehensive understanding of the
research landscape. For the bibliometric analysis, specific
features extracted were the authors’ name, publication year,
journal name, citation count, country of origin, and keywords
used in the studies. These elements were essential for identifying emerging trends, influential contributors, and patterns
within the research domain of BC, IoT, and AI integration in
traceability systems.
For the SLR, additional data were systematically collected
from the selected studies, which were research methodologies, implementation platforms or environments used,
application areas of technology integration, specific technologies utilized, and key findings and contributions. Each
study was then critically assessed based on the clarity and
relevance of the research questions, the methodology’s appropriateness, the data analysis’s robustness, and the significance
of the findings. This dual approach ensured that the analysis
was grounded in high-quality research, providing a solid
foundation for understanding the current state and potential
future directions in this field.
G. DATA SYNTHESIS
In this phase, the extracted data items were synthesized to
answer each research question. Data synthesis in this study
involved integrating and interpreting the findings from the
bibliometric analysis and SLR to draw meaningful insights.
For the bibliometric analysis, the data were quantitatively
synthesized by mapping out publication trends and identifying the most influential authors, journals, and countries,
as well as analyzing keyword co-occurrences to understand
the core themes and emerging topics in the field. This
synthesis provided a macro-level overview of the research
landscape, highlighting key focus areas and gaps within literature.
In the SLR, the data synthesis focused on the qualitative
aspects of the studies. The extracted data were categorized
and analyzed to identify standard research methodologies,
implementation platforms, application areas, and the specific
technologies utilized to integrate BC, IoT, and AI for traceability systems. This process involved comparing the findings
across different studies to identify patterns, inconsistencies,
and areas where further research is needed. By synthesizing
the data from both bibliometric analysis and SLR, the study
provided a comprehensive understanding of integrating these
technologies, offering valuable insights for both academic
research and practical applications in enhancing traceability
systems.
IV. RESULTS AND DISCUSSION
The study’s findings were structured to address the RQ.
A concise discussion is provided, aiming to answer each
FIGURE 4. Breakdown of articles distribution across multiple selected
databases.
research question as accurately as possible. The bibliometric analysis results were organized to highlight publication
trends over time and identify influential authors, institutions, countries, and journals, as well as to examine keyword
co-occurrence to reveal research hotspots and emerging
trends. The SLR also detailed the predominant research
methodologies, implementation platforms, application areas,
and technologies utilized in existing studies. By structuring
the results in this manner, the study offers a clear and comprehensive view of the current research landscape, providing
valuable insights for further studies in the field. Table 11
provides a comprehensive summary of the examined studies,
categorizing their key contributions, application domains or
use cases, methodologies employed, implementation platforms, and noted limitations. This structured representation
facilitates a clear understanding of each study’s focus.
TABLE 2. Yearly distribution of total publications (2014–April 2024).
A. SEARCH RESULTS OVERVIEW
Two search queries were executed for this study. The first
query, conducted on the SCOPUS database, yielded 530
documents used for the bibliometric analysis. The second
query was performed across multiple databases, returning
a total of 139 articles: 132 from six databases (26 from
SCOPUS, 10 from Web of Science, 7 from ScienceDirect,
9 from ACM Digital Library, and 3 from IEEE Xplore) and
7 additional articles identified through manual search. After
processing the results using the Mendeley reference manager,
23 duplicates were identified and removed. Subsequently,
61 articles were excluded based on their titles and abstracts,
and the predefined exclusion criteria were applied to reduce
the sample to 55 articles. During the full-text assessment,
12 articles were further excluded as they did not meet the
inclusion criteria, resulting in a final selection of 43 articles
for analysis. Figure 4 presents a detailed breakdown of the
database sources, and the number of articles retrieved from
each.
B. RQ1: WHAT ARE THE EMERGING TRENDS AND
PATTERNS IN PUBLICATIONS WITHIN THIS DOMAIN,
AND WHICH COUNTRIES, ARTICLES, AUTHORS,
JOURNALS, AND KEYWORDS HAVE THE GREATEST
INFLUENCE, AS DETERMINED BY
BIBLIOMETRIC ANALYSIS?
In this section, the first research question (RQ1) is addressed
using the bibliometric analysis of data collected from the
Scopus database, encompassing 530 documents. RQ1 sought
to identify the global research trend of publications, annual
scientific research production, document types, country-wise
contributions, author productivity regarding citations and
authored documents, active sources (journals), and prevalent
keywords.
1) GROWTH AND TREND OF PUBLICATIONS
Figure 5 and Table 2 display the distribution of total publications yearly from 2014 to April 2024, totaling 530 publications. A noticeable increase in publications is evident from
only one publication in 2014 to a peak of 166 publications
in 2023, indicating a growing interest in the subject over the
years. The percentage of publications shifted significantly,
particularly in recent years, with 2021 to 2023 collectively
contributing over 72% of the total publications. Notably,
2022 and 2023 accounted for 24.2% and 31.3% of the total,
respectively, reflecting a surge in research activity during this
period. Conversely, the earlier years (2014-2018) contributed
minimally, highlighting the trend toward increased scholarly
engagement in the topic of interest, as it had gained traction
within the academic community.
2) DOCUMENT TYPES
Figure 6 and Table 3 present the distribution of document
types in the research domain, showing that conference papers
are the most prevalent, accounting for 28.1% of the total publications, followed closely by journal articles at 26.2% and
conference reviews at 24.3%. These three categories dominate the research output, representing nearly 79% of the total.
Book chapters and review papers contribute smaller shares,
FIGURE 5. Annual scientific production (Source: Scopus 2024).
FIGURE 6. Document by type (Source: Scopus 2024).
at 9.6% and 8.7%, respectively. Other document types, such
as books (1.9%), editorials (0.4%), retracted papers (0.4%),
errata (0.2%), and short surveys (0.2%), form a minor portion of the total publications. This distribution highlights the
prominence of conferences and journals as critical platforms
for disseminating research. Other formats play a lesser but
still important role in the scholarly conversation.
3) COUNTRIES
The data in Table 4 and Figures 7 and 8 highlight the research
output across various countries, emphasizing the number
of publications, total citations (TC), and total link strength
(TLS). India leads with 132 publications, demonstrating significant engagement in blockchain research, accompanied
by 1,395 citations, indicating a high level of influence in
the academic community (TLS = 61). China follows with
62 publications and 1,134 citations (TLS = 44), suggesting a robust contribution and citation impact. The United
States has 49 publications and 839 citations (TLS = 52),
reflecting its established research presence. Other countries,
such as the United Kingdom, Canada, and Saudi Arabia,
show lower publication counts (25, 22, and 19, respectively).
However, their citations per publication reveal varying levels
of research impact, particularly Canada with 869 citations.
Pakistan, Italy, South Korea, and Spain exhibit similar publication figures. However, their total citations and TLS
scores reflect their distinct positions in the global blockchain
research landscape, indicating diverse research engagement
and influence. Overall, the table underscores the varying
levels of participation and impact across countries in the
blockchain research domain.
4) AUTHORS
Table 5 showcases the top 12 most-cited authors and their
associated publications, underscoring the growing interdisciplinary research emphasis on the convergence of BC, IoT,
and AI. Zhao et al. and Misra et al. are prominent and garnered significant citation counts. The prevalence of recent
publications reflects the increasing interest and intensifying
research efforts in this domain. The data also highlights a
strong collaboration between industry and academia, with
esteemed publishers, such as Elsevier and IEEE, leading the
dissemination. The research spans critical sectors, including
agriculture, healthcare, and energy, with notable contributions from authors such as Saurabh and Dey, Wang et al., and
Rahman et al. driving the innovation and application in these
fields.
5) DOCUMENTS BY AUTHOR
Figure 9 presents the distribution of documents by the
author, highlighting that A. K. Das leads with five publications. Y. Chen, N. Kumar, and D. Nagothu each have four.
Collectively, these authors contribute 49% of the analyzed
documents, demonstrating their substantial impact and significant contributions to the field.
TABLE 4. Scholarly publications and impact metrics by country.
FIGURE 7. Co-authorship network of documents by country.
FIGURE 8. Documents distribution by countries or territory.
6) KEY JOURNALS IN RESEARCH FIELD
Table 6 highlights the 12 most active journals contributing
to the research on blockchain-based traceability systems,
FIGURE 9. Distribution of publications by authors.
listing the number of publications, TC, and TLS for each
source. Lecture Notes in Networks and Systems leads the list
with 37 published documents and a modest citation impact
(TC = 4, TLS = 2). Lecture Notes in Computer Science
is closely behind, including its subseries, with 27 publications and a more substantial citation influence (TC = 41,
TLS = 3). Despite having fewer publications, the IEEE
Internet of Things Journal demonstrates a significant impact
with an impressive TC of 945 and TLS of 9, highlighting
its prominence in the field. Other key contributors include
the journals: Communications in Computer and Information
Science, IEEE Access, Sensors, and Electronics (Switzerland), each vital in advancing the academic discourse on
blockchain-based traceability. While varying in publication
volume and citation impact, these journals are essential platforms for sharing cutting-edge research.
7) KEYWORDS
Table 7 presents the distribution of keywords related to BC-,
AI- and IoT-based traceability systems. The data revealed
that ‘‘blockchain’’ leads as the most frequently used keyword by the authors, occurring in 454 publications with a
TLS of 1,656, indicating its dominant presence and research
influence in the field. ‘‘Internet of Things’’ follows closely
with 388 publications and a TLS of 1,200, reflecting its
significant role in traceability systems. ‘‘Artificial intelligence’’ ranks third with 133 publications and a TLS of
453, emphasizing its emerging but critical impact. Notably,
‘‘machine learning,’’ ‘‘deep learning,’’ and ‘‘big data’’ highlight the growing importance of advanced analytics in SCs.
Also, the occurrence of topics such as ‘‘network security’’
and ‘‘smart contracts’’ underscores the increasing focus on
data protection and automation. The distribution of the keywords indicates an interdisciplinary research landscape that
integrates various technologies to improve traceability and
security across multiple industries. Figure 10 presents the
overlay network visualization of keywords with a minimum
occurrence threshold of 25.
C. RQ2: WHAT WERE THE PREDOMINANT RESEARCH
METHODOLOGIES EMPLOYED BY STUDIES ON THE
CONVERGENCE OF BC, IoT, AND AI IN
TRACEABILITY SYSTEMS?
Integrating BC, IoT, and AI has been extensively explored
in traceability systems through various research methodologies. Researchers have employed diverse methodologies to
investigate this integration, encompassing theoretical frameworks, practical implementations, literature reviews, and
hybrid approaches that blend multiple strategies to provide
comprehensive insights. The review of 43 selected articles
on integrating BC, IoT, and AI into enhanced traceability systems revealed various methodologies employed. The
methodologies were categorized into conceptual, experimental, review, and hybrid approaches. Table 8 presents the
frequency distribution of methodologies.
The studies using the conceptual approach proposed various frameworks and models emphasizing BC for data
immutability, IoT for real-time data acquisition, and AI
for data analysis and process optimization. These models
served as foundational guidelines for developing integrated
traceability systems, providing theoretical underpinnings that
guide practical implementations. A total of 13 studies adopted
the conceptual approach, which are [2], [21], [62], [63],
[64], [65], [66], [67], [68], [69], [70], [71], [72]. These
studies focused on developing theoretical frameworks and
models for integrating these technologies into traceability
systems. Experimental studies validated these integrations
through real-world applications, simulations, and performance evaluations. These studies assessed the proposed
systems’ feasibility, accuracy, and scalability by implementing Ethereum or Hyperledger prototypes and various tools
such as TensorFlow and MATLAB. Key performance indicators, including traceability accuracy and data security,
were evaluated, demonstrating significant improvements and
practical viability. Fourteen studies employed experimental
methodologies, which are [22], [24], [73], [74], [75], [76],
[77], [78], [79], [80], [81], [82], [83], [84]. The studies
were geared towards practical implementation and validation,
testing the integration of BC, IoT, and AI in controlled or realworld environments.
Three review articles provided comprehensive overviews
and syntheses of the existing literature, which are [85], [86],
[87]. Hybrid approaches were used to combine different
methodologies, with six studies integrating conceptual and
experimental methods [44], [85], [88], [89], [90], [91], three
studies blending conceptual and empirical approaches [43],
[92], [93], two studies merging conceptual and case studies [94], [95], and two studies combining experimental and
case study methods [45], [81]. This diverse methodological
landscape reflects the multifaceted nature of traceability system research, balancing theoretical development with empirical validation. The significant presence of hybrid approaches,
totaling 13 studies, reflects the necessity of combining
multiple methodologies to achieve a more comprehensive
understanding and validation of integrated traceability systems. Figure 11 demonstrates the distributions of the studies
by methodologies used among the 43 selected papers. The
frequency analyses of the distribution of methodologies
reveal a predominant focus on experimental approaches
(14 studies), closely followed by conceptual methodologies (13 studies). The significant number of hybrid studies
(13 studies) highlights the importance of combining different
research methods to enhance depth and applicability. This
trend shows the critical need for robust theoretical models and
empirical validation to ensure the reliability and effectiveness
of proposed solutions in traceability systems.
D. RQ3: WHICH IMPLEMENTATION PLATFORMS OR
ENVIRONMENTS WERE COMMONLY USED IN STUDIES
INTEGRATING BC, IoT, AND AI INTO
TRACEABILITY SYSTEM?
To answer RQ3, a comprehensive analysis was conducted
on the implementation platforms or environments reported
across the 43 selected studies, identifying the most used tools
and technologies in integrating BC, IoT, and AI into traceability systems. Analyzing implementation platforms across
the 43 selected studies provided valuable insights into this
research domain’s prevalent tools and technologies. A critical
examination revealed that Ethereum BC and Hyperledger
Fabric/Caliper were platforms prominently featured due to
their distinctive attributes and capabilities.
Table 9 presents the overview of implementation platforms
commonly used across the selected studies. Ethereum, utilized in seven studies [22], [24], [43], [77], [88], [90], [92],
is particularly noted for its robust smart contract functionalities and decentralized architecture, making it a preferred
choice in 16% of the studies for developing secure and transparent traceability systems. Hyperledger Fabric and Caliper,
employed in four studies, which are [44], [79], [81], [91] (9%
of the sample), are favored for their modular and permissions
architecture, offering scalable and customizable solutions
ideal for enterprise-level applications.
Despite the strengths demonstrated by these platforms, the
analysis also highlights notable gaps within the existing body
of research. A significant portion of the studies, particularly
those categorized as reviews or conceptual frameworks, did
not specify any implementation platforms, with 15 studies
(35% of the sample) deemed ‘‘not applicable’’ in this context [2], [21], [62], [63], [64], [65], [66], [67], [68], [69],
[70], [71], [72], [96], [97]. This trend indicates a predominant
focus on theoretical exploration rather than practical application. Furthermore, among the experimental and empirical
studies, 12 studies did not report on the implementation
platforms used, which marked them as ‘‘not specified,’’
[21], [22], [62], [68], [69], [74], [75], [77], [78], [83], [85],
[89], [91], accounting for 28% of the sample. This lack of
transparency in reporting undermines the reproducibility and
comparability of findings, thereby limiting the potential for
researchers and practitioners to build on existing work. The
omission of critical details regarding the technologies and
tools used underscores the necessity for more rigorous and
standardized reporting practices in future research.
Regarding simulation tools, five studies [63], [75], [76],
[78], [98], constituting 12% of the selected sample, utilized environments such as TensorFlow, NetBeans IDE, and
MATLAB, for simulating and validating AI and IoT models.
These platforms are widely recognized for their effectiveness
in modeling and testing system functionalities across various
research contexts. These tools play an integral role in testing
system functionalities and refining models before their realworld deployment, providing a controlled environment that
allows researchers to experiment with different scenarios
and ensure the robustness and practicality of the proposed
systems. Figure 12 illustrates the percentage distribution of
implementation platforms across the studies.
However, while these simulation tools are crucial for model
development, their limitations must be acknowledged, such as
the potential discrepancy between simulated and real-world
conditions. The reliance on simulations alone may not fully
capture the complexities encountered in actual implementations, highlighting the importance of transitioning from
theoretical models to practical applications.
TABLE 9. Overview of implementation platforms used across selected
studies.
FIGURE 12. Distributions of platforms used in studies.
E. RQ4: WHAT AREAS WERE THE INTEGRATION OF BC,
IoT, AND AI APPLIED FOR TRACEABILITY SYSTEMS
MOST FREQUENTLY EXPLORED?
This study examined the application areas where BC, IoT,
and AI integration for traceability systems has been most
frequently explored, as evidenced by the selected studies.
Through the content analysis of the 43 studies, the research
identified seven key application areas demonstrating how
these technologies were utilized in traceability systems. The
findings are detailed in Table 10, which shows the frequency
distributions across these areas. Figure 13 visually represents
the distribution of studies by application areas.
Agri-food production and supply chain emerged as the
most researched area, with 15 studies [45], [53], [63], [65],
[66], [69], [80], [82], [83], [88], [91], [92], [93], [98]
emphasizing its significance in ensuring traceability and
transparency. This focus reflects the growing concern for food
safety, ethical sourcing, and the need for real-time data in
managing complex supply chains. The high number of studies
in this domain underscores the critical role these technologies
play in addressing the challenges faced by global food SCM.
SCM is another prominent application area, with ten studies demonstrating the pivotal role of integrated technologies
in enhancing efficiency. These studies [21], [62], [64], [68],
[70], [75], [85], [94], [99], [100] highlighted the transformative impact of BC, IoT, and AI on SC operations, including
inventory management, demand forecasting, and supplier
coordination. The emphasis on this area reflects the importance of these technologies in optimizing SC performance,
reducing operational costs, and improving overall visibility
and accountability. However, while the studies showcased
substantial potential, they also revealed challenges related to
interoperability, data privacy, and the need for standardized
protocols, including fraud prevention and compliance with
regulatory standards.
Healthcare and pharmaceutical applications were examined in five studies [44], [71], [89], [90], [95], pointing to
the potential of these technologies to improve patient safety
and drug traceability. The focus on healthcare highlights
the importance of reliable and secure traceability systems
in managing pharmaceutical SCs, especially in preventing
counterfeit drugs and ensuring the integrity of the distribution
process. Nonetheless, the relatively low number of studies in
this area indicates a gap in the research, suggesting the need
for further exploration to fully understand the potential and
address the challenges, such as regulatory compliance and
integrating existing healthcare systems.
The remaining application areas, which are manufacturing
and Industry 4.0 [67], [73], [81], [84], [86], smart cities and
urban management [43], [72], [79], financial transactions
and asset management [74], [77], [78], and environmental
monitoring and sustainability [22], [76], were explored in a
smaller number of studies. Each area presents unique opportunities and challenges for integrating BC, IoT, and AI. For
instance, manufacturing focuses on real-time monitoring and
data integration to enhance production processes. In contrast, the studies on smart cities emphasized optimizing urban
infrastructure and services. However, the limited research in
these areas highlights a need for more comprehensive studies
to explore the full potential and address the sector-specific
challenges that these technologies might face.
TABLE 10. Frequency distributions of application areas.
F. RQ5: WHAT CONCEPTUAL FRAMEWORK CAN BE
DEVELOPED FOR INTEGRATING BC, IoT, AND AI INTO
TRACEABILITY SYSTEMS, AND HOW DOES THIS
IMPROVE TRACEABILITY ACROSS KEY
APPLICATION AREAS?
Integrating BC, IoT, and AI offers a promising solution for
improving traceability systems. BC provides a decentralized
and immutable ledger, ensuring data integrity and security.
IoT enables real-time data collection through sensors and
devices, allowing for precise tracking of goods throughout
SCs [100], [101], [102]. AI offers advanced analytical tools
to process large amounts of data and derive insights to
optimize decision-making processes [39]. When integrated,
these technologies offer a holistic approach to addressing
the complexities of modern traceability systems [103], [104].
The proposed framework leverages the strengths of each
technology to create a more transparent, efficient, and secure
traceability system.
The proposed conceptual framework is a layered architecture that integrates BC, IoT, and AI to create an efficient,
secure, and transparent traceability systems [104], [105].
Each layer in the framework plays a vital role in ensuring
comprehensive monitoring, data integrity, and automation
across SCs, thereby offering a sophisticated solution for modern supply chain challenges [106]. The framework comprises
four interconnected layers, which are the perception layer,
network layer, security layer, and application layer, each
contributing uniquely to the overall system functionality. This
layered structure enables a seamless flow from data collection to end-user application, supporting traceability across all
stages of SCs.
1) PERCEPTION LAYER
The perception layer serves as the foundation of the framework and is responsible for data sourcing, collection, and
transmission. This layer comprises IoT devices, such as
sensors, RFID tags, and other monitoring tools. These are
strategically positioned to capture real-time data on asset conditions, locations, and environmental factors as goods move
through a supply chain [106], [107], [108]. By facilitating
continuous and accurate data acquisition, the perception layer
provides a reliable data stream that is essential for realtime tracking and situational awareness [109]. This layer
establishes the initial connection between physical assets and
digital systems, enabling traceability from the earliest stages
of SCs. As data is gathered, it progresses to the network
layer, where secure transmission and communication become
key [110], [111], [112], [113].
The Perception Layer plays a pivotal role in traceability
systems by leveraging IoT devices to securely collect and
transmit real-time data, addressing transparency, accountability, and security concerns. Bibliometric and content analyses
highlighted their significance, with frequent keywords such
as ‘‘Internet of Things’’ (388 occurrences, TLS: 1200) and
‘‘network security’’ (38 occurrences, TLS: 162). Its integration into Industry 4.0 and supply chain operations, evidenced
by terms like ‘‘supply chains’’ (78 occurrences, TLS: 340),
underscores its importance in enhancing operational efficiency, product authenticity, and regulatory compliance. The
layer’s interaction with Blockchain ensures secure data storage, while AI transforms raw data into actionable insights,
making it a cornerstone of robust, interdisciplinary traceability frameworks.
2) NETWORK LAYER
Above the perception layer, the network layer is responsible
for securely transmitting the collected data. The network
layer integrates IoT networks with a peer-to-peer (P2P)
communication structure, enabling direct and decentralized
interactions between devices [114]. Additionally, it includes
a blockchain network, which securely stores the transmitted
data to prevent unauthorized access or alterations. This layer
ensures that data flows seamlessly and securely from the
perception layer to higher layers, where the data is processed
and stored. In doing so, the network layer guarantees data
integrity. It supports a continuous, real-time communication
stream that is crucial for the efficiency and accuracy of traceability systems.
The Network Layer serves as a vital component in the convergence of Blockchain, IoT, and AI for enhanced traceability
systems, facilitating secure and efficient data transmission.
Its primary function is to ensure that information collected
by IoT devices is seamlessly transmitted to the blockchain
network, where it is stored immutably. Key components
include the IoT Network, which connects devices to enable
the exchange of data; Peer-to-Peer (P2P) Communication,
which establishes a decentralized architecture for secure
and direct device interactions; and the Blockchain Network,
which ensures that transmitted data is recorded in a secure,
transparent, and tamper-proof manner.
The Network Layer plays a pivotal role in maintaining
data integrity and security as information flows from the Perception Layer to the Blockchain Layer. Its ability to support
real-time, decentralized communication aligns with the findings of the bibliometric analysis, which highlighted ‘‘Internet
of Things’’ and ‘‘network security’’ as prominent keywords
in research on traceability systems. Similarly, the systematic
literature review (SLR) underscored the increasing adoption of P2P communication and IoT-enabled networks in
studies focusing on supply chain traceability, particularly in
applications requiring real-time monitoring and decentralized decision-making. By integrating these technologies, the
Network Layer addresses critical challenges such as data
tampering, scalability, and latency, enabling a robust framework that supports the demands of diverse industries. This
alignment with the bibliometric and content findings underscores the interdisciplinary nature of the research landscape,
where IoT networks and blockchain infrastructure converge
to provide reliable, secure, and scalable traceability solutions.
Advancing secured data transmission sets the stage for critical
security and analytics functionalities in the next layer, which
is the security layer.
3) SECURITY LAYER
The security layer is central to the framework’s reliability, combining BC and AI technologies to ensure robust
data security and advanced analytics. In the security layer,
BC technology establishes a distributed ledger, which maintains an immutable record of all transactions, safeguarding data from tampering and ensuring a trustworthy audit
trail [115], [116], [117], [118], [119]. Through consensus
mechanisms, this infrastructure verifies and validates all
transactions, creating a decentralized environment where
trust among supply chain stakeholders is intrinsic to the
system. Furthermore, smart contracts within the BC automate transactional processes, enabling real-time execution of
predefined conditions, thereby reducing manual intervention
and fostering process efficiency [120]. AI further enhances
this layer by preprocessing the collected data and leveraging
machine learning and deep learning tools for data analysis, anomaly detection, and predictive analytics. Together,
BC and AI offer both security and intelligence, transforming
raw data into actionable insights that aid decision-making
across a supply chain. With secure and verified data, the
framework is equipped to support user-friendly and practical
applications in the final layer, which is the application
layer [121], [122], [123], [124].
The bibliometric analysis highlighted the dominance
of Blockchain-related keywords, such as ‘‘blockchain’’
appearing in 454 publications, with TLS 1,656, ‘‘smart contracts,’’ and ‘‘network security,’’ underscoring its pivotal role
in ensuring secure and transparent traceability systems. These
findings emphasize the extensive application of Blockchain
for data immutability, automated processes, and transaction security. Similarly, AI-related keywords like ‘‘artificial
intelligence,’’ ‘‘machine learning,’’ and ‘‘deep learning’’
reflect the increasing use of advanced analytics for predictive
modelling, anomaly detection, and decision-making, evidenced by 133 publications (TLS 453). The growing interest
in IoT (388 publications, TLS 1,200) further highlights its
role as the data source that feeds into this layer for real-time
monitoring and analysis.
The Security Layer embodies the interdisciplinary nature
of research identified in the keyword analysis, showcasing
the convergence of Blockchain for data integrity, AI for
intelligent analytics, and IoT for real-time data capture.
This synergy is essential for addressing the challenges of
traceability systems, including data security, automation, and
actionable insights, thereby ensuring the efficient operation
of modern supply chains across various industries.
4) APPLICATION LAYER
At the top, the application layer functions as the user interface, providing access to processed information through a
range of specialized applications. This layer is designed
to enhance user experience and accessibility, offering tools
that allow stakeholders to monitor, analyze, and manage a
traceability system effectively. Key applications within this
layer include real-time tracking dashboards, which enable
users to visualize asset status and location across a supply
chain, and traceability tools that map each product’s journey [125]. Also included are anomaly detection alerts that
notify users of irregularities or disruptions, compliance monitoring features that ensure adherence to regulatory standards,
and data visualization tools that present complex data in
intuitive formats. All of these allow users to make informed
decisions quickly. By translating complex data streams and
analytical outputs into accessible, practical information, the
application layer empowers stakeholders to maintain control
and oversight, facilitating proactive management of logistics
operations [126]. This functionality underscores the framework’s adaptability to various industry needs, showcasing its
potential in real-world applications.
The application layer is aligned with the key domains
identified from the content analysis of selected studies.
In agri-food production and supply chains, it ensures traceability and transparency to address concerns about food
safety and ethical sourcing [91], [92], [93]. For supply
chain management (SCM), it supports functions like inventory management, demand forecasting, and fraud prevention.
In healthcare and pharmaceuticals, it enhances patient safety
and prevents counterfeit drugs through reliable traceability systems. Manufacturing applications focus on real-time
monitoring and data integration to optimize production
processes, while smart cities emphasize infrastructure and
service optimization. Additionally, this layer contributes to
financial transactions by ensuring secure asset management
and supports environmental monitoring with tools to oversee
sustainability metrics. By providing user-friendly interfaces
and applications tailored to diverse domains, the application
layer is instrumental in driving the adoption of Blockchain,
IoT, and AI technologies in traceability systems across
industries.
The integration of BC, IoT, and AI in this framework brings
numerous advantages across various industries. For instance,
in agriculture and food SCs, the framework enhances food
safety by monitoring production, storage, and transportation
conditions, while in healthcare, it helps ensure the authenticity and safety of pharmaceuticals [127]. In manufacturing
and Industry 4.0, the framework supports real-time production monitoring and inventory management [128], [129].
Collectively, these applications demonstrate the framework’s
versatility and adaptability, highlighting its potential for
broad-scale implementation [130]. However, realizing these
benefits requires overcoming specific challenges, particularly
regarding interoperability and cost.
Despite its potential, the framework faces challenges that
could hinder its adoption. One significant challenge is the
interoperability between diverse IoT devices and BC platforms, as the lack of standardization could impede seamless
integration. Moreover, implementing such a comprehensive
system involves considerable costs, which may be prohibitive
for smaller enterprises [131]. Addressing these challenges
requires a collaborative effort across industries to develop
standardized protocols and explore cost-effective solutions.
Successfully overcoming these barriers will open up new
avenues for expanding the framework’s applications and scaling its impact on traceability systems.
V. CONCLUSION AND FUTURE RESEARCH DIRECTIONS
The integration of BC, IoT, and AI technologies offers a
transformative approach to enhancing traceability systems,
particularly in SCM and other industries where transparency,
security, and efficiency are paramount. By converging these
technologies, organizations can build a robust system capable of tracking assets with greater accuracy and reliability.
This foundational insight underscores the importance of further examining the emerging trends, key contributors, and
methodologies in this field, establishing a basis for understanding the global progress and gaps in research. This study
reveals a notable increase in research publications on BC, IoT,
and AI integration, with significant contributions from India
and China, particularly in applications related to agricultural supply chains, healthcare, and Industry 4.0. Ethereum
and Hyperledger Fabric were identified as the most popular
implementation platforms, highlighting the role of BC in
securing and managing data within these systems. These
findings emphasized the diversity and industry-specific focus
within the research, providing a backdrop for exploring
methodologies that address varying requirements across sectors. Understanding these geographic and industry trends
paves the way for analyzing the prevalent research methods
used in the field.
A predominance of experimental and hybrid methodologies in the reviewed studies indicates a strong emphasis on
both theoretical development and practical validation. This
balance suggests that the integration of BC, IoT, and AI into
traceability systems is not only conceptual but also tested in
real-world scenarios to ensure applicability and effectiveness.
Such methodological approaches underline the importance
of rigorous research in advancing this field, setting the
stage for addressing technical and implementation challenges
that could impede widespread adoption. Recognizing this
methodological trend directs attention to existing challenges
that must be overcome for practical, real-world applications.
However, challenges related to interoperability, scalability,
and standardization continue to pose obstacles to broad adoption, particularly for small- and medium-sized enterprises
facing cost barriers. Addressing these challenges is critical,
as they affect the practicality and accessibility of integrated
BC, IoT, and AI systems. This highlights the need for targeted
future research that develops frameworks for overcoming the
obstacles, laying a foundation for seamless integration across
diverse operational environments. The discussion on challenges naturally extends to potential solutions, particularly in
the form of standardized protocols. Standardized frameworks
and protocols would facilitate interoperability across different BC, IoT, and AI systems, enabling cohesive integration
across industries. Developing these standards would streamline the implementation process, allowing different sectors
to adopt and adapt these technologies with minimal friction.
Such an approach underscores the need for industry collaboration and alignment, pointing to the value of standardization
as a next step in advancing the field.
Further empirical research, especially involving largescale applications, is essential to test the effectiveness and
resilience of BC, IoT, and AI integration in real-world
environments. Real-world testing not only validates the theoretical advantages but also reveals practical challenges and
opportunities for refinement, providing actionable insights
for stakeholders. As empirical studies help bridge the gap
between theoretical concepts and actual performance, they
also reinforce the importance of addressing industry-specific
needs, transitioning the discussion to sector-specific customization. Exploring sector-specific challenges, particularly
in areas such as healthcare and finance, will allow for tailored
solutions that align with the unique regulatory and operational
demands of each field. Customized frameworks can enhance
the relevance and efficiency of BC, IoT, and AI technologies
in specialized applications, further promoting their adoption
and utility. The importance of these sector-specific solutions
highlights the versatility of the proposed framework, setting
the stage for a broader conclusion on the overall impact and
future direction of this research area.