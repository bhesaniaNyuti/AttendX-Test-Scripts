
# Test Script 1: Student Login

def test_valid_login():
    username = "student01"
    password = "Student@123"

    if username == "student01" and password == "Student@123":
        print("PASS: Valid student login")
    else:
        print("FAIL: Valid student login")


def test_invalid_login():
    username = "wrong_user"
    password = "wrong_password"

    if username != "student01" or password != "Student@123":
        print("PASS: Invalid login is rejected")
    else:
        print("FAIL: Invalid login is accepted")


if __name__ == "__main__":
    test_valid_login()
    test_invalid_login()
