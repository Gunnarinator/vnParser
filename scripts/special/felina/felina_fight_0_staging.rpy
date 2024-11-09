label felina_fight_staging:
    $ fought_mound = True
    default felina_stated_goal = ""
    default felina_fight_effective_resistance = 0
    default felina_round = 0
    default felina_silence_count = 0
    default felina_rejection_count = 0
    hide fight onlayer inyourface

    $ felina_round += 1

    if felina_violence_counter > 0 and felina_come_from_violence == False and felina_violence_broken == False:
        $ felina_violence_broken = True
        voice "audio/_pristine/voice/_climax/felina/_temp/19.flac"
        show shifting pissed talk onlayer front with dissolve
        mound "That cold fire has left your eyes. Are you finally willing to listen?\n"
    $ come_from_tower = False
    $ felina_come_from_violence = False
    if felina_round == 1:
        stop secondary fadeout 1.0
        #play audio "audio/final/TheMound_SeaOfBodies_1.flac"
        if fifth_mound == "adversary":
            jump felina_adversary_start
        elif fifth_mound == "needle":
            jump felina_adversary2_start
        elif fifth_mound == "beast":
            jump felina_beast_start
        elif fifth_mound == "den":
            jump felina_beast2_start
        elif fifth_mound == "damsel" or fifth_mound == "dereal":
            jump felina_damsel_start
        elif fifth_mound == "nightmare":
            jump felina_nightmare_start
        elif fifth_mound == "clarity":
            jump felina_nightmare2_start
        elif fifth_mound == "prisonerhead" or fifth_mound == "prisonerchain":
            jump felina_prisoner_start
        elif fifth_mound == "razor" or fifth_mound == "razorheart":
            jump felina_razor_start
        elif fifth_mound == "spectre":
            jump felina_spectre_start
        elif fifth_mound == "stranger":
            jump felina_stranger_start
        elif fifth_mound == "tower" or fifth_mound == "apotheosis":
            jump felina_tower_start
        elif fifth_mound == "witch":
            jump felina_witch_start
        elif fifth_mound == "thorn":
            jump felina_thorn_start
        elif fifth_mound == "fury" or fifth_mound == "furyheart":
            jump felina_fury_start
        elif fifth_mound == "greydamsel" or fifth_mound == "greyprisoner":
            jump felina_grey_start
        elif fifth_mound == "wildnerves" or fifth_mound == "wildwound":
            jump felina_wild_start
        elif fifth_mound == "wraith":
            jump felina_wraith_start
        elif fifth_mound == "dragon" or fifth_mound == "dragonfused" or fifth_mound == "dragonhand":
            jump felina_dragon_start
        elif fifth_mound == "cage":
            jump felina_cage_start
        elif fifth_mound == "happy" or fifth_mound == "happydry":
            jump felina_happy_start
        else:
            jump felina_fight_staging

    elif felina_round == 2:
        play audio "audio/final/TheMound_SeaOfBodies_2.flac"
        if fourth_mound == "adversary":
            jump felina_adversary_start
        elif fourth_mound == "needle":
            jump felina_adversary2_start
        elif fourth_mound == "beast":
            jump felina_beast_start
        elif fourth_mound == "den":
            jump felina_beast2_start
        elif fourth_mound == "damsel" or fourth_mound == "dereal":
            jump felina_damsel_start
        elif fourth_mound == "nightmare":
            jump felina_nightmare_start
        elif fourth_mound == "clarity":
            jump felina_nightmare2_start
        elif fourth_mound == "prisonerhead" or fourth_mound == "prisonerchain":
            jump felina_prisoner_start
        elif fourth_mound == "razor" or fourth_mound == "razorheart":
            jump felina_razor_start
        elif fourth_mound == "spectre":
            jump felina_spectre_start
        elif fourth_mound == "stranger":
            jump felina_stranger_start
        elif fourth_mound == "tower" or fourth_mound == "apotheosis":
            jump felina_tower_start
        elif fourth_mound == "witch":
            jump felina_witch_start
        elif fourth_mound == "thorn":
            jump felina_thorn_start
        elif fourth_mound == "fury" or fourth_mound == "furyheart":
            jump felina_fury_start
        elif fourth_mound == "greydamsel" or fourth_mound == "greyprisoner":
            jump felina_grey_start
        elif fourth_mound == "wildnerves" or fourth_mound == "wildwound":
            jump felina_wild_start
        elif fourth_mound == "wraith":
            jump felina_wraith_start
        elif fourth_mound == "dragon" or fourth_mound == "dragonfused" or fourth_mound == "dragonhand":
            jump felina_dragon_start
        elif fourth_mound == "cage":
            jump felina_cage_start
        elif fourth_mound == "happy" or fourth_mound == "happydry":
            jump felina_happy_start
        else:
            jump felina_fight_staging

    elif felina_round == 3:
        play audio "audio/final/TheMound_SeaOfBodies_3.flac"
        if third_mound == "adversary":
            jump felina_adversary_start
        elif third_mound == "needle":
            jump felina_adversary2_start
        elif third_mound == "beast":
            jump felina_beast_start
        elif third_mound == "den":
            jump felina_beast2_start
        elif third_mound == "damsel" or third_mound == "dereal":
            jump felina_damsel_start
        elif third_mound == "nightmare":
            jump felina_nightmare_start
        elif third_mound == "clarity":
            jump felina_nightmare2_start
        elif third_mound == "prisonerhead" or third_mound == "prisonerchain":
            jump felina_prisoner_start
        elif third_mound == "razor" or third_mound == "razorheart":
            jump felina_razor_start
        elif third_mound == "spectre":
            jump felina_spectre_start
        elif third_mound == "stranger":
            jump felina_stranger_start
        elif third_mound == "tower" or third_mound == "apotheosis":
            jump felina_tower_start
        elif third_mound == "witch":
            jump felina_witch_start
        elif third_mound == "thorn":
            jump felina_thorn_start
        elif third_mound == "fury" or third_mound == "furyheart":
            jump felina_fury_start
        elif third_mound == "greydamsel" or third_mound == "greyprisoner":
            jump felina_grey_start
        elif third_mound == "wildnerves" or third_mound == "wildwound":
            jump felina_wild_start
        elif third_mound == "wraith":
            jump felina_wraith_start
        elif third_mound == "dragon" or third_mound == "dragonfused" or third_mound == "dragonhand":
            jump felina_dragon_start
        elif third_mound == "cage":
            jump felina_cage_start
        elif third_mound == "happy" or third_mound == "happydry":
            jump felina_happy_start
        else:
            jump felina_fight_staging

    elif felina_round == 4:
        play audio "audio/final/TheMound_SeaOfBodies_4.flac"
        if second_mound == "adversary":
            jump felina_adversary_start
        elif second_mound == "needle":
            jump felina_adversary2_start
        elif second_mound == "beast":
            jump felina_beast_start
        elif second_mound == "den":
            jump felina_beast2_start
        elif second_mound == "damsel" or second_mound == "dereal":
            jump felina_damsel_start
        elif second_mound == "nightmare":
            jump felina_nightmare_start
        elif second_mound == "clarity":
            jump felina_nightmare2_start
        elif second_mound == "prisonerhead" or second_mound == "prisonerchain":
            jump felina_prisoner_start
        elif second_mound == "razor" or second_mound == "razorheart":
            jump felina_razor_start
        elif second_mound == "spectre":
            jump felina_spectre_start
        elif second_mound == "stranger":
            jump felina_stranger_start
        elif second_mound == "tower" or second_mound == "apotheosis":
            jump felina_tower_start
        elif second_mound == "witch":
            jump felina_witch_start
        elif second_mound == "thorn":
            jump felina_thorn_start
        elif second_mound == "fury" or second_mound == "furyheart":
            jump felina_fury_start
        elif second_mound == "greydamsel" or second_mound == "greyprisoner":
            jump felina_grey_start
        elif second_mound == "wildnerves" or second_mound == "wildwound":
            jump felina_wild_start
        elif second_mound == "wraith":
            jump felina_wraith_start
        elif second_mound == "dragon" or second_mound == "dragonfused" or second_mound == "dragonhand":
            jump felina_dragon_start
        elif second_mound == "cage":
            jump felina_cage_start
        elif second_mound == "happy" or second_mound == "happydry":
            jump felina_happy_start
        else:
            jump felina_fight_staging

    elif felina_round == 5:
        if first_mound == "stranger":
            jump felina_fight_intermission
        else:
            play audio "audio/final/TheMound_SeaOfBodies_5.flac"
            if first_mound == "adversary":
                jump felina_adversary_start
            elif first_mound == "needle":
                jump felina_adversary2_start
            elif first_mound == "beast":
                jump felina_beast_start
            elif first_mound == "den":
                jump felina_beast2_start
            elif first_mound == "damsel" or first_mound == "dereal":
                jump felina_damsel_start
            elif first_mound == "nightmare":
                jump felina_nightmare_start
            elif first_mound == "clarity":
                jump felina_nightmare2_start
            elif first_mound == "prisonerhead" or first_mound == "prisonerchain":
                jump felina_prisoner_start
            elif first_mound == "razor" or first_mound == "razorheart":
                jump felina_razor_start
            elif first_mound == "spectre":
                jump felina_spectre_start
            elif first_mound == "stranger":
                jump felina_stranger_start
            elif first_mound == "tower" or first_mound == "apotheosis":
                jump felina_tower_start
            elif first_mound == "witch":
                jump felina_witch_start
            elif first_mound == "thorn":
                jump felina_thorn_start
            elif first_mound == "fury" or first_mound == "furyheart":
                jump felina_fury_start
            elif first_mound == "greydamsel" or first_mound == "greyprisoner":
                jump felina_grey_start
            elif first_mound == "wildnerves" or first_mound == "wildwound":
                jump felina_wild_start
            elif first_mound == "wraith":
                jump felina_wraith_start
            elif first_mound == "dragon" or first_mound == "dragonfused" or first_mound == "dragonhand":
                jump felina_dragon_start
            elif first_mound == "cage":
                jump felina_cage_start
            elif first_mound == "happy" or first_mound == "happydry":
                jump felina_happy_start
            else:
                jump felina_fight_staging

    else:
        jump felina_fight_intermission

