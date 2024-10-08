class P:
    def skills(self):
        print("fullstack, communication,fresher")
   
    def hire(self):
        print("we can hire him ")
 
class C(P):
    def hire(self):
        print("we will get back to you")
 
        print("we can hire experince person ")
 
c = C()
c.skills()
c.hire()
