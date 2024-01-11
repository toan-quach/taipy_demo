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

"""
Contain the application's configuration including the scenario configurations.

The configuration is run by the Core service.
"""

from algorithms.algorithms import split_data, train_model, test_model

from taipy import Config

# #############################################################################
# PLACEHOLDER: Put your application's configurations here                     #
#                                                                             #
# Example:                                                                    #
# scenario_config = Config.configure_scenario("placeholder_scenario", [])     #
# Comment, remove or replace the previous lines with your own use case        #
# #############################################################################

heart_disease_dn_config = Config.configure_csv_data_node("heart_disease_data", "data/heart-disease-dataset.csv")
x_train_dn_config = Config.configure_csv_data_node("x_train_dn", "data/x_train.csv")
y_train_dn_config = Config.configure_csv_data_node("y_train_dn", "data/y_train.csv")
x_test_dn_config = Config.configure_csv_data_node("x_test_dn", "data/x_test.csv")
y_test_dn_config = Config.configure_csv_data_node("y_test_dn", "data/y_test.csv")
model_dn_config = Config.configure_pickle_data_node("model", "data/model.pickle")

split_data_task_config = Config.configure_task("split_data", split_data, [heart_disease_dn_config], [x_train_dn_config, x_test_dn_config, y_train_dn_config, y_test_dn_config], skippable=True, )
train_model_task_config = Config.configure_task("train_model", train_model, [x_train_dn_config, y_train_dn_config], [model_dn_config])
test_model_task_config = Config.configure_task("test_model", test_model, [model_dn_config, x_test_dn_config, y_test_dn_config])

heart_disease_scenario_config = Config.configure_scenario("training_scenario", [split_data_task_config, train_model_task_config, test_model_task_config])
heart_disease_scenario_config.add_sequences({
    "train_model": [split_data_task_config, train_model_task_config],
    "test_model": [test_model_task_config],
})
