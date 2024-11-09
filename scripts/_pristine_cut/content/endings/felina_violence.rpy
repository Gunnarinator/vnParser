label felina_godkiller_ending:

    voice "audio/_pristine/voice/_climax/new_ending/1.flac"
    play audio "audio/_pristine/sfx/ShiftingMound sucked in blackhole_2.flac"
    play secondary "audio/final/oblivion_find.flac"
    hide farback onlayer farback
    hide back onlayer back
    hide midground onlayer front
    hide farback onlayer farback
    hide back onlayer back
    hide midground onlayer back
    hide hair onlayer front
    hide dress onlayer front
    hide shifting onlayer front
    hide dress onlayer front
    hide shifting onlayer front
    hide farback onlayer farback
    hide back onlayer back
    hide midground onlayer front
    hide hair onlayer front
    hide shifting onlayer front
    hide dress onlayer front
    hide felina onlayer back
    hide felina onlayer front
    hide felina onlayer inyourface

    #show back awakening onlayer farback at Position(ypos=1125)
    #show midground awakening onlayer back at Position(ypos=1125)
    #show mound death begin onlayer front at shakeshort, Position(ypos=1125)
    #show fore mound death begin onlayer inyourface at shakeshort, Position(ypos=1125)
    #with Dissolve(0.5)


    scene farback mound death offended talk onlayer farback at shakeshort, Position(ypos=1125)
    show bg mound death offended talk onlayer back at shakeshort, Position(ypos=1125)
    show mid mound death offended talk onlayer front at shakeshort, Position(ypos=1125)
    show mound death offended talk onlayer inyourface at shakeshort, Position(ypos=1125)
    with Dissolve(0.5)
    mounds "ENOUGH!\n"
    play audio "audio/_pristine/sfx/ShiftingMound sucked in blackhole_7.flac"
    play secondary "audio/_pristine/sfx/shifty_dance.flac"
    play tertiary "audio/_pristine/sfx/shifty_move.flac"
    hide farback onlayer farback
    hide bg onlayer back
    hide mid onlayer front
    hide mound onlayer inyourface
    hide mound onlayer front
    hide fore onlayer inyourface
    show farback mound death 1 onlayer farback at shakeshort, Position(ypos=1125)
    show bg mound death 1 onlayer farback at shakeshort, Position(ypos=1125)
    show mid mound death 1 onlayer back at shakeshort, Position(ypos=1125)
    show mound death 1 onlayer front at shakeshort, Position(ypos=1125)
    show fore mound death 1 onlayer inyourface at shakeshort, Position(ypos=1125)
    with Dissolve(0.5)
    truth "The Princess dives into you once more. But this time, no lone figure claws its way to the surface. Instead, you are swept up in the whole of her multitudes, an infinite tide crashing against you.\n"
    play secondary "audio/_pristine/sfx/shifty_crawl.flac"
    play tertiary "audio/_pristine/sfx/shifty_move.flac"
    truth "They are like gnats against your divine skin.\n"
    voice "audio/_pristine/voice/_climax/new_ending/2.flac"
    show mound death 1 talk onlayer front
    with dissolve
    mounds "I AM THE THREAD THAT WEAVES NOTHING INTO SOMETHING.\n"
    play secondary "audio/_pristine/sfx/shifty_hands.flac"
    play audio "audio/_pristine/sfx/shifty_move.flac"
    hide farback onlayer farback
    hide bg onlayer farback
    hide mid onlayer back
    hide mound onlayer front
    hide fore onlayer inyourface
    show back awakening onlayer farback at Position(ypos=1125)
    show midground awakening onlayer back at Position(ypos=1125)
    show bg mound death 2 onlayer front at shakeshort, Position(ypos=1125, xpos = 900)
    show mound death 2 onlayer inyourface at shakeshort, Position(ypos=1125)
    with Dissolve(1.0)
    truth "She tears into you, hand and fist and tooth and claw, the pace of your dance quickening and quickening and quickening. But the faster she moves, the more easily you keep pace. You have already seen the path to victory.\n"
    play audio "audio/_pristine/sfx/_hands_grab.flac"
    hide bg onlayer front
    hide back onlayer farback
    hide midground onlayer back
    hide mound onlayer inyourface
    show farback mound death 3 onlayer farback at shakeshort, Position(ypos=1125)
    show bg mound death 3 onlayer farback at shakeshort, Position(ypos=1125)
    show mid mound death 3 onlayer back at shakeshort, Position(ypos=1125)
    show mound death 3 onlayer front at shakeshort, Position(ypos=1125)
    show fore mound death 3 onlayer inyourface at shakeshort, Position(ypos=1125)
    with Dissolve(1.25)
    truth "As she strikes again you catch her, hands clasping her wrists and wings binding her arms. A furor rises in her multitudes as they struggle against you, but you remain unmovable in your resolve.\n"
    #play audio "audio/final/Assorted_TapestyUnraveledBreakingRip_1.flac"
    hide farback onlayer farback
    hide bg onlayer farback
    hide mid onlayer back
    hide mound onlayer front
    hide fore onlayer inyourface
    show farback mound death 4 onlayer farback at Position(ypos=1125)
    show bg mound death 4 onlayer farback at Position(ypos=1125)
    show mid mound death 4 onlayer back at Position(ypos=1125)
    show mound death 4 defeat onlayer front at Position(ypos=1125)
    show fore mound death 3 onlayer inyourface at Position(ypos=1125)
    with Dissolve(1.0)
    truth "And then it's over. Her shoulders slump, and her limbs go slack. You see defeat in her many eyes.\n"
    voice "audio/_pristine/voice/_climax/new_ending/3.flac"
    show mound death 4 defeat talk onlayer front
    with dissolve
    mound "This shouldn't be possible. What are you? What can you ever hope to be without me to define your shape?\n"
    voice "audio/_pristine/voice/_climax/new_ending/4.flac"
    show mound death 4 defeat onlayer front
    with dissolve
    mound "Please... don't do this to yourself.\n"
    truth "But the time for speech is over. You will make her see your truth.\n"

    menu:
        extend ""

        "{i}• [[Offer her your hand.]{/i}":
            $ gallery_zfinale.unlock_item(20)
            default final_offer = False
            show fore mound death 4 offer onlayer inyourface
            with Dissolve(1.0)
            $ renpy.pause(0.5)
            $ final_offer = True
            voice "audio/_pristine/voice/_climax/new_ending/5.flac"
            show mound death 4 defeat talk onlayer front
            with Dissolve(0.5)
            mound "You offer me your hand as if you've proven me wrong. But I'm not wrong! I can't be wrong!\n"
            voice "audio/_pristine/voice/_climax/new_ending/6.flac"
            #play audio "audio/final/Adversary_BodySMashedAgainstWall_1.flac"
            play secondary "audio/_pristine/sfx/shifty_dance.flac"
            play tertiary "audio/_pristine/sfx/shifty_move.flac"
            hide fore onlayer inyourface
            show mound death 4 talk final onlayer front
            with Dissolve(0.5)
            mounds "You just haven't listened to me.\n"
            #voice "audio/_pristine/voice/_climax/new_ending/7.flac"
            #mounds "If it takes all of eternity to free you from your delusion, then I will spend all of eternity freeing you.\n"
            jump felina_intermission_late_join

        "{i}• [[Destroy her.]{/i}":
            $ gallery_zfinale.unlock_item(16)
            $ gallery_zfinale.unlock_item(17)
            $ gallery_zfinale.unlock_item(18)
            $ renpy.save_persistent()
            stop music
            play secondary "audio/final/___The Long Quiet Softest FINAL.ogg" loop fadein 20.0
            hide back onlayer farback
            hide midground onlayer farback
            hide farback onlayer farback
            hide bg onlayer farback
            hide mid onlayer back
            hide mound onlayer front
            hide fore onlayer inyourface
            show quiet finale1 onlayer farback at Position(ypos=1125)
            show back trees cabin quiet onlayer back at Position(ypos=1500)
            show bg cabin quiet onlayer front at Position(ypos=1500)
            show mid cabin quiet onlayer inyourface at Position(ypos=1125)
            show fore cabin quiet onlayer inyourface at Position(ypos=1125)
            truthmid "She is gone. And you are truly alone.\n"
            truthmid "But there are worse things to be than alone.\n"
            truthmid "Your consciousness sits at the center of the Long Quiet. At the center of yourself. With nothing left to distract you, you can finally feel its edges. The artificial constraints put in place by a lesser thing that could never hope to understand you, where the infinite folds into itself endlessly.\n"
            if mirror_construct_follow_up:
                truthmid "The Construct.\n"
            else:
                truthmid "Your cage.\n"
            truthmid "It could only imprison you as long as you didn't notice it. And it has your full attention now.\n"
            play audio "audio/final/Assorted_SphereBreaks_1.flac"
            #$ quick_menu = False
            play sound "audio/looping/STP_chaoticwind_loop.ogg" loop
            scene reality new ending
            show quiet finale2 onlayer farback
            with Dissolve(1.5)
            $ renpy.pause(0.25)
            show quiet finale3 onlayer farback
            with Dissolve(1.5)
            $ renpy.pause(0.25)
            show quiet finale4 onlayer farback
            with Dissolve(1.5)
            $ renpy.pause(0.25)
            hide quiet onlayer farback
            with Dissolve(1.5)
            #hide farback onlayer farback
            #hide back onlayer back
            #hide bg onlayer front
            #hide mid onlayer inyourface
            #hide fore onlayer inyourface
            #scene bg black
            $ gallery_zfinale.unlock_item(19)
            truth "At the mere thought that it might break, it falls apart.\n"
            truth "And there you see it. A world free from death. Your new world. Ever moving, but never decaying. A world of uninterrupted experience.\n"
            truth "What things will you put in it, now that it is yours? What beings will you carve into eternity to experience you?\n"
            truth "What textures will you weave for yourself to occupy forever?\n"
            $ final_ending = "annihilation"
            $ quick_menu = False
            hide quiet onlayer farback
            hide slay onlayer farback
            hide back onlayer back
            hide bg onlayer front
            hide mid onlayer inyourface
            hide fore onlayer inyourface
            scene bg black
            with fade
            $ achievement.grant("ACH_ALONE")
            jump credits
            # jump to credits, this is the end
