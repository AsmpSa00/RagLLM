import os
from embedchain import App

os.environ["OPENAI_API_KEY"] = "sk-proj-HRDGyfBIqK1vRnt4aUKJT3BlbkFJVjlgFAMkew24js9cpnAS"
app = App()

app.add("https://en.wikipedia.org/wiki/Mark_Cuban")
app.add("https://www.forbes.com/profile/mark-cuban/?sh=f6c73636a04a")

app.query("How many kids does mark cuban have and name them")












