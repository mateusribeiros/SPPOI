Title: 5G-Enabled PMU-Based Distributed Measurement Systems: Network Infrastructure Optimization and Scalability Analysis

Abstract:
In recent years, there has been a rapid shift toward a fully digital paradigm in electrical substations. This shift is driven by the need for greater interoperability between different instruments and control actions, which is facilitated by the International Electrotechnical Commission (IEC) 61850 series of standards. In this article, we specifically focus on phasor measurement units (PMUs) and their role in this digital transformation. One of the challenges in adopting high-performance wired communication standards such as Ethernet and time-sensitive networking (TSN) is the cost associated with wiring over long distances between substations. To overcome this limitation, we explore the feasibility of utilizing a 5G communication infrastructure to transmit PMU measurements. Our study simulates a real-world distribution network and assesses the worst case latency between PMUs and phasor data concentrator (PDC) by scaling the number of PMUs considered. With a mean communication latency of 20 ms, the 5G communication infrastructure proves to be a valuable solution, particularly in distribution networks where the monitoring applications rely on update rates in the order of few tens of millisecond.
Published in: IEEE Transactions on Instrumentation and Measurement ( Volume: 73)
Article Sequence Number: 5504212
Date of Publication: 16 September 2024 
ISSN Information:
DOI: 10.1109/TIM.2024.3457959
Publisher: IEEE
Funding Agency:
CCBY - IEEE is not the copyright holder of this material. Please follow the instructions via https://creativecommons.org/licenses/by/4.0/ to obtain full-text articles and stipulations in the API documentation.
SECTION I.Introduction
The power systems of today are undergoing a rapid transformation, shifting away from the traditional analog-based monitoring and control approach to a new digital framework [1], [2]. This shift is driven by the integration of renewable energy sources (RESs) and the challenges they pose for distribution and transmission system operators (DSOs and TSOs) [3], [4], [5]. RES, connected through dedicated inverters, lack grid inertia and introduce power signal quality issues through their internal power electronics [6], [7], [8].

To tackle these challenges, a distributed measurement infrastructure has been deployed in substations, where various instruments enable real-time monitoring of key quantities [9]. Among the solutions, phasor measurement units (PMUs) stand out as they provide time-stamped measurements of voltage and current phasors, frequency, and rate of change of frequency (ROCOF) associated with the fundamental component. The PMU-Std (International Electrotechnical Commission (IEC)/IEEE 60255-118-1) standard [10] defines the performance requirements for PMUs, including measurement accuracy, reporting latency, response time, and synchronization with universal coordinated time (UTC).

The progressive adoption of digital substations offers enhanced control, responsiveness, cost management, and safety. The IEC 61850 standard [11] defines communication protocols and interoperability requirements for substation systems from different vendors [12], [13], [14]. It incorporates various message types, including sampled value (SV) and generic object-oriented substation event (GOOSE) protocols, as well as the integration of PMU measurements and configuration messages through the IEC 61850-90-5 standard.

However, it should be noted that within digital substations, many communications are time-critical, and fully wired solutions are not always practical or economically viable [15], [16]. For example, power line communications (PLCs) technologies utilize existing power cables for both power and data transmission. However, reliable data transmissions via power lines face technical challenges due to signal propagation characteristics, including low data rates, high signal attenuation, and interference from other power signals and external electromagnetic sources [17]. Some issues have been addressed using optical communication (fiber optics) or digital subscriber lines (DSLs), which can transmit data over several kilometers with bandwidths ranging from a few megabits per second to tens of gigabit per second. These technologies are robust against electromagnetic and radio interference, particularly optical fibers [18]. However, they require the substation to be near the network termination, which is not always feasible in remote areas. This issue can be partially mitigated using 802.15.4-based networks or IEEE 802.11-based networks (WiFi), which offer low latency and relatively high bandwidth, ranging from a few kilobits per second to several gigabit per second with the recent IEEE 802.11ax standard, and transmission ranges of 10–300 m [19]. However, latency and bandwidth trade off with distance, as covering longer distances requires more robust modulations at the expense of data rates, potentially preventing timeliness requirements from being met. To address this, recent literature has explored the feasibility and potential advantages of utilizing 5G mobile communication technologies in power systems, especially in distribution grids with limited distances between substations, where a single or a few antennas can provide sufficient coverage for the entire area of interest [20], [21].

In the recent years, the possible application of cellular networks for power system monitoring infrastructures is getting more and more popular [22], [23]. On one side, cellular networks are widespread and allow for retrofitting existing substations where no wired connectivity exists. On the other side, an improvement is necessary to guarantee sufficient resilience to cyberattacks and continuity of service in the case of systemic outages. Therefore, it is reasonable to say that a close collaboration between power system operators and service providers are encouraged to identify the most suitable infrastructure and bandwidth allocations, based on the specific topology and characteristics of each network [24].

