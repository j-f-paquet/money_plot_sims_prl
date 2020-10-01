import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


# Colormaps: Purples? Or summer?
#colors = mpl.cm.summer(np.linspace( 0.4, 1., 4 ) )

#height_ratios = [1., .3]
#fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(6,3.5),
#                sharex=False, sharey=False, constrained_layout=True) #, gridspec_kw={'height_ratios': height_ratios})

height_ratios = [1., .3]
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(6,2.5),
                sharex='col', sharey=False, constrained_layout=True, gridspec_kw={'height_ratios': height_ratios})

colors = mpl.cm.Oranges(np.linspace( 0.4, 1., 4 ) )

##########################
#BULK VISCOSITY
T_zetas=np.loadtxt("../calculations/T_zetas.dat")
prior_5pct_zetas=np.loadtxt("../calculations/prior_5pct_zetas.dat")
prior_95pct_zetas=np.loadtxt("../calculations/prior_95pct_zetas.dat")
posterior_5pct_zetas=np.loadtxt("../calculations/posterior_5pct_zetas.dat")
posterior_95pct_zetas=np.loadtxt("../calculations/posterior_95pct_zetas.dat")
info_gain_zetas=np.loadtxt("../calculations/info_gain_zetas.dat")

axes[0, 0].fill_between(T_zetas, prior_5pct_zetas,
                        prior_95pct_zetas,
                        color='gray', alpha=0.3, lw=2)

#axes[1, 0].fill_between(T_zetas, np.zeros_like(T_zetas), info_gain_zetas, color='black')
axes[1, 0].plot(T_zetas, info_gain_zetas, lw=4, color='black')
#nbins=20
#axes[1,0].hist(T_zetas,bins=nbins,weights=info_gain_zetas/(len(T_zetas)/nbins), color='black')
#axes[1, 0].set_ylabel(r'$KL(\zeta/s(T))$')
#axes[1, 0].text(0.345, .55, "Information gain",horizontalalignment='right')


axes[0, 0].fill_between(T_zetas, posterior_5pct_zetas,
                        posterior_95pct_zetas,
                        color=colors[0], lw=2)

##########################
#SHEAR VISCOSITY
T_etas=np.loadtxt("../calculations/T_etas.dat")
prior_5pct_etas=np.loadtxt("../calculations/prior_5pct_etas.dat")
prior_95pct_etas=np.loadtxt("../calculations/prior_95pct_etas.dat")
posterior_5pct_etas=np.loadtxt("../calculations/posterior_5pct_etas.dat")
posterior_95pct_etas=np.loadtxt("../calculations/posterior_95pct_etas.dat")
info_gain_etas=np.loadtxt("../calculations/info_gain_etas.dat")

axes[0, 1].fill_between(T_etas, prior_5pct_etas,
                        prior_95pct_etas,
                        color='gray', alpha=0.3, lw=2, label="90% CI Prior")

#axes[1, 1].fill_between(T_etas, np.zeros_like(T_etas), info_gain_etas, color='black')
axes[1, 1].plot(T_etas, info_gain_etas, lw=4, color='black')
#axes[1, 1].plot(T_etas, info_gain_etas, lw=2)
#nbins=20
#axes[1,1].hist(T_etas,bins=nbins,weights=info_gain_etas/(len(T_etas)/nbins), color='black')
#axes[1, 1].set_ylabel(r'$KL(\eta/s(T))$')
axes[1, 1].text(0.345, .4, "Prior"r"$\to$""Posterior\ninformation gain",horizontalalignment='right', fontsize=7)


axes[0, 1].fill_between(T_etas, posterior_5pct_etas,
                        posterior_95pct_etas,
                        color=colors[0], lw=2, label="90% CI Posterior")


handles, labels = axes[0,1].get_legend_handles_labels()
axes[0,1].legend(handles, labels, loc='upper left', frameon=False, fontsize=7)

#axes[0, 1].legend(fontsize=7, loc='upper center')

axes[0, 0].set_ylabel(r"$\zeta/s$")
axes[0, 1].set_ylabel(r"$\eta/s$")

axes[1, 0].set_ylabel(r"$D_{KL}$")
axes[1, 1].set_ylabel(r"$D_{KL}$")

axes[1, 0].set_xlabel(r"$T$ [GeV]")
axes[1, 1].set_xlabel(r"$T$ [GeV]")

axes[1, 0].set_xlim([0.135, 0.35])
axes[1, 1].set_xlim([0.135, 0.35])

axes[1, 0].set_ylim([0., 1.4])
axes[1, 1].set_ylim([0., 1.4])

T_ticks = [0.15, 0.2, 0.25, 0.3, 0.35]
axes[1, 0].set_xticks(T_ticks)
axes[1, 1].set_xticks(T_ticks)

plt.tight_layout(True)
plt.subplots_adjust(wspace=0.3, hspace=0.0)
plt.savefig("fig3.png")
plt.savefig("fig3.pdf")
plt.show()

