import requests
import json

def emotion_detector(text_to_analyze):
    """
    Analyzes a given text and returns the emotion scores for different emotions 
    (anger, disgust, fear, joy, sadness) along with the dominant emotion.

    Args:
        text_to_analyze (str): The input text whose emotions need to be detected.

    Returns:
        dict: A dictionary containing emotion scores for anger, disgust, fear, joy, 
              and sadness, as well as the dominant emotion (the one with the highest score).
    """

    # URL of the Emotion Detection Service.
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Custom header specifying the model ID for the emotion detection service.
    header = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    # Construct the input JSON object with the text to be analyzed.
    myobj = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Send a POST request to the Emotion Detection API with the input text and header.
    response = requests.post(url, json=myobj, headers=header)

    # Parse the JSON response from the API.
    formatted_response = json.loads(response.text)

    # Extract the emotion predictions from the response.
    emotions = formatted_response['emotionPredictions'][0].get('emotion', {})

    # Retrieve individual emotion scores, defaulting to 0 if the emotion is not found.
    anger_score = emotions.get('anger', 0)
    disgust_score = emotions.get('disgust', 0)
    fear_score = emotions.get('fear', 0)
    joy_score = emotions.get('joy', 0)
    sadness_score = emotions.get('sadness', 0)

    # Create a dictionary to hold the emotion scores.
    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }

    # Find the dominant emotion (the one with the highest score).
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    # Return the emotion scores and the dominant emotion.
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
