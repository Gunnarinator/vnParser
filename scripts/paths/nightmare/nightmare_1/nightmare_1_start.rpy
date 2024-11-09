label nightmare_1_start:
    $ blade_held = False
    $ trait_paranoid = True
    $ quick_menu = False
    play sound "audio/looping/uncomfortable ambiance.ogg" loop fadein 1.0
    scene chapter nightmare with fade
    show text _("{color=#FFFFFF00}Chapter Two. The Nightmare.{/color}")  at Position(ypos=850)
    $ renpy.pause(4.0)

    play sound "audio/looping/uncomfortable ambiance.ogg" loop
    play secondary "audio/looping/uncomfortable ambiance heightened.ogg" loop
    play music "audio/_music/ch1/Fragmentation.flac" loop
    scene bg path onlayer farback at flip, Position(ypos=1125)
    show midground path onlayer back at flip, Position(ypos=1125)
    show front path onlayer front at flip, Position(ypos=1125)
    show bg black
    #show loading_icon
    hide text
    hide chapter
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    $ gallery_nightmare.unlock_gallery()
    $ gallery_zch1.unlock_item(7)
    $ renpy.save_persistent()
    voice "audio/voices/ch1/woods/narrator/script_n_1.flac"
    n "You're on a path in the woods. And at the end of that path is a cabin. And in the basement of that cabin is a Princess.\n"
    voice "audio/voices/ch1/woods/narrator/script_n_2.flac"
    n "You're here to slay her.\n If you don't, it will be the end of the world.\n"
    label nightmare_1_forest:
        default nightmare_1_forest_count = 0
        default nightmare_1_forest_share_died = False
        default nightmare_1_forest_share_loop = False
        default nightmare_1_forest_princess_press = False
        default nightmare_1_forest_share_loop_insist = False
        default nightmare_1_forest_deja_vu = False
        default nightmare_1_forest_deja_vu_follow_up = False
        default nightmare_1_forest_plead_leave = False
        menu:
            extend ""

            "{i}• (Explore) I'm getting a terrible sense of deja vu.{/i}" if nightmare_1_forest_share_loop == False:
                $ nightmare_1_forest_deja_vu = True
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_1a.flac"
                n "A terrible sense of deja vu? No, you don't have that. This is the first time either of us have been here.\n"
                label nightmare_1_forest_narrator_share_join:
                    $ nightmare_1_forest_count += 1
                    $ nightmare_1_forest_share_loop = True
                    voice "audio/voices/ch2/shared/hero/ch2_share_h_1.flac"
                    hero "If He doesn't remember what happened, then maybe it's best to keep it that way.\n"
                    voice "audio/voices/ch2/nightmare/paranoid/ch2_paranoid_1.flac"
                    paranoid "Shhh. What if He hears us?\n"
                    voice "audio/voices/ch2/nightmare/narrator/ch2_nn_1.flac"
                    n "That's a very good question, little voice. What if He {i}does{/i} hear you?\n"
                    voice "audio/voices/ch2/nightmare/paranoid/ch2_paranoid_2.flac"
                    paranoid "Shit.\n"
                    voice "audio/voices/ch2/nightmare/narrator/ch2_nn_2.flac"
                    n "I think you'll find yourselves very hard pressed to keep any secrets from me. Not that it matters right now, because like I said, this is the first time we've met. Still, I'd rather not get off on the wrong foot. We've a world to save, after all.\n"
                    jump nightmare_1_forest

            "{i}• (Explore) This is more than just deja vu, though. I'm pretty sure this whole thing literally just happened.{/i}" if nightmare_1_forest_deja_vu and nightmare_1_forest_deja_vu_follow_up == False:
                $ nightmare_1_forest_deja_vu_follow_up = True
                $ nightmare_1_forest_count += 1
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_2.flac"
                n "We could go back and forth on this forever, and it won't get you any closer to doing your job and saving the world. So let's just agree to disagree.\n"
                jump nightmare_1_forest

            "{i}• (Explore) Wait... hasn't this already happened?{/i}" if nightmare_1_forest_share_loop == False:
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_1b.flac"
                n "It hasn't. Or if it has, I certainly haven't been a part of it. We've just met for the first time, you and I.\n"
                jump nightmare_1_forest_narrator_share_join

            "{i}• (Explore) Okay, no.{/i}" if nightmare_1_forest_share_loop == False:
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_3a.flac"
                n "Oh, don't you start grandstanding about morals. The fate of the world is at risk right now, and the life of a mere Princess shouldn't stop you from saving us all.\n"
                jump nightmare_1_forest_narrator_share_join

            "{i}• (Explore) But I died! What am I doing here?{/i}" if nightmare_1_forest_share_loop == False:
                $ nightmare_1_forest_share_died = True
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_4.flac"
                n "I can assure you that you're not dead. And to answer your second question, you're here to slay the Princess. I literally told you that a second ago.\n"
                jump nightmare_1_forest_narrator_share_join

            "{i}• (Explore) She's going to kill me again!{/i}" if nightmare_1_forest_share_loop == False:
                $ nightmare_1_forest_share_died = True
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_5.flac"
                n "Again? People don't die twice. You haven't even met the Princess, and I hardly think she'd be capable of killing someone as skilled and courageous as yourself.\n"
                jump nightmare_1_forest_narrator_share_join

            "{i}• (Explore) Let's assume I'm telling the truth, and all of this really did already happen. Why should I listen to you? Why should I bother doing {i}anything{/i}?{/i}" if nightmare_1_forest_share_loop and (nightmare_1_forest_deja_vu == False or (nightmare_1_forest_deja_vu_follow_up)) and nightmare_1_forest_share_loop_insist == False:
                $ nightmare_1_forest_share_loop_insist = True
                $ nightmare_1_forest_count += 1
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_6.flac"
                n "Those are two very different questions, but fine. I'll indulge you if that's what it takes to get you moving.\n"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_7.flac"
                n "Let's say for a moment that this really is the second time you've met me, or, at least, a version of me.\n"
                if nightmare_1_forest_share_died == False:
                    voice "audio/voices/ch2/shared/narrator/ch2_share_n_8.flac"
                    n "If you're back here, I'm assuming you died, which probably only happened because you didn't listen to me.\n"
                else:
                    voice "audio/voices/ch2/shared/narrator/ch2_share_n_9.flac"
                    n "You died last time, which probably only happened because you didn't listen to me.\n"
                if nightmare_join_fled:
                    voice "audio/voices/ch2/nightmare/paranoid/ch2_paranoid_3.flac"
                    paranoid "Oh, we listened to you, all right. Worst decision of our incredibly short life.\n"
                    if blade_taken_1:
                        voice "audio/voices/ch2/nightmare/hero/ch2_nh_1.flac"
                        hero "We tried to slay her, we really did, but she was going to kill us. It was either lock her in the basement or let her finish beating us to death.\n"
                    else:
                        voice "audio/voices/ch2/nightmare/hero/ch2_nh_2.flac"
                        hero "We tried to slay her, we really did, but she was going to kill us. It was either lock her in the basement or let her finish tearing us to ribbons.\n"
                else:
                    voice "audio/voices/ch2/nightmare/paranoid/ch2_paranoid_4.flac"
                    paranoid "We couldn't trust {i}either{/i} of you. And as far as I'm concerned, we still can't.\n"
                    voice "audio/voices/ch2/nightmare/hero/ch2_nh_3.flac"
                    hero "All we did was lock her away.\n"
                    voice "audio/voices/ch2/nightmare/narrator/ch2_nn_3.flac"
                    n "And how'd that work out for you?\n"
                    voice "audio/voices/ch2/nightmare/hero/ch2_nh_4.flac"
                    hero "No comment.\n"
                voice "audio/voices/ch2/nightmare/narrator/ch2_nn_4.flac"
                n "Well then, congratulations. You've been given another chance to actually do this right.\n"
                voice "audio/voices/ch2/nightmare/paranoid/ch2_paranoid_5.flac"
                paranoid "And your solution to this is to send us back in there? Do you want us to slay the Princess, or do you want the Princess to slay {i}us{/i}?\n"
                voice "audio/voices/ch2/nightmare/narrator/ch2_nn_5.flac"
                n "Obviously I want {i}you{/i} to slay {i}her{/i}. One of you poses a threat to the world, and the other doesn't.\n"
                voice "audio/voices/ch2/nightmare/narrator/ch2_nn_6.flac"
                n "Anyways, I believe your other question was something along the lines of 'what's the point of doing anything?' If you're asking that, it sounds to me like you're making the rather dangerous assumption that your actions last time around didn't have any consequences.\n"
                voice "audio/voices/ch2/nightmare/hero/ch2_nh_5a.flac"
                hero "What do you mean? Of course there weren't any consequences. We were killed by the Princess, and now everyone's right back where they started. That sounds pretty consequence-free to me.\n"
                voice "audio/voices/ch2/nightmare/paranoid/ch2_paranoid_6.flac"
                paranoid "Speak for yourself. From my perspective there were plenty of consequences. I'm never going forget the way she just made us {i}stop working{/i}.\n"
                voice "audio/voices/ch2/nightmare/narrator/ch2_nn_7.flac"
                n "And that's only scratching the surface. If what you said is true, it begs the question of {i}how{/i} you got back here. Did 'time' simply rewind itself, or have you found yourself in another world altogether? If it's the latter, what do you think happened {i}after{/i} you died?\n"
                #voice "audio/voices/ch2/shared/narrator/ch2_share_n_13.flac"
                #n "If it's the latter, what do you think happened {i}after{/i} you died?\n"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_13a.flac"
                n "Do you think the people there lived happily ever after, or do you think that the Princess, left unhindered, brought about the end to everyone and everything, just like I told you she would?\n"
                voice "audio/voices/ch2/nightmare/paranoid/ch2_paranoid_7.flac"
                paranoid "If she brought an end to everything and everyone, how are {i}we{/i} supposed to stop her? What do you want from us?\n"
                voice "audio/voices/ch2/nightmare/narrator/ch2_nn_8.flac"
                n "I want you to succeed. You'll find a way. You're the only one who can.\n"
                jump nightmare_1_forest

            "{i}• (Explore) Let's talk about this Princess...{/i}" if nightmare_1_forest_share_loop_insist and nightmare_1_forest_princess_press == False:
                $ nightmare_1_forest_count += 1
                $ nightmare_1_forest_princess_press = True
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_14.flac"
                n "Just be quick about it.\n"
                label nightmare_1_forest_princess:
                    default nightmare_1_forest_princess_count = 0
                    default nightmare_1_forest_princess_why_strong = False
                    default nightmare_1_forest_princess_basement_explain = False
                    default nightmare_1_forest_princess_why_me = False
                    default nightmare_1_forest_princess_cagey = False
                    default nightmare_1_forest_princess_tips = False
                    menu:
                        extend ""

                        "{i}• (Explore) Just being around her in the end shut down all of my organs. What the hell am I supposed to do about that?{/i}" if nightmare_1_forest_princess_tips == False:
                            $ nightmare_1_forest_princess_tips = True
                            $ nightmare_1_forest_princess_count += 1
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_15.flac"
                            n "Like I said, if she killed you, it was probably because you didn't listen to me. Don't talk to her. Don't trust her. Just go in, do your job, and save the world.\n"
                            jump nightmare_1_forest_princess

                        "{i}• (Explore) To quote you from last time around, 'she's {i}just{/i} a Princess.' How can you possibly justify saying that? She's clearly something far, far worse.{/i}" if nightmare_1_forest_princess_why_strong == False:
                            $ nightmare_1_forest_princess_why_strong = True
                            $ nightmare_1_forest_princess_count += 1
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_17.flac"
                            n "She {i}is{/i} just a Princess. Whatever you think happened to you last time, just get it out of your head before you get to the cabin, and you'll be {i}fine{/i}.\n"
                            jump nightmare_1_forest_princess

                        "{i}• (Explore) Who locked her in that basement? What {b}is{/b} this place?{/i}" if nightmare_1_forest_princess_basement_explain == False:
                            $ nightmare_1_forest_princess_basement_explain = True
                            $ nightmare_1_forest_princess_count += 1
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_18.flac"
                            n "{i}People{/i} locked her in that basement. And I told you what this place is. It's a path in the woods. Don't overcomplicate things.\n"
                            jump nightmare_1_forest_princess

                        "{i}• (Explore) If people locked her away, why couldn't {b}they{/b} slay her? Why is this falling on me?{/i}" if nightmare_1_forest_princess_basement_explain and nightmare_1_forest_princess_why_me == False:
                            $ nightmare_1_forest_princess_why_me = True
                            $ nightmare_1_forest_princess_count += 1
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_19.flac"
                            n "Look, I'm not supposed to say this, but it's because you're special. You're the {i}only{/i} person capable of doing this. Call it a prophecy if that helps, but it's just the way things are.\n"
                            voice "audio/voices/ch2/nightmare/paranoid/ch2_paranoid_8.flac"
                            paranoid "You can't just goad us into doing something by calling us special. It's manipulative. Why are you trying to manipulate us?\n"
                            voice "audio/voices/ch2/nightmare/hero/ch2_nh_6.flac"
                            hero "I don't know, I kind of like being special.\n"
                            voice "audio/voices/ch2/nightmare/paranoid/ch2_paranoid_9.flac"
                            paranoid "Okay, fine. Maybe you can goad {i}him{/i} into doing something, but he's not even the one who makes the decisions here.\n"
                            voice "audio/voices/ch2/nightmare/narrator/ch2_nn_9.flac"
                            n "I'm not goading you into doing anything. You already know that the Princess is dangerous. All I'm trying to say is that you have to be the one to deal with her. I know it doesn't seem fair, but that's just the way it is.\n"
                            voice "audio/voices/ch2/nightmare/narrator/ch2_nn_10.flac"
                            n "And for what it's worth, I know you have it in you to finish the job.\n"
                            if nightmare_1_forest_plead_leave == False:
                                $ nightmare_1_forest_plead_leave = True
                                voice "audio/voices/ch2/nightmare/paranoid/ch2_paranoid_10.flac"
                                paranoid "We don't. You saw what happened to us last time. We need to {i}leave{/i}.\n"
                            jump nightmare_1_forest_princess

                        "{i}• (Explore) You're being cagey. What aren't you telling me?{/i}" if nightmare_1_forest_princess_cagey == False and nightmare_1_forest_princess_count > 1:
                            $ nightmare_1_forest_princess_cagey = True
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_21.flac"
                            n "I've told you everything you need to know, going into more detail would just overcomplicate an otherwise very simple situation and make your job more difficult.\n"
                            voice "audio/voices/ch2/shared/hero/ch2_share_h_3.flac"
                            hero "If you want us to stand a chance against her, we need to be armed with information. What is she really capable of? How are we supposed to stop her?\n"
                            if nightmare_1_forest_princess_count < 2:
                                voice "audio/voices/ch2/shared/narrator/ch2_share_n_22.flac"
                                n "The less you know about her, the better.\n"
                            else:
                                voice "audio/voices/ch2/shared/narrator/ch2_share_n_23.flac"
                                n "Not to sound like a broken record, but the less you know about her, the better things will go for all of us. I know it sounds like I'm hiding something, but you're just going to have to take me at my word.\n"
                            voice "audio/voices/ch2/nightmare/paranoid/ch2_paranoid_11.flac"
                            paranoid "He isn't telling us everything He knows because He doesn't trust us. Which means that {i}we{/i} can't trust {i}Him{/i}.\n" id nightmare_1_forest_princess_325636fd
                            voice "audio/voices/ch2/nightmare/narrator/ch2_nn_11.flac"
                            n "Stop talking yourself in neurotic circles and just get to the cabin already.\n"
                            if nightmare_1_forest_plead_leave:
                                voice "audio/voices/ch2/nightmare/paranoid/ch2_paranoid_12a.flac"
                                paranoid "Do you see the way He keeps pushing us? We have to get out of here.\n"
                            else:
                                voice "audio/voices/ch2/nightmare/paranoid/ch2_paranoid_13.flac"
                                paranoid "No, you should do anything but that. We {i}know{/i} what's waiting for us in that basement.\n"
                            jump nightmare_1_forest_princess

                        "{i}• Nevermind.{/i}" if nightmare_1_forest_princess_count == 0:
                            label nightmare_1_forest_princess_leaving:
                                voice "audio/voices/ch2/shared/narrator/ch2_share_n_24.flac"
                                n "Great. Now if you don't mind, the whole world is waiting with bated breath for you to save it from ruin.\n"
                                jump nightmare_1_forest

                        "{i}• That's all.{/i}" if nightmare_1_forest_princess_count != 0:
                            jump nightmare_1_forest_princess_leaving

            "{i}• [[Proceed to the cabin.]{/i}":
                jump nightmare_1_cabin_arrival

            "{i}• [[Turn around and leave.]{/i}" if mound_can_attempt_flee:
                if loops_finished >= 2:
                    $ mound_can_attempt_flee = False
                    voice "audio/voices/mound/bonus/flee.flac"
                    mound "You have already committed to my completion. You cannot go further astray.\n"
                    jump nightmare_1_forest
                voice "audio/voices/ch2/nightmare/paranoid/ch2_paranoid_14.flac"
                paranoid "This is good. I was worried you might fall for his shit again, but this is good. Whatever answers there are to be found, they aren't {i}here{/i}, and they definitely aren't {i}there{/i}.\n"
                jump turn_and_leave_join

