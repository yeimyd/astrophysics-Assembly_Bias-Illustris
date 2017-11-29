//Yeimy D. Camargo Camargo 28/11/2017 (c)

#include <math.h>  
#include <stdio.h>  
#include <stddef.h>  
#include<stdlib.h>  
#include <iostream>
#include <fstream>

using namespace std; 




int main()
{
  
  int N=5000;//número de halos
 
  
  
  
  ifstream NSM;/*abre y lee el archivo de numero de sanpshot y masa*/
  NSM.open ("subhalo_mass.dat");
  

  
  
  
  double Snap,Mass;
  int i,j;
  double M[N];
  double h=0.0,m;//variable temporal para almacenar los ordendos
  double A[N];//guarda numero de snapshots correspondiente a cada halo
  for(i=0;i<=N-1;i++)
    {
      
      NSM>>Snap>> Mass;
      
      A[i]=Snap;
      M[i]=Mass;
     
    
    }
  
  
  //////////////////////////////////////////////////////



 
  ifstream SZ;/*abre y lee el archivo de numero de snap y Z (Snap_redshift.dat) allí estan los datos de número de snapshot y redshift*/
  
  SZ.open ("Snap_redshift.dat");
  
  ofstream ZM; /*escribe el archivo de datos ZvsM donde esta el redshift z, y la masa correspondiente a cada redshif, adicionalmente, esta el número de snapshot */
  ZM.open ("ZvsM_subhalo.dat");
  int k,q;
  int NS=135; //número de snapshots

  double R,Nsnap;
  double Z[NS],T[NS];//Z[NS]guarda los datos de z correspondiente a cada snapshot T[NS] guarda los datos de los numeros de sanpshots del 0-135
  
  double mass,z;    
  
  
  for(q=0;q<=NS;q++)
  
    {
      
      SZ>> Nsnap>>R;
      Z[q]=R;
      T[q]=Nsnap;
      
      
    }




  
  
  for(i=0;i<=N-1;i++)
    {
      
      
     
      for(q=0;q<=NS;q++)
	{
	  
	  
	  
	   
	   if(T[q]==A[i])
	     
	   
	   ZM<<T[q]<<"\t"<<Z[q]<<"\t"<<"\t"<<M[i]<<endl;
	   


	}
      
      cout<<T[i]<<"\t"<<Z[i]<<"\t"<<M[i]<<endl;
                
    } 



  
  
  NSM.close();
  
  SZ.close();
  ZM.close();
}
