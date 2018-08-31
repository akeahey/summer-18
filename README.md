# summer-18

## Website Scraping
* links_to_polymer_names.py

    + Extracts polymer names from the website: http://www.polymerdatabase.com/home.html

    + INPUT: input/scrape_page.html, and input/scrape_page_2.html

    + ### modules
        [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - pulls data out of HTML files
        
    + OUTPUT: polymer_names.txt

## Rule-Based Synonyms
* 1_database_synonym_extraction.ipynb

    + Identifies polymer names and their acronyms in text 

    + uses abbreviations.py
    
    + produces amber_polymer_candidates.txt
    
* 2_groundtruth_plurals.ipynb

    + Removes plurals from ground_truth_polymers_list.txt
    
    + produces ground_truth_polymers_list_plurals.txt
    
* 3_evaluation_candidates.ipynb

    + Compares polymer_candidates.txt to ground_truth_polymers_list.txt

* 4_synonyms_similarity_comparison.ipynb

    + Uses most_similar gensim model to find words most similar to polymers 
    
    + Assesses how many of these most_similar vectors are actual acronyms 

* 5_augmented_keywords_evaluation.ipynb

    + Completes evaluation with greater number of keywords
    
    + Creates /output/FT_candidates_500.txt and output/second_FT_candidates_500.txt
    
    + From input/scraped_polymer_names.txt and data/expert_curated_polymers.csv respectively
    
* 6_candidates_combination.ipynb
    
    + Combines outputs from the two sources in augmented_keywords_evaluation
    
* 7_combined_evaluation.ipynb

    + Compares input list to ground_truth_polymers_list.txt

