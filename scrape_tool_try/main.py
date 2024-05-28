import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from scrape_tool_try.agents import links_agent as la, detail_agent as da
from datas import filepaths as fp
import json
def scray_try():
    num = 5
    ls = la.get_links(num)
    for l in ls:
        d = da.get_game_detail(l)
        p = os.path.join(fp.GAME_DIR, d['name']+".json")
        with open(p, 'w+') as f:
            f.write(json.dumps(d, indent=4))

if __name__ == '__main__':
    scray_try()