import requests
from pystyle import Colors, Colorate
import os
from datetime import datetime

def fade(text: str) -> str:
    return Colorate.Horizontal(Colors.purple_to_blue, text, 1)

def interesting(url):
    interesting_paths = [
        "admin", "admin/", "admin/index.php", "admin/login.php", "admin/config.php",
        "backup", "backup/", "backup/db.sql", "backup/config.tar.gz", "backup/backup.sql",
        "private", "private/", "private/.env", "private/config.php", "private/secret.txt",
        "uploads", "uploads/", "uploads/file.txt", "uploads/image.jpg", "uploads/backup.zip",
        "api", "api/", "api/v1/", "api/v1/users", "api/v1/status",
        "logs", "logs/", "logs/error.log", "logs/access.log", "logs/debug.log",
        "cache", "cache/", "cache/temp/", "cache/session/", "cache/data/",
        "server-status", "server-status", "server-status/", "server-status/index.html",
        "dashboard", "dashboard/", "dashboard/index.html", "dashboard/admin.php", "dashboard/settings.php"
    ]

    try:
        found = 0
        if not url.endswith("/"):
            url += "/"
        
        for path in interesting_paths:
            test_url = url + path
            response = requests.get(test_url, timeout=10)
            if response.status_code == 200:
                found += 1
                time = datetime.now().strftime("%H:%M:%S")
                print(f"{fade("[")}{time}{fade("]")} {fade("[")}Vulnerability{fade("]")} Interesting Path Found: {Colorate.Color(Colors.green, f"{path}")}")
    except:
        pass
    if found == 0:
        time = datetime.now().strftime("%H:%M:%S")
        print(f"{fade("[")}{time}{fade("]")} {fade("[")}Vulnerability{fade("]")} Interesting Paths? {Colorate.Color(Colors.red, "False")}")

def sensitive(url):
    sensitive_files = [
        "etc/passwd", "etc/password", "etc/ip", "etc/passwords", "etc/ips", "etc/shadow", "etc/group",
        "etc/hosts", "etc/hostname", "etc/network/interfaces",
        "etc/sysconfig/network", "etc/sysconfig/network-scripts/ifcfg-*", "etc/fstab",
        "etc/resolv.conf", "etc/issue", "etc/motd",
        "etc/apt/sources.list", "etc/yum.conf", "etc/sudoers",
        "passwd", "password", "ip", "passwords", "ips", "shadow", "group",
        "hosts", "hostname", "network/interfaces",
        "sysconfig/network", "sysconfig/network-scripts/ifcfg-*", "fstab",
        "resolv.conf", "issue", "motd",
        "apt/sources.list", "yum.conf", "sudoers",
        "var/log/auth.log", "var/log/syslog", "var/log/messages",
        "var/log/dmesg", "var/log/secure", "var/log/maillog",
        "var/log/httpd/access_log", "var/log/httpd/error_log", "var/log/apache2/access.log",
        "var/log/apache2/error.log", "var/log/nginx/access.log", "var/log/nginx/error.log",
        "root/.bash_history", "root/.ssh/authorized_keys", "root/.ssh/id_rsa",
        "root/.ssh/id_rsa.pub", "root/.ssh/known_hosts", "home/user/.bash_history",
        "home/user/.ssh/authorized_keys", "home/user/.ssh/id_rsa", "home/user/.ssh/id_rsa.pub",
        "home/user/.ssh/known_hosts", "www/html/config.php", "www/html/wp-config.php",
        "www/html/.htaccess", "www/html/.env", "opt/lampp/etc/my.cnf",
        "opt/lampp/htdocs/index.php", "opt/lampp/phpmyadmin/config.inc.php", "boot/grub/grub.cfg",
        "boot/grub/menu.lst", "proc/self/environ", "proc/version",
        "proc/cmdline", "proc/mounts", "proc/net/arp",
        "proc/net/tcp", "proc/net/udp", "proc/net/fib_trie"
    ]

    try:
        found = 0
        if not url.endswith("/"):
            url += "/"

        for file in sensitive_files:
            test_url = url + file
            response = requests.get(test_url, timeout=10)
            if response.status_code == 200:
                if any(file in response.text for file in sensitive_files):
                    found += 1
                    time = datetime.now().strftime("%H:%M:%S")
                    print(f"{fade("[")}{time}{fade("]")} {fade("[")}Vulnerability{fade("]")} Sensitive File Found: {Colorate.Color(Colors.green, f"{file}")}")
    except:
        pass
    if found == 0:
        time = datetime.now().strftime("%H:%M:%S")
        print(f"{fade("[")}{time}{fade("]")} {fade("[")}Vulnerability{fade("]")} Sensitive Files? {Colorate.Color(Colors.red, "False")}")

