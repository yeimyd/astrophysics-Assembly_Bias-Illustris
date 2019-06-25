import groupcat as GC
import sublink as SL
import numpy as np
import lhalotree as LH
import h5py
import matplotlib.pyplot as plt



basePath = '/home/illustris/Desktop/trabajo/Illustris-3lht'
GroupFirstSub = GC.loadHalos(basePath,135,fields=['GroupFirstSub'])
Halos=GC.loadHalos(basePath,135,fields=['Group_M_Crit200','GroupPos', 'GroupNsubs'])
GroupNsubs=GC.loadHalos(basePath,135,fields=['GroupNsubs'])
Halo_mass= Halos['Group_M_Crit200']
Halo_Pos=Halos['GroupPos']

print(len(GroupNsubs))




fields = ['SnapNum', 'Group_M_Crit200']
start = 0

for i in range(start,start+5): 
        #if GroupNsubs[i] == 0:
         #       continue
	tree = LH.loadTree(basePath,135,GroupFirstSub[i],fields=fields,onlyMPB=True)
    

def find_formation_time(sublinktree):
    final_mass = sublinktree['Group_M_Crit200'][0]
    initial_mass = sublinktree['Group_M_Crit200'][-1]
    n_points = len(sublinktree['Group_M_Crit200'])
    formation_snap = 135
    for i in range(n_points-1, -1, -1):
        if sublinktree['Group_M_Crit200'][i] > final_mass/2.0:
            formation_snap = sublinktree['SnapNum'][i]
    
            break
    return formation_snap






fields = ['SnapNum','Group_M_Crit200']

start = 0
n_halos = len(Halos['Group_M_Crit200'])
formation_time = []
final_mass = []
for i in range(start,start+n_halos):
	if GroupNsubs[i] != 0:  
		#continue
		tree = LH.loadTree(basePath,135,GroupFirstSub[i],fields=fields,onlyMPB=True)
		formation_time.append(find_formation_time(tree))
		final_mass.append(tree['Group_M_Crit200'][0])

#print(formation_time,final_mass,Halo_Pos)

ii=Halo_mass>0
f1 = open ('Halo_Mass.dat','w')
subh=list(zip(formation_time,Halo_mass[ii],Halo_Pos[ii]))
for h,k in enumerate(subh):
    line1=''.join(str(x).ljust(20) for x in k)
    f1.writelines(line1+ '\n')
    f1.close


