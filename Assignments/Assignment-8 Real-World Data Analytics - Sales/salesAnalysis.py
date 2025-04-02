import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime, timedelta
import random

# Generate sample sales data
def generate_sales_data():
    start_date = datetime.today() - timedelta(days=180)
    categories = ['Electronics', 'Clothing', 'Groceries', 'Furniture', 'Toys']
    data = []
    
    for _ in range(500):
        date = start_date + timedelta(days=random.randint(0, 180))
        category = random.choice(categories)
        units_sold = random.randint(1, 100)
        price_per_unit = random.uniform(5, 500)
        total_sales = units_sold * price_per_unit
        
        data.append([date.strftime('%Y-%m-%d'), category, units_sold, round(price_per_unit, 2), round(total_sales, 2)])
    
    return pd.DataFrame(data, columns=['Date', 'Category', 'Units Sold', 'Price per Unit', 'Total Sales'])

class SalesApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sales Dashboard")
        self.geometry("1000x600")
        ctk.set_appearance_mode("dark")
        
        self.sales_data = generate_sales_data()
        self.sales_data['Date'] = pd.to_datetime(self.sales_data['Date'])
        
        self.sidebar = ctk.CTkFrame(self, width=200)
        self.sidebar.pack(side="left", fill="y")

        self.title_label = ctk.CTkLabel(self.sidebar, text="Menu", font=("Arial", 18, "bold"))
        self.title_label.pack(pady=20)

        self.dashboard_button = ctk.CTkButton(self.sidebar, text="Dashboard", command=self.show_dashboard)
        self.dashboard_button.pack(pady=10)

        self.sales_button = ctk.CTkButton(self.sidebar, text="Sales Data", command=self.show_sales_table)
        self.sales_button.pack(pady=10)
        
        self.download_button = ctk.CTkButton(self.sidebar, text="Download CSV", command=self.download_csv)
        self.download_button.pack(pady=10)
        
        self.month_var = tk.StringVar()
        months = self.sales_data['Date'].dt.strftime('%B').unique().tolist()
        self.month_dropdown = ttk.Combobox(self.sidebar, textvariable=self.month_var, values=months, state='readonly')
        self.month_dropdown.pack(pady=10)
        self.month_dropdown.bind("<<ComboboxSelected>>", self.update_visuals)
        
        self.main_frame = ctk.CTkFrame(self, width=800, height=600)
        self.main_frame.pack(side="right", fill="both", expand=True)

        self.show_dashboard()
    
    def show_dashboard(self):
        self.clear_main_frame()
        
        total_sales = round(self.sales_data['Total Sales'].sum(), 2)
        best_category = self.sales_data.groupby('Category')['Total Sales'].sum().idxmax()
        peak_month = self.sales_data.groupby(self.sales_data['Date'].dt.strftime('%B'))['Total Sales'].sum().idxmax()
        avg_daily_sales = round(self.sales_data['Total Sales'].sum() / 180, 2)
        
        ctk.CTkLabel(self.main_frame, text=f"Total Sales: ₹{total_sales}", font=("Arial", 18, "bold")).pack(pady=5)
        ctk.CTkLabel(self.main_frame, text=f"Best Selling Category: {best_category}", font=("Arial", 18)).pack(pady=5)
        ctk.CTkLabel(self.main_frame, text=f"Peak Sales Month: {peak_month}", font=("Arial", 18)).pack(pady=5)
        ctk.CTkLabel(self.main_frame, text=f"Average Sales per Day: ₹{avg_daily_sales}", font=("Arial", 18)).pack(pady=5)
    
    def show_sales_table(self):
        self.clear_main_frame()
        table_frame = ctk.CTkFrame(self.main_frame)
        table_frame.pack(fill="both", expand=True)
        
        columns = list(self.sales_data.columns)
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120, anchor="center")
        
        for _, row in self.sales_data.head(50).iterrows():
            self.tree.insert("", tk.END, values=row.tolist())
        
        self.tree.pack(fill="both", expand=True)
    
    def update_visuals(self, event=None):
        self.clear_main_frame()
        selected_month = self.month_var.get()
        monthly_data = self.sales_data[self.sales_data['Date'].dt.strftime('%B') == selected_month]
        
        fig, axes = plt.subplots(2, 2, figsize=(10, 8))
        
        monthly_data.groupby('Date')['Total Sales'].sum().plot(ax=axes[0, 0], title='Sales Trend', ylabel='Sales', xlabel='Date')
        monthly_data.groupby('Category')['Total Sales'].sum().plot(kind='bar', ax=axes[0, 1], title='Sales per Category')
        monthly_data.groupby('Category')['Total Sales'].sum().plot(kind='pie', autopct='%1.1f%%', ax=axes[1, 0], title='Category-wise Distribution')
        monthly_data['Total Sales'].hist(ax=axes[1, 1], bins=20, edgecolor='black', alpha=0.7)
        axes[1, 1].set_title('Sales Frequency Distribution')
        
        fig.tight_layout()
        canvas = FigureCanvasTkAgg(fig, master=self.main_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)
    
    def download_csv(self):
        self.sales_data.to_csv("sales_data.csv", index=False)
        print("Sales data saved as 'sales_data.csv'")
    
    def clear_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = SalesApp()
    app.mainloop()
    