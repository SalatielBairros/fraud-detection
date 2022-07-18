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

## Data augmentation and balancing

The dataset used in this project it is not balanced. There is less than 0.12% of fraud transactions in the dataset. The course proposes using the method [SMOTE](https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.SMOTE.html) implemented in a data balancing library called [imbalanced-learn](https://imbalanced-learn.readthedocs.io/en/stable/index.html). This method uses KNN to create synthetic samples from the minority class, letting all classes have the same number of samples. However this method does not perform well when the data is separated in three parts: training, validation and test, where the validation dataset is separated before the balancing. The `recall` of the frauds is greatly improved, but a lot of false positives are generated, reducing significantly the precision.

Given the nature of this classification it is acceptable to have a small percentage of false positives but correctly classify the real positives, because the cost of missclassificate a fraud is higher than the cost of false positives. Nonetheless when using SMOTE the number of false positives is too high (about 7%) for a 0.9 recall in Fraud. The problem is that the SMOTE creates too many fraud samples because the minority class is very small.

For this reason, I decided to use another algorithm called [ADASYN (Adaptive Synthetic)](https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.ADASYN.html), also implemented in [imbalanced-learn](https://imbalanced-learn.readthedocs.io/en/stable/index.html). This method is similar to SMOTE, but can generate a differente number of samples for each class and allows me to inform a proportion of samples to create for the minority class. The proportion used in this project was 0.1, almost 10 times the number of real fraud samples. With this method, the number of false positives was reduced to less then 3% with the same 0.9 fraud recall.