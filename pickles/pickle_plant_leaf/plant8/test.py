import pickle as pi
import numpy as np

file=open("plant_8.pickle","rb")
data=pi.load(file)
print(data[0])
print(data[0].__len__())