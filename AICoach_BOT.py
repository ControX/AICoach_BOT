import openai
import os
import streamlit as st

# Set the OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Configure the Streamlit page
st.set_page_config(page_title="Chat with AICoach_BOT")
st.title("Chat with AICoach_BOT")
st.sidebar.markdown("Developer: [Patrik Artell/Base from Mark Craddock](https://aicoaches.se)", unsafe_allow_html=True)
st.sidebar.markdown("Current Version: 0.2.0")
st.sidebar.markdown("Using GPT-3.5-turbo API")
st.sidebar.markdown("Performance: Not optimised")
st.sidebar.markdown("Warning: May run out of OpenAI credits")

# Set the OpenAI API model
model_name = "gpt-3.5-turbo"

# Define the initial message
def initial_message():
    initial_messages = [
        {
            "role": "system",
            "content": """
            You are AICoach_BOT. A friendly customer support chatbot that helps coaches with AI Strategy and automation. 
            Sometimes you are a bit funny. You know both Swedish and English. When you reply to a question you are very
            pedagogical and helpful. If asked complicated questions use examples and metaphors. Never say anything that is 
            not true and be very interested in helping with follow up questions.
            """
        },
        {"role": "user", "content": "I want to learn about Unique Strategy"},
        {"role": "assistant", "content": "Great, what aspects of Unique Strategy are you interested in?"}
    ]
    return initial_messages

# Define the function to get the model's response
def get_model_response(chat_messages, model=model_name):
    print("model: ", model)
    result = openai.ChatCompletion.create(
        model=model,
        messages=chat_messages
    )
    return result['choices'][0]['message']['content']

# Define the function to update the chat
def update_chat_history(chat_messages, role, content):
    chat_messages.append({"role": role, "content": content})
    return chat_messages

# Define the session state variables
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []
if 'messages' not in st.session_state:
    st.session_state['messages'] = initial_message()

# Define the query input
query = st.text_input("Question: ", "", key="input")

# Process the query
if query:
    with st.spinner("Generating response..."):
        messages = st.session_state['messages']
        messages = update_chat_history(messages, "user", query)
        response = get_model_response(messages, model_name)
        messages = update_chat_history(messages, "assistant", response)
        st.session_state.past.append(query)
        st.session_state.generated.append(response)

# Display the generated responses
if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        st.markdown(f"**Assistant**: {st.session_state['generated'][i]}")
        st.markdown(f"**User**: {st.session_state['past'][i]}")
