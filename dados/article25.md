Title: SRAM Imprinting for System Protection and Differentiation

ABSTRACT
The foundation of trusted computation depends on the ability to
verify the authenticity of the underlying hardware. This need is
further compounded by the presence of counterfeit components
in the market, highlighting the necessity for pre-deployment and
run-time chip identification techniques. Current solutions involve
burning authentication information in physical fuses or creating
a unique mask for each integrated circuit, which are either costly
or susceptible to forgery. While many solutions have been proposed to prevent chip counterfeiting at design time, no accurate,
reference-free, and cost-effective solutions exist for chip buyers
to authenticate their purchases in the pre-deployment phase and
enable software-level verification at runtime. The lack of industrystandard authentication methods forces chip buyers to either adopt
expensive solutions, such as X-Ray imaging, or simply rely on blind
faith.
This paper presents SKU-RAM, a technique for chip identification
that allows manufacturers to embed their signature into integrated
circuits, provides per-device identification, and facilitates hardwareenforced time-limited licensing functionality. Our approach takes
advantage of the aging-induced power-on state changes in SRAM
to encode authentication data into an already fabricated device,
without modifying the mask of the chips. This hardware-overheadfree augmentation to the chips eliminates numerous instances of
chip counterfeiting and enables software-level authentication. We
demonstrate the effectiveness of SKU-RAM as a comprehensive
and scalable anti-counterfeiting solution for existing and future
computing devices using commercial off-the-shelf microcontrollers
and microprocessors and multi-year real-time experiments.
CCS CONCEPTS
• Security and privacy → Tamper-proof and tamper-resistant designs.
KEYWORDS
Chip authentication; anti-counterfeit framework; SRAM aging
1 INTRODUCTION
In 2021, the Wall Street Journal published an article titled, "What’s
Worse Than a Chip Shortage? Buying Fake Ones", which details the intensification of counterfeit-chip supply in the market [70].
This report, along with others [8, 36, 38, 53, 55], underscores the
threat posed by counterfeit computing devices to the reliability and
security of computing systems. The counterfeit chip problem morphed into a catastrophe fueled by the recent global chip shortage,
triggered by a confluence of the pandemic and geopolitical tensions.
As manufacturers struggle to cope with the increased demand, counterfeiters lure desperate chip buyers using numerous methods, e.g.,
advertisement through popular search engines [70] and injecting
a large number of chips into the distribution pipeline. The use of
untested, inferior-quality counterfeit chips can lead to system failures and compromise the safety, availability, and confidentiality
of critical systems, such as healthcare, automotive, infrastructure,
and defense [2, 7]. Therefore, effective, reference-free, and scalable
anti-counterfeiting solutions are essential to ensure the reliability
and security of computer systems.
The complexity and widespread nature of the supply chain,
which spans multiple countries, creates numerous entry points
for counterfeit chips [61]. Recycled chips, often extracted from discarded PCBs, are resold as new products, while cloned chips are
replicated at the manufacturing level and passed off as original
devices [1, 65]. Regardless of their origin, these counterfeit chips
are typically unreliable, untested, and of lower quality compared to
authentic products.
To ensure system integrity, it is essential to efficiently identify
each type of counterfeit with a unique solution that supports continuous post-deployment certification. To separate cloned chips
from authentic ones, designers can insert their signatures into the
hardware itself in a process called watermarking. Etching physically identifiable features into the IC layout is a way to watermark a
device, but it falls short in providing device-specific IDs and entails
costly and time-consuming analysis, such as X-ray imaging. To
address these limitations, the industry adopted fuse-based techniques to program constant and device-specific IDs into each IC
post-manufacturing. Unfortunately, fuses are area intense, especially considering the amount of information required by modern
ID use cases. At the other end of the spectrum, fingerprinting focuses on extracting a unique ID for each chip post-manufacturing
(commonly called a Physical Unclonable Function [15, 18]). Fingerprinting is convenient because it leverages readily available
ubiquitous on-chip hardware, but suffers from noise, requires enrollment, and does not support a constant ID across all chips. One
of the most popular device fingerprints leverages the power-on
state of SRAM memory as the device ID [24]. Device wear-out (i.e.,
aging) continually increases the noise in SRAM-based fingerprints
as the device is used, eventually destroying them [47, 49].
Previous work demonstrates potential solutions using Flash
cell’s aging behavior that remove the mutually exclusive nature
of device-specific database management and extra hardware components [45, 51, 66, 67]. These watermarking techniques exploit
Flash’s susceptibility to aging-induced degradation, allowing the
designer to burn the device’s ID (i.e., watermark) into the cell’s analog layer and eliminating the need to maintain records of individual
chips. Although effective, there are shortcomings to this approach.
First, these methods are inapplicable to most computing devices
as they generally do not contain embedded Flash memory, e.g.,
general-purpose processors. In other words, Flash-based methods
are applicable to either discrete memory chips or microcontrollers,
which brings us to the second shortcoming. Second, it requires
blocking an entire Flash section from typical software operations (to
avoid contamination), reducing available memory to these already
resource-constrained devices. Third, adversaries can inject errors
in the watermark in a matter of seconds through their own targeted
program/erase cycles.
The presented paper proposes a ubiquitous and resilient chip
identification method called SKU-RAM1
that utilizes an SRAM’s
power-on state changes induced by artificial aging. We show how
SRAM’s power-on state, coupled with its aging behavior, is capable of carrying a watermark2 where manufacturers have the
option to imprint manufacturer-, device-, and time-specific information. While SRAM’s power-on state has been used previously as
a PUF [25], our approach is fundamentally different as it involves
altering SRAM’s analog domain before deployment. Table 1 details
the advancement of our approach to existing SRAM PUFs. Our
proposed method eliminates many limitations of the state-of-theart watermarking [45, 51] and authentication methods [25]. For
example, exploiting aging-induced changes on SRAM’s power-on
state affords a flexible watermarking method where both crossdevice constant IDs and per-device IDs are possible and superior to
existing solutions. Lastly, we design and implement a “disappearing
watermark” that provides information on how long the device has
been deployed, which is useful for preventing recycled counterfeits
and as a way to include hardware-level time-limited functionality.
We test SKU-RAM on five different commercial microcontrollers
and microprocessors to demonstrate its broad applicability in preventing infiltration of the computing device supply chain. Results
from our experiments show that even after a year of recovery, the
accuracy of watermark extraction remains within 90% without any
error correction.
This paper’s technical contributions include:
• We demonstrate that by exploiting the aging-induced analog
properties of on-chip SRAM, Original Chip Manufacturers
(OCMs) can design a comprehensive chip authentication
scheme (§4).
1
SKU in SKU-RAM stands for Stock Keeping Unit.
2
In this paper, we employ the term "watermark" in a broad sense to describe a chip
identification data structure that encodes various fields and remains in the background
along with the system data
• We design a flexible watermarking method that contains
both variable and constant watermark components across
devices, leveraging aging-induced changes on the power-on
state (§5.3).
• We empirically show that watermark retrieval accuracy (not
error corrected) remains close to 90% even after one-year
recovery (§5.3.1).
• We eliminate the need for public record management (§5.3.1
and §5.3.2) and show that SKU-RAM is self-referenced as an
OCM needs to release only device-family-specific information
(§5).
• We show how OCMs deploy SKU-RAM at finished productlevel to provide a practical and effective method to control
available hardware features to users as a form of hardware
licensing (§5.3.3).
2 BACKGROUND
As the IC supply chain is complex and distributed, spanning countries and possibly many regulatory frameworks, counterfeiters inject fake/used chips at different stages, such as design, manufacturing, and distribution.
2.1 Counterfeit ICs
Broadly, counterfeit ICs are unauthorized parts that can be used,
remarked as higher performance grade, or clones of an original
device with substandard performance. The following list provides a
brief overview of the three major types of counterfeits discussed in
this paper (A detailed taxonomy can be found in this paper [20]):
• Cloned: These devices are fully or partially equivalent to
original devices but with inferior performance and lower
quality of services [12]. The cloning procedure involves
many steps, including reverse engineering an IC’s layout
and a subset of functional testing. Once duplicated, counterfeiters mark them with identical labels as their original
counterparts [50].
• Repackaged/remarked: Counterfeiters repackage or remark
ICs to portray them as new or of higher performance device,
for example, commercial grade chips remarked and sold as
automotive grade [10].
• Recycled: These types of counterfeit chips are genuine but
are salvaged from used systems, which leads to premature
failure when deployed. Counterfeiters inject recycled chips
into the supply chain as new, and these chips are difficult to
detect because they are genuine and functionally equivalent
to a new chip. Recycled ICs account for 80% of the total
counterfeit market due to their technically less intensive
collection process [10, 11].
Counterfeit detection/prevention challenges: At the buyer’s
end, numerous factors complicate a chip’s authentication process,
such as the functional equivalence, identical package and marking,
lack of tractability and proper documentation, and unavailability of
reference chips [37]. On the other side, an OCM needs to balance
the cost and profit associated with design modification as a measure
to mitigate counterfeiting. The current practice, which involves
storing various information in Flash memory during the enrollment phase [45], is convenient but leaves the stored information
vulnerable to erasure, forgery, or fabrication.
Detecting recycled chips commonly involves physically invasive
or semi-invasive testing methods, such as optical imaging, X-ray
tomography, and chemical composition analysis, as highlighted
in previous works [19, 52, 56]. These defense mechanisms have
numerous limitations, such as managing a central system, lack
of clear trusted channels between manufacturers and users, low
throughput, and expensive design and test processes.
2.2 SRAM’s Power-on State
At the core of a standard 6-T SRAM cell are two cross-coupled
inverters, which drive each other to create a positive feedback
circuit structure, as illustrated in Figure 1. This loop maintains a
logic state (Q) and its complement (∼Q). Transistors N3 and N4
facilitate access to these values. The row and column decoding
circuitry controls the state of these access transistors via the Word
Line, responding to read/write requests from processing cores.
At power-on, a hardware race condition between Inverter ○1 and
Inverter ○2 determines the startup logic state. While an SRAM cell
is symmetric by design (i.e., (𝑊 /𝐿)𝑃1 = (𝑊 /𝐿)𝑃2 and (𝑊 /𝐿)𝑁 1 =
(𝑊 /𝐿)𝑁 2), manufacturing process variation introduces mismatch3
between the inverters and biases a cell towards either 0 or 1. That
is, a mismatch between the inverters makes one inverter stronger
compared to the other one, leading to a faster transient response.
Starting from the OFF state, if node Q charges faster compared to
node ∼Q, the cell powers up into logic 1. As a result, one inverter
wins the hardware race condition, and the cell powers on into a logic
state (1 or 0); the cell’s bias towards a specific logic state depends
on the relative current driving strength of an inverter. The majority
of cells always power on into 1 or 0, and they never change across
power cycles; we refer to these cells as strong cells. Figure 2a plots
an SRAM’s mean cell bias across 100 trials, and Figure 2b illustrates
the spatial distribution of these biases. Approximately 20% of the
cells show weak bias across power cycles due to their symmetric
nature and sensitivity to operational noise, e.g., temperature. These
cells are uniformly distributed between strong 1 and 0.
2.3 Data-Directed SRAM Aging
When transistors operate, they undergo physical changes that are
reflected in their analog characteristics. Physical phenomena such
as Bias Temperature Instability (BTI) and Hot Carrier Injection
(HCI) gradually increase the threshold voltage (|𝑣𝑡ℎ |), which slows
down its switching speed [34, 54]. Transistor aging affects a cell’s
bias in data directed-way; for example, if we store logic 1 in the cell
(Figure 1), Inverter-○1 ) slows down due to the gradual increase (due
to NBTI) of the threshold voltage of its PMOS (P2). Given that NBTI
effect flips relative current driving strengths of Inverter-○1 and
Inverter-○2 , making |𝑣𝑡ℎ𝑃1
| < |𝑣𝑡ℎ𝑃2
|, this cell will start up into logic
0 from in future power cycles. Aging-induced degradation is a slow
process that may take decades to change an SRAM’s analog behavior,
but elevated voltage and temperature can accelerate it, enabling us to
imprint a watermark in the power-on state within hours.
3 SECURITY ASSUMPTIONS
Similar to previous work, our threat model considers the motivation to counterfeit ICs to be profit-driven and does not include
nation-state-level malicious actors with intentions to bring down
large systems by meticulous planning and planting of counterfeit
chips [13, 14, 45]. The chip distribution channel between the chip
manufacturer (OCM) and the user is untrusted. Counterfeiters recycle, clone, and remark ICs to take advantage of the opaque nature
of the complex distribution network to turn in a quick profit. To
incorporate manufacturing information and device-specific identification, OCMs include their information that is the same across devices in addition to a unique ID in every device. OCMs need a timekeeping functionality to allow chip buyers to verify a device’s age
before deployment and to provide post-deployment age-dependent
service. Figure 3 illustrates our threat model and a general overview
of our proposed defense scheme. For OCMs, the incentive behind
the adoption of SKU-RAM is warranty claims and making their
product more attractive to the buyers as their devices provide a
guarantee of authenticity. The cost and profit must not adversely
affect an OCM business model; therefore, we consider maintaining
public database listing devices, and their respective identification
is not a feasible option. The rationale behind this is the leaking of
confidential business information, for example, device production
rate and the total number of devices produced, to competing chip
producers [13].
The chip buyers or their representatives verify the origin, device
class, and age of an IC. Broadly, the authentication party attempts
to answer the following question using on-chip information and
chip specification sheet, i.e., datasheet.
• Does this chip belong to a particular chip manufacturer?
• Is the label in the package corresponding to the die inside?
• Is this chip new or salvaged from old and used PCB?
The security of SKU-RAM relies on the robustness of underlying
cryptographic protocols (e.g., digital signature) and the unidirectional aging behavior of SRAM’s constituent transistors. An attacker
may attempt a time-and cost-bound cloning of a legitimate device
by reading out the SKU-RAM and imprinting it into the illegitimate
devices. However, we consider technically intensive counterfeit
attempts such as decapsulation of chips to separate SRAM block
out of the threat model.
4 SKU-RAM DESIGN
SKU-RAM relies on controlling the symmetry of inverters (Figure 1)
such that it imprints an OCM’s signature in the hardware race condition, i.e., power-on state. Verification of this imprinted watermark
against publicly available information released by the OCMs is a
defense mechanism against counterfeit chip deployment. As we
discuss in Section 2, data, held in a cell during aging, affects the
symmetry of a cell. Provided that a cell is unbiased or moderately
biased toward a logic state, the cell’s power-on state permanently
shifts toward the complement of the data it holds during aging.
SKU-RAM design has two major parts:
(1) OCMs register a device through watermark generation and
imprinting (steps 1 and 2 in Figure 3).
(2) Chip buyers authenticate an IC’s watermark before system
integration (step 3 in Figure 3).
4.1 Authentication Data Structure Design
Our experiments confirm that an SRAM’s power-on state serves as a
blank slate, enabling the embedding of various types of information
in the watermark (§5). We categorize the watermark content into
two segments: (1) information consistent across devices, and (2)
information unique to each device. This dual-structure watermark
offers OCMs the advantage of not being restricted to embedding
only device-specific information. It also eliminates the need for
a centralized system for post-deployment authentication [13, 25,
27, 28]. That said, a comprehensive anti-counterfeiting solution
requires three unique types of identifiers:
• Manufacturing ID information (MID) contains manufacturing information (e.g., origin and batch information)
and an OCM’s digital signature. A portion of MID is constant across devices. The MID addresses the threat of cloned,
repackaged, and remarked counterfeit ICs.
• Device specific information (DID) captures the physical
unclonable properties of a device. A DID, signed by a manufacturer’s private key, eliminates cloning and remarking
counterfeit.
• Device’s age identification (TID) encodes a device’s age,
which we create by skewing the Hamming weight of an
SRAM’s typical power-on state (i.e., 50%/50% 1s and 0s) towards more 1s or more 0s. The skewed Hamming weight
of an SRAM block partially recovers and forms a device’s
manufacturing technology-dependent trend line. The authentication process uses this recovery trend to estimate
a device’s age. Time-dependent ID is self-referenced and
provides a finer-grain method to detect recycled counterfeit
chips.
The first step in the watermarking process is to design a data
structure containing the aforementioned IDs. We construct crossdevice constant part of the MID by concatenating manufacturing information (e.g., batch ID) and an OCM’s signature. The variable part
of the MID contains a device-specific digital signature generated using an OCM’s private key and the device’s DID, i.e., 𝑆𝑖𝑔𝑛𝐾𝑝𝑟 𝑖𝑣 (𝐷𝐼𝐷).
The DID derivation requires device-specific fingerprint extraction,
and there are numerous methods to uniquely identify a device
through inter-device analog property variations[18, 27, 44, 59, 60].
We incorporate SRAM’s power-on state as a source of unique device
fingerprinting (i.e., DID generation) as it is readily available in the
device and its ease of extraction during the watermark verification
phase [25].
Two temporally separated power-on states of an SRAM will have
an inevitable mismatch because of some cells’ weak bias toward
a state (i.e., 1 or 0). As discussed in Section 2, these cells are not
strongly biased toward any logic state, and their power-on state is
heavily influenced by a device’s operational noise (e.g., temperature
and voltage). Using a power-on state directly without countering
these naturally occurring device phenomena leads to unreliability
in the device authentication in the future [21]. Therefore, we select
a region in the SRAM for DID generation and reinforce the poweron state (i.e., DID) of that region by complementing (∼DID) and
aging. As mentioned before, the reinforcement is essential because
power-on state-based device fingerprinting is susceptible to stressand operation-induced noises, which increases false negatives in
post-deployment authentications. By stressing DID region with
its complement, we are essentially leveraging the SRAM aging
effect to reduce noise in the fingerprint extraction. Aging-induced
degradation contains both permanent and recoverable components,
leading to errors in the watermark. To counter errors introduced
due to aging recovery and operational noise, the watermark data
structure contains error correction codes (§5.4).
Next, we generate TID from an SRAM region by skewing the
typical 50/50 distribution of 1s and 0s by stressing the memory
block in a time-division multiplexed ratio of all-one and all-zero
patterns. This method allows an OCM to insert different TIDs for
different devices even if the total watermark imprinting time (i.e.,
aging time) of the devices remains the same. Longer time horizons
require a high proportion of time that 1s are held by SRAM to ensure
that the 0’s in the TID region are stronger. For example, stressing
a block of SRAM with 1s for 70% of the time and 0s for 30% of the
time creates skewed power-on distribution leaning towards more 0s.
Aging recovery gravitates the distribution towards its original state,
emulating an ‘odometer’ in silicon. Putting it all together, Figure 4
illustrates different IDs concatenated to form SKU-RAM that we
imprint in the power-on state.
4.2 Imprinting Authentication Data Structure
We develop an automation flow to imprint the watermark in a device, which is summarized in Algorithm ○1 . The executable binary
in Algorithm ○1 writes the watermark to a specific address range of
the device’s SRAM (Line 4). Aging-induced changes take decades to
manifest through a cell’s power-on state when it operates at nominal voltage and temperature; we increase the intensity using two
knobs. The first one is an elevated supply voltage that increases the
density of the vertical electric field in the transistor’s channel, which
ultimately facilitates more surface state generation at the gate oxide
region [48]. Operating temperature is the second knob that induces
more thermal stress (compared to nominal operating temperature),
increasing the intensity of aging-induced degradation [54]. We utilize these tuning methods to reduce the time required to imprint a
watermark within hours instead of decades. We elevate the device’s
operating conditions to 𝑉𝑎𝑐𝑐𝑒𝑙𝑒𝑟𝑎𝑡𝑖𝑜𝑛 and 𝑇𝑎𝑐𝑐𝑒𝑙𝑒𝑟𝑎𝑡𝑖𝑜𝑛 to begin the
accelerated aging process (Line 5). Note that the acceleration voltage and temperature are device-specific (§5). The MID and DID
components of the watermark undergo static aging while the TID
block periodically alternates between all ones and all zeros. That
is, we stress the TID block by alternating all-one (𝑇0 time) and
all-zero patterns (𝑇1 time) depending on the desired recovery rate
(Line 6-10). This process deviates the power-on states of the TID
block towards a specific Hamming weight (e.g., more 1s), and the
increased or decreased (depending on which direction we skew the
distribution) Hamming weight in the TID indicates the age of a
device. The total aging time depends on the fabrication technology
of a device; smaller technology nodes are more sensitive to aging
compared to older technology nodes (§6).
4.3 Post-deployment Authentication
The authentication involves mainly reading out the SRAM’s poweron state at startup and verifying the device’s signature using OCM’s
public ID and the DID. The signature verification steps complement the power-on state of the MID region because aging-induced
changes leave an inverted burn-in effect. OCMs need to release
information such as DID address range, Hamming Weight of TID,
and ECCs to an authenticating party. Once this information is available, SKU-RAM allows fully software-based authentication at any
point in the device’s life cycle. Note that the required information
to verify a chip’s origin and age is the same across devices, making
SKU-RAM a standalone and self-referenced authentication scheme.
5 EVALUATION
The authentication information must support verification of a device’s authenticity throughout its lifetime and must be resilient to
tampering. Our method relies on influencing a portion of SRAM’s
power-on state toward the value dictated by some string of information. We use accelerated and targeted aging as a means to achieve a
hardware overhead-free watermarking method that is impossible to
remove without expending significant time on each device—making
large-scale counterfeiting impractical. We investigate watermark
extraction accuracy and the effect of recovery on errors under a
device’s active and rest conditions. We also explore the efficacy of
different error correction methods to guide an OCM to select an
appropriate correction scheme for a desired accuracy level.
5.1 Evaluation Hardware and Software Setup
Figure 5 illustrates a block diagram capturing the major components of our evaluation platform that automates different tasks such
as imprinting and authentication, and Figure 6 shows the picture
of the implementation, including the evaluation chips. The test controller communicates with the target chip to synchronize power
cycling and to elevate 𝑉𝑑𝑑 to acceleration voltage. To allow variable voltage at the target supply line, we design a digital-to-analog
converter-based power supply system to control the device-specific
stress level digitally. The test controller communicates through the
debug interface of the target to load the required executable in its
non-volatile memory during the watermark imprinting phase; at
the watermark authentication phase, it samples the power-on state
through the device’s debug port. A Test Equity thermal chamber [62]
maintains the target temperature during the watermark imprinting phase. We induce thermal stress to a device by elevating the
operating temperature to 85◦𝐶, which is the maximum allowable
temperature for these commercial-grade devices.
SKU-RAM evaluation setup includes a set of five different commercial chips that range from low-power single-cycle microcontrollers to full-fledged microprocessors, covering a wide array of
device types (Table 2). The device datasheet and our experiments
guide the acceleration voltage selection for a particular device. As
SRAM’s aging-induced behavior is regular and predictable, we use
an MSP432P401R, unless otherwise specified, for most of our experiments to keep the results and discussions consistent.
Target-specific software allows the test controller to execute
various commands on different devices under test. The primary
function of the software running in the target device is to write the
watermark in its SRAM and busy wait during a stress period. While
the exact instruction sequence varies depending on the device, read-
/write access to a microcontroller’s (e.g., Cortex-M) SRAM is trivial
as we can use either a debugger or software stored in the Flash
to extract the watermark from the SRAM directly. SRAM access
of an application processor (e.g., Cortex-A) is different because in
most cases on-chip SRAM is a cache component, which is fully
transparent to the software. For Cortex-A72 SoCs, we introduce
firmware before the kernel loading step, which contains the watermark binary. This firmware enables the L1 cache and starts moving
the watermark data block from the RAM to CPU registers, storing
the watermark in the L1D cache transparently. The firmware executes the same instruction sequence for all four cores in the SoC to
calculate the average accuracy of the watermark imprinting. Since
the target chip is not executing any other process, the cores do not
evict the lines, which eliminates the non-deterministic behavior
of a typical cache. Reading the cache’s power-on state during the
authentication phase requires executing RAM index instructions
at El3 exception level. These instructions dump the disabled cache
contents in the RAM of the test platform (Raspberry Pi 4), which
is read by the test controller through the JTAG port of the SoC.
For example, the following code snippet moves the first set of the
L1 d-cache to x3 and x4 general-purpose registers in Cortex-A72
processors [29].
5.2 SRAM’s Aging Response
Stored data determines a cell’s future power-on state under aging
conditions. Aging sensitivity varies with manufacturing technology,
yet SRAMs exhibit a consistent aging response across different
devices (§5.3). We explore this phenomenon by writing all 0s to the
SRAM embedded in three commercial devices and exposing them
to accelerated, targeted aging. Figure 7 plots the gradual increase
in the number of 1s as the devices undergo stress. To explain the
aging effect, let us assume the cell in Figure 1 powers on to 0. We
consider the only mismatch between the inverters in the cell comes
from the threshold voltage difference between PMOS transistors
(i.e., |𝑣𝑡ℎ𝑝2
| > |𝑣𝑡ℎ𝑝1
| in this case). As we age this cell with 0, the
threshold voltage of P1 (|𝑣𝑡ℎ|) increases, making it slower. As a
result, the cell’s power-on state biases towards 1. The underlying
assumption is that aging with 0 in the cell flips the relative threshold
voltage difference (i.e., |𝑣𝑡ℎ𝑝2
| < |𝑣𝑡ℎ𝑝1
|). Prolonged device stress

