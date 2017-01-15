

dict = { '#': (-1,-1) , '(': (0,100), '*': (4,3), '/': (4,3), '+': (2,1), '-': (2,1), ')': (99,0), }
oper_stack = []
num_stack = []

def series_generate(self):
    try:
        self.series=["#"]
        if len(self.currentnum)==0:
            return
        number=''
        for i in self.currentnum:
            if (i>='0' and i<='9') or i=='.':
                number+=i
            else:
                if len(number)>0:
                    self.series.append(float(number))
                self.series.append(i)
                number=''
        if len(number)>0:
            self.series.append(float(number))
        self.series.append("#")
        selfcurrentnum=''
    except:
        self.series=["#"]
        self.currentnum=''
        self.Abs="error3"
        self.Abs_flag=True
        self.update_screen()


def calculate(self):
    series_generate(self)
    if len(self.currentnum)==0:
        return
    #test code
    print(self.series)
    ###
    try:
        for i in self.series:
            flag = False
            if isinstance(i, str)==False:
                num_stack.append(i)
                continue
            while flag==False:
                if len(oper_stack)==0 or dict[i][1]>dict[oper_stack[-1]][0]:
                    oper_stack.append(i)
                    flag = True
                elif dict[i][1]==dict[oper_stack[-1]][0]:
                    oper_stack.pop()
                    flag = True
                else:
                    operator = oper_stack.pop()
                    num2 = num_stack.pop()
                    num1 = num_stack.pop()
                    if operator=='+':
                        num_stack.append(num1+num2)
                    elif operator=='-':
                        num_stack.append(num1-num2)
                    elif operator=='*':
                        num_stack.append(num1*num2)
                    elif operator=='/':
                        num_stack.append(num1/num2)
    except:
        self.series=["#"]
        self.currentnum=''
        self.Abs="error1"
        self.Abs_flag=True
        self.update_screen()

    if len(oper_stack)!=0 or len(num_stack)!=1:
        oper_stack.clear()
        num_stack.clear()
        self.series=["#"]
        self.currentnum=''
        self.Abs="error2"
        self.Abs_flag=True
        self.update_screen()
    else:
        self.Abs = num_stack[-1]
        #float to int if necessary
        if self.Abs%1<0.0000001:
            self.Abs=int(self.Abs)
        #test code
        print(self.Abs)
        ###
        self.Abs_flag=True
        self.update_screen()
        num_stack.clear()
        self.series=['#']
        self.currentnum=''

