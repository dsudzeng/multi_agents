import streamlit as st
import json
import subprocess

# Path to the task.json file and main.py script
task_json_path = 'multi_agents/task.json'
main_script_path = 'multi_agents/main.py'

# Streamlit app
st.title("Query Submission App")
st.write("Enter your query below:")

# Textbox for user input
user_query = st.text_area("Query")

# Submit button
if st.button("Submit"):
    if user_query.strip():
        # Read the existing task.json file
        with open(task_json_path, 'r') as file:
            task_data = json.load(file)

        # Update the query in the task.json file
        task_data['query'] = user_query

        # Write the updated task.json file
        with open(task_json_path, 'w') as file:
            json.dump(task_data, file, indent=4)

        # Execute the main.py script
        result = subprocess.run(["python", main_script_path], capture_output=True, text=True)

        # Display the output of the script execution
        st.write("Script executed with the following output:")
        st.write(result.stdout)
        st.write(result.stderr)
    else:
        st.write("Please enter a valid query.")
