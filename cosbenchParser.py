#!/usr/bin/python
import sys
import datetime as dt
import csv
import numpy as np
import matplotlib.pyplot as plt
def create_files(argv):
	agg, x, y, k = [],[],[],[]
	with open(sys.argv[1],'r') as csvfile:
    		plots = csv.reader(csvfile, delimiter=',')
		next(plots, None)
		next(plots, None)
    		for row in plots:
			 x.append(dt.datetime.strptime(row[0], '%H:%M:%S'))
			 k.append(float(row[9]))	
			 y.append(float(row[10]))
			 agg.append(float(row[9])+float(row[10]))
	xticks=len(x)
	x_data=[]
	for i in range(xticks):
		x_data.append(i)	
	fig = plt.figure(figsize=(18,6))
	ax1 = fig.add_subplot(111)
	ax1.yaxis.grid(True)
	ax1.xaxis.grid(True)
	ax1.yaxis.grid(color='#CDCDC1', linestyle='-', linewidth=1)
	ax1.xaxis.grid(color='#CDCDC1', linestyle='-', linewidth=1)
	ax1.set_axisbelow(True)
	ax1.plot(x_data, k, color='b',linewidth=1, marker="o", label='64K')
	ax1.plot(x_data, y, color='b',linewidth=1, marker="o", label='64M')
	ax1.plot(x_data, k, color='m',linewidth=1, marker="o", label='1G')
	ax1.plot(x_data, agg, color='orange',linewidth=1, marker="o", label='Aggreated')
	plt.tick_params(axis='both', which='major', labelsize=18)
	plt.tick_params(axis='both', which='minor', labelsize=18)
	plt.ylabel('Throughput (op/s)',  fontsize=20)
	plt.xlabel('Time (sec)',  fontsize=20)
	leg=plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=4, mode="expand", borderaxespad=0., fontsize=19)
	plt.subplots_adjust(left=0.12,bottom=0.18, right=0.9, top=0.85, wspace=0.2,hspace=0.2)
	plt.savefig(sys.argv[2]+'.pdf', format='pdf', dpi=1000)
	plt.savefig(sys.argv[2]+'.eps', format='eps', dpi=1000)
	plt.show()


if __name__ == "__main__":
	create_files(sys.argv[1:])
