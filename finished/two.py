url = "https://playtoearn.com/blockchaingames"

from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool,ScrapeWebsiteTool, WebsiteSearchTool

support_agent = Agent(
    role="找GameFi的助理",
	goal="帮助用户找到GameFi游戏",
	backstory=(
        "你在playtoearn工作，现在正在为{customer}提供支持。"
	),
	allow_delegation=False,
	verbose=True
)


docs_scrape_tool = ScrapeWebsiteTool(
    website_url=url
)

find_game_task = Task(
    description=("用户{customer}需要找到GameFi游戏"),
    expected_output=("找到GameFi游戏的信息"),
	tools=[docs_scrape_tool],
    agent=support_agent,
)

crew = Crew(
  agents=[support_agent],
  tasks=[find_game_task],
  verbose=2,
  memory=True
)

inputs = {
    "customer": "张三",
    "inquiry": "给我推荐一个GameFi游戏",
}
result = crew.kickoff(inputs=inputs)

print(result)