label beast_1_encounter_start:
    default beast_contrarian = False
    default beast_fled = False
    default beast_cant_eaten = False
    play music "audio/_music/ch2/beast/The Beast Heightened No Drums.flac" loop
    play music2 "audio/_music/ch2/beast/The Beast Heightened Drums Only.flac" loop
    play audio "audio/one_shot/new/STP_chainsmovement_2.flac"
    hide beast onlayer back with dissolve
    voice "audio/voices/ch2/beast/_encounter/narrator/1.flac"
    n "A shiver rushes up your spine and pulls you upright.\n"
    voice "audio/voices/ch2/beast/_encounter/hunted/1.flac"
    hunted "The air's shifting. She's getting ready to pounce. Move, now.\n"
    label beast_encounter_menu_1:
        default beast_player_wounded = False
        default beast_encounter_stall_count = 0
        default beast_encounter_1_where = False
        default beast_encounter_1_fine = False
        default beast_encounter_1_talk = False
        default beast_captured_delay = False
        default beast_captured_injured = False
        if beast_encounter_stall_count >= 2:
            if wild_encountered:
                $ beast_cant_eaten = True
                voice "audio/voices/mound/bonus/path.flac"
                mound "This path is already worn by travel and has been seen by one of my many eyes. You cannot walk it again. Change your course.\n"
                menu:
                    extend ""

                    "{i}• [[Dodge.]{/i}":
                        voice "audio/voices/ch2/beast/_encounter/hero/31.flac"
                        hero "Wait... what?!\n"
                        jump beast_1_encounter_dodged

            jump beast_encounter_1_eaten
        menu:
            extend ""

            "{i}• (Explore) Where?{/i}" if beast_encounter_1_where == False:
                $ beast_encounter_1_where = True
                $ beast_encounter_stall_count += 1
                voice "audio/voices/ch2/beast/_encounter/hunted/2.flac"
                hunted "Anywhere.\n"
                jump beast_encounter_menu_1

            "{i}• (Explore) Don't you hear that clinking? She's in chains again. We're fine.{/i}" if beast_encounter_1_fine == False:
                $ beast_encounter_1_fine += 1
                $ beast_encounter_stall_count += 1
                voice "audio/voices/ch2/beast/_encounter/hunted/3.flac"
                hunted "We're not. {i}Move{/i}.\n"
                jump beast_encounter_menu_1

            "{i}• (Explore) ''You're about to attack me, aren't you? I can see right through you.''{/i}" if beast_encounter_1_talk == False:
                $ beast_encounter_1_talk = True
                jump beast_encounter_1_eaten

            "{i}• (Explore) ''We don't have to kill each other. You know that, right?''{/i}" if beast_encounter_1_talk == False:
                $ beast_encounter_1_talk = True
                jump beast_encounter_1_eaten

            "{i}• [[Move.]{/i}":
                jump beast_1_encounter_dodged

            "{i}• [[Stand still.]{/i}" if beast_cant_eaten == False:
                $ achievement.grant("ACH_BEAST_FREEZE")
                if wild_encountered:
                    $ beast_cant_eaten = True
                    voice "audio/voices/mound/bonus/path.flac"
                    mound "This path is already worn by travel and has been seen by one of my many eyes. You cannot walk it again. Change your course.\n"
                    menu:
                        extend ""

                        "{i}• [[Dodge.]{/i}":
                            voice "audio/voices/ch2/beast/_encounter/hero/31.flac"
                            hero "Wait... what?!\n"
                            jump beast_1_encounter_dodged

                    jump beast_1_encounter_start
                label beast_encounter_1_eaten:
                    if wild_encountered:
                        jump beast_skeptic_end
                    if beast_captured_delay:
                        voice "audio/voices/ch2/beast/_encounter/narrator/2.flac"
                    else:
                        voice "audio/voices/ch2/beast/_encounter/narrator/3.flac"
                    play audio "audio/final/beast_charge_devour.flac"
                    hide beast onlayer back
                    hide fore onlayer inyourface
                    hide fore onlayer back
                    hide fore onlayer front
                    hide farback onlayer farback
                    hide bg onlayer back
                    show beast swallow full onlayer back
                    with dissolve
                    if beast_captured_delay:
                        #voice "audio/voices/ch2/beast/_encounter/narrator/2.flac"
                        n "As you turn to sprint for the stairs, you feel the air shift. You instinctively glance behind you just in time to see the Princess lunge from the shadows, maw unhinged and dripping, eyes fierce and full of hunger.\n"
                    else:
                        #voice "audio/voices/ch2/beast/_encounter/narrator/3.flac"
                        n "There's a shift in the humid air and something enormous—the Princess—lunges from the shadows, her maw unhinged and dripping, her eyes fierce and full of hunger.\n"
                    stop music2 fadeout 10.0
                    stop sound fadeout 5.0
                    voice "audio/voices/ch2/beast/_encounter/narrator/4.flac"
                    n "She is too quick to outrun, too nimble to outmaneuver, too determined to overpower. This is her domain. You are devoured.\n"
                    label beast_eaten_late_join:
                        voice "audio/voices/ch2/beast/_encounter/hero/1.flac"
                        hero "I guess that's it then, isn't it...\n"
                        voice "audio/voices/ch2/beast/_encounter/narrator/5.flac"
                        n "Unfortunately for you, no. This isn't 'it.'\n"
                        $ gallery_beast.unlock_item(3)
                        $ renpy.save_persistent()
                        play sound "audio/final/Beast_StomachAMBalt_loop_2.ogg" loop
                        voice "audio/voices/ch2/beast/_encounter/narrator/6.flac"
                        play secondary "audio/final/beast_inside_heart_loop.ogg"
                        $ quick_menu = False
                        hide beast onlayer back
                        show bg beast guts 1 onlayer back at Position(ypos=1125)
                        show fore beast guts 1 onlayer front at Position(ypos=1125)
                        show player guts 0 onlayer inyourface at Position(ypos=1125)
                        with fade
                        if persistent.quick_menu:
                            $ quick_menu = True
                        n "You are in a dark and caustic place. A thick, fibrous lining constricts around you, its slick surface impossible to grip, your hands scrabbling uselessly at your surroundings as they compress in on you. Your lungs can barely expand in such a tiny space, not that the humid, finite air grants you more than a few shallow breaths at a time.\n"
                        if beast_encounter_1_talk:
                            voice "audio/voices/ch2/beast/_encounter/princess/1a.flac"
                            spmid "You spoke when you needed to act.\n"
                        play audio "audio/final/Beast_AcidFleshMelt_1.flac"
                        voice "audio/voices/ch2/beast/_encounter/narrator/7.flac"
                        n "The liquid pooling beneath you starts to seep into your skin. You itch, then sting, then burn as the acid begins its slow work.\n"
                        voice "audio/voices/ch2/beast/_encounter/princess/2a.flac"
                        spmid "When I killed you I tried to leave this place, but it wouldn't let me. 'You belong down there,' it screamed at me. 'The world is better off without you in it.'\n"
                        play audio "audio/final/beast_thump_acid.flac"
                        voice "audio/voices/ch2/beast/_encounter/narrator/8a.flac"
                        show player guts 1 onlayer inyourface
                        with dissolve
                        n "The flesh around you rumbles as the Princess begins to move, her thundering footfalls twisting you helplessly about. Your skin protests as the corrosive liquid sloshes around you, but there will be no respite for you in sight. The burning grows stronger and you can feel layers of you being peeled away.\n" id beast_eaten_late_join_1f14ebf0
                        voice "audio/voices/ch2/beast/_encounter/princess/3a.flac"
                        spmid "But, you—you don't belong down here. You came from somewhere else. You came from out there. So I consumed your dead heart, and I carried it in my throat, and I draped what was left of you on my back and I threw myself against that door.\n"
                        play secondary "audio/final/Prisoner_HeavyChains_1.flac"
                        queue secondary "audio/final/chain_break_low.flac"
                        voice "audio/voices/ch2/beast/_encounter/narrator/9.flac"
                        n "She stops, her muscles tensing around you, and through the muffling layers of her flesh, you hear the whine of straining metal. And with a pop, she lurches forward, your body lurching right along with her.\n"
                        voice "audio/voices/ch2/beast/_encounter/hunted/4.flac"
                        hunted "Her chains. She's loose.\n"
                        voice "audio/voices/ch2/beast/_encounter/princess/4a.flac"
                        spmid "But even then, it denied me freedom. 'You cannot fool me by draping yourself in decay. I know your true nature and it is suffering.'\n"
                        voice "audio/voices/ch2/beast/_encounter/narrator/10.flac"
                        play audio "audio/final/beast_thump.flac"
                        n "Gravity pulls at you as you're hefted upwards, the distant creaking of ancient wooden steps barely audible over the thudding of the Princess' heart.\n"
                        voice "audio/voices/ch2/beast/_encounter/princess/5a.flac"
                        spmid "And then it was gone and I was here. A new enclosure. A nicer cage. But still a prison.\n"
                        voice "audio/voices/ch2/beast/_encounter/princess/6a.flac"
                        spmid "I learn from my wounds. You're alive now. We can leave together.\n"
                        voice "audio/voices/ch2/beast/_encounter/hero/2.flac"
                        hero "Does that work? Could she free herself if we're alive in here?\n" id beast_eaten_late_join_ab0a5dc9
                        voice "audio/voices/ch2/beast/_encounter/narrator/11a.flac"
                        n "Do you really need me to give you a definitive answer for you to understand that the situation is grim? Stop her. Do {i}something{/i}.\n"
                        if blade_held:
                            voice "audio/voices/ch2/beast/_encounter/hunted/5.flac"
                            hunted "You still have that steel claw. Tear through her. Before we are her. Survive.\n"
                            voice "audio/voices/ch2/beast/_encounter/hero/3.flac"
                            hero "Or we could use it to make this quick for ourselves. If she needs us in order to leave, we could at least deny her that.\n"
                            voice "audio/voices/ch2/beast/_encounter/hunted/6a.flac"
                            hunted "That is a bad thing to do.\n"
                        else:
                            voice "audio/voices/ch2/beast/_encounter/hunted/7.flac"
                            hunted "We don't have steel but we have tooth and claw. Tear through her. Before we are her.\n"
                        label beast_devoured_menu:
                            default beast_devoured_hp = 4
                            default beast_devoured_count = 0
                            default beast_devoured_minor_count = 0
                            default beast_devoured_cabin_talk = False
                            default beast_devoured_swalled_talk = False
                            default beast_devoured_spit_command = False
                            default beast_devoured_threaten = False
                            default beast_devoured_just_incremented = False
                            if beast_devoured_minor_count >= 2:
                                $ beast_devoured_minor_count = 0
                                $ beast_devoured_count += 1
                                $ beast_devoured_just_incremented = True
                            if beast_devoured_just_incremented:
                                $ beast_devoured_just_incremented = False
                                if beast_devoured_count == 1:
                                    voice "audio/voices/ch2/beast/_encounter/narrator/12.flac"
                                    play audio "audio/final/beast_strain_acid_2.flac"
                                    show player beast guts 2 onlayer inyourface
                                    with dissolve
                                    n "Your body is violently jostled, the disruption causing burning skin to slough from raw muscle, and you hear what you can only assume is the Princess pulling against the door to the cabin.\n" id beast_devoured_menu_c5f2018b
                                    voice "audio/voices/ch2/beast/_encounter/princess/7a.flac"
                                    spmid "The cage is still locked!\n"
                                    if beast_devoured_hp == 4:
                                        voice "audio/voices/ch2/beast/_encounter/hero/4.flac"
                                        hero "I don't think we can talk our way out of this.\n"
                                        voice "audio/voices/ch2/beast/_encounter/hunted/8.flac"
                                        hunted "We are drowning in death. There's no more space for words.\n"
                                if beast_devoured_count == 2:
                                    play audio "audio/final/beast_knock_acid.flac"
                                    play secondary "audio/final/Beast_AcidFleshMelt_2.flac"
                                    show player beast guts 3 onlayer inyourface
                                    with dissolve
                                    voice "audio/voices/ch2/beast/_encounter/narrator/13.flac"
                                    n "The pulling has turned to banging, as the Princess desperately throws everything at the cabin door. Your flesh screams as your reddened, spongy body is hit with fresh waves of blistering acid.\n"
                                    voice "audio/voices/ch2/beast/_encounter/princess/8a.flac"
                                    spmid "You can't hold me forever!\n"
                                if beast_devoured_count == 3:
                                    play audio "audio/final/Beast_AcidSizzle_2.flac"
                                    show player beast guts 4 onlayer inyourface
                                    with dissolve
                                    jump beast_devour_die

                            menu:
                                extend ""

                                "{i}• (Explore) ''Can you talk to the cabin?''{/i}" if beast_devour_cabin_explore == False:
                                    default beast_devour_cabin_explore = False
                                    $ beast_devour_cabin_explore = True
                                    $ beast_devoured_minor_count += 2
                                    voice "audio/voices/ch2/beast/_encounter/princess/9a.flac"
                                    spmid "I understand it, and it understands me. Talking is for those who don't know how to listen.\n"
                                    jump beast_devoured_menu

                                "{i}• (Explore) ''You could have asked me before swallowing me alive.''{/i}" if beast_devour_asked_explore == False:
                                    default beast_devour_asked_explore = False
                                    $ beast_devour_asked_explore = True
                                    $ beast_devoured_minor_count += 2
                                    voice "audio/voices/ch2/beast/_encounter/princess/10a.flac"
                                    spmid "I acted on my will, fledgling, and you acted on yours. The strong triumph, and the weak submit or perish.\n"
                                    jump beast_devoured_menu

                                "{i}• (Explore) ''Spit me out or I'll kill myself and nobody gets to leave.''{/i}" if blade_held and beast_devour_threaten_explore == False:
                                    default beast_devour_threaten_explore = False
                                    $ beast_devour_threaten_explore = True
                                    $ beast_devoured_minor_count += 2
                                    voice "audio/voices/ch2/beast/_encounter/princess/11a.flac"
                                    spmid "I'm so very, very patient. If it takes lives and lives and lives to swallow my way to freedom, then that is what I'll do.\n"
                                    jump beast_devoured_menu

                                "{i}• (Explore) ''You need me to want to free you, don't you? You can't force me to let you out of here.''{/i}" if beast_devoured_count >= 1 and beast_devour_need_explore == False:
                                    default beast_devour_need_explore = False
                                    $ beast_devour_need_explore = True
                                    $ beast_devoured_minor_count += 2
                                    voice "audio/voices/ch2/beast/_encounter/princess/12a.flac"
                                    spmid "Every creature craves freedom. You will too, before you die.\n"
                                    jump beast_devoured_menu

                                "{i}• (Explore) ''Just because I want freedom, doesn't mean I want to give you yours.''{/i}" if beast_devoured_count >= 1:
                                    default beast_accidental_freedom = False
                                    $ beast_accidental_freedom = True
                                    $ beast_devoured_minor_count += 2
                                    voice "audio/voices/ch2/beast/_encounter/princess/13a.flac"
                                    spmid "So you do want freedom.\n"
                                    voice "audio/voices/ch2/beast/_encounter/narrator/14.flac"
                                    n "The click of what you presume to be a door ripples through the layers of suffocating flesh.\n"
                                    # FAST
                                    voice "audio/voices/ch2/beast/_encounter/hero/5.flac"
                                    hero "But we didn't—\n{w=0.57}{nw}"
                                    show screen disableclick(0.5)
                                    voice "audio/voices/ch2/beast/_encounter/narrator/15.flac"
                                    n "Apparently that was all it took.\n"
                                    voice "audio/voices/ch2/beast/_encounter/princess/14a.flac"
                                    spmid "That wasn't so hard.\n"
                                    jump beast_surrender_late

                                "{i}• (Explore) ''I have my steel claw. I could use it to hurt you.''{/i}" if beast_devoured_hp == 4 and beast_devoured_threaten == False and blade_held:
                                    $ beast_devoured_minor_count += 2
                                    $ beast_devoured_threaten = True
                                    voice "audio/voices/ch2/beast/_encounter/princess/15a.flac"
                                    spmid "You threaten me, but you don't act.\n"
                                    jump beast_devoured_menu

                                "{i}• (Explore) ''I've found your heart. Spit me out, or I will end you.''{/i}" if beast_devoured_threaten == False and beast_devoured_hp == 0:
                                    $ beast_devoured_minor_count += 2
                                    $ beast_devoured_threaten = True
                                    voice "audio/voices/ch2/beast/_encounter/princess/15a.flac"
                                    spmid "You threaten me, but you don't act.\n"
                                    jump beast_devoured_menu

                                "{i}• (Explore) [[Claw and bite.]{/i}" if blade_held == False:
                                    $ beast_devoured_minor_count += 2
                                    $ beast_devoured_hp -= 1
                                    if beast_devoured_hp == 3:
                                        play audio "audio/final/Adversary_StabCut_3.flac"
                                        voice "audio/voices/ch2/beast/_encounter/narrator/16.flac"
                                        show bg beast guts 2 onlayer back
                                        show fore beast guts 2 onlayer front
                                        with dissolve
                                        n "Like the cornered animal you are, you tear against the thick membranes of her stomach with every part of you that can be made sharp: nails, claws, teeth, hands, feet.\n"
                                        voice "audio/voices/ch2/beast/_encounter/princess/16a.flac"
                                        spmid "I can feel you tearing through me. But are you swift enough for it to matter?\n"
                                    elif beast_devoured_hp == 2:
                                        play audio "audio/final/Adversary_StabCut_9.flac"
                                        voice "audio/voices/ch2/beast/_encounter/narrator/17.flac"
                                        show bg beast guts 3 onlayer back
                                        show fore beast guts 3 onlayer front
                                        with dissolve
                                        n "Again you tear, heart pumping with adrenaline, your ulcerating hands a blur of feverish motion fueled by the desperation to fight against being reduced to lifeless molecules and meat.\n"
                                    else:
                                        play audio "audio/final/Adversary_StabCut_10.flac"
                                        play tertiary "audio/final/Beast_AcidSizzle_2.flac"
                                        play secondary "audio/final/_nightmare_heart_loop.ogg" loop
                                        voice "audio/voices/ch2/beast/_encounter/narrator/18.flac"
                                        show bg beast guts 4 onlayer back
                                        show fore beast guts 4 onlayer front
                                        show player beast guts 4 onlayer inyourface
                                        with dissolve
                                        n "Your energy is fading. But you can hear her heart, thumping somewhere close. There's so little of you left — your fingers reduced to bone, your nerves bare and screaming, the acid pooling around you now a soup of your skin and meat. You are a spark of will driving a melted corpse.\n"
                                        jump beast_devour_die
                                    jump beast_devoured_menu

                                "{i}• (Explore) [[Dig with the steel claw.]{/i}" if blade_held and beast_devoured_hp != 0:
                                    $ default_mouse = "blood"
                                    $ beast_devoured_minor_count += 2
                                    $ beast_devoured_hp -= 2
                                    if beast_devoured_hp == 2:
                                        play audio "audio/final/Adversary_StabCut_1.flac"
                                        voice "audio/voices/ch2/beast/_encounter/narrator/19.flac"
                                        show bg beast guts 3 onlayer back
                                        show fore beast guts 3 onlayer front
                                        with dissolve
                                        n "Though you have little room to move, you use what strength you can muster to drive the blade forward into the thick walls of tissue digesting you.\n"
                                        voice "audio/voices/ch2/beast/_encounter/princess/16a.flac"
                                        spmid "I can feel you tearing through me. But are you swift enough for it to matter?\n"
                                    else:
                                        play audio "audio/final/Adversary_StabCut_10.flac"
                                        voice "audio/voices/ch2/beast/_encounter/narrator/20.flac"
                                        show bg beast guts 4 onlayer back
                                        show fore beast guts 4 onlayer front
                                        show player beast guts 4 onlayer inyourface
                                        with dissolve
                                        n "You slice again, deeper, rooting through her meat with the tip of your blade, until at last it finds her beating heart.\n"
                                    jump beast_devoured_menu

                                "{i}• [[Slay the Princess.]{/i}" if beast_devoured_hp == 0:
                                    play audio "audio/final/Beast_AcidSizzle_2.flac"
                                    voice "audio/voices/ch2/beast/_encounter/narrator/21.flac"
                                    hide bg onlayer back
                                    hide fore onlayer front
                                    hide player onlayer inyourface
                                    show bg beast heart onlayer farback at Position(ypos=1125)
                                    show heart beast onlayer back at Position(ypos=1125)
                                    show fore beast heart onlayer front at Position(ypos=1125)
                                    with Dissolve(2.0)
                                    n "Though your body is dissolving, eroding into unrecognizeable shapes, your will drives it forward. You have a target, and you will strike it.\n"
                                    voice "audio/voices/ch2/beast/_encounter/hunted/9a.flac"
                                    hunted "We're too late, aren't we? This isn't survival, this is spite.\n"
                                    #hunted "This isn't survival, is it?\n"
                                    $ achievement.grant("ACH_BEAST_AHAB")
                                    play audio "audio/final/Adversary_SkullBreaksBrain_1.flac"
                                    voice "audio/voices/ch2/beast/_encounter/narrator/22.flac"
                                    $ gallery_beast.unlock_item(4)
                                    $ renpy.save_persistent()
                                    show player beast heart stab onlayer front at Position(ypos=1125)
                                    with dissolve
                                    n "No. It's something better. It's fulfilling a noble destiny. Your lone functioning arm lashes out, stabbing up towards the Princess' heart.\n"
                                    voice "audio/voices/ch2/beast/_encounter/princess/17a.flac"
                                    sp "So you found a way to kill me. Then we'll die together, and I will see you again soon.\n"
                                    stop music fadeout 3.0
                                    stop sound fadeout 3.0
                                    stop secondary fadeout 3.0
                                    stop tertiary fadeout 3.0
                                    voice "audio/voices/ch2/beast/_encounter/narrator/23.flac"
                                    scene bg black
                                    hide player onlayer front
                                    hide fore onlayer front
                                    hide heart onlayer back
                                    hide bg onlayer farback
                                    with fade
                                    n "With those prophetic words, you do not draw another breath, your body tangled and melting in the cooling folds of the Princess' flesh. Everything goes dark, and you die.\n"
                                    voice "audio/voices/ch2/beast/_encounter/narrator/24.flac"
                                    n "But at least you've saved the world. I hope.\n"
                                    $ wild_source = "beast"
                                    $ quick_menu = False
                                    if beast_contrarian:
                                        $ wild_bonus_voice = "contrarian"
                                    else:
                                        $ wild_bonus_voice = "opportunist"
                                    jump wild_start
                                    # end

                                "{i}• ''Fine. You can leave.''{/i}":
                                    jump beast_surrender

                                "{i}• ''You can leave! Just let me go.''{/i}":
                                    jump beast_surrender

                                "{i}• ''Screw you!'' [[Slay yourself.]{/i}" if blade_held:
                                    play audio "audio/one_shot/new/throat_slit.flac"
                                    voice "audio/voices/ch2/beast/_encounter/narrator/25.flac"
                                    scene bg black
                                    hide bg onlayer back
                                    hide fore onlayer front
                                    hide player onlayer inyourface
                                    with fade
                                    n "In an act of spiteful defiance, you pull your weapon to your throat, your shaking, ulcerous hand clenched tight around its hilt. And then you draw it across your bubbling veins.\n"
                                    #too fast. Had to draw it out a little.
                                    voice "audio/voices/ch2/beast/_encounter/narrator/26.flac"
                                    n "Your blood flows out, filling the tiny space inside the Princess. You start to fade.\n"
                                    voice "audio/voices/ch2/beast/_encounter/hunted/10.flac"
                                    hunted "A waste of a good life.\n"
                                    voice "audio/voices/ch2/beast/_encounter/hero/6.flac"
                                    hero "It's better than giving in to her.\n"
                                    stop music fadeout 3.0
                                    stop sound fadeout 3.0
                                    stop secondary fadeout 3.0
                                    stop tertiary fadeout 3.0
                                    voice "audio/voices/ch2/beast/_encounter/narrator/27.flac"
                                    n "But in the end, the opinions of stray voices mean little in the grand scheme of things. Everything goes dark, and you die.\n"
                                    $ default_mouse = "default"
                                    $ wild_source = "beast"
                                    if beast_contrarian:
                                        $ wild_bonus_voice = "contrarian"
                                    else:
                                        $ wild_bonus_voice = "stubborn"
                                    jump wild_start
                                    # END

                                "{i}• [[Wait for death.]{/i}" if blade_held == False:
                                    voice "audio/voices/ch2/beast/_encounter/hunted/11.flac"
                                    if beast_devoured_count != 3:
                                        play audio "audio/final/Beast_AcidSizzle_2.flac"
                                        show player beast guts 4 onlayer inyourface
                                        with dissolve
                                    hunted "Bad! This is a bad thing to do!\n"
                                    voice "audio/voices/ch2/beast/_encounter/narrator/28.flac"
                                    n "Your will dissolves along with your flesh. You let go, and pathetically await your death, every burning second dragging on until you're reduced to a wet pile of bone and gristle.\n"
                                    voice "audio/voices/ch2/beast/_encounter/princess/18a.flac"
                                    sp "We'll do better next time.\n"
                                    stop music fadeout 3.0
                                    stop sound fadeout 3.0
                                    stop secondary fadeout 3.0
                                    stop tertiary fadeout 3.0
                                    voice "audio/voices/ch2/beast/_encounter/narrator/29.flac"
                                    scene bg black
                                    hide bg onlayer back
                                    hide fore onlayer front
                                    hide player onlayer inyourface
                                    with fade
                                    n "Your vision finally begins to blur, your eyes clouding over as they melt in their sockets. Everything goes dark, and you die.\n"
                                    $ default_mouse = "default"
                                    $ wild_source = "beast"
                                    $ quick_menu = False
                                    if beast_contrarian:
                                        $ wild_bonus_voice = "contrarian"
                                    else:
                                        $ wild_bonus_voice = "broken"
                                    jump wild_start
                                    # END

                            label beast_surrender:
                                voice "audio/voices/ch2/beast/_encounter/princess/19a.flac"
                                spmid "Oh, can I?\n"
                                voice "audio/voices/ch2/beast/_encounter/narrator/30.flac"
                                play audio "audio/final/door_bedroom_inside.flac"
                                n "The click of what you presume to be a door ripples through the layers of suffocating flesh.\n"
                                voice "audio/voices/ch2/beast/_encounter/princess/20a.flac"
                                spmid "That wasn't so hard.\n"
                                label beast_surrender_late:
                                    $ achievement.grant("ACH_BEAST_DISSOLVE")
                                    play secondary "audio/final/beast_thump_acid.flac"
                                    stop music fadeout 5.0
                                    stop sound fadeout 5.0
                                    stop secondary fadeout 10.0
                                    stop tertiary fadeout 5.0
                                    voice "audio/voices/ch2/beast/_encounter/narrator/31a.flac"
                                    n "You feel her take another massive step, and then another, and then—\n"
                                    play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 30.0
                                    voice "audio/voices/ch2/beast/_encounter/hero/7.flac"
                                    hero "And then...?\n"
                                    voice "audio/voices/ch2/beast/_encounter/hunted/12.flac"
                                    hunted "It's gone quiet, hasn't it?\n"
                                    play audio "audio/final/Beast_WetJawsCrackSwallowPlayer_1.flac"
                                    hide bg onlayer back
                                    hide fore onlayer front
                                    hide player onlayer inyourface
                                    with fade
                                    truth "You can feel a churning in the forms around you, and then a wet tunneling before you are ejected to a place that is nowhere at all.\n"
                                    $ gallery_beast.unlock_item(5)
                                    $ renpy.save_persistent()
                                    voice "audio/voices/ch2/beast/_encounter/princess/21a.flac"
                                    show farback quiet onlayer farback at Position(ypos=1125)
                                    show cg beast quiet recognize onlayer back at Position(ypos=1125)
                                    if beast_devoured_count == 0:
                                        show player beast quiet 2 onlayer inyourface at Position(ypos=1125)
                                    elif beast_devoured_count == 1:
                                        show player beast quiet 3 onlayer inyourface at Position(ypos=1125)
                                    elif beast_devoured_count == 2:
                                        show player beast quiet 4 onlayer inyourface at Position(ypos=1125)
                                    with fade
                                    sp "I guess I don't need you to be a part of me. How lucky for you.\n"
                                    voice "audio/voices/ch2/beast/_encounter/princess/22a.flac"
                                    show cg beast quiet1 onlayer back
                                    with dissolve
                                    sp "This place is cold.\n"
                                    play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                                    hide beast onlayer back
                                    show arms beast quiet1 onlayer farback at Position(ypos=1125)
                                    show cg beast quiet taken onlayer back at Position(ypos=1125)
                                    with Dissolve(1.0)
                                    $ renpy.pause(0.125)
                                    hide arms onlayer farback
                                    show arms beast quiet2 onlayer farback at Position(ypos=1125)
                                    with Dissolve(1.0)
                                    $ renpy.pause(0.125)
                                    hide cg onlayer back
                                    hide arms onlayer farback
                                    show arms beast quiet3 onlayer farback at Position(ypos=1125)
                                    with Dissolve(1.0)
                                    $ renpy.pause(0.125)
                                    hide arms onlayer farback
                                    show arms beast quiet4 onlayer farback at Position(ypos=1125)
                                    $ renpy.pause(0.125)
                                    $ blade_held = False
                                    $ default_mouse = "default"
                                    hide arms onlayer farback
                                    hide player onlayer inyourface
                                    with dissolve
                                    $ renpy.pause(3.0)
                                    show mirror quiet distant onlayer back at Position(ypos=1125)
                                    if loops_finished != 0:
                                        truth "But before you can say anything to her, she's gone. Memory returns.\n"
                                    else:
                                        truth "But before you can say anything, something takes her away, and it leaves something else in her place.\n"
                                    $ default_mouse = "default"
                                    $ princess_free += 1
                                    $ princess_satisfy += 1
                                    jump mirror_start
                                    # END

