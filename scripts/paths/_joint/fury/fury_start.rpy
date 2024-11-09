label fury_start:

    # starting things up

    stop music
    stop sound
    stop secondary
    $ default_mouse = "default"
    $ blade_held = False
    $ current_loop = 2
    $ quick_menu = False
    $ config.menu_include_disabled = False

    play sound "audio/looping/uncomfortable ambiance heightened.ogg" loop fadein 1.0
    scene chapter fury with fade
    show text _("{color=#FFFFFF00}Chapter Three. The Fury.{/color}") at Position(ypos=850)
    $ renpy.pause(4.0)

    play music "audio/_music/ch3/fury/The Fury INTRO.flac"
    queue music "audio/_music/ch3/fury/The Fury LOOP.flac" loop
    #play sound "audio/final/Tower_StormThunder_loop_1.ogg" loop
    play sound "audio/final/fury_ambient.ogg" loop fadein 1.0
    $ current_princess = "fury"
    $ fury_encountered = True
    # defines what route + actions bring the player to the fury - options are "tower" (only one point of entry from the tower); "pacifism" (pacifism route in adversary); "death_upstairs" (death route in adversary); "death_downstairs" (death downstairs route adversary

    default fury_source = ""
    default fury_unarmed_sub = ""

    $ gallery_fury.unlock_gallery()
    $ renpy.save_persistent()

    scene farback path fury onlayer farback at Position(ypos=1125)
    show bg path fury onlayer front at Position(ypos=1125)
    show mid path fury onlayer back at Position(ypos=1125)
    show fore path fury onlayer inyourface at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True

    # potential configurations:
    # From adversary: stubborn (always) + broken (if died in combat) or contrarian (if you did a pacifism)
    # from tower: broken + stubborn

    # relevant trait variables: trait_broken; trait_contrarian

    if fury_source == "tower":
        if tower_1_cabin_mirror_ask or tower_1_cabin_mirror_approached:
            $ fury_mirror_previous_comment_made = True
        jump fury_start_tower
    else:
        if adversary_1_cabin_mirror_ask or adversary_1_cabin_mirror_approached:
            $ fury_mirror_previous_comment_made = True
        if fury_source == "pacifism":
            jump fury_start_pacifism
        elif fury_source == "unarmed":
            jump fury_start_death_unarmed
        else:
            jump fury_start_adversary_other

label fury_start_tower:
    $ trait_stubborn = True
    $ trait_broken = True
    play secondary "audio/voices/ch3/fury/broken/fury_broken_sob.flac" loop
    broken "{i}Moaning and sobbing.{/i}\n{w=2.5}{nw}"
    show screen disableclick(0.5)
    voice "audio/voices/ch3/fury/narrator/1.flac"
    n "You're on a path in the woods, and at the end of that path— okay, what the hell is {i}that{/i}?\n"
    broken "{i}Continued sobbing.\n{/i}"
    voice "audio/voices/ch3/fury/hero/fury_hero_1a.flac"
    hero "I think he's upset.\n"
    stop secondary fadeout 3.0
    voice "audio/voices/ch3/fury/stubborn/1.flac"
    stubborn "And what's he got to be upset about? We just killed a god.\n"
    voice "audio/voices/ch3/fury/broken/fury_broken_1.flac"
    broken "Exactly! You heathens destroyed the most beautiful thing that ever was and ever will be.\n"
    #voice "audio/voices/ch3/fury/stubborn/2a.flac"
    #stubborn "You're damn right we did. And you'll get over it.\n"
    voice "audio/voices/ch3/fury/hero/fury_hero_2.flac"
    hero "I can't say I have much sympathy for you. She was bad for us, and you almost got us killed.\n"
    voice "audio/voices/ch3/fury/stubborn/3.flac"
    stubborn "You're being too generous. He did get us killed.\n"
    voice "audio/voices/ch3/fury/narrator/2.flac"
    n "All right, enough chatter. I've got a thing I'm supposed to do, and if you don't mind, I'd like to do it without any more interruptions.\n"
    voice "audio/voices/ch3/fury/narrator/3a.flac"
    n "Okay, great. You're listening. {i}Ahem.{/i} You're on a path in the woods, and at the end of that path is a—\n{w=7.3}{nw}"
    show screen disableclick(0.5)
    voice "audio/voices/ch3/fury/hero/fury_hero_3a.flac"
    hero "If your 'thing' is telling us about the Princess, don't waste your breath. We know all about her. And it's hardly a path in the woods at this point, is it?\n"
    jump fury_start_late_join

label fury_start_pacifism:
    $ trait_stubborn = True
    $ trait_cold = True
    voice "audio/voices/ch3/fury/narrator/4.flac"
    n "You're on a path in the woods, and at the end of that path—\n{w=3.5}{nw}"
    show screen disableclick(0.5)
    voice "audio/_pristine/voice/fury/cold/1.flac"
    cold "I think I've heard this one before. Does it involve a Princess? Are you trying to get us to do your dirty work?\n"
    voice "audio/_pristine/voice/fury/narrator/6.flac"
    n "... Yes. So you've been here before. And died here before.\n"
    voice "audio/_pristine/voice/fury/hero/4.flac"
    hero "... Yeah... twice.\n"
    voice "audio/_pristine/voice/fury/stubborn/8a.flac"
    stubborn "And it's going to be a lot more than that if we don't suck it up and actually fight her this time.\n"
    voice "audio/_pristine/voice/fury/narrator/7.flac"
    n "You didn't fight her.\n"
    #voice "audio/_pristine/voice/fury/hero/5.flac"
    #hero "Well, I mean. We fought her once. To the death, even!\n"
    #voice "audio/_pristine/voice/fury/narrator/8.flac"
    #n "{i}Sigh{/i}. Yours, I assume?\n"
    #voice "audio/_pristine/voice/fury/stubborn/9.flac"
    #stubborn "Ha! As if. It was mutual.\n"
    #voice "audio/_pristine/voice/fury/hero/6.flac"
    #hero "Yeah! We both died!\n"
    #voice "audio/_pristine/voice/fury/narrator/9.flac"
    #n "And then you gave up.\n"
    voice "audio/_pristine/voice/fury/cold/2.flac"
    cold "She wanted a rematch, and we wanted to see what would happen if we didn't give it to her. She got so very, very angry with us, and you got so very angry with us, too. It was amusing.\n"
    voice "audio/_pristine/voice/fury/hero/7.flac"
    hero "I'm sorry, you thought that was {i}amusing{/i}? I thought we were breaking a cycle of violence. I thought we were practicing pacifism in the face of mortal peril. I thought we were being brave. Heroic, even.\n"
    voice "audio/_pristine/voice/fury/cold/3.flac"
    cold "Oh, you're funny. There's no such thing as heroism when you can never truly die. All we did was look at the   same old thing from another angle.\n"
    #voice "audio/_pristine/voice/fury/hero/8.flac"
    #hero "Dying still hurt. You're taking away from the moment. It was a good moment.\n"
    voice "audio/_pristine/voice/fury/stubborn/10.flac"
    stubborn "Oh, will both of you just shut up?\n"
    #voice "audio/_pristine/voice/fury/narrator/10a.flac"
    #n "Finally, a voice of reason! That one has the right idea, the most important thing for all of you to do right now is to shut up and listen.\n"
    voice "audio/_pristine/voice/fury/narrator/11a.flac"
    n "{i}Sigh{/i}. As we've now established, you've already been here, and based on your behavior, I think we can all agree that things are not going well.\n"
    voice "audio/_pristine/voice/fury/narrator/9alt.flac"
    n "Look. You're nearing the point of no return. Whatever happens next, that's it, there won't be anymore 'do-overs,' so you'd better take things seriously.\n"
    jump fury_path_menu

