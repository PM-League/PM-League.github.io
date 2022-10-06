# Modified PERT Bistribution

$$
PERT(min,Mo,max) = Beta(\alpha,\beta)\cdot(max-min)+ min = \frac{(x-min)^{\alpha-1}(max-x)^{\beta-1}}{B(\alpha,\beta)(max-min)^{\alpha+\beta-1}}
$$

where
|Term|Definition|
|-|-|
|$min$|Lower bound|
|$Mo$|Mode|
|$max$|Upper bound|
|$\alpha$|first shape parameter|
|$\beta$|second shape parameter|
|$B$|Beta function|

The $B$ function is defined as follows:

$$
B(\alpha,\beta) = \int_{0}^{1} u^{\alpha-1}\left(1-u\right)^{\beta-1}\textrm{d}u =  \frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha+\beta)}
$$

|Term|Definition|
|-|-|
|$\Gamma$|Gamma distribution|

The shape parameters, $\alpha$ and $\beta$, are obtained as follows:

$$
\alpha = \frac{\gamma Mo + max-(\gamma+1)min}{max-min}=1+\gamma \frac{Mo-min}{max-min}
$$

$$
\beta = \frac{(\gamma+1)max-min-\gamma Mo}{max-min}=1+\gamma \frac{max-Mo}{max-min}
$$

so that

$$
\mu = \frac{min+\gamma Mo+max}{\gamma+2}
$$

and 

$$
\sigma = \frac{(\mu-min)(max-\mu}{\gamma+3}
$$

