import requests
import json
import urllib.request

# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
scoring_uri = 'http://203c9965-4a91-44ed-9289-c0aae9fd29c6.southcentralus.azurecontainer.io/score'
# If the service is authenticated, set the key or token
key = 'rqIzFsXtau3w6lJUkulbem8ZLFwBPHKu'

# Two sets of data to score, so we get two results back
data = {"Inputs": {
        "data":
        [
          {
            "age": 17,
            "job": "blue-collar",
            "marital": "married",
            "education": "university.degree",
            "default": "no",
            "housing": "yes",
            "loan": "yes",
            "contact": "cellular",
            "month": "may",
            "day_of_week": "mon",
            "duration": 971,
            "campaign": 1,
            "pdays": 999,
            "previous": 1,
            "poutcome": "failure",
            "emp.var.rate": -1.8,
            "cons.price.idx": 92.893,            
            "cons.conf.idx": -46.2,
            "euribor3m": 1.299,         
            "nr.employed": 5099.1
          },
          {
            "age": 87,
            "job": "blue-collar",
            "marital": "married",
            "education": "university.degree",
            "default": "no",
            "housing": "yes",
            "loan": "yes",
            "contact": "cellular",
	          "month": "may",
			      "day_of_week": "mon",
            "duration": 471,
            "campaign": 1,
            "pdays": 999,
            "previous": 1,
            "poutcome": "failure",
            "emp.var.rate": -1.8,
            "cons.price.idx": 92.893,
            "cons.conf.idx": -46.2,    
            "euribor3m": 1.299,            
            "nr.employed": 5099.1
          },
      ]
    },
      "GlobalParameters": {
        "method": "predict"
    }
  }
# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {'Content-Type': 'application/json'}
# If authentication is enabled, set the authorization header
headers['Authorization'] = f'Bearer {key}'

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())

#input_data = str.encode(json.dumps(data))
#req = urllib.request.Request(scoring_uri, input_data, headers)
#try:
    #response = urllib.request.urlopen(req)
    #result = response.read()
    #print(result)
#except urllib.error.HTTPError as error:
    #print("The request failed with status code: " + str(error.code))