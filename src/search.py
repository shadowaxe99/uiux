```python
from typing import List
from .schemas import SearchResultSchema

searchResults: List[SearchResultSchema] = []

def searchFeedback(query: str) -> List[SearchResultSchema]:
    global searchResults
    searchResults = []
    for project in activeProjects:
        for feedback in projectFeedback[project]:
            if query in feedback.message:
                searchResults.append(SearchResultSchema(project=project, feedback=feedback))
    return searchResults

def getSearchResults() -> List[SearchResultSchema]:
    global searchResults
    return searchResults
```