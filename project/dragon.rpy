label spectre_pristine_start:

    $ trait_opportunist = True
    $ trait_cold = True

    play tertiary "audio/final/Spectre_PossessingPlayer_7.flac"
    play audio "audio/final/Adversary_StabCut_1.flac"
    show player spectre exorcism 1 onlayer front at shakeshort
    with dissolve
    voice "audio/_pristine/voice/extras/narrator/2.flac"
    n "The Princess, her spirit bound to your prison of flesh as she had once been bound to the basement's prison of stone, cries out in agony as you slice through organ and muscle.\n"
    if spectre_hostile:
        #voice "audio/_pristine/voice/extras/spectre_princess/h1.flac"
        #spmid "Did you really just let me in here so you could stab me again?!\n"
        play audio "audio/final/Spectre_PossessingPlayer_1.flac"
        voice "audio/voices/ch2/spectre/_encounter/princess/114.flac"
        show player spectre exorcism 2 onlayer front
        with dissolve
        spmid "NO!\n"
    else:
        voice "audio/_pristine/voice/extras/spectre_princess/s2a.flac"
        #pmid "I thought you finally understood me but instead you just wanted to hurt me again.\n"
        play audio "audio/final/Spectre_PossessingPlayer_1.flac"
        show player spectre exorcism 2 onlayer front
        with dissolve
        pmid "I don't want to die in you! I thought you finally understood me but instead you just wanted to hurt me again.\n"
    voice "audio/_pristine/voice/extras/narrator/3.flac"
    play audio "audio/one_shot/hard tighten.flac"
    show player spectre exorcism 3 onlayer front
    with Dissolve(0.5)
    n "Your skin roils and bucks as she violently pushes against it from the inside. Bits of her seep through, white and glowing with ethereal light, but still the walls of your prison hold.\n"
    if spectre_hostile:
        voice "audio/_pristine/voice/extras/spectre_princess/h2.flac"
        play audio "audio/final/Adversary_PowerfulFingersDiggingSkull_2.flac"
        show player spectre exorcism 4 onlayer front
        with Dissolve(0.5)
        spmid "Who do you think you are, trying to take me out with you?! Well I'll show you. I can do worse than that little knife. It's not you taking me out, it's me taking you out. I'll tear this body to shreds!\n"
        voice "audio/_pristine/voice/extras/cold/1.flac"
        cold "Wouldn't that be interesting? I'd like to see you try. But I think this is the end for all of us.\n"
    else:
        voice "audio/_pristine/voice/extras/spectre_princess/s3.flac"
        play audio "audio/final/Adversary_PowerfulFingersDiggingSkull_2.flac"
        show player spectre exorcism 4 onlayer front
        with Dissolve(0.5)
        pmid "If only I could drag you with me and make you understand. But that's not the way things get to go for me, is it?\n"
        voice "audio/_pristine/voice/extras/cold/2.flac"
        cold "It would certainly be interesting. Though being dead does sound dull. And you are about to be dead. Again.\n"
    if spectre_hostile:
        voice "audio/_pristine/voice/extras/spectre_princess/h3.flac"
        play audio "audio/one_shot/collapse.flac"
        play secondary "audio/final/Nightmare_MaleBreath_1.flac"
        hide player onlayer front
        hide table onlayer back
        hide farback onlayer farback
        hide bg onlayer back
        hide farback onlayer back
        hide spectre onlayer inyourface
        show bg spectre exorcism collapse onlayer back at swayblur, Position(ypos=1125)
        show spectre exorcism collapse overlay onlayer inyourface at Position(ypos=1125)
        with Dissolve(1.0)
        spmid "I said I'm leaving, you cold little freak!\n"
    else:
        voice "audio/_pristine/voice/extras/spectre_princess/s4.flac"
        play audio "audio/one_shot/collapse.flac"
        play secondary "audio/final/Nightmare_MaleBreath_1.flac"
        hide player onlayer front
        hide table onlayer back
        hide farback onlayer farback
        hide bg onlayer back
        hide farback onlayer back
        hide spectre onlayer inyourface
        show bg spectre exorcism collapse onlayer back at swayblur, Position(ypos=1125)
        show spectre exorcism collapse overlay onlayer inyourface at Position(ypos=1125)
        with Dissolve(1.0)
        spmid "Get away from me, you cold little freak!\n"

    # opportunist - killed in basement
    # contrarian - killed upstairs

    $ achievement.grant("ACH_SPECTRE_EXORCIST")
    $ gallery_spectre.unlock_item(11)
    $ gallery_spectre.unlock_item(12)
    $ renpy.save_persistent()
    stop music
    stop secondary
    stop sound
    stop tertiary
    #play audio "audio/final/Assorted_TapestyUnraveledBreakingRip_1.flac"
    #play sound "audio/final/Spectre_PossessingPlayer_5.flac"
    play sound "audio/_pristine/sfx/Dragon Soul Transfer_1.flac"
    default dragon_silent_count = 0
    default dragon_alliance_statement = False
    default dragon_apologize = False
    default dragon_hands_observe = False
    default dragon_look_like = False

    hide bg onlayer back
    hide spectre onlayer inyourface
    scene bg black
    $ blade_held = False
    $ default_mouse = "princess"

    if spectre_hostile:
        truthmid "You feel a violent tear, like the shape that you thought was you was never really a single shape to begin with. Something in the space you occupy has decided to leave, and it has brought you with it.\n"
    else:
        truthmid "You feel a dull tear, like strips of meat being delicately peeled from bone. But it doesn't matter how delicate the hands if you are the meat.\n"
    truthmid "You have been stripped away from yourself. Or stripped away from something that used to be you. Or stripped away from something that used to be important. At the very least, you have been stripped away from something.\n"
    truthmid "It always hurts to forget at first, but then you forget the pain.\n"

    $ blade_held = False
    $ default_mouse = "princess"

    play secondary "audio/final/fury_heart_loop.ogg" loop
    if spectre_hostile:
        voice "audio/_pristine/voice/dragon/princess_harsh/inside/1.flac"
        spmid "Do you think we're done, you self-destructive murderer?!\n"
    else:
        voice "audio/_pristine/voice/dragon/princess_soft/inside/1a.flac"
        pmid "We were so close to leaving and now look at you! Look at me! Is this what you wanted?\n"

    $ gallery_dragon.unlock_item(1)
    $ renpy.save_persistent()
    play sound "audio/final/Assorted_OppressiveBG_loop.flac" fadein 3.0 loop
    show bg dragon start onlayer farback at bigswayblur, Position(ypos=1125)
    show dragon start onlayer back at bigswayblur, Position(ypos=1125)
    with fade
    truthmid "The words come from both inside and outside of your head. Before you on the ground is a writhing mass of flesh and scales and feathers.\n"

    menu:
        extend ""

        "{i} Is that me?! Is that what I look like?{/i}":
            if spectre_hostile:
                voice "audio/_pristine/voice/dragon/princess_harsh/inside/2.flac"
                swp "Oh. {i}You're{/i} here. Great, maybe you'll finally get to feel what it's like to be me.\n"
                voice "audio/_pristine/voice/dragon/princess_harsh/inside/3.flac"
                swp "And yeah, that's 'you.' Or what's left of you. What an ugly sight.\n"
            else:
                voice "audio/_pristine/voice/dragon/princess_soft/inside/2.flac"
                wp "Oh! You're here, too.\n"
                voice "audio/_pristine/voice/dragon/princess_soft/inside/3.flac"
                wp "Maybe... trying to slay me was for the best, if it means you could leave those other voices behind. The two mean ones, at least. I feel kind of bad for the nice one.\n"
                voice "audio/_pristine/voice/dragon/princess_soft/inside/4.flac"
                wp "But we probably shouldn't think about them too much right now. They're a mess, and I don't think we can fix them. No point in worrying over messes that can't be fixed.\n"

        "{i} This isn't what I wanted to do.{/i}":
            if spectre_hostile:
                voice "audio/_pristine/voice/dragon/princess_harsh/inside/4.flac"
                swp "Oh. You're here, too. Well, we all have to face consequences for our actions, unintended or not. Sometimes we even face consequences for doing nothing at all.\n"
                voice "audio/_pristine/voice/dragon/princess_harsh/inside/5.flac"
                swp "Like me, when you came downstairs and stabbed me in the heart. What had I done to deserve that? Then you went and stabbed yourself in the heart just to spite me... I should have seen that one coming, really. But hey. Now we're here. Stuck together.\n"
                voice "audio/_pristine/voice/dragon/princess_harsh/inside/6.flac"
                swp "That's consequences for you.\n"
            else:
                voice "audio/_pristine/voice/dragon/princess_soft/inside/5.flac"
                wp "Oh! You're here! I thought I was going to be alone again.\n"
                voice "audio/_pristine/voice/dragon/princess_soft/inside/6.flac"
                wp "Maybe... this is for the best. Maybe if we left together in that body something horrible would have happened to us. Maybe this is how we're supposed to be.\n"
                voice "audio/_pristine/voice/dragon/princess_soft/inside/7.flac"
                wp "I hope... the part of you that decided to stab us isn't the part of you that's with me. I don't really want to get stabbed a third time.\n"

        "{i} Did you mean to take me with you?{/i}":
            if spectre_hostile:
                voice "audio/_pristine/voice/dragon/princess_harsh/inside/7.flac"
                swp "Oh. {i}You're{/i} here. Great.\n"
                voice "audio/_pristine/voice/dragon/princess_harsh/inside/8.flac"
                swp "All I meant to do was leave. What happened to you and where you wound up wasn't exactly a top concern.\n" id spectre_pristine_start_aa960a37
                voice "audio/_pristine/voice/dragon/princess_harsh/inside/9.flac"
                swp "At least it seems like it's just you. Those other ones were unbearable, especially that murder-happy know-it-all.\n"
            else:
                voice "audio/_pristine/voice/dragon/princess_soft/inside/8.flac"
                wp "Oh! You're here! I thought I was going to be alone again.\n"
                voice "audio/_pristine/voice/dragon/princess_soft/inside/9.flac"
                wp "I didn't mean to bring you with me. I'm happy I only seem to have brought you... that's not nice of me to say, they weren't all bad, but they were definitely mostly bad.\n"
                voice "audio/_pristine/voice/dragon/princess_soft/inside/10a.flac"
                wp "Maybe... this means things between us can get better. Maybe everything that went wrong just came from them. I hope. Because I really wouldn't like to be stabbed a third time.\n"

        "{i} Can anyone hear me?{/i}":
            if spectre_hostile:
                voice "audio/_pristine/voice/dragon/princess_harsh/inside/10.flac"
                swp "Oh, wonderful. {i}You're{/i} here.\n"
                voice "audio/_pristine/voice/dragon/princess_harsh/inside/9.flac"
                swp "At least it seems like it's just you. Those other ones were unbearable, especially that murder-happy know-it-all.\n"
            else:
                voice "audio/_pristine/voice/dragon/princess_soft/inside/11.flac"
                wp "I can hear you! So... you left with me?\n"
                voice "audio/_pristine/voice/dragon/princess_soft/inside/12a.flac"
                wp "And it sounds like it's just the two of us now. I hope that means things are going to be better, even if we're still stuck. Maybe everything that was bad between us just came from them.\n"
                voice "audio/_pristine/voice/dragon/princess_soft/inside/13.flac"
                wp "I hope. Because I really wouldn't like to be stabbed a third time.\n"

        "{i} [[Say nothing.]{/i}":
            if spectre_hostile:
                voice "audio/_pristine/voice/dragon/princess_harsh/inside/11.flac"
                swp "'Say nothing...?' Was that... you? Great. So you hitched a ride.\n"
                voice "audio/_pristine/voice/dragon/princess_harsh/inside/9.flac"
                swp "At least it seems like it's just you. Those other ones were unbearable, especially that murder-happy know-it-all.\n" id spectre_pristine_start_72e84e3f
            else:
                voice "audio/_pristine/voice/dragon/princess_soft/inside/14.flac"
                wp "'Say nothing...?' that's you, isn't it? So you left with me. I'm not alone.\n"
                voice "audio/_pristine/voice/dragon/princess_soft/inside/12a.flac"
                wp "And it sounds like it's just the two of us now. I hope that means things are going to be better, even if we're still stuck. Maybe everything that was bad between us just came from them.\n"

    if spectre_hostile:
        voice "audio/_pristine/voice/dragon/princess_harsh/inside/12a.flac"
        swp "I'm willing to pretend that you didn't just stab yourself to spite me. But don't think I've forgotten a thing. This is an alliance of convenience.\n"


    truthmid "Gurgling liquid bubbles up from open pockets in the disintegrating mass in front of you. It is trying to speak, but it no longer has the tissue that speech requires.\n"

    if spectre_hostile:
        voice "audio/_pristine/voice/dragon/princess_harsh/inside/13.flac"
        swp "Wait maybe this still counts as leaving together. Come on, lets get the hell out of here!\n"
    else:
        voice "audio/_pristine/voice/dragon/princess_soft/inside/15.flac"
        wp "Wait, if we need to leave together to get out, this could still count. We have to try! Before your, um body stops being alive.\n"

    menu:
        extend ""
        "{i} But what about the body? What about... me?{/i}":
            if spectre_hostile:
                voice "audio/_pristine/voice/dragon/princess_harsh/inside/14.flac"
                swp "What about it? It's dying. And filled with the worst parts of you. Let's just go-\n{w=4.8}{nw}"
                show screen disableclick(0.5)
            else:
                voice "audio/_pristine/voice/dragon/princess_soft/inside/16.flac"
                wp "There's nothing we can do for it now. But we can still try to save {i}us{/i}. We just have to leave-\n{w=4.35}{nw}"
                show screen disableclick(0.5)

        "{i} Agreed. Let's go.{/i}":
            if spectre_hostile:
                voice "audio/_pristine/voice/dragon/princess_harsh/inside/15.flac"
                swp "I don't need your permission.\n"
            else:
                voice "audio/_pristine/voice/dragon/princess_soft/inside/17a.flac"
                wp "Okay. Okay. Yeah. Deep breath, Princess. Let's {i}go{/i}.\n"
            label dragon_start_flee_join:
                if spectre_upstairs:
                    play audio "audio/one_shot/footstep_run_medium.flac"
                    hide bg onlayer farback
                    hide dragon onlayer back
                    show bg dragon start upstairs 1 onlayer back at Position(ypos=1125)
                    with Dissolve(0.5)
                    truthmid "You hurtle towards the cabin door, but time seems to slow down the closer you get. In a moment, you're halfway there, and in two moments you're halfway there again. Halving the distance and halving the distance until the door feels almost within reach.\n"
                else:
                    play audio "audio/one_shot/footstep_run_medium.flac"
                    hide bg onlayer farback
                    hide dragon onlayer back
                    show bg dragon start downstairs 1 onlayer back at Position(ypos=1125)
                    with Dissolve(0.5)
                    truthmid "You hurtle towards the cabin stairs, but time seems to slow down the closer you get. In a moment, you're halfway there, and in two moments you're halfway there again. Halving the distance and halving the distance until the upstairs feels almost within reach.\n" id dragon_start_flee_join_a917159c
                if spectre_upstairs:
                    play audio "audio/one_shot/footstep_run_medium.flac"
                    show bg dragon start upstairs 2 onlayer back at Position(ypos=1125)
                    with Dissolve(0.5)
                else:
                    play audio "audio/one_shot/footstep_run_medium.flac"
                    show bg dragon start downstairs 2 onlayer back at Position(ypos=1125)
                    with Dissolve(0.5)
                if spectre_hostile:
                    voice "audio/_pristine/voice/dragon/princess_harsh/inside/16.flac"
                    swp "Come on, come on, come on! We're so clo-\n{w=2.65}{nw}"
                    show screen disableclick(0.5)
                else:
                    voice "audio/_pristine/voice/dragon/princess_soft/inside/18.flac"
                    wp "We're not gonna make it, are we? We're gonna be stuck again, we're-\n{w=2.62}{nw}"
                    show screen disableclick(0.5)

        "{i} If you leave the cabin, the world ends. I'm not going to be party to the end of everything!{/i}":
            if spectre_hostile:
                voice "audio/_pristine/voice/dragon/princess_harsh/inside/17.flac"
                swp "Are you kidding me? You don't actually believe that, do you? {i}Ugh{/i}. I'm not going to argue with you. We're leaving, now-\n{w=6.65}{nw}"
                show screen disableclick(0.5)
            else:
                voice "audio/_pristine/voice/dragon/princess_soft/inside/19.flac"
                wp "I don't want to end the world! But you can't keep me down here just because someone told you that might-\n{w=4.68}{nw}"
                show screen disableclick(0.5)

        "{i} Hell no! We're staying right here until we figure this out.{/i}":
            if spectre_hostile:
                voice "audio/_pristine/voice/dragon/princess_harsh/inside/18.flac"
                swp "I am NOT going to stick around arguing with you while that thing on the floor melts!\n"
                jump dragon_start_flee_join
            else:
                voice "audio/_pristine/voice/dragon/princess_soft/inside/20.flac"
                wp "I don't think there's anything for us to figure out down here. I think our only answers are out there. Come on, let's-\n{w=5.42}{nw}"
                show screen disableclick(0.5)

        "{i} Sorry I stabbed us.{/i}":
            $ dragon_apologize = True
            if spectre_hostile:
                voice "audio/_pristine/voice/dragon/princess_harsh/inside/19a.flac"
                swp "At least you're paying the price now. But how about we not waste time talking about what-\n{w=4.05}{nw}"
                show screen disableclick(0.5)
                #voice "audio/_pristine/voice/dragon/princess_harsh/inside/19.flac"
                #swp "At least you're paying the price now. But how about we not waste time talking about what just happened while that thing on the floor melts!\n"
                #jump dragon_start_flee_join
            else:
                voice "audio/_pristine/voice/dragon/princess_soft/inside/21.flac"
                wp "It's okay. I'm sure you had your reasons. But I think we have to leave now. Come on, let's-\n{w=3.98}{nw}"
                show screen disableclick(0.5)

        "{i} [[Say nothing.]{/i}":
            if spectre_hostile:
                voice "audio/_pristine/voice/dragon/princess_harsh/inside/20.flac"
                swp "Here we go.\n"
            else:
                voice "audio/_pristine/voice/dragon/princess_soft/inside/22.flac"
                wp "Okay. That's a yes.\n"

            jump dragon_start_flee_join

    $ gallery_dragon.unlock_item(2)
    $ gallery_dragon.unlock_gallery()
    $ renpy.save_persistent()
    $ current_princess = "dragon"
    hide bg onlayer back
    hide dragon onlayer back
    hide bg onlayer farback
    stop sound
    stop secondary
    show bg dragon true start onlayer back at Position(ypos=1125)
    truthmid "You are seated in a room that is empty. A chain digs into your wrist, binding one arm to the wall. It is quiet, and you are alone. This is what you deserve. This is what you deserve. This is what you deserve. This is what you deserve. This is what you deserve. This is what you deserve. This is what you deserve. This is what you deserve. This is what you deserve. This is what you deserve. This is what you deserve. This is what you deserve. This is what you deserve. This is what you deserve. This is what you deserve. This is what you deserve. This is what you deserve. This is what you deserve. This is what you deserve. This is what you deserve. This is what you deserve. This is what you deserve. This is what you deserve.\n"
    play music "audio/_pristine/music/dragon/The Princess and the Dragon Intro.flac"
    queue music "audio/_pristine/music/dragon/The Princess and the Dragon Loop.flac" loop
    if spectre_hostile:
        #voice "audio/_pristine/voice/dragon/princess_harsh/inside/21.flac"
        #swp "Well? Are you still there? We need to get out of here.\n"
        voice "audio/_pristine/voice/dragon/princess_harsh/inside/21a.flac"
        swp "Well? Are you still there?\n"
    else:
        voice "audio/_pristine/voice/dragon/princess_soft/inside/23.flac"
        wp "Are you still there? Am I alone again?\n"

