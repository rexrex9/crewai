import os,sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from crewai import Agent, Task, Crew
from crewai_tools import ScrapeWebsiteTool, WebsiteSearchTool



detail_agent = Agent(
    role="GameFi详细内容助理",
	goal="根据详细页面链接爬取游戏详细内容",
	backstory=(
        '根据前一个agent提供的详细页面链接，爬取游戏的详细内容'
	),
	allow_delegation=False,
	verbose=True
)


def get_game_detail(url):
    detail_scrape_tool = ScrapeWebsiteTool(website_url=url)

    find_game_detail_task = Task(
        description=("用户{customer}需要找到各个游戏的详细内容"),
        expected_output=("找到GameFi游戏的详细内容"),
        tools=[detail_scrape_tool],
        agent=detail_agent,
    )
    crew = Crew(
      agents=[detail_agent],
      tasks=[find_game_detail_task],
      verbose=2,
      memory=True
    )
    inputs = {
        "customer": "张三",
        "inquiry": "给我这个游戏的详细内容",
    }
    result = crew.kickoff(inputs=inputs)
    return result

if __name__ == '__main__':
    url = "https://playtoearn.com/blockchaingame/axie-infinity"
    result = get_game_detail(url)
    print(result)

