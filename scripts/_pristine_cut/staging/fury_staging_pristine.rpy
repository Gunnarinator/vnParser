label fury_staging_pristine:

    image bg fury abs sequence 2 = ConditionSwitch("persistent.performance_mode == True", "cg fury abs sequence 2 bg p", "persistent.performance_mode == False", At("cg fury abs sequence 2 bg p", distortion))
    image fury abs sequence 2 = ConditionSwitch("persistent.performance_mode == True", "cg fury abs sequence 2 p", "persistent.performance_mode == False", At("cg fury abs sequence 2 p", distortion))
    image bg fury abs sequence 3 = ConditionSwitch("persistent.performance_mode == True", "cg fury abs sequence 3 bg p", "persistent.performance_mode == False", At("cg fury abs sequence 3 bg p", distortion))
    image fury abs sequence 3 = ConditionSwitch("persistent.performance_mode == True", "cg fury abs sequence 3 p", "persistent.performance_mode == False", At("cg fury abs sequence 3 p", distortion))
    image bg fury abs sequence 4 = ConditionSwitch("persistent.performance_mode == True", "cg fury abs sequence 4 bg p", "persistent.performance_mode == False", At("cg fury abs sequence 4 bg p", distortion))
    image fury abs sequence 4 = ConditionSwitch("persistent.performance_mode == True", "cg fury abs sequence 4 p", "persistent.performance_mode == False", At("cg fury abs sequence 4 p", distortion))
    image bg fury abs sequence = ConditionSwitch("persistent.performance_mode == True", "cg fury abs sequence bg p", "persistent.performance_mode == False", At("cg fury abs sequence bg p", distortion))
    image rear fury abs sequence end = ConditionSwitch("persistent.performance_mode == True", "cg fury abs sequence end behind p", "persistent.performance_mode == False", At("cg fury abs sequence end behind p", distortion))
    image bg fury abs sequence end = ConditionSwitch("persistent.performance_mode == True", "cg fury abs sequence end bg p", "persistent.performance_mode == False", At("cg fury abs sequence end bg p", distortion))
    image fury abs sequence end = ConditionSwitch("persistent.performance_mode == True", "cg fury abs sequence end p", "persistent.performance_mode == False", At("cg fury abs sequence end p", distortion))

    image player fury abs sequence = ConditionSwitch("persistent.performance_mode == True", "cg fury abs sequence player p", "persistent.performance_mode == False", At("cg fury abs sequence player p", distortion))
    image fury abs sequence = ConditionSwitch("persistent.performance_mode == True", "cg fury abs sequence princess p", "persistent.performance_mode == False", At("cg fury abs sequence princess p", distortion))
    image bg fury hand = ConditionSwitch("persistent.performance_mode == True", "cg fury hand bg p", "persistent.performance_mode == False", At("cg fury hand bg p", distortion))
    image player fury hand = ConditionSwitch("persistent.performance_mode == True", "cg fury hand offer p", "persistent.performance_mode == False", At("cg fury hand offer p", distortion))
    image farback fury hand = ConditionSwitch("persistent.performance_mode == True", "cg fury hand stars p", "persistent.performance_mode == False", At("cg fury hand stars p", distortion))
    image fury hand grab = ConditionSwitch("persistent.performance_mode == True", "cg fury hand take p", "persistent.performance_mode == False", At("cg fury hand take p", distortion))
    image fury hand = ConditionSwitch("persistent.performance_mode == True", "cg fury hand p", "persistent.performance_mode == False", At("cg fury hand p", distortion))

    image farback fury leave outside = ConditionSwitch("persistent.performance_mode == True", "cg fury leave outside bg p", "persistent.performance_mode == False", At("cg fury leave outside bg p", distortion))
    image fury leave outside talk = ConditionSwitch("persistent.performance_mode == True", "cg fury leave outside talk p", "persistent.performance_mode == False", At("cg fury leave outside talk p", distortion))
    image bg fury leave outside = ConditionSwitch("persistent.performance_mode == True", "cg fury leave outside trees p", "persistent.performance_mode == False", At("cg fury leave outside trees p", distortion))
    image fury leave outside = ConditionSwitch("persistent.performance_mode == True", "cg fury leave outside p", "persistent.performance_mode == False", At("cg fury leave outside p", distortion))

    image farback fury leave stairs = ConditionSwitch("persistent.performance_mode == True", "cg fury leave stairs bg p", "persistent.performance_mode == False", At("cg fury leave stairs bg p", distortion))
    image fury leave stairs = ConditionSwitch("persistent.performance_mode == True", "cg fury leave stairs princess p", "persistent.performance_mode == False", At("cg fury leave stairs princess p", distortion))
    image bg fury leave stairs = ConditionSwitch("persistent.performance_mode == True", "cg fury leave stairs p", "persistent.performance_mode == False", At("cg fury leave stairs p", distortion))
    image bg fury leave upstairs = ConditionSwitch("persistent.performance_mode == True", "cg fury leave upstairs bg p", "persistent.performance_mode == False", At("cg fury leave upstairs bg p", distortion))
    image fury leave upstairs = ConditionSwitch("persistent.performance_mode == True", "cg fury leave upstairs princess p", "persistent.performance_mode == False", At("cg fury leave upstairs princess p", distortion))
    image farback fury leave upstairs = ConditionSwitch("persistent.performance_mode == True", "cg fury leave upstairs stars p", "persistent.performance_mode == False", At("cg fury leave upstairs stars p", distortion))
    image fury slay sad post stab talk = ConditionSwitch("persistent.performance_mode == True", "cg fury slay sad post stab talk p", "persistent.performance_mode == False", At("cg fury slay sad post stab talk p", distortion))
    image fury slay sad post stab = ConditionSwitch("persistent.performance_mode == True", "cg fury slay sad post stab p", "persistent.performance_mode == False", At("cg fury slay sad post stab p", distortion))
    image fury slay sad stab talk = ConditionSwitch("persistent.performance_mode == True", "cg fury slay sad stab talk p", "persistent.performance_mode == False", At("cg fury slay sad stab talk p", distortion))
    image fury slay sad stab = ConditionSwitch("persistent.performance_mode == True", "cg fury slay sad stab p", "persistent.performance_mode == False", At("cg fury slay sad stab p", distortion))
    image fury slay sad = ConditionSwitch("persistent.performance_mode == True", "cg fury slay sad p", "persistent.performance_mode == False", At("cg fury slay sad p", distortion))

    image cg fury tower torment = ConditionSwitch("persistent.performance_mode == True", "cg fury tower torment p", "persistent.performance_mode == False", At("cg fury tower torment p", distortion))
    image cg fury tower torment talk = ConditionSwitch("persistent.performance_mode == True", "cg fury tower torment talk p", "persistent.performance_mode == False", At("cg fury tower torment talk p", distortion))
    image cg fury tower snap = ConditionSwitch("persistent.performance_mode == True", "cg fury tower snap p", "persistent.performance_mode == False", At("cg fury tower snap p", distortion))

    image cg fury unarmed 1 clench talk = ConditionSwitch("persistent.performance_mode == True", "cg fury unarmed 1 clench talk p", "persistent.performance_mode == False", At("cg fury unarmed 1 clench talk p", distortion))
    image cg fury unarmed 1 clench = ConditionSwitch("persistent.performance_mode == True", "cg fury unarmed 1 clench p", "persistent.performance_mode == False", At("cg fury unarmed 1 clench p", distortion))
    image player fury unarmed 1 explode = ConditionSwitch("persistent.performance_mode == True", "cg fury unarmed 1 player explode p", "persistent.performance_mode == False", At("cg fury unarmed 1 player explode p", distortion))
    image player fury unarmed 1 = ConditionSwitch("persistent.performance_mode == True", "cg fury unarmed 1 player p", "persistent.performance_mode == False", At("cg fury unarmed 1 player p", distortion))
    image cg fury unarmed 1 talk = ConditionSwitch("persistent.performance_mode == True", "cg fury unarmed 1 talk p", "persistent.performance_mode == False", At("cg fury unarmed 1 talk p", distortion))
    image cg fury unarmed 1 = ConditionSwitch("persistent.performance_mode == True", "cg fury unarmed 1 p", "persistent.performance_mode == False", At("cg fury unarmed 1 p", distortion))
    image cg fury unarmed 2 clench talk = ConditionSwitch("persistent.performance_mode == True", "cg fury unarmed 2 clench talk p", "persistent.performance_mode == False", At("cg fury unarmed 2 clench talk p", distortion))
    image cg fury unarmed 2 clench = ConditionSwitch("persistent.performance_mode == True", "cg fury unarmed 2 clench p", "persistent.performance_mode == False", At("cg fury unarmed 2 clench p", distortion))
    image player fury unarmed 2 explode = ConditionSwitch("persistent.performance_mode == True", "cg fury unarmed 2 player explode p", "persistent.performance_mode == False", At("cg fury unarmed 2 player explode p", distortion))
    image player fury unarmed 2 = ConditionSwitch("persistent.performance_mode == True", "cg fury unarmed 2 player p", "persistent.performance_mode == False", At("cg fury unarmed 2 player p", distortion))
    image cg fury unarmed 2 talk = ConditionSwitch("persistent.performance_mode == True", "cg fury unarmed 2 talk p", "persistent.performance_mode == False", At("cg fury unarmed 2 talk p", distortion))
    image cg fury unarmed 2 = ConditionSwitch("persistent.performance_mode == True", "cg fury unarmed 2 p", "persistent.performance_mode == False", At("cg fury unarmed 2 p", distortion))
    image bg fury unarmed 3 = ConditionSwitch("persistent.performance_mode == True", "cg fury unarmed 3 bg p", "persistent.performance_mode == False", At("cg fury unarmed 3 bg p", distortion))
    image cg fury unarmed 3 hitme talk = ConditionSwitch("persistent.performance_mode == True", "cg fury unarmed 3 hitme talk p", "persistent.performance_mode == False", At("cg fury unarmed 3 hitme talk p", distortion))
    image cg fury unarmed 3 hitme = ConditionSwitch("persistent.performance_mode == True", "cg fury unarmed 3 hitme p", "persistent.performance_mode == False", At("cg fury unarmed 3 hitme p", distortion))
    image player fury unarmed 3 = ConditionSwitch("persistent.performance_mode == True", "cg fury unarmed 3 player p", "persistent.performance_mode == False", At("cg fury unarmed 3 player p", distortion))
    image cg fury unarmed 3 talk = ConditionSwitch("persistent.performance_mode == True", "cg fury unarmed 3 talk p", "persistent.performance_mode == False", At("cg fury unarmed 3 talk p", distortion))
    image cg fury unarmed 3 = ConditionSwitch("persistent.performance_mode == True", "cg fury unarmed 3 p", "persistent.performance_mode == False", At("cg fury unarmed 3 p", distortion))


    image panel2 fury unarmed 4 delayed:
        "emptyimage"
        5.2
        "panel2 fury unarmed 4"

    image panel2 fury unarmed 4 player delayed:
        "emptyimage"
        5.2
        "panel2 fury unarmed 4 player"

    image panel3 fury unarmed 4 delayed:
        "emptyimage"
        9.0
        "panel3 fury unarmed 4"

    image panel3 fury unarmed 4 player delayed:
        "emptyimage"
        9.0
        "panel3 fury unarmed 4 player"

    image bg fury unarmed 4 = ConditionSwitch("persistent.performance_mode == True", "cg fury unarmed 4 bg p", "persistent.performance_mode == False", At("cg fury unarmed 4 bg p", distortion))
    image panel1 fury unarmed 4 player = ConditionSwitch("persistent.performance_mode == True", "cg fury unarmed 4 panel 1 player p", "persistent.performance_mode == False", At("cg fury unarmed 4 panel 1 player p", distortion))
    image panel1 fury unarmed 4 = ConditionSwitch("persistent.performance_mode == True", "cg fury unarmed 4 panel 1 p", "persistent.performance_mode == False", At("cg fury unarmed 4 panel 1 p", distortion))
    image panel2 fury unarmed 4 player = ConditionSwitch("persistent.performance_mode == True", "cg fury unarmed 4 panel 2 player p", "persistent.performance_mode == False", At("cg fury unarmed 4 panel 2 player p", distortion))
    image panel2 fury unarmed 4 = ConditionSwitch("persistent.performance_mode == True", "cg fury unarmed 4 panel 2 p", "persistent.performance_mode == False", At("cg fury unarmed 4 panel 2 p", distortion))
    image panel3 fury unarmed 4 player = ConditionSwitch("persistent.performance_mode == True", "cg fury unarmed 4 panel 3 player p", "persistent.performance_mode == False", At("cg fury unarmed 4 panel 3 player p", distortion))
    image panel3 fury unarmed 4 = ConditionSwitch("persistent.performance_mode == True", "cg fury unarmed 4 panel 3 p", "persistent.performance_mode == False", At("cg fury unarmed 4 panel 3 p", distortion))
    image bg fury unarmed 5 = ConditionSwitch("persistent.performance_mode == True", "cg fury unarmed 5 bg p", "persistent.performance_mode == False", At("cg fury unarmed 5 bg p", distortion))
    image cg fury unarmed 5 okay = ConditionSwitch("persistent.performance_mode == True", "cg fury unarmed 5 okay p", "persistent.performance_mode == False", At("cg fury unarmed 5 okay p", distortion))
    image cg fury unarmed 5 end = ConditionSwitch("persistent.performance_mode == True", "cg fury unarmed 5 end p", "persistent.performance_mode == False", At("cg fury unarmed 5 end p", distortion))
    image cg fury unarmed 5 talk = ConditionSwitch("persistent.performance_mode == True", "cg fury unarmed 5 talk p", "persistent.performance_mode == False", At("cg fury unarmed 5 talk p", distortion))
    image cg fury unarmed 5 = ConditionSwitch("persistent.performance_mode == True", "cg fury unarmed 5 p", "persistent.performance_mode == False", At("cg fury unarmed 5 p", distortion))

    image player fury abs begin = ConditionSwitch("persistent.performance_mode == True", "fury abs begin player p", "persistent.performance_mode == False", At("fury abs begin player p", distortion))
    image fury abs begin = ConditionSwitch("persistent.performance_mode == True", "fury abs begin p", "persistent.performance_mode == False", At("fury abs begin p", distortion))
    image fury abs desperate talk = ConditionSwitch("persistent.performance_mode == True", "fury abs desperate talk p", "persistent.performance_mode == False", At("fury abs desperate talk p", distortion))
    image fury abs desperate = ConditionSwitch("persistent.performance_mode == True", "fury abs desperate p", "persistent.performance_mode == False", At("fury abs desperate p", distortion))
    image fury abs determined talk = ConditionSwitch("persistent.performance_mode == True", "fury abs determined talk p", "persistent.performance_mode == False", At("fury abs determined talk p", distortion))
    image fury abs determined = ConditionSwitch("persistent.performance_mode == True", "fury abs determined p", "persistent.performance_mode == False", At("fury abs determined p", distortion))

    image bg fury abs neutral = ConditionSwitch("persistent.performance_mode == True", "fury abs neutral bg p", "persistent.performance_mode == False", At("fury abs neutral bg p", distortion))
    image fury abs neutral talk upset = ConditionSwitch("persistent.performance_mode == True", "fury abs neutral talk upset p", "persistent.performance_mode == False", At("fury abs neutral talk upset p", distortion))
    image fury abs neutral talk = ConditionSwitch("persistent.performance_mode == True", "fury abs neutral talk p", "persistent.performance_mode == False", At("fury abs neutral talk p", distortion))
    image fury abs neutral = ConditionSwitch("persistent.performance_mode == True", "fury abs neutral p", "persistent.performance_mode == False", At("fury abs neutral p", distortion))
    image fury s sullen talk = ConditionSwitch("persistent.performance_mode == True", "fury s sullen talk p", "persistent.performance_mode == False", At("fury s sullen talk p", distortion))
    image fury s sullen = ConditionSwitch("persistent.performance_mode == True", "fury s sullen p", "persistent.performance_mode == False", At("fury s sullen p", distortion))

    image fury s glance talk = ConditionSwitch("persistent.performance_mode == True", "fury s glance talk p", "persistent.performance_mode == False", At("fury s glance talk p", distortion))
    image fury s glance = ConditionSwitch("persistent.performance_mode == True", "fury s glance p", "persistent.performance_mode == False", At("fury s glance p", distortion))

    image fury s timid talk = ConditionSwitch("persistent.performance_mode == True", "fury s timid talk p", "persistent.performance_mode == False", At("fury s timid talk p", distortion))
    image fury s timid = ConditionSwitch("persistent.performance_mode == True", "fury s timid p", "persistent.performance_mode == False", At("fury s timid p", distortion))
    image fury s wave off talk 1 = ConditionSwitch("persistent.performance_mode == True", "fury s wave off talk 1 p", "persistent.performance_mode == False", At("fury s wave off talk 1 p", distortion))
    image fury s wave off talk 2 = ConditionSwitch("persistent.performance_mode == True", "fury s wave off talk 2 p", "persistent.performance_mode == False", At("fury s wave off talk 2 p", distortion))
    image bg fury sullen = ConditionSwitch("persistent.performance_mode == True", "fury sullen bg p", "persistent.performance_mode == False", At("fury sullen bg p", distortion))
    image fury unwind annoyed talk = ConditionSwitch("persistent.performance_mode == True", "fury unwind annoyed talk p", "persistent.performance_mode == False", At("fury unwind annoyed talk p", distortion))
    image fury unwind annoyed = ConditionSwitch("persistent.performance_mode == True", "fury unwind annoyed p", "persistent.performance_mode == False", At("fury unwind annoyed p", distortion))
    image fury unwind flat talk = ConditionSwitch("persistent.performance_mode == True", "fury unwind flat talk p", "persistent.performance_mode == False", At("fury unwind flat talk p", distortion))
    image fury unwind flat = ConditionSwitch("persistent.performance_mode == True", "fury unwind flat p", "persistent.performance_mode == False", At("fury unwind flat p", distortion))
    image bg fury unwind = ConditionSwitch("persistent.performance_mode == True", "fury unwind surprise bg p", "persistent.performance_mode == False", At("fury unwind surprise bg p", distortion))
    image fury unwind surprise talk = ConditionSwitch("persistent.performance_mode == True", "fury unwind surprise talk p", "persistent.performance_mode == False", At("fury unwind surprise talk p", distortion))
    image fury unwind surprise = ConditionSwitch("persistent.performance_mode == True", "fury unwind surprise p", "persistent.performance_mode == False", At("fury unwind surprise p", distortion))
    image fury unwind wry talk = ConditionSwitch("persistent.performance_mode == True", "fury unwind wry talk p", "persistent.performance_mode == False", At("fury unwind wry talk p", distortion))
    image fury unwind wry = ConditionSwitch("persistent.performance_mode == True", "fury unwind wry p", "persistent.performance_mode == False", At("fury unwind wry p", distortion))
    image hands fury abs 2 = ConditionSwitch("persistent.performance_mode == True", "hands fury abs 2 p", "persistent.performance_mode == False", At("hands fury abs 2 p", distortion))
    image hands fury abs 3 = ConditionSwitch("persistent.performance_mode == True", "hands fury abs 3 p", "persistent.performance_mode == False", At("hands fury abs 3 p", distortion))
    image hands fury abs 4 = ConditionSwitch("persistent.performance_mode == True", "hands fury abs 4 p", "persistent.performance_mode == False", At("hands fury abs 4 p", distortion))
    image hands fury abs 1 = ConditionSwitch("persistent.performance_mode == True", "hands fury abs p", "persistent.performance_mode == False", At("hands fury abs p", distortion))
    image hands fury leave 1 = ConditionSwitch("persistent.performance_mode == True", "hands fury leave 1 p", "persistent.performance_mode == False", At("hands fury leave 1 p", distortion))
    image hands fury leave 2 = ConditionSwitch("persistent.performance_mode == True", "hands fury leave 2 p", "persistent.performance_mode == False", At("hands fury leave 2 p", distortion))
    image hands fury leave 3 = ConditionSwitch("persistent.performance_mode == True", "hands fury leave 3 p", "persistent.performance_mode == False", At("hands fury leave 3 p", distortion))
    image hands fury leave 4 = ConditionSwitch("persistent.performance_mode == True", "hands fury leave 4 p", "persistent.performance_mode == False", At("hands fury leave 4 p", distortion))
    image hands fury leave 5 = ConditionSwitch("persistent.performance_mode == True", "hands fury leave 5 p", "persistent.performance_mode == False", At("hands fury leave 5 p", distortion))
    image hands fury sad slay 1 = ConditionSwitch("persistent.performance_mode == True", "hands fury sad slay 1 p", "persistent.performance_mode == False", At("hands fury sad slay 1 p", distortion))
    image hands fury sad slay 2 = ConditionSwitch("persistent.performance_mode == True", "hands fury sad slay 2 p", "persistent.performance_mode == False", At("hands fury sad slay 2 p", distortion))
    image hands fury sad slay 3 = ConditionSwitch("persistent.performance_mode == True", "hands fury sad slay 3 p", "persistent.performance_mode == False", At("hands fury sad slay 3 p", distortion))
    image hands fury sad slay 4 = ConditionSwitch("persistent.performance_mode == True", "hands fury sad slay 4 p", "persistent.performance_mode == False", At("hands fury sad slay 4 p", distortion))
    image hands fury sad slay 5 = ConditionSwitch("persistent.performance_mode == True", "hands fury sad slay 5 p", "persistent.performance_mode == False", At("hands fury sad slay 5 p", distortion))
    image hands fury unarmed 1 = ConditionSwitch("persistent.performance_mode == True", "hands fury unarmed 1 p", "persistent.performance_mode == False", At("hands fury unarmed 1 p", distortion))
    image hands fury unarmed 2 = ConditionSwitch("persistent.performance_mode == True", "hands fury unarmed 2 p", "persistent.performance_mode == False", At("hands fury unarmed 2 p", distortion))
    image hands fury unarmed 3 = ConditionSwitch("persistent.performance_mode == True", "hands fury unarmed 3 p", "persistent.performance_mode == False", At("hands fury unarmed 3 p", distortion))
    image hands fury unarmed 4 = ConditionSwitch("persistent.performance_mode == True", "hands fury unarmed 4 p", "persistent.performance_mode == False", At("hands fury unarmed 4 p", distortion))
    image hands fury unarmed 5 = ConditionSwitch("persistent.performance_mode == True", "hands fury unarmed 5 p", "persistent.performance_mode == False", At("hands fury unarmed 5 p", distortion))

    image ribbons fury unwound 4:
        "ribbons fury start 2"
        3.2
        "emptyimage"

    image panel1 unwound 4 delayed:
        "emptyimage"
        5.5
        "panel1 unwound 4"

    image panel2 unwound 4 delayed:
        "emptyimage"
        7.0
        "panel2 unwound 4"

    image panel3 unwound 4 delayed:
        "emptyimage"
        8.3
        "panel3 unwound 4"

    image panel4 unwound 4 delayed:
        "emptyimage"
        10.4
        "panel4 unwound 4"

    image panel5 unwound 4 delayed:
        "emptyimage"
        14.73
        "panel5 unwound 4"

    image panel6 unwound 4 delayed:
        "emptyimage"
        18.1
        "panel6 unwound 4"

    image ribbons fury start 1 = ConditionSwitch("persistent.performance_mode == True", "pristine cut start guts 2 p", "persistent.performance_mode == False", At("pristine cut start guts 2 p", distortion))
    image ribbons fury start 2 = ConditionSwitch("persistent.performance_mode == True", "pristine cut start guts 3 p", "persistent.performance_mode == False", At("pristine cut start guts 3 p", distortion))
    image unwound 1 talk = ConditionSwitch("persistent.performance_mode == True", "unwound 1 talk p", "persistent.performance_mode == False", At("unwound 1 talk p", distortion))
    image unwound 1 = ConditionSwitch("persistent.performance_mode == True", "unwound 1 p", "persistent.performance_mode == False", At("unwound 1 p", distortion))
    image bg unwound 2 = ConditionSwitch("persistent.performance_mode == True", "unwound 2 bg p", "persistent.performance_mode == False", At("unwound 2 bg p", distortion))
    image unwound 2 talk = ConditionSwitch("persistent.performance_mode == True", "unwound 2 talk p", "persistent.performance_mode == False", At("unwound 2 talk p", distortion))
    image unwound 2 = ConditionSwitch("persistent.performance_mode == True", "unwound 2 p", "persistent.performance_mode == False", At("unwound 2 p", distortion))
    image bg unwound 3 = ConditionSwitch("persistent.performance_mode == True", "unwound 3 bg p", "persistent.performance_mode == False", At("unwound 3 bg p", distortion))
    image unwound 3 talk = ConditionSwitch("persistent.performance_mode == True", "unwound 3 talk p", "persistent.performance_mode == False", At("unwound 3 talk p", distortion))
    image unwound 3 = ConditionSwitch("persistent.performance_mode == True", "unwound 3 p", "persistent.performance_mode == False", At("unwound 3 p", distortion))
    image bg unwound 4 = ConditionSwitch("persistent.performance_mode == True", "unwound 4 bg p", "persistent.performance_mode == False", At("unwound 4 bg p", distortion))
    image panel1 unwound 4 = ConditionSwitch("persistent.performance_mode == True", "unwound 4 panel 1 p", "persistent.performance_mode == False", At("unwound 4 panel 1 p", distortion))
    image panel2 unwound 4 = ConditionSwitch("persistent.performance_mode == True", "unwound 4 panel 2 p", "persistent.performance_mode == False", At("unwound 4 panel 2 p", distortion))
    image panel3 unwound 4 = ConditionSwitch("persistent.performance_mode == True", "unwound 4 panel 3 p", "persistent.performance_mode == False", At("unwound 4 panel 3 p", distortion))
    image panel4 unwound 4 = ConditionSwitch("persistent.performance_mode == True", "unwound 4 panel 4 p", "persistent.performance_mode == False", At("unwound 4 panel 4 p", distortion))
    image panel5 unwound 4 = ConditionSwitch("persistent.performance_mode == True", "unwound 4 panel 5 p", "persistent.performance_mode == False", At("unwound 4 panel 5 p", distortion))
    image panel6 unwound 4 = ConditionSwitch("persistent.performance_mode == True", "unwound 4 panel 6 p", "persistent.performance_mode == False", At("unwound 4 panel 6 p", distortion))
    image bg unwound 5 = ConditionSwitch("persistent.performance_mode == True", "unwound 5 bg p", "persistent.performance_mode == False", At("unwound 5 bg p", distortion))
    image player unwound 5 = ConditionSwitch("persistent.performance_mode == True", "unwound 5 player p", "persistent.performance_mode == False", At("unwound 5 player p", distortion))
    image unwound 5 princess talk = ConditionSwitch("persistent.performance_mode == True", "unwound 5 princess talk p", "persistent.performance_mode == False", At("unwound 5 princess talk p", distortion))
    image unwound 5 princess = ConditionSwitch("persistent.performance_mode == True", "unwound 5 princess p", "persistent.performance_mode == False", At("unwound 5 princess p", distortion))
    image bg unwound 6 = ConditionSwitch("persistent.performance_mode == True", "unwound 6 bg p", "persistent.performance_mode == False", At("unwound 6 bg p", distortion))
    image bg unwound 6 stretch 1 = ConditionSwitch("persistent.performance_mode == True", "unwound 6 stretch 1 bg p", "persistent.performance_mode == False", At("unwound 6 stretch 1 bg p", distortion))
    image unwound 6 stretch 1 talk = ConditionSwitch("persistent.performance_mode == True", "unwound 6 stretch 1 talk p", "persistent.performance_mode == False", At("unwound 6 stretch 1 talk p", distortion))
    image unwound 6 stretch 1 = ConditionSwitch("persistent.performance_mode == True", "unwound 6 stretch 1 p", "persistent.performance_mode == False", At("unwound 6 stretch 1 p", distortion))
    image bg unwound 6 stretch 2 = ConditionSwitch("persistent.performance_mode == True", "unwound 6 stretch 2 bg p", "persistent.performance_mode == False", At("unwound 6 stretch 2 bg p", distortion))
    image unwound 6 stretch 2 talk = ConditionSwitch("persistent.performance_mode == True", "unwound 6 stretch 2 talk p", "persistent.performance_mode == False", At("unwound 6 stretch 2 talk p", distortion))
    image unwound 6 stretch 2 = ConditionSwitch("persistent.performance_mode == True", "unwound 6 stretch 2 p", "persistent.performance_mode == False", At("unwound 6 stretch 2 p", distortion))
    image unwound 6 talk = ConditionSwitch("persistent.performance_mode == True", "unwound 6 talk p", "persistent.performance_mode == False", At("unwound 6 talk p", distortion))
    image unwound 6 = ConditionSwitch("persistent.performance_mode == True", "unwound 6 p", "persistent.performance_mode == False", At("unwound 6 p", distortion))
    image back unwound 7 = ConditionSwitch("persistent.performance_mode == True", "unwound 7 back p", "persistent.performance_mode == False", At("unwound 7 back p", distortion))
    image bg unwound 7 = ConditionSwitch("persistent.performance_mode == True", "unwound 7 bg p", "persistent.performance_mode == False", At("unwound 7 bg p", distortion))
    image fore unwound 7 = ConditionSwitch("persistent.performance_mode == True", "unwound 7 fore p", "persistent.performance_mode == False", At("unwound 7 fore p", distortion))
    image mid unwound 7 = ConditionSwitch("persistent.performance_mode == True", "unwound 7 mid p", "persistent.performance_mode == False", At("unwound 7 mid p", distortion))
    image bg unwound 8 = ConditionSwitch("persistent.performance_mode == True", "unwound 8 bg p", "persistent.performance_mode == False", At("unwound 8 bg p", distortion))
    image mid unwound 8 = ConditionSwitch("persistent.performance_mode == True", "unwound 8 midground p", "persistent.performance_mode == False", At("unwound 8 midground p", distortion))
    image unwound 8 talk = ConditionSwitch("persistent.performance_mode == True", "unwound 8 talk p", "persistent.performance_mode == False", At("unwound 8 talk p", distortion))
    image unwound 8 = ConditionSwitch("persistent.performance_mode == True", "unwound 8 p", "persistent.performance_mode == False", At("unwound 8 p", distortion))

    image cg fury tower 1 talk = ConditionSwitch("persistent.performance_mode == True", "cg fury tower 1 talk p", "persistent.performance_mode == False", At("cg fury tower 1 talk p", distortion))
    image cg fury tower 1 = ConditionSwitch("persistent.performance_mode == True", "cg fury tower 1 p", "persistent.performance_mode == False", At("cg fury tower 1 p", distortion))
    image cg fury tower 2 tinted = ConditionSwitch("persistent.performance_mode == True", "cg fury tower 2 tinted p", "persistent.performance_mode == False", At("cg fury tower 2 tinted p", distortion))

    image cg fury tower 2 tinted delayed:
        "cg fury tower 2 explode"
        3.22
        "cg fury tower 2 tinted"

    image cg fury tower 3 tinted = ConditionSwitch("persistent.performance_mode == True", "cg fury tower 3 tinted p", "persistent.performance_mode == False", At("cg fury tower 3 tinted p", distortion))
    image cg fury tower 4 tinted = ConditionSwitch("persistent.performance_mode == True", "cg fury tower 4 tinted p", "persistent.performance_mode == False", At("cg fury tower 4 tinted p", distortion))

    image cg fury tower 4 swivel = ConditionSwitch("persistent.performance_mode == True", "cg fury tower 4 swivel p", "persistent.performance_mode == False", At("cg fury tower 4 swivel p", distortion))

    image cg fury tower end tinted = ConditionSwitch("persistent.performance_mode == True", "cg fury tower end tinted p", "persistent.performance_mode == False", At("cg fury tower end tinted p", distortion))
    image cg fury tower 2 explode = ConditionSwitch("persistent.performance_mode == True", "cg fury tower 2 explode p", "persistent.performance_mode == False", At("cg fury tower 2 explode p", distortion))
    image cg fury tower 2 talk = ConditionSwitch("persistent.performance_mode == True", "cg fury tower 2 talk p", "persistent.performance_mode == False", At("cg fury tower 2 talk p", distortion))
    image cg fury tower 2 = ConditionSwitch("persistent.performance_mode == True", "cg fury tower 2 p", "persistent.performance_mode == False", At("cg fury tower 2 p", distortion))
    image cg fury tower 3 talk = ConditionSwitch("persistent.performance_mode == True", "cg fury tower 3 talk p", "persistent.performance_mode == False", At("cg fury tower 3 talk p", distortion))
    image cg fury tower 3 = ConditionSwitch("persistent.performance_mode == True", "cg fury tower 3 p", "persistent.performance_mode == False", At("cg fury tower 3 p", distortion))
    image cg fury tower 4 talk = ConditionSwitch("persistent.performance_mode == True", "cg fury tower 4 talk p", "persistent.performance_mode == False", At("cg fury tower 4 talk p", distortion))
    image cg fury tower 4 = ConditionSwitch("persistent.performance_mode == True", "cg fury tower 4 p", "persistent.performance_mode == False", At("cg fury tower 4 p", distortion))
    image cg fury tower end glance = ConditionSwitch("persistent.performance_mode == True", "cg fury tower end glance p", "persistent.performance_mode == False", At("cg fury tower end glance p", distortion))
    image cg fury tower end talk = ConditionSwitch("persistent.performance_mode == True", "cg fury tower end talk p", "persistent.performance_mode == False", At("cg fury tower end talk p", distortion))
    image cg fury tower end = ConditionSwitch("persistent.performance_mode == True", "cg fury tower end p", "persistent.performance_mode == False", At("cg fury tower end p", distortion))
    image cg fury tower final player = ConditionSwitch("persistent.performance_mode == True", "cg fury tower final player p", "persistent.performance_mode == False", At("cg fury tower final player p", distortion))
    image cg fury tower final stab = ConditionSwitch("persistent.performance_mode == True", "cg fury tower final stab p", "persistent.performance_mode == False", At("cg fury tower final stab p", distortion))
    image cg fury tower final talk = ConditionSwitch("persistent.performance_mode == True", "cg fury tower final talk p", "persistent.performance_mode == False", At("cg fury tower final talk p", distortion))
    image cg fury tower final = ConditionSwitch("persistent.performance_mode == True", "cg fury tower final p", "persistent.performance_mode == False", At("cg fury tower final p", distortion))
    image player fury mouth assembled talk = ConditionSwitch("persistent.performance_mode == True", "player fury mouth assembled talk p", "persistent.performance_mode == False", At("player fury mouth assembled talk p", distortion))
    image player fury mouth assembled = ConditionSwitch("persistent.performance_mode == True", "player fury mouth assembled p", "persistent.performance_mode == False", At("player fury mouth assembled p", distortion))
