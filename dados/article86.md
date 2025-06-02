Title: LLM-Assisted Ontology Restriction Verification With Clustering-Based Description Generation

Abstract:
An ontology is a scheme for structuring relationships between concepts in a domain, promoting data interoperability and system integration. However, poorly designed ontologies can lead to errors and performance issues. While systems engineering has standardized evaluation guidelines (e.g., ISO/IEC), ontology engineering lacks such standards, leading to various independent evaluation methods. One frequent issue among novice developers is the misuse of ontology restrictions, particularly ‘allValuesFrom’ and ‘someValuesFrom’, which can significantly impact the correctness and reliability of ontologies. However, existing studies have not adequately addressed effective methods for detecting such errors. To address this gap, we propose a context-aware verification framework utilizing large language models to detect and correct misuse in ontology restrictions. Unlike conventional methods, our framework integrates contextual descriptions derived from ontological axioms, enabling more accurate verification. Additionally, we introduce a clustering-based description generation method that systematically organizes contextual information, further enhancing verification accuracy. Experimental evaluation conducted on diverse ontology datasets suggests that contextual integration improves verification performance. Moreover, the clustering-based description generation improves restriction misuse detection and correction compared to traditional approaches. By automating ontology restriction verification, this study contributes significantly to enhancing the reliability of ontology evaluation and provides a foundation for developing more scalable and standardized verification techniques.

Overview of the proposed framework. We utilize large language models to detect and correct misuse in ontology restrictions. In addition, we introduce a clustering-based description generation method that systematically organizes contextual information, thereby enhancing verification accuracy.
Overview of the proposed framework. We utilize large language models to detect and correct misuse in ontology restrictions. In addition, we introduce a clustering-based d...Show More
Published in: IEEE Access ( Volume: 13)
Page(s): 73603 - 73618
Date of Publication: 21 April 2025 
Electronic ISSN: 2169-3536
DOI: 10.1109/ACCESS.2025.3562560
Publisher: IEEE
Funding Agency:
SECTION I.Introduction
Ontologies are crucial schemes for knowledge representation and reasoning, widely utilized across various fields [1]. They define the relationships between concepts within a specific domain and structure knowledge [2]. By leveraging elements such as classes, object properties, data properties, instances, and axioms, ontologies can organize structured data. Ontologies facilitate data interoperability and enable seamless integration between different systems. Especially, ontologies can provide structured data representation, enabling precise querying and inference for complex information processing in knowledge-based systems. As a result, ontologies have found widespread use across diverse sectors, including healthcare, finance, and industrial automation [3], [4], [5]. Ensuring that an ontology is properly designed and implemented is essential for guaranteeing its quality [6]. A poorly designed or inaccurately implemented ontology may not function as expected in real-world applications, potentially leading to system performance degradation or errors. To prevent such issues, standardized quality assessment protocols exist in systems engineering, with international standards like those from ISO/IEC being widely adopted [7].

However, in the field of ontology engineering, there is a lack of such standardized quality evaluation guidelines. Consequently, various methodologies have independently emerged to address this need. Among these, OOPs [8] identifies 41 common pitfalls that ontology developers frequently encounter. Of these, 33 can be evaluated automatically, while the remaining 8 still require manual evaluation. One of the most common pitfalls, especially for novice ontology developers, is the misuse of restrictions [9]. The misuse of ontology restrictions often occurs when developers incorrectly apply constraints like ‘allValuesFrom’ and ‘someValuesFrom’. Since these misuses can significantly impact the functionality of an ontology, it is crucial to have reliable mechanisms to identify and rectify them. Resolving these challenges contributes to improving ontology quality, ensuring their robustness and applicability in real-world scenarios.

A. Types of Ontology Restrictions
Ontology restrictions define logical boundaries between classes to ensure consistency in semantic modeling. As illustrated in the Fig. 1, these restrictions are categorized into two main types:1

Value Constraints: Specify the type of values a property can have (e.g., Pizza must have certain Toppings).

