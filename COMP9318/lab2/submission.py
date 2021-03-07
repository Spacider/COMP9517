## import modules here 
import pandas as pd
import numpy as np
# import helper
from COMP9318.lab2.helper import project_data, select_data, remove_first_dim, slice_data_dim0, read_data


################### Question 1 ###################

def buc_rec_optimized(df):# do not change the heading of the function
    col = len(df)
    # for d in range(col):
    #     print(project_data(df, d))
    # df = remove_first_dim(df)
    fist_row = project_data(df, 1)
    print(fist_row)
    for num in fist_row:
        print(slice_data_dim0(df, num))
        print("-------------------")


if __name__ == '__main__':
    input_data = read_data('./assert/a_.txt')
    output = buc_rec_optimized(input_data)
    # print(output)