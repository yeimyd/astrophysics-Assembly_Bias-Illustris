Yeimy D. Camargo Camargo 28/11/2017 (c)

Análisis Illustris-project.org

Con este script se obtiene el redshift y número de snapshot donde cada halo/masa estelar de cada galaxia adquirio la mitad de su masa actual y su mediana de formación (en redshift y snapshot)


Se requiere la instalación de:

Gnuplot
python3
modulos de Illustris_python, los encuentras en https://bitbucket.org/illustris/illustris_python/downloads/
c++
 

Para correr el shell-script, en la terminal: sh run.sh

Dentro de cada carpeta Illustris-# (Illsutris-1, Illustris-2, Illustris-3) se debe verificar en el archivo 
assembly_Bias línea 9 el basePath (lugar donde se encuentran los datos Illustris) ej. basePath = '/media/ycamargo/ILLUSTRIS-3/Illustris-2',en este ejemplo mis datos Illustris-# se encuentran en el volumen media de ycamargo carpeta ILLUSTRIS-3 subcarpeta Illustris-2, en esa ubicación se encuentran las carpetas con los datos gropus_135, snapdir_135 y trees, tal como sugieren en la pag de Illustris project (http://www.illustris-project.org/data/docs/scripts/).


Cuando se corre en la terminal el shell-script debes entrar a cada carpeta illustris-# y hay una carpeta llamada graficas-# y allí encontras las correspondientes gráficas.
