label felina_cabin_hostile_start:

    if blade_held == False:
        if felina_stated_goal == "slay":
            voice "audio/voices/felina/cabin/harsh/princess/1.flac"
            show princess dn haughty onlayer back at Position(ypos=1125)
            with dissolve
            p "And there you are. Hands empty. And here I thought you wanted to kill me. Are you getting cold feet? Are you trying to give me a fighting chance?\n"
        else:
            voice "audio/voices/felina/cabin/harsh/princess/2a.flac"
            show princess dn haughty onlayer back at Position(ypos=1125)
            with dissolve
            p "And there you are. Hands empty. So you don't feel like recreating our first meeting detail for detail. I wonder what else will be different.\n"
        voice "audio/voices/felina/cabin/harsh/princess/3.flac"
        show princess dn confident onlayer back
        with dissolve
        p "Maybe there's still room for us to chat before the final curtain call. What do you say?\n"
        with dissolve
    else:
        if felina_stated_goal == "slay":
            voice "audio/voices/felina/cabin/harsh/princess/4.flac"
            show princess dn haughty onlayer back
            with dissolve
            p "And there you are, knife in hand. That sight brings me back. You're going to do it then, aren't you? You're really going to kill me.\n"
        else:
            voice "audio/voices/felina/cabin/harsh/princess/5.flac"
            show princess dn haughty onlayer back
            with dissolve
            p "And there you are, knife in hand. It really brings me back. Have you given up on talking? Have you finally decided to kill me?\n"
        voice "audio/voices/felina/cabin/harsh/princess/6.flac"
        show princess dn glance talk onlayer back
        with dissolve
        p "You'll have all of eternity to yourself after this. Why don't we chat a little before I go?\n"
        show princess dn glance onlayer back
        with dissolve

    menu:
        extend ""

        "{i}• [[Slay the Princess.]{/i}" if blade_held:
            voice "audio/voices/felina/cabin/harsh/hero/1.flac"
            hero "So this is it, then. Let's see this through.\n"
            play secondary "audio/one_shot/footstep_run_medium.flac"
            # play little animatic of her being slain
            jump felina_slain_start

        "{i}• [[Sit with her.]{/i}":
            $ gallery_zfinale.unlock_item(6)
            $ renpy.save_persistent()
            "{nw}"
            show screen disableclick(0.5)
            if blade_held:
                $ quick_menu = False
                play audio "audio/final/footsteps_stone_short.flac"
                hide bodies onlayer farback
                hide bg onlayer back
                hide princess onlayer back
                show bg basement close onlayer farback at Position(ypos=1125)
                show princess c harsh neutral onlayer back at Position(ypos=1125)
                with fade
                if persistent.quick_menu:
                    $ quick_menu = True
                jump felina_cabin_hostile_menu_blade
            else:
                $ quick_menu = False
                play audio "audio/final/footsteps_stone_short.flac"
                hide bodies onlayer farback
                hide bg onlayer back
                hide princess onlayer back
                show bg basement close onlayer farback at Position(ypos=1125)
                show princess c harsh neutral onlayer back at Position(ypos=1125)
                with fade
                if persistent.quick_menu:
                    $ quick_menu = True
                jump felina_cabin_hostile_menu_empty

