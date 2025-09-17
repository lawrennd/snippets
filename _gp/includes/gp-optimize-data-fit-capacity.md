\ifndef{gpOptimizeDataFitCapacity}
\define{gpOptimizeDataFitCapacity}

\editme

\subsection{Data Fit Term}

\setupplotcode{import mlai.plot as plot
import mlai
from mlai import gp_tutorial
import os}

\plotcode{np.random.seed(125)
diagrams = '\writeDiagramsDir/gp'

black_color=[0., 0., 0.]
red_color=[1., 0., 0.]
blue_color=[0., 0., 1.]
magenta_color=[1., 0., 1.]
fontsize=18}

\plotcode{y_lim = [-2.2, 2.2]
y_ticks = [-2, -1, 0, 1, 2]
x_lim = [-2, 2]
x_ticks = [-2, -1, 0, 1, 2]
err_y_lim = [-12, 20]

linewidth=3
markersize=15
markertype='.'}

\code{x = np.linspace(-1, 1, 6)[:, np.newaxis]
xtest = np.linspace(x_lim[0], x_lim[1], 200)[:, np.newaxis]

# True data
true_kernel = Kernel(eq_cov, name='Exponentiated Quadratic', shortname='eq', lengthscale=1)
K = true_kernel.K(x) + np.eye(6)*0.01 
y = np.random.multivariate_normal(np.zeros((6,)), K, 1).T}

\code{
# Fitted model
kernel = Kernel(eq_cov, name='Exponentiated Quadratic', shortname='eq', lengthscale=1)
gp = GP(x, y, sigma2=0.01, kernel=kernel)}

\plotcode{
lengthscales = np.asarray([0.01, 0.05, 0.1, 0.25, 0.5, 1, 2, 4, 8, 16, 100])

fig, ax = plt.subplots(1, 2, figsize=plot.big_wide_figsize)    
plt.subplots_adjust(wspace=0.3)
plt.tight_layout()
line = ax[1].semilogx(np.nan, np.nan, 'x-', 
                    color=black_color)
ax[1].set_ylim(err_y_lim)
ax[1].set_xlim([0.01, 100])
ax[1].grid(True)
ax[1].set_xticks([0.01, 0.1, 1, 10, 100])
ax[1].set_xticklabels(['$10^{-2}$', '$10^{-1}$', '$10^0$', '$10^1$', '$10^2$'])


err = np.zeros_like(lengthscales)
err_log_det = np.zeros_like(lengthscales)
err_fit = np.zeros_like(lengthscales)

counter = 0
for i, ls in enumerate(lengthscales):
    gp.kernel.parameters["lengthscale"] = ls
    gp.update_kernel_matrix() 
    err[i] = 0.5*(gp.logdetK + y.T@gp.Kinv@y)
    err_log_det[i] = 0.5*gp.logdetK
    err_fit[i] = 0.5*y.T@gp.Kinv@y
    ypred_mean, ypred_var = gp.predict(xtest)
    ypred_sd = np.sqrt(ypred_var)
    ax[0].clear()
    _ = gp_tutorial.gpplot(xtest.flatten(),
                           ypred_mean.flatten(),
                           ypred_mean.flatten()-2*ypred_sd.flatten(),
                           ypred_mean.flatten()+2*ypred_sd.flatten(), 
                           ax=ax[0])
    x_lim = ax[0].get_xlim()
    ax[0].set_ylabel('$f(x)$', fontsize=fontsize)
    ax[0].set_xlabel('$x$', fontsize=fontsize)

    p = ax[0].plot(x, y, markertype, color=black_color, markersize=markersize, linewidth=linewidth)
    ax[0].set_ylim(y_lim)
    ax[0].set_xlim(x_lim)                                    
    ax[0].set_xticks(x_ticks)
        #ax.set(box=False)
           
    ax[0].plot([x_lim[0], x_lim[0]], y_lim, color=black_color)
    ax[0].plot(x_lim, [y_lim[0], y_lim[0]], color=black_color)


    ax[1].clear()
    t = ax[1].semilogx(lengthscales[0:i+1], err[0:i+1], 'x-', 
                     color=magenta_color, 
                     markersize=markersize,
                     linewidth=linewidth)
    t2 = ax[1].semilogx(lengthscales[0:i+1], err_log_det[0:i+1], 'x-', 
                      color=blue_color, 
                      markersize=markersize,
                      linewidth=linewidth)
    t3 = ax[1].semilogx(lengthscales[0:i+1], err_fit[0:i+1], 'x-', 
                      color=red_color, 
                      markersize=markersize,
                      linewidth=linewidth)
    ax[1].set_ylim(err_y_lim)
    ax[1].set_xlim([0.025, 32])
    ax[1].set_xticks([0.01, 0.1, 1, 10, 100])
    ax[1].set_xticklabels(['$10^{-2}$', '$10^{-1}$', '$10^0$', '$10^1$', '$10^2$'])

    ax[1].grid(True)

    ax[1].set_ylabel('negative log likelihood', fontsize=fontsize)
    ax[1].set_xlabel('length scale, $\ell$', fontsize=fontsize)
	xlim = ax[1].get_xlim()
    ax[1].plot([xlim[0], xlim[0]], err_y_lim, color=black_color)
    ax[1].plot(xlim, [err_y_lim[0], err_y_lim[0]], color=black_color)
	
    file_name = 'gp-optimise{counter:0>3}.svg'.format(counter=counter)
    mlai.write_figure(os.path.join(diagrams, file_name),
                      figure=fig,
                      transparent=True)
    counter += 1}


