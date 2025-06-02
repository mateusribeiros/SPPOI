Title: Advancing Interoperable IoT-Based Access
Control Systems: A Unified Security Approach
in Diverse Environments

ABSTRACT The convergence of the Internet of Things (IoT) and the construction industry represents a
potent opportunity to fundamentally redefine the processes of constructing and maintaining buildings. The
integration of IoT technology has the potential to revolutionize building safety, efficiency, and sustainability,
offering a promising avenue for innovation and advancement within the industry. In this work, we propose
an innovative design and implementation of an interoperable physical access control IoT-based system that
can be easily integrated with existing access control security systems and used in various environments such
as offices, homes, and public buildings. Based on our developed and implemented physical access control
IoT-based system, we identified several challenges in the current state of access control systems. These challenges include difficulties in integrating different security systems, the absence of interoperable standards,
and the need for further research to enhance the scalability and performance of such systems.
INDEX TERMS Internet of Things (IoT), interoperability, physical access control, electronics, smart
devices, wireless communication, software design.

I. INTRODUCTION
The safety of occupants and the building itself is paramount
in both public and private buildings. Of the various security
systems used for building security, door access control is
significant. Door access control is a physical security system
that restricts access to specific individuals and maintains
records of access. With the increasing potential of IoT technology, concerns regarding interoperability and data sharing
have become significant issues, especially for physical access
control systems relying on IoT technology. In particular, door
access control systems that depend on IoT technology face
significant challenges in achieving interoperability due to the
absence of a uniform standard. Integrating different security systems can be challenging, resulting in inefficiencies
and increased costs. It is necessary to develop and adopt
interoperable standards that allow for the seamless integration
of different security systems. The adoption of such standards
can ensure that physical access control systems based on IoT
technology can interoperate and communicate effectively,
irrespective of the manufacturer or type of security system.
By addressing interoperability concerns, door access control systems can enhance building security and safeguard
occupants and structure by making unauthorized access more
difficult. By establishing a centralized control and monitoring, it is easier to manage access permissions, track entry and
exit logs, and respond to security incidents in real-time.
In this study, we present an IoT-based access control system that stands at the forefront of technological innovation in
security and interoperability. The contributions of this study
are outlined as follows:
• Our research’s core contribution lies in the development
and implementation of a unique system that seamlessly integrates with existing security frameworks while
introducing cutting-edge features, including the novel
use of rolling QR codes for dynamic authentication and
enhanced security. Rolling QR codes ensure access is
granted only within a specific timeframe, adding an extra
layer of security.
• Secondly, the proposed system not only elevates the
standard of physical access control but also addresses
critical challenges in the IoT realm, such as the lack of
interoperable standards and the complexities of integrating diverse security systems.
• Thirdly, the developed system showcases exceptional
advancement in software and hardware integration, setting a new benchmark for flexibility, scalability, and
efficiency in access control systems. Designing software
components that enable robust and efficient communication and data processing, we have enhanced the proposed
system’s ability to manage diverse security protocols
and data formats.
• Finally, the innovative hardware design, characterized
by the system’s compatibility with both traditional and
modern access control mechanisms, exemplifies our
commitment to bridging the gap between legacy systems
and future technologies.
This paper outlines a blueprint for future developments and
a solid foundation for further exploration and enhancement
of access control systems. The implications of our work
extend beyond the immediate application, providing valuable
insights and methodologies that can be applied across various
domains where security, interoperability, and technological
integration are paramount.
This paper is organized as follows: Section II delves into
the existing literature and the current state of access control
systems, setting the stage for our contributions. Section III
describes the research design and data collection methods
employed in our study, providing the foundation for our
experimental approach. In section V we detail the innovative aspects of our system, both in hardware and software,
showcasing the novel features that distinguish our work from
existing solutions. section V offers an in-depth analysis of the
communication protocols vital to ensuring system security
and efficacy. Following this, section VI outlines the various strategies and techniques utilized to achieve seamless
system integration. section VII identifies and discusses the
challenges and obstacles encountered in achieving interoperability within the scope of enterprise integration. The critical
evaluation of our system is presented in section VIII where we
assess the system against predetermined criteria. In section IX
we dissect the outcomes of our experimental implementation,
providing a comprehensive analysis of the system’s performance and integration capabilities. The paper concludes with
section X where we summarize our findings and discuss the
potential avenues for future research in this domain.
II. BACKGROUND TO RESEARCH
Access control mechanisms play a pivotal role in protecting
physical spaces, information, and resources by managing and
restricting entry. Various access control systems have been
explored in the literature, including biometric, card-based,
keypad, and mobile-based systems. Among these, RFID
smartcards have gained prominence as a widely adopted
means of authentication in access control systems [1]. A substantial body of research has investigated the use of RFID
smartcards for access control (e.g., [2], [3], [4]). These studies have demonstrated the effectiveness of RFID technology
in granting access to authorized individuals while restricting unauthorized access. However, the literature has also
identified several challenges associated with RFID smartcards, which can compromise the security and reliability of
access control systems. For example, several studies have
explored the risks of unauthorized access due to stolen,
duplicated, or lost cards [5], [6], [7]. These incidents may
enable unauthorized individuals to enter restricted areas,
posing significant security threats. Research has highlighted
the potential for impersonation attacks, in which an individual uses an authorized person’s card to access secure
locations[8], [9].In response to these security concerns, some
studies have investigated the practical issues arising from the
use of conventional smartcards [10], [11], [12]. This research
has underscored the security concerns leading to difficulties accessing restricted areas and decreased efficiency and
productivity. Given the identified limitations in security and
reliability, a growing body of literature has called for further
research and development in access control systems [13],
[14], [15]). This research has explored more secure and
dependable authentication methods, potentially leading to
innovative solutions that enhance access control mechanisms.
Some research directions include integrating biometric technologies [ [16], employing cryptographic techniques [17],
[18], and examining the potential of multi-factor authentication systems. The literature on access control systems, particularly those utilizing RFID smartcards, has identified both
the advantages and challenges of this technology. By developing and implementing advanced authentication methods,
researchers aim to address these challenges and improve
security and user experience in access control systems.
III. METHODOLOGY
The methodology employed in this study encompasses a
comprehensive research design for the collection of primary data and a summative approach for the analysis of
qualitative content. The research endeavour revolves around
the exploration of diverse solutions while embracing credible, well-referenced facts, devoid of intentions to disprove
existing information or endorse robust opinions. By implementing a comprehensive method design, this study adheres
to an interpretive paradigm, allowing for the comprehensive understanding and exploration of complex phenomena.
This approach is apt for capturing the intricate nuances,
rich contextual details, and subjective experiences embedded
within the IoT domain. Employing methods such as observations, and document analysis, the primary data collection
endeavours to garner in-depth insights and multiple perspectives. The qualitative contents amassed through data
collection undergo a summative approach during the analysis
stage. This process entails systematic coding, categorization, and synthesis of data to identify underlying meanings.
The objective is to distil the qualitative contents’ essential
features and salient aspects, leading to a comprehensive
overview of the collected data and the derivation of meaningful insights. Utilizing these methodological frameworks
allows the study to delve deeply into the subject matter, facilitate practical problem-solving, and yield tangible outcomes
with real-world implications. The adoption of qualitative data
collection methods and the incorporation of realism as the
theoretical perspective serve to enhance the comprehensiveness and validity of the research findings.
IV. COMMUNICATION PROTOCOLS IN ACCESS CONTROL
SYSTEMS
A comprehensive examination of communication protocols
in access control systems is crucial to understand their effectiveness and security features. These protocols are designed to
facilitate secure information exchange between various entities within the system, including users, devices, and servers.
This analysis will delve into the key communication protocols
utilized in access control systems, highlighting their distinct
characteristics and potential vulnerabilities [19].
A. WIEGAND PROTOCOL
The Wiegand protocol has long been perceived as the prevailing standard within the access control domain. The data
speed can accelerate up to 35 Mbit/s (within a 10-meter
range) or 100 kbit/s (spanning 1200 meters). The protocol
lacks encryption and authentication mechanisms, rendering
it vulnerable to data interception, tampering, and replay
attacks [20].
B. RS485 PROTOCOL
The RS485 protocol serves as a serial communication protocol extensively utilized in many access control systems,
encompassing biometric systems and smartcard readers. The
security features are contingent upon the higher-level protocols employed. RS485 boasts numerous advantages over
other standards, particularly in the context of applications in
noisy industrial settings. The design of RS485 is tailored to
exhibit noise tolerance and resilience [21]. It allows multiple
devices to communicate on the same bus over long distance
of about 4000 metres [22].
C. NFC (NEAR FIELD COMMUNICATION)
NFC is a wireless communication protocol that enables contactless communication between devices over short distances,
typically within a few centimetres. Frequently employed in
access control systems utilizing smartphones as credentials,
NFC facilitates secure data exchange via encryption and
cryptographic authentication, rendering it suitable for secure
access control applications [10], [23].
D. RFID (RADIO FREQUENCY IDENTIFICATION)
RFID is a wireless communication technology utilizing
radio frequency for data exchange between a reader and
a tag. Employed in diverse access control systems, such
as contactless smartcards and key fobs, the security features of RFID-based systems are dependent on the specific
RFID technology implemented (e.g., low-frequency, highfrequency, or ultra-high frequency) and the associated
cryptographic schemes [2].
E. BLUETOOTH LOW ENERGY (BLE)
BLE is a wireless communication protocol designed for
low-power devices, increasingly utilized in access control
systems leveraging smartphones as credentials. Supporting
secure communication through encryption and authentication, BLE is well-suited for access control applications. Its
vulnerability to relay attacks necessitates the implementation
of additional security measures. Old legacy access control
systems are progressively adopting more secure and versatile
communication protocols to enhance overall security and user
experience [24].
V. INTEROPERABILITY TECHNIQUES
By employing different techniques and strategies, organizations can ensure seamless integration of various access
control systems devices, and components, fostering improved
efficiency, collaboration, and overall performance. The interoperability term is defined as several components’ ability
to exchange and use the exchanged information [25]. Interoperability is a crucial aspect of modern technology, as it
enables seamless integration of various solutions and systems, enhancing efficiency, flexibility, and scalability. In this
regard, several techniques have been developed to promote
interoperability across different systems.
A. STANDARDIZATION
The development and adoption of industry-wide standards
are critical for achieving interoperability. Standards define
common protocols, data formats, and interfaces, ensuring that
different systems can communicate and work together effectively. Examples of standardization organizations include
IEEE, IETF, W3C, and ISO.
B. OPEN PROTOCOLS AND DATA FORMATS
Open protocols and data formats enable different systems
to communicate and exchange data seamlessly. Developers
can ensure their systems can be easily integrated with other
solutions by using openly documented and widely accepted
communication protocols (e.g., HTTP, MQTT) and data
formats (e.g., JSON, XML).
C. APIS (APPLICATION PROGRAMMING INTERFACES)
APIs serve as intermediaries, allowing different software
components to interact with one another. By providing welldefined, consistent, documented APIs, system developers can
ensure that other systems can communicate and integrate with
their solutions without requiring extensive modifications.
D. MIDDLEWARE
Middleware represents a software stratum situated between
disparate systems, components, or applications, functioning
to streamline communication and data exchange. By serving as an intermediary, middleware can facilitate translation among diverse communication protocols, data formats,
or interfaces, consequently fostering interoperability between
systems that might otherwise remain incompatible. This
intermediary layer plays a critical role in bridging the gap
between heterogeneous systems, promoting seamless integration, and fostering collaboration in a wide range of
technological domains.
E. SERVICE-ORIENTED ARCHITECTURE (SOA)
SOA is an architectural pattern that promotes the development of modular, loosely coupled services that can be easily
combined and reused across different systems. By designing
systems as a collection of interoperable services, developers
can achieve greater flexibility and scalability, allowing for
seamless integration with other solutions.
F. DATA TRANSFORMATION AND MAPPING
Data transformation and mapping techniques are used to
convert data between different formats or structures, enabling
interoperability between systems that use different data representations. Data transformation tools and techniques, such
as XSLT (for XML data) and ETL (Extract, Transform, Load)
processes, can be employed to facilitate data conversion and
integration.
VI. INTEROPERABILITY BARRIERS
The researchers examined the impediments and challenges
associated with interoperability within the scope of enterprise
integration [26]. They identified the following key barriers:
1) HETEROGENEITY
A diverse array of hardware, software, and communication
technologies often characterizes enterprise systems, resulting
in complications when facilitating seamless communication
and data exchange among disparate system components.
2) LEGACY SYSTEMS
Numerous enterprises maintain legacy systems, which were
not initially designed for interoperability. Integration of these
systems with contemporary technologies and applications
proves challenging due to their antiquated architectures,
communication protocols, and data formats.
3) LACK OF STANDARDS
The lack of a universally recognized standard that encompasses all communication protocols, data formats, and
interfaces can pose challenges to achieving interoperability.
While some standards do exist, they may not cover all aspects
of a system or enjoy widespread adoption within the industry.
4) SEMANTIC INCONSISTENCIES
Varied representation and interpretation of data across systems may give rise to semantic discrepancies. Ensuring a
mutual comprehension of data exchanged among systems is
imperative for attaining interoperability.
5) ORGANIZATIONAL AND CULTURAL BARRIERS
Organizational and cultural aspects can also influence
interoperability. Distinct organizations may possess unique
processes, structures, and terminologies, engendering information sharing and collaboration difficulties.
6) SECURITY AND PRIVACY CONCERNS
Guaranteeing the security and privacy of data exchanged
between systems is essential for achieving interoperability,
which may prove challenging due to the diverse security
requirements and policies of distinct organizations and systems. To overcome these barriers, the researchers underscore
the significance of formulating and adopting standards, utilizing middleware and service-oriented architectures, and
employing modeling techniques to comprehensively understand and address the intricacies of enterprise integration and
interoperability. Focusing on access control systems these
often encompass a wide variety of hardware components,
such as card readers, door controllers, biometric scanners, and
intrusion detection sensors. These components may utilize
distinct communication protocols, making seamless interaction and data exchange difficult to achieve. As a result, the
lack of standardized communication protocols for hardware
components within access control systems can hinder overall
system interoperability. To alleviate this issue, creating and
adopting industry-wide communication standards for hardware components within access control systems is necessary.
By establishing universally accepted communication protocols, manufacturers and system integrators can ensure that
diverse hardware components interact seamlessly, regardless
of their specific technology or vendor. This approach promotes greater system flexibility, as organizations can more
easily mix and match components from different manufacturers without sacrificing interoperability. Middleware is an
intermediary layer that can translate between different communication protocols, data formats, and interfaces, enabling
smooth communication between disparate hardware components. Meanwhile, service-oriented architectures promote
modularity and loose coupling, allowing for the flexible
combination of different services and systems to meet specific security requirements. Employing modeling techniques
can assist in understanding and addressing the complexities
of enterprise integration and interoperability. By modeling
the interactions between various hardware components and
communication protocols in access control systems, system
designers and integrators can identify potential bottlenecks,
inefficiencies, and incompatibilities [25].
VII. PROPOSED INTEROPERABLE ACCESS CONTROL
SYSTEM
In this study, the authors present an innovative hardware
design for an access control system that incorporates the
use of rolling QR codes while maintaining compatibility
with existing access control systems based on the widely
implemented RS485 Protocol. The proposed design seeks to
augment the security and flexibility of contemporary access
control frameworks by integrating the benefits of evolving
QR code technology without compromising interoperability.
The integration of rolling QR codes into access control systems offers several advantages, including heightened security
through the continuous generation of unique, time-sensitive
codes and the potential for contactless authentication, thereby
enhancing user convenience and mitigating concerns related
to physical contact. Furthermore, QR codes can be easily
distributed and managed through digital means, such as
smartphones or other smart devices, reducing the reliance
on physical access cards or tokens. By ensuring compatibility with the RS485 Protocol, the proposed hardware design
acknowledges the prevalence of this protocol in existing
access control systems. It alleviates potential challenges associated with integrating new technologies into legacy systems.
The RS485 Protocol has long been a standard for communication between access control devices, such as card readers and
door controllers. Consequently, preserving interoperability
with this protocol is essential for the successful implementation of the innovative rolling QR code-based access control
system. The developed solution highlights the architectural
dependency options in fig. 1 and emphasizes interoperability
to ensure seamless communication and collaboration across
legacy devices and the proposed solution.
FIGURE 1. Software architecture of the interoperable access control
system.
The developed solution aims to tackle the challenges of
integrating new systems with existing or legacy devices
while prioritizing interoperability to enable seamless communication and collaboration. The objective was to facilitate
smooth interaction and cooperation between a traditional
RS485 system and a modern access control system, overcoming potential obstacles arising from differing technologies,
data formats, or protocols. The suggested system comprises
various components, such as bespoke software and hardware, specifically designed to attain interoperability with
the RS485-based access control system. The subsequent
sub-points delineate the salient features of the design and
implementation procedure.
A. HARDWARE
This layer includes the physical components that enable
data collection, input, and communication within the testing
environment:
1) TRADITIONAL ACCESS CONTROL SYSTEM EMPLOYING
RS485
This system is an electronic security system used to manage
access to restricted areas or resources. The key components
of the system are:
• The card reader is normally installed at entry points,
such as doors. The system used in this experiment is
designed to read RFID cards or key fobs, which contain
a unique code. When the card is swiped or presented
near the reader the code is sent via RS485 protocol to
the Access control main unit.
• The access control unit receives the ID data from the
card reader and processes it to determine whether access
should be granted or denied. The panel stores a database
of authorized user IDs and can be programmed with
specific access rules, such as time restrictions or limited
access to certain areas.
• Upon receiving a signal from the access control main
unit, the electric door lock or barrier is either activated
or deactivated, allowing or denying access to the user
based on their credentials.
Figure 2 illustrates a traditional access control system; in the
image, one can observe the card readers and the access control
main unit. This image provides a clear overview of the key
components that constitute the system. This system was used
in our experiment.
B. QR CODE READER
A bespoke circuit board was developed to facilitate the reading of QR codes displayed on mobile devices. Figure 3
depicts the electronic board, which encompasses the requisite components for decoding the QR code and transmitting
the information to the IoT gateway. The board employs
the GROW GM803 Series Interface Barcode Scanner. The
GM803 is equipped with a CMOS sensor featuring a resolution of 640 × 480 pixels, enabling it to decode 1D barcodes
or 2D codes, such as QRCode, DataMatrix, or PDF417.
An ESP32 microcontroller [28], featuring a dual-core processor with a clock speed of up to 240 MHz, 520 KB of
SRAM, and integrated Wi-Fi and Bluetooth functionalities,
is employed for data processing on the QR code reader side.
The GM803 scanner transmits the scanned QR code to the
ESP32 microcontroller via a serial (RS232) protocol. After
the data transmission, the ESP32 microcontroller encrypts
the data and forwards it to the IoT gateway using either the
integrated 2.4 GHz Wi-Fi protocol or the RS-485 protocol,
facilitated by the MAX485, a low-power RS-485 transceiver.
The data transmission option can be chosen when setting up
the device. A bespoke circuit board was developed to facilitate the reading of QR codes displayed on mobile devices.
Figure 3 depicts the electronic board, which encompasses the
requisite components for decoding the QR code and transmitting the information to the IoT gateway. The board employs
the GROW GM803 Series Interface Barcode Scanner. The
GM803 is equipped with a CMOS sensor featuring a resolution of 640 × 480 pixels, enabling it to decode 1D barcodes
or 2D codes, such as QRCode, DataMatrix, or PDF417. This
software offers a comprehensive suite of tools and features
that enable the efficient and precise creation of electronic
circuit board designs. The schematic representation of the
designed board, visually illustrating its underlying electrical
connections and components, is presented in fig. 4. The data
transmission option can be chosen when setting up the device.
The design of the board in this study was facilitated by
the utilization of Kicad, an open-source software renowned
for its capabilities in electronics design and automation.
By employing Kicad [29] as the software platform and
utilizing the schematic representation, the study ensures a
systematic and meticulous approach to board design, incorporating industry-standard practices and facilitating accurate
FIGURE 3. QR code reader.
FIGURE 4. Kicad design.
communication of the design specifications. The power circuit plays a crucial role in the efficient functioning of the
system by facilitating the distribution of power to peripherals
that necessitate a stable voltage supply. In this particular
scenario, the power management system incorporates two
distinct stages. The initial stage caters to the power requirements of the QR code reader, which can accommodate an
input voltage of up to 15V DC. To achieve the desired voltage
levels for the subsequent stages, two Low-Dropout Linear
Regulators (LDOs) are employed. These LDOs effectively
regulate the voltage down to 5V and 3.3V, respectively, ensuring compatibility with the operational specifications of the
peripherals. By employing this multi-stage power management design, the system can effectively regulate the voltage

