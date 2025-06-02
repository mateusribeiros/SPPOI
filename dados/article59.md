Title: Survey of Multimodal Federated Learning: Exploring Data Integration, Challenges, and Future Directions

ABSTRACT The rapidly expanding demand for intelligent wireless applications and the Internet of
Things (IoT) requires advanced system designs to handle multimodal data effectively while ensuring user
privacy and data security. Traditional machine learning (ML) models rely on centralized architectures,
which, while powerful, often present significant privacy risks due to the centralization of sensitive
data. Federated Learning (FL) is a promising decentralized alternative for addressing these issues.
However, FL predominantly handles unimodal data, which limits its applicability in environments where
devices collect and process various data types such as text, images, and sensor output. To address this
limitation, Multimodal FL (MMFL) integrates multiple data modalities, enabling a richer and more holistic
understanding of data. In this survey, we explore the challenges and advancements in MMFL, including
data representation, fusion techniques, and cross-modal learning strategies. We present a comprehensive
taxonomy of MMFL, outlining critical challenges such as modality imbalance, fusion complexity, and
security concerns. Additionally, we highlight the role of transformers in MMFL by leveraging their
powerful attention mechanisms to process multimodal data in a federated setting. Finally, we discuss
various applications of MMFL, including healthcare, human activity recognition, and emotion recognition,
and propose future research directions for improving the scalability and robustness of MMFL systems in
real-world scenarios.
INDEX TERMS Multimodal FL, data fusion, cross-modal, multimodal federated transformer learning,
multimodal FL communication intelligent IoT applications.
I. INTRODUCTION
RECENT advances in technologies such as autonomous
agents [1], self-driving vehicles [2], health monitoring [3] and multisensory integration [4] have catalyzed
the generation of an unprecedented volume of diverse and
multimodal data. These data encompass various forms such
as text, images, videos, and sensor outputs, representing a
rich resource of information with a wide range of potential
applications in numerous domains [5]. Historically, centralized machine learning (ML) frameworks have been employed
to process and train multimodal datasets. These frameworks
typically consolidate data from numerous sources into a central repository, where complex models are trained to extract
useful patterns and insights [6]. However, conventional
ML models often struggle to effectively harness the full
spectrum of multimodal data due to challenges in capturing
and synthesizing the rich and heterogeneous nature of
multimodal data [7]. Consequently, specialized multimodal
ML (MMML) models that are explicitly designed to handle
and integrate diverse data types have been developed. These
models leverage the inherent correlations between different
modalities. This leads to more accurate and robust inferences
than those achieved by models that are limited to a single
modality [8].
Despite the advances in multimodal ML, this approach
introduces significant challenges, particularly in terms of
privacy and security [9]. The centralization of sensitive
data for processing and analysis poses a higher risk of
breach and misuse. Hence, ML systems must maintain user
privacy by prohibiting access to unauthorized data [10].
Moreover, multimodal data sources generate substantial data
that require significant communication bandwidth, often
requiring transmission to the cloud for analysis, which
strains networks and incurs considerable overhead [11]. To
address these challenges, ML developers have proposed
federated learning (FL) [12] which offers a decentralized
solution by distributing the learning process across multiple
data-generating devices or nodes. In this setup, the data
remain local to each device, addressing the privacy and
security concerns inherent in centralized approaches [13].
FL significantly enhances data privacy and reduces communication overhead, as only model parameters, not raw
data, are transmitted, enabling models to learn collaboratively
without central data aggregation. Although the FL paradigm
facilitates the training of global models without necessitating
local data sharing, it predominantly handles unimodal data,
thereby limiting its application breadth [14].
A. COMMUNICATION IN MMFL
With advancements in edge computing, many sensors and
devices continuously collect data across various multisensory modalities, including tactile feedback from industrial
machinery, thermal imaging for environmental monitoring,
and acoustic signals for urban soundscapes. For example,
autonomous vehicles integrate light detection and range
(LiDAR) data, radar, and onboard cameras in the automotive
industry to enhance navigation and safety features. Similarly,
in smart-home environments, human activities are monitored
using body sensors and RGB cameras [15]. The diversity
of data sources results in clients having varying access
levels. Some can utilize multiple data modalities (multimodal
clients), while others are restricted to a single modality
(unimodal clients). This variation in device capabilities,
data, and resources requires a comprehensive multimodal FL
(MMFL) exploration. MMFL enables AI models to integrate
information from multimodal data sources distributed across
multiple devices without requiring data centralization, while
preserving privacy by sharing model updates rather than
raw data, thus keeping sensitive information on local
devices [16].
FL relies on server-client communication, where the
server shares a global model and clients update it using
locally stored data [17]. However, this process is constrained by limited bandwidth, resource-constrained edge
devices, and statistical heterogeneity due to non-independent
and identically distributed (non-IID) data [18], [19], [20].
Compared with unimodal FL, MMFL introduces additional
communication challenges due to the increased volume and
diversity of data representations across different modalities.
In unimodal FL, model updates primarily involve processing
a single data type (e.g., images or text), making the
transmission bandwidth and computational demands more
predictable. By contrast, MMFL must handle asynchronous
updates from clients processing heterogeneous multimodal
data, each with varying sizes, computational requirements,
and learning complexities. This heterogeneity increases the
frequency of communication rounds, necessitates adaptive
update mechanisms, and introduces an additional synchronization overhead, all of which can exacerbate latency and
model inconsistency. Furthermore, multimodal feature fusion
strategies can lead to larger model architectures, increasing
the number of parameters transmitted between clients and
the server, thus further straining the communication efficiency [21].
Several communication-efficient techniques have emerged
to address these concerns, starting with selective client
participation, which prioritizes devices with complementary data distributions and adequate resources, thereby
reducing unnecessary transmissions and accelerating convergence [22], [23], [24]. Although random sampling offers
unbiased selection, it can fail to capture the non-IID and
modality-specific distributions inherent in MMFL [25], [26].
Recently proposed mechanisms tailor the selection process
considering model similarity, data quality, or loss-based
criteria to mitigate the imbalance of modalities and device
heterogeneity, thereby improving generalization [27], [28],
[29], [30]. Additional approaches reduce the communication overhead through model partitioning and modular
updates, enabling clients to exchange only relevant parameters and minimize resource usage. Parameter-efficient
fine-tuning (PEFT) narrows the scope of updates to
adapter layers or newly introduced weights, decreases the
transfer volume, and improves scalability [31], [32], [33].
Knowledge distillation (KD) further mitigates overhead
by exchanging distilled representations among teacher–
student models instead of transmitting full parameters,
thus accommodating data and device heterogeneity while
preserving performance [34], [35], [36]. Finally, compression techniques such as quantization, sparsification, and
model pruning significantly reduce parameter sizes without
severely sacrificing accuracy [37]. These methods demonstrate the ongoing advances in communication efficiency
for MMFL, while highlighting the importance of balancing
performance, resource limitations, and modality-specific
challenges. Addressing communication challenges in MMFL
is crucial for improving the scalability and practicality of
MMFL deployments in real-world edge computing scenarios.
B. RELATED WORKS
Although MMFL has attracted growing interest, its broad
potential remains underexplored, highlighting the need for
a more comprehensive examination of this emerging field.
For instance, [38] reviewed MMFL, focusing primarily
on classifications based on modal distribution and annotations. Similarly, [39] classified MMFL into congruent
and incongruent modalities, depending on the uniformity
of the modal combinations between clients, reflecting the
foundational structure of FL. Furthermore, [40] identified
the primary challenges and key lessons for developing
MMFL for healthcare applications. While these reviews offer
valuable insights into the conceptual framework of MMFL,
they often lack in-depth discussion of crucial aspects, such
FIGURE 1. Cardiovascular Diseases Example.
as fusion representation techniques. Recent work by [41]
explored fusion techniques within MMFL, yet important
challenges, such as alignment, reasoning, and generation,
remain unaddressed. Additionally, [42] classified MMFL
into three categories: Modality Exclusive, where clients
handle distinct modalities; Modality Complete, where clients
manage all available modalities; and Modality Incomplete,
where clients have access to only a subset of modalities.
As MMFL progresses rapidly, it has shown potential to
significantly enhance a wide range of applications. Thus,
a literature review that examines recent developments and
addresses the gaps in MMFL research is timely and necessary
for advancing the field. Table 2 provides a comprehensive
comparison of these results.
C. MOTIVATION AND CONTRIBUTIONS
Developments in sensor technologies, storage systems, communication networks, and auxiliary tools have significantly
accelerated data collection efforts [43]. As sensors and
networks become increasingly embedded in our daily lives,
they generate vast amounts of data that provide intricate
insights into various domain preferences and emerging
trends [44], [45]. Despite this wealth of data, its diversity in
type, structure, format, and lifespan introduces complexities
to its application. This heterogeneity often complicates data
integration from disparate sources, challenging the development of accurate models and the extraction of valuable
insights. Most of these data are multimodal, combining
elements including text, audio, images, and video [46], [47],
and adding another complexity layer.
These challenges in multimodal data integration are
exemplified in the healthcare sector, as shown in Fig. 1. For
example, Magnetic Resonance Imaging (MRI) and medical
image scanning analysis using ML models have demonstrated high efficacy in predicting Cardiovascular Diseases
(CVDs) [48]. Similarly, Personal Health Monitors (PHM),
such as smartphones and smart wearables equipped with
ML models, have proven effective in predicting cardiac diseases [49]. Electronic Health Records (EHRs) collected from
TABLE 1. List of notations and abbreviations.
various health centers such as clinics, hospitals, and smart
homes serve as valuable sources for CVD prediction using
ML algorithms [50]. However, merging these diverse data
types—MRI images as medical electronic image files, structured data from PHMs, and both structured and unstructured
data from EHRs—poses significant technical challenges. In
clinical practice, a physician may analyze all these data
types together for a more accurate diagnosis; however,
simultaneously analyzing these datasets using a single ML
model is not straightforward [51]. Healthcare data, which
are primarily restricted due to privacy concerns, are not
readily accessible for ML training. Such data are typically
dispersed across various settings, including hospitals, health
clinics, smart homes, and Personal Health Monitors (PHMs).
TABLE 2. Comparison of existing surveys on multimodal FL.
FIGURE 2. Scope of the survey paper and summary of scholarly articles on MMFL covered in this survey.
Consequently, aggregating and processing such data from
diverse sources in a centralized location poses a considerable
challenge [52]. To demonstrate the advantages of MMFL
over UMFL in CVD diagnostics, [53] conducted a comparative analysis using the PTB-XL dataset [54]. The PTB-XL
dataset comprises 12-lead ECG waveform data and additional
metadata, including patient demographics, diagnostic statements, diagnosis likelihoods, and manually annotated signal
properties, thus establishing it as a multimodal resource.
The results revealed that MMFL achieved a performance of
62.5%, outperforming UMFL’s 55.7%. This highlights the
complementary nature of multimodal data in enhancing the
diagnostic accuracy.
The example above highlights the need for a comprehensive analysis of MMFL that covers aspects such as
modalities, representations, fusion and alignment techniques,
challenges, and future directions. Although several MMFL
surveys are available, most have not thoroughly addressed
these challenges, whereas this survey introduces a novel taxonomy centered on MMFL challenges. Furthermore, while
the existing literature has explored MMFL applications,
transformers in MMFL remain underexamined, an area this
survey intends to address. Thus, the gaps in the current
research serve as the main motivation for this study.
The primary contributions of this article are summarized
as follows.
• We provide a thorough and critical review of MMFL,
focusing on its core concepts and methodologies. This
includes the clear definitions of modality, multimodality,
cross-modality, MMML, and MMFL. Additionally, we
critically compare the limitations of unimodal FL with
the capabilities of MMFL, highlighting its potential to
address complex real-world challenges.
• We thoroughly investigate the integration of transformers into MMFL for efficient multimodal data processing.
• We introduce a comprehensive and original taxonomy
for MMFL that systematically addresses core challenges, including modality diversity, data representation,
and alignment complexities.
• We analyze MMFL applications across healthcare,
human activity recognition, and emotion recognition,
linking them to practical real-world benchmarks. This
contribution not only illustrates the versatility of MMFL
but also identifies gaps in existing benchmarks, paving
the way for future advancements.
• We identify several possible directions for future
research.
D. ORGANIZATION
This survey article is structured as follows. Section II-A
provides a concise overview of Unimodal FL (UMFL),
including techniques for managing different modalities
within the UMFL framework. Section II-C outlines the
limitations of UMFL in handling multimodal data, and
highlights the necessity of a new approach to address
this challenge. In Section II-A, we define and explore
the concept of multimodality, compare it with cross-modal
learning, and discuss its implications for both ML and
FL. Section III provides a detailed discussion of MMFL
transformers, emphasizing their role and effectiveness in
managing multimodal data complexity. Section IV introduces the first part of the MMFL taxonomy based on
modality. The second part of the taxonomy is presented
in Sections V-A and V-B. Various MMFL applications are
discussed in Section VI. Section VII reviews the benchmarks
and datasets relevant to the MMFL. Section VIII discusses
the future directions and unresolved issues in the field.
Finally, Section IX summarizes the key points of the survey.
The organization of the paper is visualized in Fig. 3.
II. UNIMODAL AND MULTIMODAL FL
A. UNIMODAL FL
FL was introduced by McMahan et al. [12] as a distributed
paradigm that enables multiple devices to collaboratively
train a global model without the exchange of raw data. Each
device shares updates of the model parameters with a central
server, which aggregates these updates and redistributes the
improved global model. An FL system typically consists of a
central server and K resource-constrained IoT devices, each
with its own dataset Dk, such that the total sample count is
D = K
k=1 Dk. The fraction of data stored on device k is
given by
δk = |Dk|
D ,
where δk captures the proportion of the overall dataset
held by the client k. Each local dataset Dk comprises pairs
{(x
(k)
i,d , y
(k)
i )}
Dk
i=1, where x
(k)
i,d ∈ Rd represents the d-th feature,
and y
(k)
i is the corresponding label.
FL proceeds in three core stages. First, the initialization
stage sets up an initial global model θ 0 on the server
and selects participating devices. Next, in the local model
training stage, each client k receives θt at round t and trains
it on Dk, minimizing
Fk(θk)  1
Dk

