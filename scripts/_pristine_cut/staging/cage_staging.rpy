label cage_art_staging:

    image bg cage falling1 = ConditionSwitch("persistent.performance_mode == True", "bg cage falling1 p", "persistent.performance_mode == False", At("bg cage falling1 p", distortion))
    image bg cage falling2 = ConditionSwitch("persistent.performance_mode == True", "bg cage falling2 p", "persistent.performance_mode == False", At("bg cage falling2 p", distortion))
    image bg cage falling3 = ConditionSwitch("persistent.performance_mode == True", "bg cage falling3 p", "persistent.performance_mode == False", At("bg cage falling3 p", distortion))

    image farback cage falling:
        "bg cage falling1"
        0.125
        "bg cage falling2"
        0.125
        "bg cage falling1"
        0.125
        repeat

    image farback cage cabin ext = ConditionSwitch("persistent.performance_mode == True", "bg cage cabin ext stars p", "persistent.performance_mode == False", At("bg cage cabin ext stars p", distortion))
    image bg cage cabin ext = ConditionSwitch("persistent.performance_mode == True", "bg cage cabin ext p", "persistent.performance_mode == False", At("bg cage cabin ext p", distortion))
    image farback cage cabin int = ConditionSwitch("persistent.performance_mode == True", "bg cage cabin int stars p", "persistent.performance_mode == False", At("bg cage cabin int stars p", distortion))
    image bg cage cabin int = ConditionSwitch("persistent.performance_mode == True", "bg cage cabin int p", "persistent.performance_mode == False", At("bg cage cabin int p", distortion))
    image bg cage encounter = ConditionSwitch("persistent.performance_mode == True", "bg cage encounter bg p", "persistent.performance_mode == False", At("bg cage encounter bg p", distortion))
    image mid cage encounter = ConditionSwitch("persistent.performance_mode == True", "bg cage encounter midground p", "persistent.performance_mode == False", At("bg cage encounter midground p", distortion))
    image bg cage woods = ConditionSwitch("persistent.performance_mode == True", "bg cage woods bg p", "persistent.performance_mode == False", At("bg cage woods bg p", distortion))
    image fore cage woods = ConditionSwitch("persistent.performance_mode == True", "bg cage woods fore p", "persistent.performance_mode == False", At("bg cage woods fore p", distortion))
    image mid cage woods = ConditionSwitch("persistent.performance_mode == True", "bg cage woods mid p", "persistent.performance_mode == False", At("bg cage woods mid p", distortion))
    image farback cage woods = ConditionSwitch("persistent.performance_mode == True", "bg cage woods stars p", "persistent.performance_mode == False", At("bg cage woods stars p", distortion))
    image cage approach 1 talk = ConditionSwitch("persistent.performance_mode == True", "cage approach 1 talk p", "persistent.performance_mode == False", At("cage approach 1 talk p", distortion))
    image cage approach 1 = ConditionSwitch("persistent.performance_mode == True", "cage approach 1 p", "persistent.performance_mode == False", At("cage approach 1 p", distortion))
    image cage approach 2 talk = ConditionSwitch("persistent.performance_mode == True", "cage approach 2 talk p", "persistent.performance_mode == False", At("cage approach 2 talk p", distortion))
    image cage approach 2 = ConditionSwitch("persistent.performance_mode == True", "cage approach 2 p", "persistent.performance_mode == False", At("cage approach 2 p", distortion))
    image cage approach 3 confused = ConditionSwitch("persistent.performance_mode == True", "cage approach 3 confused p", "persistent.performance_mode == False", At("cage approach 3 confused p", distortion))
    image cage approach 3 introspection talk = ConditionSwitch("persistent.performance_mode == True", "cage approach 3 introspection talk p", "persistent.performance_mode == False", At("cage approach 3 introspection talk p", distortion))
    image cage approach 3 talk = ConditionSwitch("persistent.performance_mode == True", "cage approach 3 talk p", "persistent.performance_mode == False", At("cage approach 3 talk p", distortion))
    image cage approach 3 = ConditionSwitch("persistent.performance_mode == True", "cage approach 3 p", "persistent.performance_mode == False", At("cage approach 3 p", distortion))
    image cage approach 4 talk = ConditionSwitch("persistent.performance_mode == True", "cage approach 4 talk p", "persistent.performance_mode == False", At("cage approach 4 talk p", distortion))
    image cage approach 4 = ConditionSwitch("persistent.performance_mode == True", "cage approach 4 p", "persistent.performance_mode == False", At("cage approach 4 p", distortion))
    image cage approach 5 talk = ConditionSwitch("persistent.performance_mode == True", "cage approach 5 talk p", "persistent.performance_mode == False", At("cage approach 5 talk p", distortion))
    image cage approach 5 = ConditionSwitch("persistent.performance_mode == True", "cage approach 5 p", "persistent.performance_mode == False", At("cage approach 5 p", distortion))

    image panel1 cage pop fight = ConditionSwitch("persistent.performance_mode == True", "cage pop fight 1 p", "persistent.performance_mode == False", At("cage pop fight 1 p", distortion))
    image panel2 cage pop fight = ConditionSwitch("persistent.performance_mode == True", "cage pop fight 2 p", "persistent.performance_mode == False", At("cage pop fight 2 p", distortion))
    image panel3 cage pop fight = ConditionSwitch("persistent.performance_mode == True", "cage pop fight 3 p", "persistent.performance_mode == False", At("cage pop fight 3 p", distortion))
    image panel4 cage pop fight = ConditionSwitch("persistent.performance_mode == True", "cage pop fight 4 p", "persistent.performance_mode == False", At("cage pop fight 4 p", distortion))
    image head cage pop start = ConditionSwitch("persistent.performance_mode == True", "cage pop fight head p", "persistent.performance_mode == False", At("cage pop fight head p", distortion))

    image head cage pop cold talk = ConditionSwitch("persistent.performance_mode == True", "cage pop head cold talk p", "persistent.performance_mode == False", At("cage pop head cold talk p", distortion))
    image head cage pop cough talk = ConditionSwitch("persistent.performance_mode == True", "cage pop head cough talk p", "persistent.performance_mode == False", At("cage pop head cough talk p", distortion))
    image head cage pop cough = ConditionSwitch("persistent.performance_mode == True", "cage pop head cough p", "persistent.performance_mode == False", At("cage pop head cough p", distortion))
    image head cage pop joke talk = ConditionSwitch("persistent.performance_mode == True", "cage pop head joke talk p", "persistent.performance_mode == False", At("cage pop head joke talk p", distortion))
    image head cage pop talk glance = ConditionSwitch("persistent.performance_mode == True", "cage pop head talk glance p", "persistent.performance_mode == False", At("cage pop head talk glance p", distortion))
    image head cage pop talk = ConditionSwitch("persistent.performance_mode == True", "cage pop head talk p", "persistent.performance_mode == False", At("cage pop head talk p", distortion))
    image cage reveal = ConditionSwitch("persistent.performance_mode == True", "cage reveal p", "persistent.performance_mode == False", At("cage reveal p", distortion))


    image farback cage fall = ConditionSwitch("persistent.performance_mode == True", "cg cage fall backdrop p", "persistent.performance_mode == False", At("cg cage fall backdrop p", distortion))
    image bg cage fall = ConditionSwitch("persistent.performance_mode == True", "cg cage fall bg p", "persistent.performance_mode == False", At("cg cage fall bg p", distortion))
    image fore cage fall = ConditionSwitch("persistent.performance_mode == True", "cg cage fall foreground p", "persistent.performance_mode == False", At("cg cage fall foreground p", distortion))
    image mid cage fall = ConditionSwitch("persistent.performance_mode == True", "cg cage fall midground p", "persistent.performance_mode == False", At("cg cage fall midground p", distortion))

    image farback cage free end = ConditionSwitch("persistent.performance_mode == True", "cg cage free end stars p", "persistent.performance_mode == False", At("cg cage free end stars p", distortion))
    image bg cage free end = ConditionSwitch("persistent.performance_mode == True", "cg cage free end bg p", "persistent.performance_mode == False", At("cg cage free end bg p", distortion))
    image mid cage free end = ConditionSwitch("persistent.performance_mode == True", "cg cage free end midground p", "persistent.performance_mode == False", At("cg cage free end midground p", distortion))
    image cage free end joke talk = ConditionSwitch("persistent.performance_mode == True", "cg cage free end joke talk p", "persistent.performance_mode == False", At("cg cage free end joke talk p", distortion))
    image cage free end talk = ConditionSwitch("persistent.performance_mode == True", "cg cage free end talk p", "persistent.performance_mode == False", At("cg cage free end talk p", distortion))
    image cage free end = ConditionSwitch("persistent.performance_mode == True", "cg cage free end p", "persistent.performance_mode == False", At("cg cage free end p", distortion))


    image bg cage free glance = ConditionSwitch("persistent.performance_mode == True", "cg cage free glance bg p", "persistent.performance_mode == False", At("cg cage free glance bg p", distortion))
    image cage free glance down = ConditionSwitch("persistent.performance_mode == True", "cg cage free glance down p", "persistent.performance_mode == False", At("cg cage free glance down p", distortion))
    image cg cage free glance panel 1 = ConditionSwitch("persistent.performance_mode == True", "cg cage free glance panel 1 p", "persistent.performance_mode == False", At("cg cage free glance panel 1 p", distortion))
    image cg cage free glance panel 2 = ConditionSwitch("persistent.performance_mode == True", "cg cage free glance panel 2 p", "persistent.performance_mode == False", At("cg cage free glance panel 2 p", distortion))
    image cg cage free glance panel 3 = ConditionSwitch("persistent.performance_mode == True", "cg cage free glance panel 3 p", "persistent.performance_mode == False", At("cg cage free glance panel 3 p", distortion))
    image cage free glance talk = ConditionSwitch("persistent.performance_mode == True", "cg cage free glance talk p", "persistent.performance_mode == False", At("cg cage free glance talk p", distortion))
    image cage free glance = ConditionSwitch("persistent.performance_mode == True", "cg cage free glance p", "persistent.performance_mode == False", At("cg cage free glance p", distortion))
    image cg cage free kneel = ConditionSwitch("persistent.performance_mode == True", "cg cage free kneel p", "persistent.performance_mode == False", At("cg cage free kneel p", distortion))

    image bg cage free near = ConditionSwitch("persistent.performance_mode == True", "cg cage free near bg p", "persistent.performance_mode == False", At("cg cage free near bg p", distortion))
    image farback cage free near = ConditionSwitch("persistent.performance_mode == True", "cg cage free near stars p", "persistent.performance_mode == False", At("cg cage free near stars p", distortion))
    image cage free near talk = ConditionSwitch("persistent.performance_mode == True", "cg cage free near talk p", "persistent.performance_mode == False", At("cg cage free near talk p", distortion))
    image cage free near = ConditionSwitch("persistent.performance_mode == True", "cg cage free near p", "persistent.performance_mode == False", At("cg cage free near p", distortion))

    image cg cage free offer = ConditionSwitch("persistent.performance_mode == True", "cg cage free offer p", "persistent.performance_mode == False", At("cg cage free offer p", distortion))
    image cg cage free open talk = ConditionSwitch("persistent.performance_mode == True", "cg cage free open talk p", "persistent.performance_mode == False", At("cg cage free open talk p", distortion))
    image cg cage free open = ConditionSwitch("persistent.performance_mode == True", "cg cage free open p", "persistent.performance_mode == False", At("cg cage free open p", distortion))

    image bg cage free outside = ConditionSwitch("persistent.performance_mode == True", "cg cage free outside bg p", "persistent.performance_mode == False", At("cg cage free outside bg p", distortion))
    image cage free outside cold = ConditionSwitch("persistent.performance_mode == True", "cg cage free outside cold p", "persistent.performance_mode == False", At("cg cage free outside cold p", distortion))
    image mid cage free outside = ConditionSwitch("persistent.performance_mode == True", "cg cage free outside midground p", "persistent.performance_mode == False", At("cg cage free outside midground p", distortion))
    image farback cage free outside = ConditionSwitch("persistent.performance_mode == True", "cg cage free outside stars p", "persistent.performance_mode == False", At("cg cage free outside stars p", distortion))
    image cage free outside talk = ConditionSwitch("persistent.performance_mode == True", "cg cage free outside talk p", "persistent.performance_mode == False", At("cg cage free outside talk p", distortion))
    image cage free outside = ConditionSwitch("persistent.performance_mode == True", "cg cage free outside p", "persistent.performance_mode == False", At("cg cage free outside p", distortion))

    image bg cage free point = ConditionSwitch("persistent.performance_mode == True", "cg cage free point bg p", "persistent.performance_mode == False", At("cg cage free point bg p", distortion))
    image head cage free point = ConditionSwitch("persistent.performance_mode == True", "cg cage free point head p", "persistent.performance_mode == False", At("cg cage free point head p", distortion))
    image farback cage free point = ConditionSwitch("persistent.performance_mode == True", "cg cage free point stars p", "persistent.performance_mode == False", At("cg cage free point stars p", distortion))
    image head cage free point talk = ConditionSwitch("persistent.performance_mode == True", "cg cage free point talk p", "persistent.performance_mode == False", At("cg cage free point talk p", distortion))
    image cage free point = ConditionSwitch("persistent.performance_mode == True", "cg cage free point p", "persistent.performance_mode == False", At("cg cage free point p", distortion))
    image bg cage free rise = ConditionSwitch("persistent.performance_mode == True", "cg cage free rise bg p", "persistent.performance_mode == False", At("cg cage free rise bg p", distortion))
    image chains cage free rise = ConditionSwitch("persistent.performance_mode == True", "cg cage free rise chains p", "persistent.performance_mode == False", At("cg cage free rise chains p", distortion))
    image cage free rise talk = ConditionSwitch("persistent.performance_mode == True", "cg cage free rise talk p", "persistent.performance_mode == False", At("cg cage free rise talk p", distortion))
    image cage free rise = ConditionSwitch("persistent.performance_mode == True", "cg cage free rise p", "persistent.performance_mode == False", At("cg cage free rise p", distortion))
    image cg cage free start = ConditionSwitch("persistent.performance_mode == True", "cg cage free start p", "persistent.performance_mode == False", At("cg cage free start p", distortion))


    image player cage free reach = ConditionSwitch("persistent.performance_mode == True", "player cage free reach p", "persistent.performance_mode == False", At("player cage free reach p", distortion))

    image bg cage free take = ConditionSwitch("persistent.performance_mode == True", "cg cage free take bg p", "persistent.performance_mode == False", At("cg cage free take bg p", distortion))
    image head cage free take = ConditionSwitch("persistent.performance_mode == True", "cg cage free take head p", "persistent.performance_mode == False", At("cg cage free take head p", distortion))
    image mid cage free take = ConditionSwitch("persistent.performance_mode == True", "cg cage free take midground p", "persistent.performance_mode == False", At("cg cage free take midground p", distortion))
    image head cage free take smile = ConditionSwitch("persistent.performance_mode == True", "cg cage free take smile p", "persistent.performance_mode == False", At("cg cage free take smile p", distortion))
    image head cage free take talk = ConditionSwitch("persistent.performance_mode == True", "cg cage free take talk p", "persistent.performance_mode == False", At("cg cage free take talk p", distortion))


    image cage pop approach = ConditionSwitch("persistent.performance_mode == True", "cg cage pop approach p", "persistent.performance_mode == False", At("cg cage pop approach p", distortion))
    image bg cage pop = ConditionSwitch("persistent.performance_mode == True", "cg cage pop bg p", "persistent.performance_mode == False", At("cg cage pop bg p", distortion))
    image cage pop fight start = ConditionSwitch("persistent.performance_mode == True", "cg cage pop fight start p", "persistent.performance_mode == False", At("cg cage pop fight start p", distortion))
    image mid cage pop = ConditionSwitch("persistent.performance_mode == True", "cg cage pop midground p", "persistent.performance_mode == False", At("cg cage pop midground p", distortion))
    image cage pop begin = ConditionSwitch("persistent.performance_mode == True", "cg cage pop princess p", "persistent.performance_mode == False", At("cg cage pop princess p", distortion))
    image cage pop stoop talk = ConditionSwitch("persistent.performance_mode == True", "cg cage pop stoop talk p", "persistent.performance_mode == False", At("cg cage pop stoop talk p", distortion))
    image cage pop stoop = ConditionSwitch("persistent.performance_mode == True", "cg cage pop stoop p", "persistent.performance_mode == False", At("cg cage pop stoop p", distortion))

    image bg cage slay charge = ConditionSwitch("persistent.performance_mode == True", "cg cage slay charge bg p", "persistent.performance_mode == False", At("cg cage slay charge bg p", distortion))
    image player cage slay charge = ConditionSwitch("persistent.performance_mode == True", "cg cage slay charge player p", "persistent.performance_mode == False", At("cg cage slay charge player p", distortion))
    image cage slay charge = ConditionSwitch("persistent.performance_mode == True", "cg cage slay charge princess p", "persistent.performance_mode == False", At("cg cage slay charge princess p", distortion))

    image cg cage slay collapse cold talk = ConditionSwitch("persistent.performance_mode == True", "cg cage slay collapse cold talk p", "persistent.performance_mode == False", At("cg cage slay collapse cold talk p", distortion))
    image cg cage slay collapse talk = ConditionSwitch("persistent.performance_mode == True", "cg cage slay collapse talk p", "persistent.performance_mode == False", At("cg cage slay collapse talk p", distortion))
    image cg cage slay collapse tumble talk = ConditionSwitch("persistent.performance_mode == True", "cg cage slay collapse tumble talk p", "persistent.performance_mode == False", At("cg cage slay collapse tumble talk p", distortion))
    image cg cage slay collapse tumble = ConditionSwitch("persistent.performance_mode == True", "cg cage slay collapse tumble p", "persistent.performance_mode == False", At("cg cage slay collapse tumble p", distortion))
    image cg cage slay collapse = ConditionSwitch("persistent.performance_mode == True", "cg cage slay collapse p", "persistent.performance_mode == False", At("cg cage slay collapse p", distortion))

    image bg cage slay stab = ConditionSwitch("persistent.performance_mode == True", "cg cage slay stab bg p", "persistent.performance_mode == False", At("cg cage slay stab bg p", distortion))
    image mid cage slay stab = ConditionSwitch("persistent.performance_mode == True", "cg cage slay stab midground p", "persistent.performance_mode == False", At("cg cage slay stab midground p", distortion))
    image cage slay stab = ConditionSwitch("persistent.performance_mode == True", "cg cage slay stab p", "persistent.performance_mode == False", At("cg cage slay stab p", distortion))

    image bg cage slay start = ConditionSwitch("persistent.performance_mode == True", "cg cage slay start bg p", "persistent.performance_mode == False", At("cg cage slay start bg p", distortion))
    image fore cage slay start = ConditionSwitch("persistent.performance_mode == True", "cg cage slay start foreground p", "persistent.performance_mode == False", At("cg cage slay start foreground p", distortion))
    image mid cage slay start = ConditionSwitch("persistent.performance_mode == True", "cg cage slay start midground p", "persistent.performance_mode == False", At("cg cage slay start midground p", distortion))
    image fore cage slay wrench distant = ConditionSwitch("persistent.performance_mode == True", "cg cage slay wrench distant foreground p", "persistent.performance_mode == False", At("cg cage slay wrench distant foreground p", distortion))
    image cg cage slay wrench distant talk = ConditionSwitch("persistent.performance_mode == True", "cg cage slay wrench distant talk bg p", "persistent.performance_mode == False", At("cg cage slay wrench distant talk bg p", distortion))
    image cg cage slay wrench distant = ConditionSwitch("persistent.performance_mode == True", "cg cage slay wrench distant p", "persistent.performance_mode == False", At("cg cage slay wrench distant p", distortion))
    image cage slay wrench = ConditionSwitch("persistent.performance_mode == True", "cg cage slay wrench p", "persistent.performance_mode == False", At("cg cage slay wrench p", distortion))

    image fight final cage pop = ConditionSwitch("persistent.performance_mode == True", "fight final cage pop p", "persistent.performance_mode == False", At("fight final cage pop p", distortion))

    image player cage drop = ConditionSwitch("persistent.performance_mode == True", "cg cage drop hands p", "persistent.performance_mode == False", At("cg cage drop hands p", distortion))
    image cage drop head = ConditionSwitch("persistent.performance_mode == True", "cg cage drop head p", "persistent.performance_mode == False", At("cg cage drop head p", distortion))

    image hands cage drop 1 = ConditionSwitch("persistent.performance_mode == True", "hands cage drop 1 p", "persistent.performance_mode == False", At("hands cage drop 1 p", distortion))
    image bg cage drop panel 1 = ConditionSwitch("persistent.performance_mode == True", "hands cage drop panel 1 bg p", "persistent.performance_mode == False", At("hands cage drop panel 1 bg p", distortion))
    image bg hands cage drop panel 2 = ConditionSwitch("persistent.performance_mode == True", "hands cage drop panel 2 bg p", "persistent.performance_mode == False", At("hands cage drop panel 2 bg p", distortion))
    image hands cage drop panel 2 = ConditionSwitch("persistent.performance_mode == True", "hands cage drop panel 2 p", "persistent.performance_mode == False", At("hands cage drop panel 2 p", distortion))
    image bg hands cage drop panel 3 = ConditionSwitch("persistent.performance_mode == True", "hands cage drop panel 3 bg p", "persistent.performance_mode == False", At("hands cage drop panel 3 bg p", distortion))
    image hands cage drop panel 3 = ConditionSwitch("persistent.performance_mode == True", "hands cage drop panel 3 p", "persistent.performance_mode == False", At("hands cage drop panel 3 p", distortion))
    image hands cage drop panel 4 = ConditionSwitch("persistent.performance_mode == True", "hands cage drop panel 4 p", "persistent.performance_mode == False", At("hands cage drop panel 4 p", distortion))

    image hands cage free 1 = ConditionSwitch("persistent.performance_mode == True", "hands cage free 1 p", "persistent.performance_mode == False", At("hands cage free 1 p", distortion))
    image hands cage free 2 = ConditionSwitch("persistent.performance_mode == True", "hands cage free 2 p", "persistent.performance_mode == False", At("hands cage free 2 p", distortion))
    image hands cage free 3 = ConditionSwitch("persistent.performance_mode == True", "hands cage free 3 p", "persistent.performance_mode == False", At("hands cage free 3 p", distortion))
    image hands cage free 4 = ConditionSwitch("persistent.performance_mode == True", "hands cage free 4 p", "persistent.performance_mode == False", At("hands cage free 4 p", distortion))
    image hands cage free 5 = ConditionSwitch("persistent.performance_mode == True", "hands cage free 5 p", "persistent.performance_mode == False", At("hands cage free 5 p", distortion))
    image hands cage free 6 = ConditionSwitch("persistent.performance_mode == True", "hands cage free 6 p", "persistent.performance_mode == False", At("hands cage free 6 p", distortion))
    image hands cage pop 1 = ConditionSwitch("persistent.performance_mode == True", "hands cage pop 1 p", "persistent.performance_mode == False", At("hands cage pop 1 p", distortion))
    image hands cage pop 2 = ConditionSwitch("persistent.performance_mode == True", "hands cage pop 2 p", "persistent.performance_mode == False", At("hands cage pop 2 p", distortion))
    image hands cage pop 3 = ConditionSwitch("persistent.performance_mode == True", "hands cage pop 3 p", "persistent.performance_mode == False", At("hands cage pop 3 p", distortion))
    image hands cage pop 4 = ConditionSwitch("persistent.performance_mode == True", "hands cage pop 4 p", "persistent.performance_mode == False", At("hands cage pop 4 p", distortion))
    image hands cage pop 5 = ConditionSwitch("persistent.performance_mode == True", "hands cage pop 5 p", "persistent.performance_mode == False", At("hands cage pop 5 p", distortion))
    image hands cage pop 6 = ConditionSwitch("persistent.performance_mode == True", "hands cage pop 6 p", "persistent.performance_mode == False", At("hands cage pop 6 p", distortion))

    image hands cage slay 1 = ConditionSwitch("persistent.performance_mode == True", "hands cage slay 1 p", "persistent.performance_mode == False", At("hands cage slay 1 p", distortion))
    image hands cage slay 2 = ConditionSwitch("persistent.performance_mode == True", "hands cage slay 2 p", "persistent.performance_mode == False", At("hands cage slay 2 p", distortion))
    image hands cage slay 3 = ConditionSwitch("persistent.performance_mode == True", "hands cage slay 3 p", "persistent.performance_mode == False", At("hands cage slay 3 p", distortion))
    image hands cage slay 4 = ConditionSwitch("persistent.performance_mode == True", "hands cage slay 4 p", "persistent.performance_mode == False", At("hands cage slay 4 p", distortion))
    image hands cage slay 5 = ConditionSwitch("persistent.performance_mode == True", "hands cage slay 5 p", "persistent.performance_mode == False", At("hands cage slay 5 p", distortion))
    image hands cage slay 6 = ConditionSwitch("persistent.performance_mode == True", "hands cage slay 6 p", "persistent.performance_mode == False", At("hands cage slay 6 p", distortion))
    image hands cage slay separate = ConditionSwitch("persistent.performance_mode == True", "hands cage slay separate p", "persistent.performance_mode == False", At("hands cage slay separate p", distortion))

    image player cage approach 2 blade = ConditionSwitch("persistent.performance_mode == True", "player cage approach 2 blade p", "persistent.performance_mode == False", At("player cage approach 2 blade p", distortion))
    image player cage approach 2 = ConditionSwitch("persistent.performance_mode == True", "player cage approach 2 p", "persistent.performance_mode == False", At("player cage approach 2 p", distortion))
    image player cage approach 3 blade = ConditionSwitch("persistent.performance_mode == True", "player cage approach 3 blade p", "persistent.performance_mode == False", At("player cage approach 3 blade p", distortion))
    image player cage approach 3 = ConditionSwitch("persistent.performance_mode == True", "player cage approach 3 p", "persistent.performance_mode == False", At("player cage approach 3 p", distortion))
    image player cage approach 4 knife = ConditionSwitch("persistent.performance_mode == True", "player cage approach 4 knife p", "persistent.performance_mode == False", At("player cage approach 4 knife p", distortion))
    image player cage approach 4 = ConditionSwitch("persistent.performance_mode == True", "player cage approach 4 p", "persistent.performance_mode == False", At("player cage approach 4 p", distortion))
    image player cage arm free = ConditionSwitch("persistent.performance_mode == True", "player cage arm free p", "persistent.performance_mode == False", At("player cage arm free p", distortion))
    image player cage cut 2 = ConditionSwitch("persistent.performance_mode == True", "player cage cut 2 p", "persistent.performance_mode == False", At("player cage cut 2 p", distortion))
    image player cage cut 3 = ConditionSwitch("persistent.performance_mode == True", "player cage cut 3 p", "persistent.performance_mode == False", At("player cage cut 3 p", distortion))
    image player cage cutting = ConditionSwitch("persistent.performance_mode == True", "player cage cutting p", "persistent.performance_mode == False", At("player cage cutting p", distortion))
    image player cage encounter blade = ConditionSwitch("persistent.performance_mode == True", "player cage encounter blade p", "persistent.performance_mode == False", At("player cage encounter blade p", distortion))
    image player cage encounter = ConditionSwitch("persistent.performance_mode == True", "player cage encounter p", "persistent.performance_mode == False", At("player cage encounter p", distortion))
    image player cage knife drop = ConditionSwitch("persistent.performance_mode == True", "player cage knife drop p", "persistent.performance_mode == False", At("player cage knife drop p", distortion))
    image player cage legs = ConditionSwitch("persistent.performance_mode == True", "player cage legs p", "persistent.performance_mode == False", At("player cage legs p", distortion))
    image player cage stoop = ConditionSwitch("persistent.performance_mode == True", "player cage stoop p", "persistent.performance_mode == False", At("player cage stoop p", distortion))
