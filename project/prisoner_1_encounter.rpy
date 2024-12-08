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

            "{i} (Explore) I'm getting a terrible sense of deja vu.{/i}" if prisoner_1_forest_share_loop == False:
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

            "{i} (Explore) This is more than just deja vu, though. I'm pretty sure this whole thing really just happened.{/i}" if prisoner_1_forest_deja_vu and prisoner_1_forest_deja_vu_follow_up == False:
                $ prisoner_1_forest_deja_vu_follow_up = True
                $ prisoner_1_forest_count += 1
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_2.flac"
                n "We could go back and forth on this forever, and it won't get you any closer to doing your job and saving the world. So let's just agree to disagree.\n"
                jump prisoner_1_forest

            "{i} (Explore) Wait... hasn't this already happened?{/i}" if prisoner_1_forest_share_loop == False:
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_1b.flac"
                n "It hasn't. Or if it has, I certainly haven't been a part of it. We've just met for the first time, you and I.\n"
                jump prisoner_1_forest_narrator_share_join

            "{i} (Explore) Okay, no.{/i}" if prisoner_1_forest_share_loop == False:
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_3a.flac"
                n "Oh, don't you start grandstanding about morals. The fate of the world is at risk right now, and the life of a mere Princess shouldn't stop you from saving us all.\n"
                jump prisoner_1_forest_narrator_share_join

            "{i} (Explore) But I died! What am I doing here?{/i}" if prisoner_1_forest_share_loop == False:
                $ prisoner_1_forest_share_died = True
                default prisoner_forest_second_ago = False
                $ prisoner_forest_second_ago = True
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_4.flac"
                n "I can assure you that you're not dead. And to answer your second question, you're here to slay the Princess. I literally told you that a second ago.\n"
                jump prisoner_1_forest_narrator_share_join

            "{i} (Explore) Oh, you bastard! You're in for it now. I'm wise to your tricks!{/i}" if prisoner_1_forest_share_loop == False:
                $ prisoner_1_forest_share_died = True
                voice "audio/voices/ch2/prisoner/narrator/ch2_pn_7.flac"
                n "My tricks? What on earth are you talking about? We've just met for the first time.\n"
                jump prisoner_1_forest_narrator_share_join

            "{i} (Explore) Let's assume I'm telling the truth, and all of this really did already happen. Why should I listen to you? Why should I bother doing {i}anything{/i}?{/i}" if prisoner_1_forest_share_loop and (prisoner_1_forest_deja_vu == False or (prisoner_1_forest_deja_vu_follow_up)) and prisoner_1_forest_share_loop_insist == False:
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

            "{i} (Explore) Let's talk about this Princess...{/i}" if prisoner_1_forest_share_loop_insist and prisoner_1_forest_princess_press == False:
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

                        "{i} (Explore) The only reason she was even able to kill me last time was because I let her. And all she did was slit my throat. How is she supposed to end the world?{/i}" if prisoner_1_forest_princess_why_strong == False:
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

                                "{i} [[Check your pockets.]{/i}":
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

                                "{i} [[Leave your pockets unchecked.]{/i}":
                                    voice "audio/voices/ch2/prisoner/narrator/ch2_pn_27.flac"
                                    n "You decide to leave your pockets unchecked. See? You two are the only ones here who care about this little aside.\n"

                            jump prisoner_1_forest_princess

                        "{i} (Explore) Who locked her in that basement? What {b}is{/b} this place?{/i}" if prisoner_1_forest_princess_basement_explain == False:
                            $ prisoner_1_forest_princess_basement_explain = True
                            $ prisoner_1_forest_princess_count += 1
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_18.flac"
                            n "{i}People{/i} locked her in that basement. And I told you what this place is. It's a path in the woods. Don't overcomplicate things.\n"
                            jump prisoner_1_forest_princess

                        "{i} (Explore) If people locked her away, why couldn't {b}they{/b} slay her? Why is this falling on me?{/i}" if prisoner_1_forest_princess_basement_explain and prisoner_1_forest_princess_why_me == False:
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

                        "{i} (Explore) You're being cagey. What aren't you telling me?{/i}" if prisoner_1_forest_princess_cagey == False and prisoner_1_forest_princess_count > 1:
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

                        "{i} Nevermind.{/i}" if prisoner_1_forest_princess_count == 0:
                            label prisoner_1_forest_princess_leaving:
                                voice "audio/voices/ch2/shared/narrator/ch2_share_n_24.flac"
                                n "Great. Now if you don't mind, the whole world is waiting with bated breath for you to save it from ruin.\n"
                                jump prisoner_1_forest

                        "{i} That's all.{/i}" if prisoner_1_forest_princess_count != 0:
                            jump prisoner_1_forest_princess_leaving

            "{i} [[Proceed to the cabin.]{/i}":
                jump prisoner_1_cabin_arrival

            "{i} [[Turn around and leave.]{/i}" if mound_can_attempt_flee:
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

        "{i} [[Proceed into the cabin.]{/i}":
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

            "{i} (Explore) You didn't say anything about the mirror on the wall.{/i}" if prisoner_1_cabin_mirror_ask == False and prisoner_1_cabin_mirror_present:
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

                    "{i} Why {b}would{/b} you lie about that? What's the point?{/i}":
                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_28.flac"
                        n "Exactly. Why would I lie about something so meaningless? What good would a mirror even do? Let you waste time preening yourself instead of doing what needs to be done?\n"

                    "{i} I want to look at myself. I want to see how {b}handsome{/b} I am.{/i}":
                        voice "audio/voices/ch2/prisoner/skeptic/ch2_skeptic_15.flac"
                        skeptic "Let's not get caught up in vanity, but we should definitely take a closer look. Whatever it is, He must not want us to know about it.\n"
                        voice "audio/voices/ch2/prisoner/narrator/ch2_pn_37.flac"
                        n "Is this some sort of rehearsed bit? Use your eyes, there is no mirror. Why would I lie about something so meaningless? What good would it even do?\n"

                    "{i} It doesn't matter.{/i}":
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

                    "{i} [[Remain silent.]{/i}":
                        voice "audio/voices/ch2/shared/hero/ch2_share_h_7b.flac"
                        hero "I care about whether we're being lied to. If He's willing to lie about something as innocuous as a mirror, what else could He hiding from us?\n"
                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_31.flac"
                        n "I'm not lying to you, I {i}promise{/i}. There isn't a mirror. Really.\n"

                    "{i} [[Approach the mirror.]{/i}" if prisoner_1_cabin_mirror_approached == False:
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

                                "{i} [[Wipe the mirror clean.]{/i}":
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

            "{i} (Explore) This whole cabin is different than last time.{/i}" if prisoner_1_cabin_last_time_comment == False and prisoner_1_forest_share_loop_insist:
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

            "{i} (Explore) [[Approach the mirror.]{/i}" if prisoner_1_cabin_mirror_present and prisoner_1_cabin_mirror_approached == False:
                $ prisoner_1_cabin_mirror_approached = True
                jump prisoner_cabin_1_mirror_join

            "{i} (Explore) [[Take the blade.]{/i}" if prisoner_1_cabin_blade_taken == False:
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

            "{i} [[Enter the basement.]{/i}":
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

                            "{i} ''Hey! Don't I get a say here? What's the big idea?''{/i}" if prisoner_knife_take_force_explore == False:
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

                            "{i} [[Let it go and take the blade.]{/i}" if prisoner_knife_take_force_explore:
                                jump prisoner_knife_take_force_join

                            "{i} [[Take the blade.]{/i}" if prisoner_knife_take_force_explore == False:
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

                                        "{i} [[Enter the basement.]{/i}":
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

label prisoner_encounter_start:
    default prisoner_locked = False
    default prisoner_narrator_agree = False
    default prisoner_position = "start"
    default prisoner_sit_closer = False
    default prisoner_attack = False
    default prisoner_can_slay_attempt = True
    menu:
        extend ""

        "{i} I'm not sure I need to do much of anything. Do you see how locked up she is? I'm just going to leave her here. [[Leave the Princess in the basement.]{/i}" if prisoner_locked == False:
            label prisoner_locked_join:
                $ prisoner_locked = True
                if prisoner_1_forest_share_loop_insist or prisoner_narrator_agree:
                    voice "audio/voices/ch2/prisoner/_basement/skeptic/1.flac"
                    skeptic "The door locked behind us the last time we tried that, remember?\n"
                play secondary "audio/one_shot/door_close.flac"
                queue secondary "audio/one_shot/lock_click.flac"
                voice "audio/voices/ch2/prisoner/_basement/narrator/1.flac"
                if prisoner_position == "close":
                    show prisoner c smile onlayer back
                    with dissolve
                n "As if by divine will, just as you finish the thought, you hear a door slam. I'm afraid you won't be leaving until the task is finished. It doesn't matter how many chains she's in, without your intervention, she'll find a way out eventually.\n"
                voice "audio/voices/ch2/prisoner/_basement/hero/1.flac"
                hero "That's not fair!\n"
                voice "audio/voices/ch2/prisoner/_basement/narrator/2.flac"
                n "Unless you deal with her right here, right now, she will remain an existential threat to the entire world. What seems unfair to you is fair for everyone else.\n"
                voice "audio/voices/ch2/prisoner/_basement/skeptic/2.flac"
                skeptic "Huh. So it's not even safe to think. I see how it is.\n"
                if prisoner_abandoned_comment_flag:
                    voice "audio/voices/ch2/prisoner/_basement/princess/1.flac"
                    if prisoner_position == "close":
                        show prisoner c surprise talk onlayer back
                    else:
                        show prisoner d tilt talk onlayer back
                        with dissolve
                    sp "I told you that you'd regret saying that. But I didn't think you'd regret it so fast. And with so little effort on my part.\n"
                    voice "audio/voices/ch2/prisoner/_basement/princess/2.flac"
                    if prisoner_position == "close":
                        show prisoner c shrug talk onlayer back
                    else:
                        show prisoner d talk onlayer back
                    with dissolve
                    sp "I guess we're stuck together.\n"
                elif prisoner_narrator_agree:
                    voice "audio/voices/ch2/prisoner/_basement/princess/3.flac"
                    if prisoner_position == "close":
                        show prisoner c shrug talk onlayer back
                    else:
                        show prisoner d tilt talk onlayer back
                    with dissolve
                    sp "How surprising. They locked you down here, too. Again.\n"
                else:
                    voice "audio/voices/ch2/prisoner/_basement/princess/4.flac"
                    if prisoner_position == "close":
                        show prisoner c shrug talk onlayer back
                    else:
                        show prisoner d tilt talk onlayer back
                    with dissolve
                    sp "How surprising. They locked you down here, too.\n"

                if prisoner_position == "close":
                    show prisoner c neutral onlayer back
                else:
                    show prisoner d neutral onlayer back
            if prisoner_position == "start":
                jump prisoner_encounter_start
            else:
                jump prisoner_menu

        "{i} [[Sit with her.]{/i}":
            play audio "audio/one_shot/footsteps_stone.flac"
            voice "audio/voices/ch2/prisoner/_basement/narrator/3.flac"
            hide farback onlayer farback
            hide bg onlayer back
            hide prisoner onlayer back
            scene bg prisoner basement close onlayer back at Position(ypos=1190)
            show prisoner c halt onlayer back at Position(ypos=1190)
            with Dissolve(1.0)
            n "You step towards the Princess, but she stops you before you get too close, holding up one shackled hand.\n"
            voice "audio/voices/ch2/prisoner/_basement/princess/5.flac"
            show prisoner c halt talk onlayer back
            with dissolve
            sp "There is fine. I'd prefer we keep some distance until we've sorted this out.\n"
            voice "audio/voices/ch2/prisoner/_basement/hero/2.flac"
            show prisoner c halt onlayer back
            with dissolve
            hero "That's reasonable. We do have a weapon. Might as well put her at ease.\n"
            menu:
                extend ""

                "{i} [[Sit where you were told to sit.]{/i}":
                    $ prisoner_position = "close"
                    voice "audio/voices/ch2/prisoner/_basement/narrator/4.flac"
                    play audio "audio/final/_prisoner_sit.flac"
                    show bg onlayer back at collapse
                    show prisoner c neutral onlayer back at collapse
                    with dissolve
                    n "You do as she asks and sit on the floor, still a good distance away from her.\n"
                    voice "audio/voices/ch2/prisoner/_basement/princess/6.flac"
                    show prisoner c neutral talk onlayer back
                    with dissolve
                    sp "Thank you. Now, what are your intentions for me?\n"
                    show prisoner c neutral onlayer back

                "{i} [[Sit closer.]{/i}":
                    $ prisoner_position = "tooclose"
                    $ prisoner_sit_closer = True
                    jump prisoner_strangle_join

            jump prisoner_menu

        "{i} [[Slay the Princess.]{/i}" if blade_held and prisoner_can_slay_attempt:
            if grey_encountered:
                $ prisoner_can_slay_attempt = False
                voice "audio/voices/mound/bonus/path.flac"
                mound "This path is already worn by travel and has been seen by one of my many eyes. You cannot walk it again. Change your course.\n"
                jump prisoner_encounter_start
            $ prisoner_attack = True
            $ prisoner_position = "attack"
            voice "audio/voices/ch2/prisoner/_basement/narrator/5.flac"
            play audio "audio/one_shot/footstep_run_medium.flac"
            hide farback onlayer farback
            hide bg onlayer back
            hide prisoner onlayer back
            scene bg prisoner basement close onlayer back at zoom_instant, Position(ypos=1125)
            show prisoner c skeptical onlayer back at zoom_instant, Position(ypos=1125)
            show speedlines onlayer front at zoom_instant, Position(ypos=1125)
            with Dissolve(1.0)
            n "Without a moment of hesitation, you charge the Princess, your blade primed to deliver a lethal strike.\n"
            voice "audio/voices/ch2/prisoner/_basement/princess/7.flac"
            show prisoner c skeptical onlayer back at zoom_instant
            with dissolve
            sp "Hm.\n"
            jump prisoner_strangle_join


