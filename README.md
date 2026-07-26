<h1 align="center">Superstore Sales Analytics & Customer Segmentation</h1>

<p align="center">
  Python and SQL analysis of sales performance, customer behavior, and K-Means customer segments.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/SQL-336791?style=for-the-badge&logo=postgresql&logoColor=white" alt="SQL" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" alt="scikit-learn" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Analysis-Sales_%26_Customers-0284C7?style=flat-square" alt="Sales and customer analysis" />
  <img src="https://img.shields.io/badge/Model-K--Means-F59E0B?style=flat-square" alt="K-Means" />
  <img src="https://img.shields.io/badge/Status-Portfolio_Project-16A34A?style=flat-square" alt="Portfolio project" />
</p>

---

## Overview

This project explores a retail sales dataset through two complementary paths:

1. **SQL analysis** for business questions, aggregations, ranking, and customer behavior.
2. **Python analysis** for data cleaning, exploratory analysis, feature preparation, and customer segmentation with K-Means.

The repository demonstrates how analytical SQL and Python-based modeling can be combined to move from raw transactional records to interpretable business insights and customer groups.

> This is an analytical portfolio project. It is not presented as a production forecasting or real-time recommendation system.

---

## Questions Explored

The analysis covers questions such as:

- How are sales distributed across regions, categories, and subcategories?
- Which cities, states, products, and customer segments generate the most sales?
- How do monthly sales patterns change over time?
- Which customers place recurring orders?
- How does shipping time vary by region?
- Can customers be grouped by sales value, order frequency, and behavioral characteristics?

---

## Analytical Workflow

```text
Superstore dataset
       │
       ▼
Data inspection
       │
       ▼
Cleaning and standardization
       │
       ├───────────────┐
       ▼               ▼
SQL analysis      Python EDA
       │               │
       │               ▼
       │         Feature engineering
       │               │
       │               ▼
       │         Standardization
       │               │
       │               ▼
       └────────► K-Means clustering
                       │
                       ▼
            Customer segment output
```

---

## SQL Analysis

The SQL portion demonstrates:

- aggregations by region, category, city, and customer;
- joins and subqueries;
- Common Table Expressions;
- temporary tables;
- ranking with window functions;
- monthly sales analysis;
- shipping-efficiency calculations;
- recurring-customer identification;
- percentage contribution by category.

Relevant files include:

- [`sales_sql_analysis.sql`](./sales_sql_analysis.sql)
- [`superstore_sales.sql`](./superstore_sales.sql)

---

## Python Analysis

The Python workflow demonstrates:

- CSV ingestion with date parsing;
- duplicate and missing-value handling;
- column-name standardization;
- descriptive statistics;
- regional, product, monthly, and category analysis;
- customer-level aggregation;
- categorical encoding;
- numerical feature scaling;
- elbow-method exploration;
- K-Means clustering;
- cluster visualization;
- export of segmented customer data.

### Segmentation features

Customers are aggregated using characteristics represented in the project, including:

- total sales;
- number of unique orders;
- average order frequency;
- customer segment category.

The model assigns each customer to one of four clusters after feature preparation and scaling.

---

## Repository Contents

| File | Purpose |
|---|---|
| `superstore_sales_dataset.csv` | Source retail dataset used by the Python analysis. |
| `sales_sql_analysis.sql` | Business-oriented SQL queries and analytical exercises. |
| `superstore_sales.sql` | Table definition used for the sales dataset. |
| `customer_clusters_updated.csv` | Customer-level output with assigned cluster labels. |
| Python analysis script | Data cleaning, exploratory analysis, feature engineering, and K-Means clustering. |

---

## Technologies

| Area | Technologies |
|---|---|
| Data analysis | Python, Pandas |
| Visualization | Matplotlib, Seaborn |
| Machine learning | scikit-learn, K-Means |
| SQL analysis | SQL, CTEs, window functions, temporary tables |
| Data preparation | StandardScaler, OneHotEncoder |

---

## Reproducing the Analysis

Create a Python environment and install the libraries used by the analysis:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install pandas matplotlib seaborn scikit-learn
```

Keep `superstore_sales_dataset.csv` in the repository root before running the Python analysis script.

For the SQL portion, create the target table using `superstore_sales.sql`, load the dataset into your SQL environment, and then execute selected queries from `sales_sql_analysis.sql`.

> Database names and SQL dialect details may need adjustment for the local SQL engine being used.

---

## Engineering and Analytical Skills Demonstrated

- Translating business questions into SQL queries.
- Combining Python and SQL in one analytical workflow.
- Cleaning and standardizing transactional data.
- Designing customer-level analytical features.
- Applying unsupervised learning to customer segmentation.
- Exporting analysis-ready outputs for downstream use.
- Communicating project scope and limitations clearly.

---

## Limitations

- The project uses a static portfolio dataset.
- Cluster labels are analytical groupings and require business interpretation.
- The code does not currently expose a production API or automated pipeline.
- Reproducibility would benefit from automated tests, a dependency lockfile, and generated visual outputs committed as documentation assets.

---

## Roadmap

- Add a formal `requirements.txt`.
- Refactor the Python analysis into reusable modules.
- Add automated data-quality checks.
- Save charts under a documented `assets/` directory.
- Add cluster profiles and business-friendly segment names.
- Add tests for data preparation and feature calculations.
- Create a reproducible command-line entry point.

---

## Author

**Vinicios Falqueiro Reis** — Data Engineer focused on cloud data platforms, analytics pipelines, and reliable data products.

[LinkedIn](https://www.linkedin.com/in/vfalqueiroreis/) · [GitHub](https://github.com/vfreis)