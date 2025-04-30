import streamlit as st

# Define a custom haskey function
def haskey(dictionary, key):
    return key in dictionary

# Initialize or retrieve attendance ledger from session state
if 'attendance_ledger' not in st.session_state:
    st.session_state.attendance_ledger = {
        "Alice": ["2025-04-01", "2025-04-02"],
        "Bob": ["2025-04-01"],
        "Charlie": []
    }

attendance_ledger = st.session_state.attendance_ledger

# Streamlit UI
st.title("📘 Student Attendance Ledger")

# Form to mark attendance
with st.form("attendance_form"):
    student_name = st.text_input("Enter student name")
    date = st.date_input("Select attendance date")
    submit = st.form_submit_button("Mark Attendance")

    if submit:
        if haskey(attendance_ledger, student_name):
            attendance_ledger[student_name].append(str(date))
            st.success(f"Attendance marked for {student_name} on {date}")
        else:
            st.error(f"{student_name} not found in the ledger.")

# Display attendance ledger
st.subheader("📋 Current Attendance Ledger")
for student, dates in attendance_ledger.items():
    st.write(f"**{student}**: {', '.join(dates) if dates else 'No attendance yet'}")
