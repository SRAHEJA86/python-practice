import parseCSV

myFile = parseCSV.input_file_name()
parsed_data = parseCSV.parse_csv(myFile)
parsed_data_without_null = parseCSV.drop_null_rows(parsed_data)
parseCSV.aggregate_by_date(parsed_data_without_null)