i∈Dk
l

x
(k)
i,d , y
(k)
i

(1)
FIGURE 3. Paper organization.
where l(·) is the local error function. The model parameters
on device k are updated via gradient descent as follows:
θk ← θk − α∇Fk(θk) (2)
where α is the learning rate. Finally, in the model aggregation
stage, each client sends its updated parameters θk, the server
combines them into a new global model and calculates the
aggregate loss function as follows:
F(θ) 
K
k=1
δk Fk(θk) (3)
Subsequently, the combined model parameters are derived
in the following manner:
θ 
K
k=1
δk θk (4)
These steps are iterative until the global model converges to
an optimum, which is usually indicated by minimizing the
aggregate loss function [18], [20], [21], [55].
In UMFL, substantial heterogeneity is observed among
real-world IoT clients [18], [56]. This heterogeneity, including data heterogeneity [57], [58] poses a considerable
obstacle, and it has been established that the conventional
FL method FedAvg [12] struggles when confronted with this
scenario, leading to a notable performance drop. To address
this issue, researchers have proposed several enhancements
to UMFL. Various methods have been proposed to address
1) REGULARIZATION
To prevent divergence in UMFL models, a penalty is added
to the loss function to dynamically regulate the complexity
of the model, thereby ensuring the convergence of the
model in diverse client data [59]. FedProx builds on the
FedAvg framework [12] by incorporating a term that reduces
discrepancies between local and global models and enhances
stability [18]. A FL framework similar to FedProx, known as
FedCur, has been proposed, employing parameter stiffness
to enhance model convergence [60]. However, FedCur
distinguishes itself by integrating a penalty term into the loss
function, which forces all local models to converge towards
a shared optimum. Additionally, FedCur adopts a multitask
learning approach, enabling the simultaneous learning of
distinct tasks on the same model without interference. This
capability significantly improves convergence and addresses
complex challenges within FL environments, marking a key
advancement over the conventional approach of FedProx.
Elastic Weight Consolidation prevents catastrophic forgetting
by penalizing significant changes to crucial parameters and
adapting this technique to FL settings [61]. Recent advances
include SCAFFOLD and MOON, which improve the alignment of clients and models, and address regularization
between global and local models, respectively, [62], [63].
Techniques that apply weighted regularization based on noise
estimates help improve the performance of clients with
variable data quality [64]. Furthermore, efforts to ensure
consistency in the sample embeddings involve aligning them
with unbiased prototypes and removing irrelevant domain
information [65]. An elastic aggregation approach based
on sensitivity analysis was also developed to fine-tune
parameter adjustments, serving as an implicit regularization
mechanism [66].
2) PERSONALIZED FL
Personalized FL also addresses the issue of data heterogeneity within FL frameworks [67]. This method focuses
on developing an initial shared model in which individual
users can quickly adapt to their specific datasets through
minimal gradient descent iterations of their own data. This
personalized strategy maintains the core advantages of FL,
while producing more precisely customized models for
each user. A personalized FL algorithm was developed by
Mei et al. [68], which crafts personalized models for clients
and maintains a global model on a central server using a twostage layer-wise parameter division training process. This
enhances personalization by leveraging globally obtained
features. Similarly, Ma et al. [69] introduced pFedLA,
improving PFL by adjusting model aggregation based on the
significance of each layer and achieving better performance
with a hypernetwork for each client. Split Learning (SL),
as described by [70], contrasts with parameter decoupling
by maintaining private client updates and shared global
parameters, offering enhanced privacy but facing limitations
such as increased latency and scalability issues. Parameter
decoupling in FL has been explored through two main configurations, as discussed by [71] and [72]. These approaches
allow for the learning of personalized features while sharing
base layers and using configurations such as Local Global
Federated Averaging (LG-FedAvg) for efficient learning.
These methods reflect a trade-off between personalization,
efficiency, and privacy, crucial in deploying FL [73].
3) FEDERATED MULTITASK LEARNING
. Federated multitask learning (FML) aims to tailor models
best to match the local data distribution for each client. This
approach enables clients to locally train models on multiple
tasks without exchanging raw data, thereby improving data
privacy and security [74]. The first FML framework designed
for convex models was proposed by Smith et al. [75].
Albaseer et al. [19], [76] presented clustered FML to address
data heterogeneity. They clustered clients according to the
similarity in their data distributions.
B. MULTIMODAL FL
Modality refers to the manner in which a natural phenomenon is observed or represented. Common modalities
include speech and audio captured via microphones, visual
data from images and videos recorded through cameras,
and tactile feedback such as force and vibrations collected
through haptic sensors. These modalities range from raw,
directly acquired from sensors (e.g., speech or images),
to abstract, which is derived from raw data and includes
elements such as textual interpretations from audio or object
identification from visual inputs [77]. Multimodal scenarios
involve multiple modalities and focus on computational
analysis and the interactions between them. Modalities are
inherently heterogeneous, and have unique qualities and
structures. For example, auditory and visual signals differ
significantly in processing requirements. However, these
modalities are interconnected, often providing complementary information that enhances the functionality of the
system, such as in autonomous driving systems, where camera visuals and radar spatial data work together to improve
navigation and object detection [6]. An intriguing aspect
of multimodality is its potential for both heterogeneity and
homogeneity among the modalities involved. For instance,
images from the same camera exhibit high similarity
(homogeneity), whereas texts in different languages exhibit
significant diversity (heterogeneity). This variability enriches
the learning process, allowing nuanced feature extraction and
data interpretation across different contexts [78].
1) MULTIMODAL VS CROSSMODAL
In the field of ML, the terms ‘multimodal’ and ‘cross-modal’
are often used interchangeably in some studies [79], whereas
others lack precise definitions, leading to confusion [80].
However, these terms represent distinct concepts within
the broader spectrum of AI research. Multimodal learning
refers to the capability of a system to process and integrate
multiple types of data inputs or modalities to achieve a
FIGURE 4. Comparison between UMFL and MMFL. (a) UMFL: This shows a vanilla FL setup in which all clients process the same data modality (e.g., images) and aggregate
updates on the cloud server. (b) MMFL: Illustrates a setup where clients process different data modalities (e.g., Client 1: sensor data and images, Client 2: sensor data, Client 3:
text, and sensor data), enabling the aggregation of multimodal updates at the cloud server for a unified global model.
specific objective [81]. For example, humans utilize visual
and auditory inputs to recognize individuals or objects, a
process mirrored in multimodal AI systems.
By contrast, cross-modal learning is a specialized subset of
multimodal learning that focuses on developing algorithms
that can process and learn from unaligned data across
different modalities [82]. A typical example involves learning
from datasets in which images and textual descriptions do
not directly correspond to one another. This approach is
particularly useful for enhancing the system’s ability to
perform tasks in one modality based on the information
extracted from another. For example, recognizing a dog from
its image might improve the system’s accuracy in identifying
the animal using its bark alone, despite the non-concurrent
nature of the data.
Multimodality involves the capability of a system to utilize
various modalities or input types to accomplish a specific
task. For instance, a person can employ both vision and
hearing to recognize an individual or an object. Conversely,
cross-modality refers to a system’s capacity to leverage data
from one modality to enhance performance in another. For
example, observing a picture of a dog might allow us to
identify it by recognizing its bark when it is heard.
2) MULTIMODAL ML
MMML processes and relates data across different levels
of abstraction, extracting features from various modalities
to effectively manage heterogeneous data. This approach
integrates sensory data from visual, auditory, textual, and
kinesthetic sources to optimize learning outcomes through
enhanced cognitive processing. The goal of MMML goes
beyond simply processing multiple modalities; it aims to
understand the interrelations among these modalities and
their specific applications.
3) MULTIMODAL FL
MMFL extends the FL framework by incorporating multiple
data modalities across the distributed nodes. Unlike UMFL,
which handles a single data type, MMFL leverages local
datasets using at least two distinct modalities, as shown in
Fig. 4(b). This integration enables MMFL to utilize a richer
data environment, improve model performance, and broaden
its applicability in diverse real-world settings. A multimodal
classification task is used to define MMFL more concretely
for illustrative purposes. Within the MMFL settings, given
K clients and at least two modality categories M (where
M ≥ 2), each client k is assumed to have access to a local
dataset Dk, which includes a set of data samples. The size
of the dataset is signified by the number of these samples,
|Dk|, where Mk denotes the total number of data modalities
for a client k, with Mk ∈ [1, M]. If Mk = 1, the client is
designated unimodal. If (Mk ≥ 2), then it is considered a
multimodal client.
To classify clients according to their data modalities, the
local multimodal dataset Dk for any client k is defined as
Dk = {
xm1
k , xm2
k ,..., x
mMk
k , yk

j
| j = 1}
|Dk|
where xmk
k denotes a sample associated with the m-th
modality that belongs to client k. The i-th data sample from
client k’s local dataset is Xk(i) = (xm1
k , xm2
k ,..., x
mMk
k ). The
set of modalities for this local set is denoted as λk =
(m1, m2,..., mMk). For example, a client’s dataset may
include both image and text data, making its modality
combination λk = (image, text), and the corresponding local
data sample is Xk(i) = (x
image
k , xtext
k ). Therefore, the modality
number for this client is Mk = 2.
During a communication iteration t, the local parameters
θk for a client k are refined through a local training session
using stochastic gradient descent (SGD), expressed as:
θt+1
k = θt
k − μ∇Lk

