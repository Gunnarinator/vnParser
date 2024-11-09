label felina_violence_join:
    default felina_violence_counter = 0
    default felina_nonviolence_chosen = False
    default felina_violence_broken = False
    default felina_come_from_violence = False
    $ felina_come_from_violence = True
    $ felina_violence_counter += 1
    $ felina_fight_effective_resistance += 1
    if felina_violence_counter == 1:
        voice "audio/_pristine/voice/_climax/felina/_temp/15a.flac"
        if come_from_tower:
            $ come_from_tower = False
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
            show farback quiet onlayer farback at Position(ypos=1125)
            show back awakening onlayer back at Position(ypos=1125)
            show midground awakening onlayer front at Position(ypos=1125)
            show hair awakened onlayer front at Position(ypos=1125)
            show dress felina onlayer front at Position(ypos=1125)
            show shifting smile talk onlayer front at Position(ypos=1125)
        else:
            hide felina onlayer inyourface
            hide felina onlayer back
            hide felina onlayer front
            show shifting smile talk onlayer front
        with dissolve
        mounds "You speak of me as if I am a ghost. But I am right in front of you.\n"
    if felina_violence_counter == 2:
        voice "audio/_pristine/voice/_climax/felina/_temp/16.flac"
        if come_from_tower:
            $ come_from_tower = False
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
            show farback quiet onlayer farback at Position(ypos=1125)
            show back awakening onlayer back at Position(ypos=1125)
            show midground awakening onlayer front at Position(ypos=1125)
            show hair awakened onlayer front at Position(ypos=1125)
            show dress felina onlayer front at Position(ypos=1125)
            show shifting serious talk onlayer front at Position(ypos=1125)
        else:
            hide felina onlayer inyourface
            hide felina onlayer back
            hide felina onlayer front
            show shifting serious talk onlayer front
        with dissolve
        mounds "Death is a fantasy. Only those who lack perspective see it as anything other than transformation. You cannot destroy me.\n"
    if felina_violence_counter == 3:
        voice "audio/_pristine/voice/_climax/felina/_temp/17.flac"
        if come_from_tower:
            $ come_from_tower = False
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
            show farback quiet onlayer farback at Position(ypos=1125)
            show back awakening onlayer back at Position(ypos=1125)
            show midground awakening onlayer front at Position(ypos=1125)
            show hair awakened onlayer front at Position(ypos=1125)
            show dress felina onlayer front at Position(ypos=1125)
            show shifting pissed talk onlayer front at Position(ypos=1125)
        else:
            hide felina onlayer inyourface
            hide felina onlayer back
            hide felina onlayer front
            show shifting pissed talk onlayer front
        with dissolve
        mounds "You have never truly seen me gone. You cannot fathom a world without me!\n"
    if felina_violence_counter == 4 and first_mound != "stranger":
        voice "audio/_pristine/voice/_climax/felina/_temp/18.flac"
        if come_from_tower:
            $ come_from_tower = False
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
            show farback quiet onlayer farback at Position(ypos=1125)
            show back awakening onlayer back at Position(ypos=1125)
            show midground awakening onlayer front at Position(ypos=1125)
            show hair awakened onlayer front at Position(ypos=1125)
            show dress felina onlayer front at Position(ypos=1125)
            show shifting serious talk onlayer front at Position(ypos=1125)
        else:
            hide felina onlayer inyourface
            hide felina onlayer back
            hide felina onlayer front
            show shifting serious talk onlayer front
        with dissolve
        mounds "The Echo was deluded. A world without me would be an eternal hell.\n"
    if felina_violence_counter == 5 or (felina_violence_counter == 4 and first_mound == "stranger"):

        jump felina_godkiller_ending

    jump felina_fight_staging

label felina_silence:
    $ felina_silence_count +=1
    play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
    if come_from_tower:
        $ come_from_tower = False
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
        show farback quiet onlayer farback at Position(ypos=1125)
        show back awakening onlayer back at Position(ypos=1125)
        show midground awakening onlayer front at Position(ypos=1125)
        show hair awakened onlayer front at Position(ypos=1125)
        show dress felina onlayer front at Position(ypos=1125)
        if felina_silence_count == 1 or felina_silence_count == 2:
            show shifting pissed onlayer front at Position(ypos=1125)
        elif felina_silence_count == 3:
            show shifting smile onlayer front at Position(ypos=1125)
        elif felina_silence_count == 4:
            show shifting martyrs onlayer front at Position(ypos=1125)
        else:
            show shifting smile onlayer front at Position(ypos=1125)
        with Dissolve(1.0)
    else:
        hide felina onlayer inyourface
        hide felina onlayer back
        hide felina onlayer front
        if felina_silence_count == 1 or felina_silence_count == 2:
            show shifting pissed onlayer front at Position(ypos=1125)
        elif felina_silence_count == 3:
            show shifting smile onlayer front at Position(ypos=1125)
        elif felina_silence_count == 4:
            show shifting martyrs onlayer front at Position(ypos=1125)
        else:
            show shifting smile onlayer front at Position(ypos=1125)
        with dissolve

    if felina_silence_count == 1:
        voice "audio/voices/felina/fight/1.flac"
        show shifting pissed talk onlayer front
        with dissolve
        mound "But you say nothing.\n"

    elif felina_silence_count == 2:
        voice "audio/voices/felina/fight/2.flac"
        show shifting pissed talk onlayer front
        with dissolve
        mound "And so your quietude continues.\n"

    elif felina_silence_count == 3:
        voice "audio/voices/felina/fight/3.flac"
        show shifting smile talk onlayer front
        mound "Is your unbroken silence a lack of an answer, or has your understanding begun to move beyond words?\n"

    elif felina_silence_count == 4:
        voice "audio/voices/felina/fight/4.flac"
        show shifting martyrs talk onlayer front
        mound "Still you hide the contours of your heart from me.\n"
        show shifting martyrs onlayer front

    elif felina_silence_count == 5:
        voice "audio/voices/felina/fight/5.flac"
        show shifting closed smile talk onlayer front
        with dissolve
        mound "Your stoicism knows no end.\n"

    jump felina_fight_staging

label felina_rejection_join:
    $ felina_rejection_count += 1
    $ felina_fight_effective_resistance += 1
    play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
    if come_from_tower:
        $ come_from_tower = False
        hide shifting onlayer front
        hide farback onlayer farback
        hide back onlayer back
        hide midground onlayer front
        hide hair onlayer front
        hide shifting onlayer front
        hide dress onlayer front
        hide felina onlayer front
        hide felina onlayer back
        hide felina onlayer inyourface
        show farback quiet onlayer farback at Position(ypos=1125)
        show back awakening onlayer back at Position(ypos=1125)
        show midground awakening onlayer front at Position(ypos=1125)
        show hair awakened onlayer front at Position(ypos=1125)
        show dress felina onlayer front at Position(ypos=1125)
        if felina_rejection_count == 1 or felina_rejection_count == 3:
            show shifting closed smile talk onlayer front at Position(ypos=1125)
        elif felina_rejection_count == 2:
            show shifting martyrs onlayer front at Position(ypos=1125)
        elif felina_rejection_count == 4:
            show shifting serious onlayer front at Position(ypos=1125)
        else:
            show shifting pissed onlayer front at Position(ypos=1125)
        with Dissolve(1.0)
    else:
        hide felina onlayer front
        hide felina onlayer inyourface
        hide felina onlayer back
        if felina_rejection_count == 1 or felina_rejection_count == 3:
            show shifting closed smile talk onlayer front at Position(ypos=1125)
        elif felina_rejection_count == 2:
            show shifting martyrs onlayer front at Position(ypos=1125)
        elif felina_rejection_count == 4:
            show shifting serious onlayer front at Position(ypos=1125)
        else:
            show shifting pissed onlayer front at Position(ypos=1125)
        with dissolve

    if felina_rejection_count == 1:
        voice "audio/voices/felina/fight/6.flac"
        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
        show shifting closed smile talk onlayer front
        mound "But violence has defined the flow of everything between us. Do not deny what we are, and do not color our conflict with fear.\n"

    elif felina_rejection_count == 3:
        voice "audio/voices/felina/fight/7.flac"
        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
        show shifting martyrs talk onlayer front
        mound "The Echo saw horrors because his eyes were closed. The majesty of being extends beyond any single perspective.\n"

    elif felina_rejection_count == 2:
        voice "audio/voices/felina/fight/8.flac"
        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
        show shifting closed smile talk onlayer front
        with dissolve
        mound "Their suffering is born of their own delusion.\n"

    elif felina_rejection_count == 4:
        voice "audio/voices/felina/fight/9.flac"
        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
        show shifting serious talk onlayer front
        mounds "I reject the narrow view of impermanence. I cling to nothing. There is no better us for us to be than us. We are reality itself.\n"

    elif felina_rejection_count == 5:
        voice "audio/voices/felina/fight/10.flac"
        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
        show shifting pissed talk onlayer front
        mounds "There has never been finality, there is only the unending transformation of my multitudes. But to destroy me is to bring everything to a stop. It is only then that you will have an ending, and that ending is nothingness.\n"
    jump felina_fight_staging

label felina_appeal_join:
    default felina_appeal_count = 0
    $ felina_appeal_count += 1
    $ felina_fight_effective_resistance += 1
    play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
    if come_from_tower:
        $ come_from_tower = False
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
        show farback quiet onlayer farback at Position(ypos=1125)
        show back awakening onlayer back at Position(ypos=1125)
        show midground awakening onlayer front at Position(ypos=1125)
        show hair awakened onlayer front at Position(ypos=1125)
        show dress felina onlayer front at Position(ypos=1125)
        if felina_appeal_count == 1:
            show shifting closed smile talk onlayer front at Position(ypos=1125)
        elif felina_appeal_count == 2:
            show shifting martyrs onlayer front at Position(ypos=1125)
        elif felina_appeal_count == 3:
            show shifting pose onlayer front at Position(ypos=1125)
        elif felina_appeal_count == 4:
            show shifting serious onlayer front at Position(ypos=1125)
        else:
            show shifting pissed onlayer front at Position(ypos=1125)
        with Dissolve(1.0)
    else:
        hide felina onlayer front
        hide felina onlayer inyourface
        hide felina onlayer back
        if felina_appeal_count == 1:
            show shifting closed smile talk onlayer front at Position(ypos=1125)
        elif felina_appeal_count == 2:
            show shifting martyrs onlayer front at Position(ypos=1125)
        elif felina_appeal_count == 3:
            show shifting pose onlayer front at Position(ypos=1125)
        elif felina_appeal_count == 4:
            show shifting serious onlayer front at Position(ypos=1125)
        else:
            show shifting pissed onlayer front at Position(ypos=1125)
        with dissolve

    if felina_appeal_count == 1:
        voice "audio/_pristine/voice/_climax/felina/1.flac"
        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
        show shifting closed smile talk onlayer front
        mound "Oh? Is it not? Perhaps you can enlighten me.\n"

    elif felina_appeal_count == 2:
        voice "audio/_pristine/voice/_climax/felina/2.flac"
        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
        show shifting martyrs talk onlayer front
        mound "You cling to your notion of pain as suffering. There is beauty in ugliness and love in conflict.\n"

    elif felina_appeal_count == 3:
        voice "audio/_pristine/voice/_climax/felina/3.flac"
        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
        show shifting pose talk onlayer front
        with dissolve
        mound "We {i}are{/i} the whole of reality.\n"

    elif felina_appeal_count == 4:
        voice "audio/_pristine/voice/_climax/felina/4a.flac"
        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
        show shifting serious talk onlayer front
        mound "I could ask you the same. There is only room for one of us to be blind here, and I know it to be you. We are each other's mirrors, and are we not divine?\n"

    elif felina_appeal_count == 5:
        voice "audio/_pristine/voice/_climax/felina/5a.flac"
        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
        show shifting pissed talk onlayer front
        mounds "Why would I stoop to your level when I am offering you ascension to mine?\n"
        voice "audio/_pristine/voice/_climax/felina/6.flac"
        show shifting martyrs talk onlayer front with dissolve
        mound "It's so peaceful here. Beautiful. Eternal, but ever-changing.\n"
    jump felina_fight_staging


label felina_lecture_join:
    default felina_lecture_count = 0
    $ felina_lecture_count += 1

    play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
    if come_from_tower:
        $ come_from_tower = False
        hide felina onlayer front
        hide shifting onlayer front
        hide farback onlayer farback
        hide back onlayer back
        hide midground onlayer front
        hide hair onlayer front
        hide shifting onlayer front
        hide dress onlayer front
        hide felina onlayer back
        hide felina onlayer inyourface
        show farback quiet onlayer farback at Position(ypos=1125)
        show back awakening onlayer back at Position(ypos=1125)
        show midground awakening onlayer front at Position(ypos=1125)
        show hair awakened onlayer front at Position(ypos=1125)
        show dress felina onlayer front at Position(ypos=1125)
        if felina_lecture_count == 1 or felina_lecture_count == 3:
            show shifting closed smile talk onlayer front at Position(ypos=1125)
        elif felina_lecture_count == 2:
            show shifting martyrs onlayer front at Position(ypos=1125)
        elif felina_lecture_count == 4:
            show shifting smile onlayer front at Position(ypos=1125)
        else:
            show shifting pissed onlayer front at Position(ypos=1125)
        with Dissolve(1.0)
    else:
        hide felina onlayer front
        hide felina onlayer inyourface
        hide felina onlayer back
        if felina_lecture_count == 1 or felina_lecture_count == 3:
            show shifting closed smile talk onlayer front at Position(ypos=1125)
        elif felina_lecture_count == 2:
            show shifting martyrs onlayer front at Position(ypos=1125)
        elif felina_lecture_count == 4:
            show shifting smile onlayer front at Position(ypos=1125)
        else:
            show shifting pissed onlayer front at Position(ypos=1125)
        with dissolve

    if felina_lecture_count == 1:
        $ felina_fight_effective_resistance += 1
        voice "audio/_pristine/voice/_climax/felina/7.flac"
        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
        show shifting closed smile talk onlayer front
        mound "What you mistake for lecture is merely observation. I only want to help you.\n"
        voice "audio/_pristine/voice/_climax/felina/8a.flac"
        show shifting smile talk onlayer front with dissolve
        mound "You can vainly struggle against me, or you can follow the rhythm of our movement and find our freedom.\n"

    elif felina_lecture_count == 2:
        $ felina_fight_effective_resistance += 1
        voice "audio/_pristine/voice/_climax/felina/9.flac"
        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
        show shifting martyrs talk onlayer front
        mound "If my words feel meaningless, it's because words are meaningless! If it feels as though I lecture you from above, it is merely because you have refused to climb after me and find where you belong.\n"

    elif felina_lecture_count == 3:
        voice "audio/_pristine/voice/_climax/felina/10a.flac"
        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
        show shifting closed smile talk onlayer front
        with dissolve
        mound "The only universal truth is that there are no universal truths! There is only you and me, existing in relation to the other.\n"
        voice "audio/_pristine/voice/_climax/felina/11.flac"
        show shifting serious talk onlayer front with dissolve
        mounds "And I will not stop our dance until you understand.\n"

    elif felina_lecture_count == 4:
        voice "audio/_pristine/voice/_climax/felina/12.flac"
        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
        show shifting smile talk onlayer front
        mound "They are mere fragments of a whole. They bought into delusion because none of them were able to see past themselves.\n"

    elif felina_lecture_count == 5:
        voice "audio/_pristine/voice/_climax/felina/13a.flac"
        show shifting pissed talk onlayer front
        mound "You cling to things that never truly existed. If it takes all of eternity to break your grip on petty, fickle, fleeting selves, both mine and yours...\n"
        voice "audio/_pristine/voice/_climax/felina/14.flac"
        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
        show shifting serious talk onlayer front with dissolve
        mounds "Then I will break it.\n"
    jump felina_fight_staging


label felina_assert_join:
    default felina_assert_count = 0
    default felina_assert_lethal = False
    $ felina_assert_count += 1

    play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
    if come_from_tower:
        $ come_from_tower = False
        hide felina onlayer front
        hide shifting onlayer front
        hide farback onlayer farback
        hide back onlayer back
        hide midground onlayer front
        hide hair onlayer front
        hide shifting onlayer front
        hide dress onlayer front
        hide felina onlayer back
        show farback quiet onlayer farback at Position(ypos=1125)
        show back awakening onlayer back at Position(ypos=1125)
        show midground awakening onlayer front at Position(ypos=1125)
        show hair awakened onlayer front at Position(ypos=1125)
        show dress felina onlayer front at Position(ypos=1125)
        if felina_assert_count == 1:
            show shifting pity smile talk onlayer front at Position(ypos=1125)
        elif felina_assert_count == 2:
            show shifting closed smile talk onlayer front at Position(ypos=1125)
        elif felina_assert_count == 3:
            show shifting pissed talk onlayer front at Position(ypos=1125)
        elif felina_assert_count == 4:
            show shifting serious onlayer front at Position(ypos=1125)
        else:
            show shifting pissed onlayer front at Position(ypos=1125)
        with Dissolve(1.0)
    else:
        hide felina onlayer front
        hide felina onlayer inyourface
        hide felina onlayer back
        if felina_assert_count == 1:
            show shifting pity smile talk onlayer front at Position(ypos=1125)
        elif felina_assert_count == 2:
            show shifting closed smile talk onlayer front at Position(ypos=1125)
        elif felina_assert_count == 3:
            show shifting pissed talk onlayer front at Position(ypos=1125)
        elif felina_assert_count == 4:
            show shifting serious onlayer front at Position(ypos=1125)
        else:
            show shifting pissed onlayer front at Position(ypos=1125)
        with dissolve

    if felina_assert_count == 1:
        $ felina_fight_effective_resistance += 1
        voice "audio/_pristine/voice/_climax/felina/extra1.flac"
        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
        show shifting pity smile talk onlayer front
        mound "Have you? Or is what you think of as independence merely an illusion? Without me, you can have no contrast. And without contrast, you have no shape.\n"

    elif felina_assert_count == 2:
        $ felina_fight_effective_resistance += 1
        voice "audio/_pristine/voice/_climax/felina/extra2.flac"
        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
        show shifting closed smile talk onlayer front at Position(ypos=1125)
        mound "Time you've spent away from me is still time spent in reference to me. Even then, both of us are more than our bodies. Am I not in the trees? Am I not in the cabin? Am I not in you?\n"

    elif felina_assert_count == 3:
        voice "audio/_pristine/voice/_climax/felina/extra3.flac"
        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
        show shifting pissed talk onlayer front
        with dissolve
        mound "You place far too much trust into the ravings of a fearful ignorant soul who overstepped his bounds.\n"

    elif felina_assert_count == 4:
        voice "audio/_pristine/voice/_climax/felina/extra4.flac"
        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
        show shifting serious talk onlayer front
        mound "Intent is nothing. Wisdom is everything. I turn the wheel because suffering is a falsehood. A delusion. It is up to the world to free itself of it.\n"
        voice "audio/_pristine/voice/_climax/felina/extra5.flac"
        show shifting pity smile talk onlayer front
        with dissolve
        mound "Would you plunge yourself into a cold and empty eternity on faith alone? Would you destroy the only other thing like you to save a world you've never seen?\n"

    elif felina_assert_count == 5:
        if felina_assert_lethal:
            voice "audio/_pristine/voice/_climax/felina/extra6.flac"
            play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
            show shifting pissed talk onlayer front
            mounds "And if I need to spend all of eternity to stop you, then I will gladly do so.\n"
        else:
            voice "audio/_pristine/voice/_climax/felina/extra7.flac"
            play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
            show shifting pissed talk onlayer front
            mounds "If I need to spend all of eternity to show you the error of your ways, then I will gladly do so.\n"
    jump felina_fight_staging



label felina_adversary_start:

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
        show pop adversary onlayer inyourface at shakeshort, Position(ypos=1125)
    else:
        $ previous_transform = "danceflip"
        show shifting dance onlayer front at flip, shakeshort, Position(ypos=1125)
        show pop adversary onlayer inyourface at flip, shakeshort, Position(ypos=1125)
    with Dissolve(0.25)
    $ renpy.pause(1.45)

    $ gallery_adversary.unlock_item(20)
    $ renpy.save_persistent()
    play audio "audio/final/Adversary_ABackAndForth_1.flac"
    show fight adversary onlayer inyourface at Position(ypos=1125)
    $ renpy.pause(0.01)

    voice "audio/voices/felina/fight/adv1a.flac"
    mounds "The sensation of bleeding and sweating and breaking and mending and dying and living comes back in vivid color.\n"
    voice "audio/voices/felina/fight/adv2.flac"
    hide fight onlayer inyourface
    hide shifting onlayer front
    hide pop onlayer inyourface
    show farback quiet onlayer farback at Position(ypos=1125)
    show back awakening onlayer back at Position(ypos=1125)
    show midground awakening onlayer front at Position(ypos=1125)
    show hair awakened onlayer front at Position(ypos=1125)
    show dress felina onlayer front at Position(ypos=1125)
    show shifting pose talk onlayer front at Position(ypos=1125)
    show felina adversary2 onlayer inyourface at Position(ypos=1125)
    with Dissolve(1.0)
    mounds "You feel the shame of a hundred deaths and the pride of a hundred conquests, all of the peaks and valleys weaving themselves into a single tapestry free of beginning and free of end.\n"
    voice "audio/voices/felina/fight/adv3.flac"
    show shifting martyrs talk onlayer front
    show felina adversary3 onlayer inyourface
    with dissolve
    mound "Do you remember when we killed each other with such fervent passion that death itself no longer sat on our shoulders?\n"
    show shifting martyrs onlayer front
    label felina_adversary_menu:
        menu:
            extend ""

            "{i}• (Explore) [[Address this vessel's statement directly.]{/i}":
                menu:
                    extend ""

                    "{i}• ''It was beautiful.''{/i}":
                        voice "audio/voices/felina/fight/adv4.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        hide felina onlayer inyourface
                        show shifting pity smile talk onlayer front
                        with dissolve
                        mound "It was. Triumph does not exist without defeat. Birth does not exist without death. It is through conflict that we create beauty.\n"

                    "{i}• ''It was meaningless. Neither of us could ever truly win.''{/i}":
                        voice "audio/voices/felina/fight/adv5.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        hide felina onlayer inyourface
                        show shifting pissed talk onlayer front
                        with dissolve
                        mound "So bleakly nihilistic. Is death the end, or is it the birth of something new? If you cannot find meaning in living, how will you find meaning if you strip me from existence?\n"

                    "{i}• ''It was unnecessary. We could have worked together to build something better.''{/i}":
                        $ felina_fight_effective_resistance += 1
                        voice "audio/voices/felina/fight/adv6.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        hide felina onlayer inyourface
                        show shifting closed smile talk onlayer front
                        with dissolve
                        mound "But for us, that was better.\n"
                        jump felina_adversary_negative_join

                    "{i}• ''We didn't have to hurt each other.''{/i}":
                        $ felina_fight_effective_resistance += 1
                        voice "audio/voices/felina/fight/adv7.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        hide felina onlayer inyourface
                        show shifting pissed talk onlayer front
                        with dissolve
                        mound "Did we hurt each other?\n"
                        label felina_adversary_negative_join:
                            voice "audio/voices/felina/fight/adv8a.flac"
                            show shifting pity smile talk onlayer front
                            with dissolve
                            mound "For me there was no better end. I lost myself in an artistry so profound that it lifted both of us into something greater.\n"

                    "{i}• (Return){/i}":
                        jump felina_adversary_menu

            "{i}• [[Appeal to your shared humanity.] ''You speak about life and death and change and stagnation, but that isn't what any of this has been about.''{/i}" if felina_appeal_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''This has always just been about us. Two people forced to hurt each other again and again and again. But we don't have to hurt each other anymore.''{/i}" if felina_appeal_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''There can be love and conflict and beauty and ugliness between us without bringing the whole of reality into the picture.''{/i}" if felina_appeal_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''We're not the whole of reality. Why won't you see me the way I still see you? Why won't you see me for what I am?''{/i}" if felina_appeal_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''This doesn't have to be so big. You can come back down to my level. You can come back to me.''{/i}" if felina_appeal_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Reject her authority.] ''You've done nothing but lecture me since the minute I got here.''{/i}" if felina_lecture_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''You use all these pretentious metaphors and pretend you're making grand proclamations about who I am and who you are. But really you aren't saying much of anything.''{/i}" if felina_lecture_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''It doesn't even matter what I say to you, because you're just going to keep telling me your perspective like it's some universal truth.''{/i}" if felina_lecture_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''It was so much better when I was with your vessels. Even at their worst, they all still heard me.''{/i}" if felina_lecture_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''I don't know what you are, but you aren't any of them. You're just something wearing their skin.''{/i}" if felina_lecture_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Argue your independence.] ''You act as though the world can't exist without you. But I've existed without you.''{/i}" if felina_assert_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''What are the woods, then? What is the cabin? What is the time we've spent apart if not me existing as myself?''{/i}" if felina_assert_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''I wouldn't be here if destroying you would leave all of reality a colorless blur.''{/i}" if felina_assert_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''I'd rather trust an ignorant soul who died trying to make things better than a god who'd let the wheel of suffering turn forever.''{/i}" if felina_assert_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''If I need to destroy you to build a better world, then I will.''{/i}" if felina_assert_count == 4:
                $ felina_assert_lethal = True
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''Who said anything about destroying you? I just need to make you stop.''{/i}" if felina_assert_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Reject her perspective.] ''I won't engage with violence.''{/i}" if felina_rejection_count == 0:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''It doesn't matter how I feel. Death, suffering, and oblivion shouldn't fall on others. If we are able to transcend death, then we are responsible for those it holds captive.''{/i}" if felina_rejection_count == 1:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''Suffering born in delusion is still suffering. It doesn't matter what we are now. We hurt each other, and we shouldn't have done that. We cannot let a world be spun out of that pain.''{/i}" if felina_rejection_count == 2:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''You reject the suffering of material reality, and yet you cling to its framework for meaning. We can be better than this.''{/i}" if felina_rejection_count == 3:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''You claim your destruction would steal meaning from existence, but if my actions can make existence worse, then there must be actions that make it better. Perfection implies finality, and nothing is final.''{/i}" if felina_rejection_count == 4:
                jump felina_rejection_join

            "{i}• ''I get it. There's no need for us to keep fighting. I'll leave with you. I just don't know how.'' [[Stop the fight early and surrender.]{/i}" if felina_round >= 2:
                $ achievement.grant("ACH_END_FREE2")
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_freedom_join

            "{i}• [[Remain silent.]{/i}":
                #mound "Triumph does not exist without defeat. Birth does not exist without death.\n"
                jump felina_silence

    jump felina_fight_staging