Cardinality Constraints: Specify how many values a property can have (e.g., Students must take a minimum number of Course

FIGURE 1. - Ontology restriction Types: Value and cardinality constraints.
FIGURE 1.
Ontology restriction Types: Value and cardinality constraints.

Show All

B. Research Objective and Problem Statement
Research on the verification of ontology restrictions has been limited, but there have been recent attempts to address this issue [10], [11]. Notably, leveraging Large Language Models (LLMs) to verify the presence or misuse of restrictions [12] have shown some success, particularly in identifying missing or correctly applied restrictions. However, these studies demonstrate relatively low accuracy in detecting cases of misuse. The assumption behind this lower accuracy is that it is challenging for LLMs to determine whether a restriction is misused without any contextual information about the ontology. The core issue identified here is that the correct use of restrictions can vary significantly depending on the context. Restrictions that are valid in one scenario may be misapplied in another due to differing contextual requirements. This highlights the importance of providing LLMs with sufficient context to accurately evaluate restrictions. However, existing approaches typically present the restriction in isolation, without any contextual information, making it difficult for LLMs to distinguish between correct and incorrect usage. This limitation emphasizes the need for more advanced methods that can integrate contextual information into the verification process. Addressing this gap offers an opportunity to enhance the performance of LLM-based approaches and improve the accuracy of ontology restriction verification.

C. Methodology and Contributions
In this work, we propose a novel framework that integrates contextual information into the verification process to improve LLM-based detection of restriction misuse. This approach introduces two key innovations:

Context-Aware Verification Framework: Unlike prior methods that evaluate restrictions in isolation, our framework incorporates contextual descriptions as part of the input to LLMs. This allows for a more nuanced evaluation by providing the necessary background to distinguish between correct and incorrect uses of restrictions. By resolving ambiguities inherent in isolated evaluations, this method significantly enhances verification accuracy.

Automated Contextual Description Generation: Recognizing that ontologies often lack explicit contextual information, we adopt a clustering-based technique to generate contextual descriptions. This method groups similar axioms, ensuring internal cohesion and consistency, which in turn aids LLMs in understanding and verifying restrictions more effectively.

To validate the proposed framework, we conducted experiments on a diverse set of ontologies, including Pizza,2 Semantic Sensor Network,3 DemCare,4 Doremus,5 and ChEMBL.6 Experimental results demonstrate that incorporating contextual descriptions improves accuracy significantly, while the clustering-based generation approach further enhances the reliability of verification by identifying and addressing potential misuse patterns.

In summary, our research approaches a critical challenge in ontology engineering by introducing a context-aware, automated framework for verifying ontology restrictions. By enhancing the ability of LLMs to evaluate restrictions with contextual support, this work improves the quality of ontologies and lays the foundation for more efficient and reliable automated verification tools.

SECTION II.Related Work
A. Ontology Verification
Ontology verification has been approached through diverse methods [13], [14], [15], [16], yet the lack of a unified and standardized framework remains a significant challenge. Unlike software engineering, which benefits from established quality standards such as ISO/IEC 25012 [17], ontology verification lacks comparable consolidation. As a result, verification techniques have been developed independently, addressing specific aspects of ontology quality.

Recent studies have proposed various approaches to tackle these challenges. Wilson et al. [18] categorize ontology verification into structural, domain-specific, and application-based approaches. Tools like OntoQA [19], OOPs [8], and OntoMetrics [20] are commonly used to assess the structural consistency and logical organization of ontologies. For example, OOPs identifies 41 common ontology modeling errors, of which 33 can be automatically detected, while others require human intervention, such as evaluating domain completeness.

To address constraints on schema and inference, SHACL [13] has been proposed. The authors identify inconsistencies by verifying whether each new inference result derived from schemas violate existing constraints. Zhao et al. [21] proposed further improvements to enhance computational efficiency, including the conversion of schemas into internal representations and the use of key instances.

Domain-specific verification has also been advanced by incorporating natural language processing techniques such as keyword extraction and relation extraction. Brewster et al. [22] employed keyword identification and clustering to validate relationships between concepts, ensuring they align with real-world domain standards. More recently, Zaitoun et al. [23] utilized pretrained language models for named entity recognition and hierarchical relationship analysis, achieving improvements in the accuracy and comprehensiveness of domain alignment.

The practical applicability of ontologies is often evaluated using Competency Questions (CQs). Tan et al. [24] proposed generating CQs from software requirements specifications to assess whether an ontology meets specific use cases. By automating CQ generation process and translating them into SPARQL queries, studies such as those by Rebboud et al. [14] and Tufek et al. [15] have simplified domain-specific ontology evaluations.

Application-oriented approaches emphasize the integration of ontologies into broader systems. The authors in FOEval [25] quantitatively evaluate parameters like ontology size, class relationships, and operational performance. They provide insights into an ontology’s scalability and efficiency, ensuring its reliability in complex systems.

Wilson et al. [16] propose a systematic evaluation methodology for ontology verification to improve the quality of ontology-driven decision support systems. To achieve this, they apply quality theories from software and system engineering to classify ontology quality into structural, domain and application aspects and derived quality assessment metrics using the Goal-Question-Metric approach.

Despite these advancements, ontology verification still faces significant challenges. Existing studies have largely overlooked the verification of ontology restrictions. Most studies have focused on comparing quantitative metrics or, at best, analyzing semantic relationships through measures like cosine similarity between terms. However, critical areas that require human reasoning, such as the eight unresolved issues identified by OOPs, remain inadequately addressed. Among these, the misuse of restrictions—particularly common among novice developers—demands further investigation to bridge this gap in ontology verification research.

B. Ontology Verification with Large Language Models
Recently, LLMs have advanced rapidly and are being actively utilized in various research fields [26], [27]. In addition, some studies aim at overcoming the limitations of LLMs continue to progress [28], [29]. Notably, recent research has demonstrated the outstanding performance of LLMs in specific domains such as code generation [30], healthcare [31], and law [32]. As a result of these advancements, the application of LLMs in ontology research has also increased, with numerous studies focusing on the construction of ontologies [33] and Knowledge Graphs (KGs) [34] being published.

Ontology verification have advanced by incorporating structural and domain-specific evaluation methods. While traditional methods primarily relied on reference ontologies or domain-specific corpora to assess completeness and relevance, recent advancements with LLMs trained on diverse knowledge bases have introduced more efficient verification. For instance, Allen and Groth [35] propose a framework where LLMs evaluated class membership by analyzing instance and class information. However, the potential inclusion of Caligraph’s [36] data in the training set raises doubts about these models’ generalizability to new domains. Addressing these concerns requires further research into applicability of LLMs in novel contexts and their capacity to handle domain-specific challenges.

Another major advancement is the use of CQs to ensure that ontologies align with specific domain requirements. The CQs are typically translated into SPARQL queries for systematic analysis [37]. Recent studies have automated the CQ generation process by using LLMs [14], [15], to improve efficiency and consistency. For example, LLMs can generate and validate CQs based on domain-specific documents, with applications extending to KG evaluations [38], [39]. These methods enhance ontology verification by aligning ontologies with real-world requirements while streamlining scalability and efficiency.

There are also traditional tools like OOPS [8] have been pivotal, automatically identifying 33 out of 41 common ontology modeling errors using predefined heuristics. However, errors requiring domain-specific judgment or contextual understanding still necessitate manual evaluation. HERO [10] addresses these challenges by incorporating human-in-the-loop approach into ontology verification. The authors demonstrate that crowdsourcing, a process wherein non-expert contributors collaboratively identify errors in ontology relationships, can be comparable in quality to those obtained from expert assessments. Visualization tools such as vOWL, along with representation approaches like Rector et al. [9] and Warren et al. [40], further support this process by aiding human evaluators in understanding ontology axioms. Despite these advances, experts generally outperform non-experts on complex axiomatic verification tasks, thus there are still considerations regarding cost-effectiveness.

LLMs like ChatGPT have recently expanded the scope of ontology verification with automated methods. Tsaneva et al. [12] report that LLMs have capabilities ranging from intermediate to expert-level performance in ontology modeling tasks, often surpassing individual human evaluators in general axiom verification. Their study indicates that, although ChatGPT achieved high accuracy in axiom verification, it notably underperformed in identifying improper uses of ontology restrictions. We hypothesize that this reduced accuracy from insufficient contextual information available during restriction evaluation. Motivated by this hypothesis, our research integrates contextual information explicitly into the ontology verification process. Our approach aims to illustrate how context-aware methodologies can significantly enhance the performance of LLMs in ontology verification tasks. These insights establish the groundwork for the detailed evaluation of our proposed context-based solution, discussed comprehensively in subsequent sections.

SECTION III.Method
This study aims to identify and correct errors in ontology class restrictions. Previous research [12] employs LLMs to evaluate these restrictions but faces challenges in accurately identifying misuse. We hypothesize that the difficulty in detecting misuse of restrictions arises from the lack of consideration for the context in which the restrictions are used and the broader structure of the ontology. In this regard, we propose a method that evaluates restrictions by integrating information from both the ontology and the axioms, using a clustering-based approach to generate descriptive insights.

Our proposed framework, illustrated in Fig. 2, enhances the verification process by categorizing restrictions according to specific misuse types and clustering ontology axioms to generate comprehensive axiom descriptions. These detailed descriptions subsequently inform the creation of an ontology description, offering a holistic overview of both the ontology and its constituent axioms. Utilizing these generated descriptions, the framework systematically evaluates each restriction to identify potential misuses.

FIGURE 2. - Overview of the proposed framework.
FIGURE 2.
Overview of the proposed framework.

Show All

We incorporates contextual information to enhance the detection of ontology restriction misuses, addressing existing verification limitations. To enhance verification accuracy by thoroughly understanding the conditions under which restrictions are applied, we propose a comprehensive solution aimed at improving ontology quality.

A. Verification Flow
The framework for ontology verification comprises multiple stages, with the final validation stage serving as a critical step for confirming the correctness of restrictions. This section specifically describes the inputs and outputs involved in this final validation stage. The earlier stages within the framework are structured to produce these inputs by identifying misuse types, gathering relevant contextual information, and constructing preliminary restriction candidates.

During the final validation stage, the LLMs receive inputs including restriction scripts and detailed descriptions of the ontology, axioms, classes, and properties. The output from the LLMs is the optimal restriction script that effectively resolves the identified issues.

Input

Restriction Scripts: This involves possible scripts for sampled restrictions based on identified misuse types. It includes determining the specific type of misuse associated with each sampled restriction and creating all potential scripts capable of correcting the identified issue.

Axiom Description: This provides contextual information about how a sampled restriction is used. In other words, details about the specific setting and relationships in which the restriction appears within the ontology, helping to better understand the intended function of the restriction.

Ontology Description: The Ontology Description offers insights into the role of the sampled restriction within the broader structural perspective of the ontology. It provides an understanding of how the restriction fits into the ontology’s overall logic and schema, ensuring that any modifications maintain structural integrity and coherence.

Class/Property Definition: These are annotations (comments) from the existing ontology that contain information about each class and property. They help in understanding the intended use and characteristics of the classes and properties, thus providing additional contextual knowledge that aids in verifying and adjusting restrictions.

Output

Correct Restriction Script: From the set of generated restriction scripts, the framework selects the most appropriate script by referencing the input descriptions and definitions. This selection ensures that the chosen script aligns with the context of the ontology and addresses any identified misuse.

The entire process for creating these inputs and ensuring effective validation is detailed in the following section, which outlines the overall flow of the framework.

B. Framework Operational Sequence
The framework operates in the following steps. Initially, all axioms within the ontology are clustered to generate axiom descriptions that capture the common context of similar axioms. These axiom descriptions provide detailed information about individual clusters of axioms. Subsequently, these descriptions are used to create an ontology description, which synthesizes the broader structure and meaning of the ontology by integrating the relationships between axioms. Next, the axiom descriptions and ontology description constitute the contextual descriptions, encapsulating both the fine-grained and overarching contextual information derived from the ontology. The framework then samples specific restrictions and classifies them based on potential misuse types, generating all structurally feasible restriction scripts. Using the sampled restriction’s axiom description, ontology description, and class/property definitions, the framework selects the correct restriction script. Finally, this script is used as a reference to evaluate the existing restriction.

1) Step 1: Axiom Description Generation
Ontologies consist of axioms that define relationships, constraints, and logical structures within a specific domain. These axioms establish the foundational context and intended semantics of the ontology. We extend the scope by generating axiom descriptions through embedding all axioms and clustering them, rather than limiting ourselves to specific descriptions. This approach ensures a comprehensive and nuanced representation of the ontology.