label dragon_start_menu:
    default dragon_start_count = 0
    default dragon_what_happened = False
    default dragon_intro_explore = False
    default dragon_still_mad = False
    default dragon_tone_different = False
    default dragon_title_card = False
    default dragon_wait_first_explore = False
    default dragon_how_leave = False
    default dragon_where_others = False
    default dragon_ghost_explore = False
    default dragon_second_wait = False
    menu:
        extend ""

        "{i} (Explore) There has to be something for us to do other than wait.{/i}" if dragon_loop_joke_count != 0 or dragon_wait_attempt:
            default dragon_loop_joke_count = 0
            $ dragon_start_count += 1
            $ dragon_loop_joke_count += 1
            if dragon_loop_joke_count == 1:
                if spectre_hostile:
                    voice "audio/_pristine/voice/dragon/princess_harsh/inside/60.flac"
                    swp "You have any better ideas?\n"
                else:
                    voice "audio/_pristine/voice/dragon/princess_soft/inside/51.flac"
                    wp "Well, that's what I've always done.\n"
            elif dragon_loop_joke_count == 2:
                if spectre_hostile:
                    voice "audio/_pristine/voice/dragon/princess_harsh/inside/61a.flac"
                    swp "You already said that.\n" id dragon_start_menu_651185b4
                else:
                    voice "audio/_pristine/voice/dragon/princess_soft/inside/52.flac"
                    wp "I already told you I don't have any ideas. I... did tell you that, right? Sorry if I didn't.\n"
            elif dragon_loop_joke_count == 3:
                if spectre_hostile:
                    voice "audio/_pristine/voice/dragon/princess_harsh/inside/62.flac"
                    swp "Oh, no. Please don't make us loop on this.\n"
                else:
                    voice "audio/_pristine/voice/dragon/princess_soft/inside/53.flac"
                    wp "Um... you're kind of a broken record right now. Are you okay?\n"
            elif dragon_loop_joke_count == 4:
                if spectre_hostile:
                    voice "audio/_pristine/voice/dragon/princess_harsh/inside/63.flac"
                    swp "I'm just gonna stop talking until you fix whatever this is.\n"
                else:
                    voice "audio/_pristine/voice/dragon/princess_soft/inside/54.flac"
                    wp "Maybe... maybe if I stop answering you, you'll say something else.\n"

            elif dragon_loop_joke_count == 4:
                if spectre_hostile:
                    voice "audio/_pristine/voice/dragon/princess_harsh/inside/64.flac"
                    swp "Nope.\n"
                else:
                    voice "audio/_pristine/voice/dragon/princess_soft/inside/55.flac"
                    wp "{i}Distracted humming{/i}.\n"
            else:
                $ achievement.grant("ACH_DRAGON_LOOP")
                if spectre_hostile:
                    voice "audio/_pristine/voice/dragon/princess_harsh/inside/65.flac"
                    swp "...\n"
                else:
                    voice "audio/_pristine/voice/dragon/princess_soft/inside/56.flac"
                    wp "...\n"
            jump dragon_start_menu

        "{i} (Explore) I'm still here.{/i}" if dragon_start_count == 0 and dragon_intro_explore == False:
            $ dragon_intro_explore = True
            $ dragon_start_count += 1
            if spectre_hostile:
                voice "audio/_pristine/voice/dragon/princess_harsh/inside/24.flac"
                swp "Well, that's something. I guess we're really stuck together then.\n"
            else:
                voice "audio/_pristine/voice/dragon/princess_soft/inside/27.flac"
                wp "Then at least I won't be lonely. It's nice to hear your voice. I mean... think your voice?\n"
            jump dragon_start_menu

        "{i} (Explore) What just happened?{/i}" if dragon_start_count == 0 and dragon_what_happened == False:
            label dragon_what_happened_join:
                $ dragon_what_happened = True
                $ dragon_start_count += 1
                if dragon_intro_explore == False and dragon_start_count == 0:
                    $ dragon_intro_explore = True
                    if spectre_hostile:
                        voice "audio/_pristine/voice/dragon/princess_harsh/inside/ack.flac"
                        swp "I guess we're really stuck together then.\n"
                    else:
                        voice "audio/_pristine/voice/dragon/princess_harsh/inside/ack.flac"
                        swp "It's nice to hear your voice. I mean... think? your voice?\n"
                if spectre_hostile:
                    if spectre_death_shared:
                        voice "audio/_pristine/voice/dragon/princess_harsh/inside/22.flac"
                        swp "You died, probably. And we're back where I started.\n"
                    else:
                        voice "audio/_pristine/voice/dragon/princess_harsh/inside/23.flac"
                        swp "We're back where I started.\n"
                    #voice "audio/_pristine/voice/dragon/princess_harsh/inside/23.flac"
                    #swp "This is what happened to me last time.\n"
                else:
                    if spectre_death_shared:
                        voice "audio/_pristine/voice/dragon/princess_soft/inside/24.flac"
                        wp "I think you died... or... the body on the floor died. Sorry.\n"
                    else:
                        voice "audio/_pristine/voice/dragon/princess_soft/inside/25.flac"
                        wp "We're back at the beginning. My beginning.\n"
                    voice "audio/_pristine/voice/dragon/princess_soft/inside/26.flac"
                    wp "This is what happened to me last time.\n"
                jump dragon_start_menu

        "{i} (Explore) You're not mad at me, are you?{/i}" if dragon_still_mad == False and dragon_tone_different == False:
            $ dragon_start_count += 1
            $ dragon_still_mad = True
            if dragon_intro_explore == False and dragon_start_count == 0:
                $ dragon_intro_explore = True
                if spectre_hostile:
                    voice "audio/_pristine/voice/dragon/princess_harsh/inside/ack.flac"
                    swp "I guess we're really stuck together then.\n"
                else:
                    voice "audio/_pristine/voice/dragon/princess_harsh/inside/ack.flac"
                    swp "It's nice to hear your voice. I mean... think? your voice?\n"
            if spectre_hostile:
                voice "audio/_pristine/voice/dragon/princess_harsh/inside/bonus1a.flac"
                swp "Like I said, we have an alliance of convenience right now. I wouldn't poke too hard at the edges of that.\n"
            else:
                voice "audio/_pristine/voice/dragon/princess_soft/inside/bonus1.flac"
                wp "I don't know why you did what you did, but it's hard to be mad when you're just as stuck as I am.\n"
            jump dragon_start_menu

        "{i} (Explore) You're different. Your whole mood is different.{/i}" if dragon_start_count != 0 and dragon_tone_different == False:
            $ dragon_start_count += 1
            $ dragon_tone_different = True
            if dragon_intro_explore == False and dragon_start_count == 0:
                $ dragon_intro_explore = True
                if spectre_hostile:
                    voice "audio/_pristine/voice/dragon/princess_harsh/inside/ack.flac"
                    swp "I guess we're really stuck together then.\n"
                else:
                    voice "audio/_pristine/voice/dragon/princess_harsh/inside/ack.flac"
                    swp "It's nice to hear your voice. I mean... think? your voice?\n"
            if spectre_hostile:
                if dragon_still_mad:
                    voice "audio/_pristine/voice/dragon/princess_harsh/inside/bonus2start.flac"
                    swp "Poking at the edges when I specifically told you not to? {i}Sigh{/i}.\n"
                voice "audio/_pristine/voice/dragon/princess_harsh/inside/bonus2cont.flac"
                swp "We're both stuck here and everything's started over. How about we both just try and make the best of it, okay?\n"
                voice "audio/_pristine/voice/dragon/princess_harsh/inside/bonus3a.flac"
                swp "Besides, there's something about you being in here with me that just feels... right. It's hard to stay mad at you like this.\n"
                #voice "audio/_pristine/voice/dragon/princess_harsh/inside/bonus3.flac"
                #swp "Besides, there's something about you being in here that just feels... right. It's hard to stay mad at you like this. Even if I wanted to be mad at you, the feeling just isn't coming the way I want it to come.\n"
            else:
                voice "audio/_pristine/voice/dragon/princess_soft/inside/bonus2.flac"
                wp "I'm just trying to make the best of things... you could always make the best of things too, if you want. We both have a chance to start over.\n"
                voice "audio/_pristine/voice/dragon/princess_soft/inside/bonus3.flac"
                wp "Besides, there's something about you being in here with me that feels... right. I never wanted to be your enemy.\n"
            menu:
                extend ""

                "{i} I killed you, though. And I tried killing you again.{/i}":
                    if spectre_hostile:
                        voice "audio/_pristine/voice/dragon/princess_harsh/inside/bonus4.flac"
                        swp "You really want me to be mad at you, don't you? Too bad, I guess. For both of us.\n"
                    else:
                        voice "audio/_pristine/voice/dragon/princess_soft/inside/bonus4.flac"
                        wp "I don't know what to say. I just... feel fine right now. I think things happen for a reason, and if you trying to kill both of us is what it takes for you to finally see what I see... then I'm okay with that.\n"
                    jump dragon_start_menu

                "{i} [[Let it go, just like she has.]{/i}":
                    jump dragon_start_menu

        "{i} (Explore) Sorry I stabbed us.{/i}" if dragon_apologize == False:
            $ dragon_start_count += 1
            $ dragon_apologize = True
            if spectre_hostile:
                voice "audio/_pristine/voice/dragon/princess_harsh/inside/25.flac"
                swp "Well, I guess you're paying the price for it, aren't you?\n"
                swp "...\n"
                voice "audio/_pristine/voice/dragon/princess_harsh/inside/26.flac"
                swp "Let's just call it even for now.\n"
            else:
                voice "audio/_pristine/voice/dragon/princess_soft/inside/28.flac"
                wp "That's okay. I'm sure you had your reasons. I don't think it's good to hold on to the past like that, anyways. It's better if we choose to move forward together.\n"
            jump dragon_start_menu

        "{i} (Explore) How are we supposed to get out of here?{/i}" if dragon_how_leave == False and dragon_start_count != 1:
            $ dragon_how_leave = True
            $ dragon_start_count += 1
            if spectre_hostile:
                voice "audio/_pristine/voice/dragon/princess_harsh/inside/54.flac"
                swp "Hahaha. Are you seriously asking ME that? I've been stuck here for as long as you've known me. I don't think the two of us would be here right now if I knew how to leave.\n"
            else:
                voice "audio/_pristine/voice/dragon/princess_soft/inside/47.flac"
                wp "I wish I knew! But I think we're probably stuck here until something happens.\n"
            jump dragon_start_menu

        "{i} (Explore) If we're both here, then what happened to the others?{/i}" if dragon_where_others == False:
            $ dragon_where_others = True
            $ dragon_start_count += 1
            if spectre_hostile:
                voice "audio/_pristine/voice/dragon/princess_harsh/inside/55.flac"
                swp "There's four walls around us, and a chain around my wrist. How am I supposed to know about anything that isn't right in front of me?\n"
                voice "audio/_pristine/voice/dragon/princess_harsh/inside/56.flac"
                swp "Maybe they're gone. I guess we'll just have to wait and see.\n"
                voice "audio/_pristine/voice/dragon/princess_harsh/inside/57.flac"
                swp "And if nobody comes by... well, I guess we'll be waiting a long, long time.\n"
            else:
                voice "audio/_pristine/voice/dragon/princess_soft/inside/48.flac"
                wp "I don't know! I hope they're okay. Uh... some of them, at least. I didn't like the one that kept bossing you around. And that quiet one kind of gave me the creeps.\n"
                voice "audio/_pristine/voice/dragon/princess_soft/inside/49.flac"
                wp "I liked that last one, though. He was nice. I hope he's okay.\n"
            jump dragon_start_menu

        "{i} (Explore) Are we still a ghost?{/i}" if dragon_ghost_explore == False:
            $ dragon_ghost_explore = True
            $ dragon_start_count += 1
            $ dragon_hands_observe = True
            if dragon_intro_explore == False and dragon_start_count == 0:
                $ dragon_intro_explore = True
                if spectre_hostile:
                    voice "audio/_pristine/voice/dragon/princess_harsh/inside/ack.flac"
                    swp "I guess we're really stuck together then.\n"
                else:
                    voice "audio/_pristine/voice/dragon/princess_harsh/inside/ack.flac"
                    swp "It's nice to hear your voice. I mean... think? your voice?\n"
            $ gallery_dragon.unlock_item(3)
            $ renpy.save_persistent()
            play audio "audio/final/Spectre_PossessingPlayer_7.flac"
            hide bg onlayer back
            show bg dragon hands flicker onlayer back at Position(ypos=1125)
            show dragon hands flicker onlayer front at Position(ypos=1125)
            with dissolve
            truthmid "Your gaze turns to your hands. Solid. Then translucent. Then solid again.\n"
            if spectre_hostile:
                voice "audio/_pristine/voice/dragon/princess_harsh/inside/58.flac"
                swp "Huh. I don't know. It's like we're one and then the other.\n"
                voice "audio/_pristine/voice/dragon/princess_harsh/inside/59.flac"
                swp "Ugh. Make up your mind already, body, will you?\n"
            else:
                voice "audio/_pristine/voice/dragon/princess_soft/inside/50.flac"
                wp "Maybe? It's like sometimes we are and sometimes we aren't. Like we're something in between ghost and... not-ghost.\n"
            hide bg onlayer back
            hide dragon onlayer front
            show bg dragon true start onlayer back at Position(ypos=1125)
            with dissolve
            jump dragon_start_menu

        "{i} (Explore) So what are we supposed to do? Just wait for something to happen?{/i}" if dragon_loop_joke_count == 0 and dragon_wait_first_explore:
            jump dragon_start_wait_join

        "{i} (Explore) What are we supposed to do? Just wait for something to happen?{/i}" if dragon_loop_joke_count == 0 and dragon_wait_first_explore == False:
            label dragon_start_wait_join:
                $ dragon_start_count += 1
                $ dragon_wait_first_explore = True
                $ dragon_loop_joke_count += 1
                if spectre_hostile:
                    voice "audio/_pristine/voice/dragon/princess_harsh/inside/60.flac"
                    swp "You have any better ideas?\n"
                else:
                    voice "audio/_pristine/voice/dragon/princess_soft/inside/51.flac"
                    wp "Well, that's what I've always done.\n"
                jump dragon_start_menu

        "{i} (Explore) What happened to us? What happened to everything?{/i}" if dragon_start_count != 0 and dragon_what_happened == False:
            jump dragon_what_happened_join

        "{i} (Explore) [[Wait.]{/i}" if dragon_second_wait == False:
            default dragon_wait_attempt = False
            $ dragon_wait_attempt = True
            $ dragon_start_count += 1
            truthmid "Time passes. You are still here.\n"
            if dragon_start_count == 0:
                if spectre_hostile:
                    voice "audio/_pristine/voice/dragon/princess_harsh/inside/67.flac"
                    swp "I don't think the silent treatment's going to work. I can... feel? You choosing to wait.\n"
                else:
                    voice "audio/_pristine/voice/dragon/princess_soft/inside/58.flac"
                    wp "So you are there. You're just... choosing not to say anything. Okay. Then I guess we're waiting here.\n"
            else:
                $ dragon_second_wait = True
                if spectre_hostile:
                    voice "audio/_pristine/voice/dragon/princess_harsh/inside/68.flac"
                    swp "Huh. Did the rest of you get lost?\n"
                else:
                    voice "audio/_pristine/voice/dragon/princess_soft/inside/59a.flac"
                    wp "Waiting has always worked for me before. But... nothing's still happening. Maybe we just have to wait some more.\n"
                jump dragon_start_menu

        "{i} (Explore) [[Say nothing.]{/i}" if dragon_start_count == 0:
            $ dragon_start_count += 1
            if spectre_hostile:
                voice "audio/_pristine/voice/dragon/princess_harsh/inside/69.flac"
                swp "I don't think the silent treatment's going to work. I can... feel? You choosing not to say anything.\n"
            else:
                voice "audio/_pristine/voice/dragon/princess_soft/inside/60.flac"
                wp "So you are there. You're just... choosing not to say anything. Okay.\n"
            jump dragon_start_menu

        "{i} This isn't what it was like the last time I died. The last time I died, I got a title card.{/i}" if dragon_what_happened and dragon_title_card == False:
            $ dragon_start_count += 1
            if spectre_hostile:
                voice "audio/_pristine/voice/dragon/princess_harsh/inside/27.flac"
                swp "That's weird. And isn't how it works for me. But if you want, I guess I can humor you. What do these 'title cards' look like?\n"
            else:
                voice "audio/_pristine/voice/dragon/princess_soft/inside/29.flac"
                wp "I've never gotten a title card. What did yours say?\n"
            label dragon_title_card_menu:
                default dragon_title_card_shared = False
                default dragon_title_card_laugh_promise = False
                default dragon_title_card_no_laugh_exp = False
                menu:

                    extend ""

                    "{i} (Explore) No, this is stupid, you're going to laugh at me.{/i}" if dragon_title_card_no_laugh_exp == False:
                        $ dragon_title_card_no_laugh_exp = True
                        if spectre_hostile:
                            voice "audio/_pristine/voice/dragon/princess_harsh/inside/28.flac"
                            swp "Whether I laugh at you depends on the title. I'm not going to make any promises I can't keep. {i}I{/i} don't lie.\n"
                        else:
                            $ dragon_title_card_laugh_promise = True
                            voice "audio/_pristine/voice/dragon/princess_soft/inside/30.flac"
                            wp "No I wont! I promise! I want to know what it's like to be you.\n"
                        jump dragon_title_card_menu

                    "{i} (Explore) If I'm going to tell you, you have to {b}promise{/b} you won't laugh at me.{/i}" if dragon_title_card_no_laugh_exp and spectre_hostile and dragon_title_card_laugh_promise == False:
                        $ dragon_title_card_laugh_promise = True
                        voice "audio/_pristine/voice/dragon/princess_harsh/inside/29.flac"
                        swp "{i}Sigh{/i}. Okay. Fine. I promise I won't laugh at you. Now tell me. I wanna know.\n"
                        jump dragon_title_card_menu

                    "{i} The first one I got said 'Chapter I: The Hero and the Princess,' and then after we both died, I got 'Chapter II: The Spectre.'{/i}":
                        $ dragon_title_card_shared = True
                        if spectre_hostile:
                            if dragon_title_card_laugh_promise:
                                voice "audio/_pristine/voice/dragon/princess_harsh/inside/30.flac"
                                swp "{i}Giggling{/i}. Okay. Sorry. Sorry.\n"
                            else:
                                voice "audio/_pristine/voice/dragon/princess_harsh/inside/31.flac"
                                swp "{i}Giggling{/i}. Some hero you turned out to be.\n"
                        else:
                            voice "audio/_pristine/voice/dragon/princess_soft/inside/31.flac"
                            wp "{i}Giggling{/i}. Well, the first one is sweet.\n"
                        menu:
                            extend ""

                            "{i} You promised you wouldn't laugh at me!{/i}" if dragon_title_card_laugh_promise:
                                label dragon_no_laugh_join:
                                    if spectre_hostile:
                                        voice "audio/_pristine/voice/dragon/princess_harsh/inside/32.flac"
                                        swp "I wasn't laughing {i}at{/i} you. I was laughing at...\n"
                                        menu:
                                            extend ""

                                            "{i} You were laughing at me.{/i}":
                                                voice "audio/_pristine/voice/dragon/princess_harsh/inside/33.flac"
                                                swp "Okay, maybe I was. A little. But this whole... setup is funny, really.\n"

                                            "{i} The futility of our lives?{/i}":
                                                voice "audio/_pristine/voice/dragon/princess_harsh/inside/34.flac"
                                                swp "Yes! This whole... setup is funny, really.\n"

                                            "{i} Mhm.{/i}":
                                                voice "audio/_pristine/voice/dragon/princess_harsh/inside/35.flac"
                                                swp "I was laughing at the whole situation!"

                                            "{i} [[Say nothing.]{/i}":
                                                voice "audio/_pristine/voice/dragon/princess_harsh/inside/35.flac"
                                                swp "I was laughing at the whole situation!"

                                        #if dragon_title_card_laugh_promise:
                                        #    voice "audio/_pristine/voice/dragon/princess_harsh/inside/36.flac"
                                        #    swp "It's a loophole, so it doesn't count. I remain a Princess of my word.\n"
                                        voice "audio/_pristine/voice/dragon/princess_harsh/inside/37.flac"
                                        swp "But really, it's like our lives are some cruel little play for someone else's entertainment.\n"
                                        #voice "audio/_pristine/voice/dragon/princess_harsh/inside/38.flac"
                                        #swp "...\n"
                                        voice "audio/_pristine/voice/dragon/princess_harsh/inside/39.flac"
                                        swp "I'm sorry! Okay?\n"
                                        #voice "audio/_pristine/voice/dragon/princess_harsh/inside/40.flac"
                                        swp "...\n"
                                        voice "audio/_pristine/voice/dragon/princess_harsh/inside/41.flac"
                                        stop music
                                        swp "Chapter III. The Princess and the Dragon.\n"

                                    else:
                                        voice "audio/_pristine/voice/dragon/princess_soft/inside/32.flac"
                                        wp "Look, it would have been {i}very{/i} sweet if things didn't turn out so... violent.\n"
                                        voice "audio/_pristine/voice/dragon/princess_soft/inside/33.flac"
                                        wp "But that doesn't mean that things can't get better from here.\n"
                                        voice "audio/_pristine/voice/dragon/princess_soft/inside/34.flac"
                                        wp "I think we need a new title card, though. How about...\n"
                                        voice "audio/_pristine/voice/dragon/princess_soft/inside/35.flac"
                                        stop music
                                        wp "Chapter III. The Princess and the Dragon.\n"

                                label princess_dragon_title_reveal:
                                    menu:

                                        extend ""

                                        "{i} Oooh. Reversing the order! I like it.{/i}":
                                            stop music
                                            if spectre_hostile:
                                                voice "audio/_pristine/voice/dragon/princess_harsh/inside/42.flac"
                                                swp "Well, this is my story, isn't it? Especially if you're here watching it.\n"
                                            else:
                                                voice "audio/_pristine/voice/dragon/princess_soft/inside/36.flac"
                                                wp "Thanks! I thought it would be fun.\n"

                                        "{i} Casting yourself as the main character, I see. Very humble.{/i}":
                                            stop music
                                            if spectre_hostile:
                                                if dragon_title_card_shared:
                                                    voice "audio/_pristine/voice/dragon/princess_harsh/inside/43.flac"
                                                    swp "You're one to talk, 'hero.'\n"
                                                else:
                                                    voice "audio/_pristine/voice/dragon/princess_harsh/inside/44.flac"
                                                    swp "Yeah. I'm sure you didn't get top billing in yours.\n"
                                            else:
                                                voice "audio/_pristine/voice/dragon/princess_soft/inside/37.flac"
                                                wp "I don't think Princesses are supposed to be humble! I'm royalty, aren't I?\n"

                                        "{i} The Princess and the {b}Dragon{/b}? I thought I was maybe some sort of... bird?{/i}":
                                            stop music
                                            if spectre_hostile:
                                                voice "audio/_pristine/voice/dragon/princess_harsh/inside/45.flac"
                                                swp "I like to think of you as a dragon. It's close enough.\n"
                                            else:
                                                voice "audio/_pristine/voice/dragon/princess_soft/inside/38.flac"
                                                wp "Well, they're... similar... right?\n"

                                        "{i} Wait, am I a dragon? Hell yeah!{/i}":
                                            stop music
                                            if spectre_hostile:
                                                $ dragon_look_like = True
                                                voice "audio/_pristine/voice/dragon/princess_harsh/inside/46.flac"
                                                swp "Dragons are {i}monsters{/i}, you know. {i}Sigh{/i}. But all right... whatever makes you happy.\n"
                                            else:
                                                voice "audio/_pristine/voice/dragon/princess_soft/inside/39.flac"
                                                wp "Does being called a dragon make you happy? You're... kind of scary looking. Like, {i}really{/i} scary looking.\n"

                                        "{i} I... don't actually know what I look like. Is that... accurate?{/i}":
                                            stop music
                                            $ dragon_look_like = True
                                            if spectre_hostile:
                                                voice "audio/_pristine/voice/dragon/princess_harsh/inside/47.flac"
                                                swp "I guess you'll have to wait and see what comes down those stairs.\n"
                                            else:
                                                voice "audio/_pristine/voice/dragon/princess_soft/inside/40.flac"
                                                wp "I think so? You're... kind of scary looking. Like, {i}really{/i} scary looking.\n"

                                        "{i} [[Say nothing.]{/i}":
                                            stop music
                                            if spectre_hostile:
                                                voice "audio/_pristine/voice/dragon/princess_harsh/inside/48.flac"
                                                swp "You're welcome, by the way.\n"
                                            else:
                                                voice "audio/_pristine/voice/dragon/princess_soft/inside/41.flac"
                                                wp "Yeah. That's a real good chapter title, Princess.\n"

                            "{i} Har har. Get your laughs out.{/i}":
                                jump dragon_no_laugh_join

                            "{i} I'm still a hero! I've been trying to save the world. You know, a villain to one person might be a hero to others.{/i}" if dragon_title_card_laugh_promise == False or spectre_hostile == False:
                                if spectre_hostile:
                                    voice "audio/_pristine/voice/dragon/princess_harsh/inside/49.flac"
                                    swp "Don't try and make this about shades of grey or whatever. I'm the only other person here with you, and you're the villain in my story.\n"
                                    voice "audio/_pristine/voice/dragon/princess_harsh/inside/50.flac"
                                    swp "I'm sorry. I'm being mean again. How about we wipe the slate clean with a new chapter? We could call it...\n"
                                    voice "audio/_pristine/voice/dragon/princess_harsh/inside/51.flac"
                                    stop music
                                    swp "Chapter III. The Princess and the Dragon.\n"
                                    jump princess_dragon_title_reveal
                                else:
                                    voice "audio/_pristine/voice/dragon/princess_soft/inside/42.flac"
                                    wp "Well, maybe you're just misguided. And the story's not over yet. We might still find a happy ending. But I think it's time we start a new chapter. Hmmm. How about...\n"
                                    voice "audio/_pristine/voice/dragon/princess_soft/inside/43.flac"
                                    stop music
                                    wp "Chapter III. The Princess and the Dragon.\n"
                                    jump princess_dragon_title_reveal

                            "{i} [[Say nothing.]{/i}":
                                if dragon_title_card_laugh_promise:
                                    jump dragon_no_laugh_join
                                else:
                                    jump dragon_title_avoid


                    "{i} Nevermind. Forget I said anything.{/i}":
                        jump dragon_title_avoid

                    "{i} [[Say nothing.]{/i}":
                        label dragon_title_avoid:
                            if spectre_hostile:
                                voice "audio/_pristine/voice/dragon/princess_harsh/inside/52.flac"
                                swp "Oh, you're no fun.\n"
                                voice "audio/_pristine/voice/dragon/princess_harsh/inside/53.flac"
                                swp "What is this? Our third go-round? Hm.\n"
                                voice "audio/_pristine/voice/dragon/princess_harsh/inside/51.flac"
                                stop music
                                swp "Chapter III: The Princess and the Dragon.\n"
                            else:
                                voice "audio/_pristine/voice/dragon/princess_soft/inside/44.flac"
                                wp "I'm sorry!\n"
                                voice "audio/_pristine/voice/dragon/princess_soft/inside/45.flac"
                                wp "This is our third time here, right? So that would make this chapter three.\n"
                                voice "audio/_pristine/voice/dragon/princess_soft/inside/46.flac"
                                stop music
                                wp "Chapter III: The Princess and the Dragon.\n"
                            jump princess_dragon_title_reveal

        "{i} Now that I think about it, both times I've been here nothing happened until after I saw a title card. We haven't seen a title card yet.{/i}" if dragon_loop_joke_count == 2 or dragon_second_wait:
            $ dragon_start_count += 1
            if spectre_hostile:
                voice "audio/_pristine/voice/dragon/princess_harsh/inside/66.flac"
                swp "A title card? What on earth are you talking about?\n"
            else:
                voice "audio/_pristine/voice/dragon/princess_soft/inside/57.flac"
                wp "You've gotten title cards? What did they say?\n"
            jump dragon_title_card_menu



