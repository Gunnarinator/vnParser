label stranger_1_cabin_start:
    $ gallery_stranger.unlock_item(1)
    $ renpy.save_persistent()
    play sound "audio/looping/ambient_cabin.ogg" loop fadein 1.0
    play music "audio/_music/ch2/stranger/The Stranger Cabin.flac" loop
    #scene farback stranger cabin onlayer farback at Position(ypos=1125)
    show farback stranger cabin onlayer farback at Position(ypos=1125)
    show back2 stranger cabin onlayer back at Position(ypos=1125)
    show fore cabin stranger onlayer front at Position(ypos=1125)
    show door cabin stranger1 onlayer front at Position(ypos=1125)
    show table stranger onlayer front at Position(ypos=1125)
    show knife stranger onlayer front at Position(ypos=1125)
    show mirror base onlayer front at Position(ypos=1125)

    with fade

    voice "audio/voices/ch2/stranger/_encounter/narrator/1a.flac"
    n "The cabin interior is wrong, a confusing patchwork of many cabin interiors all projected across what's {i}almost{/i} the same space. But it's all shifted — an inch here, a foot there — such that the seams are never quite visible enough for the place to make any sense.\n"
    #n "The cabin interior is wrong, a confusing patchwork of many cabin interiors all projected across what's {i}almost{/i} the same space. But it's all shifted — an inch here, a foot there — such that the seams are never visble enough for the place to make any sense.\n"
    voice "audio/voices/ch2/stranger/_encounter/narrator/2.flac"
    n "The only furniture of note is a plain table, its legs all the wrong lengths, its material devoid of feature. Perched on that table is a pristine blade.\n"
    voice "audio/voices/ch2/shared/narrator/ch2_share_n_25.flac"
    n "The blade is your implement. You'll need it if you want to do this right.\n"
    voice "audio/voices/ch2/stranger/contrarian/ch2_contrarian_6.flac"
    contrarian "If He wants us to take it, maybe we should just leave it to collect dust. Or better yet, grab it and throw it out the window! What good is a knife against a world-ending monstrosity anyways?\n"
    voice "audio/voices/ch2/stranger/_encounter/hero/1.flac"
    hero "No, we're taking the knife. H-have you seen this place? We have literally no idea what to expect, and no idea what we're dealing with.\n"
    voice "audio/voices/ch2/stranger/narrator/ch2_sn_13.flac"
    n "I've already told you what you're dealing with. You're dealing with a {i}Princess{/i}. How many times do I have to explain this incredibly simple and straightforward premise?\n"
    voice "audio/voices/ch2/stranger/_encounter/hero/2.flac"
    hero "You can't just say that! Not when everything here is so wrong.\n"
    voice "audio/voices/ch2/stranger/_encounter/narrator/3.flac"
    n "Listen to me. My job is to describe facts as facts, and to guide you through your job, which is to slay the Princess, and through that action, save the entire world.\n"
    voice "audio/voices/ch2/stranger/_encounter/narrator/4.flac"
    n "And if you're going to slay her, you cannot let fear creep into your heart. You cannot lose yourself before you even get to her.\n"
    voice "audio/voices/ch2/stranger/_encounter/contrarian/1.flac"
    contrarian "Ohoho! You've piqued my interest. What's going to happen if we 'lose ourself'?\n"
    voice "audio/voices/ch2/stranger/_encounter/narrator/5.flac"
    n "Nothing. Because you're going to pull yourself together.\n"
    #voice "audio/voices/ch2/stranger/_encounter/contrarian/2.flac"
    #contrarian "We'll see about that!\n"
    voice "audio/voices/ch2/stranger/_encounter/narrator/6.flac"
    n "Just ignore the stressful geometry and stay calm.\n"
    voice "audio/voices/ch2/stranger/_encounter/hero/3.flac"
    hero "How?! Even if we closed our eyes you're constantly describing it to us.\n"
    voice "audio/voices/ch2/stranger/_encounter/narrator/7.flac"
    n "I'm not going to stop doing my job, so you're just going to have to get better at yours. And quickly, if you don't mind.\n"
    voice "audio/voices/ch2/stranger/_encounter/contrarian/3.flac"
    contrarian "Yes, take a deep breath. I'm all for getting under His skin, but we'll miss out on loads of fun if we shrivel up into a ball and go insane the first time we see something weird.\n"
    voice "audio/voices/ch2/stranger/_encounter/contrarian/4.flac"
    contrarian "What you're seeing here is obviously real. Just accept it and go with the flow. It really isn't hard.\n"
    voice "audio/voices/ch2/stranger/_encounter/hero/4.flac"
    hero "Okay. Okay. I'm fine.\n"
    voice "audio/voices/ch2/stranger/_encounter/narrator/8.flac"
    n "Good. Now whenever you're ready, we're all waiting for you to complete a very important task.\n"

