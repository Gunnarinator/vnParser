label quiet_2_start:
    if quiet1_direct and loops_destroyed == 1:
        voice "audio/voices/mound/mound2/1.flac"
        show mound neutral talk onlayer front
        with dissolve
        mound "When I found you in The Long Quiet alone, I was terrified. What if you had decided to let me wither?\n"
    elif quiet1_direct and loops_destroyed == 2:
        voice "audio/voices/mound/mound2/2.flac"
        show mound neutral talk onlayer front
        with dissolve
        mound "I am sorry I said that I hated you. I do not hate you. When I found you in The Long Quiet alone, I was terrified. When I found you in The Long Quiet again alone, I was hurt. I thought you had decided to leave me here to wither.\n"
    elif quiet1_direct and loops_destroyed == 3:
        voice "audio/voices/mound/mound2/3.flac"
        show mound neutral talk onlayer front
        with dissolve
        mound "You have come back to me, and you have finally brought another fragile vessel. I hope our voiceless encounters in The Long Quiet have not cracked the foundations of our relationship. We are each other's salvation. There is no one to save us but us.\n"
    elif quiet1_direct and loops_destroyed == 4:
        voice "audio/voices/mound/mound2/4.flac"
        show mound neutral talk onlayer front
        with dissolve
        mound "You have come back to me with another fragile vessel. I did not think you would.\n"
    elif quiet1_direct and loops_destroyed == 5:
        voice "audio/voices/mound/mound2/5.flac"
        show mound neutral talk onlayer front
        with dissolve
        mound "You are back. It is good that you listened to my warning. Choice has been stripped from you. There are very few paths left for you to walk, but there is still a tarnished thread leading to our freedom.\n"
    #else:
    #    voice "audio/voices/mound/mound2/6.flac"
    #    mound "You have found your way back to The Long Quiet, and you have brought with you another fragile vessel. I knew you would return to me.\n"
    if loops_destroyed >= 1 and quiet1_direct:
        voice "audio/voices/mound/mound2/7.flac"
        show mound pose talk onlayer front
        with dissolve
        mound "But your commitment now is final. Your ability to walk the path of mutual annihilation is vanished with your return. If you still wish to obliterate me, it will have to wait until I am complete.\n"

    voice "audio/voices/mound/mound2/8.flac"
    show mound shift talk onlayer front
    with dissolve
    mound "Flickering lights in empty cityscapes become pockets of vitality and movement. I am more than I was before.\n"
    voice "audio/voices/mound/mound2/9.flac"
    show mound neutral talk onlayer front
    with dissolve
    mound "Whenever you are ready, I will wipe your slate clean once again.\n"
    #mound "Flickering lights in empty cityscapes become pockets of vitality and movement. I am more than I was before. Whenever you are ready, I will wipe your slate clean once again.\n"
    show mound neutral onlayer front
    #with dissolve

