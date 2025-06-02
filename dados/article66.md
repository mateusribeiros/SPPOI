Title: Causal Physics-Infused Hybrid Learning (CPIHL) Framework for Next-Gen Battery Health Forecasting

ABSTRACT A novel hybrid model, denoted by Causal Physics-Informed Hybrid Learning Neural Networks
(CPIHL), is developed in this study to significantly enhance the accuracy, interoperability, and real-time
feasibility of battery health predictions. The model incorporates the effects of temperature and voltage
on internal resistance, effectively capturing the non-linear electrochemical behaviors that drive battery
degradation. The proposed framework is rigorously validated using two open-source datasets: the Samsung
INR21700-50E and the Forklift Battery Degradation datasets. The CPIHL model demonstrates exceptional
performance, achieving an R2
score of 0.9994, a mean absolute error of 0.0007, and a root mean square
error of 0.0025, outperforming all baseline machine learning and deep learning models, including Random
Forest, Artificial Neural Networks, Long Short-Term Memory, and Gated Recurrent Units. The CPIHL
framework exhibits robust, interpretable, and scalable behavior, making it highly effective for predictive
maintenance tasks. It provides actionable insights for battery management, enabling the optimization of
operational strategies to extend battery life. By improving battery health monitoring, this work contributes
to sustainable energy usage, enhancing efficiency and reducing battery disposal waste.
INDEX TERMS Causality analysis, deep learning, hybrid learning, lithium-ion battery degradation, physicsinfused model, state of health.
I. INTRODUCTION
Prediction of battery’s Remaining Useful Life (RUL) and
State of Health (SOH) is necessary in applications such
as electric vehicles (EVs) to enhance the performance
and ensure reliability [1], in renewable energy storage
to have more efficient operation and long-term reliability [2], and in portable electronics for consumer satisfaction and safety in portable devices [3]. Accurate battery
health prediction allows for better maintenance planning,
reduced operational costs, and the prevention of unexpected
failures [4], [5], [6], [7], [8].
Artficial Neural Networks (ANN) [9], regression methods [10], and Deep Learning (DL) algorithms [11] and many
other data-driven solutions [6], [12], [13], [14], [15] which
correlate operational conditions i.e. temperature, current,
charge cycles, and different degradation patterns are utilized
in batteries. For example, [12], [13] present fusion-based
feature selection method and evaluates it on different machine
learning algorithms such as ANN and Support Vector
Machine (SVM). Reference [14] proposes a framework that
combines the ensemble nature methods; Gradient Boost (GB)
with ANN architectures to get better performance accuracy. Reference [6] explores different data-driven Machine
Learning (ML) such as elastic-Net Classification, Multilayer
Perceptron (MLP), and Recurrent Neural Networks (RNNs),
unsupervised learning such as Principal Component Analysis (PCA), and digital twin solutions for fault diagnosis
and safety enhancement. [15] utilized a range of ML
model including Linear Regression (LR), ANN, SVM, and
Random Forest (RF) to enhance battery management and
diagnostics. The integration of these techniques enables
more accurate and efficient predictions, addressing the
complexities of battery degradation and variability in realworld applications. Despite all these advancements, most of
the models fail to capture the underlying embedded physical
principles governing battery behavior chemistry and lacking
in robustness across different battery chemistry and operating
environments. References [16], [17], [18], and [19].
Physics-Informed Neural Networks (PINNs) [20] have
emerged to remedy this problem by embedding physical
laws into the neural network architecture to provide robust
solutions even with limited or noisy data. This approach
has been adapted to various domains [21], [22], [23],
[24], [25], including fluid dynamics[20], quantum mechanics
as presentented by [26] and [27], and more recently, in battery
degradation modeling as given by [28] and [29]. PINNs can
integrate electrochemical, thermal, and aging models into
the framework, making them more interpretable. However,
it falls short in coupling electrochemical and thermal effects
in different types of batteries. Recent studies such as [30]
coupled aging and thermal effects for Li-ion batteries, they
performed parameter sensitivity tests to identify the most
crucial factors on voltage and temperature as important candidates for identifying aging behavior. The proposed model
improved the calibration accuracy for aging mechanism.
However, it faced challenges in fully capturing the nonlinear
inter-dependencies between electrochemical, thermal, and
mechanical stress effects. The research done by [31] develops
a coupled electrochemical-thermal-mechanical model, integrate SEI growth, lithium plating, and cathode material loss
under varying C-rates and temperatures. However, the current
model still lacks broader exploration in cycling conditions
and integrating multi-scale framework. All these studies
emphasize the need of refined approaches to address these
limitations and improve predictive accuracy. This leaves the
gap open for conducting further research to address this and
integrating models that can generalize across diverse battery
chemistries and conditions.
Causal inferences [32] is critical field of research,
it addresses the interactions issues by uncovering causeand-effect relationships rather than simple correlations
between factors such as operating temperature, depth of
discharge, and battery health outcomes [33]. Alternative
operational scenarios can be executed via causal graphs
technique, enabling more informed predictions and effective
predictive maintenance strategies [34]. Accurate real-time
state-of-health estimation methods also integrate operating
temperature and depth of discharge as key predictors
for battery degradation [35]. Reference [36] introduces a
robust methodology to model lithium-ion battery aging
by combining experimental insights and semi-empirical
modeling techniques to accelerate aging tests to parameterize
a coupled impedance-based electro-thermal and aging model.
All these insights in research underscore the urge need
of precise parameter calibration to optimize long-term
performance [37].
Hybrid approaches that implement RF show promise in
enhancing ANN predictions by providing localized adjustments. The developed model by [38] enhances the ANN
estimator by the RF, they integrate the local adaptivity of
RF with the global approximation capability. Researchers
in [39] describe the use of Residual Networks (ResNets)
for feature extraction and passing the features to an Oblique
RF for improved time series classification performance.
Reference [14] proposes a model that combines gradient
boosting with neural decision forests. The residual learning
from the GB integrates well with ANN, optimizing prediction
performance. These studies shows how various methods combines the strengths of ANN and RF to enhance predictions
and interpretability. To this end, no explicit research explores
the use of residuals from ANN predictions in the context of
battery degradation modeling or RUL estimation.
In this paper, a novel hybrid framework that combines
PINNs with causal inference techniques to enhance the
accuracy and interpretability of RUL and SOH predictions
is proposed. By integrating physical models with causal
inferences, the proposed framework enables simulation of
optimizing models to estimate their impact on battery life.
The key contributions of this work start with introducing
the novel causal physics-infused hybrid learning (CPIHL)
framerwork, which is an architecture that integrates a
physics-informed layer based on Ohm’s Law with a residual
learning component to deliver interpretable and accurate
predictions for battery health. The physics-informed layer
models the relationship between voltage, current, and resistance, while the residual layer captures the non-linear effects
and the unmodeled dynamics through the machine learning
technique random forest. Demonstrating CPIHL’s robustness
across diverse datasets, effectively capturing both short-term
variability and long-term degradation effects. This is achieved
by leveraging domain-specific physical principles alongside
ML for improved generalization and adaptability. Compare
CPIHL superior predictive accuracy with advanced ML and
DL models, establishing a new benchmark in battery health
prediction. By combining domain knowledge with datadriven approaches, the framework effectively addresses the
limitations of purely physics-based or purely data-driven
ones. Finally, align with Sustainable Development Goals
(SDG) 7 and 12 by promoting clean energy management and
responsible resource utilization through precise battery health
insights. The integration of physics-based modeling ensures
physical consistency, while the hybrid approach optimizes
battery lifecycle management for sustainable energy systems.
The remainder of this paper is organized as follows:
Section II presents the methods including the datasets
used in the study, the novel CPIHL framework, and
Cross-Validation (CV) and hyperparameter optimization.
Section III presents the results of the causality inferences,
CPIHL performance and a comparison of prediction performance over a range of baseline ML and DL algorithms.
Section IV is the discussion of the results achieved and
CPIHL performance and finally the concluding remarks and
future work are summarised in Section V.
II. METHODOLOGY
A. DATASETS
In this study, two diverse datasets are used, Table 1
summarizes the key characteristics that distinguish Samsung
INR21700-50E [40] and Forklift Battery Degradation [41] in
battery chemistry and environmental conditions.
Both datasets capture real-world operational conditions
ensuring the validation of CPIHL under practical deployment
scenarios [42], [43], [44], [45]. These datasets share similar
feature sets with existing studies on battery degradation and
health estimation, such as voltage, current, and temperature [42], [45].
The Samsung INR21700-50E have 444 Hybrid Pulse
Power Cycle (HPPC) tests conducted on Samsung
INR21700-50E cells. The tests were conducted in a controlled environment at 25Â◦C, ensuring thermal equilibrium
during charge and discharge cycles. SOH estimation for this
dataset is performed using the following equation based on
voltage measurements:
SOHSamsung = f (Voltage). (1)
The second dataset, Li-ion battery degradation dataset
based on a realistic forklift operation profile is operating on
elevated temperatures (35-45Â◦C). The dataset predicts the
SOH using same equation 1, the voltage is captured during
the operational cycles.
TABLE 1. Summary of datasets used for hybrid model validation.
B. CAUSAL PHYSICS-INFUSED HYBRID LEARNING
FRAMEWORK CPIHL
The model architecture combines physics-based and datadriven machine learning methods to predict the SOH of the
battery cells. The physics-informed layer [28] contains
the data loss which is the mean squared error (MSE)
between the true values and the predicted values:
Ldata =
X
N
i=1

