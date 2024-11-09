label apotheosis_start_contrarian:

    default apotheosis_end = ""

    $ trait_contrarian = True
    voice "audio/voices/ch3/apotheosis/narrator/1.flac"
    n "You're on a path in the woods. And at the end of that path—\n{w=3.7}{nw}"
    show screen disableclick(0.5)
    voice "audio/_pristine/voice/apotheosis/contrarian/0.flac"
    contrarian "Oh, let me guess! And at the end of that path is a cabin.\n"
    voice "audio/voices/ch3/apotheosis/narrator/2.flac"
    n "Excuse me?\n"
    voice "audio/_pristine/voice/apotheosis/contrarian/2.flac"
    contrarian "Come on, man. We can see it right in front of us! And besides, we've been here like... what, five times already?\n"
    voice "audio/_pristine/voice/apotheosis/hero/2.flac"
    hero "I think this is three.\n"
    voice "audio/_pristine/voice/apotheosis/contrarian/3.flac"
    contrarian "Who cares?! The woods are always the worst part, anyway. Nothing ever happens in them.\n"
    voice "audio/_pristine/voice/apotheosis/narrator/1.flac"
    n "I care! Every single time you've been here, it means an entire other reality has been damned to oblivion. One reality is already an incalculable loss. And there is a massive difference between three and five.\n"
    voice "audio/_pristine/voice/apotheosis/contrarian/5a.flac"
    contrarian "It feels like the numbers getting thrown around here are too big not to be abstract.\n"
    voice "audio/_pristine/voice/apotheosis/hero/4.flac"
    hero "Numbers like five?\n"
    voice "audio/_pristine/voice/apotheosis/contrarian/6.flac"
    contrarian "Numbers like entire realities. At the end of the day it's all just silly, isn't it? None of us can count to a whole reality, and he's asking us to think about the difference between three and five.\n"
    voice "audio/_pristine/voice/apotheosis/narrator/2.flac"
    n "{i}Sigh{/i} You're already starting to lose the thread. Just because you can't personally sum up the contents of an entire reality doesn't mean that the people inhabiting it don't contain moral value. If you have any sense of ethics left in there, if you have any moral compass... please. You have to stop her.\n"
    voice "audio/_pristine/voice/apotheosis/broken/1.flac"
    broken "Don't you get it? Might makes right. And she didn't even have to touch us last time to prove her power.\n"
    voice "audio/_pristine/voice/apotheosis/contrarian/7.flac"
    contrarian "So what, just because she made us kill ourselves we're supposed to submit to her authority without question?\n"
    #voice "audio/_pristine/voice/apotheosis/hero/5.flac"
    #hero "Hey! We didn't kill ourselves. He was the one who turned that knife on us.\n"
    voice "audio/_pristine/voice/apotheosis/broken/2.flac"
    broken "I knew when to surrender to our better. You would have lost eventually anyway, and it would only have made her angry. It would only have made things worse for all of us.\n"
    voice "audio/_pristine/voice/apotheosis/narrator/3.flac"
    n "Oh for the love of— can you all please just get on with it? You're not making this any easier for yourselves.\n"
    voice "audio/_pristine/voice/apotheosis/hero/6.flac"
    hero "Do we even have agency right now? We either do what she wants, or we do what He wants. Either way we're listening to somebody.\n" id apotheosis_start_contrarian_b83f1cde
    voice "audio/_pristine/voice/apotheosis/contrarian/9.flac"
    contrarian "Please! Nothing in life is a binary. Obviously we find a third choice that nobody wants.\n"
    voice "audio/_pristine/voice/apotheosis/broken/3.flac"
    broken "You all talk about choices and freedom, but there is no choice when it comes to the will of a god.\n"
    voice "audio/_pristine/voice/apotheosis/narrator/4.flac"
    n "I'm going to cut you off right there. She is not a god, and the more times you fail, the harder it becomes for you to succeed. But the fact that you're still here means you still have a chance to pull this off. So, Princess. Dangerous. Cabin. Slay. Now!\n"
    jump apotheosis_explore_menu

