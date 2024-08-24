from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

model = OllamaLLM(model="mistral")

systemTemplate = """system:You are a helpful assistant who provides tailored educational content for neuro-diverse students
You provide concise statements in very short and precise answer.
user:{question}"""

def generate_response( task ):
    response = model.invoke(systemTemplate.format(question=task))
    return response