label prisoner_narrator_loop_join:
    $ prisoner_narrator_agree = True
    $ prisoner_go_to_narrator_reveal = False
    if prisoner_1_forest_share_loop_insist:
        voice "audio/voices/ch2/prisoner/_basement/narrator/6.flac"
        n "I guess what you said back in the woods really was true.\n"
    elif prisoner_1_forest_share_loop:
        voice "audio/voices/ch2/prisoner/_basement/narrator/7.flac"
        n "First you make a comment about having been here before, and now this.\n"
    else:
        voice "audio/voices/ch2/prisoner/_basement/narrator/8.flac"
        n "So you've already been here.\n"
    voice "audio/voices/ch2/prisoner/_basement/narrator/9.flac"
    n "{i}Sigh.{/i} As much as I'd like to remain in denial, it's no use. This has complicated things.\n"
    voice "audio/voices/ch2/prisoner/_basement/skeptic/3.flac"
    skeptic "It's complicated things how, exactly?\n"
    voice "audio/voices/ch2/prisoner/_basement/narrator/10.flac"
    n "Ideally this was supposed to be one-and-done. You go to the cabin, you heroically slay the Princess, and in the process, you save the entire world from being damned to oblivion.\n"
    voice "audio/voices/ch2/prisoner/_basement/narrator/11.flac"
    n "This situation right now, where you're getting a second shot at things, is a contingency.\n"
    voice "audio/voices/ch2/prisoner/_basement/skeptic/4.flac"
    skeptic "A contingency for what?\n"
    voice "audio/voices/ch2/prisoner/_basement/narrator/12.flac"
    n "For you failing. Obviously. And you being here means that things are going to be a lot harder than they were. I really shouldn't say anything else, I'm just going to make it worse. Just... Good luck.\n"
    if prisoner_1_forest_share_loop_insist:
        voice "audio/voices/ch2/prisoner/_basement/skeptic/5.flac"
        skeptic "Now hold on. If you knew this could happen, why didn't you believe us back in the woods? Why lay out all of those hypotheticals? We didn't have to talk in circles.\n"
        voice "audio/voices/ch2/prisoner/_basement/narrator/13.flac"
        n "I needed you to believe this was your first time here, even if that wasn't the truth. I hoped if I pushed back hard enough I could cram this seeping mess back into the bottle.\n"
    else:
        voice "audio/voices/ch2/prisoner/_basement/skeptic/6.flac"
        skeptic "If you knew this could happen, why didn't you tell us? All of this is incredibly valuable information. It would have changed our actions considerably.\n"
        voice "audio/voices/ch2/prisoner/_basement/narrator/14.flac"
        n "I needed you to be in the dark for as long as I could keep you there. It's important. Necessary, even.\n"

    voice "audio/voices/ch2/prisoner/_basement/narrator/15.flac"
    n "And... maybe I wanted to be the first version of me that you met. I didn't want to be confronted by the alternative.\n"
    voice "audio/voices/ch2/prisoner/_basement/skeptic/7.flac"
    skeptic "That's pathetic.\n"
    voice "audio/voices/ch2/prisoner/_basement/narrator/16.flac"
    n "I never said I wasn't.\n"
    voice "audio/voices/ch2/prisoner/_basement/hero/3a.flac"
    hero "I get it. It would be pretty upsetting, wouldn't it? To know that you might not be the first version of yourself? At least we can remember what happened before, seems like we should count ourselves lucky for that.\n"
    voice "audio/voices/ch2/prisoner/_basement/narrator/17.flac"
    n "Exactly. He gets it. You're lucky. So don't waste that luck by messing it up again, all right?\n"
    voice "audio/voices/ch2/prisoner/_basement/skeptic/8.flac"
    skeptic "Moving on. Why is it important for us to be ignorant? How is it ever helpful to be in the dark?\n"
    voice "audio/voices/ch2/prisoner/_basement/narrator/18.flac"
    n "The more I say, the more your mind will swim into dangerous waters. Even saying that is too much.\n"
    voice "audio/voices/ch2/prisoner/_basement/narrator/19.flac"
    n "Your success hinges on you having imperfect information. For the sake of the entire world, you need to accept that.\n"
    voice "audio/voices/ch2/prisoner/_basement/skeptic/9.flac"
    skeptic "I won't.\n"
    voice "audio/voices/ch2/prisoner/_basement/hero/4.flac"
    hero "Just give it a rest. This isn't helping.\n"

    if prisoner_position == "start":
        voice "audio/voices/ch2/prisoner/_basement/princess/8.flac"
        show prisoner d talk onlayer back
        with dissolve
        sp "I've learned a lot of patience in my life, but that doesn't mean you should just stand around wasting everyone's time. Sit down.\n"
        show prisoner d neutral onlayer back
        jump prisoner_encounter_start
    voice "audio/voices/ch2/prisoner/_basement/princess/9a.flac"
    show prisoner c sharp talk onlayer back
    with dissolve
    sp "Focus. This is a serious situation, you shouldn't be daydreaming.\n"
    show prisoner c sharp onlayer back
    with dissolve
    jump prisoner_menu

