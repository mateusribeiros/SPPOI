Title: Designing a Data-Driven Survey System: Leveraging Participants’
Online Data to Personalize Surveys

ABSTRACT
User surveys are essential to user-centered research in many
felds, including human-computer interaction (HCI). Survey
personalization—specifcally, adapting questionnaires to the respondents’ profles and experiences—can improve reliability and quality
of responses. However, popular survey platforms lack usable mechanisms for seamlessly importing participants’ data from other systems. This paper explores the design of a data-driven survey system
to fll this gap. First, we conducted formative research, including
a literature review and a survey of researchers (� = 52), to understand researchers’ practices, experiences, needs, and interests in a
data-driven survey system. Then, we designed and implemented a
minimum viable product called Data-Driven Surveys (DDS), which
enables including respondents’ data from online service accounts
(Fitbit, Instagram, and GitHub) in survey questions, answers, and
fow/logic on existing survey platforms (Qualtrics and SurveyMonkey). Our system is open source and can be extended to work with
more online service accounts and survey platforms. It can enhance
the survey research experience for both researchers and respondents.
A demonstration video is available here:
https://doi.org/10.17605/osf.io/vedbj
CCS CONCEPTS
• Human-centered computing → Empirical studies in HCI; Interactive systems and tools; Systems and tools for interaction
design.
KEYWORDS
artefact, surveys, online accounts, user interfaces
1 INTRODUCTION
User surveys are a fundamental tool in empirical research studies.
They support user-centered research in many felds related to information technologies [85]. In human-computer interaction (HCI),
surveys support understanding how and why users perceive and
interact with (online) technologies.
Collecting rich and reliable survey data is essential to provide
meaningful insights. Survey research methodology has evolved
dramatically over the years. Online technologies superseded traditional methods of administering surveys (e.g., paper- and phonebased data collection) [23]. Online platforms such as Qualtrics,
SurveyMonkey, LimeSurvey, and Google Forms enable researchers
to design complex questionnaires, deploy them to respondents, and
collect and analyze responses. One beneft of these platforms is
easier personalization; specifcally, by adapting questionnaires to
respondents’ profles and experiences. For instance, addressing respondents by name or customizing the survey layout [22, 23, 39, 60]
tend to increase response rates. Personalization has mixed efects
on data quality [39, 49]. However, several studies suggest that personalization can improve research quality, build trust, and infuence
the way respondents report sensitive information [36].
Survey personalization can be made more powerful by using
richer information about participants’ lives, extending beyond simple customization to personalized questions and response options
for each respondent. Online platforms, social media, Internet of
Things (IoT) devices, and wearable technologies collect data that
refects users’ behavior. This data presents an opportunity for datadriven survey personalization. By accessing (with the respondent’s
permission) select items from the respondent’s digital history, researchers can dynamically modify the survey, including screening,
survey fow, display logic, skip logic, templated questions and answers, and even asking respondents questions about specifc bits
of their digital lives. This approach could increase respondents’
interest in participating, increase their engagement with the survey,
mitigate response biases [21] (e.g., social desirability biases [4]),
and ultimately improve data quality.
Data-driven personalization can enable transitioning from abstract to concrete inquiries. For example, general questions such as
“What is your main driver when you have very active weeks?” can be
replaced with specifc questions like, “On the week of [April 12th],
you engaged in [four] diferent activities and spent a total of [two]
hours exercising. What was your main motivator during this exceptionally active period?” By adding granularity to survey questions,
data-driven personalization can improve data quality.
Data-driven personalization also has benefts for recall accuracy.
For example, surveys using methodologies inspired by the critical incident technique (CIT) [15, 31] rely on participants recalling
past experiences accurately (e.g., [17, 76]). However, memory is
imperfect, and cognitive biases can afect recall accuracy [56]. Datadriven surveys can mitigate this challenge by using participants’
digital history to present them with a concrete descriptions of past
events (e.g., showing respondents their Facebook/Instagram posts
and the most aggressive comment each post received) thus improving their recall accuracy. For example, Huguenin et al. [41] used
an ah-hoc system based on LimeSurvey to show respondents their
recent Foursquare check-ins and then asked questions about them.
Further, the benefts of data-driven personalization can be applied to research across many felds. For instance, social scientists
could incorporate users’ Facebook/Instagram posts in their surveys
to gain insights about their social media behavior; sports scientists could use Fitbit activities to ask athletes about their exercise
habits, and HCI researchers could use GitHub in their surveys when
studying software development practices.1
Despite the benefts of data-driven survey personalization,2 it
comes with certain downsides. One downside is that it may bias
samples to participants who are willing to share their data. This
may make it harder to recruit large samples. Another downside
is that implementing it with existing survey tools can be difcult.
Existing tools lack usable mechanisms for seamlessly importing
participants’ data from other systems in order to enable data-driven
personalization. Instead, when researchers used respondents’ data
to personalize survey questions (e.g., [27, 41, 82]) they had to resort
to complex and resource-intensive methods such as customizing
existing survey platforms and accessing respondent data manually
(e.g., through data subject access requests made by respondents)3
or through ad-hoc API calls. Creating data-driven surveys remains
cumbersome, which prevents unleashing the full potential of datadriven surveys in research.
In this paper, we explore the design of a data-driven survey system, starting with its desirability and usefulness for researchers
1
Note that data obtained from social media platforms represents a curated projection
of one’s life. Similarly, data from platforms such as Fitbit and GitHub represents
a projection, as someone may engage in an activity without using an associated
online service (e.g., exercising without wearing their Fitbit tracker). It is important to
acknowledge that data collected from online servicessuch as Fitbit may not be perfectly
accurate [28], but should be sufciently accurate to provide useful insights [35]. 2
Data-driven questions cannot and should not replace traditional, more general questions. Rather, they can enrich the research process with detailed contextual insights. 3
See, for instance, https://help.instagram.com/181231772500920, last accessed Feb.
2024.
(i.e., our potential users). Our paper consists of three parts: (i) a
systematic survey of papers that include user surveys (� = 74)
(see, Section 3.1), (ii) a survey of researchers who do user surveys
(� = 52) (see, Section 3.2), and (iii) the design of our minimum
viable product (MVP) platform: Data-Driven Surveys or DDS (see,
Section 4). These three pillars allow usto: frst, establish the need for
DDS; second, identify key features and requirements for DDS; and
fnally, present the resultant design. The literature review informed
us about several design implications. For example, we identifed a
potential for automating participant screening by using data from
their online accounts instead of solely relying on self-reported data.
The researcher survey underscored our belief that protecting respondents’ privacy should be a priority. Considering these fndings,
we designed and implemented DDS: an open-source MVP version
of our system. DDS enables the inclusion of respondents’ data from
online service platforms, such as Fitbit, Instagram, and GitHub,
in the questions and answers of survey questionnaires and in the
survey fow and logic. We provide a 6-minute demonstration video
of DDS on OSF.4 With DDS, researchers can enhance a Qualtrics
or SurveyMonkey survey, for instance, by automatically screening
respondents whose Instagram account was created less than a year
ago, by asking certain questions only to respondents who record
yoga activities on Fitbit, by including the respondents’ total step
counts in a question text, by asking respondents questions about a
specifc GitHub repository (e.g., a repository with at least 20 open
issues), and by showing them the map and date of their running
activity for better recollection. The statistics collected from the
respondents’ Fitbit data can also simply be used to characterize
the sample of respondents (slightly active, very active, etc.) and
to identify correlations (e.g., with factor analysis) between their
physical activity and their survey responses. DDS takes multiple
steps to protect respondents’ privacy, such as using OAuth to access
respondents’ accounts, by fetching only data that is needed for a
given survey and only storing it on the survey platform, by informing respondents about the data that is collected and the way it is
used, etc. For a more detailed overview of the privacy protection
mechanisms, see Section 4.
DDS currently works with Qualtrics and SurveyMonkey, and
can import data from Fitbit, Instagram, and GitHub. It is extensible
to other survey platforms and online services (e.g., Spotify), thus
ensuring data collection efcacy across various contexts.
Our research contributions are two-fold:
● First, we present empirical insights gathered from extensive
formative research, thus ofering a comprehensive understanding of the challenges and opportunities associated with
data-driven survey personalization. These insights inform
DDS’ design and functionality, ensuring that it aligns with
researchers’ diverse practices and needs across domains.
● Second, we describe the design and implementation of our
minimum viable product platform, DDS, and we showcase
its capabilities through practical use cases.
This work introduces an innovative solution that has the potential to enhance survey research, particularly in the context of
HCI. By simplifying the development of data-driven surveys, we
provide both technical and non-technical researchers with a powerful tool—free and open-source—to enhance their survey designs.
This innovation ofers researchers new opportunities for in-depth
exploration and provides respondents with more engaging and
personalized interactions.
2 RELATED WORK
In this section, we primarily review the existing literature and tools
related to online toolkits and surveys. We also highlight the challenges that some researchers encounter when creating personalized
surveys.
2.1 Existing Survey Tools
Several researchers have studied the user interface of online surveys. Genter et al. [34] compared drag-and-drop and numeric-entry
options for survey ranking questions by using Qualtrics and analyzed responses regarding distribution patterns, response times,
and challenges associated with each design. Ebert et al. [26] developed QButterfy to overcome integration challenges between
survey tools and stimuli. QButterfy is an HCI toolkit that enables
non-technical researchers to conduct online user interaction studies by using the Qualtrics and LimeSurvey platforms. QButterfy
enables displaying stimulus web pages and recording clickstreams.
Several studies focused on improving researcher interaction with
survey tools. Molnar [59] presented SMARTRIQS5
, which enables
real-time interaction within Qualtrics surveys, such as grouping
respondents, assigning them conditions, and enabling them to chat
with other respondents in the same group. Ajilore et al. [2] studied
if using the local language, Pidgin English, and animated GIFs could
increase online survey interactivity and engagement. They found
that using GIFs and Pidgin English were perceived as highly interactive, and had specifc benefts such as fun and persuasiveness.
Finally, Rodrigues et al. [69] focused on analyzing survey data. They
developed Lyzeli,6 which enables analyzing and correlating survey
responses to address the error-proneness of survey-data analysis.
Lyzeli provides features such as automatic question type identifcation, sentiment analysis, data fltering, word cloud visualization,
and graphing.
2.2 The Use of Chatbots in Survey Research
In a diferent approach,several papers[68, 83, 86, 88] explored using
chatbots as an alternative to web-based surveys. Wen and Colley
[83] introduced a real-time moderator chat that prompts respondents to address unanswered questions or to provide clarifcations.
Xiao et al. [86] compared the results of an AI chatbot-driven survey
with a traditional online survey in a feld study with 600 participants. They found that the chatbot-driven approach elicited more
relevant,specifc, and clear responses compared to the Qualtricssurvey. Participants engaged more with the chatbot, tended to provide
more detailed and disclosing responses, and were willing to participate in future surveys. Conversely, Zarouali et al. [88] compared
web-based and chatbot surveys for data collection. They found that
respondents of web surveys often have more favorable response
5
See https://smartriqs.com/, last accessed Feb. 2024. 6
See https://arieslab.github.io/lyzeli/#/, last accessed Feb. 2024.
characteristics and data quality, as compared to chatbot surveys. Finally, Rhim et al. [68] explored humanization techniques in survey
chatbots. They compared a humanized chatbot with features such
as self-introduction and adaptive responses to a baseline chatbot.
They found the humanized survey chatbot had increased positive
perceptions, increased interaction time, and improved data quality.
2.3 Existing Instrumental Toolkits
Online behavioral research in cognitive psychology is growing,
with a particular focus on reaction-time experiments that often
demand advanced skills. Several studies proposed solutions for improving transparency, replicability, usability, and accessibility in
experimental social sciences. Several studies [2, 5, 7, 61] focused
on the accuracy of measuring reaction time in web experiments.
Nikulchev et al. [61] presented a solution that minimizes the bias
introduced by diferent devices and improves the precision of reaction time measurement. Balietti [7] developed nodeGame,7 a
framework for conducting real-time synchronous experiments online or in a lab environment by using web browsers on a wide
range of devices. Anwyl-Irvine et al. [5] also introduced the Gorilla
Experiment Builder,8 which manages time-sensitive experiments
across diferent participant groups,settings, and devices. Henninger
et al. [40] introduced lab.js,9 an experiment builder for web-based
data collection in both online and lab-based research. The platform
provides a visual interface that does not require coding. Chen et al.
[16] developed oTree10 for implementing interactive laboratory,
online, and feld experiments. Gureckis et al. [37] developed psiTurk11 to reduce technical barriers for conducting controlled online
behavioral experiments on Amazon’s Mechanical Turk.
Finally, Ferreira et al. [29] developed a mobile instrumentation
toolkit called AWARE. It utilizes smartphones’ built-in sensors to
facilitate the acquisition, inference, and generation of context for
data analysis. Such applications are usually limited to a specifc
device or hardware type and can drain device batteries.
2.4 Researchers’ Challenges in Data-Driven
Survey Creation
Several studies used data-driven surveys to varying extents.
Huguenin et al. [41] studied how the precision of a location checkin impacts its utility as perceived by the user who made it. The
researchers modifed the LimeSurvey platform to create personalized questions. First, respondents granted the survey system access
to their Foursquare accounts. Then, they were screened based on
their Foursquare data, and a number of check-ins were extracted.
Finally, for each extracted check-in, a summary of the check-in
was shown in question text along with four alternate versions that
had diferent levels of information. The respondent then rated the
utility of the four versions.
Epstein et al. [27] studied how to support ftness tracker users
when they stop using their wearables. Using the Fitbit API and an adhoc solution, they asked respondents to grant access to their Fitbit
accounts. In the survey, respondents were shown and asked questions about seven visual representations of their ftness-tracking
data.
Bauer et al. [9] used a Facebook app to study changesin Facebook
users’ privacy preferences over time. For each respondent, they randomly selected posts, collected their metadata, and included them in
the survey. Ayalon and Toch [6] asked participants to comment on
their privacy preferences for old Facebook posts. However, respondents were asked to select and report individual posts themselves.
Anaraky et al. [3] developed a Facebook app to study how framing
and default techniques infuence users’ privacy decisions for automatic public tagging in their friends’ pictures. For each respondent
they retrieved photos and tagging information, and used both in
their survey questions. Johnson et al. [43] developed a Facebook
app to study respondents’ relationships with their Facebook friends.
Two other studies analyzed privacy and data-retention needs by
using custom software to show respondents fles and images from
their e-mail and cloud-storage accounts [18, 45].
Wei et al. [82] used advertisement information from participants’
Twitter data in a survey about advertisement targeting mechanisms
preferences. Respondents had to request all their Twitter data and
send it to the researchers. This study demonstrates the value of
including real, personal data when asking participants about their
experiences and preferences.
These examples show that personalized surveys enable advanced
research, but creating them is complex and resource-intensive. Researchers had to customize existing survey platforms, develop custom applications, and access respondents’ data through APIs with
ad-hoc software tools. Although fruitful, these approaches can be
technically challenging and costly. Some researchers relied on selfreports, which can also be time-consuming for participants to look
up, be unreliable, and be error-prone. A data-driven survey tool
could signifcantly mitigate these challenges.
3 FORMATIVE RESEARCH
To understand researchers’ practices when conducting survey research, we conducted two formative research [32] studies: (i) a
literature review of papers with survey methodology and (ii) an
online survey of researchers who conduct survey research.
3.1 Literature Review
One approach to understand researchers’ practices when they use a
particular research methodology is to review their published papers.
Therefore, we conducted a systematic literature review [47] of
papers that used survey methodologies. Many HCI studies employ
surveys. To narrow the scope and make this review more tractable,
we focused specifcally on ftness-tracking studies. We chose ftness
tracking because it is an active research area with many studies, a
large proportion of which employ surveys. Also, ftness tracking
research presents a promising initial use case for our work due
to the data they collect being inherently relevant to data-driven
surveys.
3.1.1 Method. For data collection, we frst defned keywords12
and searched them in ACM DL, IEEE Xplore, AIS library, USENIX,
Science Direct, and Springer Link. We also used Google Scholar to
include papers from other databases and publishers (e.g., Taylor
& Francis). After removing duplicates, we identifed 689 papers.
We excluded the papers that (i) were not written in English, (ii)
were published in 2012 or earlier, and (iii) were not peer-reviewed.
We included only those papers that were: (i) about ftness trackers
and/or how ftness trackers are used, and (ii) conducted a survey
with participants. The second author applied the inclusion and
exclusion criteria and later confrmed them with the frst author.
Using the exclusion criteria and the frst inclusion criterion, we
selected 234 out of 689 papers.13 After applying the second inclusion criterion, we identifed � = 74 papers that conducted user
surveys. For data analysis, we employed refexive thematic analysis
(TA) [10, 11]—a method that encourages researchers to consider
their own perspectives during data interpretation. Refexive TA has
recently been used in HCI, along with systematic reviews for data
analysis [19]. This approach enabled us to code the papers from
the perspective of data-driven surveys: identifying key themes in
the textual data and examining the way these themes related to
or refected the use of or need for data-driven surveys. The frst
and second author collaboratively conducted the analysis. Initially,
the frst author reviewed the abstract and methods sections of the
papers (and other sections if necessary) and coded the parts related
to survey methodology and data collection. Subsequently, the frst
and second authors discussed the fndings to identify codes, themes,
and to refne the coding structure. To quantify these fndings, we
counted the number of papers that included relevant items.
3.1.2 Results. Qualtrics was the most commonly used platform, reported in � = 13 papers. Unfortunately, � = 54 papers did not
report which platform they used. Other reported platforms included Google Forms, Unipark, QuestionPro, REDCap, SoJump,
and LimeSurvey, all mentioned rarely. In contrast, � = 32 papers
reported the type of ftness tracker(s) studied in their research, with
Fitbit being the most commonly reported (� = 32), followed by
Garmin (� = 8) and Apple (� = 7). Other brands were reported
fewer than 7 times.
Table 1 summarizes the papers where the researchers requested
participants’ data for further analysis. Out of � = 8 identifed papers,
three papers used the Fitbit API for data collection [27, 62, 90]. One
of them used the data to implement an ad-hoc data-driven survey
system [27] (as discussed in Section 2.4).
We identifed � = 24 papers with survey questions that could
have benefted from using data-driven surveys. Table 2 (top) summarizes the goals of the surveys in these papers and how datadriven surveys could have helped. We also identifed � = 48 papers
that used surveys as a screener tool for recruiting respondents. As
highlighted in Table 2 (bottom), most of these screener questions
Table 1: The relevance of the papers to data-driven surveys: eight papers used ftness data. Only Three used the Fitbit API for
data collection and only one of them implemented an ad-hoc data-driven survey system.
Paper Data Collection Method Purpose of Data Collection
Epstein et al. [27] Fitbit API to implement an ad-hoc data-driven survey
Zuferey et al. [90] Fitbit API to infer participants’ personality traits
Orlosky et al. [62] Fitbit API did not specify
Dreher et al. [24] used a proprietary service (Fitabase∗) to validate Fitbit usage
Stück et al. [75] asked members of a health campaign (AchieveMint) to analyze physical activity behavior
Shin [74] used a mobile app called “HealthExported for Fitbit to CSV” to analyze physical activity behavior
Dai et al. [20] did not specify to validate Fitbit usage
Preusse et al. [66] downloaded manually did not specify
could be measured using a ftness-tracking platform and thus could
beneft from a data-driven survey platform.
Our literature survey unveiled the following insights into the
potential and signifcance of data-driven surveys in the feld of
ftness tracker research and beyond:
● Promising Potential for Fitness-Tracker Research.
Whereas most existing studies have not directly incorporated data-driven surveys, there is a clear opportunity for
data-driven approaches to improve the reliability and depth
of insights derived from ftness-tracking studies. Note that
our review of related works (see Section 2) also identifed this potential in other research areas (e.g., privacy research [6, 9, 41]).
● Advances in Survey Quality. Data-driven surveys could
improve survey quality. They can transform abstract questionsinto concrete inquiries, directly collect data to save time
and avoid errors(intentional or not) in respondent recall, and
facilitate faster and more precise participant screening. Thus,
data-driven surveys could (partially) bridge the gap between
measurement studies and traditional survey methods.
● Platform and Data Trends. Qualtrics was the most prevalent survey platform. Similarly, Fitbit stood out as the dominant source of ftness tracker data in this research domain.
Therefore, it could be worthwhile to include these two platforms in a data-driven survey tool.
3.2 Online Survey
We conducted a survey, targeted at researchers who conduct surveys in their research, to explore whether a data-driven survey tool
would be valuable for researchers in HCI and related disciplines.
Throughout thissection, we use the term “researcher” instead of “respondent” to avoid confusion between our respondents and generic
survey respondents.
3.2.1 Method. The full text of the survey is available in Appendix A. The survey began with a consent form, followed by some
background and screening questions about the researcher’s experience with online survey tools. Next, there were three sections
describing possible features of a data-driven survey tool:
(1) Conditioning survey fow or skip logic on extracted personal
data, e.g., skip to Question 5 if the participant has made
fewer than 200 posts on Facebook (a.k.a. “Survey Flow and
Display/Skip Logic”);
(2) Using extracted personal data to fll in variablesfor templated
questions, e.g., “Your most active month (in terms of step
count) this year was [month]. Please explain why.” (a.k.a.
“Templated Questions and Answers”); and
(3) Using extracted personal data to select example activities to
ask questions about, e.g., select the most recent Facebook
post with more than 200 likes, display it, and ask questions
about it (a.k.a. “Custom Variables”).
For each of these three features, we asked researchers whether
they had previously implemented similar functionality, whether
they would fnd it useful, and how likely they would be to use it,
followed by an open-ended question about scenarios where this
feature might be useful. We then asked researchers to describe (in
an open-ended way) any pain points that would be addressed or
benefts they would derive from using the three features. Finally, in
order to characterize our sample, we asked about age, gender, and
specifc research felds.14 We implemented the survey in Qualtrics.
Before deployment, we did cognitive pretests with two colleagues.
We used their feedback to adjust the phrasing of questions to improve clarity. The survey was designed to take less than 10 minutes,
and, in practice, took 7 minutes and 25 seconds (median).
We recruited researchers by advertising within researcher networks, including slack channels (e.g., the SOUPS Slack channel),
mailing lists (e.g., the UMD HCIL list and the SOUPS announcement list), and social media groups associated with conferences
and communities (e.g., the CHI Meta group on Facebook). We also
directly e-mailed the authors of the research papers included in
our literature review (see Section 3.1) to invite them to participate.
Researchers were not compensated. The survey was approved by
our university’s institutional review board (IRB).
For this formative research, we report on multiple-choice questions with descriptive statistics. We analyzed open-ended responses
using an open-coding approach [71], where the second author performed the initial coding and then refned it in consultation with
the entire team.
3.2.2 Results. A total of 76 researchers started the survey, of which
55 completed it. Among them, � = 52 researchers had prior experience with survey tools; we report their answers here. A summary
of their demographics, research areas, and experience with surveys
is given in Table 3. Quantitative results regarding the perceived usefulness of the three considered features of data-driven surveys, and
self-reported likelihood to use them, are summarized in Figure 1.
Regarding the proposed Survey Flow and Display/Skip Logic
feature, 57.7% of the researchers (� = 30) reported having experience with a similar mechanism. These were evenly divided between
those who considered it easy to implement (� = 13, 43.3%), and those
who reported it as difcult (� = 13, 43.3%).15 Among those who
had not used this feature before, 11.5% (� = 6) reported they had
not thought about such functionality, and 5.8% (� = 3) mentioned
it was technically difcult to implement. A researcher mentioned:
“I did use survey fows/skip logic and display logic, just not based
on participant data from social networks, but rather data from inside the survey. That was complicated enough ;)” [4 or more, a lot,
S&P].16 Most researchers found this feature useful and said they
were likely to use it, if it was easy to implement (for details, see
Figure 1). Researchers reported several potentially useful scenarios,
e.g., confguring a survey based on the frequency of interaction
with a particular technology. They mentioned this could greatly
reduce the exhaustive list of questions they must ask beforehand:
“In my recent research, I could confgure survey logic based on people’s frequency of interaction with VR devices based on their daily
use activity of VR devices.” [4 or more, about half, HCI]. Several
researchers mentioned scenarios related to user behavior and preferences research, such as analyzing developers’ practices, users’
unconscious habits, and the correlation between social media behavior and privacy preferences. “I would fnd this very useful when
surveying software developers about secure development practices.
I could imagine skipping a question or changing the fow based on
their commit history on GitHub.” [4 or more, a great deal, S&P]. A
few researchers mentioned use cases in health research and for
conducting experience-sampling and diary methods.
Regarding the proposed Templated Questions and Answers
feature, 26.9% of the researchers (� = 14) had experience using a
similar approach. Half of those who had used this feature before
found the implementation difcult (� = 7, 50.0%). Among those
who had not used it, 21.2% (� = 11) had not thought of it, and 11.5%
(� = 6) mentioned technical difculties. A researcher mentioned
a challenge related to data accessibility and scalability: “I was interested in doing this with Spotify listening data; however, the API
provides limited access. We instead had to rely on user-requested data
dumps, which takes about a week per user and doesn’t scale well.” [4
or more, about half, HCI]. A strong majority found the proposed
feature useful and many reported they would be likely to use it.
Scenarios suggested for using this feature included customizing
questions and answers based on technologies that users interacted
with, such as using logged hours on Steam for gaming research or
showing vignettes based on the social media platform users were
using. One researcher mentioned the usefulness of customization
in long-term studies: “On longitudinal surveys reminding a person
how many times they had used an app or feature in the prior month
when asking them how useful they feel the app/features is.” [3, a little,
HCI]. Another researcher mentioned combining social media data
with users’ prosocial behavior (e.g., about vaccination).
Regarding the proposed Custom Variables feature, only 9.6% of
the researchers (� = 5) reported using a similar approach. Among
those, two researchers found it difcult to implement. Of the remaining researchers who had never used it, many said they had
never thought about it (� = 19, 36.5%), and some pointed to technical barriers (� = 7, 13.5%). More than half of researchers expected
the feature to be useful, and around half considered it likely they
would use it. Multiple usage scenarios were suggested, including
evaluating the experiences and behaviors of software developers,
studying user behavior in social media, and applying stratifed sampling methods. “I could imagine using this to discuss specifc pushes
to GitHub or posts to StackOverfow to ask them about why they did
that with this post or push, how they came up with that post or push,
etc.” [4 or more, a great deal, S&P]. “Showing respondents a random
selection of posts and asking them to answer a series of questions as it
relates to that post.” [4 or more, about half, S&P].
Researchers identifed three major advantages the proposed
data-driven features could bring to their research. First was the
potential to improve data quality. Researchers pointed out that
data-driven surveys will bring precise data into the survey, avoid
reliance on only self-reported data, and gain more in-depth insights. “From a research perspective, this would be a treasure trove
of information!” [4 or more, a lot, S&P]. Two mentioned that this
could signifcantly improve participants’ recall. “It would be nice
to be able to ask about specifc experiences the participant has had,
without risking them misremembering the event.” [2, about half,
S&P]. Second, they identifed numerous research opportunities
that could be realized with data-driven surveys, including asking
novel research questions, conducting more complex studies with
context-based questions in diverse formats, and collecting more
specifc and objective answers rather than generic and subjective
ones. For example, data-driven surveys “would make complex ’if’-
Statements a lot shorter and easier.” [4 or more, a great deal, S&P].
Third, researchers highlighted the potential benefts for respondents’ engagement and experience. They mentioned reducing
respondents’ fatigue, keeping respondents engaged, and allowing
them to think about specifc events when answering questions. “[...]
minimize the number of questions that participants need to complete,
present questions only to suitable participants, ease participants burden of going through a lengthy questionnaire.” [4 or more, about half,
HCI].
Researchers also identifed some key drawbacks.
17 Several expressed concerns about privacy and anonymity in using respondents’ data. Some were concerned such a system would lead to
identifcation of the participants. “This data typically allows for
unique identifcation of the individual, which is what we would like
to avoid in surveys.” [4 or more, a lot, S&P]. This valid feedback is
not surprising, given that a large proportion of our sample works
in (usable) security and privacy. Concern for participant privacy
informed our design (see Section 4.2). In particular, we considered
transparency paramount and decided that our solution should be
open-source and should communicate to respondents what data is
collected about them. Many researchers (appropriately) take great
care when asking participants for detailed or sensitive information. Previously, researchers have asked respondents to download
a complete copy of their data (sometimes through a third-party
application) and then to send it to them. These researchers had to
develop extensive infrastructure to limit and/or clean the data they
collected. With an automated approach, access to respondents’ data
would be more fne-grained and controlled through using APIs’
permissions infrastructure, making it easier to take appropriate
care. Nonetheless, with or without automated tools, it is incumbent upon researchers to think carefully about data collection and
how to protect their participants; our design is intended to support
researchers in doing so.
Relatedly, another researcher mentioned that proper consent
collection is necessary before deploying such systems. Thus, a datadriven survey should include meaningful informed consent, where
respondents can read and agree before granting access to their data.
Some researchers felt such privacy issues could create a deployment
challenge, as the study might be blocked by IRBs and ethics
committees. “[...] it might pose a problem for IRB management if PII
like social media accounts are linked on the same platform that holds
the study data [...]” [3, about half, HCI]. We will further discuss
privacy-enhancing strategies to ensure ethical data collection.
Finally, several researchers noted challenges with usability and
learning curve. Some thought integrating data into existing survey platforms would be too complicated. “I need to fgure out how
to integrate diferent data sources by myself.” [4 or more, a great
deal, HCI]. Our envisioned design would facilitate integrating data,
simplifying the process, and ensuring that using external data from
online services for personalization would be exactly the same as
using internal data (i.e., responses to previous questions in the survey). The use of internal data is a very common practice among
researchers, suggesting there would be limited learning required.
To conclude, our online user survey highlights the need for and
interest in a data-driven survey tool and shedslight on the following
points:
● Feature Preference. While all three of the proposed features received positive feedback, the Survey Flow and Display/Skip Logic feature was favored as most useful and likely
to be used.
● Potential Use Cases and Benefts. Researchers envisioned
various potential usage scenarios for data-driven survey
tools, from customized data-driven questions in gaming research to studying developers’ commit behavior. Researchers
considered data-driven survey tools benefcial for improving
data quality, expanding research opportunities, and enhancing participant engagement.
● Concerns. Privacy and anonymity emerged as a critical concern, highlighting the need for including privacy-enhancing
mechanisms when designing data-driven survey tools (i.e.,
privacy-by-design).
4 DESIGN AND IMPLEMENTATION OF DDS
In this section, we describe the design and implementation of our
data-driven survey platform (named DDS) and our methodology to
do so. An overview of DDS is given in Figure 2, and a demo video is
18 available on OSF. The source code for DDS is hosted on GitHub.
4.1 Design Introduction
4.1.1 Design Goals. Our goal is to design and implement an extensible and easy-to-use system that enables integrating survey
participants’ data from online services into surveys. We do not
aim to build a survey platform (SP). This system should enable
researchers to integrate the three main techniques of Survey Flow
18https://github.com/DataDrivenSurveys/DataDrivenSurveys
and Display/Skip Logic, Templated Questions and Answers, and
Custom Variables into their surveys. Given the positive feedback
we collected during our formative research (see Section 3.2.2), we
decided to consider these techniques the core functionalities of
DDS.
4.1.2 Design Methodology. We followed an iterative design process [65]. One author proposed an initial system design, which
was then iterated on together by four authors. Two authors (henceforth, designers) started the UI design process by brainstorming
functional requirements and interface sequences (i.e., user fows).
They started by sketching the interface with pen and paper and
gathered feedback from colleagues in our institution with extensive
UX/UI design experience. After converging on an initial design,
the designers switched to using Figma [30], which makes it easy
to iterate on and build UX/UI designs. After converging on these
initial UI and system designs, we began implementation.
To develop DDS we used an adapted Scrum approach, which is an
agile project management system [48]. Two authors, henceforth the
Development Team (DT), implemented DDS. Another author took
on both roles of Product Owner (PO) (to ensure the prioritization
of features) and Scrum Master (to ensure that the Scrum process is
being followed). The DT would plan ‘sprints’ to implement several
features based on the PO’s requests. Then, they implemented the
features, while having daily meetings to discuss the progress and
address any issues. New feature requests from the DT and PO were
recorded through GitHub issues and project management. At the
end of each week, the DT selected the next set of features based
on priority. The DT would also actively add suggestions for new
features.
During the design and implementation processes, all authors
periodically brainstormed potential shortcomings or limitations
of the existing design, allowing us to identify and address issues
quickly and preemptively. For example, we anticipated that respondents would be hesitant to share their data. Hence we decided
to take a privacy-by-design approach and recruited security and
privacy researchers for our researcher survey. This resulted in us
implementing the transparency table described in Section 4.2.
Figure 2: Overview of the architecture and functioning of DDS. Researchers create a project on DDS and provide it with
credentials (e.g., API key, OAuth token, Client ID, Client Secret) for managing surveys on the survey platform (SP) and apps
on the selected data providers (DPs) (a.k.a. online services). DDS declares the data that can potentially be extracted from the
DPs on the SP, where the researchers can use them while designing their survey. These actions are denoted as Steps 0 and are
interleaved in time. To begin a data-driven survey, respondents follow a link to DDS (Step 1), where they are redirected to the
required DPs (Step 2) in order to grant DDS access to their data. DDS downloads and processes their data from the DPs (Step 3),
uploads the processed data to the SP (Step 4), then deletes the data from its memory. Finally, the respondents are redirected to
the SP to take the data-driven survey (Step 5). Researchers and respondents use web browsers to interact with the diferent
systems (i.e., SP, DDS, and DPs). The six screenshots at the bottom of the fgure illustrate the diferent websites and web pages
used by these users. These screenshots are provided as visual clues; readable versions of these web pages are available in other
fgures and in the demo videos. DDS currently supports Qualtrics and SurveyMonkey as SPs, as well as Fitbit, Instagram, and
GitHub as DPs. Grayed-out icons represent other popular platforms and services that could be integrated in the future (Google
Forms; Spotify).
4.1.3 Choice of Integrated Platforms and Services. We integrated
our minimum viable product implementation with Qualtrics and
SurveyMonkey, as we found them to be the most commonly used
SPs (see Section 3). We chose Fitbit, Instagram, and GitHub as initial
data providers (DPs). Our formative research (Section 3) indicated a
good potential for data-driven surveys in ftness tracking research.
We chose to integrate with Fitbit, as it was the most reported ftness
tracker brand in the studies we reviewed. Instagram was chosen as
an example to demonstrate that DDS can integrate with social media
services, as researchers studying social media often use surveys to
study user experiences, and social-media scenarios were commonly
proposed in our formative survey. GitHub was chosen as many
researchers in our researcher survey reported doing surveys with
software developers.
4.1.4 Overview and Core Features of DDS. DDS integrates with
existing SPs and enables using all the features ofered by the SP.
DDS obtains participants’ data (with permission) from DPs and
transfers it to the SP. The core features of DDS are: (i) checking
whether a survey participant has an account on a given DP platform, (ii) providing built-in (i.e., predefned) variables for each DP
and making them available on the SP, (iii) creating custom variables
to select specifc data using rules that researchers defne. Variables
provided by DDS enable conveniently collecting additional data
and statistics about respondents, creating templated questions and
answers (where placeholders are replaced with each respondent’s
data), and confguring display and survey fow logic. For templated
questions and answers, the variables can be inserted as piped text:
“On average, you walk [steps.average] steps per day. Which of the
following do you think contributes the most to you staying motivated
for this?” For display and survey-fow logic, the variables can be
compared with reference values: “Show this question/answer/branch
only if account.creation_date <= 2020-01-01.” Custom variables enable
deeper personalization by providing real and personal examples,
instead of hypotheticals, to ask about categories of events or items.
For instance, when asking about privacy concerns related to sharing location data, researchers could use DDS to show a map of the
participant’s most recent run. This would help participants think
concretely about their actual data, instead of an imagined abstraction. Additional examples are provided in the survey transcript
in Appendix A.
4.1.5 Distributing DDS Surveys. Data-driven surveys powered by
DDS do not need personalized invitation links. After a participant
gives access to the required data-provider platforms, a unique identifer is formed based on their account IDs and then linked to a
unique distribution link on the SP. Researchers can set a policy on
whether the same combination of data-provider accounts must be
used to resume the survey and/or whether previously used accounts
can be used to take the survey again (e.g., whether a respondent
can take the survey once with Fitbit account � 1 and Instagram account �1, and then again later with Fitbit account � 1 and Instagram
account �2).
4.2 Privacy Considerations
We designed DDS with a careful focus on participants’ privacy,
captured in the data-privacy policy. We aimed to address the points
brought up in Section 3.2.2. Here, we present the key points.
Respondent Informed Consent. The landing page that a respondent sees provides several features that support giving informed
consent for sharing their data. First, it informs participants that
they will need to grant access to their data. Second, it provides
a link to the privacy policy explaining data collection. Third, the
survey distribution page displays a table that summarizes the exact
data that will be extracted for each variable (see Figure 9a). For each
variable, the table shows the DP, variable type, a textual variable
description, and a link to the ofcial API documentation.
Data Minimization. Requests are made via OAuth,19 which allows
DDS to access the respondent’s data without needing their username and password, only their authorization. Figure 9b shows an
example of this interface for Fitbit. If the DP ofers diferent classes
of data access, DDS will only request access to classes that are used
in the researcher’s data-driven survey. DDS only downloads data
needed to compute the variables that a survey requires.
No Data Retention. The downloaded data is not saved to disk;
instead, it is stored temporarily in the system memory during variable computation. Once the calculated variables are uploaded to
the SP, the raw data and variables are deleted from DDS’s memory, and the access tokens for the DP(s) are revoked. The uploaded
variables are saved on the SP to be used in the survey when the
respondent takes it. They also provide context for researchers (who
would otherwise see only the templated questions and answers),
and enable exporting of the data through DDS. When exporting
survey responses through DDS, responses are downloaded to the
researchers’ computer, then placeholder values are replaced by variable values in the data. DDS does not store any of the fnal survey
responses; only the SP does this.
4.3 Architecture
DDS contains three main components: a back-end API, a front-end
(web) app, and a database. All three components are proxied using
an Nginx web server. The database stores researcher registration
information, project confgurations, and hashed participant-DP
IDs.20 The back-end API provides access to the database, obtains
data from DPs through their APIs, and communicates with the SPs’
APIs in order to upload to SPs the list of available variables (for
use in setting up piped text) and to upload participants’ computed
variable values for taking surveys. We implemented the back-end
API in Flask [64] and Python 3 [70]. For the front end, we created a
React [57] web app that both researchers and respondents can use.
It makes API calls to the back-end API.
The platform is confgured to be conveniently deployed using
Docker containers [42]. It can also be deployed directly through
GitHub. A researcher would need to fork our repository and confgure a few deployment parameters. The repository is documented
and contains step-by-step deployment instructions. For a detailed
architecture diagram, see Figure 11 in Appendix B.
4.4 Researcher Flow
The researcher fow begins with a researcher creating a new project
on DDS (shown in Figure 3). They can either create a new project
from scratch (Figure 3a), which would create a new survey on
their chosen SP, or they can link an existing survey from an SP
(Figure 3b). To create a new project from scratch, they must name
their project (the survey created on the SP will have the same name)
and provide the information required by the chosen SP (e.g., the
platform API key for Qualtrics). Creating from an existing survey
requires providing a new name, the source survey’s ID, and the
information required to interact with the platform. DDS provides
SP-specifc instructions for obtaining the required information.
Once the DDS project is created, the researcher can manage it
by adding DPs, enabling/disabling variables, changing test values,
creating custom variables, syncing the variables, and testing the
survey. We illustrate these steps with a running example using
Fitbit.
To add a DP (Fitbit in this example), the researcher must register
an app on the DP’s website using a short web form. The registered
app will be used to communicate with a respondent’s account and
to extract their data. Figure 5a shows an example of registering a
Fitbit app. When a researcher clicks on ‘+ data provider’ (shown in
Figure 5b), DDS provides most of the required information for the
app registration form. Further, DDS also provides links to tutorials
for registering the app and a link to the app creation page.21 Next,
the researcher must add the DP on DDS (shown in Figure 5b) by
selecting it from a list of available options and confguring parameters such as a client ID and secret. DDS provides instructions for
where to fnd the required parameters.
After adding the DP, a number of built-in variables are made
available in the DDS project (shown in Figure 4). Each variable has
an implicit ‘exists’ version ([variable].exists), which will be True if
a variable was calculated successfully and False otherwise. These
can be used, for example, to avoid showing respondents questions
or applying logic when there is no data. The researcher can select
which variables to enable for the current project; for example, in
Figure 4, the researcher enabled account creation date (from the
“account” category) and activities by frequency (from the “activities”
category). These variables defne (a) which data DDS will request
from the DP, and (b) which variables are available for use on the
SP.
In addition to these built-in variables, the researcher can add
custom variables that enable selecting specifc items from the participant’s account for use in the survey, according to researcherdefned selection rules. Figure 6 shows a researcher creating a
custom variable to select one specifc running activity from the
participant’s Fitbit data. In this example, Fitbit is the selected DP
and activities is the selected data category to draw from. Filtering
rules were added to select only the activities that lasted at least
3600 seconds, occurred on or after January 1, 2022, and have the
activity type ‘Run.’ Finally, the researcher must choose a selection
criterion to select one single item from the list of items that pass
the flter. Options include choosing the item with the maximum or
minimum value of some attribute, or choosing a random qualifying
item. Here, the activity date is used to select the newest qualifying
running activity. After a custom variable is defned, it is available in
the main DDS variables list (Figure 7), where it can be enabled for
use. A custom variable contains sub-variables (e.g., date, duration,
type for a Fitbit activity), that can be enabled individually and used
in a survey (just like built-in variables). To enable a sub-variable,
the custom variable as a whole must be enabled. Each sub-variable
corresponds to an attribute of the selected custom variable item. A
researcher can edit the rules used to create the custom variable or
delete it using the ‘edit’ and ‘delete’ buttons in the ‘actions’ column
of the table. Test values can be assigned to each sub-variable. Only
enabled sub-variables are uploaded to SPs.
After enabling all the desired variables (built-in and/or custom),
the researcher presses the “sync variables” button. This ensures
that the SP knows about all the available variables. If the researcher
wantsto change the enabled variables—to add an additional variable,
or to remove one that is not needed—they can simply sync the
variables again to ensure the SP is up to date.
Synced variables are visible on the SP for use in logic and question design. At this point, the researcher can design the survey as
normal, using any features provided by the SP and incorporating
DDS variables as needed. An example of a question using these
variables is shown in Figure 8.
Once the researcher fnishes designing their survey, they can
preview it using the “preview survey” button in the DDS project
view (Figure 4). This will create a survey (via the SP) in which
each personalized value will be set to the associated “test value,” as
assigned by the researcher during variable selection. In Figure 4,
the test value for an account creation date was set for January 1st,
2020.
Once data collection is complete, the researcher can export the
results via DDS (the “download data” button in Figure 4). The downloaded results will mirror a standard export of data from the SP, but
any placeholders in questions or response options will be flled in
with the actual personalized data per respondent. For a particular
respondent in our running example, the downloaded data will list
Q1 from Figure 8 as e.g., 7028 steps, rather than showing the variable placeholder. In this way, the researcher can always reconstruct
exactly what each respondent saw when taking the survey. Note
that, as discussed above, DDS does not store participant data after
uploading it to the SP; DDS instead uses the respondent data stored
in the SP to generate the annotated export.
4.5 Participant Flow
Survey participantsreceive an invitation link directing them to DDS.
Participants are presented with an authorization interface asking
them to log into each DP and grant access to their data, as described
in the comprehensive table (shown in Figure 9a). Figure 9b shows
an example of authorizing access to Fitbit. After the participant
grants access to all required DPs, DDS will download the data
required to compute the required variables and then upload it to
the SP. DDS will then redirect the participant to the SP to take
the survey, via a unique survey distribution link (the “proceed”
button shown in Figure 9c). Figure 10 shows an example of how
the templated question from Figure 8 would look to a participant:
the variables have been flled in with personalized values drawn
from the participant’s Fitbit account.
4.6 Extensions and Forward Compatibility
DDS was designed and implemented to be extensible. It can be
integrated with SPs and DPs that ofer APIs. SPs that ofer APIs
similar to Qualtrics (single global API key) and SurveyMonkey
(fne-grained authorization via OAuth) should be easy to integrate.
In contrast, it could require signifcant efort to integrate SPs with
no API that instead ofer remote control via JSON-RPC (such as
LimeSurvey). Similarly, integrating Google Forms would require
workarounds, such as using addons (e.g., Dynamic Fields Add-on
for Google Forms™) to allow piping data from another source (e.g.,
from Google Sheets). Additional DPs could be integrated, as many
online platforms ofer APIs with OAuth support.
Regarding forward compatibility, drastic changes to SPs or DPs
could prevent DDS from working. We do not expect major issues,
as we rely on public web APIs, which tend to be fairly static or at
least backward compatible, to access basic functions of SPs and to
extract respondents’ data from DPs. These public APIs are unlikely
to change in a way that would prevent DDS from functioning [87].
22
However, if a public web API were to be closed altogether, nothing
could be done as a workaround.
With regard to continued development, a road map of features and functionality that we plan to implement is available on
GitHub.
23 We hope that DDS will gain community support in the
longer term to maintain the platform and continue adding SPs and
DPs.
5 DISCUSSION
5.1 Contribution
In this paper, we make two key contributions to the HCI research
community: frst, we conducted formative research (a literature
survey and a user survey of researchers) to characterize when and
why researchers might fnd data-driven surveys useful. We found
many ways that data-driven surveys can be benefcial, including
by improving accuracy, reducing the burden on participants to recall events, avoiding survey questions in favor of measurements,
and by providing concrete and personal examples rather than hypothetical ones when asking participants about their perceptions
22For example, Qualtrics has introduced few breaking changes to their API, and none
of them removed the core functions that we use [1]. 23https://github.com/DataDrivenSurveys/DataDrivenSurveys
and preferences. Currently, implementing this kind of data-driven
survey is an ad-hoc process, often requiring technical expertise
for developing custom tools. Our formative research underscores
the importance of carefully managing participants’ privacy and of
obtaining meaningful consent when accessing their data from other
platforms as part of a survey. These privacy aspects are not specifc
to our solution but to data-driven surveys in general, including
those conducted in the related works.
Second, we designed and implemented DDS, a minimum viable product tool that researchers can use to easily implement
data-driven surveys, regardless of their technical expertise. DDS
currently integrates with Qualtrics and SurveyMonkey as survey
platforms (SPs), as well as Fitbit, Instagram, and GitHub as data
providers (DPs). DDS enables using respondents’ data from DPs
in survey fow logic, templated questions and answers. DDS also
enables selecting individual items (e.g., a ftness activity or an Instagram post) based on researcher defned rules. DDS is designed
to limit the data that is requested from DPs, to limit the storage of
the obtained data; and permissions are revoked immediately after
the necessary data is obtained. DDS is open-source and extensible,
and we hope that other researchers will make use of it to enhance
their surveys.
5.2 Limitations and Future Work
5.2.1 Limitations. Our work has several limitations. First, our literature survey was limited to papers relating to ftness trackers, only
a small slice of HCI overall (and survey research more broadly).
As such, we may not have learned about all possible use cases for
data-driven surveys. However, we believe that we found enough
evidence of their potential utility to motivate developing a tool.
Our researcher survey was also relatively small (� = 52) and did
not reach a representative sample of HCI researchers; as with the
literature survey, we nonetheless found the results sufciently encouraging to develop DDS.
Most importantly, though data-driven surveys can provide many
important benefts for research, they do ask participants to provide
accessto a potentially large amount of personal data, which could be
uncomfortable. Requiring participants to log into specifc accounts
and share data could reduce participation and bias samples toward
only those willing to share. As such, it is critical that researchers
using this approach apply best practices to deserve and maintain
participant trust: limiting requests to DPs’ APIs to the minimum
required to achieve their research goals; being very clear from the
outset about the information participants will be asked to share and
the way it will be used; obtaining meaningful consent; and using
best practices for secure data storage.
The use of data-driven surveys may have unintended consequences. First, regarding security and privacy, DDS could facilitate
malicious actors posing as researchers extracting data from people.24 Second, issues related to survey design, such as priming,
could become pronounced with data-driven surveys. For example,
asking questions where participants are shown routes of their runs,
and then asking about privacy concerns may prime them to be
more privacy conscious. Hence, researchers should take great care
when designing data-driven surveys.
5.2.2 Future Work. Currently, DDS is limited to two SPs and three
DPs with only a few built-in variables. Nonetheless, we believe it is
sufcient to demonstrate the feasibility of the approach, illustrate
the underlying concepts, and showcase its potential. We will continue developing DDS, hopefully with the input and contribution
of interested researchers and developers. In future work, we hope
to extend this to other DPs, such as Spotify, Slack (for surveys of
workers in diferent companies or industries), other social media
platforms, and other data sources with useful APIs. This extension
does not present signifcant technical difculties, as many online
platforms have a similar fow to use their APIs, including using
OAuth for authentication.
Another extension to DDS could be support for the experience
sampling method (ESM) [50, 77] that captures participants’ experiences and behaviors in their natural context. ESM can lead to
survey fatigue when participants must respond at set intervals,
especially if there are multiple questions. Previous studies showed
that simple personalization in the ESM method (e.g., selecting a
time slot for reporting [55]) or the use of event-contingent notifcations (e.g., following a smartphone unlock event [78]) could lead to
higher response rates and recall accuracy. An extended version of
DDS could trigger surveys based on participants’ real-time data (as
obtained from DPs’ APIs), such as only after certain exercise events.
A data-driven approach could reduce the questions per ESM survey
by measuring activity rather than requiring self-reporting.
In order to tackle the ethical and privacy issues raised by datadriven surveys,25 we intend to explore the design of privacypreserving solutions. Such solutions could include integrated computational data obfuscation techniques to protect respondents’ privacy (rounding numeric variables, redacting sensitive text, blurring
parts of photos, etc.) with respect to the researchers and limit the
risks of re-identifcation that would use the values of the exported
variables as pseudo-identifers.
Finally, we plan to evaluate DDS from the researchers’ perspective. Drawing on suggestions from Ledo et al. [52] on evaluating
toolkits in HCI, we plan to conduct a usability study [51], in which
we ask researchers to develop mock surveys, to measure DDS’s
usability using established usability metrics such as the System
Usability Scale (SUS) [12], as well as efciency, learnability, accuracy, and satisfaction. Findings from such a study could suggest
ways to improve DDS. We also anticipate reporting on case studies,
both of our own usage and from other researchers. Furthermore,
we intend to study respondents’ acceptability and privacy concerns
regarding data-driven surveys. Due to aforementioned privacy issues and general limitations of data-driven surveys, understanding
how respondents perceive them would ofer valuable insights.
6 CONCLUSION
We conducted formative research by using literature and researcher
surveys, and we developed DDS, an open-source platform for a
streamlined and simple way to create data-driven surveys. It currently integrates with Qualtrics and SurveyMonkey, and supports
importing data from Fitbit, Instagram, and GitHub. DDS enables
both technically-savvy and non-savvy users to create data-driven
surveys without requiring any programming. We believe that the
thoughtful use of data-driven surveys can improve the quality of
user survey results and experiences, and that this can enable the
creation of exciting new opportunities for user-centered research.
ACKNOWLEDGMENTS
This work was partially funded by the Swiss National Science Foundation with Grant #200021_178978 (PrivateLife). We thank Holly
Cogliati for proofreading this article. We thank Lahari Goswami
and James Tyler for participating in the researcher survey cognitive
pretests. We thank Carmela Troncoso and the School of Computer
and Communication Sciences at École Polytechnique Fédérale de
Lausanne for supporting Michelle Mazurek’s visit to Switzerland,
which contributed to this collaboration. We thank the anonymous
researchers who participated in our online survey and shared their
valuable insights and experiences.