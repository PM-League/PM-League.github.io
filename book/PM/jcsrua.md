# Probabilistic Scheduling

Objective:

1. Describe techniques to model cost and schedule uncertainty
2. Provide an introduction to building a fully integrated cost and schedule uncertainty analysis

## Scheduling Methods

* Deterministic
  * Critical Path Method (CPM)
  * Precedence Diagram Method (PDM)
  * Critical Resource Diagram (CRD)
  * Line of Balance (LOB)
  * Critical Chain Method (CCM)
  * Design Structure Matrix (DSM)
* Probabilistic
  * Program Evaluation Review Technique (PERT)
  * Monte Carlo
  * Latin Hypercube Sampling (LHS)

## Deterministics vs Probabilistic

| ![Figure PE_to_distribution](../images/jcsrua/PE_to_distribution.svg) |
| :-----------------------------------------------------------------: |
|                 From Deterministic to Probabilistic                 |

## Statistics

### Descriptive Statistics

| Statistic                | Formula                                                                                                             |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| Random variable          | $X$                                                                                                               |
| Mean                     | $ \mu = \frac{1}{N} \sum_{i=1}^{N} x_i$                                                                           |
| Median                   | $ x : P[X \leq x] = .5$                                                                                           |
| Mode                     | $ Mo  : P[X = Mo] = \max[P(\bf{x})]$                                                                              |
| Skewness                 | $ Skewness(X) = \frac{\mu_3}{\mu_2^{3/2}}$ where $\mu_3$ and $\mu_2$ = third and second moments about $\mu$ |
| Standard Deviation       | $ \sigma = \sqrt{\sum_{i=0}^n (x_i - \bar{x})^2/N}$                                                               |
| Variance                 | $ \sigma^2 = \sum_{i=0}^n (x_i - \bar{x})^2/N$                                                                      |
| Probability Distribution | $P(X)$                                                                                                            |
| PDF                      | $f_X(x) = P(X = x)$                                                                                               |
| CDF                      | $F_X(x) = P(X \leq x) = \int_{-\infty}^{x} f(x) \text{d}x$                                                        |

## Point Estimate

### Base

| Base               | Description                                      |
| ------------------ | ------------------------------------------------ |
| Program of Record  | Defined in the requirements documents            |
| Technical Baseline | Alternative that reflects a technical assessment |
| What-If Case       | For a specific sensitivity analysis              |

### Cost vs Schedule PE

* Cost PE $\leftarrow$ approved WBS structure
  * Direct cost
    * Labor
    * Material
    * Equipment
    * Subcontract
  * Indirect cost
    * Taxes
    * Gen. Cond.
    * Risk
      * Profit
      * Contingency
    * Overhead
* Schedule $\leftarrow$ integrated network of activities containing all the detailed discrete work packages and planning packages (or lower-level tasks of activities) necessary to support the events, accomplishments, and criteria of the project plan.

### Estimating Method

* Analogy
* Parametric
* Engineering
* Extrapolation

### Implementation Method

| Modeling Approach                | Description                                                                                                                                              |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Function of technical parameters | Uncertainty is assigned to the equation itself and to its inputs                                                                                         |
| Factor of another estimate       | The factor is one form of a parametric equation                                                                                                          |
| Level of Effort (LOE)            | Quantity times the cost per unit, burn rate times a duration, etc.                                                                                       |
| Throughputs                      | Analogies, quotes, subject matter expert opinion, etc.                                                                                                   |
| Third Party tool results         | When moving results from another model or tool into another, it is not enough to import the point estimate; the uncertainty needs to be imported as well |

## Sensitivity Analysis

### Definition

Systematic approach used to identify the **impact of potential changes** to one or more of an estimate's major input parameters to the PE.

### Objective

1. Vary input parameters over a range of probable values,
2. Recalculate the PE, and
3. Determine how sensitive the PE is to changes in the input parameters.

### Output

| ![Figure sensitivity_analysis](../images/jcsrua/sensitivity_analysis.svg) |
| :---------------------------------------------------------------------: |
|                       Sensitivity Analysis Output                       |

## Uncertainty Distributions

### Overview

The PE:

