label quiet_4_start:
    default quiet_4_ask = False
    if princess_free > princess_kept:
        $ quiet_4_ask = True
        voice "audio/voices/mound/mound4/1.flac"
        show mound pose talk onlayer front
        with dissolve
        mound "There's a world beyond the endless walls of The Long Quiet. We're supposed to be there.\n"
        voice "audio/voices/mound/mound4/2.flac"
        show mound neutral talk onlayer front
        with dissolve
        mound "Do you know what we'll find out there?\n"
        show mound neutral onlayer front
        #with dissolve
    else:
        voice "audio/voices/mound/mound4/3.flac"
        show mound shift talk onlayer front
        with dissolve
        mound "There's a world beyond the endless walls of The Long Quiet. I am curious to see what it means for us to know it.\n"
        show mound neutral onlayer front
        #with dissolve

label quiet_4_menu:
    default quiet_4_menu_count = 0
    default quiet_4_rhetorical = False
    default quiet_4_outside_explain = False
    default quiet_4_solipsism = False
    default quiet_4_vessel_thoughts = False
    default quiet_4_awaken = False
    default quiet_4_narrator = False
    default quiet_4_last_trip = False
    default quiet_4_requests = False
    default quiet_4_threaten = True
    default quiet_4_refuse = False
    default quiet_4_count = 0
    menu:
        extend ""


        "{i}• (Explore) ''Everything you say feels like a riddle. Can you give me a single straight answer?''{/i}" if mound_pretention_explore == False and quiet_4_count > 0:
            label mound_4_straight_answer:
                $ mound_pretention_explore = True
                voice "audio/_pristine/voice/_climax/mound_interstitial/1.flac"
                mound "I'm sorry. Words are... difficult for me. They never fully weave what I wish to say. If you do not like my answers, then you need not ask me questions.\n"
                voice "audio/_pristine/voice/_climax/mound_interstitial/2a.flac"
                mound "The vessels you choose to bring me carry far more meaning than anything words could say in the spaces between.\n"
                jump quiet_4_menu

        "• (Explore) ''Do you think there are people out there?''" if quiet_4_ask == False and quiet_4_outside_explain == False:
            $ quiet_4_count += 1
            $ quiet_4_menu_count += 1
            $ quiet_4_outside_explain = True
            if princess_satisfy > princess_deny:
                voice "audio/voices/mound/mound4/5a.flac"
                show mound neutral talk onlayer front
                with dissolve
                mound "It doesn't matter if there are. People are too small for us. You and I are the only things that interest me.\n"
                show mound neutral onlayer front
                #with dissolve
            else:
                show mound pose talk onlayer front
                with dissolve
                voice "audio/voices/mound/mound4/6a.flac"
                mound "It doesn't matter if there are. People are frail and impermanent. You and I are the only things that interest me.\n"
                show mound pose onlayer front
                #with dissolve
            jump quiet_4_menu

        "• (Explore) ''Is that a rhetorical question? Do you know? Do you want to tell me?''" if quiet_4_ask and quiet_4_rhetorical == False and quiet_4_menu_count == 0:
            $ quiet_4_menu_count += 1
            $ quiet_4_count += 1
            $ quiet_4_rhetorical = True
            voice "audio/voices/mound/mound4/7b.flac"
            show mound shift talk onlayer front
            with dissolve
            mound "Rhetorical. I am not rhetorical. I have only known these spaces, and I have known flickers of the lives you've brought me. Short and violent and full of passion. But all of those flickers end where The Long Quiet begins.\n"
            voice "audio/voices/mound/mound4/8b.flac"
            show mound neutral talk onlayer front
            with dissolve
            mound "I'm asking you because I cannot know your mind. Do you know what we'll find out there?\n"
            show mound neutral onlayer front
            #with dissolve
            jump quiet_4_menu

        "• (Explore) ''There's trees, and stars. And there are people, I think. At least there are supposed to be people.''" if quiet_4_ask and quiet_4_outside_explain == False:
            $ quiet_4_menu_count += 1
            $ quiet_4_count += 1
            $ quiet_4_outside_explain = True
            voice "audio/voices/mound/mound4/9.flac"
            show mound shift talk onlayer front
            with dissolve
            mound "There is a warmth and sadness in me at the thought of people. Fresh tears on a winter's day. They are not like us. They do not last.\n"
            show mound shift onlayer front
            #with dissolve
            jump quiet_4_menu

        "• (Explore) ''Do you think that anything is real out there? Do you think that we're real?''" if quiet_4_solipsism == False:
            $ quiet_4_solipsism = True
            $ quiet_4_menu_count += 1
            $ quiet_4_count += 1
            voice "audio/voices/mound/mound4/10b.flac"
            show mound pose talk onlayer front
            with dissolve
            mound "We are real. 'Nothing' is an idea that dwells in the absence of 'something.' But 'nothing' cannot exist on its own. And because of that, 'nothing' can't exist.\n"
            show mound pose onlayer front
            #with dissolve
            jump quiet_4_menu

        "• (Explore) ''Do you have thoughts on this vessel?''" if quiet_4_vessel_thoughts == False:
            $ quiet_4_vessel_thoughts = True
            $ quiet_4_menu_count += 1
            $ quiet_4_count += 1
            jump quiet_vessels

        "• (Explore) ''Do you know what's going to happen when you awaken?''" if quiet_4_awaken == False:
            $ quiet_4_awaken = True
            $ quiet_4_menu_count += 1
            $ quiet_4_count += 1
            if princess_satisfy > princess_deny:
                voice "audio/voices/mound/mound4/11.flac"
                show mound neutral talk onlayer front
                with dissolve
                mound "If I did, I would already be awake.\n"
            else:
                voice "audio/voices/mound/mound4/11a.flac"
                show mound neutral talk onlayer front
                with dissolve
                mound "No. The point of awakening is to find out.\n"
            show mound neutral onlayer front
            #with dissolve
            jump quiet_4_menu

        "• (Explore) ''When you send me back, I'm not alone. There are voices that speak to me. Some of them are me, but one of them is something else. I call him The Narrator, and he wants me to kill you. Do you have a Narrator? Have the vessels had one?''" if quiet_4_narrator == False:
            $ quiet_4_narrator = True
            $ quiet_4_menu_count += 1
            $ quiet_4_count += 1
            if wild_fed or wraith_fed or spectre_fed:
                voice "audio/voices/mound/mound4/12.flac"
                show mound pose talk onlayer front
                with dissolve
                mound "I know him through the memories of my vessels. But they have nothing like him on their own. Do you think he lives in the spaces beyond?\n"
                show mound pose onlayer front
                #with dissolve
            elif quiet_4_ask:
                voice "audio/voices/mound/mound4/13.flac"
                show mound neutral talk onlayer front
                with dissolve
                mound "No. Their thoughts are quiet. Do you think your Narrator lives in the spaces beyond?\n"
                show mound neutral onlayer front
                #with dissolve
            else:
                voice "audio/voices/mound/mound4/14.flac"
                show mound shift talk onlayer front
                with dissolve
                mound "No. Their minds are empty. Existent, but constantly shifting into something new. Do you think your Narrator lives in the spaces beyond?\n"
                show mound shift onlayer front
                #with dissolve
            menu:
                extend ""

                "• ''He does. I don't know why, but I know this for a fact.''":
                    voice "audio/voices/mound/mound4/15a.flac"
                    show mound neutral talk onlayer front
                    with dissolve
                    mound "I am on the cusp of my awakening. Perhaps you are on the cusp of yours.\n"
                    show mound neutral onlayer front
                    #with dissolve

                "• ''He does. I don't know what I'm going to do when I find him.''":
                    voice "audio/voices/mound/mound4/16.flac"
                    show mound shift talk onlayer front
                    with dissolve
                    mound "There's no need for you to know what you are going to do before you do it. If you find him, remember that I'll be waiting for you on the other side.\n"
                    show mound shift onlayer front
                    #with dissolve
                    #voice "audio/voices/mound/mound4/16a.flac"
                    #mound "If you find him, remember that I will be waiting for you on the other side.\n"

                "• ''He does. And when I find him, you and I are finally going to have answers.''":
                    voice "audio/voices/mound/mound4/17.flac"
                    show mound neutral talk onlayer front
                    with dissolve
                    mound "Do not look to one who fears me for your truth. The only answers worth knowing are those we can find within ourselves.\n"
                    show mound neutral onlayer front
                    #with dissolve

                "• ''He does. And when I find him, I'm going to kill him.''":
                    if quiet_4_ask:
                        voice "audio/voices/mound/mound4/18.flac"
                        show mound pose talk onlayer front
                        with dissolve
                        mound "If he drives you towards my destruction, then he is steeped in delusion, for he does not know me. Just as I hold compassion for you, and you hold compassion for me, you can hold compassion for those who have wronged you.\n"
                        show mound pose onlayer front
                        #with dissolve
                    else:
                        voice "audio/voices/mound/mound4/19a.flac"
                        show mound neutral talk onlayer front
                        with dissolve
                        mound "If he is anything other than us, he isn't worth the effort to destroy.\n"
                        show mound neutral onlayer front
                        #with dissolve

                "•  He does. But you're going to keep that to yourself.":
                    voice "audio/voices/mound/mound4/20a.flac"
                    show mound neutral talk onlayer front
                    with dissolve
                    mound "It's nice to be with someone whose thoughts I can never know as mine.\n"
                    show mound neutral onlayer front
                    #with dissolve

            jump quiet_4_menu

        "• (Explore) ''How many more vessels do I need to bring you?''" if quiet_4_last_trip == False:
            $ quiet_4_last_trip = True
            $ quiet_4_menu_count += 1
            $ quiet_4_count += 1
            voice "audio/voices/mound/mound4/21.flac"
            show mound pose talk onlayer front
            with dissolve
            mound "One. Whatever you bring me next will be enough, and then gravity will pull the others back to me. I will be singular. A final multitude.\n"
            show mound pose onlayer front
            #with dissolve
            jump quiet_4_menu

        "• (Explore) ''If this is the last time, is there anything you would like me to bring you?''" if quiet_4_last_trip and quiet_4_requests == False:
            $ quiet_4_count += 1
            $ quiet_4_menu_count += 1
            $ quiet_4_requests = True
            voice "audio/voices/mound/mound4/22a.flac"
            show mound neutral talk onlayer front
            with dissolve
            mound "These gifts are a conversation, and each one shows me the contours of your heart. The only thing I want to see is what you choose for me when the thread is fully drawn.\n"
            show mound neutral onlayer front
            #with dissolve
            jump quiet_4_menu

        "• (Explore) ''You know we're going to fight when this is over. Do you really want me to bring you the last vessel?''" if quiet_4_last_trip and quiet_4_threaten == False and quiet_threaten_count >= 1:
            $ quiet_4_count += 1
            $ quiet_4_threaten = True
            $ quiet_4_menu_count += 1
            $ quiet_threaten_count = True
            if princess_satisfy >= princess_deny:
                voice "audio/voices/mound/mound4/23.flac"
                show mound shift talk onlayer front
                with dissolve
                mound "We may fight, and we may not. But not all fights end in destruction, just as not all conversations end in peace.\n"
                voice "audio/voices/mound/mound4/24.flac"
                show mound neutral talk onlayer front
                with dissolve
                mound "Even if you destroy me, it will have been worth it to finally know what I am and to have had the chance to know you.\n"
                show mound neutral onlayer front
                #with dissolve
            else:
                voice "audio/voices/mound/mound4/25.flac"
                show mound pose talk onlayer front
                with dissolve
                mound "Conflict is my nature. There is nothing I want more than to finally perceive the shape of myself from every angle, and to turn that shape on you.\n"
                voice "audio/voices/mound/mound4/26.flac"
                show mound shift talk onlayer front
                with dissolve
                mound "But not all fights end in destruction, just as not all conversations end in peace.\n"
                show mound shift onlayer front
                #with dissolve
            jump quiet_4_menu

        "• (Explore) ''If this is the last stage before your completion, then I'm not going back. I'm just going to stay here.''" if quiet1_refuse_explore and quiet_4_refuse == False and quiet_4_last_trip:
            $ quiet_4_count += 1
            $ quiet_4_refuse = True
            $ quiet_4_menu_count += 1
            voice "audio/voices/mound/mound4/27.flac"
            show mound shift talk onlayer front
            with dissolve
            mound "You've already tried waiting, but I understand if you need more time. I'll wait with you.\n"
            show mound shift onlayer front
            #with dissolve
            menu:

                extend ""

                "• [[Wait.]":
                    voice "audio/voices/mound/mound4/28.flac"
                    show mound neutral talk onlayer front
                    with dissolve
                    mound "I will see you when you return.\n"
                    show mound neutral onlayer front
                    #with dissolve
                    jump wait_forever_join


                "• [[There is no waiting forever.]":
                    jump quiet_4_menu

            jump quiet_4_menu

        "• (Explore) ''If this is the last stage before your completion, then I'm not going back. I'm just going to stay here. Forever if I have to.''" if quiet_4_refuse == False and quiet1_refuse_explore == False:
            $ quiet_4_count += 1
            $ quiet_4_menu_count += 1
            $ quiet_4_refuse = True
            label quiet_4_wait_join:
                voice "audio/voices/mound/mound4/29.flac"
                show mound neutral talk onlayer front
                with dissolve
                mound "You have already chosen to walk along this path, and we both know you will see it to completion. But if you need more time, then I will wait with you.\n"
                show mound neutral onlayer front
                #with dissolve
                menu:

                    extend ""

                    "• [[Wait forever.]":
                        voice "audio/voices/mound/mound4/30.flac"
                        show mound shift talk onlayer front
                        with dissolve
                        mound "You are as I am now, and forever is a long time to remain undone. I am not you, but I know that I would return before forever was finished.\n"
                        show mound shift onlayer front
                        #with dissolve
                        jump wait_forever_join


                    "• [[There is no waiting forever.]":
                        jump quiet_4_menu

                jump quiet_4_menu

        "• ''I'm ready to go back.''":
            voice "audio/voices/mound/mound4/31.flac"
            show mound pose talk onlayer front
            with dissolve
            mound "The next time I see you, each of us will finally know what we are.\n"
            voice "audio/voices/mound/mound4/32.flac"
            mound "I will be here. Waiting for you.\n"
            show mound neutral talk onlayer front
            with dissolve
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
            voice "audio/voices/mound/mound4/33.flac"
            show mound neutral talk onlayer front
            with dissolve
            mound "My roots burrow in an ocean beyond your sight. We cannot harm each other as we are now.\n"
            show mound neutral onlayer front
            #with dissolve
            jump quiet_4_menu

        "•  [[Destroy your body.]" if quiet_suicide_attempt == False:
            $ quiet_suicide_attempt = True
            play audio "audio/final/Adversary_HandThroughChest_1.flac"
            truth "You raise your will to end your life. But as it buries into the space your body should be, you feel nothing at all.\n"
            truth "One of the many hands in front of you reaches forward, and gently plucks the instrument from your hands.\n"
            voice "audio/voices/mound/mound1/80.flac"
            show mound shift talk onlayer front
            with dissolve
            mound "There's nowhere for you to be but here.\n"
            show mound shift onlayer front
            #with dissolve
            jump quiet_4_menu

return
