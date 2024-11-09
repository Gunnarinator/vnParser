label pristine_climax_images:

    $ quick_menu = True
    show farback quiet onlayer farback at Position(ypos=1125)
    show back awakening onlayer back at Position(ypos=1125)
    show midground awakening onlayer front at Position(ypos=1125)
    show hair awakened onlayer front at Position(ypos=1125)
    show dress felina onlayer front at Position(ypos=1125)
    show shifting smile onlayer front at Position(ypos=1125)
    with Dissolve(1.5)
    #voice "audio/voices/felina/start/1b.flac"
    #mound "The first chains of our delusion have fallen, and have brought us closer to the unvarnished truth of absolute reality.\n"
    voice "audio/voices/felina/start/1.flac"
    show shifting smile talk onlayer front at Position(ypos=1125)
    with dissolve
    mound "I can finally see you, and you can finally see me.\n"
    play secondary "audio/_pristine/sfx/shifty_horror_sfx.flac"
    #play audio "audio/_pristine/sfx/shifty_move.flac"

    play secondary "audio/_pristine/sfx/shifty_crawl.flac"
    play audio "audio/_pristine/sfx/shifty_move.flac"
    hide hair onlayer front
    hide dress onlayer front
    hide shifting onlayer front
    show farback quiet onlayer farback at shakeshort
    show back awakening onlayer back at shakeshort
    show midground awakening onlayer front at shakeshort
    if previous_transform != "fierce":
        $ previous_transform = "fierce"
        show shifting fierce onlayer front at shakeshort, Position(ypos=1125)
        show pop fury onlayer inyourface at shakeshort, Position(ypos=1125)
    else:
        show shifting fierce onlayer front at flip, shakeshort, Position(ypos=1125)
        show pop fury onlayer inyourface at flip, shakeshort, Position(ypos=1125)
    with Dissolve(0.25)
    $ renpy.pause(1.3)
    show fight adversary onlayer inyourface at Position(ypos=1125)
    truth "this is a test"
    hide pop onlayer inyourface
    hide shifting onlayer front
    hide fight onlayer inyourface
    show farback quiet onlayer farback at Position(ypos=1125)
    show back awakening onlayer back at Position(ypos=1125)
    show midground awakening onlayer front at Position(ypos=1125)
    show hair awakened onlayer front at Position(ypos=1125)
    show dress felina onlayer front at Position(ypos=1125)
    show shifting smile onlayer front at Position(ypos=1125)
    show felina adversary2 onlayer inyourface at Position(ypos=1125)
    with Dissolve(1.0)
    truth "this is also a test"
    play secondary "audio/_pristine/sfx/shifty_crawl.flac"
    play audio "audio/_pristine/sfx/shifty_move.flac"
    hide felina onlayer inyourface
    hide hair onlayer front
    hide dress onlayer front
    hide shifting onlayer front
    show farback quiet onlayer farback at shakeshort
    show back awakening onlayer back at shakeshort
    show midground awakening onlayer front at shakeshort
    if previous_transform != "fierce":
        $ previous_transform = "fierce"
        show shifting fierce onlayer front at shakeshort, Position(ypos=1125)
        show pop fury onlayer inyourface at shakeshort, Position(ypos=1125)
    else:
        show shifting fierce onlayer front at flip, shakeshort, Position(ypos=1125)
        show pop fury onlayer inyourface at flip, shakeshort, Position(ypos=1125)
    with Dissolve(0.25)
    $ renpy.pause(1.3)
    show fight adversary onlayer inyourface at Position(ypos=1125)
    truth "this is a test"


    hide fight onlayer inyourface
    hide shifting onlayer front
    hide pop onlayer inyourface
    show farback quiet onlayer farback at Position(ypos=1125)
    show back awakening onlayer back at Position(ypos=1125)
    show midground awakening onlayer front at Position(ypos=1125)
    show hair awakened onlayer front at Position(ypos=1125)
    show dress felina onlayer front at Position(ypos=1125)
    show shifting closed smile talk onlayer front at Position(ypos=1125)


    # FIERCE — Fury, Den, Beast, Eye of the Needle, sharp Razor
    play secondary "audio/_pristine/sfx/shifty_crawl.flac"
    play audio "audio/_pristine/sfx/shifty_move.flac"
    hide hair onlayer front
    hide dress onlayer front
    hide shifting onlayer front
    show farback quiet onlayer farback at shakeshort
    show back awakening onlayer back at shakeshort
    show midground awakening onlayer front at shakeshort
    if previous_transform != "fierce":
        $ previous_transform = "fierce"
        show shifting fierce onlayer front at shakeshort, Position(ypos=1125)
        show pop fury onlayer inyourface at shakeshort, Position(ypos=1125)
    else:
        $ previous_transform = "fierceflip"
        show shifting fierce onlayer front at flip, shakeshort, Position(ypos=1125)
        show pop fury flip onlayer inyourface at shakeshort, Position(ypos=1125)
    with Dissolve(0.25)
    $ renpy.pause(1.3)

    # HANDS — Stranger, Prisoner (both head and no head), Wild, heart Razor, Apotheosis
    play secondary "audio/_pristine/sfx/shifty_hands.flac"
    play audio "audio/_pristine/sfx/shifty_move.flac"
    hide hair onlayer front
    hide dress onlayer front
    hide shifting onlayer front
    show farback quiet onlayer farback at shakeshort
    show back awakening onlayer back at shakeshort
    show midground awakening onlayer front at shakeshort
    if previous_transform != "hands":
        $ previous_transform = "hands"
        show shifting hands onlayer front at shakeshort, Position(ypos=1125)
        show pop wild onlayer inyourface at shakeshort, Position(ypos=1125)
    else:
        $ previous_transform = "handsflip"
        show shifting hands onlayer front at flip, shakeshort, Position(ypos=1125)
        show pop wild onlayer inyourface at flip, shakeshort, Position(ypos=1125)
    with Dissolve(0.25)
    $ renpy.pause(1.90)

    # DANCE — Witch, Thorn, Damsel, Adversary, Tower
    play secondary "audio/_pristine/sfx/shifty_dance.flac"
    play audio "audio/_pristine/sfx/shifty_move.flac"
    hide hair onlayer front
    hide dress onlayer front
    hide shifting onlayer front
    show farback quiet onlayer farback at shakeshort
    show back awakening onlayer back at shakeshort
    show midground awakening onlayer front at shakeshort
    if previous_transform != "dance":
        $ previous_transform = "dance"
        show shifting dance onlayer front at shakeshort, Position(ypos=1125)
        show pop wraith onlayer inyourface at shakeshort, Position(ypos=1125)
    else:
        $ previous_transform = "danceflip"
        show shifting dance onlayer front at flip, shakeshort, Position(ypos=1125)
        show pop wraith onlayer inyourface at flip, shakeshort, Position(ypos=1125)
    with Dissolve(0.25)
    $ renpy.pause(1.45)


    ## ZAP - Spectre; grey; derealized; wraith; nightmare; clarity
    play secondary "audio/_pristine/sfx/shifty_horror_sfx.flac"
    play audio "audio/_pristine/sfx/shifty_move.flac"
    hide hair onlayer front
    hide dress onlayer front
    hide shifting onlayer front
    show farback quiet onlayer farback at shakeshort
    show back awakening onlayer back at shakeshort
    show midground awakening onlayer front at shakeshort
    if previous_transform != "horror":
        $ previous_transform = "horror"
        show shifting horror onlayer front at shakeshort, Position(ypos=1125)
        show pop wraith onlayer inyourface at shakeshort, Position(ypos=1125)
    else:
        $ previous_transform = "horrorflip"
        show shifting horror onlayer front at flip, shakeshort, Position(ypos=1125)
        show pop wraith onlayer inyourface at flip, shakeshort, Position(ypos=1125)
    with Dissolve(0.25)
    $ renpy.pause(4.2)



    #play audio "audio/final/Adversary_ABackAndForth_1.flac"
    show fight adversary onlayer inyourface at Position(ypos=1125)
    mounds "The sensation of bleeding and sweating and breaking and mending and dying and living comes back in vivid color. A past that is also present. A pain that is everything and yet nothing at all.\n"
    voice "audio/voices/felina/fight/adv2.flac"
    hide fight onlayer inyourface
    hide shifting onlayer front
    show hair awakened onlayer front at Position(ypos=1125)
    show dress felina onlayer front at Position(ypos=1125)
    show shifting smile talk onlayer front at Position(ypos=1125)
    show felina adversary2 onlayer inyourface
    with dissolve
    mound "This is a test final line.\n"

    # records previous animation; can check to see if about to play a duplicate anim, and if so, flips on the y axis
    default previous_transform = "none"

    image shifting horror = ConditionSwitch("persistent.flickering == True", "shifting horror movie", "persistent.performance_mode == False", At("shifting horror anim", distortion), "persistent.performance_mode == True", "shifting horror anim")

    image ascension intro:
        "ascension 1"
        0.1
        "ascension 2"
        0.1
        "ascension 3"
        0.1
        "ascension 4"
        0.1
        "ascension 5"
        0.1
        "ascension 6"
        0.1
        "ascension 7"
        0.1
        "ascension 8"
        0.1
        "ascension 9"
        0.1
        "ascension 10"
        0.1
        "ascension 11"
        0.1
        "ascension 12"
        0.1
        "ascension 13"
        0.1
        "ascension 14"
        0.1
        "ascension 15"
        0.1
        "ascension 16"
        0.1
        "ascension 17"
        0.1
        "ascension 18"
        0.1
        "ascension 19"
        0.1
        "ascension 20"
        0.1
        "ascension 21"
        0.1
        "ascension 22"
        0.1
        "ascension 23"
        0.1
        "ascension 24"
        0.1
        "ascension 25"
        0.1
        "ascension 26"
        0.1
        "ascension 27"
        0.12
        "ascension loop1"
        0.12
        "ascension loop2"
        0.12
        "ascension loop3"
        0.12
        "ascension loop4"
        0.12
        "ascension loop1"
        0.12
        "ascension loop2"
        0.12
        "ascension loop3"
        0.12
        "ascension loop4"
        0.12
        "ascension loop1"
        0.12
        "ascension loop2"
        0.12
        "ascension loop3"
        0.12
        "ascension loop4"
        0.12
        "ascension loop1"
        0.12
        "ascension loop2"
        0.12
        "ascension loop3"
        0.12
        "ascension loop4"
        0.12
        "ascension loop1"
        0.12
        "ascension loop2"
        0.12
        "ascension loop3"
        0.12
        "ascension loop4"
        0.12
        "ascension loop1"
        0.12
        "ascension loop2"
        0.12
        "ascension loop3"
        0.12
        "ascension loop4"
        0.12
        "ascension loop1"
        0.12
        "ascension loop2"
        0.12
        "ascension loop3"
        0.12
        "ascension loop4"
        0.12
        "ascension loop1"
        0.12
        "ascension loop2"
        0.12
        "ascension loop3"
        0.12
        "ascension loop4"
        0.12
        "ascension loop1"
        0.12
        "ascension loop2"
        0.12
        "ascension loop3"
        0.12
        "ascension loop4"
        0.12

    image ascension loop:
        "ascension loop1"
        0.12
        "ascension loop2"
        0.12
        "ascension loop3"
        0.12
        "ascension loop4"
        0.12
        repeat

    image shifting horror movie = Movie(play="images/_pristine/_climax/animation/shifty_horror.webm", side_mask=True)


    image shifting dance = Movie(play="images/_pristine/_climax/animation/shifty_dance.webm", side_mask=True, loop = False, start_image = "shifty_dance_final1")
    image shifting fierce = Movie(play="images/_pristine/_climax/animation/shifty_fierce.webm", side_mask=True, loop = False, start_image = "shifty_fierce_anim1")
    image shifting hands = Movie(play="images/_pristine/_climax/animation/shifty_hands.webm", side_mask=True, loop = False, start_image = "shifty_hands_anim1")

    image shifting horror anim:
        "shifty horror1 p"
        0.6
        "shifty horror2 p"
        0.45
        "shifty horror3 p"
        1.0
        "shifty horror4 p"
        0.9
        "shifty horror5 p"
        0.83
        "shifty horror6 p"

    image shifting dancemanual:
        "shifty_dance_final1"
        0.1
        "shifty_dance_final2"
        0.1
        "shifty_dance_final3"
        0.1
        "shifty_dance_final4"
        0.1
        "shifty_dance_final5"
        0.1
        "shifty_dance_final6"
        0.1
        "shifty_dance_final7"
        0.1
        "shifty_dance_final8"
        0.1
        "shifty_dance_final9"
        0.1
        "shifty_dance_final10"
        0.1
        "shifty_dance_final11"
        0.1
        "shifty_dance_final12"
        0.1
        "shifty_dance_final13"
        0.1
        "shifty_dance_final14"
        0.1
        "shifty_dance_final15"
        0.1
        "shifty_dance_final16"


    image shifting fiercemanual:
        "shifty_fierce_anim1"
        0.1
        "shifty_fierce_anim2"
        0.1
        "shifty_fierce_anim3"
        0.1
        "shifty_fierce_anim4"
        0.1
        "shifty_fierce_anim5"
        0.1
        "shifty_fierce_anim6"
        0.1
        "shifty_fierce_anim7"
        0.1
        "shifty_fierce_anim8"
        0.1
        "shifty_fierce_anim9"
        0.1
        "shifty_fierce_anim10"
        0.1
        "shifty_fierce_anim11"
        0.1
        "shifty_fierce_anim12"
        0.1
        "shifty_fierce_anim13"
        0.1
        "shifty_fierce_anim14"


    image shifting handsmanual:
        "shifty_hands_anim1"
        0.1
        "shifty_hands_anim2"
        0.1
        "shifty_hands_anim3"
        0.1
        "shifty_hands_anim4"
        0.1
        "shifty_hands_anim5"
        0.1
        "shifty_hands_anim6"
        0.1
        "shifty_hands_anim7"
        0.1
        "shifty_hands_anim8"
        0.1
        "shifty_hands_anim9"
        0.1
        "shifty_hands_anim10"
        0.1
        "shifty_hands_anim11"
        0.1
        "shifty_hands_anim12"
        0.1
        "shifty_hands_anim13"
        0.1
        "shifty_hands_anim14"
        0.1
        "shifty_hands_anim15"
        0.1
        "shifty_hands_anim16"
        0.1
        "shifty_hands_anim17"
        0.1
        "shifty_hands_anim18"
        0.1
        "shifty_hands_anim19"
        0.1
        "shifty_hands_anim20"

    image pop adversary = ConditionSwitch("persistent.performance_mode == True", "adversary pop anim", "persistent.performance_mode == False", At("adversary pop anim", distortion))
    image adversary pop anim:
        1.3
        "adversary pop 1p"
        0.1
        "adversary pop 2p"
        0.1
        "adversary pop 3p"
        0.1
        "adversary pop 4p"

    image pop thorn = ConditionSwitch("persistent.performance_mode == True", "thorn pop anim", "persistent.performance_mode == False", At("thorn pop anim", distortion))
    image thorn pop anim:
        1.3
        "thorn pop 1p"
        0.1
        "thorn pop 2p"
        0.1
        "thorn pop 3p"
        0.1
        "thorn pop 4p"

    image pop witch = ConditionSwitch("persistent.performance_mode == True", "witch pop anim", "persistent.performance_mode == False", At("witch pop anim", distortion))
    image witch pop anim:
        1.3
        "witch pop 1p"
        0.1
        "witch pop 2p"
        0.1
        "witch pop 3p"
        0.1
        "witch pop 4p"

    image pop tower = ConditionSwitch("persistent.performance_mode == True", "tower pop anim", "persistent.performance_mode == False", At("tower pop anim", distortion))
    image tower pop anim:
        1.3
        "tower pop 1p"
        0.1
        "tower pop 2p"
        0.1
        "tower pop 3p"
        0.1
        "tower pop 4p"


    image pop damsel = ConditionSwitch("persistent.performance_mode == True", "damsel pop anim", "persistent.performance_mode == False", At("damsel pop anim", distortion))
    image damsel pop anim:
        1.3
        "damsel pop 1p"
        0.1
        "damsel pop 2p"
        0.1
        "damsel pop 3p"
        0.1
        "damsel pop 4p"

    image pop apotheosis = ConditionSwitch("persistent.performance_mode == True", "apotheosis pop anim", "persistent.performance_mode == False", At("apotheosis pop anim", distortion))
    image apotheosis pop anim:
        1.7
        "apotheosis pop 1p"
        0.1
        "apotheosis pop 2p"
        0.1
        "apotheosis pop 3p"
        0.1
        "apotheosis pop 4p"

    image pop stranger = ConditionSwitch("persistent.performance_mode == True", "stranger pop anim", "persistent.performance_mode == False", At("stranger pop anim", distortion))
    image stranger pop anim:
        1.7
        "stranger pop 1p"
        0.1
        "stranger pop 2p"
        0.1
        "stranger pop 3p"
        0.1
        "stranger pop 4p"

    image pop razor heart = ConditionSwitch("persistent.performance_mode == True", "razor heart pop anim", "persistent.performance_mode == False", At("razor heart pop anim", distortion))
    image razor heart pop anim:
        1.7
        "razor heart pop 1p"
        0.1
        "razor heart pop 2p"
        0.1
        "razor heart pop 3p"
        0.1
        "razor heart pop 4p"

    image pop razor sharp = ConditionSwitch("persistent.performance_mode == True", "razor sharp pop anim", "persistent.performance_mode == False", At("razor sharp pop anim", distortion))
    image razor sharp pop anim:
        1.1
        "razor sharp pop 1p"
        0.1
        "razor sharp pop 2p"
        0.1
        "razor sharp pop 3p"
        0.1
        "razor sharp pop 4p"

    image pop prisoner chain = ConditionSwitch("persistent.performance_mode == True", "prisoner chain pop anim", "persistent.performance_mode == False", At("prisoner chain pop anim", distortion))
    image prisoner chain pop anim:
        1.7
        "prisoner chain pop 1p"
        0.1
        "prisoner chain pop 2p"
        0.1
        "prisoner chain pop 3p"
        0.1
        "prisoner chain pop 4p"

    image pop prisoner head = ConditionSwitch("persistent.performance_mode == True", "prisoner head pop anim", "persistent.performance_mode == False", At("prisoner head pop anim", distortion))
    image prisoner head pop anim:
        1.7
        "prisoner head pop 1p"
        0.1
        "prisoner head pop 2p"
        0.1
        "prisoner head pop 3p"
        0.1
        "prisoner head pop 4p"

    image pop wild = ConditionSwitch("wild_end == 'joined'", "pop networked wild", "wild_end != 'joined'", "pop wounded wild")

    image pop networked wild = ConditionSwitch("persistent.performance_mode == True", "networked wild pop anim", "persistent.performance_mode == False", At("networked wild pop anim", distortion))
    image networked wild pop anim:
        1.7
        "networked wild pop 1p"
        0.1
        "networked wild pop 2p"
        0.1
        "networked wild pop 3p"
        0.1
        "networked wild pop 4p"

    image pop wounded wild = ConditionSwitch("persistent.performance_mode == True", "wounded wild pop anim", "persistent.performance_mode == False", At("wounded wild pop anim", distortion))
    image wounded wild pop anim:
        1.7
        "wounded wild pop 1p"
        0.1
        "wounded wild pop 2p"
        0.1
        "wounded wild pop 3p"
        0.1
        "wounded wild pop 4p"

    image pop beast = ConditionSwitch("persistent.performance_mode == True", "beast pop anim", "persistent.performance_mode == False", At("beast pop anim", distortion))
    image beast pop anim:
        1.1
        "beast pop 1p"
        0.1
        "beast pop 2p"
        0.1
        "beast pop 3p"
        0.1
        "beast pop 4p"

    image pop den = ConditionSwitch("persistent.performance_mode == True", "den pop anim", "persistent.performance_mode == False", At("den pop anim", distortion))
    image den pop anim:
        1.1
        "den pop 1p"
        0.1
        "den pop 2p"
        0.1
        "den pop 3p"
        0.1
        "den pop 4p"



    image pop fury = ConditionSwitch("persistent.performance_mode == True", "fury pop anim", "persistent.performance_mode == False", At("fury pop anim", distortion))
    image fury pop anim:
        1.1
        "fury pop 1p"
        0.1
        "fury pop 2p"
        0.1
        "fury pop 3p"
        0.1
        "fury pop 4p"

    image pop needle = ConditionSwitch("persistent.performance_mode == True", "needle pop anim", "persistent.performance_mode == False", At("needle pop anim", distortion))
    image needle pop anim:
        1.1
        "needle pop 1p"
        0.1
        "needle pop 2p"
        0.1
        "needle pop 3p"
        0.1
        "needle pop 4p"

    image pop fury flip = ConditionSwitch("persistent.performance_mode == True", "fury flip pop anim", "persistent.performance_mode == False", At("fury flip pop anim", distortion))
    image fury flip pop anim:
        1.1
        "fury flip pop 1p"
        0.1
        "fury flip pop 2p"
        0.1
        "fury flip pop 3p"
        0.1
        "fury flip pop 4p"

    image pop wraith = ConditionSwitch("persistent.performance_mode == True", "wraith pop anim", "persistent.performance_mode == False", At("wraith pop anim", distortion))

    image wraith pop anim:
        2.95
        "wraith pop 1p"
        0.15
        "emptyimage"
        0.75
        "wraith pop 2p"

    image pop clarity = ConditionSwitch("persistent.performance_mode == True", "clarity pop anim", "persistent.performance_mode == False", At("clarity pop anim", distortion))

    image clarity pop anim:
        2.95
        "clarity pop 1p"
        0.15
        "emptyimage"
        0.75
        "clarity pop 2p"

    image pop nightmare = ConditionSwitch("persistent.performance_mode == True", "nightmare pop anim", "persistent.performance_mode == False", At("nightmare pop anim", distortion))

    image nightmare pop anim:
        2.95
        "nightmare pop 1p"
        0.15
        "emptyimage"
        0.75
        "nightmare pop 2p"

    image pop spectre = ConditionSwitch("persistent.performance_mode == True", "spectre pop anim", "persistent.performance_mode == False", At("spectre pop anim", distortion))

    image spectre pop anim:
        2.95
        "spectre pop 1p"
        0.15
        "emptyimage"
        0.75
        "spectre pop 2p"

    image pop dereal = ConditionSwitch("persistent.performance_mode == True", "dereal pop anim", "persistent.performance_mode == False", At("dereal pop anim", distortion))

    image dereal pop anim:
        2.95
        "dereal pop 1p"
        0.15
        "emptyimage"
        0.75
        "dereal pop 2p"


    image pop grey = ConditionSwitch("grey_end == 'burn'", "pop burned grey", "grey_end != 'burn'", "pop drowned grey")

    image pop burned grey = ConditionSwitch("persistent.performance_mode == True", "burned grey pop anim", "persistent.performance_mode == False", At("burned grey pop anim", distortion))

    image burned grey pop anim:
        2.95
        "burned grey pop 1p"
        0.15
        "emptyimage"
        0.75
        "burned grey pop 2p"

    image pop drowned grey = ConditionSwitch("persistent.performance_mode == True", "drowned grey pop anim", "persistent.performance_mode == False", At("drowned grey pop anim", distortion))

    image drowned grey pop anim:
        2.95
        "drowned grey pop 1p"
        0.15
        "emptyimage"
        0.75
        "drowned grey pop 2p"


    # PRISTINE CUT BEGINS HERE

    image felina cage 1 talk = ConditionSwitch("persistent.performance_mode == True", "awakened mound cage 1 talk p", "persistent.performance_mode == False", At("awakened mound cage 1 talk p", distortion))
    image felina cage 1 = ConditionSwitch("persistent.performance_mode == True", "awakened mound cage 1 p", "persistent.performance_mode == False", At("awakened mound cage 1 p", distortion))
    image felina cage 2 talk = ConditionSwitch("persistent.performance_mode == True", "awakened mound cage 2 talk p", "persistent.performance_mode == False", At("awakened mound cage 2 talk p", distortion))
    image felina cage 2 = ConditionSwitch("persistent.performance_mode == True", "awakened mound cage 2 p", "persistent.performance_mode == False", At("awakened mound cage 2 p", distortion))
    image felina cage 3 talk = ConditionSwitch("persistent.performance_mode == True", "awakened mound cage 3 talk p", "persistent.performance_mode == False", At("awakened mound cage 3 talk p", distortion))
    image felina cage 3 = ConditionSwitch("persistent.performance_mode == True", "awakened mound cage 3 p", "persistent.performance_mode == False", At("awakened mound cage 3 p", distortion))
    image felina furyheart 1 = ConditionSwitch("persistent.performance_mode == True", "awakened mound furyheart 1 p", "persistent.performance_mode == False", At("awakened mound furyheart 1 p", distortion))
    image felina furyheart 2 = ConditionSwitch("persistent.performance_mode == True", "awakened mound furyheart 2 p", "persistent.performance_mode == False", At("awakened mound furyheart 2 p", distortion))
    image felina furyheart 3 = ConditionSwitch("persistent.performance_mode == True", "awakened mound furyheart 3 p", "persistent.performance_mode == False", At("awakened mound furyheart 3 p", distortion))
    image felina happy 1 talk = ConditionSwitch("persistent.performance_mode == True", "awakened mound happy 1 talk p", "persistent.performance_mode == False", At("awakened mound happy 1 talk p", distortion))
    image felina happy 1 = ConditionSwitch("persistent.performance_mode == True", "awakened mound happy 1 p", "persistent.performance_mode == False", At("awakened mound happy 1 p", distortion))
    image felina happy 2 talk = ConditionSwitch("persistent.performance_mode == True", "awakened mound happy 2 talk p", "persistent.performance_mode == False", At("awakened mound happy 2 talk p", distortion))
    image felina happy 2 = ConditionSwitch("persistent.performance_mode == True", "awakened mound happy 2 p", "persistent.performance_mode == False", At("awakened mound happy 2 p", distortion))
    image felina happy 3 talk = ConditionSwitch("persistent.performance_mode == True", "awakened mound happy 3 talk p", "persistent.performance_mode == False", At("awakened mound happy 3 talk p", distortion))
    image felina happy 3 = ConditionSwitch("persistent.performance_mode == True", "awakened mound happy 3 p", "persistent.performance_mode == False", At("awakened mound happy 3 p", distortion))

    image fight happy dance = ConditionSwitch("persistent.performance_mode == True", "happy dance p", "persistent.performance_mode == False", At("happy dance p", distortion))
    image fight happy = ConditionSwitch("persistent.performance_mode == True", "happy p", "persistent.performance_mode == False", At("happy p", distortion))

    image fight cage armed = ConditionSwitch("persistent.performance_mode == True", "fight cage armed p", "persistent.performance_mode == False", At("fight cage armed p", distortion))
    image fight cage = ConditionSwitch("persistent.performance_mode == True", "fight cage p", "persistent.performance_mode == False", At("fight cage p", distortion))

    image mound cage neutral talk = ConditionSwitch("persistent.performance_mode == True", "mound cage neutral talk p", "persistent.performance_mode == False", At("mound cage neutral talk p", distortion))
    image mound cage neutral = ConditionSwitch("persistent.performance_mode == True", "mound cage neutral p", "persistent.performance_mode == False", At("mound cage neutral p", distortion))
    image mound cage pose talk = ConditionSwitch("persistent.performance_mode == True", "mound cage pose talk p", "persistent.performance_mode == False", At("mound cage pose talk p", distortion))
    image mound cage pose = ConditionSwitch("persistent.performance_mode == True", "mound cage pose p", "persistent.performance_mode == False", At("mound cage pose p", distortion))
    image mound cage shift talk = ConditionSwitch("persistent.performance_mode == True", "mound cage shift talk p", "persistent.performance_mode == False", At("mound cage shift talk p", distortion))
    image mound cage shift = ConditionSwitch("persistent.performance_mode == True", "mound cage shift p", "persistent.performance_mode == False", At("mound cage shift p", distortion))
    image mound d cage = ConditionSwitch("persistent.performance_mode == True", "mound d cage p", "persistent.performance_mode == False", At("mound d cage p", distortion))
    image mound d fury heart = ConditionSwitch("persistent.performance_mode == True", "mound d fury heart p", "persistent.performance_mode == False", At("mound d fury heart p", distortion))
    image mound d happy = ConditionSwitch("persistent.performance_mode == True", "mound d happy p", "persistent.performance_mode == False", At("mound d happy p", distortion))
    image mound d dragon = ConditionSwitch("persistent.performance_mode == True", "mound d dragon p", "persistent.performance_mode == False", At("mound d dragon p", distortion))


    image farback mound death 1 = ConditionSwitch("persistent.performance_mode == True", "mound death 1 bg ladies 1 p", "persistent.performance_mode == False", At("mound death 1 bg ladies 1 p", distortion))
    image bg mound death 1 = ConditionSwitch("persistent.performance_mode == True", "mound death 1 bg ladies 2 p", "persistent.performance_mode == False", At("mound death 1 bg ladies 2 p", distortion))
    image mid mound death 1 = ConditionSwitch("persistent.performance_mode == True", "mound death 1 bg p", "persistent.performance_mode == False", At("mound death 1 bg p", distortion))
    image fore mound death 1 = ConditionSwitch("persistent.performance_mode == True", "mound death 1 foreground p", "persistent.performance_mode == False", At("mound death 1 foreground p", distortion))
    image mound death 1 talk = ConditionSwitch("persistent.performance_mode == True", "mound death 1 midground talk p", "persistent.performance_mode == False", At("mound death 1 midground talk p", distortion))
    image mound death 1 = ConditionSwitch("persistent.performance_mode == True", "mound death 1 midground p", "persistent.performance_mode == False", At("mound death 1 midground p", distortion))


    image bg mound death 2 = ConditionSwitch("persistent.performance_mode == True", "mound death 2 bg p", "persistent.performance_mode == False", At("mound death 2 bg p", distortion))
    image mound death 2 = ConditionSwitch("persistent.performance_mode == True", "mound death 2 foreground p", "persistent.performance_mode == False", At("mound death 2 foreground p", distortion))


    image bg mound death 3 = ConditionSwitch("persistent.performance_mode == True", "mound death 3 bg ladies 1 p", "persistent.performance_mode == False", At("mound death 3 bg ladies 1 p", distortion))
    image farback mound death 3 = ConditionSwitch("persistent.performance_mode == True", "mound death 3 bg ladies 2 p", "persistent.performance_mode == False", At("mound death 3 bg ladies 2 p", distortion))
    image mid mound death 3 = ConditionSwitch("persistent.performance_mode == True", "mound death 3 bg p", "persistent.performance_mode == False", At("mound death 3 bg p", distortion))
    image fore mound death 3 = ConditionSwitch("persistent.performance_mode == True", "mound death 3 foreground p", "persistent.performance_mode == False", At("mound death 3 foreground p", distortion))
    image mound death 3 = ConditionSwitch("persistent.performance_mode == True", "mound death 3 midground p", "persistent.performance_mode == False", At("mound death 3 midground p", distortion))


    image farback mound death 4 = ConditionSwitch("persistent.performance_mode == True", "mound death 4 bg ladies 1 p", "persistent.performance_mode == False", At("mound death 4 bg ladies 1 p", distortion))
    image bg mound death 4 = ConditionSwitch("persistent.performance_mode == True", "mound death 4 bg ladies 2 p", "persistent.performance_mode == False", At("mound death 4 bg ladies 2 p", distortion))
    image mid mound death 4 = ConditionSwitch("persistent.performance_mode == True", "mound death 4 bg p", "persistent.performance_mode == False", At("mound death 4 bg p", distortion))
    image fore mound death 4 offer = ConditionSwitch("persistent.performance_mode == True", "mound death 4 foreground offer p", "persistent.performance_mode == False", At("mound death 4 foreground offer p", distortion))
    image mound death 4 defeat talk = ConditionSwitch("persistent.performance_mode == True", "mound death 4 midground defeat talk p", "persistent.performance_mode == False", At("mound death 4 midground defeat talk p", distortion))
    image mound death 4 defeat = ConditionSwitch("persistent.performance_mode == True", "mound death 4 midground defeat p", "persistent.performance_mode == False", At("mound death 4 midground defeat p", distortion))
    image mound death 4 determined = ConditionSwitch("persistent.performance_mode == True", "mound death 4 midground determined p", "persistent.performance_mode == False", At("mound death 4 midground determined p", distortion))
    image mound death 4 talk final = ConditionSwitch("persistent.performance_mode == True", "mound death 4 midground talk final p", "persistent.performance_mode == False", At("mound death 4 midground talk final p", distortion))

    image mound death 4 talk final smile = ConditionSwitch("persistent.performance_mode == True", "mound death 4 talk final smile p", "persistent.performance_mode == False", At("mound death 4 talk final smile p", distortion))


    image mound death begin = ConditionSwitch("persistent.performance_mode == True", "mound death begin p", "persistent.performance_mode == False", At("mound death begin p", distortion))
    image fore mound death begin = ConditionSwitch("persistent.performance_mode == True", "mound death begin mad foreground p", "persistent.performance_mode == False", At("mound death begin mad foreground p", distortion))
    image bg mound death offended talk = ConditionSwitch("persistent.performance_mode == True", "mound death offended talk bg ladies 1 p", "persistent.performance_mode == False", At("mound death offended talk bg ladies 1 p", distortion))
    image farback mound death offended talk = ConditionSwitch("persistent.performance_mode == True", "mound death offended talk bg ladies 2 p", "persistent.performance_mode == False", At("mound death offended talk bg ladies 2 p", distortion))
    image mid mound death offended talk = ConditionSwitch("persistent.performance_mode == True", "mound death offended talk bg p", "persistent.performance_mode == False", At("mound death offended talk bg p", distortion))
    image mound death offended talk = ConditionSwitch("persistent.performance_mode == True", "mound death offended talk p", "persistent.performance_mode == False", At("mound death offended talk p", distortion))


    image mound fury heart neutral = ConditionSwitch("persistent.performance_mode == True", "mound fury heart neutral p", "persistent.performance_mode == False", At("mound fury heart neutral p", distortion))
    image mound fury heart pose = ConditionSwitch("persistent.performance_mode == True", "mound fury heart pose p", "persistent.performance_mode == False", At("mound fury heart pose p", distortion))
    image mound fury heart shift = ConditionSwitch("persistent.performance_mode == True", "mound fury heart shift p", "persistent.performance_mode == False", At("mound fury heart shift p", distortion))
    image mound happy neutral talk = ConditionSwitch("persistent.performance_mode == True", "mound happy neutral talk p", "persistent.performance_mode == False", At("mound happy neutral talk p", distortion))
    image mound happy neutral = ConditionSwitch("persistent.performance_mode == True", "mound happy neutral p", "persistent.performance_mode == False", At("mound happy neutral p", distortion))
    image mound happy pose talk = ConditionSwitch("persistent.performance_mode == True", "mound happy pose talk p", "persistent.performance_mode == False", At("mound happy pose talk p", distortion))
    image mound happy pose = ConditionSwitch("persistent.performance_mode == True", "mound happy pose p", "persistent.performance_mode == False", At("mound happy pose p", distortion))
    image mound happy shift talk = ConditionSwitch("persistent.performance_mode == True", "mound happy shift talk p", "persistent.performance_mode == False", At("mound happy shift talk p", distortion))
    image mound happy shift = ConditionSwitch("persistent.performance_mode == True", "mound happy shift p", "persistent.performance_mode == False", At("mound happy shift p", distortion))
    image mound dragon neutral talk = ConditionSwitch("persistent.performance_mode == True", "mound dragon neutral talk p", "persistent.performance_mode == False", At("mound dragon neutral talk p", distortion))
    image mound dragon neutral = ConditionSwitch("persistent.performance_mode == True", "mound dragon neutral p", "persistent.performance_mode == False", At("mound dragon neutral p", distortion))
    image mound dragon pose talk = ConditionSwitch("persistent.performance_mode == True", "mound dragon pose talk p", "persistent.performance_mode == False", At("mound dragon pose talk p", distortion))
    image mound dragon pose = ConditionSwitch("persistent.performance_mode == True", "mound dragon pose p", "persistent.performance_mode == False", At("mound dragon pose p", distortion))
    image mound dragon shift talk = ConditionSwitch("persistent.performance_mode == True", "mound dragon shift talk p", "persistent.performance_mode == False", At("mound dragon shift talk p", distortion))
    image mound dragon shift = ConditionSwitch("persistent.performance_mode == True", "mound dragon shift p", "persistent.performance_mode == False", At("mound dragon shift p", distortion))

    # CAGE GETS THE HANDS

    image pop cage:
        1.7
        "cage pop 1"
        0.1
        "cage pop 2"
        0.1
        "cage pop 3"
        0.1
        "cage pop 4"


    image cage pop 1 = ConditionSwitch("persistent.performance_mode == True", "cage pop 1 p", "persistent.performance_mode == False", At("cage pop 1 p", distortion))
    image cage pop 2 = ConditionSwitch("persistent.performance_mode == True", "cage pop 2 p", "persistent.performance_mode == False", At("cage pop 2 p", distortion))
    image cage pop 3 = ConditionSwitch("persistent.performance_mode == True", "cage pop 3 p", "persistent.performance_mode == False", At("cage pop 3 p", distortion))
    image cage pop 4 = ConditionSwitch("persistent.performance_mode == True", "cage pop 4 p", "persistent.performance_mode == False", At("cage pop 4 p", distortion))


    # DRAGON GETS THE GHOST
    image pop dragon ghost:
        2.95
        "dragon pop 2"
        0.15
        "emptyimage"
        0.75
        "dragon pop 4"

    image pop dragon final = ConditionSwitch("dragon_end == 'abandon'", "pop dragon full", "dragon_end != 'abandon'", "pop dragon nohand")

    image pop dragon full:
        1.3
        "dragon normal pop 1"
        0.1
        "dragon normal pop 2"
        0.1
        "dragon normal pop 3"
        0.1
        "dragon normal pop 4"


    image dragon pop 1 = ConditionSwitch("persistent.performance_mode == True", "dragon pop 1 p", "persistent.performance_mode == False", At("dragon pop 1 p", distortion))
    image dragon pop 2 = ConditionSwitch("persistent.performance_mode == True", "dragon pop 2 p", "persistent.performance_mode == False", At("dragon pop 2 p", distortion))
    image dragon pop 3 = ConditionSwitch("persistent.performance_mode == True", "dragon pop 3 p", "persistent.performance_mode == False", At("dragon pop 3 p", distortion))
    image dragon pop 4 = ConditionSwitch("persistent.performance_mode == True", "dragon pop 4 p", "persistent.performance_mode == False", At("dragon pop 4 p", distortion))

    # FURY HEART GETS THE HANDS

    image pop furyheart:
        1.7
        "fury heart pop 1"
        0.1
        "fury heart pop 2"
        0.1
        "fury heart pop 3"
        0.1
        "fury heart pop 4"

    image fury heart pop 1 = ConditionSwitch("persistent.performance_mode == True", "fury heart pop 1 p", "persistent.performance_mode == False", At("fury heart pop 1 p", distortion))
    image fury heart pop 2 = ConditionSwitch("persistent.performance_mode == True", "fury heart pop 2 p", "persistent.performance_mode == False", At("fury heart pop 2 p", distortion))
    image fury heart pop 3 = ConditionSwitch("persistent.performance_mode == True", "fury heart pop 3 p", "persistent.performance_mode == False", At("fury heart pop 3 p", distortion))
    image fury heart pop 4 = ConditionSwitch("persistent.performance_mode == True", "fury heart pop 4 p", "persistent.performance_mode == False", At("fury heart pop 4 p", distortion))

    # IF YOU DANCE WITH HER YOU GET DANCE

    image pop happy dance:
        1.3
        "happy dance pop 1"
        0.1
        "happy dance pop 2"
        0.1
        "happy dance pop 3"
        0.1
        "happy dance pop 4"

    image pop happy hands:
        1.7
        "happy hands pop 1"
        0.1
        "happy hands pop 2"
        0.1
        "happy hands pop 3"
        0.1
        "happy hands pop 4"

    image happy dance pop 1 = ConditionSwitch("persistent.performance_mode == True", "happy dance pop 1 p", "persistent.performance_mode == False", At("happy dance pop 1 p", distortion))
    image happy dance pop 2 = ConditionSwitch("persistent.performance_mode == True", "happy dance pop 2 p", "persistent.performance_mode == False", At("happy dance pop 2 p", distortion))
    image happy dance pop 3 = ConditionSwitch("persistent.performance_mode == True", "happy dance pop 3 p", "persistent.performance_mode == False", At("happy dance pop 3 p", distortion))
    image happy dance pop 4 = ConditionSwitch("persistent.performance_mode == True", "happy dance pop 4 p", "persistent.performance_mode == False", At("happy dance pop 4 p", distortion))



    # OTHERWISE YOU GET HANDS
    image happy hands pop 1 = ConditionSwitch("persistent.performance_mode == True", "happy hands pop 1 p", "persistent.performance_mode == False", At("happy hands pop 1 p", distortion))
    image happy hands pop 2 = ConditionSwitch("persistent.performance_mode == True", "happy hands pop 2 p", "persistent.performance_mode == False", At("happy hands pop 2 p", distortion))
    image happy hands pop 3 = ConditionSwitch("persistent.performance_mode == True", "happy hands pop 3 p", "persistent.performance_mode == False", At("happy hands pop 3 p", distortion))
    image happy hands pop 4 = ConditionSwitch("persistent.performance_mode == True", "happy hands pop 4 p", "persistent.performance_mode == False", At("happy hands pop 4 p", distortion))



    image dragon normal pop 1 = ConditionSwitch("persistent.performance_mode == True", "dragon normal pop 1 p", "persistent.performance_mode == False", At("dragon normal pop 1 p", distortion))
    image dragon normal pop 2 = ConditionSwitch("persistent.performance_mode == True", "dragon normal pop 2 p", "persistent.performance_mode == False", At("dragon normal pop 2 p", distortion))
    image dragon normal pop 3 = ConditionSwitch("persistent.performance_mode == True", "dragon normal pop 3 p", "persistent.performance_mode == False", At("dragon normal pop 3 p", distortion))
    image dragon normal pop 4 = ConditionSwitch("persistent.performance_mode == True", "dragon normal pop 4 p", "persistent.performance_mode == False", At("dragon normal pop 4 p", distortion))

    image felina dragon 1 = ConditionSwitch("dragon_end == 'fusion'", "felina dragon1", "dragon_end == 'abandon'", "felina dragon normal1", "dragon_end == 'free'", "felina dragon nohand 1")
    image felina dragon 1 talk = ConditionSwitch("dragon_end == 'fusion'", "felina dragon1 talk", "dragon_end == 'abandon'", "felina dragon normal1 talk", "dragon_end == 'free'", "felina dragon nohand talk 1")
    image felina dragon 2 = ConditionSwitch("dragon_end == 'fusion'", "felina dragon2", "dragon_end == 'abandon'", "felina dragon normal2", "dragon_end == 'free'", "felina dragon nohand 2")
    image felina dragon 2 talk = ConditionSwitch("dragon_end == 'fusion'", "felina dragon2 talk", "dragon_end == 'abandon'", "felina dragon normal2 talk", "dragon_end == 'free'", "felina dragon nohand talk 2")
    image felina dragon 3 = ConditionSwitch("dragon_end == 'fusion'", "felina dragon3", "dragon_end == 'abandon'", "felina dragon normal3", "dragon_end == 'free'", "felina dragon normal3")
    image felina dragon 3 talk = ConditionSwitch("dragon_end == 'fusion'", "felina dragon3 talk", "dragon_end == 'abandon'", "felina dragon normal3 talk", "dragon_end == 'free'", "felina dragon normal3 talk")

    image felina dragon1 talk = ConditionSwitch("persistent.performance_mode == True", "awakened mound dragon1 talk p", "persistent.performance_mode == False", At("awakened mound dragon1 talk p", distortion))
    image felina dragon1 = ConditionSwitch("persistent.performance_mode == True", "awakened mound dragon1 p", "persistent.performance_mode == False", At("awakened mound dragon1 p", distortion))
    image felina dragon2 talk = ConditionSwitch("persistent.performance_mode == True", "awakened mound dragon2 talk p", "persistent.performance_mode == False", At("awakened mound dragon2 talk p", distortion))
    image felina dragon2 = ConditionSwitch("persistent.performance_mode == True", "awakened mound dragon2 p", "persistent.performance_mode == False", At("awakened mound dragon2 p", distortion))
    image felina dragon3 talk = ConditionSwitch("persistent.performance_mode == True", "awakened mound dragon3 talk p", "persistent.performance_mode == False", At("awakened mound dragon3 talk p", distortion))
    image felina dragon3 = ConditionSwitch("persistent.performance_mode == True", "awakened mound dragon3 p", "persistent.performance_mode == False", At("awakened mound dragon3 p", distortion))

    image felina dragon nohand 1 = ConditionSwitch("persistent.performance_mode == True", "felina dragon nohand 1 p", "persistent.performance_mode == False", At("felina dragon nohand 1 p", distortion))
    image felina dragon nohand 2 = ConditionSwitch("persistent.performance_mode == True", "felina dragon nohand 3 p", "persistent.performance_mode == False", At("felina dragon nohand 3 p", distortion))
    image felina dragon nohand talk 1 = ConditionSwitch("persistent.performance_mode == True", "felina dragon nohand talk 1 p", "persistent.performance_mode == False", At("felina dragon nohand talk 1 p", distortion))
    image felina dragon nohand talk 2 = ConditionSwitch("persistent.performance_mode == True", "felina dragon nohand talk 2 p", "persistent.performance_mode == False", At("felina dragon nohand talk 2 p", distortion))
    image felina dragon normal1 talk = ConditionSwitch("persistent.performance_mode == True", "felina dragon normal1 talk p", "persistent.performance_mode == False", At("felina dragon normal1 talk p", distortion))
    image felina dragon normal1 = ConditionSwitch("persistent.performance_mode == True", "felina dragon normal1 p", "persistent.performance_mode == False", At("felina dragon normal1 p", distortion))
    image felina dragon normal2 talk = ConditionSwitch("persistent.performance_mode == True", "felina dragon normal2 talk p", "persistent.performance_mode == False", At("felina dragon normal2 talk p", distortion))
    image felina dragon normal2 = ConditionSwitch("persistent.performance_mode == True", "felina dragon normal2 p", "persistent.performance_mode == False", At("felina dragon normal2 p", distortion))
    image felina dragon normal3 talk = ConditionSwitch("persistent.performance_mode == True", "felina dragon normal3 talk p", "persistent.performance_mode == False", At("felina dragon normal3 talk p", distortion))
    image felina dragon normal3 = ConditionSwitch("persistent.performance_mode == True", "felina dragon normal3 p", "persistent.performance_mode == False", At("felina dragon normal3 p", distortion))
    image felina happy mascara 1 talk = ConditionSwitch("persistent.performance_mode == True", "felina happy mascara 1 talk p", "persistent.performance_mode == False", At("felina happy mascara 1 talk p", distortion))

    image felina happy mascara 1 = ConditionSwitch("persistent.performance_mode == True", "felina happy mascara 1 p", "persistent.performance_mode == False", At("felina happy mascara 1 p", distortion))
    image felina happy mascara 2 talk = ConditionSwitch("persistent.performance_mode == True", "felina happy mascara 2 talk p", "persistent.performance_mode == False", At("felina happy mascara 2 talk p", distortion))
    image felina happy mascara 2 = ConditionSwitch("persistent.performance_mode == True", "felina happy mascara 2 p", "persistent.performance_mode == False", At("felina happy mascara 2 p", distortion))
    image felina happy mascara 3 talk = ConditionSwitch("persistent.performance_mode == True", "felina happy mascara 3 talk p", "persistent.performance_mode == False", At("felina happy mascara 3 talk p", distortion))
    image felina happy mascara 3 = ConditionSwitch("persistent.performance_mode == True", "felina happy mascara 3 p", "persistent.performance_mode == False", At("felina happy mascara 3 p", distortion))

    image mound dragon nohand pose talk = ConditionSwitch("persistent.performance_mode == True", "mound dragon nohand pose talk p", "persistent.performance_mode == False", At("mound dragon nohand pose talk p", distortion))
    image mound dragon nohand pose = ConditionSwitch("persistent.performance_mode == True", "mound dragon nohand pose p", "persistent.performance_mode == False", At("mound dragon nohand pose p", distortion))
    image mound dragon nohand shift talk = ConditionSwitch("persistent.performance_mode == True", "mound dragon nohand shift talk p", "persistent.performance_mode == False", At("mound dragon nohand shift talk p", distortion))
    image mound dragon nohand shift = ConditionSwitch("persistent.performance_mode == True", "mound dragon nohand shift p", "persistent.performance_mode == False", At("mound dragon nohand shift p", distortion))
    image mound dragon nohand neutral talk = ConditionSwitch("persistent.performance_mode == True", "mound dragon normal neutral nohand talk p", "persistent.performance_mode == False", At("mound dragon normal neutral nohand talk p", distortion))

    image mound dragon nohand neutral = ConditionSwitch("persistent.performance_mode == True", "mound dragon normal neutral nohand p", "persistent.performance_mode == False", At("mound dragon normal neutral nohand p", distortion))
    image mound dragon normal neutral talk = ConditionSwitch("persistent.performance_mode == True", "mound dragon normal neutral talk p", "persistent.performance_mode == False", At("mound dragon normal neutral talk p", distortion))
    image mound dragon normal neutral = ConditionSwitch("persistent.performance_mode == True", "mound dragon normal neutral p", "persistent.performance_mode == False", At("mound dragon normal neutral p", distortion))
    image mound dragon normal pose talk = ConditionSwitch("persistent.performance_mode == True", "mound dragon normal pose talk p", "persistent.performance_mode == False", At("mound dragon normal pose talk p", distortion))
    image mound dragon normal pose = ConditionSwitch("persistent.performance_mode == True", "mound dragon normal pose p", "persistent.performance_mode == False", At("mound dragon normal pose p", distortion))
    image mound dragon normal shift talk = ConditionSwitch("persistent.performance_mode == True", "mound dragon normal shift talk p", "persistent.performance_mode == False", At("mound dragon normal shift talk p", distortion))

    image mound dragon normal shift = ConditionSwitch("persistent.performance_mode == True", "mound dragon normal shift p", "persistent.performance_mode == False", At("mound dragon normal shift p", distortion))
    image mound happy mascara neutral = ConditionSwitch("persistent.performance_mode == True", "mound happy mascara neutral p", "persistent.performance_mode == False", At("mound happy mascara neutral p", distortion))
    image mound happy mascara pose talk = ConditionSwitch("persistent.performance_mode == True", "mound happy mascara pose talk p", "persistent.performance_mode == False", At("mound happy mascara pose talk p", distortion))
    image mound happy mascara pose = ConditionSwitch("persistent.performance_mode == True", "mound happy mascara pose p", "persistent.performance_mode == False", At("mound happy mascara pose p", distortion))
    image mound happy mascara shift talk = ConditionSwitch("persistent.performance_mode == True", "mound happy mascara shift talk p", "persistent.performance_mode == False", At("mound happy mascara shift talk p", distortion))
    image mound happy mascara shift = ConditionSwitch("persistent.performance_mode == True", "mound happy mascara shift p", "persistent.performance_mode == False", At("mound happy mascara shift p", distortion))
