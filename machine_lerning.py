{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"name":"machine_lerning.py","provenance":[],"collapsed_sections":[],"authorship_tag":"ABX9TyN2hhd4yD79DMG1C8R6B7C1"},"kernelspec":{"name":"python3","display_name":"Python 3"}},"cells":[{"cell_type":"code","metadata":{"id":"ARjQiZLHS9tA","colab_type":"code","colab":{}},"source":["\t\n","import sklearn\n"," \n","## import the iris dataset for classification\n"," \n","from sklearn import datasets\n","iris=sklearn.datasets.load_iris()\n"," \n","## print some data, to see the imported dataset\n"," \n","print(\"Printing some sample data from the iris dataset\")\n","for training_sample in list(zip(iris.data,iris.target))[:5]:\n","    print(training_sample)\n"," \n","## save the features and class\n"," \n","features=iris.data   # split iris dataset into features and iris_class\n","iris_class=iris.target  # class[X] is output corresponding to features[X]\n"," \n","## Split the dataset into training (70%) and testing (30%)\n","## Note that the shuffle parameter has been used in splitting.\n"," \n","print(\"Splitting the data into testing and training samples\")\n","from sklearn.model_selection import train_test_split\n","features_train, features_test,iris_class_train, iris_class_test = train_test_split(features,iris_class, test_size=0.33, random_state=42)\n"," \n","## data preprocessing: Before training the network we must scale the feature data\n","print(\"Data preprocessing\")\n","from sklearn.preprocessing import StandardScaler\n","scaler = StandardScaler()\n","scaler.fit(features_train)\n","features_train_scale = scaler.transform(features_train)\n","features_test_scale = scaler.transform(features_test)\n"," \n","## The MLPClassifier and MLPRegressor are sklearn implementations of NNs\n"," \n","from sklearn.neural_network import MLPClassifier\n","iterations=1000   # define the iterations for training over the dataset\n","hidden_layers=[10,10,10]  # define the layers/depth of the NN\n"," \n","mlp = MLPClassifier(hidden_layer_sizes=(hidden_layers), max_iter=iterations) \n"," \n","# an object which represents the neural network\n","# Remember to use the pre-processed data and not original values for fit()\n"," \n","mlp.fit(features_train_scale, iris_class_train)  # fit features over NN\n"," \n","## Run the test data over the network to see the predicted outcomes.\n"," \n","predicted = mlp.predict(features_test_scale)  \n"," \n","# predict over test data\n","## evaluation metrics and analysing the accuracy/output.\n","print(\"Evaluation: considering the confusion matrix\")\n","from sklearn.metrics import confusion_matrix\n","print(confusion_matrix(iris_class_test,predicted))  \n","# all non-diagonal elements are 0 if you get 100% accuracy\n"," \n","print(\"Evaluation report:\")\n","from sklearn.metrics import classification_report\n","print(classification_report(iris_class_test,predicted)) \n","#f1-score/accuracy"],"execution_count":0,"outputs":[]},{"cell_type":"code","metadata":{"id":"2n7cdflpTHU5","colab_type":"code","colab":{}},"source":["from sklearn import datasets\n","import pandas as pd\n"," \n","sangre = pd.read_csv('transfusion.data')\n","\n","dataSangre = sangre[['Recency (months)', 'Frequency (times)', 'Monetary (c.c. blood)', 'Time (months)']]\n","targetSangre = sangre[['whether he/she donated blood in March 2007']]\n","\n","## print some data, to see the imported dataset\n"," \n","print(\"Printing some sample data from the boold dataset\")\n","for training_sample in list(zip(dataSangre ,targetSangre))[:5]:\n","    print(training_sample)\n"," \n","## save the features and class\n"," \n","features = dataSangre  # split iris dataset into features and iris_class\n","iris_class = targetSangre  # class[X] is output corresponding to features[X]\n"," \n","## Split the dataset into training (70%) and testing (30%)\n","## Note that the shuffle parameter has been used in splitting.\n"," \n","print(\"Splitting the data into testing and training samples\")\n","from sklearn.model_selection import train_test_split\n","features_train, features_test,iris_class_train, iris_class_test = train_test_split(features,iris_class, test_size=0.33, random_state=42)\n"," \n","## data preprocessing: Before training the network we must scale the feature data\n","print(\"Data preprocessing\")\n","from sklearn.preprocessing import StandardScaler\n","scaler = StandardScaler()\n","scaler.fit(features_train)\n","features_train_scale = scaler.transform(features_train)\n","features_test_scale = scaler.transform(features_test)\n"," \n","## The MLPClassifier and MLPRegressor are sklearn implementations of NNs\n"," \n","from sklearn.neural_network import MLPClassifier\n","iterations=1000   # define the iterations for training over the dataset\n","hidden_layers=[10,10,10]  # define the layers/depth of the NN\n"," \n","mlp = MLPClassifier(hidden_layer_sizes=(hidden_layers), max_iter=iterations) \n"," \n","# an object which represents the neural network\n","# Remember to use the pre-processed data and not original values for fit()\n"," \n","mlp.fit(features_train_scale, iris_class_train)  # fit features over NN\n"," \n","## Run the test data over the network to see the predicted outcomes.\n"," \n","predicted = mlp.predict(features_test_scale)  \n"," \n","# predict over test data\n","## evaluation metrics and analysing the accuracy/output.\n","print(\"Evaluation: considering the confusion matrix\")\n","from sklearn.metrics import confusion_matrix\n","print(confusion_matrix(iris_class_test,predicted))  \n","# all non-diagonal elements are 0 if you get 100% accuracy\n"," \n","print(\"Evaluation report:\")\n","from sklearn.metrics import classification_report\n","print(classification_report(iris_class_test,predicted)) \n","#f1-score/accuracy"],"execution_count":0,"outputs":[]},{"cell_type":"code","metadata":{"id":"jCWBPf5dTLNo","colab_type":"code","colab":{}},"source":["from sklearn import datasets\n","from sklearn.model_selection import train_test_split\n","from sklearn.metrics import confusion_matrix\n","from sklearn.metrics import classification_report\n","from sklearn.neighbors import KNeighborsClassifier\n","\n","vino = datasets.load_wine()\n","\n","print(vino.DESCR)\n","print()\n","print(dir(vino))\n","print()\n","print(vino.data)\n","print()\n","print(vino.feature_names)\n","print()\n","print(vino.target)\n","print()\n","\n","x_train, x_test, y_train, y_test = train_test_split(vino.data, vino.target)\n","\n","print('Entrenamiento x')\n","print(x_train)\n","print()\n","print('Entrenamiento y')\n","print(y_train)\n","print()\n","print('prueba x')\n","print(x_test)\n","print()\n","print('prueba y')\n","print(y_test)\n","print()\n","\n","knn = KNeighborsClassifier(n_neighbors=1)\n","knn.fit(x_train, y_train)\n","puntaje = knn.score(x_test, y_test)\n","\n","print(x_test)\n","\n","prediccion = knn.predict(x_test)\n","results = confusion_matrix(y_test, prediccion)\n","\n","print()\n","\n","print('Matriz de confusion: ')\n","print(results)\n","\n","print('Puntaje de presicion: ', puntaje)\n","print('reporte: ')\n","\n","print()\n","\n","print(classification_report(y_test, prediccion))"],"execution_count":0,"outputs":[]},{"cell_type":"code","metadata":{"id":"VuZRbMzGTQEH","colab_type":"code","colab":{}},"source":["from sklearn import svm\n","from sklearn.model_selection import train_test_split\n","from sklearn.metrics import confusion_matrix\n","from sklearn.metrics import classification_report\n","import pandas as pd\n","\n","\n","\n","x_train, x_test, y_train, y_test = train_test_split(dataSangre, targetSangre)\n","\n","print('Entrenamiento x')\n","print(x_train)\n","print()\n","print('Entrenamiento y')\n","print(y_train)\n","print()\n","print('prueba x')\n","print(x_test)\n","print()\n","print('prueba y')\n","print(y_test)\n","print()\n","\n","classifier = svm.SVC(kernel='linear', C=0.01).fit(x_train, y_train)\n","\n","puntaje = classifier.score(x_test, y_test)\n","\n","print(x_test)\n","\n","prediccion = classifier.predict(x_test)\n","results = confusion_matrix(y_test, prediccion)\n","\n","print()\n","\n","print('Matriz de confusion: ')\n","print(results)\n","\n","print('Puntaje de presicion: ', puntaje)\n","print('reporte: ')\n","\n","print()\n","\n","print(classification_report(y_test, prediccion))"],"execution_count":0,"outputs":[]},{"cell_type":"code","metadata":{"id":"2q5FgbkVTR9R","colab_type":"code","colab":{}},"source":["import graphviz\n","from sklearn.datasets import load_iris\n","from sklearn import tree\n","\n","iris = load_iris()\n","clf = tree.DecisionTreeClassifier()\n","clf = clf.fit(iris.data, iris.target)\n","\n","dot_data = tree.export_graphviz(clf, out_file=None)\n","graph = graphviz.Sorce(dot_data)\n","graph.render(\"iris\")\n","\n","dot_data = tree.export_graphviz(clf, out_file=None, feature_names = iris.feature_names,\n","                                class_names=iris.target_names,filled = True, rounded = True,\n","                                special_characters = True)\n","\n","graph = graphviz.Sourse(dot_data)\n","graph"],"execution_count":0,"outputs":[]}]}