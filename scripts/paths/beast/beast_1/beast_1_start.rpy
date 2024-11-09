label beast_1_start:
    $ blade_held = False
    $ trait_hunted = True
    $ quick_menu = False
    $ current_princess = "beast"
    play sound "audio/looping/uncomfortable ambiance.ogg" loop fadein 1.0
    scene chapter beast with fade
    show text _("{color=#FFFFFF00}Chapter Two. The Beast.{/color}") at Position(ypos=850)
    $ renpy.pause(4.0)

    play sound "audio/looping/uncomfortable ambiance.ogg" loop
    play secondary "audio/looping/uncomfortable ambiance heightened.ogg" loop
    play music "audio/_music/ch1/Fragmentation.flac" loop
    scene bg path onlayer farback at flip, Position(ypos=1125)
    show midground path onlayer back at flip, Position(ypos=1125)
    show front path onlayer front at flip, Position(ypos=1125)
    show bg black
    hide text
    #show loading_icon
    hide chapter
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    $ gallery_beast.unlock_gallery()
    $ gallery_zch1.unlock_item(12)
    $ renpy.save_persistent()
    voice "audio/voices/ch1/woods/narrator/script_n_1.flac"
    n "You're on a path in the woods. And at the end of that path is a cabin. And in the basement of that cabin is a Princess.\n"
    voice "audio/voices/ch1/woods/narrator/script_n_2.flac"
    n "You're here to slay her.\n If you don't, it will be the end of the world.\n"
    label beast_1_forest:
        default beast_1_forest_count = 0
        default beast_1_forest_share_died = False
        default beast_1_forest_share_loop = False
        default beast_1_forest_princess_press = False
        default beast_1_forest_share_loop_insist = False
        default beast_1_forest_deja_vu = False
        default beast_1_forest_deja_vu_follow_up = False
        menu:
            extend ""

            "{i}• (Explore) I'm getting a terrible sense of deja vu.{/i}" if beast_1_forest_share_loop == False:
                $ beast_1_forest_deja_vu = True
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_1a.flac"
                n "A terrible sense of deja vu? No, you don't have that. This is the first time either of us have been here.\n"
                label beast_1_forest_narrator_share_join:
                    $ beast_1_forest_count += 1
                    $ beast_1_forest_share_loop = True
                    voice "audio/voices/ch2/shared/hero/ch2_share_h_1.flac"
                    hero "If He doesn't remember what happened, then maybe it's best to keep it that way.\n"
                    voice "audio/voices/ch2/beast/hunted/ch2_hunt_1.flac"
                    hunted "If He doesn't remember what happened, then something else must have trapped us here.\n"
                    voice "audio/voices/ch2/beast/narrator/ch2_bn_1.flac"
                    n "You're not {i}trapped{/i} here. Nobody's forcing you to do anything, though the only sensible thing for you to do right now is march up to that cabin and slay the Princess.\n"
                    jump beast_1_forest

            "{i}• (Explore) This is more than just deja vu, though. I'm pretty sure this whole thing literally just happened.{/i}" if beast_1_forest_deja_vu and beast_1_forest_deja_vu_follow_up == False:
                $ beast_1_forest_deja_vu_follow_up = True
                $ beast_1_forest_count += 1
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_2.flac"
                n "We could go back and forth on this forever, and it won't get you any closer to doing your job and saving the world. So let's just agree to disagree.\n"
                jump beast_1_forest

            "{i}• (Explore) Wait... hasn't this already happened?{/i}" if beast_1_forest_share_loop == False:
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_1b.flac"
                n "It hasn't. Or if it has, I certainly haven't been a part of it. We've just met for the first time, you and I.\n"
                jump beast_1_forest_narrator_share_join

            "{i}• (Explore) Okay, no.{/i}" if beast_1_forest_share_loop == False:
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_3a.flac"
                n "Oh, don't you start grandstanding about morals. The fate of the world is at risk right now, and the life of a mere Princess shouldn't stop you from saving us all.\n"
                jump beast_1_forest_narrator_share_join

            "{i}• (Explore) But I died! What am I doing here?{/i}" if beast_1_forest_share_loop == False:
                $ beast_1_forest_share_died = True
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_4.flac"
                n "I can assure you that you're not dead. And to answer your second question, you're here to slay the Princess. I literally told you that a second ago.\n"
                jump beast_1_forest_narrator_share_join

            "{i}• (Explore) She's going to kill me again!{/i}" if beast_1_forest_share_loop == False:
                $ beast_1_forest_share_died = True
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_5.flac"
                n "Again? People don't die twice. You haven't even met the Princess, and I hardly think she'd be capable of killing someone as skilled and courageous as yourself.\n"
                jump beast_1_forest_narrator_share_join

            "{i}• (Explore) Let's assume I'm telling the truth, and all of this really did already happen. Why should I listen to you? Why should I bother doing {i}anything{/i}?{/i}" if beast_1_forest_share_loop and (beast_1_forest_deja_vu == False or (beast_1_forest_deja_vu_follow_up)) and beast_1_forest_share_loop_insist == False:
                $ beast_1_forest_share_loop_insist = True
                $ beast_1_forest_count += 1
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_6.flac"
                n "Those are two very different questions, but fine. I'll indulge you if that's what it takes to get you moving.\n"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_7.flac"
                n "Let's say for a moment that this really is the second time you've met me, or, at least, a version of me.\n"
                if beast_1_forest_share_died == False:
                    voice "audio/voices/ch2/shared/narrator/ch2_share_n_8.flac"
                    n "If you're back here, I'm assuming you died, which probably only happened because you didn't listen to me.\n"
                else:
                    voice "audio/voices/ch2/shared/narrator/ch2_share_n_9.flac"
                    n "You died last time, which probably only happened because you didn't listen to me.\n"
                voice "audio/voices/ch2/beast/hero/ch2_bh_1.flac"
                hero "We did our best with the information we were given.\n"
                #voice "audio/voices/ch2/shared/narrator/ch2_share_n_10.flac"
                voice "audio/voices/ch2/beast/narrator/ch2_bn_3a.flac"
                n "And yet you still died, didn't you? So, great. Congratulations. You've been given another chance to actually do this right.\n"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_11.flac"
                n "And I believe your other question was something along the lines of 'what's the point of doing anything?' If you're asking that, it sounds to me like you're making the rather dangerous assumption that your actions last time around didn't have any consequences.\n"
                voice "audio/voices/ch2/beast/hero/ch2_bh_2.flac"
                hero "What do you mean? Of course there weren't any consequences. We were killed by the Princess, and now everyone's right back where they started. That sounds pretty consequence-free to me.\n"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_12.flac"
                n "Yes, but, in this purely hypothetical scenario, that begs the question of {i}how{/i} you got back here. Did 'time' simply rewind itself, or were you instead transported to a different world entirely?\n"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_13.flac"
                n "If it's the latter, what do you think happened {i}after{/i} you died?\n"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_13a.flac"
                n "Do you think the people there lived happily ever after, or do you think that the Princess, left unhindered, brought about the end to everyone and everything, just like I told you she would?\n"
                voice "audio/voices/ch2/beast/hunted/ch2_hunt_2.flac"
                hunted "All the more reason to keep our wits about us. Should we even return to the cabin? We could find a safe little hole somewhere instead...\n"
                voice "audio/voices/ch2/beast/narrator/ch2_bn_4.flac"
                n "You have to go to the cabin. If you don't slay the Princess she's going to end the world, which you're always going to be a part of, even if you're cowering in a hole. There's no escaping your responsibility here.\n"
                jump beast_1_forest

            "{i}• (Explore) Let's talk about this Princess...{/i}" if beast_1_forest_share_loop_insist and beast_1_forest_princess_press == False:
                $ beast_1_forest_count += 1
                $ beast_1_forest_princess_press = True
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_14.flac"
                n "Just be quick about it.\n"
                label beast_1_forest_princess:
                    default beast_1_forest_princess_count = 0
                    default beast_1_forest_princess_why_strong = False
                    default beast_1_forest_princess_basement_explain = False
                    default beast_1_forest_princess_why_me = False
                    default beast_1_forest_princess_cagey = False
                    default beast_1_forest_princess_tips = False
                    menu:
                        extend ""

                        "{i}• (Explore) She killed me last time around. How can I make sure that doesn't happen again?{/i}" if beast_1_forest_princess_tips == False:
                            $ beast_1_forest_princess_tips = True
                            $ beast_1_forest_princess_count += 1
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_15.flac"
                            n "Like I said, if she killed you, it was probably because you didn't listen to me. Don't talk to her. Don't trust her. Just go in, do your job, and save the world.\n"
                            jump beast_1_forest_princess

                        "{i}• (Explore) She killed me by ripping me to pieces. Don't get me wrong, I hated it, but how can someone like that end the world?{/i}" if beast_1_forest_princess_why_strong == False:
                            $ beast_1_forest_princess_why_strong = True
                            $ beast_1_forest_princess_count += 1
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_16a.flac"
                            n "She just can. Believe me, I wish I could tell you more, but you'll just have to trust that what I'm saying is true and that, despite it all, you're fully up to the task that's been given to you.\n"
                            jump beast_1_forest_princess

                        "{i}• (Explore) To quote you from last time around, 'she's {i}just{/i} a Princess.' Why was she able to rip me apart with her bare hands?{/i}" if beast_1_forest_princess_why_strong == False:
                            $ beast_1_forest_princess_why_strong = True
                            $ beast_1_forest_princess_count += 1
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_17.flac"
                            n "She {i}is{/i} just a Princess. Whatever you think happened to you last time, just get it out of your head before you get to the cabin, and you'll be {i}fine{/i}.\n"
                            jump beast_1_forest_princess

                        "{i}• (Explore) Who locked her in that basement? What {b}is{/b} this place?{/i}" if beast_1_forest_princess_basement_explain == False:
                            $ beast_1_forest_princess_basement_explain = True
                            $ beast_1_forest_princess_count += 1
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_18.flac"
                            n "{i}People{/i} locked her in that basement. And I told you what this place is. It's a path in the woods. Don't overcomplicate things.\n"
                            jump beast_1_forest_princess

                        "{i}• (Explore) If people locked her away, why couldn't {b}they{/b} slay her? Why is this falling on me?{/i}" if beast_1_forest_princess_basement_explain and beast_1_forest_princess_why_me == False:
                            $ beast_1_forest_princess_why_me = True
                            $ beast_1_forest_princess_count += 1
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_19.flac"
                            n "Look, I'm not supposed to say this but it's because you're special. You're the {i}only{/i} person capable of doing this. Call it a prophecy if that helps, but it's just the way things are.\n"
                            voice "audio/voices/ch2/shared/hero/ch2_share_h_2.flac"
                            hero "Oh. I didn't know we were {i}special{/i}.\n"
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_20a.flac"
                            n "Of course you're special. Why else would you be here?\n"
                            voice "audio/voices/ch2/beast/hunted/ch2_hunt_3.flac"
                            hunted "Special can mean all sorts of things. Don't let it make you careless. We need clear thoughts and pricked ears.\n"
                            jump beast_1_forest_princess

                        "{i}• (Explore) You're being cagey. What aren't you telling me?{/i}" if beast_1_forest_princess_cagey == False and beast_1_forest_princess_count > 1:
                            $ beast_1_forest_princess_cagey = True
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_21.flac"
                            n "I've told you everything you need to know, going into more detail would just overcomplicate an otherwise very simple situation and make your job more difficult.\n"
                            voice "audio/voices/ch2/shared/hero/ch2_share_h_3.flac"
                            hero "If you want us to stand a chance against her, we need to be armed with information. What is she really capable of? How are we supposed to stop her?\n"
                            if beast_1_forest_princess_count < 2:
                                voice "audio/voices/ch2/shared/narrator/ch2_share_n_22.flac"
                                n "The less you know about her, the better.\n"
                            else:
                                voice "audio/voices/ch2/shared/narrator/ch2_share_n_23.flac"
                                n "Not to sound like a broken record, but the less you know about her, the better things will go for all of us. I know it sounds like I'm hiding something, but you're just going to have to take me at my word.\n"
                            voice "audio/voices/ch2/beast/hunted/ch2_hunt_4.flac"
                            hunted "You're afraid, aren't you? Just like us.\n"
                            voice "audio/voices/ch2/beast/narrator/ch2_bn_5.flac"
                            n "Of course I'm afraid. Fear is an extremely normal thing to feel when the fate of the entire world is at stake.\n"
                            voice "audio/voices/ch2/beast/hunted/ch2_hunt_5.flac"
                            hunted "But that's not the only thing you're afraid of. You're scared of something {i}worse{/i}.\n"
                            voice "audio/voices/ch2/beast/narrator/ch2_bn_6.flac"
                            n "Stop projecting your neuroses onto me and just get to the cabin already.\n"
                            jump beast_1_forest_princess

                        "{i}• Nevermind.{/i}" if beast_1_forest_princess_count == 0:
                            label beast_1_forest_princess_leaving:
                                voice "audio/voices/ch2/shared/narrator/ch2_share_n_24.flac"
                                n "Great. Now if you don't mind, the whole world is waiting with bated breath for you to save it from ruin.\n"
                                jump beast_1_forest

                        "{i}• That's all.{/i}" if beast_1_forest_princess_count != 0:
                            jump beast_1_forest_princess_leaving

            "{i}• [[Proceed to the cabin.]{/i}":
                jump beast_1_cabin_arrival

            "{i}• [[Turn around and leave.]{/i}" if mound_can_attempt_flee:
                if loops_finished >= 2:
                    $ mound_can_attempt_flee = False
                    voice "audio/voices/mound/bonus/flee.flac"
                    mound "You have already committed to my completion. You cannot go further astray.\n"
                    jump beast_1_forest
                voice "audio/voices/ch2/beast/hunted/ch2_hunt_6.flac"
                hunted "Yes. We're safer taking flight.\n"
                jump turn_and_leave_join

