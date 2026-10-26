# Customer Revenue & Retention Analytics

**PostgreSQL | SQL | Python | Power BI (Planned)**

**Status:** In Progress — Raw Data Import Completed 🚧

## Overview

This project focuses on analyzing customer revenue, purchasing patterns, and retention using transaction data from a UK-based online retailer.

I started this project to practice SQL in a business setting, with a focus on how companies track revenue and understand their customers. The analysis looks at sales performance over time, customer purchasing frequency, repeat purchases, and revenue contribution from different customer groups.

The project uses PostgreSQL for data storage and SQL analysis, and Python for preparing the source data. A Power BI dashboard is also planned to present the main KPIs and findings.

The main goal is to build a structured analytics workflow, from raw data preparation to business reporting, while keeping the analysis consistent, documented, and reproducible.

## 1. Business Context

Sales figures alone do not always show how well a business is performing.

For example, revenue may increase because the business is attracting more customers, or because existing customers are buying more frequently. These situations may require different business decisions.

There is also a risk when too much revenue comes from a small number of customers.

This project focuses on four areas:

- **Revenue Performance:** How are revenue, order volume, and average order value changing?
- **Customer Behaviour:** Who are the most valuable customers, and how often do they purchase?
- **Customer Retention:** How many customers return after their first purchase, and how does retention change over time?
- **Product Performance:** Which products contribute the most revenue, and what products are purchased by returning customers?

The results will be used to explore possible improvements in customer retention and sales performance.

## 2. Dataset

**Source:** UCI Machine Learning Repository — Online Retail

**Link:** https://archive.ics.uci.edu/dataset/352/online+retail

The dataset contains historical transaction records from a UK-based online retailer. The company mainly sells gift products, and some of its customers are wholesalers.

| Attribute | Details |
|---|---|
| Dataset | Online Retail |
| Period | Dec 1, 2010 – Dec 9, 2011 |
| Records | 541,909 transaction line items |
| Source Format | Excel (.xlsx) |
| Currency | GBP |
| Database | PostgreSQL |

### Source Fields

The original dataset contains eight columns:

| Column | Description |
|---|---|
| InvoiceNo | Invoice identifier |
| StockCode | Product identifier |
| Description | Product description |
| Quantity | Quantity recorded for each item |
| InvoiceDate | Transaction date and time |
| UnitPrice | Unit price in GBP |
| CustomerID | Customer identifier |
| Country | Customer country |

Each row represents a transaction line item, not necessarily a complete order. An invoice may contain several products.

Invoice numbers beginning with `C` indicate cancellations.

The source data is kept separately from the analytical tables so that cleaning and transformations can be reviewed without changing the original records.

## 3. Data Workflow

The project follows a staged workflow:

**Step 1 — Source Data**

Download the original Excel dataset from UCI and keep a local copy.

**Step 2 — Data Preparation**

Use Python and pandas to read the Excel file, check the source structure, and export the records to CSV with column names matching the PostgreSQL schema.

**Step 3 — Raw Data Storage**

Load the CSV into PostgreSQL using DBeaver.

The raw table is designed to preserve the imported transaction records before applying business filters.

**Step 4 — Data Quality Checks**

Examine missing values, duplicate records, cancellations, invalid prices, and transaction-level consistency.

Document the issues before deciding which records should be included in the analysis.

**Step 5 — Data Modelling and Analysis**

Build analytical tables or views based on the validated data, then write SQL queries for revenue, customer behaviour, and retention.

**Step 6 — Reporting**

Use the analytical results to build a Power BI dashboard and document the main findings.

The first three stages are completed. Data quality work is the next stage.

The CSV import is currently performed through DBeaver. A scripted database import and automated validation will be added later to improve reproducibility.

## 4. Database Design

The PostgreSQL database is named `retail_analytics`.

### Current Table

**public.raw_transactions**

This table stores the imported transaction data.

| Column | PostgreSQL Type |
|---|---|
| invoice_no | VARCHAR(20) |
| stock_code | VARCHAR(30) |
| description | TEXT |
| quantity | INTEGER |
| invoice_date | TIMESTAMP |
| unit_price | NUMERIC(12,4) |
| customer_id | BIGINT |
| country | VARCHAR(100) |

No primary key has been added to the raw table because duplicate and repeated source records need to be examined first.

### Planned Analytical Model

The next stage will evaluate a relational model with the following tables:

- **customers:** Identifiable customers and customer-level attributes.
- **orders:** Invoice-level records, dates, and transaction types.
- **order_items:** Individual product lines associated with invoices.
- **products:** Product identifiers and descriptions.

