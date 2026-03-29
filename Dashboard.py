import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# ── Load cleaned data ──────────────────────────────────────────
df = pd.read_csv("superstore_clean.csv")
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Order Year']  = df['Order Date'].dt.year
df['Order Month'] = df['Order Date'].dt.month
df['Period'] = df['Order Year'].astype(str) + '-' + df['Order Month'].astype(str).str.zfill(2)

#  Pre-compute summaries 
total_sales   = df['Sales'].sum()
total_profit  = df['Profit'].sum()
total_orders  = df['Order ID'].nunique()
profit_margin = (total_profit / total_sales) * 100

region_df  = df.groupby('Region')[['Sales','Profit']].sum().reset_index().sort_values('Sales', ascending=False)
monthly_df = df.groupby('Period')[['Sales','Profit']].sum().reset_index().sort_values('Period')
cat_df     = df.groupby('Category')[['Sales','Profit']].sum().reset_index()
subcat_df  = df.groupby('Sub-Category')[['Sales','Profit']].sum().reset_index().sort_values('Profit')

#  Build Dashboard 
fig = make_subplots(
    rows=3, cols=2,
    subplot_titles=(
        "Sales by Region",
        "Profit by Sub-Category",
        "Monthly Sales & Profit Trend",
        "Sales vs Profit by Category",
        "Discount Impact on Profit",
        "Top 10 Products by Sales"
    ),
    row_heights=[0.25, 0.40, 0.35],
    vertical_spacing=0.12,
    horizontal_spacing=0.10
)

#  Chart 1: Sales by Region (Row 1, Col 1) 
fig.add_trace(go.Bar(
    x=region_df['Region'],
    y=region_df['Sales'],
    name='Sales',
    marker_color=['#4C72B0','#DD8452','#55A868','#C44E52'],
    text=region_df['Sales'].apply(lambda x: f"${x:,.0f}"),
    textposition='outside'
), row=1, col=1)

#  Chart 2: Profit by Sub-Category (Row 1, Col 2) 
colors = ['#C44E52' if x < 0 else "#0814EF" for x in subcat_df['Profit']]
fig.add_trace(go.Bar(
    x=subcat_df['Profit'],
    y=subcat_df['Sub-Category'],
    orientation='h',
    name='Profit',
    marker_color=colors,
    showlegend=False
), row=1, col=2)

#  Chart 3: Monthly Trend (Row 2, Col 1) 
fig.add_trace(go.Scatter(
    x=monthly_df['Period'],
    y=monthly_df['Sales'],
    name='Monthly Sales',
    mode='lines+markers',
    line=dict(color='#4C72B0', width=2),
    marker=dict(size=4)
), row=2, col=1)

fig.add_trace(go.Scatter(
    x=monthly_df['Period'],
    y=monthly_df['Profit'],
    name='Monthly Profit',
    mode='lines+markers',
    line=dict(color='#55A868', width=2, dash='dot'),
    marker=dict(size=4)
), row=2, col=1)

#  Chart 4: Sales vs Profit by Category (Row 2, Col 2) 
fig.add_trace(go.Bar(
    x=cat_df['Category'],
    y=cat_df['Sales'],
    name='Sales',
    marker_color='#4C72B0',
    offsetgroup=1
), row=2, col=2)

fig.add_trace(go.Bar(
    x=cat_df['Category'],
    y=cat_df['Profit'],
    name='Profit',
    marker_color='#55A868',
    offsetgroup=2
), row=2, col=2)

#  Chart 5: Discount vs Profit Scatter (Row 3, Col 1) 
fig.add_trace(go.Scatter(
    x=df['Discount'],
    y=df['Profit'],
    mode='markers',
    name='Orders',
    marker=dict(color='#4C72B0', opacity=0.3, size=4),
    showlegend=False
), row=3, col=1)

fig.add_hline(y=0, line_dash="dash", line_color="red",
              annotation_text="Break-even", row=3, col=1)

#  Chart 6: Top 10 Products (Row 3, Col 2) 
top10 = df.groupby('Product Name')['Sales'].sum().nlargest(10).reset_index()
top10['Short Name'] = top10['Product Name'].str[:30] + '...'

fig.add_trace(go.Bar(
    x=top10['Sales'],
    y=top10['Short Name'],
    orientation='h',
    name='Top Products',
    marker_color='#DD8452',
    showlegend=False
), row=3, col=2)

#  KPI Annotations at the top 
fig.add_annotation(text=f"<b>Total Sales</b><br>${total_sales:,.0f}",
    x=0.08, y=1.15, xref='paper', yref='paper', showarrow=False,
    font=dict(size=13), bgcolor='#EBF5FB', bordercolor='#4C72B0',
    borderwidth=1, borderpad=8)

fig.add_annotation(text=f"<b>Total Profit</b><br>${total_profit:,.0f}",
    x=0.33, y=1.15, xref='paper', yref='paper', showarrow=False,
    font=dict(size=13), bgcolor='#EAFAF1', bordercolor='#55A868',
    borderwidth=1, borderpad=8)

fig.add_annotation(text=f"<b>Profit Margin</b><br>{profit_margin:.1f}%",
    x=0.58, y=1.15, xref='paper', yref='paper', showarrow=False,
    font=dict(size=13), bgcolor='#FEF9E7', bordercolor='#DD8452',
    borderwidth=1, borderpad=8)

fig.add_annotation(text=f"<b>Total Orders</b><br>{total_orders:,}",
    x=0.83, y=1.15, xref='paper', yref='paper', showarrow=False,
    font=dict(size=13), bgcolor='#FDEDEC', bordercolor='#C44E52',
    borderwidth=1, borderpad=8)

# ── Layout ─────────────────────────────────────────────────────
fig.update_layout(
    title=dict(
        text="Superstore Sales Dashboard",
        font=dict(size=24),
        x=0.5,
        y=0.98
    ),
    height=1100,
    margin=dict(t=180, b=60, l=60, r=60),
    template='plotly_white',
    legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
    barmode='group'
)

fig.update_xaxes(tickangle=-45, row=2, col=1)

#  Save & Open 
fig.write_html("dashboard.html")
print("Dashboard saved! Open dashboard.html in your browser.")
fig.show()