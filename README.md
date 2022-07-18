# Fraud Detection

This material is based on this [Alura course](https://cursos.alura.com.br/course/modelos-preditivos-dados-deteccao-fraude) using this Kaggle dataset: [Credit Card Fraud](https://www.kaggle.com/datasets/gopalmahadevan/fraud-detection-example) that is a part of [PaySim Dataset](https://www.researchgate.net/publication/313138956_PAYSIM_A_FINANCIAL_MOBILE_MONEY_SIMULATOR_FOR_FRAUD_DETECTION).

The material from course is implemented using Jupyter Notebooks, but here I implement a variation using only python and a different project structure. The goal is to detect credit cards fraud.

## Dependencies

```    
pip install pandas 
pip3 install ipywidgets
pip install pandas-profiling
pip install numpy 
pip install fastapi
pip install requests
pip install sklearn
pip install joblib
pip install pydantic
pip install "uvicorn[standard]"
pip install -U imbalanced-learn
```

## Running de Code

There is two ways to run the code: (1) running the recommendations on the console and (2) using a FastAPI server.

(1)
```bash
python src/console_main.py
```

(2)
```bash
uvicorn main:app --reload
```

> The `reload` option is used to reload the code when it changes and should be used only when developing.

For te API, the Documentation can be found at [http://localhost:8000/docs](http://localhost:8000/docs).

## Model evaluations

All the implemented models of this project uses the same evaluation metrics. The metrics are:

* **Accuracy**: The percentage of correct predictions.
* **Precision**: The percentage of correct positive predictions.
* **Recall**: Proportion of positive predictions that are correct over the total number of positive samples.
* **F1**: The harmonic mean of precision and recall.
* **AUC**: Area under the ROC curve. The ROC curve is the receiver operating characteristic curve. It is a plot of the sensitivity and specificity of the classifier.
* **Confusion Matrix**: A table that shows the number of correct and incorrect predictions for each class.