label felina_fight_intermission:
    $ gallery_zfinale.unlock_item(2)
    $ renpy.save_persistent()
    if felina_fight_effective_resistance > 3:
        jump felina_fight_intermission_winning
    elif felina_fight_effective_resistance > 1:
        jump felina_fight_intermission_draw
    else:
        jump felina_fight_intermission_losing

label felina_fight_intermission_winning:

    show shifting serious onlayer front
    with dissolve
    truth "As the clash between you abates, the Princess withdraws, trembling.\n"
    voice "audio/voices/felina/intermission/mound/1a.flac"
    show shifting pissed talk onlayer front
    with dissolve
    mound "You are unmovable. Is it by the design of our conflict that I cannot win, or are you just that fervent in how you cling to delusion?\n"
    if felina_stated_goal == "slay":
        voice "audio/voices/felina/intermission/mound/2.flac"
        show shifting serious talk onlayer front
        with dissolve
        mound "Are you so desperate to destroy me that you've grown blind to the heavenly beauty of our reality?\n"
    #else:
    #    voice "audio/voices/felina/intermission/mound/3.flac"
    #    show shifting pity smile talk onlayer front
    #    with dissolve
    #    mound "Or do you simply see something that I can not?\n"
    jump felina_fight_intermission_join

label felina_fight_intermission_draw:

    show shifting smile onlayer front
    with dissolve
    truth "As the clash between you abates, the Princess relaxes, smiling from a distance. The respite is welcome.\n"
    if felina_stated_goal == "slay":
        voice "audio/voices/felina/intermission/mound/4.flac"
        show shifting smile talk onlayer front
        with dissolve
        mound "Are you still committed to my destruction, or has your resolve started to waver?\n"
    #else:
    #    voice "audio/voices/felina/intermission/mound/5.flac"
    #    show shifting smile talk onlayer front
    #    with dissolve
    #    mound "Are you starting to see?\n"
    jump felina_fight_intermission_join