To acquire meaningful and contextually rich axiom descriptions, we utilize LLMs with generative capabilities. These detailed descriptions enhance the accuracy of restriction verification by providing insights into their intended usage and logical coherence. For instance, in the case of an axiom “VegetarianSalad has only Vegetable.”, the correctness of this restriction hinges on the interpretation of the term ‘Vegetarian.’ If it implies a strictly vegan context, the restriction is semantically appropriate. However, if ‘Vegetarian’ encompasses broader dietary allowances such as eggs or dairy products, the restriction would require refinement. Consequently, precise descriptions clarifying the context of each restriction are essential for accurate verification.

To facilitate this, we pass all axioms into a pre-processing pipeline that ensures appropriate contextual representation. This pipeline embeds all axiom statements using text embedding models, enabling effective semantic clustering. Unlike approaches that cluster only restrictions, embedding all axioms allows the framework to account for relationships among diverse types of axioms, including class hierarchies, property constraints, and domain-specific rules.

The steps include:

Axiom Embedding: Each axiom is transformed into a vector representation capturing its semantic meaning.

Clustering Axioms: Here, we utilize a K-means-based clustering approach. Using computed text embeddings, we determine the optimal number of clusters through conventional optimization methods, such as the Silhouette method[41]. The method facilitates clustering that emphasizes both intra-cluster cohesion and inter-cluster separation, effectively categorizing axioms into coherent groups. Once the optimal number of clusters is determined, the axioms are clustered accordingly, resulting in the semantically coherent clusters. This process ensures that similar axioms are grouped together, forming semantically coherent clusters.

