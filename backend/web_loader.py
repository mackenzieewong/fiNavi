from flask import Flask, render_template, request, jsonify
import vertexai
from vertexai.generative_models import GenerativeModel, Image, Part
# import openpyxl
from flask_cors import CORS
PROJECT_ID = "fair-ceiling-402704"  # @param {type:"string"}
LOCATION = "us-central1"  # @param {type:"string"}

vertexai.init(project=PROJECT_ID, location=LOCATION)
model = GenerativeModel("gemini-1.0-pro")
app = Flask(__name__)
CORS(app)
c = model.start_chat()


@app.route('/')
def home_page():
    return render_template('home_page.html' )


@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    prompt = data.get('prompt')

    if prompt:
        responses = c.send_message(prompt, stream=True)
        response_text = "".join([response.text for response in responses])
        return jsonify({'response': response_text})
    else:
        return jsonify({'error': 'No prompt provided.'}), 400


"""The following demonstrates how transaction history can be taken off a
spreadsheet (eg xlsx) and used in the AI's decision-making process."""
# lst = []
# workbook = openpyxl.load_workbook('sample_transactions.xlsx')
# sheet = workbook['Sheet1']
# for row in sheet.iter_rows(values_only=True):
#     for value in row:
#         lst.append(value)
#
# responses = c.send_message(f'{lst}', stream=True)
# for response in responses:
#     print(response.text, end="")

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=5000)
