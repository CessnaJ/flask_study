import pandas as pd
import json

excel_file = 'low_floor_bus_information.xlsx'
df = pd.read_excel(excel_file)


car_reg_arr = df['CAR_REG_NO']
route_arr = df['']

new_arr = sorted(list(set(arr)))

new_df = pd.DataFrame(columns=['CAR_REG_NO'])


for idx in range(476):
    car_reg_no = new_arr[idx]
    new_df.loc[idx] = [car_reg_no]


new_df.to_excel('output.xlsx', index=True)