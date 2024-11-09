label razor_2_nexus:

    # added voices from Razor 1:
    # took the blade — hunted
    # went down unarmed — contrarian

    # attacked her — stubborn
    # went upstairs — paranoid
    # came closer OR was attacked by her — broken

    default razor_loop = 0
    default razor_stubborn_intro = False
    default razor_hunted_intro = False
    default razor_smitten_intro = False
    default razor_paranoid_intro = False
    default razor_skeptic_intro = False
    default razor_cold_intro = False
    default razor_contrarian_intro = False
    default razor_broken_intro = False
    default razor_opportunist_intro = False
    default razor_2_count = 0
    if trait_paranoid:
        $ razor_paranoid_intro = True
    if trait_broken:
        $ razor_broken_intro = True

label razor_2_armed_start:
    play music "audio/_music/ch2/razor/The Razor Heightened.flac" loop
    voice "audio/voices/ch3/razor/nexus/narrator/1.flac"
    scene bg basement razor2 onlayer back at Position(ypos=1125)
    show razor2 neutral onlayer back at Position(ypos=1125)
    with fade
    n "Your body tumbles onto the basement floor, and the form of the Princess comes into view, standing at a distance. She gives you a wry smile.\n"
    voice "audio/voices/ch3/razor/nexus/princess/1.flac"
    show razor2 neutral talk onlayer back
    with dissolve
    sp "Hi! It looks like you don't have a way out, so I'm not going to play dumb anymore.\n"
    voice "audio/voices/ch3/razor/nexus/princess/2.flac"
    show razor2 wink talk onlayer back
    with dissolve
    sp "But don't worry about how bad you did last time. That's part of the fun!\n"
    show razor2 neutral onlayer back
    with dissolve
    if trait_stubborn:
        voice "audio/voices/ch3/razor/nexus/stubborn/1.flac"
        stubborn "She's got another thing coming if she thinks we're going down easy again.\n"
        voice "audio/voices/ch3/razor/nexus/hunted/1.flac"
        hunted "Pride makes us dead. The only thing that matters is survival.\n"
    if trait_broken:
        voice "audio/voices/ch3/razor/nexus/broken/1.flac"
        broken "Fun for her, maybe. I didn't like dying all over again.\n"
    if trait_paranoid:
        voice "audio/voices/ch3/razor/nexus/paranoid/1.flac"
        paranoid "She's toying with us. She's acting like she already knows she's won.\n"
    if trait_stubborn == False:
        voice "audio/voices/ch3/razor/nexus/hunted/2.flac"
        hunted "Thinking about dying makes us as good as dead. The only thing that matters is survival.\n"
    voice "audio/voices/ch3/razor/nexus/cheated/1.flac"
    cheated "Actually, does survival matter? We've died twice and nothing bad has come of it. We just need to find a way to win once.\n"
    voice "audio/voices/ch3/razor/nexus/hero/1.flac"
    hero "Nothing bad has come of it {i}yet{/i}.\n"
    voice "audio/voices/ch3/razor/nexus/narrator/2.flac"
    n "Plenty bad has come of it! You've left at least one entire world to ruin. The people there mattered.\n"
    voice "audio/voices/ch3/razor/nexus/hunted/3.flac"
    hunted "The past isn't real. There's only here and now.\n"
    voice "audio/voices/ch3/razor/nexus/narrator/3.flac"
    play audio "audio/final/Razor_FleshExplosion_1.flac"
    play secondary "audio/final/Razor_ImpaleSwordBody_5.flac"
    show razor2 reveal anim onlayer back
    with dissolve
    n "Your internal bickering is cut short by the wet sound of slicing meat. From the Princess' arms erupt twin blades, glistening with her blood, the empty flesh of her arms flopping at her elbows like torn sleeves. The chain clatters to the floor.\n"
    voice "audio/voices/ch3/razor/nexus/narrator/4.flac"
    n "She's loose, and she is coming for you.\n"
    voice "audio/voices/ch3/razor/nexus/princess/3.flac"
    play audio "audio/final/Prisoner_HeavyChains_2.flac"
    show bg basement razor2 postreveal onlayer back at Position(ypos=1125)
    show razor2 r talk onlayer back
    with dissolve
    sp "You're going to make me walk over to you, aren't you?\n"
    voice "audio/voices/ch3/razor/nexus/cheated/2.flac"
    play audio "audio/final/__metal_step.flac"
    show razor2 r step onlayer back
    with dissolve
    cheated "Shit, she's coming for us, and I'm out of ideas.\n"
    label razor_2_armed_beat_1:
        menu:

            extend ""

            "{i}• We're going to fight her again, and we're going to have a stiff upper lip about it. She can't hurt us if we don't let ourselves feel it.{/i}" if trait_cold == False and trait_stubborn:
                jump razor_2_fight_join

            "{i}• We're fighting her, obviously.{/i}" if trait_stubborn == False:
                voice "audio/voices/ch3/razor/nexus/hero/2.flac"
                hero "I guess we have a weapon.\n"
                voice "audio/voices/ch3/razor/nexus/cheated/3a.flac"
                cheated "Okay. I'm in. Let's do this.\n"
                #cheated "And we didn't actually try fighting her last time. Okay. I'm in. Let's do this.\n"
                if trait_paranoid:
                    voice "audio/voices/ch3/razor/nexus/paranoid/2.flac"
                    paranoid "This can't be the right answer. It's too easy!\n"
                else:
                    voice "audio/voices/ch3/razor/nexus/broken/2.flac"
                    broken "She's going to kill us.\n"
                voice "audio/voices/ch3/razor/nexus/cheated/4.flac"
                cheated "Well, if we die, we die, right? Then we can try again next time.\n"
                if trait_paranoid:
                    voice "audio/voices/ch3/razor/nexus/paranoid/3.flac"
                    paranoid "Are you sure?\n"
                else:
                    voice "audio/voices/ch3/razor/nexus/broken/3.flac"
                    broken "Bad idea. But it's not like any of you listen to me.\n"
                menu:
                    extend ""

                    "{i}• Cheer up! Maybe we'll win!{/i}":
                        label razor_2_knife_cheated_join:
                            voice "audio/voices/ch3/razor/nexus/cheated/5.flac"
                            cheated "Yeah! No more moping, we're gonna fight her, and we're gonna win!\n"
                            #voice "audio/voices/ch3/razor/nexus/hero/3.flac"
                            #hero "Let's do this!\n"
                            voice "audio/voices/ch3/razor/nexus/narrator/5.flac"
                            play audio "audio/final/__metal_run.flac"
                            show bg basement razor2 postreveal onlayer back at big_zoom
                            show razor2 r step onlayer back at big_zoom_instant
                            show speedlines onlayer inyourface at Position(ypos=1125)
                            with dissolve
                            n "Blade poised to strike, you charge the Princess.\n"
                            voice "audio/voices/ch3/razor/nexus/princess/4.flac"
                            show razor2 r happy talk onlayer back at big_zoom_instant
                            with dissolve
                            sp "Oh, so you do want a fight, huh? Okay! Yes! I love this! Try to stab me! Try to stab me and see what happens!\n"
                            voice "audio/voices/ch3/razor/nexus/hero/4.flac"
                            #play audio "audio/final/__metal_run.flac"
                            #show bg razor2 charge onlayer back at Position(ypos=1125)
                            #show cg razor2 player charge knife talk onlayer front at Position(ypos=1125)
                            #with dissolve
                            hero "Here goes... we can make this work.\n"
                            voice "audio/voices/ch3/razor/nexus/hunted/4.flac"
                            hunted "Yes. If we pay attention, we won't die.\n"
                            if trait_broken:
                                voice "audio/voices/ch3/razor/nexus/broken/4.flac"
                                broken "And what if we don't?\n"
                            if trait_paranoid:
                                voice "audio/voices/ch3/razor/nexus/paranoid/4.flac"
                                paranoid "Yeah. Mind over matter, mind over matter, mind over matter. What if we can't do this?\n"
                            voice "audio/voices/ch3/razor/nexus/narrator/6.flac"
                            $ default_mouse = "blood"
                            play secondary "audio/final/Razor_SwordCutArm_3.flac"
                            queue secondary "audio/one_shot/knife_slash.flac"
                            queue secondary "audio/final/Razor_SwordHitDrag_2.flac"
                            hide speedlines onlayer inyourface
                            hide cg onlayer front
                            hide bg onlayer back
                            hide razor2 onlayer back
                            show bg razor2 dodged onlayer farback at Position(ypos=1125)
                            show panel1 razor2 knife onlayer front at Position(ypos=1125)
                            show panel2 razor2 knife final onlayer back at Position(ypos=1125)
                            show panel3 razor2 knife final onlayer front at Position(ypos=1125)
                            with Dissolve(1.0)
                            n "You and the Princess exchange a flurry of blows, and you manage to narrowly avoid death several times.\n"
                            voice "audio/voices/ch3/razor/nexus/narrator/6a.flac"
                            play audio "audio/final/Razor_SwordHitDrag_5.flac"
                            show panel0 razor2 knife fight onlayer inyourface at Position(ypos=1125)
                            n "Until finally you see it. An opening.\n"
                            voice "audio/voices/ch3/razor/nexus/hunted/5.flac"
                            hunted "It's a trick. Don't take it.\n"
                            voice "audio/voices/ch3/razor/nexus/cheated/6.flac"
                            cheated "No, screw that. Ours! Ours! I called it, it's ours we're taking it!\n"
                            voice "audio/voices/ch3/razor/nexus/narrator/7.flac"
                            play audio "audio/final/Razor_ImpaleSwordBody_6.flac"
                            hide panel1 onlayer front
                            hide panel2 onlayer back
                            hide panel3 onlayer front
                            hide panel0 onlayer inyourface
                            hide bg onlayer farback
                            scene bg black
                            n "And you do take it. But as you close in, yet another blade erupts from the Princess. You have no time to react before you feel it sliding through your ribs.\n"
                            voice "audio/voices/ch3/razor/nexus/hunted/6.flac"
                            hunted "A trick. I knew it. I told you to be careful of tricks.\n"
                            voice "audio/voices/ch3/razor/nexus/cheated/7.flac"
                            cheated "What?! From where?\n"
                            voice "audio/voices/ch3/razor/nexus/narrator/8.flac"
                            scene cg razor2 knife stabbed knee onlayer back at Position(ypos=1125)
                            with dissolve
                            n "From her knee, apparently.\n"
                            voice "audio/voices/ch3/razor/nexus/princess/5.flac"
                            hide cg onlayer back
                            show bg razor2 close onlayer back at Position(ypos=1125)
                            show razor2 stabbed wounds hehe onlayer front at Position(ypos=1125)
                            with dissolve
                            sp "Hehehehe. Too slow!\n"
                            voice "audio/voices/ch3/razor/nexus/cheated/8.flac"
                            cheated "Oh that's bullshit! Bloody unfair!\n"
                            voice "audio/voices/ch3/razor/nexus/narrator/9.flac"
                            play audio "audio/final/Razor_ImpaleSwordBody_1.flac"
                            stop music
                            hide bg onlayer back
                            hide razor2 onlayer front
                            scene bg black
                            n "Unfortunately for the sake of the world, fair doesn't factor into this. Another of her blades comes slicing up to finish the job. She skewers you.\n"
                            voice "audio/voices/ch3/razor/nexus/hero/5.flac"
                            hero "Ow.\n"
                            voice "audio/voices/ch3/razor/nexus/princess/6.flac"
                            scene bg razor2 close onlayer back at Position(ypos=1125)
                            show razor2 close enthusiastic talk onlayer front at Position(ypos=1125)
                            with fade
                            sp "Ribbons! I'm going to make you ribbons! This is so much fun and I want to celebrate.\n"
                            voice "audio/voices/ch3/razor/nexus/stubborn/2.flac"
                            $ trait_stubborn = True
                            show razor2 close enthusiastic onlayer front
                            with dissolve
                            stubborn "It would have worked if we just stabbed her harder.\n"

                    "{i}• See, but that's the brilliance of it all. She doesn't think we have it in us to win.{/i}":
                        jump razor_2_knife_cheated_join

                    "{i}• I'm done explaining myself. I'm going to stab her now.{/i}":
                        jump razor_2_knife_cheated_join

            "{i}• We're going to appeal to her authority. Puff her up a bit. There's no reason we can't talk this out.{/i}" if trait_opportunist == False:
                voice "audio/voices/ch3/razor/nexus/hunted/7.flac"
                hunted "She isn't one to talk and we shouldn't be either.\n"
                if trait_broken:
                    voice "audio/voices/ch3/razor/nexus/broken/5.flac"
                    broken "He's right. I don't think we can talk this out. I think she wants to kill us.\n"
                if trait_paranoid:
                    voice "audio/voices/ch3/razor/nexus/paranoid/5.flac"
                    paranoid "Exactly. She wants us dead, you know!\n"
                if trait_stubborn:
                    voice "audio/voices/ch3/razor/nexus/stubborn/3.flac"
                    stubborn "I agree. Talking is boring. We should just get back to fighting her!\n"
                if trait_stubborn:
                    voice "audio/voices/ch3/razor/nexus/cheated/9.flac"
                    cheated "That's not helpful. We already tried that one, didn't we?\n"
                else:
                    voice "audio/voices/ch3/razor/nexus/cheated/10.flac"
                    cheated "Exactly. I think she established that at some point between stabbing us to death and directly telling us, just now, that she was going to kill us.\n"
                voice "audio/voices/ch3/razor/nexus/hero/6.flac"
                hero "You were the one who asked for ideas.\n"
                voice "audio/voices/ch3/razor/nexus/cheated/11.flac"
                cheated "Fine. Talk our way out of this! Maybe that's the answer.\n"
                menu:
                    extend ""

                    "{i}• ''You know, I'm a big fan of winners, and you've got 'winner' written all over you. How about we stop fighting and team up? I'll even let you be in charge!''{/i}":
                        jump razor_knife_opportunist_join

                    "{i}• ''Look, both of us are stuck here against our will. What if we joined forces?''{/i}":
                        label razor_knife_opportunist_join:
                            voice "audio/voices/ch3/razor/nexus/narrator/10.flac"
                            show razor2 r chin offer onlayer back
                            with dissolve
                            n "Oh for the love of... {i}sigh{/i}. The Princess stops for a moment, mulling over your deranged proposition.\n"
                            voice "audio/voices/ch3/razor/nexus/princess/7.flac"
                            show razor2 r chin offer talk onlayer back
                            with dissolve
                            sp "Nah! Not interested. And don't take it the wrong way! I think you're neat. But I'm having way too much fun to stop.\n"

                    "{i}• ''Has anyone ever told you how good you are at stabbing things?''{/i}":
                        voice "audio/voices/ch3/razor/nexus/princess/8.flac"
                        show razor2 r proud talk onlayer back
                        with dissolve
                        sp "Nope! But I don't need anyone to tell me that. I know I'm good at what I do! The best, I think.\n"
                        voice "audio/voices/ch3/razor/nexus/narrator/11.flac"
                        show razor2 r mull onlayer back
                        with dissolve
                        n "The Princess pauses for a moment to further ponder your ill-placed compliment.\n"
                        voice "audio/voices/ch3/razor/nexus/princess/9.flac"
                        show razor2 r impatient talk onlayer back
                        with dissolve
                        sp "Hey, what gives? Are you trying to get on my good side? You're not bored of me stabbing you, are you?\n"
                        show razor2 r impatient onlayer back
                        with dissolve
                        menu:
                            extend ""

                            "{i}• ''Yes! Yes, I am trying to get on your good side. Did it work?''{/i}":
                                voice "audio/voices/ch3/razor/nexus/princess/10.flac"
                                show razor2 r happy talk onlayer back
                                with dissolve
                                sp "You're {i}already{/i} on my good side!\n"

                            "{i}• ''Yes! Yes, I am bored of you stabbing me. Can you stop stabbing me now?''{/i}":
                                $ fake_variable = False
                                #voice "audio/voices/ch3/razor/nexus/princess/10.flac"
                                #show razor2 r happy talk onlayer back
                                #with dissolve
                                #sp "You're {i}already{/i} on my good side!\n"

                            "{i}• ''Psht. What? Me? Fluffing you up? I'm just stating facts.''{/i}":
                                voice "audio/voices/ch3/razor/nexus/princess/11.flac"
                                show razor2 r happy talk onlayer back
                                with dissolve
                                sp "And they're good facts! Great facts! And for what it's worth, you're already on my good side!\n"

                            "{i}• [[Say nothing.]{/i}":
                                voice "audio/voices/ch3/razor/nexus/princess/12.flac"
                                show razor2 r happy talk onlayer back
                                with dissolve
                                sp "Well, for what it's worth, you're already on my good side!\n"

                        voice "audio/voices/ch3/razor/nexus/princess/13.flac"
                        show razor2 r proud talk onlayer back
                        with dissolve
                        sp "But that doesn't mean I'm going to not stab you. I'm having fun! Why would I stop?\n"

                voice "audio/voices/ch3/razor/nexus/hunted/8.flac"
                show razor2 r step onlayer back
                with dissolve
                hunted "We should coil ourselves. She's about to pounce.\n"
                if trait_broken:
                    voice "audio/voices/ch3/razor/nexus/broken/6.flac"
                    broken "We're screwed. Again. I'll see you all when we die.\n"
                if trait_paranoid:
                    voice "audio/voices/ch3/razor/nexus/paranoid/6.flac"
                    paranoid "I hate this. Every choice we make is wrong.\n"
                if trait_stubborn:
                    voice "audio/voices/ch3/razor/nexus/stubborn/4.flac"
                    stubborn "Just get ready to fight back.\n"
                # FAST
                voice "audio/voices/ch3/razor/nexus/narrator/12a.flac"
                play audio "audio/final/__metal_run.flac"
                show razor2 r charge onlayer back
                with dissolve
                n "But before you can finish another thought, the Princess closes the distance and—\n{w=3.45}{nw}"
                show screen disableclick(0.5)
                voice "audio/voices/ch3/razor/nexus/hunted/9.flac"
                hunted "Dodge. Now!\n"
                voice "audio/voices/ch3/razor/nexus/narrator/13.flac"
                play audio "audio/final/Razor_SwordSwish_10.flac"
                hide razor2 onlayer back
                hide cg onlayer back
                show cg razor2 dodged onlayer back at Position(ypos=1125)
                with dissolve
                n "Fails to hit you.\n"
                if trait_stubborn:
                    voice "audio/voices/ch3/razor/nexus/stubborn/5.flac"
                    stubborn "Haha, yes!\n"
                voice "audio/voices/ch3/razor/nexus/princess/14.flac"
                show cg razor2 dodged talk onlayer back at Position(ypos=1125)
                with dissolve
                sp "Oooh, you're a fast one! That's fun! But I think I can get even faster.\n"
                show cg razor2 dodged smirk onlayer back at Position(ypos=1125)
                with dissolve
                if trait_paranoid:
                    voice "audio/voices/ch3/razor/nexus/paranoid/7.flac"
                    paranoid "I don't like the way she said that.\n"
                if trait_broken:
                    voice "audio/voices/ch3/razor/nexus/broken/7.flac"
                    broken "I'm going to be quiet for a bit now. Let me know when we die again.\n"
                if trait_stubborn:
                    voice "audio/voices/ch3/razor/nexus/stubborn/6.flac"
                    stubborn "Now hit her back!\n"
                    voice "audio/voices/ch3/razor/nexus/narrator/14.flac"
                    hide bg onlayer back
                    hide cg onlayer back
                    play secondary "audio/final/Razor_SwordCutArm_3.flac"
                    queue secondary "audio/one_shot/knife_slash.flac"
                    queue secondary "audio/final/Razor_SwordHitDrag_2.flac"
                    $ default_mouse = "blood"
                    hide speedlines onlayer inyourface
                    hide cg onlayer front
                    hide bg onlayer back
                    hide razor2 onlayer back
                    show bg razor2 dodged onlayer farback at Position(ypos=1125)
                    show panel1 razor2 knife onlayer front at Position(ypos=1125)
                    show panel2 razor2 knife final onlayer back at Position(ypos=1125)
                    show panel3 razor2 knife final onlayer front at Position(ypos=1125)
                    with Dissolve(1.0)
                    n "You dodge and parry and strike and are struck, her nicking your flesh and you nicking her skin to reveal shining metal below. But eventually you slip up. You lose the pattern, just for a moment.\n"
                    voice "audio/voices/ch3/razor/nexus/narrator/15.flac"
                    play audio "audio/final/Razor_ImpaleSwordBody_6.flac"
                    stop music
                    hide panel1 onlayer front
                    hide panel2 onlayer back
                    hide panel3 onlayer front
                    hide panel0 onlayer inyourface
                    hide bg onlayer farback
                    scene bg black
                    n "A blade flashes through the air, and she skewers you.\n"
                else:
                    voice "audio/voices/ch3/razor/nexus/narrator/16.flac"
                    play audio "audio/final/_razor2_combat.flac"
                    hide speedlines onlayer inyourface
                    hide cg onlayer front
                    hide cg onlayer back
                    hide bg onlayer back
                    hide razor2 onlayer back
                    show bg razor2 dodged onlayer farback at Position(ypos=1125)
                    show panel1 razor2 dodged onlayer back at Position(ypos=1125)
                    show panel2 razor2 dodged anim onlayer front at Position(ypos=1125)
                    show panel3 razor2 dodged anim onlayer inyourface at Position(ypos=1125)
                    with Dissolve(1.0)
                    n "You dodge and parry and dodge and parry in an endless repeating pattern, but you can only keep it up so long before making a mistake. The pattern breaks for just long enough.\n"
                    voice "audio/voices/ch3/razor/nexus/narrator/17.flac"
                    play audio "audio/final/Razor_ImpaleSwordBody_6.flac"
                    stop music
                    hide panel1 onlayer back
                    hide panel2 onlayer front
                    hide panel3 onlayer inyourface
                    hide bg onlayer farback
                    scene bg black
                    n "She skewers you.\n"
                voice "audio/voices/ch3/razor/nexus/hero/5.flac"
                hero "Ow.\n"
                voice "audio/voices/ch3/razor/nexus/opportunist/1a.flac"
                $ trait_opportunist = True
                scene bg razor2 close onlayer back at Position(ypos=1125)
                show razor2 close enthusiastic onlayer front at Position(ypos=1125)
                with fade
                opportunist "Wow, she is absolutely uncompromising, isn't she? I know it seems weird, but if anything this makes me want her to like us even more.\n"

            "{i}• We're going to unconditionally surrender.{/i}" if trait_broken == False:
                if trait_paranoid:
                    voice "audio/voices/ch3/razor/nexus/paranoid/8.flac"
                    paranoid "Oh. A bit of reverse psychology. I like it!\n"
                else:
                    voice "audio/voices/ch3/razor/nexus/stubborn/7.flac"
                    stubborn "That's pathetic.\n"
                voice "audio/voices/ch3/razor/nexus/hunted/10.flac"
                hunted "Dying is bad, and if you do this, we die.\n"
                voice "audio/voices/ch3/razor/nexus/hero/7.flac"
                hero "How does unconditionally surrendering work for us, anyway? Does it have to be unanimous?\n"
                voice "audio/voices/ch3/razor/nexus/narrator/18.flac"
                n "{i}Sigh{/i}. Apparently not.\n"
                voice "audio/voices/ch3/razor/nexus/cheated/12.flac"
                cheated "Hey now, let's see how it goes. It could work, it's worth a shot.\n"
                menu:
                    extend ""

                    "{i}• ''I give up. I'll do anything, just please don't stab me!''{/i}":
                        label razor_knife_surrender:
                            voice "audio/voices/ch3/razor/nexus/narrator/19.flac"
                            $ blade_held = False
                            $ default_mouse = "default"
                            play audio "audio/one_shot/knife_bounce_several.flac"
                            n "You throw your hands in the air and drop your blade.\n"
                            voice "audio/voices/ch3/razor/nexus/princess/15.flac"
                            show razor2 r finger wag talk anim onlayer back
                            with dissolve
                            sp "You can't surrender! Don't you know it takes two to stop a fight?\n"

                    "{i}• [[Silently throw your hands in the air.]{/i}":
                        jump razor_knife_surrender

                voice "audio/voices/ch3/razor/nexus/cheated/13.flac"
                cheated "Ah, shit.\n"
                # FAST
                voice "audio/voices/ch3/razor/nexus/narrator/20.flac"
                play audio "audio/final/__metal_run.flac"
                show razor2 r charge onlayer back
                with dissolve
                n "Before you can do anything else, she charges you and—\n{w=2.54}{nw}"
                show screen disableclick(0.5)
                voice "audio/voices/ch3/razor/nexus/hunted/11.flac"
                hunted "Dodge! We dodge!\n"
                voice "audio/voices/ch3/razor/nexus/narrator/21.flac"
                play audio "audio/final/Razor_SwordSwish_10.flac"
                hide razor2 onlayer back
                show cg razor2 dodged onlayer back at Position(ypos=1125)
                with dissolve
                n "Huh. Okay. You dodge.\n"
                voice "audio/voices/ch3/razor/nexus/princess/16.flac"
                show cg razor2 dodged talk onlayer back at Position(ypos=1125)
                with dissolve
                sp "Aw. I thought you were surrendering.\n"
                voice "audio/voices/ch3/razor/nexus/narrator/22.flac"
                play audio "audio/final/Razor_ImpaleSwordBody_6.flac"
                stop music
                hide bg onlayer back
                hide cg onlayer back
                hide razor2 onlayer back
                scene bg black
                n "And then she skewers you.\n"
                voice "audio/voices/ch3/razor/nexus/hero/5.flac"
                hero "Ow.\n"
                voice "audio/voices/ch3/razor/nexus/cheated/14.flac"
                scene bg razor2 close onlayer back at Position(ypos=1125)
                show razor2 close enthusiastic onlayer front at Position(ypos=1125)
                with fade
                $ blade_held = True
                $ default_mouse = "blade"
                cheated "Huh. That's weird. The blade's back in our hand.\n"
                $ trait_broken = True
                voice "audio/voices/ch3/razor/nexus/broken/8.flac"
                broken "Can't even surrender right.\n"

            "{i}• Oh, that's easy. I'm going to try flirting with her.{/i}" if trait_smitten == False:
                voice "audio/voices/ch3/razor/nexus/narrator/23.flac"
                n "Now I've tolerated quite a bit from you, but this is a bridge too far. Please don't try romancing the Princess. She wants to kill you! She's going to end the world if you don't stop her.\n"
                voice "audio/voices/ch3/razor/nexus/hero/8.flac"
                hero "Yeah... do we have to flirt with the murderous monster?\n"
                voice "audio/voices/ch3/razor/nexus/hunted/12a.flac"
                hunted "I'd rather not.\n"
                if trait_broken:
                    voice "audio/voices/ch3/razor/nexus/broken/9.flac"
                    broken "It's not like she wants us, anyway.\n"
                elif trait_paranoid:
                    voice "audio/voices/ch3/razor/nexus/paranoid/9.flac"
                    paranoid "Maybe it'll work! Maybe it'll throw her off. I know I'd be thrown off if she started flirting with us.\n"
                if trait_stubborn:
                    voice "audio/voices/ch3/razor/nexus/stubborn/8.flac"
                    stubborn "I'm into it.\n"
                    voice "audio/voices/ch3/razor/nexus/cheated/15.flac"
                    cheated "I can't say I mind, either. If it weren't for all the cheating, I'd say she's pretty cute.\n"
                    voice "audio/voices/ch3/razor/nexus/stubborn/9.flac"
                    stubborn "Can we flirt by fighting her, though?\n"
                else:
                    voice "audio/voices/ch3/razor/nexus/cheated/16.flac"
                    cheated "I'm fine with it. Let's see where this goes.\n"
                menu:
                    extend ""

                    "{i}• ''I know you want to kill me, but has anyone ever told you how gorgeous you are?''{/i}":
                        voice "audio/voices/ch3/razor/nexus/narrator/24.flac"
                        show razor2 r blush onlayer back
                        with dissolve
                        n "A rosy blush flushes in the Princess' cheeks, and a wide grin cuts across her face.\n"
                        voice "audio/voices/ch3/razor/nexus/princess/17.flac"
                        show razor2 r blush talk onlayer back
                        with dissolve
                        sp "You're the only person I know, so that's a first! You're sweet! I like you! You're also gorgeous!\n"
                        voice "audio/voices/ch3/razor/nexus/cheated/17.flac"
                        show razor2 r blush onlayer back
                        with dissolve
                        cheated "I'll be damned. This is actually going to work, isn't it?\n"
                        voice "audio/voices/ch3/razor/nexus/princess/18.flac"
                        show razor2 r blush serious talk onlayer back
                        with dissolve
                        sp "Still gonna kill you though.\n"

                    "{i}• ''I just feel like I really get you. I like you. Romantically, even. Maybe we can hash this out over a date.''{/i}":
                        voice "audio/voices/ch3/razor/nexus/narrator/24.flac"
                        show razor2 r blush onlayer back
                        with dissolve
                        n "A rosy blush flushes in the Princess' cheeks, and a wide grin cuts across her face.\n"
                        voice "audio/voices/ch3/razor/nexus/princess/19.flac"
                        show razor2 r blush talk onlayer back
                        with dissolve
                        sp "You're sweet! I like you too! You're probably my favorite person other than me.\n"
                        voice "audio/voices/ch3/razor/nexus/cheated/17.flac"
                        show razor2 r blush onlayer back
                        with dissolve
                        cheated "I'll be damned. This is actually going to work, isn't it?\n"
                        voice "audio/voices/ch3/razor/nexus/princess/18.flac"
                        show razor2 r blush serious talk onlayer back
                        with dissolve
                        sp "Still gonna kill you though.\n"

                    "{i}• ''How about you buy me dinner before impaling me to death?''{/i}":
                        voice "audio/voices/ch3/razor/nexus/narrator/24.flac"
                        show razor2 r blush onlayer back
                        with dissolve
                        n "A rosy blush flushes in the Princess' cheeks, and a wide grin cuts across her face.\n"
                        voice "audio/voices/ch3/razor/nexus/princess/20.flac"
                        show razor2 r blush talk onlayer back
                        with dissolve
                        sp "Oh? Is that how it is? Yeah okay I feel that. I like you too.\n"
                        voice "audio/voices/ch3/razor/nexus/cheated/17.flac"
                        show razor2 r blush onlayer back
                        with dissolve
                        cheated "I'll be damned. This is actually going to work, isn't it?\n"
                        voice "audio/voices/ch3/razor/nexus/princess/21.flac"
                        show razor2 r blush serious talk onlayer back
                        with dissolve
                        sp "But why mess around with appetizers when the main course is right here?\n"

                    "{i}• [[Give her {b}The Look{/b}.]{/i}":
                        voice "audio/voices/ch3/razor/nexus/hero/9.flac"
                        hero "{i}The Look{/i}?\n"
                        voice "audio/voices/ch3/razor/nexus/hunted/13.flac"
                        hunted "The Look. We've all used it.\n"
                        voice "audio/voices/ch3/razor/nexus/cheated/18.flac"
                        cheated "Yeah, do you not know about The Look?\n"
                        if trait_broken:
                            voice "audio/voices/ch3/razor/nexus/broken/10.flac"
                            broken "Even I know about The Look.\n"
                        elif trait_paranoid:
                            voice "audio/voices/ch3/razor/nexus/paranoid/10.flac"
                            paranoid "Are you sure we want to use The Look so early? It's supposed to be saved for emergencies\n"
                        else:
                            voice "audio/voices/ch3/razor/nexus/stubborn/10.flac"
                            stubborn "The Look, eh? So we're getting serious about this.\n"
                        voice "audio/voices/ch3/razor/nexus/narrator/25.flac"
                        n "{i}Sigh{/i}. You flash the Princess {i}The Look{/i}.\n"
                        voice "audio/voices/ch3/razor/nexus/narrator/26.flac"
                        show razor2 r blush onlayer back
                        with dissolve
                        n "... and a rosy blush rushes to the Princess' cheeks as she breaks into a wide grin. Unbelievable.\n"
                        voice "audio/voices/ch3/razor/nexus/princess/22.flac"
                        show razor2 r blush talk onlayer back
                        with dissolve
                        sp "Oh? Is that how it is? Yeah okay I feel that. I like you too. Neat!\n"
                        voice "audio/voices/ch3/razor/nexus/cheated/17.flac"
                        show razor2 r blush onlayer back
                        with dissolve
                        cheated "I'll be damned. This is actually going to work, isn't it?\n"
                        voice "audio/voices/ch3/razor/nexus/princess/23.flac"
                        show razor2 r blush serious talk onlayer back
                        with dissolve
                        sp "Still going to kill you, but now we can both enjoy a mutual romantic subtext to the murder.\n"

                $ gallery_razor.unlock_item(10)
                $ renpy.save_persistent()
                voice "audio/voices/ch3/razor/nexus/hero/10.flac"
                show razor2 r blush serious onlayer back
                with dissolve
                hero "Or not.\n"
                if trait_broken:
                    voice "audio/voices/ch3/razor/nexus/broken/11.flac"
                    broken "At least she likes us. I've never been liked before.\n"
                elif trait_paranoid:
                    voice "audio/voices/ch3/razor/nexus/paranoid/11.flac"
                    paranoid "Is anything going to work with her? She's so single minded. It's like whatever we do it's always going to end exactly the same.\n"
                elif trait_stubborn:
                    voice "audio/voices/ch3/razor/nexus/stubborn/11.flac"
                    stubborn "Oh, I like her. I like her a lot!\n"
                voice "audio/voices/ch3/razor/nexus/narrator/27.flac"
                play audio "audio/final/__metal_run.flac"
                show razor2 r blush charge onlayer back
                with dissolve
                n "Blush still glowing in her cheeks, the Princess closes the distance between you, blades flashing.\n"
                voice "audio/voices/ch3/razor/nexus/narrator/17.flac"
                play audio "audio/final/Razor_ImpaleSwordBody_6.flac"
                stop music
                hide razor2 onlayer back
                hide bg onlayer back
                scene bg black
                n "She skewers you.\n"
                voice "audio/voices/ch3/razor/nexus/hero/5.flac"
                hero "Ow.\n"
                voice "audio/voices/ch3/razor/nexus/smitten/1.flac"
                $ trait_smitten = True
                scene bg razor2 close onlayer back at Position(ypos=1125)
                show razor2 close enthusiastic onlayer front at Position(ypos=1125)
                with fade
                smitten "What worthwhile romance doesn't hurt at least a little bit? What matters is that she likes us. She's even said as much!\n"

            "{i}• She has swords for arms and we don't. We're panicking!{/i}" if trait_paranoid == False:
                if trait_stubborn:
                    voice "audio/voices/ch3/razor/nexus/stubborn/12.flac"
                    stubborn "Panicking is the worst possible thing for us to do.\n"
                    voice "audio/voices/ch3/razor/nexus/hero/11.flac"
                    hero "And panic where? Up the slide that dropped us down here?\n"
                else:
                    voice "audio/voices/ch3/razor/nexus/hero/12.flac"
                    hero "Panic where? Up the slide that dropped us down here?\n"
                voice "audio/voices/ch3/razor/nexus/hunted/14.flac"
                hunted "There's no way out?!\n"
                voice "audio/voices/ch3/razor/nexus/princess/24.flac"
                show razor2 r chin offer talk onlayer back
                with dissolve
                sp "I'm coming to get you!\n"
                voice "audio/voices/ch3/razor/nexus/hunted/15.flac"
                play audio "audio/final/__metal_run.flac"
                show razor2 r charge onlayer back
                with dissolve
                hunted "There's no way out!\n"
                if trait_broken:
                    voice "audio/voices/ch3/razor/nexus/broken/12.flac"
                    broken "It's hard to panic when we already know what's going to happen to us.\n"
                    voice "audio/voices/ch3/razor/nexus/cheated/19.flac"
                    cheated "No. Screw it. We're panicking!\n"
                else:
                    voice "audio/voices/ch3/razor/nexus/cheated/20.flac"
                    cheated "Okay. Screw it. We're panicking!\n"
                voice "audio/voices/ch3/razor/nexus/narrator/28.flac"
                play audio "audio/final/Razor_ImpaleSwordBody_6.flac"
                stop music
                hide bg onlayer back
                hide cg onlayer back
                hide razor2 onlayer back
                scene bg black
                n "You panic, but unsurprisingly, panicking doesn't save you from her blades. She skewers you.\n"
                voice "audio/voices/ch3/razor/nexus/hero/5.flac"
                hero "Ow.\n"
                $ trait_paranoid = True
                voice "audio/voices/ch3/razor/nexus/paranoid/12.flac"
                scene bg razor2 close onlayer back at Position(ypos=1125)
                show razor2 close enthusiastic onlayer front at Position(ypos=1125)
                with fade
                paranoid "Sorry about that. I gave into a bit of a fear response there, and I don't think it was very helpful.\n"

            "{i}• We're going to fight her, and we're going to have a stiff upper lip about it. She can't hurt us if we don't let ourselves feel it.{/i}" if trait_cold == False and trait_stubborn == False:
                label razor_2_fight_join:
                    if trait_stubborn:
                        voice "audio/voices/ch3/razor/nexus/stubborn/laughidea.flac"
                        stubborn "Hahahaha yes! Yes! This is the best idea anyone has ever had!\n"
                    voice "audio/voices/ch3/razor/nexus/cheated/21.flac"
                    cheated "Yeah. Sure. Why the hell not! Let's see if we can turn off the part of us that feels things.\n"
                    if trait_broken:
                        voice "audio/voices/ch3/razor/nexus/broken/13.flac"
                        broken "I turned that off ages ago.\n"
                        #contrarian "If you'd managed to do that, you wouldn't be such a whiner.\n"
                    elif trait_paranoid:
                        voice "audio/voices/ch3/razor/nexus/paranoid/13.flac"
                        paranoid "If we can't feel things, then how are we supposed to know what's true?\n"
                        voice "audio/voices/ch3/razor/nexus/narrator/29.flac"
                        n "You could always just trust what I tell you.\n"
                        voice "audio/voices/ch3/razor/nexus/cheated/22.flac"
                        cheated "Ha! No.\n"
                    voice "audio/voices/ch3/razor/nexus/hunted/16.flac"
                    hunted "Pain is good. It's how we stay alive.\n"
                    voice "audio/voices/ch3/razor/nexus/cheated/23.flac"
                    cheated "Nah, I'm sick of pain.\n"
                    voice "audio/voices/ch3/razor/nexus/hero/13.flac"
                    hero "Yeah, this whole thing would be a lot more tolerable if it didn't hurt so much.\n"
                    menu:
                        extend ""

                        "{i}• ''Do your worst! I bet you can't even hurt me.''{/i}":
                            voice "audio/voices/ch3/razor/nexus/princess/25.flac"
                            show razor2 r happy talk onlayer back
                            with dissolve
                            sp "Sure thing! I love a challenge. I bet I can hurt you {i}so much{/i}!\n"

                        "{i}• [[Wait for her to come to you.]{/i}":
                            voice "audio/voices/ch3/razor/nexus/princess/26.flac"
                            show razor2 r chin offer talk onlayer back
                            with dissolve
                            sp "Just standing there, huh? A bold strategy.\n"

                    # FAST
                    voice "audio/voices/ch3/razor/nexus/narrator/30.flac"
                    play audio "audio/final/__metal_run.flac"
                    show razor2 r charge onlayer back
                    with dissolve
                    n "The Princess closes the distance, and—\n{w=2.15}{nw}"
                    show screen disableclick(0.5)
                    voice "audio/voices/ch3/razor/nexus/hunted/17.flac"
                    hunted "We dodge!\n"
                    voice "audio/voices/ch3/razor/nexus/narrator/31.flac"
                    play audio "audio/final/Razor_SwordSwish_10.flac"
                    hide razor2 onlayer back
                    show cg razor2 dodged onlayer back at Position(ypos=1125)
                    with dissolve
                    n "And you dodge.\n"
                    if trait_stubborn:
                        voice "audio/voices/ch3/razor/nexus/stubborn/14.flac"
                        play audio "audio/final/Razor_SwordHitSword_12.flac"
                        show bg basement razor2 postreveal onlayer back
                        show cg razor2 dodged onlayer back
                        show player clean knife onlayer inyourface at Position(ypos=1125)
                        with hpunch
                        stubborn "And we fight back.\n"
                        voice "audio/voices/ch3/razor/nexus/narrator/32.flac"
                        n "And you fight back.\n"
                    voice "audio/voices/ch3/razor/nexus/princess/27a.flac"
                    show cg razor2 dodged talk onlayer back
                    sp "Oooh. You're fast! But let's see how fast you really are.\n"
                    if trait_stubborn:
                        voice "audio/voices/ch3/razor/nexus/narrator/33.flac"
                        play secondary "audio/final/Razor_SwordCutArm_3.flac"
                        queue secondary "audio/one_shot/knife_slash.flac"
                        queue secondary "audio/final/Razor_SwordHitDrag_2.flac"
                        hide player onlayer inyourface
                        hide bg onlayer back
                        hide cg onlayer back
                        hide speedlines onlayer inyourface
                        hide cg onlayer front
                        hide bg onlayer back
                        hide razor2 onlayer back
                        show bg razor2 dodged onlayer farback at Position(ypos=1125)
                        show panel1 razor2 knife onlayer front at Position(ypos=1125)
                        show panel2 razor2 knife final onlayer back at Position(ypos=1125)
                        show panel3 razor2 knife final onlayer front at Position(ypos=1125)
                        with Dissolve(1.0)
                        n "You and the Princess enter a quick and vicious exchange, each of you wounding the other, but neither landing a fatal blow.\n"
                        voice "audio/voices/ch3/razor/nexus/stubborn/15.flac"
                        stubborn "Yes! Yes! This is exactly it!\n"
                        voice "audio/voices/ch3/razor/nexus/narrator/34.flac"
                        play audio "audio/final/Razor_ImpaleSwordBody_6.flac"
                        stop music
                        hide panel1 onlayer front
                        hide panel2 onlayer back
                        hide panel3 onlayer front
                        hide bg onlayer farback
                        hide bg onlayer back
                        hide cg onlayer back
                        hide razor2 onlayer back
                        scene bg black
                        n "But the dance couldn't last forever. All it takes is a single clumsy moment. She skewers you.\n"
                    else:
                        voice "audio/voices/ch3/razor/nexus/narrator/35.flac"
                        play audio "audio/final/_razor2_combat.flac"
                        hide player onlayer inyourface
                        hide bg onlayer back
                        hide cg onlayer back
                        hide speedlines onlayer inyourface
                        hide cg onlayer front
                        hide bg onlayer back
                        hide razor2 onlayer back
                        show bg razor2 dodged onlayer farback at Position(ypos=1125)
                        show panel1 razor2 dodged onlayer back at Position(ypos=1125)
                        show panel2 razor2 dodged anim onlayer front at Position(ypos=1125)
                        show panel3 razor2 dodged anim onlayer inyourface at Position(ypos=1125)
                        with Dissolve(1.0)
                        n "You dodge the Princess' blows for as long as you can, sustaining only nicks and cuts as you attempt to avoid her blades. But it isn't long before you're winded, your feet a little slower, your gait a little clumsier.\n"
                        voice "audio/voices/ch3/razor/nexus/narrator/36.flac"
                        play audio "audio/final/Razor_ImpaleSwordBody_6.flac"
                        stop music
                        hide panel1 onlayer back
                        hide panel2 onlayer front
                        hide panel3 onlayer inyourface
                        hide bg onlayer farback
                        hide bg onlayer back
                        hide cg onlayer back
                        hide razor2 onlayer back
                        scene bg black
                        n "That's all the opening she needs. She skewers you.\n"
                    voice "audio/voices/ch3/razor/nexus/princess/28.flac"
                    spmid "Gotcha!\n"
                    voice "audio/voices/ch3/razor/nexus/hero/14.flac"
                    hero "And? Does it hurt?\n"
                    $ trait_cold = True
                    voice "audio/voices/ch3/razor/nexus/cold/1.flac"
                    scene bg razor2 close onlayer back at Position(ypos=1125)
                    show razor2 close enthusiastic onlayer front at Position(ypos=1125)
                    with fade
                    cold "No.\n"

            "{i}• She wins by killing us, right? So let's beat her to it!{/i}" if trait_contrarian == False:
                voice "audio/voices/ch3/razor/nexus/hero/15.flac"
                hero "No, no, no that's a terrible idea!\n"
                if trait_broken:
                    voice "audio/voices/ch3/razor/nexus/broken/14.flac"
                    broken "We're dead either way.\n"
                if trait_paranoid:
                    voice "audio/voices/ch3/razor/nexus/paranoid/14.flac"
                    paranoid "Yeah, I'm not sure that's going to work.\n"
                if trait_stubborn:
                    voice "audio/voices/ch3/razor/nexus/stubborn/16.flac"
                    stubborn "A win's a win.\n"
                voice "audio/voices/ch3/razor/nexus/cheated/24.flac"
                cheated "Screw it. We've already died twice. What's a third?\n"
                voice "audio/voices/ch3/razor/nexus/narrator/37.flac"
                n "A third is a third. It's bad.\n"
                voice "audio/voices/ch3/razor/nexus/cheated/25.flac"
                cheated "Who cares!\n"
                voice "audio/voices/ch3/razor/nexus/narrator/38.flac"
                show player self end onlayer front at Position(ypos=1400)
                with dissolve
                n "{i}Sigh{/i}. Fine. You raise your blade above your head.\n"
                voice "audio/voices/ch3/razor/nexus/princess/29.flac"
                show razor2 r chin offer talk onlayer back
                with dissolve
                sp "Oh, this is new! What are you gonna do? Are you really going to stab yourself? Neat!\n"
                voice "audio/voices/ch3/razor/nexus/narrator/39.flac"
                play audio "audio/final/Razor_ImpaleSwordBody_6.flac"
                hide player onlayer front
                hide bg onlayer back
                hide cg onlayer back
                hide razor2 onlayer back
                scene bg black
                n "And then you skewer yourself.\n"
                voice "audio/voices/ch3/razor/nexus/hero/5.flac"
                hero "Ow.\n"
                voice "audio/voices/ch3/razor/nexus/cheated/26.flac"
                cheated "Are we still here? Can we not actually off ourselves? Boo.\n"
                $ trait_contrarian = True
                voice "audio/voices/ch3/razor/nexus/contrarian/2.flac"
                scene bg razor2 close onlayer back at Position(ypos=1125)
                show razor2 close enthusiastic onlayer front at Position(ypos=1125)
                with fade
                contrarian "Huh. That didn't do much of anything. We're tougher than I thought.\n"


            "{i}• [[All of these ideas suck. Think up something better.]{/i}" if trait_skeptic == False:
                voice "audio/voices/ch3/razor/nexus/cheated/27a.flac"
                cheated "Yeah, that's right. We just have to think. There's probably an answer if we think.\n"
                voice "audio/voices/ch3/razor/nexus/princess/26.flac"
                show razor2 r chin offer talk onlayer back
                with dissolve
                sp "Just standing there, huh? A bold strategy.\n" id razor_2_fight_join_05af087c
                voice "audio/voices/ch3/razor/nexus/narrator/40.flac"
                play audio "audio/final/__metal_run.flac"
                show razor2 r charge onlayer back
                with dissolve
                n "But you don't have time to finish your thought. In a moment, she's across the room, blades flashing in the dim starlight.\n"
                voice "audio/voices/ch3/razor/nexus/narrator/17.flac"
                play audio "audio/final/Razor_ImpaleSwordBody_6.flac"
                stop music
                hide bg onlayer back
                hide cg onlayer back
                hide razor2 onlayer back
                scene bg black
                n "She skewers you.\n"
                voice "audio/voices/ch3/razor/nexus/hero/5.flac"
                hero "Ow.\n"
                voice "audio/voices/ch3/razor/nexus/cheated/28.flac"
                cheated "What a surprise.\n"
                $ trait_skeptic = True
                voice "audio/voices/ch3/razor/nexus/skeptic/1.flac"
                scene bg razor2 close onlayer back at Position(ypos=1125)
                show razor2 close enthusiastic onlayer front at Position(ypos=1125)
                with fade
                skeptic "Yeah. We don't even get a second to think without her stabbing us.\n"

