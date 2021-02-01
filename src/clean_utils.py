# Cleaning year function, on the Dataset:
def extract_year(last_review_string):
    return int(last_review_string[0:4])

# Cleaning function, on the web scraping info:
def cleaning(string):
    hoods = ["manhattan","brooklyn","bronx", "queens", "staten island"]
    for w in hoods:
        if w in str(string).lower(): 
            return w
    else:
         return "other"