label prisoner_menu:
    default prisoner_intentions_ask = False
    default prisoner_intentions_share = False
    default prisoner_neck_shackle_ask = False
    default prisoner_abandoned_comment_flag = False
    default prisoner_player_attempt_cut = False
    default prisoner_go_to_narrator_reveal = False
    default prisoner_door_open_beg = False
    default prisoner_intentions_explore = False
    default prisoner_menu_count = 0
    default prisoner_death_ask = False
    default prisoner_head_ask = False
    default prisoner_other_chain_ask = False
    default prisoner_what_do = False
    default prisoner_no_give_explore = False
    default prisoner_threaten_1 = False
    default prisoner_threaten_2 = False
    default prisoner_negotiate_attempt = False
    default prisoner_try_shackle = False
    default prisoner_patient_line = False
    $ prisoner_position = "close"
    menu:
        extend ""

        "{i} (Explore) [[Inspect the shackle.]{/i}" if prisoner_other_chain_ask and prisoner_try_shackle == False:
            $ prisoner_try_shackle = True
            voice "audio/voices/ch2/prisoner/_basement/narrator/31.flac"
            n "I wouldn't do that if I were you.\n"
            voice "audio/voices/ch2/prisoner/_basement/skeptic/25.flac"
            skeptic "And why is that?\n"
            voice "audio/voices/ch2/prisoner/_basement/narrator/32.flac"
            n "Do I even need to explain myself? It's a shackle, and it's one without a key. Do you want to be stuck here like she is?\n"
            voice "audio/voices/ch2/prisoner/_basement/skeptic/26.flac"
            skeptic "And what? Is it going to lock the second we put our wrist into it?\n"
            voice "audio/voices/ch2/prisoner/_basement/narrator/33.flac"
            n "I don't know. Maybe it will.\n"
            voice "audio/voices/ch2/prisoner/_basement/skeptic/27.flac"
            skeptic "He doesn't want us to look at it. That's all the reason we need to investigate.\n"
            voice "audio/voices/ch2/prisoner/_basement/hero/13.flac"
            hero "But what if He's telling the truth?\n"
            voice "audio/voices/ch2/prisoner/_basement/skeptic/28.flac"
            skeptic "He isn't.\n"
            voice "audio/voices/ch2/prisoner/_basement/narrator/34.flac"
            n "I am.\n"
            menu:
                extend ""

                "{i} [[Inspect the shackle.]{/i}":
                    jump prisoner_self_prison

                "{i} [[Let it go.]{/i}":
                    voice "audio/voices/ch2/prisoner/_basement/narrator/35.flac"
                    n "Good. Forget you ever saw it.\n"
                    voice "audio/voices/ch2/prisoner/_basement/skeptic/29.flac"
                    skeptic "Nice try, but I won't. Specifically because you told me to.\n"
                    jump prisoner_menu

        "{i} (Explore) Hey! Let me out of here! Open the door!{/i}" if prisoner_locked and prisoner_door_open_beg == False:
            $ prisoner_menu_count += 1
            $ prisoner_door_open_beg = True
            voice "audio/voices/ch2/prisoner/_basement/narrator/21.flac"
            n "You have everything you need to deal with her and save the world. I'm sure the door will open as soon as you finish your incredibly important task.\n"
            voice "audio/voices/ch2/prisoner/_basement/hero/5.flac"
            hero "It doesn't sound like we'll be able to talk Him into letting us leave.\n"
            voice "audio/voices/ch2/prisoner/_basement/skeptic/11.flac"
            skeptic "Yeah, not a chance. He's single-minded about this. But don't worry, there are plenty of things that aren't in His control.\n"
            voice "audio/voices/ch2/prisoner/_basement/narrator/22.flac"
            n "Oh? For instance...?\n"
            voice "audio/voices/ch2/prisoner/_basement/skeptic/12.flac"
            skeptic "Us. Her. But mostly us. If He didn't have his limits, we wouldn't be here. Not like this.\n"
            jump prisoner_menu

        "{i} (Explore) ''You were asking about my intentions earlier. What did you mean by that?''{/i}" if prisoner_intentions_explore == False and prisoner_menu_count != 0:
            jump prisoner_intentions_join

        "{i} (Explore) ''My intentions? What do you mean?''{/i}" if prisoner_intentions_explore == False and prisoner_menu_count == 0:
            label prisoner_intentions_join:
                $ prisoner_menu_count += 1
                $ prisoner_intentions_explore = True
                voice "audio/voices/ch2/prisoner/_basement/princess/10.flac"
                show prisoner c surprise talk onlayer back
                with dissolve
                sp "Yes. Your intentions. You have a knife. What are you going to do with it? Why are you here?\n"
                if prisoner_narrator_agree:
                    voice "audio/voices/ch2/prisoner/_basement/princess/11.flac"
                    show prisoner c shrug talk onlayer back
                    with dissolve
                    sp "There isn't a keyhole in these shackles, and I don't see any keys in your hands, either. So I'm afraid my only way out is another surgical removal.\n"
                else:
                    voice "audio/voices/ch2/prisoner/_basement/princess/12.flac"
                    show prisoner c shrug talk onlayer back
                    with dissolve
                    sp "There isn't a keyhole in these shackles, so I'm afraid my only way out is surgical removal.\n"
                voice "audio/voices/ch2/prisoner/_basement/hero/6.flac"
                show prisoner c neutral onlayer back
                with dissolve
                hero "Is she forgetting about the shackle on her neck?!\n"
                voice "audio/voices/ch2/prisoner/_basement/skeptic/13.flac"
                skeptic "Or does she think she'd survive a beheading?\n"
                voice "audio/voices/ch2/prisoner/_basement/narrator/23.flac"
                n "You're right. Maybe she's delusional. All the more reason not to trust her.\n"
                voice "audio/voices/ch2/prisoner/_basement/skeptic/14.flac"
                skeptic "Unless she really could survive.\n"
                voice "audio/voices/ch2/prisoner/_basement/princess/13.flac"
                show prisoner c closed talk onlayer back
                with dissolve
                sp "Though I suppose you could just be here to kill me. But I don't think that's in either of our best interests.\n"
                show prisoner c neutral onlayer back
                with dissolve
                jump prisoner_menu


        "{i} (Explore) ''I've been here before. Am I the only one who remembers that?''{/i}" if prisoner_narrator_agree == False:
            $ prisoner_menu_count += 1
            voice "audio/voices/ch2/prisoner/_basement/princess/14.flac"
            show prisoner c explain talk onlayer back
            with dissolve
            sp "Oh? Are we acknowledging that? I thought we weren't going to give away the game. But yeah. I remember.\n"
            show prisoner c surprise onlayer back
            with dissolve
            jump prisoner_narrator_loop_join

        "{i} (Explore) ''What happened after I died last time?''{/i}" if prisoner_death_ask == False:
            label prisoner_what_happened_died:
                $ prisoner_death_ask = True
                $ prisoner_menu_count += 1
                if prisoner_narrator_agree == False:
                    voice "audio/voices/ch2/prisoner/_basement/princess/15.flac"
                    show prisoner c surprise talk onlayer back
                    with dissolve
                    sp "Oh? Are we talking about that? I thought we weren't going to give away the game. But sure, I'll fill you in.\n"
                voice "audio/voices/ch2/prisoner/_basement/princess/16.flac"
                show prisoner c explain talk onlayer back
                with dissolve
                sp "Nothing happened. You died. I went upstairs. I couldn't leave. I found myself in a new place, in chains again. More of them.\n"
                voice "audio/voices/ch2/prisoner/_basement/princess/17.flac"
                show prisoner c closed talk onlayer back
                with dissolve
                sp "And now you're back.\n"
                voice "audio/voices/ch2/prisoner/_basement/skeptic/15.flac"
                show prisoner c neutral onlayer back
                with dissolve
                skeptic "Is that really all she knows?\n"
                voice "audio/voices/ch2/prisoner/_basement/hero/7.flac"
                hero "It's not like we have much of a clue about how things work. And she's probably even more in the dark than we are.\n"
                voice "audio/voices/ch2/prisoner/_basement/princess/18.flac"
                show prisoner c neutral talk onlayer back
                with dissolve
                sp "You're looking at me like I might be hiding something. I'm not.\n"
                voice "audio/voices/ch2/prisoner/_basement/skeptic/16.flac"
                show prisoner c neutral onlayer back
                with dissolve
                skeptic "I guess it's possible she really doesn't know anything. Maybe both of us are stuck in this loop without any idea why or how.\n"
                if prisoner_narrator_agree == False:
                    jump prisoner_narrator_loop_join
                jump prisoner_menu

        "{i} (Explore) ''How am I supposed to cut you out? If you didn't notice, your head is in a shackle, too.''{/i}" if prisoner_intentions_explore and prisoner_head_ask == False and prisoner_what_do == False:
            $ prisoner_head_ask = True
            $ prisoner_menu_count += 1
            $ prisoner_what_do = True
            voice "audio/voices/ch2/prisoner/_basement/princess/19.flac"
            show prisoner c skeptical talk onlayer back
            with dissolve
            sp "Hah. No. Like I trust you to come any closer with that knife. All you're going to do is hand it to me, and watch me work.\n"
            voice "audio/voices/ch2/prisoner/_basement/hero/8.flac"
            show prisoner c sharp onlayer back
            with dissolve
            hero "But she would have to cut her head off, right? She can't be suggesting that.\n"
            voice "audio/voices/ch2/prisoner/_basement/skeptic/17.flac"
            skeptic "She certainly seems confident. Maybe she knows something we don't.\n"
            voice "audio/voices/ch2/prisoner/_basement/narrator/24.flac"
            n "Or maybe you should consider the most likely scenario: she's bluffing so she can disarm you.\n"
            jump prisoner_what_do_join

        "{i} (Explore) ''That other chain on the wall... who is it for?''{/i}" if prisoner_other_chain_ask == False:
            $ prisoner_other_chain_ask = True
            $ prisoner_menu_count += 1
            voice "audio/voices/ch2/prisoner/_basement/princess/20.flac"
            show prisoner c shrug talk onlayer back
            with dissolve
            sp "I don't know. But you could always try it on.\n"
            voice "audio/voices/ch2/prisoner/_basement/princess/21.flac"
            show prisoner c smile talk onlayer back
            with dissolve
            sp "Maybe it'll fit.\n"
            voice "audio/voices/ch2/prisoner/_basement/narrator/25.flac"
            show prisoner c neutral onlayer back
            with dissolve
            n "I hope I don't actually have to say this, but please don't lock yourself in chains. We need you ambulatory if you're going to save the world.\n"
            jump prisoner_menu

        "{i} (Explore) ''What would you have me do?''{/i}" if prisoner_what_do == False:
            $ prisoner_what_do = True
            $ prisoner_menu_count += 1
            voice "audio/voices/ch2/prisoner/_basement/princess/22.flac"
            show prisoner c neutral talk onlayer back
            with dissolve
            sp "Let me borrow that knife.\n"
            voice "audio/voices/ch2/prisoner/_basement/princess/23.flac"
            show prisoner c shrug talk onlayer back
            with dissolve
            sp "Don't worry, you'll get it back.\n"
            voice "audio/voices/ch2/prisoner/_basement/hero/9.flac"
            show prisoner c sharp onlayer back
            with dissolve
            hero "That's... ominous.\n"
            voice "audio/voices/ch2/prisoner/_basement/skeptic/18.flac"
            skeptic "But she seems confident. Whatever it is she has planned, I think she knows what she's doing.\n"
            voice "audio/voices/ch2/prisoner/_basement/narrator/26.flac"
            n "Oh, please. She's just putting on act to disarm you. That much should be obvious. And in case you need to hear a voice of reason, it would obviously be unwise to give away your only weapon.\n"
            label prisoner_what_do_join:
                voice "audio/voices/ch2/prisoner/_basement/skeptic/19.flac"
                skeptic "Though if she isn't bluffing, whatever she has planned might be for her benefit alone. There's no guarantee that what's good for her is good for us.\n"
                voice "audio/voices/ch2/prisoner/_basement/hero/10.flac"
                hero "So... what should we do?\n"
                voice "audio/voices/ch2/prisoner/_basement/skeptic/20.flac"
                skeptic "I don't know. I'm just spelling out our options. Listing the pros and cons.\n"
                voice "audio/voices/ch2/prisoner/_basement/narrator/27.flac"
                n "Then let me help you. I'll start with the cons. If you're handing her your weapon, the cons are that she might use it to escape and end the entire world. And she might use it to kill you.\n"
                voice "audio/voices/ch2/prisoner/_basement/hero/11.flac"
                hero "That doesn't sound great. What about the pros?\n"
                voice "audio/voices/ch2/prisoner/_basement/narrator/28.flac"
                n "There are none.\n"
                voice "audio/voices/ch2/prisoner/_basement/skeptic/21.flac"
                skeptic "The pros are that we can't trust Him, possibly even more than we can't trust her, and whatever she has planned could do something to mess with what He has planned. Or maybe they're both screwing us over in their own ways.\n"
                jump prisoner_menu

        "{i} (Explore) ''I'm not giving you a weapon.''{/i}" if prisoner_what_do and prisoner_no_give_explore == False:
            $ prisoner_no_give_explore = True
            jump prisoner_no_give_explore_join

        "{i} (Explore) ''You realize that I have as much reason to distrust you as you have to distrust me, right?''{/i}" if prisoner_what_do and prisoner_patient_line == False:
            voice "audio/voices/ch2/prisoner/_basement/princess/24.flac"
            show prisoner c neutral talk onlayer back
            with dissolve
            sp "I do. So I guess this all comes down to which of us caves first. And it's not going to be me.\n"
            $ prisoner_patient_line = True
            $ prisoner_menu_count += 1
            voice "audio/voices/ch2/prisoner/_basement/princess/25.flac"
            show prisoner c shrug talk onlayer back
            with dissolve
            sp "I'm extremely patient.\n"
            voice "audio/voices/ch2/prisoner/_basement/skeptic/22.flac"
            show prisoner c neutral onlayer back
            with dissolve
            skeptic "It's probably better if we take action, anyway. No use trying to wait her out. That's playing to her strengths.\n"
            jump prisoner_menu

        "{i} (Explore) ''If you don't give up now, then I have no choice but to slay you.''{/i}" if prisoner_no_give_explore and prisoner_threaten_1 == False:
            $ prisoner_threaten_1 = True
            $ prisoner_menu_count += 1
            voice "audio/voices/ch2/prisoner/_basement/princess/26.flac"
            show prisoner c sharp talk onlayer back
            with dissolve
            sp "That attitude is exactly why I don't trust you to get close while you're holding a knife.\n"
            voice "audio/voices/ch2/prisoner/_basement/princess/27.flac"
            show prisoner c skeptical talk onlayer back
            with dissolve
            sp "If that's unacceptable to you, then try me. See what happens.\n"
            voice "audio/voices/ch2/prisoner/_basement/narrator/29.flac"
            show prisoner c skeptical onlayer back
            with dissolve
            n "She sure was quick to threaten you, wasn't she? Stop hesitating already, you know you can't trust her.\n"
            voice "audio/voices/ch2/prisoner/_basement/skeptic/23.flac"
            skeptic "Both of them are using the same argument. It's not making it any easier to pick a side.\n"
            jump prisoner_menu

        "{i} (Explore) ''I'm not giving you a weapon. In case you've forgotten, you killed me with it last time.''{/i}" if prisoner_no_give_explore == False and prisoner_what_do:
            $ prisoner_no_give_explore = True
            $ prisoner_go_to_narrator_reveal = True
            $ prisoner_menu_count += 1
            if prisoner_narrator_agree == False:
                voice "audio/voices/ch2/prisoner/_basement/princess/28.flac"
                show prisoner c shrug talk onlayer back
                with dissolve
                sp "Oh? Are we talking about that? I thought we weren't going to give away the game.\n"
            voice "audio/voices/ch2/prisoner/_basement/princess/29.flac"
            show prisoner c sharp talk onlayer back
            with dissolve
            sp "But sure, let's talk about what happened. Because what happened is exactly my issue.\n"
            jump prisoner_no_give_explore_join

        "{i} (Explore) ''You're the one in chains. If anyone should be to negotiating here, it's you, not me.''{/i}" if prisoner_no_give_explore and prisoner_negotiate_attempt == False:
            $ prisoner_negotiate_attempt = True
            $ prisoner_menu_count += 1
            if prisoner_locked:
                voice "audio/voices/ch2/prisoner/_basement/princess/31.flac"
                show prisoner c shrug talk onlayer back
                with dissolve
                sp "I might be the one in chains but we're both locked in here. The only thing you have to bargain with is that scrap of metal. Admittedly, it's a scrap of metal that I want, but...\n"
            else:
                voice "audio/voices/ch2/prisoner/_basement/princess/32.flac"
                show prisoner c smile talk onlayer back
                with dissolve
                sp "Usually, you'd be right. But this isn't exactly a usual situation. I'm not someone you can wait out.\n"
            if prisoner_patient_line == False:
                $ prisoner_patient_line = True
                voice "audio/voices/ch2/prisoner/_basement/princess/33.flac"
                show prisoner c neutral talk onlayer back
                with dissolve
                sp "You'll find that I'm extremely patient.\n"
            else:
                voice "audio/voices/ch2/prisoner/_basement/princess/34.flac"
                show prisoner c neutral talk onlayer back
                with dissolve
                sp "We've already been over this. I'm more patient than you'll ever be.\n"
            show prisoner c neutral onlayer back
            with dissolve
            jump prisoner_menu

        "{i} (Explore) ''{b}I{/b} can cut you out of here. I'm not giving you a weapon.''{/i}" if prisoner_what_do and prisoner_no_give_explore == False:
            $ prisoner_no_give_explore = True
            $ prisoner_menu_count += 1
            label prisoner_no_give_explore_join:
                if prisoner_narrator_agree:
                    voice "audio/voices/ch2/prisoner/_basement/princess/35.flac"
                    show prisoner c sharp talk onlayer back
                    with dissolve
                    sp "The last time we met, your body tried to kill me.\n"
            voice "audio/voices/ch2/prisoner/_basement/princess/36.flac"
            show prisoner c explain talk onlayer back
            with dissolve
            sp "If you take a moment to imagine yourself in my position, I think you'll understand why letting you near me with that thing is untenable.\n"
            voice "audio/voices/ch2/prisoner/_basement/princess/37.flac"
            show prisoner c sharp talk onlayer back
            with dissolve
            sp "So be a good bird and hand it over.\n"
            if prisoner_narrator_agree:
                voice "audio/voices/ch2/prisoner/_basement/princess/38.flac"
                show prisoner c skeptical talk onlayer back
                with dissolve
                sp "And if being nice isn't enough motivation? Well, I think you're aware that I'm not afraid to resort to violence.\n"
            else:
                voice "audio/voices/ch2/prisoner/_basement/princess/39.flac"
                show prisoner c skeptical talk onlayer back
                with dissolve
                sp "And if being nice isn't enough motivation? Well, I'm not afraid to resort to violence.\n"
            voice "audio/voices/ch2/prisoner/_basement/princess/40.flac"
            show prisoner c neutral talk onlayer back
            with dissolve
            sp "If you come near me with that thing I will strangle you with these chains.\n"
            voice "audio/voices/ch2/prisoner/_basement/hero/12.flac"
            show prisoner c neutral onlayer back
            with dissolve
            hero "She doesn't beat around the bush, does she?\n"
            voice "audio/voices/ch2/prisoner/_basement/narrator/30.flac"
            n "Yes, it's almost like she's a fundamentally bad person who wishes to inflict pain on others.\n"
            voice "audio/voices/ch2/prisoner/_basement/skeptic/24.flac"
            skeptic "Or it's another bluff.\n"
            voice "audio/voices/ch2/prisoner/_basement/princess/41.flac"
            show prisoner c explain talk onlayer back
            with dissolve
            sp "No hard feelings, of course. But you should be aware of my position.\n"
            if prisoner_narrator_agree == False:
                jump prisoner_narrator_loop_join
            jump prisoner_menu

        "{i} ''Okay. I'm trusting you.'' [[Give her the knife.]{/i}" if prisoner_what_do:
            jump prisoner_knife_given

        "{i} ''If you want to leave, I'm going to be the one with the weapon. Deal with it.'' [[Cut her out on your own.]{/i}" if prisoner_what_do:
            $ prisoner_player_attempt_cut = True
            jump prisoner_strangle_join

        "{i} ''If that's how you're going to be, then I guess I have to do this.'' [[Slay the Princess.]{/i}" if blade_held and prisoner_no_give_explore and prisoner_can_slay_attempt:
            if grey_encountered:
                $ prisoner_can_slay_attempt = False
                voice "audio/voices/mound/bonus/path.flac"
                mound "This path is already worn by travel and has been seen by one of my many eyes. You cannot walk it again. Change your course.\n"
                jump prisoner_menu
            $ prisoner_attack = True
            voice "audio/voices/ch2/prisoner/_basement/princess/42.flac"
            sp "You don't have to do anything, but fine. Let's see if you'll live to regret trying to kill me.\n"
            jump prisoner_strangle_join

        "{i} ''It seems I don't have much of a choice. I'm sorry.'' [[Slay the Princess.]{/i}" if blade_held and prisoner_locked and prisoner_can_slay_attempt:
            if grey_encountered:
                $ prisoner_can_slay_attempt = False
                voice "audio/voices/mound/bonus/path.flac"
                mound "This path is already worn by travel and has been seen by one of my many eyes. You cannot walk it again. Change your course.\n"
                jump prisoner_menu
            $ prisoner_attack = True
            voice "audio/voices/ch2/prisoner/_basement/princess/43.flac"
            show prisoner c sharp talk onlayer back
            with dissolve
            sp "Sorry doesn't cut it.\n"
            jump prisoner_strangle_join

        "{i} ''If you're so immovable, then I'm just going to leave you here. Bye!'' [[Leave the Princess in the basement.]{/i}" if prisoner_locked == False and (prisoner_negotiate_attempt or prisoner_threaten_1):
            $ prisoner_abandoned_comment_flag = True
            voice "audio/voices/ch2/prisoner/_basement/princess/44.flac"
            show prisoner c neutral talk onlayer back
            with dissolve
            sp "I think you'll regret this.\n"
            show prisoner c neutral onlayer back
            with dissolve
            jump prisoner_locked_join

        "{i} ''I think I'm just going to leave you here, actually. You're not much of a threat to anyone locked up like that. Bye!'' [[Leave the Princess in the basement.]{/i}" if prisoner_locked == False:
            $ prisoner_abandoned_comment_flag = True
            voice "audio/voices/ch2/prisoner/_basement/princess/45.flac"
            show prisoner c skeptical talk onlayer back
            with dissolve
            sp "Oh, you bastard! You'll regret this.\n"
            show prisoner c skeptical onlayer back
            with dissolve
            jump prisoner_locked_join

        "{i} [[Slay the Princess.]{/i}" if blade_held and prisoner_can_slay_attempt:
            if grey_encountered:
                $ prisoner_can_slay_attempt = False
                voice "audio/voices/mound/bonus/path.flac"
                mound "This path is already worn by travel and has been seen by one of my many eyes. You cannot walk it again. Change your course.\n"
                jump prisoner_menu
            $ prisoner_attack = True
            jump prisoner_strangle_join

