# Probabilistic Scheduling

Objective:

1. Describe techniques to model cost and schedule uncertainty
2. Provide an introduction to building a fully integrated cost and schedule uncertainty analysis

## Scheduling Methods

* Deterministic
  * Critical Path Method
  * Precedence Diagram Method
  * Critical Resource Diagram
  * Line-of-Balance
  * Critical Chain Method
  * Design Structure Matrix
* Probabilistic
  * PERT
  * Monte Carlo

## Deterministics vs Probabilistic

| ![Figure PE_to_distribution](../images/jcsrua/PE_to_distribution.svg) |
| :-----------------------------------------------------------------: |
|                 From Deterministic to Probabilistic                 |

## Statistics

### Descriptive Statistics

| Statistic                | Formula                                                           |
| ------------------------ | ----------------------------------------------------------------- |
| Mean                     | $ \bar{y} = \frac{1}{n} \sum_{i=0}^n y_i$                       |
| Median                   | $ y_i : P[y_j \leq y_i] = .5 \quad \text{where} \quad j \neq i$ |
| Mode                     | $ ml : P[y = ml] = max(P[y])$                                   |
| Skewness                 | $ Skewness(Y) = E \left( \frac{y-\mu_Y}{\sigma_Y} \right)^3$    |
| Standard Deviation       | $ S = \sqrt{\frac{\sum_{i=0}^n (y_i - \bar{y})^2}{n-1}}$        |
| Probability Distribution | $P[x]$                                                          |
| PDF                      | $f(x) = P[X = x]$                                               |
| CDF                      | $F(x) = P[X \leq x] = \int_{-\infty}^{\infty} f(x) \text{d}x$   |

## Point Estimate

### Requirements

| Base               | Description                                      |
| ------------------ | ------------------------------------------------ |
| Program of Record  | Defined in the requirements documents            |
| Technical Baseline | Alternative that reflects a technical assessment |
| What-If Case       | For a specific sensitivity analysis              |

### Estimating Method

* Analogy
* Parametric
* Engineering
* Extrapolation

### Implementation Method

| Modeling Approach                     | Description                                                                                                                                              |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| As a function of technical parameters | Uncertainty is assigned to the equation itself and to its inputs                                                                                         |
| As a factor of another estimate       | The factor is one form of a parametric equation                                                                                                          |
| Level of Effort (LOE)                 | Quantity times the cost per unit, burn rate times a duration, etc.                                                                                       |
| Throughputs                           | Analogies, quotes, subject matter expert opinion, etc.                                                                                                   |
| Third Party tool results              | When moving results from another model or tool into another, it is not enough to import the point estimate; the uncertainty needs to be imported as well |

### Output

$PE = f(X)$

## Sensitivity Analysis

### Definition

Systematic approach used to identify the impact of potential changes to one or more of an estimate's major input parameters on the total PE.

### Objective

1. Vary input parameters over a range of probable valuesm
2. Recalculate the PE
3. Determine how sensitive the PE is to changes in the input parameters

### Output

$opt$, $ml$, $pess$

## Uncertainty Distributions

### Overview

The PE:

* represents one possible estimate based upon a given set of program characteristics,
* serves as the reference point on which the cost uncertainty analysis is anchored,
* may be determined via one of three approaches:
  * **objective** (statistical analysis of relevant historical data),
  * **subjective** (expert opinion), or
  * **third-party tools** (separate models).

#### Objective

#### Definition

**Objective uncertainty** is an assessment of the uncertainty based on well-defined statistical processes.

#### Methods

* Developing parametric equations through **regression analysis**
* **Fitting** distributions to historical data or residuals

##### Regression Analysis

##### Curve Fitting

#### Subjective

#### Definition

**Objective uncertainty** is an assessment of the uncertainty based on well-defined statistical processes.

#### Conditions

* Applies where objective uncertainty distributions are not available
* Distributions are characterized by parameters describing their
  * dispersion ($LB$, $UB$)
  * skewness

Ideally, distribution parameters are developed from an objective assessment of relevant historical data. Often, it is necessary to rely on **informed opinion**. The analyst generally has to resort to expert judgment, such as that possessed by engineers, managers, and other knowledgeable people
This process is called elicitation, which can be difficult to do and subject to numerous biases, categorized as **Motivational** and **Cognitive**.

##### Biases

| Category     | Bias                                                                                                                                                                                                                        |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Motivational | Social pressure (face-to-face)<br />Impression (not face-to)<br />Group Think<br />Wishful thinking<br />Career goals<br />Misunderstanding<br />Project Advocacy<br />Competitive Pressures                                |
| Cognitive    | Representativeness (small sample)<br />Availability (most recent)<br />Anchoring and Adjustment<br />Inconsistency (opinion changes over time)<br />Relating to irrelevant analogies<br />Underestimation<br />Human Nature |
| Other        | Confirmation Bias<br />Premature Termination<br />Inertia<br />Selective Perception<br />Optimism Bias<br />Recency<br />Repetition Bias<br />Escalating Commitment<br />Attribution Asymmetry                              |

##### Best Practices

* Have historical **$min$**, **$max$**, and **averages** on hand for discussion
* Ask for **$LB$** and **$UB$**
* Seek the **$ml$** value
* Select a distribution shape based on **skew** and **firmness** of the bounds

##### Adjustment

Unless there is no evidence to do otherwise,

1. Treat subjective bounds (expert opinion) as 70\% range, and
2. Adjust for skew when using triangular, uniform, or PERT.
