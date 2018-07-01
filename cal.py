cal = {"+": lambda a, b: b + a,
       "-": lambda a, b: b - a,
       "*": lambda a, b: b * a,
       "/": lambda a, b: b / a}
kigo = ["+","-","*","/","(",")"]
num = ["0","1","2","3","4","5","6","7","8","9","."]
list_num = []
list_kigo = []
num_flag = False

def num_add(s):
    global num_flag, list_num
    num_flag = True
    list_num.append(s)

def kigo_add(s):
    global num_flag, list_kigo
    num_flag = False
    list_kigo.append(s)
def cal(input):
    try:
        s = list(input)
        for i in range(len(s)):
            if s[i] in kigo:
                if len(list_kigo) > 0:
                    if "(" in list_kigo and s[i] == ")":
                        index = [j for j, x in enumerate(list_kigo) if x == "("][-1]
                        tmp = list_kigo[index+1:]
                        del list_kigo[index:]
                        list_num += tmp[::-1]
                        num_flag = False
                    elif list_kigo[-1] in ["*","/"] and s[i] != "(":
                        num_add(list_kigo.pop())
                        kigo_add(s[i])
                    else:
                        kigo_add(s[i])
                else:
                    kigo_add(s[i])

            elif s[i] in num:
                if num_flag:
                    num_add(list_num.pop() + s[i])
                else:
                    num_add(s[i])
                    
        list_num += list_kigo[::-1]
        del list_kigo[:]

        ans = []
        for s in list_num:
            if s in cal:
                ans.append(cal[s](ans.pop(), ans.pop()))
            else:
                ans.append(float(s))
        return ans[0]

    except:
        return "err"
        input()