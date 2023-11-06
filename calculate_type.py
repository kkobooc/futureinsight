import pandas as pd

def calculate_type(df, q_lst):
    selected_cols = []
    for q in q_lst:
        cols = [col for col in df.columns if q in col]
        selected_cols += cols
        
    neutral_point = 3
    standard_point = neutral_point * len(selected_cols)

    result_lst = []
    for i in range(0, len(df)):
        df_i = df.iloc[i][selected_cols]
        point_i = df_i.sum()
        
        if point_i == standard_point:
            type = "NEUTRAL"
        elif point_i > standard_point:
            type = "HIGH"
        else:
            type = "LOW"
        result_lst.append(type)
    return result_lst
