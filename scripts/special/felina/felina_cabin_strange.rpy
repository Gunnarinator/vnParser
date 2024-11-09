label felina_cabin_strange_start:
    $ achievement.grant("ACH_STRANGE_END")

    stop music
    stop secondary
    stop tertiary
    play sound "audio/looping/ambient_cabin.ogg" loop fadein 1.0
    scene farback stranger cabin onlayer farback at Position(ypos=1125)
    #show bodies stranger cabin onlayer farback at Position(ypos=1125)
    show back2 stranger cabin onlayer back at Position(ypos=1125)
    show fore cabin stranger onlayer back at Position(ypos=1125)
    show bodies cabin windows stranger onlayer back at Position(ypos=1125)
    show table stranger onlayer back at Position(ypos=1125)
    if final_offer == False:
        show knife stranger onlayer back at Position(ypos=1125)
    with fade

    $ gallery_zfinale.unlock_item(11)
    $ renpy.save_persistent()
    voice "audio/voices/felina/cabin/stranger/hero/1.flac"
    hero "And here we are. I'd say we were back where it all started, but I guess it's a little after that, isn't it?\n"
    voice "audio/voices/felina/cabin/shared/hero/4a.flac"
    hero "Do you... need me to describe things?\n"
    voice "audio/voices/felina/cabin/stranger/contrarian/1.flac"
    contrarian "That'd be nice. A little comfort in an almost unfamiliar place.\n"
    voice "audio/voices/felina/cabin/stranger/hero/2.flac"
    hero "Oh. You made it here, too.\n"
    voice "audio/voices/felina/cabin/stranger/contrarian/2a.flac"
    contrarian "We never really got to talk to her, did we? {i}This one{/i}, I mean.\n"
    if mirror_n_cruel_count >= 2:
        voice "audio/voices/felina/cabin/stranger/contrarian/3.flac"
        contrarian "No hard feelings about taunting us with our 'deaths,' by the way. I thought it was funny. Not sure about the others, though.\n"
        voice "audio/voices/felina/cabin/stranger/hero/3.flac"
        hero "They're not happy.\n"
        voice "audio/voices/felina/cabin/stranger/contrarian/4.flac"
        contrarian "Oh, they'll get over it!\n"
    label felina_cabin_strange_menu_start:
        menu:
            extend ""

            "{i}• (Explore) ''I'd like that description now, if you don't mind. For old times' sake.''{/i}" if felina_cabin_menu_count == 0 and felina_cabin_describe == False:
                label felina_cabin_strange_describe_join:
                    $ felina_cabin_describe = True
                    $ felina_cabin_menu_count += 1
                    voice "audio/voices/felina/cabin/stranger/hero/4.flac"
                    hero "Yeah. Of course.\n"
                    if final_offer:
                        voice "audio/_pristine/voice/_climax/cabin_endings/general/hero/7.flac"
                        hero "The interior of the cabin is... well, it's not really a cabin, is it? It's that terrifying blend of everything. Only it doesn't feel so terrifying anymore.\n"
                        voice "audio/_pristine/voice/_climax/cabin_endings/general/hero/8.flac"
                        hero "It's still shaped like a cabin. It's just different in places. There's still walls, a door to the basement, a table. Windows.\n"
                        voice "audio/_pristine/voice/_climax/cabin_endings/general/hero/10.flac"
                        hero "No mirror this time... and there's no blade, is there? I guess whatever we find down there, we'll have to face it empty-handed.\n"
                        voice "audio/_pristine/voice/_climax/cabin_endings/general/contrarian/2.flac"
                        contrarian "Huh. I guess you're right. I think... I think it's better that way.\n"
                        voice "audio/_pristine/voice/_climax/cabin_endings/general/hero/11.flac"
                        hero "If there was a blade, you'd probably just tell us to throw it out the window.\n"
                        voice "audio/_pristine/voice/_climax/cabin_endings/general/contrarian/3.flac"
                        contrarian "{i}Sigh{/i}. Nah. There wouldn't be a third beat. We'd need a third beat for it to be funny. Besides, I don't feel like laughing anymore.\n"
                        voice "audio/_pristine/voice/_climax/cabin_endings/general/hero/12.flac"
                        hero "You've changed.\n"
                        voice "audio/_pristine/voice/_climax/cabin_endings/general/contrarian/4.flac"
                        contrarian "I think I'm just... tired. I've had... a lot of time to myself here.\n"
                    else:
                        voice "audio/voices/felina/cabin/stranger/hero/5.flac"
                        hero "The interior of the cabin is... well, it's not really a cabin, is it? It's that terrifying blend of everything. Only it doesn't feel so terrifying anymore.\n"
                        voice "audio/voices/felina/cabin/stranger/hero/6.flac"
                        hero "It's still shaped like a cabin. It's just different in places. There's still walls, a door to the basement, a table, that knife. Windows.\n"
                        voice "audio/voices/felina/cabin/stranger/hero/7.flac"
                        hero "You know, come to think of it, I don't think He ever really included the windows in his cabin descriptions, did he?\n"
                        if stranger_1_cabin_blade_tossed:
                            voice "audio/voices/felina/cabin/stranger/contrarian/5.flac"
                            contrarian "He mentioned the windows when we broke them.\n"
                            voice "audio/voices/felina/cabin/stranger/hero/8.flac"
                            hero "No mirror this time, either. I think it did whatever it needed to do.\n"
                        else:
                            voice "audio/voices/felina/cabin/stranger/contrarian/6.flac"
                            contrarian "I always thought they were implied.\n"
                            voice "audio/voices/felina/cabin/stranger/hero/9.flac"
                            hero "He never mentioned the mirror, either, but that didn't mean he implied it was there.\n"
                            voice "audio/voices/felina/cabin/stranger/hero/10.flac"
                            hero "It's gone, though. I think it did whatever it needed to do.\n"

                        if felina_stated_goal == "slay":
                            voice "audio/voices/felina/cabin/stranger/hero/11.flac"
                            hero "And I know I've already mentioned it, but if we want to see this through, we're going to need that blade.\n"
                        else:
                            voice "audio/voices/felina/cabin/stranger/hero/12.flac"
                            hero "And I know you're still trying to find some middle ground, but if things go south, we're going to need that blade.\n"
                    jump felina_cabin_strange_menu_start

            "{i}• (Explore) ''If the offer still stands, could you describe the cabin to us? For old times' sake?''{/i}" if felina_cabin_menu_count != 0 and felina_cabin_describe == False:
                jump felina_cabin_strange_describe_join

            "{i}• (Explore) ''Is it just the three of us? Did anyone else make it to the cabin?''{/i}" if felina_cabin_alone == False:
                $ felina_cabin_alone = True
                $ felina_cabin_menu_count += 1
                voice "audio/voices/felina/cabin/stranger/hero/13.flac"
                hero "It's just us. I think the rest of them are still out there jumbled up in the rest of her.\n"
                voice "audio/voices/felina/cabin/stranger/contrarian/7.flac"
                contrarian "And I've been here since you left me here. No hard feelings. I'm just glad you're back to see this through.\n"
                jump felina_cabin_strange_menu_start

            "{i}• (Explore) ''Is the Narrator really gone?''{/i}" if felina_cabin_narrator_dead == False:
                $ felina_cabin_narrator_dead = True
                $ felina_cabin_menu_count += 1
                voice "audio/voices/felina/cabin/shared/hero/12.flac"
                hero "Yeah. It's dead silent in here. Whatever it was that was left of Him... I don't think it could handle you waking up to godhood. Pretty sure He got obliterated.\n"
                voice "audio/voices/felina/cabin/stranger/contrarian/8.flac"
                contrarian "Really goes to show how much you've grown up. Killing somebody across every iteration of reality just by existing. I don't even know what I would do if I were in the driver's seat of that kind of power.\n"
                jump felina_cabin_strange_menu_start

            "{i}• (Explore) ''Good riddance.''{/i}" if felina_cabin_narrator_dead and felina_cabin_narrator_final_thoughts == "":
                $ felina_cabin_narrator_final_thoughts = "byefelicia"
                $ felina_cabin_menu_count += 1
                voice "audio/voices/felina/cabin/stranger/contrarian/9.flac"
                contrarian "Good riddance? Really? I'm gonna miss the guy.\n"
                if felina_stated_goal == "slay":
                    voice "audio/voices/felina/cabin/stranger/hero/14.flac"
                    hero "I'm surprised, considering you've decided to go through with the whole 'slaying' thing he was pushing for since the beginning. I guess you can like the idea and hate the man.\n"
                else:
                    voice "audio/voices/felina/cabin/stranger/hero/15.flac"
                    hero "Yeah, right. He really put us through hell, didn't He?\n"
                jump felina_cabin_strange_menu_start

            "{i}• (Explore) ''I don't actually know how to feel about Him being gone.''{/i}" if felina_cabin_narrator_dead and felina_cabin_narrator_final_thoughts == "":
                $ felina_cabin_narrator_final_thoughts = "unsure"
                $ felina_cabin_menu_count += 1
                label felina_cabin_strange_complicated_feelings:
                    voice "audio/voices/felina/cabin/stranger/hero/16.flac"
                    hero "Yeah, it's complicated. He put us through hell, but He's been part of us since the very beginning, hasn't He?\n"
                    if felina_cabin_narrator_final_thoughts == "unsure":
                        voice "audio/voices/felina/cabin/stranger/contrarian/10.flac"
                        contrarian "It's not complicated at all. I miss him. I feel bad that he's gone.\n"
                    jump felina_cabin_strange_menu_start

            "{i}• (Explore) ''It's funny. After everything He put us through, I'm kind of sad to see Him go.''{/i}" if felina_cabin_narrator_dead and felina_cabin_narrator_final_thoughts == "":
                $ felina_cabin_narrator_final_thoughts = "sad"
                $ felina_cabin_menu_count += 1
                voice "audio/voices/felina/cabin/stranger/contrarian/11.flac"
                contrarian "Me too. He was a lot of fun. Really easy to mess with.\n"
                if felina_stated_goal == "slay":
                    voice "audio/voices/felina/cabin/stranger/hero/17.flac"
                    hero "At least it seems you're honoring his memory. I'm sure He'd be proud to see you follow through on what he always wanted.\n"
                else:
                    jump felina_cabin_strange_complicated_feelings
                jump felina_cabin_strange_menu_start

            "{i}• (Explore) [[Take the blade.]{/i}" if blade_held == False and stranger_felina_blade_thrown == False and final_offer == False:
                play audio "audio/one_shot/knife_pickup.flac"
                $ blade_held = True
                if stranger_other_way:
                    $ default_mouse = "thumb"
                else:
                    $ default_mouse = "blade"
                hide knife onlayer front
                hide knife onlayer back with dissolve

                voice "audio/voices/felina/cabin/stranger/contrarian/12.flac"
                contrarian "That's probably for the best. It's always seemed to give us more things we can do, right?\n"
                voice "audio/voices/felina/cabin/stranger/hero/18.flac"
                hero "So you're not gonna suggest we throw it out the window?\n"
                voice "audio/voices/felina/cabin/stranger/contrarian/13.flac"
                contrarian "No, we've been through too much for that. And He's gone, so there's no one left to mess with but ourself.\n"
                voice "audio/voices/felina/cabin/stranger/hero/19.flac"
                hero "You've gotten serious.\n"
                if stranger_1_cabin_blade_tossed:
                    voice "audio/voices/felina/cabin/stranger/contrarian/14.flac"
                    contrarian "Besides, what's the third beat? It isn't funny if we toss it out the window twice.\n"
                else:
                    voice "audio/voices/felina/cabin/stranger/contrarian/15.flac"
                    contrarian "Besides, what's the third beat? It isn't funny if I suggest that twice. Especially since you never took me up on it last time.\n"
                voice "audio/voices/felina/cabin/stranger/hero/20.flac"
                hero "There's the guy I know.\n"
                jump felina_cabin_strange_menu_start

            "{i}• (Explore) [[Throw the blade out the window.]{/i}" if blade_held and stranger_felina_blade_thrown == False:
                default stranger_felina_blade_thrown = False
                $ stranger_felina_blade_thrown = True
                $ blade_held = False
                $ default_mouse = "default"
                hide bodies onlayer farback
                hide door onlayer front
                show bodies cabin windows stranger knife onlayer back at Position(ypos=1125)
                play audio "audio/final/_stranger_final_toss.flac"
                voice "audio/voices/felina/cabin/stranger/contrarian/16.flac"
                contrarian "You actually did it! I know I just told you not to, but I'm proud that you did it anyways. It's like you've finally left the nest.\n"
                voice "audio/voices/felina/cabin/stranger/hero/21.flac"
                hero "Yeah. Just like that it's gone, isn't it? Blade tossed. Glass shattered. I guess we'll have to make do without it. There's your third beat.\n"
                voice "audio/voices/felina/cabin/stranger/contrarian/17.flac"
                contrarian "Hey! You're right. Good work, that was really funny.\n"
                jump felina_cabin_strange_menu_start

            "{i}• [[Enter the basement.]{/i}":
                if blade_held == False and stranger_felina_blade_thrown == False and final_offer == False:
                    if felina_stated_goal == "slay"  and final_offer == False:
                        voice "audio/voices/felina/cabin/stranger/hero/22.flac"
                        hero "No blade, huh? Have you given up on slaying her?\n"
                    else:
                        voice "audio/voices/felina/cabin/stranger/hero/23.flac"
                        hero "No blade it is. I'm not sure what we'll be able to do without it, but your judgment has gotten us this far.\n"
                    voice "audio/voices/felina/cabin/stranger/contrarian/18.flac"
                    contrarian "If that's what you think is best, that's what you think is best. I'm just along for the ride at this point.\n"


                $ quick_menu = False
                hide bodies onlayer back
                hide table onlayer back
                hide knife onlayer back
                hide bodies onlayer front
                hide bodies onlayer farback
                hide back2 onlayer back
                hide farback onlayer farback
                hide back2 onlayer back
                hide fore onlayer front
                hide door onlayer front
                hide door onlayer back
                hide table onlayer front
                hide knife onlayer back
                hide knife onlayer front
                hide mirror onlayer back
                hide mirror onlayer front
                hide bodies onlayer front
                hide fore onlayer back
                with fade
                play audio "audio/one_shot/door_bedroom.flac"
                scene farback nightmare basement onlayer farback at Position(ypos=1125)
                show bg stranger stairs end onlayer back at Position(ypos=1125)
                show fore stranger stairs end onlayer front at Position(ypos=1125)
                with fade
                if persistent.quick_menu:
                    $ quick_menu = True
                voice "audio/voices/felina/cabin/stranger/hero/24.flac"
                hero "Those winding stairs again. But now there's only one way forward. Do you remember the first time we were here? The first time we heard her voice?\n"
                voice "audio/voices/felina/cabin/stranger/contrarian/19.flac"
                contrarian "Yeah. It was a real mess. Stopped being fun pretty quick.\n"
                voice "audio/voices/felina/cabin/stranger/princess/1.flac"
                p "It's okay, you can come down. The stairs won't bite. Not this time.\n"
                if felina_stated_goal == "slay":
                    voice "audio/voices/felina/cabin/stranger/princess/2.flac"
                    p "Let's talk, one last time, before you kill us. If that's still what you want to do.\n"
                else:
                    voice "audio/voices/felina/cabin/stranger/princess/3alt.flac"
                    p "We don't know what you want from us, but let's talk. All of us. Maybe we can help you find your way.\n"
                voice "audio/voices/felina/cabin/stranger/contrarian/20.flac"
                contrarian "She doesn't sound messy anymore, though. At least somebody here feels put together.\n"
                menu:
                    extend ""

                    "{i}• [[Continue down the stairs.]{/i}":
                        voice "audio/voices/felina/cabin/stranger/hero/25.flac"
                        $ quick_menu = False
                        play audio "audio/final/footsteps_stone_short.flac"
                        hide farback onlayer farback
                        hide bg onlayer back
                        hide fore onlayer front
                        with fade
                        hero "And forward we go. We shouldn't keep her waiting.\n"
                        jump felina_cabin_strange_basement

