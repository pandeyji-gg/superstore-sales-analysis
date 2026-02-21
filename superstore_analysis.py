import pandas as pd
import matplotlib.pyplot as plt

frame = pd.read_csv("train.csv")

# quick look at the data
frame.head()
frame.describe()

# ---- sales by region ----

region_sales = frame.groupby("Region")["Sales"].sum().sort_values()

ax = region_sales.plot(kind="barh", figsize=(10, 6), color="steelblue")

for p in ax.patches:
    ax.annotate(
        f"{p.get_width():,.0f}",
        (p.get_width(), p.get_y() + p.get_height() / 2),
        va="center",
    )

plt.xlim(0, region_sales.max() * 1.2)
plt.title("Total Sales by Region")
plt.xlabel("")
plt.tight_layout()
plt.savefig("region_sales.png", dpi=150)
plt.show()

# ---- sales by category ----

category_sales = frame.groupby("Category")["Sales"].sum().sort_values()

ax = category_sales.plot(kind="barh", figsize=(10, 6), color="steelblue")

for p in ax.patches:
    ax.annotate(
        f"{p.get_width():,.0f}",
        (p.get_width(), p.get_y() + p.get_height() / 2),
        va="center",
    )

plt.xlim(0, category_sales.max() * 1.2)
plt.title("Total Sales by Category")
plt.xlabel("")
plt.tight_layout()
plt.savefig("category_sales.png", dpi=150)
plt.show()

# ---- technology breakdown -- phones are carrying the whole category ----

tech = frame[frame["Category"] == "Technology"]
tech_subcategory = tech.groupby("Sub-Category")["Sales"].sum().sort_values()

ax = tech_subcategory.plot(kind="barh", figsize=(10, 5), color="steelblue")

for p in ax.patches:
    ax.annotate(
        f"{p.get_width():,.0f}",
        (p.get_width(), p.get_y() + p.get_height() / 2),
        va="center",
    )

plt.xlim(0, tech_subcategory.max() * 1.3)
plt.title("Technology Sales by Sub-Category")
plt.xlabel("")
plt.tight_layout()
plt.savefig("tech_subcategory.png", dpi=150)
plt.show()

# ---- monthly trend ----
# need to convert order date to datetime first

frame["Order Date"] = pd.to_datetime(frame["Order Date"], dayfirst=True)
frame["Month"] = frame["Order Date"].dt.month
frame["Year"] = frame["Order Date"].dt.year

monthly = frame.groupby(["Year", "Month"])["Sales"].sum().reset_index()
monthly["Date"] = pd.to_datetime(monthly[["Year", "Month"]].assign(Day=1))
monthly = monthly.set_index("Date")["Sales"]

monthly.plot(kind="line", figsize=(15, 5), color="steelblue")
plt.title("Monthly Sales Trend 2015-2018")
plt.ylabel("Sales")
plt.xlabel("")
plt.tight_layout()
plt.savefig("monthly_trend.png", dpi=150)
plt.show()
