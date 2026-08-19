from pydantic import BaseModel, Field



class ResumeAnalysis(BaseModel):
    candidate_summary: str = Field(
        description="Short professional summary of the candidate"
    )

    current_role: str = Field(
        description="Most likely current or recent professional role"
    )

    suitable_roles: list[str] = Field(
        description="Job roles suitable for the candidate"
    )

    technical_skills: list[str] = Field(
        description="Technical skills found in the resume"
    )

    strengths: list[str] = Field(
        description="Candidate's strongest areas based on the resume"
    )

    skill_gaps: list[str] = Field(
        description="Important skills missing or weak for the suggested roles"
    )

    recommended_projects: list[str] = Field(
        description="Projects that would strengthen the candidate's profile"
    )