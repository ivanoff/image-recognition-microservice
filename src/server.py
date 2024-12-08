import os
from flask import Flask, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer
from PIL import Image
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")

if not API_TOKEN:
    raise ValueError("API_TOKEN is not set in the .env file")

# Initialize model and tokenizer
model_id = "vikhyatk/moondream2"
revision = "2024-08-26"
model = AutoModelForCausalLM.from_pretrained(
    model_id, trust_remote_code=True, revision=revision
)
tokenizer = AutoTokenizer.from_pretrained(model_id, revision=revision)

# Create Flask app
app = Flask(__name__)

@app.route("/", methods=["POST"])
def process_image():
    # Check API token
    token = request.headers.get("Authorization")
    if not token or token.split(" ")[-1] != API_TOKEN:
        return jsonify({"error": "Unauthorized"}), 401

    # Check form data
    if "image" not in request.files:
        return jsonify({"error": "'image' is required"}), 400

    image_file = request.files["image"]
    question = request.form.get("question", "Describe this image")

    try:
        # Load and process the image
        image = Image.open(image_file)
        enc_image = model.encode_image(image)

        # Generate the answer
        answer = model.answer_question(enc_image, question, tokenizer)
        return jsonify({"question": question, "answer": answer}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

