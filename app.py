import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
XAI_API_KEY = os.getenv("XAI_API_KEY") # in the .env file, or you can hardcode it here for testing.



# Notes 
# Grok-beta can handle 131,072 tokens, no clear deliniation between input and output that I can tell


if 'messages' not in st.session_state:
    st.session_state.messages = []
if "current_length" not in st.session_state:
    st.session_state.current_length = 0

sys_prompt = ""
user_prompt = ""




max_text_length = 500000 # just spit balling 4 chars per token, and leaving a little wiggle room.  You can adjust
output_governor = 20000   # reserving 5000 tokens/20000 chars for output, you can tweak these
available_chars = max_text_length - output_governor





def BuildPrompt():
    # Get the system and user prompts from the input
    new_sys_prompt = {"role": "system", "content": sys_prompt}
    new_user_prompt = {"role": "user", "content": user_prompt}
    
    # Calculate lengths based on content (text) only
    new_sys_prompt_len = len(new_sys_prompt["content"])
    new_user_prompt_len = len(new_user_prompt["content"])
    
    # If it's the first time, initialize the conversation
    if not st.session_state.messages:
        st.session_state.messages.append(new_sys_prompt)
        st.session_state.current_length = new_sys_prompt_len
    else:
        # Update the current length with the new system prompt
        current_sys_prompt_len = len(st.session_state.messages[0]["content"])
        st.session_state.messages[0] = new_sys_prompt
        st.session_state.current_length = (
            st.session_state.current_length - current_sys_prompt_len + new_sys_prompt_len
        )
    
    # Add the user prompt to the messages and update the length
    st.session_state.messages.append(new_user_prompt)
    st.session_state.current_length += new_user_prompt_len

    # Trim history if necessary
    while st.session_state.current_length > available_chars:
        removal_len = len(st.session_state.messages[1]["content"])
        del st.session_state.messages[1]
        st.session_state.current_length -= removal_len

    
    


# Todo: Finish the UI, this just dumps the text underneath the UI, will update that another night.

st.header("Simple Streamlit Grok-Beta API Test using OpenAI Chat Completion")


sys_prompt = st.text_area(label="Enter your system prompt here:", height=200)
user_prompt = st.text_area(label="Your Prompt:", height=100)



if st.button("Submit"):

    with st.spinner():
        client = OpenAI(
            api_key=XAI_API_KEY,
            base_url="https://api.x.ai/v1",
        )

        BuildPrompt()

        completion = client.chat.completions.create(
            model="grok-beta",
            messages=st.session_state.messages,
            temperature=0.7,
        )
        
    
        new_message = {"role": completion.choices[0].message.role, "content": completion.choices[0].message.content}

        st.session_state.messages.append(new_message)
        st.session_state.current_length = completion.usage.total_tokens * 4

        for m in st.session_state.messages:
            st.markdown("**" + m["role"] +"**: " + m["content"])

        print(f"Current Length: {st.session_state.current_length} Tokens: {completion.usage.total_tokens}")