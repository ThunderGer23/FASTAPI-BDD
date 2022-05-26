from typing import Optional
from pydantic import BaseModel

class NpmDatesForGithub(BaseModel):
    id: Optional[str]
    dependencyName: str
    repository: str
    githubstar: str
    githubforks: str
    githubwatchers: str
    abondoned: str
    maintainers: str
    contributors: str
    
class NpmDatesForComplementary(BaseModel):
    id: Optional[str]
    idNpmDatesForGithub: str
    codeCoverage: str
    linters: str
    dependenats: str
    npmStars: str
    dependencies: str
    license: str
    totalissues: str
    openissues: str
    securityAdvisories: str



