label razor_final_staging:

    # starting things up
    default razor_finished = False
    default razor_just_finished = False
    default razor_blade = False
    $ razor_finished = True
    $ razor_just_finished = True
    stop music
    stop sound
    stop secondary
    $ default_mouse = "default"
    $ blade_held = False
    $ current_loop = 2
    $ quick_menu = False
    $ config.menu_include_disabled = False
    $ gallery_razor.unlock_item(11)
    $ renpy.save_persistent()
    if razor_blade:
        $ quick_menu = False
        hide bg onlayer back
        with fade
        play sound "audio/looping/uncomfortable ambiance.ogg" loop fadein 1.0
        scene chapter mad with fade
        show text _("{color=#FFFFFF00}Chapter 4. Mutually Assured Destruction.{/color}") at Position(ypos=850)
        $ renpy.pause(4.0)
        scene bg black
        with fade
        jump razor_final_start_knife
    else:
        $ quick_menu = False
        hide bg onlayer back
        with fade
        play sound "audio/looping/uncomfortable ambiance.ogg" loop fadein 1.0
        scene chapter cup with fade
        show text _("{color=#FFFFFF00}Chapter 4. The Empty Cup.{/color}") at Position(ypos=850)
        $ renpy.pause(4.0)
        scene bg black
        with fade
        jump razor_final_start_unarmed

label razor_final_start_knife:
    $ blade_held = True
    $ default_mouse = "blade"
    play music "audio/_music/ch2/razor/The Razor Slow.flac" loop
    voice "audio/voices/ch3/razor/final/narrator/1.flac"
    scene farback cabin razor3 onlayer farback at Position(ypos=1125)
    show bg cabin razor3 onlayer back at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    n "You're on a—\n{w=0.4}{nw}"
    show screen disableclick(0.5)
    voice "audio/voices/ch3/razor/final/cheated/1.flac"
    cheated "Don't lose your head. We're in a cabin, and we'll take it from here.\n"
    voice "audio/voices/ch3/razor/final/hunted/1.flac"
    hunted "Everything feels like it finally fits, doesn't it? We're up here which is different, and different is good. And our steel claw is already in our hand.\n"
    voice "audio/voices/ch3/razor/final/contrarian/1.flac"
    contrarian "Oho! What if we throw it out the window?\n"
    voice "audio/voices/ch3/razor/final/stubborn/1a.flac"
    stubborn "Over my dead body.\n"
    voice "audio/voices/ch3/razor/final/broken/1a.flac"
    broken "That wouldn't be very hard. We've died a lot. But I can't say I mind anymore.\n"
    voice "audio/voices/ch3/razor/final/smitten/1.flac"
    smitten "Besides what better way to die so very many times than at the sharp hands of a beautiful woman.\n"
    voice "audio/voices/ch3/razor/final/skeptic/1.flac"
    skeptic "I'm sure I can think of a better way to die.\n"
    voice "audio/voices/ch3/razor/final/cold/1.flac"
    cold "Eh, they're all the same, really.\n"
    voice "audio/voices/ch3/razor/final/paranoid/1.flac"
    paranoid "How about we stop thinking about horrible ways to die? I don't want us to accidentally {i}manifest{/i} anything.\n"
    voice "audio/voices/ch3/razor/final/opportunist/1.flac"
    opportunist "The only thing we're going to manifest is finally ending up on top.\n"
    voice "audio/voices/ch3/razor/final/narrator/2.flac"
    n "There are entirely too many of you. How many times have you been here?! This isn't good, this is—\n{w=5.2}{nw}"
    show screen disableclick(0.5)
    voice "audio/voices/ch3/razor/final/cheated/2.flac"
    cheated "How about you stick to describing things, and we'll stick to doing them?\n"
    voice "audio/voices/ch3/razor/final/stubborn/2.flac"
    stubborn "Yeah. Leave it to the pros. We'll notch up that win in no time.\n"
    jump razor_final_basement

