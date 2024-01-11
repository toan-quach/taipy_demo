# Pre-requisite

Make sure you have `taipy` installed in your `Python` environment. If not, you can install `taipy` by calling:

```
pip install taipy
```

# To run this exercise

To generate the template of this `taipy` application, please use:

```
taipy create --template "default"
```

To run the application, please use:

```
python main.py
```

To run the heart disease sample script, please use:

```
python sample_heart_disease_prediction_script.py
```

# Exercises

## For Core

1. How to make the `test_model_task` return the test result and store the accuracy of the model to an Excel file?
2. How to add `validate_model_task` to validate the trained model and have a split action of train-validate-test instead of just train-test?
3. How to run only `split_data_task` and `train_model_task` without running `test_model_task` and vice versa using `Sequence` in `taipy`?
4. How to leverage `taipy`'s `standalone` mode to be used in production?

## For Gui