label dragon_arrival:

    play audio "audio/_pristine/sfx/door_bedroom_suppressed.flac"
    play music "audio/_pristine/music/dragon/Life and Death Intro.flac"
    queue music "audio/_pristine/music/dragon/Life and Death Loop.flac"

    truthmid "The click of a latch and creaking hinges, muffled. Something is here.\n"
    $ gallery_dragon.unlock_item(3)
    $ renpy.save_persistent()
    if dragon_hands_observe == False:
        play audio "audio/final/Spectre_PossessingPlayer_7.flac"
        hide bg onlayer back
        show bg dragon hands flicker onlayer back at Position(ypos=1125)
        show dragon hands flicker onlayer front at Position(ypos=1125)
        with dissolve
        truthmid "Your gaze turns to your hands. Solid. Then translucent. Then solid again.\n"
        if spectre_hostile:
            voice "audio/_pristine/voice/dragon/princess_harsh/inside/70.flac"
            swp "Huh. I don't think 'you' know what we are. It's like we're one and then the other.\n"
            voice "audio/_pristine/voice/dragon/princess_harsh/inside/71.flac"
            swp "Ugh. Make up your mind already, body, will you?\n"
        else:
            voice "audio/_pristine/voice/dragon/princess_soft/inside/61.flac"
            wp "Huh. It's almost like 'you' don't know what we are. We keep changing.\n"
    else:
        if spectre_hostile:
            voice "audio/_pristine/voice/dragon/princess_harsh/inside/72.flac"
            swp "I think that's 'you.'\n"
        else:
            voice "audio/_pristine/voice/dragon/princess_soft/inside/62.flac"
            wp "I guess 'you' made it back here.\n"
        play audio "audio/final/Spectre_PossessingPlayer_7.flac"
        hide bg onlayer back
        show bg dragon hands flicker onlayer back at Position(ypos=1125)
        show dragon hands flicker onlayer front at Position(ypos=1125)
        with dissolve
        truthmid "Your gaze turns back to your hands. They flicker once again.\n"
        if spectre_hostile:
            voice "audio/_pristine/voice/dragon/princess_harsh/inside/73.flac"
            swp "We're still a mess. It's like 'you' don't really know what we are.\n"
        else:
            voice "audio/_pristine/voice/dragon/princess_soft/inside/63.flac"
            wp "We're still all... wrong. It's like 'you' don't really know what we're supposed to be.\n"

    play sound "audio/_pristine/sfx/thump_distant.flac"
    queue sound "audio/_pristine/sfx/knife_pickup_suppressed.flac"
    show bg dragon hands flicker1 onlayer back at Position(ypos=1125)
    show dragon hands flicker1 onlayer front at Position(ypos=1125)
    with Dissolve(3.0)
    truthmid "A thump on the floorboards above. And then another. The scraping of metal against a surface. The flickering in your body stops. You are solid.\n"

    if spectre_hostile:
        voice "audio/_pristine/voice/dragon/princess_harsh/inside/74a.flac"
        hide bg onlayer back
        hide dragon onlayer front
        show bg player dragon arrive onlayer back at Position(ypos=1125)
        with dissolve
        swp "So you took the knife. Of course you did.\n"
    else:
        voice "audio/_pristine/voice/dragon/princess_soft/inside/64a.flac"
        hide bg onlayer back
        hide dragon onlayer front
        show bg player dragon arrive onlayer back at Position(ypos=1125)
        with dissolve
        wp "I know that sound. That's the knife. I guess it's hard to do anything without it.\n"
    play audio "audio/one_shot/door_bedroom.flac"
    truthmid "Creaking hinges once again, but this time, clear. Closer.\n"

    default dragon_speech_attempt = False
    menu:
        extend ""

        "{i} ''Hello?''{/i}":
            $ dragon_speech_attempt = True
            truthmid "But you say nothing.\n"
            if spectre_hostile:
                voice "audio/_pristine/voice/dragon/princess_harsh/inside/75.flac"
                swp "I'm the one in control here. You don't get to put words in my mouth.\n"
            else:
                voice "audio/_pristine/voice/dragon/princess_soft/inside/65.flac"
                wp "Are you trying to say something out loud? I don't think you can do that while you're in here with me.\n"

        "{i} ''Hey! Listen to me! I'm stuck in the Princess' head, you've got to get me out of here!''{/i}":
            $ dragon_speech_attempt = True
            truthmid "But you say nothing.\n"
            if spectre_hostile:
                voice "audio/_pristine/voice/dragon/princess_harsh/inside/76.flac"
                swp "I'm the one in control here. You don't get to put words in my mouth. Especially not words like those.\n"
                voice "audio/_pristine/voice/dragon/princess_harsh/inside/77.flac"
                swp "We're stuck together. You'd better get used to that idea.\n"
            else:
                voice "audio/_pristine/voice/dragon/princess_soft/inside/65.flac"
                wp "Are you trying to say something out loud? I don't think you can do that while you're in here with me.\n"
                voice "audio/_pristine/voice/dragon/princess_soft/inside/66.flac"
                wp "I think we're stuck together. So we have to be on the same team. I'd hoped you were on my side by now.\n"

        "{i} Am I going to say anything?{/i}":
            truthmid "Silence.\n"
            if spectre_hostile:
                voice "audio/_pristine/voice/dragon/princess_harsh/inside/78.flac"
                swp "Apparently not.\n"
            else:
                voice "audio/_pristine/voice/dragon/princess_soft/inside/67.flac"
                wp "I guess not.\n"

        "{i} So... what do I look like?{/i}" if dragon_look_like == False:
            $ dragon_look_like = True
            if spectre_hostile:
                voice "audio/_pristine/voice/dragon/princess_harsh/inside/79.flac"
                swp "You really don't know, do you? I guess you'll see soon enough.\n"
            else:
                voice "audio/_pristine/voice/dragon/princess_soft/inside/68.flac"
                wp "Scary. It's... hard to describe. It's hard to look at you.\n"

        "{i} [[Say nothing.]{/i}":
            truthmid "Silence.\n"
            if spectre_hostile:
                voice "audio/_pristine/voice/dragon/princess_harsh/inside/80.flac"
                swp "I guess that body takes after you, even when you're not in it.\n"
            else:
                voice "audio/_pristine/voice/dragon/princess_soft/inside/69.flac"
                wp "Silence.\n"

    play audio "audio/_pristine/sfx/thump_end.flac"
    show player dragon arrive 1 onlayer back at Position(ypos=1125)
    with dissolve
    truthmid "Movement on the stairs.\n"
    if spectre_hostile:
        voice "audio/_pristine/voice/dragon/princess_harsh/inside/81.flac"
        play audio "audio/_pristine/sfx/thump_stairs.flac"
        show player dragon arrive 2 onlayer back at Position(ypos=1125)
        with dissolve
        swp "You're always so loud on the way down.\n"
    else:
        voice "audio/_pristine/voice/dragon/princess_soft/inside/70.flac"
        play audio "audio/_pristine/sfx/thump_stairs.flac"
        show player dragon arrive 2 onlayer back at Position(ypos=1125)
        with dissolve
        wp "Thump. Thump. Thump.\n"

    $ gallery_dragon.unlock_item(4)
    $ renpy.save_persistent()
    play audio "audio/_pristine/sfx/thump_end.flac"
    show player dragon arrive final onlayer back
    with dissolve
    $ renpy.pause(1.0)
    play audio "audio/_pristine/sfx/thump_end.flac"
    show player dragon neutral onlayer back
    with dissolve
    truthmid "And then a figure emerges, shrouded in a feathered darkness, the world trailing behind it, its shining blade gleaming against the wooden walls. It stares at you with wild, hollow eyes.\n"

