import requests
import json

def send_requests(url, data):
    methods = ["POST", "GET", "PUT", "DELETE", "HEAD", "TRACE", "OPTIONS", "PATCH"]

    headers = {
        "User-Agent": "AdvancedPythonClient/2.0",
        "Content-Type": "application/json"
    }

    for method in methods:
        print("\n" + "="*60)
        print(f" {method} --> {url}")
        print("\n"+ "=" *60)

        try:
            request_kwargs = {
                "headers": headers,
                "timeout": 10
            }

            # Set data by method
            if method == "GET":
                request_kwargs["params"] = data
            elif method in ["POST", "PUT", "PATCH", "DELETE"]:
                request_kwargs["json"] = data
            elif method == "TRACE":
                pass
            elif method == "HEAD":
                pass
            elif method == "OPTIONS":
                pass

            response = requests.request(method, url, **request_kwargs)

            print(f" Status Code: {response.status_code}")
            print(" Headers:")
            for key, value in response.headers.items():
                print(f"{key}: {value}")

        except requests.exceptions.RequestException as e:
            print(f"❌ Error in {method}: {e}")


if __name__ == "__main__":
    url = input("Enter URL: ").strip()
    raw_data = input("Enter JSON data (or leave empty): ").strip()

    if raw_data:
        try:
            data = json.loads(raw_data)
        except json.JSONDecodeError:
            print("⚠ Invalid JSON. Sending as string.")
            data = {"data": raw_data}
    else:
        data = {}

    send_requests(url, data)
