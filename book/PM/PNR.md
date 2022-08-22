# Putnam Resource Allocation Model
## The Norden-Rayleigh Curve
The curve is modeled by differential equation
\begin{equation}
m{(t)} = \frac{dy}{dt} = 2Kate^{-at^2}\end{equation}
where
|||
|-|-|
|$\frac{dy}{dt}$|manpower utilization rate per unit time|
|$a$|acceleration factor - curve sharpness parameter|
|$K$|total project effort in staff years - area underneath the curve in $\left[0,\infty\right]$|
|$t$|elapsed time|

Integrating $m{(t)}$ on $[0,\infty]$, we obtain
\begin{equation}y{(t)} = K\left[1-e^{-at^2}\right]\end{equation}

If 
\begin{equation}y(0) = 0\end{equation}
and
\begin{equation}y(\infty) = K\end{equation}
then
\begin{equation}\frac{d^2y}{dt^2} = 2Kae^{-at^2}\left[1-2at^2\right]=0\end{equation}
\begin{equation}t_d^2 = \frac{1}{2a}\end{equation}
where
$t_d$ is the time at which the maximum effort rate occurs.

Replacing $t_d$ in Eq.2 leads to
\begin{equation}E=y{(t)}=K\left(1-e^{\frac{t_d^2}{2t_d^2}}\right) = K\left(1-e^{-.5}\right)\end{equation}
\begin{equation}E=y(t)=.3935K\end{equation}
\begin{equation}a=\frac{1}{2t_d^2}\end{equation}

Replacing $a$ with $\frac{1}{2t_d^2}$ in the N/R model, we obtain
\begin{equation}m(t)=\frac{2K}{2t_d^2}te^{-\frac{t^2}{2t_d^2}} = \frac{K}{t_d^2}te^{-\frac{t^2}{2t_d^2}}\end{equation}

The peak manning is denoted by $m_0$ and is obtained
\begin{equation}m(t_d) = m_0 = \frac{K}{t_d \sqrt{e}}\end{equation}
where
|||
|-|-|
|$K$|total project cost/effort (person-years)|
|$t_d$|delivery time (years)|
|$m_0$|staffing level|

## Difficulty Metric
Slope of manpower distribution curve at $t=0$ has some useful properties.

\begin{equation}m'{(t)} = \frac{d^2y}{dt^2} = 2Kae^{-at^2}\left(1-2at^2\right)\end{equation}

For $t=0$, 
\begin{equation}m'{(0)} = 2Ka = \frac{2K}{2t_d^2} = \frac{K}{t_d^2}\end{equation}

The ratio 
\begin{equation}D = \frac{K}{t_d^2}\end{equation}
is called difficulty metric $D$ (person/year) 