from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

model = OllamaLLM(model="mistral")

def generate_response( task ):
    response = model.invoke(task)
    return response