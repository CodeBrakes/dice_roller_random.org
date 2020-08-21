import re
import json
import time
import requests

url = 'https://api.random.org/json-rpc/1/invoke'
API_KEY= '19a5d4bd-5dc0-46d5-8562-fa9aa3ebecaa'
data = {'jsonrpc':'2.0','method':'generateIntegers','params': {'apiKey': API_KEY,'n':10,'min':1,'max':6,'replacement':'true','base':10},'id':24565}
params = json.dumps(data)
response = requests.post(url,params)

print("\n************* RANDOM.ORG DICE GENERATOR *************\n")

print('The original RANDOM.ORG json is: ')
print(response.text)

num_list = []
cnt=0
cnt_1=0
cnt_2=0
cnt_3=0
cnt_4=0
cnt_5=0
cnt_6=0
for row in str(re.sub('[^0-9]', '', response.text)):
    if(cnt > 1 and cnt < 12):
        if   (row.count('1')):  cnt_1 = cnt_1 + 1
        elif (row.count('2')):  cnt_2 = cnt_2 + 1
        elif (row.count('3')):  cnt_3 = cnt_3 + 1
        elif (row.count('4')):  cnt_4 = cnt_4 + 1
        elif (row.count('5')):  cnt_5 = cnt_5 + 1
        elif (row.count('6')):  cnt_6 = cnt_6 + 1

        num_list.append(int(row))
    cnt = cnt + 1


print("\nThe RANDOM.ORG list is: ", num_list)
print("\n****************** NUMBER OCCURRENCES ******************\n")
print('Number 1 appeared: ', cnt_1, ' | ' 
      'Number 2 appeared: ', cnt_2, ' | '
      'Number 3 appeared: ', cnt_3, ' \n' 
      'Number 4 appeared: ', cnt_4, ' | '
      'Number 5 appeared: ', cnt_5, ' | '
      'Number 6 appeared: ', cnt_6,)

print("\nThe sorted number list is: ", sorted(num_list))

print('\nConverting sorted list into json object...\n')

jsr = {
  "dice": sorted(num_list)
}
json_format = json.dumps(jsr)
time.sleep(3)
print('\nThe json is: ', json_format)


print('\nSending json POST to RANDOM.ORG..')
time.sleep(3)

jsa = {"jsonrpc":"2.0","params":{"code":-32602,"message":"Sorted Dice Numbers","data":sorted(num_list)},"id": 43517}
params = json.dumps(jsa)
print('\nThe answer of RANDOM.ORG is: \n')
x = requests.post(url, data = params)

print(x.text)
