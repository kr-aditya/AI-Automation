from pydantic import BaseModel



class InterviewSchema(BaseModel):
    important_topics: list[str]
    technical_questions: list[str]
    behavioral_questions: list[str]
    practical_questions: list[str]
    preparation_strategy: list[str]