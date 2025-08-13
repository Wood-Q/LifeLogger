from src.models.vision_model import analyze_image_with_text, analyze_image_with_url

def analyze_photo_from_path(image_path: str, timestamp: str = None, location: str = None) -> str:
    """分析本地图片文件"""
    context_info = ""
    if timestamp:
        context_info += f"拍摄时间: {timestamp}\n"
    if location:
        context_info += f"拍摄地点: {location}\n"
    
    prompt = f"""请分析这张图片，并按照以下格式返回 JSON 结果：
    
{context_info}
请分析图片内容，包括：
1. 图片的主要内容描述
2. 识别出的物体和场景
3. 可能的活动类型
4. 情感推断（如果适用）

请返回标准的 JSON 格式结果。"""
    
    return analyze_image_with_text(image_path, prompt)

def analyze_photo_from_url(image_url: str, timestamp: str = None, location: str = None) -> str:
    """分析网络图片 URL"""
    context_info = ""
    if timestamp:
        context_info += f"拍摄时间: {timestamp}\n"
    if location:
        context_info += f"拍摄地点: {location}\n"
    
    prompt = f"""请分析这张图片，并按照以下格式返回 JSON 结果：
    
{context_info}
请分析图片内容，包括：
1. 图片的主要内容描述
2. 识别出的物体和场景
3. 可能的活动类型
4. 情感推断（如果适用）

请返回标准的 JSON 格式结果。"""
    
    return analyze_image_with_url(image_url, prompt)

if __name__ == "__main__":
    # 测试分析本地图片
    test_image_path = "/Users/bytedance/woodq/LifeLogger/test/data/food.jpg"
    
    print("=== 分析本地图片 ===")
    result = analyze_photo_from_path(
        image_path=test_image_path,
        timestamp="12:30",
        location="某某餐厅"
    )
    print(result)