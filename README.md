# Content Factory

This project is a Content Factory that automates the creation of audio content from Reddit. It fetches the top comments from the `r/AskReddit` subreddit, cleans the HTML, and uses Microsoft Azure's Text-to-Speech service to generate MP3 audio files of the comments.

## How it Works

1.  **Fetches Content:** The application fetches the top 5 comments from the current top 'hot' post in the `r/AskReddit` subreddit using the Python Reddit API Wrapper (`praw`).
2.  **Cleans Data:** The HTML from the Reddit comments is stripped, leaving plain text.
3.  **Synthesizes Speech:** The plain text is then converted to speech using Azure's Text-to-Speech service. The voice is configured to have an 'angry' tone using SSML.
4.  **Saves Audio:** The generated MP3 audio files are saved to a temporary directory.

The application can be run in two ways:

*   As a command-line script using `main.py`.
*   As a web service with a FastAPI backend using `api.py`.

## Technologies Used

*   **Python**
*   **FastAPI:** For the web service API.
*   **PRAW (Python Reddit API Wrapper):** For interacting with the Reddit API.
*   **Beautiful Soup:** For parsing and cleaning HTML.
*   **Azure Cognitive Services Speech SDK:** For text-to-speech synthesis.
*   **python-dotenv:** For managing environment variables.

## Setup and Installation

1.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Create a `.env` file:**
    Create a `.env` file in the root of the project and add the following environment variables:

    ```
    CLIENT_ID=<Your Reddit application's client ID>
    CLIENT_SECRET=<Your Reddit application's client secret>
    USER_AGENT=<A descriptive user agent for your Reddit application>
    SPEECH_KEY=<Your Azure Cognitive Services subscription key>
    SPEECH_REGION=<The region for your Azure Speech service>
    TEMP_DIR=<The absolute path to a directory for storing generated audio files>
    ```

## Running the Application

### As a Command-Line Script

```bash
python main.py
```

### As a Web Service

```bash
uvicorn api:app --reload
```

This will start a local development server. You can access the API documentation at `http://127.0.0.1:8000/docs`.