In this study, we explore the feasibility of utilizing a 5G communication infrastructure for a distributed measurement system based on PMUs. Our objective is to assess the statistical distribution of 5G communication delays in a realistic operational scenario. While setting a strict and singular performance objective proves challenging, real-time state estimators, which are crucial for power system control, serve as a foundation for our analysis. With time-stamped PMU measurements, the swift retrieval and aggregation of data from all grid nodes is essential. To achieve accurate results and timely responses, we aim for a target latency of 100 ms as a requirement set by [25] also considering the results from [26], where a 4G network was tested, we aimed to achieve a target latency of 100 ms. Indeed, it was found that 100 ms represented the 99th percentile latency, indicating that the vast majority of responses were delivered within this timeframe. Given that the PMU measurement process already introduces latency in the range of tens of milliseconds, the communication latency should be even lower to meet stringent requirements.

Recent experiences in the field of PMU-based state estimation prove how it could be possible to push the estimates’ update period in the order of 20 ms. This performance target might be considered as ambitious or even unrealistic over large distances or in large transmission networks [27]. Instead, it might be achieved in smaller scenarios, where the latency inherent in the measurement infrastructure could be considered uniform along all the nodes [28], [29].

Moving from the above considerations, in this article, which substantially extends [30], we propose a more structural assessment of the adoption of 5G mobile communication technologies in the context of PMU-based distributed measurements systems. In this respect, we report and discuss the results of an improved simulation setup that considers various transport protocols and redundancy techniques to explore potential enhancements in latency, packet loss, and bandwidth utilization performance metrics. Based on the obtained results, we provide an overview of the requirements and trade-offs that each technique must confront.

To conduct our analysis, we consider a distribution grid and investigate the operational complexities associated with implementing 5G technology for transmitting PMU measurements from various nodes. Using the OMNet++ network simulation environment, we replicate plausible scenarios with different network configurations and varying data volumes to be transmitted. Specifically, we evaluate the measurement latency as received at the slack bus, which serves as the aggregator node in the network. This allows us to quantify the extent to which delay can be attributed to the 5G communication infrastructure and determine the maximum number of PMUs that can be connected while maintaining latency within acceptable limits. Building upon these initial findings, we discuss potential bottlenecks in the proposed implementations and the potential impact on typical control actions. It is worth noting that while 5G opens up possibilities for a more flexible communication infrastructure, it also introduces potential cybersecurity issues [31], [32]. However, this aspect is out of the scope of this article and will be addressed in future works.

In detail, the article is organized as follows. Section II gives a brief description of the IEC 61850 Framework and outlines the possible data packets formats used by PMSs. Section III introduces the simulation setup and the communication infrastructure. Sections IV and V describe the tests carried out and discuss the obtained results. Section VI provides results of the proposed methods simulating a real application scenario. Finally, Section VII concludes the article and outlines some future directions of research.

SECTION II.PMU Packet Format in IEC 61850 Framework
In this section, we introduce the structure of PMU measurement packets according to the most recent standards. For the sake of clarity, we focus on the PMU use case, as it is directly linked to monitoring and control applications. Nevertheless, similar considerations apply to other messages and packets.

In this context, Fig. 1 presents the evolution of the PMU packet format in the different standards. On the left, the IEEE Std C37.118.2 [33] introduces the format of a PMU data packet: in addition to the fields containing the measured quantities and a few flags related to instrument status and operation, the packet also includes the network protocol layers (TCP/UDP and IP) necessary for efficient and secure message exchange over the network. In the middle, the typical structure of an IEC 61850 packet includes SV and GOOSE messages, which are intended for real-time communication services directly mapped to the Ethernet layer. As a consequence, they are not transmitted over IP but with an Ethernet IEEE 802.3 frame format. On the right, an example of PMU measurement is encapsulated within an IEC standard packet and is compatible with a routable UDP/TCP service with multicast capabilities.

Fig. 1. - Evolution of packet format for PMU measurement transmission, from IEEE C37.118.2 to IEC 61850-90-5 [34].
Fig. 1.
Evolution of packet format for PMU measurement transmission, from IEEE C37.118.2 to IEC 61850-90-5 [34].

Show All

SECTION III.Simulation Setup
In this section, we introduce the simulation models for the power grid and the communication infrastructure.

A. Simulated Power Grid
For this analysis, we considered a real-world power grid, namely a 10-kV three-phase distribution network, located in The Netherlands and operated by the DSO Alliander. The network topology (shown in Fig. 3) and its main parameters are thoroughly described in [35]. In order to reproduce a plausible operating scenario, we assume that each node is equipped with a PMU reporting rate of 50 frames/s. The PMU measurements are aggregated by a phasor data concentrator (PDC) located in Node 1.

Fig. 2. - 5G architecture.
Fig. 2.
5G architecture.

Show All

Fig. 3. - Simulated 18-bus distribution feeder located in The Netherlands [35].
Fig. 3.
Simulated 18-bus distribution feeder located in The Netherlands [35].

