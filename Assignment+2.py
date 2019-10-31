
import pandas as pd

df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index) 
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')
df.head(55)



# You should write your whole answer within the function provided. The autograder will call
# this function and compare the return value against the correct solution value
def answer_zero():
    # This function returns the row for Afghanistan, which is a Series object. The assignment
    # question description will tell you the general format the autograder is expecting
    return df.iloc[0]

# You can examine what your function returns by calling it in the cell. If you have questions
# about the assignment formats, check out the discussion forums for any FAQs
answer_zero() 

def answer_one():
    a = df.where(df["Gold"] == max(df["Gold"]))
    a=a.dropna()
    s= a.reset_index()
    s.T[0][0]
    return s.T[0][0]

def answer_two():
    df["Diff"]= abs(df["Gold"]-df["Gold.1"])
    b = df.where(df["Diff"] == max(df["Diff"]))
    b=b.dropna()
    s= b.reset_index()
    s.T[0][0]
    return s.T[0][0]

 def answer_three():
    c=df.where((df["Gold"]>=1) & (df["Gold.1"]>=1))
    z=c.dropna()
    z["Diff"]= abs(z["Gold"]-z["Gold.1"])
    z["Ratio"]= (z["Diff"]/(z["Gold.2"] ))
    y = z.where((z["Ratio"])==max(z["Ratio"]))
    return y.first_valid_index()

def answer_four():
    df["Points"] = ((3*df["Gold.2"])+ (2 *(df["Silver.2"])) + df["Bronze.2"]) 
    return df["Points"]

import pandas as pd
census_df = pd.read_csv('census.csv')
census_df.head()



def answer_five():
    df1=census_df.copy()
    df1 =df1.where(df1["SUMLEV"]== 50)
    df2= df1.groupby("STNAME").sum()
    df3= df2.sort_values(("COUNTY"), ascending =False)
    return(df3.index[0])  

def answer_six():   
    z=[]
    df2= census_df.sort_values(["STNAME", "CENSUS2010POP"], ascending = False) 
    list = df2['STNAME'].unique()
    for x in list:
        for y in range (3):
            count=0
            if df2["STNAME"][y] == x:
                count+= df2["CENSUS2010POP"][y]
        z.append([x,count])
        z.sort(reverse=True)
    a=z[:3]
    b=[a[0][0],a[1][0],a[2][0]]
    return b 

def answer_seven():
    df3 =census_df.where(census_df["SUMLEV"]== 50)
    df3= df3[["CTYNAME","POPESTIMATE2015","POPESTIMATE2014","POPESTIMATE2013","POPESTIMATE2012","POPESTIMATE2011","POPESTIMATE2010"]]
    df4 =df3.set_index("CTYNAME")
    df4["Difference"] = abs(df4.max(axis=1)-df4.min(axis=1))
    df4= df4.sort_values(("Difference"), ascending =False)
    return df4.index[0]

def answer_eight():
    df4 =census_df.where(((census_df["REGION"]== 1) | (census_df["REGION"]== 2)) & (census_df["CTYNAME"].str.startswith('Washington')) & (census_df["POPESTIMATE2015"] > census_df["POPESTIMATE2014"]))
    df5=df4.dropna()
    return df5[['STNAME','CTYNAME']] 
