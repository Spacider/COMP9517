## import modules here 
import pandas as pd
import numpy as np
import helper


################### Question 1 ###################

def buc_rec_optimized(df):

    # df = helper.project_data(df, 1) 0 选择第一列 1选择第二列
    # df = helper.select_data(df, 0, 1) 选择第一列值为 1 的全部数据
    # df = helper.slice_data_dim0(df, 1) # 选择第1列值为1的剩余数据
    result_df = pd.DataFrame(data=None, columns=df.columns)

    if len(df) == 1111111111111111:
        # single-tuple optimization
        pass
    else:
        # multiple tuple optimization
        result_df = multiple_tuple_optimization(df, result_df)
    result_df.index = range(len(result_df))
    return result_df


def multiple_tuple_optimization(df, result_df):
    dims = df.shape[1]
    if len(dims) == 0:
        return result_df
    else:
        current_dim = dims[0]  # 'A'
        value_of_dim = helper.project_data(df, 0)
        # for each distinct value v in dim1

        for dim in dims:
            print("dim:", dim)
            for data in set(value_of_dim):

                slice_data = helper.slice_data_dim0(df, data)
                print(slice_data)

                result_df = multiple_tuple_optimization(slice_data, result_df)

        # else:
        #     tmp_data = df.copy()
        #     result_df = processing_data(tmp_data, current_dim, None, result_df)
        # print("--------------slice data start -----------")
        # print(slice_data)
        # print("--------------slice data end ----------")
        # print("--------------result_df start -----------")
        # print(result_df)
        # print("--------------result_df end -----------")
        # dims.remove(current_dim)
        # data = df.drop(columns=current_dim)
        # result_df = multiple_tuple_optimization(data, dims, result_df)
        return result_df


if __name__ == '__main__':
    input_data = helper.read_data('./asset/c_.txt')
    output = buc_rec_optimized(input_data)
    print(output)
