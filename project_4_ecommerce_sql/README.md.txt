Project 4: E-commerce Sales & Marketing SQL Analysis

Project Overview

This project demonstrates how SQL can be used to analyze e-commerce sales and customer behavior. 
The main goal was to extract actionable insights from sales and marketing data, focusing on revenue trends, customer segmentation, and marketing channel performance.

The project workflow included:

1. Loading raw CSV datasets into SQLite.
2. Performing SQL queries to calculate metrics such as revenue, customer behavior, and marketing effectiveness.
3. Exporting query results as CSV files for further analysis.
4. Creating a Power BI dashboard to visualize key insights for business decision-making.

---

Datasets

| File            | Rows  | Description                                                    |
| --------------- | ----- | -------------------------------------------------------------- |
| `customers.csv` | 500   | Customer details including demographics and registration info  |
| `orders.csv`    | 2,000 | Order-level sales data including date, amount, and customer ID |
| `marketing.csv` | ~400  | Marketing campaigns and channel engagement data                |

---

Tools & Technologies

* SQLite – For querying and aggregating data
* Power BI – For visualizing sales trends and customer behavior
* CSV / Excel – For initial data storage and preparation

---

SQL Analysis & Outputs

The following SQL queries were executed, with results exported as CSVs for Power BI:

| Query / Analysis                               | Output CSV                          |
| ---------------------------------------------- | ----------------------------------- |
| Customer overview (demographics & total spend) | `customer_overview.csv`             |
| Revenue by region                              | `revenue_by_region.csv`             |
| Monthly revenue trend                          | `monthly_revenue_trend.csv`         |
| Repeat vs new customers                        | `repeat_vs_new_customers.csv`       |
| Top customers by total spend                   | `top_customers.csv`                 |
| Marketing channel performance                  | `marketing_channel_performance.csv` |

These CSVs formed the foundation of the Power BI dashboard, providing a visual summary of e-commerce performance.

---

Power BI Dashboard

The dashboard highlights:

* Revenue trends over time
* Regional sales comparisons
* Customer segmentation: repeat vs new
* Marketing channel ROI and effectiveness
* Top customers by purchase value

It was designed to provide clear, actionable insights for e-commerce strategy and marketing optimization.

---

Key Takeaways

* SQL is highly effective for cleaning, aggregating, and preparing datasets for visualization.
* Combining SQL analysis with Power BI enables interactive exploration of sales and customer insights.
* Understanding customer behavior and marketing performance helps drive data-informed business decisions.