levels to meet the specific requirements of the peripherals
while mitigating the power draw directly from the microcontroller. This approach minimizes the potential risks associated
with excessive power consumption, safeguarding the microcontroller from issues such as overheating or damage due to
high currents.
C. IoT GATEWAY
The IoT gateway was built based on the Compute Module
CM3 [30] lite version from the Raspberry Pi Foundation. The
CM3 features a Broadcom SoC CPU operating at 1.2 GHz
and 1 GB of DDR2 RAM. The IoT gateway board is designed
with 20 available GPIOs for a variety of sensors and integrates
an MPS 2617 Battery Management chipset. The embedded
1400mAh battery delivers a maximum of 10 hours of battery
life at 1000 mA under high load conditions. This duration can
be extended by employing a larger battery and adjusting the
charging circuit. For connectivity, the device incorporates a
Silicon Labs WF111A 802.11 B/G/N Module for 2.4 GHz
Wi-Fi and includes an eMMC 8GB 3.3V 200Mhz eMMC 5.0
manufactured by ISSI. The IoT gateway operates on a Debian
Linux distribution with a 4.14 kernel version, which is a
widely used open-source operating system. Debian is known
for its stability, reliability, and extensive software library,
making it a popular choice for IoT gateways and embedded
systems. In this case, the IoT gateway uses the Linux kernel
version 4.14, which introduced several improvements and
new features relevant to IoT devices, such as:
1) Enhanced support for ARM-based platforms, which
are common in IoT devices due to their low power
consumption and cost efficiency.
2) Improved power management features, enabling IoT
devices to operate more efficiently and extend battery
life.
3) Better security features and bug fixes, ensuring more
secure and stable operation for the IoT gateway.
Figure 5 illustrates the arrangement of the components on
the circuit board. This visual representation provides a clear
overview of the layout and organization of the various
FIGURE 6. Eagle design of the IoT gateway.
elements, including the microcontroller, connectivity modules, and power management components. By examining
the components’ distribution, we can better understand the
design principles, component interactions, and potential areas
for optimization or modification. The IoT gateway was
designed utilizing Eagle software, a prominent and widely
adopted electronic design automation tool renowned for its
comprehensive features and capabilities. Eagle software provides a robust and versatile platform that facilitates the
precise and efficient creation of complex electronic circuit
board designs. Using the advanced functionalities of Eagle,
the researchers could navigate the intricacies of the design
process and effectively capture the intricate details and specifications of the board. This utilization of industry-standard
software and the accompanying schematic visualization
facilitates effective communication of the design concept,
enhances the reproducibility of the study, and enables other
researchers and practitioners to comprehend and evaluate
the intricacies of the designed board. At the beginning of
the experimental phase, the initial setup encompassed data
transmission between the QR code reader and the IOT
gateway utilizing the RS232 protocol. However, after this
configuration, the research direction shifted its focus toward
the utilization of the RS485 protocol for data transmission.
Consequently, a supplementary peripheral device, namely
a DollaTek serial to RS485 adapter, was introduced and
integrated into the existing architecture of the IOT gateway. This adapter, depicted in fig. 7, facilitated the seamless
transition from the RS232 protocol to the RS485 protocol,
thereby enabling successful and efficient data transmission in the revised experimental scenario. Figure 8 visually
portrays the final hardware architecture, illustrating the interconnectedness among the diverse developed components.
This comprehensive diagram is a powerful tool for presenting the physical arrangement and connectivity within the
system. The hardware architecture encompasses integrating
multiple components, each specifically designed to facilitate data transmission between the QR code reader and the
IoT gateway. The depiction in Figure 8 aptly showcases
the intricate interrelationship and interdependence of these
components, collectively constituting a coherent and interconnected system. The figure emphasizes delineating the
established connections among the components, thereby outlining the pathways through which data, signals, and power
are seamlessly transmitted. This visual representation provides a holistic understanding of the underlying hardware
infrastructure, thereby facilitating the analysis and evaluation of the system’s overall design. By presenting Figure 8,
researchers enable a comprehensive comprehension of the
hardware architecture, as it offers a detailed depiction of the
physical arrangement and the intricate connectivity within
the system. This serves as a valuable resource for analyzing and assessing the system’s functionality, allowing for
further exploration and potential refinements. This visualization enhances the clarity and transparency of the system,
enabling a thorough examination of the physical connectivity
and facilitating future analysis, troubleshooting, and potential
modifications.
D. SOFTWARE
The implementation of this experiment required the development of various software components that work together to
enable efficient communication, data processing, and system
management. These software components are described as
follows:
1) QR CODE READER EMBEDDED SOFTWARE
The Esp32 microcontrollers are programmed using a language derived from C/C++, facilitating their utilization
through various integrated development environments
(IDEs), including the widely recognized Arduino IDE and
other compatible platforms that support C++ programming and compilation. Different approaches to writing the
code were implemented. One of those approaches was
EyesWeb [26] open-source platform, which is used to write
the block code for the hardware system. But in this particular study, the open-source version of Visual Studio Code,
integrated with the platform plugin, was selected as the
designated IDE for system development. The adoption of the
Open-source version of Visual Studio Code, renowned for
its extensive functionality and adaptability, in conjunction
with the PlatformIo plugin, significantly contributed to the
successful execution of the system development process.
This combination of tools provided comprehensive support,
encompassing efficient code editing, debugging, and deployment capabilities, thereby optimizing the programming
workflow for the Esp32 microcontrollers within the research
project. Considering the paramount importance of security
in designing the system, all device connections were implemented using the HTTPS protocol to ensure the secure
transmission of data to the server. To achieve secure data
transmission, the implementation incorporated the WiFiClientSecure library, which encrypts the traffic sent to the
IoT gateway [27]. This encryption mechanism enhances
the confidentiality and integrity of the transmitted data,
safeguarding it against unauthorized access and potential
tampering. Through the adoption of the HTTPS protocol and
the integration of the WiFiClientSecure library, the research
project assures the application of robust security measures
throughout the data transmission process [28]. This strategic
implementation safeguards sensitive information, thereby
upholding the system’s overall security posture. Figure 9
serves as an exemplification of the implementation of the
Visual Studio IDE and the incorporation of the library. The
figure showcases the practical utilization of Visual Studio
IDE, providing a visual representation of the software environment and the library’s integration within the development
framework. This illustrative example offers valuable insights
into the practical application of the IDE and the library, aiding
in the comprehension and replication of the research project’s
secure data transmission approach.
2) IOT GATEWAY EMBEDDED SOFTWARE
The embedded software component residing on the IoT
Gateway plays a crucial role in the system, serving as a
fundamental element for facilitating efficient communication
and data exchange between the traditional access control
system and the newly developed system. This software component plays a significant role in achieving interoperability
by translating and unifying disparate protocols utilized by
both systems. The protocol unification implemented by the
software allows for seamless communication, enabling
real-time insights into the access control process. The software component performs essential functions to process
information acquired from the QR code reader, employing
specific protocols for data handling. It carries out data
cleansing operations to ensure the accuracy and reliability of the obtained information. Subsequently, the software
component forwards the processed data to the backend infrastructure using API services. Notably, the communication
between the software component and the backend API is
conducted using the HTTPS protocol, emphasizing the integration of enhanced security measures [29]. By adopting the
HTTPS protocol, the system enhances the confidentiality and
integrity of the transmitted data, guarding against potential
security threats. This ensures secure and reliable communication between the software component and the backend
infrastructure, mitigating the risk of unauthorized access or
data breaches. The application residing on the IoT gateway is developed using JavaScript programming language,
implementing the Node.js framework. JavaScript is a widely
adopted language known for its versatility and extensive support across different platforms. It is particularly well-suited
for web development, and with the utilization of the Node.js
framework, it extends its capabilities to server-side application development. By employing JavaScript with the
Node.js framework, the application benefits from a range
of features and libraries that facilitate efficient and scalable
server-side programming. Node.js allows for event-driven,
non-blocking I/O operations, which enhances the application’s performance and responsiveness, making it well-suited
for handling concurrent connections and real-time communication. The JavaScript programming language, combined
with the Node.js framework, enables the application to seamlessly integrate with other system components. It allows for
the implementation of server-side logic, handling data processing, communication with external APIs, and managing
the overall functionality of the IoT gateway. The utilization of JavaScript with the Node.js framework empowers
the application residing on the IoT gateway with a robust
and versatile environment for server-side development. This
combination facilitates efficient and scalable programming,
ensuring seamless integration within the system architecture
and enabling the application to fulfill its intended functionalities effectively. The development of the application
involved the creation of various microservices to cater to
multi-protocol testing requirements. These microservices are
elucidated as follows:
1) Microservice for RS232/Wiegand/RS485 Protocol
Interaction: This microservice encompasses a distinct
software module responsible for reading data received
through any of the mentioned protocols. It undertakes
data cleansing operations, ensures the security and
privacy of exchanged data between systems, and standardizes the received data. Web Service API for WIFI
and HTTPS Protocol Data Reception: This microservice focuses on receiving data through the WIFI and
HTTPS protocols. It establishes a web service API to
facilitate the reception and processing of data obtained
via these communication channels.
2) Data Security Microservice: Dedicated to ensuring
data security, this microservice is responsible for handling the encrypted key sent from the mobile app to
the QR reader. It decrypts the key using the public and
private key keys, extracts the user identification, and
verifies the door access against a local database.
3) Hardware Interaction Microservice: Once the user
has been identified and the necessary door access
determined, this microservice interacts with the legacy
system. It sends a signal to trigger the lock release
mechanism, thereby providing access to the designated
door.
4) API Microservice: This microservice operates as
a conduit for real-time data updates to about user
access events. It consumes an API located in the
cloud, allowing for seamless integration of updated
information triggered by events. Additionally, this
microservice generates logs encompassing user activity and system performance, facilitating subsequent
data analysis endeavours. The implementation of
these microservices within the application framework
enables comprehensive coverage of multi-protocol testing scenarios. Each microservice plays a specific role,
contributing to the overall functionality and security
of the system. This modular approach streamlines the
development process, ensuring efficient communication, data processing, and seamless integration with
existing systems.
3) CLOUD SOFTWARE
The Cloud software comprises two main components: the
backend and the front end. The backend component plays a
vital role in processing requests and managing interactions
between the frontend front end and the database. It is developed using Laravel, a widely adopted and powerful PHP web
application framework. Laravel follows the Model-ViewController (MVC) architectural pattern and offers an extensive range of features and tools that empower developers to
create intricate, scalable, and high-performing web applications. Laravel encompasses several key features, including a
robust routing system, an expressive query builder, a powerful
database abstraction layer with Object-Relational Mapping
(ORM) capabilities, user-friendly authentication and authorization mechanisms, caching functionality, and support for
multiple file systems. These features collectively enhance the
development process and contribute to the creation of sophisticated web applications. The developed application, based on
Laravel, incorporates various APIs that facilitate communication and data processing within the SAME (Smart Assistance
for Manufacturing Environments) framework. These APIs
include:
• User Management API: This API utilizes Create,
Read, Update, and Delete (CRUD) operations to manage
users within the system, enabling effective user administration.
• IIoT Management API: This API also leverages
CRUD operations to manage Industrial Internet of
Things (IIoT) devices and associated data, ensuring efficient management and control of IIoT assets.
• LOGS API Interface: The LOGS API Interface is a
critical component of our system, providing a conduit
for robust data logging and in-depth analysis. This API
creates an interface that allows system activities to be
tracked, audited, and analyzed effectively, facilitating a
better understanding of system behaviors, performance,
and potential issues. At its core, the LOGS API Interface
serves to capture, store, and retrieve logs and information about the system. This information can include
transaction records, user activities, system errors, security incidents, and more. The versatility of data it can
handle makes it an invaluable tool for system management and troubleshooting. This API not only logs
data but also aids in generating comprehensive reports,
delivering insights into the system’s operation. These
reports can be customized as per the requirement, focusing on areas like user behavior, system performance,
error detection, or security auditing.
• Access Control API: These services facilitate the management of access control within the system, allowing
for the configuration of user access privileges based
on designated zones and specific time restrictions. This
service enables granular control over user permissions,
ensuring that access to various areas or resources is
granted or restricted based on predefined criteria related
to user identity, designated zones, and time parameters.
By utilizing this service, administrators can effectively
define and enforce access control policies, optimizing
security and maintaining the integrity of the system.
• Secure Mobile App API Services: These services serve
the purpose of providing secure API endpoints for the
mobile app, facilitating the secure transmission of QR
codes and ensuring the confidentiality and integrity
of the data exchanged. The frontend component of
the system encompasses a web client developed using
Angular 8, a JavaScript framework built-in TypeScript.
This open-source framework offers a comprehensive
set of tools and features for efficient web application
FIGURE 10. Access management interface.
development. The frontend system is composed of various interfaces that serve the purpose of facilitating
effective system management and providing real-time
insights into the access control process. These interfaces empower system administrators with the ability to
monitor the status of IoT gateway and QR code readers and perform user management and access control
management tasks. Additionally, the interfaces enable
administrators to visualize the current state of the overall
system. Within the frontend system, a specific interface
is dedicated to the setup of user or group access permissions. This interface allows administrators to define
access privileges based on location and time parameters.
The figure presented below illustrates the aforementioned interface, providing a visual representation of
the functionality that enables system administrators to
configure access permissions. Through this interface,
administrators have granular control over access settings, ensuring that access privileges are aligned with
specific locations and timeframes.
4) MOBILE APPLICATION
The mobile application developed plays a pivotal role as a
user-accessible platform, enabling them to utilize the secure
QR code generation API integrated within the backend system. Additionally, the application encompasses a range of
features focused on access control and data analysis, with
a specific emphasis on access history tracking. Users are
empowered with the functionality to administer their profiles and manage data usage preferences according to their
requirements. The development of the mobile application
was facilitated by Ionic, an esteemed open-source framework
widely recognized for its ability to facilitate the creation of
robust and high-performing hybrid applications. By leveraging prominent web technologies such as HTML, CSS, and
JavaScript, Ionic seamlessly integrates with widely adopted
frameworks like Angular, thereby providing a seamless and
efficient development environment. In this specific instance,
the application interfaces were implemented using Angular
12, enabling the creation of intuitive and user-friendly screens
and interactions. Importantly, the Ionic framework ensures
broad compatibility with a wide array of mobile devices available on the market, allowing the generated mobile application
to be installed and utilized across diverse platforms. Figure 11
provides a visual depiction of the interface specifically dedicated to QR code generation within the mobile application.
VIII. EVALUATION METRICS
Here, the evaluation metrics employed to assess the implemented work are presented with the predetermined requirements for an access control system [30], the following metrics
have been identified as essential for conducting a comprehensive evaluation:
1) Security: The effectiveness of the rolling QR code
mechanism in preventing unauthorized access and mitigating the risks associated with code interception or
duplication is assessed.
2) Interoperability: The system’s capacity to seamlessly
integrate with diverse access control devices, including
QR code readers, IoT gateways, and legacy systems,
is evaluated. The goal is to ensure compatibility and
interoperability among different system components.
3) User Experience: The user-friendliness and ease of
use of the system are considered, encompassing factors
such as the simplicity of QR code generation and scanning, intuitive user interfaces, and clear instructions for
accessing secured areas.
4) Scalability: The system’s scalability is determined by
assessing its ability to handle increasing numbers of
users, access points, and simultaneous access requests
while maintaining optimal performance and security.
5) Data Privacy: An evaluation is conducted to assess
the system’s adherence to data privacy regulations and
best practices. This entails verifying that user data and
access logs are securely stored, encrypted, and accessible solely to authorized personnel.
6) Auditability: The system’s capability to generate
comprehensive access logs and audit trails, enabling
traceability and accountability for access control
events, is evaluated. The accuracy and completeness of
the generated logs are also assessed.
7) Performance: The system’s performance is measured
in terms of response time, QR code generation and
scanning speed, and overall operational efficiency. This
ensures that access control processes are executed
promptly and without significant delays.
As given in [31], [32], and [33], these evaluation metrics have
been chosen to comprehensively evaluate the access control
system based on its predetermined requirements. They provide a robust framework for assessing different aspects of the
system’s functionality, security, user experience, scalability,
data privacy, auditability, and performance.
IX. RESULTS AND ANALYSIS
This section discusses the evaluation results obtained from
the design of the system and the experimental implementation conducted in this study. The system underwent various
tests to assess its effectiveness and compatibility with traditional legacy systems. Results are presented and analyzed,
highlighting the system’s performance, functionalities, and
integration capabilities. In the used test scenario, the user
employs a mobile phone to receive an encrypted key from
the server, which is subsequently transformed into a QR
code. The user then positions the phone in front of a QR
code reader device, which reads the QR code and transmits
it to the IoT gateway via RS485, RS232, or Wi-Fi protocols.
It is noteworthy that the QR code remains valid for a limited
duration of 5 seconds before it regenerates. In this depicted
scenario, a mobile phone serves as the primary medium for
a user to receive an encrypted key from a server, which is
subsequently transformed into a QR code. Once generated,
the QR code is then presented to a dedicated QR code
reader device. This device, utilizing RS485, RS232, or Wi-Fi
protocols, captures the QR code’s information and transmits it
to an IoT gateway. Upon receiving the QR code information,
the IoT gateway undertakes the decryption process, extracting
crucial data such as the user’s identification and the specific
door to be accessed. The decrypted information is verified
against a local database to check user access privileges and
ensure the QR code hasn’t been reused. Access authorization
is determined based on the decrypted data, current time, and
predefined access criteria. Once access is confirmed, a code
is dispatched from the IoT gateway to a traditional access
control system via the RS485 protocol. This code serves
as a signal to activate the lock mechanism, granting entry
to the authorized user. Used QR codes are blacklisted and
stored in the local database to maintain security and integrity.
The local database synchronizes with the backend every
minute to keep user information, access times, and authorized
doors up-to-date and secure. All system-related information
is encrypted with private and public keys to enhance security.
This encryption reduces the risk of unauthorized decryption,
protecting the confidentiality and integrity of sensitive data
throughout the access control process. The outlined process
is visually represented in Figure 12 below. The evaluation
centered on the effectiveness of the rolling QR code mechanism in preventing unauthorized access and reducing risks
of code interception or duplication. System performance was
tested using three communication protocols, WiFi, IP, RS232,
and RS485, to establish connections between the QR code
reader and the IoT gateway. The resulting data, including
average response times, incidences of code interception and
duplication, and instances of unauthorized access, are presented in Table 1. The results offer valuable insights into
the system’s performance, highlighting code interception,
duplication, and unauthorized access vulnerabilities. This
contributes to a comprehensive evaluation of the rolling QR
code mechanism’s effectiveness.
A. SYSTEM RESILIENCE TESTING
The researchers used the Wi-Fi (IP/TCP) protocol to investigate the results. Although the average response time for
all protocols was below 100ms, it was observed that the
Wi-Fi signal became unstable when the distance between
the QR reader and IoT gateway exceeded 50 meters. The
researchers found the instability due to the building’s wall
TABLE 1. Comparative analysis of protocols.
thickness and metal components. Using the HTTPS protocol
for data transmission between the QR reader and IoT gateway
prevented QR code interception and duplication over Wi-Fi
and IP/TCP.
B. SECURITY TESTING
No unauthorized access was observed, indicating the
system’s resilience against Wi-Fi-based penetration attempts.
One of the main features of HTTPS is that it is encrypted.
Wireshark was used to emulate a security attack and capture
network traffic. Since HTTPS is encrypted, there’s no way to
read it in Wireshark. The encrypted data was decrypted using
the cipher negotiated by the TLS protocol of HTTPS. The
decrypted data was found to be unaltered and the integrity of
the data was proven by the hash/compression algorithm.
For the RS232 protocol, the researchers found that the
response time was comparable to Wi-Fi, under 100ms.
However, it was discovered that the data sent in clear text
and lack of encryption made it susceptible to interception
and duplication. Interception and reading of QR codes were
possible by connecting a USB to the RS232 adapter to the
QR code reader board. However, unauthorized access was
prevented due to the expiration time and blacklisting of used
QR codes. Similar tests with the RS485 protocol showed
the same results, with no unauthorized access observed. Furthermore, the researchers calculated no data losses using a
30-meter cable with the RS485 protocol. The results of this
study indicate that the rolling QR code mechanism is highly
effective in thwarting unauthorized access attempts. Despite
the possibility of QR code interception with RS232 and
RS485 protocols, the use of expiration times and blacklisting
effectively prevented unauthorized access, thereby enhancing
the system’s overall security.
C. SCALABILITY TESTING
The system’s scalability was thoroughly evaluated, demonstrating its ability to handle increasing users, access points,
and simultaneous access requests while maintaining optimal
performance and security. Extensive testing showed that the
system efficiently managed a substantial workload without
compromising service quality. For example, a single IoT
gateway efficiently managed 45 QR code readers during
testing without degrading service performance, highlighting
the system’s robust scalability. The gateway can manage
between 100-1000 concurrent connections when operating
solely with the local database. However, when the same environment is simulated with cloud database synchronization,
the gateway can handle only 100-500 concurrent connections
before experiencing any performance degradation. Additionally, the system’s seamless integration with various legacy
access control devices was evaluated using the RS485 communication system. As given in fig. 13, the proposed system
efficiently exchanged data between the IoT gateway and traditional access control systems without complex installations,
maintaining a secure connection. A user study with 25 participants assessed the system’s user-friendliness, focusing on
the simplicity of QR code generation and scanning and the
intuitiveness of user interfaces.
D. GDPR COMPLIANCE
An assessment was conducted to ensure the system’s compliance with GDPR requirements. This included verifying that
user data and access logs were securely stored, encrypted,
and accessible only to authorized individuals. Personal information was encrypted before storage using an encryption
key derived from hardware IDs associated with the IoT
gateway. To decrypt and access personal information that
could identify the user, the IoT gateway must be online
and accessible to provide the necessary key via backend
APIs. Therefore, decrypting data becomes highly improbable
without a physical IoT gateway during a security breach.
Additionally, the QR codes generated by the system do not
contain any personal information about the user, further safeguarding data privacy. Implementing these measures ensures
GDPR compliance through robust encryption, reliance on
the IoT gateway for decryption, and exclusion of personal
details in QR codes, maintaining high data privacy and security. The evaluation assessed the system’s ability to generate
comprehensive access logs and audit trails for traceability
and accountability. Specific measures within the IoT gateway
software enabled accurate logging of access control events by
storing all requests from the QR reader to the IoT gateway
in the cloud database via an API, ensuring seamless data
transmission and logging. A dedicated listener monitored the
RS485 connection between the IoT gateway and the traditional access control system, capturing and forwarding all
data exchanges to the cloud server via APIs. The accuracy
of the access logs was rigorously evaluated, with no data loss
detected. All data exchanges were effectively recorded and
securely stored in the cloud database.
E. OVERALL SYSTEM PERFORMANCE
The system demonstrated its ability to generate comprehensive access logs and audit trails, ensuring data accuracy
and integrity, thus enhancing traceability and accountability
for access control events. The system was evaluated over
three months, operating seamlessly without manual intervention. This assessment confirmed the system’s ability to
consistently deliver its intended functionality and maintain
optimal performance, demonstrating robustness and stability
in autonomous operation.
FIGURE 13. Framework for access control.
F. USE CASE SCENARIOS
The proposed system can have various real-time applications.
• Access Management: Rolling QR codes improves efficiency by providing temporary access while maintaining
a robust log for audit purposes.
• User convenience: Rolling QR code system eliminates
physical keys or cards, enhancing security against theft
or duplication. The contactless solution also minimizes
logistical challenges.
• Compatibility and functionality: Ease of integration
legacy systems ensures compatibility and adding extra
capabilities without replacing existing infrastructure,
saving costs.
• Scalability: Rolling QR codes is scalable and supports multiple users and devices without compromising
security, ideal for large-scale industrial operations.
G. TRADE OFFS OF USING QR CODES
Frequent QR code regeneration offers enhanced security benefits but also has trade-offs. The following list presents some
key considerations:
• Increased Data Transmission: Regular updates of QR
codes can prevent unauthorized access by ensuring
that each code is unique and time-sensitive. However,
this requires frequent data transmission between the
server and the device, increasing the network traffic and
slowing operations.
• Processing Overhead: Constant generation and validation of new QR codes leads to higher computational
costs and potential delays.
• User Convenience: Users may find it inconvenient to
scan new QR codes frequently, especially if the process
is slow or the users need to update their app or device
settings.
X. CONCLUSION
As described in sections V to VII, this study has successfully demonstrated the interoperability of the proposed
access control system with legacy systems through a comprehensive assessment of the system’s functionality, performance, security, scalability, user experience, data privacy,
auditability, and communication protocols, with a primary
focus on achieving interoperability. Figure 13 depicts the
overall framework designed in this study.
The evaluation confirmed that the proposed system effectively communicated with old legacy systems, establishing
seamless integration and interoperability between the components. The system’s functionality was thoroughly evaluated,
ensuring it met the requirements and specifications for effective communication with legacy systems. Performance tests
assessed the system’s responsiveness, efficiency, and reliability in facilitating communication and data exchange with the
legacy systems. Moreover, the study paid significant attention to the system’s security aspects, evaluating its ability
to maintain data integrity and confidentiality during interactions with legacy systems. Robust security measures, such as
encryption protocols and access controls, were implemented
to safeguard sensitive information and prevent unauthorized
access. Scalability, another critical aspect of the evaluation,
examined the system’s ability to handle increasing workloads
and accommodate a growing number of users and access
points while maintaining optimal performance. The system
demonstrated its scalability by effectively scaling up and
meeting the demands of legacy systems without compromising functionality or performance. The evaluation also
focused on the user experience, assessing the system’s ease
of use, intuitiveness, and overall user satisfaction when interacting with legacy systems. The study focused on designing
user-friendly interfaces and streamlining processes to ensure
a seamless and positive user experience. Data privacy and
auditability were paramount in the evaluation, ensuring the
system complied with relevant regulations and best practices.
Measures were taken to protect user data, secure access
logs, and maintain an auditable trail of system activities with
legacy systems. We thoroughly examined the communication
protocols employed by the system, assessing their compatibility with legacy systems and ability to facilitate effective
and reliable communication. The evaluation affirmed the
proposed access control system’s interoperability with old
legacy systems, highlighting its functionality, performance,
security, scalability, user experience, data privacy, auditability, and communication protocol compatibility. The findings
of this study contribute to the body of knowledge surrounding
access control systems and provide insights into the development of interoperable solutions for integrating with legacy
systems. Figure 13 depicts key findings highlighted in this
study.
The ‘Results and Analysis’ section of the study thoroughly
examined the system’s proficiency in generating detailed
access logs and comprehensive audit trails. Our experimental
results demonstrate that the system not only records each
access event with precision but also captures a wealth of data
associated with these events. This includes the time stamp,
user identification, access point details, and the authentication method. The system’s capability to log such granular
details is pivotal in enhancing security and monitoring,
as it allows for meticulous tracking of access patterns and
identification of potential security breaches. Our analysis
shows that the system’s audit trails are robust and comprehensive, providing a detailed chronological record of all activities
and changes, including administrative actions. These audit
trails are essential for maintaining system integrity, offering
transparency and accountability crucial for security audits
and regulatory compliance. The system’s advanced data analytics tools extract meaningful insights from access logs and
audit trails, helping administrators identify trends, detect
anomalies, and make informed decisions about security policies and system enhancements. Its reporting capabilities
allow for customized reports, providing valuable data for
security analysis and organizational planning. Our results
indicate the system’s capabilities in generating and analyzing
access logs and audit trails are comprehensive and highly
efficient. Integrating IoT technology with advanced data processing ensures that the system can handle large volumes of
data seamlessly, maintaining high performance even under
heavy usage. This efficiency is a testament to the system’s
robust design and potential to be a reliable and effective tool
in various security-sensitive environments.
While HTTPS offers a secure communication channel, it is
still vulnerable to attacks like Man-in-the-Middle (MitM)
and SSL/TLS vulnerabilities. Although our research does not
specifically test these attacks and vulnerabilities, future work
could explore these possibilities. Investigating the combination of multiple authentication methods, such as rolling QR
codes with NFC, could provide a robust and secure solution
which will be looked in future studies.
DECLARATION OF COMPETING INTERESTS
The authors declare that they have no known competing
financial interests or personal relationships.
STATEMENT
During the preparation of this work, the author utilized
Grammarly and other spelling services to enhance the grammatical accuracy and readability of the paper. Following the
utilization of this tools/services, the author carefully reviewed
and edited the content, taking full responsibility for the final
publication.

