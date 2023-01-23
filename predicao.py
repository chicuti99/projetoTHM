import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import sqlite3


conn = sqlite3.connect('registros.db')


data = pd.read_sql_query("SELECT name, time, location, flood_intensity, classification FROM flooding_data", conn)


X = data[['name', 'time', 'location', 'flood_intensity']]
y = data['classification']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)


y_pred = clf.predict(X_test)


accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)


confusion_mat = confusion_matrix(y_test, y_pred)
plt.imshow(confusion_mat, cmap='Blues', interpolation='nearest')
plt.colorbar()
tick_marks = np.arange(len(set(y)))
plt.xticks(tick_marks, set(y), rotation=45)
plt.yticks(tick_marks, set(y))
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()


conn.close()
