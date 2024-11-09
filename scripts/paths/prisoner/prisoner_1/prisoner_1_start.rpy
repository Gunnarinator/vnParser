label prisoner_1_start:
    $ blade_held = False
    $ trait_skeptic = True
    $ quick_menu = False
    play sound "audio/looping/uncomfortable ambiance.ogg" loop fadein 1.0
    scene chapter prisoner with fade
    show text _("{color=#FFFFFF00}Chapter Two. The Prisoner.{/color}") at Position(ypos=850)
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
    $ gallery_prisoner.unlock_gallery()
    $ gallery_zch1.unlock_item(8)
    $ renpy.save_persistent()

    voice "audio/voices/ch1/woods/narrator/script_n_1.flac"
    n "You're on a path in the woods. And at the end of that path is a cabin. And in the basement of that cabin is a Princess.\n"
    voice "audio/voices/ch1/woods/narrator/script_n_2.flac"
    n "You're here to slay her.\n If you don't, it will be the end of the world.\n"
    label prisoner_1_forest:
        default prisoner_1_forest_count = 0
        default prisoner_1_forest_share_died = False
        default prisoner_1_forest_share_loop = False
        default prisoner_1_forest_princess_press = False
        default prisoner_1_forest_share_loop_insist = False
        default prisoner_1_forest_deja_vu = False
        default prisoner_1_forest_deja_vu_follow_up = False
        menu:
            extend ""

            "{i}• (Explore) I'm getting a terrible sense of deja vu.{/i}" if prisoner_1_forest_share_loop == False:
                $ prisoner_1_forest_deja_vu = True
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_1a.flac"
                n "A terrible sense of deja vu? No, you don't have that. This is the first time either of us have been here.\n"
                label prisoner_1_forest_narrator_share_join:
                    $ prisoner_1_forest_count += 1
                    $ prisoner_1_forest_share_loop = True
                    voice "audio/voices/ch2/prisoner/skeptic/ch2_skeptic_1.flac"
                    skeptic "Don't forget what He did to us the last time around. I wouldn't trust a word out of his mouth. There's got to be a way out of here, for us {i}and{/i} for the Princess. We just have to keep trying.\n"
                    voice "audio/voices/ch2/prisoner/hero/ch2_ph_1.flac"
                    hero "I'm inclined to agree. If He doesn't remember what happened last time, maybe it's best to keep it that way.\n"
                    voice "audio/voices/ch2/prisoner/narrator/ch2_pn_1.flac"
                    n "You know I can hear you two, right? It's going to be a lot harder than you think to keep secrets from me.\n"
                    if prisoner_forest_second_ago == False:
                        voice "audio/voices/ch2/prisoner/narrator/ch2_pn_2.flac"
                        n "And as far as trying to {i}help{/i} her goes, need I remind you how catastrophically dangerous she is to the world at large? I told you about the stakes of this situation less than a minute ago.\n"
                    jump prisoner_1_forest

            "{i}• (Explore) This is more than just deja vu, though. I'm pretty sure this whole thing really just happened.{/i}" if prisoner_1_forest_deja_vu and prisoner_1_forest_deja_vu_follow_up == False:
                $ prisoner_1_forest_deja_vu_follow_up = True
                $ prisoner_1_forest_count += 1
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_2.flac"
                n "We could go back and forth on this forever, and it won't get you any closer to doing your job and saving the world. So let's just agree to disagree.\n"
                jump prisoner_1_forest

            "{i}• (Explore) Wait... hasn't this already happened?{/i}" if prisoner_1_forest_share_loop == False:
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_1b.flac"
                n "It hasn't. Or if it has, I certainly haven't been a part of it. We've just met for the first time, you and I.\n"
                jump prisoner_1_forest_narrator_share_join

            "{i}• (Explore) Okay, no.{/i}" if prisoner_1_forest_share_loop == False:
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_3a.flac"
                n "Oh, don't you start grandstanding about morals. The fate of the world is at risk right now, and the life of a mere Princess shouldn't stop you from saving us all.\n"
                jump prisoner_1_forest_narrator_share_join

            "{i}• (Explore) But I died! What am I doing here?{/i}" if prisoner_1_forest_share_loop == False:
                $ prisoner_1_forest_share_died = True
                default prisoner_forest_second_ago = False
                $ prisoner_forest_second_ago = True
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_4.flac"
                n "I can assure you that you're not dead. And to answer your second question, you're here to slay the Princess. I literally told you that a second ago.\n"
                jump prisoner_1_forest_narrator_share_join

            "{i}• (Explore) Oh, you bastard! You're in for it now. I'm wise to your tricks!{/i}" if prisoner_1_forest_share_loop == False:
                $ prisoner_1_forest_share_died = True
                voice "audio/voices/ch2/prisoner/narrator/ch2_pn_7.flac"
                n "My tricks? What on earth are you talking about? We've just met for the first time.\n"
                jump prisoner_1_forest_narrator_share_join

            "{i}• (Explore) Let's assume I'm telling the truth, and all of this really did already happen. Why should I listen to you? Why should I bother doing {i}anything{/i}?{/i}" if prisoner_1_forest_share_loop and (prisoner_1_forest_deja_vu == False or (prisoner_1_forest_deja_vu_follow_up)) and prisoner_1_forest_share_loop_insist == False:
                $ prisoner_1_forest_share_loop_insist = True
                $ prisoner_1_forest_count += 1
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_6.flac"
                n "Those are two very different questions, but fine. I'll indulge you if that's what it takes to get you moving.\n"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_7.flac"
                n "Let's say for a moment that this really is the second time you've met me, or, at least, a version of me.\n"
                if prisoner_1_forest_share_died == False:
                    voice "audio/voices/ch2/shared/narrator/ch2_share_n_8.flac"
                    n "If you're back here, I'm assuming you died, which probably only happened because you didn't listen to me.\n"
                else:
                    voice "audio/voices/ch2/shared/narrator/ch2_share_n_9.flac"
                    n "You died last time, which probably only happened because you didn't listen to me.\n"
                voice "audio/voices/ch2/prisoner/skeptic/ch2_skeptic_2.flac"
                skeptic "The absolute irony. But that's one way to put it, I guess.\n"
                voice "audio/voices/ch2/prisoner/hero/ch2_ph_2.flac"
                hero "You {i}really{/i} don't remember what happened last time, do you? You practically forced the Princess to kill us.\n"
                voice "audio/voices/ch2/prisoner/narrator/ch2_pn_12.flac"
                n "That doesn't sound like the sort of thing I'd do, which is honestly all the more reason for you to not buy into whatever self-delusions the three of you are crafting.\n"
                voice "audio/voices/ch2/prisoner/narrator/ch2_pn_13.flac"
                n "{i}Sigh{/i}. But this is a thought experiment, so I suppose I'll continue to give you the benefit of the doubt. If I did 'practically force the Princess to kill you', it was probably for a good reason. Did you try and free her? Did you say something really mean to me? Because if I really did what you said I did, you probably deserved it. I'm a professional, after all.\n"
                voice "audio/voices/ch2/prisoner/skeptic/ch2_skeptic_3.flac"
                skeptic "Sure you are.\n"
                voice "audio/voices/ch2/prisoner/narrator/ch2_pn_14.flac"
                n "Anyways, I believe your second question was 'what's the point of doing anything?' If you're asking that, it sounds to me like you're making the rather dangerous assumption that your actions last time around didn't have any consequences.\n"
                voice "audio/voices/ch2/prisoner/hero/ch2_ph_3.flac"
                hero "What do you mean? Of course there weren't any consequences. You forced the Princess to kill us, and now everyone's right back where they started. That sounds pretty consequence-free to me.\n"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_12.flac"
                n "Yes, but, in this purely hypothetical scenario, that begs the question of {i}how{/i} you got back here. Did 'time' simply rewind itself, or were you instead transported to a different world entirely?\n"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_13.flac"
                n "If it's the latter, what do you think happened {i}after{/i} you died?\n"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_13a.flac"
                n "Do you think the people there lived happily ever after, or do you think that the Princess, left unhindered, brought about the end to everyone and everything, just like I told you she would?\n"
                voice "audio/voices/ch2/prisoner/skeptic/ch2_skeptic_4.flac"
                skeptic "What a conveniently ambiguous group of things for her to ruin. For all we know, the Princess left the cabin and never saw another soul.\n"
                voice "audio/voices/ch2/prisoner/narrator/ch2_pn_17.flac"
                n "Oh how I wish that were the case, but if the Princess weren't a certain, inevitable threat to the world, the four of us wouldn't be here. And yet, here we are.\n"
                voice "audio/voices/ch2/prisoner/skeptic/ch2_skeptic_5.flac"
                skeptic "You're talking in circles.\n"
                voice "audio/voices/ch2/prisoner/narrator/ch2_pn_18.flac"
                n "No. I'm talking in {i}facts{/i}.\n"
                jump prisoner_1_forest

            "{i}• (Explore) Let's talk about this Princess...{/i}" if prisoner_1_forest_share_loop_insist and prisoner_1_forest_princess_press == False:
                $ prisoner_1_forest_count += 1
                $ prisoner_1_forest_princess_press = True
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_14.flac"
                n "Just be quick about it.\n"
                label prisoner_1_forest_princess:
                    default prisoner_1_forest_princess_count = 0
                    default prisoner_1_forest_princess_why_strong = False
                    default prisoner_1_forest_princess_basement_explain = False
                    default prisoner_1_forest_princess_why_me = False
                    default prisoner_1_forest_princess_cagey = False
                    default prisoner_1_forest_princess_tips = False
                    menu:
                        extend ""

                        "{i}• (Explore) The only reason she was even able to kill me last time was because I let her. And all she did was slit my throat. How is she supposed to end the world?{/i}" if prisoner_1_forest_princess_why_strong == False:
                            $ prisoner_1_forest_princess_why_strong = True
                            $ prisoner_1_forest_princess_count += 1
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_16a.flac"
                            n "She just can. Believe me, I wish I could tell you more, but you'll just have to trust that what I'm saying is true and that, despite it all, you're fully up to the task that's been given to you.\n"
                            voice "audio/voices/ch2/prisoner/skeptic/ch2_skeptic_6.flac"
                            skeptic "You haven't given us an ounce of proof. You do know that, right?\n"
                            voice "audio/voices/ch2/prisoner/narrator/ch2_pn_21.flac"
                            n "What proof could you possibly ask for?\n"
                            voice "audio/voices/ch2/prisoner/hero/ch2_ph_4.flac"
                            hero "Literally anything.\n"
                            voice "audio/voices/ch2/prisoner/narrator/ch2_pn_22.flac"
                            n "{i}Sigh{/i}. Fine. Check your pockets.\n"
                            menu:
                                extend ""

                                "{i}• [[Check your pockets.]{/i}":
                                    voice "audio/voices/ch2/prisoner/narrator/ch2_pn_23.flac"
                                    play audio "audio/one_shot/page_turn_short.flac"
                                    show evidence onlayer inyourface at Position(ypos=1125)
                                    with dissolve
                                    n "You put your hands in your pockets and pull out an envelope with the words 'THE EVIDENCE' written across the front.\n"
                                    $ gallery_prisoner.unlock_item(12)
                                    $ renpy.save_persistent()
                                    voice "audio/voices/ch2/prisoner/narrator/ch2_pn_24.flac"
                                    play audio "audio/one_shot/page_turn_short.flac"
                                    show evidence 2 onlayer inyourface at Position(ypos=1125)
                                    with dissolve
                                    n "Within, you find a note in your handwriting. It reads: 'The Princess will end the world if you don't stop her. This is an immutable truth.'\n"
                                    voice "audio/voices/ch2/prisoner/skeptic/ch2_skeptic_7.flac"
                                    skeptic "That doesn't prove anything! How do we know you didn't just forge our handwriting?\n"
                                    voice "audio/voices/ch2/prisoner/narrator/ch2_pn_25.flac"
                                    n "I wish I could tell you more, but there are some rules I have to follow for all of our sakes. Please just trust that these rules are in place for a reason. I'm on your side.\n"
                                    voice "audio/voices/ch2/prisoner/skeptic/ch2_skeptic_8.flac"
                                    play audio "audio/one_shot/page_turn_short.flac"
                                    hide evidence onlayer inyourface
                                    with dissolve
                                    skeptic "You mean you're on our side as long as we do what you tell us to.\n"
                                    voice "audio/voices/ch2/prisoner/narrator/ch2_pn_26.flac"
                                    n "Exactly. Because you {i}not{/i} doing what I tell you to do means you're putting the world at risk.\n"
                                    voice "audio/voices/ch2/prisoner/hero/ch2_ph_5.flac"
                                    hero "I think we've got everything out of him that we're going to get.\n"

                                "{i}• [[Leave your pockets unchecked.]{/i}":
                                    voice "audio/voices/ch2/prisoner/narrator/ch2_pn_27.flac"
                                    n "You decide to leave your pockets unchecked. See? You two are the only ones here who care about this little aside.\n"

                            jump prisoner_1_forest_princess

                        "{i}• (Explore) Who locked her in that basement? What {b}is{/b} this place?{/i}" if prisoner_1_forest_princess_basement_explain == False:
                            $ prisoner_1_forest_princess_basement_explain = True
                            $ prisoner_1_forest_princess_count += 1
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_18.flac"
                            n "{i}People{/i} locked her in that basement. And I told you what this place is. It's a path in the woods. Don't overcomplicate things.\n"
                            jump prisoner_1_forest_princess

                        "{i}• (Explore) If people locked her away, why couldn't {b}they{/b} slay her? Why is this falling on me?{/i}" if prisoner_1_forest_princess_basement_explain and prisoner_1_forest_princess_why_me == False:
                            $ prisoner_1_forest_princess_why_me = True
                            $ prisoner_1_forest_princess_count += 1
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_19.flac"
                            n "Look, I'm not supposed to say this, but it's because you're special. You're the {i}only{/i} person capable of doing this. Call it a prophecy if that helps, but it's just the way things are.\n"
                            voice "audio/voices/ch2/shared/hero/ch2_share_h_2.flac"
                            hero "Oh. I didn't know we were {i}special{/i}.\n"
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_20a.flac"
                            n "Of course you're special. Why else would you be here?\n"
                            voice "audio/voices/ch2/prisoner/skeptic/ch2_skeptic_9.flac"
                            skeptic "Ah, yes, right. We're here because we're {i}special{/i}.\n"
                            voice "audio/voices/ch2/prisoner/narrator/ch2_pn_28.flac"
                            n "Look. You're annoyed that you're here. I get it. I'm also annoyed that I'm here. But we're all in this together, and we're dealing with a bit of a ticking clock right now, so please, just get to the cabin.\n"
                            jump prisoner_1_forest_princess

                        "{i}• (Explore) You're being cagey. What aren't you telling me?{/i}" if prisoner_1_forest_princess_cagey == False and prisoner_1_forest_princess_count > 1:
                            $ prisoner_1_forest_princess_cagey = True
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_21.flac"
                            n "I've told you everything you need to know, going into more detail would just overcomplicate an otherwise very simple situation and make your job more difficult.\n"
                            if prisoner_1_forest_princess_count < 2:
                                voice "audio/voices/ch2/shared/narrator/ch2_share_n_22.flac"
                                n "The less you know about her, the better.\n"
                            else:
                                voice "audio/voices/ch2/prisoner/narrator/ch2_pn_31.flac"
                                n "Not to sound like a broken record, but the less you know about her, the better things will go for all of us. I know it sounds like I'm hiding something, but you're just going to have to trust me here.\n"
                            jump prisoner_1_forest_princess

                        "{i}• Nevermind.{/i}" if prisoner_1_forest_princess_count == 0:
                            label prisoner_1_forest_princess_leaving:
                                voice "audio/voices/ch2/shared/narrator/ch2_share_n_24.flac"
                                n "Great. Now if you don't mind, the whole world is waiting with bated breath for you to save it from ruin.\n"
                                jump prisoner_1_forest

                        "{i}• That's all.{/i}" if prisoner_1_forest_princess_count != 0:
                            jump prisoner_1_forest_princess_leaving

            "{i}• [[Proceed to the cabin.]{/i}":
                jump prisoner_1_cabin_arrival

            "{i}• [[Turn around and leave.]{/i}" if mound_can_attempt_flee:
                if loops_finished >= 2:
                    $ mound_can_attempt_flee = False
                    voice "audio/voices/mound/bonus/flee.flac"
                    mound "You have already committed to my completion. You cannot go further astray.\n"
                    jump prisoner_1_forest
                voice "audio/voices/ch2/prisoner/skeptic/ch2_skeptic_10.flac"
                skeptic "I'm not so sure running away is the best idea. We're not the only person stuck here. What about her?\n"
                jump turn_and_leave_join

