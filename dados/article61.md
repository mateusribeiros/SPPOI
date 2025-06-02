Title: Kinematic Compensation Algorithm for Reducing Errors in a Closed-Loop Manufacturing System

ABSTRACT During the manufacturing process of a piece, different factors influence the process so
that errors of a systematic and random nature are added, affecting both the dimensions and the final
geometry. The strategy presented in this research seeks to identify, monitor, and computationally control
the errors arising from the arrangement of the actuators that can be derived from errors in assembly,
wear of the components, and thermal deformations. This article proposes an algorithm to prevent and
correct geometric and dimensional errors in manufacturing parts as a compensation strategy. The algorithm
obtains the references of the manufacturing process and estimates the process’s deviation, calculating the
manufactured part’s error concerning the projected piece. Error compensation is performed through reference
points that alter the location of the target points in the opposite direction to the resulting error to nullify
it kinematically. The validation of the strategy is carried out through the computational implementation
of kinematic algorithms of a machine tool with a Cartesian structure of two degrees of freedom on
which position and orientation errors are induced. The presented results allow for verifying the proposed
algorithm’s effectiveness against tests with significant errors. The compensation strategy presented allows
projecting this algorithm as an online software calibration method, reducing the number of stops due to
mechanical maintenance of the CNC machine and making closed-loop manufacturing possible with realtime compensation.
INDEX TERMS Advanced manufacturing, closed-loop manufacturing, STEP-NC, error compensation,
digital manufacturing.
I. INTRODUCTION
Within the demands placed by the digital era on manufacturing processes, there is a constant challenge to obtain
sustainable manufacturing. Sustainable manufacturing is
strongly related to smart manufacturing, where methods
can automatically decide the course of their operations.
In this exposed scenario of integration and interoperability of
systems, the concept of closed-loop manufacturing, known
as CLM, takes on great relevance; more than a concept, it is a
method that enables data feedback to CAx (Computer-aided
technologies) systems that can continuously influence and
improve the manufacturing process [1]. The feedback data
can be both information acquired from the manufacturing
conditions and dimensional and geometric measurement
results of already manufactured parts [2].
The variability and uncertainty of manufacturing processes
impair the balance between the quality and productivity of
the fabrication. The dimensional and geometric inspection
of manufactured parts can solve this problem, since the data
obtained provide essential information about how they were
manufactured and the sources of errors inherited from the
machine tool [3]. The objective of analyzing the inspection
data is to reduce the uncertainty values and maintain
the geometric and dimensional characteristics within the
projected specifications in the design [4].

