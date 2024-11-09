label quiet_3_start:
    voice "audio/voices/mound/mound3/1.flac"
    show mound shift talk onlayer front
    with dissolve
    mound "I am a growing chorus of contradiction. A mass of tides ebbing and flowing all at once in more directions than my attention can bear to hold. To look at any one is to shift them all into something new, and to look away is to reshape them yet again.\n"
    voice "audio/voices/mound/mound3/2.flac"
    show mound neutral talk onlayer front
    with dissolve
    mound "All of me is changing, and yet the rest of me is still the same.\n"
    show mound neutral onlayer front
    #with dissolve
label quiet_3_menu:
    default quiet_3_no_contradictions = False
    default quiet_3_how_contradiction = False
    default quiet_3_go_back_worse = False
    default quiet_3_vessel_thoughts = False
    default quiet_3_threaten = False
    default quiet_3_worlds_behind = False
    default quiet_3_desires = False
    default quiet_3_vessel_want = False
    default quiet_3_no_preferences = False
    default quiet_3_how_many = False
    default quiet_3_count = 0
    menu:
        extend ""

        "{i}• (Explore) ''Everything you say feels like a riddle. Can you give me a single straight answer?''{/i}" if mound_pretention_explore == False and quiet_3_count > 0:
            label mound_3_straight_answer:
                $ mound_pretention_explore = True
                voice "audio/_pristine/voice/_climax/mound_interstitial/1.flac"
                mound "I'm sorry. Words are... difficult for me. They never fully weave what I wish to say. If you do not like my answers, then you need not ask me questions.\n"
                voice "audio/_pristine/voice/_climax/mound_interstitial/2a.flac"
                mound "The vessels you choose to bring me carry far more meaning than anything words could say in the spaces between.\n"
                jump quiet_3_menu

        "• (Explore) ''You can't be a contradiction. Contradictions don't exist.''" if quiet_3_no_contradictions == False:
            $ quiet_3_no_contradictions = True
            $ quiet_3_count += 1
            voice "audio/voices/mound/mound3/3.flac"
            show mound pose talk onlayer front
            with dissolve
            mound "And yet my waters flow and my streets bustle. There are no words that can describe me into non-existence. There is no logic that can bind my multitudes.\n"
            voice "audio/voices/mound/mound3/4.flac"
            show mound neutral talk onlayer front
            with dissolve
            mound "I am everything that you have known me to be, but I am also none of it.\n"
            show mound neutral onlayer front
            #with dissolve
            jump quiet_3_menu

        "• (Explore) ''How can you stand to be a contradiction?''" if quiet_3_how_contradiction == False:
            $ quiet_3_how_contradiction = True
            $ quiet_3_count += 1
            voice "audio/voices/mound/mound3/5.flac"
            show mound shift talk onlayer front
            with dissolve
            mound "As easily as you can stand to be you. You are like me, even if you have chosen not to look at the corners of you that do not fit, even if you have chosen to ignore the brilliant contours of your soul.\n"
            show mound shift onlayer front
            #with dissolve
            jump quiet_3_menu

        "• (Explore) ''It doesn't matter how many times I go back. At least one of us always hurts the other. Doesn't that change you? Doesn't that make you worse?''" if quiet_3_go_back_worse == False:
            $ quiet_3_count += 1
            $ quiet_3_go_back_worse = True
            voice "audio/voices/mound/mound3/6.flac"
            show mound neutral talk onlayer front
            with dissolve
            mound "It changes me, but it doesn't make me worse, nor does it make me care for you any less. Does it make you worse? Do you resent me?\n"
            show mound neutral onlayer front
            #with dissolve
            menu:
                extend ""

                "• ''If anything, it makes me like you more. I don't know what that says about me.''":
                    voice "audio/voices/mound/mound3/7.flac"
                    show mound shift talk onlayer front
                    with dissolve
                    mound "It says that your heart is gentle. That even in the darkness, you are guided by compassion.\n"
                    show mound shift onlayer front
                    #with dissolve

                "• ''No, not really. It all seems so distant as soon as I'm near you.''":
                    voice "audio/voices/mound/mound3/8.flac"
                    show mound pose talk onlayer front
                    with dissolve
                    mound "It does seem small from here. And the more we journey, the smaller each of those steps will be. But that doesn't make any of them less special.\n"
                    show mound pose onlayer front
                    #with dissolve

                "• ''I have no opinion one way or another on the matter.''":
                    voice "audio/voices/mound/mound3/9.flac"
                    show mound neutral talk onlayer front
                    with dissolve
                    mound "How strange of you to ask me, then.\n"
                    show mound neutral onlayer front
                    #with dissolve

                "• ''I just want it all to stop.''":
                    voice "audio/voices/mound/mound3/10.flac"
                    show mound shift talk onlayer front
                    with dissolve
                    mound "It will, in time. But you still have a ways to go before we are done. Know that I hold no malice for you.\n"
                    show mound shift onlayer front
                    #with dissolve

                "• ''Yes. You're torturing me, and I hate it. I think I hate you.''":
                    if princess_satisfy >= princess_deny:
                        voice "audio/voices/mound/mound3/14.flac"
                        show mound shift talk onlayer front
                        with dissolve
                        mound "You are what brings me meaning. Know that the pain of your journey will subside in due time.\n"
                    else:
                        voice "audio/voices/mound/mound3/12.flac"
                        show mound shift talk onlayer front
                        with dissolve
                        mound "Know that I hold no malice towards you. The pain of your journey will subside in due time.\n"
                    show mound neutral talk onlayer front
                    with dissolve
                    voice "audio/voices/mound/mound3/13.flac"
                    mound "But you still have a ways to go before we are done.\n"
                    show mound neutral onlayer front
                    #with dissolve

                "• [[Remain silent.]":
                    if princess_satisfy >= princess_deny:
                        voice "audio/voices/mound/mound3/11.flac"
                        show mound shift talk onlayer front
                        with dissolve
                        mound "You are what brings me meaning. Know that the pain of your journey will subside in due time.\n"
                    else:
                        voice "audio/voices/mound/mound3/15.flac"
                        show mound shift talk onlayer front
                        with dissolve
                        mound "Know that I hold no malice towards you. Any pain you may experience along your journey will subside in due time.\n"
                    voice "audio/voices/mound/mound3/16.flac"
                    show mound neutral talk onlayer front
                    with dissolve
                    mound "But you still have a ways to go before we are done.\n"
                    show mound neutral onlayer front
                    #with dissolve

            jump quiet_3_menu

        "• (Explore) ''What do you think of this vessel?''" if quiet_3_vessel_thoughts == False:
            $ quiet_3_count += 1
            $ quiet_3_vessel_thoughts = True
            jump quiet_vessels

        "{i}• (Explore) ''Enough with all of this pretension. You're not actually saying anything.''{/i}" if mound_pretention_explore == False and quiet_3_count > 0:
            jump mound_3_straight_answer

        "• (Explore) ''I'm still planning to kill you once we're done with this.''" if quiet_3_threaten == False and quiet_2_threaten:
            $ quiet_3_count += 1
            jump quiet_3_threaten_join

        "• (Explore) ''You know that at the end of this—once you're finished—I'm going to kill you, right?''" if quiet_3_threaten == False and quiet_2_threaten == False:
            label quiet_3_threaten_join:
                $ quiet_3_count += 1
                $ quiet_threaten_count += 1
                $ quiet_3_threaten = True
                if princess_satisfy >= princess_deny:
                    voice "audio/voices/mound/mound3/17.flac"
                    show mound shift talk onlayer front
                    with dissolve
                    mound "If that remains your choice when all is said and done, then you may try. But know that I do not wish you harm, even if you attempt to destroy me.\n"
                    show mound shift onlayer front
                    #with dissolve
                else:
                    voice "audio/voices/mound/mound3/18.flac"
                    show mound pose talk onlayer front
                    with dissolve
                    mound "If that remains your choice when all is said and done, then you may try. I will regret destroying you, if that is what we come to.\n"
                    show mound pose onlayer front
                    #with dissolve
                jump quiet_3_menu

        "• (Explore) ''Do you know what happens to the worlds we leave behind?''" if quiet_3_worlds_behind == False:
            $ quiet_3_worlds_behind = True
            $ quiet_3_count += 1
            voice "audio/voices/mound/mound3/19a.flac"
            show mound shift talk onlayer front
            with dissolve
            mound "My perspectives are shadowed. You have seen what I have seen, just as I have seen what you have seen. The angles of my vantage do not offer me hidden truths, and my attention is turned inward, except when you are here with me.\n"
            voice "audio/voices/mound/mound3/20.flac"
            show mound neutral talk onlayer front
            with dissolve
            mound "Perhaps this will change when our work is done.\n"
            show mound neutral onlayer front
            #with dissolve
            jump quiet_3_menu

        "• (Explore) ''Have you figured out what you'll want when we've finished?''" if quiet_3_desires == False and quiet_2_want:
            $ quiet_3_desires = True
            $ quiet_3_count += 1
            voice "audio/voices/mound/mound3/21.flac"
            show mound pose talk onlayer front
            with dissolve
            mound "The desires of my multitude thrive in endless competition with themselves, but none of them rise above their dance to influence me.\n"
            if princess_satisfy >= princess_deny:
                voice "audio/voices/mound/mound3/22.flac"
                show mound neutral talk onlayer front
                with dissolve
                mound "I yearn for what I have always yearned for. Our awakening. Other desires shrink in the light of knowing you and knowing me.\n"
                show mound neutral onlayer front
                #with dissolve
            else:
                voice "audio/voices/mound/mound3/23.flac"
                show mound shift talk onlayer front
                with dissolve
                mound "I yearn for what I have always yearned for. My awakening. Other desires shrink in the light of self-knowledge.\n"
                show mound shift onlayer front
                #with dissolve
            jump quiet_3_menu

        "• (Explore) ''Do you still not care what I bring you next?''" if quiet_3_vessel_want == False and quiet_2_requests:
            $ quiet_3_vessel_want = True
            $ quiet_3_count += 1
            if princess_satisfy >= princess_deny:
                voice "audio/voices/mound/mound3/24.flac"
                show mound shift talk onlayer front
                with dissolve
                mound "I care about your gifts, but I have no preferences to burden you with. Even if I did, I would never dare to tarnish our relationship by assuming myself above you.\n"
                show mound shift onlayer front
                #with dissolve
            else:
                voice "audio/voices/mound/mound3/25.flac"
                show mound pose talk onlayer front
                with dissolve
                mound "I care about your gifts, but I have no preferences. You have your responsibilities, and I have mine.\n"
                show mound pose onlayer front
                #with dissolve
            jump quiet_3_menu

        "• (Explore) ''What do you want me to bring you next time?''" if quiet_3_vessel_want == False and quiet_2_requests == False:
            $ quiet_3_vessel_want = True
            $ quiet_3_count += 1
            voice "audio/voices/mound/mound3/26.flac"
            show mound shift talk onlayer front
            with dissolve
            mound "Gifts aren't what someone tells you to bring them.\n"
            if princess_satisfy > princess_deny:
                voice "audio/voices/mound/mound3/27.flac"
                show mound neutral talk onlayer front
                with dissolve
                mound "My joy is in seeing what you choose. There are no wrong answers, and every perspective illuminates my shadows and tells me new secrets.\n"
            else:
                voice "audio/voices/mound/mound2/23.flac"
                show mound neutral talk onlayer front
                with dissolve
                mound "Do not worry. There are no wrong answers, and every perspective illuminates my shadows and shares new secrets.\n"
            show mound neutral onlayer front
            #with dissolve
            jump quiet_3_menu

        "• (Explore) ''So you don't have any preferences on how you'd like to change or grow?''" if quiet_3_vessel_want and quiet_3_no_preferences == False:
            $ quiet_3_no_preferences = True
            $ quiet_3_count += 1
            voice "audio/voices/mound/mound3/28.flac"
            show mound pose talk onlayer front
            with dissolve
            mound "The tides do not dictate where they are pulled. A river does not dictate its outlets.\n"
            if princess_satisfy >= princess_deny:
                voice "audio/voices/mound/mound3/29.flac"
                show mound shift talk onlayer front
                with dissolve
                mound "My gift to you is to let you choose your path, and my task is to treasure the gifts you bring me.\n"
            else:
                voice "audio/voices/mound/mound3/30.flac"
                show mound shift talk onlayer front
                with dissolve
                mound "My gift to you is to let you choose your path, and my task is to contemplate the gifts you bring me.\n"
            show mound shift onlayer front
            #with dissolve
            jump quiet_3_menu

        "• (Explore) ''How many more vessels do I need to bring you?''" if quiet_3_how_many == False:
            $ quiet_3_how_many = True
            $ quiet_3_count += 1
            voice "audio/voices/mound/mound3/31a.flac"
            show mound neutral talk onlayer front
            with dissolve
            mound "We will know when we near our destination.\n"
            show mound neutral onlayer front
            #with dissolve
            jump quiet_3_menu

        "• (Explore) ''I don't want to go back anymore. I just want to stay here. Forever if I have to.''" if quiet1_refuse_explore == False:
            $ quiet1_refuse_explore = True
            $ quiet_3_count += 1
            voice "audio/voices/mound/mound3/32.flac"
            show mound neutral talk onlayer front
            with dissolve
            mound "If you need time, then I will wait with you.\n"
            show mound neutral onlayer front
            #with dissolve
            menu:
                extend ""

                "• [[Continue to wait. Forever.]":
                    $ quiet2_stay_forever_attempt = True
                    voice "audio/voices/mound/mound3/33.flac"
                    show mound shift talk onlayer front
                    with dissolve
                    mound "You are as I am now, and forever is a long time to remain undone. I am not you, but I know that I would return before forever was finished.\n"
                    jump wait_forever_join


                "• [[There is no waiting forever.]":
                    jump quiet_3_menu

        "• ''I'm ready to go back.''":
            voice "audio/voices/mound/mound3/34.flac"
            show mound neutral talk onlayer front
            with dissolve
            mound "I will be here when it is time for us to meet again.\n{w=3.5}{nw}"
            show screen disableclick(0.5)
            play audio "audio/final/Assorted_ForcefullyBreakingGlass_3.flac"
            stop music
            stop sound
            stop secondary
            hide farback onlayer farback
            hide mound onlayer front
            hide hands onlayer front
            hide bg onlayer farback
            show bg black onlayer farback at Position(ypos=1125)
            truth "Everything goes dark, and you die.\n"
            hide bg onlayer farback
            with fade
            jump restart_start

        "•  [[Attack the entity.]" if quiet_attack == False:
            $ quiet_attack = True
            play audio "audio/final/Assorted_WingsFlap_2.flac"
            truth "Your will cuts across the entity in front of you, but nothing happens.\n"
            voice "audio/voices/mound/mound1/79.flac"
            mound "My roots burrow in an ocean beyond your sight. We cannot harm each other as we are now.\n"
            jump quiet_3_menu

        "•  [[Destroy your body.]" if quiet_suicide_attempt == False:
            $ quiet_suicide_attempt = True
            play audio "audio/final/Adversary_HandThroughChest_1.flac"
            truth "You raise your will to end your life. But as it buries into the space your body should be, you feel nothing at all.\n"
            truth "One of the many hands in front of you reaches forward, and gently touches the side of your face.\n"
            voice "audio/voices/mound/mound1/80.flac"
            mound "There's nowhere for you to be but here.\n"
            jump quiet_3_menu

return