label felina_cabin_strange_basement:
    play sound "audio/looping/ambient_basement_interior.ogg" loop
    scene bodies basement onlayer farback at Position(ypos=1125)
    show bg basement end no chain onlayer back at Position(ypos=1125)
    show stranger d neutral onlayer back at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    voice "audio/voices/felina/cabin/stranger/contrarian/21.flac"
    contrarian "That was easy compared to last time. Just stairs! No weird fuzzy stuff or nonsense trying to pull us apart.\n"
    voice "audio/voices/felina/cabin/stranger/hero/26.flac"
    hero "Yeah, that wasn't so bad.\n"

    if blade_held == False:
        if felina_stated_goal == "slay":
            voice "audio/voices/felina/cabin/stranger/princess/4.flac"
            show stranger d confused talk onlayer back
            with dissolve
            p "No knife? Even after everything you saw out there, and all the lives we've ended together, and you coming right out and saying you'd rather see us dead... you're second guessing yourself?\n"
            voice "audio/voices/felina/cabin/stranger/princess/5.flac"
            show stranger d closed talk onlayer back
            with dissolve
            p "We thought we could see everything, but this is outside of the script.\n"
        else:
            voice "audio/voices/felina/cabin/stranger/princess/6.flac"
            show stranger d closed talk onlayer back
            with dissolve
            p "So you didn't bring the knife. After all the lives we've lived together and all the lives we haven't, you somehow found a way to move outside of the script.\n"
        voice "audio/voices/felina/cabin/stranger/princess/7.flac"
        show stranger d confused talk onlayer back
        with dissolve
        p "Are we missing a page?\n"
        show stranger d confused onlayer back

    else:
        if felina_stated_goal == "slay":
            voice "audio/voices/felina/cabin/stranger/princess/8.flac"
            show stranger d neutral talk onlayer back
            with dissolve
            p "Even after everything you've seen, and all the lives we've lived together, you still want to kill us. The Echo really got his hooks into you. Unless... you have your own reasons for wanting us dead?\n"
            show stranger d neutral onlayer back
        else:
            voice "audio/voices/felina/cabin/stranger/princess/9.flac"
            show stranger d confused talk onlayer back
            with dissolve
            p "So... you brought the knife. After everything you've seen, and all the lives we've lived together, you still aren't sure what you want to do? Unless... you are. We just hope you're sure of yourself, one way or the other.\n"
            show stranger d neutral onlayer back

    menu:
        extend ""

        "{i}• [[Slay the Princess.]{/i}" if blade_held:
            voice "audio/voices/felina/cabin/stranger/hero/27.flac"
            hero "So this is really it, then. Let's see this through.\n"
            play secondary "audio/one_shot/footstep_run_medium.flac"
            jump felina_slain_start

        "{i}• [[Sit with them.]{/i}":
            "{nw}"
            show screen disableclick(0.5)
            if blade_held:
                $ quick_menu = False
                play audio "audio/final/footsteps_stone_short.flac"
                hide bodies onlayer farback
                hide bg onlayer back
                hide stranger onlayer back
                show bg basement close onlayer farback at Position(ypos=1125)
                show stranger c sad smile onlayer back at Position(ypos=1125)
                with fade
                if persistent.quick_menu:
                    $ quick_menu = True
                jump felina_cabin_strange_talk_blade_menu
            else:
                $ quick_menu = False
                play audio "audio/final/footsteps_stone_short.flac"
                hide bodies onlayer farback
                hide bg onlayer back
                hide stranger onlayer back
                show bg basement close onlayer farback at Position(ypos=1125)
                show stranger c neutral onlayer back at Position(ypos=1125)
                with fade
                if persistent.quick_menu:
                    $ quick_menu = True
                jump felina_cabin_strange_empty_talk_menu


