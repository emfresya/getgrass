#открываем
with open('proxy_list.txt', 'r') as file:
    proxies = file.readlines()

#добавляем "socks5://" перед IP-адресом
socks5_proxies = ['socks5://' + proxy.strip() for proxy in proxies]

# открываем
with open('proxy_list.txt', 'w') as file:
    #перезаписываем
    file.write('\n'.join(socks5_proxies))
