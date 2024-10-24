# What is this?

I wanted to test out the Grok-beta API so I started working on this streamlit wrapper for it. I'm using the OpenAI Python Package since Grok is compatible with it.

Note: You need a Grok API Key to run this.

This runs, and displays output, but the UI is not finished. All the time I could put into it for tonight.

## Installation (Windows... but similar steps in other environments, translate as you go)

In Visual Studio Code or a similar IDE:

Step 1 Create a virtual environment (I use `venv`) by doing:
- Open a terminal window.
- Type `python -m venv .venv`.
- When complete, type `.venv\scripts\activate`.
- Make sure your virtual environment is active.

Step 2
- Type `pip install -r requirements.txt`.
- Make sure you have a `.env` file with your xAI Key or hardcode it in the `app.py` page.

Step 3 
- Run in streamlit.  I always forget how so I just run the page, it will error out, but int he console window it will give you the command and the path to start up Streamlit

If you don't want to have Streamlit fire up you can run the test page and change the prompts, but it is just a single shot, the app.py will keep track of the chat history and send the chat stream 
to Grok for context.

Have fun!

   