label nightmare_1_cabin_arrival:
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
    voice "audio/voices/ch2/nightmare/hero/ch2_nh_7b.flac"
    hero "I don't think 'lying' and 'cheating' is her thing. She was {i}very{/i} direct with us last time. Or, at least she was direct with us after we decided to lock her away.\n"
    voice "audio/voices/ch2/nightmare/paranoid/ch2_paranoid_15.flac"
    paranoid "It doesn't matter. Don't. Trust. Anyone.\n"
    menu:
        extend ""

        "{i}• [[Proceed into the cabin.]{/i}":
            label nightmare_stranger_rejoin:
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

    $ gallery_nightmare.unlock_item(1)
    $ renpy.save_persistent()
    voice "audio/voices/ch2/nightmare/narrator/ch2_nn_12.flac"
    play sound "audio/looping/ambient_cabin.ogg" loop fadein 1.0
    play music "audio/_music/ch2/nightmare/The Nightmare.flac" loop
    play secondary "audio/looping/uncomfortable ambiance heightened.ogg" loop
    scene farback nightmare cabin onlayer farback at Position(ypos=1125)
    show bg nightmare cabin onlayer back at Position(ypos=1125)
    show table nightmare onlayer back at Position(ypos=1125)
    show knife nightmare onlayer back at Position(ypos=1125)
    show mirror base onlayer back at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    n "The interior of the cabin is plain, the smooth wood of the walls almost featureless. The only furniture of note is a lone table, knocked on its side in the corner of the room. A pristine blade stands between you and the open, inviting basement doorway.\n"
    voice "audio/voices/ch2/shared/narrator/ch2_share_n_25.flac"
    n "The blade is your implement. You'll need it if you want to do this right.\n"
    if nightmare_1_forest_share_loop == False:
        voice "audio/voices/ch2/nightmare/paranoid/ch2_paranoid_16.flac"
        paranoid "Hold on. What happened to the door?\n"
    else:
        voice "audio/voices/ch2/nightmare/paranoid/ch2_paranoid_17.flac"
        paranoid "Hold on. What happened to the door? There was a door here last time.\n"
    voice "audio/voices/ch2/nightmare/hero/ch2_nh_8a.flac"
    hero "It's just an empty frame...\n"
    voice "audio/voices/ch2/nightmare/paranoid/ch2_paranoid_18.flac"
    paranoid "She's already gotten out, hasn't she? And she's ready for us. She's been {i}waiting{/i}. Can't you feel her eyes on us?\n"
    voice "audio/voices/ch2/nightmare/narrator/ch2_nn_13.flac"
    n "I'm going to need all of you to pull yourselves together. The Princess has {i}not{/i} already gotten out, but if you keep getting stuck in your head like this, you're going to struggle to get the job done.\n"
    voice "audio/voices/ch2/nightmare/narrator/ch2_nn_14.flac"
    n "Yes. So deep breath in, deep breath out. Your task awaits, and only you can do it.\n"
    label cabin_interior_2_nightmare_menu:
        default nightmare_1_cabin_mirror_present = True
        default nightmare_1_cabin_blade_taken = False
        default nightmare_1_cabin_mirror_ask = False
        default nightmare_1_cabin_mirror_approached = False
        default nightmare_1_cabin_last_time_comment = False
        menu:
            extend ""

            "{i}• (Explore) You didn't say anything about the mirror on the wall.{/i}" if nightmare_1_cabin_mirror_ask == False and nightmare_1_cabin_mirror_present:
                $ nightmare_1_cabin_mirror_ask = True
                $ current_run_mirror_comment = True
                voice "audio/voices/ch2/nightmare/paranoid/ch2_paranoid_19.flac"
                paranoid "You're right. I was so stuck on the the {i}eyes{/i} watching us that I didn't even notice it there.\n"
                voice "audio/voices/ch2/nightmare/narrator/ch2_nn_15.flac"
                n "What are you two talking about? There isn't a mirror. There's the table, the blade sitting on the floor, and the open doorway leading to the basement. There's nothing else in here.\n"
                voice "audio/voices/ch2/shared/hero/ch2_share_h_4.flac"
                hero "There's definitely a mirror.\n"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_27.flac"
                n "There isn't.\n"
                voice "audio/voices/ch2/nightmare/paranoid/ch2_paranoid_20.flac"
                paranoid "We have to look at it... unless that's what He wants us to do and pretending it isn't there is a trick to get us to do exactly what He wants.\n"
                menu:
                    extend ""

                    "{i}• Why {b}would{/b} you lie about there not being a mirror when it's clearly right there? What's the point?{/i}":
                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_28.flac"
                        n "Exactly. Why would I lie about something so meaningless? What good would a mirror even do? Let you waste time preening yourself instead of doing what needs to be done?\n"

                    "{i}• I want to look at myself. I want to see how {b}handsome{/b} I am.{/i}":
                        voice "audio/voices/ch2/damsel/hero/ch2_dh_9.flac"
                        hero "We shouldn't waste time {i}preening{/i}, but if He {i}is{/i} lying about the mirror, it must be important.\n"
                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_29.flac"
                        n "I'm not lying to you. Use your eyes, there is no mirror. Why would I lie about something so meaningless? What good would it even do?\n"
                        voice "audio/voices/ch2/nightmare/paranoid/ch2_paranoid_21.flac"
                        paranoid "Maybe He's trying to keep us from looking because there's something horribly wrong with us.\n"
                        voice "audio/voices/ch2/nightmare/narrator/ch2_nn_16.flac"
                        n "No. There isn't something horribly wrong with you. You look exactly how you're supposed to look, now stop second-guessing my every word.\n"


                    "{i}• It doesn't matter.{/i}":
                        $ nightmare_1_cabin_mirror_present = False
                        voice "audio/voices/ch2/shared/hero/ch2_share_h_5.flac"
                        hero "But it {i}does{/i} matter! Don't you care if we're being lied to? If He's willing to lie about something as innocuous as a mirror, what else is He hiding from us?\n"
                        voice "audio/voices/ch2/nightmare/paranoid/ch2_paranoid_22.flac"
                        paranoid "Exactly! Everything He's saying is carefully crafted lies...\n"
                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_30.flac"
                        hide mirror onlayer back
                        n "I'm not lying to you. Use your eyes, there is no mirror. Why would I lie about something so meaningless? What good would a mirror even do? Let you waste time preening yourself instead of doing what needs to be done?\n"
                        voice "audio/voices/ch2/shared/hero/ch2_share_h_6.flac"
                        hero "But there {i}was{/i} a mirror a second ago.\n"
                        voice "audio/voices/ch2/nightmare/paranoid/ch2_paranoid_23.flac"
                        paranoid "Did {i}He{/i} make it go away? Clearly there was something in there worth investigating if He wants it hidden so bad...\n"

                    "{i}• [[Remain silent.]{/i}":
                        voice "audio/voices/ch2/shared/hero/ch2_share_h_7.flac"
                        hero "If He's willing to lie about something as innocuous as a mirror, what else could He hiding from us?\n"
                        voice "audio/voices/ch2/nightmare/paranoid/ch2_paranoid_22.flac"
                        paranoid "Exactly! Everything He's saying is carefully crafted lies...\n"
                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_31.flac"
                        n "I'm not lying to you, I {i}promise{/i}. There isn't a mirror. Really.\n"

                    "{i}• [[Approach the mirror.]{/i}" if nightmare_1_cabin_mirror_approached == False:
                        label nightmare_cabin_1_mirror_join:
                            play audio "audio/one_shot/footsteps_creaky.flac"
                            hide farback onlayer farback
                            hide bg onlayer back
                            hide door onlayer back
                            hide table onlayer back
                            hide knife onlayer back
                            hide mirror onlayer back
                            scene bg nightmare mirror onlayer front at Position(ypos=1125)
                            show mirror nightmare close onlayer front at Position(ypos=1125)
                            with dissolve
                            $ nightmare_1_cabin_mirror_approached = True
                            # fix in rereads
                            if nightmare_1_forest_share_loop == False and nightmare_1_cabin_mirror_ask == False:
                                voice "audio/voices/ch2/nightmare/narrator/ch2_nn_framewall_1b.flac"
                            elif nightmare_1_cabin_mirror_ask == False:
                                voice "audio/voices/ch2/nightmare/narrator/ch2_nn_framewall_1.flac"
                            else:
                                voice "audio/voices/ch2/nightmare/narrator/ch2_nn_framewall_1a.flac"
                            n "You walk up to the wall next to the empty basement doorframe. It's a wall. There isn't much to see here.\n"
                            if nightmare_1_cabin_mirror_ask == False:
                                voice "audio/voices/ch2/shared/hero/ch2_share_h_8.flac"
                                hero "What are you talking about? This isn't a wall. It's a mirror. Or at least it'll {i}be{/i} a mirror once we wipe off that layer of grime.\n"
                            else:
                                voice "audio/voices/ch2/shared/hero/ch2_share_h_9.flac"
                                hero "This really isn't funny.\n"
                            $ current_run_mirror_comment = True
                            menu:
                                extend ""

                                "{i}• [[Wipe the mirror clean.]{/i}":
                                    $ nightmare_1_cabin_mirror_present = False
                                    if nightmare_1_cabin_mirror_ask == False:
                                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_33.flac"
                                    else:
                                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_33a.flac"
                                    hide mirror onlayer front
                                    play audio "audio/one_shot/new/STP_claws_1.flac"
                                    show player wall onlayer front at Position(ypos=1125) with dissolve
                                    n "You reach forward and rub your hand against the cabin wall. I hope you know how ridiculous you look right now.\n"
                                    hide player onlayer front with dissolve
                                    #voice "audio/voices/ch2/shared/hero/ch2_share_h_10.flac"
                                    voice "audio/voices/ch2/nightmare/paranoid/ch2_paranoid_23.flac"
                                    paranoid "Did {i}He{/i} make it go away? Clearly there was something in there worth investigating if He wants it hidden so bad...\n"
                                    play audio "audio/one_shot/footsteps_creaky.flac"
                                    hide bg onlayer front
                                    scene farback nightmare cabin onlayer farback at Position(ypos=1125)
                                    show bg nightmare cabin onlayer back at Position(ypos=1125)
                                    show table nightmare onlayer back at Position(ypos=1125)
                                    if nightmare_1_cabin_blade_taken == False:
                                        show knife nightmare onlayer back at Position(ypos=1125)
                                    with dissolve
                                    jump cabin_interior_2_nightmare_menu

                jump cabin_interior_2_nightmare_menu

            "{i}• (Explore) This whole cabin is different than I remember it being.{/i}" if nightmare_1_cabin_last_time_comment == False and nightmare_1_forest_share_loop:
                $ nightmare_1_cabin_last_time_comment = True
                voice "audio/voices/ch2/shared/hero/ch2_share_h_11.flac"
                hero "{i}Very{/i} different.\n"
                if nightmare_1_cabin_mirror_ask == False:
                    voice "audio/voices/ch2/nightmare/paranoid/ch2_paranoid_24.flac"
                    paranoid "I'm not the only one who sees her in the window, right? She knows that we're here.\n"
                else:
                    voice "audio/voices/ch2/nightmare/paranoid/ch2_paranoid_25.flac"
                    paranoid "{i}He{/i} changed it, didn't He? It's like He's trying to make us doubt our reality.\n"
                voice "audio/voices/ch2/nightmare/narrator/ch2_nn_17.flac"
                n "Calm down. Maybe the three of you just {i}think{/i} everything is different because you haven't been here before. Enough of this past-life nonsense. You haven't died, and you certainly haven't been killed by the Princess.\n"
                #voice "audio/voices/ch2/nightmare/narrator/ch2_nn_18.flac"
                #n "So focus up. A lot is riding on this.\n"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_35.flac"
                n "So focus up. A lot's riding on this.\n"
                jump cabin_interior_2_nightmare_menu

            "{i}• (Explore) [[Approach the mirror.]{/i}" if nightmare_1_cabin_mirror_present and nightmare_1_cabin_mirror_approached == False:
                $ nightmare_1_cabin_mirror_approached = True
                jump nightmare_cabin_1_mirror_join

            "{i}• (Explore) [[Take the blade.]{/i}" if nightmare_1_cabin_blade_taken == False:
                $ nightmare_1_cabin_blade_taken = True
                $ blade_held = True
                $ default_mouse = "blade"
                voice "audio/voices/ch2/nightmare/narrator/ch2_nn_18a.flac"
                play audio "audio/one_shot/knife_pickup.flac"
                hide knife onlayer back
                with dissolve
                n "You reach down and pick the blade up off the floor. It would be difficult to slay the Princess and save the world without a weapon.\n"
                voice "audio/voices/ch2/nightmare/paranoid/ch2_paranoid_26.flac"
                paranoid "Good. Steel can't lie to us.\n"
                voice "audio/voices/ch2/nightmare/hero/ch2_nh_9a.flac"
                hero "Is it gonna be enough, though? Couldn't you have given us something else? Something, I don't know, better than a knife? Can we have a bomb?\n"
                voice "audio/voices/ch2/nightmare/narrator/ch2_nn_19.flac"
                n "The blade is the only thing you need to finish your task. You're more than capable of pulling this off so long as you don't lose faith in yourself.\n"
                voice "audio/voices/ch2/nightmare/paranoid/ch2_paranoid_27.flac"
                paranoid "Those are the words of someone who knows He's sending us to our death...\n"
                jump cabin_interior_2_nightmare_menu

            "{i}• [[Enter the basement.]{/i}":
                if nightmare_1_cabin_blade_taken == False:
                    if blade_taken_1 == False:
                        voice "audio/voices/ch2/nightmare/paranoid/ch2_paranoid_28.flac"
                        paranoid "We should have taken the knife. I don't think going down there unarmed is going to do us any favors.\n"
                    else:
                        voice "audio/voices/ch2/nightmare/paranoid/ch2_paranoid_29.flac"
                        paranoid "We should have taken the knife again. I don't think she's going to take an olive branch. We need something sharper.\n"

                    #hero "I guess we'll just have to trust that we made the right call. It'll always be here if we need it.\n"

                $ quick_menu = False
                hide mirror onlayer back
                play audio "audio/one_shot/footsteps_creaky.flac"
                hide farback onlayer farback
                hide bg onlayer back
                hide door onlayer back
                hide table onlayer back
                hide knife onlayer back
                hide mirror onlayer back
                with fade

                stop sound fadeout 1.0


                play sound "audio/looping/STP_opressive_loop.ogg" loop
                scene farback nightmare basement onlayer farback at Position(ypos=1125)
                show eyes nightmare stairs onlayer back at Position(ypos=1125)
                show eyes2 nightmare stairs onlayer back at Position(ypos=1125)
                show steps nightmare stairs onlayer back at Position(ypos=1125)
                with fade
                if persistent.quick_menu:
                    $ quick_menu = True
                voice "audio/voices/ch2/nightmare/narrator/ch2_nn_20.flac"
                n "You cross over the threshold, and onto a series of isolated steps suspended in darkness.\n"
                voice "audio/voices/ch2/nightmare/paranoid/ch2_paranoid_30.flac"
                paranoid "More eyes, too. You never mention the eyes.\n"
                voice "audio/voices/ch2/nightmare/narrator/ch2_nn_21.flac"
                n "The air seeping up from below reminds you of fresh lightning and static, as if you're descending into a place that isn't meant for a creature of flesh and blood. If the Princess lives here, slaying her would probably be doing her a favor.\n"
                voice "audio/voices/ch2/nightmare/narrator/ch2_nn_22.flac"
                n "Her cruel and playful voice prances up the stairs.\n"
                voice "audio/voices/ch2/nightmare/princess/ch2_np_1.flac"
                sp "I didn't think you'd come back. We're going to have a lot of fun, you and I.\n"
                if nightmare_1_forest_share_loop == False:
                    voice "audio/voices/ch2/nightmare/narrator/ch2_nn_23.flac"
                    n "'Come back?' She must have you confused with someone else.\n"
                    voice "audio/voices/ch2/nightmare/hero/ch2_nh_10.flac"
                    hero "You really don't remember, do you? It doesn't matter. We need a game plan. We {i}know{/i} we can't just go down there unprepared.\n"
                else:
                    voice "audio/voices/ch2/nightmare/hero/ch2_nh_11.flac"
                    hero "Okay. We need a game plan. Last time we were here, just being close to her was enough to kill us.\n"
                label ch2_nightmare_stairs_menu:
                    default nightmare_blade_throw_ask = False
                    menu:
                        extend ""

                        "{i}• (Explore) How hard is it to throw a knife?{/i}" if nightmare_blade_throw_ask == False and blade_held:
                            $ nightmare_blade_throw_ask = True
                            if nightmare_1_cabin_blade_taken:
                                voice "audio/voices/ch2/nightmare/hero/ch2_nh_12.flac"
                                hero "It can't be {i}that{/i} hard.\n"
                                voice "audio/voices/ch2/nightmare/paranoid/ch2_paranoid_31.flac"
                                paranoid "But then we'd lose our weapon. We'd have to make it count. Otherwise she'd be furious and we'd be defenseless. If a knife is enough to even do anything against something like her in the first place...\n"
                                voice "audio/voices/ch2/nightmare/narrator/ch2_nn_24.flac"
                                n "It'll be enough.\n"
                            else:
                                voice "audio/voices/ch2/nightmare/hero/ch2_nh_13.flac"
                                hero "You're joking, right? You didn't even {i}bring{/i} the knife.\n"
                                voice "audio/voices/ch2/nightmare/paranoid/ch2_paranoid_32.flac"
                                paranoid "Should we go back for it? {i}Can{/i} we even go back for it?\n"
                                play audio "audio/one_shot/footsteps_creaky.flac"
                                voice "audio/voices/ch2/nightmare/narrator/ch2_nn_25.flac"
                                hide farback onlayer farback
                                hide eyes onlayer back
                                hide eyes2 onlayer back
                                hide steps onlayer back
                                show farback nightmare basement onlayer farback at Position(ypos=1125)
                                show eyes nightmare stairs forever onlayer back at Position(ypos=1125)
                                show stairs nightmare forever onlayer back at Position(ypos=1125)
                                with dissolve
                                n "You briefly turn back. Where there once was an entrance to the cabin, now there are only more stairs. Hmm. That's not right.\n" id ch2_nightmare_stairs_menu_92dfd5a6
                                voice "audio/voices/ch2/nightmare/hero/ch2_nh_14.flac"
                                hero "I guess the only way out of this place is through it.\n"
                                play audio "audio/one_shot/footsteps_creaky.flac"
                                hide farback onlayer farback
                                hide eyes onlayer back
                                hide stairs onlayer back
                                show farback nightmare basement onlayer farback at Position(ypos=1125)
                                show eyes nightmare stairs onlayer back at Position(ypos=1125)
                                show eyes2 nightmare stairs onlayer back at Position(ypos=1125)
                                show steps nightmare stairs onlayer back at Position(ypos=1125)
                                with dissolve
                            jump ch2_nightmare_stairs_menu

                        "{i}• I'm going to talk to her.{/i}":
                            voice "audio/voices/ch2/nightmare/narrator/ch2_nn_26.flac"
                            n "Didn't you hear my warning a minute ago? She can't be trusted. Talking won't do you any good.\n"
                            voice "audio/voices/ch2/nightmare/hero/ch2_nh_15.flac"
                            hero "Something tells me she isn't going to be keen on talking anyway.\n"
                            play audio "audio/one_shot/footsteps_creaky.flac"
                            $ quick_menu = False
                            hide farback onlayer farback
                            hide eyes onlayer back
                            hide eyes2 onlayer back
                            hide steps onlayer back
                            scene bg black
                            with fade
                            if persistent.quick_menu:
                                $ quick_menu = True
                            voice "audio/voices/ch2/nightmare/narrator/ch2_nn_27.flac"
                            n "You make your way to the bottom of the stairs.\n"

                        "{i}• We don't need a plan. I'm just going to kill her. Mr. Narrator seems to think I can do it. I don't know why you're all being such pessimists right now.{/i}":
                            default ch2_nightmare_voice_of_reason_comment = False
                            $ ch2_nightmare_voice_of_reason_comment = True
                            if nightmare_1_cabin_blade_taken:
                                voice "audio/voices/ch2/nightmare/narrator/ch2_nn_28.flac"
                                n "Finally, a voice of reason. The rest of you should take notes.\n"
                                voice "audio/voices/ch2/nightmare/hero/ch2_nh_16.flac"
                                hero "You know why I'm being a pessimist.\n"
                                voice "audio/voices/ch2/nightmare/paranoid/ch2_paranoid_33.flac"
                                paranoid "I'm just asking questions.\n"
                                play audio "audio/one_shot/footsteps_creaky.flac"
                                $ quick_menu = False
                                hide farback onlayer farback
                                hide eyes onlayer back
                                hide eyes2 onlayer back
                                hide steps onlayer back
                                scene bg black
                                with fade
                                if persistent.quick_menu:
                                    $ quick_menu = True
                                voice "audio/voices/ch2/nightmare/narrator/ch2_nn_27.flac"
                                n "You make your way to the bottom of the stairs.\n"
                            else:
                                voice "audio/voices/ch2/nightmare/narrator/ch2_nn_29.flac"
                                n "Finally, a voice of reason. The rest of you should take notes. Still, slaying her would be much easier if you had a weapon.\n"
                                voice "audio/voices/ch2/nightmare/paranoid/ch2_paranoid_32.flac"
                                paranoid "Should we go back for it? {i}Can{/i} we even go back for it?\n"
                                voice "audio/voices/ch2/nightmare/narrator/ch2_nn_30.flac"
                                play audio "audio/one_shot/footsteps_creaky.flac"
                                hide farback onlayer farback
                                hide eyes onlayer back
                                hide eyes2 onlayer back
                                hide steps onlayer back
                                show farback nightmare basement onlayer farback at Position(ypos=1125)
                                show eyes nightmare stairs forever onlayer back at Position(ypos=1125)
                                show stairs nightmare forever onlayer back at Position(ypos=1125)
                                with dissolve
                                n "You briefly turn back. Where there once was an entrance to the cabin, now there are only more stairs.\n"
                                voice "audio/voices/ch2/nightmare/hero/ch2_nh_14.flac"
                                play audio "audio/one_shot/footsteps_creaky.flac"
                                hide farback onlayer farback
                                hide eyes onlayer back
                                hide stairs onlayer back
                                show farback nightmare basement onlayer farback at Position(ypos=1125)
                                show eyes nightmare stairs onlayer back at Position(ypos=1125)
                                show eyes2 nightmare stairs onlayer back at Position(ypos=1125)
                                show steps nightmare stairs onlayer back at Position(ypos=1125)
                                with dissolve
                                hero "I guess the only way out of this place is through it.\n"
                                play audio "audio/one_shot/footsteps_creaky.flac"
                                $ quick_menu = False
                                hide farback onlayer farback
                                hide eyes onlayer back
                                hide eyes2 onlayer back
                                hide steps onlayer back
                                scene bg black
                                with fade
                                if persistent.quick_menu:
                                    $ quick_menu = True
                                voice "audio/voices/ch2/nightmare/narrator/ch2_nn_27.flac"
                                n "You make your way to the bottom of the stairs.\n"

                        "{i}• [[Step off into the void between the stairs.]{/i}":
                            play audio "audio/one_shot/static_short.flac"
                            show farback nightmare basement onlayer farback at Position(ypos=1125)
                            show eyes nightmare stairs onlayer back at Position(ypos=1125)
                            show eyes2 nightmare stairs onlayer back at Position(ypos=1125)
                            show steps nightmare stairs onlayer back at Position(ypos=1125)
                            with flash
                            voice "audio/voices/ch2/nightmare/narrator/ch2_nn_31a.flac"
                            n "You attempt to step off the stairs and into the pitch black surrounding them, but you're stopped by an invisible force. Why did you do that? What did you think would happen?\n"
                            menu:
                                extend ""

                                "{i}• I was curious.{/i}":
                                    voice "audio/voices/ch2/nightmare/narrator/ch2_nn_32.flac"
                                    n "Congratulations, you really lucked out. Of all the things that could have happened from stepping into a void, nothing is quite possibly the best outcome you could have gotten.\n"
                                    jump nightmare_1_basement_stairs_void_join

                                "{i}• I don't know. Falling into an infinite void seemed better than going downstairs and dying. I'm just scared.{/i}":
                                    voice "audio/voices/ch2/nightmare/narrator/ch2_nn_33.flac"
                                    n "How would falling into an infinite void be better than {i}anything{/i}?\n"
                                    jump nightmare_1_basement_stairs_void_join

                                "{i}• [[Say nothing.]{/i}":
                                    label nightmare_1_basement_stairs_void_join:
                                        play audio "audio/one_shot/footsteps_creaky.flac"
                                        hide farback onlayer farback
                                        hide eyes onlayer back
                                        hide eyes2 onlayer back
                                        hide steps onlayer back
                                        scene bg black
                                        with fade
                                        voice "audio/voices/ch2/nightmare/narrator/ch2_nn_34.flac"
                                        n "{i}Sigh.{/i} You make your way to the bottom of the stairs.\n"

                        "{i}• [[Continue down the stairs in silence.]{/i}":
                            play audio "audio/one_shot/footsteps_creaky.flac"
                            $ quick_menu = False
                            hide farback onlayer farback
                            hide eyes onlayer back
                            hide eyes2 onlayer back
                            hide steps onlayer back
                            hide bg onlayer back
                            scene bg black
                            with fade
                            if persistent.quick_menu:
                                $ quick_menu = True
                            voice "audio/voices/ch2/nightmare/narrator/ch2_nn_27.flac"
                            n "You make your way to the bottom of the stairs.\n"
                            jump nightmare_1_basement