label beast_1_encounter_dodged:
    $ beast_encounter_stairs_guarded = True
    $ gallery_beast.unlock_item(10)
    $ renpy.save_persistent()
    hide beast onlayer back
    hide fore onlayer inyourface
    hide fore onlayer back
    hide farback onlayer farback
    hide bg onlayer back
    play audio "audio/final/beast_dodge_1.flac"
    play secondary "audio/one_shot/new/STP_chainsmovement_1.flac"
    show beast dodge full onlayer back at flip
    with Dissolve(2.0)
    voice "audio/voices/ch2/beast/_encounter/narrator/32.flac"
    n "You lunge to the side, picking a direction on instinct. As you land you're buffeted by a gust of air disturbed by the sudden motion of a massive body—the Princess.\n"
    voice "audio/voices/ch2/beast/_encounter/narrator/32a.flac"
    play secondary "audio/one_shot/new/STP_chainsmovement_3.flac"
    play audio "audio/one_shot/tackle.flac"
    hide beast onlayer back
    show cg beast dodge1 onlayer back at Position(ypos=1125)
    with dissolve
    n "In an instant, she's pounced on the spot where you would have been, her chains rattling across the floor behind her.\n"
    play audio "audio/final/Beast_ChainsFastDrag_2.flac"
    voice "audio/voices/ch2/beast/_encounter/narrator/33.flac"
    show cg beast dodge1 scurry onlayer back at Position(ypos=1125)
    with dissolve
    n "Before you can blink, she's gone, vanishing once more into the shadows. But you still feel her gaze on you.\n"
    voice "audio/voices/ch2/beast/_encounter/princess/23.flac"
    hide cg onlayer back
    show bg beast generic onlayer back at Position(ypos=1125)
    with dissolve
    spmid "You're faster than you were before. But you're still meek. Reactive. Prey.\n"
    voice "audio/voices/ch2/beast/_encounter/narrator/34.flac"
    hide bg onlayer back
    show bg beast dodged onlayer back at Position(ypos=1125)
    show beast dodged onlayer back at Position(ypos=1125)
    show fore beast dodged onlayer front at Position(ypos=1125)
    with dissolve
    n "You whirl around to find her, and your gaze meets hers, a pair of shining eyes peering out at you from just beyond the basement stairs.\n"
    voice "audio/voices/ch2/beast/_encounter/hero/8.flac"
    hero "So she's cut off our escape. Shit. What do we do.\n"
    jump beast_encounter_outside_menu

