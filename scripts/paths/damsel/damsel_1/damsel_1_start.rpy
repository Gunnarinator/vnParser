label damsel_1_start:
    $ blade_held = False
    $ trait_smitten = True
    $ quick_menu = False
    play sound "audio/looping/uncomfortable ambiance.ogg" loop fadein 1.0
    scene chapter damsel with fade
    show text _("{color=#FFFFFF00}Chapter Two. The Damsel.{/color}") at Position(ypos=850)
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
    $ gallery_damsel.unlock_gallery()
    $ gallery_zch1.unlock_item(6)
    $ renpy.save_persistent()
    voice "audio/voices/ch1/woods/narrator/script_n_1.flac"
    n "You're on a path in the woods. And at the end of that path is a cabin. And in the basement of that cabin is a Princess.\n"
    voice "audio/voices/ch1/woods/narrator/script_n_2.flac"
    n "You're here to slay her.\n If you don't, it will be the end of the world.\n"
    label damsel_1_forest:
        default damsel_1_forest_count = 0
        default damsel_1_forest_share_died = False
        default damsel_1_forest_share_loop = False
        default damsel_1_forest_princess_press = False
        default damsel_1_forest_share_loop_insist = False
        default damsel_1_forest_deja_vu = False
        default damsel_1_forest_deja_vu_follow_up = False
        menu:
            extend ""

            "{i}• (Explore) I'm getting a terrible sense of deja vu.{/i}" if damsel_1_forest_share_loop == False:
                $ damsel_1_forest_deja_vu = True
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_1a.flac"
                n "A terrible sense of deja vu? No, you don't have that. This is the first time either of us have been here.\n"
                label damsel_1_forest_narrator_share_join:
                    $ damsel_1_forest_count += 1
                    $ damsel_1_forest_share_loop = True
                    voice "audio/voices/ch2/shared/hero/ch2_share_h_1.flac"
                    hero "If He doesn't remember what happened, then maybe it's best to keep it that way.\n"
                    voice "audio/voices/ch2/damsel/smitten/ch2_smitten_1.flac"
                    smitten "Yes, He didn't approve of us last time, did He? If we're going to save our beloved, we'll have to be sneaky about it.\n"
                    voice "audio/voices/ch2/damsel/hero/ch2_dh_1.flac"
                    hero "Our... 'beloved?'\n"
                    voice "audio/voices/ch2/damsel/narrator/ch2_dn_1.flac"
                    n "Yes, you'll have to be {i}very{/i} sneaky about your intentions if you're going to try and save the Princess.\n"
                    #voice "audio/voices/ch2/damsel/narrator/ch2_dn_1old.flac"
                    #n "Yes, you'll have to be {i}very{/i} sneaky about your intentions if you're going to try and save the Princess. Which, in case it isn't clear, is the exact opposite of what you should be doing.\n"
                    voice "audio/voices/ch2/damsel/smitten/ch2_smitten_2.flac"
                    smitten "Ah, so all of the cards are on the table. Then you should know that we and the Princess are in love and the four of us will be foiling any and all assassination attempts you've got in the works.\n"
                    voice "audio/voices/ch2/damsel/narrator/ch2_dn_2a.flac"
                    n "We'll see about that. Whatever you do, just be sure to ignore {i}him{/i}, specifically. It sounds like he's the sort who'd sacrifice the whole world for a peck on the cheek.\n"
                    voice "audio/voices/ch2/damsel/smitten/ch2_smitten_3.flac"
                    smitten "What can I say? A world without love is a world that isn't worth saving.\n"
                    jump damsel_1_forest

            "{i}• (Explore) This is more than just deja vu, though. I'm pretty sure this whole thing literally just happened.{/i}" if damsel_1_forest_deja_vu and damsel_1_forest_deja_vu_follow_up == False:
                $ damsel_1_forest_deja_vu_follow_up = True
                $ damsel_1_forest_count += 1
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_2.flac"
                n "We could go back and forth on this forever, and it won't get you any closer to doing your job and saving the world. So let's just agree to disagree.\n"
                jump damsel_1_forest

            "{i}• (Explore) Wait... hasn't this already happened?{/i}" if damsel_1_forest_share_loop == False:
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_1b.flac"
                n "It hasn't. Or if it has, I certainly haven't been a part of it. We've just met for the first time, you and I.\n"
                jump damsel_1_forest_narrator_share_join

            "{i}• (Explore) Okay, no.{/i}" if damsel_1_forest_share_loop == False:
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_3a.flac"
                n "Oh, don't you start grandstanding about morals. The fate of the world is at risk right now, and the life of a mere Princess shouldn't stop you from saving us all.\n"
                jump damsel_1_forest_narrator_share_join

            "{i}• (Explore) But I died! What am I doing here?{/i}" if damsel_1_forest_share_loop == False:
                $ damsel_1_forest_share_died = True
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_4.flac"
                n "I can assure you that you're not dead. And to answer your second question, you're here to slay the Princess. I literally told you that a second ago.\n"
                jump damsel_1_forest_narrator_share_join

            "{i}• (Explore) Oh, you bastard! You're in for it now. I'm wise to your tricks!{/i}" if damsel_1_forest_share_loop == False:
                $ damsel_1_forest_share_died = True
                voice "audio/voices/ch2/damsel/narrator/ch2_dn_3.flac"
                n "My tricks? What on earth are you talking about? We've just met for the first time.\n"
                jump damsel_1_forest_narrator_share_join

            "{i}• (Explore) Let's assume I'm telling the truth, and all of this really did already happen. Why should I listen to you? Why should I bother doing {i}anything{/i}?{/i}" if damsel_1_forest_share_loop and (damsel_1_forest_deja_vu == False or (damsel_1_forest_deja_vu_follow_up)) and damsel_1_forest_share_loop_insist == False:
                $ damsel_1_forest_share_loop_insist = True
                $ damsel_1_forest_count += 1
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_6.flac"
                n "Those are two very different questions, but fine. I'll indulge you if that's what it takes to get you moving.\n"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_7.flac"
                n "Let's say for a moment that this really is the second time you've met me, or, at least, a version of me.\n"
                if damsel_1_forest_share_died == False:
                    voice "audio/voices/ch2/shared/narrator/ch2_share_n_8.flac"
                    n "If you're back here, I'm assuming you died, which probably only happened because you didn't listen to me.\n"
                else:
                    voice "audio/voices/ch2/shared/narrator/ch2_share_n_9.flac"
                    n "You died last time, which probably only happened because you didn't listen to me.\n"
                voice "audio/voices/ch2/damsel/smitten/ch2_smitten_4.flac"
                smitten "{i}You{/i} were the one who did us in, villain.\n"
                voice "audio/voices/ch2/damsel/hero/ch2_dh_2.flac"
                hero "Well, not you in the literal sense, but you did everything you could to stop us from rescuing her.\n"
                voice "audio/voices/ch2/damsel/narrator/ch2_dn_4.flac"
                n "Oh, I wonder why. Maybe it's because the entire world was at stake. No lone Princess is worth that price.\n"
                voice "audio/voices/ch2/damsel/smitten/ch2_smitten_5.flac"
                smitten "I beg to differ.\n"
                voice "audio/voices/ch2/damsel/narrator/ch2_dn_5.flac"
                n "I'm not going to argue with you. I'm just going to take a deep breath and assume that whoever is making the decisions here has the common sense to {i}ignore{/i} your protestations.\n"
                voice "audio/voices/ch2/damsel/narrator/ch2_dn_6.flac"
                n "Anyways, I believe your second question was 'what's the point of doing anything?' If you're asking that, it sounds to me like you're making the rather dangerous assumption that your actions last time around didn't have any consequences.\n"
                voice "audio/voices/ch2/damsel/hero/ch2_dh_3.flac"
                hero "What do you mean? Of course there weren't any consequences. You forced the Princess to kill us, and now everyone's right back to where they started. That sounds pretty consequence-free to me.\n"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_12.flac"
                n "Yes, but, in this purely hypothetical scenario, that begs the question of {i}how{/i} you got back here. Did 'time' simply rewind itself, or were you instead transported to a different world entirely?\n"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_13.flac"
                n "If it's the latter, what do you think happened {i}after{/i} you died?\n"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_13a.flac"
                n "Do you think the people there lived happily ever after, or do you think that the Princess, left unhindered, brought about the end to everyone and everything, just like I told you she would?\n"
                voice "audio/voices/ch2/damsel/smitten/ch2_smitten_6.flac"
                smitten "She would never. She's a perfect angel that you cruelly imprisoned as part of some convoluted, dastardly scheme.\n"
                voice "audio/voices/ch2/damsel/narrator/ch2_dn_8.flac"
                n "Convoluted? I don't know how this premise could be any more simple. Princess bad. Stop her. Save everyone.\n"
                jump damsel_1_forest

            "{i}• (Explore) I'm with them. I'm going to find a way to save her from that cabin.{/i}" if damsel_1_forest_share_loop_insist and damsel_1_forest_defy == False:
                default damsel_1_forest_defy = False
                $ damsel_1_forest_defy = True
                voice "audio/voices/ch2/damsel/hero/ch2_dh_4.flac"
                hero "That's right. You can't stop all of us.\n"
                voice "audio/voices/ch2/damsel/smitten/ch2_smitten_7.flac"
                smitten "We're going to sweep her off her feet if it's the last thing anyone does.\n"
                voice "audio/voices/ch2/damsel/narrator/ch2_dn_9.flac"
                n "Are these really the sorts of people you'd like to align yourself with? {i}Sigh{/i}. You're not at the cabin yet. You still have plenty of time to reflect on the situation. I just hope for all our sakes that you make the right call.\n"
                jump damsel_1_forest

            "{i}• (Explore) Let's talk about this Princess...{/i}" if damsel_1_forest_share_loop_insist and damsel_1_forest_princess_press == False:
                $ damsel_1_forest_count += 1
                $ damsel_1_forest_princess_press = True
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_14.flac"
                n "Just be quick about it.\n"
                label damsel_1_forest_princess:
                    default damsel_1_forest_princess_count = 0
                    default damsel_1_forest_princess_why_strong = False
                    default damsel_1_forest_princess_basement_explain = False
                    default damsel_1_forest_princess_why_me = False
                    default damsel_1_forest_princess_cagey = False
                    default damsel_1_forest_princess_tips = False
                    menu:
                        extend ""

                        "{i}• (Explore) The only reason she was even able to kill me last time was because I let her. She could barely hold a knife. How is she supposed to end the world?{/i}" if damsel_1_forest_princess_why_strong == False:
                            $ damsel_1_forest_princess_why_strong = True
                            $ damsel_1_forest_princess_count += 1
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_16a.flac"
                            n "She just can. Believe me, I wish I could tell you more, but you'll just have to trust that what I'm saying is true and that, despite it all, you're fully up to the task that's been given to you.\n"
                            voice "audio/voices/ch2/damsel/smitten/ch2_smitten_8a.flac"
                            smitten "Maybe it's her {i}beauty{/i} that threatens the world.\n"
                            voice "audio/voices/ch2/damsel/narrator/ch2_dn_11a.flac"
                            n "Sure. It's her beauty. Why not? And before you ask, no. We can't just keep her down there. If you don't slay her, she's going to find a way out. It's unfortunate, I know, but it's just the way it is.\n"
                            jump damsel_1_forest_princess

                        "{i}• (Explore) Who locked her in that basement? What {b}is{/b} this place?{/i}" if damsel_1_forest_princess_basement_explain == False:
                            $ damsel_1_forest_princess_basement_explain = True
                            $ damsel_1_forest_princess_count += 1
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_18.flac"
                            n "{i}People{/i} locked her in that basement. And I told you what this place is. It's a path in the woods. Don't overcomplicate things.\n"
                            jump damsel_1_forest_princess

                        "{i}• (Explore) If people locked her away, why couldn't {b}they{/b} slay her? Why is this falling on me?{/i}" if damsel_1_forest_princess_basement_explain and damsel_1_forest_princess_why_me == False:
                            $ damsel_1_forest_princess_why_me = True
                            $ damsel_1_forest_princess_count += 1
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_19.flac"
                            n "Look, I'm not supposed to say this, but it's because you're special. You're the {i}only{/i} person capable of doing this. Call it a prophecy if that helps, but it's just the way things are.\n"
                            voice "audio/voices/ch2/shared/hero/ch2_share_h_2.flac"
                            hero "Oh. I didn't know we were {i}special{/i}.\n"
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_20a.flac"
                            n "Of course you're special. Why else would you be here?\n"
                            voice "audio/voices/ch2/damsel/smitten/ch2_smitten_9.flac"
                            smitten "Calling us special isn't going to make us friends, even if it did feel nice.\n"
                            voice "audio/voices/ch2/damsel/narrator/ch2_dn_12.flac"
                            n "Oh, believe me, the last thing I want is for you and I to be {i}friends{/i}. But I'm a professional, and I'm not going to let my dislike for you get in the way of helping you save the world.\n"
                            jump damsel_1_forest_princess

                        "{i}• (Explore) You're being cagey. What aren't you telling me?{/i}" if damsel_1_forest_princess_cagey == False and damsel_1_forest_princess_count > 1:
                            $ damsel_1_forest_princess_cagey = True
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_21.flac"
                            n "I've told you everything you need to know, going into more detail would just overcomplicate an otherwise very simple situation and make your job more difficult.\n"
                            if damsel_1_forest_princess_count < 2:
                                voice "audio/voices/ch2/shared/narrator/ch2_share_n_22.flac"
                                n "The less you know about her, the better.\n"
                            else:
                                voice "audio/voices/ch2/shared/narrator/ch2_share_n_23.flac"
                                n "Not to sound like a broken record, but the less you know about her, the better things will go for all of us. I know it sounds like I'm hiding something, but you're just going to have to take me at my word.\n"
                            jump damsel_1_forest_princess

                        "{i}• Nevermind.{/i}" if damsel_1_forest_princess_count == 0:
                            label damsel_1_forest_princess_leaving:
                                voice "audio/voices/ch2/shared/narrator/ch2_share_n_24.flac"
                                n "Great. Now if you don't mind, the whole world is waiting with bated breath for you to save it from ruin.\n"
                                jump damsel_1_forest

                        "{i}• That's all.{/i}" if damsel_1_forest_princess_count != 0:
                            jump damsel_1_forest_princess_leaving

            "{i}• [[Proceed to the cabin.]{/i}":
                jump damsel_1_cabin_arrival

            "{i}• [[Turn around and leave.]{/i}" if mound_can_attempt_flee:
                if loops_finished >= 2:
                    $ mound_can_attempt_flee = False
                    voice "audio/voices/mound/bonus/flee.flac"
                    mound "You have already committed to my completion. You cannot go further astray.\n"
                    jump damsel_1_forest
                voice "audio/voices/ch2/damsel/smitten/ch2_smitten_10a.flac"
                smitten "Are we running away? What are you doing, we have to save her!\n"
                jump turn_and_leave_join