Show All

A power grid where each node is populated with a PMU may resemble not fully realistic. Nevertheless, our objective is to assess the potential benefits and challenges of a 5G communication infrastructure in the presence of a significant number of PMUs transmitting at the same time. In this sense, the Alliander power grid has two main advantages.

The line lengths within the grid have been significantly reduced, with an average distance of 0.6 km and none exceeding 2 km. These distances are within the range of the optimal inter-gNB distance typically observed in 5G networks, which is generally a few hundred meters to a few kilometers. Therefore, it is reasonable to conclude that the entire grid can be effectively covered by a single 5G network, i.e., one or more gNBs connected to the same 5G radio access network (RAN) and backhaul network [36].

In a previous experiment [26], the PMU data stream was transmitted through a set of dedicated 4G routers (R-1300, Garderos Gmbh, Munich, Germany) in turn connected to the Vodafone network without any specific service level implemented (so that the PMU traffic is not prioritized). The latency showed a bimodal distribution centered around 70 ms.

B. Simulated Communication Infrastructure
The behavior of the 5G communication infrastructure has been analyzed using a suitable simulation environment, developed using the popular OMNeT++ simulator [37]. OMNeT++ is a C++ discrete event simulator that has been widely used in recent years to simulate communication networks. It is worth noting that OMNeT++ has recently introduced several new communication technologies, including time-sensitive networking (TSN) and 5G. The latter is of particular importance for this study and has been introduced into OMNeT++ thanks to the developers of the Simu5G project.

The Simu5G framework [38] is an OMNeT++ extension specifically designed for accurate analysis of 5G networks. Most notably, the simulator is properly validated and, unlike other popular 5G simulators such as the MATLAB-based Vienna 5G SL [39], it allows simulation of the entire stack and not just the lower layers. Finally, Simu5G also offers the possibility to perform emulation activities [40], [41].

This simulator includes appropriate modeling of both the protocol stack and the transmission channel as specified by 3GPP Rel. 16 for the data plane [42]. Fig. 2 illustrates the basic structure of a 5G network.

In particular, the 5G network is managed by a base station (i.e., gNodeB, gNB), which can be considered an evolution of the older 4G ones (eNodeB, eNB). It is worth noting that the simulator offers total compatibility with the 4G network, allowing the simulation of mixed 4G/5G scenarios. In fact, each user device (UD) can forward messages to the nearest gNB, through the so-called RAN where data communication occurs at open system interconnection (OSI) layer 2.

C. Simulation Setup and Parameters
In the simulated grid shown in Fig. 3, each black dot represents a PMU responsible for collecting measurements. The simulation is implemented using the Simu5G framework in OMNeT++, where UDs collect measurements and transmit them through a set of 5G base stations (gNBs).

The location of the 5G base stations (gNBs) is crucial for effective communication. The positioning should aim to serve as many UDs as possible while maintaining good communication quality. The distance between UDs and gNBs can affect latency and packet loss, making it important to optimize the placement of gNBs. Increasing the number of gNBs improves network coverage, reduces distance to the nearest base station, and helps distribute the network load evenly, especially in densely populated areas.

In this work, starting from the given configuration in Fig. 3, we scale the number of gNBs studying the impact of the number of gNBs on the communication delay and packet loss. We consider different scenarios where at each simulation we increment the number of gNBs by 1, starting from 1 up to 15. The position of each gNB is selected in such a way that it can cover multiple UDs. In particular, to optimize the gNBs positioning, we exploited the k-means algorithm. The k-means algorithm is a clustering algorithm that aims to partition n points into k clusters in which each point belongs to the cluster with the nearest mean, serving as a prototype of the cluster. In our simulations, the number of points n is fixed and equal to the number of UDs. At each simulation iteration, we increment the number of clusters k. Then the gNBs are placed on the centroid of the clusters.

To simulate a realistic environment with high gNB density, we employ the 3GPP TR 38.901 channel model for urban microcells, accounting for factors like fading, shadowing, and interference. The carrier frequency is set to 2 GHz. To enhance spectral efficiency, reduce latency, and improve reliability, we utilize adaptive modulation and coding (AMC), which dynamically adjusts the modulation and coding rate based on channel conditions.

In this work, we leverage the capabilities of the 3GPP Rel. 16 standard for establishing private 5G networks, also known as mobile private networks (MPNs). The objective was to achieve dedicated networks that provide secure, high-speed, and low-latency connectivity. Creating fully private 5G networks, where ownership of all equipment, systems, and private clouds is required, can be quite expensive to operate. Alternatively, a more effective approach is to adopt hybrid private-public cloud 5G networks. In this setup, power grid operators have the option to own or lease on-premises equipment. Another viable solution is utilizing the newly introduced network slicing capability. By utilizing network slicing, the aim is to obtain a network exclusively dedicated to the specific requirements of the task at hand. This network is effectively “separated” from the public 5G network, ensuring enhanced security and optimized performance. One of the key advantages of using a private 5G network through network slicing is the ability to address issues related to interfering nodes and traffic congestion. Overall, the focus is on establishing a dedicated infrastructure that meets the specific demands of the power grid application, providing reliable and efficient communication while ensuring the isolation and quality of service required for critical operations. For these reasons, in our simulation setup, we have made the realistic assumption of not considering interfering traffic. This assumption is justified by the availability of two key solutions: private 5G networks and bandwidth reservation with support for TSN in public 5G networks.

