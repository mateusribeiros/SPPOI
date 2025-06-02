Title: Additively Manufactured Ceramics for Compact Quantum Technologies

Abstract
Quantum technologies are advancing from fundamental research in specialized laboratories to practical applications in the field, driving the demand for robust, scalable, and reproducible system integration techniques. Ceramic components can be pivotal thanks to high stiffness, low thermal expansion, and excellent dimensional stability under thermal stress. Lithography-based additive manufacturing of technical ceramics is explored, especially for miniaturized physics packages and electro-optical systems. This approach enables functional systems with precisely manufactured, intricate structures, and high mechanical stability while minimizing size and weight. It facilitates rapid prototyping, simplifies fabrication and leads to highly integrated, reliable devices. As an electrical insulator with low outgassing and high temperature stability, printed technical ceramics such as 
 and AlN bridge a technology gap in quantum technology and offer advantages over other printable materials. This potential is demonstrated with CerAMRef, a micro-integrated rubidium D2 line optical frequency reference on a printed 
 micro-optical bench and housing. The frequency instability of the reference is comparable to laboratory setups while the volume of the integrated spectroscopy setup is only 
. Potential for future applications is identified in compact atomic magnetometers, miniaturized optical atom traps, and vacuum system integration.

1 Additive Manufacturing for Compact Quantum Technologies
Atomic quantum sensors exploit the quantum properties of atoms to measure physical quantities like gravity, electric and magnetic fields, inertial forces, and time with unparalleled precision and accuracy.[1, 2] These sensors therefore have significant potential in advancing navigation, timekeeping, and resource exploration. Thanks to their precision, they can be central in fundamental physics research or Earth observation in both terrestrial and extraterrestrial settings.[3-6] These varying applications require devices with high level of system integration, suitable for practical field and space deployment. This demands the extensive integration and miniaturization of all subsystems, including the laser system, electronics and the physics package. Additionally, these devices must be robust against environmental influences such as mechanical stress, thermal fluctuations, and radiation exposure to ensure reliability on mobile platforms. Future commercialization and small-series production add further requirements: systems and their components must be reproducible, scalable, and cost-effective to produce and easy to assemble.

Additive manufacturing (AM) is an innovative approach particularly beneficial for realizing compact physics packages for quantum technologies. A physics package is the core assembly containing the quantum system and is tailored to the specific application. For atomic quantum sensors, it usually incorporates atoms within a vapor cell or high vacuum system and electro-optical systems for state preparation and readout. AM enables a higher level of device integration and functionality, offering increased freedom for functional designs.[7] Initial applications of AM in quantum technologies have primarily involved 3D printing of metal components for vacuum systems. Notable examples include vacuum components such as resistively heated alkali metal dispenser (Ti-6Al-4V),[8] magnetic coils (Al-Si10-Mg)[9] and shields (permalloy-80).[10] Vacuum flanges (Ti-6Al-4V)[10] and a compact vacuum chamber (Al-Si10-Mg)[11] with gyroid structures for weight reduction have been realized and demonstrate the suitability of additively manufactured metal components for vacuum systems in quantum technology. Additionally, an optical spectroscopy system for cold atom applications (volume 
, based on 
 optics) has been realized using a photopolymer as the base material for mounting optical components.[12]

This work investigates additively manufactured ceramics for applications in miniaturized quantum technologies, exemplary components are displayed in Figure 1.

Details are in the caption following the image
Figure 1
Open in figure viewer
PowerPoint
Selection of additively manufactured 
 components, including micro-optical benches, housing lids, isogrids, holders for electro-optical components, and test structures for resolution and process parameters.
2 3D Printed Ceramics for Miniaturized Physics Packages and Electro-Optical Systems
Transferring quantum sensors and electro-optical systems to compact and robust devices for field applications requires suitable materials, miniaturized components and qualified assembly and integration technologies. Important physical and thermal properties of selected materials for compact quantum technologies are summarized in Table 1. This includes printable materials along with others commonly used in miniaturized physics packages and electro-optical systems. For mobile applications, selecting lightweight materials with a high Young's modulus 
 is critical to guarantee robust setups with minimal deformations under environmental loads. For electro-optical systems, matching the coefficient of thermal expansion (CTE) to other commonly used materials (like BK7 or titanium) is crucial for ensuring stable connections. High thermal conductivity 
 is essential to maintain minimal thermal gradients, thereby reducing non-planar deformations. The assembled setups must also meet common thermal qualification standards for mobile devices,[13] which require a minimum temperature stability from 
 to 
