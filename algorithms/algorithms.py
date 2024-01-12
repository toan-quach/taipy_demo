# Copyright 2021-2024 Avaiga Private Limited
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

"""
This file is designed to contain the various Python functions used to configure tasks.

The functions will be imported by the __init__.py file in this folder.
"""

# ##################################################################################################################
# PLACEHOLDER: Put your Python functions here                                                                      #
#                                                                                                                  #
# Example:                                                                                                         #
# def place_holder_algorithm():                                                                                    #
#     pass                                                                                                         #
# Comment, remove or replace the previous lines with your own use case                                             #
# ##################################################################################################################


def split_data(heart_disease_df):
    x, y = heart_disease_df.drop("target" , axis = 1), heart_disease_df[['target']]
    
    np.random.seed(0)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)
    
    return x_train, x_test, y_train, y_test


def train_model(x_train: pd.DataFrame, y_train: pd.DataFrame):
    model = RandomForestClassifier()

    return model.fit(x_train, y_train["target"])


def test_model(model: RandomForestClassifier, x_test: pd.DataFrame, y_test: pd.DataFrame):
    model_accuracy = model.score(x_test, y_test["target"]) * 100

    print("\n\nModel Accuracy Test:" , model_accuracy , "%\n\n")
    return model_accuracy