questions = [

    [
        "Who is the Top G ?","Andrew tate","Tristan tate","Tejendra","None",1
    ],
    [
        "Who is the Top T ?","Andrew tate","Tejendra","Vani","Elon musk",2
    ],
    [
        "Who is the top E?","Tristan tate","Elon musk","Tejendra","Vani",2
    ],
    [
        "What is the present company of Andrew tate?","Hustlers University","The real world","twitter","None",2
    ],
    [
        "Which bike is the best bike under 2lakshs?","DUKE 125","Yamaha MT 15","Pulsar ns 125","kawaski Ninja 300",2
    ],
    [
        "Which company did elon musk buy recently?","Google","Twitter","Apple","None",2
    ],

    [
        "Who is tejendra?","He is a content creator","He is a Coder","He is a Top G","All of the above",4
    ]
]

levels = [1000,5000,10000,50000,100000,1000000,10000000]

for i in range(0,len(questions)):
    question = questions[i]
    print(f"{question[0]}")
    print(f"1.{question[1]}          2.{question[2]}")
    print(f"3.{question[3]}          4.{question[4]}")
    answer =  int(input("Enter the answer between 1-4 or 0 to quit the game : "))
    if answer == 0 :
        print("You quit the game.")
        money = levels[i-1]
        break
    if (answer == question[-1]):
        print("")
        print(f"Correct answer you won Rs. {levels[i]}")
        print("")
        money = levels[i]
    elif (answer != question[-1]):
        money = levels[i-1]
        break
print("The Game is Over")
print(f"You take Rs. {money}")