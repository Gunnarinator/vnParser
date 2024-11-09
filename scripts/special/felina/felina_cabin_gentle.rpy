label felina_cabin_gentle_start:

    if blade_held == False:
        if felina_stated_goal == "slay":
            voice "audio/voices/felina/cabin/soft/princess/1.flac"
            show princess dn glance talk onlayer back
            with dissolve
            p "You don't have a weapon. Do you really want to kill me? Because you don't have to.\n"
            show princess dn glance onlayer back
            with dissolve
        else:
            voice "audio/voices/felina/cabin/soft/princess/2.flac"
            show princess dn questioning talk onlayer back
            with dissolve
            p "There you are. You look just like you did when we first met. Let's talk for a bit. Maybe we can figure this out.\n"
            show princess dn questioning onlayer back
            with dissolve

    else:
        if felina_stated_goal == "slay":
            voice "audio/voices/felina/cabin/soft/princess/3.flac"
            show princess dn glance talk onlayer back
            with dissolve
            p "You're really going to do it then, aren't you? You're really going to kill me. You don't have to, you know that, right?\n"
            voice "audio/voices/felina/cabin/soft/princess/4.flac"
            show princess dn questioning talk onlayer back
            with dissolve
            p "But if that's what you want, we might as well talk a bit first. I wouldn't mind a few extra minutes.\n"
            show princess dn questioning onlayer back
            with dissolve
        else:
            voice "audio/voices/felina/cabin/soft/princess/5.flac"
            show princess dn scared talk onlayer back
            with dissolve
            p "Wh-what's that knife for? Have you changed your mind? Are you going to kill me?\n"
            voice "audio/voices/felina/cabin/soft/princess/6.flac"
            show princess dn glance talk onlayer back
            with dissolve
            p "What if we just talk for a bit? Maybe we can figure this out.\n"
            show princess dn glance onlayer back
            with dissolve

    menu:
        extend ""

        "{i}• [[Slay the Princess.]{/i}" if blade_held:
            voice "audio/voices/felina/cabin/soft/hero/1.flac"
            hero "So this is really it, then. Let's see this through.\n"
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
                show princess c sad smile onlayer back at Position(ypos=1125)
                with fade
                if persistent.quick_menu:
                    $ quick_menu = True
                jump felina_cabin_gentle_menu_blade
            else:
                $ quick_menu = False
                play audio "audio/final/footsteps_stone_short.flac"
                hide bodies onlayer farback
                hide bg onlayer back
                hide princess onlayer back
                show bg basement close onlayer farback at Position(ypos=1125)
                show princess c sad smile onlayer back at Position(ypos=1125)
                with fade
                if persistent.quick_menu:
                    $ quick_menu = True
                jump felina_cabin_gentle_menu_empty

