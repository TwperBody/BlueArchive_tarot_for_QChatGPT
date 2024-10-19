import random
from pathlib import Path
from pkg.plugin.context import register, handler, BasePlugin, APIHost, EventContext
from pkg.plugin.events import PersonNormalMessageReceived, GroupNormalMessageReceived
from mirai import MessageChain, Plain, Image
import threading
from .servers import run_server  # 导入servers模块的run_server函数

# 注册插件
@register(name="QChatGPT_BlueArchive_tarot", description="BlueArchive塔罗牌消息", version="1.0", author="TwperBody")
class TarotCardPlugin(BasePlugin):

    def __init__(self, host: APIHost):
        self.host = host
        # 确保图片存储目录存在
        self.image_dir = Path("plugins/QChatGPT_BlueArchive_tarot")
        self.image_dir.mkdir(parents=True, exist_ok=True)

    async def initialize(self):
        print("Initializing TarotCardPlugin")
        # 你可以在这里添加更多的初始化代码

    @handler(PersonNormalMessageReceived)
    async def person_normal_message_received(self, ctx: EventContext):
        await self.handle_tarot_card(ctx)

    @handler(GroupNormalMessageReceived)
    async def group_normal_message_received(self, ctx: EventContext):
        await self.handle_tarot_card(ctx)

    async def handle_tarot_card(self, ctx: EventContext):
        msg = ctx.event.text_message
        if msg in ("塔罗牌", "塔罗"):
            random_number = random.randint(0, 21)
            image_url = self.get_image_url(random_number)
            message_chain = MessageChain([
                Plain("老师，这是你今天的塔罗牌："),
                Image(url=image_url)  
            ])
            await ctx.reply(message_chain)  
            ctx.prevent_default()

    def get_image_url(self, random_number):
        # 返回网络上的图片 URL
        return f"http://127.0.0.1:1145/uploads/{random_number:02}.png"

    def __del__(self):
        pass

if __name__ == '__main__':
    # 启动服务器线程
    server_thread = threading.Thread(target=run_server)
    server_thread.daemon = True  # 设置为守护线程
    server_thread.start()
    print("Server is running at http://localhost:1145")

    # 主程序继续执行其他任务
    print("Main program is running...")
    # 在这里添加主程序的其他逻辑
