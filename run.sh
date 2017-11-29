##Yeimy D. Camargo Camargo 28/11/2017 (c)

##Illustris-1
#cd illustris-1
#mkdir graficas1

#python3 assembly_Bias.py
#g++ snap_subhalo.cpp -o subhalo1
#cp subhalo1 /tmp
#chmod +x /tmp/subhalo1
#/tmp/subhalo1


#g++ snap_stellar.cpp -o stellar1
#cp stellar1 /tmp
#chmod +x /tmp/stellar1
#/tmp/stellar1

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
g++ snap_subhalo.cpp -o subhalo2
cp subhalo2 /tmp
chmod +x /tmp/subhalo2
/tmp/subhalo2


g++ snap_stellar.cpp -o stellar2
cp stellar2 /tmp
chmod +x /tmp/stellar2
/tmp/stellar2

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
g++ snap_subhalo.cpp -o subhalo3
cp subhalo3 /tmp
chmod +x /tmp/subhalo3
/tmp/subhalo3


g++ snap_stellar.cpp -o stellar3
cp stellar3 /tmp
chmod +x /tmp/stellar3
/tmp/stellar3

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
