label den_pristine_art_staging:

    image farback den abandon = ConditionSwitch("persistent.performance_mode == True", "bg den abandon bg p", "persistent.performance_mode == False", At("bg den abandon bg p", distortion))
    image dust den abandon collapsing = ConditionSwitch("persistent.performance_mode == True", "bg den abandon collapsing dust p", "persistent.performance_mode == False", At("bg den abandon collapsing dust p", distortion))
    image player den abandon collapsing blade = ConditionSwitch("persistent.performance_mode == True", "bg den abandon collapsing player blade p", "persistent.performance_mode == False", At("bg den abandon collapsing player blade p", distortion))
    image player den abandon collapsing = ConditionSwitch("persistent.performance_mode == True", "bg den abandon collapsing player p", "persistent.performance_mode == False", At("bg den abandon collapsing player p", distortion))
    image bg den abandon collapsing = ConditionSwitch("persistent.performance_mode == True", "bg den abandon collapsing p", "persistent.performance_mode == False", At("bg den abandon collapsing p", distortion))
    image player den abandon blade = ConditionSwitch("persistent.performance_mode == True", "bg den abandon player blade p", "persistent.performance_mode == False", At("bg den abandon player blade p", distortion))
    image player den abandon = ConditionSwitch("persistent.performance_mode == True", "bg den abandon player p", "persistent.performance_mode == False", At("bg den abandon player p", distortion))
    image bg den abandon = ConditionSwitch("persistent.performance_mode == True", "bg den abandon p", "persistent.performance_mode == False", At("bg den abandon p", distortion))
    image starving den buried 1 = ConditionSwitch("persistent.performance_mode == True", "bg den buried starving 1 p", "persistent.performance_mode == False", At("bg den buried starving 1 p", distortion))
    image starving den buried 2 = ConditionSwitch("persistent.performance_mode == True", "bg den buried starving 2 p", "persistent.performance_mode == False", At("bg den buried starving 2 p", distortion))
    image starving den buried 3 = ConditionSwitch("persistent.performance_mode == True", "bg den buried starving 3 p", "persistent.performance_mode == False", At("bg den buried starving 3 p", distortion))
    image starving den buried 4 = ConditionSwitch("persistent.performance_mode == True", "bg den buried starving 4 p", "persistent.performance_mode == False", At("bg den buried starving 4 p", distortion))
    image starving den buried 5 = ConditionSwitch("persistent.performance_mode == True", "bg den buried starving 5 p", "persistent.performance_mode == False", At("bg den buried starving 5 p", distortion))
    image bg den buried = ConditionSwitch("persistent.performance_mode == True", "bg den buried p", "persistent.performance_mode == False", At("bg den buried p", distortion))
    image panel1 den approach friend soft = ConditionSwitch("persistent.performance_mode == True", "den approach friend soft panel 1 p", "persistent.performance_mode == False", At("den approach friend soft panel 1 p", distortion))
    image panel2 den approach friend soft = ConditionSwitch("persistent.performance_mode == True", "den approach friend soft panel 2 p", "persistent.performance_mode == False", At("den approach friend soft panel 2 p", distortion))

    image panel3 den approach friend soft delayed:
        "emptyimage"
        12.5
        "panel3 den approach friend soft"

    image panel3 den approach friend soft = ConditionSwitch("persistent.performance_mode == True", "den approach friend soft panel 3 p", "persistent.performance_mode == False", At("den approach friend soft panel 3 p", distortion))
    image player den approach hand offer friend = ConditionSwitch("persistent.performance_mode == True", "den approach hand offer friend player p", "persistent.performance_mode == False", At("den approach hand offer friend player p", distortion))
    image den approach hand offer friend = ConditionSwitch("persistent.performance_mode == True", "den approach hand offer friend p", "persistent.performance_mode == False", At("den approach hand offer friend p", distortion))
    image den approach ready = ConditionSwitch("persistent.performance_mode == True", "den approach ready p", "persistent.performance_mode == False", At("den approach ready p", distortion))
    image den approach slay charge = ConditionSwitch("persistent.performance_mode == True", "den approach slay charge p", "persistent.performance_mode == False", At("den approach slay charge p", distortion))
    image den approach slay counter = ConditionSwitch("persistent.performance_mode == True", "den approach slay counter bg p", "persistent.performance_mode == False", At("den approach slay counter bg p", distortion))
    image fore den approach slay counter = ConditionSwitch("persistent.performance_mode == True", "den approach slay counter foreground p", "persistent.performance_mode == False", At("den approach slay counter foreground p", distortion))
    image bg den battle grin open = ConditionSwitch("persistent.performance_mode == True", "den battle grin open bg p", "persistent.performance_mode == False", At("den battle grin open bg p", distortion))
    image den battle grin open = ConditionSwitch("persistent.performance_mode == True", "den battle grin open p", "persistent.performance_mode == False", At("den battle grin open p", distortion))
    image bg den battle losing = ConditionSwitch("persistent.performance_mode == True", "den battle losing bg p", "persistent.performance_mode == False", At("den battle losing bg p", distortion))
    image panel1 den battle losing = ConditionSwitch("persistent.performance_mode == True", "den battle losing panel 1 p", "persistent.performance_mode == False", At("den battle losing panel 1 p", distortion))
    image panel2 den battle losing = ConditionSwitch("persistent.performance_mode == True", "den battle losing panel 2 p", "persistent.performance_mode == False", At("den battle losing panel 2 p", distortion))
    image den buried eye closed = ConditionSwitch("persistent.performance_mode == True", "den buried eye closed p", "persistent.performance_mode == False", At("den buried eye closed p", distortion))
    image den buried eye open = ConditionSwitch("persistent.performance_mode == True", "den buried eye open p", "persistent.performance_mode == False", At("den buried eye open p", distortion))
    image den buried eye sad = ConditionSwitch("persistent.performance_mode == True", "den buried eye sad p", "persistent.performance_mode == False", At("den buried eye sad p", distortion))
    image den buried eye sadder = ConditionSwitch("persistent.performance_mode == True", "den buried eye sadder p", "persistent.performance_mode == False", At("den buried eye sadder p", distortion))
    image den buried eye saddest = ConditionSwitch("persistent.performance_mode == True", "den buried eye saddest p", "persistent.performance_mode == False", At("den buried eye saddest p", distortion))
    image farback den collapse alone = ConditionSwitch("persistent.performance_mode == True", "den collapse alone bg p", "persistent.performance_mode == False", At("den collapse alone bg p", distortion))
    image den collapse alone noprincess = ConditionSwitch("persistent.performance_mode == True", "den collapse alone noprincess p", "persistent.performance_mode == False", At("den collapse alone noprincess p", distortion))
    image den collapse alone = ConditionSwitch("persistent.performance_mode == True", "den collapse alone p", "persistent.performance_mode == False", At("den collapse alone p", distortion))

    image bg den fight fear = ConditionSwitch("persistent.performance_mode == True", "den fight fear bg p", "persistent.performance_mode == False", At("den fight fear bg p", distortion))
    image den fight fear = ConditionSwitch("persistent.performance_mode == True", "den fight fear p", "persistent.performance_mode == False", At("den fight fear p", distortion))

    image bg den fight pounce = ConditionSwitch("persistent.performance_mode == True", "den fight pounce bg p", "persistent.performance_mode == False", At("den fight pounce bg p", distortion))
    image den fight pounce = ConditionSwitch("persistent.performance_mode == True", "den fight pounce p", "persistent.performance_mode == False", At("den fight pounce p", distortion))

    image den flinch grab = ConditionSwitch("persistent.performance_mode == True", "den flinch grab p", "persistent.performance_mode == False", At("den flinch grab p", distortion))
    image bg den flinch chomp = ConditionSwitch("persistent.performance_mode == True", "den flinch chomp bg p", "persistent.performance_mode == False", At("den flinch chomp bg p", distortion))
    image den flinch chomp = ConditionSwitch("persistent.performance_mode == True", "den flinch chomp p", "persistent.performance_mode == False", At("den flinch chomp p", distortion))
    image den free 1 = ConditionSwitch("persistent.performance_mode == True", "den free 1 p", "persistent.performance_mode == False", At("den free 1 p", distortion))
    image den free 2 = ConditionSwitch("persistent.performance_mode == True", "den free 2 p", "persistent.performance_mode == False", At("den free 2 p", distortion))
    image farback den free collapse = ConditionSwitch("persistent.performance_mode == True", "den free collapse stars p", "persistent.performance_mode == False", At("den free collapse stars p", distortion))
    image den free collapse = ConditionSwitch("persistent.performance_mode == True", "den free collapse p", "persistent.performance_mode == False", At("den free collapse p", distortion))
    image bg den free final = ConditionSwitch("persistent.performance_mode == True", "den free final bg p", "persistent.performance_mode == False", At("den free final bg p", distortion))
    image farback den free final = ConditionSwitch("persistent.performance_mode == True", "den free final stars p", "persistent.performance_mode == False", At("den free final stars p", distortion))
    image den free final = ConditionSwitch("persistent.performance_mode == True", "den free final p", "persistent.performance_mode == False", At("den free final p", distortion))
    image den free resigned = ConditionSwitch("persistent.performance_mode == True", "den free resigned p", "persistent.performance_mode == False", At("den free resigned p", distortion))
    image den free surprise = ConditionSwitch("persistent.performance_mode == True", "den free surprise p", "persistent.performance_mode == False", At("den free surprise p", distortion))
    image den free swing = ConditionSwitch("persistent.performance_mode == True", "den free swing p", "persistent.performance_mode == False", At("den free swing p", distortion))
    image den friend appear = ConditionSwitch("persistent.performance_mode == True", "den friend appear p", "persistent.performance_mode == False", At("den friend appear p", distortion))
    image bg den friend carry = ConditionSwitch("persistent.performance_mode == True", "den friend carry bg p", "persistent.performance_mode == False", At("den friend carry bg p", distortion))
    image den friend carry = ConditionSwitch("persistent.performance_mode == True", "den friend carry her p", "persistent.performance_mode == False", At("den friend carry her p", distortion))
    image farback den friend carry = ConditionSwitch("persistent.performance_mode == True", "den friend carry stars p", "persistent.performance_mode == False", At("den friend carry stars p", distortion))
    image den friend collapse 1 = ConditionSwitch("persistent.performance_mode == True", "den friend collapse 1 p", "persistent.performance_mode == False", At("den friend collapse 1 p", distortion))
    image den friend collapse 2 = ConditionSwitch("persistent.performance_mode == True", "den friend collapse 2 p", "persistent.performance_mode == False", At("den friend collapse 2 p", distortion))
    image dust den friend collapse dig 2 = ConditionSwitch("persistent.performance_mode == True", "den friend collapse dig 2 dust p", "persistent.performance_mode == False", At("den friend collapse dig 2 dust p", distortion))
    image den friend collapse dig 2 = ConditionSwitch("persistent.performance_mode == True", "den friend collapse dig 2 p", "persistent.performance_mode == False", At("den friend collapse dig 2 p", distortion))
    image dust den friend collapse dig = ConditionSwitch("persistent.performance_mode == True", "den friend collapse dig dust p", "persistent.performance_mode == False", At("den friend collapse dig dust p", distortion))
    image den friend collapse dig = ConditionSwitch("persistent.performance_mode == True", "den friend collapse dig p", "persistent.performance_mode == False", At("den friend collapse dig p", distortion))
    image den friend pluck = ConditionSwitch("persistent.performance_mode == True", "den friend pluck p", "persistent.performance_mode == False", At("den friend pluck p", distortion))
    image den friend tug free = ConditionSwitch("persistent.performance_mode == True", "den friend tug free p", "persistent.performance_mode == False", At("den friend tug free p", distortion))
    image den friend tug = ConditionSwitch("persistent.performance_mode == True", "den friend tug p", "persistent.performance_mode == False", At("den friend tug p", distortion))

    image bg den hero charge = ConditionSwitch("persistent.performance_mode == True", "den hero charge bg p", "persistent.performance_mode == False", At("den hero charge bg p", distortion))
    image den hero charge = ConditionSwitch("persistent.performance_mode == True", "den hero charge p", "persistent.performance_mode == False", At("den hero charge p", distortion))

    image den hero collapse cold = ConditionSwitch("persistent.performance_mode == True", "den hero collapse cold p", "persistent.performance_mode == False", At("den hero collapse cold p", distortion))
    image den hero collapse shame = ConditionSwitch("persistent.performance_mode == True", "den hero collapse shame p", "persistent.performance_mode == False", At("den hero collapse shame p", distortion))
    image den hero collapse = ConditionSwitch("persistent.performance_mode == True", "den hero collapse p", "persistent.performance_mode == False", At("den hero collapse p", distortion))

    image bg den hero fight = ConditionSwitch("persistent.performance_mode == True", "den hero fight bg p", "persistent.performance_mode == False", At("den hero fight bg p", distortion))
    image den hero fight = ConditionSwitch("persistent.performance_mode == True", "den hero fight p", "persistent.performance_mode == False", At("den hero fight p", distortion))

    image bg den hero fuse = ConditionSwitch("persistent.performance_mode == True", "den hero fuse bg p", "persistent.performance_mode == False", At("den hero fuse bg p", distortion))
    image den hero fuse = ConditionSwitch("persistent.performance_mode == True", "den hero fuse p", "persistent.performance_mode == False", At("den hero fuse p", distortion))

    image bg den instinct charge = ConditionSwitch("persistent.performance_mode == True", "den instinct charge bg p", "persistent.performance_mode == False", At("den instinct charge bg p", distortion))
    image den instinct charge = ConditionSwitch("persistent.performance_mode == True", "den instinct charge p", "persistent.performance_mode == False", At("den instinct charge p", distortion))
    image player den instinct cold = ConditionSwitch("persistent.performance_mode == True", "den instinct cold player p", "persistent.performance_mode == False", At("den instinct cold player p", distortion))
    image den instinct cold = ConditionSwitch("persistent.performance_mode == True", "den instinct cold p", "persistent.performance_mode == False", At("den instinct cold p", distortion))
    image bg den instinct eat 1 = ConditionSwitch("persistent.performance_mode == True", "den instinct eat 1 bg p", "persistent.performance_mode == False", At("den instinct eat 1 bg p", distortion))
    image den instinct eat 1 = ConditionSwitch("persistent.performance_mode == True", "den instinct eat 1 p", "persistent.performance_mode == False", At("den instinct eat 1 p", distortion))
    image bg den instinct eat 2 = ConditionSwitch("persistent.performance_mode == True", "den instinct eat 2 bg p", "persistent.performance_mode == False", At("den instinct eat 2 bg p", distortion))
    image panel1 den instinct eat 2 = ConditionSwitch("persistent.performance_mode == True", "den instinct eat 2 panel 1 p", "persistent.performance_mode == False", At("den instinct eat 2 panel 1 p", distortion))
    image panel2 den instinct eat 2 = ConditionSwitch("persistent.performance_mode == True", "den instinct eat 2 panel 2 p", "persistent.performance_mode == False", At("den instinct eat 2 panel 2 p", distortion))

    image panel2 den instinct eat 2 delayed:
        "emptyimage"
        10.78
        "panel2 den instinct eat 2"

    image den instinct eat 3 = ConditionSwitch("persistent.performance_mode == True", "den instinct eat 3 p", "persistent.performance_mode == False", At("den instinct eat 3 p", distortion))

    image panel1 den instinct eat 4 = ConditionSwitch("persistent.performance_mode == True", "den instinct eat 4 panel 1 p", "persistent.performance_mode == False", At("den instinct eat 4 panel 1 p", distortion))
    image panel2 den instinct eat 4 = ConditionSwitch("persistent.performance_mode == True", "den instinct eat 4 panel 2 p", "persistent.performance_mode == False", At("den instinct eat 4 panel 2 p", distortion))

    image panel2 den instinct eat 4 delayed:
        "emptyimage"
        6.8
        "panel2 den instinct eat 4"

    image bg den instinct eat 5 = ConditionSwitch("persistent.performance_mode == True", "den instinct eat 5 bg p", "persistent.performance_mode == False", At("den instinct eat 5 bg p", distortion))
    image den instinct eat 5 = ConditionSwitch("persistent.performance_mode == True", "den instinct eat 5 p", "persistent.performance_mode == False", At("den instinct eat 5 p", distortion))

    image bg den instinct eat finale 2 = ConditionSwitch("persistent.performance_mode == True", "den instinct eat finale 2 bg p", "persistent.performance_mode == False", At("den instinct eat finale 2 bg p", distortion))
    image player den instinct eat finale 2 = ConditionSwitch("persistent.performance_mode == True", "den instinct eat finale 2 player p", "persistent.performance_mode == False", At("den instinct eat finale 2 player p", distortion))
    image den instinct eat finale 2 = ConditionSwitch("persistent.performance_mode == True", "den instinct eat finale 2 p", "persistent.performance_mode == False", At("den instinct eat finale 2 p", distortion))

    image panel1 den instinct eat finale = ConditionSwitch("persistent.performance_mode == True", "den instinct eat finale panel 1 p", "persistent.performance_mode == False", At("den instinct eat finale panel 1 p", distortion))

    image panel2 den instinct eat finale delayed:
        "emptyimage"
        5.2
        "panel2 den instinct eat finale"

    image panel2 den instinct eat finale = ConditionSwitch("persistent.performance_mode == True", "den instinct eat finale panel 2 p", "persistent.performance_mode == False", At("den instinct eat finale panel 2 p", distortion))

    image panel3 den instinct eat finale delayed:
        "emptyimage"
        11.5
        "panel3 den instinct eat finale"

    image panel3 den instinct eat finale = ConditionSwitch("persistent.performance_mode == True", "den instinct eat finale panel 3 p", "persistent.performance_mode == False", At("den instinct eat finale panel 3 p", distortion))

    image den instinct eat finale 4 = ConditionSwitch("persistent.performance_mode == True", "den instinct eat finale panel 4 beast p", "persistent.performance_mode == False", At("den instinct eat finale panel 4 beast p", distortion))
    image player den instinct eat finale 4 = ConditionSwitch("persistent.performance_mode == True", "den instinct eat finale panel 4 hands p", "persistent.performance_mode == False", At("den instinct eat finale panel 4 hands p", distortion))
    image den instinct eat finale 5 = ConditionSwitch("persistent.performance_mode == True", "den instinct eat finale panel 5 beast p", "persistent.performance_mode == False", At("den instinct eat finale panel 5 beast p", distortion))
    image player den instinct eat finale 5 = ConditionSwitch("persistent.performance_mode == True", "den instinct eat finale panel 5 hands p", "persistent.performance_mode == False", At("den instinct eat finale panel 5 hands p", distortion))
    image den instinct eat finale 6 = ConditionSwitch("persistent.performance_mode == True", "den instinct eat finale panel 6 p", "persistent.performance_mode == False", At("den instinct eat finale panel 6 p", distortion))

    image hands den approach slay 1 = ConditionSwitch("persistent.performance_mode == True", "hands den approach slay 1 p", "persistent.performance_mode == False", At("hands den approach slay 1 p", distortion))
    image hands den approach slay 2 = ConditionSwitch("persistent.performance_mode == True", "hands den approach slay 2 p", "persistent.performance_mode == False", At("hands den approach slay 2 p", distortion))
    image hands den approach slay 3 = ConditionSwitch("persistent.performance_mode == True", "hands den approach slay 3 p", "persistent.performance_mode == False", At("hands den approach slay 3 p", distortion))
    image hands den approach slay 4 = ConditionSwitch("persistent.performance_mode == True", "hands den approach slay 4 p", "persistent.performance_mode == False", At("hands den approach slay 4 p", distortion))
    image hands den approach slay 5 = ConditionSwitch("persistent.performance_mode == True", "hands den approach slay 5 p", "persistent.performance_mode == False", At("hands den approach slay 5 p", distortion))
    image hands den approach slay 6 = ConditionSwitch("persistent.performance_mode == True", "hands den approach slay 6 p", "persistent.performance_mode == False", At("hands den approach slay 6 p", distortion))
    image bg hands den approach start = ConditionSwitch("persistent.performance_mode == True", "hands den approach start bg p", "persistent.performance_mode == False", At("hands den approach start bg p", distortion))
    image hands den approach start = ConditionSwitch("persistent.performance_mode == True", "hands den approach start p", "persistent.performance_mode == False", At("hands den approach start p", distortion))

    image hands den buried 1 = ConditionSwitch("persistent.performance_mode == True", "hands den buried 1 p", "persistent.performance_mode == False", At("hands den buried 1 p", distortion))
    image hands den buried 2 = ConditionSwitch("persistent.performance_mode == True", "hands den buried 2 p", "persistent.performance_mode == False", At("hands den buried 2 p", distortion))
    image hands den buried 3 = ConditionSwitch("persistent.performance_mode == True", "hands den buried 3 p", "persistent.performance_mode == False", At("hands den buried 3 p", distortion))
    image hands den buried 4 = ConditionSwitch("persistent.performance_mode == True", "hands den buried 4 p", "persistent.performance_mode == False", At("hands den buried 4 p", distortion))
    image hands den buried 5 = ConditionSwitch("persistent.performance_mode == True", "hands den buried 5 p", "persistent.performance_mode == False", At("hands den buried 5 p", distortion))
    image hands den buried 6 = ConditionSwitch("persistent.performance_mode == True", "hands den buried 6 p", "persistent.performance_mode == False", At("hands den buried 6 p", distortion))
    image hands den buried start = ConditionSwitch("persistent.performance_mode == True", "hands den buried start p", "persistent.performance_mode == False", At("hands den buried start p", distortion))
    image hands den flinch 2 = ConditionSwitch("persistent.performance_mode == True", "hands den flinch 2 p", "persistent.performance_mode == False", At("hands den flinch 2 p", distortion))
    image hands den flinch 3 = ConditionSwitch("persistent.performance_mode == True", "hands den flinch 3 p", "persistent.performance_mode == False", At("hands den flinch 3 p", distortion))
    image hands den flinch 4 = ConditionSwitch("persistent.performance_mode == True", "hands den flinch 4 p", "persistent.performance_mode == False", At("hands den flinch 4 p", distortion))
    image hands den flinch 5 = ConditionSwitch("persistent.performance_mode == True", "hands den flinch 5 p", "persistent.performance_mode == False", At("hands den flinch 5 p", distortion))
    image hands den flinch 6 = ConditionSwitch("persistent.performance_mode == True", "hands den flinch 6 p", "persistent.performance_mode == False", At("hands den flinch 6 p", distortion))
    image hands den flinch = ConditionSwitch("persistent.performance_mode == True", "hands den flinch p", "persistent.performance_mode == False", At("hands den flinch p", distortion))
    image hands den free 1 = ConditionSwitch("persistent.performance_mode == True", "hands den free 1 p", "persistent.performance_mode == False", At("hands den free 1 p", distortion))
    image hands den free 2 = ConditionSwitch("persistent.performance_mode == True", "hands den free 2 p", "persistent.performance_mode == False", At("hands den free 2 p", distortion))
    image hands den free 3 = ConditionSwitch("persistent.performance_mode == True", "hands den free 3 p", "persistent.performance_mode == False", At("hands den free 3 p", distortion))
    image hands den free 4 = ConditionSwitch("persistent.performance_mode == True", "hands den free 4 p", "persistent.performance_mode == False", At("hands den free 4 p", distortion))
    image hands den free 5 = ConditionSwitch("persistent.performance_mode == True", "hands den free 5 p", "persistent.performance_mode == False", At("hands den free 5 p", distortion))
    image hands den free 6 = ConditionSwitch("persistent.performance_mode == True", "hands den free 6 p", "persistent.performance_mode == False", At("hands den free 6 p", distortion))
    image hands den hero 1 = ConditionSwitch("persistent.performance_mode == True", "hands den hero 1 p", "persistent.performance_mode == False", At("hands den hero 1 p", distortion))
    image hands den hero 2 = ConditionSwitch("persistent.performance_mode == True", "hands den hero 2 p", "persistent.performance_mode == False", At("hands den hero 2 p", distortion))
    image hands den hero 3 = ConditionSwitch("persistent.performance_mode == True", "hands den hero 3 p", "persistent.performance_mode == False", At("hands den hero 3 p", distortion))
    image hands den hero 4 = ConditionSwitch("persistent.performance_mode == True", "hands den hero 4 p", "persistent.performance_mode == False", At("hands den hero 4 p", distortion))
    image hands den hero 5 = ConditionSwitch("persistent.performance_mode == True", "hands den hero 5 p", "persistent.performance_mode == False", At("hands den hero 5 p", distortion))
    image hands den hero 6 = ConditionSwitch("persistent.performance_mode == True", "hands den hero 6 p", "persistent.performance_mode == False", At("hands den hero 6 p", distortion))

    image player den instinct 1 = ConditionSwitch("persistent.performance_mode == True", "hands den instinct 1 player p", "persistent.performance_mode == False", At("hands den instinct 1 player p", distortion))
    image player den instinct 2 = ConditionSwitch("persistent.performance_mode == True", "hands den instinct 2 player foreground p", "persistent.performance_mode == False", At("hands den instinct 2 player foreground p", distortion))


    image hands den instinct 1 = ConditionSwitch("persistent.performance_mode == True", "hands den instinct 1 p", "persistent.performance_mode == False", At("hands den instinct 1 p", distortion))
    image player hands den instinct 2  = ConditionSwitch("persistent.performance_mode == True", "hands den instinct 2 player p", "persistent.performance_mode == False", At("hands den instinct 2 player p", distortion))
    image hands den instinct 2 = ConditionSwitch("persistent.performance_mode == True", "hands den instinct 2 p", "persistent.performance_mode == False", At("hands den instinct 2 p", distortion))
    image player hands den instinct 3 = ConditionSwitch("persistent.performance_mode == True", "hands den instinct 3 player p", "persistent.performance_mode == False", At("hands den instinct 3 player p", distortion))
    image hands den instinct 3 = ConditionSwitch("persistent.performance_mode == True", "hands den instinct 3 p", "persistent.performance_mode == False", At("hands den instinct 3 p", distortion))
    image player hands den instinct 4 = ConditionSwitch("persistent.performance_mode == True", "hands den instinct 4 player p", "persistent.performance_mode == False", At("hands den instinct 4 player p", distortion))
    image hands den instinct 4 = ConditionSwitch("persistent.performance_mode == True", "hands den instinct 4 p", "persistent.performance_mode == False", At("hands den instinct 4 p", distortion))
    image player hands den instinct 5 = ConditionSwitch("persistent.performance_mode == True", "hands den instinct 5 player p", "persistent.performance_mode == False", At("hands den instinct 5 player p", distortion))
    image hands den instinct 5 = ConditionSwitch("persistent.performance_mode == True", "hands den instinct 5 p", "persistent.performance_mode == False", At("hands den instinct 5 p", distortion))
    image hands den instinct 6 = ConditionSwitch("persistent.performance_mode == True", "hands den instinct 6 p", "persistent.performance_mode == False", At("hands den instinct 6 p", distortion))