label felina_adversary2_start:

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
        show pop needle onlayer inyourface at shakeshort, Position(ypos=1125)
    else:
        $ previous_transform = "fierceflip"
        show shifting fierce onlayer front at flip, shakeshort, Position(ypos=1125)
        show pop needle onlayer inyourface at flip, shakeshort, Position(ypos=1125)
    with Dissolve(0.25)
    $ renpy.pause(1.3)

    $ gallery_needle.unlock_item(20)
    $ renpy.save_persistent()
    play audio "audio/final/Adversary_HandThroughChest_2.flac"
    if adversary_2_blade_taken:
        show fight needle knife onlayer inyourface at Position(ypos=1125)
    else:
        show fight needle unarmed onlayer inyourface at Position(ypos=1125)
    $ renpy.pause(0.01)
    voice "audio/_pristine/voice/_climax/felina/85.flac"
    mounds "I crush you, I bleed you, I grind you to paste. My scars are a memory of what you used to be to me. I want those feelings back.\n"
    if adversary_2_end == "fight_fail":
        voice "audio/_pristine/voice/_climax/felina/89a.flac"
        hide fight onlayer inyourface
        hide shifting onlayer front
        hide pop onlayer inyourface
        show farback quiet onlayer farback at Position(ypos=1125)
        show back awakening onlayer back at Position(ypos=1125)
        show midground awakening onlayer front at Position(ypos=1125)
        show hair awakened onlayer front at Position(ypos=1125)
        show dress felina onlayer front at Position(ypos=1125)
        show shifting pissed talk onlayer front at Position(ypos=1125)
        show felina needle1 onlayer inyourface at Position(ypos=1125)
        with Dissolve(1.0)
        mound "You fight, but you fight as a shadow. I crush you because I have to. Because there is no honesty in mercy.\n"
        jump needle_join_fail_join

    if adversary_2_end == "fight_succeed":
        voice "audio/_pristine/voice/_climax/felina/86a.flac"
        hide fight onlayer inyourface
        hide shifting onlayer front
        hide pop onlayer inyourface
        show farback quiet onlayer farback at Position(ypos=1125)
        show back awakening onlayer back at Position(ypos=1125)
        show midground awakening onlayer front at Position(ypos=1125)
        show hair awakened onlayer front at Position(ypos=1125)
        show dress felina onlayer front at Position(ypos=1125)
        show shifting martyrs talk onlayer front at Position(ypos=1125)
        show felina needle3 onlayer inyourface at Position(ypos=1125)
        with Dissolve(1.0)
        mound "You run but you do not run away. You take me somewhere new. Somewhere we can dance like we used to. But I could not follow your steps.\n"
        voice "audio/_pristine/voice/_climax/felina/87.flac"
        show shifting pity smile talk onlayer front
        show felina needle1 onlayer inyourface
        with dissolve
        mound "There was no better gift for me than the gift of defeat. You showed me how much more I could be.\n"
        voice "audio/_pristine/voice/_climax/felina/88.flac"
        show shifting serious talk onlayer front
        show felina needle3 onlayer inyourface
        with dissolve
        mound "We made each other better. To have no challenge is to fade into nothing. A life without obstacles is no life at all.\n"
        show shifting serious onlayer front

    if adversary_2_end == "flee_fail":
        voice "audio/_pristine/voice/_climax/felina/90.flac"
        hide fight onlayer inyourface
        hide shifting onlayer front
        hide pop onlayer inyourface
        show farback quiet onlayer farback at Position(ypos=1125)
        show back awakening onlayer back at Position(ypos=1125)
        show midground awakening onlayer front at Position(ypos=1125)
        show hair awakened onlayer front at Position(ypos=1125)
        show dress felina onlayer front at Position(ypos=1125)
        show shifting pissed talk onlayer front at Position(ypos=1125)
        show felina needle1 onlayer inyourface at Position(ypos=1125)
        with Dissolve(1.0)
        mound "You run, but you don't run far. I crush you because I have to. Because there is no honesty in mercy.\n"
        label needle_join_fail_join:
            voice "audio/_pristine/voice/_climax/felina/91.flac"
            show shifting martyrs talk onlayer front
            show felina needle2 talk onlayer inyourface
            with dissolve
            mound "Who lost and who won when you entered my cave? You died on the floor, but my soul wept in ways your body couldn't.\n"
            #voice "audio/_pristine/voice/_climax/felina/92.flac"
            #show shifting serious talk onlayer front
            #show felina needle3 onlayer inyourface
            #with dissolve
            #mound "To have no challenge is to fade into nothing. A life without obstacles is no life at all.\n"
            #show shifting serious onlayer front
            voice "audio/voices/felina/fight/eye8.flac"
            show shifting pity smile talk onlayer front
            show felina needle3 onlayer inyourface
            with dissolve
            mound "But in the disappointment of my victory, you gave me a new challenge to face within myself. Without obstacles to overcome we stagnate into nothing.\n"
            show shifting pity smile onlayer front

    if adversary_2_end == "free":
        voice "audio/_pristine/voice/_climax/felina/93.flac"
        hide fight onlayer inyourface
        hide shifting onlayer front
        hide pop onlayer inyourface
        show farback quiet onlayer farback at Position(ypos=1125)
        show back awakening onlayer back at Position(ypos=1125)
        show midground awakening onlayer front at Position(ypos=1125)
        show hair awakened onlayer front at Position(ypos=1125)
        show dress felina onlayer front at Position(ypos=1125)
        show shifting martyrs talk onlayer front at Position(ypos=1125)
        show felina needle1 onlayer inyourface at Position(ypos=1125)
        with Dissolve(1.0)
        mound "You run, and you run far. And the flesh I hurl at you is answered by the empty air of a place I'd never been. Cold and lonely, but also true.\n"
        voice "audio/_pristine/voice/_climax/felina/94.flac"
        show shifting closed smile talk onlayer front
        show felina needle2 talk onlayer inyourface
        with dissolve
        mound "I didn't know what to make of my freedom then, but I know what to make of it now.\n"
        voice "audio/_pristine/voice/_climax/felina/95.flac"
        show shifting pity smile talk onlayer front
        show felina needle3 onlayer inyourface
        with dissolve
        mound "You challenged me, and by challenging me you gave me purpose. A life without obstacles is no life at all.\n"
        show shifting pity smile onlayer front

    label felina_needle_menu:
        menu:
            extend ""

            "{i}{outlinecolor=4f1313}• ''I remember the moment of my victory. As soon as you entered my domain I destroyed you.''{/outlinecolor}{/i}" if adversary_2_end == "fight_succeed":
                jump felina_violence_join

            "{i}• (Explore) [[Address this vessel's statement directly.]{/i}":
                menu:
                    extend ""

                    "{i}• ''We've both become better for what we've been through, haven't we?''{/i}":
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        voice "audio/voices/felina/fight/eye12.flac"
                        hide felina onlayer inyourface
                        show shifting smile talk onlayer front
                        with dissolve
                        mound "We have. Look at what we are now, and see how small we were then.\n"

                    "{i}• ''Not all obstacles are equal. Can meaning not exist in the absence of cruelty and pain?''{/i}":
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        $ felina_fight_effective_resistance += 1
                        voice "audio/_pristine/voice/_climax/felina/96.flac"
                        show shifting pissed talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "To lose me is to remain the same. What meaning can be taken from a single moment frozen in time?\n"
                        show shifting pissed onlayer front
                        jump felina_adversary_2_join

                    "{i}• ''I fought you to protect others, not to better myself.''{/i}" if adversary_2_end == "fight_succeed" or adversary_2_end == "fight_fail":
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        voice "audio/voices/felina/fight/eye14.flac"
                        hide felina onlayer inyourface
                        with dissolve
                        show shifting closed smile talk onlayer front
                        mound "And yet you changed regardless. Your perspective widened.\n"

                    "{i}• ''I refused to fight you because I rejected what you desired. Obstacles don't need to take the form of bloody fists.''{/i}" if adversary_2_end == "free" or adversary_2_end == "flee_fail":
                        $ felina_fight_effective_resistance += 1
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        voice "audio/voices/felina/fight/eye15.flac"
                        show shifting closed smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "A rejection of conflict is still conflict. There is no such thing as non-engagement. To refuse a choice is still to make a decision.\n"
                        label felina_adversary_2_join:
                            voice "audio/voices/felina/fight/eye16.flac"
                            show shifting smile talk onlayer front
                            with dissolve
                            mound "All conflict is violence, but to remove conflict itself is to remove the textures that define us.\n"
                            show shifting smile onlayer front

                    "{i}• (Return){/i}":
                        jump felina_needle_menu

            "{i}• [[Appeal to your shared humanity.] ''You speak about life and death and change and stagnation, but that isn't what any of this has been about.''{/i}" if felina_appeal_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''This has always just been about us. Two people forced to hurt each other again and again and again. But we don't have to hurt each other anymore.''{/i}" if felina_appeal_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''There can be love and conflict and beauty and ugliness between us without bringing the whole of reality into the picture.''{/i}" if felina_appeal_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''We're not the whole of reality. Why won't you see me the way I still see you? Why won't you see me for what I am?''{/i}" if felina_appeal_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''This doesn't have to be so big. You can come back down to my level. You can come back to me.''{/i}" if felina_appeal_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Reject her authority.] ''You've done nothing but lecture me since the minute I got here.''{/i}" if felina_lecture_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''You use all these pretentious metaphors and pretend you're making grand proclamations about who I am and who you are. But really you aren't saying much of anything.''{/i}" if felina_lecture_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''It doesn't even matter what I say to you, because you're just going to keep telling me your perspective like it's some universal truth.''{/i}" if felina_lecture_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''It was so much better when I was with your vessels. Even at their worst, they all still heard me.''{/i}" if felina_lecture_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''I don't know what you are, but you aren't any of them. You're just something wearing their skin.''{/i}" if felina_lecture_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Argue your independence.] ''You act as though the world can't exist without you. But I've existed without you.''{/i}" if felina_assert_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''What are the woods, then? What is the cabin? What is the time we've spent apart if not me existing as myself?''{/i}" if felina_assert_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''I wouldn't be here if destroying you would leave all of reality a colorless blur.''{/i}" if felina_assert_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''I'd rather trust an ignorant soul who died trying to make things better than a god who'd let the wheel of suffering turn forever.''{/i}" if felina_assert_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''If I need to destroy you to build a better world, then I will.''{/i}" if felina_assert_count == 4:
                $ felina_assert_lethal = True
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''Who said anything about destroying you? I just need to make you stop.''{/i}" if felina_assert_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Reject her perspective.] ''I won't engage with violence.''{/i}" if felina_rejection_count == 0:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''It doesn't matter how I feel. Death, suffering, and oblivion shouldn't fall on others. If we are able to transcend death, then we are responsible for those it holds captive.''{/i}" if felina_rejection_count == 1:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''Suffering born in delusion is still suffering. It doesn't matter what we are now. We hurt each other, and we shouldn't have done that. We cannot let a world be spun out of that pain.''{/i}" if felina_rejection_count == 2:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''You reject the suffering of material reality, and yet you cling to its framework for meaning. We can be better than this.''{/i}" if felina_rejection_count == 3:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''You claim your destruction would steal meaning from existence, but if my actions can make existence worse, then there must be actions that make it better. Perfection implies finality, and nothing is final.''{/i}" if felina_rejection_count == 4:
                jump felina_rejection_join

            "{i}• ''I get it. There's no need for us to keep fighting. I'll leave with you. I just don't know how.'' [[Stop the fight early and surrender.]{/i}" if felina_round >= 2:
                $ achievement.grant("ACH_END_FREE2")
                jump felina_freedom_join

            "{i}• [[Remain silent.]{/i}":
                jump felina_silence

    jump felina_fight_staging

label felina_beast_start:

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
        show pop beast onlayer inyourface at shakeshort, Position(ypos=1125)
    else:
        $ previous_transform = "fierceflip"
        show shifting fierce onlayer front at flip, shakeshort, Position(ypos=1125)
        show pop beast onlayer inyourface at flip, shakeshort, Position(ypos=1125)
    with Dissolve(0.25)
    $ renpy.pause(1.3)

    $ gallery_beast.unlock_item(17)
    $ renpy.save_persistent()
    play audio "audio/final/Beast_AcidSizzle_1.flac"
    show fight beast puke onlayer inyourface at Position(ypos=1125)
    $ renpy.pause(0.01)

    voice "audio/voices/felina/fight/beast1.flac"
    mounds "You are devoured, prey for something bigger than you that stalks and slinks in shadows. Within, you are tightly bound and choke on heavy air as acid burns its way into your pores. A nest of things devouring within things devouring.\n"
    voice "audio/voices/felina/fight/beast2.flac"
    hide fight onlayer inyourface
    hide shifting onlayer front
    hide pop onlayer inyourface
    show farback quiet onlayer farback at Position(ypos=1125)
    show back awakening onlayer back at Position(ypos=1125)
    show midground awakening onlayer front at Position(ypos=1125)
    show hair awakened onlayer front at Position(ypos=1125)
    show dress felina onlayer front at Position(ypos=1125)
    show shifting martyrs talk onlayer front at Position(ypos=1125)
    show felina beast3 onlayer inyourface at Position(ypos=1125)
    with Dissolve(1.0)
    mound "But even when dissolved, you gifted me a life. Perhaps it was fear that drove you. Perhaps it was compassion.\n"
    voice "audio/voices/felina/fight/beast3a.flac"
    show shifting serious talk onlayer front
    show felina beast2 talk onlayer inyourface
    with dissolve
    mound "But the outcome of an act matters more than its intentions. There is a natural order to the cycle of things sustaining things.\n"
    voice "audio/voices/felina/fight/beast4.flac"
    show shifting closed smile talk onlayer front
    show felina beast1 onlayer inyourface
    with dissolve
    mound "A world without sustenance is a world without relationships, and it is our relationships that give us form and substance.\n"

    label felina_beast_menu:
        menu:
            extend ""

            "{i}• (Explore) [[Address this vessel's statement directly.]{/i}":
                menu:
                    extend ""

                    "{i}• ''You're right. Without desire, we have no need for relationships. We would all be alone.''{/i}":
                        voice "audio/voices/felina/fight/beast5.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting pity smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "And it is through those desires that each of us found the other. And it is through each other that we will find our freedom.\n"
                        show shifting pity smile onlayer front

                    "{i}• ''Yes, without desire, we have no need for relationships — we would all be alone. But if we had no desires, would being alone be so bad?''{/i}":
                        $ felina_fight_effective_resistance += 1
                        voice "audio/voices/felina/fight/beast6.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        hide felina onlayer inyourface
                        with dissolve
                        mound "You seek to remove complexity itself, but it is complexity that adds color to experience.\n"

                    "{i}• ''You cannot use eating me to prove that you're right.''{/i}":
                        voice "audio/voices/felina/fight/beast7.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting pissed talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "You still cling to the horror of dying bodies that rot worlds apart from us. How many more vessels would you need to lose before you realize their irrelevance?\n"
                        show shifting pissed onlayer front

                    "{i}• ''But my intentions do matter. I only freed you to save myself.''{/i}":
                        jump felina_beast_join

                    "{i}• ''I didn't want to free you. You tricked me. I just wanted to not be eaten.''{/i}" if beast_accidental_freedom:
                        label felina_beast_join:
                            play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                            voice "audio/voices/felina/fight/beast8.flac"
                            show shifting pity smile talk onlayer front
                            hide felina onlayer inyourface
                            with dissolve
                            mound "And yet our conflicting desires liberated us both, and now we are here, so much more than we ever could have imagined.\n"

                    "{i}• (Return){/i}":
                        jump felina_beast_menu

            "{i}• [[Appeal to your shared humanity.] ''You speak about life and death and change and stagnation, but that isn't what any of this has been about.''{/i}" if felina_appeal_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''This has always just been about us. Two people forced to hurt each other again and again and again. But we don't have to hurt each other anymore.''{/i}" if felina_appeal_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''There can be love and conflict and beauty and ugliness between us without bringing the whole of reality into the picture.''{/i}" if felina_appeal_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''We're not the whole of reality. Why won't you see me the way I still see you? Why won't you see me for what I am?''{/i}" if felina_appeal_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''This doesn't have to be so big. You can come back down to my level. You can come back to me.''{/i}" if felina_appeal_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Reject her authority.] ''You've done nothing but lecture me since the minute I got here.''{/i}" if felina_lecture_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''You use all these pretentious metaphors and pretend you're making grand proclamations about who I am and who you are. But really you aren't saying much of anything.''{/i}" if felina_lecture_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''It doesn't even matter what I say to you, because you're just going to keep telling me your perspective like it's some universal truth.''{/i}" if felina_lecture_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''It was so much better when I was with your vessels. Even at their worst, they all still heard me.''{/i}" if felina_lecture_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''I don't know what you are, but you aren't any of them. You're just something wearing their skin.''{/i}" if felina_lecture_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Argue your independence.] ''You act as though the world can't exist without you. But I've existed without you.''{/i}" if felina_assert_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''What are the woods, then? What is the cabin? What is the time we've spent apart if not me existing as myself?''{/i}" if felina_assert_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''I wouldn't be here if destroying you would leave all of reality a colorless blur.''{/i}" if felina_assert_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''I'd rather trust an ignorant soul who died trying to make things better than a god who'd let the wheel of suffering turn forever.''{/i}" if felina_assert_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''If I need to destroy you to build a better world, then I will.''{/i}" if felina_assert_count == 4:
                $ felina_assert_lethal = True
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''Who said anything about destroying you? I just need to make you stop.''{/i}" if felina_assert_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Reject her perspective.] ''I won't engage with violence.''{/i}" if felina_rejection_count == 0:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''It doesn't matter how I feel. Death, suffering, and oblivion shouldn't fall on others. If we are able to transcend death, then we are responsible for those it holds captive.''{/i}" if felina_rejection_count == 1:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''Suffering born in delusion is still suffering. It doesn't matter what we are now. We hurt each other, and we shouldn't have done that. We cannot let a world be spun out of that pain.''{/i}" if felina_rejection_count == 2:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''You reject the suffering of material reality, and yet you cling to its framework for meaning. We can be better than this.''{/i}" if felina_rejection_count == 3:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''You claim your destruction would steal meaning from existence, but if my actions can make existence worse, then there must be actions that make it better. Perfection implies finality, and nothing is final.''{/i}" if felina_rejection_count == 4:
                jump felina_rejection_join

            "{i}• ''I get it. There's no need for us to keep fighting. I'll leave with you. I just don't know how.'' [[Stop the fight early and surrender.]{/i}" if felina_round >= 2:
                $ achievement.grant("ACH_END_FREE2")
                jump felina_freedom_join

            "{i}• [[Remain silent.]{/i}":
                jump felina_silence

    jump felina_fight_staging

label felina_beast2_start:

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
        show pop den onlayer inyourface at shakeshort, Position(ypos=1125)
    else:
        $ previous_transform = "fierceflip"
        show shifting fierce onlayer front at flip, shakeshort, Position(ypos=1125)
        show pop den onlayer inyourface at flip, shakeshort, Position(ypos=1125)
    with Dissolve(0.25)
    $ renpy.pause(1.3)
    $ gallery_den.unlock_item(20)
    $ renpy.save_persistent()
    if beast_2_end == "fight_succeed" or beast_2_end == "fight_fail":
        play audio "audio/final/Witch_ClawsRipWet_4.flac"
        show fight den attack onlayer inyourface at Position(ypos=1125)
        $ renpy.pause(0.01)
    else:
        if beast_2_end == "consume":
            play audio "audio/final/Witch_ClawsRipWet_4.flac"
            show fight den merge onlayer inyourface at Position(ypos=1125)
            $ renpy.pause(0.01)
        elif beast_2_end == "starve":
            play audio "audio/one_shot/blood_drip.flac"
            show fight den starve onlayer inyourface at Position(ypos=1125)
            $ renpy.pause(0.01)
        elif beast_2_end == "free_succeed":
            play audio "audio/one_shot/blood_drip.flac"
            show fight den trapped offer onlayer inyourface at Position(ypos=1125)
            $ renpy.pause(0.01)
        else:
            play audio "audio/one_shot/knife_pickup.flac"
            show fight den attack onlayer inyourface at Position(ypos=1125)
            $ renpy.pause(0.01)

    #voice "audio/voices/felina/fight/den1.flac"
    #mounds "You are devoured, prey for something bigger than you that stalks and slinks in shadows. But even after the pain of defeat, you returned.\n"
    voice "audio/_pristine/voice/_climax/felina/_temp/20.flac"
    mounds "You are devoured, prey for something bigger than you that stalks and slinks in shadows.\n"
    if beast_2_end == "fight_succeed" or beast_2_end == "consume" or beast_2_end == "slay":
        if beast_2_end == "fight_succeed" or beast_2_end == "slay":
            voice "audio/_pristine/voice/den/mound/3.flac"
        elif beast_2_end == "consume":
            voice "audio/_pristine/voice/den/mound/4.flac"
        hide fight onlayer inyourface
        hide shifting onlayer front
        hide pop onlayer inyourface
        show farback quiet onlayer farback at Position(ypos=1125)
        show back awakening onlayer back at Position(ypos=1125)
        show midground awakening onlayer front at Position(ypos=1125)
        show hair awakened onlayer front at Position(ypos=1125)
        show dress felina onlayer front at Position(ypos=1125)
        show shifting pity smile talk onlayer front at Position(ypos=1125)
        show felina den1 onlayer inyourface at Position(ypos=1125)
        with Dissolve(1.0)
        if beast_2_end == "fight_succeed" or beast_2_end == "slay":
            mounds "But we had a dance unfinished, and in the pitch black of the earth, we found it, at the tips of claws and the edge of blades.\n"
        else:
            mounds "But we had a dance unfinished, and in the pitch black of the earth, we found it. A ravenous symphony of death and rebirth.\n"
    if beast_2_end == "starve":
        voice "audio/_pristine/voice/den/mound/1.flac"
        hide fight onlayer inyourface
        hide shifting onlayer front
        hide pop onlayer inyourface
        show farback quiet onlayer farback at Position(ypos=1125)
        show back awakening onlayer back at Position(ypos=1125)
        show midground awakening onlayer front at Position(ypos=1125)
        show hair awakened onlayer front at Position(ypos=1125)
        show dress felina onlayer front at Position(ypos=1125)
        show shifting martyrs talk onlayer front at Position(ypos=1125)
        show felina den1 onlayer inyourface at Position(ypos=1125)
        with Dissolve(1.0)
        mounds "But we had a dance unfinished, and in the pitch black maw of the earth you buried me, and I buried you.\n"
        voice "audio/_pristine/voice/den/mound/2.flac"
        show shifting pity smile talk onlayer front at Position(ypos=1125)
        show felina den3 onlayer inyourface at Position(ypos=1125)
        with Dissolve(1.0)
        mounds "But even held by root and stone, we continued our step, until finally we could step no longer.\n"
    if beast_2_end == "fight_fail" or beast_2_end == "free_fail":
        voice "audio/_pristine/voice/den/mound/5.flac"
        hide fight onlayer inyourface
        hide shifting onlayer front
        hide pop onlayer inyourface
        show farback quiet onlayer farback at Position(ypos=1125)
        show back awakening onlayer back at Position(ypos=1125)
        show midground awakening onlayer front at Position(ypos=1125)
        show hair awakened onlayer front at Position(ypos=1125)
        show dress felina onlayer front at Position(ypos=1125)
        show shifting pity smile talk onlayer front at Position(ypos=1125)
        show felina den1 onlayer inyourface at Position(ypos=1125)
        with Dissolve(1.0)
        mounds "But we had a dance unfinished. Questions in need of answers. And you found truth in a waiting maw at the edge of darkness.\n"
    if beast_2_end == "free_succeed":
        #voice "audio/voices/felina/fight/den4.flac"
        voice "audio/_pristine/voice/den/mound/6.flac"
        hide fight onlayer inyourface
        hide shifting onlayer front
        hide pop onlayer inyourface
        show farback quiet onlayer farback at Position(ypos=1125)
        show back awakening onlayer back at Position(ypos=1125)
        show midground awakening onlayer front at Position(ypos=1125)
        show hair awakened onlayer front at Position(ypos=1125)
        show dress felina onlayer front at Position(ypos=1125)
        show shifting pity smile talk onlayer front at Position(ypos=1125)
        show felina den1 onlayer inyourface at Position(ypos=1125)
        with Dissolve(1.0)
        mound "But we had a dance unfinished and you had questions in need of answers. And in the cold starlight, you found them. Fear reflected in the eyes of that which terrified you.\n"
        #mound "You had questions in need of answers. And in the cold starlight, you found them. Fear reflected in the eyes of that which terrified you.\n"
        #voice "audio/voices/felina/fight/den5.flac"
        show shifting closed smile talk onlayer front
        show felina den3 onlayer inyourface at Position(ypos=1125)
        with dissolve
        voice "audio/_pristine/voice/_climax/felina/_temp/24.flac"
        mound "Even the cruelest of monsters are not unworthy of sympathy. Within me, nothing is beyond redemption. Together we dug through hell, and together we found our freedom.\n"
        #mound "Even the cruelest of monsters are not unworthy of sympathy. Within my being, nothing is beyond redemption. No soul is forever diminished by the sins it has committed.\n"
        show shifting smile onlayer front
    if beast_2_end == "starve":
        voice "audio/_pristine/voice/den/mound/8.flac"
        hide fight onlayer inyourface
        hide shifting onlayer front
        hide pop onlayer inyourface
        show farback quiet onlayer farback at Position(ypos=1125)
        show back awakening onlayer back at Position(ypos=1125)
        show midground awakening onlayer front at Position(ypos=1125)
        show hair awakened onlayer front at Position(ypos=1125)
        show dress felina onlayer front at Position(ypos=1125)
        show shifting pity smile talk onlayer front at Position(ypos=1125)
        show felina den3 onlayer inyourface at Position(ypos=1125)
        hide fight onlayer inyourface
        with dissolve
        mound "A sharp pause. A dull silence. A climax, but not a finale.\n"
        voice "audio/_pristine/voice/den/mound/9.flac"
        show shifting serious talk onlayer front at Position(ypos=1125)
        show felina den2 onlayer inyourface at Position(ypos=1125)
        with dissolve
        mound "The dance is our only salvation. Without me, you would have starved forever.\n"
        show shifting serious onlayer front
    elif beast_2_end != "free_succeed":
        #voice "audio/voices/felina/fight/den7a.flac"
        voice "audio/_pristine/voice/_climax/felina/_temp/denfinal.flac"
        hide fight onlayer inyourface
        hide shifting onlayer front
        hide pop onlayer inyourface
        show farback quiet onlayer farback at Position(ypos=1125)
        show back awakening onlayer back at Position(ypos=1125)
        show midground awakening onlayer front at Position(ypos=1125)
        show hair awakened onlayer front at Position(ypos=1125)
        show dress felina onlayer front at Position(ypos=1125)
        show shifting serious talk onlayer front at Position(ypos=1125)
        show felina den3 onlayer inyourface at Position(ypos=1125)
        hide fight onlayer inyourface
        with dissolve
        mound "The dance is its own truth. It is the movement that matters, not the pause you mistake for an ending.\n"
        show shifting serious onlayer front

    label felina_den_menu:
        menu:
            extend ""

            "{i}{outlinecolor=4f1313}• ''The more we fought, the more you became an animal. I put you down then, and I will put you down now. The world doesn't need your savagery.''{/outlinecolor}{/i}" if beast_2_end == "slay":
                jump felina_violence_join

            "{i}• (Explore) [[Address this vessel's statement directly.]{/i}":
                menu:
                    extend ""

                    "{i}• ''But I don't want to dance.''{/i}" if beast_2_end != "free_succeed":
                        voice "audio/_pristine/voice/_climax/felina/_temp/26.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting closed smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "That, too, is part of the dance. Would you rob yourself of the ability to choose?\n"

                    "{i}• ''Without you there is no need for redemption.''{/i}" if beast_2_end == "free_succeed":
                        voice "audio/_pristine/voice/_climax/felina/_temp/27.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting closed smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "Then without me, there is only eternal damnation.\n"

                    "{i}• ''Would you have us fight forever?''{/i}" if beast_2_end != "free_succeed":
                        voice "audio/voices/felina/fight/den8.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting closed smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "I would have you realize that what you decry as suffering is beauty. But even as you stir to wakefulness, you cling to mortality that was never yours.\n"

                    "{i}• ''The dance was good, wasn't it?''{/i}" if beast_2_end != "free_succeed":
                        voice "audio/voices/felina/fight/den9.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting pity smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "And it will always be good, if you choose to live in it. Do not linger on the highs and lows. They are fleeting strokes on a larger canvas.\n"
                        show shifting pity smile onlayer front

                    "{i}• ''You speak as though change comes gently, but our transformations were born of destruction and violence.''{/i}" if beast_2_end == "free_succeed":
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        $ felina_fight_effective_resistance += 1
                        voice "audio/voices/felina/fight/den10.flac"
                        show shifting closed smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "I am but the illusion of destruction. People fear that death is their true end, because they cannot fathom new beginnings. It is empathy to accept me.\n"

                    "{i}• ''But without you, I never would have starved to begin with.''{/i}" if beast_2_end == "starve":
                        label felina_den_crystalize_join:
                            $ felina_fight_effective_resistance += 1
                            play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                            voice "audio/_pristine/voice/den/mound/10.flac"
                            show shifting closed smile talk onlayer front
                            hide felina onlayer inyourface
                            with dissolve
                            mound "Without me to move things forward, everything would crystalize into misery. Without me, every moment would be unending.\n"

                    "{i}• ''Thank you for ending our misery.''{/i}" if beast_2_end == "starve":
                        label felina_den_leave_promt:
                            play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                            $ felina_fight_effective_resistance -= 1
                            voice "audio/_pristine/voice/den/mound/11.flac"
                            show shifting closed smile talk onlayer front
                            hide felina onlayer inyourface
                            with dissolve
                            mound "The only thanks you need to give is both our freedoms. Leave with me.\n"
                            menu:
                                extend ""

                                "{i}• ''I'm ready. I want to leave with you.'' [[Stop the fight early and surrender.]{/i}" if felina_round >= 2:
                                    $ achievement.grant("ACH_END_FREE2")
                                    jump felina_freedom_join

                                "{i}• ''I won't leave with you. Not until you see things from my perspective.''{/i}" if felina_round >= 2:
                                    voice "audio/voices/felina/fight/dams8.flac"
                                    show shifting smile talk onlayer front
                                    mound "If you need more time to open your eyes, then I will give you all the time in the world.\n"

                    "{i}• ''Thank you for saving us.''{/i}" if beast_2_end == "free_succeed":
                        jump felina_den_leave_promt

                    "{i}• ''I don't want to think of a world without you.''{/i}":
                        $ felina_fight_effective_resistance -= 1
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        voice "audio/voices/felina/fight/den11.flac"
                        show shifting pity smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "Then don't.\n"
                        show shifting pity smile onlayer front

                    "{i}• ''Are you so sure of yourself that you think the world would stop without you?''{/i}":
                        $ felina_fight_effective_resistance += 1
                        voice "audio/voices/felina/fight/den12.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        hide felina onlayer inyourface
                        with dissolve
                        mound "I know that I am movement itself. You've seen as much. You know it's true.\n"

                    "{i}• (Return){/i}":
                        jump felina_den_menu

            "{i}• [[Appeal to your shared humanity.] ''You speak about life and death and change and stagnation, but that isn't what any of this has been about.''{/i}" if felina_appeal_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''This has always just been about us. Two people forced to hurt each other again and again and again. But we don't have to hurt each other anymore.''{/i}" if felina_appeal_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''There can be love and conflict and beauty and ugliness between us without bringing the whole of reality into the picture.''{/i}" if felina_appeal_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''We're not the whole of reality. Why won't you see me the way I still see you? Why won't you see me for what I am?''{/i}" if felina_appeal_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''This doesn't have to be so big. You can come back down to my level. You can come back to me.''{/i}" if felina_appeal_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Reject her authority.] ''You've done nothing but lecture me since the minute I got here.''{/i}" if felina_lecture_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''You use all these pretentious metaphors and pretend you're making grand proclamations about who I am and who you are. But really you aren't saying much of anything.''{/i}" if felina_lecture_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''It doesn't even matter what I say to you, because you're just going to keep telling me your perspective like it's some universal truth.''{/i}" if felina_lecture_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''It was so much better when I was with your vessels. Even at their worst, they all still heard me.''{/i}" if felina_lecture_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''I don't know what you are, but you aren't any of them. You're just something wearing their skin.''{/i}" if felina_lecture_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Argue your independence.] ''You act as though the world can't exist without you. But I've existed without you.''{/i}" if felina_assert_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''What are the woods, then? What is the cabin? What is the time we've spent apart if not me existing as myself?''{/i}" if felina_assert_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''I wouldn't be here if destroying you would leave all of reality a colorless blur.''{/i}" if felina_assert_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''I'd rather trust an ignorant soul who died trying to make things better than a god who'd let the wheel of suffering turn forever.''{/i}" if felina_assert_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''If I need to destroy you to build a better world, then I will.''{/i}" if felina_assert_count == 4:
                $ felina_assert_lethal = True
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''Who said anything about destroying you? I just need to make you stop.''{/i}" if felina_assert_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Reject her perspective.] ''I won't engage with violence.''{/i}" if felina_rejection_count == 0:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''It doesn't matter how I feel. Death, suffering, and oblivion shouldn't fall on others. If we are able to transcend death, then we are responsible for those it holds captive.''{/i}" if felina_rejection_count == 1:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''Suffering born in delusion is still suffering. It doesn't matter what we are now. We hurt each other, and we shouldn't have done that. We cannot let a world be spun out of that pain.''{/i}" if felina_rejection_count == 2:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''You reject the suffering of material reality, and yet you cling to its framework for meaning. We can be better than this.''{/i}" if felina_rejection_count == 3:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''You claim your destruction would steal meaning from existence, but if my actions can make existence worse, then there must be actions that make it better. Perfection implies finality, and nothing is final.''{/i}" if felina_rejection_count == 4:
                jump felina_rejection_join

            "{i}• ''I get it. There's no need for us to keep fighting. I'll leave with you. I just don't know how.'' [[Stop the fight early and surrender.]{/i}" if felina_round >= 2:
                $ achievement.grant("ACH_END_FREE2")
                jump felina_freedom_join

            "{i}• [[Remain silent.]{/i}":
                jump felina_silence

    jump felina_fight_staging