Analyzing the dimensional and geometric inspection data
will allow for obtaining an approximate error model [5].
The geometric error in machine tools directly influences the
position of the tool, producing dimensional and geometric
defects in manufacturing [6]. There are several ways to
analyze when solving the problem; The first option is to carry
out a physical intervention on the machine, which means
stopping the operation and generating other complications.
Modifying the design and adjusting tolerances in the project
of the part to be manufactured could be another feasible
option; however, the traceability of the project is lost [7].
Another option is to compensate for the deviation directly on
the machine’s control system, which is more feasible with an
open system [8].
The integration architecture is necessary for manufacturing
systems to obtain autonomous processes with a physical connection of the elements, bidirectional communication under
the same data structure, and disturbance control by expert
systems. The architecture that operates with a closed-loop
manufacturing integrates the different phases of the product
life cycle: design, manufacturing, and measurement through
a neutral data structure, extensible and interpretable by
other technologies associated with the various stages of
the life cycle of the product [9]. An architecture in CLM
allows for the optimization of the process and promotes
sustainable systems [10].The execution requirements change
progressively in this digital age, but it is still essential to
implement integration and maintain interoperability between
CAx systems [11].
This document proposes a feedback control architecture
with measurement data to compensate for errors detected
in manufacturing algorithmically. Section II presents a brief
literature overview to contextualize the contribution as a compensation strategy operating in closed-loop manufacturing.
Section III presents the operation architecture and the feedback strategy. Section IV contends the error compensation
method used to calculate the deviation. Section V presents
a typical case study to check the flow of information within
the architecture. Finally, section VI presents the conclusions
and suggestions for future studies.
II. LITERATURE OVERVIEW
Thinking about contributions and developments for the
future of manufacturing consists of envisioning efficient
processes that operate with a balance between productivity
and quality while simultaneously meeting specific needs in an
increasingly sustainable way [12]. Analyzing the data of the
manufacturing process and providing feedback on the results
provides us with knowledge of manufacturing conditions,
generating helpful information to make decisions and propose
strategies to improve manufacturing conditions [13], [14].
The search for recent information found different research
papers that address this line and present a contribution. Works
such as [15] and [16] address the concept of closed-loop
manufacturing, used as a generalized solution to keep under
control the parameters that can affect the manufacturing
process. The notable difference in each job consists of how
the data flows between the systems involved and how the
integration of the systems occurs. The ISO10303 standard
can support the Integration of CAD/CAPP/CAIP/CAM/CAI
systems as a basis for exchanging information through a
neutral file that works with homogenized entities for different
contexts within the life cycle of a product [17], [18]. This is
demonstrated by research such as [19] and [20].
The main problem with automating decision-making in
closed-loop manufacturing lies in the integration and interoperability of measurement systems. They are challenging to
automate, require human intervention, and the technologies
used are only partially accessible. Mears et al. [21] present
a review of the use of coordinate measuring machines in
machining processes. The investigation shows technological
advances of CMM, as well as integration strategies of
measurement systems in machine tools. Some problems
resulting from the integration of the systems are reported,
such as the case of integrating the CMM directly with the
machine tool related to the measurement and calibration error
due to the difference between the inspection reference system
and the reference of the process of machining on the machine,
causing CNC machine errors to affect inspection [22].
Gaha et al. [23] pose challenges to using dimensional
measurement in digital environments. These challenges are
being addressed through simulation, error compensation,
rapid calibration techniques, and the incorporation of new
detection technologies. It also presents a set of functionalities
and opportunities for measurement systems within the
industry 4.0 paradigm.
According to Saif et al. [24] Closed-loop Inspection
(CLIM) and computer-assisted inspection planning (CAIP)
have become relevant and have become a method to improve
the product. The work presents a systematic review of the
literature that analyzes articles on inspection and using
CLIM together with CNC machines. The results of this
study provide a taxonomy and definition in terms of and
characteristics of this emerging technology.
During manufacturing, different factors interact so that
errors of a different nature (static, dynamic, and progressive)
are added to the process. Different investigations address
this line, managing to classify the geometric errors in parts
manufactured in CNC machining centers according to their
nature: systematic, progressive, and random. The geometric
errors in the parts processed when machining with CNC
machines can be attributed to four sources of error: machine
tool, NC programming, machining process, and other factors.
Zhen et al. [25] relate how the dynamic limitations of the
CNC machine tool lead to errors during its operation and
affect the precision of the machining of the parts. The paper
highlights the importance of reducing errors and presents
a review of the methods focused on this line, emphasizing
advantages and disadvantages. The article suggests future
studies that minimize contouring errors in parts machined
with a CNC machine.
FIGURE 1. Closed-loop manufacturing architecture.
In the search for research that addresses architectures for
closed-loop manufacturing, there is a notorious tendency
to use solutions that adhere to the ISO10303 standard
known as STEP-NC [26]. Works developed in this line [27],
[28], [29] describe strategies to converge an extensible
and open neutral solution through the standard. The ISO
10303 standard, also known as STEP (Standard for the
Exchange of Product model data), provides a mechanism for
structuring information that can be used within a closed-loop
manufacturing architecture [30]. The standard defines a
structure within the object-oriented perspective for data
representation and information exchange between systems
involved in the life cycle of a product [31], [32]. The concept
of features is considered within the standard as an integral
component used within the different possible contexts such
as design, manufacturing, and measurement; this concept is
syntactically and semantically homogenized between each
of the processes involved in the life cycle of production of
a piece [33], [34]. The STEP standard provides a neutral
format for defining product data and exchanging information
between processes [35].
Hu et al. [16] present an architecture of a STEP-NC
compliant closed-loop robot machining system, including
its function model and information stream. The closed-loop
robot machining system was implemented based on an
open STEP-NC interpreter that interprets the high-level
information in STEP-NC directly to reduce the machining
robot programming time.
III. INTEGRATED INSPECTION SYSTEM
This section describes the closed-loop inspection architecture
and the feedback strategy to compensate for manufacturing
errors. As a requirement, an interoperable architecture is
defined with a bidirectional data flow and integrated with
the different CAD/CAPP/CAIP/CAM/C NC/CAI systems,
using a neutral file STEP (Standard for the Exchange of
Product model) with support for layers: application, logic,
and physics.
Fig. 1 shows the study scenario, and the scope of
the architecture presented. The physical configuration and
the data flow between the CAx systems involved in the
compensation strategy are present.
The encoding in a STEP file of the toolpath of the
CNC machine is carried out through a framework developed
in JAVA to read, write, and update files compatible with
the ISO10303 standard. The framework generates a neutral
STEP interchange file in AP238 format that contains the
project, main Workplan, and Workingstep with paths for
facing operation. Other additional information relevant to
the manufacturing process is included through STEP-NC
Machine after importing the generated step file into the
framework. Fig. 2 shows the working environment of the
STE-NC Machine; the project structure is shown on the left
panel.
A. FRAMEWORK FOR STEP FILE ENCODING
This section explains how the proposed method for error
compensation in manufacturing processes adheres to the ISO
10303 standard, STEP (Standard for the Exchange of Product
model data). A Model-View-Controller (MVC) architecture
was used to develop the STEP interpreter. This architecture
is supported by three main logical components: the model,
the view, and the controller. Each of these components
is designed to handle specific development aspects of an
application. The model contains the dynamic data structure
of the application, which is the core where the knowledge of
FIGURE 2. Step file project for manufacturing environment.
FIGURE 3. Model-view-controller architecture for the development of the
STEP interpreter.
the STEP standard is necessary for application development.
The controller manages the program’s execution, creates the
project, receives events, implements the actions to supply
data to the model, and manages the creation of the STEP
interchange file. The view is the user interface layer. Fig. 3
shows the sequential structure of the file carried by the
execution thread, in which an SDAI session is created,
manages the repository, and encodes the STEP exchange file
with the information generated during the execution of the
program.
Integrating information within the Closed-loop inspection
requires a robust and interoperable data structure to be
compatible with the different CAx systems. ISO 10303 has
a description method in EXPRESS language specified in
ISO 10303-11 that facilitates the interpretation of information
models and application protocols. The EXPRESS language
defines in a neutral and technology-independent manner a
logical structure, restrictions, rules, functions, and procedures
for each entity, which facilitate the development of applications with a diverse context of use.
FIGURE 4. Approach for Interoperable data access, adherent to STEP
standard.
JSDAI is an Application Programming Interface (API)
for read-write and run-time manipulation of object-oriented
data defined by an EXPRESS data model. The JSDAI tools
enable the use of data structures modeled in the standard
data element type language EXPRESS (ISO 10303-11), PLIB
(ISO 13584), and IEC61360. JSDAI can store and exchange
data with STEP applications in various forms, such as STEP
XML - ISO 10303-21 (part 21) and STEP XML - ISO 10303-
28 STEP XML, among other formats. JSDAI can organize
and control application data, such as physical separation
in repositories and logical grouping between instances and
schemas.
The Fig. 4 shows a data flow scheme that supports the
integration of information in CAx systems and the pillars
supporting this application’s computational development.
Through the EXPRESS schemes provided by ISO 10303,
a series of application protocols support each phase of the
life cycle of a CAD/CAPP/CAIP/CAM/CAI product. The
protocols share an entity but are used in different contexts.
The developed framework has the function of reading,
writing, and updating values of these entities according to
the results obtained in the compensation strategy to modify
the original design executed by the CNC and compensate for
manufacturing errors. After modifying the sensitive entities
with tool positioning information, a new STEP file is created
in p21 format, which contains the necessary actions to
compensate for the design that allows compliance with the
quality standards according to the capacity of the process.
B. DIMENSIONAL AND GEOMETRIC INSPECTION PLAN
Nx-Siemens provides an environment to plan the dimensional
and geometric inspection of the part. The objective is to
simulate the measurement of the project and generate a
program for a measurement environment that identifies the
design specifications and their tolerances, the selection of
FIGURE 5. Inspection program execution.
suitable touch probes, the generation of trajectories without
collisions, and the adequate programming of the order
in which they are executed those trajectories. When the
simulations are carried out, and the configurations applied
in the CAIP are approved, a DMIS output file is generated
to perform the measurement process. Fig. 5 shows the
inspection planning process performed in NX-Siemens.
NX™ CMM inspection programming software exports the
inspection program in the industry standard Dimensional
Measurement Interface Specification (DMIS) format.
The developed inspection plane presented in this section
enables obtaining valid measurement results for the error
compensation strategy; the following section details how the
acquired data is used to measure dimensional and geometric
features.
IV. ERROR COMPENSATION METHOD
This section presents the development of an algorithm to
compensate for manufacturing errors derived from assembly
problems or wear in the actuators of a Computer numerically
controlled (CNC) machine. The compensation algorithm
uses position references extracted from the Computer Aided
Manufacturing (CAM) system to determine the deviation
produced in manufacturing parts. With the error result
obtained, the algorithm generates a system compensation
to correct the perpendicularity and parallelism errors. The
compensation acts on the kinematic model of the machine,
redefining the location of the manufacturing system actuators
and preventing the actual deviation from affecting the
manufacturing. Reference compensation consists of altering
the location of the target points in the opposite direction
to the resulting error to cancel it. The compensation is
carried out through the kinematic algorithms that intervene
in controlling a CNC machine with two degrees of freedom,
using the differences in position and the errors in orientation.
It verifies the compensation of the algorithm exposed in
this article through tests with significant parallelism and
perpendicularity errors. The results allow projecting this
algorithm as an online software calibration method, reducing
the number of stops for mechanical maintenance of the CNC
machine.
For this research, a CNC machine hybrid was built with
a Cartesian configuration and open control architecture,
designed for applications in machining, additive manufacturing, and laser cutting processes that allow validating the
error compensation strategy within a safe environment and
with the possibility of including disturbances. to the process.
The Fig. 6 shows the most essential components of the CNC
machine.
The Cartesian configuration has three prismatic actuators;
in machine tools, these actuators determine the trajectories
and the degrees of freedom for manufacturing parts. A model
is proposed to estimate the errors produced in manufacturing
using machine tools with a Cartesian configuration. In this
model, the linear actuators are located at a point other
than the origin of the reference system. Fig. 7 (b) shows a
representation of a CNC machine, highlighting two of its
three degrees of freedom determined by the linear actuators
that define the path in the X-axis and Y -axis.
The representation model is built for the machine shown
in Fig. 7 (a), for which the analysis is carried out using a
Euclidean coordinate system as a reference. All machines or
FIGURE 6. Experimental CNC machine.
movement systems have differences between the projected
movement and the actual movement they perform due to the
assembly of their actuators.
In the assembly, a fictitious error was made so that the
actuators are not entirely perpendicular, and their location
does not coincide with the origin of the reference system.
The model will consider that the actuators have an orientation
error. Fig. 7 (b) shows a representation of the actual location
of the actuators in a CNC machine, representing the actuators
in their initial position. It must be taken into account that
the CNC machine is to be modeled as a serial configuration,
where the first joint corresponds to the X-axis and the second
to the Y -axis.
Ideally, the machine would work according to the XY
system defined by the unit vectors i and j. However, in the
model proposed for analysis, the actuator that defines the
trajectory on the X-axis is located in the position defined by
the vector Oxr; the unit vector ir determines its orientation.
Analogously, the Y -axis actuator is located at the position
defined by the vector Oyr, and the unit vector jr defines its
orientation. The components of these vectors are illustrated
below in Eq. (1).
Oxr =

