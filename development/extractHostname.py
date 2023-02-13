from tldextract import extract

tsd, td, tsu = extract("https://habitica.com/") # prints abc, hostname, com
url = td # will prints as hostname.com    
print(url)