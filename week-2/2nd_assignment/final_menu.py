from datetime import date
class menu_start:
    def finals(self):
        print('option details:\n1.enter the name:\n2.enter the salary\n3.enter the date of birth\n4.exit')
        self.choice=int(input('enter the choice:'))
        return self.choice
    def final_menus(self):
        while True:
            option=self.finals()
            if option==1:
                from details import st_name
                st_name()
            elif option==2:
                from details import st_salary
                st_salary()
            elif option==3:
                from details import st_date
                st_date()
            elif option==4:
                exit(0)
if __name__=='__main__':
    em=menu_start()
    em.final_menus()
