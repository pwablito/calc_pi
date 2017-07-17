#!/apps/moose/miniconda/bin/python
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
name = MPI.Get_processor_name()
def f(x):
    return (1-(float(x)**2))**float(0.5)
n = 100000000000
nm = dict()
pi = dict()
for i in range(1,size+1):
    if i == size:
        nm[i] = (i*n/size)+1
    else:
        nm[i] = i*n/size
if rank == 0:
    val = 0
    for i in range(0,nm[1]):
        val = val+f(float(i)/float(n))
    val = val*2
    pi[0] = (float(2)/n)*(float(1)+val)
    print name, "rank", rank, "calculated", pi[0]
    for i in range(1, size):
        pi[i] = comm.recv(source=i, tag=i)
    number = sum(pi.itervalues())
    number = "%.20f" %(number)
    import time
    time.sleep(0.3)
    print "Pi is approximately", number
for proc in range(1, size):
    if proc == rank:
        val = 0
        for i in range(nm[proc]+1,nm[proc+1]):
            val = val+f(float(i)/float(n))
        val = val*2
        pi[proc] = (float(2)/n)*(float(1)+val)
        comm.send(pi[proc], dest=0, tag = proc)
        print name, "rank", rank, "calculated", pi[proc]