reveals a diminishing rate of cells altering their power-on state,
adhering to a logarithmic trend. However, it’s important to note
that extreme aging does not always overcome the bias in transistor
pairs with significantly divergent threshold voltages.
We investigate whether an SRAM’s power-on state shows any
bias in the watermark imprinting process to a specific logic state.
That is, can we encode any logic state to a cell regardless of its initial manufacturing bias? To answer this, we run an experiment
with alternating patterns of 1s and 0s, which fills up 50% of the
SRAM with 0 and the other 50% with 1. Figure 8a is a 64 × 64 bit
snippet of this pattern. We pass this pattern as a watermark to the
process of SKU-RAM (§4). The captured power-on states at 2-hour
intervals shows the progression of the imprinting process (see Figure 8c, 8d, 8e). Figure 9 provides a whole-SRAM summary of the
power-on state changes at each interval. The number of 1s shifts
-44% in the portion of SRAM that contains 0 during stress, while
the number of 0s shifts +44% in the portion that contains 1. These
results show the inverted burn-in discussed in Section 4 as well
as suggest that the watermarking process is data-independent in
terms of the direction of change due to accelerated aging.
5.3 Evaluating Post-deployment Authentication
5.3.1 Manufacturing ID information: OCM identities and manufacturing metadata, including batch number, performance grade,
and manufacturing date, form this part of the watermark. This
combination of consistent inter-device information and a unique
digital signature for each device enables chip buyers to verify a
chip’s origin, regardless of the chip’s markings or the supplier’s
credibility.
Since MID contains information (e.g., signature) that needs to
be retrieved accurately to allow device authentication, we evaluate
information retrieval accuracy in our target devices. We create an
8KB data structure (to provide a large number of cells for analysis)
that contains MID information and generate target-specific binaries for the test devices. Then our evaluation platform programs
each target device with their respective binaries and execute the
watermarking flow (see Algorithm ○1 ).
We calculate the mismatch between the imprinted watermark
with the MID of each device and list it in Table 3. These metrics
contain only MID information4
and no error correction code. Stress
time, acceleration voltage, and temperature are the determinants of
the maximum achievable watermark extraction accuracy in each
device. Overall stress response and hence accuracy in the imprinted
MID depends on underlying devices’ fabrication technology nodes
and power delivery circuits.5 The aging time for all the devices is
within 24 hours.
While applying thermal stress is trivial using a typical thermal
chamber, elevating the voltage of embedded SRAM above nominal
requires special considerations. Simpler microcontrollers allow direct control of its supply voltage through 𝑉𝑑𝑑 pins. Complex SoCs,
however, require applying a voltage to the core/memory domain
pins instead of the supply voltage. These pins are exposed outside
of an IC packaging to connect to area-intensive passive electronic
components, e.g., capacitors, and inductors [4, 39].
ATSAML11E16A LPC55S69JBD100 MSP432 BCM2711
98% 88% 93% 93%
Table 3: MID extraction accuracy.
5.3.2 Device differentiation: As mentioned in Section 4, a unique
device ID allows chip buyers to authenticate every device before
deployment. SKU-RAM facilitates such functionality by signing a
device’s unique ID using an OCM’s signature, which a chip buyer
verifies using the device family specification sheets (i.e., datasheet)
released from the manufacturer. Our method implements DID using
SRAM’s power-on state as it is unique to every device [25].
Typical power-on state-based device fingerprinting is unreliable
due to its susceptibility to operational noise and aging. We counter
such effects by using accelerated, targeted aging as a PUF reinforcement mechanism. DID reinforcement is based on the same
principle as watermark imprinting: aging a cell with its complement
power-on state to reinforce it. We derive a device’s baseline DID
(4KB string length) by applying majority voting on 101 trials of
its power-on state. We use the majority value for each bit as the
device’s baseline DID. This baseline DID is then used for comparison between instantaneous DIDs, both with and without SKU-RAM
reinforcement. Next, we sample the instantaneous DID value of the
device 100 times both before and after reinforcement to calculate
the mismatch (noisy bits) between the baseline DID and these two
groups of 100 trials. These results (supported by previous work [17])
form a metric reflecting the unreliability of power-on-state-based
SRAM fingerprinting. We plot the pre-age and post-age mismatch
(after recovery) in Figure 10. Without reinforcement, the mean error
among mismatches when DID is read is 1.8%. Reinforcement brings
down the error to 0.2%—even after one year of recovery (All of our
stress and recovery data are collected in real time). Generally, a
digital signature fails to verify noisy information, and therefore,
we need an error correction code to reconstruct the DID before
authentication (§5.4).
5.3.3 Device’s functional age identification: SRAM poweron state reveals a device’s age because threshold voltage (magnitude) increases as we use them, which manifests through the
change in the cell’s bias. This idea led to many recycled chip detection schemes, including both device enrollment-based [22] and
enrollment-free [21] methods. Enrollment-based methods keep a
record of an SRAM’s power-on state and compare that with device
under test during the authentication phase to detect whether it falls
in a recycled or new category. Since SRAM power-on state carries a unique device fingerprint, maintaining this information in a
database and allowing users to verify a device’s age. The limitation
of these methods is that OCM needs to maintain a database for
every device throughout their expected lifetime and must respond
to the query from a chip authentication party (i.e., chip buyers). To
eliminate the need for extensive database maintenance, researchers
developed recycled component detection methods that exploit software’s natural bias toward storing more zeros in the memory compared to ones [21, 68]. This phenomenon skews the distribution
of the SRAM’s power-on state bias toward more ones over time,
which serves as a device’s age indicator [21]. The classification
performance of these methods is poor because of the overlapping
distribution of new and aged chips’ power-on state bias [68].
Instead, SKU-RAM keeps track of a device’s age using the aging
recovery of an SRAM, which eliminates the need to maintain a
device-specific database, and at the same time, provides higher
accuracy by comparing the devices to themselves rather than a
distribution. Hamming weight of an SRAM’s power-on state is
approximately 1
2
×𝑙𝑒𝑛𝑔𝑡ℎ(𝑆𝑅𝐴𝑀 𝑏𝑙𝑜𝑐𝑘), for example, the Hamming
weight of a 2Kbit block is ≈ 1024. SKU-RAM systematically deviates
the Hamming weight of a block (power-on state of spatially adjacent
SRAM cells) and observes its recovery towards its typical Hamming
weight, i.e., 1
2
× 𝑙𝑒𝑛𝑔𝑡ℎ(𝑆𝑅𝐴𝑀 𝑏𝑙𝑜𝑐𝑘). To illustrate this concept,
we store all 1s in three 2048-bit blocks of two MSP432 devices
and expose them to an accelerated watermarking process for 2
hours, which reduces the Hamming weights of these blocks by
60% due to data-directed SRAM aging effect on their power-on
state. Table 4 lists the Hamming weights of the blocks for both the
chips; here 𝐻𝑢 is the Hamming weight of an unstressed device. The
collective response of SRAM cells due to the same stress shows
similar behavior within a device’s family, which is due to the same
fabrication technology nodes and the same transistor placements
across devices. We verify this observation with another class of
device: MSP430. Same as MSP432 chips, we write all 1s to its 4Kbit
SRAM block and expose four chips to accelerated stress for seven
days (see Table 2 for accelerated aging condition). Then we sample
the power-on state of each chip and let them recover naturally for
two years. The graphs in Figure 11a show that the change due to
stress remains the same across devices.
To evaluate TID and its efficacy in more fine-grain time stamps,
we create a 10-chip baseline of the MSP432 chips’ power-on states.
Then, we expose a chip to accelerated states after writing all 1s in
its 2048-block SRAM for 10 hours and let it recover for one year. We
collect the power-on state of this device in weekly intervals; initially,
the data collection frequency is higher because of the faster recovery
rate in the beginning. According to our previous observation, the
Hamming weight shift remains the same across devices within the
same class of device. So we add the observed chip’s Hamming
weight change at different stages of aging and recovery to the
baseline chips. In Figure 11b, we plot the Hamming weight trend
line along with the ±3𝜎 lines. Given 𝐻𝑇 is the Hamming weight of a
TID block, an authentication party estimates a device’s age from this
trend line. However, due to process variation, the Hamming weight
shows overlapping distribution; we illustrate this phenomenon
using Figure 12. We generate 1000 samples of virtual chips with
the same statistical properties as the 10-baseline chip and plot two
distributions at two different timestamps: one-month-old and sixmonth-old. Clearly, recycled IC tests for age >1 month from these
two distributions will lead to a large number of false negatives (i.e.,
6-month-old ICs getting classified as 1-month-old).
To improve separability between the chips in two different time
stamps after watermarking, we incorporate the initial Hamming
weight of each device into the recycled IC classification. Incorporating device-specific information into the classification process
eliminates the need for probabilistic age estimation because we
are comparing the device to itself instead of the distribution of
chips. Previous experiments (see Figure 9 and 11b) guide us to find
a trend line, transforming a classification problem into a non-linear
regression problem. We fit a non-linear curve (logarithmic) using
sampled Hamming weights of a TID block at different timestamps
(see Figure 13), and this line characterizes the recovery trend of
MSP432 chips. Considering the Hamming weight of a TID block
right after the watermarking phase is 𝐻0, a device’s age (𝑇 ) becomes
𝐻𝑇 as 𝐻𝑇 = 𝑘×𝑙𝑜𝑔10 (𝑇 ) +𝐻0, where 𝐻𝑇 and 𝑘 are Hamming weight
of a TID block and slope of the TID recovery curve, respectively. As
mentioned before, aging in SRAM cells is regular and predictable.
Therefore, the slope and the intercept of this recovery line for a
device family allow a chip buyer to estimate a device’s age. The
intercept 𝐻0 varies across devices because of their initial bias variations introduced at manufacturing time. SKU-RAM design allows us
to calculate this value from the DID as it is essentially a reinforced
power-on state of a particular device. That is, 𝐻0 for an SRAM
Δ𝐻 = 𝐻𝑢 − 𝐻0, where 𝐻𝑢 is the Hamming weight of DID (initial
Hamming weight of an SRAM TID block before exposure to stress)
and Δ𝐻 is the difference between Hamming weights before and
after watermarking a device. Note that the length of 𝐻𝑢 must be
equal to the TID block. Putting it all together, a recovery curve
characterized by a set of parameters, {𝑘, Δ𝐻 }, expresses a device’s
age 𝑇 and separates chips from overlapping distributions between
two timestamps.
5.4 Assessing Errors
The potential sources of error in the imprinted watermark need to
be accounted for before enrolling and deploying a device. The error
in the watermark primarily comes from the inability of aging to
influence the power-on states of every cell in an SRAM array. Some
cells’ power-on states are extremely biased towards a logic state,
which aging fails to flip within a reasonable stress time, introducing
error in the post-deployment watermark extraction. The enrollmenttime error increases logarithmically as a device recovers from aging,
and so this error needs to be in the modeling of an error correction
code.
5.4.1 Extreme bias condition: While most cells respond to aging (>90%), some cells retain their initial power-on state even after
long stress time, leading to errors in the watermark. The reason is
manufacturing variation among transistors which follows a normal distribution.6
In some cells’ manufacturing variations are so
extreme that it could lead to a large mismatch between inverters’
analog properties, such as threshold voltage. That is, the cells that
fall in the tails of the distribution are highly skewed toward a logic
state. Reversing this asymmetry demands stressing a device for a
long time under extreme aging conditions, which may be impractical considering time-to-market and the device’s life span. As we
illustrate in Figure 7, the aging effect saturates over time with an
asymptote determined by the manufacturing technology node of
a device, which means a device’s technology node and maximum
allowable acceleration set an error’s lower bound.
5.4.2 Natural recovery: The aging effect partially recovers when
transistors are stress-free (i.e., 𝑉𝑔𝑠 > 0), which introduces the error
rate in watermark extraction. OCMs needs to consider natural
recovery because time to deployment varies chip-to-chip; some chips
will start operating within a few days of manufacturing while other
might sit in warehouses for a few months. We study how natural
recovery affects SKU-RAM error rate using an MID imprinted device.
Figure 14 plots the recovery graph (passive) normalized by the initial
error in the watermark. The error flattens out as time progresses
and remains within 12% after one year of recovery.
5.4.3 Recovery during regular operation: The fact that SKURAM imprints information in SRAM’s analog domain means that
the system’s data can co-exist in the same cell but in the digital domain. That is, SKU-RAM demands no reserved-memory in a system.
To study how software affects the error of an imprinted watermark,
we write a random number generator using a 32-bit linear feedback
shift register seeded by a linear congruential generator (This is a
random number generator used in glibc). Seeds generated through
these methods reduce the likelihood of repeating the same number when we run the experiment for months. The random number
generator continuously overwrites the SRAM states to emulate
neutral (i.e., not biased towards any specific logic state) software
operation. Figure 14 illustrates the change in error as we keep it
operational for ten months. We observe that this form of “active”
recovery essentially reinforces the aging effect of SKU-RAM and
that the level of threshold voltage change due to aging does not
impact this recovery modality.
5.5 Improving Accuracy
Watermark extraction accuracy improves with increased exposure
to the stress conditions of accelerated aging. As discussed in Section 2, the stress-induced changes to SRAM’s analog domain properties (namely, threshold voltage) follow a logarithmic relation with
time. Embedding ECCs within the signatures shortens this required
time to achieve a desired level of accuracy. In an MSP432 device, 2
hours of stress produces 20.85% error in the watermark extraction,
and the error reduces to 0.36% when we consider a group of 7-bit as
a 1-bit watermark (7 copies). This is Hamming(n,1) ECC where the
data bit is repeated n times to correct 1 data bit. We apply this ECC
in SKU-RAM to bring down the error percentage before applying a
comparatively high code rate ECC. Using repetition codes and other
error-correcting techniques is viable for SRAM-based watermarks,
because the watermark is relatively small compared to the available
SRAM cells in SoCs, and because SKU-RAM only alters the analog
domain, no SRAM needs to be reserved. We plot the effect of error
reduction in Figure 15. Using ECC with a relatively higher code
rate reduces the memory requirement for a specific target accuracy,
which is not possible to achieve using only Hamming(n,1). We plot
an SRAM’s watermark extraction accuracy when Hamming(7,4) is
used on top of repetition codes.
5.6 Comparing Performance with Flash-based
Methods
SKU-RAM is a standalone, transistor aging-based, resilient, and
hardware overhead-free anti-counterfeit method that allows fast
verification without additional expensive test equipment, such as
imaging devices. The closest related work of SKU-RAM is Flashmark [45]. This section provides qualitative and quantitative performance comparisons with existing methods.
The most prominent advantage of SKU-RAM over Flashmark is
its versatility; SKU-RAM solves a wide array of counterfeits, including recycled IC. In addition, it covers a broader range of devices
compared to Flashmark as SKU-RAM uses a ubiquitous memory
technology, SRAM, which makes it implementable in almost all
computing devices.
SKU-RAM does not restrict software from writing in the watermarked cells, which allows OCMs to utilize the entire SRAM for
watermarking purposes. The flash-based method needs a more significant number of replicas to achieve a similar level of accuracy as
SKU-RAM; a 40K-program/erase cycle watermarking produces a 5.2
% error with three copies of the watermark [45], while SKU-RAM
achieves 2.7% with a single copy of the watermark. It is essential
to achieve higher information density in watermarking because in
embedded systems (i.e., microcontrollers), both memory types are
in limited quantity. The availability of the entire SRAM allows us
to employ lower code rates but higher accuracy error correction
methods, leading to lower error and shorter watermarking time.
We provide a qualitative summary of SKU-RAM’s performance
in Table 5, highlighting its advantages over existing methods in
terms of scalability, ubiquity, and broad applicability to similar
anti-counterfeit methods.
5.7 Security Robustness against Cloning
SKU-RAM provides a robust security guarantee against cloning;
two main technical aspects of our proposed system facilitate this.
First, SKU-RAM has a much tighter error level in its DID because
this component is derived from the intrinsic device property, i.e.,
power-on state. Therefore, an attacker needs to bring down the
error of a counterfeit device at the DID-error level to be corrected
by the embedded ECC. If counterfeiters imprint an authentic watermark on another device, the expected error will be at the same level
as the MID error, which is much higher than the DID error. As we
can see in Figure 16a, an attacker’s effort exponentially increases
as they try to get close to a perfect match to a legitimate DID. This
is true because, at this point, they are imprinting a random binary
string—instead of reinforcing an intrinsic SRAM PUF, leading to
a relatively higher error rate (2% to 10% without ECC). The embedded error correction needs to handle this significant error in
the cloned and deployed DID. To provide a more concrete example,
1024-bit DID with Hamming(7,4) authenticates a device because
the error stays within 0.2% across DID sampling in MSP432 devices.
Given that adversaries achieve MID-level accuracy (i.e., 7% error in
MSP432 device) on cloning DID into another device, a counterfeit
device will still contain errors in the DID after applying ECC. We
simulate this condition by introducing 7% random error in the DID
codeword {DID, ECC}, and apply the ECC to observe the noise that
needs to be corrected in a cloned device. When ECC is applied, the
error reduces from 7% to 3.2%, which means the correct DID can be
any ID at ≈ 32 Hamming distance away from the noisy DID. That
is, the perfectly cloned ID is one out of approximately
1024
32

