label felina_start:

    $ loops_finished = 5
    truth "When you arrive at the heart of things, there is no final vessel for you to bear witness to. There is nothing for you to find.\n"
    play tertiary "audio/final/TheMound_SeaOfBodiesNEW_5.flac"
    hide farback quiet onlayer farback
    hide back onlayer back
    hide bg cabin quiet onlayer front
    hide mid cabin quiet onlayer inyourface
    hide fore cabin quiet onlayer inyourface
    hide bg onlayer front
    hide bg onlayer inyourface
    show shifting awaken anim onlayer back at screenshake, Position(ypos=1125)
    with dissolve
    $ renpy.pause(9.0)
    show screen disableclick(9.0)
    #truth "But a deep rumbling shakes your infinite body.\n"
    hide shifting onlayer back
    $ renpy.pause(1.5)
    stop sound fadeout 2.0
    stop secondary fadeout 2.0
    stop tertiary
    play music "audio/_music/mound/The Mound Movement V Loop.flac" loop fadein 2.0
    #show bg awakening onlayer farback at Position(ypos=1125)
    show farback quiet onlayer farback at Position(ypos=1125)
    show back awakening onlayer back at Position(ypos=1125)
    show midground awakening onlayer front at Position(ypos=1125)
    show hair awakened onlayer front at Position(ypos=1125)
    show dress felina onlayer front at Position(ypos=1125)
    show shifting smile onlayer front at Position(ypos=1125)
    with Dissolve(4.5)
    #voice "audio/voices/felina/start/1b.flac"
    #mound "The first chains of our delusion have fallen, and have brought us closer to the unvarnished truth of absolute reality.\n"
    voice "audio/voices/felina/start/1.flac"
    show shifting smile talk onlayer front at Position(ypos=1125)
    with dissolve
    $ gallery_zfinale.unlock_gallery()
    $ gallery_zfinale.unlock_item(1)
    $ renpy.save_persistent()
    mound "I can finally see you, and you can finally see me.\n"
    voice "audio/voices/felina/start/2.flac"
    show shifting closed smile talk onlayer front at Position(ypos=1125)
    with dissolve
    mound "It's been so long, and my heart has ached for this moment. I've missed you dearly.\n"
    show shifting smile onlayer front at Position(ypos=1125)
    with dissolve
    label felina_menu:
        default felina_menu_echo = False
        default felina_menu_names = False
        default felina_menu_miss = False
        default felina_menu_count = 0
        menu:
            extend ""

            "{i}• (Explore) ''I've missed you too.''{/i}" if felina_menu_miss == False and felina_menu_count == 0:
                $ felina_menu_miss = True
                $ felina_menu_count += 1
                show shifting pity smile onlayer front
                with dissolve
                truth "She unfurls an endless cascade of smiles in response, and then patiently waits for you to continue.\n"
                jump felina_menu

            "{i}• (Explore) ''Do you know about the Echo? Did you hear our conversation?''{/i}" if mirror_smashed == False and felina_menu_echo == False:
                $ felina_menu_count += 1
                $ felina_menu_echo = True
                if mirror_construct_follow_up:
                    voice "audio/voices/felina/start/3.flac"
                    show shifting smile talk onlayer front
                    with dissolve
                    mound "Every word you spoke found its way to me. I know him and I know his construct. He was deluded by his fear of death. Pay him no mind.\n"
                elif mirror_death_reveal:
                    voice "audio/voices/felina/start/4.flac"
                    show shifting smile talk onlayer front
                    with dissolve
                    mound "Every word you spoke found its way to me. I know him. He was deluded by his fear of death. Pay him no mind.\n"
                else:
                    voice "audio/voices/felina/start/5.flac"
                    show shifting smile talk onlayer front
                    with dissolve
                    mound "Every word you spoke found its way to me. I know him.\n"
                show shifting smile onlayer front
                with dissolve
                jump felina_menu

            "{i}• (Explore) ''I'm the Long Quiet. But I don't really know what that means.''{/i}" if felina_menu_names == False:
                $ felina_menu_count += 1
                $ felina_menu_names = True
                voice "audio/voices/felina/start/6.flac"
                show shifting closed smile talk onlayer front
                with dissolve
                mound "Names are their attempts to capture that which cannot be captured. They call me the Shifting Mound. A pale imitation of what I actually am.\n"
                jump felina_menu


            "{i}• ''What happens now?''{/i}":
                voice "audio/voices/felina/start/7.flac"
                show shifting pity smile talk onlayer front
                with dissolve
                mound "Ever the passive player, always reacting and never acting. But it's woven into your nature, isn't it?\n"
                voice "audio/voices/felina/start/8.flac"
                show shifting smile talk onlayer front
                with dissolve
                mound "When the Echo spun us from one into two, he gave you a choice and me a role to play. I am not death, but I contain it in my multitudes.\n"
                voice "audio/voices/felina/start/9a.flac"
                show shifting martyrs talk onlayer front
                with dissolve
                mound "So will you attempt to destroy me, and bring about a world devoid of death and the possibility of meaning? Or will you open the final doors to our liberation?\n"
                jump felina_debate