label felina_cabin_gentle_menu_empty:
    menu:
        extend ""

        "{i}• (Explore) ''It's so good to finally see you again.''{/i}" if felina_leave_intro == False:
            $ felina_leave_intro = True
            $ felina_leave_count += 1
            voice "audio/_pristine/voice/_climax/cabin_endings/soft/22c.flac"
            show princess c gentle ask onlayer back
            with dissolve
            p "Yeah! I missed you so much! Not that we've ever really been apart, but still. It feels like it's been so, so long. Like this is some sort of a big reunion.\n"
            show princess c soft neutral onlayer back
            with dissolve
            jump felina_cabin_gentle_menu_empty

        "{i}• (Explore) ''I'm sorry for all of the times I've hurt you.''{/i}" if felina_leave_apologize == False:
            $ felina_leave_apologize = True
            $ felina_leave_count += 1
            if first_mound == "damsel" or first_mound == "dereal" or first_mound == "greydamsel" or first_mound == "happy" or first_mound == "happydry":
                voice "audio/_pristine/voice/_climax/cabin_endings/soft/6.flac"
                show princess c wide eyed talk onlayer back
                with dissolve
                p "You are so sweet, but the first time we met, you tried to rescue me and I stabbed you like fifty times in the chest. And you know how bad of a job I did. You were the one getting stabbed.\n"
                voice "audio/_pristine/voice/_climax/cabin_endings/soft/7.flac"
                show princess c nerves talk onlayer back
                with dissolve
                p "I mean, yes, you were possessed by that freaky voice living in your head, but I also could have maybe tried doing anything else before deciding to kill you.\n"
                voice "audio/_pristine/voice/_climax/cabin_endings/soft/8.flac"
                show princess c sad dart talk onlayer back
                with dissolve
                p "Anyways, I'm... also sorry.\n"
            if first_mound == "nightmare" or first_mound == "clarity" or (first_mound == "wraith" and wraith_source == "nightmare"):
                voice "audio/_pristine/voice/_climax/cabin_endings/soft/9.flac"
                show princess c nerves talk onlayer back
                with dissolve
                p "That is so sweet, but the first time we met, I literally scared you to death. You were just doing your best. I should be the one who's sorry, and I am. I'm sorry.\n"
            if first_mound == "beast" or first_mound == "den" or ((first_mound == "wildwound" or first_mound == "wildnerves") and wild_source == "beast"):
                voice "audio/_pristine/voice/_climax/cabin_endings/soft/10.flac"
                show princess c nerves talk onlayer back
                with dissolve
                p "Don't apologize! The first time we met I {i}ate{/i} you! I'm really sorry about that! And I also think that it kind of outweighs anything you did to me.\n"
            if first_mound == "witch" or first_mound == "thorn" or ((first_mound == "wildwound" or first_mound == "wildnerves") and wild_source == "witch"):
                voice "audio/_pristine/voice/_climax/cabin_endings/soft/11.flac"
                show princess c sad smile talk onlayer back
                with dissolve
                p "No, no, I'm sorry too! We've done a lot to each other. Like, a lot. But I still like you! And hopefully you still like me!\n"

            voice "audio/_pristine/voice/_climax/cabin_endings/soft/12.flac"
            show princess c wistful talk onlayer back
            with dissolve
            p "We both let things get a little out of hand, but we don't have to let that stop us from being who we want to be.\n"
            voice "audio/_pristine/voice/_climax/cabin_endings/leave/hero/1.flac"
            show princess c wistful onlayer back
            with dissolve
            hero "You know, when she puts it like that...\n"
            jump felina_cabin_gentle_menu_empty

        "{i}• (Explore) ''I don't think I want to be a god.''{/i}" if felina_cabin_god_comment == False:
            $ felina_cabin_god_comment = True
            $ felina_leave_count += 1
            voice "audio/_pristine/voice/_climax/cabin_endings/soft/1.flac"
            show princess c regret talk onlayer back
            with dissolve
            p "Me neither. It's so... big. It's so much responsibility. And at the end of the day, it just feels like waking up in another basement. It's something we never asked for trapping us somewhere we never wanted to be.\n"
            show princess c sad smile onlayer back
            with dissolve
            jump felina_cabin_gentle_menu_empty

        "{i}• (Explore) ''Are you... the same as you are out there?''{/i}" if felina_cabin_same_comment == False:
            $ felina_cabin_same_comment = True
            $ felina_leave_count += 1
            voice "audio/_pristine/voice/_climax/cabin_endings/soft/2.flac"
            show princess c closed talk onlayer back
            with dissolve
            p "'I am she as much as she is me and all of us are both everything and also... not everything.'\n"
            voice "audio/_pristine/voice/_climax/cabin_endings/soft/3.flac"
            show princess c coy talk onlayer back
            with dissolve
            p "Hehe. I had you there for a second, didn't I?\n"
            voice "audio/_pristine/voice/_climax/cabin_endings/soft/4.flac"
            show princess c gentle ask onlayer back
            with dissolve
            p "I think I'm... different from her? And I'm happy I'm different.\n"
            voice "audio/_pristine/voice/_climax/cabin_endings/soft/5.flac"
            show princess c sad smile talk onlayer back
            with dissolve
            p "I think being her would mean I'd lose a lot of myself along the way. I think I'd have to lose the parts of you that matter to me.\n"
            show princess c sad smile onlayer back
            with dissolve
            jump felina_cabin_gentle_menu_empty

        "{i}• (Explore) ''Which... Princess are you? You look like you did the first time we met. Is this the real you?''{/i}" if felina_leave_which_princess == False:
            $ felina_leave_which_princess = True
            $ felina_leave_count += 1
            voice "audio/_pristine/voice/_climax/cabin_endings/soft/13a.flac"
            show princess c wide eyed talk onlayer back
            with dissolve
            p "I'm the Princess. The one you've been spending all this time with. I know I've changed a few times, but so have you.\n"
            voice "audio/_pristine/voice/_climax/cabin_endings/soft/14a.flac"
            show princess c sad smile talk onlayer back
            with dissolve
            p "And you're still real to me.\n"
            show princess c wistful onlayer back
            with dissolve
            jump felina_cabin_gentle_menu_empty

        "{i}• (Explore) ''So, now that we're here at the end of everything... can you finally tell me your name?''{/i}" if felina_leave_name == False:
            $ felina_leave_name = True
            $ felina_leave_count += 1
            voice "audio/_pristine/voice/_climax/cabin_endings/soft/15.flac"
            show princess c gentle ask onlayer back
            with dissolve
            p "I don't have one! And I think I like it better that way. But... you {i}can{/i} call me Princess, if you want.\n"
            voice "audio/_pristine/voice/_climax/cabin_endings/soft/16.flac"
            show princess c wistful talk onlayer back
            with dissolve
            p "You know, you've never told me {i}your{/i} name.\n"
            show princess c wistful onlayer back
            menu:
                extend ""

                "{i}• ''I'm fine with 'The Long Quiet.'''{/i}":
                    voice "audio/_pristine/voice/_climax/cabin_endings/soft/17.flac"
                    show princess c shrug talk upbeat onlayer back
                    with dissolve
                    p "'Quiet' it is!\n"

                "{i}• ''I don't think I have one either.''{/i}":
                    voice "audio/_pristine/voice/_climax/cabin_endings/soft/18.flac"
                    show princess c shrug talk upbeat onlayer back
                    with dissolve
                    p "Then I guess I'll call you 'Quiet.'\n"

                "{i}• [[Shrug.]{/i}":
                    voice "audio/_pristine/voice/_climax/cabin_endings/soft/18.flac"
                    show princess c shrug talk upbeat onlayer back
                    with dissolve
                    p "Then I guess I'll call you 'Quiet.'\n"

                #"{i}• ''Oh. It's Gary.''{/i}":
                #    voice "audio/_pristine/voice/_climax/cabin_endings/soft/_af.flac"
                #    p "What? What month is it? What day?\n"
                #    voice "audio/_pristine/voice/_climax/cabin_endings/soft/19.flac"
                #    p "No. I'm not calling you that.\n"
                #    voice "audio/_pristine/voice/_climax/cabin_endings/soft/20.flac"
                #    p "How about... 'Quiet'?\n"

            voice "audio/_pristine/voice/_climax/cabin_endings/leave/hero/2.flac"
            show princess c wistful onlayer back
            with dissolve
            hero "Not 'hero?' Oh well, 'Quiet' will do. That's always been us, hasn't it?\n"
            jump felina_cabin_gentle_menu_empty

        "{i}• (Explore) ''None of this was ever really fair for either of us, was it?''{/i}" if felina_leave_fair == False:
            $ felina_leave_fair = True
            $ felina_leave_count += 1
            voice "audio/_pristine/voice/_climax/cabin_endings/soft/21.flac"
            show princess c gentle ask onlayer back
            with dissolve
            p "I don't know. We made it to the other side. And we found each other. I think that means all of the bad was worth it.\n"
            show princess c soft neutral onlayer back
            with dissolve
            jump felina_cabin_gentle_menu_empty

        "{i}• (Explore) ''I only wanted to slay the you out there. It's easier to want to kill an abstract concept than it is a person.''{/i}" if felina_stated_goal == "slay" and felina_loop_gentle_slay_comment == False:
            $ felina_loop_gentle_slay_comment = True
            $ felina_leave_count += 1
            voice "audio/voices/felina/cabin/soft/princess/9.flac"
            show princess c soft neutral talk onlayer back
            with dissolve
            p "For what it's worth, I'm glad you don't want to kill me anymore. But what do we do now?\n"
            show princess c soft neutral onlayer back
            with dissolve
            jump felina_cabin_gentle_menu_empty

        "{i}• (Explore) ''I don't think I ever really wanted to slay you. But I don't like what your existence means for the world.''{/i}" if felina_stated_goal == "slay" and felina_loop_gentle_slay_comment == False:
            $ felina_loop_gentle_slay_comment = True
            voice "audio/voices/felina/cabin/soft/princess/10.flac"
            show princess c wide eyed talk onlayer back
            with dissolve
            p "You were the one who decided to come down here without a weapon. What do we do now?\n"
            show princess c wide eyed onlayer back
            with dissolve
            jump felina_cabin_gentle_menu_empty

        "{i}• (Explore) ''What do you think of Her? What She wanted us to be.''{/i}" if felina_leave_mound_thoughts == False:
            $ felina_leave_count += 1
            $ felina_leave_mound_thoughts = True
            voice "audio/_pristine/voice/_climax/cabin_endings/soft/23.flac"
            show princess c sad dart talk onlayer back
            with dissolve
            p "I don't know. I don't think it's fair to judge her. It must be so lonely, thinking that she's everything that matters in the world, thinking that she's the only one with all the answers.\n"
            voice "audio/_pristine/voice/_climax/cabin_endings/leave/hero/6a.flac"
            show princess c sad dart onlayer back
            with dissolve
            hero "I never thought about it like that. That does sound lonely, doesn't it?\n"
            jump felina_cabin_gentle_menu_empty

        "{i}• ''What if we just leave?''{/i}" if felina_leave_count < 9:
            show princess c wide eyed onlayer back
            with dissolve
            jump felina_gentle_leave_join_menu

        "{i}• ''I think the only thing left for us to do is leave.''{/i}" if felina_leave_count >= 9:
            show princess c wide eyed onlayer back
            with dissolve
            label felina_gentle_leave_join_menu:
                #voice "audio/voices/felina/cabin/soft/princess/11.flac"
                #p "Can we actually do that? What would that even mean?\n"
                voice "audio/voices/felina/cabin/soft/princess/11a.flac"
                show princess c wide eyed talk onlayer back
                with dissolve
                p "Can we actually do that? What would that even mean? Where would we go?\n"
                label felina_gentle_hand_menu:
                    menu:
                        extend ""

                        "{i}• (Explore) [[Take her hand in yours.]{/i}" if felina_cabin_leave_hand_hold == False:
                            $ felina_cabin_leave_hand_hold = True
                            play music "audio/_music/mound/The Unknown Together Live Intro.flac"
                            queue music "audio/_music/mound/The Unknown Together Live Loop.flac" loop
                            show princess c soft hold hand onlayer back
                            with dissolve
                            jump felina_gentle_hand_menu

                        "{i}• ''I've always wanted to leave with you, but I didn't like being a god. I want to walk through that cabin door as we are. Just you and me.''{/i}":
                            if felina_cabin_leave_hand_hold:
                                show princess c soft hold hand blush onlayer back
                                with Dissolve(0.4)
                                $ renpy.pause(1.0)
                            else:
                                show princess c embarrassed onlayer back
                                with dissolve
                            voice "audio/voices/felina/cabin/soft/princess/12a.flac"
                            if felina_cabin_leave_hand_hold:
                                show princess c soft hold hand talk onlayer back
                                with Dissolve(0.4)
                            else:
                                show princess c sad smile talk onlayer back
                                with dissolve
                            p "I want that, too.\n"

                        "{i}• ''Not knowing what it means is why I want it. We knew everything out there, but we don't know this. I want to know something new.''{/i}":
                            if felina_cabin_leave_hand_hold:
                                show princess c soft hold hand blush onlayer back
                                with Dissolve(0.4)
                                $ renpy.pause(1.0)
                            else:
                                show princess c embarrassed onlayer back
                                with dissolve
                            voice "audio/voices/felina/cabin/soft/princess/13.flac"
                            if felina_cabin_leave_hand_hold:
                                show princess c soft hold hand talk onlayer back
                                with dissolve
                            else:
                                show princess c sad smile talk onlayer back
                                with dissolve
                            p "That's terrifying but... yeah. I think want that, too.\n"

                        "{i}• ''It doesn't matter what it means. What matters is that we're leaving together. That's all I want.''{/i}":
                            if felina_cabin_leave_hand_hold:
                                show princess c soft hold hand blush onlayer back
                                with Dissolve(0.4)
                                $ renpy.pause(1.0)
                            else:
                                show princess c embarrassed onlayer back
                                with dissolve
                            voice "audio/voices/felina/cabin/soft/princess/12a.flac"
                            if felina_cabin_leave_hand_hold:
                                show princess c soft hold hand talk onlayer back
                                with dissolve
                            else:
                                show princess c sad smile talk onlayer back
                                with dissolve
                            p "I want that, too.\n"

                        "{i}• ''I don't know where we'd go, but as long as it's not here, and as long as I'm with you, that's all I want.''{/i}":
                            if felina_cabin_leave_hand_hold:
                                show princess c soft hold hand blush onlayer back
                                with Dissolve(0.4)
                                $ renpy.pause(1.0)
                            else:
                                show princess c embarrassed onlayer back
                                with dissolve
                            voice "audio/voices/felina/cabin/soft/princess/12a.flac"
                            if felina_cabin_leave_hand_hold:
                                show princess c soft hold hand talk onlayer back
                                with dissolve
                            else:
                                show princess c sad smile talk onlayer back
                                with dissolve
                            p "I want that, too.\n"

                        "{i}• [[There's no need for words. Leave with her.]{/i}" if felina_cabin_leave_hand_hold:
                            voice "audio/voices/felina/cabin/soft/princess/14a.flac"
                            show princess c soft hold hand blush talk onlayer back
                            with dissolve
                            p "Okay. Let's do it.\n"
                            show princess c soft hold hand blush onlayer back
                            with dissolve
                            jump felina_leave_cabin_ending

                if felina_cabin_leave_hand_hold == False:
                    play music "audio/_music/mound/The Unknown Together Live Intro.flac"
                    queue music "audio/_music/mound/The Unknown Together Live Loop.flac" loop
                    show princess c sad smile onlayer back
                    with dissolve
                else:
                    show princess c soft hold hand blush onlayer back
                    with dissolve
                jump felina_leave_cabin_ending