label beast_encounter_outside_menu:
    default beast_encounter_count = 0
    default beast_encounter_phase = 1
    default beast_encounter_stairs_guarded = False
    default beast_encounter_tired_explore = False
    default beast_encounter_what_ask = False
    default beast_encounter_why_kill = False
    default beast_encounter_why_eat = False
    default beast_encounter_help_offer = False
    default beast_encounter_stop_hide = False
    default beast_encounter_deflect = False
    default beast_encounter_threat = False
    default beast_encounter_can_try_flee = True
    if beast_encounter_count == 1 and beast_encounter_phase >= 3:
        jump beast_encounter_attack_staging
    elif beast_encounter_count == 2:
        jump beast_encounter_attack_staging
    menu:
        extend ""

        "{i}• (Explore) I don't think I can keep this up.{/i}" if beast_encounter_phase >= 2 and beast_encounter_tired_explore == False:
            $ beast_encounter_tired_explore = True
            $ beast_encounter_count += 1
            voice "audio/voices/ch2/beast/_encounter/hunted/13.flac"
            hunted "You have to.\n"
            voice "audio/voices/ch2/beast/_encounter/hero/9.flac"
            hero "We at least have to make an opening.\n"
            jump beast_encounter_outside_menu

        "{i}• (Explore) ''What do you want?''{/i}" if beast_encounter_what_ask == False:
            $ beast_encounter_what_ask = True
            $ beast_encounter_count += 1
            voice "audio/voices/ch2/beast/_encounter/princess/24.flac"
            spmid "I want to swallow you whole. And I will get what I want. You have no exit. You have no hope. You live and die by my whims and my whims alone.\n"
            if blade_held:
                voice "audio/voices/ch2/beast/_encounter/narrator/35.flac"
                n "Don't ask her what she wants. Just. Slay her.\n"
            if blade_held == False:
                if beast_encounter_stairs_guarded:
                    voice "audio/voices/ch2/beast/_encounter/narrator/36.flac"
                    n "Don't ask her what she wants. Just run for the blade upstairs and slay her with it.\n"
                else:
                    voice "audio/voices/ch2/beast/_encounter/narrator/37.flac"
                    n "Don't ask her what she wants. Just go back for the blade upstairs and slay her.\n"
            voice "audio/voices/ch2/beast/_encounter/hero/10.flac"
            hero "Is that all the advice you have? We don't even know what she looks like. Some specifics would be very helpful.\n"
            voice "audio/voices/ch2/beast/_encounter/narrator/38.flac"
            n "She's just a Princess. Don't overthink it.\n"
            voice "audio/voices/ch2/beast/_encounter/hero/11.flac"
            hero "She is clearly not.\n"
            jump beast_encounter_outside_menu

        "{i}• (Explore) ''But why? Why do you want to kill me?''{/i}" if beast_encounter_why_kill == False and beast_encounter_what_ask:
            $ beast_encounter_why_kill = True
            $ beast_encounter_count += 1
            voice "audio/voices/ch2/beast/_encounter/hunted/14.flac"
            hunted "Why does anything kill anything else? She needs to.\n"
            #voice "audio/voices/ch2/beast/_encounter/hero/12.flac"
            #hero "Or she thinks that she needs to.\n"
            voice "audio/voices/ch2/beast/_encounter/princess/25.flac"
            spmid "I didn't say I wanted to {i}kill{/i} you.\n"
            voice "audio/voices/ch2/beast/_encounter/hero/13a.flac"
            hero "It sounds like she wants to do something even worse.\n"
            voice "audio/voices/ch2/beast/_encounter/narrator/39.flac"
            n "What she wants only matters if she wins, and you're not going to let that happen.\n"
            jump beast_encounter_outside_menu

        "{i}• (Explore) ''Okay, fine. Why do you want to eat me?''{/i}" if beast_encounter_why_eat == False and beast_encounter_why_kill:
            $ beast_encounter_why_eat = True
            $ beast_encounter_count += 1
            voice "audio/voices/ch2/beast/_encounter/princess/26.flac"
            spmid "I don't question who I am or what I want. I simply {i}do{/i}. To act is always better than to react. To do is always better than to watch.\n"
            voice "audio/voices/ch2/beast/_encounter/narrator/40.flac"
            n "I can't believe I'm saying this, but you'd do well to listen to her. Less standing around asking questions, more doing exactly as I say.\n"
            jump beast_encounter_outside_menu

        "{i}• (Explore) ''We don't have to kill each other. What if I helped you? What if we left together? If you could get out of here on your own, wouldn't you have already left?''{/i}" if beast_encounter_help_offer == False:
            $ beast_encounter_help_offer = True
            $ beast_encounter_count += 1
            voice "audio/voices/ch2/beast/_encounter/princess/27.flac"
            spmid "You cannot 'reason' your way out of this, fledgling. There's no compromise with what I am.\n"
            voice "audio/voices/ch2/beast/_encounter/hero/14.flac"
            hero "At least she's upfront about her intentions.\n"
            jump beast_encounter_outside_menu

        "{i}• (Explore) ''Stop hiding and show yourself.''{/i}" if beast_encounter_stop_hide == False:
            $ beast_encounter_stop_hide = True
            $ beast_encounter_count += 1
            voice "audio/voices/ch2/beast/_encounter/princess/28.flac"
            sp "If you want to see me, you should get better at seeing.\n"
            voice "audio/voices/ch2/beast/_encounter/hunted/15.flac"
            hunted "She knows that her strength lies in shadows and secrets. She won't reveal herself unless she has to.\n"
            jump beast_encounter_outside_menu

        "{i}• (Explore) ''I was sent to kill you because you're a threat to the world. I'm starting to believe that's true.''{/i}" if beast_encounter_threat == False:
            $ beast_encounter_threat = True
            $ beast_encounter_count += 1
            voice "audio/voices/ch2/beast/_encounter/narrator/41.flac"
            n "Oh, for the love of— you've given up the game, great. All that will do is hasten her victory.\n"
            voice "audio/voices/ch2/beast/_encounter/princess/29.flac"
            spmid "So many useless thoughts run through your head. Thinking thinking thinking. You'll never hurt me if you keep thinking.\n"
            jump beast_encounter_outside_menu

        "{i}• (Explore) ''You're deflecting.''{/i}" if (beast_encounter_stop_hide or beast_encounter_threat) and beast_encounter_deflect == False:
            $ beast_encounter_deflect = True
            $ beast_encounter_count += 1
            voice "audio/voices/ch2/beast/_encounter/princess/30.flac"
            sp "And you bare your weakness to the world.\n"
            jump beast_encounter_outside_menu

        "{i}• [[Run for the stairs.]{/i}" if beast_encounter_can_try_flee:
            label beast_stairs_run:
                if beast_encounter_stairs_guarded == False:
                    $ beast_captured_delay = True
                    $ beast_fled = True
                    voice "audio/voices/ch2/beast/_encounter/hunted/16.flac"
                    hunted "Yes. Now's our chance. Quick!\n"
                    if blade_held == False:
                        voice "audio/voices/ch2/beast/_encounter/hero/15.flac"
                        hero "Right, I agree, we can't do anything without a weapon. We can regroup once we're armed and try to figure out a better plan.\n"
                    else:
                        voice "audio/voices/ch2/beast/_encounter/hero/16.flac"
                        hero "And then what? We need a plan. We need to figure out {i}something{/i}.\n"
                    voice "audio/voices/ch2/beast/_encounter/hunted/17.flac"
                    hunted "Don't plan ahead. Act on the now. All that matters is that we stay alive.\n"
                    if wild_encountered == False:
                        jump beast_encounter_1_eaten
                    else:
                        $ beast_fled = True
                        jump beast_skeptic_end
                else:
                    $ beast_encounter_can_try_flee = False
                    voice "audio/voices/ch2/beast/_encounter/hunted/18.flac"
                    hunted "She's right there. We have to wait for an opening.\n"
                    #hunted "She's right there. We're just waiting for an opening.\n"
                    voice "audio/voices/ch2/beast/_encounter/hero/17.flac"
                    hero "That's fair, she'll kill us if we try and run past her.\n"
                    jump beast_encounter_outside_menu
                # loop back


