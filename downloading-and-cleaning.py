import numpy as np
import pandas as pd
import src.clean_utils as cu

# Import de dataset
Abb_NY = pd.read_csv("data/AB_NYC_2019.csv",encoding = "ISO-8859-1")

# Print it in order to be able to compare cleaning results
print(Abb_NY)

# Clening funtions

drop_cols = ["id","name","host_id","host_name","latitude", "longitude","reviews_per_month","calculated_host_listings_count","availability_365"]
Abb_NY_clean = Abb_NY.drop(drop_cols, axis =1)

Abb_NY_clean["year"] = Abb_NY_clean.last_review.dropna().apply(cu.extract_year)

Abb_NY_clean["year"].value_counts(dropna=False)

drop_cols = ["last_review"]
Abb_NY_clean = Abb_NY_clean.drop(drop_cols, axis =1)

Abb_NY_clean["year"] = Abb_NY_clean[Abb_NY_clean["year"]>2015]["year"]

Abb_NY_clean = Abb_NY_clean[Abb_NY_clean["year"].notnull()]

# Final result

print(Abb_NY_clean)