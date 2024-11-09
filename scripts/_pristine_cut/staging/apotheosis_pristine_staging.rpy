label apotheosis_pristine_staging:

    image farback apotheosis chest = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis chest bg p", "persistent.performance_mode == False", At("cg apotheosis chest bg p", distortion))
    image debris apotheosis chest = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis chest debris p", "persistent.performance_mode == False", At("cg apotheosis chest debris p", distortion))
    image apotheosis chest slash 1 = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis chest slash 1 p", "persistent.performance_mode == False", At("cg apotheosis chest slash 1 p", distortion))
    image apotheosis chest slash 2 = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis chest slash 2 p", "persistent.performance_mode == False", At("cg apotheosis chest slash 2 p", distortion))
    image apotheosis chest = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis chest p", "persistent.performance_mode == False", At("cg apotheosis chest p", distortion))
    image cg apotheosis eye beam debris = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis eye beam debris p", "persistent.performance_mode == False", At("cg apotheosis eye beam debris p", distortion))
    image shine apotheosis eye beam 1 = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis eye beam shine 1 p", "persistent.performance_mode == False", At("cg apotheosis eye beam shine 1 p", distortion))
    image shine apotheosis eye beam 2 = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis eye beam shine 2 p", "persistent.performance_mode == False", At("cg apotheosis eye beam shine 2 p", distortion))
    image shine apotheosis eye beam 3 = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis eye beam shine 3 p", "persistent.performance_mode == False", At("cg apotheosis eye beam shine 3 p", distortion))
    image apotheosis eye beam talk = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis eye beam talk p", "persistent.performance_mode == False", At("cg apotheosis eye beam talk p", distortion))
    image apotheosis eye beam = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis eye beam p", "persistent.performance_mode == False", At("cg apotheosis eye beam p", distortion))
    image farback apotheosis eye crash = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis eye crash bg p", "persistent.performance_mode == False", At("cg apotheosis eye crash bg p", distortion))
    image debris apotheosis eye crash = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis eye crash debris p", "persistent.performance_mode == False", At("cg apotheosis eye crash debris p", distortion))
    image apotheosis eye crash talk = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis eye crash talk p", "persistent.performance_mode == False", At("cg apotheosis eye crash talk p", distortion))
    image apotheosis eye crash = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis eye crash p", "persistent.performance_mode == False", At("cg apotheosis eye crash p", distortion))
    image farback apotheosis eye out = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis eye out bg p", "persistent.performance_mode == False", At("cg apotheosis eye out bg p", distortion))
    image debris apotheosis eye out = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis eye out debris p", "persistent.performance_mode == False", At("cg apotheosis eye out debris p", distortion))
    image apotheosis eye out = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis eye out p", "persistent.performance_mode == False", At("cg apotheosis eye out p", distortion))
    image fore apotheosis eye post = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis eye post beam ground p", "persistent.performance_mode == False", At("cg apotheosis eye post beam ground p", distortion))
    image hands apotheosis eye 1 = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis eye post beam quiet 1 p", "persistent.performance_mode == False", At("cg apotheosis eye post beam quiet 1 p", distortion))
    image hands apotheosis eye 2 = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis eye post beam quiet 2 p", "persistent.performance_mode == False", At("cg apotheosis eye post beam quiet 2 p", distortion))
    image hands apotheosis eye 3 = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis eye post beam quiet 3 p", "persistent.performance_mode == False", At("cg apotheosis eye post beam quiet 3 p", distortion))
    image hands apotheosis eye 4 = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis eye post beam quiet 4 p", "persistent.performance_mode == False", At("cg apotheosis eye post beam quiet 4 p", distortion))
    image hands apotheosis eye 5 = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis eye post beam quiet 5 p", "persistent.performance_mode == False", At("cg apotheosis eye post beam quiet 5 p", distortion))
    image hands apotheosis eye 6 = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis eye post beam quiet 6 p", "persistent.performance_mode == False", At("cg apotheosis eye post beam quiet 6 p", distortion))
    image hands apotheosis eye 7 = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis eye post beam quiet 7 p", "persistent.performance_mode == False", At("cg apotheosis eye post beam quiet 7 p", distortion))
    image farback apotheosis eye post = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis eye post beam stars p", "persistent.performance_mode == False", At("cg apotheosis eye post beam stars p", distortion))
    image apotheosis eye post beam talk = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis eye post beam talk p", "persistent.performance_mode == False", At("cg apotheosis eye post beam talk p", distortion))
    image apotheosis eye post beam = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis eye post beam p", "persistent.performance_mode == False", At("cg apotheosis eye post beam p", distortion))

    image knife apotheosis hurl:
        "cg apotheosis hurl knife 1"
        0.2
        "cg apotheosis hurl knife 2"
        0.2
        "cg apotheosis hurl knife 3"

    image player apotheosis hurl:
        "cg apotheosis hurl player 1"
        0.2
        "cg apotheosis hurl player 2"
        0.2
        "cg apotheosis hurl player 3"

    image cg apotheosis hurl knife 1 = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis hurl knife 1 p", "persistent.performance_mode == False", At("cg apotheosis hurl knife 1 p", distortion))
    image cg apotheosis hurl knife 2 = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis hurl knife 2 p", "persistent.performance_mode == False", At("cg apotheosis hurl knife 2 p", distortion))
    image cg apotheosis hurl knife 3 = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis hurl knife 3 p", "persistent.performance_mode == False", At("cg apotheosis hurl knife 3 p", distortion))
    image cg apotheosis hurl player 2 = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis hurl player 2 p", "persistent.performance_mode == False", At("cg apotheosis hurl player 2 p", distortion))
    image cg apotheosis hurl player 3 = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis hurl player 3 p", "persistent.performance_mode == False", At("cg apotheosis hurl player 3 p", distortion))
    image cg apotheosis hurl player 1 = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis hurl player p", "persistent.performance_mode == False", At("cg apotheosis hurl player p", distortion))
    image farback apotheosis join land = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis join land bg p", "persistent.performance_mode == False", At("cg apotheosis join land bg p", distortion))
    image debris apotheosis join land = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis join land debris p", "persistent.performance_mode == False", At("cg apotheosis join land debris p", distortion))
    image apotheosis join land = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis join land p", "persistent.performance_mode == False", At("cg apotheosis join land p", distortion))
    image bg apotheosis join quiet = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis join quiet bg p", "persistent.performance_mode == False", At("cg apotheosis join quiet bg p", distortion))
    image debris apotheosis join quiet = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis join quiet debris p", "persistent.performance_mode == False", At("cg apotheosis join quiet debris p", distortion))
    image apotheosis join quiet talk = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis join quiet talk p", "persistent.performance_mode == False", At("cg apotheosis join quiet talk p", distortion))
    image apotheosis join quiet = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis join quiet p", "persistent.performance_mode == False", At("cg apotheosis join quiet p", distortion))

    image farback apotheosis pluck = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis pluck bg p", "persistent.performance_mode == False", At("cg apotheosis pluck bg p", distortion))
    image debris apotheosis pluck = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis pluck debris p", "persistent.performance_mode == False", At("cg apotheosis pluck debris p", distortion))
    image apotheosis pluck talk = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis pluck talk p", "persistent.performance_mode == False", At("cg apotheosis pluck talk p", distortion))
    image apotheosis pluck = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis pluck p", "persistent.performance_mode == False", At("cg apotheosis pluck p", distortion))


    image debris apotheosis reach = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis reach debris p", "persistent.performance_mode == False", At("cg apotheosis reach debris p", distortion))
    image apotheosis reach talk = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis reach talk p", "persistent.performance_mode == False", At("cg apotheosis reach talk p", distortion))
    image apotheosis reach = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis reach p", "persistent.performance_mode == False", At("cg apotheosis reach p", distortion))
    image apotheosis tear = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis tear p", "persistent.performance_mode == False", At("cg apotheosis tear p", distortion))

    image bg apotheosis prison low = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis prison alt bg p", "persistent.performance_mode == False", At("cg apotheosis prison alt bg p", distortion))
    image bg apotheosis prison = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis prison bg p", "persistent.performance_mode == False", At("cg apotheosis prison bg p", distortion))
    image apotheosis prison drop quiet = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis prison drop quiet p", "persistent.performance_mode == False", At("cg apotheosis prison drop quiet p", distortion))
    image apotheosis prison drop talk = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis prison drop talk p", "persistent.performance_mode == False", At("cg apotheosis prison drop talk p", distortion))
    image apotheosis prison drop = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis prison drop p", "persistent.performance_mode == False", At("cg apotheosis prison drop p", distortion))
    image apotheosis prison glance talk = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis prison glance talk p", "persistent.performance_mode == False", At("cg apotheosis prison glance talk p", distortion))
    image apotheosis prison glance = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis prison glance p", "persistent.performance_mode == False", At("cg apotheosis prison glance p", distortion))
    image apotheosis prison talk = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis prison talk p", "persistent.performance_mode == False", At("cg apotheosis prison talk p", distortion))
    image apotheosis prison = ConditionSwitch("persistent.performance_mode == True", "cg apotheosis prison p", "persistent.performance_mode == False", At("cg apotheosis prison p", distortion))
    image hands apotheosis prison 1 = ConditionSwitch("persistent.performance_mode == True", "hands apotheosis prison 1 p", "persistent.performance_mode == False", At("hands apotheosis prison 1 p", distortion))
    image hands apotheosis prison 2 = ConditionSwitch("persistent.performance_mode == True", "hands apotheosis prison 2 p", "persistent.performance_mode == False", At("hands apotheosis prison 2 p", distortion))
    image hands apotheosis prison 3 = ConditionSwitch("persistent.performance_mode == True", "hands apotheosis prison 3 p", "persistent.performance_mode == False", At("hands apotheosis prison 3 p", distortion))
    image hands apotheosis prison 4 = ConditionSwitch("persistent.performance_mode == True", "hands apotheosis prison 4 p", "persistent.performance_mode == False", At("hands apotheosis prison 4 p", distortion))
    image hands apotheosis prison 5 = ConditionSwitch("persistent.performance_mode == True", "hands apotheosis prison 5 p", "persistent.performance_mode == False", At("hands apotheosis prison 5 p", distortion))

    image apotheosis darkness anim:
        "apotheosis darkness 3"
        0.30
        "apotheosis darkness 4"
        0.15
        "apotheosis darkness 5"
        0.15
        "apotheosis darkness 6"
        0.15
        "apotheosis darkness 7"


    image apotheosis darkness 1 = ConditionSwitch("persistent.performance_mode == True", "apotheosis darkness 1 p", "persistent.performance_mode == False", At("apotheosis darkness 1 p", distortion))
    image apotheosis darkness 2 = ConditionSwitch("persistent.performance_mode == True", "apotheosis darkness 2 p", "persistent.performance_mode == False", At("apotheosis darkness 2 p", distortion))
    image apotheosis darkness 3 = ConditionSwitch("persistent.performance_mode == True", "apotheosis darkness 3 p", "persistent.performance_mode == False", At("apotheosis darkness 3 p", distortion))
    image apotheosis darkness 4 = ConditionSwitch("persistent.performance_mode == True", "apotheosis darkness 4 p", "persistent.performance_mode == False", At("apotheosis darkness 4 p", distortion))
    image apotheosis darkness 5 = ConditionSwitch("persistent.performance_mode == True", "apotheosis darkness 5 p", "persistent.performance_mode == False", At("apotheosis darkness 5 p", distortion))
    image apotheosis darkness 6 = ConditionSwitch("persistent.performance_mode == True", "apotheosis darkness 6 p", "persistent.performance_mode == False", At("apotheosis darkness 6 p", distortion))
    image apotheosis darkness 7 = ConditionSwitch("persistent.performance_mode == True", "apotheosis darkness 7 p", "persistent.performance_mode == False", At("apotheosis darkness 7 p", distortion))
    image apotheosis freedom begin 2 talk = ConditionSwitch("persistent.performance_mode == True", "apotheosis freedom begin 2 talk p", "persistent.performance_mode == False", At("apotheosis freedom begin 2 talk p", distortion))
    image apotheosis freedom begin 2 = ConditionSwitch("persistent.performance_mode == True", "apotheosis freedom begin 2 p", "persistent.performance_mode == False", At("apotheosis freedom begin 2 p", distortion))
    image bg apotheosis freedom begin = ConditionSwitch("persistent.performance_mode == True", "apotheosis freedom begin bg p", "persistent.performance_mode == False", At("apotheosis freedom begin bg p", distortion))
    image apotheosis freedom begin talk = ConditionSwitch("persistent.performance_mode == True", "apotheosis freedom begin talk p", "persistent.performance_mode == False", At("apotheosis freedom begin talk p", distortion))
    image apotheosis freedom begin = ConditionSwitch("persistent.performance_mode == True", "apotheosis freedom begin p", "persistent.performance_mode == False", At("apotheosis freedom begin p", distortion))
    image apotheosis freedom brink talk = ConditionSwitch("persistent.performance_mode == True", "apotheosis freedom brink talk p", "persistent.performance_mode == False", At("apotheosis freedom brink talk p", distortion))
    image apotheosis freedom brink = ConditionSwitch("persistent.performance_mode == True", "apotheosis freedom brink p", "persistent.performance_mode == False", At("apotheosis freedom brink p", distortion))
    image apotheosis freedom drown cold lower = ConditionSwitch("persistent.performance_mode == True", "apotheosis freedom drown cold lower p", "persistent.performance_mode == False", At("apotheosis freedom drown cold lower p", distortion))
    image apotheosis freedom drown cold talk = ConditionSwitch("persistent.performance_mode == True", "apotheosis freedom drown cold talk p", "persistent.performance_mode == False", At("apotheosis freedom drown cold talk p", distortion))
    image apotheosis freedom drown cold upper = ConditionSwitch("persistent.performance_mode == True", "apotheosis freedom drown cold upper p", "persistent.performance_mode == False", At("apotheosis freedom drown cold upper p", distortion))
    image apotheosis freedom drown lower = ConditionSwitch("persistent.performance_mode == True", "apotheosis freedom drown lower p", "persistent.performance_mode == False", At("apotheosis freedom drown lower p", distortion))
    image apotheosis freedom drown talk = ConditionSwitch("persistent.performance_mode == True", "apotheosis freedom drown talk p", "persistent.performance_mode == False", At("apotheosis freedom drown talk p", distortion))
    image apotheosis freedom drown upper = ConditionSwitch("persistent.performance_mode == True", "apotheosis freedom drown upper p", "persistent.performance_mode == False", At("apotheosis freedom drown upper p", distortion))
    image apotheosis freedom mound attack lower = ConditionSwitch("persistent.performance_mode == True", "apotheosis freedom mound attack lower p", "persistent.performance_mode == False", At("apotheosis freedom mound attack lower p", distortion))
    image apotheosis freedom mound attack upper = ConditionSwitch("persistent.performance_mode == True", "apotheosis freedom mound attack upper p", "persistent.performance_mode == False", At("apotheosis freedom mound attack upper p", distortion))


    image apotheosis freedom brink alarm = ConditionSwitch("persistent.performance_mode == True", "apotheosis freedom brink alarm p", "persistent.performance_mode == False", At("apotheosis freedom brink alarm p", distortion))
    image bg apotheosis post tear 2 = ConditionSwitch("persistent.performance_mode == True", "apotheosis post tear bg p", "persistent.performance_mode == False", At("apotheosis post tear bg p", distortion))
    image bg apotheosis post tear 3 = ConditionSwitch("persistent.performance_mode == True", "apotheosis post tear bg 3 p", "persistent.performance_mode == False", At("apotheosis post tear bg 3 p", distortion))
    image bg apotheosis post tear 4 = ConditionSwitch("persistent.performance_mode == True", "apotheosis post tear bg 4 p", "persistent.performance_mode == False", At("apotheosis post tear bg 4 p", distortion))
    image bg apotheosis post tear = ConditionSwitch("persistent.performance_mode == True", "apotheosis post tear bg p", "persistent.performance_mode == False", At("apotheosis post tear bg p", distortion))

    image bg apoth yeet 2 = ConditionSwitch("persistent.performance_mode == True", "bg apoth yeet 2 p", "persistent.performance_mode == False", At("bg apoth yeet 2 p", distortion))
    image bg apoth yeet 3 = ConditionSwitch("persistent.performance_mode == True", "bg apoth yeet 3 p", "persistent.performance_mode == False", At("bg apoth yeet 3 p", distortion))

    image apotheosis freedom stopped lower = ConditionSwitch("persistent.performance_mode == True", "apotheosis freedom stopped lower p", "persistent.performance_mode == False", At("apotheosis freedom stopped lower p", distortion))
    image apotheosis freedom stopped talk = ConditionSwitch("persistent.performance_mode == True", "apotheosis freedom stopped talk p", "persistent.performance_mode == False", At("apotheosis freedom stopped talk p", distortion))
    image apotheosis freedom stopped upper = ConditionSwitch("persistent.performance_mode == True", "apotheosis freedom stopped upper p", "persistent.performance_mode == False", At("apotheosis freedom stopped upper p", distortion))
    image apotheosis freedom yeet = ConditionSwitch("persistent.performance_mode == True", "apotheosis freedom yeet p", "persistent.performance_mode == False", At("apotheosis freedom yeet p", distortion))

    image player apotheosis barrier plummet = ConditionSwitch("persistent.performance_mode == True", "apotheosis barrier plummet player p", "persistent.performance_mode == False", At("apotheosis barrier plummet player p", distortion))
    image apotheosis barrier plummet = ConditionSwitch("persistent.performance_mode == True", "apotheosis barrier plummet princess p", "persistent.performance_mode == False", At("apotheosis barrier plummet princess p", distortion))
    image farback apotheosis barrier plummet = ConditionSwitch("persistent.performance_mode == True", "apotheosis barrier plummet stars p", "persistent.performance_mode == False", At("apotheosis barrier plummet stars p", distortion))
    image apotheosis barrier plummet talk = ConditionSwitch("persistent.performance_mode == True", "apotheosis barrier plummet talk p", "persistent.performance_mode == False", At("apotheosis barrier plummet talk p", distortion))

    image apotheosis dust reveal close talk = ConditionSwitch("persistent.performance_mode == True", "apotheosis dust reveal close talk p", "persistent.performance_mode == False", At("apotheosis dust reveal close talk p", distortion))
    image apotheosis dust reveal close = ConditionSwitch("persistent.performance_mode == True", "apotheosis dust reveal close p", "persistent.performance_mode == False", At("apotheosis dust reveal close p", distortion))
    image debris apotheosis dust reveal = ConditionSwitch("persistent.performance_mode == True", "apotheosis dust reveal debris p", "persistent.performance_mode == False", At("apotheosis dust reveal debris p", distortion))
    image apotheosis dust reveal open talk = ConditionSwitch("persistent.performance_mode == True", "apotheosis dust reveal open talk p", "persistent.performance_mode == False", At("apotheosis dust reveal open talk p", distortion))
    image apotheosis dust reveal open = ConditionSwitch("persistent.performance_mode == True", "apotheosis dust reveal open p", "persistent.performance_mode == False", At("apotheosis dust reveal open p", distortion))
    image farback apotheosis dust reveal = ConditionSwitch("persistent.performance_mode == True", "apotheosis dust reveal stars p", "persistent.performance_mode == False", At("apotheosis dust reveal stars p", distortion))
    image apotheosis dust reveal = ConditionSwitch("persistent.performance_mode == True", "apotheosis dust reveal p", "persistent.performance_mode == False", At("apotheosis dust reveal p", distortion))
    image apotheosis flee debris = ConditionSwitch("persistent.performance_mode == True", "apotheosis flee debris p", "persistent.performance_mode == False", At("apotheosis flee debris p", distortion))
    image apotheosis flee pluck debris = ConditionSwitch("persistent.performance_mode == True", "apotheosis flee pluck debris p", "persistent.performance_mode == False", At("apotheosis flee pluck debris p", distortion))
    image farback apotheosis flee pluck = ConditionSwitch("persistent.performance_mode == True", "apotheosis flee pluck stars p", "persistent.performance_mode == False", At("apotheosis flee pluck stars p", distortion))
    image farback apotheosis flee = ConditionSwitch("persistent.performance_mode == True", "apotheosis flee stars p", "persistent.performance_mode == False", At("apotheosis flee stars p", distortion))


    image debris apotheosis paranoid attack 1 back = ConditionSwitch("persistent.performance_mode == True", "apotheosis paranoid attack 1 back debris p", "persistent.performance_mode == False", At("apotheosis paranoid attack 1 back debris p", distortion))
    image front apotheosis paranoid attack 1 = ConditionSwitch("persistent.performance_mode == True", "apotheosis paranoid attack 1 front p", "persistent.performance_mode == False", At("apotheosis paranoid attack 1 front p", distortion))
    image apotheosis paranoid attack 1 = ConditionSwitch("persistent.performance_mode == True", "apotheosis paranoid attack 1 princess p", "persistent.performance_mode == False", At("apotheosis paranoid attack 1 princess p", distortion))
    image farback apotheosis paranoid attack 1 = ConditionSwitch("persistent.performance_mode == True", "apotheosis paranoid attack 1 stars p", "persistent.performance_mode == False", At("apotheosis paranoid attack 1 stars p", distortion))
    image debris apotheosis paranoid attack 2 back = ConditionSwitch("persistent.performance_mode == True", "apotheosis paranoid attack 2 back debris p", "persistent.performance_mode == False", At("apotheosis paranoid attack 2 back debris p", distortion))
    image front apotheosis paranoid attack 2 = ConditionSwitch("persistent.performance_mode == True", "apotheosis paranoid attack 2 front p", "persistent.performance_mode == False", At("apotheosis paranoid attack 2 front p", distortion))
    image apotheosis paranoid attack 2 = ConditionSwitch("persistent.performance_mode == True", "apotheosis paranoid attack 2 princess p", "persistent.performance_mode == False", At("apotheosis paranoid attack 2 princess p", distortion))
    image apotheosis paranoid attack 2 talk = ConditionSwitch("persistent.performance_mode == True", "apotheosis paranoid attack 2 talk p", "persistent.performance_mode == False", At("apotheosis paranoid attack 2 talk p", distortion))

    image debris apotheosis paranoid attack dust = ConditionSwitch("persistent.performance_mode == True", "apotheosis paranoid attack dust debris p", "persistent.performance_mode == False", At("apotheosis paranoid attack dust debris p", distortion))
    image player apotheosis paranoid attack dust = ConditionSwitch("persistent.performance_mode == True", "apotheosis paranoid attack dust player p", "persistent.performance_mode == False", At("apotheosis paranoid attack dust player p", distortion))
    image farback apotheosis paranoid attack dust = ConditionSwitch("persistent.performance_mode == True", "apotheosis paranoid attack dust stars p", "persistent.performance_mode == False", At("apotheosis paranoid attack dust stars p", distortion))
    image apotheosis paranoid attack dust = ConditionSwitch("persistent.performance_mode == True", "apotheosis paranoid attack dust p", "persistent.performance_mode == False", At("apotheosis paranoid attack dust p", distortion))

    image field apotheosis shatter anim:
        "field apotheosis paranoid barrier"
        4.07
        "apotheosis paranoid barrier break 1"
        3.23
        "apotheosis paranoid barrier break 2"
        3.6
        "apotheosis paranoid barrier break final"


    image apotheosis paranoid barrier break 1 = ConditionSwitch("persistent.performance_mode == True", "apotheosis paranoid barrier break 1 p", "persistent.performance_mode == False", At("apotheosis paranoid barrier break 1 p", distortion))
    image apotheosis paranoid barrier break 2 = ConditionSwitch("persistent.performance_mode == True", "apotheosis paranoid barrier break 2 p", "persistent.performance_mode == False", At("apotheosis paranoid barrier break 2 p", distortion))
    image apotheosis paranoid barrier break final = ConditionSwitch("persistent.performance_mode == True", "apotheosis paranoid barrier break final p", "persistent.performance_mode == False", At("apotheosis paranoid barrier break final p", distortion))
    image field apotheosis paranoid barrier = ConditionSwitch("persistent.performance_mode == True", "apotheosis paranoid barrier forcefield p", "persistent.performance_mode == False", At("apotheosis paranoid barrier forcefield p", distortion))
    image player apotheosis paranoid barrier = ConditionSwitch("persistent.performance_mode == True", "apotheosis paranoid barrier player p", "persistent.performance_mode == False", At("apotheosis paranoid barrier player p", distortion))
    image apotheosis paranoid barrier = ConditionSwitch("persistent.performance_mode == True", "apotheosis paranoid barrier princess p", "persistent.performance_mode == False", At("apotheosis paranoid barrier princess p", distortion))
    image farback apotheosis paranoid barrier = ConditionSwitch("persistent.performance_mode == True", "apotheosis paranoid barrier stars p", "persistent.performance_mode == False", At("apotheosis paranoid barrier stars p", distortion))
    image apotheosis paranoid barrier talk = ConditionSwitch("persistent.performance_mode == True", "apotheosis paranoid barrier talk p", "persistent.performance_mode == False", At("apotheosis paranoid barrier talk p", distortion))
    image player apotheosis paranoid charge = ConditionSwitch("persistent.performance_mode == True", "apotheosis paranoid charge player p", "persistent.performance_mode == False", At("apotheosis paranoid charge player p", distortion))
    image apotheosis paranoid charge = ConditionSwitch("persistent.performance_mode == True", "apotheosis paranoid charge princess p", "persistent.performance_mode == False", At("apotheosis paranoid charge princess p", distortion))
    image player apotheosis paranoid charge lift = ConditionSwitch("persistent.performance_mode == True", "apotheosis paranoid charge raise player p", "persistent.performance_mode == False", At("apotheosis paranoid charge raise player p", distortion))
    image apotheosis paranoid charge lift = ConditionSwitch("persistent.performance_mode == True", "apotheosis paranoid charge raise princess p", "persistent.performance_mode == False", At("apotheosis paranoid charge raise princess p", distortion))
    image farback apotheosis paranoid charge lift = ConditionSwitch("persistent.performance_mode == True", "apotheosis paranoid charge raise stars p", "persistent.performance_mode == False", At("apotheosis paranoid charge raise stars p", distortion))
    image farback apotheosis paranoid charge = ConditionSwitch("persistent.performance_mode == True", "apotheosis paranoid charge stars p", "persistent.performance_mode == False", At("apotheosis paranoid charge stars p", distortion))


    image player apotheosis paranoid pelt 1 = ConditionSwitch("persistent.performance_mode == True", "apotheosis paranoid pelt accumulation 1 p", "persistent.performance_mode == False", At("apotheosis paranoid pelt accumulation 1 p", distortion))
    image player apotheosis paranoid pelt 2 = ConditionSwitch("persistent.performance_mode == True", "apotheosis paranoid pelt accumulation 2 p", "persistent.performance_mode == False", At("apotheosis paranoid pelt accumulation 2 p", distortion))
    image player apotheosis paranoid pelt 3 = ConditionSwitch("persistent.performance_mode == True", "apotheosis paranoid pelt accumulation 3 p", "persistent.performance_mode == False", At("apotheosis paranoid pelt accumulation 3 p", distortion))
    image player apotheosis paranoid pelt 4 = ConditionSwitch("persistent.performance_mode == True", "apotheosis paranoid pelt accumulation 4 p", "persistent.performance_mode == False", At("apotheosis paranoid pelt accumulation 4 p", distortion))

    image player apotheosis pelt anim:
        "player apotheosis paranoid pelt 1"
        0.85
        "player apotheosis paranoid pelt 2"
        0.85
        "player apotheosis paranoid pelt 3"
        0.85
        "player apotheosis paranoid pelt 4"
        1.0
        "bg impact"

    image debris apotheosis pelt anim:
        "apotheosis paranoid pelt debris 1"
        0.125
        "apotheosis paranoid pelt debris 2"
        0.125
        "apotheosis paranoid pelt debris 3"
        0.125
        repeat
    image player normal hold = ConditionSwitch("persistent.performance_mode == True", "player normal hold p", "persistent.performance_mode == False", At("player normal hold p", distortion))
    image apotheosis paranoid pelt debris 1 = ConditionSwitch("persistent.performance_mode == True", "apotheosis paranoid pelt debris 1 p", "persistent.performance_mode == False", At("apotheosis paranoid pelt debris 1 p", distortion))
    image apotheosis paranoid pelt debris 2 = ConditionSwitch("persistent.performance_mode == True", "apotheosis paranoid pelt debris 2 p", "persistent.performance_mode == False", At("apotheosis paranoid pelt debris 2 p", distortion))
    image apotheosis paranoid pelt debris 3 = ConditionSwitch("persistent.performance_mode == True", "apotheosis paranoid pelt debris 3 p", "persistent.performance_mode == False", At("apotheosis paranoid pelt debris 3 p", distortion))
    image farback apotheosis paranoid pelt = ConditionSwitch("persistent.performance_mode == True", "apotheosis paranoid pelt stars p", "persistent.performance_mode == False", At("apotheosis paranoid pelt stars p", distortion))
    image apotheosis paranoid pelt = ConditionSwitch("persistent.performance_mode == True", "apotheosis paranoid pelt p", "persistent.performance_mode == False", At("apotheosis paranoid pelt p", distortion))

    image sparks apotheosis paranoid barrier = ConditionSwitch("persistent.performance_mode == True", "apotheosis paranoid barrier sparks p", "persistent.performance_mode == False", At("apotheosis paranoid barrier sparks p", distortion))
    image player apotheosis paranoid quiet begin = ConditionSwitch("persistent.performance_mode == True", "apotheosis paranoid quiet begin player p", "persistent.performance_mode == False", At("apotheosis paranoid quiet begin player p", distortion))
    image apotheosis paranoid quiet begin talk = ConditionSwitch("persistent.performance_mode == True", "apotheosis paranoid quiet begin talk p", "persistent.performance_mode == False", At("apotheosis paranoid quiet begin talk p", distortion))
    image apotheosis paranoid quiet begin = ConditionSwitch("persistent.performance_mode == True", "apotheosis paranoid quiet begin p", "persistent.performance_mode == False", At("apotheosis paranoid quiet begin p", distortion))
    image apotheosis paranoid quiet wonder talk = ConditionSwitch("persistent.performance_mode == True", "apotheosis paranoid quiet wonder talk p", "persistent.performance_mode == False", At("apotheosis paranoid quiet wonder talk p", distortion))
    image apotheosis paranoid quiet wonder = ConditionSwitch("persistent.performance_mode == True", "apotheosis paranoid quiet wonder p", "persistent.performance_mode == False", At("apotheosis paranoid quiet wonder p", distortion))

    image apotheosis paranoid torment anim:
        "apotheosis paranoid torment 1"
        0.25
        "apotheosis paranoid torment 2"
        0.25
        "apotheosis paranoid torment 3"

    image apotheosis paranoid torment 1 = ConditionSwitch("persistent.performance_mode == True", "apotheosis paranoid torment 1 p", "persistent.performance_mode == False", At("apotheosis paranoid torment 1 p", distortion))
    image apotheosis paranoid torment 2 = ConditionSwitch("persistent.performance_mode == True", "apotheosis paranoid torment 2 p", "persistent.performance_mode == False", At("apotheosis paranoid torment 2 p", distortion))
    image apotheosis paranoid torment 3 = ConditionSwitch("persistent.performance_mode == True", "apotheosis paranoid torment 3 p", "persistent.performance_mode == False", At("apotheosis paranoid torment 3 p", distortion))
    image apotheosis paranoid torment 4 talk = ConditionSwitch("persistent.performance_mode == True", "apotheosis paranoid torment 4 talk p", "persistent.performance_mode == False", At("apotheosis paranoid torment 4 talk p", distortion))
    image apotheosis paranoid torment 4 = ConditionSwitch("persistent.performance_mode == True", "apotheosis paranoid torment 4 p", "persistent.performance_mode == False", At("apotheosis paranoid torment 4 p", distortion))
    image apotheosis paranoid torment final quiet = ConditionSwitch("persistent.performance_mode == True", "apotheosis paranoid torment final quiet p", "persistent.performance_mode == False", At("apotheosis paranoid torment final quiet p", distortion))
    image apotheosis paranoid torment final talk = ConditionSwitch("persistent.performance_mode == True", "apotheosis paranoid torment final talk p", "persistent.performance_mode == False", At("apotheosis paranoid torment final talk p", distortion))
    image apotheosis paranoid torment final = ConditionSwitch("persistent.performance_mode == True", "apotheosis paranoid torment final p", "persistent.performance_mode == False", At("apotheosis paranoid torment final p", distortion))
    image hands apotheosis paranoid 2 = ConditionSwitch("persistent.performance_mode == True", "hands apotheosis paranoid 2 p", "persistent.performance_mode == False", At("hands apotheosis paranoid 2 p", distortion))
    image hands apotheosis paranoid 3 = ConditionSwitch("persistent.performance_mode == True", "hands apotheosis paranoid 3 p", "persistent.performance_mode == False", At("hands apotheosis paranoid 3 p", distortion))
    image hands apotheosis paranoid 4 = ConditionSwitch("persistent.performance_mode == True", "hands apotheosis paranoid 4 p", "persistent.performance_mode == False", At("hands apotheosis paranoid 4 p", distortion))
    image hands apotheosis paranoid 5 = ConditionSwitch("persistent.performance_mode == True", "hands apotheosis paranoid 5 p", "persistent.performance_mode == False", At("hands apotheosis paranoid 5 p", distortion))
    image hands apotheosis paranoid 6 = ConditionSwitch("persistent.performance_mode == True", "hands apotheosis paranoid 6 p", "persistent.performance_mode == False", At("hands apotheosis paranoid 6 p", distortion))
    image hands apotheosis paranoid = ConditionSwitch("persistent.performance_mode == True", "hands apotheosis paranoid p", "persistent.performance_mode == False", At("hands apotheosis paranoid p", distortion))