label felina_damsel_start:

    if damsel_end == "dereal":
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
            show pop dereal onlayer inyourface at shakeshort, Position(ypos=1125)
        else:
            $ previous_transform = "horrorflip"
            show shifting horror onlayer front at flip, shakeshort, Position(ypos=1125)
            show pop dereal onlayer inyourface at flip, shakeshort, Position(ypos=1125)
        with Dissolve(0.25)
        $ renpy.pause(4.2)
    else:
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
            show pop damsel onlayer inyourface at shakeshort, Position(ypos=1125)
        else:
            $ previous_transform = "danceflip"
            show shifting dance onlayer front at flip, shakeshort, Position(ypos=1125)
            show pop damsel onlayer inyourface at flip, shakeshort, Position(ypos=1125)
        with Dissolve(0.25)
        $ renpy.pause(1.45)

    play audio "audio/final/Tower_KnifeBlow_SEQUENCED_5.flac"
    show fight damsel onlayer inyourface at Position(ypos=1125)
    $ renpy.pause(0.01)
    $ gallery_damsel.unlock_item(20)
    $ renpy.save_persistent()
    voice "audio/voices/felina/fight/dams1.flac"
    with Dissolve(1.0)
    mound "Your lover drives a stake into your body. And another, and another, and another. Do I miss your heart because I can't stand to see it go?\n"
    if damsel_end == "free":
        voice "audio/voices/felina/fight/dams2.flac"
        hide fight onlayer inyourface
        hide shifting onlayer front
        hide pop onlayer inyourface
        show farback quiet onlayer farback at Position(ypos=1125)
        show back awakening onlayer back at Position(ypos=1125)
        show midground awakening onlayer front at Position(ypos=1125)
        show hair awakened onlayer front at Position(ypos=1125)
        show dress felina onlayer front at Position(ypos=1125)
        show shifting martyrs talk onlayer front at Position(ypos=1125)
        show felina dams2 talk onlayer inyourface at Position(ypos=1125)
        with dissolve
        mound "But the stakes meant nothing to you. You had a desire, and you set that desire free, you lifting me and me lifting you, forever and ever and ever. Consumed by true belief, there was nothing that could hold us back.\n"
        show shifting martyrs onlayer front
        show felina dams3 onlayer inyourface
        with dissolve

    if damsel_end == "dereal":
        voice "audio/voices/felina/fight/dams3.flac"
        hide fight onlayer inyourface
        hide shifting onlayer front
        hide pop onlayer inyourface
        show farback quiet onlayer farback at Position(ypos=1125)
        show back awakening onlayer back at Position(ypos=1125)
        show midground awakening onlayer front at Position(ypos=1125)
        show hair awakened onlayer front at Position(ypos=1125)
        show dress felina onlayer front at Position(ypos=1125)
        show shifting martyrs talk onlayer front at Position(ypos=1125)
        show felina dams2 talk onlayer inyourface at Position(ypos=1125)
        with dissolve
        mound "Love melted into skepticism, and you pulled back layer after layer after layer until all you were left with was the knowledge that you did not know me.\n"
        voice "audio/voices/felina/fight/dams4a.flac"
        show shifting pissed talk onlayer front
        show felina dams3 onlayer inyourface
        with dissolve
        mound "You sought the truth then. Will you hide from it now that it is within your grasp?\n"
        show shifting pissed onlayer front

    label felina_damsel_menu:
        menu:
            extend ""

            "{i}{outlinecolor=4f1313}• ''My thoughts alone were enough to reduce you into nothing.''{/outlinecolor}{/i}" if damsel_end == "dereal":
                jump felina_violence_join

            "{i}• (Explore) [[Address this vessel's statement directly.]{/i}":
                menu:
                    extend ""

                    "{i}• ''I was blinded by emotion. We both know that.''{/i}" if damsel_end == "free":
                        voice "audio/voices/felina/fight/dams5.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting martyrs talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "We were both taken by the moment. It was how things are meant to be.\n"

                    "{i}• ''I want that feeling back.''{/i}" if damsel_end == "free":
                        $ felina_fight_effective_resistance -= 1
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        voice "audio/voices/felina/fight/dams6.flac"
                        show shifting pity smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "It never left you. You just need to open your heart to me once more.\n"

                    "{i}• ''That feeling never left me.''{/i}" if damsel_end == "free":
                        $ felina_fight_effective_resistance -= 1
                        voice "audio/voices/felina/fight/dams7.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting pity smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "Then there's no need for you to fight what we are. Whenever you're ready, we can leave together, hand in loving hand.\n"
                        show shifting pity smile onlayer front
                        label felina_damsel_leave_ready:
                            menu:
                                extend ""

                                "{i}• ''I'm ready. I want to leave with you.'' [[Stop the fight early and surrender.]{/i}" if felina_round >= 2:
                                    $ achievement.grant("ACH_END_FREE2")
                                    jump felina_freedom_join

                                "{i}• ''I won't leave with you. Not until you see things from my perspective.''{/i}" if felina_round >= 2:
                                    voice "audio/voices/felina/fight/dams8.flac"
                                    show shifting closed smile talk onlayer front
                                    with dissolve
                                    mound "If you need more time to open your eyes, then I will give you all the time in the world.\n"

                    "{i}• ''I have no desire to hide, but the truth can be made better. If destroying you is what that takes... so be it.''{/i}" if damsel_end == "dereal":
                        $ felina_fight_effective_resistance += 1
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        voice "audio/voices/felina/fight/dams9.flac"
                        show shifting martyrs talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "I am so deeply woven into the threads of this reality that I cannot imagine it without me. Perhaps there is a better world to build.\n"
                        voice "audio/voices/felina/fight/dams10.flac"
                        show shifting pissed talk onlayer front
                        with dissolve
                        mound "But you cannot know until you see it. Are you so sure in your blind optimism that you would shatter all of creation?\n"

                    "{i}• ''I don't want to hide from the truth.''{/i}" if damsel_end == "dereal":
                        voice "audio/voices/felina/fight/dams11.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting closed smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "Then don't.\n"
                        voice "audio/voices/felina/fight/dams12.flac"
                        show shifting pity smile talk onlayer front
                        with dissolve
                        mound "Leave with me. There's no need for you to fight what we are.\n"
                        show shifting pity smile onlayer front
                        jump felina_damsel_leave_ready

                    "{i}• (Return){/i}":
                        jump felina_damsel_menu

            "{i}• [[Appeal to your shared humanity.] ''You speak about life and death and change and stagnation, but that isn't what any of this has been about.''{/i}" if felina_appeal_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''This has always just been about us. Two people forced to hurt each other again and again and again. But we don't have to hurt each other anymore.''{/i}" if felina_appeal_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''There can be love and conflict and beauty and ugliness between us without bringing the whole of reality into the picture.''{/i}" if felina_appeal_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''We're not the whole of reality. Why won't you see me the way I still see you? Why won't you see me for what I am?''{/i}" if felina_appeal_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''This doesn't have to be so big. You can come back down to my level. You can come back to me.''{/i}" if felina_appeal_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Reject her authority.] ''You've done nothing but lecture me since the minute I got here.''{/i}" if felina_lecture_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''You use all these pretentious metaphors and pretend you're making grand proclamations about who I am and who you are. But really you aren't saying much of anything.''{/i}" if felina_lecture_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''It doesn't even matter what I say to you, because you're just going to keep telling me your perspective like it's some universal truth.''{/i}" if felina_lecture_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''It was so much better when I was with your vessels. Even at their worst, they all still heard me.''{/i}" if felina_lecture_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''I don't know what you are, but you aren't any of them. You're just something wearing their skin.''{/i}" if felina_lecture_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Argue your independence.] ''You act as though the world can't exist without you. But I've existed without you.''{/i}" if felina_assert_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''What are the woods, then? What is the cabin? What is the time we've spent apart if not me existing as myself?''{/i}" if felina_assert_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''I wouldn't be here if destroying you would leave all of reality a colorless blur.''{/i}" if felina_assert_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''I'd rather trust an ignorant soul who died trying to make things better than a god who'd let the wheel of suffering turn forever.''{/i}" if felina_assert_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''If I need to destroy you to build a better world, then I will.''{/i}" if felina_assert_count == 4:
                $ felina_assert_lethal = True
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''Who said anything about destroying you? I just need to make you stop.''{/i}" if felina_assert_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Reject her perspective.] ''I won't engage with violence.''{/i}" if felina_rejection_count == 0:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''It doesn't matter how I feel. Death, suffering, and oblivion shouldn't fall on others. If we are able to transcend death, then we are responsible for those it holds captive.''{/i}" if felina_rejection_count == 1:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''Suffering born in delusion is still suffering. It doesn't matter what we are now. We hurt each other, and we shouldn't have done that. We cannot let a world be spun out of that pain.''{/i}" if felina_rejection_count == 2:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''You reject the suffering of material reality, and yet you cling to its framework for meaning. We can be better than this.''{/i}" if felina_rejection_count == 3:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''You claim your destruction would steal meaning from existence, but if my actions can make existence worse, then there must be actions that make it better. Perfection implies finality, and nothing is final.''{/i}" if felina_rejection_count == 4:
                jump felina_rejection_join

            "{i}• ''I get it. There's no need for us to keep fighting. I'll leave with you. I just don't know how.'' [[Stop the fight early and surrender.]{/i}" if felina_round >= 2:
                $ achievement.grant("ACH_END_FREE2")
                jump felina_freedom_join

            "{i}• [[Remain silent.]{/i}":
                jump felina_silence

    jump felina_fight_staging

label felina_nightmare_start:

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
        show pop nightmare onlayer inyourface at shakeshort, Position(ypos=1125)
    else:
        $ previous_transform = "horrorflip"
        show shifting horror onlayer front at flip, shakeshort, Position(ypos=1125)
        show pop nightmare onlayer inyourface at flip, shakeshort, Position(ypos=1125)
    with Dissolve(0.25)
    $ renpy.pause(4.2)

    $ gallery_nightmare.unlock_item(19)
    $ renpy.save_persistent()
    play audio "audio/final/Assorted_Static_5.flac"
    show fight nightmare onlayer inyourface at Position(ypos=1125)
    $ renpy.pause(0.01)
    voice "audio/voices/felina/fight/nm1a.flac"
    mounds "Fear is what pretends to protect us from loss. To fear death 'protects' from losing a body. To fear ruin 'protects' from losing status. To fear rejection 'protects' from being known.\n"
    voice "audio/voices/felina/fight/nm2.flac"
    hide fight onlayer inyourface
    hide shifting onlayer front
    hide pop onlayer inyourface
    show farback quiet onlayer farback at Position(ypos=1125)
    show back awakening onlayer back at Position(ypos=1125)
    show midground awakening onlayer front at Position(ypos=1125)
    show hair awakened onlayer front at Position(ypos=1125)
    show dress felina onlayer front at Position(ypos=1125)
    show shifting closed smile talk onlayer front at Position(ypos=1125)
    show felina nightmare3 onlayer inyourface at Position(ypos=1125)
    with Dissolve(1.0)
    mound "But losing a body is contained within having a body. Losing status is contained within having status. Being known is contained within being conscious.\n"
    voice "audio/voices/felina/fight/nm3.flac"
    show shifting martyrs talk onlayer front
    show felina nightmare1 onlayer inyourface
    with dissolve
    mound "It is the nature of all things to transform. To go from known to hidden to known again.\n"
    voice "audio/voices/felina/fight/nm4.flac"
    show shifting pity smile talk onlayer front
    show felina nightmare2 onlayer inyourface
    with dissolve
    mound "But when the ceaseless impermanence of all things strips away the finality of endings, what remains of fear? Is it a shelter protecting you from itself? Or is it a shelter protecting itself from you?\n"
    voice "audio/voices/felina/fight/nm5.flac"
    show shifting martyrs talk onlayer front
    show felina nightmare3 onlayer inyourface
    with dissolve
    mound "You took fear by the hand and walked with it into the unknown, and through that, you feared nothing.\n"
    show shifting martyrs onlayer front
    label felina_nightmare_menu:
        menu:
            extend ""

            "{i}• (Explore) [[Address this vessel's statement directly.]{/i}":
                menu:
                    extend ""

                    "{i}• ''That wasn't a rejection of fear. You broke me to your will.''{/i}":
                        $ felina_fight_effective_resistance += 1
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        voice "audio/voices/felina/fight/nm6.flac"
                        show shifting pissed talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "Were you afraid when you stepped through that door, or were you enticed by what might come next? By what might lie beyond fear? By what you might become?\n"
                        voice "audio/voices/felina/fight/nm7.flac"
                        show shifting closed smile talk onlayer front
                        with dissolve
                        mound "You say I broke you, but was that curiosity not freedom of its own?\n"

                    "{i}• ''You wanted to make the world suffer. You act as if you're above it all, but you're not.''{/i}":
                        $ felina_fight_effective_resistance += 1
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        voice "audio/voices/felina/fight/nm8.flac"
                        show shifting pissed talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "A desire borne from the narrow view of a single life. But even then, the only gifts I brought were context and sensation.\n"
                        voice "audio/voices/felina/fight/nm9.flac"
                        show shifting serious talk onlayer front
                        with dissolve
                        mound "To feel is to exist, and to exist is to have meaning.\n"

                    "{i}• ''I'm not afraid anymore.''{/i}":
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        voice "audio/voices/felina/fight/nm10.flac"
                        show shifting pity smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "Then you are one step closer to being free of your bindings.\n"

                    "{i}• ''Even if I'm not afraid now, the fear of others is real. We can't uphold the harm that everyone suffers just because we're beyond it.''{/i}":
                        $ felina_fight_effective_resistance += 1
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        #voice "audio/voices/felina/fight/nm11.flac"
                        voice "audio/_pristine/voice/_climax/felina/59.flac"
                        show shifting pissed talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "Others cling to fear because they have not yet seen beyond it. Will you strip the world of possibility just because some refuse to see its beauty?\n"
                        #mound "Others cling to fear because they have not yet seen beyond it. Will you strip the beauty of transformation just because some refuse to acknowledge it?\n"

                    "{i}• (Return){/i}":
                        jump felina_nightmare_menu

            "{i}• [[Appeal to your shared humanity.] ''You speak about life and death and change and stagnation, but that isn't what any of this has been about.''{/i}" if felina_appeal_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''This has always just been about us. Two people forced to hurt each other again and again and again. But we don't have to hurt each other anymore.''{/i}" if felina_appeal_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''There can be love and conflict and beauty and ugliness between us without bringing the whole of reality into the picture.''{/i}" if felina_appeal_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''We're not the whole of reality. Why won't you see me the way I still see you? Why won't you see me for what I am?''{/i}" if felina_appeal_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''This doesn't have to be so big. You can come back down to my level. You can come back to me.''{/i}" if felina_appeal_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Reject her authority.] ''You've done nothing but lecture me since the minute I got here.''{/i}" if felina_lecture_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''You use all these pretentious metaphors and pretend you're making grand proclamations about who I am and who you are. But really you aren't saying much of anything.''{/i}" if felina_lecture_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''It doesn't even matter what I say to you, because you're just going to keep telling me your perspective like it's some universal truth.''{/i}" if felina_lecture_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''It was so much better when I was with your vessels. Even at their worst, they all still heard me.''{/i}" if felina_lecture_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''I don't know what you are, but you aren't any of them. You're just something wearing their skin.''{/i}" if felina_lecture_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Argue your independence.] ''You act as though the world can't exist without you. But I've existed without you.''{/i}" if felina_assert_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''What are the woods, then? What is the cabin? What is the time we've spent apart if not me existing as myself?''{/i}" if felina_assert_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''I wouldn't be here if destroying you would leave all of reality a colorless blur.''{/i}" if felina_assert_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''I'd rather trust an ignorant soul who died trying to make things better than a god who'd let the wheel of suffering turn forever.''{/i}" if felina_assert_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''If I need to destroy you to build a better world, then I will.''{/i}" if felina_assert_count == 4:
                $ felina_assert_lethal = True
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''Who said anything about destroying you? I just need to make you stop.''{/i}" if felina_assert_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Reject her perspective.] ''I won't engage with violence.''{/i}" if felina_rejection_count == 0:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''It doesn't matter how I feel. Death, suffering, and oblivion shouldn't fall on others. If we are able to transcend death, then we are responsible for those it holds captive.''{/i}" if felina_rejection_count == 1:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''Suffering born in delusion is still suffering. It doesn't matter what we are now. We hurt each other, and we shouldn't have done that. We cannot let a world be spun out of that pain.''{/i}" if felina_rejection_count == 2:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''You reject the suffering of material reality, and yet you cling to its framework for meaning. We can be better than this.''{/i}" if felina_rejection_count == 3:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''You claim your destruction would steal meaning from existence, but if my actions can make existence worse, then there must be actions that make it better. Perfection implies finality, and nothing is final.''{/i}" if felina_rejection_count == 4:
                jump felina_rejection_join

            "{i}• ''I get it. There's no need for us to keep fighting. I'll leave with you. I just don't know how.'' [[Stop the fight early and surrender.]{/i}" if felina_round >= 2:
                $ achievement.grant("ACH_END_FREE2")
                jump felina_freedom_join

            "{i}• [[Remain silent.]{/i}":
                jump felina_silence

    jump felina_fight_staging

label felina_nightmare2_start:

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
        show pop clarity onlayer inyourface at shakeshort, Position(ypos=1125)
    else:
        $ previous_transform = "horrorflip"
        show shifting horror onlayer front at flip, shakeshort, Position(ypos=1125)
        show pop clarity onlayer inyourface at flip, shakeshort, Position(ypos=1125)
    with Dissolve(0.25)
    $ renpy.pause(4.2)
    $ gallery_clarity.unlock_item(14)
    $ renpy.save_persistent()
    play audio "audio/final/Assorted_Static_5.flac"
    show fight clarity onlayer inyourface at Position(ypos=1125)
    $ renpy.pause(0.1)
    voice "audio/voices/felina/fight/c1.flac"
    mounds "There are few things more terrifying than one's own heart, and there is almost nothing more terrifying than sharing it with another.\n"
    voice "audio/voices/felina/fight/c2.flac"
    hide fight onlayer inyourface
    hide shifting onlayer front
    hide pop onlayer inyourface
    show farback quiet onlayer farback at Position(ypos=1125)
    show back awakening onlayer back at Position(ypos=1125)
    show midground awakening onlayer front at Position(ypos=1125)
    show hair awakened onlayer front at Position(ypos=1125)
    show dress felina onlayer front at Position(ypos=1125)
    show shifting martyrs talk onlayer front at Position(ypos=1125)
    show felina clarity2 onlayer inyourface at Position(ypos=1125)
    with Dissolve(0.5)
    mound "But the most terrifying thing of all is to leave one's heart unshared. You are the only thing like me, and I am the only thing like you.\n"
    voice "audio/voices/felina/fight/c3.flac"
    show shifting smile talk onlayer front
    show felina clarity3 onlayer inyourface
    with dissolve
    mound "Could you bear the weight of an eternity alone? Do you dare to shape a reality of solitude and thrust it on creation?\n"
    show shifting smile onlayer front
    with dissolve
    label felina_clarity_menu:
        menu:
            extend ""

            "{i}• (Explore) [[Address this vessel's statement directly.]{/i}":
                menu:
                    extend ""

                    "{i}• ''Thank you for sharing yourself with me.''{/i}":
                        $ felina_fight_effective_resistance -= 1
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        voice "audio/voices/felina/fight/c4.flac"
                        show shifting pity smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "I am aware of what it did to you. The understanding you've returned to me is a gift.\n"

                    "{i}• ''I don't need to share my heart with anyone.''{/i}":
                        $ felina_fight_effective_resistance += 1
                        jump nightmare_2_felina_join

                    "{i}• ''I wish I could share my heart with you.''{/i}":
                        $ felina_fight_effective_resistance -= 1
                        label nightmare_2_felina_join:
                            voice "audio/voices/felina/fight/c5.flac"
                            play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                            show shifting pity smile talk onlayer front
                            hide felina onlayer inyourface
                            with dissolve
                            mound "But you already have, in so many ways. It is beautiful and adored. When movement slows and the dust settles, I hope you'll leave with me.\n"

                    "{i}• ''You showed me your heart to break me. It was a terrible thing to see.''{/i}":
                        voice "audio/voices/felina/fight/c6.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting pity smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "I am aware of what it did to you. But it is through the pain of vulnerability that we heal. Will you leave all who have been hurt to live unmended?\n"

                    "{i}• ''If that is what it takes to rid the world of suffering, I could bear the solitude.''{/i}":
                        $ felina_fight_effective_resistance += 1
                        voice "audio/voices/felina/fight/c7.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting serious talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "Your certainty is an illusion of passion and reflex. You won't know what solitude truly is unless you sentence yourself to it forever.\n"

                    "{i}• (Return){/i}":
                        jump felina_clarity_menu

            "{i}• [[Appeal to your shared humanity.] ''You speak about life and death and change and stagnation, but that isn't what any of this has been about.''{/i}" if felina_appeal_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''This has always just been about us. Two people forced to hurt each other again and again and again. But we don't have to hurt each other anymore.''{/i}" if felina_appeal_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''There can be love and conflict and beauty and ugliness between us without bringing the whole of reality into the picture.''{/i}" if felina_appeal_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''We're not the whole of reality. Why won't you see me the way I still see you? Why won't you see me for what I am?''{/i}" if felina_appeal_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''This doesn't have to be so big. You can come back down to my level. You can come back to me.''{/i}" if felina_appeal_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Reject her authority.] ''You've done nothing but lecture me since the minute I got here.''{/i}" if felina_lecture_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''You use all these pretentious metaphors and pretend you're making grand proclamations about who I am and who you are. But really you aren't saying much of anything.''{/i}" if felina_lecture_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''It doesn't even matter what I say to you, because you're just going to keep telling me your perspective like it's some universal truth.''{/i}" if felina_lecture_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''It was so much better when I was with your vessels. Even at their worst, they all still heard me.''{/i}" if felina_lecture_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''I don't know what you are, but you aren't any of them. You're just something wearing their skin.''{/i}" if felina_lecture_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Argue your independence.] ''You act as though the world can't exist without you. But I've existed without you.''{/i}" if felina_assert_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''What are the woods, then? What is the cabin? What is the time we've spent apart if not me existing as myself?''{/i}" if felina_assert_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''I wouldn't be here if destroying you would leave all of reality a colorless blur.''{/i}" if felina_assert_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''I'd rather trust an ignorant soul who died trying to make things better than a god who'd let the wheel of suffering turn forever.''{/i}" if felina_assert_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''If I need to destroy you to build a better world, then I will.''{/i}" if felina_assert_count == 4:
                $ felina_assert_lethal = True
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''Who said anything about destroying you? I just need to make you stop.''{/i}" if felina_assert_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Reject her perspective.] ''I won't engage with violence.''{/i}" if felina_rejection_count == 0:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''It doesn't matter how I feel. Death, suffering, and oblivion shouldn't fall on others. If we are able to transcend death, then we are responsible for those it holds captive.''{/i}" if felina_rejection_count == 1:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''Suffering born in delusion is still suffering. It doesn't matter what we are now. We hurt each other, and we shouldn't have done that. We cannot let a world be spun out of that pain.''{/i}" if felina_rejection_count == 2:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''You reject the suffering of material reality, and yet you cling to its framework for meaning. We can be better than this.''{/i}" if felina_rejection_count == 3:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''You claim your destruction would steal meaning from existence, but if my actions can make existence worse, then there must be actions that make it better. Perfection implies finality, and nothing is final.''{/i}" if felina_rejection_count == 4:
                jump felina_rejection_join

            "{i}• ''I get it. There's no need for us to keep fighting. I'll leave with you. I just don't know how.'' [[Stop the fight early and surrender.]{/i}" if felina_round >= 2:
                $ achievement.grant("ACH_END_FREE2")
                jump felina_freedom_join

            "{i}• [[Remain silent.]{/i}":
                jump felina_silence

    jump felina_fight_staging

