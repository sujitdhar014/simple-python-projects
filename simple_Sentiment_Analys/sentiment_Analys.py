from textblob import TextBlob
from dataclasses import dataclass

@dataclass
class Mood:
    emoji: str
    sentiment: float

def get_mood(input_text: str, *, threshold: float) -> Mood:
    sentiment = TextBlob(input_text).sentiment.polarity

    # Define emoji and sentiment values based on sentiment polarity
    if sentiment >= threshold:
        emoji = "😄"  # Positive emoji
    elif sentiment <= -threshold:
        emoji = "😡"  # Negative emoji
    else:
        emoji = "😐"  # Neutral emoji

    return Mood(emoji, sentiment)

if __name__ == "__main__":
    while True:
        text = input('Text: ')
        mood = get_mood(text, threshold=3)

        print(f'{mood.emoji} ({mood.sentiment})')
