import matplotlib.pyplot as plt
import cosima_cookbook as cc

def wind_stress(expts=[]):
    """
    Plot zonally averaged wind stress.
    """

    plt.figure(figsize=(12,6))

    for expt in expts:
        mean_tau_x = cc.diagnostics.mean_tau_x(expt)
        plt.plot(mean_tau_x, mean_tau_x.yu_ocean,
             linewidth=2,
             label=expt)

    plt.ylim([-70, 65])
    plt.xlim([-0.08, 0.20])
    plt.ylabel('Latitude ($^\circ$N)')
    plt.xlabel('Stress (N m$^{-2}$)')
    plt.legend(loc='upper right',fontsize=10)

def annual_scalar(expts=[], variable='', ax=None):

    print("Calculating...", end='')

    if not isinstance(expts, list):
        expts = [expts]

    for expt in expts:
        annual_average = cc.diagnostics.annual_scalar(expt, variable)
        annual_average.plot(label=expt, ax=ax)

    if ax is None:
        ax = plt.gca()

    ax.set_title(annual_average.long_name)
    ax.set_ylabel(annual_average.name + ' ({})'.format(annual_average.units))
    ax.legend()
    print('done.')

def drake_passage(expts=[]):
    """
    Plot Drake Passage transport.
    """
    print("Calculating...", end='')

    plt.figure(figsize=(12,6))

    for expt in expts:
        transport = cc.diagnostics.drake_passage(expt)
        transport.plot(label=expt)

    plt.title('Drake Passage Transport')
    plt.xlabel('Time')
    plt.ylabel('Transport (Sv)')
    plt.legend(fontsize=10)
    print('done.')