The final table structure and key constraints will depend on data quality results.

In particular, invoice uniqueness, missing customer IDs, and inconsistent product descriptions must be reviewed before building relationships.

## 5. Data Quality and Validation

Data quality is an important part of this project because incorrect transaction records can affect revenue and retention calculations.

The initial audit will cover:

| Check | Purpose |
|---|---|
| Row count | Confirm all source rows were imported |
| Missing values | Identify incomplete customer, product, and transaction fields |
| Duplicate records | Check repeated records and determine whether they are valid |
| Invoice consistency | Verify invoice-level customer and date relationships |
| Negative quantities | Investigate cancellations and other adjustments |
| Non-positive prices | Identify transactions requiring further review |
| Product consistency | Check differences in descriptions for the same product code |
| Date coverage | Confirm transaction period and incomplete months |

### Initial Import Validation

The raw data import has been completed.

```text
Database: retail_analytics
Table: public.raw_transactions

Expected source rows: 541,909
Imported rows:        541,909
Result:               PASS
```

The total row count was checked using:

```sql
SELECT COUNT(*) AS total_rows
FROM public.raw_transactions;
```

This confirms that the imported row count matches the source dataset. It does not yet confirm that all records are valid for analysis.

Further checks will be recorded in `sql/01_data_quality.sql`, with findings documented separately.

### Data Handling Rules

The following rules will be reviewed before creating analytical datasets:

- Keep the original imported records unchanged.
- Identify cancellations separately from normal sales.
- Do not automatically remove negative quantities or duplicate records.
- Separate transactions without valid CustomerID from customer-level analysis where required.
- Check product codes and unusual transaction values before excluding them.
- Record the reason for any filtering or transformation.

The aim is to make data cleaning decisions clear and consistent, rather than removing records only because they look unusual.

## 6. SQL Analysis

The SQL analysis is divided into separate files based on business purpose.

### 6.1 Revenue Analysis

File: `sql/02_revenue_analysis.sql`

Planned work:

- Monthly revenue and order volume
- Average order value (AOV)
- Month-over-month revenue growth
- Running revenue totals
- Revenue by country
- Revenue from first-time and returning customers

### 6.2 Customer Analysis

File: `sql/03_customer_analysis.sql`

Planned work:

- Revenue per customer
- Purchase frequency
- First and most recent observed purchase
- Customer ranking by revenue
- Revenue concentration among top customers
- Customer segmentation using purchasing behaviour

### 6.3 Retention Analysis

File: `sql/04_retention_analysis.sql`

Planned work:

- Repeat purchase rate
- Time between purchases
- Time to second purchase
- First-purchase cohorts
- Monthly cohort retention
- Retention differences across cohorts

### 6.4 Product Analysis

File: `sql/05_product_analysis.sql`

Planned work:

- Revenue by product
- Units sold
- Unique customers by product
- Products purchased by returning customers
- Product-level revenue concentration

The queries will use JOINs, aggregations, CTEs, date functions, and window functions where appropriate.

The focus is on correct calculations and readable SQL. More complex queries will be used when they help answer a business question, rather than only to demonstrate a specific SQL function.

## 7. KPI Definitions

The main KPIs will be defined before the revenue and retention analysis.

| KPI | Working Definition |
|---|---|
| Sales Revenue | Sum of quantity × unit price for eligible sales records |
| Order Volume | Distinct eligible purchase invoices |
| Average Order Value | Sales revenue / eligible order volume |
| Monthly Revenue Growth | Percentage change from the previous month's revenue |
| Unique Customers | Distinct identifiable purchasing customers |
| Revenue per Customer | Eligible revenue / identifiable purchasing customers |
| Repeat Purchase Rate | Customers with at least two eligible purchase invoices / customers with at least one |
| Purchase Frequency | Eligible purchase invoices per identifiable customer |
| Time to Second Purchase | Time between first and second observed eligible purchases |
| Observed Customer Lifetime Revenue | Total eligible revenue from a customer during the dataset period |
| Cohort Retention | Share of customers from a first-purchase cohort who purchase again in a later month |

These are working definitions and may be updated after the data quality audit.

For example, cancellation records must be reviewed before deciding how to report gross sales and net revenue. They should not be treated as ordinary purchases.

## 8. Power BI Dashboard (Planned)

The Power BI dashboard will be built after the SQL analysis is validated.

The dashboard is planned to have three pages.

**Revenue Overview**

- Total sales revenue
- Monthly revenue trend
- Order volume
- Average order value
- Revenue by country

**Customer Performance**

- Unique customers
- First-time vs returning customer revenue
- Repeat purchase rate
- Top customers by revenue
- Customer segments

