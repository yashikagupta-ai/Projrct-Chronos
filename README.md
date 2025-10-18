# Project Chronos: The AI Archeologist

## Team Members
- Himasree Dintakurthy - SE23UARI032
- Manogna Chalasani - SE23UCSE046
- Ishani Singh - SE23UCSE078
- Tanvi Ganesh - SE23UCSE172
- Yashika Gupta - SE23UCSE190

## Project Description
Project Chronos is an AI-powered archaeological tool that reconstructs fragmented digital texts from internet history. It uses Google Gemini for text reconstruction and web search APIs to provide contextual explanations.

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd project-chronos
Install dependencies

bash
pip install -r requirements.txt
Set up API keys

Create a .env file in the project root

Add your API keys:

text
GEMINI_API_KEY=your_actual_gemini_key
GOOGLE_SEARCH_API_KEY=your_search_key
GOOGLE_SEARCH_ENGINE_ID=your_engine_id
Run the application

bash
python main.py "your fragmented text here"
Usage Examples
bash
python main.py "brb afk coffee"
python main.py "that's what she said"
python main.py "rickroll'd"
Features
AI-powered text reconstruction using Google Gemini

Automated web search for contextual information

Comprehensive reconstruction reports

Easy-to-use command-line interface

### Step 7: Testing and Demonstration

Create test examples:
```python
# test_examples.py
test_cases = [
    "smh my bff jill. ttyl?",
    "leeroy jenkins!!!",
    "the cake is a lie",
    "y u do dis",
    "it's over 9000!"
]