label dragon_menu_pre_talk:
    default dragon_body_made_aware = False
    default dragon_what_am_i = False
    menu:
        extend ""

        "{i} (Explore) What the hell am I?{/i}" if dragon_what_am_i == False:
            $ dragon_what_am_i = True
            if spectre_hostile:
                voice "audio/_pristine/voice/dragon/princess_harsh/inside/82.flac"
                swp "The dragon. Obviously.\n"
            else:
                voice "audio/_pristine/voice/dragon/princess_soft/inside/71.flac"
                wp "You're... you? You've always looked like this. You're scary, sometimes, but looks only matter so much.\n"
                #wp "I guess you did kill me, though. And then you tried doing it again. But I know it doesn't have to be this way!\n"
            jump dragon_menu_pre_talk

        "{i} ''Hello?''{/i}" if dragon_speech_attempt == False:
            $ dragon_speech_attempt = True
            truthmid "But you say nothing.\n"
            if spectre_hostile:
                voice "audio/_pristine/voice/dragon/princess_harsh/inside/75.flac"
                swp "I'm the one in control here. You don't get to put words in my mouth.\n"
            else:
                voice "audio/_pristine/voice/dragon/princess_soft/inside/65.flac"
                wp "Are you trying to say something out loud? I don't think you can do that while you're in here with me.\n"


        "{i} ''Hey! Listen to me! I'm stuck in the Princess' head, you've got to get me out of here!''{/i}" if dragon_speech_attempt == False:
            $ dragon_speech_attempt = True
            truthmid "But you say nothing.\n"
            if spectre_hostile:
                voice "audio/_pristine/voice/dragon/princess_harsh/inside/76.flac"
                swp "I'm the one in control here. You don't get to put words in my mouth. Especially not words like those.\n"
                voice "audio/_pristine/voice/dragon/princess_harsh/inside/77.flac"
                swp "We're stuck together. You'd better get used to that idea.\n"
            else:
                voice "audio/_pristine/voice/dragon/princess_soft/inside/65.flac"
                wp "Are you trying to say something out loud? I don't think you can do that while you're in here with me.\n"
                voice "audio/_pristine/voice/dragon/princess_soft/inside/66.flac"
                wp "I think we're stuck together. So we have to be on the same team. I'd hoped you were on my side by now.\n"
            label dragon_menu_pre_talk_share_join:
                $ dragon_body_made_aware = True
                if spectre_hostile:
                    voice "audio/_pristine/voice/dragon/princess_harsh/inside/83.flac"
                    swp "But maybe tipping our hand a bit isn't such a bad idea.\n"
                else:
                    voice "audio/_pristine/voice/dragon/princess_soft/inside/72.flac"
                    wp "But maybe we should let them know you're here with me. Maybe it'll help.\n"

        "{i} Quick. Tell them I'm in here!{/i}":
            $ dragon_body_made_aware = True
            if spectre_hostile:
                voice "audio/_pristine/voice/dragon/princess_harsh/inside/84.flac"
                swp "Hmm.... maybe that's not so terrible an idea.\n"
            else:
                voice "audio/_pristine/voice/dragon/princess_soft/inside/73.flac"
                wp "Okay. Let's see what happens.\n"

        "{i} Don't let them know I'm here!{/i}":
            if spectre_hostile:
                voice "audio/_pristine/voice/dragon/princess_harsh/inside/85.flac"
                swp "Keeping our cards close to our chest, hmm? All right. I'll play along.\n"
            else:
                voice "audio/_pristine/voice/dragon/princess_soft/inside/74.flac"
                wp "Do you think they'll get mad? Do you think they'll get violent?\n"

        "{i} What do you want to do?{/i}":
            if spectre_hostile:
                $ dragon_body_made_aware = True
                voice "audio/_pristine/voice/dragon/princess_harsh/inside/86.flac"
                swp "Let's see...\n"
            else:
                voice "audio/_pristine/voice/dragon/princess_soft/inside/75.flac"
                wp "I guess we'll just have to talk to them.\n"

        "{i} [[Say nothing.]{/i}":
            if spectre_hostile:
                $ dragon_body_made_aware = True

    if dragon_body_made_aware:
        $ gallery_dragon.unlock_item(5)
        $ renpy.save_persistent()
        if spectre_hostile:
            voice "audio/_pristine/voice/dragon/princess_harsh/outside/1.flac"
            sp "You're missing something important, aren't you?\n"
        else:
            voice "audio/_pristine/voice/dragon/princess_soft/outside/1.flac"
            p "I'm not alone here this time. Part of you stayed with me when we split apart.\n"
        show player dragon tilt onlayer back
        with dissolve
        truthmid "The head on the figure cocks to the side. Is it inquisitive? Suspicious? Hostile? Its emotions are unreadable.\n"
        if spectre_hostile:
            voice "audio/_pristine/voice/dragon/princess_harsh/outside/2.flac"
            sp "I know because I have it right here.\n"
        else:
            voice "audio/_pristine/voice/dragon/princess_soft/outside/2.flac"
            p "You don't want to hurt that part of you, do you?\n"

    else:
        $ gallery_dragon.unlock_item(6)
        $ renpy.save_persistent()
        if spectre_hostile:
            voice "audio/_pristine/voice/dragon/princess_harsh/outside/3.flac"
            sp "Back to the same song and dance, aren't we?\n"
        else:
            voice "audio/_pristine/voice/dragon/princess_soft/outside/3.flac"
            p "So here we are again. I'm back in chains, and you have your knife. So. What are we going to do?\n"
        show player dragon tilt onlayer back
        with dissolve
        truthmid "The head on the figure cocks to the side. Is it inquisitive? Suspicious? Hostile? Its emotions are unreadable.\n"
        if spectre_hostile:
            voice "audio/_pristine/voice/dragon/princess_harsh/outside/4.flac"
            sp "Well...? What's it going to be this time?\n"
        else:
            voice "audio/_pristine/voice/dragon/princess_soft/outside/4.flac"
            p "I guess we could just... stare... at each other.\n"

    truthmid "The silence holds.\n"


label dragon_final_menu_pre_action:
    menu:
        extend ""


        "{i} Why am I being so quiet? Is it because I'm not there?{/i}":
            if spectre_hostile:
                voice "audio/_pristine/voice/dragon/princess_harsh/inside/87.flac"
                swp "You're always this quiet.\n"
            else:
                voice "audio/_pristine/voice/dragon/princess_soft/inside/76.flac"
                wp "No, I don't think so. You've always been a little quiet.\n"

        "{i} I hate this silence. It's putting me on edge.{/i}":
            if spectre_hostile:
                voice "audio/_pristine/voice/dragon/princess_harsh/inside/88.flac"
                swp "Oh, is it? Because you do this quiet staring act a lot. Can't say I'm a fan.\n"
            else:
                voice "audio/_pristine/voice/dragon/princess_soft/inside/77.flac"
                wp "Now you know how I felt when I first saw you. But I got used to it pretty quick. I'm sure you will too.\n"

        "{i} Am I arguing with myself in there? Has that always happened in real time?{/i}":
            if spectre_hostile:
                voice "audio/_pristine/voice/dragon/princess_harsh/inside/89.flac"
                swp "So that's what was going on with all that silent staring.\n"
            else:
                voice "audio/_pristine/voice/dragon/princess_soft/inside/78.flac"
                wp "Is that why you're always quietly staring?\n"

        "{i} [[Say nothing.]{/i}":
            if spectre_hostile:
                voice "audio/_pristine/voice/dragon/princess_harsh/inside/90.flac"
                swp "Silence. Of course. You really do belong in that body.\n"
            else:
                voice "audio/_pristine/voice/dragon/princess_soft/inside/79.flac"
                wp "Still quiet, huh? Even when you're not in your body, you're kind of quiet.\n"

    if spectre_hostile:
        voice "audio/_pristine/voice/dragon/princess_harsh/outside/5.flac"
        sp "Hey. I'm talking to you. It's rude to have a conversation in front of other people without letting them in on it.\n"
    else:
        voice "audio/_pristine/voice/dragon/princess_soft/outside/5.flac"
        p "I... can't hear what's going on in there anymore now that I'm back in my own body. Do you want to... share your thoughts? It'd only be polite, really.\n"

    ##### split into separate labels based on which voice you're adding.

