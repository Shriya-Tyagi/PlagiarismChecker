Plagiarism Checker with Web Scraping & NLP

This Python tool checks a block of text for potential plagiarism by:

- Cleaning and preprocessing the input,
- Extracting key terms using word frequency,
- Searching the web via DuckDuckGo (via ddgs),
- Scraping page content from search results,
- Comparing similarity with TF-IDF + cosine similarity.

Great for basic plagiarism checks using live web data.

------------------------------------------------------------

#+ Features

- Keyword extraction with nltk
- Web search using DuckDuckGo (via ddgs)
- Smart text preprocessing
- Web scraping with requests and BeautifulSoup
- Text similarity using sklearn's TF-IDF + cosine similarity (might add BERT later for paraphrased text detection)

------------------------------------------------------------

#+ Setup & Installation

1. Clone the repository:
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name

2. Create  a virtual environment and install dependencies:
   source .venv/bin/activate
   pip install -r requirements.txt

------------------------------------------------------------

#+ Usage

You'll be prompted to enter a block of text to check for plagiarism.

The program will:
1. Clean your input text.
2. Extract top keywords.
3. Search the web and scrape content.
4. Compare your text with scraped results.
5. Show URLs and similarity percentages.

------------------------------------------------------------

#+ Dependencies

Main Python packages used:

- nltk
- scikit-learn
- ddgs
- beautifulsoup4
- requests
- numpy
See requirements.txt.

------------------------------------------------------------

#+ Disclaimer

This is a simple heuristic-based tool. It:

- Does not detect paraphrasing or deep plagiarism.
- Is limited by what DuckDuckGo returns and what can be scraped.
- May be blocked by some websites.

------------------------------------------------------------

#+ License

This project is not open source.  
All rights reserved. You may not use, copy, modify, or distribute this code without explicit written permission from the author.

------------------------------------------------------------

#+ Author

Shriya Tyagi
GitHub: https://github.com/Shriya-Tyagi.
