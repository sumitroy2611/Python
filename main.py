import streamlit as st
import time
import os

__version__ = '20240528.1755'


def main():

    if 'hello_txt' not in st.session_state:
        st.session_state['hello_txt'] = ''

    with st.sidebar:
        st.image(os.path.join(os.getcwd(), 'kr-logo.png'))
        st.divider()

        temperature = st.slider(label='Chat temperature',
                                min_value=1,
                                max_value=3,
                                value=1,
                                step=1,
                                key='temperature')

    st.title(f"Hello, World")

    st.divider()

    user_name = st.text_input(label='Please enter your name: ',
                                key='user_name')

    button_hello = st.button(label='Say hello')

    if button_hello:
        with st.spinner():
            time.sleep(0.5)
            hello_text = [f"Hello, {user_name}" for i in range(temperature)]
            st.session_state['hello_txt'] = '\n'.join(hello_text)
    else:
        hello_text = ''

    st.divider()

    st.text_area(label="How are you",
                 value=st.session_state['hello_txt'],
                 key='generated_output')

    st.divider()

    with st.expander('StreamLit session state'):
        st.write(st.session_state)

    return True


if '__main__' == __name__:
    print('Hello i am in the main')
    main()