**Retention and Products**

- Cohort retention matrix
- Time to second purchase
- Purchase frequency
- Top products by revenue
- Product purchasing patterns

The goal is to make the KPIs easy to understand and allow business users to compare performance by time period and customer group.

## 9. Project Structure

The repository is being organized as follows:

```text
customer-revenue-retention-analytics/
│
├── README.md
├── .gitignore
│
├── data/
│   ├── raw/
│   └── processed/
│
├── schema/
│   └── create_tables.sql
│
├── scripts/
│   └── load_data.py
│
├── sql/
│   ├── 01_data_quality.sql
│   ├── 02_revenue_analysis.sql
│   ├── 03_customer_analysis.sql
│   ├── 04_retention_analysis.sql
│   └── 05_product_analysis.sql
│
├── tests/
│   └── validation_queries.sql
│
├── dashboard/
│   ├── README.md
│   └── screenshots/
│
└── results/
    ├── data_quality_report.md
    └── insights.md
```

Some files are planned and will be added as the project progresses.

The original Excel file and generated CSV are kept locally and excluded from Git tracking. The source dataset can be downloaded from UCI.

## 10. Reproducing the Data Import

The following steps describe the current local setup.

**Requirements:**

- PostgreSQL
- Python 3
- pandas
- openpyxl
- DBeaver or another PostgreSQL client

**1. Download the dataset**

Download `Online Retail.xlsx` from the UCI repository and place it in:

`data/raw/Online Retail.xlsx`

**2. Install Python dependencies**

```bash
python3 -m pip install pandas openpyxl
```

A virtual environment is recommended.

**3. Prepare the CSV**

From the project root, run:

```bash
python3 scripts/load_data.py
```

The script reads the Excel file and exports the data to:

`data/processed/online_retail.csv`

**4. Prepare PostgreSQL**

Create the `retail_analytics` database and run `schema/create_tables.sql` in that database.

**5. Import the CSV**

Import the CSV into `public.raw_transactions` using DBeaver. Map the CSV columns to the existing table and confirm the timestamp and NULL settings.

**6. Validate**

```sql
SELECT COUNT(*)
FROM public.raw_transactions;
```

Expected result: `541909`

Do not run the full import again on a populated table without checking the existing records.

A scripted import process will be added in a later stage.

## 11. Project Progress

### Completed

- [x] Defined the business scope and main questions
- [x] Selected the UCI Online Retail dataset
- [x] Downloaded the source data
- [x] Set up PostgreSQL and DBeaver
- [x] Created the `retail_analytics` database
- [x] Created the `raw_transactions` table
- [x] Prepared the CSV using Python
- [x] Imported 541,909 rows into PostgreSQL
- [x] Verified the imported row count

### In Progress / Next Steps

- [ ] Complete data quality audit
- [ ] Define final transaction filtering and revenue rules
- [ ] Build validated analytical tables or views
- [ ] Add SQL validation tests
- [ ] Complete revenue analysis
- [ ] Complete customer analysis
- [ ] Complete retention and cohort analysis
- [ ] Complete product analysis
- [ ] Document business findings and limitations
- [ ] Build Power BI dashboard
- [ ] Document a fully reproducible database import workflow

## 12. Limitations

There are several limitations to consider when interpreting the results.

First, the data covers a historical period from December 2010 to December 2011. The findings describe this dataset and should not be treated as current retail market performance.

Second, customer registration dates are not available. Therefore, customer cohorts will be based on the first purchase observed in the data. This may not represent a customer's actual first purchase with the business.

Third, the observation period is limited. Recent customer cohorts have less time to make repeat purchases, and December 2011 is incomplete. Retention comparisons must account for these differences.

Finally, the dataset does not include product costs, inventory records, or a complete refund history. Profitability and inventory recommendations cannot be confirmed from these records alone.

Business recommendations will be based on what the data can support, with additional data requirements noted where necessary.

## 13. Results and Business Recommendations

**Status: Not yet completed**

Findings will be added after SQL analysis and validation.

The final summary will cover:

- Main revenue trends
- Customer purchasing behaviour
- Retention patterns across cohorts
- Revenue concentration risks
- Product performance
- Possible business actions and their limitations

Recommendations will be based on observed results, not assumed findings.

## 14. Data Source and Attribution

Chen, D. (2015). *Online Retail* [Dataset]. UCI Machine Learning Repository.

https://doi.org/10.24432/C5BW33

The dataset is available under the Creative Commons Attribution 4.0 International (CC BY 4.0) license.

This is an independent portfolio project for learning and professional development. It is not affiliated with the original retailer.