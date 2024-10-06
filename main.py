import os
import re
import random
from pkg.plugin.models import *
from pkg.plugin.host import EventContext, PluginHost
from mirai import Image, Plain

@register(name="QChatGPT_BlueArchive_tarot", description="BlueArchive塔罗牌消息", version="1.0", author="TwperBody")
class TarotCardPlugin(Plugin):

    def __init__(self, plugin_host: PluginHost):
        super().__init__(plugin_host)
        # 设置本地图片文件夹路径
        self.image_folder = "plugins/QChatGPT_BlueArchive_tarot/image"

    @on(NormalMessageResponded)
    def add_tarot_card(self, event: EventContext, **kwargs):
        original_message = kwargs['response_text']
        if "卡罗牌" in original_message:
            optimized_message = self.add_tarot_card_to_message()
            event.add_return('reply', optimized_message)
        else:
            event.add_return('reply', original_message)

    def add_tarot_card_to_message(self):
        # 生成一个0-21的随机数
        random_number = random.randint(0, 21)
        # 确保编号为两位数，如01, 02, ..., 21
        formatted_number = f"{random_number:02d}"
        image_name = f"{formatted_number}.png"  # 假设图片文件名格式为 card_00.png, card_01.png, ...
        image_path = os.path.join(self.image_folder, image_name)
        if os.path.exists(image_path):
            return [Plain("老师，这是你今天的卡罗牌："), Image(path=image_path)]
        else:
            return [Plain("老师，这是你今天的卡罗牌："), Plain("图片未找到。")]

    def __del__(self):
        pass