from pystyle import Colors, Colorate, Center
import os
import platform

def fade(text: str) -> str:
    return Colorate.Horizontal(Colors.purple_to_blue, text, 1)

def cls():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

username = os.getlogin()

banner = """
                               ███▄ ▄███▓ ▄▄▄        ██████ ▄▄▄█████▓▓█████  ██▀███  
                               ▓██▒▀█▀ ██▒▒████▄    ▒██    ▒ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒
                               ▓██    ▓██░▒██  ▀█▄  ░ ▓██▄   ▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒
                               ▒██    ▒██ ░██▄▄▄▄██   ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄  
                               ▒██▒   ░██▒ ▓█   ▓██▒▒██████▒▒  ▒██▒ ░ ░▒████▒░██▓ ▒██▒
                               ░ ▒░   ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░
                               ░  ░      ░  ▒   ▒▒ ░░ ░▒  ░ ░    ░     ░ ░  ░  ░▒ ░ ▒░
                               ░      ░     ░   ▒   ░  ░  ░    ░         ░     ░░   ░ 
                                   ░         ░  ░      ░              ░  ░   ░     
"""
menu1 = f"""
{fade("          ┌─────────────────┐                        ┌───────┐                           ┌───────────┐            ")}
{fade("┌─────────┤")}     Network    {fade(" ├─────────┬──────────────┤")} OSINT {fade("├──────────────┬────────────┤")} Utilities {fade("├────────────┐")}
{fade("│         └─────────────────┘         │              └───────┘              │            └───────────┘")}
{fade("├─ [")}01{fade("]")} Website Vulnerability Scanner {fade("├─")} {fade("[")}05{fade("]")} Username Lookup               {fade("├─")}
{fade("├─ [")}02{fade("]")} Website Crawler               {fade("├─")} {fade("[")}06{fade("]")} Phone Number Lookup           {fade("├─")}
{fade("├─ [")}03{fade("]")} IP Info                       {fade("├─")}
{fade("├─ [")}04{fade("]")} IP Port Scanner               {fade("├─")}
{fade("└─────────────────────────────────────┴─────────────────────────────────────┴─────────────────────────────────────┘")}
"""

def main():
    cls()
    print(Colorate.Horizontal(Colors.purple_to_blue, banner, 1))
    print(menu1)
    print(f"{fade('┌──(')}{username}{fade('@')}master{fade(')')}")
    cmd = input(f"{fade('└─')}$ ")

    if cmd == "01":
        os.system("python tools/website-vuln-scanner.py")
    elif cmd == "02":
        os.system("python tools/web-spider.py")
    elif cmd == "03":
        os.system("python tools/ip-info.py")
    elif cmd == "04":
        os.system("python tools/ip-port-scanner.py")
    elif cmd == "05":
        os.system("python tools/username-lookup.py")
    elif cmd == "06":
        os.system("python tools/phone-number-lookup.py")

if __name__ == "__main__":
    main()
