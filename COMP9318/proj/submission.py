import math

import numpy as np
import pandas as pd
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error


# Project-Part1
def predict_COVID_part1(svm_model, train_df, train_labels_df, past_cases_interval,
                        past_weather_interval, test_feature):
    train_features = []
    train_labels = []
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
    pass


