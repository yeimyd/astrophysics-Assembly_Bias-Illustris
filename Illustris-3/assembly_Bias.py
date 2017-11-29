import groupcat as GC
import sublink as SL
import numpy as np
import matplotlib.pyplot as plt



###2###
basePath = '/media/ycamargo/ILLUSTRIS-3/Illustris-3'
GroupFirstSub = GC.loadHalos(basePath,135,fields=['GroupFirstSub'])


###3###
fields = ['SubhaloMass','SubfindID','SnapNum']
start = 0
for i in range(start,start+5):
    tree = SL.loadTree(basePath,135,GroupFirstSub[i],fields=fields,onlyMPB=True)
   

###4###

def find_formation_time(sublinktree):
    final_mass = sublinktree['SubhaloMass'][0]
    initial_mass = sublinktree['SubhaloMass'][-1]
    n_points = len(sublinktree['SubhaloMass'])
    formation_snap = -1
    for i in range(n_points-1, -1, -1):
        if sublinktree['SubhaloMass'][i] > final_mass/2.0:
            formation_snap = sublinktree['SnapNum'][i]
    
            break
    return formation_snap

    
###5###



fields = ['SubhaloMass','SubfindID','SnapNum']

start = 0
n_halos = 5000
formation_time = []
final_mass = []
for i in range(start,start+n_halos):
    tree = SL.loadTree(basePath,135,GroupFirstSub[i],fields=fields,onlyMPB=True)
    formation_time.append(find_formation_time(tree))
    final_mass.append(tree['SubhaloMass'][0])




#data=list(zip(formation_time,final_mass))
#for h,k in enumerate(data):
#    line=''.join(str(x).ljust(12) for x in k)
#    print(line)


f1 = open ('subhalo_mass.dat','w')
subh=list(zip(formation_time,final_mass ))
for h,k in enumerate(subh):
    line1=''.join(str(x).ljust(20) for x in k)
    f1.writelines(line1+ '\n')
    f1.close




# Stellar masses



fields = ['SubhaloMass','SubfindID','SnapNum', 'SubhaloMassInRadType']

for i in range(start,start+5):
    tree = SL.loadTree(basePath,135,GroupFirstSub[i],fields=fields,onlyMPB=True)
    plt.plot(tree['SnapNum'],tree['SubhaloMassInRadType'][:,4],'-')



####12

def find_formation_time_stellar_mass(sublinktree):
    final_mass = sublinktree['SubhaloMassInRadType'][0,4]
    initial_mass = sublinktree['SubhaloMassInRadType'][-1,4]
    n_points = len(sublinktree['SubhaloMassInRadType'][:,4])
    formation_snap = -1
    for i in range(n_points-1, -1, -1):
        if sublinktree['SubhaloMassInRadType'][i,4] > final_mass/2.0:
            formation_snap = sublinktree['SnapNum'][i]
            break
    return formation_snap




###17##### MasavsSnapshot

fields = ['SubhaloMass','SubfindID','SnapNum', 'SubhaloMassInRadType']
start = 0
n_halos = 5000
formation_time_stellar = []
final_stellar_mass = []
for i in range(start,start+n_halos):
    tree = SL.loadTree(basePath,135,GroupFirstSub[i],fields=fields,onlyMPB=True)
    formation_time_stellar.append(find_formation_time_stellar_mass(tree))
    final_stellar_mass.append(tree['SubhaloMassInRadType'][0,4])





#data=list(zip(formation_time_stellar,final_stellar_mass))
#for h,k in enumerate(data):
#    line=''.join(str(x).ljust(12) for x in k)
#    print(line)


f = open ('stellar_mass.dat','w')
stellar=list(zip(formation_time_stellar,final_stellar_mass))
for h,k in enumerate(stellar):
    line=''.join(str(x).ljust(20) for x in k)
    f.writelines(line+ '\n')
    f.close





