label dragon_opportunist_start:

    voice "audio/_pristine/voice/dragon/opportunist/1.flac"
    show player dragon opp onlayer back
    with Dissolve(1.0)
    opportunistdragon "Oh, you would like to hear what we're thinking, wouldn't you?\n"
    play audio "audio/one_shot/knife_pickup.flac"
    show player dragon opp dangle onlayer back
    show knife dragon dangle onlayer back at Position(ypos=1125)
    with Dissolve(1.0)
    truthmid "He raises the blade above his head, dangling it by the handle in front of his eyes.\n"
    voice "audio/_pristine/voice/dragon/opportunist/2.flac"
    show player dragon opp dangle talk onlayer back
    with dissolve
    opportunistdragon "But I think we hold the power right now.\n"
    if dragon_body_made_aware:
        voice "audio/_pristine/voice/dragon/hero/1.flac"
        hide knife onlayer back
        show player dragon hero talk onlayer back
        with Dissolve(1.0)
        herodragon "But she knows about the decider being gone. That would be a weird bluff to come up with if it weren't true.\n"
        label dragon_opportunist_sidebar_join:
            voice "audio/_pristine/voice/dragon/opportunist/3a.flac"
            show player dragon opp onlayer back
            with Dissolve(1.0)
            opportunistdragon "Look, I love that you're trying to contribute, but I think we need to take a little sidebar.\n"
            # SKIP
            voice "audio/_pristine/voice/dragon/hero/2b.flac"
            show player dragon hero talk onlayer back
            with Dissolve(1.0)
            herodragon "But I don't want to do a-\n{w=1.40}{nw}"
            show screen disableclick(0.5)
            voice "audio/_pristine/voice/dragon/opportunist/4.flac"
            show player dragon opp onlayer back
            with Dissolve(1.0)
            opportunistdragon "I'm so sorry, this will just be a moment.\n"
            show player dragon neutral onlayer back
            with Dissolve(1.0)
            truthmid "Silence, as the mind in front you falls back into itself.\n"
            if spectre_hostile:
                voice "audio/_pristine/voice/dragon/princess_harsh/inside/91.flac"
                swp "Unbelievable.\n"
            else:
                voice "audio/_pristine/voice/dragon/princess_soft/inside/80.flac"
                wp "Well... okay. I guess we wait for an answer.\n"
            menu:
                extend ""

                "{i} We can wait for them to finish.{/i}" if spectre_hostile:
                    voice "audio/_pristine/voice/dragon/princess_harsh/inside/92.flac"
                    swp "Absolutely not.\n"

                "{i} Yeah, I guess there's nothing we can do, is there?{/i}" if spectre_hostile == False:
                    jump dragon_opportunist_soft_quiet

                "{i} Right? How rude.{/i}" if spectre_hostile:
                    if spectre_hostile:
                        voice "audio/_pristine/voice/dragon/princess_harsh/inside/93.flac"
                        swp "Yeah. This isn't over yet. One second.\n"

                "{i} It's rude, though.{/i}" if spectre_hostile == False:
                    voice "audio/_pristine/voice/dragon/princess_soft/inside/81.flac"
                    wp "Yeah. But I guess there isn't much we can do about it.\n"
                    jump dragon_opportunist_soft_quiet

                "{i} I think you'll have to make them listen. Try being assertive.{/i}":
                    if spectre_hostile:
                        voice "audio/_pristine/voice/dragon/princess_harsh/inside/94.flac"
                        swp "Believe me I can be assertive.\n"
                    else:
                        voice "audio/_pristine/voice/dragon/princess_soft/inside/82.flac"
                        wp "But I don't want to be assertive!\n"
                        voice "audio/_pristine/voice/dragon/princess_soft/inside/83.flac"
                        wp "... {i}Sigh{/i}. Fine.\n"

                "{i} [[Say nothing.]{/i}":
                    if spectre_hostile:
                        voice "audio/_pristine/voice/dragon/princess_harsh/inside/95.flac"
                        swp "Oh, they're in for it if they think we're just going to sit here in silence again. One second.\n"
                    else:
                        jump dragon_opportunist_soft_quiet

            if spectre_hostile:
                voice "audio/_pristine/voice/dragon/princess_harsh/outside/6.flac"
                sp "Hey! I'm talking to you.\n"
            else:
                voice "audio/_pristine/voice/dragon/princess_soft/outside/7.flac"
                p "Um... excuse me?\n"
            voice "audio/_pristine/voice/dragon/cold/1.flac"
            show player dragon cold talk onlayer back
            with Dissolve(1.0)
            colddragon "My apologies. They're really being quite dull in here.\n"
            show player dragon neutral onlayer back
            with Dissolve(1.0)
            truthmid "More silence.\n"
            voice "audio/_pristine/voice/dragon/cold/2.flac"
            show player dragon cold talk onlayer back
            with Dissolve(1.0)
            colddragon "I think they want to kill you. At least the new one does. He's very, very passionate about it.\n"
            if spectre_hostile:
                voice "audio/_pristine/voice/dragon/princess_harsh/outside/7.flac"
                show player dragon neutral onlayer back
                with Dissolve(1.0)
                sp "Well, he can try if he wants, but I'm not so sure you all have it in you. Not without your missing piece.\n"
                voice "audio/_pristine/voice/dragon/opportunist/5.flac"
                play audio "audio/one_shot/knife_pickup.flac"
                show player dragon opp dangle talk onlayer back
                show knife dragon dangle onlayer back at Position(ypos=1125)
                with Dissolve(1.0)
                opportunistdragon "Ah, but that just makes it two birds with one stone, doesn't it? How tempting.\n"
            else:
                voice "audio/_pristine/voice/dragon/princess_soft/outside/extra.flac"
                show player dragon neutral onlayer back
                with Dissolve(1.0)
                p "Can you... tell him not to?\n"
                voice "audio/_pristine/voice/dragon/opportunist/6.flac"
                play audio "audio/one_shot/knife_pickup.flac"
                show player dragon opp dangle talk onlayer back
                show knife dragon dangle onlayer back at Position(ypos=1125)
                with Dissolve(1.0)
                opportunistdragon "Your opinion has been duly noted, annnnnnnnd disregarded. In fact, I think a decision's been made. Two birds with one stone. How tempting.\n"
            jump dragon_opportunist_attack

    else:
        if spectre_hostile:
            $ gallery_dragon.unlock_item(5)
            $ renpy.save_persistent()
            voice "audio/_pristine/voice/dragon/princess_harsh/outside/8.flac"
            hide knife onlayer back
            show player dragon tilt onlayer back
            with Dissolve(1.0)
            sp "Do you hold the power right now? Because I think you're missing a very important part of yourself, so I wouldn't be too hasty about using that knife.\n"
            voice "audio/_pristine/voice/dragon/hero/3a.flac"
            show player dragon hero talk onlayer back
            with Dissolve(1.0)
            herodragon "Wait, you know about the decider being gone? Okay, well that changes things, doesn't it?\n"
            jump dragon_opportunist_sidebar_join
        show player dragon opp dangle onlayer back
        with dissolve
        truthmid "Silence, as the figure continues to stare with a wild grin, but does not act.\n"
        voice "audio/_pristine/voice/dragon/cold/3.flac"
        hide knife onlayer back
        show player dragon cold talk onlayer back
        with Dissolve(1.0)
        colddragon "How dull. We've already had our discussions in private. I'd rather not keep listening to the rest of you run in circles repeating the same arguments again and again and again. It was so much more interesting when we had someone to mediate.\n"
        voice "audio/_pristine/voice/dragon/opportunist/7.flac"
        show player dragon opp onlayer back
        with Dissolve(1.0)
        opportunistdragon "I'm sorry, did you just share {i}privileged information{/i} with the enemy?\n"
        voice "audio/_pristine/voice/dragon/hero/4.flac"
        show player dragon hero talk onlayer back
        with Dissolve(1.0)
        herodragon "Well, it isn't privileged anymore now, is it? Do we really need all this secrecy?\n"
        voice "audio/_pristine/voice/dragon/cold/4.flac"
        show player dragon cold talk onlayer back
        with Dissolve(1.0)
        colddragon "No. We don't.\n"
        voice "audio/_pristine/voice/dragon/opportunist/8.flac"
        show player dragon opp onlayer back
        with Dissolve(1.0)
        opportunistdragon "Uh, yes we do? Sidebar, everyone. Now. Chop chop!\n"
        show player dragon neutral onlayer back
        with Dissolve(1.0)
        truthmid "Silence, as the mind in front you falls back into itself.\n"
        # note, only soft princess can get to this point.
        voice "audio/_pristine/voice/dragon/princess_soft/outside/6.flac"
        p "Um...\n"
        truthmid "There is no response.\n"
        voice "audio/_pristine/voice/dragon/princess_soft/outside/7.flac"
        p "Um, excuse me?\n"
        truth "Nothing.\n"
        voice "audio/_pristine/voice/dragon/princess_soft/inside/84.flac"
        wp "They're not listening to me.\n"
        menu:
            extend ""

            "{i} We can wait for them to finish.{/i}":
                voice "audio/_pristine/voice/dragon/princess_soft/inside/85.flac"
                wp "Yeah, I guess. It's not very nice, though!\n"
                jump dragon_opportunist_soft_quiet

            "{i} Right? How rude.{/i}":
                voice "audio/_pristine/voice/dragon/princess_soft/inside/86.flac"
                wp "Exactly. And you know what? I'm not going to let them push us around like this.\n"
                jump dragon_opportunist_soft_speak_up

            "{i} I think you'll have to make them listen. Try being assertive.{/i}":
                voice "audio/_pristine/voice/dragon/princess_soft/inside/87.flac"
                wp "You're right. No more Nice Princess for them. I'm going to speak my mind.\n"
                label dragon_opportunist_soft_speak_up:
                    $ gallery_dragon.unlock_item(5)
                    $ renpy.save_persistent()
                    default dragon_learn_late = False
                    $ dragon_learn_late = True
                    voice "audio/_pristine/voice/dragon/princess_soft/outside/8.flac"
                    p "Uh... hello?\n"
                    truthmid "Silence.\n"
                    voice "audio/_pristine/voice/dragon/princess_soft/outside/9.flac"
                    p "I'm trying to say something.\n"
                    truthmid "Silence again.\n"
                    voice "audio/_pristine/voice/dragon/princess_soft/outside/yell.flac"
                    show player dragon tilt onlayer back
                    p "HEY I SAID I'M TALKING NOW WILL YOU LISTEN TO ME?!\n"
                    voice "audio/_pristine/voice/dragon/cold/5.flac"
                    show player dragon cold talk onlayer back
                    with Dissolve(1.0)
                    colddragon "So you are. And very loudly. Do you have something to say?\n"
                    voice "audio/_pristine/voice/dragon/princess_soft/outside/10.flac"
                    show player dragon cold onlayer back
                    with dissolve
                    p "Oops. I mean, yeah! I already know about all that 'privileged information.' Because he's in here. With me.\n"
                    voice "audio/_pristine/voice/dragon/cold/6.flac"
                    show player dragon cold talk onlayer back
                    with dissolve
                    colddragon "Oh? How very interesting.\n"
                    voice "audio/_pristine/voice/dragon/hero/5.flac"
                    show player dragon hero talk onlayer back
                    with Dissolve(1.0)
                    herodragon "Yeah. That changes things, doesn't it?\n"
                    voice "audio/_pristine/voice/dragon/hero/6.flac"
                    show player dragon hero onlayer back
                    with Dissolve(1.0)
                    herodragon "... Doesn't it?\n"
                    voice "audio/_pristine/voice/dragon/opportunist/9.flac"
                    play audio "audio/one_shot/knife_pickup.flac"
                    show player dragon opp dangle talk onlayer back
                    show knife dragon dangle onlayer back at Position(ypos=1125)
                    with Dissolve(1.0)
                    opportunistdragon "Oh, it changes things alright. We get to take out two birds with one stone.\n"
                    voice "audio/_pristine/voice/dragon/princess_soft/outside/11.flac"
                    p "Wait... what?\n"
                    jump dragon_opportunist_attack

            "{i} [[Say nothing.]{/i}":
                voice "audio/_pristine/voice/dragon/princess_soft/inside/88.flac"
                wp "Okay. I guess we'll just wait.\n"
                label dragon_opportunist_soft_quiet:
                    truthmid "And so you wait.\n"
                    voice "audio/_pristine/voice/dragon/cold/7.flac"
                    show player dragon cold talk onlayer back
                    with Dissolve(1.0)
                    colddragon "My apologies. They're really being quite dull in here.\n"
                    show player dragon cold onlayer back
                    with dissolve
                    truthmid "And wait.\n"
                    voice "audio/_pristine/voice/dragon/opportunist/10.flac"
                    show player dragon opp onlayer back
                    with Dissolve(1.0)
                    opportunistdragon "We're not being dull! We're strategizing. Now if you would all just bear with me.\n"
                    show player dragon hero onlayer back
                    with Dissolve(1.0)
                    truthmid "And wait.\n"
                    voice "audio/_pristine/voice/dragon/opportunist/11.flac"
                    show player dragon opp onlayer back
                    with Dissolve(1.0)
                    opportunistdragon "And decision made.\n"
                    voice "audio/_pristine/voice/dragon/princess_soft/outside/12.flac"
                    play audio "audio/one_shot/knife_pickup.flac"
                    show player dragon opp dangle onlayer back
                    show knife dragon dangle onlayer back at Position(ypos=1125)
                    with Dissolve(1.0)
                    p "I hope it's a good one?\n"
                    if dragon_body_made_aware:
                        voice "audio/_pristine/voice/dragon/opportunist/12.flac"
                        show player dragon opp dangle talk onlayer back
                        with dissolve
                        opportunistdragon "Good for us. Not for you. But we get to take out two birds with one stone.\n"
                    else:
                        voice "audio/_pristine/voice/dragon/opportunist/13.flac"
                        show player dragon opp dangle talk onlayer back
                        with dissolve
                        opportunistdragon "Oh, good for us. But not so good for you.\n"
                    jump dragon_opportunist_attack


    label dragon_opportunist_attack:
        voice "audio/_pristine/voice/dragon/opportunist/14.flac"
        play audio "audio/_pristine/sfx/thump_end.flac"
        hide knife onlayer back
        show player dragon kill opportunist talk onlayer back
        with Dissolve(1.0)
        opportunistdragon "From what I remember, it was pretty easy to kill you the first time around, and this time you're back to being very... what's the word?\n"
        voice "audio/_pristine/voice/dragon/cold/8.flac"
        show player dragon kill cold talk onlayer back
        with Dissolve(1.0)
        colddragon "Fleshy?\n"
        voice "audio/_pristine/voice/dragon/opportunist/15.flac"
        show player dragon kill opportunist talk onlayer back
        with Dissolve(1.0)
        opportunistdragon "Yes! Exactly! That's precisely the word I was looking for! You're fleshy now. No more of that incorporeality. Trust me. I wouldn't be doing this if I didn't think it would be easy.\n"
        if spectre_hostile:
            voice "audio/_pristine/voice/dragon/princess_harsh/outside/9.flac"
            show player dragon kill hero talk onlayer back
            with Dissolve(1.0)
            sp "Bring it then, but you caught me off guard the first time. It's not going to happen again.\n"
            voice "audio/_pristine/voice/dragon/opportunist/16a.flac"
            show player dragon kill opportunist onlayer back
            with Dissolve(1.0)
            opportunistdragon "Well, what can I say? I'd back off if I wasn't already overcommitted. So I guess I'll just have to pretend that you're bluffing! Which you maybe, probably are!\n"
            voice "audio/_pristine/voice/dragon/princess_harsh/outside/10.flac"
            show player dragon kill hero neutral onlayer back
            with Dissolve(1.0)
            sp "Having second thoughts?\n"
            voice "audio/_pristine/voice/dragon/opportunist/17a.flac"
            show player dragon opportunist talk onlayer back
            with Dissolve(1.0)
            opportunistdragon "Shut up!\n"
        else:
            voice "audio/_pristine/voice/dragon/princess_soft/outside/13.flac"
            show player dragon kill opportunist onlayer back
            with Dissolve(1.0)
            p "And... are you doing this?\n"
            voice "audio/_pristine/voice/dragon/opportunist/18.flac"
            show player dragon kill opportunist talk onlayer back
            with Dissolve(1.0)
            opportunistdragon "Oh I most definitely am!\n"
        if spectre_hostile:
            play sound "audio/_pristine/sfx/_thump_run.flac"
            queue sound "audio/one_shot/knife_pickup.flac"
            hide bg onlayer back
            hide player onlayer back
            show cg dragon attack opp onlayer back at Position(ypos=1125)
            show feathers dragon attack onlayer front at Position(ypos=1125)
            with Dissolve(0.5)
            truthmid "You can feel yourself shrink and then grow, vacilating between small and large, weak and powerful, as the thing in front of you attacks, blade raised and wings spreading.\n" id dragon_opportunist_attack_9c044404
        else:
            play sound "audio/_pristine/sfx/_thump_run.flac"
            queue sound "audio/one_shot/knife_pickup.flac"
            hide bg onlayer back
            hide player onlayer back
            show cg dragon attack opp onlayer back at Position(ypos=1125)
            show feathers dragon attack onlayer front at Position(ypos=1125)
            show arms dragon attack onlayer inyourface at Position(ypos=1125)
            with Dissolve(0.5)
            truthmid "You feel small as the monster in front of you attacks, blade raised and wings spreading.\n"
        voice "audio/_pristine/voice/dragon/hero/7.flac"
        show cg dragon attack hero talk onlayer back
        with Dissolve(1.0)
        herodragon "Uh. Before anything happens, I just wanted to let you all know that we are not all on board with this.\n"
        voice "audio/_pristine/voice/dragon/opportunist/19a.flac"
        show cg dragon attack opp talk onlayer back
        with dissolve
        opportunistdragon "Now, now. We voted.\n"
        voice "audio/_pristine/voice/dragon/hero/8.flac"
        show cg dragon attack hero talk onlayer back
        with dissolve
        herodragon "It was not a majority decision.\n"
        voice "audio/_pristine/voice/dragon/opportunist/20.flac"
        show cg dragon attack opp onlayer back
        with dissolve
        opportunistdragon "But we did have a plurality!\n"
        voice "audio/_pristine/voice/dragon/hero/9.flac"
        show cg dragon attack hero onlayer back
        with dissolve
        herodragon "{i}He{/i} shouldn't count.\n"
        voice "audio/_pristine/voice/dragon/opportunist/21.flac"
        show cg dragon attack opp talk onlayer back
        with dissolve
        opportunistdragon "Says who?\n"
        voice "audio/_pristine/voice/dragon/hero/10.flac"
        show cg dragon attack hero talk onlayer back
        with dissolve
        herodragon "Says me. He's not one of us!\n"
        voice "audio/_pristine/voice/dragon/opportunist/22.flac"
        show cg dragon attack opp onlayer back
        with dissolve
        opportunistdragon "He's been here since the beginning! The old chum really deserves a say. Besides, you'll all thank us when this is finally over, and we are officially on top. But enough chatter.\n"
        voice "audio/_pristine/voice/dragon/cold/final_extra.flac"
        show cg dragon attack cold talk onlayer back
        with dissolve
        colddragon "Oh, so you've finally decided to do something, have you?\n"
        show cg dragon attack cold onlayer back
        with dissolve
        truth "Silence, for just a moment, as cold eyes regard you.\n"
        if spectre_hostile:
            show cg dragon attack hero onlayer back
            with dissolve
            truth "And then silence still as soft eyes hesitate.\n"
            jump dragon_opportunist_fight_hostile
        else:
            show cg dragon attack hero onlayer back
            with dissolve
            truth "And then silence still as soft eyes hesitate.\n"
            jump dragon_opportunist_fight_soft

