import json
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

response_json_format = """
    {
        "title":"project_title",
        "difficulty":project_difficulty_integer,
        "description":"project_description_short",
        "techstack":["string", "string"],
        "roadmap":["day - day , objective : objective , tasks : tasks", "day - day , objective : objective , tasks : tasks"]
    }
    
    the roadmap does not have any nested json structs it is just one array for each day
"""

def generate_project(techstack = "Random" , difficulty = "random",duration = "7 days",theme="random systems and backend engineering centered"):
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    chat = client.chats.create(model="gemini-3.5-flash-lite")

    prompt = f"""
    Generate a {duration} roadmap for a Software Engineering projects 
    The theme is {theme} 
    The Tech-Stack is {techstack}
    The difficulty is {difficulty} on a scale of 3-10
    Be Straight to the point and precise giving a clear outline in json format.
    
    return only one valid raw json  project in this structure as the response
    {response_json_format}
    
    without the preceeding ```json content tags ```
    """

    response = chat.send_message(f"{prompt}")
    print(response.text)
    data = json.loads(response.text)

    return data
