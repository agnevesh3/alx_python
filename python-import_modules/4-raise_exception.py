#!/usr/bin/python3
def raise_exception():
    try:
        scripts = ""
    except TypeError as te:
        scripts = "Exception has been raised"
        return scripts
    else:
        return scripts
    finally:
        print(scripts)


raise_exception()