. Vacuum compatibility is another crucial criterion for use within hermetically sealed devices or in the vacuum systems of physics packages.

Table 1. Relevant physical properties of materials for applications in miniaturized physics packages and electro-optical systems: Young's modulus 
, density 
, coefficient of thermal expansion (CTE), thermal conductance 
 at room temperature. Furthermore, the temperature and vacuum suitability and machinability of the materials in standard machine shops is denoted. The table is divided into two sections: above the line are materials with established printing processes including popular engineering polymers, and below are materials typically used in sub-assemblies such as micro-optical systems. Ceramics are highlighted in bold. Where available, typical properties of printed materials are provided. Note that these properties vary based on test method, manufacturing machine, process parameters, part geometry, and post-processing. They should be regarded as reference values and require experimental validation for specific applications.
Material	
 
 
CTE 
 
Temp. & vac. suitabilitya)	Machinabilityb)	Ref.
3.99	380	7.6	29	
−	[14]
AlN	3.26	308	3.9	160	
−	[15, 16]
Al-Si10-Mg	2.68	70	23	130	
[17]
Rigid 4000	1.26	4	63	0.3	
c)	
[18-20]d)
High Temp	1.14	3	75	0.3	
c)	
[19, 21]d)
PLA	1.25	2.3	68	0.2	
e)	
[12, 22-24]
SS 316L	7.98	180	16	15	
[25, 26]
Ti-6Al-4V	4.47	110	9	6.6	
[27]
6.09	205	10	2.5	
−	[14]
BK7	2.51	82	8.3	1.1	
−	[28]
Fused Silica	2.20	73	0.5	1.4	
−	[29]
ZERODUR	2.53	90	
0.02	1.5	
−	[30]
Sapphire	3.98	345	8.4	27.2		−	[31]
Kovar	8.36	138	5.1	17.3			[32]
a) Temperature stability to at least 
 is a common requirement.[13] Application in compact high vacuum systems requires outgassing rates 
. This usually involves conditioning above 
. In general, only a few polymers are high-vacuum compatible;
b) 
 excellent/good machinability; 
 demanding material, possible in standard machine shops; − materials with high hardness, specialized tooling and techniques required (e.g. ultrasonic machining), expensive;
c) 
 (Rigid 4000) and 
 (High Temp) heat deflection point at 
;[18, 21]
d) Since the value for 
 is not available, an optimistic estimation from comparable photopolymers is stated for reference;[19]
e) 
 heat deflection point at 
, 
 glass transition temperature.[23]
Compared to other printable materials detailed in Table 1, technical ceramics possess several unique properties: exceptionally high stiffness, low density 
, low thermal expansion, and relatively high thermal conductivity. These properties ensure mechanical stability under varying temperature conditions and mechanical loads. For applications requiring thermal insulation, materials such as 
 are suitable. Ceramics can be manufactured into precise shapes and are compatible with a wide range of microfabrication and thick-film technologies. As electrical insulators with high temperature stability, they can be fully or partially metallized with a variety of methods. This enables realization of electrical conductor tracks, wire bonding, or soldering of components onto substrates. Combined with excellent dielectric properties, ceramics are a well-established choice for high-frequency applications. Proven processes are available for hermetically sealing ceramic materials and alumina (
) is a standard insulator material for electrical vacuum feedthroughs. For instance, a compact vacuum chamber made of traditionally manufactured alumina with optical viewports has been successfully realized for cold atom applications.[33] In comparison to other temperature-stable materials listed in Table 1, ceramics have no magnetic susceptibility and high purity. These attributes are particularly important for magnetically sensitive applications, such as atomic magnetometers, where even minor ferromagnetic impurities in materials like aluminum alloys can disturb measurements. These advantages make ceramics an ideal choice for the development and production of robust and miniaturized quantum sensor systems, leveraging a broadly established technology base.

One approach to realize compact optical systems and laser sources at the Ferdinand-Braun-Institut (FBH) is integrating optics, electro-optical components, and electronics on a unified substrate, a micro-optical bench (MIOB).[34] This substrate often includes custom precision reference marks for alignment, specialized shapes for component mounting and is made of ceramics (AlN, 
) for the discussed advantages. Application of conventional methods for manufacturing ceramics presents specific challenges for micro-optical systems. The required high precision often involves additional post-processing with diamond tools, multiplying the high costs associated with ceramics. Furthermore, traditional manufacturing techniques are limited in mechanical complexity because of their inability to realize complex shapes or internal structures. They also suffer from extended lead times due to complex process chains. This becomes especially noticeable when prototyping or fabricating unique components and limits development agility.

