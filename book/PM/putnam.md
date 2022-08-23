# Putnam Model
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

\begin{figure}[H]
	\pgfplotstableread[col sep=comma]{profiles.dat}{\table}
	\centering
	\begin{tikzpicture}[-]
		\begin{groupplot}
			[
				group style={
					group size=1 by 2,
					x descriptions at=edge bottom,
					vertical sep=70pt
				}
			]
			\nextgroupplot[
				title ={Work},
				xlabel = {Time},
				xtick style={draw=none},
				ytick style={draw=none},
				xmin = 1,
				xmax = 28,
				ymin = 0,
				ymax = 1,
				width = .95\textwidth,
				height = .3\textwidth,
				enlargelimits=false,
				legend cell align = {left},
				legend pos = south east,
				smooth
			]
			\addplot[thick, black!100] table [x = {0}, y = {WP_L}] {\table};
			\addplot[thick, black!80, dashed] table [x = {0}, y = {WP_Xp}] {\table};
			\addplot[thick, black!60, dash pattern={on 7pt off 2pt on 1pt off 3pt}] table [x = {0}, y = {WP_Xm}] {\table};
			\addplot[thick, black!40, double] table [x = {0}, y = {WP_S}] {\table};
			\legend{
			    $WP^{\textrm{l}}_t$,
			    $WP^{\textrm{k}^+}_t$,
			    $WP^{\textrm{k}^-}_t$,
			    $WP^{\textrm{s}}_t$,
			}

			\nextgroupplot[
				title ={Work Rate},
				xlabel = {Time},
				xtick style={draw=none},
				ytick style={draw=none},
				xmin = 1,
				xmax = 28,
				ymin = 0,
				xtick = {1, 28},
				xticklabels = {1, PD},
				width = .95\textwidth,
				height = .3\textwidth,
				enlargelimits=false,
				legend cell align = {left},
				legend pos = north east,
				smooth
			]
			\addplot[thick, black!100] table [x = {0}, y = {dWP_L}] {\table};
			\addplot[thick, black!80, dashed] table [x = {0}, y = {dWP_Xp}] {\table};
			\addplot[thick, black!60, dash pattern={on 7pt off 2pt on 1pt off 3pt}] table [x = {0}, y = {dWP_Xm}] {\table};
			\addplot[thick, black!40, double] table [x = {0}, y = {dWP_S}] {\table};
			\legend{
			    $dWP^{\textrm{l}}_t$,
			    $dWP^{\textrm{k}^+}_t$,
			    $dWP^{\textrm{k}^-}_t$,
			    $dWP^{\textrm{s}}_t$,
			}
		\end{groupplot}	
		
	\end{tikzpicture}
	\caption{Project profiles}
	\label{fig:PP}
\end{figure}

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