\setupdisplaycode{import notutils as nu
from ipywidgets import IntSlider}
\displaycode{nu.display_plots('gp-optimise{sample:0>3}.svg', 
                                          directory='\writeDiagramsDir/gp', 
			                  sample=IntSlider(0, 0, 10, 1))}

\slides{
\startanimation{gp-optimise}{0}{10}
\newframe{\columns{\includediagram{\diagramsDir/gp/gp-optimise000}}{\includediagram{\diagramsDir/gp/gp-optimise001}}{50%}{50%}}{gp-optimise}
\newframe{\columns{\includediagram{\diagramsDir/gp/gp-optimise002}}{\includediagram{\diagramsDir/gp/gp-optimise003}}{50%}{50%}}{gp-optimise}
\newframe{\columns{\includediagram{\diagramsDir/gp/gp-optimise004}}{\includediagram{\diagramsDir/gp/gp-optimise005}}{50%}{50%}}{gp-optimise}
\newframe{\columns{\includediagram{\diagramsDir/gp/gp-optimise006}}{\includediagram{\diagramsDir/gp/gp-optimise007}}{50%}{50%}}{gp-optimise}
\newframe{\columns{\includediagram{\diagramsDir/gp/gp-optimise008}}{\includediagram{\diagramsDir/gp/gp-optimise009}}{50%}{50%}}{gp-optimise}
\newframe{\columns{\includediagram{\diagramsDir/gp/gp-optimise010}}{\includediagram{\diagramsDir/gp/gp-optimise011}}{50%}{50%}}{gp-optimise}
\newframe{\columns{\includediagram{\diagramsDir/gp/gp-optimise012}}{\includediagram{\diagramsDir/gp/gp-optimise013}}{50%}{50%}}{gp-optimise}
\newframe{\columns{\includediagram{\diagramsDir/gp/gp-optimise014}}{\includediagram{\diagramsDir/gp/gp-optimise015}}{50%}{50%}}{gp-optimise}
\newframe{\columns{\includediagram{\diagramsDir/gp/gp-optimise016}}{\includediagram{\diagramsDir/gp/gp-optimise017}}{50%}{50%}}{gp-optimise}
\newframe{\columns{\includediagram{\diagramsDir/gp/gp-optimise018}}{\includediagram{\diagramsDir/gp/gp-optimise019}}{50%}{50%}}{gp-optimise}
\newframe{\columns{\includediagram{\diagramsDir/gp/gp-optimise020}}{\includediagram{\diagramsDir/gp/gp-optimise021}}{50%}{50%}}{gp-optimise}
\endanimation
}

\notes{\figure{\columns{\includediagram{\diagramsDir/gp/gp-optimise006}{100%}}{\includediagram{\diagramsDir/gp/gp-optimise010}{100%}}{50%}{50%}
\columns{\includediagram{\diagramsDir/gp/gp-optimise016}{100%}}{\includediagram{\diagramsDir/gp/gp-optimise021}{100%}}{50%}{50%}}{Variation in the data fit term, the capacity term and the negative log likelihood for different lengthscales.}{gp-optimise}}

\endif