label felina_cabin_strange_empty_talk_menu:
    default felina_stranger_count = 0

    default felina_stranger_mound_thoughts = False
    default felina_stranger_fair = False
    default felina_stranger_intro = False
    default felina_stranger_sorry = False
    default felina_stranger_which = False
    default felina_stranger_name = False
    menu:
        extend ""

        "{i}• (Explore) ''I never got the chance to talk to you before you were taken away. Not {b}you{/b} you, at least. I'm sorry for what I did to you.''{/i}" if felina_stranger_sorry == False:
            $ felina_stranger_sorry = True
            $ felina_stranger_count += 1
            voice "audio/voices/felina/cabin/stranger/princess/10a.flac"
            show stranger c shrug talk onlayer back
            with dissolve
            p "It's okay, no hard feelings. In a way, you helped us become a version of... her. But we weren't very good at it. A conversation with us then probably wouldn't have been very insightful.\n"
            voice "audio/voices/felina/cabin/stranger/princess/11.flac"
            show stranger c sad smile talk onlayer back
            with dissolve
            p "That's probably why we were taken away. That's all we had to offer you, it was time to change again.\n"
            show stranger c sad smile onlayer back
            voice "audio/voices/felina/cabin/stranger/contrarian/22.flac"
            contrarian "After all we did, she's just forgiving us? Just like that?! ... You know... that means a lot.\n"
            jump felina_cabin_strange_empty_talk_menu

        "{i}• (Explore) ''It's so good to finally see you again.''{/i}" if felina_stranger_intro == False:
            $ felina_stranger_intro = True
            $ felina_stranger_count += 1
            voice "audio/_pristine/voice/_climax/cabin_endings/stranger/7.flac"
            show stranger c smile talk onlayer back
            with dissolve
            p "It is, for all of us! We've seen so many threads of stories told between us, but this moment is... unexpected. Even when we've seen it all, you still manage to surprise us.\n"
            show stranger c smile onlayer back
            with dissolve
            jump felina_cabin_strange_empty_talk_menu

        "{i}• (Explore) ''I don't think I want to be a god.''{/i}" if felina_cabin_god_comment == False:
            $ felina_cabin_god_comment = True
            $ felina_stranger_count += 1
            voice "audio/voices/felina/cabin/stranger/contrarian/23.flac"
            contrarian "Hard agree. Seems overrated. Too much pressure.\n"
            voice "audio/voices/felina/cabin/stranger/princess/12.flac"
            show stranger c smile talk onlayer back
            with dissolve
            p "But that's what you've always been. Even now. You can't put aside such an important part of who you are, and neither can we.\n"
            voice "audio/voices/felina/cabin/stranger/princess/13.flac"
            show stranger c shrug talk onlayer back
            with dissolve
            p "So... you might as well embrace it!\n"
            show stranger c smile onlayer back
            jump felina_cabin_strange_empty_talk_menu

        "{i}• (Explore) ''Are you... the same as you are out there?''{/i}" if felina_cabin_same_comment == False:
            $ felina_cabin_same_comment = True
            $ felina_stranger_count += 1
            voice "audio/voices/felina/cabin/stranger/princess/14.flac"
            show stranger c gentle ask onlayer back
            with dissolve
            p "Yes... we think. We're kind of like a shadow. Out there, every part of us is blended together into one huge idea, a big wave of unyielding change crashing against the world...\n"
            voice "audio/voices/felina/cabin/stranger/princess/15.flac"
            show stranger c closed talk onlayer back
            with dissolve
            p "But in here, we're fractured. Small. Still a little more separate than we'd like to be, our instincts still trying to pull us in different directions\n"
            voice "audio/voices/felina/cabin/stranger/contrarian/24.flac"
            show stranger c smile onlayer back
            with dissolve
            contrarian "That's kind of like us, isn't it?\n"
            voice "audio/voices/felina/cabin/stranger/hero/28.flac"
            hero "Yeah. We really are the same.\n"
            jump felina_cabin_strange_empty_talk_menu

        "{i}• (Explore) ''What do you think of Her? What She wanted us to be.''{/i}" if felina_stranger_mound_thoughts == False:
            $ felina_stranger_count += 1
            $ felina_stranger_mound_thoughts = True
            voice "audio/_pristine/voice/_climax/cabin_endings/stranger/8.flac"
            show stranger c serious talk onlayer back
            with dissolve
            stranger "We... don't know. We've seen through so many eyes, but all of them have been Hers.\n"
            voice "audio/_pristine/voice/_climax/cabin_endings/stranger/9.flac"
            show stranger c sad smile talk onlayer back
            with dissolve
            stranger "We like you as you are. We like us as we are. Maybe we would have liked Her version of us, too, turning the wheel of a cosmic cycle together. But that's not the choice you made, even though She did everything in Her power to convince you.\n"
            voice "audio/_pristine/voice/_climax/cabin_endings/stranger/10.flac"
            show stranger c gentle ask onlayer back
            with dissolve
            stranger "It took courage for you to make your way down here, away from the paths others would have had you walk. We find that courage beautiful.\n"
            voice "audio/_pristine/voice/_climax/cabin_endings/leave/contrarian/4.flac"
            show stranger c gentle onlayer back
            with dissolve
            contrarian "But that's... the worst part of us. That's me she's talking about.\n"
            voice "audio/_pristine/voice/_climax/cabin_endings/leave/hero/8.flac"
            hero "I think that's the point. There is no worst part of us.\n"
            jump felina_cabin_strange_empty_talk_menu

        "{i}• (Explore) ''Which... Princess are you? You look like you did the first time we met. Is this the real you?''{/i}" if felina_stranger_which == False:
            $ felina_stranger_which = True
            $ felina_stranger_count += 1
            voice "audio/_pristine/voice/_climax/cabin_endings/stranger/1.flac"
            show stranger c offering talk onlayer back
            with dissolve
            p "It's so tempting to speak as She would. To simply state that we're all of them, but that we're also something new. We don't know if you'll find that answer satisfying.\n"
            voice "audio/_pristine/voice/_climax/cabin_endings/stranger/2a.flac"
            show stranger c sad smile talk onlayer back
            with dissolve
            p "Perhaps you'd rather hear that we're the first version of her that you've met, but that we've been shaped by the experiences of all of the others.\n"
            voice "audio/_pristine/voice/_climax/cabin_endings/stranger/3.flac"
            show stranger c closed talk onlayer back
            with dissolve
            p "Yes. That feels right to us.\n"
            voice "audio/_pristine/voice/_climax/cabin_endings/leave/contrarian/1.flac"
            show stranger c sad smile onlayer back
            with dissolve
            contrarian "It's her. It wouldn't make sense if she was anyone else.\n"
            jump felina_cabin_strange_empty_talk_menu

        "{i}• (Explore) ''So, now that we're here at the end of everything... can you finally tell me your name?''{/i}" if felina_stranger_name == False:
            $ felina_stranger_name = True
            $ felina_stranger_count += 1
            voice "audio/_pristine/voice/_climax/cabin_endings/stranger/4.flac"
            show stranger c closed talk onlayer back
            with dissolve
            p "We're just a stranger, but that doesn't mean we have to be distant from you. It just means that we'll always be able to find new things to discover in each other.\n"
            voice "audio/_pristine/voice/_climax/cabin_endings/leave/contrarian/2.flac"
            show stranger c gentle onlayer back
            with dissolve
            contrarian "That's sweet. But it's also a little sad.\n"
            voice "audio/_pristine/voice/_climax/cabin_endings/leave/hero/4.flac"
            hero "I think it's only sad if we want it to be sad.\n"
            jump felina_cabin_strange_empty_talk_menu

        "{i}• (Explore) ''None of this was ever really fair for either of us, was it?''{/i}" if felina_stranger_fair == False:
            $ felina_stranger_fair = True
            $ felina_stranger_count += 1
            voice "audio/_pristine/voice/_climax/cabin_endings/leave/contrarian/3.flac"
            contrarian "Is it unfair if it's our fault?\n"
            voice "audio/_pristine/voice/_climax/cabin_endings/stranger/5.flac"
            show stranger c shrug talk onlayer back
            with dissolve
            p "Was it not? We've found you, at the end of all things. And you've found us. Is that not fair? Would this moment be what it is without the pain that built to it?\n"
            voice "audio/_pristine/voice/_climax/cabin_endings/stranger/6.flac"
            show stranger c offering talk onlayer back
            with dissolve
            p "We know we must sound like her, but... it's how we feel. Everything that happened to us seems so important now. We walked a long and winding path together and we've cherished every second of it.\n"
            voice "audio/_pristine/voice/_climax/cabin_endings/leave/hero/5.flac"
            show stranger c sad smile onlayer back
            with dissolve
            hero "Besides, I don't think fairness has much to do with anything.\n"
            jump felina_cabin_strange_empty_talk_menu

        "{i}• (Explore) ''I only wanted to slay the you out there. It's easier to want to kill an abstract concept than it is a person. As weird a person as you are.''{/i}" if felina_stated_goal == "slay" and felina_cabin_same_comment == False and felina_strange_slay_comment == False:
            voice "audio/voices/felina/cabin/stranger/princess/16.flac"
            show stranger c smile talk onlayer back
            with dissolve
            p "Who are you calling weird?\n"
            voice "audio/voices/felina/cabin/stranger/princess/17.flac"
            show stranger c wink talk onlayer back
            with dissolve
            p "Just kidding, we know we're weird. And so are you.\n"
            label felina_strange_slay_cabin_join:
                $ felina_stranger_count += 1
                $ felina_strange_slay_comment = True
                default felina_strange_slay_comment = False
                voice "audio/voices/felina/cabin/stranger/princess/18.flac"
                show stranger c gentle ask onlayer back
                with dissolve
                p "We don't have many options, though, do we? There are only so many places to go, and you don't have a means to slay us. So what will we do?\n"
                show stranger c sad smile onlayer back
                jump felina_cabin_strange_empty_talk_menu

        "{i}• (Explore) ''I only wanted to slay the you out there. It's easier to want to kill an abstract concept than it is a person. Even if you say that you're the same.''{/i}" if felina_stated_goal == "slay" and felina_cabin_same_comment and felina_strange_slay_comment == False:
            show stranger c neutral onlayer back
            with dissolve
            jump felina_strange_slay_cabin_join

        "{i}• (Explore) ''I don't think I ever really wanted to slay you. But I don't like what your existence means for the world.''{/i}" if felina_stated_goal == "slay" and felina_strange_slay_comment == False:
            show stranger c neutral onlayer back
            with dissolve
            jump felina_strange_slay_cabin_join

        "{i}• ''What if we just leave?''{/i}" if felina_stranger_count < 9:
            show stranger c neutral onlayer back
            with dissolve
            jump felina_strange_leave_join_menu

        "{i}• ''I think the only thing left for us to do is leave.''{/i}" if felina_stranger_count >= 9:
            label felina_strange_leave_join_menu:
                voice "audio/voices/felina/cabin/stranger/contrarian/25.flac"
                contrarian "He'd hate that. So you should do it. Even if He isn't here anymore, it's the spirit of the thing.\n"
                voice "audio/voices/felina/cabin/stranger/princess/19.flac"
                show stranger c closed talk onlayer back
                with dissolve
                p "Leave? But what would happen if we left with you? Would we exist inside ourselves? Are you sure you want to find out if that's possible, or what that would mean for you?\n"
                voice "audio/voices/felina/cabin/stranger/princess/20.flac"
                show stranger c gentle ask onlayer back
                with dissolve
                p "Is that what you want?\n"
                label stranger_leave_hand_menu:
                    menu:
                        extend ""

                        "{i}• (Explore) [[Take their hand in yours.]{/i}" if felina_cabin_leave_hand_hold == False:
                            $ felina_cabin_leave_hand_hold = True
                            play music "audio/_music/mound/The Unknown Together Live Intro.flac"
                            queue music "audio/_music/mound/The Unknown Together Live Loop.flac" loop
                            show stranger c hold hand onlayer back
                            with dissolve
                            jump stranger_leave_hand_menu
                            jump felina_leave_cabin_ending

                        "{i}• ''I've always wanted to leave with you, but I didn't like being a god. I want to walk through that cabin door as we are. Just you and me.''{/i}":
                            jump felina_strange_pre_leave

                        "{i}• ''Not knowing is exactly why I want it. We knew everything out there, but we don't know this. I want this.''{/i}":
                            jump felina_strange_pre_leave

                        "{i}• ''It doesn't matter what it means. What matters is that we're leaving together. That's all I want.''{/i}":
                            jump felina_strange_pre_leave

                        "{i}• [[There's no need for words. Leave with her.]{/i}" if felina_cabin_leave_hand_hold:
                            jump felina_strange_pre_leave

                label felina_strange_pre_leave:
                    if felina_cabin_leave_hand_hold == False:
                        play music "audio/_music/mound/The Unknown Together Live Intro.flac"
                        queue music "audio/_music/mound/The Unknown Together Live Loop.flac" loop
                    voice "audio/voices/felina/cabin/stranger/princess/21.flac"
                    if felina_cabin_leave_hand_hold:
                        show stranger c hold hand talk onlayer back
                    else:
                        show stranger c tear onlayer back
                    with dissolve
                    p "After so many iterations, so many different versions of us clashing and coming together and clashing again... leaving with you feels like all we ever really wanted\n"
                    if felina_cabin_leave_hand_hold:
                        show stranger c hold hand onlayer back with dissolve
                    jump felina_leave_cabin_ending

