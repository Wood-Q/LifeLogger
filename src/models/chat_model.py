import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from src.prompts.template import apply_prompt_template

# 首先加载环境变量

doubao=ChatOpenAI(
    model=os.getenv("MODEL"),
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY"),
)

chat_model=doubao

# 创建 prompt 模板
def create_logger_prompt():
    """创建 LifeLogger 的 prompt 模板"""
    system_prompt = apply_prompt_template("logger")
    
    # 转义 Jinja2 模板中的大括号，避免与 LangChain 变量冲突
    system_prompt = system_prompt.replace("{", "{{").replace("}", "}}")
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{user_input}")
    ])
    
    return prompt

# 创建完整的链式调用
def create_logger_chain():
    """创建带有 prompt 的完整链"""
    prompt = create_logger_prompt()
    chain = prompt | chat_model
    return chain
