import numpy as np
#q1
print("Current version of numpy is",np.__version__)

#q2
#(i)
a=np.arange(10)
print("The array is:",a)

#(ii)
b=np.random.choice([True,False],size=(3,3),p=[0.7,0.3]) #np.random.choice(choices,size of the matrix,probability of occurrence of the choices)
print(f"The boolean array is:\n",b)
"""array_bool=[[1,0,1],[0,1,1],[1,0,1]]
c=np.array(array_bool,dtype=bool)
print("The boolean array is:",c)"""

#(iii)
arr=np.array([x for x in range(2,51) if all(x%i!=0 for i in range(2,x))])
print("Array of prime numbers from 1 to 50: ",arr)

#(iv)
a=np.random.choice(100,size=20,replace=False)
print("1D array with 20 random elements: ",a)
print(f"The reshaped array is: \n",a.reshape(4,5))

#(v)
a=np.arange(10)
print("1D array with numbers ranging from 0 to 9:",a)
b=np.ones(9)
print("1D array with ones only:",b)
print("The horizontally stacked array is:", np.hstack((a,b)))

a=np.arange(100)
print("1D array with first 100 numbers:",a)
b=([x for x in range(2,1000) if all(x%i!=0 for i in range(2,x))][:100]) #extracts the first 100 prime numbers
print("1D array with first 100 prime numbers",b)

#(vi)
print("The intersection is: ",np.intersect1d(a,b))

#(vii)
print("The difference is ",np.setdiff1d(a,b))

#(viii)
overlap=np.isin(a,b)
print("The indices of common elements is",np.where(overlap)[0])

#(ix)
a=np.arange(30)
print("The array is: ",np.where((a>5) & (a<20))[0])

#q3
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print(f"original array is:\n",a)
print(f"with reversed rows is:\n",a[::-1,:])
print("with reversed columns is:\n",a[:,::-1])

#q4
a = np.random.rand(3, 3)
print(f"original matrix is: \n",a)
a[:,[0,1]]=a[:,[1,0]]
print(f"first 2 columns swapped :\n",a)

#q5
a = np.array([1, 2])
b = np.array([0, 5])
result=np.maximum(a,b)
print(" the maximum of the two arrays:",result)

#q6
a = np.random.rand(3, 3)
np.set_printoptions(precision=3)
print(f"The 3x3 matrix containing random numbers up to 3 decimal places is:\n",a)

#q7
np.set_printoptions(suppress=True)
a = np.array([0.0000001, 0.000002, 1000000, 2000000])
print(a)

#q8
a = np.array([45, 12, 67, 89, 23, 15, 90, 34, 10, 56])
print("Average",np.average(a))
print("Highest ",np.max(a))
print("Lowest ",np.min(a))
print("Numbers above 20:", np.sum(a > 20))
print("Numbers below 20:", np.sum(a < 20))

#q9
a = np.array([100, 200, 300, 400, 500])
log=np.round(np.log2(a),2)
print("log2 of each element ",log)
percent=np.round((a/np.sum(a))*100,1)
print("gene percentage",percent)

#q10
a=np.arange(0,121,20)
print("Time:",a)
popu=np.array(100*2**(a/20))
print("Population:",popu)
print(popu[-1] / popu[0])
print(a[popu > 1000])

#q11
s="GATTACA"
mapping={'A':[1,0,0,0],'T':[0,1,0,0],'G':[0,0,1,0],'C':[0,0,0,1]}
print(np.array([mapping[base] for base in s]))

#q12
a=np.random.rand(5,10)*100
mean=np.mean(a,axis=1,keepdims=True)
b=a-mean
expr=np.sum(b,axis=0)
Threshold=50
print("matrix:\n",a)
print("mean:\n",mean)
print("Total expression:\n",expr)
print("Samples (>50):\n",np.where(expr>Threshold)[0])
print("Expression data:\n",b[:,expr>Threshold])