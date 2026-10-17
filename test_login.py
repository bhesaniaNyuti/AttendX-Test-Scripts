
# Test Script 1: Student Login
# Application: AttendX Student Attendance App

def test_valid_login():
    username = "student01"
    password = "Student@123"

    if username == "student01" and password == "Student@123":
        print("PASS: Valid student login")
    else:
        print("FAIL: Valid student login")


if __name__ == "__main__":
    test_valid_login()