* $=$ **one possible estimate** based upon a given set of characteristics
* $\rightarrow$ **reference point** on which the cost uncertainty analysis is **anchored**
* $\leftarrow$ approach:
  * **objective** (statistical analysis of relevant historical data),
  * **subjective** (expert opinion), or
  * **third-party tools** (separate models).

#### Objective

#### Definition

**Objective uncertainty** is an assessment of the uncertainty based on well-defined statistical processes.

#### Methods

* Developing parametric equations through **regression analysis**
* **Fitting** theoretical distributions to historical data

##### Regression Analysis

##### Curve Fitting

###### Descriptive Statistics

$\min$ < $LB$ < $Mo$ / $Median$ / $\mu$  < $UB$ < $\max$ where

* $\min = p_0$
* $\max = p_{100}$
* $LB = p_\alpha$
* $UB = p_{1-\alpha}$

##### Guidelines

| Distribution | Application                                                 | Parameters | Recommendation       |
| ------------ | ----------------------------------------------------------- | ---------- | -------------------- |
| Lognormal    | Default                                                     | 2          | $Median,UB$        |
| Log-t        | Lognormal $\in n \leq 30$                                  | 3          |                      |
| Triangular   | Expert opinion<br />Finite $\min,\max$<br />Possible skew | 3          | $LB,Mo,UB$         |
| PERT         | Between Triangular and Beta                                 | 3          | $LB,Mo,UB$         |
| Beta         | $\min,\max$ region > $Mo$                               | 4          | $\min,LB,UB,\max$ |
| Normal       | Equal chance$LB,UB$                                       | 2          | $\mu,Median,Mo,UB$ |
| t            | Normal $\in n\leq30$                                       | 3          | $LB,UB$            |
| Uniform      |                                                             | 2          |                      |

#### Subjective

#### Definition

**Subjective uncertainty** is an assessment of the uncertainty based on expert judgment.

#### Conditions

* Applies where objective uncertainty distributions are not available
* Distributions are characterized by parameters describing their
  * dispersion ($LB$, $UB$)
  * skewness
* Elicitation is subject to **Motivational** and **Cognitive** biases

##### Biases

| Category     | Bias                                                                                                                                                                                                                        |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Motivational | Social pressure (face-to-face)<br />Impression (not face-to)<br />Group Think<br />Wishful thinking<br />Career goals<br />Misunderstanding<br />Project Advocacy<br />Competitive Pressures                                |
| Cognitive    | Representativeness (small sample)<br />Availability (most recent)<br />Anchoring and Adjustment<br />Inconsistency (opinion changes over time)<br />Relating to irrelevant analogies<br />Underestimation<br />Human Nature |
| Other        | Confirmation Bias<br />Premature Termination<br />Inertia<br />Selective Perception<br />Optimism Bias<br />Recency<br />Repetition Bias<br />Escalating Commitment<br />Attribution Asymmetry                              |

##### Best Practices

* Have historical **$\min$**, **$\max$**, and **averages** on hand for discussion
* Ask for **$LB$** and **$UB$**
* Seek the **$Mo$** value
* Select a distribution shape based on **skew** and **firmness** of the bounds

##### Adjustment

Unless there is no evidence to do otherwise,

1. Treat subjective bounds (expert opinion) as 70\% range, and
2. Adjust for skew when using triangular, uniform, or PERT.

## Special Considerations

* Truncate distributions at zero unless there is evidence to do otherwise
* Sunk costs should not have uncertainty distributions associated with them

## PERT

### Assumptions

### Algorithm
1. For each task $i$:
    1. Define $LB,Mo,UB$
    2. Evaluate Task mean: $\mu = (LB+4Mo + UB)/6$
    3. Evaluate Task variance: $\sigma^2 = (UB-LB)/36$
        * $\pm 1\sigma \rightarrow 68.26\% $
        * $\pm 2\sigma \rightarrow 95.46\% $
        * $\pm 3\sigma \rightarrow 99.73\% $
2. For each path $j$:
    1. Evaluate Path mean: $\mu_j = \sum \mu_i$
    2. Evaluate Path variance: $\sigma^2_j = \sum \sigma^2_i$
    3. Evaluate Path standard deviation: $\sigma_j = \sqrt{\sigma^2_i}$
3. Determine $P(T <= x) = N^{-1}[()]$

## Monte Carlo

## Latin Hypercube Sampling