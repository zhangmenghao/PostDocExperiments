#!/usr/bin/env python
# coding=utf-8

import sys
import os
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

# plot config
sys.path.append("..")
import plot_config

def extract_data(data_path):
    data_list = []
    for log_name in os.listdir(data_path):
        log_path = data_path + "/" + log_name
        for data in open(log_path).readlines():
            data_list.append(int(data.split()[0]) / 1000.0)
    data_list.sort()
    return data_list

# There are get_percentile(data_list, target_data) values in
# data_list not larger than target_data
def get_percentile(data_list, target_data):
    for idx in range(len(data_list)):
        if target_data < data_list[idx]:
            return idx / len(data_list)
    return 1.0

imap_data = extract_data("data/imap")
zmap_data = extract_data("data/zmap")

# print(get_percentile(imap_data, 600))
# print(get_percentile(zmap_data, 600))

# plotting
plt.figure(figsize=plot_config.multi_fig_size)

ymajorLocator   = MultipleLocator(50)
ymajorFormatter = FormatStrFormatter('%1d')
yminorLocator   = MultipleLocator(25)

ax = plt.subplot(111)

ax.yaxis.set_major_locator(ymajorLocator)
ax.yaxis.set_major_formatter(ymajorFormatter)

ax.yaxis.set_minor_locator(yminorLocator)

ax.yaxis.grid(True, which='major', ls='dotted')

plt.ylim(0, 450)
# plt.xlim(0, 16)

# plt.plot(imap_xcdf, imap_ycdf, '-', label="IMap")
# plt.plot(zmap_xcdf, zmap_ycdf, '-', label="ZMap")
plt.bar([0, 3, 6, 9, 12, 15], [424.6, 39.3, 6.9, 4.5, 3.1, 3.3], width=1, label="Scan at 55.6 Mpps (40 GbE)")
plt.bar([1, 4, 7, 10, 13, 16], [101.8, 8.8, 3.6, 2.1, 1.2, 1.1], width=1, label="Scan at 14.7 Mpps (10 GbE)")
plt.errorbar([0, 3, 6, 9, 12, 15], [424.6, 39.3, 6.9, 4.5, 3.1, 3.3],
             yerr=[16.8, 3.2, 1.6, 0.9, 0.5, 0.6], 
             ecolor='black', fmt="None", elinewidth=2, capthick=2, capsize=3)
plt.errorbar([1, 4, 7, 10, 13, 16], [101.8, 8.8, 3.6, 2.1, 1.2, 1.1],
             yerr=[5.7, 1.2, 0.6, 0.3, 0.2, 0.2], 
             ecolor='black', fmt="None", elinewidth=2, capthick=2, capsize=3)

plt.legend(loc='upper right', fontsize=plot_config.font_size, shadow=False)

for label in ax.xaxis.get_ticklabels():
    label.set_fontsize(plot_config.font_size)
for label in ax.yaxis.get_ticklabels():
    label.set_fontsize(plot_config.font_size)

plt.xticks([0.5, 3.5, 6.5, 9.5, 12.5, 15.5],
           ["0.1", "0.2", "0.3", "0.4", "0.5", "1.3"])
plt.xlabel('t (s)', fontsize=plot_config.font_size)
plt.ylabel('Unverified Responses (pps)', fontsize=plot_config.font_size)

plt.tight_layout(rect=[0, 0, 1, 1])
plt.subplots_adjust(wspace=0, hspace=0.05)
plt.savefig('t_impact.pdf')
plt.savefig('t_impact.png')
# plt.show()