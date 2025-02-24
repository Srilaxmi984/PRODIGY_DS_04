import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load the dataset (replace with your actual file path)
df = pd.read_csv("twitter_training.csv", header=None)

# Assign column names based on dataset structure
df.columns = ['id', 'entity', 'sentiment', 'text']

# Drop any missing values
df.dropna(inplace=True)

# Sentiment distribution visualization
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='sentiment', palette='coolwarm', order=df['sentiment'].value_counts().index)
plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.show()

# Sentiment per entity
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='entity', hue='sentiment', palette='coolwarm', order=df['entity'].value_counts().index[:10])
plt.xticks(rotation=45)
plt.title("Sentiment by Entity (Top 10)")
plt.xlabel("Entity")
plt.ylabel("Count")
plt.show()

# WordCloud for positive sentiment
positive_text = " ".join(df[df['sentiment'] == 'Positive']['text'])
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(positive_text)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Word Cloud for Positive Sentiment")
plt.show()

# WordCloud for negative sentiment
negative_text = " ".join(df[df['sentiment'] == 'Negative']['text'])
wordcloud = WordCloud(width=800, height=400, background_color='black').generate(negative_text)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Word Cloud for Negative Sentiment")
plt.show()

# Save processed dataset
df.to_csv("processed_twitter_sentiment.csv", index=False)
