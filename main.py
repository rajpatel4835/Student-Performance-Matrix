from re import I
import pandas as pd
import math
import smtplib
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import SGDRegressor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from pandas import read_excel

f=read_excel("data.xlsx")

def sendmail():
    k=list(f["gmail"])
    p=",".join(k[1:])
    sender_email = k[0]
    receiver_email = p
    password = '12345678'
    message = "Dear Parents, Your Child marks has been uploaded"

    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email.split(","), message)
    print("MAIL SENT\n")
    server.close()

def draw1(roll , sem):
    e=[]
    e1=[]
    for i in range((sem-1)*10+1,(sem*10)+1):

        sub='Subject '+str(i) +' Semester Marks'
        sub2='Subject '+str(i) +' Internal Marks'
        sub1='Subject '+str(i) +' '
        if math.isnan(data.loc[data['Roll No']==roll][sub]):
            continue
        t=(data.loc[data['Roll No']==roll]['Subject '+str(i)+' ']).to_numpy()
        e1.append(str(t[0]))
        e.append(((data.loc[data['Roll No']==roll][sub]).mean())+((data.loc[data['Roll No']==roll][sub2]).mean()))
    df=pd.DataFrame([e],columns=e1)
    ax=df.plot(kind='bar',title=str(roll)+' SEMESTER'+str(sem)+' MARKS ANALYSIS',width=0.2)
    ax.set_xlabel("")
    ax.set_ylabel("Marks")
    ax.set_xticklabels([])
    h1=[ i for i in range(0,151,5) ]
    ax.set_yticks(h1)
    h=[ str(i) for i in range(0,151,5) ]
    ax.set_yticklabels(h)
    for container in ax.containers:
        ax.bar_label(container)

