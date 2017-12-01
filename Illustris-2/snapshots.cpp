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

  ifstream stellar;
  stellar.open("stellar_mass.dat");
  
  
  
  
    double Snap,Mass,stellar_mass,stellar_snap;
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

  double  MS[N],SS[N];
  for(i=0;i<=N-1;i++)
    {
      
      stellar>>stellar_snap>>stellar_mass;
      SS[i]= stellar_snap;
      MS[i]=stellar_mass;     
     
    }
  
  
  //////////////////////////////////////////////////////
  
  
  
  
  ifstream SZ;/*abre y lee el archivo de numero de snap y Z (Snap_redshift.dat) allí estan los datos de número de snapshot y redshift*/
  
  SZ.open ("Snap_redshift.dat");
  
 

  
  int k,q;
  int NS=135; 
  double R,Nsnap;
  double Z[NS],T[NS];
 
  for(q=0;q<=NS;q++)
    
    {
      
      SZ>> Nsnap>>R;
      Z[q]=R;
      T[q]=Nsnap;
      
      
    }
  ofstream ZM;
  ZM.open ("ZvsM_subhalo.dat");
  
  for(i=0;i<=N-1;i++)
    {
      
      for(q=0;q<=NS;q++)
	{
	  
	  if(T[q]==A[i])
	    
	    
	    ZM<<T[q]<<"\t"<<Z[q]<<"\t"<<"\t"<<M[i]<<endl;
	  
	}
      
    }
  
  
 ofstream Zstellar;
  Zstellar.open ("ZvsM_stellar.dat");
  
  
  for(i=0;i<=N-1;i++)
    {
      
      for(q=0;q<=NS;q++)
	{
	  
	  if(T[q]==SS[i])
	    
	    
	    Zstellar<<T[q]<<"\t"<<Z[q]<<"\t"<<"\t"<<MS[i]<<endl;
  
	}
      
    }
  
  
  
  NSM.close();
  SZ.close();
  ZM.close();
  stellar.close();
  Zstellar.close();
  
}
