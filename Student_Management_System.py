class student:
    def __init__(self,name,student_id):
        self.name=name 
        self.student_id=student_id
        self.grades={"Chinese":0,"Math":0,"English":0}
    
    def set_grade(self,course,grade):
        if course in self.grades:
            self.grades[course]=grade
    
    def print_grade(self):
        print(f"student {self.name} (studetn_id{self.student_id})'s grades: ")
        for course in self.grades:
            print(f"{course}:{self.grades[course]}")

def student_setting(na=input("name:"),id=input("id:"),cg=input("cg:"),mg=input("mg:"),eg=input("eg:")):
    ST=student(na,id)
    ST.set_grade("Chinese",cg)
    ST.set_grade("Math",mg)
    ST.set_grade("English",eg)
    ST.print_grade()

if __name__=="__main__":
    student_setting()