label cabin_interior_2_stranger_menu:
    default stranger_1_cabin_mirror_present = True
    default stranger_1_cabin_blade_taken = False
    default stranger_1_cabin_mirror_ask = False
    default stranger_1_cabin_mirror_approached = False
    default stranger_1_cabin_last_time_comment = False
    default stranger_1_cabin_blade_tossed = False
    menu:
        extend ""

        "{i}• (Explore) You didn't say anything about the mirror on the wall.{/i}" if stranger_1_cabin_mirror_ask == False and stranger_1_cabin_mirror_present:
            $ stranger_1_cabin_mirror_ask = True
            $ current_run_mirror_comment = True
            voice "audio/voices/ch2/stranger/contrarian/ch2_contrarian_7.flac"
            contrarian "Ooh! We should look at ourselves. Wouldn't that be fun?\n"
            if stranger_1_cabin_blade_taken == False:
                voice "audio/voices/ch2/stranger/_encounter/narrator/9.flac"
                n "You won't be looking at yourself because there isn't a mirror. There's the table, the blade sitting on the table, and the door to the basement. There's nothing else in here.\n"
                #n "You won't be looking at yourself because there isn't a mirror. There's the object, the blade sitting on the object, and the door to the basement. There's nothing else in here.\n"
            else:
                voice "audio/voices/ch2/stranger/_encounter/narrator/9a.flac"
                n "You won't be looking at yourself because there isn't a mirror. There's the table and the door to the basement. There's nothing else in here.\n"
                #n "You won't be looking at yourself because there isn't a mirror. There's the object and the door to the basement. There's nothing else in here.\n"
            voice "audio/voices/ch2/shared/hero/ch2_share_h_4.flac"
            hero "There's definitely a mirror.\n"
            voice "audio/voices/ch2/shared/narrator/ch2_share_n_27.flac"
            n "There isn't.\n"
            voice "audio/voices/ch2/stranger/contrarian/ch2_contrarian_8.flac"
            contrarian "You insisting it isn't there just makes me want to look at it even more.\n"
            menu:
                extend ""

                "{i}• Why {b}would{/b} you lie about that? What's the point?{/i}":
                    voice "audio/voices/ch2/shared/narrator/ch2_share_n_28.flac"
                    n "Exactly. Why would I lie about something so meaningless? What good would a mirror even do? Let you waste time preening yourself instead of doing what needs to be done?\n"

                "{i}• I also want to look at myself. I want to see how {b}handsome{/b} I am.{/i}":
                    voice "audio/voices/ch2/damsel/hero/ch2_dh_9.flac"
                    hero "We shouldn't waste time {i}preening{/i}, but if He {i}is{/i} lying about the mirror, it might be important.\n"
                    voice "audio/voices/ch2/shared/narrator/ch2_share_n_29.flac"
                    n "I'm not lying to you. Use your eyes, there is no mirror. Why would I lie about something so meaningless? What good would it even do?\n"
                    voice "audio/voices/ch2/stranger/contrarian/ch2_contrarian_9.flac"
                    contrarian "So we're all in agreement. We're looking.\n"

                "{i}• It doesn't matter.{/i}":
                    $ stranger_1_cabin_mirror_present = False
                    voice "audio/voices/ch2/shared/hero/ch2_share_h_5.flac"
                    hero "But it does matter! Don't you care if we're being lied to? If He's willing to lie about something as innocuous as a mirror, what else is He hiding from us?\n"
                    voice "audio/voices/ch2/shared/narrator/ch2_share_n_30.flac"
                    hide mirror onlayer front
                    n "I'm not lying to you. Use your eyes, there is no mirror. Why would I lie about something so meaningless? What good would a mirror even do? Let you waste time preening yourself instead of doing what needs to be done?\n"
                    voice "audio/voices/ch2/shared/hero/ch2_share_h_6.flac"
                    hero "But there {i}was{/i} a mirror a second ago.\n"
                    voice "audio/voices/ch2/stranger/contrarian/ch2_contrarian_10.flac"
                    contrarian "And now it's gone. You know that taking the mirror away from us isn't going to change things, right? We'll find it again, and then we'll see whatever it is that you don't want us to see.\n"

                "{i}• [[Remain silent.]{/i}":
                    voice "audio/voices/ch2/shared/hero/ch2_share_h_7b.flac"
                    hero "I care about whether we're being lied to. If He's willing to lie about something as innocuous as a mirror, what else could He be hiding from us?\n"
                    voice "audio/voices/ch2/shared/narrator/ch2_share_n_31.flac"
                    n "I'm not lying to you, I {i}promise{/i}. There isn't a mirror. Really.\n"

                "{i}• [[Approach the mirror.]{/i}" if stranger_1_cabin_mirror_approached == False:
                    label stranger_cabin_1_mirror_join:
                        $ stranger_1_cabin_mirror_approached = True
                        play audio "audio/one_shot/footsteps_creaky.flac"
                        hide farback onlayer farback
                        hide bg onlayer back
                        hide door onlayer back
                        hide table onlayer back
                        hide knife onlayer back
                        hide mirror onlayer back
                        scene bg stranger mirror close onlayer front at Position(ypos=1125)
                        with dissolve
                        voice "audio/voices/ch2/shared/narrator/ch2_share_n_32.flac"
                        n "You walk up to the wall next to the basement door. It's a wall. There isn't much to see here.\n"
                        if stranger_1_cabin_mirror_ask == False:
                            voice "audio/voices/ch2/shared/hero/ch2_share_h_8.flac"
                            hero "What are you talking about? This isn't a wall. It's a mirror. Or at least it'll {i}be{/i} a mirror once we wipe off that layer of grime.\n"
                        else:
                            voice "audio/voices/ch2/shared/hero/ch2_share_h_9.flac"
                            hero "This really isn't funny.\n"
                        $ current_run_mirror_touched = True
                        menu:
                            extend ""

                            "{i}• [[Wipe the mirror clean.]{/i}":
                                $ stranger_1_cabin_mirror_present = False
                                show bg stranger mirror close gone onlayer front
                                play audio "audio/one_shot/new/STP_claws_1.flac"
                                show player wall onlayer front at Position(ypos=1125) with dissolve
                                if stranger_1_cabin_mirror_ask == False:
                                    voice "audio/voices/ch2/shared/narrator/ch2_share_n_33.flac"
                                else:
                                    voice "audio/voices/ch2/shared/narrator/ch2_share_n_33a.flac"
                                n "You reach forward and rub your hand against the cabin wall. I hope you know how ridiculous you look right now.\n"
                                hide player onlayer front with dissolve
                                if stranger_1_cabin_mirror_ask:
                                    voice "audio/voices/ch2/shared/hero/ch2_share_h_10.flac"
                                    hero "But it was there a second ago!\n"
                                else:
                                    voice "audio/voices/ch2/shared/hero/ch2_share_h_6.flac"
                                    hero "But there was a mirror a second ago.\n"
                                voice "audio/voices/ch2/stranger/contrarian/ch2_contrarian_10.flac"
                                contrarian "And now it's gone. You know that taking the mirror away from us isn't going to change things, right? We'll find it again, and then we'll see whatever it is that you don't want us to see.\n"
                                play audio "audio/one_shot/footsteps_creaky.flac"
                                hide bg onlayer front
                                #scene farback stranger cabin onlayer farback at Position(ypos=1125)
                                show farback stranger cabin onlayer farback at Position(ypos=1125)
                                show back2 stranger cabin onlayer back at Position(ypos=1125)
                                show fore cabin stranger onlayer front at Position(ypos=1125)
                                if stranger_1_cabin_blade_tossed == False:
                                    show door cabin stranger1 onlayer front at Position(ypos=1125)
                                else:
                                    show door cabin stranger1 broken onlayer front at Position(ypos=1125)
                                show table stranger onlayer front at Position(ypos=1125)
                                if stranger_1_cabin_blade_taken == False:
                                    show knife stranger onlayer front at Position(ypos=1125)
                                with dissolve
                                jump cabin_interior_2_stranger_menu

            jump cabin_interior_2_stranger_menu

        "{i}• (Explore) [[Approach the mirror.]{/i}" if stranger_1_cabin_mirror_present and stranger_1_cabin_mirror_approached == False:
            $ stranger_1_cabin_mirror_approached = True
            jump stranger_cabin_1_mirror_join

        "{i}• (Explore) [[Take the blade.]{/i}" if stranger_1_cabin_blade_taken == False:
            $ stranger_1_cabin_blade_taken = True
            $ blade_held = True
            $ default_mouse = "blade"
            play audio "audio/one_shot/knife_pickup.flac"
            hide knife onlayer front
            with dissolve
            voice "audio/voices/ch2/stranger/_encounter/narrator/11.flac"
            n "You take the blade from the table. It would be difficult to slay the Princess and save the world without a weapon.\n"
            #n "You take the blade from the object holding it. It would be difficult to slay the Princess and save the world without a weapon.\n"
            voice "audio/voices/ch2/stranger/contrarian/ch2_contrarian_11.flac"
            contrarian "Okay, fine. You took the knife. But you really shouldn't hold it like {i}that{/i}.\n"
            voice "audio/voices/ch2/stranger/hero/ch2_sh_8.flac"
            hero "Then how are we supposed to hold it?\n"
            voice "audio/voices/ch2/stranger/contrarian/ch2_contrarian_12.flac"
            contrarian "The {i}other{/i} way. Thumb at the bottom. We'll look much cooler and more serious if we hold it with our thumb at the bottom.\n"
            voice "audio/voices/ch2/stranger/narrator/ch2_sn_16.flac"
            n "It really doesn't matter how you hold the blade, as long as you have it. Just make a choice.\n"
            menu:
                extend ""

                "{i}• [[Keep your grip as it is.]{/i}":
                    voice "audio/voices/ch2/stranger/narrator/ch2_sn_17.flac"
                    n "Great. You keep your grip the way it is. Your task awaits.\n"

                "{i}• [[Hold the blade the other way.]{/i}":
                    default stranger_other_way = False
                    $ stranger_other_way = True
                    play audio "audio/one_shot/knife_pickup.flac"
                    $ default_mouse = "thumb"
                    voice "audio/voices/ch2/stranger/narrator/ch2_sn_18.flac"
                    n "You switch your grip on the blade. Congratulations.\n"
                    voice "audio/voices/ch2/stranger/contrarian/ch2_contrarian_13.flac"
                    contrarian "Yes! Isn't this so much better?\n"
                    voice "audio/voices/ch2/stranger/hero/ch2_sh_9.flac"
                    hero "Okay, fine. You're right. This does look a lot better.\n"
                    voice "audio/voices/ch2/stranger/narrator/ch2_sn_19.flac"
                    n "It really doesn't matter. Just get on with it and deal with the Princess already.\n"

            jump cabin_interior_2_stranger_menu

        "{i}• (Explore) [[Throw the blade out the window.]{/i}" if stranger_1_cabin_blade_taken and blade_held:
            $ stranger_1_cabin_blade_tossed = True
            voice "audio/voices/ch2/stranger/contrarian/ch2_contrarian_14.flac"
            contrarian "Hahaha, {i}yes{/i}! Do it!\n"
            play audio "audio/final/_stranger_first_toss.flac"
            $ blade_held = False
            $ default_mouse = "default"
            $ achievement.grant("ACH_WINDOW")
            show door cabin stranger1 broken onlayer front at Position(ypos=1125)
            voice "audio/voices/ch2/stranger/_encounter/narrator/12.flac"
            n "Seriously? {i}Sigh{/i}. You throw the blade at the window, glass showering the cabin as your weapon flies out into the night. I suppose you'll just have to deal with the Princess without it.\n"
            if stranger_1_woods_share_loop:
                voice "audio/voices/ch2/stranger/contrarian/ch2_contrarian_15.flac"
                contrarian "We'll be fine. Don't worry about it. What's the worst that could happen, the world ends? Been there, done that.\n"
            else:
                voice "audio/voices/ch2/stranger/contrarian/ch2_contrarian_16.flac"
                contrarian "We'll be fine. Don't worry about it. What's the worst that could happen, the world ends? Oh well. If the Princess wasn't going to do it, the heat death of the universe was going to come for it eventually.\n"
            voice "audio/voices/ch2/stranger/_encounter/hero/5a.flac"
            hero "I'm not so sure. This place is already messing with my head. It would be much better if we had a weapon.\n"
            voice "audio/voices/ch2/stranger/narrator/ch2_sn_21.flac"
            n "What's done is done. Good luck, hero.\n"
            jump cabin_interior_2_stranger_menu

        "{i}• [[Enter the basement.]{/i}":
            $ quick_menu = False
            play audio "audio/one_shot/door_bedroom.flac"
            hide farback onlayer farback
            hide back2 onlayer back
            hide fore onlayer front
            hide door onlayer front
            hide door onlayer back
            hide table onlayer front
            hide knife onlayer back
            hide knife onlayer front
            hide mirror onlayer back
            hide mirror onlayer front
            scene bg black with fade
            jump stranger_1_basement_stairs