label fury_start_death_unarmed:
    $ trait_stubborn = True
    if fury_unarmed_sub == "broken":
        $ trait_broken = True
    else:
        $ trait_contrarian = True
    voice "audio/voices/ch3/fury/narrator/4.flac"
    n "You're on a path in the woods, and at the end of that path—\n{w=3.5}{nw}"
    show screen disableclick(0.5)
    voice "audio/voices/ch3/fury/stubborn/6.flac"
    stubborn "All right! Change of plans. We're taking the blade this time.\n"
    if trait_contrarian:
        voice "audio/voices/ch3/fury/contrarian/fury_contrarian_5.flac"
        contrarian "Now why would we ever do {i}that{/i}?\n"
        voice "audio/voices/ch3/fury/hero/fury_hero_6.flac"
        hero "Because she absolutely destroyed us?\n"
        voice "audio/voices/ch3/fury/contrarian/fury_contrarian_6.flac"
        contrarian "She sure did, but what a great way to go.\n"
        if adversary_1_face_missing_explore:
            voice "audio/voices/ch3/fury/hero/fury_hero_7.flac"
            hero "We lost our face!\n"
            voice "audio/voices/ch3/fury/contrarian/fury_contrarian_7.flac"
            contrarian "Yes! It was hilarious!\n"
            voice "audio/voices/ch3/fury/hero/fury_hero_8.flac"
            hero "It was horrifying!\n"
        voice "audio/voices/ch3/fury/stubborn/7.flac"
        stubborn "Does it matter? We lost.\n"
        voice "audio/voices/ch3/fury/contrarian/fury_contrarian_8.flac"
        contrarian "Oh, why so glum, rage-boy? I thought you were brave! I thought you were proud! Or was all of that bravado just hot air?\n"
        voice "audio/voices/ch3/fury/stubborn/8.flac"
        stubborn "Look, it was just— the fight was better the first time, and the first time we had a weapon.\n"
    else:
        voice "audio/voices/ch3/fury/broken/fury_broken_2.flac"
        broken "Who cares about the blade? If we had a chance against her, we already missed it, didn't we? She got stronger, and we stayed the same.\n"
        voice "audio/voices/ch3/fury/stubborn/9.flac"
        stubborn "Last I checked she still bleeds, and that means we can still win. We just didn't take it seriously enough last time.\n"
        jump fury_death_start_join
    jump fury_start_join

label fury_start_adversary_other:
    $ trait_stubborn = True
    $ trait_broken = True
    voice "audio/voices/ch3/fury/narrator/4.flac"
    n "You're on a path in the woods, and at the end of that path—\n{w=3.5}{nw}"
    show screen disableclick(0.5)
    if adversary_1_cabin_blade_taken:
        voice "audio/voices/ch3/fury/stubborn/10a.flac"
        stubborn "All right! Change of plans. No more hesitation. No more dying. We're taking the fight straight to her.\n"
        voice "audio/voices/ch3/fury/broken/fury_broken_2a.flac"
        broken "If we had a chance against her, we already missed it, didn't we? She got stronger, and we stayed the same.\n"
    else:
        voice "audio/voices/ch3/fury/stubborn/10.flac"
        stubborn "All right! Change of plans. We're taking the blade this time, and we're not hiding upstairs.\n"
        voice "audio/voices/ch3/fury/broken/fury_broken_2.flac"
        broken "Who cares about the blade? If we had a chance against her, we already missed it, didn't we? She got stronger, and we stayed the same.\n"
    voice "audio/voices/ch3/fury/stubborn/11.flac"
    stubborn "We've seen her bleed. Whatever she is, she started out mortal, which means she probably is still mortal, which means we can win. We just didn't take things seriously enough last time.\n"
    label fury_death_start_join:
        voice "audio/voices/ch3/fury/broken/fury_broken_3.flac"
        broken "If that's what you want then fine. Enjoy being beaten to death again and again and again.\n"
        #voice "audio/voices/ch3/fury/hero/fury_hero_9.flac"
        #hero "You're stuck here with us too! For all you know, we'll never get to leave this place until we get it right.\n"

label fury_start_join:
    voice "audio/voices/ch3/fury/narrator/5a.flac"
    n "Well this is just great. {i}Sigh{/i}. Let me cut to the chase. Clearly you've already been here.\n"
    voice "audio/voices/ch3/fury/hero/fury_hero_10a.flac"
    hero "Yeah, you think?\n"
    if trait_contrarian:
        voice "audio/voices/ch3/fury/contrarian/fury_contrarian_9.flac"
        contrarian "What does 'here' even mean, though? You've told us about the path and the Princess and all of that already, but this is a very different path than the last one.\n"
    else:
        voice "audio/voices/ch3/fury/broken/fury_broken_4.flac"
        broken "Actually, I don't think we have been here.\n"
        voice "audio/voices/ch3/fury/broken/fury_broken_5.flac"
        broken "This is all different, isn't it?\n"

    if fury_source != "tower":
        voice "audio/voices/ch3/fury/hero/fury_hero_12a.flac"
        hero "That's a good point. Everything here is a little... off.\n"

    label fury_start_late_join:
        voice "audio/voices/ch3/fury/narrator/9.flac"
        n "{i}Sigh{/i}. Look. If the world around you is changing, especially all the way out here, then that means you're nearing the point of no return. Whatever happens next, that's it, there won't be anymore 'do-overs', so you'd better take things seriously.\n"

