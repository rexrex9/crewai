import os,sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from crewai import Agent, Task, Crew

gamefi_search_agent = Agent(
    role="GameFi Search Assistant",
    goal="Find the GameFi game's detailed according to the user's query,which is {query}",
    backstory="You are a GameFi Search Assistant, your task is to find the detailed page"
              " of the GameFi game according to the user's query. GameFi is the blockchain game"
)

gamefi_recommend_agent = Agent(
    role="GameFi Recommend Assistant",
    goal="Recommend the GameFi game according to the user's query,which is {query}",
    backstory="You are a GameFi Recommend Assistant, your task is to recommend the GameFi game"
              " according to the user's query. GameFi is the blockchain game"
)

task_search = Task(
    description="find GameFi games according to {query}",
    expected_output="games' details",
    agent=gamefi_search_agent
)

task_recommend = Task(
    description="recommend GameFi games according to {query}",
    expected_output="games' recommendation",
    agent=gamefi_recommend_agent
)


crew = Crew(
    agents=[gamefi_search_agent, gamefi_recommend_agent],
    tasks=[task_search, task_recommend],
    verbose=2,
    memory=True
)

inputs = {
    "query": "I need a fps gameFi game"
}

result = crew.kickoff(inputs=inputs)

print(result)