label felina_cabin_gentle_menu_blade:
    menu:
        extend ""

        "{i}• (Explore) ''I don't want to be a god.''{/i}" if felina_cabin_god_comment == False:
            $ felina_cabin_god_comment = True
            voice "audio/voices/felina/cabin/soft/princess/15.flac"
            show princess c sad smile talk onlayer back
            with dissolve
            p "I don't think I want that, either.\n"
            show princess c sad smile onlayer back
            with dissolve
            jump felina_cabin_gentle_menu_blade

        "{i}• (Explore) ''Are you... the same as you are out there?''{/i}" if felina_cabin_same_comment == False:
            $ felina_cabin_same_comment = True
            voice "audio/voices/felina/cabin/soft/princess/16.flac"
            show princess c gentle ask onlayer back
            with dissolve
            p "I don't feel the same. I feel smaller.\n"
            show princess c soft neutral onlayer back
            with dissolve
            jump felina_cabin_gentle_menu_blade

        "{i}• (Explore) ''I only wanted to slay the you out there. It's easier to want to kill an abstract concept than it is a person.''{/i}" if felina_stated_goal == "slay":
            $ felina_loop_gentle_slay_comment = True
            jump felina_loop_gentle

        "{i}• (Explore) ''I don't want to hurt anyone. There has to be a way out of this.''{/i}":
            $ felina_loop_gentle_way_out_comment = True
            jump felina_loop_gentle

        "{i}• (Explore) ''I don't think I ever really wanted to slay you. But I don't like what your existence means for the world.''{/i}" if felina_stated_goal == "slay":
            $ felina_loop_gentle_slay_comment = True
            jump felina_loop_gentle

        "{i}• (Explore) ''What are we going to do?''{/i}":
            jump felina_loop_gentle

        "{i}• (Explore) ''I don't want to have to slay you, but I don't know what other options there are.''{/i}":
            $ felina_loop_gentle_slay_comment = True
            jump felina_loop_gentle

        "{i}• ''I'm sorry.'' [[Slay the Princess.]{/i}":
            $ felina_slain_apologize = True
            voice "audio/voices/felina/cabin/slay/princess/5.flac"
            show princess c regret talk onlayer back
            with dissolve
            p "I'm sorry, too.\n"
            jump felina_slain_start

        "{i}• [[Slay the Princess.]{/i}":
            voice "audio/voices/felina/cabin/soft/hero/1.flac"
            hero "So this is really it, then. Let's see this through.\n"
            jump felina_slain_start

