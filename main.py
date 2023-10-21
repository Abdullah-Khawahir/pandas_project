import pandas as pd
import os as os
import utils as utils
CLUSTER=1
TAG= 0
SR=18
TYPE=15
COMPANY=16
MODEL=17
PROCESSOR=19
DISK=20
RAM=21
CONDITION=22
HEADERS= [
"Asset tag number",
"Cluster",
"Facility type",
"Facility name",
"District",
"Existing facility code",
"Existing Floor number",
"Existing Room number",
"Building address",
"Building name",
"Existing building code",
"Department / management",
"Custodian name",
"Custodian National ID / Iqama",
"Asset class",
"Asset description",
"Asset manufacturer",
"Asset model",
"Serial number",
"PCs processor",
"hard disk types",
"Ram size",
"Condition "
]

paths = []
for  dirpath, dirnames, filenames in os.walk('/home/abtuly/pandas_projects/New folder'):
    for file in filenames:
        paths.append(f'{dirpath}/{file}')

data_frames = []
for path in paths:
    print(f'reading {path}')
    data_frames.append(pd.read_excel(path,skiprows=[0,1,2,3],usecols=range(0,23),header=None))

all_data_frames = pd.concat(data_frames)

complete_rows:list[pd.Series] = []
not_complete_rows:list[pd.Series] = []

for i,row in all_data_frames.iterrows():
    if  str(row.get(TYPE)).upper() in ['PC' ,'LAPTOP' ]:
        pc = row.get([SR,TYPE,COMPANY,MODEL,PROCESSOR,DISK,RAM])
        if not pc.isnull().values.any() or \
           not pc.isna().values.any():
            complete_rows.append(row)
        else:
            not_complete_rows.append(row)
    else:
        not_pc =row.get([SR,TYPE,COMPANY,MODEL])
        if  not not_pc.isnull().values.any() or \
            not not_pc.isna().values.any()  :
            complete_rows.append(row)
        else:
            not_complete_rows.append(row)



valid_df = pd.concat(complete_rows , ignore_index=True,axis='columns').T.drop_duplicates([SR] ,keep="first")
invalid_df = pd.concat(not_complete_rows,ignore_index=True,axis='columns').T.drop_duplicates([SR] ,keep="first")

for i,invalid_row in invalid_df.iterrows():
    for j,valid_row in valid_df.iterrows():
        if invalid_row.get(SR) in valid_df[SR].to_list():
            invalid_df.drop([i])



print(f'valid   {len(complete_rows)}\nunique  {valid_df[SR].is_unique}')

print(f'invalid {len(not_complete_rows)}\nunique  {invalid_df[SR].is_unique}')




with open('./all.csv' ,'w') as f : 
    f.write(all_data_frames.to_csv(header=HEADERS , index=False))


with open('./valid.csv' ,'w') as f : 
    f.write(valid_df
            .drop_duplicates(ignore_index=True ,subset=[SR])
            .to_csv(header=HEADERS , index=False))
with open('./invalid.csv' ,'w') as f : 
    f.write(invalid_df
            .to_csv(header=HEADERS , index=False))
















# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', None)
# pd.set_option('display.max_colwidth', None)


# def write_to_csv(path,rows:pd.DataFrame, headers):
#     with open(path, 'w') as file:
#         print(f'writing {rows.shape[1]} rows to {path}')
#         file.write(rows.T.to_csv(index=False , header=headers ))

# def processRows(df:pd.DataFrame):
#     completeRows =[]
#     incompleteRows=[]
#     counter = 0
#     for index, series in df.iterrows():
#         counter= counter +1
#         if str(series.get(TYPE)).upper() in ['PC' ,'LAPTOP' ] :
#             if  not series.get([SR,TYPE,COMPANY,MODEL,PROCESSOR,DISK,RAM]).isnull().values.any() and\
#                 not series.get([SR,TYPE,COMPANY,MODEL,PROCESSOR,DISK,RAM]).isna().values.any(): 
#                 completeRows.append(series)
#             else:
#                 incompleteRows.append(series)
#         else:
#             if not series.get([SR,TYPE,COMPANY, MODEL]).isnull().values.any() and\
#                 not series.get([SR,TYPE,COMPANY,MODEL]).isna().values.any(): 
#                 completeRows.append(series)
#             else:
#                 incompleteRows.append(series)
#     print(counter)
#     return (completeRows , incompleteRows  )
    
        

