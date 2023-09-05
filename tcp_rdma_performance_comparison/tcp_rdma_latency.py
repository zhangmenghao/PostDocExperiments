#!/usr/bin/env python
# coding=utf-8

import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

# plot config
sys.path.append("..")
import plot_config

# plotting
plt.figure(figsize=plot_config.multi_fig_size)

# ymajorLocator   = MultipleLocator(50)
# ymajorFormatter = FormatStrFormatter('%1d')
# yminorLocator   = MultipleLocator(25)

ax = plt.subplot(111)

# ax.yaxis.set_major_locator(ymajorLocator)
# ax.yaxis.set_major_formatter(ymajorFormatter)
# ax.yaxis.set_minor_locator(yminorLocator)

ax.yaxis.grid(True, which='major', ls='dotted')

# plt.ylim(0, 450)
# plt.xlim(0, 16)

# plt.plot(imap_xcdf, imap_ycdf, '-', label="IMap")
# plt.plot(zmap_xcdf, zmap_ycdf, '-', label="ZMap")
x = np.array(['TCP', 'RDMA Write', 'RDMA Read', 'RDMA Send'])
y = np.array([50, 2.22, 4.32, 2.24])
plt.bar(x, y)
plt.xticks(rotation=15)

# plt.legend(loc='upper right', fontsize=plot_config.font_size, shadow=False)

for label in ax.xaxis.get_ticklabels():
    label.set_fontsize(plot_config.font_size)
for label in ax.yaxis.get_ticklabels():
    label.set_fontsize(plot_config.font_size)

# plt.xlabel('t (s)', fontsize=plot_config.font_size)
plt.ylabel('Time to transfer 2B (us)', fontsize=plot_config.font_size)

plt.tight_layout(rect=[0, 0, 1, 1])
plt.subplots_adjust(wspace=0, hspace=0.05)
plt.savefig('tcp_rdma_latency.pdf')
plt.savefig('tcp_rdma_latency.png')
# plt.show()