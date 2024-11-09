label razor_2_start:
    # starting things up PLEASE note that the title card for the razor 2 doesn't pop up until you enter the basement

    stop music
    stop sound
    stop secondary
    $ default_mouse = "default"
    $ blade_held = False
    $ current_loop = 2
    $ quick_menu = False
    $ config.menu_include_disabled = False
    play sound "audio/looping/uncomfortable ambiance.ogg" loop fadein 1.0
    if razor_1_cabin_blade_taken:
        scene chapter arms with fade
        show text _("{color=#FFFFFF00}Chapter 3. The Arms Race.{/color}") at Position(ypos=850)
        $ trait_hunted = True
    else:
        scene chapter way with fade
        show text _("{color=#FFFFFF00}Chapter Three. No Way Out.{/color}") at Position(ypos=850)
        $ trait_contrarian = True
    $ renpy.pause(4.0)

    $ gallery_razor.unlock_item(6)
    $ renpy.save_persistent()
    play music "audio/_music/ch2/razor/The Razor.flac" loop
    scene farback path razor2 onlayer farback at Position(ypos=1125)
    show bg path razor2 onlayer back at Position(ypos=1125)
    show mid path razor2 onlayer front at Position(ypos=1125)
    show fore path razor2 onlayer inyourface at Position(ypos=1125)
    hide chapter
    show bg black
    hide text
    with fade
    if persistent.quick_menu:
        $ quick_menu = True

    default razor_1_mirror_interact = False
    if razor_1_cabin_mirror_ask or razor_1_cabin_mirror_approached:
        $ razor_1_mirror_interact = True
    voice "audio/voices/ch3/razor/start/narrator/1.flac"
    n "You're on a path in the woods—\n{w=1.95}{nw}"
    show screen disableclick(0.5)
    voice "audio/voices/ch3/razor/start/cheated/1.flac"
    cheated "No, fuck that! If we're going to have to keep doing this over and over and over again, we're not starting in the goddamn woods every time. We're starting in the fucking cabin.\n"
    voice "audio/voices/ch3/razor/start/narrator/2.flac"
    n "You're what?!\n{w=0.75}{nw}"
    show screen disableclick(0.5)
    $ gallery_razor.unlock_item(7)
    $ renpy.save_persistent()
    voice "audio/voices/ch3/razor/start/narrator/3.flac"
    hide farback onlayer farback
    hide bg onlayer back
    hide mid onlayer front
    hide fore onlayer inyourface
    show farback cabin razor 2 onlayer farback at Position(ypos=1125)
    show bg cabin razor 2 onlayer back at Position(ypos=1125)
    show mirror cabin razor 2 onlayer back at Position(ypos=1125)
    show knife cabin razor 2 onlayer back at Position(ypos=1125)
    n "The interior of the cabin is sharp, a constricting mess of curved and battered sheet metal pushing you towards— wait, excuse me?! What just happened? What did you just do?\n"
    voice "audio/voices/ch3/razor/start/hero/1.flac"
    hero "I feel dizzy.\n"
    voice "audio/voices/ch3/razor/start/cheated/2a.flac"
    cheated "Ohohoho. I guess I took us to the cabin, didn't I? Isn't {i}that{/i} interesting. Who holds the cards now?\n"
    #voice "audio/voices/ch3/razor/start/narrator/4.flac"
    #n "Nobody. Nobody holds the cards. That's how it's always been. That's unfortunately how reality works.\n"
    if trait_contrarian:
        voice "audio/voices/ch3/razor/start/contrarian/1.flac"
        contrarian "Who cares about cards? You're all acting like this is about winning and losing, while this is {i}actually{/i} about having fun.\n"
        if trait_broken:
            voice "audio/voices/ch3/razor/start/broken/1.flac"
            broken "Is this fun for you? It's not fun for me. I don't like being sliced to pieces.\n"
        elif trait_paranoid:
            voice "audio/voices/ch3/razor/start/paranoid/1.flac"
            paranoid "How could you care about having fun at a time like this? There is someone or something out there pulling the strings, and we're all just puppets until we can figure out how to see them.\n"

    elif trait_hunted:
        voice "audio/voices/ch3/razor/start/hunted/1.flac"
        hunted "The circle's getting smaller and smaller. Running isn't an option anymore. We have to fight.\n"
        if trait_stubborn:
            voice "audio/voices/ch3/razor/start/stubborn/1.flac"
            stubborn "Good. It's better that way. Without a fight, no one can win, and if no one can win, then nothing has any meaning.\n"
        elif trait_broken:
            voice "audio/voices/ch3/razor/start/broken/2.flac"
            broken "What's the point of fighting if she's just going to win every time? It hurts being sliced to pieces. We're better off just sitting up here and doing nothing.\n"
        elif trait_paranoid:
            voice "audio/voices/ch3/razor/start/paranoid/2.flac"
            paranoid "Yeah, but for whom? Someone or something is out there pulling the strings, and we're all just puppets until we can figure out how to see them.\n"

    if trait_paranoid:
        voice "audio/voices/ch3/razor/start/cheated/3.flac"
        cheated "But what if that someone is {i}us{/i}? Eh? Eh? Wouldn't that be neat.\n"
        voice "audio/voices/ch3/razor/start/hero/2a.flac"
        hero "If we were the ones pulling the strings, I'm pretty sure we wouldn't have died twice already.\n"

    voice "audio/voices/ch3/razor/start/narrator/5.flac"
    n "Great. So obviously you've already been here. How many times?\n"
    voice "audio/voices/ch3/razor/start/hero/3.flac"
    hero "This is our third?\n"
    voice "audio/voices/ch3/razor/start/narrator/6a.flac"
    n "No wonder things have fallen apart. You do realize that every time you fail, she escapes and an entire world is damned to destruction, right?\n"
    voice "audio/voices/ch3/razor/start/hero/4.flac"
    hero "That can't be right. That's too much responsibility!\n"
    if trait_paranoid:
        voice "audio/voices/ch3/razor/start/paranoid/3.flac"
        paranoid "It's only too much responsibility if these 'worlds' are real.\n"
    if trait_stubborn:
        voice "audio/voices/ch3/razor/start/stubborn/2.flac"
        stubborn "Nah, impossibly high stakes make the fight so much better.\n"
    if trait_broken:
        voice "audio/voices/ch3/razor/start/broken/3.flac"
        broken "I couldn't agree more. We couldn't be trusted with the fate of a single person, let alone the fate of the world.\n"
    voice "audio/voices/ch3/razor/start/narrator/7.flac"
    n "{i}Sigh{/i}. Let's just stay focused, shall we?\n"
    voice "audio/voices/ch3/razor/start/narrator/8.flac"
    n "The only furniture of note is a bent metal table, a pristine blade perched—\n{w=4.30}{nw}"
    show screen disableclick(0.5)
    voice "audio/voices/ch3/razor/start/cheated/4.flac"
    cheated "We take it.\n"
    $ blade_held = True
    $ default_mouse = "blade"
    play audio "audio/one_shot/knife_pickup.flac"
    voice "audio/voices/ch3/razor/start/narrator/9.flac"
    hide knife onlayer back
    with dissolve
    n "Okay. Sure. You take the blade before letting me finish telling you it's there. It would be difficult to slay the Princess and save the world without a weapon.\n"
    if trait_contrarian:
        voice "audio/voices/ch3/razor/start/contrarian/2.flac"
        contrarian "And then we throw it out the window!\n"
        # FAST
        voice "audio/voices/ch3/razor/start/cheated/5.flac"
        cheated "What?! That blade is the only edge we have, we are not—\n{w=2.7}{nw}"
        show screen disableclick(0.5)
        voice "audio/voices/ch3/razor/start/contrarian/3.flac"
        contrarian "Too late! Because we already did it, didn't we?\n"
        voice "audio/voices/ch3/razor/start/narrator/10.flac"
        $ blade_held = False
        $ default_mouse = "default"
        play audio "audio/final/Razor_SwordSwish_1.flac"
        n "... Unfortunately for the rest of you, and for me, and for the sake of the world... yes.\n"
        #voice "audio/voices/ch3/razor/start/narrator/11.flac"
        #n "You throw the blade at the window, glass shattering as your weapon flies out into the night. I suppose you'll just have to deal with the Princess without it.\n"
        voice "audio/voices/ch3/razor/start/cheated/6.flac"
        cheated "That is horribly unfair. He shouldn't be allowed to just do things like that.\n"
        voice "audio/voices/ch3/razor/start/contrarian/4.flac"
        contrarian "You were the one who made us pick it up! See? You're not the only one who can figure out how to do things.\n"
        voice "audio/voices/ch3/razor/start/narrator/12.flac"
        n "What's done is done. I suggest you make the best of it.\n"
        if trait_broken:
            voice "audio/voices/ch3/razor/start/broken/4a.flac"
            broken "You're all so mad at each other. I'm just going to sit here quietly in the corner. You can be the ones to figure out what to do.\n"
        if trait_paranoid:
            voice "audio/voices/ch3/razor/start/paranoid/4.flac"
            paranoid "Oh. Is this how things are going to be now? All of us vying over a single body? Fine. See this corner? It's mine. And I'd better not see any of you trying to invade my personal space.\n"
    else:
        voice "audio/voices/ch3/razor/start/hunted/2.flac"
        hunted "This feels right. We just have to keep our senses sharp.\n"
        voice "audio/voices/ch3/razor/start/cheated/7.flac"
        cheated "That's right. We've got to be able to win eventually.\n"
        if trait_broken:
            voice "audio/voices/ch3/razor/start/broken/5.flac"
            broken "And what if we never do?\n"
            #voice "audio/voices/ch3/razor/start/hero/5.flac"
            #hero "Don't be like that! I know things are hard right now, but we've got to stay positive. If they're confident, then I'm confident.\n"
        if trait_stubborn:
            voice "audio/voices/ch3/razor/start/stubborn/3.flac"
            stubborn "We {i}will{/i} win eventually. Hell, we might even win now.\n"
            voice "audio/voices/ch3/razor/start/narrator/13.flac"
            n "That's a fighting spirit I like to see. You could all learn a thing or two from this one.\n"
        elif trait_paranoid:
            voice "audio/voices/ch3/razor/start/paranoid/5a.flac"
            paranoid "What if winning is the wrong move?\n"
            voice "audio/voices/ch3/razor/start/narrator/14.flac"
            n "It isn't. I don't care whether you trust me or not, but at least trust that defeating the person who has apparently killed you twice already is a good idea.\n"
    if trait_contrarian or trait_broken:
        voice "audio/voices/ch3/razor/start/narrator/15.flac"
        n "So. Are you just going to stand there, or are you going to head to the basement like you're supposed to?\n"
    voice "audio/voices/ch3/razor/start/cheated/8.flac"
    cheated "I'd love to get started just as much as you would, but how {i}are{/i} we supposed to get down there?\n"
    voice "audio/voices/ch3/razor/start/narrator/16.flac"
    n "You walk through the door. You do know what doors are, right?\n"
    if razor_1_mirror_interact:
        voice "audio/voices/ch3/razor/start/hero/6.flac"
        hero "But there isn't a door. It's just that mirror again.\n"
    else:
        voice "audio/voices/ch3/razor/start/hero/7.flac"
        hero "But there isn't a door. There's just that mirror.\n"
    voice "audio/voices/ch3/razor/start/narrator/17.flac"
    n "There isn't a mirror. You really messed things up, didn't you? It's like you can't even see reality anymore.\n"
    if trait_paranoid:
        voice "audio/voices/ch3/razor/start/paranoid/6.flac"
        paranoid "We can see our reality just fine. Why should we trust His?\n"
    #if razor_1_mirror_interact:
    #    voice "audio/voices/ch3/razor/start/cheated/9.flac"
    #    cheated "It disappeared last time. It'll probably just disappear this time, too.\n"
    #    if trait_contrarian:
    #        voice "audio/voices/ch3/razor/start/cheated/5.flac"
    #        contrarian "And I bet it'll stay right where it is! Let's take a look.\n"
    if trait_hunted:
        voice "audio/voices/ch3/razor/start/hunted/3.flac"
        hunted "I can feel the air coming up from behind it, stinking of iron and steel. He might be right. Could be a trick. If our other senses can't feel it, then we can't trust it.\n"
    if trait_stubborn:
        voice "audio/voices/ch3/razor/start/stubborn/4.flac"
        stubborn "If it's in our way, let's just break it and move on.\n"