label beast_encounter_attack_staging:
    $ beast_encounter_count = 0
    $ beast_encounter_can_try_flee = True
    if beast_encounter_phase == 1:
        $ beast_encounter_phase += 1
        jump beast_attack_2
    elif beast_encounter_phase == 2:
        $ beast_encounter_phase += 1
        jump beast_attack_3
    elif beast_encounter_phase == 3:
        $ beast_encounter_phase += 1
        jump beast_attack_4
    else:
        jump beast_skeptic_end

label beast_attack_2:
    voice "audio/voices/ch2/beast/_encounter/hunted/19.flac"
    hunted "She's coiling for another strike. Be somewhere else.\n"
    voice "audio/voices/ch2/beast/_encounter/hero/18.flac"
    hero "We're on the back foot.\n"
    voice "audio/voices/ch2/beast/_encounter/hunted/20.flac"
    hunted "The back foot keeps us nimble. Keeps us alive.\n"
    voice "audio/voices/ch2/beast/_encounter/hero/19.flac"
    hero "It doesn't matter if it keeps us alive if it eventually kills us. We need to take back the momentum. We need to do something.\n"
    label beast_attack_2_menu:
        default beast_attack_2_menu_explore = False
        menu:
            extend ""

            "{i}• (Explore) How exactly are we supposed to take back the momentum here?{/i}" if beast_attack_2_menu_explore == False and blade_held:
                $ beast_attack_2_menu_explore = True
                if blade_held:
                    voice "audio/voices/ch2/beast/_encounter/hero/20.flac"
                    hero "We have the blade, I assume all she has are nails and teeth. Let's use our advantage.\n"
                    voice "audio/voices/ch2/beast/_encounter/hunted/21.flac"
                    hunted "The steel claw is small, and she is large. It's dangerous to fight back. It should only be a last resort.\n"
                else:
                    voice "audio/voices/ch2/beast/_encounter/hero/21.flac"
                    hero "The blade is upstairs. We just need to wait for her to be somewhere else, and sprint out of here.\n"
                    voice "audio/voices/ch2/beast/_encounter/hunted/22.flac"
                    hunted "Anything that gets us out of danger.\n"
                jump beast_attack_2_menu

            "{i}• [[Survive.]{/i}":
                $ beast_encounter_stairs_guarded = False
                $ beast_encounter_count = 0
                voice "audio/voices/ch2/beast/_encounter/narrator/42.flac"
                play secondary "audio/final/Beast_ChainsFastDrag_2.flac"
                play audio "audio/final/beast_dodge_2.flac"
                hide bg onlayer back
                hide beast onlayer back
                hide fore onlayer front
                show beast dodge full onlayer back
                with Dissolve(2.0)
                n "You spring to a new patch of jungle, barely moving out of the way before the Princess surges past you with a speed that makes her practically unseen.\n"
                $ gallery_beast.unlock_item(11)
                $ renpy.save_persistent()
                hide beast onlayer back
                scene farback beast basement onlayer farback at Position(ypos=1125)
                show bg beast basement onlayer back at Position(ypos=1125)
                show beast d stare onlayer back at Position(ypos=1125)
                show fore beast basement onlayer inyourface at Position(ypos=1125)
                with Dissolve(2.0)
                jump beast_encounter_outside_menu

            "{i}• [[Wait for her to strike, and hit her back.]{/i}" if blade_held:
                jump beast_stubborn_end

            "{i}• [[Play dead.]{/i}" if beast_cant_eaten == False:
                if wild_encountered:
                    $ beast_cant_eaten = True
                    voice "audio/voices/mound/bonus/path.flac"
                    mound "This path is already worn by travel and has been seen by one of my many eyes. You cannot walk it again. Change your course.\n"
                    voice "audio/voices/ch2/beast/_encounter/hero/31.flac"
                    hero "Wait... what?!\n"
                    jump beast_attack_2
                jump beast_contrarian_end

            "{i}• [[Stand still.]{/i}" if beast_cant_eaten == False:
                if wild_encountered:
                    $ beast_cant_eaten = True
                    voice "audio/voices/mound/bonus/path.flac"
                    mound "This path is already worn by travel and has been seen by one of my many eyes. You cannot walk it again. Change your course.\n"
                    voice "audio/voices/ch2/beast/_encounter/hero/31.flac"
                    hero "Wait... what?!\n"
                    jump beast_attack_2
                jump beast_encounter_1_eaten

