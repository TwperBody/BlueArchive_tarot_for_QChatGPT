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
        if  msg == "塔罗牌":
            random_number = random.randint(0, 21)
            image_path = self.get_image_path(random_number)
            message_chain = MessageChain([
                Plain("老师，这是你今天的塔罗牌："),
                Image(path=str(image_path))
            ])
            await ctx.api.send_message_chain(ctx.event.group_id if hasattr(ctx.event, 'group_id') else ctx.event.user_id, message_chain)
            ctx.prevent_default()
            

    def get_image_path(self, random_number):
        return Path(f"plugins/QChatGPT_BlueArchive_tarot/image/{random_number}.jpg")

    def __del__(self):
        pass
