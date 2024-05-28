
import os,sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool,ScrapeWebsiteTool, WebsiteSearchTool

url = "https://playtoearn.com/blockchaingames"
#url = "https://playtoearn.com/blockchaingame/axie-infinity"

overall_agent = Agent(
    role="找GameFi详细页面谅解的助理",
	goal="找到GameFi游戏的详细页面连接",
	backstory=(
        "https://playtoearn.com/blockchaingame/+游戏名是一个GameFi游戏详细页面连接,"
        "所以仅需找到游戏名组合成的这样的连接返回用户即可。"
	),
	allow_delegation=False,
	verbose=True
)

overall_scrape_tool = ScrapeWebsiteTool(website_url=url)

find_game_task = Task(
    description=("用户{customer}需要找到各个游戏的详细页面连接"),
    expected_output=("找到GameFi游戏详细页面连接,输出一个列表给用户{customer}"),
	tools=[overall_scrape_tool],
    agent=overall_agent,
)

crew = Crew(
  agents=[overall_agent],
  tasks=[find_game_task],
  verbose=2,
  memory=True
)

inputs = {
    "customer": "张三",
    "inquiry": "给我找一下GameFi游戏的详细页面连接",
}
result = crew.kickoff(inputs=inputs)

print(result)