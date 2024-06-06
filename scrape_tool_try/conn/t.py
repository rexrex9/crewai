import os,sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain
from crewai import Agent, Task, Crew
if "OPENAI_API_KEY" in os.environ:
    del os.environ["OPENAI_API_KEY"]
api_key = os.getenv("GOOGLE_API_KEY")
llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=api_key)

# prompt_template = PromptTemplate.from_template("Write a short story about {topic}.")
# llm_chain = LLMChain(llm=llm, prompt=prompt_template)
#
# if __name__ == "__main__":
#     topic = "a cat"
#     response = llm_chain.run(topic=topic)
#     print(response)



agent = Agent(
    role="情感分析专家",
    goal="研究用户的{query}，找到他的情绪倾向",
    backstory="你是一位情感分析专家，你的任务是根据用户的{query}，找到他的情绪倾向。",
    llm=llm
)


task = Task(
    description="根据用户的{query}，找到他的情绪倾向",
    expected_output="用户的情绪倾向",
    agent=agent,
    llm=llm
)


crew = Crew(
    agents=[agent],
    tasks=[task],
    verbose=2,
    memory=True,
    manager_llm=llm
)

inputs = {
    "query": "我很开心"
}

result = crew.kickoff(inputs=inputs)


