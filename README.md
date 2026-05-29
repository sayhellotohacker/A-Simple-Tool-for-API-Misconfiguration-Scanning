# HTTP Method Tester – A Simple Tool for API Misconfiguration Scanning

This Python script sends HTTP requests to a given URL using all standard HTTP methods (GET, POST, PUT, DELETE, HEAD, TRACE, OPTIONS, PATCH) and displays the response status code and headers for each method.

It is designed to help security researchers, developers, and penetration testers quickly identify **HTTP method misconfigurations**, such as:

- Unexpectedly enabled methods (e.g., TRACE, PUT, DELETE on production endpoints)
- Improper CORS or authentication handling
- Hidden debug endpoints
- Verb tampering vulnerabilities

The script is lightweight, easy to extend, and perfect for inclusion in your security testing toolkit.

---

## 🚀 Features

- Tests **all 8 HTTP methods** in one run  
- Sends custom **JSON data** (parsed or raw)  
- Shows **status codes** and **response headers** for each method  
- Handles errors gracefully per method  
- Clean, readable console output  

---

## 📦 Requirements

- Python 3.6 or higher  
- `requests` library (install with `pip install requests`)  

No external dependencies other than `requests` (standard library `json` is used).

---

## 📋 Usage

Run the script from the terminal:

```bash
python http_method_tester.py
```

You will be prompted for:

1. **URL** – the target endpoint (e.g., `https://example.com/api/resource`)
2. **JSON data** (optional) – if you want to send a body (e.g., `{"key": "value"}`). Leave empty for no data.

Example interaction:

```
Enter URL: https://httpbin.org/put
Enter JSON data (or leave empty): {"name": "test"}

============================================================
 POST --> https://httpbin.org/put
============================================================
 Status Code: 200
 Headers:
 Content-Type: application/json
 ...
```

The script will iterate over all methods and print a block for each.

---

## 🔍 How It Works

1. The user provides a URL and optional JSON data.  
2. For each HTTP method, the script builds the appropriate request:
   - **GET** – sends data as query parameters (`params`)
   - **POST, PUT, PATCH, DELETE** – sends data as JSON body (`json`)
   - **HEAD, TRACE, OPTIONS** – no body sent
3. A simple `User-Agent` header (`AdvancedPythonClient/2.0`) is added to avoid basic blocking.  
4. The response status code and all response headers are printed.  
5. If any method fails (timeout, connection error, etc.), the error is shown but execution continues with the next method.

---

## 📁 Sample Output

```
============================================================
 GET --> https://example.com/api/users
============================================================
 Status Code: 200
 Headers:
 Content-Type: application/json
 ...

============================================================
 POST --> https://example.com/api/users
============================================================
 Status Code: 405
 Headers:
 Allow: GET, HEAD, OPTIONS
 ...
```

From the output you can immediately see that `POST`, `PUT`, `DELETE`, and others are **not allowed** (405 Method Not Allowed), and the `Allow` header shows which methods are actually permitted – a clear sign of a well-configured endpoint.

---

## 💡 When to Use This Tool

- **Security audits** – Quickly check if sensitive endpoints allow unintended methods.  
- **API testing** – Verify that your API returns correct `405` for disallowed methods.  
- **Bug bounty / CTF** – Discover hidden endpoints or debug methods like `TRACE` or `OPTIONS`.  
- **Resume / portfolio** – Demonstrates practical Python scripting and security awareness.

---

## ⚠️ Disclaimer

This script is intended for **educational and authorised testing purposes only**. Do not use it against systems you do not own or have explicit permission to test. Unauthorised scanning may be illegal.

---

## 🧑‍💻 Extending

You can easily modify the script to:

- Show response body (just add `print(response.text)` inside the loop)  
- Add authentication headers (Bearer token, Basic auth)  
- Output results in JSON format  
- Add multiple URLs from a file  

Example extension for showing body:

```python
if method != "HEAD":
    print(" Body:", response.text[:500])
```

---

## 📄 License

MIT – free to use, modify, and share. No warranty.

---

*Written for a clean, professional GitHub profile – simple code, clear purpose.*

Author: Miaad Shirvani
Date: May 29, 2026
