import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [12000, 15000, 17000, 16000, 18000, 20000],
    "Profit": [3000, 3500, 4200, 3900, 4500, 5000],
    "Customers": [120, 140, 160, 155, 180, 200],
    "Marketing_Spend": [2000, 2200, 2500, 2400, 2600, 3000],
    "Rating": [4.1, 4.3, 4.0, 4.2, 4.4, 4.5]
}
df=pd.DataFrame(data)
#print(df)
#df.plot()
#plt.show()
# plt.barh(df["Month"],df["Sales"],color=["red","lightgreen","orange","skyblue","yellow","pink"])
# plt.barh(df["Month"],df["Profit"],color="green")
# plt.legend(["Sales","Profit"])
# plt.show()
# plt.pie(df["Sales"],labels=df["Month"],autopct="%0.1f%%")
# plt.title("sales distribution")
# plt.show()
plt.fill_between(df["Month"],df["Sales"],alpha=0.4)
plt.title("sales area chart")
plt.show()
