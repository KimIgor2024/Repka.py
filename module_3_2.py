
def send_email(message, recipient, sender = "university.help@gmail.com"):
    if "@" not in  recipient or not (recipient .endswith('.com') or recipient.endswith(".ru") or recipient.endswith(".net")):
        print(f' {message} Невозможно отправитьписьмо с адреса {sender} на адрес {recipient}.')
    elif "@" not in sender or not (sender.endswith(".com") or sender.endswith(".ru") or sender.endswith(".net")):
        print(f"{message} Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
    elif sender == recipient :
       print(f"{message} Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"{message} Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"{message} НЕСЕАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

