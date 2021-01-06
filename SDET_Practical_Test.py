# import libraries
import json
import requests
import pandas as pd 


# 1. Query REST API with Basic Authentication which returns XML or JSON
# safe url
api_test = 'http://api.open-notify.org/astros.json'

# safe request response
response = requests.get(api_test)
# print(get_response(api_test))  # check response == 200
# print (response.json())  # look at the response

# safe response in easy to read format
result = json.loads(response.text)
# print(result)

# print('Keys:', result.keys())  # print keys

# 2. Convert the response into pandas dataframe
temp = []  # to safe the results
#  loop through the result
for k, v in enumerate(result['people']):  
    # safe the result
    user_dict = (k, v['craft'], v['name'])
    temp.append(user_dict)

# print(temp)   

# 3. Filter the dataframe by values in 1, 2, bonus: n columns
df = pd.DataFrame(temp, columns = ['item', 'craft', 'name'])
# print(df)

# 4. Bonus: run python tests like unittest, pytest, nosetest
def get_response(api_test):
    '''
    returns status code of the request
    '''
    response = requests.get(api_test)
    return response.status_code

