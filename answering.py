import wolframalpha

app_id = 'Q3V6YX-WH5PHUHAKP'

client = wolframalpha.Client(app_id)

class answering:
    def __init__(self):
        pass

    def answerQuestion(self, question):
        res = client.query(question)
        try:
            answer = next(res.results).text
            return answer
        except:
            return "sorry i have no answer for that"

# asnwer_instance = answering()
# print(asnwer_instance.answerQuestion("what is sandwich"))