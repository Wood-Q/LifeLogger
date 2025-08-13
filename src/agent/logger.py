from langchain_core.prompts import ChatPromptTemplate
from src.models.chat_model import chat_model
from src.prompts.template import apply_prompt_template
from langchain_core.agents import create_react_agent

logger=create_react_agent(
    llm=chat_model,
    prompt=ChatPromptTemplate.from_template(apply_prompt_template("logger")),
    name="logger",
)