In addition to the above considerations, the 5G network is simulated using specific parameters listed in Table I.

TABLE I Parameters Used for the Simulations
Table I- Parameters Used for the Simulations
SECTION IV.Experimental Results
The positions of the gNBs obtained using the k-means algorithm are visualized in Fig. 4, presenting the first set of results. The distribution of gNBs generally reflects the density of UDs in the grid. This strategy is advantageous as it allows gNBs to be located near areas with a higher concentration of UDs, optimizing communication delays and minimizing packet loss. Conversely, UDs situated farther away from the gNBs may experience increased delays and packet loss.

Fig. 4. - Position of the devices in the simulated network. Stars represent the UDs, i.e., the PMUs. Circles represent the position gNBs according to the k-means algorithm. The hue of the circles represents the number of clusters, i.e., the number of gNBs. Notice that in some cases the circles are not visible because they are overlapped.
Fig. 4.
Position of the devices in the simulated network. Stars represent the UDs, i.e., the PMUs. Circles represent the position gNBs according to the k-means algorithm. The hue of the circles represents the number of clusters, i.e., the number of gNBs. Notice that in some cases the circles are not visible because they are overlapped.

Show All

Furthermore, it is observed that with an increasing number of gNBs determined by the k-means algorithm, in several cases, the gNBs are positioned in close proximity to the UDs. This outcome is not surprising, as the algorithm aims to cluster the UDs and place gNBs at the centroids of these clusters. Therefore, it is expected that in such scenarios, the gNBs and UDs share similar positions.

By employing the k-means algorithm to determine the optimal positions of the gNBs, the network can effectively adapt to the spatial distribution of UDs, enhancing the overall communication performance. However, it is important to consider that the positioning of gNBs should strike a balance between minimizing latency and packet loss for UDs near the gNBs and ensuring acceptable performance for UDs situated farther away. Also, economic aspects should be taken into account, as positioning a large number of gNBs may not be cost-effective or practically feasible. Fig. 5 reports the mean inter-gNB distance and the mean distance from UDs to the closest gNB varying the number of deployed gNBs.

Fig. 5. - Mean inter-gNB distance (blue) and mean distance from UDs to the closest gNB.
Fig. 5.
Mean inter-gNB distance (blue) and mean distance from UDs to the closest gNB.

Show All

For each clustering configuration, we conducted measurements of latency and packet loss. In our setup, depicted in Fig. 6, we implemented an “edge-to-edge (E2E)” scenario where data from the PMUs is transmitted to the first substation (UD[0]). This scenario represents the worst case scenario as it involves multiple RAN latencies resulting from the transmission across the 5G network, as well as delays introduced by the backhaul network connecting the gNBs to the server. Latency is measured as the time taken for a data packet generated at a UD to be received at the destination device, UD[0]. This latency measurement includes all the transmission delays within the 5G network and the backhaul network. To assess the reliability of the network, we calculated the packet delivery ratio (PDR) using the (1). The PDR represents the ratio of successfully delivered packets to the total number of packets transmitted. It provides an indication of the network’s ability to deliver data packets reliably. By analyzing latency and PDR under different clustering configurations, we can evaluate the performance of the network and understand how the placement of gNBs impacts these metrics. This analysis will help us determine the optimal number and positioning of gNBs to achieve the desired latency and reliability targets for the PMU-based distributed measurement system
PDR=#correctly delivered packets#total sent packets⋅100.(1)
View SourceRight-click on figure for MathML and additional features.

Fig. 6. - Network simulated in Simu5G-OmNet++.
Fig. 6.
Network simulated in Simu5G-OmNet++.

Show All