label contrarian_pristine_apoth_menu:
    default contrarian_pristine_apoth_menu_explore = False
    menu:
        extend ""

        "{i}• (Explore) Hey, funny one, didn't you say something about a third option earlier? One that would make everyone unhappy?{/i}" if contrarian_pristine_apoth_menu_explore == False:
            $ contrarian_pristine_apoth_menu_explore = True
            if apotheosis_run:
                voice "audio/_pristine/voice/apotheosis/contrarian/10.flac"
                contrarian "I dunno! I'm at loss. What if we... run away again? I'm sure it'll work this time.\n"
            else:
                voice "audio/_pristine/voice/apotheosis/contrarian/11a.flac"
                contrarian "Well, we could always run away, right?\n"
            voice "audio/_pristine/voice/apotheosis/hero/7.flac"
            hero "To where?\n"
            if apotheosis_run:
                voice "audio/_pristine/voice/apotheosis/contrarian/12.flac"
                contrarian "Anywhere!\n"
            else:
                voice "audio/_pristine/voice/apotheosis/contrarian/13.flac"
                contrarian "I dunno. Anywhere!\n"
            voice "audio/_pristine/voice/apotheosis/broken/4.flac"
            broken "You're all ruining the moment of her ascension. Have you no respect for the divine?\n"
            jump contrarian_pristine_apoth_menu

        "{i}• [[Take the blade.]{/i}":
            voice "audio/_pristine/voice/apotheosis/narrator/5.flac"
            $ blade_held = True
            $ default_mouse = "thumb"
            play audio "audio/one_shot/knife_pickup.flac"
            hide blade onlayer front
            show player apotheosis blade tree onlayer inyourface at Position(ypos=1125)
            with dissolve
            n "With a grim determination, you yank the blade from the trunk.\n"
            voice "audio/_pristine/voice/apotheosis/contrarian/14.flac"
            hide player onlayer inyourface
            hide fore onlayer front
            hide mid onlayer back
            hide stars onlayer farback
            show stars apotheosis charge onlayer farback at Position(ypos=1125)
            show apotheosis charge onlayer back at Position(ypos=1125)
            show fore apotheosis charge onlayer front at Position(ypos=1125)
            show player apotheosis charge onlayer inyourface at Position(ypos=1125)
            with Dissolve(1.0)
            contrarian "Yeah. This feels right. She doesn't get to just smugly stand over us like we don't matter. Let's take her down a peg.\n"
            voice "audio/_pristine/voice/apotheosis/broken/5.flac"
            broken "You're not going to win. You know that, right? What are you going to do with that tiny blade? Give her a scratch?\n"
            voice "audio/_pristine/voice/apotheosis/hero/8.flac"
            hero "Even if that's all we manage, I'd rather go down swinging.\n"
            voice "audio/_pristine/voice/apotheosis/contrarian/15.flac"
            contrarian "See how everything's floating around her? I bet we could make it if we just jumped really hard.\n"
            voice "audio/_pristine/voice/apotheosis/narrator/6.flac"
            hide stars onlayer farback
            hide apotheosis onlayer back
            hide fore onlayer front
            hide player onlayer inyourface
            with fade
            scene bg black
            with fade
            n "You gather yourself, closing your eyes and shutting out the towering vision of the Princess. There is only her, and you. That's all there ever was.\n"
            voice "audio/_pristine/voice/apotheosis/narrator/7.flac"
            show stars apotheosis charge onlayer farback at Position(ypos=1125)
            show apotheosis charge onlayer back at Position(ypos=1125)
            show fore apotheosis charge onlayer front at Position(ypos=1125)
            show player apotheosis charge onlayer inyourface at Position(ypos=1125)
            with fade
            n "It's time to face her.\n"
            menu:
                extend ""

                "{i}• [[Charge into oblivion.]{/i}":
                    $ quick_menu = False
                    voice "audio/_pristine/voice/apotheosis/narrator/8.flac"
                    play tertiary "audio/one_shot/footstep_run_dirt_short.flac"
                    queue tertiary "audio/final/den_emerge.flac"
                    hide stars onlayer farback
                    hide apotheosis onlayer back
                    hide fore onlayer front
                    hide player onlayer inyourface
                    with fade
                    show stars apotheosis charge 2 onlayer farback at Position(ypos=1125)
                    show bg apotheosis charge 2 onlayer back at Position(ypos=1125)
                    show apotheosis charge 2 onlayer back at Position(ypos=1125)
                    show fore apotheosis charge 2 onlayer front at Position(ypos=1125)
                    show player apotheosis charge onlayer inyourface at Position(ypos=1125)
                    with fade
                    if persistent.quick_menu:
                        $ quick_menu = True
                    n "You launch yourself towards the Princess. The pull of her gravity catches you, carrying you across the ground into the violent swirl of her orbit.\n"
                    $ gallery_apotheosis.unlock_item(3)
                    $ renpy.save_persistent()
                    voice "audio/_pristine/voice/apotheosis/princess/1.flac"
                    play audio "audio/final/Tower_WindWHistlingFly_oneshot_1.flac"
                    hide stars onlayer farback
                    hide apotheosis onlayer back
                    hide fore onlayer front
                    show stars apotheosis charge 3 onlayer farback at Position(ypos=1125)
                    show bg apotheosis charge 3 onlayer back at Position(ypos=1125)
                    show apotheosis charge 3 onlayer back at Position(ypos=1125)
                    show fore apotheosis charge 3 onlayer front at Position(ypos=1125)
                    with Dissolve(2.0)
                    sp "Such defiance, even now. Do it, then. Show me what you think it takes to end that which is destined to end everything.\n"
                    voice "audio/_pristine/voice/apotheosis/broken/6.flac"
                    show apotheosis charge 3 onlayer back at Position(ypos=1125)
                    with dissolve
                    broken "Don't you see how hopeless this is? She fears nothing.\n"
                    voice "audio/_pristine/voice/apotheosis/contrarian/16a.flac"
                    contrarian "That's right, she doesn't. So she has no idea what she's in for.\n"

            voice "audio/_pristine/voice/apotheosis/narrator/9.flac"
            play audio "audio/final/Adversary_BPlayerAggressivelyThrown_1.flac"
            hide stars onlayer farback
            hide bg onlayer back
            hide apotheosis onlayer back
            hide player onlayer inyourface
            hide fore onlayer front
            show farback apotheosis chest onlayer farback at Position(ypos=1125)
            show apotheosis chest onlayer front at Position(ypos=1125)
            show debris apotheosis chest onlayer inyourface at Position(ypos=1125)
            with Dissolve(1.0)
            n "With a heavy thump, you land on her chest.\n"
            voice "audio/_pristine/voice/apotheosis/hero/9.flac"
            hero "It's now or never. We've come this far, let's take it home.\n"
            menu:
                extend ""

                "{i}• [[Carve into her divine heart.]{/i}":
                    $ gallery_apotheosis.unlock_item(9)
                    $ renpy.save_persistent()
                    voice "audio/_pristine/voice/apotheosis/narrator/10.flac"
                    play audio "audio/_pristine/sfx/apotheosis_knife_doomed.flac"
                    show apotheosis chest slash 1 onlayer front
                    with dissolve
                    n "You strike, but her skin is like steel. Though you stab at her again and again, the wounds are superficial, mere etchings in a sprawling surface.\n"
                    voice "audio/_pristine/voice/apotheosis/broken/7.flac"
                    show apotheosis chest slash 2 onlayer front
                    with dissolve
                    broken "You see? It was always pointless. All this has done is bring us close to her... and how beautiful it is, to be so close.\n"
                    voice "audio/_pristine/voice/apotheosis/hero/10.flac"
                    hero "It's not pointless, it can't be! We wouldn't be here if there wasn't some hope we could succeed.\n"

            voice "audio/_pristine/voice/apotheosis/princess/2.flac"
            show apotheosis chest onlayer front
            with Dissolve(1.0)
            sp "Is that all?\n"
            $ quick_menu = False
            voice "audio/_pristine/voice/apotheosis/narrator/11.flac"
            play secondary "audio/final/den_emerge.flac"
            queue secondary "audio/one_shot/door_stone.flac"
            hide farback onlayer farback
            hide debris onlayer inyourface
            hide apotheosis onlayer front
            hide player onlayer inyourface
            scene bg black
            with fade
            show farback apotheosis pluck onlayer farback at Position(ypos=1125)
            show debris apotheosis pluck onlayer front at Position(ypos=1125)
            show apotheosis pluck onlayer back at Position(ypos=1125)
            with fade
            if persistent.quick_menu:
                $ quick_menu = True
            n "The Princess plucks you from her chest, pinching the scruff of your neck delicately between two fingers as she brings you to eye level.\n"
            voice "audio/_pristine/voice/apotheosis/princess/3.flac"
            show apotheosis pluck talk onlayer back
            with dissolve
            sp "I forgive you your transgressions. But my destiny is inescapable.\n"
            voice "audio/_pristine/voice/apotheosis/contrarian/17.flac"
            show apotheosis pluck onlayer back
            with dissolve
            contrarian "She thinks she's so much better than us! There has to be something else we can do, we're not going out like this.\n"
            voice "audio/_pristine/voice/apotheosis/broken/8.flac"
            broken "She offered us forgiveness. You would turn down such an incredible gift? You would turn away from her glory for something as petty as pride?\n"
            menu:
                extend ""

                "{i}• [[Hurl the blade at her eye.]{/i}":
                    voice "audio/_pristine/voice/apotheosis/contrarian/18.flac"
                    contrarian "Yes. YES! Let's give her something to remember us by.\n"
                    $ blade_held = False
                    $ default_mouse = "default"
                    voice "audio/_pristine/voice/apotheosis/narrator/12.flac"
                    play audio "audio/final/Razor_SwordSwish_1.flac"
                    show knife apotheosis hurl onlayer inyourface at Position(ypos=1125)
                    show player apotheosis hurl onlayer inyourface at Position(ypos=1125)
                    with dissolve
                    n "You concentrate your will to a fine point, and hurl your blade at the Princess' eye. It flies through the night sky and...\n"
                    voice "audio/_pristine/voice/apotheosis/broken/9.flac"
                    broken "And then nothing. She could never be harmed by—\n{w=5.20}{nw}"
                    show screen disableclick(0.5)
                    $ gallery_apotheosis.unlock_item(10)
                    $ renpy.save_persistent()
                    stop music
                    stop music2
                    voice "audio/_pristine/voice/apotheosis/princess/scream1.flac"
                    play audio "audio/one_shot/new/STP_stabcut_1.flac"
                    hide knife onlayer inyourface
                    hide player onlayer inyourface
                    hide farback onlayer farback
                    hide debris onlayer front
                    hide apotheosis onlayer back
                    show farback apotheosis eye out onlayer farback at shakeshort, Position(ypos=1125)
                    show debris apotheosis eye out onlayer front at shakeshort, Position(ypos=1125)
                    show apotheosis eye out onlayer back at shakeshort, Position(ypos=1125)
                    with dissolve
                    sp "AHHHHHHHHHHHHHHHHHH!\n"
                    voice "audio/_pristine/voice/apotheosis/narrator/13b.flac"
                    n "It pierces her cornea.\n"
                    voice "audio/_pristine/voice/apotheosis/narrator/14.flac"
                    play audio "audio/_pristine/sfx/breeze.flac"
                    show debris apotheosis eye out onlayer front at zoom_fall
                    show apotheosis eye out onlayer back at zoom_fall
                    n "She howls, recoiling in pain, and you fall from her distracted hand.\n"
                    $ quick_menu = False
                    play tertiary "audio/one_shot/tackle.flac"
                    queue tertiary "audio/final/Tower_Earthquake_oneshot_faded_1.flac"
                    voice "audio/_pristine/voice/apotheosis/narrator/15.flac"
                    stop sound fadeout 5.0
                    play secondary "audio/_pristine/sfx/Apotheosis Oppresive AMB_2loop.flac" loop
                    hide debris onlayer front
                    hide farback onlayer farback
                    hide apotheosis onlayer back
                    with fade
                    scene bg black
                    with fade
                    scene bg black
                    with fade
                    scene farback apotheosis eye crash onlayer farback at Position(ypos=1125)
                    show debris apotheosis eye crash onlayer front at Position(ypos=1125)
                    show apotheosis eye crash onlayer back at Position(ypos=1125)
                    with fade
                    if persistent.quick_menu:
                        $ quick_menu = True
                    n "You hit the ground with a painful thud. She narrowly misses you as she comes crashing down to her knees.\n"
                    voice "audio/_pristine/voice/apotheosis/princess/4a.flac"
                    show apotheosis eye crash talk onlayer back
                    with Dissolve(0.5)
                    sp "So I've misread you. You are not the willful key that will turn the lock of my liberation. You are an enemy to be smitten by my hand.\n"
                    voice "audio/_pristine/voice/apotheosis/narrator/16.flac"
                    play sound "audio/_pristine/sfx/Apotheosis HiPitch tear_4.flac"
                    queue sound "audio/_pristine/sfx/Apotheosis Oppresive_11.flac"
                    play tertiary "audio/_pristine/sfx/apotheosis_erupt.flac"
                    queue tertiary "audio/final/grey_fire_loop3.ogg" loop
                    show quiet creep1 onlayer farback at Position(ypos=1125)
                    show apotheosis eye beam onlayer back
                    show shine apotheosis eye beam 1 onlayer back at Position(ypos=1125)
                    with Dissolve(1.0)
                    n "The Princess holds up her monumental hand, its glowing palm radiating a blinding light. It grows, and grows, until it's all you can see. And then you erupt, your very soul mere kindling to her light.\n"
                    play audio "audio/_pristine/sfx/Apotheosis Oppresive_12.flac"
                    voice "audio/_pristine/voice/apotheosis/narrator/17b.flac"
                    play sound "audio/_pristine/sfx/Apotheosis Oppresive_7.flac"
                    show shine apotheosis eye beam 2 onlayer front
                    with dissolve
                    n "The inferno incinerates everything that is you, and with it... no. No, that's not right! Why is it hot? I'm not supposed to be able to feel anything oh no, oh no no no no no...\n"
                    voice "audio/_pristine/voice/apotheosis/princess/5.flac"
                    play audio "audio/_pristine/sfx/Apotheosis HiPitch tear_3.flac"
                    show apotheosis eye beam talk onlayer back
                    show shine apotheosis eye beam 3 onlayer inyourface
                    with dissolve
                    sp "You leave me no other choice! Suffer for the crime you have committed against my divine body! ... damnation will purify us both.\n"
                    $ gallery_apotheosis.unlock_item(11)
                    $ renpy.save_persistent()
                    $ quick_menu = False
                    stop music fadeout 10.0
                    stop music2 fadeout 10.0
                    stop sound fadeout 10.0
                    stop secondary fadeout 10.0
                    stop tertiary fadeout 10.0
                    play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 10.0
                    hide debris onlayer front
                    hide apotheosis onlayer back
                    hide farback onlayer farback
                    hide shine onlayer inyourface
                    hide shine onlayer back
                    hide shine onlayer inyourface
                    hide shine onlayer farback
                    hide shine onlayer front
                    hide quiet onlayer farback
                    show farback apotheosis eye post onlayer farback at Position(ypos=1125)
                    show quiet creep3 onlayer farback at Position(ypos=1125)
                    show fore apotheosis eye post onlayer front at Position(ypos=1125)
                    show apotheosis eye post beam onlayer front at Position(ypos=1125)
                    with Dissolve(4.0)
                    if persistent.quick_menu:
                        $ quick_menu = True
                    truth "There is nothing left to burn. Yet still you persist amid a world unraveled.\n"
                    voice "audio/_pristine/voice/apotheosis/princess/6.flac"
                    sp "It's cold now. And I feel... small. I thought I was everything.\n"
                    voice "audio/_pristine/voice/apotheosis/princess/7.flac"
                    show apotheosis eye post beam talk onlayer front
                    with Dissolve(0.5)
                    sp "But I'm no better than you, am I?\n"
                    play audio "audio/final/assorted_Handsgrabbing_BIG_1.flac"
                    hide apotheosis onlayer front
                    hide fore onlayer front
                    show hands apotheosis eye 1 onlayer front at Position(ypos=1125)
                    with Dissolve(1.5)
                    $ renpy.pause(1.0)
                    show hands apotheosis eye 2 onlayer front at Position(ypos=1125)
                    with Dissolve(1.0)
                    $ renpy.pause(0.5)
                    show hands apotheosis eye 3 onlayer front at Position(ypos=1125)
                    with Dissolve(0.5)
                    $ renpy.pause(0.25)
                    show hands apotheosis eye 4 onlayer front at Position(ypos=1125)
                    with Dissolve(0.25)
                    $ renpy.pause(0.125)
                    show hands apotheosis eye 5 onlayer front at Position(ypos=1125)
                    with Dissolve(0.25)
                    $ renpy.pause(0.125)
                    show hands apotheosis eye 6 onlayer front at Position(ypos=1125)
                    with Dissolve(0.25)
                    $ renpy.pause(0.125)
                    show hands apotheosis eye 7 onlayer front at Position(ypos=1125)
                    with Dissolve(0.25)
                    $ renpy.pause(0.125)
                    hide hands onlayer front
                    with Dissolve(0.25)
                    $ renpy.pause(0.125)
                    $ blade_held = False
                    $ default_mouse = "default"
                    stop music
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
                    hide quiet onlayer farback
                    hide quiet onlayer front
                    show farback quiet onlayer farback at Position(ypos=1125)
                    with Dissolve(4.0)
                    show mirror quiet distant onlayer back at Position(ypos=1125)
                    if loops_finished != 0:
                        truth "You do not get the chance to respond, nor will you ever. It's time to leave. Memory returns.\n"
                    else:
                        truth "You do not get the chance to respond, nor will you ever. Something has taken her away, and it's left something else in her place.\n"
                    $ achievement.grant("ACH_APOTH_BLIND")
                    $ trait_broken = False
                    $ trait_contrarian = False
                    $ apotheosis_end = "defy"
                    $ princess_deny += 1
                    $ princess_kept += 1
                    menu:

                        "{i}• [[Approach the mirror.]{/i}":
                            hide mirror onlayer back
                            show content m empty onlayer front at Position(ypos=1125)
                            show mirror frame onlayer front at Position(ypos=1125)
                            with Dissolve(2.0)
                            truth "Silence as you approach. The voices all have burned away.\n"
                            menu:

                                extend ""

                                "{i}• [[Gaze into your reflection.]{/i}":
                                    jump mirror_n_gaze_join



                "{i}• [[Embrace your new goddess.]{/i}":
                    default apotheosis_contrarian_late_join = False
                    $ apotheosis_contrarian_late_join = True
                    $ blade_held = False
                    $ default_mouse = "default"
                    play audio "audio/final/Tower_WindWHistlingFly_oneshot_1.flac"
                    voice "audio/_pristine/voice/apotheosis/contrarian/20.flac"
                    contrarian "So much for spiting her. Spiting Him it is.\n"
                    voice "audio/_pristine/voice/apotheosis/princess/8a.flac"
                    show apotheosis pluck talk onlayer back
                    with dissolve
                    sp "Good. I can feel your heart opening to mine.\n"
                    #sp "Good. I can feel your heart opening to mine. Here, come to my side.\n"
                    jump apotheosis_contrarian_freedom_join

        "{i}• [[Embrace your new goddess.]{/i}":
            label apotheosis_pristine_freedom:
                if trait_contrarian:
                    voice "audio/_pristine/voice/apotheosis/contrarian/21.flac"
                    contrarian "All right. Spiting Him it is.\n"
                    voice "audio/_pristine/voice/apotheosis/narrator/18a.flac"
                    n "You don't know what you're doing!\n"
                    voice "audio/_pristine/voice/apotheosis/contrarian/22.flac"
                    contrarian "That's half the fun!\n"
                else:
                    voice "audio/_pristine/voice/apotheosis/broken/11.flac"
                    broken "This was our only real choice. Even the ground itself kneels to her.\n"
                    voice "audio/_pristine/voice/apotheosis/paranoid/1.flac"
                    paranoid "It was all turned to dust so easily. Is it even real?\n"
                    #voice "audio/_pristine/voice/apotheosis/hero/12.flac"
                    #hero "The ground has to be real. Look at all these chunks of it floating around us, they seem plenty real to me.\n"
                voice "audio/_pristine/voice/apotheosis/princess/9.flac"
                hide blade onlayer front
                hide player onlayer inyourface
                hide fore onlayer front
                hide mid onlayer back
                hide stars onlayer farback
                show stars apotheosis charge onlayer farback at Position(ypos=1125)
                show apotheosis charge onlayer back at Position(ypos=1125)
                show fore apotheosis charge onlayer front at Position(ypos=1125)
                with Dissolve(1.0)
                sp "Fill the empty seat by my side. Join me for a new dawn.\n"
                voice "audio/_pristine/voice/apotheosis/narrator/19.flac"
                play audio "audio/final/den_emerge.flac"
                hide stars onlayer farback
                hide apotheosis onlayer back
                hide fore onlayer front
                hide player onlayer inyourface
                show stars apotheosis charge 2 onlayer farback at Position(ypos=1125)
                show bg apotheosis charge 2 onlayer back at Position(ypos=1125)
                show apotheosis charge 2 onlayer back at Position(ypos=1125)
                show fore apotheosis charge 2 onlayer front at Position(ypos=1125)
                with Dissolve(2.0)
                n "You fool. You can feel the pull of her gravity catch you, carrying you from the ground into the violent swirl of her orbit.\n"
                voice "audio/_pristine/voice/apotheosis/princess/10.flac"
                play audio "audio/final/Tower_WindWHistlingFly_oneshot_1.flac"
                hide stars onlayer farback
                hide apotheosis onlayer back
                hide fore onlayer front
                show stars apotheosis charge 3 onlayer farback at Position(ypos=1125)
                show bg apotheosis charge 3 onlayer back at Position(ypos=1125)
                show apotheosis charge 3 onlayer back at Position(ypos=1125)
                show fore apotheosis charge 3 onlayer front at Position(ypos=1125)
                with Dissolve(2.0)
                sp "Come to me.\n"
                label apotheosis_contrarian_freedom_join:
                    play audio "audio/_pristine/sfx/breeze.flac"
                    voice "audio/_pristine/voice/apotheosis/narrator/20.flac"
                    if apotheosis_contrarian_late_join:
                        show farback apotheosis pluck onlayer farback at apoth_zoom_fall, Position(ypos=1125)
                        show debris apotheosis pluck onlayer front at apoth_zoom_fall, Position(ypos=1125)
                        show apotheosis pluck onlayer back at apoth_zoom_fall, Position(ypos=1125)
                    else:
                        show stars apotheosis charge 3 onlayer farback at apoth_zoom_fall, Position(ypos=1125)
                        show bg apotheosis charge 3 onlayer back at apoth_zoom_fall, Position(ypos=1125)
                        show apotheosis charge 3 onlayer back at apoth_zoom_fall, Position(ypos=1125)
                        show fore apotheosis charge 3 onlayer front at apoth_zoom_fall, Position(ypos=1125)
                    n "Her words are like a gentle tug, drawing you closer to the mountain of her body.\n"

                    voice "audio/_pristine/voice/apotheosis/narrator/21.flac"
                    play audio "audio/one_shot/thump.flac"
                    hide stars onlayer farback
                    hide farback onlayer farback
                    hide debris onlayer front
                    hide bg onlayer back
                    hide apotheosis onlayer back
                    hide fore onlayer front
                    show farback apotheosis join land onlayer farback at Position(ypos=1125)
                    show apotheosis join land onlayer back at Position(ypos=1125)
                    show debris apotheosis join land onlayer front at Position(ypos=1125)
                    with Dissolve(1.5)
                    n "You land softly on her shoulder. Her skin is warm and comforting. This really is the end, isn't it?\n"
                    voice "audio/_pristine/voice/apotheosis/hero/13b.flac"
                    hero "Is it the end? We're still here.\n"
                    $ renpy.music.set_volume(0.65, 4.0, channel='music')
                    stop sound fadeout 10.0
                    stop secondary fadeout 10.0
                    stop tertiary fadeout 10.0
                    play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 10.0
                    hide farback onlayer farback
                    show bg apotheosis join quiet onlayer farback at Position(ypos=1125)
                    show apotheosis join quiet onlayer back at Position(ypos=1125)
                    show debris apotheosis join quiet onlayer front at Position(ypos=1125)
                    with Dissolve(2.0)
                    truth "The night sky unweaves into a textured nothingness. He does not respond.\n"
                    if trait_contrarian:
                        voice "audio/_pristine/voice/apotheosis/broken/12.flac"
                        broken "Everything is gone but us and her. This is her power. This is where we're meant to be.\n"
                        voice "audio/_pristine/voice/apotheosis/hero/14a.flac"
                        hero "He's really gone? Huh. That's... unexpected. But He would have said something by now if were still here, right?\n"
                        voice "audio/_pristine/voice/apotheosis/contrarian/23.flac"
                        contrarian "Yeah. Never knew when to shut up, that one. It's part of why I liked him so much. I can't believe all it took to make Him disappear was saying 'no' once.\n"
                    else:
                        voice "audio/_pristine/voice/apotheosis/paranoid/2.flac"
                        paranoid "There's nothing left but us and her. Even the dust is gone.\n" id apotheosis_contrarian_freedom_join_065ce724
                        #voice "audio/_pristine/voice/apotheosis/broken/12a.flac"
                        #broken "What was it He said? 'I'm here to keep him in check?' Well He's gone now, and the truth has been revealed.\n"
                        voice "audio/_pristine/voice/apotheosis/broken/13.flac"
                        broken "She's the answer to our questions. She always has been. He tried to blind you all... but she broke through His lies. As she always would.\n"
                    voice "audio/_pristine/voice/apotheosis/hero/15.flac"
                    hero "... What happens now?\n"
                    if trait_paranoid:
                        voice "audio/_pristine/voice/apotheosis/paranoid/3.flac"
                        paranoid "Even though the whole world's turned to nothing, we still exist. And if we're real, then there must be something else that's real, something that's been hidden from us. We have to find it.\n"
                    voice "audio/_pristine/voice/apotheosis/princess/11.flac"
                    show apotheosis join quiet talk onlayer back
                    with dissolve
                    sp "This world is but an illusion keeping us from my ascension. A play of shadows dancing on the wall.\n"
                    if trait_paranoid:
                        voice "audio/_pristine/voice/apotheosis/paranoid/4.flac"
                        paranoid "Yes... she understands!\n"
                    label apotheosis_freedom_second_join:
                        $ gallery_apotheosis.unlock_item(8)
                        $ renpy.save_persistent()
                        play audio "audio/_pristine/sfx/Apotheosis Tentacle feather_1.flac"
                        scene reality ending
                        hide bg onlayer farback
                        show apotheosis reach onlayer back
                        show debris apotheosis reach onlayer front
                        with Dissolve(1.5)
                        truth "The Princess reaches forward into the textured nothing and buries her fingers in its divine flesh. Her touch is soft.\n"
                        voice "audio/_pristine/voice/apotheosis/princess/12a.flac"
                        show apotheosis reach talk onlayer back
                        with dissolve
                        sp "The flame may be snuffed, but the wall remains. This isn't just for my glory. You are a part of this now.\n"
                        voice "audio/_pristine/voice/apotheosis/broken/14.flac"
                        show apotheosis reach onlayer back
                        with dissolve
                        broken "See? This is nice. We're safe. She's helping us. She's helping everyone.\n"
                        $ renpy.music.set_volume(0.0, 0.75, channel='music')
                        $ renpy.music.set_volume(1.0, 0.75, channel='music2')
                        play audio "audio/final/Assorted_TapestyUnraveledBreakingRip_1.flac"
                        play sound "audio/_pristine/sfx/Apotheosis HiPitch tear_3.flac"
                        show apotheosis tear onlayer back
                        $ renpy.pause(0.75)
                        hide apotheosis onlayer back
                        hide debris onlayer front
                        scene bg black
                        show bg black onlayer farback
                        show apotheosis darkness 1 onlayer front at Position(ypos=1125)
                        truthmid "Her grip tightens, and somehow, you feel it. The pain sits at the limits of your comprehension. Like an endless sea of hands falling on you one after another after another before finally collapsing in on themselves. You lose yourself in the darkness.\n"
                        menu:
                            extend ""

                            "{i}• [[Scream in unintelligible agony.]{/i}":
                                jump apotheosis_freedom_suffer_join

                            "{i}• ''YOU HAVE TO STOP THIS, I CAN'T TAKE IT!''{/i}":
                                label apotheosis_freedom_suffer_join:
                                    #edited for flow! Kept all the same parts but made her a little less wordy. Could also take out distant for the dream part since fading memory is already implying the same kinda thing, up to you
                                    voice "audio/_pristine/voice/apotheosis/princess/13.flac"
                                    spmid "It will be over soon, little bird. Then your eyes will open, and all of this pain will seem but the fading memory of a distant dream.\n"
                                    voice "audio/_pristine/voice/apotheosis/hero/16.flac"
                                    hero "Soon...? Soon...? Does that mean there's gonna be more?\n"
                                    if trait_contrarian:
                                        voice "audio/_pristine/voice/apotheosis/contrarian/24.flac"
                                        contrarian "My only comfort is that He isn't here to see us suffer. He would love that, wouldn't he?\n"
                                    else:
                                        voice "audio/_pristine/voice/apotheosis/paranoid/5a.flac"
                                        paranoid "So many things we believed were real were nothing at all. Just look at the world around us, or lack thereof. Who's to say pain is even real?\n"
                                        voice "audio/_pristine/voice/apotheosis/hero/17.flac"
                                        hero "How about the fact that it HURTS?!\n"
                                    $ default_mouse = "eye"
                                    play audio "audio/final/Assorted_TapestyUnraveledBreakingRip_2.flac"
                                    play sound "audio/_pristine/sfx/Apotheosis HiPitch tear_4.flac"
                                    show apotheosis darkness 2 onlayer front
                                    with Dissolve(2.0)
                                    truthmid "The textured nothing is ripped open, and with it, you are ripped open. Amid a sea of dissociative pain, you can feel everything that is you pouring out into the ether. And you feel something else, too. Anger. A need to lash out and hurt that which is hurting you.\n"
                                    voice "audio/_pristine/voice/apotheosis/hero/18.flac"
                                    hero "Yes... hurt her! Do something, anything to make it stop!\n"
                                    voice "audio/_pristine/voice/apotheosis/broken/15.flac"
                                    broken "No! If suffering is what she demands of us, suffering is what we'll give! Why would I doubt our god?\n"
                                    if trait_contrarian:
                                        voice "audio/_pristine/voice/apotheosis/contrarian/25.flac"
                                        contrarian "It is so, so tempting to see what's on the other side of that great big nothing, but I think I'm going to lose myself if this goes on for much longer... why do we have to be the ones going through all this pain while she gets all the benefits?\n"
                                        voice "audio/_pristine/voice/apotheosis/broken/16.flac"
                                        broken "Blasphemer. We have been given the gift of offering ourselves to a higher purpose, and you spit in its face?\n"
                                    else:
                                        voice "audio/_pristine/voice/apotheosis/paranoid/6.flac"
                                        paranoid "We can endure this. It's all just words and ideas. We're only telling ourselves it's painful, it doesn't have to hurt if we don't think it should!\n" id apotheosis_freedom_suffer_join_2165cc71
                                    menu:

                                        extend ""

                                        "{i}• [[Make her suffer with you.]{/i}":
                                            if trait_paranoid:
                                                voice "audio/_pristine/voice/apotheosis/paranoid/7.flac"
                                                paranoid "Who am I kidding? It's not going to stop unless we make it stop. We have to make it stop.\n"
                                            label apotheosis_tendrils_shared_join:
                                                $ renpy.music.set_volume(1.0, 0.0, channel='music')
                                                $ renpy.music.set_volume(0.0, 0.0, channel='music2')
                                                stop music
                                                stop music2
                                                play sound "audio/_pristine/sfx/Apotheosis Tentacle feather_5.flac"
                                                show apotheosis darkness 5 onlayer front
                                                with dissolve
                                                truth "You are a wave of tendrils racing against themselves and down the shape of an arm. You snap around it.\n"
                                                play sound "audio/_pristine/sfx/apoth_snap.flac"
                                                $ quick_menu = False
                                                voice "audio/_pristine/voice/apotheosis/princess/scream2.flac"
                                                show apotheosis darkness 4 onlayer front
                                                sp "AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH!\n"
                                                $ default_mouse = "default"
                                                hide apotheosis darkness onlayer front
                                                with Dissolve(1.5)
                                                truth "Relief as a massive burden is lifted from you. You are in one piece. You are in your body.\n"
                                                $ gallery_apotheosis.unlock_item(12)
                                                $ renpy.save_persistent()
                                                scene reality ending
                                                show bg apotheosis prison low onlayer farback at Position(ypos=1125)
                                                show apotheosis prison onlayer back at Position(ypos=1125)
                                                with fade
                                                if persistent.quick_menu:
                                                    $ quick_menu = True
                                                truth "Your eyes open. Before you is the massive form of the Princess, arms bound by the textured nothing. Behind her a hole in the world leading into something beyond. Something beautiful.\n"
                                                if trait_contrarian:
                                                    voice "audio/_pristine/voice/apotheosis/contrarian/26.flac"
                                                    contrarian "I knew it, that old windbag was hiding all kinds of secrets from us. There's a whole world out there!\n"
                                                else:
                                                    voice "audio/_pristine/voice/apotheosis/paranoid/8a.flac"
                                                    paranoid "Th-there it is. Something actually real.\n"
                                                voice "audio/_pristine/voice/apotheosis/hero/19.flac"
                                                hero "I don't know what to say... it's just so beautiful.\n"
                                                voice "audio/_pristine/voice/apotheosis/broken/17.flac"
                                                broken "Doesn't the mere sight make all the misery worth it?\n"
                                                if trait_contrarian:
                                                    voice "audio/_pristine/voice/apotheosis/contrarian/27a.flac"
                                                    contrarian "Eh. It's not all that.\n"
                                                voice "audio/_pristine/voice/apotheosis/princess/14a.flac"
                                                show apotheosis prison talk onlayer back
                                                with dissolve
                                                sp "What did you do to me?! I was supposed to be perfect! I was supposed to be a god! I was all of those things and now I'm not. All because of YOU.\n"
                                                show apotheosis prison glance onlayer back
                                                with Dissolve(1.5)
                                                truth "She looks up with futile sorrow at the something beautiful that sits beyond.\n"
                                                $ gallery_apotheosis.unlock_item(13)
                                                $ renpy.save_persistent()
                                                voice "audio/_pristine/voice/apotheosis/princess/15a.flac"
                                                show apotheosis prison glance talk onlayer back
                                                with dissolve
                                                sp "We could have had everything, if only you had given me a little more. We could have been free on the wings of my glory. Now we're stuck here. Forever.\n"
                                                if trait_contrarian:
                                                    voice "audio/_pristine/voice/apotheosis/contrarian/28.flac"
                                                    show apotheosis prison onlayer back
                                                    with Dissolve(2.0)
                                                    contrarian "I for one am perfectly happy to be stuck here forever. It's more than worth it if that's the price we paid for taking her down a peg.\n"
                                                else:
                                                    voice "audio/_pristine/voice/apotheosis/paranoid/9.flac"
                                                    show apotheosis prison onlayer back
                                                    with Dissolve(2.0)
                                                    paranoid "We... we made this prison. And I don't think we can unmake it.\n"
                                                play audio "audio/_pristine/sfx/Apotheosis Tentacle feather_1.flac"
                                                hide bg onlayer farback
                                                show bg apotheosis quiet join onlayer farback at Position(ypos=1125)
                                                show apotheosis prison drop onlayer back
                                                with Dissolve(3.0)
                                                truth "The hole mends shut. As it closes, the tendrils loose their grip, freeing the Princess as they retreat.\n"
                                                voice "audio/_pristine/voice/apotheosis/broken/18.flac"
                                                scene bg black
                                                show apotheosis prison drop quiet onlayer back
                                                with dissolve
                                                broken "It's gone. No... no! How do we get it back? Can we try again? We'll suffer so much better if we get to try again, I promise!\n"
                                                voice "audio/_pristine/voice/apotheosis/princess/16.flac"
                                                show apotheosis prison drop talk onlayer back
                                                with dissolve
                                                sp "It's so cold here. If this wasn't enough... then what is?\n"
                                                play audio "audio/final/assorted_Handsgrabbing_BIG_1.flac"
                                                hide apotheosis onlayer back
                                                hide fore onlayer front
                                                show hands apotheosis prison 1 onlayer back at Position(ypos=1125)
                                                with Dissolve(1.5)
                                                $ renpy.pause(1.0)
                                                show hands apotheosis prison 2 onlayer back at Position(ypos=1125)
                                                with Dissolve(1.0)
                                                $ renpy.pause(0.5)
                                                show hands apotheosis prison 3 onlayer back at Position(ypos=1125)
                                                with Dissolve(0.5)
                                                $ renpy.pause(0.25)
                                                show hands apotheosis prison 4 onlayer back at Position(ypos=1125)
                                                with Dissolve(0.25)
                                                $ renpy.pause(0.125)
                                                show hands apotheosis prison 5 onlayer back at Position(ypos=1125)
                                                with Dissolve(0.25)
                                                $ renpy.pause(0.125)
                                                hide hands onlayer back
                                                with Dissolve(0.25)
                                                $ renpy.pause(0.125)
                                                $ blade_held = False
                                                $ default_mouse = "default"
                                                stop music
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
                                                hide quiet onlayer farback
                                                hide quiet onlayer front
                                                show farback quiet onlayer farback at Position(ypos=1125)
                                                with Dissolve(4.0)
                                                show mirror quiet distant onlayer back at Position(ypos=1125)
                                                if loops_finished != 0:
                                                    truth "But you don't get the opportunity to try again, nor will you ever. It's time to leave. Memory returns.\n"
                                                else:
                                                    truth "But you don't get the opportunity to try again. Something has taken her away, and it's left something else in her place.\n"
                                                $ achievement.grant("ACH_APOTH_BOUND")
                                                $ apotheosis_end = "prison"
                                                $ princess_kept += 1
                                                $ princess_deny += 1
                                                jump mirror_start

                                        "{i}• [[Suffer in the darkness alone.]{/i}":
                                            label apotheosis_alone_final_join:
                                                play sound "audio/_pristine/sfx/Apotheosis HiPitch tear_4.flac"
                                                show apotheosis darkness 3 onlayer front
                                                with Dissolve(2.0)
                                                truthmid "You continue to lose important pieces of yourself. The memories of entire lifetimes lived fade away into a space where your only recollection of them is that something used to be there.\n"
                                                play sound "audio/_pristine/sfx/Apotheosis Tentacle feather_5.flac"
                                                show apotheosis darkness anim onlayer front
                                                with dissolve
                                                truthmid "You die and are reborn, and die and are reborn, shrinking and shrinking again and again until there is no you left to die or shrink.\n"
                                                voice "audio/_pristine/voice/apotheosis/princess/17a.flac"
                                                spmid "You've done so well, little bird. Behold, the fruit of your anguish!\n"
                                                $ default_mouse = "default"
                                                $ quick_menu = False
                                                hide apotheosis onlayer front
                                                scene bg black
                                                with fade
                                                scene reality ending at blurred
                                                show bg apotheosis post tear onlayer farback at blurred, Position(ypos=1125)
                                                show apotheosis freedom begin onlayer back at cage_blur, Position(ypos=1125)
                                                with fade
                                                if persistent.quick_menu:
                                                    $ quick_menu = True
                                                truthmid "Eyes open. Are they yours? They don't feel like yours anymore, but there is no other word to describe what they belong to.\n"
                                                voice "audio/_pristine/voice/apotheosis/hero/20.flac"
                                                hero "Ugh... where are we?\n"
                                                if trait_contrarian:
                                                    voice "audio/_pristine/voice/apotheosis/contrarian/29.flac"
                                                    contrarian "Does it even matter? Here, there, it's all the same.\n"
                                                else:
                                                    voice "audio/_pristine/voice/apotheosis/paranoid/10.flac"
                                                    paranoid "It doesn't matter. We've never really known where we are, have we?\n"
                                                voice "audio/_pristine/voice/apotheosis/broken/19.flac"
                                                broken "You're all starting to sound like me.\n"
                                                $ renpy.music.set_volume(0.75, 1.25, channel='music')
                                                $ renpy.music.set_volume(0.0, 1.25, channel='music2')
                                                hide bg onlayer farback
                                                hide apotheosis onlayer back
                                                scene reality ending
                                                show bg apotheosis post tear onlayer farback at Position(ypos=1125)
                                                show apotheosis freedom begin onlayer back at Position(ypos=1125)
                                                with Dissolve(2.5)
                                                truth "Your vision focuses, revealing what has been done. The world has opened up. And beyond is something beautiful.\n"
                                                #sp "This is what's been hidden from us.\n"
                                                voice "audio/_pristine/voice/apotheosis/hero/21.flac"
                                                hero "Oh. What... what is that? I think I want to be there.\n"
                                                voice "audio/_pristine/voice/apotheosis/broken/20.flac"
                                                broken "It's where we're supposed to be.\n"
                                                if trait_contrarian:
                                                    voice "audio/_pristine/voice/apotheosis/contrarian/30.flac"
                                                    contrarian "Can we come back if we go there? I don't want to go there if it means we can't come back.\n"
                                                else:
                                                    voice "audio/_pristine/voice/apotheosis/paranoid/11.flac"
                                                    paranoid "It's something actually real.\n"
                                                #voice "audio/_pristine/voice/apotheosis/princess/18.flac"
                                                #sp "Come.\n"
                                                play audio "audio/_pristine/sfx/apoth_walk_short.flac"
                                                show bg apotheosis freedom begin onlayer farback at shakeshort, Position(ypos=1125)
                                                show apotheosis freedom brink onlayer back at shakeshort, Position(ypos=1125)
                                                with Dissolve(2.0)
                                                truth "The Princess steps forward, bringing you both to the edge of the something beautiful. It is dizzyingly vast.\n"
                                                $ renpy.music.set_volume(0.5, 0.5, channel='music')
                                                play tertiary "audio/final/Assorted_HordRunningRumble_1.flac"
                                                #play audio "audio/final/TheMound_SeaOfBodiesNEW_5.flac"
                                                show apotheosis freedom brink alarm onlayer back at shakeshort
                                                with Dissolve(1.0)
                                                truth "But neither of you cross the threshold. There is a roaring, like underground thunder. She is stopped in place.\n"
                                                if trait_contrarian:
                                                    voice "audio/_pristine/voice/apotheosis/contrarian/31.flac"
                                                    contrarian "Were we supposed to stop?\n"
                                                    voice "audio/_pristine/voice/apotheosis/hero/22.flac"
                                                    hero "I don't think this is over.\n"
                                                    #voice "audio/_pristine/voice/apotheosis/broken/21.flac"
                                                    #broken "But it has to be over. We're all that's left, and we're not powerful enough to hold her back.\n"
                                                else:
                                                    voice "audio/_pristine/voice/apotheosis/paranoid/12.flac"
                                                    paranoid "Something is holding us back. Is it one of us? Is it part of her? Is it some part of Him that managed to cling to this place?\n"
                                                    voice "audio/_pristine/voice/apotheosis/hero/23.flac"
                                                    hero "I don't think it's me. Would I know if it was me?\n"
                                                    #voice "audio/_pristine/voice/apotheosis/broken/22a.flac"
                                                    #broken "We're not powerful enough to hold her back. It has to be over. We're all that's left.\n"
                                                voice "audio/_pristine/voice/apotheosis/princess/19.flac"
                                                show apotheosis freedom brink talk onlayer back
                                                with Dissolve(1.0)
                                                sp "After everything I cast aside on my path to ascension... what remnant of the old could possibly be left to defy me?\n"
                                                $ renpy.music.set_volume(0.35, 0.5, channel='music')
                                                $ renpy.music.set_volume(0.6, 0.5, channel='music2')
                                                #play audio "audio/final/TheMound_SeaOfBodiesNEW_5.flac"
                                                $ gallery_apotheosis.unlock_item(14)
                                                $ renpy.save_persistent()
                                                play sound "audio/final/assorted_Handsgrabbing_BIG_1.flac"
                                                scene bg black
                                                hide bg onlayer farback
                                                hide apotheosis onlayer back
                                                scene farback quiet onlayer farback at Position(ypos=1125)
                                                show apotheosis freedom stopped lower onlayer back at Position(ypos=1125)
                                                show apotheosis freedom stopped upper onlayer front at Position(ypos=1125)
                                                with Dissolve(1.0)
                                                truth "You look down. At the Princess' feet writhes a shifting mound, a mass of hands clambering over each other, crawling their way up her body. They start to pull.\n"
                                                voice "audio/_pristine/voice/apotheosis/princess/no2.flac"
                                                play audio "audio/_pristine/sfx/Apotheosis HiPitch tear_4.flac"
                                                play sound "audio/final/assorted_Handsgrabbing_BIG_2.flac"
                                                $ renpy.music.set_volume(0.25, 0.5, channel='music')
                                                $ renpy.music.set_volume(0.75, 0.5, channel='music2')
                                                show apotheosis freedom stopped lower onlayer back at shakeshort
                                                show apotheosis freedom stopped talk onlayer front at shakeshort
                                                with Dissolve(1.0)
                                                sp "NO!\n"
                                                $ gallery_apotheosis.unlock_item(15)
                                                $ renpy.save_persistent()
                                                play sound "audio/final/assorted_Handsgrabbing_BIG_1.flac"
                                                play audio "audio/_pristine/sfx/shifty_crawl.flac"
                                                $ renpy.music.set_volume(0.15, 0.5, channel='music')
                                                $ renpy.music.set_volume(0.85, 0.5, channel='music2')
                                                show apotheosis freedom mound attack lower onlayer back
                                                show apotheosis freedom mound attack upper onlayer front
                                                with Dissolve(1.5)
                                                truth "The mound becomes a sea, and the Princess struggles to stay afloat, to keep the two of you close to the hole in the world and the light of the something beautiful beyond. But she is drowning.\n"
                                                #voice "audio/_pristine/voice/apotheosis/broken/23.flac"
                                                #broken "How can a god possibly drown? She... she can't! Nothing could kill her, she's better than death!\n"
                                                #if trait_contrarian:
                                                #    voice "audio/_pristine/voice/apotheosis/contrarian/32.flac"
                                                #    contrarian "She clearly isn't, which means we've found a new top dog to annoy.\n"
                                                #    voice "audio/_pristine/voice/apotheosis/hero/24.flac"
                                                #    hero "How do we annoy {i}that{/i}?\n"
                                                #    voice "audio/_pristine/voice/apotheosis/contrarian/33.flac"
                                                #    contrarian "I dunno. I'm sure we'll figure something out.\n"
                                                #else:
                                                    # cut maybe
                                                    #voice "audio/_pristine/voice/apotheosis/paranoid/13.flac"
                                                    #paranoid "Of course... it isn't part of any of us holding her back. It's part of {i}her{/i}.\n"
                                                play audio "audio/_pristine/sfx/ShiftingMound sucked in blackhole_2.flac"
                                                play sound "audio/final/assorted_Handsgrabbing_BIG_1.flac"
                                                $ renpy.music.set_volume(0.0, 0.5, channel='music')
                                                $ renpy.music.set_volume(1.0, 0.5, channel='music2')
                                                hide apotheosis onlayer back
                                                hide apotheosis onlayer front
                                                show apotheosis freedom drown lower onlayer farback at Position(ypos=1125)
                                                show apotheosis freedom drown upper onlayer back at Position(ypos=1125)
                                                with Dissolve(2.0)
                                                truth "As the sea rises, she pulls you from her shoulder and holds you above the tide. You turn back to look at her.\n"
                                                voice "audio/_pristine/voice/apotheosis/broken/24.flac"
                                                broken "We have to be able to do something to help her! This can't be how it ends, it can't, it can't it can't it can't!\n"
                                                voice "audio/_pristine/voice/apotheosis/princess/20.flac"
                                                show apotheosis freedom drown talk onlayer back at Position(ypos=1125)
                                                with Dissolve(1.0)
                                                sp "I think... this is the end. I can feel every part of me freezing over.\n"
                                                play sound "audio/final/assorted_Handsgrabbing_BIG_2.flac"
                                                play audio "audio/_pristine/sfx/shifty_hands.flac"
                                                stop music
                                                $ renpy.music.set_volume(1.0, 0.5, channel='music')
                                                $ renpy.music.set_volume(0.70, 0.5, channel='music2')
                                                show apotheosis freedom drown cold lower onlayer farback at Position(ypos=1125)
                                                show apotheosis freedom drown cold upper onlayer back at Position(ypos=1125)
                                                with Dissolve(2.0)
                                                truth "Hands reach over hands, pulling at her face. Dragging her down into their frigid depths. She is tired, and life fades from her eyes.\n"
                                                $ gallery_apotheosis.unlock_item(16)
                                                $ renpy.save_persistent()
                                                voice "audio/_pristine/voice/apotheosis/princess/21.flac"
                                                $ renpy.music.set_volume(0.4, 0.5, channel='music2')
                                                show apotheosis freedom drown cold talk onlayer back at Position(ypos=1125)
                                                with Dissolve(1.0)
                                                sp "You have been the only thing I've ever known to show me grace. I am sorry if I have not shown you the same.\n"
                                                #voice "audio/_pristine/voice/apotheosis/hero/25.flac"
                                                #hero "Huh. So she had a heart after all.\n"
                                                #if trait_contrarian:
                                                #    voice "audio/_pristine/voice/apotheosis/broken/25.flac"
                                                #    broken "Of course she did. Everything has a heart.\n"
                                                #    voice "audio/_pristine/voice/apotheosis/contrarian/34.flac"
                                                #    contrarian "{i}Sniff{/i}. Yeah. But where does that leave us?\n"
                                                #else:
                                                #    voice "audio/_pristine/voice/apotheosis/paranoid/14.flac"
                                                #    paranoid "All she wanted was freedom... just like us.\n"
                                                #    voice "audio/_pristine/voice/apotheosis/broken/26.flac"
                                                #    broken "Everything has a heart. I'm glad you could all finally see what I saw in her.\n"
                                                $ gallery_apotheosis.unlock_item(17)
                                                $ renpy.save_persistent()
                                                play audio "audio/final/den_emerge.flac"
                                                hide apotheosis onlayer back
                                                hide apotheosis onlayer farback
                                                show apotheosis freedom yeet onlayer farback at Position(ypos=1125)
                                                with Dissolve(1.5)
                                                truth "The Princess summons the last of her strength, her face a shield of purpose and determination. In her final act, she hurls you towards the hole in the world, towards the something beautiful beyond.\n"
                                                # note to self, probably cut everything after fly, little bird
                                                voice "audio/_pristine/voice/apotheosis/princess/22.flac"
                                                sp "Fly, little bird.\n"
                                                voice "audio/_pristine/voice/apotheosis/broken/27.flac"
                                                hide apotheosis onlayer farback
                                                hide apotheosis onlayer back
                                                hide farback onlayer farback
                                                scene reality ending
                                                show bg apotheosis post tear 2 onlayer farback at Position(ypos=1125)
                                                with Dissolve(1.0)
                                                broken "No, no! I don't want to be somewhere she isn't! It would always be dark without her!\n"
                                                voice "audio/_pristine/voice/apotheosis/hero/26.flac"
                                                show bg apotheosis post tear 3 onlayer farback at Position(ypos=1125)
                                                with Dissolve(2.0)
                                                hero "It's what she wants for us. But can we make it?\n"

                                                if trait_contrarian:
                                                    voice "audio/_pristine/voice/apotheosis/contrarian/35a.flac"
                                                    show bg apotheosis post tear 4 onlayer farback at Position(ypos=1125)
                                                    with Dissolve(2.0)
                                                    contrarian "Of course we can, we can do whatever we want. And I... believe in her.\n"
                                                else:
                                                    voice "audio/_pristine/voice/apotheosis/paranoid/15.flac"
                                                    show bg apotheosis post tear 4 onlayer farback at Position(ypos=1125)
                                                    with Dissolve(2.0)
                                                    paranoid "Yeah. We just have to believe, and everything is going to be okay.\n"
                                                $ renpy.music.set_volume(0.0, 0.5, channel='music2')
                                                play audio "audio/_pristine/sfx/Apotheosis Tentacle feather_1.flac"
                                                stop music
                                                stop music2
                                                stop sound
                                                stop tertiary
                                                hide bg onlayer farback
                                                show farback quiet onlayer farback at Position(ypos=1125)
                                                with Dissolve(2.0)
                                                truth "But the hole seals before you can make it to the other side. If there is a time to bask in what lies beyond, it is not now.\n"
                                                play sound "audio/final/assorted_Handsgrabbing_BIG_2.flac"
                                                $ renpy.pause(0.125)
                                                $ blade_held = False
                                                $ default_mouse = "default"
                                                stop music
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
                                                hide quiet onlayer farback
                                                hide quiet onlayer front
                                                show farback quiet onlayer farback at Position(ypos=1125)
                                                with Dissolve(4.0)
                                                show mirror quiet distant onlayer back at Position(ypos=1125)
                                                if loops_finished != 0:
                                                    truth "As you turn to look back at her, you see that she is gone. It's time to leave. Memory returns.\n"
                                                else:
                                                    truth "As you turn to look back at her, you see that she is gone. Something has taken her away, and it's left something else in her place.\n"
                                                $ achievement.grant("ACH_APOTH_GRACE")
                                                $ apotheosis_end = "fly"
                                                $ princess_free += 1
                                                $ princess_satisfy += 1
                                                jump mirror_start_2


                            "{i}• ''YOU'RE HURTING ME!''{/i}":
                                jump apotheosis_freedom_suffer_join

                            "{i}• [[Suffer in silence.]{/i}":
                                jump apotheosis_freedom_suffer_join

        "{i}• [[Flee.]{/i}" if contrarian_pristine_apoth_menu_explore:
            # note, paranoid does not present flight as an option
            voice "audio/_pristine/voice/apotheosis/narrator/22.flac"
            $ quick_menu = False
            play tertiary "audio/one_shot/footstep_run_dirt_short.flac"
            queue tertiary "audio/final/den_emerge.flac"
            hide blade onlayer front
            hide player onlayer inyourface
            hide fore onlayer front
            hide mid onlayer back
            hide stars onlayer farback
            with fade
            show farback apotheosis flee onlayer farback at Position(ypos=1125)
            show apotheosis flee debris onlayer front at Position(ypos=1125)
            if persistent.quick_menu:
                $ quick_menu = True
            n "A coward to your core, you turn to flee, leaping from the piece of floating debris and into the empty space beyond where the woods used to be.\n"
            voice "audio/_pristine/voice/apotheosis/contrarian/36.flac"
            contrarian "Nah, this isn't cowardice! This is a calculated move.\n"
            voice "audio/_pristine/voice/apotheosis/narrator/23.flac"
            n "Sure it is.\n"
            voice "audio/_pristine/voice/apotheosis/hero/27.flac"
            hero "Can it be a bit of both? I'd be lying if I said I wasn't a just a little afraid of her.\n"
            voice "audio/_pristine/voice/apotheosis/princess/23.flac"
            sp "Are you so awestruck by my glory that you cannot bear to look at me? I. Think. Not.\n"
            voice "audio/_pristine/voice/apotheosis/narrator/24.flac"
            play audio "audio/one_shot/hard tighten.flac"
            show farback apotheosis flee pluck onlayer farback at Position(ypos=1125)
            show apotheosis flee pluck debris onlayer front at Position(ypos=1125)
            with dissolve
            n "As you fall, a great force pulls at the back of your neck, violently yanking you away from whatever lack of destination you were headed towards.\n"
            voice "audio/_pristine/voice/apotheosis/princess/24.flac"
            show apotheosis flee pluck debris onlayer front at shakeshort
            sp "Now witness me!\n"
            voice "audio/_pristine/voice/apotheosis/broken/28.flac"
            broken "Yes, your grace.\n"
            voice "audio/_pristine/voice/apotheosis/narrator/25.flac"
            $ quick_menu = False
            hide farback onlayer farback
            hide apotheosis onlayer front
            hide farback onlayer farback
            hide debris onlayer inyourface
            hide apotheosis onlayer front
            hide player onlayer inyourface
            scene bg black
            with fade
            show farback apotheosis pluck onlayer farback at Position(ypos=1125)
            show debris apotheosis pluck onlayer front at Position(ypos=1125)
            show apotheosis pluck onlayer back at Position(ypos=1125)
            with fade
            if persistent.quick_menu:
                $ quick_menu = True
            n "She turns you to face her. The scruff of your neck is held firmly between two giant fingers.\n"
            voice "audio/_pristine/voice/apotheosis/hero/28a.flac"
            hero "So much for running away.\n"
            voice "audio/_pristine/voice/apotheosis/princess/3.flac"
            show apotheosis pluck talk onlayer back
            with dissolve
            sp "I forgive you your transgressions. But my destiny is inescapable.\n"
            voice "audio/_pristine/voice/apotheosis/contrarian/37.flac"
            show apotheosis pluck onlayer back
            with dissolve
            contrarian "She's right. We don't even have a weapon. It's over, isn't it?\n"
            voice "audio/_pristine/voice/apotheosis/broken/29.flac"
            broken "And yet, she still extends her mercy. We should do as she says. Why are you all resisting in the first place?\n"
            menu:
                extend ""

                "{i}• [[Embrace your new goddess.]{/i}":
                    $ apotheosis_contrarian_late_join = True
                    $ blade_held = False
                    $ default_mouse = "default"
                    voice "audio/_pristine/voice/apotheosis/contrarian/20.flac"
                    contrarian "So much for spiting her. Spiting Him it is.\n"
                    voice "audio/_pristine/voice/apotheosis/princess/8a.flac"
                    show apotheosis pluck talk onlayer back
                    with dissolve
                    sp "Good. I can feel your heart opening to mine.\n"
                    jump apotheosis_contrarian_freedom_join


