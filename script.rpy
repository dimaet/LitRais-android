init:
    define n = nvl_narrator
    $ page = 0

screen switches():

    imagebutton:
        xalign 0.9
        yalign 0.5
        idle "images/forward buttom.png"
        action Jump("nextLabel")

    imagebutton:
        xalign 0.1
        yalign 0.5
        idle "images/back buttom.png"
        action Jump("backLabel")

label start:

    scene background with dissolve

    show screen switches

    nvl clear

    $ outputText = phrases[page]

    n "[outputText]"


label backLabel:

    $ page -= 1 if page != 0 else 0

    call start


label nextLabel:

    $ page += 1 if len(phrases) > page + 1 else 0

    call start
