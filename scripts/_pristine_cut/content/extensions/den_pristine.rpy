label den_pristine_fight:

    voice "audio/_pristine/voice/den/narrator/1.flac"
    hide bg onlayer farback
    hide den onlayer back
    show bg den fight fear onlayer farback at Position(ypos=1125)
    show den fight fear onlayer back at Position(ypos=1125)
    with Dissolve(1.0)
    n "Her gleaming eyes watch you from the shadows, unblinking. There's fear in them now. But it is a fear wreathed in fury. And beneath it all lurks something far more primal.\n"
    voice "audio/_pristine/voice/den/hunted/1.flac"
    hunted "Hunger.\n"
    voice "audio/_pristine/voice/den/narrator/2.flac"
    n "Yes. She knows your strength now, and she wishes to devour it. How unseemly.\n"
    voice "audio/_pristine/voice/den/stubborn/1.flac"
    stubborn "I'd like to see her try.\n"
    #added "desperate" and removed "fear", we want hunger to be the motivator for the fight
    #voice "audio/_pristine/voice/den/hunted/2.flac"
    #hunted "You're too bold. Hunger makes her desperate. Makes her careless. Fear does the same, but hunger is so much worse.\n"
    #voice "audio/_pristine/voice/den/stubborn/2.flac"
    #stubborn "There's nothing wrong with careless. If she's careless, she'll make mistakes.\n"
    #voice "audio/_pristine/voice/den/hunted/3.flac"
    #hunted "Careless is dangerous.\n"

    # CUT SCREAM
    voice "audio/_pristine/voice/den/narrator/3a.flac"
    play secondary "audio/final/den_charge.flac"
    queue secondary "audio/_pristine/sfx/den_swing.flac"
    hide bg onlayer farback
    hide den onlayer back
    show bg den fight pounce onlayer farback at Position(ypos=1125)
    show den fight pounce onlayer back at shakeshort, Position(ypos=1125)
    with Dissolve(1.0)
    n "The Princess lunges with even more ferocity than before. Both voices were right. Within that ferocity there is the clumsiness of doubt; a chaotic dance between impulse and restraint.\n"
    #n "The Princess lunges with even more ferocity than before. Both voices were right. Within that ferocity there is the clumsiness of hesitation, but there is also a careless desperation; a chaotic dance between restraint and impulse.\n"
    voice "audio/_pristine/voice/den/narrator/4.flac"
    play audio "audio/final/Tower_KnifeBlow_SEQUENCED_5.flac"
    play secondary "audio/final/Beast_ClawsRipping_1.flac"
    queue secondary "audio/final/Beast_ClawsRipping_2.flac"
    queue secondary "audio/final/Beast_ClawsRipping_3.flac"
    hide bg onlayer farback
    hide den onlayer back
    show bg den fight1 onlayer back at Position(ypos=1125)
    show den fight panels onlayer front at Position(ypos=1125)
    with dissolve
    n "Not a word is spoken between you and the Princess as you exchange blows in the dark. The glint of bloody claws and fangs. The flash of wet steel. In the pit, all of your senses are heightened, each injury stinging like a chorus of insects, each small shift in your favor a major victory that swells your confidence.\n" id den_pristine_fight_5aa9cd6a
    #voice "audio/_pristine/voice/den/hero/1.flac"
    #hero "Yes! We're doing it! This isn't so hard after all.\n"
    voice "audio/_pristine/voice/den/narrator/5.flac"
    play audio "audio/_pristine/sfx/Fury body exploading_2.flac"
    play secondary "audio/_pristine/sfx/Den Creatures Eating_10.flac"
    hide bg onlayer farback
    hide den onlayer front
    show bg den battle losing onlayer farback at Position(ypos=1125)
    show panel1 den battle losing onlayer back at shakeshort, Position(ypos=1125)
    with Dissolve(0.5)
    n "And yet, for all the wounds you've managed to inflict upon her, you remain at a stalemate. And then you start to lose ground. While your body slows, hers quickens, her wounds mending as she licks the blood of her prey from her dripping maw.\n"
    play audio "audio/final/Beast_LionRipping_1.flac"
    voice "audio/_pristine/voice/den/hero/2.flac"
    show panel2 den battle losing onlayer front at Position(ypos=1125)
    with Dissolve(0.5)
    hero "So she really can 'devour our strength.' Can... we do something like that? All these wounds are starting to add up.\n"
    voice "audio/_pristine/voice/den/stubborn/3.flac"
    stubborn "Nah, screw that. We're not stooping to her level. We'll just have to give this our all, end it in one final hit.\n"
    voice "audio/_pristine/voice/den/hunted/4.flac"
    hunted "We die if we do that. We have to make ourselves like her. We have to embrace instinct.\n"
    voice "audio/_pristine/voice/den/narrator/6.flac"
    play audio "audio/final/BEAST_LionSniff_1.flac"
    hide bg onlayer farback
    hide panel1 onlayer back
    hide panel2 onlayer front
    show bg den battle grin open onlayer farback at Position(ypos=1125)
    show den battle grin open onlayer back at Position(ypos=1125)
    with Dissolve(0.5)
    n "She shifts towards you, her bloody grin shining in the dark. And then you see it: your opening.\n"
    voice "audio/_pristine/voice/den/stubborn/4.flac"
    stubborn "Take it! Put her down like the mindless beast she is!\n"
    #voice "audio/_pristine/voice/den/hunted/5.flac"
    #hunted "We're stronger than we were last time. She knows it. We can turn the hunt on her.\n"
    $ gallery_den.unlock_item(16)
    $ renpy.save_persistent()
    menu:
        extend ""

        "{i}• [[Take the opening and strike at her heart.]{/i}":
            $ default_mouse = "blood"
            play secondary "audio/final/Razor_ImpaleSwordBody_6.flac"
            voice "audio/_pristine/voice/den/narrator/7.flac"
            hide bg onlayer farback
            hide den onlayer back
            show bg den hero charge onlayer farback at Position(ypos=1125)
            show den hero charge onlayer back at Position(ypos=1160)
            with Dissolve(1.0)
            n "You hurl yourself towards the Princess, your movement too quick, too bold for her to intercept. You bury your blade deep in her chest.\n"

            # LOUDER
            voice "audio/_pristine/voice/den/stubborn/5a.flac"
            stubborn "Yes, yes! We're going out in a blaze of glory!\n"
            voice "audio/_pristine/voice/den/hunted/6.flac"
            hunted "Nature doesn't have glory. This is just death.\n"
            voice "audio/_pristine/voice/den/narrator/8.flac"
            play audio "audio/final/den_roar_final.flac"
            play secondary "audio/final/Beast_ClawsRipping_2.flac"
            queue secondary "audio/final/Beast_ClawsRipping_1.flac"
            hide bg onlayer farback
            hide den onlayer back
            show bg den hero fight onlayer farback at Position(ypos=1125)
            show den hero fight onlayer back at Position(ypos=1125)
            with Dissolve(1.0)
            n "She howls in pain, retaliating with claws and teeth, desperately tearing, trying to devour you to make herself whole once again. Chunks of your flesh are torn away, feathers and blood and bits of gore splattering to the ground, but your work is already done."
            voice "audio/_pristine/voice/den/narrator/9.flac"
            play audio "audio/_pristine/sfx/Den Wounds regenerating_3.flac"
            play secondary "audio/_pristine/sfx/Den Creatures Eating_11.flac"
            hide bg onlayer farback
            hide den onlayer back
            show bg den hero fuse onlayer farback at Position(ypos=1125)
            show den hero fuse onlayer back at Position(ypos=1125)
            with Dissolve(1.0)
            n "No sating of her ravenous hunger will be enough to mend her now. Though her flesh begins to seal itself around you, she cannot remove your blade from her heart.\n"
            stop music fadeout 20.0
            stop sound fadeout 20.0
            stop tertiary fadeout 20.0
            play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 20.0
            voice "audio/_pristine/voice/den/narrator/10.flac"
            play audio "audio/_pristine/sfx/double_collapse.flac"
            play secondary "audio/_pristine/sfx/Cage_bone break_5.flac"
            hide bg onlayer farback
            hide den onlayer back
            show den hero collapse onlayer back at Position(ypos=1125)
            with Dissolve(1.0)
            n "You and the Princess collapse to the floor together, your bodies fused, entwined in a bloody mass of limbs and teeth.\n"
            voice "audio/_pristine/voice/den/stubborn/6.flac"
            stubborn "I wouldn't have it any other way.\n"
            voice "audio/_pristine/voice/den/narrator/11a.flac"
            #play secondary "audio/final/Fury_Degloving_1.flac"
            show den hero collapse shame onlayer back
            with dissolve
            n "As the two of you fade, a new emotion creeps into the Princess' eyes. Something akin to shame. 'What have we done?' they ask.\n"
            voice "audio/_pristine/voice/den/hero/3.flac"
            hero "I guess that's it. At least we saved the world... right?\n"
            voice "audio/_pristine/voice/den/hero/4.flac"
            hero "... Right?\n"
            voice "audio/_pristine/voice/den/hunted/7.flac"
            hunted "He's gone. Everything is gone. Except her, and us.\n"
            voice "audio/_pristine/voice/den/stubborn/7.flac"
            stubborn "It doesn't matter. We won.\n"
            $ gallery_den.unlock_item(4)
            $ gallery_den.unlock_item(5)
            $ renpy.save_persistent()
            show den hero collapse cold onlayer back
            with dissolve
            truth "The Princess' eyes speak again. 'I'm cold. I don't want to be cold.'\n"
            play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
            hide den onlayer back
            show quiet creep3 onlayer front
            show hands den hero 1 onlayer front at Position(ypos=1125)
            with Dissolve(1.0)
            $ renpy.pause(0.5)
            show hands den hero 2 onlayer front at Position(ypos=1125)
            with Dissolve(1.0)
            $ renpy.pause(0.5)
            show hands den hero 3 onlayer front at Position(ypos=1125)
            with Dissolve(0.5)
            $ renpy.pause(0.25)
            show hands den hero 4 onlayer front at Position(ypos=1125)
            with Dissolve(0.25)
            $ renpy.pause(0.125)
            show hands den hero 5 onlayer front at Position(ypos=1125)
            with Dissolve(0.25)
            $ renpy.pause(0.125)
            show hands den hero 6 onlayer front at Position(ypos=1125)
            with Dissolve(0.25)
            $ renpy.pause(0.125)
            hide hands onlayer front
            with Dissolve(0.25)
            $ blade_held = False
            $ default_mouse = "default"
            hide bg onlayer back
            hide bg onlayer front
            hide player onlayer front
            hide player onlayer back
            hide fore onlayer front
            hide mid onlayer front
            hide fore onlayer inyourface
            hide farback onlayer farback
            hide bg onlayer back
            hide bg onlayer farback
            hide mid onlayer back
            hide stars onlayer farback
            hide bg onlayer back
            hide quiet onlayer back
            hide quiet onlayer front
            show farback quiet onlayer farback at Position(ypos=1125)
            with Dissolve(4.0)
            show mirror quiet distant onlayer back at Position(ypos=1125)
            if loops_finished != 0:
                truth "But you don't get the opportunity to respond, nor will you ever. It's time to leave. Memory returns.\n"
            else:
                truth "But you don't get the opportunity to respond. Something has taken her away, and it's left something else in her place.\n"
            $ achievement.grant("ACH_DEN_STRIKE")
            $ beast_2_end = "slay"
            $ princess_deny += 1
            $ princess_satisfy += 1
            jump mirror_start
            # END


        "{i}• [[Embrace instinct.]{/i}":
            $ blade_held = False
            $ default_mouse = "default"
            play audio "audio/one_shot/knife_bounce_several.flac"
            voice "audio/_pristine/voice/den/narrator/12.flac"
            play secondary "audio/one_shot/footstep_run_dirt_short.flac"
            queue secondary "audio/final/Beast_ClawsRipping_1.flac"
            $ quick_menu = False
            hide bg onlayer farback
            hide bg onlayer back
            hide den onlayer back
            scene bg black
            with fade
            show bg den instinct charge onlayer farback at Position(ypos=1125)
            show den instinct charge onlayer back at Position(ypos=1125)
            with fade
            if persistent.quick_menu:
                $ quick_menu = True
            n "You hurl yourself towards the Princess' body, carving into her not with steel, but instead with tooth and claw. You are a blur of bloodied things that tear and rend.\n"
            voice "audio/_pristine/voice/den/hunted/8.flac"
            hunted "Yes... yes! We are not prey. We are more!\n"
            voice "audio/_pristine/voice/den/narrator/13.flac"
            play sound "audio/_pristine/sfx/den_howl.flac"
            play audio "audio/_pristine/sfx/Fury Body Horror_10.flac"
            hide bg onlayer farback
            hide den onlayer back
            show bg den instinct eat 1 onlayer farback at Position(ypos=1125)
            show den instinct eat 1 onlayer back at Position(ypos=1125)
            show player den instinct 1 onlayer inyourface at Position(ypos=1125)
            with Dissolve(1.0)
            n "The Princess howls in fear and outrage as you peel away a chunk of her flesh. But, as the bloody meat slides down your throat, you feel... invigorated. Your wounds burn less. You feel faster, more responsive.\n"
            voice "audio/_pristine/voice/den/hunted/9.flac"
            hunted "Again. The more we take of her, the less she will be able to take of us.\n"
            voice "audio/_pristine/voice/den/narrator/14.flac"

            # CUT FIRST SCREAM

            play audio "audio/_pristine/sfx/den_eat_2b.flac"
            hide bg onlayer farback
            hide player onlayer inyourface
            hide den onlayer back
            show bg den instinct eat 2 onlayer farback at Position(ypos=1125)
            show panel1 den instinct eat 2 onlayer back at Position(ypos=1125)
            show panel2 den instinct eat 2 delayed onlayer front at Position(ypos=1125)
            with Dissolve(0.5)
            n "There is no time to rest if you're to do this right. She tries to bat you away with her massive paw, but as it smashes into your ribs, you clamp your teeth around the limb. You give her no time to react before snapping it from its joint.\n"
            play audio "audio/_pristine/sfx/Den Creatures Eating_17.flac"
            voice "audio/_pristine/voice/den/narrator/15.flac"
            hide bg onlayer farback
            hide panel1 onlayer back
            hide panel2 onlayer front
            show den instinct eat 3 onlayer back at Position(ypos=1125)
            #show player den instinct 1 onlayer inyourface at Position(ypos=1125)
            with Dissolve(0.75)
            n "The Princess pulls back in pained shock as you crunch through bone, devouring the arm that was part of her. It's part of you now. Your wounds heal.\n"
            voice "audio/_pristine/voice/den/hero/5.flac"
            hero "That's disgusting! I don't want to do that!\n"
            voice "audio/_pristine/voice/den/stubborn/8.flac"
            stubborn "You were the one who asked if we could do this, and if it means we win... well. We have to win. Victory demands we do whatever it takes to claim it.\n"
            voice "audio/_pristine/voice/den/hero/6.flac"
            hero "I didn't think it would be so... dehumanizing.\n"
            voice "audio/_pristine/voice/den/hunted/10.flac"
            hunted "But we feel bigger than her now. Don't we?\n"
            voice "audio/_pristine/voice/den/narrator/16.flac"
            # CUT FIRST YELL
            play audio "audio/_pristine/sfx/den_eat_4a.flac"
            hide den onlayer back
            hide player onlayer inyourface
            show bg den instinct eat 2 onlayer farback at Position(ypos=1125)
            show panel1 den instinct eat 4 onlayer back at Position(ypos=1125)
            show panel2 den instinct eat 4 delayed onlayer front at Position(ypos=1125)
            with Dissolve(0.75)
            n "The feeling doesn't linger. As you choke down the last of her severed arm, she lunges, taking advantage of the distraction. In a frenzied flash of blood and feathers, she rips into your side, swallowing another piece of you.\n"
            $ gallery_den.unlock_item(17)
            $ renpy.save_persistent()
            voice "audio/_pristine/voice/den/narrator/17.flac"
            play secondary "audio/final/Fury_Degloving_1.flac"
            hide bg onlayer farback
            hide panel1 onlayer back
            hide panel2 onlayer front
            show bg den instinct eat 5 onlayer farback at Position(ypos=1125)
            show den instinct eat 5 onlayer back at Position(ypos=1125)
            with Dissolve(0.75)
            n "Weakness returns. Her arm starts to mend itself, fresh claws sprouting from developing flesh.\n"
            voice "audio/_pristine/voice/den/hunted/11.flac"
            hunted "We can't be small again! We have to take more. We have to take it now!\n"
            # tony made abby sad times
            play audio "audio/_pristine/sfx/den_eat_finale_1.flac"
            voice "audio/_pristine/voice/den/narrator/18.flac"
            hide bg onlayer farback
            hide den onlayer back
            show bg den instinct eat finale 2 onlayer farback at Position(ypos=1125)
            show panel1 den instinct eat finale onlayer back at Position(ypos=1125)
            show panel2 den instinct eat finale delayed onlayer front at Position(ypos=1125)
            show panel3 den instinct eat finale delayed onlayer inyourface at Position(ypos=1125)
            with Dissolve(0.5)
            n "You descend upon her again, jaws gnashing, desperate to regain your power. You both lose yourself in the rhythm of the feast. You devouring her and she devouring you, mending and bleeding and consuming in an endless cycle, on and on and on.\n"
            $ gallery_den.unlock_item(6)
            $ renpy.save_persistent()
            voice "audio/_pristine/voice/den/stubborn/9.flac"
            play audio "audio/_pristine/sfx/den_swing.flac"
            hide panel1 onlayer back
            hide panel2 onlayer front
            hide panel3 onlayer inyourface
            show den instinct eat finale 4 onlayer back at Position(ypos=1125)
            show player den instinct eat finale 4 onlayer front at Position(ypos=1125)
            with Dissolve(0.5)
            stubborn "Come on, just one more bite, then we'll have her right where we want her!\n"
            voice "audio/_pristine/voice/den/hero/7.flac"
            play secondary "audio/_pristine/sfx/cage_pop.flac"
            play audio "audio/_pristine/sfx/Fury Body Horror_5.flac"
            hide den onlayer back
            hide player onlayer front
            show den instinct eat finale 5 onlayer back at Position(ypos=1125)
            show player den instinct eat finale 5 onlayer front at Position(ypos=1125)
            with Dissolve(0.5)
            hero "Am I really the only one who's not on board with this? I'm gonna be sick.\n"
            voice "audio/_pristine/voice/den/narrator/19.flac"
            play audio "audio/_pristine/sfx/Dragon Bubbling Flesh_5.flac"
            hide den onlayer back
            hide player onlayer front
            show den instinct eat finale 6 onlayer back at Position(ypos=1125)
            with Dissolve(1.0)
            n "The more you consume, the more the lines that differentiate you and her begin to blur, the flesh of your bodies twisting into warped reflections of what you swallow. You have to snap out of this. You can't destroy her if you lose sight of yourself.\n" id den_pristine_fight_1b852753
            voice "audio/_pristine/voice/den/hunted/12.flac"
            hunted "We are the predator now. There is nothing to do but embrace our true nature.\n"
            stop music fadeout 20.0
            stop sound fadeout 20.0
            stop tertiary fadeout 20.0
            play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 20.0
            voice "audio/_pristine/voice/den/narrator/20.flac"
            play audio "audio/_pristine/sfx/Fury Body Horror_16.flac"
            hide den onlayer back
            show quiet creep1 onlayer farback at Position(ypos=1125)
            show den instinct eat finale 2 onlayer back at Position(ypos=1125)
            with Dissolve(1.0)
            n "{i}Sigh{/i}. But words fade into hollow vibrations as you and she continue to tear at each other in the darkness. There are no beginnings, there are no endings, there are no moments of calm. There is only savage violence.\n"
            voice "audio/_pristine/voice/den/hero/8.flac"
            hero "Did you say no endings?\n"
            show quiet creep2 onlayer farback
            with Dissolve(0.5)
            truth "But He doesn't respond. He's gone.\n"
            voice "audio/_pristine/voice/den/stubborn/10a.flac"
            stubborn "But... how are we supposed to know if we won?\n"
            voice "audio/_pristine/voice/den/hunted/13.flac"
            show quiet creep2 onlayer farback
            #show den instinct cold onlayer back at Position(ypos=1125)
            #with Dissolve(0.5)
            hunted "We have won. We'll never die so long as we keep eating. We can be forever.\n"
            $ gallery_den.unlock_item(7)
            $ renpy.save_persistent()
            # here is where something tears you apart
            play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
            play sound "audio/_pristine/sfx/Fury Body Horror_29.flac"
            hide den onlayer back
            show hands den instinct 1 onlayer back at Position(ypos=1125)
            show player hands den instinct 2 onlayer front at Position(ypos=1125)
            with Dissolve(1.5)
            truth "But you and she are separated—your flesh ripped from where it joins together—before forever can come to pass. You lock eyes. You see a new emotion there. Shame. 'What have we done?' they ask.\n"
            play audio "audio/final/assorted_Handsgrabbing_LIGHT_2.flac"
            show hands den instinct 2 onlayer back
            with Dissolve(0.75)
            $ renpy.pause(0.75)
            show hands den instinct 3 onlayer back
            show player hands den instinct 3 onlayer front
            with Dissolve(0.5)
            $ renpy.pause(0.5)
            show hands den instinct 4 onlayer back
            show player hands den instinct 4 onlayer front
            with Dissolve(0.35)
            $ renpy.pause(0.35)
            show hands den instinct 5 onlayer back
            show player hands den instinct 5 onlayer front
            with Dissolve(0.25)
            $ renpy.pause(0.25)
            hide player onlayer front
            show hands den instinct 6 onlayer back
            with Dissolve(0.25)
            $ renpy.pause(0.25)
            hide hands onlayer back
            with Dissolve(0.25)
            $ renpy.pause(0.25)
            $ blade_held = False
            $ default_mouse = "default"
            hide bg onlayer back
            hide bg onlayer front
            hide player onlayer front
            hide player onlayer back
            hide fore onlayer front
            hide mid onlayer front
            hide fore onlayer inyourface
            hide farback onlayer farback
            hide bg onlayer back
            hide bg onlayer farback
            hide mid onlayer back
            hide stars onlayer farback
            hide bg onlayer back
            hide quiet onlayer back
            hide quiet onlayer front
            show farback quiet onlayer farback at Position(ypos=1125)
            with Dissolve(4.0)
            show mirror quiet distant onlayer back at Position(ypos=1125)
            if loops_finished != 0:
                truth "You don't get the opportunity to respond, nor will you ever. It's time to leave. Memory returns.\n"
            else:
                truth "You don't get the opportunity to respond. Something has taken her away, and it's left something else in her place.\n"
            $ achievement.grant("ACH_DEN_EAT")
            $ current_princess = "den"
            $ beast_2_end = "consume"
            $ princess_kept += 1
            $ princess_deny += 1
            jump mirror_start
            # END