label razor_final_start_unarmed:
    play music "audio/_music/ch2/razor/The Razor Slow.flac" loop
    voice "audio/voices/ch3/razor/final/narrator/1.flac"
    scene farback cabin razor3 onlayer farback at Position(ypos=1125)
    show bg cabin razor3 onlayer back at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    n "You're on a—\n{w=0.4}{nw}"
    show screen disableclick(0.5)
    voice "audio/voices/ch3/razor/final/cheated/1a.flac"
    cheated "Don't lose your head. We're in a cabin, and we'll take it from here.\n"
    voice "audio/voices/ch3/razor/final/hunted/2.flac"
    hunted "No steel claw though.\n"
    voice "audio/voices/ch3/razor/final/contrarian/2a.flac"
    contrarian "Was tossing it the only thing we've done that was permanent? That's a sick joke, universe. A sick, sick joke!\n"
    voice "audio/voices/ch3/razor/final/skeptic/2.flac"
    skeptic "If it's gone for good, then maybe we never actually needed it.\n"
    voice "audio/voices/ch3/razor/final/stubborn/3.flac"
    stubborn "That's what I've been telling you all. We can do this without it. We're tougher than steel.\n"
    voice "audio/voices/ch3/razor/final/paranoid/2.flac"
    paranoid "Yeah. Mind over matter.\n"
    voice "audio/voices/ch3/razor/final/smitten/2.flac"
    smitten "Who needs violence when you have love?\n"
    voice "audio/voices/ch3/razor/final/cold/2.flac"
    cold "Who needs love when you've mastered yourself?\n"
    voice "audio/voices/ch3/razor/final/broken/2.flac"
    broken "Who needs anything when we don't matter?\n"
    voice "audio/voices/ch3/razor/final/opportunist/2.flac"
    opportunist "Well, boys? Are we ready?\n"
    voice "audio/voices/ch3/razor/final/narrator/2.flac"
    n "There are entirely too many of you. How many times have you been here?! This isn't good, this is—\n{w=5.2}{nw}"
    show screen disableclick(0.5)
    voice "audio/voices/ch3/razor/final/cheated/2.flac"
    cheated "How about you stick to describing things, and we'll stick to doing them?\n"
    voice "audio/voices/ch3/razor/final/stubborn/4.flac"
    stubborn "Yeah. Leave it to the pros.\n"
    jump razor_final_basement