Additive manufacturing methods of ceramics based on vat photopolymerization are a versatile solution to these limitations of traditional manufacturing.[35] These methods enable the creation of complex geometries and functional designs, which is advantageous in research and development (R&D) environments. The streamlined and scalable manufacturing process enables cost-effective rapid prototyping and customization, substantially reducing lead times and enabling on-demand manufacturing. Depending on the method used, high precision and excellent surface qualities are achieved without the need for additional post-processing. Designs can be tailored to specific applications, for instance, topological optimization can be used to produce parts with reduced size and weight[36] or to incorporate special functionality such as localized heating zones by spatially tailored thermal conduction. Additive manufacturing presents a versatile and efficient approach for producing ceramic substrates for micro-optical systems and other components for high-performance applications in quantum technologies. Additionally, employing 3D printing enables in-house management of the entire process chain. This ensures reproducible quality and provides complete control over the manufacturing process.

2.1 Methods for Additive Manufacturing of Technical Ceramics
For the generative production of ceramic parts, multiple methods with distinct benefits and specific disadvantages have been established. These include Stereolithography (SL), Binder Jetting (BJ), Fused Deposition Modeling (FDM), Direct Ink Writing (DIW), and Selective Laser Sintering (SLS). Their feedstock systems use, for example, ceramic powders or slurries, which are ceramic-filled suspensions with a photopolymer or water.[35] Lithography-based ceramic manufacturing (LCM)[37] is a form of vat photopolymerization. Similar to SL, it uses light to polymerize a ceramic slurry in a vat. A dynamic mask is formed with a digital micromirror device (DMD) to shape the light and cure the polymer in defined areas.

LCM is the method of choice for our applications, as it facilitates the manufacturing of highly complex parts with delicate features, internal structures, and high feature resolution and precision. The technique is well-suited for prototyping and small-volume productions. A selection of example components is shown in Figure 1. In our experience, the quality of the final components is considerably better than printed metal or polymer materials listed in Table 1. Moreover, the mechanical and thermal properties have been demonstrated to be similar to those produced by classical manufacturing methods.[16, 37-39] An extensive range of materials is established, including 
, 
, AlN, which are of particular interest for our application requirements. Our printer (Lithoz CeraFab S65) is equipped with a build platform measuring 
, provides a build height of 
, a layer thickness of 
, and a lateral resolution of 
. The manufacturing process is bottom-up, beginning with the dispensing of the ceramic slurry into the vat, where it is evenly distributed by a blade.[37] Subsequently, the build platform is lowered into the slurry and the desired areas are selectively cured by exposure through the transparent bottom of the vat. This procedure is repeated, building the part layer-by-layer with up to 
. Following the print process, the parts are removed, cleaned and then subjected to a thermal debinding and sintering cycle.[40] With this final step, the printed parts achieve full density. Subsequent optical quality inspection is used to optimize the design, printing, and processing parameters in the next run to achieve the desired geometrical tolerances and functions. Typical process duration for the parts depicted in Figure 1 are a few hours for printing and four to eight days for thermal post-processing, depending on the thickness of the part. Consequently, agile development cycles with periods of two weeks are possible.

3 CerAMRef: Optical Frequency Reference on a Printed Alumina Micro-Optical Bench
To demonstrate the feasibility of additively manufactured ceramics for integrated electro-optical systems and packages, we realized a miniaturized optical frequency reference, CerAMRef, shown in Figure 2. This reference employs LCM printed 
 ceramics for both the micro-optical bench and the overall housing. It utilizes Doppler-free frequency-modulation spectroscopy (FMS)[41] on the D2 line of atomic rubidium within a vapor cell and is used to stabilize a laser system at 
.

Details are in the caption following the image
Figure 2
Open in figure viewer
PowerPoint
Top: CerAMRef frequency reference module mounted on a Peltier element with PEEK screws for thermal insulation. The PCB is electrically connected with the photodiode and Pt100 temperature sensor and includes operational amplifiers. Bottom: a CAD rendering overlaid with the beam path of the Doppler-free FMS setup with fiber collimator (1), PBS (2), Rb-filled vapor cell (3), 
 plate (4), mirror (5), focusing lens (6) and photodiode (7).
