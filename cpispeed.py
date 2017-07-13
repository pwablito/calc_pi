#!/opt/moose/miniconda/bin/python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import os
import time
tp1 = time.time()
os.system('cd ~/Desktop/Scripts/Practice; ./cpi.pl > piperl.txt')
tp = time.time()-tp1
in_file = open('piperl.txt', 'rt')
perlpi = in_file.read()
in_file.close()
perlpi = float(perlpi)
realpi = 3.14159265358979323846264338
tpy1 = time.time()
os.system('cd ~/Desktop/Scripts/Practice; ./cpi.py > pipy.txt')
tpy = time.time()-tpy1
in_file = open('pipy.txt', 'rt')
pythonpi = in_file.read()
in_file.close()
pythonpi = float(pythonpi)
os.system('cd ~/Desktop/Scripts/Practice; gcc cpi.c')
tc1 = time.time()
os.system('cd ~/Desktop/Scripts/Practice; ./a.out > piinc.txt')
tc = time.time()-tc1
in_file = open('piinc.txt', 'rt')
cpi = in_file.read()
in_file.close()
cpi = float(cpi)
objects = ('Perl', 'Python', 'C')
y_pos = np.arange(len(objects))
performance = [1/tp,1/tpy,1/tc]
precision = [abs(realpi - perlpi),abs(realpi - pythonpi),abs(realpi - cpi)]
plt.figure(1)
plt.subplot(3,1,1)
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('''Speed
(runs per second)''')
plt.title('CPI Speed and Precision')
plt.subplot(3,1,2)
plt.bar(y_pos, precision, align='center', alpha=0.5)
perlobject = '''Perl
%s''' % perlpi
pyobject = '''Python
%s''' % pythonpi
cobject = '''C
%s''' % cpi
piobjects = [perlobject, pyobject, cobject]
plt.xticks(y_pos, piobjects)
plt.ylabel('''Error
(distance from pi)''')
speed = [tp,tpy,tc]
plt.subplot(3,1,3)
speed = [tp,tpy,tc]
overall = [1/(tp*abs(realpi - perlpi)), 1/(tpy*abs(realpi - pythonpi)), 1/(tc*abs(realpi - cpi))]
plt.bar(y_pos, overall, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('''Overall performance
(speed x precision)''')
plt.gcf().subplots_adjust(left=0.18)
plt.gcf().subplots_adjust(bottom=0.15)
plt.savefig('cpistats.pdf',pad_inches=5)
os.system('cd ~/Desktop/Scripts/Practice; rm piperl.txt pipy.txt piinc.txt')
os.system('open cpistats.pdf')
