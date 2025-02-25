from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults

load_dotenv()

tool = TavilySearchResults()
response = tool.run('Today weather in peshawar is?')
for data in response:
    print(data['content'])