label beast_attack_3:
    voice "audio/voices/ch2/beast/_encounter/narrator/43.flac"
    n "A tickling sensation rises at the base of your neck.\n"
    voice "audio/voices/ch2/beast/_encounter/hunted/23.flac"
    hunted "Flee!\n"
    voice "audio/voices/ch2/beast/_encounter/hero/22.flac"
    hero "We can't keep doing this.\n"
    label beast_attack_3_menu:
        menu:
            extend ""

            "{i}• [[Stay. Alive.]{/i}":
                $ beast_encounter_count = 0
                $ beast_encounter_stairs_guarded = True
                $ beast_player_wounded = True
                voice "audio/voices/ch2/beast/_encounter/narrator/44.flac"
                hide beast onlayer back
                hide fore onlayer inyourface
                hide fore onlayer back
                hide fore onlayer front
                hide farback onlayer farback
                hide bg onlayer back
                play audio "audio/final/beast_dodge_1.flac"
                play secondary "audio/one_shot/new/STP_chainsmovement_1.flac"
                play tertiary "audio/one_shot/tackle.flac"
                show beast dodge full onlayer back at flip
                with Dissolve(2.0)
                n "You're a little slower this time, or maybe she's a little faster. You avoid her slavering jaws, but she manages to graze you, her titanic momentum skinning you along your side.\n"
                voice "audio/voices/ch2/beast/_encounter/hero/23.flac"
                hide bg onlayer back
                hide beast onlayer back
                show beast dodge2 onlayer back at flip, Position(ypos=1125)
                show fore beast dodge2 onlayer front at Position(ypos=1125)
                with dissolve
                hero "It's like being sideswiped by sandpaper, how is she that fast?!\n"
                voice "audio/voices/ch2/beast/_encounter/princess/31.flac"
                hide beast onlayer back
                show beast dodge2 talk onlayer back at flip
                with dissolve
                spmid "You're bleeding now.\n"
                play secondary "audio/one_shot/new/STP_chainsmovement_1.flac"
                voice "audio/voices/ch2/beast/_encounter/narrator/45.flac"
                hide beast onlayer back
                hide fore onlayer front
                show bg beast dodged onlayer back at Position(ypos=1125)
                show beast dodged onlayer back at Position(ypos=1125)
                show fore beast dodged onlayer front at Position(ypos=1125)
                with dissolve
                n "You instinctively touch your side, testing her claim. It's wet and stings from the gentle touch of your fingertips.\n"
                voice "audio/voices/ch2/beast/_encounter/hunted/24.flac"
                hunted "A costly mistake. We can't make it again.\n"
                voice "audio/voices/ch2/beast/_encounter/hero/24.flac"
                hero "We will make it again unless something changes. We have to break the pattern.\n"
                voice "audio/voices/ch2/beast/_encounter/hunted/25.flac"
                hunted "We need more time. She's cutting off our escape.\n"
                voice "audio/voices/ch2/beast/_encounter/princess/32.flac"
                spmid "Our game is nearing its end.\n"
                jump beast_encounter_outside_menu

            "{i}• [[Run for the stairs.]{/i}":
                jump beast_stairs_run

            "{i}• [[Wait for her to strike, and hit her back.]{/i}" if blade_held:
                jump beast_stubborn_end

            "{i}• [[Play dead.]{/i}" if beast_cant_eaten == False:
                if wild_encountered:
                    $ beast_cant_eaten = True
                    voice "audio/voices/mound/bonus/path.flac"
                    mound "This path is already worn by travel and has been seen by one of my many eyes. You cannot walk it again. Change your course.\n"
                    voice "audio/voices/ch2/beast/_encounter/hero/31.flac"
                    hero "Wait... what?!\n"
                    jump beast_attack_3
                jump beast_contrarian_end

            "{i}• [[Stand still.]{/i}" if beast_cant_eaten == False:
                if wild_encountered:
                    $ beast_cant_eaten = True
                    voice "audio/voices/mound/bonus/path.flac"
                    mound "This path is already worn by travel and has been seen by one of my many eyes. You cannot walk it again. Change your course.\n"
                    voice "audio/voices/ch2/beast/_encounter/hero/31.flac"
                    hero "Wait... what?!\n"
                    jump beast_attack_3
                jump beast_encounter_1_eaten

