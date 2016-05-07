import cPickle as pickle
import numpy as np
import os

print('Checking cluster centers...')
c1 = pickle.load(open('clustercenters-1.p', 'rb'))
c8 = np.load('clustercenters.npy')

THRESHOLD = 1.0e-3
ndiff = 0
for (x,y) in zip(c1,c8):
   dist = np.sqrt(np.sum((x-y)**2))
   if dist > THRESHOLD:
       ndiff += 1
print('%d / %d centers differ' % (ndiff, len(c1)))

print('Checking cluster assignments...')

def load_dtrajs(dirname):
   trajectories = list()
   ntraj = 10
   for trajindex in range(ntraj):
      filename = os.path.join(dirname, '%d.npy' % trajindex) 
      trajectory = np.load(filename)
      trajectories.append(trajectory)
   return trajectories

trajs1 = load_dtrajs('dtrajs-1')
trajs8 = load_dtrajs('dtrajs')

for (traj1, traj8) in zip(trajs1, trajs8):
    nmatch = (traj1 == traj8).sum()
    ntot = len(traj1)
    print('%8d / %8d cluster assignents match' % (nmatch, ntot))

