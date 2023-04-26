from datetime import date
from classes import car,abcd,age
from emp_detail import Employee
from instance_var import InstDtls,empolyee

def classes_and_object():
    cr=car()
    cr.speed=20
    cr.light=30
    cr.print_car()
    cr.speed_up()
    cr.turn_on_light()
    cr.turn_off_light()

    self = 10
    #print(self)

    cr1 = car()

    cr1.speed = 55
    cr1.light = 56
    cr1.print_car()

    cr1.turn_off_light()

    #abc1 = abc()  # object
def classes_abc_construction():
    ob1=abcd(10,20,30)
    ob1.print_abc()

def age_calculator():
    ac =age()
    print(ac.age_cal(date(1999,9,24)))

def emp():
    e=Employee('abc',35)
    e.info()
def cls_inst_dtls():
    dtl1 = InstDtls('inst1')

    dtl2 = InstDtls('inst2')

    dtl3 = InstDtls('inst3')

    print('Before Setting CLS')
    print(dtl1.cls_prop, ',', dtl2.cls_prop, ',', dtl3.cls_prop)
    print('After Setting CLS')

    dtl1.cls_prop = 'cls1'
    #InstDtls.cls_prop = 'cls1'

    print(dtl1.cls_prop, ',', dtl2.cls_prop, ',', dtl3.cls_prop)
    print('----------------------------')
    print('Before Setting INST')
    print(dtl1.inst_prop, ',', dtl2.inst_prop, ',', dtl3.inst_prop)
    print('After Setting INST')
    dtl1.inst_prop = 'inst11'
    print(dtl1.inst_prop, ',', dtl2.inst_prop, ',', dtl3.inst_prop)

def empl():
    em=empolyee(456)
    em.abc=123
    em.bc='ji'
    empolyee.avy=122
    print(em.abc,em.bc)



if __name__ == '__main__':
    classes_abc_construction()
    classes_and_object()
    age_calculator()
    emp()
    cls_inst_dtls()
    empl()
    

