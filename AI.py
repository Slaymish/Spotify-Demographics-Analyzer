import json
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)


def call_ai_model(wanted_format: str,expected_format: str, main_text: str) -> dict:
    """
    Call the AI model to generate structured data from the main text.
    This function is a placeholder and needs to be implemented to make actual API calls.
    """

    prompt = f"Given the text: \"{main_text}\", format the information as JSON according to this structure: {wanted_format}. An example of the expected format is: {expected_format}"


    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": "You only respond in JSON format. For any unspecifed fields, use undefined. For location, only use the country name."},
            {"role": "user", "content": prompt}
        ]
    )

    
    # Assuming the AI's response is directly usable as structured JSON
    if response and response.choices:
        content = response.choices[0].message.content
        try:
            return json.loads(content)
        except json.JSONDecodeError:
            return {"error": "Failed to decode JSON from AI response."}
    return {"error": "No valid response from AI model."}

def get_formatted_demographic_data(demographic_data: dict) -> dict:
    artist_name = demographic_data.get("artist_name")  # Assume this key holds the artist's name
    
    wanted_format = """
    {
        "gender": {
            "person1 gender",
            "person2 gender"
        }
        "age": {
            "person1 age",
            "person2 age"
        },
        "location": {
            "person1 location",
            "person2 location"
        }
    }
    """

    example_demographic = """
    {
        "gender": { "male" },
        "age": { 25 },
        "location": { "United States" }
    }
    """

    # Call the AI model to format the Wikipedia text according to the wanted format
    formatted_data = call_ai_model(wanted_format, example_demographic, demographic_data["main_text"])

    return formatted_data
