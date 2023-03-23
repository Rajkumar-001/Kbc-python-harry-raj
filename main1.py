questions=[
    ["which language was used to create facbook","javascript","python","java","php",4],
    ["Total bits used by the IPv6 address","64 bit","256bit","128bit","32bit",4],
    ["which langauge is mainly used for artifical intelligence","java","javascript","prolog","c",4],
    ["why is the firewall used in a comp[uter","monitoring","data transmisiion","authentiaction","security",4],
    ["how many levels are there in the artitecture of DBMS","1","2","4","3",4],
    ["which language was used to create facbook", "javascript", "python", "java", "php", 4],
    ["Total bits used by the IPv6 address", "64 bit", "256bit", "128bit", "32bit", 4],
    ["which langauge is mainly used for artifical intelligence", "java", "javascript", "prolog", "c",4],
    ["why is the firewall used in a comp[uter", "monitoring", "data transmisiion", "authentiaction", "security", 4],
    ["how many levels are there in the artitecture of DBMS", "1", "2", "4", "3", 4],
    ["which language was used to create facbook", "javascript", "python", "java", "php", 4],
    ["Total bits used by the IPv6 address", "64 bit", "256bit", "128bit", "32bit", 4],
    ["which langauge is mainly used for artifical intelligence", "java", "javascript", "prolog", "c",4],
    ["why is the firewall used in a comp[uter", "monitoring", "data transmisiion", "authentiaction", "security", 4],
    ["how many levels are there in the artitecture of DBMS", "1", "2", "4", "3", 4],
    ["which language was used to create facbook", "javascript", "python", "java", "php", 4],
    ["Total bits used by the IPv6 address", "64 bit", "256bit", "128bit", "32bit", 4],
    ["which langauge is mainly used for artifical intelligence", "java", "javascript", "prolog", "c",4],
    ["why is the firewall used in a comp[uter", "monitoring", "data transmisiion", "authentiaction", "security", 4],
    ["how many levels are there in the artitecture of DBMS", "1", "2", "4", "3", 4],
    ["which language was used to create facbook", "javascript", "python", "java", "php", 4],
    ["Total bits used by the IPv6 address", "64 bit", "256bit", "128bit", "32bit", 4],
    ["which langauge is mainly used for artifical intelligence", "java", "javascript", "prolog", "c",4],
    ["why is the firewall used in a comp[uter", "monitoring", "data transmisiion", "authentiaction", "security", "4"],
    ["how many levels are there in the artitecture of DBMS", "1", "2", "4", "3", 4]
]
levels=[1000,2000,10000,25000,100000,125000,200000,320000,500000,1000000,2000000,2500000,5000000,10000000,20000000,50000000,70000000]

money=0
for i in range(0,len(questions)):
    question=questions[i]
    print(f"\n\nquestion for  Rs.{levels[i]}")
    print(f"a.{question[1]}   b.{question[2]} c.{question[3]} d.{question[4]} ")
    reply=int(input("enter your answer[1-4]"))
    if reply==question[-1]:
        print(f"correct answer,you have won Rs{levels[i]}")
        if i==4:
            money==10000
        elif i==9:
            money==320000
        elif i==12:
            money==10000000

    else:
        print("wrong answer!")
        break

    print(f"your take home money is {money}")


