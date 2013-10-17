
import pylab 
import numpy as np
from numpy import pi
import scipy
from scipy.fftpack import fft, fftfreq
import matplotlib.pyplot as plt

importarDatos=open('sampled+ma0844az_1-1+_data.txt', 'r') #se importan los datos del encefalograma

#Transformada de fourier con espectro de potencias P

datos = importarDatos.read() # cadena con contenido del archivo

#Tiempo
tiempo=[]
nl=400
for a in range(nl):
	tiempo=a
 
#saca los datos de las columnas

nc=24
for i in range(nc):
	datosColumna = datos[:i]
	print datosColumna

d=0.1 #paso de frecuencia
fft_datos= fft(datosColumna)/nl #fourier
frecuencia= fftfreq(len(tiempo),d) #frecuencia
fft_x=np.abs(fft_datos) ** 2 #norma al cuadrado

#Grafica del espectro de potencias
plt.plot(frecuencia,fft_x)
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Espectro')

#Obtencion de 10 valores maximos
maxim=zeros(1,10)
for i in range(0,len(maxim)):
	maxim[i]=max(fft_x)
		for j in range (0,len(fft_x)):
			if fft_x[j]==max[0]:
				fft_x[j]=0

#Reemplaza los otros valores por cero
for k in range(0,len(fft_datos)):
	for h in range(0,len(maxim)):
		if fft_datos[k]!=maxim[h]:
			fft_datos[k]=0

#Grafica de la senal reconstruida
senalInvertida=ifft(fft_datos)
plt.plot(tiempo,senalInvertida)
plt.xlabel('Tiempo (min)')
plt.ylabel('Amplitud')
plt.title('Senal reconstruida')

#Grafica de la senal original
plt.plot(tiempo,datos2)
plt.xlabel('Tiempo (min)')
plt.ylabel('Amplitud')
plt.title('Senal original')

#Prueba chi cuadrado
chi2=0
for c in range(0,len(tiempo)):
	chi2=chi2+(((datos2[c]-senalInvertida[c])**2)/senalInvertida[c])
print 'La prueba chi cuadrado dio ',chi2

