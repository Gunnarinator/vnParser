label spectre_1_start:
    $ blade_held = False
    $ trait_cold = True
    $ quick_menu = False
    play sound "audio/looping/uncomfortable ambiance.ogg" loop fadein 1.0
    scene chapter spectre with fade
    show text _("{color=#FFFFFF00}Chapter 2. The Spectre.{/color}") at Position(ypos=850)
    $ renpy.pause(4.0)

    # staging for conversation variables
    default spectre_how_hurt_explore = False
    default spectre_not_dead_explore = False
    default spectre_body_point = False
    default spectre_why_back = False
    default spectre_home_follow = False
    default spectre_victim = False
    default spectre_sorry = False
    default spectre_grovel_1 = False
    default spectre_trick = False
    default spectre_if_only = False
    default spectre_also_dead = False
    default spectre_teleport = False
    default spectre_walls = False

    default spectre_paranoid_override = False

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
    $ gallery_spectre.unlock_gallery()
    $ gallery_zch1.unlock_item(9)
    $ renpy.save_persistent()
    voice "audio/voices/ch1/woods/narrator/script_n_1.flac"
    n "You're on a path in the woods. And at the end of that path is a cabin. And in the basement of that cabin is a Princess.\n"
    voice "audio/voices/ch1/woods/narrator/script_n_2.flac"
    n "You're here to slay her.\n If you don't, it will be the end of the world.\n"
    label spectre_1_forest:
        default spectre_1_forest_count = 0
        default spectre_1_forest_share_died = False
        default spectre_1_forest_share_loop = False
        default spectre_1_forest_princess_press = False
        default spectre_1_forest_share_loop_insist = False
        default spectre_1_forest_deja_vu = False
        default spectre_1_forest_deja_vu_follow_up = False
        menu:
            extend ""

            "{i}• (Explore) Oh, you bastard! You're in for it now. I'm wise to your tricks!{/i}" if spectre_1_forest_share_loop == False:
                $ spectre_1_forest_share_loop = True
                voice "audio/voices/ch2/prisoner/narrator/ch2_pn_7.flac"
                n "My tricks? What on earth are you talking about? We've just met for the first time.\n"
                jump spectre_1_forest_narrator_share_join

            "{i}• (Explore) I'm getting a terrible sense of deja vu.{/i}" if spectre_1_forest_share_loop == False:
                $ spectre_1_forest_deja_vu = True
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_1a.flac"
                n "A terrible sense of deja vu? No, you don't have that. This is the first time either of us have been here.\n"
                label spectre_1_forest_narrator_share_join:
                    $ spectre_1_forest_count += 1
                    $ spectre_1_forest_share_loop = True
                    voice "audio/voices/ch2/shared/hero/ch2_share_h_1.flac"
                    hero "If He doesn't remember what happened, then maybe it's best to keep it that way.\n"
                    voice "audio/voices/ch2/spectre/cold/ch2_cold_1.flac"
                    cold "That's fine. It wasn't very hard to kill her last time. We'll just do it again.\n"
                    voice "audio/voices/ch2/spectre/narrator/ch2_gn_1.flac"
                    n "Well, if for whatever reason you're going to insist that this has happened before, at least your heart's in the right place.\n"
                    jump spectre_1_forest

            "{i}• (Explore) This is more than just deja vu, though. I'm pretty sure this whole thing literally just happened.{/i}" if spectre_1_forest_deja_vu and spectre_1_forest_deja_vu_follow_up == False:
                $ spectre_1_forest_deja_vu_follow_up = True
                $ spectre_1_forest_count += 1
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_1.flac"
                n "It hasn't. Or if it has, I certainly haven't been a part of it. Like I said, we've just met for the first time, you and I.\n"
                jump spectre_1_forest

            "{i}• (Explore) Wait... hasn't this already happened?{/i}" if spectre_1_forest_share_loop == False:
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_1b.flac"
                n "It hasn't. Or if it has, I certainly haven't been a part of it. We've just met for the first time, you and I.\n"
                jump spectre_1_forest_narrator_share_join

            "{i}• (Explore) Okay, no.{/i}" if spectre_1_forest_share_loop == False:
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_3a.flac"
                n "Oh, don't you start grandstanding about morals. The fate of the world is at risk right now, and the life of a mere Princess shouldn't stop you from saving us all.\n"
                jump spectre_1_forest_narrator_share_join

            "{i}• (Explore) But I killed myself! What am I doing here?{/i}" if spectre_1_forest_share_loop == False:
                $ spectre_1_forest_share_died = True
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_4.flac"
                n "I can assure you that you're not dead. And to answer your second question, you're here to slay the Princess. I literally told you that a second ago.\n"
                jump spectre_1_forest_narrator_share_join

            "{i}• (Explore) But I already killed the Princess.{/i}" if current_princess == "ghost" and loop_2_forest_share_loop == False:
                $ loop_2_forest_share_loop = True
                voice "audio/voices/ch2/spectre/narrator/ch2_gn_2.flac"
                n "I can assure you that you didn't.\n"
                jump spectre_1_forest_narrator_share_join

            "{i}• (Explore) You trapped me here after I slew her last time. I'm not going to play along this time.{/i}" if current_princess == "ghost":
                voice "audio/voices/ch2/spectre/narrator/ch2_gn_3.flac"
                n "How unfortunate that the sole person capable of slaying the Princess also seems to be somewhat insane. Oh, well. So long as you get the job done, it doesn't matter what sort of mental state you're in.\n"
                jump spectre_1_forest_narrator_share_join

            "{i}• (Explore) Let's assume I'm telling the truth, and all of this really did already happen. Why should I listen to you? Why should I bother doing {i}anything{/i}?{/i}" if spectre_1_forest_share_loop and (spectre_1_forest_deja_vu == False or (spectre_1_forest_deja_vu_follow_up)) and spectre_1_forest_share_loop_insist == False:
                $ spectre_1_forest_share_loop_insist = True
                $ spectre_1_forest_count += 1
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_6.flac"
                n "Those are two very different questions, but fine. I'll indulge you if that's what it takes to get you moving.\n"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_7.flac"
                n "Let's say for a moment that this really is the second time you've met me, or, at least, a version of me.\n"
                if spectre_1_forest_share_died == False:
                    voice "audio/voices/ch2/shared/narrator/ch2_share_n_8.flac"
                    n "If you're back here, I'm assuming you died, which probably only happened because you didn't listen to me.\n"
                else:
                    voice "audio/voices/ch2/shared/narrator/ch2_share_n_9.flac"
                    n "You died last time, which probably only happened because you didn't listen to me.\n"
                voice "audio/voices/ch2/spectre/cold/ch2_cold_2.flac"
                cold "Oh, we listened to you plenty. We slew the Princess, just like you asked us to. And then you locked us away in an empty void for eternity. So we slew ourselves, too.\n"
                voice "audio/voices/ch2/spectre/narrator/ch2_gn_4.flac"
                n "Well, if you killed yourself then you {i}weren't{/i} listening to me. Because I would never want you to do that. Believe it or not, I care about you.\n"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_11.flac"
                n "And I believe your other question was something along the lines of 'what's the point of doing anything?' If you're asking that, it sounds to me like you're making the rather dangerous assumption that your actions last time around didn't have any consequences.\n"
                voice "audio/voices/ch2/spectre/hero/ch2_gh_1.flac"
                hero "What do you mean? Of course there weren't any consequences. We slew the Princess, the world outside the cabin disappeared, we died, and now everyone's right back where they started. That sounds pretty consequence-free to me.\n"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_12.flac"
                n "Yes, but, in this purely hypothetical scenario, that begs the question of {i}how{/i} you got back here. Did 'time' simply rewind itself, or were you instead transported to a different world entirely?\n"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_12a.flac"
                n "Had you failed to slay the Princess, what would have happened to everyone in the place you left?\n"
                voice "audio/voices/ch2/spectre/cold/ch2_cold_3.flac"
                cold "It doesn't matter, because we didn't fail to slay her, and if she's really back, which I doubt, it'll be just as easy to do it again. But after that nasty trick you pulled on us, maybe she's not the only one around here in need of slaying.\n"
                voice "audio/voices/ch2/spectre/narrator/ch2_gn_5.flac"
                n "Just stay focused, will you?\n"
                jump spectre_1_forest

            "{i}• (Explore) Let's talk about this Princess...{/i}" if spectre_1_forest_share_loop_insist and spectre_1_forest_princess_press == False:
                $ spectre_1_forest_count += 1
                $ spectre_1_forest_princess_press = True
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_14.flac"
                n "Just be quick about it.\n"
                label spectre_1_forest_princess:
                    default spectre_1_forest_princess_count = 0
                    default spectre_1_forest_princess_why_strong = False
                    default spectre_1_forest_princess_basement_explain = False
                    default spectre_1_forest_princess_why_me = False
                    default spectre_1_forest_princess_cagey = False
                    default spectre_1_forest_princess_tips = False
                    default spectre_1_forest_princess_teleport = False
                    menu:
                        extend ""

                        "{i}• (Explore) If anything, the world ended {b}after{/b} I slew her. When I tried to leave, everything was gone.{/i}" if spectre_1_forest_princess_teleport == False:
                            $ spectre_1_forest_princess_teleport = True
                            voice "audio/voices/ch2/spectre/hero/ch2_gh_2.flac"
                            hero "That's a good point. How do we know we didn't have things backwards? Maybe slaying the Princess was what ended the world, not the other way around.\n"
                            voice "audio/voices/ch2/spectre/cold/ch2_cold_4.flac"
                            cold "Yes, maybe this whole thing was a trick to get us to end the world. And now we get to go through the whole charade again wholly aware of what's waiting for us at the end.\n"
                            voice "audio/voices/ch2/spectre/cold/ch2_cold_5.flac"
                            cold "But that's assuming she's alive in that cabin. We did kill her, after all.\n"
                            voice "audio/voices/ch2/spectre/narrator/ch2_gn_6.flac"
                            n "You're going to find her in the cabin. If the Princess had actually been slain, you wouldn't be here.\n"
                            voice "audio/voices/ch2/spectre/narrator/ch2_gn_7.flac"
                            n "And let me assure you, killing her will not end the world. I don't know what you think happened to you 'last time', but it's a load of nonsense. You'll get your happy ending, I promise.\n"
                            voice "audio/voices/ch2/spectre/hero/ch2_gh_3.flac"
                            hero "That's exactly what we're afraid of.\n"
                            voice "audio/voices/ch2/spectre/narrator/ch2_gn_8a.flac"
                            n "Really? Living happily ever after sounds {i}that bad{/i} to you? Oh well, there's no use arguing over your masochism. The cabin awaits.\n"
                            jump spectre_1_forest_princess

                        "{i}• (Explore) Last time around I stabbed her in the heart and she died. How can someone like that end the world?{/i}" if spectre_1_forest_princess_why_strong == False:
                            $ spectre_1_forest_princess_why_strong = True
                            $ spectre_1_forest_princess_count += 1
                            voice "audio/voices/ch2/spectre/narrator/ch2_gn_9a.flac"
                            n "She just can. You'll have to trust that what I'm saying is true.\n"
                            jump spectre_1_forest_princess

                        "{i}• (Explore) Who locked her in that basement? What {b}is{/b} this place?{/i}" if spectre_1_forest_princess_basement_explain == False:
                            $ spectre_1_forest_princess_basement_explain = True
                            $ spectre_1_forest_princess_count += 1
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_18.flac"
                            n "{i}People{/i} locked her in that basement. And I told you what this place is. It's a path in the woods. Don't overcomplicate things.\n"
                            jump spectre_1_forest_princess

                        "{i}• (Explore) If people locked her away, why couldn't {b}they{/b} slay her? Why is this falling on me?{/i}" if spectre_1_forest_princess_basement_explain and spectre_1_forest_princess_why_me == False:
                            $ spectre_1_forest_princess_why_me = True
                            $ spectre_1_forest_princess_count += 1
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_19.flac"
                            n "Look, I'm not supposed to say this, but it's because you're special. You're the {i}only{/i} person capable of doing this. Call it a prophecy if that helps, but it's just the way things are.\n"
                            voice "audio/voices/ch2/shared/hero/ch2_share_h_2.flac"
                            hero "Oh. I didn't know we were {i}special{/i}.\n"
                            voice "audio/voices/ch2/spectre/cold/ch2_cold_6.flac"
                            cold "Of course we're special.\n"
                            jump spectre_1_forest_princess

                        "{i}• (Explore) You're being cagey. What aren't you telling me?{/i}" if spectre_1_forest_princess_cagey == False and spectre_1_forest_princess_count > 1:
                            $ spectre_1_forest_princess_cagey = True
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_21.flac"
                            n "I've told you everything you need to know, going into more detail would just overcomplicate an otherwise very simple situation and make your job more difficult.\n"
                            voice "audio/voices/ch2/spectre/cold/ch2_cold_7.flac"
                            cold "This is boring. He's clearly not interested in talking, so let's just do as He says and maybe He'll stop bothering us.\n"
                            jump spectre_1_forest_princess

                        "{i}• Nevermind.{/i}" if spectre_1_forest_princess_count == 0:
                            label spectre_1_forest_princess_leaving:
                                voice "audio/voices/ch2/shared/narrator/ch2_share_n_24.flac"
                                n "Great. Now if you don't mind, the whole world is waiting with bated breath for you to save it from ruin.\n"
                                jump spectre_1_forest

                        "{i}• That's all.{/i}" if spectre_1_forest_princess_count != 0:
                            jump spectre_1_forest_princess_leaving

            "{i}• [[Proceed to the cabin.]{/i}":
                jump spectre_1_cabin_arrival

            "{i}• [[Turn around and leave.]{/i}" if mound_can_attempt_flee:
                if loops_finished >= 2:
                    $ mound_can_attempt_flee = False
                    voice "audio/voices/mound/bonus/flee.flac"
                    mound "You have already committed to my completion. You cannot go further astray.\n"
                    jump spectre_1_forest
                voice "audio/voices/ch2/spectre/cold/ch2_cold_8.flac"
                cold "Oh? Do you think there's something else out there? All right, let's see what we can find. It's bound to be more interesting than doing the same thing over again.\n"
                jump turn_and_leave_join

