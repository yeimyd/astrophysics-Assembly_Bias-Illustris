#Yeimy D. Camargo Camargo 28/11/2017 (c)


import numpy as np
import matplotlib.pyplot as plt

start = 0
n_halos = 10
Snapformation_time = []
Zformation=[]
final_mass = []

archivo=open("ZvsM_subhalo.dat","r")  #abre el archivo ZvsM donde estan los datos ordendos(por snap) de snapshot, z y masas de correspondinetes
for i in (row.strip().split() for row in archivo): #lee por columnas el archivo (python solo lee listas)

    Snapformation_time.append(float(i[0])) #convierte las columnas de los datos en listas para operar los datos
    Zformation.append(float(i[1]))
    final_mass.append(float(i[2]))

Snapformation_time = np.array(Snapformation_time) #convierte los datos de listas a array
Zformation=np.array(Zformation)
final_mass = np.array(final_mass)

n_bins = 10
mass_bins = np.logspace(1.5,4,n_bins) #crea un espacio log igualmente espaciado comenzando en 10^1.5 y termina el 10^4 y crea 9 partes iguales 4-1.5/9
medianSnap_formation = np.ones(n_bins-1) #llena de 1 todo 
medianZ_formation = np.ones(n_bins-1)

for i in range(n_bins-1):
    ii = (final_mass > mass_bins[i]) & (final_mass < mass_bins[i+1]) #busca masas que cumplan con cada espacio del log
    medianSnap_formation[i] = np.median(Snapformation_time[ii]) #las masas que cumplen con esa condición les asigna el snapshot/z y les calcula la mediana de snapshot/z (ordena los datos si no estan ordenados)
    medianZ_formation[i] = np.median(Zformation[ii])
    
    
centered_mass_bin = 0.5*(mass_bins[1:] + mass_bins[0:-1]) #masas en el espacio log



 
f1 = open ('median_subhalo.dat','w')#Genera el archivo median_subhalo.dat cuyas columnas son, masa, mediana de Z, mediana de snapshot
median_subh=list(zip(centered_mass_bin,medianZ_formation,medianSnap_formation))
for h,k in enumerate(median_subh):
    line1=''.join(str(x).ljust(20) for x in k)
    f1.writelines(line1+ '\n')
    f1.close



archivo.close()



##############Median Stellar########################

Snapformation_Stellar_time = []
Zformation_Stellar=[]
final_Stellar_mass = []

archivo1=open("ZvsM_stellar.dat","r")  
for i in (row.strip().split() for row in archivo1): 

    Snapformation_Stellar_time.append(float(i[0])) 
    Zformation_Stellar.append(float(i[1]))
    final_Stellar_mass.append(float(i[2]))

Snapformation_Stellar_time = np.array(Snapformation_Stellar_time) 
Zformation_Stellar=np.array(Zformation_Stellar)
final_Stellar_mass = np.array(final_Stellar_mass)





n_binsStellar = 10
Stellar_mass_bins = np.logspace(-2,2,n_binsStellar) 
medianSnap_stellarformation = np.ones(n_binsStellar-1)  
medianZ_stellarformation = np.ones(n_binsStellar-1)

for i in range(n_binsStellar-1):
    ii = (final_Stellar_mass > Stellar_mass_bins[i]) & (final_Stellar_mass < Stellar_mass_bins[i+1]) 
    medianSnap_stellarformation[i] = np.median(Snapformation_Stellar_time[ii])
    medianZ_stellarformation[i] = np.median(Zformation_Stellar[ii])
    
    
centered_mass_binstellar = 0.5*(Stellar_mass_bins[1:] + Stellar_mass_bins[0:-1]) 


f = open ('median_stellar.dat','w')#Genera el archivo median_stellar.dat cuyas columnas son, masa, mediana de Z, mediana de snapshot
median_stellar=list(zip(centered_mass_binstellar,medianZ_stellarformation,medianSnap_stellarformation))
for h,k in enumerate(median_stellar):
    line2=''.join(str(x).ljust(20) for x in k)
    f.writelines(line2+ '\n')
    f.close









#data=list(zip(centered_mass_binstellar,medianZ_stellarformation,medianSnap_stellarformation)) 
#for h,k in enumerate(data):
#    line=''.join(str(x).ljust(20) for x in k)
#    print(line)






archivo1.close()