label razor_2_armed_beat_2:

    voice "audio/voices/ch3/razor/nexus/hero/16.flac"
    hero "Oh! A new one of us.\n"
    voice "audio/voices/ch3/razor/nexus/cheated/29.flac"
    cheated "I thought that only happens when we die. Did we die?\n"
    if trait_contrarian:
        voice "audio/voices/ch3/razor/nexus/contrarian/3a.flac"
        contrarian "Nah, we'd {i}know{/i} if we died... right?\n"
    play music "audio/_music/ch2/razor/The Razor Fast.flac" loop
    voice "audio/voices/ch3/razor/nexus/narrator/41.flac"
    n "You're on a— no, you're in a— where the hell are you?\n"
    if trait_paranoid:
        voice "audio/voices/ch3/razor/nexus/paranoid/15.flac"
        paranoid "We're dead, aren't we? We're {i}dead{/i} dead. How long have we been dead? Have we been dead the whole time?\n"
        if trait_broken:
            voice "audio/voices/ch3/razor/nexus/broken/15.flac"
            broken "Dead dead dead dead dead.\n"
    elif trait_broken:
        voice "audio/voices/ch3/razor/nexus/broken/16.flac"
        broken "I think we're dead. And that's all we'll ever be. Dead dead dead dead dead.\n"
    else:
        voice "audio/voices/ch3/razor/nexus/hero/_extra2.flac"
        hero "I don't like that we died without us knowing it. This really, really blurs some lines that I prefer not be blurred. Are we still dead? Are we alive again? How are we even supposed to know the difference?\n"
    if trait_cold:
        voice "audio/voices/ch3/razor/nexus/cold/2.flac"
        cold "If we didn't realize we were dead, then we made progress. Good job.\n"
    voice "audio/voices/ch3/razor/nexus/cheated/30.flac"
    cheated "Stop saying dead, all of you! We might have died a second ago, but right now we're extremely not dead.\n"
    voice "audio/voices/ch3/razor/nexus/narrator/42.flac"
    n "This is all horribly wrong. How many times have you been here?\n"
    voice "audio/voices/ch3/razor/nexus/hunted/18a.flac"
    hunted "This is four.\n"
    voice "audio/voices/ch3/razor/nexus/narrator/43.flac"
    n "No wonder everything's such a mess. This wasn't supposed to go past one.\n"
    voice "audio/voices/ch3/razor/nexus/princess/30.flac"
    show razor2 close neutral talk onlayer front
    with dissolve
    sp "I wonder what you're going to do next! You're so full of ideas and I love that.\n"
    voice "audio/voices/ch3/razor/nexus/narrator/44.flac"
    show razor2 close neutral onlayer front at spectre_small_zoom
    with dissolve
    n "But I guess we don't have time to talk about things before the Princess advances.\n"
    voice "audio/voices/ch3/razor/nexus/cheated/31.flac"
    cheated "Okay. Whatever we do gets us another... us. Let's see how many we can stack. There's got to be a point where it makes us better than her.\n"
    if trait_stubborn:
        voice "audio/voices/ch3/razor/nexus/stubborn/17.flac"
        stubborn "We don't need any other voices chattering about in here. It'll just confuse us. All we need is to keep fighting!\n"
        voice "audio/voices/ch3/razor/nexus/cheated/32.flac"
        cheated "Yeah, I'll pass on that.\n"
    if trait_hunted:
        voice "audio/voices/ch3/razor/nexus/hunted/19.flac"
        hunted "As long as we keep moving.\n"
    if trait_cold:
        voice "audio/voices/ch3/razor/nexus/cold/3.flac"
        cold "Why not? It's not like dying again and again is doing us any harm. Let's see how far this little mind-hole goes, shall we?\n"
    if trait_smitten:
        voice "audio/voices/ch3/razor/nexus/smitten/2.flac"
        smitten "We'll win her heart eventually!\n"
    if trait_paranoid and razor_paranoid_intro == False:
        $ razor_paranoid_intro = True
        voice "audio/voices/ch3/razor/nexus/paranoid/16.flac"
        paranoid "It's going to get so loud in here. How are we going to keep it all straight?\n"
    if trait_broken and razor_broken_intro == False:
        $ razor_broken_intro = True
        voice "audio/voices/ch3/razor/nexus/broken/17.flac"
        broken "Oh, great. So it's going to get even more crowded. Even more deluded voices that think we might stand any kind of chance.\n"
    if trait_opportunist:
        voice "audio/voices/ch3/razor/nexus/opportunist/2.flac"
        opportunist "Flawless idea if you ask me. Such a go-getter attitude!\n"
    if trait_contrarian:
        voice "audio/voices/ch3/razor/nexus/contrarian/4a.flac"
        contrarian "Who cares about getting better than her. Let's do something weird. Like really, really weird.\n"
    voice "audio/voices/ch3/razor/nexus/princess/31.flac"
    show razor2 close impatient talk onlayer front at spectre_small_zoom_instant
    with dissolve
    sp "Come onnnnnn! Show me something new!\n"
    show razor2 close impatient onlayer front at spectre_small_zoom_instant
    with dissolve
    if trait_skeptic:
        voice "audio/voices/ch3/razor/nexus/skeptic/2.flac"
        skeptic "Okay. Plan. Now!\n"
    menu:
        extend ""

        "{i}• We're going to fight her again, and we're going to have a stiff upper lip about it. She can't hurt us if we don't let ourselves feel it.{/i}" if trait_cold == False and trait_stubborn:
            $ trait_cold = True
            jump razor_2_armed_cold_early_join

        "{i}• We're fighting her, obviously.{/i}" if trait_stubborn == False:
            hide bg onlayer back
            hide razor2 onlayer back
            hide razor2 onlayer front
            show bg razor2 dodged onlayer farback at Position(ypos=1125)
            with Dissolve(1.0)
            truthmid "It doesn't work, and she kills you again. And again, and again, and again. Your memory blurs as your consciousness leaps from life to life to life, holding only snippets of the conflict that transpires.\n"
            $ trait_stubborn = True
            voice "audio/voices/ch3/razor/nexus/stubborn/18.flac"
            play audio "audio/final/Razor_SwordHitSword_2.flac"
            show montage1 razor armed onlayer back at Position(ypos=1125)
            with dissolve
            stubborn "We just have to hit her harder!\n"
            voice "audio/voices/ch3/razor/nexus/narrator/skewer1.flac"
            play audio "audio/final/Razor_ImpaleSwordBody_3.flac"
            n "She skewers you.\n"
            voice "audio/voices/ch3/razor/nexus/princess/32.flac"
            show montage1 razor armed talk onlayer back at Position(ypos=1125)
            with dissolve
            spmid "You'll have to be trickier than that.\n"
            jump razor_2_armed_montage

        "{i}• We're going to appeal to her authority. Puff her up a bit. There's no reason we can't talk this out.{/i}" if trait_opportunist == False:
            hide bg onlayer back
            hide razor2 onlayer front
            hide razor2 onlayer back
            show bg razor2 dodged onlayer farback at Position(ypos=1125)
            with Dissolve(1.0)
            truthmid "It doesn't work, and she kills you again. And again, and again, and again. Your memory blurs as your consciousness leaps from life to life to life, holding only snippets of the conflict that transpires.\n"
            $ trait_opportunist = True
            play audio "audio/final/Razor_SwordHitSword_2.flac"
            voice "audio/voices/ch3/razor/nexus/opportunist/3.flac"
            show montage1 razor armed onlayer back at Position(ypos=1125)
            with dissolve
            opportunist "Let's appeal to her better nature! We haven't tried that. I'm sure she'll listen to reason.\n"
            voice "audio/voices/ch3/razor/nexus/narrator/skewer2.flac"
            play audio "audio/final/Razor_ImpaleSwordBody_3.flac"
            n "She skewers you.\n"
            jump razor_2_armed_montage

        "{i}• We're going to unconditionally surrender.{/i}" if trait_broken == False:
            hide bg onlayer back
            hide razor2 onlayer front
            hide razor2 onlayer back
            show bg razor2 dodged onlayer farback at Position(ypos=1125)
            with Dissolve(1.0)
            truthmid "It doesn't work, and she kills you again. And again, and again, and again. Your memory blurs as your consciousness leaps from life to life to life, holding only snippets of the conflict that transpires.\n"
            $ trait_broken = True
            voice "audio/voices/ch3/razor/nexus/broken/18.flac"
            play audio "audio/final/Razor_SwordHitSword_2.flac"
            show montage1 razor armed onlayer back at Position(ypos=1125)
            with dissolve
            broken "What's the point? It's all the same.\n"
            voice "audio/voices/ch3/razor/nexus/narrator/skewer2.flac"
            play audio "audio/final/Razor_ImpaleSwordBody_3.flac"
            n "She skewers you.\n"
            voice "audio/voices/ch3/razor/nexus/princess/33.flac"
            show montage1 razor armed talk onlayer back
            with dissolve
            spmid "Oh, don't give up on me just yet! You gotta keep going!\n"
            jump razor_2_armed_montage


        "{i}• Oh, that's easy. I'm going to try flirting with her.{/i}" if trait_smitten == False:
            hide bg onlayer back
            hide razor2 onlayer back
            hide razor2 onlayer front
            show bg razor2 dodged onlayer farback at Position(ypos=1125)
            with Dissolve(1.0)
            truthmid "It doesn't work, and she kills you again. And again, and again, and again. Your memory blurs as your consciousness leaps from life to life to life, holding only snippets of the conflict that transpires.\n"
            $ trait_smitten = True
            voice "audio/voices/ch3/razor/nexus/smitten/3.flac"
            play audio "audio/final/Razor_SwordHitSword_2.flac"
            show montage1 razor armed onlayer back at Position(ypos=1125)
            with dissolve
            smitten "Compliment her on those gleaming blades! There's nothing better than a capable woman.\n"
            voice "audio/voices/ch3/razor/nexus/narrator/skewer3.flac"
            play audio "audio/final/Razor_ImpaleSwordBody_3.flac"
            n "She skewers you.\n"
            voice "audio/voices/ch3/razor/nexus/princess/35.flac"
            show montage1 razor armed talk onlayer back
            with dissolve
            spmid "You're cute.\n"
            jump razor_2_armed_montage

        "{i}• She has swords for arms and we don't. We're panicking!{/i}" if trait_paranoid == False:
            hide bg onlayer back
            hide razor2 onlayer back
            hide razor2 onlayer front
            show bg razor2 dodged onlayer farback at Position(ypos=1125)
            with Dissolve(1.0)
            truthmid "It doesn't work, and she kills you again. And again, and again, and again. Your memory blurs as your consciousness leaps from life to life to life, holding only snippets of the conflict that transpires.\n"
            $ trait_paranoid = True
            voice "audio/voices/ch3/razor/nexus/paranoid/17.flac"
            play audio "audio/final/Razor_SwordHitSword_2.flac"
            show montage1 razor armed onlayer back at Position(ypos=1125)
            with dissolve
            paranoid "Just panic! Flee!\n"
            voice "audio/voices/ch3/razor/nexus/narrator/skewer4.flac"
            play audio "audio/final/Razor_ImpaleSwordBody_3.flac"
            n "She skewers you.\n"
            voice "audio/voices/ch3/razor/nexus/princess/36.flac"
            show montage1 razor armed talk onlayer back
            with dissolve
            spmid "No, you don't get to escape! That's not how this works.\n"
            jump razor_2_armed_montage

        "{i}• We're going to let her stab us, and we're going to have a stiff upper lip about it. She can't hurt us if we don't let ourselves feel it.{/i}" if trait_cold == False and trait_stubborn == False:
            label razor_2_armed_cold_early_join:
                hide bg onlayer back
                hide razor2 onlayer back
                hide razor2 onlayer front
                show bg razor2 dodged onlayer farback at Position(ypos=1125)
                with Dissolve(1.0)
                truthmid "It doesn't work, and she kills you again. And again, and again, and again. Your memory blurs as your consciousness leaps from life to life to life, holding only snippets of the conflict that transpires.\n"
                $ trait_cold = True
                voice "audio/voices/ch3/razor/nexus/cold/4.flac"
                play audio "audio/final/Razor_SwordHitSword_2.flac"
                show montage1 razor armed onlayer back at Position(ypos=1125)
                with dissolve
                cold "She's going to kill this body either way. So stop feeling what it feels.\n"
                voice "audio/voices/ch3/razor/nexus/narrator/skewer5.flac"
                play audio "audio/final/Razor_ImpaleSwordBody_3.flac"
                n "She skewers you.\n"
                voice "audio/voices/ch3/razor/nexus/princess/37.flac"
                show montage1 razor armed talk onlayer back
                with dissolve
                spmid "Ooooh. Not bad! Real tough!\n"
                jump razor_2_armed_montage

        "{i}• She wins by killing us, right? So let's beat her to it!{/i}" if trait_contrarian == False:
            hide bg onlayer back
            hide razor2 onlayer back
            hide razor2 onlayer front
            show bg razor2 dodged onlayer farback at Position(ypos=1125)
            with Dissolve(1.0)
            truthmid "It doesn't work, and she kills you again. And again, and again, and again. Your memory blurs as your consciousness leaps from life to life to life, holding only snippets of the conflict that transpires.\n"
            $ trait_contrarian = True
            voice "audio/voices/ch3/razor/nexus/narrator/39.flac"
            play audio "audio/final/Razor_ImpaleSwordBody_6.flac"
            show montagec razor armed onlayer back at Position(ypos=1125)
            with dissolve
            n "And then you skewer yourself.\n"
            voice "audio/voices/ch3/razor/nexus/princess/34.flac"
            show montagec razor armed talk onlayer back
            with dissolve
            sp "I thought we both understood that dying doesn't get you anywhere.\n"
            voice "audio/voices/ch3/razor/nexus/contrarian/2.flac"
            contrarian "Huh. That didn't do much of anything. We're tougher than I thought.\n"
            jump razor_2_armed_montage

        "{i}• [[All of these ideas suck. Think up something better.]{/i}" if trait_skeptic == False:
            hide bg onlayer back
            hide razor2 onlayer back
            hide razor2 onlayer front
            show bg razor2 dodged onlayer farback at Position(ypos=1125)
            with Dissolve(1.0)
            truthmid "It doesn't work, and she kills you again. And again, and again, and again. Your memory blurs as your consciousness leaps from life to life to life, holding only snippets of the conflict that transpires.\n"
            $ trait_skeptic = True
            voice "audio/voices/ch3/razor/nexus/skeptic/3.flac"
            play audio "audio/final/Razor_SwordHitSword_2.flac"
            show montage1 razor armed onlayer back at Position(ypos=1125)
            with dissolve
            skeptic "None of this is working! Think. Think!\n"
            voice "audio/voices/ch3/razor/nexus/narrator/skewer7.flac"
            play audio "audio/final/Razor_ImpaleSwordBody_3.flac"
            show montage1 razor armed talk onlayer back
            with dissolve
            n "She skewers you.\n"
            jump razor_2_armed_montage

    label razor_2_armed_montage:
        $ razor_montage_panel_number = 1
        label razor_2_armed_montage_loop:
            default razor_montage_panel_number = 1
            $ razor_loop += 1
            if razor_loop <= 5:
                if razor_loop == 1:
                    voice "audio/voices/ch3/razor/nexus/cheated/33.flac"
                    cheated "Well, there's more of us. Let's see if that helps.\n"

                if razor_loop == 2 and razor_mont_cont_flag == False:
                    voice "audio/voices/ch3/razor/nexus/cheated/34.flac"
                    cheated "Do you see that? We almost had her!\n"
                    voice "audio/voices/ch3/razor/nexus/hero/17.flac"
                    hero "That was luck.\n"
                    voice "audio/voices/ch3/razor/nexus/cheated/35.flac"
                    cheated "But we only have to get lucky once.\n"

                if razor_loop == 3:
                    voice "audio/voices/ch3/razor/nexus/cheated/36.flac"
                    cheated "It doesn't matter how many times this takes. We can't give up.\n"
                    voice "audio/voices/ch3/razor/nexus/hero/18.flac"
                    hero "{i}Sigh{/i}. Okay. Let's go again.\n"

                if razor_loop == 4:
                    voice "audio/voices/ch3/razor/nexus/cheated/37.flac"
                    cheated "See? We're getting better.\n"
                    voice "audio/voices/ch3/razor/nexus/hero/19.flac"
                    hero "Okay. Okay, yeah. That was a good one.\n"

                if razor_loop == 5:
                    voice "audio/voices/ch3/razor/nexus/cheated/38.flac"
                    cheated "We're getting close to something, can't you feel it? One. Last. Time.\n"
                    voice "audio/voices/ch3/razor/nexus/hero/20.flac"
                    hero "You're right. One last time. That's all we need.\n"

                if trait_stubborn == False:
                    $ razor_montage_panel_number += 1
                    $ trait_stubborn = True
                    default mont_panel_2_flag = False
                    voice "audio/voices/ch3/razor/nexus/stubborn/18.flac"
                    play audio "audio/final/Razor_SwordHitSword_2.flac"
                    if trait_contrarian == False:
                        show montage3 razor armed onlayer back
                        with dissolve
                    else:
                        $ mont_panel_2_flag = True
                        show montage2 razor armed onlayer back
                        with dissolve
                    stubborn "We just have to hit her harder!\n"
                    voice "audio/voices/ch3/razor/nexus/narrator/skewer1.flac"
                    play audio "audio/final/Razor_ImpaleSwordBody_5.flac"
                    n "She skewers you.\n"
                    voice "audio/voices/ch3/razor/nexus/princess/32.flac"
                    if trait_contrarian == False:
                        show montage3 razor armed talk onlayer back
                        with dissolve
                    else:
                        show montage2 razor armed talk onlayer back
                        with dissolve
                    sp "You'll have to be trickier than that.\n"

                if trait_contrarian == False:
                    default razor_mont_cont_flag = False
                    $ razor_montage_panel_number += 1
                    $ razor_mont_cont_flag = True
                    $ trait_contrarian = True
                    voice "audio/voices/ch3/razor/nexus/narrator/39.flac"
                    play audio "audio/final/Razor_ImpaleSwordBody_3.flac"
                    show montagec razor armed onlayer back
                    with dissolve
                    n "And then you skewer yourself.\n"
                    voice "audio/voices/ch3/razor/nexus/princess/34.flac"
                    show montagec razor armed talk onlayer back
                    with dissolve
                    sp "I thought we both understood that dying doesn't get you anywhere.\n"
                    voice "audio/voices/ch3/razor/nexus/contrarian/2.flac"
                    contrarian "Huh. That didn't do much of anything. We're tougher than I thought.\n"

                elif trait_broken == False:
                    $ trait_broken = True
                    $ razor_montage_panel_number += 1
                    voice "audio/voices/ch3/razor/nexus/broken/18.flac"
                    play audio "audio/final/Razor_SwordHitSword_1.flac"
                    if razor_montage_panel_number == 2:
                        show montage2 razor armed onlayer back
                        with dissolve
                    elif razor_montage_panel_number == 3:
                        show montage3 razor armed onlayer front
                        with dissolve
                    elif razor_montage_panel_number == 4:
                        show montage4 razor armed onlayer front
                        with dissolve
                    elif razor_montage_panel_number == 5:
                        show montage5 razor armed onlayer inyourface
                        with dissolve
                    elif razor_montage_panel_number == 6:
                        show montage6 razor armed onlayer inyourface
                        with dissolve
                    broken "What's the point? It's all the same.\n"
                    voice "audio/voices/ch3/razor/nexus/narrator/skewer2.flac"
                    play audio "audio/final/Razor_ImpaleSwordBody_5.flac"
                    n "She skewers you.\n"
                    voice "audio/voices/ch3/razor/nexus/princess/33.flac"
                    if razor_montage_panel_number == 2:
                        show montage2 razor armed talk onlayer back
                        with dissolve
                    elif razor_montage_panel_number == 3:
                        show montage3 razor armed talk onlayer front
                        with dissolve
                    elif razor_montage_panel_number == 4:
                        show montage4 razor armed talk onlayer front
                        with dissolve
                    elif razor_montage_panel_number == 5:
                        show montage5 razor armed talk onlayer inyourface
                        with dissolve
                    elif razor_montage_panel_number == 6:
                        show montage6 razor armed talk onlayer inyourface
                        with dissolve
                    sp "Oh, don't give up on me just yet! You gotta keep going!\n"

                elif trait_smitten == False:
                    $ trait_smitten = True
                    $ razor_montage_panel_number += 1
                    play audio "audio/final/Razor_SwordHitSword_3.flac"
                    voice "audio/voices/ch3/razor/nexus/smitten/3.flac"
                    if razor_montage_panel_number == 2:
                        show montage2 razor armed onlayer back
                        with dissolve
                    elif razor_montage_panel_number == 3:
                        show montage3 razor armed onlayer front
                        with dissolve
                    elif razor_montage_panel_number == 4:
                        show montage4 razor armed onlayer front
                        with dissolve
                    elif razor_montage_panel_number == 5:
                        show montage5 razor armed onlayer inyourface
                        with dissolve
                    elif razor_montage_panel_number == 6:
                        show montage6 razor armed onlayer inyourface
                        with dissolve
                    smitten "Compliment her on those gleaming blades! There's nothing better than a capable woman.\n"
                    voice "audio/voices/ch3/razor/nexus/narrator/skewer3.flac"
                    play audio "audio/final/Razor_ImpaleSwordBody_5.flac"
                    n "She skewers you.\n"
                    voice "audio/voices/ch3/razor/nexus/princess/35.flac"
                    if razor_montage_panel_number == 2:
                        show montage2 razor armed talk onlayer back
                        with dissolve
                    elif razor_montage_panel_number == 3:
                        show montage3 razor armed talk onlayer front
                        with dissolve
                    elif razor_montage_panel_number == 4:
                        show montage4 razor armed talk onlayer front
                        with dissolve
                    elif razor_montage_panel_number == 5:
                        show montage5 razor armed talk onlayer inyourface
                        with dissolve
                    elif razor_montage_panel_number == 6:
                        show montage6 razor armed talk onlayer inyourface
                        with dissolve
                    sp "You're cute.\n"

                elif trait_paranoid == False:
                    $ trait_paranoid = True
                    $ razor_montage_panel_number += 1
                    play audio "audio/final/Razor_SwordHitSword_4.flac"
                    voice "audio/voices/ch3/razor/nexus/paranoid/17.flac"
                    if razor_montage_panel_number == 2:
                        show montage2 razor armed onlayer back
                        with dissolve
                    elif razor_montage_panel_number == 3:
                        show montage3 razor armed onlayer front
                        with dissolve
                    elif razor_montage_panel_number == 4:
                        show montage4 razor armed onlayer front
                        with dissolve
                    elif razor_montage_panel_number == 5:
                        show montage5 razor armed onlayer inyourface
                        with dissolve
                    elif razor_montage_panel_number == 6:
                        show montage6 razor armed onlayer inyourface
                        with dissolve
                    paranoid "Just panic! Flee!\n"
                    voice "audio/voices/ch3/razor/nexus/narrator/skewer4.flac"
                    play audio "audio/final/Razor_ImpaleSwordBody_5.flac"
                    n "She skewers you.\n"
                    voice "audio/voices/ch3/razor/nexus/princess/36.flac"
                    if razor_montage_panel_number == 2:
                        show montage2 razor armed talk onlayer back
                        with dissolve
                    elif razor_montage_panel_number == 3:
                        show montage3 razor armed talk onlayer front
                        with dissolve
                    elif razor_montage_panel_number == 4:
                        show montage4 razor armed talk onlayer front
                        with dissolve
                    elif razor_montage_panel_number == 5:
                        show montage5 razor armed talk onlayer inyourface
                        with dissolve
                    elif razor_montage_panel_number == 6:
                        show montage6 razor armed talk onlayer inyourface
                        with dissolve
                    sp "No, you don't get to escape! That's not how this works.\n"

                elif trait_cold == False:
                    $ trait_cold = True
                    $ razor_montage_panel_number += 1
                    play audio "audio/final/Razor_SwordHitSword_5.flac"
                    voice "audio/voices/ch3/razor/nexus/cold/4.flac"
                    if razor_montage_panel_number == 2:
                        show montage2 razor armed onlayer back
                        with dissolve
                    elif razor_montage_panel_number == 3:
                        show montage3 razor armed onlayer front
                        with dissolve
                    elif razor_montage_panel_number == 4:
                        show montage4 razor armed onlayer front
                        with dissolve
                    elif razor_montage_panel_number == 5:
                        show montage5 razor armed onlayer inyourface
                        with dissolve
                    elif razor_montage_panel_number == 6:
                        show montage6 razor armed onlayer inyourface
                        with dissolve
                    cold "She's going to kill this body either way. So stop feeling what it feels.\n"
                    voice "audio/voices/ch3/razor/nexus/narrator/skewer5.flac"
                    play audio "audio/final/Razor_ImpaleSwordBody_5.flac"
                    n "She skewers you.\n"
                    voice "audio/voices/ch3/razor/nexus/princess/37.flac"
                    if razor_montage_panel_number == 2:
                        show montage2 razor armed talk onlayer back
                        with dissolve
                    elif razor_montage_panel_number == 3:
                        show montage3 razor armed talk onlayer front
                        with dissolve
                    elif razor_montage_panel_number == 4:
                        show montage4 razor armed talk onlayer front
                        with dissolve
                    elif razor_montage_panel_number == 5:
                        show montage5 razor armed talk onlayer inyourface
                        with dissolve
                    elif razor_montage_panel_number == 6:
                        show montage6 razor armed talk onlayer inyourface
                        with dissolve
                    sp "Ooooh. Not bad! Real tough!\n"

                elif trait_opportunist == False:
                    $ trait_opportunist = True
                    $ razor_montage_panel_number += 1
                    voice "audio/voices/ch3/razor/nexus/opportunist/3.flac"
                    play audio "audio/final/Razor_SwordHitSword_6.flac"
                    if razor_montage_panel_number == 2:
                        show montage2 razor armed onlayer back
                        with dissolve
                    elif razor_montage_panel_number == 3:
                        show montage3 razor armed onlayer front
                        with dissolve
                    elif razor_montage_panel_number == 4:
                        show montage4 razor armed onlayer front
                        with dissolve
                    elif razor_montage_panel_number == 5:
                        show montage5 razor armed onlayer inyourface
                        with dissolve
                    elif razor_montage_panel_number == 6:
                        show montage6 razor armed onlayer inyourface
                        with dissolve
                    opportunist "Let's appeal to her better nature! We haven't tried that. I'm sure she'll listen to reason.\n"
                    voice "audio/voices/ch3/razor/nexus/narrator/skewer2.flac"
                    play audio "audio/final/Razor_ImpaleSwordBody_5.flac"
                    n "She skewers you.\n"

                elif trait_skeptic == False:
                    $ trait_skeptic = True
                    $ razor_montage_panel_number += 1
                    voice "audio/voices/ch3/razor/nexus/skeptic/3.flac"
                    play audio "audio/final/Razor_SwordHitSword_7.flac"
                    if razor_montage_panel_number == 2:
                        show montage2 razor armed onlayer back
                        with dissolve
                    elif razor_montage_panel_number == 3:
                        show montage3 razor armed onlayer front
                        with dissolve
                    elif razor_montage_panel_number == 4:
                        show montage4 razor armed onlayer front
                        with dissolve
                    elif razor_montage_panel_number == 5:
                        show montage5 razor armed onlayer inyourface
                        with dissolve
                    elif razor_montage_panel_number == 6:
                        show montage6 razor armed onlayer inyourface
                        with dissolve
                    skeptic "None of this is working! Think. Think!\n"
                    play audio "audio/final/Razor_ImpaleSwordBody_5.flac"
                    voice "audio/voices/ch3/razor/nexus/narrator/skewer7.flac"
                    n "She skewers you.\n"

                jump razor_2_armed_montage_loop

        stop sound
        stop secondary
        stop music
        hide bg onlayer farback
        hide montagec onlayer back
        hide montagec onlayer front
        hide montage1 onlayer back
        hide montage2 onlayer back
        hide montage2 onlayer front
        hide montage3 onlayer back
        hide montage3 onlayer front
        hide montage4 onlayer front
        hide montage5 onlayer inyourface
        hide montage6 onlayer inyourface
        with fade
        voice "audio/voices/ch3/razor/nexus/narrator/45.flac"
        n "And then everything goes dark, and you die.\n"
        $ razor_blade = True
        jump razor_final_staging

