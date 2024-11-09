label razor_1_start:
    $ blade_held = False
    $ trait_cheated = True
    $ quick_menu = False
    play sound "audio/looping/uncomfortable ambiance.ogg" loop fadein 1.0
    scene chapter razor with fade
    show text _("{color=#FFFFFF00}Chapter Two. The Razor.{/color}") at Position(ypos=850)
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
    $ gallery_razor.unlock_gallery()
    $ gallery_zch1.unlock_item(10)
    $ renpy.save_persistent()
    voice "audio/voices/ch1/woods/narrator/script_n_1.flac"
    n "You're on a path in the woods. And at the end of that path is a cabin. And in the basement of that cabin is a Princess.\n"
    voice "audio/voices/ch1/woods/narrator/script_n_2.flac"
    n "You're here to slay her.\n If you don't, it will be the end of the world.\n"
    label razor_1_forest:
        default razor_1_forest_count = 0
        default razor_1_forest_share_died = False
        default razor_1_forest_share_loop = False
        default razor_1_forest_princess_press = False
        default razor_1_forest_share_loop_insist = False
        default razor_1_forest_deja_vu = False
        default razor_1_forest_deja_vu_follow_up = False
        menu:
            extend ""

            "{i}• (Explore) I'm getting a terrible sense of deja vu.{/i}" if razor_1_forest_share_loop == False:
                $ razor_1_forest_deja_vu = True
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_1a.flac"
                n "A terrible sense of deja vu? No, you don't have that. This is the first time either of us have been here.\n"
                label razor_1_forest_narrator_share_join:
                    $ razor_1_forest_count += 1
                    $ razor_1_forest_share_loop = True
                    voice "audio/voices/ch2/shared/hero/ch2_share_h_1.flac"
                    hero "If He doesn't remember what happened, then maybe it's best to keep it that way.\n"
                    voice "audio/voices/ch2/razor/cheated/1.flac"
                    cheated "This whole thing's a crock of shit. She's just going to pull a knife out of nowhere and stab us again.\n"
                    voice "audio/voices/ch2/razor/narrator/ch2_rn_1.flac"
                    n "Stabbed to death? Well, you won't have to worry about that. The Princess is unarmed.\n"
                    if razor_revival:
                        voice "audio/voices/ch2/razor/cheated/2.flac"
                        cheated "Yeah, that's exactly what you told us last time. You said this whole thing would be easy, but after we sank our blade into her heart she just got up and started stabbing us.\n"
                    else:
                        voice "audio/voices/ch2/razor/cheated/3.flac"
                        cheated "Yeah, that's exactly what you told us last time. When we asked you if you were sure she didn't have a weapon on her, you said you were 'positive' she didn't.\n"
                        voice "audio/voices/ch2/razor/cheated/4.flac"
                        cheated "But it turns out she did. Because when we charged her, she started stabbing us. To {i}death{/i}!\n"
                    voice "audio/voices/ch2/razor/narrator/ch2_rn_2.flac"
                    n "Calm down. I assure you she has no weapons, so there's no reason to fear her. You were made for this job. You'll do just fine.\n"
                    jump razor_1_forest

            "{i}• (Explore) This is more than just deja vu, though. I'm pretty sure this whole thing literally just happened.{/i}" if razor_1_forest_deja_vu and razor_1_forest_deja_vu_follow_up == False:
                $ razor_1_forest_deja_vu_follow_up = True
                $ razor_1_forest_count += 1
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_1.flac"
                n "It hasn't. Or if it has, I certainly haven't been a part of it. Like I said, we've just met for the first time, you and I.\n"
                jump razor_1_forest

            "{i}• (Explore) Wait... hasn't this already happened?{/i}" if razor_1_forest_share_loop == False:
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_1b.flac"
                n "It hasn't. Or if it has, I certainly haven't been a part of it. We've just met for the first time, you and I.\n"
                jump razor_1_forest_narrator_share_join

            "{i}• (Explore) Okay, no.{/i}" if razor_1_forest_share_loop == False:
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_3a.flac"
                n "Oh, don't you start grandstanding about morals. The fate of the world is at risk right now, and the life of a mere Princess shouldn't stop you from saving us all.\n"
                jump razor_1_forest_narrator_share_join

            "{i}• (Explore) But I died! What am I doing here?{/i}" if razor_1_forest_share_loop == False:
                $ razor_1_forest_share_died = True
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_4.flac"
                n "I can assure you that you're not dead. And to answer your second question, you're here to slay the Princess. I literally told you that a second ago.\n"
                jump razor_1_forest_narrator_share_join

            "{i}• (Explore) She's going to kill me again!{/i}" if razor_1_forest_share_loop == False:
                $ razor_1_forest_share_died = True
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_5.flac"
                n "Again? People don't die twice. You haven't even met the Princess, and I hardly think she'd be capable of killing someone as skilled and courageous as yourself.\n"
                jump razor_1_forest_narrator_share_join

            "{i}• (Explore) But I already slew the Princess. Sure, she {i}also{/i} killed me, but I definitely got her. Why am I here again?{/i}" if current_mutual_death == 1 and razor_1_forest_share_loop == False:
                $ razor_1_forest_share_died = True
                $ razor_1_forest_share_loop = True
                voice "audio/voices/ch2/adversary/narrator/ch2_an_3.flac"
                n "I can assure you that you didn't slay her, and that she didn't kill you. People don't just spring back to life after dying, and the two of us are meeting for the very first time.\n"
                jump razor_1_forest_narrator_share_join

            "{i}• (Explore) Let's assume I'm telling the truth, and all of this really did already happen. Why should I listen to you? Why should I bother doing {i}anything{/i}?{/i}" if razor_1_forest_share_loop and (razor_1_forest_deja_vu == False or (razor_1_forest_deja_vu_follow_up)) and razor_1_forest_share_loop_insist == False:
                $ razor_1_forest_share_loop_insist = True
                $ razor_1_forest_count += 1
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_6.flac"
                n "Those are two very different questions, but fine. I'll indulge you if that's what it takes to get you moving.\n"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_7.flac"
                n "Let's say for a moment that this really is the second time you've met me, or, at least, a version of me.\n"
                if razor_1_forest_share_died == False:
                    voice "audio/voices/ch2/shared/narrator/ch2_share_n_8.flac"
                    n "If you're back here, I'm assuming you died, which probably only happened because you didn't listen to me.\n"
                else:
                    voice "audio/voices/ch2/shared/narrator/ch2_share_n_9.flac"
                    n "You died last time, which probably only happened because you didn't listen to me.\n"
                if razor_revival:
                    voice "audio/voices/ch2/razor/hero/ch2_rh_1.flac"
                    hero "We mostly listened to you. How were we supposed to know she'd spring back to life?\n"
                    voice "audio/voices/ch2/razor/narrator/ch2_rn_3.flac"
                    n "If she 'sprung' back to life in this hypothetical scenario, then clearly you {i}didn't{/i} slay her.\n"
                else:
                    voice "audio/voices/ch2/razor/hero/ch2_rh_2.flac"
                    hero "We did exactly what you said...\n"
                    voice "audio/voices/ch2/razor/narrator/ch2_rn_4.flac"
                    n "Sounds to me like you probably had some kind of elaborate nightmare, in which case I shouldn't be held accountable for what supposedly happened.\n"
                voice "audio/voices/ch2/razor/narrator/ch2_rn_5.flac"
                n "But congratulations. You've been given a chance to actually do this right.\n"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_11.flac"
                n "And I believe your other question was something along the lines of 'what's the point of doing anything?' If you're asking that, it sounds to me like you're making the rather dangerous assumption that your actions last time around didn't have any consequences.\n"
                if current_mutual_death == 1 or loop_1_princess_killed:
                    voice "audio/voices/ch2/razor/hero/ch2_rh_5.flac"
                    hero "What do you mean? Of course there weren't any consequences. We stabbed the Princess, the Princess stabbed us, and now everyone's right back where they started. That sounds pretty consequence-free to me.\n"
                    voice "audio/voices/ch2/shared/narrator/ch2_share_n_12.flac"
                    n "Yes, but, in this purely hypothetical scenario, that begs the question of {i}how{/i} you got back here. Did 'time' simply rewind itself, or were you instead transported to a different world entirely?\n"
                    voice "audio/voices/ch2/shared/narrator/ch2_share_n_12a.flac"
                    n "Had you failed to slay the Princess, what would have happened to everyone in the place you left?\n"
                else:
                    voice "audio/voices/ch2/razor/hero/ch2_rh_4.flac"
                    hero "What do you mean? Of course there weren't any consequences. We were killed by the Princess, and now everyone's right back where they started. That sounds pretty consequence-free to me.\n"
                    voice "audio/voices/ch2/shared/narrator/ch2_share_n_12.flac"
                    n "Yes, but, in this purely hypothetical scenario, that begs the question of {i}how{/i} you got back here. Did 'time' simply rewind itself, or were you instead transported to a different world entirely?\n"
                    voice "audio/voices/ch2/shared/narrator/ch2_share_n_13.flac"
                    n "If it's the latter, what do you think happened {i}after{/i} you died?\n"
                    voice "audio/voices/ch2/shared/narrator/ch2_share_n_13a.flac"
                    n "Do you think the people there lived happily ever after, or do you think that the Princess, left unhindered, brought about the end to everyone and everything, just like I told you she would?\n"
                voice "audio/voices/ch2/razor/cheated/5.flac"
                cheated "Screw this. Who cares what happened to everyone else? She's not going to play fair, so we should do what we can to save ourselves and just {i}get out of here{/i}.\n"
                # re-do
                voice "audio/voices/ch2/razor/narrator/ch2_rn_8.flac"
                n "At least you know not to trust her, but you do realize that 'everything and everyone' includes you, right? If you turn around and leave, you're dooming yourself as well as everyone else.\n"
                if razor_revival:
                    voice "audio/voices/ch2/razor/hero/ch2_rh_6.flac"
                    hero "We were so close to finishing the job last time. She can't get the jump on us twice. If we're careful, we should be fine.\n"
                else:
                    voice "audio/voices/ch2/razor/hero/ch2_rh_7.flac"
                    hero "She just caught us by surprise last time. She can't do that twice. So long as we're careful, we can win this.\n"
                voice "audio/voices/ch2/razor/narrator/ch2_rn_9.flac"
                n "That's the spirit. Just keep that stiff upper lip and you'll save the world in no time at all.\n"
                jump razor_1_forest

            "{i}• (Explore) Let's talk about this Princess...{/i}" if razor_1_forest_share_loop_insist and razor_1_forest_princess_press == False:
                $ razor_1_forest_count += 1
                $ razor_1_forest_princess_press = True
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_14.flac"
                n "Just be quick about it.\n"
                label razor_1_forest_princess:
                    default razor_1_forest_princess_count = 0
                    default razor_1_forest_princess_why_strong = False
                    default razor_1_forest_princess_basement_explain = False
                    default razor_1_forest_princess_why_me = False
                    default razor_1_forest_princess_cagey = False
                    default razor_1_forest_princess_tips = False
                    menu:
                        extend ""

                        "{i}• (Explore) We killed each other last time around. How can I make sure that doesn't happen again?{/i}" if razor_1_forest_princess_tips == False and current_mutual_death == 1:
                            $ razor_1_forest_princess_tips = True
                            $ razor_1_forest_princess_count += 1
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_15.flac"
                            n "Like I said, if she killed you, it was probably because you didn't listen to me. Don't talk to her. Don't trust her. Just go in, do your job, and save the world.\n"
                            voice "audio/voices/ch2/razor/cheated/6.flac"
                            cheated "Oh, and don't get stabbed while you're at it.\n"
                            jump razor_1_forest_princess

                        "{i}• (Explore) All she did last time around was stab me to death. How can someone like that end the world?{/i}" if razor_1_forest_princess_why_strong == False:
                            $ razor_1_forest_princess_why_strong = True
                            $ razor_1_forest_princess_count += 1
                            voice "audio/voices/ch2/razor/narrator/ch2_rn_11.flac"
                            n "She just can. But she's still only a Princess. You're fully up to the task you've been given, so long as you remember that.\n"
                            #voice "audio/voices/ch2/shared/narrator/ch2_share_n_16.flac"
                            #n "She just can. Believe me, I wish I could tell you more, but you'll just have to trust that what I'm saying is true and that, despite it all, you're fully up to the task that's been given to you. Have a little faith in yourself.\n"
                            jump razor_1_forest_princess

                        "{i}• (Explore) Who locked her in that basement? What {b}is{/b} this place?{/i}" if razor_1_forest_princess_basement_explain == False:
                            $ razor_1_forest_princess_basement_explain = True
                            $ razor_1_forest_princess_count += 1
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_18.flac"
                            n "{i}People{/i} locked her in that basement. And I told you what this place is. It's a path in the woods. Don't overcomplicate things.\n"
                            jump razor_1_forest_princess

                        "{i}• (Explore) If people locked her away, why couldn't {b}they{/b} slay her? Why is this falling on me?{/i}" if razor_1_forest_princess_basement_explain and razor_1_forest_princess_why_me == False:
                            $ razor_1_forest_princess_why_me = True
                            $ razor_1_forest_princess_count += 1
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_19.flac"
                            n "Look, I'm not supposed to say this, but it's because you're special. You're the {i}only{/i} person capable of doing this. Call it a prophecy if that helps, but it's just the way things are.\n"
                            voice "audio/voices/ch2/shared/hero/ch2_share_h_2.flac"
                            hero "Oh. I didn't know we were {i}special{/i}.\n"
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_20a.flac"
                            n "Of course you're special. Why else would you be here?\n"
                            if razor_revival:
                                voice "audio/voices/ch2/razor/cheated/7.flac"
                                cheated "If anyone's 'special' here, it's her. Last I checked we can't get up from a knife in the chest.\n"
                            else:
                                voice "audio/voices/ch2/razor/cheated/8.flac"
                                cheated "If anyone's 'special' here, it's her. That was a nasty trick she pulled on us.\n"
                            jump razor_1_forest_princess

                        "{i}• (Explore) You're being cagey. What aren't you telling me?{/i}" if razor_1_forest_princess_cagey == False and razor_1_forest_princess_count > 1:
                            $ razor_1_forest_princess_cagey = True
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_21.flac"
                            n "I've told you everything you need to know, going into more detail would just overcomplicate an otherwise very simple situation and make your job more difficult.\n"
                            voice "audio/voices/ch2/razor/cheated/9.flac"
                            cheated "You didn't tell us about her knife last time though.\n"
                            voice "audio/voices/ch2/razor/narrator/ch2_rn_12.flac"
                            n "That's because she's unarmed, and more than that, it's because there {i}wasn't{/i} a last time.\n"
                            jump razor_1_forest_princess

                        "{i}• Nevermind.{/i}" if razor_1_forest_princess_count == 0:
                            label razor_1_forest_princess_leaving:
                                voice "audio/voices/ch2/shared/narrator/ch2_share_n_24.flac"
                                n "Great. Now if you don't mind, the whole world is waiting with bated breath for you to save it from ruin.\n"
                                jump razor_1_forest

                        "{i}• That's all.{/i}" if razor_1_forest_princess_count != 0:
                            jump razor_1_forest_princess_leaving

            "{i}• [[Proceed to the cabin.]{/i}":
                jump razor_1_cabin_arrival

            "{i}• [[Turn around and leave.]{/i}" if mound_can_attempt_flee:
                if loops_finished >= 2:
                    $ mound_can_attempt_flee = False
                    voice "audio/voices/mound/bonus/flee.flac"
                    mound "You have already committed to my completion. You cannot go further astray.\n"
                    jump razor_1_forest
                voice "audio/voices/ch2/razor/cheated/10.flac"
                cheated "Heh. And away we go. Good call.\n"
                jump turn_and_leave_join

