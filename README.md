# US Hospital Performance & Operations Dashboard
### Python • Power BI • Data Analysis

---

## Project Overview

This project analyzes a publicly available US hospital dataset to explore hospital distribution, ownership patterns, performance ratings, and emergency services availability across all US states.

The goal was to clean and transform raw data using Python, derive meaningful insights, and present findings through an interactive Power BI dashboard.

---

## Tools & Technologies Used

| Tool | Purpose |
|------|---------|
| Python (Pandas) | Data cleaning, transformation, feature engineering |
| Power BI Desktop | Dashboard development, interactive visualizations |
| Excel/CSV | Raw data format |
| VS Code | Development environment |

---

## Dataset

- **Source:** Publicly available US Hospital dataset (Kaggle)
- **Files used:**
  - `hospital_locations.csv` - 7,623 hospital records with location, type, status, population
  - `Hospital_General_Information.csv` - 4,818 hospital records with ratings, ownership, emergency services

---

## Data Cleaning & Preparation (Python)

Key steps performed in `hospital_analysis.py`:

- Removed closed hospitals and filtered to US-only records
- Replaced invalid population values (-999) with null
- Standardized column names for readability
- Replaced "Not Available" strings with null values
- Converted Overall_Rating to numeric format
- Exported two cleaned CSV files ready for Power BI

---

## Dashboard Visuals

The Power BI dashboard (`US_Hospital_Dashboard.pbix`) includes:

1. **Total Hospitals** - KPI Card showing 4,818 hospitals across the US
2. **Hospitals by State** - Top 15 states by hospital count (TX leads with 407)
3. **Hospital Type Breakdown** - Donut chart showing General Acute Care dominates at 58%
4. **Avg Rating by Ownership** - Physician-owned hospitals rate highest at 4.10
5. **Emergency Services** - 93.9% of hospitals provide emergency services
6. **Avg Population by State** - DC, CT, NJ serve the highest average populations

---

## Key Insights

- **Texas** has the highest number of hospitals (407), followed by California (345) and Florida (187)
- **Physician-owned** hospitals have the highest average rating (4.10) compared to Government-owned (2.65–3.03)
- **93.9%** of US hospitals offer emergency services
- **General Acute Care** is the most common hospital type (58.46%)
- **DC, CT and NJ** serve the highest average populations per hospital

---

## How to Run

1. Clone this repository
2. Install dependencies:
```
pip install pandas
```
3. Place both CSV files in the same folder as `hospital_analysis.py`
4. Run:
```
python hospital_analysis.py
```
5. Open `US_Hospital_Dashboard.pbix` in Power BI Desktop

---

## Project Structure

```
us-hospital-performance-dashboard/
│
├── hospital_analysis.py          # Python data cleaning script
├── general_info_cleaned.csv      # Cleaned general info data
├── locations_cleaned.csv         # Cleaned locations data
├── US_Hospital_Dashboard.pbix    # Power BI dashboard file
└── README.md                     # Project documentation
```

---

*Built as a personal portfolio project to demonstrate data analysis and visualization skills.*# hospital-dashboard-project
Personal portfolio project - US Hospital Performance &amp; Operations Dashboard built using Python (Pandas) and Power BI with real hospital dataset
