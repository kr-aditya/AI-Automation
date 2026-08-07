from pydantic import BaseModel, Field


class CareerAnalysis(BaseModel):
    current_level: str = Field(
        description="Current skill level of the candidate"
    )

    match_score: int = Field(
        description="Overall job readiness score from 0 to 100"
    )

    strengths: list[str] = Field(
        description="Candidate's strongest skills"
    )

    weaknesses: list[str] = Field(
        description="Areas that need improvement"
    )

    missing_skills: list[str] = Field(
        description="Important missing skills for the target role"
    )

    learning_priority: list[str] = Field(
        description="Skills to learn in order of priority"
    )

    career_summary: str = Field(
        description="A short summary of the candidate's profile"
    )