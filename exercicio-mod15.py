import streamlit as st
import pandas as pd
import numpy as np

st.markdown("# Exercício  - Módulo 15")
st.markdown("### Código #1")#1
"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

st.markdown("### Código #2")#2
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

st.markdown("### Código #3")#3
dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

st.markdown("### Código #4")#4
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))

st.markdown("### Código #5")#5
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)

st.markdown("### Código #6")#6
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

st.markdown("### Código #7")#7
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

st.markdown("### Código #8")#8
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

st.markdown("### Código #9")#9
st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name

st.markdown("### Código #10")#10
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

st.markdown("### Código #11")#11
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })


option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option

st.markdown("### Código #12 (sidebar)")#12
# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    '#12 - How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

st.markdown("### Código #13 (sidebar)")#13
# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    '#13 - Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

st.markdown("### Códigos #14 e #15")
#14
left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

#15
# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")

import time

st.markdown("### Código #16")#16
'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'

st.markdown("### Código #17")#17
with st.echo():
    st.write("Code will be executed and printed")

st.markdown("### Código #18")#18
# Insert a chat message container.
with st.chat_message("user"):
    st.write("Hello 👋")
    st.line_chart(np.random.randn(30, 3))

# Display a chat input widget.
st.chat_input("Say something")


st.markdown("### Código #19")#19
st.camera_input("Take a picture")


st.markdown("### Código #20")#20
st.image("https://cdn4.vectorstock.com/i/1000x1000/75/43/smiling-emoticon-wearing-sunglasses-giving-thumb-u-vector-5077543.jpg")

