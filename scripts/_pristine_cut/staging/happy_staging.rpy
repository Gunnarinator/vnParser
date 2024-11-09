label happy_art_staging:

    image mirror happy downstairs = "bg happy downstairs mirror p"
    image bg happy downstairs = ConditionSwitch("persistent.performance_mode == True", "bg happy downstairs p", "persistent.performance_mode == False", At("bg happy downstairs p", distortion))

    image bg happy dark = ConditionSwitch("persistent.performance_mode == True", "bg happy dark p", "persistent.performance_mode == False", At("bg happy dark p", distortion))

    image bg happy upstairs = ConditionSwitch("happy_torches == 4", "bg happy main", "happy_torches == 3", "bg happy main onedown", "happy_torches == 2", "bg happy main twodown", "happy_torches == 1", "bg happy main threedown", "happy_torches <= 0", "bg happy dark")


    image bg happy leaving hand offer = ConditionSwitch("persistent.performance_mode == True", "bg happy leaving hand offer p", "persistent.performance_mode == False", At("bg happy leaving hand offer p", distortion))
    image bg happy main onedown = ConditionSwitch("persistent.performance_mode == True", "bg happy main onedown p", "persistent.performance_mode == False", At("bg happy main onedown p", distortion))
    image bg happy main = ConditionSwitch("persistent.performance_mode == True", "bg happy main p", "persistent.performance_mode == False", At("bg happy main p", distortion))
    image bg happy main threedown = ConditionSwitch("persistent.performance_mode == True", "bg happy main threedown p", "persistent.performance_mode == False", At("bg happy main threedown p", distortion))
    image bg happy main twodown = ConditionSwitch("persistent.performance_mode == True", "bg happy main twodown p", "persistent.performance_mode == False", At("bg happy main twodown p", distortion))

    image bg happy mirror door = ConditionSwitch("persistent.performance_mode == True", "bg happy mirror door p", "persistent.performance_mode == False", At("bg happy mirror door p", distortion))
    image player happy mirror = ConditionSwitch("persistent.performance_mode == True", "bg happy mirror hand p", "persistent.performance_mode == False", At("bg happy mirror hand p", distortion))
    image mirror happy close = "bg happy mirror p"

    image bg happy no exit = ConditionSwitch("persistent.performance_mode == True", "bg happy no exit p", "persistent.performance_mode == False", At("bg happy no exit p", distortion))
    image bg happy stairs = ConditionSwitch("persistent.performance_mode == True", "bg happy stairs p", "persistent.performance_mode == False", At("bg happy stairs p", distortion))

    image cg happy dance 1 = ConditionSwitch("persistent.performance_mode == True", "cg happy dance 1 foreground p", "persistent.performance_mode == False", At("cg happy dance 1 foreground p", distortion))
    image bg happy dance 1 = ConditionSwitch("persistent.performance_mode == True", "cg happy dance 1 stars p", "persistent.performance_mode == False", At("cg happy dance 1 stars p", distortion))

    image cg happy dance 2 = ConditionSwitch("persistent.performance_mode == True", "cg happy dance 2 p", "persistent.performance_mode == False", At("cg happy dance 2 p", distortion))
    image bg happy dance 2 = ConditionSwitch("persistent.performance_mode == True", "cg happy dance 2 stars p", "persistent.performance_mode == False", At("cg happy dance 2 stars p", distortion))

    image cg happy dance 3 = ConditionSwitch("persistent.performance_mode == True", "cg happy dance 3 p", "persistent.performance_mode == False", At("cg happy dance 3 p", distortion))
    image bg happy dance 3 = ConditionSwitch("persistent.performance_mode == True", "cg happy dance 3 stars p", "persistent.performance_mode == False", At("cg happy dance 3 stars p", distortion))

    image cg happy dance 3 talk = ConditionSwitch("persistent.performance_mode == True", "cg happy dance 3 talk p", "persistent.performance_mode == False", At("cg happy dance 3 talk p", distortion))
    image cg happy leaving stairs nohand = ConditionSwitch("persistent.performance_mode == True", "cg happy leaving stairs nohand p", "persistent.performance_mode == False", At("cg happy leaving stairs nohand p", distortion))
    image cg happy leaving stairs = ConditionSwitch("persistent.performance_mode == True", "cg happy leaving stairs p", "persistent.performance_mode == False", At("cg happy leaving stairs p", distortion))

    image farback happy outside = ConditionSwitch("persistent.performance_mode == True", "cg happy outside stars p", "persistent.performance_mode == False", At("cg happy outside stars p", distortion))
    image bg happy outside = ConditionSwitch("persistent.performance_mode == True", "cg happy outside bg trees p", "persistent.performance_mode == False", At("cg happy outside bg trees p", distortion))
    image mid happy outside = ConditionSwitch("persistent.performance_mode == True", "cg happy outside midground trees p", "persistent.performance_mode == False", At("cg happy outside midground trees p", distortion))
    image cg happy outside nohand = ConditionSwitch("persistent.performance_mode == True", "cg happy outside nohand p", "persistent.performance_mode == False", At("cg happy outside nohand p", distortion))
    image cg happy outside nohand talk = ConditionSwitch("persistent.performance_mode == True", "cg happy outside nohand talk p", "persistent.performance_mode == False", At("cg happy outside nohand talk p", distortion))
    image cg happy outside = ConditionSwitch("persistent.performance_mode == True", "cg happy outside p", "persistent.performance_mode == False", At("cg happy outside p", distortion))

    image cg happy outside talk = ConditionSwitch("persistent.performance_mode == True", "cg happy outside talk p", "persistent.performance_mode == False", At("cg happy outside talk p", distortion))
    image cg happy rise = ConditionSwitch("persistent.performance_mode == True", "cg happy rise p", "persistent.performance_mode == False", At("cg happy rise p", distortion))
    image cg happy slay begin = ConditionSwitch("persistent.performance_mode == True", "cg happy slay begin p", "persistent.performance_mode == False", At("cg happy slay begin p", distortion))
    image cg happy slay cold = ConditionSwitch("persistent.performance_mode == True", "cg happy slay cold p", "persistent.performance_mode == False", At("cg happy slay cold p", distortion))
    image cg happy slay cold talk = ConditionSwitch("persistent.performance_mode == True", "cg happy slay cold talk p", "persistent.performance_mode == False", At("cg happy slay cold talk p", distortion))
    image cg happy slay grab = ConditionSwitch("persistent.performance_mode == True", "cg happy slay grab p", "persistent.performance_mode == False", At("cg happy slay grab p", distortion))
    image cg happy slay murder = ConditionSwitch("persistent.performance_mode == True", "cg happy slay murder p", "persistent.performance_mode == False", At("cg happy slay murder p", distortion))
    image cg happy slay murder talk = ConditionSwitch("persistent.performance_mode == True", "cg happy slay murder talk p", "persistent.performance_mode == False", At("cg happy slay murder talk p", distortion))
    image damsel disc = ConditionSwitch("persistent.performance_mode == True", "damsel disc p", "persistent.performance_mode == False", At("damsel disc p", distortion))
    image damsel disc shook = ConditionSwitch("persistent.performance_mode == True", "damsel disc shook p", "persistent.performance_mode == False", At("damsel disc shook p", distortion))
    image damsel disc shook talk = ConditionSwitch("persistent.performance_mode == True", "damsel disc shook talk p", "persistent.performance_mode == False", At("damsel disc shook talk p", distortion))
    image damsel disc shrug = ConditionSwitch("persistent.performance_mode == True", "damsel disc shrug p", "persistent.performance_mode == False", At("damsel disc shrug p", distortion))
    image damsel disc shrug talk = ConditionSwitch("persistent.performance_mode == True", "damsel disc shrug talk p", "persistent.performance_mode == False", At("damsel disc shrug talk p", distortion))
    image damsel disc talk = ConditionSwitch("persistent.performance_mode == True", "damsel disc talk p", "persistent.performance_mode == False", At("damsel disc talk p", distortion))
    image damsel heart reach = ConditionSwitch("persistent.performance_mode == True", "damsel heart reach p", "persistent.performance_mode == False", At("damsel heart reach p", distortion))
    image damsel mesmerized = ConditionSwitch("persistent.performance_mode == True", "damsel mesmerized p", "persistent.performance_mode == False", At("damsel mesmerized p", distortion))
    image damsel mesmerized talk = ConditionSwitch("persistent.performance_mode == True", "damsel mesmerized talk p", "persistent.performance_mode == False", At("damsel mesmerized talk p", distortion))
    image damsel disc eyes = ConditionSwitch("persistent.performance_mode == True", "damsel disc eyes p", "persistent.performance_mode == False", At("damsel disc eyes p", distortion))
    image damsel disc eyes talk = ConditionSwitch("persistent.performance_mode == True", "damsel disc eyes talk p", "persistent.performance_mode == False", At("damsel disc eyes talk p", distortion))
    image damsel disc meh = ConditionSwitch("persistent.performance_mode == True", "damsel disc meh p", "persistent.performance_mode == False", At("damsel disc meh p", distortion))


    image fire happy = ConditionSwitch("happy_torches == 4", "fire happy1", "happy_torches == 3", "fire happy2", "happy_torches == 2", "fire happy3", "happy_torches == 1", "fire happy4", "happy_torches < 1", "emptyimage")
    image fire happy flare = ConditionSwitch("happy_torches == 4", "fire happy1 flare", "happy_torches == 3", "fire happy2 flare", "happy_torches == 2", "fire happy3 flare", "happy_torches == 1", "fire happy4 flare", "happy_torches < 1", "emptyimage")

    image fire happy1:
        "fire happy 1"
        0.1
        "fire happy 2"
        0.1
        "fire happy 3"
        0.1
        "fire happy 4"
        0.1
        repeat

    image fire happy1 flare:
        "fire happy flare all 1"
        0.1
        "fire happy flare all 2"
        0.1
        "fire happy flare all 3"
        0.1
        repeat

    image fire happy2:
        "fire happy onedown 1"
        0.1
        "fire happy onedown 2"
        0.1
        "fire happy onedown 3"
        0.1
        "fire happy onedown 4"
        0.1
        repeat

    image fire happy2 flare:
        "fire happy flare onedown 1"
        0.1
        "fire happy flare onedown 2"
        0.1
        "fire happy flare onedown 3"
        0.1
        repeat

    image fire happy3:
        "fire happy twodown 1"
        0.1
        "fire happy twodown 2"
        0.1
        "fire happy twodown 3"
        0.1
        "fire happy twodown 4"
        0.1
        repeat

    image fire happy3 flare:
        "fire happy flare twodown 1"
        0.1
        "fire happy flare twodown 2"
        0.1
        "fire happy flare twodown 3"
        0.1
        repeat

    image fire happy4:
        "fire happy threedown 1"
        0.1
        "fire happy threedown 2"
        0.1
        "fire happy threedown 3"
        0.1
        "fire happy threedown 4"
        0.1
        repeat

    image fire happy4 flare:
        "fire happy flare threedown 1"
        0.1
        "fire happy flare threedown 2"
        0.1
        "fire happy flare threedown 3"
        0.1
        repeat

    image fire happy 1 = ConditionSwitch("persistent.performance_mode == True", "fire happy 1 p", "persistent.performance_mode == False", At("fire happy 1 p", distortion))
    image fire happy 2 = ConditionSwitch("persistent.performance_mode == True", "fire happy 2 p", "persistent.performance_mode == False", At("fire happy 2 p", distortion))
    image fire happy 3 = ConditionSwitch("persistent.performance_mode == True", "fire happy 3 p", "persistent.performance_mode == False", At("fire happy 3 p", distortion))
    image fire happy 4 = ConditionSwitch("persistent.performance_mode == True", "fire happy 4 p", "persistent.performance_mode == False", At("fire happy 4 p", distortion))
    image fire happy flare all 1 = ConditionSwitch("persistent.performance_mode == True", "fire happy flare all 1 p", "persistent.performance_mode == False", At("fire happy flare all 1 p", distortion))
    image fire happy flare all 2 = ConditionSwitch("persistent.performance_mode == True", "fire happy flare all 2 p", "persistent.performance_mode == False", At("fire happy flare all 2 p", distortion))
    image fire happy flare all 3 = ConditionSwitch("persistent.performance_mode == True", "fire happy flare all 3 p", "persistent.performance_mode == False", At("fire happy flare all 3 p", distortion))
    image fire happy flare onedown 1 = ConditionSwitch("persistent.performance_mode == True", "fire happy flare onedown 1 p", "persistent.performance_mode == False", At("fire happy flare onedown 1 p", distortion))
    image fire happy flare onedown 2 = ConditionSwitch("persistent.performance_mode == True", "fire happy flare onedown 2 p", "persistent.performance_mode == False", At("fire happy flare onedown 2 p", distortion))
    image fire happy flare onedown 3 = ConditionSwitch("persistent.performance_mode == True", "fire happy flare onedown 3 p", "persistent.performance_mode == False", At("fire happy flare onedown 3 p", distortion))
    image fire happy flare threedown 1 = ConditionSwitch("persistent.performance_mode == True", "fire happy flare threedown 1 p", "persistent.performance_mode == False", At("fire happy flare threedown 1 p", distortion))
    image fire happy flare threedown 2 = ConditionSwitch("persistent.performance_mode == True", "fire happy flare threedown 2 p", "persistent.performance_mode == False", At("fire happy flare threedown 2 p", distortion))
    image fire happy flare threedown 3 = ConditionSwitch("persistent.performance_mode == True", "fire happy flare threedown 3 p", "persistent.performance_mode == False", At("fire happy flare threedown 3 p", distortion))
    image fire happy flare twodown 1 = ConditionSwitch("persistent.performance_mode == True", "fire happy flare twodown 1 p", "persistent.performance_mode == False", At("fire happy flare twodown 1 p", distortion))
    image fire happy flare twodown 2 = ConditionSwitch("persistent.performance_mode == True", "fire happy flare twodown 2 p", "persistent.performance_mode == False", At("fire happy flare twodown 2 p", distortion))
    image fire happy flare twodown 3 = ConditionSwitch("persistent.performance_mode == True", "fire happy flare twodown 3 p", "persistent.performance_mode == False", At("fire happy flare twodown 3 p", distortion))
    image fire happy onedown 1 = ConditionSwitch("persistent.performance_mode == True", "fire happy onedown 1 p", "persistent.performance_mode == False", At("fire happy onedown 1 p", distortion))
    image fire happy onedown 2 = ConditionSwitch("persistent.performance_mode == True", "fire happy onedown 2 p", "persistent.performance_mode == False", At("fire happy onedown 2 p", distortion))
    image fire happy onedown 3 = ConditionSwitch("persistent.performance_mode == True", "fire happy onedown 3 p", "persistent.performance_mode == False", At("fire happy onedown 3 p", distortion))
    image fire happy onedown 4 = ConditionSwitch("persistent.performance_mode == True", "fire happy onedown 4 p", "persistent.performance_mode == False", At("fire happy onedown 4 p", distortion))
    image fire happy threedown 1 = ConditionSwitch("persistent.performance_mode == True", "fire happy threedown 1 p", "persistent.performance_mode == False", At("fire happy threedown 1 p", distortion))
    image fire happy threedown 2 = ConditionSwitch("persistent.performance_mode == True", "fire happy threedown 2 p", "persistent.performance_mode == False", At("fire happy threedown 2 p", distortion))
    image fire happy threedown 3 = ConditionSwitch("persistent.performance_mode == True", "fire happy threedown 3 p", "persistent.performance_mode == False", At("fire happy threedown 3 p", distortion))
    image fire happy threedown 4 = ConditionSwitch("persistent.performance_mode == True", "fire happy threedown 4 p", "persistent.performance_mode == False", At("fire happy threedown 4 p", distortion))
    image fire happy twodown 1 = ConditionSwitch("persistent.performance_mode == True", "fire happy twodown 1 p", "persistent.performance_mode == False", At("fire happy twodown 1 p", distortion))
    image fire happy twodown 2 = ConditionSwitch("persistent.performance_mode == True", "fire happy twodown 2 p", "persistent.performance_mode == False", At("fire happy twodown 2 p", distortion))
    image fire happy twodown 3 = ConditionSwitch("persistent.performance_mode == True", "fire happy twodown 3 p", "persistent.performance_mode == False", At("fire happy twodown 3 p", distortion))
    image fire happy twodown 4 = ConditionSwitch("persistent.performance_mode == True", "fire happy twodown 4 p", "persistent.performance_mode == False", At("fire happy twodown 4 p", distortion))

    image game happy basic set:
        "emptyimage"
        0.5
        "game happy basic"

    image game happy advanced set:
        "game happy basic finished"
        0.5
        "game happy complex"

    image food happy disappear:
        "food happy eaten"
        0.5
        "emptyimage"


    image food happy untouched disappear:
        "food happy set"
        0.5
        "emptyimage"


    image food happy swept:
        "food happy eaten"
        0.5
        "emptyimage"


    image food happy eaten = ConditionSwitch("persistent.performance_mode == True", "food happy eaten p", "persistent.performance_mode == False", At("food happy eaten p", distortion))

    image food happy replace:
        "food happy eaten"
        0.5
        "food happy set"


    image food happy placed:
        "emptyimage"
        0.5
        "food happy set"

    image food happy set = ConditionSwitch("persistent.performance_mode == True", "food happy set p", "persistent.performance_mode == False", At("food happy set p", distortion))




    image game happy basic finished = ConditionSwitch("persistent.performance_mode == True", "game happy basic finished p", "persistent.performance_mode == False", At("game happy basic finished p", distortion))
    image game happy basic = ConditionSwitch("persistent.performance_mode == True", "game happy basic p", "persistent.performance_mode == False", At("game happy basic p", distortion))
    image game happy complex finished = ConditionSwitch("persistent.performance_mode == True", "game happy complex finished p", "persistent.performance_mode == False", At("game happy complex finished p", distortion))
    image game happy complex = ConditionSwitch("persistent.performance_mode == True", "game happy complex p", "persistent.performance_mode == False", At("game happy complex p", distortion))
    image hands happy dance 1 = ConditionSwitch("persistent.performance_mode == True", "hands happy dance 1 p", "persistent.performance_mode == False", At("hands happy dance 1 p", distortion))
    image hands happy dance 2 = ConditionSwitch("persistent.performance_mode == True", "hands happy dance 2 p", "persistent.performance_mode == False", At("hands happy dance 2 p", distortion))
    image hands happy dance 3 = ConditionSwitch("persistent.performance_mode == True", "hands happy dance 3 p", "persistent.performance_mode == False", At("hands happy dance 3 p", distortion))
    image hands happy dance 4 = ConditionSwitch("persistent.performance_mode == True", "hands happy dance 4 p", "persistent.performance_mode == False", At("hands happy dance 4 p", distortion))
    image hands happy dance 5 = ConditionSwitch("persistent.performance_mode == True", "hands happy dance 5 p", "persistent.performance_mode == False", At("hands happy dance 5 p", distortion))
    image hands happy fire 1 = ConditionSwitch("persistent.performance_mode == True", "hands happy fire 1 p", "persistent.performance_mode == False", At("hands happy fire 1 p", distortion))
    image hands happy fire 2 = ConditionSwitch("persistent.performance_mode == True", "hands happy fire 2 p", "persistent.performance_mode == False", At("hands happy fire 2 p", distortion))
    image hands happy fire 3 = ConditionSwitch("persistent.performance_mode == True", "hands happy fire 3 p", "persistent.performance_mode == False", At("hands happy fire 3 p", distortion))
    image hands happy fire 4 = ConditionSwitch("persistent.performance_mode == True", "hands happy fire 4 p", "persistent.performance_mode == False", At("hands happy fire 4 p", distortion))
    image hands happy fire 5 = ConditionSwitch("persistent.performance_mode == True", "hands happy fire 5 p", "persistent.performance_mode == False", At("hands happy fire 5 p", distortion))
    image hands happy fire 6 = ConditionSwitch("persistent.performance_mode == True", "hands happy fire 6 p", "persistent.performance_mode == False", At("hands happy fire 6 p", distortion))
    image hands happy free final 1 = ConditionSwitch("persistent.performance_mode == True", "hands happy free final 1 p", "persistent.performance_mode == False", At("hands happy free final 1 p", distortion))
    image hands happy free final 2 = ConditionSwitch("persistent.performance_mode == True", "hands happy free final 2 p", "persistent.performance_mode == False", At("hands happy free final 2 p", distortion))
    image hands happy free final 3 = ConditionSwitch("persistent.performance_mode == True", "hands happy free final 3 p", "persistent.performance_mode == False", At("hands happy free final 3 p", distortion))
    image hands happy free final 4 = ConditionSwitch("persistent.performance_mode == True", "hands happy free final 4 p", "persistent.performance_mode == False", At("hands happy free final 4 p", distortion))
    image hands happy free final 5 = ConditionSwitch("persistent.performance_mode == True", "hands happy free final 5 p", "persistent.performance_mode == False", At("hands happy free final 5 p", distortion))
    image hands happy slay 2 = ConditionSwitch("persistent.performance_mode == True", "hands happy slay 2 p", "persistent.performance_mode == False", At("hands happy slay 2 p", distortion))
    image hands happy slay 3 = ConditionSwitch("persistent.performance_mode == True", "hands happy slay 3 p", "persistent.performance_mode == False", At("hands happy slay 3 p", distortion))
    image hands happy slay 4 = ConditionSwitch("persistent.performance_mode == True", "hands happy slay 4 p", "persistent.performance_mode == False", At("hands happy slay 4 p", distortion))
    image hands happy slay 5 = ConditionSwitch("persistent.performance_mode == True", "hands happy slay 5 p", "persistent.performance_mode == False", At("hands happy slay 5 p", distortion))
    image hands happy slay1 = ConditionSwitch("persistent.performance_mode == True", "hands happy slay1 p", "persistent.performance_mode == False", At("hands happy slay1 p", distortion))
    image happy d neutral = ConditionSwitch("persistent.performance_mode == True", "happy d neutral p", "persistent.performance_mode == False", At("happy d neutral p", strongwarp))
    image happy d neutral talk = ConditionSwitch("persistent.performance_mode == True", "happy d neutral talk p", "persistent.performance_mode == False", At("happy d neutral talk p", strongwarp))
    image happy d sad = ConditionSwitch("persistent.performance_mode == True", "happy d sad p", "persistent.performance_mode == False", At("happy d sad p", strongwarp))
    image happy d sad talk = ConditionSwitch("persistent.performance_mode == True", "happy d sad talk p", "persistent.performance_mode == False", At("happy d sad talk p", strongwarp))
    image happy d sob = ConditionSwitch("persistent.performance_mode == True", "happy d sob p", "persistent.performance_mode == False", At("happy d sob p", strongwarp))
    image cg happy dance suggest = ConditionSwitch("persistent.performance_mode == True", "happy dance suggest p", "persistent.performance_mode == False", At("happy dance suggest p", distortion))
    image cg happy dance suggest talk = ConditionSwitch("persistent.performance_mode == True", "happy dance suggest talk p", "persistent.performance_mode == False", At("happy dance suggest talk p", distortion))
    image happy free final talk = ConditionSwitch("persistent.performance_mode == True", "happy free final talk p", "persistent.performance_mode == False", At("happy free final talk p", distortion))
    image happy leaving end = ConditionSwitch("persistent.performance_mode == True", "happy leaving end p", "persistent.performance_mode == False", At("happy leaving end p", distortion))
    image happy leaving end talk = ConditionSwitch("persistent.performance_mode == True", "happy leaving end talk p", "persistent.performance_mode == False", At("happy leaving end talk p", distortion))
    image happy leaving hand offer = ConditionSwitch("persistent.performance_mode == True", "happy leaving hand offer p", "persistent.performance_mode == False", At("happy leaving hand offer p", distortion))
    image happy leaving neutral = ConditionSwitch("persistent.performance_mode == True", "happy leaving neutral p", "persistent.performance_mode == False", At("happy leaving neutral p", distortion))
    image happy leaving neutral talk = ConditionSwitch("persistent.performance_mode == True", "happy leaving neutral talk p", "persistent.performance_mode == False", At("happy leaving neutral talk p", distortion))
    image happy leaving relieved talk = ConditionSwitch("persistent.performance_mode == True", "happy leaving relieved talk p", "persistent.performance_mode == False", At("happy leaving relieved talk p", distortion))
    image happy leaving sad smile = ConditionSwitch("persistent.performance_mode == True", "happy leaving sad smile p", "persistent.performance_mode == False", At("happy leaving sad smile p", distortion))
    image happy leaving sad smile talk = ConditionSwitch("persistent.performance_mode == True", "happy leaving sad smile talk p", "persistent.performance_mode == False", At("happy leaving sad smile talk p", distortion))
    image happy leaving take hand = ConditionSwitch("persistent.performance_mode == True", "happy leaving take hand p", "persistent.performance_mode == False", At("happy leaving take hand p", distortion))
    image happy leaving tired = ConditionSwitch("persistent.performance_mode == True", "happy leaving tired p", "persistent.performance_mode == False", At("happy leaving tired p", distortion))
    image happy leaving tired talk = ConditionSwitch("persistent.performance_mode == True", "happy leaving tired talk p", "persistent.performance_mode == False", At("happy leaving tired talk p", distortion))
    image happy leaving worried talk = ConditionSwitch("persistent.performance_mode == True", "happy leaving worried talk p", "persistent.performance_mode == False", At("happy leaving worried talk p", distortion))
    image happy t eat = ConditionSwitch("persistent.performance_mode == True", "happy t eat p", "persistent.performance_mode == False", At("happy t eat p", strongwarp))
    image happy t empty smile = ConditionSwitch("persistent.performance_mode == True", "happy t empty smile p", "persistent.performance_mode == False", At("happy t empty smile p", strongwarp))
    image happy t empty smile talk = ConditionSwitch("persistent.performance_mode == True", "happy t empty smile talk p", "persistent.performance_mode == False", At("happy t empty smile talk p", strongwarp))
    image happy t nervous = ConditionSwitch("persistent.performance_mode == True", "happy t nervous p", "persistent.performance_mode == False", At("happy t nervous p", strongwarp))
    image happy t nervous talk = ConditionSwitch("persistent.performance_mode == True", "happy t nervous talk p", "persistent.performance_mode == False", At("happy t nervous talk p", strongwarp))
    image happy t neutral = ConditionSwitch("persistent.performance_mode == True", "happy t neutral p", "persistent.performance_mode == False", At("happy t neutral p", strongwarp))
    image happy t neutral talk = ConditionSwitch("persistent.performance_mode == True", "happy t neutral talk p", "persistent.performance_mode == False", At("happy t neutral talk p", strongwarp))
    image happy t sad = ConditionSwitch("persistent.performance_mode == True", "happy t sad p", "persistent.performance_mode == False", At("happy t sad p", strongwarp))
    image happy t sad smile = ConditionSwitch("persistent.performance_mode == True", "happy t sad smile p", "persistent.performance_mode == False", At("happy t sad smile p", strongwarp))
    image happy t sad smile talk = ConditionSwitch("persistent.performance_mode == True", "happy t sad smile talk p", "persistent.performance_mode == False", At("happy t sad smile talk p", strongwarp))
    image happy t scared = ConditionSwitch("persistent.performance_mode == True", "happy t scared p", "persistent.performance_mode == False", At("happy t scared p", strongwarp))
    image happy t scared talk = ConditionSwitch("persistent.performance_mode == True", "happy t scared talk p", "persistent.performance_mode == False", At("happy t scared talk p", strongwarp))
    image happy t serious talk = ConditionSwitch("persistent.performance_mode == True", "happy t serious talk p", "persistent.performance_mode == False", At("happy t serious talk p", strongwarp))
    image happy t shadow tight = ConditionSwitch("persistent.performance_mode == True", "happy t shadow tight p", "persistent.performance_mode == False", At("happy t shadow tight p", strongwarp))
    image happy t shadow tight talk = ConditionSwitch("persistent.performance_mode == True", "happy t shadow tight talk p", "persistent.performance_mode == False", At("happy t shadow tight talk p", strongwarp))
    image happy t smile genuine = ConditionSwitch("persistent.performance_mode == True", "happy t smile genuine p", "persistent.performance_mode == False", At("happy t smile genuine p", strongwarp))
    image happy t smile genuine talk = ConditionSwitch("persistent.performance_mode == True", "happy t smile genuine talk p", "persistent.performance_mode == False", At("happy t smile genuine talk p", strongwarp))
    image happy tf final = ConditionSwitch("persistent.performance_mode == True", "happy tf final p", "persistent.performance_mode == False", At("happy tf final p", strongwarp))
    image happy tf final talk = ConditionSwitch("persistent.performance_mode == True", "happy tf final talk p", "persistent.performance_mode == False", At("happy tf final talk p", strongwarp))
    image happy tf fond = ConditionSwitch("persistent.performance_mode == True", "happy tf fond p", "persistent.performance_mode == False", At("happy tf fond p", strongwarp))
    image happy tf fond talk = ConditionSwitch("persistent.performance_mode == True", "happy tf fond talk p", "persistent.performance_mode == False", At("happy tf fond talk p", strongwarp))
    image player chairarms empty = ConditionSwitch("persistent.performance_mode == True", "player chairarms empty p", "persistent.performance_mode == False", At("player chairarms empty p", distortion))
    image player damsel hands plunge = ConditionSwitch("persistent.performance_mode == True", "player damsel hands plunge p", "persistent.performance_mode == False", At("player damsel hands plunge p", distortion))
    image player damsel hands up = ConditionSwitch("persistent.performance_mode == True", "player damsel hands raise p", "persistent.performance_mode == False", At("player damsel hands raise p", distortion))
    image player damsel yowch = ConditionSwitch("persistent.performance_mode == True", "player damsel yowch p", "persistent.performance_mode == False", At("player damsel yowch p", distortion))
    image player food eat = ConditionSwitch("persistent.performance_mode == True", "player food eat p", "persistent.performance_mode == False", At("player food eat p", distortion))
    image player game playing = ConditionSwitch("persistent.performance_mode == True", "player game play p", "persistent.performance_mode == False", At("player game play p", distortion))
    image player happy chair hands = ConditionSwitch("persistent.performance_mode == True", "player happy chair hands p", "persistent.performance_mode == False", At("player happy chair hands p", distortion))
    image player happy leaving hand offer = ConditionSwitch("persistent.performance_mode == True", "player happy leaving hand offer p", "persistent.performance_mode == False", At("player happy leaving hand offer p", distortion))
    image player happy shadow hands = ConditionSwitch("persistent.performance_mode == True", "player happy shadow hands p", "persistent.performance_mode == False", At("player happy shadow hands p", distortion))

    image shadows happy neutral = ConditionSwitch("happy_torches == 4", "shadow happy 4", "happy_torches == 3", "shadow happy 3", "happy_torches == 2", "shadow happy 2", "happy_torches == 1", "shadow happy 1", "happy_torches == 0", "emptyimage")


    image shadows happy smile = ConditionSwitch("happy_torches == 4", "shadow happy 4 smile", "happy_torches == 3", "shadow happy 3 smile", "happy_torches == 2", "shadow happy 2 smile", "happy_torches < 2", "emptyimage")


    image shadow happy 2 smile:
        "shadow happy 2_1 smile"
        0.1
        "shadow happy 2_2 smile"
        0.1
        "shadow happy 2_3 smile"
        0.1
        "shadow happy 2_2 smile"
        0.1
        "shadow happy 2_1 smile"
        0.1
        "shadow happy 2_3 smile"
        0.1
        "shadow happy 2_1 smile"
        0.1
        "shadow happy 2_2 smile"
        0.1
        "shadow happy 2_3 smile"
        0.1
        "shadow happy 2_1 smile"
        0.1
        "shadow happy 2_2 smile"
        0.1
        "shadow happy 2_3 smile"
        0.1
        "shadow happy 2_2 smile"
        0.1
        repeat


    image shadow happy 3 smile:
        "shadow happy 3_1 smile"
        0.1
        "shadow happy 3_2 smile"
        0.1
        "shadow happy 3_3 smile"
        0.1
        "shadow happy 3_2 smile"
        0.1
        "shadow happy 3_1 smile"
        0.1
        "shadow happy 3_3 smile"
        0.1
        "shadow happy 3_1 smile"
        0.1
        "shadow happy 3_2 smile"
        0.1
        "shadow happy 3_3 smile"
        0.1
        "shadow happy 3_1 smile"
        0.1
        "shadow happy 3_2 smile"
        0.1
        "shadow happy 3_3 smile"
        0.1
        "shadow happy 3_2 smile"
        0.1
        repeat


    image shadow happy 4 smile:
        "shadow happy 4_1 smile"
        0.1
        "shadow happy 4_2 smile"
        0.1
        "shadow happy 4_3 smile"
        0.1
        "shadow happy 4_2 smile"
        0.1
        "shadow happy 4_1 smile"
        0.1
        "shadow happy 4_3 smile"
        0.1
        "shadow happy 4_1 smile"
        0.1
        "shadow happy 4_2 smile"
        0.1
        "shadow happy 4_3 smile"
        0.1
        "shadow happy 4_1 smile"
        0.1
        "shadow happy 4_2 smile"
        0.1
        "shadow happy 4_3 smile"
        0.1
        "shadow happy 4_2 smile"
        0.1
        repeat

    image shadows set:
        "shadows happy neutral"
        0.125
        "shadow happy table 1"
        0.125
        "shadow happy table 2"
        0.125
        "shadow happy table 3"
        0.125
        "shadow happy table 4"
        0.10
        "shadow happy table 3"
        0.10
        "shadow happy table 2"
        0.1
        "shadow happy table 1"
        0.1
        "shadows happy neutral"

    image shadow happy table 1 = ConditionSwitch("persistent.performance_mode == True", "shadow happy table 1 p", "persistent.performance_mode == False", At("shadow happy table 1 p", strongwarp))
    image shadow happy table 2 = ConditionSwitch("persistent.performance_mode == True", "shadow happy table 2 p", "persistent.performance_mode == False", At("shadow happy table 2 p", strongwarp))
    image shadow happy table 3 = ConditionSwitch("persistent.performance_mode == True", "shadow happy table 3 p", "persistent.performance_mode == False", At("shadow happy table 3 p", strongwarp))
    image shadow happy table 4 = ConditionSwitch("persistent.performance_mode == True", "shadow happy table 4 p", "persistent.performance_mode == False", At("shadow happy table 4 p", strongwarp))

    image shadow happy 1:
        "shadow happy 1_1 neutral"
        0.1
        "shadow happy 1_2 neutral"
        0.1
        "shadow happy 1_3 neutral"
        0.1
        "shadow happy 1_2 neutral"
        0.1
        "shadow happy 1_1 neutral"
        0.1
        "shadow happy 1_3 neutral"
        0.1
        "shadow happy 1_1 neutral"
        0.1
        "shadow happy 1_2 neutral"
        0.1
        "shadow happy 1_3 neutral"
        0.1
        "shadow happy 1_1 neutral"
        0.1
        "shadow happy 1_2 neutral"
        0.1
        "shadow happy 1_3 neutral"
        0.1
        "shadow happy 1_2 neutral"
        0.1
        repeat

    image shadow happy 2:
        "shadow happy 2_1 neutral"
        0.1
        "shadow happy 2_2 neutral"
        0.1
        "shadow happy 2_3 neutral"
        0.1
        "shadow happy 2_2 neutral"
        0.1
        "shadow happy 2_1 neutral"
        0.1
        "shadow happy 2_3 neutral"
        0.1
        "shadow happy 2_1 neutral"
        0.1
        "shadow happy 2_2 neutral"
        0.1
        "shadow happy 2_3 neutral"
        0.1
        "shadow happy 2_1 neutral"
        0.1
        "shadow happy 2_2 neutral"
        0.1
        "shadow happy 2_3 neutral"
        0.1
        "shadow happy 2_2 neutral"
        0.1
        repeat

    image shadow happy 3:
        "shadow happy 3_1 neutral"
        0.1
        "shadow happy 3_2 neutral"
        0.1
        "shadow happy 3_3 neutral"
        0.1
        "shadow happy 3_2 neutral"
        0.1
        "shadow happy 3_1 neutral"
        0.1
        "shadow happy 3_3 neutral"
        0.1
        "shadow happy 3_1 neutral"
        0.1
        "shadow happy 3_2 neutral"
        0.1
        "shadow happy 3_3 neutral"
        0.1
        "shadow happy 3_1 neutral"
        0.1
        "shadow happy 3_2 neutral"
        0.1
        "shadow happy 3_3 neutral"
        0.1
        "shadow happy 3_2 neutral"
        0.1
        repeat

    image shadow happy 4:
        "shadow happy 4_1 neutral"
        0.1
        "shadow happy 4_2 neutral"
        0.1
        "shadow happy 4_3 neutral"
        0.1
        "shadow happy 4_2 neutral"
        0.1
        "shadow happy 4_1 neutral"
        0.1
        "shadow happy 4_3 neutral"
        0.1
        "shadow happy 4_1 neutral"
        0.1
        "shadow happy 4_2 neutral"
        0.1
        "shadow happy 4_3 neutral"
        0.1
        "shadow happy 4_1 neutral"
        0.1
        "shadow happy 4_2 neutral"
        0.1
        "shadow happy 4_3 neutral"
        0.1
        "shadow happy 4_2 neutral"
        0.1
        repeat


