import streamlit as st
import pandas as pd

if "students" not in st.session_state:
    st.session_state.students = []

st.title("Student Management System")

menu = ["Add", "View", "Search", "Delete"]
choice = st.sidebar.selectbox("Menu", menu)

# Add Student
if choice == "Add":
    name = st.text_input("Student Name")
    marks = st.number_input("Marks", min_value=0, max_value=100)

    if st.button("Add Student"):
        grade = "A" if marks >= 90 else "B" if marks >= 75 else "C"
        st.session_state.students.append(
            {"Name": name, "Marks": marks, "Grade": grade}
        )
        st.success("Student Added Successfully!")

# View Students
elif choice == "View":
    if st.session_state.students:
        df = pd.DataFrame(st.session_state.students)
        st.dataframe(df)
    else:
        st.warning("No Students Available")

# Search Student
elif choice == "Search":
    search_name = st.text_input("Enter Student Name")

    if st.button("Search"):
        found = False
        for student in st.session_state.students:
            if student["Name"].lower() == search_name.lower():
                st.write(student)
                found = True
                break

        if not found:
            st.error("Student Not Found")

# Delete Student
elif choice == "Delete":
    delete_name = st.text_input("Enter Student Name")

    if st.button("Delete"):
        original_count = len(st.session_state.students)

        st.session_state.students = [
            student
            for student in st.session_state.students
            if student["Name"].lower() != delete_name.lower()
        ]

        if len(st.session_state.students) < original_count:
            st.success("Student Deleted Successfully!")
        else:
            st.error("Student Not Found")
