import h5py
import numpy as np
import pylab as pl
from matplotlib.mlab import PCA
from mpl_toolkits.mplot3d import Axes3D


name = "koendata.h5"
file = h5py.File(name, 'r')
    
def dataProcessing(file, rat, date):
    object = file[rat][date]["valueMatrix"]
    data = np.array(object)
    pca = PCA(data)
    print pca.fracs[0], pca.fracs[1], pca.fracs[2], pca.fracs[3]

    pl.close('all') 
    fig1 = pl.figure()
    ax = Axes3D(fig1)
    ax.scatter(pca.Y[::1,0], pca.Y[::1,1], pca.Y[::1,2], 'bo')
    ax.set_xlim([-10,20])
    ax.set_ylim([-15,15])
    ax.set_zlim([-15,10])
    pl.savefig("3D_" +rat + "_" + date+".png")

    pl.close('all') 
    pl.xlim([-10,20])
    pl.ylim([-15,15])
    pl.scatter(pca.Y[::1,0], pca.Y[::1,1])
    pl.savefig("2D_" + rat + "_" + date + ".png")


    
        
for rat in file.keys():
    #dataProcessing(file, rat, file[rat][0])
    date1 = file[rat].keys()[0]
    object = file[rat][date1]["valueMatrix"]
    data = np.array(object)
    pca = PCA(data)
    print pca.fracs[0], pca.fracs[1], pca.fracs[2], pca.fracs[3]

    pl.close('all') 
    fig1 = pl.figure()
    ax = Axes3D(fig1)
    ax.scatter(pca.Y[::1,0], pca.Y[::1,1], pca.Y[::1,2], 'bo')
    ax.set_xlim([-10,20])
    ax.set_ylim([-15,20])
    ax.set_zlim([-15,15])
    pl.savefig("3D_" +rat + "_" + date1+".png")

    pl.close('all') 
    pl.xlim([-10,20])
    pl.ylim([-15,15])
    pl.scatter(pca.Y[::1,0], pca.Y[::1,1])
    pl.savefig("2D_" + rat + "_" + date1 + ".png")
    
    for date in file[rat]:
        if date != date1: 
            try:
                object = file[rat][date]["valueMatrix"]
                data = np.array(object)
                projectedData = pca.project(data)

                pl.close('all') 
                fig1 = pl.figure()
                ax = Axes3D(fig1)
                ax.scatter(projectedData[::1,0], projectedData[::1,1], projectedData[::1,2], 'bo')
                ax.set_xlim([-10,20])
                ax.set_ylim([-15,20])
                ax.set_zlim([-15,15])
                pl.savefig("3D_" +rat + "_" + date+".png")

                pl.close('all') 
                pl.xlim([-10,20])
                pl.ylim([-15,15])
                pl.scatter(projectedData[::1,0], projectedData[::1,1])
                pl.savefig("2D_" + rat + "_" + date + ".png")
                #dataProcessing(file, rat, date)
            except ValueError:
                print "Probably NaN"
