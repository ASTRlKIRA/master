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
page = 1

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
{fade("                                                                                                         ")}Next {fade("[")}N{fade("]")}{fade("─┐")}
{fade("          ┌─────────────────┐                        ┌───────┐                           ┌───────────┐            ")}{fade("│")}
{fade("┌──[")}1{fade("]")}{fade("────┤")}     Network    {fade(" ├─────────┬──────────────┤")} OSINT {fade("├──────────────┬────────────┤")} Utilities {fade("├────────────┴─")}
{fade("│         └─────────────────┘         │              └───────┘              │            └───────────┘")}
{fade("├─ [")}01{fade("]")} Website Vulnerability Scanner {fade("├─")} {fade("[")}05{fade("]")} Username Lookup               {fade("├─")} {fade("[")}00{fade("]")} ...
{fade("├─ [")}02{fade("]")} Website Crawler               {fade("├─")} {fade("[")}06{fade("]")} Phone Number Lookup           {fade("├─")} {fade("[")}00{fade("]")} ...
{fade("├─ [")}03{fade("]")} IP Info                       {fade("├─")} {fade("[")}07{fade("]")} Email Lookup        {fade("[")}PC ONLY{fade("]")} {fade("├─")} {fade("[")}00{fade("]")} ...
{fade("└─ [")}04{fade("]")} IP Port Scanner               {fade("└─")} {fade("[")}08{fade("]")} IP Lookup                     {fade("└─")} {fade("[")}00{fade("]")} ...
"""

menu2 = f"""
{fade("                                                                                              ")}Back {fade("[")}B{fade("]")} {fade("|")} Next {fade("[")}N{fade("]")}{fade("─┐")}
{fade("          ┌─────────────────┐                        ┌───────┐                           ┌───────────┐            ")}{fade("│")}
{fade("┌──[")}2{fade("]")}{fade("────┤")}     Network    {fade(" ├─────────┬──────────────┤")} OSINT {fade("├──────────────┬────────────┤")} Utilities {fade("├────────────┴─")}
{fade("│         └─────────────────┘         │              └───────┘              │            └───────────┘")}
{fade("├─ [")}01{fade("]")} Website Vulnerability Scanner {fade("├─")} {fade("[")}05{fade("]")} Username Lookup               {fade("├─")} {fade("[")}00{fade("]")} ...
{fade("├─ [")}02{fade("]")} Website Crawler               {fade("├─")} {fade("[")}06{fade("]")} Phone Number Lookup           {fade("├─")} {fade("[")}00{fade("]")} ...
{fade("├─ [")}03{fade("]")} IP Info                       {fade("├─")} {fade("[")}07{fade("]")} Email Lookup        {fade("[")}PC ONLY{fade("]")} {fade("├─")} {fade("[")}00{fade("]")} ...
{fade("└─ [")}04{fade("]")} IP Port Scanner               {fade("└─")} {fade("[")}08{fade("]")} IP Lookup                     {fade("└─")} {fade("[")}00{fade("]")} ...
"""

def render_menu():
    global page
    cls()
    print(Colorate.Horizontal(Colors.purple_to_blue, banner, 1))
    if page == 1:
        print(menu1)
    elif page == 2:
        print(menu2)

def main():
    global page
    while True:
        render_menu()
        print(f"{fade('┌──(')}{username}{fade('@')}master{fade(')')}")
        cmd = input(f"{fade('└─')}$ ").strip().upper()

        if cmd == "N":
            if page < 2:
                page += 1
        elif cmd == "B":
            if page > 1:
                page -= 1
        elif cmd == "01":
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
        elif cmd == "07":
            os.system("python tools/email-lookup.py")
        elif cmd == "08":
            os.system("python tools/ip-lookup.py")
        elif cmd == "EXIT":
            break
        else:
            print(f"{fade('Invalid command! Try again.')}")

if __name__ == "__main__":
    main()
