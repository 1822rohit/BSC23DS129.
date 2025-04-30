# Define a custom haskey function
def haskey(dictionary, key):
    return key in dictionary

# Initialize an attendance ledger
attendance_ledger = {
    "Alice": ["2025-04-01", "2025-04-02"],
    "Bob": ["2025-04-01"],
    "Charlie": []
}

# Function to mark attendance
def mark_attendance(student_name, date):
    if haskey(attendance_ledger, student_name):
        attendance_ledger[student_name].append(date)
    else:
        print(f"{student_name} not found in the ledger.")

# Example usage
mark_attendance("Alice", "2025-04-03")
mark_attendance("David", "2025-04-01")  # Student not in ledger

# Print updated ledger
for student, dates in attendance_ledger.items():
    print(f"{student}: {dates}")
