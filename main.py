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

import taipy as tp
from taipy.gui import notify
from configuration.config import heart_disease_scenario_config

scenario = None
data_node = None
job = None

# can also be an exercise
def notify_from_submissions(state, _, details):
    submission_status = details.get('submission_status')

    if submission_status == 'COMPLETED':
        # Add additional actions here, like updating the GUI or logging the completion.
        notify(state, 'success', 'Completed!')

    elif submission_status == 'FAILED':
        # Handle failure, like sending notifications or logging the error.
        notify(state, 'error', 'FAILED!')


page = """
# Taipy Heart Disease Prediction

<|navbar|>
"""

scenario_md = """
<|layout|
<|{scenario}|scenario_selector|>

<|{scenario}|scenario|on_submission_change=notify_from_submissions|>
|>

<|{scenario}|scenario_dag|>
"""

data_node_md = """
<|layout|

<|{data_node}|data_node_selector|>

<|{data_node}|data_node|>

|>
"""

job_md = """
<|{job}|job_selector|>
"""

core = tp.Core()
gui = tp.Gui(page=page)
gui.add_page("scenario", scenario_md)
gui.add_page("data_node", data_node_md)
gui.add_page("job_selector", job_md)

if __name__ == "__main__":
    tp.run(core, gui, title="Heart Disease Prediction")
