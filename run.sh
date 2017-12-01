##Yeimy D. Camargo Camargo 28/11/2017 (c)

##Illustris-1
#cd illustris-1
#mkdir graficas1

#python3 assembly_Bias.py
#g++ snapshots.cpp -o snaps1
#cp snaps1 /tmp
#chmod +x /tmp/snaps1
#/tmp/snaps1

#python3 median.py


#gnuplot graph.gp

#mv Median_snapStellar.png graficas1
#mv MedianSubhalo_Z.png graficas1
#mv Median_ZStellar.png graficas1
#mv MedianSubhalo_snap.png graficas1
#mv SnapvsMass_Subhalo.png graficas1
#mv SnapvsM_stellar.png graficas1
#mv ZvsM_stellar.png graficas1
#mv ZvsM_subhalo.png graficas1



#cd ..

####Illustris-2

cd illustris-2
mkdir graficas2

python3 assembly_Bias.py
g++ snapshots.cpp -o snaps2
cp snaps2 /tmp
chmod +x /tmp/snaps2
/tmp/snaps2


python3 median.py


gnuplot graph.gp

mv Median_snapStellar.png graficas2
mv MedianSubhalo_Z.png graficas2
mv Median_ZStellar.png graficas2
mv MedianSubhalo_snap.png graficas2
mv SnapvsMass_Subhalo.png graficas2
mv SnapvsM_stellar.png graficas2
mv ZvsM_stellar.png graficas2
mv ZvsM_subhalo.png graficas2


cd ..


#####Illustris-3

cd illustris-3
mkdir graficas3

python3 assembly_Bias.py

g++ snapshots.cpp -o snaps3
cp snaps3 /tmp
chmod +x /tmp/snaps3
/tmp/snaps3


python3 median.py


gnuplot graph.gp

mv Median_snapStellar.png graficas3
mv MedianSubhalo_Z.png graficas3
mv Median_ZStellar.png graficas3
mv MedianSubhalo_snap.png graficas3
mv SnapvsMass_Subhalo.png graficas3
mv SnapvsM_stellar.png graficas3
mv ZvsM_stellar.png graficas3
mv ZvsM_subhalo.png graficas3

cd ..
###fin
