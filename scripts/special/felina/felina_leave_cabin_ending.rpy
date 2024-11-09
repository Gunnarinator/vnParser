label felina_leave_cabin_ending:
    voice "audio/voices/felina/cabin/leave/hero/1.flac"
    hero "I think I'm going to stay right here. Whatever you're doing right now, wherever you're going, it feels like it's for just the two of you.\n"
    if first_princess == "stranger":
        voice "audio/voices/felina/cabin/leave/contrarian/1.flac"
        contrarian "Yeah. I think we've done our job.\n"
    label felina_leave_cabin_hero_goodbye:
        default felina_leave_cabin_hero_goodbye = False
        menu:
            extend ""

            "{i}• (Explore) Are you going to be okay alone?{/i}" if first_princess != "stranger" and felina_leave_cabin_hero_goodbye == False:
                $ felina_leave_cabin_hero_goodbye = True
                voice "audio/voices/felina/cabin/leave/hero/2.flac"
                hero "Yeah. I'm not sure I'll be alone for too long, anyways. The others are still around here somewhere. I'll find them.\n"
                jump felina_leave_cabin_hero_goodbye

            "{i}• (Explore) Are you two going to be okay alone?{/i}" if first_princess == "stranger" and felina_leave_cabin_hero_goodbye == False:
                $ felina_leave_cabin_hero_goodbye = True
                voice "audio/voices/felina/cabin/leave/contrarian/2.flac"
                contrarian "We're not alone. We have each other!\n"
                voice "audio/voices/felina/cabin/leave/hero/3.flac"
                hero "And I'm sure we'll find the others.\n"
                jump felina_leave_cabin_hero_goodbye

            "{i}• (Explore) Thanks for everything.{/i}" if felina_leave_cabin_hero_goodbye == False:
                $ felina_leave_cabin_hero_goodbye = True
                voice "audio/voices/felina/cabin/leave/hero/4.flac"
                hero "Don't mention it. Thanks for making all the hard choices along the way.\n"
                jump felina_leave_cabin_hero_goodbye

            "{i}• (Explore) Are you sure you don't want to come?{/i}" if felina_leave_cabin_hero_goodbye == False:
                $ felina_leave_cabin_hero_goodbye = True
                voice "audio/voices/felina/cabin/leave/hero/5.flac"
                hero "Yeah. It wouldn't feel right. But I'll be okay.\n"
                if first_princess == "stranger":
                    voice "audio/voices/felina/cabin/leave/contrarian/3.flac"
                    contrarian "We'll be okay.\n"
                    voice "audio/voices/felina/cabin/leave/hero/6.flac"
                    hero "See? I'm not even alone. If he's here with me, I'm sure we can find the others, too.\n"
                else:
                    voice "audio/voices/felina/cabin/leave/hero/7.flac"
                    hero "I don't think I'll be alone for long, either. I'm sure I can find the others.\n"
                jump felina_leave_cabin_hero_goodbye

            "{i}• [[Leave with the Princess.]{/i}":
                jump felina_leave_cabin_leave_join

