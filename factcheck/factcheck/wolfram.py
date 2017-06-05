import wolframalpha

client = wolframalpha.Client('P7UPQ6-JPXYQKL84U')  # P7UPQ6-JPXYQKL84U


# Get query
def askwolfram(question):
    res = client.query(question)
    for pod in res.pods:
        if pod.title == "Result":
            for sub in pod.subpods:
                return sub.plaintext


# Works best for social/economy statistical data
# checkfact("What is the meaning of life","42")
def checkfact(question, answer):
    result = askwolfram(question)
    if answer in result:
        print("Your answer is correct, good job!")
        return True
    else:
        print("You are wrong, sorry.")
        print("Correct answer is : ")
        print(result)
        return False
