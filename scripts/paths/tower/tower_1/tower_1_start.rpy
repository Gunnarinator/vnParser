label tower_1_start:
    $ blade_held = False
    $ trait_broken = True
    $ quick_menu = False
    play sound "audio/looping/uncomfortable ambiance.ogg" loop fadein 1.0
    scene chapter tower with fade
    show text _("{color=#FFFFFF00}Chapter 2. The Tower.{/color}") at Position(ypos=850)
    $ renpy.pause(4.0)

    play sound "audio/looping/uncomfortable ambiance.ogg" loop
    play secondary "audio/looping/uncomfortable ambiance heightened.ogg" loop
    play music "audio/_music/ch1/Fragmentation.flac" loop
    scene bg path onlayer farback at flip, Position(ypos=1125)
    show midground path onlayer back at flip, Position(ypos=1125)
    show front path onlayer front at flip, Position(ypos=1125)
    show bg black
    #show loading_icon
    hide chapter
    hide text
    with fade

    if persistent.quick_menu:
        $ quick_menu = True
    $ gallery_tower.unlock_gallery()
    $gallery_zch1.unlock_item(5)
    $ renpy.save_persistent()
    voice "audio/voices/ch1/woods/narrator/script_n_1.flac"
    n "You're on a path in the woods. And at the end of that path is a cabin. And in the basement of that cabin is a Princess.\n"
    voice "audio/voices/ch1/woods/narrator/script_n_2.flac"
    n "You're here to slay her.\n If you don't, it will be the end of the world.\n"
    label tower_1_forest:
        default tower_1_forest_count = 0
        default tower_1_forest_share_died = False
        default tower_1_forest_share_loop = False
        default tower_1_forest_princess_press = False
        default tower_1_forest_share_loop_insist = False
        default tower_1_forest_deja_vu = False
        default tower_1_forest_deja_vu_follow_up = False
        menu:
            extend ""

            "{i}• (Explore) I'm getting a terrible sense of deja vu.{/i}" if tower_1_forest_share_loop == False:
                $ tower_1_forest_deja_vu = True
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_1a.flac"
                n "A terrible sense of deja vu? No, you don't have that. This is the first time either of us have been here.\n"
                label tower_1_forest_narrator_share_join:
                    $ tower_1_forest_count += 1
                    $ tower_1_forest_share_loop = True
                    voice "audio/voices/ch2/shared/hero/ch2_share_h_1.flac"
                    hero "If He doesn't remember what happened, then maybe it's best to keep it that way.\n"
                    voice "audio/voices/ch2/tower/narrator/ch2_tn_1.flac"
                    n "You know I can hear you, right? It's going to be a lot harder than you think to keep secrets from me.\n"
                    voice "audio/voices/ch2/tower/broken/ch2_broken_1.flac"
                    broken "What does it matter what He knows? There's nothing we can do to stop her. She's just going to kill us again.\n"
                    voice "audio/voices/ch2/tower/narrator/ch2_tn_2.flac"
                    n "She is {i}not{/i} going to kill you unless you let her. But slaying the Princess and saving the world is going to be much more difficult than it has to be if you spend the whole time second guessing yourself.\n"
                    jump tower_1_forest

            "{i}• (Explore) This is more than just deja vu, though. I'm pretty sure this whole thing literally just happened.{/i}" if tower_1_forest_deja_vu and tower_1_forest_deja_vu_follow_up == False:
                $ tower_1_forest_deja_vu_follow_up = True
                $ tower_1_forest_count += 1
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_1b.flac"
                n "It hasn't. Or if it has, I certainly haven't been a part of it. Like I said, we've just met for the first time, you and I.\n"
                jump tower_1_forest

            "{i}• (Explore) Wait... hasn't this already happened?{/i}" if tower_1_forest_share_loop == False:
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_1b.flac"
                n "It hasn't. Or if it has, I certainly haven't been a part of it. We've just met for the first time, you and I.\n"
                jump tower_1_forest_narrator_share_join

            "{i}• (Explore) Okay, no.{/i}" if tower_1_forest_share_loop == False:
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_3a.flac"
                n "Oh, don't you start grandstanding about morals. The fate of the world is at risk right now, and the life of a mere Princess shouldn't stop you from saving us all.\n"
                jump tower_1_forest_narrator_share_join

            "{i}• (Explore) But I died! What am I doing here?{/i}" if tower_1_forest_share_loop == False:
                $ tower_1_forest_share_died = True
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_4.flac"
                n "I can assure you that you're not dead. And to answer your second question, you're here to slay the Princess. I literally told you that a second ago.\n"
                jump tower_1_forest_narrator_share_join

            "{i}• (Explore) She's going to kill me again!{/i}" if tower_1_forest_share_loop == False:
                $ tower_1_forest_share_died = True
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_5.flac"
                n "Again? People don't die twice. You haven't even met the Princess, and I hardly think she'd be capable of killing someone as skilled and courageous as yourself.\n"
                jump tower_1_forest_narrator_share_join

            "{i}• (Explore) Let's assume I'm telling the truth, and all of this really did already happen. Why should I listen to you? Why should I bother doing {i}anything{/i}?{/i}" if tower_1_forest_share_loop and (tower_1_forest_deja_vu == False or (tower_1_forest_deja_vu_follow_up)) and tower_1_forest_share_loop_insist == False:
                $ tower_1_forest_share_loop_insist = True
                $ tower_1_forest_count += 1
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_6.flac"
                n "Those are two very different questions, but fine. I'll indulge you if that's what it takes to get you moving.\n"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_7.flac"
                n "Let's say for a moment that this really is the second time you've met me, or, at least, a version of me.\n"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_9.flac"
                n "You died last time, which probably only happened because you didn't listen to me.\n"
                if tower_unharmed:
                    voice "audio/voices/ch2/tower/broken/ch2_broken_2.flac"
                    broken "Of course we died. We couldn't land a {i}single{/i} blow on her and she broke every bone in our body before she decided to let us die.\n"
                else:
                    voice "audio/voices/ch2/tower/broken/ch2_broken_3.flac"
                    broken "Of course we died. She didn't feel pain. She didn't feel much of anything, did she? And she broke every bone in our body before she decided to let us die.\n"
                voice "audio/voices/ch2/tower/broken/ch2_broken_4.flac"
                broken "What were we supposed to do to stop her then? What are we supposed to do to stop her now? It's pointless.\n"
                voice "audio/voices/ch2/tower/narrator/ch2_tn_3.flac"
                n "She's {i}just{/i} a Princess. Slaying her shouldn't have been difficult, but congratulations. You've been given another chance to actually do this right.\n"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_11.flac"
                n "And I believe your other question was something along the lines of 'what's the point of doing anything?' If you're asking that, it sounds to me like you're making the rather dangerous assumption that your actions last time around didn't have any consequences.\n"
                voice "audio/voices/ch2/tower/hero/ch2_th_1.flac"
                hero "What do you mean? Of course there weren't any consequences. The Princess killed us, and now everyone's right back where they started. That sounds pretty consequence-free to me.\n"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_12.flac"
                n "Yes, but, in this purely hypothetical scenario, that begs the question of {i}how{/i} you got back here. Did 'time' simply rewind itself, or were you instead transported to a different world entirely?\n"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_13.flac"
                n "If it's the latter, what do you think happened {i}after{/i} you died?\n"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_13a.flac"
                n "Do you think the people there lived happily ever after, or do you think that the Princess, left unhindered, brought about the end to everyone and everything, just like I told you she would?\n"
                voice "audio/voices/ch2/tower/broken/ch2_broken_5.flac"
                broken "If she ended the entire world, why should we even bother? We might as well just walk up to that cabin, break her chains, and let her do whatever she wants. It's all the same in the end.\n"
                voice "audio/voices/ch2/tower/narrator/ch2_tn_5.flac"
                #n "Just because she's capable of ending the world doesn't mean that you're {i}not{/i} capable of slaying her. Both of those things can be true at the same time. So chin up, I believe in you. You can do this.\n"
                n "Just because she's capable of ending the world doesn't mean that you're not capable of slaying her. Both of those things can be true at the same time. So chin up, I believe in you.\n"
                jump tower_1_forest

            "{i}• (Explore) Let's talk about this Princess...{/i}" if tower_1_forest_share_loop_insist and tower_1_forest_princess_press == False:
                $ tower_1_forest_count += 1
                $ tower_1_forest_princess_press = True
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_14.flac"
                n "Just be quick about it.\n"
                label tower_1_forest_princess:
                    default tower_1_forest_princess_count = 0
                    default tower_1_forest_princess_why_strong = False
                    default tower_1_forest_princess_basement_explain = False
                    default tower_1_forest_princess_why_me = False
                    default tower_1_forest_princess_cagey = False
                    default tower_1_forest_princess_tips = False
                    default tower_1_forest_pessimism_comment = False
                    menu:
                        extend ""

                        "{i}• (Explore) She killed me last time around. How can I make sure that doesn't happen again?{/i}" if tower_1_forest_princess_tips == False:
                            $ tower_1_forest_princess_tips = True
                            $ tower_1_forest_princess_count += 1
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_15.flac"
                            n "Like I said, if she killed you, it was probably because you didn't listen to me. Don't talk to her. Don't trust her. Just go in, do your job, and save the world.\n"
                            jump tower_1_forest_princess

                        "{i}• (Explore) All she did last time around was beat me to death. How can someone like that end the world?{/i}" if tower_1_forest_princess_why_strong == False:
                            $ tower_1_forest_princess_why_strong = True
                            $ tower_1_forest_princess_count += 1
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_16a.flac"
                            n "She just can. Believe me, I wish I could tell you more, but you'll just have to trust that what I'm saying is true and that, despite it all, you're fully up to the task that's been given to you.\n"
                            if tower_1_forest_pessimism_comment == False:
                                $ tower_1_forest_pessimism_comment = True
                                voice "audio/voices/ch2/tower/broken/ch2_broken_6.flac"
                                broken "We're not. We might as well just pledge ourselves to her and stop pretending that we're capable of doing anything in this situation. She probably doesn't even need to try to overpower us.\n"
                                voice "audio/voices/ch2/tower/hero/ch2_th_2.flac"
                                hero "Can we tone down the pessimism just a smidge?\n"
                                voice "audio/voices/ch2/tower/broken/ch2_broken_7.flac"
                                broken "I'm not being a pessimist. I'm just being {i}realistic{/i}.\n"
                                voice "audio/voices/ch2/tower/hero/ch2_th_3.flac"
                                hero "You're being annoying.\n"
                                voice "audio/voices/ch2/tower/narrator/ch2_tn_8.flac"
                                n "Just ignore their bickering, and whatever you do, don't 'pledge yourself to her.' I cannot stress enough how absolutely {i}catastrophic{/i} that would be for everyone. Yourself included.\n"
                            jump tower_1_forest_princess

                        "{i}• (Explore) To quote you from last time around, 'she's {i}just{/i} a Princess.' Why was she strong enough to beat me to death with her bare hands?{/i}" if tower_1_forest_princess_why_strong == False:
                            $ tower_1_forest_princess_why_strong = True
                            $ tower_1_forest_princess_count += 1
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_17.flac"
                            n "She {i}is{/i} just a Princess. Whatever you think happened to you last time, just get it out of your head before you get to the cabin, and you'll be {i}fine{/i}.\n"
                            if tower_1_forest_pessimism_comment == False:
                                $ tower_1_forest_pessimism_comment = True
                                voice "audio/voices/ch2/tower/broken/ch2_broken_8.flac"
                                broken "Or we could pledge ourselves to her and stop pretending that we're capable of doing anything in this situation. She probably doesn't even need to try to overpower us.\n"
                                voice "audio/voices/ch2/tower/hero/ch2_th_2.flac"
                                hero "Can we tone down the pessimism just a smidge?\n"
                                voice "audio/voices/ch2/tower/broken/ch2_broken_7.flac"
                                broken "I'm not being a pessimist. I'm just being {i}realistic{/i}.\n"
                                voice "audio/voices/ch2/tower/hero/ch2_th_3.flac"
                                hero "You're being annoying.\n"
                                voice "audio/voices/ch2/tower/narrator/ch2_tn_8.flac"
                                n "Just ignore their bickering, and whatever you do, don't 'pledge yourself to her.' I cannot stress enough how absolutely {i}catastrophic{/i} that would be for everyone. Yourself included.\n"
                            jump tower_1_forest_princess

                        "{i}• (Explore) Who locked her in that basement? What {b}is{/b} this place?{/i}" if tower_1_forest_princess_basement_explain == False:
                            $ tower_1_forest_princess_basement_explain = True
                            $ tower_1_forest_princess_count += 1
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_18.flac"
                            n "{i}People{/i} locked her in that basement. And I told you what this place is. It's a path in the woods. Don't overcomplicate things.\n"
                            jump tower_1_forest_princess

                        "{i}• (Explore) If people locked her away, why couldn't {b}they{/b} slay her? Why is this falling on me?{/i}" if tower_1_forest_princess_basement_explain and tower_1_forest_princess_why_me == False:
                            $ tower_1_forest_princess_why_me = True
                            $ tower_1_forest_princess_count += 1
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_19.flac"
                            n "Look, I'm not supposed to say this but it's because you're special. You're the {i}only{/i} person capable of doing this. Call it a prophecy if that helps, but it's just the way things are.\n"
                            voice "audio/voices/ch2/shared/hero/ch2_share_h_2.flac"
                            hero "Oh. I didn't know we were {i}special{/i}.\n"
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_20a.flac"
                            n "Of course you're special. Why else would you be here?\n"
                            voice "audio/voices/ch2/tower/broken/ch2_broken_9.flac"
                            broken "Who cares if {i}you{/i} think we're special? As far as I can tell, the only thing special about us is that we get to experience painfully dying all over again.\n"
                            jump tower_1_forest_princess

                        "{i}• (Explore) You're being cagey. What aren't you telling me?{/i}" if tower_1_forest_princess_cagey == False and tower_1_forest_princess_count > 1:
                            $ tower_1_forest_princess_cagey = True
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_21.flac"
                            n "I've told you everything you need to know, going into more detail would just overcomplicate an otherwise very simple situation and make your job more difficult.\n"
                            if tower_1_forest_pessimism_comment == False:
                                $ tower_1_forest_pessimism_comment = True
                                voice "audio/voices/ch2/tower/broken/ch2_broken_10.flac"
                                broken "Even if He's hiding something, I doubt it would help us. I'm sure knowing what He knows would only make things worse.\n"
                                voice "audio/voices/ch2/tower/hero/ch2_th_2.flac"
                                hero "Can we tone down the pessimism just a smidge?\n"
                                voice "audio/voices/ch2/tower/broken/ch2_broken_7.flac"
                                broken "I'm not being a pessimist. I'm just being {i}realistic{/i}.\n"
                                voice "audio/voices/ch2/tower/hero/ch2_th_3.flac"
                                hero "You're being annoying.\n"
                                voice "audio/voices/ch2/tower/narrator/ch2_tn_8.flac"
                                n "Just ignore their bickering, and whatever you do, don't 'pledge yourself to her.' I cannot stress enough how absolutely {i}catastrophic{/i} that would be for everyone. Yourself included.\n"
                            else:
                                voice "audio/voices/ch2/shared/narrator/ch2_share_n_22.flac"
                                n "The less you know about her, the better.\n"
                            jump tower_1_forest_princess

                        "{i}• Nevermind.{/i}" if tower_1_forest_princess_count == 0:
                            label tower_1_forest_princess_leaving:
                                voice "audio/voices/ch2/shared/narrator/ch2_share_n_24.flac"
                                n "Great. Now if you don't mind, the whole world is waiting with bated breath for you to save it from ruin.\n"
                                jump tower_1_forest

                        "{i}• That's all.{/i}" if tower_1_forest_princess_count != 0:
                            jump tower_1_forest_princess_leaving

            "{i}• [[Proceed to the cabin.]{/i}":
                jump tower_1_cabin_arrival

            "{i}• [[Turn around and leave.]{/i}" if mound_can_attempt_flee:
                if loops_finished >= 2:
                    $ mound_can_attempt_flee = False
                    voice "audio/voices/mound/bonus/flee.flac"
                    mound "You have already committed to my completion. You cannot go further astray.\n"
                    jump tower_1_forest
                voice "audio/voices/ch2/tower/broken/ch2_broken_11.flac"
                broken "You're right. We should just leave. There's nothing we can do to stop her, so we might as well enjoy what little time we have left.\n"
                jump turn_and_leave_join

