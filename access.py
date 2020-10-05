import requests  # this gives us the ability to use different requests methods
import json  # this gives us the ability to use different methods involving JSON files

# Below is the skeleton code to complete the requests. The base URL Call has been provided to you. You can run the code as is and see what is provided.
# Feel free to ask any workshop officer questions if you are stuck
# Sample Code is present at the bottom of the Python file

# NOTE: Postman can be used to your aid, however, you MUST implement the code below in addition (we will check).

# QUESTION: How do I format my parameters?
# ANSWER: The key will be specified in the question, and you will replace value with your response
#         {"key": "value"}

# Ready... GET set... POST!

# This is the starting GET request, already completed for you! It returns the first set of instructions (in JSON) and is currently printing it to the console
def gettingStarted():
  response = requests.get(
    'https://acc-dsc-api.herokuapp.com'
    
    # this request does not require any params but if it did, it would look like this:
    # your formatting for some of the next questions will require this line to be uncommented and filled in accordingly
    #
    # json={"answer": "my_answer"},

  )

  json_data = response.text

  return json_data

print(gettingStarted())

# Sample Code

# GET Request
# Used to retrieve information. These do not normally require any additional parameters when making a response.

# Python Code:
# def getRequest():
#   response = requests.get (
#     'route (url) of the api you are accessing'
#   )
#   json_data = response.text
#   return json_data
#
# print(getRequest())


# POST Request
# Used to submit data. These may require additional parameters, such as the information that you want to submit.

# Python Code:
# def postRequest():
#   response = requests.post (
#     'route (url) of the api you are accessing',
#     json = {'somekey': 'somevalue'} # data is optional and is where you would supply any answers you want to submit for this activity
#   )
#   json_data = response.text
#   return json_data
#
# print(postRequest())