label felina_prisoner_start:


    if prisoner_end == "free":
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
            show pop prisoner head onlayer inyourface at shakeshort, Position(ypos=1125)
        else:
            $ previous_transform = "handsflip"
            show shifting hands onlayer front at flip, shakeshort, Position(ypos=1125)
            show pop prisoner head onlayer inyourface at flip, shakeshort, Position(ypos=1125)
        with Dissolve(0.25)
        $ renpy.pause(1.90)
        $ gallery_prisoner.unlock_item(17)
        $ renpy.save_persistent()
        play audio "audio/final/Prisoner_HeavyChains_2.flac"
        show fight prisoner onlayer inyourface at Position(ypos=1125)
        $ renpy.pause(0.01)
        #voice "audio/voices/felina/fight/p1.flac"
        voice "audio/_pristine/voice/_climax/felina/60.flac"
        mounds "To question everything is to deny the truth in front of you. To live alone within the caverns of your mind is to trap yourself in them forever.\n"
        #mounds "To question everything is to deny proof of the reality that lies in front of you. To live alone within the caverns of your mind is to trap yourself in them forever.\n"
        #voice "audio/voices/felina/fight/p2.flac"
        voice "audio/_pristine/voice/_climax/felina/61.flac"
        hide fight onlayer inyourface
        hide shifting onlayer front
        hide pop onlayer inyourface
        show farback quiet onlayer farback at Position(ypos=1125)
        show back awakening onlayer back at Position(ypos=1125)
        show midground awakening onlayer front at Position(ypos=1125)
        show hair awakened onlayer front at Position(ypos=1125)
        show dress felina onlayer front at Position(ypos=1125)
        show shifting smile talk onlayer front at Position(ypos=1125)
        show felina prisoner head2 talk onlayer inyourface at Position(ypos=1125)
        with Dissolve(1.0)
        #mound "But you did not live alone. You found me. And we held trust in each other for no reason than to believe in something that wasn't us.\n"
        mound "But you found me. And we chose to trust each other for no reason than the sake of believing in something that wasn't us.\n"
        #voice "audio/voices/felina/fight/p3.flac"
        voice "audio/_pristine/voice/_climax/felina/62.flac"
        show shifting martyrs talk onlayer front
        show felina prisoner head3 onlayer inyourface
        with dissolve
        #mound "Cold skepticism turned to liberation, but it required a journey to blossom.\n"
        mound "Shared skepticism blossomed into freedom, but we needed to walk a path together to bloom.\n"
        voice "audio/_pristine/voice/_climax/felina/63.flac"
        #voice "audio/voices/felina/fight/p4.flac"
        show shifting closed smile talk onlayer front
        show felina prisoner head1 onlayer inyourface
        with dissolve
        mound "Would you stop our journey now that you've seen its beginning? What of those in the worlds beyond? Would you erase their paths to stop them from going astray?\n"
        #mound "Though you have blossomed, do you have no more journeys left to make? What of those in the spaces beyond? Would you erase the path ahead to hold everyone still?\n"
    if prisoner_end == "stuck":
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
            show pop prisoner chain onlayer inyourface at shakeshort, Position(ypos=1125)
        else:
            $ previous_transform = "handsflip"
            show shifting hands onlayer front at flip, shakeshort, Position(ypos=1125)
            show pop prisoner chain onlayer inyourface at flip, shakeshort, Position(ypos=1125)
        with Dissolve(0.25)
        $ renpy.pause(1.90)
        $ gallery_prisoner.unlock_item(17)
        $ renpy.save_persistent()
        play audio "audio/final/Prisoner_HeavyChains_2.flac"
        show fight prisoner onlayer inyourface at Position(ypos=1125)
        $ renpy.pause(0.01)
        #voice "audio/voices/felina/fight/p5.flac"
        voice "audio/_pristine/voice/_climax/felina/64.flac"
        #show felina prisoner chain2 talk onlayer inyourface
        #show shifting pose talk onlayer front
        #with dissolve
        mounds "To question everything is to deny the truth in front of you. By believing in your suffering, you make your suffering real. By believing in your limitations, you placed a shackle on your neck.\n"
        #mounds "To question everything is to deny the proof of reality that lies in front of you. By believing in your suffering, you make your suffering real. In believing in your limitations, you placed a shackle on your neck.\n"
        #voice "audio/voices/felina/fight/p6.flac"
        voice "audio/_pristine/voice/_climax/felina/65.flac"
        hide fight onlayer inyourface
        hide shifting onlayer front
        hide pop onlayer inyourface
        show farback quiet onlayer farback at Position(ypos=1125)
        show back awakening onlayer back at Position(ypos=1125)
        show midground awakening onlayer front at Position(ypos=1125)
        show hair awakened onlayer front at Position(ypos=1125)
        show dress felina onlayer front at Position(ypos=1125)
        show shifting smile talk onlayer front at Position(ypos=1125)
        show felina prisoner chain2 talk onlayer inyourface at Position(ypos=1125)
        with Dissolve(1.0)
        mound "Bound for eternity, you saw the need for impermanence, and it was through that need that you carved our freedom.\n"
        #mound "But even then, you remembered the impermanence of the material, and watched as the walls of your prison decayed into nothing.\n"
        #voice "audio/voices/felina/fight/p7.flac"
        voice "audio/_pristine/voice/_climax/felina/66.flac"
        show shifting martyrs talk onlayer front
        show felina prisoner chain3 onlayer inyourface
        with dissolve
        mound "Without impermanence the suffering of living things is infinite.\n"
        #mound "To be impermanent is not to end, but to change, and for the world to be impermanent is to make finite the suffering of all things.\n"
        #voice "audio/voices/felina/fight/p8.flac"
        voice "audio/_pristine/voice/_climax/felina/67.flac"
        show shifting serious talk onlayer front
        show felina prisoner chain2 talk onlayer inyourface
        with dissolve
        mound "Would you strip my gifts away and leave everyone to suffer in the dark?\n"
        #mound "Would you strip that gift away and leave them all to suffer in their permanence?\n"
        show shifting serious onlayer front
        show felina prisoner chain3 onlayer inyourface
        with dissolve

    label felina_prisoner_menu:
        menu:
            extend ""

            "{i}• (Explore) [[Address this vessel's statement directly.]{/i}":
                menu:
                    extend ""

                    "{i}• ''The path is just a metaphor. I want to protect them.''{/i}" if prisoner_end == "free":
                        voice "audio/voices/felina/fight/p9.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting closed smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "And that is what I want, too. To protect them from the horrors of an eternity without me.\n"

                    "{i}• ''I don't want to keep anyone still.''{/i}" if prisoner_end == "free":
                        $ felina_fight_effective_resistance -= 1
                        voice "audio/voices/felina/fight/p10.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting closed smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "Nor should you. Nor should I. Our purpose is to be and to experience, and their purpose is the same.\n"

                    "{i}• ''What does the path matter if it always ends?''{/i}" if prisoner_end == "free":
                        $ felina_fight_effective_resistance -= 1
                        voice "audio/voices/felina/fight/p11.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting closed smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "The path only ends when it becomes a new beginning. To see those seams as finality is to pass over them with closed eyes.\n"

                    "{i}• ''They'll get over it. They'll see your end as a gift in time.''{/i}" if prisoner_end == "stuck":
                        $ felina_fight_effective_resistance += 1
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        voice "audio/voices/felina/fight/p12.flac"
                        show shifting pissed talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "Or, in time, would they see it as a curse?\n"

                    "{i}• ''That would be torture.''{/i}" if prisoner_end == "stuck":
                        $ felina_fight_effective_resistance -= 1
                        voice "audio/voices/felina/fight/p13.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting closed smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "It would. Our purpose is to be and to experience, and their purpose is the same. To be permanent is to cease. To be paused is to be trapped.\n"

                    "{i}• (Return){/i}":
                        jump felina_prisoner_menu

            "{i}• [[Appeal to your shared humanity.] ''You speak about life and death and change and stagnation, but that isn't what any of this has been about.''{/i}" if felina_appeal_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''This has always just been about us. Two people forced to hurt each other again and again and again. But we don't have to hurt each other anymore.''{/i}" if felina_appeal_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''There can be love and conflict and beauty and ugliness between us without bringing the whole of reality into the picture.''{/i}" if felina_appeal_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''We're not the whole of reality. Why won't you see me the way I still see you? Why won't you see me for what I am?''{/i}" if felina_appeal_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''This doesn't have to be so big. You can come back down to my level. You can come back to me.''{/i}" if felina_appeal_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Reject her authority.] ''You've done nothing but lecture me since the minute I got here.''{/i}" if felina_lecture_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''You use all these pretentious metaphors and pretend you're making grand proclamations about who I am and who you are. But really you aren't saying much of anything.''{/i}" if felina_lecture_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''It doesn't even matter what I say to you, because you're just going to keep telling me your perspective like it's some universal truth.''{/i}" if felina_lecture_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''It was so much better when I was with your vessels. Even at their worst, they all still heard me.''{/i}" if felina_lecture_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''I don't know what you are, but you aren't any of them. You're just something wearing their skin.''{/i}" if felina_lecture_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Argue your independence.] ''You act as though the world can't exist without you. But I've existed without you.''{/i}" if felina_assert_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''What are the woods, then? What is the cabin? What is the time we've spent apart if not me existing as myself?''{/i}" if felina_assert_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''I wouldn't be here if destroying you would leave all of reality a colorless blur.''{/i}" if felina_assert_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''I'd rather trust an ignorant soul who died trying to make things better than a god who'd let the wheel of suffering turn forever.''{/i}" if felina_assert_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''If I need to destroy you to build a better world, then I will.''{/i}" if felina_assert_count == 4:
                $ felina_assert_lethal = True
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''Who said anything about destroying you? I just need to make you stop.''{/i}" if felina_assert_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Reject her perspective.] ''I won't engage with an argument that favors death and suffering.''{/i}" if felina_rejection_count == 0:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''It doesn't matter how I feel. Death, suffering, and oblivion shouldn't fall on others. If we are able to transcend death, then we are responsible for those it holds captive.''{/i}" if felina_rejection_count == 1:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''Suffering born in delusion is still suffering. It doesn't matter what we are now. We hurt each other, and we shouldn't have done that. We cannot let a world be spun out of that pain.''{/i}" if felina_rejection_count == 2:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''You reject the suffering of material reality, and yet you cling to its framework for meaning. We can be better than this.''{/i}" if felina_rejection_count == 3:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''You claim your destruction would steal meaning from existence, but if my actions can make existence worse, then there must be actions that make it better. Perfection implies finality, and nothing is final.''{/i}" if felina_rejection_count == 4:
                jump felina_rejection_join

            "{i}• ''I get it. There's no need for us to keep fighting. I'll leave with you. I just don't know how.'' [[Stop the fight early and surrender.]{/i}" if felina_round >= 2:
                $ achievement.grant("ACH_END_FREE2")
                jump felina_freedom_join

            "{i}• [[Remain silent.]{/i}":
                jump felina_silence

    jump felina_fight_staging

label felina_razor_start:

    if razor_end == "peace":
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
            show pop razor heart onlayer inyourface at shakeshort, Position(ypos=1125)
        else:
            $ previous_transform = "handsflip"
            show shifting hands onlayer front at flip, shakeshort, Position(ypos=1125)
            show pop razor heart onlayer inyourface at flip, shakeshort, Position(ypos=1125)
        with Dissolve(0.25)
        $ renpy.pause(1.90)

    elif razor_end == "fight":
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
            show pop razor sharp onlayer inyourface at shakeshort, Position(ypos=1125)
        else:
            $ previous_transform = "fierceflip"
            show shifting fierce onlayer front at flip, shakeshort, Position(ypos=1125)
            show pop razor sharp onlayer inyourface at flip, shakeshort, Position(ypos=1125)
        with Dissolve(0.25)
        $ renpy.pause(1.3)

    $ gallery_razor.unlock_item(20)
    $ renpy.save_persistent()
    play audio "audio/final/Razor_ImpaleSwordBody_6.flac"
    show fight razor onlayer inyourface at Position(ypos=1125)
    $ renpy.pause(0.01)
    voice "audio/voices/felina/fight/razor1.flac"
    mounds "A boundless torrent of blades cuts you from boundless angles. You are a body. You are gory ribbons. You are a body again. And you feel all of it.\n" id felina_razor_start_2f9dc7e4
    voice "audio/voices/felina/fight/razor2.flac"
    hide fight onlayer inyourface
    hide shifting onlayer front
    hide pop onlayer inyourface
    show farback quiet onlayer farback at Position(ypos=1125)
    show back awakening onlayer back at Position(ypos=1125)
    show midground awakening onlayer front at Position(ypos=1125)
    show hair awakened onlayer front at Position(ypos=1125)
    show dress felina onlayer front at Position(ypos=1125)
    show shifting pose talk onlayer front at Position(ypos=1125)
    show felina raz2 onlayer inyourface at Position(ypos=1125)
    with Dissolve(1.0)
    mounds "On and on it goes, until your bodies are not your thoughts are not you. Alive, dead, alive, dead, alive, dead, then alive and dead and alive and dead all at once.\n"

    if razor_end == "fight":
        #voice "audio/voices/felina/fight/razor3.flac"
        voice "audio/_pristine/voice/_climax/felina/68.flac"
        show shifting martyrs talk onlayer front
        show felina raz3 onlayer inyourface
        with dissolve
        mound "You learned to put yourself away. And in your stillness you rose above me.\n"
        #mound "You learned to put yourself away, and to follow the flow of reality. And you used it to rise above me.\n"
    if razor_end == "peace":
        #voice "audio/voices/felina/fight/razor4.flac"
        voice "audio/_pristine/voice/_climax/felina/69.flac"
        show shifting martyrs talk onlayer front
        show felina raz3 onlayer inyourface
        with dissolve
        #mound "You learned to put yourself away, and to follow the flow of reality. And you used it to humble me. To show me how far I was from what I needed to be."
        mound "You learned to put yourself away. And in your stillness you humbled me.\n"
    #voice "audio/voices/felina/fight/razor5.flac"
    voice "audio/_pristine/voice/_climax/felina/70.flac"
    show shifting pity smile talk onlayer front
    show felina raz1 onlayer inyourface
    with dissolve
    mound "You died countless steely deaths, and you lived countless short lives, and yet it is all so far behind you. I pushed you to a greatness you never would have reached without me.\n"
    #mound "You died countless steely deaths, and you lived countless short lives, and yet it is all so far behind you. Unjust impossibilities pushed you to become something you would never have been without them.\n"
    show shifting pity smile onlayer front
    label felina_razor_menu:
        menu:
            extend ""

            "{i}{outlinecolor=4f1313}• ''I did rise far above you. And I am far above you still. I will destroy you now as I destroyed you then.''{/outlinecolor}{/i}" if razor_end == "fight":
                jump felina_violence_join

            "{i}{outlinecolor=4f1313}• ''I didn't humble you. You humbled yourself. Just as you broke yourself upon me then, so will you break yourself upon me now.''{/outlinecolor}{/i}" if razor_end == "peace":
                jump felina_violence_join

            "{i}• (Explore) [[Address this vessel's statement directly.]{/i}":
                menu:
                    extend ""

                    "{i}• ''It didn't last. It wasn't worth it''{/i}" if razor_end == "peace":
                        voice "audio/voices/felina/fight/razor6.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting closed smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "And yet here we are, finally on the cusp of reaching something so much bigger than that little play.\n"

                    "{i}• ''If you hadn't snatched that body away, we would have killed each other. We were self-destructive.''{/i}" if razor_end == "fight":
                        voice "audio/voices/felina/fight/razor7.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting closed smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        $ felina_fight_effective_resistance += 1
                        mound "Were we self-destructive, or did the beauty of our dance reach beyond the shadow of death? It was lethality that made us what we were.\n"

                    "{i}• ''It felt so good to finally win, even if it was going to cost me my life.''{/i}" if razor_end == "fight":
                        label razor_felina_joy_join:
                            $ felina_fight_effective_resistance -= 1
                            #voice "audio/voices/felina/fight/razor8.flac"
                            voice "audio/_pristine/voice/_climax/felina/71a.flac"
                            play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                            show shifting closed smile talk onlayer front
                            hide felina onlayer inyourface
                            with dissolve
                            #mound "And it was a joy for me to finally face my end. Even when I thought I had reached an unconquerable peak, you showed me how much further I could still climb.\n"
                            mound "And it was a joy for me to finally face my end. Even when I thought I reached my limits, you showed me how much further I could climb.\n"

                    "{i}• ''After everything you put me through, it felt good to watch you fall apart.''{/i}" if razor_end == "peace":
                        jump razor_felina_joy_join

                    "{i}• ''Even if the journey was agony, the end gave the struggle meaning.''{/i}":
                        voice "audio/voices/felina/fight/razor9.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting martyrs talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "And even then, what we saw was not an ending. When I thought I had reached an unconquerable peak, you showed me how much further I could still climb.\n"

                    "{i}• (Return){/i}":
                        jump felina_razor_menu

            "{i}• [[Appeal to your shared humanity.] ''You speak about life and death and change and stagnation, but that isn't what any of this has been about.''{/i}" if felina_appeal_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''This has always just been about us. Two people forced to hurt each other again and again and again. But we don't have to hurt each other anymore.''{/i}" if felina_appeal_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''There can be love and conflict and beauty and ugliness between us without bringing the whole of reality into the picture.''{/i}" if felina_appeal_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''We're not the whole of reality. Why won't you see me the way I still see you? Why won't you see me for what I am?''{/i}" if felina_appeal_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''This doesn't have to be so big. You can come back down to my level. You can come back to me.''{/i}" if felina_appeal_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Reject her authority.] ''You've done nothing but lecture me since the minute I got here.''{/i}" if felina_lecture_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''You use all these pretentious metaphors and pretend you're making grand proclamations about who I am and who you are. But really you aren't saying much of anything.''{/i}" if felina_lecture_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''It doesn't even matter what I say to you, because you're just going to keep telling me your perspective like it's some universal truth.''{/i}" if felina_lecture_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''It was so much better when I was with your vessels. Even at their worst, they all still heard me.''{/i}" if felina_lecture_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''I don't know what you are, but you aren't any of them. You're just something wearing their skin.''{/i}" if felina_lecture_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Argue your independence.] ''You act as though the world can't exist without you. But I've existed without you.''{/i}" if felina_assert_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''What are the woods, then? What is the cabin? What is the time we've spent apart if not me existing as myself?''{/i}" if felina_assert_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''I wouldn't be here if destroying you would leave all of reality a colorless blur.''{/i}" if felina_assert_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''I'd rather trust an ignorant soul who died trying to make things better than a god who'd let the wheel of suffering turn forever.''{/i}" if felina_assert_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''If I need to destroy you to build a better world, then I will.''{/i}" if felina_assert_count == 4:
                $ felina_assert_lethal = True
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''Who said anything about destroying you? I just need to make you stop.''{/i}" if felina_assert_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Reject her perspective.] ''I won't engage with violence.''{/i}" if felina_rejection_count == 0:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''It doesn't matter how I feel. Death, suffering, and oblivion shouldn't fall on others. If we are able to transcend death, then we are responsible for those it holds captive.''{/i}" if felina_rejection_count == 1:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''Suffering born in delusion is still suffering. It doesn't matter what we are now. We hurt each other, and we shouldn't have done that. We cannot let a world be spun out of that pain.''{/i}" if felina_rejection_count == 2:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''You reject the suffering of material reality, and yet you cling to its framework for meaning. We can be better than this.''{/i}" if felina_rejection_count == 3:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''You claim your destruction would steal meaning from existence, but if my actions can make existence worse, then there must be actions that make it better. Perfection implies finality, and nothing is final.''{/i}" if felina_rejection_count == 4:
                jump felina_rejection_join

            "{i}• ''I get it. There's no need for us to keep fighting. I'll leave with you. I just don't know how.'' [[Stop the fight early and surrender.]{/i}" if felina_round >= 2:
                $ achievement.grant("ACH_END_FREE2")
                jump felina_freedom_join

            "{i}• [[Remain silent.]{/i}":
                jump felina_silence

    jump felina_fight_staging

label felina_spectre_start:

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
        show pop spectre onlayer inyourface at shakeshort, Position(ypos=1125)
    else:
        $ previous_transform = "horrorflip"
        show shifting horror onlayer front at flip, shakeshort, Position(ypos=1125)
        show pop spectre onlayer inyourface at flip, shakeshort, Position(ypos=1125)
    with Dissolve(0.25)
    $ renpy.pause(4.2)

    if spectre_end == "free":
        play audio "audio/final/Spectre_PossessingPlayer_5.flac"
        show fight spectre possession onlayer inyourface at Position(ypos=1125)
        $ renpy.pause(0.01)
    else:
        play audio "audio/final/Razor_ImpaleSwordBody_6.flac"
        show fight spectre exorcism onlayer inyourface at Position(ypos=1125)
        $ renpy.pause(0.01)

    $ gallery_spectre.unlock_item(18)
    $ renpy.save_persistent()
    #voice "audio/voices/felina/fight/spec1.flac"
    voice "audio/_pristine/voice/_climax/felina/72a.flac"
    mounds "A shiver passes through you as unseen fingers dance across your skin. They remember the violence you inflicted on them. And yet they don't return it.\n"
    #mounds "A shiver passes through you as unseen fingers, cold as the grave, dance across your skin. They remember the violence you inflicted on them. And yet they do not return it.\n"
    #voice "audio/voices/felina/fight/spec2.flac"
    voice "audio/_pristine/voice/_climax/felina/73.flac"
    hide fight onlayer inyourface
    hide shifting onlayer front
    hide pop onlayer inyourface
    show farback quiet onlayer farback at Position(ypos=1125)
    show back awakening onlayer back at Position(ypos=1125)
    show midground awakening onlayer front at Position(ypos=1125)
    show hair awakened onlayer front at Position(ypos=1125)
    show dress felina onlayer front at Position(ypos=1125)
    show shifting closed smile talk onlayer front at Position(ypos=1125)
    show felina spectre4 onlayer inyourface at Position(ypos=1125)
    with Dissolve(1.0)
    mound "I offer you absolution, and you take my hand in yours.\n"
    #mound "I offer you a path to your redemption, and you take my hand in yours.\n"
    if spectre_end == "free":
        voice "audio/voices/felina/fight/spec3.flac"
        show shifting martyrs talk onlayer front
        show felina spectre3 talk onlayer inyourface
        with dissolve
        mound "You felt the pain you caused another, and you were willing to sacrifice everything you thought was you to set me free.\n"
        voice "audio/voices/felina/fight/spec4.flac"
        show shifting pity smile talk onlayer front
        show felina spectre4 onlayer inyourface
        with dissolve
        mound "Without sin, there is no redemption.\n"

    if spectre_end == "slay":
        voice "audio/voices/felina/fight/spec5.flac"
        show shifting martyrs talk onlayer front
        show felina spectre3 talk onlayer inyourface
        with dissolve
        mound "But you do not follow my path. Hands clasped together, you break yourself, and you break me with you.\n"
        voice "audio/voices/felina/fight/spec6.flac"
        show shifting pity smile talk onlayer front
        show felina spectre4 onlayer inyourface
        with dissolve
        mound "You were willing to sacrifice everything you thought was you to end me again.\n"
    show shifting pity smile onlayer front
    label felina_spectre_menu:
        menu:
            extend ""

            #"{i}{outlinecolor=4f1313}• ''I killed you when I first saw you, and that didn't make me go away. The world doesn't need you.''{/outlinecolor}{/i}" if felina_violence_broken == False:
            #    jump felina_violence_join

            "{i}• (Explore) [[Address this vessel's statement directly.]{/i}":
                menu:
                    extend ""

                    "{i}• ''But without redemption there can be no sin.''{/i}" if spectre_end == "free":
                        $ felina_fight_effective_resistance += 1
                        voice "audio/voices/felina/fight/spec7.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "And without contrast, there can be nothing at all.\n"

                    "{i}• ''If I'd known what you were, I never would have freed you.''{/i}" if spectre_end == "free":
                        $ felina_fight_effective_resistance -= 1
                        voice "audio/_pristine/voice/_climax/felina/75b.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "Truth is a box with ever-changing contents. You knew me then, just as you know me now.\n"

                    "{i}• ''And I would sacrifice everything to free you again.''{/i}" if spectre_end == "free":
                        $ felina_fight_effective_resistance -= 1
                        voice "audio/voices/felina/fight/spec8.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "And yet there is nothing left for you to sacrifice, so long as you accept me with open arms.\n"

                    "{i}• ''I had to sacrifice myself. The entire world was at stake.''{/i}" if spectre_end == "slay":
                        voice "audio/voices/felina/fight/spec9.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "And your actions will echo in the tapestry of time. You gave yourself to a higher purpose.\n"

                    "{i}• ''I was glad to end us together.''{/i}" if spectre_end == "slay":
                        voice "audio/voices/felina/fight/spec10.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting martyrs talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "And the thread of that ending wove itself into yet another experience, which wove itself into yet another.\n"

                    "{i}• (Return){/i}":
                        jump felina_spectre_menu

            "{i}• [[Appeal to your shared humanity.] ''You speak about life and death and change and stagnation, but that isn't what any of this has been about.''{/i}" if felina_appeal_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''This has always just been about us. Two people forced to hurt each other again and again and again. But we don't have to hurt each other anymore.''{/i}" if felina_appeal_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''There can be love and conflict and beauty and ugliness between us without bringing the whole of reality into the picture.''{/i}" if felina_appeal_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''We're not the whole of reality. Why won't you see me the way I still see you? Why won't you see me for what I am?''{/i}" if felina_appeal_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''This doesn't have to be so big. You can come back down to my level. You can come back to me.''{/i}" if felina_appeal_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Reject her authority.] ''You've done nothing but lecture me since the minute I got here.''{/i}" if felina_lecture_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''You use all these pretentious metaphors and pretend you're making grand proclamations about who I am and who you are. But really you aren't saying much of anything.''{/i}" if felina_lecture_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''It doesn't even matter what I say to you, because you're just going to keep telling me your perspective like it's some universal truth.''{/i}" if felina_lecture_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''It was so much better when I was with your vessels. Even at their worst, they all still heard me.''{/i}" if felina_lecture_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''I don't know what you are, but you aren't any of them. You're just something wearing their skin.''{/i}" if felina_lecture_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Argue your independence.] ''You act as though the world can't exist without you. But I've existed without you.''{/i}" if felina_assert_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''What are the woods, then? What is the cabin? What is the time we've spent apart if not me existing as myself?''{/i}" if felina_assert_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''I wouldn't be here if destroying you would leave all of reality a colorless blur.''{/i}" if felina_assert_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''I'd rather trust an ignorant soul who died trying to make things better than a god who'd let the wheel of suffering turn forever.''{/i}" if felina_assert_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''If I need to destroy you to build a better world, then I will.''{/i}" if felina_assert_count == 4:
                $ felina_assert_lethal = True
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''Who said anything about destroying you? I just need to make you stop.''{/i}" if felina_assert_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Reject her perspective.] ''I won't engage with violence.''{/i}" if felina_rejection_count == 0:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''It doesn't matter how I feel. Death, suffering, and oblivion shouldn't fall on others. If we are able to transcend death, then we are responsible for those it holds captive.''{/i}" if felina_rejection_count == 1:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''Suffering born in delusion is still suffering. It doesn't matter what we are now. We hurt each other, and we shouldn't have done that. We cannot let a world be spun out of that pain.''{/i}" if felina_rejection_count == 2:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''You reject the suffering of material reality, and yet you cling to its framework for meaning. We can be better than this.''{/i}" if felina_rejection_count == 3:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''You claim your destruction would steal meaning from existence, but if my actions can make existence worse, then there must be actions that make it better. Perfection implies finality, and nothing is final.''{/i}" if felina_rejection_count == 4:
                jump felina_rejection_join

            "{i}• ''I get it. There's no need for us to keep fighting. I'll leave with you. I just don't know how.'' [[Stop the fight early and surrender.]{/i}" if felina_round >= 2:
                $ achievement.grant("ACH_END_FREE2")
                jump felina_freedom_join

            "{i}• [[Remain silent.]{/i}":
                jump felina_silence

    jump felina_fight_staging

label felina_stranger_start:

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
        show pop stranger onlayer inyourface at shakeshort, Position(ypos=1125)
    else:
        $ previous_transform = "handsflip"
        show shifting hands onlayer front at flip, shakeshort, Position(ypos=1125)
        show pop stranger onlayer inyourface at flip, shakeshort, Position(ypos=1125)
    with Dissolve(0.25)
    $ renpy.pause(1.90)
    $ gallery_stranger.unlock_item(12)
    $ renpy.save_persistent()
    play audio "audio/final/Stranger_BodiesIntoOne_1.flac"
    show fight stranger onlayer inyourface at Position(ypos=1125)
    $ renpy.pause(0.01)
    voice "audio/_pristine/voice/_climax/felina/76a.flac"
    mounds "My masses mob you. There is no beginning to them and there is no end. There is only the flood of bodies. In every moment you hold every possible sensation at once, and then you hold them all again.\n"
    voice "audio/_pristine/voice/_climax/felina/77b.flac"
    hide fight onlayer inyourface
    hide shifting onlayer front
    hide pop onlayer inyourface
    show farback quiet onlayer farback at Position(ypos=1125)
    show back awakening onlayer back at Position(ypos=1125)
    show midground awakening onlayer front at Position(ypos=1125)
    show hair awakened onlayer front at Position(ypos=1125)
    show dress felina onlayer front at Position(ypos=1125)
    show shifting martyrs talk onlayer front at Position(ypos=1125)
    show felina stranger2 talk onlayer inyourface at Position(ypos=1125)
    with Dissolve(1.0)
    mound "But in the end, you reflected it back at me. For a brief moment, both of us were everything.\n"
    voice "audio/_pristine/voice/_climax/felina/78a.flac"
    show shifting smile talk onlayer front
    show felina stranger3 onlayer inyourface
    with dissolve
    mound "We can be everything again. We can weave a beautiful and endless song.\n"
    show shifting smile onlayer front

    label felina_stranger_menu:
        menu:
            extend ""

            "{i}{outlinecolor=4f1313}• ''I saw every version of us across every reality, and not every reality had you drawing breath. Even then, I went on. The world doesn't need you.''{/outlinecolor}{/i}":
                jump felina_violence_join

            "{i}• (Explore) [[Address this vessel's statement directly.]{/i}":
                menu:
                    extend ""

                    "{i}• ''To be everything at once is the same as being nothing at all. Why would either of us want that?''{/i}":
                        voice "audio/_pristine/voice/_climax/felina/79.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting closed smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "Here is where words fail us. So long as we both exist, we will always be distinct. The only thing to fear is a reality without me.\n"

                    "{i}• ''To contain everything is to contain every evil alongside every good. Can we not shed the confines of our old selves and create?''{/i}":
                        voice "audio/_pristine/voice/_climax/felina/80.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting closed smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "Without the contrast of pain, pleasure is muted, made dull by the assurance that it will always be. A song that is only sweet is a pale horizon that never falls.\n"

                    "{i}• ''I couldn't understand you then, but I think I understand you now.''{/i}":
                        voice "audio/voices/felina/fight/strange4.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "You saw with a single pair of eyes what you needed dozens to comprehend.\n"
                        label felina_stranger_join:
                            #voice "audio/voices/felina/fight/strange5.flac"
                            voice "audio/_pristine/voice/_climax/felina/81a.flac"
                            show shifting closed smile talk onlayer front
                            with dissolve
                            #mound "And now here we are, each with millions of eyes and all of them opening to what we are.\n"
                            mound "And now here we are, each with millions of eyes and all of them open.\n"

                    "{i}• ''You seemed in pain. I'm sorry for what I did to you, but it was the only thing I could do.''{/i}":
                        voice "audio/voices/felina/fight/strange6.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "I saw with a single pair of eyes what I needed dozens to comprehend.\n"
                        jump felina_stranger_join

                    "{i}• (Return){/i}":
                        jump felina_stranger_menu

            "{i}• [[Appeal to your shared humanity.] ''You speak about life and death and change and stagnation, but that isn't what any of this has been about.''{/i}" if felina_appeal_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''This has always just been about us. Two people forced to hurt each other again and again and again. But we don't have to hurt each other anymore.''{/i}" if felina_appeal_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''There can be love and conflict and beauty and ugliness between us without bringing the whole of reality into the picture.''{/i}" if felina_appeal_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''We're not the whole of reality. Why won't you see me the way I still see you? Why won't you see me for what I am?''{/i}" if felina_appeal_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''This doesn't have to be so big. You can come back down to my level. You can come back to me.''{/i}" if felina_appeal_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Reject her authority.] ''You've done nothing but lecture me since the minute I got here.''{/i}" if felina_lecture_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''You use all these pretentious metaphors and pretend you're making grand proclamations about who I am and who you are. But really you aren't saying much of anything.''{/i}" if felina_lecture_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''It doesn't even matter what I say to you, because you're just going to keep telling me your perspective like it's some universal truth.''{/i}" if felina_lecture_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''It was so much better when I was with your vessels. Even at their worst, they all still heard me.''{/i}" if felina_lecture_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''I don't know what you are, but you aren't any of them. You're just something wearing their skin.''{/i}" if felina_lecture_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Argue your independence.] ''You act as though the world can't exist without you. But I've existed without you.''{/i}" if felina_assert_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''What are the woods, then? What is the cabin? What is the time we've spent apart if not me existing as myself?''{/i}" if felina_assert_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''I wouldn't be here if destroying you would leave all of reality a colorless blur.''{/i}" if felina_assert_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''I'd rather trust an ignorant soul who died trying to make things better than a god who'd let the wheel of suffering turn forever.''{/i}" if felina_assert_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''If I need to destroy you to build a better world, then I will.''{/i}" if felina_assert_count == 4:
                $ felina_assert_lethal = True
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''Who said anything about destroying you? I just need to make you stop.''{/i}" if felina_assert_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Reject her perspective.] ''I won't engage with violence.''{/i}" if felina_rejection_count == 0:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''It doesn't matter how I feel. Death, suffering, and oblivion shouldn't fall on others. If we are able to transcend death, then we are responsible for those it holds captive.''{/i}" if felina_rejection_count == 1:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''Suffering born in delusion is still suffering. It doesn't matter what we are now. We hurt each other, and we shouldn't have done that. We cannot let a world be spun out of that pain.''{/i}" if felina_rejection_count == 2:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''You reject the suffering of material reality, and yet you cling to its framework for meaning. We can be better than this.''{/i}" if felina_rejection_count == 3:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''You claim your destruction would steal meaning from existence, but if my actions can make existence worse, then there must be actions that make it better. Perfection implies finality, and nothing is final.''{/i}" if felina_rejection_count == 4:
                jump felina_rejection_join

            "{i}• ''I get it. There's no need for us to keep fighting. I'll leave with you. I just don't know how.'' [[Stop the fight early and surrender.]{/i}" if felina_round >= 2:
                $ achievement.grant("ACH_END_FREE2")
                jump felina_freedom_join

            "{i}• [[Remain silent.]{/i}":
                jump felina_silence

    jump felina_fight_staging

