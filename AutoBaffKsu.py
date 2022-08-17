from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api

access_token = "vk1.a.Jc2n6tTk9bm0ePdsJ_ZmziwM24D5m-Vuyvm3Ga2m4z_SLvXBIzduTB6NhPxDBVaSCZrw8P-vuVlz2EDWNCrgPrPDjiYOJbbLahPiRYd1YOI6DOruKOPk8zISCe6eDCI4T0_zgtqrQP8GjDp3biz8LRs7p2hdRR27ha6VSWcstfBzB5v8RvtLnlNkiFecy5U7"
vk_session = vk_api.VkApi(token=access_token)
session_api = vk_session.get_api()
long_poll = VkLongPoll(vk_session)
user_king = [584067096]

msg = "Черный Санитар готов предоставить вам благословения на ваш выбор, " \
      "просто задействуйте соответствующую команду из перечисленных ниже:" \
        "\nБаф у1 - Удача" \
        "\nБаф а1 - Атака" \
        "\nБаф з1 - Защита" \
        "\nБаф д1 - Демона" \

while True:
    try:
        for event in long_poll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                if event.from_chat and event.chat_id == 103:
                    response = event.text.lower()
                    if response == 'Санитар':
                        vk_session.method("messages.send", {"chat_id": event.chat_id,
                                                            "message": msg,
                                                            "random_id": 0})
                    if response == 'Санитар  статус':
                        if event.user_id in user_king:
                            vk_session.method("messages.send", {"chat_id": event.chat_id,
                                                                "message": "статус: включен",
                                                                "random_id": 0})
                    if "баф" in response:
                            if "у1" in response:
                                vk_session.method("messages.send", {"chat_id": event.chat_id,
                                                                    "message": "Благословение удачи",
                                                                    "reply_to": event.message_id,
                                                                    "random_id": 0})
                            if "а1" in response:
                                vk_session.method("messages.send", {"chat_id": event.chat_id,
                                                                    "message": "Благословение атаки",
                                                                    "reply_to": event.message_id,
                                                                    "random_id": 0})
                            if "з1" in response:
                                vk_session.method("messages.send", {"chat_id": event.chat_id,
                                                                    "message": "Благословение защиты",
                                                                    "reply_to": event.message_id,
                                                                    "random_id": 0})
                            if "д1" in response:
                                vk_session.method("messages.send", {"chat_id": event.chat_id,
                                                                    "message": "Благословение демона",
                                                                    "reply_to": event.message_id,
                                                                    "random_id": 0})
    except Exception:
        pass
