class ManagementSystem:
    def __init__(self):
        self.students = []
    def add_student(self):
        name = input('Enter student name: ').strip()
        if not name: #make sure the name is vaild
            print('Student name cannot be empty~')
            return
        for s in self.students:
            if s['name'] == name:
                print('Sorry,student already exists~')
                return
        try:
            scores = list(map(int, input('Enter scores: ').split(','))) # convert the input str type into an int list
            if not scores: #to check the score list is valid
                print('Please enter at least one score~')
                return
        except ValueError: # capture the error if the element in the score list is not an int type
            print('Please enter valid integer scores separated by commas~') # ask to input again if the score list contains some other types of data
            return
        except Exception as e:
            print(e)
            return
        self.students.append({'name': name, 'scores': scores})
        print('Student added successfully~')

    def show_students(self):
        if not self.students:
            print('the student list is empty~')
            return
        for s in self.students:
            if not s['scores']: #check the score list is not empty
                print(f'There is no available score for {s['name']}~')
                continue
            avg = round(sum(s['scores']) / len(s['scores']), 2)
            print(f"name: {s['name']}, scores: {s['scores']}, average score: {avg}")

    def find_student(self):
        name = input('Enter student name to find: ').strip()
        if not name:
            print('Student name cannot be empty~')
            return
        found = False # create a flag
        for s in self.students:
            if s['name'] == name:
                print(s)
                found = True
                break
        if not found:
            print('Student does not exists~')

    def remove_student(self):
        name = input('Enter student name to remove: ').strip()
        if not name:
            print('Student name cannot be empty~')
            return
        if not self.students:
            print('Student list is empty~')
            return

        for i, s in enumerate(self.students):
            if s['name'] == name:
                del self.students[i]
                print('Student removed successfully~')
                return
        print('Cannot find the student~')

    def get_avg_scores(self):
        if self.students:# check the student list is not empty so the length of score list is not 0
            total = 0
            for s in self.students:
                scores = sum(s['scores'])
                total += scores
            avg = round(total/len(self.students), 2)
            print(f'Average total_scores of all students is: {avg}')
        else:
            print('Cant find students~')
        return
    def save_students(self):
        with open('students.txt','w', encoding = 'utf-8') as fw:
            for s in self.students:
                scores_str = ', '.join(str(score) for score in s['scores'])
                fw.write(f'{s['name']}: {scores_str}\n')
            print('Students info saved successfully~')
    def read_file(self):
        try:
            with open('students.txt','r', encoding = 'utf-8') as fr:
                self.students = []
                content = fr.read().splitlines()
                for line in content:
                    name, scores_str = line.split(':', 1)
                    scores = []
                    for score in scores_str.split(','):
                        if not score:
                            print('score cannot be empty~')
                            return
                        scores.append(int(score))
                    self.students.append({'name': name, 'scores': scores})
        except FileNotFoundError:
            print('The file cannot be found~ ')
        except Exception as e:
            print(e)
    def running_system(self):
        while True:
            print('-------Student Management System-------')

            print('''
            1.Add Student
            2.Show Students Info
            3.Search Student(by name)
            4.Delete Student
            5.Calculate Students Average Scores
            6.Save the Students Info to file
            7.load Students Info from file
            8.Exit the system
            ''')

            choice = input('Please choose the operation(1-8):')
            match choice:
                case '1':
                    self.add_student()
                case '2':
                    self.show_students()
                case '3':
                    self.find_student()
                case '4':
                    self.remove_student()
                case '5':
                    self.get_avg_scores()
                case '6':
                    self.save_students()
                case '7':
                    self.read_file()
                case '8':
                    print('Thank you, Bye~')
                    break
                case _:
                    print('Invalid choice~, please choose again')
if __name__ == '__main__':
    ManagementSystem().running_system()