label felina_cabin_strange_talk_blade_menu:
    menu:
        extend ""

        "{i}• (Explore) ''I never got the chance to talk to you before you were taken away. Not {b}you{/b} you, at least. I'm sorry for what I did.''{/i}" if felina_stranger_sorry == False:
            $ felina_stranger_sorry = True
            voice "audio/voices/felina/cabin/stranger/princess/22.flac"
            show stranger c shrug talk onlayer back
            with dissolve
            p "It's okay, no hard feelings. In a way, you helped us become a version of... her. But we weren't very good at it. I don't think a conversation with us then would have been very insightful.\n"
            voice "audio/voices/felina/cabin/stranger/princess/23.flac"
            show stranger c closed talk onlayer back
            with dissolve
            p "That's probably why we were taken away. That's all we had to offer you, it was time to change again.\n"
            voice "audio/voices/felina/cabin/stranger/contrarian/22.flac"
            show stranger c sad smile onlayer back
            with dissolve
            contrarian "After all we did, she's just forgiving us? Just like that?! ... You know... that means a lot.\n"
            jump felina_cabin_strange_talk_blade_menu

        "{i}• (Explore) ''I don't think I want to be a god.''{/i}" if felina_cabin_god_comment == False:
            $ felina_cabin_god_comment = True
            voice "audio/voices/felina/cabin/stranger/contrarian/23.flac"
            contrarian "Hard agree. Seems overrated, too much pressure.\n"
            voice "audio/voices/felina/cabin/stranger/princess/24.flac"
            show stranger c closed talk onlayer back
            with dissolve
            p "But that's what you've always been. Even now. You can't put aside such an important part of who you are, and neither can we.\n"
            voice "audio/voices/felina/cabin/stranger/princess/25.flac"
            show stranger c wink talk onlayer back
            with dissolve
            p "So... you might as well embrace it!\n"
            jump felina_cabin_strange_talk_blade_menu

        "{i}• (Explore) ''Are you... the same as you are out there?''{/i}" if felina_cabin_same_comment == False:
            $ felina_cabin_same_comment = True
            voice "audio/voices/felina/cabin/stranger/princess/26.flac"
            show stranger c gentle ask onlayer back
            with dissolve
            p "Yes... we think. We're kind of like a shadow. Out there, every part of us is blended together into one huge idea, a big wave of unyielding change crashing against the world...\n"
            voice "audio/voices/felina/cabin/stranger/princess/27.flac"
            show stranger c closed talk onlayer back
            with dissolve
            p "But in here, we're fractured. Small. Still a little more separate than we'd like to be, our instincts still trying to pull us in different directions\n"
            voice "audio/voices/felina/cabin/stranger/contrarian/24.flac"
            show stranger c sad smile onlayer back
            with dissolve
            contrarian "That's kind of like us, isn't it?\n"
            voice "audio/voices/felina/cabin/stranger/hero/28.flac"
            hero "Yeah. We really are the same.\n"
            jump felina_cabin_strange_talk_blade_menu

        "{i}• (Explore) ''I only wanted to slay the you out there. It's easier to want to kill an abstract concept than it is a person. As weird a person as you are.''{/i}" if felina_stated_goal == "slay" and felina_loop_strange_slay_weird_comment == False:
            default felina_loop_strange_slay_weird_comment = False
            $ felina_loop_strange_slay_weird_comment = True
            voice "audio/voices/felina/cabin/stranger/princess/16.flac"
            show stranger c smile talk onlayer back
            with dissolve
            p "Who are you calling weird?\n"
            voice "audio/voices/felina/cabin/stranger/princess/17.flac"
            show stranger c wink talk onlayer back
            with dissolve
            p "Just kidding, we know we're weird. And so are you.\n"
            show stranger c sad smile onlayer back
            jump felina_cabin_strange_talk_blade_menu

        "{i}• (Explore) ''I don't want to hurt anyone. There has to be a way out of this.''{/i}":
            $ felina_loop_strange_way_out_comment = True
            jump felina_loop_strange

        "{i}• (Explore) ''I don't think I ever really wanted to slay you. But I don't like what your existence means for the world.''{/i}" if felina_stated_goal == "slay":
            $ felina_loop_strange_slay_comment = True
            jump felina_loop_strange

        "{i}• (Explore) ''What are we going to do?''{/i}":
            jump felina_loop_strange

        "{i}• (Explore) ''I don't want to have to slay you, but I don't know what other options there are.''{/i}":
            $ felina_loop_strange_slay_comment = True
            jump felina_loop_strange

        "{i}• ''I'm sorry.'' [[Slay the Princess.]{/i}":
            $ felina_slain_apologize = True
            jump felina_slain_start

        "{i}• [[Slay the Princess.]{/i}":
            voice "audio/voices/felina/cabin/stranger/hero/27.flac"
            hero "So this is really it then. Let's see this through.\n"
            jump felina_slain_start