label razor_1_cabin_arrival:
    $ quick_menu = False
    play audio "audio/one_shot/footsteps_hike_short.flac"
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
    voice "audio/voices/ch2/razor/cheated/11.flac"
    cheated "He couldn't be more on the money. But we're really doing this, aren't we? I'd say your loss, but I'm stuck here with you.\n"
    #cheated "He couldn't be more on the money. But we're really doing this, aren't we? I'd say your loss, but I'm stuck here with you. All right, fine. Let's make her hurt for what she did to us.\n"
    voice "audio/voices/ch2/razor/hero/ch2_rh_9.flac"
    hero "We know what to look out for this time. We know to be careful.\n"
    voice "audio/voices/ch2/razor/narrator/ch2_rn_13.flac"
    n "Just stay focused and you'll be fine.\n"
    menu:
        extend ""

        "{i}• [[Proceed into the cabin.]{/i}":
            label razor_stranger_rejoin:
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

    $ gallery_razor.unlock_item(1)
    $ renpy.save_persistent()
    voice "audio/voices/ch2/razor/narrator/ch2_rn_14.flac"
    play sound "audio/looping/ambient_cabin.ogg" loop fadein 1.0
    play music "audio/_music/ch2/razor/The Razor.flac" loop
    play secondary "audio/looping/uncomfortable ambiance heightened.ogg" loop
    scene farback interior cabin onlayer farback at Position(ypos=1125)
    show bg razor cabin onlayer back at Position(ypos=1125)
    show door razor1 onlayer back at Position(ypos=1125)
    show table razor onlayer back at Position(ypos=1125)
    show knife razor onlayer back at Position(ypos=1125)
    show mirror base onlayer back at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    n "The interior of the cabin is a jagged mess of warped wood and broken boards, their splintered edges as uninviting as shattered glass. The only furniture of note is a pointed table with a pristine blade perched on its edge.\n"
    voice "audio/voices/ch2/shared/narrator/ch2_share_n_25.flac"
    n "The blade is your implement. You'll need it if you want to do this right.\n"
    label cabin_interior_2_razor_menu:
        default razor_1_cabin_mirror_present = True
        default razor_1_cabin_blade_taken = False
        default razor_1_cabin_mirror_ask = False
        default razor_1_cabin_mirror_approached = False
        default razor_1_cabin_last_time_comment = False
        menu:
            extend ""

            "{i}• (Explore) You didn't say anything about the mirror on the wall.{/i}" if razor_1_cabin_mirror_ask == False and razor_1_cabin_mirror_present:
                $ razor_1_cabin_mirror_ask = True
                $ current_run_mirror_comment = True
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_26.flac"
                n "That's because there isn't a mirror. There's a table, the blade sitting on the table, and the door to the basement. There's nothing else in here.\n"
                voice "audio/voices/ch2/shared/hero/ch2_share_h_4.flac"
                hero "There's definitely a mirror.\n"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_27.flac"
                n "There isn't.\n"
                voice "audio/voices/ch2/razor/cheated/12.flac"
                cheated "Can you two stop arguing? It's stressful enough in here without all of this extra noise.\n"
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
                        $ razor_1_cabin_mirror_present = False
                        voice "audio/voices/ch2/shared/hero/ch2_share_h_5.flac"
                        hero "But it {i}does{/i} matter! Don't you care if we're being lied to? If He's willing to lie about something as innocuous as a mirror, what else is He hiding from us?\n"
                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_30.flac"
                        hide mirror onlayer back
                        n "I'm not lying to you. Use your eyes, there is no mirror. Why would I lie about something so meaningless? What good would a mirror even do? Let you waste time preening yourself instead of doing what needs to be done?\n"
                        voice "audio/voices/ch2/shared/hero/ch2_share_h_6.flac"
                        hero "But there {i}was{/i} a mirror a second ago.\n"
                        voice "audio/voices/ch2/razor/cheated/13.flac"
                        cheated "And now it's gone. Yet another thing in here playing tricks on us. I hate this place.\n"

                    "{i}• [[Remain silent.]{/i}":
                        voice "audio/voices/ch2/shared/hero/ch2_share_h_7b.flac"
                        hero "I care about whether we're being lied to. If He's willing to lie about something as innocuous as a mirror, what else could He hiding from us?\n"
                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_31.flac"
                        n "I'm not lying to you, I {i}promise{/i}. There isn't a mirror. Really.\n"

                    "{i}• [[Approach the mirror.]{/i}" if razor_1_cabin_mirror_approached == False:
                        label razor_cabin_1_mirror_join:
                            $ razor_1_cabin_mirror_approached = True
                            play audio "audio/one_shot/footsteps_creaky.flac"
                            hide farback onlayer farback
                            hide bg onlayer back
                            hide door onlayer back
                            hide table onlayer back
                            hide knife onlayer back
                            hide mirror onlayer back
                            scene bg razor mirror onlayer front at Position(ypos=1125)
                            show mirror razor close onlayer front at Position(ypos=1125)
                            with dissolve
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_32.flac"
                            n "You walk up to the wall next to the basement door. It's a wall. There isn't much to see here.\n"
                            if razor_1_cabin_mirror_ask == False:
                                voice "audio/voices/ch2/shared/hero/ch2_share_h_8.flac"
                                hero "What are you talking about? This isn't a wall. It's a mirror. Or at least it'll {i}be{/i} a mirror once we wipe off that layer of grime.\n"
                            else:
                                voice "audio/voices/ch2/shared/hero/ch2_share_h_9.flac"
                                hero "This really isn't funny.\n"
                            $ current_run_mirror_touched = True
                            menu:
                                extend ""

                                "{i}• [[Wipe the mirror clean.]{/i}":
                                    $ razor_1_cabin_mirror_present = False
                                    hide mirror onlayer front
                                    play audio "audio/one_shot/new/STP_claws_1.flac"
                                    show player wall onlayer front at Position(ypos=1125) with dissolve
                                    if razor_1_cabin_mirror_ask == False:
                                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_33.flac"
                                    else:
                                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_33a.flac"
                                    n "You reach forward and rub your hand against the cabin wall. I hope you know how ridiculous you look right now.\n"
                                    hide player onlayer front with dissolve
                                    if razor_1_cabin_mirror_ask:
                                        voice "audio/voices/ch2/shared/hero/ch2_share_h_10.flac"
                                        hero "But it was there a second ago!\n"
                                    else:
                                        voice "audio/voices/ch2/shared/hero/ch2_share_h_6.flac"
                                        hero "But there was a mirror a second ago.\n"
                                    voice "audio/voices/ch2/razor/cheated/13.flac"
                                    cheated "And now it's gone. Yet another thing in here playing tricks on us. I hate this place.\n"
                                    play audio "audio/one_shot/footsteps_creaky.flac"
                                    hide bg onlayer front
                                    scene farback interior cabin onlayer farback at Position(ypos=1125)
                                    show bg razor cabin onlayer back at Position(ypos=1125)
                                    show door razor1 onlayer back at Position(ypos=1125)
                                    show table razor onlayer back at Position(ypos=1125)
                                    if razor_1_cabin_blade_taken == False:
                                        show knife razor onlayer back at Position(ypos=1125)
                                    with dissolve
                                    jump cabin_interior_2_razor_menu

                jump cabin_interior_2_razor_menu

            "{i}• (Explore) This whole cabin is different than last time.{/i}" if razor_1_cabin_last_time_comment == False and razor_1_forest_share_loop_insist:
                $ razor_1_cabin_last_time_comment = True
                voice "audio/voices/ch2/shared/hero/ch2_share_h_11.flac"
                hero "{i}Very{/i} different.\n"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_34.flac"
                n "Maybe that's because you haven't actually been here. I hope this means you'll finally drop that ridiculous past-life nonsense. You haven't died, and you certainly haven't been killed by the Princess.\n"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_35.flac"
                n "So focus up. A lot's riding on this.\n"
                jump cabin_interior_2_razor_menu

            "{i}• (Explore) [[Approach the mirror.]{/i}" if razor_1_cabin_mirror_present and razor_1_cabin_mirror_approached == False:
                $ razor_1_cabin_mirror_approached = True
                jump razor_cabin_1_mirror_join

            "{i}• (Explore) [[Take the blade.]{/i}" if razor_1_cabin_blade_taken == False:
                $ razor_1_cabin_blade_taken = True
                $ blade_held = True
                $ default_mouse = "blade"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_36.flac"
                play audio "audio/one_shot/knife_pickup.flac"
                hide knife onlayer back
                with dissolve
                n "You take the blade from the table. It would be difficult to slay the Princess and save the world without a weapon.\n"
                voice "audio/voices/ch2/razor/cheated/14.flac"
                cheated "It feels a bit better to have a weapon in our hands. Let's make her hurt for what she's done to us.\n"
                jump cabin_interior_2_razor_menu

            "{i}• [[Enter the basement.]{/i}":
                if razor_1_cabin_blade_taken == False:
                    voice "audio/voices/ch2/razor/cheated/15.flac"
                    cheated "Are we really doing this without a weapon? You know she has one, right?\n"
                    if razor_1_forest_share_loop:
                        voice "audio/voices/ch2/razor/narrator/ch2_rn_16.flac"
                        n "Once again, I'd like to remind you that she's unarmed. But you're right. This would be a lot easier if you had the blade. I hope you know what you're doing.\n"
                # get to da basement.
                $ quick_menu = False
                play audio "audio/one_shot/door_bedroom.flac"
                show door razor2 onlayer back at Position(ypos=1125)
                with Dissolve(0.5)
                hide mirror onlayer back
                show door razor3 onlayer back at Position(ypos=1125) with Dissolve(0.5)
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

                voice "audio/voices/ch2/razor/narrator/ch2_rn_17.flac"
                play audio "audio/one_shot/new/STP_swordscrape_3.flac"
                scene bg razor stairs onlayer back at Position(ypos=1125)
                with fade
                if persistent.quick_menu:
                    $ quick_menu = True
                n "The door to the basement creaks open, revealing what must once have been stairs. The fractured slats look as if they've been torn from their source and violently jammed into the wall.\n"
                voice "audio/voices/ch2/razor/narrator/ch2_rn_17a.flac"
                n "The air seeping up from below has an almost metallic quality to it. Like the smell of fresh blood. And you can hear what sounds like the rhythmic scraping of metal coming from down below. If the Princess lives here, slaying her would probably be doing her a favor.\n"
                play audio "audio/one_shot/new/STP_swordscrape_2.flac"
                if razor_1_forest_share_loop:
                    voice "audio/voices/ch2/razor/cheated/16.flac"
                    cheated "That's right, {i}scraping{/i}. I told you she has something. I {i}told{/i} you.\n"
                else:
                    voice "audio/voices/ch2/razor/cheated/17.flac"
                    cheated "Scraping? She's not even trying to hide her knife. It's like she wants to get in our head.\n"
                voice "audio/voices/ch2/razor/narrator/ch2_rn_18.flac"
                n "That sound could be anything. It's probably just her chains dragging across the floor. I am begging you to get out of your head.\n"
                play audio "audio/one_shot/new/STP_swordscrape_4.flac"
                voice "audio/voices/ch2/razor/narrator/ch2_rn_19.flac"
                n "Her grating voice carries up the stairs.\n"
                voice "audio/voices/ch2/razor/princess/ch2_rp_1.flac"
                sp "I hope you've come to rescue me. I've been stuck down here {i}forever{/i}.\n"
                voice "audio/voices/ch2/razor/hero/ch2_rh_9a.flac"
                hero "There's something so wrong with that voice.\n"
                voice "audio/voices/ch2/razor/cheated/18.flac"
                cheated "Yeah. She thinks she's better than us. Like she doesn't even have to put on an act this time.\n"
                $ gallery_razor.unlock_item(2)
                $ renpy.save_persistent()
                play audio "audio/one_shot/footsteps_creaky.flac"
                $ quick_menu = False
                stop secondary fadeout 1.0
                hide bg onlayer back
                with fade
                scene farback razor basement onlayer farback at Position(ypos=1125)
                show bg razor basement onlayer back at Position(ypos=1125)
                show razor d neutral onlayer back at Position(ypos=1125)
                with fade
                if persistent.quick_menu:
                    $ quick_menu = True
                voice "audio/voices/ch2/razor/narrator/ch2_rn_20.flac"
                n "As you descend the final step, the form of the Princess comes into view, her sharp eyes following you from across the room.\n"
                if razor_1_forest_share_loop:
                    voice "audio/voices/ch2/razor/hero/ch2_rh_10.flac"
                    hero "I wonder if she remembers us.\n"
                show razor d plead onlayer back with dissolve
                voice "audio/voices/ch2/razor/princess/ch2_rp_2.flac"
                sp "Finally, {i}somebody{/i}! Quick, get me out of these chains, we're not safe here.\n"
                voice "audio/voices/ch2/razor/cheated/19.flac"
                show razor d cheeky onlayer back with dissolve
                cheated "Come on, now. We're not falling for that, are we? She's trying to trick us, but she can't hide that threatening edge to her voice. She just wants us to get close, to let our guard down.\n"
                if razor_1_cabin_blade_taken:
                    voice "audio/voices/ch2/razor/narrator/ch2_rn_21.flac"
                    n "If she sounds threatening, it's because her mask is already slipping. She knows why you're here. You {i}are{/i} armed, after all.\n"
                else:
                    voice "audio/voices/ch2/razor/narrator/ch2_rn_22.flac"
                    n "Exactly. She sounds threatening because her mask is already slipping. She knows why you're here.\n"
                show razor d cheeky talk onlayer back with dissolve
                voice "audio/voices/ch2/razor/princess/ch2_rp_3.flac"
                sp "What are you waiting for? You are here to rescue me, right?\n"
                show razor d cheeky onlayer back with dissolve
                jump razor_1_basement_menu


return
