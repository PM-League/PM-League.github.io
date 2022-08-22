# Putnam Resource Allocation Model
## The Norden-Rayleigh Curve
The curve is modeled by differential equation
$$m{(t)} = \frac{dy}{dt} = 2kate^{-at^2}$$
where
|||
|-|-|
|$\frac{dy}{dt}$|manpower utilization rate per unit time|
|$a$|acceleration factor - curve sharpness parameter|
|$K$|total project effort in staff years - area underneath the curve in $\left[0,\infty\right]$|
|$t$|elapsed time|

Integrating $m{(t)}$ on $[0,\infty]$, we obtain
$$y{(t)} = K\left[1-e^{-at^2}\right]$$

If 
$$y(0) = 0$$
and
$$y(\infty) = K$$
then
$$\frac{d^2y}{dt^2} = 2kae^{-at^2}\left[1-2at^2\right]=0$$
$$t_d^2 = \frac{1}{2a}$$
where
$t_d$ is the time at which the maximum effort rate occurs.

Replacing $t_d$ in Eq.2 leads to
$$E=y{(t)}=k\left(1-e^{\frac{t_d^2}{2t_d^2}}\right) = K\left(1-e^{-.5}\right)$$
$$E=y(t)=.3935k$$
$$a=\frac{1}{2t_d^2}$$

Replacing $a$ with $\frac{1}{2t_d^2}$ in the N/R model, we obtain
$$m(t)=\frac{2K}{2t_d^2}te^{-\frac{t^2}{2t_d^2}} = \frac{K}{t_d^2}te^{-\frac{t^2}{2t_d^2}}$$

The peak manning is denoted by $m_0$ and is obtained
$$m(t_d) = m_0 = \frac{K}{t_d \sqrt{e}}$$
where
|||
|-|-|
|$K$|total project cost/effort (person-years)|
|$t_d$|delivery time (years)|
|$m_0$|staffing level|

## Difficulty Metric
Slope of manpower distribution curve at $t=0$ has some useful properties.

$$m'{(t)} = \frac{d^2y}{dt^2} = 2kae^{-at^2}\left(1-2at^2\right)$$

For $t=0$, 
$$m'{(0)} = 2Ka = \frac{2K}{2t_d^2} = \frac{K}{t_d^2}$$

The ratio 
$$D = \frac{K}{t_d^2}$$
is called difficulty metric $D$ (person/year) 