label nightmare_1_basement:
    play audio "audio/one_shot/footsteps_creaky.flac"
    voice "audio/voices/ch2/nightmare/narrator/ch2_nn_35.flac"
    hide bg onlayer back
    $ quick_menu = False
    show farback nightmare basement onlayer farback at Position(ypos=1125)
    show eyes nightmare stairs onlayer back at Position(ypos=1125)
    show eyes2 nightmare stairs onlayer back at Position(ypos=1125)
    show wood nightmare basement onlayer front at Position(ypos=1125)
    show rocks nightmare basement onlayer front at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    n "As you emerge, you find yourself between two loose rows of white wooden planks, suspended in nothingness. A smattering of cobblestones, visible against the inky black of the basement, mark where the floor should be, forming vague pathways. At what seems to be the end of the room, they diverge in opposite directions. Left and right.\n"
    voice "audio/voices/ch2/nightmare/paranoid/ch2_paranoid_34.flac"
    paranoid "She could be anywhere. And there's nowhere for us to hide. We're completely exposed.\n"
    voice "audio/voices/ch2/nightmare/hero/ch2_nh_17.flac"
    hero "Are you really not going to comment on how {i}weird{/i} this place is?\n"
    if ch2_nightmare_voice_of_reason_comment == False:
        voice "audio/voices/ch2/nightmare/narrator/ch2_nn_36.flac"
        n "No, I'm not. Somebody needs to be the voice of reason here, and it certainly isn't you.\n"
        voice "audio/voices/ch2/nightmare/hero/ch2_nh_18.flac"
        hero "Excuse me? I'm being {i}incredibly{/i} reasonable. You're the one who's just matter-of-factly describing whatever the hell we're looking at like it's an ordinary basement.\n"
    else:
        voice "audio/voices/ch2/nightmare/narrator/ch2_nn_36a.flac"
        n "No, I'm not.\n"
    voice "audio/voices/ch2/nightmare/paranoid/ch2_paranoid_35.flac"
    paranoid "We're going to die down here. I don't want to die again.\n"
    voice "audio/voices/ch2/nightmare/narrator/ch2_nn_37.flac"
    n "Please stop saying that. You're only going to make things worse. Just pick a direction and start moving.\n"
    voice "audio/voices/ch2/nightmare/princess/ch2_np_2.flac"
    sp "I wouldn't give it too much thought, if I were you. It doesn't really matter, because either way you go, I'm going to find you.\n"
    menu:
        extend ""

        "{i}• Go left.{/i}":
            $ quick_menu = False
            show farback nightmare basement onlayer farback at Position(ypos=1125)
            show eyes nightmare stairs onlayer back at Position(ypos=1125)
            show eyes2 nightmare stairs onlayer back at Position(ypos=1125)
            show wood nightmare basement var onlayer front at Position(ypos=1125)
            show rocks nightmare basement var onlayer front at Position(ypos=1125)
            with fade
            if persistent.quick_menu:
                $ quick_menu = True
            voice "audio/voices/ch2/nightmare/narrator/ch2_nn_43.flac"
            n "You turn to the left.\n"
            jump nightmare_1_basement_direction_join

        "{i}• Go right.{/i}":
            $ quick_menu = False
            show farback nightmare basement onlayer farback at Position(ypos=1125)
            show eyes nightmare stairs onlayer back at Position(ypos=1125)
            show eyes2 nightmare stairs onlayer back at Position(ypos=1125)
            show wood nightmare basement var onlayer front at Position(ypos=1125)
            show rocks nightmare basement var onlayer front at Position(ypos=1125)
            with fade
            if persistent.quick_menu:
                $ quick_menu = True
            voice "audio/voices/ch2/nightmare/narrator/ch2_nn_44.flac"
            n "You turn to the right.\n"
            jump nightmare_1_basement_direction_join

        "{i}• Do nothing.{/i}":
            default nightmare_basement_nothing = False
            $ nightmare_basement_nothing = True
            voice "audio/voices/ch2/nightmare/narrator/ch2_nn_45.flac"
            n "You decide it's best to do nothing.\n"
            jump nightmare_1_basement_direction_join

        "{i}• Go back the way you came.{/i}":
            $ quick_menu = False
            show farback nightmare basement onlayer farback at Position(ypos=1125)
            show eyes nightmare stairs onlayer back at Position(ypos=1125)
            show eyes2 nightmare stairs onlayer back at Position(ypos=1125)
            show wood nightmare basement var onlayer front at Position(ypos=1125)
            show rocks nightmare basement var onlayer front at Position(ypos=1125)
            with fade
            if persistent.quick_menu:
                $ quick_menu = True
            voice "audio/voices/ch2/nightmare/narrator/ch2_nn_38.flac"
            n "You turn back to the stairs, only to find that they aren't there.\n"
            label nightmare_1_basement_direction_join:
                if nightmare_basement_nothing == False:
                    voice "audio/voices/ch2/nightmare/narrator/ch2_nn_39.flac"
                    #n "A faintly outlined path lies before you. You step forward.\n"
                    n "A faintly outlined path lies before you.\n"

                $ gallery_nightmare.unlock_item(2)
                $ renpy.save_persistent()
                voice "audio/voices/ch2/nightmare/princess/ch2_np_3.flac"
                play audio "audio/one_shot/static_short3.flac"
                show fog nightmare 2 1 onlayer front at Position(ypos=1125)
                show nightmare approach1 onlayer front at Position(ypos=1125)
                sp "There you are! I told you I was going to find you.\n"
                voice "audio/voices/ch2/nightmare/narrator/ch2_nn_40.flac"
                play audio "audio/one_shot/static_short.flac"
                hide fog onlayer front
                show nightmare upstairs blade look onlayer front
                n "As the Princess approaches, your legs suddenly go numb.\n"
                voice "audio/voices/ch2/nightmare/narrator/ch2_nn_41.flac"
                n "Your arms quickly follow.\n"
                voice "audio/voices/ch2/nightmare/hero/ch2_nh_19.flac"
                hero "This is it, isn't it?\n"
                play audio "audio/one_shot/static_short3.flac"
                #show fog nightmare 2 3 onlayer front at Position(ypos=1125)
                show nightmare upstairs angry onlayer front
                if nightmare_1_cabin_blade_taken:
                    if blade_taken_1:
                        voice "audio/voices/ch2/nightmare/princess/ch2_np_4a.flac"
                        sp "And you brought your little knife with you again. Cute.\n"
                    else:
                        voice "audio/voices/ch2/nightmare/princess/ch2_np_5.flac"
                        sp "And you brought a little knife with you. Cute.\n"
                else:
                    if blade_taken_1:
                        voice "audio/voices/ch2/nightmare/princess/ch2_np_6.flac"
                        sp "No little knife this time? It's almost like... you {i}want{/i} me to get you.\n"
                    else:
                        voice "audio/voices/ch2/nightmare/princess/ch2_np_7a.flac"
                        sp "It's almost like... you {i}want{/i} me to get you.\n"
                voice "audio/voices/ch2/nightmare/paranoid/ch2_paranoid_36.flac"
                paranoid "There has to be a way out of this. Think. {i}Think{/i}!\n"
                voice "audio/voices/ch2/nightmare/narrator/ch2_nn_42a.flac"
                n "What did you do? Pull yourself together, she isn't supposed to be like this.\n"
                play audio "audio/one_shot/static_short.flac"
                show nightmare stairs wait onlayer front
                voice "audio/voices/ch2/nightmare/princess/ch2_np_8.flac"
                sp "I wonder how many times I'll get to play with you before you break.\n"
                $ gallery_nightmare.unlock_item(3)
                $ renpy.save_persistent()
                jump nightmare_encounter_start
