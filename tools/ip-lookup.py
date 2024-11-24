import requests
from pystyle import Colors, Colorate
import os
from datetime import datetime

def fade(text: str) -> str:
    return Colorate.Horizontal(Colors.purple_to_blue, text, 1)

def ip_lookup(ip_address):
    try:
        url = f"http://ip-api.com/json/{ip_address}"
        
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            if data['status'] == 'success':
                return data
            else:
                return {"error": f"Unable to fetch details: {data.get('message', 'Unknown error')}"}
        else:
            return {"error": f"HTTP Error: {response.status_code}"}
    
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}

if __name__ == "__main__":
    banner = r"""
            ______              
         .-'      `-.           
       .'            `.         
      /                \        
     ;                 ;`       
     |                 |;       
     ;                 ;|
     '\               / ;       
      \`.           .' /        
       `.`-._____.-' .'         
         / /`_____.-'           
        / / /                   
       / / /
      / / /
     / / /
    / / /
   / / /
  / / /
 / / /
/ / /
\/_/
"""

    print(Colorate.Horizontal(Colors.purple_to_blue, banner, 1))
    time = datetime.now().strftime("%H:%M:%S")
    ip = input(f"\n{fade("[")}{time}{fade("]")} > Enter IP: ")

    result = ip_lookup(ip)
    
    if 'error' in result:
        time = datetime.now().strftime("%H:%M:%S")
        print(f"{fade("[")}{time}{fade("]")} Error: {Colorate.Color(Colors.red, f"{result['error']}")}")
    else:
        time = datetime.now().strftime("%H:%M:%S")
        print(f"{fade("[")}{time}{fade("]")} Details for IP Address: {ip}")
        time = datetime.now().strftime("%H:%M:%S")
        print(f"{fade("[")}{time}{fade("]")} Country: {result['country']}")
        time = datetime.now().strftime("%H:%M:%S")
        print(f"{fade("[")}{time}{fade("]")} Region: {result['regionName']}")
        print(f"{fade("[")}{time}{fade("]")} City: {result['city']}")
        time = datetime.now().strftime("%H:%M:%S")
        print(f"{fade("[")}{time}{fade("]")} ZIP: {result['zip']}")
        time = datetime.now().strftime("%H:%M:%S")
        print(f"{fade("[")}{time}{fade("]")} Latitude: {result['lat']}")
        time = datetime.now().strftime("%H:%M:%S")
        print(f"{fade("[")}{time}{fade("]")} Longitude: {result['lon']}")
        time = datetime.now().strftime("%H:%M:%S")
        print(f"{fade("[")}{time}{fade("]")} ISP: {result['isp']}")
        time = datetime.now().strftime("%H:%M:%S")
        print(f"{fade("[")}{time}{fade("]")} Organization: {result['org']}")

    time = datetime.now().strftime("%H:%M:%S")
    input(f"{fade("[")}{time}{fade("]")} Press any key to go back.")
    os.system("python master.py")
