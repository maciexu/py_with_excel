import pandas as pd

# Series
print("-"*30 + "Section 1 Series" + "-"*30)

S1 = pd.Series(['a', 'b', 'c', 'd', 'e'])
print(S1)

df = pd.read_excel(r'C:\Users\mengx\Downloads\Data_Extract_From_Education_Statistics_-_All_Indicators.xlsx', sheet_name='Data')
# sheet_name = 0
# index_col = 0   the index would be the first col, not the default index 0, 1, 2.....
df = pd.read_excel(r'C:\Users\mengx\Downloads\Data_Extract_From_Education_Statistics_-_All_Indicators.xlsx', sheet_name='Data', index_col=0)

# head
df = pd.read_excel(r'C:\Users\mengx\Downloads\Data_Extract_From_Education_Statistics_-_All_Indicators.xlsx', sheet_name='Data', index_col=0, head=0)

# usecols is be a list
# nrows must be integer, display top nrows 
df = pd.read_excel(r'C:\Users\mengx\Downloads\Data_Extract_From_Education_Statistics_-_All_Indicators.xlsx',  usecols=[3,4,5,6,7,8,9,10], nrows=8)
print(df)



# Note: csv has seperater!!!!
# read_csv(r'XXXXXX.csv', sep=' ')       sep can be blank space, or comma
# *.csv(gbk) and .csv(UTF-8) are different!!     
# .csv by default is UTF-8
# gbk.csv     2nd argument must be encoding = 'gbk'

# txt, read_table can be used for all seperatered files, and sep must be defined



