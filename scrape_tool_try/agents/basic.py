import os,sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from crewai import Agent, Task, Crew
from crewai_tools import ScrapeWebsiteTool, WebsiteSearchTool, PDFSearchTool
from crewai import Process

agent = Agent(
    role="情感分析专家",
    goal="研究用户的{query}，找到他的情绪倾向",
    backstory="你是一位情感分析专家，你的任务是根据用户的{query}，找到他的情绪倾向。",
)


task = Task(
    description="根据用户的{query}，找到他的情绪倾向",
    expected_output="用户的情绪倾向",
    agent=agent
)


crew = Crew(
    agents=[agent],
    tasks=[task],
    verbose=2,
    memory=True
)

inputs = {
    "query": "我很开心"
}

result = crew.kickoff(inputs=inputs)

print(result)