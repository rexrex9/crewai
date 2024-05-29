
import os,sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from crewai import Agent, Task, Crew
from crewai_tools import ScrapeWebsiteTool, WebsiteSearchTool

url = "https://playtoearn.com/blockchaingames"
#url = "https://playtoearn.com/blockchaingame/axie-infinity"

overall_agent = Agent(
    role="找GameFi详细页面链接的助理",
	goal="根据用户的query,找到他所需GameFi游戏的详细页面连接",
	backstory=(
        'https://playtoearn.com/blockchaingame/+游戏名是一个GameFi游戏详细页面连接,'
        '所以仅需找到游戏名组合成的这样的连接返回用户即可。请注意，这些链接中的游戏名中的空格需'
        '要替换成"-"。例如，如果游戏名是"The New Order"，'
        '那么详细页面的链接就是"https://playtoearn.com/blockchaingame/The-New-Order",'
        '请确保返回的链接是有效的。'
	),
	allow_delegation=False,
	verbose=True
)

overall_scrape_tool = WebsiteSearchTool(website_url=url)

find_game_task = Task(
    description=("用户{customer}需要找到游戏详细页面连接"),
    expected_output=("找到游戏详细页面连接"),
	tools=[overall_scrape_tool],
    agent=overall_agent,
)


detail_agent = Agent(
    role="GameFi详细内容助理",
	goal="根据详细页面链接把游戏详细内容返回给用户",
	backstory=(
        '根据前一个agent提供的详细页面链接，得到游戏的详细内容给用户'
	),
	allow_delegation=False,
	verbose=True
)
detail_scrape_tool = WebsiteSearchTool()

find_game_detail_task = Task(
    description=("用户{customer}需要找到游戏的详细内容"),
    expected_output=("找到游戏的详细内容"),
	tools=[detail_scrape_tool],
    agent=detail_agent,

)



crew = Crew(
  agents=[overall_agent,detail_agent],
  tasks=[find_game_task,find_game_detail_task],
  verbose=2,
  memory=True
)

def query(query):
    inputs = {
        "customer": "张三",
        "inquiry": query
    }
    result = crew.kickoff(inputs=inputs)
    return result



