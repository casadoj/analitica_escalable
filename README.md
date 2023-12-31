# PEC2: Analítica escalable

***Autor**: Jesús Casado Rodríguez*<br>
***Fecha**: 17-06-2023*<br>

PEC 2 de la asignatura "Analítica escalable" del Máster en Ciencia de Datos de la Universidad de Alcalá de Henares.

## Introducción

He creado una API web que estima el coste del seguro sanitario en función de ciertas variables introducidas por el usuario: edad, sexo, índice de masa corporal, número de hijos, si es fumador o no, y la zona de EEUU en la que reside. Esta API web, a su vez, utiliza la librería Python [insurance](https://pypi.org/project/insurance/0.0.5/), disponible en PyPI. 

## Algoritmo de predicción

El algoritmo de _machine learning_ que predice los costes sanitarios se basa en 6 variables:

* _age_: de tipo entero.
* _sex_: un texto que puede tomar los valores _male_ o _female_.
* _bmi_: un número real que indica el índice de masa corporal.
* _children_: número entero correspondiente al número de hijos de la persona.
* _smoker_: un texto que puede tomar los valores _yes_ o _no_.
* _region_: un texto que puede tomar los valores _northeast_, _southeast_, _southwest_ o _northwest_.

Las variables predictoras son preprocesadas en función de si son categóricas o numéricas. Las variables numéricas (_age_ y _bmi_) se escalan mediante el algoritmo [`StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html) de Scikit-learn con el objetivo es que todas estén en un mismo orden de magnitud. Las variables categóricas (_sex_, _children_, _smoker_ y _region_) se tranforman en numéricas mediante la función [`OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder) de Scikit-learn. Como algoritmo de regresión he escogido Stochastic Gradient Descent ([`SGDRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor) en Scikit-learn). 

He creado un `Pipeline` que incluye el propresado de los datos y el algoritmo de regresión. Este `Pipeline` se entrena en una [muestra de datos de entrenamiento](https://github.com/casadoj/analitica_escalable/blob/main/library/my_model/datasets/train.csv), y se evalúa en una [muestra de validación](https://github.com/casadoj/analitica_escalable/blob/main/library/my_model/datasets/test.csv). El [modelo entrenado](https://github.com/casadoj/analitica_escalable/tree/main/library/my_model/trained_models) se guarda en un archivo Pickle.

El análisis exploratorio de los datos y el desarrollo del `Pipeline` lo he hecho en el _notebook_ [_train_pipeline.ipynb_](https://github.com/casadoj/analitica_escalable/blob/main/notebook/train_pipeline.ipynb). Para ello creé un entorno de Conda que se puede replicar con el archivo [environment.yml](https://github.com/casadoj/analitica_escalable/blob/main/env/environment.yml).

## Librería PyPI

Todo el proceso antes explicado ha sido empaquetado en forma de librería Python llamada [insurance](https://pypi.org/project/insurance/0.0.5/) disponible en PyPI. Todos los archivos necesarios para empaquetar el algoritmo están en el directorio [Library](https://github.com/casadoj/analitica_escalable/blob/main/library/).

El comando para instalar la librería con `pip` es el siguiente:

```pip install insurance==0.0.5```

## API web

He creado una imagen Docker con la API web. Todos los archivos necesarios para crear esta imagen están en el directorio [API](https://github.com/casadoj/analitica_escalable/blob/main/API/) del respositorio. Son los siguientes:

* _Dockerfile_: contiene las instrucciones necesarias para construir la imagen. Se crea un entorno Python, se copian los archivos necesarios al directorio `./app`, se establece este directorio como el de trabajo, se instalan las librerías especificadas en _requirements.txt_, se expone el puerto 5000 y se ejecuta el archivo _app.py_, que contiene el modelo de predicción.
* _requiremensts.txt_: especifica las librerías Python requeridas para poder ejecutar el modelo. Entre ellas está la librería que se creó en la sección anterior: `insurance==0.0.5`.
* _app.py_: es el modelo a ejecutar. Se utiliza la librería `Flask` para recibir la información introducida por el usuario de la web. Estos datos se meten en un _DataFrame_ de Pandas, que a su vez es el dato de entrada para hacer la predición (función `make_prediction`). Esta función proviene de la librería `insurance` creada en el apartado anterior.
* _template/website.html_: es la plantilla que define el aspecto de la API web.

El siguiente comando permite importar la imagen con la API web desde DockerHub:

```docker pull chuscas88/insurance:0.0.5```

## Testeo del paquete con [`tox`](https://tox.wiki/en/latest/)

No he podido hacer el testeo del paquete en `tox` porque hay algún problema de configuración en mi PC. Cuando ejecuto el comando `tox -r` obtengo el error del archivo [_error_tox.txt_](https://github.com/casadoj/analitica_escalable/blob/main/library/error_tox.txt). He intentado crear un entorno de Conda nuevo con una nueva instalación de `OpenSSL`, pero el error persiste, incluso en ejemplos tan sencillos como el de este [tutorial](https://christophergs.com/python/2020/04/12/python-tox-why-use-it-and-tutorial/).
