# Fraud Detection

This material is based on this [Alura course](https://cursos.alura.com.br/course/modelos-preditivos-dados-deteccao-fraude) using this Kaggle dataset: [Credit Card Fraud](https://www.kaggle.com/datasets/gopalmahadevan/fraud-detection-example).

The material from course is implemented using Jupyter Notebooks, but here I implement a variation using only python and a different project structure. The goal is to detect credit cards fraud.

## Dependencies

```    
pip install pandas 
pip install numpy 
pip install fastapi
pip install requests
pip install sklearn
pip install joblib
pip install pydantic
pip install "uvicorn[standard]"
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