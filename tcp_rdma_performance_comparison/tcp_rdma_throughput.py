#!/usr/bin/env python3
# coding=utf-8

import sys
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

# plot config
sys.path.append("..")
import plot_config

# plotting
plt.figure(figsize=plot_config.multi_fig_size)

xmajorLocator   = MultipleLocator(10)
xmajorFormatter = FormatStrFormatter('%1d')
xminorLocator   = MultipleLocator(5)

ymajorLocator   = MultipleLocator(20)
ymajorFormatter = FormatStrFormatter('%1d')
yminorLocator   = MultipleLocator(10)

ax = plt.subplot(111)

ax.xaxis.set_major_locator(xmajorLocator)
ax.xaxis.set_major_formatter(xmajorFormatter)

ax.yaxis.set_major_locator(ymajorLocator)
ax.yaxis.set_major_formatter(ymajorFormatter)

ax.xaxis.set_minor_locator(xminorLocator)
ax.yaxis.set_minor_locator(yminorLocator)

ax.xaxis.grid(True, which='major', ls='dotted')
ax.yaxis.grid(True, which='major', ls='dotted')

plt.ylim(0, 100)
plt.xlim(128, 65536*2)

x_loc = [256, 1024, 4096, 16384, 65536]
x_value = ["256", "1K", "4K", "16K", "64K"]

y_tcp = [16.5, 16.6, 16.9, 16.9, 17.4]
y_rdma = [13.8, 50.85, 91.97, 92.44, 92.55]

plt.plot(x_loc, y_tcp, marker='o', label="TCP")
plt.plot(x_loc, y_rdma, marker='o', label="RDMA")
plt.xscale('log', base=2)
plt.xticks(x_loc, x_value)

plt.legend(loc='upper left', fontsize=plot_config.font_size, shadow=False)

for label in ax.xaxis.get_ticklabels():
    label.set_fontsize(plot_config.font_size)
for label in ax.yaxis.get_ticklabels():
    label.set_fontsize(plot_config.font_size)

plt.xlabel('Message Size', fontsize=plot_config.font_size)
plt.ylabel('Throughput (Gbps)', fontsize=plot_config.font_size)

plt.tight_layout(rect=[0, 0, 1, 1])
plt.subplots_adjust(wspace=0, hspace=0.05)
plt.savefig('tcp_rdma_throughput.pdf')
plt.savefig('tcp_rdma_throughput.png')
# plt.show()