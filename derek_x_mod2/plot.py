import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from collections import OrderedDict




### DEFAULTS FROM bayes_plot.py
fontsize = dict(
    large=11,
    normal=10,
    small=9,
    tiny=8,
)

qm_font_large = 11
qm_font_small = 9

cb,co,cg,cr = plt.cm.Blues(.6), \
    plt.cm.Oranges(.6), plt.cm.Greens(.6), plt.cm.Reds(.6)
offblack = '#262626'
gray = '0.8'

# new tableau colors
# https://www.tableau.com/about/blog/2016/7/colors-upgrade-tableau-10-56782
colors = OrderedDict([
    ('blue', '#4e79a7'),
    ('orange', '#f28e2b'),
    ('green', '#59a14f'),
    ('red', '#e15759'),
    ('cyan', '#76b7b2'),
    ('purple', '#b07aa1'),
    ('brown', '#9c755f'),
    ('yellow', '#edc948'),
    ('pink', '#ff9da7'),
    ('gray', '#bab0ac')
])

offblack = '.15'

plt.rcdefaults()
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Lato'],
    'mathtext.fontset': 'custom',
    'mathtext.default': 'it',
    'mathtext.rm': 'sans',
    'mathtext.it': 'sans:italic:medium',
    'mathtext.cal': 'sans',
    'font.size': fontsize['normal'],
    'legend.fontsize': fontsize['normal'],
    'axes.labelsize': fontsize['normal'],
    'axes.titlesize': fontsize['large'],
    'xtick.labelsize': fontsize['small'],
    'ytick.labelsize': fontsize['small'],
    #'font.weight': 400,
    'axes.labelweight': 400,
    'axes.titleweight': 400,
    'axes.prop_cycle': plt.cycler('color', list(colors.values())),
    'lines.linewidth': .8,
    'lines.markersize': 3,
    'lines.markeredgewidth': 0,
    'patch.linewidth': .8,
    'axes.linewidth': .6,
    'xtick.major.width': .6,
    'ytick.major.width': .6,
    'xtick.minor.width': .4,
    'ytick.minor.width': .4,
    'xtick.major.size': 3.,
    'ytick.major.size': 3.,
    'xtick.minor.size': 2.,
    'ytick.minor.size': 2.,
    'xtick.major.pad': 3.5,
    'ytick.major.pad': 3.5,
    'axes.labelpad': 4.,
    'axes.formatter.limits': (-5, 5),
    #'axes.spines.top': False,
    #'axes.spines.right': False,
    'text.color': offblack,
    'axes.edgecolor': offblack,
    'axes.labelcolor': offblack,
    'xtick.color': offblack,
    'ytick.color': offblack,
    'legend.frameon': False,
    'image.cmap': 'Blues',
    'image.interpolation': 'none',
})






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
fig.align_ylabels()

plt.tight_layout(True)
plt.subplots_adjust(wspace=0.3, hspace=0.0)
plt.savefig("fig3.png", dpi=400)
plt.savefig("fig3.pdf", dpi=400)
plt.show()
