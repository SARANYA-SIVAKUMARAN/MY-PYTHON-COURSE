from mcq import Mcq
question=["1. Father of computer__\na. Charles babge\tb. James\tc. Nicolus",
          "2. Father of Gravity__ \na. Raman\tb. Newton\tc. charlus",
          "3. who is the ceo of google__\na. Manirathnam\tb. Newton\tc.Sunder pichai"]


test=[Mcq(question[0],"a"),Mcq(question[1],"b"),Mcq(question[2],"c")]


def runtest():
    score=0
    for que in test:
        print(que.question)
        answer=input("Enter your answer: ")
        if answer==que.answer:
            score+=1
    # print("You have scored: " + score+"/"+ len(test))   
    print(f"You have scored: {score}/{len(test)}")
    print("\n")
runtest()         