Oxri
Oxrj
; Oyr =

Oyri
Oyrj
;ir =

irx
iry
;jr =

jrx
jry
; (1)
Since the vectors ir and jr are not perpendicular, using
a vector analysis representing non-orthogonal systems is
necessary. The position error of the actuators makes it
necessary to generate a new reference point that can be
considered the origin of the non-orthogonal coordinate
system. The reference point of the proposed model is
established at the projection intersection of the X and
Y -axis, determined by the current location of the actuators
(represented through a circle in Fig. 7.
The difference between the positions of the actuators Oyr
and Oxr define the vector 1Or (see Eq. (2)). On the other
hand, 1Or
is XY ’s base of the coordinate system.
1Or = Oyr − Oxr (2)
The intersection point of the actuator’s projected axes is
calculated by expressing Eq. (2) in terms of the unit vectors
ir and jr
, as shown in Eq. (3). Note that mx is the distance
between the origin of the X-axis actuator and the point of
intersection. Similarly, my is the distance of the other actuator
concerning the same point.
−mx ir + myjr = 1Or (3)
Equation 3 can be expanded by expressing the components
of the vectorsir
, jr
, and 1Or concerning the reference system
XY . See Eq. (4).
−mx

irx
iry
+ my

jrx
jry
=

1Orx
1Ory
(4)
Eq. (4) can be rewritten to express the equation as a system
of matrix equations. Note that the unknown variables are mx
and my as expressed in Eq.(5).

−irx jrx
−iry jry mx
my

=

1Orx
1Ory
(5)
By generating the inverse matrix of dimensions 2×2 on the
right side of the equality of Eq. (5), through the multiplication
of both sides by the inverse matrix, we arrive at Eq. (6), which
expresses the solution of the variables mx and my. These
variables fully define the intersection point of the actuators’
axes.

mx
my

=

−irx jrx
−iry jry−1 
1Orx
1Ory
(6)
The next step is to calculate the direct kinematics of the
structure, which consists of determining the values of the
position of the final effector of the CNC machine defined by
the vector P (see Eq. (8)) concerning the coordinate system
XY from the known coordinates of the actuators and defined
by the vector Pr
, see Eq. (7).
Pr =

Pir
Pjr
(7)
P =

Pi
Pj

(8)
Fig. 8 illustrates the relationship between the position
of the end effector concerning the actuators and the XY
coordinate system. Fig. 8 shows that the orientation error
in the actuators will generate perpendicularity errors in the
manufactured parts. The fact that the actuators have zero error
due to not starting at the exact origin reduces the machine’s
workspace. Fig. 8 represents the structure of a CNC machine
whose actuator that defines the path on the X-axis is fixed to
the base, and the Y-axis actuator is serially connected to the
previous one.
Fig. 8 defines the strategy to relate the position of the end
effector and the XY coordinate system. The strategy consists
of moving from the XY system origin along the vector Oxr
to the origin of the X-axis actuator. Next, a translation of
magnitude Pir is performed along the direction ir (defined
by the orientation of the actuator). Subsequently, it moves in
FIGURE 7. The actual location of the actuators in a CNC machine: (a) Cartesian configuration machine;
(b) Geometric representation.
FIGURE 8. The Kinematic diagram relates the actuators’ position
concerning a CNC machine’s XY coordinate system.
the direction and magnitude of 1Or
, where this displacement
corresponds to the position error of the Y -axis actuator to
the origin of the X-axis actuator. After that, move in the
direction of the second actuator defined by jr
, a distance equal
to Pjr. This magnitude corresponds to the displacement of the
actuator of the Y axis. This path can be represented by Eq.(9).
P = Oxr + irPir + 1Or + jrPjr (9)
Eq.(9) corresponds to the direct kinematic model of the
machine according to its Cartesian configuration. This model
allows calculating or simulating the actual position reached
by the end effector or tools when each actuator’s joint
coordinates and the position and orientation errors are known.
In constructing the kinematic compensation algorithm for
reducing errors in the CNC machine, the inverse kinematic
model of the previously described Cartesian configuration
is proposed as the basis of the solution. This model allows
calculating the correct joint coordinates to correct errors in
the location of the actuators. Eq. (9) can be rewritten in the
form expressed in Eq. (10) to organize the terms of the joint
coordinates on the left side of the equation.
irPir + jrPjr = V1 (10)
where:
V1 = P − Oxr − 1Or (11)
Equation 10 can be expressed in a matrix as equation 12,
where all terms are defined based on the XY frame of
reference.

irxPir + jrxPjr
iryPir + jryPjr 
=

V1x
V1y

(12)
Equation 12 can be rearranged as the product of a 2 ×
2 matrix representing a non-orthogonal transformation matrix
that multiplies the vector of actuator coordinates to obtain
vector V1. See equation 13.

irx jrx
iry jry Pir
Pjr

=

V1x
V1y

(13)
Once the equation is rearranged, it is rewritten in its
compact form, as illustrated in equation 14.

ir
jr

Pr = P − Oxr − 1Or (14)
Finally, utilizing its inverse, we pass the non-orthogonal
transformation matrix to the right side of the equation. With
this, the inverse kinematic model of the machine represented
in Eq. (15) is obtained. Note that this model has the reference
positions of the tool as input parameters and considers the
errors in orientation and the actuator’s position. This equation
will allow the correct coordinates of the actuators to be
calculated to reduce manufacturing errors.
Pr =

ir
jr
−1
[P − Oxr − 1Or] (15)

FIGURE 9. Measurement graph for the variable: (a) Chart inspection data; (b) Distance histogram.
A. ERROR CALCULATION
Product dimensional management is necessary to balance productivity and quality for industrial manufacturing
processes. The closed-loop inspection presented in this
document brings the process closer to the ideal product
quality while maintaining high productivity. The relevant
issue to be resolved within this case study is to avoid
overestimated dimensional specifications in the design since
they lead to manufacturing problems that are difficult to
solve because they require greater capacities in machines
and adjusted processes to meet the demanding ones. In other
words, parts with demanding specifications are better quality
but more challenging to manufacture, affecting productivity.
Another aspect of this problem is that relaxed geometric, and
dimensional specifications increase productivity but sacrifice
quality in the final result. The closed-loop inspection architecture seeks a zone or interval of dimensional compliance
that balances productivity and quality, seeking continuous
process improvement.
The central limit theorem is an appropriate method to
estimate the behavior of random variables as it happens
in manufacturing parts. The theorem states that when the
size of a sample and the number of parts manufactured
is large enough, the distribution of the mean follows
an approximately normal or Gaussian distribution. This
distribution causes samples to accumulate around the mean,
and the pieces with values far from the mean are at their
extremes. This distribution is what we call the confidence
interval for geometric conformity. Operating manufacturing
processes with dimensional conformity fosters a robust
system against dimensional variations in manufacturing and
correct control of errors in production processes.
The inspection results obtained through a part production
follow-up are used for this analysis. The dimensional inspection was performed on a Mitutoyo Crysta-Plus M 574 CMM,
and the results exported from MeasurLink are used to identify
the causes of particular variations within the process. The
measurement is made on the critical characteristics that must
be monitored and a statistical study that allows relating the
errors and the causes that cause them. It also determines
the capacity of the machine to manufacture these types of
parts. Measurements are made on two linear features of the
piece that can provide relevant information about the process.
These characteristics represent the functional characteristics
of the workpiece under control.
In this case, a statistical study is carried out to relate the
errors with the causes that cause them. The applied process
also determines the capacity of the machine to manufacture
this type of part. Measurements are made on two controlled
features of the part that can provide relevant information
about the process.
The case of process control is defined between the limits
of 6σ. The variability measure is associated with considering
the Gaussian result where the µ ± 3 σ range includes
approximately 99.7% of the characteristic values. The range
limits define natural tolerances as intrinsic to the process. The
Lower Specification Limit (LSL) and Upper Specification
Limit (USL) are considered to define the range of permissible
values of the variables that are forced. The objective defined
by the mean value µ will be centered on the specification
limits. The capability index (Cp) is defined as:
Cp = USL − LSL/6σ (16)
ToleranceNatural = (UCLx¯ − LCLx¯)
√
n (17)
where,
UCLx¯
: Upper Control Limit.
LCLx¯
: Lower Control Limit.
n: Sample size or number of observations.
A2 :Constant to adjust the control limit based on
expected variability.
TABLE 1. Quality control references.
TABLE 2. Manufacturing errors found with inspection results.
If µ and σ are known, then the construction of the graph
of media is immediate from its definition:
UCLx¯ = ¯x + A2 ∗ R¯ (18)
LCLx¯ = ¯x − A2 ∗ R¯ (19)
where,
A2: Constant to adjust the control limit based on
expected variability.
x¯ : Mean of the process subgroups.
R¯: Average range of process subgroups.
Figure 9 (a) presents a graphical result of means. An analysis of the results is necessary to obtain more information on
the behavior of the process. Indeed, from the dispersion of the
sample values, it is possible to estimate the dispersion of the
process and follow the evolution. The standard deviation σ
measures the dispersion of the values of a population, and the
most frequently used sample estimators are the path R (Graph
R) and the sample standard deviation S (Graph S).
Table 1 presents a summary of the measurement result
returned by Measurlink that presents standard deviation (σ),
natural process variability (6σ), and process capability (Cp).
With the parameters presented in Table 1, it is possible to
obtain the errors associated with the part. It is determined that
the systematic error is constant in the process and is present
in the same way in each of the measurements made on the
feature. The leading cause of systematic errors in the process
is attributed to defects in the manufacturing machine. Eq.
(20) is used to calculate a systematic error value. The result
obtained for the systematic error is presented in Table 2.
ErrorSis = Vi − X¯
i (20)
where Vi
: Desired value X¯
i
: Mean
FIGURE 10. Linear regression relation between valor & measurement
sample.
The value for the manufacturing error is obtained using
the root mean square error definition with the variability
values of the natural process (6σ).To characterize the error,
we determine the angle associated with the displacement of
each actuator or axis of the machine using the vestigial data
found in part. The offset angle is calculated by performing a
linear regression on the standard distribution data to obtain
a line correlating with the measurement result values. The
equation obtained for each feature will describe a slight
incline calculated to determine the offset angle. The data used
in this procedure is the output data generated by the Mitutoyo
Measurlink software.
Fig. 9 shows the graphical result thrown for the Dx feature.
The information on each feature that was manufactured in
TABLE 3. Parameters of the errors in position and orientation of the actuators.
FIGURE 11. Analysis of the trajectories generated by applying and without applying the kinematic compensation
algorithm.
the disposition of a machine tool axis is extracted. Fig. 10
shows the result of the linear regression procedure for Feature
Dx. Table 2 summarizes the result for each feature analyzed;
it presents the deduced equation and the displacement angle
concerning an axis of the machine. The results obtained allow
for making corrective maintenance decisions that improve the
part’s quality.
The presented procedure shows a dominant error, and it is
possible to estimate its deviation. The processed data sample
contains traces of systematic errors due to machine problems.
FIGURE 12. Quantitative analysis of the trajectories generated by the CNC applying and without applying the kinematic
compensation algorithm.
The scenario introduces an error compensation algorithm
that allows building pieces to reduce the variability detected.
The objective is to obtain dimensional conformity that favors
the balance between productivity and quality. This strategy
controls the process and algorithmically compensates for
identified errors.
V. TYPICAL CASE: CIRCULARITY ERROR COMPENSATION
The proposed algorithm is verified by constructing a CNC
machine model with two degrees of freedom in a simulation
environment. The experiment introduces significant errors
in both position and orientation in the two actuators that
define the trajectory on the X-axis and the Y-axis. After
causing errors in the machine’s configuration assembly,
a circular operating path is created. Subsequently, the
simulations were carried out using traditional kinematic
calculations to generate the CNC’s trajectory. Finally, the
new references were generated using inverse kinematics with
the compensation algorithm. Fig. 11 shows some of the tests
performed; in these tests, it can be seen how the orientation
errors of the actuators were varied (see parameters in Table 3,
which is why a considerable error of perpendicularity is
generated).
In Fig. 11 (a), a schematic of a Cartesian configuration
is illustrated whose actuator that defines the path on the
X-axis has an orientation error of 10◦
, and the actuator
that defines the path on the Y-axis has an error of 15◦
(measured clockwise). Note that the two actuators have a
significant phase shift concerning the initial position; These
high-magnitude fictitious errors were defined to identify
traces of the manufacturing process. By defining a circular
path and observing the results obtained, the effectiveness
of the error compensation strategy can be corroborated
using the proposed algorithm. Fig. 11 shows the trajectories
obtained by following a sequence with references provided
by the computerized numerical control; the result obtained
is an elliptical path when projecting a circular path (see
gray ellipse). It is observed that there is a considerable
phase shift in the resulting position concerning the projected
one; note that it is further to the right of the projected
point on the X-axis and has a greater magnitude in the
position on the Y-axis. Fig. 12 (a) shows the numerical
values of the trajectories of the two actuators with and
without compensation and the trajectories with compensated
references.
The kinematic compensation algorithm to correct the
error generates new references (Ellipse of black color in
interrupted line, Fig. 11). The offset references generated
by the algorithm are characterized by being located in the
opposite direction to the initial offset, seeking to prevent
manufacturing error. Similarly, the proposed algorithm generates eccentric references where the ellipse’s central axis
corresponds to the ellipse’s minor axis resulting from the
traditional method, allowing for suppressing the eccentricity
errors derived from the location errors of the actuators.
Fig. 11 (b) shows the result obtained for an error variation
of 15◦
(measured clockwise) on the actuator that defines the
trajectory on the Y-axis. Fig. 12 (b) shows the numerical
values of the trajectories of the two actuators with and
without compensation, and the trajectories with compensated
references. Fig. 11 (c) presents the result for position errors
in the actuators concerning the origin. Orientation errors
provide an environment for experimentation of the actuators,
causing variations more or less than 90Â◦
, which is the ideal
condition. In all the tests, it is observed that the algorithm
generates and modifies the path references to compensate
for the machine error. Fig. 12 (c) shows the numerical
values of the trajectories of the two actuators with and
without compensation, and the trajectories with compensated
references.
In Fig. 12, it is possible to graphically observe the behavior
of the actuators with the numerical values adopted in each
of the trajectories. The graphic results of both compensated
trajectories and those produced by assembly errors are shown
to analyze the strategy and compare. It can be seen how the
compensated trajectory references are acting in the opposite
direction to the original trajectory, with assembly errors in all
cases.
The proposed kinematic compensation algorithm is
essential to the manufacturing error correction strategy.
It demonstrates that with closed-loop manufacturing control,
it is possible to reduce manufacturing uncertainties caused
by assembly problems and machine structure errors. The
algorithm generates new references for the trajectory in
proportion to the acting error, which allows manufacturing
uncertainties to be drastically reduced without the machine’s
need for intervention or manual recalibration. The proposed
algorithm can be used to prepare the machine tool as a
form of recalibration via software, enabling the possibility of
making changes online during system operation, increasing
production times, reducing machine stops, and maintaining
geometric and dimensional control of the manufactured parts.
VI. CONCLUSION
The flow of information in the architecture presented is
supported by the neutral STEP exchange files that meet
the communication requirements between the measurement
and manufacturing processes, meeting the demands for
integration and interoperability with technologies adhering to
the perspective of Industry 4.0.
The concepts of error control documented and studied
in statistical processes have applications within closedloop manufacturing. The architecture is validated within a
case study that begins with determining the machine tool’s
geometric error, directly influencing geometric errors when
manufacturing the feature.
The article presents the error compensation strategy
through an algorithm that modifies the joint positions of the
machine to correct the error without performing a mechanical
intervention on the machine. This strategy can compensate
for systematic and progressive errors in machine tools and is
projected to be used in real-time control by enabling digital
twin definitions.
This research promotes technological solutions based
on exchange-neutral files that guarantee integration and
interoperability. A computational implementation method
adhering to the STEP standard was developed. The solution
obtained is specific and applied within the manufacturing
context, but it allows knowing and interpreting the standard
to develop new solutions that increase functionalities.
The dimensional and geometric inspection processes
become relevant within the digital context, especially in collecting and constructing knowledge; Technological advances
in measurement systems seek to automate the process, reduce
human involvement and minimize errors produced in the
measurement phase. The closed-loop inspection strategy
requires solutions promoting integration, maintaining interoperability, interpreting results, associating manufacturing
errors with process causes, establishing automatic error
compensation strategies, and optimizing the measurement
process.
In future work, the Closed Loop Machining methodology
should be validated using a machining center with several
years of use, exhibiting an adequate level of wear in the
actuators/joints, to validate the proposed method by identifying potential gains through the reduction of positioning
errors and improvement in the quality of the machined
part, thus comparing the results without compensation and
with error compensation on an industrial machine. In these
experiments, the effect of different actuator speeds should
be considered to observe the behavior of the error and its
compensation.
Automatic feature recognition, generation of optimal
paths, kinematic control, and configuration of process variables can be controlled algorithmically to improve process
efficiency. Hybrid fabrication structures, including real-time
inspection within fabrication, can make error control more
flexible.