label quiet_2_menu:
    default quiet_2_same = False
    default quiet_2_how_feel = False
    default quiet_2_want = False
    default quiet_2_threaten = False
    default quiet_2_restrictions = False
    default quiet_2_nice = False
    default quiet_2_requests = False
    default quiet_2_vessel_thoughts = False
    default quiet_2_requests_follow = False
    default quiet_2_her_feelings = False
    default quiet_2_how_many = False
    default quiet_2_count = 0
    menu:
        extend ""

        "{i}• (Explore) ''Everything you say feels like a riddle. Can you give me a single straight answer?''{/i}" if mound_pretention_explore == False and quiet_2_count > 0:
            jump mound_2_straight_answer

        "• (Explore) ''Are you the same being as you were before? How much have you changed?''" if quiet_2_same == False:
            $ quiet_2_same = True
            $ quiet_2_count += 1
            voice "audio/voices/mound/mound2/10.flac"
            show mound shift talk onlayer front
            with dissolve
            mound "Is a child the same as an infant? I am an unbroken pattern, but every vessel gifts fresh perspectives and carves new avenues of expression. 'I' am different, but I am the same.\n"
            show mound shift onlayer front
            #with dissolve
            jump quiet_2_menu

        "• (Explore) ''What does it feel like to change like this?''" if quiet_2_how_feel == False:
            $ quiet_2_how_feel = True
            $ quiet_2_count += 1
            voice "audio/voices/mound/mound2/11.flac"
            show mound shift talk onlayer front
            with dissolve
            mound "Eyes close in reflection.\n"
            voice "audio/voices/mound/mound2/12.flac"
            show mound pose talk onlayer front
            with dissolve
            mound "Perspectives meld together, and the breadth of my experience stretches to new corners. There are contradictions, conflicts in my nature. And there are familiarities that bind everything together.\n"
            voice "audio/voices/mound/mound2/13a.flac"
            show mound neutral talk onlayer front
            with dissolve
            mound "It feels correct. This is what I need to be. This is the only path forward.\n"
            show mound neutral onlayer front
            #with dissolve
            jump quiet_2_menu

        "• (Explore) ''When this is all done, do you know what you want to do?''" if quiet_2_want == False:
            $ quiet_2_want = True
            $ quiet_2_count += 1
            voice "audio/voices/mound/mound2/14.flac"
            show mound shift talk onlayer front
            with dissolve
            mound "With every gift you bring me, I excavate the alleys of what I am meant to be, and every exploration yields new and complicated truths. What I will be is different than what I am and what I am is different from what I was.\n"
            voice "audio/voices/mound/mound2/15.flac"
            show mound pose talk onlayer front
            with dissolve
            mound "I cannot tell you what desires I will hold when I have changed.\n"
            if princess_satisfy >= princess_deny:
                voice "audio/voices/mound/mound2/16.flac"
                show mound neutral talk onlayer front
                with dissolve
                mound "But in this moment, all I want is to know myself and to know you.\n"
            else:
                voice "audio/voices/mound/mound2/17.flac"
                show mound neutral talk onlayer front
                with dissolve
                mound "But in this moment, all I want is to know myself.\n"
            show mound neutral onlayer front
            #with dissolve
            jump quiet_2_menu

        "• (Explore) ''You know that at the end of this—once you're finished—I'm going to kill you, right?''" if quiet_2_threaten == False:
            $ quiet_threaten_count += 1
            $ quiet_2_threaten = True
            $ quiet_2_count += 1
            voice "audio/voices/mound/mound2/18.flac"
            show mound neutral talk onlayer front
            with dissolve
            mound "There is still much to be seen. Neither of us know the depths of our being. Perhaps at the end of this, I will be the one to kill you. Or perhaps we will leave this place together, and find new horizons to discover.\n"
            show mound neutral onlayer front
            with dissolve
            jump quiet_2_menu

        "• (Explore) ''When I go back, it's as if an invisible wall closes around me. Why can I not do the same things I've done before?''" if quiet_2_restrictions == False:
            $ quiet_2_restrictions = True
            $ quiet_2_count += 1
            voice "audio/voices/mound/mound2/19.flac"
            show mound shift talk onlayer front
            with dissolve
            mound "Those paths lead to worlds you've already seen, and to perspectives I have already made my own. They are useless to us now. Inaccessible. The only paths of value are those that are yet untread.\n"
            show mound shift onlayer front
            #with dissolve
            jump quiet_2_menu

        "• (Explore) ''You have been kinder to me than anyone else I've met. Thank you.''" if quiet_2_nice == False:
            jump mound_2_nice_join

        "• (Explore) ''You have been kinder to me than anyone else I've met. Why?''" if quiet_2_nice == False:
            label mound_2_nice_join:
                $ quiet_2_count += 1
                $ quiet_2_nice = True
                voice "audio/voices/mound/mound2/20.flac"
                show mound pose talk onlayer front
                with dissolve
                mound "Why wouldn't I be kind to you? You are the only thing I know that isn't me.\n"
                show mound pose onlayer front
                #with dissolve
                jump quiet_2_menu

        "• (Explore) ''What do you want me to bring you next time?''" if quiet_2_requests == False:
            $ quiet_2_requests = True
            $ quiet_2_count += 1
            voice "audio/voices/mound/mound2/21.flac"
            show mound pose talk onlayer front
            with dissolve
            mound "Gifts aren't what someone tells you to bring them.\n"
            if princess_satisfy > princess_deny:
                voice "audio/voices/mound/mound2/22.flac"
                show mound shift talk onlayer front
                with dissolve
                mound "My joy is in seeing what you choose. There are no wrong answers, and every perspective illuminates my shadows and shares new secrets.\n"
                #show mound shift onlayer front
                with dissolve
            else:
                voice "audio/voices/mound/mound2/23.flac"
                show mound neutral talk onlayer front
                with dissolve
                mound "Do not worry. There are no wrong answers, and every perspective illuminates my shadows and shares new secrets.\n"
                show mound neutral onlayer front
                #with dissolve
            jump quiet_2_menu

        "• (Explore) ''Do you have any thoughts on this vessel?''" if quiet_2_vessel_thoughts == False:
            $ quiet_2_vessel_thoughts = True
            jump quiet_vessels

        "• (Explore) ''So you don't have any preferences on how you'd like to change or grow?''" if quiet_2_requests and quiet_2_requests_follow == False:
            $ quiet_2_requests_follow = True
            $ quiet_2_count += 1
            voice "audio/voices/mound/mound2/24.flac"
            show mound pose talk onlayer front
            with dissolve
            mound "My preference is for you to show me what you would like me to see. I cannot know the ways I wish to grow, for I have yet to feel them. It is you who guides me down the thin trail of perspective and memory.\n"
            show mound pose onlayer front
            #with dissolve
            jump quiet_2_menu

        "• (Explore) ''I don't want to hurt you, but the more times I go back, the worse I fear things will be.''" if quiet_2_her_feelings == False:
            $ quiet_2_her_feelings = True
            jump quiet_2_feelings_join

        "• (Explore) ''What do you feel about me? These vessels I've been bringing you, I've hurt them.''" if quiet_2_her_feelings == False:
            $ quiet_2_her_feelings = True
            label quiet_2_feelings_join:
                $ quiet_2_count += 1
                if princess_satisfy > princess_deny:
                    if princess_kept > princess_free:
                        voice "audio/voices/mound/mound2/25.flac"
                        show mound shift talk onlayer front
                        with dissolve
                        mound "The vessels are shaped by memories of you, but they are drawn to the edge of The Long Quiet. To them you are a gate to something more. But they are only thoughts and perspectives. They are not me.\n" id quiet_2_feelings_join_c5641cbc
                    else:
                        voice "audio/voices/mound/mound2/26.flac"
                        show mound pose talk onlayer front
                        with dissolve
                        mound "The vessels are shaped by memories of you, but their impulses are drawn to the edge of The Long Quiet. To them you are a gate to something more, and any hurt you've caused them is understood as a fair price for freedom. But they are only thoughts and perspectives. They are not me.\n"
                elif princess_deny > princess_satisfy:
                    voice "audio/voices/mound/mound2/27.flac"
                    show mound neutral talk onlayer front
                    with dissolve
                    mound "There is a hurt that dwells in them, but they are not me. They are thoughts and perspectives. They are feelings that inform my being.\n"
                else:
                    voice "audio/voices/mound/mound2/28.flac"
                    show mound neutral talk onlayer front
                    with dissolve
                    mound "The vessels are a weave of emotion at odds with themselves, but they are only perspectives. They are not me.\n"
                voice "audio/voices/mound/mound2/29.flac"
                show mound pose talk onlayer front
                with dissolve
                mound "The wounds they've suffered carve texture around my heart. Without them, I would be as I was before.\n"
                if princess_satisfy >= princess_deny:
                    voice "audio/voices/mound/mound2/30.flac"
                    show mound neutral talk onlayer front
                    with dissolve
                    mound "I would be alone and without sensation. I could not feel the joy of having you by my side, for I would not know your absence.\n"
                else:
                    show mound neutral talk onlayer front
                    with dissolve
                    voice "audio/voices/mound/mound2/31a.flac"
                    mound "I cannot be as I was before. There are new spaces that I must fill.\n"
                show mound neutral onlayer front
                #with dissolve
                jump quiet_2_menu

        "• (Explore) ''How many more vessels do I need to bring you?''" if quiet_2_how_many == False:
            $ quiet_2_how_many = True
            $ quiet_2_count += 1
            if princess_satisfy > princess_deny:
                voice "audio/voices/mound/mound2/32.flac"
                show mound shift talk onlayer front
                with dissolve
                mound "If I am to be an ocean, you have nurtured me into a pond. My waters are shallow and murky, and I yearn for more perspective.\n"
                voice "audio/voices/mound/mound2/33.flac"
                show mound neutral talk onlayer front
                with dissolve
                mound "You will have your rest in due time, and I am sorry for the burdens I place on you.\n"
                show mound neutral onlayer front
                #with dissolve
            else:
                voice "audio/voices/mound/mound2/34.flac"
                show mound shift talk onlayer front
                with dissolve
                mound "If I am to be an ocean, you have given me enough to build a pond. My waters are shallow and murky, and I yearn for more perspective.\n"
                if princess_kept > princess_free:
                    voice "audio/voices/mound/mound2/35.flac"
                    show mound pose talk onlayer front
                    with dissolve
                    mound "I will transcend in due time, and there is no way forward but to contribute to my awakening.\n"
                    show mound pose onlayer front
                    #with dissolve
                else:
                    voice "audio/voices/mound/mound2/36.flac"
                    show mound neutral talk onlayer front
                    with dissolve
                    mound "The task of finding my vessels is your burden to carry.\n"
                    show mound neutral onlayer front
                    #with dissolve
            jump quiet_2_menu


        "• (Explore) ''And what if I don't want to bring you any more vessels? What if I just wait here forever?''" if quiet1_refuse_explore == False:
            $ quiet1_refuse_explore = True
            $ quiet_2_count += 1
            voice "audio/voices/mound/mound2/37.flac"
            show mound neutral talk onlayer front
            with dissolve
            mound "Then we will remain here as we are now. Barely finished, damp, cavernous.\n"
            show mound neutral onlayer front
            #with dissolve
            menu:
                extend ""

                "• [[Wait.]" if quiet2_stay_forever_attempt == False:
                    default quiet2_stay_forever_attempt = False
                    $ quiet2_stay_forever_attempt = True
                    voice "audio/voices/mound/mound2/38.flac"
                    show mound shift talk onlayer front
                    with dissolve
                    mound "If you need time, then I'll wait with you.\n"
                    show mound shift onlayer front
                    #with dissolve
                    menu:

                        "• [[Wait forever.]":
                            $ quiet2_stay_forever_attempt = True
                            voice "audio/voices/mound/mound1/66.flac"
                            show mound neutral talk onlayer front
                            with dissolve
                            mound "You are as I am now, and forever is a long time to remain undone.\n"
                            voice "audio/voices/mound/mound1/67a.flac"
                            show mound pose talk onlayer front
                            with dissolve
                            mound "I am not you, but I know that I would return before forever was finished.\n"
                            jump wait_forever_join


                        "• [[You have no need to wait.]":
                            jump quiet_2_menu

                "• [[You have no need to wait.]":
                    jump quiet_2_menu

        "{i}• (Explore) ''Enough with all of this pretension. You're not actually saying anything.''{/i}" if mound_pretention_explore == False and quiet_2_count > 0:
            label mound_2_straight_answer:
                $ mound_pretention_explore = True
                voice "audio/_pristine/voice/_climax/mound_interstitial/1.flac"
                mound "I'm sorry. Words are... difficult for me. They never fully weave what I wish to say. If you do not like my answers, then you need not ask me questions.\n"
                voice "audio/_pristine/voice/_climax/mound_interstitial/2a.flac"
                mound "The vessels you choose to bring me carry far more meaning than anything words could say in the spaces between.\n"
                jump quiet_2_menu

        "• ''I'm ready to go back.''":
            if princess_satisfy > princess_deny:
                voice "audio/voices/mound/mound2/39.flac"
                show mound shift talk onlayer front
                with dissolve
                mound "I will long for your return. But it will give me time to reflect on what I am.\n"

            else:
                voice "audio/voices/mound/mound2/40.flac"
                show mound pose talk onlayer front
                with dissolve
                mound "I await your return, but it will give me time to reflect on what I am.\n" id mound_2_straight_answer_c15a722d
            voice "audio/voices/mound/mound2/41a.flac"
            show mound neutral talk onlayer front
            with dissolve
            mound "We will meet again.\n{w=1.15}{nw}"
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
            # restart

        "•  [[Attack the entity.]" if quiet_attack == False:
            $ quiet2_mound_attacked = True
            $ quiet_attack = True
            play audio "audio/final/Assorted_WingsFlap_2.flac"
            truth "Your will cuts across the entity in front of you, but nothing happens.\n"
            voice "audio/voices/mound/mound1/79.flac"
            show mound neutral talk onlayer front
            with dissolve
            mound "My roots burrow in an ocean beyond your sight. We cannot harm each other as we are now.\n"
            show mound neutral onlayer front
            #with dissolve
            jump quiet_2_menu

        "•  [[Destroy your body.]" if quiet_suicide_attempt == False:
            $ quiet_suicide_attempt = True
            $ quiet2_suicide = True
            play audio "audio/final/Adversary_HandThroughChest_1.flac"
            truth "You raise your will to end your life. But as it buries into the space your body should be, you feel nothing at all.\n"
            truth "One of the many hands in front of you reaches forward, and gently touches the side of your face.\n"
            voice "audio/voices/mound/mound1/80.flac"
            show mound neutral talk onlayer front
            with dissolve
            mound "There's nowhere for you to be but here.\n"
            show mound neutral onlayer front
            #with dissolve
            jump quiet_2_menu
return
