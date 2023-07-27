#!/usr/bin/python3
def raise_exception_msg(message):
    try:
        message_raise = message
    except NameError:
        message_raise = message
        return message_raise
    else:
        return message_raise
    finally:
        print(message_raise)