ui − ˆui
2
, (2)
where: ui
: true SOH value for the i-th sample, uˆi
: predicted
SOH value for the i-th sample, N: Total number of samples.
The core methodology of CPIHL integrates the domain
knowledge of Ohm’s Law, where the voltage V is approximated as:
V = I · R, (3)
where I represents the current and R is the resistance.
Resistance R can also depend on the effects of temperature,
a critical factor for battery performance. This addition is
implemented in equation 3 and used to model key battery
degradation processes based on [36]:
R = R0 + k · (T − T0) (4)
where R is the internal resistance of the battery. R0 is the
reference resistance at the reference temperature T0. k is
the proportionality constant accounting for the change in
resistance with temperature. T is the current temperature.
And T0 represents the reference temperature.
The causality is incorporated by studying the relationships
between temperature, resistance, and SOH, as identified in
the study [36]:
B(T , V) = cT ·

T − T0
1T

+ cV ·

V − V0
1V

(5)
where B(T , V) represents the aging rate as a function of
temperature (T ) and voltage (V), cT is the coefficient of
sensitivity of the aging rate to changes in temperature,
and cV is the coefficient of sensitivity of the aging rate
to changes in voltage. The variable T denotes the current
operating temperature, T0 is the reference temperature,
typically the baseline operating temperature. 1T is the
scaling factor for temperature, indicating the temperature
range over which aging is analyzed. The variable V is the
current voltage, and V0 is the reference voltage, typically the
nominal or baseline voltage. Finally, 1V is the scaling factor
for voltage.
The residual learning is next applied. Residuals are defined
as the difference between the true voltage values ytrue and the
physics-based predictions yphysics:
Residual = ytrue − yphysics. (6)
It monitors the effects that are not captured by the physics
layer, such as the battery aging and non-linear behavior.
RF regression machine is then trained on the residuals.
It enables the model to learn complex patterns from the
data and correct physics-based predictions. The final hybrid
prediction combines the physics-based estimates and the
machine learning residuals:
yhybrid = yphysics + Residualpredicted. (7)
This hybrid approach ensures physical consistency where
the physics-based models alone are insufficient due to simplifications assumptions. By combining domain knowledge
with ML, the hybrid model achieves improved prediction
accuracy and robustness while maintaining physical interpretability.
C. FRAMEWORK AND NON-LINEARITY MODELING
The complete model is illustrated in Figure 1. The flow
chart outlines the sequential steps in CPIHL framework.
The process begins with data preparation, including loading,
preprocessing steps, and feature engineering. The data is
then structured and split appropriately into training and
testing sets. This is crucial for maintaining data integrity and
preventing data leakage.
The hybrid prediction phase consists of a PINN layer
that embeds fundamental physical laws governing battery
behavior. The governing equations, including Ohm’s Law
and resistance-temperature dependencies, allow the model
to provide physically meaningful predictions while ensuring
consistency with electrochemical principles. The model then
predicts key battery parameters such as voltage and SOH.
By integrating domain knowledge into the learning process,
CPIHL enhances its interpretability and reduces the risk of
overfitting to data noise.
Following this, residual calculation is performed to quantify discrepancies between the physics-informed predictions
and actual observations. This is essential for identifying the
influence of unmodeled non-linearities such as hysteresis,
polarization effects, and transient heating. To address this,
CPIHL leverages a Random Forest regression model trained
using the residuals to enable the framework to learn and
compensate for complex, unstructured variations that are not
explicitly captured by the PINN layer.
Finally, the evaluation phase assesses the combined
model’s predictive accuracy using key performance metrics
such as R-squared (R2), Root Mean Square Error (RMSE),
and Mean Absolute Error (MAE). CPIHL framework is
then compared to advanced baseline machine learning and
deep learning models, such as Artificial Neural Networks
(ANNs), Long Short-Term Memory (LSTM) networks, and
Gated Recurrent Units (GRUs). By incorporating both
physics-based principles and machine learning corrections,
CPIHL ensures robustness across different battery types
and operating conditions, making it suitable for real-world
deployment in battery management systems.
CPIHL integration of the non-linearity in battery degredation based on multiple physics-based and machine
learning components. The resistance-temperature relationship accounts for changes due to thermal effects, while
voltage-SOH dependencies help track long-term degradation
trends. Complex electrochemical phenomena such as hysteresis, polarization effects, and transient heating introduce
non-linearities that are challenging to explicitly model using
purely physics-based or data-driven approaches due to their
dependence on operating conditions and battery chemistry.
Directly incorporating these effects into governing equations
would require highly specific experimental setups and
additional parameterization, making generalization across
different battery types difficult. Instead, CPIHL mitigates
these effects by employing a hybrid approach, where
the physics-informed model provides physically consistent
estimates, and the residual learning mechanism captures
deviations caused by unmodeled nonlinearities. The Random
Forest regression applied to residuals ensures adaptability
to dynamic conditions, enhancing robustness and predictive
accuracy without requiring extensive empirical calibration.
D. 5-FOLD CROSS-VALIDATION AND HYPERPARAMETER
OPTIMIZATION
Five-fold cross-validation with random search to choose the
best hyperparameters for all models is used in this study.
The results in table 2 summarizes the hyperparameters
selection of all methods used here.
TABLE 2. Hyperparameters for models in this study.
III. RESULTS
In this section the causality effect between different variables
when analyzed using granger causality and transfer entropy
is checked. The relationships between different battery
parameters are evaluated, this is depicted in the experiment
in III-A, other state-of-the-art machine learning and neural
network methods are investigated and CPIHL’s predictive
performance is evaluated in III-A compared to state-of-theart machine learning and neural network models. Finally,
an analysis of CPIHL’s runtime efficiency and computational
complexity analysis are provided to assess its feasibility for
real-time battery management applications.
A. CAUSALITY EFFECT BETWEEN DIFFERENT VARIABLES
USING GRANGER CAUSALITY AND TRANSFER ENTROPY
Granger causality and transfer entropy are used to analyse
the relationships between all features, concentrating on the
temperature, voltage effect on the resistance.
FIGURE 1. Overview of the CPIHL. The methodology begins with input data preparation,
including dataset loading, preprocessing, and feature selection. The PINN layer incorporates
physical laws and resistance-temperature relationships to predict features the resistance
and SOH. Residuals between true values and PINN predictions, are computed to account for
unmodeled effects. These residuals are used to train a random forest model for capturing
non-linear dynamics. The hybrid prediction combines PINN outputs with random forest
corrections, ensuring both physical consistency and improved accuracy. The framework is
validated and its performance is compared to the baseline machine learning models,
including ANN, LSTM, and GRU.
The selection of temperature (T ), voltage (V), and
resistance (R) as causal drivers was not arbitrary but guided
by a rigorous causality analysis. We applied both Granger
causality and Transfer Entropy to evaluate the directional
influence of all available features on battery degradation.
Figure 2 illustrates that T and V exert the highest causal influence on R, which in turn impacts the State of Health (SOH).
The statistical results in Table 3 confirm this observation,
where T → R and V → R exhibit significant causality
effects at lag 4 with p < 0.05. Transfer Entropy further
strengthens this argument, showing a dominant entropy value
of 23.026 for T → R, significantly higher than the entropy for
V → R. These findings align with physical battery dynamics,
where temperature fluctuations alter internal resistance due to
electrochemical reactions, while voltage variations affect the
charge-discharge cycle behavior. The inclusion of resistance
as an intermediate variable ensures that our framework
captures the non-linear and coupled electrochemical-thermal
effects on battery aging, reinforcing the robustness of the
CPIHL model.
The results for the Samsung INR21700-50E are summarised in Table 3.
Granger causality analysis as given in the Table 3 reveals
that the temperature has a statistical significant causal effect
on resistance at lag 4 (p < 0.05), highlighting a strong
directional influence. Voltage also influences resistance at lag
4 with a slightly weaker significance (p = 0.0378). Transfer
Entropy results further emphasize the dominant influence of
temperature, with a TE value of 23.02585 for temperature
to resistance, compared to a lower, yet non-zero TE value
FIGURE 2. Causal relationships based on transfer entropy results. Larger
circles and thicker arrows represent features with higher transfer entropy
values influencing R (Resistance).
TABLE 3. Causality effects between variables in samsung INR21700-50E
dataset.
of 2.96180 for voltage to resistance. These results suggest
the primary role of temperature in driving resistance changes,
consistent with the physical relationship resistance to temperature, while voltage has a secondary, less pronounced effect,
potentially reflecting indirect electrochemical processes.
Figure 3 illustrates the dynamic relationships between
temperature, voltage, and resistance over the analyzed time
segment. Clearly, explains the variations in temperature and
voltage and how it influences the resistance fluctuations
supporting the causality results in Table 3.
The causality relations for the forklift battery degredation
dataset are depicted in Figure 4, which shows high p-values
greater than 0.05, suggesting a non-causal relationship with
resistance. This is due to the granger causality assumning
a linear relationship between variables and tests whether
past values of one variable can predict another. If the
FIGURE 3. Relationships between temperature, voltage, and resistance
over time in SamsungINR21700-50E dataset.
FIGURE 4. Causal relationships based on granger causality and transfer
entropy results. Forklift battery degredation dataset.
relationship is nonlinear or involves complex interactions,
granger causality may fail to detect it; apparently this is
the case for this dataset. The transfer entropy analysis is
more general and does not assume linearity, here it suggests
that current and temperature are the dominant factors in
influencing the resistance in the RPT dataset. The entropy
results shows current as the most influential variable on
resistance with a high entropy value (6.88), followed by
temperature (2.84), while voltage, energy.
In the aging dataset, granger causality shows similar results
to the RPT ones. The transfer entropy analysis supports
also that, with entropy value for the current showing 3.87,
followed by energy (1.06) and voltage (0.58). These results
suggest that current and energy drive primarily resistance
changes in the aging dataset, aligning with the physical
dynamics of aging batteries.
The visualization in Figures 5 and 6 show the complexity of
the relationships between the different variables. The temperature exhibits sharp drops and rises, indicating non-linearity.
FIGURE 5. Relationships between temperature, voltage, and resistance
over time in forklift battery degradation (RPT) dataset.
Similar behavior for the resistance with strong variability
and outliers and noise-like patterns across the time index.
This visual complexity aligns with the discrepancies observed
between granger causality and TE analyses, suggesting
that non-linear and higher-order interactions may exist
between these variables, making causal inference more
challenging.
FIGURE 6. Relationships between temperature, voltage, and resistance
over time in forklift battery degradation (Aging) dataset.
B. CPIHL PERFORMANCE AND COMPARISON WITH
OTHERS AND NEURAL NETWORK METHODS
CPIHL prerformance was compared to several state-of-theart machine learning models. The results are illustrated in
Figrues 7, 8, and 9, and Tables 4, 5, 6, and 7.
For the Samsung dataset, CPIHL achieved an RMSE of
0.0008 ± 0.0001, MAE of 0.0001 ± 0.00001, and R
2 =
0.9999 ± 0.0001, significantly outperforming other neural
network-based models such as ANN and LSTM.
Similarly, for the Forklift battery degredation datasets,
CPIHL demonstrated superior performance in both the Aging
TABLE 4. Comparative analysis of battery health prediction models,
including CPIHL model and benchmark models from the literature gated
recurrent unit with battery performance predictor (GRU-BPP), XGBoost,
and linear mixed effects (LME) for RPT and Aging datasets, including
results from [7].
(R
2 = 0.9444 ± 0.0005) and RPT (R
2 = 0.9812 ± 0.0002)
scenarios, establishing its effectiveness in both short-term and
long-term health prediction contexts. Table 4 pTable 4 further
substantiates the superior performance of CPIHL by comparing it with additional advanced models, including GRU-BPP,
XGBoost, and LME. The results demonstrate that CPIHL
consistently outperforms all benchmark models, achieving
the lowest RMSE and MAE values across both datasets. This
underscores CPIHL’s robustness, reliability, and accuracy in
battery health estimation.
To this end, the results achieved confirm the superior
performance of the CPIHL over traditional and advnaced
NN-based models. Additionally, it achieved an interpretable,
physics-informed predictions, positioning it as a powerful
tool for next-generation battery health prediction.
FIGURE 7. Performance comparison for samsung INR21700-50E dataset.
C. RUNTIME OF THE PROPOSED CPIHL FRAMEWORK
The proposed Causal Physics-Infused Hybrid Learning
(CPIHL) framework was executed on a MacBook Pro with an
Apple M3 Pro chip, 12-core CPU, 18-core GPU, and 18 GB
unified memory. The runtime performance of the framework
TABLE 5. R
2 results for samsung INR21700-50E dataset.
FIGURE 8. Performance comparison for forklift battery degradation (RPT)
dataset.
TABLE 6. R
2 performance comparison for forklift battery degradation
dataset (RPT).
TABLE 7. R
2 results for forklift battery degradation dataset (Aging).
is evaluated based on inference time during testing, where
execution times are reported as averages Â± standard
deviation (std) over multiple runs.
FIGURE 9. Performance comparison for forklift battery degradation
(Aging) dataset.
To assess real-time feasibility, the framework processes
a batch of 32 samples in an average time of 0.00219 ±
0.00005 seconds, while the expected time threshold per
batch, based on dataset timestamps, is 0.032 seconds. This
corresponds to a per-sample testing time of 0.0000684 ±
0.0000015 seconds, which remains significantly lower than
the 0.001-second interval between consecutive data points in
the dataset. The batch size of 32 samples was selected based
on empirical testing and analysis of the dataset’s sampling
rate. The timestamps from our dataset indicate that samples
arrive at a rate of approximately 100 Hz (every 10 ms
per sample).
The batch size of 32 samples was selected based on
empirical testing and analysis of the dataset’s sampling
rate. The timestamps from our dataset indicate that samples
arrive at a rate of approximately 100 Hz (every 10 ms
per sample). Processing batches of 32 samples optimizes
computational efficiency while ensuring real-time constraints
are met. This configuration guarantees that predictions are
generated before new data arrives, aligning with real-world
streaming battery health monitoring requirements. Increasing
batch size beyond 32 leads to diminishing returns due to
latency in data handling, whereas reducing it significantly
increases computational overhead.
The runtime results confirm that CPIHL inference operates
well within real-time constraints, as the time required to
generate predictions is nearly 14 times faster than the
arrival rate of new data. This ensures that the model can
successfully process each battery health data point before
the next observation arrives. These findings highlight the
feasibility of deploying CPIHL for real-time SOH and RUL
estimation, making it suitable for practical battery management applications where timely predictions are crucial. For
the Forklift dataset, including both RPT and Aging scenarios,
the framework achieves an average batch testing time of
0.00430 ± 0.00008 seconds and a per-sample inference time
of 0.000134 ± 0.000002 seconds, still well within real-time
constraints given the dataset’s 0.001-second sampling interval, demonstrating its scalability across different battery types
and operating conditions.
D. COMPUTATIONAL COMPLEXITY ANALYSIS
To validate the real-world applicability of CPIHL, we analyze
its computational complexity, memory footprint, and execution time. CPIHL consists of two sequential components: the
Physics-Informed Neural Network (PINN) and the residual
correction model using Random Forest (RF) regression. The
computational complexity of the PINN is determined by its
dense layers, leading to an overall complexity of O(NL),
where N is the number of neurons per layer and L is the
number of layers. The Random Forest model introduces an
additional complexity of O(TD log M), where T is the number
of trees, D is the depth of each tree, and M is the number of
training samples. Since these components operate in series
rather than in parallel, the total complexity is given by:
O(NL) + O(TD log M).
To benchmark execution performance, we trained and tested
CPIHL on an Apple M3 Pro system. The total inference
time for a batch of 32 samples was recorded as 0.00219 ±
0.00005 seconds, ensuring that CPIHL operates within realtime constraints. Compared to standard deep learning models
such as LSTM and GRU, CPIHL incurs a slightly higher
computational cost due to the physics-informed component
but benefits from improved generalization and robustness.
These results confirm that CPIHL is both computationally
efficient and scalable for large-scale deployment.
IV. DISCUSSION
The results highlight the superiority of the causal physicsinfused hybrid learning framework, compared to advanced
ANN methodologies. The multi-layer architecture integrates
the physics-based modeling with data-driven approaches,
it addresses also the physical interpretability of the battery
model by addressing the challenges of battery health
prediction, delivering both high accuracy and physical clarity.
This dual representation ensures that the model is consistents with physical principles and improve the accuracy.
The CPIHL framework achieved exceptional results on
the Samsung INR21700-50E dataset, with an RMSE of
0.0008 and MAE of 0.0001, outperforming random forest,
ANN and, other LSTM variations. This underscores the
advantages of leveraging domain knowledge, such as Ohm’s
law and resistance-temperature relationships, in predictive
modeling. CPIHL demonstrates the effectiveness of combining physics-informed layers with residual correction through
machine learning. This approach not only improves accuracy
but also ensures consistency with the underlying physical
principles, a feature that purely data-driven models like ANN
R
2 = 0.9809 and LSTM R
2 = 0.9959 struggle to achieve.
By including direct relationships between temperature and
resistance, the novel model prediction’s alligns well with
the observed electrochemical phenomena. Granger causality
analysis shows significance statistically which captures the
influence of temperature on resistance at lag 4 (p = 0.0150),
with transfer entropy stressing the dominant role of the
temperature with (TE = 23.02585). This integration of
causality ensures the robust reliability in capturing non-linear
dynamics that purely data-driven models, such as Bi-LSTM
R
2 = 0.9964, fail to explain.
For the Forklift Battery Degradation datasets, CPIHL’s
robustness across both aging and RPT datasets demonstrates
its versatility in handling both short-term variability and
long-term degradation patterns. On aging dataset CPIHL
achieved an impressive RMSE = 0.0075, outperforming ANN
RMSE = 4.2951 and LSTM RMSE = 0.6375. Similarly
on the RPT, the CPIHL outperformed the best achieving
algorithm attention-LSTM by (6.93%). Additionally, the
causality transfer entropy findings complement the accuracy
results, showing the current as important factor in resistance
changes. The results of TE value of 6.88 compared to
temperature (TE = 2.84), show this complementary role of the
current. The results emphasize the limitations of purely neural
network-based models in capturing the complex dynamics of
battery systems, especially when physical principles are not
integrated. While advanced architectures such as AttentionLSTM and Bi-LSTM improved performance compared to
ANN and LSTM, their reliance on data alone makes them less
reliable for generalizing across different conditions. CPIHL
bridges the gap between causality, physics, and machine
learning, leveraging the strengths of both to provide accurate
and reliable predictions. Its ability to capture non-linear
interactions through the hybrid approach ensures adaptability
across diverse datasets and battery chemistries. Overall,
CPIHL sets a new benchmark in battery health prediction,
demonstrating the potential of fusing physics and causality
in predictive modeling. This research aligns with the United
Nations Sustainable Development Goal 7, which focuses
on ensuring access to affordable, reliable, sustainable, and
modern energy for all. By improving the accuracy and
reliability of battery health predictions, this study contributes
to enhancing the efficiency and longevity of energy storage
systems, ultimately supporting the transition to renewable
energy and sustainable energy management practices.
V. CONCLUSION AND FUTURE WORK
In this study, CPIHL Framework is introduced, a novel and
approach that synergizes physics-based principles, causality,
and advanced machine learning models to predict battery
health with unprecedented accuracy and interpretability.
By embedding domain-specific knowledge—such as Ohm’s
Law and resistance-temperature relationships—into the
learning process, CPIHL not only achieves state-of-the-art
predictive performance but also ensures that predictions
are physically consistent and interpretable. This framework
effectively bridges the gap between traditional empirical
models and purely data-driven deep learning methods,
delivering robust performance across a wide range of
operational conditions. Through comprehensive evaluations
on diverse datasets, CPIHL has demonstrated scalability,
adaptability, and generalization capabilities, consistently
outperforming conventional machine learning models such
as ANN, LSTM, and GRU across key performance metrics.
Its unique ability to incorporate non-linear electrochemical
effects while maintaining physical consistency makes it
particularly well-suited for real-time battery health assessment and predictive maintenance applications. These results
underscore CPIHL’s potential to revolutionize battery health
monitoring, driving improvements in energy efficiency,
reducing operational costs, and supporting global sustainability initiatives. Future work will focus on enhancing
the scalability and computational efficiency of CPIHL to
facilitate its deployment in large-scale applications, such
as electric vehicle fleets and grid-scale energy storage systems. This will involve exploring real-time implementation
optimizations, including lightweight model adaptations and
edge computing integration, to improve inference speed and
energy efficiency. Further refinements to the causal inference
mechanisms will be pursued to deepen the understanding of
complex interactions within battery systems. This includes
improving the handling of hysteresis, polarization, and
transient heating effects, which will enhance the accuracy of
SOH and RUL predictions. Extension to Alternative Energy
Storage Technologies: The framework will be extended
beyond lithium-ion batteries to encompass other energy
storage technologies, such as supercapacitors and fuel
cells. This expansion will broaden CPIHL’s applicability
and contribute to the development of sustainable energy
solutions across diverse domains. Integration with IoT and
Edge AI. A key priority will be the integration of CPIHL
with IoT-based monitoring platforms to enable real-time
battery diagnostics and predictive maintenance in industrial
settings. By combining CPIHL with edge AI and cloudbased analytics, the framework can support the development of intelligent, automated, and energy-efficient battery
management systems. This integration will further solidify
CPIHL’s role in advancing sustainable energy solutions and
next-generation battery technologies. In summary, CPIHL
represents a significant leap forward in battery health prediction, offering a robust, interpretable, and scalable solution
that aligns with the growing demand for sustainable energy
management. Its continued development and deployment
hold immense promise for transforming energy storage
systems and contributing to a more sustainable future.