label felina_loop_gentle:
    play music "audio/_music/mound/Loop Ending.flac" loop
    default felina_loop_gentle_slay_comment = False
    default felina_loop_gentle_way_out_comment = False
    if felina_loop_gentle_way_out_comment:
        voice "audio/voices/felina/cabin/soft/princess/17.flac"
        show princess c gentle ask onlayer back
        with dissolve
        p "I don't think there's a way out, but maybe there doesn't have to be an ending.\n"
    elif felina_loop_gentle_slay_comment:
        voice "audio/voices/felina/cabin/soft/princess/18.flac"
        show princess c gentle ask onlayer back
        with dissolve
        p "Then maybe you don't have to kill me. Maybe there never even has to be an ending.\n"
    else:
        voice "audio/voices/felina/cabin/soft/princess/19.flac"
        show princess c gentle ask onlayer back
        with dissolve
        p "Maybe this doesn't have to end just yet. Maybe there never even has to be an ending.\n"
    voice "audio/voices/felina/cabin/soft/princess/20.flac"
    show princess c sad smile talk onlayer back
    with dissolve
    p "I'm able to do the things you believe me to be able to do.\n"
    if mirror_construct:
        voice "audio/voices/felina/cabin/soft/princess/21.flac"
        show princess c soft neutral talk onlayer back
        with dissolve
        p "So make me put it all back. Help me fix the Echo's construct and make us both forget.\n"
        #edited same as hostile menu
    else:
        voice "audio/voices/felina/cabin/soft/princess/22.flac"
        show princess c soft neutral talk onlayer back
        with dissolve
        p "So make me put it all back. Help me fix this place and make us both forget.\n"
        #same as prev
    voice "audio/voices/felina/cabin/soft/princess/23.flac"
    show princess c regret talk onlayer back
    with dissolve
    p "Help me send us back to the beginning, before we woke up. Before either of us saw the truth.\n"
    voice "audio/voices/felina/cabin/soft/hero/2.flac"
    show princess c regret onlayer back
    with dissolve
    hero "Can she really do that? Are you sure that's what you want?\n"
    label loop_ending_gentle_menu:
        menu:
            extend ""

            "{i}• (Explore) ''Would resetting it do anything to help {b}them{/b}? The people out there? If you continue to exist, then don't they continue to die and suffer?''{/i}" if loop_reset_help == False:
                $ loop_reset_help = True
                voice "audio/voices/felina/cabin/soft/princess/24.flac"
                show princess c gentle ask onlayer back
                with dissolve
                p "If you can believe this helps them, then it will help them, right?\n"
                show princess c soft neutral onlayer back
                with dissolve
                jump loop_ending_gentle_menu

            "{i}• (Explore) ''I don't want to forget you.''{/i}" if loop_forget == False:
                $ loop_forget = True
                voice "audio/voices/felina/cabin/soft/princess/25.flac"
                show princess c empathy talk onlayer back
                with dissolve
                p "I don't want to forget you either. But unless we do this, you'll have to choose, right now, between me and everyone else.\n"
                show princess c empathy onlayer back
                with dissolve
                jump loop_ending_gentle_menu

            "{i}• (Explore) ''We're going to find ourselves back here eventually.''{/i}" if loop_return == False:
                $ loop_return = True
                voice "audio/voices/felina/cabin/soft/princess/26.flac"
                show princess c sad smile talk onlayer back
                with dissolve
                p "And when we do, we'll make the same choice. We'll choose to forget and we'll reset everything again.\n"
                show princess c sad smile onlayer back
                with dissolve
                jump loop_ending_gentle_menu

            "{i}• (Explore) ''If we're talking about this right now, how do we know we haven't done this before?''{/i}" if loop_repeat == False:
                $ loop_repeat = True
                voice "audio/voices/felina/cabin/soft/princess/27a.flac"
                show princess c wistful talk onlayer back
                with dissolve
                p "Maybe we have done all of this before. Maybe we're supposed to do this forever.\n"
                show princess c wistful onlayer back
                with dissolve
                #p "There's no way for us to ever know, is there? Maybe we have done all of this before. Maybe we're supposed to do this forever.\n"
                jump loop_ending_gentle_menu

            "{i}• (Explore) ''How do you know that things won't end worse? What if when I make my way back here I'm different and I hurt you? What if I kill you? What if I let you bring about the end of everything?''{/i}" if loop_worse == False and loop_repeat:
                $ loop_worse = True
                voice "audio/voices/felina/cabin/soft/princess/28.flac"
                show princess c gentle ask onlayer back
                with dissolve
                p "None of that will happen. Because you'll still be you, and I'll still be me.\n"
                show princess c sad smile onlayer back
                with dissolve
                jump loop_ending_gentle_menu

            "{i}• (Explore) ''But how do you know that? We'd have to decide to do this every single time. Forever. Eventually something is going to be different.''{/i}" if loop_worse and loop_worse_follow == False:
                $ loop_worse_follow = True
                voice "audio/voices/felina/cabin/soft/princess/29.flac"
                show princess c gentle ask onlayer back
                with dissolve
                p "I know because it doesn't matter how many times we've hurt each other. I've never stopped caring about you.\n"
                voice "audio/voices/felina/cabin/soft/princess/30.flac"
                show princess c sad smile talk onlayer back
                with dissolve
                p "And if you feel the same, then everything is going to be okay.\n"
                show princess c sad smile onlayer back
                with dissolve
                jump loop_ending_gentle_menu

            "{i}• (Explore) ''This isn't fair. I want to be here with you. I don't want to be alone again.''{/i}" if loop_fair == False:
                $ loop_fair = True
                voice "audio/voices/felina/cabin/soft/princess/31.flac"
                show princess c gentle ask onlayer back
                with dissolve
                p "But you won't be alone for long. I'll be right here waiting for you.\n"
                show princess c wistful onlayer back
                with dissolve
                jump loop_ending_gentle_menu

            "{i}• (Explore) ''Is there any other way?''{/i}" if loop_other_way == False:
                $ loop_other_way = True
                voice "audio/voices/felina/cabin/soft/princess/32.flac"
                show princess c sad smile talk onlayer back
                with dissolve
                p "I think you brought that knife down here for a reason. It has to be a part of how this ends.\n"
                show princess c sad smile onlayer back
                with dissolve
                jump loop_ending_gentle_menu

            "{i}• (Explore) ''I take it all back. I don't want this, and I don't want to kill you. Is it too late to go back to being a god?''{/i}" if loop_regret == False:
                $ loop_regret = True
                voice "audio/voices/felina/cabin/soft/princess/33.flac"
                show princess c wistful talk onlayer back
                with dissolve
                p "It feels like it is. You wouldn't have come here if you were just going to go back.\n"
                show princess c wistful onlayer back
                jump loop_ending_gentle_menu

            "{i}• ''Okay. Then let's do it. I believe in us.'' [[Agree to her plan.]{/i}":
                show princess c wistful onlayer back
                with dissolve
                voice "audio/voices/felina/cabin/soft/hero/3.flac"
                hero "Okay. If this is your choice, then we're doing it. I guess I'll see you on the other side.\n"
                show princess c soft take blade onlayer back
                with Dissolve(1.0)
                voice "audio/voices/felina/cabin/soft/hero/4a.flac"
                $ blade_held = False
                $ default_mouse = "default"
                play audio "audio/one_shot/knife_pickup.flac"
                show princess c soft final line onlayer back
                with Dissolve(1.0)
                hero "She takes the blade from our hand. She raises her gentle eyes to ours... a fondness in her gaze.\n"
                menu:

                    extend ""

                    "{i}• ''I love you.''{/i}":
                        show princess c soft final line cry onlayer back
                        with dissolve
                        voice "audio/voices/felina/cabin/soft/princess/34.flac"
                        show princess c soft final line cry talk onlayer back
                        with dissolve
                        p "Everything is going to be okay. I love you, too.\n"
                        # she strikes. game goes back to the Real chapter 1

                    "{i}• ''Just do it.''{/i}":
                        show princess c soft final line cry onlayer back
                        with dissolve
                        voice "audio/voices/felina/cabin/soft/princess/35.flac"
                        show princess c soft final line cry talk onlayer back
                        with dissolve
                        p "Everything is going to be okay. I love you.\n"
                        # she strikes. game goes back to the Real chapter 1

                    "{i}• ''I'll see you soon.''{/i}":
                        show princess c soft final line cry onlayer back
                        with dissolve
                        voice "audio/voices/felina/cabin/soft/princess/35.flac"
                        show princess c soft final line cry talk onlayer back
                        with dissolve
                        p "Everything is going to be okay. I love you.\n"
                        # she strikes. game goes back to the Real chapter 1

                    "{i}• [[Remain silent.]{/i}":
                        voice "audio/voices/felina/cabin/soft/hero/5.flac"
                        show princess c soft final line cry onlayer back
                        with dissolve
                        hero "Yeah. It's better if we don't say anything.\n"
                        voice "audio/voices/felina/cabin/soft/princess/35.flac"
                        show princess c soft final line cry talk onlayer back
                        with dissolve
                        p "Everything is going to be okay. I love you.\n"
                        # she strikes. game goes back to the Real chapter 1

                $ gallery_zfinale.unlock_item(7)
                $ renpy.save_persistent()
                show princess c soft finale onlayer back
                with dissolve
                $ renpy.pause(0.25)
                stop music
                stop sound
                hide princess onlayer back
                hide bg onlayer farback
                play audio "audio/final/Tower_KnifeBlow_3.flac"
                scene bg black
                $ renpy.pause(2.0)
                jump loop_ending

            "{i}• ''I'm sorry, but I can't do that.'' [[Slay the Princess.]{/i}":
                stop music fadeout 1.0
                $ felina_slain_apologize = True
                voice "audio/voices/felina/cabin/slay/princess/5.flac"
                show princess c regret talk onlayer back
                with dissolve
                p "I'm sorry, too.\n"
                jump felina_slain_start

            "{i}• [[Slay the Princess.]{/i}":
                stop music fadeout 1.0
                voice "audio/voices/felina/cabin/soft/hero/6.flac"
                hero "So this is really it, then.\n"
                #added comma and removed last clause
                jump felina_slain_start

return
