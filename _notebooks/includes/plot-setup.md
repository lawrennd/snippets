\ifndef{plotSetup}
\define{plotSetup}

\editme

\setupplotcode{import matplotlib.pyplot as plt
import shutil

if shutil.which('latex') is None:
    plt.rcParams['text.usetex'] = False
else:
    plt.rcParams['text.usetex'] = True
    plt.rcParams['text.latex.preamble']=r'\usepackage{amsmath}'

plt.rcParams.update({'font.size': 22})}

<!--setupplotcode{import seaborn as sns
sns.set_style('darkgrid')
sns.set_context('paper')
sns.set_palette('colorblind')}-->

\endif
