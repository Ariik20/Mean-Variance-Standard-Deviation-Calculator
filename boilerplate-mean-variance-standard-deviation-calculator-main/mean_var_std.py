import numpy as np

def calculate(list):
    arr=np.array(list)
    reshaped_Array=arr.reshape(3,3)
    #finding Mean
    row_means=np.mean(reshaped_Array, axis=1)
    column_means=np.mean(reshaped_Array, axis=0)
    # finding Variance
    row_var=np.var(reshaped_Array,axis=1)
    column_var=np.var(reshaped_Array,axis=0)
    # finding Deviation
    row_deviation=np.std(reshaped_Array,axis=1)
    column_deviation=np.std(reshaped_Array,axis=0)
    # finding Maximum NUMBER
    row_max=np.max(reshaped_Array,axis=1)
    column_max=np.max(reshaped_Array,axis=0)
    # finding MININUM NUMBER
    row_min=np.min(reshaped_Array,axis=1)
    column_min=np.min(reshaped_Array,axis=0)
    # FINDING SUM
    row_sum=np.sum(reshaped_Array,axis=1)
    column_sum=np.sum(reshaped_Array,axis=0)

    # CREATE THE DICTIONARY TO STORE ALL YOUR DATA 
    calculations = {
    "mean": [column_means,row_means,reshaped_Array.mean()],
    "variance": [column_var,row_var,reshaped_Array.var()],
    "standard deviation":[column_deviation,row_deviation,reshaped_Array.std()],
    "max": [column_max,row_max,reshaped_Array.max()],
    "min": [column_min,row_max,reshaped_Array.min()],
    "sum": [column_sum,row_sum,reshaped_Array.sum()]
             }

    return calculations