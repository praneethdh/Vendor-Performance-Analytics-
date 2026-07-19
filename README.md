# Vendor Performance Analytics Platform

## About The Project

This project is an end-to-end vendor performance analytics workflow built around inventory, purchase, sales, invoice, and product pricing data. The goal is to transform raw operational files into a single, analysis-ready dataset that can be used to evaluate vendor profitability, stock efficiency, and pricing performance. The workflow starts with raw CSV files stored in the `data/` folder and loads them into a SQLite database using `Ingestion_db.py` and `Ingestion_db.ipynb`. From there, `get_vendor_summary.ipynb` joins and aggregates the source tables into a consolidated `vendor_sales_summary` table that becomes the foundation for all downstream analysis.

The summary table combines purchase transactions, sales transactions, freight costs, and product-level pricing information. It also engineers business metrics that make the data more useful for decision-making, including Gross Profit, Profit Margin, Stock Turnover, and Sales-to-Purchase Ratio. These derived fields help identify which vendors generate the most value, which brands move slowly, where inventory is tied up, and which products or vendors may need pricing or procurement adjustments.

The exploratory analysis notebooks, `EDA.ipynb` and `Vendor Performance Analysis.ipynb`, are used to inspect the structure of the database, check distributions, study outliers, evaluate correlations, and answer business questions about vendor performance. The analysis highlights key areas such as high- and low-performing vendors, brands with strong margins but low sales volume, vendors contributing disproportionately to purchase spend, and unsold inventory capital. Statistical analysis, including confidence intervals and a two-sample t-test, is used to compare vendor groups and validate whether profit margin differences are meaningful.

The Power BI dashboard is the reporting layer of the same project. It uses the `vendor_sales_summary` dataset as its core source and presents the analysis in a business-friendly format with KPI cards, contribution charts, top vendor and top brand visuals, low-performing vendor/brand views, and inventory turnover insights. The additional tables and measures created in Power BI are supporting model objects for the dashboard, helping the visuals and calculations remain interactive and easy to use.

Overall, the project moves from raw data ingestion to SQL-based transformation, then to Python analysis, and finally to Power BI reporting. The result is a practical vendor analytics platform that supports better vendor selection, pricing strategy, and inventory planning.

## 📊 Dashboard Preview

*(Insert 1-2 Power BI screenshots here before final submission.)*

![Dashboard Overview](dashboard/screenshots/dashboard-overview.png)

## Project Pipeline

**1. Data Ingestion**  
Raw transactional CSVs are loaded into a SQLite database via `Ingestion_db.py`, creating queryable tables for each source.

**2. Data Transformation**  
`get_vendor_summary.ipynb` merges and aggregates the source tables into `vendor_sales_summary`.

**3. Business Metric Engineering**  
Key metrics are derived directly in the pipeline:
- Gross Profit
- Profit Margin
- Stock Turnover
- Sales-to-Purchase Ratio

**4. Exploratory & Statistical Analysis**  
`EDA.ipynb` and `Vendor Performance Analysis.ipynb` explore distributions, outliers, correlations, and business questions around vendor and brand performance.

**5. Dashboard & Reporting**  
The Power BI dashboard uses `vendor_sales_summary` as its core dataset and presents executive KPIs, vendor concentration, top performers, low performers, and inventory efficiency.

## Key Business Insights

- Identifies vendors contributing disproportionately to unsold capital.
- Highlights brands with low sales but high margins as pricing or marketing opportunities.
- Surfaces slow-moving inventory through stock turnover analysis.
- Compares profit margins between top-performing and low-performing vendors using statistical testing.

## Tech Stack

- **Data Storage:** SQLite
- **Data Processing:** Python, Pandas, NumPy
- **Statistical Analysis:** SciPy
- **Visualization:** Power BI
- **Notebooks:** Jupyter

## Project Structure

```text
├── data/                           # Raw CSV source files
├── Ingestion_db.py                 # Loads raw CSVs into SQLite
├── Ingestion_db.ipynb
├── get_vendor_summary.ipynb        # Builds vendor_sales_summary table
├── get_vendor_summary.txt
├── EDA.ipynb                       # Exploratory analysis
├── Vendor Performance Analysis.ipynb  # Statistical testing & insights
├── vendor_sales_summary.csv        # Final analytical dataset
└── dashboard/                      # Power BI file + screenshots
```

## How to Run

1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run `Ingestion_db.py` to build the SQLite database.
4. Run `get_vendor_summary.ipynb` to generate the summary table.
5. Open `EDA.ipynb` and `Vendor Performance Analysis.ipynb` to explore the analysis.
6. Open the `.pbix` file in Power BI Desktop to view the dashboard.

## License

MIT License