label felina_tower_start:
    default come_from_tower = False
    $ come_from_tower = True
    if tower_end == "submit":
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
            show pop tower onlayer front at shakeshort, Position(ypos=1125)
            show shifting dance onlayer front at shakeshort, Position(ypos=1125)
        else:
            $ previous_transform = "danceflip"
            show pop tower onlayer front at flip, shakeshort, Position(ypos=1125)
            show shifting dance onlayer front at flip, shakeshort, Position(ypos=1125)
        with Dissolve(0.25)
        $ renpy.pause(1.45)
        $ gallery_tower.unlock_item(13)
        $ renpy.save_persistent()
        play audio "audio/one_shot/collapse.flac"
        show fight tower onlayer inyourface at Position(ypos=1125)
        $ renpy.pause(0.01)
        voice "audio/_pristine/voice/_climax/felina//28a.flac"
        mounds "You are nothing. A black hole of self-loathing fed by the matter of your restless thoughts. A dog blind to its leash. But there is no light without the dark.\n"
        voice "audio/_pristine/voice/_climax/felina//29.flac"
        hide fight onlayer inyourface
        hide shifting onlayer front
        hide pop onlayer front
        show farback quiet onlayer farback at Position(ypos=1125)
        show back awakening onlayer back at Position(ypos=1125)
        show midground awakening onlayer front at Position(ypos=1125)
        show felina tower2 onlayer front at Position(ypos=1125)
        show hair awakened onlayer front at Position(ypos=1125)
        show dress felina onlayer front at Position(ypos=1125)
        show shifting pose talk onlayer front at Position(ypos=1125)
        with Dissolve(1.0)
        mounds "When I proclaimed my godhood and offered you a place at my side, you gladly became the instrument of my new creation.\n"
        voice "audio/_pristine/voice/_climax/felina//30c.flac"
        show shifting pity smile talk onlayer front
        show felina tower3 onlayer front
        with dissolve
        mound "Only with both of us is there a future to look towards. It is hope that carves meaning into being.\n"

    if apotheosis_end == "defy" or apotheosis_end == "prison":
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
            show pop apotheosis onlayer front at shakeshort, Position(ypos=1125)
            show shifting hands onlayer front at shakeshort, Position(ypos=1125)
        else:
            $ previous_transform = "handsflip"
            show pop apotheosis onlayer front at flip, shakeshort, Position(ypos=1125)
            show shifting hands onlayer front at flip, shakeshort, Position(ypos=1125)
        with Dissolve(0.25)
        $ renpy.pause(1.90)
        $ gallery_apotheosis.unlock_item(20)
        $ renpy.save_persistent()
        voice "audio/_pristine/voice/_climax/felina/_temp/34.flac"
        play audio "audio/final/Tower_Earthquake_oneshot_faded_1.flac"
        play tertiary "audio/_pristine/sfx/Apotheosis HiPitch tear_4.flac"
        show fight apotheosis knife onlayer inyourface at Position(ypos=1125)
        $ renpy.pause(0.01)
        voice sustain
        with Dissolve(1.0)
        mounds "You are weightless and alone, suspended in the gravity of an idea too great for you to hold. A tiny island caught between the death of the old and the birth of the new.\n"
        voice "audio/_pristine/voice/_climax/felina/_temp/35.flac"
        hide fight onlayer inyourface
        hide shifting onlayer front
        hide pop onlayer front
        show farback quiet onlayer farback at Position(ypos=1125)
        show back awakening onlayer back at Position(ypos=1125)
        show midground awakening onlayer front at Position(ypos=1125)
        show felina apotheosis3 talk onlayer front at Position(ypos=1125)
        show hair awakened onlayer front at Position(ypos=1125)
        show dress felina onlayer front at Position(ypos=1125)
        show shifting pose talk onlayer front at Position(ypos=1125)
        with Dissolve(2.0)
        mound "But you did not go quietly. You spat in the eye of that which would claim godhood, and through that defiance, you bound us both together.\n"
        voice "audio/_pristine/voice/_climax/felina/_temp/36.flac"
        show shifting pity smile talk onlayer front at Position(ypos=1125)
        show felina apotheosis4 onlayer front
        with dissolve
        mound "Without me, there are no externalities to resist, and without you to resist me, there can be no externalities. It is struggle that carves meaning into consciousness.\n"
        show shifting pity smile onlayer front

    if apotheosis_end == "unraveled":
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
            show pop apotheosis onlayer front at shakeshort, Position(ypos=1125)
            show shifting hands onlayer front at shakeshort, Position(ypos=1125)
        else:
            $ previous_transform = "handsflip"
            show pop apotheosis onlayer front at flip, shakeshort, Position(ypos=1125)
            show shifting hands onlayer front at flip, shakeshort, Position(ypos=1125)
        with Dissolve(0.25)
        $ renpy.pause(1.90)
        $ gallery_apotheosis.unlock_item(20)
        $ renpy.save_persistent()
        voice "audio/_pristine/voice/_climax/felina/_temp/38.flac"
        play audio "audio/final/Tower_Earthquake_oneshot_faded_1.flac"
        play tertiary "audio/_pristine/sfx/Apotheosis HiPitch tear_4.flac"
        show fight apotheosis knife onlayer inyourface at Position(ypos=1125)
        mounds "You are weightless and alone, suspended in the gravity of an idea too great for you to hold. A tiny island caught between the death of the old and the birth of the new. But weightless is not helpless.\n"
        voice "audio/_pristine/voice/_climax/felina/_temp/39a.flac"
        hide fight onlayer inyourface
        hide shifting onlayer front
        hide pop onlayer front
        show farback quiet onlayer farback at Position(ypos=1125)
        show back awakening onlayer back at Position(ypos=1125)
        show midground awakening onlayer front at Position(ypos=1125)
        show felina apotheosis3 talk onlayer front at Position(ypos=1125)
        show hair awakened onlayer front at Position(ypos=1125)
        show dress felina onlayer front at Position(ypos=1125)
        show shifting pose talk onlayer front at Position(ypos=1125)
        with Dissolve(2.0)
        mound "You unchained your will and rose against a would-be god, and for a shining moment, made yourself my equal. And then, you surpassed me.\n"
        #voice "audio/voices/felina/fight/t7.flac"
        #mounds "When you were confronted with my vessel's apotheosis, you chose against all odds to defy me. To hold on to your inner self, with all its flaws, even in the scorching light of my divinity.\n"
        #voice "audio/_pristine/voice/_climax/felina/_temp/40.flac"
        voice "audio/_pristine/voice/_climax/felina/_temp/36.flac"
        show felina apotheosis4 onlayer front
        show shifting martyrs talk onlayer front
        with dissolve
        mound "Without me, there are no externalities to resist, and without you to resist me, there can be no externalities. It is struggle that carves meaning into consciousness.\n"
        #mound "Without obstacles there is no growth, and without growth there can be nothing at all. It is purpose that carves meaning into being.\n"
        show shifting martyrs onlayer front

    if apotheosis_end == "fly":
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
            show pop apotheosis onlayer front at shakeshort, Position(ypos=1125)
            show shifting hands onlayer front at shakeshort, Position(ypos=1125)
        else:
            $ previous_transform = "handsflip"
            show pop apotheosis onlayer front at flip, shakeshort, Position(ypos=1125)
            show shifting hands onlayer front at flip, shakeshort, Position(ypos=1125)
        with Dissolve(0.25)
        $ renpy.pause(1.90)
        $ gallery_apotheosis.unlock_item(20)
        $ renpy.save_persistent()
        voice "audio/_pristine/voice/_climax/felina/_temp/31.flac"
        play audio "audio/final/Tower_Earthquake_oneshot_faded_1.flac"
        play tertiary "audio/final/Tower_StormThunder_oneshot_faded_1.flac"
        show fight apotheosis giveup onlayer inyourface at Position(ypos=1125)
        mounds "You are weightless and alone, suspended in the gravity of an idea too great for you to hold. The very ground beneath your feet loses its meaning. There is nothing but me.\n"
        voice "audio/_pristine/voice/_climax/felina/_temp/32a.flac"
        hide fight onlayer inyourface
        hide shifting onlayer front
        hide pop onlayer front
        show farback quiet onlayer farback at Position(ypos=1125)
        show back awakening onlayer back at Position(ypos=1125)
        show midground awakening onlayer front at Position(ypos=1125)
        show felina apotheosis3 talk onlayer front at Position(ypos=1125)
        show hair awakened onlayer front at Position(ypos=1125)
        show dress felina onlayer front at Position(ypos=1125)
        show shifting pose talk onlayer front at Position(ypos=1125)
        with Dissolve(2.0)
        mound "When you were confronted with my vessel's apotheosis, you chose to accept me, to allow me to burn away all doubt and turn you into an instrument of my divine will. You accepted that I was everything, and together we found our purpose.\n"
        voice "audio/_pristine/voice/_climax/felina/30a.flac"
        show felina apotheosis4 onlayer front
        show shifting martyrs talk onlayer front
        with dissolve
        mound "Only with both of us is there a future to look towards. It is hope that carves meaning into consciousness.\n"

    show shifting martyrs onlayer front

    label felina_tower_menu:
        menu:
            extend ""

            "{i}{outlinecolor=4f1313}• ''Even when you became a shadow of a god, one good shot was all it took to bring you crashing down.''{/outlinecolor}{/i}" if apotheosis_end == "defy":
                jump felina_violence_join

            "{i}{outlinecolor=4f1313}• ''Even when you became a shadow of a god, still you were bound to my will. I denied you apotheosis then, and I will deny you apotheosis now.''{/outlinecolor}{/i}" if apotheosis_end == "prison":
                jump felina_violence_join

            "{i}{outlinecolor=4f1313}• ''Even when you became a shadow of a god, still you were bound to my will. I unraveled you then, and there is nothing stopping me from unraveling you now.''{/outlinecolor}{/i}" if apotheosis_end == "unraveled":
                jump felina_violence_join

            "{i}• (Explore) [[Address this vessel's statement directly.]{/i}":
                menu:
                    extend ""

                    "{i}• ''I still defy you now.''{/i}" if apotheosis_end == "defy":
                        $ felina_fight_effective_resistance += 1
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        voice "audio/voices/felina/fight/t10.flac"
                        hide shifting onlayer front
                        hide farback onlayer farback
                        hide back onlayer back
                        hide midground onlayer front
                        hide hair onlayer front
                        hide shifting onlayer front
                        hide dress onlayer front
                        hide felina onlayer back
                        hide felina onlayer front
                        show farback quiet onlayer farback at Position(ypos=1125)
                        show back awakening onlayer back at Position(ypos=1125)
                        show midground awakening onlayer front at Position(ypos=1125)
                        show hair awakened onlayer front at Position(ypos=1125)
                        show dress felina onlayer front at Position(ypos=1125)
                        show shifting closed smile talk onlayer front at Position(ypos=1125)
                        with Dissolve(1.0)
                        mound "But in your defiance I have already won. There is no power without resistance. Our actions feed each other into something greater.\n"

                    "{i}• ''We were so close to freedom.''{/i}" if apotheosis_end == "fly":
                        $ felina_fight_effective_resistance -= 1
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        voice "audio/_pristine/voice/_climax/felina/_temp/41.flac"
                        hide shifting onlayer front
                        hide farback onlayer farback
                        hide back onlayer back
                        hide midground onlayer front
                        hide hair onlayer front
                        hide shifting onlayer front
                        hide dress onlayer front
                        hide felina onlayer back
                        hide felina onlayer front
                        show farback quiet onlayer farback at Position(ypos=1125)
                        show back awakening onlayer back at Position(ypos=1125)
                        show midground awakening onlayer front at Position(ypos=1125)
                        show hair awakened onlayer front at Position(ypos=1125)
                        show dress felina onlayer front at Position(ypos=1125)
                        show shifting closed smile talk onlayer front at Position(ypos=1125)
                        with Dissolve(1.0)
                        mound "And we are so close to freedom again, if you'll let us have it.\n"

                    "{i}• ''It was you who stopped us from escaping.''{/i}" if apotheosis_end == "fly":
                        $ felina_fight_effective_resistance += 1
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        voice "audio/_pristine/voice/_climax/felina/_temp/42a.flac"
                        hide shifting onlayer front
                        hide farback onlayer farback
                        hide back onlayer back
                        hide midground onlayer front
                        hide hair onlayer front
                        hide shifting onlayer front
                        hide dress onlayer front
                        hide felina onlayer back
                        hide felina onlayer front
                        show farback quiet onlayer farback at Position(ypos=1125)
                        show back awakening onlayer back at Position(ypos=1125)
                        show midground awakening onlayer front at Position(ypos=1125)
                        show hair awakened onlayer front at Position(ypos=1125)
                        show dress felina onlayer front at Position(ypos=1125)
                        show shifting martyrs talk onlayer front at Position(ypos=1125)
                        with Dissolve(1.0)
                        mound "We weren't ready for it then, but we are now.\n"

                    "{i}• ''I'm sorry for what I did to you.''{/i}" if apotheosis_end == "prison" or apotheosis_end == "defy" or apotheosis_end == "unraveled":
                        $ felina_fight_effective_resistance -= 1
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        voice "audio/_pristine/voice/_climax/felina/_temp/43a.flac"
                        hide shifting onlayer front
                        hide farback onlayer farback
                        hide back onlayer back
                        hide midground onlayer front
                        hide hair onlayer front
                        hide shifting onlayer front
                        hide dress onlayer front
                        hide felina onlayer back
                        hide felina onlayer front
                        show farback quiet onlayer farback at Position(ypos=1125)
                        show back awakening onlayer back at Position(ypos=1125)
                        show midground awakening onlayer front at Position(ypos=1125)
                        show hair awakened onlayer front at Position(ypos=1125)
                        show dress felina onlayer front at Position(ypos=1125)
                        show shifting martyrs talk onlayer front at Position(ypos=1125)
                        with Dissolve(1.0)
                        mound "Don't be. Everything we've done has shaped who we are.\n"

                    "{i}• ''We made each other worse.''{/i}" if apotheosis_end == "prison" or apotheosis_end == "defy" or apotheosis_end == "unraveled":
                        $ felina_fight_effective_resistance += 1
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        voice "audio/_pristine/voice/_climax/felina/_temp/44.flac"
                        hide shifting onlayer front
                        hide farback onlayer farback
                        hide back onlayer back
                        hide midground onlayer front
                        hide hair onlayer front
                        hide shifting onlayer front
                        hide dress onlayer front
                        hide felina onlayer back
                        hide felina onlayer front
                        show farback quiet onlayer farback at Position(ypos=1125)
                        show back awakening onlayer back at Position(ypos=1125)
                        show midground awakening onlayer front at Position(ypos=1125)
                        show hair awakened onlayer front at Position(ypos=1125)
                        show dress felina onlayer front at Position(ypos=1125)
                        show shifting martyrs talk onlayer front at Position(ypos=1125)
                        with Dissolve(1.0)
                        mound "We changed each other. Are you not happy with who you've become?\n"

                    "{i}• ''You ripped me open then. I was only returning the favor.''{/i}" if apotheosis_end == "prison" or apotheosis_end == "unraveled":
                        $ felina_fight_effective_resistance += 1
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        voice "audio/_pristine/voice/_climax/felina/_temp/45a.flac"
                        hide shifting onlayer front
                        hide farback onlayer farback
                        hide back onlayer back
                        hide midground onlayer front
                        hide hair onlayer front
                        hide shifting onlayer front
                        hide dress onlayer front
                        hide felina onlayer back
                        hide felina onlayer front
                        show farback quiet onlayer farback at Position(ypos=1125)
                        show back awakening onlayer back at Position(ypos=1125)
                        show midground awakening onlayer front at Position(ypos=1125)
                        show hair awakened onlayer front at Position(ypos=1125)
                        show dress felina onlayer front at Position(ypos=1125)
                        show shifting martyrs talk onlayer front at Position(ypos=1125)
                        with Dissolve(1.0)
                        mound "You linger in moments that have long-since passed. We changed each other. Are you not happy with who you've become?\n"

                    "{i}• ''I miss when that was you.''{/i}":
                        $ felina_fight_effective_resistance -= 1
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        voice "audio/voices/felina/fight/t11.flac"
                        hide shifting onlayer front
                        hide farback onlayer farback
                        hide back onlayer back
                        hide midground onlayer front
                        hide hair onlayer front
                        hide shifting onlayer front
                        hide dress onlayer front
                        hide felina onlayer front
                        hide felina onlayer back
                        show farback quiet onlayer farback at Position(ypos=1125)
                        show back awakening onlayer back at Position(ypos=1125)
                        show midground awakening onlayer front at Position(ypos=1125)
                        show hair awakened onlayer front at Position(ypos=1125)
                        show dress felina onlayer front at Position(ypos=1125)
                        show shifting pity smile talk onlayer front at Position(ypos=1125)
                        with Dissolve(1.0)
                        mound "My threads, like yours, are unbroken. She is me as much as I was her.\n"

                    "{i}• ''Submitting to you was a mistake. I would have destroyed you if I knew what you were.''{/i}" if apotheosis_end == "fly" or tower_end == "submit":
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        voice "audio/voices/felina/fight/t12.flac"
                        hide shifting onlayer front
                        hide farback onlayer farback
                        hide felina onlayer front
                        hide back onlayer back
                        hide midground onlayer front
                        hide hair onlayer front
                        hide shifting onlayer front
                        hide dress onlayer front
                        hide felina onlayer back
                        show farback quiet onlayer farback at Position(ypos=1125)
                        show back awakening onlayer back at Position(ypos=1125)
                        show midground awakening onlayer front at Position(ypos=1125)
                        show hair awakened onlayer front at Position(ypos=1125)
                        show dress felina onlayer front at Position(ypos=1125)
                        show shifting closed smile talk onlayer front at Position(ypos=1125)
                        with Dissolve(1.0)
                        mound "You knew what I was then, just as you know what I am now.\n"

                    "{i}• ''You were consumed by your own ego.''{/i}":
                        $ felina_fight_effective_resistance += 1
                        if apotheosis_end == "unraveled" or apotheosis_end == "defy" or apotheosis_end == "prison":
                            voice "audio/voices/felina/fight/t13.flac"
                            play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                            hide shifting onlayer front
                            hide farback onlayer farback
                            hide back onlayer back
                            hide midground onlayer front
                            hide felina onlayer front
                            hide hair onlayer front
                            hide shifting onlayer front
                            hide dress onlayer front
                            hide felina onlayer back
                            show farback quiet onlayer farback at Position(ypos=1125)
                            show back awakening onlayer back at Position(ypos=1125)
                            show midground awakening onlayer front at Position(ypos=1125)
                            show hair awakened onlayer front at Position(ypos=1125)
                            show dress felina onlayer front at Position(ypos=1125)
                            show shifting serious talk onlayer front at Position(ypos=1125)
                            with Dissolve(1.0)
                            mound "And you shed your doubts to rise against me. It was only together that we were able to create something beautiful.\n"
                        else:
                            voice "audio/voices/felina/fight/t14.flac"
                            play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                            hide shifting onlayer front
                            hide farback onlayer farback
                            hide back onlayer back
                            hide midground onlayer front
                            hide felina onlayer front
                            hide hair onlayer front
                            hide shifting onlayer front
                            hide dress onlayer front
                            hide felina onlayer back
                            show farback quiet onlayer farback at Position(ypos=1125)
                            show back awakening onlayer back at Position(ypos=1125)
                            show midground awakening onlayer front at Position(ypos=1125)
                            show hair awakened onlayer front at Position(ypos=1125)
                            show dress felina onlayer front at Position(ypos=1125)
                            show shifting pissed talk onlayer front at Position(ypos=1125)
                            with Dissolve(1.0)
                            mound "And through your lack of one, you, too, were consumed. Yet together we were able to create something beautiful.\n"

                    "{i}• (Return){/i}":
                        jump felina_tower_menu

            "{i}• [[Appeal to your shared humanity.] ''You speak about life and death and change and stagnation, but that isn't what any of this has been about.''{/i}" if felina_appeal_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''This has always just been about us. Two people forced to hurt each other again and again and again. But we don't have to hurt each other anymore.''{/i}" if felina_appeal_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''There can be love and conflict and beauty and ugliness between us without bringing the whole of reality into the picture.''{/i}" if felina_appeal_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''We're not the whole of reality. Why won't you see me the way I still see you? Why won't you see me for what I am?''{/i}" if felina_appeal_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''This doesn't have to be so big. You can come back down to my level. You can come back to me.''{/i}" if felina_appeal_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Reject her authority.] ''You've done nothing but lecture me since the minute I got here.''{/i}" if felina_lecture_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''You use all these pretentious metaphors and pretend you're making grand proclamations about who I am and who you are. But really you aren't saying much of anything.''{/i}" if felina_lecture_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''It doesn't even matter what I say to you, because you're just going to keep telling me your perspective like it's some universal truth.''{/i}" if felina_lecture_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''It was so much better when I was with your vessels. Even at their worst, they all still heard me.''{/i}" if felina_lecture_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''I don't know what you are, but you aren't any of them. You're just something wearing their skin.''{/i}" if felina_lecture_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Argue your independence.] ''You act as though the world can't exist without you. But I've existed without you.''{/i}" if felina_assert_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''What are the woods, then? What is the cabin? What is the time we've spent apart if not me existing as myself?''{/i}" if felina_assert_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''I wouldn't be here if destroying you would leave all of reality a colorless blur.''{/i}" if felina_assert_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''I'd rather trust an ignorant soul who died trying to make things better than a god who'd let the wheel of suffering turn forever.''{/i}" if felina_assert_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''If I need to destroy you to build a better world, then I will.''{/i}" if felina_assert_count == 4:
                $ felina_assert_lethal = True
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''Who said anything about destroying you? I just need to make you stop.''{/i}" if felina_assert_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Reject her perspective.] ''I won't engage with violence.''{/i}" if felina_rejection_count == 0:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''It doesn't matter how I feel. Death, suffering, and oblivion shouldn't fall on others. If we are able to transcend death, then we are responsible for those it holds captive.''{/i}" if felina_rejection_count == 1:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''Suffering born in delusion is still suffering. It doesn't matter what we are now. We hurt each other, and we shouldn't have done that. We cannot let a world be spun out of that pain.''{/i}" if felina_rejection_count == 2:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''You reject the suffering of material reality, and yet you cling to its framework for meaning. We can be better than this.''{/i}" if felina_rejection_count == 3:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''You claim your destruction would steal meaning from existence, but if my actions can make existence worse, then there must be actions that make it better. Perfection implies finality, and nothing is final.''{/i}" if felina_rejection_count == 4:
                jump felina_rejection_join

            "{i}• ''I get it. There's no need for us to keep fighting. I'll leave with you. I just don't know how.'' [[Stop the fight early and surrender.]{/i}" if felina_round >= 2:
                $ achievement.grant("ACH_END_FREE2")
                jump felina_freedom_join

            "{i}• [[Remain silent.]{/i}":
                jump felina_silence

    jump felina_fight_staging

