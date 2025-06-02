Title: An Extensive Overview of Inductive Charging Technologies for Stationary and In-Motion Electric Vehicles

ABSTRACT The wireless power transfer (WPT) system holds potential as a viable solution for charging
electric vehicles (EVs) owing to its benefits including safety, automated operation, efficiency, and simplicity.
Among the WPT technologies, inductive power transfer (IPT) stands out as particularly well-suited for
charging EV batteries. This is primarily due to its capability to transmit high power across considerable
air gap distances, accommodating the ground clearance requirements of most EVs, operating automatically
without driver involvement, ensuring safety and convenience even in challenging conditions such as snow,
rain, and dust, and offering maintenance-free operation by eliminating the need for plug-in connections.
This manuscript provides a comprehensive exploration and analysis of the progress made in IPT technology.
The manuscript introduces the operational principle of the IPT system and highlights the benefits of its
components. Additionally, it discusses the transmitter and receiver architectures, outlines the characteristics
of various charging pads, in case of both stationary and in-motion charging scenarios. Furthermore, it delves
into different compensation circuit topologies and various WPT designs based on compensating structures
associated with the IPT system. It also categorizes the converter topologies utilized in the system and
presents the operating technique for each one. In addition, the ongoing research and development (R&D)
endeavors pertaining to each technology are discussed, addressing challenges, existing gaps, and offering
recommendations for further advancements in both stationary and in-motion charging applications.
INDEX TERMS Review, IPT technology, R&D activities, compensation networks, control, challenges,
opportunities.
I. INTRODUCTION
In recent decades, transportation sector comes as one of the
main sources of harmful emissions and greenhouse gases
(GHG). It mainly depends on fossil fuels, such as petroleum,
which are non-permanent sources of energy and likely to be
depleted over time. There is an urgent need to electrify our
transportation sector by promoting electric vehicles (EVs).
Electric vehicles will not only assist to reduce reliance
on fossil fuels, but will also lower the amount of energy
consumed in transportation since electric drive systems are
more efficient than internal combustion engines. These two
items will help to reduce GHG emissions from transportation
sector. Mass deployment of EV realizes challenges, such as
driving range anxiety, long charging time, and infrastructure
readiness.
There are three strategies for EV battery charging [1];
Wireless (stationary and in-motion), plug-in, and replacing
batteries charging. In case of charging by replacing batteries,
empty EV battery is exchanged with a charged one, which
usually takes less than five minute leading to recharging
process similar to gas station [2]. This model provides
flexibility in charging time, where the charging process can
be scheduled during off-peak periods. Despite the advantages
offered by this method, the system cost, battery lifetime,
swapping difficulties due to battery heavy weight, battery
damage due to human misuse, and applicability of this system
are still questioned and researched [2]. The second way
for EV charging is using conductive (plug-in) technology,
whether during long-term parking using AC Level 1 (L1)
and 2 (L2) or opportunistic charging at DC fast charging
stations. This approach offers appropriate option in terms
of cost, efficiency, and reliability, and it is more convenient
for passenger cars, especially those who have access to L1
or L2 charger at home or at workplace. Plug-in charging is
relatively slow compared to gas station model, which may
take from 20 minutes to 30 hours [3]. Also, it is a manual
process and it becomes challenge to deal with heavy-duty
cables at fast and extreme fast charging stations. Additionally,
charging cables and plugs introduce safety concerns at public
stations during harsh environment, such as heavy snow and
rain.
The other way of charging an EV is to use the WPT
strategy, that enables the battery of EV to be recharged
wirelessly without the need for a wired connection. This
technology offers a flexible solution that can charge EV
when parked for an extended period of time (stationary
charging), temporary halts (opportunistic or quasi-dynamic
charging), and driving at high speed (dynamic or in-motion
charging) [4]. Also, it can be installed at private garages
for overnight charging, public parking, street parking, bus
stops, or in the roads. WPT technology is automatic by
nature, which makes it an ideal solution for charging selfdriving cars. Additionally, the removal of cables makes it
safer and more reliable in harsh environment and extreme
weather conditions [5]. However, like other technologies,
WPT systems faces challenges related to loss of efficiency
due to misalignment, high unit and installation cost, and
complexity in design, manufacturing, and integration.
The first spark of WPT technology may be dated back to
the late of 18th century, when Hertz was trying to spread
waves in form of electromagnetic field in air using a spark
gap [6], [7]. Nicola Tesla examined the ability of radio waves
to transport electric power through air in 1890. Between
1894 and 1918, he constructed an enormous coil attached
with a ball made of copper and put it on the top of a turret. This
system can be utilized for WPT by electrostatic induction [8].
In 1960, a WPT system was proposed by William Brown
and tested to transport sunlight energy in space for use in
powering spacecraft [8]. Between 2007 and 2013, a team
of Massachusetts Institute of Technology (MIT) scientists
recreated experiments and researches of Tesla that relied
on the magnetic link of two resonators. They achieved a
transported power of 60 W through an air gap of 2 meters
with 40 % transmission efficiency utilizing coil with a
diameter of 0.6 m [9]. From that time, experts around the
whole world have been investigating WPT technology for
a variety of applications, including mobile phones, EVs,
domestic devices, healthcare equipment, and so on. The
research described in [10] introduces a straightforward power
management algorithm designed to oversee the integration
of multiple energy sources for charging a vehicle, even
while it is in motion. The system comprises a wireless
charging system, a photovoltaic generator, a fuel cell, and
a battery system. Additionally, a set of power converters
is associated with each energy resource to facilitate the
necessary adaptation between input and output electrical
signals. The study’s results indicate that all designed models
function effectively, and the power management control loop
has been successfully tested under simulation conditions.
Statistics indicate that the utilization of this multi-recharge
tool enhances vehicle power performance and extends vehicle
autonomy.
As depicted in Figure 1, WPT technology is broken down
to four primary classifications [3]: near-field technique [11],
far-field technique, acoustic technique [12], and mechanical
interaction technique by utilizing permanent magnets [13].
Magnetic gear wireless power transfer (MGWPT) technology
uses mechanical interaction in energy transfer. At first, it was
presented to replace conventional linked gear, it was later
developed for a variety of applications, including healthcare
equipment [14], EV driving [15], and EV static charging [16].
A transmitter turns electric power into squeezed sound waves
that move through the air, and a receiver outfitted with a
transducer transforms the motion generated by the sound
waves into electric power [12].
Using electromagnetic fields (EMFs) is the other method
of transporting the electric power wirelessly and these fields
are far-field and near-field. Power is conveyed in far-field
technology via electromagnetic radiations in the frequency
domain of GHz [16], which include radio signals [17],
microwave [18], and laser [19]. High levels of power can
be transported over long ranges with this technique [6], but
it necessitates giant antennas as well as intricate concentration and monitoring approach. This technique has seen
widespread application in military and aerospace sectors[20].
Near-field technology utilizes inductive electromagnetic
waves to convey electric power wirelessly, while fields
remaining within a limited zone surrounding the transmitting
coil. The fields in this region are classified into two types,
electric fields that uses capacitors (capacitive power transfer
[CPT]) [21], or magnetic fields generated by inductors
(inductive power transfer [IPT]) [3]. IPT and CPT are
regarded as the most appropriate techniques for charging
EVs. CPT system has the ability to reduce electromagnetic
interference by confining the electric flux between the
two plates [22]. It requires two capacitor systems: one for
transmission and the other for reception, to complete the
electrical circuit and facilitate energy transfer between both
sides. Additionally, to ensure effective energy transfer, proper
isolation of the two electrodes from the ground and the
car chassis is essential [23]. This system encounters various
challenges, including the requirement for planar capacitors
positioned in a straight line with minimal air gap between
them. It also cannot accommodate significant misalignments [24], and necessitates a high oscillating voltage source
to produce a strong electric field for energy transmission.
Additionally, the capacitors must be of considerable size to
effectively fulfill their function [25]. CPT faces a significant
challenge stemming from the exceptionally low permittivity
of air, resulting in very small coupling capacitance. Any
misalignment between the coupling plates or a sizable air gap
in CPT leads to a notable reduction in coupling capacitance.
Consequently, this technique is unsuitable for charging
electric EVs that necessitate power transfer over extensive
distances and may encounter misalignment between the
transmitter and receiver sides [26].
FIGURE 1. Categorization of WPT technologies.
IPT is a perfectly suitable system for charging EVs due
to its merits including: (1) it is capable of transmitting high
power (few kilowatts to Megawatt) across a relatively large
air gap distance ranging from 100 mm to 400 mm, which
meets the ground clearance requirements for most EVs [27];
(2) all components are electrically isolated, which makes the
charging process safer for human [5]; (3) it is a self-operating
(automatic) system and does not require user intervention;
(4) it is reliable during extreme environmental circumstances,
such as heavy rains, wind, and snow; (5) it eliminates the
concern of EV users about interoperability between plugs and
chargers [28]; and it has no moving or rotating parts, so it is
less noise and requires less maintenance.
Therefore, this manuscript focuses on IPT technology that
is applicable for EVs charging. Considering aspects related
to power transfer capability, transfer distance, efficiency,
and practicality, IPT show promising results for EV applications. The manuscript explored IPT technology including
principle of operation, system architecture, compensation
circuits, R&D activities, challenges, and technology gaps and
recommendations.
II. INDUCTIVE POWER TRANSFER SYSTEMS
IPT is an innovative method that wirelessly delivers electricity through the air using magnetic fields produced by
inductive coupling coils. This technology is used in several
applications such as biomedical devices [29], consumer
electronic [30], and EVs [31]. Ampere and Faraday’s laws
explain the basic operation principle of IPT system as
depicted in Figure 2. A magnetic field is generated when the
current (I) passes through the transmitter coil according to
Ampere’s law, as in Equation (1). This equation means the
flowing current in an enclosed path is equivalent to the line
integral of the strength of the magnetic field (H).
I =
I
−→H .
−→dl (1)
As defined by Faraday’s law when the magnetic field cuts
the receiver coil with number of turns (N2), an induced voltage (V) is generated, which can be expressed mathematically
as in Equation (2), where φ is the magnetic flux [32].
V = −N2
dφ
dt
(2)
FIGURE 2. Illustration of the IPT system principle of operation.
IPT is a perfectly suitable system for charging EV because:
(1) it is capable of transmitting high power (few kilowatts to
Megawatt) across a relatively large air gap distance ranging
from 100 mm to 400 mm, which meets the ground clearance
requirements for most EVs [27]; (2) all components are
electrically isolated, which makes the charging process safer
for human [5]; (3) it is a self-operating (automatic) system
and does not require user intervention; (4) it is reliable during
extreme environmental circumstances, such as heavy rains,
wind, and snow; (5) it eliminates the concern of EV users
about interoperability between plugs and chargers[28]; and it
has no moving or rotating parts, so it is less noise and requires
less maintenance.
An IPT system includes two electrically isolated sides:
the ground side includes a ground (transmitter) pad, rectifier
and PFC, and high-frequency (HF) inverter; and the vehicle
side incorporates the vehicle (receiver) pad, and rectifier,
depicted in Figure 3 [3]. Both sides include a compensation
(resonant) topology that keeps the system operating at
resonance condition to transport the nominal power at the
highest efficiency. This topology can be a single capacitor
(C) or an LC-network [4]. The transmitter coil is fed by HF
supply, which generates HF electromagnetic fields (EMFs).
These EMFs induce voltage and currents to the secondary
circuit to be rectified and charge the battery. According to
the SAE J2954 standard, the frequency of operation of IPT
system ranges between 79 kHz and 90 kHz, which makes
it easier diminish the size of both transmitting and receiving
pads. A wireless channel for communication exists between
both receiver and transmitter controllers to provide services
such as payment, ease of correct alignment, and alerting the
battery status [33].
FIGURE 3. Components of an IPT system.
A. MAGNETIC COUPLER SYSTEM ARCHITECTURE
The charging assembly is an essential element of IPT charging technique. It oversees transporting the electric power
from the supply to electric car battery. Three fundamental
parts with special specifications are involved in forming a
charging pad: conductive coils [34], magnetic cores as field
concentrators [35], and electromagnetic field shielding [36].
1) STATIONARY IPT
Pad architecture in stationary IPT system includes the conductive coil, magnetic materials and metallic shield identifies
the architecture of an inductive power pad. This architecture
is momentous in identifying the performance of an IPT
system, in terms of EMFs safety, transmission efficiency,
coupling factor, and tolerance for misalignment cases [5]. Ucores[37], [38], E-cores[37], and pot cores[39] were initially
the architecture used in conventional transformers, and were
considered for IPT system. These architectures introduce
undesirable performance with stationary charging of EVs due
to their large size, crisp configuration, heavy weight, high
cost, and very small tolerance to lateral misalignments [40].
Planar coils has been suggested in [5], [41], and [42] to
overcome these obstacles.
The three components (coil, core, and shield) must be
carefully designed to meet power and efficiency requirements; reduce the weight, size and thickness of the power
transmission pad; and decrease sensitivity to lateral and
rotational misalignments. According to the nature and the
shape of electromagnetic field produced, the architecture
of charging pad is classified into three categories: nonpolarized charging pads that produce magnetic fields with
perpendicular ingredients such as circular and rectangular
charging pads [28]; polarized charging pads, like DD, DDQ
charging pads [43], that generate horizontal magnetic field
ingredients; and multiple coils pad such as bipolar and
tripolar charging pads, which produce both perpendicular and
horizontal field ingredients [44].
In contrast to the DDQ charging pad architecture [45],
and bipolar charging pad architecture [46] which are suitable
to act as a car-side transmitter, the vast majority of pad
architecture works better on the transmitter side such as
Double-D (DD) [47], multi-coil homogeneous [48], circular,
and rectangular pad architectures [5]. In addition, most
of these architectures achieve the interoperability concept,
where any EV can be charged from any inductive charger
without limitations from the EV or inductive charger
producers [28].
FIGURE 4. Different architectures for stationary inductive charging pads
for both transmitters and receivers, (a) single-coil architectures, and
(b) multiple-coil architectures.
Figure 4 and Table 1 describe and compare various
charging pad architectures presented in the existing literature.
This comparison is conducted across several attributes
including shape, misalignment sensitivity, polarization, air
gap distance, interoperability, and others.
2) IN-MOTION IPT
In-motion charging technique is capable of being utilized
to charge EVs during their movement on the highways
without resorting to a complete stop or waiting even for
small periods. The in-motion charging technology has several
merits including, increasing the driving range while reducing
the size of the storage battery. It also increases the chances
of developing and designing autonomous cars which makes
it easier for the user to take advantage of the time spent in the
driving process. In-motion charging technology is occurred
by inhumation the power transmitter track beneath the surface
of the ground and hanging the power receiver coil at the
vehicle chassis. The power transmitter and receiver coils are
fed from a high frequency (HF) AC source. The generated
EMFs from the transmitter are cut with the receiving coil
while the EV moves above charging track in order to transport
TABLE 1. Characteristics of some stationary charging pad for electric vehicles.
the required power with highest transmission efficiency.
Additionally, there are several limitations that hamper the
prevalence of in-motion charging, such as the expensive price
of initial implementation, needing to provide independent
charging lanes, that is not easy to be available in packed cities,
and an ideal alignment between receiver and transmitter track
must be realized to avert a loss during the transmission of
power [51]. The transmitting track for in-motion technology
may be one of two pad kinds; stretched (single long) track
and segmented track [61], [62].
The in-motion charging pads at receiver side are the same
kinds as that available for stationary charging. This helps to
reduce the size of the vehicle ingredients, resulting in less
EV weight and expense, as well as increases the possibility
of interoperability between different architectures on the
transmitter side, whether in stationary or in-motion charging.
The vehicle side may hold one or several pads, according to
the EV class. The EV can carry a single pad which is more
appropriate for charging the small light-duty electric vehicles
or multiple pads, that may be required for intermediate- and
high-weight levels of EVs in order to comply with the power
demands [63].
For stretched transmitter track the length of the coil is
larger than its counterpart on the vehicle side. The track
length is between 1m to 100 m in the ground, which leads to
the possibility of charging more than one electric car on the
same track, simultaneously [64]. The elongated transmitter
consists of a lengthy track of litz wire supplied from a primary
station. This station incorporates a compensation network,
HF DC-AC converter (inverter), and AC-DC converter
(rectifier), as illustrated in Figure 5(a). This design possesses
several characteristics, including simplicity, ease of control,
a consistent coupling coefficient when the vehicle aligns
with the track, and it requires a straightforward resonant
compensation network. The charging system with stretched
track was constructed for general transport buses and shuttle
utilities with a name known as online electric vehicle (OLEV)
in South Korea [64].
FIGURE 5. Different architectures of transmitter for in-motion inductive
charging, (a) single extended coil path architecture, (b) sectionalized
transmitter architecture utilizing individual HF inverter for each coil, and
(c) sectionalized transmitter architecture utilizing collective HF inverter.
From another point of view, this architecture has some
defects, which are summarized as follows, generating excess
electromagnetic fields in cases of misalignment, the need for
periodic maintenance work [65], low coupling factor, which
leads to a decrease in power and efficiency [66]. There are
several classes for the extended transmitter lane depending on
the core configuration of magnetic pad; U- core form [67], Ecore form [67], I- core form [68], S- core form [69], ultra slim
S- core form [69], and cross sectionalized form (X-path) [70],
TABLE 2. Performance evaluation of several stretched transmitter track utilized in in-motion charging arrangements.
as depicted in Figure 6. Table 2 compares and highlights the
performance of the core classifications.
FIGURE 6. Types of cores for the extended track employed in an
in-motion charging system (a) I- core, (b) U-core, (c) E- core, (d) X-path
(e) S- core, and (f) ultra slim S- core.
The segmented charging track requires many compensation circuits and several converters and coils for transmission,
so this system is of high cost and complex in construction.
It is also vital to remove the self-coupling that occurs between
the transmitter segments, therefore the horizontal distance
between these segments and each other must be increased,
which leads to the fluctuation of the transmitted power and its
arrival in the middle of this distance to almost zero when the
receiver is one straight with the middle of this distance. Power
fluctuation can be decreased by shortening this distance and
positioning the transmitter segments near to each other, which
affects the resonant components due to the self-coupling of
the coils [64].
The transmission segmented track can be fed in two
arrangements, the first is to feed each segment separately
with a high-frequency inverter as in Figure 5(b), [66], and
the second is to use a common high-frequency inverter for
all segments in the transmission track as in Figure 5(c) [73].
In the initial configuration, the charging system is activated
or deactivated based on the vehicle’s alignment, with a highfrequency inverter connected to each transmission segment.
Each segment’s inverter operates at low power and is linked
to a compensation circuit to enhance system performance,
efficiency, and reliability. While this setup offers simplicity
and straightforward installation and configuration, it poses
safety risks due to high-power and voltage DC line operation.
Moreover, it requires a large number of inverters and sensing
devices, driving up system costs.
In the second configuration, a shared high-frequency
inverter powers the system through switches, with an
independent compensation circuit for each charging segment.
Switching devices control the activation or deactivation of
each charging segment, reducing safety risks compared to
other setups. However, this arrangement faces challenges
such as increased system costs due to the longer transmitting
track [74]. Despite the advantages that are available as a result
of using a common inverter, the arrangement needs to use a
large number of switches and sensors [71].
III. RESONANT CIRCUITS
Compensation (Resonant) network components are utilized
in inductive charging system due to several merits including,
compensation for the large leakage inductance resulting from
large air gap distance, which improve the system power
and efficiency [100]. Furthermore, it minimizes the source
apparent power by giving the demands of reactive power.
Additionally, it permits electronic devices to work with
soft switching [77]. Bifurcation is additionally averted by
operating the compensating elements at unity power factor
(UPF) to reach zero phase angle. The main reason for
introducing compensation networks into WPT technique is a
study by a team of MIT scientists[78]. This study was carried
out in 2007, where it showed a significant improvement in the
transmitting efficiency during the distance of an air gap after
the introduction of the compensation elements to the charging
circuit.
Compensation (Resonant) techniques can be classified
into basic (classical) compensation techniques as shown
in Figure 7 from (a), to (d), and mixed (composite)
compensation techniques as depicted in Figure 7 from (e) to
(l). There are four basic compensation techniques obtained
by connecting a parallel or series resonant capacitor to each
side of the transmitter and receiver. These basic techniques
are series primary capacitor-series secondary capacitor (S-S)
[79], [80], series primary capacitor -parallel secondary capacitor (S-P) [81], parallel primary capacitor-series secondary
capacitor (P-S) [82], and parallel primary capacitor -parallel
secondary capacitor (P-P) [83]. When mixing these basic
capacitors with inductors, hybrid compensation techniques
are produced, which include more than one inductor and/or
capacitor on one side such as LCL-P [84], LCL [85], LCLLCL [86], LCCL- LCCL [28], LCC [87], S-CLC [88],
CCL [89], and others.
FIGURE 7. Different compensation topologies, with (a)-(d) representing
fundamental topologies and (e)-(l) depicting mixed topologies.
Most of the studies dealt with basic compensation circuits
such as [40], [51], [83], and [90], while others dealt with
hybrid compensation techniques such as [49] and [91].
In [90], a -phase bipolar pad was utilized to transport a 50 kW
output power through 150 mm air gap with a transmission
efficiency of 95% using a series compensation circuit. In [92],
With the goal of enhancing the charging system efficiency
while utilizing asymmetric coils, an analysis of series-parallel
and series-series compensation techniques was performed.
This analysis is done on double models, one of them is
achieved by using equal size transmitter and receiver, and
the other when using unequal size coils. The efficiency of the
two models was observed at various transmission distances.
As a result of this, the series-parallel compensation technique
introduces higher efficiency than series-series compensation
when using transmitter that is larger than receiver (asymmetry
coils). According to the quality factor, coupling factor, and
compensation technique on both sides, the capacitance (C)
and inductance (L) values can be selected [93]. Because
of the enormous impedance of input, the difficulty of
the computations, and the load’s dependability, parallel
compensation is rarely utilized on the transmission side [94].
The capacitance in S-S compensation technique relies
on the inductance of transmitter (L1) and the resonance
frequency value, whereas the S-P compensation technique
depends on both L1 and resonance frequency, as well as
the mutual inductance (M) between the transmitting and
receiving coils[95]. In P-P and P-S compensation techniques,
the capacitance of transmitting side not relies only on
the coupling factor and inductance but also on the load
impedance. In P-S and P-P compensation circuits, to transport
a sufficient amount of power, a high operating voltage is
required because of the large input impedance of these
compensation techniques [96]. These techniques have some
advantages including high power factor, wide load variability
and high transfer efficiency at small mutual inductance [97].
Additionally, they utilize the same operating frequency and
operate at minimal power levels with a reasonably long
transmission distance [98].
When using mixed compensation circuits on both
sides of the transmitter and receiver, such as inductorcapacitor-capacitor (LCC)/ inductor-capacitor-capacitor
(LCC) and inductor-capacitor-inductor (LCL)/ inductorcapacitor-inductor, the efficiency of the IPT system is
increased throughout the total range of coupling and loading.
The extra leakage resistance in capacitances and inductances
increases copper losses significantly in mixed compensation
techniques than those in S-S compensation technique [99].
The both-sided LCL and LCC techniques are a perfect
compensation for EVs battery charging, because of the
behavior of the current source at vehicle side while a voltage
source inverter was working at the ground side. In [91],
The double-sided inductor-capacitor-capacitor compensation
technique has been studied. It was concluded that when
adjusting the LCC circuit, it is possible to reach the zero
current switching, in addition to that when the supply voltage
is constant, the output current rms value is constant. The
reactive power at the receiver side can be compensated by
using LCC compensation technique to fulfill unity power
factor operation. Also, this compensation technique doesn’t
rely on loading circumstances and coupling factor [100]. LCC
compensation technology is affected by several obstacles,
including the size and the increase in the system ingredients
which leads to a high cost [91]. Other than these limitations,
this compensation technology is the most common used
because of its merits such as the independence of the load
characteristics, high efficiency and allowing a large variation
in the cases of misalignment, in addition to reducing the
inverter current stress [91].
The basic and mixed compensation techniques are compared in Table 3, considering several metrics like operating
frequency (f ), load power (po), coupling coefficient (k),
transmission efficiency (η), air gap distance and coupler
configuration {Circular (CP), Rectangle (RP), Double-D
(DDP), and Bipolar (BP)}.
IV. CONVERTER TOPOLOGIES
Power electronics represent an essential ingredient in wireless
EVs battery charging. For better charging efficiency, it is
vital to concentrate on enhancing the effectiveness of the
power converters. The converters are relied upon the sort of
compensating strategy implemented as well as the wireless
system’s applications. In the beginning, an IGBT-based
push pull converter had been employed to finish off the
transformation procedures; however, with the advancement
of MOSFET infrastructure while employed at medium
voltages that vary between 60 V and 1200 V and raising the
value of frequency at which the switching occurs, the key
reliance to finish the step of conversion has been changed to
the full bridge MOSFET to work as power converter [111],
[112]. Power converters are divided into two main categories:
TABLE 3. Various WPT designs depending on compensating structure.
those used on the ground side and those used on the electric
vehicle side, as shown in Figure 8. The former typically
involve one or two conversion stages, while the latter can be
achieved using rectifiers.
A. CONVERSION PROSSES OF GROUND SIDE
The importance of the conversion prosses at ground side is the
ability to raise the network’s AC power frequency from low
value (60 Hz) to high value for matching the power levels to
be achieved according to the application to be used. There are
two ways to complete this conversion process, the first way is
to employ an AC-to-AC converter in order to directly convert
minimal-frequency AC power to high-frequency AC power
{single (one) stage AC-to-AC conversion}. This conversion
way can be achieved by using matrix converters. The second
conversion method takes place in two steps (AC-to-DC then
DC-to-AC) and is called dual (two) stage conversion.
FIGURE 8. Classification of converter techniques for IPT systems.
When talking about two stage power conversion, it can
be said that minimal-frequency AC power goes through
two conversion processes: the first is to convert it into DC
power, then the inverter comes in the second conversion
stage to convert this DC power into high-frequency AC
power [62]. Inverters have multiple merits that make them
well-suited for employment in EVs wireless charging. These
features are that; they can be implemented and controlled
simply and easily, through which the on/off prosses of the
power assemblies that make up the charging coupler can be
controlled, in addition, being harmonious with various coil
configurations, whether a single coil or multiple coils.
Most common inverter configurations in an inductive
charging system can be identified as shown in Figure 9.
These configurations include class EF [113], current source
push-pull [114], [115], and voltage source 1-ph, 3-ph,
or multi-phase [68], [116], [117], [118].
In [119], the authors propose the use of an H-bridge
converter on the ground side. On the vehicle side, two Hbridge converters are employed, with one supplying active
power to the battery and the other regulating the charging
current. This proposed system requires an external backup
DC source in the vehicle to provide approximately 50% of
the power to the battery, while the magnetic charger (coils)
furnishes the remaining 50% required to complete the battery
charge. Consequently, the overall cost of the electric vehicle
will rise due to increased size and weight. To make the ground
side devices more isolated and safer, the authors in [120]
suggested a HF transformer that minimizes the voltage to
the required levels. Through this system, conductive losses
are minimized by taking into account high voltage and low
current, and this helping to improve the efficiency of the
ground side inverter.
FIGURE 9. Inverter structures of DIPT (a) only one coil is energized by a
1-phase inverter, (b) Several series coils are energized by a 1-ph inverter,
(c) Several parallel coils are energized by a 1-ph inverter, (d) inverter with
several phases.
Most of the high-frequency converters utilized in wireless systems are illustrated in Figure 10. Regardless of
fluctuations in the coupling coefficient between the ground
and the vehicle, or changes in the load, it is feasible to
maintain constant and specific values for the load voltage and
current by employing various compensation circuits. These
compensation circuits, comprising a rectifier composed of
diodes connected to a soft output filter along with a DC-toDC converter, can be referred to as power conditioners.
While one-stage converters have a straightforward architecture, they are unable to fully execute the variable frequency
process. On the other hand, two-stage converters can achieve
voltage and frequency regulation, but they require extensive
passive components, including a large filter and a sizable
capacitor for the DC link. Consequently, system reliability
diminishes and overall costs increase [121]. An alternative
converter architecture for wireless power transfer systems,
distinct from both one- and two-stage converters, is known
as matrix converters (MC) [122]. Originally, these converters found applications in solar energy systems, aircraft,
and machinery utilizing induction principles, among other
uses [123]. Using this matrix converter (MC) architecture
allows for the elimination of bulky passive storage components and DC link elements, thereby enabling efficient
one-stage power conversion [124]. The matrix converter
(MC) functions by linking the load to the three-phase voltage
supply through its internal components, consisting of a series
of bidirectional semiconductor switching devices.
In [125], the introduced conversion technology was
represented by a one stage converter connected with two
sorts of compensation circuits, one S-S and the other SP. Comparing the two sorts of compensation, it was found
that the S-S topology results in the generation of a massive
leakage inductance at the car side, but it is preferable to use
it in WPT applications that required high power. In [126],
at high load cases and to increase the overall efficiency
of the three-coil charging coupler, a conversion topology
was proposed consisting of series or parallel compensation
FIGURE 10. Various types of transmitter converters, (a) voltage fed full
bridge, (b) voltage fed half bridge, (c) current fed full bridge, (d) voltage
fed class D amplifier, (e) current fed class E RF amplifier, (f) voltage fed
LCL converter.
elements connected to both the H-bridge converter and the
H-bridge rectifier at the ground side and the vehicle side,
respectively.
An alternative approach to the conversion process involves
the use of a one-phase (1)-ph) matrix converter (MC).
In this configuration, four bidirectional switching devices
are utilized to achieve an output with adjustable amplitude
and frequency at a predetermined switching angle, as shown
in Figure 11(a) [127]. From a theoretical perspective,
achieving an analysis of the open circuit (OC) and short
circuit (SC) conditions without any hindrances or issues
requires the use of a conventional 1-ph matrix converter
(MC) capable of synchronous and instantaneous switching.
However, in practice, attaining an ideal switching state is not
feasible, leading to the utilization of switching strategies in
the MC. One-phase Z-source matrix converters (MCs) offer
the capability for amplitude control and adjustable frequency,
which contrasts with traditional one-phase MCs that only
provide reduced amplitude as the frequency of operation
increases [128]. Figure 11 (b) depicts the arrangement of
1-ph Z-source MC. Because of its enhanced dependability
and capacity to directly transform the power in a single
step [129], the benefits of the Z-source MC drew the attention
of numerous applications [130], [131], [132]. It is made up of
an impedance grid consisting of double capacitors and double
inductors, 5 two-directional switches, an inductor-capacitor
(LC) filter, plus a load. The boost function is accomplished
by exploiting the impedance grid’s storage elements.
Figure 11(c) illustrates the complete architecture of a 6-
switch buck-boost matrix converter (MC). In contrast to the
one-phase Z-source MC, which features double capacitors
and double inductors and offers variable amplitude control
and frequency of operation, the 6-switch buck-boost MC
stores energy in a single inductor. The 6-switch buck-boost
MC consists of an inductor, 6 bidirectional switches, and
double capacitors functioning as a filter [133]. In [134],
a HF transformer insulated MC architecture was suggested,
in order to establish electrical insulation, therefore the huge
line transformer can be abandoned as well as give a variable
frequency and rectified voltages at output. It is made up
of a HF transformer with 4-switches at ground side and 2-
switches at vehicle side. Additionally, an inductor-capacitor
(LC) filter and DC isolating capacitor are employed at vehicle
side as demonstrated in Figure 11(d).
FIGURE 11. Types of 1-ph MC, (a) traditional 1-ph MC, (b) 1-ph Z-source
MC, (c) 6-switches buck-boost MC, and (d) HF transformer-isolated MC.
B. CONVERSION PROSSES OF VEHICLE SIDE
In most applications, such as wireless medical equipment’s,
it is preferable for the power conditioner to composed of the
rectifier only, which makes the size of the receiving coil small
to suit the small size of these devices. The full bridge diode
rectifier transforms the HF AC power generated at vehicle
side into DC power in order to charge the electric car battery.
DC power is obtained at the load (battery) by employing a
diode rectifier or synchronous rectification method. A DC-toDC converter can be connected after the rectifier in the first
method for the possibility of controlling the receiving side,
while the second method does not provide any possibility of
control but rather works to increase efficiency [107], [114],
[135], [136], [137].
FIGURE 12. Receiver side converters, (a) series adjusted receiver buck
converter, and (b) parallel adjusted receiver boost converter.
Rectifiers are categorized into two types: current-fed
rectifiers and voltage-fed rectifiers. Additional buck, boost,
or buck-boost converters can be employed with currentfed rectifiers, which occurs when compensation circuits are
S-S or LCC on the car side. Conversely, with voltagefed rectifiers, boost or buck-boost converters are used,
particularly when employing parallel compensation on the
car side. The most common types of converters utilized
in wireless charging systems are depicted in Figure 12.
When the vehicle incorporates multiple coils architecture
or a DDQ architecture on its side, it becomes feasible to
achieve multiple rectification stages but at the same time the
dimensions of the vehicle are increased. Therefore, this coils
architecture is not commonly employed [107], [114], [137].
In [138], the authors achieved a solution to charge the car
battery with the appropriate DC voltage by inserting a DC-toDC converter after the diode rectifier, which works to convert
the HF voltage on the car side to the appropriate voltage level
for the battery. To improve system efficiency, [139]suggested
a universal strategy feasible to all wireless charging systems,
which included a system-level study of a serial buck-boost
DC-to-DC converter and optimum impedance matching. The
serial buck-boost DC-to-DC converter accomplishes two
objectives, which may be stated as follows: the first is to
provide dynamic load isolation, and the other is to match
the optimum impedance of the amplifier, coil, and rectifier.
To prove this strategy, laboratory tests were conducted for a
wireless system that transmits 40 W of power at a frequency
of 13.56 MHz with a grid-to-battery (G2B) efficiency of up to
70 %. This efficiency is achieved for various loads, whether
they are resistors, batteries, or supercapacitors.
V. STATE OF THE ART
There are three methodologies of inductive charging for
electric cars: stationary inductive charging, which is achieved
when the car is stopped for a long time in parking lots [33],
quasi-dynamic inductive charging, such as what happens at
traffic lights while driving at low speeds [51], and in-motion
inductive charging when the vehicle is moving on fast roads,
in which a stretched coil or multiple segmented coils are
buried under the ground [51].
A. STATIONARY INDUCTIVE CHARGING
The stationary charging system of electric vehicles must
be carefully and precisely designed to suit the operating
requirements in terms of different power levels and air
gaps through which the power is transmitted. Therefore,
the development, research and demonstration activities of
the wireless inductive charging system take place. The
power levels that are suitable for EVs can be classified into
two main categories according to the global criterion and
guidelines [140]. The first is to transmit power ranging from
1 kW to 22 kW and is suitable for light-duty electric vehicles
(LDEVs). The other category is suitable for medium- and
heavy-duty electric vehicles (MDEVs/HDEVs) and transmits
power higher than 22 kW. Furthermore, the influence of
EV dimensions on power demands, every car category has
distinct levels of ground clearance. Therefore, the air gap
from the ground pad to the vehicle pad of the inductive system
is affected. This air gap distance is between100 mm and
400 mm for LDEVs and is larger for MDEVs and HDEVs.
The receiver pad must be consistent in size to the size of the
EV and not negatively affect the total weight of the vehicle
or the power consumption. The stationary wireless charging
system must efficiently transfer the desired power through the
appropriate air gaps, using designs with a weight and size
consistent with the vehicle. All this to meet the operating
restrictions and requirements (size, weight, air gap and power
levels). Inductive charging systems for EVs also have an
extensive domain of operating frequencies as well as with
various maximum power and transmission distance. Though,
several inductive systems work at domains of frequency from
10-to-100 kHz, limited researches have been conducted on
air-core coils at higher frequencies [141].
Based on the findings from literature, Table 4 presents a
comprehensive summary of various prototypes and models
of stationary inductive charging systems for electric vehicles.
This summary includes details such as power level (Po),
operating frequency (f ), distance between the ground pad and
the car pad (air gap), architecture of the magnetic coupler, and
transmission efficiency (η). Efficiency values are categorized
as pad-to-pad (P2P), reflecting the efficiency of inductive
pads; utility-to-load (U2L), indicating the efficiency of the
entire system; and DC-to-DC, encompassing all components
from the DC-bus of the ground side to the vehicle’s battery.
The table illustrates the wide range of stationary inductive
prototypes, with power levels spanning from 1 kW to
100 kW, developed worldwide at research centers, universities, national labs, and elsewhere. Additionally, beyond
research endeavors, several vehicle manufacturers have also
initiated the development of stationary inductive charging
systems. Table 5 provides an overview of the commercially
available products, detailing their power levels, transmission
efficiency, operating frequency, and other specifications.
B. IN-MOTION INDUCTIVE CHARGING
In 1976, the first inductive charging design was created
to suit the in-motion charging technology. This model
could transmit a power of 8 kW, but it did not work at
full efficiency [161]. Another prototype, the Santa Barbara
electric bus, was developed in 1979 [162]. In 1992, an inmotion charging system was attempted in the lab and on
the real field by PATH project (Partners for Advanced
Transit and Highways). Inductive charging system model are
manufactured and suspended in a bus. The roads have been
built and equipped with power transmission systems, and then
it has been possible to study and analyze the negative effects
that may be generated in the environment surrounding the
charging system. The PATH project design was capable of
transporting a 60 kW of power with an efficiency of 60%
through an air gap distance of 76 mm. But this prototype
of the project was not commercially popular due to its
disadvantages including the large weight and size of the
magnetic coupler, the setting up of the whole system is very
expensive, the increment of current because of the use of a
low operating frequency of up to 400 Hz, and high acoustic
noise, in addition to that it transmits the power through an
air gap distance not convenient for the various levels of air
gaps for electric cars. Even though the presence of all these
obstacles in this project, it was a good first spark that opens
the field for scientists and engineers to create and enhance
in-motion charging strategy [163].
In [164], it was suggested to use a transmission coil
extending inside the ground with a length commensurate with
the vehicle’s speed and power consumption per km. On the
other side of the charging system, a rectangular coil was
suspended in the car, and the system was operated with LCCS compensation technology, considering the calculation of
the transmitted power value and the efficiency of the system,
and the maximum value of the power is employed to deduce
the minimal value of the transmission current. It was found
that this system transmits efficiency slightly higher than 85%.
In [165], the segmented transmitter track is suggested with
several pads, each pad contains DD coils. A finite element
model was created to study the mutual induction between
the transmitter and receiver pads. A study and analysis were
also done to obtain the best dimensions for the design and
to determine the appropriate horizontal distance between the
pads that achieve the optimal properties of the system.
In [166], a two-spiral repeater was utilized in order to
ameliorate the efficiency, enlarge the air gap, and raise
the tolerance of the lateral misalignments. Transmission
efficiency can be enhanced to 60 % at an air gap distance
of 350 mm, as well as 81% at an air gap distance
of 100 mm, by optimizing system elements such as the
horizontal distance between sectionalized transmitter coils,
the number of the segments, and the loading circumstances.
In [72], a two-coupled charging system was utilized for the
sectionalized transmitter. The system works at a 20 kHz
frequency, and transport power of 5-kW at an efficiency of
92.5%.
It is clear that the possibility of spreading the in-motion
charging system within cities and on highways is considered
an urgent need these days to provide self-driving cars
and to help spread environmentally friendly electric cars.
Therefore, scientists and researchers are working with great
continuous effort to develop and improve in-motion charging
systems. Table 6 presents the R&D achievements in inmotion charging systems in terms of power level (Po),
frequency of operation (f ), efficiency (η), air gap distance,
transmitter (Tx ) architecture, receiver (Rx ) architecture, and
misalignment range (M.R).
C. STANDARDIZATION ACTIVITIES
As a nascent technology, wireless charging systems require
standards that offer precise specifications and directives for
technology advancement, testing, installation, and functioning. EV supply equipment firms and automotive manufacturers intending to introduce this technology to the market
will depend on these standards to streamline development,
cut expenses, hasten adoption, and adhere to interoperability
goals, safety standards, and efficiency requirements. Furthermore, standardization will aid in enabling interoperable
system operation with various vehicles.
TABLE 4. Present power levels for stationary inductive charging prototypes.
TABLE 5. Commercial EV products for stationary inductive charging system.
Numerous national and international organizations are
in the process of developing standards, guidelines, specifications, and recommended practices for wireless chargers
catering to various vehicles and operational environments.
These entities include the Society of Automotive Engineering
(SAE) [140], the International Electrotechnical Commission
(IEC) [173], the Japan Automobile Research Institute (JARI)
[174], the International Organization for Standardization
(ISO), Underwriters Laboratories (UL), the National Technical Committee of Auto Standardization (NTCAS), International Commission on Non-Ionizing Radiation Protection
(ICNIRP) guidelines [175], etc. Some of these standards
delineate system configurations for different power levels
and air gaps, such as SAE J2954 and IEC 61980-1, while
others offer guidance on data communication and interfaces,
as exemplified by IEC/TS 61980-2. ICNIRP has established
safety thresholds for leakage electromagnetic fields across
varying operating frequencies. These standards address
various aspects of the technology. However, there are still
challenges encountered during the standardization process,
as outlined below:
- Standards take into account different coil shapes, like
CP, RP, and DDP, which may not efficiently work together.
This raises concerns about interoperability and complicates system design to ensure interoperability, consequently
increasing system costs.
tion concerning compensation topologies, power converters,
control mechanisms, and system operation.
- The standards have been formulated specifically for lightduty EVs with slow charging capabilities. However, there is
currently a lack of standards addressing fast wireless charging
for EVs across various weight categories, including light,
medium, and heavy-duty vehicles.
VI. CHALLENGES, GAPS, AND RECOMMENDATIONS
Inductive charging, although offering automatic and convenient charging, encounters several challenges (gaps) such
as efficiency, compatibility, positioning, complexity, standardization, safety, interoperability, and cost. It’s imperative
to address these challenges and provide recommendations
for both stationary and in-motion inductive charging for
EVs. This is crucial to enhance the charging experience,
boost efficiency, and expedite the adoption of EVs in the
transportation sector. This section introduces several challenges encountered by the system along with corresponding
recommendations for addressing each challenge.
A. STATIONARY INDUCTIVE CHARGING
1) POWER TRANSFER EFFICIENCY
Inductive charging systems for electric vehicles often
encounter energy losses during the charging process, primarily due to factors such as distance between the charging pad
and the vehicle, alignment, and electromagnetic interference.
Optimize the design of the coils used in the charging
pad and the receiving device to maximize the coupling
efficiency between them. This includes selecting appropriate
coil geometries, materials, and configurations to minimize
resistance and maximize magnetic field strength. Improving
power transfer efficiency is crucial to reduce energy loss and
enable quicker and more efficient charging.
2) HIGH POWER CHARGING
Effectively transmitting high power wirelessly presents a
notable obstacle in inductive charging for EVs. Addressing
constraints in technology efficiency and heat dispersion is
vital to facilitate safe and efficient high-power charging,
thereby minimizing charging duration and optimizing the
usability of EVs.
3) STANDARDIZATION
The absence of standardized charging protocols poses compatibility challenges in the inductive charging industry for
electric vehicles. Diverse charging standards and protocols
adopted by different automakers and charging infrastructure
providers hinder seamless interoperability. Develop and
implement standardized technical specifications for IPT
systems, including parameters such as power levels, operating frequencies, communication protocols, and physical
interfaces. This ensures compatibility between different IPT
systems and components, allowing for seamless integration
and interoperability.
4) INFRASTRUCTURE DEPLOYMENT
Establishing an extensive and accessible infrastructure for
stationary inductive charging is a formidable task. The
installation of charging pads at diverse locations necessitates
substantial investments and coordination among stakeholders. Expanding the charging infrastructure over extensive
geographical regions is essential to promote widespread
adoption and facilitate convenient usage of electric vehicles.
B. IN-MOTION INDUCTIVE CHARGING
1) ALIGNMENT AND POSITIONING
In-motion inductive charging systems for electric vehicles
require precise alignment and positioning between the
charging infrastructure embedded in the road and the receiver
installed on the vehicle. Implementing automated alignment
systems can help ensure precise positioning of the charging
pad and the receiving device without requiring manual
intervention. This could involve the use of sensors, cameras,
or other technologies to detect and adjust alignment as
needed.
2) POWER TRANSFER EFFICIENCY
In-motion inductive charging systems face additional efficiency challenges compared to stationary systems. As the
vehicle moves over the charging infrastructure, the alignment
and distance between the charging pads can vary, affecting
power transfer efficiency. Overcoming these hurdles and
guaranteeing reliable and efficient power transfer during
dynamic charging is crucial. Implement dynamic power
control algorithms that adjust the power delivery in real-time
based on factors such as the distance between the charging
pad and the receiving device, the state of charge of the battery,
and environmental conditions. This ensures optimal power
transfer efficiency under varying operating conditions.
3) SAFETY AND RELIABILITY
In-motion inductive charging systems must ensure the safety
and reliability of both the charging infrastructure and the
vehicle. Safeguarding the charging pads integrated into the
road from environmental elements like moisture, debris,
and extreme temperatures is essential. Furthermore, robust
safety protocols need implementation to avert inadvertent
electrical contact and uphold the system’s reliability during
operation. Ensure that the IPT system complies with electromagnetic compatibility standards to prevent interference
with other electronic devices and systems, maintaining the
integrity of communication networks and avoiding potential
safety risks.
4) STANDARDIZATION AND INTEROPERABILITY
Similar to stationary inductive charging, In-motion charging
systems also encounter challenges related to standardization
TABLE 6. R&D for in-motion inductive charging system.
and interoperability. Diverse manufacturers adopting varying
standards and technologies for dynamic charging impede
compatibility between charging infrastructure and electric
vehicles. Collaboration within the industry to establish
standardized protocols and specifications for IPT technology
can facilitate interoperability, streamline development efforts,
and accelerate market adoption.
5) COST AND COMPLEXITY
cost of infrastructure are challenges that need to be addressed.
Implementing inductive stationary and In-motion charging
technology requires the installation of charging pads and
supporting infrastructure in various locations, such as homes,
offices, public spaces, and roads. The cost of infrastructure
setup and maintenance, as well as the need for widespread
adoption to justify the investment, pose significant challenges
for the wide-scale deployment of inductive charging. Initiatives aimed at reducing the overall cost of IPT systems
should be pursued, including advancements in manufacturing
techniques, component optimization, and economies of scale.
By tackling these shortcomings and putting into action the
recommended strategies, IPT technology can advance and
mature, opening avenues for its extensive adoption for static
and dynamic charging of EVs.
VII. CONCLUSION
This manuscript offers a comprehensive overview of inductive charging technologies applicable to both stationary and
in-motion electric vehicle (EV) charging. IPT emerges as the
most appropriate choice for EV battery charging owing to its
numerous advantages. It discusses and presents the working
principle and components of the IPT charging system.
Furthermore, it explores the different pad configurations at
both the transmitting and receiving sides that employed in
stationary charging systems, while assessing their effectiveness in terms of factors such as tolerance to misalignment,
dimensions of charging zones, interoperability, etc. It then
introduces the configurations employed at transmitter side
in dynamic charging systems, providing a comparative
analysis among them and an overview of the feeding
arrangements accessible. It discusses the various topologies
of compensation networks, including traditional and hybrid,
and then summarizes different WPT designs based on
the compensating structure. The manuscript investigates
different converters used in inductive charging system,
assessing their appropriateness for both the transmitting and
receiving sides. Additionally, the research and development
(R&D) that took place in stationary and in-motion IPT was
presented, and they were compared based on output power,
efficiency of transmission, distance between components,
frequency, and other factors. Ultimately, it highlights the challenges and gaps observed in both stationary and in-motion
inductive charging systems, offering recommendations to
tackle these challenges. These endeavors aim to serve as a
manual for individuals intrigued by the wireless charging
technology of electric vehicles (EVs), ultimately fostering
the wider adoption of these eco-friendly vehicles. The
various wireless charging technologies also marks the initial
steps toward achieving self-charging and self-driving electric
vehicles.
