def mediumEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "title": item.get("title"),
        "url": item.get("url"),
        "authors": item.get("authors"),
        "text": item.get("text"),
        "timestamp": item.get("timestamp"),
        "tags": item.get("tags")
    }

def mediumsEntity(entity) -> list:
    return [mediumEntity(item) for item in entity]