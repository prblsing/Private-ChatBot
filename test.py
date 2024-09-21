import streamlit as st

# Create a title for the application
st.title('My Streamlit Conversational Bot')

# Left panel
st.sidebar.title('Sidebar')
year = st.sidebar.selectbox('Select a year', options=range(2000, 2023))

# Initialize chat log
if 'chat_log' not in st.session_state:
    st.session_state['chat_log'] = []

# Display chat
st.subheader('Chat')
for message in st.session_state['chat_log']:
    st.write(message)

# User input
if 'user_input' not in st.session_state:
    st.session_state['user_input'] = ''

user_input = st.text_input('Enter your message', value=st.session_state['user_input'])

# Respond to user
if st.button('Send'):
    # Append user's message to chat log
    st.session_state['chat_log'].append(f'You: {user_input}')

    # Generate a response
    bot_response = f'Bot: You said "{user_input}" in the year {year}.'
    st.session_state['chat_log'].append(bot_response)

    # Clear the input box by updating the session_state
    st.session_state['user_input'] = ''