Generating Cluster Summaries: The framework uses LLMs to generate concise axiom descriptions, as shown in Fig. 3, capturing their interaction within the ontology. The LLMs is given the clustered axioms, then generates summaries of each axiom cluster. Without clustering, descriptions can either be overly specific or excessively general. For instance, a specific description might state that “Parmesan cheese has a mild spiciness level,” which focuses too much on an individual axiom. On the other hand, a general description might state that “This ontology categorizes entities based on various attributes and relationships,” which lacks sufficient detail to be useful. By clustering semantically similar axioms, the framework ensures that the generated descriptions maintain an appropriate balance—such as summarizing a group of axioms with “Cheese types are classified based on spiciness levels (mild, medium, hot),” which captures the key patterns without being overly narrow or too broad.

FIGURE 3. - An Example of Axiom Description Generation Prompt.
FIGURE 3.
An Example of Axiom Description Generation Prompt.

Show All

This approach addresses challenges in generating descriptions that are either overly detailed (focusing on specific axioms) or too generic (describing the entire ontology). By creating clusters of semantically similar axioms, the framework ensures that the descriptions strike a balance between specificity and generality, providing meaningful insights for subsequent verification steps.

2) Step 2: Ontology Description Generation
Accurately evaluating restrictions requires an understanding of their roles within the overall ontology. For instance, in the case of “VegetarianSalad has only Vegetable,” it is beneficial to comprehend how each element integrates into the broader ontology. If the ontology is about types of vegetarians, recipes, ingredients, and nutrients, ‘VegetarianSalad’ might represent a dish associated with a particular dietary type, and ‘Vegetable’ would denote an ingredient within that context.

This broader understanding is achieved through the generation of an ontology description. Based on the axiom descriptions, our framework constructs a more comprehensive ontology description that encapsulates the overall structure and context of the ontology by leveraging the LLMs. This step is crucial for understanding how individual restrictions align with and contribute to the logical framework of the ontology.

To accomplish this, we employ a prompt-based generation method (Fig. 4), which the LLM uses to synthesize axiom descriptions into a domain-oriented and coherent ontology description.

FIGURE 4. - An example of ontology description generation prompt.
FIGURE 4.
An example of ontology description generation prompt.

Show All

Here, we define and utilize three main components to describe and represent ontologies: key elements, relationships, and purpose. As shown in the corresponding answer in Fig. 4, the generated ontology description encompasses key elements, relationships, and the overall purpose of the ontology.

First, key elements refer to the core concepts central to an ontology. For instance, in a pizza ontology, essential concepts such as toppings and base serve as key elements, as these form the fundamental building blocks used to classify and describe different pizza types.

Second, relationships explain how the previously identified key elements relate to each other within the ontology’s domain. For example, in a pizza ontology, a relationship might be expressed as: “The base serves as the foundation upon which toppings are placed.”

Finally, the purpose articulates the intended application or objective behind creating and utilizing the ontology. It explicitly conveys the ontology’s intended function, derived from a combination of key elements and relationships. For instance, a pizza ontology’s purpose could be described as: “An ontology designed to classify and represent various pizza types based on toppings, base, and spiciness.”

This process ensures that the ontology description is neither overly concentrated on isolated axioms nor excessively generic. Instead, it provides a balanced perspective that clarifies the ontology’s structure, purpose, and logical relationships. By doing so, the framework enhances its capacity to evaluate axioms within the full context of the ontology’s schema.

3) Step 3: Restriction Scripts Generation
This step starts by categorizing restrictions based on common misuse types, enabling the verification process to effectively address specific errors. Misuse types are categorized into the following three types:

Type 1: Misuse of ‘allValuesFrom’ and ‘someValuesFrom’. The most frequent error made by novice developers is confusing the use of ‘some’ and ‘only.’ For example, a restriction like “Class1 Property ‘some’ Class2” could be incorrectly stated as “Class1 Property ‘only’ Class2.”

Type 2: Incorrect use of values with ‘hasValue’. This error occur when a specific entity or value in ‘hasValue’ is replaced with another incorrect or unintended value. For instance, “Class1 Property ‘hasValue’ Value1” might be incorrectly specified with an unintended entity or literal.

Type 3: Misuse of cardinality constraints. This involves incorrect application or interchange of ‘maxCardinality’, ‘minCardinality’, and ‘cardinality’, leading to logical inconsistencies. For example, “Class1 Property ‘min 2’ Class2” might be mistakenly swapped with ‘max 2’ or ‘exactly 2’.

Once each restriction is categorized into one of these types, it generates possible Restriction Scripts to represent alternative forms of the restriction for verification purposes.

For example:

A restriction like “Class1 Property ‘some’ Class2” categorized under Type 1 would generate scripts such as:

“Class1 Property ‘some’ Class2”

“Class1 Property ‘only’ Class2”

A restriction like “Class1 Property ‘hasValue’ Value1” categorized under Type 2 would retain its original script as the correct form.

A restriction like “Class1 Property ‘min 2’ Class2” categorized under Type 3 would generate scripts such as:

“Class1 Property ‘min 2’ Class2”

