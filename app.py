import os
from flask import Flask, request, jsonify
import google.cloud.aiplatform as aiplatform

app = Flask(__name__)

# Set the API key as an environment variable
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = latha-424019-a4c20cec40af
# Initialize the Gemini model
model = aiplatform.gapitlm.Model(
    endpoint='projects/latha-424019/locations/us-cental1-c/models/geminiai'
)

@app.route('/generate', methods=['POST'])
def generate_text():
    prompt = request.json.get('prompt')
    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400

    try:
        # Generate text using the model
        response = model.predict(prompt)
        return jsonify({'generated_text': response.text}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
