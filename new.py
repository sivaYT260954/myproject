
import numpy as np

marks = np.array ([[70,80,90],
[60,75,85],[88,92,79],[55,65,70]])
        

print("shape:",marks.shape) 
print("datatype:",marks.dtype)
print("size:",marks.size)

print("slicing:", marks [:2,-1])

print("student averages: ", marks.mean(axis=1).round(2))

print("student average: ", marks.mean(axis=0))

grace_marks= marks + 5
print("grace marks:")
print(grace_marks)


weights =[0.3,0.3,0.4]

print("weighted scores: ", np.dot(marks,weights))

arr=np.arange(12).reshape(3,4)
print(arr)


