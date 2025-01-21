import requests

# Replace with the correct raw URL
url = input("Enter the url of the raw github page you would like to read: ")

try:
    r = requests.get(url)
    if r.status_code == 200:
        # Display the file content
        print("File content:")
        print(r.text)
    else:
        print(f"Failed to fetch the file. Status code: {r.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