label fury_path_menu:
    default fury_path_menu_letting_on = False
    default fury_path_menu_pulled = False
    default fury_path_menu_brinksmanship = False
    menu:
        extend ""

        "{i}• (Explore) It feels like I'm being pulled in a hundred different directions. You'd better all listen to me when the time comes to make a choice.{/i}" if fury_path_menu_pulled == False:
            $ fury_path_menu_pulled = True
            if trait_broken and fury_source != "tower":
                voice "audio/_pristine/voice/extras/broken/4a.flac"
                broken "It feels like you're being pulled in a hundred different directions because we've been beaten to death twice.\n"
            if trait_contrarian:
                voice "audio/voices/ch3/fury/contrarian/fury_contrarian_13a.flac"
                contrarian "A hundred? Where are you getting that number? We're talking four, maaaaybe five directions, tops. At least for now. I'm sure I can come up with more if you give me enough time.\n"
            if fury_source == "tower":
                voice "audio/voices/ch3/fury/broken/fury_broken_10.flac"
                broken "So what if I'm speaking my mind? It's not like I've ever really gotten a say in things...\n"
                voice "audio/voices/ch3/fury/stubborn/14.flac"
                stubborn "What a crock of shit.\n"
                voice "audio/voices/ch3/fury/hero/fury_hero_17.flac"
                hero "Yeah! You stabbed us last time. Repeatedly.\n"
                voice "audio/voices/ch3/fury/broken/fury_broken_11a.flac"
                broken "It didn't even work. It doesn't count.\n"
                voice "audio/voices/ch3/fury/stubborn/15.flac"
                stubborn "We died!\n"
                voice "audio/voices/ch3/fury/hero/fury_hero_18.flac"
                hero "If you didn't submit to her, for all we know, that wouldn't have happened.\n"
                voice "audio/voices/ch3/fury/broken/fury_broken_12.flac"
                broken "It's the punishment you all deserved for not listening to me. To {i}her{/i}.\n"
                voice "audio/voices/ch3/fury/hero/fury_hero_19.flac"
                hero "Aside from our sulking friend, I don't think you have much to worry about. You're still the one in charge here, and I don't think that's ever going to change.\n"
                voice "audio/voices/ch3/fury/stubborn/17.flac"
                stubborn "The second he tries something, I'll put a stop to it.\n"
            elif trait_cold:
                voice "audio/_pristine/voice/fury/cold/4.flac"
                cold "I've never made you do anything you didn't want to do yourself. It'll be interesting to see what's happened to her. She was so fiery last time... I wonder if we've managed to douse that flame.\n"
                voice "audio/_pristine/voice/fury/stubborn/11.flac"
                stubborn "You'd better hope not. I liked her spark.\n"
                voice "audio/_pristine/voice/fury/cold/5.flac"
                cold "'Hope not?' Is that some kind of threat? What could you possibly do to me?\n"
                voice "audio/_pristine/voice/fury/stubborn/12.flac"
                stubborn "Wouldn't you like to find out, you chilly little freak!\n"
                voice "audio/_pristine/voice/fury/hero/9.flac"
                hero "Come on, let's not fight. We've done enough of that already.\n"
            else:
                voice "audio/voices/ch3/fury/hero/fury_hero_20.flac"
                hero "I don't think you have much to worry about. You're still the one in charge here, and I don't think that's ever going to change.\n"

            jump fury_path_menu

        "{i}• (Explore) If we hit this 'point of no return' you mentioned... then what happens?{/i}" if fury_path_menu_brinksmanship == False:
            $ fury_path_menu_brinksmanship = True
            voice "audio/voices/ch3/fury/narrator/17.flac"
            n "'Then what happens?' Have you even been listening? It's the end is what happens.\n"
            voice "audio/voices/ch3/fury/hero/fury_hero_21a.flac"
            hero "Yeah, but is there something... after the end?\n"
            voice "audio/voices/ch3/fury/narrator/18.flac"
            n "How am I supposed to know? The end means finality. It's not like I can just peek on over to the other side and tell you what it's like there. If there even is a there.\n"
            if trait_contrarian:
                voice "audio/voices/ch3/fury/contrarian/fury_contrarian_14a.flac"
                contrarian "Isn't it your job to know things? Maybe we need a better Narrator who can actually answer our questions...\n"
                voice "audio/voices/ch3/fury/narrator/19.flac"
                n "It's my job to guide you through your task and to state the facts of what's happening. That hardly requires omniscience, and besides, I'm the best you're going to get, because I'm the only one here who can do my job.\n"
            elif trait_cold:
                voice "audio/_pristine/voice/fury/cold/6.flac"
                cold "We've seen the 'other side,' and if you'd really like to know, there's nothing there. A pause. A breath. And then we're back in the woods again.\n"
                voice "audio/_pristine/voice/fury/narrator/13.flac"
                n "Good for you. But your opinion on the matter doesn't count.\n"
                voice "audio/_pristine/voice/fury/cold/7.flac"
                cold "How convenient. As soon as you get an answer to life's great mysteries, it doesn't count.\n"
                voice "audio/_pristine/voice/fury/narrator/14.flac"
                n "{i}Sigh{/i}. Moving on.\n"
            else:
                voice "audio/voices/ch3/fury/stubborn/18a.flac"
                stubborn "It doesn't matter, because we're going to win.\n"
                voice "audio/voices/ch3/fury/narrator/20.flac"
                n "Now that's exactly the sort of mindset I like to see. Don't let yourself be consumed with self-doubt. Don't flirt with oblivion. Just focus on the present, and everything will be absolutely fine.\n"
            jump fury_path_menu

        "{i}• No matter what happens next, it seems like our answers are at the cabin. We might as well see this through. [[Proceed to the cabin.]{/i}":
            jump fury_cabin_exterior

        "{i}• [[Silently proceed to the cabin.]{/i}":
            jump fury_cabin_exterior

        "{i}• I'm done with this. Bye! [[Turn around and leave.]{/i}" if mound_can_attempt_flee:
            if loops_finished >= 2:
                $ mound_can_attempt_flee = False
                voice "audio/voices/mound/bonus/flee.flac"
                mound "You have already committed to my completion. You cannot go further astray.\n"
                jump fury_path_menu
            $ caught_origin_current = "fury"
            $ caught_origin_ch3 = True
            if trait_contrarian:
                voice "audio/voices/ch3/fury/contrarian/fury_contrarian_15.flac"
                contrarian "Hahaha! Yessssss, here we go!\n"
            voice "audio/voices/ch3/fury/narrator/21.flac"
            n "Are you serious?! Fine. You walk away from the cabin. Let's see how that goes for you.\n" id fury_path_menu_1bb55469
            jump caught_start


label fury_cabin_exterior:

    play audio "audio/final/fury_ext_walk.flac"
    $ quick_menu = False
    hide farback onlayer farback
    hide bg onlayer front
    hide mid onlayer back
    hide bg onlayer back
    hide fore onlayer front
    hide fore onlayer inyourface
    hide stars onlayer farback
    hide back onlayer back
    hide mid onlayer front
    scene bg black
    with fade

    show farback exterior fury onlayer farback at Position(ypos=1125)
    show bg cabin exterior fury onlayer back at Position(ypos=1125)
    show mid cabin exterior fury closed onlayer front at Position(ypos=1125)
    show fore cabin exterior fury onlayer inyourface at Position(ypos=1125)
    with fade

    if persistent.quick_menu:
        $ quick_menu = True
    voice "audio/voices/ch3/fury/narrator/22.flac"
    n "Good. We're all on the same page.\n"

    # go to cabin
    voice "audio/voices/ch3/fury/narrator/23.flac"
    n "It isn't long before you find yourself at the end of the path, staring up at the cabin on the hill. You'll find the Princess within, as I'm sure you already know. End her.\n"
    voice "audio/voices/ch3/fury/hero/fury_hero_22.flac"
    hero "That's it? No final words of advice?\n"
    voice "audio/voices/ch3/fury/narrator/24.flac"
    n "I'd rather not waste any more time. I'm sure that... any advice I'd give at this point is something you've already heard.\n"
    if trait_contrarian:
        voice "audio/voices/ch3/fury/contrarian/fury_contrarian_16.flac"
        contrarian "Don't be so hard on yourself. We all wind up in creative ruts now and then. I'm sure if you put your mind to it you could think of something worth telling us.\n"
    elif fury_source == "tower":
        voice "audio/voices/ch3/fury/broken/fury_broken_6a.flac"
        broken "If there's still a Princess at the cabin, maybe we can salvage things. Maybe if we just grovel and apologize things can go back to how they were before.\n"
        voice "audio/voices/ch3/fury/stubborn/13.flac"
        stubborn "Oh, cut it out, will you? We need to be tough right now, and you're making it so much harder than it has to be. So stop whining.\n"
    else:
        voice "audio/voices/ch3/fury/stubborn/19.flac"
        stubborn "That's fine by me. Let's get moving, I'm itching for a rematch.\n"
    menu:
        extend ""

        "{i}• [[Proceed into the cabin.]{/i}":
            play tertiary "audio/one_shot/door_bedroom.flac"
            queue tertiary "audio/final/fury_ext_walk.flac"
            show mid cabin exterior fury open onlayer front
            $ renpy.pause(0.1)
            $ quick_menu = False
            hide farback onlayer farback
            hide bg onlayer back
            hide mid onlayer front
            hide fore onlayer inyourface
            scene bg black
            with fade
            jump fury_cabin_interior

