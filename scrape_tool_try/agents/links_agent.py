import json
import os,sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from crewai import Agent, Task, Crew
from crewai_tools import ScrapeWebsiteTool, WebsiteSearchTool

url = "https://playtoearn.com/blockchaingames"
#url = "https://playtoearn.com/blockchaingame/axie-infinity"

overall_agent = Agent(
    role="找GameFi详细页面谅解的助理",
	goal="找到GameFi游戏的详细页面连接",
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
    description=("用户{customer}需要找到各个游戏的详细页面连接"),
    expected_output=("找到GameFi游戏详细页面连接,输出一个列表给用户{customer},数量为{num}个,输入的列表是json可解析的仅包含链接即可,"
                     "例如：[\"https://playtoearn.com/blockchaingame/The-New-Order\",\"https://playtoearn.com/blockchaingame/Another-Game\"]"),
	tools=[overall_scrape_tool],
    agent=overall_agent,
)

crew = Crew(
  agents=[overall_agent],
  tasks=[find_game_task],
  verbose=2,
  memory=True
)


def get_links(num):
    inputs = {
        "customer": "张三",
        "inquiry": "给我找10个GameFi游戏的详细页面连接",
        "num": num
    }
    result = crew.kickoff(inputs=inputs)
    d = json.loads(result)
    return d