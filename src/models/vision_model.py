import dotenv
import os
import base64
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from src.prompts.template import apply_prompt_template

dotenv.load_dotenv()

vision=ChatOpenAI(
    model=os.getenv("VISION_MODEL"),
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY"),
)

vision_model=vision

def encode_image_to_base64(image_path: str) -> str:
    """将图片文件编码为 base64 字符串"""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def analyze_image_with_text(image_path: str, text_prompt: str = None) -> str:
    """分析图片并返回描述"""
    
    # 获取 vision analyzer prompt
    if text_prompt is None:
        text_prompt = apply_prompt_template("vision_analyzer")
        # 转义大括号
        text_prompt = text_prompt.replace("{", "{{").replace("}", "}}")
    
    # 方法1：使用 base64 编码
    base64_image = encode_image_to_base64(image_path)
    
    message = HumanMessage(
        content=[
            {
                "type": "text", 
                "text": text_prompt
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image}"
                }
            }
        ]
    )
    
    response = vision_model.invoke([message])
    return response.content
    