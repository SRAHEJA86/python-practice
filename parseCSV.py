import csv
from argparse import ArgumentParser
import pandas as pd
import datetime as dt
try:
          def input_file_name():
                #to take the csv file path as an argument from cmd
                parser = ArgumentParser()
                parser.add_argument("-f", "--file", dest="myFile", help="Open specified file")
                args = parser.parse_args()
                myFile = args.myFile
                return myFile
            
          def parse_csv(myFile):
                dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S')# required for extraction of date from datetime
                parsed_data = pd.read_csv(myFile,parse_dates=['ds'],date_parser=dateparse)
                print(parsed_data.head(2))#prints the first 2 rows
                return parsed_data

          def drop_null_rows(parsed_data):
                parsed_data_without_null = parsed_data.dropna()#drops the rows with null data
                print(parsed_data_without_null.head(2))# prints the first 2 rows without null date
                return parsed_data_without_null
            
          def aggregate_by_date(parsed_data_without_null):
                # to extract date from datetime
                df1 = parsed_data_without_null.copy()
                df1['ds'] = pd.to_datetime(df1['ds'],format='%Y%m%d', errors='ignore').dt.date
                df1=df1.groupby(['ds','Year'])[["Vancouver", "Portland", "San Francisco","Seattle"]].sum()#aggregate the weather data on the basis of dates
                # Writing the modified data into csv file
                df1.to_csv("modified.csv")
            

except Exception as e:
            print('Error while parsing and processing date from csv:',e)
    
           

