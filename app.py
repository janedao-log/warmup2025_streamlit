import streamlit as st

st.title("To-do list")

if "tasks" not in st.session_state:
  st.session_state.tasks = []

#Input information
new_task = st.text_input("New Task")

#Processing
if st.button("Add Task"):
  st.session_state.tasks.append(new_task)

#Show output
st.write("Tasks:", st.session_state.tasks)