label prisoner_1_cabin_arrival:
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
    voice "audio/voices/ch2/prisoner/skeptic/ch2_skeptic_11.flac"
    skeptic "Yes, yes, don't believe a word she says. Just go in, take the knife, and do what you're supposed to. Wink.\n"
    voice "audio/voices/ch2/prisoner/narrator/ch2_pn_33.flac"
    n "Did you just say 'wink' out loud?\n"
    voice "audio/voices/ch2/prisoner/skeptic/ch2_skeptic_12.flac"
    skeptic "No, I didn't. Wink.\n"
    voice "audio/voices/ch2/prisoner/narrator/ch2_pn_34.flac"
    n "Just ignore this clown and focus on the Princess.\n"
    menu:
        extend ""

        "{i}• [[Proceed into the cabin.]{/i}":
            label prisoner_stranger_rejoin:
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

    $ gallery_prisoner.unlock_item(1)
    $ renpy.save_persistent()
    voice "audio/voices/ch2/prisoner/narrator/ch2_pn_35.flac"
    play sound "audio/looping/ambient_cabin.ogg" loop fadein 1.0
    play music "audio/_music/ch2/prisoner/The Prisoner Intro.flac"
    queue music "audio/_music/ch2/prisoner/The Prisoner Loop.flac" loop
    scene farback prisoner cabin onlayer farback at Position(ypos=1125)
    show bg prisoner cabin onlayer back at Position(ypos=1125)
    show door prisoner1 onlayer back at Position(ypos=1125)
    show table prisoner onlayer back at Position(ypos=1125)
    show knife prisoner onlayer back at Position(ypos=1125)
    show mirror base onlayer back at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    n "The interior of the cabin is less a cozy woodland retreat and more like a dungeon. A few pathetic wisps of starlight attempt to illuminate the cold, uninviting stone walls, and thick wrought-iron bars barricade the windows, reminding anyone who enters that this is a prison.\n"
    voice "audio/voices/ch2/prisoner/narrator/ch2_pn_35a.flac"
    n "The only furniture of note is an iron table, bolted to the floor, a pristine blade perched on its edge.\n"
    voice "audio/voices/ch2/shared/narrator/ch2_share_n_25.flac"
    n "The blade is your implement. You'll need it if you want to do this right.\n"
    label cabin_interior_2_prisoner_menu:
        default prisoner_1_cabin_mirror_present = True
        default prisoner_1_cabin_blade_taken = False
        default prisoner_1_cabin_mirror_ask = False
        default prisoner_1_cabin_mirror_approached = False
        default prisoner_1_cabin_last_time_comment = False
        menu:
            extend ""

            "{i}• (Explore) You didn't say anything about the mirror on the wall.{/i}" if prisoner_1_cabin_mirror_ask == False and prisoner_1_cabin_mirror_present:
                $ prisoner_1_cabin_mirror_ask = True
                $ current_run_mirror_comment = True
                voice "audio/voices/ch2/prisoner/skeptic/ch2_skeptic_13.flac"
                skeptic "He definitely did not. Does a mirror not count as 'furniture of note' to you? Because it should.\n"
                voice "audio/voices/ch2/prisoner/narrator/ch2_pn_mirrorfix.flac"
                n "There isn't a mirror. There's a table, the blade sitting on the table, and the door to the basement. There's nothing else in here.\n"
                #n "What are you talking about? There isn't a mirror. There's the table, the blade sitting on the table, and the door to the basement. There's nothing else in here. If there were a mirror I'd have told you there were a mirror.\n"
                voice "audio/voices/ch2/shared/hero/ch2_share_h_4.flac"
                hero "There's definitely a mirror.\n"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_27.flac"
                n "There isn't.\n"
                voice "audio/voices/ch2/prisoner/skeptic/ch2_skeptic_14.flac"
                skeptic "I think you know what we have to do.\n"
                menu:
                    extend ""

                    "{i}• Why {b}would{/b} you lie about that? What's the point?{/i}":
                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_28.flac"
                        n "Exactly. Why would I lie about something so meaningless? What good would a mirror even do? Let you waste time preening yourself instead of doing what needs to be done?\n"

                    "{i}• I want to look at myself. I want to see how {b}handsome{/b} I am.{/i}":
                        voice "audio/voices/ch2/prisoner/skeptic/ch2_skeptic_15.flac"
                        skeptic "Let's not get caught up in vanity, but we should definitely take a closer look. Whatever it is, He must not want us to know about it.\n"
                        voice "audio/voices/ch2/prisoner/narrator/ch2_pn_37.flac"
                        n "Is this some sort of rehearsed bit? Use your eyes, there is no mirror. Why would I lie about something so meaningless? What good would it even do?\n"

                    "{i}• It doesn't matter.{/i}":
                        $ prisoner_1_cabin_mirror_present = False
                        voice "audio/voices/ch2/prisoner/skeptic/ch2_skeptic_16.flac"
                        skeptic "We should treat everything in here like it matters.\n"
                        voice "audio/voices/ch2/prisoner/hero/ch2_ph_8.flac"
                        hero "Exactly, don't you care if we're being lied to? If He's willing to lie about something as innocuous as a mirror, what else is He hiding from us?\n"
                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_30.flac"
                        hide mirror onlayer back
                        n "I'm not lying to you. Use your eyes, there is no mirror. Why would I lie about something so meaningless? What good would a mirror even do? Let you waste time preening yourself instead of doing what needs to be done?\n"
                        voice "audio/voices/ch2/shared/hero/ch2_share_h_6.flac"
                        hero "But there {i}was{/i} a mirror a second ago.\n"
                        voice "audio/voices/ch2/prisoner/skeptic/ch2_skeptic_17.flac"
                        skeptic "And now it's gone. If He doesn't want us to know about it, it must be important. We should keep our eyes peeled. Maybe it'll be back.\n"

                    "{i}• [[Remain silent.]{/i}":
                        voice "audio/voices/ch2/shared/hero/ch2_share_h_7b.flac"
                        hero "I care about whether we're being lied to. If He's willing to lie about something as innocuous as a mirror, what else could He hiding from us?\n"
                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_31.flac"
                        n "I'm not lying to you, I {i}promise{/i}. There isn't a mirror. Really.\n"

                    "{i}• [[Approach the mirror.]{/i}" if prisoner_1_cabin_mirror_approached == False:
                        label prisoner_cabin_1_mirror_join:
                            $ prisoner_1_cabin_mirror_approached = True
                            play audio "audio/one_shot/footsteps_creaky.flac"
                            hide farback onlayer farback
                            hide bg onlayer back
                            hide door onlayer back
                            hide table onlayer back
                            hide knife onlayer back
                            hide mirror onlayer back
                            scene bg prisoner mirror onlayer front at Position(ypos=1125)
                            show mirror prisoner close onlayer front at Position(ypos=1125)
                            with dissolve
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_32.flac"
                            n "You walk up to the wall next to the basement door. It's a wall. There isn't much to see here.\n"
                            if prisoner_1_cabin_mirror_ask == False:
                                voice "audio/voices/ch2/shared/hero/ch2_share_h_8.flac"
                                hero "What are you talking about? This isn't a wall. It's a mirror. Or at least it'll {i}be{/i} a mirror once we wipe off that layer of grime.\n"
                            else:
                                voice "audio/voices/ch2/shared/hero/ch2_share_h_9.flac"
                                hero "This really isn't funny.\n"
                            $ current_run_mirror_touched = True
                            menu:
                                extend ""

                                "{i}• [[Wipe the mirror clean.]{/i}":
                                    $ prisoner_1_cabin_mirror_present = False
                                    hide mirror onlayer front
                                    play audio "audio/one_shot/new/STP_claws_1.flac"
                                    show player wall onlayer front at Position(ypos=1125) with dissolve
                                    if prisoner_1_cabin_mirror_ask == False:
                                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_33.flac"
                                    else:
                                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_33a.flac"
                                    n "You reach forward and rub your hand against the cabin wall. I hope you know how ridiculous you look right now.\n"
                                    hide player onlayer front with dissolve
                                    if prisoner_1_cabin_mirror_ask:
                                        voice "audio/voices/ch2/shared/hero/ch2_share_h_10.flac"
                                        hero "But it was there a second ago!\n"
                                    else:
                                        voice "audio/voices/ch2/shared/hero/ch2_share_h_6.flac"
                                        hero "But there was a mirror a second ago.\n"
                                    voice "audio/voices/ch2/prisoner/skeptic/ch2_skeptic_17.flac"
                                    skeptic "And now it's gone. If He doesn't want us to know about it, it must be important. We should keep our eyes peeled. Maybe it'll be back.\n"
                                    play audio "audio/one_shot/footsteps_creaky.flac"
                                    hide bg onlayer front
                                    scene farback prisoner cabin onlayer farback at Position(ypos=1125)
                                    show bg prisoner cabin onlayer back at Position(ypos=1125)
                                    show door prisoner1 onlayer back at Position(ypos=1125)
                                    show table prisoner onlayer back at Position(ypos=1125)
                                    if prisoner_1_cabin_blade_taken == False:
                                        show knife prisoner onlayer back at Position(ypos=1125)
                                    with dissolve
                                    jump cabin_interior_2_prisoner_menu

                jump cabin_interior_2_prisoner_menu

            "{i}• (Explore) This whole cabin is different than last time.{/i}" if prisoner_1_cabin_last_time_comment == False and prisoner_1_forest_share_loop_insist:
                $ prisoner_1_cabin_last_time_comment = True
                voice "audio/voices/ch2/shared/hero/ch2_share_h_11.flac"
                hero "{i}Very{/i} different.\n"
                voice "audio/voices/ch2/prisoner/skeptic/ch2_skeptic_18.flac"
                skeptic "Yes, but {i}why{/i}? Did He change it, or did it change all on its own? Maybe it's a different cabin entirely.\n"
                voice "audio/voices/ch2/prisoner/narrator/ch2_pn_41.flac"
                n "Now isn't that a novel thought! Maybe you {i}haven't{/i} actually been here before. I hope this means you'll finally drop your ridiculous past-life nonsense. You haven't died, and you certainly haven't been killed by the Princess.\n"
                voice "audio/voices/ch2/prisoner/narrator/ch2_pn_42.flac"
                n "So focus up. Don't get distracted by minor details.\n"
                jump cabin_interior_2_prisoner_menu

            "{i}• (Explore) [[Approach the mirror.]{/i}" if prisoner_1_cabin_mirror_present and prisoner_1_cabin_mirror_approached == False:
                $ prisoner_1_cabin_mirror_approached = True
                jump prisoner_cabin_1_mirror_join

            "{i}• (Explore) [[Take the blade.]{/i}" if prisoner_1_cabin_blade_taken == False:
                $ prisoner_1_cabin_blade_taken = True
                $ blade_held = True
                $ default_mouse = "blade"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_36.flac"
                play audio "audio/one_shot/knife_pickup.flac"
                hide knife onlayer back
                with dissolve
                n "You take the blade from the table. It would be difficult to slay the Princess and save the world without a weapon.\n"
                voice "audio/voices/ch2/prisoner/skeptic/ch2_skeptic_19.flac"
                skeptic "Good idea. Much better to be armed than to go in with blind hope alone.\n"
                jump cabin_interior_2_prisoner_menu

            "{i}• [[Enter the basement.]{/i}":
                if blade_held == False:
                    $ prisoner_delayed_knife_comment = True
                    voice "audio/voices/ch2/prisoner/skeptic/s1.flac"
                    skeptic "I'm afraid I'm going to insist we take the blade. We're in a dangerous situation, and I'm not letting us go down there without a weapon.\n"
                    if prisoner_1_forest_share_loop_insist == False:
                        voice "audio/voices/ch2/prisoner/hero/s1.flac"
                        hero "Are you sure? What if she, I don't know... turns it against us? ... Which I'm bringing up in a purely hypothetical manner.\n"
                        voice "audio/voices/ch2/prisoner/skeptic/s2.flac"
                        skeptic "Yes. I'm sure.\n"
                        voice "audio/voices/ch2/prisoner/narrator/s1.flac"
                        n "Turns it against you? She's a prisoner here. And she'll only be able to turn it against you if you give it to her. Which you won't be doing, because she's an existential threat to the entire world.\n"

                    else:
                        voice "audio/voices/ch2/prisoner/hero/s2.flac"
                        hero "Are you sure? She killed us with it last time. What if she turns it against us {i}again{/i}.\n"
                        voice "audio/voices/ch2/prisoner/skeptic/s3.flac"
                        skeptic "Yes. I'm sure. And I've already got a plan for that.\n"
                        voice "audio/voices/ch2/prisoner/narrator/s2.flac"
                        n "Still with those past-life delusions are we? I hope part of that plan is 'don't give the world-ending monstrosity your only weapon.' Because unless you've decided to arm the Princess, I don't think you need to worry about her having a weapon.\n"
                        voice "audio/voices/ch2/prisoner/skeptic/s4.flac"
                        skeptic "Peachy. We'll be fine.\n"
                    voice "audio/voices/ch2/prisoner/hero/s3.flac"
                    hero "Okay. I'm trusting you.\n"
                    label prisoner_knife_take_force:
                        default prisoner_knife_take_force_explore = False
                        default prisoner_delayed_knife_comment = False
                        menu:
                            extend ""

                            "{i}• ''Hey! Don't I get a say here? What's the big idea?''{/i}" if prisoner_knife_take_force_explore == False:
                                $ prisoner_knife_take_force_explore = True
                                voice "audio/voices/ch2/prisoner/skeptic/s5.flac"
                                skeptic "Normally, yeah. But not about this. Call it a reflex. We take the knife as we go.\n"
                                $ prisoner_1_cabin_blade_taken = True
                                $ blade_held = True
                                $ default_mouse = "blade"
                                play audio "audio/one_shot/knife_pickup.flac"
                                hide knife onlayer back
                                with dissolve
                                voice "audio/voices/ch2/prisoner/narrator/s3.flac"
                                n "Wonderful. You do exactly that, sweeping the blade from the table before proceeding to the basement.\n"
                                voice "audio/voices/ch2/prisoner/hero/s4.flac"
                                hero "Don't worry about it. We have a knife, so what? It's not like we have to use it.\n"
                                voice "audio/voices/ch2/prisoner/narrator/s4.flac"
                                n "No, you don't have to do anything. But you'd do well to use it regardless. {i}Sigh{/i}. Moving on.\n"

                            "{i}• [[Let it go and take the blade.]{/i}" if prisoner_knife_take_force_explore:
                                jump prisoner_knife_take_force_join

                            "{i}• [[Take the blade.]{/i}" if prisoner_knife_take_force_explore == False:
                                label prisoner_knife_take_force_join:
                                    $ prisoner_1_cabin_blade_taken = True
                                    $ blade_held = True
                                    $ default_mouse = "blade"
                                    voice "audio/voices/ch2/shared/narrator/ch2_share_n_36.flac"
                                    play audio "audio/one_shot/knife_pickup.flac"
                                    hide knife onlayer back
                                    with dissolve
                                    n "You take the blade from the table. It would be difficult to slay the Princess and save the world without a weapon.\n"
                                    voice "audio/voices/ch2/prisoner/skeptic/s6.flac"
                                    skeptic "Thanks. I mean it.\n"
                                    menu:
                                        extend ""

                                        "{i}• [[Enter the basement.]{/i}":
                                            $ blade_held = True

                play audio "audio/one_shot/door_bedroom.flac"
                $ quick_menu = False
                show door prisoner2 onlayer back at Position(ypos=1125)
                with Dissolve(0.5)
                hide mirror onlayer back
                show door prisoner3 onlayer back at Position(ypos=1125) with Dissolve(0.5)
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

                play secondary "audio/looping/STP_firecontrolled_loop.ogg" loop fadein 1.0
                voice "audio/voices/ch2/prisoner/narrator/ch2_pn_44.flac"

                scene bg prisoner stairs onlayer back at Position(ypos=1125)
                show fire prisoner stairs onlayer back at Position(ypos=1125)
                with fade
                if persistent.quick_menu:
                    $ quick_menu = True
                n "The door to the basement creaks open, revealing an old stone staircase. A few sputtering torches attempt to vaguely illuminate your path, dancing across glimmering patches of slimy moss on the stone steps. If the Princess lives here, slaying her would probably be doing her a favor.\n"
                voice "audio/voices/ch2/prisoner/narrator/ch2_pn_45.flac"
                n "Her voice, harsh but controlled, carries up the stairs.\n"
                voice "audio/voices/ch2/prisoner/princess/ch2_pp_1.flac"
                sp "Is that a visitor I hear? Please, come downstairs. It's been a while since I've had company.\n"
                if blade_held == False:
                    voice "audio/voices/ch2/prisoner/narrator/ch2_pn_46.flac"
                    n "You shouldn't have come down here unarmed.\n"
                if prisoner_1_forest_share_loop:
                    voice "audio/voices/ch2/prisoner/skeptic/ch2_skeptic_20.flac"
                    skeptic "Does she remember us?\n"
                else:
                    voice "audio/voices/ch2/prisoner/skeptic/ch2_skeptic_21.flac"
                    skeptic "I wonder what visitors she could be referring to. Are we not the first?\n"

                $ gallery_prisoner.unlock_item(2)
                $ renpy.save_persistent()
                stop secondary fadeout 1.0
                play audio "audio/one_shot/footsteps_creaky.flac"
                stop secondary fadeout 1.0
                $ quick_menu = False
                hide bg onlayer back
                hide fire onlayer back
                with fade
                scene farback prisoner basement onlayer farback at Position(ypos=1125)
                show bg prisoner basement onlayer back at Position(ypos=1125)
                show prisoner d neutral onlayer back at Position(ypos=1125)
                with fade
                if persistent.quick_menu:
                    $ quick_menu = True
                voice "audio/voices/ch2/prisoner/narrator/ch2_pn_47.flac"
                n "You walk down the stairs and lock eyes with the Princess. She looks up at you, the heavy collar around her neck clanking loudly as she moves, the chains binding both her wrists to the far wall joining the metallic chorus as she adjusts her hands in her lap.\n"
                show prisoner d tilt onlayer back at Position(ypos=1125) with dissolve
                if prisoner_1_forest_share_loop_insist:
                    voice "audio/voices/ch2/prisoner/hero/ch2_ph_15.flac"
                    hero "So much for cutting her out of here...\n"
                    voice "audio/voices/ch2/prisoner/narrator/ch2_pn_48.flac"
                    n "Do you hear yourself right now? 'Cutting her out of here' never should have been on the table.\n"
                else:
                    voice "audio/voices/ch2/prisoner/hero/ch2_ph_16.flac"
                    hero "Should we be worried about the one around her neck?\n"
                    voice "audio/voices/ch2/prisoner/narrator/ch2_pn_49.flac"
                    n "Why would you be worried about her restraints. If anything, they'll make your job easier.\n"
                voice "audio/voices/ch2/prisoner/skeptic/ch2_skeptic_22.flac"
                skeptic "Have you noticed the empty chain on the wall? Odd that in a place where everything seems to serve a distinct purpose, there would be something so obviously useless.\n"
                if prisoner_1_forest_share_loop_insist:
                    voice "audio/voices/ch2/prisoner/hero/ch2_ph_17.flac"
                    hero "That was there last time too, wasn't it?\n"
                    voice "audio/voices/ch2/prisoner/skeptic/ch2_skeptic_23.flac"
                    skeptic "It was.\n"
                show prisoner d talk onlayer back at Position(ypos=1125) with dissolve
                if blade_held:
                    voice "audio/voices/ch2/prisoner/princess/ch2_pp_2.flac"
                    sp "What an interesting development. Why don't you have a seat? The two of us should chat before you bury that thing in my heart.\n"
                else:
                    voice "audio/voices/ch2/prisoner/princess/ch2_pp_3.flac"
                    sp "What an interesting development. Why don't you have a seat? I'm sure the two of us have quite a bit to talk about.\n"

                jump prisoner_encounter_start
