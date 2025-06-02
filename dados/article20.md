Title: On the Industrial Leadership and Involvement
in the LwM2M IoT Ecosystem

ABSTRACT
The importance of standards, and especially ICT standards, in the
IoT domain is widely recognised. Implementations of standard specifications provided as Open Source Software (OSS) promote interoperability and longevity of systems and create conditions for avoiding
lock-in, and industrial involvement is important since it can affect
community dynamics and will to contribute. The overarching goal
of this study is to characterize the industrial leadership and involvement in the LwM2M (Lightweight machine to machine) ecosystem.
Specifically, the main focus of the study is on involvement with
OSS projects implementing LwM2M elements by individuals who
cooperate in projects that implement or use the LwM2M standard
in their projects. This can be done by analyzing the commits to the
git repository, the bugs issued and commented in the bug-tracking
system and the pull requests performed in the project. Techniques
will be applied to merge authors using different identities (i.e., different e-mail addresses). By means of identifying the affiliation of
those individuals we plan to analyze the involvement of companies
in those projects, and thus how they are present in an IoT standard,
in this case LwM2M.
CCS CONCEPTS
• Software and its engineering → Collaboration in software
development.
KEYWORDS
IoT, software ecosystem, industry, OSS, LwM2M

1 INTRODUCTION
ICT (Information and Communications Technology) standards are
important for several reasons, including: interoperability (they ensure that different ICT products and services can work together
seamlessly), innovation (they provide a common basis for innovation), competition (they promote competition by creating a level
playing field for all ICT providers), security (they can help improve
security by providing a common framework for security measures),
and trust (they can help build trust in ICT products and services).
Implementations of standard specifications provided as Open
Source Software (OSS)1 promote, in addition to the aforementioned
characteristics, longevity of systems and create conditions for avoiding vendor lock-in, i.e., a user is not forced to continue using a
product or service, because switching to another vendor is not practical. It has been reported that strategic use of OSS, and strategic
engagement with OSS projects, in company contexts can effectively
address the fundamental challenges of lock-in, interoperability, and
longevity of software and associated digital assets [13].
The field of Internet of Things (IoT) is thus full of standards,
and some of them are implemented in OSS. One of them is the
Lightweight M2M (LwM2M) standard2
. LwM2M is a protocol for
device management and service enablement in IoT. It is designed
for constrained devices, such as microcontrollers and sensors, that
have limited processing power and memory. The goal of LwM2M
is to be a lightweight and efficient protocol that can be used to
manage a wide range of devices, including smart meters, wearable
devices, and industrial controllers.
There are many stakeholders involved in the development and
deployment of LwM2M, forming a software ecosystem of industrial
companies, consortia, universities, research institutes and individuals.
Overall, industrial leadership and involvement in protocols and
standards is essential for the continued growth and development of
the ICT industry. By participating in the development of protocols
and standards, companies can help to ensure that the industry
continues to thrive and that consumers benefit from the latest
innovations. For instance, the development of the TCP/IP protocol
stack has been very relevant for the widespread use of the Internet.
TCP/IP was developed through the open collaboration of industry
leaders, and the success of TCP/IP is a testament to the power of
open standards [18].
The overarching goal of this study is to characterize the industrial
leadership and involvement in the LwM2M ecosystem. Specifically,
the main focus of the study is on engagement with OSS projects
implementing LwM2M elements by individuals who cooperate
in projects that implement or use the LwM2M standard in their
projects. This can be done by analyzing the commits to the git
repository, the bugs issued and commented in the bug-tracking
system and the pull requests performed. Techniques will be applied
to merge authors using different identities (i.e., different e-mail
addresses). Finally, by assigning developers to the companies where
they are employed, we study the companies’ involvement in the
ecosystem as well as their collaboration links.
From the main goal, we derive four research questions:
• RQ1: How are individuals involved in the LwM2M ecosystem?
• RQ2: Who is involved in multiple LwM2M projects?
• RQ3: How are companies involved in the LwM2M ecosystem?
• RQ4: What companies have involvement in multiple LwM2M
projects?
The structure of the paper is as follows: First, we provide some
background on LwM2M together with related research in Section
2. The research approach is described in Section 3. In Section 4,
results are presented. Discussion and implications for research and
practice can be found in Section 5. Finally, conclusions are drawn
and future directions of research are pointed out in Section 6.
2 BACKGROUND & RELATED WORKS
Lightweight M2M (LwM2M) is an Open Mobile Alliance protocol for
machine-to-machine (M2M) or IoT device management and service
enablement [20]. The LwM2M standard defines the application
layer communication protocol between a LwM2M server and a
LwM2M client, which is located on an IoT device [22]. It offers
an approach to IoT device management and allows devices and
systems from different vendors to coexist in an IoT ecosystem.
LwM2M was originally built on top of the Constrained Application Protocol (CoAP) [15], but later versions of LwM2M also
support additional transfer protocols. LwM2M’s device management capabilities include remote provisioning of security credentials, firmware updates, connectivity management (e.g., for cellular
and WiFi), remote device diagnosis and troubleshooting. LwM2M’s
service enabling capabilities include sensor and meter readings,
remote actuation, and host device configuration.
In combination with the LwM2M protocol, the LwM2M Objects
data model supports the various LwM2M use cases. The data model
is extensible and capable of supporting applications for various
types of industries.
For software intensive companies that develop and use solutions
in the IoT domain it is essential to comprehend how different stakeholders are engaged with, and to what extent they contribute to,
different software projects implementing standards (such as, for
example, the LwM2M standard) which are important for the IoT
domain. Despite extensive company interest in many OSS projects
there is limited research addressing how different stakeholders engage with OSS projects implementing standards in the IoT domain.
IoT has gained significant attention and is expected to support
various emerging domains. Operating system (OS) support for
IoT plays a crucial role in developing scalable, interoperable, reliable, and efficient applications. Qutqut et al. offer a comprehensive
overview of common and existing OSS OSs for IoT, categorized
based on their design and development aspects [14].
Algren et al. have previously emphasized the significance of
interoperability and open data in smart cities [1]. The authors
underscore that institutions become tethered to a vendor’s system
once they have made an investment in it. The challenge in this
scenario lies in providing an open system that empowers users to
access open data and cloud services without becoming beholden to
a specific platform.
Rose et al. argue that so-called “walled gardens" restrict users’
access to the full potential of the Internet, limiting its social, political, and economic benefits [17]. These walled gardens only allow
users to interact with a select group of websites and services, hindering the free flow of information and innovation. They point
out that some device manufacturers create proprietary ecosystems,
essentially walled gardens, to gain a competitive edge in the IoT
market. By limiting interoperability to devices within their own
brand, these manufacturers lock users into their ecosystem, making
it difficult and costly to switch to a different brand or use components from other vendors. This strategy can be seen in the home
automation market, where light bulbs from one company may not
work with the light switches or control systems of another.
Gamalielsson et al. present an investigation of a standard in the
web domain (RDFa) and its implementation in OSS; this work is one
of (very few) ones that have investigated organizational influence
between a specific software standard (RDFa) and an OSS project
that implements this standard [5].
Lundell et al. present seven practical guidelines for developing,
using, and deploying software in diverse contexts which include
guidelines for OSS implementations of ICT standards, offering a
valuable resource for any organization [9]. Drawing on the experiences of individuals and organizations in the primary and secondary software sectors, the article proposes and elaborates on
effective organizational strategies and guidelines for utilizing OSS
and open standards. These strategies and guidelines emphasize how
enterprises can harness the opportunities presented by engagement
with OSS projects and their associated communities. The guidelines include also recommendations for addressing the relationship
between ICT standards and OSS projects.
Lundell et al. have investigated legal and licensing conditions
for implementation and use of the HEVC (High Efficiency Video
Coding) standard by software projects [12]. Specifically, the study
investigated the possibility of obtaining the complete technical
specification of the standard and obtaining licenses for all standard essential patents from patent holders that would allow for
implementation and use of the standard by a software project. The
study shows complexities related to an evolving specification and
findings show that it is impossible to obtain patent licenses that
would allow for implementation and use of the standard by an OSS
project, something which underscores the complexities involved in
implementing and utilizing the HEVC standard in software.
Teixeira et al. explore how rival firms collaborate in the OpenStack, an OSS cloud computing platform for public and private
clouds [19]. It is important to note that software development is
increasingly being done nowadays by a network of individuals and
organizations collaborating on OSS projects, creating OSS ecosystems. The authors found that competition for the same revenue
model and homophily (the tendency of individuals to associate and
bond with similar others) do not necessarily hinder collaboration,
providing insights into coopetition (a strategic business approach
that involves both cooperation and competition with other companies) strategy and high-tech entrepreneurship.
3 RESEARCH APPROACH
To identify the projects of the LwM2M ecosystem in GitHub, a
search was carried out in the GitHub API using the term “LwM2M”,
resulting in 374 repositories. The repositories returned by the
GitHub API are non-fork repositories, i.e., they are not repositories forked from other repositories. For all these repositories the
following information has been retrieved: Activity in (1) the bugtracking system, with information on who has added new bug
issues and who has commented on them; (2) pull-requests, with
information about who made a pull request and who commented on
it; and (3) the git version control repository, with information
about the authors of the commits.
To collect this information, the GrimoireLab Perceval tool [4]
from the CHAOSS project of the Linux Foundation was used. GrimoireLab Perceval provides a command line interface and Python
API to obtain data from many data sources (e.g., GitHub, git, Bugzilla,
Jira, mailing lists), serving as a single interface for data collection.
For the bug-tracking system and pull-request functionality, GrimoireLab Perceval offers an interface to the GitHub API, which
automatically manages, for example, the limit of requests per hour
that GitHub has set so as not to overload its servers. To mine the
version control system, GrimoireLab Perceval makes a local copy
of the latest version of the repository and analyzes its log. The
information retrieved from the three sources is offered as JSON
files, from which the information can be easily extracted.
From the JSON files, the authorship fields are extracted. For git
this usually means to have a string that includes the full name and
an email address (e.g., “John Smith < john.smith@domain.edu >”).
However, for the interactions in pull requests and bug issues, it
is only composed of a username (e.g., jsmith). This means that an
individual may have several identities [16], which have to be merged
into a single one. There have been several disambiguation heuristics
studied in the research literature [23]. In this analysis we have used
gambit [6], a disambiguation tool designed for version control
systems which significantly outperforms previous disambiguation
algorithms. We have expanded gambit to include data from pull
requests and issues.
The disambiguation process, after optimization for the current
research, takes 33 minutes, and the 8838 original identities are
merged into 7842 identities.
Among the 7842, we have found many bots, which have recently
become very popular in OSS development projects [2]. We found
and removed the following (18 in total): ReadmeCritic, dependabot, release bot, leshan-bot, snyk-bot, emqx-ci-robot, renovate
bot, monty-bot, dependabot-preview, github-actions, greenkeeper,
weekly-digest, fossabot, github-code-scanning, sync-by-unito, codecov, copilot4prs, and jenkins.
Another identity that we have removed is the ghost user. This
user is used in GitHub to take the place of user accounts that have
been deleted.
Obtaining information on which companies collaborate on projects
in the LwM2M ecosystem is of great interest, as it would allow us to
discern industrial interest in the standard and how companies are
getting involved. Unfortunately, it is not easy to obtain this information publicly. Our approach consists of attributing the activity
of their employees to companies. Although you could search the
developers’ personal pages on GitHub or the LinkedIn website3
,
this is still a laborious task as it generally requires a manual, laborintensive verification. Within this study, we determine affiliation
based on email domains. If we encounter an email address like
company.com among the multiple email addresses associated with
a developer after the disambiguation phase, we assume that the
developer belongs to the company associated with that domain.
We also investigate which companies have collaborated with
other companies in the LwM2M ecosystem. Therefore, we have created a social network of collaborating companies. In order to avoid
noise, we have set a minimum threshold of 4 actions (4 commits, 4
pull request posts or 4 bug issue actions) that developers affiliated
to a company have to perform to be part of the network. The results
are analyzed and visualized using NetworkX [7], a Python package
for the creation, manipulation, and study of complex networks.
The entire process has been carried out with Python scripts,
which are made available in the article’s reproduction package
(linked at the end of the paper), along with the JSONs resulting
from the analysis.
4 RESULTS
In addition to the RQs presented above, we have added an additional
subsection to get an overview of the repositories that we have found
as part of the LwM2M ecosystem in GitHub.
4.1 Most relevant repositories in the LwM2M
ecosystem
From the 374 repositories that we have obtained from the GitHub
API, we had to remove 7 repositories, because they contained a
copy of another of the repositories under study. This happens, for
instance, for the jvermillard/leshan repository, that was moved
to the eclipse-leshan/leshan repository when the project was
taken over by the Eclipse Foundation. We also removed the 4 repositories of the OpenMobile Alliance Archive GitHub organization as
we have seen that they contain test repositories, mirrors, images
and a bulk update tool not related to the standard.
Table 1 offers an overview of the all-time most active repositories of the LwM2M ecosystem in GitHub by number of commits.
The table shows not only the number of commits per repository,
but also the number of committers, number of issues in the issue
tracking system, number of participants in the issue tracking system (including not only those who opened an issue, but also those
who have commented it), number of pull requests, and number of
participants in pull request discussions (e.g., not only the author
who submitted the pull request, but all others who have participated in it with comments). Most of the repositories in Table 1 have
activity in all sources of data (commits, issues and pull requests),
which is indicative of having a community around them. Those
repositories that have not such activity (nfi/contiki-LwM2M and
KoljaV/LwM2M_stats) are special cases, being the former inactive
since Nov 23, 2015, while the latter offers stats on LwM2M adoption,
and is thus not really a development repository.
4.2 How are individuals involved in the
LwM2M ecosystem?
After disambiguation, and removing bots, we have found 7842 distinct developers that have contributed to the 363 repositories under
study. Involvement in repositories is very unevenly distributed,
with most of the them (7,170 or 91.44%) having participated in just
one repository, as can be seen in Figure 1. This share grows to
97.36% if we consider developers who have participated in three or
less repositories. On the other hand, only 0.46% of the developers
participate in more than six repositories.
4.3 Who is involved in multiple LwM2M
projects?
Table 2 lists the developers that we have found and that have contributed to more than 9 repositories in the LwM2M ecosystem.
The highest number of repositories that a single developer has
been involved in is 18 (that is almost 20% of all repositories in the
ecosystem).
4.4 How are companies involved in the
LwM2M ecosystem?
Table 3 offers the domains that appear most frequently in the data
we have acquired. It should be noted that ‘github.user’ is the domain
that we have assigned to those users who participate in the issue
tracking system or pull requests, since email information is not included in the authorship as is done when commits are performed. In
second position we find the gmail.com domain which is not indicative of any company, but of the popular webmail service offered by
Google. In the third position we find users.noreply.github.com
which can be found in commits frequently, since there are developers who do not want to be contacted. As can be seen in Table 3,
a filtering process is necessary to obtain company domains; the
first domain that is indicative of a company is in fourth position
(arm.com) that corresponds to ARM (a British semiconductor and
software design company whose primary business is the design
of central processing unit (CPU) cores that implement the ARM
architecture family of instruction sets).
To obtain a more sanitized list, we have removed the following
domains that appear frequently: those (1) related to GitHub or other
software development platforms: ‘.user’, ‘github.com’, ‘users.sourceforge.net’,
‘synk.io’; (2) popular email service providers: ‘gmail.com’, ‘yahoo.com’,
‘hotmail.com’, among others; and (3) related to local machines: ‘.local’.
Table 4 offers the result of our filtering process by showing those
company domains for which we have found at least four developers
in the LwM2M ecosystem. After ARM, with 75 different identified
developers, we can find Sierra Wireless (a Canadian multinational
wireless communications equipment designer, manufacturer and
service provider), Imagination Technologies Limited (a British semiconductor and software design company with its primary business
in the design of PowerVR mobile graphics processors (GPUs), neural network accelerators for AI processing, and networking routers),
and ThingsBoard (an Ukrainian SME that offers a platform to design and prototype their smart solutions in garages and industrial
customers with a wide range of requirements for device management, data processing, security, privacy, analysis, etc). All in all, the
involvement of companies in LwM2M is notable, with big actors
from the ICT industry as Intel, Ericsson, Telefónica or Microsoft,
but also smaller companies specialized in the IoT field.
4.5 What companies have involvement in
multiple LwM2M projects?
The result of visualizing the network of involved companies in the
LwM2M ecosystem in GitHub can be seen in Figure 2. The dots
in the figure correspond to companies; two dots are connected
with an undirected edge if they have been involved in a GitHub
repository. We have found a total of 351 corporate email domains
in our analysis, but only those with collaborations (e.g., that have
an edge to other companies) are shown in the network.
Figure 2 shows an interesting pattern, as we can find several
(depending on how you count, five or six) clusters of repositories
where companies collaborate. These clusters are connected by one
or more companies that act as a linchpin.
If we calculate the density of the network, we obtain a value of
0.144, which means that it is not very dense. It should be noted
that if all repositories would be connected to all others, we would
have a single cluster and a density value of 1. A value of 0.144 is
indicative of a dispersed network, with several clusters.
If we analyze the network at the node (company) level, one of
the most relevant metrics is the degree centrality. Figure 3 offers an
overview of the distribution of degree (i.e., number of edges) in the
network under study (note that the vertical axis is in logarithmic
scale). As can be observed, degree is very unevenly distributed, with
a majority of companies having no links to other companies. Only
a few companies have many links, being Intel (one of the world’s
largest semiconductor chip manufacturers by revenue), the one
that has the highest amount, 46, of links to other companies, with
a degree centrality value of 0.60. Second stands the Research Institutes of Sweden (RISE, rise.se), with 17 edges. In third position, with
12 edges, we have found Nordic Semiconductor (nordicsemi.no, a
Norwegian fabless technology company that specializes in designing ultra-low-power wireless communication semiconductors and
supporting software for engineers developing and manufacturing
IoT products).
Betweenness centrality is a measure of centrality in a network
that assesses the number of shortest paths that pass through a
particular node. It indicates the node’s influence in controlling the
flow of information or resources within the network. A node with
high betweenness centrality acts as a bridge or gatekeeper, connecting different parts of the network and potentially influencing
the communication between them. In the network under study,
Intel has the highest value of betweenness centrality with 0.48.
Second is husqvarnagroup.com, a Swedish manufacturer of outdoor power products including robotic lawn mowers, chainsaws,
trimmers, brushcutters, cultivators, and garden tractors, with 0.11,
5 DISCUSSION AND IMPLICATIONS FOR
RESEARCH AND PRACTICE
Software engineering is vital for IoT to design systems that are
secure, interoperable, modifiable, and scalable. However, we still
lack the required knowledge on crucial questions like what are
the best practices for developing projects for IoT, how protocols
and standards are built. In this paper we have taken the idea of
IoT projects being an ecosystem [3, 8], and have analyzed it using
techniques from the area of mining software repositories (MSR). The
results, although still superficial, already provide an overview of one
ecosystem linked to an IoT standard, LwM2M. This information
is scattered among many repositories, and given the amount of
stakeholders (standardization bodies, companies, volunteers, among
others) it is often not easy to have a practical overview of what is
going on.
We have seen that, even for a relatively new standard such as
LwM2M, a large amount of information can be gathered and analyzed from GitHub. This information can be considered at the
individual developer level, as we have done for RQ1 and RQ2, but
it seems to be more relevant at the company level, given the many
corporations involved in the ecosystem. We argue that this information is of special interest to corporations as they can take informed
decisions on their strategy towards a technology or standard. With
an analysis as the one we have shown, companies can be aware
of where other (maybe competing companies) are working on in
an ecosystem; but it is as well a convenient way to find out where
collaboration is happening. As some scholars have noted, it is not
uncommon to find companies competing with products in the customer market and at the same time collaborating in software development efforts [19]. Nonetheless, competition is not only to be seen
in the context of a given standard, in this case LwM2M, as there is as
well competition among different standards, e.g., between LwM2M
and other M2M standards.
Standardization bodies could also benefit from an analysis like
the one presented. They could identify in what parts of the ecosystem there is active development or where industrial interest can
be found, but also the opposite: where there is no development or
industrial interest. This can help promoting those parts. Thus, we
envision that standardization bodies can use this information to
lead initiatives that better address the limitations of the ecosystem.
While we provide a method based on MSR research state-of-theart practices, including retrieval from various sources, disambiguation and bot detection, the whole process is not straightforward.
In particular, the assignment of affiliations (e.g., what individuals
work for which company) has still much room for improvement.
Concerning validity, Wohlin et al. [24] present four types of
threats to validity in software engineering: Construct validity
refers to the degree to which a study measures what it intends to
measure. Most of the limitations of this research fall under this
threat. First, even if we analyze several sources such as git repositories, pull requests and issues, we only capture part of the interactions that occur while developing software. Then, even if we apply
state-of-the-art tools for disambiguation, these are not free of errors,
and particularly when the data is not very rich (e.g., for issues and
pull requests we only have the username), this task is more complex.
Finally, the part that assigns developers to companies is the one
that is more difficult. This is because we do this assignment on
top of the disambiguation, which sometimes helps in this task (e.g.,
when a developer has a gmail address and a corporate account,
we have assigned it to the corporate account), but others is not
enough (e.g., when our disambiguation technique has not been able
to link an email address found in git with a username found in pull
requests). In addition, developers might have had several affiliations
even if the timespan of the repositories under investigation is less
than 10 years, a situation that is not infrequent in the computer
science field. Nonetheless, developers might have contributed not
providing any information of their affiliation as they have done it
with their personal email (e.g., a gmail account) address. Another
threat to construct validity is that there might be noise in the data.
That is why after each step in the analysis, the obtained results
have been manually validated. Hence, duplicated repositories, bots
and email domains have been identified and filtered out. Still we
cannot ensure that the results are free of errors. Internal validity
refers to the degree to which a study can establish a causal relationship between the independent and dependent variables. This
being observatory research, it is difficult to infer any causality from
our findings. External validity refers to the degree to which the
results of a study can be generalized to other populations, settings,
or times. This research shows a case study where we have addressed
one IoT ecosystem. As we have only analyzed GitHub repositories,
we may have missed other repositories that are related to LwM2M,
but that are not hosted on GitHub. On the other side, there might
be other repositories in GitHub that are related with the LwM2M
standard, but that have not appeared in the GitHub search, because
they do not use the term we have looked for (in the repository
name, in the Readme.md file, and in the repository keywords). Even
if difficult to generalize to other settings, learning from case studies
has shown to be of very high relevance, and it is a method that is not
uncommonly found in the software engineering research context.
Conclusion validity refers to the degree to which the conclusions
of a study are justified by the data. In this regard, we might have
failed to consider alternative explanations for the results. While this
might be difficult to avoid, we have to point out that this research
stems from collaboration involving academic researchers and IoT
stakeholders from industry. While the former have been mainly in
charge of the scientific part, the latter have supported them with
fruitful discussion, in addition to advice and feedback.
6 CONCLUSIONS & FUTURE WORK
In this paper we have seen that the involvement of industrial entities
in Open Source Software projects implementing LwM2M elements
is crucial for promoting interoperability, longevity, and avoiding
vendor lock-in in the IoT domain. This study aims to characterize
industrial leadership and involvement in the LwM2M ecosystem by
analyzing contributions to git repositories, bug-tracking systems,
and pull requests, with a focus on identifying the affiliation of individuals involved in LwM2M projects. This analysis has revealed the
extent of industrial involvement in the development and adoption
of the LwM2M standard.
This study has shown significant business interest amongst many
companies that contribute to Open Source Software projects implementing a standard in the IoT domain, and previous research
has identified that development and use of IoT sensors may provide new business opportunities. Further, previous research has
identified that patents impinging on standards may prevent implementation and use of ICT standards by software projects (see, for
example [10, 11, 13]).
Even though we do not address legal issues in this paper, it is
clear that there are several “legal challenges" concerning standards
in the IoT domain, including patents [21]. This remains an issue
that future research should address, and that is of particular interest
in the area of IoT.
All in all, we offer in this paper a first detailed analysis of an IoT
ecosystem in GitHub by mining software repositories. In the near
future we would like to undertake the same task with other IoT
ecosystems (e.g., Zigbee, https://csa-iot.org/) and compare them in
order to gain more insight into how standards and protocols are
developed in OSS repositories.
Reproduction package: Scripts used for retrieval and analysis,
and an anonymized version of the dataset can be obtained at https:
//gsyc.urjc.es/~grex/repro/2023-serp4iot/.
ACKNOWLEDGMENTS
This research has been financially supported by the Swedish Knowledge Foundation (KK-stiftelsen) and participating partner organizations in the SUDO project. The authors are grateful for the
stimulating collaboration and support from colleagues and partner
organizations.
