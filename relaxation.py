#
# Capacitor Potential Relaxation
#
#
import numpy as np
import matplotlib.pyplot as plt

iterations = 500
grid_size = 50
plate_thickness= 0.05 * grid_size 
plate_width = .5 * grid_size
gap = .05 * grid_size
potential = 1

side = grid_size
plate_start0 = (grid_size - plate_width)*0.5
plate_end0 = (grid_size + plate_width)*0.5 + 1
plate1_start1 = (side - gap)*0.5
plate1_end1 = (plate1_start1 - plate_thickness)-1
plate2_start1 = (side + gap)*0.5
plate2_end1 = (plate2_start1 + plate_thickness)+1


#print(plate_start0,plate_end0,plate1_start1,plate1_end1,plate2_start1,plate2_end1)



array0 = np.zeros((side,side))
array0[0,:] = 0
array0[-1,:] = 0
array0[:,0] = 0
array0[:,-1] = 0
array0[plate1_end1:plate1_start1,plate_start0:plate_end0] = potential
array0[plate2_start1:plate2_end1,plate_start0:plate_end0] = potential

#print(array0)

array1 = np.roll(array0,1,0)
array2 = np.roll(array0,-1,0)
array3 = np.roll(array0,1,1)
array4 = np.roll(array0,-1,1)        

for i in range(iterations):
    print('Iteration number %i out of %i' %(i,iterations))
    array0 = 0.25*(array1 + array2 + array3 + array4)
    array0[0,:] = 0
    array0[-1,:] = 0
    array0[:,0] = 0
    array0[:,-1] = 0
    array0[plate1_end1:plate1_start1,plate_start0:plate_end0] = potential
    array0[plate2_start1:plate2_end1,plate_start0:plate_end0] = -1*potential
    array1 = np.roll(array0,1,0)
    array2 = np.roll(array0,-1,0)
    array3 = np.roll(array0,1,1)
    array4 = np.roll(array0,-1,1)

#print(array0)
    
#plt.plot(array0)
plt.figure(figsize=(7.5,5))
plt.imshow(array0)
plt.title('Capacitor Potential Relaxation')
plt.axis('off')

plt.show()






