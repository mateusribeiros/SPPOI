Title: Etching-Free Fabrication and Integration of 45°
Micro-Mirror for Surface-Compatible
Photonic Packaging

Abstract—We demonstrate how micro-mirrors can enable
surface-normal coupling of light to a photonic integrated circuit
(PIC) equipped with edge couplers. Most micro-mirrors are fabricated using etching techniques with a crystallographic direction
dependency, long processing times, and high fabrication costs. This
study fabricates a 45 ± 2° etching-free micro-mirror at the wafer
level using dicing and e-beam metal evaporation methods. The
root-mean-square (RMS) surface roughness of Au-deposited diced
µ-mirror is as low as 9 ± 0.65 nm with an angular profile of 45 ± 2°,
resulting in a 2.7 ± 0.2 dB reflectance loss. The diced micro-mirrors
are integrated into a PIC with edge couplers for demonstrating
the surface-compatible pluggable connection between the PIC and
fiber array. Overall transmission loss from the laser source-PIClensed fiber array is −6.06 dB at 1550 nm with ultra-relaxed 1dB
alignment tolerance of ±35 µm. The method described in this paper can be scaled to higher-volume manufacturing and wafer-level
integration of the µ-mirror and µ-lens array onto a PIC.
Index Terms—Etching-free micro-mirror, micro-optics integration, pluggable photonic packaging, surface coupling, wafer-level
photonic packaging.

