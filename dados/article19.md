Title: Accurate, Yet Scalable: A SPICE-based Design and Optimization
Framework for eNVM-based Analog In-memory Computing

ABSTRACT
This paper introduces a scalable SPICE-based tool infrastructure
designed to optimize analog compute-in-memory (ACIM) architectures utilizing emerging non-volatile resistive memory (eNVM)
technologies. The inherent efficiency of analog eNVM crossbar
arrays in performing matrix-vector multiplications significantly
enhances the power, performance, and area efficiency of edge AI
devices and other applications. Our framework addresses the challenges of accurately simulating ACIM architectures, which are
highly susceptible to variations in process, voltage, temperature,
and analog noise. The framework uses SPICE for accurate analog
and mixed-signal circuit simulation. It automates the generation
of SPICE-level ACIM designs for deep neural networks. Additionally, it speeds up the simulation runtime by up to 35× for large
DNN models while maintaining the same SPICE-level accuracy.
Moreover, it ensures simulation convergence for large netlists, facilitating SPICE simulation of large-scale eNVM crossbars that were
previously impractical. We demonstrated that our framework is
capable of simulating inference using netlists for MLPs with over
800,000 parameters trained on the MNIST dataset within acceptable runtime, where contemporary SPICE simulators do not even
converge. We validated the simulation results in terms of inference
accuracy, which shows less than a 3.8% accuracy drop compared
to software-based inference results. Lastly, we demonstrated the
integration of our framework with an architectural simulator, facilitating comprehensive system-level simulation.
CCS CONCEPTS
• Hardware → Electronic design automation.
KEYWORDS
Analog in-memory-computing, eNVM, SPICE, Design automation
1 INTRODUCTION
The integration of artificial intelligence (AI) in edge devices necessitates highly efficient hardware capable of supporting Deep Neural
Network (DNN) models. Compute-in-memory (CIM) architectures,
utilizing emerging non-volatile memories (eNVMs) such as Resistive Random-Access Memory (RRAM), present a promising solution
to meet the demands for low-power, high-density computing necessary for edge AI applications [1]. These architectures leverage
the intrinsic properties of eNVMs, where matrix-vector multiply
and accumulate (MAC) operations are performed by modulating
the device conductance to mirror the neural model weights [2].
Among CIM approaches, analog compute-in-memory (ACIM) is
particularly advantageous for its superior power, performance, and
area (PPA) efficiency, attributed to the analog nature of computation
within eNVM crossbars [3]. However, designing and optimizing
eNVM-based ACIM poses considerable challenges, primarily due
to the extreme sensitivity of these systems to noise, and process,
voltage, and temperature (PVT) variations, which can significantly
affect both hardware functionality and software-level inference accuracy [4]. Accurate simulations are therefore essential for achieving functional, reliable, and optimized design.
SPICE, the industry standard for analog and mixed-signal (AMS)
circuit simulation, offers high accuracy in circuit design and devicelevel characterization [5]. As the primary language for AMS circuit
development, it offers a plethora of analysis options and design flexibility. SPICE is widely adopted by leading EDA companies, design
houses, and fabrication facilities integrated within their PDKs. Its
adaptability and customizability allow for the seamless integration
of new circuit topologies and hardware innovations. Therefore,
leveraging SPICE simulation is desirable for designing, developing,
and researching ACIM architectures that integrate eNVM arrays
with CMOS analog circuit blocks, and account for interconnect parasitic [6]. However, SPICE faces scalability challenges with design
and testbench generation for large-scale systems such as eNVM
crossbar array-based ACIM architectures. Additionally, the conventional pulse-based write-verify method for mapping DNN weights
to large eNVM crossbar arrays is not only time-consuming to simulate but also complex, making the retention of mapped conductance
values for subsequent inference simulations complicated. Moreover, simulating large crossbars and their peripheral circuits for
even small DNNs can lead to extended simulation times or nonconverging DC iterations as the netlist size increases.
Numerous simulation frameworks have been proposed for both
architecture and circuit analysis to enhance the accuracy and efficiency of hardware model simulations for DNN applications. However, a common issue among these frameworks is their reliance
on built-in modules for their result estimation, which often limits
flexibility and accuracy. This is particularly problematic for conducting detailed design trade-offs necessary for the development
of fabricable Analog Compute in Memory (ACIM) designs.
For example, popular pre-RTL simulators such as MNSim [7] and
NeuroSIM [8] are highly efficient in simulating hardware models
and facilitating early PPA estimations and design decisions. Yet,
their dependency on integrated estimation modules restricts their
utility in detailed circuit-level analysis. In response to these limitations, more focused circuit-level analysis frameworks have been
developed. A notable example includes a MATLAB-based dot product engine [9], which not only enhances simulation speed but also
achieves greater circuit-level inference accuracy by mapping pretrained weights to the crossbar array while accounting for device
non-idealities. Despite its advancements, this framework lacks the
versatility required for broader ACIM design applications and does
not provide accurate latency and power calculations.
Further advancements include CCCS [10], another MATLABbased framework that reports significant simulation speedups. However, it suffers from a high error rate, which could critically undermine the functional integrity of ACIM designs. Similarly, MemSPICE [11], a SPICE-based logic-in-memory framework, excels in
generating SPICE netlists and test benches for energy estimation
in logic-in-memory (LIM) applications but falls short in addressing the design challenges of large crossbar arrays and essential
peripherals for CIM implementations. IMACSim [12], a more recent
endeavor, provides a simulation framework for analog crossbar
simulation in eNVM, featuring design partitioning and full-spice
simulated results for measuring inference accuracy, power, and
latency. However, it employs ideal resistors to model the resistive
memory devices for ACIM design. This simplification overlooks the
complex non-idealities associated with real eNVM device models,
which can significantly impact the fidelity of simulation results.
Furthermore, IMACSim lacks comprehensive peripheral circuits
and does not provide a robust system-level organization, essential
for creating a scalable system that can be integrated with practical
DNN hardware. Additionally, it fails to address the critical issue of
non-convergence in SPICE simulations, which is a significant barrier for designers using SPICE for large ACIM design analysis. Table
1 provides a detailed comparison between the proposed ACIM simulation framework and other established simulation frameworks
such as DPE, CCCS, IMAC-Sim, MemSPICE, and NeuroSim.
Despite the availability of sophisticated simulation languages
like SPICE and tools such as Cadence Spectre and Hspice, there
is a significant gap between these advanced simulation resources
and their integration with the promising hardware developed for
DNN acceleration, particularly in the research community focused
on analog and mixed-signal computation. This gap impedes the
ability of designers and researchers to effectively use these tools
in tandem, which would otherwise enhance research quality and
reduce both design and analysis time significantly. To address the
identified challenges in ACIM design and simulation, this paper
makes several key contributions through our novel framework. The
tool, SpiceCiM1
is made open source for researchers and designers.
1 Automated SPICE Netlist Generation: Our framework automates SPICE netlist creation for any DNN model, streamlining the transition from design to hardware implementation.
1The open source tool: https://github.com/ASTHA-Lab/SpiceCiM
2 DNN Weights to eNVM Conductance Mapping: It maps DNN
model weights to eNVM conductance values in crossbar arrays, ensuring accurate reflection of neural network requirements.
3 Accurate Inference Simulation: The framework generates
netlists and accurately simulates inference on designed hardware, validating DNN performance, latency, energy consumption, and inference accuracy in real-world scenarios.
4 Seed Crossbar-Based Simulation Optimization: A novel seed
crossbar re-mapping methodology significantly reduces simulation run times and addresses non-convergence issues in
SPICE simulations of large crossbar arrays, improving feasibility and efficiency.
5 Integration with GEM5: Demonstrates compatibility with
the GEM5 architectural simulator for comprehensive systemlevel simulations.
The rest of the paper is structured as follows: Section 2 provides
the necessary background; Section 3 details our proposed framework; Section 4 discusses the results obtained from our analyses,
and Section 5 concludes the discussion.
2 BACKGROUND
2.1 Emerging non-volatile Memories
Emerging Non-Volatile Memories (eNVMs) represent a diverse class
of storage technologies that retain stored information even when
not powered, offering promising alternatives to traditional volatile
memory systems like DRAM. These technologies include Resistive
Random Access Memory (RRAM), Phase-Change Memory (PCM),
Ferroelectric RAM (FeRAM), and Magnetoresistive RAM (MRAM),
each characterized by unique materials and mechanisms that offer
distinct advantages and challenges. Most of the eNVM can be used
as compute-in-memory devices for their unique characteristics to
form crossbar array [13, 14]. Here we are going to briefly review
some of the promising eNVM devices.
2.1.1 Resistive Random Access Memory (RRAM). RRAM operates
based on the resistance change in a dielectric solid-state material,
often referred to as a memristor [15, 16]. When a voltage is applied,
the dielectric changes from a high-resistance state (HRS) to a lowresistance state (LRS) and vice versa. This switching mechanism
is highly scalable, energy-efficient, and capable of fast switching,
making RRAM particularly suitable for memory-intensive applications. RRAM crossbar array configuration can be utilized as a
non-volatile memory for storage [17] and security [18] applications.
It is also one of the key devices for in-memory-computing research
and development [19, 20].
2.1.2 Phase-Change Memory (PCM). PCM [21] employs the property of chalcogenide glass, which can be switched between amorphous and crystalline states through the application of heat generated by electric current. The significant difference in electrical
resistance between these states is used to represent binary data.
PCM offers durability and high speed but struggles with high programming currents and thermal stability.
2.1.3 Ferroelectric RAM (FeRAM). FeRAM [22] utilizes ferroelectric materials, which exhibit spontaneous polarization to store data.
The polarization direction of these materials can be altered with an
electric field, allowing for data storage. FeRAM combines attributes
of both RAM and flash memory, being both fast and non-volatile,
though it typically offers lower density compared to other forms of
eNVM.
2.1.4 Magnetoresistive RAM (MRAM). MRAM [23] uses magnetic
states to store data, relying on magnetic tunnel junctions (MTJ)
that can be magnetically flipped between parallel (low resistance)
and antiparallel (high resistance) alignments. MRAM is notable for
its durability and speed, which are comparable to DRAM, making
it an attractive option for universal memory applications.
In this paper, we will be using RRAM for the evaluation purpose
of our framework.
2.2 Analog Compute in Memory using RRAM:
In a typical RRAM crossbar array, a grid-like structure comprises
perpendicular sets of parallel wires, with RRAM cells situated at
each intersection. However, in practice, a 1 transistor 1 memristor,
commonly known as 1T1R cell, is used to eliminate sneak path current. Each RRAM cell can be set to different resistance states (high
or low) by altering the voltage across them, representing storing
binary data. For computing, these resistance states are inherently
used to perform matrix-vector multiplications through Ohm’s law
and Kirchhoff’s current law. When a vector of voltages is applied to
one set of parallel wires (wordlines), the resulting currents flowing
through the perpendicular wires (bitlines) are determined by the
resistances of the RRAM cells, effectively computing the dot product of the resistance matrix and the input voltage vector. However,
modern RRAM devices often feature multiple states, enhancing the
potential for analog in-memory computing. As a promising avenue
for sustainable computing technologies, numerous research initiatives [24–27] have been undertaken and continue to be explored. A
recent study reported 100 states in RRAM devices [28] which may
open up the opportunity to explore analog in-memory computing
even further.
3 PROPOSED FRAMEWORK
Our proposed end-to-end design and simulation framework for
eNVM-based ACIM is illustrated in Fig. 1. As mentioned earlier,
RRAM has been selected as the example eNVM device to demonstrate the capabilities of our framework. The process begins by retrieving user-specified design and simulation configurations from
a simple configuration script, ‘config.ini’. Subsequently, the
framework constructs the neural network (NN) model using hyperparameters defined by the user. Following this, the Hierarchical
Design Generator within the framework produces a comprehensive
netlist that includes both the crossbar array and peripheral circuits
tailored to the generated NN model. The design is partitioned from
the Synaptic Array to the Processing Elements (PEs) and Tiles,
with the configuration of the synaptic array size, the number of
synaptic arrays per PE, and the number of PEs per Tile being fully
reconfigurable based on user specifications.
After the design phase, we implement an innovative weight mapping strategy that converts neural network weights into RRAM
conductance values and maps them onto the device model. Next,
our framework introduces a novel SPICE-level hardware-software
co-simulation engine, that employs a seed crossbar array to significantly reduce simulation run times while maintaining full SPICEsimulation level accuracy. Finally, the framework compiles and
processes all simulation data, generating detailed inference results
and an analysis report. This report provides metrics such as the inference latency of the hardware, the total energy consumption, and
the hardware-level inference accuracy. We will now dive into the
specific components and functionalities of our proposed framework.
3.1 DNN Model Generation and Training
The first component of our framework is the DNN model generator, as depicted in Fig. 1(a). This generator constructs the neural
network model based on the hyper-parameters specified in the
‘config.ini’ file, utilizing popular deep learning libraries such as
TensorFlow or PyTorch. For instance, to create a Multilayer Perceptron (MLP), the user must define the size of the input layer, the
number of hidden layers, the size of each hidden layer, and the size
of the output layer. If the number of hidden layers is specified as
’0’, the generator creates a straightforward Single-Layer Perceptron
(SLP) directly mapping inputs to outputs.
Following the model construction, it is trained using a selected
dataset. In the current implementation, we utilize built-in training
datasets provided by the deep learning library. For the purposes of
evaluation in this paper, the MNIST dataset of handwritten digits
was chosen. For training, user can choose between Quantizationaware Training (QAT) or Post-training Quantization (PTQ) methods.
Once the model is trained, we extract the model and its parameters
to proceed with the generation of the hierarchical design of the
RRAM crossbar. This trained model and the associated parameters
form the basis for further simulations and hardware implementations in subsequent stages of our framework.
3.2 Hierarchical Design Generator
As illustrated in Fig. 1(b-c), the Hierarchical Design Generator is
one of the important components of our framework. It takes the
various layer sizes and weights from the neural network model as
inputs and produces a comprehensive hierarchical design netlist of
the analog crossbar array with all the peripherals in SPICE. Initially,
it calculates the hardware requirements necessary for implementing the model based on user-defined parameters such as synaptic
array size, PE size, and Tile size. Subsequently, the generator constructs the fundamental unit of the system—the synaptic crossbar
array—and incorporates the required peripherals into the design as
necessary. Following the creation of the synaptic crossbar array, the
design of the Processing Element (PE) is carried out, considering the
PE size specified in the user configuration. Tiles are then designed
using the number of PEs, considering the specified Tile size. The
individual synaptic arrays and PEs are interconnected using the
H-bridge method, ensuring efficient signal transmission and circuit
integration. The design generator offers several key features for
design space exploration:
3.2.1 Design Reconfigurability: The design generator produces designs in a modular fashion, offering high reconfigurability. Users can
switch between different RRAM models by introducing Verilog-A
or SPICE models of the device. The current implementation utilizes the fabricable 𝐻𝐹𝑂𝑥 RRAM model from the Skywater 130nm
process [29]. Users can also adjust the size of the synaptic crossbar array, selecting the number of rows and columns individually
to optimize cell utilization for neural networks with non-square
layer sizes. Furthermore, the number of synaptic arrays in a PE and
the number of PEs in a Tile can be adjusted using the respective
size parameters, leading to more optimized, robust, and error-free
designs for ACIM.
3.2.2 Synaptic Array Architecture: The unit synaptic array architecture within our framework is showcased in Fig. 1(c). Our design
primarily utilizes the 1T1R configuration, yet it allows for minimal
adjustments to accommodate other RRAM cell configurations such
as 2T1R or 2T2R. A state-of-the-art differential conductance mapping scheme has been adopted [30], where each synaptic link from
one layer (Layer A) to the subsequent layer (Layer B) is represented
by two columns of differential RRAM cells within the crossbar. This
organization allows mapping both positive and negative quantized
weight values into the RRAM crossbar.
The architecture includes all necessary peripheral circuits for
programming the conductance to the RRAM cells sequentially, such
as wordline (WL) and bitline (BL) decoders and drivers, and a source
line (SL) decoder and driver, which are automatically scaled with
the crossbar size. This design allows analog voltage inputs to be
directly fed into the input pins of the bitline decoder driver, which
employs an analog multiplexer (MUX) to select the desired signal.
The wordline decoder is digital, primarily used to select the active
1T1R cell, while the SL decoder can be utilized for on-chip training
scenarios.
During inference, there is no need for sequential cell selection;
instead, all WLs and BLs are activated simultaneously to perform
parallel multiplication operations and allow analog voltage inputs
to be directly fed into the input pins of the bitline decoder driver.
Additional peripheral circuits integrated into the design include
digital-to-analog converters (DACs), current-to-voltage converters,
subtractors, neuron circuits (ReLU), and analog-to-digital converters (ADCs). These components can be implemented via the circuit
design or Verilog-A, or alternatively, a software implementation
can be used depending on the specific requirements and constraints
of the simulation. Note that, complex functions such as softmax or
hyperbolic tangent are not implemented at the circuit level in the
current configuration.
3.3 Novel synaptic weight mapping
Our framework introduces a sophisticated weight mapping algorithm that utilizes the conductive filament thickness, 𝑇filament, of
Resistive Random Access Memory (RRAM) to efficiently simulate
the conductance mapping of neural network weights for SPICE
simulations. This approach does not entail real-time programming
of RRAM devices but rather uses the relationship between 𝑇filament
and conductance to streamline the simulation of large RRAM crossbar arrays during inference. By approximating the conductance
values through 𝑇filament, we significantly reduce the computational
complexity and enhance the feasibility of simulating large-scale
neuromorphic architectures in computationally intensive SPICE
environments. This method not only improves the efficiency of the
simulations but also allows for more manageable and scalable modeling of synaptic behaviors in neuromorphic computing systems.
3.3.1 Conductance Mapping Overview: The traditional method for
conductance mapping in RRAM-based crossbar arrays is defined
as:
𝐺
+
𝑖𝑗 − 𝐺
−
𝑖𝑗 = Δ𝐺 · 𝑤ˆ𝑖𝑗
where 𝐺
+
𝑖𝑗 −𝐺
−
𝑖𝑗 represents the conductance difference proportional
to the signed quantized weight. The constant Δ𝐺 is determined by:
Δ𝐺 =
𝐺max − 𝐺min
𝐿 − 1
Here, 𝐿 represents the total quantization levels, for instance, 256
for weights quantized to 8 bits. This helps define the conductance
3.3.3 Practical Implications: This method simplifies the SPICE simulation process during inference by avoiding the time-consuming
write-verify method typically required for setting each RRAM’s
conductance. By approximating the conductance-based on 𝑇filament,
which correlates directly with the desired weights through a logarithmic relationship, the simulation becomes both accurate and
efficient under conditions of low read voltages. In Fig. 2, we show
that for a read voltage around V(TE,BE)=0.7V, the error minimum.
Hence, we chose our read voltage for the selected RRAM model
to be 0.7V throughout our design and evaluation process. This approach effectively bridges the computational requirements with
the physical properties of the RRAM devices, maintaining accuracy
while enhancing simulation efficiency.
Algorithm 2 Hardware Software Co-simulation Engine
Require: Layer weights directory 𝑊 , baseline file path 𝐵, simulation parameters {𝑅res,𝐶cap, 𝑄,𝐺max,𝐺min,𝑇min}
Ensure: Simulation results, Power consumption 𝑃, Latency metrics 𝜏, Inference accuracy 𝛼
1: for each layer 𝑙 sorted by dependency do
2: for all layers 𝑙 ∈ 𝐿 do
3: 𝑊𝑄 ← Quantize weights of 𝑙 with 𝑄 bits
4: 𝑇pos,𝑇neg ← MapWeights(𝑊𝑄 , 𝐺max, 𝐺min, 𝑇min)
5: WeightMapping(𝑇pos, 𝑇neg, 𝑅res, 𝐶cap)
6: 𝐺+ ← Conductance array from 𝑇pos
7: 𝐺− ← Conductance array from 𝑇neg
8: if layer 𝑙 is the input layer then
9: Setup primary simulation for 𝐺+ and 𝐺−
10: Map primary inputs to simulation/ Map time multiplex inputs
11: RunSimulation(Spectre/HSPICE)
12: Repeat for 𝐺−
13: else
14: Setup simulation for subsequent layers using 𝐺+
and 𝐺−
15: Adjust inputs for non-primary layers
16: Repeat simulation steps for both 𝐺+ and 𝐺−
17: end if
18: end for
19: Store cycle time 𝑇cycle, Number of rows 𝑁𝑟
20: end for
21: Compute 𝑃, 𝜏, 𝛼
3.4 Spice-based Hardware-software
Co-simulation engine
In this segment of our proposed framework, we introduce a novel cosimulation engine to address the non-convergence issues associated
with SPICE simulations of large crossbar circuits. Furthermore, this
engine significantly reduces the simulation runtime, optimizing it
through a two-stage process:
a During Image Processing for Inference: the first stage
of optimization occurs during the processing of images for
inference. Here, we encode all the images subjected to inference into a time-multiplexed analog signal. This encoded
signal is then integrated into the simulation testbench file of
the simulation.
b During Simulation: The second stage of optimization is
implemented during the simulation itself. At this stage, we
introduce a "seed crossbar array," a predefined, optimized
array configuration that can be reused across multiple iterations over the full SPICE netlist. Since the DC iteration
of the SPICE simulation often causes convergence issues
for large circuits, reusing the seed crossbar can effectively
resolve the non-convergence issue while speeding up the
total simulation run time.
3.4.1 Inference data preparation: To validate the performance of
our proposed simulation framework, we used random images from
MNIST validation dataset. Each image is initially represented as a
28 × 28 pixel grid. If the input layer size is smaller, then we start
by resizing the image to fit the input layer of the model. We then
flatten the images and convert the two-dimensional pixel array
into a one-dimensional array that aligns with the network’s input layer, where each input neuron corresponds to an individual
pixel value. Next, the digital pixel values, which range from 0 to
255, undergo normalization and conversion into an analog voltage
range. Typically, these values are scaled to a range more conducive
to the operational parameters of our model, generally between 0
and the maximum Vread that doesn’t violate the approximation we
made during the weight mapping. The conversion can either be performed through software algorithms that simulate the function of
a Digital-to-Analog Converter (DAC) or by actually utilizing DACs
in a pre-simulation stage. Following the normalization process,
the analog voltages are encoded into a time-multiplexed fashion.
Time multiplexing arranges the signals for various images in a
sequential format over time, enabling the system to handle multiple signals sequentially within a single simulation run. Therefore,
we can achieve significantly reduced simulation time in terms of
per-inference operation.
Once all pixel values have been appropriately encoded into the
corresponding analog voltage values using the time-multiplexed
signal, the simulation environment is fully prepared to execute the
SPICE simulation.
3.4.2 Re-using seed crossbar simulation: After processing and generating the sources for the simulation testbench, we create a seed
crossbar netlist of size 𝑥 ×𝑦, as depicted in Fig. 1(e). This seed crossbar processes 𝑥 inputs from the total neural network model input
𝑁, and it generates testbenches by leveraging the time-multiplexed
signals created in the preceding step. The outputs of the seed crossbar are configured to handle 𝑦 outputs, representing a fraction of
the 𝑀 outputs from the output layer.
The runtime for a SPICE simulation of a crossbar of size 𝑆 can
generally be described by:
𝑇𝑆 = 𝐾
𝑆
where 𝑇𝑆 becomes non-convergent at 𝑆max, the point at which DC
operating point convergence is no longer achievable. In contrast,
our framework guarantees convergence with significant improvement in the total simulation time, calculated as:
𝑇𝑆 ≈
𝑁
𝑥
×
𝑀
𝑦
×𝑇𝑋𝑌 ×
1
𝑃
+ 𝑡loop
Here, 𝑇𝑋𝑌 denotes the simulation time for the seed crossbar circuit,
𝑃 is the speedup factor achieved through parallel or multicore
processing, and 𝑡loop is the loop delay for running each simulation
iteratively. Due to the distributed architecture of this framework,
employing parallel simulation and multicore batch processing can
further enhance the speed of the simulations.
The testbenches are dynamically created for both positive and
negative states by updating the 𝑇
+
filament and 𝑇
−
filament data, which
are then passed to the RRAM model in the 1T1R subcircuit of each
cell. Following setup, the framework initiates a transient simulation
using a SPICE simulator such as Cadence Spectre or Hspice. The
stop time of the transient simulation is determined by the number
of images as the total simulation time must satisfy all the timemultiplexed signals.
It is important to note that a transient simulation is essential
when employing a real RRAM model to precisely calculate hardwarelevel inference latency, dynamic power, and inference accuracy. As
the simulation progresses, it iterates over all synaptic arrays, Processing Elements (PEs), and Tiles. Upon completing the simulation
of one layer, it aggregates all partial sums of currents from the
waveform file of the transient simulation. If ReLU is not integrated
within the seed crossbar, it is applied at this stage (ReLU can be
implemented in both hardware and software). The next step involves taking the difference of the differential pair currents 𝐼
+ − 𝐼
−,
converting these back to the corresponding analog voltage, and if
necessary, adding an equivalent bias term. This processed output is
then used to simulate the synaptic arrays of the subsequent layer,
continuing with the same seed crossbar-based simulation iteration. This methodical approach ensures efficient management and
processing of large-scale SPICE simulation of ACIM architectures.
3.4.3 Result Collection and Processing: After simulating all the layers, the initial step involves calculating the actual output current by
subtracting the currents between the positive and negative arrays.
This current is then passed through a voltage converter and processed through a softmax function before being converted back to
8-bit digital data using Analog-to-Digital Converters (ADCs). The
ADCs can be integrated at the circuit level within the seed crossbar
array or implemented via software. Additionally, power consumption and latency metrics are retrieved for all synaptic arrays across
all layers from the waveform files. This data is essential for analyzing the performance and efficiency of the simulated neuromorphic
system.
The framework processes the final output data to perform inference on all the given input data. It also compiles a comprehensive
report detailing total power consumption (both dynamic and static),
average power consumption, energy usage, inference latency, and
hardware-level inference accuracy. We have implemented Algorithm 2 for the core management of iterative simulation using the
seed crossbar over the full spice netlist. Then it calculates and
returns the power, latency, and inference accuracy.
4 RESULT AND DISCUSSION
This section evaluates our framework using the MNIST dataset with
various Multi-Layer Perceptron (MLP) configurations. Cadence
Spectre, renowned for its accurate AMS simulations, was used as
the simulation engine. The simulations were executed on a cluster
node with 16 CPU cores and 64GB of memory, without the aid of
GPUs for deep learning frameworks or the SPICE simulator.
4.1 Simulation Speedup
Initially, our objective was to assess the speedup of simulation
times compared to traditional SPICE simulations, as elaborated in
Section 3.4. Fig. 3 illustrates the total simulation runtime across
different parameter sizes. We executed SPICE simulations for models encompassing more than 800,000 parameters. The red curve
in Fig. 3 represents the runtime for regular SPICE simulations under similar configuration settings. It was observed that regular
SPICE simulations failed to converge for model parameter sizes exceeding approximately 50,000. The largest model tested had 46,816
parameters and required 32 hours and 16 minutes to complete the
simulation. This increase in runtime is attributable to the simulation
engine’s need to determine all DC operating points of the circuit
extensively.
In contrast, our framework utilizes a seed crossbar of a specific
size to mitigate non-convergence issues. During our experiments,
we tested seed crossbar sizes of 16×16, 32×32, 64×64, and 128×128.
All simulations across various parameter sizes converged, thereby
eliminating scenarios of non-convergence. Notably, different seed
crossbar sizes optimized the simulation runtime for various model
parameter ranges. For instance, a 64 × 64 seed crossbar array was
most effective for model parameter sizes from 0 to 200,000, while
a 32 × 32 seed crossbar proved the most efficient beyond 200,000
parameters.
4.2 Inference Accuracy and Performance
Metrics
Fig. 4(a) displays the confusion matrix generated by TensorFlow for
the trained model on the MNIST dataset. Fig. 4(b) compares these
results with those obtained from our simulation framework, which
exhibited a 3.8% drop in accuracy compared to the TensorFlow
predictions. This discrepancy was likely due to the presence of particularly challenging images within the test dataset, especially those
representing the digit ‘7’, which contributed to misclassifications.
We can see that effect from the class-wise accuracy comparison between the software-based and simulation-based prediction depicted
in Fig. 5.
Fig. 6(b) reports the average power consumption for different
sizes of the crossbar array. Interestingly, for a specific set of inference images encoded during the simulation, the variations in power
consumption were minimal. Finally, Fig. 6(a) outlines the latency
measurements across nominal, worst, and best PVT corners using
a 130nm PDK. The latency trends observed align with the expected
PVT variations.
4.3 Integration into Architectural Simulation
The adaptations of the proposed framework within architectural
simulators, such as gem5 [31], demonstrate its potential to improve
system designs and facilitate design space exploration, particularly
for edge AI applications. By simulating ACIM with the proposed
framework in gem5 alongside traditional CPU and GPU architectures, we evaluated the performance of deep learning tasks using
the MNIST dataset. Table 2 shows the comparison of latency obtained for an external DNN accelerator for MNIST classification
workload from the gem5 for CPU and GPU and the integration
of our framework with gem5 that obtains the latency of ACIM.
The latency comparison of different accelerators highlights ACIM’s
superior performance, with CPUs and GPUs recording inference
times of 3.62465 × 105
𝜇𝑠 and 6.0005 × 105
𝜇𝑠 per image, respectively, while ACIM achieved an impressive 65.741𝜇𝑠 per image.
This substantial reduction in latency by ACIM, as compared to traditional architectures, underscores its efficiency and transformative
potential for rapid, on-device AI computations. Furthermore, the
proposed framework allows the simulation of eNVM-based accelerators within conventional systems prior to device fabrication and
system integration. This capability, absent in other circuit-level simulation frameworks for CIM, provides critical insights into system
performance and potential bottlenecks, thus aiding the development and optimization of next-generation compute-in-memory
architectures.
5 CONCLUSION
In this paper, we developed a SPICE-based framework for designing
and optimizing eNVM-based ACIM systems. First, we established
the necessity of utilizing SPICE for simulating ACIM, highlighting existing gaps in its application by designers and researchers
due to simulation bottlenecks. Next, we introduced our framework
that produces comprehensive SPICE-level designs for given DNN
models, incorporating a novel approach to map DNN weights to
the conductance of RRAM models, capturing all nonlinear device
characteristics. We also introduced a compact, efficient simulation
method using a seed crossbar array that iterates over the entire
netlist, accurately integrating SPICE simulations for large crossbar arrays ensuring convergence and reducing total simulation
runtime by 35×. As ACIM technology progresses, this framework
becomes an indispensable tool for advancing analog computing
with eNVM technologies, paving the way for more robust, efficient,
and compact AI devices targeting edge. Future work will focus on
further enhancing the framework’s capabilities to include more
complex AI models and extending its application to other types
of eNVMs. Moreover, we will streamline the integration of our
framework with architecture simulators for further comprehensive
system-level analysis.