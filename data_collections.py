#A daļa - Saraksti

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
number_list.append(16)
number_list.pop(5)

#number_list.insert(2, 2.5)

total = 0
count = 0

for n in number_list:
    total += n
    count += 1

average = total / count

print("# --- Saraksti ---")
print(f"# Summa: {total}, Vidējais: {average}")

even_numbers = []                   #even_numbers ir saraksts
for n in number_list:               #katrs skaitlis number_list
    if n % 2 == 0:                  #ja skaitli dalīt ar divi ir True
        even_numbers.append(n)      #even_numbers izceļ pāra skaitļus

print(f"# Pāra skaitļi: {even_numbers}")

first_three = number_list[:3]
last_two = number_list[-2:]
every_second = number_list[::2]

print(f"# Pirmie 3: {first_three}, Pēdējie 2: {last_two}")

#print(len(number_list))                              #extra kods
#number_length = len(number_list)
#print("Saraksta garums ir:", number_length)

#print(number_list[2])
#print(number_list[-4])

#if 2 in number_list:
    #print("2 ir sarakstā")
    #number_list.remove(2)
#else:
    #print("2 nav sarakstā!")                         #extra kods beidzas

#B daļa - Vārdnīcas

names_dict = {"Anna": 85, "Jānis": 72, "Līga": 95, "Pēteris": 63}
names_dict["Sergejs"] = 92          #pievieno jaunu studentu
names_dict["Anna"] = 87             #nomaina esošo atzīmi

print("# --- Vārdnīcas ---")

for name, grade in names_dict.items():
    print(f"# {name}: {grade}")

best_name = ""
best_grade = -1

for name, grade in names_dict.items():
    if grade > best_grade:
        best_grade = grade
        best_name = name

print(f"# Labākais students: {best_name} ({best_grade})")

#C daļa - Kombinācija

student_list = [{"name": "Anna", "grade": 87}, {"name": "Jānis", "grade": 72}, {"name": "Līga", "grade": 95}, {"name": "Pēteris", "grade": 63}, {"name": "Sergejs", "grade": 92}]

high_grade = []
for n in student_list:
    if n["grade"] >= 80:
        high_grade.append(n)

print("# --- Studenti ar atzīmi >= 80 ---")

for i, n in enumerate(high_grade, start=1):
    print(f"# {i}. {n["name"]} - {n["grade"]}")