label felina_fight_intermission_losing:

    show farback quiet onlayer farback at shakeshort
    show back awakening onlayer back at shakeshort
    show midground awakening onlayer front at shakeshort
    show hair awakened onlayer front at shakeshort
    show dress felina onlayer front at shakeshort
    show shifting pity smile onlayer front at shakeshort
    with dissolve
    #truth "As the vessel falls back into the mass of bodies, she rushes towards you, clasping your hands. You begin to shake, your will rapidly dissolving.\n"
    # old
    truth "As the clash between you abates, you begin to shake, your will rapidly dissolving.\n"
    #if felina_stated_goal == "slay":
    #    show shifting pity smile talk onlayer front
    #    with dissolve
    #    voice "audio/voices/felina/intermission/mound/5.flac"
    #    mound "Are you starting to see?\n"
    #else:
    #    voice "audio/voices/felina/intermission/mound/5.flac"
    #    show shifting pity smile talk onlayer front
    #    with dissolve
    #    mound "Are you starting to see?\n"
    jump felina_fight_intermission_join

label felina_fight_intermission_join:

    voice "audio/voices/felina/intermission/mound/6.flac"
    show shifting pose talk onlayer front
    with dissolve
    mounds "Nothing is immutable. Everything that is exists only in relation to everything it isn't.\n"
    voice "audio/voices/felina/intermission/mound/7.flac"
    show shifting pose onlayer front
    with dissolve
    mounds "There is no constant. There is no center.\n"
    if felina_stated_goal == "slay":
        voice "audio/voices/felina/intermission/mound/8.flac"
        show shifting serious talk onlayer front
        with dissolve
        mounds "You cannot remove something without removing the relations which define it. To destroy what you perceive as evil is to damn everything you perceive as good.\n"
    voice "audio/voices/felina/intermission/mound/9.flac"
    show shifting pity smile talk onlayer front
    with dissolve
    mound "Open your eyes and accept what we are. We can leave this prison together.\n"
    show shifting pity smile onlayer front
