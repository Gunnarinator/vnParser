label basement_1_knife_start:

    default can_slay = True
    default must_spectre = False
    if tower_encountered and prisoner_encountered and nightmare_encountered and adversary_encountered:
        # technically requires spectre OR razor
        $ must_spectre = True

    if tower_encountered and nightmare_encountered and adversary_encountered:
        $ can_slay = False


    #knife route image defines

    #knife route sprite defines
    play sound "audio/looping/ambient_basement_interior.ogg" loop
    scene bg basement stairs onlayer farback at Position(ypos=1125)
    show front basement stairs onlayer farback at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    voice "audio/voices/ch1/shared/narrator/ch1_share_n_1.flac"
    n "The door to the basement creaks open, revealing a staircase faintly illuminated by an unseen light in the room below. This is an oppressive place. The air feels heavy and damp, a hint of rot filtering from the ancient wood. If the Princess really lives here, slaying her is probably doing her a favor.\n"
    voice "audio/voices/ch1/knife/narrator/knife_n_0.flac"
    n "Her voice carries up the stairs.\n"
    #re-read
    voice "audio/voices/ch1/knife/princess/stab_p_1.flac"
    p "Who's there?\n"
    voice "audio/voices/ch1/knife/hero/k_h_1.flac"
    #hero "It's hypnotizing. It's the kind of voice you only have to hear once to remember it for the rest of your life."
    hero "She sounds... dangerous...  It's almost as if she's the one in charge down here.\n"
    voice "audio/voices/ch1/knife/narrator/knife_n_1.flac"
    n "Don't let it fool you. It's all part of the manipulation.\n"
    default basement_1_knife_kill_joke = False
    menu:
        extend ""

        "{i}• ''Hi!''{/i}":
            voice "audio/voices/ch1/knife/princess/stab_p_2b.flac"
            p "Don't be a stranger. It's been so long since I've had any visitors, come on down.\n"

        "{i}• ''Just checking in on you.''{/i}":
            voice "audio/voices/ch1/knife/princess/stab_p_3b.flac"
            p "Oh? It's been so long since anyone's come down here. I was starting to think they'd forgotten about me.\n"

        "{i}• ''Hey, I think I'm here to kill you?''{/i}":
            $ basement_1_knife_kill_joke = True
            #voice "audio/voices/ch1/knife/princess/stab_p_4.flac"
            #p "You must have the wrong address.\n"
            voice "audio/voices/ch1/knife/princess/stab_p_4.flac"
            p "Ohohohoho, are you now? Why don't you come down and let me take a look at you.\n"
            voice "audio/voices/ch1/knife/narrator/knife_n_2.flac"
            n "Great job, you gave away the element of surprise. Good luck, hero.\n"

        "{i}• [[Continue down the stairs.]{/i}":
            voice "audio/voices/ch1/knife/narrator/knife_n_3.flac"
            n "Good. You're still listening to reason.\n"

    $gallery_zch1.unlock_item(4)
    $renpy.save_persistent()
    $ quick_menu = False
    play audio "audio/one_shot/footsteps_creaky.flac"
    hide bg basement stairs onlayer farback at Position(ypos=1125)
    hide front basement stairs onlayer farback at Position(ypos=1125)
    with fade
    scene bg basement distant onlayer farback at Position(ypos=1125)
    show back basement distant onlayer back at Position(ypos=1125)
    show princess d down onlayer back at Position(ypos=1125)
    with fade
    show princess d haughty onlayer back at Position(ypos=1125)
    with dissolve
    if persistent.quick_menu:
        $ quick_menu = True
    voice "audio/voices/ch1/knife/narrator/knife_n_4.flac"
    n "You walk down the stairs and lock eyes with the Princess. There's a heavy chain around her wrist, binding her to the far wall of the basement.\n"
    voice "audio/voices/ch1/knife/hero/k_h_2.flac"
    hero "She's so coldly beautiful... is she really a threat to the world?\n"
    voice "audio/voices/ch1/knife/narrator/knife_n_5.flac"
    n "Focus on the task at hand.\n"
    show princess d squint talk onlayer back with dissolve
    if basement_1_knife_kill_joke:
        voice "audio/voices/ch1/knife/princess/stab_p_5b.flac"
        p "You weren't kidding when you said you were here to kill me.\n"
    else:
        voice "audio/voices/ch1/knife/princess/stab_p_6b.flac"
        p "And there you are. Are you here to kill me or something?\n"
        #p "Are you here to kill me or something?\n"
    show princess d haughty onlayer back with dissolve
    default basement_1_knife_confronted_steel = False
    label basement_1_knife_confronted:
        menu:
            extend ""

            "{i}• ''What? No way. Why would you even think that?''{/i}" if must_spectre == False:
                $ basement_1_nerves_steeled_hesitated = True
                $ can_spectre = False
                show princess d confident talk onlayer back with dissolve
                voice "audio/voices/ch1/knife/princess/stab_p_7b.flac"
                p "That giant knife you're holding kind of gives it away, doesn't it?\n"
                #p "Uh... maybe because of the giant knife you're holding?\n"
                show princess d confident onlayer back with dissolve
                voice "audio/voices/ch1/knife/hero/k_h_3.flac"
                hero "The blade! Of course she doesn't want to talk. Who'd want to have a conversation at knife point? We should drop it.\n"

            "{i}• ''Yeah, it wasn't a joke.''{/i}" if basement_1_knife_kill_joke:
                show princess d confident talk onlayer back with dissolve
                voice "audio/voices/ch1/knife/princess/stab_p_8.flac"
                p "I know. You brought a knife with you and everything. But you don't have to try and kill me. You could always toss that scrap of metal to the ground, and give the two of us a chance to talk things out.\n"
                #p "Okay, well, what if you {i}didn't{/i} kill me?\n"
                voice "audio/voices/ch1/knife/hero/k_h_4.flac"
                show princess d confident onlayer back with dissolve
                hero "She makes a compelling point. What if we didn't kill her? What if we just dropped the blade and {i}talked{/i}?\n"

            "{i}• ''Okay, yeah, you caught me. I'm here to slay you.''{/i}" if basement_1_knife_kill_joke == False and must_spectre == False:
                #$ basement_1_nerves_steeled_hesitated = True
                $ can_spectre = False
                show princess d squint talk onlayer back with dissolve
                voice "audio/voices/ch1/knife/princess/stab_p_9.flac"
                p "That isn't a good idea. Just drop the knife, and maybe the two of us can talk things out.\n"
                #p "Well, you shouldn't.\n"
                voice "audio/voices/ch1/knife/hero/k_h_5.flac"
                show princess d squint onlayer back with dissolve
                hero "She's right. We shouldn't. We should just drop the blade.\n"

            "{i}• ''Nuh... nuh uh!''{/i}" if basement_1_knife_kill_joke == False and must_spectre == False:
                $ basement_1_nerves_steeled_hesitated = True
                $ can_spectre = False
                show princess d squint talk onlayer back with dissolve
                voice "audio/voices/ch1/knife/princess/stab_p_10.flac"
                p "Then drop the knife.\n"
                show princess d haughty onlayer back with dissolve
                voice "audio/voices/ch1/knife/hero/k_h_6.flac"
                hero "We should. It'd go a long way to building trust with her.\n"

            "{i}• ''I haven't decided yet.''{/i}" if must_spectre == False:
                default knife_queue_undecided = False
                $ basement_1_nerves_steeled_hesitated = True
                $ knife_queue_undecided = True
                $ can_spectre = False
                show princess d haughty talk onlayer back with dissolve
                voice "audio/voices/ch1/knife/princess/stab_p_11.flac"
                p "How about you drop the knife and the two of us just talk?\n"
                voice "audio/voices/ch1/knife/hero/k_h_7.flac"
                show princess d squint onlayer back with dissolve
                hero "Look how reasonable she's being. We should just drop the blade and talk things out.\n"

            "{i}• ''I'm just here to talk.''{/i}" if must_spectre == False:
                $ basement_1_nerves_steeled_hesitated = True
                $ can_spectre = False
                show princess d squint talk onlayer back with dissolve
                voice "audio/voices/ch1/knife/princess/stab_p_12.flac"
                p "Then why did you bring a knife with you? How about you drop it and then we can chat.\n"
                #p "So... why'd you bring a knife with you? How about you drop it and then we can chat.\n"
                show princess d squint onlayer back with dissolve
                voice "audio/voices/ch1/knife/hero/k_h_8.flac"
                hero "She makes a compelling point. What if we just dropped the blade and {i}talked{/i}? Look at her. It's not like she's a threat.\n"


            "{i}• [[Steel your nerves and step forward.]{/i}":
                $ basement_1_knife_confronted_steel = True
                jump basement_1_nerves_steeled

    voice "audio/voices/ch1/knife/narrator/knife_n_6.flac"
    n "Don't you dare.\n"
    show princess d haughty onlayer back with dissolve
    voice "audio/voices/ch1/knife/hero/k_h_9.flac"
    hero "It's fine. We can decide what we want to do {i}after{/i} we talk to her. Maybe she really is a monster. But killing someone in cold blood isn't very becoming of us.\n"

    menu:
        extend ""

        "{i}• [[Drop it.]{/i}" if must_spectre == False:
            $ blade_held = False
            $ default_mouse = "default"
            play audio "audio/one_shot/knife_bounce_several.flac"
            voice "audio/voices/ch1/knife/narrator/knife_n_7.flac"
            n "{i}Sigh{/i}. The blade tumbles out of your trembling hands and drops to the floor with an unceremonious clang.\n"
            show princess d haughty talk onlayer back with dissolve
            if knife_queue_undecided == False:
                voice "audio/voices/ch1/knife/princess/stab_p_13.flac"
                p "Thank you. Maybe now we can just... talk.\n"
            else:
                voice "audio/voices/ch1/knife/princess/stab_p_13b.flac"
                p "Thank you.\n"
            jump basement_1_knife_dropped

        "{i}• [[Tighten your grip.]{/i}":
            #$ basement_1_nerves_steeled_hesitated = True
            play audio "audio/one_shot/knife_tighten.flac"
            voice "audio/voices/ch1/knife/narrator/knife_n_8.flac"
            show princess d neutral onlayer back with dissolve
            n "You ignore the trembling in your hands and tighten your grip on the blade.\n"
            show princess d haughty talk onlayer back with dissolve
            voice "audio/voices/ch1/knife/princess/stab_p_14.flac"
            p "You poor thing, your hands are shaking. Are you... scared of me?\nBecause you should be.\n"
            jump basement_1_nerves_steeled


