import wolframalpha
import wikipedia

while True:
    question = input("Ask me anything! ")
    app_id = "******-***********"
    try:
        client = wolframalpha.Client(app_id)
        res = client.query(question)
        answer = next(res.results).text
        print(answer)
    except:
        print(wikipedia.summary(question,sentences=2))