label felina_fight_intermission_menu:
    default felina_intermission_easy = False
    default felina_intermission_leave = False
    menu:
        extend ""

        "{i}• (Explore) ''It's easy to believe in the things you believe in when you get to sit above it all.''{/i}" if felina_intermission_easy == False:
            $ felina_intermission_easy = True
            voice "audio/voices/felina/intermission/mound/10a.flac"
            show shifting serious talk onlayer front
            with dissolve
            mound "It is from my vantage point that I can see the totality of truth.\n"
            show shifting serious onlayer front
            jump felina_fight_intermission_menu

        "{i}• (Explore) ''What do you think happens if we leave here?''{/i}" if felina_intermission_leave == False:
            $ felina_intermission_leave = True
            voice "audio/voices/felina/intermission/mound/11.flac"
            show shifting martyrs talk onlayer front
            with dissolve
            mound "This universe dies, and a new one is born. And that one dies. And a new one is born. And you and I get to witness it all, weaving a tapestry of life wherever we go.\n"
            show shifting martyrs onlayer front
            jump felina_fight_intermission_menu

        "{i}• ''Okay. I'm ready to go. But how do we leave?''{/i}":
            $ achievement.grant("ACH_END_FREE2")
            stop music
            jump felina_freedom_join

        "{i}• ''I never wanted to fight you. But how do we leave?''{/i}" if felina_stated_goal != "slay":
            $ achievement.grant("ACH_END_FREE2")
            stop music
            jump felina_freedom_join

        "{i}• ''I can't let that happen. I can't let everything die.'' [[Slay the Princess.]{/i}":
            $ felina_stated_goal = "slay"
            jump felina_intermission_post_menu

        "{i}• ''I was told there was enough of you in me to preserve meaning in existence. I'm going to trust that's true.'' [[Slay the Princess.]{/i}" if mirror_fates_worse_than_death:
            $ felina_stated_goal = "slay"
            jump felina_intermission_post_menu

        "{i}• ''I have to fight for a better world. I'm so sorry.'' [[Slay the Princess.]{/i}":
            $ felina_stated_goal = "slay"
            jump felina_intermission_post_menu

        "{i}• ''You are cruelty itself, and I cannot let you exist.'' [[Slay the Princess.]{/i}":
            $ felina_stated_goal = "slay"
            jump felina_intermission_post_menu

        "{i}• ''I don't know what the answer is, but there has to be something else. It can't be {b}this{/b}. I won't kill you, but I won't let you free.''{/i}":
            $ felina_stated_goal = "pacifism"
            voice "audio/voices/felina/intermission/mound/12a.flac"
            show shifting pose talk onlayer front
            with dissolve
            mound "There is no something else. This — what we are — is everything.\n"
            jump felina_intermission_post_menu

        "{i}• ''You've done everything you can to make me understand your perspective, but you keep dismissing mine. If you think you can change me, then I must be able to change you.''{/i}":
            $ felina_stated_goal = "pacifism"
            voice "audio/voices/felina/intermission/mound/13.flac"
            show shifting serious talk onlayer front
            with dissolve
            mound "What I offer you is not perspective. It is truth.\n"
            jump felina_intermission_post_menu

