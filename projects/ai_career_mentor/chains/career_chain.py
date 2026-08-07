from langchain_core.output_parsers import PydanticOutputParser

from prompts.career_prompt import career_prompt
from schemas.career_schema import CareerAnalysis
from utils.llm import llm

parser = PydanticOutputParser(
    pydantic_object=CareerAnalysis
)

career_chain = (
    career_prompt.partial(
        format_instructions=parser.get_format_instructions()
    )
    | llm
    | parser
)