label den_pristine_free:

    voice "audio/_pristine/voice/den/skeptic/1.flac"
    skeptic "Now let's think for a second. Let's reevaluate. Should we help her?\n"
    voice "audio/_pristine/voice/den/hero/9.flac"
    hero "Well, I do feel bad looking at her.\n"
    voice "audio/_pristine/voice/den/skeptic/2.flac"
    skeptic "There's no way to get close without being in reach of those claws. We've come this far, but can we trust a creature that, until a few short moments ago, fully intended to eat us?\n"
    voice "audio/_pristine/voice/den/narrator/24.flac"
    n "What an excellent question with an equally excellent answer: NO! You should not help her! She's clearly just waiting for you to drop your guard, and beyond that, you'd do well to remember that she poses a threat to reality itself.\n" id den_pristine_free_8e1ce55b
    if blade_held:
        voice "audio/_pristine/voice/den/narrator/25.flac"
        show den free resigned onlayer back
        with dissolve
        n "{i}Sigh{/i}. You already have a weapon, and she's as vulnerable as she's ever going to be. How about you use it?\n"
    else:
        voice "audio/_pristine/voice/den/narrator/26.flac"
        show den free resigned onlayer back
        with dissolve
        n "She is stuck, and you abandoned a perfectly usable weapon right behind you. How about you turn around, get the blade, and end this once and for all?\n"

    #voice "audio/_pristine/voice/den/skeptic/3.flac"
    #skeptic "What threat can she pose to the world while she's stuck like this?\n"
    #voice "audio/_pristine/voice/den/narrator/27.flac"
    #n "The same threat she posed before you got here.\n"
    #voice "audio/_pristine/voice/den/skeptic/4.flac"
    #skeptic "So none at all. We can wash our hands of this right here, right now. Let's. Just. Leave.\n"
    #voice "audio/_pristine/voice/den/narrator/28.flac"
    #n "She'll get out eventually, and you'll have missed your best chance at ending her. All of this would have been for nothing!\n"
    #voice "audio/_pristine/voice/den/hunted/14.flac"
    #hunted "And what if she doesn't? This is a bad, cruel place to be, stuck in a hole forever. Wasting until there's nothing left to waste.\n"
    #voice "audio/_pristine/voice/den/hero/10.flac"
    #hero "He's right. We can't leave her like this, it's too sad.\n"
    #voice "audio/_pristine/voice/den/narrator/29.flac"
    #n "Enough. Only one of you gets to make a choice, and I hope for all our sakes that he knows what choice to make. This isn't hard. This isn't a trick question. The life of this miserable creature for the salvation of the entire world. Choose.\n"


