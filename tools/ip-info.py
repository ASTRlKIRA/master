import requests
import ipaddress
from pystyle import Colors, Colorate
import os
from datetime import datetime

def fade(text: str) -> str:
    return Colorate.Horizontal(Colors.purple_to_blue, text, 1)

def version(ip_address):
    try:
        ip = ipaddress.ip_address(ip_address)
        ip_version = "IPv4" if ip.version == 4 else "IPv6"
        return ip_version
    except ValueError:
        return "Invalid IP", "Unknown"

def info(ip_address=""):
    try:
        url = f"https://ipinfo.io/{ip_address}/json"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        ip = data.get("ip", "N/A")
        hostname = data.get("hostname", "N/A")
        city = data.get("city", "N/A")
        region = data.get("region", "N/A")
        country = data.get("country", "N/A")
        loc = data.get("loc", "N/A")
        org = data.get("org", "N/A")
        postal = data.get("postal", "N/A")
        timezone = data.get("timezone", "N/A")

        ip_version = version(ip)

        time = datetime.now().strftime("%H:%M:%S")

        print(f"{fade("[")}{time}{fade("]")} IP: {ip}")
        print(f"{fade("[")}{time}{fade("]")} Host Name: {hostname}")
        print(f"{fade("[")}{time}{fade("]")} Host Country: {country}")
        print(f"{fade("[")}{time}{fade("]")} Region: {region}")
        print(f"{fade("[")}{time}{fade("]")} City: {city}")
        print(f"{fade("[")}{time}{fade("]")} Location (Lat, Long): {loc}")
        print(f"{fade("[")}{time}{fade("]")} Postal Code: {postal}")
        print(f"{fade("[")}{time}{fade("]")} Timezone: {timezone}")
        print(f"{fade("[")}{time}{fade("]")} ISP/Organization: {org}")
        print(f"{fade("[")}{time}{fade("]")} IP Version: {ip_version}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching IP info: {e}")
    except ValueError as ve:
        print(f"Invalid IP address: {ve}")

if __name__ == "__main__":
    banner = r"""

             ..,,;;;;;;,,,,
       .,;'';;,..,;;;,,,,,.''';;,..
    ,,''                    '';;;;,;''
   ;'    ,;@@;'  ,@@;, @@, ';;;@@;,;';.
  ''  ,;@@@@@'  ;@@@@; ''    ;;@@@@@;;;;
     ;;@@@@@;    '''     .,,;;;@@@@@@@;;;
    ;;@@@@@@;           , ';;;@@@@@@@@;;;.
     '';@@@@@,.  ,   .   ',;;;@@@@@@;;;;;;
        .   '';;;;;;;;;,;;;;@@@@@;;' ,.:;'
          ''..,,     ''''    '  .,;'
               ''''''::''''''''
"""

    print(Colorate.Horizontal(Colors.purple_to_blue, banner, 1))
    time = datetime.now().strftime("%H:%M:%S")
    ip = input(f"\n{fade("[")}{time}{fade("]")} > Enter IP: ").strip()
    info(ip)

    time = datetime.now().strftime("%H:%M:%S")
    input(f"{fade("[")}{time}{fade("]")} Press any key to go back.")
    os.system("python master.py")
