import pandas as pd
from sklearn.preprocessing import StandardScaler
#from sklearn.cluster import KMeans
from sklearn import decomposition
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# LOAD THE DATA
data = pd.read_csv('NC_001416.aa', sep='\t')

# STRIP OUT ONLY THE COUNTS
dat = data[list("ARNDCEQGHILKMFPSTWYV")]

# DIVIDE BY THE ROW SUMS TO GET THE FREQUENCY
dat_norm = dat.div(dat.sum(axis=1), axis=0)

# SCALE THE VALUES
dat_scaled = StandardScaler().fit_transform(dat_norm)

# CLASSIFY EACH ROW USING KMEANS
#clust = KMeans(n_clusters=2).fit(dat_scaled).labels_

# CALCULATE THE PRINCIPLE COMPONENTS
pca = decomposition.PCA(n_components = 2, svd_solver='full').fit(dat_scaled)
dat_pca = pca.transform(dat_scaled)

x_vector = pca.components_[0]
y_vector = pca.components_[1]

# PLOT
fig, ax = plt.subplots()
colors = {'noncoding':'#F2766E', 'coding':'#3CC9CF'}

df = pd.DataFrame({'X':dat_pca[:,0],'Y':dat_pca[:,1],'TYPE':data.TYPE})

ax.scatter(df['X'], df['Y'], label=df['TYPE'], c=df['TYPE'].apply(lambda x: colors[x]), marker='.', linewidths=0.0, alpha=0.9, zorder=5)

for i in range(len(x_vector)):
    x = (1.2*x_vector[i]*max(dat_pca[:,0]))
    y = (1.2*y_vector[i]*max(dat_pca[:,0]))
    plt.arrow(0, 0, x, y,  color='black', width=0.00005, zorder=10)
    plt.text(x*1.1, y*1.1, dat.columns[i], color='black', zorder=10)

# LEGEND
plt.legend(handles=[mpatches.Patch(color=col, label=str(lab)) for lab,col in colors.items()])

ax.set_title('amino-acid frequency of potential ORFs from Lambda phage')
ax.set(xlabel='PC1', ylabel='PC2')
#plt.show()
fig.set_size_inches(8, 8)
fig.savefig('figure2.png', dpi=100, format='png')