label damsel_1_cabin_arrival:
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
    if damsel_1_forest_share_loop == False:
        voice "audio/voices/ch2/damsel/smitten/ch2_smitten_11.flac"
        smitten "If only you knew what you did to us, you villain.\n"
        voice "audio/voices/ch2/damsel/narrator/ch2_dn_13.flac"
        n "Excuse me?\n"
        voice "audio/voices/ch2/damsel/hero/ch2_dh_5.flac"
        hero "Forget he said anything.\n"
        voice "audio/voices/ch2/damsel/smitten/ch2_smitten_12.flac"
        smitten "But He {i}is{/i} a villain. He made our beloved brutally take our life last time. He's trying to keep us apart, but He won't be able to withstand the power of our love!\n"
        voice "audio/voices/ch2/damsel/narrator/ch2_dn_14.flac"
        n "Last time? What are you talking about?\n"
        voice "audio/voices/ch2/damsel/hero/ch2_dh_6.flac"
        hero "I think he just likes to hear the sound of his own voice. Let's try to ignore him.\n"
    else:
        voice "audio/voices/ch2/damsel/smitten/ch2_smitten_13.flac"
        smitten "We already told you we're not playing along with your little game, it's your lies that can't be trusted. Her beauty is the only thing in the world we {i}can{/i} believe in!\n"
        voice "audio/voices/ch2/damsel/hero/ch2_dh_7.flac"
        hero "I think we've already been over this. I'm pretty sure he just likes the sound of his own voice.\n"
    voice "audio/voices/ch2/damsel/smitten/ch2_smitten_14.flac"
    smitten "I do, but I also speak from the heart. My passions are too great to be stifled, they must be expressed!\n"
    voice "audio/voices/ch2/damsel/hero/ch2_dh_8.flac"
    hero "Sure, yeah, your passions are strong and all, but not everyone needs to hear them. Some things are better kept quiet.\n"
    voice "audio/voices/ch2/damsel/narrator/ch2_dn_15.flac"
    n "Don't pay their bickering any mind. Focus on the task ahead.\n"
    menu:
        extend ""

        "{i}• [[Proceed into the cabin.]{/i}":
            label damsel_stranger_rejoin:
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
                scene bg black
                #show loading_icon
                with fade

    $ gallery_damsel.unlock_item(1)
    $ renpy.save_persistent()

    voice "audio/voices/ch2/damsel/narrator/ch2_dn_16.flac"
    $ renpy.music.set_volume(0.0, 0.0, channel='music2')
    $ renpy.music.set_volume(0.0, 0.0, channel='music3')
    $ renpy.music.set_volume(0.0, 0.0, channel='music4')
    $ renpy.music.set_volume(0.0, 0.0, channel='music5')
    play sound "audio/looping/ambient_cabin.ogg" loop fadein 1.0
    play music "audio/_music/ch2/damsel/The Damsel.flac" loop
    play music2 "audio/_music/ch2/damsel/The Damsel Master DR1 LOOP.flac" loop
    play music3 "audio/_music/ch2/damsel/The Damsel Master DR2 LOOP.flac" loop
    play music4 "audio/_music/ch2/damsel/The Damsel Master DR3 LOOP.flac" loop
    play music5 "audio/_music/ch2/damsel/The Damsel Master DR4 LOOP.flac" loop
    scene farback damsel cabin onlayer farback at Position(ypos=1125)
    show bg damsel cabin onlayer back at Position(ypos=1125)
    show door damsel1 onlayer back at Position(ypos=1125)
    show table damsel onlayer back at Position(ypos=1125)
    show knife damsel onlayer back at Position(ypos=1125)
    show mirror base onlayer back at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    n "The interior of the cabin is clean and elegant, its stone walls draped in fine-threaded tapestries, a prison befitting a royal prisoner. The only furniture of note is an ornate wooden table with a pristine blade perched on its edge.\n"
    voice "audio/voices/ch2/shared/narrator/ch2_share_n_25.flac"
    n "The blade is your implement. You'll need it if you want to do this right.\n"
    label cabin_interior_2_damsel_menu:
        default damsel_1_cabin_mirror_present = True
        default damsel_1_cabin_blade_taken = False
        default damsel_1_cabin_mirror_ask = False
        default damsel_1_cabin_mirror_approached = False
        default damsel_1_cabin_last_time_comment = False
        menu:
            extend ""

            "{i}• (Explore) You didn't say anything about the mirror on the wall.{/i}" if damsel_1_cabin_mirror_ask == False and damsel_1_cabin_mirror_present:
                $ damsel_1_cabin_mirror_ask = True
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_26.flac"
                n "That's because there isn't a mirror. There's a table, the blade sitting on the table, and the door to the basement. There's nothing else in here.\n"
                voice "audio/voices/ch2/shared/hero/ch2_share_h_4.flac"
                hero "There's definitely a mirror.\n"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_27.flac"
                n "There isn't.\n"
                voice "audio/voices/ch2/damsel/smitten/ch2_smitten_15.flac"
                smitten "I'm sure the Princess would tell us there was a mirror if {i}she{/i} were up here.\n"
                voice "audio/voices/ch2/damsel/narrator/ch2_dn_17.flac"
                n "In which case she'd be lying to you, because again, there isn't a mirror.\n"
                menu:
                    extend ""

                    "{i}• Why {b}would{/b} you lie about that? What's the point?{/i}":
                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_28.flac"
                        n "Exactly. Why would I lie about something so meaningless? What good would a mirror even do? Let you waste time preening yourself instead of doing what needs to be done?\n"

                    "{i}• I want to look at myself. I want to see how {b}handsome{/b} I am.{/i}":
                        voice "audio/voices/ch2/damsel/smitten/ch2_smitten_16.flac"
                        smitten "That's a great idea. We have to make sure we're looking our best before we save her.\n"
                        voice "audio/voices/ch2/damsel/hero/ch2_dh_9.flac"
                        hero "We shouldn't waste time {i}preening{/i}, but if He {i}is{/i} lying about the mirror, it might be important.\n"
                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_29.flac"
                        n "I'm not lying to you. Use your eyes, there is no mirror. Why would I lie about something so meaningless? What good would it even do?\n"

                    "{i}• It doesn't matter.{/i}":
                        $ damsel_1_cabin_mirror_present = False
                        voice "audio/voices/ch2/shared/hero/ch2_share_h_5.flac"
                        hero "But it {i}does{/i} matter! Don't you care if we're being lied to? If He's willing to lie about something as innocuous as a mirror, what else is He hiding from us?\n"
                        hide mirror onlayer back
                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_30.flac"
                        n "I'm not lying to you. Use your eyes, there is no mirror. Why would I lie about something so meaningless? What good would a mirror even do? Let you waste time preening yourself instead of doing what needs to be done?\n"
                        voice "audio/voices/ch2/shared/hero/ch2_share_h_6.flac"
                        hero "But there {i}was{/i} a mirror a second ago.\n"
                        voice "audio/voices/ch2/damsel/smitten/ch2_smitten_17.flac"
                        smitten "And now it's gone. Pity. We could have a feather out of place and now we'll never know. We can't gallantly sweep her off her feet if we have a feather out of place.\n"

                    "{i}• [[Remain silent.]{/i}":
                        voice "audio/voices/ch2/shared/hero/ch2_share_h_7b.flac"
                        hero "I care if we're being lied to. If He's willing to lie about something as innocuous as a mirror, what else could He hiding from us?\n"
                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_31.flac"
                        n "I'm not lying to you, I {i}promise{/i}. There isn't a mirror. Really.\n"

                    "{i}• [[Approach the mirror.]{/i}" if damsel_1_cabin_mirror_approached == False:
                        label damsel_cabin_1_mirror_join:
                            play audio "audio/one_shot/footsteps_creaky.flac"
                            hide farback onlayer farback
                            hide bg onlayer back
                            hide door onlayer back
                            hide table onlayer back
                            hide knife onlayer back
                            hide mirror onlayer back
                            scene bg damsel mirror onlayer front at Position(ypos=1125)
                            show mirror damsel close onlayer front at Position(ypos=1125)
                            with dissolve
                            $ damsel_1_cabin_mirror_approached = True
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_32.flac"
                            n "You walk up to the wall next to the basement door. It's a wall. There isn't much to see here.\n"
                            if damsel_1_cabin_mirror_ask == False:
                                voice "audio/voices/ch2/shared/hero/ch2_share_h_8.flac"
                                hero "What are you talking about? This isn't a wall. It's a mirror. Or at least it'll {i}be{/i} a mirror once we wipe off that layer of grime.\n"
                            else:
                                voice "audio/voices/ch2/shared/hero/ch2_share_h_9.flac"
                                hero "This really isn't funny.\n"
                            menu:
                                extend ""

                                "{i}• [[Wipe the mirror clean.]{/i}":
                                    $ damsel_1_cabin_mirror_present = False
                                    hide mirror onlayer front
                                    play audio "audio/one_shot/new/STP_claws_1.flac"
                                    show player wall onlayer front at Position(ypos=1125) with dissolve
                                    if damsel_1_cabin_mirror_ask == False:
                                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_33.flac"
                                    else:
                                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_33a.flac"
                                    n "You reach forward and rub your hand against the cabin wall. I hope you know how ridiculous you look right now.\n"
                                    hide player onlayer front with dissolve
                                    if damsel_1_cabin_mirror_ask:
                                        voice "audio/voices/ch2/shared/hero/ch2_share_h_10.flac"
                                        hero "But it was there a second ago!\n"
                                    else:
                                        voice "audio/voices/ch2/shared/hero/ch2_share_h_6.flac"
                                        hero "But there was a mirror a second ago.\n"
                                    voice "audio/voices/ch2/damsel/smitten/ch2_smitten_17.flac"
                                    smitten "And now it's gone. Pity. We could have a feather out of place and now we'll never know. We can't gallantly sweep her off her feet if we have a feather out of place.\n"
                                    play audio "audio/one_shot/footsteps_creaky.flac"
                                    hide bg onlayer front
                                    scene farback damsel cabin onlayer farback at Position(ypos=1125)
                                    show bg damsel cabin onlayer back at Position(ypos=1125)
                                    show door damsel1 onlayer back at Position(ypos=1125)
                                    show table damsel onlayer back at Position(ypos=1125)
                                    if damsel_1_cabin_blade_taken == False:
                                        show knife damsel onlayer back at Position(ypos=1125)
                                    with dissolve
                                    jump cabin_interior_2_damsel_menu

                jump cabin_interior_2_damsel_menu

            "{i}• (Explore) This whole cabin is different than last time.{/i}" if damsel_1_cabin_last_time_comment == False and damsel_1_forest_share_loop_insist:
                $ damsel_1_cabin_last_time_comment = True
                voice "audio/voices/ch2/shared/hero/ch2_share_h_11.flac"
                hero "{i}Very{/i} different.\n"
                voice "audio/voices/ch2/damsel/smitten/ch2_smitten_18.flac"
                smitten "Is it? I can't say I was paying much attention to the scenery last time around.\n"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_34.flac"
                n "Maybe that's because you haven't actually been here. I hope this means you'll finally drop that ridiculous past-life nonsense. You haven't died, and you certainly haven't been killed by the Princess.\n"
                voice "audio/voices/ch2/damsel/narrator/ch2_dn_18.flac"
                n "So focus up. Stop letting yourself get distracted.\n"
                jump cabin_interior_2_damsel_menu

            "{i}• (Explore) [[Approach the mirror.]{/i}" if damsel_1_cabin_mirror_present and damsel_1_cabin_mirror_approached == False:
                $ damsel_1_cabin_mirror_approached = True
                jump damsel_cabin_1_mirror_join

            "{i}• (Explore) [[Take the blade.]{/i}" if damsel_1_cabin_blade_taken == False:
                $ damsel_1_cabin_blade_taken = True
                $ blade_held = True
                $ default_mouse = "blade"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_36.flac"
                play audio "audio/one_shot/knife_pickup.flac"
                hide knife onlayer back
                with dissolve
                n "You take the blade from the table. It would be difficult to slay the Princess and save the world without a weapon.\n"
                voice "audio/voices/ch2/damsel/smitten/ch2_smitten_19.flac"
                smitten "I suppose if we're to play the role of dashing knight we need an equally dashing sword. That way she'll know we can defend her from her enemies.\n"
                if damsel_1_forest_share_loop == False:
                    voice "audio/voices/ch2/damsel/hero/ch2_dh_10.flac"
                    hero "Hopefully it doesn't put her on edge.\n"
                else:
                    voice "audio/voices/ch2/damsel/hero/ch2_dh_11.flac"
                    hero "Hopefully it doesn't put her on edge. And hopefully it doesn't get turned on us... again.\n"
                voice "audio/voices/ch2/damsel/narrator/ch2_dn_19.flac"
                n "There's no use arguing over {i}motivations{/i} right now. It's good that you took the blade. You'll need it to do your job.\n"
                jump cabin_interior_2_damsel_menu

            "{i}• [[Enter the basement.]{/i}":

                play audio "audio/one_shot/door_bedroom.flac"
                $ quick_menu = False
                show door damsel2 onlayer back at Position(ypos=1125)
                with Dissolve(0.5)
                hide mirror onlayer back
                show door damsel3 onlayer back at Position(ypos=1125) with Dissolve(0.5)
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

                voice "audio/voices/ch2/damsel/narrator/ch2_dn_20.flac"
                play secondary "audio/looping/STP_firecontrolled_loop.ogg" loop fadein 1.0
                scene bg damsel stairs onlayer back at Position(ypos=1125)
                show fire damsel stairs onlayer back at Position(ypos=1125)
                with fade
                if persistent.quick_menu:
                    $ quick_menu = True
                n "The door to the basement creaks open, revealing an intricate stairwell. Gold-trimmed carpet glimmers in the light of the torches positioned along the walls. The basement almost seems welcoming in the dim firelight.\n"
                voice "audio/voices/ch2/damsel/narrator/ch2_dn_20a.flac"
                n "But it's still a stone basement. If the Princess lives here, slaying her is probably doing her a favor.\n"
                voice "audio/voices/ch2/damsel/narrator/ch2_dn_21.flac"
                n "A soft voice carries up the stairs.\n"
                #if blade_held == False:
                #    voice "audio/voices/ch2/damsel/narrator/ch2_dn_22.flac"
                #    n "You shouldn't have come down here unarmed.\n"
                voice "audio/voices/ch2/damsel/princess/ch2_dp_1.flac"
                p "H-hello? Is someone there?\n"
                if damsel_1_forest_share_loop:
                    voice "audio/voices/ch2/damsel/smitten/ch2_smitten_20a.flac"
                    smitten "Her voice... it's somehow even more beautiful than last time. I can hear wedding bells already...\n"
                    voice "audio/voices/ch2/damsel/hero/ch2_dh_12.flac"
                    hero "I've held my tongue 'til now, but you're taking this a little too far. We barely even know the Princess. We can still do right by her without all this over-the-top fawning.\n"
                else:
                    voice "audio/voices/ch2/damsel/smitten/ch2_smitten_20.flac"
                    smitten "Her voice... it's somehow even more beautiful than last time. I think we're in love.\n"
                    voice "audio/voices/ch2/damsel/hero/ch2_dh_13.flac"
                    hero "Okay, I'm with you that we should be doing whatever we can to save her, but saying we're in love is a bit much, don't you think?\n"
                    voice "audio/voices/ch2/damsel/hero/ch2_dh_14.flac"
                    hero "We don't even know the Princess. We can still do right by her without all this... fawning.\n"
                voice "audio/voices/ch2/damsel/narrator/ch2_dn_23.flac"
                n "Yes. For everyone's sake, you're not in love. {i}Sigh{/i}. Just remember that her charms are all part of the manipulation.\n"
                $ gallery_damsel.unlock_item(2)
                $ renpy.save_persistent()
                play audio "audio/one_shot/footsteps_creaky.flac"
                $ quick_menu = False
                stop secondary fadeout 1.0
                hide bg onlayer back
                hide fire onlayer back
                with fade
                scene farback damsel basement onlayer farback at Position(ypos=1125)
                show bg damsel basement onlayer back at Position(ypos=1125)
                show damsel d neutral onlayer back at Position(ypos=1125)
                with fade
                if persistent.quick_menu:
                    $ quick_menu = True
                voice "audio/voices/ch2/damsel/narrator/ch2_dn_24.flac"
                n "You walk down the stairs and lock eyes with the Princess. There's a heavy chain around her wrist, binding her to the far wall.\n"
                voice "audio/voices/ch2/damsel/smitten/ch2_smitten_22.flac"
                smitten "My love! We're here to rescue you from your unjust and foul imprisonment!\n"
                voice "audio/voices/ch2/damsel/narrator/ch2_dn_25a.flac"
                n "You know she can't hear you, right?\n"
                voice "audio/voices/ch2/damsel/smitten/ch2_smitten_23.flac"
                smitten "She may not be able to hear my words, but surely, she can hear my spirit.\n"
                voice "audio/voices/ch2/damsel/hero/ch2_dh_16a.flac"
                n "Oh, your spirit's plenty loud, alright.\n"
                jump damsel_1_encounter_start
