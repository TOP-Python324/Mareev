mail = input("Введите email: ")
if "@" and "." in mail and mail.find("@") < mail.find(".") :
    print("да")
else:
    print("нет")
    
# Введите email: mareev@da.ru
# да
