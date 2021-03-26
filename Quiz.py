
import requests,json,random,html
true_reponses = 0
false_reponses = 0
qst = 0
while True :

    quizApi = requests.get("https://opentdb.com/api.php?amount=1&difficulty=easy")
    quiz = json.loads(quizApi.text)
    quiz = quiz['results']
    quiz=quiz[0]
    
    

    reponses =[]
    reponses.append(quiz['correct_answer']) 
    reponses+=quiz['incorrect_answers']
    
    random.shuffle(reponses)
    print("------------------------ ",quiz['correct_answer'],"-----------------------------")
    quiz['correct_answer']
    print("########## ",quiz['category'],"##########")
    print(html.unescape(quiz['question'])," : ")
    qst+=1
    for i in reponses : 
        print("    ",reponses.index(i)+1," - ",i)

    while True : 

        rep = input("tapez N° de votre reponse : ")
        try : 
            rep = int(rep)
        except : 
            print("invalid valeur")
            continue

        if rep < 1 and rep > len(reponses):
            print("invalid valeur")
            continue
            
        if reponses[rep-1] == quiz['correct_answer'] : 
            true_reponses+=1
            break
        else : 
            false_reponses+=1  
            break


    exit = input("Rejouer ? y/n : ")
    if exit !="y":
        break
            
print("nb de qst",qst)
print("nb de bonne : ",true_reponses)
print("nb de mauvaise : ",false_reponses)