label felina_intermission_post_menu:
    if felina_stated_goal == "slay":
        if felina_fight_effective_resistance > 3:
            voice "audio/voices/felina/intermission/mound/14.flac"
            show shifting serious talk onlayer front
            with dissolve
            mound "Then destroy me, if you're able! But I will not coddle you in my final moments. I will not yield to your delusion without a vicious struggle.\n"
            show shifting serious onlayer front
        elif felina_fight_effective_resistance > 1:
            voice "audio/voices/felina/intermission/mound/15.flac"
            show shifting serious talk onlayer front
            with dissolve
            mound "Then try to destroy me, if you can. But I will not yield easily to your delusion.\n"
            show shifting serious onlayer front
        else:
            voice "audio/voices/felina/intermission/mound/16.flac"
            show shifting closed smile talk onlayer front
            with dissolve
            mound "Even now you think you can destroy me. If it takes all of eternity to break your delusion, I will still break it.\n"
            show shifting pity smile onlayer front
            with dissolve
        voice "audio/voices/felina/intermission/hero/1.flac"
        hero "You don't have to face her alone.\n"
    else:
        label felina_intermission_late_join:
            voice "audio/voices/felina/intermission/hero/2.flac"
            if final_offer:
                show mound death 4 determined onlayer front
                with dissolve
            hero "Whatever you're trying to do right now, you don't have to do it alone.\n"

    label felina_intermission_hero_menu:
        default felina_intermission_hero_menu_cruelty_comment = False
        default felina_intermission_hero_which = False
        menu:
            extend ""

            "{i}• (Explore) ''Which... 'Hero' are you?''{/i}" if felina_intermission_hero_which == False:
                $ felina_intermission_hero_which = True
                voice "audio/voices/felina/intermission/hero/3.flac"
                hero "I'm all of them? I assume in the same way that you're all of you.\n"
                jump felina_intermission_hero_menu

            "{i}• ''You have no idea how good it is to hear you.''{/i}":
                if mirror_n_cruel_count >= 2:
                    $ felina_intermission_hero_menu_cruelty_comment = True
                    voice "audio/voices/felina/intermission/hero/4.flac"
                    hero "After all the times you told me that mirror was going to kill me, I'm genuinely surprised you missed me. But we don't have to get into all that. I'm here now, that's what matters.\n"
                else:
                    voice "audio/voices/felina/intermission/hero/5.flac"
                    hero "It's good to be here.\n"
                label felina_intermission_hero_join:
                    if felina_fight_effective_resistance > 3:
                        if felina_stated_goal == "slay":
                            voice "audio/voices/felina/intermission/hero/6.flac"
                            hero "Seems like you've been doing all right on your own, but I don't think you can strike a decisive blow from out here.\n"
                        else:
                            voice "audio/voices/felina/intermission/hero/7.flac"
                            hero "Seems like you've been doing all right on your own, but she's too many things at once out here. If you want to get through to her, you need some way to get past all of that divine confidence.\n"
                    else:
                        if felina_stated_goal == "slay":
                            voice "audio/voices/felina/intermission/hero/8.flac"
                            hero "You'll never be able to strike a decisive blow from out here.\n"
                        else:
                            voice "audio/voices/felina/intermission/hero/9.flac"
                            hero "She's too many things all at once out here. If you want to get through to her, you need some way to get through all that divine confidence.\n"
                    jump felina_intermission_hero_late_join


            "{i}• ''I can do this alone.''{/i}":
                if felina_fight_effective_resistance > 3:
                    if felina_stated_goal == "slay":
                        voice "audio/voices/felina/intermission/hero/11.flac"
                        hero "You've been doing all right on your own, but you're not going to strike a decisive blow from out here.\n"
                    else:
                        voice "audio/voices/felina/intermission/hero/12.flac"
                        hero "You've been surviving on your own, but you're never going to get through to her while she's like this.\n"
                else:
                    if felina_stated_goal == "slay":
                        voice "audio/voices/felina/intermission/hero/13.flac"
                        hero "I don't think you can. You obviously need help if you're going to strike a decisive blow. You're not going to slay her from out here.\n"
                    else:
                        voice "audio/voices/felina/intermission/hero/14.flac"
                        hero "I don't think you can. She's too many things all at once out here. If you want to get through to her, you need some way to get through all that divine confidence.\n"
                jump felina_intermission_hero_late_join

            "{i}• ''Where's everyone else?''{/i}":
                voice "audio/voices/felina/intermission/hero/15.flac"
                hero "They're still where you left them, stuck in the folds of this place. Part of me is with them, just like part of me is with you right now.\n"
                jump felina_intermission_hero_late_join


            "{i}• ''How are you supposed to help?''{/i}":
                if felina_stated_goal == "slay":
                    voice "audio/voices/felina/intermission/hero/16.flac"
                    hero "You need a better place to strike from if you're going to land a decisive blow. I can help you with that.\n" id felina_intermission_hero_join_5c3c0f76
                else:
                    voice "audio/voices/felina/intermission/hero/17.flac"
                    hero "She's too many things all at once out here. If you want to get through to her, you need some way to get through all that divine confidence. I can help.\n"
                jump felina_intermission_hero_late_join

            "{i}• ''I thought voices weren't allowed here.''{/i}":
                voice "audio/voices/felina/intermission/hero/18.flac"
                hero "Apparently that's not true, but we can worry about it later.\n"
                jump felina_intermission_hero_join

            "{i}• ''I thought you died whenever I looked in the mirror.''{/i}":
                voice "audio/voices/felina/intermission/hero/19.flac"
                hero "I don't think that's wrong, but I'm not sure it's right either. But we can worry about that later.\n"
                jump felina_intermission_hero_join

            "{i}• [[Say nothing.]{/i}":
                jump felina_intermission_hero_join

