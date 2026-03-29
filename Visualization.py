import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#  Load cleaned data 
df = pd.read_csv("superstore_clean.csv")
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Order Year']  = df['Order Date'].dt.year
df['Order Month'] = df['Order Date'].dt.month

sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams['figure.figsize'] = (10, 5)

#  Chart 1: Sales by Region 
region_plot = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)

plt.figure()
ax = region_plot.plot(kind='bar', color=['#4C72B0','#DD8452','#55A868','#C44E52'], edgecolor='white')
plt.title('Total Sales by Region')
plt.xlabel('Region')
plt.ylabel('Sales ($)')
plt.xticks(rotation=0)
for p in ax.patches:
    ax.annotate(f"${p.get_height():,.0f}", (p.get_x()+0.1, p.get_height()+500))
plt.tight_layout()
plt.savefig('sales_by_region.png', dpi=150)
plt.show()
print("Chart 1 saved.")

#  Chart 2: Monthly Sales Trend 
monthly = df.groupby(['Order Year','Order Month'])['Sales'].sum().reset_index()
monthly['Period'] = monthly['Order Year'].astype(str) + '-' + monthly['Order Month'].astype(str).str.zfill(2)

plt.figure()
plt.plot(monthly['Period'], monthly['Sales'], marker='o', linewidth=2, color='#4C72B0')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.xticks(rotation=45, ha='right', fontsize=7)
plt.tight_layout()
plt.savefig('monthly_trend.png', dpi=150)
plt.show()
print("Chart 2 saved.")

#  Chart 3: Profit by Category 
cat_profit = df.groupby('Category')['Profit'].sum().sort_values()

colors = ['#C44E52' if x < 0 else '#55A868' for x in cat_profit]
plt.figure()
cat_profit.plot(kind='barh', color=colors, edgecolor='white')
plt.title('Total Profit by Category')
plt.xlabel('Profit ($)')
plt.tight_layout()
plt.savefig('profit_by_category.png', dpi=150)
plt.show()
print("Chart 3 saved.")

#  Chart 4: Discount vs Profit 
plt.figure()
plt.scatter(df['Discount'], df['Profit'], alpha=0.3, color='#4C72B0', edgecolors='none')
plt.axhline(0, color='red', linewidth=1, linestyle='--', label='Break-even')
plt.title('Discount vs Profit')
plt.xlabel('Discount')
plt.ylabel('Profit ($)')
plt.legend()
plt.tight_layout()
plt.savefig('discount_vs_profit.png', dpi=150)
plt.show()
print("Chart 4 saved.")

#  Chart 5: Sales Heatmap 
pivot = df.pivot_table(values='Sales', index='Category', columns='Region', aggfunc='sum')

plt.figure()
sns.heatmap(pivot, annot=True, fmt=',.0f', cmap='YlGnBu', linewidths=0.5)
plt.title('Sales Heatmap — Category vs Region')
plt.tight_layout()
plt.savefig('heatmap.png', dpi=150)
plt.show()
print("Chart 5 saved.")

print("\nAll charts saved successfully!")