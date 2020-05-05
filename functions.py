from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

from data import f_bias, sphere, schwefel, rosenbrock, rastrigin, griewank, ackley

def plot_fct (fct, bounds=[-100,100]):
    fig = plt.figure(figsize=(10,10))
    ax = fig.gca(projection='3d')

    # Make data.
    X = np.arange(bounds[0], bounds[1]+1, (bounds[1]-bounds[0])/400)
    Y = np.arange(bounds[0], bounds[1]+1, (bounds[1]-bounds[0])/400)
    X, Y = np.meshgrid(X, Y)
    Z = fct(np.stack((X.ravel(), Y.ravel()),axis=1))

    # Plot the surface.
    surf = ax.plot_trisurf(X.ravel(), Y.ravel(), Z, cmap=plt.cm.Spectral,linewidth=0.2, antialiased=False)
    plt.show()
    

#  F1: Shifted Sphere Function 
def Shifted_Sphere( x ):
    z=0
    F = 0
    for i in range(0,x.shape[1]):
        z = x[:,i] - sphere[i]
        F = F + z*z;
    return F + f_bias[0];



#  F2: Schwefel’s Problem 2.21 
def Schwefel_Problem( x ):
    F = abs(x[:,0])
    for i in range(0,x.shape[1]):
        z = x[:,i] - schwefel[i]
        F = np.maximum(F , abs(z))
    return F + f_bias[1]



# F3: Shifted Rosenbrock’s Function 
def Shifted_Rosenbrock( x ):
    z=[]
    F = 0
    for i in range(0,x.shape[1]):
        z.append(x[:,i] - rosenbrock[i] + 1)
    for i in range(0,x.shape[1]-1):   
        F = F + 100*(z[i]**2-z[i+1])**2  + (z[i]-1)**2
    #print (F)
    return F + f_bias[2]




# F4: Shifted Rastrigin’s Function 
def Shifted_Rastrigin( x ):
    F = 0;
    for i in range(0,x.shape[1]):
        z = x[:,i] - rastrigin[i];
        F = F + ( z**2 - 10*np.cos(2*np.pi*z) + 10);
    return F + f_bias[3]; 




# F5: Shifted Griewank’s Function 
def Shifted_Griewank( x ):
    F1 = 0;
    F2 = 1;
    for i in range(0,x.shape[1]):    
        z = x[:,i] - griewank[i];
        F1 = F1 + ( z**2 / 4000 );
        F2 = F2 * ( np.cos(z/np.sqrt(i+1)));
    return (F1 - F2 + 1 + f_bias[4]); 



# F6: Shifted Ackley’s Function 
def Shifted_Ackley( x ):
    Sum1 = 0
    Sum2 = 0
    F = 0
    for i in range(0,x.shape[1]):  
        z = x[:,i] - ackley[i]
        Sum1 = Sum1 + z**2
        Sum2 = Sum2 + np.cos(2*np.pi*z)
    F = -20*np.exp(-0.2*np.sqrt(Sum1/x.shape[1])) -np.exp(Sum2/x.shape[1]) + 20 + np.e + f_bias[5];
    return F; 