3.1 Design and Assembly of the Frequency Reference
The optical layout is illustrated in Figure 2. It realizes a Doppler-free spectroscopy setup using two counter-propagating light beams[42] on a small volume and minimizes the optical beam paths with suitable optical components. Light is coupled into the frequency reference with a pigtail-style fiber collimator with a single mode, polarization-maintaining fiber, emitting light with a 
 beam diameter of 
. Subsequent custom optical components have an edge length of 
 unless otherwise specified, providing a sufficient optical aperture. The p-polarized light first passes a polarizing beam splitter (PBS) before it enters a borosilicate cell. This cell (Rydberg Technologies) is glass-blown, 
 long and 
 in diameter, features anti-reflective (AR) coated windows angled at 
 and contains rubidium vapor in its natural abundance. The light then passes through a 
 plate (thickness 
) and is reflected off a dielectric mirror aligned to overlap the incoming and reflected beam, thus enabling a Doppler-free measurement geometry. After the second pass of the 
 plate, the now s-polarized light is reflected by the PBS and focused onto a photodiode with a 
 lens (Thorlabs LA1024-B, 
 diameter). This fiber-coupled design enables modular connection to the spectroscopy laser source, allowing versatile integration into various laser systems for different applications.

The mechanical design of the frequency reference incorporates a housing and micro-optical bench made of 3D-printed alumina.[14] This bench features custom mounting geometries, V-grooves and alignment features for the electro-optical components, which are either cylindrical, cuboidal or have an irregular shape like the glass-blown alkali cell, see Figures 2 and  3. These geometries are specifically tailored to the components of the reference. For example, the dimensions of the glass-blown vapor cell are determined with a measuring microscope, indicating a thickness variation at the location of the fill port. The V-groove in the bench for mounting the cell is designed specifically for the cell integrated in the CerAMRef, leaving adequate space around the fill port while ensuring sufficient contact area for the adhesive bond. Additionally, the bench includes a mounting recess for a Pt100 temperature sensor. The photodiode (Hamamatsu S5972) is packaged in a TO-18 housing and fixed in a custom recess on the module's sidewall. This recess is slightly tilted relative to the optical beam path to avoid etalons from spurious reflections of the diode, compare Figure 2. These geometries are efficiently realized using the LCM method, resulting in a monolithic micro-optical bench that offers precise dimensions, high stiffness, and sufficient flatness after thermal processing. The design of the bench keeps wall thicknesses below 
, which leads to short printing times and reduces deformations during thermal post-processing, particularly during the debinding step. The benches are processed following the slurry's standard thermal profile and achieved dimensional precision of 
, flatness of 
 (peak-to-valley) and surface roughness of 
 for the relevant geometries and surfaces. This is well-suited for the presented application and within the tolerances that are compensated by micro-integration. Further improvement is possible for more challenging applications by iterative optimization of the print parameters and thermal processing. For cell heating and temperature stabilization of the overall setup, a Peltier element is placed underneath the frequency reference. A compact, custom-designed PCB, mounted on the reference module's side, is used for simple electrical connection. It connects the references photodiode and the Pt100 sensor to electrical sockets for integration into larger systems and includes a transimpedance amplifier circuit for the photodiode. The ceramic optical frequency reference housing has dimensions of 
 and a mass of 
 including optics. The optical path length of 
, combined with the monolithic micro-optical bench and the high stiffness of alumina results in a mechanically very stable optical system without the need for realignment after integration. These specifications are a substantial improvement in size and weight compared to laboratory spectroscopy setups. Such integrated frequency references could be incorporated into higher level systems like wavemeters, optical spectrum analyzers, or cold atom sensors acting as absolute frequency reference.

Details are in the caption following the image
Figure 3
Open in figure viewer
PowerPoint
Top: CerAMRef module during assembly in the micro-integration setup. The PBS is fixed with UV-curing adhesive after alignment while monitoring the spectroscopy signal. Bottom: microscope image of the printed alumina substrate with geometrical features for pre-aligning and mounting electro-optical components and the rubidium cell.
The frequency reference is assembled with a specialized micro-integration facility, compare Figure 3. Precision actuators adjust up to four components simultaneously with high precision in all six degrees of freedom (
 and 
 stepsize). This allows for precise handling of small and delicate optics, in this application with an edge length of 