θt
n; Xki
, yk

where α indicates the learning rate and ∇Lk denotes the
gradient of the loss function for the model parameters.
Within this context, Xk signifies the respective multimodal
input data for clients k and Lk is the aggregate loss function
for the client. Here, θt
k represents the model parameters for
client k during round t of training.
The contributions of various data modalities to the overall
loss may vary depending on factors such as problem
type, data quality, and task requirements. For example,
in a classification scenario with image-text data, the loss
contribution from the image data may be prioritized over
the text data. For a given input Xk(i), the total loss Lk is
represented as:
Lk

Xk(i), θt
k, yk(i)

=
Mk
j=1
δ
mj
k · Lmj
k

θmj
k (·, θt
k), yn(i)

Here, δ
mj
k represents the aggregated weight of modality mj,
thetak is the local model of client k, Lmj
k is the loss function
for modality mj, and Xmj
k is the input data for modality mj.
The local training target is defined accordingly:
fk = 1
|Dk|

|Dk|
i=1
Lk(Xk(i), θk, yk(i))
Consequently, the objective of global optimization is formulated as
min F(θ) =
K
k=1
δkfk(θk)
where θ are the global model parameters; δk is the global
aggregation weight for client k; and K is the total number
of clients.
C. DISCUSSION
The development of UMFL techniques such as Personalized
FL and FML has been pivotal in addressing the heterogeneity
of client data distributions. Despite these advances, such
techniques often fall short when dealing with the complexity
of real-world data, which frequently manifests in multiple
modalities. Although personalized FL customizes learning
models to fit individual client profiles, its effectiveness is
inherently limited by the singularity of the data modality it handles, often overlooking the rich interconnected
cues present across different sensory inputs. Similarly,
although FML improves model robustness by leveraging
task-related commonalities, it is predominantly structured
around the unimodal data streams. This singular focus
restricts its capacity to fully exploit the multifaceted nature
of sensory data, thereby limiting its application scope in
complex real-world scenarios where multiple data types
are interlinked. The MMFL addresses these limitations by
integrating multiple data modalities (e.g., visual, textual, and
auditory) at the federated level, thus fostering a more holistic
understanding of the data. MMFL not only enhances the
predictive performance and robustness but also broadens the
applicability of FL to more complex scenarios. It effectively
tackles challenges, such as modality imbalance and crossmodal learning, which are pivotal in diverse and data-rich
settings. Fig. 4 provides a comparison between UMFL and
MMFL.
FIGURE 5. Vanilla Transformer Architecture [83].
III. MULTIMODAL FL TRANSFORMER
Transformers represent a recently developed and highly
effective deep learning (DL) architecture known for
their outstanding performance in numerous language-based
tasks, including text classification, machine translation, and
question answering [83], [84]. As shown in Fig. 5, the
transformer model features an encoder-decoder structure,
which accepts tokenized data as input. This architecture
consists of multiple layers, known as a transformer block.
These blocks include two principal sublayers: a multihead
self-attention mechanism (MHSA) and a position-wise, fully
connected feedforward network (FFN), complemented by
normalization and shortcut connections. The MHSA component is fundamental to the basic design of a transformer [83].
A. TRANSFORMER ADAPTABILITY FOR MMFL
Although transformers were originally designed for natural
language processing (NLP) tasks, they have proven highly
effective in handling multimodal data because of their
self-attention mechanisms that can capture long-range dependencies and interactions between different modalities in
a unified representation of multimodal and heterogeneous
data. Transformers are well suited for multimodal learning
because of their capability to process and fuse data from
diverse modalities within a unified architecture. In MMFL,
transformers serve as backbone models for processing local
multimodal data, while preserving privacy. Federated transformers offer key advantages, including unified multimodal
representations and dynamic interaction mechanisms, making
them ideal for applications, such as autonomous driving,
where multimodal data is prevalent. Unlike traditional
heterogeneous networks, which are complex to design under
TABLE 3. Recent works on multimodal transformer FL.
privacy constraints, transformers excel in federated scenarios
due to their high capacity and modularity. Their structure
supports flexible partitioning, enabling efficient adaptation
to clients with limited computational resources, thereby
addressing the latency challenges in FL. Additionally,
transformers excel in self-supervised learning, reducing the
dependency on labeled data, due to their scalability in model
capacity and data handling. Finally, their pair-wise similaritybased attention mechanism enhances performance with
non-IID data, offering better generalization than frameworks
such as convolutional neural networks (CNNs).
Owing to the significant success of vanilla transformers,
numerous derivative models have been developed, including
BERT [89], BART [90], GPT [91], Longformer [92],
Transformer-XL [93], and XLNet [94]. Following the development of various transformer-based models, the Vision
Transformer (ViT) [95] has emerged as a groundbreaking
approach. It extends transformer encoders to image processing and has been widely adopted in tasks such as
recognition [96], detection [97], and segmentation [98]. It
performs well in both supervised [96] and self-supervised
learning [99], [100], [101]. Recent research has also
enhanced the theoretical understanding of ViT, particularly
regarding representation robustness [102] and latent propagation [103], [104]. Although ViTs have established themselves
as the standard architecture for centralized computer vision
tasks, their application in FL is still in its early stages. For
instance, [14] assessed the performance of ViTs in global FL
settings, highlighting the robustness of the data heterogeneity.
Concurrently, FedPerFix [105] and FedTP [106] explore the
personalization of ViTs within personalized FL frameworks.
Additionally, research focusing on other aspects of ViTs,
such as pre-trained models, has also begun to attract
attention [107], [108], [109].
In a pioneering study on the application of transformers to multimodal tasks, VideoBERT [110] demonstrated
the significant potential of this architecture in handling
complex multimodal contexts. Several transformer-based
multimodal pretraining models including ViLBERT [111],
LXMERT [112], and VisualBERT [113] were introduced
after VideoBERT. These have become increasingly prominent in ML research. A significant advancement in this area
came with the introduction of CLIP [114] in 2021, which
redefined classification as a retrieval task, enabling zero-shot
recognition through extensive multimodal pretraining. The
success of CLIP has paved the way for further exploration,
inspiring the development of related models such as CLIPbased zero-shot semantic segmentation [115], ALIGN [116],
and CoCa [117]. For further insights into the use of
transformers in multimodal learning, refer to [118].
The architecture is shown in Fig. 6 demonstrates a
Transformer-based approach for MMFL, structured around
embedding layers, Transformer blocks, and task heads. Each
client, whether dealing with images, text, or both, utilizes
customized embedding layers and task heads tailored to their
specific data and local objectives, whereas the transformer
blocks operate within a unified framework to ensure consistent processing across modalities. During each round of FL,
unimodal clients download the global model specific to their
modality and the transformer blocks from other modalities.
They then conduct complementary local training to bridge
cross-modality gaps. By contrast, multimodal clients perform
standard multimodal training. After local training, all clients
send their updates to the server, where the server performs
uni-aggregation and collaborative aggregation. This process
effectively addresses both cross-modality and in-modality
gaps and enhances the integration of diverse data within the
global model.
B. CHALLENGES IN TRANSFORMER DEPLOYMENT FOR
MMFL
Two significant challenges arise when deploying transformers in the MMFL. While individual users can download
and locally fine-tune the weights of transformer models
for specific tasks, pre-training these models requires access
to extensive training datasets and substantial computational
resources. These stringent requirements render it impractical for any client to undertake the pretraining process
FIGURE 6. Multimodal Federated Transformer Architecture [88].
FIGURE 7. MMFL Taxonomy.
independently. To address these challenges, FedBERT [87]
was introduced, enabling clients with limited computational
power to pre-train a large model. This approach combines
FL and split learning techniques and allows BERT [89]
to be pretrained in a distributed manner. Seminal work on
Transformers in MMFL was conducted by Tian et al. [119].
Their research introduced a hierarchical architecture for
intelligent vehicle transformers, comprising an in-vehicle
transformer, a federated in-vehicle transformer, and a federation of in-vehicle transformers. This design enhances
multimodal data representation and facilitates privacypreserving computations and collaboration. However, their
study lacked implementation and experimental evaluation.
Certain studies have employed adapter-based techniques
by integrating small, trainable adapters into fixed pretrained transformer models, enabling client-specific model
customization without modifying the original FL model.
For example, FedDAT [35] utilized a dual-adapter approach,
where personalized adapters captured client-specific knowledge, whereas a global adapter retained client-agnostic
information. FedDAT implements bidirectional knowledge
distillation between personalized and global adapters to
regularize client updates and mitigate overfitting. Similarly,
FedCLIP [86] extended the CLIP model [114] by adding an
adapter module after the CLIP backbone, allowing efficient
deployment in FL environments. These lightweight adapters
maximize the pre-trained model information usage and
ensure adaptability for specific client tasks while reducing
computational and communication burdens. Furthermore,
FedCola [88] investigated a transfer MMFL scenario in
the vision-language domain, where clients hold data from
different modalities spread across various datasets. This
study systematically evaluated the performance of existing
methods using a FedCola transformer architecture designed
to address in-modality and cross-modality gaps among
clients.
Unlike the conventional UMFL, the multimodal transformer framework requires dedicated encoders for each
modality, leading to larger, more complex models. Training
these models requires substantial resources, which present
significant difficulties for clients with limited computational and communication capabilities [120]. Hierarchical
knowledge disentanglement across modalities and clients
through a multistage training paradigm can address the
computational challenges in transformers for MMFL. This
design enables efficient collaboration among heterogeneous
clients, minimizes storage overhead, and ensures adaptability
to new sensing modalities [121]. Alternatively, submodel
extraction provides a flexible solution by aligning the
complexity of the model with the computational capacity of
each client. This approach dynamically adjusts the submodels
based on the importance of the model parameters, effectively
addressing the limitations of static and conventional dynamic
extraction methods [122]. Submodel extraction may face
challenges such as reliance on accurate metrics, added complexity, delays, scaling issues, reduced model accuracy, and
difficulty in integrating with existing systems. Furthermore,
efforts to improve communication efficiency in FL, such
as sparsification [123], quantization [124], and client selection [125] can reduce overhead but risk-degrade accuracy or
introduce biases. In MMFL, these challenges are heightened
because compression may compromise critical modalityspecific information, and prioritizing clients with stronger
links can skew the global model. Balancing communication
efficiency and performance is particularly difficult because
of the unequal contributions of the different modalities [126].
Table 3 summarizes recent studies on multimodal federated transformer learning.
IV. TAXONOMY AND MODALITIES IN MMFL
Multimodals emulate human sensory and cognitive functions
by integrating diverse data sources, resulting in a richer and
more comprehensive understanding of real-world scenarios.
The taxonomy of the MMFL categorizes this complex field
into distinct areas: modalities, representation techniques, and
alignment strategies, as shown in Fig. 7. Each category
addresses specific challenges and uses unique methodologies
to exploit the complementary strengths of multimodal data
effectively. This section introduces the first category of
taxonomy, focusing on modality. Other categories, including
representation and alignment techniques, are discussed in
Sections V-A and V-B.
Based on modality presence across clients, MMFL can be
classified into three primary categories: Modality Exclusive,
Modality Complete, and Modality Incomplete. Table 4
provides a detailed summary of the studies on MMFL,
categorizing them according to the class of modality, task,
fusion stage, fusion level, and performance metrics. The
modality class highlights whether the studies used complete,
incomplete, or cross-modal data, reflecting the adaptability
of MMFL to handle varying data availability. The tasks
covered include diverse applications, such as healthcare,
activity recognition, autonomy, and vehicles, which showcase
the versatility of MMFL in all domains. The table further
classifies studies by their stage of fusion (early, late, or
hybrid), indicating how the data are integrated into the
learning process. The fusion levels are described as features,
scores, or network levels, showing where integration occurs
in the model pipeline. Feature-level fusion is prominently
used because of its effectiveness in combining multimodal
data, particularly in scenarios with heterogeneous data
formats. Performance metrics such as accuracy, precision,
recall, F1 score, communication efficiency, and training time
provide a comprehensive evaluation of each study, with
healthcare applications prioritizing precision and recall and
tasks such as activity recognition focusing on accuracy and
efficiency. presents a detailed summary of existing research
on MMFRegardings, and includes extensive analysis of key
studies in the subsequent sections, covering aspects such as
modality class, application scenarios, fusion stage, fusion
level, and metrics.
A. COMPLETE MODALITY
In Complete Modality MMFL (CM-MMFL), one client is
equipped with all available data modalities, while the other
clients share overlapping data to varying extents. In one
configuration, all the clients possess multimodal data with
uniform modality types. Alternatively, the method can be
structured such that one client maintains a complete set
of modalities and the other clients contribute additional
complementary data. The majority of current studies fall
within this category. In terms of representation extraction
and fusion, certain architectures resemble those used in
Cross-Modality MMFL. Two main techniques are commonly
used in this context. One involves the transmission of
parameters, whereas the other focuses on the transmission
of representations.
1) TRANSMISSION OF PARAMETERS
In this approach, the server and clients exchange the
model parameters. The server aggregates the parameters
sent by clients, which are typically gradients or weights,
and updates the global model accordingly. Each client
receives the updated global model and continues to train
locally. In addition, local clients in MMFL extract features
from their respective data modalities and fuse them to
generate the model parameters. This technique follows traditional methods in cross-modality MMFL, where the model
parameters are exchanged between the server and clients.
This ensures that raw data remain distributed to clients,
enhancing privacy and reducing the need for centralized data
collection. However, it may not efficiently capture complex
multimodal relationships because aggregation is performed
at the parameter level without explicitly considering the
diversity of data modalities.
For instance, the authors in [127] applied this approach to
melanoma detection by utilizing CNNs and a custom network
to process medical images and clinical data separately.
They employed a late fusion strategy to combine features
and achieve competitive performance. However, their study
focused on relatively simple downstream tasks and limited
heterogeneity in the multimodal data handling of the model.
Building on this, [16] proposed the MMFed, which offers
a more comprehensive solution for CM-MMFL. Their
method integrates Co-attention and Model-Agnostic MetaLearning (MAML), enabling human activity recognition
from video signals. Co-attention allows complementary
information from multiple modalities to be effectively
combined, whereas MAML personalizes models for each
client. Although MMFed improves accuracy, especially in
video signal datasets, challenges such as communication
costs and model complexity still require further investigation.
In addition, Chen and Pan [138] advanced MMFL with a
method for generating medical image reports. Using CNNs
for image feature extraction and transformers for handling
textual data, their report generator converts these features into
predictive labels. They also introduced FedSW, which adjusts
client weights based on performance scores, and shows
improvements in local training. However, challenges remain
with dataset heterogeneity and the high costs associated
with addressing the performance discrepancies. The authors
of [128] addressed the issue of modality consistency by
converting time-series data into two-dimensional images
using the Gramian Angular Field method. This approach
stacked features to improve the model complexity and
performance, although further development is still required
to handle more complex tasks and diverse datasets.
To address the missing modalities, the authors of [28]
introduced AutoFed, which uses intermodal autoencoders to
impute absent data. This method enhances modality heterogeneity by applying feature-level fusion and demonstrates
strong results in object detection for autonomous driving
systems. Despite these advances, challenges such as privacy
concerns and scalability in federated environments remain
as key areas for future research. Finally, Ouyang et al. [129]
tackled the issue of straggling clients in MMFL using their
harmony framework. By incorporating modality-wise FL
and federated fusion learning, harmony improved training
times and accuracy by balancing training latencies. Future
work in MMFL should focus on overcoming challenges such
as adversarial attacks and fusion strategies and ensuring
the sustainable deployment of models across multimodal
datasets.
2) TRANSMISSION OF REPRESENTATIONS
In contrast, this technique involves sharing learned representations rather than the model parameters. Additionally,
it typically includes sharing data representations and model
parameters, and blending the two for more comprehensive
communication between clients and the server. Clients
generate intermediate representations from their local data,
which are then transmitted to a server for aggregation.
Depending on the configuration, representations can be
shared directly between the server and clients, or exchanged
among clients in a decentralized manner. This method allows
the model to better integrate multimodal data by learning
from representations and capturing richer information from
different modalities. It offers greater flexibility but may
introduce additional communication overhead and privacy
concerns if sensitive information is embedded in the representations. In this direction, Zhao et al. [130] proposed the
Multimodal-FedAvg framework, which uses an auto-encoder
to fuse data from different modalities, aligning unlabeled
clients with those possessing complete modalities. By transferring multimodal representations, this approach achieves
better alignment and improves performance across datasets,
especially in F1 scores, compared to traditional unimodal
methods. Despite its advantages, this study addressed only
limited heterogeneity issues. The authors in [139] tackled
cross-modality retrieval by introducing a federated crossmodality framework that effectively manages multimodal
data in a federated setting. By using VGGNet for image
data and BERT for text, the method creates a shared latent
subspace for fusion, significantly improving the performance
in retrieval tasks. However, this method does not fully
explore how to handle imbalanced or unevenly distributed
client data. FedUSL [131] was designed for fatigue detection
by exchanging the projection matrices between clients and
servers. This approach reduces the number of communication rounds and performs well, even with limited labeled
data for specific modalities. This research highlights the
framework’s efficiency in practical applications, although it
calls for further exploration in privacy and computational
cost management. In parallel, FedMEKT [132] focused on
knowledge transfer by continuously enriching multimodal
representations. This semi-supervised method uses joint
TABLE 4. Summary of MMFL studies: It categorizes MMFL studies based on modality types (complete, incomplete, cross), tasks (e.g., healthcare, activity recognition,
autonomous vehicles), fusion stages (early, late, hybrid), fusion levels (feature, score, network), and performance metrics (e.g., accuracy, precision, recall).
embedding knowledge transfer to enhance both communication efficiency and model generalization. FedMEKT provides
a more scalable approach to FL by reducing the need for
a direct parameter exchange. Further developments include
CreamFL [34], a framework that relies on public datasets
for knowledge distillation, in which clients exchange representations using a contrastive learning approach to reduce
model drift. Although this method achieves high performance
by integrating global representations, it also incurs high
computational and communication costs. Moreover, it raises
concerns regarding secure representation transmission, especially in the presence of malicious actors.
B. CROSS-MODALITY
Cross-modality (CrM-MMFL) describes a unique scenario
in which each client involved in federated training possesses
only one type of modality or sensor, effectively rendering
each participant a unimodal client. Notably, clients may
still have the same modality despite being limited to a
single data type. For unimodal data handling in MMFL,
Liang et al. [133] pioneered LG-FEDAVG, which employs
a long short-term memory (LSTM) model and ResNet-18
to fuse multimodal data using element-wise multiplication.
Although it outperformed FedAvg, it struggled to effectively
integrate diverse modalities. Similarly, the authors of [140]
developed a method for COVID-19 diagnosis using VGG16
to process X-ray and ultrasound data separately. Although
this achieved good accuracy, its generalization was limited
owing to the dataset and edge-computing challenges. Most
methods derived from the FedAvg exchange model parameters often lose their critical modality-specific features. To
address this, Yang et al. [134]. studied cross-modal federated
human activity recognition (CM-FHAR), which maps client
data to a shared modality-agnostic space, thereby improving
accuracy. They refined this approach with a modalitycollaborative activity recognition network (MCARN) by
adding a calibration mechanism to better handle both balanced and unbalanced scenarios. However, their complexity
poses challenges for their practical application.
FedFusion [141] was proposed for satellite detection using
SVD to decompose local data into vectors for global model
creation without raw data transmission. Similarly, the authors
in [135] developed federated modality-specific encoders and
multimodal anchors (FedMEMA) for brain tumor segmentation, employing multimodal fusion to enhance performance,
although intra-modality challenges remain unresolved. Three
fusion strategies have emerged: direct connection, shared
subspace, and attention mechanisms. Direct connections,
such as LG-FEDAVG, retain less information, whereas
shared subspaces such as FDARN and MCARN can suffer from negative data interference. Attention mechanisms
present a more robust solution that offers the potential to
address these challenges in future research.
C. INCOMPLETE MODALITY
Incomplete Modality MMFL (IC-MMFL) arises when no
client possesses all data modalities or the modalities
are unknown (modal-model agnostic). This scenario is
more complex than traditional methods and often requires
advanced techniques, such as graph-based structures or
shared modules, to extract the semantic relationships between
modalities. In cases where the specific modalities are
uncertain, but the task is defined, FL can leverage all
available modalities for training, followed by a local fusion
process. Although effective, this method can be computationally intensive. A more efficient strategy involves selecting
clients that provide the most relevant data for the task,
which helps to minimize the computational overhead. In
practical applications, multimodal data frequently suffer from
incompleteness, with certain samples missing from partial
modalities. This is predominantly due to unforeseen issues,
such as equipment failure and losses during data transmission
and storage, presenting a significant challenge in MMFL. In
the diagnosis of Alzheimer’s Disease, integrating data from
various modalities, including magnetic resonance imaging
(MRI) scans, positron emission tomography (PET) scans,
and cerebrospinal fluid (CSF) analysis, has been shown
to enhance diagnostic accuracy [142], [143]. However, the
high costs associated with PET and the invasive nature
of CSF tests often lead to patient reluctance to undergo
these procedures. Consequently, this often leads to the
occurrence of incomplete datasets in Alzheimer’s Disease
diagnosis, compounding the challenges in MMFL where
certain clients may possess missing or incomplete modalities [144], [145]. Additionally, studies have demonstrated
that a model trained on a complete dataset may experience
a significant decline in performance when later applied to
incomplete multimodal data [28]. For instance, Yuan et al.
[30] proposed an incomplete MMFL framework that employs
a late-fusion stage strategy by modularizing models and
training each unimodal component independently. Their
experimental results demonstrated the effectiveness of the
approach by selectively choosing modalities and local clients
to minimize communication overhead. However, the reliance
of the framework on numerous hyperparameters is a notable
drawback as it prevents the achievement of high accuracy
across all datasets. MMVFL [137] integrated vertical FL into
a multimodal system to address multimodal data distribution
and encryption challenges. They introduced a two-step
multimodal transformer model that effectively captures
cross-domain semantic features. They employed a bivariate
Taylor series expansion to transform the objective function to
overcome encryption limitations without relying on a thirdparty co-operator. Experiments on diverse video text and
image text datasets demonstrated the superior performance
of the framework over state-of-the-art methods, confirming
its effectiveness in multimodal vertical FL settings.
Various methods have been developed to address this
problem of missing modalities. The initial approach to
addressing missing modalities involves the use of imputationbased methods to replace missing data. However, these
techniques include zero-filling [28] and average imputation [146]. Zero-filling is a basic technique in which missing
values in multimodal data are replaced by zeros. Average
imputation handles missing modalities by replacing missing
values with the mean average of the available values in the
same column. However, both techniques have limitations as
they primarily utilize information within the same modality
and neglect correlations across different modalities. Another
technique based on imputation is generative network reconstruction to restore missing modalities. An example of this
technique is the conditional generator [147], which produces
absent modalities based on the present modalities. Given
the strong correlation among multiple MR modalities in
tumor areas, a multisource correlation network was devised
to capture these relationships. This network not only aids
the conditional generator in producing coherent modalities,
but also enhances the segmentation network by guiding it to
learn correlated feature representations, thereby improving
segmentation performance. However, these methods typically
require complete datasets for model training, which are often
challenging to obtain in practical settings. Another imputation method called the adversarial method was presented
in [148]. It is designed to enhance the generator’s ability
to produce high-quality missing modalities. Similarly, [146]
employed an adversarial strategy to impute missing modalities, followed by encoding features from all modalities into
a latent representation to improve the overall completeness.
Conversely, certain techniques differ from the imputationbased methods. A prime example is the graph-based
method [149] that employs a heterogeneous graph structure
to fuse multimodal data without requiring data deletion
or imputation. This method constructs a heterogeneous
hypernode graph to model data with various combinations
of missing modalities. A graph neural network is used to
project incomplete data into a unified embedding space.
An additional technique is the sparse linear predictionbased method [150] that can handle incomplete or missing
modalities. It utilizes the available data to estimate covariance matrices without resorting to imputing the data.
Subsequently, it employs a lasso-type estimator to offer
a sparse coefficient estimate for optimal linear prediction.
Nevertheless, both graph-based and sparse linear prediction
techniques are not directly applicable to FL because they
construct hypergraphs or compute the covariance matrix of
predictors in a centralized fashion.
V. REPRESENTATION TECHNIQUES AND ALIGNMENT
STRATEGIES IN MMFL
Effective representation and alignment of multimodal data
are crucial for enhancing the performance and coherence of
models in MMFL. These processes involve encoding diverse
data types and synchronizing their interactions to facilitate
comprehensive learning across the distributed systems.
A. REPRESENTATION
MMFL leverages data from diverse sources to enrich the
representation of the information. This process involves
encoding and summarizing data from multiple modalities
and exploiting the complementary and redundant features
inherent in these diverse data types. Representation in
multimodal learning can be viewed as either learning detailed
representations that focus on interactions between particular
elements, such as the correlation between audio spikes and
emotional expressions in videos, or utilizing a comprehensive
approach that encompasses broad features across modalities,
such as integrating image and text features to improve the
performance of visual question answering systems.
Such representations often lead to the challenge of
handling heterogeneous data, which can complicate the integration efforts. Specifically, difficulties arise when datasets
lack common attributes, or when their overlapping features
are minimal. Addressing these challenges is critical for
effectively applying MMFL techniques, as it directly affects
the accuracy and efficiency of the derived models. Two
representation methods exist in multimodal learning: fusion
and coordination.
1) FUSION REPRESENTATION
The Fusion representation method, also known as a joint
method, involves integrating high common knowledge or
model outputs derived from multiple data modalities across
geographically dispersed clients. Three types of fusion stage
representations are commonly used in MMFL: early, late,
and hybrid. Various concatenation forms combine modality
data into a single feature vector to implement fusion stage
representations. This approach can utilize input data such
as raw features, class likelihood vectors, or neural network
nodes. Alternatively, a merging method integrates modality
data with a more complex logic than simple concatenation.
This merging process often applies to features and involves
an arithmetic operator, such as summation (), to transform
the input values into a new feature vector [151].
a: Early Fusion Stage Early fusion stage representation
involves combining features from different modalities at
the client level before model training occurs. However,
because data are not centrally collected in FL, this approach
often requires preprocessing the data on each client into
a common format that can be used to train local models.
For instance, [128] introduced an MMFL system designed
for data-level fusion, specifically integrating wearable sensor
signals and images to detect user falls. On the other hand,
Martínez-Villaseñor et al. [152] extracted manual features,
including the mean and standard deviation, from the original
dataset, which were then combined for implementation in
ML-based fall detection systems. Similarly, [16] presented
an early fusion MMFL technique called the co-attention
mechanism to integrate complementary information from
various modalities, thereby enhancing the performance of
FL. In MMFL, some early fusion approaches utilized public
datasets on the global server side to extract common knowledge. This strategy helps in leveraging shared features and
information that are beneficial across multiple clients while
still adhering to the privacy-preserving principles of FL. To
address modality discrepancies, FedMEKT [132] presented
a novel semisupervised MMFL framework. It incorporates a
suite of components: local multimodal autoencoder training,
the construction of generalized multimodal autoencoders,
and generalized classifier training. At its core, FedMEKT
employs a distillation-based knowledge transfer mechanism
that enables the exchange of joint multimodal embedding
knowledge between servers and clients via a multimodal
proxy dataset. This framework strategically updates generalized global encoders by iteratively incorporating multimodal
embedding knowledge from clients, thereby facilitating
enhanced local learning through targeted knowledge transfer.
Additionally, FedUSL [131] utilized an early fusion method.
It is designed for fatigue detection by exchanging projection
matrices between clients and servers, reducing the number
of communication rounds, and working well with limited
labeled data.
b: Late Fusion stage Conversely, late fusion trains separate
models on different modal datasets for initial decision
tasks such as classification or regression. After these
preliminary decisions, the model integrates the individual
predictions from each model. This fusion occurs postdecision or at the decision level, where each modality is
processed independently and their outputs are combined
to make a final decision. This preserves modality-specific
information to the maximum extent. FedMultimodal [53]
delineates a robust framework for the MMFL to process
multisensory inputs. The architecture begins by deploying a
Conv+RNN combination for spatial and sequential data from
sensors, or an RNN-only configuration for purely sequential
data. Following the initial data encoding, a late fusion
strategy amalgamates modality-specific representations into
an integrated multimodal representation. This composite
FIGURE 8. Comparative Fusion Methods in Multimodal Client Architectures (a) Early Fusion: combining features from all modalities at the input level; (b) Hybrid Fusion,
integrating intermediate features from modality-specific networks; and (c) Late Fusion, processing modalities independently and fusing outputs at the decision level.
representation subsequently passes through dual dense layers,
thereby facilitating refined downstream predictive decisions.
This sequential processing and integration strategy preserves
the distinct characteristics of each data type until final fusion,
thereby enhancing the overall decision-making efficacy of the
model. Additionally, it utilizes concatenation and attention
mechanisms specifically designed to address three distinct
types of heterogeneity: missing modality, missing labels, and
label errors. FedMFS [136] introduced a multimodal fusion
FL approach that balances performance and communication
in resource-constrained, heterogeneous MMFL settings. It
uses the late fusion stage, in which predictions from modality
models serve as inputs to the ensemble model. The method
incorporates selective modality communication, recognizing
that clients may not always be able to upload all modality
models
c: Hybrid Fusion Stage Finally, hybrid fusion integrates
diverse modalities at various stages across a distributed
network, employing early and late fusion techniques to
enhance model learning, while maintaining data privacy
and locality. This approach is particularly beneficial in
environments in which clients possess distinct data types,
such as cross-institutional healthcare studies or sensor
networks spread across different geographical locations. For
instance, [153] developed a hybrid feature fusion method
that combines MobileNetV3, a Swin Transformer, and
variational autoencoders for disease detection in robusta
coffee leaves. When evaluated on the RoCoLe database,
the approach achieved an accuracy of 84.3%. Moreover,
it has demonstrated success in tasks, such as identifying
speakers across multiple modalities [154] and detecting
events in multimedia content [155]. Knowledge distillation
(KD) is one of the most widely used methods to transfer
this extracted common knowledge to end clients at various
stages. CreamFL [34] proposed the first KD-based MMFL
architecture that leveraged a contrastive-based methodology
for integrating representations. It distinctively applies a
modality-specific contrastive technique during the local
training phase. While pioneering, CreamFL is implemented
in a supervised environment, which poses challenges, such
as limited training and public dataset availability, owing
to the high costs associated with obtaining labeled data.
However, hybrid fusion methods have been underexplored
within the context of FL. Table 5 and Fig. 8 provide a
detailed comparison of the three fusion stage techniques.
2) COORDINATED REPRESENTATION
Instead of creating a fused representation, a coordinated
representation can be employed. This alternative approach
maintains separate representations for each modality that
are synchronized through the application of a designated
constraint. In addition, it learns multimodally contextualized representations that are aligned by their cross-modal
interactions, functioning in parallel to ensure comprehensive
coherence. An early example of minimizing inter-modal
distances within a coordinated space is presented by
Weston et al. [156] in the WSABIE model. This model
constructs a coordinated space specifically for images and
TABLE 5. Comparison of multimodal fusion techniques.
their annotations using simple linear mapping. This mapping is designed such that the inner product between the
corresponding image and annotation features is maximized,
resulting in a smaller cosine distance than that between
non-corresponding pairs. Clients in MMFL often possess
distinct or partially overlapping data modalities. For instance,
Yang et al. [157] hypothesized that each client manages
a single modality and proposed aFDARN, which is a
framework of five modules tailored for cross-modal federated
HAR.
B. ALIGNMENT
Alignment refers to the identification of relationships,
connections, and interactions among all the components
within a multimodal sample [158]. For instance, consider
situations of speech and human gestures. The objective is
to correlate specific gestures with the verbal expressions
they accompany, thereby enhancing the understanding of
communication [159]. The alignment of heterogeneous data
modalities across distributed nodes, such as audio, visual, and
textual data, is pivotal for model coherence and performance
enhancements. Proper alignment influences the effectiveness
of subsequent stages of model training and application.
Furthermore, the research demonstrated that data derived
from various modalities, such as sensory and visual data,
present in a multimodal client, inherently possess alignment
cues. For instance, the synchronization of local timestamps
between sensory data samples and video frames within the
client facilitates the training of models to derive multimodal
representations from the data [130]. However, prevalent
MMFL methodologies primarily necessitate manual alignment on the client side, focusing on datasets with explicitly
labeled alignments that are often created manually. This
requirement for preprocessing multimodal data or identifying
congruent features across high-dimensional modal data
represents a significant bottleneck, impairing both the realtime performance of algorithms and the efficiency of the
training process [160]. One of the first studies to tackle crossmodal alignment in foundational models, masked language
modeling (MLM), was conducted by [161]. It introduced
a cross-modal transformer, MMFL, designed to discern
alignments and relationships between visual and textual
modalities. Shuai and Shen [162] introduce a novel approach
tailored to address data heterogeneity across vision and
language tasks in healthcare settings. This method, which is
a cross-modal alignment FL strategy, effectively binds local
client data with an ideal alignment model.
A practical method for the alignment of MMFL, such as
audio and video, involves standardizing diverse modalities
into a common feature space. An illustrative example
involves correlating temporal features from audio frequency
intensities with video frame pixel intensities to enhance
applications, such as activity recognition. In this context,
Tan et al. introduced a novel feature alignment method called
FedSea that improves data interoperability across non-IID
datasets [163]. FedSea employs a domain adversarial learning framework that incorporates an affine transform-based
generator to standardize features and a gradient-reversalbased client discriminator to anonymize data origins, thereby
boosting model robustness. The method also features an
attention-based mask module that selectively aligns critical
features, supported by a feature IID confidence quantification
method to evaluate and adjust data uniformity, offering
significant advancement in handling multimodal data in
federated environments. However, feature alignment can
pose significant privacy risks, particularly through potential
feature leakages and inference attacks. As features from
various modalities are preprocessed and transformed to
align them for training, sensitive information might be
inadvertently exposed, even if the raw data remain local.
VI. APPLICATIONS
The remarkable success of multimodal learning has facilitated its deployment in several practical applications.
Many MMFL techniques have enhanced task performance
by aligning these tasks more closely with real-world
demands and learning objectives. This section explores the
diverse applications of MMFL and reviews the cuttingedge literature to elaborate on how MMFL effectively
addresses complex challenges in real-world settings. Table 6
summarizes the key trends in recent MMFL applications,
while highlighting the diversity of tasks, datasets, fusion
techniques, and performance metrics. This reveals that late
fusion is commonly employed in complex tasks, such as
medical diagnosis and activity recognition, reflecting its
effectiveness in integrating diverse modalities. Early fusion
is mainly observed in tasks such as image captioning
and leveraging synchronized data sources. The table also
shows that performance varies widely across applications,
influenced by the nature of the datasets and modality-specific
challenges. For instance, structured clinical data present
unique complexities in healthcare tasks, while cross-modal
tasks emphasize modality alignment. Despite these advances,
gaps remain in reporting fusion strategies and ensuring
consistent performance across diverse datasets. These trends
underline the evolving focus on optimizing fusion techniques
and addressing dataset-specific challenges in the MMFL.
A. EMOTION RECOGNITION (ER)
Emotion recognition seeks to decipher and interpret human
emotions manifested across various modalities including speech content, vocal tone, and facial expressions.
Research has demonstrated that various modalities complement each other in expressing emotions, leading to the
development of numerous effective multimodal fusion techniques that enhance emotion recognition performance [164].
Nonetheless, multimedia data linked to user emotions, such
as chat logs and personal photographs, are susceptible to
privacy. The MMFL provides a robust solution for handling
multimedia data associated with user emotions. Using a
decentralized approach, MMFL enables efficient collaborative training across devices without compromising data
security. Few studies of MMFL have focused on emotion
recognition. A prominent example is [165], where each client
in the network possesses a single modality and unimodal
encoders are trained locally. This hierarchical aggregation
approach groups the encoders according to the type of
modality held by each client and implements an attentionbased mechanism to standardize the decoder weights across
different data modalities. The study was evaluated on
CMU-MOSI and CMU-MOSEI sentiment analysis datasets.
Chen and Zhang [166] introduced the MMFL approach for
ER enabling federated training on diverse multimodal data
without requiring uniform sensors across clients. The core
concept, FedMSplit, utilizes a dynamic multiview graph to
dynamically reflect the correlations between client models by
dividing them into shareable blocks, each offering a distinct
perspective on client interactions. Moreover, Gahlan and
Sethia [167] introduced the F-MERS framework for emotion
recognition, which integrates data from multiple physiological sensors, namely, EEG, GSR, ECG, and RESP. It
employs a Multi-layer Perceptron (MLP) to classify complex
emotions across three dimensions: Valence, Arousal, and
Dominance (VAD). The efficacy of the F-MERS framework
was confirmed by testing it using three benchmark emotion
datasets: DEAP, AMIGOS, and DREAMER.
B. HUMAN ACTIVITY RECOGNITION (HAR)
HAR utilizes data from wearable devices such as accelerometers and gyroscopes to identify human actions. Given its
compatibility with wearable technology, it has emerged as
a significant area of research in the field of FL [168].
MMFL is particularly applicable in environments, including IoT systems, where a distributed array of sensors
consistently captures observations of the same object or
event. Zhao et al. [130] introduced a semi-supervised,
MMFL approach that uses auto-encoders to derive correlated
representations from diverse local data modalities on client
devices. In addition, they developed a multimodal FedAvg
algorithm to aggregate local auto-encoders. The global
autoencoder, trained across different modalities, was then
employed for HAR, utilizing auxiliary labeled data on the
server for classification. Each client, represented as a device,
received an equal division of multimodal data. Subsequently,
a local co-attention mechanism is employed for multimodal
fusion, illustrating the client-as-sensor approach. In [169],
the HAR process involved integrating features from video
and sensor signals, with heart rate signals employed as selfmonitoring data to improve the model performance.
C. HEALTHCARE
In the evolving field of healthcare AI, there is a significant
transition from specialized, unimodal tasks limited to clinical
data or medical scans towards expanding machine capabilities. This expansion involves incorporating a wider range
of clinical information, such as biospecimens and omics
data, to utilize all available input modes together [174].
The fundamental goal of MMML is to enhance the efficacy of DL models by integrating the data from various
sources. This is achieved by simultaneously processing
information from multiple modalities, which is crucial for
tasks that require a thorough assimilation and interpretation
of data across these diverse sources.In addition, diagnosing diseases, including global health challenges such
as COVID-19, often requires analysis of multiple data
types through MMML. For instance, identifying COVID-19
involves lung computed tomography (CT) or X-ray images
and electronic health records [175], [176]. This complexity
presents a significant challenge for healthcare technology.
Consequently, MMFL, which facilitates distributed learning
with multimodal data while ensuring privacy protection,is
a critical solution for addressing these challenges. In
this direction, Agbley et al. [127] targeted the detection
of melanoma using medical images of skin lesions and
associated clinical data, including gender and the lesion’s
malignancy status. In this study, a federated environment
is simulated by distributing the central dataset across five
client nodes. This study adopted the FedAvg algorithm for
model aggregation. Similarly, Ji et al. [177] developed an
MMFL that utilizes multimodal data to identify human
status. The model addresses the challenge of speed variations stemming from device heterogeneity and differing
modal complexities by implementing a rapid and secure
module that substantially reduces data transmission volume.
Validation experiments, which included brain CT images
and a time-series dataset of heart rates, confirmed the
TABLE 6. Summary of recent works on MMFL applications.
viability of MMFL in detecting human states. An et al. [178]
propose an MMFL approach for healthcare using MRI
and PET data from the ADNI dataset [179], achieving
an accuracy of 68.3%. This method groups clients by
modality for efficient aggregation and uses a prototype contrastive strategy for knowledge sharing. Another healthcare
application of MMML is cancer staging,which integrates
imaging, genetic, and clinical data to assess cancer severity [180], [181]. Shao et al. [182] illustrated that the
performance of ML models for cancer staging is significantly
improved by combining histopathological imaging, gene
expression data, and clinical records. To mitigate privacy
concerns associated with MMML, [171] presented a new
FL architecture that addresses data and modality heterogeneity across institutions. Distributed gradient blending and
proximity-aware client-weighting strategies were utilized to
manage the varying convergence speeds among modalities.
Experiments using The Cancer Genome Atlas (TCGA)
datasets [183], involving mRNA sequences, histopathological images, and clinical data, achieved accuracies of
67.84%, 66.65%, and 60.72%, respectively. FedMEMA [135]
presented a robust MMFL framework for brain tumor
image segmentation. It uses four encoders, a multimodal
fusion decoder, and a cross-attention module to handle
the missing modalities. Based on BraTS [184] dataset, it
outperforms prior models, but only addresses inter-modality
heterogeneity, overlooking intra-modality and client-side
variations.
D. VISUAL AND LANGUAGE TASKS
Visual-language tasks integrate visual and textual data,
thereby significantly enhancing applications in augmented
reality, automated content generation, assistive technologies, and information retrieval systems. The application
of MMFL to these domains is essential for addressing
key data privacy challenges and system scalability in
distributed computing environments. This method not only
preserves the confidentiality of user databases, but also
optimizes the complementary strengths of different data
types, resulting in enhanced performance and robustness
of technological solutions. Therefore, some initial studies
investigated the role of MMFL in vision-textual tasks, further
illustrating its importance and utility in complex computing
environments. In this context, Liu et al. [172] presented
a visual textual framework called aimNet that has been
evaluated across various configurations, including horizontal
FL, vertical FL, and Federated Transfer Learning (FTL).
These evaluations were conducted specifically for tasks such
as Visual Question Answering (VQA) and image captioning. Complementarily, Yu et al. [34] harnessed contrastive
learning techniques to ensemble heterogeneous local models
by contrasting their output representations, accommodating
both unimodal and multimodal vision-language tasks, such as
VQA and image-text retrieval within federated frameworks.
Additionally, [173] applied prompt training techniques to
integrate substantial foundational models into FL systems,
thereby enhancing the connection between vision and
language data. Moreover, [139] studied the federated crossmodal retrieval domain, effectively reducing discrepancies in
representation spaces using a weighted aggregation approach
that considers local data volumes and category diversity.
These advancements collectively enrich the robustness and
functionality of technologies in fields leveraging visualtextual interaction while also demonstrating the importance
of MMFL in improving data privacy and system scalability
across distributed networks.
VII. BENCHMARKS AND DATASETS
The widespread availability of diverse sources such as
sensors and mobile devices has driven the increasing utilization of multimodal data. MMFL capitalizes on this by
segmenting multimodal datasets to represent client nodes
that may exhibit homogeneous or heterogeneous characteristics. The proliferation of diverse multimodal datasets has
propelled substantial advancements in MMFL. Given the
extensive range of available datasets, selecting appropriate
data for MMFL research requires careful deliberation. This
section examines the benchmarks of MMF and, analyzes
how different datasets affect the effectiveness and practical
deployment of MMFL in various environments. It specifically emphasizes the selection of publicly available datasets,
ensuring ease of access and reproducibility, which are key
factors for advancing research in this domain.
A. EMOTION RECOGNITION (ER)
The Multimodal EmotionLines Dataset (MELD) [185] is
a comprehensive dataset for multiparty dialogues, featuring
over 9,000 utterances from the “Friends” TV series, complete
with audio recordings and transcripts. Each utterance in this
dataset is labeled with specific emotions and sentiments and
includes data across audio, visual, and textual modalities.
The CREMA-D dataset [186] comprises 7, 442 audio-visual
clips recorded by 91 actors from various ethnic backgrounds.
Each actor performed 12 scripted sentences, depicting six
emotional states: neutral, happy, angry, disgusted, fearful,
and sad. This dataset is particularly valuable for research on
multimodal emotion expressions and perception, containing
both facial and vocal expressions corresponding to basic
emotions. Ratings were gathered across three modalities,
namely audio, visual, and audio-visual, by 2,443 crowdsourced raters who provided both categorical emotion labels
and real-value intensity scores for each perceived emotion.
The CMU-MOSI and CMU-MOSEI datasets [187]
and [188] offer comprehensive resources for emotion and
sentiment analysis within opinionated multimedia content,
respectively. The CMU-MOSI dataset includes 2,199 opinion
video clips, each meticulously annotated with sentiment values ranging from −3 to +3. It features detailed annotations
of subjectivity, sentiment intensity, visual cues annotated
per frame and opinion, and audio features in milliseconds.
Expanding on this, the CMU-MOSEI dataset comprises
23,453 video segments from 1,000 YouTube videos, each
segment enriched with transcriptions and detailed audio and
visual features. This dataset provides extensive annotations
on sentiment, emotion, and intensity levels, facilitating indepth studies on how language, vocal expressions, and
visual data interact to convey sentiments and emotions in
opinionated texts and speech.
The IEMOCAP database [189] is a comprehensive
multimodal dataset tailored for the analysis of emotional
expressions. It includes roughly 12 hours of audio-visual
content, featuring video recordings, speech, facial motion
capture, and corresponding text transcriptions. This resource
is structured around dyadic sessions, where actors perform in
both spontaneous and scripted situations designed to provoke
varied emotional reactions. Annotations in the database
are extensive, with emotions identified by multiple raters
using categorical labels, such as anger, happiness, sadness,
and neutrality, and dimensional metrics, such as valence,
activation, and dominance.
B. HAR
The UCI-HAR dataset [190] captures data from smartphone
sensors, specifically accelerometers and gyroscopes, from
30 individuals aged 19 to 48 years, who performed six
common activities: walking, ascending stairs, descending
stairs, sitting, standing, and lying down. Smartphones were
positioned at the waist of the participants throughout data
collection, with sensor readings recorded at a rate of
50 Hz. Alternatively, the KU-HAR dataset [191] involves a
broader cohort of 90 participants (75 male and 15 female),
documenting 1,945 raw activity samples from 18 distinct
activity classes. Data were also gathered using the builtin smartphone sensors. This dataset further includes 20,750
derived subsamples, each representing 3 seconds of activity
data, meticulously extracted from the original recordings.
The EPIC-KITCHENS-100 dataset [192] offers a largescale egocentric visual corpus that describes individuals’
kitchen activities via audio-visual recordings from headmounted cameras. Spanning 45 kitchens in four distinct
urban settings, this dataset encompasses 100 hours of fullHD video across 20 million frames, providing a diverse
environmental context for detailed visual analysis. The
dataset’s annotations, derived from a novel ‘Pause-and-Talk’
narration interface, include 90,000 action segments and
20,000 unique narrations in multiple languages, supporting
cross-cultural research. It categorizes actions into 97 verb
and 300 noun classes, enabling a precise activity analysis
within kitchen environments. In contrast, the NTU RGB+D
120 dataset [193] was designed for RGB+D human action
recognition, featuring data from 106 subjects and over 114
thousand video samples, with a total of 8 million frames.
This dataset classifies a wide array of 120 action types,
including daily activities, interactive behaviors, and healthrelated actions. It serves as a crucial resource for research
and development in human action recognition, facilitating
progress in computer vision, ML, and artificial intelligence.
C. HEALTHCARE
The PTB-XL dataset [54] comprises over 20,000 clinical
12-lead ECG recordings from 18,885 patients designed for
multi-label classification. The dataset categorizes ECGs into
five diagnostic groups: normal ECG, myocardial infarction,
ST/T changes, conduction disturbances, and hypertrophy.
Notably, it includes a significant number of records from
healthy individuals, which broadens the diagnostic spectrum. The dataset also incorporates extensive metadata such
as demographic details, additional diagnostic evaluations,
probabilities of diagnoses, and expertly annotated signal
characteristics. FLamby [194] is a specialized cross-silo
dataset suite tailored for healthcare research. It comprises
seven distinct healthcare datasets, each featuring natural
divisions to facilitate diverse tasks, modalities, and data
scales. On the other hand, the MIMIC-IV dataset [195]
is sourced from Beth Israel Deaconess Medical Center’s
electronic health records. It is a comprehensive and widely
used database that offers detailed clinical data from ICU
patients. This dataset includes de-identified information,
such as patient measurements, orders, diagnoses, procedures,
treatments, free-text clinical notes, vital signs, laboratory
results, medications, and patient demographics. This is
invaluable for the research and development of algorithms
and models in critical care medicine, clinical decisionmaking, and healthcare analytics.
D. VISUAL-LANGUAGE
The Hateful Memes dataset, derived from the 2020 Hateful
Memes Challenge [196], was designed to identify hateful
speech in memes. It contains 10,000 multimodal instances,
each featuring an image and text pair classified into
binary categories. The dataset is uniquely challenging as
it includes ‘benign confounders’ to discourage reliance
solely on unimodal information. Although this task requires
sophisticated reasoning, it is efficiently evaluated using
binary classification metrics. The Crisis MMD dataset [197]
encompasses 18.1k tweets, each featuring combined visual
and textual elements, sourced from major natural disasters,
including the 2017 California Wildfires. This dataset was
designed to facilitate the analysis of disaster-related impacts,
such as infrastructural damage and human casualties.
The CUB-200-2011 dataset [198] expands upon the
CUB-200 dataset by doubling the number of images per
class and incorporating new annotations for part locations,
thereby establishing itself as a prominent resource for
fine-grained categorization studies. It encompasses 11,788
images, divided into 200 subcategories. Comprehensive
annotations for each image are provided, including a subcategory label, bounding box, 15 specific part locations, and
312 binary attributes. The Oxford 102 Flower dataset [199] is
a specialized dataset designed for fine-grained classification
that includes 102 common flower varieties in the United
Kingdom. Each flower category comprised 40–258 images,
with each image supported by 10 textual descriptions. The
dataset also introduced an expanded set with 103 flower
classes. It features analyses based on four distinct attributes:
local shape and texture, boundary shape, spatial petal
distribution, and color, thereby providing comprehensive
insights into various floral characteristics. The Food-101
dataset [200] is a multimodal classification dataset with a
distinct structure that features images paired with captions
across 101 food categories. It comprises 101,000 images
divided into 750 training images and 250 testing images
per category. While the training set contained some label
and caption noise, potentially affecting the clarity of the
label information, the testing set was meticulously cleaned
to remove such inconsistencies.
VIII. OPEN ISSUES AND FUTURE DIRECTIONS
MMFL is an emerging and exciting area of research that
is gaining significant attention because of its potential to
revolutionize the use of diverse data modalities in distributed
learning environments. This section systematically identifies
and discusses open issues and future research directions in
this dynamic field.
A. FEW SHOTS AND SELF-SUPERVISED LEARNING
In real-world applications of MMFL, DL models rely heavily
on large amounts of labeled data. However, the acquisition
of extensive labels in complex decentralized environments
is challenging. The diverse nature of multimodal data
distributed across multiple clients often leads to insufficient data volume and scarce labeled examples, which
can hinder the model performance [201]. Refining feature
representations from small samples, merging knowledge
across modalities, enhancing task-specific processing with
limited data, and extending generalization to FL settings
further compounded these challenges [202]. Exploring fewshot and self-supervised learning methods offers promising
solutions. Few-shot learning reduces dependency on extensive annotations by enabling models to learn from minimal
labeled data. Recent advances in meta-learning and prototypical network approaches, such as adapting MAML for
multimodal settings, allow models to rapidly adjust to new
tasks by leveraging shared representations across modalities
and effectively handling client data heterogeneity. Selfsupervised learning leverages the abundance of unlabeled
data to extract useful feature representations using techniques
such as contrastive learning, cross-modal alignment, and
clustering-based methods. For instance, designing pretext
tasks that align audio and visual cues can enhance joint
feature extraction even in the absence of labels. Nevertheless,
these approaches must overcome challenges including noisy
data, class imbalance, and inconsistent data quality across
clients.
The real-world deployment of these methods also faces
challenges related to computational resources, communication overhead, and data heterogeneity. Implementing
few-shot and self-supervised strategies in MMFL requires
addressing network latency, synchronization issues, and
scalability of meta-learning algorithms in distributed environments. Adaptive mechanisms that balance local learning
with global model updates are essential for ensuring efficient resource utilization and robust performance. Future
research should focus on developing domain-specific fewshot techniques tailored to multimodal heterogeneity and
robust self-supervised frameworks that can handle noisy
and imbalanced datasets. Further exploration of embeddingbased strategies, crossmodal augmentation techniques, and
domain adaptation methods will be critical. Combining
these approaches with personalized or hierarchical federated
learning can further enhance the generalization across diverse
clients.
B. PRIVACY AND SECURITY CONCERNS
Although protecting client data from potential intrusions and
leaks is inherent in the fundamental principles of federated
learning, the integration of multimodal data exacerbates
privacy risks compared with unimodal FL. In unimodal
FL, each client typically processes a single data type,
limiting the potential for crossmodal inferences. However,
the diverse nature of multimodal data increases the risk
of user re-identification because complementary information
from different modalities can be combined to reveal sensitive
details [203]. Moreover, the fusion techniques used in MMFL
produce richer feature representations, which adversaries can
exploit through inference attacks [204], [205]. For instance,
an attacker may deduce critical information from one modality that, when correlated with another, poses a significant
threat to client privacy. The application of conventional
defense mechanisms, such as differential privacy [206] and
homomorphic encryption [207] to MMFL is particularly
challenging because different data modalities provide varying
levels of information granularity. This variation complicates the task of achieving an optimal balance between
privacy protection and model performance.] In scenarios
where modality heterogeneity is significant, local model
architectures can vary widely between clients, increasing the
risk of information leakage during the aggregation process.
These challenges underscore the special privacy-preserving
issues unique to multimodal FL compared to their unimodal
counterparts.
To address these challenges, future research should focus
on developing local differential privacy methods specifically
tailored for multimodal data environments. It is essential
to design adaptive aggregation strategies that dynamically
adjust the weighting of each client’s contribution based
on the quality, sensitivity, and reliability of their data. In
addition, there is a need to establish context-aware privacy
budgets that can be dynamically adjusted according to the
sensitivity of each modality. Advanced cryptographic techniques, such as secure multiparty computation adapted for
multimodal data, may also help mitigate information leakage
while preserving the model performance. These research
directions are key to strengthening privacy-preserving mechanisms in MMFL and ensuring that the benefits of integrating
diverse data sources can be realized without compromising
client privacy.
C. REASONING
As discussed earlier, fusion techniques in MMFL integrate
different data modalities to capture and leverage crossmodal interactions. This fusion process represents the initial
step in handling multimodal data. Following fusion, the
alignment phase is essential, as it identifies and maps the
connections between various modalities. These connections
often arise from complementary information shared across
different modalities, rather than from the unique information
present in a single modality [208]. After alignment, the
reasoning phase is initiated, in which the system synthesizes
and derives knowledge from the combined multimodal
evidence through multiple inferential steps to address specific tasks. Currently, research on reasoning within the
MMFL context is limited. Therefore, future work should
explore explainable MMFL frameworks, knowledge graph
integration, and sequential inference approaches to transform
fused multimodal data into actionable knowledge. Integrating
interpretable reasoning processes with FL frameworks will
be particularly valuable in sensitive applications such as
healthcare and autonomous systems, where transparency and
explainability are critical.
A promising implementation strategy is to develop
modular reasoning architectures that incorporate dedicated
submodules for fusion, alignment, and inference. For example, designing deep neural networks with explicit attention
mechanisms to align features from different modalities may
improve interpretability and facilitate sequential reasoning.
In addition, leveraging knowledge graphs to represent intermodal relationships can enable dynamic and explainable
inferences. However, potential challenges include increased
computational complexity associated with multi-step inference processes and the difficulty of integrating these modules
in decentralized environments, where communication delays
and model heterogeneity can impair real-time reasoning.
Real-world applications must address scalability issues and
the need for robust error handling in critical domains such
as medical diagnosis or autonomous navigation.
D. KNOWLEDGE TRANSFER AND DISTILLATION
Although knowledge transfer and distillation have
been extensively studied and applied in unimodal
FL [209], [210], [211], their potential in MMFL remains
largely unexplored. These techniques offer promising
avenues for addressing key challenges in MMFL, such as
managing heterogeneous data, improving communication
efficiency, and enhancing model performance in resourceconstrained environments. Knowledge transfer can improve
the generalization of multimodal models by enabling the
sharing of learned representations between clients operating
in different data modalities. In MMFL, where clients
may have access to varying combinations of modalities,
leveraging knowledge transfer allows models to benefit from
the complementary information present across modalities,
even if certain clients only have access to a subset
of them. This cross-modality knowledge exchange can
enhance overall performance, particularly in scenarios with
diverse and non-IID data distributions. However, knowledge
distillation can be pivotal in addressing communication
and computational constraints that often arise in MMFL.
By distilling the knowledge from larger, more complex
multimodal models into smaller, more efficient ones, it
is possible to significantly reduce the model size and the
bandwidth required for communication between clients and
the server. This process preserves key insights from the
original model while making it feasible for deployment in
environments with limited computational resources, such as
edge devices and IoT systems.
An effective implementation approach involves the development of hybrid teacher–student frameworks tailored to
multimodal data, where a large, centralized multimodal
teacher model transfers knowledge to smaller, modalityspecific student models. Techniques such as iterative
distillation and adaptive layer-wise training can be investigated to optimize the balance between the performance
and communication overhead. In terms of real-world challenges, issues such as handling missing modalities, managing
modality-specific noise, and ensuring that distilled models
maintain robustness in diverse client environments must be
addressed. Moreover, system heterogeneity and variability
in local computational resources can complicate the distillation process, which requires adaptive algorithms that can
dynamically adjust to different client conditions.
E. RESOURCE-CONSTRAINED MMFL
Resource-constrained MMFL is a critical area of research
that addresses the challenges posed by the limited computational, communication, and energy resources of edge devices
participating in MMFL. Traditional MMFL systems often
assume sufficient resources for training and communication;
however, real-world deployments involve mobile phones, IoT
sensors, and embedded systems that operate under strict
resource constraints. These constraints exacerbate existing
challenges in MMFL, such as the computational cost of
training large multimodal models, bandwidth required to
transmit updates, and energy consumption associated with
these processes. The heterogeneity of client devices further
complicates the landscape as capabilities and resource availability can vary significantly. Addressing these limitations is
essential for ensuring the scalability and feasibility of MMFL
in practical scenarios. To overcome these challenges, future
research should focus on developing lightweight multimodal
architectures that maintain performance while reducing
resource demand. Techniques such as model compression, including quantization and pruning, can significantly
reduce the size and computational complexity of multimodal
models. Federated knowledge distillation offers another
promising approach that allows edge devices to train smaller
models that approximate the performance of larger models.
Adaptive communication strategies, such as periodic or selective updates based on client importance or data relevance,
can mitigate bandwidth constraints while maintaining model
quality. Energy-efficient training algorithms that optimize
computational processes on resource-limited devices are also
crucial for minimizing the power consumption.
A promising strategy is to design adaptive multimodal
models that dynamically adjust their complexity based on
the resources available for each client. For example, models
can selectively activate or deactivate certain modalities or
layers, depending on the current computational or energy
constraints. Implementing edge-aware update protocols that
affect device capabilities and network conditions can further
enhance efficiency. The potential challenges in real-world
applications include the variability of device hardware,
unpredictable network connectivity, and trade-off between
model accuracy and resource consumption. These factors
necessitate robust algorithms that can adapt to highly
dynamic environments, while maintaining a consistent level
of performance and ensuring data privacy.
F. FEDERATED MULTIMODAL FOUNDATION MODELS
(FMFMS)
FMFMs offer a transformative approach to MMFL by
leveraging pretrained foundational models to address the
critical limitations of traditional federated systems. Existing
FL frameworks face challenges such as data heterogeneity, limited generalization across diverse modalities, and
significant computational and communication overheads.
FMFMs overcome these issues by utilizing pretrained
multimodal architectures that learn unified representations
across modalities and can be fine-tuned for heterogeneous
client data. Techniques such as model partitioning and
sparse updates ensure scalability on resource-constrained
edge devices, whereas privacy-preserving mechanisms such
as differential privacy and secure aggregation enhance
both security and efficiency. FMFMs have wide-ranging
applications, including the privacy-preserving integration
of patient records, medical imaging, and biosignals for
healthcare diagnostics, as well as optimizing decision making
in autonomous vehicles through federated sensor data. Future
research should focus on dynamic knowledge fusion to
address evolving or incomplete modalities, scalable finetuning methods for federated settings, and domain-specific
FMFMs tailored to specific application demands. Despite
their promise, challenges such as scalability, privacy, and
standardization must be addressed to ensure real-world
feasibility. A promising implementation strategy for FMFMs
is to develop modular fine-tuning techniques that allow
partitioning and selective updating of foundation models
based on client-specific modality availability. Advanced
methods such as continual learning and transfer learning
tailored for multimodal data can be employed to maintain
model relevance over time. Potential challenges in real-world
applications include integrating these models into the existing
infrastructure, managing the trade-offs between personalization and generalization, and ensuring that privacy-preserving
measures do not excessively hinder performance. Moreover,
standardizing communication protocols and updating mechanisms across diverse client devices is critical for practical
deployment of FMFMs in decentralized environments.
IX. CONCLUSION
In this survey, we provide a comprehensive analysis of the
emerging MMFL fields. We began by examining UMFL
and summarizing its methodologies for handling unimodal
data before delving into the intricacies of multimodality,
distinguishing it from cross-modal learning, and discussing
its broader implications for ML and FL. Particular emphasis
was placed on MMFL transformers, which have proven
to be instrumental in managing and integrating complex
multimodal data across decentralized systems. We introduced
a taxonomy for MMFL, categorizing key challenges and
suggesting potential solutions within this framework, while
exploring practical applications to underscore the real-world
relevance and transformative potential of MMFL techniques.
We also provide a detailed overview of the relevant
benchmarks and datasets that offer valuable resources to
researchers and practitioners. Finally, we outline future
directions and unresolved challenges in MMFL, emphasizing areas requiring further exploration to advance the
field. MMFL is expected to significantly influence nextgeneration technologies, ranging from intelligent healthcare
systems and autonomous vehicles to smart cities and
immersive augmented reality environments. As the demand
for advanced and scalable solutions grows, ongoing research
in MMFL will address current limitations while unveiling
transformative opportunities that drive innovation and shape
decentralized learning and data integration.
