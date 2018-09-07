# python-practice
Files :
1. parseCSV.py
The main logic of parsing the raw.csv file has been included in parseCSV.py file
2. parse_csv.py 
This file is simply used to call the functions of parseCSV.py file
To make the csv file location configurable,user can provide the filepath as a parameter in cmd

Please follow the steps below to execute the csv file parsing:
1. Go to command prompt and  type parse_csv.py -f <csv-file-location>
  for example : parse_csv.py -f "C:\Users\ABC\Test\raw.csv"
2. The output csv file would be saved in the current working directory with name modified.csv
