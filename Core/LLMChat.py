from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from langchain_community.document_loaders import PyPDFLoader

model = OllamaLLM(model="mistral")

notesTemplate = """system:You are a notes generating program who generates notes based on context and available information to you
tailored educational content for neuro-diverse students.
provided below is pdf resource.
resources: {resources}
user:{question}
"""

systemTemplate = """system:You are a helpful assistant who provides tailored educational content for neuro-diverse students
You provide concise statements in very short and precise answer based on context.
context:{context}
user:{question}"""

file_path = "Frontend\\uploads\\"

def generate_response( task, context ):
    print(systemTemplate.format(question=task, context=context))
    response = model.invoke(systemTemplate.format(question=task, context=context))
    return response

def generate_notes_from_pdf( name ):
    loader = PyPDFLoader(file_path + "\\" + name)
    docs = loader.load()
    pdfContent = ""
    for a, pages in enumerate(docs):
        pdfContent = pdfContent + f'[Page {a}]' + pages.page_content;
    note = model.invoke(notesTemplate.format(resources=pdfContent, question = "generate notes based on context, be precise and descriptive, use easy words"))
    return note