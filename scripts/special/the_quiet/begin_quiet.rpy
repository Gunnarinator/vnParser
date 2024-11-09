label begin_quiet:

    $ gallery_ztlq.unlock_item(1)
    $ renpy.save_persistent()
    if loops_finished == 1:
        stop secondary fadeout 15.0
        play music "audio/_music/mound/The Mound Movement II Intro.flac" fadein 20.0
        queue music "audio/_music/mound/The Mound Movement II Loop.flac" loop
    elif loops_finished == 2:
        stop secondary fadeout 15.0
        play music "audio/_music/mound/The Mound Movement III Intro.flac" fadein 20.0
        queue music "audio/_music/mound/The Mound Movement III Loop.flac" loop
    elif loops_finished == 3:
        stop secondary fadeout 15.0
        play music "audio/_music/mound/The Mound Movement IV Intro.flac" fadein 20.0
        queue music "audio/_music/mound/The Mound Movement IV Loop.flac" loop

    $ quick_menu = False
    $ blade_held = False
    hide farback onlayer farback
    hide farback onlayer farback
    hide mirror onlayer front
    hide content onlayer front
    hide player onlayer front
    scene bg black
    with fade
    scene farback quiet onlayer farback at Position(ypos=1125)
    show bg quiet path onlayer back at Position(ypos=1125)
    show mid quiet path onlayer front at Position(ypos=1125)
    show fore quiet path onlayer inyourface at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    if loops_finished == 0:
        truth "You are alone in a place that is empty. It is quiet here.\n"

    else:
        truth "You find yourself in The Long Quiet once again.\n"


    menu:
        extend ""

        "{i}• [[Proceed to the cabin.]{/i}":
            $ gallery_ztlq.unlock_item(2)
            $ renpy.save_persistent()
            play audio "audio/one_shot/footsteps_hike_short.flac"
            $ quick_menu = False
            hide farback onlayer back
            hide farback onlayer farback
            hide bg onlayer back
            hide mid onlayer front
            hide fore onlayer inyourface
            scene bg black
            with fade
            scene farback quiet onlayer farback at Position(ypos=1125)
            show back trees cabin quiet onlayer back at Position(ypos=1125)
            show bg cabin quiet onlayer front at Position(ypos=1125)
            if loops_finished != 5:
                show fire anim mound onlayer front at Position(ypos=1125)
                show mound d onlayer front at Position(ypos=1125)
            show mid cabin quiet onlayer inyourface at Position(ypos=1125)
            show fore cabin quiet onlayer inyourface at Position(ypos=1125)
            with fade
            if persistent.quick_menu:
                $ quick_menu = True

            if loops_finished == 0:
                stop secondary fadeout 15.0
                play music "audio/_music/mound/The Mound Movement I.flac" loop fadein 20.0
            if loops_finished == 5:
                jump felina_start
            # shift locations
            truth "You are at the cabin.\n"
            menu:
                extend ""

                "{i}• [[Approach her.]{/i}":
                    $ quick_menu = False
                    play audio "audio/one_shot/footsteps_hike_short.flac"
                    scene bg black
                    hide farback onlayer farback
                    hide farback back farback
                    hide bg onlayer front
                    hide fire onlayer front
                    hide back onlayer back
                    hide mound onlayer front
                    hide mid onlayer inyourface
                    hide fore onlayer inyourface
                    with fade
                    show farback quiet onlayer farback at Position(ypos=1125)
                    show hands mound onlayer front at Position(ypos=1125)
                    show mound neutral onlayer front at Position(ypos=1125)
                    with fade
                    if persistent.quick_menu:
                        $ quick_menu = True
                    if loops_finished == 0:
                        jump quiet_1_start
                    elif loops_finished == 1:
                        jump quiet_2_start
                    elif loops_finished == 2:
                        jump quiet_3_start
                    elif loops_finished == 3:
                        jump quiet_4_start

return
