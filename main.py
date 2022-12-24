# Importing the pipeline function from the transformers library
from transformers import pipeline
# Creating a TextClassificationPipeline for Sentiment Analysis
pipe = pipeline(task='sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')
# Analyzing sentiment
print(pipe("I do not like the way it fits."))