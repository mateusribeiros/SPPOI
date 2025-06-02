Title: An empirical study of testing machine learning in the wild

Background: Recently, machine and deep learning (ML/DL) algorithms have been increasingly adopted
in many software systems. Due to their inductive nature, ensuring the quality of these systems remains a
signi!cant challenge for the research community. Unlike traditional software built deductively by writing
explicit rules, ML/DL systems infer rules from training data. Recent research in ML/DL quality assurance has
adapted concepts from traditional software testing, such as mutation testing, to improve reliability. However,
it is unclear if these proposed testing techniques are adopted in practice, or if new testing strategies have
emerged from real-world ML deployments. There is little empirical evidence about the testing strategies.
Aims: To !ll this gap, we perform the !rst !ne-grained empirical study on ML testing in the wild to identify
the ML properties being tested, the testing strategies, and their implementation throughout the ML work"ow.
Method: We conducted a mixed-methods study to understand ML software testing practices. We analyzed test
!les and cases from 11 open-source ML/DL projects on GitHub. Using open coding, we manually examined
the testing strategies, tested ML properties, and implemented testing methods to understand their practical
application in building and releasing ML/DL software systems.
Results: Our !ndings reveal several key insights: 1.) The most common testing strategies, accounting for less
than 40%, are Grey-box and White-box methods, such as Negative Testing, Oracle Approximation, and Statistical
Testing. 2.) A wide range of 17 ML properties are tested, out of which only 20% to 30% are frequently tested,
including Consistency, Correctness, and E!ciency. 3.) Bias and Fairness is more tested in Recommendation (6%)
and CV (3.9%) systems, while Security & Privacy is tested in CV (2%), Application Platforms (0.9%), and NLP
(0.5%). 4.) We identi!ed 13 types of testing methods, such as Unit Testing, Input Testing, and Model Testing.
Conclusions: This study sheds light on the current adoption of software testing techniques and highlights
gaps and limitations in existing ML testing practices.
CCS Concepts: • Machine learning and Deep Learning ! Testing practice; Testing strategy; • Test types;
Additional Key Words and Phrases: Machine learning, Deep learning, Software Testing, Machine learning
work"ow, Testing strategies, Testing methods, ML properties, Test types/ Types of testing

