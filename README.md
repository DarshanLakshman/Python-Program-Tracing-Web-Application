# Python Program Tracing Application

A web-based educational platform designed to help users visualize the execution of Python code. This interactive debugger allows users to input code, execute it step-by-step, and observe the state of variables and program flow in real-time.

## Live Sites

* **[Original Version (No Input Support)](http://traceTableProject.pythonanywhere.com)**
    * *Best for quick start-up times.*
* **[Full Version (Includes Input Support)](https://python-program-tracing-web-application-2.onrender.com/)**
    * *Utilizes Gunicorn and supports `stdin` inputs. Note: Hosting on Render may experience "cold starts," causing a slight delay on initial visits.*

## Features

* **Interactive Visualization:** Supports "Side-by-Side" and "Top-to-Bottom" views for analyzing code execution flow.
* **Input Handling:** Fully supports the `input()` function within the traced Python code.
* **Educational Resources:** Dedicated pages for application information and PyTracer module documentation.
* **Robust Error Handling:** Built-in mechanisms to catch and display code execution errors gracefully.

## Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML5, Bootstrap 5, FontAwesome, CodeMirror

## Project Structure

    ├── app.py                            # Main Flask application controller
    ├── errors.py                         # Custom exception handling for tracing logic
    ├── requirements.txt                  # Project dependencies
    ├── static/                           # CSS, JavaScript, and favicon
    └── templates/                        # HTML interface files
        ├── base.html                     # Core layout
        ├── index.html                    # Side-by-side visualization view
        ├── index2.html                   # Top-to-bottom visualization view
        ├── information.html              # Informational page
        └── documentation_display.html    # PyTracer documentation

## Installation & Usage Locally

### 1. Clone the repository
    git clone https://github.com/DarshanLakshman/Python-Program-Tracing-Web-Application
    cd Python-Program-Tracing-Web-Application

### 2. Install dependencies
Ensure you are in the project root directory, then install the required packages:
    pip install -r requirements.txt (Windows)
    pip3 install -r requirements.txt (Windows)
    

### 3. Run the application
    python app.py (on Windows)
    python3 app.py (on Mac)

### 4. Access the application
Open your web browser and navigate to the local address provided in your terminal (using localhost `http://127.0.0.1:5000`).
