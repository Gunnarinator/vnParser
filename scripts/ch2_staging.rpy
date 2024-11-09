label start_2:
    stop music
    stop sound
    stop secondary
    $ default_mouse = "default"
    $ blade_held = False
    $ current_loop = 2
    $ quick_menu = False
    $ config.menu_include_disabled = False

    if current_princess == "adversary":
        $ adversary_encountered = True
        jump adversary_1_start

    elif current_princess == "beast":
        $ beast_encountered = True
        jump beast_1_start

    elif current_princess == "damsel":
        $ damsel_encountered = True
        jump damsel_1_start

    elif current_princess == "nightmare":
        $ nightmare_encountered = True
        jump nightmare_1_start

    elif current_princess == "prisoner":
        $ prisoner_encountered = True
        jump prisoner_1_start

    elif current_princess == "razor":
        $ razor_encountered = True
        jump razor_1_start

    elif current_princess == "spectre":
        $ spectre_encountered = True
        jump spectre_1_start

    elif current_princess == "stranger":
        $ stranger_encountered = True
        jump stranger_1_start

    elif current_princess == "tower":
        $ tower_encountered = True
        jump tower_1_start

    elif current_princess == "witch":
        $ witch_encountered = True
        jump witch_1_start

    else:
        $ stranger_encountered = True
        jump stranger_1_start

label chapter_2_stranger_rejoin_1:
    if current_princess == "adversary":
        jump adversary_1_cabin_arrival

    elif current_princess == "beast":
        jump beast_1_cabin_arrival

    elif current_princess == "damsel":
        jump damsel_1_cabin_arrival

    elif current_princess == "nightmare":
        jump nightmare_1_cabin_arrival

    elif current_princess == "prisoner":
        jump prisoner_1_cabin_arrival

    elif current_princess == "razor":
        jump razor_1_cabin_arrival

    elif current_princess == "spectre":
        jump spectre_1_cabin_arrival

    elif current_princess == "tower":
        jump tower_1_cabin_arrival

    elif current_princess == "witch":
        jump witch_1_cabin_arrival

    else:
        jump prisoner_1_cabin_arrival

label chapter_2_stranger_rejoin:
    if current_princess == "adversary":
        jump adversary_stranger_rejoin

    elif current_princess == "beast":
        jump beast_stranger_rejoin

    elif current_princess == "damsel":
        jump damsel_stranger_rejoin

    elif current_princess == "nightmare":
        jump nightmare_stranger_rejoin

    elif current_princess == "prisoner":
        jump prisoner_stranger_rejoin

    elif current_princess == "razor":
        jump razor_stranger_rejoin

    elif current_princess == "spectre":
        jump spectre_stranger_rejoin

    elif current_princess == "tower":
        jump tower_stranger_rejoin

    elif current_princess == "witch":
        jump witch_stranger_rejoin


return
