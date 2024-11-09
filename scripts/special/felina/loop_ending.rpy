label loop_ending:

    $ quick_menu = False

    stop music fadeout 1.0
    $ quick_menu = False
    $ current_princess = "base"
    $ trait_hero = True
    play sound "audio/looping/uncomfortable ambiance.ogg" loop fadein 1.0
    scene chapter princess with fade
    show text _("{color=#FFFFFF00}Chapter One. The Hero and the Princess.{/color}") at Position(ypos=850)
    $ renpy.pause(4.0)
    stop sound fadeout 1.0
    play music "audio/_music/ch1/The Princess.flac" loop
    play sound "audio/looping/uncomfortable ambiance.ogg" loop
    hide text
    scene bg path onlayer farback at flip, Position(ypos=1125)
    show midground path onlayer back at flip, Position(ypos=1125)
    show front path onlayer front at flip, Position(ypos=1125)

    show bg black
    hide chapter
    with fade

    voice "audio/voices/ch1/woods/narrator/script_n_1.flac"

    if persistent.quick_menu:
        $ quick_menu = True

    n "You're on a path in the woods. And at the end of that path is a cabin. And in the basement of that cabin is a princess.\n"
    voice "audio/voices/ch1/woods/narrator/script_n_2.flac"
    n "You're here to slay her.\nIf you don't, it will be the end of the world.\n"
    menu:
        extend ""

        "{i}• (Explore) The end of the world? What are you talking about?{/i}" if forest_1_questioning_start == False:
            jump loop_precredits

        "{i}• (Explore) Have you considered that maybe the only reason she's going to end the world is {b}because{/b} she's locked up?{/i}":
            jump loop_precredits

        "{i}• (Explore) Killing a princess seems kind of bad, though, doesn't it?{/i}":
            jump loop_precredits

        "{i}• (Explore) Can't someone else do this?{/i}" if forest_1_someone_else_explore == False:
            jump loop_precredits

        "{i}• (Explore) Forget it, I'm not doing this.{/i}":
            jump loop_precredits

        "{i}• (Explore) Have you considered that maybe I'm okay with the world ending?{/i}":
            jump loop_precredits

        "{i}• (Explore) Do I get some sort of reward for doing this?{/i}":
            jump loop_precredits

        "{i}• Oh, okay. Thanks for telling me what to do.{/i}":
            jump loop_precredits

        "{i}• Sweet! I've always wanted to off a monarch. Viva la revolución!{/i}" if forest_1_conscientious_objector_explore == False:
            jump loop_precredits

        "{i}• [[Silently continue to the cabin.]{/i}":
            jump loop_precredits

        "{i}• [[Turn around and leave.]{/i}":
            jump loop_precredits

label loop_precredits:
    $ achievement.grant("ACH_END_LOOP")
    hide bg path onlayer farback
    hide midground path onlayer back
    hide front path onlayer front
    with fade
    $ final_ending = "loop"
    jump credits

return
