from selenium_profiles.utils.installer import install_chromedriver
from pyChatGPT import ChatGPT
from interfaces.interfaces import IAChat


class GPTIA(ChatGPT, IAChat):
    def __init__(self, tokenChatGPTSession: str):
        install_chromedriver()
        ChatGPT.__init__(self, session_token=tokenChatGPTSession)

    def run(self) -> None:
        pass

    async def chat(self, query: str) -> str:
        return self.send_message(message=query)['message']