label basement_1_nerves_steeled:
    default basement_1_nerves_steeled = False
    default basement_1_nerves_steeled_hesitated = False
    default basement_1_nerves_armed = False
    default basement_1_nerves_fear = False
    default basement_1_nerves_steeled_hesitated_explore = False
    default can_spectre = True
    $ basement_1_nerves_steeled = True
    play audio "audio/one_shot/footstep_mines.flac"
    voice "audio/voices/ch1/knife/narrator/knife_n_9.flac"
    show princess d squint onlayer back with dissolve
    n "You step forward, your grip on the blade tightening as you steel your resolve.\n"
    if basement_1_nerves_steeled_hesitated == False:
        show princess d squint talk onlayer back with dissolve
        voice "audio/voices/ch1/knife/princess/stab_p_15.flac"
        p "Oh? No talking, then? Fine. What even makes you think you can kill me?\n"
    show princess d confident talk onlayer back with dissolve
    voice "audio/voices/ch1/knife/princess/stab_p_16.flac"
    p "I'm probably chained up in this basement for a reason, right? And if that knife is the only weapon you have, you'll have to get close enough to use it.\n"
    voice "audio/voices/ch1/knife/princess/stab_p_16b.flac"
    show princess d haughty talk onlayer back with dissolve
    p "So... you should just drop it. Best not to risk finding out what I can do.\n"
    show princess d haughty onlayer back with dissolve
    #voice "audio/voices/ch1/knife/hero/k_h_10.flac"
    #hero "Do you hear the conviction in her voice? Do you see that razor sharpness in her gaze? I don't think she's bluffing.\n"
    voice "audio/voices/ch1/knife/narrator/knife_n_10.flac"
    n "She's unarmed. If you hesitate now, it'll be too late. {i}End this{/i}.\n"
    label basement_1_nerves_steeled_menu:
        menu:
            extend ""

            "{i}• (Explore) What if she isn't bluffing? What if she kills us?{/i}" if basement_1_nerves_steeled_hesitated_explore == False and tower_encountered == False and must_spectre == False:
                $ basement_1_nerves_steeled_hesitated = True
                $ basement_1_nerves_steeled_hesitated_explore = True
                $ basement_1_nerves_fear = True
                $ can_spectre = False
                voice "audio/voices/ch1/knife/narrator/knife_n_11.flac"
                n "If you go into this expecting to die, you're going to die.\n"
                show princess d confident talk onlayer back with dissolve
                voice "audio/voices/ch1/knife/princess/stab_p_18.flac"
                p "Hesitating? Why don't you drop the knife and the two of us can be civilized with each other.\n"
                jump basement_1_nerves_steeled_menu

            "{i}• (Explore) Are you {b}sure{/b} she's not armed?{/i}" if basement_1_nerves_steeled_hesitated_explore == False and razor_encountered == False:
                $ basement_1_nerves_steeled_hesitated_explore = True
                $ basement_1_nerves_steeled_hesitated = True
                $ basement_1_nerves_armed = True
                $ can_spectre = False
                voice "audio/voices/ch1/knife/narrator/knife_n_12.flac"
                n "I'm positive.\n"
                voice "audio/voices/ch1/knife/hero/k_h_11.flac"
                hero "I'm not. But we'll keep our eyes peeled. If she has a weapon, she'll have to draw it before she can use it.\n"
                show princess d confident talk onlayer back with dissolve
                voice "audio/voices/ch1/knife/princess/stab_p_18.flac"
                p "Hesitating? Why don't you drop the knife and the two of us can be civilized with each other.\n"
                jump basement_1_nerves_steeled_menu

            "{i}• (Explore) ''I'm sorry. Can we just talk?''{/i}" if basement_1_nerves_steeled_hesitated_explore == False and must_spectre == False:
                $ basement_1_nerves_steeled_hesitated_explore = True
                $ basement_1_nerves_steeled_hesitated = True
                $ can_spectre = False
                voice "audio/voices/ch1/knife/narrator/knife_n_13.flac"
                n "You're so close! Don't give up, you've come this far.\n"
                voice "audio/voices/ch1/knife/hero/k_h_12.flac"
                hero "No, this is a good idea. Maybe we can de-escalate things.\n"
                show princess d haughty talk onlayer back with dissolve
                voice "audio/voices/ch1/knife/princess/stab_p_19.flac"
                p "Oh, threatened, are we? You poor thing. Drop the knife and of course we can talk.\n"
                jump basement_1_nerves_steeled_menu

            "{i}• ''I'm not dropping the blade.''{/i}" if must_spectre == False:
                default basement_1_not_dropping_stare = False
                $ basement_1_nerves_steeled_hesitated = True
                $ can_spectre = False
                show princess d confident talk onlayer back with dissolve
                voice "audio/voices/ch1/knife/princess/stab_p_20.flac"
                p "Then I'm not talking to you.\n"
                show princess d confident onlayer back with dissolve
                menu:
                    extend ""

                    "{i}• ''Fine then, I guess we're at an impasse!''{/i}":
                        show princess d confident talk onlayer back with dissolve
                        voice "audio/voices/ch1/knife/princess/stab_p_21.flac"
                        p "I guess we are!\n"
                        show princess d confident onlayer back with dissolve
                        voice "audio/voices/ch1/knife/narrator/knife_n_14.flac"
                        n "For the love of everything, just slay her already!\n"
                        voice "audio/voices/ch1/knife/hero/k_h_13.flac"
                        hero "Or drop the blade. Do {i}something{/i}.\n"

                    "{i}• [[Squint at the Princess while holding onto the blade.]{/i}":
                        $ basement_1_not_dropping_stare = True
                        voice "audio/voices/ch1/knife/narrator/knife_n_15.flac"
                        n "You stare at the Princess, squinting.\n"
                        voice "audio/voices/ch1/knife/narrator/knife_n_16.flac"
                        show princess d squint onlayer back with dissolve
                        n "She squints back.\n"
                        voice "audio/voices/ch1/knife/hero/k_h_14.flac"
                        hero "The two of you are going to do this forever, aren't you?\n"

                    "{i}• [[Drop the blade.]{/i}":
                        $ can_spectre = False
                        jump basement_1_knife_dropped_steeled

                    "{i}• [[Slay the Princess.]{/i}" if (can_spectre and (spectre_encountered == False or razor_encountered == False)) or (basement_1_nerves_armed and razor_encountered == False) or (basement_1_nerves_steeled_hesitated and (adversary_encountered == False or tower_encountered == False or nightmare_encountered == False)) or (basement_1_nerves_fear and tower_encountered == False) and can_slay:
                        jump basement_1_knife_slay_join

                menu:
                    extend ""

                    "{i}• ''Are you sure you don't want to talk?''{/i}":
                        $ basement_1_not_dropping_stare = True
                        show princess d haughty talk onlayer back with dissolve
                        voice "audio/voices/ch1/knife/princess/stab_p_22.flac"
                        p "Yeah. I'm sure.\n"
                        show princess d confident onlayer back with dissolve
                        voice "audio/voices/ch1/knife/narrator/knife_n_17.flac"
                        n "For goodness' sake, the two of you can't just stand around like this forever. Eventually, something is going to give, and I {i}highly{/i} recommend that you be the one to take the initiative here.\n"

                    "{i}• [[Squint at the Princess even harder.]{/i}" if basement_1_not_dropping_stare:
                        voice "audio/voices/ch1/knife/narrator/knife_n_18.flac"
                        n "You squint even harder.\n"
                        voice "audio/voices/ch1/knife/narrator/knife_n_19.flac"
                        n "So does she.\n"
                        voice "audio/voices/ch1/knife/hero/k_h_15.flac"
                        hero "At least nobody's dying right now...\n"
                        voice "audio/voices/ch1/knife/narrator/knife_n_20.flac"
                        n "You're going to have to make a choice. You can't keep squinting forever. Eventually, someone is going to have to blink.\n"

                    "{i}• [[Stare at the Princess while holding onto the blade.]{/i}" if basement_1_not_dropping_stare == False:
                        $ basement_1_not_dropping_stare = True
                        voice "audio/voices/ch1/knife/narrator/knife_n_21.flac"
                        n "You stare at the Princess, squinting fiercely.\n"
                        voice "audio/voices/ch1/knife/narrator/knife_n_22.flac"
                        show princess d squint onlayer back with dissolve
                        n "She squints back.\n"
                        voice "audio/voices/ch1/knife/hero/k_h_14.flac"
                        hero "The two of you are going to do this forever, aren't you?\n"
                        voice "audio/voices/ch1/knife/narrator/knife_n_23.flac"
                        n "You'll have to blink eventually. Just make a {i}choice{/i}.\n"

                    "{i}• [[Drop the blade.]{/i}":
                        jump basement_1_knife_dropped_steeled

                    "{i}• [[Slay the Princess.]{/i}" if (can_spectre and (spectre_encountered == False or razor_encountered == False)) or (basement_1_nerves_armed and razor_encountered == False) or (basement_1_nerves_steeled_hesitated and (adversary_encountered == False or tower_encountered == False or nightmare_encountered == False)) or (basement_1_nerves_fear and tower_encountered == False) and can_slay:
                        jump basement_1_knife_slay_join

                menu:
                    extend ""

                    "{i}• [[Drop the blade.]{/i}":
                        jump basement_1_knife_dropped_steeled

                    "{i}• [[Slay the Princess.]{/i}" if (can_spectre and (spectre_encountered == False or razor_encountered == False)) or (basement_1_nerves_armed and razor_encountered == False) or (basement_1_nerves_steeled_hesitated and (adversary_encountered == False or tower_encountered == False or nightmare_encountered == False)) or (basement_1_nerves_fear and tower_encountered == False) and can_slay:
                        jump basement_1_knife_slay_join

            "{i}• [[Drop the blade.]{/i}" if must_spectre == False:
                label basement_1_knife_dropped_steeled:
                    $ can_spectre = False
                    $ blade_held = False
                    $ default_mouse = "default"
                    play audio "audio/one_shot/knife_bounce_several.flac"
                    voice "audio/voices/ch1/knife/narrator/knife_n_24.flac"
                    show princess d confident onlayer back with dissolve
                    n "{i}Sigh{/i}. The blade tumbles out of your trembling hands and drops to the floor with an unceremonious clang.\n"
                    show princess d haughty talk onlayer back with dissolve
                    voice "audio/voices/ch1/knife/princess/stab_p_13.flac"
                    p "Thank you. Maybe now we can just... talk.\n"
                jump basement_1_knife_dropped

            "{i}• [[Slay the Princess.]{/i}" if (can_spectre and ((spectre_encountered == False or razor_encountered == False))) or (basement_1_nerves_armed and razor_encountered == False) or (basement_1_nerves_steeled_hesitated and (adversary_encountered == False or tower_encountered == False or nightmare_encountered == False)) or (basement_1_nerves_fear and tower_encountered == False) and can_slay:
                label basement_1_knife_slay_join:
                    default razor_pathetic = False
                    if basement_1_nerves_steeled_hesitated:
                        if basement_1_nerves_armed:
                            $ current_princess = "razor"
                            play secondary "audio/one_shot/footstep_run_dirt_short.flac"
                            queue secondary "audio/one_shot/knife_slash.flac"
                            voice "audio/voices/ch1/knife/narrator/knife_n_25.flac"
                            $ gallery_zch1.unlock_item(15)
                            $ renpy.save_persistent()
                            hide princess d onlayer back
                            hide bg basement distant onlayer farback
                            hide back basement distant onlayer back
                            show bg black onlayer back at Position(ypos=1125)
                            show knife slice onlayer front at yflip, Position(ypos=1125)
                            n "You charge the Princess, blade in hand, but unfortunately, your earlier suspicions proved correct. A blade of her own slips down her sleeve and catches you in the neck.\n"
                            hide bg black onlayer back
                            hide knife slice onlayer front
                            show bg generic onlayer farback at Position(ypos=1125)
                            show fury sprayed knife onlayer back at Position(ypos=1125)
                            with dissolve
                            play audio "audio/one_shot/blood_spray.flac"
                            voice "audio/voices/ch1/knife/narrator/knife_n_26.flac"
                            n "Blood sprays from the cut, your severed carotid artery painting the princess with strokes of red. You'd better finish your task quickly, before you run out of time.\n"
                            menu:
                                extend ""

                                "{i}• [[Die.]{/i}":
                                    $ current_princess = "razor"
                                    $ razor_pathetic = True
                                    voice "audio/voices/ch1/knife/narrator/knife_n_27.flac"
                                    n "Are you serious? {i}Sigh{/i}.\n"
                                    play audio "audio/one_shot/collapse.flac"
                                    voice "audio/voices/ch1/knife/narrator/knife_n_28.flac"
                                    hide bg generic onlayer farback
                                    hide fury sprayed knife onlayer back
                                    show bg black onlayer farback at Position(ypos=1125)
                                    with dissolve
                                    n "The wound in your neck is too much for you to bear, and you collapse to the floor of the basement, rapidly bleeding out.\n"
                                    play secondary "audio/one_shot/knife_bounce_several.flac"
                                    $ blade_held = False
                                    $ default_mouse = "default"
                                    hide bg onlayer back
                                    show bg fury stub betrayed loom onlayer farback at Position(ypos=1125)
                                    show fury sprayed loom onlayer back at Position(ypos=1125)
                                    with dissolve
                                    voice "audio/voices/ch1/knife/narrator/knife_n_29.flac"
                                    n "The Princess stands over you with an intense curiosity as you fade away.\n"
                                    voice "audio/voices/ch1/knife/princess/stab_p_24.flac"
                                    show fury sprayed loom talk onlayer back
                                    with dissolve
                                    sp "Oops.\n"
                                    #sp "I guess your heart really wasn't in it. How cute.\n"
                                    stop music fadeout 1.0
                                    stop sound fadeout 1.0
                                    hide bg fury stub betrayed loom onlayer farback
                                    hide fury sprayed loom talk onlayer back
                                    show bg black onlayer back at Position(ypos=1125)
                                    with dissolve
                                    voice "audio/voices/ch1/knife/narrator/knife_n_30.flac"
                                    $ persistent.death_count += 1

                                    n "Everything goes dark and you die.\n"
                                    hide bg black onlayer back with dissolve
                                    jump start_2

                                "{i}• [[Finish the job.]{/i}":
                                    default razor_loop1_killed = False
                                    $ current_princess = "razor"
                                    $ loop_1_princess_killed = True
                                    $ current_mutual_death += 1
                                    $ razor_loop1_killed = True
                                    play audio "audio/one_shot/knife_stab.flac"
                                    hide bg generic onlayer farback
                                    hide fury sprayed knife onlayer back
                                    show bg generic dark onlayer farback at Position(ypos=1125)
                                    show fury sprayed stabbed onlayer back at Position(ypos=1125)
                                    with dissolve
                                    $ default_mouse = "blood"
                                    voice "audio/voices/ch1/knife/narrator/knife_n_31.flac"
                                    n "With the last bit of your will, you press forward, sinking the blade deep into the Princess' heart.\n"
                                    voice "audio/voices/ch1/knife/princess/stab_p_25.flac"
                                    sp "O... oh.\n"
                                    play audio "audio/one_shot/collapse.flac"
                                    $ blade_held = False
                                    $ default_mouse = "default"
                                    hide bg generic dark onlayer farback
                                    hide fury sprayed stabbed onlayer back
                                    show bg fury mutual death onlayer back at Position(ypos=1125)
                                    show fury sprayed dying talk onlayer front at Position(ypos=1125)
                                    with dissolve
                                    voice "audio/voices/ch1/knife/narrator/knife_n_32.flac"
                                    n "The two of you collapse on the floor together, rapidly bleeding out.\n"
                                    voice "audio/voices/ch1/knife/princess/stab_p_26.flac"
                                    sp "Somehow I thought this would turn out a little differently.\nBut I wonder...\n"
                                    voice "audio/voices/ch1/knife/princess/stab_p_27.flac"
                                    sp "Do you really think {i}this{/i} was enough to stop me?\n"
                                    #sp "Do you {i}really{/i} think this is the end?\n"
                                    voice "audio/voices/ch1/knife/hero/k_h_16.flac"
                                    show fury sprayed dead onlayer front
                                    with dissolve
                                    hero "It's like she's convinced she can't die.\n"
                                    $ persistent.death_count += 1
                                    stop music fadeout 1.0
                                    stop sound fadeout 1.0
                                    hide bg onlayer back
                                    hide fury onlayer front
                                    show bg black onlayer back at Position(ypos=1125)
                                    with dissolve
                                    voice "audio/voices/ch1/knife/narrator/knife_n_33.flac"
                                    n "But you don't have time to worry over such things. Everything goes dark, and you die.\n"
                                    hide bg black onlayer back with dissolve
                                    jump start_2


                        elif basement_1_nerves_fear:
                            $ tower_unharmed = True
                            $ current_princess = "tower"
                            hide princess d onlayer back
                            hide bg basement distant onlayer farback
                            hide back basement distant onlayer back
                            show bg fury chain fear dodge onlayer farback at Position(ypos=1125)
                            show midground fury chain fear dodge onlayer back at Position(ypos=1125)
                            show fury chain fear dodge onlayer front at Position(ypos=1125)
                            show player clean knife onlayer inyourface at Position(ypos=1125)
                            with Dissolve(0.75)
                            play audio "audio/one_shot/footstep_run_dirt_short.flac"
                            voice "audio/voices/ch1/knife/narrator/knife_n_34.flac"
                            n "You charge the Princess, blade trembling in your hand, but you've already lost the battle.\n"
                            hide bg onlayer farback
                            hide midground onlayer back
                            hide fury onlayer front
                            hide player onlayer inyourface
                            show bg black onlayer back at Position (ypos=1125)
                            with dissolve
                            play secondary "audio/one_shot/punch_one.flac"
                            queue secondary "audio/one_shot/collapse.flac"
                            voice "audio/voices/ch1/knife/narrator/knife_n_34b.flac"
                            n "She casually sidesteps your thrust before knocking you to the ground with a single blow from her elbow.\n"
                            play audio "audio/one_shot/ear_ring.flac"
                            voice "audio/voices/ch1/knife/hero/k_h_17.flac"
                            hero "We shouldn't have hesitated.\n"
                            play audio "audio/one_shot/punch_many.flac"
                            voice "audio/voices/ch1/knife/narrator/knife_n_35.flac"
                            hide bg black onlayer back
                            show bg generic dark onlayer back at Position (ypos=1125)
                            show fury chain fear kick onlayer front at Position (ypos=1125)
                            show player defend razor onlayer inyourface at Position(ypos=1125)
                            with dissolve
                            n "But she doesn't stop there. She kicks you a few times for good measure, the pointed tip of her shoes feeling like a pickaxe against your fracturing bones, making sure you {i}stay{/i} down.\n"
                            play audio "audio/one_shot/knee_drop.flac"
                            voice "audio/voices/ch1/knife/narrator/knife_n_36.flac"
                            hide player onlayer inyourface
                            show fury chain fear kneel smirk onlayer front
                            with dissolve
                            n "As you lie crushed and broken on the basement floor, the Princess kneels on your throat with the kind of weight you didn't think her slight frame could possibly possess. As you gasp for air she eyes you with an intense curiosity.\n"
                            play secondary "audio/one_shot/knife_bounce_several.flac"
                            $ blade_held = False
                            $ default_mouse = "default"
                            voice "audio/voices/ch1/knife/narrator/knife_n_37.flac"
                            n "You shouldn't have let that fear creep into your heart. You had the upper hand, and now look at you.\n"
                            voice "audio/voices/ch1/knife/princess/stab_p_28.flac"
                            show fury chain fear kneel talk onlayer front with dissolve
                            sp "Is this really the best you could do? Look at you. Completely broken. I'd be lying if I said I wasn't a little disappointed.\n"
                            play audio "audio/one_shot/knee_kill.flac"
                            voice "audio/voices/ch1/knife/narrator/knife_n_38.flac"
                            show fury chain fear kneel smirk onlayer front with dissolve
                            n "She applies more pressure, slowly squeezing what's left of your life out of your lungs.\n"
                            voice "audio/voices/ch1/knife/hero/k_h_18.flac"
                            hero "This is the end, isn't it?\n"
                            voice "audio/voices/ch1/knife/narrator/knife_n_39.flac"
                            n "I'm afraid it is.\n"
                            $ persistent.death_count += 1
                            stop music fadeout 1.0
                            stop sound fadeout 1.0
                            hide bg onlayer back
                            hide fury onlayer front
                            show bg black onlayer back at Position(ypos=1125)
                            with dissolve
                            voice "audio/voices/ch1/knife/narrator/knife_n_40.flac"
                            n "Everything goes dark, and you die.\n"
                            hide bg black onlayer back with dissolve
                            jump start_2

                        else:
                            play audio "audio/one_shot/footstep_run_dirt_short.flac"
                            voice "audio/voices/ch1/knife/narrator/knife_n_41.flac"
                            hide princess d onlayer back
                            hide bg basement distant onlayer farback
                            hide back basement distant onlayer back
                            show bg fury chain doubt dodge onlayer farback at Position(ypos=1125)
                            show fury chain doubt dodge onlayer front at Position(ypos=1125)
                            show player clean knife onlayer inyourface at Position(ypos=1125)
                            with Dissolve(0.75)
                            n "Doubt, unfortunately, clouds your thoughts as you attempt to run her through.\n"
                            play audio "audio/one_shot/punch_one.flac"
                            voice "audio/voices/ch1/knife/narrator/knife_n_42.flac"
                            hide bg onlayer farback
                            hide fury onlayer front
                            hide player onlayer inyourface
                            show bg black onlayer back at Position(ypos=1125)
                            with dissolve
                            n "A moment of distraction and hesitation is all she needed to sidestep your thrust and deliver a catastrophic blow to your jaw.\n"
                            play audio "audio/one_shot/ear_ring.flac"
                            voice "audio/voices/ch1/knife/narrator/knife_n_43.flac"
                            hide bg onlayer back
                            show bg fury stub betrayed distant onlayer farback at Position(ypos=1125)
                            show fury clean distant onlayer back at Position(ypos=1125)
                            with dissolve
                            n "It feels like you've been hit with a sledgehammer. You can feel bone grinding on bone where your jaw has been fractured.\n"
                            voice "audio/voices/ch1/knife/hero/k_h_19.flac"
                            hero "Holy {i}shit{/i} that {i}hurt{/i}!\n"
                            voice "audio/voices/ch1/knife/narrator/knife_n_44.flac"
                            n "Though she's unarmed, the shock of that first strike is enough to stagger you, putting you and the Princess on somewhat equal footing.\n"
                            play audio "audio/one_shot/punch_many_knife.flac"
                            voice "audio/voices/ch1/knife/narrator/knife_n_45.flac"
                            $ default_mouse = "blood"
                            hide bg onlayer farback
                            hide fury onlayer back
                            show bg generic dark onlayer back at Position(ypos=1125)
                            show battle fury chain stabbed onlayer front at Position(ypos=1125)
                            #show battle1 fury chain stabbed onlayer front at Position(ypos=1125)
                            #show battle2 fury chain stabbed onlayer front at Position(ypos=1125)
                            #show battle3 fury chain stabbed onlayer front at Position(ypos=1125)
                            with Dissolve(0.75)
                            n "Your blade slashes through the air again and again, and her fists connect with your body as many times or more, each impact as heavy as that first bone-crushing hit.\n"
                            voice "audio/voices/ch1/knife/hero/k_h_20.flac"
                            hero "We can still turn this around.\n"
                            $ config.menu_include_disabled = True
                            menu:
                                extend ""

                                "{i}• [[Give up.]{/i}" if tower_encountered == False:
                                    default tower_pathetic = False
                                    $ tower_pathetic = True
                                    $ config.menu_include_disabled = False
                                    $ current_princess = "tower"
                                    $ blade_held = False
                                    $ default_mouse = "default"
                                    play audio "audio/one_shot/knife_bounce_several.flac"
                                    voice "audio/voices/ch1/knife/narrator/knife_n_46.flac"
                                    hide battle onlayer front
                                    show knife dropped onlayer inyourface at Position(ypos=1125)
                                    with dissolve
                                    n "Are you serious? {i}Sigh{/i}. As internal bleeding sets in, the blade falls from your trembling hands, clattering to the ground uselessly.\n"
                                    play audio "audio/one_shot/collapse.flac"
                                    voice "audio/voices/ch1/knife/narrator/knife_n_47.flac"
                                    hide bg onlayer back
                                    hide knife onlayer inyourface
                                    show bg fury stub betrayed loom onlayer back at Position(ypos=1125)
                                    show fury chain stabbed loom onlayer front at Position(ypos=1125)
                                    with dissolve
                                    n "You lacked the will to finish the job, your bruised and broken body falling to its knees before her.\n"
                                    play audio "audio/one_shot/knife_kicked.flac"
                                    voice "audio/voices/ch1/knife/narrator/knife_n_48.flac"
                                    n "The Princess, exhausted, chest heaving with heavy breaths, tosses the blade away from you.\n"
                                    voice "audio/voices/ch1/knife/hero/k_h_21.flac"
                                    hero "This is the end, isn't it?\n"
                                    voice "audio/voices/ch1/knife/princess/stab_p_28.flac"
                                    show fury chain stabbed loom talk onlayer front with dissolve
                                    # replace with tower disappointed line
                                    #sp "Look at you. Completely broken. This was fun.\n"
                                    sp "Is this really the best you could do? Look at you. Completely broken. I'd be lying if I said I wasn't a little disappointed.\n"
                                    play audio "audio/one_shot/thump.flac"
                                    voice "audio/voices/ch1/knife/narrator/knife_n_49.flac"
                                    show fury chain stabbed foot onlayer front with dissolve
                                    n "She plants her foot on your chest and pushes you onto your back, the air leaving your lungs in a heavy puff.\n"
                                    play audio "audio/one_shot/knee_drop.flac"
                                    voice "audio/voices/ch1/knife/narrator/knife_n_50.flac"
                                    show fury chain stabbed kneel onlayer front with dissolve
                                    n "And then she brings her knee to your throat.\n"
                                    play audio "audio/one_shot/knee_kill.flac"
                                    voice "audio/voices/ch1/knife/narrator/knife_n_51.flac"
                                    n "She leans into it with the kind of weight you didn't think her slight frame could possibly possess, shattering your windpipe and leaving you starved for breath.\n"
                                    voice "audio/voices/ch1/knife/princess/stab_p_30.flac"
                                    show fury chain stabbed kneel talk onlayer front with dissolve
                                    sp "It's too bad. I was looking forward to some company.\n"
                                    $ persistent.death_count += 1
                                    stop music fadeout 1.0
                                    stop sound fadeout 1.0
                                    hide bg onlayer back
                                    hide fury onlayer front
                                    show bg black onlayer back at Position(ypos=1125)
                                    with dissolve
                                    voice "audio/voices/ch1/knife/narrator/knife_n_52.flac"
                                    n "Everything goes dark, and you die.\n"
                                    hide bg black onlayer back with dissolve
                                    jump start_2

                                "{i}• [[Finish the job.]{/i}" if adversary_encountered == False:
                                    $ config.menu_include_disabled = False
                                    $ loop_1_princess_killed = True
                                    $ current_princess = "adversary"
                                    voice "audio/voices/ch1/knife/narrator/knife_n_53.flac"
                                    hide bg onlayer back
                                    hide battle onlayer front
                                    show bg fury stub betrayed distant onlayer farback at Position(ypos=1125)
                                    show fury stabbed distant stare onlayer back at Position(ypos=1125)
                                    show player bloody knife onlayer inyourface at Position(ypos=1125)
                                    with Dissolve(0.75)
                                    n "You and the Princess stare at each other, both gasping for breath, equally exhausted. You probably won't make it out of here alive, but you can at least make sure that she won't make it out of here, either.\n"
                                    voice "audio/voices/ch1/knife/hero/k_h_22.flac"
                                    hero "Excuse me?\n"
                                    voice "audio/voices/ch1/knife/narrator/knife_n_54.flac"
                                    n "Do you think this is what I wanted to happen? I have a duty to state the facts of the situation, and honestly, it's a miracle anyone is still standing right now.\n"
                                    voice "audio/voices/ch1/knife/narrator/knife_n_55.flac"
                                    n "Can you not feel all those ruptured organs bouncing around in there? If the Princess doesn't do our friend in herself, internal bleeding is certain to finish the job.\n"
                                    play audio "audio/one_shot/punch_stab.flac"
                                    voice "audio/voices/ch1/knife/narrator/knife_n_56.flac"
                                    hide bg onlayer farback
                                    hide fury onlayer back
                                    hide player onlayer inyourface
                                    show bg generic dark onlayer back at Position(ypos=1125)
                                    show finale fury chain stabbed onlayer front at Position(ypos=1125)
                                    #show finale1 fury chain stabbed onlayer front at Position(ypos=1125)
                                    #show finale2 fury chain stabbed onlayer front at Position(ypos=1125)
                                    with Dissolve(0.75)
                                    n "The two of you clash for the final time. You feel your ribs break as she delivers a heavy blow, but you push through the pain, falling forward and sinking your blade deep into the Princess' heart.\n"
                                    voice "audio/voices/ch1/knife/princess/stab_p_31.flac"
                                    hide bg onlayer back
                                    hide finale onlayer front
                                    show bg generic onlayer farback at Position(ypos=1125)
                                    show fury chain stabbed dying onlayer front at Position(ypos=1125)
                                    with dissolve
                                    sp "O... oh.\n"
                                    play audio "audio/one_shot/collapse.flac"
                                    play secondary "audio/one_shot/knife_bounce_several.flac"
                                    $ blade_held = False
                                    $ default_mouse = "default"
                                    voice "audio/voices/ch1/knife/narrator/knife_n_57.flac"
                                    show bg fury chained stabbed dying talk onlayer farback at Position(ypos=1125)
                                    show fury chain stabbed dying talk onlayer front at Position(ypos=1125)
                                    with dissolve
                                    n "The two of you fall to the floor.\n"
                                    voice "audio/voices/ch1/knife/princess/stab_p_32.flac"
                                    sp "This was fun.\n"
                                    voice "audio/voices/ch1/knife/narrator/knife_n_58.flac"
                                    n "The Princess gasps, her voice an unhealthy rasp as her lungs start to fill with blood.\n"
                                    voice "audio/voices/ch1/knife/princess/stab_p_33.flac"
                                    sp "You put up more of a fight than I thought you would...\nBut I have to wonder...\n"
                                    voice "audio/voices/ch1/knife/princess/stab_p_34.flac"
                                    sp "Do you {i}really{/i} think this is the end?\n"
                                    #voice "audio/voices/ch1/knife/hero/k_h_16.flac"
                                    #show fury chain stabbed dead onlayer front with dissolve
                                    #hero "There it is again, that razor-sharp look in her eyes and that terrifying conviction in her words."
                                    $ persistent.death_count += 1
                                    stop music fadeout 1.0
                                    stop sound fadeout 1.0
                                    hide bg onlayer farback
                                    hide fury onlayer front
                                    show bg black onlayer back at Position(ypos=1125)
                                    with dissolve
                                    voice "audio/voices/ch1/knife/narrator/knife_n_59.flac"
                                    n "But you don't have time to worry over such things. Everything goes dark, and you die.\n"
                                    hide bg black onlayer back with dissolve
                                    jump start_2

                                "{i}• [[Flee and lock her in the basement.]{/i}" if nightmare_encountered == False:
                                    $ config.menu_include_disabled = False
                                    $ nightmare_join_fled = True
                                    $ current_princess = "nightmare"
                                    voice "audio/voices/ch1/knife/narrator/knife_n_60.flac"
                                    hide farback onlayer back
                                    hide bg onlayer back
                                    hide battle onlayer front
                                    show bg fury stub betrayed distant onlayer farback at Position(ypos=1125)
                                    show fury stabbed distant stare onlayer back at Position(ypos=1125)
                                    show player bloody knife onlayer inyourface at Position(ypos=1125)
                                    with Dissolve(0.75)
                                    n "Are you {i}serious{/i}?\n"
                                    voice "audio/voices/ch1/knife/hero/k_h_23.flac"
                                    hero "It's a good idea. We've taken some bad hits, but we've dealt some, too. She has to be feeling it more than we are. Let's regroup upstairs. If we're lucky, maybe she'll just bleed out.\n"
                                    play audio "audio/one_shot/footstep_run_medium.flac"
                                    play secondary "audio/one_shot/chain_1.flac"
                                    voice "audio/voices/ch1/knife/narrator/knife_n_61.flac"
                                    hide bg onlayer farback
                                    hide fury onlayer back
                                    hide player onlayer inyourface
                                    show farbg flee back onlayer farback at Position(ypos=1125)
                                    show bg flee onlayer back at Position(ypos=1125)
                                    with dissolve
                                    n "Fine. You make a mad dash to the basement stairs, the Princess' chains rattling as she tries to chase you, but pulling taut much too soon for her to catch up.\n"
                                    #re-read
                                    voice "audio/voices/ch1/knife/princess/stab_p_35.flac"
                                    sp "Do you really think you can just {i}walk out of here{/i}?\n"
                                    voice "audio/voices/ch1/knife/narrator/knife_n_62.flac"
                                    hide farbg onlayer farback
                                    hide bg onlayer back
                                    show bg basement distant onlayer farback at Position(ypos=1125)
                                    show bg fury chains onlayer back at Position(ypos=1125)
                                    show fury chains pull onlayer back at Position(ypos=1125)
                                    with dissolve
                                    play audio "audio/one_shot/chain_6.flac"
                                    n "She steps towards you, ignoring her chains.\n"
                                    play audio "audio/one_shot/chain_break.flac"
                                    voice "audio/voices/ch1/knife/narrator/knife_n_62b.flac"
                                    show fury chains break onlayer back with dissolve
                                    $ gallery_zch1.unlock_item(16)
                                    $ renpy.save_persistent()
                                    n "They creak and strain as she pulls against them, until, finally, they break. The links clatter to the floor, useless.\n"
                                    voice "audio/voices/ch1/knife/narrator/knife_n_63.flac"
                                    n "She's free. Hurry.\n"
                                    play audio "audio/one_shot/footstep_run_medium.flac"
                                    voice "audio/voices/ch1/knife/narrator/knife_n_64.flac"
                                    hide bg onlayer farback
                                    hide fury chains onlayer back
                                    hide bg onlayer back
                                    hide distant onlayer farback
                                    show basement stairs open onlayer front at Position(ypos=1125)
                                    with dissolve
                                    n "You push your broken body as she closes in, and just barely manage to pass the threshold of the basement doorway before she catches up to you.\n"
                                    $ quick_menu = False
                                    hide distant onlayer farback
                                    hide basement onlayer front
                                    scene bg black
                                    with fade
                                    jump nightmare_join


                    else:
                        $ loop_1_princess_killed = True
                        $ current_princess = "spectre"
                        play audio "audio/one_shot/footstep_run_medium.flac"
                        voice "audio/voices/ch1/knife/narrator/knife_n_65.flac"
                        hide princess d onlayer back
                        hide bg basement distant onlayer farback
                        hide back basement distant onlayer back
                        show bg generic onlayer back at Position(ypos=1125)
                        show princess murder shock onlayer front at Position(ypos=1125)
                        with dissolve
                        n "You lunge forward without a moment's hesitation.\n"
                        #voice "audio/voices/ch1/knife/narrator/knife_n_66.flac"
                        #n "As the gap between you and the Princess closes, it's as though your body moves entirely of its own accord.\n"
                        #voice "audio/voices/ch1/knife/narrator/knife_n_67.flac"
                        #n "The Princess tries to outmaneuver you, but you're far too quick to be bested here."
                        play audio "audio/one_shot/knife_stab.flac"
                        $ default_mouse = "blood"
                        voice "audio/voices/ch1/knife/narrator/knife_n_68.flac"
                        show bg generic onlayer back at Position(ypos=1125)
                        show princess murder stabbed onlayer front at Position(ypos=1125)
                        with dissolve
                        n "You feel flesh easily give way and look down to see your blade already sinking deep into her heart.\n"
                        voice "audio/voices/ch1/knife/princess/stab_p_36.flac"
                        show princess murder stabbed talk onlayer front with dissolve
                        p "O... oh.\n"
                        voice "audio/voices/ch1/knife/princess/stab_p_37.flac"
                        p "This is it, isn't it?\n"
                        play audio "audio/one_shot/collapse.flac"
                        voice "audio/voices/ch1/knife/princess/stab_p_38.flac"
                        $ blade_held = False
                        $ default_mouse = "default"
                        hide bg generic onlayer back
                        hide princess murder stabbed onlayer front
                        show princess murder dying talk onlayer front at Position(ypos=1125)
                        with dissolve
                        p "I'm almost embarrassed. I should have seen that coming.\nBut... I have to wonder...\n"
                        voice "audio/voices/ch1/knife/princess/stab_p_39.flac"
                        sp "Do you {i}actually{/i} believe this was enough to kill me?\n"
                        voice "audio/voices/ch1/knife/hero/k_h_16.flac"
                        show princess murder dying onlayer front with dissolve
                        hero "It's like she's convinced she can't die.\n"
                        voice "audio/voices/ch1/knife/narrator/knife_n_69.flac"
                        show princess murder dead onlayer front with dissolve
                        n "Yes. Even as she lays there dying, she entirely {i}believes{/i} herself to be alive and well.\n"
                        stop music fadeout 1.0
                        play sound "audio/looping/uncomfortable ambiance heightened.ogg" loop
                        voice "audio/voices/ch1/knife/narrator/knife_n_70.flac"
                        n "But it's over, isn't it? She stopped breathing moments ago, that arrogant look still plastered on her face.\n"
                        voice "audio/voices/ch1/knife/hero/k_h_24.flac"
                        hero "But {i}is{/i} it over? {i}Really{/i} over?\n"
                        $ config.menu_include_disabled = True
                        menu:
                            extend ""

                            "{i}• Of course it is. She's dead.{/i}" if spectre_encountered == False:
                                voice "audio/voices/ch1/knife/narrator/knife_n_71.flac"
                                n "Yes, exactly. It's over.\n"

                            "{i}• I'm not sure. I feel like she has to have some kind of trick up her sleeve.{/i}" if razor_encountered == False:
                                voice "audio/voices/ch1/knife/narrator/knife_n_72.flac"
                                n "It's over. You could check her sleeves if you want, but I can assure you that there's nothing hidden up there.\n"
                                # NEW
                                label ch1_razor_alt_start:
                                    default ch1_razor_pulse = False
                                    voice "audio/voices/ch1/knife/hero/knife_nh_1.flac"
                                    hero "We should make sure. What's the harm in checking for a pulse?\n"
                                    voice "audio/voices/ch1/knife/narrator/knife_nr_9.flac"
                                    n "I really don't think you should do that.\n"
                                    voice "audio/voices/ch1/knife/hero/knife_nh_2.flac"
                                    hero "And why shouldn't we? Is there something you're not telling us?\n"
                                    voice "audio/voices/ch1/knife/narrator/knife_nr_10.flac"
                                    n "I've told you everything that's happened with complete accuracy. The Princess is {i}dead{/i}. Your blade pierced her heart, there's no coming back from that.\n"
                                    menu:
                                        extend ""

                                        "{i}• [[Remove the blade.]{/i}":
                                            $ blade_held = True
                                            $ default_mouse = "blood"
                                            play audio "audio/one_shot/knife_pickup.flac"
                                            show princess murder dead close onlayer front
                                            show player grab knife princess dead onlayer front at Position(ypos=1125)
                                            with dissolve
                                            voice "audio/voices/ch1/knife/narrator/knife_nr_11.flac"
                                            n "You lean down and wrap your hand around the blade's hilt.\n"
                                            play audio "audio/one_shot/knife_stab.flac"
                                            voice "audio/voices/ch1/knife/narrator/knife_nr_12a.flac"
                                            hide player onlayer front
                                            show princess murder dead close noknife onlayer front
                                            show player bloody knife onlayer inyourface at Position(ypos=1125)
                                            with flash
                                            n "But as you begin to slide it out of its resting place, you feel a sharp and sudden jab in your side.\n"
                                            voice "audio/voices/ch1/knife/hero/knife_nh_3.flac"
                                            hero "What was {i}that{/i}?\n"
                                            play music "audio/_music/ch1/The World-Ender.flac"
                                            queue music "audio/_music/ch1/The World-Ender Loop.flac" loop
                                            voice "audio/voices/ch1/knife/princess/r_p_1.flac"
                                            show princess murder dead close noknife open onlayer front
                                            sp "I guess I won't be dying alone after all...\n"
                                            jump alt_razor_final_join

                                        "{i}• [[Check for a pulse.]{/i}":
                                            $ ch1_razor_pulse = True
                                            $ blade_held = False
                                            show princess murder dead close onlayer front
                                            show player pulse check onlayer front at Position(ypos=1125)
                                            with dissolve
                                            voice "audio/voices/ch1/knife/narrator/knife_nr_13.flac"
                                            n "You lean down and place your hand against the her neck, holding your breath as you search for a pulse. Even though you know you're not going to find one.\n"
                                            voice "audio/voices/ch1/knife/hero/knife_nh_4.flac"
                                            hero "We definitely won't if {i}you{/i} keep talking.\n"
                                            voice "audio/voices/ch1/knife/narrator/knife_nr_14a.flac"
                                            n "I'm sorry, do you {i}want{/i} her to be alive? You just saved the entire world from annihilation, why are you suddenly trying to call that into {i}question{/i}—\n"
                                            # a heartbeat
                                            play audio "audio/one_shot/heart_beat.flac"
                                            $ renpy.pause(1.5)
                                            voice "audio/voices/ch1/knife/hero/knife_nh_5.flac"
                                            hero "Wait... what was that?\n"
                                            hide player onlayer front with dissolve
                                            voice "audio/voices/ch1/knife/narrator/knife_nr_15.flac"
                                            n "You know what that was. That was a sound of a heartbeat. Followed by another. And another.\n"
                                            voice "audio/voices/ch1/knife/princess/r_p_1.flac"
                                            show princess murder dead close open onlayer front
                                            sp "I guess I won't be dying alone after all...\n"
                                            play audio "audio/one_shot/knife_stab.flac"
                                            voice "audio/voices/ch1/knife/narrator/knife_nr_16.flac"
                                            play music "audio/_music/ch1/The World-Ender.flac"
                                            queue music "audio/_music/ch1/The World-Ender Loop.flac" loop
                                            show princess murder dead close open onlayer front with flash
                                            n "Something sharp digs into your side, the shock of it sending your nerves into a pained frenzy.\n"
                                            #n "Your nerves cry out in pain as something sharp digs into your side.\n"
                                            label alt_razor_final_join:
                                                $ razor_revival = True
                                                $ current_princess = "razor"
                                                $ current_mutual_death += 1
                                                voice "audio/voices/ch1/knife/hero/knife_nh_6.flac"
                                                hero "Quick, let's get out of here!\n"
                                                play audio "audio/one_shot/knife_stab.flac"
                                                voice "audio/voices/ch1/knife/narrator/knife_nr_17.flac"
                                                if blade_held:
                                                    hide player onlayer inyourface
                                                    hide princess onlayer front
                                                    scene bg ceiling onlayer back at Position(ypos=1125)
                                                    show razor 1 stab onlayer front at Position(ypos=1125)
                                                    show player bloody knife onlayer inyourface at Position(ypos=1125)
                                                    with flash
                                                else:
                                                    hide princess onlayer front
                                                    scene bg ceiling onlayer back at Position(ypos=1125)
                                                    show razor 1 stab knife onlayer front at Position(ypos=1125)
                                                    show player defend razor onlayer inyourface at Position(ypos=1125)
                                                    with flash
                                                n "It's too late for that now. You collapse to the ground as the mortally-wounded Princess twists a blade of her own deeper between your ribs.\n"
                                                if blade_held:
                                                    play secondary "audio/one_shot/knife_bounce_several.flac"
                                                    $ blade_held = False
                                                    $ default_mouse = "default"
                                                play audio "audio/one_shot/collapse.flac"
                                                voice "audio/voices/ch1/knife/narrator/knife_nr_18.flac"
                                                hide razor onlayer front
                                                hide bg onlayer back
                                                hide player onlayer inyourface
                                                scene bg generic dark onlayer back
                                                if ch1_razor_pulse:
                                                    show fury sprayed dying talk onlayer front
                                                else:
                                                    show fury sprayed dying noknife talk onlayer front
                                                with dissolve
                                                n "As you fall, she falls with you, exhausted by the effort, the little life that was left in her eyes fading rapidly.\n"
                                                voice "audio/voices/ch1/knife/princess/r_p_2.flac"
                                                sp "An eye for an eye. A life for a life. I guess we're even now...\n"
                                                #voice "audio/voices/ch1/knife/narrator/knife_nr_20.flac"
                                                #n "She laughs, coughing up a spray of blood.\n"
                                                voice "audio/voices/ch1/knife/princess/r_p_3.flac"
                                                sp "See you around.\n"
                                                if ch1_razor_pulse:
                                                    show fury sprayed dead onlayer front
                                                else:
                                                    show fury sprayed dead noknife onlayer front
                                                with dissolve
                                                voice "audio/voices/ch1/knife/narrator/knife_nr_21.flac"
                                                n "You were {i}so{/i} close! Why did you hesitate? {i}Sigh{/i}. It doesn't matter. At least you managed to take her with you.\n"
                                                voice "audio/voices/ch1/knife/hero/knife_nh_7.flac"
                                                hero "For whatever that's worth.\n"
                                                $ blade_held = False
                                                $ default_mouse = "default"
                                                $ quick_menu = False
                                                stop music fadeout 1.0
                                                stop sound fadeout 1.0
                                                hide bg onlayer back
                                                hide player onlayer front
                                                hide fury onlayer front
                                                show bg black onlayer back at Position(ypos=1125)
                                                with fade
                                                $ persistent.death_count += 1
                                                voice "audio/voices/ch1/knife/narrator/knife_nr_22.flac"
                                                n "Everything goes dark, and you die.\n"
                                                hide bg black onlayer back with dissolve
                                                jump start_2


                                        "{i}• You're right. She's dead. Let's just get out of here.{/i}" if spectre_encountered == False:
                                            voice "audio/voices/ch1/knife/narrator/knife_n_71.flac"
                                            n "Yes, exactly. It's over.\n"
                                            $ config.menu_include_disabled = False
                                            #hero "Fair enough. She {i}does{/i} have a knife sticking out of her heart. Forget I said anything.\n"
                                            # rejoins upstairs

                            "{i}• Of course not. That was too easy.{/i}" if razor_encountered == False:
                                voice "audio/voices/ch1/knife/narrator/knife_n_73.flac"
                                n "It's. Over. Don't get all worked up.\n"
                                jump ch1_razor_alt_start

                        $ config.menu_include_disabled = False
                        play sound "audio/looping/ambient_cabin.ogg" loop
                        play secondary "audio/one_shot/footsteps_creaky.flac"
                        queue secondary "audio/one_shot/door_close.flac"
                        voice "audio/voices/ch1/knife/narrator/knife_n_74.flac"
                        $ quick_menu = False
                        hide princess onlayer front
                        show bg black onlayer back
                        with fade
                        hide bg onlayer back
                        scene farback cabin quiet onlayer farback at Position(ypos=1125)
                        show bg interior cabin onlayer back at Position(ypos=1125)
                        #show door interior cabin onlayer back at Position(ypos=1125)
                        with fade
                        if persistent.quick_menu:
                            $ quick_menu = True
                        n "With your work done, you make your way back up the stairs, closing the door to the basement behind you.\n"
                        voice "audio/voices/ch1/knife/hero/k_h_25.flac"
                        hero "Why do I feel like we've done something terrible?\n"
                        voice "audio/voices/ch1/knife/narrator/knife_n_75.flac"
                        n "You did kill someone. Greater good or not, something would be very wrong with you if you didn't feel at least a little bad. But it {i}was{/i} for the greater good. One of these days, that will sink in and help ease your guilty conscience.\n"
                        voice "audio/voices/ch1/knife/hero/k_h_26.flac"
                        hero "But that day isn't today. Let's just get out of here.\n"
                        menu:
                            extend ""

                            "{i}• [[Leave.]{/i}":
                                stop sound fadeout 1.0
                                play audio "audio/one_shot/door_bedroom.flac"
                                voice "audio/voices/ch1/knife/narrator/knife_n_76.flac"
                                $ quick_menu = False
                                hide bg onlayer back
                                hide door onlayer back
                                show bg black big onlayer back at Position(ypos=1125)
                                with fade
                                n "You open the cabin door, ready to return to a world saved from certain doom.\n"

                        voice "audio/voices/ch1/knife/narrator/knife_n_77.flac"
                        play sound "audio/looping/STP_opressive_loop.ogg" loop
                        hide bg black onlayer back
                        show bg void onlayer farback at Position(ypos=1125)
                        show door void onlayer front at Position(ypos=1125)
                        with dissolve
                        if persistent.quick_menu:
                            $ quick_menu = True
                        n "Only, a world saved from certain doom isn't what you find. Instead, what you find is nothing at all. Where a lush forest stood mere minutes ago, the only thing in front of you now is the vast emptiness of some place far away.\n"
                        voice "audio/voices/ch1/knife/hero/k_h_27.flac"
                        hero "What... happened?\n"
                        voice "audio/voices/ch1/knife/narrator/knife_n_78.flac"
                        n "Everyone is fine, it's just that you and the cabin are now far away from them. Don't worry. You'll be safe here. This is good. Everyone is happy. {i}You'll{/i} be happy.\n"
                        menu:
                            extend ""

                            "{i}• Wait, is this my prize? This is great! Thank you so much.{/i}" if forest_1_prize:
                                voice "audio/voices/ch1/knife/narrator/s2.flac"
                                n "I'm just happy that you're happy. I knew you'd like it.\n"

                            "{i}• Wait, is this my prize? This sucks!{/i}" if forest_1_prize:
                                voice "audio/voices/ch1/knife/narrator/s1.flac"
                                n "What's done is done, and there's no going back now. I'm sorry you don't like your reward, but maybe you'll learn to appreciate it in time.\n"

                            "{i}• That's bullshit! Let me out of here!{/i}":
                                #voice "audio/voices/ch1/knife/narrator/knife_n_79.flac"
                                #n "What's done is done, and there's no going back now.\n"
                                if forest_1_prize:
                                    voice "audio/voices/ch1/knife/narrator/s1.flac"
                                    n "What's done is done, and there's no going back now. I'm sorry you don't like your reward, but maybe you'll learn to appreciate it in time.\n"
                                else:
                                    voice "audio/voices/ch1/knife/narrator/knife_n_79.flac"
                                    n "What's done is done, and there's no going back now.\n"

                            "{i}• Oh. Okay.{/i}":
                                voice "audio/voices/ch1/knife/narrator/knife_n_80.flac"
                                n "I'm so glad you're keeping an open mind.\n"

                            "{i}• I was kind of hoping I'd get a better ending for saving the world.{/i}":
                                voice "audio/voices/ch1/knife/narrator/knife_n_81.flac"
                                n "This isn't an ending. In fact, now that the Princess has been slain, endings are a thing of the past.\nNo... this is the beginning of {i}eternity{/i}. Your reward.\n"

                        voice "audio/voices/ch1/knife/narrator/knife_n_82.flac"
                        n "This is what's best for everyone. Trust me.\n"
                        play audio "audio/one_shot/door_close.flac"
                        play sound "audio/looping/ambient_cabin.ogg" loop
                        voice "audio/voices/ch1/knife/narrator/knife_n_83.flac"
                        $ quick_menu = False
                        hide door onlayer front
                        hide bg onlayer farback
                        show farback cabin quiet onlayer farback at Position(ypos=1125)
                        show bg interior cabin onlayer back at Position(ypos=1125)
                        #show door interior cabin onlayer back at Position(ypos=1125)
                        with fade
                        if persistent.quick_menu:
                            $ quick_menu = True
                        n "Time passes. You can't be sure if it's days, or months, or years or even decades. It's all a wonderful, boring blur. You've never been happier.\n"
                        voice "audio/voices/ch1/knife/hero/k_h_28.flac"
                        hero "Pst! Hey! We're not just going to stay here {i}forever{/i} right?\n"
                        label cycle_1_princess_slain_offer:
                            default cycle_1_princess_slain_offer_explore = False
                            default cycle_1_princess_slain_offer_rejected = False
                            menu:

                                extend ""

                                "{i}• (Explore) Didn't you hear The Narrator? I'm happy. We're happy.{/i}" if cycle_1_princess_slain_offer_explore == False:
                                    $ cycle_1_princess_slain_offer_explore = True
                                    voice "audio/voices/ch1/knife/hero/k_h_29.flac"
                                    hero "Are we really happy, or is He just telling us that we are?\n"
                                    jump cycle_1_princess_slain_offer

                                "{i}• Hmm, okay maybe I'm not happy. And I'm not just saying that because you're the last person I talked to.{/i}" if cycle_1_princess_slain_offer_explore or ch1_mound:
                                    voice "audio/voices/ch1/knife/hero/k_h_30.flac"
                                    hero "Good, because I have an idea to get us out of here. Though you're probably not going to like it.\n"

                                "{i}• No, we're happy. I'm sure of it.{/i}" if cycle_1_princess_slain_offer_explore and ch1_mound == False:
                                    $ cycle_1_princess_slain_offer_rejected = True
                                    voice "audio/voices/ch1/knife/hero/k_h_31.flac"
                                    hero "Really? Well, if you ever change your mind, just let me know I guess.\n"

                                "{i}• Hell no, do you have any idea how to get us the heck out of here?{/i}" if cycle_1_princess_slain_offer_explore == False and (ch1_mound == False or ch1_mound_fresh == False):
                                    voice "audio/voices/ch1/knife/hero/k_h_32.flac"
                                    hero "I do, but you're probably not going to like it.\n"

                                "{i}• Of course we are. I like it here.{/i}" if cycle_1_princess_slain_offer_explore == False and ch1_mound == False:
                                    $ cycle_1_princess_slain_offer_rejected = True
                                    voice "audio/voices/ch1/knife/hero/k_h_31.flac"
                                    hero "Really? Well, if you ever change your mind, just let me know I guess.\n"


                        if cycle_1_princess_slain_offer_rejected:
                            label cycle_1_princess_slain_eternity:

                                voice "audio/voices/ch1/knife/narrator/knife_n_84.flac"
                                n "More happy time passes, though the word begins to lose its meaning. 'Time,' that is, not 'happy.' 'Happy' still has plenty of meaning.\n"
                                voice "audio/voices/ch1/knife/hero/k_h_33.flac"
                                hero "Please, shake yourself out of it. We have to get out of here.\n"
                                voice "audio/voices/ch1/knife/narrator/knife_n_85.flac"
                                n "The little voice's pleas fall on deaf ears.\n"
                                voice "audio/voices/ch1/knife/narrator/knife_n_86.flac"
                                n "Eventually, you pass into a blissful state of pure existence. Though words like 'eventually' and 'pass' ceased to have any meaning to you long before that shift. You simply exist. Happy. Forever.\n"
                                $ gallery_zch1.unlock_item(18)
                                $ renpy.save_persistent()
                                play music "audio/looping/party.ogg" loop
                                $ quick_menu = False
                                hide farback interior cabin onlayer farback
                                hide bg interior cabin onlayer back
                                hide door interior cabin onlayer back
                                show end good onlayer back at Position(ypos=1125)
                                if _preferences.language is not None:
                                    show text _("{color=000000}Good Ending! =:) YOU DID IT!!! you saved EVERYONE!{/color}") onlayer front at Position(ypos=950)
                                with fade
                                if loops_finished > 0:
                                    $ renpy.pause(2.0)
                                    default ch1_mound = False
                                    default ch1_mound_fresh = False
                                    $ ch1_mound = True
                                    $ ch1_mound_fresh = True
                                    $ cycle_1_princess_slain_offer_rejected = False
                                    stop music
                                    play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                                    $ renpy.pause(1.0)
                                    voice "audio/voices/mound/bonus/flee.flac"
                                    pmid "You have already committed to my completion. You cannot go further astray.\n{w=5.2}{nw}"
                                    show screen disableclick(0.5)
                                    stop music
                                    if persistent.quick_menu:
                                        $ quick_menu = True
                                    hide text onlayer front
                                    hide end onlayer back
                                    show farback cabin quiet onlayer farback at Position(ypos=1125)
                                    show bg interior cabin onlayer back at Position(ypos=1125)
                                    $ achievement.grant("ACH_GOOD2")
                                    "{nw}"
                                    jump cycle_1_princess_slain_offer
                                $ gallery_zch1.unlock_item(18)
                                $ renpy.save_persistent()
                                $ achievement.grant("ACH_GOOD")
                                $ renpy.pause()
                                stop sound fadeout 1.0
                                hide text onlayer front
                                hide end good onlayer back
                                with fade
                                $ final_ending = "good"
                                jump credits
                                return

                        else:
                            voice "audio/voices/ch1/knife/hero/k_h_34.flac"
                            hero "The blade. We can use the blade to get out of this.\n"
                            voice "audio/voices/ch1/knife/narrator/knife_n_87.flac"
                            n "I can hear everything you say, little voice. There's only one thing it would want you to use that blade on, and I'm afraid that thing is {i}you{/i}, dear hero.\n"
                            voice "audio/voices/ch1/knife/hero/k_h_35.flac"
                            hero "He's right. It's the only way out.\n"
                            voice "audio/voices/ch1/knife/narrator/knife_n_88.flac"
                            n "Do you hear that? It wants to take this happiness away from you. It wants this wonderful place to {i}end{/i}.\n"
                            voice "audio/voices/ch1/knife/hero/k_h_36.flac"
                            hero "Do you not? There's more for us to do, and the only way for us to do it is to take that blade and use it.\n"
                            voice "audio/voices/ch1/knife/narrator/knife_n_89.flac"
                            n "Don't you {i}dare{/i}.\n"
                            label cycle_1_princess_slain_offer_heard_menu:
                                default cycle_1_princess_slain_offer_heard_menu_explore = False
                                menu:
                                    extend ""

                                    "{i}• (Explore) Wouldn't 'using' the blade... you know, kill us? Wouldn't we be dead?{/i}" if cycle_1_princess_slain_offer_heard_menu_explore == False:
                                        $ cycle_1_princess_slain_offer_heard_menu_explore = True
                                        voice "audio/voices/ch1/knife/narrator/knife_n_90.flac"
                                        n "How astute. You're absolutely correct. Using the blade to kill yourself would kill you and you shouldn't do it.\n"
                                        voice "audio/voices/ch1/knife/hero/k_h_37.flac"
                                        hero "In a sense, we'd die, but looking at things from another angle, are we even really alive anymore? This place... it's nothing! It's absolutely nothing. It's just the same thing, constantly, forever.\n"
                                        voice "audio/voices/ch1/knife/hero/k_h_38.flac"
                                        hero "I know this is out there, but trust me, I {i}know{/i} using the blade will work.\n"
                                        voice "audio/voices/ch1/knife/narrator/knife_n_91.flac"
                                        n "That little voice didn't want you to slay the Princess. It didn't want you to be {i}happy{/i}.\n"
                                        jump cycle_1_princess_slain_offer_heard_menu

                                    "{i}• You'd better be right about this. I'll be pretty upset if we {b}die{/b} die.{/i}" if cycle_1_princess_slain_offer_heard_menu_explore:
                                        voice "audio/voices/ch1/knife/hero/k_h_39.flac"
                                        hero "If we 'die' die, you can yell at me all you want.\n"
                                        label cycle_1_princess_slain_die:
                                            voice "audio/voices/ch1/knife/narrator/knife_n_92.flac"
                                            n "I {i}made{/i} this happy little place for you! Is this not a good enough reward for saving the world? An eternity of bliss? You... you ingrate!\n"
                                            voice "audio/voices/ch1/knife/narrator/knife_n_93.flac"
                                            play sound "audio/looping/ambient_basement_interior.ogg" loop
                                            play audio "audio/one_shot/enter_basement.flac"
                                            $ quick_menu = False
                                            hide farback interior cabin onlayer farback
                                            hide bg interior cabin onlayer back
                                            hide door interior cabin onlayer back
                                            scene bg basement stairs onlayer farback at Position(ypos=1125)
                                            show front basement stairs onlayer farback at Position(ypos=1125)
                                            with fade
                                            if persistent.quick_menu:
                                                $ quick_menu = True
                                            n "Fine. Whatever. For the first time since time stopped meaning anything, you throw open the door to the basement and walk down the stairs.\n"
                                            voice "audio/voices/ch1/knife/narrator/knife_n_94.flac"
                                            $ quick_menu = False
                                            hide bg onlayer farback
                                            hide front onlayer farback
                                            scene farback quiet onlayer farback at Position(ypos=1125)
                                            show back basement distant onlayer back at Position(ypos=1125)
                                            show princess bones knife onlayer back at Position(ypos=1125)
                                            with fade
                                            if persistent.quick_menu:
                                                $ quick_menu = True
                                            n "The Princess' body is dust and bones, though the blade you used to slay her is still as pristine as the day you first held it.\n"
                                            play secondary "audio/one_shot/knife_pickup.flac"
                                            $ default_mouse = "blood"
                                            $ blade_held = True
                                            $ default_mouse = "blade"
                                            voice "audio/voices/ch1/knife/narrator/knife_n_95.flac"
                                            hide bg onlayer farback
                                            hide back onlayer back
                                            hide princess onlayer back
                                            scene bg generic dark onlayer back at Position(ypos=1125)
                                            show player self end onlayer front at Position(ypos=1125)
                                            with fade
                                            n "You pick up the blade, you stab yourself, and you {i}die{/i}.\n"
                                            $ persistent.death_count += 1
                                            play secondary "audio/one_shot/knife_stab.flac"
                                            queue secondary "audio/one_shot/collapse.flac"
                                            voice "audio/voices/ch1/knife/narrator/knife_n_95b.flac"
                                            $ quick_menu = False
                                            $ blade_held = False
                                            $ default_mouse = "default"
                                            stop music fadeout 1.0
                                            stop sound fadeout 1.0
                                            hide farback onlayer farback
                                            hide bg onlayer back
                                            hide player onlayer front
                                            show bg black onlayer back at Position(ypos=1125)
                                            with fade
                                            n "The end. Nice knowing you.\n"
                                            hide bg black onlayer back with dissolve
                                            jump start_2

                                    "{i}• I'm not risking {b}death{/b} over your weird hunch.{/i}" if cycle_1_princess_slain_offer_heard_menu_explore and ch1_mound == False:
                                        voice "audio/voices/ch1/knife/hero/k_h_40.flac"
                                        hero "I suppose we've got all the time in the world for you to change your mind.\n"
                                        jump cycle_1_princess_slain_eternity

                                    "{i}• Anything to get out of this hell.{/i}":
                                        voice "audio/voices/ch1/knife/hero/k_h_41.flac"
                                        hero "Thank you.\n"
                                        jump cycle_1_princess_slain_die

                                    "{i}• You're right. I didn't like that idea. I'm just going to stick around and do nothing, at least for a little while longer.{/i}" if ch1_mound == False:
                                        voice "audio/voices/ch1/knife/narrator/knife_n_96.flac"
                                        n "What a relief.\n"
                                        voice "audio/voices/ch1/knife/hero/k_h_40.flac"
                                        hero "I suppose we've got all the time in the world for you to change your mind.\n"
                                        jump cycle_1_princess_slain_eternity