label stranger_1_basement_stairs:
    $ gallery_stranger.unlock_item(2)
    $ renpy.save_persistent()
    voice "audio/voices/ch2/stranger/_encounter/narrator/13.flac"
    scene farback nightmare basement onlayer farback at Position(ypos=1125)
    show bg stairs stranger onlayer back at Position(ypos=1125)
    show fore stairs stranger onlayer front at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    n "The door to the basement creaks open, revealing a web of branching staircases all built from unidentifiable materials.\n"
    #voice "audio/voices/ch2/stranger/_encounter/narrator/13a.flac"
    #n "The door to the basement creaks open, revealing a web of branching staircases all built from unidentifiable materials, none of them the same as any other.\n"
    voice "audio/voices/ch2/stranger/_encounter/narrator/14.flac"
    n "Nothing here seems to belong, and the closer you examine your surroundings, the more confused you get, your head throbbing with the effort of making sense of this place. None of the stairs even seem to go anywhere, let alone down.\n"
    voice "audio/voices/ch2/stranger/_encounter/narrator/15.flac"
    n "The air here has a sickening, almost sludge-like miasma to it, the kind of indiscernible quality that comes from the blending together of every scent there is at once. An odor that is simultaneously everything and yet the sum of it all coalescing into a thick, nauseating nothing.\n"
    voice "audio/voices/ch2/stranger/_encounter/narrator/16.flac"
    n "If the Princess lives here, slaying her is probably doing her a favor.\n"
    voice "audio/voices/ch2/stranger/_encounter/narrator/17.flac"
    n "Her voice, a disquieting collage of tone and personality, drags up the stairs.\n"
    voice "audio/voices/ch2/stranger/_encounter/princess/1.flac"
    spmid "Hello? HI. What are you doing here? Are you here to— KILL.\n"
    voice "audio/voices/ch2/stranger/_encounter/hero/6.flac"
    hero "Mmmm. No. No thank you.\n"
    voice "audio/voices/ch2/stranger/_encounter/contrarian/5.flac"
    contrarian "Oh, don't be such a baby!\n"
    voice "audio/voices/ch2/stranger/_encounter/hero/7.flac"
    hero "I don't want to do this. Let's just turn around and leave. This feels wrong, this feels like a trap, like whatever we do we're gonna die.\n"
    if blade_held == False:
        voice "audio/voices/ch2/stranger/_encounter/hero/8.flac"
        hero "We don't even have a weapon...\n"
    voice "audio/voices/ch2/stranger/_encounter/contrarian/6.flac"
    contrarian "But we already tried turning around and leaving, didn't we? And He threw up a wall. No way to go but forward, and whatever choice we make, whatever she is, we know one thing for sure.\n"
    voice "audio/voices/ch2/stranger/_encounter/hero/9.flac"
    hero "And what's that?\n"
    voice "audio/voices/ch2/stranger/_encounter/narrator/18.flac"
    n "That the fate of the world hinges on your success?\n"
    voice "audio/voices/ch2/stranger/_encounter/contrarian/7.flac"
    contrarian "There'll still be plenty of ways to ruin His day.\n"
    default stranger_stairs_choice = ""
    menu:

        extend ""

        "{i}• [[Take the harsh stairs to the left.]{/i}":
            $ stranger_stairs_choice = "left"
            $ stranger_schism_first = "harsh"
            $ quick_menu = False
            play audio "audio/final/footsteps_stone_short.flac"
            voice "audio/voices/ch2/stranger/_encounter/narrator/19.flac"
            hide bg onlayer back
            hide fore onlayer front
            show path stranger harsh 1 onlayer back at Position(ypos=1125)
            with fade
            if persistent.quick_menu:
                $ quick_menu = True
            n "You step to the left. The path is cruel against your feet, the impact of each step sending pulsing vibrations up your legs until there's nothing left in them to feel.\n"
            play audio "audio/final/footsteps_stone_short.flac"
            voice "audio/voices/ch2/stranger/_encounter/narrator/20.flac"
            show path stranger harsh 2 onlayer back at Position(ypos=1125)
            with dissolve
            n "The air around you grows colder the further you progress, at first a barely-noticeable drop, quickly evolving into a numbing cold.\n"
            play audio "audio/final/footsteps_stone_short.flac"
            voice "audio/voices/ch2/stranger/_encounter/narrator/20a.flac"
            show path stranger harsh 3 onlayer back at Position(ypos=1125)
            with dissolve
            n "Your toes feel like blocks of ice, your breaths puff out in clouds of condensed vapor.\n"
            play audio "audio/final/footsteps_stone_short.flac"
            voice "audio/voices/ch2/stranger/_encounter/narrator/20b.flac"
            show path stranger harsh 4 onlayer back at Position(ypos=1125)
            with dissolve
            n "You shudder against it as you continue down the stairway, losing yourself in the bone-deep chill.\n"

        "{i}• [[Take the center staircase.]{/i}":
            $ stranger_stairs_choice = "center"
            $ stranger_schism_first = "neutral"
            $ quick_menu = False
            play audio "audio/one_shot/footsteps_creaky.flac"
            voice "audio/voices/ch2/stranger/_encounter/narrator/21.flac"
            hide bg onlayer back
            hide fore onlayer front
            show path stranger neutral 2 onlayer back at Position(ypos=1125)
            with fade
            if persistent.quick_menu:
                $ quick_menu = True
            n "You step onto the center staircase. Paths wind out around you in all directions, each step branching into its own staircases which branch into their own staircases and so on. You aren't quite sure if yours is taking you up or down, but at the very least it's taking you somewhere.\n"
            play audio "audio/one_shot/footsteps_creaky.flac"
            voice "audio/voices/ch2/stranger/_encounter/narrator/22.flac"
            show path stranger neutral 3 onlayer back at Position(ypos=1125)
            with dissolve
            n "You concentrate on where you are, careful not to stray onto any of the many splitting branches that tempt you on all sides. You wouldn't want to have to backtrack to yours once you'd made a decision that took you someplace else.\n"
            play audio "audio/one_shot/footsteps_creaky.flac"
            voice "audio/voices/ch2/stranger/_encounter/narrator/23.flac"
            show path stranger neutral 4 onlayer back at Position(ypos=1125)
            with dissolve
            n "And so you take one careful, focused step after another. One foot down, another foot down, another after that. You lose yourself in following the correct pattern, in following what looks to you to be the true path, the one that cuts straight down. Or up. Or maybe sideways.\n"
            play audio "audio/one_shot/footsteps_creaky.flac"
            voice "audio/voices/ch2/stranger/_encounter/narrator/24.flac"
            show path stranger neutral 4 onlayer back at Position(ypos=1125)
            with dissolve
            n "But no matter the direction it goes, it certainly is the most true path, you know that much.\n"


        "{i}• [[Take the soft stairs to the right.]{/i}":
            $ stranger_stairs_choice = "right"
            $ stranger_schism_first = "gentle"
            $ quick_menu = False
            play audio "audio/one_shot/thump.flac"
            voice "audio/voices/ch2/stranger/_encounter/narrator/25.flac"
            hide bg onlayer back
            hide fore onlayer front
            show path stranger gentle 1 onlayer back at Position(ypos=1125)
            with fade
            if persistent.quick_menu:
                $ quick_menu = True
            n "You step to the right. The path feels soft and reassuring against your feet. The stairs almost seem to cradle you as you make your way down, like they're guiding your heels from one step directly to the next. You barely have to extend any effort to descend, the stairway doing most of the work for you, and you don't feel like there's any concern that you might slip or tumble or lose your way.\n"
            play audio "audio/one_shot/thump.flac"
            voice "audio/voices/ch2/stranger/_encounter/narrator/26.flac"
            show path stranger gentle 2 onlayer back at Position(ypos=1125)
            with dissolve
            n "But the further you go, the deeper you sink in. First it's like a lovely plush carpet, your toes digging down and barely hitting any resistance at all. But soon enough you're fighting just to keep your knees from sinking out of sight.\n"
            play audio "audio/one_shot/thump.flac"
            voice "audio/voices/ch2/stranger/_encounter/narrator/27.flac"
            show path stranger gentle 3 onlayer back at Position(ypos=1125)
            with dissolve
            n "The softness threatens to swallow you whole, to wrest control of your body and surround you in a false ethereal bliss, pretending to save you from the cruelties of choice and consequence.\n"
            play audio "audio/one_shot/thump.flac"
            voice "audio/voices/ch2/stranger/_encounter/narrator/28.flac"
            show path stranger gentle 4 onlayer back at Position(ypos=1125)
            with dissolve
            n "It's slow-going, but you manage to fight against the overwhelming urge to fall back into the comfort and nothingness, the very struggle to continue forward consuming your every thought.\n"

label stranger_1_basement:

    voice "audio/voices/ch2/stranger/_encounter/narrator/29.flac"
    stop music fadeout 15.0
    stop sound fadeout 20.0
    stop tertiary fadeout 20.0
    play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 15.0
    hide farback onlayer farback
    hide path onlayer back
    show bg derealization poem onlayer farback at Position(ypos=1125)
    show dereal strange 1 onlayer back at Position(ypos=1125)
    with Dissolve(4.0)
    n "You slowly lose sense of yourself the further you go.\n"
    voice "audio/voices/ch2/stranger/_encounter/narrator/29a.flac"
    $ default_mouse = "eye"
    show dereal strange 2 onlayer back at Position(ypos=1125)
    n "Time disappears, and you can feel yourself begin to untether.\n"
    voice "audio/voices/ch2/stranger/_encounter/narrator/30.flac"
    show dereal strange 3 onlayer back at Position(ypos=1125)
    n "Physical sensations dull and then vanish, until the only things experienced are the endlessly repeating patterns and emotions of the journey. A continuous march forward to a destination long forgotten.\n"
    hide dereal onlayer back at Position(ypos=1125)
    with Dissolve(2.0)
    $ renpy.pause(1.0)
    $ gallery_stranger.unlock_item(3)
    $ renpy.save_persistent()
    voice "audio/voices/ch2/stranger/_encounter/narrator/31.flac"
    show derealization poem onlayer back at Position(ypos=1125)
    n "Consumption and betrayal. Skepticism and blind devotion. Rivalry and submission. Terror and longing. Pain and unfamiliarity. And at the heart of it all, an emotion that can only be described as—.\n{w=15.3}{nw}"
    if blade_held:
        $ default_mouse = "blade"
    else:
        $ default_mouse = "default"
    show screen disableclick(0.5)
    $ gallery_stranger.unlock_item(4)
    $ renpy.save_persistent()
    stop secondary
    play sound "audio/looping/ambient_cabin.ogg" loop
    play music "audio/_music/ch2/stranger/The Stranger.flac"
    queue music "audio/_music/ch2/stranger/The Stranger Loop.flac" loop
    hide derealization onlayer back
    hide bg onlayer farback
    show farback stranger start onlayer farback at Position(ypos=1125)
    show bg stranger start onlayer back at Position(ypos=1125)
    if stranger_schism_first == "gentle":
        show stranger gentle start talk onlayer back at Position(ypos=1125)
        show fore stranger start onlayer back at Position(ypos=1125)
        voice "audio/voices/ch2/stranger/_encounter/princess/2.flac"
        p "Are you okay?\n"
        show stranger gentle start onlayer back
    elif stranger_schism_first == "harsh":
        show stranger harsh start talk onlayer back at Position(ypos=1125)
        show fore stranger start onlayer back at Position(ypos=1125)
        voice "audio/voices/ch2/stranger/_encounter/princess/3.flac"
        p "Are you just going to stand there?\n"
        show stranger harsh start onlayer back
    else:
        show stranger neutral start talk onlayer back at Position(ypos=1125)
        show fore stranger start onlayer back at Position(ypos=1125)
        voice "audio/voices/ch2/stranger/_encounter/princess/4.flac"
        p "Can I help you?\n"
        show stranger neutral start onlayer back
    voice "audio/voices/ch2/stranger/_encounter/hero/10.flac"
    hero "What— what the hell was that?! What happened to us?\n"
    voice "audio/voices/ch2/stranger/_encounter/contrarian/8.flac"
    contrarian "I feel so... strange. Like I'm fundamentally different, but also... still the same person I was at the top of the stairs.\n"
    #voice "audio/voices/ch2/stranger/_encounter/hero/11.flac"
    #hero "I don't know...\n"
    voice "audio/voices/ch2/stranger/_encounter/contrarian/9.flac"
    contrarian "Oh well! That was a trip but now it's over. Time to get back to our old devilish ways.\n"
    voice "audio/voices/ch2/stranger/_encounter/narrator/32.flac"
    n "The Princess, eyes bright but otherwise shrouded in darkness, watches you impatiently from the other side of the basement. Don't forget why you're here.\n"
    voice "audio/voices/ch2/stranger/_encounter/contrarian/10.flac"
    contrarian "And why are we here again? In case you weren't listening, I'm afraid I lost myself on the way down.\n"
    # FAST
    voice "audio/voices/ch2/stranger/_encounter/narrator/33.flac"
    n "{i}Sigh.{/i} You're here to—\n{w=1.19}{nw}"
    show screen disableclick(0.5)
    voice "audio/voices/ch2/stranger/_encounter/hero/12.flac"
    hero "He's just being an ass. We remember. Though I'm still not sure if we should trust you. Let's talk to her for a bit. Try and get our bearings. She seems... normal.\n"

