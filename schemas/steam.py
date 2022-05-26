def steamEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "url": item.get("url"),
        "name": item.get("name"),
        "categories": item.get("categories"),
        "img_url": item.get("img_url"),
        "user_reviews": item.get("user_reviews"),
        "all_reviews": item.get("all_reviews"),
        "date": item.get("date"),
        "developer": item.get("developer"),
        "publisher": item.get("publisher"),
        "price": item.get("price"),
        "pegi": item.get("pegi"),
        "pegi_url": item.get("pegi_url"),
    }

def steamsEntity(entity) -> list:
    return [steamEntity(item) for item in entity]