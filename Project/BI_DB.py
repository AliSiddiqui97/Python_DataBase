import pandas as pd
import pyodbc 
import numpy as np
import sys


def convert_SQL(df,filename):
    qry_str = 'CREATE TABLE '+filename+'('
    df_type = df.dtypes
    df_col = df.columns
    for i in range(len(df_type)): 
        if str(df_type[i]) in "object":
            qry_str = qry_str +df.columns[i]+' '+'text, '
        elif str(df_type[i]) in "float64":
            qry_str = qry_str +df.columns[i]+' '+'float,  '
        elif str(df_type[i]) in "int64":
            qry_str = qry_str +df.columns[i]+' '+'numeric(18, 0), '
        elif str(df_type[i]) in "datetime64[ns]":
            qry_str = qry_str +df.columns[i]+' '+'datetime, '
    qry_str = qry_str[:-2]+')'


    CREATE_TABLE(qry_str)
    INSERT(df,filename)

def read_SQL(name):
    qry_str = 'SELECT * from '+name
    conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-P707RUQ\SQLEXPRESS;'
                        'Database=VH_Automation;'
                        'Trusted_Connection=yes;')
    cur = conn.cursor()
    cur.execute(qry_str)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
   
    return pd.DataFrame(rows)



def get_row(df,num, filename):
    df_col = df.columns
    msg='INSERT INTO '+filename+' VALUES('
    for i in df_col:
        if (str(df[i].dtypes) not in 'float64') and (str(df[i].dtypes) not in 'int64'):
            msg += "'"+str(df[i][num])+"', "
        else:
            msg += str(df[i][num])+", "
    msg = msg[:-2]
    msg=msg.replace('nan','0')
    
    print(msg +')')
    return (msg +')')

def INSERT(df,filename):
   
    
    conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-P707RUQ\SQLEXPRESS;'
                        'Database=VH_Automation;'
                        'Trusted_Connection=yes;')
    cur = conn.cursor()
    for i in range(len(df)):
        try:
            cur.execute(get_row(df,i,filename))
        except:
            print("Variable x is not defined")
        
    
    conn.commit()
    conn.close()
   


def CREATE_TABLE(qry_str):
   
    
    conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-P707RUQ\SQLEXPRESS;'
                        'Database=VH_Automation;'
                        'Trusted_Connection=yes;')
    cur = conn.cursor()
    cur.execute(qry_str)
    conn.commit()
    conn.close()

def main(a,b):
    
    optionToRead = a
    filename = b
    print(optionToRead,filename)
    if(optionToRead !='3'):
        ext = filename.split('.')
        filename = ext[0]
        ext = ext[1]
        
    if optionToRead=='1':
        df= pd.read_csv(filename+'.'+ext)
    elif optionToRead=='3':
        df = read_SQL(filename)

    elif optionToRead=='2':
        df = pd.read_excel(filename+'.'+ext)
    else:
        print('Yo boi dis crashin... x)')

    print(df.head(5))

    # df_type = df.dtypes
    # df_col = df.columns
    # print(df_type)
    # print(df_col)

    while(True):
        choice =  input()
        if(choice == '1'):
            print('you chose data cleaning')
            print('Press')
            print('Press "1" to view column name')
            print('Press "2" to view column name and their types')
            print('Press "q" to Quit')
            
            
            choice = input()
            if(choice=='q'):
                break
            elif choice=='1':
                print_col_name(df)
            elif choice =='2':
                print_col_name_type(df)
        else:
            print('You chose machine learning')
    # convert_SQL(df,filename)
    # print(df.head(2))

main('1','csv.csv')