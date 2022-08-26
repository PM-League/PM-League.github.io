---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Putnam Model
## The Norden-Rayleigh Curve
The curve is modeled by differential equation

$$
m{(t)} = \frac{dy}{dt} = 2Kate^{-at^2}
$$

<!-- ```{code-cell} ipython3
:tags: ["remove-input"]
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame()
df['t'] = np.arange(0,12+1)
df['dK(t)'] = [0, 12.9, 13.0, 23.0, 25.0, 25.0, 32.0, 36.7, 38.6, 39.3, 39.9, 40.5, 9.0]
df['K(t)'] = df['dK(t)'].cumsum()
fig, ax = plt.subplots(1, 1, figsize=(6, 2), dpi=100)
ax.scatter(df['t'], df['K(t)'])
ax.set_xlim(left=0)
ax.set_ylim(0, max(df['K(t)']))
ax.set_ylabel('$m(t)$')
ax.set_xlabel('$t$')
plt.show()
``` -->

where
|Term|Definition|
|-|-|
|$\frac{dy}{dt}$|manpower utilization rate per unit time|
|$a$|acceleration factor - curve sharpness parameter|
|$K$|total project effort in staff years - area underneath the curve in $\left[0,\infty\right]$|
|$t$|elapsed time|

Integrating $m{(t)}$ on $[0,\infty]$, we obtain

$$
y{(t)} = K\left[1-e^{-at^2}\right]
$$

If $y(0) = 0$ and $y(\infty) = K$, then

$$
\frac{d^2y}{dt^2} = 2Kae^{-at^2}\left[1-2at^2\right]=0
$$

$$
t_d^2 = \frac{1}{2a}
$$

where $t_d$ is the time at which the maximum effort rate occurs.

Replacing $t_d$ leads to

$$
E=y{(t)}=K\left(1-e^{\frac{t_d^2}{2t_d^2}}\right) = K\left(1-e^{-.5}\right)
$$

$$
E=y(t)=.3935K
$$

$$
a=\frac{1}{2t_d^2}
$$

Replacing $a$ with $\frac{1}{2t_d^2}$ in the N/R model, we obtain

$$
m(t)=\frac{2K}{2t_d^2}te^{-\frac{t^2}{2t_d^2}} = \frac{K}{t_d^2}te^{-\frac{t^2}{2t_d^2}}
$$

The peak manning is denoted by $m_0$ and is obtained

$$
m(t_d) = m_0 = \frac{K}{t_d \sqrt{e}}
$$

where
|Term|Definition|
|-|-|
|$K$|total project cost/effort (person-years)|
|$t_d$|delivery time (years)|
|$m_0$|staffing level|

## Difficulty Metric
Slope of manpower distribution curve at $t=0$ has some useful properties.

$$
m'{(t)} = \frac{d^2y}{dt^2} = 2Kae^{-at^2}\left(1-2at^2\right)
$$

For $t=0$, 

$$
m'{(0)} = 2Ka = \frac{2K}{2t_d^2} = \frac{K}{t_d^2}
$$

The ratio 

$$
D = \frac{K}{t_d^2}
$$

is called difficulty metric $D$ (person/year) 

## The Software Equation
The average productivity

$$
\overline{PR} = \frac{\text{total end product code}}{\text{total effort to produce code}}
$$

The general size of the product in source statements is

$$
S_s = C_k K^{1/3} t_d^{4/3}
$$

where $C_k$ is a measure of the state of technology of the human-machine system.

This is a reasonable relation linking the output ($S_s$) to the input ($K$, $t_d$ - management parameters) and a constant ($C_k$) which is somehow a measure of the state of technology being applied to the project. \
Adding people to accelerate a project can accomplish this until the gradient condition is reached, but only at a very high cost.

### The Effort-Time Tradeoff Law
The tradeoff law between effort and time can be obtained
explicity from the software equation

$$
S_s = C_k K^{1/3} t_d^{4/3}
$$

A constant number of source statements ($S_s = \text{const}$) implies $K t_d^4 = \text{const}$. \
So, $K = \text{constant}/t_d^4$, or proportionally, development effort = constat/$t_d^4$, is the effort-development tradeoff law.

### Effect of Constant Productivity
One other relation is worth obtaining; the one where the
average productivity remains constant.

$$
\overline{PR} = C_n D^{-2/3}
$$

implies that

$$
D = \text{const}
$$

So the productivity for different projects will be the same
only if the difficulty is the same. \
This does not seem reasonable to expect very frequently since the difficulty is a measure of the software work to be done, i.e., $K/t_d^2 = D$  which is a function of the number of files, the number of reports, and the number of programs the system has. \
Thus, planning a new project based on using the same productivity a previous project had, is fallacious unless the difficulty is the same.