def npmEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "Dependency Name": item.get("Dependency Name"),
        "Repository": item.get("Repository"),
        "GitHub Star": item.get("GitHub Star"),
        "GitHub Forks": item.get("GitHub Forks"),
        "GitHub Watchers": item.get("GitHub Watchers"),
        "Abondoned": item.get("Abondoned"),
        "Code Coverage %": item.get("Code Coverage %"),
        "Linters": item.get("Linters"),
        "Dependenats": item.get("Dependenats"),
        "NPM Stars": item.get("NPM Stars"),
        "Maintainers": item.get("Maintainers"),
        "Contributors": item.get("Contributors"),
        "Dependencies": item.get("Dependencies"),
        "License": item.get("License"),
        "Total Issues": item.get("Total Issues"),
        "Open Issues": item.get("Open Issues"),
        "Security Advisories": item.get("Security Advisories")
    }

def npmsEntity(entity) -> list:
    return [npmEntity(item) for item in entity]