from flask import Flask, request, jsonify
import boto3
import io
import base64
import json

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
            {"Bytes": bytes},
        ]
    )

    response_dict = {}
    for elem in response["IdentityDocuments"][0]["IdentityDocumentFields"]:
        response_dict[elem["Type"]["Text"]] = elem["ValueDetection"]["Text"]

    return response_dict
        

    # print("returning")
    # return response["IdentityDocuments"][0]["IdentityDocumentFields"][0]


@app.route("/ping")
def ping():
    return "hi"


if __name__ == "__main__":
    app.run(debug=True)