label felina_cabin_hostile_menu_empty:
    default hostile_slay_comment = False
    menu:
        extend ""

        "{i}• (Explore) ''It's so good to finally see you again.''{/i}" if felina_leave_intro == False:
            $ felina_leave_intro = True
            $ felina_leave_count += 1
            voice "audio/_pristine/voice/_climax/cabin_endings/harsh/22.flac"
            show princess c coy talk onlayer back
            with dissolve
            p "Right back at you. In a way, it hasn't been much time at all, but it feels like it's been forever since I've seen you. Thanks for coming back.\n"
            show princess c coy onlayer back
            with dissolve
            jump felina_cabin_hostile_menu_empty

        "{i}• (Explore) ''I'm sorry for all of the times I've hurt you.''{/i}" if felina_leave_apologize == False:
            $ felina_leave_apologize = True
            $ felina_leave_count += 1
            if first_mound == "prisonerhead" or first_mound == "prisonerchain" or first_mound == "greyprisoner" or first_mound == "cage":
                voice "audio/_pristine/voice/_climax/cabin_endings/harsh/3.flac"
                show princess c shrug talk upbeat onlayer back
                with dissolve
                p "{i}Laughing{/i}. The first time we met I cut your throat open. If anyone should be apologizing for anything, it should be me. You were only trying to help.\n"
            if first_mound == "razor" or first_mound == "razorheart":
                if razor_revival:
                    voice "audio/_pristine/voice/_climax/cabin_endings/harsh/4.flac"
                    show princess c shrug talk upbeat onlayer back
                    with dissolve
                    p "{i}Laughing{/i}. The first time we met I stabbed you to death.\n"
                    voice "audio/_pristine/voice/_climax/cabin_endings/harsh/5a.flac"
                    show princess c coy talk onlayer back
                    with dissolve
                    p "Sure, you stabbed me first, but who cares? We, uh... we both took things a little far.\n"
                    #p "Sure, you stabbed me first, but who cares? We, uh... we both took things a little far. But now we're here. It's no big deal.\n"
                else:
                    voice "audio/_pristine/voice/_climax/cabin_endings/harsh/6.flac"
                    show princess c shrug talk upbeat onlayer back
                    with dissolve
                    p "{i}Laughing{/i}. The first time we met I cut your throat open.\n"
                    if razor_loop1_killed:
                        voice "audio/_pristine/voice/_climax/cabin_endings/harsh/7.flac"
                        show princess c coy talk onlayer back
                        with dissolve
                        p "Sure, you also killed me, but hey. That just makes us even.\n"
                    else:
                        voice "audio/_pristine/voice/_climax/cabin_endings/harsh/8.flac"
                        show princess c coy talk onlayer back
                        with dissolve
                        p "You didn't even try and get me back for that! You just died. If anyone should be apologizing here, it should be me.\n"

            if first_mound == "nightmare" or first_mound == "clarity" or (first_mound == "wraith" and wraith_source == "nightmare"):
                #voice "audio/_pristine/voice/_climax/cabin_endings/harsh/9.flac"
                #p "{i}Laughing{/i}. The first time we met I scared you so much your organs stopped working. All of them. And I meant to do that. If anyone should be apologizing here, it should be me.\n"
                voice "audio/_pristine/voice/_climax/cabin_endings/harsh/9a.flac"
                show princess c shrug talk upbeat onlayer back
                with dissolve
                p "{i}Laughing{/i}. The first time we met I scared you so much your organs stopped working. And I meant to do that. If anyone should be apologizing here, it should be me.\n"
                voice "audio/_pristine/voice/_climax/cabin_endings/harsh/10.flac"
                show princess c coy talk onlayer back
                with dissolve
                p "But hey, we both took things a little far, didn't we? It's no big deal. All of that's behind us now, I think.\n"

            if first_mound == "spectre" or (first_mound == "wraith" and wraith_source == "spectre") or first_mound == "dragon" or first_mound == "dragonfused" or first_mound == "dragonhand":
                voice "audio/_pristine/voice/_climax/cabin_endings/harsh/11.flac"
                show princess c shrug talk upbeat onlayer back
                with dissolve
                p "{i}Laughing{/i}. Well, you did stab me to death as soon as we met, but it's not like I'm completely innocent. We both took things a little far.\n"
                voice "audio/_pristine/voice/_climax/cabin_endings/harsh/12.flac"
                show princess c coy talk onlayer back
                with dissolve
                p "Still. Apology accepted.\n"

            if first_mound == "tower" or first_mound == "apotheosis" or ((first_mound == "fury" or first_mound == "furyheart") and fury_source == "tower"):
                voice "audio/_pristine/voice/_climax/cabin_endings/harsh/13.flac"
                show princess c shrug talk upbeat onlayer back
                with dissolve
                p "{i}Laughing{/i}. The first time we met I literally beat you to death with my bare hands. You don't have to apologize to me.\n"
                voice "audio/_pristine/voice/_climax/cabin_endings/harsh/14.flac"
                show princess c sad smile talk onlayer back
                with dissolve
                p "But still, I appreciate it. And I hope you can also forgive me.\n"

            if first_mound == "adversary" or first_mound == "needle" or ((first_mound == "fury" or first_mound == "furyheart") and fury_source != "tower"):
                voice "audio/_pristine/voice/_climax/cabin_endings/harsh/15.flac"
                show princess c shrug talk upbeat onlayer back
                with dissolve
                p "{i}Laughing{/i}. The first time we met you stabbed me in the heart and I beat you to death with my bare hands. And it was fun! You really don't have to apologize.\n"
                voice "audio/_pristine/voice/_climax/cabin_endings/harsh/16.flac"
                show princess c sad smile talk onlayer back
                with dissolve
                p "We both went a little overboard. But there's no reason we can't put it all behind us.\n"

            voice "audio/_pristine/voice/_climax/cabin_endings/leave/hero/1.flac"
            show princess c coy onlayer back
            with dissolve
            hero "You know, when she puts it like that...\n"
            jump felina_cabin_hostile_menu_empty

        "{i}• (Explore) ''I don't think I want to be a god.''{/i}" if felina_cabin_god_comment == False:
            $ felina_cabin_god_comment = True
            $ felina_leave_count += 1
            voice "audio/_pristine/voice/_climax/cabin_endings/harsh/1.flac"
            show princess c closed talk onlayer back
            with dissolve
            p "Does it matter what we call ourselves? It's just another label, and I don't think labels have ever helped us. All they do is cram us into boxes where we don't fit.\n"
            voice "audio/_pristine/voice/_climax/cabin_endings/harsh/1b.flac"
            show princess c embarrassed talk onlayer back
            with dissolve
            p "Just like this cabin.\n"
            show princess c embarrassed onlayer back
            with dissolve
            jump felina_cabin_hostile_menu_empty

        "{i}• (Explore) ''Are you... the same as you are out there?''{/i}" if felina_cabin_same_comment == False:
            $ felina_cabin_same_comment = True
            $ felina_leave_count += 1
            voice "audio/_pristine/voice/_climax/cabin_endings/harsh/2b.flac"
            show princess c regret talk onlayer back
            with dissolve
            p "I don't know. I'm a part of her, I think. But she's seen so much more than we have. Like, she's seen {i}everything{/i}, right? I don't think I could hold all of that without losing myself. I don't think you could, either.\n"
            show princess c sad dart onlayer back
            with dissolve
            jump felina_cabin_hostile_menu_empty

        "{i}• (Explore) ''Which... Princess are you? You look like you did the first time we met. Is this the real you?''{/i}" if felina_leave_which_princess == False:
            $ felina_leave_which_princess = True
            $ felina_leave_count += 1
            voice "audio/_pristine/voice/_climax/cabin_endings/harsh/17.flac"
            show princess c tsundere talk onlayer back
            with dissolve
            p "I'm the same Princess that's been with you since the beginning. And I feel real.\n"
            voice "audio/_pristine/voice/_climax/cabin_endings/harsh/17a.flac"
            show princess c wistful talk onlayer back
            with dissolve
            p "But I also feel like I'm a lot... more than I was then? We've been through a lot together. I don't think there's anything more real than that.\n"
            show princess c wistful onlayer back
            with dissolve
            jump felina_cabin_hostile_menu_empty

        "{i}• (Explore) ''So, now that we're here at the end of everything... can you finally tell me your name?''{/i}" if felina_leave_name == False:
            $ felina_leave_name = True
            $ felina_leave_count += 1
            if felina_menu_names or mirror_mound_reveal:
                voice "audio/_pristine/voice/_climax/cabin_endings/harsh/18.flac"
                show princess c tsundere talk onlayer back
                with dissolve
                p "Ha! I never had one. And {i}do not{/i} call me 'The Shifting Mound.' It's too much.\n"
            else:
                voice "audio/_pristine/voice/_climax/cabin_endings/harsh/18a.flac"
                show princess c tsundere talk onlayer back
                with dissolve
                p "Ha! I never had one.\n"
            voice "audio/_pristine/voice/_climax/cabin_endings/harsh/19a.flac"
            show princess c shrug upbeat talk onlayer back
            with dissolve
            p "But I've always been a Princess to you, right? So why don't we stick with that?\n"
            voice "audio/_pristine/voice/_climax/cabin_endings/harsh/20.flac"
            show princess c sad smile talk onlayer back
            with dissolve
            p "And as for you, well... 'hero' works for me.\n"
            voice "audio/_pristine/voice/_climax/cabin_endings/leave/hero/3.flac"
            show princess c sad smile onlayer back
            with dissolve
            hero "But that's me! You know... I think I like that.\n"
            jump felina_cabin_hostile_menu_empty

        "{i}• (Explore) ''None of this was ever really fair for either of us, was it?''{/i}" if felina_leave_fair == False:
            $ felina_leave_fair = True
            $ felina_leave_count += 1
            voice "audio/_pristine/voice/_climax/cabin_endings/harsh/21.flac"
            show princess c coy talk onlayer back
            with dissolve
            p "No. It really wasn't. But just because it hasn't been fair doesn't mean that it hasn't been worth it. I'm... really glad I got to know you.\n"
            show princess c coy onlayer back
            with dissolve
            jump felina_cabin_hostile_menu_empty

        "{i}• (Explore) ''I only wanted to slay the you out there. It's easier to want to kill an abstract concept than it is a person.''{/i}" if felina_stated_goal == "slay" and hostile_slay_comment == False:
            $ hostile_slay_comment = True
            $ felina_leave_count += 1
            voice "audio/voices/felina/cabin/harsh/princess/9a.flac"
            show princess c shrug talk upbeat onlayer back
            with dissolve
            p "Well, for what it's worth, I'm glad you don't want to kill me anymore. So what's your plan?\n"
            show princess c wistful onlayer back
            with dissolve
            jump felina_cabin_hostile_menu_empty

        "{i}• (Explore) ''I don't think I ever really wanted to slay you. But I don't like what your existence means for the world.''{/i}" if felina_stated_goal == "slay" and hostile_slay_comment == False:
            $ hostile_slay_comment = True
            $ felina_leave_count += 1
            voice "audio/voices/felina/cabin/harsh/princess/10.flac"
            show princess c shrug talk upbeat onlayer back
            with dissolve
            p "You were the one who decided to come down here without a weapon. So what's your plan?\n"
            show princess c wistful onlayer back
            with dissolve
            jump felina_cabin_hostile_menu_empty

        "{i}• (Explore) ''What do you think of Her? What She wanted us to be.''{/i}" if felina_leave_mound_thoughts == False:
            $ felina_leave_count += 1
            $ felina_leave_mound_thoughts = True
            voice "audio/_pristine/voice/_climax/cabin_endings/harsh/23.flac"
            show princess c closed talk onlayer back
            with dissolve
            p "I don't think she's the sort of thing you can really disagree with. It doesn't matter if she's right or wrong, because she exists. She's this big unrelenting force, and there's no arguing with her.\n"
            voice "audio/_pristine/voice/_climax/cabin_endings/harsh/24.flac"
            show princess c embarrassed talk onlayer back
            with dissolve
            p "But I guess that was the question out there, wasn't it? And it was the question before you came down here, too. Should she get to exist?\n"
            voice "audio/_pristine/voice/_climax/cabin_endings/harsh/25.flac"
            show princess c nerves talk onlayer back
            with dissolve
            p "... I'm glad you didn't bring that knife with you.\n"
            if felina_cabin_same_comment:
                voice "audio/_pristine/voice/_climax/cabin_endings/harsh/26.flac"
                show princess c sad smile talk onlayer back
                with dissolve
                p "And like I said earlier, I don't really want to be her. I think I just want to be me.\n"
            else:
                voice "audio/_pristine/voice/_climax/cabin_endings/harsh/27.flac"
                show princess c sad smile talk onlayer back
                with dissolve
                p "And I don't want to {i}be{/i} her, if that's what you're asking. I think I just want to be me.\n"
            voice "audio/_pristine/voice/_climax/cabin_endings/leave/hero/7.flac"
            show princess c sad smile onlayer back
            with dissolve
            hero "Yeah. I'm happy not to be everything. Just being us is plenty.\n"
            jump felina_cabin_hostile_menu_empty

        "{i}• ''What if we just leave?''{/i}" if felina_leave_count < 9:
            show princess c serious final onlayer back
            with dissolve
            jump felina_hostile_leave_join_menu

        "{i}• ''I think the only thing left for us to do here is leave.''{/i}" if felina_leave_count >= 9:
            show princess c serious final onlayer back
            with dissolve
            label felina_hostile_leave_join_menu:
                voice "audio/voices/felina/cabin/harsh/princess/11a.flac"
                show princess c serious final talk onlayer back
                with dissolve
                p "Do you know where this cabin is? Because I don't. I don't even know what's supposed to be outside other than... us. What would even happen if we leave? What would that even mean?\n"
                show princess c serious final onlayer back
                with dissolve
                label felina_harsh_hand_menu:
                    menu:
                        extend ""

                        "{i}• (Explore) [[Take her hand in yours.]{/i}" if felina_cabin_leave_hand_hold == False:
                            $ felina_cabin_leave_hand_hold = True
                            play music "audio/_music/mound/The Unknown Together Live Intro.flac"
                            queue music "audio/_music/mound/The Unknown Together Live Loop.flac" loop
                            show princess c harsh hold hand onlayer back
                            with Dissolve(1.0)
                            jump felina_harsh_hand_menu
                            #voice "audio/voices/felina/cabin/harsh/princess/15.flac"
                            #show princess c harsh hold hand blush talk onlayer back
                            #with dissolve
                            #p "Okay, then. Let's leave.\n"
                            #show princess c harsh hold hand blush onlayer back
                            #with dissolve
                            jump felina_harsh_hand_menu

                        "{i}• ''I don't know, but I've always wanted to leave with you, I just didn't like being a god. I want to walk through that cabin door as we are. Just you and me.''{/i}":
                            if felina_cabin_leave_hand_hold:
                                show princess c soft hold hand blush onlayer back
                                with Dissolve(0.4)
                                $ renpy.pause(1.0)
                            else:
                                show princess c embarrassed onlayer back
                                with dissolve
                            voice "audio/voices/felina/cabin/harsh/princess/12.flac"
                            if felina_cabin_leave_hand_hold:
                                show princess c soft hold hand blush talk onlayer back
                                with dissolve
                            else:
                                show princess c embarrassed talk onlayer back
                                with dissolve
                            p "... I want that too.\n"

                        "{i}• ''Not knowing what it means is why I want it. We knew everything out there, but we don't know this. I want to know this.''{/i}":
                            if felina_cabin_leave_hand_hold:
                                show princess c soft hold hand blush onlayer back
                                with Dissolve(0.4)
                                $ renpy.pause(1.0)
                            else:
                                show princess c embarrassed onlayer back
                                with dissolve
                            voice "audio/voices/felina/cabin/harsh/princess/13.flac"
                            if felina_cabin_leave_hand_hold:
                                show princess c soft hold hand blush talk onlayer back
                                with dissolve
                            else:
                                show princess c embarrassed talk onlayer back
                                with dissolve
                            p "I guess, when you put it that way... I want that, too.\n"


                        "{i}• ''It doesn't matter what happens or what it means. What matters is that we're leaving together. That's all I want.''{/i}":
                            if felina_cabin_leave_hand_hold:
                                show princess c soft hold hand blush onlayer back
                                with Dissolve(0.4)
                                $ renpy.pause(1.0)
                            else:
                                show princess c embarrassed onlayer back
                                with dissolve
                            voice "audio/voices/felina/cabin/harsh/princess/14.flac"
                            if felina_cabin_leave_hand_hold:
                                show princess c soft hold hand blush talk onlayer back
                                with dissolve
                            else:
                                show princess c embarrassed talk onlayer back
                                with dissolve
                            p "You know what? Yeah. I want that too.\n"

                        "{i}• [[There's no need for words. Leave with her.]{/i}" if felina_cabin_leave_hand_hold:
                            voice "audio/voices/felina/cabin/harsh/princess/15.flac"
                            show princess c harsh hold hand blush talk onlayer back
                            with dissolve
                            p "Okay, then. Let's leave.\n"
                            show princess c soft hold hand blush onlayer back
                            with dissolve
                            jump felina_leave_cabin_ending

                if felina_cabin_leave_hand_hold == False:
                    play music "audio/_music/mound/The Unknown Together Live Intro.flac"
                    queue music "audio/_music/mound/The Unknown Together Live Loop.flac" loop
                    show princess c coy onlayer back
                    with dissolve
                else:
                    show princess c soft hold hand blush onlayer back
                    with dissolve
                jump felina_leave_cabin_ending

