PROJECT_ID = "fair-ceiling-402704"  # @param {type:"string"}
LOCATION = "us-central1"  # @param {type:"string"}

import vertexai
from vertexai.generative_models import GenerationConfig, GenerativeModel, Image, Part
vertexai.init(project=PROJECT_ID, location=LOCATION)
model = GenerativeModel("gemini-1.0-pro")

# Initialize Vertex AI
chat = model.start_chat()
prompt = '[[groceries, 70.21], [clothing, 90.66], [groceries, 13.45]]. Where could I save money?'

responses = chat.send_message(prompt, stream=True)

# with io.open('spreadsheet.xls', 'rb') as f:
#     content = f.read()
# spreadsheet = client.document_text_detection(image=content)
#
# text = spreadsheet.full_text_annotation.text

for response in responses:
    print(response.text, end="")

#Final app.py
#import files