. During the micro-integration process, the optical system is operational, allowing for active alignment of the optical components. This is done while monitoring spectroscopy or other relevant reference signals. The components are bonded to the alumina substrate with qualified low-outgassing thermal or UV-curing epoxy adhesive. Further details on the micro-integration procedures, techniques and adhesive qualification are given in ref. [43].

3.2 Performance Demonstration
To assess the performance of the CerAMRef module, we set up a laser system to perform frequency modulation spectroscopy and determine the frequency instability. The experimental setup is illustrated in Figure 4. The CerAMRef is operated at 
 with a micro-integrated, narrow linewidth external-cavity diode laser (ECDL) developed at FBH.[34] To stabilize its temperature, Peltier elements and a thermoelectric cooler controller (TEC, Meerstetter Engineering TEC-1091) are used. The temperature of the CerAMRef module is also controlled by a Peltier element and stabilized at 
. The light from the fiber-coupled ECDL laser passes a fiber-coupled acousto-optical modulator (AOM, G&H Fibre-Q SFO5498), operated at 
 and used for stabilization of the optical power, and is then split with a 50:50 fiber splitter. One part is used for beat-note measurements[44] with a reference system, while the other is coupled to the spectroscopy setup for frequency stabilization. This part interfaces with a fiber-coupled electro-optical phase-modulator (EOM, iXblue NIR-MPX800-LN) that modulates the laser light at a frequency of 
. Another fiber splitter after the EOM splits off 10 % of the light, which is guided to a photodiode (Thorlabs PDA36A2). The photodiode signal is used for power stabilization through a servo loop,[45] operated on a field-programmable gate array (FPGA, Red Pitaya STEMlab 125-14), which is connected to the AOM. The remaining 90 % of the light is connected to the CerAMRef module, compare Figure 2. The signal of the reference's photodiode is subsequently amplified, low-pass filtered and relayed to an FPGA based signal processing system (Liquid Instruments Moku:Pro). Here, the signal is shifted in phase and demodulated with the modulation signal of the EOM, which is also generated by the FPGA. This demodulated signal is used as error signal and internally processed by a servo to generate a control signal, providing feedback to the ECDL's current modulation port and stabilize the lasers frequency to the target transition. The FMS spectrum of CerAMRef is shown in Figure 5, exhibiting 
 and 
 D2 line transitions.

Details are in the caption following the image
Figure 4
Open in figure viewer
PowerPoint
Experimental setup for spectroscopy, laser frequency stabilization and frequency instability measurements of the CerAMRef reference with optical connections (red) and electrical connections for frequency (blue), laser intensity (green) and temperature (orange) stabilization. Further details on the electronic components are provided in the text.
Details are in the caption following the image
Figure 5
Open in figure viewer
PowerPoint
Overlapping Allan deviation of the CerAMRef, calculated from three beat-note time series. The insert displays the FMS spectrum of the CerAMRef using the locked-to transition as reference for the detuning. This spectrum exhibits features from the 
 D2 
 and 
 D2 
 transitions.
The frequency instability of the laser system locked to the CerAMRef is determined from a beat-note with a reference laser system of a transportable quantum gravimeter.[46] It employs modulation-transfer spectroscopy (MTS)[47] of the 
 D2 
 transition. The CerAMRef's system is frequency-locked to the 
 D2 
 crossover transition, which shows the best slope and signal to noise ratio for the lock. For this setting we measure the expected beat-note frequency of 
 including a 
 offset from an AOM in the MTS reference system.[48, 49]

To evaluate the frequency instability of the CerAMRef, the beat-note signal between the locked laser systems is recorded with a frequency counter (Pendulum CNT-91) and analyzed using the overlapping Allan deviation 
.[50, 51] The Allan deviation provides a measure of the relative frequency instability, defined as 
 with frequency fluctuations 
 and optical frequency 
 (here 
), over various averaging times 
. Figure 5 shows the Allan deviation of the beat-note frequency between the two lasers locked to the CerAMRef and the MTS reference, calculated from three dead-time free time series. A linear drift of 
 is subtracted from the data. For averaging times below 
 we find white frequency noise at a level of 
. At 
 averaging time, an overlapping Allan deviation of 
 is achieved, increasing to 
 at 
. The presented stability is typical for a rubidium D2 FMS reference and comparable to previous studies.[52, 53] For averaging times between 
 and 
 the Allan deviation shows an instability well below 
 (
) and for averaging times up to 
, well below 
 (
), perfectly suitable for cold atom applications using magneto-optical traps (MOT).[54, 55]

