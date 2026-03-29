# Superstore Sales Analysis — Insights Report

**Prepared by:** RUDRA ROY 
**Dataset:** Sample Superstore (2014–2018)  
**Tools Used:** Python, pandas, matplotlib, seaborn, Plotly  

---

## 1. Executive Summary

This report analyses 5,009 orders placed between 2014 and 2018 across
four regions of a fictional superstore chain. Total revenue stood at
$2,297,201 with a net profit of $286,397 — a profit margin of 12.5%.
The analysis uncovers regional performance gaps, loss-making product
categories, and the damaging effect of heavy discounting on profitability.

---

## 2. Key Performance Indicators

| Metric         | Value        |
|----------------|--------------|
| Total Sales    | $2,297,201   |
| Total Profit   | $286,397     |
| Profit Margin  | 12.5%        |
| Total Orders   | 5,009        |

---

## 3. Regional Performance

- **West** is the top-performing region with $725,458 in sales.
- **South** is the weakest region at $391,722 in sales.
- Despite lower sales, **East** maintains healthier profit margins
  than Central, suggesting better cost control.

**Recommendation:** Investigate why Central and South underperform.
Consider targeted promotions or pricing adjustments in those regions.

---

## 4. Category & Sub-Category Analysis

- **Technology** generates the highest sales ($836,154) and the
  best profit margins among the three categories.
- **Furniture** has high sales ($741,999) but extremely thin margins,
  contributing only marginally to profit.
- **Office Supplies** has the best balance of volume and profitability.

### Loss-Making Sub-Categories

| Sub-Category | Profit     |
|--------------|------------|
| Tables       | −$17,725   |
| Bookcases    | −$3,473    |
| Supplies     | −$1,189    |

**Recommendation:** Review pricing strategy for Tables and Bookcases.
Consider discontinuing heavy discounts on these items or removing them
from the catalogue if losses persist.

---

## 5. Sales Trend Over Time

- Sales show a **clear upward trend** from 2014 to 2018.
- A strong **seasonal spike** is visible every November–December,
  likely driven by holiday shopping.
- Profit growth is slower than sales growth, indicating rising costs
  or increasing discounts over time.

**Recommendation:** Plan inventory and staffing around the Q4 seasonal
spike. Investigate why profit growth is lagging behind sales growth.

---

## 6. Discount Impact on Profit

- Orders with **0% discount** are almost always profitable.
- Once discounts exceed **30%**, the majority of orders turn into losses.
- Several orders with 60–70% discounts recorded losses of over $5,000.

**Recommendation:** Cap discounts at 20% as a company-wide policy.
High discounts are destroying profitability without clear evidence of
driving enough volume to compensate.

---

## 7. Top Products

- **Canon imageCLASS 2200** is the single best-selling product at
  over $60,000 in sales.
- The top 10 products are dominated by printers and binding machines,
  all from the Technology and Office Supplies categories.

**Recommendation:** Prioritise stock availability for top-performing
products, especially heading into Q4.

---

## 8. Conclusion

The Superstore is growing steadily but faces profitability challenges
in Furniture and certain Office Supplies sub-categories. The biggest
controllable risk is the aggressive discounting policy, which is
directly responsible for a large portion of loss-making orders.
Addressing discount caps and refocusing on Technology — the most
profitable category — would significantly improve the bottom line.

---

## 9. Files in This Project

| File                    | Description                        |
|-------------------------|------------------------------------|
| superstore_clean.csv    | Cleaned dataset                    |
| analysis.py             | Data exploration & KPI calculation |
| visualizations.py       | Static charts (matplotlib/seaborn) |
| dashboard.py            | Interactive Plotly dashboard       |
| dashboard.html          | Final interactive dashboard        |
| insights_report.md      | This report                        |