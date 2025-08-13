from rich.traceback import install
from src.models.vision_model import vision_model
import dotenv

# 运行这一行，rich 就会自动接管后续所有的报错信息
install()
dotenv.load_dotenv()

if __name__ == "__main__":
    print(vision_model.invoke("你好，介绍一下你自己").content)