import requests
test_url = "https://www.163.com/"
response = requests.get(test_url)
print(response.status_code)
print(response.headers)
# print(response.text)