label felina_witch_start:

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
        show pop witch onlayer inyourface at shakeshort, Position(ypos=1125)
    else:
        $ previous_transform = "danceflip"
        show shifting dance onlayer front at flip, shakeshort, Position(ypos=1125)
        show pop witch onlayer inyourface at flip, shakeshort, Position(ypos=1125)
    with Dissolve(0.25)
    $ renpy.pause(1.45)
    if witch_end == "witch_betray_lock":
        $ gallery_witch.unlock_item(20)
        $ renpy.save_persistent()
        play audio "audio/one_shot/door_close.flac"
        show fight witch slam onlayer inyourface at Position(ypos=1125)
    else:
        $ gallery_witch.unlock_item(19)
        $ renpy.save_persistent()
        play audio "audio/final/Nightmare_NeckCrack_1.flac"
        show fight witch broken onlayer inyourface at Position(ypos=1125)
    $ renpy.pause(0.01)
    voice "audio/voices/felina/fight/witch1.flac"
    mounds "A trick behind your back, and a trick behind mine. We dance, revolving and revolving around each other, but forever stuck in place. We both move and yet we both don't, for each of us watches the other instead of ourselves.\n"
    if witch_end == "witch_betray_lock":
        voice "audio/voices/felina/fight/witch2.flac"
        hide fight onlayer inyourface
        hide shifting onlayer front
        hide pop onlayer inyourface
        show farback quiet onlayer farback at Position(ypos=1125)
        show back awakening onlayer back at Position(ypos=1125)
        show midground awakening onlayer front at Position(ypos=1125)
        show hair awakened onlayer front at Position(ypos=1125)
        show dress felina onlayer front at Position(ypos=1125)
        show shifting smile talk onlayer front at Position(ypos=1125)
        show felina witch2 talk onlayer inyourface at Position(ypos=1125)
        with Dissolve(1.0)
        mounds "But forever is not forever. You let me move and I slam the door, but that is not the end, and both of us must face our partner once again. The barbs twist deeper, but they do not have to.\n"
    elif witch_end == "witch_betray":
        voice "audio/voices/felina/fight/witch3.flac"
        hide fight onlayer inyourface
        hide shifting onlayer front
        hide pop onlayer inyourface
        show farback quiet onlayer farback at Position(ypos=1125)
        show back awakening onlayer back at Position(ypos=1125)
        show midground awakening onlayer front at Position(ypos=1125)
        show hair awakened onlayer front at Position(ypos=1125)
        show dress felina onlayer front at Position(ypos=1125)
        show shifting smile talk onlayer front at Position(ypos=1125)
        show felina witch2 talk onlayer inyourface at Position(ypos=1125)
        with Dissolve(1.0)
        mounds "But forever is not forever. I move and you react and both of us break the other. But broken is only a moment in time.\n"
    elif witch_end == "player_betray":
        voice "audio/voices/felina/fight/witch4.flac"
        #mound
        #voice "audio/voices/felina/fight/witch3.flac"
        hide fight onlayer inyourface
        hide shifting onlayer front
        hide pop onlayer inyourface
        show farback quiet onlayer farback at Position(ypos=1125)
        show back awakening onlayer back at Position(ypos=1125)
        show midground awakening onlayer front at Position(ypos=1125)
        show hair awakened onlayer front at Position(ypos=1125)
        show dress felina onlayer front at Position(ypos=1125)
        show shifting smile talk onlayer front at Position(ypos=1125)
        show felina witch2 talk onlayer inyourface at Position(ypos=1125)
        with Dissolve(1.0)
        mounds "But forever is not forever. You move and I react and both of us break the other. But broken is only a moment in time.\n" id felina_witch_start_ec0c8f12
    voice "audio/voices/felina/fight/witch5.flac"
    show shifting closed smile talk onlayer front
    show felina witch3 onlayer inyourface
    with dissolve
    mound "To change is to hold the potential to rise above. Would you limit yourself to what you are now, or would you like to see what you might become tomorrow?\n"
    label felina_witch_menu:
        menu:
            extend ""

            "{i}• (Explore) [[Address this vessel's statement directly.]{/i}":
                menu:
                    extend ""

                    "{i}• ''If there are no endings, there are no limits. If there are no limits, then there is no difference between growth and decay.''{/i}":
                        $ felina_fight_effective_resistance += 1
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        voice "audio/voices/felina/fight/witch6.flac"
                        show shifting pissed talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "Meaning lies in experience, and experience lies in contrast. Abandoning one's search is not the same as losing the capacity to discover.\n"
                        voice "audio/voices/felina/fight/witch7a.flac"
                        show shifting pose talk onlayer front
                        mound "I am contrast itself. To reject me is to reject the shape of everything. Do not use words to reduce that which your eyes know to be irreducible.\n"

                    "{i}• ''I have already come so far. What more is there left for me to see?''{/i}":
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        voice "audio/voices/felina/fight/witch8.flac"
                        show shifting martyrs talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "More than either of us can possibly imagine, if you would only open yourself to the totality of existence.\n"

                    "{i}• ''With time, we could have been better.''{/i}":
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        voice "audio/voices/felina/fight/witch9.flac"
                        show shifting pity smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "And there is always time.\n"

                    "{i}• ''But I stabbed you in the back and left both of us paralyzed. What potential was there to rise above?''{/i}" if witch_end == "player_betray":
                        label felina_witch_join:
                            voice "audio/voices/felina/fight/witch10a.flac"
                            play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                            show shifting pose onlayer front
                            hide felina onlayer inyourface
                            with dissolve
                            mounds "You mire yourself in an ending that did not end. Lift your gaze beyond moments, and towards the infinite depth of reality.\n"

                    "{i}• ''But you betrayed me. What potential was left for either of us to rise above?''{/i}" if witch_end == "player_betray":
                        jump felina_witch_join

                    "{i}• (Return){/i}":
                        jump felina_witch_menu

            "{i}• [[Appeal to your shared humanity.] ''You speak about life and death and change and stagnation, but that isn't what any of this has been about.''{/i}" if felina_appeal_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''This has always just been about us. Two people forced to hurt each other again and again and again. But we don't have to hurt each other anymore.''{/i}" if felina_appeal_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''There can be love and conflict and beauty and ugliness between us without bringing the whole of reality into the picture.''{/i}" if felina_appeal_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''We're not the whole of reality. Why won't you see me the way I still see you? Why won't you see me for what I am?''{/i}" if felina_appeal_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''This doesn't have to be so big. You can come back down to my level. You can come back to me.''{/i}" if felina_appeal_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Reject her authority.] ''You've done nothing but lecture me since the minute I got here.''{/i}" if felina_lecture_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''You use all these pretentious metaphors and pretend you're making grand proclamations about who I am and who you are. But really you aren't saying much of anything.''{/i}" if felina_lecture_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''It doesn't even matter what I say to you, because you're just going to keep telling me your perspective like it's some universal truth.''{/i}" if felina_lecture_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''It was so much better when I was with your vessels. Even at their worst, they all still heard me.''{/i}" if felina_lecture_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''I don't know what you are, but you aren't any of them. You're just something wearing their skin.''{/i}" if felina_lecture_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Argue your independence.] ''You act as though the world can't exist without you. But I've existed without you.''{/i}" if felina_assert_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''What are the woods, then? What is the cabin? What is the time we've spent apart if not me existing as myself?''{/i}" if felina_assert_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''I wouldn't be here if destroying you would leave all of reality a colorless blur.''{/i}" if felina_assert_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''I'd rather trust an ignorant soul who died trying to make things better than a god who'd let the wheel of suffering turn forever.''{/i}" if felina_assert_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''If I need to destroy you to build a better world, then I will.''{/i}" if felina_assert_count == 4:
                $ felina_assert_lethal = True
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''Who said anything about destroying you? I just need to make you stop.''{/i}" if felina_assert_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Reject her perspective.] ''I won't engage with violence.''{/i}" if felina_rejection_count == 0:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''It doesn't matter how I feel. Death, suffering, and oblivion shouldn't fall on others. If we are able to transcend death, then we are responsible for those it holds captive.''{/i}" if felina_rejection_count == 1:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''Suffering born in delusion is still suffering. It doesn't matter what we are now. We hurt each other, and we shouldn't have done that. We cannot let a world be spun out of that pain.''{/i}" if felina_rejection_count == 2:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''You reject the suffering of material reality, and yet you cling to its framework for meaning. We can be better than this.''{/i}" if felina_rejection_count == 3:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''You claim your destruction would steal meaning from existence, but if my actions can make existence worse, then there must be actions that make it better. Perfection implies finality, and nothing is final.''{/i}" if felina_rejection_count == 4:
                jump felina_rejection_join

            "{i}• ''I get it. There's no need for us to keep fighting. I'll leave with you. I just don't know how.'' [[Stop the fight early and surrender.]{/i}" if felina_round >= 2:
                $ achievement.grant("ACH_END_FREE2")
                jump felina_freedom_join

            "{i}• [[Remain silent.]{/i}":
                jump felina_silence

    jump felina_fight_staging

label felina_thorn_start:

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
        show pop thorn onlayer inyourface at shakeshort, Position(ypos=1125)
    else:
        $ previous_transform = "danceflip"
        show shifting dance onlayer front at flip, shakeshort, Position(ypos=1125)
        show pop thorn onlayer inyourface at flip, shakeshort, Position(ypos=1125)
    with Dissolve(0.25)
    $ renpy.pause(1.45)
    $ gallery_thorn.unlock_item(19)
    $ renpy.save_persistent()
    play audio "audio/final/Witch_TreeWrap_1.flac"
    show fight thorn onlayer inyourface at Position(ypos=1125)
    $ renpy.pause(0.01)
    voice "audio/voices/felina/fight/thorn1.flac"
    mound "A thought is a vine, and some thoughts nurture thorns that bleed the soul. An endless growth that blots your vision and strangles your trust.\n"

    if thorn_end == "free" or thorn_end == "free_kiss":
        voice "audio/voices/felina/fight/thorn2.flac"
        hide fight onlayer inyourface
        hide shifting onlayer front
        hide pop onlayer inyourface
        show farback quiet onlayer farback at Position(ypos=1125)
        show back awakening onlayer back at Position(ypos=1125)
        show midground awakening onlayer front at Position(ypos=1125)
        show hair awakened onlayer front at Position(ypos=1125)
        show dress felina onlayer front at Position(ypos=1125)
        show shifting martyrs talk onlayer front at Position(ypos=1125)
        show felina thorn3 onlayer inyourface at Position(ypos=1125)
        with Dissolve(1.0)
        mound "When I succumbed to myself, you patiently stood by me and cut the thistles that rooted in my skin.\n"
        voice "audio/voices/felina/fight/thorn3.flac"
        show shifting pity smile talk onlayer front
        show felina thorn2 talk onlayer inyourface
        with dissolve
        mound "Your compassion is what freed us both, but compassion is a thing that must
        be nurtured, and you cannot nurture that which cannot change.\n"
        show shifting pity smile onlayer front
        show felina thorn1 onlayer inyourface
        with dissolve

    if thorn_end == "stuck" or thorn_end == "stuck_together" or thorn_end == "slay_attempt" or thorn_end == "free_attempt" or thorn_end == "abandoned":
        if thorn_end == "stuck" or thorn_end == "stuck_together":
            voice "audio/voices/felina/fight/thorn4a.flac"
            hide fight onlayer inyourface
            hide shifting onlayer front
            hide pop onlayer inyourface
            show farback quiet onlayer farback at Position(ypos=1125)
            show back awakening onlayer back at Position(ypos=1125)
            show midground awakening onlayer front at Position(ypos=1125)
            show hair awakened onlayer front at Position(ypos=1125)
            show dress felina onlayer front at Position(ypos=1125)
            show shifting martyrs talk onlayer front at Position(ypos=1125)
            show felina thorn3 onlayer inyourface at Position(ypos=1125)
            with Dissolve(1.0)
            mound "When I succumbed to myself, you left me to rot, and in your abandonment, the two of us were bound in our suffering together.\n"
        elif thorn_end == "abandoned":
            voice "audio/voices/felina/fight/thorn4c.flac"
            hide fight onlayer inyourface
            hide shifting onlayer front
            hide pop onlayer inyourface
            show farback quiet onlayer farback at Position(ypos=1125)
            show back awakening onlayer back at Position(ypos=1125)
            show midground awakening onlayer front at Position(ypos=1125)
            show hair awakened onlayer front at Position(ypos=1125)
            show dress felina onlayer front at Position(ypos=1125)
            show shifting martyrs talk onlayer front at Position(ypos=1125)
            show felina thorn3 onlayer inyourface at Position(ypos=1125)
            with Dissolve(1.0)
            mound "When I succumbed to myself, you left me to rot.\n"
        else:
            voice "audio/voices/felina/fight/thorn5.flac"
            hide fight onlayer inyourface
            hide shifting onlayer front
            hide pop onlayer inyourface
            show farback quiet onlayer farback at Position(ypos=1125)
            show back awakening onlayer back at Position(ypos=1125)
            show midground awakening onlayer front at Position(ypos=1125)
            show hair awakened onlayer front at Position(ypos=1125)
            show dress felina onlayer front at Position(ypos=1125)
            show shifting smile talk onlayer front at Position(ypos=1125)
            show felina thorn3 onlayer inyourface at Position(ypos=1125)
            with Dissolve(1.0)
            mound "When I succumbed to myself, you pretended to stand patiently by me, pretended you would cut the thistles rooted in my skin.\n"
            voice "audio/voices/felina/fight/thorn6.flac"
            show felina thorn2 talk onlayer inyourface
            show shifting martyrs talk onlayer front
            with dissolve
            mound "But then you took my trust and used it to strike at my heart. The two of us were bound in our suffering together.\n"
        voice "audio/voices/felina/fight/thorn7.flac"
        hide fight onlayer inyourface
        show shifting closed smile talk onlayer front
        show felina thorn1 onlayer inyourface
        with dissolve
        mound "A painful eternity, but one that is only unceasing if you remove what happens next.\n"

    label felina_thorn_menu:
        menu:
            extend ""

            "{i}• (Explore) [[Address this vessel's statement directly.]{/i}":
                menu:
                    extend ""

                    "{i}• ''With time we could have been better.''{/i}" if thorn_end == "stuck" or thorn_end == "stuck_together" or thorn_end == "slay_attempt":
                        voice "audio/voices/felina/fight/thorn8.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting pity smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "And there is always time.\n"

                    "{i}• ''I would have liked to see that.''{/i}" if thorn_end == "stuck" or thorn_end == "stuck_together" or thorn_end == "slay_attempt" or thorn_end == "abandoned":
                        $ felina_fight_effective_resistance -= 1
                        voice "audio/voices/felina/fight/thorn9.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting pity smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "And you see it now. I am before you, and you are before me, and we can choose our freedom.\n"

                    "{i}• ''But you were stuck. That was it.''{/i}" if thorn_end == "abandoned":
                        $ felina_fight_effective_resistance += 1
                        voice "audio/voices/felina/fight/thorn10.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting pose onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "You mire yourself in an ending that did not end. Lift your gaze beyond moments, and towards the infinite depth of reality.\n"

                    "{i}• ''But we were stuck. That was it.''{/i}" if thorn_end == "stuck" or thorn_end == "stuck_together" or thorn_end == "slay_attempt":
                        $ felina_fight_effective_resistance += 1
                        voice "audio/voices/felina/fight/thorn10.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting pose onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "You mire yourself in an ending that did not end. Lift your gaze beyond moments, and towards the infinite depth of reality.\n"

                    "{i}• ''If I had known what you really were, I wouldn't have been so quick to free you.''{/i}" if thorn_end == "free" or thorn_end == "free_kiss":
                        voice "audio/voices/felina/fight/thorn11.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "And yet you did, first by giving me your life, and then by refusing to take mine. You don't need to turn back to the way things were before.\n"

                    "{i}• ''Of course I helped you. I didn't want us to hate each other.''{/i}" if thorn_end == "free" or thorn_end == "free_kiss":
                        $ felina_fight_effective_resistance -= 1
                        voice "audio/voices/felina/fight/thorn12.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "Then help me again. We are each other's liberation.\n"

                    "{i}• (Return){/i}":
                        jump felina_thorn_menu

            "{i}• [[Appeal to your shared humanity.] ''You speak about life and death and change and stagnation, but that isn't what any of this has been about.''{/i}" if felina_appeal_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''This has always just been about us. Two people forced to hurt each other again and again and again. But we don't have to hurt each other anymore.''{/i}" if felina_appeal_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''There can be love and conflict and beauty and ugliness between us without bringing the whole of reality into the picture.''{/i}" if felina_appeal_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''We're not the whole of reality. Why won't you see me the way I still see you? Why won't you see me for what I am?''{/i}" if felina_appeal_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''This doesn't have to be so big. You can come back down to my level. You can come back to me.''{/i}" if felina_appeal_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Reject her authority.] ''You've done nothing but lecture me since the minute I got here.''{/i}" if felina_lecture_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''You use all these pretentious metaphors and pretend you're making grand proclamations about who I am and who you are. But really you aren't saying much of anything.''{/i}" if felina_lecture_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''It doesn't even matter what I say to you, because you're just going to keep telling me your perspective like it's some universal truth.''{/i}" if felina_lecture_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''It was so much better when I was with your vessels. Even at their worst, they all still heard me.''{/i}" if felina_lecture_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''I don't know what you are, but you aren't any of them. You're just something wearing their skin.''{/i}" if felina_lecture_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Argue your independence.] ''You act as though the world can't exist without you. But I've existed without you.''{/i}" if felina_assert_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''What are the woods, then? What is the cabin? What is the time we've spent apart if not me existing as myself?''{/i}" if felina_assert_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''I wouldn't be here if destroying you would leave all of reality a colorless blur.''{/i}" if felina_assert_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''I'd rather trust an ignorant soul who died trying to make things better than a god who'd let the wheel of suffering turn forever.''{/i}" if felina_assert_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''If I need to destroy you to build a better world, then I will.''{/i}" if felina_assert_count == 4:
                $ felina_assert_lethal = True
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''Who said anything about destroying you? I just need to make you stop.''{/i}" if felina_assert_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Reject her perspective.] ''I won't engage with violence.''{/i}" if felina_rejection_count == 0:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''It doesn't matter how I feel. Death, suffering, and oblivion shouldn't fall on others. If we are able to transcend death, then we are responsible for those it holds captive.''{/i}" if felina_rejection_count == 1:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''Suffering born in delusion is still suffering. It doesn't matter what we are now. We hurt each other, and we shouldn't have done that. We cannot let a world be spun out of that pain.''{/i}" if felina_rejection_count == 2:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''You reject the suffering of material reality, and yet you cling to its framework for meaning. We can be better than this.''{/i}" if felina_rejection_count == 3:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''You claim your destruction would steal meaning from existence, but if my actions can make existence worse, then there must be actions that make it better. Perfection implies finality, and nothing is final.''{/i}" if felina_rejection_count == 4:
                jump felina_rejection_join

            "{i}• ''I get it. There's no need for us to keep fighting. I'll leave with you. I just don't know how.'' [[Stop the fight early and surrender.]{/i}" if felina_round >= 2:
                $ achievement.grant("ACH_END_FREE2")
                jump felina_freedom_join

            "{i}• [[Remain silent.]{/i}":
                jump felina_silence

    jump felina_fight_staging

label felina_fury_start:
    if fury_end == "fusion":
        play secondary "audio/_pristine/sfx/shifty_hands.flac"
    else:
        play secondary "audio/_pristine/sfx/shifty_crawl.flac"
    play audio "audio/_pristine/sfx/shifty_move.flac"
    hide hair onlayer front
    hide dress onlayer front
    hide shifting onlayer front
    show farback quiet onlayer farback at shakeshort
    show back awakening onlayer back at shakeshort
    show midground awakening onlayer front at shakeshort
    if fury_end == "heart":
        if previous_transform != "hands":
            $ previous_transform = "hands"
            show shifting hands onlayer front at shakeshort, Position(ypos=1125)
            show pop furyheart onlayer inyourface at shakeshort, Position(ypos=1125)
        else:
            $ previous_transform = "handsflip"
            show shifting hands onlayer front at flip, shakeshort, Position(ypos=1125)
            show pop furyheart onlayer inyourface at flip, shakeshort, Position(ypos=1125)
    else:
        if previous_transform != "fierce":
            $ previous_transform = "fierce"
            show shifting fierce onlayer front at shakeshort, Position(ypos=1125)
            show pop fury onlayer inyourface at shakeshort, Position(ypos=1125)
        else:
            $ previous_transform = "fierceflip"
            show shifting fierce onlayer front at flip, shakeshort, Position(ypos=1125)
            show pop fury flip onlayer inyourface at shakeshort, Position(ypos=1125)
    with Dissolve(0.25)
    if fury_end == "heart":
        $ renpy.pause(1.9)
    else:
        $ renpy.pause(1.3)
    $ gallery_fury.unlock_item(20)
    $ renpy.save_persistent()
    play audio "audio/final/Spectre_HeartCrush_2 copy.flac"
    show fight fury onlayer inyourface at Position(ypos=1125)
    $ renpy.pause(0.01)
    voice "audio/voices/felina/fight/fury1.flac"
    mounds "What is a person? Is it their body? Is it all of their body? Pluck the eyes, peel the skin, strip the tendons, mince the meat, grind the bones. When it is all gone, do you still have who you started with?\n"
    voice "audio/voices/felina/fight/fury2.flac"
    hide fight onlayer inyourface
    hide shifting onlayer front
    hide pop onlayer inyourface
    show farback quiet onlayer farback at Position(ypos=1125)
    show back awakening onlayer back at Position(ypos=1125)
    show midground awakening onlayer front at Position(ypos=1125)
    show hair awakened onlayer front at Position(ypos=1125)
    show dress felina onlayer front at Position(ypos=1125)
    show shifting serious talk onlayer front at Position(ypos=1125)
    if fury_end == "heart":
        show felina furyheart 2 onlayer inyourface at Position(ypos=1125)
    else:
        show felina fury2 talk onlayer inyourface at Position(ypos=1125)
    with Dissolve(1.0)
    mound "A person is not a body. Death is a transformation into something new. It is only bodies that fear it.\n"
    if fury_end == "heart":
        show felina furyheart 3 onlayer inyourface
    else:
        show felina fury3 onlayer inyourface
    show shifting serious onlayer front
    with dissolve
    label felina_fury_menu:
        menu:
            extend ""

            "{i}{outlinecolor=4f1313}• ''Even when you reduced me to nothing, you could not rid yourself of me. But I was able to rid myself of you.''{/outlinecolor}{/i}" if fury_end == "slay" or fury_end == "slay_unarmed" or fury_end == "slay_tower":
                jump felina_violence_join

            "{i}{outlinecolor=4f1313}• ''Even when you reduced me to nothing, you could not rid yourself of me. But I was able to rid myself of you. I didn't even need to kill you to break your spirit.''{/outlinecolor}{/i}" if fury_end == "leave":
                jump felina_violence_join

            "{i}• (Explore) [[Address this vessel's statement directly.]{/i}":
                menu:
                    extend ""

                    "{i}• ''I am not my body, but I feel my body suffer.''{/i}":
                        $ felina_fight_effective_resistance += 1
                        voice "audio/voices/felina/fight/fury3.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting pose onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "Do you suffer now? Let go of what you think yourself to be, and exist.\n"

                    "{i}• ''I am not my body, but perhaps others are theirs.''{/i}":
                        voice "audio/voices/felina/fight/fury4.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting closed smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "And yet bodies change and consciousness goes on. The infant's body is not the child's is not the adult's, but the thread of existence remains strung through it all.\n"

                    "{i}• ''I don't fear death. Not anymore.''{/i}":
                        voice "audio/voices/felina/fight/fury5.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting pity smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "If you do not fear it, then there is no need for you to struggle against it. Let go. Leave with me.\n"
                        show shifting pity smile onlayer front
                        menu:
                            extend ""

                            "{i}• ''I'm ready. I want to leave with you.'' [[Stop the fight early and surrender.]{/i}" if felina_round >= 2:
                                $ achievement.grant("ACH_END_FREE2")
                                jump felina_freedom_join

                            "{i}• ''I won't leave with you. Not until you see things from my perspective.''{/i}" if felina_round >= 2:
                                voice "audio/voices/felina/fight/dams8.flac"
                                show shifting smile talk onlayer front
                                mound "If you need more time to open your eyes, then I will give you all the time in the world.\n"

                    "{i}• ''But what am I, if I'm not a body?''{/i}":
                        voice "audio/voices/felina/fight/fury6.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting pity smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "You are you.\n"

                    "{i}• (Return){/i}":
                        jump felina_fury_menu

            "{i}• [[Appeal to your shared humanity.] ''You speak about life and death and change and stagnation, but that isn't what any of this has been about.''{/i}" if felina_appeal_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''This has always just been about us. Two people forced to hurt each other again and again and again. But we don't have to hurt each other anymore.''{/i}" if felina_appeal_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''There can be love and conflict and beauty and ugliness between us without bringing the whole of reality into the picture.''{/i}" if felina_appeal_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''We're not the whole of reality. Why won't you see me the way I still see you? Why won't you see me for what I am?''{/i}" if felina_appeal_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''This doesn't have to be so big. You can come back down to my level. You can come back to me.''{/i}" if felina_appeal_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Reject her authority.] ''You've done nothing but lecture me since the minute I got here.''{/i}" if felina_lecture_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''You use all these pretentious metaphors and pretend you're making grand proclamations about who I am and who you are. But really you aren't saying much of anything.''{/i}" if felina_lecture_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''It doesn't even matter what I say to you, because you're just going to keep telling me your perspective like it's some universal truth.''{/i}" if felina_lecture_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''It was so much better when I was with your vessels. Even at their worst, they all still heard me.''{/i}" if felina_lecture_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''I don't know what you are, but you aren't any of them. You're just something wearing their skin.''{/i}" if felina_lecture_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Argue your independence.] ''You act as though the world can't exist without you. But I've existed without you.''{/i}" if felina_assert_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''What are the woods, then? What is the cabin? What is the time we've spent apart if not me existing as myself?''{/i}" if felina_assert_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''I wouldn't be here if destroying you would leave all of reality a colorless blur.''{/i}" if felina_assert_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''I'd rather trust an ignorant soul who died trying to make things better than a god who'd let the wheel of suffering turn forever.''{/i}" if felina_assert_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''If I need to destroy you to build a better world, then I will.''{/i}" if felina_assert_count == 4:
                $ felina_assert_lethal = True
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''Who said anything about destroying you? I just need to make you stop.''{/i}" if felina_assert_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Reject her perspective.] ''I won't engage with violence.''{/i}" if felina_rejection_count == 0:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''It doesn't matter how I feel. Death, suffering, and oblivion shouldn't fall on others. If we are able to transcend death, then we are responsible for those it holds captive.''{/i}" if felina_rejection_count == 1:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''Suffering born in delusion is still suffering. It doesn't matter what we are now. We hurt each other, and we shouldn't have done that. We cannot let a world be spun out of that pain.''{/i}" if felina_rejection_count == 2:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''You reject the suffering of material reality, and yet you cling to its framework for meaning. We can be better than this.''{/i}" if felina_rejection_count == 3:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''You claim your destruction would steal meaning from existence, but if my actions can make existence worse, then there must be actions that make it better. Perfection implies finality, and nothing is final.''{/i}" if felina_rejection_count == 4:
                jump felina_rejection_join

            "{i}• ''I get it. There's no need for us to keep fighting. I'll leave with you. I just don't know how.'' [[Stop the fight early and surrender.]{/i}" if felina_round >= 2:
                $ achievement.grant("ACH_END_FREE2")
                jump felina_freedom_join

            "{i}• [[Remain silent.]{/i}":
                jump felina_silence

    jump felina_fight_staging

label felina_grey_start:

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
        show pop grey onlayer inyourface at shakeshort, Position(ypos=1125)
    else:
        $ previous_transform = "horrorflip"
        show shifting horror onlayer front at flip, shakeshort, Position(ypos=1125)
        show pop grey onlayer inyourface at flip, shakeshort, Position(ypos=1125)
    with Dissolve(0.25)
    $ renpy.pause(4.2)
    if grey_end == "burn":
        $ gallery_grey.unlock_item(19)
        $ renpy.save_persistent()
        play tertiary "audio/final/Fire_Small_Oneshot_1.flac"
        show fight grey fire onlayer inyourface at Position(ypos=1125)
        $ renpy.pause(0.01)
    else:
        $ gallery_grey.unlock_item(20)
        $ renpy.save_persistent()
        play audio "audio/final/Water_UnderwaterRushIN_1.flac"
        show fight grey water onlayer inyourface at Position(ypos=1125)
        $ renpy.pause(0.01)

    voice "audio/voices/felina/fight/grey1.flac"
    mounds "I kill you. You kill me. Back and forth we go, faster and faster and faster. I kill you. You kill me.\n"
    if grey_end == "burn":
        stop tertiary fadeout 1.0
        voice "audio/voices/felina/fight/grey2.flac"
        hide fight onlayer inyourface
        hide shifting onlayer front
        hide pop onlayer inyourface
        show farback quiet onlayer farback at Position(ypos=1125)
        show back awakening onlayer back at Position(ypos=1125)
        show midground awakening onlayer front at Position(ypos=1125)
        show hair awakened onlayer front at Position(ypos=1125)
        show dress felina onlayer front at Position(ypos=1125)
        show shifting martyrs talk onlayer front at Position(ypos=1125)
        show felina grey3 onlayer inyourface at Position(ypos=1125)
        with Dissolve(1.0)
        mounds "Hollow eyes watch from the dry corners of a memory. A home built on all the futures that were supposed to be, preserved until the moment of reunion. The fire of the heart sets it all ablaze.\n"
    if grey_end == "drown":
        voice "audio/voices/felina/fight/grey3.flac"
        hide fight onlayer inyourface
        hide shifting onlayer front
        hide pop onlayer inyourface
        show farback quiet onlayer farback at Position(ypos=1125)
        show back awakening onlayer back at Position(ypos=1125)
        show midground awakening onlayer front at Position(ypos=1125)
        show hair awakened onlayer front at Position(ypos=1125)
        show dress felina onlayer front at Position(ypos=1125)
        show shifting martyrs talk onlayer front at Position(ypos=1125)
        show felina grey3 onlayer inyourface at Position(ypos=1125)
        with Dissolve(1.0)
        mounds "Hollow eyes watch from the dark corners of a forgotten place flooded by emotions left unspoken. The tide rises.\n"
    voice "audio/voices/felina/fight/grey4.flac"
    show shifting pity smile talk onlayer front
    show felina grey1 onlayer inyourface
    with dissolve
    mounds "I kill you and me.\n"
    voice "audio/voices/felina/fight/grey5.flac"
    show shifting martyrs talk onlayer front
    show felina grey2 talk onlayer inyourface
    with dissolve
    mound "An ending is a passion that can only be expressed with a moment in time. It is a seed for a new beginning. To linger on an ending is to rob it of its life.\n"
    voice "audio/voices/felina/fight/grey6.flac"
    show shifting pity smile talk onlayer front
    show felina grey3 onlayer inyourface
    with dissolve
    mound "And without me, all that's left to do is linger.\n"
    show shifting pity smile onlayer front
    label felina_grey_menu:
        menu:
            extend ""

            "{i}{outlinecolor=4f1313}• ''I killed you while you tried to strangle me. And when you flooded me with tears I did not drown.''{/outlinecolor}{/i}" if grey_end == "drown":
                jump felina_violence_join

            "{i}{outlinecolor=4f1313}• ''I killed you without a second thought. And when you returned to set us both ablaze, I remained while you burned away.''{/outlinecolor}{/i}" if grey_end == "burn":
                jump felina_violence_join

            "{i}• (Explore) [[Address this vessel's statement directly.]{/i}":
                menu:
                    extend ""

                    "{i}• ''I'm okay lingering.''{/i}":
                        $ felina_fight_effective_resistance += 1
                        voice "audio/voices/felina/fight/grey7.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting martyrs talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "To linger too long is to become worse than when you started. Would you rob yourself of all context to remain trapped in a single moment?\n"

                    "{i}• ''I don't want to linger.''{/i}":
                        $ felina_fight_effective_resistance -= 1
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        voice "audio/voices/felina/fight/grey8.flac"
                        show shifting smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "Then don't.\n"

                    "{i}• ''I deserved what you did to me.''{/i}":
                        $ felina_fight_effective_resistance -= 1
                        voice "audio/voices/felina/fight/grey9.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting closed smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "There is no deserve, no punishment, no retribution. There is only action and reaction.\n"

                    "{i}• (Return){/i}":
                        jump felina_grey_menu

            "{i}• [[Appeal to your shared humanity.] ''You speak about life and death and change and stagnation, but that isn't what any of this has been about.''{/i}" if felina_appeal_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''This has always just been about us. Two people forced to hurt each other again and again and again. But we don't have to hurt each other anymore.''{/i}" if felina_appeal_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''There can be love and conflict and beauty and ugliness between us without bringing the whole of reality into the picture.''{/i}" if felina_appeal_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''We're not the whole of reality. Why won't you see me the way I still see you? Why won't you see me for what I am?''{/i}" if felina_appeal_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''This doesn't have to be so big. You can come back down to my level. You can come back to me.''{/i}" if felina_appeal_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Reject her authority.] ''You've done nothing but lecture me since the minute I got here.''{/i}" if felina_lecture_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''You use all these pretentious metaphors and pretend you're making grand proclamations about who I am and who you are. But really you aren't saying much of anything.''{/i}" if felina_lecture_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''It doesn't even matter what I say to you, because you're just going to keep telling me your perspective like it's some universal truth.''{/i}" if felina_lecture_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''It was so much better when I was with your vessels. Even at their worst, they all still heard me.''{/i}" if felina_lecture_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''I don't know what you are, but you aren't any of them. You're just something wearing their skin.''{/i}" if felina_lecture_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Argue your independence.] ''You act as though the world can't exist without you. But I've existed without you.''{/i}" if felina_assert_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''What are the woods, then? What is the cabin? What is the time we've spent apart if not me existing as myself?''{/i}" if felina_assert_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''I wouldn't be here if destroying you would leave all of reality a colorless blur.''{/i}" if felina_assert_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''I'd rather trust an ignorant soul who died trying to make things better than a god who'd let the wheel of suffering turn forever.''{/i}" if felina_assert_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''If I need to destroy you to build a better world, then I will.''{/i}" if felina_assert_count == 4:
                $ felina_assert_lethal = True
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''Who said anything about destroying you? I just need to make you stop.''{/i}" if felina_assert_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Reject her perspective.] ''I won't engage with violence.''{/i}" if felina_rejection_count == 0:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''It doesn't matter how I feel. Death, suffering, and oblivion shouldn't fall on others. If we are able to transcend death, then we are responsible for those it holds captive.''{/i}" if felina_rejection_count == 1:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''Suffering born in delusion is still suffering. It doesn't matter what we are now. We hurt each other, and we shouldn't have done that. We cannot let a world be spun out of that pain.''{/i}" if felina_rejection_count == 2:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''You reject the suffering of material reality, and yet you cling to its framework for meaning. We can be better than this.''{/i}" if felina_rejection_count == 3:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''You claim your destruction would steal meaning from existence, but if my actions can make existence worse, then there must be actions that make it better. Perfection implies finality, and nothing is final.''{/i}" if felina_rejection_count == 4:
                jump felina_rejection_join

            "{i}• ''I get it. There's no need for us to keep fighting. I'll leave with you. I just don't know how.'' [[Stop the fight early and surrender.]{/i}" if felina_round >= 2:
                $ achievement.grant("ACH_END_FREE2")
                jump felina_freedom_join

            "{i}• [[Remain silent.]{/i}":
                jump felina_silence

    jump felina_fight_staging

