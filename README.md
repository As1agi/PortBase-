# PortBase

PortBase is a project generation engine for people who want to build but don't know what to build yet.

It generates project ideas based on a predefined technology stack and saves the generated projects to a local SQLite database.

## How to Run

### Prerequisites

Make sure you have:

* Python 3 installed
* Git installed (optional, if cloning the repository)

### Step 1: Create a Virtual Environment

Move into the PortBase directory and create a Python virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

**Linux/macOS:**

```bash
source .venv/bin/activate
```

**Windows:**

```powershell
.venv\Scripts\activate
```

### Step 2: Install Dependencies

Install the required Python packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Step 3: Configure the API Key

Create a `.env` file in the root directory of the project:

```bash
touch .env
```

Create a Gemini API key from Google AI Studio:

https://aistudio.google.com/api-keys

Add the key to `.env` using the following variable:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

### Step 4: Start the Application

Run the FastAPI application using Uvicorn:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

### Step 5: Generate a Project

Navigate to:

```text
http://127.0.0.1:8000/api/v1/projects/generate
```

This endpoint generates a project using Gemini and saves the resulting project to the local SQLite database.
