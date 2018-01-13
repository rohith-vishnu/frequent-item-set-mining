from collections import OrderedDict

with open("urls.txt","r") as f:
    content = f.readlines()
websites=[x.split() for x in content]
final_urls=[]
for website in websites:
    url=website[0].split('/')
    final_urls.append(url[2])
    print(url)
final_urls_1=list(set(final_urls))
print(final_urls_1)