label beast_1_cabin_arrival:
    play audio "audio/one_shot/footsteps_hike_short.flac"
    $ quick_menu = False
    hide bg path onlayer farback
    hide midground path onlayer back
    hide front path onlayer front
    show bg black
    with fade
    scene skyline cabin onlayer farback at Position(ypos = 1080)
    show bg cabin onlayer back at Position(ypos = 1200)
    show midground cabin onlayer front at Position(ypos = 1140)
    show foreground cabin onlayer inyourface at Position(ypos = 1120)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    voice "audio/voices/ch1/woods/narrator/script_n_38.flac"
    n "A warning, before you go any further...\n"
    voice "audio/voices/ch1/woods/narrator/script_n_62.flac"
    n "She will lie, she will cheat, and she will do everything in her power to stop you from slaying her. Don't believe a word she says.\n"
    voice "audio/voices/ch2/beast/hunted/ch2_hunt_7.flac"
    hunted "Does a cat lie to a cornered mouse when it plays with its freedom, or is it just acting out its nature?\n"
    voice "audio/voices/ch2/beast/hero/ch2_bh_3.flac"
    hero "I don't see why that matters. A lie is a lie, and if anything, she's the one who's cornered.\n"
    voice "audio/voices/ch2/beast/hunted/ch2_hunt_8.flac"
    hunted "She could have gotten out of there whenever she wanted to. We should trust nothing that she tells us, only what we hear and smell.\n"
    voice "audio/voices/ch2/beast/narrator/ch2_bn_7.flac"
    n "That's a very roundabout way of saying that you should listen to me and take this seriously.\n"
    voice "audio/voices/ch2/beast/hunted/ch2_hunt_9.flac"
    hunted "Maybe.\n"
    menu:
        extend ""

        "{i}• [[Proceed into the cabin.]{/i}":
            label beast_stranger_rejoin:
                $ quick_menu = False
                play audio "audio/one_shot/enter_cabin_audio.flac"
                hide skyline onlayer farback
                hide bg onlayer back
                hide midground onlayer front
                hide walls onlayer back
                hide foreground onlayer inyourface
                show cutscene cabin
                with dissolve
                $ renpy.pause(4.0)
                stop sound fadeout 1.0
                stop music fadeout 1.0
                scene bg black
                #show loading_icon
                with fade

    $ gallery_beast.unlock_item(1)
    $ renpy.save_persistent()
    play sound "audio/looping/ambient_cabin.ogg" loop fadein 1.0
    play music "audio/_music/ch2/beast/The Beast.flac" loop
    scene farback beast cabin onlayer farback at Position(ypos=1125)
    show bg beast cabin onlayer back at Position(ypos=1125)
    show door beast1 onlayer back at Position(ypos=1125)
    #show table beast onlayer back at Position(ypos=1125)
    show knife beast onlayer back at Position(ypos=1125)
    show mirror base onlayer back at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    voice "audio/voices/ch2/beast/narrator/ch2_bn_8.flac"
    n "The interior of the cabin is ruinous and dilapidated. It feels like no one has lived here for a long time, wind rushing in through cracks and holes in the wooden walls. The only furniture of note is a termite-eaten table with a pristine blade perched on its edge.\n"
    voice "audio/voices/ch2/shared/narrator/ch2_share_n_25.flac"
    n "The blade is your implement. You'll need it if you want to do this right.\n"
    label cabin_interior_2_beast_menu:
        default beast_1_cabin_mirror_present = True
        default beast_1_cabin_blade_taken = False
        default beast_1_cabin_mirror_ask = False
        default beast_1_cabin_mirror_approached = False
        default beast_1_cabin_last_time_comment = False
        menu:
            extend ""

            "{i}• (Explore) You didn't say anything about the mirror on the wall.{/i}" if beast_1_cabin_mirror_ask == False and beast_1_cabin_mirror_present:
                $ beast_1_cabin_mirror_ask = True
                $ current_run_mirror_comment = True
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_26.flac"
                n "That's because there isn't a mirror. There's a table, the blade sitting on the table, and the door to the basement. There's nothing else in here.\n"
                voice "audio/voices/ch2/shared/hero/ch2_share_h_4.flac"
                hero "There's definitely a mirror.\n"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_27.flac"
                n "There isn't.\n"
                if beast_1_forest_share_loop:
                    voice "audio/voices/ch2/beast/hunted/ch2_hunt_10.flac"
                    hunted "What a strange thing to lie about. Maybe He doesn't see it, much like He hasn't seen what's already happened.\n"
                else:
                    voice "audio/voices/ch2/beast/hunted/ch2_hunt_10ab.flac"
                    hunted "What a strange thing to lie about. Maybe He doesn't see it.\n"
                menu:
                    extend ""

                    "{i}• Why {b}would{/b} you lie about that? What's the point?{/i}":
                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_28.flac"
                        n "Exactly. Why would I lie about something so meaningless? What good would a mirror even do? Let you waste time preening yourself instead of doing what needs to be done?\n"

                    "{i}• I want to look at myself. I want to see how {b}handsome{/b} I am.{/i}":
                        voice "audio/voices/ch2/damsel/hero/ch2_dh_9.flac"
                        hero "We shouldn't waste time {i}preening{/i}, but if He {i}is{/i} lying about the mirror, it might be important.\n"
                        voice "audio/voices/ch2/beast/hunted/ch2_hunt_11.flac"
                        hunted "Or it's dangerous.\n"
                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_29.flac"
                        n "I'm not lying to you. Use your eyes, there is no mirror. Why would I lie about something so meaningless? What good would it even do?\n"

                    "{i}• It doesn't matter.{/i}":
                        $ beast_1_cabin_mirror_present = False
                        voice "audio/voices/ch2/shared/hero/ch2_share_h_5.flac"
                        hero "But it {i}does{/i} matter! Don't you care if we're being lied to? If He's willing to lie about something as innocuous as a mirror, what else is He hiding from us?\n"
                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_30.flac"
                        hide mirror onlayer back
                        n "I'm not lying to you. Use your eyes, there is no mirror. Why would I lie about something so meaningless? What good would a mirror even do? Let you waste time preening yourself instead of doing what needs to be done?\n"
                        voice "audio/voices/ch2/shared/hero/ch2_share_h_6.flac"
                        hero "But there {i}was{/i} a mirror a second ago.\n"
                        voice "audio/voices/ch2/beast/hunted/ch2_hunt_12.flac"
                        hunted "And now it's gone.\n"

                    "{i}• [[Remain silent.]{/i}":
                        voice "audio/voices/ch2/shared/hero/ch2_share_h_7b.flac"
                        hero "I care about whether we're being lied to. If He's willing to lie about something as innocuous as a mirror, what else could He hiding from us?\n"
                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_31.flac"
                        n "I'm not lying to you, I {i}promise{/i}. There isn't a mirror. Really.\n"

                    "{i}• [[Approach the mirror.]{/i}" if beast_1_cabin_mirror_approached == False:
                        label beast_cabin_1_mirror_join:
                            play audio "audio/one_shot/footsteps_creaky.flac"
                            hide farback onlayer farback
                            hide bg onlayer back
                            hide door onlayer back
                            hide table onlayer back
                            hide knife onlayer back
                            hide mirror onlayer back
                            scene bg beast mirror onlayer front at Position(ypos=1125)
                            show mirror beast close onlayer front at Position(ypos=1125)
                            with dissolve
                            $ beast_1_cabin_mirror_approached = True
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_32.flac"
                            n "You walk up to the wall next to the basement door. It's a wall. There isn't much to see here.\n"
                            if beast_1_cabin_mirror_ask == False:
                                voice "audio/voices/ch2/shared/hero/ch2_share_h_8.flac"
                                hero "What are you talking about? This isn't a wall. It's a mirror. Or at least it'll {i}be{/i} a mirror once we wipe off that layer of grime.\n"
                            else:
                                voice "audio/voices/ch2/shared/hero/ch2_share_h_9.flac"
                                hero "This really isn't funny.\n"
                            $ current_run_mirror_touched = True
                            menu:
                                extend ""

                                "{i}• [[Wipe the mirror clean.]{/i}":
                                    $ beast_1_cabin_mirror_present = False
                                    hide mirror onlayer front
                                    play audio "audio/one_shot/new/STP_claws_1.flac"
                                    show player wall onlayer front at Position(ypos=1125) with dissolve
                                    if beast_1_cabin_mirror_ask == False:
                                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_33.flac"
                                    else:
                                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_33a.flac"
                                    n "You reach forward and rub your hand against the cabin wall. I hope you know how ridiculous you look right now.\n"
                                    hide player onlayer front with dissolve
                                    if beast_1_cabin_mirror_ask:
                                        voice "audio/voices/ch2/shared/hero/ch2_share_h_10.flac"
                                        hero "But it was there a second ago!\n"
                                    else:
                                        voice "audio/voices/ch2/shared/hero/ch2_share_h_6.flac"
                                        hero "But there was a mirror a second ago.\n"
                                    voice "audio/voices/ch2/beast/hunted/ch2_hunt_12.flac"
                                    hunted "And now it's gone.\n"
                                    play audio "audio/one_shot/footsteps_creaky.flac"
                                    hide bg onlayer front
                                    scene farback beast cabin onlayer farback at Position(ypos=1125)
                                    show bg beast cabin onlayer back at Position(ypos=1125)
                                    show door beast1 onlayer back at Position(ypos=1125)
                                    if beast_1_cabin_blade_taken == False:
                                        show knife beast onlayer back at Position(ypos=1125)
                                    with dissolve
                                    jump cabin_interior_2_beast_menu

                jump cabin_interior_2_beast_menu

            "{i}• (Explore) This whole cabin is different than last time.{/i}" if beast_1_cabin_last_time_comment == False and beast_1_forest_share_loop_insist:
                $ beast_1_cabin_last_time_comment = True
                voice "audio/voices/ch2/shared/hero/ch2_share_h_11.flac"
                hero "{i}Very{/i} different.\n"
                voice "audio/voices/ch2/beast/hunted/ch2_hunt_13.flac"
                hunted "I wonder why.\n"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_34.flac"
                n "Maybe that's because you haven't actually been here. I hope this means you'll finally drop that ridiculous past-life nonsense. You haven't died, and you certainly haven't been killed by the Princess.\n"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_35.flac"
                n "So focus up. A lot's riding on this.\n"
                jump cabin_interior_2_beast_menu

            "{i}• (Explore) [[Approach the mirror.]{/i}" if beast_1_cabin_mirror_present and beast_1_cabin_mirror_approached == False:
                $ beast_1_cabin_mirror_approached = True
                jump beast_cabin_1_mirror_join

            "{i}• (Explore) [[Take the blade.]{/i}" if beast_1_cabin_blade_taken == False:
                $ beast_1_cabin_blade_taken = True
                $ blade_held = True
                $ default_mouse = "blade"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_36.flac"
                play audio "audio/one_shot/knife_pickup.flac"
                hide knife onlayer back
                with dissolve
                n "You take the blade from the table. It would be difficult to slay the Princess and save the world without a weapon.\n"
                jump cabin_interior_2_beast_menu

            "{i}• [[Enter the basement.]{/i}":
                if beast_1_cabin_blade_taken == False:
                    voice "audio/voices/ch2/beast/hunted/ch2_hunt_14a.flac"
                    hunted "No steel claw. Do you think we can talk our way out of this? I don't think she wants to talk.\n"
                    voice "audio/voices/ch2/shared/hero/ch2_share_h_12.flac"
                    hero "I guess we'll just have to trust that we made the right call. It'll still be here if we need it.\n"

                $ quick_menu = False
                play audio "audio/one_shot/door_bedroom.flac"
                hide mirror onlayer back
                show door beast2 onlayer back at Position(ypos=1125) with Dissolve(0.5)
                show door beast3 onlayer back at Position(ypos=1125) with Dissolve(0.5)
                hide farback onlayer farback
                hide bg onlayer back
                hide door onlayer back
                hide table onlayer back
                hide knife onlayer back
                hide mirror onlayer back
                with fade
                stop sound fadeout 1.0
                scene bg black
                #show loading_icon
                with fade

                play sound "audio/looping/STP_jungle_loop.ogg" loop fadein 1.0
                voice "audio/voices/ch2/beast/narrator/ch2_bn_9.flac"
                scene bg beast stairs onlayer back at Position(ypos=1125)
                with fade
                if persistent.quick_menu:
                    $ quick_menu = True
                n "The door to the basement creaks open, revealing what's left of an old, wooden staircase. It's still sturdy enough that you can make your way down in one piece, though you'll have to be mindful of holes.\n"
                voice "audio/voices/ch2/beast/narrator/ch2_bn_10.flac"
                n "The air seeping up from below is oddly warm and wet, as if you're descending into a jungle. If the Princess lives here, slaying her would probably be doing her a favor.\n"
                voice "audio/voices/ch2/beast/narrator/ch2_bn_11.flac"
                n "She growls up the stairs.\n"
                voice "audio/voices/ch2/beast/princess/ch2_bp_1.flac"
                sp "I can smell you.\n"
                voice "audio/voices/ch2/beast/hero/ch2_bh_4.flac"
                hero "She sounds almost... feral.\n"
                voice "audio/voices/ch2/beast/hunted/ch2_hunt_15.flac"
                hunted "Impatient. Or maybe eager.\n"
                play audio "audio/one_shot/footsteps_creaky.flac"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_37.flac"
                hide bg onlayer back
                hide loading_icon
                scene bg black with dissolve
                n "You carefully make your way down the stairs.\n"
                $ gallery_beast.unlock_item(2)
                $ renpy.save_persistent()
                voice "audio/voices/ch2/beast/narrator/ch2_bn_12.flac"
                $ quick_menu = False
                scene farback beast basement onlayer farback at Position(ypos=1125)
                show bg beast basement onlayer back at Position(ypos=1125)
                show beast d repose onlayer back at Position(ypos=1125)
                show fore beast basement onlayer inyourface at Position(ypos=1125)
                with fade
                if persistent.quick_menu:
                    $ quick_menu = True
                n "The last step gives way to the damp earth floor of a starlit pit. The walls are obscured by an impenetrable darkness, giving the illusion that the room might stretch on forever. You brush against the wide leaves of plants that surround you on all sides, seemingly the only living things that occupy this strange underground wilderness.\n"
                voice "audio/voices/ch2/beast/hunted/ch2_hunt_16.flac"
                hunted "The jungle is pressing in on us... hiding her from view. She could be anywhere.\n"
                #hunted "Last time we were down here, there were two chains on the wall, and one of them was empty. There they are again.\n"
                play audio "audio/one_shot/new/STP_chainsmovement_1.flac"
                show beast d startle onlayer back at Position(ypos=1125)
                with dissolve
                $ renpy.pause(0.125)
                hide beast onlayer back with dissolve
                voice "audio/voices/ch2/beast/narrator/ch2_bn_13.flac"
                n "You see only a flash of the Princess before she scurries away into the underbrush, dragging her heavy chain behind her.\n"
                voice "audio/voices/ch2/beast/narrator/ch2_bn_14.flac"
                n "Remember, she's just a Princess.\n"
                play audio "audio/one_shot/new/STP_chainsmovement_2.flac"
                voice "audio/voices/ch2/beast/hero/ch2_bh_5a.flac"
                hero "She is certainly {i}not{/i} just a Princess.\n"
                voice "audio/voices/ch2/beast/narrator/ch2_bn_15a.flac"
                n "You're not helping.\n"
                voice "audio/voices/ch2/beast/hunted/ch2_hunt_17.flac"
                hunted "It doesn't matter what she is. It only matters what she does.\n"
                play audio "audio/one_shot/new/STP_chainsmovement_3.flac"
                show beast d stare onlayer back at Position(ypos=1125) with dissolve
                voice "audio/voices/ch2/beast/narrator/ch2_bn_16.flac"
                n "Her shining eyes appear between the leaves, staring hungrily at you from the darkness.\n"
                #n "She emerges, her shining eyes and glistening claws visible in the gloom, staring hungrily at your from the darkness.\n"
                stop music fadeout 1.0
                if beast_1_cabin_blade_taken:
                    voice "audio/voices/ch2/beast/princess/ch2_bp_2.flac"
                    spmid "I can hear your heart pounding from the bottom of the stairs, fledgling. You're right to be terrified.\n"
                    voice "audio/voices/ch2/beast/princess/ch2_bp_2a.flac"
                    sp "I'm so much more than you, and a little splinter clutched in trembling hands won't save you from me.\n"
                else:
                    voice "audio/voices/ch2/beast/princess/ch2_bp_3.flac"
                    spmid "I can hear your heart pounding from the bottom of the stairs, fledgling. You're right to be terrified. I'm so much more than you.\n"

                jump beast_1_encounter_start
