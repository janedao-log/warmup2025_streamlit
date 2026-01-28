import streamlit as st
st.title("Basic To-do list")

if 'tasks' not in st.session_state:
    st.session_state.tasks = []
    st.session_state.next_id = 0

with st.form("add_form"):
    new_task = st.text_input("New task")
    btn_form = st.form_submit_button("Add")

if btn_form and new_task:
    task = {
        "id": st.session_state.next_id,
        "text": new_task,
        "done": False
    }
    st.session_state.tasks.append(task)

    st.session_state[f"done_{task['id']}"] = False
    st.session_state.next_id += 1
    st.rerun()

for i, task in enumerate(st.session_state.tasks):
    col1, col2 = st.columns([0.1, 0.9])
    
    checkbox_key = f"done_{task['id']}"

    with col1:
        done = st.checkbox(
            "",
            key = checkbox_key
        )
        task["done"] = done

    with col2:
        status = "✅" if task["done"] else "🙅‍♀️"
        st.write(f"{status} {task['text']}")
