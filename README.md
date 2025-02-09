```markdown
# Heart Disease Prediction Project

This project aims to predict the presence of heart disease in a patient using machine learning techniques. The model is trained using the Logistic Regression algorithm on a dataset containing various health parameters.

## Requirements

To install the required packages, run:
```bash
pip install -r requirements.txt
```

## Usage

1. **Load the dataset**: The dataset should be placed in the `datasets` directory with the name `heart.csv`.

2. **Run the Jupyter Notebook**: Open and run the `models/heart.ipynb` notebook to train the model and make predictions.

3. **Save the model**: The trained model will be saved as `heart-disease-model.sav`.

4. **Load the model**: You can load the saved model using the following code:
```python
import pickle
loaded_model = pickle.load(open('heart-disease-model.sav', 'rb'))
```

5. **Make predictions**: Use the loaded model to make predictions on new data.

## Example

To make a prediction for a new patient, use the following code:
```python
input_data = (63, 1, 3, 145, 233, 1, 0, 150, 0, 2.3, 0, 0, 1)
input_data_as_numpy_array = np.asarray(input_data)
input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if prediction[0] == 0:
    print("The person does not have a heart disease")
else:
    print("The person has heart disease")
```

## License

This project is licensed under the MIT License.
```