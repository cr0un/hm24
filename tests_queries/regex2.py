import requests

url = "http://127.0.0.1:5000/perform_query"
payload = {
   'file_name': 'apache_logs.txt',
   'cmd1': 'regex',
   'value1': 'images/\\w+\\.png',
   'cmd2': 'sort',
   'value2': 'asc'
}
response = requests.post(url, json=payload)
print(response.text)
