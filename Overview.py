import streamlit as st

st.set_page_config(
    page_title="Overview",
)


st.image('data/equipo_uno.jpg')


st.title('Build a Machine Learning Web App with Streamlit')

st.header('Objectives')
st.markdown('1. Understand the basics of Streamlit')
st.markdown('2. Import and use a pre-trained model')
st.markdown('3. Build a simple web app using Streamlit')
st.markdown('4. Deploy the web app')

st.header('What is Streamlit?')
st.write('Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science. In just a few minutes you can build and deploy powerful data apps - and host them for free.')

st.header('Pros and Cons')

st.markdown("""
| Pros | Cons |
| :---: | :---: |
| Easy to use | Limited customizations |
| Fast | Limited interactivity |
| Free hosting | Limited deployment options |
| Python | Limited support for other languages |
""")


st.header('Let\'s get started!')

st.markdown('1. **Clone this repo**')
st.markdown('[Streamlit DS450 Demo](https://github.com/lsneth/bd_streamlit/tree/main)')

st.markdown('2. **Install the required packages**')
st.code('pip install -r requirements.txt')
st.markdown('If you have issue with any of the packages, try creating a [virtual environment and install the packages](https://docs.streamlit.io/get-started/installation/command-line).')

st.markdown('3. **Run the app**')
st.code('streamlit run app.py')

st.markdown('4. **Learn how to explore data**')

st.markdown('5. **Import a ML model and use it**')

st.markdown('6. **Deploy the app**')

st.header('Add more content!')
st.markdown('[API Reference](https://docs.streamlit.io/library/api-reference)')