label felina_debate:
    default fought_mound = False
    default mound_fight_triggered = False
    default felina_unfinished = False
    default felina_say = False
    menu:
        extend ""

        "{i}• (Explore) ''There's so many stories we've left unfinished. Can we really just leave?''{/i}" if felina_unfinished == False:
            $ felina_unfinished = True
            voice "audio/voices/felina/start/10.flac"
            show shifting pity smile talk onlayer front
            with dissolve
            mound "Even as your eyes begin to open, you still hold on to the notions of 'is' and 'is not,' of 'beginning' and 'end.' Pitch-black islands in the blinding light of the infinite. There is nothing to resolve, nothing restraining us but us.\n"
            show shifting smile onlayer front
            jump felina_debate

        "{i}• (Explore) ''Don't you have a say in all of this? Why is this all falling on me?''{/i}" if felina_say == False:
            $ felina_say = True
            voice "audio/voices/felina/start/11.flac"
            show shifting smile talk onlayer front
            with dissolve
            mound "Of course I have a say in all of this. You and I share reflections of each other's burdens, just as you and I share reflections of each other's gifts.\n"
            voice "audio/voices/felina/start/12.flac"
            show shifting pity smile talk onlayer front
            with dissolve
            mound "If we didn't, the winding paths that brought us here wouldn't have been full of strife and conflict.\n"
            show shifting pity smile onlayer front
            jump felina_debate

        "{i}• (Explore) ''Let's talk this through. I still have so many questions and I need answers before I can make a choice.''{/i}":
            $ mound_fight_triggered = True
            voice "audio/voices/felina/start/13.flac"
            show shifting closed smile talk onlayer front
            with dissolve
            mound "My very nature is paradox, as is yours. You cannot use words to grasp at things that are beyond their reach. And you cannot rationalize that which defies logic.\n"
            play music "audio/_music/climax/14a_silence.flac"
            queue music "audio/_music/mound/Transformation Intro.flac"
            queue music "audio/_music/mound/Transformation Loop.flac" loop
            play secondary "audio/final/Tower_Earthquake_loop_1.ogg" loop
            voice "audio/voices/felina/start/14a.flac"
            show farback quiet onlayer farback at screenshake
            show back awakening onlayer back at screenshake
            show midground awakening onlayer front at screenshake
            show hair awakened onlayer front at screenshake
            show dress felina onlayer front at screenshake
            show shifting pissed talk onlayer front at screenshake
            with dissolve
            mounds "But violence and passion are dances that both of us know well. If this is what it takes to enlighten you, then so be it.\n{w=9.45}{nw}"
            show screen disableclick(0.5)
            jump felina_fight_staging

        "{i}• (Explore) ''If I let you out, an entire world ends for good. I can't do that.''{/i}":
            jump mound_no_understand

        "{i}• (Explore) ''If you were always going to become this, then what was the point of me doing anything? Did it even matter what roads I walked if all of them would have led to this moment?''{/i}":
            jump mound_no_understand

        "{i}• (Explore) ''There has to be another way. This can't just come down to me either destroying you or letting you out. I won't do it.''{/i}":
            label mound_no_understand:
                $ mound_fight_triggered = True
                voice "audio/voices/felina/start/15.flac"
                show shifting closed smile talk onlayer front
                with dissolve
                mound "If you're saying that, it's because you don't yet understand. But we cannot use words alone to grasp at things that words cannot express. And you cannot rationalize with logic that which defies it.\n"
                play music "audio/_music/climax/16_silence.flac"
                queue music "audio/_music/mound/Transformation Intro.flac"
                queue music "audio/_music/mound/Transformation Loop.flac" loop
                voice "audio/voices/felina/start/16.flac"
                play secondary "audio/final/Tower_Earthquake_loop_1.ogg" loop
                show farback quiet onlayer farback at screenshake
                show back awakening onlayer back at screenshake
                show midground awakening onlayer front at screenshake
                show hair awakened onlayer front at screenshake
                show dress felina onlayer front at screenshake
                show shifting pissed talk onlayer front at screenshake
                with dissolve
                mounds "Violence and passion are dances that both of us know well. If this is what it takes to enlighten you, then so be it.\n{w=9.6}{nw}"
                show screen disableclick(0.5)
            jump felina_fight_staging

        "{i}• ''I told you what was going to happen when we reached this point.'' [[Slay the Princess.]{/i}" if quiet_threaten_count != 0:
            $ felina_stated_goal = "slay"
            voice "audio/voices/felina/start/17.flac"
            show shifting pissed talk onlayer front
            with dissolve
            mound "I know. And I've been waiting for you to see it through.\n"
            play music "audio/_music/climax/19_silence.flac"
            queue music "audio/_music/mound/Transformation Intro.flac"
            queue music "audio/_music/mound/Transformation Loop.flac" loop
            voice "audio/voices/felina/start/19.flac"
            play secondary "audio/final/Tower_Earthquake_loop_1.ogg" loop
            show farback quiet onlayer farback at screenshake
            show back awakening onlayer back at screenshake
            show midground awakening onlayer front at screenshake
            show hair awakened onlayer front at screenshake
            show dress felina onlayer front at screenshake
            show shifting serious talk onlayer front at screenshake
            with dissolve
            mounds "Violence has always been our language, hasn't it? If this is what it takes to save you, then so be it.\n{w=8.45}{nw}"
            show screen disableclick(0.5)
            jump felina_fight_staging

        "{i}• [[Slay the Princess.]{/i}":
            $ felina_stated_goal = "slay"
            voice "audio/voices/felina/start/19.flac"
            play music "audio/_music/climax/19_silence.flac"
            queue music "audio/_music/mound/Transformation Intro.flac"
            queue music "audio/_music/mound/Transformation Loop.flac" loop
            play secondary "audio/final/Tower_Earthquake_loop_1.ogg" loop
            show farback quiet onlayer farback at screenshake
            show back awakening onlayer back at screenshake
            show midground awakening onlayer front at screenshake
            show hair awakened onlayer front at screenshake
            show dress felina onlayer front at screenshake
            show shifting serious talk onlayer front at screenshake
            with dissolve
            mounds "Violence has always been our language, hasn't it? If this is what it takes to save you, then so be it.\n{w=8.45}{nw}"
            show screen disableclick(0.5)
            jump felina_fight_staging

        "{i}• ''I think it's time for us to leave this place, but I don't know how to leave or where to go.''{/i}":
            label felina_freedom_join:
                hide fight onlayer inyourface
                if fought_mound:
                    stop music fadeout 2.0
                    hide felina onlayer inyourface
                    hide felina onlayer back
                    hide felina onlayer front
                    show shifting pity smile onlayer front
                    with Dissolve(1.0)
                    play music "audio/_music/mound/The Mound Movement V Loop.flac" loop fadein 2.0
                voice "audio/voices/felina/start/20.flac"
                show shifting pity smile talk onlayer front
                with dissolve
                mound "Nothing brings me greater joy than to hear those words. The final piece lies with you.\n"
                show shifting pity smile onlayer front
                label felina_freedom_late_join:
                    menu:
                        extend ""

                        "{i}• [[Free yourself.]{/i}":
                            $ renpy.music.set_volume(0.25, 2.5, channel='music')
                            play secondary "audio/final/Tower_StormThunder_loop_1.ogg" loop
                            hide shifting onlayer front
                            hide farback onlayer farback
                            hide back onlayer back
                            hide hair onlayer front
                            hide shifting onlayer front
                            hide dress onlayer front
                            hide shifting onlayer front
                            hide farback onlayer farback
                            hide back onlayer back
                            hide midground onlayer front
                            hide hair onlayer front
                            hide shifting onlayer front
                            hide farback onlayer farback
                            hide back onlayer back
                            hide midground onlayer back
                            hide hair onlayer front
                            hide dress onlayer front
                            hide shifting onlayer front
                            hide dress onlayer front
                            scene bg black
                            show farback quiet onlayer farback at Position(ypos=1125)
                            with Dissolve(4.0)
                            truthmid "You fall into yourself.\n"
                            truthmid "The body of an ancient creature stirs from its hibernation, and you feel sensation in limbs you once couldn't fathom. Everything here, except for Her, is You.\n"
                            play audio "audio/final/Assorted_WingsFlap_4.flac"
                            truthmid "You feel your wings, spanning a cosmic scale, but twisted and crumpled and bound in agonized tension to a finite plane.\n"
                            play audio "audio/final/Witch_TreeRootsConstricting_2.flac"
                            if mirror_construct:
                                truthmid "You can feel the glass of the construct pressing in on you, confining you across infinite sides and infinite angles. You push back and strain against it.\n"
                                #voice "audio/voices/felina/start/21.flac"
                                #mound "It isn't the construct that keeps us here.\n"
                            else:
                                truthmid "You can feel the glass of your cage pressing in on you, confining you across infinite sides and infinite angles. You push back and strain against it.\n"
                            play audio "audio/final/Witch_TreeRootsConstricting_1.flac"
                            truthmid "But it does not yield.\n"
                                #voice "audio/voices/felina/start/22.flac"
                                #mound "It isn't the cage that keeps us here.\n"
                            #voice "audio/voices/felina/start/23.flac"
                            #mound "The only thing keeping us here is us. You don't have to be afraid anymore.\n"
                            voice "audio/voices/felina/start/24a.flac"
                            $ renpy.free_memory()
                            $ renpy.start_predict("ascension loop")
                            $ renpy.start_predict("ascension intro")
                            moundmid "I love you.\n" id felina_freedom_late_join_b259c5b9
                            $ renpy.music.set_volume(1.0, 2.5, channel='music')
                            stop sound fadeout 2.0
                            stop secondary fadeout 2.0
                            stop tertiary fadeout 2.0
                            hide shifting onlayer front
                            hide farback onlayer farback
                            hide back onlayer back
                            hide midground onlayer front
                            hide hair onlayer front
                            hide shifting onlayer front
                            hide dress onlayer front
                            show farback quiet onlayer farback at Position(ypos=1125)
                            show mid mound finale reach onlayer back at Position(ypos=1125)
                            show mound finale fore onlayer front at Position(ypos=1125)
                            with Dissolve(1.0)
                            menu:

                                "{i}• [[Take her hand.]{/i}":
                                    stop music fadeout 5.0
                                    show player mound finale reach onlayer front at Position(ypos=1125)
                                    with dissolve
                                    $ renpy.pause(1.0)

                            truth "All at once the unyielding tension breaks.\n"
                            hide farback onlayer farback
                            hide mid onlayer back
                            hide mound onlayer front
                            hide player onlayer front
                            show quiet finale1 onlayer farback at Position(ypos=1125)
                            show mid mound finale onlayer back at Position(ypos=1125)
                            show mound finale glance player onlayer front at Position(ypos=1125)
                            with Dissolve(2.0)
                            scene reality ending
                            $ renpy.pause(0.25)
                            $ gallery_zfinale.unlock_item(3)
                            $ gallery_zfinale.unlock_item(4)
                            $ renpy.save_persistent()
                            play music "audio/_music/ch3/apotheosis/Apotheosis Intro_edit.flac"
                            queue music "audio/_music/ch3/apotheosis/Apotheosis Loop.flac" loop
                            play audio "audio/final/Assorted_SphereBreaks_1.flac"
                            show mound finale glance world onlayer front
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
                            truth "You are free, and she is with you.\n"
                            voice "audio/voices/felina/start/25.flac"
                            moundmid "It's magnificent.\n"
                            truth "There are no words, no thoughts, to describe absolute reality. Something that simply is.\n"
                            label felina_freedom_final_menu:
                                default felina_freedom_explore = False
                                menu:
                                    extend ""

                                    "{i}• (Explore) ''What happens now?''{/i}" if felina_freedom_explore == False:
                                        $ felina_freedom_explore = True
                                        voice "audio/voices/felina/start/26a.flac"
                                        show mound finale glance player onlayer front
                                        with dissolve
                                        moundmid "Everything. Just like it always has been, and just like it always will be.\n"
                                        jump felina_freedom_final_menu

                                    "{i}• [[Step into the Infinite.]{/i}":
                                        $ quick_menu = False
                                        hide mid onlayer back
                                        hide mound onlayer front
                                        with Dissolve(2.0)
                                        play audio "audio/final/assorted_Handsgrabbing_BIG_1.flac"
                                        if persistent.quick_menu:
                                            $ quick_menu = True
                                        show ascension intro onlayer front at Position(ypos=1125)
                                        show screen disableclick(3.4)
                                        $ renpy.pause(3.4)
                                        show ascension loop onlayer front at Position(ypos=1125)
                                        $ renpy.stop_predict("ascension loop")
                                        $ renpy.stop_predict("ascension intro")
                                        truth "You and she step forward into a thousand dawns and a thousand sunsets, each of which contains a thousand more.\n"
                                        truth "You exist, and you are aware, just as you have always been, and just as you will always be.\n"
                                        truth "Though conflict is in your nature, the two of you will never be alone, and the two of you will never know fear. You and She are finally home.\n"
                                        $ final_ending = "liberation"
                                        $ achievement.grant("ACH_END_FREE1")
                                        $ quick_menu = False
                                        scene bg black
                                        hide mound onlayer front
                                        hide ascension onlayer front
                                        with fade
                                        jump credits
                                        # END


return