label razor_2_cabin_menu:
    menu:
        extend ""

        "{i}• [[Approach the mirror.]{/i}":
            $ current_run_mirror_comment = True
            voice "audio/voices/ch3/razor/start/narrator/18.flac"
            play audio "audio/final/__metal_step.flac"
            hide farback onlayer farback
            hide knife onlayer back
            hide mirror onlayer back
            hide bg onlayer back
            scene bg cabin razor 2 close closed onlayer back at Position(ypos=1125)
            show mirror cabin razor 2 close onlayer back at Position(ypos=1125)
            with Dissolve(0.5)
            n "You make your way to the door at the end of the room, stopping just in front of it. You really must think you're looking at a 'mirror.' Well, it doesn't exist. {i}Sigh.{/i} Just reach forward and open it.\n"
            if trait_broken:
                voice "audio/voices/ch3/razor/start/broken/6.flac"
                broken "Let's just move it out of the way without looking. I don't want to see us. I'm sure we all look awful after dying twice.\n"
            voice "audio/voices/ch3/razor/start/cheated/10.flac"
            cheated "Let's just fumble for the handle and be done with it, I don't care what we look like. I care about getting to the end of this mess.\n"
            menu:
                extend ""

                "{i}• [[Wipe the mirror clean.]{/i}":
                    if trait_broken:
                        voice "audio/voices/ch3/razor/start/broken/7.flac"
                        broken "{i}Long, drawn-out sigh.{/i}\n"
                    hide mirror onlayer back
                    $ renpy.pause(0.25)
                    voice "audio/voices/ch3/razor/start/narrator/19.flac"
                    play audio "audio/final/door_razor.flac"
                    show bg cabin razor 2 close open onlayer back
                    with dissolve
                    n "You reach forward and place your hand on the door to the basement. It creaks open.\n"
                    voice "audio/voices/ch3/razor/start/cheated/11.flac"
                    cheated "And the mirror's gone. How surprising.\n"
                    if trait_contrarian:
                        voice "audio/voices/ch3/razor/start/contrarian/6.flac"
                        contrarian "I can't say I was particularly invested in looking at it before, but now... now I really want to see what's in it. If it's so keen on hiding from us, whatever it has must be {i}real good{/i}.\n"
                    if trait_hunted:
                        voice "audio/voices/ch3/razor/start/hunted/4.flac"
                        hunted "It was never there. Just an illusion.\n"
                    if trait_stubborn:
                        voice "audio/voices/ch3/razor/start/stubborn/5.flac"
                        stubborn "Let's just get to the Princess already. I didn't care about the mirror before, and I care about it even less now.\n"
                    if trait_paranoid:
                        voice "audio/voices/ch3/razor/start/paranoid/7.flac"
                        paranoid "It feels like it's hiding something. It's part of the big picture, I just know it. That's why it's being kept from us.\n"
                    voice "audio/voices/ch3/razor/start/hero/8.flac"
                    hero "I guess it's time for us to see her again.\n"
                    stop music
                    voice "audio/voices/ch3/razor/start/narrator/20.flac"
                    n "Just stay focused, and you'll be fine.\n"

            $ quick_menu = False
            hide bg onlayer back
            scene bg black
            with fade
            scene bg stairs razor 2 onlayer back at Position(ypos=1125)
            with fade
            if persistent.quick_menu:
                $ quick_menu = True
            voice "audio/voices/ch3/razor/start/narrator/21.flac"
            show bg stairs razor 2 onlayer back at zoom_in
            $ renpy.pause(0.5)
            voice sustain
            hide bg onlayer back
            scene bg black
            play secondary "audio/one_shot/tower_stairs_fall.flac"
            queue secondary "audio/one_shot/tackle.flac"

            scene bg black
            n "You step forward, but you don't get a chance to linger on the basement stairs. They are smooth and flat and metallic, an unintentional and unfortunately slippery ramp that quickly sends you skittering to the bottom.\n"
            $ gallery_razor.unlock_item(8)
            $ renpy.save_persistent()
            if blade_held:
                jump razor_2_armed_start
            else:
                jump razor_2_unarmed_start
return
