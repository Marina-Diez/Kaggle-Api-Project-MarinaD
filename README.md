# KAGGLE AND APIS/SCRAPING PROJECT - NY AIRBnB

![abnb](images/nyc-600-x-250.jpg)

# Finding Kaggle Dataset and enriching with scraping.
The aim of this project is to find and enrich a dataset that we must select from different sources. I have decided to use the following kaggle dataset ["New York City Airbnb Open Data"](https://www.kaggle.com/dgomonov/new-york-city-airbnb-open-data) because is a information I´m familiar with, it is a clean dataset with high level of usability and  I can find articles and webs in order to enrich it.

To achive all this I will follow nexts steps:
>1. **Expore Kaggle Database**. And find the one that I will foccus on. I decided to use New York City Airbnb Open Data.
>2. **Find usefull information to enrich my data conclusions** I decided to enrich my information with NY monuments data.
>2. **Think on a wire conductor**  What do I whant to support whith our info ?
>3. **Clean the dataset and the scraping info**. which are the usefull datas to find and support my hypothesis?
>4. **Analyze the data**. 
>5. **Make it visual**. For me and for others to de understable

### Exproring datasets and finding enriching information.
I started with a clean dataset with the following shape (48895, 16), but with non usefull columns that I decided to drop and I also made some clening funtion in order to get my clean dataset with a shape of (37171,7).

### Wire conductor 
AirBnB in NY by neighbourhoods, are there relation between the number of bookings per neighbourhoods and the amount of monuments in those zones? or it also dependS on prices? I will focuss my attention in those years over 2015, in order to skip the years involved in the Great recesion.

### Cleaning and enriching
I have follow 3 steps in order to clean and found the important imformation:
>1. Look for the years over 2015
>2. Import and clean scraping information and give it a shape similar to our dataframe table.
>3. Cross both information in order to relate it.

### Visualization and conclusions
What we want to see in or visual plots is which NY neighbourhood has more visits, and if it is related to the number of monuments per zone or it is related to price.
In the following plot we can se which are the neighbourhood with more AirBnB visits.
![RANKING](https://github.com/Marina-Diez/Kaggle-Api-Project-MarinaD/blob/master/output/Ranking_plot.jpg)

In the following plot we can see that Manhattan is the neighbourhood with more monuments (and we also know that there is also the financial district of NY), so it makes sense that most of the people would like to find a house to rent here. But what about Brooklyn? It has lot of AirBnB visit but not that much monuments.
![MONUMENTS](https://github.com/Marina-Diez/Kaggle-Api-Project-MarinaD/blob/master/output/Monuments_plot.jpg)

And as we can see in the following plot, the median of price in Broklyn is much lower than in Manhattan and it is a close neighbourhood, so we can say that people also preffer to be on a neighbourhood that is more relax and near to where mostly every monuments and offices are.
![MEDIANPRICE](https://github.com/Marina-Diez/Kaggle-Api-Project-MarinaD/blob/master/output/median_plot.jpg)

**If you want further information of muy project, please visit it!**

### Aditional information

I have use severals libraries in order to be able to analyze and me dada visual, suchs as: ["numpy"](https://numpy.org/), ["pandas"](https://pandas.pydata.org/) , ["regex"](https://regexr.com/), ["seaborn"](https://seaborn.pydata.org/index.html), and ["matplotlib"](https://matplotlib.org/).