label tower_1_cabin_arrival:
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
    if tower_1_forest_pessimism_comment == False:
        $ tower_1_forest_pessimism_comment = True
        voice "audio/voices/ch2/tower/broken/ch2_broken_12.flac"
        broken "We might as well just pledge ourselves to her and stop pretending we're capable of doing anything in this situation. She probably doesn't even need to try to overpower us.\n" id tower_1_cabin_arrival_7460a29f
        voice "audio/voices/ch2/tower/hero/ch2_th_2.flac"
        hero "Can we tone down the pessimism just a smidge?\n"
        voice "audio/voices/ch2/tower/broken/ch2_broken_7.flac"
        broken "I'm not being a pessimist. I'm just being {i}realistic{/i}.\n"
        voice "audio/voices/ch2/tower/hero/ch2_th_3.flac"
        hero "You're being annoying.\n"
        voice "audio/voices/ch2/tower/narrator/ch2_tn_8.flac"
        n "Just ignore their bickering, and whatever you do, don't 'pledge yourself to her.' I cannot stress enough how absolutely {i}catastrophic{/i} that would be for everyone. Yourself included.\n"
        voice "audio/voices/ch2/tower/hero/ch2_th_4.flac"
        hero "I agree. If she's wrongfully imprisoned then we should rescue her, but if He's telling the truth, we shouldn't just hand her the world on a silver platter.\n"
        voice "audio/voices/ch2/tower/narrator/ch2_tn_12.flac"
        n "'Rescue her?' Given the stakes of the situation, there isn't really a difference between 'rescuing her' and 'pledging yourself to her.' Either would be terrible.\n"
        voice "audio/voices/ch2/tower/narrator/ch2_tn_13.flac"
        n "So please, try to ignore {i}both{/i} of those knuckleheads and focus on saving the world. Let's not make this harder than it has to be.\n"
    else:
        voice "audio/voices/ch2/tower/broken/ch2_broken_13a.flac"
        broken "Lying? Cheating? Why would she even bother? She didn't need to do anything like that last time.\n"
        voice "audio/voices/ch2/tower/hero/ch2_th_bonus.flac"
        hero "She caught us off-guard last time. We'll be fine. Let's just keep our wits about us.\n"
        #n "'Talk some sense into her?' Please, ignore {i}both{/i} of those knuckleheads and focus on saving the world. Let's not make this harder than it has to be.\n"
        voice "audio/voices/ch2/tower/narrator/ch2_tn_bonus.flac"
        n "At least one of you has a shred of sense. Just make sure you listen to {i}him{/i} and not that... whiner.\n"
    menu:
        extend ""

        "{i}• [[Proceed into the cabin.]{/i}":
            label tower_stranger_rejoin:
                voice "audio/voices/ch2/tower/broken/ch2_broken_14.flac"
                broken "If that's what you want... I guess I don't have a say here.\n"
                play audio "audio/one_shot/enter_cabin_audio.flac"
                $ quick_menu = False
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

    $ gallery_tower.unlock_item(1)
    $ renpy.save_persistent()
    play sound "audio/looping/uncomfortable ambiance heightened.ogg" loop fadein 1.0
    play music "audio/_music/ch2/tower/The Tower.flac" loop fadein 1.0
    scene farback tower cabin onlayer farback at Position(ypos=1125)
    show bg tower cabin onlayer back at Position(ypos=1125)
    show door tower1 onlayer back at Position(ypos=1125)
    show table tower onlayer back at Position(ypos=1125)
    show knife tower onlayer back at Position(ypos=1125)
    show mirror tower onlayer back at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    voice "audio/voices/ch2/tower/narrator/ch2_tn_15.flac"
    n "The interior of the cabin is larger and more grandiose than its humble exterior would suggest. The only furniture of note is a massive marble altar with a pristine blade perched on its edge.\n"
    voice "audio/voices/ch2/shared/narrator/ch2_share_n_25.flac"
    n "The blade is your implement. You'll need it if you want to do this right.\n"
    voice "audio/voices/ch2/tower/hero/ch2_th_6.flac"
    hero "Why do we feel so... {i}small{/i}?\n"
    voice "audio/voices/ch2/tower/broken/ch2_broken_15.flac"
    broken "We don't feel small. We {i}are{/i} small.\n"
    label cabin_interior_2_tower_menu:
        default tower_1_cabin_mirror_present = True
        default tower_1_cabin_blade_taken = False
        default tower_1_cabin_mirror_ask = False
        default tower_1_cabin_mirror_approached = False
        default tower_1_cabin_last_time_comment = False
        menu:
            extend ""

            "{i}• (Explore) You didn't say anything about the mirror on the wall.{/i}" if tower_1_cabin_mirror_ask == False and tower_1_cabin_mirror_present:
                $ tower_1_cabin_mirror_ask = True
                $ current_run_mirror_comment = True
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_39.flac"
                n "That's because there isn't a mirror. There's the altar, the blade sitting on the altar, and the door to the basement. There's nothing else in here.\n"
                voice "audio/voices/ch2/shared/hero/ch2_share_h_4.flac"
                hero "There's definitely a mirror.\n"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_27.flac"
                n "There isn't.\n"
                voice "audio/voices/ch2/tower/broken/ch2_broken_16.flac"
                broken "Who cares if there's a mirror? We're all going to die anyway, and I'm sure that if we looked in there we'd just see something sad and miserable looking back at us. We don't need any reminders of what we are. It would only make things worse.\n"
                voice "audio/voices/ch2/tower/narrator/ch2_tn_16.flac"
                n "{i}Sigh{/i}. For the last time, you're not going to die unless you let it happen. And luckily for you, there isn't a mirror, so no one needs to worry about confronting a grisly visage any time in the near future.\n"
                voice "audio/voices/ch2/tower/narrator/ch2_tn_17.flac"
                n "Though, for what it's worth, if there were a mirror, I'm sure that you wouldn't find anything 'sad' or 'miserable' in it looking back at you. You probably look perfectly normal.\n"
                voice "audio/voices/ch2/tower/hero/ch2_th_7.flac"
                hero "'Probably?' Do you not know what we look like?\n"
                voice "audio/voices/ch2/tower/broken/ch2_broken_17.flac"
                broken "He knows. He just doesn't have the heart to tell us.\n"
                menu:
                    extend ""

                    "{i}• I care about whether I'm being lied to. There's a mirror.{/i}":
                        voice "audio/voices/ch2/tower/hero/ch2_th_8.flac"
                        hero "As do I, and yeah, there is.\n"
                        #n "I'm not lying to you, I {i}promise{/i}. There isn't a mirror. Really.\n"
                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_30.flac"
                        n "I'm not lying to you. Use your eyes, there is no mirror. Why would I lie about something so meaningless? What good would a mirror even do? Let you waste time preening yourself instead of doing what needs to be done?\n"

                    "{i}• I want to look at myself. I want to see how {b}handsome{/b} I am.{/i}":
                        voice "audio/voices/ch2/tower/broken/ch2_broken_18.flac"
                        broken "Please don't. I'd rather the Princess kill us again than see how dreadful we are.\n"
                        voice "audio/voices/ch2/tower/hero/ch2_th_9.flac"
                        hero "I care less about what we look like and more about whether we're being lied to. If He's willing to lie about something as innocuous as a mirror, what else is He hiding from us?\n"
                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_29.flac"
                        n "I'm not lying to you. Use your eyes, there is no mirror. Why would I lie about something so meaningless? What good would it even do?\n"

                    "{i}• It doesn't matter if there's a mirror.{/i}":
                        $ tower_1_cabin_mirror_present = False
                        voice "audio/voices/ch2/shared/hero/ch2_share_h_5.flac"
                        hero "But it {i}does{/i} matter! Don't you care if we're being lied to? If He's willing to lie about something as innocuous as a mirror, what else is He hiding from us?\n"
                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_30.flac"
                        hide mirror onlayer back
                        n "I'm not lying to you. Use your eyes, there is no mirror. Why would I lie about something so meaningless? What good would a mirror even do? Let you waste time preening yourself instead of doing what needs to be done?\n"
                        voice "audio/voices/ch2/shared/hero/ch2_share_h_6.flac"
                        hero "But there {i}was{/i} a mirror a second ago.\n"
                        voice "audio/voices/ch2/tower/broken/ch2_broken_19.flac"
                        broken "We should count ourselves lucky. Some things are better left unseen.\n"

                    "{i}• [[Remain silent.]{/i}":
                        voice "audio/voices/ch2/shared/hero/ch2_share_h_7b.flac"
                        hero "I care about whether we're being lied to. If He's willing to lie about something as innocuous as a mirror, what else could He hiding from us?\n"
                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_31.flac"
                        n "I'm not lying to you, I {i}promise{/i}. There isn't a mirror. Really.\n"

                    "{i}• [[Approach the mirror.]{/i}" if tower_1_cabin_mirror_approached == False:
                        label tower_cabin_1_mirror_join:
                            play audio "audio/one_shot/footsteps_creaky.flac"
                            hide farback onlayer farback
                            hide bg onlayer back
                            hide door onlayer back
                            hide table onlayer back
                            hide knife onlayer back
                            hide mirror onlayer back
                            scene bg tower mirror onlayer front at Position(ypos=1125)
                            show mirror tower close onlayer front at Position(ypos=1125)
                            with dissolve
                            $ tower_1_cabin_mirror_approached = True
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_32.flac"
                            n "You walk up to the wall next to the basement door. It's a wall. There isn't much to see here.\n"
                            if tower_1_cabin_mirror_ask == False:
                                voice "audio/voices/ch2/shared/hero/ch2_share_h_8.flac"
                                hero "What are you talking about? This isn't a wall. It's a mirror. Or at least it'll {i}be{/i} a mirror once we wipe off that layer of grime.\n"
                            else:
                                voice "audio/voices/ch2/shared/hero/ch2_share_h_9.flac"
                                hero "This really isn't funny.\n"
                            $ current_run_mirror_touched = True
                            menu:
                                extend ""

                                "{i}• [[Wipe the mirror clean.]{/i}":
                                    $ tower_1_cabin_mirror_present = False
                                    hide mirror onlayer front
                                    play audio "audio/one_shot/new/STP_claws_1.flac"
                                    show player wall onlayer front at Position(ypos=1125) with dissolve
                                    if tower_1_cabin_mirror_ask == False:
                                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_33.flac"
                                    else:
                                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_33a.flac"
                                    n "You reach forward and rub your hand against the cabin wall. I hope you know how ridiculous you look right now.\n"
                                    hide player onlayer front with dissolve
                                    #voice "audio/voices/ch2/shared/hero/ch2_share_h_10.flac"
                                    #hero "But it was there a second ago!\n"
                                    voice "audio/voices/ch2/tower/broken/ch2_broken_19.flac"
                                    broken "We should count ourselves lucky. Some things are better left unseen.\n"
                                    play audio "audio/one_shot/footsteps_creaky.flac"
                                    hide bg onlayer front
                                    scene farback tower cabin onlayer farback at Position(ypos=1125)
                                    show bg tower cabin onlayer back at Position(ypos=1125)
                                    show door tower1 onlayer back at Position(ypos=1125)
                                    show table tower onlayer back at Position(ypos=1125)
                                    if tower_1_cabin_blade_taken == False:
                                        show knife tower onlayer back at Position(ypos=1125)
                                    with dissolve
                                    jump cabin_interior_2_tower_menu

                jump cabin_interior_2_tower_menu

            "{i}• (Explore) This whole cabin is different than last time.{/i}" if tower_1_cabin_last_time_comment == False and tower_1_forest_share_loop_insist:
                $ tower_1_cabin_last_time_comment = True
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_34.flac"
                n "Maybe that's because you haven't actually been here. I hope this means you'll finally drop that ridiculous past-life nonsense. You haven't died, and you certainly haven't been killed by the Princess.\n"
                #hero "I don't know about you, but I feel absolutely tiny.\n"
                #broken "That's just you. We've always been this small.\n"
                #n "Focus up, you three. A lot's riding on this.\n"
                jump cabin_interior_2_tower_menu

            "{i}• (Explore) [[Approach the mirror.]{/i}" if tower_1_cabin_mirror_present and tower_1_cabin_mirror_approached == False:
                $ tower_1_cabin_mirror_approached = True
                jump tower_cabin_1_mirror_join

            "{i}• (Explore) [[Take the blade.]{/i}" if tower_1_cabin_blade_taken == False:
                $ tower_resist_count += 1
                $ tower_1_cabin_blade_taken = True
                $ blade_held = True
                $ default_mouse = "blade"

                voice "audio/voices/ch2/tower/narrator/ch2_tn_18.flac"
                play audio "audio/one_shot/knife_pickup.flac"
                hide knife onlayer back
                with dissolve
                n "You take the blade from the altar. It would be difficult to slay the Princess and save the world without a weapon.\n"
                jump cabin_interior_2_tower_menu

            "{i}• [[Enter the basement.]{/i}":
                if tower_1_cabin_blade_taken == False:
                    $ tower_submit_count += 1
                    #hero "No blade this time? So we're going to talk our way out of this?\n"
                    voice "audio/voices/ch2/tower/hero/ch2_th_10.flac"
                    hero "No blade this time? Yeah. Maybe she'll be more receptive if we're unarmed.\n"
                    #n "That would be a mistake.\n"
                    voice "audio/voices/ch2/tower/broken/ch2_broken_20.flac"
                    broken "Blade. No blade. It doesn't matter.\n"

                play audio "audio/one_shot/door_stone.flac"
                $ quick_menu = False
                show door tower2 onlayer back at Position(ypos=1125)
                with Dissolve(1.0)
                hide mirror onlayer back
                show door tower3 onlayer back at Position(ypos=1125) with Dissolve(1.5)
                hide farback onlayer farback
                hide bg onlayer back
                hide door onlayer back
                hide table onlayer back
                hide knife onlayer back
                hide mirror onlayer back
                with fade
                scene bg black
                #show loading_icon
                with fade


                # get to da basement.
                voice "audio/voices/ch2/tower/narrator/ch2_tn_20.flac"
                scene bg tower stairs onlayer back at Position(ypos=1125)
                with fade
                if persistent.quick_menu:
                    $ quick_menu = True
                n "The door to the basement creaks open, revealing a spiral staircase, its steps almost as deep as you are tall. The smell of incense drifts up from below. For a moment, you almost feel at ease.\n"
                voice "audio/voices/ch2/tower/broken/ch2_broken_21.flac"
                broken "Huh. This is actually kind of nice.\n"
                voice "audio/voices/ch2/tower/narrator/ch2_tn_20b.flac"
                n "It's still a stone basement. If the Princess lives here, slaying her is probably doing her a favor.\n"

                #voice "audio/voices/ch2/tower/narrator/ch2_tn_21.flac"
                #n "Don't let it deceive you. This is all part of the manipulation.\n"
                voice "audio/voices/ch2/tower/narrator/ch2_tn_23.flac"
                n "Her booming voice rolls up the stairs.\n"
                voice "audio/voices/ch2/tower/princess/ch2_tp_1.flac"
                p "Is that a guest I hear? Don't linger on the stairs. {outlinecolor=4f1313}{color=#e44646}Come down and witness me.{/color}{/outlinecolor}\n"
                voice "audio/voices/ch2/tower/hero/ch2_th_11.flac"
                hero "You weren't kidding when you said it was 'booming.' She wasn't like this last time.\n"
                if tower_1_cabin_blade_taken == False:
                    voice "audio/voices/ch2/tower/narrator/ch2_tn_22.flac"
                    n "You shouldn't have come down here unarmed.\n"
                voice "audio/voices/ch2/tower/broken/ch2_broken_22.flac"
                broken "We need to get down there. She wants us to see her. We need to see her.\n"
                voice "audio/voices/ch2/tower/hero/ch2_th_12.flac"
                hero "Should we be worried about your sudden change in attitude? Just a few minutes ago you were going on about how pointless everything was, now you {i}want{/i} to go down there?\n"
                voice "audio/voices/ch2/tower/narrator/ch2_tn_25.flac"
                n "It doesn't matter what that little voice says. He's not the one making the decisions... Though if his ramblings get you to the Princess, they get you to the Princess.\n"
                menu:
                    extend ""

                    "{i}• [[Continue down the stairs.]{/i}":
                        $ fake_variable = False

                play audio "audio/one_shot/tower_stairs_fall.flac"
                $ quick_menu = False
                hide bg onlayer back
                scene bg black onlayer back at Position(ypos=1125)
                with fade
                voice "audio/voices/ch2/tower/narrator/ch2_tn_26.flac"
                n "Making your way down the spiral staircase is a time consuming and exhausting effort, every step requiring you to clamber over one edge before dropping to the next. But soon, the end comes into view, and you tumble to the bottom, entering the vast, temple-like room beyond.\n"
                $ gallery_tower.unlock_item(2)
                $ renpy.save_persistent()
                hide bg onlayer back
                scene farback tower basement onlayer farback at Position(ypos=1350)
                show bg tower basement onlayer back at Position(ypos=1350)
                show flutter tower onlayer back at Position(ypos=1350)
                show tower d neutral onlayer back at Position(ypos=1350)
                with fade
                if persistent.quick_menu:
                    $ quick_menu = True
                voice "audio/voices/ch2/tower/narrator/ch2_tn_27.flac"
                n "The Princess towers over you, almost glowing in the weak starlight, her figure framed by a stained glass window. Her long hair billows around her, and a chain binds her wrist to the far wall.\n"
                #voice "audio/voices/ch2/tower/hero/ch2_th_13.flac"
                #hero "That... isn't what she looked like last time.\n"
                voice "audio/voices/ch2/tower/broken/ch2_broken_23.flac"
                broken "The chain is nothing to her. It might as well be a toy for all the good it would do. I told you it was pointless to resist her.\n"
                voice "audio/voices/ch2/tower/princess/ch2_tp_2.flac"
                show tower d talk onlayer back with dissolve
                p "The little bird has returned to me. I wonder what he wants.\n"
                if tower_1_cabin_blade_taken:
                    voice "audio/voices/ch2/tower/princess/ch2_tp_3.flac"
                    show tower d smile talk onlayer back with dissolve
                    p "You've brought that knife again... even though you know it's useless. Such charming audacity.\n"
                    voice "audio/voices/ch2/tower/princess/ch2_tp_4.flac"
                    show tower d neutral onlayer back with dissolve
                    sp "{i}Drop it{/i}.\n"
                    default tower_1_basement_drop_tighten = False
                    menu:
                        extend ""

                        "{i}• Drop it.{/i}":
                            $ tower_submit_count += 1
                            $ blade_held = False
                            $ default_mouse = "default"
                            play audio "audio/one_shot/knife_bounce_several.flac"
                            voice "audio/voices/ch2/tower/narrator/ch2_tn_28.flac"
                            n "The blade slips from your fingers and clatters uselessly to the floor.\n"
                            voice "audio/voices/ch2/tower/hero/ch2_th_14.flac"
                            hero "We didn't have to do that.\n"
                            voice "audio/voices/ch2/tower/narrator/ch2_tn_29.flac"
                            n "And yet you did.\n"
                            voice "audio/voices/ch2/tower/broken/ch2_broken_24.flac"
                            broken "She's so much more than us. You wouldn't understand what it feels like to be in her presence.\n"

                        "{i}• Tighten your grip.{/i}":
                            $ tower_resist_count += 1
                            $ tower_1_basement_drop_tighten = True
                            $ blade_held = False
                            $ default_mouse = "default"
                            play audio "audio/one_shot/knife_bounce_several.flac"
                            voice "audio/voices/ch2/tower/narrator/ch2_tn_30.flac"
                            n "As if on command, the blade slips from your grasp. It clatters uselessly to the floor.\n"
                            voice "audio/voices/ch2/tower/hero/ch2_th_15.flac"
                            hero "But we {i}didn't{/i} drop it. We decided to grip it tighter, remember? Are you really just going to let that happen to us?\n"
                            voice "audio/voices/ch2/tower/narrator/ch2_tn_31.flac"
                            n "I have a duty to report facts as facts, and the fact is that you dropped the blade.\n"
                            voice "audio/voices/ch2/tower/broken/ch2_broken_25.flac"
                            broken "Of course we dropped it. She's so much more than us. You wouldn't understand what it feels like to be in her presence.\n"

                    voice "audio/voices/ch2/tower/narrator/ch2_tn_32.flac"
                    n "Oh, I understand what's going on, and you'd better snap yourself out of it.\n"

                else:
                    show tower d smile talk onlayer back with dissolve
                    voice "audio/voices/ch2/tower/princess/ch2_tp_5.flac"
                    p "I see your hands are empty. You've already given up, haven't you? You aren't even going to try and kill me. How sweet.\n"
                    show tower d talk onlayer back with dissolve
                    voice "audio/voices/ch2/tower/princess/ch2_tp_5a.flac"
                    p "And more than a little disappointing.\n"
                    voice "audio/voices/ch2/tower/broken/ch2_broken_26a.flac"
                    show tower d neutral onlayer back with dissolve
                    broken "She's disappointed in us?\n"
                    #broken "She's disappointed in us? But I thought our display of weakness would show our loyalty...\n"
                    #n "Loyalty? To {i}her{/i}? You really are a lost cause.\n"
                    #voice "audio/voices/ch2/tower/narrator/ch2_tn_33a.flac"
                    #n "You really are a lost cause.\n"
                    #voice "audio/voices/ch2/tower/hero/ch2_th_16a.flac"
                    #hero "I knew we should have taken the blade...\n"

                show tower d talk onlayer back with dissolve
                voice "audio/voices/ch2/tower/princess/ch2_tp_6.flac"
                sp "Kneel.\n"
                show tower d neutral onlayer back with dissolve
                menu:
                    extend ""

                    "{i}• ''No.''{/i}":
                        $ tower_resist_count += 1
                        if tower_1_basement_drop_tighten:
                            voice "audio/voices/ch2/tower/princess/ch2_tp_7.flac"
                            show tower d smile talk onlayer back
                            p "Oh? Are you still trying to defy me? I. Said. {i}{outlinecolor=4f1313}{color=#e44646}kneel{/color}{/outlinecolor}{/i}.\n{w=5.41}{nw}"
                            show screen disableclick(0.5)
                            show tower d command onlayer back
                            voice "audio/voices/ch2/tower/princess/ch2_tp_7a.flac"
                            extend "\n{w=0.3}{nw}"
                            show screen disableclick(0.5)
                            play audio "audio/one_shot/collapse.flac"
                            show farback tower basement onlayer farback at collapse
                            show bg tower basement onlayer back at collapse
                            show flutter tower onlayer back at collapse
                            show tower d command onlayer back at collapse
                            $ renpy.pause(0.6)
                            voice "audio/voices/ch2/tower/narrator/ch2_tn_34.flac"
                            n "Your legs buckle, and your knees hit the floor.\n"
                        else:
                            play audio "audio/one_shot/collapse.flac"
                            show farback tower basement onlayer farback at collapse
                            show bg tower basement onlayer back at collapse
                            show flutter tower onlayer back at collapse
                            show tower d neutral onlayer back at collapse
                            $ renpy.pause(0.6)
                            voice "audio/voices/ch2/tower/narrator/ch2_tn_35.flac"
                            n "But the words don't leave your mouth. Instead, your legs buckle, and your knees hit the floor.\n"

                    "{i}• Kneel.{/i}":
                        $ tower_submit_count += 1
                        play audio "audio/one_shot/collapse.flac"
                        show farback tower basement onlayer farback at collapse
                        show bg tower basement onlayer back at collapse
                        show flutter tower onlayer back at collapse
                        show tower d neutral onlayer back at collapse
                        $ renpy.pause(0.6)
                        voice "audio/voices/ch2/tower/narrator/ch2_tn_36.flac"
                        n "On her command, you fall to the floor, knees painfully connecting with hard stone.\n"

                show tower d smile talk onlayer back with dissolve
                voice "audio/voices/ch2/tower/princess/ch2_tp_8.flac"
                p "That's my good little bird. Now... why don't we talk?\n"
                jump tower_1_convo_start

return
