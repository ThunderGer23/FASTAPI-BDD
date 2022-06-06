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

def mediumRepoEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "text": item.get("text"),
        "tags": item.get("tags")
    }

def mediumDatesEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "idMediumText": item.get("idMediumText"),
        "title": item.get("title"),
        "url": item.get("url"),
        "authors": item.get("authors"),        
        "timestamp": item.get("timestamp"),
    }

def mediumsEntity(entity) -> list:
    return [mediumEntity(item) for item in entity]

def mediumsDatesEntity(entity) -> list:
    return [mediumDatesEntity(item) for item in entity]