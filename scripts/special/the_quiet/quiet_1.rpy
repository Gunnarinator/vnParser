label quiet_1_start:
    if current_princess == "stranger":
        $ princess_satisfy += 1
    if loops_destroyed > 0:
        truth "You recognize the presence inhabiting the shell. It is the entity that dwells in the spaces between.\n"
        voice "audio/voices/mound/mound1/1a.flac"
        show hands mound onlayer front at Position(ypos=1125)
        show mound talk onlayer front at Position(ypos=1125)
        with dissolve
        mound "Something returns to the Long Quiet. It has surrendered its path of annihilation and brings me the gift of a fragile vessel.\n"
    else:
        $ quiet1_direct = True
        voice "audio/voices/mound/mound1/2a.flac"
        show hands mound onlayer front at Position(ypos=1125)
        show mound neutral talk onlayer front at Position(ypos=1125)
        with dissolve
        mound "Something finds me in the Long Quiet and brings me the gift of a fragile vessel.\n"
    show mound neutral onlayer front
    #truth "She speaks in a soft voice, almost a whisper. You step forward, drawn to her.\n"
    label quiet_1_menu:
        menu:
            extend ""

            "• (Explore) ''You're that thing I met in the space outside of the woods, aren't you? I thought that was a dream.''" if loops_destroyed > 0 and quiet_1_destroyed_explore == False:
                default quiet_1_destroyed_explore = False
                $ quiet_1_destroyed_explore = True
                voice "audio/voices/mound/mound1/53.flac"
                show mound pose talk onlayer front
                with dissolve
                mound "Vague recollections. Empty tunnels without a mouth. I am sorry if I frightened you.\n"
                show mound pose onlayer front
                #with dissolve
                jump quiet_1_menu


            "• (Explore) ''What are you?''" if quiet1_what == False:
                $ quiet1_what = True
                voice "audio/voices/mound/mound1/3a.flac"
                show mound shift talk onlayer front
                with dissolve
                mound "I am solitary lights in an empty city. What are you?\n"
                show mound shift onlayer front
                #with dissolve
                label quiet1_what_menu_join:
                    menu:
                        extend ""

                        "• (Explore) ''Solitary lights? What do you mean?''" if quiet1_lights == False:
                            $ quiet1_lights = True
                            voice "audio/voices/mound/mound1/4.flac"
                            show mound neutral talk onlayer front
                            with dissolve
                            mound "Thoughts without connections. A dim and nascent network. I wish to be more.\n"
                            show mound neutral onlayer front
                            #with dissolve
                            jump quiet1_what_menu_join

                        "• ''What do you think I am?''":
                            voice "audio/voices/mound/mound1/5.flac"
                            show mound pose talk onlayer front
                            with dissolve
                            mound "I think that you are like me.\n"

                        "• ''I don't know what I am.''":
                            voice "audio/voices/mound/mound1/5.flac"
                            show mound pose talk onlayer front
                            with dissolve
                            mound "I think that you are like me.\n"

                        "• ''I'm a person.''":
                            voice "audio/voices/mound/mound1/6b.flac"
                            show mound pose talk onlayer front
                            with dissolve
                            mound "A person. A set of eyes witnessing from one perspective. I think that you are more like me than you are like a person.\n"

                    voice "audio/voices/mound/mound1/7.flac"
                    show mound shift talk onlayer front
                    with dissolve
                    mound "We are oceans reduced to shallow creeks.\n"
                    show mound shift onlayer front
                    #with dissolve
                    jump quiet_1_menu

            "• (Explore) ''The gift of a fragile vessel?''" if quiet1_fragile == False:
                $ quiet1_fragile = True
                voice "audio/voices/mound/mound1/8a.flac"
                show mound pose talk onlayer front
                with dissolve
                mound "Yes. Nerves and fibers to feel the worlds beyond. Perspectives to make my own.\n"
                label quiet_vessels:
                    if current_princess == "adversary":
                        #voice "audio/voices/mound/mound1/9.flac"
                        voice "audio/_pristine/voice/_climax/mound_interstitial/_final/15.flac"
                        show mound shift talk onlayer front
                        with dissolve
                        mound "This one yearns to grow and struggle. Even now I feel a will pushing against mine, not realizing that we are one. She will make for a bold heart.\n"
                        #mound "This one yearns to grow and struggle. Even now I feel a will pushing against mine, not realizing that we are one. She will make for a fierce heart.\n"
                        voice "audio/voices/mound/mound1/10.flac"
                        show mound neutral talk onlayer front
                        with dissolve
                        mound "Do not mourn her. We will provide her with the growth she fought for.\n"
                    elif current_princess == "needle":
                        voice "audio/_pristine/voice/_climax/mound_interstitial/_final/16.flac"
                        show mound shift talk onlayer front
                        with dissolve
                        mound "This one remembers a spark lost in time, and she would stop at nothing to reclaim it. She will make for a burning heart.\n"
                        voice "audio/_pristine/voice/_climax/mound_interstitial/_final/17.flac"
                        show mound neutral talk onlayer front
                        with dissolve
                        mound "Do not mourn her. She has finally remembered what she thought she'd lost.\n"
                    elif current_princess == "dragon" or current_princess == "dragonfused" or current_princess == "dragonhand":
                        voice "audio/_pristine/voice/_climax/mound_interstitial/_final/6.flac"
                        show mound shift talk onlayer front
                        with dissolve
                        mound "This one is perspectives bleeding into one. You know her better than you know yourself. She will make for an empathetic heart.\n"
                        voice "audio/_pristine/voice/_climax/mound_interstitial/_final/7.flac"
                        show mound neutral talk onlayer front
                        with dissolve
                        mound "Do not mourn her, for you would not mourn yourself.\n"
                    elif current_princess == "cage":
                        if cage_end == "free":
                            voice "audio/_pristine/voice/_climax/mound_interstitial/_final/8a.flac"
                            show mound shift talk onlayer front
                            with dissolve
                            mound "This one is a locked door to which you held the key. She will make for an open heart, if you let her.\n"
                            voice "audio/_pristine/voice/_climax/mound_interstitial/_final/9.flac"
                            show mound neutral talk onlayer front
                            with dissolve
                            mound "Do not mourn her. She is no longer bound.\n"
                        else:
                            voice "audio/_pristine/voice/_climax/mound_interstitial/_final/10.flac"
                            show mound shift talk onlayer front
                            with dissolve
                            mound "This one is a body that convinced herself she was only a set of eyes. She will make for a watchful heart.\n"
                            voice "audio/_pristine/voice/_climax/mound_interstitial/_final/11.flac"
                            show mound neutral talk onlayer front
                            with dissolve
                            mound "Do not mourn her. She is now what she wished that she could be.\n"
                    elif current_princess == "happy" or current_princess == "happydry":
                        voice "audio/_pristine/voice/_climax/mound_interstitial/_final/12.flac"
                        show mound shift talk onlayer front
                        with dissolve
                        mound "This one is a songbird in a cage of gilded shadows. She will make for an honest heart.\n"
                        voice "audio/_pristine/voice/_climax/mound_interstitial/_final/13.flac"
                        show mound neutral talk onlayer front
                        with dissolve
                        mound "Do not mourn her. She has finally learned to sing for herself.\n"
                    elif current_princess == "beast":
                        #voice "audio/voices/mound/mound1/11.flac"
                        voice "audio/_pristine/voice/_climax/mound_interstitial/_final/14.flac"
                        show mound shift talk onlayer front
                        with dissolve
                        mound "This one is consumed by instinct. A predator pushing those around her to adapt. She will make for a cunning heart.\n"
                        voice "audio/voices/mound/mound1/12.flac"
                        show mound pose talk onlayer front
                        with dissolve
                        mound "She wishes me to devour you. To make you a part of myself. But she is only a voice.\n"
                        voice "audio/voices/mound/mound1/13.flac"
                        show mound neutral talk onlayer front
                        with dissolve
                        mound "Do not mourn her, for she is part of something greater.\n"
                    elif current_princess == "den":
                        voice "audio/_pristine/voice/_climax/mound_interstitial/_final/23.flac"
                        show mound shift talk onlayer front
                        with dissolve
                        mound "This one is consumed by instinct. A dancer moving to the rhythm of the flesh. She will make for a ravenous heart.\n"
                        if beast_2_end != "free":
                            voice "audio/voices/mound/mound1/12.flac"
                            show mound pose talk onlayer front
                            with dissolve
                            mound "She wishes me to devour you. To make you a part of myself. But she is only a voice.\n"
                        voice "audio/voices/mound/mound1/13.flac"
                        show mound neutral talk onlayer front
                        with dissolve
                        mound "Do not mourn her, for she is part of something greater.\n"
                    elif current_princess == "damsel":
                        voice "audio/voices/mound/mound1/14.flac"
                        show mound shift talk onlayer front
                        with dissolve
                        mound "This one is soft and delicate. You molded her to love you, and she'll make for a gentle heart.\n"
                        voice "audio/voices/mound/mound1/15.flac"
                        show mound neutral talk onlayer front
                        with dissolve
                        mound "Do not mourn her. She has served her purpose.\n"
                    elif current_princess == "dereal":
                        voice "audio/_pristine/voice/_climax/mound_interstitial/_final/21.flac"
                        show mound shift talk onlayer front
                        with dissolve
                        mound "This one is a reflecting pool of desire unfulfilled. She will make for a pliant heart.\n"
                        voice "audio/voices/mound/mound1/15.flac"
                        show mound neutral talk onlayer front
                        with dissolve
                        mound "Do not mourn her. She has served her purpose.\n"
                    elif current_princess == "nightmare":
                        voice "audio/voices/mound/mound1/16.flac"
                        show mound shift talk onlayer front
                        with dissolve
                        mound "This one is filled with sadness. A doll abandoned to the company of her darkest impulses. She desires only companionship, but the only thing she knows is how to hurt. She will make for a tender heart.\n"
                        voice "audio/voices/mound/mound1/17.flac"
                        show mound neutral talk onlayer front
                        with dissolve
                        mound "Do not mourn her — she has finally found her way home.\n"
                    elif current_princess == "clarity":
                        voice "audio/_pristine/voice/_climax/mound_interstitial/_final/24.flac"
                        show mound shift talk onlayer front
                        with dissolve
                        mound "The one is a waiting maw. An inevitable destination where all roads end. She will make for a wise heart.\n"
                        voice "audio/voices/mound/mound1/21.flac"
                        show mound neutral talk onlayer front
                        with dissolve
                        mound "Do not mourn her — she is exactly where she needs to be.\n"
                    elif current_princess == "prisonerhead" or current_princess == "prisoner":
                        voice "audio/voices/mound/mound1/18.flac"
                        show mound shift talk onlayer front
                        with dissolve
                        mound "This one is cold and cynical. She has protected herself when others could not. She will make for a clever heart.\n"
                        voice "audio/voices/mound/mound1/19.flac"
                        show mound neutral talk onlayer front
                        with dissolve
                        mound "Do not mourn her — she doesn't need to be protected any longer.\n"
                    elif current_princess == "prisonerchain":
                        voice "audio/_pristine/voice/_climax/mound_interstitial/_final/25.flac"
                        show mound shift talk onlayer front
                        with dissolve
                        mound "This one is determined, but also cautious, one that would rather let the world move around her than move it herself. She will make for a patient heart.\n"
                        voice "audio/voices/mound/mound1/21.flac"
                        show mound neutral talk onlayer front
                        with dissolve
                        mound "Do not mourn her — she is exactly where she needs to be.\n"
                    elif current_princess == "razor" or current_princess == "razorheart":
                        #voice "audio/voices/mound/mound1/20.flac"
                        voice "audio/_pristine/voice/_climax/mound_interstitial/_final/22a.flac"
                        show mound shift talk onlayer front
                        with dissolve
                        #mound "This one is sharp and single-minded. She is cruelty. But she is also joy. She will make for an indomitable heart.\n"
                        mound "This one is a single-minded edge. She is cruelty. But she is also joy. She will make for a piercing heart.\n"
                        voice "audio/voices/mound/mound1/21.flac"
                        show mound neutral talk onlayer front
                        with dissolve
                        mound "Do not mourn her — she is exactly where she needs to be.\n"
                    elif current_princess == "spectre":
                        #voice "audio/voices/mound/mound1/22.flac"
                        voice "audio/_pristine/voice/_climax/mound_interstitial/_final/5a.flac"
                        show mound shift talk onlayer front
                        with dissolve
                        mound "This one is vaporous. She is a dream of a life she could never have, but that longing has given her so much capacity for kindness. She will make for a yearning heart.\n"
                        #mound "This one is vaporous. She is a dream for a life she could never have, but that longing has given her so much capacity for kindness. She will make for an understanding heart.\n"
                        voice "audio/voices/mound/mound1/23.flac"
                        show mound neutral talk onlayer front
                        with dissolve
                        mound "Do not mourn her — she will finally be able to hold what she never knew.\n"
                    elif current_princess == "stranger":
                        voice "audio/voices/mound/mound1/24.flac"
                        show mound shift talk onlayer front
                        with dissolve
                        mound "These ones are a contradiction. A winding kaleidoscope of paths unwalked. They are stretched into a shape not unlike me, but it is a shape they cannot hold.\n"
                        if loops_finished == 0:
                            voice "audio/voices/mound/mound1/25.flac"
                            show mound pose talk onlayer front
                            with dissolve
                            mound "I am sorry that you met this vessel so early in your journey, but they will make for a rich and vibrant heart.\n"
                        else:
                            voice "audio/voices/mound/mound1/26.flac"
                            show mound pose talk onlayer front
                            with dissolve
                            mound "They will make for a rich and vibrant heart.\n"
                        voice "audio/voices/mound/mound1/27.flac"
                        show mound neutral talk onlayer front
                        with dissolve
                        mound "Do not mourn them — for they will finally get to know themselves.\n"
                    elif current_princess == "tower":
                        #voice "audio/voices/mound/mound1/28a.flac"
                        voice "audio/_pristine/voice/_climax/mound_interstitial/_final/18.flac"
                        show mound shift talk onlayer front
                        with dissolve
                        #mound "This one is dominance. A figure capable of bending everything to her will. She will make for a terrifying and divine heart.\n"
                        mound "This one is dominance. A figure capable of bending everything to her will. She will make for an overwhelming heart.\n"
                        voice "audio/voices/mound/mound1/29.flac"
                        show mound neutral talk onlayer front
                        with dissolve
                        mound "Do not mourn her, for she would not be able to mourn you.\n"
                    elif current_princess == "apotheosis":
                        voice "audio/_pristine/voice/_climax/mound_interstitial/_final/19.flac"
                        show mound shift talk onlayer front
                        with dissolve
                        mound "This one sits at the cusp of awakening. A new god, waiting to be born. She will make for a terrifying and divine heart.\n"
                        voice "audio/_pristine/voice/_climax/mound_interstitial/_final/20.flac"
                        show mound neutral talk onlayer front
                        with dissolve
                        mound "Do not mourn her, for she has finally found her light.\n"
                    elif current_princess == "witch":
                        #voice "audio/voices/mound/mound1/30.flac"
                        voice "audio/_pristine/voice/_climax/mound_interstitial/_final/4.flac"
                        show mound shift talk onlayer front
                        with dissolve
                        mound "This one is hope marred by bitterness and betrayal. She could see the end of the tunnel, and the door was closed on her. She will make for a righteous heart.\n"
                        #mound "This one is hope marred by bitterness. She could see the end of the tunnel, and the door was closed on her. She will make for a righteous and weathered heart.\n"
                        voice "audio/voices/mound/mound1/31.flac"
                        show mound neutral talk onlayer front
                        with dissolve
                        mound "Do not mourn her — she is finally on the other side.\n"
                    elif current_princess == "fury" or current_princess == "furyheart":
                        voice "audio/_pristine/voice/_climax/mound_interstitial/_final/3.flac"
                        #voice "audio/voices/mound/mound1/32.flac"
                        show mound shift talk onlayer front
                        with dissolve
                        mound "This one is desecration. She placed the weight of her agony on you, yet it is she who unwound herself. There is passion and empathy buried under her unfeeling skin. She will make for a weathered heart.\n"
                        #mound "This one is desecration. She placed the weight of her agony on you, yet it is she who unwound herself. But there is passion and empathy in her misery. She will make for a burning heart.\n"
                        voice "audio/voices/mound/mound1/33.flac"
                        show mound neutral talk onlayer front
                        with dissolve
                        mound "Do not mourn her — she has finally found peace.\n"
                    elif current_princess == "wildnerves":
                        voice "audio/voices/mound/mound1/34a.flac"
                        show mound shift talk onlayer front
                        with dissolve
                        mound "This one is like a shadow of me, twisting vines in search of answers. She will make for a curious heart.\n"
                        voice "audio/voices/mound/mound1/35.flac"
                        show mound neutral talk onlayer front
                        with dissolve
                        mound "Do not mourn her — she has found what she yearned for.\n"
                    elif current_princess == "wildwound":
                        voice "audio/_pristine/voice/_climax/mound_interstitial/_final/26.flac"
                        show mound shift talk onlayer front
                        with dissolve
                        mound "This one is like a shadow of me, a memory of what she used to be, bound to the wounds of distance and time. She will make for a scarred and beautiful heart.\n"
                        voice "audio/voices/mound/mound1/33.flac"
                        show mound neutral talk onlayer front
                        with dissolve
                        mound "Do not mourn her — she has finally found peace.\n"
                    elif current_princess == "wraith":
                        voice "audio/voices/mound/mound1/36.flac"
                        show mound shift talk onlayer front
                        with dissolve
                        mound "This one is loneliness turned to seething. She could not find her strength in others, so she found it in herself. She will make for a driven heart.\n"
                        voice "audio/voices/mound/mound1/37.flac"
                        show mound neutral talk onlayer front
                        with dissolve
                        mound "Do not mourn her — she isn't alone anymore.\n"
                    elif current_princess == "greydamsel" or current_princess == "greyprisoner":
                        if current_princess == "greydamsel":
                            voice "audio/voices/mound/mound1/38.flac"
                            show mound shift talk onlayer front
                            with dissolve
                            mound "This one is passion betrayed. But even in the end, her love never faded. She will make for a bright heart.\n"
                            voice "audio/_pristine/voice/_climax/mound_interstitial/_final/20.flac"
                            #voice "audio/voices/mound/mound1/39.flac"
                            show mound neutral talk onlayer front
                            with dissolve
                            mound "Do not mourn her, for she has finally found her light.\n"
                            #mound "Do not mourn her. She has served her purpose.\n"
                        else:
                            voice "audio/voices/mound/mound1/40.flac"
                            show mound shift talk onlayer front
                            with dissolve
                            mound "This one is guarded sorrow. She saw herself as alone, but in the end had the courage to share with another. She will make for a deep heart.\n"
                            voice "audio/voices/mound/mound1/41.flac"
                            show mound neutral talk onlayer front
                            with dissolve
                            mound "Do not mourn her — she has finally been heard.\n"
                    elif current_princess == "thorn":
                        voice "audio/voices/mound/mound1/42.flac"
                        show mound shift talk onlayer front
                        with dissolve
                        mound "This one yearns for connections she feels she doesn't deserve. Even when shown compassion, she hid herself away. She will make for a cautious heart.\n"
                        voice "audio/voices/mound/mound1/43a.flac"
                        show mound neutral talk onlayer front
                        #with dissolve
                        mound "Do not mourn her — she isn't alone anymore.\n"

                show mound neutral onlayer front
                with dissolve
                if loops_finished == 0:
                    jump quiet_1_menu
                elif loops_finished == 1:
                    jump quiet_2_menu
                elif loops_finished == 2:
                    jump quiet_3_menu
                elif loops_finished == 3:
                    jump quiet_4_menu

            "• (Explore) ''Is this the end of the world?''" if quiet_1_world_end == False:
                default quiet_1_world_end = False
                $ quiet_1_world_end = True
                voice "audio/voices/mound/mound1/44a.flac"
                show mound shift talk onlayer front
                with dissolve
                mound "How can the world have ended if we are talking?\n"
                show mound shift onlayer front
                #with dissolve
                jump quiet_1_menu

            "• (Explore) ''Let her out of there!''" if quiet_1_let_out == False:
                default quiet_1_let_out = False
                $ quiet_1_let_out = True
                voice "audio/voices/mound/mound1/45.flac"
                show mound neutral talk onlayer front
                with dissolve
                mound "I'm sorry. There are some changes that can never be undone, there are some tears that can never be unshed. This is not a place that can hold a fragment of a concept. The moment she arrived here, she was going to return to me.\n"
                voice "audio/voices/mound/mound1/46.flac"
                show mound shift talk onlayer front
                with dissolve
                mound "I promise that it doesn't hurt.\n"
                show mound shift onlayer front
                #with dissolve
                jump quiet_1_menu

            "• (Explore) ''Do you know the Narrator?''" if quiet1_narrator == False:
                $ quiet1_narrator = True
                if wild_fed or wraith_fed or spectre_fed or apotheosis_fed or tower_fed:
                    voice "audio/voices/mound/mound1/47b.flac"
                    show mound neutral talk onlayer front
                    with dissolve
                    mound "I know of him through the memories of my vessel. But she had nothing like him on her own.\n"
                else:
                    voice "audio/voices/mound/mound1/47.flac"
                    show mound neutral talk onlayer front
                    with dissolve
                    mound "You are the only thing I have ever known.\n"

                voice "audio/voices/mound/mound1/48.flac"
                show mound shift talk onlayer front
                with dissolve
                mound "The space we're in is vacant. Nothing comes here but us.\n"
                show mound shift onlayer front
                #with dissolve
                jump quiet_1_menu

            "• (Explore) ''Are you what sent me to slay the Princess? Are you what trapped me here?''" if quiet1_trapped == False:
                $ quiet1_trapped = True
                voice "audio/voices/mound/mound1/49.flac"
                show mound neutral talk onlayer front
                with dissolve
                mound "I have only just now stirred to consciousness. I could not have trapped you here, and I too yearn to be free.\n"
                show mound neutral onlayer front
                #with dissolve
                jump quiet_1_menu

            "• (Explore) ''Do you know about the worlds beyond this place?''" if quiet1_worlds_beyond == False:
                $ quiet1_worlds_beyond = True
                voice "audio/voices/mound/mound1/50.flac"
                show mound pose talk onlayer front
                with dissolve
                mound "I know only that they are.\n"
                show mound pose onlayer front
                #with dissolve
                jump quiet_1_menu

            "• (Explore) ''Are you the Princess?''" if quiet1_are_you_princess == False:
                $ quiet1_are_you_princess = True
                voice "audio/voices/mound/mound1/51.flac"
                show mound neutral talk onlayer front
                with dissolve
                mound "She is part of me, and part of me is her.\n"
                show mound neutral onlayer front
                #with dissolve
                menu:
                    extend ""

                    "• ''But were you always the Princess, or are you just making her a part of yourself?''":
                        voice "audio/voices/mound/mound1/52.flac"
                        show mound shift talk onlayer front
                        with dissolve
                        mound "You speak in circles. Does it matter where one thing begins and another ends?\n"
                        show mound shift onlayer front
                        #with dissolve

                    "• [[Say nothing.]":
                        jump quiet_1_menu

                jump quiet_1_menu

            "• (Explore) ''Do we know each other?''" if quiet1_know_each_other == False and loops_destroyed == False:
                $ quiet1_know_each_other = True
                voice "audio/voices/mound/mound1/54.flac"
                show mound shift talk onlayer front
                with dissolve
                mound "You are familiar, but you are not me. I feel sadness, longing, hope, as I witness you.\n"
                show mound shift onlayer front
                #with dissolve
                jump quiet_1_menu

            "• ''What happens now?''":
                voice "audio/voices/mound/mound1/55.flac"
                show mound neutral talk onlayer front
                with dissolve
                mound "Nothing, as we are. But I know that there are worlds beyond us, and that we are meant to reach them.\n"
                voice "audio/voices/mound/mound1/56.flac"
                show mound pose talk onlayer front
                with dissolve
                mound "There is no exit, but this vessel is a creature of perception. She can make you forget, if only you believe her to be able to.\n"
                voice "audio/voices/mound/mound1/57.flac"
                show mound neutral talk onlayer front
                with dissolve
                mound "Bring me more perspectives, so that I may be whole, and perhaps then we will know our freedom.\n"
                show mound neutral onlayer front
                #with dissolve
                label quiet1_decision:
                    default quiet1_decision_count = 0
                    menu:
                        extend ""

                        "• (Explore) ''Aren't you scared that I'll find a way to kill you?''" if quiet1_kill_explore == False:
                            $ quiet1_kill_explore = True
                            $ quiet1_decision_count += 1
                            #$ quiet_threaten_count += 1
                            voice "audio/voices/mound/mound1/58.flac"
                            show mound neutral talk onlayer front
                            with dissolve
                            mound "I have not lived. I am not afraid to die.\n"
                            show mound neutral onlayer front
                            #with dissolve
                            jump quiet1_decision

                        "• (Explore) ''How much will I forget?''" if quiet1_forget_explore == False:
                            $ quiet1_forget_explore = True
                            $ quiet1_decision_count += 1
                            voice "audio/voices/mound/mound1/59.flac"
                            show mound shift talk onlayer front
                            with dissolve
                            mound "Everything, until we meet again.\n"
                            show mound shift onlayer front
                            #with dissolve
                            jump quiet1_decision

                        "• (Explore) ''How many more pieces of you do I have to find?''" if quiet1_pieces_explore == False:
                            $ quiet1_pieces_explore = True
                            $ quiet1_decision_count += 1
                            voice "audio/voices/mound/mound1/60.flac"
                            show mound pose talk onlayer front
                            with dissolve
                            mound "More than you have found, but less than there are to find. I am infinite. The rest will find their own way home.\n"
                            show mound pose onlayer front
                            #with dissolve
                            jump quiet1_decision

                        "• (Explore) ''And what if I don't let you do this to me?''" if quiet1_refuse_explore == False:
                            $ quiet1_refuse_explore = True
                            $ quiet1_decision_count += 1
                            voice "audio/voices/mound/mound1/61.flac"
                            show mound neutral talk onlayer front
                            with dissolve
                            mound "Then we will be here forever, as we are now. Unfinished, dry, hollow.\n"
                            show mound neutral onlayer front
                            #with dissolve
                            jump quiet1_decision

                        "• (Explore) ''I was sent to slay the Princess to stop her from destroying the world. If I help you, is that what you're going to do?''" if quiet1_destroy_explore == False:
                            $ quiet1_destroy_explore = True
                            $ quiet1_decision_count += 1
                            voice "audio/voices/mound/mound1/62.flac"
                            show mound shift talk onlayer front
                            with dissolve
                            mound "You ask of things that cannot be done. To destroy is merely to reshape. To remold.\n"
                            show mound shift onlayer front
                            #with dissolve
                            menu:
                                extend ""

                                "• ''You're being semantic. What are you going to do if I help you?''":
                                    voice "audio/voices/mound/mound1/63.flac"
                                    show mound pose talk onlayer front
                                    with dissolve
                                    mound "How can I know? I am flickers in something sprawling and unilluminated.\n"
                                    show mound pose onlayer front
                                    #with dissolve
                                    jump quiet1_decision

                                "• [[Let it be.]":
                                    jump quiet1_decision


                        "• ''I'm not going back.'' [[Wait.]" if quiet1_stay_forever_attempt == False and quiet1_refuse_explore:
                            $ quiet1_stay_forever_attempt = True
                            voice "audio/voices/mound/mound1/65.flac"
                            show mound neutral talk onlayer front
                            with dissolve
                            mound "If you need time, then I'll wait with you.\n"
                            show mound neutral onlayer front
                            #with dissolve
                            menu:

                                "• [[Wait forever.]":
                                    $ quiet1_stay_forever_attempt = True
                                    voice "audio/voices/mound/mound1/66.flac"
                                    show mound shift talk onlayer front
                                    with dissolve
                                    mound "You are as I am now, and forever is a long time to remain undone.\n"
                                    voice "audio/voices/mound/mound1/67a.flac"
                                    show mound neutral talk onlayer front
                                    with dissolve
                                    mound "I am not you, but I know that I would return before forever was finished.\n"
                                    label wait_forever_join:
                                        voice "audio/voices/mound/mound1/68.flac"
                                        show mound pose talk onlayer front
                                        with dissolve
                                        mound "What textures will you weave for yourself to occupy forever? Will you place the images of 'You' and 'I' into a box for safekeeping?\n"
                                        voice "audio/voices/mound/mound1/69.flac"
                                        show mound shift talk onlayer front
                                        with dissolve
                                        mound "If you close that box, will you become another you in another world? An imaginary pattern repeating itself until it can no longer bear the weight of its hand-drawn cage.\n"
                                        voice "audio/voices/mound/mound1/70.flac"
                                        show mound neutral talk onlayer front
                                        with dissolve
                                        mound "You'll always come back to the box, because you'll always want to know what it means to be you. I will be here waiting by your side until you're ready to return to mine.\n"
                                        if renpy.variant("pc"):
                                            $ persistent.quiet_gimmick = True
                                            $ persistent.quiet_gimmick_stage_2 = False
                                        $ quiet_date_1 = datetime.date.today()
                                        label wait_forever_late_join:
                                            if renpy.variant("pc"):
                                                $ renpy.save('gimmick')
                                            if persistent.quiet_gimmick_stage_2:
                                                jump quiet_1_wait_forever_join
                                            if renpy.variant("console"):
                                                $ quick_menu = False
                                                stop music
                                                stop sound
                                                stop secondary
                                                play music "audio/_music/main_menu.flac"
                                                show screen fake_menu()
                                                $ renpy.pause()
                                                label console_wait_jump:
                                                    if persistent.quick_menu:
                                                        $ quick_menu = True
                                                    play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg"
                                                    if loops_finished == 0:
                                                        play music "audio/_music/mound/The Mound Movement I.flac" loop
                                                    if loops_finished == 1:
                                                        play music "audio/_music/mound/The Mound Movement II Intro.flac"
                                                        queue music "audio/_music/mound/The Mound Movement II Loop.flac" loop
                                                    elif loops_finished == 2:
                                                        stop secondary fadeout 15.0
                                                        play music "audio/_music/mound/The Mound Movement III Intro.flac"
                                                        queue music "audio/_music/mound/The Mound Movement III Loop.flac" loop
                                                    elif loops_finished == 3:
                                                        stop secondary fadeout 15.0
                                                        play music "audio/_music/mound/The Mound Movement IV Intro.flac"
                                                        queue music "audio/_music/mound/The Mound Movement IV Loop.flac" loop
                                            elif persistent.quiet_gimmick:
                                                $ renpy.quit()
                                            label quiet_1_wait_forever_join:
                                                if renpy.variant("pc"):
                                                    if persistent.gimmick_quick_loaded:
                                                        $ persistent.gimmick_quick_loaded = False
                                                        $ renpy.unlink_save("quick-1")
                                                    $ renpy.unlink_save("gimmick")

                                                $ achievement.grant("ACH_MOUND_WAIT")
                                                $ persistent.quiet_gimmick = False
                                                $ persistent.quiet_gimmick_stage_2 = False
                                                $ quiet_date_2 = datetime.date.today()
                                                $ quiet_date_delta = quiet_date_2 - quiet_date_1
                                                $ quiet_delta_delta_days = quiet_date_delta.days
                                                if quiet_delta_delta_days < 1 and renpy.variant("pc"):
                                                    voice "audio/voices/mound/mound1/71.flac"
                                                    mound "You have returned to me. Though you were gone mere moments, I never left your side.\n"
                                                elif quiet_delta_delta_days < 7:
                                                    voice "audio/voices/mound/mound1/72.flac"
                                                    mound "I see you have returned to me. Days mean nothing in the maw of forever. I never left your side.\n" id quiet_1_wait_forever_join_6f653e4a
                                                elif quiet_delta_delta_days < 50:
                                                    voice "audio/voices/mound/mound1/73.flac"
                                                    mound "I see you have returned to me. Weeks mean nothing in the maw of forever. I never left your side.\n"
                                                elif quiet_delta_delta_days < 91:
                                                    voice "audio/voices/mound/mound1/74.flac"
                                                    mound "I see you have returned to me. Months mean nothing in the maw of forever. I never left your side.\n"
                                                elif quiet_delta_delta_days < 765:
                                                    voice "audio/voices/mound/mound1/75.flac"
                                                    mound "I see you have returned to me. Years mean nothing in the maw of forever. I never left your side.\n"
                                                elif quiet_delta_delta_days < 7650:
                                                    voice "audio/voices/mound/mound1/76.flac"
                                                    mound "I see you have returned to me. Decades mean nothing in the maw of forever. I never left your side.\n"
                                                elif quiet_delta_delta_days < 76500:
                                                    voice "audio/voices/mound/mound1/77.flac"
                                                    mound "I see you have returned to me. Centuries mean nothing in the maw of forever. I never left your side.\n"
                                                else:
                                                    voice "audio/voices/mound/mound1/78.flac"
                                                    mound "I see you have returned to me. Even millennia mean nothing in the maw of forever. I never left your side.\n"
                                                show mound neutral onlayer front
                                                with dissolve
                                                if loops_finished == 0:
                                                    jump quiet1_decision
                                                elif loops_finished == 1:
                                                    jump quiet_2_menu
                                                elif loops_finished == 2:
                                                    jump quiet_3_menu
                                                elif loops_finished == 3:
                                                    jump quiet_4_menu

                                "• ''Okay. I'm ready. Make me forget.''":
                                    jump quiet_1_forget_join

                        "• ''Okay. Make me forget.''":
                            label quiet_1_forget_join:
                                voice "audio/voices/mound/mound1/64.flac"
                                show mound neutral talk onlayer front
                                with dissolve
                                mound "She asks that I tell you to remember her.\n"
                                voice "audio/voices/mound/mound1/64a.flac"
                                show mound shift talk onlayer front
                                with dissolve
                                mound "You won't.\n{w=0.8}{nw}"
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
                $ quiet1_mound_attacked = True
                $ quiet_attack = True
                play audio "audio/final/Assorted_WingsFlap_2.flac"
                truth "Your will cuts across the entity in front of you, but nothing happens.\n"
                voice "audio/voices/mound/mound1/79.flac"
                show mound neutral talk onlayer front
                with dissolve
                mound "My roots burrow in an ocean beyond your sight. We cannot harm each other as we are now.\n"
                show mound neutral onlayer front
                #with dissolve
                jump quiet_1_menu

            "•  [[Destroy your body.]" if quiet_suicide_attempt == False:
                $ quiet1_suicide = True
                $ quiet_suicide_attempt = True
                play audio "audio/final/Adversary_HandThroughChest_1.flac"
                truth "You raise your will to end your life. But as it buries into the space your body should be, you feel nothing at all.\n"
                truth "One of the many hands in front of you reaches forward, and gently touches the side of your face.\n"
                voice "audio/voices/mound/mound1/80.flac"
                show mound pose talk onlayer front
                with dissolve
                mound "There's nowhere for you to be but here.\n"
                show mound pose onlayer front
                #with dissolve
                jump quiet_1_menu
return
