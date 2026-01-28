import streamlit as st

st.title("To-do list")

if "tasks" not in st.session_state:
  st.session_state.tasks = []

#Input information
# new_task = st.text_input("New Task")
Year = st.text_input("Năm Kinh Nghiệm")
salary = st.number_input("Mức Lương", min_value=0, value=0)

#Processing
if st.button("Add Info"):
  # st.session_state.tasks.append(new_task)
  real_salary = salary*1.2 if int(Year) > 5 else salary

#Show output
# for i, task in enumerate(st.session_state.tasks):
#   st.write(f"ID - {i}: Value - {task}")
st.write(f"Real Salary: {real_salary}")
