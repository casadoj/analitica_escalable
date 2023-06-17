# PEC2: Analítica escalable

***Autor**: Jesús Casado Rodríguez*<br>
***Fecha**: 17-06-2023*<br>

PEC 2 de la asignatura "Analítica escalable" del Máster en Ciencia de Datos de la Universidad de Alcalá de Henares.

## Introducción

He creado una API web que estima el coste del seguro sanitario en función de ciertas variables introducidas por el usuario: edad, sexo, índice de masa corporal, número de hijos, si es fumador o no, y la zona de EEUU en la que reside. Esta API web, a su vez, utiliza la librería Python [insurance](https://pypi.org/project/insurance/0.0.5/), disponible en PyPI. 

## Algoritmo de predicción

El algoritmo de _machine learning_ que predice los costes sanitarios se basa en 6 variables:

* `age`: de tipo entero.
* `sex`: un texto que puede tomar los valores _male_ o _female_.
* `bmi`: un número real que indica el índice de masa corporal.
* `children`: número entero correspondiente al número de hijos de la persona.
* `smoker`: un texto que puede tomar los valores _yes_ o _no_.
* `region`: un texto que puede tomar los valores _northeast_, _southeast_, _southwest_ o _northwest_.

Las variables predictoras son preprocesadas en función de si son categóricas o numéricas. Las variables numéricas (`age` y `bmi`) se escalan mediante el algoritmo [`StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html) de Scikit-learn con el objetivo es que todas estén en un mismo orden de magnitud. Las variables categóricas (`sex`, `children`, `smoker` y `region`) se tranforman en numéricas mediante la función [`OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder) de Scikit-learn. Como algoritmo de regresión he escogido Stochastic Gradient Descent ([`SGDRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor) en Scikit-learn). 

He creado un `Pipeline` que incluye el propresado de los datos y el algoritmo de regresión. Este `Pipeline` se entrena en una [muestra de datos de entrenamiento](https://github.com/casadoj/analitica_escalable/blob/main/library/my_model/datasets/train.csv), y se evalúa en una [muestra de validación](https://github.com/casadoj/analitica_escalable/blob/main/library/my_model/datasets/test.csv). El [modelo entrenado](https://github.com/casadoj/analitica_escalable/tree/main/library/my_model/trained_models) se guarda en un archivo Pickle.

## Librería PyPI

Todo el proceso antes explicado ha sido empaquetado en forma de librería Python llamada [insurance](https://pypi.org/project/insurance/0.0.5/) disponible en PyPI. El comando para instalar la librería con `pip` es el siguiente:

```pip install insurance==0.0.5```

## Importar imagen Docker

El comando para importar la imagen Docker con la API web es el siguiente:

```docker pull chuscas88/insurance:0.0.5```