label spectre_1_cabin_arrival:
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
    voice "audio/voices/ch2/spectre/cold/ch2_cold_9.flac"
    cold "She won't be a problem.\n"
    menu:
        extend ""

        "{i}• [[Proceed into the cabin.]{/i}":
            label spectre_stranger_rejoin:
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

    $ gallery_spectre.unlock_item(1)
    $ renpy.save_persistent()
    voice "audio/voices/ch2/spectre/narrator/ch2_gn_10.flac"
    play sound "audio/looping/STP_hauntedhouse_loop.ogg" loop fadein 1.0
    play music "audio/_music/ch2/spectre/The Spectre.flac" loop
    scene farback interior cabin onlayer farback at Position(ypos=1125)
    show bg spectre cabin onlayer back at Position(ypos=1125)
    show door spectre1 onlayer back at Position(ypos=1125)
    show table spectre onlayer back at Position(ypos=1125)
    show knife spectre onlayer back at Position(ypos=1125)
    show mirror base onlayer back at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    n "The interior of the cabin is cold, a soft odor of dirt permeating the air. Cobwebs flutter in the corners. You can hear wind whistling outside, banging the shutters against the windows. The only furniture of note is an elegant antique table with a pristine blade perched on the edge.\n"
    voice "audio/voices/ch2/shared/narrator/ch2_share_n_25.flac"
    n "The blade is your implement. You'll need it if you want to do this right.\n"
    voice "audio/voices/ch2/spectre/hero/ch2_gh_4.flac"
    hero "It feels like no one's been here for a long, long time.\n"
    voice "audio/voices/ch2/spectre/cold/ch2_cold_10.flac"
    cold "Like I've been saying. She's dead. We killed her already.\n"
    label cabin_interior_2_spectre_menu:
        default spectre_1_cabin_mirror_present = True
        default spectre_1_cabin_blade_taken = False
        default spectre_1_cabin_mirror_ask = False
        default spectre_1_cabin_mirror_approached = False
        default spectre_1_cabin_last_time_comment = False
        menu:
            extend ""

            "{i}• (Explore) You didn't say anything about the mirror on the wall.{/i}" if spectre_1_cabin_mirror_ask == False and spectre_1_cabin_mirror_present:
                $ spectre_1_cabin_mirror_ask = True
                $ current_run_mirror_comment = True
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_26.flac"
                n "That's because there isn't a mirror. There's a table, the blade sitting on the table, and the door to the basement. There's nothing else in here.\n"
                voice "audio/voices/ch2/shared/hero/ch2_share_h_4.flac"
                hero "There's definitely a mirror.\n"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_27.flac"
                n "There isn't.\n"
                voice "audio/voices/ch2/spectre/cold/ch2_cold_11.flac"
                cold "Who cares if there's a mirror? Let's just go into the basement and find her body so we can be done with this.\n"
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
                        $ spectre_1_cabin_mirror_present = False
                        voice "audio/voices/ch2/shared/hero/ch2_share_h_5.flac"
                        hero "But it {i}does{/i} matter! Don't you care if we're being lied to? If He's willing to lie about something as innocuous as a mirror, what else is He hiding from us?\n"
                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_30.flac"
                        hide mirror onlayer back
                        n "I'm not lying to you. Use your eyes, there is no mirror. Why would I lie about something so meaningless? What good would a mirror even do? Let you waste time preening yourself instead of doing what needs to be done?\n"
                        voice "audio/voices/ch2/shared/hero/ch2_share_h_6.flac"
                        hero "But there {i}was{/i} a mirror a second ago.\n"
                        voice "audio/voices/ch2/spectre/cold/ch2_cold_12.flac"
                        cold "And now it's gone. Let's not spend much longer worrying over it. Clearly it's not even important enough to be acknowledged.\n"

                    "{i}• [[Remain silent.]{/i}":
                        voice "audio/voices/ch2/shared/hero/ch2_share_h_7a.flac"
                        hero "I care about whether we're being lied to. If He's willing to lie about something as innocuous as a mirror, what else could He hiding from us?\n"
                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_31.flac"
                        n "I'm not lying to you, I {i}promise{/i}. There isn't a mirror. Really.\n"

                    "{i}• [[Approach the mirror.]{/i}" if spectre_1_cabin_mirror_approached == False:
                        label spectre_cabin_1_mirror_join:
                            $ spectre_1_cabin_mirror_approached = True
                            play audio "audio/one_shot/footsteps_creaky.flac"
                            hide farback onlayer farback
                            hide bg onlayer back
                            hide door onlayer back
                            hide table onlayer back
                            hide knife onlayer back
                            hide mirror onlayer back
                            scene bg spectre mirror onlayer front at Position(ypos=1125)
                            show mirror spectre close onlayer front at Position(ypos=1125)
                            with dissolve
                            voice "audio/voices/ch2/shared/narrator/ch2_share_n_32.flac"
                            n "You walk up to the wall next to the basement door. It's a wall. There isn't much to see here.\n"
                            if spectre_1_cabin_mirror_ask == False:
                                voice "audio/voices/ch2/shared/hero/ch2_share_h_8.flac"
                                hero "What are you talking about? This isn't a wall. It's a mirror. Or at least it'll {i}be{/i} a mirror once we wipe off that layer of grime.\n"
                            else:
                                voice "audio/voices/ch2/shared/hero/ch2_share_h_9.flac"
                                hero "This really isn't funny.\n"
                            $ current_run_mirror_touched = True
                            menu:
                                extend ""

                                "{i}• [[Wipe the mirror clean.]{/i}":
                                    $ spectre_1_cabin_mirror_present = False
                                    hide mirror onlayer front
                                    play audio "audio/one_shot/new/STP_claws_1.flac"
                                    show player wall onlayer front at Position(ypos=1125) with dissolve
                                    if spectre_1_cabin_mirror_ask == False:
                                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_33.flac"
                                    else:
                                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_33a.flac"
                                    n "You reach forward and rub your hand against the cabin wall. I hope you know how ridiculous you look right now.\n"
                                    hide player onlayer front with dissolve
                                    if spectre_1_cabin_mirror_ask:
                                        voice "audio/voices/ch2/shared/hero/ch2_share_h_10.flac"
                                        hero "But it was there a second ago!\n"
                                    else:
                                        voice "audio/voices/ch2/shared/hero/ch2_share_h_6.flac"
                                        hero "But there was a mirror a second ago.\n"
                                    voice "audio/voices/ch2/spectre/cold/ch2_cold_12.flac"
                                    cold "And now it's gone. Let's not spend much longer worrying over it. Clearly it's not even important enough to be acknowledged.\n"
                                    play audio "audio/one_shot/footsteps_creaky.flac"
                                    hide bg onlayer front
                                    scene farback interior cabin onlayer farback at Position(ypos=1125)
                                    show bg spectre cabin onlayer back at Position(ypos=1125)
                                    show door spectre1 onlayer back at Position(ypos=1125)
                                    show table spectre onlayer back at Position(ypos=1125)
                                    if spectre_1_cabin_blade_taken == False:
                                        show knife spectre onlayer back at Position(ypos=1125)
                                    with dissolve
                                    jump cabin_interior_2_spectre_menu

                jump cabin_interior_2_spectre_menu

            "{i}• (Explore) This whole cabin is different than last time.{/i}" if spectre_1_cabin_last_time_comment == False and spectre_1_forest_share_loop_insist:
                $ spectre_1_cabin_last_time_comment = True
                voice "audio/voices/ch2/shared/hero/ch2_share_h_11.flac"
                hero "{i}Very{/i} different.\n"
                voice "audio/voices/ch2/spectre/narrator/ch2_gn_11.flac"
                n "Maybe that's because you haven't actually been here. I hope this means you'll finally drop that ridiculous second-life proposition. You haven't died, and you certainly haven't already slain the Princess.\n"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_35.flac"
                n "So focus up. A lot's riding on this.\n"
                jump cabin_interior_2_spectre_menu

            "{i}• (Explore) [[Approach the mirror.]{/i}" if spectre_1_cabin_mirror_present and spectre_1_cabin_mirror_approached == False:
                $ spectre_1_cabin_mirror_approached = True
                jump spectre_cabin_1_mirror_join

            "{i}• (Explore) [[Take the blade.]{/i}" if spectre_1_cabin_blade_taken == False:
                $ spectre_1_cabin_blade_taken = True
                $ blade_held = True
                $ default_mouse = "blade"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_36.flac"
                play audio "audio/one_shot/knife_pickup.flac"
                hide knife onlayer back
                with dissolve
                n "You take the blade from the table. It would be difficult to slay the Princess and save the world without a weapon.\n"
                jump cabin_interior_2_spectre_menu

            "{i}• [[Enter the basement.]{/i}":
                # get to da basement.
                $ quick_menu = False
                play audio "audio/one_shot/door_bedroom.flac"
                show door spectre2 onlayer back at Position(ypos=1125)
                with Dissolve(0.5)
                hide mirror onlayer back
                show door spectre3 onlayer back at Position(ypos=1125) with Dissolve(0.5)
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

                voice "audio/voices/ch2/spectre/narrator/ch2_gn_13.flac"
                scene bg spectre stairs onlayer back at Position(ypos=1125)
                with fade
                if persistent.quick_menu:
                    $ quick_menu = True
                n "The door to the basement groans open, revealing an old banister and a creaky, wooden stairwell. Everything is coated in a thick layer of dust, and you can feel it settle into your lungs as you breathe in the stale air. The very building itself feels dead. If the Princess lives here, slaying her would probably be doing her a favor.\n"
                voice "audio/voices/ch2/spectre/narrator/ch2_gn_14.flac"
                n "The room below is silent.\n"
                voice "audio/voices/ch2/spectre/cold/ch2_cold_13.flac"
                cold "Nobody's here. Naturally.\n"
                voice "audio/voices/ch2/spectre/narrator/ch2_gn_15.flac"
                n "As much as I appreciate the optimism, you shouldn't be so sure.\n"
                voice "audio/voices/ch2/spectre/hero/ch2_gh_5.flac"
                hero "I guess we'll just have to go down and see.\n"
                $ gallery_spectre.unlock_item(2)
                $ renpy.save_persistent()
                $ quick_menu = False
                play audio "audio/one_shot/footsteps_creaky.flac"
                hide bg onlayer back
                with fade
                scene farback spectre basement onlayer farback at Position(ypos=1125)
                show bg spectre basement onlayer back at Position(ypos=1125)
                with fade
                if persistent.quick_menu:
                    $ quick_menu = True
                voice "audio/voices/ch2/spectre/narrator/ch2_gn_16.flac"
                n "As you descend the final step, the form of the Princess comes into view. A skeletal body lying in a heap on the floor, its wrist still bound to the wall by a thick chain.\n"
                voice "audio/voices/ch2/spectre/hero/ch2_gh_6.flac"
                hero "Okay. She's definitely dead.\n"
                voice "audio/voices/ch2/spectre/cold/ch2_cold_15.flac"
                cold "It's just like I told you—\n{w=2.2}{nw}"
                show screen disableclick(0.5)
                voice "audio/voices/ch2/spectre/narrator/ch2_gn_17.flac"
                show spectre d head onlayer back with dissolve
                n "Before you have a chance to finish your thought, the top of a head appears from underneath the floor.\n"
                $ gallery_spectre.unlock_item(3)
                $ renpy.save_persistent()
                show spectre d head2 onlayer back with dissolve
                voice "audio/voices/ch2/spectre/narrator/ch2_gn_18.flac"
                n "Two deep-set eyes stare up at you, followed by a mischievous skeletal grin.\n"
                voice "audio/voices/ch2/spectre/narrator/ch2_gn_19.flac"
                show spectre d wave onlayer back
                with Dissolve(1.0)
                n "And finally, the rest of the body floats up to join the head. Wait... this isn't right. What's going on here?\n"
                voice "audio/voices/ch2/spectre/hero/ch2_gh_7.flac"
                show spectre d serious onlayer back with dissolve
                hero "A g-g-g-ghost!\n"
                voice "audio/voices/ch2/spectre/cold/ch2_cold_16.flac"
                cold "Oh. Wow. How absolutely terrifying. What's a ghost supposed to do to us?\n"
                show spectre d talk onlayer back with dissolve
                voice "audio/voices/ch2/spectre/princess/ch2_sp_1.flac"
                p "Oh. It's you. Hiya, killer. I was hoping to see you again. I have some issues with how our last meeting went.\n"
                #show spectre d serious talk onlayer back with dissolve
                #voice "audio/voices/ch2/spectre/princess/ch2_sp_2.flac"
                #sp "Like how you murdered me.\n"

                jump spectre_encounter_start
