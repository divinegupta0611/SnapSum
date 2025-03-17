# **Summary Generator Tool**

This tool generates a summary of the given text content using **Flask** and **Text Processing Python Libraries**.  
---

## **Tech Stack**
-Backend:
    Python,
    Flask,
    Text Processing Libraries (SpaCy, NLTK, Heapq)

    
-Frontend:
    HTML5,
    CSS3,
    Bootstrap,
    Jinja2 (Flask's templating engine)

---

## **Getting Started**

# Clone the repository
git clone https://github.com/your-username/your-repo.git

# Navigate into the project directory
cd your-repo

# Create and activate a virtual environment
python -m venv env       (create virtual env.)


source env/bin/activate  # For Linux/macOS


.\env\Scripts\activate   # For Windows


## **Tool Workflow**

### **1. Text Processing Function**
- The `text_summary.py` file contains a function that processes the input text and generates a summary.
- It uses the **normalized frequency of words** and sentences to identify the key sentences for the summary.
- The function ensures that the most important content is retained while reducing redundancy.

### **2. Flask Application**
- The `app.py` file sets up a **Flask web application**.
- This application provides a user-friendly **Graphical User Interface (GUI)** for the tool.
- Users can:
  - Input the text content through the web interface.
  - Click the **"Generate Summary"** button to receive the summarized text output.
 
## Usage

### Run the Flask Application

1.Start the Flask server:
python app.py


2.Access the Tool:
Open your browser and navigate to :
http://127.0.0.1:5000/


Input the text content in the provided field.


Click the "Generate Summary" button to get the summarized text.
