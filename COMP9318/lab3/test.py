

## import modules here
import pandas as pd
import numpy as np
import helper





df = helper.read_data('./asset/c_.txt')


slice_data = helper.slice_data_dim0(df, 1)

print(slice_data)
for line in slice_data:
    print(line)