label prisoner_self_prison:

    voice "audio/voices/ch2/prisoner/_basement/narrator/36.flac"
    play audio "audio/one_shot/footsteps_stone.flac"
    hide bg onlayer back
    hide prisoner onlayer back
    show bg prisoner shackle examine onlayer back at Position(ypos=1125)
    with Dissolve(1.0)
    n "{i}Sigh{/i}. Against your better judgment, you approach the chain dangling from the far wall. The Princess watches you with faux-disinterest as you inspect it, though she can't fully hide her curiosity.\n"
    voice "audio/voices/ch2/prisoner/_basement/narrator/37.flac"
    stop music
    play audio "audio/one_shot/chain_1.flac"
    show bg prisoner shackle examine lift onlayer back
    with dissolve
    n "I don't want to say what I'm supposed to say next.\n"
    voice "audio/voices/ch2/prisoner/_basement/hero/14.flac"
    hero "What is that supposed to mean? It sounds bad. Is it bad?\n"
    voice "audio/voices/ch2/prisoner/_basement/narrator/38.flac"
    n "Yes. It's bad.\n"
    voice "audio/voices/ch2/prisoner/_basement/skeptic/30.flac"
    skeptic "Come out and say it, then. You're just wasting time.\n"
    voice "audio/voices/ch2/prisoner/_basement/narrator/39.flac"
    play audio "audio/final/Adversary_ChainSTressBreaking_2.flac"
    show bg prisoner shackle examine latch onlayer back
    with dissolve
    n "Fine. As you hoist the shackle, its heft shifts within your grasp, as if pulled by some odd magnetism. Before you can so much as blink, it practically leaps from your hands, snapping around your neck.\n"
    $ blade_held = False
    $ default_mouse = "default"
    play audio "audio/one_shot/knife_bounce_several.flac"
    voice "audio/voices/ch2/prisoner/_basement/narrator/40.flac"
    n "And, as if your situation weren't bad enough, the same magnetism repels your blade, which is flung from your hand and sent skittering across the floor of the basement.\n"
    voice "audio/voices/ch2/prisoner/_basement/hero/15.flac"
    hero "Um... excuse me?\n"
    voice "audio/voices/ch2/prisoner/_basement/narrator/41.flac"
    n "Yes?\n"
    voice "audio/voices/ch2/prisoner/_basement/hero/16.flac"
    hero "Are we... stuck here now?\n"
    $ achievement.grant("ACH_PRISONER_STUCK")
    voice "audio/voices/ch2/prisoner/_basement/narrator/42.flac"
    play music "audio/_music/ch2/prisoner/The Prisoner Time Erodes Loop.flac" loop
    scene bg prisoner shackle together onlayer back at Position(ypos=1125)
    show knife prisoner waiting onlayer back at Position(ypos=1125)
    show prisoner shackle together onlayer back at Position(ypos=1125)
    with Dissolve(3.0)
    n "Yes.\n"
    voice "audio/voices/ch2/prisoner/_basement/princess/46a.flac"
    show prisoner shackle together talk onlayer back
    with dissolve
    sp "Huh. So it does fit. And I guess it doesn't like your knife. We're stuck here together, aren't we? That's funny.\n"
    show prisoner shackle together onlayer back
    with dissolve
    voice "audio/voices/ch2/prisoner/_basement/hero/17.flac"
    hero "What are we supposed to do now?\n"
    voice "audio/voices/ch2/prisoner/_basement/skeptic/31.flac"
    skeptic "Can't even cut ourselves out. Guess we'll... starve.\n"
    voice "audio/voices/ch2/prisoner/_basement/hero/18.flac"
    hero "That's horrible!\n"
    voice "audio/voices/ch2/prisoner/_basement/skeptic/32.flac"
    skeptic "It's not all bad. We learned a valuable piece of information.\n"
    voice "audio/voices/ch2/prisoner/_basement/hero/19.flac"
    hero "Not to touch things we're specifically told not to touch?\n"
    voice "audio/voices/ch2/prisoner/_basement/skeptic/33.flac"
    skeptic "No. That there's something special about this loose chain. It's clearly important.\n"

    label prisoner_self_prison_menu:
        default prisoner_self_prison_stuck = False
        default prisoner_self_prison_what = False
        default prisoner_self_prison_know = False
        default prisoner_self_prison_small_talk = False
        default prisoner_self_prison_count = 0
        menu:
            extend ""

            "{i} (Explore) ''So we're both stuck here.''{/i}" if prisoner_self_prison_stuck == False:
                $ prisoner_self_prison_stuck = True
                $ prisoner_self_prison_count += 1
                if prisoner_self_prison_small_talk == False:
                    voice "audio/voices/ch2/prisoner/_basement/princess/47.flac"
                    show prisoner shackle together talk onlayer back
                    with dissolve
                    sp "Yep.\n"
                    show prisoner shackle together onlayer back
                    with dissolve
                else:
                    sp "...\n"
                jump prisoner_self_prison_menu

            "{i} (Explore) ''What should we do?''{/i}" if prisoner_self_prison_what == False:
                $ prisoner_self_prison_what = True
                $ prisoner_self_prison_count += 1
                if prisoner_self_prison_small_talk == False:
                    voice "audio/voices/ch2/prisoner/_basement/princess/48.flac"
                    show prisoner shackle together talk onlayer back
                    with dissolve
                    sp "Wait, I guess. Maybe something else will happen. Maybe not.\n"
                    show prisoner shackle together onlayer back
                    with dissolve
                else:
                    sp "...\n"
                jump prisoner_self_prison_menu

            "{i} (Explore) ''Did you know that this was going to happen to me?''{/i}" if prisoner_self_prison_know == False:
                $ prisoner_self_prison_know = True
                $ prisoner_self_prison_count += 1
                if prisoner_self_prison_small_talk == False:
                    voice "audio/voices/ch2/prisoner/_basement/princess/49.flac"
                    show prisoner shackle together talk onlayer back
                    with dissolve
                    sp "No.\n"
                    show prisoner shackle together onlayer back
                    with dissolve
                else:
                    sp "...\n"
                jump prisoner_self_prison_menu

            "{i} (Explore) ''Not one for small talk, are you?''{/i}" if prisoner_self_prison_small_talk == False and prisoner_self_prison_count >= 2:
                $ prisoner_self_prison_small_talk = True
                voice "audio/voices/ch2/prisoner/_basement/princess/50.flac"
                show prisoner shackle together talk onlayer back
                with dissolve
                sp "Nope.\n"
                voice "audio/voices/ch2/prisoner/_basement/hero/20.flac"
                show prisoner shackle together onlayer back
                with dissolve
                hero "That's rude.\n"
                jump prisoner_self_prison_menu

            "{i} [[Wait in silence.]{/i}":
                voice "audio/voices/ch2/prisoner/_basement/narrator/43.flac"
                n "You and the Princess wait in silence, though neither of you knows what you're waiting for. But you're waiting for something. You're waiting for anything.\n"
                voice "audio/voices/ch2/prisoner/_basement/hero/21.flac"
                hero "This is so boring!\n"
                voice "audio/voices/ch2/prisoner/_basement/skeptic/34.flac"
                skeptic "There must be something we can do to get out of here. There must be something we're missing.\n"
                voice "audio/voices/ch2/prisoner/_basement/narrator/44.flac"
                n "But there isn't.\n"
                voice "audio/voices/ch2/prisoner/_basement/narrator/45.flac"
                n "Time passes.\n"
                voice "audio/voices/ch2/prisoner/_basement/narrator/46.flac"
                n "It passes, and passes, and passes, and the basement of the cabin remains much the same. It is cold, and silent.\n"
                voice "audio/voices/ch2/prisoner/_basement/hero/22.flac"
                hero "At least the world is safe.\n"
                voice "audio/voices/ch2/prisoner/_basement/narrator/47.flac"
                n "It isn't. You're stuck, too far away from both the Princess and your blade to do much of anything.\n"
                voice "audio/voices/ch2/prisoner/_basement/hero/23.flac"
                hero "But she's not ending anything! She's just sitting there.\n"
                voice "audio/voices/ch2/prisoner/_basement/narrator/48.flac"
                n "Her very existence is a threat. It harms everything around it.\n"
                voice "audio/voices/ch2/prisoner/_basement/skeptic/35.flac"
                skeptic "How exactly does that work?\n"
                voice "audio/voices/ch2/prisoner/_basement/narrator/49.flac"
                n "It just does.\n"
                voice "audio/voices/ch2/prisoner/_basement/skeptic/36.flac"
                skeptic "But-\n{w=0.3}{nw}"
                show screen disableclick(0.5)
                voice "audio/voices/ch2/prisoner/_basement/narrator/50.flac"
                n "Your line of questioning is interrupted by the passage of even more time, and after that, even more time passes again.\n"
                voice "audio/voices/ch2/prisoner/_basement/hero/24.flac"
                hero "And let me guess! The cabin remains the same.\n"
                voice "audio/voices/ch2/prisoner/_basement/skeptic/37.flac"
                skeptic "If time is passing, the cabin can't be the same. Even if the differences are small they have to exist. That's just how things work.\n"
                voice "audio/voices/ch2/prisoner/_basement/narrator/51.flac"
                show bg prisoner shackle time1 onlayer back
                with Dissolve(5.0)
                n "I suppose you're correct. Things are changing. The differences are small at first. A bit of weathering here, a bit of erosion there. But then they get larger. And larger.\n"
                label prisoner_forever_menu_2:
                    default prisoner_forever_menu_2_explore = False
                    menu:
                        extend ""

                        "{i} (Explore) ''Hey, have you noticed the basement changing?''{/i}" if prisoner_forever_menu_2_explore == False:
                            $ prisoner_forever_menu_2_explore = True
                            if prisoner_self_prison_small_talk:
                                voice "audio/voices/ch2/prisoner/_basement/princess/51.flac"
                                show prisoner shackle together talk onlayer back
                                with dissolve
                                sp "I don't like small talk, remember?\n"
                                voice "audio/voices/ch2/prisoner/_basement/hero/25.flac"
                                show prisoner shackle together onlayer back
                                with dissolve
                                hero "Still rude.\n"
                            else:
                                voice "audio/voices/ch2/prisoner/_basement/princess/52.flac"
                                show prisoner shackle together talk onlayer back
                                with dissolve
                                sp "I don't like small talk.\n"
                                voice "audio/voices/ch2/prisoner/_basement/hero/20.flac"
                                show prisoner shackle together onlayer back
                                with dissolve
                                hero "That's rude.\n"
                            jump prisoner_forever_menu_2

                        "{i} [[Continue to wait in silence.]{/i}":
                            voice "audio/voices/ch2/prisoner/_basement/narrator/52.flac"
                            show bg prisoner shackle time2 onlayer back
                            with Dissolve(5.0)
                            n "You continue to wait in silence, and the cabin continues to change. The decay comes faster now. You can see earth through holes in the stonework, can watch lichen spread along the seams of the walls.\n"
                            voice "audio/voices/ch2/prisoner/_basement/skeptic/38.flac"
                            skeptic "That doesn't make sense. Has our entire concept of time changed? What happened to starving? We should have died by now if the rocks around us are starting to erode.\n"
                            voice "audio/voices/ch2/prisoner/_basement/hero/26.flac"
                            hero "She hasn't starved.\n"
                            voice "audio/voices/ch2/prisoner/_basement/skeptic/39.flac"
                            skeptic "I guess she hasn't.\n"
                            voice "audio/voices/ch2/prisoner/_basement/narrator/53.flac"
                            hide knife onlayer back
                            show bg prisoner shackle time3 onlayer back
                            with Dissolve(5.0)
                            n "Even more silent time passes as you watch roots push themselves through the increasingly porous walls of the basement. Dirt seeps inside, flowing across the stone floor like a liquid, covering the ground and threatening to swallow you both. Time continues to pass. And pass. And pass.\n"
                            voice "audio/voices/ch2/prisoner/_basement/narrator/54a.flac"
                            show farback prisoner shackle time4 onlayer farback at Position(ypos=1125)
                            show bg prisoner shackle time4 onlayer back
                            show prisoner shackle free onlayer back
                            n "Until suddenly, there are no walls. And then-\n"
                            voice "audio/voices/ch2/prisoner/_basement/hero/27.flac"
                            stop music fadeout 15.0
                            stop sound fadeout 20.0
                            stop tertiary fadeout 20.0
                            play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 15.0
                            show quiet creep1 onlayer farback at Position(ypos=1125)
                            with dissolve
                            hero "... And?\n"
                            voice "audio/voices/ch2/prisoner/_basement/skeptic/40.flac"
                            show quiet creep2 onlayer farback at Position(ypos=1125)
                            with dissolve
                            skeptic "I think He's gone.\n"
                            voice "audio/voices/ch2/prisoner/_basement/princess/53.flac"
                            show prisoner shackle free talk onlayer back at Position(ypos=1125)
                            with dissolve
                            sp "Would you look at that? We made it out of the cabin, and nothing bad had to happen to either of us.\n"
                            $ gallery_prisoner.unlock_item(3)
                            $ gallery_prisoner.unlock_item(4)
                            $ gallery_prisoner.unlock_item(5)
                            $ gallery_prisoner.unlock_item(6)
                            $ renpy.save_persistent()
                            voice "audio/voices/ch2/prisoner/_basement/princess/54.flac"
                            hide quiet onlayer farback
                            hide prisoner onlayer back
                            show quiet creep3 onlayer back at Position(ypos=1125)
                            show prisoner shackle free cold onlayer back
                            with Dissolve(1.5)
                            sp "So this is the outside world. It's cold.\n"
                            play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                            hide prisoner onlayer back
                            show arms p shackle1 onlayer back at Position(ypos=1125)
                            show prisoner shackle free cold onlayer back at Position(ypos=1125)
                            with Dissolve(1.0)
                            $ renpy.pause(0.125)
                            show arms p shackle2 onlayer back at Position(ypos=1125)
                            show prisoner shackle free quiet onlayer back
                            with Dissolve(1.0)
                            $ renpy.pause(0.125)
                            hide prisoner onlayer front
                            hide prisoner onlayer back
                            show arms p shackle3 onlayer back at Position(ypos=1125)
                            with Dissolve(0.5)
                            $ renpy.pause(0.125)
                            show arms p shackle4 onlayer back at Position(ypos=1125)
                            with Dissolve(0.5)
                            $ renpy.pause(0.125)
                            hide arms onlayer back
                            with Dissolve(0.5)
                            $ renpy.pause(0.125)
                            $ blade_held = False
                            $ default_mouse = "default"
                            hide fore onlayer front
                            hide fore onlayer inyourface
                            hide farback onlayer farback
                            hide bg onlayer back
                            hide mid onlayer back
                            hide stars onlayer farback
                            hide bg onlayer back
                            hide quiet onlayer back
                            show farback quiet onlayer farback at Position(ypos=1125)
                            with Dissolve(4.0)
                            show mirror quiet distant onlayer back at Position(ypos=1125)
                            if loops_finished != 0:
                                truth "But you do not get the chance to respond, nor will you ever. It's time to leave. Memory returns.\n"
                            else:
                                truth "But you don't get the chance to respond. Something has taken her away, and it's left something else in her stead.\n"
                            $ prisoner_end = "stuck"
                            $ princess_free += 1
                            $ current_princess = "prisonerchain"
                            jump mirror_start

