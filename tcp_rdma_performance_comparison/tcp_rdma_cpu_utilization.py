#!/usr/bin/env python3
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

xmajorLocator   = MultipleLocator(10)
xmajorFormatter = FormatStrFormatter('%1d')
xminorLocator   = MultipleLocator(5)

ymajorLocator   = MultipleLocator(1)
ymajorFormatter = FormatStrFormatter('%.1f')
yminorLocator   = MultipleLocator(0.5)

ax = plt.subplot(111)

ax.xaxis.set_major_locator(xmajorLocator)
ax.xaxis.set_major_formatter(xmajorFormatter)

ax.yaxis.set_major_locator(ymajorLocator)
ax.yaxis.set_major_formatter(ymajorFormatter)

ax.xaxis.set_minor_locator(xminorLocator)
ax.yaxis.set_minor_locator(yminorLocator)

ax.xaxis.grid(True, which='major', ls='dotted')
ax.yaxis.grid(True, which='major', ls='dotted')

plt.ylim(0, 10)
# plt.xlim(128, 65536*2)

x_loc = [256, 1024, 4096, 16384, 65536, 65536*4, 65536*16, 65536*64, 65536*256]
x_value = ["256", "1K", "4K", "16K", "64K", "256K", "1M", "4M", "16M"]

y_tcp_c =  [  11, 11.5, 11.6,  11.5,  11.4,   11.6, 11.5, 11.5, 11.5]
y_tcp_s =  [ 703,  705,  710,   712,   713,    711,  712,  713, 714]
y_rdma_c =  [0.8, 0.82,  0.8,   0.8,   0.8,    0.8, 0.81, 0.82, 0.82]
y_rdma_s =  [  0,    0,    0,     0,     0,      0,    0,    0,    0]
y_tcp_c = np.divide(y_tcp_c, 128)
y_tcp_s = np.divide(y_tcp_s, 128)
y_rdma_c = np.divide(y_rdma_c, 128)
y_rdma_s = np.divide(y_rdma_s, 128)

plt.plot(x_loc, y_tcp_c, marker='o', label="TCP Client")
plt.plot(x_loc, y_tcp_s, marker='o', label="TCP Server")
plt.plot(x_loc, y_rdma_c, marker='o', label="RDMA Client")
plt.plot(x_loc, y_rdma_s, marker='o', label="RDMA Server")
plt.xscale('log', base=2)
plt.yscale('symlog', base=2)
plt.xticks(x_loc, x_value)

plt.legend(loc='upper left', fontsize=plot_config.font_size, shadow=False)

for label in ax.xaxis.get_ticklabels():
    label.set_fontsize(plot_config.font_size)
for label in ax.yaxis.get_ticklabels():
    label.set_fontsize(plot_config.font_size)

plt.xlabel('Message Size (Byte)', fontsize=plot_config.font_size)
plt.ylabel('CPU Utilization (%)', fontsize=plot_config.font_size)

plt.tight_layout(rect=[0, 0, 1, 1])
plt.subplots_adjust(wspace=0, hspace=0.05)
plt.savefig('tcp_rdma_cpu_utilization.pdf')
plt.savefig('tcp_rdma_cpu_utilization.png')
# plt.show()