label beast_attack_4:
    voice "audio/voices/ch2/beast/_encounter/hunted/26.flac"
    hunted "She's more tense this time. She means this next blow to be the last.\n"
    voice "audio/voices/ch2/beast/_encounter/narrator/46.flac"
    n "The mere thought of moving again makes your bloodied side ache.\n"
    voice "audio/voices/ch2/beast/_encounter/hero/25.flac"
    hero "We're exhausted. We're bleeding.\n"
    voice "audio/voices/ch2/beast/_encounter/hunted/27.flac"
    hunted "We're still alive. We owe it to ourselves to move.\n"
    label beast_attack_4_menu:
        menu:
            extend ""

            "{i}• [[Again...]{/i}":
                jump beast_skeptic_end

            "{i}• [[Wait for her to strike, and hit her back.]{/i}" if blade_held:
                jump beast_stubborn_end

            "{i}• [[Play dead.]{/i}"if beast_cant_eaten == False:
                if wild_encountered:
                    $ beast_cant_eaten = True
                    voice "audio/voices/mound/bonus/path.flac"
                    mound "This path is already worn by travel and has been seen by one of my many eyes. You cannot walk it again. Change your course.\n"
                    voice "audio/voices/ch2/beast/_encounter/hero/31.flac"
                    hero "Wait... what?!\n"
                    jump beast_attack_4
                jump beast_contrarian_end

            "{i}• [[Stand still.]{/i}" if beast_cant_eaten == False:
                if wild_encountered:
                    $ beast_cant_eaten = True
                    voice "audio/voices/mound/bonus/path.flac"
                    mound "This path is already worn by travel and has been seen by one of my many eyes. You cannot walk it again. Change your course.\n"
                    voice "audio/voices/ch2/beast/_encounter/hero/31.flac"
                    hero "Wait... what?!\n"
                    jump beast_attack_4
                jump beast_encounter_1_eaten