label stranger_basement_menu:
    # first schism can be "neutral" "harsh" or "gentle"
    default stranger_schism_first = ""
    default stranger_schism_count = 1
    default stranger_schism_gentle = False
    default stranger_schism_neutral = False
    default stranger_schism_harsh = False
    default stranger_schism_emo = False
    default stranger_schism_monster = False

    # block for code reduction via preset variables

    default stranger_gentle_set = False
    default stranger_neutral_set = False
    default stranger_harsh_set = False
    default stranger_emo_set = False
    default stranger_monster_set = False

    if stranger_gentle_set:
        $ stranger_gentle_set = False
        $ stranger_schism_gentle = True
    if stranger_neutral_set:
        $ stranger_neutral_set = False
        $ stranger_schism_neutral = True
    if stranger_harsh_set:
        $ stranger_harsh_set = False
        $ stranger_schism_harsh = True
    if stranger_emo_set:
        $ stranger_emo_set = False
        $ stranger_schism_emo = True
    if stranger_monster_set:
        $ stranger_monster_set = False
        $ stranger_schism_monster = True

    default stranger_current_schism_comment = False
    default stranger_schism_up = True

    # count of no. times options have been selected in the basement.
    default stranger_basement_menu_count = 0

    # variables for menu options

    default stranger_menu_sorry = False
    default stranger_menu_more = False
    default stranger_menu_more_break = False
    default stranger_menu_name = False
    default stranger_menu_weird = False
    default stranger_menu_reason = False
    default stranger_menu_threat_share = False
    default stranger_menu_what_do = False

    default stranger_current_speaker = ""

    #
    default stranger_floating = ""

    if stranger_current_schism_comment == False and stranger_schism_up and stranger_schism_count != 1:
        $ stranger_current_schism_comment = True
        if stranger_schism_count == 2:
            voice "audio/voices/ch2/stranger/_encounter/narrator/34.flac"
            n "As the Princess speaks again, it's almost as if she fractures, and where there was once just one of her, there is now another.\n"
            voice "audio/voices/ch2/stranger/_encounter/contrarian/11.flac"
            contrarian "We can do that?!\n"
            voice "audio/voices/ch2/stranger/_encounter/hero/13.flac"
            hero "I don't like this. It's those cabins all over again. Can... can we put her back?\n"
            if stranger_1_woods_share_loop == False:
                voice "audio/voices/ch2/stranger/_encounter/narrator/35.flac"
                n "'Again?' Have you been here before?\n"
                voice "audio/voices/ch2/stranger/_encounter/hero/14.flac"
                hero "Should we tell Him?\n" id stranger_basement_menu_4ccb9032
                voice "audio/voices/ch2/stranger/_encounter/contrarian/12.flac"
                contrarian "Nah. Let him stew.\n"
                voice "audio/voices/ch2/stranger/_encounter/hero/15.flac"
                hero "Right. I'm telling him. Yeah, we've 'been here before.' But we never went to the cabin. We just... turned around and left, until...\n"
                voice "audio/voices/ch2/stranger/_encounter/narrator/36.flac"
                n "Until?\n"
                voice "audio/voices/ch2/stranger/_encounter/hero/16.flac"
                hero "It's hard to describe. Until the only thing we could see was the same cabin going on forever? And then you told us that the world ended and we died. And then we woke up, and I'm pretty sure you're familiar with all the rest of it.\n"
            else:
                if stranger_1_forest_share_loop_insist:
                    voice "audio/voices/ch2/stranger/_encounter/narrator/37.flac"
                    n "You said 'the world ended' last time you were here, didn't you?\n"
                    voice "audio/voices/ch2/stranger/_encounter/contrarian/13.flac"
                    contrarian "Yeah, what of it?\n"
                else:
                    voice "audio/voices/ch2/stranger/_encounter/narrator/38.flac"
                    n "You said you'd been here before, right? What exactly happened last time?\n"
                    voice "audio/voices/ch2/stranger/_encounter/contrarian/14.flac"
                    contrarian "Does it matter?\n"
                    voice "audio/voices/ch2/stranger/_encounter/narrator/39.flac"
                    n "Yes, it matters! But I'm not going to waste any more time prying out details if you're going to be so irritating about it.\n"
            voice "audio/voices/ch2/stranger/_encounter/narrator/40a.flac"
            n "It seems to me like you saw something you weren't supposed to have seen. If only you'd listened to whatever words of wisdom you were given in that other reality. {i}Sigh.{/i} But what's done is done, isn't it?\n"
            voice "audio/voices/ch2/stranger/_encounter/narrator/41.flac"
            n "Whatever you saw last time? Unsee it. Whatever thoughts weaseled their way into your head? Unthink them, if it's not already too late. You have a job to do here but you need to do it now.\n"
            voice "audio/voices/ch2/stranger/_encounter/contrarian/15.flac"
            contrarian "New plan! Let's see if we can make even more of her.\n"

        if stranger_schism_count == 3:
            voice "audio/voices/ch2/stranger/_encounter/hero/17.flac"
            hero "I don't think we're going to be able to put her back.\n"
            voice "audio/voices/ch2/stranger/_encounter/contrarian/16.flac"
            contrarian "It kind of hurts to think about it, doesn't it? It's like everything we say just multiplies her.\n"
            voice "audio/voices/ch2/stranger/_encounter/narrator/42.flac"
            n "It certainly looks that way. So please, for the love of everything, stop asking her questions, and stop stalling. You're obviously just making things worse.\n"


        if stranger_schism_count == 4:
            voice "audio/voices/ch2/stranger/_encounter/contrarian/17.flac"
            contrarian "Okay. This was fun for a bit, but we can't even really interact with her, can we? What's the point of asking questions if all we're going to get is a million answers?\n"
            voice "audio/voices/ch2/stranger/_encounter/hero/18.flac"
            hero "I can't even follow what's going on anymore.\n"
            voice "audio/voices/ch2/stranger/_encounter/contrarian/18.flac"
            contrarian "We need to get out of here. This whole place is making me itch.\n"

        if stranger_schism_count == 5:
            $ gallery_stranger.unlock_item(5)
            $ renpy.save_persistent()
            voice "audio/voices/ch2/stranger/_encounter/narrator/43.flac"
            n "This is reaching its breaking point. If you don't act now, there will be nothing in here but her. Take a deep breath and focus up. You can do this.\n"
            voice "audio/voices/ch2/stranger/_encounter/hero/19a.flac"
            hero "But how do we decide what to do? Can there even be a right choice when all of them are so different?\n"
            voice "audio/voices/ch2/stranger/_encounter/narrator/44.flac"
            n "Stop overthinking it. Your drifting thoughts have clearly been part of the reason this situation has gotten out of hand. If you're trying to do the right thing, there's only ever been the one option, and that option is slaying her.\n"
            voice "audio/voices/ch2/stranger/_encounter/contrarian/19a.flac"
            contrarian "Just do something! Do anything! Do all of it if that's what you want. This place is hell and it's only getting worse.\n"


    menu:
        extend ""

        "{i}• (Explore) ''I'm sorry... I didn't realize I was here.''{/i}" if stranger_schism_count == 1 and stranger_menu_sorry == False:
            $ stranger_menu_sorry = True
            $ stranger_basement_menu_count += 1
            if stranger_schism_first == "gentle":
                voice "audio/voices/ch2/stranger/_encounter/princess/5.flac"
                show stranger gentle start talk onlayer back
                p "That's okay. Sometimes I forget where I am too.\n"
                voice "audio/voices/ch2/stranger/_encounter/narrator/45.flac"
                show stranger gentle start onlayer back
                hide fore onlayer back
                with dissolve
                n "The shadows recede, revealing the Princess' face.\n"
                voice "audio/voices/ch2/stranger/_encounter/hero/20.flac"
                hero "She's so warm, and friendly...\n"
                voice "audio/voices/ch2/stranger/_encounter/narrator/46.flac"
                n "It's deception. Don't buy into it.\n"
                play audio "audio/one_shot/glass_1.flac"
                hide stranger onlayer back
                hide farback onlayer farback
                hide bg onlayer back
                show stranger center onlayer farback at Position(ypos=1125)

            elif stranger_schism_first == "harsh":
                voice "audio/voices/ch2/stranger/_encounter/princess/6.flac"
                show stranger harsh start talk onlayer back
                p "Yeah. I know. I've been watching you stare at me for a long, long time.\n"
                voice "audio/voices/ch2/stranger/_encounter/narrator/45.flac"
                show stranger harsh start onlayer back
                hide fore onlayer back
                with dissolve
                n "The shadows recede, revealing the Princess' face.\n"
                voice "audio/voices/ch2/stranger/_encounter/contrarian/20.flac"
                contrarian "I don't think she likes us.\n"
                voice "audio/voices/ch2/stranger/_encounter/hero/21.flac"
                hero "Wouldn't you be skeptical of someone stumbling in here if you were her? We lost ourselves the second we stepped into this place. I don't know how long she's been here, but I can't imagine it'd be easy for her to trust anyone.\n"
                voice "audio/voices/ch2/stranger/_encounter/hero/22.flac"
                hero "Those eyes, though... they're so sharp.\n"
                voice "audio/voices/ch2/stranger/_encounter/narrator/47.flac"
                n "It's just deception. Don't buy into it. You can do this.\n"
                play audio "audio/one_shot/glass_1.flac"
                hide stranger onlayer back
                hide farback onlayer farback
                hide bg onlayer back
                show stranger center onlayer farback at Position(ypos=1125)

            elif stranger_schism_first == "neutral":
                voice "audio/voices/ch2/stranger/_encounter/princess/7.flac"
                show stranger neutral start talk onlayer back
                p "And yet here you are. How strange. Do you remember anything at all? Do you know why you're here? Do you know me?\n"
                show stranger neutral start onlayer back
                hide fore onlayer back
                with dissolve
                voice "audio/voices/ch2/stranger/_encounter/narrator/45.flac"
                n "The shadows recede, revealing the Princess' face.\n"
                voice "audio/voices/ch2/stranger/_encounter/hero/23.flac"
                hero "She's so... blank. I have no idea who she is.\n"
                voice "audio/voices/ch2/stranger/_encounter/contrarian/21.flac"
                contrarian "Isn't that fun? A new puzzle for us to take apart.\n"
                voice "audio/voices/ch2/stranger/_encounter/narrator/48.flac"
                n "If she's keeping her cards close to her chest, it's because she wants to deceive you.\n"
                play audio "audio/one_shot/glass_1.flac"
                hide stranger onlayer back
                hide farback onlayer farback
                hide bg onlayer back
                show stranger center onlayer farback at Position(ypos=1125)

            $ stranger_current_schism_comment = False
            # breaks into a second schism
            $ stranger_schism_count += 1
            if blade_held:
                if stranger_schism_first != "harsh":
                    $ stranger_schism_harsh = True
                else:
                    $ stranger_schism_neutral = True
            else:
                if stranger_schism_first != "gentle":
                    $ stranger_schism_gentle = True
                else:
                    $ stranger_schism_neutral = True

            if stranger_schism_gentle:
                show gentle stranger talk onlayer back at Position(ypos=1125)
                with hpunch
                voice "audio/voices/ch2/stranger/_encounter/princess/8.flac"
                p "It's okay. Don't worry. Sometimes I get lost here too.\n"
                show gentle stranger onlayer back
            if stranger_schism_neutral:
                show neutral stranger talk onlayer back at Position(ypos=1125)
                with hpunch
                voice "audio/voices/ch2/stranger/_encounter/princess/9.flac"
                p "How strange. So why are you here?\n"
                show neutral stranger onlayer back
            if stranger_schism_harsh:
                show harsh stranger talk onlayer back at Position(ypos=1125)
                with hpunch
                voice "audio/voices/ch2/stranger/_encounter/princess/10.flac"
                p "I'm tired of waiting for an answer.\n"
                show harsh stranger onlayer back

            jump stranger_basement_menu

        "{i}• (Explore) ''There's more of you now...''{/i}" if stranger_schism_count > 1 and stranger_menu_more == False and stranger_schism_count != 5:
            $ stranger_menu_more = True
            if stranger_schism_first == "gentle":
                voice "audio/voices/ch2/stranger/_encounter/princess/11.flac"
                show stranger center talk onlayer farback
                p "Do you need help? Not that there's much I can do chained up like this, but I'm the only one down here, so if you need anything I'll do my best.\n"
            elif stranger_schism_first == "neutral":
                voice "audio/voices/ch2/stranger/_encounter/princess/12.flac"
                show stranger center talk onlayer farback
                p "There must be something wrong with you. I'm the same as I was a moment ago.\n"
            elif stranger_schism_first == "harsh":
                voice "audio/voices/ch2/stranger/_encounter/princess/13.flac"
                show stranger center talk onlayer farback
                p "And what's that supposed to mean? Are you trying to get under my skin?\n"

            show stranger center onlayer farback at Position(ypos=1125)
            if stranger_schism_emo:
                voice "audio/voices/ch2/stranger/_encounter/princess/14.flac"
                show emo stranger talk onlayer front
                p "I don't feel like I've gotten any bigger.\n"
                show emo stranger onlayer front
            if stranger_schism_monster:
                voice "audio/voices/ch2/stranger/_encounter/princess/15a.flac"
                show monster stranger talk onlayer front
                spmid "It must be fear creeping into your heart. You know you can't stop me.\n"
                show monster stranger onlayer front

            if stranger_schism_neutral == False and stranger_schism_first != "neutral":
                $ stranger_menu_more_break = True
                $ stranger_schism_neutral = True
                $ stranger_current_schism_comment = False
                # breaks into a second schism
                $ stranger_schism_count += 1
                voice "audio/voices/ch2/stranger/_encounter/princess/12.flac"
                play audio "audio/final/Assorted_Glass Breaking_7.flac"
                show neutral stranger talk onlayer back
                with hpunch
                p "There must be something wrong with you. I'm the same as I was a moment ago.\n"
                show neutral stranger onlayer back
            elif stranger_schism_harsh == False and stranger_schism_first != "harsh":
                $ stranger_menu_more_break = True
                $ stranger_schism_harsh = True
                $ stranger_current_schism_comment = False
                # breaks into a second schism
                $ stranger_schism_count += 1
                voice "audio/voices/ch2/stranger/_encounter/princess/13.flac"
                play audio "audio/final/Assorted_Glass Breaking_7.flac"
                show harsh stranger talk onlayer back
                with hpunch
                p "And what is that supposed to mean? Are you trying to get under my skin?\n"
                show harsh stranger onlayer back
            elif stranger_schism_gentle == False and stranger_schism_first != "gentle":
                $ stranger_menu_more_break = True
                $ stranger_schism_gentle = True
                $ stranger_current_schism_comment = False
                # breaks into a second schism
                $ stranger_schism_count += 1
                voice "audio/voices/ch2/stranger/_encounter/princess/11a.flac"
                play audio "audio/final/Assorted_Glass Breaking_7.flac"
                show gentle stranger talk onlayer back
                with hpunch
                p "Do you need help? Not that there's much I can do chained up like this, but I'm the only one down here, so if you need anything I'll do my best.\n"
                show gentle stranger onlayer back


            if stranger_menu_more_break:
                voice "audio/voices/ch2/stranger/_encounter/narrator/49.flac"
                n "She fractures again.\n"
                voice "audio/voices/ch2/stranger/_encounter/hero/24.flac"
                hero "I don't like where this is going.\n"
                voice "audio/voices/ch2/stranger/_encounter/narrator/50.flac"
                n "Neither do I. Which is why you need to slay her now before things get more complicated than they already are.\n"

            else:
                if stranger_schism_neutral:
                    voice "audio/voices/ch2/stranger/_encounter/princess/12.flac"
                    show neutral stranger talk onlayer back
                    p "There must be something wrong with you. I'm the same as I was a moment ago.\n"
                    show neutral stranger onlayer back
                if stranger_schism_harsh:
                    voice "audio/voices/ch2/stranger/_encounter/princess/13a.flac"
                    show harsh stranger talk onlayer back
                    p "And what is that supposed to mean? Are you trying to get under my skin?\n"
                    show harsh stranger onlayer back
                if stranger_schism_gentle:
                    voice "audio/voices/ch2/stranger/_encounter/princess/11.flac"
                    show gentle stranger talk onlayer back
                    p "Do you need help? Not that there's much I can do chained up like this, but I'm the only one down here, so if you need anything I'll do my best.\n"
                    show gentle stranger onlayer back
                voice "audio/voices/ch2/stranger/_encounter/contrarian/22.flac"
                contrarian "Huh. And here I was expecting her to split again. Is that it? What do we do now?\n"
                voice "audio/voices/ch2/stranger/_encounter/narrator/51.flac"
                n "You slay her.\n"
            voice "audio/voices/ch2/stranger/_encounter/hero/25.flac"
            hero "How would we even do that? Where would we start?\n"
            if blade_held == False:
                voice "audio/voices/ch2/stranger/_encounter/narrator/52.flac"
                n "You could always start by retrieving the blade...\n"
                if stranger_1_cabin_blade_tossed:
                    voice "audio/voices/ch2/stranger/_encounter/hero/26.flac"
                    hero "The one that he made us throw out the window?\n"
                    voice "audio/voices/ch2/stranger/_encounter/contrarian/23.flac"
                    contrarian "I wasn't the one who threw it.\n"
                    voice "audio/voices/ch2/stranger/_encounter/hero/27.flac"
                    hero "Oh come on, you told us to! Don't try to pass the blame now that it's come back to bite us.\n"
                    voice "audio/voices/ch2/stranger/_encounter/contrarian/24.flac"
                    contrarian "Well, if I'd known we'd be dealing with this, maybe I wouldn't have been so hasty with my suggestions.\n"
                else:
                    voice "audio/voices/ch2/stranger/_encounter/hero/28.flac"
                    hero "Can we even leave this place? I don't like thinking about what might happen to us if we have to go back... {i}through{/i} those stairs.\n"
                    voice "audio/voices/ch2/stranger/_encounter/narrator/53.flac"
                    n "Well that's where the blade is. If you want it, you'll have to go and get it.\n"
            else:
                voice "audio/voices/ch2/stranger/_encounter/narrator/54.flac"
                n "You could always start by stabbing her.\n"
                voice "audio/voices/ch2/stranger/_encounter/hero/29.flac"
                hero "... Which her?\n"
                voice "audio/voices/ch2/stranger/_encounter/narrator/55.flac"
                n "Any of them.\n"
                voice "audio/voices/ch2/stranger/_encounter/contrarian/25.flac"
                contrarian "I don't know about you but I'm sure glad we took that knife with us. I can't believe someone suggested you toss it out the window. Can you imagine?\n"

            jump stranger_basement_menu

        "{i}• (Explore) ''What's your name?''{/i}" if stranger_menu_name == False and stranger_schism_count != 5:
            $ stranger_menu_name = True
            if stranger_schism_count == 1:
                hide fore onlayer back
                show stranger start talk onlayer back at Position(ypos=1125)
                with dissolve
            else:
                show stranger center talk onlayer farback at Position(ypos=1125)
            if stranger_schism_first == "gentle":
                voice "audio/voices/ch2/stranger/_encounter/princess/16.flac"
                p "You can call me Princess, if you'd like...\n"
            if stranger_schism_first == "neutral":
                voice "audio/voices/ch2/stranger/_encounter/princess/17.flac"
                p "Princess.\n"
            if stranger_schism_first == "harsh":
                voice "audio/voices/ch2/stranger/_encounter/princess/18.flac"
                p "You can address me as Your Royal Highness, or Her Majesty. Any honorific should do, really.\n"
            if stranger_schism_count == 1:
                show stranger start onlayer back at Position(ypos=1125)
            else:
                show stranger center onlayer farback at Position(ypos=1125)
            if stranger_schism_count == 1:
                $ stranger_current_schism_comment = False
                # breaks into a second schism
                $ stranger_schism_count += 1
                if blade_held:
                    if stranger_schism_first != "harsh":
                        $ stranger_schism_harsh = True
                        play audio "audio/final/Assorted_ForcefullyBreakingGlass_1.flac"
                        hide fore onlayer back
                        hide stranger onlayer back
                        hide farback onlayer farback
                        hide bg onlayer back
                        show stranger center onlayer farback at Position(ypos=1125)
                        show harsh stranger talk onlayer back at Position(ypos=1125)
                        with hpunch
                    else:
                        $ stranger_schism_neutral = True
                        play audio "audio/final/Assorted_ForcefullyBreakingGlass_1.flac"
                        hide stranger onlayer back
                        hide fore onlayer back
                        hide farback onlayer farback
                        hide bg onlayer back
                        show stranger center onlayer farback at Position(ypos=1125)
                        show neutral stranger talk onlayer back at Position(ypos=1125)
                        with hpunch
                else:
                    if stranger_schism_first != "gentle":
                        $ stranger_schism_gentle = True
                        play audio "audio/final/Assorted_ForcefullyBreakingGlass_1.flac"
                        hide fore onlayer back
                        hide stranger onlayer back
                        hide farback onlayer farback
                        hide bg onlayer back
                        show stranger center onlayer farback at Position(ypos=1125)
                        show gentle stranger talk onlayer back at Position(ypos=1125)
                        with hpunch
                    else:
                        $ stranger_schism_neutral = True
                        play audio "audio/final/Assorted_ForcefullyBreakingGlass_1.flac"
                        hide stranger onlayer back
                        hide farback onlayer farback
                        hide bg onlayer back
                        show stranger center onlayer farback at Position(ypos=1125)
                        show neutral stranger talk onlayer back at Position(ypos=1125)
                        with hpunch

            if stranger_schism_gentle:
                voice "audio/voices/ch2/stranger/_encounter/princess/16.flac"
                show gentle stranger talk onlayer back
                p "You can call me Princess if you'd like...\n"
                show gentle stranger onlayer back
            if stranger_schism_neutral:
                voice "audio/voices/ch2/stranger/_encounter/princess/17.flac"
                show neutral stranger talk onlayer back
                p "Princess.\n"
                show neutral stranger onlayer back
            if stranger_schism_harsh:
                voice "audio/voices/ch2/stranger/_encounter/princess/18.flac"
                show harsh stranger talk onlayer back
                p "You can address me as Your Royal Highness, or Her Majesty. Any honorific should do, really.\n"
                show harsh stranger onlayer back
            if stranger_schism_emo:
                voice "audio/voices/ch2/stranger/_encounter/princess/19.flac"
                show emo stranger talk onlayer front
                p "It doesn't matter. I've been down here for so long. What's the point of a name if there's no one around to use it?\n"
                show emo stranger onlayer front
            if stranger_schism_monster:
                voice "audio/voices/ch2/stranger/_encounter/princess/20a.flac"
                show monster stranger talk onlayer front
                spmid "I don't need a name. My name is whatever hushed whispers follow in the wake of my devastation.\n"
                show monster stranger onlayer front
            if stranger_schism_count != 2:
                #voice "audio/voices/ch2/stranger/_encounter/hero/30.flac"
                #hero "She doesn't have a name...\n"
                voice "audio/voices/ch2/stranger/_encounter/contrarian/26.flac"
                contrarian "None of them have names.\n"
                voice "audio/voices/ch2/stranger/_encounter/narrator/56.flac"
                n "How astute. I told you she was untrustworthy.\n"

            jump stranger_basement_menu



        "{i}• (Explore) ''Getting down here was... weird. Like I was pulled apart and put back together again. Do you know what happened to me?''{/i}" if stranger_menu_weird == False and stranger_schism_count != 5:
            $ stranger_menu_weird = True
            default stranger_weird_break = False
            # get sad, otherwise get monster
            if stranger_schism_count == 1:
                hide fore onlayer back
                show stranger start talk onlayer back at Position(ypos=1125)
                with dissolve
            else:
                show stranger center talk onlayer farback at Position(ypos=1125)
            if stranger_schism_first == "gentle":
                voice "audio/voices/ch2/stranger/_encounter/princess/21.flac"
                p "I don't know what happened to you, but you look like you're in one piece now. But I understand. Sometimes I feel like I'm being pulled apart, too. It's so terrifying down here. But at least now you're not alone, and I'm not alone, either.\n"
            if stranger_schism_first == "harsh":
                voice "audio/voices/ch2/stranger/_encounter/princess/22.flac"
                p "What, like you need me to hold your hand and tell you everything's okay? You're not really cut out for this, are you? Why are you even here?\n"
            if stranger_schism_first == "neutral":
                voice "audio/voices/ch2/stranger/_encounter/princess/23.flac"
                p "I don't remember what it was like before I was in this place. Why would I know what happened to you?\n"
            if stranger_schism_count == 1:
                show stranger start onlayer back at Position(ypos=1125)
            else:
                show stranger center onlayer farback at Position(ypos=1125)
            if stranger_schism_emo == False:
                $ stranger_schism_count += 1
                $ stranger_weird_break = True
                $ stranger_emo_set = True
                voice "audio/voices/ch2/stranger/_encounter/princess/24.flac"
                play audio "audio/final/Assorted_ForcefullyBreakingGlass_3.flac"
                hide fore onlayer back
                hide stranger onlayer back
                hide farback onlayer farback
                hide bg onlayer back
                show stranger center onlayer farback at Position(ypos=1125)
                show emo stranger talk onlayer front at Position(ypos=1125)
                with hpunch
                p "We're probably stuck down here forever, aren't we? There's no way out, and barely a way in...\n"
                show emo stranger onlayer front

            elif stranger_schism_monster == False:
                $ stranger_schism_count += 1
                $ stranger_weird_break = True
                $ stranger_monster_set = True
                voice "audio/voices/ch2/stranger/_encounter/princess/25a.flac"
                play audio "audio/final/Assorted_ForcefullyBreakingGlass_3.flac"
                hide fore onlayer back
                hide stranger onlayer back
                hide farback onlayer farback
                hide bg onlayer back
                show stranger center onlayer farback at Position(ypos=1125)
                show monster stranger talk onlayer front at Position(ypos=1125)
                with hpunch
                spmid "I thought they would send something better to deal with me. If the stairs managed to chew you up, I will devour you.\n"
                show monster stranger onlayer front

            if stranger_weird_break == False:
                if stranger_schism_gentle == False and stranger_schism_first != "gentle":
                    $ stranger_schism_count += 1
                    $ stranger_current_schism_comment = False
                    $ stranger_gentle_set = True
                    $ stranger_weird_break = True
                    voice "audio/voices/ch2/stranger/_encounter/princess/26.flac"
                    play audio "audio/final/Assorted_ForcefullyBreakingGlass_3.flac"
                    hide stranger onlayer back
                    hide farback onlayer farback
                    hide bg onlayer back
                    show stranger center onlayer farback at Position(ypos=1125)
                    show gentle stranger talk onlayer back at Position(ypos=1125)
                    with hpunch
                    p "Sometimes I feel like I'm being pulled apart, too. It's so terrifying down here. But at least now you're not alone, and I'm not alone, either.\n"
                    show gentle stranger onlayer back
                elif stranger_schism_harsh == False and stranger_schism_first != "harsh":
                    $ stranger_schism_count += 1
                    $ stranger_current_schism_comment = False
                    $ stranger_harsh_set = True
                    $ stranger_weird_break = True
                    voice "audio/voices/ch2/stranger/_encounter/princess/27.flac"
                    play audio "audio/final/Assorted_ForcefullyBreakingGlass_3.flac"
                    hide fore onlayer back
                    hide stranger onlayer back
                    hide farback onlayer farback
                    hide bg onlayer back
                    show stranger center onlayer farback at Position(ypos=1125)
                    show harsh stranger talk onlayer back at Position(ypos=1125)
                    with hpunch
                    p "You're not really cut out for this, are you? Why are you even here?\n"
                    show harsh stranger onlayer back
                elif stranger_schism_neutral == False and stranger_schism_first != "neutral":
                    $ stranger_schism_count += 1
                    $ stranger_current_schism_comment = False
                    $ stranger_neutral_set = True
                    $ stranger_weird_break = True
                    voice "audio/voices/ch2/stranger/_encounter/princess/28.flac"
                    play audio "audio/final/Assorted_ForcefullyBreakingGlass_3.flac"
                    hide fore onlayer back
                    hide stranger onlayer back
                    hide farback onlayer farback
                    hide bg onlayer back
                    show stranger center onlayer farback at Position(ypos=1125)
                    show neutral stranger talk onlayer back at Position(ypos=1125)
                    with hpunch
                    p "I don't remember what it was like before I was in this place. Why would I know what happened to you?\n"
                    show neutral stranger onlayer back

            if stranger_schism_gentle:
                voice "audio/voices/ch2/stranger/_encounter/princess/26.flac"
                show gentle stranger talk onlayer back
                p "Sometimes I feel like I'm being pulled apart, too. It's so terrifying down here. But at least now you're not alone, and I'm not alone, either.\n"
                show gentle stranger onlayer back
            if stranger_schism_neutral:
                voice "audio/voices/ch2/stranger/_encounter/princess/28.flac"
                show neutral stranger talk onlayer back
                p "I don't remember what it was like before I was in this place. Why would I know what happened to you?\n"
                show neutral stranger onlayer back
            if stranger_schism_harsh:
                voice "audio/voices/ch2/stranger/_encounter/princess/27.flac"
                show harsh stranger talk onlayer back
                p "You're not really cut out for this, are you? Why are you even here?\n"
                show harsh stranger onlayer back
            if stranger_schism_emo:
                voice "audio/voices/ch2/stranger/_encounter/princess/24.flac"
                show emo stranger talk onlayer front
                p "We're probably stuck down here forever, aren't we? There's no way out, and barely a way in...\n"
                show emo stranger onlayer front
            if stranger_schism_monster:
                voice "audio/voices/ch2/stranger/_encounter/princess/25a.flac"
                show monster stranger talk onlayer front
                spmid "I thought they would send something better to deal with me. If the stairs managed to chew you up, I will devour you.\n"
                show monster stranger onlayer front

            jump stranger_basement_menu


        "{i}• (Explore) ''For all I know, you're locked up down here for a reason. Do you know why you're down here?''{/i}" if stranger_menu_reason == False and stranger_schism_count != 5:
            $ stranger_menu_reason = True
            # this is where you get the sad one, if you don't already have her; otherwise you get the monster (if you don't already have her)
            if stranger_schism_count == 1:
                hide fore onlayer back
                show stranger start talk onlayer back at Position(ypos=1125)
                with dissolve
            else:
                show stranger center talk onlayer farback at Position(ypos=1125)
            if stranger_schism_first == "gentle":
                voice "audio/voices/ch2/stranger/_encounter/princess/29.flac"
                p "I don't know why I'm here, but there has to be a reason, right? You don't just lock a Princess away in a place like this without a reason. I wish I knew what it was.\n"
            if stranger_schism_first == "harsh":
                voice "audio/voices/ch2/stranger/_encounter/princess/30a.flac"
                p "Maybe it's because I'm dangerous.\n"
            if stranger_schism_first == "neutral":
                if blade_held:
                    voice "audio/voices/ch2/stranger/_encounter/princess/31.flac"
                    p "Is this a quiz? You're the one who came down here, and with a sharp, sharp knife, too.\n"
                else:
                    voice "audio/voices/ch2/stranger/_encounter/princess/32.flac"
                    p "Is this a quiz? If you're here, then surely you know why I'm here.\n"
            if stranger_schism_count == 1:
                show stranger start onlayer back at Position(ypos=1125)
            else:
                show stranger center onlayer farback at Position(ypos=1125)
            if stranger_schism_emo == False:
                # schism happens
                $ stranger_emo_set = True
                $ stranger_current_schism_comment = False
                $ stranger_schism_count += 1
                voice "audio/voices/ch2/stranger/_encounter/princess/33.flac"
                play audio "audio/one_shot/glass_1.flac"
                hide stranger onlayer back
                hide farback onlayer farback
                hide bg onlayer back
                show stranger center onlayer farback at Position(ypos=1125)
                show emo stranger talk onlayer front at Position(ypos=1125)
                with hpunch
                p "But you know, right? You have to know. You're the only other person I've ever seen, or at least the only one I can remember. Don't give me false hope. Please just end this already. One way or another, just do it.\n"
                show emo stranger onlayer front
            else:
                voice "audio/voices/ch2/stranger/_encounter/princess/33.flac"
                show emo stranger talk onlayer front
                p "But you know, right? You have to know. You're the only other person I've ever seen, or at least the only one I can remember. Don't give me false hope. Please just end this already. One way or another, just do it.\n"
                show emo stranger onlayer front
                if stranger_schism_monster == False:
                    # schism happens
                    $ stranger_monster_set = True
                    $ stranger_current_schism_comment = False
                    $ stranger_schism_count += 1
                    voice "audio/voices/ch2/stranger/_encounter/princess/34.flac"
                    play audio "audio/final/Assorted_ForcefullyBreakingGlass_2.flac"
                    hide stranger onlayer back
                    hide farback onlayer farback
                    hide bg onlayer back
                    show stranger center onlayer farback at Position(ypos=1125)
                    show monster stranger talk onlayer front at Position(ypos=1125)
                    with hpunch
                    spmid "Don't be coy. We both know why I'm locked away here. I'm a monster, and the second I get out of this place, I'm going to end the entire world.\n"
                    show monster stranger onlayer front

                else:
                    voice "audio/voices/ch2/stranger/_encounter/princess/34.flac"
                    show monster stranger talk onlayer front
                    spmid "Don't be coy. We both know why I'm locked away here. I'm a monster, and the second I get out of this place, I'm going to end the entire world.\n"
                    show monster stranger onlayer front

            jump stranger_basement_menu

        "{i}• (Explore) ''You're apparently a threat to the world. I was sent here to slay you.''{/i}" if stranger_menu_reason == False and stranger_schism_count != 5:
            $ stranger_menu_reason = True
            $ stranger_menu_threat_share = True
            # this is the one that gets you the monster
            if stranger_schism_count == 1:
                hide fore onlayer back
                show stranger start talk onlayer back at Position(ypos=1125)
                with dissolve
            else:
                show stranger center talk onlayer farback at Position(ypos=1125)
            if stranger_schism_first == "gentle":
                voice "audio/voices/ch2/stranger/_encounter/princess/35.flac"
                p "But I don't want to hurt anyone. I like the world!\nI think. You... you don't think I'm some sort of monster, do you?\n"
            elif stranger_schism_first == "harsh":
                voice "audio/voices/ch2/stranger/_encounter/princess/36.flac"
                p "And you believe that? Do you think I'm some sort of... monster?\n"
            elif stranger_schism_first == "neutral":
                voice "audio/voices/ch2/stranger/_encounter/princess/37.flac"
                p "I don't have any weapons. And I'm chained to a wall. Do I look like someone that could end the world? Do I look like a monster?\n"
            if stranger_schism_count == 1:
                show stranger start onlayer back at Position(ypos=1125)
            else:
                show stranger center onlayer farback at Position(ypos=1125)
            if stranger_schism_monster == False:
                # schism happens
                $ stranger_monster_set = True
                $ stranger_current_schism_comment = False
                $ stranger_schism_count += 1
                voice "audio/voices/ch2/stranger/_encounter/princess/38.flac"
                play audio "audio/final/Assorted_ForcefullyBreakingGlass_2.flac"
                hide stranger onlayer back
                hide farback onlayer farback
                hide bg onlayer back
                show stranger center onlayer farback at Position(ypos=1125)
                show monster stranger talk onlayer front at Position(ypos=1125)
                with hpunch
                spmid "Because I am. Everything you've heard about me is true, and I am going to lay waste to everything. Starting with you.\n"
                show monster stranger onlayer front

            else:
                voice "audio/voices/ch2/stranger/_encounter/princess/38.flac"
                show monster stranger talk onlayer front
                spmid "Because I am. Everything you've heard about me is true, and I am going to lay waste to everything. Starting with you.\n"
                show monster stranger onlayer front
                if stranger_schism_emo == False:
                    # schism happens
                    $ stranger_emo_set = True
                    $ stranger_current_schism_comment = False
                    $ stranger_schism_count += 1
                    voice "audio/voices/ch2/stranger/_encounter/princess/39.flac"
                    play audio "audio/one_shot/glass_1.flac"
                    hide stranger onlayer back
                    hide farback onlayer farback
                    hide bg onlayer back
                    show stranger center onlayer farback at Position(ypos=1125)
                    show emo stranger talk onlayer front at Position(ypos=1125)
                    with hpunch
                    p "I don't know. Maybe that's true. I probably shouldn't be given the chance anyway. If you were sent here to kill me, maybe you should just get it over with.\n"
                    show emo stranger onlayer front
                else:
                    voice "audio/voices/ch2/stranger/_encounter/princess/39.flac"
                    show emo stranger talk onlayer front
                    p "I don't know. Maybe that's true. I probably shouldn't be given the chance anyway. If you were sent here to kill me, maybe you should just get it over with.\n"
                    show emo stranger onlayer front

            jump stranger_basement_menu


        "{i}• (Explore) ''If I let you out of here, what are you going to do?''{/i}" if stranger_menu_what_do == False and stranger_schism_count != 5 and (stranger_menu_threat_share or (stranger_menu_reason and stranger_schism_monster)):
            default stranger_what_do_break = False
            default stranger_what_do_count = 0
            $ stranger_menu_what_do = True
            if stranger_schism_count == 1:
                hide fore onlayer back
                show stranger start talk onlayer back at Position(ypos=1125)
                with dissolve
            else:
                show stranger center talk onlayer farback at Position(ypos=1125)
            if stranger_schism_first == "gentle":
                voice "audio/voices/ch2/stranger/_encounter/princess/40.flac"
                p "Are you looking for the truth, or are you looking for the 'right' answer?\n"

            elif stranger_schism_first == "neutral":
                voice "audio/voices/ch2/stranger/_encounter/princess/41.flac"
                p "I don't think I can answer that question in a way you'd find meaningful.\n"

            elif stranger_schism_first == "harsh":
                voice "audio/voices/ch2/stranger/_encounter/princess/42.flac"
                p "I don't think what I'd do really matters, does it?\n"
            if stranger_schism_count == 1:
                show stranger start onlayer back at Position(ypos=1125)
            else:
                show stranger center onlayer farback at Position(ypos=1125)
            if stranger_what_do_break == False:
                if stranger_schism_harsh == False and stranger_schism_first != "harsh":
                    $ stranger_what_do_count += 1
                    $ stranger_harsh_set = True
                    $ stranger_what_do_break = True
                    $ stranger_schism_count += 1
                    $ stranger_current_schism_comment = False
                    voice "audio/voices/ch2/stranger/_encounter/princess/43.flac"
                    play audio "audio/final/Assorted_Glass Breaking_6.flac"
                    hide stranger onlayer back
                    hide farback onlayer farback
                    hide bg onlayer back
                    show stranger center onlayer farback at Position(ypos=1125)
                    show harsh stranger talk onlayer back at Position(ypos=1125)
                    with hpunch
                    p "What do you want me to say? That I'd be a good person?\n"
                    show harsh stranger onlayer back
                elif stranger_schism_neutral == False and stranger_schism_first != "neutral":
                    $ stranger_what_do_count += 1
                    $ stranger_neutral_set = True
                    $ stranger_what_do_break = True
                    $ stranger_schism_count += 1
                    $ stranger_current_schism_comment = False
                    voice "audio/voices/ch2/stranger/_encounter/princess/44.flac"
                    play audio "audio/final/Assorted_Glass Breaking_6.flac"
                    hide stranger onlayer back
                    hide farback onlayer farback
                    hide bg onlayer back
                    show stranger center onlayer farback at Position(ypos=1125)
                    show neutral stranger talk onlayer back at Position(ypos=1125)
                    with hpunch
                    p "I could tell you that I'd lead a quiet life in the woods or that I'd open an orphanage or that I'd do any other number of 'good' things that I'm sure you think you want to hear.\n"
                    show neutral stranger onlayer back
                elif stranger_schism_gentle == False and stranger_schism_first != "gentle":
                    $ stranger_what_do_count += 1
                    $ stranger_gentle_set = True
                    $ stranger_what_do_break = True
                    $ stranger_schism_count += 1
                    $ stranger_current_schism_comment = False
                    voice "audio/voices/ch2/stranger/_encounter/princess/45.flac"
                    play audio "audio/final/Assorted_Glass Breaking_6.flac"
                    hide stranger onlayer back
                    hide farback onlayer farback
                    hide bg onlayer back
                    show stranger center onlayer farback at Position(ypos=1125)
                    show gentle stranger talk onlayer back at Position(ypos=1125)
                    with hpunch
                    p "I just want to live my life.\n"
                    show gentle stranger onlayer back

            if stranger_what_do_break == False:
                if stranger_schism_neutral:
                    voice "audio/voices/ch2/stranger/_encounter/princess/44.flac"
                    show neutral stranger talk onlayer back
                    p "I could tell you that I'd lead a quiet life in the woods or that I'd open an orphanage or that I'd do any other number of 'good' things that I'm sure you think you want to hear.\n"
                    show neutral stranger onlayer back
                elif stranger_schism_harsh:
                    voice "audio/voices/ch2/stranger/_encounter/princess/43.flac"
                    show harsh stranger talk onlayer back
                    p "What do you want me to say? That I'd be a good person?\n"
                    show harsh stranger onlayer back
                elif stranger_schism_gentle:
                    show gentle stranger talk onlayer back
                    p "I just want to live my life.\n"
                    show gentle stranger onlayer back

            if stranger_schism_gentle:
                voice "audio/voices/ch2/stranger/_encounter/princess/46.flac"
                show gentle stranger talk onlayer back
                p "You either trust me or you believe that I'm dangerous. What I say won't change how you already feel about me.\n"
                show gentle stranger onlayer back
            elif stranger_schism_neutral:
                voice "audio/voices/ch2/stranger/_encounter/princess/47.flac"
                show neutral stranger talk onlayer back
                p "I'm a prisoner here, and whether or not you shoved me down here, you're practically my captor at this point. Anything I'd say is tainted by that.\n"
                show neutral stranger onlayer back
            elif stranger_schism_harsh:
                voice "audio/voices/ch2/stranger/_encounter/princess/48.flac"
                show harsh stranger talk onlayer back
                p "I'm not going to dance for you.\n"
                show harsh stranger onlayer back
            if stranger_schism_monster:
                voice "audio/voices/ch2/stranger/_encounter/princess/49.flac"
                show monster stranger talk onlayer front
                spmid "Besides, you already know what I'm going to do.\n"
                show monster stranger onlayer front
            if stranger_schism_emo:
                voice "audio/voices/ch2/stranger/_encounter/princess/50.flac"
                show emo stranger talk onlayer front
                p "If you want to put an end to me, then put an end to me.\n"
                show emo stranger onlayer front

            if stranger_schism_monster == False:
                voice "audio/voices/ch2/stranger/_encounter/hero/31.flac"
                hero "Not a single real answer...\n"
                voice "audio/voices/ch2/stranger/_encounter/contrarian/27.flac"
                contrarian "It's infuriating isn't it?\n"
            else:
                voice "audio/voices/ch2/stranger/_encounter/hero/31.flac"
                hero "Not a single real answer...\n"
                voice "audio/voices/ch2/stranger/_encounter/contrarian/28.flac"
                contrarian "At least aside from Miss Blood-and-Destruction. It's infuriating isn't it?\n"
            voice "audio/voices/ch2/stranger/_encounter/contrarian/29.flac"
            contrarian "Whose buttons are there for us to press? Whose skin is there for us to get under?\n"
            voice "audio/voices/ch2/stranger/_encounter/hero/32.flac"
            hero "Not exactly how I'd put it, but I don't disagree. There must be something we can do. Asking questions just seems to make things worse.\n"
            jump stranger_basement_menu


        "{i}• ''I'm getting you out of here.'' [[Try and free her.]\n• ''I don't know what you are, but I can't trust you. I can't trust anything here.'' [[Leave her in the basement.]\n• [[Slay the Princess.]\n{/i}" if blade_held and stranger_schism_count >= 2:
            $ stranger_floating = "slay"
            jump stranger_ending

        "{i}• ''I'm getting you out of here.'' [[Try and free her.]\n• ''I don't know what you are, but I can't trust you. I can't trust anything here.'' [[Leave her in the basement.]\n• [[Retrieve the blade.]\n{/i}" if blade_held == False and stranger_1_cabin_blade_tossed == False and stranger_schism_count >= 2:
            $ stranger_floating = "retrieve"
            jump stranger_ending

        "{i}• ''I'm getting you out of here.'' [[Try and free her.]\n• ''I don't know what you are, but I can't trust you. I can't trust anything here.'' [[Leave her in the basement.]\n• [[Regretfully think about that time you threw the blade out the window.]\n{/i}" if blade_held == False and stranger_1_cabin_blade_tossed and stranger_schism_count >= 2:
            $ stranger_floating = "mourn"
            jump stranger_ending