label prisoner_knife_given:

    default prisoner_decapitate = False
    $ prisoner_decapitate = True
    voice "audio/voices/ch2/prisoner/_basement/princess/55.flac"
    show prisoner c sharp talk onlayer back
    with dissolve
    sp "Slide it over.\n"
    voice "audio/voices/ch2/prisoner/_basement/narrator/55.flac"
    show prisoner c sharp onlayer back
    with dissolve
    n "No. Absolutely not. I am not letting you hand your only weapon over to the {i}world-ending{/i} Princess. Until you come up with any other idea-like, say, I don't know, doing your job and slaying her-you remain rigidly in place.\n"
    if prisoner_narrator_agree:
        voice "audio/voices/ch2/prisoner/_basement/skeptic/41.flac"
        skeptic "You tried this last time. Do you want to know how it went for you?\n"
        voice "audio/voices/ch2/prisoner/_basement/hero/28a.flac"
        hero "Oh, I remember! She killed us, which by your estimation, ended the world. Right?\n"
        voice "audio/voices/ch2/prisoner/_basement/narrator/56.flac"
        n "{i}Angry grumbling.{/i}\n"
        voice "audio/voices/ch2/prisoner/_basement/skeptic/42.flac"
        skeptic "Exactly. If I were you, I wouldn't be too keen on repeating your mistake. Hell, we could even force your hand and do it ourselves. I'm not afraid of dying again. Are you?\n"
        voice "audio/voices/ch2/prisoner/_basement/hero/29.flac"
        hero "A little.\n"
        voice "audio/voices/ch2/prisoner/_basement/narrator/57.flac"
        n "I think you got your point across. Fine.\n"
    else:
        voice "audio/voices/ch2/prisoner/_basement/skeptic/43.flac"
        skeptic "Do you think this will work? Interesting that you're only having us remain in place. It's almost like there are very real limits to your power.\n"
        voice "audio/voices/ch2/prisoner/_basement/narrator/58.flac"
        n "I don't know what you're talking about.\n"
        voice "audio/voices/ch2/prisoner/_basement/skeptic/44.flac"
        skeptic "The world ends if we fail, right? Her killing us might not be our only failure state, if you catch my meaning.\n"
        voice "audio/voices/ch2/prisoner/_basement/hero/30.flac"
        hero "I don't know where you're going with this. Could you explain?\n"
        voice "audio/voices/ch2/prisoner/_basement/narrator/59.flac"
        n "Yes. Explain it.\n"
        voice "audio/voices/ch2/prisoner/_basement/skeptic/45.flac"
        skeptic "Sure. I'm insinuating that we could kill ourself. Ruin this whole thing.\n"
        voice "audio/voices/ch2/prisoner/_basement/narrator/60.flac"
        n "You wouldn't.\n"
        voice "audio/voices/ch2/prisoner/_basement/skeptic/46.flac"
        skeptic "I'm not afraid of dying. Are you?\n"
        voice "audio/voices/ch2/prisoner/_basement/hero/29.flac"
        hero "A little.\n"
        voice "audio/voices/ch2/prisoner/_basement/narrator/61.flac"
        n "You got your point across. Fine.\n"

    $ blade_held = False
    $ default_mouse = "default"
    play audio "audio/one_shot/knife_bounce_several.flac"
    voice "audio/voices/ch2/prisoner/_basement/narrator/62.flac"
    $ blade_held = False
    $ default_mouse = "default"
    play audio "audio/one_shot/knife_bounce_several.flac"
    show knife prisoner floor onlayer back at Position(ypos=1125)
    with Dissolve(1.0)
    n "{i}Sigh{/i}. You slide the blade across the floor.\n"
    voice "audio/voices/ch2/prisoner/_basement/narrator/63.flac"
    play audio "audio/one_shot/knife_pickup.flac"
    hide knife onlayer back
    show prisoner c grab knife onlayer back
    with dissolve
    n "The Princess maintains unsettling eye contact as she reaches down to pick it up.\n"
    voice "audio/voices/ch2/prisoner/_basement/princess/56.flac"
    show prisoner c grab knife talk onlayer back
    with dissolve
    sp "Thanks.\n"
    stop music
    voice "audio/voices/ch2/prisoner/_basement/narrator/64.flac"
    play audio "audio/final/Prisoner_HairHeadStress_3.flac"
    show prisoner c knife neck onlayer back
    with dissolve
    n "She pulls up her hair, smiling slightly as she raises the blade to her throat.\n"
    label prisoner_knife_given_late_join:
        $ prisoner_decapitate = True
        voice "audio/voices/ch2/prisoner/_basement/hero/31.flac"
        hero "What is she doing?\n"
        voice "audio/voices/ch2/prisoner/_basement/narrator/65.flac"
        play music "audio/_music/ch2/prisoner/The Prisoner Headsaw.flac" loop
        play audio "audio/final/Prisoner_SawingThrough_1.flac"
        show prisoner c decap start onlayer back
        with dissolve
        n "She doesn't say another word as she cuts into her own neck.\n"
        voice "audio/voices/ch2/prisoner/_basement/hero/32a.flac"
        hero "No!\n"
        default prisoner_decapitation_watch = False
        menu:
            extend ""

            "{i} [[Look away.]{/i}":
                $ gallery_prisoner.unlock_item(7)
                $ renpy.save_persistent()
                hide bg onlayer back
                hide prisoner onlayer back
                scene bg black
                voice "audio/voices/ch2/prisoner/_basement/narrator/66.flac"
                play audio "audio/final/Prisoner_SawingThrough_1.flac"
                n "You close your eyes, but that doesn't stop you from hearing every grisly detail. The splitting of skin, the wet mulching of severed veins, the grinding of metal against bone.\n"
                voice "audio/voices/ch2/prisoner/_basement/narrator/67.flac"
                n "I'll be damned. She's actually doing your job for you. Why would she do that?\n"
                voice "audio/voices/ch2/prisoner/_basement/skeptic/47.flac"
                skeptic "Huh. So that's her play.\n"
                voice "audio/voices/ch2/prisoner/_basement/hero/33.flac"
                hero "Killing herself?!\n"
                voice "audio/voices/ch2/prisoner/_basement/skeptic/48.flac"
                play audio "audio/final/Prisoner_SawingBone_1.flac"
                skeptic "We don't know that she's dead yet. We're not even watching it happen. She could just be faking those sounds.\n"
                voice "audio/voices/ch2/prisoner/_basement/narrator/68.flac"
                play sound "audio/looping/uncomfortable ambiance heightened.ogg" loop
                stop music
                play audio "audio/final/Prisoner_NeckSnap_2.flac"
                n "And then finally you hear a snap, and an uneasy silence.\n"
                voice "audio/voices/ch2/prisoner/_basement/narrator/68a.flac"
                play audio "audio/final/_prisoner_tear.flac"
                n "There is a slow and fleshy tear. Hard to fake that.\n"
                voice "audio/voices/ch2/prisoner/_basement/hero/34.flac"
                hero "This is worse than watching.\n"
                voice "audio/voices/ch2/prisoner/_basement/skeptic/49.flac"
                skeptic "And yet our eyes are still closed.\n"
                voice "audio/voices/ch2/prisoner/_basement/narrator/69.flac"
                play secondary "audio/final/Prisoner_HeavyChains_1.flac"
                queue secondary "audio/final/Prisoner_BodyFall_1.flac"
                play audio "audio/final/_prisoner_bounce.flac"
                n "Finally, there's the soft thud of something roughly head-sized bouncing against the floor, and the clattering of chains as they drop along with it.\n"
                voice "audio/voices/ch2/prisoner/_basement/narrator/70.flac"
                n "I think you can open your eyes now.\n"
                scene bg prisoner basement close onlayer back at Position(ypos=1125)
                show prisoner c decap collapse onlayer back at Position(ypos=1125)
                with Dissolve(1.5)

            "{i} [[Watch in uneasy silence.]{/i}":
                $ gallery_prisoner.unlock_item(7)
                $ renpy.save_persistent()
                $ prisoner_decapitation_watch = True
                voice "audio/voices/ch2/prisoner/_basement/narrator/71a.flac"
                play audio "audio/final/Prisoner_SawingBone_1.flac"
                show prisoner c decap sequence 1 onlayer back
                with Dissolve(2.5)
                n "Her eyes stare forward, unblinking, as she saws through skin, veins, cartilage. At last she reaches bone, the blade grinding audibly against her vertebrae as it continues to slice its way through her neck.\n"
                voice "audio/voices/ch2/prisoner/_basement/narrator/67.flac"
                n "I'll be damned. She's actually doing your job for you. Why would she do that?\n"
                voice "audio/voices/ch2/prisoner/_basement/skeptic/50.flac"
                skeptic "Huh. So that's her play.\n"
                voice "audio/voices/ch2/prisoner/_basement/hero/33.flac"
                hero "Killing herself?!\n"
                voice "audio/voices/ch2/prisoner/_basement/skeptic/51.flac"
                skeptic "She isn't dead yet.\n"
                voice "audio/voices/ch2/prisoner/_basement/narrator/72.flac"
                play sound "audio/looping/uncomfortable ambiance heightened.ogg" loop
                stop music
                play audio "audio/final/Prisoner_NeckSnap_2.flac"
                show prisoner c decap sequence 2 onlayer back
                with Dissolve(0.125)
                n "Finally, you hear a snap. Her eye twitches.\n"
                voice "audio/voices/ch2/prisoner/_basement/narrator/73.flac"
                n "There's an uneasy silence. She remains motionless for a long moment, her twitching eye the only movement in the room, until at last it stops in an unsettling half-wink.\n"
                voice "audio/voices/ch2/prisoner/_basement/narrator/74.flac"
                play audio "audio/final/_prisoner_tear.flac"
                show prisoner c decap sequence peel anim onlayer back
                with dissolve
                n "Her head twists slowly to the side, flopping to her shoulder, and her neck... opens.\n"
                voice "audio/voices/ch2/prisoner/_basement/narrator/75.flac"
                play secondary "audio/final/Prisoner_HeavyChains_1.flac"
                queue secondary "audio/final/Prisoner_BodyFall_1.flac"
                play audio "audio/final/_prisoner_bounce.flac"
                show prisoner c decap collapse onlayer back
                with dissolve
                n "The remaining tissue is not enough to hold the weight of her severed head. It stretches and tears, until finally, it falls to the floor, completely free. It bounces a few times before rolling to a stop at your feet.\n"

        voice "audio/voices/ch2/prisoner/_basement/hero/35a.flac"
        hero "Oh no oh no oh no what did we do? Can we put it back? Please tell me we can put it back.\n"
        voice "audio/voices/ch2/prisoner/_basement/narrator/77.flac"
        n "The Princess' eyes stare up at you. Dead. Congratulations. You saved the world.\n"
        voice "audio/_pristine/voice/cage/skeptic/1.flac"
        skeptic "Huh. So I guess that's it. What a way to go. But she is gone, isn't she?\n"
        voice "audio/voices/ch2/prisoner/_basement/hero/36a.flac"
        hero "I hate this. Can we just get out of here now? Please?\n"
        voice "audio/voices/ch2/prisoner/_basement/narrator/79.flac"
        n "Of course. The Princess is slain, and the world is saved. Whenever you're ready you can proceed to your reward.\n"
        voice "audio/_pristine/voice/cage/skeptic/2.flac"
        skeptic "Now hold on. She's dead. So what's the rush? What's your angle?\n"
        voice "audio/_pristine/voice/cage/narrator/1.flac"
        n "I don't have an angle. I'm just looking forward to putting all this behind us, I'm sure you can understand that.\n"
        voice "audio/_pristine/voice/cage/skeptic/3.flac"
        skeptic "Look, I'm just not ready to put my guard down. It's best to keep sharp. She wouldn't have done all that without some kind of reason, she's left us with this dangling thread and I need to know {i}why{/i}.\n"
        voice "audio/_pristine/voice/cage/narrator/2.flac"
        n "You're just wasting your energy. The danger has passed, and now we can all relax and enjoy your reward!\n"
        default prisoner_can_leave = True
        label prisoner_head_choice:
            menu:
                extend ""

                "{i} [[Leave the basement to claim your reward.]{/i}":
                    $ quick_menu = False
                    hide bg onlayer back
                    hide farback onlayer farback
                    hide prisoner onlayer back
                    with fade
                    jump prisoner_dead_late_join

                "{i} [[Take the Princess with you.]{/i}":
                    default princess_head_taken = False
                    $ princess_head_taken = True
                    $ quick_menu = False
                    $ blade_held = True
                    $ default_mouse = "blood"
                    voice "audio/voices/ch2/prisoner/_basement/narrator/83.flac"
                    play audio "audio/one_shot/knife_pickup.flac"
                    play secondary "audio/final/Prisoner_HairHeadStress_1.flac"
                    queue secondary "audio/one_shot/footsteps_stone.flac"
                    show prisoner c decap collapse nohead onlayer back
                    show prisoner head held onlayer front at Position(ypos=1125)
                    with dissolve
                    hide bg onlayer back
                    hide farback onlayer farback
                    hide prisoner onlayer back
                    hide prisoner onlayer front
                    scene bg black
                    with fade
                    n "Ugh. Fine. You pick up the Princess' severed head, its neck stump still oozing bodily fluids, then make your way back upstairs to the first floor of the cabin.\n"
                    jump prisoner_free_join