label beast_stubborn_end:
    if beast_player_wounded and wild_encountered == False:
        $ beast_captured_injured = True
        voice "audio/voices/ch2/beast/_encounter/hunted/28.flac"
        hunted "This isn't going to work. We're in her domain, and we are bleeding.\n"
        voice "audio/voices/ch2/beast/_encounter/hero/26.flac"
        hero "Exactly. If we don't do something now, we're finished.\n"
        play audio "audio/final/Tower_KnifeBlow_4.flac"
        voice "audio/voices/ch2/beast/_encounter/narrator/47.flac"
        hide beast onlayer back
        hide fore onlayer inyourface
        hide fore onlayer back
        hide fore onlayer front
        hide farback onlayer farback
        hide bg onlayer back
        show bg beast feign onlayer back at Position(ypos=1125)
        show panel beast fight2 3 onlayer front at Position(ypos=1125)
        with dissolve
        n "As the Princess lunges at you from the shadows once more, you tighten your grip, lashing out with the blade.\n"
        voice "audio/voices/ch2/beast/_encounter/narrator/48.flac"
        n "But your injured side stretches and tears as you move, and you find yourself slowed by the sudden pain.\n"
        voice "audio/voices/ch2/beast/_encounter/narrator/49.flac"
        play audio "audio/final/beast_charge_devour.flac"
        hide beast onlayer back
        hide panel onlayer front
        hide fore onlayer inyourface
        hide fore onlayer back
        hide fore onlayer front
        hide farback onlayer farback
        hide bg onlayer back
        show beast swallow full onlayer back
        with dissolve
        n "The Princess, maw unhinged and dripping, eyes fierce and full of hunger, closes in on you. You are devoured.\n"
        jump beast_eaten_late_join
    else:
        $ achievement.grant("ACH_BEAST_FIGHT")
        voice "audio/voices/ch2/beast/_encounter/hunted/29.flac"
        hunted "This isn't going to work. We're in her domain. We just have to stay alive.\n"
        voice "audio/voices/ch2/beast/_encounter/hero/27.flac"
        hero "If we keep dodging her forever, we're going to get tired. We're going to slip up. We have to take a risk.\n"
        $ default_mouse = "blood"
        play secondary "audio/final/beast_charge_devour.flac"
        play audio "audio/final/Tower_KnifeBlow_4.flac"
        voice "audio/voices/ch2/beast/_encounter/narrator/50.flac"
        hide beast onlayer back
        hide fore onlayer inyourface
        hide fore onlayer back
        hide fore onlayer front
        hide farback onlayer farback
        hide bg onlayer back
        show bg beast feign onlayer back at Position(ypos=1125)
        show panel beast fight 3 onlayer front at Position(ypos=1125)
        with dissolve
        n "As the Princess lunges from the shadows once more, you tighten your grip on the blade and lash out. It strikes, cutting deep, and the Princess loses her focus, crying out in pained surprise as she crashes into you.\n"
        $ gallery_beast.unlock_item(13)
        voice "audio/voices/ch2/beast/_encounter/narrator/51.flac"
        play audio "audio/one_shot/tackle.flac"
        hide bg onlayer back
        hide panel onlayer front
        show beast fight interstitial onlayer back at Position(ypos=1125)
        show fore beast fight interstitial onlayer front at Position(ypos=1125)
        with dissolve
        n "You're sent sprawling, and can already feel the massive bruise blossoming on your ribs as she scrambles back into the darkness.\n"
        voice "audio/voices/ch2/beast/_encounter/hero/28.flac"
        hero "Ha! Look at that! We wounded her.\n"
        voice "audio/voices/ch2/beast/_encounter/hunted/30.flac"
        hunted "And she wounded us. Bad trade.\n"
        voice "audio/voices/ch2/beast/_encounter/princess/33.flac"
        show beast fight interstitial talk onlayer back at Position(ypos=1125)
        sp "That hurt. Are you just the cornered animal you seem to be, or could you be a rival?\n"
        play audio "audio/final/Tower_KnifeBlow_4.flac"
        voice "audio/voices/ch2/beast/_encounter/narrator/52.flac"
        play secondary "audio/final/Beast_ClawsRipping_1.flac"
        queue secondary "audio/final/Beast_ClawsRipping_2.flac"
        queue secondary "audio/final/Beast_ClawsRipping_3.flac"
        hide beast onlayer back
        hide fore onlayer front
        show bg beast feign onlayer back at Position(ypos=1125)
        show panel beast fight2 3 onlayer front at Position(ypos=1125)
        with dissolve
        n "She rears back, then leaps at you, more forceful, more ferocious, more serious. The scuffle is brief, and though you inflict a few deep wounds, you find yourself quickly overwhelmed by her savagery.\n"
        play audio "audio/final/Beast_Roar_2.flac"
        play secondary "audio/one_shot/tackle.flac"
        voice "audio/voices/ch2/beast/_encounter/narrator/53.flac"
        hide panel onlayer front
        hide bg onlayer back
        show bg beast fight 3 onlayer back at Position(ypos=1125)
        show cg beast fight sequence onlayer front at Position(ypos=1125)
        with dissolve
        n "You collapse to the floor, and she wastes no time before pouncing on you in a flurry of claws and blood, your nerves barely able to keep up with the onslaught.\n"
        stop music2 fadeout 5.0
        voice "audio/voices/ch2/beast/_encounter/narrator/53a.flac"
        hide bg onlayer back
        hide cg onlayer front
        show bg beast fight 3 final onlayer farback at Position(ypos=1125)
        show beast fight 3 final onlayer back at Position(ypos=1125)
        with dissolve
        n "By the end, you're lying in a nest of your own intestines, spine severed, blood rapidly draining out onto the jungle floor.\n"
        voice "audio/voices/ch2/beast/_encounter/narrator/54.flac"
        show beast fight 3 final prod onlayer back
        with dissolve
        n "The Princess, drenched in both her blood and yours, idly prods your body.\n"
        voice "audio/voices/ch2/beast/_encounter/princess/34.flac"
        show beast fight 3 final prod talk onlayer back
        with dissolve
        sp "Oh, that's it, then. Cornered animal it was.\n"
        voice "audio/voices/ch2/beast/_encounter/princess/35.flac"
        show beast fight 3 final talk onlayer back
        with dissolve
        sp "Do better next time. I still need to devour you, and it doesn't count if you're dead.\n"
        show beast fight 3 final onlayer back
        with dissolve
        $ trait_stubborn = True
    jump beast_2_ending_join

label beast_contrarian_end:
    $ beast_contrarian = True
    voice "audio/voices/ch2/beast/_encounter/hero/29.flac"
    hero "We're playing dead?\n"
    voice "audio/voices/ch2/beast/_encounter/hunted/31.flac"
    hunted "It's unexpected. It could work.\n"
    $ achievement.grant("ACH_BEAST_DUSTIN")
    voice "audio/voices/ch2/beast/_encounter/narrator/55.flac"
    stop music2 fadeout 3.0
    play audio "audio/one_shot/tackle.flac"
    play secondary "audio/one_shot/new/STP_chainsmovement_1.flac"
    hide beast onlayer back
    hide fore onlayer inyourface
    hide fore onlayer back
    hide fore onlayer front
    hide farback onlayer farback
    hide bg onlayer back
    show bg beast feign onlayer back at Position(ypos=1125)
    with dissolve
    n "As the Princess lunges from the shadows once more, you collapse to the ground, feigning death. She lands directly on top of you with her full weight, nearly crushing you into the dirt, but then... silence. Only broken by the sound of your beating heart.\n"
    voice "audio/voices/ch2/beast/_encounter/hero/30.flac"
    hero "It actually worked, didn't it? Only... what do we do to make her leave? Do we just keep playing dead?\n"
    play audio "audio/final/BEAST_LionSniffNEW_1.flac"
    voice "audio/voices/ch2/beast/_encounter/narrator/56.flac"
    n "She sniffs at you, shifting her weight uncomfortably as her face finds yours. Her breaths are hot and oppressive against your skin.\n"
    $ gallery_beast.unlock_item(9)
    $ renpy.save_persistent()
    show beast feign blurred onlayer back at Position(ypos=1125)
    with dissolve
    voice "audio/voices/ch2/beast/_encounter/princess/36.flac"
    sp "Have you seen my great big eyes? Because they see you, fledgling. They see your heartbeat pulsing in your throat.\n"
    voice "audio/voices/ch2/beast/_encounter/hunted/32.flac"
    show beast feign onlayer back at Position(ypos=1125)
    with dissolve
    hunted "Move! Now!\n"
    voice "audio/voices/ch2/beast/_encounter/narrator/57.flac"
    play audio "audio/final/Beast_WetJawsCrackSwallowPlayer_1.flac"
    hide beast onlayer back
    hide bg onlayer back
    show beast swallow short onlayer back
    with dissolve
    n "But it's too late for you to move. Her jaw unhinges, and she swallows you whole.\n"
    jump beast_eaten_late_join