def xss(url):
    xss_provocations = [
        "<script>alert('XssFound')</script>", 
        "<img src=x onerror=alert('XssFound')>", 
        "<body onload=alert('XssFound')>", 
        "<svg/onload=alert('XssFound')>", 
        "javascript:alert('XssFound')", 
        "<iframe src='javascript:alert(\"XssFound\")'></iframe>", 
        "<input type=\"text\" onfocus=\"alert('XssFound')\">", 
        "<a href=\"javascript:alert('XssFound')\">Click me</a>"
    ]

    xss_indicators = ["<script>", "alert(", "onerror=", "onload=", "javascript:"]

    try:
        found = 0 
        for xss_provocation in xss_provocations:
            xss = url + xss_provocation
            response = requests.get(xss, timeout=10)
            if any(xss_indicator in response.text for xss_indicator in xss_indicators):
                found += 1
                time = datetime.now().strftime("%H:%M:%S")
                print(f"{fade("[")}{time}{fade("]")} {fade("[")}Vulnerability{fade("]")} Xss Found at: {Colorate.Color(Colors.green, f"{xss}")}")
                break
    except:
        pass
    if found == 0:
        time = datetime.now().strftime("%H:%M:%S")
        print(f"{fade("[")}{time}{fade("]")} {fade("[")}Vulnerability{fade("]")} Xss vulnerability? {Colorate.Color(Colors.red, "False")}")

def sql(url):
    sql_indicators = [
        "SQL syntax", "SQL error", "MySQL", "syntax error", "SQLite", "PostgreSQL", 
        "Truncated incorrect", "Division by zero", "You have an error in your SQL syntax"
    ]

    sql_provocations  = [
        "'", "' OR '1'='1'", "' UNION SELECT NULL--", "' OR 1=1 --", "admin' --"
    ]

    try:
        found = 0
        for sql_provocation in sql_provocations:
            test_url = url + sql_provocation
            response = requests.get(test_url, timeout=10)
            if any(sql_indicator in response.text for sql_indicator in sql_indicators):
                found += 1
                time = datetime.now().strftime("%H:%M:%S")
                print(f"{fade("[")}{time}{fade("]")} {fade("[")}Vulnerability{fade("]")} Sql Injection Found")
                break
    except:
        pass
    if found == 0:
        time = datetime.now().strftime("%H:%M:%S")
        print(f"{fade("[")}{time}{fade("]")} {fade("[")}Vulnerability{fade("]")} Sql vulnerability? {Colorate.Color(Colors.red, "False")}")

if __name__ == "__main__":
    banner = r'''
    .-""-.
   / .--. \
  / /    \ \
  | |    | |
  | |.-""-.|
 ///`.::::.`\
||| ::/  \:: ;
||; ::\__/:: ;
 \\\ '::::' /
  `=':-..-'`
'''

    print(Colorate.Horizontal(Colors.purple_to_blue, banner, 1))
    time = datetime.now().strftime("%H:%M:%S")
    url = input(f"\n{fade("[")}{time}{fade("]")} > Enter URL: ").strip()

    time = datetime.now().strftime("%H:%M:%S")
    print(f"{fade("[")}{time}{fade("]")} Scanning for vulnerabilities @ {url}")
    interesting(url)
    sensitive(url)
    xss(url)
    sql(url)

    time = datetime.now().strftime("%H:%M:%S")
    input(f"{fade("[")}{time}{fade("]")} Press any key to go back.")
    os.system("python master.py")