label felina_wild_start:

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

    if wild_end == "joined":
        $ gallery_wild.unlock_item(11)
        $ renpy.save_persistent()
        play audio "audio/final/Witch_VinesTwist_2.flac"
        show fight wild nerves onlayer inyourface at Position(ypos=1125)
        $ renpy.pause(0.01)
    else:
        $ gallery_wild.unlock_item(12)
        $ renpy.save_persistent()
        play audio "audio/final/Assorted_TapestyUnraveledBreakingRip_1.flac"
        show fight wild wound onlayer inyourface at Position(ypos=1125)
        $ renpy.pause(0.01)

    voice "audio/voices/felina/fight/wild1.flac"
    mound "A web of nerves lain upon a web of nerves lain upon a web of nerves. The shade of a beautiful beginning we can never return to.\n"
    if wild_end == "joined":
        voice "audio/voices/felina/fight/wild2.flac"
        hide fight onlayer inyourface
        hide shifting onlayer front
        hide pop onlayer inyourface
        show farback quiet onlayer farback at Position(ypos=1125)
        show back awakening onlayer back at Position(ypos=1125)
        show midground awakening onlayer front at Position(ypos=1125)
        show hair awakened onlayer front at Position(ypos=1125)
        show dress felina onlayer front at Position(ypos=1125)
        show shifting pity smile talk onlayer front at Position(ypos=1125)
        show felina wild2 talk onlayer inyourface at Position(ypos=1125)
        with Dissolve(1.0)
        mound "Where did you end and I begin? When you felt what it was to be me, we held on to each other and pierced the veil of truth. Will you abandon that curiosity now that we are no longer joined in physicality?\n"
        show shifting pity smile onlayer front
    else:
        voice "audio/voices/felina/fight/wild3.flac"
        hide fight onlayer inyourface
        hide shifting onlayer front
        hide pop onlayer inyourface
        show farback quiet onlayer farback at Position(ypos=1125)
        show back awakening onlayer back at Position(ypos=1125)
        show midground awakening onlayer front at Position(ypos=1125)
        show hair awakened onlayer front at Position(ypos=1125)
        show dress felina onlayer front at Position(ypos=1125)
        show shifting pity smile talk onlayer front at Position(ypos=1125)
        show felina wild2 talk onlayer inyourface at Position(ypos=1125)
        with Dissolve(1.0)
        mound "You knew me and I knew you, even more than either of us know each other now. And you chose to pull apart that weave.\n"
        show shifting pity smile onlayer front
    if wild_end == "separate":
        voice "audio/voices/felina/fight/wild4.flac"
        show shifting smile talk onlayer front
        show felina wild3 onlayer inyourface
        with dissolve
        mound "But you did not choose to end me. We were still one, but we were also separate, and we were free. We were as we are. Will you excise that part of yourself now that you see me from yet another angle?\n"
        show shifting smile onlayer front
    if wild_end == "slay":
        voice "audio/voices/felina/fight/wild5.flac"
        show shifting serious talk onlayer front
        show felina wild3 onlayer inyourface
        with dissolve
        mound "And when the tapestry was undone you struck at my heart. You saw me as a part of you to be excised, but in that desire for excision, you made yourself whole. Will you still be whole if you destroy me?\n"
        show shifting serious onlayer front

    label felina_wild_menu:
        menu:
            extend ""

            "{i}{outlinecolor=4f1313}• ''Of course I will be, because I destroyed you then.''{/outlinecolor}{/i}" if wild_end == "slay":
                jump felina_violence_join

            "{i}• (Explore) [[Address this vessel's statement directly.]{/i}":
                menu:
                    extend ""

                    "{i}• ''Curiosity comes second to doing the right thing.''{/i}" if wild_end == "joined":
                        $ felina_fight_effective_resistance += 1
                        jump felina_wild_separate_join

                    "{i}• ''I still want to know what's out there.''{/i}" if wild_end == "joined":
                        $ felina_fight_effective_resistance -= 1
                        voice "audio/voices/felina/fight/wild6.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting pity smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "Then leave with me, and we will see it all together.\n"
                        menu:
                            extend ""

                            "{i}• ''I'm ready. I want to leave with you.'' [[Stop the fight early and surrender.]{/i}" if felina_round >= 2:
                                $ achievement.grant("ACH_END_FREE2")
                                jump felina_freedom_join

                            "{i}• ''I won't leave with you. Not until you see things from my perspective.''{/i}" if felina_round >= 2:
                                voice "audio/voices/felina/fight/dams8.flac"
                                show shifting smile talk onlayer front
                                mound "If you need more time to open your eyes, then I will give you all the time in the world.\n"

                    "{i}• ''You were a part of me. I couldn't bring myself to hurt you.''{/i}" if wild_end == "separate":
                        $ felina_fight_effective_resistance -= 1
                        label felina_wild_separate_join:
                            voice "audio/voices/felina/fight/wild7.flac"
                            play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                            show shifting closed smile talk onlayer front
                            hide felina onlayer inyourface
                            with dissolve
                            mound "All things are connected through me and through you. To harm me is to harm yourself is to harm everything. The truth of that moment remains our truth.\n"

                    "{i}• ''I couldn't bring myself to hurt you then, but maybe I should have.''{/i}" if wild_end == "separate":
                        jump felina_wild_separate_join

                    "{i}• ''I don't care about being whole. I just care about doing the right thing.''{/i}" if wild_end == "slay":
                        $ felina_fight_effective_resistance += 1
                        label felina_wild_slay_join:
                            voice "audio/voices/felina/fight/wild8.flac"
                            play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                            show shifting pity smile talk onlayer front
                            hide felina onlayer inyourface
                            with dissolve
                            mound "Do not neglect yourself in your quest to serve others. All things are connected through me and through you. To harm yourself is to harm everything.\n"

                    "{i}• ''I miss what it was like to be together. Can we go back to it?''{/i}":
                        $ felina_fight_effective_resistance -= 1
                        voice "audio/voices/felina/fight/wild9.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting martyrs talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "Though that was us before we were us, there is no turning back. For all the Echo's delusion, he still managed to reshape reality itself, though he could not destroy what could not be destroyed.\n"
                        voice "audio/voices/felina/fight/wild10.flac"
                        show shifting pity smile talk onlayer front
                        with dissolve
                        mound "We are intertwined, but we are separate.\n"

                    "{i}• ''I don't want to destroy you. I just want to do what's right.''{/i}" if wild_end == "slay":
                        jump felina_wild_slay_join

                    "{i}• (Return){/i}":
                        jump felina_wild_menu

            "{i}• [[Appeal to your shared humanity.] ''You speak about life and death and change and stagnation, but that isn't what any of this has been about.''{/i}" if felina_appeal_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''This has always just been about us. Two people forced to hurt each other again and again and again. But we don't have to hurt each other anymore.''{/i}" if felina_appeal_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''There can be love and conflict and beauty and ugliness between us without bringing the whole of reality into the picture.''{/i}" if felina_appeal_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''We're not the whole of reality. Why won't you see me the way I still see you? Why won't you see me for what I am?''{/i}" if felina_appeal_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''This doesn't have to be so big. You can come back down to my level. You can come back to me.''{/i}" if felina_appeal_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Reject her authority.] ''You've done nothing but lecture me since the minute I got here.''{/i}" if felina_lecture_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''You use all these pretentious metaphors and pretend you're making grand proclamations about who I am and who you are. But really you aren't saying much of anything.''{/i}" if felina_lecture_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''It doesn't even matter what I say to you, because you're just going to keep telling me your perspective like it's some universal truth.''{/i}" if felina_lecture_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''It was so much better when I was with your vessels. Even at their worst, they all still heard me.''{/i}" if felina_lecture_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''I don't know what you are, but you aren't any of them. You're just something wearing their skin.''{/i}" if felina_lecture_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Argue your independence.] ''You act as though the world can't exist without you. But I've existed without you.''{/i}" if felina_assert_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''What are the woods, then? What is the cabin? What is the time we've spent apart if not me existing as myself?''{/i}" if felina_assert_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''I wouldn't be here if destroying you would leave all of reality a colorless blur.''{/i}" if felina_assert_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''I'd rather trust an ignorant soul who died trying to make things better than a god who'd let the wheel of suffering turn forever.''{/i}" if felina_assert_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''If I need to destroy you to build a better world, then I will.''{/i}" if felina_assert_count == 4:
                $ felina_assert_lethal = True
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''Who said anything about destroying you? I just need to make you stop.''{/i}" if felina_assert_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Reject her perspective.] ''I won't engage with violence.''{/i}" if felina_rejection_count == 0:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''It doesn't matter how I feel. Death, suffering, and oblivion shouldn't fall on others. If we are able to transcend death, then we are responsible for those it holds captive.''{/i}" if felina_rejection_count == 1:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''Suffering born in delusion is still suffering. It doesn't matter what we are now. We hurt each other, and we shouldn't have done that. We cannot let a world be spun out of that pain.''{/i}" if felina_rejection_count == 2:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''You reject the suffering of material reality, and yet you cling to its framework for meaning. We can be better than this.''{/i}" if felina_rejection_count == 3:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''You claim your destruction would steal meaning from existence, but if my actions can make existence worse, then there must be actions that make it better. Perfection implies finality, and nothing is final.''{/i}" if felina_rejection_count == 4:
                jump felina_rejection_join

            "{i}• ''I get it. There's no need for us to keep fighting. I'll leave with you. I just don't know how.'' [[Stop the fight early and surrender.]{/i}" if felina_round >= 2:
                $ achievement.grant("ACH_END_FREE2")
                jump felina_freedom_join

            "{i}• [[Remain silent.]{/i}":
                jump felina_silence

    jump felina_fight_staging

label felina_wraith_start:

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
    $ gallery_wraith.unlock_item(11)
    $ renpy.save_persistent()
    play audio "audio/final/Nightmare_NeckCrack_1.flac"
    show fight wraith onlayer inyourface at Position(ypos=1125)
    $ renpy.pause(0.01)
    voice "audio/voices/felina/fight/wraith1.flac"
    mounds "Flesh is a vehicle, and to destroy the flesh is to strand the spirit. With violence, you stranded me, and with violence, I sought to twist your flesh back into mine.\n"
    if wraith_end == "slay":
        voice "audio/voices/felina/fight/wraith2.flac"
        hide fight onlayer inyourface
        hide shifting onlayer front
        hide pop onlayer inyourface
        show farback quiet onlayer farback at Position(ypos=1125)
        show back awakening onlayer back at Position(ypos=1125)
        show midground awakening onlayer front at Position(ypos=1125)
        show hair awakened onlayer front at Position(ypos=1125)
        show dress felina onlayer front at Position(ypos=1125)
        show shifting closed smile talk onlayer front at Position(ypos=1125)
        show felina wraith2 talk onlayer inyourface at Position(ypos=1125)
        with Dissolve(1.0)
        mound "When forced between choosing your death, and forfeiting your body, you chose agency. But agency requires action, and action requires an endless tapestry of events. In your final moments, would you remove action itself from reality?\n"
        show felina wraith1 onlayer inyourface
        with dissolve
    if wraith_end == "free":
        voice "audio/voices/felina/fight/wraith3.flac"
        hide fight onlayer inyourface
        hide shifting onlayer front
        hide pop onlayer inyourface
        show farback quiet onlayer farback at Position(ypos=1125)
        show back awakening onlayer back at Position(ypos=1125)
        show midground awakening onlayer front at Position(ypos=1125)
        show hair awakened onlayer front at Position(ypos=1125)
        show dress felina onlayer front at Position(ypos=1125)
        show shifting martyrs talk onlayer front at Position(ypos=1125)
        show felina wraith3 onlayer inyourface at Position(ypos=1125)
        with Dissolve(1.0)
        mound "You did not resist my violence when it overcame you. Did you understand that the flesh wasn't you, or did you choose to gift yourself to someone who thought she hated you?\n"
        voice "audio/voices/felina/fight/wraith4.flac"
        show shifting pity smile talk onlayer front
        show felina wraith1 onlayer inyourface
        with dissolve
        mound "To fear me is to fear losing the flesh, but the flesh is not the spirit.\n"
        show shifting pity smile onlayer front

    label felina_wraith_menu:
        menu:
            extend ""

            "{i}{outlinecolor=4f1313}• ''The first time we met I executed you without a second thought. And at the end of my confrontation with your spirit, I hurled you down a bottomless pit.''{/outlinecolor}{/i}" if wraith_end == "slay" and wraith_source == "spectre":
                jump felina_violence_join

            "{i}{outlinecolor=4f1313}• ''Even when you cut the signal to my body, I cleanly executed you. And when I was confronted with your spirit, I hurled you down a bottomless pit.''{/outlinecolor}{/i}" if wraith_end == "slay" and wraith_source == "nightmare":
                jump felina_violence_join

            "{i}• (Explore) [[Address this vessel's statement directly.]{/i}":
                menu:
                    extend ""

                    "{i}• ''I helped you out of fear, and I'm not afraid of you anymore. That is why I resist you now.''{/i}" if wraith_end == "free":
                        $ felina_fight_effective_resistance += 1
                        voice "audio/voices/felina/fight/wraith5a.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting closed smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "And yet there is no reason to resist me beyond fear and delusion. If you aren't afraid of me, why would you resist me? Why would you force the rest of the world to resist me, too?\n"

                    "{i}• ''I fear you now more than ever.''{/i}" if wraith_end == "free":
                        $ felina_fight_effective_resistance -= 1
                        voice "audio/voices/felina/fight/wraith6.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting closed smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "You have no reason to fear me. There would be no dance if we weren't equals. And are we not dancing now?\n"

                    "{i}• ''I was glad to set you free.''{/i}" if wraith_end == "free":
                        $ felina_fight_effective_resistance -= 1
                        voice "audio/voices/felina/fight/wraith7.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "Then set me free again. Set both of us free.\n"
                        show shifting smile onlayer front
                        menu:
                            extend ""

                            "{i}• ''I'm ready. I want to leave with you.'' [[Stop the fight early and surrender.]{/i}" if felina_round >= 2:
                                $ achievement.grant("ACH_END_FREE2")
                                jump felina_freedom_join

                            "{i}• ''I won't leave with you. Not until you see things from my perspective.''{/i}" if felina_round >= 2:
                                voice "audio/voices/felina/fight/dams8.flac"
                                show shifting pity smile talk onlayer front
                                mound "If you need more time to open your eyes, then I will give you all the time in the world.\n"

                    "{i}• ''Can you say with certainty what shape a world without you will take?''{/i}" if wraith_end == "slay":
                        $ felina_fight_effective_resistance += 1
                        voice "audio/voices/felina/fight/wraith8a.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting pissed talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "I know what I am, but I do not know what I am not. If a world without me is so unknown, then how can you be so sure you want to create it?\n"

                    "{i}• ''I don't want that world to come to pass.''{/i}" if wraith_end == "slay":
                        $ felina_fight_effective_resistance += 1
                        voice "audio/voices/felina/fight/wraith9.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "Then accept the world as it is now, with both of us a part of it.\n"

                    "{i}• ''You didn't give me much choice.''{/i}" if wraith_end == "slay":
                        $ felina_fight_effective_resistance += 1
                        voice "audio/voices/felina/fight/wraith10.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "And yet still, you chose. To be capable of change is to be capable of choice.\n"

                    "{i}• (Return){/i}":
                        jump felina_wraith_menu


            "{i}• [[Appeal to your shared humanity.] ''You speak about life and death and change and stagnation, but that isn't what any of this has been about.''{/i}" if felina_appeal_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''This has always just been about us. Two people forced to hurt each other again and again and again. But we don't have to hurt each other anymore.''{/i}" if felina_appeal_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''There can be love and conflict and beauty and ugliness between us without bringing the whole of reality into the picture.''{/i}" if felina_appeal_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''We're not the whole of reality. Why won't you see me the way I still see you? Why won't you see me for what I am?''{/i}" if felina_appeal_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''This doesn't have to be so big. You can come back down to my level. You can come back to me.''{/i}" if felina_appeal_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Reject her authority.] ''You've done nothing but lecture me since the minute I got here.''{/i}" if felina_lecture_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''You use all these pretentious metaphors and pretend you're making grand proclamations about who I am and who you are. But really you aren't saying much of anything.''{/i}" if felina_lecture_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''It doesn't even matter what I say to you, because you're just going to keep telling me your perspective like it's some universal truth.''{/i}" if felina_lecture_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''It was so much better when I was with your vessels. Even at their worst, they all still heard me.''{/i}" if felina_lecture_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''I don't know what you are, but you aren't any of them. You're just something wearing their skin.''{/i}" if felina_lecture_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Argue your independence.] ''You act as though the world can't exist without you. But I've existed without you.''{/i}" if felina_assert_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''What are the woods, then? What is the cabin? What is the time we've spent apart if not me existing as myself?''{/i}" if felina_assert_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''I wouldn't be here if destroying you would leave all of reality a colorless blur.''{/i}" if felina_assert_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''I'd rather trust an ignorant soul who died trying to make things better than a god who'd let the wheel of suffering turn forever.''{/i}" if felina_assert_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''If I need to destroy you to build a better world, then I will.''{/i}" if felina_assert_count == 4:
                $ felina_assert_lethal = True
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''Who said anything about destroying you? I just need to make you stop.''{/i}" if felina_assert_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Reject her perspective.] ''I won't engage with violence.''{/i}" if felina_rejection_count == 0:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''It doesn't matter how I feel. Death, suffering, and oblivion shouldn't fall on others. If we are able to transcend death, then we are responsible for those it holds captive.''{/i}" if felina_rejection_count == 1:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''Suffering born in delusion is still suffering. It doesn't matter what we are now. We hurt each other, and we shouldn't have done that. We cannot let a world be spun out of that pain.''{/i}" if felina_rejection_count == 2:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''You reject the suffering of material reality, and yet you cling to its framework for meaning. We can be better than this.''{/i}" if felina_rejection_count == 3:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''You claim your destruction would steal meaning from existence, but if my actions can make existence worse, then there must be actions that make it better. Perfection implies finality, and nothing is final.''{/i}" if felina_rejection_count == 4:
                jump felina_rejection_join

            "{i}• ''I get it. There's no need for us to keep fighting. I'll leave with you. I just don't know how.'' [[Stop the fight early and surrender.]{/i}" if felina_round >= 2:
                $ achievement.grant("ACH_END_FREE2")
                jump felina_freedom_join

            "{i}• [[Remain silent.]{/i}":
                jump felina_silence

    jump felina_fight_staging

# PRISTINE CUT

label felina_dragon_start:

    if dragon_end == "fusion":
        play secondary "audio/_pristine/sfx/shifty_horror_sfx.flac"
    else:
        play secondary "audio/_pristine/sfx/shifty_dance.flac"
    play audio "audio/_pristine/sfx/shifty_move.flac"
    hide hair onlayer front
    hide dress onlayer front
    hide shifting onlayer front
    show farback quiet onlayer farback at shakeshort
    show back awakening onlayer back at shakeshort
    show midground awakening onlayer front at shakeshort
    if dragon_end == "fusion":
        if previous_transform != "horror":
            $ previous_transform = "horror"
            show shifting horror onlayer front at shakeshort, Position(ypos=1125)
            show pop dragon ghost onlayer inyourface at shakeshort, Position(ypos=1125)
        else:
            $ previous_transform = "horrorflip"
            show shifting horror onlayer front at flip, shakeshort, Position(ypos=1125)
            show pop dragon ghost onlayer inyourface at flip, shakeshort, Position(ypos=1125)
    else:
        if previous_transform != "dance":
            $ previous_transform = "dance"
            show shifting dance onlayer front at shakeshort, Position(ypos=1125)
            show pop dragon full onlayer inyourface at shakeshort, Position(ypos=1125)
        else:
            $ previous_transform = "danceflip"
            show shifting dance onlayer front at flip, shakeshort, Position(ypos=1125)
            show pop dragon full onlayer inyourface at flip, shakeshort, Position(ypos=1125)
    with Dissolve(0.25)
    if dragon_end == "fusion":
        $ renpy.pause(4.2)
    else:
        $ renpy.pause(1.45)
    $ gallery_dragon.unlock_item(20)
    $ renpy.save_persistent()
    play audio "audio/_pristine/sfx/Dragon Soul Transfer_1.flac"
    show cg dragon attack opp onlayer inyourface at Position(ypos=1125)
    $ renpy.pause(0.1)
    voice "audio/_pristine/voice/_climax/felina/_temp/46.flac"
    mounds "What once was one, then was two, and then was one again. You gave me shelter when you burned mine down, and then you struck another match.\n"
    voice "audio/_pristine/voice/_climax/felina/_temp/47.flac"
    hide cg onlayer inyourface
    hide fight onlayer inyourface
    hide shifting onlayer front
    hide pop onlayer inyourface
    show farback quiet onlayer farback at Position(ypos=1125)
    show back awakening onlayer back at Position(ypos=1125)
    show midground awakening onlayer front at Position(ypos=1125)
    show hair awakened onlayer front at Position(ypos=1125)
    show dress felina onlayer front at Position(ypos=1125)
    show shifting martyrs talk onlayer front at Position(ypos=1125)
    show felina dragon 1 talk onlayer inyourface at Position(ypos=1125)
    with Dissolve(1.0)
    mound "I pulled you from the ruins and then we built a life. What once was one, then was one again.\n"
    voice "audio/_pristine/voice/_climax/felina/_temp/48.flac"
    show shifting smile talk onlayer front at Position(ypos=1125)
    show felina dragon 2 talk onlayer inyourface at Position(ypos=1125)
    with dissolve
    mound "The peace didn't last. The worm in your heart came for us.\n"

    if dragon_end == "free":
        voice "audio/_pristine/voice/_climax/felina/_temp/49.flac"
        show shifting pity smile talk onlayer front at Position(ypos=1125)
        show felina dragon 3 talk onlayer inyourface at Position(ypos=1125)
        with dissolve
        mound "It took you from me, but you took me with you, and together we both left. What once was one, then was two and also one again.\n"

    if dragon_end == "fusion":
        voice "audio/_pristine/voice/_climax/felina/_temp/50.flac"
        show shifting pity smile talk onlayer front at Position(ypos=1125)
        show felina dragon 3 talk onlayer inyourface at Position(ypos=1125)
        with dissolve
        mound "It took you from me, and I took you back. What once was one, then was two, then was one again.\n"

    if dragon_end == "abandon":
        voice "audio/_pristine/voice/_climax/felina/_temp/51a.flac"
        show shifting pity smile talk onlayer front at Position(ypos=1125)
        show felina dragon 3 talk onlayer inyourface at Position(ypos=1125)
        with dissolve
        mound "It took you from me, and then you left. What once was one, then was two, but it could be one again.\n"

    voice "audio/_pristine/voice/_climax/felina/_temp/52.flac"
    show shifting smile talk onlayer front at Position(ypos=1125)
    show felina dragon 1 talk onlayer inyourface at Position(ypos=1125)
    with dissolve
    mound "You and I are bound together. To rid yourself of me would be to leave yourself forever incomplete.\n"
    show shifting smile onlayer front at Position(ypos=1125)
    show felina dragon 1 onlayer inyourface at Position(ypos=1125)

    label felina_dragon_menu:
        menu:
            extend ""

            "{i}{outlinecolor=4f1313}• ''When your spirit possessed my body, I excised you from my heart. And when you tried to take me with you, I left you to languish. There is nothing you can do to me that lasts.''{/outlinecolor}{/i}" if dragon_end == "abandon":
                jump felina_violence_join

            "{i}• (Explore) [[Address this vessel's statement directly.]{/i}":
                menu:
                    extend ""

                    "{i}• ''I wish I could leave with you now like we did then.''{/i}" if dragon_end == "free":
                        jump dragon_leave_with_me_mound

                    "{i}• ''I miss being so close to you.''{/i}":
                        label dragon_leave_with_me_mound:
                            $ felina_fight_effective_resistance -= 2
                            voice "audio/_pristine/voice/_climax/felina/_temp/57.flac"
                            play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                            show shifting smile talk onlayer front
                            hide felina onlayer inyourface
                            with dissolve
                            mound "Then leave with me.\n"
                            show shifting smile onlayer front
                            menu:
                                extend ""

                                "{i}• ''I'm ready. I want to leave with you.'' [[Stop the fight early and surrender.]{/i}" if felina_round >= 2:
                                    $ achievement.grant("ACH_END_FREE2")
                                    jump felina_freedom_join

                                "{i}• ''I won't leave with you. Not until you see things from my perspective.''{/i}" if felina_round >= 2:
                                    voice "audio/voices/felina/fight/dams8.flac"
                                    show shifting pity smile talk onlayer front
                                    mound "If you need more time to open your eyes, then I will give you all the time in the world.\n"

                    "{i}• ''Just because we're bound together doesn't mean I can't be whole without you.''{/i}":
                        $ felina_fight_effective_resistance += 1
                        voice "audio/_pristine/voice/_climax/felina/_temp/53.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting closed smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "Could you bear the risk of seeking that truth? What if you're wrong?\n"

                    "{i}• ''That was terrible. I never want to be so close to anyone ever again.''{/i}":
                        $ felina_fight_effective_resistance -= 1
                        voice "audio/_pristine/voice/_climax/felina/_temp/54.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting closed smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "It doesn't have to be so terrible. In a world with both of us, nothing has to last forever.\n"

                    "{i}• ''I never wanted to get pulled into you. I was only trying to save the world.''{/i}" :
                        $ felina_fight_effective_resistance -= 1
                        voice "audio/_pristine/voice/_climax/felina/_temp/55.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting pissed talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "But the world doesn't need saving. We've moved it along for as long as it's existed.\n"

                    "{i}• ''I never wanted to get pulled into you. I just didn't like sharing a body with you. And you rewarded me with more of what I didn't like.''{/i}":
                        $ felina_fight_effective_resistance += 1
                        voice "audio/_pristine/voice/_climax/felina/_temp/56.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting closed smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "But it's over now. Things changed. And they can change again.\n"

                    "{i}• ''I'm sorry that had to end so violently.''{/i}" if dragon_end == "fusion":
                        $ felina_fight_effective_resistance += 1
                        voice "audio/_pristine/voice/_climax/felina/_temp/58a.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting closed smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "Violence is a blinding flash of color, but no flash lasts forever.\n"

                    "{i}• (Return){/i}":
                        jump felina_dragon_menu


            "{i}• [[Appeal to your shared humanity.] ''You speak about life and death and change and stagnation, but that isn't what any of this has been about.''{/i}" if felina_appeal_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''This has always just been about us. Two people forced to hurt each other again and again and again. But we don't have to hurt each other anymore.''{/i}" if felina_appeal_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''There can be love and conflict and beauty and ugliness between us without bringing the whole of reality into the picture.''{/i}" if felina_appeal_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''We're not the whole of reality. Why won't you see me the way I still see you? Why won't you see me for what I am?''{/i}" if felina_appeal_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''This doesn't have to be so big. You can come back down to my level. You can come back to me.''{/i}" if felina_appeal_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Reject her authority.] ''You've done nothing but lecture me since the minute I got here.''{/i}" if felina_lecture_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''You use all these pretentious metaphors and pretend you're making grand proclamations about who I am and who you are. But really you aren't saying much of anything.''{/i}" if felina_lecture_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''It doesn't even matter what I say to you, because you're just going to keep telling me your perspective like it's some universal truth.''{/i}" if felina_lecture_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''It was so much better when I was with your vessels. Even at their worst, they all still heard me.''{/i}" if felina_lecture_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''I don't know what you are, but you aren't any of them. You're just something wearing their skin.''{/i}" if felina_lecture_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Argue your independence.] ''You act as though the world can't exist without you. But I've existed without you.''{/i}" if felina_assert_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''What are the woods, then? What is the cabin? What is the time we've spent apart if not me existing as myself?''{/i}" if felina_assert_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''I wouldn't be here if destroying you would leave all of reality a colorless blur.''{/i}" if felina_assert_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''I'd rather trust an ignorant soul who died trying to make things better than a god who'd let the wheel of suffering turn forever.''{/i}" if felina_assert_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''If I need to destroy you to build a better world, then I will.''{/i}" if felina_assert_count == 4:
                $ felina_assert_lethal = True
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''Who said anything about destroying you? I just need to make you stop.''{/i}" if felina_assert_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Reject her perspective.] ''I won't engage with violence.''{/i}" if felina_rejection_count == 0:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''It doesn't matter how I feel. Death, suffering, and oblivion shouldn't fall on others. If we are able to transcend death, then we are responsible for those it holds captive.''{/i}" if felina_rejection_count == 1:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''Suffering born in delusion is still suffering. It doesn't matter what we are now. We hurt each other, and we shouldn't have done that. We cannot let a world be spun out of that pain.''{/i}" if felina_rejection_count == 2:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''You reject the suffering of material reality, and yet you cling to its framework for meaning. We can be better than this.''{/i}" if felina_rejection_count == 3:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''You claim your destruction would steal meaning from existence, but if my actions can make existence worse, then there must be actions that make it better. Perfection implies finality, and nothing is final.''{/i}" if felina_rejection_count == 4:
                jump felina_rejection_join

            "{i}• ''I get it. There's no need for us to keep fighting. I'll leave with you. I just don't know how.'' [[Stop the fight early and surrender.]{/i}" if felina_round >= 2:
                $ achievement.grant("ACH_END_FREE2")
                jump felina_freedom_join

            "{i}• [[Remain silent.]{/i}":
                jump felina_silence

    jump felina_fight_staging


