set terminal png
set output "ZvsM_subhalo.png"
set xlabel "Total Subhalo Mass [Code Units]"
set ylabel "Redshift Formation"
unset key
set grid
set logscale x
plot "ZvsM_subhalo.dat" u 3:2 pt 7 ps 1.5
set output


set terminal png
set output "SnapvsMass_Subhalo.png"
set xlabel "Total Subhalo Mass [Code Units]"
set ylabel "Formation Snapshot"
unset key
set grid
set logscale x
plot "ZvsM_subhalo.dat" u 3:1 pt 7 ps 1.5
set output

###########median##############



set terminal png
set output "MedianSubhalo_snap.png"
set xlabel "Median Subhalo Mass [Code Units]"
set ylabel "Median Formation Snapshot"
unset key
set grid
set logscale x
plot "median_subhalo.dat" u 1:3 pt 7 ps 1.5
set output



set terminal png
set output "MedianSubhalo_Z.png"
set xlabel "Median Subhalo Mass [Code Units]"
set ylabel "Median Formation Redshitf"
unset key
set grid
set logscale x
plot "median_subhalo.dat" u 1:2 pt 7 ps 1.5
set output


#**********stellar***********

set terminal png
set output "ZvsM_stellar.png"
set xlabel "Total Stellar Mass [Code Units]"
set ylabel "Redshift Formation"
unset key
set grid
set logscale x
plot "ZvsM_stellar.dat" u 3:2 pt 7 ps 1.5
set output


set terminal png
set output "SnapvsM_stellar.png"
set xlabel "Total Stellar Mass [Code Units]"
set ylabel "Formation Snapshot"
unset key
set grid
set logscale x
plot "ZvsM_stellar.dat" u 3:1 pt 7 ps 1.5
set output

###########median##############



set terminal png
set output "Median_snapStellar.png"
set xlabel "Median Stellar Mass [Code Units]"
set ylabel "Median Formation Snapshot"
unset key
set grid
set logscale x
plot "median_stellar.dat" u 1:3 pt 7 ps 1.5
set output



set terminal png
set output "Median_ZStellar.png"
set xlabel "Median Stellar Mass [Code Units]"
set ylabel "Median Formation Redshitf"
unset key
set grid
set logscale x
plot "median_stellar.dat" u 1:2 pt 7 ps 1.5
set output
