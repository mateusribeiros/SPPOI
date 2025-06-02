Title: Automated Text Structuring: Natural Language Processing and Regular Expressions in XML Tag Filling

ABSTRACT The conversion of documents into XML markup requires efficient algorithms and automated
solutions. The focus is on tagging documents to meet NISO STS standards, ensuring compatibility across
systems. A method combining Natural Language Processing (NLP) and Regular Expressions (regex)
for automated XML tag filling is proposed. NLP enhances content understanding, while regex enables
precise pattern matching. This approach streamlines the conversion process, reducing manual effort and
ensuring standardized tagging. Through experiments, the effectiveness of the method in achieving accurate
XML markup aligned with NISO STS guidelines is validated. This research advances automated data
structuring, exemplified by the GOST R ontology within NISO STS standards, providing a template for
other ontology-based document XML-structuring.
INDEX TERMS XML, automated structuring, natural language processing, regular expressions.
I. INTRODUCTION
The structured representation of textual data in XML
(eXtensible Markup Language) format is a key factor for
effective data management, sharing, and analysis across
different systems and platforms. As the volume of documents
needing conversion to XML markup increases, the demand
for automated solutions and standardized tagging practices
has grown. One such standard gaining prominence is the
NISO STS (National Information Standards Organization
Standards Tag Suite) [1], which provides guidelines for
structuring scholarly texts in XML, facilitating standardized
formatting and interoperability across various platforms and
systems.
When converting documents to XML, several challenges
can arise. These include dealing with various document
formats [2] such as PDF, DOCX, DOC, and EPUB, ect. each
with its own structure and encoding. To address this, it is
necessary to use robust parsers and converters for each format
to accurately extract content and metadata. Another issue is
the presence of complex structures within documents [3],
such as nested elements, tables, figures, footnotes, and crossreferences. Developing advanced algorithms to recognize
and correctly interpret these structures can ensure accurate
representation in XML.
Inconsistent formatting and styles [4] within documents
can further complicate the conversion process, leading to
incorrect tagging or loss of information. This can be mitigated
by utilizing machine learning techniques to detect and
standardize diverse formatting and styles before conversion.
Additionally, there is the problem of semantic information
loss [5], where the meaning of the document content may not
be preserved during conversion to XML. Employing natural
language processing (NLP) methods can help maintain
semantic integrity and accurately map document content to
XML tags.
Documents may also contain embedded objects such as
images [6], charts, and multimedia, which can be challenging
to convert into XML. Creating specialized routines to
accurately extract and encode these embedded objects within
the XML structure is a key component of any XML extractor.
To ensure that the converted XML document maintains
the integrity and fidelity of the original document, implementing rigorous validation and verification processes [7]
is necessary. This involves comparing the converted XML
with the original document, identifying, and correcting
discrepancies. Another challenge is converting large volumes
of documents [2] efficiently without compromising on
quality. This may require parallel processing and cloud-based
solutions to handle large-scale conversions, optimizing both
speed and accuracy.
The conversion task has applications across different
industries, each of which may require customized XML
frameworks [8] and specific tagging conventions. Designing
a flexible conversion framework that allows for customization
and easy adaptation to various XML frameworks and
standards is essential. Ideally, the goal is to fully automate
the conversion process [9] while minimizing the need for
manual intervention. This requires developing sophisticated
automation tools and workflows capable of handling the
entire conversion process autonomously, with minimal
human oversight.
This paper addresses the automation of XML tag generation for documents in the catalog based on the Russian
State Standards (GOST R), with a particular emphasis on
compliance with NISO STS standards. The ontology of
GOST R documents includes certifications that confirm
the compliance of various products with state standards.
Given the extensive application of these standards, there is
a large volume of documents—totaling 51,037 units [10]—
that require organization, as certification is mandatory for
numerous goods and services. Structuring this collection
effectively necessitates converting the documents into XML
format.
To address this challenge, an approach is proposed
that integrates NLP techniques with Regular Expressions
(regex) to streamline the document tagging process. NLP
enhances the capability to comprehend textual content, while
regex offers robust pattern-matching functionalities, ensuring
accurate and standardized tagging.
By leveraging this combined approach, the methodology
aims to minimize manual effort and maintain consistency in
XML markup, adhering to NISO STS standards. Practical
examples and experiments illustrate the effectiveness of this
approach in achieving precise and reliable XML tagging.
This research contributes to advancing automated data
structuring methodologies, specifically tailored to fulfill the
requirements of XML tagging within the context of NISO
STS guidelines.
To guide the reader through the exploration of these topics,
a structured outline of the paper is provided. In Section II,
the related work in the field is examined, providing context
for the study. Section III outlines the methodology, detailing
the techniques employed for data collection and analysis.
The results of the experiments and their implications are
highlighted in Section IV. In Section V, conclusions are
drawn from the findings, and in Section VI, avenues for future
research are discussed.
II. RELATED WORKS
XML is an integral component in structured data processing,
playing a key role in information exchange and storage [11].
Methods and technologies related to XML usage are
extensively discussed in scientific literature, reflecting its
significance in the contemporary information landscape.
For instance, Kurgan et al. [12] introduces XMapper,
a system for generating semantic mappings between XML
sources within the same domain. XMapper stands out for
its reliance on standalone XML documents and its use of
machine learning to enhance accuracy, especially in complex
domains. Experimental results confirm XMapper’s ability
to produce highly accurate mappings, enabling seamless
integration of XML data sources for unified information
processing across applications. XML’s role in structuring and
describing data relationships makes it widely utilized across
industries and computer science disciplines, including data
mining and knowledge discovery.
Morishima et al. Introducing XLearner, a novel tool
for rapidly developing XML mapping queries written in
XQuery [13]. It learns queries from provided examples of
intended results, minimizing user interactions. By integrating
machine learning techniques and addressing XQuery-specific
challenges, XLearner efficiently generates complex queries.
Experimental results demonstrate its effectiveness in producing sophisticated queries, offering an advancement in XML
data integration and restructuring tools.
Public archives hold extensive text data, legally required
for public access. Semantically tagged XML documents
enable efficient searching, but transforming legacy text is
laborious. Winkler and Spiliopoulou [14] proposes DIAsDEM framework semi-automates semantic tagging, grouping
text units, deriving labels, and generating XML DTDs.
They apply DIAsDEM to Commercial Register archives,
enhancing data accessibility and quality.
Liu et al. [15] introduces an automatic method for inferring
tag weights in XML retrieval. By investigating 15 tagrelated features, authors select five based on correlations with
manual tag weights. Their model, ATG, assigns tag weights
using these features. Evaluation on real datasets (IEEECS and
Wikipedia) demonstrates ATG’s effectiveness. Results show
high correlation between ATG-generated weights and manual
weights, indicating improved retrieval performance.
Web services can implement Service-Oriented Architecture (SOA) applications, but the sheer volume of available
services makes finding the right one difficult. Manual tagging, a common method for organizing services, is laborious
and prone to errors. Azmeh et al. [16] suggests a solution:
automatically tagging web services using text mining and
machine learning techniques applied to WSDL [17] descriptions. By extracting and enriching tags with synonyms
from WordNet, their approach simplifies service discovery. Validation on 146 services from Seekda confirms its
effectiveness.
The proliferation of heterogeneous XML documents
underscores the need for efficient XML transformations.
Current manual mapping methods face scalability and
semantic matching challenges. To address these issues,
Boukottaya et al. [18] propose the Layered Interoperability
Model for XML Schemas (LIMXS), offering a semantic
view of XML schemas to automate transformation processes dynamically and incrementally. LIMXS resolves
the limitations of existing algorithms and advocates for
conceptual modeling as a solution. Their approach promises
to streamline XML transformations and enhance scalability.
The realization of the Semantic Web hinges on interpreting
XML data with respect to ontologies, necessitating semantic
mappings between XML schemas and ontologies. Heuristic
approach to construct complex mappings from simple
correspondences, reducing effort has been presented by
An et al. [19]. This method employs a mapping formalism
to capture XML schema semantics and a heuristic algorithm
for mapping construction. Empirical results demonstrate
substantial time savings when using this prototype tool for
complex mapping construction.
A schema matching method for XML document transformation introduced by Lee and Lee [20], comprising two
steps: preliminary matching of leaf nodes based on ontology
and leaf node similarity, and extraction of final matchings
using path similarity. The proposed method incorporates
user feedback to incrementally update the ontology, enabling
computation of both simple and complex matchings.
Agreement exists on the need to address data semantics
for machine-processable XML data. However, creating
mappings between XML schemas and ontologies is laborious
and error-prone. To streamline this, a heuristic solution
proposed by An et al. [21] for automated mapping discovery
based on initial correspondences. This approach generates
mapping formulas and facilitates consistency maintenance
as schemas and ontologies evolve. Through empirical study,
it demonstrates efficiency gains and propose a maintenance
plan for schema evolution. This work offers effective solutions for building sustainable semantic integration systems
for XML data.
Efficiently mapping XML data to relational databases
is critical for leveraging XML technology. While schema
and query mapping have been extensively studied, the
task of mapping XML data to relational data has received
less attention. Atay et al. [22] proposes a linear algorithm,
XInsert, to translate XML INSERT statements into SQL
INSERT statements. Building upon the previous schema
mapping work, XInsert efficiently handles this task.
The extraction of information from documents with subsequent structuring into XML format is actively discussed in the
scientific literature. Rausch et al. [23] presents ‘‘DocParser,’’
an end-to-end system for parsing hierarchical document
structures. It introduces a dataset for evaluation and a scalable
learning framework for settings with limited data. Empirical
results show improvements in document entity detection
and hierarchical relation classification. This addresses the
challenge of inferring complete document structures from
renderings, essential for various NLP tasks, given prevalent
file formats lacking hierarchical information.
Ma et al. [24] introduce a task of hierarchical reconstruction for document structures, particularly focusing on
multi-page documents. They present HRDoc, a large dataset
with line-level annotations, and propose a hierarchical
document structure parsing system (DSPS) that outperforms
baseline methods. This work aims to advance understanding
and performance in reconstructing hierarchical document
structures.
Document AI has emerged as a vital research area encompassing automated reading, understanding, and analysis of
business documents. Cui et al. [25] provide an overview of
Document AI, highlighting its significance in NLP and
computer vision. It explores the advancements driven by
deep learning, including document layout analysis, visual
information extraction, and document image classification.
Capraro et al. [26] propose an approach emphasizes
the linguistic aspects of decision-making. Using sentiment
analysis, it becomes possible to automatically detect and
analyze the emotional tone of text within documents.
Aumiller et al. [27] propose a novel method for structural
text segmentation, particularly suited for legal documents.
Current systems often miss the semantic coherence of
text segments, leading to suboptimal representations. Their
approach, based on transformer networks, predicts the topical
coherence of sequential text segments spanning multiple
paragraphs. It outperforms baselines, adapts well to legal
document complexities, and simplifies training by framing
the task as a series of independent binary predictions.
Table 1 provides summary of limitations of mentioned
works.
The contribution of this article lies in the introduction
of an approach that integrates the segmentation of textual
information from documents using NLP techniques and
regex, followed by hierarchical XML structuring based on a
specified ontology that complies with NISO STS standards.
This integrated approach facilitates the effective extraction
of structured data from documents while taking into account
their context and specificity, thereby distinguishing this work
from existing research in the field.
III. MATERIALS AND METHODS
A. EXPERIMENTAL PIPELINE
The task of assigning tags to GOST documents is addressed
in this study. Tagging is outlined for one ontological model
TABLE 1. Summary of document processing studies.
of the document - GOST R. Input data consists of a
PDF document with a text layer. To structure the text
with NISO STS 1.2 tags, a hierarchy of tags is used to
divide the document into sections and subsections. Python
programming language with various libraries is utilized
for preparing data for further processing. Thanks to the
standardized structure of GOST R documents, a model has
been created that most effectively addresses the task at hand.
Fig. 1 presents a schematic representation of the tagging
pipeline process utilized for text documents in this study. The
methodology is tailored for documents that contain a text
layer. The red line in the figure indicates that for documents
lacking a textual layer, i.e., where text is embedded within
images, additional optical character recognition (OCR) is
required to extract the textual layer.
The task involves several stages. First, the PDF document
needs to be obtained. Next, it’s necessary to determine if the
PDF contains a text layer. If not, recognition mechanisms
must be employed to ensure the preservation of the original
PDF file structure without a text layer. Then, the ontological
model of the document needs to be identified, whether it
belongs to GOST R, SP, or others. Afterward, the PDF
document must be converted to DOCX format using the
‘pythondocx’ open-source library. Following this, all images
from the obtained DOCX file should be saved into a separate
folder. Subsequently, a ‘‘default’’ XML file based on the
DOCX document needs to be created, containing all styles
FIGURE 1. Schematic representation of the tagging pipeline process for
text document.
for each line in the document. Finally, the ‘‘default’’ XML
file must be converted to an XML file corresponding to the
structure of NISO STS 1.2.
For the creation of the final script, the following modules
were utilized:
1) xml.etree.ElementTree module - for creating
and structuring XML tags. (Built into Python by
default, described in [28])
2) Converter module from the pdf2docx library -
an open-source library used for converting PDF
documents to DOCX format. (Described in [29])
3) python-docx library - for creating the default XML.
(Open-source library, described in [30])
4) re library - for searching for specific expressions in the
text. (Built into Python by default, described in [31])
5) zipfile library - for extracting all images from
DOCX files. (Built into Python by default, described
in [32])
6) os library - for creating new files and folders,
necessary for batch processing of PDF documents.
(Built into Python by default, described in [33])
7) Image module from the PIL library - for image
manipulation. (Built into Python by default, described
in [34])
8) datetime module from the datetime library -
used for date processing. (Built into Python by default,
described in [35])
9) translate module from the Translator library -
for translating certain tags to English. (Open-source
library, works without an API, described in [36])
B. DOCX TO ‘‘DEFAULT’’ XML CONVERSION
While python-docx does not directly convert PDF
documents to XML format like some other libraries, it offers
several advantages for working with Word documents.
At first, it specifically designed to handle .docx documents
and provides comprehensive support for various text formatting features such as font styles, colors, bullet points,
tables, and more, ensuring that the converted XML retains
the original formatting of the Word document. At second,
it preserves the hierarchical structure of the Word document,
including sections, paragraphs, headers, footers, and other
elements. This ensures that the resulting XML maintains the
intended document structure.
By preserving the structure of the original document text
using this library, conversion to XML according to a specified
ontology becomes feasible.
The purpose of this step is to accurately convey the styles
and structure utilized for each line and paragraph in the
docx document. Currently, there are no methods available to
directly convert docx to NISO STS XML styles. Therefore,
creating such default XML is an excellent intermediary step
in this conversion process. The default XML attributes for
each line and/or paragraph of the docx document include
parameters such as font, font size, boldness, italics, underline,
alignment, and leading. Additionally, it is important to
maintain the sequential tag number (line_number) in the
default XML to aid in structuring the file into sections.
Next, the actual default XML file must be created.
Besides lines or paragraphs, documents may contain tables
and images. Understanding the table structure—such as
the number of rows and columns and their orientation—is
important, especially for documents with many tables. This
knowledge aids in processing complex tables, as large tables
often lead to unsatisfactory XML structures. However, the
current system effectively manages tables that serve as frames
for definitions or citations from the reference list.
Fig. 2 a) displays a snippet extracted from a document
formatted in DOCX, conforming to the GOST standard.
Additionally, Fig. 2 b) and c) illustrate the initiation and
continuation, respectively, of the highlighted segment of
the document in the default XML format. Each line in
the XML representation is characterized by attributes such
as text line_number, indent, leading, alignment, underline,
italic, bold, font_size, and font, as specified. This comparison
visually showcases the transformation process from the
original DOCX document to its XML representation.
C. ‘‘DEFAULT’’ XML TO XML CONVERSION ACCORDING TO
NISO STS
Developing a function to convert default XML into XML
adhering to NISO STS styles poses a challenge, yet script has
demonstrated proficiency in handling this task, particularly
with GOST R documents. This endeavor can be delineated
into several key stages: firstly, establishing the framework
of the tag structure, identifying fixed tags applicable across
all documents and dynamic tags contingent upon documentspecific attributes. Secondly, organizing text content within
predetermined tags. Thirdly, assigning appropriate tags to
accommodate variable content. Lastly, implementing checks
to ensure the absence of empty tags and maintaining
structural integrity.
Primary tag structure in these documents:
<standard xmlns:tbx="urn:iso:std:iso:
30042:ed-1" xmlns:svg="http://...">
Following are the three main sub-tags:
1) <front> - contains all metadata related to the document (these tags remain constant for any GOST R).
2) <body> - includes all textual information from the
document (these tags vary depending on the number of
sections).
3) <back> - encompasses all appendices and bibliographic references from the document (these tags also
vary depending on the number of sections).
The document structure for the ontological model of GOST
R is depicted in Fig. 3
The tagging process for the <front> section involved
mapping from the default XML to XML corresponding to
the ontological model of the processed document (in this
case, GOST R). The mapping process was executed with
code resembling the following example, demonstrating the
population of the <intro> tag. Specifically, this pertains
to extracting the title of the current metrological standard
document, GOST R, from its cover page.
if (text_element.get(’font’) ==
’Arial’ &
text_element.get(’font_size’) ==
FIGURE 2. a) Fragment of a document in DOCX format according to the GOST standard, while figures b) and c) depict the beginning and continuation of
the highlighted section of the document in the generated default XML, where attributes such as text line_number, indent, leading, alignment, underline,
italic, bold, font_size, and font are specified for each line.
’18.0’ &
text_element.get(’bold’) == ’true’ &
text_element.get(’italic’) ==
’false’ &
text_element.get(’underline’) ==
’false’ &
text_element.get(’alignment’) ==
’left’ &
text_element.get(’leading’) ==
’12.25’ &
text_element.get(’indent’) == ’67.8’):
# Extract the text content from the
<text>
# tag and add it to <intro>
text_content = text_element.text
intro.text = text_content
This approach assumes uniform styling across all documents converted from PDF with a text layer to DOCX.
Therefore, it is able populate the tags for the cover in this
manner.
Developing the processing logic to construct the <body>
and <back> structures posed a challenge, demanding an
approach to logic. The primary objective was to accurately
delineate the junctures marking the inception of new sections,
assign unique identifiers (id attributes) to these sections,
and ascertain the pertinent tags from the default XML
corresponding to each section.
The methodology employed involves iterating through the
section_texts, which is a list containing lines with section
attributes (also obtained using the method for locating the
<main> tag). Each section is encapsulated within <sec>
tags, and a unique id attribute is assigned to denote its
sequence. For each section, a <label> element containing
the section number is created to provide a structured
hierarchy. Utilizing regex, any leading numerical digits
are removed from the section text to ensure clarity and
conciseness. The processed section text is then populated
within the <title> (which belongs current <sec>)
element to succinctly represent the section’s content. Regular
expression patterns are defined to facilitate the identification
and matching of id attributes.
As result obtain base sections structure which shown in
Fig. 3c). The same logic is applied for locating appendices
within the document.
To delineating lines pertinent to various sections, an empty
dictionary was initialized to organize the line numbers
associated with each distinct section. Through systematic
iteration, it was paired adjacent numbers and establish the
corresponding mapping. This process involves determining
the start and end lines for each section, ensuring precise
demarcation. For the final section, a tailored approach is
employed, leveraging the last number in the sequence as the
end line. Subsequently, a list of line numbers was compiled
within each section, spanning from the start line to the
end line inclusively. These delineations are then cataloged
within the dictionary, associating each section identifier with
its respective line numbers. This meticulous orchestration
ensures a systematic and comprehensive organization of the
document’s content.
As a result, a list of line numbers was obtained indicating
the start of each section, along with a nested list containing
the lines belonging to each corresponding section. Example
of this is shown below:
[start_1, start_2, ... start_N,
start_A, start_B, ... start_Bbl]
sec_1: [sec1_1, sec1_2, sec1_x]
sec_2: [sec2_1, sec2_2, ... sec2_x]
...
sec_N: [sec10_1, sec10_2, ... sec10_x]
app_a: [app_a1, app_a2, ... app_ax]
app_b: [app_b1, app_b2, ... app_bx]
...
sec_bibl: [sec_bibl1, sec_bibl2,
... sec_biblx]
FIGURE 3. a) A schematic representation of the GOST R entire tag structure. b) and c) Screenshots of the collapsed view of the tag tree.
Further, a function was utilized to extract text based
on line numbers from the obtained lists in order to
populate the generated <sec>, <app> and <bibl> tags.
For this purpose, it was necessary to create individual
functions to handle each section according to its name.
For example, each of these sections, such as ‘‘Normative
References,’’ ‘‘Definitions,’’ ‘‘Appendix,’’ and ‘‘Bibliography,’’ had its own filling structure tailored to its specific characteristics. Examples of tagging are shown on
Fig. 4.
FIGURE 4. Fragment of Document Sections: a) Normative References and c) Definitions, Allocated to Tags According to NISO STS (Figures b) and d)).
Converting documents from PDF to DOCX and subsequently to XML involves distinct processes tailored to each
format’s characteristics. Converting from PDF to DOCX
retains the document’s overall appearance and organization,
making it suitable for further editing or presentation purposes
in a word processing environment. In contrast, converting
from DOCX to XML shifts the emphasis towards semantic
mapping and structured tagging. Here, the goal is to translate
the preserved structural elements and formatting details into
a structured XML format that accurately represents the
document’s semantic content.
The ‘‘default’’ XML file serves as the starting point for
converting documents into NISO STS 1.2 XML format. This
initial XML file captures the document’s structure and basic
semantic content, facilitating subsequent refinement to meet
the specific tagging and formatting requirements of NISO
STS 1.2. By providing a structured framework, it ensures
consistency and accuracy in the final XML output, essential
for maintaining scholarly and technical content standards
IV. RESULTS
A. METHODOLOGY FOR XML DOCUMENT STRUCTURING
The implemented methodology involves several key steps for
structuring XML documents in alignment with a predefined
ontology. The initial phase entails identifying specific
sections within the XML document relevant to terms and
references. Keywords associated with terms and references
are defined and utilized to efficiently locate these sections.
Leveraging the identified keywords, the algorithm extracts
the section IDs containing terms and references. This
strategic extraction ensures focused processing of pertinent
content within the XML document. Subsequently, the code
systematically traverses through the XML content line by
line for each identified section. Utilizing regular expression
patterns, it parses and extracts information such as labels,
definitions, and references from the textual data.
Within sections dedicated to terms, the algorithm meticulously extracts the label and definition of each term.
This information is structured into XML elements, ensuring
precise representation and systematic organization of terms
within the document. In sections pertaining to references,
the code identifies and formats the references according
to predefined patterns. It discriminates between various
reference types and ensures their accurate portrayal within
the XML structure. Special scenarios, such as footnotes and
appendix sections, are accommodated through specialized
logic. This ensures consistent formatting and lucidity across
the entire document, even in exceptional circumstances.
The processed text content is then diligently assigned
to designated XML elements, ensuring coherence with the
predefined ontology. Specific sections of the document
are updated with corresponding text, preserving coherence
and completeness. Finally, the modified XML structure is
encapsulated within a new XML tree and persistently saved
to a file. This ensures that the processed document accurately
reflects the specified ontology and stands ready for further
analysis or publication. Figure 5 illustrates the flowchart of
the proposed approach.
B. REGEX-BASED TAGGING
Regex serves as a tool for pattern matching and text manipulation. Regex were designed to capture specific linguistic
patterns and expressions, including dates, numerical values,
specialized terminology, and formatting conventions unique
to the domain of the documents.
While the NLP methods excel in understanding and
processing natural language text, regex offers specialized
capabilities for identifying and extracting specific textual
patterns or formats.
For instance, let’s consider the process of filling in the
document introduction date tag:
|<meta-date type="ratification">..
..</meta-date>|.
Here, an approach was adopted based on a correctly
populated database of tags containing introduction dates.
If the tag in the current document is either empty or
incorrectly filled, the regex scans the text for matches
resembling a date in the specified format YYYY-MM-DD,
or occurring after keywords like ‘‘introduction date,’’ and
adds this information to the tag accordingly. Numerical
values such as measurements, quantities, or codes were
targeted using regex patterns tailored to match specific
numeric formats or units commonly encountered in the
document domain. This facilitated the automated extraction
and tagging of numerical data, contributing to the overall
completeness and consistency of the tagged documents.
Specialized terminology unique to the domain was identified
through regex patterns designed to capture specific keywords,
phrases, or abbreviations relevant to the subject matter.
By recognizing and tagging these domain-specific terms,
the regex techniques enriched the semantic understanding
of the text and ensured the accurate representation of
domain-specific concepts. Moreover, regex patterns were
utilized to detect and handle formatting conventions inherent
to the document domain, such as citations, references,
and section headings. By identifying and processing these
structural elements, regex facilitated the organization and
categorization of textual content, contributing to the overall
clarity and coherence of the tagged documents.
The following regex patterns are utilized to capture specialized terminology and formatting conventions, contributing to document clarity. The first pattern,
r’\^(\d+(\.\d+)*)’, identifies numeric identifiers
at the beginning of lines, facilitating sectioning based on
numbered headings. For handling GOST references, the
pattern r’GOST+(?:ISO/IEC|R|R+ISO)?+[.
../-]*’.
ensure that standard identifiers are correctly formatted for
inclusion in the XML structure.
To identify terms, the pattern r’\^\d+(\.\d+)+’
matches terms that begin with a number followed by periods,
allowing for their proper extraction for further processing.
Additionally, the pattern r’\^(?:[A-Z]\.\d+)’ captures lines that start with a letter followed by a period and
digits, typically used to identify appendices.
For citation formats, the regex pattern r’\[(\d+)\]’
captures numeric citations enclosed in brackets, aiding in
reference linking within the document. Lastly, the general text
matching pattern r’\^\d+(\.\d+)+\s’ matches terms
with a numeric prefix, enabling the extraction of labels and
definitions from the text.
These regex patterns enhance document clarity by ensuring
that specialized terminology is accurately identified and
formatted, thereby improving the structural integrity of the
generated XML documents. Automating the extraction of
these elements allows for greater readability and organization, facilitating easier navigation and comprehension of
complex content.
C. NLP-BASED TAGGING
It was applied deep learning methods, particularly the BERT
(Bidirectional Encoder Representations from Transformers) [37], [38] model, for tagging the bibliography lists from
documents. Leveraging a pre-trained BERT model, trained
on vast amounts of textual data, enabled us to conduct text
tokenization aimed at identifying literature sources.
One aspect of this research was matching numerical
identifiers pertaining to literature sources with each of these
sources. For this purpose, each source was entered into a
dedicated section
<ref-list content-type="bibl" id="sec_bibl">,
where each source was assigned its own tag
<ref id="biblref_..">,
containing the numerical designation of the source
in square brackets, along with sub-tags <label>[..]
</label> and <element-citation> providing information about the source itself.
A similar approach was also employed in cases where the
standard text tag <p>, which could contain plain text from a
paragraph, was split into multiple consecutive <p> tags. This
occurred due to the segmentation of each new line during the
transformation of the document from docx format to default
XML, with each line being treated as a separate string with
its attributes. Consequently, these tags could not be identified
as quotations, footnotes, literature sources, or other elements.
BERT’s ability to determine the context of text [39] content
from tags by identifying analogies between two adjacent text
fragments helped identify missing headers or subheaders in
the text that were omitted during default XML conversion.
Additionally, it aided in recognizing whether the content
FIGURE 5. Flowchart illustrating the proposed approach.
of consecutive <p> tags formed a cohesive textual unit.
If identified as such, BERT consolidated them into a single
<p> tag.
D. ERROR ANALYSIS
Errors can occur during the tagging process according to
NISO STS, particularly in the <front> section, where some
tags may remain empty due to variations in source document
formatting or issues in PDF to DOCX conversion. The lack
of a text layer in PDFs increases the likelihood of formatting
errors.
One common challenge in automated text tagging is
accurately tagging tables to reflect their original structure,
often leading to technical errors. These errors can be
identified by comparing automatically tagged tables with
their manually tagged counterparts. Another issue involves
correctly associating figure captions with their corresponding
figures; misattributions can occur if captions are not properly
detected or linked.
To address these challenges, the proposed approach
compares automatically generated XML documents with
manually tagged versions, specifically assessing the similarity of tags within the <front> section using NLP methods.
This method ensures high accuracy by utilizing NLP
techniques to detect subtle differences between texts. The
automated comparison process saves significant time and
effort compared to manual verification and helps identify
hidden errors that may not be evident during superficial
analysis, improving overall document quality. Additionally,
regular use of this method enhances the quality of automatic
tagging and reduces future errors, utilizing the Natural
Language Toolkit (NLTK) for NLP processing.
Within the scope of this study, 27 manually tagged
documents were analyzed to conduct comparisons. Figure 6
showcases a quantitative analysis of tag completion specifically within the <body> section of these documents. The
figures depicted in the graph represent the count of accurately
filled tags, taking into account their occurrence across all
documents, and provide a comparison between the XML
generated through automated methods and the XML obtained
through manual tagging.
Accuracy and refinement of algorithms for automated tag
generation are evaluated by comparing information extracted
from tags generated by the proposed approach against manually created tags. This comparison employs two methods:
a straightforward character-by-character comparison [40]
FIGURE 6. Tag filling statistics for tags within <iso-meta> and
<nat-meta> belonging to the <body> section were gathered from
27 manually annotated documents by domain experts.
and the computation of Levenshtein distance [41] between
the texts of corresponding tags. The character-by-character
comparison provides a precise measure of text similarity,
while the Levenshtein distance indicates the extent of
variation between the manually annotated texts and those
produced by the automated tagging model. Fig. 7 presents the
average Levenshtein distances across the selected tag groups.
FIGURE 7. Average Levenshtein distance for incorrectly filled tags for tags
within <iso-meta> and <nat-meta> belonging to the <body> section.
If the Levenshtein distance was zero or the character-wise
comparison flagged the texts as similar, the tags were
considered comparable, and statistics were recorded in Fig. 6.
For documents with a non-zero Levenshtein distance, the
average distance was calculated and depicted in Fig. 7.
Non-zero Levenshtein distances often result from technical
errors, such as extra spaces or characters introduced during
text parsing into XML tags. Discrepancies, like the presence
of hyphens in tagged text that are absent in manually
annotated versions, help identify errors in the automated
tagging process. These discrepancies indicate areas where
the algorithm may need adjustments to improve tagging
accuracy.
Figure 8 ia a flowchart illustrating the iterative process for
refining automated tagging algorithms. The diagram outlines
the steps taken to identify discrepancies between manually
annotated and automatically generated tags, including error
analysis, expert feedback, algorithm adjustments, and evaluation of tagging accuracy. Conditional paths indicate actions
based on findings at each stage, facilitating continuous
improvement of the tagging system
The automated tagging approach significantly enhances
time efficiency compared to manual tagging. The experiments were conducted on a standard computer equipped
with an Intel(R) Core(TM) i5-6600K CPU running at
3.50 GHz and 8.00 GB of RAM. Tagging the 27 documents
manually required one week of an expert’s time, whereas
the automated tagging process completed the same task
in approximately 5 minutes, significantly enhancing the
efficiency of processing large volumes of documents. While
manual tagging ensures high accuracy due to human judgment, the automated method, when fine-tuned, can achieve
comparable accuracy levels while significantly reducing the
time required for tagging. This efficiency makes automated
tagging particularly advantageous for large numbers of
document collections.
Comparing manually and automatically generated XML
documents improves tag completion accuracy, particularly in
specific sections. Analyzing discrepancies reveals common
errors and patterns that may not be evident through manual
review. Understanding how manual tags reflect document
content helps adjust the automated algorithm for better
alignment with these standards.
Continuous feedback promotes iterative improvements,
increasing tag accuracy across XML documents. Insights
from both tagging methods enhance output quality and the
system’s adaptability to various document types. By systematically addressing identified issues, the automated tagging
process can evolve, ensuring effectiveness in managing
diverse content and formatting requirements in future applications.
V. DISCUSSION
The achieved results underscore the precision and robustness
of the automated tagging algorithm in processing documents
and assigning appropriate tags. However, it’s imperative to
acknowledge that despite the success achieved, there remains
room for refinement to enhance the algorithm’s accuracy
further. Variations ontology of document structures [42],
formatting inconsistencies [43], and nuances in language
usage present continual challenges that necessitate ongoing
optimization efforts.
Semantic analysis and text processing using NLTK [44],
[45], [46] offers a comprehensive suite of tools designed
to facilitate tasks such as tokenization [47], stemming [48],
lemmatization [49], part-of-speech tagging [50], parsing.
By leveraging NLTK’s functionalities, it is possible to extract
valuable insights from unstructured text data, enabling to
uncover patterns, sentiments, and relationships embedded
within textual content. One of the key strengths of NLTK
lies in its ability to perform understanding the meaning in
context of words and sentences in a given text. Through
techniques such as word sense disambiguation [51] and
semantic role labeling [52], NLTK enables to decipher the
FIGURE 8. Flowchart depicting the iterative process for refining automated tagging algorithms based on discrepancies between manual and automated
tags.
intended semantics behind linguistic expressions, thereby
facilitating more accurate interpretation of textual data. This
capability streamlines the process of tagging by ensuring
that the relevant textual content is accurately identified and
utilized for annotation purposes.
The tagging process highlighted challenges in automated
document processing, such as interpreting complex structures [53], [54] and accurately identifying relevant sections.
While the current algorithm is effective, iterative improvements are needed to address these issues. Future iterations
could incorporate advanced feature extraction techniques,
enhanced entity recognition models, and refined pattern
matching algorithms to reduce limitations.
The approach addresses challenges by automating document tagging using a predefined ontology and leveraging
NLP to handle nuances that regex cannot resolve by
interpreting and understanding the contextual meaning and
relationships within the text, which is often nuanced and
context-dependent. Unlike regex, which rely on specific
patterns, NLP techniques can grasp semantics, disambiguate
meanings, and adapt to variations in language use [55],
ensuring more accurate and contextually appropriate tagging
of document content. This combination not only enhances
efficiency but also improves the precision and reliability of
the tagging process, making it suitable for complex document
structures and diverse linguistic contexts encountered in
practical applications.
The comparison between automated tagging and manual tagging methods highlights the efficiency gains and
scalability achieved through automation. While manual
tagging remains a gold standard for accuracy, the automated
approach offers unparalleled speed and scalability. It is
should be noted that manual [56] oversight and validation are
indispensable components of the tagging process to ensure
the highest levels of accuracy and reliability.
Rigorous validation strategies and quality assurance
measures are vital for maintaining tagging integrity. Key
components include cross-validation with manually tagged
reference documents, continuous monitoring for discrepancies, and proactive error detection mechanisms [57].
Additionally, ongoing validation against diverse document
types and formats is necessary to adapt the algorithm to
evolving structures effectively.
While Python libraries such as pdfx and pdfminer provide
similar functionality in terms of extracting text from PDF
documents, the current study offers several key distinctions.
Firstly, unlike pdfx [58], which primarily focuses on
extracting metadata and references from pdf documents,
and pdfminer [59], which is a general-purpose PDF parser,
this approach specifically focuses on extracting structured
data from government standard documents with a predefined
ontology. This specialized focus allows us to tailor methods
to the unique characteristics and formatting conventions
commonly found in legal texts, thereby enhancing the
accuracy and reliability of the results.
Table 2 presents a summary of comparison of methods for
extracting data from PDF documents, focusing particularly
on the validation of their approaches.
TABLE 2. Summary of works on automated tagging and document processing.
Secondly, the study goes beyond simple text extraction by
incorporating advanced NLP techniques and Regex patterns
to segment and categorize the extracted text according to predefined criteria. This combination of NLP and Regex enables
us to identify and extract specific types of information,
such as case citations, statutory references, and contractual
clauses, with greater precision and efficiency than existing
libraries.
Furthermore, whereas pdfx and pdfminer primarily output
raw text data, the study extends the functionality by providing
hierarchical XML structuring of the extracted text. This
structured representation, conforming to the NISO STS
standards and aligned with a specified ontology, facilitates
easier navigation, search, and analysis of the document
contents, particularly in applications requiring semantic
understanding or interoperability with other systems.
A key observation from the results is the effectiveness of
the proposed approach in achieving accurate and consistent
tagging across 27 manually tagged documents. Despite
the complexity of the tagging task and variability in
document formats, the method maintained a high degree
of alignment with manually tagged documents. The study
further underscores the importance of incorporating context
and domain-specific features in designing automated tagging
methodologies. The use of regex patterns tailored to capture
domain-specific terminology, formatting conventions, and
structural elements was instrumental in ensuring the relevance and accuracy of the generated XML markup.
Some limitations and areas for improvement are acknowledged. While the approach yielded satisfactory results,
challenges such as managing variations in document formatting and resolving ambiguities in tag assignment remain
as avenues for further research. Additionally, the scalability
of the methodology for larger document volumes and
adaptability to diverse ontologies merit further exploration.
By automating the tagging process through the integration
of NLP techniques and regex, the methodology reduces
the manual effort required, making it scalable for larger
document collections. The challenges addressed in this study
are highly relevant to practical scenarios where organizations
handle vast textual data that requires efficient structuring
and tagging. The approach extends beyond basic keyword
matching to extract semantically meaningful information,
enabling automated XML tag generation that accurately
reflects both the content and context of the documents.
Achieving automation involves applying a predefined
ontology uniformly across all documents, enabling consistent
tagging through a standardized algorithm. Initially, this
entails implementing the ontology to categorize and tag
document elements systematically, ensuring that similar
content types are treated uniformly across different documents. This uniform approach facilitates streamlined processing and ensures that the tagging process adheres to
predefined standards, enhancing efficiency and consistency
in document handling. Looking ahead, the focus shifts to
automating the ontology definition for incoming documents
using ML technique by identification and adaptation of
ontology structures based on the content and structure of each
document.
VI. CONCLUSION
The successful incmplementation of automated tagging
represents a step forward in document processing and
metadata extraction. The additional contribution of this study
lies in the systematic integration and orchestration of the
existing libraries like pdf2docx, ElementTree, zip file, re,
image, os, Translator within a coherent pipeline tailored
to the specific task of document conversion. Rather than
merely selecting a set of tools and using them individually,
the study demonstrates how these tools can be effectively
combined and utilized in a sequential manner to achieve the
desired outcome. Also the study introduce novel methods for
handling specific challenges or optimizing the performance
of the pdf conversion process, which would constitute further
contributions beyond the mere selection of tools.
Future research endeavors should prioritize enhancing
the algorithm’s capabilities to accommodate a wider array
of document structures, formats, and languages within
various ontologies. Integrating different types of ontologies
with NLP, including sentiment analysis and context-aware
tagging, holds promise for enabling a more nuanced understanding and interpretation of document content. Moreover,
the exploration of Large Language Models (LLMs) [60], [61],
[62] for automating document tagging presents a compelling
avenue for future investigation. Leveraging the immense
language processing power of LLMs could improve the
efficiency and accuracy of document annotation processes,
ultimately advancing the field of document analysis and
semantic tagging.
Tailoring the automated tagging algorithm to specific
domains or industries can improve its effectiveness and
relevance. By incorporating domain-specific ontologies [63],
terminology [64], and heuristics [65], the algorithm can
provide more accurate and contextually relevant metadata
extraction for specialized document types.
Integrating automated tagging with knowledge graphs [66]
and semantic web technologies can unlock new possibilities
for data interoperability, discovery, and integration. By mapping document metadata to existing knowledge graphs
and ontologies, researchers can facilitate more efficient
information retrieval and knowledge discovery processes
by having access to structured data that encapsulates the
relationships and attributes of various entities. Knowledge
graphs facilitate the linking of tagged data to external
datasets. For example, a tagged document mentioning a
specific medical condition can be linked to a knowledge
graph containing detailed information about that condition,
thereby enriching the document’s content and providing a
more comprehensive resource.
Adopting a user-centric design approach [67] and soliciting
feedback from end-users and domain experts when correcting
obtained XMLs documents can refine the automated tagging
system. User evaluations and usability studies can identify
pain points, usability issues, and areas for improvement,
guiding iterative development and ensuring alignment with
user needs and expectations.
Ensuring scalability and efficiency are paramount for
libraries and archives with vast repositories of textual
documents that require automated processing into XML
format. Optimizing algorithms for parallel processing [68],
distributed computing, and cloud-based infrastructure can
enhance scalability and performance. This optimization
enables the processing of large volumes of documents in
real-time or near-real-time scenarios, thereby facilitating the
seamless conversion of textual data into structured XML
format.
In conclusion, while the current implementation of automated tagging for the GOST R ontology demonstrates
promising results, there remains ample room for exploration
and improvement, particularly for other potential ontologies.
The scenario described in this paper merely illustrates
the potential to extend this approach to automate the
processing of textual documents with various ontologies.
By prioritizing enhanced algorithmic capabilities, domainspecific adaptations, integration with knowledge graphs,
user-centric design, and scalability, researchers can propel
the state-of-the-art in document processing and metadata
extraction. This advancement unlocks new possibilities for
information management and knowledge discovery, paving
the way for innovative solutions in the field.
