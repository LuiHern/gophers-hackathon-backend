from flask import Flask, request, jsonify
import boto3
import io
import base64

app = Flask(__name__)

# Initialize the Textract client
textract = boto3.client("textract", region_name="us-east-2")


@app.route("/extract-text", methods=["POST"])
def extract_text():
    # Check if the request contains an image
    if "image" not in request.files:
        return jsonify({"error": "No image provided"}), 400

    # Get the image from the request
    print("attempt to assign image from body")
    image_file = request.files["image"]

    bytes = image_file.read()



    print("calling textract")
    response = textract.analyze_id(
    DocumentPages=[
        {
            "Bytes": bytes
        },
    ]
)


    print("returning")
    return response["IdentityDocuments"][0]["IdentityDocumentFields"]


@app.route("/ping")
def ping():
    return "hi"


if __name__ == "__main__":
    app.run(debug=True)