4 Conclusion 
This work underlines the significant potential of additively manufactured ceramics as key technology for miniaturized functional designs of electro-optical systems and compact quantum technologies. Ceramics are characterized by a high Young's modulus, low density, high temperature stability, and thermal conductivity that ranges from isolating (as for 
) to very high (as for AlN), compare Table 1. They close a technology gap in available materials for additive manufacturing and enable the fabrication of compact, lightweight components and assemblies. As a demonstrator, we have realized a micro-integrated optical frequency reference based on FMS spectroscopy of the rubidium D2 line at 
.

This demonstrator achieves significant improvement in size and weight compared to lab-based setups through optical micro-integration techniques on an additively manufactured alumina substrate. The reported instability (e.g., 
 at 
) is well-suited for atom-referenced quantum technology applications such as sensing or computing. The spectroscopy device consumes 
 of power for the temperature stabilization and photodiode amplifier electronics. With a volume of 
 and mass of 
 for the integrated spectroscopy module, the CerAMRef is one of the smallest fiber-coupled FMS reference to our knowledge. Other miniaturized rubidium D2 line frequency references have been realized,[52, 56, 57] but differ in scope and include the laser diode itself. A comparable fiber-coupled spectroscopy system is commercially available[58] (volume 
), but information on frequency instability for a direct comparison is not published.

Further miniaturization can be achieved by incorporating a MEMS-based vapor cell,[59] a more compact collimator or by integrating electronic circuits and components on the electrically insulating optical bench. The frequency reference can be easily adapted for other wavelengths by switching the atomic species in the vapor cell (e.g., potassium, caesium) and thus address a broad application range. Furthermore, the optical layout of the reference could be extended to integrate a second collimator and optical path, realizing an MTS setup. This could further enhance the stability at longer averaging times, while leading to only a small increase of the system volume.

5 Outlook
Further applications of the technology currently investigated at FBH include compact atom-based magnetometers and atom trapping layouts. Atomic magnetometers use optical excitation of vaporized alkali metal atoms for precise magnetic field detection.[60] Figure 6 shows a miniaturized physics package of an optically pumped magnetometer (OPM), micro-integrated on an additively manufactured ceramic bench. The sensitivity of an OPM strongly depends on the temperature of the alkali vapor,[61] requiring suitable thermal stability and localized heating. Additive manufacturing of ceramics is promising to extend the range of field applications for atomic magnetometers.

Details are in the caption following the image
Figure 6
Open in figure viewer
PowerPoint
Future applications of additive manufactured alumina in quantum technologies: a) depicts an atomic magnetometer featuring a heated caesium vapor cell and micro-integrated optics. In (b), a micro-optical bench is shown (36 
 43 
 10 
), designed for a miniaturized crossed beam optical dipole trap. The transmitted light highlights the lightweight design with internal lattice structure. c) displays an ultra-high vacuum application: an alumina holder with a threefold surface grating for a grating MOT, mounted on a printed aluminum CF40 flange. The electrically isolating and thermally stable ceramic enables easy integration of restively heated dispensers and planar magnetic structures.
An optical bench for a micro-integrated crossed-beam optical dipole trap[43, 62] is depicted in Figure 6. This trapping scheme can be used for ultra-cold atom applications.[63] The design features a lightweight structure with various mounting geometries and internal lattice structures, benefiting from the high stiffness of alumina. Additionally, Figure 6 depicts a printed ceramic holder for a threefold diffraction surface grating used in a grating magneto-optical trap (gMOT).[64] This holder, attached to a printed aluminum CF40 flange with an electrical feedthrough, utilizes the vacuum compatibility, thermal stability, and electrical insulation of 
. It simplifies the electrical connections for heating a rubidium dispenser and accommodates planar electrical structures for magnetic field generation.[65] Other ceramic materials, like AlN, can address further quantum technology applications, such as high-power diode laser systems requiring advanced thermal management.

R&D applications of additively manufactured ceramics using vat photo-polymerization are continually evolving and future innovations and improvements of the printing technology and materials are to be expected. One current development is multi-material printing[66] which combines different ceramics (e.g., 
 and 
) and ceramics with metals in a single print. These combinations can be configured layer-by-layer, within individual layers, or as functionally graded materials, allowing for tailored mechanical and thermal properties. A promising aspect is the integration of electric conductors, enabling components with embedded magnetic field generation or heating elements, leading to a further system integration and reducing the number of components and production steps.
