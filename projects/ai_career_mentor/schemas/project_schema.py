from pydantic import BaseModel


class Project(BaseModel):
    title: str
    difficulty: str
    purpose: str
    tech_stack: list[str]
    key_features: list[str]


class ProjectSchema(BaseModel):
    projects: list[Project]