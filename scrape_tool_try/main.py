import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from scrape_tool_try.agents import links_agent as la, detail_agent as da,both_agent as ba
from datas import filepaths as fp
import json
import time
def scray_try():
    num = 10
    ls = la.get_links(num)
    for l in ls:
        try:
            d = da.get_game_detail(l)
            p = os.path.join(fp.GAME_DIR, d['name']+".json")
            with open(p, 'w+') as f:
                f.write(json.dumps(d, indent=4))
        except Exception as e:
            print("error")
            continue

def query_game_detail(query):
    ba.query(query)

if __name__ == '__main__':
    t1 = time.time()
    query_game_detail("给我AI Arena这个游戏的详细内容")
    t2 = time.time()
    print(t2-t1)