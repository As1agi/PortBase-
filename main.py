from  fastapi import FastAPI
import database
import gemini as ai

#check for database.db if not exists we run the migration script
database.migrate( )
app = FastAPI()
@app.get("/api/v1/projects/generate")
def generate():
    data = ai.generate_project()
    database.addProject(data["title"],data["difficulty"],data["description"],data["techstack"],data["roadmap"])
    return data
