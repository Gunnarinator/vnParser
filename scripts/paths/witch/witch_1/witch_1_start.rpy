label witch_1_start:
    $ blade_held = False
    $ trait_opportunist = True
    $ quick_menu = False
    play sound "audio/looping/uncomfortable ambiance.ogg" loop fadein 1.0
    scene chapter witch with fade
    show text _("{color=#FFFFFF00}Chapter 2. The Witch.{/color}") at Position(ypos=850)
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
    $ gallery_witch.unlock_gallery()
    $ gallery_zch1.unlock_item(11)
    $ renpy.save_persistent()
    voice "audio/voices/ch1/woods/narrator/script_n_1.flac"
    n "You're on a path in the woods. And at the end of that path is a cabin. And in the basement of that cabin is a Princess.\n"
    voice "audio/voices/ch1/woods/narrator/script_n_2.flac"
    n "You're here to slay her.\n If you don't, it will be the end of the world.\n"
    label witch_1_forest:
        default witch_1_forest_count = 0
        default witch_1_forest_share_died = False
        default witch_1_forest_share_loop = False
        default witch_1_forest_princess_press = False
        default witch_1_forest_share_loop_insist = False
        default witch_1_forest_deja_vu = False
        default witch_1_forest_deja_vu_follow_up = False
        menu:
            extend ""

            "{i}• (Explore) I'm getting a terrible sense of deja vu.{/i}" if witch_1_forest_share_loop == False:
                $ witch_1_forest_deja_vu = True
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_1a.flac"
                n "A terrible sense of deja vu? No, you don't have that. This is the first time either of us have been here.\n"
                label witch_1_forest_narrator_share_join:
                    $ witch_1_forest_count += 1
                    $ witch_1_forest_share_loop = True
                    voice "audio/voices/ch2/shared/hero/ch2_share_h_1.flac"
                    hero "If He doesn't remember what happened, then maybe it's best to keep it that way.\n"
                    voice "audio/voices/ch2/witch/opportunist/ch2_opportunist_1.flac"
                    opportunist "Brilliant. We need to keep our cards close to our chest, and I'm not sure we can trust {i}Him{/i}.\n"
                    voice "audio/voices/ch2/witch/narrator/ch2_wn_1.flac"
                    n "You know I can hear you, right? It's going to be a lot harder than you think to keep secrets from me.\n"
                    voice "audio/voices/ch2/witch/opportunist/ch2_opportunist_2.flac"
                    opportunist "Did I say 'I'm not sure we can trust {i}Him{/i}?' Slip of the tongue. Bit of the old brain fog. I meant to say that we should probably head over to the cabin and slay that Princess. We already know we can't trust {i}her{/i}, so let's get on with the show.\n" id witch_1_forest_narrator_share_join_8669dc93
                    jump witch_1_forest

            "{i}• (Explore) This is more than just deja vu, though. I'm pretty sure this whole thing literally just happened.{/i}" if witch_1_forest_deja_vu and witch_1_forest_deja_vu_follow_up == False:
                $ witch_1_forest_deja_vu_follow_up = True
                $ witch_1_forest_count += 1
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_2.flac"
                n "We could go back and forth on this forever, and it won't get you any closer to doing your job and saving the world. So let's just agree to disagree.\n"
                jump witch_1_forest

            "{i}• (Explore) Wait... hasn't this already happened?{/i}" if witch_1_forest_share_loop == False:
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_1b.flac"
                n "It hasn't. Or if it has, I certainly haven't been a part of it. We've just met for the first time, you and I.\n"
                jump witch_1_forest_narrator_share_join

            "{i}• (Explore) Okay, no.{/i}" if witch_1_forest_share_loop == False:
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_3a.flac"
                n "Oh, don't you start grandstanding about morals. The fate of the world is at risk right now, and the life of a mere Princess shouldn't stop you from saving us all.\n"
                jump witch_1_forest_narrator_share_join

            "{i}• (Explore) But I died! What am I doing here?{/i}" if witch_1_forest_share_loop == False:
                $ witch_1_forest_share_died = True
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_4.flac"
                n "I can assure you that you're not dead. And to answer your second question, you're here to slay the Princess. I literally told you that a second ago.\n"
                jump witch_1_forest_narrator_share_join

            "{i}• (Explore) She's going to kill me again!{/i}" if witch_1_forest_share_loop == False and loop_1_locked == False:
                $ witch_1_forest_share_died = True
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_5.flac"
                n "Again? People don't die twice. You haven't even met the Princess, and I hardly think she'd be capable of killing someone as skilled and courageous as yourself.\n"
                jump witch_1_forest_narrator_share_join

            "{i}• (Explore) But I already slew the Princess. Sure, she {i}also{/i} killed me, but I definitely got her. Why am I here again?{/i}" if witch_1_forest_share_loop == False and loop_1_locked == False:
                $ witch_1_forest_share_died = True
                voice "audio/voices/ch2/witch/narrator/ch2_wn_3.flac"
                n "I can assure you that you didn't slay her, and that she didn't kill you. People don't just spring back to life after dying, and the two of us are meeting for the very first time.\n"
                jump witch_1_forest_narrator_share_join

            "{i}• (Explore) Let's assume I'm telling the truth, and all of this really did already happen. Why should I listen to you? Why should I bother doing {i}anything{/i}?{/i}" if witch_1_forest_share_loop and (witch_1_forest_deja_vu == False or (witch_1_forest_deja_vu_follow_up)) and witch_1_forest_share_loop_insist == False:
                $ witch_1_forest_share_loop_insist = True
                $ witch_1_forest_count += 1
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_6.flac"
                n "Those are two very different questions, but fine. I'll indulge you if that's what it takes to get you moving.\n"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_7.flac"
                n "Let's say for a moment that this really is the second time you've met me, or, at least, a version of me.\n"
                if witch_1_forest_share_died == False:
                    voice "audio/voices/ch2/shared/narrator/ch2_share_n_8.flac"
                    n "If you're back here, I'm assuming you died, which probably only happened because you didn't listen to me.\n"
                else:
                    voice "audio/voices/ch2/shared/narrator/ch2_share_n_9.flac"
                    n "You died last time, which probably only happened because you didn't listen to me.\n"
                voice "audio/voices/ch2/witch/opportunist/ch2_opportunist_3.flac"
                opportunist "We were just weighing our options in a morally ambiguous situation. You can't blame us for weighing our options.\n"
                if current_mutual_death > 0:
                    voice "audio/voices/ch2/adversary/hero/ch2_ah_1.flac"
                    hero "We did our best with the information we were given. And we {i}did{/i} kill her.\n"
                    voice "audio/voices/ch2/adversary/narrator/ch2_an_4.flac"
                    n "And yet you still died, didn't you? So congratulations. You've been given another chance to actually do this right.\n"
                else:
                    voice "audio/voices/ch2/witch/narrator/ch2_wn_4.flac"
                    n "I can if you failed to slay the Princess, which you apparently did. So, great. Congratulations. You've been given another chance to actually do this right.\n"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_11.flac"
                n "And I believe your other question was something along the lines of 'what's the point of doing anything?' If you're asking that, it sounds to me like you're making the rather dangerous assumption that your actions last time around didn't have any consequences.\n"
                if current_mutual_death > 0:
                    voice "audio/voices/ch2/witch/hero/ch2_wh_1.flac"
                    hero "What do you mean? Of course there weren't any consequences. We killed the Princess, the Princess killed us, and now everyone's right back where they started. That sounds pretty consequence-free to me.\n"
                elif loop_1_locked:
                    voice "audio/voices/ch2/witch/hero/ch2_wh_2.flac"
                    hero "What do you mean? Of course there weren't any consequences. The Princess locked us in the basement, we eventually died, and now everyone's right back where they started. That sounds pretty consequence-free to me.\n"
                else:
                    voice "audio/voices/ch2/witch/hero/ch2_wh_3.flac"
                    hero "What do you mean? Of course there weren't any consequences. We were killed by the Princess, and now everyone's right back where they started. That sounds pretty consequence-free to me.\n"
                if current_mutual_death > 0:
                    voice "audio/voices/ch2/shared/narrator/ch2_share_n_12.flac"
                    n "Yes, but, in this purely hypothetical scenario, that begs the question of {i}how{/i} you got back here. Did 'time' simply rewind itself, or were you instead transported to a different world entirely?\n"
                    voice "audio/voices/ch2/shared/narrator/ch2_share_n_12a.flac"
                    n "Had you failed to slay the Princess, what would have happened to everyone in the place you left?\n"
                else:
                    voice "audio/voices/ch2/shared/narrator/ch2_share_n_12.flac"
                    n "Yes, but, in this purely hypothetical scenario, that begs the question of {i}how{/i} you got back here. Did 'time' simply rewind itself, or were you instead transported to a different world entirely?\n"
                    voice "audio/voices/ch2/shared/narrator/ch2_share_n_13.flac"
                    n "If it's the latter, what do you think happened {i}after{/i} you died?\n"
                    voice "audio/voices/ch2/shared/narrator/ch2_share_n_13a.flac"
                    n "Do you think the people there lived happily ever after, or do you think that the Princess, left unhindered, brought about the end to everyone and everything, just like I told you she would?\n"
                voice "audio/voices/ch2/witch/opportunist/ch2_opportunist_4.flac"
                opportunist "That's a very good point. This Princess character seems like a lot of trouble. And if you think about it, actually slaying her probably breaks us out of this cycle, right? We don't want to be stuck here forever, do we?\n"
                voice "audio/voices/ch2/witch/hero/ch2_wh_4.flac"
                hero "You're laying it on a little thick, aren't you?\n"
                voice "audio/voices/ch2/witch/opportunist/ch2_opportunist_5.flac"
                opportunist "Laying it on a little thick? What are you talking about? I'm sharing my honest opinions.\n"
                voice "audio/voices/ch2/witch/narrator/ch2_wn_5.flac"
                n "What matters is that almost everyone seems to be on the same page. So whenever you're ready, you can stop dawdling, get to the cabin, and save the world.\n"
                jump witch_1_forest

            "{i}• (Explore) Let's talk about this Princess...{/i}" if witch_1_forest_share_loop_insist and witch_1_forest_princess_press == False:
                $ witch_1_forest_count += 1
                $ witch_1_forest_princess_press = True
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_14.flac"
                n "Just be quick about it.\n"
                label witch_1_forest_princess:
                    default witch_1_forest_princess_count = 0
                    default witch_1_forest_princess_why_strong = False
                    default witch_1_forest_princess_basement_explain = False
                    default witch_1_forest_princess_why_me = False
                    default witch_1_forest_princess_cagey = False
                    default witch_1_forest_princess_tips = False
                    menu:
                        extend ""

                        "{i}• (Explore) She killed me last time around. How can I make sure that doesn't happen again?{/i}" if witch_1_forest_princess_tips == False:
                            $ witch_1_forest_princess_tips = True
                            $ witch_1_forest_princess_count += 1
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_15.flac"
                            n "Like I said, if she killed you, it was probably because you didn't listen to me. Don't talk to her. Don't trust her. Just go in, do your job, and save the world.\n"
                            jump witch_1_forest_princess

                        "{i}• (Explore) She killed me by ripping me to pieces. Don't get me wrong, I hated it, but how can someone like that end the world?{/i}" if witch_1_forest_princess_why_strong == False and loop_1_locked == False:
                            $ witch_1_forest_princess_why_strong = True
                            $ witch_1_forest_princess_count += 1
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_16a.flac"
                            n "She just can. Believe me, I wish I could tell you more, but you'll just have to trust that what I'm saying is true and that, despite it all, you're fully up to the task that's been given to you.\n"
                            jump witch_1_forest_princess

                        "{i}• (Explore) All she did last time was lock me in a basement until I died. Don't get me wrong, I hated it, but how can someone like that end the world?{/i}" if witch_1_forest_princess_why_strong == False and loop_1_locked:
                            $ witch_1_forest_princess_why_strong = True
                            $ witch_1_forest_princess_count += 1
                            voice "audio/voices/ch2/witch/narrator/ch2_wn_7.flac"
                            n "She just can. But that doesn't mean you're not fully up to the task that's been given to you. Have a little faith in yourself, and maybe try to not get tricked this time.\n"
                            jump witch_1_forest_princess

                        "{i}• (Explore) To quote you from last time around, 'she's {i}just{/i} a Princess.' Why was she able to rip me apart with her bare hands?{/i}" if witch_1_forest_princess_why_strong == False and loop_1_locked == False:
                            $ witch_1_forest_princess_why_strong = True
                            $ witch_1_forest_princess_count += 1
                            #voice "audio/voices/ch2/shared/narrator/ch2_share_n_17.flac"
                            voice "audio/voices/ch2/witch/narrator/ch2_wn_8.flac"
                            n "She {i}is{/i} just a Princess. Whatever you think happened to you last time, just get it out of your head before you get to the cabin, and you'll be {i}fine{/i}.\n"
                            jump witch_1_forest_princess

                        "{i}• (Explore) Who locked her in that basement? What {b}is{/b} this place?{/i}" if witch_1_forest_princess_basement_explain == False:
                            $ witch_1_forest_princess_basement_explain = True
                            $ witch_1_forest_princess_count += 1
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_18.flac"
                            n "{i}People{/i} locked her in that basement. And I told you what this place is. It's a path in the woods. Don't overcomplicate things.\n"
                            jump witch_1_forest_princess

                        "{i}• (Explore) If people locked her away, why couldn't {b}they{/b} slay her? Why is this falling on me?{/i}" if witch_1_forest_princess_basement_explain and witch_1_forest_princess_why_me == False:
                            $ witch_1_forest_princess_why_me = True
                            $ witch_1_forest_princess_count += 1
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_19.flac"
                            n "Look, I'm not supposed to say this but it's because you're special. You're the {i}only{/i} person capable of doing this. Call it a prophecy if that helps, but it's just the way things are.\n"
                            voice "audio/voices/ch2/shared/hero/ch2_share_h_2.flac"
                            hero "Oh. I didn't know we were {i}special{/i}.\n"
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_20a.flac"
                            n "Of course you're special. Why else would you be here?\n"
                            voice "audio/voices/ch2/witch/opportunist/ch2_opportunist_6.flac"
                            opportunist "Good point. That really explains almost everything.\n"
                            voice "audio/voices/ch2/witch/hero/ch2_wh_5.flac"
                            hero "I'm not so sure about {i}that{/i}.\n"
                            voice "audio/voices/ch2/witch/opportunist/ch2_opportunist_7.flac"
                            opportunist "You know, you're right. But it explains {i}almost{/i} everything.\n"
                            jump witch_1_forest_princess

                        "{i}• (Explore) You're being cagey. What aren't you telling me?{/i}" if witch_1_forest_princess_cagey == False and witch_1_forest_princess_count > 1:
                            $ witch_1_forest_princess_cagey = True
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_21.flac"
                            n "I've told you everything you need to know, going into more detail would just overcomplicate an otherwise very simple situation and make your job more difficult.\n"
                            if loop_1_locked == False:
                                voice "audio/voices/ch2/witch/hero/ch2_wh_6a.flac"
                                hero "If you want us to stand a chance against her, we need to be armed with information. What is she really capable of? How are we supposed to stop her?\n"
                            if witch_1_forest_princess_count < 2:
                                voice "audio/voices/ch2/shared/narrator/ch2_share_n_22.flac"
                                n "The less you know about her, the better.\n"
                            else:
                                voice "audio/voices/ch2/shared/narrator/ch2_share_n_23.flac"
                                n "Not to sound like a broken record, but the less you know about her, the better things will go for all of us. I know it sounds like I'm hiding something, but you're just going to have to take me at my word.\n"
                            voice "audio/voices/ch2/witch/opportunist/ch2_opportunist_8.flac"
                            opportunist "I don't think either of you really need to press the man on this. He wants us to slay the Princess, so why would He have anything to hide? He seems like a nice guy to me!\n"
                            voice "audio/voices/ch2/witch/narrator/ch2_wn_9.flac"
                            n "I appreciate the vote of confidence, but you should really stop wasting time chatting amongst yourselves in the woods, so if we could move this along...\n"
                            jump witch_1_forest_princess

                        "{i}• Nevermind.{/i}" if witch_1_forest_princess_count == 0:
                            label witch_1_forest_princess_leaving:
                                voice "audio/voices/ch2/shared/narrator/ch2_share_n_24.flac"
                                n "Great. Now if you don't mind, the whole world is waiting with bated breath for you to save it from ruin.\n"
                                jump witch_1_forest

                        "{i}• That's all.{/i}" if witch_1_forest_princess_count != 0:
                            jump witch_1_forest_princess_leaving

            "{i}• [[Proceed to the cabin.]{/i}":
                jump witch_1_cabin_arrival

            "{i}• [[Turn around and leave.]{/i}" if mound_can_attempt_flee:
                if loops_finished >= 2:
                    $ mound_can_attempt_flee = False
                    voice "audio/voices/mound/bonus/flee.flac"
                    mound "You have already committed to my completion. You cannot go further astray.\n"
                    jump witch_1_forest
                voice "audio/voices/ch2/witch/opportunist/ch2_opportunist_9.flac"
                opportunist "Well, you're the boss.\n"
                jump turn_and_leave_join

