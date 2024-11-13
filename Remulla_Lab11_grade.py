avecounter = 0
grade = []

for i in range(5):
    x = float(int(input("Student grade: ")))
    if x < 40 or x > 100:
        print("Invalid grade")
        break
    grade.append(x)
    if x >= 75:
        avecounter += 1

if x < 40 or x > 100:
    exit()

y = sum(grade)/5
z = (avecounter/5)*100


print("Average grade:", y)
print("Number of students with passing grade:", str(avecounter))
print("Passing percentage:", z,"%")