label beast_skeptic_end:
    if beast_fled:
        voice "audio/voices/ch2/beast/_encounter/narrator/58.flac"
        n "You sprint for the stairs, but as soon as your take your first step—\n{w=2.95}{nw}"
        show screen disableclick(0.5)
        voice "audio/voices/mound/bonus/path.flac"
        mound "This path is already worn by travel and has been seen by one of my many eyes. You cannot walk it again. Change your course.\n"
        menu:
            extend ""

            "{i}• [[Dodge.]{/i}":
                voice "audio/voices/ch2/beast/_encounter/hero/31.flac"
                hero "Wait... what?!\n"

    if beast_player_wounded:
        voice "audio/voices/ch2/beast/_encounter/narrator/59.flac"
        hide beast onlayer back
        hide fore onlayer inyourface
        hide fore onlayer back
        hide fore onlayer front
        hide farback onlayer farback
        hide bg onlayer back
        play audio "audio/final/beast_dodge_1.flac"
        play secondary "audio/one_shot/new/STP_chainsmovement_1.flac"
        show beast dodge full onlayer back at flip
        with Dissolve(2.0)
        n "Once again, you narrowly avoid the full force of the impact. And once again, you are too slow to come away unscathed. You're starting to get tired. You're making mistakes.\n"

    else:
        $ beast_player_wounded = True
        voice "audio/voices/ch2/beast/_encounter/narrator/60.flac"
        hide beast onlayer back
        hide fore onlayer inyourface
        hide fore onlayer back
        hide fore onlayer front
        hide farback onlayer farback
        hide bg onlayer back
        play audio "audio/final/beast_dodge_1.flac"
        play secondary "audio/one_shot/new/STP_chainsmovement_1.flac"
        show beast dodge full onlayer back at flip
        with Dissolve(2.0)
        n "You manage to avoid her slavering jaws, but you aren't fast enough to evade the whole of her titanic momentum. She grazes you, the force of it enough to skin you all along your side, leaving a line of red, raw flesh.\n"
        voice "audio/voices/ch2/beast/_encounter/hero/32.flac"
        hero "It's like being sideswiped by sandpaper, how is she that fast?!\n"

    voice "audio/voices/ch2/beast/_encounter/hero/33.flac"
    hero "This isn't working. We have to do something, we have to figure out a plan.\n"
    voice "audio/voices/ch2/beast/_encounter/hunted/17.flac"
    hunted "Don't plan ahead. Act on the now. All that matters is that we stay alive.\n" id beast_skeptic_end_9343ce09
    voice "audio/voices/ch2/beast/_encounter/hero/34.flac"
    hero "We're trying, but we can't keep this up much longer.\n"
    voice "audio/voices/ch2/beast/_encounter/hunted/33.flac"
    hunted "We have to. We keep up, or we die.\n"
    #voice "audio/voices/ch2/beast/_encounter/narrator/61.flac"
    #n "The Princess chuckles from the shadows.\n"
    voice "audio/voices/ch2/beast/_encounter/princess/37.flac"
    spmid "You're getting slow.\n"
    play secondary "audio/final/Beast_ClawsRipping_1.flac"
    queue secondary "audio/final/Beast_ClawsRipping_2.flac"
    queue secondary "audio/final/Beast_ClawsRipping_3.flac"
    voice "audio/voices/ch2/beast/_encounter/narrator/62.flac"
    hide beast onlayer back
    show bg beast fight 3 onlayer back at Position(ypos=1125)
    show cg beast fight 3 onlayer front at Position(ypos=1125)
    with Dissolve(3.0)
    n "She seizes the opportunity, lunging once again from the darkness, fangs bared and claws flashing. She attacks over, and over, and over, and each time she leaves with a little piece of you.\n"
    voice "audio/voices/ch2/beast/_encounter/hero/35.flac"
    hero "Too tired to think. But we have to think.\n"
    voice "audio/voices/ch2/beast/_encounter/hunted/34.flac"
    hunted "We have to move.\n"
    voice "audio/voices/ch2/beast/_encounter/narrator/63.flac"
    play audio "audio/final/beast_charge_devour.flac"
    hide cg onlayer front
    hide beast onlayer back
    hide fore onlayer inyourface
    hide fore onlayer back
    hide fore onlayer front
    hide farback onlayer farback
    hide bg onlayer back
    show beast swallow full onlayer back
    with dissolve
    n "It's too late. Before you get the chance to react, it's over. She makes her last foray from the dark corners of the room, unhinging her dripping maw, her eyes fierce and full of hunger.\n"
    voice "audio/voices/ch2/beast/_encounter/narrator/64.flac"
    $ achievement.grant("ACH_BEAST_DODGE")
    play audio "audio/one_shot/tackle.flac"
    play secondary "audio/final/Beast_ClawsRipping_3.flac"
    n "You do you best to dive out of the way, and you... partially succeed.\n"
    voice "audio/voices/ch2/beast/_encounter/hero/36.flac"
    hero "... Partially?\n"
    voice "audio/voices/ch2/beast/_encounter/narrator/65.flac"
    n "Yes. The Princess fails to swallow you whole. She only swallows your lower body.\n"
    voice "audio/voices/ch2/beast/_encounter/hero/37.flac"
    hero "That's just as bad! That's worse, even!\n"
    voice "audio/voices/ch2/beast/_encounter/hunted/35.flac"
    hunted "It's death, either way. At least this will be a faster end.\n"
    $ gallery_beast.unlock_item(14)
    voice "audio/voices/ch2/beast/_encounter/narrator/66.flac"
    play audio "audio/final/Beast_LionRipping_1.flac"
    hide beast onlayer back
    show beast skeptic 1 onlayer back at Position(ypos=1125)
    with dissolve
    n "You look down to see that the dirt between you is strewn with your intestines, trailing all the way up and disappearing behind her blood-stained teeth. Your legs are nowhere to be seen. You start to go into shock.\n"
    voice "audio/voices/ch2/beast/_encounter/narrator/67.flac"
    show beast skeptic 2 start onlayer back
    show fore beast skeptic 2 onlayer front at Position(ypos=1125)
    with Dissolve(1.5)
    n "The Princess, bloody saliva dripping from her lips, idly gnaws on what's left of you as you rapidly fade away.\n"
    voice "audio/voices/ch2/beast/_encounter/princess/38.flac"
    show beast skeptic 2 talk onlayer back
    with dissolve
    sp "I didn't mean to do that. I still need to devour you, and it doesn't count if you're dead.\n"
    show beast skeptic 2 neutral onlayer back
    $ trait_skeptic = True
    label beast_2_ending_join:
        voice "audio/voices/ch2/beast/_encounter/hero/38.flac"
        hero "But we're not dead, we're—\n{w=1.75}{nw}"
        show screen disableclick(0.5)
        stop music fadeout 3.0
        stop sound fadeout 3.0
        stop secondary fadeout 3.0
        stop tertiary fadeout 3.0
        stop music2 fadeout 3.0
        voice "audio/voices/ch2/beast/_encounter/narrator/68.flac"
        if trait_stubborn:
            $ gallery_beast.unlock_item(6)
            $ gallery_beast.unlock_item(7)
            $ gallery_beast.unlock_item(8)
            $ renpy.save_persistent()
        else:
            $ gallery_beast.unlock_item(12)
            $ renpy.save_persistent()
        scene bg black onlayer back
        hide cg onlayer back
        hide fore onlayer front
        hide cg onlayer front
        hide beast onlayer back
        hide fore onlayer inyourface
        hide fore onlayer back
        hide fore onlayer front
        hide farback onlayer farback
        hide bg onlayer back
        hide bg onlayer farback
        with fade
        n "But you don't have time to protest her premature observation of your death, because everything goes dark and you die.\n"
        hide bg onlayer back
        scene bg black
        with fade
        $ default_mouse = "default"
        jump beast_2_start
        # end

    #end

label beast_devour_die:
    play audio "audio/final/Beast_AcidSizzle_3.flac"
    voice "audio/voices/ch2/beast/_encounter/narrator/69.flac"
    show bg beast heart onlayer inyourface at Position(ypos=1125)
    with Dissolve(3.5)
    n "But will can never truly exceed the limits of the flesh. Your vision finally begins to blur, your eyes clouding over as they melt in their sockets.\n"
    stop music fadeout 5.0
    stop music2 fadeout 5.0
    stop sound fadeout 5.0
    stop secondary fadeout 5.0
    stop tertiary fadeout 5.0
    voice "audio/voices/ch2/beast/_encounter/narrator/70.flac"
    scene bg black onlayer farback
    hide bg onlayer inyourface
    hide player onlayer inyourface
    hide fore onlayer front
    hide bg onlayer back
    with dissolve
    n "What little air remains in this rancid stew of flesh and slippery organs is finally too foul to breathe, and your lungs mercifully give out before you have to suffer another burning, liquefying moment. Everything goes dark and you die.\n"
    $ quick_menu = False
    $ wild_source = "beast"
    if beast_contrarian:
        $ wild_bonus_voice = "contrarian"
    else:
        $ wild_bonus_voice = "broken"
    hide bg onlayer farback with fade
    jump wild_start
    # END

return
