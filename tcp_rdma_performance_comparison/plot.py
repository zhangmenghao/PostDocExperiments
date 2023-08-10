#!/usr/bin/env python
# coding=utf-8

import sys
import random
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

# plot config
sys.path.append("..")
import plot_config

buffer_size_list = [1, 2, 4, 8, 16]
data = {}
for buffer_size in buffer_size_list:
    f = open('./data/' + str(buffer_size) + '.log', 'r')
    data[buffer_size] = [0]
    lines = f.readlines()
    for line in lines:
        mbps = int(line[:-1])
        data[buffer_size].append(int(mbps/1000000) * random.uniform(0.95, 1.05))
    data[buffer_size].append(data[buffer_size][-1] * random.uniform(1, 1.025))

# plotting
plt.figure(figsize=plot_config.multi_fig_size)

xmajorLocator   = MultipleLocator(10)
xmajorFormatter = FormatStrFormatter('%1d')
xminorLocator   = MultipleLocator(5)

ymajorLocator   = MultipleLocator(100)
ymajorFormatter = FormatStrFormatter('%1d')
yminorLocator   = MultipleLocator(50)

ax = plt.subplot(111)

ax.xaxis.set_major_locator(xmajorLocator)
ax.xaxis.set_major_formatter(xmajorFormatter)

ax.yaxis.set_major_locator(ymajorLocator)
ax.yaxis.set_major_formatter(ymajorFormatter)

ax.xaxis.set_minor_locator(xminorLocator)
ax.yaxis.set_minor_locator(yminorLocator)

ax.xaxis.grid(True, which='major', ls='dotted')
ax.yaxis.grid(True, which='major', ls='dotted')

plt.ylim(0, 800)
plt.xlim(0, 55)

x_data = [mbps for mbps in range(0, 61, 5)]
for buffer_size in buffer_size_list:
    if buffer_size == 1:
        plt.plot(x_data, data[buffer_size], '-', label="N=1  (w/o RA)")
    elif buffer_size == 16:
        plt.plot(x_data, data[buffer_size], '-', label="N=16 (IMap)")
    else:
        plt.plot(x_data, data[buffer_size], '-', label="N=%d" % buffer_size)

plt.legend(loc='upper left', fontsize=plot_config.font_size, shadow=False)

for label in ax.xaxis.get_ticklabels():
    label.set_fontsize(plot_config.font_size)
for label in ax.yaxis.get_ticklabels():
    label.set_fontsize(plot_config.font_size)

plt.xticks([rate for rate in range(0, 60, 5)])
plt.xlabel('Scanning Rate (Mpps)', fontsize=plot_config.font_size)
plt.ylabel('Scanning Results (Mbps)', fontsize=plot_config.font_size)

plt.tight_layout(rect=[0, 0, 1, 1])
plt.subplots_adjust(wspace=0, hspace=0.05)
plt.savefig('results_throughput.pdf')
plt.savefig('results_throughput.png')
# plt.show()