label stranger_ending:
    voice "audio/voices/ch2/stranger/_encounter/narrator/57.flac"
    n "Wait... that's not right.\n"
    voice "audio/voices/ch2/stranger/_encounter/contrarian/30.flac"
    contrarian "Go on.\n"
    play audio "audio/one_shot/footstep_run_dirt_short.flac"
    play sound "audio/one_shot/footsteps_stone.flac"
    if stranger_schism_count != 5:
        play audio "audio/final/Assorted_ForcefullyBreakingGlass_2.flac"
    else:
        play tertiary "audio/one_shot/footsteps_creaky.flac"
    voice "audio/voices/ch2/stranger/_encounter/narrator/58.flac"
    stop music fadeout 10.0
    hide stranger onlayer farback
    hide emo onlayer front
    hide monster onlayer front
    hide neutral onlayer back
    hide gentle onlayer back
    hide harsh onlayer back
    hide fore onlayer back
    hide farback onlayer farback
    hide bg onlayer back
    show bg stranger act begin onlayer back at Position(ypos=1125)
    show mid stranger act begin onlayer front at Position(ypos=1125)
    if blade_held:
        show fore stranger act begin onlayer inyourface at Position(ypos=1125)
    with hpunch
    n "You take a step forward. Your foot lands. But it lands... different. You experience a firm footfall, a gentle tread, a confident stride.\n"
    voice "audio/voices/ch2/stranger/_encounter/narrator/59.flac"
    n "You can feel yourself rupture. The room spins, your perception multiplying in a sickening kaleidoscope as your very self is pulled in incomprehensibly many directions.\n"
    play music "audio/_music/ch2/stranger/The Stranger End.flac" loop
    if stranger_floating == "slay":
        if stranger_other_way:
            $ default_mouse = "bloodthumb"
        else:
            $ default_mouse = "blood"
        voice "audio/voices/ch2/stranger/_encounter/narrator/60.flac"
        play audio "audio/final/Assorted_SphereBreaks_2.flac"
        hide bg stranger act onlayer back at Position(ypos=1125)
        hide mid onlayer front
        hide fore onlayer inyourface
        show bg stranger act onlayer back at Position(ypos=1125)
        show mid stranger act onlayer front at Position(ypos=1125)
        show fore stranger act onlayer inyourface at Position(ypos=1125)
        with Dissolve(1.5)
        n "All at once you charge forward, knife gleaming to slay the Princess, just as you strike at her bindings and leave her to languish alone.\n"
    else:
        $ blade_held = True
        $ default_mouse = "blood"
        play audio "audio/one_shot/knife_pickup.flac"
        voice "audio/voices/ch2/stranger/_encounter/narrator/61.flac"
        play audio "audio/final/Assorted_SphereBreaks_2.flac"
        hide bg stranger act onlayer back at Position(ypos=1125)
        hide mid onlayer front
        hide fore onlayer inyourface
        show bg stranger act onlayer back at Position(ypos=1125)
        show mid stranger act onlayer front at Position(ypos=1125)
        show fore stranger act onlayer inyourface at Position(ypos=1125)
        with Dissolve(1.5)
        n "You find the blade suddenly in your hands. All at once you use it to strike at her bindings as you remain upstairs and slay her and leave her to languish alone.\n"
    #voice "audio/voices/ch2/stranger/_encounter/hero/33.flac"
    #hero "But that doesn't make sense!\n"
    voice "audio/voices/ch2/stranger/_encounter/narrator/62b.flac"
    n "Is this what the end of the world looks like? What an unbearable mess...\n"
    #n "It's what's happening. Is this what the end of the world looks like? What an unbearable mess...\n"
    #n "I know. But it's what's happening. Is this what the end of the world looks like? What an unbearable mess...\n"
    # FAST
    voice "audio/voices/ch2/stranger/_encounter/contrarian/31.flac"
    play audio "audio/one_shot/new/STP_stranger_2.flac"
    hide bg onlayer back
    hide mid onlayer front
    hide fore onlayer inyourface
    show bg stranger collapse1 onlayer farback at Position(ypos=1125)
    show mid stranger collapse onlayer back at Position(ypos=1125)
    show fore stranger collapse onlayer front at Position(ypos=1125)
    with dissolve
    contrarian "But this— we can't—\n"
    play audio "audio/one_shot/new/STP_strangershuffle_4.flac"
    voice "audio/voices/ch2/stranger/_encounter/hero/34a.flac"
    hide bg onlayer farback
    hide mid onlayer back
    hide fore onlayer front
    show bg stranger collapse2 onlayer back at Position(ypos=1125)
    show stranger collapse2 onlayer front at Position(ypos=1125)
    with dissolve
    hero "... do you not have anything witty to say? I could use a good bit of wit right now.\n"
    voice "audio/voices/ch2/stranger/_encounter/contrarian/32.flac"
    play audio "audio/one_shot/new/STP_stranger_1.flac"
    hide bg onlayer farback
    hide mid onlayer back
    hide fore onlayer front
    show bg stranger collapse3 onlayer back at Position(ypos=1125)
    show stranger collapse3 onlayer front at Position(ypos=1125)
    with dissolve
    contrarian "No, I don't. Because this isn't fun. How are we supposed to have fun if everything is happening at the same time? It's the same as nothing happening, and nothing is excrutiating!\n"
    voice "audio/voices/ch2/stranger/_encounter/narrator/63a.flac"
    play audio "audio/final/Stranger_BodiesIntoOne_1.flac"
    hide bg onlayer back
    hide stranger onlayer front
    scene bg black
    n "Luckily for all of us, nothing, and everything, doesn't go on forever. The world, and the Princess, collapse in on themselves before it all—\n"
    voice "audio/voices/ch2/stranger/_encounter/hero/35.flac"
    $ blade_held = False
    $ default_mouse = "default"
    show bg stranger collapse3 onlayer back at Position(ypos=1125)
    show stranger collapse distraught onlayer front at Position(ypos=1125)
    with fade
    hero "... Falls apart?\n"
    voice "audio/voices/ch2/stranger/_encounter/contrarian/33.flac"
    contrarian "I think He's gone.\n" id stranger_ending_dcb6ed96
    voice "audio/voices/ch2/stranger/_encounter/hero/36.flac"
    hero "We were never going to salvage this, were we?\n"
    #voice "audio/voices/ch2/stranger/_encounter/contrarian/34.flac"
    #contrarian "What is there to salvage? Existence goes on.\n"
    stop music fadeout 10.0
    stop sound fadeout 20.0
    stop tertiary fadeout 20.0
    play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 20.0
    voice "audio/voices/ch2/stranger/_encounter/princess/51.flac"
    show stranger collapse distraught onlayer front at Position(ypos=1125)
    show quiet creep1 onlayer back at Position(ypos=1125)
    with dissolve
    sp "What happened to us? What are we? There are parts of us that are dead, and the others.... they just don't fit.\n"
    voice "audio/voices/ch2/stranger/_encounter/princess/52.flac"
    play audio "audio/one_shot/new/STP_strangershuffle_4.flac"
    show stranger collapse horror talk onlayer front at Position(ypos=1125)
    show quiet creep2 onlayer back at Position(ypos=1125)
    with dissolve
    sp "We can feel them moving around in spaces they don't belong. It's all so uncomfortable.\n"
    voice "audio/voices/ch2/stranger/_encounter/princess/53.flac"
    play audio "audio/one_shot/new/STP_strangershuffle_5.flac"
    show stranger collapse sad talk onlayer front at Position(ypos=1125)
    show quiet creep3 onlayer back at Position(ypos=1125)
    with dissolve
    sp "Did you do this? Did we do this? Can... can you pull us back apart? Can you fix us?\n"
    show stranger collapse sad onlayer front at Position(ypos=1125)
    voice "audio/voices/ch2/stranger/_encounter/contrarian/35.flac"
    contrarian "We should help her. I think... we did this.\n"
    voice "audio/voices/ch2/stranger/_encounter/hero/37.flac"
    hero "How surprisingly sincere.\n"
    voice "audio/voices/ch2/stranger/_encounter/contrarian/36a.flac"
    contrarian "I didn't actually think our actions had consequences.\n"
    voice "audio/voices/ch2/stranger/_encounter/hero/38.flac"
    hero "It's a little late for regret, isn't it?\n"
    $ gallery_stranger.unlock_item(6)
    $ gallery_stranger.unlock_item(7)
    $ gallery_stranger.unlock_item(8)
    $ gallery_stranger.unlock_item(9)
    $ renpy.save_persistent()
    voice "audio/voices/ch2/stranger/_encounter/princess/54.flac"
    show stranger collapse sad talk onlayer front at Position(ypos=1125)
    with dissolve
    sp "Please?\n"
    show stranger collapse sad onlayer front at Position(ypos=1125)
    menu:
        extend ""

        "{i}• ''It's going to be okay...''{/i}":
            $ fake_variable = False

        "{i}• ''I'll do my best.''{/i}":
            $ fake_variable = False

        "{i}• ''I don't think you're supposed to be fixed.''{/i}":
            $ fake_variable = False

        "{i}• ''No.''{/i}":
            $ fake_variable = False

        "{i}• ''You just destroyed everything. I'm not going to fix you.''{/i}":
            $ fake_variable = False

        "{i}• [[Say nothing.]{/i}":
            $ achievement.grant("ACH_STRANGER_FINISH")
            play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
            show arms stranger1 onlayer back at Position(ypos=1125)
            with Dissolve(1.0)
            $ renpy.pause(0.125)
            show arms stranger2 onlayer back at Position(ypos=1125)
            with Dissolve(0.75)
            $ renpy.pause(0.125)
            hide stranger onlayer front
            show arms stranger3 onlayer back at Position(ypos=1125)
            with Dissolve(0.5)
            $ renpy.pause(0.125)
            show arms stranger4 onlayer back at Position(ypos=1125)
            with Dissolve(0.25)
            $ renpy.pause(0.1025)
            hide arms onlayer back
            with dissolve
            $ renpy.pause(0.125)
            $ blade_held = False
            $ default_mouse = "default"
            hide stars onlayer farback
            hide bg onlayer back
            hide quiet onlayer back
            show farback quiet onlayer farback at Position(ypos=1125)
            with Dissolve(4.0)
            show mirror quiet distant onlayer back at Position(ypos=1125)
            if loops_finished != 0:
                truth "But you'll never know if she hears your silence. She's gone. Memory returns.\n"
            else:
                truth "But you don't know if she had the chance to hear your silence. She's gone, replaced with something else.\n"
            jump stranger_end_say_nothing_join

    play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
    show arms stranger1 onlayer back at Position(ypos=1125)
    with Dissolve(1.0)
    $ renpy.pause(0.125)
    show arms stranger2 onlayer back at Position(ypos=1125)
    with Dissolve(0.75)
    $ renpy.pause(0.125)
    hide stranger onlayer front
    show arms stranger3 onlayer back at Position(ypos=1125)
    with Dissolve(0.5)
    $ renpy.pause(0.125)
    show arms stranger4 onlayer back at Position(ypos=1125)
    with dissolve
    $ renpy.pause(0.1025)
    hide arms onlayer back
    with dissolve
    $ renpy.pause(0.125)
    $ blade_held = False
    $ default_mouse = "default"
    hide stars onlayer farback
    hide bg onlayer back
    hide quiet onlayer back
    show farback quiet onlayer farback at Position(ypos=1125)
    with Dissolve(4.0)
    show mirror quiet distant onlayer back at Position(ypos=1125)
    $ achievement.grant("ACH_STRANGER_FINISH")
    if loops_finished != 0:
        truth "But you'll never know if she hears your reply. She's gone. Memory returns.\n"
    else:
        truth "But you don't know if she had the chance to hear your reply. She's gone, replaced with something else.\n"

label stranger_end_say_nothing_join:
    $ current_princess = "stranger"
    jump mirror_start
return