label witch_1_cabin_arrival:
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
    if witch_1_forest_share_loop_insist:
        voice "audio/voices/ch2/witch/opportunist/ch2_opportunist_10.flac"
        opportunist "Don't worry. I think we've taken that lesson to heart at this point. You can trust us to get the job done.\n"
    else:
        voice "audio/voices/ch2/witch/opportunist/ch2_opportunist_11.flac"
        opportunist "Don't worry. You can trust us to get the job done.\n"
    menu:
        extend ""

        "{i}• [[Proceed into the cabin.]{/i}":
            label witch_stranger_rejoin:
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

    $ gallery_witch.unlock_item(1)
    $ renpy.save_persistent()
    play sound "audio/looping/ambient_cabin.ogg" loop fadein 1.0
    play secondary "audio/looping/uncomfortable ambiance heightened.ogg" loop
    play music "audio/_music/ch2/witch/The Witch.flac" loop
    scene farback witch cabin onlayer farback at Position(ypos=1125)
    show bg witch cabin onlayer back at Position(ypos=1125)
    show door witch1 onlayer back at Position(ypos=1125)
    show table witch onlayer back at Position(ypos=1125)
    show knife witch onlayer back at Position(ypos=1125)
    show mirror base onlayer back at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    voice "audio/voices/ch2/witch/narrator/ch2_wn_11.flac"
    n "The interior of the cabin is a mess of twisted roots, the walls a chaotic weave of knotted wood that, almost as if by accident just happened to resemble a room. The floor is damp and earthy, and the only furniture of note is a slab of mud in the shape of a shelf, with a pristine blade perched on its edge.\n"
    voice "audio/voices/ch2/shared/narrator/ch2_share_n_25.flac"
    n "The blade is your implement. You'll need it if you want to do this right.\n"
    label cabin_interior_2_witch_menu:
        default witch_1_cabin_mirror_present = True
        default witch_1_cabin_blade_taken = False
        default witch_1_cabin_mirror_ask = False
        default witch_1_cabin_mirror_approached = False
        default witch_1_cabin_last_time_comment = False
        menu:
            extend ""

            "{i}• (Explore) You didn't say anything about the mirror on the wall.{/i}" if witch_1_cabin_mirror_ask == False and witch_1_cabin_mirror_present:
                $ witch_1_cabin_mirror_ask = True
                $ current_run_mirror_comment = True
                voice "audio/voices/ch2/witch/narrator/ch2_wn_12.flac"
                n "That's because there isn't a mirror. There's the muddy shelf, the blade sitting on the muddy shelf, and the door to the basement. There's nothing else in here.\n"
                voice "audio/voices/ch2/shared/hero/ch2_share_h_4.flac"
                hero "There's definitely a mirror.\n"
                voice "audio/voices/ch2/witch/opportunist/ch2_opportunist_12.flac"
                opportunist "But He says there isn't one. That's got to count for something, right?\n"
                menu:
                    extend ""

                    "{i}• I trust my eyes. Why would He lie about there not being a mirror? What's the point?{/i}":
                        voice "audio/voices/ch2/witch/opportunist/ch2_opportunist_13.flac"
                        opportunist "Come on, now. He's pretty much in charge here. When have authority figures ever lied about anything? If there were a mirror in this cabin and we were supposed to look at it, He would have told us about it.\n"
                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_28.flac"
                        n "Exactly. Why would I lie about something so meaningless? What good would a mirror even do? Let you waste time preening yourself instead of doing what needs to be done?\n"

                    "{i}• I want to look at myself. I want to see how {b}handsome{/b} I am.{/i}":
                        voice "audio/voices/ch2/witch/opportunist/ch2_opportunist_14.flac"
                        opportunist "Oh, I'm sure we'd look great. If only there were some sort of reflective surface we could examine. Absolute shame there isn't anything like that around here.\n"
                        voice "audio/voices/ch2/witch/hero/ch2_wh_7.flac"
                        hero "You... you {i}do{/i} see it, right? I don't know how to read you.\n"
                        voice "audio/voices/ch2/witch/opportunist/ch2_opportunist_15.flac"
                        opportunist "I see all sorts of things.\n"
                        voice "audio/voices/ch2/witch/hero/ch2_wh_8.flac"
                        hero "But do you see the mirror? It's a simple yes or no question.\n"
                        voice "audio/voices/ch2/witch/opportunist/ch2_opportunist_16.flac"
                        opportunist "Uh... I... help me out here, will you?\n"
                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_30.flac"
                        n "I'm not lying to you. Use your eyes, there is no mirror. Why would I lie about something so meaningless? What good would a mirror even do? Let you waste time preening yourself instead of doing what needs to be done?\n"
                        #n "For the last time, use your eyes, there is no mirror. Why would I lie about something so meaningless? What good would it even do?\n"

                    "{i}• It doesn't matter.{/i}":
                        $ witch_1_cabin_mirror_present = False
                        voice "audio/voices/ch2/shared/hero/ch2_share_h_5.flac"
                        hero "But it {i}does{/i} matter! Don't you care if we're being lied to? If He's willing to lie about something as innocuous as a mirror, what else is He hiding from us?\n"
                        voice "audio/voices/ch2/witch/opportunist/ch2_opportunist_13.flac"
                        opportunist "Come on, now. He's pretty much in charge here. When have authority figures ever lied about anything? If there were a mirror in this cabin and we were supposed to look at it, He would have told us about it.\n"
                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_30.flac"
                        hide mirror onlayer back
                        n "I'm not lying to you. Use your eyes, there is no mirror. Why would I lie about something so meaningless? What good would a mirror even do? Let you waste time preening yourself instead of doing what needs to be done?\n"
                        #n "That's right. And I'm not lying to you. Use your eyes, there is no mirror. Why would I lie about something so meaningless? What good would a mirror even do? Let you waste time preening yourself instead of doing what needs to be done?\n"
                        voice "audio/voices/ch2/shared/hero/ch2_share_h_6.flac"
                        hero "But there {i}was{/i} a mirror a second ago.\n"
                        voice "audio/voices/ch2/witch/opportunist/ch2_opportunist_17.flac"
                        opportunist "Well, at least we can all agree now that there's nothing to see here. Case closed. Good work everyone.\n"

                    "{i}• [[Remain silent.]{/i}":
                        voice "audio/voices/ch2/shared/hero/ch2_share_h_7a.flac"
                        hero "I care about if we're being lied to. If He's willing to lie about something as innocuous as a mirror, what else could He hiding from us?\n"
                        voice "audio/voices/ch2/witch/opportunist/ch2_opportunist_13.flac"
                        opportunist "Come on, now. He's pretty much in charge here. When have authority figures ever lied about anything? If there were a mirror in this cabin and we were supposed to look at it, He would have told us about it.\n"
                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_31.flac"
                        #n "That's right. I'm not lying to you, I {i}promise{/i}. There isn't a mirror. Really.\n"
                        n "I'm not lying to you, I {i}promise{/i}. There isn't a mirror. Really.\n"

                    "{i}• [[Approach the mirror.]{/i}" if witch_1_cabin_mirror_approached == False:
                        label witch_cabin_1_mirror_join:
                            $ witch_1_cabin_mirror_approached = True
                            play audio "audio/one_shot/footsteps_creaky.flac"
                            hide farback onlayer farback
                            hide bg onlayer back
                            hide door onlayer back
                            hide table onlayer back
                            hide knife onlayer back
                            hide mirror onlayer back
                            scene bg witch mirror onlayer front at Position(ypos=1125)
                            show mirror witch close onlayer front at Position(ypos=1125)
                            with dissolve
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_32.flac"
                            n "You walk up to the wall next to the basement door. It's a wall. There isn't much to see here.\n"
                            if witch_1_cabin_mirror_ask == False:
                                voice "audio/voices/ch2/shared/hero/ch2_share_h_8.flac"
                                hero "What are you talking about? This isn't a wall. It's a mirror. Or at least it'll {i}be{/i} a mirror once we wipe off that layer of grime.\n"
                            else:
                                voice "audio/voices/ch2/shared/hero/ch2_share_h_9.flac"
                                hero "This really isn't funny.\n"
                            $ current_run_mirror_touched = True
                            menu:
                                extend ""

                                "{i}• [[Wipe the mirror clean.]{/i}":
                                    $ witch_1_cabin_mirror_present = False
                                    hide mirror onlayer front
                                    play audio "audio/one_shot/new/STP_claws_1.flac"
                                    show player wall onlayer front at Position(ypos=1125) with dissolve
                                    if witch_1_cabin_mirror_ask == False:
                                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_33.flac"
                                    else:
                                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_33a.flac"
                                    n "You reach forward and rub your hand against the cabin wall. I hope you know how ridiculous you look right now.\n"
                                    hide player onlayer front with dissolve
                                    #voice "audio/voices/ch2/shared/hero/ch2_share_h_10.flac"
                                    #hero "But it was there a second ago!\n"
                                    if witch_1_cabin_mirror_ask:
                                        voice "audio/voices/ch2/witch/opportunist/ch2_opportunist_17.flac"
                                        opportunist "Well, at least we can all agree {i}now{/i} that there's nothing to see here. Case closed. Good work everyone.\n"
                                    play audio "audio/one_shot/footsteps_creaky.flac"
                                    hide bg onlayer front
                                    scene farback witch cabin onlayer farback at Position(ypos=1125)
                                    show bg witch cabin onlayer back at Position(ypos=1125)
                                    show door witch1 onlayer back at Position(ypos=1125)
                                    show table witch onlayer back at Position(ypos=1125)
                                    if witch_1_cabin_blade_taken == False:
                                        show knife witch onlayer back at Position(ypos=1125)
                                    with dissolve
                                    jump cabin_interior_2_witch_menu

                jump cabin_interior_2_witch_menu

            "{i}• (Explore) This whole cabin is different than last time.{/i}" if witch_1_cabin_last_time_comment == False and witch_1_forest_share_loop_insist:
                $ witch_1_cabin_last_time_comment = True
                voice "audio/voices/ch2/shared/hero/ch2_share_h_11.flac"
                hero "{i}Very{/i} different.\n"
                #voice "audio/voices/ch2/witch/opportunist/ch2_opportunist_18.flac"
                #opportunist "It's pretty squalid in here, don't you think?\n"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_34.flac"
                n "Maybe that's because you haven't actually been here. I hope this means you'll finally drop that ridiculous past-life nonsense. You haven't died, and you certainly haven't been killed by the Princess.\n"
                #n "{i}Maybe{/i} it looks different because you haven't actually been here. I hope this means you'll finally drop that ridiculous past-life nonsense. You haven't died, and you certainly haven't been killed by the Princess.\n"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_35.flac"
                n "So focus up. A lot's riding on this.\n"
                jump cabin_interior_2_witch_menu

            "{i}• (Explore) [[Approach the mirror.]{/i}" if witch_1_cabin_mirror_present and witch_1_cabin_mirror_approached == False:
                $ witch_1_cabin_mirror_approached = True
                jump witch_cabin_1_mirror_join

            "{i}• (Explore) [[Take the blade.]{/i}" if witch_1_cabin_blade_taken == False:
                $ witch_1_cabin_blade_taken = True
                $ blade_held = True
                $ default_mouse = "blade"
                voice "audio/voices/ch2/witch/narrator/ch2_wn_13.flac"
                play audio "audio/one_shot/knife_pickup.flac"
                hide knife onlayer back
                with dissolve
                n "You take the blade from the shelf. It would be difficult to slay the Princess and save the world without a weapon.\n"
                voice "audio/voices/ch2/witch/opportunist/ch2_opportunist_19.flac"
                opportunist "Well, if we're grabbing a weapon, we should probably keep it hidden behind our backs. She doesn't have to know we have it.\n"
                voice "audio/voices/ch2/witch/hero/ch2_wh_9.flac"
                hero "That's not actually a bad idea.\n"
                jump cabin_interior_2_witch_menu

            "{i}• [[Enter the basement.]{/i}":
                if witch_1_cabin_blade_taken == False:
                    if witch_1_forest_share_loop_insist:
                        voice "audio/voices/ch2/witch/hero/ch2_wh_10.flac"
                        hero "No blade? Leaving it behind didn't work out so well for us last time...\n"
                    else:
                        voice "audio/voices/ch2/witch/hero/ch2_wh_11.flac"
                        hero "No blade. I hope you know what you're getting us into.\n"
                    voice "audio/voices/ch2/witch/opportunist/ch2_opportunist_20.flac"
                    opportunist "It'll always be here if we need it. Sure, that was also true last time, and we still died. But we definitely know what we're doing {i}this{/i} time.\n"


                play audio "audio/one_shot/door_bedroom.flac"
                $ quick_menu = False
                show door witch2 onlayer back at Position(ypos=1125)
                with Dissolve(0.5)
                hide mirror onlayer back
                show door witch3 onlayer back at Position(ypos=1125) with Dissolve(0.5)
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

                voice "audio/voices/ch2/witch/narrator/ch2_wn_14.flac"
                play secondary "audio/looping/uncomfortable ambiance heightened.ogg" loop
                scene bg witch stairs onlayer back at Position(ypos=1125)
                with fade
                if persistent.quick_menu:
                    $ quick_menu = True
                n "The door to the basement creaks open, revealing a staircase dug into the muddy earth below. The ceiling is thick with roots that hang like locks of tangled hair.\n"
                voice "audio/voices/ch2/witch/narrator/ch2_wn_15.flac"
                n "The weak starlight from the cabin windows behind you can barely penetrate the gloom here, only illuminating the edges of an opening below. It shines in the darkness like some kind of massive maw, waiting to swallow you up into the earth.\n"
                voice "audio/voices/ch2/witch/narrator/ch2_wn_16.flac"
                n "The air smells of dirt and copper. It's thick and wet, as if your lungs are being coated in mud with each intake of breath. If the Princess lives here, slaying her would probably be doing her a favor.\n"
                voice "audio/voices/ch2/witch/narrator/ch2_wn_17.flac"
                n "Her voice skitters up from below.\n"
                voice "audio/voices/ch2/witch/princess/ch2_wp_1.flac"
                sp "Something nasty finds itself on my stairs. Come on down, don't be scared. I probably won't bite.\n"
                menu:
                    extend ""

                    "{i}• ''I'm not nasty!''{/i}":
                        voice "audio/voices/ch2/witch/princess/ch2_wp_2.flac"
                        sp "But you are. You're a wretched little thing.\n"
                        voice "audio/voices/ch2/witch/princess/ch2_wp_3.flac"
                        sp "I recognize that voice as easily as I recognized your nervous little footsteps coming up the path. I know who you are, and I remember what you've done.\n"

                    "{i}• ''Hello.''{/i}":
                        voice "audio/voices/ch2/witch/princess/ch2_wp_3.flac"
                        sp "I recognize that voice as easily as I recognized your nervous little footsteps coming up the path. I know who you are, and I remember what you've done.\n"

                    "{i}• Say nothing.{/i}":
                        voice "audio/voices/ch2/witch/princess/ch2_wp_4.flac"
                        sp "Silence, I see. Don't think I've forgotten about you. I recognized the sound of your nervous little footsteps as soon as they came into my home. I know who you are, and I remember what you've done.\n"

                if witch_1_forest_share_loop_insist == False:
                    voice "audio/voices/ch2/witch/narrator/ch2_wn_18a.flac"
                    n "She must have you confused with someone else.\n"
                else:
                    voice "audio/voices/ch2/witch/hero/ch2_wh_12.flac"
                    hero "See? She knows us. Is this enough for you to believe what we've been saying?\n"
                    voice "audio/voices/ch2/witch/narrator/ch2_wn_19.flac"
                    n "Maybe, but you shouldn't let that cloud your judgment. She's just a Princess. As long as you remember that and remain focused, slaying her will be {i}easy{/i}.\n"
                voice "audio/voices/ch2/witch/opportunist/ch2_opportunist_21.flac"
                opportunist "She seems friendly enough. Maybe we can talk our way out of this whole situation.\n"
                voice "audio/voices/ch2/witch/narrator/ch2_wn_20.flac"
                n "{i}Sigh{/i}. You can't. Unless you slay her right away, she's going to break free and end the world. There's no reasoning with what she is.\n"
                voice "audio/voices/ch2/witch/opportunist/ch2_opportunist_22.flac"
                opportunist "Look, I'm just throwing ideas out there. I like to think out loud. I'm the kind of guy who likes a {i}discussion{/i}, don't we want to hear what everyone has to say before making any big decisions?\n"
                voice "audio/voices/ch2/witch/hero/ch2_wh_13.flac"
                hero "Do you want to hear what everyone has to say, or do you just want to hear yourself talk?\n"
                voice "audio/voices/ch2/witch/narrator/ch2_wn_21.flac"
                n "You need to stop lingering. Your task is to {i}slay{/i} the Princess, not endlessly debate about what to do with the Princess.\n"
                voice "audio/voices/ch2/witch/opportunist/ch2_opportunist_23.flac"
                opportunist "Fine, fine. You're the boss.\n"
                $ gallery_witch.unlock_item(2)
                $ renpy.save_persistent()
                voice "audio/voices/ch2/witch/narrator/ch2_wn_22.flac"
                play audio "audio/one_shot/footsteps_creaky.flac"
                $ quick_menu = False
                hide bg onlayer back
                with fade
                #play sound "audio/looping/STP_firecontrolled_loop.ogg" loop fadein 1.0
                scene bg witch basement onlayer back at Position(ypos=1125)
                show witch d neutral onlayer back at Position(ypos=1125)
                #show fire witch basement onlayer back at Position(ypos=1125)
                with fade
                if persistent.quick_menu:
                    $ quick_menu = True
                n "Thank you. You descend the basement steps, entering the dark room below.\n"
                #voice "audio/voices/ch2/witch/narrator/ch2_wn_23.flac"
                voice "audio/voices/ch2/witch/narrator/s1.flac"
                n "You can just make out the shape of the Princess in the gloom. She's huddled against the far wall, her eyes bright and glaring from amid the thick roots.\n"

                if witch_1_cabin_blade_taken:
                    voice "audio/voices/ch2/witch/princess/ch2_wp_5.flac"
                    show witch d wry talk onlayer back at Position(ypos=1125) with dissolve
                    sp "And there you are, one hand tucked away behind your back, gripping that sharp, sharp blade, no doubt.\n"
                    show witch d wry onlayer back at Position(ypos=1125) with dissolve
                    voice "audio/voices/ch2/witch/opportunist/ch2_opportunist_24.flac"
                    opportunist "That's no fair, how would she know that?\n"
                    voice "audio/voices/ch2/witch/princess/ch2_wp_6.flac"
                    show witch d sass talk onlayer back at Position(ypos=1125) with dissolve
                    sp "So we've dropped the pretenses.\n"
                    voice "audio/voices/ch2/witch/princess/ch2_wp_7.flac"
                    show witch d annoyed talk onlayer back
                    with dissolve
                    sp "Good.\n"
                else:
                    voice "audio/voices/ch2/witch/princess/ch2_wp_8.flac"
                    show witch d wry talk onlayer back at Position(ypos=1125) with dissolve
                    sp "And there you are, once again seeming to offer a helping hand while likely hiding the other behind your back. Fine. I'll play along for now. What do you want?\n"

                jump witch_1_encounter_start
