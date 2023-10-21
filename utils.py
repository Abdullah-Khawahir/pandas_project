import pandas as pd
def for_each_row(df:pd.DataFrame ,function:()  ):
    row_count = 0
    for index ,row in df.iterrows(): 
        function(row)
        row_count = row_count +1
    return row_count
 


