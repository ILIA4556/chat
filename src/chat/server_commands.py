import os

# class Command: 
#    """ ТУТ команды """
#    def __call__(self, client, *args, **kwds):
#        client.send()
def help(client,prefixes):
    help_message = ("Список команд:\n" + '\n'.join([prefix for prefix in prefixes.values()]))
    client.send(help_message.encode('utf-8'))
def handle_calculation(message):
    expression = message.replace("/calc","")
    expression = expression.replace("^","**")
    result = eval(expression)
    try:
        logging.info(f"server: {result}")
        broadcast(f"server: {result}")
    except:
        broadcast("ошибка")