label razor_2_unarmed_start:
    play music "audio/_music/ch2/razor/The Razor Heightened.flac" loop
    voice "audio/voices/ch3/razor/nexus/narrator/46.flac"
    scene bg basement razor2 onlayer back at Position(ypos=1125)
    show razor2 neutral onlayer back at Position(ypos=1125)
    with fade
    n "As your body tumbles onto the basement landing, the form of the Princess comes into view. Wryly smiling at you from a distance.\n"
    voice "audio/voices/ch3/razor/nexus/princess/1.flac"
    show razor2 neutral talk onlayer back
    with dissolve
    sp "Hi! It looks like you don't have a way out, so I'm not going to play dumb anymore.\n"
    voice "audio/voices/ch3/razor/nexus/princess/38.flac"
    show razor2 wink talk onlayer back
    with dissolve
    sp "And you still don't have a weapon! That's funny! That's a joke! I'm going to kill you now.\n"
    voice "audio/voices/ch3/razor/nexus/contrarian/5.flac"
    show razor2 neutral onlayer back
    with dissolve
    contrarian "Yes, that was extremely silly of whoever did that. Probably a bad idea!\n"
    voice "audio/voices/ch3/razor/nexus/hero/21.flac"
    hero "That was you!\n"
    voice "audio/voices/ch3/razor/nexus/contrarian/6.flac"
    contrarian "I know! I'm just trying to add some levity to this.\n"
    voice "audio/voices/ch3/razor/nexus/cheated/39.flac"
    cheated "Well, since all of this was your idea, how about you figure out how to get us out of it?\n"
    voice "audio/voices/ch3/razor/nexus/contrarian/7.flac"
    contrarian "Oh, guys like us don't get to make any decisions, you should know that.\n"
    voice "audio/voices/ch3/razor/nexus/cheated/40.flac"
    cheated "I decided to pick up that blade, and {i}you{/i} decided to throw it out the window.\n"
    #voice "audio/voices/ch3/razor/nexus/contrarian/8.flac"
    #contrarian "I provided the set up. The punchline is up to you.\n"
    if trait_paranoid:
        $ razor_paranoid_intro = True
        voice "audio/voices/ch3/razor/nexus/paranoid/18.flac"
        paranoid "I take it back. Having my own corner clearly isn't working because I can still hear you three yelling at each other. She's going to kill us again, you know. Especially if we keep fighting with ourself. We need to get rid of our thoughts.\n"
    elif trait_broken:
        $ razor_broken_intro = True
        voice "audio/voices/ch3/razor/nexus/broken/19.flac"
        broken "This is why we've already lost. Can't even stop bickering with ourself. How are we supposed to beat her without a weapon? She's so sharp.\n"
    voice "audio/voices/ch3/razor/nexus/narrator/3.flac"
    play audio "audio/final/Razor_FleshExplosion_1.flac"
    play secondary "audio/final/Razor_ImpaleSwordBody_5.flac"
    show razor2 reveal anim onlayer back
    with dissolve
    n "Your internal bickering is cut short by the wet sound of slicing meat. From the Princess' arms erupt twin blades, glistening with her blood, the empty flesh of her arms flopping at her elbows like torn sleeves. The chain clatters to the floor.\n"
    voice "audio/voices/ch3/razor/nexus/princess/3.flac"
    show bg basement razor2 postreveal onlayer back at Position(ypos=1125)
    show razor2 r talk onlayer back
    with dissolve
    sp "You're going to make me walk over to you, aren't you?\n"
    voice "audio/voices/ch3/razor/nexus/cheated/41.flac"
    play audio "audio/final/__metal_step.flac"
    show razor2 r step onlayer back
    with dissolve
    cheated "All right. I'm out of ideas. What we doing?\n"
    label razor_2_unarmed_beat_1:
        menu:
            extend ""

            "{i}• We're fighting her, obviously.{/i}" if trait_stubborn == False:
                voice "audio/voices/ch3/razor/nexus/hero/22.flac"
                hero "We're fighting her? Are you forgetting the part where the cheeky one thought it'd be funny to throw our only weapon out the window?\n"
                voice "audio/voices/ch3/razor/nexus/contrarian/9.flac"
                contrarian "I mean, it {i}was{/i} funny. Even she said it was funny.\n"
                voice "audio/voices/ch3/razor/nexus/cheated/42.flac"
                cheated "Oh, yes. It was absolutely hilarious.\n"
                voice "audio/voices/ch3/razor/nexus/contrarian/10.flac"
                contrarian "We'll all be laughing together once we're out of here.\n"
                if trait_broken:
                    voice "audio/voices/ch3/razor/nexus/broken/20.flac"
                    broken "If we make it out of here. But I don't know. That seems unlikely.\n"
                else:
                    voice "audio/voices/ch3/razor/nexus/paranoid/19a.flac"
                    paranoid "Do any of us think we can hurt her like this?\n"
                menu:
                    extend ""

                    "{i}• Maybe we'll win!{/i}":
                        voice "audio/voices/ch3/razor/nexus/contrarian/11.flac"
                        contrarian "Yes, exactly! Who knows what we're capable of? For all we know that 'blade' was holding us back.\n"
                        label razor_2_unarmed_cheated_join:
                            voice "audio/voices/ch3/razor/nexus/cheated/43.flac"
                            cheated "{i}Sigh{/i}. Okay. Why not?\n"
                            voice "audio/voices/ch3/razor/nexus/narrator/47.flac"
                            play audio "audio/final/__metal_run.flac"
                            show bg basement razor2 postreveal onlayer back at big_zoom
                            show razor2 r step onlayer back at big_zoom_instant
                            show speedlines onlayer inyourface at Position(ypos=1125)
                            with dissolve
                            n "Fists raised, you charge the Princess.\n"
                            voice "audio/voices/ch3/razor/nexus/princess/39.flac"
                            show razor2 r happy talk onlayer back at big_zoom_instant
                            with dissolve
                            sp "Oh, so you do want a fight, huh? Okay! Hit me! Hit me and see what happens! I'll give you a free shot and everything!\n"
                            voice "audio/voices/ch3/razor/nexus/hero/4.flac"
                            hero "Here goes... we can make this work.\n"
                            if trait_broken:
                                voice "audio/voices/ch3/razor/nexus/broken/4.flac"
                                broken "And what if we don't?\n"
                            if trait_paranoid:
                                voice "audio/voices/ch3/razor/nexus/paranoid/20.flac"
                                paranoid "Yeah. Mind over matter, mind over matter, mind over matter. What if she's lying? What if she isn't going to give us a free shot?\n"
                            voice "audio/voices/ch3/razor/nexus/narrator/48.flac"
                            play audio "audio/final/Razor_StepMetal_3.flac"
                            hide speedlines onlayer inyourface
                            hide razor2 onlayer back
                            hide bg onlayer back
                            show bg razor2 close onlayer back at Position(ypos=1125)
                            show cg razor2 fist slam onlayer front at Position(ypos=1125)
                            with Dissolve(1.0)
                            n "Your fist slams into the Princess' face, and she recoils in pain.\n"
                            voice "audio/voices/ch3/razor/nexus/cheated/44.flac"
                            cheated "Huh. We actually did something to her!\n"
                            voice "audio/voices/ch3/razor/nexus/princess/40.flac"
                            show cg razor2 fist slam recoil onlayer front
                            with dissolve
                            spmid "Ow ow ow ow ow! That hurt! What are your bones made of, metal?\n"
                            voice "audio/voices/ch3/razor/nexus/princess/41.flac"
                            show cg razor2 fist slam recover onlayer front
                            with dissolve
                            sp "Because mine are.\n"
                            $ gallery_razor.unlock_item(9)
                            $ renpy.save_persistent()
                            $ achievement.grant("ACH_RAZOR_PUNCH")
                            voice "audio/voices/ch3/razor/nexus/narrator/49.flac"
                            play audio "audio/final/den_emerge.flac"
                            show cg razor2 punch counter onlayer front
                            with dissolve
                            n "Before you can react, she returns a punch of her own, only it isn't really a 'punch.'\n"
                            voice "audio/voices/ch3/razor/nexus/cheated/45.flac"
                            cheated "Yes, we all know she has swords for arms. We have eyes.\n"
                            voice "audio/voices/ch3/razor/nexus/narrator/50.flac"
                            play audio "audio/final/Razor_ImpaleSwordBody_6.flac"
                            stop music
                            hide bg onlayer back
                            hide cg onlayer back
                            hide cg onlayer front
                            hide razor2 onlayer back
                            scene bg black
                            n "Well, she skewers you.\n"
                            voice "audio/voices/ch3/razor/nexus/hero/5.flac"
                            hero "Ow.\n"
                            voice "audio/voices/ch3/razor/nexus/princess/6.flac"
                            scene bg razor2 close onlayer back at Position(ypos=1125)
                            show razor2 close enthusiastic talk onlayer front at Position(ypos=1125)
                            with fade
                            sp "Ribbons! I'm going to make you ribbons! This is so much fun and I want to celebrate.\n"
                            #cheated "What a surprise.\n"
                            $ trait_stubborn = True
                            voice "audio/voices/ch3/razor/nexus/stubborn/19.flac"
                            stubborn "It would have worked if we punched harder.\n"

                    "{i}• See, but that's the brilliance of it all. She won't see it coming.{/i}":
                        jump razor_2_unarmed_cheated_join

                    "{i}• I'm done explaining myself. I'm going to punch her now.{/i}":
                        voice "audio/voices/ch3/razor/nexus/contrarian/12.flac"
                        contrarian "Oooh. Someone's mad!\n"
                        jump razor_2_unarmed_cheated_join

            "{i}• We're going to appeal to her authority. Puff her up a bit. There's no reason we can't talk this out.{/i}" if trait_opportunist == False:
                if trait_broken:
                    voice "audio/voices/ch3/razor/nexus/broken/21.flac"
                    broken "{i}Can{/i} we talk this out? I think she wants to kill us.\n"
                if trait_paranoid:
                    voice "audio/voices/ch3/razor/nexus/paranoid/21.flac"
                    paranoid "Can we trust someone who wants us dead?\n"
                voice "audio/voices/ch3/razor/nexus/cheated/10.flac"
                cheated "Exactly. I think she established that at some point between stabbing us to death and directly telling us, just now, that she was going to kill us.\n"
                voice "audio/voices/ch3/razor/nexus/hero/6.flac"
                hero "You were the one who asked for ideas.\n"
                voice "audio/voices/ch3/razor/nexus/cheated/11.flac"
                cheated "Fine. Talk our way out of this! Maybe that's the answer.\n"
                menu:
                    extend ""

                    "{i}• ''You know, I'm a big fan of winners, and you've got 'winner' written all over you. How about we stop fighting and team up? I'll even let you be in charge!''{/i}":
                        jump razor_empty_opportunist_join

                    "{i}• ''Look, both of us are stuck here against our will. What if we joined forces?''{/i}":
                        label razor_empty_opportunist_join:
                            voice "audio/voices/ch3/razor/nexus/narrator/10.flac"
                            show razor2 r mull onlayer back
                            with dissolve
                            n "Oh for the love of... {i}sigh{/i}. The Princess stops for a moment, mulling over your deranged proposition.\n"
                            voice "audio/voices/ch3/razor/nexus/princess/7.flac"
                            show razor2 r happy talk onlayer back
                            with dissolve
                            sp "Nah! Not interested. And don't take it the wrong way! I think you're neat. But I'm having way too much fun to stop.\n"

                    "{i}• ''Has anyone ever told you how good you are at stabbing things?''{/i}":
                        voice "audio/voices/ch3/razor/nexus/princess/8.flac"
                        show razor2 r proud talk onlayer back
                        with dissolve
                        sp "Nope! But I don't need anyone to tell me that. I know I'm good at what I do! The best, I think.\n"
                        voice "audio/voices/ch3/razor/nexus/narrator/11.flac"
                        show razor2 r mull onlayer back
                        with dissolve
                        n "The Princess pauses for a moment to further ponder your ill-placed compliment.\n"
                        voice "audio/voices/ch3/razor/nexus/princess/42.flac"
                        show razor2 r impatient talk onlayer back
                        with dissolve
                        sp "Hey, what gives? Are you trying to get on my good side?\n"
                        show razor2 r impatient onlayer back
                        with dissolve
                        menu:
                            extend ""

                            "{i}• ''Yes! Yes I am. Did it work?''{/i}":
                                voice "audio/voices/ch3/razor/nexus/princess/10.flac"
                                show razor2 r happy talk onlayer back
                                with dissolve
                                sp "You're {i}already{/i} on my good side!\n"

                            "{i}• ''Psht. What? Me? I'm just stating facts.''{/i}":
                                voice "audio/voices/ch3/razor/nexus/princess/43.flac"
                                show razor2 r happy talk onlayer back
                                with dissolve
                                sp "And hey! They're good facts! Great facts! And for what it's worth, you're already on my good side.\n"

                            "{i}• [[Say nothing.]{/i}":
                                voice "audio/voices/ch3/razor/nexus/princess/12.flac"
                                show razor2 r happy talk onlayer back
                                with dissolve
                                sp "Well, for what it's worth, you're already on my good side!\n"

                        voice "audio/voices/ch3/razor/nexus/princess/13.flac"
                        show razor2 r chin offer talk onlayer back
                        with dissolve
                        sp "But that doesn't mean I'm going to not stab you. I'm having fun! Why would I stop?\n"

                voice "audio/voices/ch3/razor/nexus/contrarian/13.flac"
                show razor2 r chin offer onlayer back
                with dissolve
                contrarian "Is this what it's like dealing with me?\n"
                voice "audio/voices/ch3/razor/nexus/cheated/46.flac"
                cheated "Yeah. It is. You're the worst one of us. You know that, right?\n"
                if trait_broken:
                    voice "audio/voices/ch3/razor/nexus/broken/6.flac"
                    broken "We're screwed. Again. I'll see you all when we die.\n"
                    voice "audio/voices/ch3/razor/nexus/contrarian/14.flac"
                    contrarian "Really? I'm the worst one? Do you hear how whiny and un-fun he is?\n"
                if trait_paranoid:
                    # FAST
                    voice "audio/voices/ch3/razor/nexus/paranoid/22.flac"
                    paranoid "Don't rank us! The last thing we need is to be arguing with ourselves while—\n{w=4.20}{nw}"
                    show screen disableclick(0.5)
                voice "audio/voices/ch3/razor/nexus/narrator/51.flac"
                play audio "audio/final/__metal_run.flac"
                show razor2 r charge onlayer back
                with dissolve
                n "But you never finish that argument before the Princess closes the distance.\n"
                voice "audio/voices/ch3/razor/nexus/narrator/17.flac"
                stop music
                play audio "audio/final/Razor_ImpaleSwordBody_6.flac"
                hide bg onlayer back
                hide cg onlayer back
                hide razor2 onlayer back
                scene bg black
                n "She skewers you.\n"
                voice "audio/voices/ch3/razor/nexus/hero/5.flac"
                hero "Ow.\n"
                $ trait_opportunist = True
                voice "audio/voices/ch3/razor/nexus/opportunist/1a.flac"
                scene bg razor2 close onlayer back at Position(ypos=1125)
                show razor2 close enthusiastic onlayer front at Position(ypos=1125)
                with fade
                opportunist "Wow, she is absolutely uncompromising, isn't she? I know it seems weird, but if anything this makes me want her to like us even more.\n"

            "{i}• We're going to unconditionally surrender.{/i}" if trait_broken == False:
                voice "audio/voices/ch3/razor/nexus/contrarian/15.flac"
                contrarian "Ooh! That'll show her!\n"
                voice "audio/voices/ch3/razor/nexus/paranoid/23.flac"
                paranoid "Yeah. A bit of reverse psychology. I like it!\n"
                voice "audio/voices/ch3/razor/nexus/hero/23.flac"
                hero "How does unconditionally surrendering work for us? Does it have to be unanimous?\n"
                voice "audio/voices/ch3/razor/nexus/contrarian/16.flac"
                contrarian "I think it's up to the one making the decisions. We're really all just here in an advisory role.\n"
                voice "audio/voices/ch3/razor/nexus/cheated/47.flac"
                cheated "Let's see how it goes.\n"
                menu:
                    extend ""

                    "{i}• ''I give up. I'll do anything, just please don't stab me!''{/i}":
                        label razor_empty_surrender:
                            voice "audio/voices/ch3/razor/nexus/princess/44.flac"
                            show razor2 r finger wag talk anim onlayer back
                            with dissolve
                            sp "Surrendering, are we? Don't you know it takes two to stop a fight?\n"

                    "{i}• [[Silently throw your hands in the air.]{/i}":
                        voice "audio/voices/ch3/razor/nexus/narrator/52.flac"
                        n "You silently throw your hands in the air.\n"
                        jump razor_empty_surrender

                voice "audio/voices/ch3/razor/nexus/cheated/13.flac"
                play audio "audio/final/__metal_run.flac"
                show razor2 r charge onlayer back
                with dissolve
                cheated "Ah, shit.\n"
                voice "audio/voices/ch3/razor/nexus/narrator/53.flac"
                play audio "audio/final/Razor_ImpaleSwordBody_6.flac"
                stop music
                hide bg onlayer back
                hide cg onlayer back
                hide razor2 onlayer back
                scene bg black
                n "Before you can make another move, she skewers you.\n"
                voice "audio/voices/ch3/razor/nexus/hero/5.flac"
                hero "Ow.\n"
                $ trait_broken = True
                voice "audio/voices/ch3/razor/nexus/broken/22.flac"
                scene bg razor2 close onlayer back at Position(ypos=1125)
                show razor2 close enthusiastic onlayer front at Position(ypos=1125)
                with fade
                broken "We deserved it. Can't even surrender right.\n"

            "{i}• I'm going to go with not letting her stab us. We can dodge, right?{/i}" if trait_hunted == False:
                voice "audio/voices/ch3/razor/nexus/hero/24.flac"
                hero "Okay, that's not a bad idea.\n"
                voice "audio/voices/ch3/razor/nexus/contrarian/17.flac"
                contrarian "What are we going to do, tire her out?\n"
                voice "audio/voices/ch3/razor/nexus/hero/25.flac"
                hero "Maybe!\n"
                voice "audio/voices/ch3/razor/nexus/cheated/48.flac"
                cheated "And we'll learn how she moves. If we can keep ourselves alive, that's one step closer to getting through this.\n"
                if trait_broken:
                    voice "audio/voices/ch3/razor/nexus/broken/23.flac"
                    broken "It doesn't matter if she kills us. It's always going to be the same. This is what we deserve.\n"
                else:
                    voice "audio/voices/ch3/razor/nexus/paranoid/24.flac"
                    paranoid "We're not the only ones who can learn. For all we know, she's going to pick up on our movements faster than we can pick up on hers. She's been one step ahead of us since we got here.\n"
                voice "audio/voices/ch3/razor/nexus/narrator/54.flac"
                play audio "audio/final/__metal_run.flac"
                show razor2 r charge onlayer back
                with dissolve
                n "But you don't have time to bicker amongst yourselves forever. Knives out, she charges you.\n"
                voice "audio/voices/ch3/razor/nexus/narrator/55.flac"
                play audio "audio/final/Razor_SwordSwish_9.flac"
                hide razor2 onlayer back
                hide bg onlayer back
                show bg razor2 dodged onlayer farback at Position(ypos=1125)
                show panel1 razor2 unarmed dodge onlayer back at Position(ypos=1125)
                with Dissolve(1.0)
                n "And what do you know? You dodge her attack.\n"
                voice "audio/voices/ch3/razor/nexus/cheated/49.flac"
                cheated "And there we go! Yes.\n"
                voice "audio/voices/ch3/razor/nexus/narrator/56.flac"
                n "And then she attacks again.\n"
                voice "audio/voices/ch3/razor/nexus/cheated/50.flac"
                cheated "Hey wait a second.\n"
                voice "audio/voices/ch3/razor/nexus/narrator/57.flac"
                play audio "audio/final/Razor_SwordSwish_5.flac"
                show panel2 razor2 unarmed dodge onlayer front at Position(ypos=1125)
                with dissolve
                n "And you dodge again.\n"
                voice "audio/voices/ch3/razor/nexus/hero/26.flac"
                hero "Phew.\n"
                voice "audio/voices/ch3/razor/nexus/narrator/58.flac"
                play audio "audio/final/Razor_SwordSwish_2.flac"
                show panel3 razor2 unarmed dodge onlayer inyourface at Position(ypos=1125)
                with dissolve
                n "And she attacks again, barely missing you.\n"
                voice "audio/voices/ch3/razor/nexus/cheated/51.flac"
                cheated "Just how many attacks does she have?\n"
                voice "audio/voices/ch3/razor/nexus/princess/45.flac"
                show panel3 razor2 unarmed dodge talk onlayer inyourface at Position(ypos=1125)
                with dissolve
                sp "Do you really think you can dodge me forever? I have so many more moves than you can even imagine! And one of them's going to hit you.\n"
                if trait_broken:
                    voice "audio/voices/ch3/razor/nexus/broken/24.flac"
                    broken "We're doomed, aren't we?\n"
                else:
                    voice "audio/voices/ch3/razor/nexus/paranoid/25.flac"
                    paranoid "It's like she's in our head! What are we supposed to do?\n"
                # FAST
                voice "audio/voices/ch3/razor/nexus/narrator/59.flac"
                play audio "audio/final/den_emerge.flac"
                hide panel1 onlayer back
                hide panel2 onlayer front
                hide panel3 onlayer inyourface
                hide panel3 onlayer front
                hide bg onlayer back
                hide bg onlayer farback
                show bg razor2 close onlayer back at Position(ypos=1125)
                show cg razor2 punch counter onlayer front at Position(ypos=1125)
                with dissolve
                n "She attacks once more—\n{w=1.3}{nw}"
                show screen disableclick(0.5)
                voice "audio/voices/ch3/razor/nexus/cheated/52.flac"
                cheated "I don't like how you just changed the way you said it.\n"
                voice "audio/voices/ch3/razor/nexus/narrator/60.flac"
                play audio "audio/final/Razor_ImpaleSwordBody_6.flac"
                stop music
                hide cg onlayer front
                hide bg onlayer back
                hide cg onlayer back
                hide razor2 onlayer back
                scene bg black
                n "And she skewers you.\n"
                voice "audio/voices/ch3/razor/nexus/hero/5.flac"
                hero "Ow.\n"
                $ trait_hunted = True
                voice "audio/voices/ch3/razor/nexus/hunted/20.flac"
                scene bg razor2 close onlayer back at Position(ypos=1125)
                show razor2 close enthusiastic onlayer front at Position(ypos=1125)
                with fade
                hunted "I did my best.\n"

            "{i}• Oh, that's easy. I'm going to try flirting with her.{/i}" if trait_smitten == False:
                voice "audio/voices/ch3/razor/nexus/contrarian/18.flac"
                contrarian "Now {i}that{/i} is an interesting move.\n"
                voice "audio/voices/ch3/razor/nexus/narrator/61.flac"
                n "Interesting? It's disgusting. No, don't try romancing the Princess. She wants to kill you! She's going to end the world if you don't stop her.\n"
                voice "audio/voices/ch3/razor/nexus/hero/8.flac"
                hero "Yeah... do we have to flirt with the murderous monster?\n"
                voice "audio/voices/ch3/razor/nexus/contrarian/19.flac"
                contrarian "Of course we do! I'm into it. The one making the decisions is into it. Are you not?\n"
                voice "audio/voices/ch3/razor/nexus/hero/27.flac"
                hero "... I don't think so? I don't know.\n"
                voice "audio/voices/ch3/razor/nexus/cheated/53.flac"
                cheated "I could go either way, honestly.\n"
                if trait_broken:
                    voice "audio/voices/ch3/razor/nexus/broken/25.flac"
                    broken "She doesn't want us.\n"
                    voice "audio/voices/ch3/razor/nexus/contrarian/20.flac"
                    contrarian "You're just saying that because you want her to be into you.\n"
                    voice "audio/voices/ch3/razor/nexus/broken/26.flac"
                    broken "I know. I thought I was being obvious.\n"
                else:
                    voice "audio/voices/ch3/razor/nexus/paranoid/9.flac"
                    paranoid "Maybe it'll work! Maybe it'll throw her off. I know I'd be thrown off if she started flirting with us.\n"
                    voice "audio/voices/ch3/razor/nexus/contrarian/21.flac"
                    contrarian "Yeah, because you'd be into it.\n"
                    voice "audio/voices/ch3/razor/nexus/paranoid/26.flac"
                    paranoid "No comment.\n"
                menu:
                    extend ""

                    "{i}• ''I know you want to kill me, but has anyone ever told you how gorgeous you are?''{/i}":
                        voice "audio/voices/ch3/razor/nexus/narrator/24.flac"
                        show razor2 r blush onlayer back
                        with dissolve
                        n "A rosy blush flushes in the Princess' cheeks, and a wide grin cuts across her face.\n"
                        voice "audio/voices/ch3/razor/nexus/princess/17.flac"
                        show razor2 r blush talk onlayer back
                        with dissolve
                        sp "You're the only person I know, so that's a first! You're sweet! I like you! You're also gorgeous!\n"
                        voice "audio/voices/ch3/razor/nexus/cheated/17.flac"
                        show razor2 r blush onlayer back
                        with dissolve
                        cheated "I'll be damned. This is actually going to work, isn't it?\n"
                        voice "audio/voices/ch3/razor/nexus/princess/18.flac"
                        show razor2 r blush serious talk onlayer back
                        with dissolve
                        sp "Still gonna kill you though.\n"

                    "{i}• ''I just feel like I really get you. I like you. Romantically, even. Maybe we can hash this out over a date.''{/i}":
                        voice "audio/voices/ch3/razor/nexus/narrator/24.flac"
                        show razor2 r blush onlayer back
                        with dissolve
                        n "A rosy blush flushes in the Princess' cheeks, and a wide grin cuts across her face.\n"
                        voice "audio/voices/ch3/razor/nexus/princess/19.flac"
                        show razor2 r blush talk onlayer back
                        with dissolve
                        sp "You're sweet! I like you too! You're probably my favorite person other than me.\n"
                        voice "audio/voices/ch3/razor/nexus/cheated/17.flac"
                        show razor2 r blush onlayer back
                        with dissolve
                        cheated "I'll be damned. This is actually going to work, isn't it?\n"
                        voice "audio/voices/ch3/razor/nexus/princess/18.flac"
                        show razor2 r blush serious talk onlayer back
                        with dissolve
                        sp "Still gonna kill you though.\n"

                    "{i}• ''How about you buy me dinner before impaling me to death?''{/i}":
                        voice "audio/voices/ch3/razor/nexus/narrator/24.flac"
                        show razor2 r blush onlayer back
                        with dissolve
                        n "A rosy blush flushes in the Princess' cheeks, and a wide grin cuts across her face.\n"
                        voice "audio/voices/ch3/razor/nexus/princess/20.flac"
                        show razor2 r blush talk onlayer back
                        with dissolve
                        sp "Oh? Is that how it is? Yeah okay I feel that. I like you too.\n"
                        voice "audio/voices/ch3/razor/nexus/cheated/17.flac"
                        show razor2 r blush onlayer back
                        with dissolve
                        cheated "I'll be damned. This is actually going to work, isn't it?\n"
                        voice "audio/voices/ch3/razor/nexus/princess/21.flac"
                        show razor2 r blush serious talk onlayer back
                        with dissolve
                        sp "But why mess around with appetizers when the main course is right here?\n"

                    "{i}• [[Give her {b}The Look{/b}.]{/i}":
                        voice "audio/voices/ch3/razor/nexus/hero/9.flac"
                        hero "{i}The Look{/i}?\n"
                        voice "audio/voices/ch3/razor/nexus/contrarian/22.flac"
                        contrarian "Yeah. The best flirts know how to flirt without saying anything. We just have to let her know, right?\n"
                        voice "audio/voices/ch3/razor/nexus/narrator/25.flac"
                        n "{i}Sigh{/i}. You flash the Princess {i}The Look{/i}.\n"
                        voice "audio/voices/ch3/razor/nexus/narrator/26.flac"
                        show razor2 r blush onlayer back
                        with dissolve
                        n "... And a rosy blush rushes to the Princess' cheeks as she breaks into a wide grin. Unbelievable.\n"
                        voice "audio/voices/ch3/razor/nexus/princess/22.flac"
                        show razor2 r blush talk onlayer back
                        with dissolve
                        sp "Oh? Is that how it is? Yeah okay I feel that. I like you too. Neat!\n"
                        voice "audio/voices/ch3/razor/nexus/cheated/17.flac"
                        show razor2 r blush onlayer back
                        with dissolve
                        cheated "I'll be damned. This is actually going to work, isn't it?\n"
                        voice "audio/voices/ch3/razor/nexus/princess/23.flac"
                        show razor2 r blush serious talk onlayer back
                        with dissolve
                        sp "Still going to kill you, but now we can both enjoy a mutual romantic subtext to the murder.\n"

                $ gallery_razor.unlock_item(10)
                $ renpy.save_persistent()
                voice "audio/voices/ch3/razor/nexus/hero/10.flac"
                play audio "audio/final/__metal_run.flac"
                show razor2 r blush charge onlayer back
                with dissolve
                hero "Or not.\n"
                if trait_broken:
                    voice "audio/voices/ch3/razor/nexus/broken/11.flac"
                    broken "At least she likes us. I've never been liked before.\n"
                elif trait_paranoid:
                    voice "audio/voices/ch3/razor/nexus/paranoid/11.flac"
                    paranoid "Is anything going to work with her? She's so single minded. It's like whatever we do it's always going to end exactly the same.\n"
                voice "audio/voices/ch3/razor/nexus/narrator/62.flac"
                play audio "audio/final/Razor_ImpaleSwordBody_6.flac"
                stop music
                hide bg onlayer back
                hide cg onlayer back
                hide razor2 onlayer back
                scene bg black
                n "Blush still glowing in her cheeks, the Princess closes the distance between you and skewers you.\n"
                voice "audio/voices/ch3/razor/nexus/hero/5.flac"
                hero "Ow.\n"
                $ trait_smitten = True
                voice "audio/voices/ch3/razor/nexus/smitten/1.flac"
                scene bg razor2 close onlayer back at Position(ypos=1125)
                show razor2 close enthusiastic onlayer front at Position(ypos=1125)
                with fade
                smitten "What worthwhile romance doesn't hurt at least a little bit? What matters is that she likes us. She's even said as much!\n"

            "{i}• She has swords for arms and we don't. We're panicking!{/i}" if trait_paranoid == False:
                voice "audio/voices/ch3/razor/nexus/hero/28.flac"
                hero "What, and run back up the slide that dropped us down here?\n"
                voice "audio/voices/ch3/razor/nexus/princess/24.flac"
                show razor2 r chin offer talk onlayer back
                with dissolve
                sp "I'm coming to get you!\n" id razor_empty_surrender_91c11421
                voice "audio/voices/ch3/razor/nexus/contrarian/23.flac"
                contrarian "Nah, I'm with the decider. It defeats the whole point of panicking if we think about what we're doing, and I don't know if you've been listening, but she's coming to get us! So panic! Give in to the chaos!\n"
                voice "audio/voices/ch3/razor/nexus/broken/27.flac"
                broken "Oh yes, the chaos of dying. How fun.\n"
                voice "audio/voices/ch3/razor/nexus/cheated/54.flac"
                cheated "Stop whining and do it!\n"
                voice "audio/voices/ch3/razor/nexus/narrator/63.flac"
                play audio "audio/final/__metal_run.flac"
                show razor2 r charge onlayer back
                with dissolve
                n "You panic, but unsurprisingly, panicking doesn't save you from her blades.\n"
                voice "audio/voices/ch3/razor/nexus/narrator/17.flac"
                play audio "audio/final/Razor_ImpaleSwordBody_6.flac"
                stop music
                hide bg onlayer back
                hide cg onlayer back
                hide razor2 onlayer back
                scene bg black
                n "She skewers you.\n"
                voice "audio/voices/ch3/razor/nexus/hero/5.flac"
                hero "Ow.\n"
                $ trait_paranoid = True
                voice "audio/voices/ch3/razor/nexus/paranoid/12.flac"
                scene bg razor2 close onlayer back at Position(ypos=1125)
                show razor2 close enthusiastic onlayer front at Position(ypos=1125)
                with fade
                paranoid "Sorry about that. I gave into a bit of a fear response there, and I don't think it was very helpful.\n"

            "{i}• We're going to let her stab us, and we're going to have a stiff upper lip about it. She can't hurt us if we don't let ourselves feel it.{/i}" if trait_cold == False:
                voice "audio/voices/ch3/razor/nexus/contrarian/24.flac"
                contrarian "That is the worst plan I've ever heard, and I absolute love it. Let's try it out.\n" id razor_empty_surrender_15222e76
                voice "audio/voices/ch3/razor/nexus/cheated/55.flac"
                cheated "Sure! Why the hell not! Let's see if we can turn off the part of us that feels things.\n"
                if trait_broken:
                    voice "audio/voices/ch3/razor/nexus/broken/13.flac"
                    broken "I turned that off ages ago.\n"
                    voice "audio/voices/ch3/razor/nexus/contrarian/1.flac"
                    contrarian "If you'd managed to do that, you wouldn't be such a whiner.\n"
                elif trait_paranoid:
                    voice "audio/voices/ch3/razor/nexus/paranoid/13.flac"
                    paranoid "If we can't feel things, then how are we supposed to know what's true?\n"
                    voice "audio/voices/ch3/razor/nexus/narrator/29.flac"
                    n "You could always just trust what I tell you.\n"
                    voice "audio/voices/ch3/razor/nexus/cheated/22.flac"
                    cheated "Ha! No.\n"
                menu:
                    extend ""

                    "{i}• ''Do your worst! I bet you can't even hurt me.''{/i}":
                        voice "audio/voices/ch3/razor/nexus/princess/25.flac"
                        show razor2 r happy talk onlayer back
                        with dissolve
                        sp "Sure thing! I love a challenge. I bet I can hurt you {i}so much{/i}!\n"

                    "{i}• [[Silently let her stab you.]{/i}":
                        voice "audio/voices/ch3/razor/nexus/princess/26.flac"
                        show razor2 r chin offer talk onlayer back
                        with dissolve
                        sp "Just standing there, huh? A bold strategy.\n"

                voice "audio/voices/ch3/razor/nexus/narrator/64.flac"
                play audio "audio/final/__metal_run.flac"
                show razor2 r charge onlayer back
                with dissolve
                n "The Princess rapidly closes the distance.\n"
                voice "audio/voices/ch3/razor/nexus/narrator/22.flac"
                play audio "audio/final/Razor_ImpaleSwordBody_6.flac"
                stop music
                hide bg onlayer back
                hide cg onlayer back
                hide razor2 onlayer back
                scene bg black
                n "And then she skewers you.\n"
                voice "audio/voices/ch3/razor/nexus/hero/14.flac"
                hero "And? Does it hurt?\n"
                $ trait_cold = True
                voice "audio/voices/ch3/razor/nexus/cold/1.flac"
                scene bg razor2 close onlayer back at Position(ypos=1125)
                show razor2 close enthusiastic onlayer front at Position(ypos=1125)
                with fade
                cold "No.\n"

            "{i}• [[All of these ideas suck. Think up something better.]{/i}" if trait_skeptic == False:
                voice "audio/voices/ch3/razor/nexus/cheated/27a.flac"
                cheated "Yeah, that's right. We just have to think. There's probably an answer if we think.\n"
                voice "audio/voices/ch3/razor/nexus/princess/26.flac"
                show razor2 r chin offer talk onlayer back
                with dissolve
                sp "Just standing there, huh? A bold strategy.\n"
                voice "audio/voices/ch3/razor/nexus/narrator/65.flac"
                play audio "audio/final/__metal_run.flac"
                show razor2 r charge onlayer back
                with dissolve
                n "But you don't have time to finish your thought before she closes the distance.\n"
                voice "audio/voices/ch3/razor/nexus/narrator/22.flac"
                play audio "audio/final/Razor_ImpaleSwordBody_6.flac"
                stop music
                hide bg onlayer back
                hide cg onlayer back
                hide razor2 onlayer back
                scene bg black
                n "And then she skewers you.\n"
                voice "audio/voices/ch3/razor/nexus/hero/5.flac"
                hero "Ow.\n"
                voice "audio/voices/ch3/razor/nexus/cheated/28.flac"
                cheated "What a surprise.\n"
                $ trait_skeptic = True
                voice "audio/voices/ch3/razor/nexus/skeptic/1.flac"
                scene bg razor2 close onlayer back at Position(ypos=1125)
                show razor2 close enthusiastic onlayer front at Position(ypos=1125)
                with fade
                skeptic "Yeah. We don't even get a second to think without her stabbing us.\n"

