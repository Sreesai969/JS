import pandas as pd
import matplotlib.pyplot as plt
data = [
    {"Day": "2025-05-01",  "Temperature": 22.5, "Humidity": 55, "WindSpeed": 10.2, "Precipitation": 1.2},
    {"Day": "2025-05-02",  "Temperature": 24.0, "Humidity": 60, "WindSpeed": 8.5,  "Precipitation": 0.0},
    {"Day": "2025-05-03",  "Temperature": 25.3, "Humidity": 58, "WindSpeed": 12.1, "Precipitation": 0.4},
    {"Day": "2025-05-04",  "Temperature": 23.8, "Humidity": 62, "WindSpeed": 9.9,  "Precipitation": 2.3},
    {"Day": "2025-05-05",  "Temperature": 21.4, "Humidity": 65, "WindSpeed": 11.5, "Precipitation": 3.1},
    {"Day": "2025-05-06",  "Temperature": 20.0, "Humidity": 70, "WindSpeed": 13.0, "Precipitation": 4.0},
    {"Day": "2025-05-07",  "Temperature": 19.8, "Humidity": 68, "WindSpeed": 10.8, "Precipitation": 2.7},
    {"Day": "2025-05-08",  "Temperature": 22.1, "Humidity": 59, "WindSpeed": 9.3,  "Precipitation": 0.5},
    {"Day": "2025-05-09",  "Temperature": 24.5, "Humidity": 55, "WindSpeed": 7.2,  "Precipitation": 0.0},
    {"Day": "2025-05-10",  "Temperature": 25.7, "Humidity": 52, "WindSpeed": 8.0,  "Precipitation": 0.0},
    {"Day": "2025-05-11",  "Temperature": 26.2, "Humidity": 50, "WindSpeed": 7.5,  "Precipitation": 0.0},
    {"Day": "2025-05-12",  "Temperature": 27.0, "Humidity": 48, "WindSpeed": 6.9,  "Precipitation": 0.1},
    {"Day": "2025-05-13",  "Temperature": 26.8, "Humidity": 49, "WindSpeed": 8.2,  "Precipitation": 0.3},
    {"Day": "2025-05-14",  "Temperature": 25.9, "Humidity": 53, "WindSpeed": 9.0,  "Precipitation": 0.8},
    {"Day": "2025-05-15",  "Temperature": 24.3, "Humidity": 57, "WindSpeed": 10.1, "Precipitation": 1.5},
    {"Day": "2025-05-16",  "Temperature": 23.0, "Humidity": 60, "WindSpeed": 11.2, "Precipitation": 2.0},
    {"Day": "2025-05-17",  "Temperature": 22.7, "Humidity": 63, "WindSpeed": 12.5, "Precipitation": 2.8},
    {"Day": "2025-05-18",  "Temperature": 22.2, "Humidity": 66, "WindSpeed": 11.8, "Precipitation": 3.4},
    {"Day": "2025-05-19",  "Temperature": 21.9, "Humidity": 67, "WindSpeed": 10.6, "Precipitation": 2.9},
    {"Day": "2025-05-20",  "Temperature": 22.4, "Humidity": 64, "WindSpeed": 9.7,  "Precipitation": 1.2},
]
df=pd.DataFrame(data)
# print(df)
# df.plot()
# plt.show()
# plt.bar(df["Day"],df["Temperature"],color="coral")
# plt.show()