label dragon_opportunist_fight_hostile:
    $ gallery_dragon.unlock_item(10)
    $ renpy.save_persistent()
    default dragon_arm_gone = False
    play audio "audio/final/Razor_ImpaleSwordBody_6.flac"
    hide cg onlayer back
    hide feathers onlayer front
    hide arms onlayer inyourface
    show dragon stabbed harsh onlayer back at Position(ypos=1125)
    show feathers dragon stabbed harsh onlayer front at Position(ypos=1125)
    show hands dragon stabbed harsh onlayer inyourface at Position(ypos=1125)
    with Dissolve(0.5)
    truthmid "But the hesitation doesn't last, and you feel the sharp sting of cold metal sliding deep into your chest, but you can feel something else too...\n" id dragon_opportunist_fight_hostile_d6f85fe4
    play audio "audio/one_shot/knife_tighten.flac"
    play secondary "audio/final/Assorted_TapestyUnraveledBreakingRip_1.flac"
    #play sound "audio/final/Spectre_PossessingPlayer_5.flac"
    play sound "audio/_pristine/sfx/Dragon Soul Transfer_3.flac"
    show dragon stabbed harsh2 onlayer back at Position(ypos=1125)
    show feathers dragon stabbed harsh2 onlayer front at Position(ypos=1125)
    show hands dragon stabbed harsh2 onlayer inyourface at Position(ypos=1125)
    with Dissolve(0.5)
    truthmid "Rage, flowing from your heart and balling up in closed fists. You throw them at the thing's face and-\n"
    # interrupting - you have switched perspectives.
    $ default_mouse = "default"
    play music "audio/_music/ch1/The World-Ender Loop.flac" loop
    voice "audio/_pristine/voice/dragon/narrator/1.flac"
    play sound "audio/one_shot/punch_two.flac"
    queue sound "audio/one_shot/tackle.flac"
    hide dragon onlayer back
    hide feathers onlayer front
    hide hands onlayer inyourface
    show farback dragon post stabbed harsh onlayer farback at Position(ypos=1125)
    show cg dragon post stabbed harsh onlayer back at Position(ypos=1125)
    show hands dragon post stabbed harsh onlayer front at Position(ypos=1125)
    n "-You can feel bone crack as her fist collides with your jaw, and then a thud as you tumble across the room.\n"
    voice "audio/_pristine/voice/dragon/cold/9.flac"
    cold "You are such a disappointment.\n"
    voice "audio/_pristine/voice/dragon/opportunist/23a.flac"
    opportunist "I'd like to see you do better.\n"
    voice "audio/_pristine/voice/dragon/narrator/2.flac"
    play audio "audio/one_shot/knife_pickup.flac"
    play sound "audio/final/Adversary_StabCut_10.flac"
    queue sound "audio/final/Razor_ImpaleSwordBody_6.flac"
    queue sound "audio/one_shot/blood_leak.flac"
    hide farback onlayer farback
    hide cg onlayer back
    hide hands onlayer front
    show bg dragon generic onlayer farback at Position(ypos=1125)
    show panel1 dragon post stabbed harsh yank onlayer back at Position(ypos=1125)
    show panel2 dragon post stabbed harsh yank onlayer front at Position(ypos=1125, xpos=760)
    with dissolve
    $ dragon_arm_gone = True
    n "The Princess rips the blade from her chest, and, fury in her eyes, cuts herself loose from her bindings.\n"
    menu:
        extend ""

        "{i} ''Wait wait wait I'm back in my body stop! You getting stabbed switched me back!''{/i}":
            hide bg onlayer farback
            hide panel1 onlayer back
            hide panel2 onlayer front
            show bg dragon generic onlayer back at Position(ypos=1125)
            show harsh dragon charge stare onlayer front at Position(ypos=1125)
            with Dissolve(0.5)
            voice "audio/_pristine/voice/dragon/narrator/3a.flac"
            n "Oh... you're different.\n"
            voice "audio/_pristine/voice/dragon/opportunist/24a.flac"
            opportunist "You're back! Just as I intended. I was never cut out for leadership, really.\n"
            voice "audio/_pristine/voice/dragon/princess_harsh/outside/11.flac"
            show harsh dragon charge stare talk onlayer front
            with dissolve
            sp "Then I just have to make this next one count!\n"
            label dragon_harsh_opportunist_violent_end:
                default dragon_harsh_stab_end = False
                stop music
                $ dragon_harsh_stab_end = True
                voice "audio/_pristine/voice/dragon/narrator/4.flac"
                play audio "audio/one_shot/footstep_run_dirt_short.flac"
                hide bg onlayer farback
                hide panel1 onlayer back
                hide panel2 onlayer front
                hide bg onlayer back
                hide harsh onlayer front
                show bg dragon generic onlayer farback at Position(ypos=1125)
                show cg dragon post harsh charge onlayer back at Position(ypos=1125)
                show speedlines onlayer front at Position(ypos=1125)
                show hands dragon post harsh charge onlayer inyourface at Position(ypos=1125)
                with Dissolve(0.5)
                n "As she closes the distance, she raises the blade to strike and...\n"
                play audio "audio/one_shot/knife_pickup.flac"
                voice "audio/_pristine/voice/dragon/hero/11.flac"
                hide speedlines onlayer front
                hide cg onlayer back
                show harsh dragon charge raise onlayer back at Position(ypos=1125)
                with dissolve
                hero "Kills us?\n"
                $ achievement.grant("ACH_DRAGON_OOPS")
                play music "audio/_pristine/music/dragon/Vertigo Intro.flac"
                queue music "audio/_pristine/music/dragon/Vertigo Loop.flac"
                voice "audio/_pristine/voice/dragon/narrator/5.flac"
                play audio "audio/final/Razor_ImpaleSwordBody_6.flac"
                hide harsh onlayer back
                show cg dragon post harsh stabbed onlayer back at Position(ypos=1125)
                show hands dragon post harsh charge onlayer inyourface at shakeshort
                with dissolve
                n "Well, she certainly stabs you, and it certainly hurts.\n"
                $ gallery_dragon.unlock_item(11)
                $ renpy.save_persistent()
                voice "audio/_pristine/voice/dragon/narrator/6.flac"
                play audio "audio/one_shot/blood_spray.flac"
                play sound "audio/one_shot/collapse.flac"
                hide hands onlayer inyourface
                hide cg onlayer back
                hide bg onlayer farback
                scene bg ceiling onlayer farback at shakeshort, Position(ypos=1125)
                show cg dragon post harsh drive onlayer front at shakeshort, Position(ypos=1125)
                with Dissolve(1.0)
                n "But the knife doesn't leave your body. As you grab her wrists, she drives the weapon deeper and deeper into your chest. Your knees buckle from the pain, and as she forcefully pushes you to the ground-\n{w=12.0}{nw}"
                show screen disableclick(0.5)
                # above is interrupted by another perspective shift
                label dragon_harsh_opp_split_join:
                    $ gallery_dragon.unlock_item(8)
                    $ renpy.save_persistent()
                    $ default_mouse = "fusion"
                    play audio "audio/_pristine/sfx/Dragon Soul Transfer_3.flac"
                    if dragon_harsh_stab_end:
                        hide player onlayer front
                        hide hands onlayer front
                        hide bg onlayer back
                        hide cg onlayer front
                        hide bg onlayer farback
                        show bg dragon join sequence onlayer farback at Position(ypos=1125)
                        show cg dragon post harsh drive flick onlayer front at Position(ypos=1125)
                        show invplay dragon join sequence 1 flick onlayer back at Position(ypos=1125)
                        with dissolve
                    else:
                        hide hands onlayer front
                        hide player onlayer front
                        hide cg onlayer back
                        hide princess onlayer back
                        hide bg onlayer back
                        hide cg onlayer front
                        hide bg onlayer farback
                        show bg dragon join sequence onlayer farback at Position(ypos=1125)
                        show princess dragon join sequence 1 flick onlayer front at Position(ypos=1125)
                        show invplay dragon join sequence 1 flick onlayer back at Position(ypos=1125)
                        with Dissolve(1.0)
                    truthmid "You are torn between two places.\n"
                    if spectre_hostile:
                        #voice "audio/_pristine/voice/dragon/princess_harsh/inside/96.flac"
                        #swp "Stay with me!\n"
                        if dragon_harsh_opp_no_comment_fight:
                            voice "audio/_pristine/voice/dragon/princess_harsh/outside/12.flac"
                            if dragon_harsh_stab_end:
                                show cg dragon post harsh drive talk flick onlayer front
                            else:
                                show princess dragon join sequence 1 flick onlayer front
                            with dissolve
                            sp "Wait. I can feel you in there. I'm pulling you out.\n"
                        else:
                            voice "audio/_pristine/voice/dragon/princess_harsh/outside/13.flac"
                            if dragon_harsh_stab_end:
                                show cg dragon post harsh drive talk flick onlayer front
                            else:
                                show princess dragon join sequence 1 flick onlayer front
                            with dissolve
                            sp "I'm taking you back.\n"
                    elif dragon_opp_soft_leave_keep_blade:
                        voice "audio/_pristine/voice/dragon/princess_soft/inside/89.flac"
                        show princess dragon join sequence 1 flick onlayer front
                        with dissolve
                        wp "Don't leave me!\n"
                    else:
                        voice "audio/_pristine/voice/dragon/princess_soft/inside/90.flac"
                        show princess dragon join sequence 1 flick onlayer front
                        with dissolve
                        wp "Come back to me!"
                    play audio "audio/_pristine/sfx/Dragon Soul Transfer_2.flac"
                    hide bg onlayer farback
                    hide bg onlayer back
                    hide cg onlayer front
                    hide bg onlayer farback
                    scene bg black
                    scene bg dragon join sequence onlayer farback at Position(ypos=1125)
                    show invp dragon join sequence 2 flick onlayer farback at Position(ypos=1125)
                    show player dragon join sequence 2 flick onlayer inyourface at Position(ypos=1125)
                    with Dissolve(1.0)
                    truthmid "You are power and you are weakness. You are hope and you are despair. You are acceptance and you are rejection.\n"
                    truthmid "You are the canvas and you are the painter.\n"
                    play audio "audio/_pristine/sfx/Dragon Soul Transfer_4.flac"
                    show invp dragon join sequence penultimate flick onlayer farback
                    show player dragon join sequence penultimate flick onlayer inyourface
                    show princess dragon join sequence penultimate flick onlayer front
                    show invplay dragon join sequence penultimate flick onlayer back
                    with Dissolve(1.0)
                    truthmid "You are the victim and you are the victimizer. You are life and you are death. The Hero and the Princess. The Princess and the Dragon.\n"
                    voice "audio/_pristine/voice/dragon/hero/12.flac"
                    hero "Don't let us die here.\n"
                    play secondary "audio/one_shot/door_close.flac"
                    queue secondary "audio/one_shot/lock_click.flac"
                    truthmid "You slam the door in your own face.\n"
                    voice "audio/_pristine/voice/dragon/narrator/7.flac"
                    n "Don't let everything die here. You have to end this.\n"
                    play audio "audio/_pristine/sfx/Dragon Soul Transfer_1.flac"
                    truthmid "His words are empty. Hollow echoes. The ravings of a ghost.\n"
                    voice "audio/_pristine/voice/dragon/narrator/8.flac"
                    n "Please.\n"
                    stop music
                    if dragon_arm_gone:
                        show invp dragon join sequence final stub flick onlayer farback
                    else:
                        show invp dragon join sequence final flick onlayer farback
                    show player dragon join sequence final flick onlayer inyourface
                    if dragon_arm_gone:
                        show princess dragon join sequence final stub flick onlayer front
                    else:
                        show princess dragon join sequence final flick onlayer front
                    show invplay dragon join sequence final flick onlayer back
                    with Dissolve(1.0)
                    truthmid "But He is already gone. The threads all tie themselves together into a loop that does not end.\n"
                    $ gallery_dragon.unlock_item(9)
                    $ renpy.save_persistent()
                    play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 5.0
                    play music "audio/_pristine/music/dragon/Flute Intro.flac"
                    queue music "audio/_pristine/music/dragon/Flute Loop.flac" loop
                    hide invp onlayer farback
                    hide player onlayer inyourface
                    hide princess onlayer front
                    hide invplay onlayer back
                    show invplay dragon join sequence final onlayer back at Position(ypos=1125)
                    if dragon_arm_gone:
                        show invp dragon join sequence final stub onlayer back at Position(ypos=1125)
                    else:
                        show invp dragon join sequence final onlayer back at Position(ypos=1125)
                    show player dragon join sequence final onlayer inyourface at Position(ypos=1125)
                    if dragon_arm_gone:
                        show princess dragon join sequence final stub onlayer inyourface at Position(ypos=1125)
                    else:
                        show princess dragon join sequence final onlayer inyourface at Position(ypos=1125)
                    with Dissolve(3.0)
                    if spectre_hostile:
                        voice "audio/_pristine/voice/dragon/princess_harsh/inside/97.flac"
                        swp "Does this mean we're together?\n"
                    else:
                        voice "audio/_pristine/voice/dragon/princess_soft/inside/91.flac"
                        wp "We're back together again.\n"
                    show quiet creep1 onlayer farback at Position(ypos=1125)
                    with dissolve
                    truthmid "You look at your hands, tattered and stained in memories.\n"
                    voice "audio/_pristine/voice/dragon/hero/13.flac"
                    hero "Maybe. Why were we fighting each other?\n"
                    if spectre_hostile:
                        voice "audio/_pristine/voice/dragon/princess_harsh/inside/98.flac"
                        show quiet creep2 onlayer farback at Position(ypos=1125)
                        with dissolve
                        swp "You started it.\n"
                        voice "audio/_pristine/voice/dragon/cold/10a.flac"
                    else:
                        voice "audio/_pristine/voice/dragon/princess_soft/inside/92.flac"
                        show quiet creep2 onlayer farback at Position(ypos=1125)
                        with dissolve
                        wp "I don't know.\n"
                        voice "audio/_pristine/voice/dragon/cold/10.flac"
                    cold "We needed something to do.\n"
                    if spectre_hostile:
                        voice "audio/_pristine/voice/dragon/princess_harsh/inside/99.flac"
                        swp "I guess we did.\n"
                    else:
                        voice "audio/_pristine/voice/dragon/princess_soft/inside/93.flac"
                        wp "Then I guess we need something to do again.\n"
                    voice "audio/_pristine/voice/dragon/opportunist/25.flac"
                    show quiet creep3 onlayer farback at Position(ypos=1125)
                    with dissolve
                    opportunist "To new beginnings!\n"
                    stop music
                    if spectre_hostile:
                        voice "audio/_pristine/voice/dragon/princess_harsh/inside/100.flac"
                        swp "Do you feel... cold?\n"
                    else:
                        voice "audio/_pristine/voice/dragon/princess_soft/inside/94.flac"
                        wp "I didn't think being together would feel so... cold. It shouldn't feel like this. It didn't before.\n"
                    play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                    show hands dragon join sequence 1 onlayer inyourface at Position(ypos=1125)
                    with Dissolve(1.0)
                    $ renpy.pause(0.125)
                    if dragon_arm_gone:
                        show hands dragon join sequence stub 2 onlayer inyourface
                    else:
                        show hands dragon join sequence 2 onlayer inyourface
                    with Dissolve(1.0)
                    $ renpy.pause(0.125)
                    hide princess onlayer inyourface
                    hide invp onlayer back
                    hide invplay onlayer back
                    if dragon_arm_gone:
                        show hands dragon join sequence stub 3 onlayer inyourface
                    else:
                        show hands dragon join sequence 3 onlayer inyourface
                    with Dissolve(0.75)
                    $ renpy.pause(0.125)
                    if dragon_arm_gone:
                        show hands dragon join sequence stub 4 onlayer inyourface
                    else:
                        show hands dragon join sequence 4 onlayer inyourface
                    with Dissolve(0.25)
                    $ renpy.pause(0.125)
                    hide hands onlayer inyourface
                    with Dissolve(0.2)
                    $ renpy.pause(0.125)
                    $ blade_held = False
                    $ default_mouse = "default"
                    hide fore onlayer front
                    hide fore onlayer inyourface
                    hide farback onlayer farback
                    hide bg onlayer back
                    hide mid onlayer back
                    hide stars onlayer farback
                    hide bg onlayer back
                    hide quiet onlayer back
                    hide quiet onlayer front
                    hide player onlayer inyourface
                    show farback quiet onlayer farback at Position(ypos=1125)
                    with Dissolve(4.0)
                    show mirror quiet distant onlayer back at Position(ypos=1125)
                    if loops_finished != 0:
                        truthmid "Your peace does not last, nor can it ever. It's time to leave. Memory returns.\n"
                    else:
                        truthmid "Your peace does not last. Something has ripped her from you, and it's left something else in her place.\n"
                    $ dragon_end = "fusion"
                    $ achievement.grant("ACH_DRAGON_FUSE")
                    $ current_princess = "dragonfused"
                    $ princess_kept += 1
                    $ princess_satisfy += 1
                    jump mirror_start
                    # END

        "{i} ''I'm back in here, but you should do it. Kill me. End this and save yourself.''{/i}":
            voice "audio/_pristine/voice/dragon/narrator/3a.flac"
            hide bg onlayer farback
            hide panel1 onlayer back
            hide panel2 onlayer front
            show bg dragon generic onlayer back at Position(ypos=1125)
            show harsh dragon charge stare onlayer front at Position(ypos=1125)
            with Dissolve(0.5)
            n "Oh... you're different.\n"
            voice "audio/_pristine/voice/dragon/opportunist/24a.flac"
            opportunist "You're back! Just as I intended. I was never cut out for leadership, really.\n"
            voice "audio/_pristine/voice/dragon/narrator/9.flac"
            play audio "audio/one_shot/footstep_run_dirt_short.flac"
            hide bg onlayer back
            hide harsh onlayer front
            show bg dragon generic onlayer farback at Position(ypos=1125)
            show cg dragon post harsh charge onlayer back at Position(ypos=1125)
            show speedlines onlayer front at Position(ypos=1125)
            show hands dragon post harsh charge onlayer inyourface at Position(ypos=1125)
            with Dissolve(0.5)
            n "The Princess' hand trembles as she charges at you. But charge she does.\n"
            voice "audio/_pristine/voice/dragon/hero/14.flac"
            hero "Uh. I'm not sure 'kill me' counts as good leadership.\n"
            voice "audio/_pristine/voice/dragon/opportunist/26.flac"
            opportunist "It's certainly decisive, I just love that about this guy. Much better than the choices I would make.\n"
            voice "audio/_pristine/voice/dragon/cold/11.flac"
            cold "Oh. Wow. You actually managed to say something I agreed with.\n"
            voice "audio/_pristine/voice/dragon/narrator/10a.flac"
            play audio "audio/one_shot/knife_pickup.flac"
            hide speedlines onlayer front
            hide cg onlayer back
            show harsh dragon charge raise onlayer back at Position(ypos=1125)
            with dissolve
            n "As she closes the distance, she raises the blade to strike and...\n"
            voice "audio/_pristine/voice/dragon/hero/15.flac"
            hide speedlines onlayer front
            hide cg onlayer back
            show harsh dragon charge doubt onlayer back at Position(ypos=1125)
            with dissolve
            hero "Kills us?\n"
            voice "audio/_pristine/voice/dragon/narrator/11.flac"
            hide hands onlayer inyourface
            show harsh dragon charge fall onlayer back at Position(ypos=1125)
            with dissolve
            n "Lets it fall to her side. She doesn't make eye contact as she speaks.\n"
            voice "audio/_pristine/voice/dragon/princess_harsh/outside/14.flac"
            show harsh dragon charge fall talk onlayer back at Position(ypos=1125)
            with dissolve
            sp "I almost killed you there.\n"
            voice "audio/_pristine/voice/dragon/narrator/12.flac"
            show harsh dragon charge stare onlayer back at Position(ypos=1125)
            with dissolve
            n "And then she looks up at you with fierceness in her gaze.\n"
            voice "audio/_pristine/voice/dragon/princess_harsh/outside/15.flac"
            show harsh dragon charge stare talk onlayer back at Position(ypos=1125)
            with dissolve
            sp "This had better not be a trick. And you're not getting this back.\n"
            stop music
            play audio "audio/final/Razor_SwordSwish_1.flac"
            voice "audio/_pristine/voice/dragon/narrator/13.flac"
            hide bg onlayer farback
            hide harsh onlayer back
            hide hands onlayer inyourface
            show farback dragon blade hurl onlayer farback at Position(ypos=1125)
            show bg dragon blade hurl onlayer back at Position(ypos=1125)
            show knife harsh dragon blade hurl 1 onlayer back at Position(ypos=1125)
            show harsh dragon blade hurl princess onlayer front at Position(ypos=1125)
            with Dissolve(0.50)
            $ renpy.pause(0.125)
            voice sustain
            show knife harsh dragon blade hurl 2 onlayer back at Position(ypos=1125)
            with Dissolve(0.50)
            $ renpy.pause(0.125)
            hide knife onlayer back
            with Dissolve(0.50)
            voice sustain
            n "She turns her back on you and hurls the blade through the basement window, never to be seen again. No no no no no! You need the blade to deal with her!\n"
            voice "audio/_pristine/voice/dragon/cold/12.flac"
            cold "Then I guess we won't be doing your dirty work.\n"
            voice "audio/_pristine/voice/dragon/hero/16.flac"
            hero "Yeah!\n"
            voice "audio/_pristine/voice/dragon/princess_harsh/outside/16.flac"
            show harsh dragon relief talk onlayer front at Position(ypos=1125)
            with Dissolve(0.75)
            spmid "You have no idea how good it felt to get rid of that thing.\n"
            show harsh dragon relief onlayer front at Position(ypos=1125)
            with dissolve
            menu:
                extend ""

                "{i} [[Take her hand in yours.]{/i}":
                    voice "audio/_pristine/voice/dragon/narrator/14.flac"
                    n "Are you serious?! Eugh.\n"
                    voice "audio/_pristine/voice/dragon/cold/13.flac"
                    cold "Well? Are you going to say what happens? You already said yourself that we won't be killing her.\n"
                    voice "audio/_pristine/voice/dragon/narrator/15.flac"
                    play music "audio/_pristine/music/dragon/Piano Intro.flac"
                    queue music "audio/_pristine/music/dragon/Piano Loop.flac" loop
                    play audio "audio/one_shot/knife_tighten.flac"
                    hide harsh onlayer front
                    show dragon leave hold hand onlayer front at Position(ypos=1125)
                    with Dissolve(0.5)
                    n "Grrrrrrrrrrrr. Fine. You take her remaining hand in yours.\n"
                    label dragon_opp_harsh_leave_together:
                        #voice "audio/_pristine/voice/dragon/hero/_extra.flac"
                        #hero "Yeah? And what does it feel like? Is it... nice?\n"
                        voice "audio/_pristine/voice/dragon/opportunist/27a.flac"
                        opportunist "Yeah? And what does it feel like? Is it... nice?\n"
                        voice "audio/_pristine/voice/dragon/narrator/16.flac"
                        n "Why do you want to know?\n"
                        voice "audio/_pristine/voice/dragon/opportunist/28a.flac"
                        opportunist "You can tell a lot of things about someone from their handshake. I want to know more about the person we decided, unanimously, to throw our lot in with.\n"
                        voice "audio/_pristine/voice/dragon/narrator/17.flac"
                        n "Ugh. Whatever. It's rough, but still tender.\n"
                        voice "audio/_pristine/voice/dragon/opportunist/29.flac"
                        opportunist "Ah. The hand of someone who's suffered, but hasn't forgotten what it's like to have a heart. That'll do.\n"
                        voice "audio/_pristine/voice/dragon/princess_harsh/outside/17.flac"
                        show dragon leave hold hand talk onlayer front at Position(ypos=1125)
                        with dissolve
                        spmid "Come on. Let's get out of here.\n"
                        play audio "audio/one_shot/footsteps_creaky.flac"
                        $ quick_menu = False
                        hide farback onlayer farback
                        hide bg onlayer back
                        hide dragon onlayer front
                        scene bg black
                        with fade
                        voice "audio/_pristine/voice/dragon/narrator/18.flac"
                        show farback dragon leave basement onlayer farback at Position(ypos=1125)
                        show cg dragon leave basement onlayer back at Position(ypos=1125)
                        with fade
                        if persistent.quick_menu:
                            $ quick_menu = True
                        n "Hand in hand, you and the Princess leave the basement together. {i}Sigh{/i}.\n"
                        label dragon_opp_leave_together_join:
                            voice "audio/_pristine/voice/dragon/hero/17.flac"
                            hero "Welcome back, by the way.\n"
                            voice "audio/_pristine/voice/dragon/cold/14.flac"
                            cold "Yes. We all missed you so very much.\n"
                            voice "audio/_pristine/voice/dragon/opportunist/30.flac"
                            opportunist "I missed you the most.\n"
                            voice "audio/_pristine/voice/dragon/hero/18.flac"
                            hero "You weren't even here until he was gone.\n"
                            $ quick_menu = False
                            play audio "audio/one_shot/footsteps_creaky.flac"
                            hide farback onlayer farback
                            hide cg onlayer back
                            hide cg onlayer front
                            scene bg black
                            with fade
                            voice "audio/_pristine/voice/dragon/narrator/19.flac"
                            show bg dragon leave door onlayer back at Position(ypos=1125)
                            if spectre_hostile:
                                show cg dragon leave door hostile onlayer front at Position(ypos=1125)
                            else:
                                show cg dragon leave door neutral onlayer front at Position(ypos=1125)
                            with fade
                            if persistent.quick_menu:
                                $ quick_menu = True
                            n "Whatever, it doesn't matter. If you step through that door, you're damning every single person alive. You do realize that, yes?\n"
                            voice "audio/_pristine/voice/dragon/opportunist/31.flac"
                            opportunist "Who cares!\n"
                            if spectre_hostile:
                                #voice "audio/_pristine/voice/dragon/princess_harsh/outside/18.flac"
                                #sp "All we have to do is open that door.\n"
                                voice "audio/_pristine/voice/dragon/princess_harsh/outside/19a.flac"
                                show cg dragon leave door hostile talk arm onlayer front
                                with dissolve
                                sp "In case you hadn't noticed, I lost a hand down there. Would you mind?\n"
                                show cg dragon leave door hostile onlayer front
                                with dissolve
                            else:
                                voice "audio/_pristine/voice/dragon/princess_soft/outside/14.flac"
                                show cg dragon leave door neutral talk onlayer front
                                with dissolve
                                p "One last door and then we're free.\n"
                                voice "audio/_pristine/voice/dragon/princess_soft/outside/15.flac"
                                show cg dragon leave door neutral talk arm onlayer front
                                with dissolve
                                p "I... uh. I'm down a hand, so you'll have to be the one to open it.\n"
                                show cg dragon leave door neutral onlayer front
                                with dissolve
                            menu:
                                extend ""

                                "{i} [[Step into your freedom.]{/i}":
                                    $ quick_menu = False
                                    play audio "audio/one_shot/door_bedroom.flac"
                                    stop sound
                                    stop secondary
                                    stop tertiary
                                    hide bg onlayer back
                                    hide cg onlayer front
                                    scene bg black
                                    with fade
                                    play sound "audio/_pristine/sfx/dragon_grass_collapse.flac"
                                    voice "audio/_pristine/voice/dragon/narrator/20a.flac"
                                    show farback dragon free onlayer farback at Position(ypos=1125)
                                    show cg dragon free onlayer back at Position(ypos=1125)
                                    with fade
                                    if persistent.quick_menu:
                                        $ quick_menu = True
                                    n "You twist the doorknob in your hand and step forward into the world you've damned. You and the Princess fall to the ground, exhausted.\n"
                                    voice "audio/_pristine/voice/dragon/narrator/21b.flac"
                                    n "I hope this all comes back to bite you, do you hear? I hope you're forced to feel the weight of all the regret there's ever been...\n"
                                    truthmid "But He doesn't finish His thought before disappearing entirely. And you find yourself free of any of the regrets he wished upon you.\n"
                                    $ gallery_dragon.unlock_item(16)
                                    $ renpy.save_persistent()
                                    if spectre_hostile:
                                        $ gallery_dragon.unlock_item(14)
                                        $ renpy.save_persistent()
                                        voice "audio/_pristine/voice/dragon/princess_harsh/outside/20.flac"
                                        show cg dragon free talk onlayer back
                                        with dissolve
                                        sp "Finally. This is nice. This is so nice.\n"
                                        voice "audio/_pristine/voice/dragon/princess_harsh/outside/21.flac"
                                        stop music fadeout 20.0
                                        stop sound fadeout 20.0
                                        stop tertiary fadeout 20.0
                                        play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 20.0
                                        show cg dragon free cold talk onlayer back
                                        with dissolve
                                        sp "But it's also cold...\n"
                                    else:
                                        $ gallery_dragon.unlock_item(15)
                                        $ renpy.save_persistent()
                                        voice "audio/_pristine/voice/dragon/princess_soft/outside/16.flac"
                                        show cg dragon free talk onlayer back
                                        with dissolve
                                        p "I didn't think I'd ever get to be happy. But I think I am.\n"
                                        voice "audio/_pristine/voice/dragon/princess_soft/outside/17.flac"
                                        stop music fadeout 20.0
                                        stop sound fadeout 20.0
                                        stop tertiary fadeout 20.0
                                        play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 20.0
                                        show cg dragon free cold talk onlayer back
                                        with dissolve
                                        p "I just didn't realize that being happy would feel so... cold.\n"
                                    play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                                    hide cg onlayer back
                                    show quiet creep3 onlayer farback at Position(ypos=1125)
                                    show hands dragon free 1 onlayer back at Position(ypos=1125)
                                    with Dissolve(1.5)
                                    $ renpy.pause(1.0)
                                    show hands dragon free 2 onlayer back at Position(ypos=1125)
                                    with Dissolve(1.0)
                                    $ renpy.pause(0.5)
                                    show hands dragon free 3 onlayer back at Position(ypos=1125)
                                    with Dissolve(0.5)
                                    $ renpy.pause(0.25)
                                    show hands dragon free 4 onlayer back at Position(ypos=1125)
                                    with Dissolve(0.25)
                                    $ renpy.pause(0.125)
                                    show hands dragon free 5 onlayer back at Position(ypos=1125)
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
                                        truthmid "Your peace does not last, nor can it ever. It's time to leave. Memory returns.\n"
                                    else:
                                        truthmid "Your peace does not last. Something has ripped her from you, and it's left something else in her place.\n"
                                    $ achievement.grant("ACH_DRAGON_FREE")
                                    $ dragon_end = "free"
                                    $ princess_free += 1
                                    $ princess_satisfy += 1
                                    jump mirror_start
                                    # END



                "{i} ''Now what?''{/i}":
                    voice "audio/_pristine/voice/dragon/princess_harsh/outside/22.flac"
                    show harsh dragon relief line talk onlayer front
                    with dissolve
                    sp "We leave, obviously. There's nothing left for either of us here.\n"
                    label dragon_opp_alt_hand:
                        play music "audio/_pristine/music/dragon/Piano Intro.flac"
                        queue music "audio/_pristine/music/dragon/Piano Loop.flac" loop
                        voice "audio/_pristine/voice/dragon/narrator/22.flac"
                        play audio "audio/one_shot/knife_tighten.flac"
                        hide harsh onlayer front
                        show dragon leave hold hand onlayer front at Position(ypos=1125)
                        with Dissolve(0.5)
                        n "The Princess reaches forward and clasps her remaining hand in yours. Eugh.\n"
                        jump dragon_opp_harsh_leave_together

                "{i} ''I guess the only thing for us to do is leave.''{/i}":
                    voice "audio/_pristine/voice/dragon/princess_harsh/outside/23.flac"
                    show harsh dragon relief line talk onlayer front
                    with dissolve
                    sp "Yeah. There's nothing left for either of us here.\n"
                    jump dragon_opp_alt_hand

                "{i} [[Say nothing.]{/i}":
                    voice "audio/_pristine/voice/dragon/princess_harsh/outside/24.flac"
                    show harsh dragon relief line talk onlayer front
                    with dissolve
                    sp "Come on. Let's just go. There's nothing left for either of us here.\n"
                    jump dragon_opp_alt_hand



        "{i} [[Say nothing.]{/i}":
            default dragon_harsh_opp_no_comment_fight = False
            $ dragon_harsh_opp_no_comment_fight = True
            jump dragon_harsh_opportunist_violent_end