label razor_2_unarmed_beat_2:

    voice "audio/voices/ch3/razor/nexus/hero/16.flac"
    hero "Oh! A new one of us.\n"
    voice "audio/voices/ch3/razor/nexus/cheated/29.flac"
    cheated "I thought that only happens when we die. Did we die?\n"
    voice "audio/voices/ch3/razor/nexus/contrarian/3a.flac"
    contrarian "Nah, we'd {i}know{/i} if we died... right?\n"
    voice "audio/voices/ch3/razor/nexus/narrator/41.flac"
    play music "audio/_music/ch2/razor/The Razor Fast.flac" loop
    n "You're on a— no, you're in a— where the hell are you?\n"
    if trait_paranoid:
        voice "audio/voices/ch3/razor/nexus/paranoid/15.flac"
        paranoid "We're dead, aren't we? We're {i}dead{/i} dead. How long have we been dead? Have we been dead the whole time?\n"
        if trait_broken:
            voice "audio/voices/ch3/razor/nexus/broken/15.flac"
            broken "Dead dead dead dead dead.\n"
    elif trait_broken:
        voice "audio/voices/ch3/razor/nexus/broken/16.flac"
        broken "I think we're dead. And that's all we'll ever be. Dead dead dead dead dead.\n"
    else:
        voice "audio/voices/ch3/razor/nexus/hero/_extra2.flac"
        hero "I don't like that we died without us knowing it. This really, really blurs some lines that I prefer not be blurred. Are we still dead? Are we alive again? How are we even supposed to know the difference?\n"
    if trait_cold:
        voice "audio/voices/ch3/razor/nexus/cold/2.flac"
        cold "If we didn't realize we were dead, then we made progress. Good job.\n"
    voice "audio/voices/ch3/razor/nexus/cheated/30.flac"
    cheated "Stop saying dead, all of you! We might have died a second ago, but right now we're extremely not dead.\n"
    voice "audio/voices/ch3/razor/nexus/narrator/42.flac"
    n "This is all horribly wrong. How many times have you been here?\n"
    voice "audio/voices/ch3/razor/nexus/contrarian/25.flac"
    contrarian "I don't actually know how to answer that question.\n"
    voice "audio/voices/ch3/razor/nexus/hero/29.flac"
    hero "I think he means how many times have we died.\n"
    voice "audio/voices/ch3/razor/nexus/narrator/66.flac"
    n "Yes. That.\n"
    voice "audio/voices/ch3/razor/nexus/contrarian/26.flac"
    contrarian "Oh, I've lost count to be honest.\n"
    voice "audio/voices/ch3/razor/nexus/cheated/56a.flac"
    cheated "I haven't. It's four.\n"
    voice "audio/voices/ch3/razor/nexus/narrator/43.flac"
    n "No wonder everything's such a mess. This wasn't supposed to go past one.\n"
    voice "audio/voices/ch3/razor/nexus/princess/46.flac"
    show razor2 close neutral talk onlayer front
    with dissolve
    sp "I wonder what you're going to do next! You're so full of ideas and I love that!\n"
    voice "audio/voices/ch3/razor/nexus/narrator/44.flac"
    play audio "audio/final/__metal_step.flac"
    show razor2 close neutral onlayer front at spectre_small_zoom
    with dissolve
    n "But I guess we don't have time to talk about things before the Princess advances.\n"
    voice "audio/voices/ch3/razor/nexus/cheated/31.flac"
    cheated "Okay. Whatever we do gets us another... us. Let's see how many we can stack. There's got to be a point where it makes us better than her.\n"
    if trait_stubborn:
        voice "audio/voices/ch3/razor/nexus/stubborn/20.flac"
        stubborn "You don't need any others. We just have to keep pushing!\n"
        voice "audio/voices/ch3/razor/nexus/cheated/32.flac"
        cheated "Yeah, I'll pass on that.\n"
    if trait_hunted:
        voice "audio/voices/ch3/razor/nexus/hunted/19.flac"
        hunted "As long as we keep moving.\n"
    if trait_cold:
        voice "audio/voices/ch3/razor/nexus/cold/3.flac"
        cold "Why not? It's not like dying again and again is doing us any harm. Let's see how far this little mind-hole goes, shall we?\n"
    if trait_smitten:
        voice "audio/voices/ch3/razor/nexus/smitten/2.flac"
        smitten "We'll win her heart eventually!\n"
    if trait_paranoid and razor_paranoid_intro == False:
        $ razor_paranoid_intro = True
        voice "audio/voices/ch3/razor/nexus/paranoid/16.flac"
        paranoid "It's going to get so loud in here. How are we going to keep it all straight?\n"
    if trait_broken and razor_broken_intro == False:
        $ razor_broken_intro = True
        voice "audio/voices/ch3/razor/nexus/broken/17.flac"
        broken "Oh, great. So it's going to get even more crowded. Even more deluded voices that think we might stand any kind of chance.\n"
    if trait_opportunist:
        voice "audio/voices/ch3/razor/nexus/opportunist/2.flac"
        opportunist "Flawless idea if you ask me. Such a go-getter attitude!\n"
        #and this one, those were good ones
    voice "audio/voices/ch3/razor/nexus/princess/31.flac"
    show razor2 close impatient talk onlayer front at spectre_small_zoom_instant
    with dissolve
    sp "Come onnnnnn! Show me something new!\n"
    show razor2 close impatient onlayer front at spectre_small_zoom_instant
    with dissolve
    if trait_skeptic:
        voice "audio/voices/ch3/razor/nexus/skeptic/2.flac"
        skeptic "Okay. Plan. Now!\n"
    menu:
        extend ""

        "{i}• We're fighting her, obviously.{/i}" if trait_stubborn == False:
            hide bg onlayer back
            hide razor2 onlayer back
            hide razor2 onlayer front
            show bg razor2 dodged onlayer farback at Position(ypos=1125)
            with Dissolve(1.0)
            truthmid "It doesn't work, and she kills you again. And again, and again, and again. Your memory blurs as your consciousness leaps from life to life to life, holding only snippets of the conflict that transpires.\n"
            $ trait_stubborn = True
            voice "audio/voices/ch3/razor/nexus/stubborn/18.flac"
            play audio "audio/final/Razor_SwordJUSTdrag_7.flac"
            show montage1 razor unarmed onlayer back at Position(ypos=1125)
            with dissolve
            stubborn "We just have to hit her harder!\n"
            voice "audio/voices/ch3/razor/nexus/narrator/skewer1.flac"
            play audio "audio/final/Razor_ImpaleSwordBody_3.flac"
            n "She skewers you.\n"
            jump razor_2_unarmed_montage

        "{i}• We're going to appeal to her authority. Puff her up a bit. There's no reason we can't talk this out.{/i}" if trait_opportunist == False:
            hide bg onlayer back
            hide razor2 onlayer front
            hide razor2 onlayer back
            show bg razor2 dodged onlayer farback at Position(ypos=1125)
            with Dissolve(1.0)
            truthmid "It doesn't work, and she kills you again. And again, and again, and again. Your memory blurs as your consciousness leaps from life to life to life, holding only snippets of the conflict that transpires.\n"
            $ trait_opportunist = True
            voice "audio/voices/ch3/razor/nexus/opportunist/3.flac"
            play audio "audio/final/Razor_SwordJUSTdrag_3.flac"
            show montage1 razor unarmed onlayer back at Position(ypos=1125)
            with dissolve
            opportunist "Let's appeal to her better nature! We haven't tried that. I'm sure she'll listen to reason.\n"
            voice "audio/voices/ch3/razor/nexus/narrator/17.flac"
            play audio "audio/final/Razor_ImpaleSwordBody_3.flac"
            n "She skewers you.\n"
            jump razor_2_unarmed_montage

        "{i}• We're going to unconditionally surrender.{/i}" if trait_broken == False:
            hide bg onlayer back
            hide razor2 onlayer back
            hide razor2 onlayer front
            show bg razor2 dodged onlayer farback at Position(ypos=1125)
            with Dissolve(1.0)
            truthmid "It doesn't work, and she kills you again. And again, and again, and again. Your memory blurs as your consciousness leaps from life to life to life, holding only snippets of the conflict that transpires.\n"
            $ trait_broken = True
            voice "audio/voices/ch3/razor/nexus/broken/18.flac"
            play audio "audio/final/Razor_SwordJUSTdrag_4.flac"
            show montage1 razor unarmed onlayer back at Position(ypos=1125)
            with dissolve
            broken "What's the point? It's all the same.\n"
            voice "audio/voices/ch3/razor/nexus/narrator/skewer2.flac"
            play audio "audio/final/Razor_ImpaleSwordBody_3.flac"
            n "She skewers you.\n"
            voice "audio/voices/ch3/razor/nexus/princess/33.flac"
            show montage1 razor unarmed talk onlayer back at Position(ypos=1125)
            with dissolve
            sp "Oh, don't give up on me just yet! You gotta keep going!\n"
            jump razor_2_unarmed_montage

        "{i}• I'm going to go with not letting her stab us. We can dodge, right?{/i}" if trait_hunted == False:
            hide bg onlayer back
            hide razor2 onlayer back
            hide razor2 onlayer front
            show bg razor2 dodged onlayer farback at Position(ypos=1125)
            with Dissolve(1.0)
            truthmid "It doesn't work, and she kills you again. And again, and again, and again. Your memory blurs as your consciousness leaps from life to life to life, holding only snippets of the conflict that transpires.\n"
            $ trait_hunted = True
            voice "audio/voices/ch3/razor/nexus/hunted/21.flac"
            play audio "audio/final/Razor_SwordJUSTdrag_2.flac"
            show montage1 razor unarmed onlayer back at Position(ypos=1125)
            with dissolve
            hunted "Just keep dodging. Just keep dodging. Just keep dodging.\n"
            voice "audio/voices/ch3/razor/nexus/narrator/skewer3.flac"
            play audio "audio/final/Razor_ImpaleSwordBody_3.flac"
            n "She skewers you.\n"
            voice "audio/voices/ch3/razor/nexus/princess/47.flac"
            show montage1 razor unarmed talk onlayer back at Position(ypos=1125)
            with dissolve
            sp "What's the point of avoiding me if you're not going to fight.\n"
            jump razor_2_unarmed_montage

        "{i}• Oh, that's easy. I'm going to try flirting with her.{/i}" if trait_smitten == False:
            hide bg onlayer back
            hide razor2 onlayer back
            hide razor2 onlayer front
            show bg razor2 dodged onlayer farback at Position(ypos=1125)
            with Dissolve(1.0)
            truthmid "It doesn't work, and she kills you again. And again, and again, and again. Your memory blurs as your consciousness leaps from life to life to life, holding only snippets of the conflict that transpires.\n"
            $ trait_smitten = True
            voice "audio/voices/ch3/razor/nexus/smitten/3.flac"
            play audio "audio/final/Razor_SwordJUSTdrag_1.flac"
            show montage1 razor unarmed onlayer back at Position(ypos=1125)
            with dissolve
            smitten "Compliment her on those gleaming blades! There's nothing better than a capable woman.\n"
            voice "audio/voices/ch3/razor/nexus/narrator/skewer4.flac"
            play audio "audio/final/Razor_ImpaleSwordBody_3.flac"
            n "She skewers you.\n"
            voice "audio/voices/ch3/razor/nexus/princess/35.flac"
            show montage1 razor unarmed talk onlayer back at Position(ypos=1125)
            with dissolve
            sp "You're cute.\n"
            jump razor_2_unarmed_montage

        "{i}• She has swords for arms and we don't. We're panicking!{/i}" if trait_paranoid == False:
            hide bg onlayer back
            hide razor2 onlayer back
            hide razor2 onlayer front
            show bg razor2 dodged onlayer farback at Position(ypos=1125)
            with Dissolve(1.0)
            truthmid "It doesn't work, and she kills you again. And again, and again, and again. Your memory blurs as your consciousness leaps from life to life to life, holding only snippets of the conflict that transpires.\n"
            $ trait_paranoid = True
            voice "audio/voices/ch3/razor/nexus/paranoid/17.flac"
            play audio "audio/final/Razor_SwordJUSTdrag_4.flac"
            show montage1 razor unarmed onlayer back at Position(ypos=1125)
            with dissolve
            paranoid "Just panic! Flee!\n"
            voice "audio/voices/ch3/razor/nexus/narrator/skewer5.flac"
            play audio "audio/final/Razor_ImpaleSwordBody_3.flac"
            n "She skewers you.\n"
            voice "audio/voices/ch3/razor/nexus/princess/36.flac"
            show montage1 razor unarmed talk onlayer back at Position(ypos=1125)
            with dissolve
            sp "No, you don't get to escape! That's not how this works.\n"
            jump razor_2_unarmed_montage

        "{i}• We're going to let her stab us, and we're going to have a stiff upper lip about it. She can't hurt us if we don't let ourselves feel it.{/i}" if trait_cold == False:
            hide bg onlayer back
            hide razor2 onlayer back
            hide razor2 onlayer front
            show bg razor2 dodged onlayer farback at Position(ypos=1125)
            with Dissolve(1.0)
            truthmid "It doesn't work, and she kills you again. And again, and again, and again. Your memory blurs as your consciousness leaps from life to life to life, holding only snippets of the conflict that transpires.\n"
            $ trait_cold = True
            voice "audio/voices/ch3/razor/nexus/cold/4.flac"
            play audio "audio/final/Razor_SwordJUSTdrag_2.flac"
            show montage1 razor unarmed onlayer back at Position(ypos=1125)
            with dissolve
            cold "She's going to kill this body either way. So stop feeling what it feels.\n"
            voice "audio/voices/ch3/razor/nexus/narrator/skewer6.flac"
            play audio "audio/final/Razor_ImpaleSwordBody_3.flac"
            n "She skewers you.\n"
            voice "audio/voices/ch3/razor/nexus/princess/37.flac"
            show montage1 razor unarmed talk onlayer back at Position(ypos=1125)
            with dissolve
            sp "Ooooh. Not bad! Real tough!\n"
            jump razor_2_unarmed_montage

        "{i}• [[All of these ideas suck. Think up something better.]{/i}" if trait_skeptic == False:
            hide bg onlayer back
            hide razor2 onlayer back
            hide razor2 onlayer front
            show bg razor2 dodged onlayer farback at Position(ypos=1125)
            with Dissolve(1.0)
            truthmid "It doesn't work, and she kills you again. And again, and again, and again. Your memory blurs as your consciousness leaps from life to life to life, holding only snippets of the conflict that transpires.\n"
            $ trait_skeptic = True
            voice "audio/voices/ch3/razor/nexus/skeptic/3.flac"
            play audio "audio/final/Razor_SwordJUSTdrag_5.flac"
            show montage1 razor unarmed onlayer back at Position(ypos=1125)
            skeptic "None of this is working! Think. Think!\n"
            voice "audio/voices/ch3/razor/nexus/narrator/skewer7.flac"
            play audio "audio/final/Razor_ImpaleSwordBody_3.flac"
            n "She skewers you.\n"
            jump razor_2_unarmed_montage

    label razor_2_unarmed_montage:
        $ razor_montage_panel_number = 1
        label razor_2_unarmed_montage_loop:
            if razor_loop <= 5:
                $ razor_montage_panel_number += 1
                $ razor_loop += 1
                if razor_loop == 1:
                    voice "audio/voices/ch3/razor/nexus/cheated/33.flac"
                    cheated "Well, there's more of us. Let's see if that helps.\n"

                if razor_loop == 2:
                    voice "audio/voices/ch3/razor/nexus/hero/30.flac"
                    hero "More noise isn't helping. It's just making it harder to focus.\n"

                if razor_loop == 3:
                    voice "audio/voices/ch3/razor/nexus/cheated/36.flac"
                    cheated "It doesn't matter how many times this takes. We can't give up.\n"
                    voice "audio/voices/ch3/razor/nexus/hero/31.flac"
                    hero "We don't even have a weapon.\n"
                    voice "audio/voices/ch3/razor/nexus/contrarian/27.flac"
                    contrarian "Yeah. Some clod threw it out the window.\n"
                    voice "audio/voices/ch3/razor/nexus/hero/32.flac"
                    hero "Again. That was you!\n"
                    voice "audio/voices/ch3/razor/nexus/contrarian/28.flac"
                    contrarian "No, I was just the clod who suggested it. And if I knew we'd be stuck here forever, I wouldn't have done that.\n"

                if razor_loop == 4:
                    voice "audio/voices/ch3/razor/nexus/cheated/57.flac"
                    cheated "See? We lasted a little longer.\n"
                    voice "audio/voices/ch3/razor/nexus/hero/33.flac"
                    hero "Barely.\n"

                if razor_loop == 5:
                    voice "audio/voices/ch3/razor/nexus/cheated/38.flac"
                    cheated "We're getting close to something, can't you feel it? One. Last. Time.\n"
                    voice "audio/voices/ch3/razor/nexus/hero/34.flac"
                    hero "Fine. One last time.\n"


                if trait_stubborn == False:
                    $ trait_stubborn = True
                    voice "audio/voices/ch3/razor/nexus/stubborn/18.flac"
                    play audio "audio/final/Razor_SwordSwish_1.flac"
                    if razor_montage_panel_number == 2:
                        show montage2 razor unarmed onlayer back
                        with dissolve
                    elif razor_montage_panel_number == 3:
                        show montage3 razor unarmed onlayer front
                        with dissolve
                    elif razor_montage_panel_number == 4:
                        show montage4 razor unarmed onlayer front
                        with dissolve
                    elif razor_montage_panel_number == 5:
                        show montage5 razor unarmed onlayer inyourface
                        with dissolve
                    elif razor_montage_panel_number == 6:
                        show montage6 razor unarmed onlayer inyourface
                        with dissolve
                    stubborn "We just have to hit her harder!\n"
                    voice "audio/voices/ch3/razor/nexus/narrator/skewer1.flac"
                    play audio "audio/final/Razor_ImpaleSwordBody_1.flac"
                    n "She skewers you.\n"

                elif trait_broken == False:
                    $ trait_broken = True
                    voice "audio/voices/ch3/razor/nexus/broken/18.flac"
                    broken "What's the point? It's all the same.\n"
                    voice "audio/voices/ch3/razor/nexus/narrator/skewer2.flac"
                    play audio "audio/final/Razor_SwordSwish_2.flac"
                    if razor_montage_panel_number == 2:
                        show montage2 razor unarmed onlayer back
                        with dissolve
                    elif razor_montage_panel_number == 3:
                        show montage3 razor unarmed onlayer front
                        with dissolve
                    elif razor_montage_panel_number == 4:
                        show montage4 razor unarmed onlayer front
                        with dissolve
                    elif razor_montage_panel_number == 5:
                        show montage5 razor unarmed onlayer inyourface
                        with dissolve
                    elif razor_montage_panel_number == 6:
                        show montage6 razor unarmed onlayer inyourface
                        with dissolve
                    play audio "audio/final/Razor_ImpaleSwordBody_2.flac"
                    n "She skewers you.\n"
                    voice "audio/voices/ch3/razor/nexus/princess/33.flac"
                    if razor_montage_panel_number == 2:
                        show montage2 razor unarmed talk onlayer back
                        with dissolve
                    elif razor_montage_panel_number == 3:
                        show montage3 razor unarmed talk onlayer front
                        with dissolve
                    elif razor_montage_panel_number == 4:
                        show montage4 razor unarmed  talk onlayer front
                        with dissolve
                    elif razor_montage_panel_number == 5:
                        show montage5 razor unarmed talk onlayer inyourface
                        with dissolve
                    elif razor_montage_panel_number == 6:
                        show montage6 razor unarmed talk onlayer inyourface
                        with dissolve
                    sp "Oh, don't give up on me just yet! You gotta keep going!\n"

                elif trait_hunted == False:
                    $ trait_hunted = True
                    voice "audio/voices/ch3/razor/nexus/hunted/21.flac"
                    play audio "audio/final/Razor_SwordSwish_3.flac"
                    if razor_montage_panel_number == 2:
                        show montage2 razor unarmed onlayer back
                        with dissolve
                    elif razor_montage_panel_number == 3:
                        show montage3 razor unarmed onlayer front
                        with dissolve
                    elif razor_montage_panel_number == 4:
                        show montage4 razor unarmed onlayer front
                        with dissolve
                    elif razor_montage_panel_number == 5:
                        show montage5 razor unarmed onlayer inyourface
                        with dissolve
                    elif razor_montage_panel_number == 6:
                        show montage6 razor unarmed onlayer inyourface
                        with dissolve
                    hunted "Just keep dodging. Just keep dodging. Just keep dodging.\n"
                    voice "audio/voices/ch3/razor/nexus/narrator/skewer3.flac"
                    play audio "audio/final/Razor_ImpaleSwordBody_3.flac"
                    n "She skewers you.\n"
                    voice "audio/voices/ch3/razor/nexus/princess/47.flac"
                    if razor_montage_panel_number == 2:
                        show montage2 razor unarmed talk onlayer back
                        with dissolve
                    elif razor_montage_panel_number == 3:
                        show montage3 razor unarmed talk onlayer front
                        with dissolve
                    elif razor_montage_panel_number == 4:
                        show montage4 razor unarmed  talk onlayer front
                        with dissolve
                    elif razor_montage_panel_number == 5:
                        show montage5 razor unarmed talk onlayer inyourface
                        with dissolve
                    elif razor_montage_panel_number == 6:
                        show montage6 razor unarmed talk onlayer inyourface
                        with dissolve
                    sp "What's the point of avoiding me if you're not going to fight.\n"

                elif trait_smitten == False:
                    $ trait_smitten = True
                    voice "audio/voices/ch3/razor/nexus/smitten/3.flac"
                    play audio "audio/final/Razor_SwordSwish_4.flac"
                    if razor_montage_panel_number == 2:
                        show montage2 razor unarmed onlayer back
                        with dissolve
                    elif razor_montage_panel_number == 3:
                        show montage3 razor unarmed onlayer front
                        with dissolve
                    elif razor_montage_panel_number == 4:
                        show montage4 razor unarmed onlayer front
                        with dissolve
                    elif razor_montage_panel_number == 5:
                        show montage5 razor unarmed onlayer inyourface
                        with dissolve
                    elif razor_montage_panel_number == 6:
                        show montage6 razor unarmed onlayer inyourface
                        with dissolve
                    smitten "Compliment her on those gleaming blades! There's nothing better than a capable woman.\n"
                    voice "audio/voices/ch3/razor/nexus/narrator/skewer4.flac"
                    play audio "audio/final/Razor_ImpaleSwordBody_4.flac"
                    n "She skewers you.\n"
                    voice "audio/voices/ch3/razor/nexus/princess/35.flac"
                    if razor_montage_panel_number == 2:
                        show montage2 razor unarmed talk onlayer back
                        with dissolve
                    elif razor_montage_panel_number == 3:
                        show montage3 razor unarmed talk onlayer front
                        with dissolve
                    elif razor_montage_panel_number == 4:
                        show montage4 razor unarmed  talk onlayer front
                        with dissolve
                    elif razor_montage_panel_number == 5:
                        show montage5 razor unarmed talk onlayer inyourface
                        with dissolve
                    elif razor_montage_panel_number == 6:
                        show montage6 razor unarmed talk onlayer inyourface
                        with dissolve
                    sp "You're cute.\n"

                elif trait_paranoid == False:
                    $ trait_paranoid = True
                    voice "audio/voices/ch3/razor/nexus/paranoid/17.flac"
                    play audio "audio/final/Razor_SwordSwish_5.flac"
                    if razor_montage_panel_number == 2:
                        show montage2 razor unarmed onlayer back
                        with dissolve
                    elif razor_montage_panel_number == 3:
                        show montage3 razor unarmed onlayer front
                        with dissolve
                    elif razor_montage_panel_number == 4:
                        show montage4 razor unarmed onlayer front
                        with dissolve
                    elif razor_montage_panel_number == 5:
                        show montage5 razor unarmed onlayer inyourface
                        with dissolve
                    elif razor_montage_panel_number == 6:
                        show montage6 razor unarmed onlayer inyourface
                        with dissolve
                    paranoid "Just panic! Flee!\n"
                    voice "audio/voices/ch3/razor/nexus/narrator/skewer5.flac"
                    play audio "audio/final/Razor_ImpaleSwordBody_5.flac"
                    n "She skewers you.\n"
                    voice "audio/voices/ch3/razor/nexus/princess/36.flac"
                    if razor_montage_panel_number == 2:
                        show montage2 razor unarmed talk onlayer back
                        with dissolve
                    elif razor_montage_panel_number == 3:
                        show montage3 razor unarmed talk onlayer front
                        with dissolve
                    elif razor_montage_panel_number == 4:
                        show montage4 razor unarmed  talk onlayer front
                        with dissolve
                    elif razor_montage_panel_number == 5:
                        show montage5 razor unarmed talk onlayer inyourface
                        with dissolve
                    elif razor_montage_panel_number == 6:
                        show montage6 razor unarmed talk onlayer inyourface
                        with dissolve
                    sp "No, you don't get to escape! That's not how this works.\n"

                elif trait_cold == False:
                    $ trait_cold = True
                    voice "audio/voices/ch3/razor/nexus/cold/4.flac"
                    play audio "audio/final/Razor_SwordSwish_6.flac"
                    if razor_montage_panel_number == 2:
                        show montage2 razor unarmed onlayer back
                        with dissolve
                    elif razor_montage_panel_number == 3:
                        show montage3 razor unarmed onlayer front
                        with dissolve
                    elif razor_montage_panel_number == 4:
                        show montage4 razor unarmed onlayer front
                        with dissolve
                    elif razor_montage_panel_number == 5:
                        show montage5 razor unarmed onlayer inyourface
                        with dissolve
                    elif razor_montage_panel_number == 6:
                        show montage6 razor unarmed onlayer inyourface
                        with dissolve
                    cold "She's going to kill this body either way. So stop feeling what it feels.\n"
                    voice "audio/voices/ch3/razor/nexus/narrator/skewer6.flac"
                    play audio "audio/final/Razor_ImpaleSwordBody_6.flac"
                    n "She skewers you.\n"
                    voice "audio/voices/ch3/razor/nexus/princess/37.flac"
                    if razor_montage_panel_number == 2:
                        show montage2 razor unarmed talk onlayer back
                        with dissolve
                    elif razor_montage_panel_number == 3:
                        show montage3 razor unarmed talk onlayer front
                        with dissolve
                    elif razor_montage_panel_number == 4:
                        show montage4 razor unarmed  talk onlayer front
                        with dissolve
                    elif razor_montage_panel_number == 5:
                        show montage5 razor unarmed talk onlayer inyourface
                        with dissolve
                    elif razor_montage_panel_number == 6:
                        show montage6 razor unarmed talk onlayer inyourface
                        with dissolve
                    sp "Ooooh. Not bad! Real tough!\n"

                elif trait_opportunist == False:
                    $ trait_opportunist = True
                    voice "audio/voices/ch3/razor/nexus/opportunist/3.flac"
                    play audio "audio/final/Razor_SwordSwish_7.flac"
                    if razor_montage_panel_number == 2:
                        show montage2 razor unarmed onlayer back
                        with dissolve
                    elif razor_montage_panel_number == 3:
                        show montage3 razor unarmed onlayer front
                        with dissolve
                    elif razor_montage_panel_number == 4:
                        show montage4 razor unarmed onlayer front
                        with dissolve
                    elif razor_montage_panel_number == 5:
                        show montage5 razor unarmed onlayer inyourface
                        with dissolve
                    elif razor_montage_panel_number == 6:
                        show montage6 razor unarmed onlayer inyourface
                        with dissolve
                    opportunist "Let's appeal to her better nature! We haven't tried that. I'm sure she'll listen to reason.\n"
                    voice "audio/voices/ch3/razor/nexus/narrator/17.flac"
                    play audio "audio/final/Razor_ImpaleSwordBody_1.flac"
                    n "She skewers you.\n"

                elif trait_skeptic == False:
                    $ trait_skeptic = True
                    voice "audio/voices/ch3/razor/nexus/skeptic/3.flac"
                    play audio "audio/final/Razor_SwordSwish_8.flac"
                    if razor_montage_panel_number == 2:
                        show montage2 razor unarmed onlayer back
                        with dissolve
                    elif razor_montage_panel_number == 3:
                        show montage3 razor unarmed onlayer front
                        with dissolve
                    elif razor_montage_panel_number == 4:
                        show montage4 razor unarmed onlayer front
                        with dissolve
                    elif razor_montage_panel_number == 5:
                        show montage5 razor unarmed onlayer inyourface
                        with dissolve
                    elif razor_montage_panel_number == 6:
                        show montage6 razor unarmed onlayer inyourface
                        with dissolve
                    skeptic "None of this is working! Think. Think!\n"
                    voice "audio/voices/ch3/razor/nexus/narrator/skewer7.flac"
                    play audio "audio/final/Razor_ImpaleSwordBody_2.flac"
                    n "She skewers you.\n"

                jump razor_2_unarmed_montage_loop

        $ quick_menu = False
        voice "audio/voices/ch3/razor/nexus/narrator/45.flac"
        hide bg onlayer farback
        hide bg onlayer back
        hide farback onlayer farback
        hide montage1 onlayer back
        hide montage2 onlayer back
        hide montage3 onlayer front
        hide montage4 onlayer front
        hide montage5 onlayer inyourface
        hide montage6 onlayer inyourface
        scene bg black
        with fade
        n "And then everything goes dark, and you die.\n"
        jump razor_final_staging
return
