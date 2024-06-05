import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=api_key)

prompt_template = PromptTemplate.from_template("Write a short story about {topic}.")
llm_chain = LLMChain(llm=llm, prompt=prompt_template)

if __name__ == "__main__":
    topic = "a cat"
    response = llm_chain.run(topic=topic)
    print(response)

