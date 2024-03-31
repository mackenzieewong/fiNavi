PROJECT_ID = "fair-ceiling-40270"  # kora-id ?
LOCATION = "us-central1"

import vertexai

vertexai.init(project=PROJECT_ID, location=LOCATION)
from vertexai.preview.language_models import ChatModel, InputOutputTextPair


def predict_large_language_model_sample(
        project_id: str,
        model_name: str,
        temperature: float,
        max_output_tokens: int,
        top_p: float,
        top_k: int,
        location: str = "us-central1",
) :
    """Predict using a Large Language Model."""
    vertexai.init(project=project_id, location=location)

    chat_model = ChatModel.from_pretrained(model_name)
    parameters = {
        "temperature": temperature,
        "max_output_tokens": max_output_tokens,
        "top_p": top_p,
        "top_k": top_k,
    }

    chat = chat_model.start_chat(
        examples=[]
    )
    response=chat.send_message('''Hello''',**parameters)
    print(response.text)
