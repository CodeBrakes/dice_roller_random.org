import re
import json
import time
import requests

#Call API of Random.org
url = 'https://api.random.org/json-rpc/1/invoke'
#The API key of Random.org
API_KEY= '19a5d4bd-5dc0-46d5-8562-fa9aa3ebecaa'
#Data to be requested from Random.org
data = {'jsonrpc':'2.0','method':'generateIntegers','params': {'apiKey': API_KEY,'n':10,'min':1,'max':6,'replacement':'true','base':10},'id':24565}
#Pass data to json parser
params = json.dumps(data)
#set a response with the URL ans the additional json
response = requests.post(url,params)

print("\n************* RANDOM.ORG DICE GENERATOR *************\n")

print('The original RANDOM.ORG json is: ')
#print the returned json from random.org
print(response.text)

#empyt list
num_list = []

#counters
cnt=0
cnt_1=0
cnt_2=0
cnt_3=0
cnt_4=0
cnt_5=0
cnt_6=0

#For each row located in response.text do the following
for row in str(re.sub('[^0-9]', '', response.text)):
    #if main character counter is between 1 and 12 then do the following
    if(cnt > 1 and cnt < 12):
        #count hom many times number 1 appered on the set numbers
        if   (row.count('1')):  cnt_1 = cnt_1 + 1
        #count hom many times number 2 appered on the set numbers
        elif (row.count('2')):  cnt_2 = cnt_2 + 1
        #count hom many times number 3 appered on the set numbers
        elif (row.count('3')):  cnt_3 = cnt_3 + 1
        #count hom many times number 4 appered on the set numbers
        elif (row.count('4')):  cnt_4 = cnt_4 + 1
        #count hom many times number 5 appered on the set numbers
        elif (row.count('5')):  cnt_5 = cnt_5 + 1
        #count hom many times number 6 appered on the set numbers
        elif (row.count('6')):  cnt_6 = cnt_6 + 1

        num_list.append(int(row))
    cnt = cnt + 1


print("\nThe RANDOM.ORG list is: ", num_list)
print("\n****************** NUMBER OCCURRENCES ******************\n")

#print the occurences of numbers
print('Number 1 appeared: ', cnt_1, ' | ' 
      'Number 2 appeared: ', cnt_2, ' | '
      'Number 3 appeared: ', cnt_3, ' \n' 
      'Number 4 appeared: ', cnt_4, ' | '
      'Number 5 appeared: ', cnt_5, ' | '
      'Number 6 appeared: ', cnt_6,)

print("\nThe sorted number list is: ", sorted(num_list))

print('\nConverting sorted list into json object...\n')

#format to json
jsr = {
  "dice": sorted(num_list)
}
#convert element to json
json_format = json.dumps(jsr)
#wait for 3 minutes (cause it is cool) and print converted json
time.sleep(3)
print('\nThe json is: ', json_format)


print('\nSending json POST to RANDOM.ORG..')
time.sleep(3)

jsa = {"jsonrpc":"2.0","params":{"code":-32602,"message":"Sorted Dice Numbers","data":sorted(num_list)},"id": 43517}
params = json.dumps(jsa)
print('\nThe answer of RANDOM.ORG is: \n')
x = requests.post(url, data = params)

print(x.text)
