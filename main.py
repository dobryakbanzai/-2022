import eel
from functs import gen, expr

eel.init("web")


@eel.expose
def genericPrim():
    gn = ""
    while len(gn) < 3:
        gn = gen()
        print(gn)
    return gn


@eel.expose
def genericAnsw(msg):
    an, i = expr(msg, 0)
    print(an)
    return an


eel.start("main.html", size=(700, 700))