label felina_cabin_hostile_menu_blade:
    menu:
        extend ""

        "{i}• (Explore) ''I don't think I want to be a god.''{/i}" if felina_cabin_god_comment == False:
            $ felina_cabin_god_comment = True
            voice "audio/voices/felina/cabin/harsh/princess/16.flac"
            show princess c regret talk onlayer back
            with dissolve
            p "Honestly, me neither.\n"
            show princess c regret onlayer back
            with dissolve
            jump felina_cabin_hostile_menu_blade

        "{i}• (Explore) ''Are you... the same as you are out there?''{/i}" if felina_cabin_same_comment == False:
            $ felina_cabin_same_comment = True
            voice "audio/voices/felina/cabin/harsh/princess/17.flac"
            show princess c resigned talk onlayer back
            with dissolve
            p "No. I feel like I'm myself again.\n"
            show princess c resigned onlayer back
            with dissolve
            jump felina_cabin_hostile_menu_blade

        "{i}• (Explore) ''I only wanted to slay the you out there. It's easier to want to kill an abstract concept than it is a person.''{/i}" if felina_stated_goal == "slay":
            jump felina_loop_hostile

        "{i}• (Explore) ''I don't want to hurt anyone. There has to be a way out of this.''{/i}":
            jump felina_loop_hostile

        "{i}• (Explore) ''I don't think I ever really wanted to slay you. But I don't like what your existence means for the world.''{/i}" if felina_stated_goal == "slay":
            jump felina_loop_hostile

        "{i}• (Explore) ''What are we going to do?''{/i}":
            jump felina_loop_hostile

        "{i}• (Explore) ''I don't want to have to slay you, but I don't know what other options there are.''{/i}":
            jump felina_loop_hostile

        "{i}• ''I'm sorry.'' [[Slay the Princess.]{/i}":
            $ felina_slain_apologize = True
            jump felina_slain_start

        "{i}• [[Slay the Princess.]{/i}":
            voice "audio/voices/felina/cabin/harsh/hero/2.flac"
            hero "So this is really it then. Let's see this through.\n"
            jump felina_slain_start

