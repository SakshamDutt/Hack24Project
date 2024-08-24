from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

model = OllamaLLM(model="mistral")

def generate_response( task, answerclass ):
    response = model.invoke(task)
    print(response)
    answerclass.content