“Class1 Property ‘max 2’ Class2”

“Class1 Property ‘exactly 2’ Class2”

By classifying restrictions into misuse types and generating corresponding Restriction Scripts, the framework adopts a systematic and comprehensive approach to identifying and correcting common errors in ontology restrictions.

4) Step 4: Choosing the Correct Restriction Script
This step utilizes the generated axiom descriptions, ontology descriptions, and the definitions of the involved classes and properties to select the most appropriate restriction script for each misuse type. This process integrates context-aware information to ensure a more accurate evaluation compared to direct assessment methods that lack such contextual understanding.

For Type 1 and Type 3, the framework determines the most appropriate script from the generated options. For Type 2, it evaluates whether the current restriction is correct or incorrect. Leveraging the given contextual inputs, the framework relies on an LLM to analyze, process, and determine the most valid script—referred to as the correct restriction script—as illustrated in Fig. 5.

FIGURE 5. - Choosing correct restriction script prompt.
FIGURE 5.
Choosing correct restriction script prompt.

Show All

The final step involves comparing the original restriction with the correct restriction script derived from the previous steps. This comparison helps detect potential misuse and verify the logical consistency of the restriction.

By integrating contextual information into the ontology verification process, this framework enhances the accuracy of restriction evaluation, ensuring clear and effective application of restrictions.

SECTION IV.Experiments
In this study, we designed various experiments to evaluate the performance of the proposed ontology verification framework. Through these experiments, we aim to verify the accuracy of constraint evaluation when ontology and axiom descriptions are provided. The experiments involve preparing data by intentionally inserting errors into the constraints across ontologies from diverse domains. Additionally, we compared the performance of the proposed method based on different aspects such as LLMs, clustering, and error rates. An ablation study is also conducted to demonstrate the effectiveness of the proposed approach.

A. Experimental Setup
1) Datasets
The datasets were prepared from various domains, as shown in Table 1. A brief description of each ontology is provided below:

SSN: A standard developed by W3C that structurally represents sensor networks and their data. It focuses on IoT sensors and their interoperability.

ChEMBL: An ontology providing a biological knowledge base used in drug development. It includes biologics and associated metadata.

Doremus: A music ontology that offers information on various musical works and performances in an interoperable format.

DemCare: An ontology linking sensor data with dementia management for diagnosis and treatment. It supports the integration of data from multiple sources for healthcare applications.

Pizza: An educational ontology used for learning OWL (Web Ontology Language). It is designed as a demonstrative example for ontology construction and reasoning.

TABLE 1 Statistics of Each Dataset
Table 1- Statistics of Each Dataset
2) Error Generation
To evaluate the effectiveness of our proposed ontology verification method, datasets containing intentional restriction errors were required. These error datasets were generated using the following procedure: correct label assignments were derived from existing ontology constraints, establishing a baseline ground truth. By utilizing intentional errors and comparing these modified datasets with correct constraint configurations, we assessed the performance of our proposed approach. Specifically, we randomly selected ontology elements and replaced constraint conditions to create various erroneous scenarios while minimizing fluctuations in our experiments. To ensure experimental consistency, a fixed random seed was applied. The primary technique for error generation involved constraint replacement, designed to create confusion in constraint conditions. Restrictions such as ‘some’, ‘only’, ‘minimum’, ‘maximum’, and ‘exactly’ were randomly modified within the same restriction type to deliberately generate errors. In the specific case of ‘hasValue’ restrictions, entities were replaced with entities from different classes to induce errors. A default error rate of 10% was applied across all experiments, indicating that 10% of dataset entries contained intentional errors. To provide comprehensive comparative analyses, we examined the impact of varying error rates by testing additional scenarios with different levels of error prevalence.

B. Experimental Design
The experiments are conducted to comprehensively evaluate various aspects of the proposed framework. This includes comparing the performance across different LLMs, analyzing the impact of varying error rates on verification performance, assessing the changes in performance based on clustering techniques, and verifying the utility of the descriptions generated from ontology restrictions.

1) Performance Comparison Across LLM Models
To verify whether the proposed framework effectively leverages different LLM models, the experiments are conducted by using ChatGPT7 and LLAMA 3.1.8 For GPT models, the tests are performed using OpenAI’s API batch processing with models such as GPT-4 and GPT-3.5-turbo-0125. The LLAMA models are evaluated using the llama-api, with experiments comparing LLAMA 3.1-70B and LLAMA 3.1-8B. These comparative tests are conducted to evaluate the performance of each model under consistent conditions, thereby confirming the applicability of our proposed method.

2) Performance Comparison By Error Rate
Since the framework involves generating descriptions using ontology restrictions for verification, an experiment are conducted to assess how the error rate within the restrictions affects the verification performance. To this end, error rates are set at 10%, 20%, and 40%, and datasets were prepared using the error generation methods outlined in the experimental setup. This allows for a comprehensive analysis of the impact of varying levels of intentional errors on the framework’s robustness to detect them.

3) Performance Comparison Across Clustering Techniques
Two prominent methods for estimating the optimal number of clusters are the Elbow method [42] and the Silhouette method [41]. The Elbow method calculates within-cluster variance and identifies the point at which the rate of variance reduction sharply decreases, selecting this as the optimal number of clusters. In contrast, the Silhouette method evaluates both cohesion within clusters and separation between clusters, determining the optimal number of clusters based on the highest Silhouette score. Using both techniques, we determined the optimal number of clusters, which were then used to generate descriptions. With this comparison, we analyze the impact of clustering methods on ontology validation performance.

4) Performance Comparison with Existing Study
In previous research [12], verification of the misuse of ontology constraints is conducted. Therefore, the same dataset (90 samples from the Pizza ontology dataset) used in the existing study are utilized for the experiments. The approach involves extracting data represented using the Rector technique from the original dataset and performing clustering. The optimal number of clusters is determined to be 4. Using this, axiom descriptions and ontology descriptions were generated, and verification is performed on 15 misuse dataset samples.

