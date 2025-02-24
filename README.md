# Twitter Sentiment Analysis


## Overview  


This project analyzes sentiment from a Twitter dataset using Python, Pandas, Matplotlib, Seaborn, and WordCloud. The dataset is preprocessed to remove missing values, and visualizations are generated to explore sentiment distribution and word frequency.  

## Features  


- *Data Cleaning:* Removes missing values and saves a processed dataset.
- 
- *Sentiment Distribution:* A bar chart shows the distribution of sentiments.
- 
- *Entity-Based Sentiment:* Visualizes sentiment for the top 10 most mentioned entities.
- 
- *Word Clouds:* Generates word clouds for positive and negative sentiments.  

## Dataset  


The dataset (twitter_training.csv) consists of:  

- id: Unique identifier
- 
- entity: Entity mentioned in the tweet
- 
- sentiment: Sentiment label (Positive, Negative, Neutral, or Others)
- 
- text: Tweet content  

## Installation  

### Prerequisites  
Ensure you have Python installed along with the required libraries: 

```bash

pip install pandas matplotlib seaborn wordcloud

## Result

Sentiment distribution graph

Entity-based sentiment distribution

Word clouds for positive and negative sentiments