≈ 2
201
possibilities.
Even if an attacker achieves a similar error level to an intrinsic
DID, recovery prevents a cloned device from being authenticated
once sold. Figure 16b shows that as a device waits for deployment,
the DID recovery stays the same for months showing no significant
error increase, but a cloned device DID quickly moves away (3%
drop in the match within a week). Therefore, an attempt to authenticate a cloned device fails because a DID’s ECC is unable to correct
10x higher error level. Second, the time-dependent component of
the SKU-RAM, i.e., TID, relies on how constituent transistors recover from stress. An advanced node (e.g., 14nm) has a radically
different aging response compared to a counterfeit off-node device (see Figure 13). Matching reinforced DID and TID both would
require significant time (weeks of aging) and expense (fabricating at the same node) which are antithetical to typical large-scale
counterfeiting.
6 DISCUSSION
6.1 An Example Self-authentication Scheme
We show how SKU-RAM is implementable in a low-cost system that
allows maintenance-free self-hosted watermark verification using
popular SoC used in many devices. This implementation employs
the ARM Trust Zone (TZ) as a hardware-backed memory protection
mechanism, enabling startup self-authentication and verification.
ARM-TZ and SKU-RAM form a duo to facilitate hardware licensing by the equipment manufacturer and strengthen the watermark security. In addition, hardware-enforced memory isolation
reduces the impact of recovery on the watermark through softwarecontrolled watermark reinforcement. ARM-TZ creates two execution states called Secure and Normal Worlds; software in Normal
World cannot access memory marked as secure or lower exception
level. We implement SKU-RAM in the Raspberry Pi 4, a Cortex-A72
device, and select a 1KB signature string as the 𝑀𝐼𝐷, 𝐷𝐼𝐷, and
𝑇𝐼𝐷. Then we execute Algorithm ○1 for a total of 24 hours. Since
this is a self-authentication mechanism, the boot software contains
a few utility functions (e.g., ECC and signature verification) and
data structures containing OCM-released public information (§4).
This implementation uses a Hamming(27,1) code to recover the
watermark fully7
. The boot flow starts at the EL3 exception level
and dumps the d-cache contents into the RAM before enabling the
caches for general software usage. In addition, it performs error
correction on the dumped cache content before executing signature verification; Listing 2 provides the flow of the firmware. This
self-authentication firmware and the watermark-imprinted SRAM
region lie in the processor’s secure state. This measure provides
extra protection for the watermark; tampering with the watermark
requires reverse aging of a memory area, bypassing the secure boot
flow that authenticates the cache’s power-on state. If the verification
passes, the authentication software complements the watermark
(when specific cache lines are not being actively used by the system) to reinforce it, which prevents recovery of the aging effect and
increases watermark fidelity. The processor reduces its execution
state to a lower level (e.g., EL2 or EL1) and allows access to resources
(e.g., cryptographic accelerator) as per the licensing agreement; a
failure halts the boot process, and the processor stays in the higher
exception level (i.e., EL3). The combination of hardware-backed
secure boot flow and SKU-RAM guarantees a verifiable authenticity
of a device even under this extreme threat model.

