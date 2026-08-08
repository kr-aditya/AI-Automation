from pydantic import BaseModel, Field


class RoadmapSchema(BaseModel):
    target_role: str = Field(
        description="The career role the user wants to achieve"
    )

    roadmap_duration: str = Field(
        description="Recommended duration for the roadmap"
    )

    phases: list[str] = Field(
        description="Major phases of the learning roadmap"
    )

    skills_to_learn: list[str] = Field(
        description="Important skills the user should learn"
    )

    projects_to_build: list[str] = Field(
        description="Projects the user should build for practical experience"
    )

    final_advice: str = Field(
        description="Final personalized advice for the learner"
    )