# allRows:list[pd.Series] = []
# for filePath in paths :
#         try:
#           print(f'reading {filePath}')
#           data_frame = pd.read_excel(filePath,header=None,skiprows=[0,1,2] , usecols=range(0,23))
#           utils.for_each_row(data_frame , function = lambda r : allRows.append(r)  )
#         except:
#             print(f'failed to read {filePath}')


# all_as_data_frame_with_duplicates = pd.concat(allRows ,axis="columns").T
# all_as_data_frame = all_as_data_frame_with_duplicates.drop_duplicates(subset=[SR] , ignore_index=True)

# print(f'duplicates {all_as_data_frame_with_duplicates.shape}')
# print(f'non-duplicates {all_as_data_frame.shape}')

# comp , incomp = processRows(all_as_data_frame)

# v = write_to_csv
# write_to_csv(path='./comp.csv',rows=pd.concat(comp ,axis='columns') ,headers=HEADERS)

# write_to_csv(path='./incomp.csv',rows=pd.concat(incomp ,axis='columns') ,headers=HEADERS)

# with open('./all-with-duplicate.csv' , 'w') as file:
#     file.write(all_as_data_frame_with_duplicates.to_csv(index=False ,header=HEADERS) )


# with open('./all-without-duplicate.csv' , 'w') as file:
#     file.write(all_as_data_frame.to_csv(index=False ,header=HEADERS))

# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', None)
# pd.set_option('display.max_colwidth', None)


# def write_to_csv(path,rows:pd.DataFrame, headers):
#     with open(path, 'w') as file:
#         print(f'writing {rows.shape[1]} rows to {path}')
#         file.write(rows.T.to_csv(index=False , header=headers ))

# def processRows(df:pd.DataFrame):
#     completeRows =[]
#     incompleteRows=[]
#     counter = 0
#     for index, series in df.iterrows():
#         counter= counter +1
#         if str(series.get(TYPE)).upper() in ['PC' ,'LAPTOP' ] :
#             if  not series.get([SR,TYPE,COMPANY,MODEL,PROCESSOR,DISK,RAM]).isnull().values.any() and\
#                 not series.get([SR,TYPE,COMPANY,MODEL,PROCESSOR,DISK,RAM]).isna().values.any(): 
#                 completeRows.append(series)
#             else:
#                 incompleteRows.append(series)
#         else:
#             if not series.get([SR,TYPE,COMPANY, MODEL]).isnull().values.any() and\
#                 not series.get([SR,TYPE,COMPANY,MODEL]).isna().values.any(): 
#                 completeRows.append(series)
#             else:
#                 incompleteRows.append(series)
#     print(counter)
#     return (completeRows , incompleteRows  )
    
        

# paths = []
# for  dirpath, dirnames, filenames in os.walk('/home/abtuly/pandas_projects/New folder'):
#     for file in filenames:
#         paths.append(f'{dirpath}/{file}')

# allRows:list[pd.Series] = []
# for filePath in paths :
#         try:
#           print(f'reading {filePath}')
#           data_frame = pd.read_excel(filePath,header=None,skiprows=[0,1,2] , usecols=range(0,23))
#           utils.for_each_row(data_frame , function = lambda r : allRows.append(r)  )
#         except:
#             print(f'failed to read {filePath}')


# all_as_data_frame_with_duplicates = pd.concat(allRows ,axis="columns").T
# all_as_data_frame = all_as_data_frame_with_duplicates.drop_duplicates(subset=[SR] , ignore_index=True)

# print(f'duplicates {all_as_data_frame_with_duplicates.shape}')
# print(f'non-duplicates {all_as_data_frame.shape}')

# comp , incomp = processRows(all_as_data_frame)

# v = write_to_csv
# write_to_csv(path='./comp.csv',rows=pd.concat(comp ,axis='columns') ,headers=HEADERS)

# write_to_csv(path='./incomp.csv',rows=pd.concat(incomp ,axis='columns') ,headers=HEADERS)

# with open('./all-with-duplicate.csv' , 'w') as file:
#     file.write(all_as_data_frame_with_duplicates.to_csv(index=False ,header=HEADERS) )


# with open('./all-without-duplicate.csv' , 'w') as file:
#     file.write(all_as_data_frame.to_csv(index=False ,header=HEADERS))