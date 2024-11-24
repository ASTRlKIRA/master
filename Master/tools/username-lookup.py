import requests
import time
from concurrent.futures import ThreadPoolExecutor
from pystyle import Colors, Colorate
import os
from datetime import datetime

def fade(text: str) -> str:
    return Colorate.Horizontal(Colors.purple_to_blue, text, 1)

websites = {
    "TikTok": "https://www.tiktok.com/@{}",
    "Telegram": "https://t.me/{}",
    "WeChat": "https://www.wechat.com/en/{}",
    "WhatsApp": "https://wa.me/{}",
    "Twitter": "https://x.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "Pinterest": "https://www.pinterest.com/{}/",
    "Discord": "https://discord.com/users/{}",
    "Quora": "https://www.quora.com/profile/{}",
    "LinkedIn": "https://www.linkedin.com/in/{}",
    "Snapchat": "https://www.snapchat.com/add/{}",
    "Instagram": "https://www.instagram.com/{}/",
    "Facebook": "https://www.facebook.com/{}",
    "YouTube": "https://www.youtube.com/c/{}",
    "Twitch": "https://www.twitch.tv/{}",
    "Spotify": "https://open.spotify.com/user/{}",
    "Tumblr": "https://{}.tumblr.com/",
    "Medium": "https://medium.com/@{}",
    "Vimeo": "https://vimeo.com/{}",
    "GitHub": "https://github.com/{}",
    "GitLab": "https://gitlab.com/{}",
    "Behance": "https://www.behance.net/{}",
    "Dribbble": "https://dribbble.com/{}",
    "Steam": "https://steamcommunity.com/id/{}",
    "Flickr": "https://www.flickr.com/photos/{}",
    "StackOverflow": "https://stackoverflow.com/users/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "Twitch": "https://www.twitch.tv/{}",
    "Discord": "https://discord.com/users/{}",
    "Grindr": "https://grindr.com/{}",
    "OkCupid": "https://www.okcupid.com/profile/{}",
    "Bumble": "https://bumble.com/user/{}",
    "Tinder": "https://tinder.com/@{}",
    "Hinge": "https://www.hinge.co/users/{}",
    "Badoo": "https://badoo.com/en/{}",
    "Match": "https://www.match.com/profile/{}",
    "Rumble": "https://rumble.com/user/{}",
    "Clubhouse": "https://www.joinclubhouse.com/@{}",
    "Snapchat": "https://www.snapchat.com/add/{}",
    "Xiaohongshu (RED)": "https://www.xiaohongshu.com/user/profile/{}",
    "Vero": "https://vero.co/{}",
    "Ravelry": "https://www.ravelry.com/people/{}",
    "Twitch": "https://www.twitch.tv/{}",
    "ShareChat": "https://www.sharechat.com/{}/",
    "Threads": "https://www.threads.net/@{}",
    "Viber": "https://www.viber.com/en/users/{}",
    "Zalo": "https://zalo.me/{}",
    "Line": "https://line.me/{}",
    "VK (Vkontakte)": "https://vk.com/{}",
    "Microsoft Teams": "https://teams.microsoft.com/l/team/{}",
    "Riot Games": "https://www.riotgames.com/en/{}",
}


def check_username_on_site(site, url, username):
    try:
        formatted_url = url.format(username)
        response = requests.get(formatted_url)
        
        if response.status_code == 200:
            time = datetime.now().strftime("%H:%M:%S")
            return f"{fade("[")}{time}{fade("]")} {site}: {Colorate.Color(Colors.green, "TRUE")} > {formatted_url}"
    except requests.RequestException as e:
        return None
    
    return None

def check_username(username):
    results = []

    with ThreadPoolExecutor(max_workers=50) as executor:
        futures = [
            executor.submit(check_username_on_site, site, url, username)
            for site, url in websites.items()
        ]

        for future in futures:
            result = future.result()
            if result:
                results.append(result)
    
    return results

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
    username_to_check = input(f"\n{fade("[")}{time}{fade("]")} > Enter Username: ")
    results = check_username(username_to_check)

    if results:
        for result in results:
            print(result)
    else:
        time = datetime.now().strftime("%H:%M:%S")
        print(f"\n{fade("[")}{time}{fade("]")} Username not found.")

    time = datetime.now().strftime("%H:%M:%S")
    input(f"{fade("[")}{time}{fade("]")} Press any key to go back.")
    os.system("python master.py")
