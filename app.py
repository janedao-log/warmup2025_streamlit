import streamlit as st

st.title("To-do list")

task = []

#Input information
new_task = st.text_input("New Task")

#Processing
if st.button("Add Task"):
  task.append(new_task)

#Show output
st.write("Tasks:", task)