label dragon_opportunist_fight_soft:
    $ gallery_dragon.unlock_item(12)
    $ renpy.save_persistent()
    play audio "audio/final/Razor_ImpaleSwordBody_6.flac"
    hide cg onlayer back
    hide feathers onlayer front
    hide arms onlayer inyourface
    show dragon stabbed harsh onlayer back at Position(ypos=1125)
    show feathers dragon stabbed harsh onlayer front at Position(ypos=1125)
    show hands dragon stabbed harsh onlayer inyourface at Position(ypos=1125)
    with Dissolve(0.5)
    truthmid "You can feel the sharp sting of cold metal sliding deep into your chest, but you can feel something else, too.\n"
    truthmid "Fear as your legs wobble, and then as-\n"
    # perspective switches
    $ blade_held = True
    $ default_mouse = "blood"
    play music "audio/_music/ch1/The World-Ender Loop.flac" loop
    voice "audio/_pristine/voice/dragon/narrator/23.flac"
    play sound "audio/one_shot/collapse.flac"
    hide dragon onlayer back
    hide feathers onlayer front
    hide hands onlayer inyourface
    show bg switch dragon soft onlayer back at Position(ypos=1125)
    show player switch dragon soft onlayer front at Position(ypos=1125)
    n "-Princess collapses against the wall.\n"
    voice "audio/_pristine/voice/dragon/opportunist/32a.flac"
    #play audio "audio/one_shot/footsteps_creaky.flac"
    hide bg onlayer back
    hide player onlayer front
    show princess dragon soft stabbed sad neutral onlayer back at Position(ypos=1125)
    show player switch dragon soft aback onlayer front at Position(ypos=1125)
    with Dissolve(0.75)
    opportunist "See? That was {i}easy{/i}.\n"
    voice "audio/_pristine/voice/dragon/hero/19.flac"
    hero "It was too easy. It felt bad.\n"
    voice "audio/_pristine/voice/dragon/opportunist/33a.flac"
    opportunist "Don't feel bad! Life is all about taking the easy wins. You don't think the people at the top got there because they worked for it, do you?\n"
    voice "audio/_pristine/voice/dragon/hero/20.flac"
    hero "I mean, of course they did? Hard work is important.\n"
    voice "audio/_pristine/voice/dragon/cold/15.flac"
    cold "Eh. Hard work often goes unappreciated. Why bother?\n"
    voice "audio/_pristine/voice/dragon/opportunist/34.flac"
    opportunist "Yeah! Screw hard work! I guarantee you that anyone who's anyone has done nothing but take shortcuts.\n"
    voice "audio/_pristine/voice/dragon/hero/21.flac"
    hero "Am I supposed to find that impressive?\n"
    voice "audio/_pristine/voice/dragon/opportunist/35.flac"
    opportunist "Of course you are! I got us here, didn't I?\n"
    voice "audio/_pristine/voice/dragon/narrator/24.flac"
    n "Yes, yes. Everyone's very impressed with your accomplishments, but in case you haven't noticed, she isn't dead yet. So how about you finish this before you start celebrating yourself?\n"
    voice "audio/_pristine/voice/dragon/princess_soft/outside/18.flac"
    show princess dragon soft stabbed hurt talk onlayer back
    with dissolve
    p "What are you waiting for? You won, didn't you? Not that it's hard, executing a helpless captive.\n"
    show princess dragon soft stabbed hurt talk onlayer back
    label dragon_soft_opp_choice_join:
        default dragon_soft_opp_choice_explore = False
        menu:
            extend ""

            "{i} (Explore) ''Oh no! I am so so sorry! Are you okay?''{/i}" if dragon_soft_opp_choice_explore == False:
                voice "audio/_pristine/voice/dragon/narrator/3a.flac"
                show princess dragon soft stabbed sad neutral onlayer back
                with dissolve
                n "Oh... you're different.\n"
                voice "audio/_pristine/voice/dragon/opportunist/24a.flac"
                opportunist "You're back! Just as I intended. I was never cut out for leadership, really.\n"
                voice "audio/_pristine/voice/dragon/princess_soft/outside/19.flac"
                show princess dragon soft relief talk onlayer back
                with dissolve
                p "That's... that's you in that body again, isn't it? I thought it felt a little empty in here.\n"
                voice "audio/_pristine/voice/dragon/princess_soft/outside/20.flac"
                show princess dragon soft stabbed hurt talk onlayer back
                with dissolve
                p "I'm hurt, but I'll live. If you'll let me. Will you? Or are you still going to kill me?\n"
                show princess dragon soft stabbed hurt onlayer back
                jump dragon_soft_opp_choice_sub

            "{i} (Explore) ''Oh, hey. I'm back in my body.''{/i}" if dragon_soft_opp_choice_explore == False:
                $ dragon_soft_opp_choice_explore = True
                voice "audio/_pristine/voice/dragon/narrator/3a.flac"
                show princess dragon soft stabbed sad neutral onlayer back
                with dissolve
                n "Oh... you're different.\n"
                voice "audio/_pristine/voice/dragon/opportunist/24a.flac"
                opportunist "You're back! Just as I intended. I was never cut out for leadership, really.\n"
                voice "audio/_pristine/voice/dragon/princess_soft/outside/21.flac"
                show princess dragon soft stabbed talk thatsyou onlayer back
                with dissolve
                p "You're right. It's quiet again. Are you... still going to kill me?\n"
                voice "audio/_pristine/voice/dragon/opportunist/36.flac"
                show princess dragon soft stabbed hurt onlayer back
                with dissolve
                opportunist "Oooh! Should we? It would be so easy.\n"
                voice "audio/_pristine/voice/dragon/narrator/25.flac"
                n "Absolutely. Nothing of substance has changed. She remains a threat to the entire world.\n"
                label dragon_soft_opp_choice_sub:
                    menu:
                        extend ""

                        "{i} ''Yeah. Sorry about that.'' [[Finish the job.]{/i}":
                            jump dragon_soft_opp_slay_join

                        "{i} ''I'm obviously not going to kill you.''{/i}":
                            voice "audio/_pristine/voice/dragon/princess_soft/outside/22.flac"
                            show princess dragon soft relief talk onlayer back
                            with dissolve
                            p "Then the only thing left to do is cut me out of here.\n"
                            jump dragon_soft_leave_late_join

                        "{i} ''I don't know what I want to do.''{/i}":
                            jump dragon_opp_soft_leave_suggest

                        "{i} [[Say nothing.]{/i}":
                            jump dragon_opp_soft_leave_silent


            "{i} Good to be back boys. [[Finish the job.]{/i}":
                voice "audio/_pristine/voice/dragon/narrator/3a.flac"
                show princess dragon soft stabbed sad neutral onlayer back
                with dissolve
                n "Oh... you're different.\n"
                voice "audio/_pristine/voice/dragon/opportunist/24a.flac"
                opportunist "You're back! Just as I intended. I was never cut out for leadership, really.\n"
                label dragon_soft_opp_slay_join:
                    voice "audio/_pristine/voice/dragon/hero/22.flac"
                    hero "I guess we're really seeing this through, then.\n"
                    voice "audio/_pristine/voice/dragon/narrator/26.flac"
                    play audio "audio/one_shot/knife_pickup.flac"
                    play sound "audio/one_shot/footstep_run_dirt_short.flac"
                    hide princess onlayer back
                    hide player onlayer front
                    show cg dragon soft switch stab onlayer back at Position(ypos=1125)
                    show player switch dragon soft onlayer front at Position(ypos=1125)
                    with Dissolve(0.5)
                    n "You certainly are. Blade raised, you leap towards the Princess with killing intent.\n"
                    stop music
                    if dragon_soft_opp_choice_explore == False:
                        voice "audio/_pristine/voice/dragon/princess_soft/outside/23.flac"
                        show cg dragon soft switch stab talk onlayer back
                        with dissolve
                        p "That's... you in there again, isn't it? I didn't think you'd want to kill me anymore. Not after everything we've been through together.\n"
                    elif dragon_opp_soft_leave_betray:
                        voice "audio/_pristine/voice/dragon/princess_soft/outside/24.flac"
                        show cg dragon soft switch stab talk onlayer back
                        with dissolve
                        p "Oh. I guess you changed your mind. That's... really sad.\n"
                    else:
                        voice "audio/_pristine/voice/dragon/princess_soft/outside/25.flac"
                        show cg dragon soft switch stab talk onlayer back
                        with dissolve
                        p "I didn't think you'd want to kill me anymore. Not after everything we've been through together. Are you sure that's what you want?\n"
                    play music "audio/_pristine/music/dragon/Vertigo Intro.flac"
                    queue music "audio/_pristine/music/dragon/Vertigo Loop.flac"
                    voice "audio/_pristine/voice/dragon/narrator/27.flac"
                    play audio "audio/final/Razor_ImpaleSwordBody_6.flac"
                    hide player onlayer front
                    show cg dragon soft switch stab event onlayer back
                    with dissolve
                    n "But you ignore her words, and as the blade sinks into soft tissue-\n{w=4.3}{nw}"
                    show screen disableclick(0.5)
                    jump dragon_harsh_opp_split_join

            "{i} [[Drop the blade.]{/i}":
                default dragon_dropped_blade = False
                $ dragon_dropped_blade = True
                $ blade_held = False
                $ default_mouse = "default"
                voice "audio/_pristine/voice/dragon/narrator/28.flac"
                play audio "audio/one_shot/knife_bounce_several.flac"
                hide player onlayer front
                show princess dragon soft relief onlayer back
                with dissolve
                n "Are you... {i}sigh{/i}. The blade tumbles uselessly from your hands and clatters to the floor. You're different, aren't you?\n"
                voice "audio/_pristine/voice/dragon/opportunist/24a.flac"
                opportunist "You're back! Just as I intended. I was never cut out for leadership, really.\n"
                voice "audio/_pristine/voice/dragon/princess_soft/outside/26.flac"
                show princess dragon soft stabbed talk thatsyou onlayer back
                with dissolve
                p "Oh... it's {i}you{/i} in there now, isn't it? I thought it got a little quiet. What happens now?\n"
                show princess dragon soft stabbed hurt onlayer back
                with dissolve
                menu:

                    "{i} ''We do it right this time. We leave together. Hand in hand.''{/i}":
                        label dragon_opp_soft_leave_join:
                            voice "audio/_pristine/voice/dragon/narrator/29.flac"
                            show princess dragon soft relief onlayer back
                            with dissolve
                            n "Absolutely not!\n"
                            voice "audio/_pristine/voice/dragon/cold/16.flac"
                            cold "I don't think there's much you can do about it if that's the choice he makes.\n"
                            voice "audio/_pristine/voice/dragon/narrator/30a.flac"
                            n "But-\n"
                            voice "audio/_pristine/voice/dragon/cold/17.flac"
                            cold "No. I think I'd like to see what happens.\n"
                            #voice "audio/_pristine/voice/dragon/opportunist/37.flac"
                            #opportunist "He is the decider, after all.\n"
                            voice "audio/_pristine/voice/dragon/princess_soft/outside/27.flac"
                            show princess dragon soft relief talk onlayer back
                            with dissolve
                            p "Okay. I'd like that. But we still have to get me out of these chains.\n"
                            label dragon_soft_leave_late_join:
                                if dragon_dropped_blade:
                                    voice "audio/_pristine/voice/dragon/princess_soft/outside/28.flac"
                                    show princess dragon soft stabbed talk hurt onlayer back
                                    with dissolve
                                    p "I know that dropping the knife was like, this big symbolic gesture for you, but we still need it. Just for a minute.\n"
                                    voice "audio/_pristine/voice/dragon/princess_soft/outside/29.flac"
                                    show princess dragon soft stabbed talk onlayer back
                                    with dissolve
                                    p "You should give it to me though. What if you using it kicks you out of your body again?\n"
                                else:
                                    voice "audio/_pristine/voice/dragon/princess_soft/outside/30.flac"
                                    show princess dragon soft stabbed talk onlayer back
                                    with dissolve
                                    p "You should give the knife to me though. What if you using it kicks you out of your body again?\n"
                                voice "audio/_pristine/voice/dragon/opportunist/38.flac"
                                show princess dragon soft stabbed sad neutral onlayer back
                                with dissolve
                                opportunist "Okay. Listen. I know you're in charge again, but this is obviously a trick. We can't trust her. We literally just stabbed her!\n"
                                voice "audio/_pristine/voice/dragon/hero/23.flac"
                                hero "Someone's going to have to take a leap of faith eventually...\n"
                                #voice "audio/_pristine/voice/dragon/narrator/31.flac"
                                #n "No. Nobody has to take any leaps of faith. Not if you slay her and save the entire world like you're supposed to.\n"
                                #voice "audio/_pristine/voice/dragon/cold/18.flac"
                                #cold "I think we've already decided that we're not doing that. It's boring to backtrack.\n"
                                default dragon_opp_soft_leave_keep_blade = False
                                default dragon_opp_soft_leave_betray = False
                                menu:
                                    extend ""

                                    "{i} [[Slay the Princess.]{/i}":
                                        $ dragon_opp_soft_leave_betray = True
                                        #voice "audio/_pristine/voice/dragon/narrator/32.flac"
                                        #n "Thank you. Clearly someone here is sane. Clearly someone here has realized that boring doesn't matter!\n" id dragon_soft_leave_late_join_53a15926
                                        voice "audio/_pristine/voice/dragon/opportunist/39.flac"
                                        opportunist "A leader after my own heart.\n"
                                        if blade_held == False:
                                            play audio "audio/one_shot/knife_pickup.flac"
                                            $ blade_held = True
                                            $ default_mouse = "blood"
                                        jump dragon_soft_opp_slay_join


                                    "{i} [[Cut her free on your own.]{/i}":
                                        $ dragon_opp_soft_leave_keep_blade = True
                                        label dragon_opp_soft_free_oops:
                                            $ gallery_dragon.unlock_item(13)
                                            $ renpy.save_persistent()
                                            if blade_held == False:
                                                play audio "audio/one_shot/knife_pickup.flac"
                                                $ blade_held = True
                                                $ default_mouse = "blood"
                                            stop music
                                            voice "audio/_pristine/voice/dragon/narrator/33.flac"
                                            play audio "audio/one_shot/stab_goop.flac"
                                            hide player onlayer front
                                            hide princess onlayer back
                                            show cg dragon soft oops cut onlayer back at Position(ypos=1125)
                                            with Dissolve(0.75)
                                            n "You go to cut the Princess from her bindings, and as the blade slices into her wrist-\n{w=6.3}{nw}"
                                            show screen disableclick(0.5)
                                            play music "audio/_pristine/music/dragon/Vertigo Intro.flac"
                                            queue music "audio/_pristine/music/dragon/Vertigo Loop.flac"
                                            play audio "audio/_pristine/sfx/Dragon Soul Transfer_1.flac"
                                            hide cg onlayer back
                                            show cg dragon soft oops switch onlayer back at Position(ypos=1125)
                                            truthmid "You are pulled back across the threshold.\n"
                                            voice "audio/_pristine/voice/dragon/princess_soft/outside/31.flac"
                                            wp "Oh. I... felt that. You're back!\n"
                                            truthmid "Menace permeates the hollow eyes in front of you.\n"
                                            voice "audio/_pristine/voice/dragon/princess_soft/outside/32.flac"
                                            wp "... Oh no you're back!\n"
                                            voice "audio/_pristine/voice/dragon/opportunist/40.flac"
                                            show cg dragon soft oops grin onlayer back
                                            with dissolve
                                            opportunistdragon "Sorry, girlie, but we're seeing this through!\n"
                                            play audio "audio/final/Razor_ImpaleSwordBody_6.flac"
                                            show cg dragon soft oops stab onlayer back
                                            show hands dragon soft oops stab onlayer front at Position(ypos=1125)
                                            with dissolve
                                            truthmid "The monster in front of you pulls the blade back and drives it into your heart.\n"
                                            jump dragon_harsh_opp_split_join


                                    "{i} [[Give her the blade.]{/i}":
                                        label dragon_opp_soft_free_join:
                                            if blade_held == False:
                                                voice "audio/_pristine/voice/dragon/narrator/34.flac"
                                                play audio "audio/one_shot/knife_pickup.flac"
                                                $ blade_held = True
                                                $ default_mouse = "blood"
                                                show player switch dragon soft aback onlayer front at Position(ypos=1125)
                                                with dissolve
                                                n "{i}Sigh{/i}. Fine. Whatever. You stoop to the floor and pick up the pristine blade, only rather than using it for its intendended purpose, you...\n"
                                                voice "audio/_pristine/voice/dragon/cold/19.flac"
                                                cold "Go on.\n"
                                                voice "audio/_pristine/voice/dragon/narrator/35.flac"
                                                $ blade_held = False
                                                $ default_mouse = "default"
                                                play audio "audio/one_shot/stab_goop.flac"
                                                hide player onlayer front
                                                hide princess onlayer back
                                                hide bg onlayer back
                                                show princess dragon soft free onlayer back at Position(ypos=1125)
                                                with Dissolve(0.5)
                                                n "You hand it to the Princess, who gingerly cuts herself free from her bindings. You maniac.\n"
                                            else:
                                                voice "audio/_pristine/voice/dragon/narrator/35a.flac"
                                                $ blade_held = False
                                                $ default_mouse = "default"
                                                play audio "audio/one_shot/stab_goop.flac"
                                                hide player onlayer front
                                                hide princess onlayer back
                                                hide bg onlayer back
                                                show princess dragon soft free onlayer back at Position(ypos=1125)
                                                with Dissolve(0.5)
                                                n "You hand the blade to the Princess, who gingerly cuts herself free from her bindings. You maniac.\n"
                                            stop music
                                            voice "audio/_pristine/voice/dragon/hero/24.flac"
                                            hero "... And then what happens?\n"
                                            voice "audio/_pristine/voice/dragon/narrator/36.flac"
                                            stop music
                                            play tertiary "audio/one_shot/chain_1.flac"
                                            play audio "audio/final/Razor_SwordSwish_1.flac"
                                            hide princess onlayer back
                                            hide bg onlayer farback
                                            hide harsh onlayer back
                                            hide hands onlayer inyourface
                                            show farback dragon blade hurl onlayer farback at Position(ypos=1125)
                                            show bg dragon blade hurl onlayer back at Position(ypos=1125)
                                            show knife harsh dragon blade hurl 1 onlayer back at Position(ypos=1125)
                                            show harsh dragon blade hurl princess onlayer front at Position(ypos=1125)
                                            with Dissolve(0.50)
                                            $ renpy.pause(0.125)
                                            voice sustain
                                            show knife harsh dragon blade hurl 2 onlayer back at Position(ypos=1125)
                                            with Dissolve(0.50)
                                            $ renpy.pause(0.125)
                                            hide knife onlayer back
                                            with Dissolve(0.50)
                                            voice sustain
                                            n "Then, as her chains clatter to the floor, she turns her back on you and hurls the blade through the basement window, never to be seen again. No no no no no! You need the blade to deal with her!\n" id dragon_opp_soft_free_join_c723506b
                                            voice "audio/_pristine/voice/dragon/princess_soft/outside/33.flac"
                                            show harsh dragon relief talk onlayer front at Position(ypos=1125)
                                            with Dissolve(0.75)
                                            pmid "{i}Sigh.{/i} I'm so glad that's behind us. Come on. Let's get out of here.\n"
                                            voice "audio/_pristine/voice/dragon/narrator/37.flac"
                                            play audio "audio/one_shot/knife_tighten.flac"
                                            play music "audio/_pristine/music/dragon/Piano Intro.flac"
                                            queue music "audio/_pristine/music/dragon/Piano Loop.flac" loop
                                            hide harsh onlayer front
                                            show dragon leave hold hand onlayer front at Position(ypos=1125)
                                            with Dissolve(0.5)
                                            n "She reaches forward and takes your hand in hers before excitedly pulling you towards the basement stairs.\n" id dragon_opp_soft_free_join_0648c2ba
                                            #voice "audio/_pristine/voice/dragon/hero/_extra.flac"
                                            #hero "Yeah? And what does it feel like? Is it... nice?\n"
                                            voice "audio/_pristine/voice/dragon/opportunist/27a.flac"
                                            opportunist "Yeah? And what does it feel like? Is it... nice?\n"
                                            voice "audio/_pristine/voice/dragon/narrator/38.flac"
                                            n "Why do you want to know?\n"
                                            voice "audio/_pristine/voice/dragon/opportunist/28a.flac"
                                            opportunist "You can tell a lot of things about someone from their handshake. I want to know more about the person we decided, unanimously, to throw our lot in with.\n"
                                            voice "audio/_pristine/voice/dragon/narrator/39.flac"
                                            n "Ugh. Whatever. It's delicate and tender.\n"
                                            voice "audio/_pristine/voice/dragon/opportunist/42.flac"
                                            opportunist "Ah. So even through everything, she hasn't forgotten what it's like to have a heart. That'll do.\n"
                                            play audio "audio/one_shot/footsteps_creaky.flac"
                                            $ quick_menu = False
                                            hide farback onlayer farback
                                            hide bg onlayer back
                                            hide dragon onlayer front
                                            scene bg black
                                            with fade
                                            voice "audio/_pristine/voice/dragon/narrator/40.flac"
                                            show farback dragon leave basement onlayer farback at Position(ypos=1125)
                                            show cg dragon leave basement onlayer back at Position(ypos=1125)
                                            with fade
                                            if persistent.quick_menu:
                                                $ quick_menu = True
                                            n "{i}Sigh{/i}. The two of you rush up the basement stairs... together. Eugh.\n"
                                            jump dragon_opp_leave_together_join


                    "{i} ''I don't know.''{/i}":
                        label dragon_opp_soft_leave_suggest:
                            voice "audio/_pristine/voice/dragon/princess_soft/outside/34.flac"
                            show princess dragon soft relief talk onlayer back
                            with dissolve
                            p "Well... what if we try again, only we do it right this time? We can leave together, and we can even do it in two separate bodies.\n"
                            jump dragon_opp_soft_leave_join


                    "{i} [[Say nothing.]{/i}":
                        label dragon_opp_soft_leave_silent:
                            voice "audio/_pristine/voice/dragon/princess_soft/outside/35.flac"
                            show princess dragon soft relief talk onlayer back
                            with dissolve
                            p "Okay. Quiet it is. That's fine. I can do the talking for both of us.\n"
                            jump dragon_opp_soft_leave_suggest

            "{i} [[Turn around and leave.]{/i}":
                stop music fadeout 10.0
                $ quick_menu = False
                play audio "audio/one_shot/footsteps_creaky.flac"
                hide princess onlayer back
                hide player onlayer front
                with fade
                voice "audio/_pristine/voice/dragon/opportunist/24a.flac"
                show farback dragon leave basement onlayer farback at Position(ypos=1125)
                show bg dragon leave alone onlayer back at Position(ypos=1125)
                with fade
                if persistent.quick_menu:
                    $ quick_menu = True
                opportunist "You're back! Just as I intended. I was never cut out for leadership, really.\n"
                voice "audio/_pristine/voice/dragon/opportunist/43a.flac"
                opportunist "And that's a brilliant plan! Who ever needed violence anyways?\n"
                voice "audio/_pristine/voice/dragon/narrator/41.flac"
                n "Inaction is still a choice. If you turn around and leave, you're damning everyone to death.\n"
                voice "audio/_pristine/voice/dragon/opportunist/44.flac"
                opportunist "But we're not damning {i}ourself{/i}.\n"
                voice "audio/_pristine/voice/dragon/narrator/42.flac"
                n "You're part of everyone.\n"
                voice "audio/_pristine/voice/dragon/cold/20.flac"
                cold "Are we now?\n"
                voice "audio/_pristine/voice/dragon/princess_soft/outside/36.flac"
                p "That must be you in that body again, but... you're just turning around and leaving? What about me? What am I supposed to do here?\n"
                voice "audio/_pristine/voice/dragon/hero/25.flac"
                hero "She sounds so sad.\n"
                menu:
                    extend ""

                    "{i} ''You can figure that out on your own.''{/i}":
                        voice "audio/_pristine/voice/dragon/princess_soft/outside/37.flac"
                        p "I'm bleeding and chained to a wall.\n"
                        jump dragon_soft_leave

                    "{i} ''I just wanted my body back.''{/i}":
                        voice "audio/_pristine/voice/dragon/princess_soft/outside/38.flac"
                        p "Well. I guess you have it.\n"
                        jump dragon_soft_leave

                    "{i} [[Say nothing.]{/i}":
                        default dragon_leave_silent = False
                        $ dragon_leave_silent = True
                        label dragon_soft_leave:
                            #voice "audio/_pristine/voice/dragon/narrator/43.flac"
                            #n "You turn and leave without another word. This is not a resolution.\n"
                            voice "audio/_pristine/voice/dragon/narrator/43a.flac"
                            stop music fadeout 20.0
                            stop sound fadeout 20.0
                            stop tertiary fadeout 20.0
                            play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 20.0
                            show quiet creep1 onlayer back at Position(ypos=1125)
                            with Dissolve(0.5)
                            n "This is not a resolution.\n"
                            voice "audio/_pristine/voice/dragon/hero/26.flac"
                            hero "I don't know. It kind of feels like it is.\n"
                            voice "audio/_pristine/voice/dragon/opportunist/45.flac"
                            show quiet creep2 onlayer back
                            with Dissolve(0.5)
                            opportunist "Yeah. We got our decider back. And we didn't die. I feel on top of the world right now.\n"
                            if dragon_leave_silent == False:
                                voice "audio/_pristine/voice/dragon/princess_soft/outside/39.flac"
                                p "What did I ever do to deserve you?\n"
                            else:
                                voice "audio/_pristine/voice/dragon/princess_soft/outside/40.flac"
                                p "You're not even going to answer me. What did I ever do to deserve you?\n"
                            voice "audio/_pristine/voice/dragon/cold/21.flac"
                            $ gallery_dragon.unlock_item(7)
                            $ renpy.save_persistent()
                            show quiet creep3 onlayer back
                            with Dissolve(0.5)
                            cold "Nothing.\n"
                            voice "audio/_pristine/voice/dragon/princess_soft/outside/41.flac"
                            p "It's so cold and empty here.\n"
                            play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                            hide farback onlayer farback
                            hide bg onlayer back
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
                                truthmid "But as look over your shoulder, you do not find her, nor will you ever. It's time to leave. Memory returns.\n"
                            else:
                                truthmid "But as look over your shoulder, you do not find her. Something has taken her away, and it's left something else in her place.\n"
                            $ dragon_end = "abandon"
                            $ current_princess = "dragonhand"
                            $ princess_kept += 1
                            $ princess_deny += 1
                            $ achievement.grant("ACH_DRAGON_ABANDON")
                            jump mirror_start
                            # END





return