## EXTRAS

    image food happy set 2 = ConditionSwitch("persistent.performance_mode == True", "food happy set 2 p", "persistent.performance_mode == False", At("food happy set 2 p", distortion))
    image food happy set 3 = ConditionSwitch("persistent.performance_mode == True", "food happy set 3 p", "persistent.performance_mode == False", At("food happy set 3 p", distortion))
    image happy t shadow tight sad = ConditionSwitch("persistent.performance_mode == True", "happy t shadow tight sad p", "persistent.performance_mode == False", At("happy t shadow tight sad p", distortion))
    image happy t shadow tight talk quiet = ConditionSwitch("persistent.performance_mode == True", "happy t shadow tight talk quiet p", "persistent.performance_mode == False", At("happy t shadow tight talk quiet p", distortion))
    image happy t shadow tight talk = ConditionSwitch("persistent.performance_mode == True", "happy t shadow tight talk p", "persistent.performance_mode == False", At("happy t shadow tight talk p", distortion))
    image happy t shadow tight = ConditionSwitch("persistent.performance_mode == True", "happy t shadow tight p", "persistent.performance_mode == False", At("happy t shadow tight p", distortion))
    image quiet damsel unfurl = ConditionSwitch("persistent.performance_mode == True", "quiet damsel unfurl p", "persistent.performance_mode == False", At("quiet damsel unfurl p", distortion))


    image shadow happy 1_1 neutral = ConditionSwitch("persistent.performance_mode == True", "shadow happy 1_1 neutral p", "persistent.performance_mode == False", At("shadow happy 1_1 neutral p", distortion))
    image shadow happy 1_2 neutral = ConditionSwitch("persistent.performance_mode == True", "shadow happy 1_2 neutral p", "persistent.performance_mode == False", At("shadow happy 1_2 neutral p", distortion))
    image shadow happy 1_3 neutral = ConditionSwitch("persistent.performance_mode == True", "shadow happy 1_3 neutral p", "persistent.performance_mode == False", At("shadow happy 1_3 neutral p", distortion))

    image shadow happy 2_1 neutral = ConditionSwitch("persistent.performance_mode == True", "shadow happy 2_1 neutral p", "persistent.performance_mode == False", At("shadow happy 2_1 neutral p", distortion))
    image shadow happy 2_2 neutral = ConditionSwitch("persistent.performance_mode == True", "shadow happy 2_2 neutral p", "persistent.performance_mode == False", At("shadow happy 2_2 neutral p", distortion))
    image shadow happy 2_3 neutral = ConditionSwitch("persistent.performance_mode == True", "shadow happy 2_3 neutral p", "persistent.performance_mode == False", At("shadow happy 2_3 neutral p", distortion))


    image shadow happy 2_1 smile = ConditionSwitch("persistent.performance_mode == True", "shadow happy 2_1 smile p", "persistent.performance_mode == False", At("shadow happy 2_1 smile p", distortion))
    image shadow happy 2_2 smile = ConditionSwitch("persistent.performance_mode == True", "shadow happy 2_2 smile p", "persistent.performance_mode == False", At("shadow happy 2_2 smile p", distortion))
    image shadow happy 2_3 smile = ConditionSwitch("persistent.performance_mode == True", "shadow happy 2_3 smile p", "persistent.performance_mode == False", At("shadow happy 2_3 smile p", distortion))


    image shadow happy 4_1 neutral = ConditionSwitch("persistent.performance_mode == True", "shadow happy 4_1 neutral p", "persistent.performance_mode == False", At("shadow happy 4_1 neutral p", distortion))
    image shadow happy 4_1 smile = ConditionSwitch("persistent.performance_mode == True", "shadow happy 4_1 smile p", "persistent.performance_mode == False", At("shadow happy 4_1 smile p", distortion))
    image shadow happy 4_2 neutral = ConditionSwitch("persistent.performance_mode == True", "shadow happy 4_2 neutral p", "persistent.performance_mode == False", At("shadow happy 4_2 neutral p", distortion))
    image shadow happy 4_2 smile = ConditionSwitch("persistent.performance_mode == True", "shadow happy 4_2 smile p", "persistent.performance_mode == False", At("shadow happy 4_2 smile p", distortion))
    image shadow happy 4_3 neutral = ConditionSwitch("persistent.performance_mode == True", "shadow happy 4_3 neutral p", "persistent.performance_mode == False", At("shadow happy 4_3 neutral p", distortion))
    image shadow happy 4_3 smile = ConditionSwitch("persistent.performance_mode == True", "shadow happy 4_3 smile p", "persistent.performance_mode == False", At("shadow happy 4_3 smile p", distortion))
    image shadow happy 3_1 neutral = ConditionSwitch("persistent.performance_mode == True", "shadow happy 3_1 neutral p", "persistent.performance_mode == False", At("shadow happy 3_1 neutral p", distortion))
    image shadow happy 3_1 smile = ConditionSwitch("persistent.performance_mode == True", "shadow happy 3_1 smile p", "persistent.performance_mode == False", At("shadow happy 3_1 smile p", distortion))
    image shadow happy 3_2 neutral = ConditionSwitch("persistent.performance_mode == True", "shadow happy 3_2 neutral p", "persistent.performance_mode == False", At("shadow happy 3_2 neutral p", distortion))
    image shadow happy 3_2 smile = ConditionSwitch("persistent.performance_mode == True", "shadow happy 3_2 smile p", "persistent.performance_mode == False", At("shadow happy 3_2 smile p", distortion))
    image shadow happy 3_3 neutral = ConditionSwitch("persistent.performance_mode == True", "shadow happy 3_3 neutral p", "persistent.performance_mode == False", At("shadow happy 3_3 neutral p", distortion))
    image shadow happy 3_3 smile = ConditionSwitch("persistent.performance_mode == True", "shadow happy 3_3 smile p", "persistent.performance_mode == False", At("shadow happy 3_3 smile p", distortion))
    image shadow happy 4_1 neutral = ConditionSwitch("persistent.performance_mode == True", "shadow happy 4_1 neutral p", "persistent.performance_mode == False", At("shadow happy 4_1 neutral p", distortion))
    image shadow happy 4_1 smile = ConditionSwitch("persistent.performance_mode == True", "shadow happy 4_1 smile p", "persistent.performance_mode == False", At("shadow happy 4_1 smile p", distortion))
    image shadow happy 4_2 neutral = ConditionSwitch("persistent.performance_mode == True", "shadow happy 4_2 neutral p", "persistent.performance_mode == False", At("shadow happy 4_2 neutral p", distortion))
    image shadow happy 4_2 smile = ConditionSwitch("persistent.performance_mode == True", "shadow happy 4_2 smile p", "persistent.performance_mode == False", At("shadow happy 4_2 smile p", distortion))
    image shadow happy 4_3 neutral = ConditionSwitch("persistent.performance_mode == True", "shadow happy 4_3 neutral p", "persistent.performance_mode == False", At("shadow happy 4_3 neutral p", distortion))
    image shadow happy 4_3 smile = ConditionSwitch("persistent.performance_mode == True", "shadow happy 4_3 smile p", "persistent.performance_mode == False", At("shadow happy 4_3 smile p", distortion))


    image shadows happy grab = ConditionSwitch("happy_torches >= 1", "shadows happy grab anim", "happy_torches == 0", "emptyimage")
    image shadows happy grab anim:
        "shadow happy grab 1"
        0.1
        "shadow happy grab 2"
        0.1
        "shadow happy grab 3"
        0.1
        repeat

    image shadow happy grab 1 = ConditionSwitch("persistent.performance_mode == True", "shadow happy grab 1 p", "persistent.performance_mode == False", At("shadow happy grab 1 p", distortion))
    image shadow happy grab 2 = ConditionSwitch("persistent.performance_mode == True", "shadow happy grab 2 p", "persistent.performance_mode == False", At("shadow happy grab 2 p", distortion))
    image shadow happy grab 3 = ConditionSwitch("persistent.performance_mode == True", "shadow happy grab 3 p", "persistent.performance_mode == False", At("shadow happy grab 3 p", distortion))
