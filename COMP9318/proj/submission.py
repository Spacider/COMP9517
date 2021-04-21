import math

import numpy as np
import pandas as pd
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error


# Project-Part1
def predict_COVID_part1(svm_model, train_df, train_labels_df, past_cases_interval,
                        past_weather_interval, test_feature):
    train_features = []
    N = 30  # maximum allowed values of the features from the past
    train_size = len(train_df)
    weather_features = ['max_temp', 'max_dew', 'max_humid']
    for index in range(N, train_size):
        # [max_temp, max_dew, max_humid, past_cases]
        # count weather feature
        tmp_data = []
        weather_df = train_df.iloc[index - past_weather_interval:index]
        for features in weather_features:
            new_weather = weather_df[features].values.tolist()
            for weather in new_weather:
                tmp_data.append(weather)
        # count cases features
        cases_df = train_df.iloc[index - past_cases_interval:index]
        new_cases = cases_df['dailly_cases'].values.tolist()
        for cases in new_cases:
            tmp_data.append(cases)
        train_features.append(tmp_data)

    # derive labels
    ground_truth = train_labels_df.iloc[N:train_size]
    train_labels = ground_truth['dailly_cases'].values.tolist()
    svm_model.fit(train_features, train_labels)

    predict_feature = []
    # weather_features = ['max_temp', 'max_dew', 'max_humid']
    for features in weather_features:
        for i in range(past_weather_interval, 0, -1):
            tmp = test_feature[features + '-' + str(i)]
            predict_feature.append(tmp)

    for i in range(past_cases_interval, 0, -1):
        tmp = test_feature['dailly_cases-' + str(i)]
        predict_feature.append(tmp)

    res = svm_model.predict([predict_feature])
    return math.floor(res[0])


# Project-Part2
def predict_COVID_part2(train_df, train_labels_df, test_feature):
    temp_model = SVR()
    temp_model.set_params(**{'kernel': 'rbf', 'degree': 1, 'C': 6000,
                            'gamma': 'scale', 'coef0': 0.0, 'tol': 0.001, 'epsilon': 13})

    humid_model = SVR()
    humid_model.set_params(**{'kernel': 'poly', 'degree': 1, 'C': 6000,
                             'gamma': 'scale', 'coef0': 0.6, 'tol': 0.001, 'epsilon': 13})

    temp_features = ['min_temp', 'max_temp', 'max_humid', 'min_humid']
    humid_features = ['min_dew', 'max_pressure']

    res1 = train_and_get_results(train_df, train_labels_df, temp_model, temp_features, test_feature, 95)
    res2 = train_and_get_results(train_df, train_labels_df, temp_model, humid_features, test_feature, 180)
    # print(res1)
    # print(res2)
    # print("--------------")

    res = (res1[0] + res2[0]) / 2
    return math.floor(res)


def train_and_get_results(train_df, train_labels_df, model, weather_features, test_feature, Start_index):
    past_cases_interval = 18
    past_weather_interval = 27
    train_features = []
    train_size = len(train_df)
    train_size = train_size - 5
    for index in range(Start_index, train_size):
        # [max_temp, max_dew, max_humid, past_cases]
        # count weather feature
        tmp_data = []
        weather_df = train_df.iloc[index - past_weather_interval:index]
        for features in weather_features:
            new_weather = weather_df[features].values.tolist()
            for weather in new_weather:
                tmp_data.append(weather)
        # count cases features
        cases_df = train_df.iloc[index - past_cases_interval:index]
        new_cases = cases_df['dailly_cases'].values.tolist()
        for cases in new_cases:
            tmp_data.append(cases)
        train_features.append(tmp_data)

    # derive labels
    ground_truth = train_labels_df.iloc[Start_index:train_size]
    train_labels = ground_truth['dailly_cases'].values.tolist()
    model.fit(train_features, train_labels)

    predict_feature = []
    # weather_features = ['max_temp', 'max_dew', 'max_humid']
    for features in weather_features:
        for i in range(past_weather_interval, 0, -1):
            tmp = test_feature[features + '-' + str(i)]
            predict_feature.append(tmp)

    for i in range(past_cases_interval, 0, -1):
        tmp = test_feature['dailly_cases-' + str(i)]
        predict_feature.append(tmp)

    return model.predict([predict_feature])