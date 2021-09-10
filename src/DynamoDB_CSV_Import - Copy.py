# Python Script to insert csv records in dynamodb table.
from __future__ import print_function  # Python 2/3 compatibility
from __future__ import division  # Python 2/3 compatiblity for integer division
import argparse
import boto3
from csv import reader
import time
import os
# command line arguments
parser = argparse.ArgumentParser(
    description='Write CSV records to dynamo db table. CSV Header must map to dynamo table field names.')
parser.add_argument('csvFile', help='..\\data\\raw\\hospital_account_infoNew.csv')
parser.add_argument('table', help='hospital_account_info')
parser.add_argument('writeRate', default=5, type=int, nargs='?',
                    help='Number of records to write in table per second (default:5)')
parser.add_argument('delimiter', default=',', nargs='?', help='Delimiter for csv records (default=,)')
parser.add_argument('region', default='us-east-1', nargs='?', help='Dynamo db region name (default=us-east-1')
args = parser.parse_args()
print(args)

# dynamodb and table initialization
endpointUrl = "https://dynamodb.us-east-1.amazonaws.com"
dynamodb = boto3.resource('dynamodb', region_name=args.region, endpoint_url=endpointUrl)
table = dynamodb.Table(args.table)
print(table.name)
table_name=table.name
Account_Num='0'
id_counter=1
id_table = boto3.resource('dynamodb').Table('hospital_account_info')

# write records to dynamo db
with open(args.csvFile) as csv_file:
    tokens = reader(csv_file, delimiter=args.delimiter)
    # read first line in file which contains dynamo db field names
    header = next(tokens)
    #print filename
    csv_file_name=os.path.splitext(os.path.split(csv_file.name)[1])[0]
    print(csv_file_name)
    print(id_table)
  
    # read second line in file which contains dynamo db field data types
    headerFormat = next(tokens)
    # rest of file contain new records
    for token in tokens:
        #print(token)
        
        item = {}
      
        for i, val in enumerate(token):
            #print(val)
            #item[id_counter]=new_id
            if val:
                key = header[i]
                if headerFormat[i] == 'int':
                    val = int(val)
                    #print(val)
                if headerFormat[i] == 'stringset':
                    tempVal = val.split('|')
                    val = set()
                    for tok in enumerate(tempVal):
                        #print(tok)
                        val.add(str(tok[1]))
                #print(val)
                item[key] = val
                id_counter = val
                print(header[i])
                #print(header[val])
          #print(item)
        table.put_item(Item=item)
        time.sleep(1 / args.writeRate)  # to accomodate max write provisioned capacity for table