label prisoner_free_join:
    $ quick_menu = False
    play audio "audio/one_shot/door_bedroom.flac"
    scene farback prisoner leave upstairs onlayer farback at Position(ypos=1125)
    show bg prisoner upstairs exit onlayer back at Position(ypos=1125)
    show prisoner head held onlayer front at Position(ypos=1125)
    with fade
    $ renpy.pause(0.125)
    show prisoner head held twitch onlayer front
    if persistent.quick_menu:
        $ quick_menu = True
    voice "audio/voices/ch2/prisoner/_basement/skeptic/57.flac"
    skeptic "Did you see that? I could have sworn she moved.\n"
    voice "audio/voices/ch2/prisoner/_basement/narrator/84.flac"
    n "She didn't. She's dead.\n"
    voice "audio/voices/ch2/prisoner/_basement/hero/38.flac"
    hero "But what if she's not?!\n"
    voice "audio/voices/ch2/prisoner/_basement/narrator/85.flac"
    show prisoner head held onlayer front
    n "Are you listening to yourself? Do I need to explain to you why decapitation is lethal? The door to your bountiful reward is right in front of you - all you have to do is open it.\n"
    menu:
        extend ""

        "{i} [[Leave the cabin and claim your reward.]{/i}":
            $ quick_menu = False
            play audio "audio/one_shot/door_bedroom.flac"
            voice "audio/voices/ch2/prisoner/_basement/narrator/86.flac"
            hide farback onlayer farback
            hide bg onlayer back
            hide prisoner onlayer front
            scene bg black
            with fade
            n "You open the cabin door, ready to return to a world saved from certain doom.\n"
            voice "audio/voices/ch2/prisoner/_basement/narrator/87.flac"
            show farback damsel outside onlayer farback at Position(ypos=1125)
            show bg damsel outside onlayer back at Position(ypos=1125)
            show mid damsel outside onlayer back at Position(ypos=1125)
            show fore damsel outside onlayer front at Position(ypos=1125)
            show prisoner head held onlayer inyourface at Position(ypos=1125)
            with dissolve
            if persistent.quick_menu:
                $ quick_menu = True
            n "Only, a world saved from certain doom isn't what you find. Instead, what you find is- wait, no, that's not right.\n"
            $ achievement.grant("ACH_PRISONER_FREE")
            play music "audio/_music/ch2/prisoner/The Prisoner Time Erodes Loop.flac" loop
            voice "audio/voices/ch2/prisoner/_basement/princess/58.flac"
            show prisoner head held talk onlayer inyourface
            with dissolve
            sp "Well played.\n"
            stop music fadeout 15.0
            stop sound fadeout 20.0
            stop tertiary fadeout 20.0
            play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 15.0
            voice "audio/voices/ch2/prisoner/_basement/narrator/88b.flac"
            show prisoner head held neutral onlayer inyourface
            show quiet creep1 onlayer front at Position(ypos=1125)
            with Dissolve(1.0)
            n "This is - this - this is the end of the world, isn't it? I always thought I'd at least have time to explain myself before I had to watch it happen, but it's already-\n"
            voice "audio/voices/ch2/prisoner/_basement/hero/40.flac"
            show quiet creep2 onlayer front at Position(ypos=1125)
            with Dissolve(0.5)
            hero "... Over? Is he gone?\n"
            voice "audio/voices/ch2/prisoner/_basement/skeptic/60.flac"
            show quiet creep3 onlayer front at Position(ypos=1125)
            with Dissolve(0.5)
            skeptic "But we're still here. Maybe it wasn't the end of the world after all. Maybe it was just the end of His.\n"
            voice "audio/voices/ch2/prisoner/_basement/princess/59.flac"
            show prisoner head held look hopeful onlayer inyourface
            with dissolve
            sp "Thanks for carrying me up here. I had to take it on faith that you would know what to do. I'm glad I was right to trust you.\n"
            $ gallery_prisoner.unlock_item(8)
            $ renpy.save_persistent()
            voice "audio/voices/ch2/prisoner/_basement/princess/60.flac"
            show prisoner head held hesitant onlayer inyourface
            with dissolve
            sp "So this is the outside. Maybe it's just my lack of body, but... it's colder than I expected.\n"
            play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
            show prisoner head held quiet onlayer inyourface at Position(ypos=1125)
            with Dissolve(1.0)
            $ renpy.pause(0.125)
            show prisoner head held quiet arms3 onlayer inyourface
            with Dissolve(1.0)
            $ renpy.pause(0.125)
            hide prisoner onlayer inyourface
            with Dissolve(1.0)
            $ renpy.pause(0.125)
            $ blade_held = False
            $ default_mouse = "default"
            hide fore onlayer front
            hide fore onlayer inyourface
            hide farback onlayer farback
            hide bg onlayer back
            hide mid onlayer back
            hide stars onlayer farback
            hide bg onlayer back
            hide quiet onlayer back
            hide quiet onlayer front
            show farback quiet onlayer farback at Position(ypos=1125)
            with Dissolve(4.0)
            show mirror quiet distant onlayer back at Position(ypos=1125)
            if loops_finished != 0:
                truth "But you do not get the chance to respond, nor will you ever. It's time to leave. Memory returns.\n"
            else:
                truth "But you don't get the chance to respond. Something has taken her away, and it's left something else in her place.\n"
            $ princess_free += 1
            $ princess_satisfy += 1
            $ current_princess = "prisonerhead"
            $ prisoner_end = "free"
            jump mirror_start