label felina_intermission_hero_late_join:
    voice "audio/voices/felina/intermission/hero/10.flac"
    hero "There's still a piece of me nestled close to where it all began. I can take you there... I can take you to her heart.\n"
    voice "audio/voices/felina/intermission/mound/17.flac"
    if final_offer:
        show mound death 4 talk final onlayer front
    else:
        show shifting pose talk onlayer front
    with dissolve
    mound "It's time to resume our dance.\n"
    voice "audio/voices/felina/intermission/hero/20.flac"
    if final_offer:
        show mound death 4 talk final smile onlayer front
    else:
        show shifting pose onlayer front
    with dissolve
    hero "She's relentless, isn't she? Let's make this quick. Are you ready?\n"
    menu:
        extend ""

        "{i}• ''I'm ready.''{/i}":
            voice "audio/voices/felina/intermission/hero/21.flac"
            hero "Then let's go.\n"

        "{i}• ''No.''{/i}":
            voice "audio/voices/felina/intermission/hero/22.flac"
            hero "Too bad. We're going, now.\n"

        "{i}• ''I can do this out here on my own.''{/i}":
            voice "audio/voices/felina/intermission/hero/23.flac"
            hero "You can't, and lucky for you, I'm not going to let you try.\n"

        "{i}• [[Say nothing.]{/i}":
            voice "audio/voices/felina/intermission/hero/24.flac"
            hero "I'm going to take that as a yes.\n"

label felina_cabin_staging:

    play audio "audio/final/_dereal_reverse.flac"
    stop music
    stop sound
    stop secondary
    stop tertiary
    hide back onlayer farback
    hide midground onlayer farback
    hide farback onlayer farback
    hide bg onlayer farback
    hide mid onlayer back
    hide mound onlayer front
    hide fore onlayer inyourface
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
    scene dereal reverse
    show screen disableclick(5.0)
    $ renpy.pause(11.0)
    #jump felina_cabin_staging
    scene bg black
    $ default_mouse = "default"
    if first_princess == "harsh" or first_princess == "gentle":
        jump felina_cabin_start

    else:
        jump felina_cabin_strange_start

return
