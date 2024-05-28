import json
import os,sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from crewai import Agent, Task, Crew
from crewai_tools import ScrapeWebsiteTool, WebsiteSearchTool



detail_agent = Agent(
    role="GameFi详细内容助理",
	goal="根据详细页面链接爬取游戏详细内容",
	backstory=(
        '根据前一个agent提供的详细页面链接，爬取游戏的详细内容,并以json格式返回给用户。'
        '请确保返回的内容是有效的json格式。例如'
        '{"name": "AI Arena","url": "https://playtoearn.net/blockchaingame/ai-arena","genres": ["Fighting","PVP","Sci-Fi"],'
        '"blockchain": "Other","platforms": ["Web"],"status": "Live","content": "AI Arena is a breakthrough gaming experience where humans collect, train and battle AI powered characters in PvP platform fighting game.\n\nIn the AI Arena - Gaming Competition, Gamers can purchase, train and battle AI-enabled NFTs in a PvP fighting game. \n\nGame Style - AI Arena is a platform fighting game, where the objective is to knock your opponent off of a platform. \n\nHow to Play - First, you train your NFT character through Imitation Learning, where the AI learns to play the game by copying your actions. When you feel your character is ready to fight, you submit the NFT into the arena to compete in Ranked Battle. Your NFT then fights autonomously against opponents near its skill level. \n\nThe Objective -The objective of the game is to train the most powerful AI NFT, climb the global leaderboard, and earn rewards in our native token called Neurons or $NRN.",'
        '"NFT_support": "Yes","free_to_play": "Yes","play_to_earns": ["Crypto"],"socialscore_number": "612","socialscore_change": "(-33.21%)"}'
	),
	allow_delegation=False,
	verbose=True
)

sss = '''
{"name": "AI Arena","url": "https://playtoearn.net/blockchaingame/ai-arena","genres": ["Fighting","PVP","Sci-Fi"],
    "blockchain": "Other",
    "platforms": ["Web"],
    "status": "Live",
    "content": "AI Arena is a breakthrough gaming experience where humans collect, train and battle AI powered characters in PvP platform fighting game.\n\nIn the AI Arena - Gaming Competition, Gamers can purchase, train and battle AI-enabled NFTs in a PvP fighting game. \n\nGame Style - AI Arena is a platform fighting game, where the objective is to knock your opponent off of a platform. \n\nHow to Play - First, you train your NFT character through Imitation Learning, where the AI learns to play the game by copying your actions. When you feel your character is ready to fight, you submit the NFT into the arena to compete in Ranked Battle. Your NFT then fights autonomously against opponents near its skill level. \n\nThe Objective -The objective of the game is to train the most powerful AI NFT, climb the global leaderboard, and earn rewards in our native token called Neurons or $NRN.",
    "NFT_support": "Yes",
    "free_to_play": "Yes",
    "play_to_earns": ["Crypto"],
    "socialscore_number": "612",
    "socialscore_change": "(-33.21%)"}
'''
def get_game_detail(url):
    detail_scrape_tool = ScrapeWebsiteTool(website_url=url)

    find_game_detail_task = Task(
        description=("用户{customer}需要找到游戏的详细内容"),
        expected_output=('找到GameFi游戏的详细内容,并以json格式返回给用户{customer}'),
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

    print(json.loads(result))
    d = json.loads(result)
    with open("game_detail.json","w") as f:
        json.dump(d,f,indent=4)