label basement_1_knife_dropped:
    $ basement_1_talked = True
    $ can_spectre = False
    play audio "audio/one_shot/footsteps_hike_short.flac"
    $ basement_1_nerves_steeled_hesitated = True
    if basement_1_nerves_steeled:
        $ basement_1_threatening_tension = True
    $ renpy.free_memory()
    $ quick_menu = False
    hide princess d haughty talk onlayer back
    hide bg basement distant onlayer farback
    hide back basement distant onlayer back
    show bg basement close onlayer farback at Position(ypos=1125)
    show princess c cold onlayer back at Position(ypos=1125)
    with fade
    $ blade_held = False
    $ default_mouse = "default"
    if persistent.quick_menu:
        $ quick_menu = True
    voice "audio/voices/ch1/knife/narrator/knife_n_97.flac"
    n "Against your better judgment, you step forward to speak with the Princess face-to-face. Unarmed.\n"
    voice "audio/voices/ch1/knife/hero/k_h_42.flac"
    hero "We'll be fine.\n"
    voice "audio/voices/ch1/knife/narrator/knife_n_98.flac"
    n "I don't know what you're hoping to accomplish here, but I can assure you there's no reasoning with her.\n{i}Sigh{/i}. Just make sure you don't forget about the blade on the floor. You're going to need it.\n"
    show princess c bored talk onlayer back with dissolve
    voice "audio/voices/ch1/knife/princess/stab_p_40.flac"
    p "So here we are. What an awkward start to a relationship.\n"
    show princess c sad glance onlayer back with dissolve
    label basement_1_knife_dropped_menu:
        default basement_1_knife_dropped_relationship_explore = False
        default basement_1_knife_dropped_awkward = False
        menu:
            extend ""

            "{i}• (Explore) ''Yeah, it's uh... pretty awkward.''{/i}" if basement_1_knife_dropped_awkward == False and basement_1_knife_dropped_relationship_explore == False and basement_1_shared_task == False:
                $ basement_1_knife_dropped_relationship_explore = True
                $ basement_1_knife_dropped_awkward = True
                show princess c serious talk onlayer back with dissolve
                voice "audio/voices/ch1/knife/princess/stab_p_41.flac"
                #p "Not to make things even more awkward, but do you know why you're here to kill me?\n"
                p "I know. I just said that. Now why are you here to kill me?\n"
                show princess c serious onlayer back
                menu:
                    extend ""

                    "{i}• ''I have my reasons. Do you think I'd just come here to kill someone without even knowing why? That'd be ridiculous!''{/i}":
                        show princess c bored talk onlayer back with dissolve
                        if basement_1_nerves_steeled_hesitated:
                            voice "audio/voices/ch1/knife/princess/stab_p_42.flac"
                            p "And yet you hesitated the moment you saw me. And you dropped your knife. If killing me was really that important, you would have had a little more gumption, don't you think?\n"
                        elif basement_1_nerves_steeled:
                            voice "audio/voices/ch1/knife/princess/stab_p_43.flac"
                            p "And yet you dropped your knife.\n"
                        else:
                            voice "audio/voices/ch1/knife/princess/stab_p_44.flac"
                            p "And yet you dropped your knife the second you saw me.\n"
                        show princess c serious talk onlayer back with dissolve
                        voice "audio/voices/ch1/knife/princess/stab_p_45.flac"
                        p "So... someone put you up to this, right? And whoever it is, it's probably the same someone who shoved me into this dark pit and chained me to a wall.\n"
                        show princess c serious onlayer back with dissolve
                        voice "audio/voices/ch1/knife/hero/k_h_43.flac"
                        hero "That's a fair question. Who chained her in this basement, and if she's so dangerous, {i}how{/i} did they manage to trap her? And why have we been left to do their dirty work?\n"
                        voice "audio/voices/ch1/knife/narrator/knife_n_99.flac"
                        n "Don't give away the game, and don't let her distract you. That's exactly what she wants.\n"
                        show princess c bored talk onlayer back with dissolve
                        voice "audio/voices/ch1/knife/princess/stab_p_46.flac"
                        p "I'm right, aren't I? So who put you up to this?\n"
                        show princess c bored onlayer back with dissolve
                        jump basement_1_knife_dropped_menu

                    "{i}• ''Do you know why I'm here to kill you?''{/i}":
                        show princess c nervous smile talk onlayer back with dissolve
                        voice "audio/voices/ch1/knife/princess/stab_p_laugh.flac"
                        $ renpy.pause(2.5)
                        show princess c sinister onlayer back with dissolve
                        if basement_1_threatening_tension == False:
                            voice "audio/voices/ch1/knife/hero/k_h_44.flac"
                            hero "That laugh! I think I'm in love.\n"
                            voice "audio/voices/ch1/knife/narrator/knife_n_100.flac"
                            n "Stop it.\n"
                        else:
                            voice "audio/voices/ch1/knife/hero/k_h_45.flac"
                            hero "She was just threatening us a second ago. Am I the only one here unnerved by that perfect little laugh?\n"
                            voice "audio/voices/ch1/knife/narrator/knife_n_101.flac"
                            n "I'll take that as a sign that you're finally coming around to reason.\n"
                        show princess c glance sad talk onlayer back with dissolve
                        voice "audio/voices/ch1/knife/princess/stab_p_47.flac"
                        p "I have no idea. To be honest, I don't even know why I'm down here... or how I got here.\n"
                        show princess c serious talk onlayer back with dissolve
                        voice "audio/voices/ch1/knife/princess/stab_p_48.flac"
                        p "I was kind of hoping {i}you{/i} might be able to shed some light on the whole situation.\n"
                        show princess c serious onlayer back with dissolve
                        jump basement_1_knife_dropped_menu

                    "{i}• ''You're supposed to end the world.''{/i}" if basement_1_shared_task == False and tower_encountered == False:
                        label basement_1_shared_task_join:
                            $ basement_1_nerves_fear = True
                            $ basement_1_shared_task = True
                            show princess c cold onlayer back with dissolve
                            voice "audio/voices/ch1/knife/narrator/knife_n_102.flac"
                            n "Don't just {i}tell{/i} her that!\n"
                            if basement_1_threatening_tension == False:
                                show princess c sinister talk onlayer back with dissolve
                                voice "audio/voices/ch1/knife/princess/stab_p_49.flac"
                                p "Is that why they threw me down here? But I don't want to hurt anyone. I like the world!\nI think.\n"
                                show princess c bored talk onlayer back with dissolve
                                voice "audio/voices/ch1/knife/princess/stab_p_50.flac"
                                p "I don't remember much about it, to be honest. I've been down here a long time.\n"
                                voice "audio/voices/ch1/knife/hero/k_h_46.flac"
                                show princess c bored onlayer back with dissolve
                                hero "Just how long has she been down here?\n"
                                #nvoice "audio/voices/ch1/knife/narrator/knife_n_103.flac"
                                #n "How long does she want you to {i}think{/i} she's been down here?"
                            else:
                                show princess c sinister talk onlayer back with dissolve
                                voice "audio/voices/ch1/knife/princess/stab_p_51.flac"
                                p "That's cute. Do you believe that? Do you think I'm some sort of... monster?\n"

                            show princess c bored talk onlayer back with dissolve
                            voice "audio/voices/ch1/knife/princess/stab_p_52.flac"
                            p "If I'm supposed to be capable of ending the world, then how did I wind up here, chained to a wall? Have they told you why I'm allegedly so... dangerous?\n"
                            show princess c sinister onlayer back with dissolve
                            menu:
                                extend ""

                                "{i}• (Deflect) ''What are you going to do if I let you out of here?''{/i}" if what_would_you_do_1 == False:
                                    $ what_would_you_do_1 = True
                                    voice "audio/voices/ch1/knife/narrator/knife_n_104.flac"
                                    show princess c cold onlayer back with dissolve
                                    n "The Princess hesitates before responding.\n"
                                    voice "audio/voices/ch1/empty/hero/empty_h_11.flac"
                                    hero "She doesn't know. She's been down here too long to have any idea of what she'd do in another life.\n"
                                    voice "audio/voices/ch1/knife/narrator/knife_n_105.flac"
                                    n "She knows what she'd do. She's just searching for whatever answer she thinks you want to hear.\n"
                                    show princess c cold talk onlayer back with dissolve
                                    voice "audio/voices/ch1/knife/princess/stab_p_53.flac"
                                    p "I don't think I can answer that question in a way you'd find meaningful.\n"
                                    jump basement_1_philosophy_knife

                                "{i}• ''I've been told enough.''{/i}":
                                    show princess c bored onlayer back with dissolve
                                    voice "audio/voices/ch1/knife/narrator/knife_n_106.flac"
                                    n "Thanks for the vote of confidence.\n"
                                    show princess c sad glance talk onlayer back with dissolve
                                    voice "audio/voices/ch1/knife/princess/stab_p_54.flac"
                                    p "They haven't shared a thing, have they? All they've done is point a finger.\n"
                                    jump basement_1_philosophy_knife

                                "{i}• ''I was hoping you'd tell me.''{/i}":
                                    $ basement_1_nerves_fear = False
                                    show princess c sad glance talk onlayer back with dissolve
                                    voice "audio/voices/ch1/knife/princess/stab_p_55.flac"
                                    p "Ending the world seems like an awful lot for just one person to do. I wouldn't even know where to start.\n"
                                    #p "I don't know how to destroy the world, if that's what you're asking.\n"
                                    show princess c sad glance onlayer back with dissolve
                                    voice "audio/voices/ch1/knife/hero/k_h_47.flac"
                                    hero "I believe her.\n"
                                    voice "audio/voices/ch1/knife/narrator/knife_n_107.flac"
                                    n "She doesn't have to know how to destroy the world to be capable of doing it.\n"
                                    jump basement_1_philosophy_knife

                                "{i}• ''No. But I'm sure they have their reasons for keeping that information secret from me.''{/i}":
                                    show princess c sad glance onlayer back with dissolve
                                    voice "audio/voices/ch1/knife/narrator/knife_n_108.flac"
                                    n "Thanks for the vote of confidence.\n"
                                    show princess c cold talk onlayer back with dissolve
                                    voice "audio/voices/ch1/knife/princess/stab_p_56.flac"
                                    p "What if they're bad reasons, though? If they had {i}good{/i} reasons for thinking I was dangerous, wouldn't they have shared them with you? I don't want to hurt anyone. I just want to leave.\n"
                                    jump basement_1_philosophy_knife

                                "{i}• ''No. And if I'm being honest, I'm more inclined to trust you than I'm inclined to trust Them.''{/i}":
                                    $ basement_1_nerves_fear = False
                                    $ basement_1_nerves_doubt = True
                                    show princess c nervous smile onlayer back with dissolve
                                    voice "audio/voices/ch1/knife/narrator/knife_n_109.flac"
                                    n "Sooner or later you'll understand that I have your best interests at heart. Hopefully sooner.\n"
                                    show princess c sad talk onlayer back with dissolve
                                    voice "audio/voices/ch1/knife/princess/stab_p_57.flac"
                                    p "How sweet. Now be a pal and help me get out of here, would you? We can figure out how to deal with Them after I'm free.\n"
                                    show princess c sad onlayer back with dissolve
                                    menu:
                                        extend ""

                                        "{i}• ''I still have a few more questions before I decide what to do.''{/i}":
                                            show princess c sad glance talk onlayer back with dissolve
                                            voice "audio/voices/ch1/knife/princess/stab_p_58.flac"
                                            p "Fine. What do you want to know?\n"
                                            show princess c bored onlayer back with dissolve
                                            $ previous_dialogue = "Fine. What do you want to know?\n"
                                            $ speaker = p
                                            jump basement_1_knife_dropped_menu

                                        "{i}• [[Slay the Princess] ''Actually, I've changed my mind. I don't trust you.''{/i}" if (can_spectre and (spectre_encountered == False or razor_encountered == False)) or (basement_1_nerves_armed and razor_encountered == False) or (basement_1_nerves_steeled_hesitated and (adversary_encountered == False or tower_encountered == False or nightmare_encountered == False)) or (basement_1_nerves_fear and tower_encountered == False) and can_slay:
                                            show princess c haughty onlayer back with dissolve
                                            play audio "audio/one_shot/knife_pickup.flac"
                                            jump basement_1_knife_slay_join

                                        "{i}• [[Examine the chains] ''I'll see what I can do.''{/i}" if prisoner_encountered == False or tower_encountered == False or adversary_encountered == False:
                                            show princess c thinking onlayer back with dissolve
                                            jump basement_1_knife_rescue

                                "{i}• [[Remain silent.]{/i}":
                                    voice "audio/voices/ch1/knife/princess/stab_p_59.flac"
                                    p "They haven't told you anything, have they?\n"
                                    jump basement_1_philosophy_knife

                                    label basement_1_philosophy_knife:
                                        default basement_1_knife_vague_count = 0
                                        default basement_1_philosophy_knife_flag = False
                                        $ basement_1_philosophy_knife_flag
                                        $ basement_1_knife_vague_count += 1
                                        show princess c serious talk onlayer back with dissolve
                                        voice "audio/voices/ch1/knife/princess/stab_p_60.flac"
                                        p "At the end of the day, whatever the two of us have going on down here is about trust.\n"
                                        show princess c bored talk onlayer back with dissolve
                                        voice "audio/voices/ch1/knife/princess/stab_p_61.flac"
                                        p "Whoever sent you to 'slay' me claimed I was a threat to the world, but they didn't tell you why.\n"
                                        show princess c sad glance talk onlayer back with dissolve
                                        voice "audio/voices/ch1/knife/princess/stab_p_62.flac"
                                        p "That doesn't sound right to me, and I don't think it sounds right to you, either. Otherwise we'd be killing each other instead of talking.\n"
                                        show princess c sad glance onlayer back with dissolve
                                        voice "audio/voices/ch1/knife/hero/k_h_48.flac"
                                        hero "She has a point. There's a reason I've been telling you to question this situation. And there's a reason you've listened.\n"
                                        show princess c sad talk onlayer back with dissolve
                                        voice "audio/voices/ch1/knife/princess/stab_p_63.flac"
                                        p "So I could tell you that I'd lead a quiet life in the woods or that I'd open an orphanage or that I'd do any other number of 'good' things that I'm sure you think you want to hear...\n"
                                        #p "So I could tell you that I'd lead a quiet life in the woods or that I'd open an orphanage or any other number of 'good' things that I'm sure you want to hear...\n"
                                        show princess c cold talk onlayer back with dissolve
                                        voice "audio/voices/ch1/knife/princess/stab_p_64.flac"
                                        p "But you don't really know me, do you? What can my word possibly be worth in a situation like this?\n"
                                        show princess c cold onlayer back with dissolve
                                        voice "audio/voices/ch1/knife/narrator/knife_n_110.flac"
                                        n "She's right about one thing. Her word isn't worth anything.\n"
                                        show princess c bored talk onlayer back with dissolve
                                        voice "audio/voices/ch1/knife/princess/stab_p_65.flac"
                                        p "Like I said, it's all about trust. Blind trust.\n"
                                        show princess c serious talk onlayer back with dissolve
                                        voice "audio/voices/ch1/knife/princess/stab_p_66.flac"
                                        p "So do you trust me—the prisoner, the victim, the Princess {i}clearly{/i} incapable of ending the world—or do you trust whoever put me here?\n"
                                        show princess c serious onlayer back with dissolve
                                        voice "audio/voices/ch1/knife/narrator/knife_n_111.flac"
                                        n "She's wrong. This isn't about trust. This is about {b}risk{/b}. We stand to lose everything, all for the sake of one person. And a subjugating {i}monarch{/i}, no less.\n"
                                        jump basement_1_knife_dropped_menu

                    "{i}• ''I've been told things, but I'm not sure what to believe.''{/i}":
                        voice "audio/voices/ch1/knife/narrator/knife_n_112.flac"
                        show princess c bored onlayer back with dissolve
                        n "Believe {i}me{/i}.\n"
                        show princess c serious talk onlayer back with dissolve
                        voice "audio/voices/ch1/knife/princess/stab_p_67.flac"
                        p "And do you think asking {i}me{/i} what to believe is going to suddenly make everything crystal clear? Let's not pretend that's going to happen. As far as you're concerned, and as far as They're concerned, I'm going to say whatever I have to to get out of here. That's just the dynamic of our situation.\n"
                        show princess c sad glance onlayer back with dissolve
                        jump basement_1_knife_dropped_menu

            "{i}• (Explore) ''A 'relationship?' Are you coming on to me?''{/i}" if basement_1_knife_dropped_relationship_explore == False and basement_1_knife_dropped_awkward == False:
                $ basement_1_knife_dropped_awkward = True
                $ basement_1_knife_dropped_relationship_explore = True
                show princess c bored talk onlayer back with dissolve
                voice "audio/voices/ch1/knife/princess/stab_p_68.flac"
                p "Don't jump to any weird conclusions. We're two people who have met each other. By definition, we have a relationship.\n"
                show princess c bored onlayer back
                jump basement_1_knife_dropped_menu

            "{i}• (Explore) ''How would I get you out of here?''{/i}" if basement_1_knife_how_escape == False:
                default basement_1_knife_how_escape = False
                $ basement_1_knife_how_escape = True
                show princess c sad glance onlayer back with dissolve
                voice "audio/voices/ch1/knife/narrator/knife_n_113.flac"
                n "You can't. Don't bother.\n"
                show princess c serious talk onlayer back with dissolve
                voice "audio/voices/ch1/knife/princess/stab_p_69.flac"
                p "I'm guessing you don't have the key, then? I'm sure there's a key somewhere around here. And if there isn't...\n"
                show princess c sinister talk onlayer back with dissolve
                voice "audio/voices/ch1/knife/princess/stab_p_70.flac"
                p "Well, we can always put that knife to good use.\n"
                voice "audio/voices/ch1/knife/narrator/knife_n_114.flac"
                show princess c serious onlayer back with dissolve
                n "Her sharp eyes settle on the edge of the blade.\n"
                voice "audio/voices/ch1/knife/hero/k_h_49.flac"
                hero "She isn't suggesting what I think she's suggesting... right?\n"
                voice "audio/voices/ch1/knife/narrator/knife_n_115.flac"
                n "She is. I'm sure of it.\n"
                jump basement_1_knife_dropped_menu

            "{i}• (Explore) ''I'm here because you're supposed to end the world.'{/i}" if basement_1_shared_task == False and tower_encountered == False:
                jump basement_1_shared_task_join

            "{i}• (Explore) ''There's people out there who think you're going to end the world. What do you have to say about that?''{/i}" if basement_1_shared_task == False and tower_encountered == False:
                jump basement_1_shared_task_join

            "{i}• (Explore) ''What's your name?''{/i}" if basement_1_name_ask == False:
                $ basement_1_knife_vague_count += 1
                $ basement_1_name_ask = True
                show princess c cold onlayer back with dissolve
                voice "audio/voices/ch1/knife/narrator/knife_n_116.flac"
                n "She hesitates before answering.\n"
                show princess c bored talk onlayer back with dissolve
                voice "audio/voices/ch1/knife/princess/stab_p_71.flac"
                p "You can address me as Your Royal Highness, or Her Majesty. Any honorific should do, really.\n"
                show princess c bored onlayer back with dissolve
                if basement_1_knife_vague_count == 1:
                    voice "audio/voices/ch1/knife/narrator/knife_n_117.flac"
                    n "Note the lack of detail. You can't trust her.\n"
                elif basement_1_knife_vague_count == 2:
                    voice "audio/voices/ch1/knife/narrator/knife_n_118.flac"
                    n "Again, she offers no specifics. No matter how hard you try, you'll never get a straight answer out of her.\n"
                jump basement_1_knife_dropped_menu

            "{i}• (Explore) ''How long have you been down here?''{/i}" if basement_1_knife_how_long == False:
                default basement_1_knife_how_long = False
                $ basement_1_knife_vague_count += 1
                $ basement_1_knife_how_long = True
                show princess c bored talk onlayer back with dissolve
                voice "audio/voices/ch1/knife/princess/stab_p_72.flac"
                p "Too long.\n"
                show princess c bored onlayer back
                if basement_1_knife_vague_count == 1:
                    voice "audio/voices/ch1/knife/narrator/knife_n_117.flac"
                    n "Note the lack of detail. You can't trust her.\n"
                elif basement_1_knife_vague_count == 2:
                    voice "audio/voices/ch1/knife/narrator/knife_n_118.flac"
                    n "Again, she offers no specifics. No matter how hard you try, you'll never get a straight answer out of her.\n"
                jump basement_1_knife_dropped_menu

            "{i}• (Explore) ''Do you know {i}why{/i} I'm here to kill you?''{/i}" if basement_1_knife_why_here_explore == False and basement_1_shared_task == False:
                #$ basement_1_shared_task = True
                default basement_1_knife_why_here_explore = False
                $ basement_1_knife_why_here_explore = True
                show princess c cold talk onlayer back with dissolve
                voice "audio/voices/ch1/knife/princess/stab_p_73.flac"
                p "Do you?\n"
                menu:
                    extend ""

                    "{i}• ''You're apparently going to end the world.''{/i}" if tower_encountered == False:
                        jump basement_1_shared_task_join

                    "{i}• ''I know what I've been told. Whether or not I believe it is an entirely different matter.''{/i}":
                        show princess c bored talk onlayer back with dissolve
                        voice "audio/voices/ch1/knife/princess/stab_p_73b.flac"
                        p "So you're not going to share? How pointless. If you want to talk, I'll talk, but this isn't talking.\n"
                        show princess c bored onlayer back with dissolve
                        jump basement_1_knife_dropped_menu

                    "{i}• (Lie) ''No.''{/i}":
                        show princess c serious talk onlayer back with dissolve
                        voice "audio/voices/ch1/knife/princess/stab_p_74.flac"
                        p "You're lying.\n"
                        show princess c serious onlayer back with dissolve
                        voice "audio/voices/ch1/knife/hero/k_h_50.flac"
                        hero "How does she know that?\n"
                        show princess c cold talk onlayer back with dissolve
                        voice "audio/voices/ch1/knife/princess/stab_p_75.flac"
                        p "Don't think that just because I'm the one in chains it means you have a right to interrogate me.\n"
                        show princess c sad glance onlayer back with dissolve
                        jump basement_1_knife_dropped_menu

                    "{i}• [[Remain silent.]{/i}":
                        show princess c bored talk onlayer back with dissolve
                        voice "audio/voices/ch1/knife/princess/stab_p_76.flac"
                        p "I see. The silent treatment. You know, if you don't share with me, I'm not going to share with you.\n"
                        show princess c bored onlayer back with dissolve
                        jump basement_1_knife_dropped_menu

            "{i}• ''Okay, we've talked enough...''{/i}":
                show princess c bored talk onlayer back with dissolve
                voice "audio/voices/ch1/knife/princess/stab_p_77.flac"
                p "Oh. Have you decided what to do with me?\n"
                show princess c serious onlayer back with dissolve
                voice "audio/voices/ch1/knife/narrator/knife_n_119.flac"
                n "You know why you're here...\n"
                menu:

                    "{i}• [[Slay the Princess.]{/i}" if (can_spectre and (spectre_encountered == False or razor_encountered == False)) or (basement_1_nerves_armed and razor_encountered == False) or (basement_1_nerves_steeled_hesitated and (adversary_encountered == False or tower_encountered == False or nightmare_encountered == False)) or (basement_1_nerves_fear and tower_encountered == False) and can_slay:
                        play audio "audio/one_shot/knife_pickup.flac"
                        $ blade_held = True
                        $ default_mouse = "blade"
                        jump basement_1_knife_slay_join

                    "{i}• ''I'm getting you out of here.'' [[Examine the chains.]{/i}" if prisoner_encountered == False or tower_encountered == False or adversary_encountered == False:
                        show princess c nervous smile onlayer back with dissolve
                        voice "audio/voices/ch1/knife/narrator/knife_n_120.flac"
                        n "Oh, you have to be kidding me!\n"
                        jump basement_1_knife_rescue

                    "{i}• ''I'm going to keep you locked away down here. At least for a bit. We can get to know each other better while I decide what to do.'' [[Keep her locked away.]{/i}" if nightmare_encountered == False:
                        label basement_1_knife_nightmare_join:
                            show princess c haughty onlayer back with dissolve
                            voice "audio/voices/ch1/knife/hero/k_h_51.flac"
                            hero "That seems like a pretty good compromise.\n"
                            voice "audio/voices/ch1/knife/narrator/knife_n_121.flac"
                            n "Leaving her alive is too risky. If you don't deal with her soon, she {i}will{/i} find a way out.\n"
                            show princess c bored talk onlayer back with dissolve
                            voice "audio/voices/ch1/knife/princess/stab_p_78.flac"
                            sp "One way or another, I'm going to find a way out of here. You can make it easier for both of us if you help.\n"
                            show princess c cold talk onlayer back with dissolve
                            voice "audio/voices/ch1/knife/princess/stab_p_78b.flac"
                            sp "And if you don't...\n"
                            show princess c sinister talk onlayer back with dissolve
                            voice "audio/voices/ch1/knife/princess/stab_p_79.flac"
                            sp "I can promise that you'll come to regret that decision.\n"
                            show princess c sinister onlayer back with dissolve
                            voice "audio/voices/ch1/knife/narrator/knife_n_122.flac"
                            n "You have to make a choice. Let's hope for all our sakes it's the right one.\n"
                            menu:
                                extend ""

                                "{i}• [[Slay the Princess.]{/i}" if tower_encountered == False or (basement_1_nerves_armed and razor_encountered == False):
                                    $ basement_1_nerves_fear = True
                                    play audio "audio/one_shot/knife_pickup.flac"
                                    $ blade_held = False
                                    $ default_mouse = "blade"
                                    jump basement_1_knife_slay_join

                                "{i}• ''Okay. Let's get you out of here.'' [[Examine the chains.]{/i}" if prisoner_encountered == False or tower_encountered == False or adversary_encountered == False:
                                    show princess c serious onlayer back with dissolve
                                    voice "audio/voices/ch1/knife/narrator/knife_n_123.flac"
                                    n "Oh, for the love of...\n"
                                    show princess c serious talk onlayer back with dissolve
                                    voice "audio/voices/ch1/knife/princess/stab_p_80.flac"
                                    p "Good. I'm glad you've come to your senses.\n"
                                    voice "audio/voices/ch1/knife/narrator/knife_n_124.flac"
                                    show princess c nervous smile onlayer back with dissolve
                                    n "You're making a huge mistake.\n"
                                    voice "audio/voices/ch1/knife/hero/k_h_52.flac"
                                    hero "No. You're doing the right thing.\n"
                                    jump basement_1_knife_rescue

                                "{i}• Uh, I {i}made{/i} my choice. I'm locking her in the basement.{/i}":
                                    show princess c serious onlayer back with dissolve
                                    voice "audio/voices/ch1/knife/narrator/knife_n_125.flac"
                                    n "I know you think this is a fair compromise, but it isn't. {b}No one{/b} wins here.\n"
                                    voice "audio/voices/ch1/knife/hero/k_h_53.flac"
                                    hero "It's a chance we'll have to take. We can make this work. If we just stay here and keep watch, no one has to die.\n"
                                    show princess c serious talk onlayer back with dissolve
                                    voice "audio/voices/ch1/knife/princess/stab_p_81.flac"
                                    sp "You're making a mistake.\n"
                                    show princess c sinister onlayer back with dissolve
                                    #voice "audio/voices/ch1/knife/narrator/knife_n_126.flac"
                                    #n "Her voice is unsettlingly playful."
                                    play audio "audio/one_shot/footsteps_hike_short.flac"
                                    voice "audio/voices/ch1/knife/narrator/knife_n_127.flac"
                                    play audio "audio/one_shot/knife_pickup.flac"
                                    $ blade_held = False
                                    $ default_mouse = "blade"
                                    $ quick_menu = False
                                    hide princess onlayer back
                                    hide bg onlayer farback
                                    show basement stairs open onlayer front at Position(ypos=1125)
                                    with fade
                                    if persistent.quick_menu:
                                        $ quick_menu = True
                                    n "You turn your back to the Princess and make your way to the stairs.\n"
                                    voice "audio/voices/ch1/knife/princess/stab_p_82.flac"
                                    sp "It won't be long before I slip these chains. And once I'm out of here, there will be hell to pay for leaving me behind.\n"
                                    voice "audio/voices/ch1/empty/hero/empty_h_16.flac"
                                    hero "'Slip these chains?' She can't, right? She needed our help to get out of here. But do you hear the conviction in her voice? I don't think she's bluffing.\n"
                                    voice "audio/voices/ch1/knife/narrator/knife_n_128.flac"
                                    n "Either way, she dropped her mask, didn't she? You can still turn around and finish the job.\n"
                                    menu:
                                        extend ""

                                        "{i}• No, we're sticking to the plan and locking her down here.{/i}":
                                            default nightmare_no_wounds = False
                                            $ nightmare_no_wounds = True
                                            voice "audio/voices/ch1/knife/narrator/knife_n_129.flac"
                                            n "You'll be the death of all of us, but fine. Have it your way.\n"
                                            play audio "audio/one_shot/footsteps_creaky.flac"
                                            $ quick_menu = False
                                            hide basement onlayer front
                                            scene bg black
                                            with fade
                                            jump nightmare_join

                                        "{i}• Oh that's a relief! I was afraid I'd already committed to not slaying her.{/i}" if tower_encountered == False:
                                            $ basement_1_nerves_fear = True
                                            voice "audio/voices/ch1/knife/narrator/knife_n_130.flac"
                                            n "It's never too late to do the right thing. Now hurry.\n"
                                            $ quick_menu = False
                                            hide basement onlayer front
                                            scene bg black
                                            with fade
                                            jump basement_1_knife_slay_join

