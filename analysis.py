import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, OneHotEncoder


# 1 - loading dataset [date formet needs to parse]
df = pd.read_csv('superstore_sales_dataset.csv', parse_dates=['Order Date', 'Ship Date'], dayfirst=True)
print(df.head(2))

# exploring dataset 
print(df.info())
print(df.isnull().sum())

# 2 - data cleaning | 'postal code' has 11 missing values
df.drop_duplicates(inplace=True)
df.fillna(0, inplace=True)

# validating if worked [it does]
print(df.isnull().sum())

# standardization (now we replace " " with "_")
df.columns = df.columns.str.replace(" ", "_")
print(df.info()) # validating

# 3 - starting statistical analysis
print(df.describe()) # segment shows to be promissing
print(df['Segment'].value_counts())

# 4 - exploratory data analysis
# sales by region
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=True)
region_sales.plot(kind='bar', title='Sales by Region', color= 'Skyblue')
plt.ylabel('Total Sales')
# plt.show()

# top sold products
top_products = df.groupby('Product_Name')['Sales'].sum().sort_values(ascending=True)
top_products.plot(kind='barh', title='Top 10 Best-Selling Products', color='Orange')
plt.xlabel('Total Sales')
# plt.show()

# monthly sales
df['Month'] = df['Order_Date'].dt.month
monthly_sales = df.groupby('Month')['Sales'].sum()
sns.lineplot(x=monthly_sales.index, y=monthly_sales.values, markers='o')
plt.title('Monthly Sales Trends')
plt.xlabel('Month')
plt.ylabel('Total Sales')
# plt.show()

# profit by category
category_profit = df.groupby('Category')['Sales'].sum()
category_profit.plot(kind='pie', autopct='%1.1f%%', title='Sales Distribution by Category')
plt.ylabel("")
 # plt.show()

## Clustering ##

# data formatting
df['Order_Date'] = pd.to_datetime(df['Order_Date'], format='%d/%m/y%')
df['Ship_Date'] = pd.to_datetime(df['Ship_Date'], format='%d/%m/y%')

# Preprocessing: aggregate data by 'Customer ID'
customer_data = df.groupby('Customer_ID').agg({
    'Sales' : 'sum', # sales by customer
    'Order_ID' : 'nunique', # number of unique orders
    'Order_Date' : lambda x: (x.max() - x.min()).days / (len(x) + 1),
    'Segment' : 'first'
}).reset_index()

# rename column to clarity
customer_data.rename(columns={
    'Order_ID' : 'Num_Orders',
    'Order_Date' : 'Avg_Order_Frequency'
}, inplace=True)

# Encode the categorical 'Segment' feature
encoder = OneHotEncoder(sparse_output=False, drop='first')
encoded_segment = encoder.fit_transform(customer_data[['Segment']])
encoded_segment_df = pd.DataFrame(encoded_segment, columns=encoder.get_feature_names_out(['Segment']))
customer_data = pd.concat([customer_data, encoded_segment_df], axis=1)

# scale numeric features
features = ['Sales', 'Num_Orders', 'Avg_Order_Frequency'] + list(encoded_segment_df.columns)
scaler = StandardScaler()
scaled_features = scaler.fit_transform(customer_data[features])

# elbow method to optimize number of clusters
sse = []
for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_features)
    sse.append(kmeans.inertia_)

# plot elbow curve
plt.figure(figsize=(8, 5))
plt.plot(range(2, 11), sse, marker='o', linestyle='--')
plt.title('Elbow Method for Optimal Clusters')
plt.xlabel('Number of Clusters')
plt.ylabel('Sum of Squared Error (SSE)')
# plt.grid()
# plt.show()

# applying k-means
optimal_k = 4
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
customer_data['Cluster'] = kmeans.fit_predict(scaled_features)

# analyzing each cluster
cluster_summary = customer_data.groupby('Cluster').mean(numeric_only=True)
print(cluster_summary)

# visualize clusters using pair plots
sns.pairplot(customer_data, vars=features, hue='Cluster', palette='viridis', diag_kind='kde')
plt.suptitle('Cluster Pairplot', y=1.02)
plt.show()

# save results for further analysis
customer_data.to_csv('customer_clusters_updated.csv', index=False)