label felina_leave_cabin_leave_join:

    $ quick_menu = False
    play audio "audio/one_shot/footsteps_creaky.flac"
    scene bg black
    hide bg onlayer farback
    hide stranger onlayer back
    hide princess onlayer back
    with fade
    if felina_cabin_leave_hand_hold:
        truthmid "Hands clasped together, you and the Princess leave the basement behind for the last time.\n"
    else:
        truthmid "You lead, and the Princess follows, and together, you leave the basement behind for the last time.\n"
    scene farback interior cabin onlayer farback at flip, Position(ypos=1125)
    show bg cabin end reverse onlayer back at Position(ypos=1125)
    if first_princess == "stranger":
        show stranger leave ending upstairs onlayer front at Position(ypos=1125)
    else:
        show princess leave ending upstairs onlayer front at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True

    truth "It's quiet as you ascend, a comfortable silence filling a space that used to be flooded with violence and words and noisy thoughts.\n"
    truth "But there is an energy in the silence— an electricity, the anticipation of the unknown.\n"
    truth "At the top of the stairs, the Princess stalls, eyes fixed on the cabin door.\n"

    if felina_cabin_leave_hand_hold:
        if first_princess == "stranger":
            truth "You feel their hand tremble in yours. They're unsure of themselves for the first time in their long and short existence.\n"
        else:
            truth "You feel her hand tremble in yours. She's unsure of herself for the first time in her long and short existence.\n"
    else:
        if first_princess == "stranger":
            truth "You can see a tension seize them. They're unsure of themselves for the first time in their long and short existence.\n"
        else:
            truth "You can see a tension seize her. She's unsure of herself for the first time in her long and short existence.\n"
    if first_princess == "stranger":
        truth "They have no part to play anymore, and they know this. Yet they still {i}are{/i}.\n"
    else:
        truth "She has no part to play anymore, and she knows this. Yet she still {i}is{/i}.\n"

    if felina_cabin_leave_hand_hold:
        if first_princess == "stranger":
            play audio "audio/one_shot/footsteps_creaky.flac"
            show stranger leave ending upstairs cross hold onlayer front at Position(ypos=1125)
            with dissolve
            truth "And then they cross the room to the door outside, pulling you excitedly with them.\n"
        else:
            play audio "audio/one_shot/footsteps_creaky.flac"
            if first_princess == "harsh":
                show princess harsh leave ending upstairs hold onlayer front at Position(ypos=1125)
            else:
                show princess soft leave ending upstairs hold onlayer front at Position(ypos=1125)
            with dissolve
            truth "And then she crosses the room to the door outside, pulling you excitedly with her.\n"
        play audio "audio/one_shot/footsteps_creaky.flac"
    else:
        $ quick_menu = False
        play audio "audio/one_shot/footsteps_creaky.flac"
        hide farback onlayer farback
        hide bg onlayer back
        hide princess onlayer front
        hide stranger onlayer front
        with fade
        if persistent.quick_menu:
            $ quick_menu = True
        if first_princess == "stranger":
            truth "And then they cross the room to the door outside. You follow their confident steps.\n"
        else:
            truth "And then she crosses the room to the door outside. You follow her confident steps.\n"

    hide farback onlayer farback
    hide bg onlayer back
    hide princess onlayer front
    hide stranger onlayer front
    show bg leave ending door onlayer back at Position(ypos=1125)
    if first_princess == "stranger":
        show stranger leave door onlayer front at Position(ypos=1125)
    else:
        show princess leave door onlayer front at Position(ypos=1125)
    with Dissolve(1.0)
    if first_princess == "gentle":
        $ gallery_zfinale.unlock_item(9)
        $ renpy.save_persistent()
        voice "audio/voices/felina/cabin/leave/princess/1.flac"
        show princess soft leave door talk 1 onlayer front
        with dissolve
        p "Come on, Princess, it's just a door.\n"
        voice "audio/voices/felina/cabin/leave/princess/2.flac"
        show princess harsh leave door talk 3 onlayer front
        with dissolve
        p "Sorry, I'm just a little nervous. This is really it. Whatever happens next will be completely new.\n"
        #voice "audio/voices/felina/cabin/leave/princess/3.flac"
        #p "But... I think I want to see it. And I want to see it with you.\n"
    elif first_princess == "harsh":
        $ gallery_zfinale.unlock_item(9)
        $ renpy.save_persistent()
        voice "audio/voices/felina/cabin/leave/princess/4.flac"
        show princess soft leave door talk 1 onlayer front
        with dissolve
        p "This is it. I have no idea what it's going to be like out there.\n"
        voice "audio/voices/felina/cabin/leave/princess/5.flac"
        show princess harsh leave door talk 3 onlayer front
        with dissolve
        p "N-not that I'm scared or anything. It's exciting, really. Anything could happen.\n"
        voice "audio/voices/felina/cabin/leave/princess/6.flac"
        show princess leave door talk 3 onlayer front
        with dissolve
        p "And if it's bad then... It won't be bad. Not with you.\n"
    else:
        $ gallery_zfinale.unlock_item(13)
        $ renpy.save_persistent()
        voice "audio/voices/felina/cabin/leave/princess/7.flac"
        show stranger leave door talk onlayer front
        with dissolve
        p "We can feel the threads of all the stories we've told together, all pulling us back down the stairs and into those chains where we know the outcome of everything that could ever come to pass...\n"
        voice "audio/voices/felina/cabin/leave/princess/8.flac"
        show stranger leave door talk 2 onlayer front
        with dissolve
        p "It's comfortable there. But it's... confining. We want more. We want whatever might be on the other side of this door. Something new, that we'll experience together. With someone who exists outside of us.\n"
        voice "audio/voices/felina/cabin/leave/princess/9.flac"
        show stranger leave door talk 3 onlayer front
        with dissolve
        p "With someone who can see us in a way we can never see ourself.\n"
        show stranger leave door onlayer front
        with dissolve

    label felina_leave_cabin_final_menu:
        menu:
            extend ""

            "{i}• ''I love you.''{/i}":
                if first_princess == "gentle":
                    voice "audio/voices/felina/cabin/leave/princess/10.flac"
                    show princess leave door shy onlayer front
                    with dissolve
                    p "I love you, too.\n"
                elif first_princess == "harsh":
                    voice "audio/voices/felina/cabin/leave/princess/11.flac"
                    show princess leave door shy onlayer front
                    with dissolve
                    p "I... love you, too.\n"
                    voice "audio/voices/felina/cabin/leave/princess/12.flac"
                    show princess harsh leave door talk 3 onlayer front
                    with dissolve
                    p "But I'm trying not to be sappy about it! Don't make me get all emotional.\n"
                else:
                    voice "audio/voices/felina/cabin/leave/princess/13.flac"
                    show stranger leave door talk 3 onlayer front
                    with dissolve
                    p "And we love you, too.\n"
                jump felina_leave_cabin_final_join

            "{i}• ''Who's going to open it?''{/i}":
                if first_princess == "gentle":
                    voice "audio/voices/felina/cabin/leave/princess/14a.flac"
                    show princess leave door talk 3 onlayer front
                    with dissolve
                    p "Both of us, right?\n"
                elif first_princess == "harsh":
                    voice "audio/voices/felina/cabin/leave/princess/15a.flac"
                    show princess leave door talk 2 onlayer front
                    with dissolve
                    p "Both of us. Together.\n"
                else:
                    voice "audio/voices/felina/cabin/leave/princess/16.flac"
                    show stranger leave door talk 2 onlayer front
                    with dissolve
                    p "All of us.\n"
                jump felina_leave_cabin_final_join

            "{i}• ''Are you ready?''{/i}":
                if first_princess == "gentle":
                    voice "audio/voices/felina/cabin/leave/princess/17.flac"
                    show princess leave door shy onlayer front
                    with dissolve
                    p "Yeah. As ready as I'll ever be.\n"
                elif first_princess == "harsh":
                    voice "audio/voices/felina/cabin/leave/princess/18.flac"
                    show princess leave door shy onlayer front
                    with dissolve
                    p "Of course I am. Are... are you?\n"
                else:
                    voice "audio/voices/felina/cabin/leave/princess/19.flac"
                    show stranger leave door talk 2 onlayer front
                    with dissolve
                    p "It's hard to tell, with so many voices talking at once... but we're more ready than we're not.\n"
                jump felina_leave_cabin_final_join

            "{i}• ''Neither of us knows what it's going to be like out there.''{/i}":
                if first_princess == "gentle":
                    voice "audio/voices/felina/cabin/leave/princess/20.flac"
                    show princess leave door talk 2 onlayer front
                    with dissolve
                    p "And that's okay. That's the point, right? Side by side, stepping out into the unknown. Together.\n"
                elif first_princess == "harsh":
                    voice "audio/voices/felina/cabin/leave/princess/21.flac"
                    show princess leave door talk 2 onlayer front
                    with dissolve
                    p "It's something new. But whatever it is, we'll face it together.\n"
                else:
                    voice "audio/voices/felina/cabin/leave/princess/22.flac"
                    show stranger leave door talk 2 onlayer front
                    with dissolve
                    p "And that is why we're here. We can't wait to see it with you.\n"
                jump felina_leave_cabin_final_join

            "{i}• [[Open the door.]{/i}":
                label felina_leave_cabin_final_join:
                    if first_princess != "stranger":
                        show princess leave door reach onlayer front
                        with dissolve
                    else:
                        show stranger leave door final onlayer front
                        with dissolve
                    $ renpy.pause(0.25)
                    hide princess onlayer front
                    hide stranger onlayer front
                    hide bg onlayer back
                    show bg end door onlayer back at Position(ypos=1125)
                    show princess door end onlayer back at Position(ypos=1125)
                    show player door end onlayer back at Position(ypos=1125)
                    with Dissolve(1.0)
                    $ renpy.pause(0.5)
                    play audio "audio/one_shot/door_bedroom.flac"
                    show bg end door open onlayer back at Position(ypos=1125)
                    show princess door end open onlayer back at Position(ypos=1125)
                    show player door end open onlayer back at Position(ypos=1125)
                    $ renpy.pause(1.0)
                    hide player onlayer back
                    hide bg onlayer back
                    hide princess onlayer back
                    scene bg black
                    $ renpy.pause(2.0)
                    $ achievement.grant("ACH_END_CABIN")
                    $ final_ending = "leave"
                    $ gallery_zfinale.unlock_item(10)
                    $ renpy.save_persistent()
                    jump credits
                    # slam to credits