def draw5(roll , sem):
    e=[]
    e1=[]
    e2=[]
    e3=[]
    for i in range((sem-1)*10+1,(sem*10)+1):
        sub='Subject '+str(i) +' Semester Marks'
        sub2='Subject '+str(i) +' Internal Marks'
        sub1='Subject '+str(i) +' '
        if math.isnan(data.loc[data['Roll No']==roll][sub]):
            continue
        t=(data.loc[data['Roll No']==roll]['Subject '+str(i)+' ']).to_numpy()
        e.append(str(t[0]))
        e1.append(((data.loc[data['Roll No']==roll][sub]).mean())+int((data.loc[data['Roll No']==roll][sub2]).mean()))
        e2.append(((data.loc[((data['Roll No'])//100)==roll//100][sub]).mean())+int((data.loc[((data['Roll No'])//100)==roll//100][sub2]).mean()))
        e3.append(((data.loc[((data['Roll No'])//100)==roll//100][sub]).max())+int((data.loc[((data['Roll No'])//100)==roll//100][sub2]).max()))
    x=np.arange(10)
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - .2, e1, width=0.1, label='you_ward\'s_marks')
    rects2 = ax.bar(x  , e2, width=0.1, label='class_average')
    rects3 = ax.bar(x +.2, e3, width=0.1, label='highest_in_class')
    ax.set_ylabel('MARKS')
    ax.set_title(str(roll)+' SEMESTER '+str(sem)+' MARKS COMPARISON')
    ax.set_xlabel('SUBJECT')
    ax.set_xticks(x, e,rotation=45)
    ax.legend()
    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)
    ax.bar_label(rects3, padding=3)
    fig.tight_layout()
    plt.show()
        
def getIndexes(dfObj, value):
    listOfPos = []
    result = dfObj.isin([value])
    seriesObj = result.any()
    columnNames = list(seriesObj[seriesObj == True].index)
    for col in columnNames:
        rows = list(result[col][result[col] == True].index)
        for row in rows:
            listOfPos.append((row, col))
    return listOfPos

def draw2(roll , sem , sub):
    e=[]
    e1=['CT1 MARKS' , 'CT2 MARKS' , 'TA' , 'INTERNAL MARKS' , 'END SEM MARKS']
    ar=getIndexes(data,sub)
    #print(ar)
    for i in ar:
        if data.loc[i[0]]['Roll No'].mean()==roll:
            e.append(data.loc[i[0]][i[1]+'CT1 Marks'].mean())
            e.append(data.loc[i[0]][i[1]+'CT2 Marks'].mean())
            e.append(data.loc[i[0]][i[1]+'TA'].mean())
            e.append(data.loc[i[0]][i[1]+'Internal Marks'].mean())
            e.append(data.loc[i[0]][i[1]+'Semester Marks'].mean())
    df=pd.DataFrame([e],columns=e1)
    ax=df.plot(kind='bar',title=str(roll)+ ' '+sub+' MARKS ANALYSIS',width=0.2)
    ax.set_xlabel("")
    ax.set_ylabel("Marks")
    ax.set_xticklabels([])
    h1=[ i for i in range(0,101,5) ]
    ax.set_yticks(h1)
    h=[ str(i) for i in range(0,101,5) ]
    ax.set_yticklabels(h)
    for container in ax.containers:
        ax.bar_label(container)

def draw6(roll , sem , sub):
    e1=[]
    e2=[]
    e3=[]
    ar=getIndexes(data,sub)
    #print(ar)
    for i in ar:
        if data.loc[i[0]]['Roll No'].mean()==roll:
            e1.append(data.loc[i[0]][i[1]+'CT1 Marks'].mean())
            e2.append(data.loc[:][i[1]+'CT1 Marks'].mean())
            e3.append(data.loc[:][i[1]+'CT1 Marks'].max())
            e1.append(data.loc[i[0]][i[1]+'CT2 Marks'].mean())
            e2.append(data.loc[:][i[1]+'CT2 Marks'].mean())
            e3.append(data.loc[:][i[1]+'CT2 Marks'].max())
            e1.append(data.loc[i[0]][i[1]+'TA'].mean())
            e2.append(data.loc[:][i[1]+'TA'].mean())
            e3.append(data.loc[:][i[1]+'TA'].max())
            e1.append(data.loc[i[0]][i[1]+'Internal Marks'].mean())
            e2.append(data.loc[:][i[1]+'Internal Marks'].mean())
            e3.append(data.loc[:][i[1]+'Internal Marks'].max())
            e1.append(data.loc[i[0]][i[1]+'Semester Marks'].mean())
            e2.append(data.loc[:][i[1]+'Semester Marks'].mean())
            e3.append(data.loc[:][i[1]+'Semester Marks'].max())
    x=np.arange(5)
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - .2, e1, width=0.1, label='you_ward\'s_marks')
    rects2 = ax.bar(x  , e2, width=0.1, label='class_average')
    rects3 = ax.bar(x +.2, e3, width=0.1, label='highest_in_class')
    ax.set_ylabel('MARKS')
    ax.set_title(str(roll)+' '+sub+' MARKS COMPARISON')
    ax.set_xlabel('EXAM NAME')
    ax.set_xticks(x, ['CT1 MARKS' , 'CT2 MARKS' , 'TA' , 'INTERNAL MARKS' , 'END SEM MARKS'])
    ax.legend()
    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)
    ax.bar_label(rects3, padding=3)
    fig.tight_layout()

def draw3(roll , id , sem):
    e=[]
    e1=[]
    for i in range((sem-1)*10+1,(sem*10)+1):
        sub='Subject '+str(i) +' '+id
        if id=='TA Marks':
            sub=sub[0:-6]
        sub1='Subject '+str(i) +' '
        if math.isnan((data.loc[data['Roll No']==roll][sub])):
            continue
        t=(data.loc[data['Roll No']==roll]['Subject '+str(i)+' ']).to_numpy()
        e1.append(str(t[0]))
        e.append(((data.loc[data['Roll No']==roll][sub]).mean()))
    t2=(data.loc[data['Roll No']==roll][sub]).to_numpy()
    j1=100
    if id[0]=='C' and id[1]=='T':
        j1=30
    elif id[0]=='T' and id[1]=='A':
        j1=20
    elif id=='Internal Marks':
        j1=50
    else:
        j1=100
    df=pd.DataFrame([e],columns=e1)
    t=(data.loc[data['Roll No']==roll]['Subject '+str(i)+' ']).to_numpy()
    ax=df.plot(kind='bar',title=str(roll)+' SEMESTER'+str(sem)+' '+id[0:-5]+' marks analysis',width=0.2)
    ax.set_xlabel("")
    ax.set_ylabel("Marks")
    ax.set_xticklabels([])
    h1=[ i for i in range(0,j1+1,5) ]
    ax.set_yticks(h1)
    h=[ str(i) for i in range(0,j1+1,5) ]
    ax.set_yticklabels(h)
    for container in ax.containers:
        ax.bar_label(container)

def draw4(roll):
    e=[]
    e1=['SEMESTER 1 TOTAL','SEMESTER 2 TOTAL','SEMESTER 3 TOTAL','SEMESTER 4 TOTAL','SEMESTER 5 TOTAL','SEMESTER 6 TOTAL','SEMESTER 7 TOTAL','SEMESTER 8 TOTAL']
    for i in range(1,9):
        if math.isnan((data.loc[data['Roll No']==roll]['Semester '+str(i)+' Total'])):
            e.append(0)
            continue
        e.append(((data.loc[data['Roll No']==roll]['Semester '+str(i)+' Total']).mean()))
    df=pd.DataFrame([e],columns=e1)
    ax=df.plot(kind='bar',title=str(roll)+' SEMESTER ANALYSIS',width=0.2)
    ax.set_xlabel("")
    ax.set_ylabel("Marks")
    ax.set_xticklabels([])
    h1=[ i for i in range(0,1000,50) ]
    ax.set_yticks(h1)
    h=[ str(i) for i in range(0,1000,50) ]
    ax.set_yticklabels(h)
    for container in ax.containers:
        ax.bar_label(container)

def draw7(roll , id, sem):
    e=[]
    e1=[]
    e2=[]
    e3=[]
    for i in range((sem-1)*10+1,(sem*10)+1):
        sub='Subject '+str(i) +' '+id
        if id=='TA Marks':
            sub=sub[0:-6]
        t=(data.loc[data['Roll No']==roll]['Subject '+str(i)+' ']).to_numpy()
        e.append(str(t[0]))
        e1.append(((data.loc[data['Roll No']==roll][sub]).mean()))
        e2.append(((data.loc[data['Roll No']//100==roll//100][sub]).mean()))
        e3.append(((data.loc[data['Roll No']//100==roll//100][sub]).max()))
    x=np.arange(10)
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - .2, e1, width=0.1, label='you_ward\'s_marks')
    rects2 = ax.bar(x  , e2, width=0.1, label='class_average')
    rects3 = ax.bar(x +.2, e3, width=0.1, label='highest_in_class')
    ax.set_ylabel('MARKS')
    ax.set_title(str(roll)+' '+id+ ' COMPARISON')
    ax.set_xlabel('SUBJECT')
    ax.set_xticks(x, e,rotation=45)
    ax.legend()
    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)
    ax.bar_label(rects3, padding=3)
    fig.tight_layout()

def draw8(roll):
    e1=[]
    e2=[]
    e3=[]
    e=['SEMESTER 1 TOTAL','SEMESTER 2 TOTAL','SEMESTER 3 TOTAL','SEMESTER 4 TOTAL','SEMESTER 5 TOTAL','SEMESTER 6 TOTAL','SEMESTER 7 TOTAL','SEMESTER 8 TOTAL']
    for i in range(1,9):
        if math.isnan((data.loc[data['Roll No']==roll]['Semester '+str(i)+' Total']).mean()):
            e1.append(0)
            e2.append(0)
            e3.append(0)
            continue
        e1.append(((data.loc[data['Roll No']==roll]['Semester '+str(i)+' Total']).mean()))
        e2.append(((data.loc[data['Roll No']//100==roll//100]['Semester '+str(i)+' Total']).mean()))
        e3.append(((data.loc[data['Roll No']//100==roll//100]['Semester '+str(i)+' Total']).max()))
    x=np.arange(8)
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - .2, e1, width=0.1, label='you_ward\'s_marks')
    rects2 = ax.bar(x  , e2, width=0.1, label='class_average')
    rects3 = ax.bar(x +.2, e3, width=0.1, label='highest_in_class')
    ax.set_ylabel('MARKS')
    ax.set_title(str(roll)+' TOTAL SEMESTER MARKS COMPARISON')
    ax.set_xlabel('SEMESTER NO.')
    ax.set_xticks(x, e,rotation=45)
    ax.legend()
    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)
    ax.bar_label(rects3, padding=3)
    fig.tight_layout()


def testpas(m,n):
  if n!=list(f.loc[(f["userid"]==m),"password"]):
    if (encrypt(n)).split()==list(f.loc[(f["userid"]==m),"password"]):
       return True
    else:
       return False

def testid(m):
    if m in list(f["userid"]):
      return True
    else:
      return False

def encrypt(n):
    dict={
     "a":"^","b":">","c":"<","d":".","e":",","f":"~","g":"*","h":"19","i":"18","j":"17","k":"16","l":"15",
     "m":"14","n":"13","o":"12","p":"11","q":"10","r":"9","s":"8","t":"7","u":"6","v":"5","w":"4","x":"3","y":"2",
     "z":"1","1":"@","2":'#',"3":"$","4":"_","6":"-","8":"(","9":")",
     "0":"/"
}
    b=list(n)
    for i in b:
       if i in dict:
          b[b.index(i)]=dict[i]
    z="".join(b)
    return z

def passreset(m,n=None):
    print("ENTER NEW PASSWORS")
    j=encrypt(input(""))

    f.loc[(f["userid"]==m),"password"]=j
    f.to_csv("data.csv",index=False)
    print("PASSWORS HAS BEEN RESET\n")

while True:
    print("\nFOR ADMIN LOGIN, PRESS 1\nFOR PARENTS LOGIN, PRESS 2\nFOR PASSWORD RESET, PRESS 3")
    a=int(input())
    if a==1:
      t=0
      while True:
            if t==1:
               break
            print("ENTER ADMIN USER ID")
            a=input("")
            print("ENTER ADMIN PASSWORD")
            b=input("")
            if (testpas(a,b) and testid(a)):
             while True:
               print("FOR SENDING MAIL TO PARENTS THAT STUDENTS MARKS HAS BEEN UPADATED, PRESS 3")
               print("FOR EXIT, PRESS 0")
               print("FOR PASSWORD RESET OF STUDENT'S PARENTS, PRESS 2")
               print("FOR STUDENT PERFORMANCE MATRIX, PRESS 5")
               b=int(input())
               if b==3:
                  sendmail()
               elif b==0:
                  t=1
                  break
               elif b==5:
                    data=pd.read_csv("DATASET.csv")
                    d1=pd.read_csv("attendance.csv",encoding='latin1')
                    print('\nWELCOME SUPERUSER\n')
                    while(1):
                        print("\nANALYSIS AND COMPARISON MENU\n")
                        print("\n1. ANALYSIS MENU\n")
                        print("\n2. COMPARISON MENU\n")
                        print("\n3. SEE ATTENDANCE IN A PARTICULAR SUBJECT\n")
                        print("\n4. SEE FACULTY\'S REMARKS IN A PERTICULAR SUBJECT\n")
                        print("\n5. SEE EXPECTATION OF NEXT SEMESTER\n")
                        print("\n6. COMPARE STUDENTS\n")
                        print("\n7. EXIT\n")
                        c=int(input("ENTER YOUR CHOICE: "))
                        if c==1:
                            while(1):
                                print('\nANALYSIS MENU\n')
                                roll=int(input("ENTER THE ROLL NO\n"))
                                if not(roll in data['Roll No'].unique()):
                                    print('ROLL NO INVALID PLEASE TRY AGAIN')
                                    continue
                                else:
                                    break
                            while(1):
                                print("\n1. ANALYSE A PARTICULAR SEMESTER\n")
                                print("\n2. ANALYSE A PARTICULAR SUBJECT\n")
                                print("\n3. ANALYSE A PARTICULAR SEMESTER\'S PARTICULAR EXAM\n")
                                print("\n4. INTER SEMESTER ANALYSIS\n")
                                print("\n5. RETURN TO PREVIOUS MENU\n")
                                c1=int(input("ENTER YOUR CHOICE: "))
                                if c1==1:
                                    
                                    while(1):
                                        sem=int(input("ENTER THE SEMESTER TO ANALYSE: "))
                                        if not (sem in range(1,9,1)):
                                            print('INVALID SEMESTER NO. PLEASE TRY AGAIN\n')
                                            continue
                                        else:
                                            break
                                    draw1(roll,sem)
                                    plt.show()
                                elif c1==2:
                                    while(1):
                                        sem=int(input("ENTER THE SEMESTER TO ANALYSE: "))
                                        if not (sem in range(1,9,1)):
                                            print('INVALID SEMESTER NO. PLEASE TRY AGAIN\n')
                                            continue
                                        else:
                                            break
                                    fs=[col for col in data if col.startswith('Subject') and col.endswith(' ')]
                                    a=np.array([])
                                    for i in fs:
                                        if pd.isna(data[i].unique()):
                                            pass
                                        else:
                                            a=np.append(a,str(data[i].unique()))
                                    rs=np.unique(a)
                                    for i in rs:
                                        print(i)
                                    sub=input("ENTER THE SUBJECT TO ANALYSE (from above note::CASE-SENSITIVE FAILURE WILL RESULT IN ERROR): ")
                                    draw2(roll,sem,sub)
                                    plt.show()
                                elif c1==3:
                                    while(1):
                                        sem=int(input("ENTER THE SEMESTER TO ANALYSE: "))
                                        if not (sem in range(1,9,1)):
                                            print('INVALID SEMESTER NO. PLEASE TRY AGAIN\n')
                                            continue
                                        else:
                                            break
                                    print("\n1. CT1")
                                    print("\n2. CT2")
                                    print("\n3. TA")
                                    print("\n4. INTERNAL")
                                    print("\n5. END SEM")
                                    c3=int(input("ENTER YOUR CHOICE: "))
                                    if c3==1:
                                        draw3(roll,'CT1 Marks',sem)
                                        plt.show()
                                    elif c3==2:
                                        draw3(roll,'CT2 Marks',sem)
                                        plt.show()
                                    elif c3==3:
                                        draw3(roll,'TA Marks',sem)
                                        plt.show()
                                    elif c3==4:
                                        draw3(roll,'Internal Marks',sem)
                                        plt.show()
                                    elif c3==5:
                                        draw3(roll,'Semester Marks',sem)
                                        plt.show()
                                    else:
                                        print("\nWRONG CHOICE\n")
                                elif c1==4:
                                    draw4(roll)
                                    plt.show()
                                elif c1==5:
                                    break
                                else:
                                    print("\nPLEASE ENTER A VALID CHOICE\n")
                        elif c==2:
                            while(1):
                                print('\nCOMPARISON MENU\n')
                                roll=int(input("ENTER THE ROLL NO\n"))
                                if not(roll in data['Roll No'].unique()):
                                    print('ROLL NO INVALID PLEASE TRY AGAIN')
                                    continue
                                else:
                                    break
                            while(1):
                                print("\n1. COMPARISON IN A PARTICULAR SEMESTER\n")
                                print("\n2. COMPARISON IN A PARTICULAR SUBJECT\n")
                                print("\n3. COMPARISON IN A PARTICULAR SEMESTER\'S PARTICULAR EXAM\n")
                                print("\n4. INTER SEMESTER COMPARISON\n")
                                print("\n5. RETURN TO PREVIOUS MENU\n")
                                c2=int(input("ENTER YOUR CHOICE: "))
                                if c2==1:
                                    while(1):
                                        sem=int(input("ENTER THE SEMESTER TO ANALYSE: "))
                                        if not (sem in range(1,9,1)):
                                            print('INVALID SEMESTER NO. PLEASE TRY AGAIN\n')
                                            continue
                                        else:
                                            break
                                    draw5(roll,sem)
                                    plt.show()
                                elif c2==2:
                                    while(1):
                                        sem=int(input("ENTER THE SEMESTER TO ANALYSE: "))
                                        if not (sem in range(1,9,1)):
                                            print('INVALID SEMESTER NO. PLEASE TRY AGAIN\n')
                                            continue
                                        else:
                                            break
                                    fs=[col for col in data if col.startswith('Subject') and col.endswith(' ')]
                                    a=np.array([])
                                    for i in fs:
                                        if pd.isna(data[i].unique()):
                                            pass
                                        else:
                                            a=np.append(a,str(data[i].unique()))
                                    rs=np.unique(a)
                                    for i in rs:
                                        print(i)
                                    sub=input("ENTER THE SUBJECT TO COMPARE (from above note::CASE-SENSITIVE FAILURE WILL RESULT IN ERROR): ")
                                    draw6(roll,sem,sub)
                                    plt.show()
                                elif c2==3:
                                    while(1):
                                        sem=int(input("ENTER THE SEMESTER TO ANALYSE: "))
                                        if not (sem in range(1,9,1)):
                                            print('INVALID SEMESTER NO. PLEASE TRY AGAIN\n')
                                            continue
                                        else:
                                            break
                                    print("\n1. CT1")
                                    print("\n2. CT2")
                                    print("\n3. TA")
                                    print("\n4. INTERNAL")
                                    print("\n5. END SEM")
                                    c3=int(input("ENTER YOUR CHOICE: "))
                                    if c3==1:
                                        draw7(roll,'CT1 Marks',sem)
                                        plt.show()
                                    elif c3==2:
                                        draw7(roll,'CT2 Marks',sem)
                                        plt.show()
                                    elif c3==3:
                                        draw7(roll,'TA Marks',sem)
                                        plt.show()
                                    elif c3==4:
                                        draw7(roll,'Internal Marks',sem)
                                        plt.show()
                                    elif c3==5:
                                        draw7(roll,'Semester Marks',sem)
                                        plt.show()
                                    else:
                                        print("\nWRONG CHOICE\n")
                                        plt.show()
                                elif c2==4:
                                    draw8(roll)
                                    plt.show()
                                elif c2==5:
                                    break
                                else:
                                    print("\nPLEASE ENTER A VALID CHOICE\n")
                        elif c==3:
                            
                            while(1):
                                print("\nSEE ATTENDANCE IN A PARTICULAR SUBJECT\n")
                                roll=int(input("ENTER THE ROLL NO\n"))
                                if not(roll in data['Roll No'].unique()):
                                    print('ROLL NO INVALID PLEASE TRY AGAIN')
                                    continue
                                else:
                                    break
                            fs=[col for col in data if col.startswith('Subject') and col.endswith(' ')]
                            a=np.array([])
                            for i in fs:
                                if pd.isna(data[i].unique()):
                                    pass
                                else:
                                    a=np.append(a,str(data[i].unique()))
                            rs=np.unique(a)
                            for i in rs:
                                print(i)
                            sub=input("ENTER THE SUBJECT TO SEE ATTENDANCE (from above note::CASE-SENSITIVE FAILURE WILL RESULT IN ERROR): ")
                            print(d1.loc[data['Roll No']==roll][sub].mean(),end=" ")
                            print("out of ",end='')
                            print(d1.loc[data['Roll No']==roll][sub+' MAX'].mean())
                        elif c==4:
                            while(1):
                                print("\nSEE FACULTY REMARKS IN A PARTICULAR SUBJECT\n")
                                roll=int(input("ENTER THE ROLL NO\n"))
                                if not(roll in data['Roll No'].unique()):
                                    print('ROLL NO INVALID PLEASE TRY AGAIN')
                                    continue
                                else:
                                    break
                            fs=[col for col in data if col.startswith('Subject') and col.endswith(' ')]
                            a=np.array([])
                            for i in fs:
                                if pd.isna(data[i].unique()):
                                    pass
                                else:
                                    a=np.append(a,str(data[i].unique()))
                            rs=np.unique(a)
                            for i in rs:
                                print(i)
                            sub=input("ENTER THE SUBJECT TO SEE FACULTY\'S REMARKS (from above note::CASE-SENSITIVE FAILURE WILL RESULT IN ERROR): ")
                            ar=getIndexes(data,sub)
                            for i in ar:
                                if data.loc[i[0]]['Roll No'].mean()==roll:
                                    print(data.loc[data['Roll No']==roll][i[1]+'Faculty Remarks'].to_numpy())
                        elif c==5:
                            while(1):
                                print("\nEXPECTATION OF NEXT SEMESTER\n")
                                roll=int(input("ENTER THE ROLL NO\n"))
                                if not(roll in data['Roll No'].unique()):
                                    print('ROLL NO INVALID PLEASE TRY AGAIN')
                                    continue
                                else:
                                    break
                            print("\nWE CAN PREDICT ONLY IF MARKS OF BOTH CT OF THIS SEMESTER ARE PRESENT IN OUR RECORDS AND RESULT OF ATLEAST TWO SEMESTERS IS DECLARED\n")
                            
                            e=[]
                            e1=[]
                            e2=[]
                            l=0
                            for i in range(1,9):
                                if math.isnan((data.loc[data['Roll No']==roll]['Semester '+str(i)+' Total'])):
                                    continue
                                if(math.isnan(data.loc[data['Roll No']==roll]['Subject '+str((l)*10+1)+' CT1 Marks'])):
                                    continue
                                id1='CT1 Marks'
                                id2='CT2 Marks'
                                e.append(((data.loc[data['Roll No']==roll]['Semester '+str(i)+' Total']).mean()))
                                u=0
                                p=0
                                for j in range((i-1)*10+1,(i*10)+1):
                                    sub='Subject '+str(j) +' '+id1
                                    sub2='Subject '+str(j) +' '+id2
                                    if math.isnan((data.loc[data['Roll No']==roll][sub])):
                                        continue
                                    u=u+(data.loc[data['Roll No']==roll][sub].mean())+(data.loc[data['Roll No']==roll][sub2].mean())
                                    p+=1
                                e3=[]
                                e3.append(u/(p*60)*100)
                                e1.append(u/(p*60)*100)
                                e2.append(((data.loc[data['Roll No']==roll]['Semester '+str(i)+' Total Max Marks']).mean()))
                                l=i
                            k=[]
                            
                            for i,j in zip(e,e2):
                                k1=[]
                                k1.append((i/j)*100)
                                k.append(k1)
                            reg = make_pipeline(StandardScaler(),SGDRegressor(max_iter=2222, tol=1e-3))
                            reg.fit(k,e1)
                            u=0
                            for j in range((l)*10+1,((l+1)*10)+1):
                                sub='Subject '+str(j) +' '+id1
                                sub2='Subject '+str(j) +' '+id2
                                if math.isnan((data.loc[data['Roll No']==roll][sub])):
                                    continue
                                u=u+(data.loc[data['Roll No']==roll][sub].mean())+(data.loc[data['Roll No']==roll][sub2].mean())
                            if(math.isnan(data.loc[data['Roll No']==roll]['Subject '+str((l)*10+1)+' CT1 Marks']) or l<2):
                                print("\nCANNOT PREDICT\n")
                                continue
                            print("\nIN NEXT SEMESTER THIS STUDENT SHOULD GET THESE MARKS (IN OVERALL PERCENTAGE): \n")
                            r=[]
                            r1=[]
                            r.append(u/0.6)
                            r1.append(r)
                            print(reg.predict(r1))
                        elif c==6:
                            while(1):
                                print("\nCOMPARE STUDENTS\n")
                                print('ENTER ROLL NUMBERS TO COMPARE: (SEPARATED BY SPACES) \n')
                                input_string = input()
                                rl = input_string.split()
                                for i in range(len(rl)):
                                    rl[i] = int(rl[i])
                                flag=0
                                for i in rl:
                                    if not(i in data['Roll No'].unique()):
                                        print('ROLL NO INVALID PLEASE TRY AGAIN')
                                        flag=1
                                        break
                                if flag==1:
                                    continue
                                else:
                                    break

                            while(1):
                                print("\n1. COMPARISON A PARTICULAR SEMESTER\n")
                                print("\n2. COMPARISON A PARTICULAR SUBJECT\n")
                                print("\n3. COMPARISON A PARTICULAR SEMESTER\'S PARTICULAR EXAM\n")
                                print("\n4. INTER SEMESTER COMPARISON\n")
                                print("\n5. CLASS COMPARISON IN A PARTICULAR SEMESTER\n")
                                print("\n6. CLASS COMPARISON IN A PARTICULAR SUBJECT\n")
                                print("\n7. CLASS COMPARISON IN A PARTICULAR SEMESTER\'S PARTICULAR EXAM\n")
                                print("\n8. INTER SEMESTER CLASS COMPARISON\n")
                                print("\n9. RETURN TO PREVIOUS MENU\n")
                                c1=int(input("ENTER YOUR CHOICE: "))
                                if c1==1:
                                    while(1):
                                        sem=int(input("ENTER THE SEMESTER TO ANALYSE: "))
                                        if not (sem in range(1,9,1)):
                                            print('INVALID SEMESTER NO. PLEASE TRY AGAIN\n')
                                            continue
                                        else:
                                            break
                                    for i in rl:
                                        draw1(i,sem)
                                    plt.show()
                                elif c1==2:
                                    while(1):
                                        sem=int(input("ENTER THE SEMESTER TO ANALYSE: "))
                                        if not (sem in range(1,9,1)):
                                            print('INVALID SEMESTER NO. PLEASE TRY AGAIN\n')
                                            continue
                                        else:
                                            break
                                    fs=[col for col in data if col.startswith('Subject') and col.endswith(' ')]
                                    a=np.array([])
                                    for i in fs:
                                        if pd.isna(data[i].unique()):
                                            pass
                                        else:
                                            a=np.append(a,str(data[i].unique()))
                                    rs=np.unique(a)
                                    for i in rs:
                                        print(i)
                                    sub=input("ENTER THE SUBJECT TO COMPARE (from above note::CASE-SENSITIVE FAILURE WILL RESULT IN ERROR): ")
                                    for i in rl:
                                        draw2(i,sem,sub)
                                    plt.show()
                                elif c1==3:
                                    while(1):
                                        sem=int(input("ENTER THE SEMESTER TO ANALYSE: "))
                                        if not (sem in range(1,9,1)):
                                            print('INVALID SEMESTER NO. PLEASE TRY AGAIN\n')
                                            continue
                                        else:
                                            break
                                    print("\n1. CT1")
                                    print("\n2. CT2")
                                    print("\n3. TA")
                                    print("\n4. INTERNAL")
                                    print("\n5. END SEM")
                                    c3=int(input("ENTER YOUR CHOICE: "))
                                    if c3==1:
                                        for i in rl:
                                            draw3(i,'CT1 Marks',sem)
                                        plt.show()
                                    elif c3==2:
                                        for i in rl:
                                            draw3(i,'CT2 Marks',sem)
                                        plt.show()
                                    elif c3==3:
                                        for i in rl:
                                            draw3(i,'TA Marks',sem)
                                        plt.show()
                                    elif c3==4:
                                        for i in rl:
                                            draw3(i,'Internal Marks',sem)    
                                        plt.show()
                                    elif c3==5:
                                        for i in rl:
                                            draw3(i,'Semester Marks',sem)
                                        plt.show()
                                    else:
                                        print("\nWRONG CHOICE\n")
                                elif c1==4:
                                    for i in rl:
                                        draw4(i)    
                                    plt.show()
                                elif c1==5:
                                    while(1):
                                        sem=int(input("ENTER THE SEMESTER TO ANALYSE: "))
                                        if not (sem in range(1,9,1)):
                                            print('INVALID SEMESTER NO. PLEASE TRY AGAIN\n')
                                            continue
                                        else:
                                            break
                                    for i in rl:
                                        draw5(i,sem)
                                    plt.show()
                                elif c1==6:
                                    while(1):
                                        sem=int(input("ENTER THE SEMESTER TO ANALYSE: "))
                                        if not (sem in range(1,9,1)):
                                            print('INVALID SEMESTER NO. PLEASE TRY AGAIN\n')
                                            continue
                                        else:
                                            break
                                    fs=[col for col in data if col.startswith('Subject') and col.endswith(' ')]
                                    a=np.array([])
                                    for i in fs:
                                        if pd.isna(data[i].unique()):
                                            pass
                                        else:
                                            a=np.append(a,str(data[i].unique()))
                                    rs=np.unique(a)
                                    for i in rs:
                                        print(i)
                                    sub=input("ENTER THE SUBJECT TO COMPARE (from above note::CASE-SENSITIVE FAILURE WILL RESULT IN ERROR): ")
                                    for i in rl:
                                        draw6(i,sem,sub)
                                    plt.show()
                                elif c1==7:
                                    while(1):
                                        sem=int(input("ENTER THE SEMESTER TO ANALYSE: "))
                                        if not (sem in range(1,9,1)):
                                            print('INVALID SEMESTER NO. PLEASE TRY AGAIN\n')
                                            continue
                                        else:
                                            break
                                    print("\n1. CT1")
                                    print("\n2. CT2")
                                    print("\n3. TA")
                                    print("\n4. INTERNAL")
                                    print("\n5. END SEM")
                                    c3=int(input("ENTER YOUR CHOICE: "))
                                    if c3==1:
                                        for i in rl:
                                            draw7(i,'CT1 Marks',sem)
                                        plt.show()
                                    elif c3==2:
                                        for i in rl:
                                            draw7(i,'CT2 Marks',sem)
                                        plt.show()
                                    elif c3==3:
                                        for i in rl:
                                            draw7(i,'TA Marks',sem)
                                        plt.show()
                                    elif c3==4:
                                        for i in rl:
                                            draw7(i,'Internal Marks',sem)
                                        plt.show()
                                    elif c3==5:
                                        for i in rl:
                                            draw7(i,'Semester Marks',sem)
                                        plt.show()
                                    else:
                                        print("\nWRONG CHOICE\n")
                                elif c1==8:
                                    for i in rl:
                                        draw8(i)
                                    plt.show()
                                elif c1==9:
                                    break

                                else:
                                    print("\nPLEASE ENTER A VALID CHOICE\n")
                            
                        elif c==7:
                            break
                        else:
                            print("\nPLEASE ENTER A VALID CHOICE\n")
               elif b==2:
                  while True:
                     print("ENTER PARENT USER ID")
                     a=input("")
                     if (testid(a)):
                        passreset(a)
                        break
                     else:
                        print("INVALID PARENT USER ID")
                        print("FOR TRY AGAIN PRESS 1")
                        print("FOR EXIT PRESS 0")
                        d=int(input(""))
                        if d==0:
                           break
            elif (testpas(a,b)==False):
               print("PASSWORD IS WRONG PLZZ TRY AGAIN")
            elif (testid(a)==False):
               print("USER ID IS WRONG PLZZ TRY AGAIN")
            
    elif a==2:
       t=0
       while True:
            if t==1:
               break
            print("ENTER USER ID")
            a=input("")
            print("ENTER PASSWORD")
            b=input("")
            if (testpas(a,b) and testid(a)):
             while True:
               print("FFOR EXIT PRESS 0")
               print("FOR STUDENT PERFORMANCE MATRIX PRESS 1")
               b=int(input())
               if b==1:
                    data=pd.read_csv("DATASET.csv")
                    d1=pd.read_csv("attendance.csv",encoding='latin1')
                    roll=int(input("ENTER THE ROLL NO\n"))
                    pn=(data.loc[data['Roll No']==roll]['Father\'s Name']).to_numpy()
                    lis = list(pn[0].split(" "))
                    length = len(lis)
                    print("WELCOME MR. AND MRS. ",lis[length-1])
                    print("YOUR WARD\'S COMPLETE DATA IS: \n")
                    h=(data.loc[data['Roll No']==roll])
                    h=h.dropna(axis=1)
                    h1=h.to_dict('index')
                    for i,j in h1[next(iter(h1))].items():
                        print(i," : ",j)
                    while(1):
                        print("\nANALYSIS AND COMPARISON MENU\n")
                        print("\n1. ANALYSIS MENU\n")
                        print("\n2. COMPARISON MENU\n")
                        print("\n3. SEE ATTENDANCE IN A PARTICULAR SUBJECT\n")
                        print("\n4. SEE FACULTY\'S REMARKS IN A PERTICULAR SUBJECT\n")
                        print("\n5. SEE EXPECTATION OF NEXT SEMESTER\n")
                        print("\n6. EXIT\n")
                        c=int(input("ENTER YOUR CHOICE: "))
                        if c==1:
                            while(1):
                                print("\nANALYSIS MENU\n")
                                print("\n1. ANALYSE A PARTICULAR SEMESTER\n")
                                print("\n2. ANALYSE A PARTICULAR SUBJECT\n")
                                print("\n3. ANALYSE A PARTICULAR SEMESTER\'S PARTICULAR EXAM\n")
                                print("\n4. INTER SEMESTER ANALYSIS\n")
                                print("\n5. SEMESTER ANALYSIS IN DETAIL\n")
                                print("\n6. RETURN TO PREVIOUS MENU\n")
                                c1=int(input("ENTER YOUR CHOICE: "))
                                if c1==1:
                                    sem=int(input("ENTER THE SEMESTER TO ANALYSE: "))
                                    draw1(roll,sem)
                                    plt.show()
                                elif c1==2:
                                    sem=int(input("ENTER THE SEMESTER TO ANALYSE: "))
                                    fs=[col for col in data if col.startswith('Subject') and col.endswith(' ')]
                                    a=np.array([])
                                    for i in fs:
                                        if pd.isna(data[i].unique()):
                                            pass
                                        else:
                                            a=np.append(a,str(data[i].unique()))
                                    rs=np.unique(a)
                                    for i in rs:
                                        print(i)
                                    sub=input("ENTER THE SUBJECT TO ANALYSE (from above note::CASE-SENSITIVE): ")
                                    draw2(roll,sem,sub)
                                    plt.show()
                                elif c1==3:
                                    sem=int(input("ENTER THE SEMESTER TO ANALYSE: "))
                                    print("\n1. CT1")
                                    print("\n2. CT2")
                                    print("\n3. TA")
                                    print("\n4. INTERNAL")
                                    print("\n5. END SEM")
                                    c3=int(input("ENTER YOUR CHOICE: "))
                                    if c3==1:
                                        draw3(roll,'CT1 Marks',sem)
                                        plt.show()
                                    elif c3==2:
                                        draw3(roll,'CT2 Marks',sem)
                                        plt.show()
                                    elif c3==3:
                                        draw3(roll,'TA Marks',sem)
                                        plt.show()
                                    elif c3==4:
                                        draw3(roll,'Internal Marks',sem)
                                        plt.show()
                                    elif c3==5:
                                        draw3(roll,'Semester Marks',sem)
                                        plt.show()
                                    else:
                                        print("\nWRONG CHOICE\n")
                                elif c1==4:
                                    draw4(roll)
                                    plt.show()
                                elif c1==5:
                                    print("\n5. SEMESTER ANALYSIS IN DETAIL\n")
                                    sem=int(input("ENTER THE SEMESTER TO ANALYSE: "))
                                    draw3(roll,'CT1 Marks',sem)
                                    draw3(roll,'CT2 Marks',sem)
                                    draw3(roll,'TA Marks',sem)
                                    draw3(roll,'Internal Marks',sem)
                                    draw3(roll,'Semester Marks',sem)
                                    plt.show()
                                elif c1==6:
                                    break
                                else:
                                    print("\nPLEASE ENTER A VALID CHOICE\n")
                        elif c==2:
                            while(1):
                                print("\n1. COMPARISON IN A PARTICULAR SEMESTER\n")
                                print("\n2. COMPARISON IN A PARTICULAR SUBJECT\n")
                                print("\n3. COMPARISON IN A PARTICULAR SEMESTER\'S PARTICULAR EXAM\n")
                                print("\n4. INTER SEMESTER COMPARISON\n")
                                print("\n5. SEMESTER COMPARISON IN DETAIL\n")
                                print("\n6. RETURN TO PREVIOUS MENU\n")
                                c2=int(input("ENTER YOUR CHOICE: "))
                                if c2==1:
                                    sem=int(input("ENTER THE SEMESTER TO COMPARE: "))
                                    draw5(roll,sem)
                                    plt.show()
                                elif c2==2:
                                    sem=int(input("ENTER THE SEMESTER TO COMPARE: "))
                                    fs=[col for col in data if col.startswith('Subject') and col.endswith(' ')]
                                    a=np.array([])
                                    for i in fs:
                                        if pd.isna(data[i].unique()):
                                            pass
                                        else:
                                            a=np.append(a,str(data[i].unique()))
                                    rs=np.unique(a)
                                    for i in rs:
                                        print(i)
                                    sub=input("ENTER THE SUBJECT TO COMPARE (from above note::CASE-SENSITIVE): ")
                                    draw6(roll,sem,sub)
                                    plt.show()
                                elif c2==3:
                                    sem=int(input("ENTER THE SEMESTER TO ANALYSE: "))
                                    print("\n1. CT1")
                                    print("\n2. CT2")
                                    print("\n3. TA")
                                    print("\n4. INTERNAL")
                                    print("\n5. END SEM")
                                    c3=int(input("ENTER YOUR CHOICE: "))
                                    if c3==1:
                                        draw7(roll,'CT1 Marks',sem)
                                        plt.show()
                                    elif c3==2:
                                        draw7(roll,'CT2 Marks',sem)
                                        plt.show()
                                    elif c3==3:
                                        draw7(roll,'TA Marks',sem)
                                        plt.show()
                                    elif c3==4:
                                        draw7(roll,'Internal Marks',sem)
                                        plt.show()
                                    elif c3==5:
                                        draw7(roll,'Semester Marks',sem)
                                        plt.show()
                                    else:
                                        print("\nWRONG CHOICE\n")
                                elif c2==4:
                                    draw8(roll)
                                    plt.show()
                                elif c2==5:
                                    print("\n5. SEMESTER ANALYSIS IN DETAIL\n")
                                    sem=int(input("ENTER THE SEMESTER TO ANALYSE: "))
                                    draw7(roll,'CT1 Marks',sem)
                                    draw7(roll,'CT2 Marks',sem)
                                    draw7(roll,'TA Marks',sem)
                                    draw7(roll,'Internal Marks',sem)
                                    draw7(roll,'Semester Marks',sem)
                                    plt.show()
                                elif c2==6:
                                    break
                                else:
                                    print("\nPLEASE ENTER A VALID CHOICE\n")
                        elif c==3:
                            print("\n3. SEE ATTENDANCE IN A PARTICULAR SUBJECT\n")
                            fs=[col for col in data if col.startswith('Subject') and col.endswith(' ')]
                            a=np.array([])
                            for i in fs:
                                if pd.isna(data[i].unique()):
                                    pass
                                else:
                                    a=np.append(a,str(data[i].unique()))
                            rs=np.unique(a)
                            for i in rs:
                                print(i)
                            sub=input("ENTER THE SUBJECT TO SEE ATTENDANCE (from above note::CASE-SENSITIVE): ")
                            print(d1.loc[data['Roll No']==roll][sub].mean(),end=" ")
                            print("out of ",end='')
                            print(d1.loc[data['Roll No']==roll][sub+' MAX'].mean())
                        elif c==4:
                            print("\n4. SEE FACULTY\'S REMARKS IN A PERTICULAR SUBJECT\n")
                            fs=[col for col in data if col.startswith('Subject') and col.endswith(' ')]
                            a=np.array([])
                            for i in fs:
                                if pd.isna(data[i].unique()):
                                    pass
                                else:
                                    a=np.append(a,str(data[i].unique()))
                            rs=np.unique(a)
                            for i in rs:
                                print(i)
                            sub=input("ENTER THE SUBJECT TO SEE FACULTY\'S REMARKS (from above note::CASE-SENSITIVE): ")
                            ar=getIndexes(data,sub)
                            for i in ar:
                                if data.loc[i[0]]['Roll No'].mean()==roll:
                                    print(data.loc[data['Roll No']==roll][i[1]+'Faculty Remarks'].to_numpy())
                        elif c==5:
                            print("\nEXPECTATION OF NEXT SEMESTER\n")
                            print("\nWE CAN PREDICT ONLY IF MARKS OF BOTH CT OF THIS SEMESTER ARE PRESENT IN OUR RECORDS AND RESULT OF ATLEAST TWO SEMESTERS IS DECLARED\n")
                            
                            e=[]
                            e1=[]
                            e2=[]
                            l=0
                            for i in range(1,9):
                                if math.isnan((data.loc[data['Roll No']==roll]['Semester '+str(i)+' Total'])):
                                    continue
                                if(math.isnan(data.loc[data['Roll No']==roll]['Subject '+str((l)*10+1)+' CT1 Marks'])):
                                    continue
                                id1='CT1 Marks'
                                id2='CT2 Marks'
                                e.append(((data.loc[data['Roll No']==roll]['Semester '+str(i)+' Total']).mean()))
                                u=0
                                p=0
                                for j in range((i-1)*10+1,(i*10)+1):
                                    sub='Subject '+str(j) +' '+id1
                                    sub2='Subject '+str(j) +' '+id2
                                    if math.isnan((data.loc[data['Roll No']==roll][sub])):
                                        continue
                                    u=u+(data.loc[data['Roll No']==roll][sub].mean())+(data.loc[data['Roll No']==roll][sub2].mean())
                                    p+=1
                                e3=[]
                                e3.append(u/(p*60)*100)
                                e1.append(u/(p*60)*100)
                                e2.append(((data.loc[data['Roll No']==roll]['Semester '+str(i)+' Total Max Marks']).mean()))
                                l=i
                            k=[]
                            
                            for i,j in zip(e,e2):
                                k1=[]
                                k1.append((i/j)*100)
                                k.append(k1)
                            reg = make_pipeline(StandardScaler(),SGDRegressor(max_iter=2222, tol=1e-3))
                            reg.fit(k,e1)
                            u=0
                            for j in range((l)*10+1,((l+1)*10)+1):
                                sub='Subject '+str(j) +' '+id1
                                sub2='Subject '+str(j) +' '+id2
                                if math.isnan((data.loc[data['Roll No']==roll][sub])):
                                    continue
                                u=u+(data.loc[data['Roll No']==roll][sub].mean())+(data.loc[data['Roll No']==roll][sub2].mean())
                            if(math.isnan(data.loc[data['Roll No']==roll]['Subject '+str((l)*10+1)+' CT1 Marks']) or l<2):
                                print("\nCANNOT PREDICT\n")
                                continue
                            print("\nIN NEXT SEMESTER YOU SHOULD GET THESE MARKS (IN OVERALL PERCENTAGE): \n")
                            r=[]
                            r1=[]
                            r.append(u/0.6)
                            r1.append(r)
                            print(reg.predict(r1))
                        elif c==6:
                            break
                        else:
                            print("\nPLEASE ENTER A VALID CHOICE\n")
               elif b==0:
                  t=1
                  break
            elif (testpas(a,b)==False):
               print("PASSWORD IS WRONG PLZZ TRY AGAIN")
            elif (testid(a)==False):
               print("USER ID IS WRONG PLZZ TRY AGAIN")
    elif a==3:
        while True:
           print("ENTER USER ID")
           a=input("")
           print("ENTER CURRENT PASSWORD")
           b=input("")
           if (testpas(a,b) and testid(a)):
              passreset(a,b)
              break
           else:
              print("INVALID CURRENT DETAIL")
              print("FOR TRY AGAIN, PRESS 1")
              print("FOR EXIT, PRESS 0")
              d=int(input(""))
              if d==0:
                break
