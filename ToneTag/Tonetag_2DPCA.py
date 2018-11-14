
import pandas as pd
import numpy as np
import random as rd
from sklearn.decomposition import PCA
from sklearn import preprocessing
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

dataset = pd.read_csv('tonetag_trial_data.csv')
print(np.shape(dataset))
data = dataset.iloc[:11, 2:42]


print(data.head())
print(data.shape)


# First center and scale the data
scaled_data = preprocessing.scale(data)
#scaled_data = StandardScaler().fit_transform(data)
print (scaled_data)
pca = PCA(n_components=10)  # create a PCA object
pca.fit(scaled_data)  # do the math
pca_data = pca.transform(scaled_data)  # get PCA coordinates for scaled_data


# The following code constructs the Scree plot
per_var = np.round(pca.explained_variance_ratio_ * 100, decimals=1)
labels = ['PC' + str(x) for x in range(1, len(per_var) + 1)]


plt.bar(x=range(1, len(per_var) + 1), height=per_var, tick_label=labels)
plt.ylabel('Percentage of Explained Variance')
plt.xlabel('Principal Component')
plt.title('Scree Plot')
plt.show()

Information = ['Information' + str(i) for i in range(1)]
Not_Information = ['Not_Information' + str(i) for i in range(0, 10)]

pca_df = pd.DataFrame(pca_data, index=[*Information, *Not_Information], columns=labels)
print(pca_df)

classes = dataset.iloc[:11,-1].values
#print (z)
colors = np.array(["red", "blue"])
clusters = np.array(["Information", "Not_Information"])
plt.scatter(pca_df.PC1, pca_df.PC2, c=colors[classes], label = True)

recs = []
for i in range(0,len(colors[classes])):
        recs.append(mpatches.Rectangle((0,0),1,1,fc=colors[classes][i]))
plt.legend(recs, clusters, loc = 'lower right')
plt.title('ToneTag_Frequency')
plt.xlabel('PC1 - {0}%'.format(per_var[0]))
plt.ylabel('PC2 - {0}%'.format(per_var[1]))


#for sample in pca_df.index:
 #   plt.annotate(sample, (pca_df.PC1.loc[sample], pca_df.PC2.loc[sample]))

plt.show()

#plt.scatter(x,y, c=colors[z])