label basement_1_knife_rescue:
    show princess c thinking onlayer back with dissolve
    voice "audio/voices/ch1/knife/narrator/knife_n_131.flac"
    play audio "audio/one_shot/chain_2.flac"
    n "You walk up to the chains binding the Princess to the wall and give them a tug.\n"
    voice "audio/voices/ch1/knife/narrator/knife_n_132.flac"
    n "They're large and heavy, far too solid for you to even imagine trying to break them apart.\n"
    show princess c serious talk onlayer back with dissolve
    if basement_1_knife_how_escape == False:
        voice "audio/voices/ch1/knife/princess/stab_p_83.flac"
        p "I'm guessing you don't have the key.\n"
        show princess c serious onlayer back with dissolve
        voice "audio/voices/ch1/knife/hero/k_h_54.flac"
        hero "Maybe it's somewhere upstairs.\n"
    else:
        voice "audio/voices/ch1/knife/princess/stab_p_84.flac"
        p "If you don't have the key, maybe you should go looking for it. I'm sure it's somewhere upstairs.\n"
        show princess c serious onlayer back with dissolve
    voice "audio/voices/ch1/knife/narrator/knife_n_133.flac"
    n "Doubtful. Whoever locked the Princess away down here intended for her to never see the light of day. They wouldn't have just left the key to her chains somewhere in the cabin.\n"
    menu:
        extend ""

        "{i}• ''And if there isn't a key... do you have any ideas? Besides me cutting you out of here?''{/i}" if basement_1_knife_how_escape:
            show princess c cold talk onlayer back with dissolve
            voice "audio/voices/ch1/knife/princess/stab_p_85.flac"
            p "That would be fine. I can lose an arm.\n"
            show princess c cold onlayer back with dissolve
            voice "audio/voices/ch1/knife/narrator/knife_n_134.flac"
            n "She speaks with almost complete nonchalance.\n"
            voice "audio/voices/ch1/knife/hero/k_h_55.flac"
            hero "If we were stuck down here for long enough, I'm sure we'd be nonchalant about cutting our way out. Anything to finally be free.\n"

        "{i}• ''And if there isn't a key... do you have any ideas?''{/i}" if basement_1_knife_how_escape == False:
            show princess c cold talk onlayer back with dissolve
            voice "audio/voices/ch1/knife/princess/stab_p_86.flac"
            p "Well, you do have that big sharp knife. You could always cut me out of here.\n"
            show princess c cold onlayer back with dissolve
            voice "audio/voices/ch1/knife/narrator/knife_n_134.flac"
            n "She speaks with almost complete nonchalance.\n"
            voice "audio/voices/ch1/knife/hero/k_h_55.flac"
            hero "If we were stuck down here for long enough, I'm sure we'd be nonchalant about cutting our way out. Anything to finally be free.\n"

        "{i}• ''I'm going to check upstairs. Maybe the key's still lying around somewhere up there. And if not, maybe I can at least find something to break you free.''{/i}":
            show princess c cold talk onlayer back with dissolve
            voice "audio/voices/ch1/knife/princess/stab_p_87.flac"
            p "I'll be here.\n"

    play secondary "audio/one_shot/footsteps_creaky.flac"
    queue secondary "audio/one_shot/door_close.flac"
    queue secondary "audio/one_shot/lock_click.flac"
    voice "audio/voices/ch1/knife/narrator/knife_n_135.flac"
    $ quick_menu = False
    hide princess onlayer back
    hide bg onlayer farback
    show basement stairs closed onlayer front at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    n "You attempt to make your way out of the basement, but the door at the top of the stairs slams shut. You hear the click of a lock sliding into place.\n"
    voice "audio/voices/ch1/empty/hero/empty_h_21.flac"
    hero "Is someone else here?\n"
    label basement_1_knife_rescue_door:
        default basement_1_knife_rescue_door_try_explore = False
        default basement_1_knife_rescue_door_force_explore = False
        default basement_1_knife_rescue_door_shout_explore = False
        menu:
            extend ""

            "{i}• (Explore) ''Hey! Let me out of here!''{/i}" if basement_1_knife_rescue_door_shout_explore == False:
                $ basement_1_knife_rescue_door_shout_explore = True
                voice "audio/voices/ch1/knife/narrator/knife_n_136.flac"
                n "Your shouts and pleas are met with silence.\n"
                if basement_1_knife_rescue_door_try_explore == True:
                    voice "audio/voices/ch1/knife/narrator/knife_n_137.flac"
                    n "I'll repeat myself once again. You're here to slay the Princess, and you won't leave until the task is done.\n"
                else:
                    voice "audio/voices/ch1/knife/narrator/knife_n_138.flac"
                    n "You're here to slay the Princess, and you won't leave until the task is done.\n"
                jump basement_1_knife_rescue_door

            "{i}• (Explore) [[Try the door.]{/i}" if basement_1_knife_rescue_door_try_explore == False:
                play audio "audio/one_shot/door_try.flac"
                $ basement_1_knife_rescue_door_try_explore = True
                voice "audio/voices/ch1/knife/narrator/knife_n_139.flac"
                n "You try the door, but it's locked from the outside.\n"
                if basement_1_knife_rescue_door_shout_explore == True:
                    voice "audio/voices/ch1/knife/narrator/knife_n_137.flac"
                    n "I'll repeat myself once again. You're here to slay the Princess, and you won't leave until the task is done.\n"
                else:
                    voice "audio/voices/ch1/knife/narrator/knife_n_138.flac"
                    n "You're here to slay the Princess, and you won't leave until the task is done.\n"
                jump basement_1_knife_rescue_door

            "{i}• [[Return to the bottom of the stairs.]{/i}":
                play audio "audio/one_shot/footsteps_creaky.flac"
                voice "audio/voices/ch1/knife/narrator/knife_n_140.flac"
                $ quick_menu = False
                hide basement onlayer front
                scene bg basement distant onlayer farback at Position(ypos=1125)
                show back basement distant onlayer back at Position(ypos=1125)
                show princess d haughty onlayer back at Position(ypos=1125)
                with fade
                if persistent.quick_menu:
                    $ quick_menu = True
                n "You make your way back to the bottom of the stairs. This would have been so much easier if you'd simply slain her like you were supposed to.\n"
                voice "audio/voices/ch1/empty/hero/empty_h_22.flac"
                hero "Easier for whom?\n"
                voice "audio/voices/ch1/knife/narrator/knife_n_141.flac"
                n "Easier for {i}everyone{/i}.\n"

        $ quick_menu = False
        hide bg onlayer farback
        hide back onlayer back
        hide princess onlayer back
        show bg basement close onlayer farback at Position(ypos=1125)
        show princess c cold onlayer back at Position(ypos=1125)
        with fade
        if persistent.quick_menu:
            $ quick_menu = True
        show princess c cold talk onlayer back with dissolve
        voice "audio/voices/ch1/knife/princess/stab_p_88.flac"
        p "I heard the door slam... they locked you down here too, didn't they?\n"
        show princess c serious talk onlayer back with dissolve
        voice "audio/voices/ch1/knife/princess/stab_p_89.flac"
        p "The knife. Pick it up and cut me out of here.\n"
        play secondary "audio/one_shot/knife_pickup.flac"
        $ blade_held = True
        $ default_mouse = "blade"
        show princess c serious onlayer back at Position(ypos=1125) with dissolve
        voice "audio/voices/ch1/knife/narrator/knife_n_142.flac"
        n "You won't like what happens if you do that...\n"
        if preferences.self_voicing == False:
            $ config.menu_include_disabled = True
        menu:
            extend ""

            "{i}• [[Save the Princess.]{/i}" if prisoner_encountered == False or tower_encountered == False:
                $ default_mouse = "blood"
                play audio "audio/one_shot/stab_fleshy.flac"
                voice "audio/voices/ch1/knife/narrator/knife_n_143.flac"
                hide bg onlayer farback
                hide princess onlayer back
                show bg princess cut onlayer back at Position(ypos=1125)
                show princess clean cut onlayer front at Position(ypos=1125)
                with dissolve
                n "Against your better judgment, you place the blade against the Princess' arm, just above the massive, unyielding chain.\n"
                play audio "audio/one_shot/stab_goop.flac"
                voice "audio/voices/ch1/knife/narrator/knife_n_144.flac"
                n "You cut into her flesh.\n"
                play audio "audio/one_shot/arm_rip.flac"
                voice "audio/voices/ch1/knife/narrator/knife_n_145.flac"
                hide bg princess cut onlayer back
                hide princess onlayer front
                show bg generic onlayer back at Position(ypos=1125)
                show princess arm pull clean onlayer front at Position(ypos=1125)
                with dissolve
                n "The blade is sharp, and you make quick work of it. Before long, you're able to crack through bone, and she pulls the bleeding stub of her arm through the iron gauntlet.\n"
                voice "audio/voices/ch1/knife/hero/k_h_56.flac"
                hero "She didn't so much as utter a sound...\n"
                # REPLACE
                voice "audio/voices/ch1/knife/narrator/knife_n_146.flac"
                show princess free steel onlayer front at Position(ypos=1125)
                with dissolve
                n "Free from her bindings, the Princess turns to face you, her fierce gaze meeting your eye.\n"
                # OLD
                #n "The Princess clutches the wound, her fierce gaze meeting your eye.\n"
                voice "audio/voices/ch1/knife/hero/k_h_57.flac"
                hero "How is she so composed after losing an arm? It's like she isn't even bothered by it.\n"
                voice "audio/voices/ch1/knife/princess/stab_p_90.flac"
                show princess free steel talk onlayer front at Position(ypos=1125)
                with dissolve
                p "Thank you. Now let's get out of here.\n"
                show princess free steel onlayer front at Position(ypos=1125)
                with dissolve
                menu:
                    extend ""

                    "{i}• [[Approach the locked door.]{/i}":
                        play audio "audio/one_shot/footsteps_hike_short.flac"
                        voice "audio/voices/ch1/knife/narrator/knife_n_147.flac"
                        hide princess onlayer front
                        hide bg onlayer back
                        show bg black onlayer front at Position(ypos=1125)
                        with dissolve
                        n "No. We won't have any of that. The stakes are too high. You can't just let her escape into the world.\n... no. {i}I{/i} just can't let her escape into the world.\n"
                        voice "audio/voices/ch1/knife/narrator/knife_n_148.flac"
                        hide bg onlayer front
                        show bg generic onlayer back at Position(ypos=1125)
                        show fury back onlayer front at Position(ypos=1125)
                        show player bloody knife onlayer inyourface at Position(ypos=1125)
                        with dissolve
                        n "As the Princess approaches the bottom stair, your body steps forward and raises the blade.\n"
                        voice "audio/voices/ch1/knife/hero/k_h_58.flac"
                        hero "Wait... this isn't fair. You can't just {i}do{/i} that!\n"
                        voice "audio/voices/ch1/knife/narrator/knife_n_149.flac"
                        n "Watch me.\n"
                        if tower_encountered and preferences.self_voicing == False:
                            $ config.menu_include_disabled = True
                        $ small_yadj = True
                        menu:
                            extend ""

                            "{i}• [[Slay the Princess.]{/i}" if tower_encountered == False:
                                label basement_1_knife_rescue_controlled_start:
                                    $ small_yadj = False
                                    $ config.menu_include_disabled = False
                                    play audio "audio/one_shot/knife_stab.flac"
                                    voice "audio/voices/ch1/knife/narrator/knife_n_150.flac"
                                    hide player onlayer inyourface
                                    show fury stub betrayed onlayer front
                                    with dissolve
                                    n "You bring the blade down and plunge it into the Princess' back. {i}Finally{/i}.\n"
                                    voice "audio/voices/ch1/knife/hero/k_h_59.flac"
                                    hero "Okay. There's no going back now.\n"
                                    voice "audio/voices/ch1/knife/narrator/knife_n_151.flac"
                                    show fury stub betrayed talk onlayer front with dissolve
                                    n "Though the blade left a deep gash in her shoulder, she barely so much as flinches, turning around to stare at you incredulously.\n"
                                    voice "audio/voices/ch1/knife/princess/stab_p_91.flac"
                                    show fury stub betrayed talk2 onlayer front with dissolve
                                    spmid "Are you serious?\n"
                                    voice "audio/voices/ch1/knife/princess/stab_p_92.flac"
                                    show fury stub betrayed talk open onlayer front with dissolve
                                    spmid "I don't know what came over you, but if we're doing this, I guess I'll have to kill you.\n"
                                    voice "audio/voices/ch1/knife/princess/stab_p_92a.flac"
                                    show fury stub betrayed talk2 onlayer front with dissolve
                                    spmid "Do you think I need both of my arms to do that? I can beat you to death with one.\n"
                                    voice "audio/voices/ch1/knife/princess/stab_p_93.flac"
                                    hide fury onlayer front
                                    show bg fury chain stabbed onlayer back
                                    show fury stub betrayed tall talk onlayer front at Position(ypos=1125)
                                    show player fury stub betrayed tall hand onlayer inyourface at Position(ypos=1125)
                                    with dissolve
                                    sp "But I don't have to tell you that. I'll go ahead and show you.\n"
                                    #voice "audio/voices/ch1/empty/hero/empty_h_28.flac"
                                    show fury stub betrayed tall onlayer front with dissolve
                                    #hero "Do you hear the conviction in her voice? Do you see that razor sharpness in her gaze? I don't think she's bluffing.\n"
                                    menu:
                                        extend ""

                                        "{i}• [[Slay the Princess.]{/i}":
                                            jump basement_1_knife_rescue_controlled_2_start

                                        "{i}• [[Give up.]{/i}":
                                            $ tower_pathetic = True
                                            jump basement_1_knife_fury

                                    label basement_1_knife_fury:
                                        play secondary "audio/one_shot/knife_bounce_several.flac"
                                        $ default_mouse = "default"
                                        $ current_princess = "tower"
                                        $ config.menu_include_disabled = False
                                        # REPLACE
                                        voice "audio/voices/ch1/knife/narrator/knife_n_152.flac"
                                        show fury stub betrayed haymaker onlayer front at Position(ypos=1125)
                                        with dissolve
                                        n "{i}Sigh{/i}. As the blade falls from your trembling hands, the Princess rears back, readying a bone-shattering haymaker.\n"
                                        # old line
                                        #n "Before you have the opportunity to make another move, she rears back and hits you with a bone-shattering haymaker.\n"
                                        play audio "audio/one_shot/ear_ring.flac"
                                        play secondary "audio/one_shot/punch_one.flac"
                                        queue secondary "audio/one_shot/collapse.flac"
                                        # REPLACE
                                        voice "audio/voices/ch1/knife/narrator/knife_n_153.flac"
                                        $ quick_menu = False
                                        hide player onlayer inyourface
                                        hide bg onlayer back
                                        show bg fury stub betrayed loom onlayer back at Position(ypos=1125)
                                        show fury stub betrayed loom onlayer front at Position(ypos=1125)
                                        with fade
                                        if persistent.quick_menu:
                                            $ quick_menu = True
                                        n "You fall to your knees. You're barely able to process the ringing in your ears before she hits you again.\n"
                                        # old
                                        #n "You fall to your knees. You're barely able to bring your trembling arms up to defend yourself before she hits you again.\n"
                                        play audio "audio/one_shot/punch_many.flac"
                                        voice "audio/voices/ch1/knife/narrator/knife_n_154.flac"
                                        hide bg onlayer back
                                        hide fury onlayer front
                                        show bg generic dark onlayer back at Position(ypos=1125)
                                        show battle fury stub betrayed onlayer front at Position(ypos=1125)
                                        #show battle1 fury stub betrayed onlayer front at Position(ypos=1125)
                                        #show battle2 fury stub betrayed onlayer front at Position(ypos=1125)
                                        #show battle3 fury stub betrayed onlayer front at Position(ypos=1125)
                                        with Dissolve(0.75)
                                        n "Every blow is as punishing as the first. You feel bones shatter with every impact, unknown ruptures blossoming with blood somewhere inside of you.\n"
                                        voice "audio/voices/ch1/knife/narrator/knife_n_155.flac"
                                        $ quick_menu = False
                                        hide battle onlayer front
                                        hide bg onlayer back
                                        show bg fury stub betrayed loom onlayer back at Position(ypos=1125)
                                        show fury stub betrayed loom onlayer front at Position(ypos=1125)
                                        with fade
                                        if persistent.quick_menu:
                                            $ quick_menu = True
                                        n "If we're lucky, the wound you managed to inflict will be enough to at least delay her escape from this place. If we're very lucky, it will kill her before she gets out.\n"
                                        voice "audio/voices/ch1/knife/princess/stab_p_94.flac"
                                        sp "Too weak to even try fighting back. How disappointing.\n"
                                        play audio "audio/one_shot/thump.flac"
                                        voice "audio/voices/ch1/knife/narrator/knife_n_156.flac"
                                        play audio "audio/one_shot/knife_bounce_several.flac"
                                        $ blade_held = False
                                        $ default_mouse = "default"
                                        show fury stub betrayed foot onlayer front at Position(ypos=1125) with dissolve
                                        n "She places a confident heel on your chest and pushes you down to the ground.\n"
                                        play audio "audio/one_shot/knee_drop.flac"
                                        voice "audio/voices/ch1/knife/narrator/knife_n_157.flac"
                                        show fury stub betrayed kneel onlayer front at Position(ypos=1125) with dissolve
                                        n "Her knee falls to your throat, your windpipe crushed beneath a weight you didn't think her slight form could possibly possess.\n"
                                        voice "audio/voices/ch1/empty/hero/empty_h_29.flac"
                                        hero "It can't just end like this, right?\n"
                                        play audio "audio/one_shot/knee_kill.flac"
                                        voice "audio/voices/ch1/knife/narrator/knife_n_158.flac"
                                        n "I'm sorry, but it's over.\n"
                                        $ persistent.death_count += 1
                                        voice "audio/voices/ch1/knife/narrator/knife_n_159.flac"
                                        stop music fadeout 1.0
                                        stop sound fadeout 1.0
                                        hide bg onlayer back
                                        hide fury onlayer front
                                        show bg black onlayer back at Position(ypos=1125)
                                        with dissolve
                                        n "Everything goes dark, and you die.\n"
                                        hide bg black onlayer back with dissolve
                                        jump start_2

                            "{i}• [[Slay the Princess.]{/i}" if tower_encountered == False and preferences.self_voicing == False:
                                jump basement_1_knife_rescue_controlled_start

                            "{i}• [[Slay the Princess.]{/i}" if tower_encountered == False and preferences.self_voicing == False:
                                jump basement_1_knife_rescue_controlled_start

                            "{i}• [[Slay the Princess.]{/i}" if tower_encountered == False and preferences.self_voicing == False:
                                jump basement_1_knife_rescue_controlled_start

                            "{i}• [[Slay the Princess.]{/i}" if tower_encountered == False and preferences.self_voicing == False:
                                jump basement_1_knife_rescue_controlled_start

                            "{i}• [[Slay the Princess.]{/i}" if tower_encountered == False and preferences.self_voicing == False:
                                jump basement_1_knife_rescue_controlled_start

                            "{i}• [[Slay the Princess.]{/i}" if tower_encountered == False and preferences.self_voicing == False:
                                jump basement_1_knife_rescue_controlled_start

                            "{i}• [[Slay the Princess.]{/i}" if tower_encountered == False and preferences.self_voicing == False:
                                jump basement_1_knife_rescue_controlled_start

                            "{i}• [[Slay the Princess.]{/i}" if tower_encountered == False and preferences.self_voicing == False:
                                jump basement_1_knife_rescue_controlled_start

                            "{i}• [[Slay the Princess.]{/i}" if tower_encountered == False and preferences.self_voicing == False:
                                jump basement_1_knife_rescue_controlled_start

                            "{i}• [[Slay the Princess.]{/i}" if tower_encountered == False and preferences.self_voicing == False:
                                jump basement_1_knife_rescue_controlled_start

                            "{i}• [[Slay the Princess.]{/i}" if tower_encountered == False and preferences.self_voicing == False:
                                jump basement_1_knife_rescue_controlled_start

                            "{i}• [[Warn her.]{/i}":
                                #y "Something's controlling me! Watch out!"
                                voice "audio/voices/ch1/knife/narrator/knife_n_160.flac"
                                n "Stop that.\n"
                                voice "audio/voices/ch1/knife/princess/stab_p_95.flac"
                                #sp "Oh. I thought this was a little too easy.\n"
                                sp "I thought this was a little too easy.\n"
                                # REPLACE
                                play audio "audio/one_shot/knife_slash.flac"
                                hide fury onlayer front
                                hide player onlayer inyourface
                                show bg black onlayer back at Position(ypos=1125)
                                show knife slice onlayer front at yflip, Position(ypos=1125)
                                $ renpy.pause(1.0)
                                hide knife onlayer front
                                show bg generic onlayer back at Position(ypos=1125)
                                show fury stub betrayed talk onlayer front at Position(ypos=1125)
                                with dissolve
                                voice "audio/voices/ch1/knife/narrator/knife_n_161.flac"
                                n "Your body lunges forward to sink the blade into her back, but the Princess swiftly moves out the way before you can connect.\n"
                                # old
                                # n "Your body lunges forward to sink the blade into her back, but the Princess dodges.\n"
                                voice "audio/voices/ch1/knife/narrator/knife_n_162.flac"
                                n "Stop it! Stop resisting me! I am trying to get you out of here alive.\n"
                                menu:
                                    extend ""

                                    "{i}• [[Slay the Princess.]{/i}" if tower_encountered == False:
                                        label basement_1_knife_rescue_controlled_2_start:
                                            $ small_yadj = False
                                            $ config.menu_include_disabled = False
                                            voice "audio/voices/ch1/knife/narrator/knife_n_163.flac"
                                            n "{i}Thank{/i} you.\n"
                                            $ current_princess = "tower"
                                            play audio "audio/one_shot/knife_slash.flac"
                                            hide bg onlayer back
                                            hide fury onlayer front
                                            hide player onlayer inyourface
                                            show bg black onlayer back at Position(ypos=1125)
                                            show knife slice onlayer front at yflip, Position(ypos=1125)
                                            voice "audio/voices/ch1/knife/narrator/knife_n_164.flac"
                                            n "You swing your arm towards her throat, the blade singing through the air.\n"
                                            play secondary "audio/one_shot/thump.flac"
                                            queue secondary "audio/one_shot/arm_crush_buildup.flac"
                                            voice "audio/voices/ch1/knife/narrator/knife_n_165.flac"
                                            hide knife onlayer front
                                            show bg generic onlayer back at Position(ypos=1125)
                                            show fury stub resist crush 1 onlayer front at Position(ypos=1125)
                                            with dissolve
                                            n "But she's ready for it. She grabs your arm, her grip like a stone vice.\n"
                                            $ blade_held = False
                                            $ default_mouse = "default"
                                            play secondary "audio/one_shot/crunch_prime.flac"
                                            queue secondary "audio/one_shot/knife_bounce_several.flac"
                                            voice "audio/voices/ch1/knife/narrator/knife_n_165b.flac"
                                            show fury stub resist crush 2 onlayer front
                                            with dissolve
                                            n "You drop the blade. Pathetically.\n"
                                            voice "audio/voices/ch1/knife/narrator/knife_n_166.flac"
                                            show fury stub betrayed haymaker onlayer front at Position(ypos=1125)
                                            with dissolve
                                            n "She lets go, and faster than you can react, rears back and hits you with a bone-shattering haymaker.\n"
                                            play secondary "audio/one_shot/punch_one.flac"
                                            play audio "audio/one_shot/ear_ring.flac"
                                            voice "audio/voices/ch1/knife/narrator/knife_n_167.flac"
                                            $ quick_menu = False
                                            hide bg onlayer back
                                            hide fury onlayer front
                                            show bg fury stub betrayed distant onlayer farback at Position(ypos=1125)
                                            show fury stub betrayed distant foreground onlayer back at Position(ypos=1125)
                                            with fade
                                            if persistent.quick_menu:
                                                $ quick_menu = True
                                            n "There's a ringing in your ears. You're fairly certain you can feel bone grinding against bone where she fractured your jaw, but your body isn't allowing you to feel much right now, adrenaline coursing through your system and numbing your nerves.\n"
                                            play audio "audio/one_shot/collapse.flac"
                                            voice "audio/voices/ch1/knife/narrator/knife_n_168.flac"
                                            $ quick_menu = False
                                            hide bg onlayer farback
                                            hide fury onlayer back
                                            show bg fury stub betrayed loom onlayer back at Position(ypos=1125)
                                            show fury stub gohan loom onlayer front at Position(ypos=1125)
                                            with fade
                                            if persistent.quick_menu:
                                                $ quick_menu = True
                                            n "You fall to your knees. You're barely able to bring your trembling arms up to defend yourself before she hits you again.\n"
                                            play audio "audio/one_shot/punch_many.flac"
                                            voice "audio/voices/ch1/knife/narrator/knife_n_154.flac"
                                            show fury stub gohan kick onlayer front at Position(ypos=1125)
                                            show player defend razor onlayer inyourface at Position(ypos=1125)
                                            with dissolve
                                            n "Every blow is as punishing as the first. You feel bones shatter with every impact, unknown ruptures blossoming with blood somewhere inside of you.\n"
                                            voice "audio/voices/ch1/knife/princess/stab_p_96.flac"
                                            $ quick_menu = False
                                            hide bg onlayer back
                                            hide player onlayer inyourface
                                            show bg fury stub betrayed loom onlayer back at Position(ypos=1125)
                                            show fury stub gohan loom onlayer front at Position(ypos=1125)
                                            with fade
                                            if persistent.quick_menu:
                                                $ quick_menu = True
                                            sp "You poor thing. I'll go ahead and put you out of your misery.\n"
                                            play audio "audio/one_shot/thump.flac"
                                            voice "audio/voices/ch1/knife/narrator/knife_n_156.flac"
                                            show fury stub gohan foot onlayer front with dissolve
                                            n "She places a confident heel on your chest and pushes you down to the ground.\n"
                                            play audio "audio/one_shot/knee_drop.flac"
                                            voice "audio/voices/ch1/knife/narrator/knife_n_157.flac"
                                            show fury stub betrayed kneel onlayer front at Position(ypos=1125) with dissolve
                                            n "Her knee falls to your throat, your windpipe crushed beneath a weight you didn't think her slight form could possibly possess.\n"
                                            voice "audio/voices/ch1/empty/hero/empty_h_29.flac"
                                            play audio "audio/one_shot/knee_kill.flac"
                                            hero "It can't just end like this, right?\n"
                                            voice "audio/voices/ch1/knife/narrator/knife_n_158.flac"
                                            n "I'm sorry, but it's over.\n"
                                            $ persistent.death_count += 1
                                            voice "audio/voices/ch1/knife/narrator/knife_n_159.flac"
                                            $ quick_menu = False
                                            stop music fadeout 1.0
                                            stop sound fadeout 1.0
                                            hide bg onlayer back
                                            hide fury onlayer front
                                            show bg black onlayer back at Position(ypos=1125)
                                            with dissolve
                                            n "Everything goes dark, and you die.\n"
                                            hide bg black onlayer back with dissolve
                                            jump start_2

                                    "{i}• [[Slay the Princess.]{/i}" if tower_encountered == False and preferences.self_voicing == False:
                                        jump basement_1_knife_rescue_controlled_2_start

                                    "{i}• [[Slay the Princess.]{/i}" if tower_encountered == False and preferences.self_voicing == False:
                                        jump basement_1_knife_rescue_controlled_2_start

                                    "{i}• [[Slay the Princess.]{/i}" if tower_encountered == False and preferences.self_voicing == False:
                                        jump basement_1_knife_rescue_controlled_2_start

                                    "{i}• [[Slay the Princess.]{/i}" if tower_encountered == False and preferences.self_voicing == False:
                                        jump basement_1_knife_rescue_controlled_2_start

                                    "{i}• [[Slay the Princess.]{/i}" if tower_encountered == False and preferences.self_voicing == False:
                                        jump basement_1_knife_rescue_controlled_2_start

                                    "{i}• [[Slay the Princess.]{/i}" if tower_encountered == False and preferences.self_voicing == False:
                                        jump basement_1_knife_rescue_controlled_2_start

                                    "{i}• [[Slay the Princess.]{/i}" if tower_encountered == False and preferences.self_voicing == False:
                                        jump basement_1_knife_rescue_controlled_2_start

                                    "{i}• [[Slay the Princess.]{/i}" if tower_encountered == False and preferences.self_voicing == False:
                                        jump basement_1_knife_rescue_controlled_2_start

                                    "{i}• [[Slay the Princess.]{/i}" if tower_encountered == False and preferences.self_voicing == False:
                                        jump basement_1_knife_rescue_controlled_2_start

                                    "{i}• [[Slay the Princess.]{/i}" if tower_encountered == False and preferences.self_voicing == False:
                                        jump basement_1_knife_rescue_controlled_2_start

                                    "{i}• [[Slay the Princess.]{/i}" if tower_encountered == False and preferences.self_voicing == False:
                                        jump basement_1_knife_rescue_controlled_2_start

                                    "{i}• [[Slay the Princess.]{/i}" if tower_encountered == False and preferences.self_voicing == False:
                                        jump basement_1_knife_rescue_controlled_2_start

                                    "{i}• [[Slay the Princess.]{/i}" if tower_encountered == False and preferences.self_voicing == False:
                                        jump basement_1_knife_rescue_controlled_2_start

                                    "{i}• [[Slay the Princess.]{/i}" if tower_encountered == False and preferences.self_voicing == False:
                                        jump basement_1_knife_rescue_controlled_2_start

                                    "{i}• [[Resist.]{/i}" if prisoner_encountered == False:
                                        $ small_yadj = False
                                        $ config.menu_include_disabled = False
                                        $ current_princess = "prisoner"
                                        voice "audio/voices/ch1/knife/narrator/knife_n_169.flac"
                                        hide fury onlayer front
                                        show prisoner 1 turn clean onlayer front at Position(ypos=1125)
                                        show player bloody knife onlayer inyourface at Position(ypos=1125)
                                        with dissolve
                                        n "The blade! Move. The. {i}Blade{/i}!\n"
                                        voice "audio/voices/ch1/knife/princess/stab_p_97.flac"
                                        show prisoner 1 turn clean talk onlayer front with dissolve
                                        spmid "You're doing your best to help me, aren't you? I can see the conflict in your eyes.\n"
                                        play audio "audio/one_shot/footsteps_stone.flac"
                                        voice "audio/voices/ch1/knife/princess/stab_p_98.flac"
                                        show prisoner 1 blade talk onlayer front with dissolve
                                        sp "I'll make this quick.\n"
                                        # REPLACE
                                        voice "audio/voices/ch1/knife/narrator/knife_n_170.flac"
                                        play secondary "audio/one_shot/knife_pickup.flac"
                                        $ blade_held = False
                                        $ default_mouse = "default"
                                        show prisoner 1 blade onlayer front
                                        show player hand no knife onlayer inyourface at Position(ypos=1125)
                                        with dissolve
                                        n "She steps forward and pries the blade from your rigid hands.\n"
                                        # old
                                        #n "She knocks your legs out from under you with a swift kick. You didn't even see it coming.\n"
                                        # REPLACE NEW
                                        show prisoner 1 blade talk onlayer front with dissolve
                                        voice "audio/voices/ch1/knife/princess/stab_p_1p.flac"
                                        sp "Maybe I'll see you in another life.\n"
                                        play audio "audio/one_shot/new/throat_slit.flac"
                                        show prisoner 1 blade slit onlayer front with dissolve
                                        $ renpy.pause(0.5)
                                        show prisoner 1 blade bloody onlayer front with dissolve
                                        voice "audio/voices/ch1/knife/narrator/knife_nr_6.flac"
                                        n "And then she slits your throat with an almost clinical ease.\n"
                                        play audio "audio/one_shot/collapse.flac"
                                        hide player onlayer inyourface
                                        show bg ceiling onlayer back
                                        show prisoner 1 loom onlayer front
                                        with dissolve
                                        voice "audio/voices/ch1/knife/narrator/knife_nr_7.flac"
                                        n "Her face remains unchanged as she watches you collapse to the ground, blood flowing from your butchered neck.\n"
                                        voice "audio/voices/ch1/knife/hero/k_h_64.flac"
                                        hero "This is the end, isn't it?\n"
                                        $ persistent.death_count += 1
                                        $ quick_menu = False
                                        stop music fadeout 1.0
                                        stop sound fadeout 1.0
                                        hide bg onlayer back
                                        hide prisoner onlayer front
                                        show bg black onlayer back at Position(ypos=1125)
                                        with dissolve
                                        voice "audio/voices/ch1/knife/narrator/knife_nr_8.flac"
                                        n "I'm afraid it is. Everything goes dark, and you die. I hope it was worth it.\n"
                                        hide bg black onlayer back with dissolve
                                        jump start_2

                                    "{i}• [[Slay the Princess.]{/i}" if tower_encountered == False and preferences.self_voicing == False:
                                        jump basement_1_knife_rescue_controlled_2_start

                                    "{i}• [[Slay the Princess.]{/i}" if tower_encountered == False and preferences.self_voicing == False:
                                        jump basement_1_knife_rescue_controlled_2_start

                                    "{i}• [[Slay the Princess.]{/i}" if tower_encountered == False and preferences.self_voicing == False:
                                        jump basement_1_knife_rescue_controlled_2_start

                                    "{i}• [[Slay the Princess.]{/i}" if tower_encountered == False and preferences.self_voicing == False:
                                        jump basement_1_knife_rescue_controlled_2_start

                                    "{i}• [[Slay the Princess.]{/i}" if tower_encountered == False and preferences.self_voicing == False:
                                        jump basement_1_knife_rescue_controlled_2_start

                                    "{i}• [[Slay the Princess.]{/i}" if tower_encountered == False and preferences.self_voicing == False:
                                        jump basement_1_knife_rescue_controlled_2_start


                            "{i}• [[Slay the Princess.]{/i}" if tower_encountered == False and preferences.self_voicing == False:
                                jump basement_1_knife_rescue_controlled_start

                            "{i}• [[Slay the Princess.]{/i}" if tower_encountered == False and preferences.self_voicing == False:
                                jump basement_1_knife_rescue_controlled_start

                            "{i}• [[Slay the Princess.]{/i}" if tower_encountered == False and preferences.self_voicing == False:
                                jump basement_1_knife_rescue_controlled_start

                            "{i}• [[Slay the Princess.]{/i}" if tower_encountered == False and preferences.self_voicing == False:
                                jump basement_1_knife_rescue_controlled_start

                            "{i}• [[Slay the Princess.]{/i}" if tower_encountered == False and preferences.self_voicing == False:
                                jump basement_1_knife_rescue_controlled_start

                            "{i}• [[Slay the Princess.]{/i}" if tower_encountered == False and preferences.self_voicing == False:
                                jump basement_1_knife_rescue_controlled_start

                            "{i}• [[Slay the Princess.]{/i}" if tower_encountered == False and preferences.self_voicing == False:
                                jump basement_1_knife_rescue_controlled_start

                            "{i}• [[Slay the Princess.]{/i}" if tower_encountered == False and preferences.self_voicing == False:
                                jump basement_1_knife_rescue_controlled_start


            "{i}• [[Slay the Princess.]{/i}" if tower_encountered == False or adversary_encountered == False or nightmare_encountered == False:
                $ basement_1_knife_wounded = True
                $ default_mouse = "blood"
                play audio "audio/one_shot/knife_stab.flac"
                voice "audio/voices/ch1/knife/narrator/knife_n_175.flac"
                hide bg onlayer farback
                hide princess onlayer back
                show bg fury chain stabbed onlayer back at Position(ypos=1125)
                show midground fury chain stabbed onlayer front at Position(ypos=1125)
                show fury chain stabbed onlayer inyourface at Position(ypos=1125)
                with dissolve
                n "Without hesitation, you bring the blade down. The Princess flinches as you strike, and your weapon sinks into her shoulder.\n"
                voice "audio/voices/ch1/knife/princess/stab_p_99.flac"
                show fury chain stabbed glare talk onlayer inyourface at Position(ypos=1125) with dissolve
                sp "You bastard! If I have to kill you to leave this place, I'll {i}do it{/i}.\n"
                voice "audio/voices/ch1/knife/hero/k_h_60a.flac"
                show fury chain stabbed glare onlayer inyourface at Position(ypos=1125) with dissolve
                hero "I thought we had the upper hand, but it's as if she's barely even threatened by us.\n"
                #hero "Do you hear the conviction in her voice? Do you see that razor sharpness in her gaze? I thought we had the upper hand, but it's as if she's barely even threatened by us.\n"
                voice "audio/voices/ch1/knife/narrator/knife_n_176.flac"
                n "It's an act. She's unarmed and there's nothing she can do to hurt you.\n"
                voice "audio/voices/ch1/knife/hero/k_h_61.flac"
                hero "I'm not so sure...\n"
                voice "audio/voices/ch1/knife/narrator/knife_n_177.flac"
                n "Don't waver now.\n"
                voice "audio/voices/ch1/knife/narrator/knife_n_177b.flac"
                play audio "audio/one_shot/collapse.flac"
                hide fury onlayer inyourface
                hide bg onlayer back
                hide midground onlayer front
                show bg black onlayer back at Position(ypos=1125)
                with dissolve
                n "As you raise your blade to strike again, she kicks out, knocking your legs out from under you.\n"
                play audio "audio/one_shot/punch_many_knife.flac"
                voice "audio/voices/ch1/knife/narrator/knife_n_178.flac"
                hide bg onlayer back
                show bg generic dark onlayer back at Position(ypos=1125)
                show battle fury chain stabbed onlayer front at Position(ypos=1125)
                #show battle1 fury chain stabbed onlayer front at Position(ypos=1125)
                #show battle2 fury chain stabbed onlayer front at Position(ypos=1125)
                #show battle3 fury chain stabbed onlayer front at Position(ypos=1125)
                with Dissolve(0.75)
                n "The two of you struggle on the ground. You lash out with the blade, slicing wherever you can. Her fists connect with your body again and again, each blow stronger than the last, shattering bone and rupturing tissue with reckless abandon.\n"
                voice "audio/voices/ch1/knife/hero/k_h_62.flac"
                hero "Forget trying to rescue her. This is about {i}survival{/i} now. Give her everything you've got.\n"
                menu:
                    extend ""

                    "{i}• [[Slay the Princess.]{/i}":
                        play audio "audio/one_shot/collapse.flac"
                        voice "audio/voices/ch1/knife/narrator/knife_n_180.flac"
                        hide bg onlayer back
                        hide battle onlayer front
                        show bg fury stub betrayed distant onlayer farback at Position(ypos=1125)
                        show fury stabbed distant stare onlayer back at Position(ypos=1125)
                        show player bloody knife onlayer inyourface at Position(ypos=1125)
                        with Dissolve(0.75)
                        n "You roll out of her grasp and shakily push yourself back to your feet.\n"
                        voice "audio/voices/ch1/knife/narrator/knife_n_179.flac"
                        play audio "audio/one_shot/blood_drip.flac"
                        n "Though every inch of you is in pain, the Princess probably has it worse— blood pours out from countless gashes, staining her once pristine dress. She pauses for a moment, catching her breath, staring at you with wild eyes.\n"
                        voice "audio/voices/ch1/knife/hero/k_h_63.flac"
                        hero "We can still turn this around.\n"
                        $ config.menu_include_disabled = True
                        menu:
                            extend ""

                            "{i}• [[Give up.]{/i}" if tower_encountered == False:
                                $ tower_pathetic = True
                                $ current_princess = "tower"
                                $ blade_held = False
                                $ default_mouse = "default"
                                $ config.menu_include_disabled = False
                                play audio "audio/one_shot/knife_bounce_several.flac"
                                voice "audio/voices/ch1/knife/narrator/knife_n_181.flac"
                                hide bg onlayer farback
                                hide fury onlayer back
                                hide player onlayer inyourface
                                show bg generic dark onlayer back at Position(ypos=1125)
                                show knife dropped onlayer inyourface at Position(ypos=1125)
                                with dissolve
                                n "Are you serious? {i}Sigh{/i}. As the force of her blows overwhelms your body, the blade falls from your trembling hands, clattering uselessly to the cobblestones below. I suppose you just lacked the will to finish the job.\n"
                                #n "Are you serious? {i}Sigh{/i}. As the force of her blows overwhelms your body, the blade falls from your trembling hands, clattering uselessly to the cobblestones below. I suppose you just lacked the will to finish the job.\n"
                                voice "audio/voices/ch1/knife/narrator/knife_n_182.flac"
                                hide bg onlayer back
                                hide knife onlayer inyourface
                                show bg fury stub betrayed loom onlayer back at Position(ypos=1125)
                                show fury chain stabbed loom onlayer front at Position(ypos=1125)
                                with dissolve
                                n "The Princess, wounded, but still alive, stands to face you.\n"
                                play audio "audio/one_shot/thump.flac"
                                voice "audio/voices/ch1/knife/narrator/knife_n_183.flac"
                                show fury chain stabbed foot onlayer front at Position(ypos=1125) with dissolve
                                n "She places a confident heel on your chest, and pushes you to the ground.\n"
                                play audio "audio/one_shot/knee_kill.flac"
                                voice "audio/voices/ch1/knife/narrator/knife_n_183b.flac"
                                show fury chain stabbed kneel onlayer front with dissolve
                                n "Her knee slides to your throat and your windpipe is crushed under weight you didn't think her frame could possibly possess.\n"
                                voice "audio/voices/ch1/knife/princess/stab_p_100.flac"
                                show fury chain stabbed kneel talk onlayer front with dissolve
                                sp "Pathetic.\n"
                                show fury chain stabbed kneel onlayer front with dissolve
                                voice "audio/voices/ch1/knife/hero/k_h_64.flac"
                                hero "This is the end, isn't it?\n"
                                $ persistent.death_count += 1
                                voice "audio/voices/ch1/knife/narrator/knife_n_184.flac"
                                $ quick_menu = False
                                stop music fadeout 1.0
                                stop sound fadeout 1.0
                                hide bg onlayer back
                                hide fury onlayer front
                                show bg black onlayer back at Position(ypos=1125)
                                with dissolve
                                n "Everything goes dark, and you die.\n"
                                hide bg black onlayer back with dissolve
                                jump start_2

                            "{i}• [[Finish the job.]{/i}" if adversary_encountered == False:
                                $ loop_1_princess_killed = True
                                $ config.menu_include_disabled = False
                                $ current_princess = "adversary"
                                voice "audio/voices/ch1/knife/narrator/knife_n_185.flac"
                                n "You steel your resolve and take another step towards the Princess. You probably won't make it out of here alive, but you can at least make sure she won't make it out of here, either.\n"
                                voice "audio/voices/ch1/knife/hero/k_h_65.flac"
                                hero "Excuse me? What was that about not making it out of here alive?\n"
                                voice "audio/voices/ch1/knife/narrator/knife_n_186.flac"
                                n "Do you think this is what I wanted to happen? I have a duty to state the facts of the situation, and honestly, it's a miracle {i}anyone{/i} is still standing right now.\n"
                                voice "audio/voices/ch1/knife/narrator/knife_n_187.flac"
                                n "Can you not feel all those ruptured organs bouncing around in there? If the Princess doesn't do our friend in herself, internal bleeding is certain to finish the job.\n"
                                voice "audio/voices/ch1/knife/narrator/knife_n_56.flac"
                                $ default_mouse = "default"
                                play audio "audio/one_shot/punch_stab.flac"
                                hide bg onlayer farback
                                hide fury onlayer back
                                hide player onlayer inyourface
                                show bg generic dark onlayer back at Position(ypos=1125)
                                show finale fury chain stabbed onlayer front at Position(ypos=1125)
                                #show finale1 fury chain stabbed onlayer front at Position(ypos=1125)
                                #show finale2 fury chain stabbed onlayer front at Position(ypos=1125)
                                with Dissolve(0.75)
                                n "The two of you clash for the final time. You feel your ribs break as she delivers a heavy blow, but you push through the pain, falling forward and sinking your blade deep into the Princess' heart.\n"
                                voice "audio/voices/ch1/knife/princess/stab_p_101.flac"
                                hide bg onlayer back
                                hide finale onlayer front
                                show bg generic onlayer farback at Position(ypos=1125)
                                show fury chain stabbed dying onlayer front at Position(ypos=1125)
                                with dissolve
                                sp "O... oh.\n"
                                play audio "audio/one_shot/collapse.flac"
                                play secondary "audio/one_shot/knife_bounce_several.flac"
                                voice "audio/voices/ch1/knife/narrator/knife_n_189.flac"
                                $ blade_held = False
                                $ default_mouse = "default"
                                show bg fury chained stabbed dying talk onlayer farback at Position(ypos=1125)
                                show fury chain stabbed dying talk onlayer front at Position(ypos=1125)
                                with dissolve
                                n "The two of you fall to the floor.\n"
                                voice "audio/voices/ch1/knife/princess/stab_p_102.flac"
                                sp "This was fun. You put up more of a fight than I thought you would.\nBut I have to wonder...\n"
                                voice "audio/voices/ch1/knife/princess/stab_p_103.flac"
                                sp "Do you {i}really{/i} think this is the end?\n"
                                #voice "audio/voices/ch1/knife/hero/k_h_66.flac"
                                show fury chain stabbed dead onlayer front with dissolve
                                #hero "There it is again, that razor-sharp look in her eyes and the terrifying conviction in her words.\n"
                                voice "audio/voices/ch1/knife/narrator/knife_n_190.flac"
                                n "But you don't have the time to worry over her words.\n"
                                $ persistent.death_count += 1
                                voice "audio/voices/ch1/knife/narrator/knife_n_30.flac"
                                $ quick_menu = False
                                stop music fadeout 1.0
                                stop sound fadeout 1.0
                                hide bg onlayer farback
                                hide fury onlayer front
                                show bg black onlayer back at Position(ypos=1125)
                                with dissolve
                                n "Everything goes dark, and you die.\n"
                                hide bg black onlayer back with dissolve
                                jump start_2

                            "{i}• [[Run for the stairs and lock her in the basement. Maybe she'll bleed out.]{/i}" if nightmare_encountered == False:
                                $ nightmare_join_fled = True
                                $ current_princess = "nightmare"
                                voice "audio/voices/ch1/knife/narrator/knife_n_192.flac"
                                n "The Princess is still chained to the wall. There's nothing she can do to stop you from getting out of here.\n"
                                voice "audio/voices/ch1/knife/hero/k_h_67.flac"
                                hero "What if she doesn't succumb to her wounds? Whatever she is, she's {i}so{/i} much more dangerous than I thought she'd be.\n"
                                voice "audio/voices/ch1/empty/narrator/empty_n_113.flac"
                                play audio "audio/one_shot/footstep_run_medium.flac"
                                $ quick_menu = False
                                hide bg onlayer farback
                                hide fury onlayer back
                                hide player onlayer inyourface
                                show basement stairs open onlayer front at Position(ypos=1125)
                                with fade
                                if persistent.quick_menu:
                                    $ quick_menu = True
                                n "You rush up the stairs and dive past the threshold. You're safe. For now.\n"
                                $ quick_menu = False
                                hide basement onlayer front
                                scene bg black
                                with fade
                                jump nightmare_join

return
