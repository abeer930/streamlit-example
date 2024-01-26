import streamlit as st

# Title
st.title("My Streamlit App")

# Header
st.header("Welcome to my app!")

# Text
st.text("This is some text.")

# Markdown
st.markdown("### This is a markdown title")

# Button
button_clicked = st.button("Click me!")
if button_clicked:
    st.write("Button clicked!")

# Checkbox
checkbox_state = st.checkbox("Check me!")
if checkbox_state:
    st.write("Checkbox checked!")

# Slider
slider_value = st.slider("Slide me", 0, 100, 50)
st.write("Slider value:", slider_value)

# Selectbox
option = st.selectbox("Select an option", ["Option 1", "Option 2", "Option 3"])
st.write("Selected option:", option)

# File uploader
uploaded_file = st.file_uploader("Upload a file")
if uploaded_file is not None:
    st.write("File uploaded!")

# Plotting
st.subheader("Data Visualization")
data = [1, 2, 3, 4, 5]
st.line_chart(data)

# Displaying images
st.subheader("Image")
image_url = "https://example.com/image.jpg"
st.image(image_url, caption="Example Image", use_column_width=True)

# Dataframe
st.subheader("Dataframe")
import pandas as pd
data = {"Name": ["John", "Jane", "Alice"], "Age": [25, 30, 35]}
df = pd.DataFrame(data)
st.dataframe(df)

# Display raw code
st.subheader("Code")
code = '''
def hello():
    print("Hello, Streamlit!")
hello()
'''
st.code(code, language="python")