label felina_loop_strange:
    play music "audio/_music/mound/Loop Ending.flac" loop
    default felina_loop_strange_slay_comment = False
    default felina_loop_strange_way_out_comment = False
    if felina_loop_strange_way_out_comment:
        voice "audio/voices/felina/cabin/stranger/princess/29alt.flac"
        show stranger c offering talk onlayer back
        with dissolve
        p "We don't think there's a way for us to leave, but maybe there doesn't have to be an ending.\n"
    elif felina_loop_strange_slay_weird_comment:
        voice "audio/voices/felina/cabin/stranger/princess/30.flac"
        show stranger c offering talk onlayer back
        with dissolve
        p "But if you don't want to slay us, then don't slay us. Maybe there never even has to be an ending.\n"
    elif felina_loop_strange_slay_comment:
        voice "audio/voices/felina/cabin/stranger/princess/31.flac"
        show stranger c offering talk onlayer back
        with dissolve
        p "Then don't slay us. Maybe there never even has to be an ending.\n"
    else:
        voice "audio/voices/felina/cabin/stranger/princess/32.flac"
        show stranger c offering talk onlayer back
        with dissolve
        p "Maybe this doesn't have to end just yet. Maybe there never even has to be an ending.\n"
    voice "audio/voices/felina/cabin/stranger/princess/33.flac"
    show stranger c closed talk onlayer back
    with dissolve
    p "The way it all works seems to be based on you. If you believe we can do something, then we can do it\n"
    if mirror_construct:
        voice "audio/voices/felina/cabin/stranger/princess/34.flac"
        show stranger c serious talk onlayer back
        with dissolve
        p "So believe that we can put it all back. Believe we can fix the Echo's construct, and make us all forget.\n"
    else:
        voice "audio/voices/felina/cabin/stranger/princess/35.flac"
        show stranger c serious talk onlayer back
        with dissolve
        p "So believe that we can put it all back. Believe we can fix this place, and believe we can make us all forget.\n"
    voice "audio/voices/felina/cabin/stranger/princess/36.flac"
    show stranger c sad smile talk onlayer back
    with dissolve
    p "Believe we can send us all back to the beginning, before anyone woke up. Before the truth consumed us.\n"
    voice "audio/voices/felina/cabin/stranger/hero/29.flac"
    show stranger c tear onlayer back
    with dissolve
    hero "Can they really do that? Are you sure that's what you want?\n"
    voice "audio/voices/felina/cabin/stranger/contrarian/26.flac"
    contrarian "Why wouldn't it be what we want? Especially if it brings Him back. We can't keep going without a nemesis.\n"
    label loop_ending_strange_menu:
        menu:
            extend ""

            "{i}• (Explore) ''Would resetting it do anything to help {b}them{/b}? The people out there? If you continue to exist, then don't they continue to die and suffer?''{/i}" if loop_reset_help == False:
                $ loop_reset_help = True
                voice "audio/voices/felina/cabin/stranger/princess/37.flac"
                show stranger c gentle ask onlayer back
                with dissolve
                p "If you believe we can give them more time, then we can give them more time. It's all up to you\n"
                voice "audio/voices/felina/cabin/stranger/contrarian/27.flac"
                show stranger c gentle onlayer back
                with dissolve
                contrarian "Yeah. Don't underestimate the power of our thoughts. You've seen what they can do.\n"
                voice "audio/voices/felina/cabin/stranger/hero/30.flac"
                hero "You haven't even seen the half of it.\n"
                jump loop_ending_strange_menu

            "{i}• (Explore) ''I don't want to forget you.''{/i}" if loop_forget == False:
                $ loop_forget = True
                voice "audio/voices/felina/cabin/stranger/princess/38.flac"
                show stranger c sad smile talk onlayer back
                with dissolve
                p "We don't want to forget you, either. But that's what we would have to do\n"
                voice "audio/voices/felina/cabin/stranger/hero/31.flac"
                show stranger c tear onlayer back
                with dissolve
                hero "A single tear forms in one eye and slides down their cheek. Sorry, couldn't help myself.\n"
                voice "audio/voices/felina/cabin/stranger/princess/39aa.flac"
                show stranger c neutral talk onlayer back
                with dissolve
                p "We don't think we ever really forget, anyway. There's always something that draws us back together. Some buried memory that both of us treasure.\n"
                show stranger c neutral onlayer back
                with dissolve
                jump loop_ending_strange_menu

            "{i}• (Explore) ''We're going to find ourselves back here eventually.''{/i}" if loop_return == False:
                $ loop_return = True
                voice "audio/voices/felina/cabin/stranger/princess/40.flac"
                show stranger c sad smile talk onlayer back
                with dissolve
                p "And when we do, we can choose to do it all again. We'll always be able to start over. If that's what all of us want\n"
                show stranger c sad smile onlayer back
                with dissolve
                jump loop_ending_strange_menu

            "{i}• (Explore) ''If we're here talking about this right now, how do we know we haven't done this before?''{/i}" if loop_repeat == False:
                $ loop_repeat = True
                voice "audio/voices/felina/cabin/stranger/princess/41.flac"
                show stranger c shrug talk onlayer back
                with dissolve
                p "Maybe we have, maybe we haven't. We can't know something like that. But we're choosing to do it now. And maybe we'll just keep doing it again and again, forever.\n"
                voice "audio/voices/felina/cabin/stranger/princess/41a.flac"
                show stranger c sad smile talk onlayer back
                with dissolve
                p "It's... almost comforting. To know we can keep meeting each other over and over again\n"
                show stranger c sad smile onlayer back
                with dissolve
                jump loop_ending_strange_menu

            "{i}• (Explore) ''How do you know that things won't just end worse? What if when I make my way back here I'm different and I hurt you? What if I kill you? What if I let you bring about the end of everything?''{/i}" if loop_worse == False and loop_repeat:
                $ loop_worse = True
                voice "audio/voices/felina/cabin/stranger/princess/42a.flac"
                show stranger c sad smile talk onlayer back
                with dissolve
                p "That's okay. We have to be able to trust that whatever choices we make, they're the right choices.\n"
                voice "audio/voices/felina/cabin/stranger/princess/43.flac"
                show stranger c closed talk onlayer back
                with dissolve
                p "Maybe we'll continue the loop of forgetting and restarting forever. Or maybe we'll decide, at some point, that it's time for things to end.\n"
                show stranger c sad smile onlayer back
                with dissolve
                jump loop_ending_strange_menu

            "{i}• (Explore) ''But how can we trust ourselves? Our memories will be gone, and we'd have to decide to do this every single time. Forever. Eventually something is going to be different.''{/i}" if loop_worse_follow == False and loop_worse:
                $ loop_worse_follow = True
                voice "audio/voices/felina/cabin/stranger/princess/44.flac"
                show stranger c gentle ask onlayer back
                with dissolve
                p "When we first met each other in the Long Quiet, there was... something inside of us, something we couldn't recognize or understand. And we can't say we fully understand it now.\n"
                voice "audio/voices/felina/cabin/stranger/princess/44a.flac"
                show stranger c serious talk onlayer back
                with dissolve
                p "A warmth when we look at you, the kind you don't realize you're missing until it's come back.\n"
                voice "audio/voices/felina/cabin/stranger/princess/45.flac"
                show stranger c closed talk onlayer back
                with dissolve
                p "Every time we hurt each other, every time something awful happened, it was still there. Undercutting the pain on the surface with a constant soothing glow.\n"
                voice "audio/voices/felina/cabin/stranger/princess/46.flac"
                show stranger c sad smile talk onlayer back
                with dissolve
                p "That warmth is never going to go away. And that's why we believe in you.\n"
                show stranger c sad smile onlayer back
                with dissolve
                jump loop_ending_strange_menu

            "{i}• (Explore) ''This isn't fair. I want to be here with you. I don't want to be alone again.''{/i}" if loop_fair == False:
                $ loop_fair = True
                voice "audio/voices/felina/cabin/stranger/princess/47.flac"
                show stranger c gentle ask onlayer back
                with dissolve
                p "You'll be back here again, sooner than you think. And then we'll part ways again, and find each other, and part ways, and find each other. It's like we're never really alone.\n"
                voice "audio/voices/felina/cabin/stranger/princess/48.flac"
                show stranger c sad smile talk onlayer back
                with dissolve
                p "Because even the time we spend apart is time spent chasing these moments of reunion. And they're all the sweeter for the isolation in between, don't you think?\n"
                voice "audio/voices/felina/cabin/stranger/contrarian/28.flac"
                show stranger c sad smile onlayer back
                with dissolve
                contrarian "{i}Sniff{/i}. That's beautiful.\n"
                voice "audio/voices/felina/cabin/stranger/hero/32.flac"
                hero "You've really grown a heart, haven't you?\n"
                jump loop_ending_strange_menu

            "{i}• (Explore) ''Is there any other way?''{/i}" if loop_other_way == False:
                $ loop_other_way = True
                voice "audio/voices/felina/cabin/stranger/princess/49alt.flac"
                show stranger c sad smile talk onlayer back
                with dissolve
                p "Our options are limited to what that knife offers us. Either we use it to put things back, or... you kill us. We're sure you can figure out which one we'd prefer\n"
                voice "audio/voices/felina/cabin/stranger/princess/50.flac"
                show stranger c closed talk onlayer back
                with dissolve
                p "But we don't want to influence you. We're sure you'll do what you think is best. If it's time for it to be over, it's time for it to be over. As much as we might want a few more precious lifetimes with you\n"
                show stranger c sad smile onlayer back
                with dissolve
                jump loop_ending_strange_menu

            "{i}• (Explore) ''I take it all back. I don't want this, and I don't want to kill you. Is it too late to go back to being a god?''{/i}" if loop_regret == False:
                $ loop_regret = True
                voice "audio/voices/felina/cabin/stranger/princess/51.flac"
                show stranger c closed talk onlayer back
                with dissolve
                p "There's no turning back now. You came down here with the knife, which means the knife has to get used. Or there wouldn't have been any meaning to taking it. And this place is all about meaning\n"
                voice "audio/voices/felina/cabin/stranger/princess/52.flac"
                show stranger c sad smile talk onlayer back
                with dissolve
                p "But if that's what you want, you can always hope that the next you will want that, too. But there's only one way to give him that choice\n"
                voice "audio/voices/felina/cabin/stranger/contrarian/29.flac"
                show stranger c sad smile onlayer back
                with dissolve
                contrarian "Yeah. We're already here, and we've already brought the blade, and nobody wanted to throw it out the window. We can't just go back now. One way or another, we'll have to see this through.\n"
                voice "audio/voices/felina/cabin/stranger/hero/33.flac"
                hero "There's your third beat.\n"
                voice "audio/voices/felina/cabin/stranger/contrarian/30.flac"
                contrarian "Hey! You're right. There it is. Can't say it's very funny, though.\n"
                jump loop_ending_strange_menu

            "{i}• ''Okay. Then let's do it. I believe in us.'' [[Agree to her plan.]{/i}":
                voice "audio/voices/felina/cabin/stranger/hero/34.flac"
                show stranger c tear onlayer back
                with dissolve
                hero "Okay. If this is your choice, then I have your back. I guess I'll see you on the other side.\n"
                voice "audio/voices/felina/cabin/stranger/contrarian/31.flac"
                contrarian "Speak for yourself. Maybe I'll see you two, maybe I won't.\n"
                $ blade_held = False
                $ default_mouse = "default"
                play audio "audio/one_shot/knife_pickup.flac"
                voice "audio/voices/felina/cabin/stranger/hero/35.flac"
                show stranger c take blade onlayer back
                with Dissolve(1.0)
                if persistent.quick_menu:
                    $ quick_menu = True
                hero "They take the blade from our hand and stare fondly into our eyes.\n"
                show stranger c final words onlayer back
                with dissolve
                menu:

                    extend ""

                    "{i}• ''I love you.''{/i}":
                        voice "audio/voices/felina/cabin/stranger/princess/53.flac"
                        show stranger c final words talk onlayer back
                        with dissolve
                        p "We love you too. Everything is going to be okay.\n"
                        # she strikes. game goes back to the Real chapter 1

                    "{i}• ''Just do it.''{/i}":
                        voice "audio/voices/felina/cabin/stranger/princess/54.flac"
                        show stranger c final words talk onlayer back
                        with dissolve
                        p "Everything is going to be okay. We love you.\n"
                        # she strikes. game goes back to the Real chapter 1

                    "{i}• ''I'll see you soon.''{/i}":
                        voice "audio/voices/felina/cabin/stranger/princess/54.flac"
                        show stranger c final words talk onlayer back
                        with dissolve
                        p "Everything is going to be okay. We love you.\n"
                        # she strikes. game goes back to the Real chapter 1

                    "{i}• [[Remain silent.]{/i}":
                        voice "audio/voices/felina/cabin/stranger/hero/36.flac"
                        hero "Yeah. It's better if we don't say anything.\n"
                        voice "audio/voices/felina/cabin/stranger/princess/54.flac"
                        show stranger c final words talk onlayer back
                        with dissolve
                        p "Everything is going to be okay. We love you.\n"
                        # she strikes. game goes back to the Real chapter 1


                show stranger c finale onlayer back
                with dissolve
                $ renpy.pause(0.25)
                stop music
                stop sound
                hide stranger onlayer back
                hide bg onlayer farback
                play audio "audio/final/Tower_KnifeBlow_3.flac"
                scene bg black
                $ renpy.pause(2.0)
                $ gallery_zfinale.unlock_item(12)
                $ renpy.save_persistent()
                jump loop_ending

            "{i}• ''I'm sorry, but I can't do that.'' [[Slay the Princess.]{/i}":
                stop music fadeout 1.0
                $ felina_slain_apologize = True
                jump felina_slain_start

            "{i}• [[Slay the Princess.]{/i}":
                stop music fadeout 1.0
                voice "audio/voices/felina/cabin/stranger/hero/27.flac"
                hero "So this is really it then. Let's see this through.\n"
                jump felina_slain_start
return
