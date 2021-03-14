## import modules here 
import pandas as pd
import numpy as np
import helper


################### Question 1 ###################

def buc_rec_optimized(df):

    # df = helper.project_data(df, 1) 0 选择第一列 1选择第二列
    # df = helper.select_data(df, 0, 1) 选择第一列值为 1 的全部数据
    # df = helper.slice_data_dim0(df, 1) # 选择第1列值为1的剩余数据

    if len(df) == 1:
        # single-tuple optimization
        result_df = None
        print("this is single tuple")
    else:
        # multiple tuple optimization
        result_df = pd.DataFrame(data=None, columns=df.columns)
        dims = df.columns.tolist()
        dims.remove('M')
        result_df = multiple_tuple_optimization(df, dims, result_df)
    return result_df


def multiple_tuple_optimization(df, dims, result_df):
    if len(dims) == 0:
        return result_df
    else:
        current_dim = dims[0]
        value_of_dim = df[current_dim]
        # for each distinct value v in dim1
        for data in set(value_of_dim):
            origin_data = helper.select_data(df, 0, data)
            result_df = result_df.append(origin_data, ignore_index=True)
            # print(result_df)
            slice_data = helper.slice_data_dim0(df, data)
            print("--------------slice data start -----------")
            print("data = ", data, 'len(slice_data)=', len(slice_data))
            slice_data.loc['ALL'] = slice_data.sum()
            print(slice_data)
            print("--------------slice data end ----------")


            # dims.pop(0)
            # dict = multiple_tuple_optimization(slice_data, dict)
    return result_df


if __name__ == '__main__':
    input_data = helper.read_data('./asset/a_.txt')
    output = buc_rec_optimized(input_data)
    print(output)