label felina_loop_hostile:
    play music "audio/_music/mound/Loop Ending.flac" loop
    voice "audio/voices/felina/cabin/harsh/princess/18.flac"
    show princess c tsundere talk onlayer back
    with dissolve
    p "Well, I don't want to be at the end of that knife, so how about we figure something out?\n"
    voice "audio/voices/felina/cabin/harsh/princess/19.flac"
    show princess c closed talk onlayer back
    with dissolve
    p "What if we tried doing this forever? I can do whatever you think I can, right?\n"
    if mirror_construct:
        voice "audio/voices/felina/cabin/harsh/princess/20.flac"
        show princess c harsh neutral talk onlayer back
        with dissolve
        p "So make me put it all back. Make me fix the Echo's construct and make me wipe our memories of everything that's happened.\n"
    else:
        voice "audio/voices/felina/cabin/harsh/princess/21.flac"
        show princess c harsh neutral talk onlayer back
        with dissolve
        p "So make me put it all back. Make me fix whatever this place is and make me wipe our memories of everything that's happened.\n"
    voice "audio/voices/felina/cabin/harsh/princess/22.flac"
    show princess c regret talk onlayer back
    with dissolve
    p "Make me send us back to the beginning, before we woke up. Before either of us saw the truth.\n"
    #p "Make me send us back to the beginning, before we woke up. Before either of us saw the truth. You just have to believe I can do it.\n"
    voice "audio/voices/felina/cabin/harsh/hero/3.flac"
    show princess c regret onlayer back
    with dissolve
    hero "Can she really do that? Are you sure that's what you want?\n"
    label loop_ending_hostile_menu:
        menu:
            extend ""

            "{i}• (Explore) ''Would resetting it do anything to help {b}them{/b}? The people out there? If you continue to exist, don't they continue to die and suffer?''{/i}" if loop_reset_help == False:
                $ loop_reset_help = True
                voice "audio/voices/felina/cabin/harsh/princess/23.flac"
                show princess c closed talk onlayer back
                with dissolve
                p "Fixing that is on you, not me. If you want me to help them you'll have to make me help them.\n"
                show princess c regret onlayer back
                with dissolve
                jump loop_ending_hostile_menu

            "{i}• (Explore) ''I don't want to forget you.''{/i}" if loop_forget == False:
                $ loop_forget = True
                voice "audio/voices/felina/cabin/harsh/princess/24a.flac"
                show princess c coy talk onlayer back
                with dissolve
                p "That's sweet, but unless you do, the whole world ends, right? Not like I care. But it seems important to you.\n"
                show princess c coy onlayer back
                with dissolve
                jump loop_ending_hostile_menu

            "{i}• (Explore) ''We're going to find ourselves back here eventually.''{/i}" if loop_return == False:
                $ loop_return = True
                voice "audio/voices/felina/cabin/harsh/princess/25.flac"
                show princess c serious final talk onlayer back
                with dissolve
                p "And if we do, nothing is stopping us from making the same choice. We could just keep doing this forever.\n"
                jump loop_ending_hostile_menu

            "{i}• (Explore) ''If we're talking about this right now, how do we know we haven't done this before?''{/i}" if loop_repeat == False:
                $ loop_repeat = True
                voice "audio/voices/felina/cabin/harsh/princess/26.flac"
                show princess c shrug talk onlayer back
                with dissolve
                p "I don't think that's something we'll ever get to know. But odds are we've probably done it before.\n"
                show princess c regret onlayer back
                with dissolve
                jump loop_ending_hostile_menu

            "{i}• (Explore) ''How do you know that things won't end worse? What if when I make my way back here I'm different and I hurt you? What if I kill you? What if I let you bring about the end of everything?''{/i}" if loop_worse == False and loop_repeat:
                $ loop_worse = True
                voice "audio/voices/felina/cabin/harsh/princess/27a.flac"
                show princess c wistful talk onlayer back
                with dissolve
                p "Who cares? We've hurt each other plenty, and I still like you.\n"
                voice "audio/voices/felina/cabin/harsh/princess/27aa.flac"
                show princess c embarrassed talk onlayer back
                with dissolve
                p "And if you're hesitating, then you must still like me, too.\n"
                show princess c embarrassed onlayer back
                with dissolve
                jump loop_ending_hostile_menu

            "{i}• (Explore) ''We'd have to decide to do this every single time. Forever. Eventually something is going to be different. What if we change our minds?''{/i}" if loop_worse_follow == False and loop_worse:
                $ loop_worse_follow = True
                voice "audio/voices/felina/cabin/harsh/princess/28a.flac"
                show princess c closed talk onlayer back
                with dissolve
                p "Well, if we change our minds, we change our minds. What matters is that we'll always have a choice. This is just the one we're making now.\n"
                show princess c wistful onlayer back
                with dissolve
                jump loop_ending_hostile_menu

            "{i}• (Explore) ''This isn't fair. I want to be here with you. I don't want to be alone again.''{/i}" if loop_fair == False:
                $ loop_fair = True
                voice "audio/voices/felina/cabin/harsh/princess/29.flac"
                show princess c sad smile talk onlayer back
                with dissolve
                p "... Neither do I. But we won't be alone for long. I'll be right here waiting for you.\n"
                show princess c sad smile onlayer back
                with dissolve
                jump loop_ending_hostile_menu

            "{i}• (Explore) ''Is there any other way?''{/i}" if loop_other_way == False:
                $ loop_other_way = True
                voice "audio/voices/felina/cabin/harsh/princess/30a.flac"
                show princess c resigned talk onlayer back
                with dissolve
                p "You brought that knife down here for a reason. Either you use it to kill me, or I use it to put things back.\n"
                show princess c resigned onlayer back
                with dissolve
                jump loop_ending_hostile_menu

            "{i}• (Explore) ''I take it all back. I don't want this, and I don't want to kill you. Is it too late to go back to being a god?''{/i}" if loop_regret == False:
                $ loop_regret = True
                voice "audio/voices/felina/cabin/harsh/princess/31.flac"
                show princess c sad smile talk onlayer back
                with dissolve
                p "Yeah. I think it's too late for that. But maybe next time.\n"
                show princess c sad smile onlayer back
                with dissolve
                jump loop_ending_hostile_menu

            "{i}• ''Okay. Then let's do it. I believe in us.'' [[Agree to her plan.]{/i}":
                voice "audio/voices/felina/cabin/harsh/hero/4.flac"
                show princess c sad smile onlayer back
                with dissolve
                hero "Okay. If this is your choice, then I have your back. I guess I'll see you on the other side.\n"
                show princess c harsh blade take onlayer back
                with Dissolve(1.0)
                voice "audio/voices/felina/cabin/harsh/hero/4a.flac"
                $ blade_held = False
                $ default_mouse = "default"
                play audio "audio/one_shot/knife_pickup.flac"
                show princess c harsh final words onlayer back
                with Dissolve(1.0)
                hero "She takes the blade from our hand, a fondness in her gaze.\n"
                menu:

                    extend ""

                    "{i}• ''I love you.''{/i}":
                        show princess c final words smile tears onlayer back
                        with dissolve
                        voice "audio/voices/felina/cabin/harsh/princess/32a.flac"
                        show princess c final words smile talk tears onlayer back
                        with dissolve
                        p "Oh... I love you too.\n"
                        # she strikes. game goes back to the Real chapter 1

                    "{i}• ''Just do it.''{/i}":
                        show princess c final words smile tears onlayer back
                        with dissolve
                        voice "audio/voices/felina/cabin/harsh/princess/33.flac"
                        show princess c final words smile talk tears onlayer back
                        with dissolve
                        p "Hey. I love you.\n"
                        # she strikes. game goes back to the Real chapter 1

                    "{i}• ''I'll see you soon.''{/i}":
                        show princess c final words smile tears onlayer back
                        with dissolve
                        voice "audio/voices/felina/cabin/harsh/princess/33.flac"
                        show princess c final words smile talk tears onlayer back
                        with dissolve
                        p "Hey. I love you.\n"
                        # she strikes. game goes back to the Real chapter 1

                    "{i}• [[Remain silent.]{/i}":
                        voice "audio/voices/felina/cabin/soft/hero/5.flac"
                        show princess c final words smile tears onlayer back
                        with dissolve
                        hero "Yeah. It's better if we don't say anything.\n"
                        voice "audio/voices/felina/cabin/harsh/princess/33.flac"
                        show princess c final words smile talk tears onlayer back
                        with dissolve
                        p "Hey. I love you.\n"
                        # she strikes. game goes back to the Real chapter 1

                $ gallery_zfinale.unlock_item(7)
                $ renpy.save_persistent()
                show princess c harsh stab onlayer back
                with dissolve
                $ renpy.pause(0.25)
                hide princess onlayer back
                hide bg onlayer farback
                stop music
                stop sound
                play audio "audio/final/Tower_KnifeBlow_3.flac"
                scene bg black
                $ renpy.pause(2.0)
                jump loop_ending

            "{i}• ''I'm sorry, but I can't do that.'' [[Slay the Princess.]{/i}":
                $ felina_slain_apologize = True
                stop music fadeout 1.0
                jump felina_slain_start

            "{i}• [[Slay the Princess.]{/i}":
                stop music fadeout 1.0
                voice "audio/voices/felina/cabin/harsh/hero/2.flac"
                hero "So this is really it then. Let's see this through.\n"
                jump felina_slain_start
return
