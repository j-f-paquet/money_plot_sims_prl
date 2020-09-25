import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


# Colormaps: Purples? Or summer?
#colors = mpl.cm.summer(np.linspace( 0.4, 1., 4 ) )

#height_ratios = [1., .3]
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(6,3.5),
                sharex=False, sharey=False, constrained_layout=True) #, gridspec_kw={'height_ratios': height_ratios})


##########################
#BULK VISCOSITY
T_zetas=np.loadtxt("T_zetas.dat")
prior_5pct_zetas=np.loadtxt("prior_5pct_zetas.dat")
prior_95pct_zetas=np.loadtxt("prior_95pct_zetas.dat")
posterior_5pct_zetas=np.loadtxt("posterior_5pct_zetas.dat")
posterior_95pct_zetas=np.loadtxt("posterior_95pct_zetas.dat")
info_gain_zetas=np.loadtxt("info_gain_zetas.dat")

num=len(T_zetas)

#Map [0,1] to [0.5,1]
colors = mpl.cm.Purples(info_gain_zetas/2.+0.5)

axes[0].fill_between(T_zetas, prior_5pct_zetas,
                prior_95pct_zetas,
                color='gray', alpha=0.3, lw=2)

for i in range(num):

    axes[0].fill_between(T_zetas[i:i+1], posterior_5pct_zetas[i:i+1],
                        posterior_95pct_zetas[i:i+1],
                        color=colors[i], lw=2)

##########################
#SHEAR VISCOSITY
T_etas=np.loadtxt("T_etas.dat")
prior_5pct_etas=np.loadtxt("prior_5pct_etas.dat")
prior_95pct_etas=np.loadtxt("prior_95pct_etas.dat")
posterior_5pct_etas=np.loadtxt("posterior_5pct_etas.dat")
posterior_95pct_etas=np.loadtxt("posterior_95pct_etas.dat")
info_gain_etas=np.loadtxt("info_gain_etas.dat")

#Map [0,1] to [0.5,1]
colors = mpl.cm.Purples(info_gain_etas/2.+0.5)

axes[1].fill_between(T_etas, prior_5pct_etas,
                prior_95pct_etas,
                color='gray', alpha=0.3, lw=2)

for i in range(num):

    axes[1].fill_between(T_etas[i:i+1], posterior_5pct_etas[i:i+1],
                        posterior_95pct_etas[i:i+1],
                        color=colors[i], lw=2)


axes[1].legend(fontsize=7, loc='upper center')

axes[0].set_ylabel(r"$\zeta/s$")
axes[1].set_ylabel(r"$\eta/s$")

axes[0].set_xlabel(r"$T$ [GeV]")
axes[1].set_xlabel(r"$T$ [GeV]")

axes[0].set_xlim([0.135, 0.35])
axes[1].set_xlim([0.135, 0.35])

T_ticks = [0.15, 0.2, 0.25, 0.3, 0.35]
axes[0].set_xticks(T_ticks)
axes[1].set_xticks(T_ticks)

#cax = fig.add_axes([0.95, 0.2, 0.02, 0.6])
#cb = mpl.colorbar.ColorbarBase(cax, cmap=mpl.cm.Purples, spacing='proportional')
#test=mpl.cm.ScalarMappable(norm=1,cmap=mpl.cm.Purples)
#plt.colorbar(test)
#cb=plt.colorbar(mpl.cm.ScalarMappable(cmap=mpl.cm.Purples)) #cmap=mpl.cm.Purples)
#cb.set_label('Information gain')

plt.tight_layout(True)
plt.subplots_adjust(wspace=0.3, hspace=0.1)
plt.savefig("fig3.png")
plt.savefig("fig3.pdf")
plt.show()

