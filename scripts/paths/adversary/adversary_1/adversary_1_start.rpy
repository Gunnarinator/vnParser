label adversary_1_start:

    # adversary variable staging
    default adversary_respawn_count = 0
    default adversary_narrator_loop = False
    default adversary_1_narrator_proof = False
    default adversary_1_chains_broken = False

    $ gallery_adversary.unlock_gallery()
    $ gallery_zch1.unlock_item(13)
    $ renpy.save_persistent()
    $ current_princess = "adversary"
    $ blade_held = False
    $ trait_stubborn = True
    $ quick_menu = False
    play sound "audio/looping/uncomfortable ambiance.ogg" loop fadein 1.0
    scene chapter adversary with fade
    show text _("{color=#FFFFFF00}Chapter Two. The Adversary.{/color}") at Position(ypos=850)
    $ renpy.pause(4.0)

    play sound "audio/looping/uncomfortable ambiance.ogg" loop
    play tertiary "audio/looping/uncomfortable ambiance heightened.ogg" loop
    play music "audio/_music/ch1/Fragmentation.flac" loop
    scene bg path onlayer farback at flip, Position(ypos=1125)
    show midground path onlayer back at flip, Position(ypos=1125)
    show front path onlayer front at flip, Position(ypos=1125)
    show bg black
    ##show loading_icon
    hide chapter
    with fade
    if persistent.quick_menu:
        $ quick_menu = True

    voice "audio/voices/ch1/woods/narrator/script_n_1.flac"
    n "You're on a path in the woods. And at the end of that path is a cabin. And in the basement of that cabin is a Princess.\n"
    voice "audio/voices/ch1/woods/narrator/script_n_2.flac"
    n "You're here to slay her.\n If you don't, it will be the end of the world.\n"
    label adversary_1_forest:
        default adversary_1_forest_count = 0
        default adversary_1_forest_share_died = False
        default adversary_1_forest_share_loop = False
        default adversary_1_forest_princess_press = False
        default adversary_1_forest_share_loop_insist = False
        default adversary_1_forest_deja_vu = False
        default adversary_1_forest_deja_vu_follow_up = False
        menu:
            extend ""

            "{i}• (Explore) I'm getting a terrible sense of deja vu.{/i}" if adversary_1_forest_share_loop == False:
                $ adversary_1_forest_deja_vu = True
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_1a.flac"
                n "A terrible sense of deja vu? No, you don't have that. This is the first time either of us have been here.\n"
                label adversary_1_forest_narrator_share_join:
                    $ adversary_1_forest_count += 1
                    $ adversary_1_forest_share_loop = True
                    voice "audio/voices/ch2/shared/hero/ch2_share_h_1.flac"
                    hero "If He doesn't remember what happened, then maybe it's best to keep it that way.\n"
                    voice "audio/voices/ch2/adversary/narrator/ch2_an_1.flac"
                    n "You know I can hear you, right? It's going to be a lot harder than you think to keep secrets from me.\n"
                    voice "audio/voices/ch2/adversary/stubborn/ch2_stubborn_1.flac"
                    stubborn "That's fine. It doesn't matter if He can hear us. The only thing that matters is marching up to that cabin and {i}winning{/i}.\n"
                    voice "audio/voices/ch2/adversary/narrator/ch2_an_2.flac"
                    n "That's the spirit. There's no point in squabbling when the real threat is just up that hill.\n"
                    #n "I'm not going to object to your rigor, but I would like to stress that I'm the closest thing you have to a guide here. We have to be able to trust each other. There's no point in squabbling when the biggest threat to all of us is waiting in the basement of that cabin.\n"
                    jump adversary_1_forest

            "{i}• (Explore) This is more than just deja vu, though. I'm pretty sure this whole thing literally just happened.{/i}" if adversary_1_forest_deja_vu and adversary_1_forest_deja_vu_follow_up == False:
                $ adversary_1_forest_deja_vu_follow_up = True
                $ adversary_1_forest_count += 1
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_1.flac"
                n "It hasn't. Or if it has, I certainly haven't been a part of it. Like I said, we've just met for the first time, you and I.\n"
                jump adversary_1_forest

            "{i}• (Explore) Wait... hasn't this already happened?{/i}" if adversary_1_forest_share_loop == False:
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_1b.flac"
                n "It hasn't. Or if it has, I certainly haven't been a part of it. We've just met for the first time, you and I.\n"
                jump adversary_1_forest_narrator_share_join

            "{i}• (Explore) Okay, no.{/i}" if adversary_1_forest_share_loop == False:
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_3a.flac"
                n "Oh, don't you start grandstanding about morals. The fate of the world is at risk right now, and the life of a mere Princess shouldn't stop you from saving us all.\n"
                jump adversary_1_forest_narrator_share_join

            "{i}• (Explore) But I died! What am I doing here?{/i}" if adversary_1_forest_share_loop == False:
                $ adversary_1_forest_share_died = True
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_4.flac"
                n "I can assure you that you're not dead. And to answer your second question, you're here to slay the Princess. I literally told you that a second ago.\n"
                jump adversary_1_forest_narrator_share_join

            "{i}• (Explore) She's going to kill me again!{/i}" if adversary_1_forest_share_loop == False:
                $ adversary_1_forest_share_died = True
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_5.flac"
                n "Again? People don't die twice. You haven't even met the Princess, and I hardly think she'd be capable of killing someone as skilled and courageous as yourself.\n"
                jump adversary_1_forest_narrator_share_join

            "{i}• (Explore) But I already slew the Princess. Sure, she {i}also{/i} killed me, but I definitely got her. Why am I here again?{/i}" if adversary_1_forest_share_loop == False:
                $ adversary_1_forest_share_died = True
                voice "audio/voices/ch2/adversary/narrator/ch2_an_3.flac"
                n "I can assure you that you didn't slay her, and that she didn't kill you. People don't just spring back to life after dying, and the two of us are meeting for the very first time.\n"
                jump adversary_1_forest_narrator_share_join

            "{i}• (Explore) Let's assume I'm telling the truth, and all of this really did already happen. Why should I listen to you? Why should I bother doing {i}anything{/i}?{/i}" if adversary_1_forest_share_loop and (adversary_1_forest_deja_vu == False or (adversary_1_forest_deja_vu_follow_up)) and adversary_1_forest_share_loop_insist == False:
                $ adversary_1_forest_share_loop_insist = True
                $ adversary_1_forest_count += 1
                $ adversary_narrator_loop = True
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_6.flac"
                n "Those are two very different questions, but fine. I'll indulge you if that's what it takes to get you moving.\n"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_7.flac"
                n "Let's say for a moment that this really is the second time you've met me, or, at least, a version of me.\n"
                if adversary_1_forest_share_died == False:
                    voice "audio/voices/ch2/shared/narrator/ch2_share_n_8.flac"
                    n "If you're back here, I'm assuming you died, which probably only happened because you didn't listen to me.\n"
                else:
                    voice "audio/voices/ch2/shared/narrator/ch2_share_n_9.flac"
                    n "You died last time, which probably only happened because you didn't listen to me.\n"
                voice "audio/voices/ch2/adversary/hero/ch2_ah_1.flac"
                hero "We did our best with the information we were given. And we {i}did{/i} kill her.\n"
                voice "audio/voices/ch2/adversary/narrator/ch2_an_4.flac"
                n "And yet you still died, didn't you? So congratulations. You've been given another chance to actually do this right.\n"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_11.flac"
                n "And I believe your other question was something along the lines of 'what's the point of doing anything?' If you're asking that, it sounds to me like you're making the rather dangerous assumption that your actions last time around didn't have any consequences.\n"
                voice "audio/voices/ch2/adversary/hero/ch2_ah_2.flac"
                hero "What do you mean? Of course there weren't any consequences. We killed the Princess, the Princess killed us, and now everyone's right back where they started. That sounds pretty consequence-free to me.\n"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_12.flac"
                n "Yes, but, in this purely hypothetical scenario, that begs the question of {i}how{/i} you got back here. Did 'time' simply rewind itself, or were you instead transported to a different world entirely?\n"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_12a.flac"
                n "Had you failed to slay the Princess, what would have happened to everyone in the place you left?\n"
                voice "audio/voices/ch2/adversary/stubborn/ch2_stubborn_2.flac"
                stubborn "Ugh. Enough with the talking! We've got a fight to win. Nothing. Else. Matters.\n"
                voice "audio/voices/ch2/adversary/narrator/ch2_an_6.flac"
                n "I couldn't agree more. The cabin, and your destined confrontation with the Princess, awaits.\n"
                jump adversary_1_forest

            "{i}• (Explore) Let's talk about this Princess...{/i}" if adversary_1_forest_share_loop_insist and adversary_1_forest_princess_press == False:
                $ adversary_1_forest_count += 1
                $ adversary_1_forest_princess_press = True
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_14.flac"
                n "Just be quick about it.\n"
                label adversary_1_forest_princess:
                    default adversary_1_forest_princess_count = 0
                    default adversary_1_forest_princess_why_strong = False
                    default adversary_1_forest_princess_basement_explain = False
                    default adversary_1_forest_princess_why_me = False
                    default adversary_1_forest_princess_cagey = False
                    default adversary_1_forest_princess_tips = False
                    menu:
                        extend ""

                        "{i}• (Explore) We killed each other last time around. How can I make sure that doesn't happen again?{/i}" if adversary_1_forest_princess_tips == False:
                            $ adversary_1_forest_princess_tips = True
                            $ adversary_1_forest_princess_count += 1
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_15.flac"
                            n "Like I said, if she killed you, it was probably because you didn't listen to me. Don't talk to her. Don't trust her. Just go in, do your job, and save the world.\n"
                            if adversary_1_forest_princess_count == 2:
                                voice "audio/voices/ch2/adversary/stubborn/ch2_stubborn_3b.flac"
                                stubborn "Oh this is {i}maddening{/i}. Why do you keep asking questions?\n" id adversary_1_forest_princess_d4d6cc5f
                                voice "audio/voices/ch2/adversary/hero/ch2_ah_3.flac"
                                hero "There's nothing wrong with getting the full picture of what's going on here.\n"
                                voice "audio/voices/ch2/adversary/stubborn/ch2_stubborn_4.flac"
                                stubborn "Sure there is. It's wasting time and energy that would be better spent fighting.\n"
                            jump adversary_1_forest_princess

                        "{i}• (Explore) All she did last time around was beat me to death. How can someone like that end the world?{/i}" if adversary_1_forest_princess_why_strong == False:
                            $ adversary_1_forest_princess_why_strong = True
                            $ adversary_1_forest_princess_count += 1
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_16a.flac"
                            n "She just can. Believe me, I wish I could tell you more, but you'll just have to trust that what I'm saying is true and that, despite it all, you're fully up to the task that's been given to you.\n"
                            if adversary_1_forest_princess_count == 2:
                                voice "audio/voices/ch2/adversary/stubborn/ch2_stubborn_3b.flac"
                                stubborn "Oh this is {i}maddening{/i}. Why do you keep asking questions?\n" id adversary_1_forest_princess_d4d6cc5f_1
                                voice "audio/voices/ch2/adversary/hero/ch2_ah_3.flac"
                                hero "There's nothing wrong with getting the full picture of what's going on here.\n"
                                voice "audio/voices/ch2/adversary/stubborn/ch2_stubborn_4.flac"
                                stubborn "Sure there is. It's wasting time and energy that would be better spent fighting.\n"
                            jump adversary_1_forest_princess

                        "{i}• (Explore) To quote you from last time around, 'she's {i}just{/i} a Princess.' Why was she strong enough to beat me to death with her bare hands?{/i}" if adversary_1_forest_princess_why_strong == False:
                            $ adversary_1_forest_princess_why_strong = True
                            $ adversary_1_forest_princess_count += 1
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_17.flac"
                            n "She {i}is{/i} just a Princess. Whatever you think happened to you last time, just get it out of your head before you get to the cabin, and you'll be {i}fine{/i}.\n"
                            if adversary_1_forest_princess_count == 2:
                                voice "audio/voices/ch2/adversary/stubborn/ch2_stubborn_3b.flac"
                                stubborn "Oh this is {i}maddening{/i}. Why do you keep asking questions?\n" id adversary_1_forest_princess_d4d6cc5f_2
                                voice "audio/voices/ch2/adversary/hero/ch2_ah_3.flac"
                                hero "There's nothing wrong with getting the full picture of what's going on here.\n"
                                voice "audio/voices/ch2/adversary/stubborn/ch2_stubborn_4.flac"
                                stubborn "Sure there is. It's wasting time and energy that would be better spent fighting.\n"
                            jump adversary_1_forest_princess

                        "{i}• (Explore) Who locked her in that basement? What {b}is{/b} this place?{/i}" if adversary_1_forest_princess_basement_explain == False:
                            $ adversary_1_forest_princess_basement_explain = True
                            $ adversary_1_forest_princess_count += 1
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_18.flac"
                            n "{i}People{/i} locked her in that basement. And I told you what this place is. It's a path in the woods. Don't overcomplicate things.\n"
                            if adversary_1_forest_princess_count == 2:
                                voice "audio/voices/ch2/adversary/stubborn/ch2_stubborn_3b.flac"
                                stubborn "Oh this is {i}maddening{/i}. Why do you keep asking questions?\n" id adversary_1_forest_princess_d4d6cc5f_3
                                voice "audio/voices/ch2/adversary/hero/ch2_ah_3.flac"
                                hero "There's nothing wrong with getting the full picture of what's going on here.\n"
                                voice "audio/voices/ch2/adversary/stubborn/ch2_stubborn_4.flac"
                                stubborn "Sure there is. It's wasting time and energy that would be better spent fighting.\n"
                            jump adversary_1_forest_princess

                        "{i}• (Explore) If people locked her away, why couldn't {b}they{/b} slay her? Why is this falling on me?{/i}" if adversary_1_forest_princess_basement_explain and adversary_1_forest_princess_why_me == False:
                            $ adversary_1_forest_princess_why_me = True
                            $ adversary_1_forest_princess_count += 1
                            if adversary_1_forest_princess_count == 2:
                                voice "audio/voices/ch2/adversary/stubborn/ch2_stubborn_3b.flac"
                                stubborn "Oh this is {i}maddening{/i}. Why do you keep asking questions?\n" id adversary_1_forest_princess_d4d6cc5f_4
                                voice "audio/voices/ch2/adversary/hero/ch2_ah_3.flac"
                                hero "There's nothing wrong with getting the full picture of what's going on here.\n"
                                voice "audio/voices/ch2/adversary/stubborn/ch2_stubborn_4.flac"
                                stubborn "Sure there is. It's wasting time and energy that would be better spent fighting.\n"
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_19.flac"
                            n "Look, I'm not supposed to say this, but it's because you're special. You're the {i}only{/i} person capable of doing this. Call it a prophecy if that helps, but it's just the way things are.\n"
                            voice "audio/voices/ch2/shared/hero/ch2_share_h_2.flac"
                            hero "Oh. I didn't know we were {i}special{/i}.\n"
                            voice "audio/voices/ch2/adversary/stubborn/ch2_stubborn_5.flac"
                            stubborn "Yeah, I like the sound of that.\n"
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_20a.flac"
                            n "Of course you're special. Why else would you be here?\n"
                            jump adversary_1_forest_princess

                        "{i}• (Explore) You're being cagey. What aren't you telling me?{/i}" if adversary_1_forest_princess_cagey == False and adversary_1_forest_princess_count > 1:
                            $ adversary_1_forest_princess_cagey = True
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_21.flac"
                            n "I've told you everything you need to know, going into more detail would just overcomplicate an otherwise very simple situation and make your job more difficult.\n"
                            voice "audio/voices/ch2/adversary/stubborn/ch2_stubborn_6.flac"
                            stubborn "What else would we even {i}need{/i} to know? We've got all the reason we need for a rematch.\n"
                            voice "audio/voices/ch2/adversary/narrator/ch2_an_7.flac"
                            n "Exactly. The less you know about her, the better.\n"
                            jump adversary_1_forest_princess

                        "{i}• Nevermind.{/i}" if adversary_1_forest_princess_count == 0:
                            label adversary_1_forest_princess_leaving:
                                voice "audio/voices/ch2/shared/narrator/ch2_share_n_24.flac"
                                n "Great. Now if you don't mind, the whole world is waiting with bated breath for you to save it from ruin.\n"
                                jump adversary_1_forest

                        "{i}• That's all.{/i}" if adversary_1_forest_princess_count != 0:
                            jump adversary_1_forest_princess_leaving

            "{i}• [[Proceed to the cabin.]{/i}":
                jump adversary_1_cabin_arrival

            "{i}• [[Turn around and leave.]{/i}" if mound_can_attempt_flee:
                if loops_finished >= 2:
                    $ mound_can_attempt_flee = False
                    voice "audio/voices/mound/bonus/flee.flac"
                    mound "You have already committed to my completion. You cannot go further astray.\n"
                    jump adversary_1_forest
                voice "audio/voices/ch2/adversary/stubborn/ch2_stubborn_7.flac"
                stubborn "We can't just leave, we're supposed to fight her! Where are you going?\n"
                jump turn_and_leave_join

