Title: A Survey on Digital Twins: Enabling Technologies, Use Cases, Application, Open Issues, and More

Abstract—Digital Twins, sophisticated digital replicas of
physical entities, have been gaining significant attention,
especially after NASA’s endorsement, and are poised to
revolutionize numerous fields, such as medicine and construction. These advanced models offer dynamic, real-time
simulations, leveraging enabling technologies, such as artificial intelligence, machine learning, IoT, cloud computing,
and Big Data analytics to enhance their functionality and
applicability. In the medical field, Digital Twins facilitate
personalized treatment plans and predictive maintenance
of medical equipment by simulating human organs with
precision. In construction, they enable efficient building
design and urban planning, optimizing resource use, and
reducing costs through predictive maintenance. Startups
are innovatively employing Digital Twins in various sectors,
from smart cities—where they optimize traffic flow, energy
consumption, and waste management—to industrial machinery, ensuring predictive maintenance and minimizing
downtime. This survey delves into the diverse use cases,
market potential, and challenges of Digital Twins, such as
data security and interoperability, while emphasizing their
transformative impact on industries. The future prospects
are promising, with continuous advancements in AI, ML,
IoT, and cloud computing driving further expansion and
application of Digital Twin technologies.
Index Terms—6G, artificial intelligence (AI), digital twins
(DTs).
NOMENCLATURE
DT: Digital Twins.
AI: Artificial intelligence.
AR: Augmented reality.
VR: Virtual reality.
IoT: Internet of Things.
UAV: Unmanned aerial vehicle.
I. INTRODUCTION
I
N RECENT years, global progress has brought about remarkable advancements alongside unsettling challenges.
The construction of magnificent architectural marvels and the
emergence of novel diseases have pushed the boundaries of
human experience [1]. However, assessing the durability of
these constructions and developing preventive drugs or vaccines
through human testing remains exceedingly arduous and timeconsuming.
The COVID-19 pandemic highlighted significant obstacles in
the rapid development and deployment of preventive vaccines.
Pharmaceutical companies encountered formidable challenges
during the rigorous three-stage testing process, which spanned
nearly a year and tragically resulted in substantial loss of life
due to the rampant spread of the disease [2]. Similarly, in the
field of construction, numerous accidents have occurred due
to structures’ inability to withstand weight or natural disasters,
often as a result of inadequate testing procedures. A poignant
example is the October 2022 collapse of a pedestrian bridge
in Gujarat, India, under excessive weight, which led to approximately 150 fatalities. The implementation of appropriate
measures and the use of real-time data could have potentially
averted this devastating incident [3].
Traditionally, vaccines and medications undergo a lengthy
development process, approximately 4–5 years, before approval
for clinical trials and mass production. Initially, potential vaccines are tested on small animals, such as rodents. Upon successful outcomes, human trials commence, which are timeconsuming and costly, ultimately leading to significant loss
of life and public health damage during the trial period [4].
Therefore, there is an urgent need for more efficient and effective methods to test the efficacy of drugs and vaccines against
diseases within a shorter time frame [5].
In recent times, the incorporation of IoT-based sensors in
constructions, such as roads and bridges, has generated vast
amounts of data. However, this Big Data is often too complex to
handle and must be converted into a more manageable form [6].
The primary challenge faced by road construction companies
is the inadequate gathering of essential project information,
leading to subsequent drawbacks and complications [7]. For
example, insufficient early determination of a bridge’s maximum load-bearing capacity can result in structural failure under
excessive weight, necessitating costly repairs and causing public
inconvenience. Similarly, the efficacy of medicines and vaccines
is often short-lived, requiring regular doses or additional booster
shots, which may entail undesirable side effects. These challenges underscore the importance of robust data collection for
informed decision-making [8].
DTs play a crucial role in enhancing safety measures through
dynamic risk management. They offer numerous benefits, including training simulations, real-time monitoring, remote observations, and the optimization of safety protocols. By utilizing
DTs, organizations can reduce accidents, enhance safe operating
procedures, and foster a stronger safety culture [9].
The phrase “TIME IS MONEY” holds unparalleled relevance today, underscoring the need to conserve time, money,
and resources. Employing AI in drug/vaccine manufacturing
and bridge/road construction can achieve this objective. This
approach is facilitated by harnessing the power of DTs—AIgenerated models of structures or human bodies [10]. These
models can preemptively test drugs/vaccines and aid in construction, marking a revolutionary step that propels AI to its
zenith and streamlines development and utilization.
The integration of DT technology with emerging 6G communication networks promises to catalyze unprecedented advancements across multiple domains. The ultra-low latency,
enhanced reliability, and massive connectivity offered by 6G
will facilitate real-time operation of DT models with remarkable
accuracy [11]. In the context of medical applications, 6G will
enable instantaneous data exchange between DT simulations and
healthcare professionals, thereby improving decision-making
processes and expediting the development of advanced treatments. Similarly, in civil engineering, the enhanced speed and
bandwidth of 6G will allow for continuous real-time monitoring and predictive analysis of infrastructure systems, enabling
proactive maintenance and mitigating the risk of catastrophic
failures [12].
Moreover, the ability of 6G to support massive IoT deployments will significantly enhance the scalability of DT systems.
This will allow seamless interaction between physical assets and
their digital counterparts across expansive networks, making it
feasible to manage and monitor multiple infrastructures concurrently. The convergence of 6G and DTs has the potential to revolutionize industries by ensuring faster, more efficient, and highly
reliable operations, ultimately contributing to the optimization
of safety, cost-effectiveness, and time efficiency. Consequently,
the fusion of 6G communications with DT technology is poised
to unlock novel dimensions of innovation, efficiency, and operational excellence across a wide array of sectors [13].
The intention of this survey article is to provide valuable
insights to researchers, scholars, and enthusiasts regarding DT
models and their applications across various physical domains.
Improving existing models in the medical and civil engineering
fields is imperative to enhance their reliability, security, and
cost-effectiveness. The major contributions of this survey are
as follows.
1) Literal and technical definition of DT.
2) Enabling technologies for DT, e.g., IoT, AR/VR, cloud
computing, etc. [14].
3) Case study of models where DT is being used.
4) Applications of DT and methods to improve existing
models.
5) Open challenges in implementing DT models and issues
that may arise.
II. RELATED WORK
Related Works The term DTs emerged in the early 21st century, with its inception at NASA through John Vickers in 2010.
NASA’s creation of a DT of a space shuttle for comprehensive
testing marked a significant milestone in the development of
this technology. Since then, numerous studies and surveys have
delved into various aspects of DTs, primarily concentrating on
their potential to address specific concerns and transform industries[20]. However, there is a scarcity of resources exploring the
broader spectrum of DT applications across diverse domains,
showcasing their time and cost-saving potential.
Foundational Studies and Applications According to Mihai
et al. [1], DTs possess the transformative potential to reshape
industries in unprecedented ways, transcending contemporary
computer-based processes. This concept represents a futuristic
paradigm extending beyond current practices, embodying an immaculate digital replication of a physical entity where digital and
real-world systems coexist. Utilizing platforms and bidirectional
data interaction, DTs emulate the genuine physical attributes and
behaviors of their originals. This intricate framework combines
diverse computing fields, such as AI, IoT, 3-D Models, AR/VR,
and high-speed mobile communications, such as 5G/6G, along
with electronic sensors. This amalgamation enables continuous
assessment, thorough analysis, future predictions, and evaluation of the physical counterpart’s conditions. DTs offer an unparalleled avenue to scrutinize complex systems with an intricacy
unattainable through prevailing methods.
Industry 4.0 and Risk Mitigation DTs play a pivotal role in
ushering in Industry 4.0, a topic thoroughly explored by Cristina
Alcaraz et al. [15]. This study delves into the simulation capabilities of DTs and their capacity to mitigate risks. This article
underscores that DT technology is a convergence of AI and Big
Data. Moreover, it addresses the potential threats associated with
DT adoption and assesses their current state. Notably, limited research exists on the adverse impacts of DTs, making this article a
valuable contribution to that realm. It furnishes insights into this
aspect while providing security recommendations and strategies
for ensuring the secure and appropriate utilization of DTs.
Smart cities and UAVs: In recent times, significant research
and progress have been observed in the realm of DTs, captivating
the interest of scholars due to their multifarious applications. As
noted by Jafari et al. [16], DTs hold the potential to enhance
diverse facets of smart cities. These applications encompass
real-time traffic management in transportation systems, urban
planning, remote data transmission within power grids, and a
Fig. 1. Sections of the survey.
range of other analyses. Through the scrutiny and exploration of
digital replicas of these sectors, solutions to the aforementioned
challenges can be achieved.
Lu et al. [17] explored how 6G technology will enhance
DTs in Industry 4.0 by enabling real-time data exchange and
better connectivity between machines, humans, and systems.
It highlights the potential of 6G-powered DTs to improve industrial processes, optimize predictive maintenance, and drive
intelligent automation through seamless communication. This
article also acknowledges challenges, such as data security and
system interoperability, while identifying key technologies, such
as AI and IoT, as crucial enablers for realizing the full potential
of 6G-empowered DTs in industrial settings.
Safety, security, and IoT applications: Utilizing DTs for safety
and security purposes, accident prevention gains prominence.
Carotenuto et al. [18] advocated the notion of digitally twinning
a system’s black box using I/O pairs. This approach yields a
precise real-time approximation of the system’s condition and
status. The proposed model of this DT black box finds relevance
in diverse IoT and Industry 4.0 contexts, facilitating tasks, such
as maintenance, error detection, and cloud control. Essentially,
it forms a composite numerical model marked by reduced
computational complexity and memory usage. This model is
well-suited for microcontroller-based IoT applications [21].
The use of DTs in control systems is of growing interest
due to their real-time monitoring and control capabilities. Prior
research primarily explored DTs for closed-loop systems to
improve stability against disturbances, allowing for real-time
parameter adjustments. Traditional DTs, however, rely on cloud
platforms for data transfer, introducing latency and privacy
issues. Recently, FPGA-based DTs have been proposed,
enabling direct, parallel communication with physical assets
and removing the need for cloud-based data transfers. This
approach has shown effectiveness in applications, such as
monitoring power systems under sensor faults, marking a shift
toward faster, more secure DT models suited for high-speed
control environments [19].
The selection of these works is intended to showcase the broad
applications and transformative potential of DTs across various
domains. While there are hundreds of related works, the chosen
studies highlight key aspects, such as the foundational development at NASA, integration with Industry 4.0, applications in
smart cities and UAVs, and the use of DTs for safety and security
in IoT. These examples illustrate the diverse capabilities of DTs
and their relevance in both theoretical and practical contexts,
providing a comprehensive overview of the current state and
future potential of DT technology. Fig. 1 shows the organization
of the entire paper. Also, Table I lists all the contributions of the
related works along with their strenghts and weaknesses.
III. ABOUT DTS
The advent of Industry 4.0 brought forth the transformative
concept of DTs, symbolizing a revolutionary bridge between
physical and digital domains. These dynamic, immersive counterparts encapsulate real-world entities within virtual ecosystems, facilitating a seamless exchange of data and insights [22].
DTs are not confined to a single sector; their impact spans
diverse industries. In manufacturing, they optimize production,
predict maintenance needs, and refine designs. In healthcare,
they enhance patient care through personalized treatment plans
and predictive analytics. Aerospace and energy sectors leverage
TABLE I
NOTABLE RELATED WORKS ON DTS THAT HAVE LEFT A SIGNIFICANT IMPACT, THEIR CONTRIBUTIONS, ADVANTAGES, DISADVANTAGES, AND APPLICATIONS
DTs for performance optimization, predictive maintenance, and
safety enhancements [23].
At the core of DTs lies a continuous flow of real-time sensor
data and IoT connectivity. This synergy, coupled with advanced
analytics and simulation techniques, allows not only the representation of current states but also predicts future behaviors.
This predictive prowess empowers industries by providing holistic insights into operations, optimizing maintenance schedules,
anticipating failures, and refining design processes [24].
DTs are more than mere replicas; they serve as innovation
crucibles. They act as platforms for testing new ideas, simulating
scenarios, and training personnel in risk-free virtual environments. The iterative feedback loop between the physical and
digital spheres refines the twin’s accuracy over time, evolving
alongside its physical counterpart [25].
The synergy between DTs and emerging technologies, such
as AI, AR, and VR, augments their capabilities exponentially.
AI enhances predictive analytics, while AR and VR enable
immersive experiences for remote monitoring, training, and
simulations. This convergence promises a future where physical
and virtual realms harmonize seamlessly [26].
DTs in 6G communication represent a virtual replication of
the entire network infrastructure, enabling real-time monitoring, simulation, and optimization of the physical network. By
mirroring network performance, they help operators manage
resources efficiently, predict faults before they occur, and test
new technologies in a risk-free virtual environment. DTs also
enhance cybersecurity by simulating potential attacks and identifying vulnerabilities. Their ability to model network behavior
in real time is key to improving performance, reliability, and
the seamless integration of advanced services, such as IoT, edge
computing, and network slicing in 6G networks.
While DTs offer immense potential, challenges, such as
data privacy, interoperability, and scalability persist. Addressing
these hurdles will be pivotal in unlocking their full capabilities.
Looking ahead, advancements in edge computing, blockchain,
and cybersecurity will further fortify the DT ecosystem, fostering greater reliability and security [27].
DTs stand at the forefront of technological innovation, revolutionizing industries by bridging the gap between physical
and digital realities. Their ability to simulate, predict, and optimize processes not only enhances efficiency but also drives
unprecedented innovation. As technology continues to evolve,
the symbiotic relationship between DTs and emerging technologies promises a future where seamless convergence leads to
unparalleled progress and insights [28].
The evolution of DTs is a dynamic process. Future advancements could include enhanced AI algorithms for more accurate
predictions, decentralized architectures leveraging blockchain
for data security and transparency, and the integration of quantum computing for complex simulations. In addition, the refinement of edge computing capabilities will enable real-time
processing of vast data streams, reducing latency and improving
responsiveness [29].
Now, as DTs become more ubiquitous, ethical considerations
regarding data privacy, ownership, and transparency come to
the forefront. Striking a balance between innovation and ethical
responsibility is crucial. Robust frameworks and regulations
need to be established to safeguard sensitive data and ensure
responsible use, fostering trust among stakeholders and the
public. The widespread adoption of DTs will have profound
socioeconomic implications. It has the potential to bridge the
technological divide, providing opportunities for developing
nations to leapfrog traditional infrastructural limitations. Moreover, in urban planning and smart city initiatives, DTs can
optimize resource allocation, improve infrastructure resilience,
and enhance the quality of life for citizens [29].
DTs can play a pivotal role in achieving sustainability goals.
By modeling and analyzing energy consumption, optimizing
supply chains, and simulating environmental impacts, they facilitate informed decision-making towards more sustainable practices. This includes reducing waste, lowering carbon footprints,
and promoting circular economy principles [30].
To fully unlock the potential of DTs, collaboration and standardization across industries are imperative. Establishing interoperability standards will enable seamless integration and data
exchange between different systems and platforms. This collaboration fosters innovation, accelerates development, and ensures
compatibility between various DT implementations [31].
In conclusion, DTs stand as a cornerstone of Industry 4.0,
revolutionizing how we perceive and interact with the physical
world. Their evolution hinges on technological advancements,
ethical considerations, and global collaborations. By addressing
challenges and responsibly harnessing their capabilities, DTs
have the potential to redefine industries, promote sustainability,
and drive societal progress on a global scale [30].
Expanding on these facets provides a comprehensive understanding of the multifaceted impact and considerations surrounding DTs. Their potential for reshaping industries, addressing global challenges, and fostering innovation remains a
fascinating prospect worth exploring further.
IV. ENABLING TECHNOLOGIES FOR DTS
DTs may seem like a simple 3-D model of an entity, but in
reality, it is a much more detailed and complex process, which
requires the usage of various technologies in different stages of
manufacture [32]. These technologies are termed as enabling
technologies for DTs. Enabling technologies play a pivotal role
in the creation and utilization of DTs within the manufacturing
sector. These technologies encompass a wide spectrum, ranging
from the IoT and data analytics to AI, cloud computing, and
augmented reality (AR). The integration and synergy of these
technologies form the foundation upon which DTs are built and
thrive [22]. Their detailed contribution in the formation of DTs
is as follows. Table II lists all the enabling technolgies that are
used with digital twins to make it practically usable in various
domains.
A. Internet of Things
1) Data acquisition: IoT devices, such as sensors and actuators, are deployed throughout the manufacturing environment to collect real-time data from physical assets,
machines, and processes. These sensors measure various
parameters, such as temperature, vibration, etc [29].
TABLE II
ENABLING TECHNOLOGIES FOR DTS: THE VARIOUS TECHNOLOGY THAT ARE INVOLVED IN THE MANUFACTURE OR MAKING OF DTS
2) Data transmission: IoT devices transmit the collected
data to cloud-based platforms or edge computing systems
using wireless communication protocols, such as Wi-Fi,
Bluetooth, or cellular networks, that makes data readily
available [33].
3) Data integration: The data collected from different IoT
devices are integrated into a central repository. This
centralized data hub ensures availability of all relevant
information [34].
4) Real-time monitoring: With IoT, manufacturers can continuously monitor the performance of their physical assets. This real-time monitoring helps identify anomalies,
predict maintenance needs, and optimize operational efficiency [35].
5) Predictive maintenance: DTs created with IoT data can
predict when equipment or machinery is likely to fail,
allowing manufacturers to schedule maintenance activities proactively. This reduces downtime and extends the
lifespan of assets [36].
6) Process optimization: Manufacturers can use DTs to
simulate different scenarios and optimize manufacturing
processes. This can lead to improvements in product
quality, energy efficiency, and resource utilization [18].
7) Remote control and monitoring: IoT-enabled DTs can
also enable remote control and monitoring of manufacturing processes and equipment, which is valuable in
scenarios where physical access to the site is limited or
when dealing with hazardous environments [34].
8) Supply chain visibility: IoT can be used to track the
movement and condition of raw materials, components,
and finished products throughout the supply chain
[37].
In summary, IoT is instrumental in the manufacturing of DTs
by providing the data needed to create accurate virtual representations of physical assets and processes. This technology
enhances real-time monitoring, predictive maintenance, process
optimization, and supply chain visibility in the manufacturing
industry [38].
B. Data Analytics and Big Data
Data analytics and Big Data are integral in crafting DTs for
manufacturing. They form the data foundation, collecting and
processing information from various sources. These technologies preprocess and cleanse data, aiding in the development
of accurate DT models. In real-time, DTs are maintained and
monitored through continuous data influx, thanks to Big Data’s
capabilities [39].
Predictive maintenance is made possible through data analysis, reducing downtime. Furthermore, DTs facilitate process
optimization by simulating scenarios, with data analytics finetuning these simulations. Quality control benefits from real-time
analysis of DT data, ensuring product quality [40].
Supply chains are optimized by analyzing data from DTs
throughout the supply chain elements. Customization and personalization are achieved through customer data analysis. The
DT evolves through the product lifecycle with continuous data
analysis, enhancing its accuracy and value [23]. In manufacturing, data analytics and Big Data are essential tools for creating,
managing, and improving DTs, resulting in enhanced efficiency
and decision-making [41].
C. Artificial Intelligence
1) Data processing: AI algorithms efficiently handle vast
datasets from various sources, ensuring that the DT
is built upon accurate and comprehensive information [42].
2) Modeling: AI techniques, such as machine learning, create highly sophisticated models for DTs, which capture
intricate relationships within the physical system for
accurate and dynamic simulations [26].
3) Real-time monitoring: AI-powered analytics enable
continuous real-time monitoring of the physical system
represented by the DT [43].
4) Predictive analytics: AI analyzes historical data and
real-time inputs to forecast future system behavior [44].
5) Optimization: Using AI-driven optimization algorithms,
DTs can explore various scenarios and find the most
efficient and cost-effective solutions for manufacturing
processes [45].
6) Natural language processing (NLP): AI-driven NLP
technology allows engineers and operators to interact
with the DT using natural language, making it more
accessible and user-friendly [46].
7) Autonomous decision-making:In some instances, AI can
be integrated into the control systems of manufacturing
processes, enabling DTs to make autonomous decisions
based on real-time data [47].
8) Quality control: AI algorithms continuously analyze
data from sensors and cameras within the DT, enabling
real-time detection of quality issues [48].
9) Supply chain management: AI-driven DTs optimize supply chains by forecasting demand, managing inventory,
and optimizing logistics based on real-time data analysis [49].
10) Lifecycle improvement: AI continually enhances DTs by
adapting models and recommendations based on newly
acquired data [50].
D. Cloud Computing
1) Scalability: Cloud platforms provide the necessary scalability to handle the massive amounts of data required for
DTs [51].
2) Data storage: Cloud storage solutions offer secure and
cost-effective options for storing the extensive datasets
generated by sensors and IoT devices [52].
3) Data processing: Cloud computing provides the computational power required for processing and analyzing
data. Complex simulations, data analytics, and AI-driven
algorithms that are essential for DTs can be executed
efficiently in the cloud [50].
4) Collaboration: Cloud-based platforms facilitate collaboration among geographically dispersed teams. Engineers,
designers, and operators can work together on the development and operation of DTs, sharing data and insights
in real time [34].
5) Remote access: Cloud-based DTs can be accessed
from anywhere with an internet connection, allowing
stakeholders to monitor and interact with the twin remotely [53].
6) Security and cost efficiency: Leading cloud providers
offer robust security measures and compliance standards
to protect sensitive manufacturing data and it is much
more cheaper than other means [54].
7) Updates, maintenance, backup, and disaster recovery:
Cloud platforms offer automated backup and disaster
recovery solutions, reducing the risk of data loss and
downtime in the case of unexpected events. They also
provide regular updates and offer maintenance for the
stored data [55].
E. AR and VR
Conventional plant information systems rely on 2-D engineering blueprints with data points. Modern advancements introduce
precise 3-D digital models synchronized with real-world data
in real time. This integration forms a “DT” residing in a virtual
realm. Here, applications offer operational reports, maintenance
assistance, training, and the freedom to explore enhancement
possibilities through experimentation [56].
Contemporary applications employ 3-D models and engineering simulations extensively, yet a fundamental schism persists
between these systems and the practical world when transitioning from design to physical manifestation [57]. The remedy lies
in the conception of a cohesive virtual realm, where designs are
conceived, experienced, and seamlessly advanced through their
life cycle into production, thereby birthing a dynamic DT [58].
This can be achieved by using AR and by the use of VR, the DT
model can be implemented. This DT encapsulates the entirety
of data and knowledge amassed during its evolution [59].
1) The convergence of virtuality and reality, a core objective
of the DT concept, aligns seamlessly with two advancing
technologies: VR and AR [60].
2) VR is dedicated to enhancing human–machine interactions (HMI) through 3-D computer-generated simulations. Users, equipped with wearable electronic devices,
can intuitively immerse themselves in these digital environments [61].
3) In contrast, AR harnesses wearable devices to overlay
3-D digital imagery onto the physical world. Its purpose
is to seamlessly blend virtual information with the real
environment, augmenting users’ understanding [62].
4) VR offers immersive interaction with virtual twins of
industrial equipment, enabling engineers to test circular
economy strategies, create safe training scenarios, and
facilitate hands-on learning experiences [63].
5) AR simplifies DT access by superimposing virtual data
onto real entities through camera feeds. This allows dynamic monitoring without disconnecting from the physical environment [64].
6) VR and AR address challenges in HMI development,
including realistic asset representations, data availability,
and intuitive interfaces [65].
7) Neither VR nor AR fully merges real and virtual worlds,
necessitating mixed reality (MR) technologies. MR combines VR and AR advantages to integrate digital models
into the physical world and simulate processes realistically [66].
8) Researchers have leveraged these technologies to enable
immersive HMI, training, and monitoring within the DT
paradigm [67].
In summary, VR, AR, and MR technologies have revolutionized the DT concept, bridging the gap between the real and
virtual realms, enhancing human interactions, and expanding
their applications across various domains [68].
F. Simulation and Modeling Tools
1) Accurate representation: They build precise digital
replicas of physical systems or objects, forming the basis
of DTs [69].
2) Dynamic behavior: These tools simulate real-world behaviors, enabling in-depth analysis and predictions[70].
3) Validation: DTs are rigorously tested and validated,
reducing risks and ensuring accuracy [71].
4) Iterative refinement: Engineers can continually improve
DTs as new data becomes available or changes occur [72].
5) Optimization: Simulations help identify efficient strategies, optimizing manufacturing processes [23].
6) Predictive maintenance: Maintenance needs are predicted, minimizing downtime and unexpected failures [73].
7) Environmental assessment: Manufacturers evaluate the
environmental impact of processes, including energy
usage and emissions [74].
8) Complex systems: Modeling aids in understanding and
optimizing complex systems, such as smart factories [75].
9) Realistic visualization: Visualization tools provide realistic representations for better understanding [76].
10) Training: Simulations serve as training environments for
personnel [77].
11) Risk assessment: Risks are assessed, helping to make
informed decisions and ensure safety [78].
12) Continuous improvement: DTs evolve through ongoing
analysis, refinement, and adaptation to changing conditions [79].
13) Data integration: Real-time data from sensors and IoT
devices are integrated for accurate representation [80].
All these above elements play a crucial role in the manufacture
of DTs. They help to visualize and generate the model of DTs
as per requirement.
V. CASE STUDIES ON DTS
In today’s tech-driven world, “DTs” have emerged as a
transformative concept, representing virtual replicas of physical
objects, systems, or processes equipped with real-time data and
analytics. They revolutionize design, operation, and management, delivering unmatched insights and efficiency.
DTs find applications in diverse sectors, spanning manufacturing, healthcare, aerospace, and more. This series of case
studies explores real-world DT implementations, showcasing
their impact on businesses and society. They reveal how DTs
boost productivity, cut costs, enhance safety, and fuel innovation.
Each case study spotlights unique scenarios where DTs play
a pivotal role, outlining challenges, solutions, and outcomes.
These examples underline the transformative potential of DTs,
reshaping industries and reimagining our interaction with the
physical world. Table III gives the summary of all the case
studies of digital twins taken under consideration in this paper.
A. cmbuilder.io
cmbuilder.io is a web platform that makes it easy for users
to simulate the construction process and accurately, bid, plan
and win projects. 1) Enter an address to generate a 3-D topographic map of your site. 2) Upload BIM models or use
massing feature to visualize your project in context. This startup
uses the following aspects for manufacturing DTs of smart
cities. Fig. 2 shows the working functionality of cmbuilder.io.
1) As-built reality capture—a new dawn in construction:
The advent of modern technology has ushered in a significant transformation within the construction industry,
particularly in the domains of as-built reality capture
and construction site logistics. Through the integration
of advanced techniques, such as 3-D scanning, and photogrammetry, and the utilization of 4-D site logistics
planning platforms, such as cmBuilder.io, stakeholders
have gained the capacity to harness the full potential of
comprehensive digital simulations. This amalgamation
of cutting-edge technologies not only augments planning
efficiency through potent visualizations but also serves as
a means to mitigate construction-related risks, ultimately
resulting in enhanced project delivery. The significance
of as-built reality capture in the construction sphere cannot be overstated. This innovative technology, leveraging
the capabilities of 3-D scanning and photogrammetry,
empowers architects, engineers, and contractors to accurately and promptly capture existing conditions. By
engendering a comprehensive digital representation of the
physical world, these technologies yield a treasure trove
of information that serves as a guiding beacon throughout
the construction life-cycle. 3-D scanning, rooted in laser
technology, facilitates the acquisition of spatial data. It
diligently maps physical entities or environments and
seamlessly transforms them into digital 3-D models.
These models are amenable to manipulation, analysis, and
sharing, offering insights that might elude conventional
2-D drawings. In parallel, photogrammetry, through the
assembly of meticulously stitched-together photographs,
engenders 3-D meshes capable of faithfully representing the physical realm in terms of scale and contextual
relevance. When employed in tandem with 3-D scanning, it furnishes a more comprehensive perspective of a
construction site, providing a precise portrayal of structures, topography, and the surrounding environment [81].
2) 4-D site logistics planning—A paradigm shift in construction management: While 3-D reality capture provides
a comprehensive representation of the present state of
TABLE III
SUMMARY OF DT CASE STUDIES: THE VARIOUS GOALS AND ADVANTAGES OF THE DT-BASED STARTUPS
a construction site, the emergence of 4-D site logistics
planning platforms, such as cmBuilder.io, elevates this
concept to a new level of sophistication. These platforms
introduce time as the fourth dimension, affording project
managers the capability to visualize and oversee the entirety of the construction process, from its inception to its
culmination.
A notable exemplar, cmBuilder.io, furnishes an
interactive 4-D simulation of the construction endeavor
by seamlessly integrating both spatial and temporal
dimensions. This integration encompasses critical
resources, including but not limited to fences, cranes,
hoists, and more, thus presenting a holistic perspective of
the logistical aspects of construction on-site. Empowered
by this technology, project teams can engage in the
simulation of diverse scenarios, optimize construction
schedules, allocate resources judiciously, and proactively
address potential disruptions. Through the identification
of challenges in advance, cmBuilder.io streamlines
project management, ultimately augmenting overall
productivity and efficiency [82].
3) DroneDeploy—A game changer for aerial surveys:
DroneDeploy complements 3-D scanning and photogrammetry by offering a bird’s-eye view of construction
sites. This cloud-based drone mapping software captures
high-resolution aerial data, which can be converted into
orthomosaics, 3-D models, and topographical maps. With
DroneDeploy, construction professionals can easily monitor progress, identify potential issues, and make real-time
adjustments, enhancing overall construction site logistics [83].
4) Power of integrated workflows: The integration of as-built
reality capture with 4-D site logistics planning platforms,
such as cmBuilder.io, revolutionizes construction site
logistics by combining 3-D scanning, photogrammetry,
DroneDeploy, and cmBuilder.io. This synergy offers a
comprehensive view of construction projects, facilitating
precise planning and execution through accurate 3-D
models and aerial imagery. Furthermore, these technologies enhance collaboration among stakeholders by enabling the easy sharing and access of 3-D models and
4-D simulations, fostering clear communication and reducing misunderstandings and rework. This integration
is reshaping the construction industry, empowering professionals to deliver projects on time, within budget, and
with exceptional quality. The future of construction site
logistics is digital, and it holds immense promise for the
industry’s continued advancement [84].
Fig. 2. Working Functionality of cmbuilder.io: A web platform facilitating the simulation of construction processes, allowing users to accurately bid,
plan, and win projects. It generates 3-D topographic maps from addresses and visualizes projects using BIM models or massing features, aiding in
the creation of DTs for smart cities.
B. NEWTWEN
This case study explores the groundbreaking software developed by the Italian startup NEWTWEN, designed to create
accurate and real-time DTs for electromechanical and electronic
components within electric powertrains. NEWTWEN’s proprietary algorithms enable the construction of compressed yet
highly precise DTs, facilitating optimal thermal management,
fault identification, predictive maintenance, and performance
enhancement. This software revolutionizes the automotive industry by providing manufacturers with the tools to improve
hardware systems, ultimately increasing efficiency and reducing
maintenance costs [85].
NEWTWEN’s software comprises a four-step DT Factory,
streamlining the process of constructing DTs for electromechanical components.
1) Full-order model (FOM): This phase begins with the
importation of 2-D/3-D CAD models, which are automatically processed to create an accurate digital replica,
capturing geometry and material details.
2) Reduced-order model (ROM): Electromagnetic and thermal analysis results in a compressed yet physically accurate model, significantly reducing computational complexity for integration into real-time embedded firmware.
3) AI model calibration: Empirical measurement data from
laboratory tests are used to calibrate the DT with machine learning algorithms, ensuring the highest accuracy. The graph provided in Fig. 3 shows the perfection
that is achieved by using AI for model calibration as
it is put alongside the calibration curve without using
AI.
4) DT embedded code generation: The software facilitates
automatic code generation for embedding DT models into
simulation environments and embedded firmware [86].
NEWTWEN’s software offers a range of benefits and key
features.
1) Real-time monitoring: The DT enables real-time performance monitoring of critical parameters, enhancing
IoT-based systems and cloud platforms.
2) Optimal thermal management: Smart soft sensors generated by the software optimize thermal management,
improving performance, safety, and reducing production
costs.
3) Predictive behavior and what-if scenarios: Models predict system behavior in real-world conditions, leading
to higher efficiency, energy savings, longer lifespan, and
lower maintenance costs.
4) Fault detection and predictive maintenance: The adaptive
capacity of the software enhances reliability, safety, and
reduces unscheduled downtime.
5) Lower development costs: NEWTWEN’s platform saves
substantial time and effort for thermal modeling, significantly reducing development time compared to thirdparty software [87].
6) Lower production costs: The software reduces bill of
material complexity, energy usage, and engine size while
maintaining performance, resulting in reduced production
costs.
NEWTWEN’s innovative software represents a significant advancement in the automotive industry, providing manufacturers
with the tools to optimize their electric powertrains. By creating
Fig. 3. NEWTWEN: How it works.
accurate and real-time DTs, NEWTWEN’s software improves
efficiency, lowers maintenance costs, and enhances overall system performance, ultimately contributing to a more sustainable
and cost-effective future for electric powertrains. This case study
highlights the immense potential of NEWTWEN’s technology
in revolutionizing the electric vehicle landscape [88].
C. Novacene
This case study examines the innovative approach taken
by Novacene, a U.K.-based startup, in partnership with East
Renfrewshire Council (ERC) to enhance indoor air quality in
educational institutions using DTs and IoT technology. Novacene’s platform enables property owners and managers to
optimize building performance and environmental impact by
creating DTs and utilizing real-time sensor data. The study
highlights the successful implementation of this technology in
ERC’s 47 schools, emphasizing its ability to provide actionable
insights quickly and meet statutory requirements for indoor air
quality [89].
Novacene, a pioneering U.K. startup, specializes in a building
health platform that leverages DTs and IoT technology to monitor and optimize building performance, energy efficiency, and
environmental impact. This case study delves into their collaboration with ERC, wherein Novacene’s expertise was employed
to address indoor air quality concerns in educational institutions.
1) Challenges Faced by ERC: ERC, responsible for managing 47 schools, recognized the need for a smart monitoring
solution to ensure safety and productivity in classrooms, especially during the winter months and amidst rising COVID-19
transmission rates. The council turned to Novacene for datadriven insights to enhance air quality across all ERC learning
establishments.
2) Novacene Solution: Working closely with ERC, Novacene devised a three-phase strategy, swiftly implemented over
a three-week period. They initiated the process by creating DTs
of each school’s floor plans, ensuring minimal disruptions during
the installation of 2500 smart wireless sensors across all learning
areas. These sensors collected data on CO2, temperature, and
humidity levels [90]. Fig. 4 shows the working principles of
Novacena.
3) Rapid Data Insights: Once operational, the sensors provided ERC with real-time air quality data, enabling the identification of schools and classrooms requiring immediate attention
within just three days of installation.Within one week, Novacene
delivered comprehensive reports on the overall portfolio of
schools and individual school analyses, meeting and exceeding
Department of Education Scotland’s statutory requirements for
indoor air quality.
The partnership with Novacene yielded remarkable outcomes
includes the following.
1) Provision of actionable data within as little as three days
from installation.
2) Detailed analysis of air quality in all learning areas delivered within one week of live data tracking [91].
3) Compliance with Department of Education Scotland
statutory requirements for indoor air quality in schools.
4) Future Prospects: Novacene’s advanced AI technology
continues to empower ERC in identifying emerging patterns
and trends in air quality data across all 47 schools in real time.
Their collaboration extends to enhancing energy efficiency by
recognizing the relationship between CO2 levels and energy
consumption, thereby reducing energy waste and optimizing
consumption [92]. The Novacene-ERC collaboration demonstrates the transformative potential of DTs and IoT technology in
improving indoor air quality and building efficiency. The success
of this partnership underscores the importance of data-driven
solutions in addressing contemporary challenges faced by educational institutions. Novacene’s innovative approach not only
ensures a healthier learning environment but also contributes
to sustainable energy usage in the long run. This case study
serves as an exemplar for educational institutions and property
Fig. 4. Working principle of Novacene; good denotes good ventilation and air quality; moderate denotes moderate ventilation and air quality. Poor
denotes poor ventilation and air quality, indicating a potential need for improvement. Adequate ventilation and air quality are crucial for maintaining
a healthy and comfortable indoor environment, reducing the risk of respiratory issues, and ensuring overall well-being.
managers seeking innovative ways to enhance building performance and environmental impact. Next section talks about, the
Role of Digital Twins in designing precision machines: A Focus
on Flexure-Based Mechanisms.
D. DTs and Flexure Based Mechanisms
The concept of DT technology has rapidly evolved, offering a powerful tool for designing and optimizing precision
machines, including flexure-based mechanisms. Flexure-based
mechanisms, known for their high precision and repeatability,
are integral in applications such as micropositioning stages and
microgrippers. [93] The integration of DTs in the design process
can significantly enhance the performance and reliability of
these mechanisms. This discussion delves into how DTs can
be utilized in the design of flexure-based mechanisms, using
examples from the literature to illustrate their potential.
DTs and flexure-based mechanisms DTs refer to virtual replicas of physical entities that can simulate, predict, and optimize
performance across various stages of their lifecycle. For precision machines, such as flexure-based mechanisms, DTs offer
several benefits.
Simulation and testing: DTs enable comprehensive simulation of the mechanical behavior of flexure-based mechanisms
under different conditions. This allows designers to test various
scenarios and design parameters without the need for physical
prototypes.
Optimization: By continuously analyzing real-time data and
feeding it back into the simulation model, DTs can optimize the
performance of the mechanism, ensuring it meets the desired
specifications with higher accuracy.
Predictive maintenance: DTs can predict potential failures or
performance degradation, allowing for preemptive maintenance
and reducing downtime.
E. NVIDIA’s 6G Research Cloud: Revolutionizing
Next-Generation Wireless Communication With DTs
NVIDIA’s recent unveiling of its 6G Research Cloud platform represents a significant breakthrough in the development
of next-generation wireless communication technologies. At
the core of this platform is the innovative use of DTs, which
offer powerful solutions to the complexities expected with 6G
networks, including the management of trillions of connected
devices worldwide. The platform integrates three key components: the NVIDIA Aerial Omniverse DT for 6G, which allows for highly accurate simulations of real-world environments
from single cell towers to entire cities; the NVIDIA Aerial
CUDA-Accelerated RAN, a flexible and programmable RAN
stack designed to test novel configurations in real time; and the
NVIDIA Sionna Neural Radio Framework, a tool that leverages
AI to refine wireless algorithms and optimize spectral efficiency.
Together, these tools provide researchers with the ability to advance AI-driven optimizations and model 6G network behavior,
offering insights into improving network performance through
real-time, site-specific data. NVIDIA’s 6G Research Cloud platform signifies a transformative leap in the future of wireless
Fig. 5. NVIDIA 6G user developer program.
communication, merging AI, DTs, and high-performance computing to tackle the intricacies of 6G networks. Central to the
platform is the use of DTs, enabling highly accurate simulations
of network environments—from individual cell towers to vast
urban landscapes. These simulations, powered by the NVIDIA
Aerial Omniverse DT for 6G, incorporate real-world terrains and
data, allowing researchers to refine transmission efficiency and
spectral optimization through real-time model training. Meanwhile, the NVIDIA Aerial CUDA-Accelerated RAN provides a
software-defined, customizable RAN stack that enables the rapid
testing and iteration of novel network configurations, crucial
for meeting 6G’s high demands, such as ultra-low latency and
massive device connectivity. The NVIDIA Sionna Neural Radio
Framework, integrated with machine learning platforms, such as
PyTorch and TensorFlow, further enhances the platform by allowing scalable AI-driven optimizations in wireless simulations,
addressing critical challenges, such as interference management
and network handoffs in a hyperconnected world. Fig. 5 shows
the detials of NVIDIA 6G user developer program.
The broader implications of this platform extend into various industries, offering advanced simulation capabilities that
could revolutionize sectors, such as autonomous vehicles, smart
cities, extended reality (XR), and industrial automation. For
autonomous vehicles, DTs can create detailed traffic and infrastructure simulations to optimize vehicle-to-everything (V2X)
communications, enhancing safety and reducing latency. In
smart city applications, the platform can simulate and optimize
large-scale urban infrastructure, providing valuable insights into
how 6G networks can support utilities, smart buildings, and
other interconnected systems. XR, an area that demands high
bandwidth and low-latency connections, also benefits from realtime simulations, improving immersive experiences in sectors,
such as education, healthcare, and entertainment. Moreover, the
platform’s ability to simulate collaborative robots (cobots) in
industrial environments ensures that automation processes are
safe, efficient, and precise. By integrating these advanced tools
and offering a flexible, open research environment, NVIDIA’s
6G Research Cloud platform is poised to be a critical enabler for
the next wave of wireless technology, driving innovations that
will shape global connectivity for years to come.
F. Case Study: Piezo-Actuated Compliant
Micropositioning Stages
A relevant survey, “A Survey on the Mechanical Design
for Piezo-Actuated Compliant Micro-Positioning Stages,” highlights the importance of precise design in achieving highperformance micropositioning. This study underscores how DTs
can be instrumental in this domain.
Design optimization: DTs can simulate the piezoelectric actuation and its interaction with the compliant mechanism. This
helps in fine-tuning the design to achieve the desired motion
range and resolution.
Material selection: By simulating the mechanical properties
of different materials, DTs can aid in selecting the most suitable
material for the flexure mechanism to ensure durability and
performance [94].
Practical example—asymmetrical underactuated microgripper: To concretely demonstrate the potential of DTs, we can
refer to the specific design and analysis of an asymmetrical
underactuated microgripper.
TABLE IV
CHALLENGES AND SOLUTIONS FOR DTS
Design and analysis: In the study “Design, Analysis, and Experimental Investigations of an Asymmetrical Under-Actuated
Micro-Gripper,” the authors detail the intricate design and testing process. A DT can replicate this process digitally, enabling
multiple iterations and optimizations before physical prototyping.
Performance optimization:By creating a DT of the microgripper, designers can optimize the asymmetrical design for better
gripping force distribution and higher precision in handling
microcomponents.
Experimental validation: The DT can predict the experimental outcomes, and any discrepancies can be used to refine the
model, leading to an iterative improvement cycle.
Conclusion: DT technology stands out as a transformative
approach in the design and optimization of precision machines,
particularly flexure-based mechanisms. By enabling detailed
simulation, continuous optimization, and predictive maintenance, DTs enhance the efficiency and performance of these
mechanisms. Specific examples, such as piezo-actuated compliant micropositioning stages and asymmetrical underactuated
microgrippers, illustrate the practical benefits of integrating DTs
into the design process. As this technology continues to evolve,
its application in precision engineering is poised to expand,
offering unprecedented capabilities in achieving high precision
and reliability [95].
VI. CHALLENGES AND CONSIDERATIONS
DTs have gained significant attention and traction across
various industries due to their promising market potential. A DT
is a virtual representation of a physical object, system, or process,
and it offers a wide range of benefits such as improved operational efficiency, predictive maintenance, and better decisionmaking. However, alongside their market potential, DTs also
present several challenges and considerations that need to be
addressed for successful implementation and adoption. Table IV
summarizes various challenges and respective solutions in the
practical implementation of DTs in real world.
A. Challenges:
1) Data integration and quality: Developing an accurate DT
requires comprehensive and reliable data from various
sources. Integrating data from disparate systems, ensuring
its accuracy, and maintaining data quality over time can
be challenging. Inaccurate or incomplete data can lead
to inaccurate DT models, undermining their effectiveness [96].
2) Complexity of models: Creating an accurate and effective
DT often involves complex modeling techniques that
require expertise in fields, such as physics, engineering,
and data science. Designing and refining these models
can be time-consuming and resource-intensive [25].
3) Scalability: Implementing DTs at scale, especially in
large and complex industrial environments, can be difficult. As the number of interconnected systems and components increases, managing and updating DT models for
each entity becomes more complex [50].
4) Interoperability: In many industries, different systems,
machines, and devices come from different manufacturers and use various communication protocols. Ensuring
seamless interoperability between these components to
create a unified DT ecosystem can be a significant challenge [97].
5) Security and privacy: DTs involve the collection and analysis of sensitive data from physical assets and processes.
Ensuring the security of this data and protecting it from
cyber threats is crucial. In addition, privacy concerns arise
when dealing with personal or proprietary data in the DT
context [98].
B. Considerations:
1) Data governance: Establishing clear data governance
policies is essential to ensure that data used for DTs is
accurate, consistent, and compliant with relevant regulations. This involves defining data ownership, access
controls, and data life-cycle management [15].
2) Model validation and calibration: Validating and calibrating DT models against real-world data are crucial for
their accuracy. Continuously comparing model predictions with actual outcomes helps refine the models and
ensures that they remain relevant [99].
3) Life-cycle management: DTs are most effective when they
are updated to reflect changes in the physical counterpart
throughout its life-cycle. Implementing processes for regular updates, maintenance, and adjustments is necessary
to ensure that DTs remain accurate and valuable [100].
4) Skill-set and workforce: Developing and managing DTs
require a multidisciplinary workforce with expertise in
data analytics, domain knowledge, and model development. Organizations need to invest in training and recruitment to build the necessary skill-set [101].
5) Return on investment (ROI) assessment: While DTs offer
significant potential benefits, organizations must carefully assess the ROI to justify the costs associated with
their implementation. This involves quantifying the value
gained through improved efficiency, reduced downtime,
and other measurable outcomes [102].
DTs hold tremendous market potential across various industries, but their successful adoption requires addressing challenges related to data, complexity, scalability, interoperability,
security, and privacy. Organizations must carefully consider factors such as data governance, model validation, lifecycle management, workforce expertise, and ROI assessment to ensure
that the benefits of DTs are realized while managing associated
risks [103].
VII. USE OF DTS IN VARIOUS FIELDS
There are various applications of DTs in different fields[104].
1) Roads: The application of DTs technology in the road
construction and maintenance sector is a revolutionary
step toward enhancing efficiency, reducing costs, and
ensuring safer and more sustainable infrastructure. This
article explores the multifaceted role of DTs in road
development, from design and planning to construction,
monitoring, and maintenance [105]. By creating virtual
replicas of roads and their surrounding environment,
stakeholders can simulate scenarios, predict performance,
and make informed decisions. The potential of DTs to
streamline processes and optimize resource utilization is
poised to reshape the road construction industry [106].
a) Design and planning: DTs play a pivotal role in the
design and planning phase of road construction. Engineers and designers can create virtual models of roads,
considering factors, such as traffic flow, terrain, and
environmental impact. Simulations can help optimize
designs, leading to road layouts that minimize congestion, reduce environmental impact, and enhance
safety. In addition, stakeholders can collaborate in a
virtual environment to address potential challenges
early in the project life-cycle [70].
b) Construction: The utilization of DTs during the construction phase brings unprecedented advantages.
Contractors can simulate construction processes to
identify potential bottlenecks, improve sequencing,
and optimize resource allocation. This not only enhances efficiency but also minimizes disruptions and
reduces project delays. Real-time monitoring of construction progress using DTs allows project managers
to identify discrepancies between the virtual plan
and the actual progress, facilitating timely adjustments [107].
c) Performance monitoring: Once roads are operational,
DTs continue to play a significant role in performance
monitoring. Sensors embedded in the physical infrastructure provide real-time data that feed into the
digital replica. This enables continuous monitoring
of factors, such as traffic flow, structural integrity,
and environmental conditions. On analyzing this data,
maintenance teams can predict and address potential
issues before they escalate, thus prolonging the lifespan of the road and ensuring user safety [55].
d) Maintenance and repairs: The predictive capabilities
of DTs are especially valuable in road maintenance
and repair. Analyzing these data from sensors and
historical maintenance records, the virtual model can
predict maintenance needs and identify areas prone to
deterioration. This proactive approach allows maintenance crews to target specific areas, reducing the
need for extensive repairs and minimizing disruption
to road users [31].
e) Challenges and considerations: While the potential
of DTs in road construction is immense, challenges
do exist. Ensuring accurate data input for the virtual
replica is crucial, as discrepancies between the physical and digital models could lead to inaccurate predictions. In addition, data security, interoperability,
and the integration of diverse data sources must be
addressed to maximize the benefits of DTs [7].
The integration of DTs in road construction and maintenance is poised to redefine the industry’s landscape; from
streamlined design and planning to efficient construction
and predictive maintenance, the advantages are substantial. With continuous advancement of technology and
stakeholders recognizing the potential for cost savings,
enhanced safety, and improved infrastructure, the adoption of DTs in road development is inevitable [108]. Addressing challenges and leveraging their capabilities, the
road construction sector can drive innovation, optimize
resource utilization, and create a more sustainable and
resilient transportation infrastructure for the future [109].
2) Buildings and bridges:The integration of DTs technology
has ushered in a new era of innovation in the construction
industry, particularly in the creation of buildings and
bridges. This article explores the transformative potential of DTs throughout the life-cycle of these structures,
from design and planning to construction, operation, and
maintenance. Enabling real-time visualization, simulation, and analysis, DTs optimize resource allocation,
enhance safety, and promote sustainability. This article
delves into the diverse applications of DTs, illustrating
their capacity to reshape the construction landscape [54].
a) Introduction: DTs have emerged as a game-changing
technology, transcending traditional construction
practices in the creation of buildings and bridges.
Through the creation of virtual replicas, stakeholders
can simulate and analyze various aspects of a project,
leading to informed decision-making, improved efficiency, and enhanced collaboration. This article showcases the multifaceted role of DTs in revolutionizing
the construction industry [110].
b) Design and planning: DTs are a cornerstone of modern construction design and planning. Architects and
engineers can create virtual models of buildings and
bridges, integrating parameters, such as structural integrity, aesthetics, and environmental impact. These
simulations facilitate collaboration among stakeholders, enabling them to refine designs and address potential issues before construction begins. Visualization
of the final outcome in a virtual environment helps
project teams to align their vision and reduce costly
revisions [111].
c) Construction: In the construction phase, DTs prove
invaluable by optimizing processes and resource allocation. Contractors can simulate construction sequences, identify potential clashes, and optimize
equipment deployment. This leads to reduced downtime, improved safety, and streamlined workflows.
Furthermore, real-time monitoring through DTs enables project managers to track progress and compare
it with the virtual plan, enhancing accountability and
facilitating timely adjustments [112].
d) Operation and performance monitoring: After completion, DTs continue to provide benefits in the operational phase. Stakeholders can monitor factors,
such as energy consumption, occupancy patterns, and
structural health, by integrating sensor data from the
physical structure into the virtual replica. Predictive
analytics help identify maintenance needs, preventing
costly downtime and ensuring the longevity of the
building or bridge [113].
e) Maintenance and repairs: DTs offer a proactive approach to maintenance and repairs. The virtual model
can predict potential issues and areas prone to deterioration, by analyzing sensor data and historical maintenance records. Maintenance teams can then prioritize
tasks and allocate resources more efficiently, reducing
the impact on users and extending the lifespan of the
structure [114].
f) Challenges and considerations:While the potential of
DTs in construction is vast, several challenges must be
addressed. Ensuring accurate and up-to-date data for
the virtual replica is crucial for accurate predictions
and analyses. The interoperability of various software
tools and data sources must also be considered to
maintain a comprehensive digital representation. In
addition, ensuring data security and protecting intellectual property are paramount concerns [115].
3) Vaccines and medicines: The integration of DTs technology in the manufacturing of vaccines and medicines
marks a transformative leap in the pharmaceutical industry [116]. This article delves into the profound impact of
DTs across the entire life-cycle of drug production, from
research and development to manufacturing and quality
control [117]. Pharmaceutical companies can accelerate
innovation, enhance efficiency, and ensure the production of safe and effective treatments, by creating virtual
replicas that mirror real-world processes [118].
a) Research and development: DTs play a pivotal role
in drug discovery and development. Creation of virtual models of molecular structures and simulating interactions help researchers to streamline the
process of identifying potential candidates for vaccines and medicines. This accelerates the preclinical stage, expediting the journey from lab to market
[119].
b) Process development: The manufacturing process for
pharmaceuticals is intricate and must adhere to strict
regulatory standards. DTs allow companies to simulate and optimize production processes before they
are implemented in the physical world. This reduces
the need for costly trial-and-error approaches, leading
to faster scale-up and production readiness [120].
c) Manufacturing optimization: DTs facilitate the optimization of manufacturing operations. Manufacturers
can simulate different scenarios to identify bottlenecks, reduce downtime, and enhance resource allocation, by creating virtual replicas of production
lines and equipment. This results in increased efficiency, reduced waste, and accelerated production
timelines [121].
d) Quality control and compliance: Ensuring product
quality and compliance with regulatory standards is
paramount in pharmaceutical manufacturing. DTs enable real-time monitoring and data analysis, allowing
manufacturers to detect deviations from expected parameters. This proactive approach to quality control
minimizes the risk of producing substandard products
and ensures adherence to strict regulations [122].
e) Challenges and considerations: While the potential
of DTs in pharmaceutical manufacturing is immense,
challenges, such as data integration, accuracy, and
cyber-security, must be addressed. Ensuring that the
virtual model accurately reflects real-world processes
is crucial for making reliable predictions and decisions [123].
DTs are reshaping pharmaceutical manufacturing, driving innovation, and efficiency in the production of vaccines and medicines. As the industry embraces this technology, the creation of safer, more effective treatments
becomes more accessible. Using the capabilities of DTs to
the fullest, pharmaceutical companies can accelerate drug
development, optimize manufacturing processes, and ultimately contribute to the advancement of healthcare on
a global scale [124].
4) 6G communication DTs play a transformative role in
enhancing 6G communication by providing a detailed
virtual model of the physical network infrastructure. This
digital counterpart allows network operators, engineers,
and researchers to visualize, simulate, and manage the
network in ways that were previously unattainable. Here
is how DTs contribute to 6G communication in detail.
a) Network optimization and real-time management:
DTs enable operators to continuously monitor the
entire 6G network in real time. They create a mirror
of every aspect of the network, from device behavior
to traffic patterns, signal strength, and user density.
With this level of insight. The DT can run simulations
to predict traffic congestion, latency spikes, or signal
interference before they impact real users. This allows
for preemptive adjustments, such as rerouting data
traffic or reallocating bandwidth. Operators can finetune network parameters dynamically, optimizing for
speed, bandwidth, and energy efficiency. For instance,
as demand changes during peak times, the twin model
helps identify resource bottlenecks, guiding decisions
on load balancing. By integrating with edge computing nodes, the DT can optimize data processing
between the cloud and the edge, improving response
times and reducing latency [125].
b) Testing and prototyping new technologies: Before any
new device, service, or architecture is deployed, it
can be virtually tested within the DT environment.
Engineers can run simulations on 6G infrastructure
modifications—such as upgrading base stations or
integrating new frequency bands—without affecting
the live network. By identifying potential issues in the
virtual model, they can ensure that new technologies
will perform as expected in the real world. DTs can
simulate different device types and conditions (e.g.,
smartphones, IoT devices, and autonomous vehicles),
ensuring new devices are compatible with the network’s protocols, frequencies, and quality standards.
This testing reduces the chances of device-network
conflicts or incompatibilities postlaunch. DTs allow
experimentation with energy-saving algorithms or
hardware configurations, aiding in the development
of more energy-efficient 6G networks.
c) Predictive maintenance and fault prevention: DTs
can detect potential network issues before they affect users by analyzing real-time data and simulating
future scenarios. By using AI-driven analytics on the
twin model, operators can foresee where hardware
failures (such as base station malfunctions or signal tower issues) might happen. Maintenance can be
scheduled proactively, reducing unplanned outages.
When issues, such as packet loss or degraded signal
quality, arise, DTs can quickly simulate the network’s
entire architecture, pinpointing the exact source of the
problem. This allows operators to address issues more
swiftly than through traditional troubleshooting. By
preventing faults before they occur, DTs contribute
to higher uptime and more reliable connectivity, key
goals of 6G.
d) Enhanced network security: Security in 6G networks
is paramount, and DTs play a crucial role in identifying and mitigating potential threats. By creating
virtual replicas of the network, DTs allow for safe
testing of various attack scenarios, such as DDoS
(Distributed denial-of-service) attacks, malware infiltrations, or data breaches. These simulations enable
operators to see how the network responds under
attack, helping them patch vulnerabilities before they
can be exploited in real-world conditions. Using machine learning algorithms, DTs can monitor for abnormal behaviors within the network, such as unexpected
data spikes or unrecognized devices connecting to the
network. These indicators can signal security threats,
triggering automated responses to contain or neutralize the threat before it escalates. DTs can be used to
simulate the implementation of new security protocols, verifying how they impact network performance
and whether they introduce new vulnerabilities.
e) Resource management and load balancing: DTs allow for efficient resource management in 6G networks, particularly in balancing high data demands
across users and devices. The twin model can predict
where data bottlenecks may form (e.g., in densely
populated areas or during peak usage times). By
simulating traffic distribution, operators can reroute
traffic and allocate resources dynamically, ensuring
consistent speed and low latency across the network.
By simulating energy consumption patterns, DTs help
operators adjust network functions, such as powering
down underutilized nodes or reallocating resources
to higher demand areas, improving overall network
efficiency.
f) Virtualized network slicing and service customization: DTs are critical to the implementation of network slicing in 6G, where the physical network is
virtually divided into slices, each tailored to specific
use cases (e.g., IoT, autonomous vehicles, or highbandwidth applications, such as AR/VR). DTs can
simulate different network slices, allowing operators
to test how each slice performs under varying conditions (e.g., load stress or signal interference). This
ensures that each slice is optimized for its specific use
case, without negatively impacting other slices. By
mirroring user behaviors and service demands, DTs
enable personalized services. Operators can simulate
and deploy services tailored to individual users or industries, such as enhanced IoT connectivity for smart
cities or ultrareliable low-latency communication for
autonomous systems.
In 6G communication, DTs serve as a powerful tool to enhance network performance, improve testing and deployment
TABLE V
APPLICATION OF DTS IN DIFFERENT FIELDS: HOW THEY ARE USED AND THEIR BENEFITS
processes, and ensure network resilience through predictive
maintenance and threat detection. By virtually simulating the
entire network, operators can innovate more efficiently, maintain higher service quality, and implement security measures
proactively. This detailed, real-time insight into network behavior marks a significant advancement in how future communication networks will be managed and optimized. Table V
summarizes the applications of DTs in various fields mentioned
above.
VIII. MARKET POTENTIALS OF DTS
The concept of DTs has emerged as a transformative technology, blurring the boundaries between the physical and digital
realms. This article delves into the remarkable market potentials
that DTs offer across various industries. Being a versatile tool,
DTs are poised to revolutionize processes, enhance decisionmaking, and optimize efficiency [126]. We explore their
applications in manufacturing, healthcare, energy, and urban
development, shedding light on the immense value they bring to
Fig. 6. DT of the “Queensferry Crossing” bridge in Scotland uses real-time data from sensors to monitor strain, vibrations, temperature, and
corrosion, helping engineers optimize maintenance and extend the bridge’s lifespan. Designed for a 120-year life, the DT’s insights can extend
the bridge’s longevity by an additional 10–20 years. It also improves durability by enhancing fatigue resistance by 15%–20%, reducing corrosion’s
impact by 30%–40%, and managing load distribution to reduce wear by 10%–15%. This data-driven approach ensures the bridge remains safe and
durable for decades beyond its design life.
the table. The challenges and considerations accompanying their
implementation are also discussed, presenting a comprehensive
view of the landscape that the technology is set to reshape.
1) Manufacturing:In the manufacturing sector, DTs are projected to be a game-changer. Manufacturers can simulate
various scenarios, optimize processes, and predict maintenance needs, by creating virtual replicas of products,
production lines, and even entire factories [127]. This
results in reduced downtime enhanced productivity, and
efficient resource allocation. Moreover, the application of
DTs in product life-cycle management enables real-time
monitoring and data-driven improvements, resulting in
higher quality products. With the shifting of manufacturing landscape toward Industry 4.0, the market potential
of DTs becomes increasingly evident [128].
2) Healthcare: DTs have the potential to revolutionize
healthcare by enabling personalized medicine and predictive care [129]. Medical professionals can simulate
treatment responses and predict potential health issues,
by creating virtual models of individual patients. This
proactive approach not only improves patient outcomes
but also reduces healthcare costs. Furthermore, DTs facilitate medical training, allowing practitioners to practice
procedures on virtual patients[130], enhancing their skills
without risk. The healthcare industry is on the cusp of a
transformative shift, with DTs playing a pivotal role in
this evolution.
3) Energy: The energy sector is embracing DTs to optimize
operations and improve sustainability. Creating digital
replicas of power plants, grids, and renewable energy installations helps operators to simulate various conditions
and assess the impact of different strategies on efficiency
and environmental impact [52]. This empowers them to
make informed decisions that balance energy demand,
supply, and environmental concerns. The world seeks
greener and more efficient energy solutions. This makes
the market potential for DTs in the energy sector quite
substantial [131].
4) Urban development: DTs are reshaping the way cities are
designed, built, and managed. City planners can simulate
the impact of various infrastructure projects, transportation systems, and policies, by creating virtual representations of urban environments [112]. This aids in designing
more sustainable, resilient, and livable cities. In addition, DTs facilitate real-time monitoring of urban assets,
enabling predictive maintenance and swift responses to
emergencies [107]. The global rise in urbanization makes
the market potential for DTs in urban development, a vast
one.
There are a few more fields where DTs hold ample potential
to thrive.
1) Aerospace and defense: DTs optimize aircraft design,
manufacturing, and maintenance, enhancing safety and
efficiency [132].
2) Automotive industry: Virtual testing of vehicle components accelerates innovation, reduces costs, and supports
autonomous and electric vehicle development [133].
3) Smart agriculture: DTs enable precision farming by
tracking crop growth and livestock health, leading to
higher yields and resource efficiency [134].
4) Infrastructure and construction: Planning and managing
construction projects become more efficient, resulting in
cost savings and improved project outcomes [135]. Fig. 6
shows the details of queensferry crossing digital twin.
5) Oil and gas industry: DTs monitor and predict maintenance needs of complex assets, improving operational
efficiency and safety [136].
6) DTs can be used in the Industry 4.0 for consumer electronics [137].
7) Entertainment and gaming: DTs create immersive and
realistic experiences in video games, VR and AR applications [138].
In conclusion, DTs represent a paradigm shift in how industries operate, innovate, and grow. Evolution of technology and
industries embracing digitalization, the market potential of DTs
is yet to be realized globally. Organizations can largely benefit
by tackling challenges and capitalizing where necessary.
IX. CONCLUSION
DTs, driven by advanced technologies, such as AI, the IoT,
and Big Data, are transforming industries by offering real-time,
dynamic simulations of physical entities. In manufacturing,
DTs support predictive maintenance, minimize downtime, and
optimize production. In healthcare, they enable personalized
medicine through patient-specific simulations and support the
predictive maintenance of medical equipment. Smart cities benefit from improved resource management, enhancing traffic flow,
energy use, and waste management. Future advancements, such
as the Internet of DTs, will foster networks of interconnected
digital replicas, while AR/VR integration will further enrich
visualization and interaction. Key challenges remain, including
ensuring data security for sensitive information, achieving interoperability across platforms, and advancing AI algorithms, for
better predictive capabilities. Addressing these challenges will
unlock the immense potential of DTs to reshape industries, driving efficiency, cost-effectiveness, and innovation—a promising
step toward a smarter, more connected future.