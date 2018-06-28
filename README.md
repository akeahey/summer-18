# summer-18

## links_to_polymer_names

Extracts polymer names from the website: http://www.polymerdatabase.com/home.html

### modules
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - pulls data out of HTML files

### improvements 
In the second set of links that lead to polymer links, some of the group names of polymers (ex: arylates, esters) link to the same page (as arylates and esters both links to /polyesters.html). This creates redundancies in the list of polymers- some are listed more than once in the final list of polymer names.
Presumably this convergence because there can be two different names for the same thing.
Alternatively, this convergence could be due to a mistake on behalf of the website creator.
Either way, the code could be improved by removing these redundancies.
