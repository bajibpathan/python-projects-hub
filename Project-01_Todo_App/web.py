import streamlit as st
import functions

# Load existing todos from the file using helper function
todos = functions.get_todos()


def add_todo():
    """
    Callback function triggered when a new todo is added.
    It appends the new todo to the list, saves it to file,
    and clears the input box.
    """
    todo = st.session_state["new_todo"] + "\n"  # Get input and add newline
    todos.append(todo)                          # Add todo to list
    functions.write_todos(todos)                # Persist todos to file
    st.session_state["new_todo"] = ""            # Clear input field


# App title and description
st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")


# Display each todo item with a checkbox
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)  # Create checkbox for each todo

    # If checkbox is checked, remove the todo
    if checkbox:
        todos.pop(index)                   # Remove from list
        functions.write_todos(todos)       # Update file
        del st.session_state[todo]         # Remove from Streamlit session state
        st.rerun()                         # Refresh app


# Input box for adding new todos
st.text_input(
    label="Todo",
    placeholder="Add new todo..",
    on_change=add_todo,
    key="new_todo"
)