Furthermore, for each scenario, we conducted three simulations employing different transport layers and packet delivery techniques, namely user data protocol (UDP), transmission control protocol (TCP), and UDP with redundant connections over multiple cells. Each technique offers a unique set of advantages and disadvantages. UDP is a lightweight and efficient protocol, well-suited for applications that require low overhead and minimal latency. It does not guarantee packet delivery or order, making it suitable for real-time applications. However, it lacks error recovery and flow control mechanisms. TCP is known for its reliability, ensuring the delivery of data packets, maintaining their order, and implementing flow control. However, it comes with higher overhead due to its error-checking and connection establishment processes, making it less suitable for real-time applications and potentially introducing complexity. In our utilization of the last technique, which is UDP with redundant connections over multiple cells, we harness the capability of 5G-enabled devices to simultaneously connect to 5G (gNBs) and LTE (eNB) ground stations. This approach allows us to establish multiple connections to the same devices, utilizing distinct and independent communication paths. Theoretically, this should increase the probability of successfully delivering packets. In our simulations, we assume that the connection to the 5G network is reserved, implying that we are either connected to a private 5G network or have a dedicated bandwidth allocation within a public 5G network. In contrast, the connection to the LTE network is not reserved and is treated as a public network, with no dedicated bandwidth allocation. Our expectation is that the majority of packets will be delivered through the 5G network, resulting in latencies similar to the UDP scenario. Lost packets on the 5G network will received by the end device through the LTE network, incurring higher latencies due to the presence of interfering traffic. By employing this technique, we anticipate achieving a better PDR and latency similar to that of the UDP scenario.

A. User Data Protocol
Fig. 7 illustrates the results of the simulations, presented as cumulative distribution functions (cdfs) of communication delay with varying numbers of gNBs. Additional detailed statistics can be found in Table II. Regardless of the number of gNBs, the cdfs exhibit similar trends, and in all cases, the latency remains below the target of 100 ms. However, as expected, increasing the number of gNBs yields significant benefits in terms of latency, standard deviation, and PDR. Table II shows that the mean latency, standard deviation, and PDR improve as the number of gNBs increases. It is important to note that beyond a certain number, increasing the number of gNBs does not provide significant advantages. This observation is evident in Fig. 7 and further supported by the similarities in the cdfs and statistical values (mean, standard deviation, and PDR) listed in Table II for 9–15 gNBs. This finding suggests that there is an optimal range for the number of gNBs that offers the desired performance improvements in latency and reliability. Going beyond this range may not yield substantial additional benefits and could result in unnecessary infrastructure costs. Therefore, careful consideration should be given to determining the appropriate number of gNBs for the PMU-based distributed measurement system to achieve the desired performance targets while balancing the economic aspects associated with deploying and maintaining the 5G infrastructure.

TABLE II Statistics of the Communication Delay and Packet Loss Varying the Number of gNBs While Maintaining Fixed the Number of UDs
Table II- Statistics of the Communication Delay and Packet Loss Varying the Number of gNBs While Maintaining Fixed the Number of UDs
Fig. 7. - CDF of the communication delay for the E2E scenarios.
Fig. 7.
CDF of the communication delay for the E2E scenarios.

Show All

In a real-world network, it is reasonable to expect that the system operator aims to find the most suitable trade-off between infrastructure costs and minimum guaranteed performance. Given the topology of the considered network, this heuristic analysis suggests that nine gNBs represent a promising and effective solution. Indeed, as stated in the introduction, we aim for a latency below 100 ms, which is achieved even with a single gNB. However, as shown in Table II, when we also consider the PDR, increasing the number of gNBs brings substantial improvements in both mean latency and PDR. Considering all the reported performance metrics, nine gNBs is the lowest number that nearly achieves the maximum performance across all scenarios. Increasing the number of gNBs beyond nine does not provide any substantial advantage. However, the optimal solution depends on the specific application requirements, involving a trade-off between deployment costs, latency, and PDR. In such cases, the optimal solution can be determined using a proper cost function that takes these aspects into account. On the other hand, these considerations strongly depend on the requirements of the PMU measurements’ application and on the performance target set by the system operator or by the regulator.

B. Transmission Control Protocol
In this section, we present the results obtained using the TCP protocol. We maintained the same network structure as in the previous experiment but replaced UDP with the TCP transport protocol. It is important to note that the Nagle function in TCP has been disabled. As a result, packets are transmitted as they are without aggregating multiple TCP packets into a single one. Fig. 8 illustrates the cdfs, while Table III provides detailed statistics. Upon examining both the figure and the table, some unexpected differences become apparent.

TABLE III Statistics of the Communication Delay and Packet Loss Varying the Number of gNBs While Maintaining Fixed the Number of UDs Using TCP Transport Protocol
Table III- Statistics of the Communication Delay and Packet Loss Varying the Number of gNBs While Maintaining Fixed the Number of UDs Using TCP Transport Protocol
Fig. 8. - CDF of the communication delay using TCP as the transport protocol.
Fig. 8.
CDF of the communication delay using TCP as the transport protocol.

Show All

Compared to the UDP experiment, we observed that with a low number of gNBs (ranging from 2 to 7), both latency and PDR worsened. The mean latency in the majority of cases reached several thousand of milliseconds, and the PDR dropped to approximately 60% in the worst case. These results were unexpected since we anticipated an improved PDR with TCP at the expense of only a few milliseconds in latency.

