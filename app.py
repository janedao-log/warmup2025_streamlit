import streamlit as st

st.title("To-do list")

if "tasks" not in st.session_state:
  st.session_state.tasks = []

#Input information
new_task = st.text_input("New Task")
# Year = st.text_input("Năm Kinh Nghiệm")
# salary = st.number_input("Mức Lương", min_value=0, value=0)
# real_salary = 0

#Processing
if st.button("Add Task"):
  st.session_state.tasks.append(new_task)
  print("Add task:", st.session_state.tasks)
  # real_salary = salary*1.2 if int(Year) > 5 else salary
  # real.salary = model.predit(salary)

#Show output
for i, task in enumerate(st.session_state.tasks):
  col1, col2 = st.columns([3,1])
  with col1:
    st.write(f"{i}: {task}")
  with col2:
    if st.button("Delete", key=f"{i}"):
      st.session_state.tasks.pop(i)
      # st.return()
  # st.write(f"ID - {i}: Value - {task}")
# st.write(f"Real Salary: {real_salary}")