1 Introduction
The increasing adoption of Machine Learning (ML) and Deep Learning (DL) in many software
systems, including safety-critical software systems (e.g., autonomous driving [31, 104], medical
software systems [84]) raises concerns about their reliability and trustworthiness. Ensuring the
quality of these software systems is yet an open challenge for the research community. The main
reason behind the di#culty in ensuring the quality of ML software systems is the shift in the
development paradigm as induced by ML. Contrary to traditional software systems, where the
engineers have to manually formulate the rules that govern the behavior of the software system
as program code, in ML the algorithm automatically formulates the rules from the data. This
paradigm makes it di#cult to reason about the behavior of software systems with ML components,
resulting in software systems that are intrinsically challenging to test and verify. A defect in an ML
software system may come from its training data, the program code, execution environment, or
even third-party frameworks. A few research advances in the quality assurance on ML systems
recently have adapted di$erent concepts from traditional (i.e., software not using ML) software
testing, such as evaluating their e$ectiveness (e.g., mutation testing [34, 88]) and introduced new
techniques to verify the security or privacy of an ML system (e.g., Spoo!ng attacks in autonomous
systems [25, 131]), to help improve the reliability of ML based software systems.
With the support of programming languages like Python and C/C++, ML engineers can e$ectively
perform both white-box and black-box testing on ML models and software systems. Notably, blackbox tests can be written in Python even if the system under test (SUT) is not written in Python.
ML engineers can develop test cases, which are collections of unit tests that verify a function’s
performance under various conditions. These test cases consider all possible inputs that the function
is expected to handle, ensuring comprehensive coverage. By analyzing the test code of an ML
software system, we can gain insights into the testing strategies employed by ML engineers, the
ML properties they test, and the types of tests or testing types they utilize in their work"ow.
We de!ne testing strategies as the various approaches and resources employed during testing
activities to identify defects in software or ML systems. It speci!es the methods and techniques
to be used, the types of testing to be conducted, the test environments to be employed, and the
criteria for test completion. These strategies are crucial to ensuring that testing activities meet
software quality assurance objectives and that the most suitable methods are used to evaluate
the behavior of ML systems and the e$ectiveness of existing test cases. In ML/DL, factors such as
randomness and "oating-point arithmetic often lead to signi!cant discrepancies between computed
results and expected outcomes across di$erent test runs, making ML systems challenging to test.
ML engineers often resort to strategies like Oracle Approximation [98], which allows for slight
di$erences between computed results and the oracle, rather than specifying exact values for tests.
For example, to test the correctness of an ML component, engineers might use a rounding tolerance
approximation API provided by the unittest framework in Python. This approach enables a
speci!ed number of decimal places (dp) for rounding the actual value of the code under test (a_val)
and its expected value (oracle), as shown in the assertion: assertAlmostEqual(a_val,
oracle, places=dp). Similarly, to determine the optimal threshold value for classi!cation,
ML engineers often implement appropriate Thresholding strategies [111, 123] that maximize a
balance among di$erent performance metrics (e.g., Recall, Precision, Accuracy) instead of relying
on the default classi!cation threshold (e.g., 0.5).
In the context of an ML software system, ensuring that the software behaves adequately also
involves guaranteeing that critical “ML properties” are not violated during the development and
evolution of the system [42]. These “ML properties” refer to underspeci!cation issues and requirements that must be satis!ed to ensure that a model behaves as expected. Examples of such
properties include functional correctness, consistency, e#ciency, bias and fairness, robustness,
among others. These requirements are essential to ensure that models generalize as expected in
deployment scenarios [18, 132, 150]. Violating these properties often results in instability and
poor model performance in practice. Testing these properties is crucial not only for producing
high-quality software systems but also for regulatory and auditing purposes [48]. Therefore, ML
properties should be tested throughout the ML work"ow to ensure that the generated models meet
expected requirements, by following some “testing strategy (s)” and “test types”. Software test
types encompass various activities used to validate the System Under Test (SUT) for de!ned test
objectives. These methods are categorized into types such as black-box or white-box testing. Similar
to traditional software systems, ML engineers employ numerous testing types, including unit tests,
integration tests, and manual tests, throughout the development process [1]. This comprehensive
testing ensures that the ML software system can operate successfully under multiple conditions
and across di$erent platforms.
However, little is known about the current practices for testing ML software systems, and
it remains unclear if the testing techniques proposed in research are being adopted in practice.
Additionally, the emergence of new ML testing techniques from real-world deployments is largely
unknown. To !ll this gap, we conduct the !rst !ne-grained empirical study on ML testing practices
in the wild, aiming to identify the ML properties being tested, the testing strategies employed, and
their implementation throughout the ML work"ow. We manually analyzed the test code contents of
11 ML software systems from four (4) di$erent application domains; Computer Vision (CV) systems
(e.g., Autonomous driving), NLP systems (e.g., Voice recognition), Recommendation systems (e.g.,
Lightfm), and Application Platform (e.g., Medical system, Distributed ML, Music and Art Generation
with Machine Intelligence), by following an open coding procedure to derive a taxonomy of the
ML testing strategies used by ML engineers. Second, we examine the speci!c ML properties that
engineers commonly test throughout the ML work"ow. Third, We examine the software types of
tests/testing types that are used to test the ML software systems in the ML development phases.
Moreover, we compare the usage of the di$erent testing strategies, the tested ML properties and
the tests methods across the studied ML software system’s and the ML domains.
Overall, our !ndings provide actionable implications for di$erent groups of audiences: (1) ML
practitioners can use our presented taxonomy to learn about the existing ML testing strategies that
they can implement in their ML work"ow, especially the most frequently used testing strategies,
Grey-box and White-box testing, such as: Exception and Error Condition, Statistical Analysis, Decision
& Logical Condition, and Oracle Approximation. Our results can also guide them on how to verify
speci!c ML properties, such as functional correctness and consistency, e#ciency and Robustness.
(2) Researchers can build on our work to further investigate the e$ectiveness of di$erent ML
testing strategies and investigating the underlying reasons for the non-uniform application of these
methods across di$erent ML software systems with the end goal to developing standardized best
practices for ML testing. (3) Designers of testing tools can develop better tooling support to the
help testing for ML properties (e.g., Security and privacy, Bias and fairness, Certainty, Compatibility
and Portability), across the di$erent ML domains such as CV, NLP, and Recommendation Systems.
In summary, we make the following main contributions:
• To the best of our knowledge, this is the !rst empirical study on the adoption of research
advances in software testing of ML software systems by the industry, speci!cally by examining
the testing strategies, the ML properties, and the testing types adopted in the !eld. Speci!cally,
we highlighted 15 major categories of testing strategies, 17 di$erent ML properties, and 13
di$erent types of tests that the ML engineers commonly test.
• We compared how the tests are distributed across the ML work"ow, ad observed that a
signi!cant portion of testing activities occurs during model training and feature engineering.
• We provided a comparison of the testing strategies, the testing properties and testing types
used across the studied systems to identify common or inconsistent practices in their existing
testing practices. We observed an overall uneven distribution in the testing practice, with a
signi!cant number of studied ML software systems relying on a limited number of testing
strategies and testing types, which could potentially lead to gaps in coverage.
• We highlighted some challenges and proposed new research directions for the research community. Moreover, we discussed the potential applications of the identi!ed testing strategy
to help drive future research. ML practitioners can also leverage our !ndings to learn about
di$erent testing strategies, properties to test, and testing types that can be implemented to
improve the reliability of their next ML software system.
Paper organization: The remainder of the paper is organized as follows: in Section 2, we
provide background information on ML work"ows and discuss related works. Section 3 describes
the eight major steps of our methodology. Section 4 presents the results of our analysis, addressing
three research questions. Section 5 discusses more our !ndings, the critical analysis, the challenges
and lessons learnt and the implications of our !ndings. Section 6 outlines potential threats to the
validity of this work. Finally, Section 7 concludes the paper.
2 Background on Machine Learning workflow
In this study, we want to assess the practice of testing ML software systems across the entire ML
work"ow. Figure 1 highlights nine activities of a machine learning work"ow to build and deploy
ML software system adopted from Microsoft [5]. This work"ow is comparable to those used by
other major companies, such as Google [58], and IBM [72]. Below are the nine activities of this ML
work"ow:
(1) Model Requirements: The primary activity in constructing a machine learning model is
specifying the model’s requirements. Based on the product and the problem statement, the decision
is made on the appropriate types of models for the problem and features to implement with machine
learning. (2) Data collection: This activity follows after the model requirements, where the data
from di$erent sources are identi!ed and collected. This data may come from batch storage software
components such as databases and !le storage or generated from external components such as
detection components (e.g., camera or LiDAR sensors). Indeed, most ML training would require
a considerably large amount of data to train from and make meaningful inferences on the new
data, making the data collection challenging. (3) Data cleaning: Once the data is gathered, the next
activity (Data cleaning) is to process or clean the data to remove anomalies that are likely to hinder
the training phase. Most activities common to data science are performed during this step, such as
generating descriptive statistics about the features in the data and the distribution of the number of
values per example. (4) Data labeling: Assigns ground truth labels to each data record, for example,
assigning labels to a set of images with the objects present in the image. This step is required in
most supervised learning techniques to induce a model. (5) Feature engineering: This activity is
where the features are being prepared and validated for training. This activity also includes data
