label dragon_art_staging:

    # ROUTE START

    image bg dragon generic = ConditionSwitch("persistent.performance_mode == True", "bg dragon generic p", "persistent.performance_mode == False", At("bg dragon generic p", distortion))

    image bg dragon start = ConditionSwitch("persistent.performance_mode == True", "dragon start bg p", "persistent.performance_mode == False", At("dragon start bg p", distortion))
    image arms dragon start 1 = ConditionSwitch("persistent.performance_mode == True", "dragon start flee arms 1 p", "persistent.performance_mode == False", At("dragon start flee arms 1 p", distortion))
    image arms dragon start 2 = ConditionSwitch("persistent.performance_mode == True", "dragon start flee arms 2 p", "persistent.performance_mode == False", At("dragon start flee arms 2 p", distortion))
    image arms dragon start 3 = ConditionSwitch("persistent.performance_mode == True", "dragon start flee arms 3 p", "persistent.performance_mode == False", At("dragon start flee arms 3 p", distortion))
    image arms dragon start 4 = ConditionSwitch("persistent.performance_mode == True", "dragon start flee arms 4 p", "persistent.performance_mode == False", At("dragon start flee arms 4 p", distortion))
    image bg dragon start downstairs 1 = ConditionSwitch("persistent.performance_mode == True", "dragon start flee downstairs 1 p", "persistent.performance_mode == False", At("dragon start flee downstairs 1 p", distortion))
    image bg dragon start downstairs 2 = ConditionSwitch("persistent.performance_mode == True", "dragon start flee downstairs 2 p", "persistent.performance_mode == False", At("dragon start flee downstairs 2 p", distortion))
    image bg dragon start downstairs 3 = ConditionSwitch("persistent.performance_mode == True", "dragon start flee downstairs 3 p", "persistent.performance_mode == False", At("dragon start flee downstairs 3 p", distortion))
    image bg dragon start downstairs 4 = ConditionSwitch("persistent.performance_mode == True", "dragon start flee downstairs 4 p", "persistent.performance_mode == False", At("dragon start flee downstairs 4 p", distortion))
    image bg dragon start upstairs 1 = ConditionSwitch("persistent.performance_mode == True", "dragon start flee upstairs 1 p", "persistent.performance_mode == False", At("dragon start flee upstairs 1 p", distortion))
    image bg dragon start upstairs 2 = ConditionSwitch("persistent.performance_mode == True", "dragon start flee upstairs 2 p", "persistent.performance_mode == False", At("dragon start flee upstairs 2 p", distortion))
    image bg dragon start upstairs 3 = ConditionSwitch("persistent.performance_mode == True", "dragon start flee upstairs 3 p", "persistent.performance_mode == False", At("dragon start flee upstairs 3 p", distortion))
    image bg dragon start upstairs 4 = ConditionSwitch("persistent.performance_mode == True", "dragon start flee upstairs 4 p", "persistent.performance_mode == False", At("dragon start flee upstairs 4 p", distortion))
    image dragon start twitch = ConditionSwitch("persistent.performance_mode == True", "dragon start twitch p", "persistent.performance_mode == False", At("dragon start twitch p", distortion))
    image dragon start = ConditionSwitch("persistent.performance_mode == True", "dragon start p", "persistent.performance_mode == False", At("dragon start p", distortion))

    # basic bg

    image bg dragon true start = ConditionSwitch("persistent.performance_mode == True", "bg dragon true start p", "persistent.performance_mode == False", At("bg dragon true start p", distortion))

    # HANDS FLICKERING

    image bg dragon hands flicker = ConditionSwitch("persistent.flickering == True", "bg dragon hands flicker anim", "persistent.flickering == False", "bg dragon hands flicker2")

    image dragon hands flicker = ConditionSwitch("persistent.flickering == True", "dragon hands flicker anim", "persistent.flickering == False", "dragon hands flicker2")

    image bg dragon hands flicker anim:
        "bg dragon hands flicker1"
        0.1
        "bg dragon hands flicker2"
        0.05
        "bg dragon hands flicker1"
        0.12
        "bg dragon hands flicker2"
        0.14
        "bg dragon hands flicker1"
        0.09
        "bg dragon hands flicker2"
        0.05
        "bg dragon hands flicker1"
        0.2
        "bg dragon hands flicker2"
        0.1
        "bg dragon hands flicker1"
        0.23
        "bg dragon hands flicker2"
        0.1234
        "bg dragon hands flicker1"
        0.15
        "bg dragon hands flicker2"
        0.3
        "bg dragon hands flicker1"
        0.36
        "bg dragon hands flicker2"
        0.1
        "bg dragon hands flicker1"
        0.05
        "bg dragon hands flicker2"
        0.08
        "bg dragon hands flicker1"
        0.6
        "bg dragon hands flicker2"
        0.35
        repeat

    image dragon hands flicker anim:
        "dragon hands flicker1"
        0.125
        "dragon hands flicker2"
        0.2
        "dragon hands flicker1"
        0.1067
        "dragon hands flicker2"
        0.123
        "dragon hands flicker1"
        0.16
        "dragon hands flicker2"
        0.27
        "dragon hands flicker1"
        0.48
        "dragon hands flicker2"
        0.09
        "dragon hands flicker1"
        0.07
        "dragon hands flicker2"
        0.02
        "dragon hands flicker1"
        0.03
        "dragon hands flicker2"
        0.04
        "dragon hands flicker1"
        0.125
        "dragon hands flicker2"
        0.156
        "dragon hands flicker1"
        0.07
        "dragon hands flicker2"
        0.223
        "dragon hands flicker1"
        0.04
        "dragon hands flicker2"
        0.268
        "dragon hands flicker1"
        0.14
        "dragon hands flicker2"
        0.08
        repeat

    image bg dragon hands flicker1 = ConditionSwitch("persistent.performance_mode == True", "cg dragon hands flicker bg p", "persistent.performance_mode == False", At("cg dragon hands flicker bg p", distortion))
    image bg dragon hands flicker2 = ConditionSwitch("persistent.performance_mode == True", "cg dragon hands flicker bg2 p", "persistent.performance_mode == False", At("cg dragon hands flicker bg2 p", distortion))
    image dragon hands flicker1 = ConditionSwitch("persistent.performance_mode == True", "cg dragon hands flicker p", "persistent.performance_mode == False", At("cg dragon hands flicker p", distortion))
    image dragon hands flicker2 = ConditionSwitch("persistent.performance_mode == True", "cg dragon hands flicker2 p", "persistent.performance_mode == False", At("cg dragon hands flicker2 p", distortion))



    image bg dragon leave alone = ConditionSwitch("persistent.performance_mode == True", "bg dragon leave alone p", "persistent.performance_mode == False", At("bg dragon leave alone p", distortion))

    image feathers dragon attack = ConditionSwitch("persistent.performance_mode == True", "cg dragon attack feathers p", "persistent.performance_mode == False", At("cg dragon attack feathers p", distortion))
    image arms dragon attack = ConditionSwitch("persistent.performance_mode == True", "cg dragon attack arms p", "persistent.performance_mode == False", At("cg dragon attack arms p", distortion))

    image cg dragon attack cold talk = ConditionSwitch("persistent.performance_mode == True", "cg dragon attack cold talk p", "persistent.performance_mode == False", At("cg dragon attack cold talk p", distortion))
    image cg dragon attack cold = ConditionSwitch("persistent.performance_mode == True", "cg dragon attack cold p", "persistent.performance_mode == False", At("cg dragon attack cold p", distortion))
    image cg dragon attack hero talk = ConditionSwitch("persistent.performance_mode == True", "cg dragon attack hero talk p", "persistent.performance_mode == False", At("cg dragon attack hero talk p", distortion))
    image cg dragon attack hero = ConditionSwitch("persistent.performance_mode == True", "cg dragon attack hero p", "persistent.performance_mode == False", At("cg dragon attack hero p", distortion))
    image cg dragon attack opp talk = ConditionSwitch("persistent.performance_mode == True", "cg dragon attack opp talk p", "persistent.performance_mode == False", At("cg dragon attack opp talk p", distortion))
    image cg dragon attack opp = ConditionSwitch("persistent.performance_mode == True", "cg dragon attack opp p", "persistent.performance_mode == False", At("cg dragon attack opp p", distortion))


    image cg dragon free cold talk = ConditionSwitch("persistent.performance_mode == True", "cg dragon free cold talk p", "persistent.performance_mode == False", At("cg dragon free cold talk p", distortion))
    image farback dragon free = ConditionSwitch("persistent.performance_mode == True", "cg dragon free stars p", "persistent.performance_mode == False", At("cg dragon free stars p", distortion))
    image cg dragon free talk = ConditionSwitch("persistent.performance_mode == True", "cg dragon free talk p", "persistent.performance_mode == False", At("cg dragon free talk p", distortion))
    image cg dragon free = ConditionSwitch("persistent.performance_mode == True", "cg dragon free p", "persistent.performance_mode == False", At("cg dragon free p", distortion))





    image farback dragon leave basement = ConditionSwitch("persistent.performance_mode == True", "cg dragon leave basement bg p", "persistent.performance_mode == False", At("cg dragon leave basement bg p", distortion))
    image cg dragon leave basement = ConditionSwitch("persistent.performance_mode == True", "cg dragon leave basement p", "persistent.performance_mode == False", At("cg dragon leave basement p", distortion))

    image bg dragon leave door = ConditionSwitch("persistent.performance_mode == True", "cg dragon leave door bg p", "persistent.performance_mode == False", At("cg dragon leave door bg p", distortion))
    image cg dragon leave door hostile talk arm = ConditionSwitch("persistent.performance_mode == True", "cg dragon leave door hostile talk arm p", "persistent.performance_mode == False", At("cg dragon leave door hostile talk arm p", distortion))
    image cg dragon leave door hostile talk = ConditionSwitch("persistent.performance_mode == True", "cg dragon leave door hostile talk p", "persistent.performance_mode == False", At("cg dragon leave door hostile talk p", distortion))
    image cg dragon leave door hostile = ConditionSwitch("persistent.performance_mode == True", "cg dragon leave door hostile p", "persistent.performance_mode == False", At("cg dragon leave door hostile p", distortion))
    image cg dragon leave door neutral talk arm = ConditionSwitch("persistent.performance_mode == True", "cg dragon leave door neutral talk arm p", "persistent.performance_mode == False", At("cg dragon leave door neutral talk arm p", distortion))
    image cg dragon leave door neutral talk = ConditionSwitch("persistent.performance_mode == True", "cg dragon leave door neutral talk p", "persistent.performance_mode == False", At("cg dragon leave door neutral talk p", distortion))
    image cg dragon leave door neutral = ConditionSwitch("persistent.performance_mode == True", "cg dragon leave door neutral p", "persistent.performance_mode == False", At("cg dragon leave door neutral p", distortion))
    image hands dragon post harsh charge = ConditionSwitch("persistent.performance_mode == True", "cg dragon post harsh charge hands p", "persistent.performance_mode == False", At("cg dragon post harsh charge hands p", distortion))
    image cg dragon post harsh charge = ConditionSwitch("persistent.performance_mode == True", "cg dragon post harsh charge p", "persistent.performance_mode == False", At("cg dragon post harsh charge p", distortion))
    image cg dragon post harsh drive talk = ConditionSwitch("persistent.performance_mode == True", "cg dragon post harsh drive talk p", "persistent.performance_mode == False", At("cg dragon post harsh drive talk p", distortion))
    image cg dragon post harsh drive = ConditionSwitch("persistent.performance_mode == True", "cg dragon post harsh drive p", "persistent.performance_mode == False", At("cg dragon post harsh drive p", distortion))
    image cg dragon post harsh stabbed = ConditionSwitch("persistent.performance_mode == True", "cg dragon post harsh stabbed p", "persistent.performance_mode == False", At("cg dragon post harsh stabbed p", distortion))

    image hands dragon post stabbed harsh = ConditionSwitch("persistent.performance_mode == True", "cg dragon post stabbed harsh start hands p", "persistent.performance_mode == False", At("cg dragon post stabbed harsh start hands p", distortion))
    image farback dragon post stabbed harsh = ConditionSwitch("persistent.performance_mode == True", "cg dragon post stabbed harsh start stars p", "persistent.performance_mode == False", At("cg dragon post stabbed harsh start stars p", distortion))
    image cg dragon post stabbed harsh = ConditionSwitch("persistent.performance_mode == True", "cg dragon post stabbed harsh start p", "persistent.performance_mode == False", At("cg dragon post stabbed harsh start p", distortion))


    image panel1 dragon post stabbed harsh yank = ConditionSwitch("persistent.performance_mode == True", "cg dragon post stabbed harsh yank 1 p", "persistent.performance_mode == False", At("cg dragon post stabbed harsh yank 1 p", distortion))

    image panel2 dragon post stabbed harsh yank:
        "emptyimage"
        3.3
        "panel2 dragon post stabbed harsh yank base"

    image panel2 dragon post stabbed harsh yank base = ConditionSwitch("persistent.performance_mode == True", "cg dragon post stabbed harsh yank 2 p", "persistent.performance_mode == False", At("cg dragon post stabbed harsh yank 2 p", distortion))

    image cg dragon soft oops cut = ConditionSwitch("persistent.performance_mode == True", "cg dragon soft oops cut p", "persistent.performance_mode == False", At("cg dragon soft oops cut p", distortion))
    image cg dragon soft oops grin = ConditionSwitch("persistent.performance_mode == True", "cg dragon soft oops grin p", "persistent.performance_mode == False", At("cg dragon soft oops grin p", distortion))
    image hands dragon soft oops stab = ConditionSwitch("persistent.performance_mode == True", "cg dragon soft oops stab hands p", "persistent.performance_mode == False", At("cg dragon soft oops stab hands p", distortion))

    image cg dragon soft oops stab = ConditionSwitch("persistent.performance_mode == True", "cg dragon soft oops stab p", "persistent.performance_mode == False", At("cg dragon soft oops stab p", distortion))
    image cg dragon soft oops switch = ConditionSwitch("persistent.performance_mode == True", "cg dragon soft oops switch p", "persistent.performance_mode == False", At("cg dragon soft oops switch p", distortion))

    image cg dragon soft switch stab event = ConditionSwitch("persistent.performance_mode == True", "cg dragon soft switch stab event p", "persistent.performance_mode == False", At("cg dragon soft switch stab event p", distortion))
    image cg dragon soft switch stab talk = ConditionSwitch("persistent.performance_mode == True", "cg dragon soft switch stab talk p", "persistent.performance_mode == False", At("cg dragon soft switch stab talk p", distortion))
    image cg dragon soft switch stab = ConditionSwitch("persistent.performance_mode == True", "cg dragon soft switch stab p", "persistent.performance_mode == False", At("cg dragon soft switch stab p", distortion))
    image player switch dragon soft aback = ConditionSwitch("persistent.performance_mode == True", "cg switch dragon soft player aback p", "persistent.performance_mode == False", At("cg switch dragon soft player aback p", distortion))
    image player switch dragon soft = ConditionSwitch("persistent.performance_mode == True", "cg switch dragon soft player p", "persistent.performance_mode == False", At("cg switch dragon soft player p", distortion))


    image bg switch dragon soft = ConditionSwitch("persistent.performance_mode == True", "cg switch dragon soft p", "persistent.performance_mode == False", At("cg switch dragon soft p", distortion))

    image bg dragon join sequence = ConditionSwitch("persistent.performance_mode == True", "dragon join sequence 1 bg p", "persistent.performance_mode == False", At("dragon join sequence 1 bg p", distortion))


    image invplay dragon join sequence 1 = ConditionSwitch("persistent.performance_mode == True", "dragon join sequence 1 player p", "persistent.performance_mode == False", At("dragon join sequence 1 player p", distortion))
    image invp dragon join sequence 1 talk = ConditionSwitch("persistent.performance_mode == True", "dragon join sequence 1 princess talk p", "persistent.performance_mode == False", At("dragon join sequence 1 princess talk p", distortion))
    image princess dragon join sequence 1 = ConditionSwitch("persistent.performance_mode == True", "dragon join sequence 1 princess p", "persistent.performance_mode == False", At("dragon join sequence 1 princess p", distortion))
    image player dragon join sequence 2 = ConditionSwitch("persistent.performance_mode == True", "dragon join sequence 2 player inverse p", "persistent.performance_mode == False", At("dragon join sequence 2 player inverse p", distortion))
    image invplay dragon join sequence 2 = ConditionSwitch("persistent.performance_mode == True", "dragon join sequence 2 player p", "persistent.performance_mode == False", At("dragon join sequence 2 player p", distortion))
    image invp dragon join sequence 2 = ConditionSwitch("persistent.performance_mode == True", "dragon join sequence 2 princess inverse p", "persistent.performance_mode == False", At("dragon join sequence 2 princess inverse p", distortion))
    image princess dragon join sequence 2 = ConditionSwitch("persistent.performance_mode == True", "dragon join sequence 2 princess p", "persistent.performance_mode == False", At("dragon join sequence 2 princess p", distortion))
    image invp dragon join sequence 2 talk = ConditionSwitch("persistent.performance_mode == True", "dragon join sequence 2 talk princess inverse p", "persistent.performance_mode == False", At("dragon join sequence 2 talk princess inverse p", distortion))
    image princess dragon join sequence 2 talk = ConditionSwitch("persistent.performance_mode == True", "dragon join sequence 2 talk princess p", "persistent.performance_mode == False", At("dragon join sequence 2 talk princess p", distortion))
    image player dragon join sequence final = ConditionSwitch("persistent.performance_mode == True", "dragon join sequence final player inverse p", "persistent.performance_mode == False", At("dragon join sequence final player inverse p", distortion))
    image invplay dragon join sequence final = ConditionSwitch("persistent.performance_mode == True", "dragon join sequence final player p", "persistent.performance_mode == False", At("dragon join sequence final player p", distortion))
    image invp dragon join sequence final stub = ConditionSwitch("persistent.performance_mode == True", "dragon join sequence final princess inverse stub p", "persistent.performance_mode == False", At("dragon join sequence final princess inverse stub p", distortion))
    image invp dragon join sequence final = ConditionSwitch("persistent.performance_mode == True", "dragon join sequence final princess inverse p", "persistent.performance_mode == False", At("dragon join sequence final princess inverse p", distortion))
    image princess dragon join sequence final stub = ConditionSwitch("persistent.performance_mode == True", "dragon join sequence final princess stub p", "persistent.performance_mode == False", At("dragon join sequence final princess stub p", distortion))
    image princess dragon join sequence final = ConditionSwitch("persistent.performance_mode == True", "dragon join sequence final princess p", "persistent.performance_mode == False", At("dragon join sequence final princess p", distortion))
    image invplay dragon join sequence penultimate = ConditionSwitch("persistent.performance_mode == True", "dragon join sequence penultimate player inverse p", "persistent.performance_mode == False", At("dragon join sequence penultimate player inverse p", distortion))
    image player dragon join sequence penultimate = ConditionSwitch("persistent.performance_mode == True", "dragon join sequence penultimate player p", "persistent.performance_mode == False", At("dragon join sequence penultimate player p", distortion))
    image invp dragon join sequence penultimate talk = ConditionSwitch("persistent.performance_mode == True", "dragon join sequence penultimate princess inverse talk p", "persistent.performance_mode == False", At("dragon join sequence penultimate princess inverse talk p", distortion))
    image invp dragon join sequence penultimate = ConditionSwitch("persistent.performance_mode == True", "dragon join sequence penultimate princess inverse p", "persistent.performance_mode == False", At("dragon join sequence penultimate princess inverse p", distortion))
    image princess join sequence penultimate talk = ConditionSwitch("persistent.performance_mode == True", "dragon join sequence penultimate princess talk p", "persistent.performance_mode == False", At("dragon join sequence penultimate princess talk p", distortion))
    image princess dragon join sequence penultimate = ConditionSwitch("persistent.performance_mode == True", "dragon join sequence penultimate princess p", "persistent.performance_mode == False", At("dragon join sequence penultimate princess p", distortion))


    image invplay dragon join sequence 1 flick = ConditionSwitch("persistent.flickering == True", At("invplay dragon join sequence 1", alpha_dragon_delay), "persistent.flickering == False", At("invplay dragon join sequence 1", alpha_dragon_safe))
    image invp dragon join sequence 1 talk flick = ConditionSwitch("persistent.flickering == True", At("invp dragon join sequence 1 talk", alpha_dragon_delay), "persistent.flickering == False", At("invp dragon join sequence 1 talk", alpha_dragon_safe))
    image princess dragon join sequence 1 flick = ConditionSwitch("persistent.flickering == True", At("princess dragon join sequence 1", alpha_dragon), "persistent.flickering == False", At("princess dragon join sequence 1", alpha_dragon_safe))
    image player dragon join sequence 2 flick = ConditionSwitch("persistent.flickering == True", At("player dragon join sequence 2", alpha_dragon), "persistent.flickering == False", At("player dragon join sequence 2", alpha_dragon_safe))
    image invplay dragon join sequence 2 flick = ConditionSwitch("persistent.flickering == True", At("invplay dragon join sequence 2", alpha_dragon_delay), "persistent.flickering == False", At("invplay dragon join sequence 2", alpha_dragon_safe))
    image invp dragon join sequence 2 flick = ConditionSwitch("persistent.flickering == True", At("invp dragon join sequence 2", alpha_dragon_delay), "persistent.flickering == False", At("invp dragon join sequence 2", alpha_dragon_safe))
    image princess dragon join sequence 2 flick = ConditionSwitch("persistent.flickering == True", At("princess dragon join sequence 2", alpha_dragon), "persistent.flickering == False", At("princess dragon join sequence 2", alpha_dragon_safe))
    image invp dragon join sequence 2 talk flick = ConditionSwitch("persistent.flickering == True", At("invp dragon join sequence 2 talk", alpha_dragon_delay), "persistent.flickering == False", At("invp dragon join sequence 2 talk", alpha_dragon_safe))
    image princess dragon join sequence 2 talk flick = ConditionSwitch("persistent.flickering == True", At("princess dragon join sequence 2 talk", alpha_dragon), "persistent.flickering == False", At("princess dragon join sequence 2 talk", alpha_dragon_safe))
    image player dragon join sequence final flick = ConditionSwitch("persistent.flickering == True", At("player dragon join sequence final", alpha_dragon), "persistent.flickering == False", At("player dragon join sequence final", alpha_dragon_safe))
    image invplay dragon join sequence final flick = ConditionSwitch("persistent.flickering == True", At("invplay dragon join sequence final", alpha_dragon_delay), "persistent.flickering == False", At("invplay dragon join sequence final", alpha_dragon_safe))
    image invp dragon join sequence final stub flick = ConditionSwitch("persistent.flickering == True", At("invp dragon join sequence final stub", alpha_dragon_delay), "persistent.flickering == False", At("invp dragon join sequence final stub", alpha_dragon_safe))
    image invp dragon join sequence final flick = ConditionSwitch("persistent.flickering == True", At("invp dragon join sequence final", alpha_dragon_delay), "persistent.flickering == False", At("invp dragon join sequence final", alpha_dragon_safe))
    image princess dragon join sequence final stub flick = ConditionSwitch("persistent.flickering == True", At("princess dragon join sequence final stub", alpha_dragon), "persistent.flickering == False", At("princess dragon join sequence final stub", alpha_dragon_safe))
    image princess dragon join sequence final flick = ConditionSwitch("persistent.flickering == True", At("princess dragon join sequence final", alpha_dragon), "persistent.flickering == False", At("princess dragon join sequence final", alpha_dragon_safe))
    image invplay dragon join sequence penultimate flick = ConditionSwitch("persistent.flickering == True", At("invplay dragon join sequence penultimate", alpha_dragon_delay), "persistent.flickering == False", At("invplay dragon join sequence penultimate", alpha_dragon_safe))
    image player dragon join sequence penultimate flick = ConditionSwitch("persistent.flickering == True", At("player dragon join sequence penultimate", alpha_dragon), "persistent.flickering == False", At("player dragon join sequence penultimate", alpha_dragon_safe))
    image invp dragon join sequence penultimate talk flick = ConditionSwitch("persistent.flickering == True", At("invp dragon join sequence penultimate talk", alpha_dragon_delay), "persistent.flickering == False", At("invp dragon join sequence penultimate talk", alpha_dragon_safe))
    image invp dragon join sequence penultimate flick = ConditionSwitch("persistent.flickering == True", At("invp dragon join sequence penultimate", alpha_dragon_delay), "persistent.flickering == False", At("invp dragon join sequence penultimate", alpha_dragon_safe))
    image princess join sequence penultimate talk flick = ConditionSwitch("persistent.flickering == True", At("princess join sequence penultimate talk", alpha_dragon), "persistent.flickering == False", At("princess join sequence penultimate talk", alpha_dragon_safe))
    image princess dragon join sequence penultimate flick = ConditionSwitch("persistent.flickering == True", At("princess dragon join sequence penultimate", alpha_dragon), "persistent.flickering == False", At("princess dragon join sequence penultimate", alpha_dragon_safe))

    image cg dragon post harsh drive talk flick = ConditionSwitch("persistent.flickering == True", At("cg dragon post harsh drive talk", alpha_dragon), "persistent.flickering == False", At("cg dragon post harsh drive talk", alpha_dragon_safe))
    image cg dragon post harsh drive flick = ConditionSwitch("persistent.flickering == True", At("cg dragon post harsh drive", alpha_dragon), "persistent.flickering == False", At("cg dragon post harsh drive", alpha_dragon_safe))






    image dragon leave hold hand = ConditionSwitch("persistent.performance_mode == True", "dragon leave hold hand p", "persistent.performance_mode == False", At("dragon leave hold hand p", distortion))

    image dragon leave hold hand talk = ConditionSwitch("persistent.performance_mode == True", "dragon leave hold hand talk p", "persistent.performance_mode == False", At("dragon leave hold hand talk p", distortion))


    image feathers dragon stabbed harsh2 = ConditionSwitch("persistent.performance_mode == True", "dragon stabbed harsh 2 feathers p", "persistent.performance_mode == False", At("dragon stabbed harsh 2 feathers p", distortion))
    image hands dragon stabbed harsh2 = ConditionSwitch("persistent.performance_mode == True", "dragon stabbed harsh 2 fist p", "persistent.performance_mode == False", At("dragon stabbed harsh 2 fist p", distortion))
    image dragon stabbed harsh2 = ConditionSwitch("persistent.performance_mode == True", "dragon stabbed harsh 2 p", "persistent.performance_mode == False", At("dragon stabbed harsh 2 p", distortion))
    image feathers dragon stabbed harsh = ConditionSwitch("persistent.performance_mode == True", "dragon stabbed harsh feathers p", "persistent.performance_mode == False", At("dragon stabbed harsh feathers p", distortion))
    image hands dragon stabbed harsh = ConditionSwitch("persistent.performance_mode == True", "dragon stabbed harsh hands p", "persistent.performance_mode == False", At("dragon stabbed harsh hands p", distortion))
    image dragon stabbed harsh = ConditionSwitch("persistent.performance_mode == True", "dragon stabbed harsh p", "persistent.performance_mode == False", At("dragon stabbed harsh p", distortion))



    image hands dragon free 1 = ConditionSwitch("persistent.performance_mode == True", "hands dragon free 1 p", "persistent.performance_mode == False", At("hands dragon free 1 p", distortion))
    image hands dragon free 2 = ConditionSwitch("persistent.performance_mode == True", "hands dragon free2 p", "persistent.performance_mode == False", At("hands dragon free2 p", distortion))
    image hands dragon free 3 = ConditionSwitch("persistent.performance_mode == True", "hands dragon free3 p", "persistent.performance_mode == False", At("hands dragon free3 p", distortion))
    image hands dragon free 4 = ConditionSwitch("persistent.performance_mode == True", "hands dragon free4 p", "persistent.performance_mode == False", At("hands dragon free4 p", distortion))
    image hands dragon free 5 = ConditionSwitch("persistent.performance_mode == True", "hands dragon free5 p", "persistent.performance_mode == False", At("hands dragon free5 p", distortion))
    image hands dragon join sequence 1 = ConditionSwitch("persistent.performance_mode == True", "hands dragon join sequence 1 p", "persistent.performance_mode == False", At("hands dragon join sequence 1 p", distortion))
    image hands dragon join sequence 2 = ConditionSwitch("persistent.performance_mode == True", "hands dragon join sequence 2 p", "persistent.performance_mode == False", At("hands dragon join sequence 2 p", distortion))
    image hands dragon join sequence 3 = ConditionSwitch("persistent.performance_mode == True", "hands dragon join sequence 3 p", "persistent.performance_mode == False", At("hands dragon join sequence 3 p", distortion))
    image hands dragon join sequence 4 = ConditionSwitch("persistent.performance_mode == True", "hands dragon join sequence 4 p", "persistent.performance_mode == False", At("hands dragon join sequence 4 p", distortion))
    image hands dragon join sequence stub 2 = ConditionSwitch("persistent.performance_mode == True", "hands dragon join sequence stub 2 p", "persistent.performance_mode == False", At("hands dragon join sequence stub 2 p", distortion))
    image hands dragon join sequence stub 3 = ConditionSwitch("persistent.performance_mode == True", "hands dragon join sequence stub 3 p", "persistent.performance_mode == False", At("hands dragon join sequence stub 3 p", distortion))
    image hands dragon join sequence stub 4 = ConditionSwitch("persistent.performance_mode == True", "hands dragon join sequence stub 4 p", "persistent.performance_mode == False", At("hands dragon join sequence stub 4 p", distortion))

    image bg dragon blade hurl = ConditionSwitch("persistent.performance_mode == True", "harsh dragon blade hurl bg p", "persistent.performance_mode == False", At("harsh dragon blade hurl bg p", distortion))
    image knife harsh dragon blade hurl 1 = ConditionSwitch("persistent.performance_mode == True", "harsh dragon blade hurl blade1 p", "persistent.performance_mode == False", At("harsh dragon blade hurl blade1 p", distortion))
    image knife harsh dragon blade hurl 2 = ConditionSwitch("persistent.performance_mode == True", "harsh dragon blade hurl blade2 p", "persistent.performance_mode == False", At("harsh dragon blade hurl blade2 p", distortion))
    image harsh dragon blade hurl princess = ConditionSwitch("persistent.performance_mode == True", "harsh dragon blade hurl princess p", "persistent.performance_mode == False", At("harsh dragon blade hurl princess p", distortion))
    image farback dragon blade hurl = ConditionSwitch("persistent.performance_mode == True", "harsh dragon blade hurl stars p", "persistent.performance_mode == False", At("harsh dragon blade hurl stars p", distortion))

    image harsh dragon charge doubt = ConditionSwitch("persistent.performance_mode == True", "harsh dragon charge doubt p", "persistent.performance_mode == False", At("harsh dragon charge doubt p", distortion))
    image harsh dragon charge fall talk = ConditionSwitch("persistent.performance_mode == True", "harsh dragon charge fall talk p", "persistent.performance_mode == False", At("harsh dragon charge fall talk p", distortion))
    image harsh dragon charge fall = ConditionSwitch("persistent.performance_mode == True", "harsh dragon charge fall p", "persistent.performance_mode == False", At("harsh dragon charge fall p", distortion))
    image harsh dragon charge raise = ConditionSwitch("persistent.performance_mode == True", "harsh dragon charge raise p", "persistent.performance_mode == False", At("harsh dragon charge raise p", distortion))
    image harsh dragon charge stare talk = ConditionSwitch("persistent.performance_mode == True", "harsh dragon charge stare talk p", "persistent.performance_mode == False", At("harsh dragon charge stare talk p", distortion))
    image harsh dragon charge stare = ConditionSwitch("persistent.performance_mode == True", "harsh dragon charge stare p", "persistent.performance_mode == False", At("harsh dragon charge stare p", distortion))
    image harsh dragon relief line talk = ConditionSwitch("persistent.performance_mode == True", "harsh dragon relief line talk p", "persistent.performance_mode == False", At("harsh dragon relief line talk p", distortion))
    image harsh dragon relief line = ConditionSwitch("persistent.performance_mode == True", "harsh dragon relief line p", "persistent.performance_mode == False", At("harsh dragon relief line p", distortion))
    image harsh dragon relief talk = ConditionSwitch("persistent.performance_mode == True", "harsh dragon relief talk p", "persistent.performance_mode == False", At("harsh dragon relief talk p", distortion))
    image harsh dragon relief = ConditionSwitch("persistent.performance_mode == True", "harsh dragon relief p", "persistent.performance_mode == False", At("harsh dragon relief p", distortion))
    image player dragon arrive 1 = ConditionSwitch("persistent.performance_mode == True", "player dragon arrive 1 p", "persistent.performance_mode == False", At("player dragon arrive 1 p", distortion))
    image player dragon arrive 2 = ConditionSwitch("persistent.performance_mode == True", "player dragon arrive 2 p", "persistent.performance_mode == False", At("player dragon arrive 2 p", distortion))
    image bg player dragon arrive = ConditionSwitch("persistent.performance_mode == True", "player dragon arrive bg p", "persistent.performance_mode == False", At("player dragon arrive bg p", distortion))
    image player dragon arrive final = ConditionSwitch("persistent.performance_mode == True", "player dragon arrive final p", "persistent.performance_mode == False", At("player dragon arrive final p", distortion))
    image player dragon cold talk = ConditionSwitch("persistent.performance_mode == True", "player dragon cold talk p", "persistent.performance_mode == False", At("player dragon cold talk p", distortion))
    image player dragon cold = ConditionSwitch("persistent.performance_mode == True", "player dragon cold p", "persistent.performance_mode == False", At("player dragon cold p", distortion))
    image player dragon hero talk = ConditionSwitch("persistent.performance_mode == True", "player dragon hero talk p", "persistent.performance_mode == False", At("player dragon hero talk p", distortion))
    image player dragon hero = ConditionSwitch("persistent.performance_mode == True", "player dragon hero p", "persistent.performance_mode == False", At("player dragon hero p", distortion))
    image player dragon kill cold talk = ConditionSwitch("persistent.performance_mode == True", "player dragon kill cold talk p", "persistent.performance_mode == False", At("player dragon kill cold talk p", distortion))
    image player dragon kill cold = ConditionSwitch("persistent.performance_mode == True", "player dragon kill cold p", "persistent.performance_mode == False", At("player dragon kill cold p", distortion))
    image player dragon kill hero neutral = ConditionSwitch("persistent.performance_mode == True", "player dragon kill hero neutral p", "persistent.performance_mode == False", At("player dragon kill hero neutral p", distortion))
    image player dragon kill hero talk = ConditionSwitch("persistent.performance_mode == True", "player dragon kill hero talk p", "persistent.performance_mode == False", At("player dragon kill hero talk p", distortion))
    image player dragon kill opportunist talk = ConditionSwitch("persistent.performance_mode == True", "player dragon kill opportunist talk p", "persistent.performance_mode == False", At("player dragon kill opportunist talk p", distortion))
    image player dragon kill opportunist = ConditionSwitch("persistent.performance_mode == True", "player dragon kill opportunist p", "persistent.performance_mode == False", At("player dragon kill opportunist p", distortion))
    image player dragon neutral = ConditionSwitch("persistent.performance_mode == True", "player dragon neutral p", "persistent.performance_mode == False", At("player dragon neutral p", distortion))

    image knife dragon dangle:
        "player dragon opp dangle hand 1"
        0.25
        "player dragon opp dangle hand 2"
        0.1
        "player dragon opp dangle hand 3"
        0.25
        "player dragon opp dangle hand 2"
        0.1
        repeat

    image player dragon opp dangle hand 1 = ConditionSwitch("persistent.performance_mode == True", "player dragon opp dangle hand 1 p", "persistent.performance_mode == False", At("player dragon opp dangle hand 1 p", distortion))
    image player dragon opp dangle hand 2 = ConditionSwitch("persistent.performance_mode == True", "player dragon opp dangle hand 2 p", "persistent.performance_mode == False", At("player dragon opp dangle hand 2 p", distortion))
    image player dragon opp dangle hand 3 = ConditionSwitch("persistent.performance_mode == True", "player dragon opp dangle hand 3 p", "persistent.performance_mode == False", At("player dragon opp dangle hand 3 p", distortion))
    image player dragon opp dangle talk = ConditionSwitch("persistent.performance_mode == True", "player dragon opp dangle talk p", "persistent.performance_mode == False", At("player dragon opp dangle talk p", distortion))
    image player dragon opp dangle = ConditionSwitch("persistent.performance_mode == True", "player dragon opp dangle p", "persistent.performance_mode == False", At("player dragon opp dangle p", distortion))
    image player dragon opp = ConditionSwitch("persistent.performance_mode == True", "player dragon opp p", "persistent.performance_mode == False", At("player dragon opp p", distortion))
    image player dragon tilt = ConditionSwitch("persistent.performance_mode == True", "player dragon tilt p", "persistent.performance_mode == False", At("player dragon tilt p", distortion))
    image prev-attack = ConditionSwitch("persistent.performance_mode == True", "prev-attack p", "persistent.performance_mode == False", At("prev-attack p", distortion))
    image prev-free = ConditionSwitch("persistent.performance_mode == True", "prev-free p", "persistent.performance_mode == False", At("prev-free p", distortion))
    image prev-player = ConditionSwitch("persistent.performance_mode == True", "prev-player p", "persistent.performance_mode == False", At("prev-player p", distortion))
    image prev-playerarrive = ConditionSwitch("persistent.performance_mode == True", "prev-playerarrive p", "persistent.performance_mode == False", At("prev-playerarrive p", distortion))
    image princess dragon soft free = ConditionSwitch("persistent.performance_mode == True", "princess dragon soft free p", "persistent.performance_mode == False", At("princess dragon soft free p", distortion))
    image princess dragon soft relief talk = ConditionSwitch("persistent.performance_mode == True", "princess dragon soft relief talk p", "persistent.performance_mode == False", At("princess dragon soft relief talk p", distortion))
    image princess dragon soft relief = ConditionSwitch("persistent.performance_mode == True", "princess dragon soft relief p", "persistent.performance_mode == False", At("princess dragon soft relief p", distortion))
    image princess dragon soft stabbed hurt = ConditionSwitch("persistent.performance_mode == True", "princess dragon soft stabbed hurt p", "persistent.performance_mode == False", At("princess dragon soft stabbed hurt p", distortion))
    image princess dragon soft stabbed sad neutral = ConditionSwitch("persistent.performance_mode == True", "princess dragon soft stabbed sad neutral p", "persistent.performance_mode == False", At("princess dragon soft stabbed sad neutral p", distortion))
    image princess dragon soft stabbed talk hurt = ConditionSwitch("persistent.performance_mode == True", "princess dragon soft stabbed talk hurt p", "persistent.performance_mode == False", At("princess dragon soft stabbed talk hurt p", distortion))
    image princess dragon soft stabbed talk player = ConditionSwitch("persistent.performance_mode == True", "princess dragon soft stabbed talk player p", "persistent.performance_mode == False", At("princess dragon soft stabbed talk player p", distortion))
    image princess dragon soft stabbed talk thatsyou = ConditionSwitch("persistent.performance_mode == True", "princess dragon soft stabbed talk thatsyou p", "persistent.performance_mode == False", At("princess dragon soft stabbed talk thatsyou p", distortion))
    image princess dragon soft stabbed talk = ConditionSwitch("persistent.performance_mode == True", "princess dragon soft stabbed talk p", "persistent.performance_mode == False", At("princess dragon soft stabbed talk p", distortion))