label razor_final_basement:
    voice "audio/voices/ch3/razor/final/smitten/3.flac"
    smitten "Narrator! We heroically stride through the door and towards our destined final encounter with our star-crossed lover!\n"
    voice "audio/voices/ch3/razor/final/narrator/3.flac"
    play audio "audio/final/__metal_step.flac"
    show bg cabin razor3 onlayer back at small_zoom
    with dissolve
    n "Fine by me. You walk to the door and onto the basement stairs, only—\n{w=4.4}{nw}"
    show screen disableclick(0.5)
    voice "audio/voices/ch3/razor/final/hero/1.flac"
    hero "It's more of a slide? We know.\n"
    voice "audio/voices/ch3/razor/final/narrator/4.flac"
    hide bg onlayer back
    hide farback onlayer farback
    n "Fine. I'll just shut up then and speed this whole thing along.\n"
    voice "audio/voices/ch3/razor/final/narrator/5.flac"
    n "... Are you sure you don't want me to describe the stairs? Or this room? Or anything? It feels like I'm hardly a part of this.\n"
    if razor_1_cabin_blade_taken:
        voice "audio/voices/ch3/razor/final/cheated/3.flac"
        cheated "Don't care. Just want to win.\n"
    else:
        voice "audio/voices/ch3/razor/final/cheated/4.flac"
        cheated "Don't care. Just want to see how this ends.\n"

    play audio "audio/final/__metal_step.flac"
    voice "audio/voices/ch3/razor/final/narrator/6.flac"
    scene bg basement razor3 onlayer back at Position(ypos=1125)
    show razor f start onlayer back at Position(ypos=1125)
    with Dissolve(1.0)
    n "Fine. You make your way to the basement, where the Princess awaits you.\n"
    voice "audio/voices/ch3/razor/final/princess/1.flac"
    show razor f talk1 onlayer back
    with dissolve
    sp "You know, this last time I killed you and you didn't pop right back up again?\n"
    voice "audio/voices/ch3/razor/final/princess/2.flac"
    show razor f talk2 onlayer back
    with dissolve
    sp "I thought I'd actually done it! I thought I'd cut you into so many pieces you just weren't able to stitch yourself back together.\n"
    voice "audio/voices/ch3/razor/final/princess/3.flac"
    show razor f talk3 onlayer back
    with dissolve
    sp "But I guess we're not done! That's okay with me. It's good, even. I like that!\n"
    voice "audio/voices/ch3/razor/final/princess/4a.flac"
    show razor f talk4 onlayer back
    with dissolve
    sp "I got something ready for you while you were gone. Do you want to see it?\n"
    voice "audio/voices/ch3/razor/final/princess/5.flac"
    show razor f talk5 onlayer back
    with dissolve
    sp "I'm not going to wait for an answer. I'm just gonna show you! It's worth it though. Just you wait. And not for very long, because I'm going to do it right now.\n"
    voice "audio/voices/ch3/razor/final/narrator/7.flac"
    n "...\n"
    voice "audio/voices/ch3/razor/final/hero/2.flac"
    hero "Are you going to say what she does?\n"
    voice "audio/voices/ch3/razor/final/narrator/8.flac"
    n "Oh, do you want me to talk now?\n"
    voice "audio/voices/ch3/razor/final/hero/3.flac"
    hero "Well, yeah. She says she has something new. I want to hear about the new thing.\n"
    voice "audio/voices/ch3/razor/final/cheated/5.flac"
    cheated "Yeah, me too.\n"
    voice "audio/voices/ch3/razor/final/opportunist/3.flac"
    opportunist "I think I speak for all of us when I say that I would like to hear you describe her new thing.\n"
    voice "audio/voices/ch3/razor/final/narrator/9.flac"
    n "Really? Okay then.\n"
    voice "audio/voices/ch3/razor/final/princess/6.flac"
    show razor f talk2 onlayer back
    with dissolve
    sp "Here we go! Now!\n"
    voice "audio/voices/ch3/razor/final/narrator/10.flac"
    play audio "audio/final/Razor_ButcheringBody_1.flac"
    show razor f explode1 onlayer back
    with Dissolve(0.4)
    $ renpy.pause(0.5)
    voice sustain
    show razor f explode2 onlayer back
    with Dissolve(0.4)
    n "The Princess' skin twists, splitting into red blooms of raw meat as it stretches and tears. And then it... erupts.\n"
    play audio "audio/final/Razor_FleshExplosion_1.flac"
    play tertiary "audio/final/Razor_FleshExplosion_2.flac"
    play secondary "audio/final/Razor_FleshExplosion_3.flac"
    voice "audio/voices/ch3/razor/final/narrator/11.flac"
    show razor f explode3 onlayer back
    with dissolve
    $ renpy.pause(1.0)
    voice sustain
    show bg razor3 post explode onlayer back
    show razor f final wait onlayer back
    with Dissolve(1.5)
    play tertiary "audio/final/razor_heart_loop.ogg" loop
    $ gallery_razor.unlock_item(12)
    $ renpy.save_persistent()
    n "She becomes a wave of blood and viscera, pieces of her splattering against the walls. All that remains in the center of the room is a skeleton of blades. A heart beats furiously in its cage of a chest.\n"
    voice "audio/voices/ch3/razor/final/princess/7.flac"
    show razor f final talk onlayer back
    sp "Are you ready for what comes next?\n"
    voice "audio/voices/ch3/razor/final/hero/4.flac"
    hero "Holy shit!\n"
    voice "audio/voices/ch3/razor/final/smitten/4.flac"
    smitten "She's gorgeous! Absolutely divine!\n"
    voice "audio/voices/ch3/razor/final/stubborn/5.flac"
    stubborn "Yes! Behold, the perfect woman!\n"
    voice "audio/voices/ch3/razor/final/contrarian/3.flac"
    contrarian "Do you think we can throw {i}her{/i} out the window?\n"
    voice "audio/voices/ch3/razor/final/cold/3.flac"
    cold "That looked... painful.\n"
    voice "audio/voices/ch3/razor/final/skeptic/3a.flac"
    skeptic "How is she still alive?\n"
    voice "audio/voices/ch3/razor/final/hunted/3.flac"
    hunted "Heart's still beating. That's all she needs.\n"
    voice "audio/voices/ch3/razor/final/paranoid/3.flac"
    paranoid "This is fake! This is all fake! That's all! Just made up!\n"
    #voice "audio/voices/ch3/razor/final/broken/3a.flac"
    #broken "This is all just a sick joke.\n"
    if razor_1_cabin_blade_taken:
        voice "audio/voices/ch3/razor/final/opportunist/4.flac"
        opportunist "She doesn't even have a back anymore. How are we supposed to stab her in it?\n"
    else:
        voice "audio/voices/ch3/razor/final/opportunist/5.flac"
        opportunist "I'd say we bow down to her right now if that had ever even slightly worked for us.\n"
    voice "audio/voices/ch3/razor/final/broken/3.flac"
    broken "This is all just a sick joke. I hate existing.\n"
    voice "audio/voices/ch3/razor/final/cheated/6.flac"
    cheated "We're screwed. I quit! I'm done! Forget it!\n"
    play sound "audio/final/_razor_horror_loop.ogg" loop
    if razor_blade:
        jump razor_knife_final_menu
    else:
        jump razor_empty_final_menu

    label razor_knife_final_menu:
        menu:
            extend ""

            "{i}• [[Empty your mind.]{/i}":
                # changes to ch1 basement background
                #play music "audio/music/main_theme.ogg" loop
                play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 15
                stop music
                stop sound
                hide bg onlayer back
                hide razor onlayer back
                show bg basement distant onlayer farback at Position(ypos=1190)
                show back basement distant onlayer back at Position(ypos=1190)
                show razor f final wait onlayer back at Position(ypos=1125)
                voice "audio/voices/ch3/razor/final/narrator/12.flac"
                n "... What just happened? It's so quiet.\n"
                menu:
                    extend ""

                    "{i}• [[Him too.]{/i}":
                        stop music
                        hide bg onlayer farback
                        hide back onlayer back
                        show farback quiet onlayer farback at Position(ypos=1125)
                        $ renpy.pause(1.0)
                        voice "audio/voices/ch3/razor/final/princess/8.flac"
                        sp "Something feels different about you. It almost makes {i}me{/i} feel different. Like I should actually take this seriously for once.\n"
                        play sound "audio/final/den_emerge.flac"
                        hide razor onlayer back
                        show panel1 razor final fight onlayer back at Position(ypos=1125)
                        show panel2 razor final fight onlayer front at Position(ypos=1125)
                        with Dissolve(2.0)
                        truth "You do not act, and yet through that inaction your body moves on its own. The Princess strikes as you approach, but as her blow finishes its arc, you're already somewhere else.\n"
                        voice "audio/voices/ch3/razor/final/princess/9.flac"
                        show panel2 razor final fight talk onlayer front at Position(ypos=1125)
                        with dissolve
                        sp "You're incredible.\n"
                        play audio "audio/final/_razor2_combat.flac"
                        hide panel1 onlayer back
                        hide panel2 onlayer front
                        show panel1 razor final fight progression onlayer farback at Position(ypos=1125)
                        with dissolve
                        truth "Your weapons clash again and again, you and her entering a rhythm free of thought and free of self.\n"
                        play audio "audio/final/_razor2_combat_2.flac"
                        show panel2 razor final fight progression onlayer back at Position(ypos=1125)
                        with dissolve
                        truth "There is only the dance. The ebb and flow, the shifting of the tides back and forth between you.\n"
                        play audio "audio/final/_razor2_combat_3.flac"
                        show panel3 razor final fight progression onlayer front at Position(ypos=1125)
                        with dissolve
                        truth "The deeper you fall into your play, the faster your hearts pound, and the faster the momentum volleys between you.\n"
                        play sound "audio/final/_razor2_combat_4.flac"

                        show panel4 razor final fight progression onlayer inyourface at Position(ypos=1125)
                        with dissolve
                        truth "An endlessly building crescendo and then... an opening.\n"
                        play audio "audio/final/den_emerge.flac"
                        hide panel1 onlayer farback
                        hide panel2 onlayer back
                        hide panel3 onlayer front
                        hide panel4 onlayer inyourface
                        show razor final fight killingblow onlayer front at Position(ypos=1125)
                        with dissolve
                        truth "Your blade strikes free of volition, and hers strikes, too.\n"
                        $ achievement.grant("ACH_RAZOR_FINAL")
                        stop tertiary fadeout(6.0)
                        play audio "audio/final/Adversary_HandThroughChest_2.flac"
                        show razor final fight killingblow stab onlayer front at Position(ypos=1125)
                        truth "Both strikes are lethal. Neither of you will survive, but neither of you fear what's to come. This is a good ending.\n"

        $ gallery_razor.unlock_item(13)
        $ renpy.save_persistent()
        hide player onlayer front
        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
        show arms razor2 onlayer back at Position(ypos=1125)
        show razor final fight quiet onlayer front
        with Dissolve(0.75)
        $ renpy.pause(0.125)
        show arms razor2 onlayer back
        show razor quiet final fight taken onlayer front
        with Dissolve(0.5)
        $ renpy.pause(0.125)
        hide razor onlayer front
        show arms razor3 onlayer back
        with Dissolve(0.5)
        $ renpy.pause(0.125)
        show arms razor4 onlayer back
        with Dissolve(0.5)
        $ renpy.pause(0.125)
        hide arms onlayer back
        with Dissolve(0.25)
        $ renpy.pause(0.125)
        $ blade_held = False
        $ default_mouse = "default"
        hide ribbons onlayer inyourface
        hide fore onlayer front
        hide fore onlayer inyourface
        hide farback onlayer farback
        hide bg onlayer back
        hide mid onlayer back
        hide stars onlayer farback
        hide bg onlayer back
        hide quiet onlayer back
        hide quiet onlayer front
        show farback quiet onlayer farback at Position(ypos=1125)
        with Dissolve(4.0)
        show mirror quiet distant onlayer back at Position(ypos=1125)
        if loops_finished != 0:
            truth "You do not get to see each other die. Nor will you ever. It's time for you to leave. Memory returns.\n"
        else:
            truth "You do not get to see each other die. Something has taken her away, and it's left something else in her place.\n"
        $ princess_kept += 1
        $ princess_satisfy += 1
        $ razor_end = "fight"
        $ current_princess = "razor"
        jump razor_final_mirror

    label razor_empty_final_menu:
        menu:
            extend ""

            "{i}• [[Empty your mind.]{/i}":
                # changes to ch1 basement background
                play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 15
                stop music
                stop sound
                hide bg onlayer back
                hide razor onlayer back
                show bg basement distant onlayer farback at Position(ypos=1190)
                show back basement distant onlayer back at Position(ypos=1190)
                show razor f final wait onlayer back at Position(ypos=1125)
                voice "audio/voices/ch3/razor/final/narrator/12.flac"
                n "... What just happened? It's so quiet.\n"
                menu:
                    extend ""

                    "{i}• [[Him too.]{/i}":
                        # changes to "the quiet" background
                        $ default_mouse = "eye"
                        stop music
                        hide bg onlayer farback
                        hide back onlayer back
                        show farback quiet onlayer farback at Position(ypos=1125)
                        $ renpy.pause(1.0)
                        voice "audio/voices/ch3/razor/final/princess/8.flac"
                        sp "Something feels different about you. It almost makes {i}me{/i} feel different. Like I should actually take this seriously for once.\n"
                        play sound "audio/final/den_emerge.flac"
                        hide razor onlayer back
                        show panel1 razor final fight onlayer back at Position(ypos=1125)
                        with Dissolve(1.0)
                        truth "You do not act as the Princess approaches, instead allowing her to crash against your form. And yet, there is seemingly nothing for her to crash against.\n"
                        play audio "audio/final/razor_dodge_neo.flac"
                        show panel2 razor final fight onlayer front at Position(ypos=1125)
                        with Dissolve(1.0)
                        truth "Again and again she swings at 'you,' but there never really was a 'you' to swing at.\n"
                        voice "audio/voices/ch3/razor/final/princess/10.flac"
                        show panel2 razor final fight talk onlayer front
                        sp "This worked before. I was able to make you dead before!\n"
                        play audio "audio/final/razor_smash.flac"
                        hide farback onlayer farback
                        hide panel1 onlayer back
                        hide panel2 onlayer front
                        scene bg black
                        $ renpy.pause(0.25)
                        show farback quiet onlayer farback at Position(ypos=1125)
                        show razor pacifism 3 talk onlayer front at Position(ypos=1125)
                        with fade
                        truth "She swings again, and this time, she hits something, or something hits her. She looks down in confused terror as her arm bends and folds in upon itself.\n"
                        voice "audio/voices/ch3/razor/final/princess/11.flac"
                        show razor pacifism 3 talk2 onlayer front
                        sp "Did you do that? It's funny if you did. You're nothing! You've done nothing to me and I've done so much to you and—\n"
                        voice "audio/voices/ch3/razor/final/princess/12.flac"
                        show razor pacifism 3 talk2 onlayer front
                        sp "That's who we are. But it's like you're nothing now. You can't be nothing! If you're nothing, then what am I? Am I nothing, too?\n"
                        voice "audio/voices/ch3/razor/final/princess/13.flac"
                        show razor pacifism 4 attack onlayer front
                        with dissolve
                        sp "No! I'm the one who hurts you!\n"
                        play audio "audio/final/razor_insane_2.flac"
                        show razor pacifism 4 attack anim onlayer front
                        truth "She hurls herself at you, but as she does, her metal body bends outward, the very contact with what you are repelling her to the point of destruction.\n"
                        play audio "audio/one_shot/stab_goop.flac"
                        $ achievement.grant("ACH_RAZOR_PACIFISM")
                        $ quick_menu = False
                        hide farback onlayer farback
                        hide razor onlayer front
                        scene bg black
                        with fade
                        show farback quiet onlayer farback at Position(ypos=1125)
                        show razor pacifism heart onlayer front at Position(ypos=1125)
                        with fade
                        if persistent.quick_menu:
                            $ quick_menu = True
                        truth "The din of shrieking metal subsides, and something small and delicate falls into your hand. It's her heart. It beats gently, calmly, in your palm.\n"
                        #voice "audio/voices/ch3/razor/final/princess/14.flac"
                        #sp "Oh.\n"
                        $ gallery_razor.unlock_item(14)
                        $ gallery_razor.unlock_item(15)
                        $ renpy.save_persistent()
                        stop tertiary fadeout 5.0
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show hand razorheart reach onlayer back at Position(ypos=1125)
                        with Dissolve(0.5)
                        $ renpy.pause(0.125)
                        hide hand onlayer back
                        show hand razorheart take onlayer front at Position(ypos=1125)
                        with Dissolve(0.5)
                        $ renpy.pause(0.125)
                        hide hand onlayer front
                        hide razor onlayer front
                        show player pacifism posttake onlayer front at Position(ypos=1125)
                        show hand razorheart leave onlayer back at Position(ypos=1125)
                        with Dissolve(0.5)
                        $ renpy.pause(0.125)
                        hide hand onlayer back
                        with Dissolve(0.25)
                        $ renpy.pause(0.125)
                        hide player onlayer front
                        $ blade_held = False
                        $ default_mouse = "default"
                        hide ribbons onlayer inyourface
                        hide fore onlayer front
                        hide fore onlayer inyourface
                        hide farback onlayer farback
                        hide bg onlayer back
                        hide mid onlayer back
                        hide stars onlayer farback
                        hide bg onlayer back
                        hide quiet onlayer back
                        hide quiet onlayer front
                        show farback quiet onlayer farback at Position(ypos=1125)
                        with Dissolve(4.0)
                        show mirror quiet distant onlayer back at Position(ypos=1125)
                        if loops_finished != 0:
                            truth "Not another word is spoken. It's time for you to leave. Memory returns.\n"
                        else:
                            truth "Not another word is spoken. Something has taken her away, and it's left something else in her place.\n"
                        $ razor_end = "peace"
                        $ current_princess = "razorheart"
                        $ princess_kept += 1
                        $ princess_satisfy += 1
                        jump razor_final_mirror

label razor_final_mirror:

    menu:
        extend ""

        "{i}• [[Approach the mirror.]{/i}":
            hide mirror onlayer back
            show content m empty onlayer front at Position(ypos=1125)
            show mirror frame onlayer front at Position(ypos=1125)
            with Dissolve(2.0)
            truth "You do so.\n"
            jump mirror_n_wipe
return
