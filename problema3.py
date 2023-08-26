import requests
url = 'https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=870&q=80'
response = requests.get(url)
with open('perrito_cute.jpg', 'wb') as f:
    f.write(response.content)
    pass