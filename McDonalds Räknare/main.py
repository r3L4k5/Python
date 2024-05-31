import numpy  as np
import matplotlib.pyplot as mpl

sales_data = [
{"Hamburgare": 150, "Pommes frites": 200, "Läsk": 180, "Milkshake": 40, "Sallader": 30, "McNuggets": 100},
{"Hamburgare": 170, "Pommes frites": 220, "Läsk": 190, "Milkshake": 50, "Sallader": 35, "McNuggets": 105},
{"Hamburgare": 160, "Pommes frites": 210, "Läsk": 185, "Milkshake": 45, "Sallader": 33, "McNuggets": 110},
{"Hamburgare": 180, "Pommes frites": 230, "Läsk": 200, "Milkshake": 55, "Sallader": 40, "McNuggets": 115},
{"Hamburgare": 170, "Pommes frites": 220, "Läsk": 195, "Milkshake": 50, "Sallader": 38, "McNuggets": 120},
{"Hamburgare": 190, "Pommes frites": 240, "Läsk": 210, "Milkshake": 60, "Sallader": 42, "McNuggets": 125},
{"Hamburgare": 185, "Pommes frites": 235, "Läsk": 205, "Milkshake": 58, "Sallader": 40, "McNuggets": 130},
{"Hamburgare": 175, "Pommes frites": 225, "Läsk": 190, "Milkshake": 52, "Sallader": 36, "McNuggets": 120},
{"Hamburgare": 165, "Pommes frites": 215, "Läsk": 185, "Milkshake": 48, "Sallader": 34, "McNuggets": 110},
{"Hamburgare": 180, "Pommes frites": 230, "Läsk": 200, "Milkshake": 55, "Sallader": 39, "McNuggets": 115}
]

costs = [50, 25, 20, 30, 45, 35]
total_money = []

for i in range(len(sales_data)):
    
    sales_day = []
    money_day = 0

    for product in sales_data[i]:
        product_sales = sales_data[i][product]
        
        sales_day.append(product_sales)

    for i in range(len(sales_day)):
        money = sales_day[i] * costs[i]

        money_day += money
    
    total_money.append(money_day)

y_axis= np.array(total_money)
x_axis = np.array(list(range(1, len(sales_data) + 1)))

mpl.plot(x_axis, y_axis)

mpl.show()

        