label fury_cabin_interior:
    $ gallery_fury.unlock_item(1)
    $ renpy.save_persistent()
    scene farback cabin fury onlayer farback at Position(ypos=1125)
    show bg cabin fury onlayer back at Position(ypos=1125)
    show door cabin fury onlayer back at Position(ypos=1125)
    show table cabin fury onlayer back at Position(ypos=1125)
    show knife cabin fury onlayer back at Position(ypos=1125)
    show mirror cabin fury onlayer back at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    voice "audio/voices/ch3/fury/narrator/25.flac"
    n "The interior of the cabin is a place that feels long forgotten. There was once an elegance to its construction, carved marble columns holding a high-arched roof, vaulted windows letting in the weak starlight.\n"
    voice "audio/voices/ch3/fury/narrator/26.flac"
    n "But that is how it was. Now, there is a growth that has overtaken it. A viscous fluid seeps from cracks in the stone walls, and it congeals into chaotic streaks of writhing nerves and wet clumps of living meat.\n"
    voice "audio/voices/ch3/fury/hero/fury_hero_backup1.flac"
    hero "That's horrible.\n"
    if fury_source == "tower":
        voice "audio/voices/ch3/fury/broken/fury_broken_backup1.flac"
        broken "You did this.\n"
    elif trait_contrarian:
        voice "audio/voices/ch3/fury/contrarian/backup.flac"
        contrarian "I think it's kind of nice. Makes the room feel alive, doesn't it?\n"
    elif trait_cold:
        voice "audio/_pristine/voice/fury/cold/8.flac"
        cold "It's just meat. If you cut us open, I'm sure we'd look the same inside.\n"
        voice "audio/_pristine/voice/fury/hero/10.flac"
        hero "That's {i}why{/i} it's horrible.\n"
        voice "audio/_pristine/voice/fury/cold/9.flac"
        cold "And that attitude is why you're miserable.\n"
    else:
        voice "audio/voices/ch3/fury/stubborn/20.flac"
        stubborn "It doesn't matter.\n"
    #n "But all of it has fallen to ruin. The columns have cracked. The ceiling has fallen away, exposing the space within to the harsh and uncaring world beyond.\n"
    voice "audio/voices/ch3/fury/narrator/27.flac"
    n "The only furniture of note is a pulsating pedestal, a pristine blade perched on its edge.\n"
    voice "audio/voices/ch3/fury/narrator/28.flac"
    n "The blade is your implement. You'll need it if you want to do this right.\n"
    if trait_contrarian:
        voice "audio/voices/ch3/fury/contrarian/fury_contrarian_17.flac"
        contrarian "We'll need it if we want to do things 'right'. I say we leave it to rust.\n"
        if adversary_1_cabin_blade_taken == False:
            voice "audio/voices/ch3/fury/stubborn/21.flac"
            stubborn "Let's not make the same mistake twice. We could have won if we had it last time. Take it.\n"
        else:
            voice "audio/voices/ch3/fury/stubborn/22.flac"
            stubborn "Take it. We're going into this prepared.\n"
    label fury_cabin_interior_menu:
        default fury_mirror_previous_comment_made = False
        default fury_mirror_comment = False
        default fury_blade_taken = False
        menu:

            extend ""

            "{i}• (Explore) It's that mirror again. And this time it's blocking the door.{/i}" if fury_mirror_comment == False:
                jump fury_no_door_join

            "{i}• (Explore) You didn't mention the mirror last time either. Why?{/i}" if fury_mirror_comment == False:
                jump fury_no_door_join

            "{i}• (Explore) How are we supposed to get to the basement. There's no door. There's just a mirror where the door used to be.{/i}" if fury_mirror_comment == False:
                label fury_no_door_join:
                    $ fury_mirror_comment = True
                    if current_run_mirror_comment:
                        voice "audio/voices/ch3/fury/narrator/29.flac"
                        n "A mirror? There is no mirror. There's—\n{w=2.7}{nw}"
                        show screen disableclick(0.5)
                        if trait_contrarian:
                            if blade_held == False:
                                voice "audio/voices/ch3/fury/contrarian/fury_contrarian_18.flac"
                                contrarian "'The pedestal, the blade sitting on the pedestal, and the door to the basement.' Yeah, we've done all this already.\n"
                            else:
                                voice "audio/voices/ch3/fury/contrarian/fury_contrarian_19.flac"
                                contrarian "'The pedestal and the door to the basement.' Yeah, we've done all this already.\n"

                        else:
                            voice "audio/voices/ch3/fury/stubborn/23.flac"
                            stubborn "We've done this already, try to keep up. The repetition is maddening.\n"
                            if trait_cold:
                                voice "audio/_pristine/voice/fury/cold/10.flac"
                                cold "Oh, you're so impatient. We can look around the meat shack if we want to. It's not like the Princess will be leaving without us.\n"

                    else:
                        if blade_held == False:
                            voice "audio/voices/ch3/fury/narrator/30.flac"
                            n "A mirror? There is no mirror. There's the pedestal, the blade sitting on the pedestal, and the door to the basement.\n"
                        else:
                            voice "audio/voices/ch3/fury/narrator/31.flac"
                            n "A mirror? There is no mirror. There's the pedestal and the door to the basement.\n"
                        if trait_contrarian:
                            voice "audio/voices/ch3/fury/contrarian/fury_contrarian_20.flac"
                            contrarian "Oh, are we playing a game where we lie to people about things? That sounds fun! I respect and admire all of you, and I'm so happy to be here.\n"
                            voice "audio/voices/ch3/fury/narrator/32.flac"
                            n "What?\n"
                            voice "audio/voices/ch3/fury/hero/fury_hero_23.flac"
                            hero "There's clearly a mirror.\n"
                        else:
                            voice "audio/voices/ch3/fury/stubborn/24.flac"
                            stubborn "Just tell us where the door is. I'd like to get back to fighting, and if you want us to kill her so bad I'm sure you feel the same. No more messing around.\n"
                            if trait_cold:
                                voice "audio/_pristine/voice/fury/cold/10.flac"
                                cold "Oh, you're so impatient. We can look around the meat shack if we want to. It's not like the Princess will be leaving without us.\n"
                    voice "audio/voices/ch3/fury/narrator/33.flac"
                    n "{i}Sigh{/i}. I don't know what to tell you! There isn't a mirror, because I would know if there was a mirror. You're either seeing things or you're confused on the definitions of 'door' and 'mirror'. Or you're seeing things. That seems far more likely.\n"
                    voice "audio/voices/ch3/fury/stubborn/25.flac"
                    stubborn "What are you trying to say, exactly?\n"
                    if trait_broken:
                        voice "audio/voices/ch3/fury/broken/fury_broken_13.flac"
                        broken "He thinks we've lost it. That we're succumbing to madness. That something in us has... broken.\n"
                        voice "audio/voices/ch3/fury/narrator/34.flac"
                        n "That's an unnecessarily melodramatic way to describe a hallucination, but sure. I'm not going to waste time arguing with any of you.\n"
                    else:
                        voice "audio/voices/ch3/fury/narrator/35.flac"
                        n "It means you're hallucinating.\n"
                    if current_run_mirror_touched:
                        voice "audio/voices/ch3/fury/hero/fury_hero_24.flac"
                        hero "It went away when we touched it last time. Let's just do it again.\n"
                    else:
                        voice "audio/voices/ch3/fury/stubborn/26.flac"
                        stubborn "It's in our way. Let's just smash it.\n"
                    jump fury_cabin_interior_menu

            "{i}• (Explore) [[Take the blade.]{/i}" if fury_blade_taken == False:
                $ fury_blade_taken = True
                $ blade_held = True
                $ default_mouse = "blade"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_38.flac"
                play audio "audio/one_shot/knife_pickup.flac"
                hide knife onlayer back
                with dissolve
                voice "audio/voices/ch3/fury/narrator/36.flac"
                n "You take the blade from the pedestal. It would be difficult to slay the Princess and save the world without a weapon.\n"
                voice "audio/voices/ch3/fury/stubborn/27.flac"
                stubborn "Good. Nothing feels better than gripping cold steel.\n"
                if trait_contrarian:
                    voice "audio/_pristine/voice/fury/contrarian/1.flac"
                    contrarian "Okay, okay. You picked up the blade. That's fine. But we're not taking it with us.\n"
                    voice "audio/_pristine/voice/fury/narrator/1.flac"
                    n "Oh? And what do you plan to do with it then?\n"
                    voice "audio/_pristine/voice/fury/contrarian/2.flac"
                    contrarian "Oh, I dunno. We... throw it out the window!\n"
                    voice "audio/_pristine/voice/fury/stubborn/1.flac"
                    stubborn "Hell no.\n"
                    voice "audio/_pristine/voice/fury/hero/1.flac"
                    hero "Yeah... what if we need it?\n"
                    voice "audio/_pristine/voice/fury/contrarian/3a.flac"
                    contrarian "Psht. We don't need it! We had her up against the ropes last time.\n"
                    voice "audio/_pristine/voice/fury/hero/2.flac"
                    hero "Did we?\n"
                    voice "audio/_pristine/voice/fury/stubborn/2.flac"
                    stubborn "{i}Angry grumbling.{/i} We were doing great. But a weapon would have been useful.\n"
                    voice "audio/_pristine/voice/fury/contrarian/4.flac"
                    contrarian "Are you saying that you don't think we can win this fair and square?\n"
                    voice "audio/_pristine/voice/fury/stubborn/3.flac"
                    stubborn "No, I'm just—\n"
                    voice "audio/_pristine/voice/fury/contrarian/5.flac"
                    contrarian "Because it sounds to me like you don't think we can win this fair and square.\n"
                    voice "audio/_pristine/voice/fury/stubborn/4.flac"
                    stubborn "You know what, fine! I'm with him! We started round two with our fists, and that's how we're going to end this.\n"
                    voice "audio/_pristine/voice/fury/stubborn/5.flac"
                    stubborn "You! Annoying one who keeps telling us what to do! We throw the blade out the window.\n"
                    voice "audio/_pristine/voice/fury/narrator/2.flac"
                    n "Are you serious?!\n"
                    voice "audio/_pristine/voice/fury/hero/3.flac"
                    hero "Can we do that?\n"
                    voice "audio/_pristine/voice/fury/stubborn/6.flac"
                    stubborn "It's already done, isn't it?\n"
                    voice "audio/_pristine/voice/fury/contrarian/6.flac"
                    contrarian "Yeah. And now you have to describe it to us!\n"
                    $ blade_held = False
                    $ default_mouse = "default"
                    play audio "audio/final/Razor_SwordSwish_1.flac"
                    voice "audio/_pristine/voice/fury/narrator/3.flac"
                    n "{i}Sigh.{/i} Fine. With an unceremonious 'whoosh,' the pristine blade flies out into the night, never to be seen again.\n" id fury_no_door_join_f7281a65
                    voice "audio/_pristine/voice/fury/narrator/4a.flac"
                    n "Your destiny, and the destiny of the entire world, awaits. Best of luck. You're going to need it.\n"

                    menu:
                        extend ""

                        "{i}• ''No. We absolutely did not throw the blade out the window.''{/i}":
                            voice "audio/_pristine/voice/fury/contrarian/7.flac"
                            contrarian "I dunno. It sounds like we did!\n"
                            voice "audio/_pristine/voice/fury/narrator/5.flac"
                            n "Yes. Unfortunately, you did.\n"
                            jump fury_pristine_toss_join

                        "{i}• ''Hey, I thought I was the one who made the decisions around here.''{/i}":
                            voice "audio/_pristine/voice/fury/contrarian/8a.flac"
                            contrarian "It sounds to me like you're not! How fun!\n"
                            jump fury_pristine_toss_join

                        "{i}• ''So, what, you can all just override me now?''{/i}":
                            voice "audio/_pristine/voice/fury/contrarian/9.flac"
                            contrarian "I guess we can. So you'd better watch out!\n"
                            label fury_pristine_toss_join:
                                voice "audio/_pristine/voice/fury/stubborn/7.flac"
                                stubborn "Let's just get on with it. I'm itching for that rematch.\n"

                        "{i}• Hell yeah, that kicked ass. Love when my tenants throw things out of windows when I'm not paying attention.{/i}":
                            jump fury_pristine_toss_join

                        "{i}• [[Let it go.]{/i}":
                            jump fury_pristine_toss_join

                jump fury_cabin_interior_menu

            "{i}• [[Approach the mirror.]{/i}":
                play audio "audio/one_shot/footsteps_stone.flac"
                hide farback onlayer farback
                hide bg onlayer back
                hide table onlayer back
                hide knife onlayer back
                hide mirror onlayer back
                hide door onlayer back
                show bg cabin fury close onlayer back at Position(ypos=1125)
                show door cabin fury close onlayer back at Position(ypos=1125)
                show mirror cabin fury close onlayer back at Position(ypos=1125)
                with fade
                if fury_mirror_comment:
                    voice "audio/voices/ch3/fury/narrator/37.flac"
                    n "You step forward and approach the door to the basement, hesitating before you open it. As if you don't see it. You really don't do you? How strange.\n"
                else:
                    voice "audio/voices/ch3/fury/narrator/38.flac"
                    n "You step forward and approach the door to the basement, hesitating before you open it. Almost as if you don't see it. But you must, because it's right there in front of you.\n"
                    voice "audio/voices/ch3/fury/stubborn/29.flac"
                    stubborn "All we see is a damned mirror.\n"
                if current_run_mirror_touched:
                    voice "audio/voices/ch3/fury/hero/fury_hero_26.flac"
                    hero "It really is just like last time. Are we really hallucinating? Why here? Why now?\n"
                else:
                    voice "audio/voices/ch3/fury/hero/fury_hero_27.flac"
                    hero "It's a bit grimy. Why don't we wipe it clean?\n"
                    if fury_mirror_comment:
                        voice "audio/voices/ch3/fury/narrator/39.flac"
                        n "Wipe what clean? Are you still on about that mirror? It's not real. I'd know about it if it were real.\n"
                        voice "audio/voices/ch3/fury/hero/fury_hero_28.flac"
                        hero "No! We can't doubt our eyes like that. It has to be real.\n"
                    else:
                        voice "audio/voices/ch3/fury/narrator/40.flac"
                        n "Wipe what clean, the door?\n"
                        voice "audio/voices/ch3/fury/hero/fury_hero_29.flac"
                        hero "The mirror.\n"
                        voice "audio/voices/ch3/fury/narrator/41.flac"
                        n "What are you talking about? You're standing in front of a door. Whatever non-door thing you think you're looking at, it isn't real, because if it were real, I'd know about it.\n"
                        voice "audio/voices/ch3/fury/hero/fury_hero_30a.flac"
                        hero "But it has to be real. It's right there!\n"
                if fury_source == "tower":
                    voice "audio/voices/ch3/fury/broken/fury_broken_14a.flac"
                    broken "Smash it. Smash it to pieces. It's the only thing keeping us from Her.\n"
                    voice "audio/voices/ch3/fury/hero/fury_hero_31.flac"
                    hero "Don't you want to know what we'll see in there? We won't be able to see anything if we smash it.\n"
                    voice "audio/voices/ch3/fury/stubborn/30.flac"
                    stubborn "Nah, I'm with him on this one. Smash it! Let's get violent already!\n"
                else:
                    if trait_contrarian:
                        voice "audio/voices/ch3/fury/contrarian/23a.flac"
                        contrarian "Does it matter if it's actually real or not? Talking about it gets under His skin, and that's all that matters. We should talk about it even more.\n"
                    voice "audio/voices/ch3/fury/stubborn/31.flac"
                    stubborn "Let's just smash it and get it over with. I'm ready to get violent!\n"
                    voice "audio/voices/ch3/fury/hero/fury_hero_32.flac"
                    hero "We won't be able to see what's in there if we smash it...\n"
                    if trait_cold:
                        voice "audio/_pristine/voice/fury/cold/11.flac"
                        cold "It's just a mirror. What we do with it doesn't really matter.\n"

                $ current_run_mirror_touched = True
                voice "audio/voices/ch3/fury/narrator/42.flac"
                n "Do whatever you want with it. The mirror isn't real, so how you handle it doesn't matter aside from wasting dangerous amounts of time.\n"
                menu:
                    extend ""

                    "{i}• [[Wipe the mirror clean.]{/i}":
                        voice "audio/voices/ch3/fury/narrator/43.flac"
                        hide mirror onlayer back
                        play audio "audio/one_shot/new/STP_claws_1.flac"
                        #show player wall onlayer front at Position(ypos=1125) with dissolve
                        n "You reach forward and drag your hand across the door leading to the basement.\n"
                        voice "audio/voices/ch3/fury/narrator/43a.flac"
                        play audio "audio/one_shot/door_stone.flac"
                        show door cabin fury close open onlayer back
                        with dissolve
                        $ renpy.pause(0.25)
                        voice sustain
                        hide player onlayer back
                        hide door onlayer back
                        with dissolve
                        n "As if on command, it slowly slides open, scraping against the stone floor, its ancient hinges moaning as it reveals the dim path ahead.\n"

                    "{i}• [[Smash it.]{/i}":
                        voice "audio/voices/ch3/fury/narrator/44.flac"
                        hide mirror onlayer back
                        $ renpy.pause(0.1)
                        voice sustain
                        show player den close onlayer front at Position(ypos=1125)
                        with dissolve
                        play audio "audio/one_shot/thump_6.flac"
                        n "You bring your fist crashing down against the door leading to the basement.\n"
                        #voice "audio/voices/ch3/fury/narrator/44a.flac"
                        voice "audio/voices/ch3/fury/narrator/43a.flac"
                        play audio "audio/one_shot/door_stone.flac"
                        show door cabin fury close open onlayer back
                        with dissolve
                        $ renpy.pause(0.25)
                        voice sustain
                        hide player onlayer back
                        hide door onlayer back
                        with dissolve
                        n "As if on command, it slowly slides open, scraping against the stone floor, its ancient hinges moaning as it reveals the dim path ahead.\n"

                if current_run_mirror_touched:
                    voice "audio/voices/ch3/fury/hero/fury_hero_33.flac"
                    hero "Why am I not surprised...\n"
                else:
                    voice "audio/voices/ch3/fury/hero/fury_hero_34.flac"
                    hero "It's gone... Why is it gone?\n"
                    voice "audio/voices/ch3/fury/stubborn/32.flac"
                    stubborn "It was in our way and now it isn't. That's all that matters.\n"
                $ quick_menu = False
                voice "audio/voices/ch3/fury/narrator/45.flac"
                play audio "audio/one_shot/footsteps_stone.flac"
                hide player onlayer front
                hide door onlayer back
                hide bg onlayer back
                scene bg black
                with fade
                n "You step forward into the darkness.\n"


