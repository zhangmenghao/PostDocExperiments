#!/usr/bin/env python
# coding=utf-8

import numpy as np
from cycler import cycler
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import matplotlib.patches as mpatches
import brewer2mpl

single_fig_size = [10, 5]
multi_fig_size = [10, 7.5]
font_size = 30
# font_size = 'xx-large'
# colors = brewer2mpl.get_map('Set1', 'qualitative', 9).mpl_colors
colors = [
    (74 / 255.0, 114 / 255.0, 176 / 255.0),
    (196 / 255.0, 78 / 255.0, 82 / 255.0),
    (85 / 255.0, 168 / 255.0, 104 / 255.0),
    (129 / 255.0, 114 / 255.0, 178 / 255.0),
    (204 / 255.0, 185 / 255.0, 116 / 255.0),
    (100 / 255.0, 181 / 255.0, 205 / 255.0),
    (247 / 255.0, 129 / 255.0, 191 / 255.0),
    (255 / 255.0, 217 / 255.0, 47 / 255.0),
    (251 / 255.0, 128 / 255.0, 114 / 255.0),
    (179 / 255.0, 222 / 255.0, 105 / 255.0),
]
plt.rc('axes', prop_cycle=(cycler('color', colors)))
plt.rc('lines', linewidth=5)

mpl.rcParams['pdf.fonttype'] = 42
mpl.rcParams['ps.fonttype'] = 42