During these simulations, we noticed that using TCP led to roughly double the amount of traffic compared to UDP due to the exchange of data and ACK packets. The last gNB, which is connected to UD[0], experienced the most significant impact from this traffic increase. It had to manage both inbound and outbound traffic from UD[0] to other UDs, as well as connections to other UDs, resulting in a noticeable increase in latency and a worsen in PDR. Also, the link quality is primarily influenced by path loss, which is distance-dependent. When the loss approaches or exceeds the sensitivity threshold of the UD, link quality deteriorates rapidly, leading to poorer performance.

Conversely, when there was a high number of gNBs (ranging from 8 to 15), the TCP protocol performed as expected, achieving a 100% PDR and only a slight increase in latency of few milliseconds. In these scenarios, traffic distribution was more balanced, and the gNB connected to UD[0] only had to handle inbound and outbound traffic, without the additional burden of connecting to other UDs. Traffic from other UDs reached the gNB associated with UD[0] through a backhaul network with significantly higher capacity, leading to lower introduced latency and packet loss.

All in all, these TCP experiments seem to confirm our earlier findings with UDP. It appears that there is an optimal (or minimal, if we aim to minimize operational costs) number of gNBs required to meet latency and packet loss requirements. In the specific case of TCP, with eight gNBs, we were able to achieve the target latency of 100 ms and eliminate packet loss.

C. UDP With Redundant Connections Over Multiple Cells
In this series of experiments, we made slight adjustments to the simulation scenario to incorporate the capability of 5G-enabled devices to connect simultaneously to 5G (gNBs) and LTE (eNB) ground stations. As depicted in Fig. 9, this approach enables the establishment of multiple connections to the same devices, utilizing distinct and independent communication paths.

Fig. 9. - Connection scenarios in UD. (a) Single connection to either the 5G or LTE network. The UD can switch to one connection to another. (b) Dual connection to both the 5G and LTE networks. The UD is connected to both networks simultaneously [43].
Fig. 9.
Connection scenarios in UD. (a) Single connection to either the 5G or LTE network. The UD can switch to one connection to another. (b) Dual connection to both the 5G and LTE networks. The UD is connected to both networks simultaneously [43].

Show All

In our scenarios, we deployed two LTE eNBs strategically located to serve the two primary clusters of UDs on the right and left sides of the operational environment. To prevent mutual interference, we configured the two eNBs to operate on different carrier frequencies compared to the gNBs. Other parameters, such as transmission power, remained unchanged. To create a more realistic scenario, we introduced additional devices connected to the eNBs to simulate connections to a public LTE network. In practice, apart from the PMUs, 400 UDs were connected to the LTE network, with 200 per eNB, exchanging data at a constant bitrate of 1 Mb/s with the backhaul network or other public UDs connected to the LTE network. Regarding the 5G connection, we maintained the same configuration as in the UDP simulations, assuming that the connection to the 5G network is reserved. This implies that we are either connected to a private 5G network or have a dedicated bandwidth allocation within a public 5G network.

In these scenarios, the PMUs simultaneously send data packets on both connections. Upon reaching the receiving UD, the packets may arrive at different times. In such cases, the UD considers the first received packet as valid and discards the others. As specified in the standard, packets contain a sequence number that facilitates the identification of already received or out-of-order packets. This way, the UD can keep track of received packets and discard duplicates.

By implementing a redundant connection, we expected to improve the PDR compared to the UDP scenario. In terms of latency, packets received through the 5G network should exhibit latencies similar to the UDP scenario, while the packets lost on the 5G network but received through the LTE network should have higher latencies due to the presence of interfering traffic.

The results of these simulations are presented in Fig. 10 and Table IV, which, respectively, report the cdfs and detailed statistics.

TABLE IV Statistics of the Communication Delay and Packet Loss Varying the Number of gNBs While Maintaining Fixed the Number of UDs Using UDP With Redundant Connections
Table IV- Statistics of the Communication Delay and Packet Loss Varying the Number of gNBs While Maintaining Fixed the Number of UDs Using UDP With Redundant Connections
Fig. 10. - CDF of the communication delay using UDP with redundant connections.
Fig. 10.
CDF of the communication delay using UDP with redundant connections.

Show All

As evident, the results regarding PDR align with our expectations. Even with just two gNBs, we achieve the same PDR as in the UDP scenario with seven or more gNBs. Packets received through the LTE network exhibit high latencies, primarily due to interfering traffic. It should be noted that when considering the different scenarios, we keep the number of eNBs fixed at two while changing the number of gNBs as explained. We placed the eNBs such that each serves roughly 50% of the UDs. Therefore, since the number of UDs and eNBs is kept constant across the simulations, we expect similar latency when only considering the connection between the eNB and the UD. However, the variability in latency should be attributed to the backhaul network and how the different streams of traffic (5G and LTE) are handled and prioritized with respect to the 5G traffic in different segments of the backhaul. Unexpectedly, the latency on the 5G network is higher compared to the simulations using plain UDP. The reasons for these observations include the fact that we are considering the worst case scenario in which all PMUs generate packets synchronously, meaning they all transmit at the same time. With a limited number of gNBs, the communication paths are few, resulting in consistent delays for all packets. Since the delays are uniform, all packets arrive at the receiving node simultaneously. Especially with active redundancy, the number of packets reaching the application layer of the receiving node is high. Consequently, these packets are queued and processed one at a time, introducing delays. As the number of gNBs increases, the communication paths become diverse, leading to varying delays when reaching the receiving node. This reduces congestion in the application state, resulting in lower overall latency.