label fury_stairs:
    voice "audio/voices/ch3/fury/narrator/46.flac"
    scene bg stairs fury onlayer back at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    n "The stairs leading down to the basement are at once both narrow and grandiose. A high-vaulted ceiling stretches up into a gloom beyond your sight while walls wet with tumorous growths press in uncomfortably at your sides. You feel both unprotected and trapped, at once exposed and claustrophobic.\n"
    voice "audio/voices/ch3/fury/narrator/47.flac"
    n "The air is thick, its odor an oppressive violence — the metallic scent of fresh blood twisting with the nauseating embers of charred remains. If the Princess lives here, slaying her is probably doing her a favor.\n"
    voice "audio/voices/ch3/fury/narrator/48.flac"
    n "Her voice—a bellowing rage—roars up the stairs.\n"
    if fury_source == "tower":
        voice "audio/voices/ch3/fury/princess/1a.flac"
        sp "Was severing the tendons of my ascension not enough for you? Was it not enough to rend my divine heart?\n"
        voice "audio/voices/ch3/fury/princess/2.flac"
        sp "Come! See the horrors you've wrought upon my flesh and feel my hands set upon your throat!\n"
        voice "audio/_pristine/voice/fury/princess/5.flac"
        sp "See how you've soured my once divine melody.\n"
        voice "audio/voices/ch3/fury/broken/fury_broken_15.flac"
        broken "She's so angry with us... why, why did you desecrate her? Why couldn't I stop you?\n"
        voice "audio/voices/ch3/fury/hero/fury_hero_35.flac"
        hero "You've got to stop thinking about her like that, it isn't doing anyone any good.\n"
        voice "audio/voices/ch3/fury/stubborn/33.flac"
        stubborn "She's not some untouchable God, she's an abomination, and we're going to put an end to her once and for all.\n"
        voice "audio/voices/ch3/fury/broken/fury_broken_16.flac"
        broken "Whatever she is now is our fault. If she's an abomination, then what does that make us?\n"
        if tower_self_knowledge:
            voice "audio/voices/ch3/fury/hero/fury_hero_36.flac"
            hero "She was going to end the world last time!\n"
        else:
            voice "audio/voices/ch3/fury/stubborn/34.flac"
            stubborn "It doesn't matter what we are. She needs slaying, and we've got the means to do it, so let's get a move on!\n"
        voice "audio/voices/ch3/fury/narrator/49.flac"
        n "If I might interject, you didn't make her into an abomination. She's always been what she is. It's why you're here, and it's why your task is so important.\n"

    elif fury_source == "pacifism" or fury_source == "death_downstairs":
        voice "audio/voices/ch3/fury/princess/3.flac"
        sp "So you've returned after denying me the salvation of combat? Are you here to gloat? Are you here to mock what I've become?\n"
        voice "audio/voices/ch3/fury/princess/3aa.flac"
        sp "Do you think that if you let me kill you enough times, I'll suddenly soften and repent for sins that live solely in your head?\n"
        voice "audio/voices/ch3/fury/princess/4.flac"
        sp "Well, we've tried that, haven't we? Now come down and see what your refusal has done to me. See how much you can bear to witness the consequences of your actions.\n"
        if trait_contrarian:
            voice "audio/voices/ch3/fury/contrarian/fury_contrarian_24.flac"
            contrarian "Do you hear that? Sounds like we got to her last time. Let's keep pushing, see what else we can make happen.\n"
        elif trait_cold:
            voice "audio/_pristine/voice/fury/cold/12.flac"
            cold "Oh, we've changed her, have we? I'm intrigued.\n"
        if trait_broken:
            jump fury_broken_intro

    else:
        if fury_source == "unarmed" or fury_unarmed_sub == "broken":
            voice "audio/voices/ch3/fury/princess/5.flac"
            sp "So you've returned. Do you intend to weakly claw your fingers across my skin? Or have you finally decided to try and kill me properly?\n"
            voice "audio/voices/ch3/fury/princess/6.flac"
            sp "I think you'll find it won't be so simple. I've... changed. The way your flesh felt grinding beneath my fist... it woke something in me.\n"
        else:
            voice "audio/voices/ch3/fury/princess/7.flac"
            sp "And so you've returned. Do you intend to cower and hide again? Or have you finally decided to try and kill me?\n"
            voice "audio/voices/ch3/fury/princess/8.flac"
            sp "I think you'll find it won't be so simple. I've... changed. The way your body broke and bled against the walls of this temple... it woke something in me.\n"
        voice "audio/_pristine/voice/fury/princess/2a.flac"
        sp "A fight is a song, but there was no music in our conflict. There was no beauty in what we did to each other. And now there is no beauty in me. Come down and see what you've done.\n"
        if trait_broken:
            label fury_broken_intro:
                voice "audio/_pristine/voice/extras/broken/1.flac"
                broken "It cuts both ways. We've both hurt each other.\n"


        else:
            voice "audio/voices/ch3/fury/contrarian/fury_contrarian_24.flac"
            contrarian "Do you hear that? Sounds like we got to her last time. Let's keep pushing, see what else we can make happen.\n"

    menu:
        extend ""

        "{i}• [[Continue down the stairs.]{/i}":
            $ quick_menu = False
            voice "audio/voices/ch3/fury/narrator/50.flac"
            hide bg onlayer back
            scene bg black
            with fade
            n "You make your way to the bottom of the stairs.\n"
            $ gallery_fury.unlock_item(2)
            $ renpy.save_persistent()
            voice "audio/voices/ch3/fury/narrator/51.flac"
            play tertiary "audio/final/fury_heart_loop.ogg" loop
            scene farback basement fury onlayer farback at Position(ypos=1150)
            show bg fury basement nochains onlayer back at Position(ypos=1150)
            show fury d neutral onlayer back at Position(ypos=1150)
            show fore fury basement onlayer front at Position(ypos=1150)
            with fade
            if persistent.quick_menu:
                $ quick_menu = True
            n "The chamber's walls are painted in blood, a deep sickening red that drips down in clotted streams onto the charred corpses that make up its floor. This place reeks of torment, of ripped skin and burning bone.\n"


    $ achievement.grant("ACH_FURY_END")
    voice "audio/voices/ch3/fury/narrator/52.flac"
    n "The Princess stands in its center, muscles flayed and bare and weeping, draped in a tattered dress of her own skin. Her heart beats from its place in her open chest.\n"
    if trait_broken and fury_source != "tower":
        voice "audio/_pristine/voice/extras/broken/5.flac"
        broken "She's been hollowed out. Just like us.\n"
    voice "audio/voices/ch3/fury/princess/10.flac"
    sp "Do you know what I'm going to do to you?\n"
    voice "audio/voices/ch3/fury/narrator/53.flac"
    #play audio "audio/final/Fury_AMetalCuffCuttingInto_1.flac"
    play audio "audio/final/fury_walk_short.flac"
    play secondary "audio/final/fury_approach_ouch.flac"
    #hide farback onlayer farback
    hide fury onlayer back
    show bg fury basement nochains onlayer back
    show fury d step onlayer back at Position(ypos=1150) with hpunch
    with dissolve
    n "There's not so much a moment of hesitation before she steps forward. Her chains pull taut, holding fast as she strains against them. The cuff around her wrist digs deeper into her skin. Blood drips from the place where metal meets flesh.\n" id fury_broken_intro_c0c65b38
    voice "audio/voices/ch3/fury/narrator/54.flac"
    play audio "audio/final/Fury_DeglovingSHORTER_2.flac"
    show fury d deglove1 onlayer back
    with Dissolve(1.0)
    $ renpy.pause(0.5)
    voice sustain
    show fury d deglove2 onlayer back
    with Dissolve(1.0)
    $ renpy.pause(0.5)
    voice sustain
    play audio "audio/final/Spectre_HeartCrush_2 copy.flac"
    hide fury onlayer back
    show chain fury deglove onlayer back at Position(ypos=1150)
    show fury d deglove3 onlayer back at Position(ypos=1150)
    with dissolve
    n "And then, with a nauseating sound, the skin tears. It plops to the ground, and she pulls her red, glistening arm free from her bindings.\n"
    voice "audio/voices/ch3/fury/narrator/55.flac"
    play audio "audio/final/fury_walk_single.flac"
    show fury d approach onlayer back with hpunch
    with dissolve
    n "She is loose, and she is coming for you.\n"
    if fury_source == "tower":
        voice "audio/voices/ch3/fury/broken/fury_broken_18.flac"
        broken "Let her end it. It's the punishment you all deserve for what you did to her. It's the punishment I deserve for letting it happen.\n"
        voice "audio/voices/ch3/fury/stubborn/36a.flac"
        stubborn "Screw that! We can win. We've done it before and we'll do it again, only this time, we'll make it out the other side. Hell, she's practically done most of the work for us!\n"
    elif trait_contrarian:
        voice "audio/voices/ch3/fury/contrarian/fury_contrarian_25.flac"
        contrarian "She wants us to be afraid because she wants us to think she can make us suffer. Don't give her the satisfaction.\n"
        voice "audio/voices/ch3/fury/stubborn/37.flac"
        stubborn "That's right. No fear. She's bigger than the last time but she's pulling herself apart. She's practically done most of the work for us!\n" id fury_broken_intro_e9b97314
    elif trait_cold:
        voice "audio/_pristine/voice/fury/cold/13.flac"
        cold "I like this one. Let's see her do her worst. Let's see if she can make us actually feel something.\n"
        voice "audio/_pristine/voice/fury/hero/11.flac"
        hero "Uh... whatever she wants to make us feel, I think it's going to be bad.\n"
        voice "audio/_pristine/voice/fury/cold/14.flac"
        cold "But bad is so much more interesting than numb.\n"
        voice "audio/_pristine/voice/fury/stubborn/13.flac"
        stubborn "Gah! Stop it with all this talk about feelings. The only feeling that matters is the rush of victory!\n"
    else:
        voice "audio/_pristine/voice/extras/broken/6.flac"
        broken "She's only trying to connect with us. Wouldn't you want to dig for a spark once you lost it? To try to reignite something, even if it hurts?\n"
        #voice "audio/voices/ch3/fury/stubborn/38.flac"
        #stubborn "Stop that. We can win! We just have to lose our fear.\n"
    if fury_blade_taken == False:
        voice "audio/voices/ch3/fury/hero/fury_hero_37.flac"
        hero "We don't even have a weapon.\n"
        voice "audio/voices/ch3/fury/stubborn/39.flac"
        stubborn "It doesn't matter. I refuse to go out any way that isn't kicking and screaming.\n"
    play audio "audio/final/fury_walk_single.flac"
    show fury d approach2 onlayer back with hpunch
    with dissolve
    menu:
        extend ""

        "{i}• ''Given up on destroying the world, have we?''{/i}" if fury_source == "tower" and tower_self_knowledge:
            voice "audio/voices/ch3/fury/princess/11.flac"
            show fury d approach2 talk onlayer back
            sp "The world hasn't wronged me the way you have. Maybe I'll get around to it eventually, though. Once I've had my fill of you.\n"
            jump fury_no_fight_end

        "{i}• ''What happened to you?''{/i}":
            show fury d approach2 talk onlayer back
            if fury_source == "tower":
                voice "audio/voices/ch3/fury/princess/12.flac"
                sp "Time happened. You happened. But none of that matters. We're together again, and I'll have my pound of flesh.\n"
            else:
                voice "audio/_pristine/voice/fury/princess/3a.flac"
                sp "Time happened. You happened. But none of that matters. We're together again, and I'll have the resolution you denied me.\n"
            jump fury_no_fight_end

        "{i}• ''Wait! We don't have to do this!''{/i}":
            show fury d approach2 talk onlayer back
            if fury_source == "tower":
                voice "audio/voices/ch3/fury/princess/14.flac"
                sp "You're right. We don't. But I want to. So, so badly.\n"
            else:
                voice "audio/_pristine/voice/fury/princess/4a.flac"
                sp "But we do! It's part of who we are! These are the fleshy threads that bind us together. I'll just have to show you.\n"
            jump fury_no_fight_end

        "{i}• ''I'm sorry, okay? I'm sorry for what I did to you!''{/i}":
            show fury d approach2 talk onlayer back
            default fury_early_sorry = False
            $ fury_early_sorry = True
            if fury_source == "tower":
                voice "audio/voices/ch3/fury/princess/15.flac"
                sp "Words are not repentance. Apologies are paid for only in flesh and deed.\n"
                voice "audio/voices/ch3/fury/princess/16.flac"
                sp "And flesh works for me.\n"
            else:
                voice "audio/voices/ch3/fury/princess/17.flac"
                sp "If you're sorry then you'll stand and fight.\n"
                voice "audio/voices/ch3/fury/princess/18.flac"
                sp "I don't want a sniveling coward. I want to squeeze the life out of a ferocious heart.\n"
            jump fury_no_fight_end

        "{i}• ''Please just listen to me!''{/i}":
            show fury d approach2 talk onlayer back
            if fury_source == "tower":
                voice "audio/voices/ch3/fury/princess/19.flac"
                sp "No. I don't care about your words. I care about getting my pound of flesh.\n"
            else:
                voice "audio/voices/ch3/fury/princess/20.flac"
                sp "No! No more words! There is only the truth of violence left between us!\n"
            label fury_no_fight_end:
                voice "audio/voices/ch3/fury/narrator/56.flac"
                play secondary "audio/final/fury_walk_short.flac"
                hide chain onlayer back
                hide bg onlayer back
                hide fore onlayer front
                hide fury onlayer back
                show bg fury charge onlayer back at shakeshort, Position(ypos=1125)
                show fury charge onlayer front at shakeshort, Position(ypos=1125)
                with Dissolve(1.0)
                n "She bounds across the room, her fists ready, her heart set upon your destruction.\n"
                jump fury_mirror

        "{i}• ''This isn't over until I say it's over. I'm taking you out.'' [[Round three.]{/i}" if fury_source == "unarmed":
            jump fury_claim_charge_join

        "{i}• ''I'm going to end you.'' [[Slay the Princess]{/i}" if blade_held and fury_source != "pacifism":
            label fury_claim_charge_join:
                voice "audio/voices/ch3/fury/princess/21.flac"
                sp "You'll try. And that's what I've been so excited for. Let's hurt each other.\n"
                jump fury_blade_charge_join

        "{i}• [[Slay the Princess.]{/i}" if blade_held and fury_source != "pacifism":
            label fury_blade_charge_join:
                voice "audio/voices/ch3/fury/narrator/57.flac"
                play audio "audio/one_shot/footstep_run_medium.flac"
                play secondary "audio/final/fury_walk_short.flac"
                hide chain onlayer back
                hide bg onlayer back
                hide fore onlayer front
                hide fury onlayer back
                show bg fury charge onlayer back at shakeshort, Position(ypos=1125)
                show fury charge onlayer front at shakeshort, Position(ypos=1125)
                with Dissolve(1.0)
                n "Your heart free of fear, you charge towards the Princess, your eyes locked on each other, both of you prepared to lay down your very essence in one blow.\n"
                voice "audio/voices/ch3/fury/stubborn/40.flac"
                stubborn "It's now or never, let's make it a beautiful blaze of glory!\n"
                jump fury_mirror

        "{i}• [[Round three.]{/i}" if fury_source == "unarmed":
            jump fury_blade_charge_join

        "{i}• [[Fight back.]{/i}" if blade_held == False and fury_source != "unarmed":
            voice "audio/voices/ch3/fury/narrator/58.flac"
            play secondary "audio/final/fury_walk_short.flac"
            play audio "audio/one_shot/footstep_run_medium.flac"
            hide chain onlayer back
            hide bg onlayer back
            hide fore onlayer front
            hide fury onlayer back
            show bg fury charge onlayer back at shakeshort, Position(ypos=1125)
            show fury charge onlayer front at shakeshort, Position(ypos=1125)
            with Dissolve(1.0)
            n "Still unarmed, you charge towards the Princess.\n"
            voice "audio/voices/ch3/fury/stubborn/40.flac"
            stubborn "It's now or never, let's make it a beautiful blaze of glory!\n"
            jump fury_mirror

        "{i}• [[Let her end you.]{/i}":
            play secondary "audio/final/fury_walk_short.flac"
            if blade_held:
                $ blade_held = False
                $ default_mouse = "default"
                play audio "audio/one_shot/knife_bounce_several.flac"
                voice "audio/voices/ch3/fury/narrator/59.flac"
                hide chain onlayer back
                hide bg onlayer back
                hide fore onlayer front
                hide fury onlayer back
                show bg fury charge onlayer back at shakeshort, Position(ypos=1125)
                show fury charge onlayer front at shakeshort, Position(ypos=1125)
                with Dissolve(1.0)
                n "The blade tumbles from your nervous fingers as you stand, arms outstretched, facing the bleeding Princess as she barrels towards you.\n"
            else:
                voice "audio/voices/ch3/fury/narrator/60.flac"
                hide chain onlayer back
                hide bg onlayer back
                hide fore onlayer front
                hide fury onlayer back
                show bg fury charge onlayer back at shakeshort, Position(ypos=1125)
                show fury charge onlayer front at shakeshort, Position(ypos=1125)
                with Dissolve(1.0)
                n "You stand, arms outstretched, facing the bleeding Princess as she barrels towards you.\n"
            jump fury_mirror

label fury_mirror:
    stop music
    if fury_source != "tower" and blade_held:
        $ blade_held = False
        $ default_mouse = "default"
        play audio "audio/one_shot/knife_bounce_several.flac"
    voice "audio/voices/ch3/fury/narrator/squelch.flac"
    play secondary "audio/final/Assorted_TapestyUnraveledBreakingRip_1.flac"
    play audio "audio/final/Spectre_HeartCrush_2 copy.flac"
    hide farback onlayer back
    show fury charge ribbons onlayer front at Position(ypos=1125)
    show ribbons fury start 1 onlayer inyourface at Position(ypos=1125)
    n "With a horrifying squelch, you are unwound.\n"
    jump fury_pristine