label adversary_1_cabin_arrival:
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
    voice "audio/voices/ch2/adversary/stubborn/ch2_stubborn_8a.flac"
    stubborn "'Lying' and 'cheating' doesn't sound like her at all. Not that it matters, it's not like she can lie or cheat in the middle of a fight.\n"
    voice "audio/voices/ch2/adversary/hero/ch2_ah_4.flac"
    hero "Are you sure about that?\n"
    voice "audio/voices/ch2/adversary/narrator/ch2_an_8.flac"
    n "The point of my warning wasn't to start an argument over what circumstances the Princess is capable of lying in. It was to give you some broadly applicable advice.\n"
    voice "audio/voices/ch2/adversary/narrator/ch2_an_8a.flac"
    n "The Princess will do and say whatever she thinks it will take to get her out of there. So don't trust her. Ever. Are we clear?\n"
    #n "Just be careful and make sure you stay {i}focused{/i}.\n"
    voice "audio/voices/ch2/adversary/stubborn/ch2_stubborn_8b.flac"
    stubborn "Crystal. Let's just get on with it already.\n"
    menu:
        extend ""

        "{i}• [[Proceed into the cabin.]{/i}":
            label adversary_stranger_rejoin:
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

    $ gallery_adversary.unlock_item(1)
    $ renpy.save_persistent()
    play music "audio/_music/ch2/adversary/The Adversary.flac" loop
    play sound "audio/looping/STP_cave_loop.ogg" loop fadein 1.0
    scene farback adversary cabin onlayer farback at Position(ypos=1125)
    show bg adversary cabin onlayer back at Position(ypos=1125)
    show door adversary1 onlayer back at Position(ypos=1125)
    show table adversary onlayer back at Position(ypos=1125)
    show knife adversary onlayer back at Position(ypos=1125)
    show mirror adversary onlayer back at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    voice "audio/voices/ch2/adversary/narrator/ch2_an_9.flac"
    n "The cabin is tighter than its exterior would suggest. Its cold stone walls press in on you, as if trying to forcefully direct you towards your destination. The only furniture of note is a black-iron altar with a pristine blade perched on its edge.\n"
    if adversary_1_forest_count >= 2 or adversary_1_forest_princess_count >= 2:
        voice "audio/voices/ch2/adversary/stubborn/ch2_stubborn_9.flac"
        stubborn "See? Even the cabin has the right idea. Let's get moving.\n"
    voice "audio/voices/ch2/shared/narrator/ch2_share_n_25.flac"
    n "The blade is your implement. You'll need it if you want to do this right.\n"
    label cabin_interior_2_adversary_menu:
        default adversary_1_cabin_mirror_present = True
        default adversary_1_cabin_blade_taken = False
        default adversary_1_cabin_mirror_ask = False
        default adversary_1_cabin_mirror_approached = False
        default adversary_1_cabin_last_time_comment = False
        menu:
            extend ""

            "{i}• (Explore) You didn't say anything about the mirror on the wall.{/i}" if adversary_1_cabin_mirror_ask == False and adversary_1_cabin_mirror_present:
                $ adversary_1_cabin_mirror_ask = True
                $ current_run_mirror_comment = True
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_39.flac"
                n "That's because there isn't a mirror. There's the altar, the blade sitting on the altar, and the door to the basement. There's nothing else in here.\n"
                voice "audio/voices/ch2/shared/hero/ch2_share_h_4.flac"
                hero "There's definitely a mirror.\n"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_27.flac"
                n "There isn't.\n"
                if adversary_1_forest_count >= 2 or adversary_1_forest_princess_count >= 2:
                    voice "audio/voices/ch2/adversary/stubborn/ch2_stubborn_10.flac"
                    stubborn "You already wasted {i}so{/i} much time in the woods! Who even cares if there's a mirror?\n"
                else:
                    voice "audio/voices/ch2/adversary/stubborn/ch2_stubborn_11.flac"
                    stubborn "Oh, stop bickering and just get on with it. Who even cares if there's a mirror?\n"
                menu:
                    extend ""

                    "{i}• I care about whether I'm being lied to.{/i}":
                        voice "audio/voices/ch2/adversary/hero/ch2_ah_5.flac"
                        hero "As do I.\n"
                        #n "I'm not lying to you, I {i}promise{/i}. There isn't a mirror. Really.\n"
                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_30.flac"
                        n "I'm not lying to you. Use your eyes, there is no mirror. Why would I lie about something so meaningless? What good would a mirror even do? Let you waste time preening yourself instead of doing what needs to be done?\n"

                    "{i}• I care. I want to look at myself. I want to see how {b}handsome{/b} I am.{/i}":
                        voice "audio/voices/ch2/adversary/hero/ch2_ah_6.flac"
                        hero "I care less about that and more about whether we're being lied to. If He's willing to lie about something as innocuous as a mirror, what else is He hiding from us?\n"
                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_29.flac"
                        n "I'm not lying to you. Use your eyes, there is no mirror. Why would I lie about something so meaningless? What good would it even do?\n"

                    "{i}• You're right. It doesn't matter.{/i}":
                        $ adversary_1_cabin_mirror_present = False
                        voice "audio/voices/ch2/shared/hero/ch2_share_h_5.flac"
                        hero "But it {i}does{/i} matter! Don't you care if we're being lied to? If He's willing to lie about something as innocuous as a mirror, what else is He hiding from us?\n"
                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_30.flac"
                        hide mirror onlayer back
                        n "I'm not lying to you. Use your eyes, there is no mirror. Why would I lie about something so meaningless? What good would a mirror even do? Let you waste time preening yourself instead of doing what needs to be done?\n"
                        # da mirror friggen skinamarinks
                        voice "audio/voices/ch2/shared/hero/ch2_share_h_6.flac"
                        hero "But there {i}was{/i} a mirror a second ago.\n"
                        voice "audio/voices/ch2/adversary/stubborn/ch2_stubborn_13.flac"
                        stubborn "And now it's gone, so all of us can stop arguing about it and get to fightin'.\n"

                    "{i}• [[Remain silent.]{/i}":
                        voice "audio/voices/ch2/shared/hero/ch2_share_h_7a.flac"
                        hero "I care about whether we're being lied to. If He's willing to lie about something as innocuous as a mirror, what else is He hiding from us?\n"
                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_31.flac"
                        n "I'm not lying to you, I {i}promise{/i}. There isn't a mirror. Really.\n"

                    "{i}• [[Approach the mirror.]{/i}" if adversary_1_cabin_mirror_approached == False:
                        label adversary_cabin_1_mirror_join:
                            $ current_run_mirror_touched = True
                            play audio "audio/one_shot/footsteps_stone.flac"
                            hide farback onlayer farback
                            hide bg onlayer back
                            hide door onlayer back
                            hide table onlayer back
                            hide knife onlayer back
                            hide mirror onlayer back
                            scene bg adversary mirror onlayer front at Position(ypos=1125)
                            show mirror adversary close onlayer front at Position(ypos=1125)
                            with dissolve
                            $ adversary_1_cabin_mirror_approached = True
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_32.flac"
                            n "You walk up to the wall next to the basement door. It's a wall. There isn't much to see here.\n"
                            if adversary_1_cabin_mirror_ask == False:
                                voice "audio/voices/ch2/shared/hero/ch2_share_h_8.flac"
                                hero "What are you talking about? This isn't a wall. It's a mirror. Or at least it'll {i}be{/i} a mirror once we wipe off that layer of grime.\n"
                            else:
                                voice "audio/voices/ch2/shared/hero/ch2_share_h_9.flac"
                                hero "This really isn't funny.\n"
                            menu:
                                extend ""

                                "{i}• [[Wipe the mirror clean.]{/i}":
                                    $ adversary_1_cabin_mirror_present = False
                                    hide mirror onlayer front
                                    play audio "audio/one_shot/new/STP_claws_1.flac"
                                    show player wall onlayer front at Position(ypos=1125) with dissolve
                                    if adversary_1_cabin_mirror_ask == False:
                                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_33.flac"
                                    else:
                                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_33a.flac"
                                    n "You reach forward and rub your hand against the cabin wall. I hope you know how ridiculous you look right now.\n"
                                    hide player onlayer front with dissolve
                                    if adversary_1_cabin_mirror_ask:
                                        voice "audio/voices/ch2/shared/hero/ch2_share_h_10.flac"
                                        hero "But it was there a second ago!\n"
                                    else:
                                        voice "audio/voices/ch2/shared/hero/ch2_share_h_6.flac"
                                        hero "But there was a mirror a second ago.\n"
                                    voice "audio/voices/ch2/adversary/stubborn/ch2_stubborn_13.flac"
                                    stubborn "And now it's gone. So all of us can stop arguing about it and get to fightin'.\n"
                                    play audio "audio/one_shot/footsteps_stone.flac"
                                    hide bg onlayer front
                                    scene farback adversary cabin onlayer farback at Position(ypos=1125)
                                    show bg adversary cabin onlayer back at Position(ypos=1125)
                                    show door adversary1 onlayer back at Position(ypos=1125)
                                    show table adversary onlayer back at Position(ypos=1125)
                                    if adversary_1_cabin_blade_taken == False:
                                        show knife adversary onlayer back at Position(ypos=1125)
                                    with dissolve
                                    jump cabin_interior_2_adversary_menu

                jump cabin_interior_2_adversary_menu

            "{i}• (Explore) This whole cabin is different than last time.{/i}" if adversary_1_cabin_last_time_comment == False and adversary_1_forest_share_loop_insist:
                $ adversary_1_cabin_last_time_comment = True
                voice "audio/voices/ch2/shared/hero/ch2_share_h_11.flac"
                hero "{i}Very{/i} different.\n"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_34.flac"
                n "Maybe that's because you haven't actually been here. I hope this means you'll finally drop that ridiculous past-life nonsense. You haven't died, and you certainly haven't been killed by the Princess.\n"
                voice "audio/voices/ch2/adversary/narrator/ch2_an_10.flac"
                n "So focus up. The world is depending on you.\n"
                jump cabin_interior_2_adversary_menu

            "{i}• (Explore) [[Approach the mirror.]{/i}" if adversary_1_cabin_mirror_present and adversary_1_cabin_mirror_approached == False:
                $ adversary_1_cabin_mirror_approached = True
                jump adversary_cabin_1_mirror_join

            "{i}• (Explore) [[Take the blade.]{/i}" if adversary_1_cabin_blade_taken == False:
                $ adversary_1_cabin_blade_taken = True
                $ blade_held = True
                $ default_mouse = "blade"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_38.flac"
                play audio "audio/one_shot/knife_pickup.flac"
                hide knife onlayer back
                with dissolve
                n "You take the blade from the altar. It would be difficult to slay the Princess and save the world without a weapon.\n"
                jump cabin_interior_2_adversary_menu

            "{i}• [[Enter the basement.]{/i}":
                if adversary_1_cabin_blade_taken == False:
                    voice "audio/voices/ch2/adversary/stubborn/ch2_stubborn_14.flac"
                    stubborn "No blade this time? Right then, fisticuffs it is. Probably more fair to her anyway. Wouldn't want to feel like we cheated our way to a win.\n"
                    voice "audio/voices/ch2/adversary/narrator/ch2_an_11.flac"
                    n "As long as you can still get the job done... and don't forget that the blade is waiting for you upstairs if you happen to change your mind.\n"

                $ quick_menu = False
                play audio "audio/one_shot/door_stone.flac"
                hide mirror onlayer back
                show door adversary2 onlayer back at Position(ypos=1125) with Dissolve(1.0)
                show door adversary3 onlayer back at Position(ypos=1125) with Dissolve(1.5)
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
                voice "audio/voices/ch2/adversary/narrator/ch2_an_12.flac"
                scene bg adversary stairs onlayer back at Position(ypos=1125)
                with fade
                if persistent.quick_menu:
                    $ quick_menu = True
                n "The door to the basement creaks open, revealing a rough stone staircase, its walls pressing at your sides and tightening as you descend. The air seeping from below is heavy and oppressive, with an almost sulfuric odor to it. If the Princess lives here, slaying her would probably be doing her a favor.\n"
                voice "audio/voices/ch2/adversary/narrator/ch2_an_13.flac"
                n "Her fierce voice carries up the stairs.\n"
                voice "audio/voices/ch2/adversary/princess/ch2_ap_1.flac"
                sp "Is that another challenger? {i}Finally{/i}. It's been ages since I've had a good fight.\n"
                voice "audio/voices/ch2/adversary/hero/ch2_ah_8.flac"
                hero "This isn't what she sounded like last time. Her voice is a little deeper, almost threatening.\n"
                voice "audio/voices/ch2/adversary/stubborn/ch2_stubborn_15.flac"
                stubborn "Good. Sounds like my kind of Princess.\n"
                voice "audio/voices/ch2/adversary/narrator/ch2_an_14.flac"
                n "As much as I appreciate the enthusiasm, just make sure you don't let your bloodlust get to your head. You need to stay focused and keep your wits about you. Remember you're here to {i}slay{/i} the Princess, not to have a good fight.\n"
                # continue down the stairs
                $ gallery_adversary.unlock_item(2)
                $ renpy.save_persistent()
                play audio "audio/one_shot/footsteps_stone.flac"
                $ quick_menu = False
                hide bg onlayer back
                with fade
                scene farback adversary basement onlayer farback at Position(ypos=1125)
                show bg adversary basement onlayer back at Position(ypos=1125)
                show adversary d glare onlayer back at Position(ypos=1125)
                with fade
                if persistent.quick_menu:
                    $ quick_menu = True
                voice "audio/voices/ch2/adversary/narrator/ch2_an_15.flac"
                n "As you descend the final step, the form of the Princess comes into view, a large shackle leading from her wrist to the basement wall.\n"
                #if adversary_1_forest_share_loop_insist:
                #    voice "audio/voices/ch2/adversary/hero/ch2_ah_9.flac"
                #    hero "Is it just me, or does she look... stronger than she used to? It looks like she could rip those chains out of the wall without a second thought.\n"
                #    voice "audio/voices/ch2/adversary/stubborn/ch2_stubborn_16.flac"
                #    stubborn "But this time we're ready for her.\n"
                #else:
                voice "audio/voices/ch2/adversary/hero/ch2_ah_9a.flac"
                hero "It looks like she could rip those chains out of the wall without a second thought.\n"
                voice "audio/voices/ch2/adversary/princess/ch2_ap_2.flac"
                show adversary d talk2 onlayer back at Position(ypos=1125) with dissolve
                sp "Oh, it's you again. I've been hoping you'd find your way back here. Good to see that death doesn't stick for either of us.\n"
                if adversary_1_cabin_blade_taken:
                    voice "audio/voices/ch2/adversary/princess/ch2_ap_3.flac"
                    show adversary d neutral onlayer back at Position(ypos=1125) with dissolve
                    sp "And you brought your little knife, too. {i}Yes{/i}.\n"
                    # she smiles
                    #stop music fadeout 1.0
                    voice "audio/voices/ch2/adversary/princess/ch2_ap_4.flac"
                    show adversary d talk2 onlayer back at Position(ypos=1125) with dissolve
                    sp "I'm going to have fun breaking you into little pieces.\n"
                    show adversary d neutral onlayer back
                else:
                    voice "audio/voices/ch2/adversary/princess/ch2_ap_5.flac"
                    show adversary d talk2 onlayer back at Position(ypos=1125) with dissolve
                    sp "But no little knife this time, huh?\n"
                    #stop music fadeout 1.0
                    voice "audio/voices/ch2/adversary/princess/ch2_ap_6.flac"
                    show adversary d talk onlayer back at Position(ypos=1125) with dissolve
                    sp "Ugh. I hope you're not just here to 'chat.' I've been itching for a rematch.\n"
                    show adversary d bored onlayer back
                jump adversary_1_distant_chat

                #$ quick_menu = False
                #play music "audio/music/Hit.ogg" noloop
                #hide adversary onlayer back
                #hide farback onlayer farback
                #hide bg onlayer back
                #show bg generic onlayer farback at Position(ypos=1125)
                #show card adversary onlayer back at Position(ypos=1125)
                #$ renpy.pause(1.0)
                #play audio "audio/one_shot/glass_1.flac"
                #$ renpy.pause(0.5)
                #show shard adversary onlayer front at Position(ypos=1125) with hpunch
                # bring her BACK





return