5) Ablation Study
The primary hypotheses of this study are twofold: first, the LLMs would more accurately verify misuse of constraints when descriptions are provided as input; second, these descriptions would yield better verification performance when generated by clustering the text embeddings of the restrictions. To test these assumptions, two specific ablation experiments are conducted.

a: Performance Comparison Without Descriptions
To evaluate the impact of descriptions on the verification process, experiments are carried out by selectively removing the descriptions from the input. We compared the performance across following scenarios where (1) only the ontology or restrictions are used without descriptions, (2) both are used without descriptions, and (3) both ontology and restriction inputs included descriptions.

b: Performance Comparison Without Clustering
To analyze the role of clustering, the experiments are adjusted to remove the clustering process altogether. In this scenario, descriptions are generated from all the text within the ontology at once, combining the ontology descriptions and axiom descriptions without segmenting through clustering. These comprehensive descriptions are then used as input for the verification, and the performance is compared to evaluate how the absence of clustering impacted the results.

C. Results
1) Performance Comparison Across LLM Models
The performance comparison across various LLMs reveals important insights regarding the influence of model architecture, parameter count, and training advancements on task performance. In particular, we analyze how our proposed method leverage state-of-the-art models like LLAMA and GPT to highlight its strengths and potential advantages in various ontologies. Below, additional analyses are provided to strengthen the interpretation of the results (Table 2):

TABLE 2 Performance Comparison Across Large Language Models
Table 2- Performance Comparison Across Large Language Models
a: Parameter Count and Model Performance
The results consistently demonstrate that models with a larger number of parameters tend to outperform their smaller counterparts. GPT-4 and LLAMA-70B, which have the highest parameter counts among the evaluated models, exhibit significantly higher average performance scores (82.9 and 73.2, respectively) compared to GPT-3.5 (64.7) and LLAMA-8B (47.1). This finding aligns with the hypothesis that larger models have greater capacity to capture and utilize complex patterns in data, enhancing their reasoning and inference abilities.

b: Impact of Model Architecture
The performance across ontology types highlights interesting task-specific trends

Type1 tasks: GPT-4 leads in this category, followed by LLAMA-70B. This suggests that GPT-4 excels in tasks requiring high-level logical reasoning and structural understanding.

Type2 tasks: LLAMA-70B slightly narrows the performance gap with GPT-4 in these tasks, which may involve domain-specific constraints or patterns.

Type3 tasks: Performance is generally consistent across all models, indicating that this task type might involve simpler or more constrained challenges, reducing the gap between high- and low-performing models.

c: Release Date and Technological Advancements
The correlation between release dates and performance highlights the importance of continual advancements in model training techniques.

GPT-4, the most recent model, shows substantial improvements over GPT-3.5, reaffirming that better models are generally more effective in ontology validation.

LLAMA series models, despite being released in the same timeframe as GPT-4, trail behind, suggesting that different training methods or strategies for language models can result in different ontology validation performance.

These findings highlight the importance of scaling model parameters and incorporating the latest advancements and appropriate models by considering the training methodologies to improve the performance of LLMs in ontology-related applications.

2) Performance Comparison by Error Rate
The results(table 3) provide insights into the impact of error rates on the verification performance of the proposed method. Despite the introduction of varying error rates (10%, 20%, 40%) within constraints, the overall performance remained consistent, demonstrating the robustness of the method. Below is a detailed analysis of the findings:

TABLE 3 Performance Comparison By Error Rate
Table 3- Performance Comparison By Error Rate
a: Performance Stability Across Error Rates
The overall performance remains stable across error rates, with average total scores of 82.9 (10%), 84.2 (20%), and 81.1 (40%). This suggests that the proposed method effectively utilizes contextual information and clustering to mitigate the impact of errors in constraints.

b: Ontology-Specific Trends
Performance variations across individual ontologies reveal notable patterns:

Pizza Ontology: Performance remains high and consistent, with scores of 88.3, 86.1, and 89.2 for 10%, 20%, and 40% error rates, respectively. This indicates that the method handles this ontology well, possibly due to its structured relationships.

SSN Ontology: A significant drop in performance is observed at 40% error rate (64.6), compared to 83.3 at 10%. This suggests that SSN is more sensitive to errors, potentially due to complex interdependencies within the constraints.

DemCare Ontology: Interestingly, performance improves slightly as error rates increase, particularly for Type2 tasks (87 at 10% to 95.9 at 40%). This indicates that the method may leverage noisy data effectively, using clustering to enhance contextual understanding.

c: Impact on Task Types
Performance across task types highlights the following:

Type1 Tasks: Performance remains relatively stable, ranging from 81.1 to 87, showcasing the method’s ability to handle logical reasoning even with noisy constraints.

Type2 Tasks: Variability is observed, with a peak average performance at 20% error rate (80.3). This indicates that Type 2 tasks have different characteristics for error rates than other tasks. One possible explanation is that, with a certain level of errors, the description generation process provides the right amount of diversity, resulting in better quality ontology and axiom descriptions.

Type3 Tasks: Performance is consistent across all error rates (83.3), indicating these tasks are less sensitive to errors or rely on simpler constraints.

d: Optimal Error Tolerance
The peak performance observed at 20% error rate (84.2) suggests an optimal balance where clustering benefits from diverse inputs while managing the noise. This highlights the method’s capacity to maintain high performance in real-world scenarios with imperfect constraints.

The proposed method shows strong robustness to errors, maintaining high performance even at higher error rates. Performance differences across ontologies highlight the potential for domain-specific optimizations, while the peak at a 20% error rate suggests clustering effectively leverages moderate noise. We speculate that the moderate error rate facilitated the utilization of the LLMs’ reasoning capabilities during the description generation and determining process. When presented with inputs containing a mixture of correct and erroneous information, the LLMs likely reprocess the data independently, resulting in descriptions that more accurately captured essential information. Stability in simpler tasks and variability in complex ones underline the need to account for task complexity in verification design. These findings confirm the method’s adaptability across diverse ontologies and conditions.

