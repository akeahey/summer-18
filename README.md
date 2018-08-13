# summer-18

## Website Scraping
* links_to_polymer_names.py

    + Extracts polymer names from the website: http://www.polymerdatabase.com/home.html

    + files available as scrape_page.html, and scrape_page_2.html

    + ### modules
        [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - pulls data out of HTML files

## Rule-Based Synonyms
* test_synonym_extraction.ipynb

    + Identifies polymer names and their acronyms in text 

    + uses abbreviations.py
    
    + produces amber_polymer_candidates.txt
    
* evaluation_candidates.ipynb

    + Compares polymer_candidates.txt to ground_truth_polymers_list.txt
    
* groundtruth_plurals.ipynb

    + Removes plurals from ground_truth_polymers_list.txt
    
    + produces ground_truth_polymers_list_plurals.txt

* synonyms_similarity_comparison.ipynb

    + Uses most_similar gensim model to find words most similar to polymers 
    
    + Assesses how many of these most_similar vectors are actual acronyms 

