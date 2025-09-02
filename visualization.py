import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from seaborn import barplot,scatterplot
file_path = "1) iris.csv"
df = pd.read_csv(file_path)

cat_col = "species"
num_col1 = "sepal_length"
num_col2 = "petal_length"


print("Bar Plot")
plt.figure(figsize=(8,5))
sns.barplot(x=cat_col, y=num_col1, data=df, color="skyblue")
plt.title('Bar Plot: Average of NumericalColumn1 by Category', fontsize=14)
plt.xlabel("Category", fontsize=12)
plt.ylabel("Average Value", fontsize=12)
plt.xticks(rotation=30)
plt.savefig("bar_plot.png", dpi=300, bbox_inches="tight")
plt.show()

print("Line Plot")
plt.figure(figsize=(8,5))
plt.plot(df[num_col1], label=num_col1, marker="o")
plt.plot(df[num_col2], label=num_col2, marker="s")
plt.title("Line Chart of Numerical Columns", fontsize=14)
plt.xlabel("Index", fontsize=12)
plt.ylabel("Value", fontsize=12)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.7)
plt.savefig("line_chart.png", dpi=300, bbox_inches="tight")
plt.show()

print("Scatter Plot")
plt.figure(figsize=(8,5))
scatterplot(x=num_col1, y=num_col2, data=df, hue=cat_col, palette="coolwarm", s=70)
plt.title(f"Scatter Plot: {num_col1} vs {num_col2}", fontsize=14)
plt.xlabel(num_col1, fontsize=12)
plt.ylabel(num_col2, fontsize=12)
plt.legend(title=cat_col)
plt.savefig("scatter_plot.png", dpi=300, bbox_inches="tight")
plt.show()

print("✅ Plots created and saved as images (PNG files).")
