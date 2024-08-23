# pip install duckduckgo-search langchain-community langchain

from langchain_community.tools import DuckDuckGoSearchRun
ddg_search = DuckDuckGoSearchRun()
result = ddg_search.run("python")
print(result)