import os,sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from langchain_google_genai import ChatGoogleGenerativeAI
from crewai import Agent, Task, Crew

api_key = os.getenv("GOOGLE_API_KEY")
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", google_api_key=api_key)

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
)

crew = Crew(
    agents=[agent],
    tasks=[task],
    verbose=2,
)

inputs = {
    "query": "我很开心"
}

result = crew.kickoff(inputs=inputs)


