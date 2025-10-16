import nltk
import requests
from nltk.corpus import stopwords
import re
from ddgs import DDGS
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from bs4 import BeautifulSoup
from collections import Counter
nltk.download('stopwords') 


###INITILIZE EVERYTHING

intext = input("Enter your text to check for plagiarism: ")

checktext = "Placeholder."


###DEFINE THE FUCTIONS FOR CLEANING AND CHCEKING:

def preprocess(text):
    #Make small, remove weird charas, whitepace, and stop words to compare easily:
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    stop_words =  set(stopwords.words('english'))
    text = " ".join(word for word in text.split() if word not in stop_words)
    return text



#Get the checktexts: (Extract keywords, ddgs, scrape):

def extract_keywords(text, top_n=10):
    words = text.split()
    stop_words = set(stopwords.words('english'))
    filtered = [w for w in words if w not in stop_words]
    
    freq = Counter(filtered)
    return [word for word, _ in freq.most_common(top_n)]

def search_duckduckgo(query, nlinks=5):
    links = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=nlinks):
            links.append(r["href"])
    return links
    

def scrape_text(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'} 
        r = requests.get(url, headers=headers, timeout=5) 
        soup = BeautifulSoup(r.text, 'html.parser') 
        paragraphs = soup.find_all('p')   
        text = ' '.join(p.get_text() for p in paragraphs)
        return text
    except Exception as e:
        print(f"Failed to scrape {url}: {e}")
        return ""


#Check intext against a checktext:  


def check_plagiarism(textA, textB):
    #Make the vectors:
    tfidfvec = TfidfVectorizer()
    vectors = tfidfvec.fit_transform([textA, textB])
    #Check for similarity btw the 2 vectors:
    similarity_matrix = cosine_similarity(vectors) 
    similarity_score = similarity_matrix[0][1]

    return similarity_score * 100


###CALL ALL FUNCTIONS IN THE RIGHT ORDER:


Cleanintext = preprocess(intext)
print("Cleaned intext:" + Cleanintext)


# Extract keywords from the cleaned intext:
keywords = []
keywords = extract_keywords(Cleanintext)
print(keywords)

#Find all the urls to scape: find a url per keyword:
urls = []
for kw in keywords:
    urls.extend(search_duckduckgo(kw))


#Scrape each url, compare:
# List to store results of similarity checks:
results = []

# Loop through the scraped URLs
for url in urls:    
    # Scrape:
    checktext = scrape_text(url)
    
    # If the scraping was successful; clean and compare:
    if checktext:
        Cleanchecktest = preprocess(checktext)
        similarity = check_plagiarism(Cleanintext, Cleanchecktest)
        
        #Add the result to the results list (URL and similarity)
        results.append((url, similarity))

        print(url)
        print("=====> Similarity: ")
        print(similarity)
        print(f"{similarity:.2f}%")


# Sort by similarity:
results.sort(key=lambda x: x[1], reverse=True)

#Print:
for url, score in results[:5]:
    print(f"{url} -> Similarity: {score:.2f}%")

