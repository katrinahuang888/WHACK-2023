import csv, wikipediaapi, requests, json
#from googletrans import Translator

#user input + list translation
x = input("Enter region to travel to: ")
regionsList = x.split(", ")

# reading food data
with open('food_data.csv', mode = 'r') as inFile:
    csv_reader = csv.DictReader(inFile)
    result = ""
    countries = ""
    content = [row for row in csv_reader]
    for row in content:
        for r in regionsList:
            if row['Region'] == r:
                countries += "The top two most popular foods from " + r + " are " + row['Food1'] + " and " + row['Food2'] + ". \n\n"
                result = "Here is a short description of " + row['Food1'] + ": " + "\n" + row ['Description1'] + "\n\n" + result  
                result = "Here is a short description of " + row['Food2']+ ": " + "\n" + row['Description2'] + "\n\n" + result
    print(countries + result)

URL = "https://en.wikipedia.org/w/api.php"
query = regionsList[0]
PARAMS = {"action": "opensearch", "search": "List of " + query + " cuisines", "format": "json"}
response = requests.get(url = URL, params = PARAMS)
print(response)
if response.status_code == 200:
    data = json.loads(response.content)
    print("Here is a starter point for you if you are interested in looking further into this topic!")
    print(data)


# transactions data
with open('transactions_data.csv', mode = 'r') as inFile:
    csv_reader2 = csv.DictReader(inFile)
    result = ""
    countries = ""
    content2 = [row for row in csv_reader2]
    for row in content2:
        for r in regionsList:
            if row['Region'] == r: 
                result += "\nThe most commonly used form of currencies: " + row['Currency'] + "\n"
                result += "The exchange rate for USD:Foreign is " + row['Exchange Rate (USD:Foreign)'] + "\n"
                result += "The UN level terrorist warning is: " + row['Terrorist Level Warning (UN)'] + "\n"
    print(result)
    
#music portion
with open('music_data.csv', mode = 'r') as inFile:
    csv_reader3 = csv.DictReader(inFile)
    result = ""
    content3 = [row for row in csv_reader3]
    for row in content3:
        for r in regionsList:
            if row['Region'] == r:
                result += "Here is a link to a popular spotify playlist with music from that area to explore: " + row['Playlist'] + "\n"
    print(result)

#translator portion
# translator = Translator(service_urls=['translate.googleapis.com'])
# y = input("Please enter an English phrase to translate into your traveled region: ")
# for r in regionsList:
#     if r == "North Africa and Middle East":
#         out = "Here is your phrase translated into Arabic, the most spoken language in that region. " + translator.translate(y, dest = "ar")
#     elif r == "South Africa":
#         out = "Here is your phrase translated into Zulu, the most spoken language in that region. " + translator.translate(y, dest = "zu")
#     elif r == "Central and Southeast Asia":
#         out = "Here is your phrase translated into Malay, the most spoken language in that region. " + translator.translate(y, dest = "ms")
#     elif r == "Europe":
#         out = "Here is your phrase translated into Russian, the most spoken language in that region. " + translator.translate(y, dest = "ru")
#     elif r == "Central America":
#         out = "Here is your phrase translated into Spanish, the most spoken language in that region. " + translator.translate(y, dest = "es")
#     elif r == "South America":
#         out = "Here is your phrase translated into Spanish, the most spoken language in that region. " + translator.translate(y, dest = "es")
#     elif r == "East Asia":
#         out = "Here is your phrase translated into Chinese (traditional), the most spoken language in that region. " +translator.translate(y, dest = "zh-tw")
#     elif r == "South Asia":
#         out = "Here is your phrase translated into Hindi, the most spoken language in that region. " + translator.translate(y, dest = "hi")
#     else:
#         out = "Here is your phrase translated into English, the most spoken language in that region. " + translator.translate(y, dest = "en")
# print(y.origin, ' -> ', y.text)


""" APIs for later


PARAMS2 = {
"action": "opensearch",
"search": "List of " + regionsList[1] + " cuisines",
"format": "json"
}
print(PARAMS2)
response2 = requests.get(url=URL, params = PARAMS2)
print(response2)
if response2.status_code == 200:
    data2 = response2.json()
    print(data2)

content = []
responses = []
listLength = len(regionsList)
i = 0
while i < listLength:
    PARAMS1 = {"action": "opensearch", 
    "search": "List of " + regionsList[i] + " cuisines",
    "format": "json"}
    responses.append(requests.get(url=URL, params = PARAMS1))
    if responses[i].status_code == 200:
        content.append(json.loads(responses[i].content))
    #if response1.status_code == 200:
    i += 1
print(content)

for region in regionsList:
    query = region
    params = {"action": "opensearch", "format": "json",
    "search": "List of " + query + " cuisines"}
    data = requests.get(URL, params = params)
    print(data.json()) """

# food data into wikipedias
# keyWords = {"North Africa and Middle East": "Maghrebi_cuisine", "South Africa": "South_African_cuisine", 
# "Central and Southeast Asia": "Central_Asian_cuisine", "Europe":"List_of_European_cuisines", 
# "Central America":"Latin_American_cuisine", "South America":"South_American_cuisine",
# "East Asia": "List_of_Asian_cuisines#East_Asian_cuisine", "South Asia": "South_Asian_cuisine",
# "North America":"North_American_cuisine"}