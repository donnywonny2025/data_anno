import os
import json
import urllib.request
import argparse
import sys

def firecrawl_search(query):
    # This key was verified directly
    api_key = os.environ.get("FIRECRAWL_API_KEY", "fc-a464096db59749bbabef6243870430e0")
    
    url = "https://api.firecrawl.dev/v1/search"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    data = json.dumps({"query": query}).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    
    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode("utf-8"))
            if result.get("success"):
                return result.get("data", [])
            else:
                return {"error": "API returned unsuccessful response"}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Firecrawl Fact Checking Tool")
    parser.add_argument("query", type=str, help="The search query to fact check")
    args = parser.parse_args()
    
    results = firecrawl_search(args.query)
    print(json.dumps(results, indent=2))
