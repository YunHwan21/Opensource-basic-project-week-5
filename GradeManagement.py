# 입력 함수
def input_student():
    students = []
    for i in range(5):
        student = {}
        student['학번'] = input("학번을 입력하세요: ")
        student['이름'] = input("이름을 입력하세요: ")
        student['영어'] = int(input("영어 점수를 입력하세요: "))
        student['C언어'] = int(input("C언어 점수를 입력하세요: "))
        student['파이썬'] = int(input("파이썬 점수를 입력하세요: "))
        students.append(student)
    return students

# 총점/평균 계산 함수
def calculate_score(students):
    for student in students:
        student['총점'] = student['영어'] + student['C언어'] + student['파이썬']
        student['평균'] = student['총점'] / 3
    return students

# 학점 계산 함수
def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# 등수 계산 함수
def calculate_rank(students):
    sorted_students = sorted(students, key=lambda x: x['총점'], reverse=True)
    for i, student in enumerate(sorted_students):
        student['등수'] = i + 1
    return students

# 출력 함수
def print_student(student):
    print(f"학번: {student['학번']}, 이름: {student['이름']}, 영어: {student['영어']}, C언어: {student['C언어']}, 파이썬: {student['파이썬']}, 총점: {student['총점']}, 평균: {student['평균']}, 학점: {student['학점']}, 등수: {student['등수']}")


# 삽입 함수
def insert_student(students, new_student):
    students.append(new_student)
    return students

# 삭제 함수
def delete_student_by_id(students, student_id):
    for student in students:
        if student['학번'] == student_id:
            students.remove(student)
            break
    return students

# 탐색 함수(학번, 이름)
def search_student_by_id(students, student_id):
    for student in students:
        if student['학번'] == student_id:
            return student
    return None

def search_student_by_name(students, name):
    for student in students:
        if student['이름'] == name:
            return student
    return None

# 정렬(총점) 함수
def sort_students_by_score(students):
    return sorted(students, key=lambda x: x['총점'], reverse=True)

# 80점 이상 학생 수 카운트 함수
def count_students_above_80(students):
    count = 0
    for student in students:
        if student['총점'] >= 80 * 3:
            count += 1
    return count

# 메인 함수
def main():
    students = input_student()
    students = calculate_score(students)
    for student in students:
        student['학점'] = calculate_grade(student['평균'])  # 개별 학생의 평균 점수를 전달
    students = calculate_rank(students)

    while True:
        print("\n1. 삽입  2. 삭제  3. 탐색  4. 종료")
        choice = input("메뉴를 선택하세요: ")

        if choice == '1':
            new_student = {}
            new_student['학번'] = input("학번을 입력하세요: ")
            new_student['이름'] = input("이름을 입력하세요: ")
            new_student['영어'] = int(input("영어 점수를 입력하세요: "))
            new_student['C언어'] = int(input("C언어 점수를 입력하세요: "))
            new_student['파이썬'] = int(input("파이썬 점수를 입력하세요: "))
            students = insert_student(students, new_student)
            students = calculate_score(students)  # 수정된 학생 정보에 대해 다시 총점 계산
            for student in students:
                student['학점'] = calculate_grade(student['평균'])  # 수정된 학생 정보에 대해 다시 학점 계산
            students = calculate_rank(students)  # 수정된 학생 정보에 대해 다시 등수 계산
            print("학생이 추가되었습니다.")
        elif choice == '2':
            student_id = input("삭제할 학생의 학번을 입력하세요: ")
            result = delete_student_by_id(students, student_id)
            if result:
                print("학생이 삭제되었습니다.")
                students = result
            else:
                print("학번이 일치하는 학생이 없습니다.")
        elif choice == '3':
            search_type = input("탐색할 방법을 선택하세요 (1: 학번, 2: 이름): ")
            if search_type == '1':
                student_id = input("탐색할 학생의 학번을 입력하세요: ")
                student = search_student_by_id(students, student_id)
            elif search_type == '2':
                name = input("탐색할 학생의 이름을 입력하세요: ")
                student = search_student_by_name(students, name)

            if student:
                print("\n검색 결과:")
                print_student(student)
            else:
                print("일치하는 학생이 없습니다.")
        elif choice == '4':
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 메뉴를 선택하세요.")


if __name__ == "__main__":
    main()
