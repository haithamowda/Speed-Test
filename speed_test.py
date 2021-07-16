import speedtest
red="\033[1;31m"
green="\033[1;32m"
blue="\033[1;34m"
yellow="\033[1;33m"
black="\033[1;30m"
purple="\033[1;35m"
even="\033[1;36m"
white="\033[1;37m"
print(f'''


{red}███████╗██████╗ ███████╗███████╗██████╗     {yellow}████████╗███████╗███████╗████████╗
██╔════╝██╔══██╗██╔════{blue}╝██╔════╝██╔══██╗    ╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝
{green}███████╗██████╔╝█████╗  █████╗  ██║  ██║       ██║   █████╗  ███████╗   ██║   
╚════██║██╔═══╝ ██╔══╝  {red}██╔══╝  ██║  ██║       ██║   ██╔══╝  ╚════██║   ██║   
███████║██║     {yellow}███████╗███████╗██████╔╝       ██║   ███████╗███████║   ██║   
╚══════╝╚═╝     {even}╚══════╝╚══════╝╚═════╝        ╚═╝   ╚══════╝╚══════╝   ╚═╝   
                                                                              
    {red}Youtube {green}>>{yellow} https://www.youtube.com/c/HaithamLinux
    {even}Twitter {green}>>{yellow} Haotham_Owda
   {blue} Telegram {green}>>{yellow} https://t.me/techcyber
    {black}Github {green}>>{yellow} https://github.com/haithamowda
    {red}Instagram {green}>>{yellow} haithamowda
''')

test = speedtest.Speedtest()

print("Loading server list...")
test.get_servers() ## -> get list of servers
print("Choosing best server...")
best = test.get_best_server() ## -> choose best server
print(f"Found: {best['host']} located in {best['country']}")

print("Performing download test...")
download_result = test.download()
print("Performing upload test...")
upload_result = test.upload()
ping_result = test.results.ping

print(f"Download Speed: {download_result / 1024 / 1024:.2f} Mbit/s")
print(f"Upload Speed: {upload_result / 1024 / 1024:.2f} Mbit/s")
print(f"Ping: {ping_result:.2f} ms")