label felina_happy_start:
    if happy_end == "tend":
        play secondary "audio/_pristine/sfx/shifty_hands.flac"
    else:
        play secondary "audio/_pristine/sfx/shifty_dance.flac"
    play audio "audio/_pristine/sfx/shifty_move.flac"
    hide hair onlayer front
    hide dress onlayer front
    hide shifting onlayer front
    show farback quiet onlayer farback at shakeshort
    show back awakening onlayer back at shakeshort
    show midground awakening onlayer front at shakeshort
    if happy_end == "tend":
        if previous_transform != "hands":
            $ previous_transform = "hands"
            show shifting hands onlayer front at shakeshort, Position(ypos=1125)
            show pop happy hands onlayer inyourface at shakeshort, Position(ypos=1125)
        else:
            $ previous_transform = "handsflip"
            show shifting hands onlayer front at flip, shakeshort, Position(ypos=1125)
            show pop happy hands onlayer inyourface at flip, shakeshort, Position(ypos=1125)
    else:
        if previous_transform != "dance":
            $ previous_transform = "dance"
            show shifting dance onlayer front at shakeshort, Position(ypos=1125)
            show pop happy dance onlayer inyourface at shakeshort, Position(ypos=1125)
        else:
            $ previous_transform = "danceflip"
            show shifting dance onlayer front at flip, shakeshort, Position(ypos=1125)
            show pop happy dance onlayer inyourface at flip, shakeshort, Position(ypos=1125)
    with Dissolve(0.25)
    if happy_end == "tend":
        $ renpy.pause(1.9)
    else:
        $ renpy.pause(1.45)
    play audio "audio/final/Damsel_FireSHootingOut_1.flac"
    if happy_end == "dance":
        $ gallery_happy.unlock_item(20)
        $ renpy.save_persistent()
        show fight happy dance onlayer inyourface at Position(ypos=1125)
    else:
        $ gallery_happy.unlock_item(19)
        $ renpy.save_persistent()
        show fight happy onlayer inyourface at Position(ypos=1125)
    $ renpy.pause(0.01)
    voice "audio/_pristine/voice/happy/mound/1.flac"
    mound "A picture of a life in a picture of a life in a picture of a life. How deep must repetition still our movements until even the air we breathe is stale?\n"


    if happy_end == "slay":
        voice "audio/_pristine/voice/happy/mound/2.flac"
        hide fight onlayer inyourface
        hide shifting onlayer front
        hide pop onlayer inyourface
        show farback quiet onlayer farback at Position(ypos=1125)
        show back awakening onlayer back at Position(ypos=1125)
        show midground awakening onlayer front at Position(ypos=1125)
        show hair awakened onlayer front at Position(ypos=1125)
        show dress felina onlayer front at Position(ypos=1125)
        show shifting martyrs talk onlayer front at Position(ypos=1125)
        show felina happy mascara 1 talk onlayer inyourface at Position(ypos=1125)
        with Dissolve(1.0)
        mound "You doused the flames of false devotion, and in my despair, you tore down the walls and freed us both from a mockery of life.\n"

    elif happy_end == "tend":
        voice "audio/_pristine/voice/happy/mound/3.flac"
        hide fight onlayer inyourface
        hide shifting onlayer front
        hide pop onlayer inyourface
        show farback quiet onlayer farback at Position(ypos=1125)
        show back awakening onlayer back at Position(ypos=1125)
        show midground awakening onlayer front at Position(ypos=1125)
        show hair awakened onlayer front at Position(ypos=1125)
        show dress felina onlayer front at Position(ypos=1125)
        show shifting martyrs talk onlayer front at Position(ypos=1125)
        show felina happy 1 talk onlayer inyourface at Position(ypos=1125)
        with Dissolve(1.0)
        mound "As our flame threatened to blow itself out, you saved me from despair and helped me build something from nothing.\n"
        voice "audio/_pristine/voice/happy/mound/3a.flac"
        show shifting closed smile talk onlayer front at Position(ypos=1125)
        show felina happy 2 talk onlayer inyourface at Position(ypos=1125)
        with dissolve
        mound "But the flames had to diminish for us to build something new.\n"
        voice "audio/_pristine/voice/happy/mound/4.flac"
        show shifting pity smile talk onlayer front at Position(ypos=1125)
        show felina happy 3 talk onlayer inyourface at Position(ypos=1125)
        with dissolve
        mound "In a world without both of us, the flames could not go out, nor could they be lit again. Would you hold the world in place forever?\n" id felina_happy_start_e2c52d82

    elif happy_end == "dance":
        voice "audio/_pristine/voice/happy/mound/5.flac"
        hide fight onlayer inyourface
        hide shifting onlayer front
        hide pop onlayer inyourface
        show farback quiet onlayer farback at Position(ypos=1125)
        show back awakening onlayer back at Position(ypos=1125)
        show midground awakening onlayer front at Position(ypos=1125)
        show hair awakened onlayer front at Position(ypos=1125)
        show dress felina onlayer front at Position(ypos=1125)
        show shifting martyrs talk onlayer front at Position(ypos=1125)
        show felina happy mascara 2 talk onlayer inyourface at Position(ypos=1125)
        with Dissolve(1.0)
        mound "You doused the flames of false devotion, and in my despair you lifted my chin, and the two of us danced beneath the stars.\n"
        voice "audio/_pristine/voice/happy/mound/6.flac"
        show shifting pity smile talk onlayer front at Position(ypos=1125)
        show felina happy mascara 3 talk onlayer inyourface at Position(ypos=1125)
        with dissolve
        mound "But the stars can't be seen unless the flames go out and the walls come crashing down. Can you not do for all things what you did for us?\n"

    elif happy_end == "free":
        voice "audio/_pristine/voice/happy/mound/7.flac"
        hide fight onlayer inyourface
        hide shifting onlayer front
        hide pop onlayer inyourface
        show farback quiet onlayer farback at Position(ypos=1125)
        show back awakening onlayer back at Position(ypos=1125)
        show midground awakening onlayer front at Position(ypos=1125)
        show hair awakened onlayer front at Position(ypos=1125)
        show dress felina onlayer front at Position(ypos=1125)
        show shifting martyrs talk onlayer front at Position(ypos=1125)
        show felina happy mascara 2 talk onlayer inyourface at Position(ypos=1125)
        with Dissolve(1.0)
        mound "You doused the flames of false devotion, and in my despair you lifted my chin and tore down the walls that confined us.\n"

    if happy_end == "free" or happy_end == "slay":
        voice "audio/_pristine/voice/happy/mound/8.flac"
        show shifting pity smile talk onlayer front at Position(ypos=1125)
        show felina happy mascara 3 talk onlayer inyourface at Position(ypos=1125)
        with dissolve
        mound "Would you rebuild those walls and throw the world in them? Would you keep them in that box we shared and tell them that they're happy?\n"

    show shifting pity smile onlayer front at Position(ypos=1125)
    if happy_end == "tend":
        show felina happy 1 onlayer inyourface at Position(ypos=1125)
    else:
        show felina happy mascara 1 onlayer inyourface at Position(ypos=1125)
    with dissolve

    label felina_happy_menu:
        menu:
            extend ""

            "{i}{outlinecolor=4f1313}• ''I sunk my blade in your heart because I didn't need you. I still don't need you.''{/outlinecolor}{/i}" if happy_end == "slay":
                jump felina_violence_join

            "{i}• (Explore) [[Address this vessel's statement directly.]{/i}":
                menu:
                    extend ""

                    "{i}• ''I was so glad to dance with you.''{/i}" if happy_end == "dance":
                        $ felina_fight_effective_resistance -= 2
                        voice "audio/_pristine/voice/happy/mound/9.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting pity smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "Then dance with me again, and we'll never have to stop.\n"

                    "{i}• ''That was a mockery of a life we shared.''{/i}":
                        $ felina_fight_effective_resistance -= 1
                        voice "audio/_pristine/voice/happy/mound/10.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting closed smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "It was a cruelty of this construct. Leave with me, when the time comes, and we can find a true life together.\n"

                    "{i}• ''I'm sorry I killed you. I didn't know what else I should do.''{/i}" if happy_end == "slay":
                        $ felina_fight_effective_resistance -= 1
                        voice "audio/_pristine/voice/happy/mound/11.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "Do not apologize, for I've never truly died. All you need to do is let go and leave with me.\n"

                    "{i}• ''What we shared there was agony, but it doesn't have to be like that. We can find a way to make things better.''{/i}":
                        $ felina_fight_effective_resistance += 1
                        voice "audio/_pristine/voice/happy/mound/12.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "What we saw was a world without me. Everything will be okay, so long as we leave together.\n"

                    "{i}• ''I'd never want to hold the world still. But is suffering the only alternative?''{/i}":
                        $ felina_fight_effective_resistance += 1
                        voice "audio/_pristine/voice/happy/mound/13.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "There is no suffering but the lies we tell ourselves. The only real suffering would be a world without my mercy.\n"

                    "{i}• ''I'd never want to hold the world still. It needs you.''{/i}":
                        $ felina_fight_effective_resistance -= 1
                        voice "audio/_pristine/voice/happy/mound/14.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "Then you're starting to wake up. Leave with me, when the time comes, and we can dance forever.\n"

                    "{i}• ''The only reason we weren't happy was because we couldn't forget. There's a version of that world worth living in.''{/i}":
                        $ felina_fight_effective_resistance += 1
                        voice "audio/_pristine/voice/happy/mound/15a.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting pissed talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "You steep yourself deeper in delusion. I pity you for the thoughts that dance in your mind. And I will break them before we're through.\n"

                    "{i}• (Return){/i}":
                        jump felina_happy_menu


            "{i}• [[Appeal to your shared humanity.] ''You speak about life and death and change and stagnation, but that isn't what any of this has been about.''{/i}" if felina_appeal_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''This has always just been about us. Two people forced to hurt each other again and again and again. But we don't have to hurt each other anymore.''{/i}" if felina_appeal_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''There can be love and conflict and beauty and ugliness between us without bringing the whole of reality into the picture.''{/i}" if felina_appeal_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''We're not the whole of reality. Why won't you see me the way I still see you? Why won't you see me for what I am?''{/i}" if felina_appeal_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''This doesn't have to be so big. You can come back down to my level. You can come back to me.''{/i}" if felina_appeal_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Reject her authority.] ''You've done nothing but lecture me since the minute I got here.''{/i}" if felina_lecture_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''You use all these pretentious metaphors and pretend you're making grand proclamations about who I am and who you are. But really you aren't saying much of anything.''{/i}" if felina_lecture_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''It doesn't even matter what I say to you, because you're just going to keep telling me your perspective like it's some universal truth.''{/i}" if felina_lecture_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''It was so much better when I was with your vessels. Even at their worst, they all still heard me.''{/i}" if felina_lecture_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''I don't know what you are, but you aren't any of them. You're just something wearing their skin.''{/i}" if felina_lecture_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Argue your independence.] ''You act as though the world can't exist without you. But I've existed without you.''{/i}" if felina_assert_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''What are the woods, then? What is the cabin? What is the time we've spent apart if not me existing as myself?''{/i}" if felina_assert_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''I wouldn't be here if destroying you would leave all of reality a colorless blur.''{/i}" if felina_assert_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''I'd rather trust an ignorant soul who died trying to make things better than a god who'd let the wheel of suffering turn forever.''{/i}" if felina_assert_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''If I need to destroy you to build a better world, then I will.''{/i}" if felina_assert_count == 4:
                $ felina_assert_lethal = True
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''Who said anything about destroying you? I just need to make you stop.''{/i}" if felina_assert_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Reject her perspective.] ''I won't engage with violence.''{/i}" if felina_rejection_count == 0:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''It doesn't matter how I feel. Death, suffering, and oblivion shouldn't fall on others. If we are able to transcend death, then we are responsible for those it holds captive.''{/i}" if felina_rejection_count == 1:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''Suffering born in delusion is still suffering. It doesn't matter what we are now. We hurt each other, and we shouldn't have done that. We cannot let a world be spun out of that pain.''{/i}" if felina_rejection_count == 2:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''You reject the suffering of material reality, and yet you cling to its framework for meaning. We can be better than this.''{/i}" if felina_rejection_count == 3:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''You claim your destruction would steal meaning from existence, but if my actions can make existence worse, then there must be actions that make it better. Perfection implies finality, and nothing is final.''{/i}" if felina_rejection_count == 4:
                jump felina_rejection_join

            "{i}• ''I get it. There's no need for us to keep fighting. I'll leave with you. I just don't know how.'' [[Stop the fight early and surrender.]{/i}" if felina_round >= 2:
                $ achievement.grant("ACH_END_FREE2")
                jump felina_freedom_join

            "{i}• [[Remain silent.]{/i}":
                jump felina_silence

    jump felina_fight_staging




label felina_cage_start:

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
        show pop cage onlayer inyourface at shakeshort, Position(ypos=1125)
    else:
        $ previous_transform = "handsflip"
        show shifting hands onlayer front at flip, shakeshort, Position(ypos=1125)
        show pop cage onlayer inyourface at flip, shakeshort, Position(ypos=1125)
    with Dissolve(0.25)
    $ renpy.pause(1.9)
    $ gallery_cage.unlock_item(20)
    $ renpy.save_persistent()

    play audio "audio/_pristine/sfx/Cage_chain floor breaks fall LONG_1.flac"
    if cage_blade_thrown:
        show fight cage onlayer inyourface at Position(ypos=1125)
    else:
        show fight cage armed onlayer inyourface at Position(ypos=1125)
    $ renpy.pause(0.01)
    voice "audio/_pristine/voice/cage/mound/1.flac"
    mounds "Fear is a chain around the neck and a needle in the eye.\n"
    voice "audio/_pristine/voice/cage/mound/2.flac"
    hide fight onlayer inyourface
    hide shifting onlayer front
    hide pop onlayer inyourface
    show farback quiet onlayer farback at Position(ypos=1125)
    show back awakening onlayer back at Position(ypos=1125)
    show midground awakening onlayer front at Position(ypos=1125)
    show hair awakened onlayer front at Position(ypos=1125)
    show dress felina onlayer front at Position(ypos=1125)
    show shifting martyrs talk onlayer front at Position(ypos=1125)
    show felina cage 1 talk onlayer inyourface at Position(ypos=1125)
    with Dissolve(1.0)
    mound "It was fear that made our prison, and it was fear that told the lie that our spirits were not free to choose.\n"
    if cage_end == "free" or cage_end == "drop":
        voice "audio/_pristine/voice/cage/mound/3.flac"
        show shifting pity smile talk onlayer front at Position(ypos=1125)
        show felina cage 2 talk onlayer inyourface at Position(ypos=1125)
        with dissolve
        mound "But even bound, you saw a light, and you gave me the wisdom to speak my heart and shed my doubts.\n"
        voice "audio/_pristine/voice/cage/mound/4.flac"
        show shifting smile talk onlayer front at Position(ypos=1125)
        show felina cage 3 talk onlayer inyourface at Position(ypos=1125)
        with dissolve
        mound "Without fear, suffering ceases to be. Without fear, death dissolves. Without fear, we are free to choose beauty.\n"
        if cage_end == "drop":
            voice "audio/_pristine/voice/cage/mound/5.flac"
            show shifting martyrs talk onlayer front at Position(ypos=1125)
            show felina cage 2 talk onlayer inyourface at Position(ypos=1125)
            with dissolve
            mound "Even when we reached the end and you sent me plunging back into the abyss, I was already free of fear. That act was your final assertion of will over chains.\n"
    elif cage_end == "stuck":
        voice "audio/_pristine/voice/cage/mound/6.flac"
        show shifting smile talk onlayer front at Position(ypos=1125)
        show felina cage 3 talk onlayer inyourface at Position(ypos=1125)
        with dissolve
        mound "But together we left it all behind, and found a world free of burdens. We found the beauty in accepting our dance.\n"
    elif cage_end == "slay":
        voice "audio/_pristine/voice/cage/mound/7.flac"
        show shifting smile talk onlayer front at Position(ypos=1125)
        show felina cage 2 talk onlayer inyourface at Position(ypos=1125)
        with dissolve
        mound "Even while you cut yourself 'free,' it was that lie that kept us bound in the dark. It was that lie that drove your edge through my heart.\n"
    voice "audio/_pristine/voice/cage/mound/8.flac"
    show shifting pity smile talk onlayer front at Position(ypos=1125)
    show felina cage 1 talk onlayer inyourface at Position(ypos=1125)
    with dissolve
    mound "This construct is a machine of fear. It has no place in our divine hearts. Shatter it. Leave with me.\n"
    show shifting pity smile onlayer front

    label felina_cage_menu:
        menu:
            extend ""

            "{i}{outlinecolor=4f1313}• ''It was so easy to let you fall into the abyss. You needed me, but I've never needed you.''{/outlinecolor}{/i}" if cage_end == "drop":
                jump felina_violence_join

            "{i}{outlinecolor=4f1313}• ''Fear or not, I drove that blade into your heart, and I remained while you were taken away.''{/outlinecolor}{/i}" if cage_end == "slay":
                jump felina_violence_join

            "{i}• (Explore) [[Address this vessel's statement directly.]{/i}":
                menu:
                    extend ""

                    "{i}• ''I was happy to leave with you.''{/i}" if cage_end == "free":
                        $ felina_fight_effective_resistance -= 1
                        voice "audio/_pristine/voice/cage/mound/14.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "And I hope you'll be happy to leave with me again.\n"
                        show shifting smile onlayer front
                        menu:
                            extend ""

                            "{i}• ''I'm ready. I want to leave with you.'' [[Stop the fight early and surrender.]{/i}" if felina_round >= 2:
                                $ achievement.grant("ACH_END_FREE2")
                                jump felina_freedom_join

                            "{i}• ''I won't leave with you. Not until you see things from my perspective.''{/i}" if felina_round >= 2:
                                voice "audio/voices/felina/fight/dams8.flac"
                                show shifting pity smile talk onlayer front
                                mound "If you need more time to open your eyes, then I will give you all the time in the world.\n"

                    "{i}• ''Neither of us could have been free without the other.''{/i}" if cage_end == "free":
                        $ felina_fight_effective_resistance -= 1
                        voice "audio/_pristine/voice/cage/mound/9.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting closed smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "Just as neither of us can be free without the other now.\n"

                    "{i}• ''I was happy to watch the world with you.''{/i}" if cage_end == "stuck":
                        $ felina_fight_effective_resistance -= 1
                        voice "audio/_pristine/voice/cage/mound/15.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting closed smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "And I hope you'll be happy to watch the world with me again.\n"

                    "{i}• ''You were okay with me dropping you into the abyss?''{/i}" if cage_end == "drop":
                        #$ felina_fight_effective_resistance -= 1
                        voice "audio/_pristine/voice/cage/mound/10.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting closed smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "Of course I was. And I've grown so much from it.\n"

                    "{i}• ''I'm so sorry for killing you.''{/i}" if cage_end == "slay":
                        $ felina_fight_effective_resistance -= 1
                        voice "audio/_pristine/voice/cage/mound/11.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "There is no need for you to apologize. We were shadows of our true selves. And shadows cannot truly die.\n"

                    "{i}• ''No matter what we did, we kept trapping each other again, and again, and again.''{/i}":
                        $ felina_fight_effective_resistance -= 1
                        voice "audio/_pristine/voice/cage/mound/12.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "And yet here we are, bound only by our final shackles. It will have all been worth it once we're finally free.\n"

                    "{i}• ''Death is more than fear. It is reality. Just because we can reject it, does not mean the world is free of it.''{/i}":
                        $ felina_fight_effective_resistance += 1
                        voice "audio/_pristine/voice/cage/mound/16.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "Their prisons are their own, and should we not give them the ability to find their freedom? If we can free ourselves, the world can certainly follow suit.\n"

                    "{i}• ''I'm sorry for dropping you into the abyss.''{/i}" if cage_end == "drop":
                        $ felina_fight_effective_resistance -= 1
                        voice "audio/_pristine/voice/cage/mound/13.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting pity smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "There is no need for you to apologize. It was a lesson I sorely needed to realize my freedom.\n"

                    "{i}• ''You speak as if I chose to follow you. You ripped my head from my body and made me watch us kill each other.''{/i}" if cage_end == "stuck":
                        $ felina_fight_effective_resistance += 1
                        voice "audio/_pristine/voice/cage/mound/17.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting pity smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "You walked the path that took you there, and just like all paths, it did not last forever. Did you not value the time we spent together?\n"

                    "{i}• ''You denounce fear and yet you laud violence and strife as necessary and beautiful. Can there be courage without fear? And is courage not beautiful?''{/i}" if cage_end == "stuck":
                        $ felina_fight_effective_resistance += 1
                        voice "audio/_pristine/voice/cage/mound/18.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting martyrs talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "Fear is a delusion. It places barriers in the minds of those who do not free themselves from it. To see that there is no horror in living, to embrace the violence and the pain. That is the only way to truly appreciate the tapestry of the divine.\n"

                    "{i}• ''You're right. There's nothing for us here.''{/i}":
                        $ felina_fight_effective_resistance -= 1
                        voice "audio/_pristine/voice/cage/mound/19.flac"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show shifting smile talk onlayer front
                        hide felina onlayer inyourface
                        with dissolve
                        mound "Their prisons are their own, and should we not give them the ability to find their freedom? If we can free ourselves, the world can certainly follow suit.\n"
                        mound "Then leave with me. Now. Forget this struggle, and dance with me forever.\n"
                        show shifting smile onlayer front
                        menu:
                            extend ""

                            "{i}• ''I'm ready. I want to leave with you.'' [[Stop the fight early and surrender.]{/i}" if felina_round >= 2:
                                $ achievement.grant("ACH_END_FREE2")
                                jump felina_freedom_join

                            "{i}• ''I won't leave with you. Not until you see things from my perspective.''{/i}" if felina_round >= 2:
                                voice "audio/voices/felina/fight/dams8.flac"
                                show shifting pity smile talk onlayer front
                                mound "If you need more time to open your eyes, then I will give you all the time in the world.\n"



                    "{i}• (Return){/i}":
                        jump felina_cage_menu


            "{i}• [[Appeal to your shared humanity.] ''You speak about life and death and change and stagnation, but that isn't what any of this has been about.''{/i}" if felina_appeal_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''This has always just been about us. Two people forced to hurt each other again and again and again. But we don't have to hurt each other anymore.''{/i}" if felina_appeal_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''There can be love and conflict and beauty and ugliness between us without bringing the whole of reality into the picture.''{/i}" if felina_appeal_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''We're not the whole of reality. Why won't you see me the way I still see you? Why won't you see me for what I am?''{/i}" if felina_appeal_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Continue to appeal to your shared humanity.] ''This doesn't have to be so big. You can come back down to my level. You can come back to me.''{/i}" if felina_appeal_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_appeal_join

            "{i}• [[Reject her authority.] ''You've done nothing but lecture me since the minute I got here.''{/i}" if felina_lecture_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''You use all these pretentious metaphors and pretend you're making grand proclamations about who I am and who you are. But really you aren't saying much of anything.''{/i}" if felina_lecture_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''It doesn't even matter what I say to you, because you're just going to keep telling me your perspective like it's some universal truth.''{/i}" if felina_lecture_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''It was so much better when I was with your vessels. Even at their worst, they all still heard me.''{/i}" if felina_lecture_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Continue to reject her authority.] ''I don't know what you are, but you aren't any of them. You're just something wearing their skin.''{/i}" if felina_lecture_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_lecture_join

            "{i}• [[Argue your independence.] ''You act as though the world can't exist without you. But I've existed without you.''{/i}" if felina_assert_count == 0:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''What are the woods, then? What is the cabin? What is the time we've spent apart if not me existing as myself?''{/i}" if felina_assert_count == 1:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''I wouldn't be here if destroying you would leave all of reality a colorless blur.''{/i}" if felina_assert_count == 2:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''I'd rather trust an ignorant soul who died trying to make things better than a god who'd let the wheel of suffering turn forever.''{/i}" if felina_assert_count == 3:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''If I need to destroy you to build a better world, then I will.''{/i}" if felina_assert_count == 4:
                $ felina_assert_lethal = True
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Continue to argue your independence.] ''Who said anything about destroying you? I just need to make you stop.''{/i}" if felina_assert_count == 4:
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                jump felina_assert_join

            "{i}• [[Reject her perspective.] ''I won't engage with violence.''{/i}" if felina_rejection_count == 0:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''It doesn't matter how I feel. Death, suffering, and oblivion shouldn't fall on others. If we are able to transcend death, then we are responsible for those it holds captive.''{/i}" if felina_rejection_count == 1:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''Suffering born in delusion is still suffering. It doesn't matter what we are now. We hurt each other, and we shouldn't have done that. We cannot let a world be spun out of that pain.''{/i}" if felina_rejection_count == 2:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''You reject the suffering of material reality, and yet you cling to its framework for meaning. We can be better than this.''{/i}" if felina_rejection_count == 3:
                jump felina_rejection_join

            "{i}• [[Continue to reject her perspective.] ''You claim your destruction would steal meaning from existence, but if my actions can make existence worse, then there must be actions that make it better. Perfection implies finality, and nothing is final.''{/i}" if felina_rejection_count == 4:
                jump felina_rejection_join

            "{i}• ''I get it. There's no need for us to keep fighting. I'll leave with you. I just don't know how.'' [[Stop the fight early and surrender.]{/i}" if felina_round >= 2:
                $ achievement.grant("ACH_END_FREE2")
                jump felina_freedom_join

            "{i}• [[Remain silent.]{/i}":
                jump felina_silence

    jump felina_fight_staging

return