With an increase in the number of gNBs to 4, the latency on the 5G network noticeably decreases to a level comparable to the plain UDP experiment. However, the latency on the LTE network remains high. In terms of PDR, there is an improvement compared to the plain UDP experiment, but we are still unable to reach 100%. To see improvements in both metrics, we need to increase the number of gNBs to 6. In this scenario, we achieve a 100% PDR, with the latency on the 5G network averaging 20 ms, well below the target latency of 100 ms. Nonetheless, some issues persist with the LTE network, as the latency remains in the hundreds of milliseconds range.

These results from this set of experiments seem to reaffirm the notion that there is an optimal number of gNBs required to meet latency and packet loss requirements, which, in this case, appears to be 6. The majority of packets reach UD[0] through the 5G network with low latency. The redundancy in the LTE network significantly improves PDR but comes at the cost of higher latency for packets lost on the 5G network.

D. Bandwidth Analysis
As we assume bandwidth reservation for the 5G network, especially in the case of a public 5G network, it becomes crucial to estimate the total bandwidth usage, as this directly impacts operational costs. To assess the total bandwidth consumption, we measured both outbound and inbound traffic related to the IEC61850 protocol on the PMUs. This approach considers only the specific traffic while disregarding other types of control traffic, such as those associated with 5G network management, which may be specific to the service provider. It is important to note that in scenarios using UDP, only outbound traffic is relevant to communication, as there is no response from the receiving UD. In TCP scenarios, both inbound and outbound traffic matter since TCP Acknowledgments (ACKs) are integral parts of the communication protocol.

The bandwidth utilization data is presented in Table V. The table provides a clear overview of the different scenarios and their respective network usage.

TABLE V Bandwidth Utilization on the Different Scenarios
Table V- Bandwidth Utilization on the Different Scenarios
The results indicate that UDP with redundant cells and the plain UDP scenario consume the same bandwidth, if we consider only the 5G network. In contrast, the TCP scenario utilizes more bandwidth, significantly impacting operational expenses. These bandwidth figures are essential considerations when evaluating the cost-effectiveness of each technique.

E. Discussion of the Results
The obtained results so far allow us to draw some insights into the proposed techniques. It is our opinion that the choice of technique depends on application requirements, performance criteria, and operational expenses.

The simplest solution is to use plain UDP, which guarantees the lowest latency among the three techniques. However, it is suitable for PMU systems that implement control strategies robust to packet loss since it ensures a 97% PDR in the best case, even with a relatively small number of deployed gNBs.

On the other hand, TCP offers better PDR performance with comparable latency but comes at a higher operational cost. This approach necessitates deploying a greater number of gNBs to achieve the same performance as UDP and requires a higher amount of bandwidth reservation (if in a public 5G network) due to the increased data exchange (including data, ACKs, and control packets).

Lastly, the UDP with redundant connections over multiple cells technique can be deployed in PMU applications intolerant of packet loss but robust against communication delays. In this case, a 100% PDR is achievable, albeit with slightly higher latency for packets lost on the 5G network. Operational expenses are estimated to be lower compared to TCP, as it requires fewer gNBs and can rely on the legacy public LTE network. The amount of reserved bandwidth on the 5G network remains the same as in the plain UDP scenario.

Hence, a thoughtful evaluation of the specific application requirements and performance targets is essential in determining the most suitable technique.

SECTION V.Scalability Analysis
Based on these findings, we conducted an additional set of measurements to assess the scalability in terms of the number of UDs. For this evaluation, we kept the number of gNBs fixed at 9 and varied the number of UDs from 9 to 153. To ensure realistic scenarios, we utilized the positions of the nine gNBs obtained from the previous simulations using the k-means algorithm. Subsequently, we randomly placed UDs within a 300-m radius from their corresponding gNBs. In the first simulation, we had one UD for each gNB, in the second simulation, we had two UDs for each gNB, and so on. The objective of this experiment was to determine the maximum number of UDs that could be deployed while maintaining a latency below the target threshold of 100 ms. By gradually increasing the number of UDs, we aimed to identify the point at which the latency exceeded the desired limit.

