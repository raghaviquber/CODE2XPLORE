marks_input =input("Enter marks of different subjects: ")
marks = []
num = ""
for ch in (marks_input):
    if ch != " " and ch.isdigit():
        num += ch
    else:
        if num != "":
            marks.append(int(num))
            num = ""
if num != "":
    marks.append(int(num))
total_valid = 0
total_failed = 0
print("\nOutput:")
for m in marks:
    if 0 <= m <= 100 and str(m).isdigit():
        total_valid += 1
        if m >= 90:
            print(m, "→ Excellent")
        elif m >= 75:
            print(m, "→ Very Good")
        elif m >= 60:
            print(m, "→ Good")
        elif m >= 40:
            print(m, "→ Average")
        else:
            print(m, "→ Fail")
            total_failed += 1
    else:
        print(m, "→ Invalid Marks")
print("Total Valid Subjects:", total_valid)
print("Total Failed Subjects:", total_failed)