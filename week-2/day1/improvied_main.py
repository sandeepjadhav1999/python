from inheritance import badageexception
class improviedmain:
    def inheritance(self):
        age=int(input('enter the age'))
        if age>85:
            ex=badageexception('age must be less than 85')
            ex.abc()
            ex.with_traceback(None)
            raise ex
if __name__=='__main__':
    im=improviedmain()
    im.inheritance()