''' 
Executing this function initiates the application of Emotion Detection
    to be executed over the Flask channel and deployed on localhost:5000.
'''

# Import Flask, render_template, request from the flask framework package
from flask import Flask, render_template, request

# Import the EmotionDetection function from the package created
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the Flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_analyzer():
    ''' 
    Retrieve the text to analyze from the request arguments,
    pass it to the emotion detector, and return the response
    with the emotion scores and the dominant emotion.
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the emotion scores for anger, disgust, fear, joy, sadness
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']

    # Extract the dominant emotion
    dominant_emotion = response['dominant_emotion']

    # Check if the dominant emotion is None (invalid text)
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Return the response with the emotion scores and dominant emotion
    return (f"For the given statement, the system response is: "
            f"'anger': {anger_score}, 'disgust': {disgust_score}, "
            f"'fear': {fear_score}, 'joy': {joy_score} and "
            f"'sadness': {sadness_score}. "
            f"The dominant emotion is <b>{dominant_emotion}</b>.")


@app.route("/")
def render_index_page():
    ''' 
    This function initiates the rendering of the main application
    page over the Flask channel.
    '''
    return render_template('index.html')


if __name__ == "__main__":
    # This function executes the Flask app and deploys it on localhost:5000
    app.run(debug=False)
