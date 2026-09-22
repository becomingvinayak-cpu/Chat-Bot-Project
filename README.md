
# Chat-Bot Project

A Python-based AI chatbot project built using the Gemini API and FastAPI.

This project started as a learning project to understand an AI-powered application works beyond simply calling an API. The goal is to progressively build a working chatbot while learning backend development, APIs, HTTP, JSON, and software engineering practices.

## Current Status

The backend currently includes:

- Gemini API integration
- Environment-variable based API key management 
- Modular AI logic
- HTTP communication
- FastAPI backend
- '/chat' endpoint
- Conversation memory

The frontend and additional functionality are still under development.

## Tech Stack

- Python
- Gemini API
- FastAPI
- HTTP
- JSON
- Git
- GitHub

## Project Journey

### Stage 0 - Project Setup

Set up the Python backend environment and project structure.

### Stage 1 - Gemini API connection

Connected the Python backend to the Gemini API and created the initial chatbot interaction.

### Stage 2 - Environment Variables

Moved the API key into a '.env' file instead of keeping the secret directly in the source code.

The '.env' file is excluded from Git using '.gitignore'.

### Stage 3 - Modular AI Logic 

Separated the AI-related logic into its own Python module to make the backend cleaner and easier to maintain.

### Stage 4 - HTTP and JSON

Learned how HTTP communication and JSON data are used to move information between different parts of an application.

### Stage 5 - FastAPI

Introduced FastAPI to turn the backend logic into an API.

### Stage 6 - '/chat' Endpoint

Built the '/chat' endpoint for receiving a user message and returning an AI-generated response.

### Stage 7 - Conversation Memory

Learned how to build a temporary memory for the communication between the terminal and Gemini.

## What I Am Learning ?

This project is being developed as a practical learning project. Instead of only following tutorials, I'm documenting the concepts, errors, debugging process, and architectural decisions encountered while building it.

## Challenges and Lessons

### Topic 1 - Project Setup

- Virtual Environment Creation

**Problem:**
In the Chat-Bot folder, when I selected the backend folder it didn't work.

**Error:**
Backend is a file not a folder.

**Cause:**
Venv wasn't created inside a folder.

**Solution:**
Venv should be created inside a folder not a file.

**Lesson:**
To create a venv you should create a new terminal only in a folder otherwise it won't work.

- Powershell Activation

**Problem:**
Venv was created successfully, but the Powershell wasn't activating it.

**Error:**
Running scripts was disabled on my system.

**Cause:**
Powershell's execution policy was preventing the 'activate.ps1' script from running.

**Solution:**
Run in the terminal: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

Then: \venv\Scripts\Activate.ps1

**Lesson:**
Creating a venv and activating a venv are two separate things, the environment can exist even if Powershell initially refuses to run its activation script.

### Topic 2 - Gemini API Connection

- VS code .env configuration

**Problem:**
VS code warned that terminal environment injection was disabled.

**Error:**
I wasn't able to run code in the virtual environment.

**Cause:**
VS code wasn't able to use variables from my '.env' file.

**Solution:**
Run: python.terminal.useEnvFile

Then: python-dotenv

Then: load_dotenv()

**Lesson:**

VS code also needs access to the virtual environment to run our program.

- Gemini API Error

**Problem:**
Gemini API returned a 404 NOT_FOUND error.

**Error:**
Gemini-2.5-flash was unavailable for my API access.

**Cause:**
The model specified in my code was no longer available for my account/new users.

**Solution:**
Changed the model to Gemini-3.6-flash.

**Lesson:**
An API error doesn't necessarily mean my whole program is broken. I need to read the traceback and identify where the failure occured.

- API Key Exposed

**Problem:**
I accidentally exposed my API key in my source code.

**Solution:**
Revoked the exposed key and created a new one.

**Lesson:**
Keep the API key in '.env' and access it with os.getenv("GEMINI_API_KEY").

### Topic 3 - API Key Security

**Lesson 1:**
I learned that .env values can be written with or without quotes, python-dotenv correctly reads the value either way.

**Lesson 2:**
Security isn't just about hiding a password. I need to design the application so secrets aren't part of the source code.

### Topic 4 - '/chat' Endpoint

**Lesson 1:**
A frontend sends a POST request containing JSON to '/chat'. FastAPI validates that JSON using ChatRequest. The endpoint extracts request.message and passes it to ask_gemini(). Gemini generates the answer.

The backend returns the result using ChatResponse structure. If something unexpected happens during the Gemini call, the exception is converted into an HTTP 500 error.

### Topic 5 - 

**Lesson 1:**
Temporary Python memory can store conversation data while the server is running, but it disappears when the program stops.

**Lesson 2:**
The database stores the history; the backend retrieves the relevant history and provides it to Gemini as context.

**Lesson 3:**
'conversation_id' connects messages to a conversation, 'role' identifies 'user' or 'assistant'.

**Lesson 4:**
Dictionary stores conversations temporarily in server memory.

- Python Interpreter/Path Issue

**Problem:**
The program was unable to found the interpreter.

**Error:**
Python wasn't found; run without arguments to install from the Microsoft Store...

**Cause:**
I didn't assigned the program a certain path to get interpreted.

**Solution:**
Go to Python Interpreter in VS Code.

Then: Select '.env', inside it select FastAPI.


**Lesson:**
Always make sure your program has a path to be interpreted.

## Future Plans

- Build the frontend
- Connect the frontend with the backend
- Build backend security
- Work on database
- Testing
- Deployment
- Improve the chatbot experience
- Add additional functionality
- Immprove project structure and documentation
- Continue documenting the development process

## Project Status

Actively under development