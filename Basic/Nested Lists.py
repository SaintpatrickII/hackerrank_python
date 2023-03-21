if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    # sorts students by grade
    # students = sorted(students, key=lambda x: x[1], reverse=True)

    # takes set of all scores, sorts them ascending & takes 2nd lowest score
    second_lowest = sorted(list(set([x[1] for x in students])))[1]
    

    #  for students if make == second lowest adds name to the wanted students
    wanted_students = []
    for pupil in students:
        if pupil[1] == second_lowest:
            wanted_students.append(pupil[0])
    
    #  new line prints all students with second lowest scores alphabetically
    print('\n'.join(sorted(wanted_students)))
        
    # print(students)