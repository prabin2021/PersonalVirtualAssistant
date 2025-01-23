# import re
# import pywhatkit as kit
# import requests
# from bs4 import BeautifulSoup

# def search_google(query):
#         start_keywords = ["search for","search for the topic","search for the name","search for the title","search" ,"look for", "find that", "find out"," information about","idea about" "search about", "show me", "watch", "search that", "tell me","search",
#                         "give me the idea about","give me idea about","google that","google search that","my query is","my question is","for","about","find"]
#         words = query.lower().split()
#         search_query = ""
#         for i, word in enumerate(words):
#                 if word in start_keywords:
#                 search_query1 = " ".join(words[i + 1:])
#         search_query = re.sub(r"\s?(in|at|on|with|from)\s?(google|internet)", "", search_query1)

#         print(search_query)

#         if not search_query:
#                 print("Please specify properly what you want to search for.")
#                 return

#         # kit.search(search_query)
#         print("Ok sir, here is your search result.")
        
#         google_url = f"https://www.google.com/search?q={search_query}"
#         response = requests.get(google_url)
#         if response.status_code != 200:
#                 print("I am unable to fetch the search results right now sir.")
#                 return

#         soup = BeautifulSoup(response.text, 'html.parser')
        
#         print("I have collected 1 results sir.")
#         allData = soup.find_all("div",{"class":"g"})
#         print(allData)
#         g=0
#         Data = [ ]
#         l={}
#         for i in range(0,len(allData)):
#                         link = allData[i].find('a').get('href')

#                         if(link is not None):
#                                 if(link.find('https') != -1 and link.find('http') == 0 and link.find('aclk') == -1):
#                                 g=g+1
#                                 l["link"]=link
#                                 try:
#                                         l["title"]=allData[i].find('h3',{"class":"DKV0Md"}).text
#                                 except:
#                                         l["title"]=None

#                                 try:
#                                         l["description"]=allData[i].find("div",{"class":"VwiC3b"}).text
#                                 except:
#                                         l["description"]=None

#                                 l["position"]=g

#                                 Data.append(l)

#                                 l={}

#                                 else:
#                                 continue

#                         else:
#                                 continue

# import requests
# from bs4 import BeautifulSoup

# # Set headers to mimic a browser request
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
# }

# # Perform a Google search
# query = "Why Python is so popular"
# url = f"https://www.google.com/search?q={query}"
# response = requests.get(url, headers=headers)

# # Parse the content with BeautifulSoup
# soup = BeautifulSoup(response.text, 'html.parser')
# print(response.text)
# # Scrape the search results
# results = []
# print("html parse garyo")
# for result in soup.find_all("div"):
#     h3 = result.find("h3")
#     if h3:
#         print(h3.text)

# for result in soup.find_all("div"):
#     if "h3" in result.text:
#         print(result.prettify())
# for result in soup.find_all("div", class_="rPeykc"):
#     try:
#         title_tag = result.find("h3")
#         link_tag = result.find("a")
#         snippet_tag = result.find("span")

#         if title_tag and link_tag and snippet_tag:
#             title = title_tag.text
#             link = link_tag["href"]
#             snippet = snippet_tag.text
#             results.append({"title": title, "link": link, "snippet": snippet})
#     except AttributeError:
#         continue


# # Print the results
# for idx, res in enumerate(results, start=1):
#     print(f"Result {idx}:")
#     print(f"Title: {res['title']}")
#     print(f"Link: {res['link']}")
#     print(f"Snippet: {res['snippet']}\n")