label paranoid_pristine_apoth_menu:

    menu:

        extend ""

        "{i}• [[Take the blade.]{/i}":
            voice "audio/voices/ch3/apotheosis/hero/11.flac"
            #voice "audio/_pristine/voice/apotheosis/hero/29.flac"
            hero "Yeah. Screw all of this. I'm with you. A real god wouldn't need us as part of her plan.\n"
            #voice "audio/voices/ch3/apotheosis/broken/t2_broken_5.flac"
            voice "audio/_pristine/voice/apotheosis/broken/30.flac"
            broken "You'll never make it to her, and even if you do, what could you possibly hope to accomplish?\n" id paranoid_pristine_apoth_menu_41712058
            #voice "audio/voices/ch3/apotheosis/hero/12.flac"
            voice "audio/_pristine/voice/apotheosis/hero/30.flac"
            hero "We'll do what we were always supposed to. We'll take this blade and we'll sink it into her heart.\n"
            voice "audio/_pristine/voice/apotheosis/paranoid/16.flac"
            paranoid "Look at the way everything's being flung around her. If we just throw ourselves in her direction... I don't know. Maybe it'll work. If our thoughts are what gave her power, maybe it can cut both ways. Hahahahahahaha. Maybe we can do whatever we want to do! Maybe none of this is real!\n"
            $ blade_held = True
            $ default_mouse = "blade"
            play audio "audio/one_shot/knife_pickup.flac"
            voice "audio/_pristine/voice/apotheosis/narrator/26.flac"
            hide blade onlayer front
            show player normal hold onlayer inyourface at Position(ypos=1125)
            with dissolve
            n "With a forceful tug, you yank the blade out from the tree.\n"
            voice "audio/voices/ch3/apotheosis/narrator/27.flac"
            $ quick_menu = False
            hide player onlayer inyourface
            hide fore onlayer front
            hide mid onlayer back
            hide stars onlayer farback
            show bg impact onlayer back at Position(ypos=1125)
            with dissolve
            n "You close your eyes and take a deep breath, and for a moment, you can feel everything around you, like you're a part of everything and everything is a part of you.\n"
            voice "audio/voices/ch3/apotheosis/narrator/28.flac"
            if persistent.quick_menu:
                $ quick_menu = True
            hide bg onlayer back
            show stars apotheosis charge onlayer farback at Position(ypos=1125)
            show apotheosis charge onlayer back at Position(ypos=1125)
            show fore apotheosis charge onlayer front at Position(ypos=1125)
            show player normal hold onlayer inyourface at Position(ypos=1125)
            with Dissolve(1.0)
            n "And then your eyes open, settling on your target. It's time.\n"
            menu:
                extend ""

                "{i}• [[Embrace your destiny.]{/i}":
                    $ quick_menu = False
                    voice "audio/_pristine/voice/apotheosis/narrator/29.flac"
                    play tertiary "audio/one_shot/footstep_run_dirt_short.flac"
                    queue tertiary "audio/final/den_emerge.flac"
                    hide stars onlayer farback
                    hide apotheosis onlayer back
                    hide fore onlayer front
                    hide player onlayer inyourface
                    with fade
                    show stars apotheosis charge 2 onlayer farback at Position(ypos=1125)
                    show bg apotheosis charge 2 onlayer back at Position(ypos=1125)
                    show apotheosis charge 2 onlayer back at Position(ypos=1125)
                    show fore apotheosis charge 2 onlayer front at Position(ypos=1125)
                    show player normal hold onlayer inyourface at Position(ypos=1125)
                    with fade
                    if persistent.quick_menu:
                        $ quick_menu = True
                    n "You launch yourself towards the Princess. You can feel the pull of her gravity catch you, carrying you from the ground into the violent swirl of her orbit.\n"
                    $ gallery_apotheosis.unlock_item(3)
                    $ renpy.save_persistent()
                    play audio "audio/final/Tower_WindWHistlingFly_oneshot_1.flac"
                    voice "audio/voices/ch3/apotheosis/princess/sp2.flac"
                    hide stars onlayer farback
                    hide apotheosis onlayer back
                    hide fore onlayer front
                    show stars apotheosis charge 3 onlayer farback at Position(ypos=1125)
                    show bg apotheosis charge 3 onlayer back at Position(ypos=1125)
                    show apotheosis charge 3 onlayer back at Position(ypos=1125)
                    show fore apotheosis charge 3 onlayer front at Position(ypos=1125)
                    with Dissolve(2.0)
                    voice "audio/_pristine/voice/apotheosis/princess/25.flac"
                    sp "Even now, you defy me. Do it, then. Show me what you think it takes to end what's destined to end everything.\n"
                    show apotheosis charge 3 onlayer back at Position(ypos=1125)
                    with dissolve
                    #voice "audio/voices/ch3/apotheosis/hero/13.flac"
                    voice "audio/_pristine/voice/apotheosis/hero/31.flac"
                    hero "Yeah. Do it. Show her.\n"
                    menu:
                        extend ""

                        "{i}• [[Assail the unassailable.]{/i}":
                            voice "audio/_pristine/voice/apotheosis/broken/31.flac"
                            broken "You're not going to win. You know that, right? What are you even going to do with that tiny knife? Give her a scratch?\n"
                            voice "audio/_pristine/voice/apotheosis/paranoid/17a.flac"
                            paranoid "Hahahahahahaha. You still don't get it, do you? We can be whatever we want to be. Nothing is real! It all might as well just be a dream.\n"
                            voice "audio/_pristine/voice/apotheosis/hero/32.flac"
                            hero "Are you okay?\n"
                            voice "audio/_pristine/voice/apotheosis/paranoid/18.flac"
                            play audio "audio/_pristine/sfx/breeze.flac"
                            hide player onlayer inyourface
                            hide bg onlayer back
                            hide stars onlayer farback
                            hide apotheosis onlayer back
                            hide fore onlayer front
                            show farback apotheosis paranoid attack 1 onlayer farback at Position(ypos=1125)
                            show debris apotheosis paranoid attack 1 back onlayer back at Position(ypos=1125)
                            show apotheosis paranoid attack 1 onlayer front at Position(ypos=1125)
                            show front apotheosis paranoid attack 1 onlayer inyourface at Position(ypos=1125)
                            with Dissolve(1.0)
                            paranoid "Of course I'm not okay! I've never been okay. But maybe I needed to never be okay for us to make this happen.\n"
                            $ gallery_apotheosis.unlock_item(4)
                            $ renpy.save_persistent()
                            voice "audio/_pristine/voice/apotheosis/narrator/30.flac"
                            play audio "audio/_pristine/sfx/apoth_swing_1.flac"
                            show apotheosis paranoid attack 2 onlayer front at Position(ypos=1125)
                            show front apotheosis paranoid attack 2 onlayer inyourface at Position(ypos=1125)
                            with Dissolve(1.0)
                            n "As you fall towards the Princess, you swing the blade in a massive arc, putting all of your strength behind it. It cuts a shockwave through the very air, splitting everything in its path.\n" id paranoid_pristine_apoth_menu_6e014c78
                            #voice "audio/_pristine/voice/apotheosis/hero/33.flac"
                            #hero "I'll be damned. We did that?\n"
                            $ renpy.music.set_volume(0.0, 0.5, channel='music')
                            #voice "audio/_pristine/voice/apotheosis/narrator/31.flac"
                            #play audio "audio/_pristine/sfx/Apotheosis Tentacle feather_5.flac"
                            #play tertiary "audio/_pristine/sfx/Apotheosis HiPitch tear_3.flac"
                            #show farback apotheosis paranoid attack 2 onlayer farback at Position(ypos=1125)
                            #show debris apotheosis paranoid attack 2 back onlayer back at Position(ypos=1125)
                            #show apotheosis paranoid attack 2 onlayer front at Position(ypos=1125)
                            #show front apotheosis paranoid attack 2 onlayer inyourface at Position(ypos=1125)
                            #with Dissolve(1.0)
                            #n "The divine confidence in the Princess' eyes fades as she sees it coming, horror dawning in her expression.\n"
                            voice "audio/_pristine/voice/apotheosis/broken/32.flac"
                            broken "It won't be enough.\n" id paranoid_pristine_apoth_menu_49b40114
                            voice "audio/_pristine/voice/apotheosis/princess/26.flac"
                            show apotheosis paranoid attack 2 talk onlayer front
                            with dissolve
                            sp "Huh. How unexpected.\n"
                            voice "audio/_pristine/voice/apotheosis/narrator/32.flac"
                            play audio "audio/_pristine/sfx/apoth_anime_pew.flac"
                            hide front onlayer inyourface
                            #scene bg impact onlayer inyourface at Position(ypos=1125)
                            #with Dissolve(1.0)
                            #hide bg onlayer inyourface
                            hide apotheosis onlayer front
                            hide debris onlayer back
                            if persistent.flickering:
                                show farback apotheosis paranoid attack dust onlayer farback at shakeshort
                                show apotheosis paranoid attack dust onlayer back at shakeshort, Position(ypos=1125)
                                show debris apotheosis paranoid attack dust onlayer front at shakeshort
                                show player apotheosis paranoid attack dust onlayer inyourface at shakeshort, Position(ypos=1125)
                                with flash
                            else:
                                show farback apotheosis paranoid attack dust onlayer farback at shakeshort
                                show apotheosis paranoid attack dust onlayer back at shakeshort, Position(ypos=1125)
                                show debris apotheosis paranoid attack dust onlayer front at shakeshort
                                show player apotheosis paranoid attack dust onlayer inyourface at shakeshort, Position(ypos=1125)
                                with dissolve
                            n "As the blow lands, the entire world shakes. The outline of the Princess disappears into a storm of dust and debris.\n"
                            play audio "audio/final/Tower_Earthquake_oneshot_faded_1.flac"
                            voice "audio/_pristine/voice/apotheosis/hero/34.flac"
                            hide farback onlayer farback
                            hide apotheosis onlayer back
                            hide debris onlayer front
                            hide player onlayer inyourface
                            show bg impact onlayer farback at shakeshort, Position(ypos=1125)
                            with fade
                            hero "Could we have done that the whole time?!\n"
                            voice "audio/_pristine/voice/apotheosis/broken/33.flac"
                            broken "It was a fluke, I'm sure. An accident. That's all.\n"
                            voice "audio/_pristine/voice/apotheosis/hero/35.flac"
                            hero "It won't be a fluke if we do it again.\n"
                            voice "audio/_pristine/voice/apotheosis/narrator/33.flac"
                            $ renpy.music.set_volume(1.0, 3.5, channel='music')
                            play audio "audio/_pristine/sfx/breeze.flac"
                            hide farback onlayer farback
                            hide apotheosis onlayer front
                            hide debris onlayer back
                            hide player onlayer inyourface
                            show farback apotheosis dust reveal onlayer farback at Position(ypos=1125)
                            show apotheosis dust reveal onlayer back at Position(ypos=1125)
                            show debris apotheosis dust reveal onlayer front at Position(ypos=1125)
                            with Dissolve(2.5)
                            n "As the dust settles, the form of the Princess comes back into view. Her skin and vestments are lightly scuffed, but her body is whole, and her face is full of self-righteous fury.\n"
                            voice "audio/_pristine/voice/apotheosis/hero/36a.flac"
                            hero "At least we made her mad. That has to count for something.\n"
                            #voice "audio/_pristine/voice/apotheosis/hero/36.flac"
                            #hero "Well, at least we made her mad. That means something.\n"
                            # Close the eyes on her dress as well.
                            voice "audio/_pristine/voice/apotheosis/narrator/34.flac"
                            show apotheosis dust reveal close onlayer back with dissolve
                            n "But she holds her anger back. Her eyes close, and a gentle smile curls across her lips.\n"
                            voice "audio/_pristine/voice/apotheosis/princess/27.flac"
                            show apotheosis dust reveal close talk onlayer back with dissolve
                            sp "And so the little bird has found his heart at the end of the world.\n"
                            voice "audio/_pristine/voice/apotheosis/narrator/35.flac"
                            show apotheosis dust reveal open onlayer back with dissolve
                            n "Her eyes flit open, pupils narrowing on your form.\n"
                            voice "audio/_pristine/voice/apotheosis/princess/28.flac"
                            show apotheosis dust reveal open talk onlayer back with dissolve
                            sp "But is it courage that courses through his veins? Or is it madness?\n" id paranoid_pristine_apoth_menu_662ca61c
                            #voice "audio/_pristine/voice/apotheosis/princess/29.flac"
                            #sp "So this is the final test before my ascension.\n"
                            voice "audio/_pristine/voice/apotheosis/narrator/36.flac"
                            show apotheosis dust reveal open onlayer back with dissolve
                            n "The world around her stills. The debris stops in place, and the air is calm and silent.\n"
                            voice "audio/_pristine/voice/apotheosis/princess/30.flac"
                            show apotheosis dust reveal open talk onlayer back with dissolve
                            sp "You walk a razor's edge. It won't be long before you slip.\n"
                            $ gallery_apotheosis.unlock_item(5)
                            $ renpy.save_persistent()
                            play tertiary "audio/_pristine/sfx/_rock_storm_3.flac"
                            play audio "audio/_pristine/sfx/Apotheosis HiPitch tear_4.flac"
                            voice "audio/_pristine/voice/apotheosis/narrator/37.flac"
                            if persistent.flickering:
                                hide debris onlayer front
                                hide farback onlayer farback
                                hide apotheosis onlayer back
                                show farback apotheosis paranoid pelt onlayer farback at Position(ypos=1125)
                                show apotheosis paranoid pelt onlayer back at Position(ypos=1125)
                                show debris apotheosis pelt anim onlayer front at Position(ypos=1125)
                                show player apotheosis pelt anim onlayer inyourface at Position(ypos=1125)
                                with flash
                            else:
                                hide debris onlayer front
                                hide farback onlayer farback
                                hide apotheosis onlayer back
                                show farback apotheosis paranoid pelt onlayer farback at Position(ypos=1125)
                                show apotheosis paranoid pelt onlayer back at Position(ypos=1125)
                                show debris apotheosis pelt anim onlayer front at Position(ypos=1125)
                                show player apotheosis pelt anim onlayer inyourface at Position(ypos=1125)
                                with Dissolve(1.0)
                            n "And then, in an instant, it all comes at you. You are pelted with stone after massive stone, even the pebbles slicing through you like bullets. You cannot hope to so much as move as the bombardment continues, your body being destroyed bit by bit, crushed under the mass of wood and rock.\n"
                            voice "audio/_pristine/voice/apotheosis/broken/34.flac"
                            hide farback onlayer farback
                            hide apotheosis onlayer back
                            hide debris onlayer front
                            hide player onlayer inyourface
                            show bg impact onlayer inyourface at Position(ypos=1125)
                            with dissolve
                            broken "It's over. You had your moment, I'll give you that, but that's all it was. Hope it was worth it.\n"
                            voice "audio/_pristine/voice/apotheosis/hero/37.flac"
                            hero "Enough with the 'you's! Whether you like it or not, you're a part of us. Hell, whether I like it or not, you're a part of us. That was your moment, too, and we can have another if we all work together. She's not your perfect goddess. Just look at what she's doing to you, her most loyal servant!\n"
                            voice "audio/_pristine/voice/apotheosis/broken/35.flac"
                            broken "This... isn't very nice. But we did make her angry. Isn't it what we deserve?\n"
                            voice "audio/_pristine/voice/apotheosis/paranoid/19.flac"
                            paranoid "Who deserves something like this? She wants her freedom at the expense of ours, and she's willing to destroy us over and over again if it helps her. What kind of god does that? Stop deluding yourself. If we're going to make this work, all of us need to see the truth!\n"
                            voice "audio/_pristine/voice/apotheosis/broken/36.flac"
                            broken "But... I love her.\n"
                            voice "audio/_pristine/voice/apotheosis/narrator/38.flac"
                            n "And she doesn't love you. She doesn't even know you exist. You are just a tiny part of an obstacle, and she is currently in the process of destroying said obstacle. So I suggest you snap out of it now while you still can.\n"
                            menu:
                                extend ""

                                "{i}• [[Still your doubts.]{/i}":
                                    #voice "audio/_pristine/voice/apotheosis/broken/37.flac"
                                    #broken "Okay... I'm willing to try.\n"
                                    #voice "audio/_pristine/voice/apotheosis/hero/39.flac"
                                    #hero "Glad to hear it. All together now.\n"
                                    #voice "audio/_pristine/voice/apotheosis/paranoid/20.flac"
                                    #paranoid "Right. Remember, the only thing that's real is whatever we believe.\n"
                                    $ default_mouse = "sword"
                                    play tertiary "audio/_pristine/sfx/_rock_storm_3.flac" loop
                                    voice "audio/_pristine/voice/apotheosis/narrator/39.flac"
                                    play audio "audio/_pristine/sfx/apoth_free_rocks.flac"
                                    hide bg onlayer inyourface
                                    if persistent.flickering:
                                        show farback apotheosis paranoid charge onlayer farback at Position(ypos=1125)
                                        show apotheosis paranoid charge onlayer back at Position(ypos=1125)
                                        show debris apotheosis pelt anim onlayer front at Position(ypos=1125)
                                        show player apotheosis paranoid charge onlayer inyourface at Position(ypos=1125)
                                        with flash
                                    else:
                                        show farback apotheosis paranoid charge onlayer farback at Position(ypos=1125)
                                        show apotheosis paranoid charge onlayer back at Position(ypos=1125)
                                        show debris apotheosis pelt anim onlayer front at Position(ypos=1125)
                                        show player apotheosis paranoid charge onlayer inyourface at Position(ypos=1125)
                                        with dissolve
                                    n "All at once, the pressure breaks. You burst through a mountain of debris and straight for the Princess' heart. As you soar towards her the eyes on her vestments open wide, the light of their gaze slowing your pursuit as more and more matter continues to assail you.\n"
                                    voice "audio/_pristine/voice/apotheosis/broken/38.flac"
                                    broken "But it's not enough to stop us, is it? We're going to make it to her.\n"
                                    stop tertiary fadeout 2.0
                                    voice "audio/_pristine/voice/apotheosis/narrator/40.flac"
                                    play audio "audio/final/Assorted_SwordMagicalCut_1.flac"
                                    hide debris onlayer front
                                    show farback apotheosis paranoid charge lift onlayer farback at Position(ypos=1125)
                                    show apotheosis paranoid charge lift onlayer back at Position(ypos=1125)
                                    show player apotheosis paranoid charge lift onlayer inyourface at Position(ypos=1125)
                                    with Dissolve(1.5)
                                    n "You are. As you draw near, you extend your blade, readying a powerful strike. It sings through the air.\n"
                                    voice "audio/_pristine/voice/apotheosis/narrator/41.flac"
                                    play audio "audio/_pristine/sfx/Apotheosis Sword Magic Grind Energy_6.flac"
                                    play tertiary "audio/_pristine/sfx/Apotheosis HiPitch tear_4.flac"
                                    if persistent.flickering:
                                        hide player onlayer inyourface
                                        show farback apotheosis paranoid barrier onlayer farback
                                        show apotheosis paranoid barrier onlayer back
                                        show field apotheosis paranoid barrier onlayer inyourface at Position(ypos=1125)
                                        show sparks apotheosis paranoid barrier onlayer inyourface at Position(ypos=1125)
                                        show player apotheosis paranoid barrier onlayer inyourface at Position(ypos=1125)
                                        with flash
                                    else:
                                        hide player onlayer inyourface
                                        show farback apotheosis paranoid barrier onlayer farback
                                        show apotheosis paranoid barrier onlayer back
                                        show field apotheosis paranoid barrier onlayer inyourface at Position(ypos=1125)
                                        show sparks apotheosis paranoid barrier onlayer inyourface at Position(ypos=1125)
                                        show player apotheosis paranoid barrier onlayer inyourface at Position(ypos=1125)
                                        with Dissolve(1.0)
                                    n "And is met with a barrier of light. You remain frozen in midair, the two of you unblinking, waiting to see who breaks first.\n"
                                    voice "audio/_pristine/voice/apotheosis/hero/40.flac"
                                    hero "And then we win... right?\n"
                                    voice "audio/_pristine/voice/apotheosis/paranoid/21.flac"
                                    paranoid "That's what should happen. Why isn't it happening? Did we do something wrong? Were all these powerful, heroic thoughts not enough?\n"
                                    voice "audio/_pristine/voice/apotheosis/broken/39.flac"
                                    broken "I believe! I believe in us! Isn't that enough?\n"
                                    voice "audio/_pristine/voice/apotheosis/paranoid/22a.flac"
                                    paranoid "Unless we got the rules wrong... I'm sorry. I think I messed this up.\n"
                                    default paranoid_apotheosis_fight_back = False

                                    # CONSIDERING just making this yet another one option menu where you can only successfully fight back — I don't think giving up here really adds anything, but it also feels like there's been too little room for player agency in this route.
                                    menu:

                                        extend ""

                                        "{i}• (Explore) Then what do we do? I thought you said that all of this was like a dream. That we could choose how it goes. So why can't we choose to win?{/i}":
                                            $ default_mouse = "blade"
                                            #voice "audio/_pristine/voice/apotheosis/hero/43.flac"
                                            #hero "It can't be! I thought you said that all of this was like a dream! That we could choose how it goes.\n"
                                            voice "audio/_pristine/voice/apotheosis/paranoid/25.flac"
                                            play audio "audio/_pristine/sfx/Apotheosis Oppresive_12.flac"
                                            hide sparks onlayer inyourface
                                            hide field onlayer inyourface
                                            show farback apotheosis barrier plummet onlayer farback
                                            show apotheosis barrier plummet onlayer back
                                            show player normal hold onlayer inyourface
                                            with Dissolve(1.0)
                                            paranoid "The thing with dreams is that they always end.\n"
                                            voice "audio/_pristine/voice/apotheosis/princess/34.flac"
                                            show apotheosis barrier plummet talk onlayer back
                                            with dissolve
                                            sp "An admirable effort, but one that would never have succeeded. Come. Let us leave this world of illusions.\n"
                                            voice "audio/_pristine/voice/apotheosis/narrator/45.flac"
                                            n "She's just trying to undermine you. She's lying, don't listen to her—\n{w=4.5}{nw}" id paranoid_pristine_apoth_menu_b722e168
                                            show screen disableclick(0.5)
                                            $ renpy.music.set_volume(0.5, 0.75, channel='music')
                                            $ blade_held = False
                                            $ default_mouse = "default"
                                            stop sound fadeout 10.0
                                            stop secondary fadeout 10.0
                                            stop tertiary fadeout 10.0
                                            play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 10.0
                                            show farback quiet onlayer farback
                                            show apotheosis paranoid quiet begin onlayer back
                                            show player apotheosis paranoid quiet begin onlayer inyourface
                                            with Dissolve(1.0)
                                            truth "But before He can finish His thought, He is gone, and your blade has vanished from your hand. The world around you unravels into a textured nothing.\n"
                                            voice "audio/_pristine/voice/apotheosis/princess/35.flac"
                                            hide player onlayer inyourface
                                            show apotheosis paranoid quiet begin talk onlayer back
                                            with Dissolve(1.0)
                                            sp "You have no weapon. Your will has been conquered.\n"

                                        "{i}• No! We just have to push harder! We wouldn't be here if there wasn't a way for us to win.{/i}":
                                            $ paranoid_apotheosis_fight_back = True
                                            voice "audio/_pristine/voice/apotheosis/hero/41.flac"
                                            hero "That's right! So come on, push! All of you!\n"
                                            voice "audio/_pristine/voice/apotheosis/broken/40.flac"
                                            broken "I'll do my best!\n"
                                            voice "audio/_pristine/voice/apotheosis/paranoid/23.flac"
                                            paranoid "All right. One. Last. Try.\n"
                                            voice "audio/_pristine/voice/apotheosis/narrator/42.flac"
                                            play audio "audio/_pristine/sfx/Apotheosis Sword Magic Grind Energy_4.flac"
                                            show field apotheosis paranoid barrier onlayer inyourface at shakeshort, Position(ypos=1125)
                                            show sparks apotheosis paranoid barrier onlayer inyourface at shakeshort,  Position(ypos=1125)
                                            show player apotheosis paranoid barrier onlayer inyourface at shakeshort,  Position(ypos=1125)
                                            n "You continue the struggle, your blade kicking up sparks as it grinds against the Princess' barrier. But you're getting to her.\n"
                                            voice "audio/_pristine/voice/apotheosis/princess/31.flac"
                                            show apotheosis paranoid barrier talk onlayer back
                                            with dissolve
                                            sp "Your persistence is admirable, but it's misplaced.\n"
                                            voice "audio/_pristine/voice/apotheosis/broken/41.flac"
                                            show apotheosis paranoid barrier onlayer back
                                            with dissolve
                                            broken "We're so much more than I thought we were... it won't be misplaced if we win!\n"
                                            $ gallery_apotheosis.unlock_item(6)
                                            $ renpy.save_persistent()
                                            voice "audio/_pristine/voice/apotheosis/narrator/43.flac"
                                            play audio "audio/_pristine/sfx/Apotheosis Sword Magic Grind Energy_10.flac"
                                            play tertiary "audio/_pristine/sfx/Apotheosis Sword Magic Grind Energy_3.flac"
                                            play secondary "audio/_pristine/sfx/barrier_break.flac"
                                            show sparks apotheosis paranoid barrier onlayer inyourface at shakeshort,  Position(ypos=1125)
                                            show player apotheosis paranoid barrier onlayer inyourface at shakeshort,  Position(ypos=1125)
                                            show field apotheosis shatter anim onlayer inyourface at shakeshort
                                            n "You ignore the Princess' words and push a little further, and then... a crack. And where that crack formed, another forms, and then another. Finally, it shatters.\n"
                                            voice "audio/_pristine/voice/apotheosis/hero/42.flac"
                                            hide sparks onlayer inyourface
                                            hide field onlayer inyourface
                                            with dissolve
                                            hero "We did it! We actually did it!\n"
                                            voice "audio/_pristine/voice/apotheosis/narrator/44.flac"
                                            play audio "audio/final/Assorted_SwordMagicalCut_2.flac"
                                            show farback apotheosis barrier plummet onlayer farback
                                            show apotheosis barrier plummet onlayer back
                                            show player apotheosis barrier plummet onlayer inyourface
                                            with Dissolve(1.0)
                                            n "The Princess' face remains serene as your blade plummets towards her heart.\n"
                                            voice "audio/_pristine/voice/apotheosis/princess/32.flac"
                                            show apotheosis barrier plummet talk onlayer back
                                            with dissolve
                                            sp "A victory, but one that remains rooted in the material. And I am beyond that now. Come. Let us leave this world of illusions.\n"
                                            $ renpy.music.set_volume(0.5, 0.75, channel='music')
                                            $ default_mouse = "default"
                                            $ blade_held = False
                                            stop sound fadeout 10.0
                                            stop secondary fadeout 10.0
                                            stop tertiary fadeout 10.0
                                            play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 10.0
                                            show farback quiet onlayer farback
                                            show apotheosis paranoid quiet begin onlayer back
                                            show player apotheosis paranoid quiet begin onlayer inyourface
                                            with Dissolve(2.0)
                                            truth "Before your blade can pierce her heart, it is vanished from your hand. The world around you unravels into a textured nothing.\n"
                                            $ achievement.grant("ACH_APOTH_BATTLE")
                                            voice "audio/_pristine/voice/apotheosis/princess/33.flac"
                                            hide player onlayer inyourface
                                            show apotheosis paranoid quiet begin talk onlayer back
                                            with Dissolve(1.0)
                                            sp "You have no weapon. Our battle is at an end.\n"
                                            #voice "audio/_pristine/voice/apotheosis/paranoid/24.flac"
                                            #paranoid "We didn't do that, did we? Maybe we're less in control here than I thought.\n"
                                            #voice "audio/_pristine/voice/apotheosis/paranoid/25.flac"
                                            #paranoid "The thing with dreams is that they always end.\n"



                                    voice "audio/_pristine/voice/apotheosis/broken/42.flac"
                                    show apotheosis paranoid quiet begin onlayer back
                                    with dissolve
                                    broken "Is she going to hurt us now?\n"
                                    #voice "audio/_pristine/voice/apotheosis/princess/36.flac"
                                    #sp "But it means something that you and I persist while nothing else does.\n"
                                    $ gallery_apotheosis.unlock_item(8)
                                    $ renpy.save_persistent()
                                    play audio "audio/_pristine/sfx/Apotheosis Tentacle feather_1.flac"
                                    scene reality ending
                                    hide apotheosis onlayer farback
                                    hide farback onlayer farback
                                    hide bg onlayer farback
                                    show apotheosis reach onlayer back
                                    show debris apotheosis reach onlayer front
                                    with Dissolve(1.5)
                                    truth "The Princess reaches forward into the textured nothing and buries her fingers in its divine flesh. Her touch is soft.\n"
                                    voice "audio/_pristine/voice/apotheosis/broken/43.flac"
                                    broken "Oh... that feels nice.\n"
                                    #voice "audio/_pristine/voice/apotheosis/hero/44.flac"
                                    #hero "Come on now, I know it feels easy to give up at a time like this, but there has to be something we can do.\n"
                                    #voice "audio/_pristine/voice/apotheosis/princess/37.flac"
                                    #sp "All that remains is for me to pull at the seams.\n"
                                    voice "audio/_pristine/voice/apotheosis/princess/12a.flac"
                                    show apotheosis reach talk onlayer back
                                    with dissolve
                                    sp "The flame may be snuffed, but the wall remains. This isn't just for my glory. You are a part of this now.\n"
                                    $ default_mouse = "eye"
                                    $ renpy.music.set_volume(0.0, 0.75, channel='music')
                                    $ renpy.music.set_volume(1.0, 0.75, channel='music2')
                                    play audio "audio/final/Assorted_TapestyUnraveledBreakingRip_1.flac"
                                    play sound "audio/_pristine/sfx/Apotheosis HiPitch tear_3.flac"
                                    show apotheosis tear onlayer back
                                    $ renpy.pause(0.75)
                                    hide apotheosis onlayer back
                                    hide debris onlayer front
                                    scene bg black
                                    show bg black onlayer farback
                                    show apotheosis darkness 1 onlayer front at Position(ypos=1125)
                                    truthmid "Her grip tightens, and somehow, you feel it. The pain sits at the limits of your comprehension. Like an endless sea of hands falling on you one after another after another before finally collapsing in on themselves. You lose yourself in the darkness.\n"
                                    voice "audio/_pristine/voice/apotheosis/broken/44.flac"
                                    broken "She's hurting us again. I've never hurt like this before.\n"
                                    voice "audio/_pristine/voice/apotheosis/hero/45.flac"
                                    hero "She isn't even touching us. How can she hurt us without touching us...?\n"
                                    voice "audio/_pristine/voice/apotheosis/paranoid/26.flac"
                                    paranoid "Unless all of this is us. No. No, we can't be this. But it feels like she's ripping us apart.\n"
                                    menu:
                                        extend ""

                                        "{i}• [[Fight back.]{/i}":
                                            voice "audio/_pristine/voice/apotheosis/paranoid/27.flac"
                                            paranoid "Maybe... maybe if we feel all of this nothing... maybe we can use it.\n"
                                            voice "audio/_pristine/voice/apotheosis/hero/46.flac"
                                            hero "Anything to make this stop!\n"
                                            voice "audio/_pristine/voice/apotheosis/broken/45.flac"
                                            broken "Anything to make her feel what we feel.\n"
                                            if paranoid_apotheosis_fight_back == False:
                                                jump apotheosis_tendrils_shared_join
                                            else:
                                                $ renpy.music.set_volume(1.0, 0.0, channel='music')
                                                $ renpy.music.set_volume(0.0, 0.0, channel='music2')
                                                stop music
                                                stop music2
                                                play sound "audio/_pristine/sfx/Apotheosis Tentacle feather_5.flac"
                                                show apotheosis darkness 5 onlayer front
                                                with dissolve
                                                truth "You are a wave of tendrils racing against themselves and down the shape of an arm. You snap around it.\n"
                                                play sound "audio/_pristine/sfx/apoth_snap.flac"
                                                $ quick_menu = False
                                                voice "audio/_pristine/voice/apotheosis/princess/scream2.flac"
                                                show apotheosis darkness 4 onlayer front
                                                spmid "AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH!\n"
                                                voice "audio/_pristine/voice/apotheosis/broken/46a.flac"
                                                broken "But that isn't enough, is it? We can show her more... we can show her what she's done to us! We can make her understand. We can make her feel what we've felt.\n"
                                                play audio "audio/_pristine/sfx/Apotheosis HiPitch tear_3.flac"
                                                show apotheosis paranoid torment 1 onlayer front
                                                with Dissolve(1.5)
                                                truth "Your awareness shifts between undulating fibers of nothingness that is somehow outside of your body, but part of it. Time yields to feeling.\n" id paranoid_pristine_apoth_menu_2cc606fd
                                                play audio "audio/_pristine/sfx/Apotheosis Tentacle feather_5.flac"
                                                show apotheosis paranoid torment 2 onlayer front
                                                with Dissolve(1.0)
                                                truth "You wrap around wrist, ankle, neck, and pull from her heart the whole of her experience, and in return, she pulls from your heart the whole of yours.\n"
                                                play audio "audio/_pristine/sfx/Apotheosis Oppresive_12.flac"
                                                show apotheosis paranoid torment 3 onlayer front
                                                with Dissolve(1.0)
                                                truth "So much of her is empty bluster. Boasts muttered first in quiet to give an empty life a sense of meaning, and then the same boasts wrapped in a bow of true belief.\n"
                                                play audio "audio/one_shot/hard tighten.flac"
                                                show apotheosis paranoid torment 4 onlayer front
                                                with Dissolve(1.0)
                                                truth "Belief turned to arrogance. Arrogance that shatters as she finally sees something other than herself.\n"
                                                voice "audio/_pristine/voice/apotheosis/princess/39.flac"
                                                show apotheosis paranoid torment 4 talk onlayer front
                                                with Dissolve(1.0)
                                                sp "Oh. We've both hurt each other so very much, haven't we?\n"
                                                $ gallery_apotheosis.unlock_item(7)
                                                $ renpy.save_persistent()
                                                play sound "audio/final/Assorted_TapestyUnraveledBreakingRip_2.flac"
                                                play audio "audio/_pristine/sfx/Fury Body Horror_1.flac"
                                                $ quick_menu = False
                                                hide apotheosis onlayer front
                                                with fade
                                                show farback quiet onlayer farback at Position(ypos=1125)
                                                show apotheosis paranoid torment final quiet onlayer back at Position(ypos=1125)
                                                with fade
                                                if persistent.quick_menu:
                                                    $ quick_menu = True
                                                truth "Your eyes open. She is bound to you, and you are bound to her. Hollow echoes of what you used to be.\n"
                                                voice "audio/_pristine/voice/apotheosis/princess/40.flac"
                                                show apotheosis paranoid torment final talk onlayer back
                                                with dissolve
                                                sp "I can hear your voices prattle in my head. I was never going to ascend. This is all so very small. I'm so very small. I'm sorry.\n"
                                                play audio "audio/final/assorted_Handsgrabbing_BIG_1.flac"
                                                hide apotheosis onlayer back
                                                hide fore onlayer front
                                                show hands apotheosis paranoid onlayer back at Position(ypos=1125)
                                                with Dissolve(1.5)
                                                $ renpy.pause(1.0)
                                                show hands apotheosis paranoid 2 onlayer back at Position(ypos=1125)
                                                with Dissolve(1.0)
                                                $ renpy.pause(0.5)
                                                show hands apotheosis paranoid 3 onlayer back at Position(ypos=1125)
                                                with Dissolve(0.5)
                                                $ renpy.pause(0.25)
                                                show hands apotheosis paranoid 4 onlayer back at Position(ypos=1125)
                                                with Dissolve(0.25)
                                                $ renpy.pause(0.125)
                                                show hands apotheosis paranoid 5 onlayer back at Position(ypos=1125)
                                                with Dissolve(0.25)
                                                $ renpy.pause(0.125)
                                                show hands apotheosis paranoid 6 onlayer back at Position(ypos=1125)
                                                with Dissolve(0.25)
                                                $ renpy.pause(0.125)
                                                hide hands onlayer back
                                                with Dissolve(0.25)
                                                $ renpy.pause(0.125)
                                                $ blade_held = False
                                                $ default_mouse = "default"
                                                stop music
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
                                                hide quiet onlayer farback
                                                hide quiet onlayer front
                                                show farback quiet onlayer farback at Position(ypos=1125)
                                                with Dissolve(4.0)
                                                show mirror quiet distant onlayer back at Position(ypos=1125)
                                                if loops_finished != 0:
                                                    truth "But you do not get the chance to respond, nor will you ever. It's time to leave. Memory returns.\n"
                                                else:
                                                    truth "But you do not get the chance to respond, nor will you ever. Something has taken her away, and it's left something else in her place.\n"
                                                $ achievement.grant("ACH_APOTH_THREADS")
                                                $ trait_broken = False
                                                $ trait_paranoid = False
                                                $ apotheosis_end = "unraveled"
                                                $ princess_deny += 1
                                                $ princess_kept += 1
                                                menu:

                                                    "{i}• [[Approach the mirror.]{/i}":
                                                        hide mirror onlayer back
                                                        show content m empty onlayer front at Position(ypos=1125)
                                                        show mirror frame onlayer front at Position(ypos=1125)
                                                        with Dissolve(2.0)
                                                        truth "Silence as you approach.\n"
                                                        menu:

                                                            extend ""

                                                            "{i}• [[Gaze into your reflection.]{/i}":
                                                                jump mirror_n_gaze_join
                                                # END

                                        "{i}• [[Submit.]{/i}":
                                            voice "audio/_pristine/voice/apotheosis/princess/41.flac"
                                            sp "Finally you have seen my light. All is forgiven.\n"
                                            jump apotheosis_alone_final_join






        "{i}• [[Embrace your new goddess.]{/i}":
            jump apotheosis_pristine_freedom
