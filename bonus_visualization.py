import sqlite3
import matplotlib.pyplot as plt

db_path = "data_analysis.db"

try:
    with sqlite3.connect(db_path) as connection:
        cursor = connection.cursor()

        query = """
        SELECT Product, SUM(Price * Quantity) AS TotalRevenue
        FROM Sales
        GROUP BY Product
        ORDER BY TotalRevenue DESC;
        """
        cursor.execute(query)
        data = cursor.fetchall()

        if not data:
            raise ValueError("Error: There is no data")

        products, revenues = zip(*data)

        plt.figure(figsize=(10, 6))
        plt.bar(products, revenues, color="skyblue", edgecolor="black")

        plt.xlabel("Products", fontsize=12)
        plt.ylabel("Total Revenue", fontsize=12)
        plt.title("Total Revenue by Product", fontsize=14, fontweight="bold")
        plt.xticks(rotation=45, ha="right", fontsize=10)
        plt.grid(axis="y", linestyle="--", alpha=0.7)

        plt.tight_layout()
        plt.savefig("revenue_chart.png", dpi=300)
        plt.show()

except sqlite3.Error as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Error: {e}")