label prisoner_strangle_join:
    stop music
    hide speedlines onlayer front
    hide bg onlayer back
    hide farback onlayer farback
    hide prisoner onlayer back
    scene bg black
    with fade
    $ gallery_prisoner.unlock_item(9)
    $ gallery_prisoner.unlock_item(10)
    $ renpy.save_persistent()
    if prisoner_attack:
        voice "audio/voices/ch2/prisoner/_basement/princess/61.flac"
        spmid "I am not a damsel to be helplessly murdered!\n"
        voice "audio/voices/ch2/prisoner/_basement/narrator/89a.flac"
        play music "audio/_music/ch2/prisoner/The Prisoner Heightened INTRO.flac"
        queue music "audio/_music/ch2/prisoner/The Prisoner Heightened LOOP.flac" loop
        play audio "audio/final/Prisoner_HeavyChains_2.flac"
        scene bg prisoner very close onlayer back at Position(ypos=1125)
        show prisoner v chains wrap onlayer back at Position(ypos=1125)
        with Dissolve(1.0)
        n "As you move to strike at the Princess, she stands, her chains clinking as she wraps them around her fists.\n"
        voice "audio/voices/ch2/prisoner/_basement/narrator/90.flac"
        play tertiary "audio/final/Beast_ChainsFastDrag_2.flac"
        play audio "audio/final/Prisoner_BodyFall_1.flac"
        play secondary "audio/one_shot/hard tighten.flac"
        hide bg onlayer back
        hide prisoner onlayer back
        show prisoner v chains attack onlayer back at Position(ypos=1125)
        with dissolve
        n "In an instant they're around your neck, both of you dropping to the ground as she pulls them taut, bracing her body against yours as you struggle uselessly.\n"
        voice "audio/voices/ch2/prisoner/_basement/princess/62.flac"
        show prisoner v chains attack talk onlayer back
        with dissolve
        play audio "audio/final/Witch_TreeWrap_1.flac"
        sp "Drop it or you die!\n"

        if prisoner_narrator_agree:
            voice "audio/voices/ch2/prisoner/_basement/hero/41.flac"
            show prisoner v chains attack onlayer back
            with dissolve
            hero "I thought this was going to be a safe move, but she's going to kill us again! Just listen to her! Do what she says!\n"
        else:
            voice "audio/voices/ch2/prisoner/_basement/hero/42.flac"
            show prisoner v chains attack onlayer back
            with dissolve
            hero "I thought this was going to be a safe move, but she's going to kill us! Just listen to her! Do what she says!\n"
    elif prisoner_sit_closer:
        voice "audio/voices/ch2/prisoner/_basement/princess/63.flac"
        spmid "Do you think this is a game? Do you think these chains take away my say in things?!\n"
    else:
        voice "audio/voices/ch2/prisoner/_basement/princess/64.flac"
        spmid "Do you think these chains take away my say in things?! I said no!\n"
    if prisoner_attack == False:
        voice "audio/voices/ch2/prisoner/_basement/narrator/91a.flac"
        play audio "audio/final/Prisoner_HeavyChains_2.flac"
        scene bg prisoner very close onlayer back at Position(ypos=1125)
        show prisoner v chains wrap onlayer back at Position(ypos=1125)
        with Dissolve(1.0)
        play music "audio/_music/ch2/prisoner/The Prisoner Heightened INTRO.flac"
        queue music "audio/_music/ch2/prisoner/The Prisoner Heightened LOOP.flac" loop
        n "As you move towards the Princess, she stands, her chains clinking as she wraps them around her fists.\n"
        voice "audio/voices/ch2/prisoner/_basement/narrator/90.flac"
        play tertiary "audio/final/Beast_ChainsFastDrag_2.flac"
        play audio "audio/final/Prisoner_BodyFall_1.flac"
        play secondary "audio/one_shot/hard tighten.flac"
        hide bg onlayer back
        hide prisoner onlayer back
        show prisoner v chains attack onlayer back at Position(ypos=1125)
        with dissolve
        n "In an instant they're around your neck, both of you dropping to the ground as she pulls them taut, bracing her body against yours as you struggle uselessly.\n"
        voice "audio/voices/ch2/prisoner/_basement/narrator/92.flac"
        n "The metal chains constrict around your windpipe as the Princess heaves with a muscled intensity.\n"
        voice "audio/voices/ch2/prisoner/_basement/princess/65.flac"
        play audio "audio/final/Witch_TreeWrap_1.flac"
        show prisoner v chains attack talk onlayer back
        with dissolve
        sp "Drop the knife or you die!\n"
        voice "audio/voices/ch2/prisoner/_basement/hero/43a.flac"
        show prisoner v chains attack onlayer back
        with dissolve
        hero "What is she doing?! We weren't trying to attack her!\n"
        if prisoner_narrator_agree:
            voice "audio/voices/ch2/prisoner/_basement/skeptic/61.flac"
            skeptic "I can see where she might have gotten the wrong idea. She doesn't have much agency here. Would we have trusted her if she walked up to us with a blade again, after what happened between us?\n"
        else:
            voice "audio/voices/ch2/prisoner/_basement/skeptic/62.flac"
            skeptic "I can see where she might have gotten the wrong idea. She doesn't have much agency here. Would we have trusted her if the roles were reversed?\n"
            voice "audio/voices/ch2/prisoner/_basement/hero/44.flac"
            hero "I don't know! How about we think about the nuances of interpersonal relationships when we're not being strangled?!\n"
    voice "audio/voices/ch2/prisoner/_basement/narrator/93.flac"
    n "How many times did I warn you - she's not to be trusted! But while strangulation can be very distracting, she's not armed, and you have your pristine blade. End her. Before she ends you.\n"
    label prisoner_fight_menu:
        menu:
            extend ""

            "{i} [[Slay the Princess.]{/i}" if prisoner_can_slay_attempt:
                default prisoner_slain_by_player = False
                if grey_encountered:
                    $ prisoner_can_slay_attempt = False
                    voice "audio/voices/mound/bonus/path.flac"
                    mound "This path is already worn by travel and has been seen by one of my many eyes. You cannot walk it again. Change your course.\n"
                    voice "audio/voices/ch2/beast/_encounter/hero/31.flac"
                    hero "Wait... what?!\n"
                    jump prisoner_fight_menu
                $ prisoner_slain_by_player = True
                voice "audio/voices/ch2/prisoner/_basement/narrator/94.flac"
                play audio "audio/one_shot/chain_break.flac"
                hide prisoner onlayer back
                scene bg black
                n "You steel your will and refuse to give in to the Princess' demands, ignoring the stars dancing in your eyes and the screaming of your starved lungs. You strike.\n"
                $ default_mouse = "blood"
                play secondary "audio/final/Razor_SwordDrag_1.flac"
                queue secondary "audio/one_shot/knife_slash.flac"
                show prisoner v chains attack slay struggle onlayer back
                show player arm prisoner fight onlayer front at Position(ypos=1125)
                with dissolve
                voice "audio/voices/ch2/prisoner/_basement/narrator/95.flac"
                n "You fumble your first few attempts, only making surface-level scratches and gouges as your arm flails forward, barely able to obey you.\n"
                voice "audio/voices/ch2/prisoner/_basement/narrator/96.flac"
                play audio "audio/one_shot/blood_spray.flac"
                hide player onlayer front
                show prisoner v chain attack slay stab onlayer back
                n "But a single focused blow was all it took. Your blade pierces up through her ribs, slicing through flesh, striking her heart.\n"
                $ gallery_prisoner.unlock_item(11)
                $ renpy.save_persistent()
                $ quick_menu = False
                voice "audio/voices/ch2/prisoner/_basement/narrator/97.flac"
                play secondary "audio/final/Prisoner_HeavyChains_1.flac"
                hide prisoner onlayer back
                scene bg black with fade
                scene prisoner dying sequence onlayer back at Position(ypos=1125)
                with fade
                n "The chains loosen. The darkness creeping in at the edges of your vision subsides.\n"

            "{i} [[Drop it.]{/i}":
                $ blade_held = False
                $ default_mouse = "default"
                play secondary "audio/final/Adversary_BPlayerAggressivelyThrown_3.flac"
                queue secondary "audio/one_shot/knife_bounce_several.flac"
                voice "audio/voices/ch2/prisoner/_basement/narrator/98.flac"
                hide prisoner onlayer back
                scene bg black with fade
                scene bg prisoner basement close onlayer back at swayblur, Position(ypos=1125)
                show prisoner v chains attack surrender onlayer back at swayblur, Position(ypos=1125)
                with fade
                n "As your weapon falls pathetically to the floor, the Princess releases you from her stranglehold, shoving you away with a swift kick.\n"
                voice "audio/voices/ch2/prisoner/_basement/narrator/99.flac"
                play audio "audio/one_shot/knife_pickup.flac"
                show prisoner v chains attack surrender 2 onlayer back
                with dissolve
                n "Your hands test the bruised flesh of your neck as you regain your senses, watching with a dazed expression as the Princess snatches up the blade.\n"
                if prisoner_attack:
                    voice "audio/voices/ch2/prisoner/_basement/princess/66.flac"
                    hide bg onlayer back
                    hide prisoner onlayer back
                    scene bg prisoner basement close onlayer back at Position(ypos=1125)
                    show prisoner v chains attack surrender 3 onlayer back at Position(ypos=1125)
                    with Dissolve(0.5)
                    sp "I'm going to pretend for both our sakes that this was a round of make believe. A trick to get me what I needed to get us out of here.\n"
                    voice "audio/voices/ch2/prisoner/_basement/narrator/100.flac"
                    n "That wasn't a trick. I'd have known if it were a trick. You just didn't have the guts to see things through and save the world.\n"
                    voice "audio/voices/ch2/prisoner/_basement/skeptic/63.flac"
                    skeptic "Or maybe we outwitted you. Who's to say.\n"
                    voice "audio/voices/ch2/prisoner/_basement/princess/67.flac"
                    sp "But I wouldn't try anything else if I were you. Don't push your luck.\n"
                else:
                    voice "audio/voices/ch2/prisoner/_basement/princess/68.flac"
                    hide bg onlayer back
                    hide prisoner onlayer back
                    scene bg prisoner basement close onlayer back at Position(ypos=1125)
                    show prisoner v chains attack surrender 3 onlayer back at Position(ypos=1125)
                    with Dissolve(0.5)
                    sp "That wasn't so hard, was it?\n"

                stop music
                voice "audio/voices/ch2/prisoner/_basement/narrator/64.flac"
                play audio "audio/final/Prisoner_HairHeadStress_3.flac"
                show prisoner c knife neck onlayer back
                with dissolve
                n "She pulls up her hair, smiling slightly as she raises the blade to her throat.\n"
                voice "audio/voices/ch2/prisoner/_basement/princess/69.flac"
                show prisoner c knife neck talk onlayer back
                with dissolve
                sp "You can stay right where you are for this next part.\n"
                jump prisoner_knife_given_late_join

    stop music
    voice "audio/voices/ch2/prisoner/_basement/princess/71.flac"
    show prisoner dying sequence talk onlayer back
    with dissolve
    sp "None of this was ever very fair, was it? But I did kill you last time. I should have expected you might want some petty revenge.\n"
    voice "audio/voices/ch2/prisoner/_basement/princess/72.flac"
    sp "Unfortunately for you, that means you've dug your own grave. You can forget about me ever helping you again. Even if it damns us both.\n"
    $ achievement.grant("ACH_PRISONER_SLAY")
    voice "audio/voices/ch2/prisoner/_basement/narrator/101.flac"
    play sound "audio/looping/uncomfortable ambiance heightened.ogg" loop fadein 5.0
    stop secondary fadeout 5.0
    stop tertiary fadeout 5.0
    show prisoner dying sequence dead yesknife onlayer back
    with dissolve
    n "And just like that, the Princess is slain, and the world is saved. Whenever you're ready, you can proceed to your reward.\n"
    voice "audio/voices/ch2/prisoner/_basement/skeptic/64.flac"
    skeptic "I don't like this. It was too easy.\n"
    voice "audio/voices/ch2/prisoner/_basement/hero/45a.flac"
    hero "It was not 'too easy!' We almost died!\n"
    voice "audio/voices/ch2/prisoner/_basement/narrator/102.flac"
    n "That's right. This was an incredibly difficult task, and you performed it admirably.\n"
    voice "audio/voices/ch2/prisoner/_basement/hero/46a.flac"
    hero "Let's just get out of here. I don't like looking at her body... plus He said there'd be a reward. I'd appreciate a reward right about now.\n"
    voice "audio/voices/ch2/prisoner/_basement/skeptic/65.flac"
    skeptic "You have the attention span of a fly. How are we supposed to unravel the mysteries of this place if you're so easily distracted by empty promises?\n"
    voice "audio/voices/ch2/prisoner/_basement/narrator/103.flac"
    n "It's better to have a short attention span in a situation like this. There's no use dwelling on the past, especially when it's already set in stone.\n"
    voice "audio/voices/ch2/prisoner/_basement/narrator/104.flac"
    n "And especially when your promised reward is not, in fact, empty, and is worth all the adversity you've been through to get here.\n"
    label prisoner_dead_late_join:
        voice "audio/voices/ch2/prisoner/_basement/skeptic/66.flac"
        skeptic "... Fine. But if we're leaving, then we're taking the blade. I feel exposed without it.\n"
        $ blade_held = True
        $ quick_menu = False
        $ default_mouse = "blood"
        play secondary "audio/one_shot/knife_pickup.flac"
        queue secondary "audio/one_shot/footsteps_stone.flac"
        queue secondary "audio/one_shot/door_bedroom.flac"
        voice "audio/voices/ch2/prisoner/_basement/narrator/105.flac"
        hide prisoner onlayer back
        scene bg black
        with fade
        scene farback quiet onlayer farback at Position(ypos=1125)
        show bg prisoner upstairs exit onlayer back at Position(ypos=1125)
        with fade

        if persistent.quick_menu:
            $ quick_menu = True
        n "With your work done, you remove the blade from the Princess' corpse and make your way back upstairs, closing the door to the basement behind you. You can think of it as sealing yourself off from an unpleasant chapter of your life. It's all uphill from here!\n"
        voice "audio/voices/ch2/prisoner/_basement/skeptic/67.flac"
        skeptic "The windows. Do you see that? We used to be able to see the outside world from up here, but now it's just... empty.\n"
        voice "audio/voices/ch2/prisoner/_basement/skeptic/68.flac"
        skeptic "The door! Check the door!\n"
        menu:
            extend ""

            "{i} [[Open the door and accept your reward.]{/i}":
                $ quick_menu = False
                voice "audio/voices/ch2/prisoner/_basement/narrator/106.flac"
                play audio "audio/one_shot/door_bedroom.flac"
                hide farback quiet onlayer farback
                hide bg onlayer back
                with fade
                scene farback quiet onlayer farback at Position(ypos=1125)
                with fade
                if persistent.quick_menu:
                    $ quick_menu = True
                n "You open the cabin door, ready to return to a world saved from certain doom.\n"
                voice "audio/voices/ch2/prisoner/_basement/narrator/107.flac"
                n "Only, a world saved from certain doom isn't what you find. Instead, what you find is nothing at all. Where a lush forest stood mere minutes ago, the only thing in front of you now is the vast emptiness of some place far away.\n"
                voice "audio/voices/ch2/prisoner/_basement/skeptic/69.flac"
                skeptic "You don't have to act surprised. We could see this 'vast emptiness' through the windows.\n"
                voice "audio/voices/ch2/prisoner/_basement/hero/47a.flac"
                hero "But if everything's gone... Does that mean we're not gonna get our reward?\n"

        voice "audio/voices/ch2/prisoner/_basement/narrator/108.flac"
        n "This {i}is{/i} your reward. An eternity of bliss, if you'll have it. And I suggest that you have it.\n"
        voice "audio/voices/ch2/prisoner/_basement/hero/48.flac"
        hero "O...kay.\n"
        $ quick_menu = False
        voice "audio/voices/ch2/prisoner/_basement/narrator/109.flac"
        play audio "audio/one_shot/door_close.flac"
        hide farback onlayer farback
        scene farback quiet onlayer farback at Position(ypos=1125)
        show bg prisoner cabin onlayer back at Position(ypos=1125)
        show door prisoner1 onlayer back at Position(ypos=1125)
        show table prisoner onlayer back at Position(ypos=1125)
        with fade
        if persistent.quick_menu:
            $ quick_menu = True
        n "This is what's best for everyone. Trust me.\n"
        voice "audio/voices/ch2/prisoner/_basement/skeptic/70.flac"
        skeptic "Like hell it is!\n"

        menu:
            extend ""

            "{i} That's bullshit! Let us out of here!{/i}":
                voice "audio/voices/ch1/knife/narrator/knife_n_79.flac"
                n "What's done is done, and there's no going back now.\n"

            "{i} I don't know. I'm pretty okay with this.{/i}":
                voice "audio/voices/ch1/knife/narrator/knife_n_80.flac"
                n "I'm so glad you're keeping an open mind.\n"

            "{i} I was kind of hoping we'd get a better ending for saving the world.{/i}":
                voice "audio/voices/ch2/prisoner/_basement/narrator/110.flac"
                n "This isn't an ending. In fact, now that the Princess has been slain, endings are a thing of the past. No... this is the beginning of {i}eternity{/i}. Your reward. Like I just told you.\n"

        voice "audio/voices/ch1/knife/narrator/knife_n_83.flac"
        n "Time passes. You can't be sure if it's days, or months, or years, or even decades. It's all a wonderful, boring blur. You've never been happier.\n"
        voice "audio/voices/ch2/prisoner/_basement/skeptic/71.flac"
        skeptic "Decades?! No. It can't be decades. We can't go along with this. We can't let Him win.\n" id prisoner_dead_late_join_d6717a84
        label prisoner_happy_menu:
            default prisoner_happy_menu_happy_explore = False
            default prisoner_happy_menu_suggestion_explore = False
            default prisoner_happy_menu_explore = False
            menu:
                extend ""

                "{i} (Explore) Didn't you hear The Narrator? I'm happy. We're happy.{/i}" if prisoner_happy_menu_happy_explore == False:
                    $ prisoner_happy_menu_happy_explore = True
                    voice "audio/voices/ch2/prisoner/_basement/skeptic/72.flac"
                    skeptic "But we're not happy. He's just telling us that we are! I can tell you for a fact that I'm extremely unhappy right now.\n"
                    voice "audio/voices/ch2/prisoner/_basement/hero/49.flac"
                    hero "Yeah, what he said!\n"
                    jump prisoner_happy_menu

                "{i} (Explore) What do you suggest, then?{/i}" if prisoner_happy_menu_suggestion_explore == False:
                    $ prisoner_happy_menu_suggestion_explore = True
                    voice "audio/voices/ch2/prisoner/_basement/skeptic/73.flac"
                    skeptic "We still have a blade. Let's use it on ourselves and start over.\n"
                    voice "audio/voices/ch2/prisoner/_basement/narrator/111.flac"
                    n "He's suggesting you kill yourself. You shouldn't kill yourself when you have an eternity of bliss right in front of you.\n"
                    jump prisoner_happy_menu

                "{i} I don't want to die again. I didn't like dying last time. I'm going to accept my reward now.{/i}" if prisoner_happy_menu_explore == False:
                    jump prisoner_happy_join

                "{i} I dunno, I'm pretty happy. I'm going to accept my reward now.{/i}" if prisoner_happy_menu_explore == False:
                    jump prisoner_happy_join

                "{i} Well, you might not be happy, but I am. I'm going to accept my reward now.{/i}" if prisoner_happy_menu_explore:
                    label prisoner_happy_join:
                        default prisoner_happy_seen = False
                        $ prisoner_happy_seen = True
                        voice "audio/voices/ch2/prisoner/_basement/narrator/112.flac"
                        n "That's great! Congratulations. You've earned it.\n"
                        voice "audio/voices/ch1/knife/narrator/knife_n_84.flac"
                        n "More happy time passes, though the word begins to lose its meaning. 'Time,' that is, not 'happy.' 'Happy' still has plenty of meaning.\n"
                        voice "audio/voices/ch2/prisoner/_basement/skeptic/74.flac"
                        skeptic "He's just saying things.\n"
                        voice "audio/voices/ch2/prisoner/_basement/narrator/113.flac"
                        n "The voice's protestations fall on deaf ears.\n"
                        voice "audio/voices/ch1/knife/narrator/knife_n_86.flac"
                        n "Eventually, you pass into a blissful state of pure existence. Though words like 'eventually' and 'pass' ceased to have any meaning to you long before that shift. You simply exist. Happy. Forever.\n"
                        play sound "audio/looping/party.ogg" loop
                        hide farback onlayer farback
                        hide bg onlayer back
                        hide table onlayer back
                        hide door onlayer back
                        show end good onlayer back at Position(ypos=1125)
                        if _preferences.language is not None:
                            show text _("{color=000000}Good Ending! =:) YOU DID IT!!! you saved EVERYONE!{/color}") onlayer front at Position(ypos=950)
                        with fade
                        $ renpy.pause(4.0)
                        hide text onlayer front
                        play audio "audio/final/Nightmare_MaleBreath_1.flac"
                        voice "audio/voices/ch2/prisoner/_basement/skeptic/75.flac"
                        skeptic "No. You stop that! Stop all this nonsense.\n{w=3.45}{nw}"
                        show screen disableclick(0.5)
                        stop sound
                        voice "audio/voices/ch2/prisoner/_basement/narrator/114.flac"
                        hide end onlayer back
                        show farback quiet onlayer back at Position(ypos=1125)
                        show bg prisoner cabin onlayer back at Position(ypos=1125)
                        show door prisoner1 onlayer back at Position(ypos=1125)
                        show table prisoner onlayer back at Position(ypos=1125)
                        play sound "audio/looping/uncomfortable ambiance heightened.ogg" loop
                        $ achievement.grant("ACH_PRISONER_RESTLESS")
                        n "You really don't want to be happy, do you?\n"
                        if prisoner_happy_menu_suggestion_explore == False:
                            voice "audio/voices/ch2/prisoner/_basement/skeptic/76.flac"
                            skeptic "We still have a blade. Let's use it on ourselves and start over.\n"
                            voice "audio/voices/ch2/prisoner/_basement/narrator/111.flac"
                            n "He's suggesting you kill yourself. You shouldn't kill yourself when you have an eternity of bliss right in front of you.\n"
                        else:
                            voice "audio/voices/ch2/prisoner/_basement/skeptic/77.flac"
                            skeptic "You know what you have to do.\n"
                        label prisoner_post_happy_menu:
                            default prisoner_post_happy_no_other_way = False
                            default prisoner_post_happy_sad = False
                            default prisoner_heart_stop = False
                            default prisoner_give_skeptic_blade = False
                            menu:
                                extend ""

                                "{i} (Explore) Is there really no other way? Because I don't want to use the blade on myself.{/i}" if prisoner_post_happy_no_other_way == False:
                                    $ prisoner_post_happy_no_other_way = True
                                    voice "audio/voices/ch2/prisoner/_basement/skeptic/78.flac"
                                    skeptic "If it makes it easier for you, I can do it. Let me have it.\n"
                                    jump prisoner_post_happy_menu

                                "{i} (Explore) But I liked being happy! Are you really going to take it away from me?{/i}" if prisoner_post_happy_sad == False:
                                    $ prisoner_post_happy_sad = True
                                    voice "audio/voices/ch2/prisoner/_basement/skeptic/79.flac"
                                    skeptic "That wasn't real happiness. The truth is still out there for us to find, but we can't find it here.\n"
                                    jump prisoner_post_happy_menu

                                "{i} [[Give the blade to the Voice of the Skeptic.]{/i}" if prisoner_post_happy_no_other_way:
                                    $ prisoner_give_skeptic_blade = True
                                    voice "audio/voices/ch2/prisoner/_basement/skeptic/80.flac"
                                    skeptic "All right. I'll make this quick.\n"
                                    jump prisoner_slay_self_join

                                "{i} [[Slay yourself.]{/i}":
                                    jump prisoner_slay_self_join

                                "{i} Sorry, but we're not doing that.{/i}":
                                    $ prisoner_heart_stop = True
                                    voice "audio/voices/ch2/prisoner/_basement/skeptic/81.flac"
                                    skeptic "Don't apologize. I'm sorry.\n"
                                    voice "audio/voices/ch2/prisoner/_basement/hero/50.flac"
                                    hero "Wait, why are you sorry?\n"
                                    voice "audio/voices/ch2/prisoner/_basement/narrator/115.flac"
                                    play audio "audio/one_shot/hard tighten.flac"
                                    hide farback onlayer back
                                    hide farback onlayer farback
                                    hide bg onlayer back
                                    hide table onlayer back
                                    hide door onlayer back
                                    scene bg black
                                    n "Your body lurches as your heart suddenly stops beating.\n"
                                    voice "audio/voices/ch2/prisoner/_basement/hero/51.flac"
                                    hero "Are you killing us?!\n"
                                    voice "audio/voices/ch2/prisoner/_basement/skeptic/82.flac"
                                    skeptic "You'll forgive me eventually.\n"
                                    jump prisoner_slay_self_join



                "{i} [[Slay yourself.]{/i}" if prisoner_happy_menu_suggestion_explore:
                    label prisoner_slay_self_join:
                        voice "audio/voices/ch2/prisoner/_basement/narrator/116.flac"
                        n "You goddamned spiteful bastard. Are you really going to turn down immortality itself just to make me lose?\n"
                        voice "audio/voices/ch2/prisoner/_basement/skeptic/83.flac"
                        skeptic "Why should it matter if we die at this point? Haven't you already gotten what you want?\n"
                        voice "audio/voices/ch2/prisoner/_basement/narrator/117.flac"
                        n "I... I don't have to answer that!\n"
                        voice "audio/voices/ch2/prisoner/_basement/skeptic/84.flac"
                        skeptic "That's all we needed to hear.\n"
                        if prisoner_give_skeptic_blade:
                            play audio "audio/one_shot/new/throat_slit.flac"
                            voice "audio/voices/ch2/prisoner/_basement/narrator/118.flac"
                            show player throat slit anim onlayer inyourface at Position(ypos=1125)
                            with dissolve
                            $ renpy.pause(0.125)
                            voice sustain
                            hide farback onlayer back
                            hide player onlayer inyourface
                            hide farback onlayer farback
                            hide bg onlayer back
                            hide table onlayer back
                            hide door onlayer back
                            scene bg black
                            n "Gah! Fine! The little voice raises the pristine blade to your throat and cuts it open. You rapidly bleed out, and then you die. You're a genocidal maniac, you know that, right?\n"
                        elif prisoner_heart_stop:
                            voice "audio/voices/ch2/prisoner/_basement/narrator/119.flac"
                            n "It turns that it doesn't take long to die after your heart stops beating.\n"
                            voice "audio/voices/ch2/prisoner/_basement/narrator/120.flac"
                            play audio "audio/one_shot/collapse.flac"
                            n "You collapse to the floor, everything goes dark, and you die. You're a genocidal maniac, you know that, right?\n"
                        else:
                            voice "audio/voices/ch2/prisoner/_basement/narrator/121.flac"
                            show player self end onlayer front at Position(ypos=1125)
                            with dissolve
                            $ renpy.pause(0.125)
                            voice sustain
                            play audio "audio/one_shot/knife_stab.flac"
                            hide player onlayer inyourface
                            hide farback onlayer back
                            hide player onlayer front
                            hide farback onlayer farback
                            hide bg onlayer back
                            hide table onlayer back
                            hide door onlayer back
                            scene bg black
                            n "You raise the blade, then drive it into your heart.\n"
                            voice "audio/voices/ch2/prisoner/_basement/narrator/120.flac"
                            play audio "audio/one_shot/collapse.flac"
                            n "You collapse to the floor. Everything goes dark, and you die. You're a genocidal maniac, you know that, right?\n"
                        voice "audio/voices/ch2/prisoner/_basement/skeptic/85.flac"
                        skeptic "Yeah. We'll see about that.\n"
                        if prisoner_slain_by_player:
                            jump grey_start
                        else:
                            jump cage_start


return