6.2 SKU-RAM Cost Assessment
OCMs run numerous tests on every chip before distributing them;
the set of tests includes structural, functional, and burn-in tests,
among many others. A chip burn-in [63] and system level test [57]
can run for many hours [9] are standard tests to assess a device’s
reliability, latent defects, unpredictable soft error, and infant mortality [5, 43]. These tests’ environments are the same as the SKU-RAM
testing setup that includes voltage manipulation in the core and
system-level software execution. In addition, SKU-RAM is fully
scalable because once loaded with the data structure (§4), chips
undergo the imprinting process automatically without external
intervention. To provide a heating cost estimation, our thermal
chamber (2.5 cubic feet & 1KW) costs <$0.24 in a 2-hour operation.
The chamber watermarks >100 MSP430 ICs ($2.5 each) at a time,
costing <$0.0024/chip.
6.3 Generality of SKU-RAM
The imprinting time for SKU-RAM’s data structure depends on
the device’s manufacturing technology node and the design of its
internal power delivery network. Newer technology nodes are more
sensitive to stress, which reduces the time required to imprint data
with the desired accuracy. For instance, stressing a 130nm MSP430
( [40]) for 160 hours changes the power-on state of 21% of its strong
SRAM cells. In contrast, for more recent devices like the MSP432
and ATSAML11E16 chips, 82% and 54% of strong cells flip within
less than 17 hours, respectively, showing significant reduction in
the imprinting time. Provided the SRAM circuit structure and power
delivery network remain consistent, SKU-RAM can be adapted to
other devices as well.
7 RELATED WORK
The demand for end-to-end transparency in the increasingly complex supply chain propels a significant research drive in the counterfeit detection and avoidance landscape. Yet, the traceability of
a chip’s origin remains an undeniable concern in terms of both
reliability and security.
Aging-based anti-counterfeit methods: Wang et al. lay the
foundation for exploring a Flash cell’s aging behavior and demonstrate its multifarious applications in the design of security primitives, including random number generation, fingerprinting [66], and
data hiding [67]. Flashmark [45] and Flash watermark [51] extend
the idea and show that Flash cell aging is exploitable to watermark
Flash memory devices, such as SSD. These counterfeit Flash detection methods utilize the stress-induced change to the program/erase
(PE) time of the Flash cells; repeated PE cycles (stress) degrade the
timing behavior of a Flash cell. The programming time increases as
it goes through thousands of PE cycles, and exploiting this analog
characteristic allows OCMs to encode information in a Flash cell.
Watermark ReRAM uses the timing degradation of ReRAM cells
to provide an anti-counterfeiting method for new and emerging
persistent memory technology [14]. Similar to the Flash memory
cell’s program/erase time, a ReRAM cell’s write time increases as
a device undergoes a repeated set/rest phase. While effective for
respective memory device tracing, these methods are inapplicable
to the counterfeit chips without embedded Flash or ReRAM, e.g.,
general, purpose processors.
Fingerprinting-based on physical variations: The flow of
current through conductors inside of a chip emits electromagnetic
signals that are unique to the chip due to intra-device physical
variations in the conductive paths. Huang et al. show how electromagnetic signals emitted from ICs carry unique signatures, and
then design a counterfeit detection method based on electromagnetic signal emission [30]. EMFORCED applies a similar idea to
target specifically remarked and cloned chips [58]. Exploiting the
same physical property, i.e., electromagnetic emission, Balasch et
al. fingerprint ICs to detect malicious hardware implants, known
as Trojans [6]. Using Quantum Diamond Microscope, Turner et al.
empirically show that ICs even radiate unique magnetic field [64],
which is another way to fingerprint chips. These methods are lowthroughput and expensive to implement.
Physical Unclonable Function (PUF) emerged as a device identification technique using silicon property instead of storing a secret
key in EEPROM [23]. Exploiting process variation (silicon variation)
that manifests through the power-on state, researchers developed
SRAM-based device fingerprinting methods [24–26]. SRAM poweron state-based methods suffer from operational noise due to the
random nature of the weak cells and aging effects. CounterFOIL is
an inexpensive and robust solution that fingerprints the naturally
occurring variation in the IC packaging [13]. While these methods provide high throughput solutions, the chip buyers need to
communicate with the chip manufacturer for device-specific IDs.
Recycled IC detection: The recycled integrated circuit takes up
a large share in the counterfeit market [73], which led to the development of dedicated used chip detection and prevention schemes.
A set of methods implement hardware measures to detect a device’s
functional age; these are known as designs for anti-counterfeit.
The variety of these sensor structures ranges from simple counting
and storing a device’s run-time [3, 35] to using differential circuit
structure for time keeping [69, 71]. Another set of methods analyzes the statistical properties of different device parameters to
draw a classification boundary between used and new ICs [16].
Path delay is one such parameter that reveals a device’s functional
age because of the aging-induced degradation of the transistors in
the path (also other effects such as electromigration). For example,
by fingerprinting the delays of new ICs and creating a distribution, we can predict (with certain statistical confidence) a device’s
age [72]. Researchers applied different statistical analyses such
as support vector machines [31] to detect recycled components.
While design for anti-counterfeiting requires design modification,
aging-sensorless methods lead to less accurate classification due to
process variation and lack of reference.
8 CONCLUSION
Chips are designed to be the same, but allowing systems to uniquely
identify underlying circuits ensures establishing a chain of trust
beginning in authentic hardware and eliminates the threat of counterfeit chips circulating in the supply chain. Encoding manufacturer identification, unique device ID, and temporal functionality
management (as a form of hardware licensing) require hardware
modification. This paper shows how using existing SRAM, along
with its aging behavior, allows computing device manufacturers
to encode their signatures into the devices while also facilitating
a mechanism to encode per-device identification and time-based
signatures. We evaluate our system, SKU-RAM, using five state-ofthe-art commercial devices for imprinting and extraction efficacy,
aging time, recovery impact, and error reduction strategies. Our
results reveal SKU-RAM is >90% accurate in watermark imprinting and extraction after only moderate aging. Broadly, SKU-RAM
allows seamless integration to pre- and post-manufactured future
chips, closing the long-standing gap between counterfeit detection
and counterfeit avoidance.