e: Analysis of Fluctuation on Each Error Rate
The experimental results presented in Table 3 illustrate variability across different error rates. For instance, in the case of DemCare, optimal performance was achieved at a 40% error rate, while overall performance peaked at a 20% error rate. Although efforts were made to reduce variability through random sampling during the experimental setup, several factors could contribute to the observed fluctuations.

First, the used ontologies in our experiments are relatively small-scale, with a limited number of restrictions. Consequently, some inherent variability is unavoidable. Specifically, corruption of a critical axiom that effectively defines the ontology’s domain based on our error-generation method could significantly alter clustering outcomes, thereby substantially impacting performance.

Second, the employed LLMs may possess intrinsic knowledge of each ontology’s domain. Consequently, variations in performance can result from how the LLMs’ internal knowledge interacts with artificially introduced errors.

Despite these factors, Table 3 primarily serves to demonstrate that ontology verification remains robust under diverse conditions. Notably, our proposed method exhibits minimal overall performance variance across the tested error rates, showing its reliability and stability in handling varied error scenarios.

3) Performance Comparison Across Clustering Techniques
We compared the performance of two clustering techniques, Elbow and Silhouette, focusing on their ability to determine the optimal number of clusters and their impact on verification performance. Below is an in-depth analysis of the findings:

a: Performance Superiority of the Silhouette Method
The Silhouette method consistently outperformed the Elbow method, achieving an overall score of 82.9 compared to 84.2 for Elbow (Table 4). Key observations include:

Internal Cohesion and Separation: The Silhouette method demonstrated better internal cohesion and inter-cluster separation, effectively clustering related data points and leading to higher verification performance.

Task Types: The Silhouette method maintained stability across task types (Type1: 87, Type2: 78.4, Type3: 83.3), while the Elbow method showed greater variability, particularly in Type2 tasks (62.7).

TABLE 4 Performance Comparison Across Different Clustering Methods
Table 4- Performance Comparison Across Different Clustering Methods
However, solely relying on approaches such as the Silhouette method and other intra-cluster-focused methods might result in clusters whose shapes and boundaries do not accurately reflect optimal values for individual axiom groups. Therefore, a detailed investigation into optimizing cluster shapes and boundaries will be addressed in future research.

b: Optimal Number of Clusters
The Silhouette method generally identifies a much higher number of clusters compared to the Elbow method (Table 5). This highlights the Silhouette method’s ability to reveal meaningful structures in diverse and complex datasets. Specifically, based on the results presented in Table 4 and Table 5, it is observed that methods producing too few clusters, such as the Elbow method, do not significantly improve validation performance. Our experiments reveal that ontologies, each tailored to specific domains, inherently contain contextually similar axioms, resulting in closely aligned embeddings. Consequently, clustering techniques emphasizing intra-cluster distances, like the Elbow method, tend to yield fewer clusters. Therefore, future research should investigate and determine optimal clustering methodologies and optimization strategies to further enhance ontology validation effectiveness.

TABLE 5 Optimal Number of Clusters Determined by Elbow and Silhouette Methods
Table 5- Optimal Number of Clusters Determined by Elbow and Silhouette Methods
TABLE 6 Performance Comparison With Existing Study
Table 6- Performance Comparison With Existing Study
TABLE 7 Performance Comparison Without Descriptions
Table 7- Performance Comparison Without Descriptions
TABLE 8 Performance Comparison Without Clustering
Table 8- Performance Comparison Without Clustering
c: Visualization Insights
The clustering visualizations(Fig. 6) highlight the effectiveness of the Silhouette method across different ontologies, showcasing its adaptability to varying complexity and domain-specific characteristics. For SSN ontology, the clusters are distinct and well-separated, indicating strong internal cohesion. This reflects the method’s ability to precisely group related data, which is critical for semantic tasks in sensor networks. In Pizza ontology, a larger number of clusters are observed, capturing fine-grained relationships between concepts. The method effectively handles the higher granularity of this dataset, ensuring closely related entities are grouped together. ChEMBL ontology displays clusters primarily divided into two main regions, reflecting its hierarchical structure. The clear separation between regions and compact clusters within them demonstrate the method’s capability to manage both high-level structure and detailed relationships. For Doremus ontology, the visualization shows numerous small, well-defined clusters, capturing the subtle and nuanced relationships in cultural and musicological data. The method excels in identifying these intricate connections. In DemAware ontology, the clusters are more dispersed, reflecting the high variability and heterogeneity of the dataset. Despite this, the method maintains clear separation, demonstrating robustness in handling noisy and diverse data.

FIGURE 6. - Clustering visualization results for each ontology.
FIGURE 6.
Clustering visualization results for each ontology.

Show All

The Silhouette method consistently produces well-defined clusters, demonstrating adaptability across diverse datasets, from compact clusters in SSN to granular ones in Pizza and Doremus. It excels in capturing meaningful groupings for various domains, including hierarchical, and heterogeneous data, making it a reliable and versatile choice for ontology verification tasks.

d: Task-Specific Performance Trends
The Silhouette method outperformed the Elbow method across task types:

Type1 Tasks: Both methods show strong performance, but the Silhouette method has an edge (87 vs. 81.6), suggesting its suitability for tasks involving logical reasoning.

Type2 Tasks: The Silhouette method achieves significantly higher scores (78.4 vs. 62.7), highlighting its robustness in handling domain-specific constraints.

Type3 Tasks: The Silhouette method maintain consistent performance (83.3), whereas the Elbow method struggle with stability (66.7).