label den_pristine_free_choice:
    default den_late_blade_dropped = False
    menu:
        extend ""

        "{i}• [[Drop the blade and approach her.]{/i}" if blade_held:
            $ blade_held = False
            $ den_late_blade_dropped = True
            $ default_mouse = "default"
            play audio "audio/one_shot/knife_bounce_several.flac"
            voice "audio/_pristine/voice/den/narrator/30.flac"
            show den free surprise onlayer back
            with dissolve
            n "The Princess' eyes go wide as the blade tumbles from your hand. You're going to get yourself killed.\n"
            voice "audio/_pristine/voice/den/skeptic/5.flac"
            skeptic "What are you doing? We could all just turn around and be done. What's your game?\n"
            voice "audio/_pristine/voice/den/narrator/31.flac"
            n "{i}Sigh{/i}. You and I both know there's no game. He's made a bad choice.\n"
            jump den_approach_join

        "{i}• [[Approach her, blade held behind your back.]{/i}" if blade_held:
            jump den_approach_join

        "{i}• [[Approach her.]{/i}" if blade_held == False:
            voice "audio/_pristine/voice/den/skeptic/5.flac"
            skeptic "What are you doing? We could all just turn around and be done. What's your game?\n"
            voice "audio/_pristine/voice/den/narrator/31.flac"
            n "{i}Sigh{/i}. You and I both know there's no game. He's made a bad choice.\n"
            label den_approach_join:
                voice "audio/_pristine/voice/den/narrator/32.flac"
                play audio "audio/one_shot/footstep_mines.flac"
                hide bg onlayer back
                hide den onlayer back
                show den approach ready onlayer back at Position(ypos=1125)
                with Dissolve(0.5)
                n "As you draw near, she readies her claws, raising them to strike.\n"
                voice "audio/_pristine/voice/den/hunted/15.flac"
                play audio "audio/final/BEAST_LionSniff_1.flac"
                hunted "Don't. Flinch. Show her our resolve.\n"
                if blade_held:
                    voice "audio/_pristine/voice/den/narrator/33.flac"
                    n "If you're going to attack, might I suggest you do so quickly?\n"
                menu:
                    extend ""

                    "{i}• [[Strike her heart.]{/i}" if blade_held:
                        voice "audio/_pristine/voice/den/hunted/16.flac"
                        hunted "Violence is still a mercy here. It's still help.\n"
                        voice "audio/_pristine/voice/den/hero/11.flac"
                        hero "Yeah. Maybe this is what's best for everyone...\n"
                        voice "audio/_pristine/voice/den/skeptic/6.flac"
                        skeptic "I still think leaving would have been best, but... we haven't seen what happens after she dies. It could give us some answers.\n"
                        $ default_mouse = "blood"
                        voice "audio/_pristine/voice/den/narrator/34.flac"
                        play secondary "audio/final/Razor_ImpaleSwordBody_6.flac"
                        show den approach slay charge onlayer back
                        with Dissolve(0.5)
                        n "You rush forward, your confidence carrying you with enough speed to avoid her desperate strike. Your blade sinks deep into her chest.\n"
                        voice "audio/_pristine/voice/den/hero/12.flac"
                        hero "So we actually did it. Why does it feel so... bad?\n"
                        voice "audio/_pristine/voice/den/hunted/17.flac"
                        hunted "Killing the weak always does.\n"
                        voice "audio/_pristine/voice/den/skeptic/7.flac"
                        skeptic "I don't think she's dead just yet.\n"
                        voice "audio/_pristine/voice/den/narrator/35.flac"
                        play audio "audio/_pristine/sfx/den_roar_shake.flac"
                        show den approach slay counter onlayer back at shakeshort
                        with dissolve
                        n "No. She isn't. As you dig towards her heart, she howls with an earth shattering shriek, and then... {i}Sigh{/i}.\n" id den_approach_join_5a04980b
                        stop music
                        voice "audio/_pristine/voice/den/hero/13.flac"
                        hero "We're at least taking her with us, right?\n"
                        voice "audio/_pristine/voice/den/narrator/36.flac"
                        play audio "audio/final/Beast_ClawsRipping_3.flac"
                        show fore den approach slay counter onlayer front at Position(ypos=1125)
                        with dissolve
                        n "Yes. But not without paying a grave price. She lashes out, tearing you open.\n" id den_approach_join_8c6adcb7
                        stop music fadeout 20.0
                        stop sound fadeout 20.0
                        stop tertiary fadeout 20.0
                        play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 20.0
                        voice "audio/_pristine/voice/den/skeptic/8.flac"
                        play audio "audio/one_shot/collapse.flac"
                        hide den onlayer back
                        hide fore onlayer front
                        show bg hands den approach start onlayer back at Position(ypos=1125)
                        show quiet creep1 onlayer back at Position(ypos=1125)
                        show hands den approach start onlayer back at Position(ypos=1125)
                        with Dissolve(1.0)
                        skeptic "Another death, and we've still learned nothing. I knew leaving was the right answer. You should have listened to me.\n"
                        $ gallery_den.unlock_item(8)
                        $ renpy.save_persistent()
                        voice "audio/_pristine/voice/den/narrator/37.flac"
                        show quiet creep2 onlayer back at Position(ypos=1125)
                        show hands den approach slay 1 onlayer back
                        with Dissolve(0.75)
                        n "It doesn't matter now. In her final moments, she made sure that there would be no way out for either of you. It's over.\n"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show hands den approach slay 2 onlayer back
                        with Dissolve(0.75)
                        $ renpy.pause(0.75)
                        show hands den approach slay 3 onlayer back
                        with Dissolve(0.5)
                        $ renpy.pause(0.5)
                        show hands den approach slay 4 onlayer back
                        with Dissolve(0.35)
                        $ renpy.pause(0.35)
                        show hands den approach slay 5 onlayer back
                        with Dissolve(0.25)
                        $ renpy.pause(0.25)
                        hide player onlayer front
                        show hands den approach slay 6 onlayer back
                        with Dissolve(0.25)
                        $ renpy.pause(0.25)
                        hide hands onlayer back
                        with Dissolve(0.25)
                        $ renpy.pause(0.25)
                        $ blade_held = False
                        $ default_mouse = "default"
                        hide bg onlayer back
                        hide bg onlayer front
                        hide player onlayer front
                        hide player onlayer back
                        hide fore onlayer front
                        hide mid onlayer front
                        hide fore onlayer inyourface
                        hide farback onlayer farback
                        hide bg onlayer back
                        hide bg onlayer farback
                        hide mid onlayer back
                        hide stars onlayer farback
                        hide bg onlayer back
                        hide quiet onlayer back
                        hide quiet onlayer front
                        show farback quiet onlayer farback at Position(ypos=1125)
                        with Dissolve(4.0)
                        show mirror quiet distant onlayer back at Position(ypos=1125)
                        if loops_finished != 0:
                            truth "But this is no true end, and you do not get the chance to see her die. Nor will you ever. It's time to leave. Memory returns.\n"
                        else:
                            truth "But this is no true end, and you do not get the chance to see her die. Something has taken her away, and it's left something else in her place.\n"
                        $ achievement.grant("ACH_DEN_COUP")
                        $ beast_2_end = "slay"
                        $ princess_kept += 1
                        $ princess_satisfy += 1
                        jump mirror_start


                    "{i}• [[Offer her your hand.]{/i}":
                        if blade_held:
                            stop music
                            play secondary "audio/final/_nightmare_heart_loop.ogg" loop
                            voice "audio/_pristine/voice/den/narrator/38.flac"
                            show den approach hand offer friend onlayer back
                            show player den approach hand offer friend onlayer front at Position(ypos=1125)
                            with Dissolve(0.5)
                            n "You reach forward, offering the Princess your hand. But she doesn't take it.\n"
                            voice "audio/_pristine/voice/den/hunted/18.flac"
                            hunted "She remembers the glint of our steel claw.\n"
                            voice "audio/_pristine/voice/den/narrator/39.flac"
                            play audio "audio/final/Beast_ClawsRipping_3.flac"
                            hide den onlayer back
                            hide player onlayer front
                            show den approach slay counter onlayer back at Position(ypos=1125)
                            show fore den approach slay counter onlayer front at Position(ypos=1125)
                            with Dissolve(0.5)
                            n "She certainly does. In a surprising burst of speed, she swipes at you, her claws meeting your throat.\n"
                            voice "audio/_pristine/voice/den/narrator/40.flac"
                            n "It's too late. You had your chance, and she had hers.\n"
                            jump den_flinch_end_join
                        else:
                            play audio "audio/final/BEAST_LionSniff_2.flac"
                            voice "audio/_pristine/voice/den/narrator/41.flac"
                            show den approach hand offer friend onlayer back
                            show player den approach hand offer friend onlayer front at Position(ypos=1125)
                            with Dissolve(0.5)
                            n "You reach forward, offering the Princess your hand. How ridiculous. She was about to kill you, do you really think getting stuck in a tunnel for less than a minute has fundamentally changed her?\n"
                            voice "audio/_pristine/voice/den/hunted/19.flac"
                            hunted "Yes. She's a victim of her own nature. Just like we are.\n"
                            voice "audio/_pristine/voice/den/hero/14.flac"
                            hero "If all she wanted was to kill us, she'd have kept trying. But she's hestitating, isn't she?\n"
                            stop music
                            #play secondary "audio/final/_nightmare_heart_loop.ogg" loop
                            voice "audio/_pristine/voice/den/narrator/42a.flac"
                            play music "audio/_pristine/music/den/Hand in Claw Heart Intro.flac"
                            queue music "audio/_pristine/music/den/Hand in Claw Loop.flac" loop
                            play audio "audio/_pristine/sfx/den_hand_grab_start.flac"
                            hide den onlayer back
                            hide player onlayer front
                            show bg den flinch chomp onlayer farback at Position(ypos=1125)
                            show panel1 den approach friend soft onlayer back at Position(ypos=1125)
                            show panel2 den approach friend soft onlayer front at Position(ypos=1125)
                            show panel3 den approach friend soft delayed onlayer inyourface at Position(ypos=1125)
                            with Dissolve(0.5)
                            n "{i}Sigh{/i}... yes. She is. Her eyes shift from faux ferocity, to confusion, to a gentle sadness. She lowers her claw... and places it in your hand. Eugh.\n"
                            voice "audio/_pristine/voice/den/hero/15.flac"
                            hide panel1 onlayer back
                            hide panel2 onlayer front
                            hide panel3 onlayer inyourface
                            hide bg onlayer farback
                            show den friend tug onlayer back at Position(ypos=1125)
                            with Dissolve(1.0)
                            hero "Do you think we can pull her out of there?\n"
                            #hunted "We have to try. We are the only creatures here. We only have each other.\n"
                            voice "audio/_pristine/voice/den/hunted/20.flac"
                            hunted "We have to try. It's a bad death, being stuck in place.\n"
                            voice "audio/_pristine/voice/den/skeptic/9.flac"
                            skeptic "And what if it doesn't work? What if we can't trust her?\n"
                            voice "audio/_pristine/voice/den/hero/16.flac"
                            hero "We have to trust someone else eventually. It's either Him or her, and I know you don't trust Him.\n"
                            voice "audio/_pristine/voice/den/skeptic/10.flac"
                            skeptic "I don't even trust the rest of you. But that doesn't mean we have to go around pulling bloodthirsty monsters out of perfectly good traps.\n"
                            voice "audio/_pristine/voice/den/hero/17.flac"
                            hero "But we haven't seen what happens if we help her. Doesn't that mean it's worth exploring?\n"
                            voice "audio/_pristine/voice/den/skeptic/11a.flac"
                            skeptic "... I can't argue with that. All right... let's see what happens. Maybe we'll finally get some answers.\n"

                            menu:
                                extend ""

                                "{i}• [[Pull her free.]{/i}":
                                    voice "audio/_pristine/voice/den/narrator/43.flac"
                                    play audio "audio/one_shot/knife_tighten.flac"
                                    show den friend tug onlayer back at cage_sway
                                    with dissolve
                                    n "You tug, but the Princess remains stuck. What a shame that the bones of her massive form are too large to fit through the narrow tunnel.\n"
                                    #voice "audio/_pristine/voice/den/skeptic/12.flac"
                                    #skeptic "No, no. Now that doesn't make sense. She had to have gotten down here somehow, right? She can't be too big for the tunnel.\n"
                                    #voice "audio/_pristine/voice/den/narrator/44.flac"
                                    #n "Maybe she just grew while she was down there.\n"
                                    #voice "audio/_pristine/voice/den/hunted/21.flac"
                                    #hunted "But she's so hungry. She can't have grown if she's so hungry.\n"
                                    voice "audio/_pristine/voice/den/hero/18.flac"
                                    hero "Keep pulling. All He has are empty words. He can't undermine us if we don't listen!\n"
                                    voice "audio/_pristine/voice/den/narrator/45.flac"
                                    play audio "audio/_pristine/sfx/Den Tunel collapse_1.flac"
                                    hide den onlayer back
                                    show den friend tug free onlayer back at Position(ypos=1125)
                                    with dissolve
                                    n "You are all infuriating to work with. But fine, you continue to pull on the Princess' arm, and she... starts to budge. She pushes with her back legs, clawing at the earth, a burst of strength aiding your efforts. The dirt and stone start to crumble around her.\n"
                                    # LOUDER
                                    voice "audio/_pristine/voice/den/hero/19.flac"
                                    hero "That's the spirit, keep going!\n"
                                    voice "audio/_pristine/voice/den/skeptic/13.flac"
                                    skeptic "Yes, quickly, before the whole tunnel comes down on top of us!\n"
                                    voice "audio/_pristine/voice/den/narrator/46.flac"
                                    n "Yes, wouldn't that be an interesting development. What if the very nature of this tunnel was such that you were incapable of leaving safely with the Princess? How devious.\n"
                                    voice "audio/_pristine/voice/den/hero/20.flac"
                                    hero "Does it... collapse?\n"
                                    voice "audio/_pristine/voice/den/narrator/47.flac"
                                    play audio "audio/_pristine/sfx/Den Tunel collapse_2.flac"
                                    stop music fadeout 3.0
                                    show den friend collapse 1 onlayer back
                                    with Dissolve(0.5)
                                    $ renpy.pause(0.5)
                                    hide den onlayer back
                                    scene bg black
                                    with fade
                                    voice sustain
                                    n "Yes. It does. As you pull the Princess free, the tunnel around you does exactly what you thought it might do. It falls apart.\n"
                                    voice "audio/_pristine/voice/den/hunted/22.flac"
                                    hunted "Trapped... no, we have to get out, we have to get out!\n"
                                    voice "audio/_pristine/voice/den/narrator/48.flac"
                                    play audio "audio/_pristine/sfx/Den Tunel collapse_3.flac"
                                    n "It's too late to scramble for freedom now, little voice. You didn't think 'just pulling her out of there' would be consequence-free, did you? Well, the ceiling collapses, heavy stones tumbling down on top of you and the Princess and...\n"
                                    voice "audio/_pristine/voice/den/narrator/49.flac"
                                    n "I don't believe it.\n"
                                    voice "audio/_pristine/voice/den/hero/21.flac"
                                    hero "Let me guess. Everything goes dark, and we die.\n"
                                    voice "audio/_pristine/voice/den/narrator/50.flac"
                                    play music "audio/_pristine/music/den/Hand in Claw Intro.flac"
                                    queue music "audio/_pristine/music/den/Hand in Claw Loop.flac" loop
                                    show den friend collapse dig onlayer back at Position(ypos=1125)
                                    with fade
                                    n "No. Not yet. You open your eyes to see the Princess, her body stretched over yours, her face wincing as she shields you from the heavy rocks and debris. There is space enough for you to move, at least for now.\n"
                                    $ gallery_den.unlock_item(12)
                                    $ renpy.save_persistent()
                                    voice "audio/_pristine/voice/den/skeptic/14.flac"
                                    show den friend collapse 2 onlayer back at Position(ypos=1125)
                                    with dissolve
                                    skeptic "I'll be damned. So there's more to her, after all.\n"
                                    #voice "audio/_pristine/voice/den/hero/22.flac"
                                    #hero "Yeah. Trust pays off, doesn't it?\n"
                                    voice "audio/_pristine/voice/den/hunted/23.flac"
                                    hunted "The pack is always stronger than the lone hunter. We save her, she saves us. She understands.\n"
                                    $ gallery_den.unlock_item(13)
                                    $ renpy.save_persistent()
                                    voice "audio/_pristine/voice/den/narrator/51.flac"
                                    play audio "audio/_pristine/sfx/Den Tunel collapse_3.flac"
                                    show den friend collapse dig onlayer back at shakeshort
                                    show dust den friend collapse dig onlayer front at shakeshort, Position(ypos=1125)
                                    with dissolve
                                    n "Well, you can't keep saving each other forever! Her arms are already starting to give out, and there's a whole mountain of earth on top of her just waiting to bury you both.\n"
                                    voice "audio/_pristine/voice/den/hunted/24.flac"
                                    hunted "We can always dig. Both of us.\n"
                                    voice "audio/_pristine/voice/den/skeptic/15.flac"
                                    skeptic "It beats suffocating to death down here in the dark.\n"
                                    voice "audio/_pristine/voice/den/hero/23.flac"
                                    hero "Then let's do it.\n"
                                    menu:
                                        extend ""

                                        "{i}• [[Dig through the earth together.]{/i}":
                                            $ quick_menu = False
                                            play audio "audio/_pristine/sfx/Den creatures digging rock_3.flac"
                                            voice "audio/_pristine/voice/den/narrator/52.flac"
                                            hide den onlayer back
                                            hide dust onlayer front
                                            scene bg black
                                            with fade
                                            show den friend collapse dig 2 onlayer back at Position(ypos=1125)
                                            with fade
                                            if persistent.quick_menu:
                                                $ quick_menu = True
                                            n "You and the Princess dig through the loose earth of the collapsed tunnel... together. How sweet. But it seems the harder you try to claw your way forward, the denser the path becomes. All of this effort, and for what? A chance to end the world? I hope you fail.\n"
                                            #voice "audio/_pristine/voice/den/skeptic/16.flac"
                                            #skeptic "You really don't want us to see what happens when we leave.\n"
                                            #voice "audio/_pristine/voice/den/narrator/53a.flac"
                                            #n "Of course I don't! And I've already told you why at least a half-dozen times.\n"
                                            voice "audio/_pristine/voice/den/hunted/25.flac"
                                            hunted "His words are nothing. Pay attention to what you feel and see.\n"
                                            #voice "audio/_pristine/voice/den/hero/24.flac"
                                            #hero "Yeah. Ignore him. This isn't as hard as he's making it out to be.\n"

                                    voice "audio/_pristine/voice/den/narrator/54.flac"
                                    show den friend collapse dig 2 onlayer back at shakeshort
                                    show dust den friend collapse dig 2 onlayer front at shakeshort, Position(ypos=1125)
                                    with Dissolve(0.5)
                                    n "It doesn't matter if you ignore me, because I'm just telling you what's happening, and what's happening is that you and the Princess are getting tired, and your mouths are full of dirt, and it's getting harder to breathe...\n"
                                    voice "audio/_pristine/voice/den/skeptic/17.flac"
                                    skeptic "Harder to breathe is still breathing.\n"
                                    voice "audio/_pristine/voice/den/narrator/55.flac"
                                    n "Well, either way, the two of you are miserable.\n"
                                    voice "audio/_pristine/voice/den/hero/25.flac"
                                    hero "I don't know. I feel like we're forming a bond with her. It can't be all that bad if we're bonding.\n"
                                    voice "audio/_pristine/voice/den/narrator/56.flac"
                                    n "She's not capable of 'bonding.' Need I remind you that as soon as she saw you, she tried to eat you? You are not friends, and as soon as you're out, you'll see just how seriously she values your life!\n"
                                    voice "audio/_pristine/voice/den/skeptic/18.flac"
                                    skeptic "If you were so sure we were going to fail, you wouldn't sound so desperate. You're just... hot air. There's nothing of substance to you at all, is there?\n" id den_approach_join_898d9302
                                    voice "audio/_pristine/voice/den/narrator/57.flac"
                                    n "I... have plenty of substance! I have feelings, and desires! Like my desire to save everyone in the world, I feel that very strongly.\n"
                                    voice "audio/_pristine/voice/den/hunted/26.flac"
                                    hunted "Do you smell it? Fresh air.\n"
                                    #voice "audio/_pristine/voice/den/hero/26.flac"
                                    #hero "Come on, altogether now, one last push!\n"
                                    menu:
                                        extend ""

                                        "{i}• [[Claw your way to freedom.]{/i}":
                                            voice "audio/_pristine/voice/den/narrator/58.flac"
                                            play audio "audio/_pristine/sfx/_den_collapse_flee.flac"
                                            hide dust onlayer front
                                            hide den onlayer back
                                            show farback den collapse alone onlayer farback at Position(ypos=1125)
                                            show den collapse alone onlayer front at shakeshort, Position(ypos=1125)
                                            with Dissolve(0.5)
                                            n "With one final massive heave of her body, the Princess pushes her way out of the tunnel, leaving you behind in the quickly collapsing space you once shared.\n"
                                            play audio "audio/_pristine/sfx/Den Tunel collapse_4.flac"
                                            voice "audio/_pristine/voice/den/narrator/59.flac"
                                            show den collapse alone noprincess onlayer front at shakeshort
                                            with Dissolve(0.5)
                                            n "Yours was an alliance of convenience, just as I predicted. She has left you to die buried and alone.\n"
                                            voice "audio/_pristine/voice/den/hero/27.flac"
                                            hero "You are unbelievably petty.\n"
                                            voice "audio/_pristine/voice/den/narrator/60.flac"
                                            n "Oh, my pettiness is nothing compared to yours. You were delighting in my suffering and the damnation of the entire world just moments ago–!\n"
                                            play audio "audio/_pristine/sfx/den_thump.flac"
                                            voice "audio/_pristine/voice/den/hunted/27.flac"
                                            hunted "She hasn't left. She's coming back, don't you hear her?\n"
                                            voice "audio/_pristine/voice/den/narrator/61.flac"
                                            n "No, she isn't, she's—\n"
                                            $ gallery_den.unlock_item(14)
                                            $ renpy.save_persistent()
                                            show den friend appear onlayer front
                                            with Dissolve(0.5)
                                            #I assume this is where her face appears in the gap
                                            play audio "audio/_pristine/sfx/Den Large Creature pluc player_2.flac"
                                            voice "audio/_pristine/voice/den/skeptic/19.flac"
                                            skeptic "How many times do you have to be wrong before you stop talking?\n"
                                            play audio "audio/_pristine/sfx/Den Large Creature pluc player_1.flac"
                                            voice "audio/_pristine/voice/den/narrator/62.flac"
                                            show den friend pluck onlayer front
                                            with Dissolve(0.5)
                                            n "{i}Sigh{/i}. The Princess stares down at you from the opening. Before the tunnel can finish sealing itself, she cranes her elongated neck and... gently plucks you from the earth.\n"
                                            play audio "audio/_pristine/sfx/den_thump.flac"
                                            voice "audio/_pristine/voice/den/narrator/63.flac"
                                            hide den onlayer front
                                            show farback den friend carry onlayer farback at Position(ypos=1125)
                                            show bg den friend carry onlayer back at Position(ypos=1125)
                                            show den friend carry onlayer front at Position(ypos=1125)
                                            with Dissolve(1.0)
                                            n "She carries you across the half-collapsed ruin that was a cabin, carefully setting you down by the door.\n"
                                            #voice "audio/_pristine/voice/den/hunted/28.flac"
                                            #hunted "Just one last piece of wood. Then... freedom.\n"
                                            voice "audio/_pristine/voice/den/narrator/64.flac"
                                            n "If there were to be a record, let it show that I tried. I really, really tried. But there won't be a record, will there?\n"
                                            menu:
                                                extend ""

                                                "{i}• [[Open the door and step into the wilds.]{/i}":
                                                    $ quick_menu = False


                                    $ gallery_den.unlock_item(15)
                                    $ renpy.save_persistent()
                                    voice "audio/_pristine/voice/den/narrator/65early.flac"
                                    play secondary "audio/one_shot/door_bedroom.flac"
                                    queue secondary "audio/one_shot/collapse.flac"
                                    stop music
                                    hide farback onlayer farback
                                    hide bg onlayer back
                                    hide den onlayer front
                                    with fade
                                    show farback den free collapse onlayer farback at Position(ypos=1125)
                                    show den free collapse onlayer back at Position(ypos=1125)
                                    with fade
                                    if persistent.quick_menu:
                                        $ quick_menu = True
                                    n "You open the door, the two of you stepping out into the fresh air, and collapsing together onto the dewey grass of the outside world.\n"
                                    stop music fadeout 20.0
                                    stop sound fadeout 20.0
                                    stop tertiary fadeout 20.0
                                    play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 20.0
                                    #voice "audio/_pristine/voice/den/narrator/66.flac"
                                    #n "You're both exhausted, bruised and battered from your ordeal, a minor price to pay for the grave sin you have just committed. You have damned everyone to oblivion.\n"
                                    voice "audio/_pristine/voice/den/skeptic/20.flac"
                                    show quiet creep1 onlayer farback at Position(ypos=1125)
                                    with Dissolve(0.5)
                                    skeptic "Hah. We're outside, and there's ground beneath our feet. I don't see any oblivion. Admit it, there never was an end of the world coming, was there?\n"
                                    truth "He does not reply.\n"
                                    voice "audio/_pristine/voice/den/hero/28.flac"
                                    hero "Yeah, we got him there, didn't we? I don't think I've ever seen him stunned into silence before.\n"
                                    voice "audio/_pristine/voice/den/hunted/29.flac"
                                    show quiet creep2 onlayer farback
                                    with Dissolve(0.5)
                                    hunted "Can't you feel the hole where He was? He's gone.\n" id den_approach_join_2018d7fe
                                    voice "audio/_pristine/voice/den/hero/29.flac"
                                    hero "Fancy that.\n"
                                    voice "audio/_pristine/voice/den/hunted/30.flac"
                                    show quiet creep3 onlayer farback
                                    with Dissolve(0.5)
                                    hunted "I'm not sure gone is good.\n"
                                    hide quiet onlayer farback
                                    hide den onlayer back
                                    show bg den free final onlayer back at Position(ypos=1125)
                                    show quiet creep3 onlayer back at Position(ypos=1125)
                                    show den free final onlayer back at Position(ypos=1125)
                                    with Dissolve(1.5)
                                    truth "The Princess rests her head close to you. Her eyes stare into yours amid the untextured threads of a world unraveled. 'Are we free?' They ask. 'I'm cold. I don't want to be cold.'\n" id den_approach_join_2a379208
                                    play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                                    hide den onlayer back
                                    show hands den free 1 onlayer back
                                    with Dissolve(0.75)
                                    $ renpy.pause(0.75)
                                    show hands den free 2 onlayer back
                                    with Dissolve(0.75)
                                    $ renpy.pause(0.75)
                                    show hands den free 3 onlayer back
                                    with Dissolve(0.5)
                                    $ renpy.pause(0.5)
                                    show hands den free 4 onlayer back
                                    with Dissolve(0.35)
                                    $ renpy.pause(0.35)
                                    show hands den free 5 onlayer back
                                    with Dissolve(0.25)
                                    $ renpy.pause(0.25)
                                    hide player onlayer front
                                    show hands den free 6 onlayer back
                                    with Dissolve(0.25)
                                    $ renpy.pause(0.25)
                                    hide hands onlayer back
                                    with Dissolve(0.25)
                                    $ renpy.pause(0.25)
                                    $ blade_held = False
                                    $ default_mouse = "default"
                                    hide farback onlayer farback
                                    hide bg onlayer back
                                    hide bg onlayer back
                                    hide bg onlayer front
                                    hide player onlayer front
                                    hide player onlayer back
                                    hide fore onlayer front
                                    hide mid onlayer front
                                    hide fore onlayer inyourface
                                    hide farback onlayer farback
                                    hide bg onlayer back
                                    hide bg onlayer farback
                                    hide mid onlayer back
                                    hide stars onlayer farback
                                    hide bg onlayer back
                                    hide quiet onlayer back
                                    hide quiet onlayer front
                                    hide quiet onlayer farback
                                    show farback quiet onlayer farback at Position(ypos=1125)
                                    with Dissolve(4.0)
                                    show mirror quiet distant onlayer back at Position(ypos=1125)
                                    if loops_finished != 0:
                                        truth "But you don't get the opportunity to respond, nor will you ever. It's time to leave. Memory returns.\n"
                                    else:
                                        truth "But you don't get the opportunity to respond. Something has taken her away, and it's left something else in her place.\n"
                                    $ achievement.grant("ACH_DEN_LION")
                                    $ beast_2_end = "free_succeed"
                                    $ princess_free += 1
                                    $ princess_satisfy += 1
                                    jump mirror_start
                                    # end



                    "{i}• [[Flinch.]{/i}":
                        default den_end_flinch = False
                        $ den_end_flinch = True
                        voice "audio/_pristine/voice/den/hunted/31.flac"
                        hunted "Bad! This is a bad thing to do!\n"
                        voice "audio/_pristine/voice/den/narrator/67.flac"
                        play audio "audio/final/Beast_ClawsRipping_3.flac"
                        hide den onlayer back
                        hide player onlayer front
                        show den approach slay counter onlayer back at Position(ypos=1125)
                        show fore den approach slay counter onlayer front at Position(ypos=1125)
                        with Dissolve(0.5)
                        n "Against the wise protestations of the little voice in your head, you flinch, and the Princess' claws rake across your body, tearing you open.\n"
                        if blade_held:
                            voice "audio/_pristine/voice/den/narrator/68.flac"
                            play audio "audio/one_shot/knife_bounce_several.flac"
                            $ blade_held = False
                            $ default_mouse = "default"
                            n "The blade tumbles hopelessly from your faltering grip as your blood spills onto the dirt below.\n"
                        label den_flinch_end_join:
                            $ gallery_den.unlock_item(9)
                            $ renpy.save_persistent()
                            stop music fadeout 10.0
                            voice "audio/_pristine/voice/den/narrator/69.flac"
                            play secondary "audio/one_shot/collapse.flac"
                            queue secondary "audio/_pristine/sfx/Den Large Creature pluc player_1.flac"
                            hide den onlayer back
                            hide fore onlayer front
                            show den flinch grab onlayer back at Position(ypos=1125)
                            with Dissolve(0.75)
                            n "You fall forward, and she hooks you with her paw, dragging you towards her. You start to grow cold. She prods you in an almost sorrowful confusion, hoping for some reaction. But there is no reaction for her to find. Your body is irreparably broken.\n"
                            #n "You fall forward, and she hooks you with her paw, dragging you towards her. You start to grow cold. She prods you in an almost sorrowful confusion, hoping for some reaction.\n"
                            voice "audio/_pristine/voice/den/hero/30.flac"
                            hero "I don't think she wanted to hurt us.\n"
                            voice "audio/_pristine/voice/den/skeptic/21.flac"
                            skeptic "And yet she did. Intent matters less than facts.\n"
                            #voice "audio/_pristine/voice/den/narrator/70.flac"
                            #n "Oh, I wholly agree, and that's a lesson you'd do best to carry with you to your grave.\n"
                            voice "audio/_pristine/voice/den/narrator/71.flac"
                            stop music fadeout 20.0
                            stop sound fadeout 20.0
                            stop tertiary fadeout 20.0
                            play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 20.0
                            play audio "audio/_pristine/sfx/Fury Body Horror_4.flac"
                            hide den onlayer back
                            show bg den flinch chomp onlayer back at Position(ypos=1125)
                            show den flinch chomp onlayer front at Position(ypos=1125)
                            with Dissolve(0.5)
                            n "Her sorrow doesn't last. And when it's gone, she begins to feast.\n"
                            voice "audio/_pristine/voice/den/hunted/32.flac"
                            show quiet creep3 onlayer back at Position(ypos=1125)
                            with Dissolve(1.0)
                            hunted "Prey again. It's all just a circle. And it never ends.\n"
                            play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                            hide den onlayer front
                            hide bg onlayer back
                            show hands den flinch onlayer back
                            with Dissolve(0.75)
                            $ renpy.pause(0.75)
                            show hands den flinch 2 onlayer back
                            with Dissolve(0.75)
                            $ renpy.pause(0.75)
                            show hands den flinch 3 onlayer back
                            with Dissolve(0.5)
                            $ renpy.pause(0.5)
                            show hands den flinch 4 onlayer back
                            with Dissolve(0.35)
                            $ renpy.pause(0.35)
                            show hands den flinch 5 onlayer back
                            with Dissolve(0.25)
                            $ renpy.pause(0.25)
                            hide player onlayer front
                            show hands den flinch 6 onlayer back
                            with Dissolve(0.25)
                            $ renpy.pause(0.25)
                            hide hands onlayer back
                            with Dissolve(0.25)
                            $ renpy.pause(0.25)
                            $ blade_held = False
                            $ default_mouse = "default"
                            hide bg onlayer back
                            hide bg onlayer front
                            hide player onlayer front
                            hide player onlayer back
                            hide fore onlayer front
                            hide mid onlayer front
                            hide fore onlayer inyourface
                            hide farback onlayer farback
                            hide bg onlayer back
                            hide bg onlayer farback
                            hide mid onlayer back
                            hide stars onlayer farback
                            hide bg onlayer back
                            hide quiet onlayer back
                            hide quiet onlayer front
                            hide quiet onlayer farback
                            show farback quiet onlayer farback at Position(ypos=1125)
                            with Dissolve(4.0)
                            show mirror quiet distant onlayer back at Position(ypos=1125)
                            if loops_finished != 0:
                                truth "But the circle doesn't close, nor will it ever. It's time to leave. Memory returns.\n"
                            else:
                                truth "But the circle doesn't close, nor will it ever. Something has taken her away, and it's left something else in her place.\n"
                            $ beast_2_end = "free_fail"
                            $ princess_kept += 1
                            $ princess_satisfy += 1
                            jump mirror_start
                            # END


        "{i}• [[Turn back for the blade.]{/i}" if blade_held == False:
            jump den_collapse_join

        "{i}• [[Turn around and leave. You're done here.]{/i}" if blade_held:
            label den_collapse_join:
                play secondary "audio/one_shot/footstep_mines.flac"
                queue secondary "audio/_pristine/sfx/den_roar_shake.flac"
                voice "audio/_pristine/voice/den/narrator/72.flac"
                $ quick_menu = False
                hide bg onlayer back
                hide den onlayer back
                with fade
                show farback den abandon onlayer farback at shakeshort, Position(ypos=1125)
                show bg den abandon onlayer back at shakeshort, Position(ypos=1125)
                if blade_held:
                    show player den abandon blade onlayer back at shakeshort, Position(ypos=1125)
                else:
                    show player den abandon onlayer back at shakeshort, Position(ypos=1125)
                with fade
                if persistent.quick_menu:
                    $ quick_menu = True
                n "You turn back towards the exit, leaving her behind. But the tense silence of the tunnel is suddenly interrupted by the panicked, gutteral wails of a creature in distress. She has redoubled her struggle against the confines of the earth around her, the very walls shaking as she desperately thrashes against them.\n"
                voice "audio/_pristine/voice/den/hero/31.flac"
                hero "She... is stuck here, right?\n"
                voice "audio/_pristine/voice/den/skeptic/22.flac"
                skeptic "Of course! It's too small for her to get up here.\n"
                voice "audio/_pristine/voice/den/hero/32.flac"
                hero "But is 'up here' stable?\n"
                voice "audio/_pristine/voice/den/skeptic/23.flac"
                skeptic "I... don't know. I didn't think about that when I started to plan all of this.\n"
                voice "audio/_pristine/voice/den/hunted/33.flac"
                hunted "It isn't. It's only dirt and stone, and she is very, very big. Hurry!\n"
                voice "audio/_pristine/voice/den/narrator/73.flac"
                play audio "audio/_pristine/sfx/Den Tunel collapse_1.flac"
                show bg den abandon collapsing onlayer back at shakeshort, Position(ypos=1125)
                if blade_held:
                    show player den abandon collapsing blade onlayer back at shakeshort, Position(ypos=1125)
                else:
                    show player den abandon collapsing onlayer back at shakeshort, Position(ypos=1125)
                show dust den abandon collapsing onlayer inyourface at shakeshort, Position(ypos=1125)
                with Dissolve(1.0)
                n "You do your best to scramble up towards the exit, but you barely manage to get halfway before the ground beneath you begins to crumble. And she is getting closer, her breath hot on the back of your neck.\n"
                #n "You do your best to scramble up towards the exit, but you barely manage to get halfway before the ground beneath you begins to give way. The whole tunnel is falling apart. And she is getting closer, her breath hot on the back of your neck.\n"
                voice "audio/_pristine/voice/den/skeptic/24.flac"
                skeptic "Damn it all! This whole thing is just an exercise in futility, isn't it?\n"
                voice "audio/_pristine/voice/den/hunted/34.flac"
                hunted "No words, only action! Keep running!\n"
                voice "audio/_pristine/voice/den/narrator/74a.flac"
                play audio "audio/_pristine/sfx/den_large_collapse.flac"
                stop music
                hide farback onlayer farback
                hide bg onlayer back
                hide player onlayer back
                hide dust onlayer inyourface
                scene bg black
                n "But the tunnel collapses before either you or the Princess manages to reach the exit.\n"
                voice "audio/_pristine/voice/den/hero/33.flac"
                hero "{i}Sigh{/i}. Everything goes dark and we die?\n"
                voice "audio/_pristine/voice/den/narrator/75.flac"
                n "Oh, no. You're perfectly fine. You're just buried under literal tons of earth. As is the Princess.\n"
                voice "audio/_pristine/voice/den/skeptic/25.flac"
                skeptic "Why for the love of everything did I not think about the stability of the tunnels?! I'm supposed to be smarter than this! I'm supposed to have a plan for everything.\n"
                #voice "audio/_pristine/voice/den/hunted/35.flac"
                #hunted "Plans are nothing without instinct. And a lone hunter is always vulnerable to mistakes. It was true of her, and it was true of us.\n"
                voice "audio/_pristine/voice/den/hero/34.flac"
                hero "This is all my fault. I was the one who started worrying about this place falling apart.\n"
                voice "audio/_pristine/voice/den/skeptic/26.flac"
                skeptic "And what, you think worrying made the tunnel collapse?\n"
                voice "audio/_pristine/voice/den/hero/35.flac"
                hero "I don't know, maybe!\n"
                voice "audio/_pristine/voice/den/skeptic/27.flac"
                skeptic "It was physics. You can't change things just by thinking about them, that's ridiculous.\n"
                voice "audio/_pristine/voice/den/hunted/36a.flac"
                hunted "Bickering and bickering doesn't matter, because now we're here. Stuck in a dark place. Not a place to move. Not even room to dig.\n"
                $ gallery_den.unlock_item(10)
                $ renpy.save_persistent()
                voice "audio/_pristine/voice/den/narrator/76.flac"
                play secondary "audio/_pristine/sfx/Apotheosis Oppresive AMB_2loop.flac" loop
                show den buried eye open onlayer back at Position(ypos=1125)
                show bg den buried onlayer back at Position(ypos=1125)
                with fade
                n "Something shifts in the gloom around you. An eye opens. The wet glint of it pierces the darkness, its pupil focused on you.\n"
                voice "audio/_pristine/voice/den/narrator/77.flac"
                n "The Princess. {i}Sigh{/i}. At least she's as stuck as you are. Not that it'll do much good in the end. Stuck is still alive.\n"
                voice "audio/_pristine/voice/den/hunted/37.flac"
                hunted "But it's not alive forever. I can smell the end all around us. Sweet, and empty. This is where we die. I'm going to lie down now.\n"
                voice "audio/_pristine/voice/den/narrator/78a.flac"
                show den buried eye sad onlayer back
                with dissolve
                n "The eye stares at you with resignation. A glimmer of regret. 'Are we going to be here forever? Is this my fault?'\n"
                label den_collapse_final_menu:
                    default den_collapse_stuck_explore = False
                    default den_collapse_die_explore = False
                    default den_collapse_struggle = False
                    menu:
                        extend ""

                        "{i}• (Explore) I still have the blade. Maybe I can still end this.{/i}" if blade_held and den_collapse_stuck_explore == False:
                            $ den_collapse_stuck_explore = True
                            voice "audio/_pristine/voice/den/narrator/79.flac"
                            n "I wish that were the case, but she's too far away for you to reach, and even if she weren't, your arm is pinned.\n"
                            voice "audio/_pristine/voice/den/hero/36.flac"
                            hero "Can you make it... unpinned?\n"
                            voice "audio/_pristine/voice/den/skeptic/28.flac"
                            skeptic "Of course he can't. We've been over this. You can't just change reality on a whim. That's what makes it real.\n"
                            label den_collapse_circles:
                                voice "audio/_pristine/voice/den/narrator/80.flac"
                                n "{i}Sigh{/i}. He's right. There's nothing I can do here. I'm sorry.\n"
                                voice "audio/_pristine/voice/den/hunted/38.flac"
                                hunted "No more circles to run in. It's time to sleep.\n"
                                jump den_collapse_final_menu

                        "{i}• (Explore) So we're dying down here. How long is that going to take?{/i}" if den_collapse_die_explore == False and den_collapse_stuck_explore and den_collapse_struggle:
                            $ den_collapse_die_explore = True
                            voice "audio/_pristine/voice/den/narrator/81.flac"
                            n "A while. You're stuck, not injured.\n"
                            voice "audio/_pristine/voice/den/skeptic/29.flac"
                            skeptic "I wonder what'll get us first. Suffocation? Thirst?\n"
                            voice "audio/_pristine/voice/den/hunted/39.flac"
                            hunted "We could always just let ourselves die.\n"
                            voice "audio/_pristine/voice/den/hero/37.flac"
                            hero "That doesn't sound like you. I thought you were about survival.\n"
                            voice "audio/_pristine/voice/den/hunted/40.flac"
                            hunted "Only when survival is possible. There's nothing left for us here but suffering.\n"
                            voice "audio/_pristine/voice/den/skeptic/30.flac"
                            skeptic "Hate to break it to you, but you can't just decide to die. Death is something that happens to you. It's external. It's a consequence.\n"
                            voice "audio/_pristine/voice/den/hero/38.flac"
                            hero "You almost sound like you think we deserve this.\n"
                            voice "audio/_pristine/voice/den/skeptic/31.flac"
                            skeptic "We made a mistake. It's what's supposed to happen to us. It's the only way we can learn.\n"
                            jump den_collapse_final_menu

                        "{i}• (Explore) Come on, you have to give us something! Just a little wiggle room.{/i}" if den_collapse_stuck_explore == False:
                            $ den_collapse_stuck_explore = True
                            voice "audio/_pristine/voice/den/skeptic/32.flac"
                            skeptic "If we had wiggle room, He would have said we had wiggle room.\n"
                            jump den_collapse_circles

                        "{i}• (Explore) [[Struggle to free yourself.]{/i}" if den_collapse_struggle == False:
                            $ den_collapse_struggle = True
                            voice "audio/_pristine/voice/den/skeptic/33.flac"
                            skeptic "Hah. Good luck with that.\n"
                            voice "audio/_pristine/voice/den/narrator/82.flac"
                            n "You do your best to move your body, but try as you might, your earthen coffin doesn't budge in the slightest.\n"
                            voice "audio/_pristine/voice/den/skeptic/34.flac"
                            skeptic "This is pointless. Just give up already and die a miserable death with the rest of us. And then we'll start again, and we'll do better.\n"
                            jump den_collapse_final_menu

                        "{i}• ''We can't both be stuck here! This can't be how it ends. You must be able to free us.''{/i}":
                            voice "audio/_pristine/voice/den/narrator/83.flac"
                            show den buried eye closed onlayer back
                            with dissolve
                            n "The Princess' eye closes in concentration as she attempts, and fails, to move her body. I'm afraid you {i}are{/i} both stuck.\n"
                            show den buried eye sad onlayer back
                            with dissolve
                            jump den_collapse_final

                        "{i}• ''This is both of our faults. I'm sorry.''{/i}":
                            label den_collapse_okay:
                                voice "audio/_pristine/voice/den/narrator/84.flac"
                                show den buried eye sadder onlayer back
                                with dissolve
                                n "A tear clouds the eye. 'It's okay.' It isn't. If this is the end, don't reconcile with this creature. Revile her. This is her fault. She did this.\n"
                                jump den_collapse_final

                        "{i}• ''This is my fault. I should have done things differently. I'm sorry.''{/i}":
                            jump den_collapse_okay

                        "{i}• ''Yes. This is your fault.''{/i}":
                            voice "audio/_pristine/voice/den/narrator/85a.flac"
                            show den buried eye saddest onlayer back
                            with dissolve
                            n "A tear clouds the eye. 'I'm sorry.' Don't listen to her. She's not capable of feeling remorse. The only thing she's sorry about is being stuck here. If this is the end, don't die offering her forgiveness. She doesn't deserve it.\n"
                            jump den_collapse_final

                        "{i}• ''This isn't anybody's fault.''{/i}":
                            jump den_collapse_okay

                        "{i}• ''I know whose fault this is, and it isn't ours.''{/i}":
                            if blade_held:
                                voice "audio/_pristine/voice/den/narrator/86.flac"
                                n "Oh, and I suppose you think this is my fault? As if. You had your chance to save the world, and you squandered it by turning your back on destiny. Deciding not to do anything is still a choice.\n"
                            else:
                                voice "audio/_pristine/voice/den/narrator/87.flac"
                                n "Oh, and I suppose you think this is my fault? As if. You had your chance to come down here prepared, and you left your weapon behind.\n"
                            voice "audio/_pristine/voice/den/narrator/88.flac"
                            n "This is on you. You have free will, and you decided to use it.\n"
                            jump den_collapse_final

                        "{i}• [[Wait in silence for your end.]{/i}":
                            voice "audio/_pristine/voice/den/hunted/41.flac"
                            hunted "Yes. It's time. There will be peace soon, even if it's short.\n"
                            voice "audio/_pristine/voice/den/skeptic/35a.flac"
                            skeptic "Not until we really suffer for it.\n"
                            label den_collapse_final:
                                voice "audio/_pristine/voice/den/skeptic/36a.flac"
                                skeptic "We all know where this is going, so get on with it.\n"
                                voice "audio/_pristine/voice/den/narrator/89.flac"
                                n "{i}Deep breathing{/i}. All right. And I'll go into extra detail, just for you.\n"
                                voice "audio/_pristine/voice/den/narrator/90.flac"
                                n "The weight of the world you have destroyed rests on your chest. It both crushes and cradles you, holding your lungs in a stasis where you can never take in quite enough breath for comfort.\n"
                                voice "audio/_pristine/voice/den/narrator/91.flac"
                                show den buried eye sadder onlayer back at Position(ypos=1125)
                                show starving den buried 1 onlayer back at Position(ypos=1125)
                                with Dissolve(0.5)
                                n "Your limbs ache, muscles screaming in their locked positions, one arm slowly growing numb as your blood struggles to reach it. There is dirt in your eyes. They fill with tears.\n"
                                voice "audio/_pristine/voice/den/hero/39.flac"
                                hero "Okay, I think that's enough, we get the picture. Skip to the 'everything goes dark' part, please.\n"
                                voice "audio/_pristine/voice/den/narrator/92.flac"
                                show den buried eye saddest onlayer back at Position(ypos=1125)
                                show starving den buried 2 onlayer back at Position(ypos=1125)
                                with Dissolve(0.5)
                                n "No, not quite yet, I haven't even gotten to the starvation. Or the thirst. That gnawing that starts as a nibble, a little reminder that despite it all, you're still alive.\n"
                                voice "audio/_pristine/voice/den/narrator/93.flac"
                                show den buried eye open onlayer back at Position(ypos=1125)
                                show starving den buried 3 onlayer back at Position(ypos=1125)
                                with Dissolve(0.5)
                                n "You can see that she, too, feels herself being eaten from the inside. Her gaze never leaves you. Any semblance of thought has vanished, replaced with a desire for the only thing that can sate her hunger.\n"
                                voice "audio/_pristine/voice/den/narrator/94.flac"
                                n "You can feel a strain as your parched mouth attempts—and fails—to water. But even with a dry tongue, your hunger is such that you can't help but think about what her flesh might taste like.\n"
                                #voice "audio/_pristine/voice/den/narrator/95.flac"
                                #n "You swallow, pretending there is any substance in your throat to save you. And soon enough you cannot even summon enough saliva to drool. You feel dry, despite the dampness of the earth, your body yearning for an ounce of moisture as your tongue turns to sandpaper in your mouth.\n"
                                voice "audio/_pristine/voice/den/skeptic/37.flac"
                                skeptic "Don't think I'll forget how much you're enjoying this, you sick bastard.\n"
                                voice "audio/_pristine/voice/den/narrator/96.flac"
                                stop music fadeout 20.0
                                stop sound fadeout 20.0
                                stop tertiary fadeout 20.0
                                play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 20.0
                                show starving den buried 4 onlayer back at Position(ypos=1125)
                                with Dissolve(0.5)
                                # SPLIT INTO TWO
                                n "Don't worry, The end is close. Your mind grows cloudy as your blood slows, your chest trying to suck in enough oxygen to feed your starved muscles, your bruised ribs doing little more than bumping up against hard-packed dirt. You aren't even sure you have limbs anymore, or whether the vacant ache where they once were is just the memory of limbs. Any second, you might breathe in one last shallow, earth-choked breath...\n"
                                voice "audio/_pristine/voice/den/hero/40.flac"
                                hide den onlayer back
                                hide bg onlayer back
                                hide starving onlayer back
                                show quiet creep3 onlayer back at Position(ypos=1125)
                                show hands den buried start onlayer back at Position(ypos=1125)
                                show starving den buried 5 onlayer back at Position(ypos=1125)
                                with Dissolve(0.5)
                                hero "Well? Are we almost done yet?\n"
                                voice "audio/_pristine/voice/den/hunted/42.flac"
                                hunted "He's gone.\n"
                                voice "audio/_pristine/voice/den/skeptic/38.flac"
                                skeptic "And we're somewhere new. Is this what happens when we really die?\n"
                                $ gallery_den.unlock_item(11)
                                $ renpy.save_persistent()
                                hide starving onlayer back
                                with Dissolve(1.0)
                                truth "Neither you nor the Princess ever draw that final breath, because neither of you dies here. As the world around you unwinds, she places her head at your feet. 'I'm cold' say her eyes. 'I don't want to be cold.'\n"
                                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                                hide den onlayer front
                                hide bg onlayer back
                                show hands den buried 1 onlayer back
                                with Dissolve(0.75)
                                $ renpy.pause(0.75)
                                show hands den buried 2 onlayer back
                                with Dissolve(0.75)
                                $ renpy.pause(0.75)
                                show hands den buried 3 onlayer back
                                with Dissolve(0.5)
                                $ renpy.pause(0.5)
                                show hands den buried 4 onlayer back
                                with Dissolve(0.35)
                                $ renpy.pause(0.35)
                                show hands den buried 5 onlayer back
                                with Dissolve(0.25)
                                $ renpy.pause(0.25)
                                hide player onlayer front
                                show hands den buried 6 onlayer back
                                with Dissolve(0.25)
                                $ renpy.pause(0.25)
                                hide hands onlayer back
                                with Dissolve(0.25)
                                $ renpy.pause(0.25)
                                $ blade_held = False
                                $ default_mouse = "default"
                                hide bg onlayer back
                                hide bg onlayer front
                                hide player onlayer front
                                hide player onlayer back
                                hide fore onlayer front
                                hide mid onlayer front
                                hide fore onlayer inyourface
                                hide farback onlayer farback
                                hide bg onlayer back
                                hide bg onlayer farback
                                hide mid onlayer back
                                hide stars onlayer farback
                                hide bg onlayer back
                                hide quiet onlayer back
                                hide quiet onlayer front
                                hide quiet onlayer farback
                                show farback quiet onlayer farback at Position(ypos=1125)
                                with Dissolve(4.0)
                                show mirror quiet distant onlayer back at Position(ypos=1125)
                                if loops_finished != 0:
                                    truth "But you don't get the opportunity to respond, nor will you ever. It's time to leave. Memory returns.\n"
                                else:
                                    truth "But you don't get the opportunity to respond. Something has taken her away, and it's left something else in her place.\n"
                                $ achievement.grant("ACH_DEN_STARVE")
                                $ beast_2_end = "starve"
                                $ princess_kept += 1
                                $ princess_deny += 1
                                jump mirror_start