The results are presented in Fig. 11, and the corresponding statistics are shown in Table VI. It is evident that increasing the number of UDs leads to a rapid deterioration in latency. According to the mean value, it is possible to deploy up to 99 UDs, equivalent to 11 UDs per gNB, before the latency exceeds the target threshold of 100 ms. However, relying solely on the mean value may not accurately represent the overall network performance. Since reliability is a crucial factor, it is essential that the majority of measurements reach the destination promptly. In this context, the 99th percentile offers a more suitable metric for evaluation. By considering this metric, as indicated in Table VI, the maximum number of UDs that can be deployed while maintaining the desired performance targets is 36, equivalent to four UDs per gNB. Beyond this threshold, the network struggles to reliably deliver all packets, resulting in latency surpassing the target threshold of 100 ms. It is important to note that the 99th percentile captures the upper tail of the latency distribution, providing insights into the worst case scenarios. These findings highlight the limitations of scalability in terms of the number of UDs. As the number of UDs increases beyond a certain threshold, the network’s performance deteriorates, and the desired latency targets become challenging to achieve. Therefore, careful consideration should be given to network capacity planning and resource allocation to ensure reliable and efficient communication in scenarios with a high number of UDs.

TABLE VI Statistics of E2E Latency Incrementing the Number of UDs
Table VI- Statistics of E2E Latency Incrementing the Number of UDs
Fig. 11. - E2E latency incrementing the number of UDs.
Fig. 11.
E2E latency incrementing the number of UDs.

Show All

SECTION VI.Simulation on a Real Deployment and Sensitivity Analysis
We finally simulated a real deployment, represented in Fig. 12. The scenario is adapted from [44], which defines the topology of the grid, as well as the placement of the PMUs and base stations. Specifically, this deployment comprises a total of 18 PMUs, as in the simulation scenario we have considered so far, along with eNBs (LTE cells). We implemented this scenario in OMNeT++, using the same locations and substituting the eNBs with gNBs. In the simulation, we placed the PMUs (i.e., the UDs) at ground level, while positioning the gNBs at 10 m above the ground. This hypothesis was made because we only have 2-D geospatial information of the test field instead of 3-D information. Additionally, we assume that the PDC is located in the southernmost marked location in Fig. 12. We considered UDP as transport protocol and the other simulation parameters are the same as those considered so far and are reported in Table I.

Fig. 12. - Placement of PMUs (blue circles) and gNBs (red stars) in the real application scenario. PDC is the southernmost blue circle. Adapted from [44].
Fig. 12.
Placement of PMUs (blue circles) and gNBs (red stars) in the real application scenario. PDC is the southernmost blue circle. Adapted from [44].

Show All

For this scenario, we adopted a Monte Carlo approach, repeating the experiments 30 times, each with a different random number generator seed. This allowed us to define a confidence interval within which the simulation can be considered reliable.

The results of these simulations are shown in Fig. 13, while the detailed statistics are reported in Table VII. Looking at the overall statistics, it is noticeable that the obtained results are close to those considered in the previous scenario. Indeed, we obtained an average latency of 17.35 ms and a PDR close to 89% across all the considered simulations. This similarity is not surprising since, even in the real setup, the gNBs are placed close to the high-density areas, just as the k-means algorithm suggested in the previous simulations.

TABLE VII Statistics of the Communication Delay and Packet Loss on Different Simulation Runs in the Real Scenario
Table VII- Statistics of the Communication Delay and Packet Loss on Different Simulation Runs in the Real Scenario
Fig. 13. - Statistics of the communication delay on different simulation runs in the real scenario.
Fig. 13.
Statistics of the communication delay on different simulation runs in the real scenario.

Show All

Regarding the sensitivity of these results, considering the mean values of the latency and the PDR, and using a 95% confidence interval, we obtain
CILatencyCIPDR=[17.03,17.65] ms=[86.86,90.20]%.(2)(3)
View SourceRight-click on figure for MathML and additional features.

For latency, the narrow confidence interval implies that the latency results are reliable, with just minor sensitivity to changing random seeds. While the PDR exhibits greater variability than latency, the interval stays quite narrow, indicating consistent network performance across simulated runs.

Overall, these results indicate that the simulation is robust, with predicted performance metrics that are rather insensitive to initial random conditions. The confidence intervals show that the observed findings are a good estimate of actual performance under the simulation settings.

SECTION VII.Conclusion
In this article, we evaluated the scalability of 5G infrastructures for the transmission of IEC 61850 data. In this context, latency is a fundamental parameter to assess since timely delivery of measurements collected by PMUs across substations is essential, and communication delays directly impact the accuracy of voltage phasor reconstruction. We investigated the influence of factors such as the number and spatial distribution of gNBs, as well as the number of UDs, on communication latency. The results obtained provide valuable insights for optimizing the deployment and positioning of gNBs and assessing the network’s scalability to accommodate a large number of UDs while meeting latency and reliability requirements. These findings serve as guidance for the design and implementation of PMU-based distributed measurement systems, effectively balancing performance needs and economic considerations to ensure efficient and reliable communication. Future works will address various aspects, including comparing alternative communication solutions like fiber optics or power line carrier (PLC)-based communication. Additionally, the potential cybersecurity issues associated with 5G-based communication systems will be investigated.