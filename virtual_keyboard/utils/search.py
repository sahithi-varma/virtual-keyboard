import webbrowser

def perform_search(platform, query):
    if not query.strip():
        return
    if platform == "Google":
        url = f"https://www.google.com/search?q={query}"
    elif platform == "YouTube":
        url = f"https://www.youtube.com/results?search_query={query}"
    elif platform == "Instagram":
        url = f"https://www.instagram.com/explore/tags/{query}/"
    webbrowser.open(url)