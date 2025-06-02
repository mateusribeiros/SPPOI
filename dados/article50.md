Title: Addressing Technical Challenges in Large Language Model-Driven Educational Software System

ABSTRACT The integration of large language models (LLMs) into educational systems poses
significant challenges across several key attributes, including integration, explainability, testability, and
scalability. These challenges arise from the complexity of coordinating system components, difficulty
interpreting LLM decision-making processes, and the need for reliable, consistent model outputs in varied
educational scenarios. Additionally, ensuring scalability requires robust autoscaling mechanisms and suitable
architecture design to handle fluctuating workloads. This paper tackles these challenges by proposing tactics
to improve system integration, enhance explainability through metadata and an algorithm process, ensure
response consistency via regression testing, and facilitate efficient autoscaling through an event-driven
microservice architecture. The evaluation results highlight the effectiveness of these tactics, confirming both
functional consistency and robust system performance under varying loads.
INDEX TERMS Artificial intelligence, educational application, generative AI, large language model, LLM.

I. INTRODUCTION
Personalized education is an instructional approach tailored
to meet the unique needs, preferences, and learning styles
of individual students [1]. By focusing on each learner’s
strengths and weaknesses, personalized education aims to
enhance engagement and improve academic outcomes. However, developing effective personalized education systems
presents several challenges, including ensuring seamless
integration of various educational resources, maintaining
data privacy, and creating adaptable curricula that can
evolve with student progress [2]. Additionally, teachers often
face difficulties tracking student performance and providing
timely recommendations in a personalized context [3].
The integration of large language models (LLMs) in education has revolutionized personalized learning by providing
adaptive learning experiences that can respond in real time
to student inputs [4], [5]. LLMs are equipped to analyze
vast amounts of data from diverse sources, including student
behavior, progress, and performance metrics, to generate
personalized content [6]. This capability allows educators to
present customized learning materials that align with each
student’s learning style, needs, and progress[7]. Furthermore,
LLMs can offer targeted feedback based on individual
responses, helping learners address specific challenges and
improve performance more effectively [8]. In addition to
content generation and feedback, LLMs facilitate dynamic
interactions by simulating conversations, conducting assessments, and guiding learners through complex topics in
a conversational and engaging manner. These features
enhance the learning experiences, making education not
only more accessible but also more impactful. As educators
leverage LLMs to create customized learning pathways,
they can better support students with diverse backgrounds,
allowing for real-time adjustments in instruction that foster
a more inclusive, adaptable, and responsive educational
environment [9], [10]. This integration aims to guarantee
that students receive the personalized support necessary for
academic success.
Incorporating LLMs into educational software systems
presents several challenges supporting key system attributes,
such as integration, explainability, testability, and scalability.
Firstly, integration challenges stem from managing reasoning
traces and ensuring smooth interactions between system
modules. Secondly, explainability remains difficult because
of the opaque nature of LLMs, making interpreting their
decision-making processes a challenge and hindering user
trust. Thirdly, testability is a challenge, as ensuring consistent
and reliable outputs demands sophisticated testing methods to
assess model behavior accurately. Lastly, scalability must be
addressed, as educational systems need to dynamically adapt
to varying workloads. Robust autoscaling mechanisms are
essential for maintaining system performance during highdemand scenarios. However, they require a well-designed
architecture to function effectively. This paper addresses
these technical challenges in detail and proposes tactics to
overcome them, including the following:
1) A novel design pattern called the chain of reasoning
and action, which breaks down the LLM-driven
system into functional components, facilitating better
integration.
2) The metadata and algorithm to maintain explanations,
supporting debugging and auditing of LLM-driven
functions.
3) Regression testing to measure response consistency in
LLMs, helping identify the most suitable models and
prompts for specific requirements.
4) An event-driven microservice architecture that enables
autoscaling, ensuring the system can handle increasing
loads efficiently.
The remainder of this paper is organized as follows:
Section II discusses the limitations of LLMs in education
and explores the technical aspects of applying them to educational applications. Section III addresses the development
challenges in these systems. In Section IV, we present the
proposed tactics to overcome these challenges, which are
subsequently implemented and evaluated in an educational
application. The evaluation results are provided in Section V.
Section VI compares other LLM-driven personalized education systems with ours. Finally, the paper concludes in
Section VII.
II. LLMs IN EDUCATIONAL APPLICATIONS
LLMs provide significant benefits across a wide range
of applications. One key strength lies in their ability to
imitate understanding and generate human-like text with
remarkable accuracy and coherence [11]. This capability
enables LLMs to automate a variety of repetitive tasks across
numerous domains, including customer service, healthcare,
legal services, and education.
For example, educators can leverage LLMs to generate
high-quality educational content, such as quizzes [12], lesson
plans, and instructional materials [9]. LLMs can assist with
personalized tutoring, generate tailored lesson plans, and
provide instant feedback to students, reducing the burden
on educators and enhancing the learning experience [13].
LLMs can make educational resources more accessible by
adapting content to support different audiences with diverse
backgrounds. For instance, they can simplify complex texts
for younger audiences or those with learning difficulties,
providing all students access to the curriculum [14]. While
LLMs hold significant promise for personalizing education,
one study suggested that the quality of content generation
depends on various factors, such as the prompts used and
the amount of context provided. One critical challenge is
minimizing hallucinations, where the model generates inaccurate or fabricated information that appears plausible but
lacks factual grounding. Addressing this issue is essential for
achieving reliable outputs in educational applications [15].
These limitations can be addressed through prompt engineering and retrieval-augmented generation techniques.
A. PROMPT ENGINEERING
Prompt engineering is an important discipline within natural
language processing (NLP) that involves designing and refining input prompts to optimize the performance of language
models, particularly LLMs. As these models are increasingly
deployed in various applications, the effectiveness of their
outputs largely hinges on the structure and specificity of the
prompts provided. Numerous prompt engineering techniques
have been proposed:
Few-shot prompting [16] improves model performance by
providing demonstration examples. This technique facilitates
in-context learning, enabling the model to generate responses
based on the conditioning provided by these examples.
However, despite its effectiveness, few-shot prompting has
limitations, particularly when dealing with complex reasoning tasks. In such cases, the model may struggle to produce
accurate responses, as it relies heavily on the quality and
relevance of the provided examples.
Meta prompting [17] offers a structured and abstract
approach to interacting with LLMs, emphasizing the format
and syntax of tasks over specific content. This leads to
increased token efficiency, fair comparisons between models,
and improved performance in complex reasoning tasks.
While it can enhance performance in familiar scenarios, its
effectiveness may decline when applied to some particular
new tasks.
Chain-of-thought (CoT) prompting [18] enhances complex reasoning capabilities by incorporating intermediate
reasoning steps, making it especially effective when combined with few-shot prompting. While CoT prompting
significantly improves reasoning ability, it may still struggle
with certain reasoning tasks, particularly when the examples
provided do not cover the necessary diversity of input
scenarios. To address these challenges, researchers have
proposed approaches like automatic CoT (Auto-CoT) [19],
which automate the generation of reasoning chains but may
still encounter errors if not sufficiently diverse.
React prompting [20] (ReAct) (ReAct) enables LLMs to
generate reasoning traces alongside task-specific actions,
facilitating dynamic interactions with external knowledge
sources. This approach improves the reliability and interpretability of LLM outputs, particularly in language and
decision-making tasks. ReAct often outperforms traditional
prompting methods, particularly in knowledge-intensive
tasks like question answering and fact verification. However,
it still faces challenges, including a reliance on the quality of
retrieved information, which can affect reasoning accuracy.
These prompt engineering techniques tackle the education
domain well, offering various opportunities for enhancing
learning experiences and outcomes. For instance, few-shot
prompting and ReAct can be particularly beneficial in
creating adaptive educational tools that provide personalized
feedback and support to students based on their specific
needs. By leveraging these techniques, educators can develop
systems that not only assess student understanding more
effectively but also guide learners through complex problemsolving processes. Meta and CoT prompting can enable the
tutoring systems to present content in a structured manner that
aligns with learners’ cognitive processes. This can facilitate
deeper understanding and retention of material as students
are guided through the logical steps required to arrive at
solutions.
While these techniques can be beneficial, their effectiveness relies heavily on the quality of the context provided in
the prompt. Therefore, additional techniques are needed to
enhance content generation in LLMs.
B. RETRIEVAL-AUGMENTED GENERATION
In education, retrieval-augmented generation (RAG) offers
significant potential by enhancing language models for
knowledge-intensive tasks [21]. Unlike general-purpose
models used for basic tasks, like sentiment analysis, RAG
integrates information retrieval from external sources, such
as Wikipedia, textbooks, and websites, to support factual
accuracy and mitigate the hallucination issue. As shown
in Figure 1, the input prompt is used to retrieve relevant
context from external sources. This retrieved context is then
combined with the prompt and fed into the LLM to generate
a response.
These external sources ensure more reliable and up-todate responses, particularly when dealing with evolving
information. The integration of a vector store plays a crucial
role in this process. A vector store is a specialized database
FIGURE 1. Process of retrieval-augmented generation.
that stores data in the form of vectors, which are numerical
representations of text or other data types. This enables
efficient similarity searches, and the system can retrieve
relevant information quickly based on user queries.
In RAG, the vector store operates by converting
both queries and external knowledge sources into a
high-dimensional vector space and matching them accordingly. This is achieved using embedding models [22], which
convert sentences into vectors that capture their semantic
meaning. Both commercial and open embedding models
are available, such as OpenAI’s text-embedding-31
and the
Instructor model.2 The generated vectors vary in length
depending on the model used. The length of the query vector
must match that of the vectors stored in the vector store for
effective retrieval and accurate similarity comparisons.
When a student submits a query, it is converted into
a vector representation using the embedding model. The
system then conducts a similarity search within the vector
store to locate the closest matching vectors, which correspond
to the most relevant learning materials or resources. These
retrieved results are then integrated with the generative
abilities of LLMs to provide context-rich, accurate responses
tailored to the student’s learning needs. By leveraging the
strengths of both retrieval and generation, RAG can provide
students and educators with precise, real-time information,
making it particularly useful for research, fact-checking,
and dynamic learning environments, where knowledge is
continuously updated. This approach significantly enhances
the educational experience by giving learners access to the
latest and most relevant information tailored to their specific
queries.
III. KEY TECHNICAL CHALLENGES
Developing software systems that incorporate LLMs presents
a complex challenge. Unlike traditional software systems,
LLM-driven systems exhibit distinct characteristics that
necessitate careful attention during the design and development processes. These attributes are discussed in the
following subsections.
A. INTEGRATION
Developing LLM-driven systems, particularly for supporting
RAG, presents notable challenges in managing reasoning
traces and connecting various system modules. In LLM
systems, accurate responses often depend on a series of
prompts that construct sequential reasoning paths, with each
step relying on the successful execution of the previous
one. This interdependence necessitates careful coordination
during the development process so that modules effectively
communicate and share data, maintaining coherent reasoning
chains.
The integration of diverse components, such as the prompt
generator, vector store, and external data sources, adds further
complexity to the development process. Developers must
establish clear interfaces and protocols for these components
to work together seamlessly. This involves not only technical
implementation but also thorough documentation and testing
to preserve reasoning traces and ensure they accurately reflect
the logic of the prompts issued.
Although existing frameworks, like LangChain, offer
valuable tools for building LLM-driven applications and
RAG, they face limitations in supporting the aforementioned
requirements. Notably, the reasoning paths must be handled
and processed on the same machine, which can lead
to scalability issues and restrict the system’s ability to
leverage distributed resources. This constraint can impede the
performance of LLMs, particularly when managing complex
multi-prompt scenarios, such as those encountered in the
education domain or when high responsiveness is essential
in dynamic environments. Thus, addressing these limitations
is essential for the successful integration and deployment of
LLM-driven systems in practical applications.
B. EXPLAINABILITY
A key development challenge in LLM-driven systems is
explainability. Unlike traditional software systems, where
each operation is deterministic and traceable, LLMs operate
as black boxes, making their decision-making process
opaque. This lack of transparency poses significant challenges, especially in critical domains, such as healthcare,
education, and finance, where understanding how decisions
are made is crucial. Developers must design mechanisms
that allow users to trace the logic behind LLM-generated
outputs to build trust in the system’s decisions. Without such
transparency, users may struggle to interpret or rely on the
model’s results, particularly when the outputs impact highstakes situations.
Addressing this challenge involves adding complexity to
the development process. Achieving explainability in LLM
systems requires incorporating components that can break
down reasoning steps or link outputs to relevant data sources,
allowing users to trace the rationale behind a response.
This not only enhances transparency but also helps identify
potential errors or biases in the model’s decision-making
process. However, implementing these features demands
significant engineering effort, as it introduces additional
layers of logic and control. Consequently, it increases design
complexity and computational overhead, often necessitating
more advanced infrastructure and optimization techniques to
maintain system performance at scale.
The need for auditing and debugging adds another layer
of complexity when prompts are crucial for LLM-driven
systems. As LLMs rely on intricate reasoning paths generated
by various prompts, maintaining a detailed audit trail of
these interactions becomes vital to identify errors or inconsistencies effectively. Without robust auditing mechanisms,
tracing back through complex interactions to understand
the origins of a particular output can be challenging,
complicating debugging efforts. Ensuring that all prompts
and their outcomes are documented meticulously is essential
for not only improving the system’s reliability but also
meeting regulatory requirements in sensitive sectors. Thus,
the interplay between explainability, auditing, and debugging
presents a multifaceted challenge that developers must handle
when developing LLM-driven applications.
C. TESTABILITY
Testability in LLM-driven systems presents unique challenges, especially when it comes to ensuring consistent
responses through prompt adaptation. Traditional software
testing relies on deterministic outputs for given inputs,
making validating and realizing predictable behavior relatively straightforward. However, LLM-driven systems are
probabilistic in nature, meaning that even slight variations
in prompts can lead to different outputs, making consistency
difficult to achieve.
Response consistency is particularly challenging because
LLMs rely heavily on prompt engineering. Small changes
in wording, structure, or context can yield unpredictable
variations in the output, making the standardization of
responses across different scenarios difficult. Testing for
consistency thus requires a comprehensive suite of test cases
and an understanding of how variations in prompts may affect
outputs, which can be difficult.
Moreover, LLMs may exhibit behavioral changes because
of model updates or variations in the models used, leading
to inconsistencies in the responses generated over time.
This makes regression testing essential to ensure that any
modifications to the model do not negatively impact the
accuracy or reliability of the system’s outputs. Traditional
unit tests are often inadequate, as they fail to account for the
subtleties of prompt sensitivity and the inherently dynamic
nature of LLM outputs. Comprehensive testing strategies
must, therefore, go beyond conventional approaches to
effectively capture and address these challenges.
Developers need to implement sophisticated validation
techniques, including testing across a wide range of prompts
and scenarios and even human-in-the-loop evaluations,
to assess the consistency and reliability of responses. This
adds a significant burden to the development process,
as prompt adaptation and iterative testing become necessary
to optimize system behavior while maintaining accuracy and
coherence.
D. SCALABILITY
Scaling an LLM-driven system composed of interconnected
components introduces significant challenges related to
reliability and performance. This complexity is heightened
when the system requires multiple prompts to build reasoning
traces and integrate external data sources, such as in RAG.
Each module typically performs a specialized function, such
as data retrieval, prompt, or response generation. Their
coordination is critical for smooth system operation.
From a scalability perspective, the reliance on sequential
processes presents a key challenge. For instance, reasoning
traces in LLM systems depend on multiple prompt executions, each of which must be completed in a timely and
accurate manner for the system to proceed effectively. If any
one component encounters an issue, such as a network
delay or processing bottleneck, the performance of the entire
system is compromised. As the system scales, the potential
for such delays or disruptions increases, making designing
for resilience crucial.
To overcome these obstacles, implementing scalability
solutions, such as load balancing, parallel processing, and
distributed architectures, becomes essential. However, incorporating these scalability measures introduces complexities.
For instance, while distributed systems increase capacity,
they also require sophisticated orchestration mechanisms to
synchronize tasks and ensure that modules remain aligned.
Moreover, implementing fallback strategies and redundancies
adds to the overall computational overhead, potentially
impacting performance if not managed correctly. Therefore,
balancing the trade-offs between reliability, performance,
and scalability requires a thoughtful architectural design that
anticipates growth while maintaining system integrity.
IV. PROPOSED PERSONALIZED EDUCATION SYSTEM
This section introduces AITeach, a personalized education
system. The system analyses student data in real time to
provide tailored educational experiences that dynamically
adapt to individual learner needs. By employing proposed
design and development tactics to address the technical
challenges discussed in Section III, AITeach enhances the
learning experience with reliability and effectiveness.
Figure 2 illustrates the overall process by which AITeach
generates content from provided learning materials. In an
LLM-driven system, the accuracy of content generation relies
significantly on the context provided in the prompt. The
vector store plays a crucial role in this process, as it contains a
collection of high-dimensional representations of data points,
known as embeddings.
Embedding models convert learning reference materials
presented in various raw data formats, such as document
files, text, and images, into high-dimensional vectors. This
transformation enables the system to capture the semantic
meaning of the learning materials, allowing for more nuanced
FIGURE 2. Content personalization by AITeach.
and contextually relevant responses to the students. AITeach
enables instructors to upload reference materials in formats
such as PDF, DOC, and PPT, which are then converted into
high-dimensional vectors through indexing. This process is
managed by the Indexer component, as outlined in steps
a1 and a2 (as shown in Figure 2). When these sources are
updated, re-indexing keeps the information current.
When a student submits a question, the Generator
component first retrieves both the lesson objectives and the
question before querying the vector store, as outlined in steps
b1 to b3. This triggers AITeach to find relevant embeddings
that align with the lesson goals and the student’s inquiry.
The system then combines the prompt with the retrieved
context to send to the LLM, which generates the response for
the student, following steps b4 and b5. Finally, the LLM’s
response is processed and saved in data storage for future
access, as described in steps b6 and b7. The remainder of this
section discusses the tactics proposed in developing AITeach
to address various technical challenges.
A. ACHIEVING INTEGRATION
AITeach is designed as a workflow-based application, where
each lesson consists of structured learning activities assigned
to the student. As the student completes each task, the
system dynamically updates their progress, assessing their
performance and adapting the learning path accordingly.
The determination of the next task is based on the ReAct
prompting concept, which combines reasoning traces with
task-specific actions to provide adaptive and contextually
relevant next steps.
To address the integration challenges, we employ a design
tactic inspired by the chain-of-responsibility pattern [23],
which we adapt into what we term the chain-of-reasoningand-action pattern. In the chain-of-responsibility pattern,
components are treated as independent units, each responsible for a specific aspect of data processing. These components
are organized in a sequence, each performing its designated
task before passing the data to the next. The formula below
FIGURE 3. Workflow integration.
formally represents the flow of data through a sequence of
components in a chain-of-reasoning-and-action pattern:
Mn
out = A

