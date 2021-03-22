## import modules here 
import pandas as pd
import numpy as np
import helper


################### Question 1 ###################

def buc_rec_optimized(df):

    result_df = pd.DataFrame(data=None, columns=df.columns)
    columns = []

    if len(df) == 1:
        # single-tuple optimization
        single_tuple_optimization(df, result_df, columns)
    else:
        # multiple tuple optimization
        result_df = buc(df, result_df, columns)
    # result_df.index = range(len(result_df))
    return result_df


def copy_list(list):
    new_list = []
    for i in list:
        new_list.append(i)
    return new_list


def single_tuple_optimization(df, result_df, columns):
    all_possible = []

    if len(df.columns) > 1:
        for index in range(df.shape[1] - 1):
            tmp_list = []
            # two possibles 'ALL' or data
            single_possible = [df.iloc[0, index], 'ALL']
            if len(all_possible):
                for tmp in all_possible:
                    for single in single_possible:
                        new_tmp = copy_list(tmp)
                        new_tmp.append(single)
                        tmp_list.append(new_tmp)
                # update the all possibles list
                all_possible = tmp_list
            else:
                # if all possibles list is empty
                # that means first time
                # need to import first data and 'ALL'
                all_possible = [[_] for _ in single_possible]
    else:
        all_possible = [columns]
        columns = []
    for possible in all_possible:
        # add M to the data
        possible.append(df.iloc[0, df.shape[1] - 1])
        new_columns = copy_list(columns)
        new_columns.extend(possible)
        # add lines to dataframe
        result_df.loc[len(result_df)] = new_columns


def buc(df, result_df, columns):
    dims = len(df.columns)  # len of dims

    if len(df) == 1:
        single_tuple_optimization(df, result_df, columns)
    else:
        if dims == 1:
            df_sum = sum(helper.project_data(df, 0))
            columns.append(df_sum)
            result_df.loc[len(result_df)] = columns
        else:
            dim_values = set(helper.project_data(df, 0))
            tmp = copy_list(columns)
            for value in dim_values:
                tmp_column = copy_list(tmp)
                slice_data = helper.slice_data_dim0(df, value)
                tmp_column.append(value)
                buc(slice_data, result_df, tmp_column)

            sub_data = helper.remove_first_dim(df)
            tmp_column = copy_list(tmp)
            tmp_column.append('ALL')
            buc(sub_data, result_df, tmp_column)

    return result_df
