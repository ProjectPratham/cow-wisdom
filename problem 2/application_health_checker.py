import requests

def interpret_status_code(status_code):
    if 200 <= status_code < 300:
        return "UP: The application is responding normally."
    elif 300 <= status_code < 400:
        return f"REDIRECT: The application is redirecting requests (status code: {status_code})."
    elif 400 <= status_code < 500:
        return f"CLIENT ERROR: There may be an issue with the request (status code: {status_code})."
    elif 500 <= status_code < 600:
        return f"SERVER ERROR: The server encountered an error (status code: {status_code})."
    else:
        return f"UNKNOWN STATUS: Received unexpected status code {status_code}."

def check_app_health(url):
    try:
        response = requests.get(url, timeout=5, allow_redirects=False)
        print(f"{response}")
        message = interpret_status_code(response.status_code)
        print(f"Checked {url} --> {message}")
    except requests.exceptions.Timeout:
        print(f"TIMEOUT: The application at {url} did not respond in time.")
    except requests.exceptions.ConnectionError:
        print(f"CONNECTION ERROR: Unable to reach the application at {url}.")
    except requests.exceptions.RequestException as e:
        print(f"ERROR: An unexpected error occurred while checking {url}. Details: {e}")

# Example usage
user_url = input("Enter the URL to check (including https://): ").strip()
check_app_health(user_url)
