import numpy as np
from sklearn.cluster import KMeans
import pandas as pd

#################################
# DATA: On retire la colonne "id"
#################################
data_df = pd.read_csv("properties.csv"); #print(data_df.head(5))

ids=data_df['Id'].values;print(ids)
data_df=data_df.drop('Id',axis=1)  #;print(data_df.head(130))

data=data_df.values
#################################
# PREPARE DATA: "STANDARDIZATION"
#################################
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler(copy=True, with_mean=True, with_std=True)
# Apprentissage
data=scaler.fit_transform(data) #Apprend moyenne et ecart-type pour normalisation par [transform]

#################################
# CLUSTERING
#################################
kmeans = KMeans(n_clusters=4, n_init=10)
kmeans.fit(data)
print("Identifiants: ", ids)
print("Categories:", kmeans.labels_)

for i,c in zip(ids,kmeans.labels_):
    print("id",i," -> categorie: ",c)

new_data = np.array([[1.14, 297.9]])
new_rescaled_data = scaler.transform(new_data)
result = kmeans.predict(new_rescaled_data)
print("result : ", result)