R
n

R
n−1

. . . R
1

M1
in, P
1
 , P
n−1

, P
n

where Mn
out represents the final output and M1
in denotes the
initial input. Each module employs a reasoning function
R
i
that processes the input according to the ith parameter
P
i
, with the output of one reasoning step serving as the
input for the next, facilitating a continuous flow. The final
action A signifies the culmination of this reasoning sequence
into the output, representing the determination of the action.
This structure underscores the modular nature of the system,
enhancing scalability and maintainability while supporting
traceability and ensuring consistent reasoning throughout.
The chain of reasoning and action is integrated into the
design of AITeach, as illustrated in Figure 3. The process
begins when the student updates a learning task as an initial
input to the chain. The Event Trigger component captures
this update, extracts the necessary information, such as the
progress made, and forwards it to the Thinker component.
The Thinker generates a thought based on the task data,
leveraging a prompt from the LLM to simulate cognitive
processing. These insights are then passed to the Planner
component, which analyses the information to determine the
next appropriate task from a set of available options. Once the
decision is made, the Worker component creates the next task
for the student to complete.
The chain-of-reasoning-and-action pattern is highly effective for managing complex data processing tasks because of
its support for modularity and separation of concerns. Each
component is dedicated to a specific function, such as data
collection, validation, transformation, or decision-making,
ensuring that changes within one component do not propagate
to others. This architecture facilitates ease of maintenance
and scalability, allowing for seamless integration of new
components with minimal disruption to the overall system.
Furthermore, it enhances system traceability by enabling each
component to document its reasoning process, simplifying
debugging and auditing procedures.
FIGURE 4. Metadata in AITeach.
B. ACHIEVING EXPLAINABILITY
To achieve explainability in AITeach, we adopt specific
tactics that support debugging and auditing procedures,
providing transparency in the system’s decision-making
process. Explainability in this context is essential not only
for building trust in the generated outputs but also for
allowing instructors and system administrators to review and
assess student progress accurately. One key tactic involves
creating metadata for each learning task, which store vital
information, such as the student’s score, the timestamp of the
task, and any contextual details relevant to that specific task.
These metadata serve as the foundation for creating an
observation entity for each learning task, capturing the
current state. In educational applications like AITeach, this
entity stores a detailed record of student progress and
provides a natural expression of how students progress
through their lessons, allowing both instructors and the
system to trace the learning process.
Algorithm 1 Generate Observation
Require: activities is a list of possible activities
Require: last_task is information of the last task
Initialize activities_txt and latest_state as empty strings
for each activity in activities do
Append activity details to activities_txt
if activity name matches last_task’s activity then
Update latest_state with lesson and progress
break
return activities_txt, latest_state
The observation is generated by the Thinker component
using the information from the last task, as described
in Algorithm 1. This observation comprises two key
components—activitiest xt and latests
tate—both of which are
included in the prompt for the Planner. The algorithm takes a
list of possible activities, activities, from the lesson and the
details of the last task as input. In AITeach, the activities
list includes a variety of tasks, such as pretests, lectures,
exercises, and quizzes. The algorithm iterates through these
activities to 1) compile all activity details into activitiest xt
FIGURE 5. Observation in AITeach.
FIGURE 6. Prompt to think.
and 2) locate the activity matching the last task, updating
latests
tate with relevant details, like the activity’s objective,
lesson, and specific information from the last task, such as
progress. Figure 1 presents a sample observation generated
by Algorithm 1. This observation includes various data that
represent the current state of the learning task performed by
the student.
After the observation is created, the Thinker component
generates a thought by issuing a prompt to the LLM.
As illustrated in Figure 6, this prompt is structured into
three distinct sections: system, observation, and response.
The system and observation sections collectively establish
the context for the interaction. Specifically, the system part
assigns the LLM its role as an interactive agent, while
the observation part provides the necessary background
information to guide the interaction. The response section
remains empty, allowing the LLM to produce a contextually
appropriate output. The response generated by the LLM
becomes an integral part of the prompt for the subsequent
planning step.
The Planner component leverages the thought generated
by the Thinker component to plan the next task by prompting
the LLM, as illustrated in Figure 7. The prompt consists
of three parts: system, thought, and response. The system
part provides a list of possible activities along with the
conditions for executing each, instructing the LLM to select
the appropriate task. The thought part reflects the output from
FIGURE 7. Prompt to plan.
the Thinker component. The next task is determined based
on these predefined conditions, and the LLM’s response
identifies the most suitable activity to undertake next,
accompanied by an explanation of why that particular activity
was chosen.
All prompts and responses in AITeach are recorded in
the database, providing users with clear explanations of
decisions made by the system. This traceability allows users
to follow the reasoning behind task assignments, supporting
transparency, debugging, and trust in the system’s outputs.
C. ACHIEVING TESTABILITY
In LLM-driven systems, ensuring consistency in application
is a critical challenge because of the non-deterministic nature
of language model outputs. One effective method to address
this issue is through regression testing, which is designed to
ensure that changes in the system, such as model updates or
prompt adjustments, do not lead to unintended variations in
the results.
The first step in regression testing is to establish baseline
outputs. This involves running a set of predefined prompts Pi
through the LLM and recording the corresponding outputs
R
(baseline)
i
. These outputs serve as the reference point for
future comparisons. The function of the LLM in this context
is represented as
R
(baseline)
i = f (Pi)
where f is the LLM’s reasoning process applied to the
prompt Pi
.
After the baseline is established, if any system changes
occur (e.g., updates to the LLM or modifications to
prompts), the same set of prompts Pi
is reissued, and new
responses R
(new)
i
are recorded. This automated re-execution of
prompts allows for the efficient collection of updated outputs
without human intervention, which is crucial for maintaining
consistency.
Then, the consistency of the system’s behavior is evaluated
by comparing the original baseline responses R
(baseline)
i with
the new responses R
(new)
i
. A similarity measure, namely,
cosine similarity for embeddings, is used to quantify the
degree of change between the two sets of text. Cosine
similarity is a widely used measure to assess the degree of
similarity between two vectors, particularly in the context
of text embeddings [24]. It quantifies how aligned or close
two vectors are in a high-dimensional space by calculating
the cosine of the angle between them [25]. A value of
one indicates that the vectors are identical (pointing in the
same direction), while zero signifies that they are orthogonal,
implying no similarity. This comparison can be represented
mathematically as
d(R
(baseline)
i
, R
(new)
i
) ≤ ϵ
where d represents the distance or difference between the
two outputs. Ideally, this difference should remain within an
acceptable threshold ϵ. A value of d exceeding ϵ indicates
a potential inconsistency in the model’s behavior, suggesting
that the updates may have introduced undesirable variations
in the outputs. In practice, maintaining outputs within this
threshold is crucial for the system’s overall stability and
trustworthiness. Significant deviations not only compromise
the model’s consistency but may also lead to unexpected
outcomes in real-world applications, undermining user
confidence.
In our regression testing process, we define a specific
set of test prompts. A pass/fail criterion is then applied to
evaluate the results. If d remains below the threshold ϵ for all
tested prompts, the regression test is considered successful,
confirming that the system maintains its consistency despite
any changes. However, if the difference exceeds the threshold
for one or more prompts, a deviation in the system’s
behavior exists, necessitating further investigation to identify
the source of the inconsistency and implement corrective
measures.
By integrating rigorous regression testing into the development process, developers can ensure that updates to
LLM-driven systems maintain the consistency of planning
and decision-making processes. In systems like AITeach,
where the conditions for each activity and the representation
of the current state are crucial for determining the next
task, regression testing becomes especially important. This
practice not only safeguards the integrity of LLM-based
applications over time but also fosters greater user trust in
the system’s ability to perform predictably across a variety of
tasks and scenarios.
D. ACHIEVING SCALABILITY
Scalability is crucial for personalized learning systems like
AITeach, especially as it accommodates a growing number
of learners, each following personalized learning paths.
To maintain performance and efficiency at scale, AITeach
leverages an event-driven architecture, enabling flexible and
efficient data processing and response management across
its core components: Thinker, Planner, and Worker. Each
component operates independently, handling specific tasks,
and it is developed as a microservice, as depicted in Figure 8.
FIGURE 8. Event-driven architecture.
Utilizing containerization technology for deployment, we can
seamlessly scale these microservices in response to demand.
The components, deployed as microservices, communicate
through an event bus, which comprises various channels to
store events related to data, such as thoughts, tasks, and plans.
When a task is updated, the Thinker receives an update event
and generates a new thought, which is then published to the
event bus. The Planner subsequently receives the thought
and formulates a plan, identifying the next task. Finally, the
Worker receives an event prompting it to execute the newly
created task.
By leveraging an event-driven architecture, AITeach’s
components communicate asynchronously by emitting events
in response to user actions or system triggers. This decoupled
design reduces the need for constant direct communication,
enabling each microservice corresponding to the Thinker,
Planner, and Worker component to operate independently
and process tasks concurrently. To support scalability,
AITeach is deployed on cloud platforms like Google Cloud
Run3
and Amazon ECS,4 which provide automatic scaling
based on real-time demand. This setup ensures that each
microservice can dynamically scale up or down according to
workload, resulting in faster response times, improved system
throughput, and optimized resource utilization without being
constrained by other components.
To dynamically scale based on the system load, a process
known as autoscaling, we must configure several key
parameters, such as the maximum number of concurrent
requests per instance, the minimum and maximum number of
instances, and CPU allocation. The CPU is typically allocated
only during request processing to optimize cost efficiency,
and the minimum number of instances is often set to zero.
The system automatically adjusts the number of instances by
calculating the difference between the current load and the
desired capacity, adding or removing instances as needed to
maintain performance and resource efficiency.
In autoscaling, the scaling factor is a metric used to adjust
the number of instances based on system load. It is calculated
as the ratio of the current load to the desired load per instance:
Scaling Factor =
Lcurrent
Ldesired
where Lcurrent is the current load (the number of requests per
second) and Ldesired is the desired load per instance. This
ensures that resources are added or removed in real-time
according to demand. For instance, if a system handles
400 requests per second and each instance can manage
100 requests, the scaling factor would be four, meaning four
instances are needed. As the load increases or decreases,
the scaling factor guides how many instances should be
provisioned or de-provisioned to maintain performance and
efficiency.
Autoscaling, based on the scaling factor, optimizes
performance while minimizing costs, especially in cloud
environments like Google Cloud Run and Amazon ECS.
These platforms automatically adjust resources based on
real-time demand, allowing systems to scale up during high
load and down during low demand, improving both system
throughput and resource utilization.
V. EVALUATION
We evaluated AITeach5 based on the tactics outlined in the
previous section. Our evaluation focuses on two key research
questions:
1) RQ1. How effective is regression testing in measuring
response consistency in LLM-driven systems?
2) RQ2. How does event-driven architecture improve
software scalability?
RQ1 focuses on evaluating the effectiveness of regression testing in ensuring consistency in LLM responses,
while RQ2 examines the critical aspects of scalability and resource management facilitated by event-driven
microservice architecture.
A. EXPERIMENTAL SETUP
To evaluate RQ1, we created a test suite comprising
100 updated tasks with varying progress values across
different activities. Each task was processed through the
Thinker and Planner components to determine the subsequent
activity. In every test, we set ideal thoughts and expected
next actions as our baselines. Upon completing the test,
we compared the thoughts generated by the Thinker and
the next action decided by the Planner against the baseline.
This comparison employed the regression testing technique
outlined in Section IV-C to assess consistency in the
responses produced by LLM.
We selected the LLM models Gemini-1.5-Pro-002,
Gemini-1.0-Pro-002, GPT-3.5 Turbo, and GPT-4 Turbo
for this evaluation. To evaluate the generated thoughts,
we analyzed the distance d, which quantifies the difference
between the two outputs. This process utilized OpenAI’s
5The complete source code can be found at https://github.com/cnachamfu/aiteach
embedding model, text-embedding-3-small, to convert sentences into vector representations. Following this,
we applied the cosine_similarity method from
sklearn6
to compute d. A d value closer to one indicates
greater consistency in the model’s responses.
To evaluate the model’s accuracy in predicting the next
action compared to the expected action, we use a simple
formula for the ratio of correct predictions to the total
predictions, expressed as a percentage:
Accuracy =
Ncorrect
Ntotal
× 100
where Ncorrect represents the number of tests in which the
model’s predicted next action aligns with the expected action
and Ntotal denotes the total number of tests conducted.
By concentrating on the thought provided by the Thinker and
the next activity determined by the Planner, we measured
the system’s consistency in determining the next actions in
response to an updated task. This experiment allowed us to
compare the consistency of various LLMs and identify the
most suitable one for our requirements.
For RQ2, we assessed the scalability of AITeach by
deploying its core components, namely, the Thinker, Planner,
and Worker, as independent microservices on Google Cloud
Run. This deployment utilized a container configuration
with 512 MB of RAM and one CPU.
We conducted load tests at rates of 20, 40, 60, 80, and
100 requests per second by updating a set of tasks to
initiate a workflow that traverses all key components of
the system. The desired load per instance was configured
to 80 requests, enabling us to effectively investigate the
autoscaling capabilities of the architecture. Throughout
the testing procedures, we systematically monitored both
response times and the number of instances utilized. The
response time was defined as the duration from the update of
the task to the successful creation of the new task. By comparing the results from each load test, we could analyze
how effectively the event-driven microservice architecture
managed increasing workloads while maintaining optimal
performance and resource efficiency.
B. RESULTS AND DISCUSSION
The evaluation of the LLM models across 100 test cases, segmented by activity type, reveals significant insights regarding
their performance consistency, as shown in Table 1. In pretest
and lecture activities, Gemini-1.0-Pro-002 emerged as the
most reliable model, achieving the greatest average d value.
This indicates its superior capability to produce expected
outputs consistently across different progress levels. Gemini1.5-Pro-002 also demonstrated commendable performance in
exercise and quiz activity, reflecting its ability to maintain
a relatively stable response. Both models outperformed the
others in this category, with GPT-4 Turbo and GPT-3.5 Turbo
showing lower d values and variability, particularly in their
responses for the pretest activity.
TABLE 1. Summary of d values in generating thought by activity type.
TABLE 2. Overall d values in generating thought.
TABLE 3. Accuracy in determining next action.
Table 2 shows that Gemini-1.5-Pro-002 again stands
out with the highest average d value across all activity
types, indicating its robustness and reliability in various
learning scenarios, closely followed by Gemini-1.0-Pro002, demonstrating consistent performance but with slightly
greater variability. GPT-4 Turbo maintained moderate reliability, while GPT-3.5 Turbo had the lowest average d
value, indicating its difficulty in maintaining consistency.
These findings suggest that while Gemini-1.5-Pro-002 is the
most suitable model overall, Gemini-1.0-Pro-002 and GPT-4
Turbo are also viable options, particularly when considering
other factors like reasoning and contextual understanding.
The accuracy results for determining the next action across
the evaluated LLM models reveal performance differences,
as shown in Table 3. Gemini-1.5-Pro-002 demonstrates the
highest reliability in producing expected outputs, establishing
itself as the most robust choice for consistent decisionmaking. GPT-4 Turbo follows closely, presenting itself as a
strong alternative, particularly due to its enhanced contextual reasoning capabilities. Gemini-1.0-Pro-002 also shows
solid consistency, although with slightly more variability
in responses. In contrast, GPT-3.5 Turbo exhibits greater
challenges in maintaining consistency, suggesting it may be
less suitable for tasks requiring precise action determination.
Overall, these findings emphasize the importance of selecting
the right model based on specific accuracy requirements for
different tasks.
To address RQ1, the evaluation of regression testing’s
effectiveness in maintaining response consistency within
LLM-driven systems revealed its critical role in identifying
discrepancies between expected and actual outputs across
various models. The findings indicate that Gemini-1.5-Pro002 consistently outperformed its counterparts, underscoring
the effectiveness of regression testing in assessing and
ensuring the reliability of model responses. This systematic approach reinforces the necessity of robust testing
FIGURE 9. Results of load test.
methodologies for sustaining response consistency in an
LLM-driven system.
Figure 9 depicts the response times observed during each
load test, reflecting the variations in the number of concurrent
requests. The load test results reveal valuable insights into the
system’s performance under varying request rates. Initially,
the response time increased as the load grew, indicating that
the system was managing the increased demand effectively.
However, as the load reached a certain threshold, the response
time rose more significantly, suggesting that the system was
experiencing strain.
Interestingly, there was a moment when the response
time decreased even as the load increased (notably at
80 concurrent requests), suggesting that effective autoscaling
mechanisms were at play. However, as the load continued
to rise, response times increased again, indicating potential
performance limits. Overall, these results underscore the
system’s robustness and highlight the significance of effective
resource management and autoscaling strategies in maintaining performance consistency during high-demand scenarios.
The evaluation of the load tests demonstrates that dividing
the system using the chain-of-reasoning-and-action pattern,
along with an event-driven microservice architecture, significantly enhances software scalability by enabling effective
autoscaling mechanisms. The results illustrate how this
architecture facilitates dynamic resource management, which
is essential for maintaining performance consistency in
high-demand scenarios and optimizing scalability. Consequently, these findings effectively address RQ2, emphasizing
the vital role of event-driven microservice architecture in
improving scalability in LLM-driven systems.
C. THREATS TO VALIDITY
Our experiments faced several internal threats that may
affect the reliability of the results. One significant limitation
was the restricted range of load scenarios, testing only
five rates of concurrent requests. This narrow spectrum
may not adequately capture the system’s performance under
extreme conditions. Additionally, the variability of task
progress updates was limited, which may not accurately
reflect real-world applications. The language used to generate
thoughts, serving as inputs for planning the next actions,
could also introduce inconsistencies, affecting the models’
outputs. The choice of language employed to generate
thoughts, which serve as inputs for planning subsequent
actions, can introduce inconsistencies that significantly affect
the outputs produced by various models. For instance, the
Gemini models exhibit a higher level of efficiency when
processing Thai compared to their performance with OpenAI
models. Therefore, accounting for these language-specific
characteristics is crucial when assessing the capabilities of
LLMs in different applications.
An external threat to the generalizability of the results
arises from the limitations of the tested LLM models, which
may stem from their differing architectures and training data.
This can lead to performance variability that may not be
representative of other models in the landscape. To enhance
the applicability of future findings, a broader range of LLM
models, including open LLMs, should be evaluated to gain a
more comprehensive understanding of their performance in
LLM-driven systems.
Our approaches address challenges in integrating and
explaining LLM-driven systems for personalized education
but acknowledges limitations in assessing these attributes
quantitatively. We used qualitative assessments to evaluate
integration and explainability, providing insights into their
effectiveness and guiding improvements. These assessments,
while insightful, may not offer the same precision as
quantitative methods. To address this, we could use metrics
such as latency of module interaction, error propagation
rate, integration coverage, and scalability for integration
evaluation. For explainability, we suggest traceability scores,
explanation consistency, feedback time, and user perception
metrics. These proposed metrics offer an objective framework
to measure system efficiency and reliability. However, these
aspects remain underexplored in our evaluation and represent
potential directions for future research, where developing
tools and methodologies for their implementation could
enable systematic benchmarking and foster confidence in
LLM-driven educational systems.
VI. RELATED WORKS
The lack of standardized benchmarks complicates any
comparison of our proposed design tactics for achieving
non-functional attributes with those used in other systems, limiting direct performance comparisons. Additionally,
factors such as infrastructure play a significant role in influencing system performance. Still, functional comparisons
with other personalized education systems remain vital for
evaluating the scope and effectiveness of the systems we
develop using these proposed tactics.
In this section, we evaluate existing LLM-driven personalized learning systems by comparing key functionalities
that contribute to their capacity for delivering customized
learning experiences. These functionalities include 1) content
generation (CG), where systems produce tailored content
based on individual learner profiles or inquiries; 2) adaptive
TABLE 4. Evaluation of the LLM-based recommender system.
learning pathways (AL), which determine the learning
activity in response to a learner’s progress; 3) personalized recommendation engines (PR), which direct students
toward relevant learning resources; 4) real-time feedback
mechanisms (RF) that offer immediate insights into learner
performance; and 5) integration with external educational
resources (IE), which broadens the system’s access to diverse
and up-to-date content. Table 4 compares seven works from
the literature based on their functionalities.
Recent advancements in personalized learning have introduced several systems with varying strengths and areas for
improvement. Dehbozorgi et al. [26] developed a system
that excels in content generation and personalized recommendations, showing potential for enhancing pedagogical
practices for novice educators. However, it lacks adaptive
learning pathways, real-time feedback mechanisms, and
learner engagement tracking, highlighting the need for further
refinement. In contrast, the Ladder framework [27] leverages
advanced LLM tagging to produce tailored learning materials
and establish adaptive learning pathways by analyzing synthetic student profiles, significantly enhancing the learning
experience.
On the other hand, GPTutor [28] demonstrates strong
content generation capabilities but lacks features like
adaptive learning pathways and real-time feedback. This
web application uses Generative AI to align educational
content with student interests and career goals, enhancing
engagement. Similarly, the Learning Butler chatbot [5] excels
in personalized recommendations and real-time feedback
but does not offer content generation or adaptive learning
pathways. Utilizing the GPT language model, the chatbot
assists students in managing tasks while fostering grit and a
growth mindset, leading to improved learning outcomes.
Additionally, the LLM Virtual Assistant for collaborative
learning [8] and Becerra et al.’s Generative AI-based tool [10]
demonstrate significant capabilities in adaptive learning
pathways and personalized recommendations. The former
enhances group cohesion through problem feedback and
resource gathering, while the latter analyses student’s data
to provide personalized feedback and insights for instructors.
Lastly, MCQGen [12] automates the creation of multiplechoice questions, showcasing robust content generation and
personalized recommendations, though it lacks adaptive
pathways and real-time feedback. Collectively, these systems
contribute to the evolving landscape of personalized learning,
each addressing unique aspects of learner needs.
Our system integrates the strengths of existing educational systems while addressing their limitations to support
a comprehensive suite of functionalities. By leveraging
LLM for content generation, adaptive learning pathways,
and personalized recommendations, we create an engaging
environment that enhances academic performance. Realtime feedback mechanisms facilitate timely interventions,
keeping learners motivated and on track. Additionally,
our approach prioritizes seamless integration, explainability,
testability, and scalability by incorporating design elements
that foster user trust, facilitating rigorous testing for ongoing improvement, and enabling seamless integration with
external resources to enhance the learning experience.
VII. CONCLUSION
Developing LLM-driven personalized learning systems
presents distinct challenges, particularly in supporting critical
system attributes like integration, explainability, testability,
and scalability. Unlike conventional software systems, LLMbased systems face complexities arising from the dynamic
nature of learning models, the opaque nature of their decisionmaking processes, and the handling of natural language data.
These unique characteristics introduce additional layers of
complexity that must be addressed to ensure reliable and
effective educational systems.
In this work, we propose a set of tactics to address challenges at both the design and implementation levels. These
tactics include seamless integration of LLM components,
enhanced model transparency to improve explainability,
increased testability to support evolving prompts and models,
and scalable performance under varying workloads. Our evaluation, applied to the development of a personalized learning
system, demonstrates the effectiveness of these approaches in
improving response consistency and guiding the selection of
appropriate models tailored to specific system requirements.
Moreover, the adoption of an event-driven microservice
architecture, where the system is broken down into components that communicate through events, proved instrumental
in supporting the system’s ability to dynamically adjust
resources through autoscaling. This enabled robust handling
of fluctuating demands, ensuring scalability and maintaining
performance even under high-load scenarios.
Future research will explore applying the proposed tactics
to other LLM-driven domains, such as healthcare, where
personalization and large-scale data processing are crucial.
Healthcare systems require tailored solutions for diagnostics
and treatment, demanding high transparency, testability,
and scalability. Adapting event-driven architectures and
robust testing frameworks will be essential to manage vast
amounts of data while ensuring reliable, safe, and scalable
performance in delivering personalized medical care.