The Silhouette method outperforms the Elbow method due to its ability to calculate both internal cohesion and inter-cluster separation, resulting in more meaningful and precise clusters. This advantage makes the Silhouette method particularly effective for complex and nuanced datasets, while the Elbow method’s simplicity and computational efficiency may still make it suitable for smaller or less complex datasets. Overall, the Silhouette method demonstrates superior performance in clustering-based verification tasks.

4) Performance Comparison with Existing Study
Experimental results using the dataset from previous studies [12] showed that our methodology achieves an accuracy of 86.7, outperforming the existing approach, which has a result of 73.3. Notably, even for constraints expressed in Turtle (TTL), our method demonstrates better performance when a description is provided. However, this result should be interpreted cautiously, as only five samples are available for each expression format, leading to a limited scope of experimentation. Therefore, it cannot be conclusively stated that TTL expressions yield better verification accuracy.

5) Ablation Study
a: Performance Comparison Without Descriptions
In Ablation Study 1, the verification performance is compared when the ontology description and axiom description are each removed individually, as well as when both are removed. The experimental results show that providing all descriptions as input led to the highest verification accuracy. Notably, the scenario where only the axiom description is provided outperformed the scenario where only the ontology description is used. These findings suggest that the ability to reference the context in which a given restriction is applied, through the use of descriptions, allows for more accurate verification. Therefore, utilizing both the ontology and axiom descriptions contributes to improved verification performance.

Specifically, these results suggest that relying exclusively on a zero-shot LLM approach is inadequate for precise ontology validation. Ontologies inherently encapsulate detailed and structured domain-specific knowledge, with representations varying according to their intended applications. Consequently, without explicitly provided contextual descriptions, LLMs face significant challenges in accurately interpreting ontology constraints. Thus, they may fail to fully capture the objectives and semantics embedded within ontological structures. Future research can incorporate explicit contextual information to enhance LLM performance in ontology validation tasks.

b: Performance Comparison Without Clustering
In Ablation Study 2, the change in performance is analyzed when clustering is removed. The results show that the model’s performance tends to decrease when clustering is omitted. Through clustering, semantically similar axioms are effectively grouped, enabling descriptions generated by the LLMs to achieve an optimal balance between specificity and generality. This approach ensures that the resulting axiom descriptions are both precise enough to convey detailed meaning and sufficiently general to capture broader semantic relationships. Consequently, these balanced descriptions facilitate accurate ontology validation. By leveraging this approach, our experiments demonstrate enhanced performance in ontology validation tasks, underscoring the value of tailored clustering methodologies in improving the accuracy and effectiveness of LLM-based ontology verification processes. In other words, this can be interpreted as evidence that clustering helps to generate more refined axiom descriptions, and these more precise representations positively impact verification performance. Therefore, the clustering technique can be considered a crucial component for enhancing the performance of the proposed framework.

SECTION V.Conclusion
A. Contributions
This study proposes a method that enables more accurate verification by utilizing ontology and axiom descriptions. Specifically, the approach involves classifying restrictions using clustering techniques, which helps generate more refined descriptions, leading to improved performance. Experimental results confirm that even when the error rate increased, the content of the descriptions remained largely consistent, and the verification performance did not degrade.

Furthermore, this study presents a method for automatically verifying the misuse of ontology constraints. By leveraging LLMs, an automated verification method is developed, with the following three key contributions:

Proposal of an Automated Method for Verifying Ontology Constraints: We improve upon traditional manual verification processes by developing a system that automatically detects and verifies the misuse of ontology constraints using LLMs. This significantly enhances the efficiency and accuracy of the verification process.

Confirmation of the Importance of descriptions for Verification Accuracy: Through experiments, it is demonstrated that descriptions play a crucial role in the verification process. In particular, axiom descriptions help achieve a more accurate understanding of the contextual meaning of constraints, leading to improved verification accuracy, as evidenced by experimental results.

Clustering-Based Approach for Generating Refined Descriptions: To generate more precise descriptions, a method is proposed that involves clustering the content of restrictions to extract common contextual information. This clustering-based approach contributes to creating descriptions that could more effectively explain a variety of constraints.

B. Future Research Directions
This study introduces a novel LLM-based approach for ontology constraint verification, emphasizing the role of semantic descriptions in improving verification accuracy. By leveraging detailed descriptions, our proposed method demonstrates significant improvements in understanding the contextual meaning of constraints. However, two critical issues and limitations are identified, pointing to areas for future research.

First, when descriptions are inaccurately or incompletely generated, they distort the meaning of constraints and lead to incorrect verification results. This underscores the need for a robust process to assess and ensure the quality of descriptions prior to their use. Without such measures, the reliability of the method may be compromised in real-world applications.

Second, the proposed approach is limited in its ability to identify or generate missing concepts within ontologies. Ontology management requires not only verification but also the continuous addition and refinement of concepts to reflect changes in domain knowledge. The lack of a mechanism to detect and incorporate missing elements reduces the method’s applicability to dynamic and evolving ontologies.

To address these limitations, future research will focus on two key directions. First, a quality assurance framework for generated descriptions will be developed to improve the reliability and accuracy of constraint verification. This includes an examination of clustering methods, highlighting the necessity of refining these techniques by taking into account the distinct characteristics of each ontology. Further investigation is required to analyze clusters from multiple perspectives and utilize these insights for generating comprehensive descriptions. This could involve additional verification steps, such as leveraging multiple LLMs or integrating domain-specific knowledge bases to cross-check and refine descriptions. Second, the method will be expanded to include functionality for identifying and generating missing concepts. By incorporating techniques for automatic ontology extension and adaptation, the approach can evolve to support not only verification but also the growth and refinement of ontologies over time.

In conclusion, while this study has made progress in improving ontology constraint verification using LLMs, addressing these challenges will allow the method to better support the full lifecycle of ontology management. Expanding the approach to include description quality assurance and ontology extension will enhance its utility, scalability, and applicability across diverse domains.