I. INTRODUCTION
I
N SURFACE/VERTICAL coupling by micro-mirror, light
from edge couplers are generally reflected up by a 45° micromirror and coupled to a fiber as shown in Fig. 1. The advantages
of vertical coupling include scalability through wafer-level assembly and testing, improved machine vision system, potentially
eliminating the need for careful dicing and polishing of the chip,
and it may also enable surface-couple pluggable connectors
[1], [2], [3], [4], [5], [6]. The wet chemical etching of silicon
wafers is the most common way of fabricating near a 45° mirror
[7], [8], [9], [10]. In wet chemical etching, a <110> silicon
wafer is etched with KOH / KOH+triton / KOH+alcohols /
TMAH chemical solutions and these create an angular sidewall.
Researchers have also used dry etching, reactive ion etching,
and liquid emersion techniques for fabricating 45° mirrors from
Si and InP wafers [11], [12]. Etching is crystallographic dependent which means a wafer with a specific crystallographic
direction will give a near 45° micro-mirror. Therefore, a wafer
with <100> or <101> planes cannot be used for obtaining a
45° profile because etching of <100> wafer exposes <111>
walls which are square/rectangular v-groove [13]. This means
that etching is limited to certain wafer materials. Recently,
multi-photon polymerization-based 3D printing of the micromirror approach has been introduced and applied by a few
research groups [14], [15], [16], [17], [18]. The micro-mirrors
were 3D-printed on the facet of an edge-emitting laser and the
reflected light was coupled to a single-mode fiber (SMF) with a
coupling loss of−2.9 dB. This was further reduced to−1.1 dB by
printing a mirror on the laser as well as on SMF [14]. In another
work, a micro-reflector was printed at the edge of a PIC using
two-photon polymerization (TPP), and the light was coupled to
an SMF showing a −1 dB coupling loss [15]. One more group
fabricated a micro-mirror with monolithically integrated
cylindrical micro-lenses using deep proton writing (DPW). The
overall surface coupling from input MMF-micro-mirror-output
MMF was −0.97 dB [16], [17]. Undoubtedly, 3D printing can
produce micro-optics with complex shapes with high precision
and low loss. However, high-volume production of micro-optics
could pose a challenge due to the long processing times associated with additive manufacturing. For example, the fabrication
times for a single micro-optic component were 3 minutes using
TPP-based 3D printing in [15], 7.5 minutes using ink-jet printing
in [16], and 5 hours using the DPW method in [17], [18]. The
process of fabricating micro-mirrors at a fully embedded board
level is detailed using the pattern transfer method in [19], [20].
A silicon master mold with a 45° profile, created through deep
reactive ion etching, is pressed onto a UV-cross-linked polymer
substrate, followed by gold (Au) deposition using the liftoff
process. The overall reflectance loss of these micro-mirrors
was reported to be between −0.6 and −1.6 dB. Notably, this
fabrication was conducted at the board level, not the chip
level, and again the master silicon mold was obtained through
crystallographic-dependent etching as described in [7], [8], [9],
[10].
Recently, dicing of glass substrate was used to make a micromirror on a glass substrate [21]. Dicing is crystallographicindependent and a cost-effective physical method of preparing a
45° profile from any wafer type. A diced-mirror profile with root
mean square (RMS) roughness as low as 19 nm was obtained
for applications such as making a glass-based beam splitter for
an optical coherence tomography (OCT) system [21]. This work
introduced the possibility of dicing for fabricating various sizes
of mirrors (up to 500µm). However, there was no discussion
about the reflectivity of those mirror profiles, surface roughness
improvements, and exploring an opportunity to integrate them
into a photonic device.
To the best of the author’s knowledge, the wafer-scale fabrication of a micro-mirror with a dicing and e-beam process
and testing has yet to be reported in the literature. Therefore,
the novelties of this work would be fabricating scalable micromirrors from any wafer regardless of crystallographic directions
with significantly low processing time (refer to Section II-C).
Incorporating these micro-mirrors into a PIC will facilitate
vertical optical coupling that can be scalable to wafer-level
assemblies. Also, a pluggable photonic package will be built
by integrating a micro-lens array with a diced micro-mirror.
The demonstration of this package is included at the end of this
paper and a live demonstration is also available in supplementary
information.
II. FABRICATION AND TESTING OF AN ETCH-FREE
MICRO-MIRRORS
The focus of this study is to conceptualize, fabricate, and
test diced micro-mirrors and integrate them into a photonic
device. The mirrors of 15–20 µm height were fabricated by
dicing 500 µm thick Si followed by creating an Au deposition
layer using e-beam evaporation. The cutting speeds and depth
in dicing were optimized based on the microscopic profile,
surface roughness, and reflectivity of the fabricated mirror. The
micro-mirrors were then integrated into a photonic device as
described in Section III. This section details the methodology
used in the study.
A. Etching-Free Micro-Mirror Function
Micro-mirrors can be placed in front of edge couplers so
that light emanating from the coupler facet will be reflected
vertically upwards such that the optical axis of the reflected
beam is orthogonal to the surface plane of the PIC, as shown
by the designs in Fig. 1. This provides an example of how
this design could be integrated into future PICs, assuming that
additional thinning processes for reducing the thickness of the
micro-mirror were used to fit the mirror into trenches. Also, this
design is material agnostic to the PIC waveguide therefore, it
could be used in heterogeneous integration of III-V materials
in multi-chip arrangement. As a proof of concept, in this paper,
the micro-mirror is placed at the edge of a diced silicon nitride
PIC. For an etch-free micro-mirror, the 45° profile is diced from
a silicon wafer and then Au-plated using e-beam evaporation
techniques for improved surface roughness and reflectivity.
B. Fabrication of Etching-Free Micro-Mirror
A customized blade (ZH05-SD2000-KL45N) was supplied
by Disco with three important criteria such as 45° profile,
thickness, and surface roughness [22]. The fabricated blade
has a higher diamond concentration with the finest grit size to
minimize the surface roughness of the micro-mirror and wear of
the blade. One Si wafer of 4-inch diameter and 300 µm thickness
was used to make 15–20 µm deep 45° profiled trenches using the
automated dicing machine (Disco DAD3305) with two different
cutting speeds and parameters as specified in Table I. Once the
cutting speed was optimized with the test wafer, a 30 mm x
90 mm x 0.3 mm silicon wafer piece with an oxide alignment
mark was diced with the same blade using the same DAD3305
machine to make 15–20 µm deep 45° profiled trenches. Au
was deposited on the side wall of these trenches using the
Temescal UFC4900 e-beam metal evaporator. The minimum
required thickness of Au was 1 µm based on data acquired
from atomic force microscope (AFM) measurements. Finally,
micro-mirrors from these trenches were isolated by a thin dicing
blade (ZH05-SD2000-N1-70) [22].
C. The Testing of Micro-Mirror
The profile of more than 20 micro-mirrors with and without
Au deposition was measured using FEI Quanta 650 Scanning
Electron Microscopy (SEM) and 3D profiling with Promicron
Leica INM 200 microscope. The surface roughness of the 10 x
10 µm area of the micro-mirror reflective surface was measured
with a Bruker AFM machine-dimension Icon. The reflectivity
of 5 micro-mirrors before and after Au deposition was tested
by connecting a 1550 nm fiber-coupled SLD laser source to a
single-mode fiber (SMF-28). The reflected light from the diced
micro-mirror was coupled to a 105 µm core size multi-mode
fiber (MMF) which was connected to a Thorlabs photodetector
(the setup of the reflectivity test shown in Fig. 2).
The microscopic image of the wafer with the alignment mark
includes a total of 14 trenches with alignment mark spacing of
6 mm out of which one trench of 3 mm can be isolated. From
each isolated trench, two micro-mirrors can be obtained (Fig. 3).
Thus, dicing of 30 mm x 90 mm x 0.3 mm wafer piece gives 336
micro-mirrors of 3 mm x 5 mm x 0.3 mm size and approx. 84
micro-mirrors of 0.5 mm x 5 mm x 0.3 mm size with a dicing time
of 17.3 minutes with an additional time of 5 minutes for set-up.
SEM images of a 20 µm micro-mirror show a near 45-degree
sidewall profile.
From the test wafer, the reflection loss of micro-mirrors, their
surface roughness, and angular micro-mirror profile with two
cutting speeds before Au deposition are presented in Table II.
From Table II, decreasing the cutting speed from 10 mm/s to
5 mm/s reduces the reflection loss by −0.7 dB (15% coupling
loss). Also, variation in the angular sidewall profile of the
micro-mirror for 5 mm/s was lower than 10 mm/s with reduced
roughness. Based on the reflectivity, roughness, and profile of
micro-mirrors, a 5 mm/s cutting speed was selected for making
trenches from a 30 mm x 90 mm x 0.3 mm silicon wafer tile
with an oxide alignment mark. Then Au was deposited all over
the wafer piece covering the side wall of trenches as shown in
SEM images as shown in Fig. 4.
The performance of Au-deposited micro-mirror is presented
in Table III.
The overall reflectivity loss for 5 Au- deposited micro-mirror
ranged from −2.72 to −3.50 dB with RMS roughness ranging
from 8.93–15.25 nm. The AFM microstructure of as diced and
Au deposited micro-mirror for 5 mm/sec. cutting speed is given
in Fig. 5.
The surface roughness and peak to valley of the Au-deposited
micro-mirror (Fig. 5(b)) is ∼10 × lower than a diced micromirror (Fig. 5(a)). The calculated side-wall angular profile of 10
micro-mirrors ranged from 43.29-46.66°, the 3D profile of an
example micro-mirror is shown in Fig. 6.
Based on reflectivity results, micro-mirrors with the lowest
reflectivity loss were chosen to demonstrate integration with
photonic devices.
III. INTEGRATION OF MICRO-MIRROR WITH PHOTONIC
DEVICES
As shown in Fig. 1, a diced micro-mirror can be attached to
the edge of a PIC to reflect light vertically upwards to make
surface-compatible photonic packaging. The SOLIDWORKS
design and Zemax optical simulation of such a package (Figs. 7
and 8) consider that light in the form of a Gaussian beam from
the waveguide with mode field diameters (MFD) of 6.8 µm x
6.2 µm is reflected up by a 20 µm long 45° micro-mirror (∼97%
reflectance at 1550 nm) with ledge of 5 µm. This light beam
gets expanded and collimated by an off-the-shelf fused-silica
micro-lens with NA of 0.16 [23] bonded on a micro-mirror with
5 µm thick index matching adhesive (RI: 1.55). The collimated
beam in the air was coupled to micro-lens with the same mode
size (beam size of 128µm) which was bonded to SMF with
20 µm thick index-match adhesive. The system was simulated
and optimized for maximum coupling efficiency and alignment
tolerance of the micro-mirror was investigated. Furthermore,
the alignment tolerances of the micro-mirror integration and
pluggable connection were calculated by displacing lensed SMF
in the X and Z axes.
For an additional 1 dB loss (∼80% coupling efficiency),
the alignment tolerance of the micro-mirror in Z-direction is
±2.7 µm. The 1 dB angular alignment tolerance of the micromirror is ±1.5°. The height of the micro-mirror was decided by
maximizing the coupling efficiency of the system. Simulation
(Fig. 8(c)) shows that maximum coupling can be achieved for
micro-mirrors of ≥ 15 µm height therefore, 15–20 µm height
of micro-mirrors were fabricated in this study. The overall
tolerances of the pluggable system simulated by displacing
lensed fiber were ±30 µm in the X and ±32 µm in the Z axes,
respectively.
The SiN reference PIC (3.5 x 3.5 mm) used in this package,
as described in [24], [25], was fabricated by LioniX and it has a
series of loopback edge couplers on the east and west end of the
chip. The experimentally measured MFD of the edge couplers
was 6.8 µm x 6.2 µm at 1550 nm [24], [25]. The PIC was
mounted on a 3.3 mm wide aluminum sub-mount using epo-tech
H20E silver epoxy to provide a 100µm overhang on each side of
the PIC. An 8-channel fiber array (FA) was aligned and bonded
to the edge coupler facet using Dymax OP-20632 UV-curable
adhesive for evaluating optical loss at the bonded interface.
Then, the micro-mirror with the best reflectivity (−2.72 dB)
was aligned and bonded to the output edge coupler using the
same optical epoxy. This alignment was performed with SMF-28
fiber to which light reflected by the micro-mirror was coupled.
An off-the-shelf fused-silica micro-lens array from Axetris (Part
No.: FCA250FS, 1 × 8 Array, 250 µm Array Pitch, Radius of
Curvature = 0.315 mm, conic k = −0.7) was secured with in
a Nanoglue machine from Nanosystec. This machine features a
single camera for machine-vision processes, a 6-axis alignment
arm with pneumatic grippers, and automated epoxy dispensing
and curing capabilities. The micro-lens array was held on one
end, while a lensed fiber array was gripped on the other. Initially,
the micro-lens array was passively aligned with a micro-mirror
attached to a PIC assembly and the lensed fiber array. Active
alignment was then performed to optimize the signal. Ultimately,
the micro-lens array was bonded to the interface between the
PIC and the mirror, transforming the packaging into a surfacecompatible pluggable photonic packaging. The image of the
experimental setup for expanded beam connection shows an
8-channel fiber array bonded to one end of a PIC (Fig. 9). The
micro-mirror was bonded to the other end of the PIC and a
micro-lens array was integrated into the interface between PIC
and micro-mirror.
The reflectivity loss, alignment tolerance of surfaceassembled pluggable connection, and comparison between simulation and experiment are shown in Fig. 10. The reflectivity
results in Fig. 10(a) show that Au deposition reduced reflection
loss by ∼4x than diced micro-mirror without Au. The overall
coupling loss of surface-compatible pluggable connection was
−6 dB with significantly relaxed tolerances of ±30 µm in X and
±32 µm in Z (Fig. 10(b). The simulation results of the overall
package shown in Fig. 1 match well with the experiment in the
X direction (Fig. 10(c)). As seen, the experimental tolerance
in Z is higher than the simulated tolerance (Fig. 10(d)). The
−1 dB tolerance of micro-mirror in Z direction is ±3.3 µm
as presented in Fig. 10(e) which is comparable to tolerance
(±2.7 µm) obtained in the simulation.
The losses from different assemblies and components of
surface-compatible photonic packaging demonstrator are shown
in Table IV.
demonstrator is −6 dB which is mainly coming from four
sub-assembly losses (L1) fiber array bonding to PIC loss per
facet; (L2) micro-optics assembly losses (i.e., back-reflection,
scattering, and alignment of micro-mirror and micro-lens array);
(L3) the reflectance loss and (L4) µ-lens fiber array preparation
loss (Fig. 11).
IV. DEMONSTRATION OF PLUGGABLE OPTICAL I/O USING
MICRO-MIRROR
High-precision injection molded plastic building blocks
(Lego) were used to build a pluggable connector demonstrator,
similar to the one shown in [25]. Building this connector involved three processes. The first step was to make an Aluminium
sub-mount and fix PIC to this sub-mount with adhesive. In the
next step, the fiber array was passively aligned and epoxy bonded
on a Lego block. Further, the whole Lego assembly was aligned
to the micro-lens array on the chip. Finally, the Lego was bonded
on the baseplate using Dymax OP-29 UV-curable epoxy. 30 trials
of plug and unplug were performed to evaluate the reliability of
such a pluggable interface.
From the trials of repeated plugging and unplugging, the mean
total loss was −6.4 ± 0.3 dB (Fig. 12). This high reproducibility
comes at the cost of an additional 0.4 dB loss which is comparable to pluggable connectors demonstrated before [23], [24],
[25], [26].
Bandwidth of the demonstrator was measured using AnritsuMS9710C Optical Spectrum Analyzer. 1dB bandwidth of the
V. DISCUSSION
This study presents and investigates a scalable approach to
fabricate micro-mirrors at the wafer level with an etch-free
dicing process. The surface assembly of a photonic package is
mainly dependent on the angular profile of micro-mirrors. For
example, a minor change in the angle of the mirror introduces
the optical and geometrical shift of other assembly components
such as micro-lens array and lensed fiber array, aligning these
could be complex [27], [28]. The profile and reflectivity of the
micro-mirror depend on the optimization of blade grit size and
dicing parameters such as cutting speed, cutting depth, and Au
deposition. With e-beam evaporation, atoms of Au in the vapor
phase were deposited on the side wall of the trench/micro-mirror
making a thin film Au reflective coating, The coatings have
been used for smoothening of wafers/substrates to increase
reflectivity and minimize scattering [29], [30]. The reflectivity
of Au film is impacted by the surface roughness and thickness
of the film. The reflectivity of the film reduces with an increase
in the thickness of the film and surface roughness as shown
in [31], [32]. In our study, a minimum Au coating thickness
of 1 µm was required, based on the surface roughness and
peak-valley height data obtained from AFM. Due to operational
constraints with the e-beam evaporator, a higher thickness of
5.4–7 µm was deposited. These could be contributing factors
behind the −2.7 dB reflectance loss of Au-coated micro-mirror.
In the future, reflectance loss could be reduced by changing the
grit size of the blade such as forming a blade with >#2000 grit
and optimizing the e-beam evaporation method. Also, further
machine process development could be performed to deposit a
thickness closer to 1 µm.
The optical simulation of the surface-compatible assembly in
Fig. 8(a) assumes the mode sizes of waveguide in X and Z to be
6.8 µm × 6.2 µm which matches the mode sizes of manufactured
PIC used in this study [24], [25]. The mode size in the Z (6.2 µm)
is smaller which gives a higher divergence of the beam. This
large-size beam is collimated by a micro-lens array which is
why tolerance in the Z-direction is more relaxed than in the Xdirection. The simulated and experimental alignment tolerances
of the micro-mirror in Z directions relative to PIC, for 1dB loss,
are ±2.7 µm and ±3.3 µm, respectively. This level of tolerance
will require both passive and active alignment of micro-mirror.
In future, if highly accurate pick and place methods such as
micro-transfer printing could be used then active alignment
could be easier. Overall losses of surface-compatible packaging
could be further minimized by eliminating the ledge on the
micro-mirror for better alignment. The micro-optics assembly
loss of −2.1 dB (Table IV) could be minimized by designing an
appropriate micro-lens array that better matches the mode size
of the waveguide, rather than using an off-the-shelf micro-lens
array designed for an MFD of 10.4µm. For example, based on
analytical simulations of a 6.8 × 6.2 µm MFD edge coupler, a
680 µm thick fused silica micro-lens with a radius of curvature of
210 µm would work better than current lenses. The pluggable
Lego demonstration introduced low additional loss with very
high reproducibility of 0.3 dB for 30 plug/unplug cycles.
More scalable wafer-level assembly can be built if thousands
of micro-optics can be picked and placed at once with
techniques such as micro-transfer printing [33]. It has already
been demonstrated that micro-transfer printing can be used on
thick optical components. Combining the techniques used in
[33] with the technology shown in this paper could open the
possibility of wafer-level testing of optical packaging (example
shown in Fig. 14). In this example, a wafer with PICs could
be diced then arrays of micro-mirrors and micro-lenses could
be integrated to the PICs by micro-transfer printing. After that,
an optical probe with an array of fibers can be moved from
package to package on the wafer for optical testing.
VI. CONCLUSION
This study presents the design, fabrication, and characterization of micro-mirrors formed by dicing and e-beam evaporation
techniques. These mirrors were further used for demonstrating
surface-compatible pluggable photonic packaging. The dicing of
the Si wafer with the ZH05-SD2000-KL45N blade introduces
a 45° ± 2° angular profile of the micro-mirror. The e-beam
evaporation of thick Au on the micro-mirror smoothens the
RMS surface roughness (8.9–15.2 nm) which is 10× lower as
compared with a diced mirror (44–55 nm). The reflectivity loss
of the micro-mirror formed with the customized dicing blade
is as low as −2.7 dB which is a result of low RMS surface
roughness, reduced waviness, and near 45° angular profile. In the
future, the reflectivity of these micro-mirrors can be improved by
designing a blade with a higher grit size (>2000) and optimizing
the e-beam evaporation method.
By using a micro-lens array and diced micro-mirror, the
surface-compatible pluggable package was built with an overall
assembly loss of −6 dB and relaxed tolerances of ±5 mm,
±30 µm and ±35 µm in Y, X and Z directions. Finally, a
pluggable Lego demonstrator with a high coupling reproducibility of 0.3 dB was obtained. The advantage of dicing is its
flexibility in fabricating various shapes and sizes of micro-mirror
at wafer-level with a low processing time of 17 minutes per wafer
as compared to etching (≥30 minutes). Also, this technique has
a better scalability potential compared to direct writing methods
(TPP-3D print, DPW, ink-jet printing) as thousands of diced
micro-mirrors can be picked and placed using micro-transfer
printing. Integrating these mirrors with photonic devices enables
surface-compatible optical connection and introduces higher
optical interconnect density where light can be coupled between
multiple input and output channels of PIC and fiber.
CONFLICT OF INTEREST
The authors do not have any conflict of interest regarding the
data presented in this study.

