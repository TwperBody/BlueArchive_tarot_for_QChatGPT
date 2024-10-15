import random
from pathlib import Path
from pkg.plugin.context import register, handler, BasePlugin, APIHost, EventContext
from pkg.plugin.events import PersonNormalMessageReceived, GroupNormalMessageReceived
from mirai import MessageChain, Plain, Image

# 注册插件
@register(name="QChatGPT_BlueArchive_tarot", description="BlueArchive塔罗牌消息", version="1.0", author="TwperBody")
class TarotCardPlugin(BasePlugin):

    def __init__(self, host: APIHost):
        self.host = host
        # 确保图片存储目录存在
        self.image_dir = Path("plugins/QChatGPT_BlueArchive_tarot")
        self.image_dir.mkdir(parents=True, exist_ok=True)

    async def initialize(self):
        pass

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
            Image(url=image_url)  # 使用网络上的图片 URL
        ])
        await ctx.reply(message_chain)  # 使用 ctx.reply 发送消息链
        ctx.prevent_default()

def get_image_url(self, random_number):
    # 返回网络上的图片 URL
    return f"http://http://127.0.0.1:1145/upload/{random_number:02}.png"


def __del__(self):
    pass


#    def convert_message(self, message):
#        parts = []
#        last_end = 0
#        for match in self.image_pattern.finditer(message):
#            start, end = match.span()
#            # 添加图片前的文本
#            if start > last_end:
#                parts.append(Plain(message[last_end:start]))
#            # 提取图片 URL 并添加图片
#            image_url = match.group(1)
#            parts.append(Image(url=image_url))
#            last_end = end
#        # 添加最后一个图片后的文本
#        if last_end < len(message):
#            parts.append(Plain(message[last_end:]))
#        return parts if parts else message  # 如果没有修改，返回原始消息
