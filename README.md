# Netflix-and-TV-Shows-Clustering-and-recommendation-system
Problem Statement
This dataset consists of tv shows and movies available on Netflix as of 2019. The dataset is collected from Flixable which is a third-party Netflix search engine.

In 2018, they released an interesting report which shows that the number of TV shows on Netflix has nearly tripled since 2010. The streaming service’s number of movies has decreased by more than 2,000 titles since 2010, while its number of TV shows has nearly tripled. It will be interesting to explore what all other insights can be obtained from the same dataset.

Integrating this dataset with other external datasets such as IMDB ratings, rotten tomatoes can also provide many interesting findings.

In this project, you are required to do
Exploratory Data Analysis

Understanding what type content is available in different countries

Is Netflix has increasingly focusing on TV rather than movies in recent years.

Clustering similar content by matching text-based features

Attribute Information
show_id : Unique ID for every Movie / Tv Show

type : Identifier - A Movie or TV Show

title : Title of the Movie / Tv Show

director : Director of the Movie

cast : Actors involved in the movie / show

country : Country where the movie / show was produced

date_added : Date it was added on Netflix

release_year : Actual Releaseyear of the movie / show

rating : TV Rating of the movie / show

duration : Total Duration - in minutes or number of seasons

listed_in : Genere

description: The Summary description



Summary of the project

Data Visualization: 

Data visualization techniques for instance histogram, line graphs, heatmaps, box plots,pie charts etc helps us in understanding the pattern the data follows. Firstly, we used a pie chart plot to look at the type column. Then we used bar plots and boxplots to visualize the other variables, as most of the variables are categorical in nature. Further we went on to look at the other variable like director ,release date,cast and visualized them using bar chart and word cloud
Feature Engineering (Natural Language Processing):
Natural Language Processing techniques are used so that computers can understand human languages. We performed Natural Language processing techniques like cleaning, removing stopwords, stemming, TF-IDF vectorization. Further we went ahead to perform Principal Component Analysis on the features of the vectorised version of the text based columns.

Feature Selection:

Feature selection helps in reducing the number of input variables to decrease the computational cost of modeling and in some cases it improves the performance of the model.
We selected categorical columns like rating, year and type for K-modes clustering. And we selected text based columns description, listed_in, cast and director for K-means and Hierarchical Clustering. 
  
Optimal number of Cluster Selection:

After training the dataset on KMode and KMeans models and evaluating on the four evaluation metrics- Elbow method, Silhouette Score, Calinski-Harabasz Index, Dendrogram, the optimal number of clusters came out to be 6 for both the models and for KMeans on the basis of majority from Dendrogram and Elbow Method. 
 
Model Clusters :
Using 6 as the optimal number of clusters under Kmode algorithm the 14 rating variables got clustered properly each cluster comprising mostly one kind of rated content except cluster 1 and 6 comprises Movies and Tv Shows of various ratings. Under KMeans algorithm the Cluster 1 comprises mostly of Documentaries and Musical Documentaries, cluster 2-Dramas and International Movies,cluster 3- Children and Family Movies,cluster 4-Children and Family Movies,cluster 5-International Tv Shows and Tv Dramas, cluster 6-Stand Up Comedy and Talk Shows.

Prediction And Recommendation :-

Recommendation engines basically filter the data and recommend most relevant results to users. These results are recommended in such a manner that likelihood of interest results in maximum. We created a recommendation system by Using Cosine similarity matrix.Cosine similarity is a metric used to measure how similar two items are. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. The output value ranges from 0–1. When we provided a movie name ‘Handsome Devil’ then in recommendation we get similar type of genre movie like Secret time, homecoming king, live in new york….etc  in recommendation  
