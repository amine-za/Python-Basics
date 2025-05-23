import requests

response = requests.get("https://api.github.com")
print(response.status_code)      # Should print 200 if successful
open("response.txt", "w").write(response.text)  # Save the response text to a file