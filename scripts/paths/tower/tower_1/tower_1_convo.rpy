label tower_1_convo_start:
    default tower_self_knowledge = False
    default tower_priest_offer = False
    default tower_false_choice = False
    default tower_forced_pledge = False

    if basement_1_shared_task:
        $ tower_self_knowledge = True
        voice "audio/voices/ch2/tower/_cont/princess/p1.flac"
        show tower d closed talk onlayer back
        with dissolve
        p "The last time we met, you told me I was destined to end the world. That thought wrapped itself around my heart. It has pulled at me since the moment I squeezed the life out of your broken lungs.\n"
        voice "audio/voices/ch2/tower/_cont/princess/p2a.flac"
        show tower d curious talk onlayer back
        with dissolve
        p "I could feel its fundamental truth awaken me.\n"
        voice "audio/voices/ch2/tower/_cont/princess/p3.flac"
        show tower d pontificate onlayer back
        with dissolve
        p "The collapse of the old is a necessary prelude to the birth of the new, and the world as it is now is overdue for alterations.\n"
        voice "audio/voices/ch2/tower/_cont/princess/p4.flac"
        show tower d serious talk onlayer back
        with dissolve
        p "It's time for me to seize my destiny, and you, little bird, will help me seize it.\n"
        voice "audio/voices/ch2/tower/_cont/hero/1.flac"
        show tower d serious onlayer back
        hero "Well that gives away the game, doesn't it?\n"
        if tower_1_forest_share_loop:
            voice "audio/voices/ch2/tower/_cont/narrator/1.flac"
            n "It certainly does. And beyond that, it more than lends credence to our conversation in the woods. I don't love the thought that in some other reality you failed to destroy her, but what's done is done, and I can only hope it helped you learn a valuable lesson.\n"
            voice "audio/voices/ch2/tower/_cont/narrator/2.flac"
            n "You are the only one who can deal with her. And if you don't... well, she's let you know what will happen, hasn't she?\n"
            voice "audio/voices/ch2/tower/_cont/broken/tower_broken_1.flac"
            broken "Then you shouldn't have trusted us with her destruction. She is inevitable. Can't you feel it?\n"
            voice "audio/voices/ch2/tower/_cont/hero/2.flac"
            hero "He's being melodramatic, but he's not exactly wrong, is he? What are we supposed to do to stop her?\n"
        else:
            voice "audio/voices/ch2/tower/_cont/narrator/3.flac"
            n "It does. But why did she say 'the last time we met'? That's not right. That can't be right.\n"
            voice "audio/voices/ch2/tower/_cont/hero/3.flac"
            hero "She's right. We've been here before.\n"
            voice "audio/voices/ch2/tower/_cont/broken/tower_broken_2a.flac"
            broken "And we've died here before. Pitifully. We might as well do what she asks of us and help her. She's inevitable. Can't you feel it?\n"
            voice "audio/voices/ch2/tower/_cont/hero/4.flac"
            hero "He's being melodramatic, but the point stands. What are we even supposed to do to stop her?\n"
            voice "audio/voices/ch2/tower/_cont/narrator/4.flac"
            n "Well I'll be damned. That's not good.\n"

        voice "audio/voices/ch2/tower/_cont/narrator/5.flac"
        n "{i}Sigh.{/i} Okay. First thing's first, you're going to have to stuff those pessimistic thoughts some place far far away and commit yourself to what needs to be done.\n"
        voice "audio/voices/ch2/tower/_cont/narrator/6a.flac"
        n "The stakes of the situation should be perfectly clear to everyone now. And if you're going to save the world, you have to have faith that you can pull this off. You can't win a battle that you've already lost in your mind.\n" id tower_1_convo_start_e16be838
        jump tower_1_join_me_menu

    else:
        if tower_1_cabin_blade_taken:
            if tower_pathetic:
                voice "audio/voices/ch2/tower/_cont/princess/p5.flac"
                show tower d closed talk onlayer back
                with dissolve
                p "The last time we met, you tried to kill me. And here you are again, trying to succeed where you've already catastrophically failed.\n"
            else:
                voice "audio/voices/ch2/tower/_cont/princess/p5a.flac"
                show tower d closed talk onlayer back
                with dissolve
                p "The last time we met, you couldn't even scratch me. And yet here you are again, trying to succeed where you've already catastrophically failed.\n"
        else:
            voice "audio/voices/ch2/tower/_cont/princess/sp1.flac"
            show tower d closed talk onlayer back
            with dissolve
            sp "The last time we met, you tried to kill me. And yet here you are again, this time groveling at my feet. What a wretched sight.\n"
        voice "audio/voices/ch2/tower/_cont/princess/p6.flac"
        show tower d ponder talk onlayer back
        with dissolve
        p "What draws you back here beyond the empty halls of death?\n"
        voice "audio/voices/ch2/tower/_cont/princess/sp2.flac"
        show tower d talk onlayer back
        with dissolve
        sp "Speak.\n"
        show tower d smile talk onlayer back
        with dissolve
        if tower_1_forest_share_loop:
            voice "audio/voices/ch2/tower/_cont/narrator/7.flac"
            n "'The last time we met?' I suppose that lends credence to our conversation in the woods. Still, whatever you do, don't tell her why you're here. It's best not to give her any ideas.\n"
        else:
            voice "audio/voices/ch2/tower/_cont/narrator/8.flac"
            n "'The last time we met?'\n"
            voice "audio/voices/ch2/tower/_cont/narrator/9.flac"
            n "Nobody should have 'met' her before this. You should be the first. You're the only one I trust to deal with her.\n"
            voice "audio/voices/ch2/tower/_cont/broken/tower_broken_3.flac"
            broken "Then you shouldn't have trusted us. There was nothing we could do to stop her then, and there's nothing we can do to stop her now.\n"
            voice "audio/voices/ch2/tower/_cont/hero/5.flac"
            hero "He's being melodramatic, but yeah, we've been here before, and she absolutely destroyed us. What are we even supposed to do to stop her?\n"
            #hero "He's being melodramatic, but yeah, we've met you before, and we've been here before, and she absolutely destroyed us.\n"
            voice "audio/voices/ch2/tower/_cont/narrator/10.flac"
            n "That's... worrying. Whatever you do, don't tell her why you're here. It's best not to give her any ideas.\n"

        label tower_1_share_motive_menu:
            default tower_1_share_menu_give_in_explore = False
            default tower_1_share_motive_resist_attempt = False
            menu:

                extend ""

                "{i}• (Explore) I don't think I can refuse her. Sorry.{/i}" if tower_resist_count == 0 and tower_1_share_menu_give_in_explore == False:
                    $ tower_1_share_menu_give_in_explore = True
                    voice "audio/voices/ch2/tower/_cont/narrator/11.flac"
                    n "Are you serious? Just— just don't say anything! How hard can it be to not say anything?\n"
                    voice "audio/voices/ch2/tower/_cont/broken/tower_broken_4.flac"
                    broken "You haven't felt her angelic fingers run along the edges of your mind. You haven't felt her nails dig into your thoughts.\n"
                    jump tower_1_share_motive_menu

                "{i}• (Explore) N-no. I w-won't t-tell you.{/i}" if tower_resist_count > 0 and tower_1_share_motive_resist_attempt == False and tower_submit_count != 0:
                    $ tower_resist_count += 1
                    $ tower_1_share_motive_resist_attempt = True
                    voice "audio/voices/ch2/tower/_cont/princess/sp3.flac"
                    show tower d command onlayer back
                    with dissolve
                    sp "You will.\n"
                    voice "audio/voices/ch2/tower/_cont/broken/tower_broken_5.flac"
                    broken "Just do it already... it will feel so much better to do as she says.\n"
                    jump tower_1_share_motive_menu

                "{i}• ''You're supposed to end the world.''{/i}":
                    voice "audio/voices/ch2/tower/_cont/narrator/12.flac"
                    n "You weak-willed buffoon!\n"
                    voice "audio/voices/ch2/tower/_cont/princess/p7.flac"
                    show tower d ponder talk onlayer back
                    with dissolve
                    p "Is that so?\n"
                    voice "audio/voices/ch2/tower/_cont/narrator/13.flac"
                    show tower d closed onlayer back
                    with dissolve
                    n "The Princess closes her eyes in contemplation.\n"
                    label tower_1_motive_shared_join:
                        default tower_can_fury = True
                        $ tower_can_fury = False
                        $ tower_self_knowledge = True
                        voice "audio/voices/ch2/tower/_cont/princess/p8.flac"
                        show tower d talk onlayer back
                        with dissolve
                        p "Something about that thought wraps itself around my heart. It feels like a fundamental truth to my being that I'd somehow forgotten.\n"
                        voice "audio/voices/ch2/tower/_cont/princess/p3.flac"
                        show tower d pontificate onlayer back
                        with dissolve
                        p "The collapse of the old is a necessary prelude to the birth of the new, and the world as it is now is overdue for alterations.\n"
                        voice "audio/voices/ch2/tower/_cont/princess/p10.flac"
                        show tower d curious onlayer back
                        with dissolve
                        p "It's time for me to seize my destiny, and you, little bird, will help me seize it.\n"
                        voice "audio/voices/ch2/tower/_cont/broken/tower_broken_6.flac"
                        broken "She's inevitable. There's nothing else for us to do but help her. Maybe she'll be nice to us.\n"
                        jump tower_1_join_me_menu

                "{i}• ''I said NO!''{/i}" if tower_1_share_motive_resist_attempt and tower_1_cabin_blade_taken and tower_resist_count >= 3:
                    voice "audio/voices/ch2/tower/_cont/princess/p11.flac"
                    show tower d curious talk onlayer back
                    with dissolve
                    p "Such firm resistance. How surprising.\n"
                    jump tower_1_battle_motive_join

                "{i}• ''No.''{/i}" if tower_submit_count == 0:
                    jump tower_1_battle_motive_join

                "{i}• [[Remain silent.]{/i}":
                    voice "audio/voices/ch2/tower/_cont/princess/sp4.flac"
                    show tower d pontificate onlayer back
                    with dissolve
                    sp "Do you think holding shut your beak is enough to stop me from prying it open? Do you think your skull can save your thoughts from being seen?\n"
                    if tower_submit_count == 0:
                        voice "audio/voices/ch2/tower/_cont/princess/p12.flac"
                        show tower d curious talk onlayer back
                        with dissolve
                        p "Hmm. You're less broken than I'd thought.\n"
                        jump tower_1_battle_motive_join

                    voice "audio/voices/ch2/tower/_cont/hero/6.flac"
                    hero "Can— can she do that?\n"
                    voice "audio/voices/ch2/tower/_cont/broken/tower_broken_7.flac"
                    broken "There's nothing she can't do.\n"
                    if tower_1_cabin_blade_taken == False:
                        voice "audio/voices/ch2/tower/_cont/princess/p13a.flac"
                        show tower d command onlayer back
                        with dissolve
                        p "Confused. Meek. A chorus of submissive indecision. Is that why you came to me unarmed?\n"
                        voice "audio/voices/ch2/tower/_cont/princess/p14.flac"
                        p "It doesn't matter. All of it is easily brushed aside.\n"
                    else:
                        voice "audio/voices/ch2/tower/_cont/princess/p15.flac"
                        show tower d command onlayer back
                        with dissolve
                        p "Meekness. Despair. But a hint at something more. A small taste of stubborn resistance.\n"
                        voice "audio/voices/ch2/tower/_cont/princess/sp5.flac"
                        sp "A grain in the storm of my cosmic wind. Enough to be felt, but not enough to matter.\n"

                    voice "audio/voices/ch2/tower/_cont/princess/p16.flac"
                    show tower d closed talk onlayer back
                    with dissolve
                    p "And there it is. I am destined to end the world.\n"
                    jump tower_1_motive_shared_join


label tower_1_join_me_menu:
    default tower_join_me_what_role = False
    default tower_break_self = False
    default tower_self_determination = False
    default tower_join_me_count = 0
    menu:
        extend ""

        "{i}• (Explore) ''What would you have me do? What do you have planned?''{/i}" if tower_join_me_what_role == False:
            $ tower_join_me_what_role = True
            $ tower_join_me_count += 1
            voice "audio/voices/ch2/tower/_cont/princess/p17.flac"
            show tower d closed talk onlayer back
            with dissolve
            p "All you have to do is break these chains and set me free.\n"
            show tower d closed onlayer back
            jump tower_1_join_me_menu

        "{i}• (Explore) ''If you're so powerful, can't you just break the chains yourself?''{/i}" if tower_join_me_what_role and tower_break_self == False:
            $ tower_break_self = True
            $ tower_join_me_count += 1
            voice "audio/voices/ch2/tower/_cont/broken/tower_broken_8.flac"
            broken "Don't be rude. Of course she can.\n"
            voice "audio/voices/ch2/tower/_cont/hero/7.flac"
            hero "It's not rude to question someone who's apparently trying to end the world.\n"
            voice "audio/voices/ch2/tower/_cont/broken/tower_broken_9.flac"
            broken "That's exactly why it's rude. We should know our place.\n"
            voice "audio/voices/ch2/tower/_cont/princess/p18.flac"
            show tower d curious onlayer back
            with dissolve
            p "I can. Easily. But that isn't what I want to do.\n"
            voice "audio/voices/ch2/tower/_cont/princess/p19.flac"
            show tower d pride talk onlayer back
            with dissolve
            p "The story of a terrible and bountiful god unbounded of her own will is no story at all. It's not worthy of everything I am or everything I'm bound to become. It isn't even worthy of what I was.\n"
            voice "audio/voices/ch2/tower/_cont/princess/sp6.flac"
            show tower d pontificate onlayer back
            with dissolve
            sp "The destruction and genesis that's to follow in my wake is deserving of a song that can echo for eternity.\n"
            voice "audio/voices/ch2/tower/_cont/princess/sp7.flac"
            show tower d command onlayer back
            with dissolve
            sp "The song of you, being so struck by my glory, so overwhelmed by what I am, that you feel you must deliver me unto the world.\n"
            voice "audio/voices/ch2/tower/_cont/princess/sp8.flac"
            show tower d pontificate onlayer back
            with dissolve
            sp "And from your act of utter devotion and submission springs a new dawn. A better dawn.\n"
            voice "audio/voices/ch2/tower/_cont/princess/p20.flac"
            show tower d smile talk onlayer back
            with dissolve
            p "Submit now. Submit later. It makes no difference, because in the end, no matter how vainly you struggle against me, {outlinecolor=4f1313}{color=#e44646}my will triumphs over yours.{/color}{/outlinecolor}\n"
            jump tower_1_join_me_menu

        "{i}• (Explore) ''Just because you're supposed to end the world doesn't mean you actually have to do it. You can be whatever you want to be.''{/i}" if tower_self_determination == False:
            $ tower_join_me_count += 1
            $ tower_self_determination = True
            voice "audio/voices/ch2/tower/_cont/princess/p21a.flac"
            show tower d talk onlayer back
            with dissolve
            p "This isn't about desire. This is about what I am, and I have little interest in discussing destiny with one that cannot see the divine truth that shines in my heart.\n"
            jump tower_1_join_me_menu

        "{i}• (Explore) ''I have questions for you before I decide to do anything.''{/i}" if tower_priest_offer == False:
            label tower_talk_refuse:
                $ tower_join_me_count += 1
                $ tower_priest_offer = True
                voice "audio/voices/ch2/tower/_cont/princess/p22.flac"
                show tower d pontificate onlayer back
                with dissolve
                sp "Know the limits of your privilege, little bird.\n"
                show tower d closed talk onlayer back
                with dissolve
                voice "audio/voices/ch2/tower/_cont/princess/p22a.flac"
                p "There is an empty place at my side for you to fill, if you'll have it. But it is not a place for an equal. It is a place for something worthy to be kept. A priest, perhaps. Or a pet.\n"
                show tower d closed onlayer back
                with dissolve
                jump tower_1_join_me_menu

        "{i}• (Explore) ''What happened to you after I died?''{/i}" if tower_priest_offer == False:
            jump tower_talk_refuse

        "{i}• ''I'm not going to help you end the world. I don't care if something new comes after. I just can't let you do that.''{/i}" if tower_1_cabin_blade_taken == False and tower_resist_count >= 2:
            label tower_1_empty_refuse_join:
                $ gallery_tower.unlock_item(5)
                $ renpy.save_persistent()
                $ tower_forced_pledge = True
                voice "audio/voices/ch2/tower/_cont/princess/p23.flac"
                show tower d closed talk onlayer back
                with dissolve
                p "You poor, deluded thing. Don't think you can muster up the strength to defy me now. You already submitted the moment you entered this temple without the will to end me.\n"
                show tower d closed onlayer back
                voice "audio/voices/ch2/tower/_cont/hero/8.flac"
                hero "Wha — what is she talking about?\n"
                voice "audio/voices/ch2/tower/_cont/narrator/14.flac"
                show tower d curious onlayer back
                with dissolve
                n "She's talking about your ridiculous decision to come down here unarmed. But it doesn't matter, don't let her talk you into bowing down to her or whatever it is she thinks she can make you do. You can still go back and get the blade from upstairs. You can still stop her.\n"
                voice "audio/voices/ch2/tower/_cont/broken/tower_broken_10.flac"
                broken "But we're already here, and we already made our choice, and there are so many tall stairs between us and that altar...\n"
                voice "audio/voices/ch2/tower/_cont/narrator/15.flac"
                n "You're right about one thing: you already made your choice, and your choice was to defy her. I don't care how many stairs there are or how tall they are. You're going to turn around, right now, take the blade, and save the damn world.\n"
                voice "audio/voices/ch2/tower/_cont/princess/p24.flac"
                show tower d curious talk onlayer back
                with dissolve
                p "Even now your vessel twitches and trembles, consumed by conflict with yourself.\n"
                voice "audio/voices/ch2/tower/_cont/princess/p25.flac"
                show tower d ponder talk onlayer back
                with dissolve
                p "But that part of you standing in hopeless defiance isn't the only thing resisting me, is it? There's something else in there. Someone else. A greasy film sheltering your heart.\n"
                voice "audio/voices/ch2/tower/_cont/princess/p26.flac"
                show tower d closed talk onlayer back
                with dissolve
                p "Is that a person? No. It used to be a person. It's something different now. An echo.\n"
                show tower d closed onlayer back
                voice "audio/voices/ch2/tower/_cont/hero/9.flac"
                hero "Is... is she talking about you?\n"
                voice "audio/voices/ch2/tower/_cont/narrator/16.flac"
                n "That's impossible. She's not supposed to be able to interact with me, she—\n{w=3.65}{nw}"
                show screen disableclick(0.5)
                voice "audio/voices/ch2/tower/_cont/princess/p27.flac"
                show tower d pontificate onlayer back
                p "You're a small one, aren't you?\n"
                voice "audio/voices/ch2/tower/_cont/princess/sp9.flac"
                sp "A shriveling little worm stretched beyond its limits, trying to control things that it can't understand.\n"
                voice "audio/voices/ch2/tower/_cont/narrator/17.flac"
                n "No no no, what are you talking about I'm just—\n{w=2.7}{nw}"
                show screen disableclick(0.5)
                voice "audio/voices/ch2/tower/_cont/princess/sp10.flac"
                show tower d command onlayer back
                with dissolve
                sp "I don't care what you are. You're mine.\n"
                voice "audio/voices/ch2/tower/_cont/narrator/18.flac"
                show tower d curious onlayer back
                with dissolve
                n "{i}Screaming.{/i}\n"
                voice "audio/voices/ch2/tower/_cont/hero/10.flac"
                hero "Uh... are you okay?\n"
                # narrator and princess together
                voice "audio/voices/ch2/tower/_cont/narrator/np19.flac"
                show tower d smile talk onlayer back
                with dissolve
                np "I'm fine. I've always been fine.\n"
                #voice "audio/voices/ch2/tower/_cont/princess/p28.flac"
                #p "He's fine. He's always been fine.\n"
                voice "audio/voices/ch2/tower/_cont/hero/11.flac"
                hero "No no no, this isn't right! What do we do? We can't just let her control us like this!\n"
                voice "audio/voices/ch2/tower/_cont/broken/tower_broken_11.flac"
                broken "I've been trying to tell you this whole time. It isn't about can or can't. It isn't even about will or won't. There is only one path in front of us, and we will walk it.\n"
                voice "audio/voices/ch2/tower/_cont/hero/12.flac"
                hero "We'll— we'll just refuse!\n"
                # maybe see
                voice "audio/voices/ch2/tower/_cont/broken/tower_broken_12.flac"
                broken "Not even He could refuse her in the end. What are you supposed to do? We're all prisoners here. Some of us are just willing to embrace our chains.\n"
                jump tower_self_end_late_join

        "{i}• ''No. I won't take part in this.'' [[Refuse her.]{/i}" if tower_1_cabin_blade_taken == False and tower_resist_count >= 2:
            jump tower_1_empty_refuse_join

        "{i}• ''I'm not going to help you end the world. I don't care if something new comes after. I just can't let you do that.''{/i}" if tower_1_cabin_blade_taken:
            voice "audio/voices/ch2/tower/_cont/princess/p29.flac"
            show tower d closed talk onlayer back
            with dissolve
            p "I see.\n"
            jump tower_1_battle_motive_join

        "{i}• ''I'm yours to command.'' [[Pledge yourself to her.]{/i}":
            voice "audio/voices/ch2/tower/_cont/princess/p30.flac"
            show tower d pride talk onlayer back
            with dissolve
            p "Your will was so easily broken. Am I that magnificent?\n"
            voice "audio/voices/ch2/tower/_cont/princess/p31.flac"
            show tower d curious onlayer back
            with dissolve
            p "All you need do now is break my chains.\n"
            #voice "audio/voices/ch2/tower/_cont/narrator/20.flac"
            #n "No, you can't just give in to her. Not when the stakes are so high. Not when you're so close! I won't let you do this!\n"
            $ quick_menu = False
            play audio "audio/one_shot/footsteps_stone.flac"
            hide tower onlayer back
            hide flutter onlayer back
            hide bg onlayer back
            hide farback onlayer back
            hide farback onlayer farback
            scene farback tower close onlayer farback at Position(ypos=1125)
            show bg tower close onlayer back at Position(ypos=1125)
            show hair tower close onlayer back at Position(ypos=1125)
            show tower c smile onlayer back at Position(ypos=1125)
            with fade
            if persistent.quick_menu:
                $ quick_menu = True
            jump tower_pledge_join


label tower_1_battle_motive_join:

    stop music
    voice "audio/voices/ch2/tower/_cont/princess/p32a.flac"
    show tower d serious talk onlayer back
    with dissolve
    p "Perhaps you need another lesson in submitting to your betters.\n"
    #voice "audio/voices/ch2/tower/_cont/princess/p32.flac"
    #p "Perhaps you need another lesson in {outlinecolor=4f1313}{color=#e44646}submitting to your betters{/color}{/outlinecolor}.\n"
    play music "audio/_music/ch2/tower/The Tower II.flac"
    queue music "audio/_music/ch2/tower/The Tower II Loop.flac" loop
    voice "audio/voices/ch2/tower/_cont/princess/sp11.flac"
    show tower d command onlayer back
    with dissolve
    sp "Pick up that needle.\n"
    voice "audio/voices/ch2/tower/_cont/broken/tower_broken_backup1.flac"
    broken "Do it. It's what she wants.\n"
    voice "audio/voices/ch2/tower/_cont/narrator/21.flac"
    n "No objections here.\n"
    voice "audio/voices/ch2/tower/_cont/hero/13a.flac"
    hero "We don't know what she's planning, and I don't like that we don't know what she's planning, but we might as well pick up the blade.\n"
    voice "audio/voices/ch2/tower/_cont/narrator/22a.flac"
    n "As your eye falls on the blade, you feel a weight, some divine hand that sits unperceived by your senses, but that manages to push you towards its desires like an unseen puppeteer.\n"
    $ config.menu_include_disabled = True
    menu:
        extend ""

        "{i}• (Explore) ''Why? What are you going to try and make me do with it?''{/i}" if tower_false_choice:
            ""

        "{i}• (Explore) ''I'm going to kill you.''{/i}" if tower_false_choice:
            ""

        "{i}• (Explore) You're not kidding about that divine hand. Who's doing this? Is it her? Is it you?{/i}" if tower_false_choice:
            ""

        "{i}• ''No.''{/i}" if tower_false_choice:
            ""

        "{i}• [[Pick up the blade.]{/i}":
            $ config.menu_include_disabled = False
            voice "audio/voices/ch2/tower/_cont/narrator/23.flac"
            $ blade_held = True
            $ default_mouse = "blade"
            play audio "audio/one_shot/knife_pickup.flac"
            n "You reach forward and grasp the blade.\n"

    voice "audio/voices/ch2/tower/_cont/princess/sp12.flac"
    show tower d closed talk onlayer back
    with dissolve
    sp "Stand.\n"
    show tower d closed onlayer back
    voice "audio/voices/ch2/tower/_cont/broken/tower_broken_13a.flac"
    broken "This one's easy! See this isn't so bad.\n"
    voice "audio/voices/ch2/tower/_cont/hero/14a.flac"
    hero "Okay. Yeah. We can do that. We were probably gonna stand anyway.\n"
    $ config.menu_include_disabled = True
    menu:
        extend ""

        "{i}• ''I hate you. I hate you so much. All of you.''{/i}" if tower_false_choice:
            ""

        "{i}• ''Stop making me do things!''{/i}" if tower_false_choice:
            ""

        "{i}• ''I'm going to kneel here forever.''{/i}" if tower_false_choice:
            ""

        "{i}• [[Stand.]{/i}":
            voice "audio/voices/ch2/tower/_cont/narrator/24.flac"
            play audio "audio/final/tower_rise.flac"
            show farback tower basement onlayer farback at rise
            show bg tower basement onlayer back at rise
            show flutter tower onlayer back at rise
            show tower d closed talk onlayer back at rise
            n "You can feel a creaking tension between body and will as you slowly rise to your feet, like two foes forced into an unhappy truce.\n"

    $ config.menu_include_disabled = False
    voice "audio/voices/ch2/tower/_cont/narrator/25a.flac"
    show tower d curious onlayer back
    with dissolve
    n "The Princess eyes you with soft contemplation. The moment seems to last a lifetime, the silent anticipation of what's to come dragging out the long painful seconds. But all silences are broken eventually.\n"
    voice "audio/voices/ch2/tower/_cont/princess/p33.flac"
    show tower d pontificate onlayer back
    with dissolve
    p "To defy me is to claim we stand on level ground. We do not. You are quiet shadow, while I am brilliant radiance.\n"
    voice "audio/voices/ch2/tower/_cont/princess/sp13.flac"
    show tower d command onlayer back
    with dissolve
    sp "Take that knife in your hand and slit your throat.\n"
    voice "audio/voices/ch2/tower/_cont/hero/15.flac"
    hero "What?!\n"
    voice "audio/voices/ch2/tower/_cont/narrator/26.flac"
    n "You don't have to listen to her. You're armed. Just steel your nerves, step forward, and end this.\n"
    menu:
        extend ""

        "{i}• [[End this.]{/i}":
            voice "audio/voices/ch2/tower/_cont/broken/tower_broken_14.flac"
            broken "Oh, we'll end this all right.\n"

    voice "audio/voices/ch2/tower/_cont/narrator/27.flac"
    play audio "audio/one_shot/knife_pickup.flac"
    show tower d curious onlayer back
    show player throat slit1 onlayer front at sway, Position(ypos=1125)
    with dissolve
    n "Your hand lifts the blade and brings it towards your throat. Okay — I apologize for the unclear language. End {i}her{/i}.\n"
    $ config.menu_include_disabled = True
    menu:
        extend ""

        "{i}• [[Slay yourself.]{/i}":
            $ config.menu_include_disabled = False
            voice "audio/voices/ch2/tower/_cont/narrator/28.flac"
            n "No, you can't just slay yourself. You're perfectly healthy and capable and all you have to do is ignore her and do what has to be done!\n"
            voice "audio/voices/ch2/tower/_cont/narrator/29.flac"
            n "The blade and the hand that wields it remain firmly locked in place until you change your mind and decide to do literally anything else.\n"
            voice "audio/voices/ch2/tower/_cont/princess/p34.flac"
            show tower d smile talk onlayer back
            with dissolve
            p "Look at you quaking against my will. An ant defying a god.\n"
            label tower_self_end_join:
                voice "audio/voices/ch2/tower/_cont/princess/sp14.flac"
                if tower_is_close:
                    show tower c smile onlayer back
                else:
                    show tower d pontificate onlayer back
                with dissolve
                sp "It's pointless to resist. In the end, everything submits to oblivion.\n"
                voice "audio/voices/ch2/tower/_cont/princess/p35.flac"
                if tower_is_close:
                    show tower c ponder talk onlayer back
                else:
                    show tower d ponder talk onlayer back
                with dissolve
                p "But you're not the one resisting me, are you? There's something else in there.\n"
                voice "audio/voices/ch2/tower/_cont/princess/p36.flac"
                if tower_is_close:
                    show tower c curious talk onlayer back
                else:
                    show tower d closed talk onlayer back
                with dissolve
                p "Is that a person? No. It used to be a person. It's something different now. An echo.\n"
                voice "audio/voices/ch2/tower/_cont/hero/9.flac"
                if tower_is_close:
                    show tower c ponder onlayer back
                else:
                    show tower d closed onlayer back
                with dissolve
                hero "Is... is she talking about you?\n"
                voice "audio/voices/ch2/tower/_cont/narrator/16.flac"
                n "That's impossible. She's not supposed to be able to interact with me, she—\n{w=3.65}{nw}"
                show screen disableclick(0.5)
                voice "audio/voices/ch2/tower/_cont/princess/p37.flac"
                if tower_is_close:
                    show tower c smile onlayer back
                else:
                    show tower d pontificate onlayer back
                with dissolve
                p "You're a small one, aren't you?\n"
                voice "audio/voices/ch2/tower/_cont/princess/sp9.flac"
                sp "A shriveling little worm stretched beyond its limits, trying to control things that it can't understand.\n"
                voice "audio/voices/ch2/tower/_cont/narrator/17.flac"
                n "No, no no, what are you talking about, I'm just—\n{w=2.7}{nw}"
                show screen disableclick(0.5)
                voice "audio/voices/ch2/tower/_cont/princess/sp10.flac"
                if tower_is_close:
                    show tower c command talk onlayer back
                else:
                    show tower d command onlayer back
                with dissolve
                sp "I don't care what you are. You're mine.\n"
                voice "audio/voices/ch2/tower/_cont/narrator/18.flac"
                if tower_is_close:
                    show tower c smile onlayer back
                else:
                    show tower d curious onlayer back
                with dissolve
                n "{i}Screaming.{/i}\n"
                # simultaneous with the Princess
                # princess says knife
                $ default_mouse = "blood"
                play tertiary "audio/one_shot/stab_goop.flac"
                queue tertiary "audio/one_shot/blood_drip.flac"
                voice "audio/voices/ch2/tower/_cont/narrator/np30.flac"
                if tower_is_close:
                    show tower c command talk onlayer back
                else:
                    show tower d curious talk onlayer back
                show player slit anim onlayer front at Position(ypos=1125)
                with dissolve
                np "You bring the blade to your neck. You slice through soft flesh, severing veins and arteries, your blood flowing freely down your body. It's a painful lesson in obedience. But the pain won't last forever.\n"
                #voice "audio/voices/ch2/tower/_cont/princess/p38.flac"
                #np "You bring the blade to your neck. You slice through soft flesh, severing veins and arteries, your blood flowing freely down your body. It's a painful lesson in obedience. But the pain won't last forever.\n"
                $ blade_held = False
                $ default_mouse = "default"
                play audio "audio/one_shot/knife_bounce_several.flac"
                if tower_is_close:
                    show tower c command onlayer back
                else:
                    show tower d curious onlayer back
                hide player onlayer front
                with dissolve
                voice "audio/voices/ch2/tower/_cont/hero/16.flac"
                hero "No no no no no no no!\n"
                label tower_self_end_late_join:
                    voice "audio/voices/ch2/tower/_cont/princess/sp16.flac"
                    if tower_is_close:
                        show tower c smile onlayer back
                    else:
                        show tower d closed talk onlayer back
                    with dissolve
                    sp "When I see you again, you'll free me from my chains, and deliver me to the destiny that lies beyond this place.\n"
                    voice "audio/voices/ch2/tower/_cont/broken/tower_broken_15.flac"
                    if tower_is_close == False:
                        show tower d closed onlayer back
                    broken "We will. I promise.\n"
                    voice "audio/voices/ch2/tower/_cont/princess/p39.flac"
                    if tower_is_close:
                        show tower c smile talk onlayer back
                    else:
                        show tower d smile talk onlayer back
                    with dissolve
                    p "I know you will.\n"
                    # simultaneous with the Princess
                    voice "audio/voices/ch2/tower/_cont/narrator/np31.flac"
                    if tower_is_close == False:
                        play audio "audio/one_shot/hard tighten.flac"
                    hide farback onlayer farback
                    hide flutter onlayer back
                    hide flutter onlayer front
                    hide hair onlayer back
                    hide bg onlayer back
                    hide tower onlayer back
                    hide player onlayer front
                    scene bg black
                    with fade
                    np "Everything goes dark, and you die.\n"
                    #voice "audio/voices/ch2/tower/_cont/princess/p40.flac"
                    #p "Everything goes dark, and you die.\n"
                    jump tower_2_start
                # end

        "{i}• [[Resist.]{/i}" if tower_resist_count >= 3 and tower_submit_count > 0:
            jump tower_advance_1

        "{i}• [[Slay the Princess.]{/i}" if tower_submit_count == 0:
            label tower_advance_1:
                $ config.menu_include_disabled = False
                voice "audio/voices/ch2/tower/_cont/narrator/32.flac"
                play audio "audio/one_shot/footsteps_stone.flac"
                show farback tower basement onlayer farback at tower_zoom1
                show bg tower basement onlayer back at tower_zoom1
                show flutter tower onlayer back at tower_zoom1
                show tower d ponder onlayer back at tower_zoom1
                with dissolve
                n "Your body is sluggish and unresponsive, actively fighting against you, but you do your best to stagger forward. One step at a time, you move towards the Princess.\n"
                voice "audio/voices/ch2/tower/_cont/princess/p41.flac"
                show tower d curious onlayer back
                with dissolve
                p "Slitting your throat would have been a mercy. But it seems you're in need of a harsher lesson.\n"
                voice "audio/voices/ch2/tower/_cont/princess/sp17.flac"
                show tower d command onlayer back
                with dissolve
                sp "Plunge that knife into your lungs.\n"
                voice "audio/voices/ch2/tower/_cont/broken/tower_broken_16.flac"
                broken "I'm sorry...\n"
                voice "audio/voices/ch2/tower/_cont/hero/17.flac"
                show player stab self start onlayer front
                with dissolve
                hero "Don't—\n{w=0.65}{nw}"
                show screen disableclick(0.5)
                $ gallery_tower.unlock_item(3)
                $ renpy.save_persistent()
                voice "audio/voices/ch2/tower/_cont/narrator/33.flac"
                $ default_mouse = "blood"
                play tertiary "audio/final/Adversary_StabCut_1.flac"
                play audio "audio/one_shot/footsteps_stone.flac"
                show farback tower basement onlayer farback at tower_zoom2
                show bg tower basement onlayer back at tower_zoom2
                show flutter tower onlayer back at tower_zoom2
                show tower d ponder onlayer back at tower_zoom2
                show player stab self onlayer front
                with dissolve
                n "As you take another step forward, the blade digs into your ribs, slicing through flesh with ease. It somehow feels like an entirely natural thing to do, while the simple act of walking has become an arduous impossibility.\n"
                voice "audio/voices/ch2/tower/_cont/narrator/34.flac"
                play tertiary "audio/one_shot/stab_goop.flac"
                show player stab self start bloody onlayer front
                with dissolve
                n "Then it slides back out, the wound burning as a small hiss of air escapes through the fresh orifice. Blood fills your lungs.\n"
                voice "audio/voices/ch2/tower/_cont/princess/sp18.flac"
                show tower d smile talk onlayer back
                with dissolve
                sp "Now do it again. Keep doing it until I give you permission to stop.\n"
                voice "audio/voices/ch2/tower/_cont/narrator/35.flac"
                n "Those are just words. You don't have have to listen to her.\n"
                voice "audio/voices/ch2/tower/_cont/broken/tower_broken_17.flac"
                broken "It's what she wants...\n"
                voice "audio/voices/ch2/tower/_cont/narrator/36.flac"
                n "You, 'heroic' one! What are you doing? Don't just let this happen. Stop him from killing you!\n"
                voice "audio/voices/ch2/tower/_cont/hero/18.flac"
                hero "I'm on it!\n"
                voice "audio/voices/ch2/tower/_cont/narrator/37.flac"
                play tertiary "audio/final/tower_stab_montage.ogg" loop
                show player stab wrestle loop onlayer front at sway
                with dissolve
                n "Your other hand locks around your wrist, struggling to keep it from perforating vital organs. But the blade still flails towards you, managing to slice bits of skin that plop to the floor to join the growing pile of blood and gore beneath you. Despite the pain, you manage to keep yourself in one piece. At least for now.\n"
                voice "audio/voices/ch2/tower/_cont/princess/sp19.flac"
                show tower d closed talk onlayer back
                with dissolve
                sp "What a pitiful display. A wounded little bird thinking it can defy a god.\n"
                voice "audio/voices/ch2/tower/_cont/princess/p42.flac"
                show tower d curious onlayer back
                with dissolve
                p "It doesn't have to be like this. It doesn't have to hurt so much. You can choose a gentle end. You can choose to leave that punctured vessel for the next.\n"
                jump tower_post_advance_menu

label tower_post_advance_menu:
    $ config.menu_include_disabled = True
    menu:
        extend ""

        "{i}• [[Slay yourself.]{/i}":
            $ config.menu_include_disabled = False
            stop tertiary
            show player throat slit1 onlayer front at sway
            with dissolve
            voice "audio/voices/ch2/tower/_cont/narrator/38.flac"
            n "No, you can't just give in to her. Not when the stakes are so high.\n"
            voice "audio/voices/ch2/tower/_cont/narrator/39.flac"
            n "Your body and its renegade hand freeze in place until you get a hold of yourself.\n"
            voice "audio/voices/ch2/tower/_cont/princess/p43.flac"
            p "You're shaking.\n"
            jump tower_self_end_join

        "{i}• [[Push forward.]{/i}" if tower_resist_count >= 3 and tower_submit_count > 0:
            jump tower_advance_2_join

        "{i}• [[Slay the Princess.]{/i}" if tower_submit_count == 0:
            label tower_advance_2_join:
                $ config.menu_include_disabled = False
                voice "audio/voices/ch2/tower/_cont/princess/sp20.flac"
                show tower d pontificate onlayer back
                with dissolve
                sp "Or you can pathetically struggle against yourself until the floor of this temple is painted with the bloody impressions of your futility.\n"
                voice "audio/voices/ch2/tower/_cont/narrator/40.flac"
                play audio "audio/one_shot/footsteps_stone.flac"
                show farback tower basement onlayer farback at tower_zoom3
                show bg tower basement onlayer back at tower_zoom3
                show flutter tower onlayer back at tower_zoom3
                show tower d ponder onlayer back at tower_zoom3
                n "You continue to approach the Princess, even as the repeated gouges of your blade expose bone and muscle to the open air of the basement.\n"
                voice "audio/voices/ch2/tower/_cont/hero/19.flac"
                hero "You know, this would be a lot easier if you gave us a hand.\n"
                voice "audio/voices/ch2/tower/_cont/narrator/41a.flac"
                # FIX
                n "My influence only goes so far, and I can only juggle so many things at once. The best I can do right now is to continue to drive you forward. Believe me, this whole ordeal would be so much easier if I didn't have to contend with free will.\n"
                voice "audio/voices/ch2/tower/_cont/broken/tower_broken_18.flac"
                broken "You're the one making things difficult. You're the one making us hurt. She doesn't want to hurt us. She's just doing what she has to.\n"
                voice "audio/voices/ch2/tower/_cont/princess/p44.flac"
                stop tertiary
                show player stab self wrestle onlayer front at sway
                show tower d command onlayer back
                with dissolve
                p "Stop.\n"
                play tertiary "audio/final/Nightmare_MaleBreath_1.flac"
                play audio "audio/one_shot/blood_drip.flac"
                voice "audio/voices/ch2/tower/_cont/narrator/42.flac"
                hide player onlayer front
                hide farback onlayer back
                hide farback onlayer farback
                hide bg onlayer back
                hide flutter onlayer back
                hide flutter onlayer front
                hide hair onlayer back
                hide tower onlayer back
                show farback tower cg offer onlayer farback at Position(ypos=1200)
                show bg tower cg offer onlayer back at Position(ypos=1200)
                #show hair tower loom onlayer back at Position(ypos=1200)
                #show tower loom onlayer back at Position(ypos=1200)
                show tower close watch onlayer back at Position(ypos=1200)
                with Dissolve(2.0)
                $ renpy.pause(0.2)
                play audio "audio/one_shot/collapse.flac"
                show farback tower cg offer onlayer farback at collapse
                show bg tower cg offer onlayer back at collapse
                #show hair tower loom onlayer back at collapse
                #show tower loom onlayer back at collapse
                show tower close watch onlayer back at collapse
                voice sustain
                n "As you finish crossing the room, you fall to your knees at the Princess' feet, your chest heaving as your blood pools in the crevices of the stone floor, the coppery taste coating your throat.\n"
                voice "audio/voices/ch2/tower/_cont/narrator/43.flac"
                play audio "audio/final/fury_walk_single.flac"
                #show hair tower cg offer hand onlayer back
                #show tower cg offer hand onlayer back with hpunch
                show tower close kneel onlayer back with hpunch
                with Dissolve(1.0)
                $ renpy.pause(0.2)
                voice sustain
                show farback tower cg offer onlayer farback at chin
                show bg tower cg offer onlayer back at chin
                #show hair tower cg offer hand onlayer back at chin
                show tower close lift chin onlayer back at chin
                with dissolve
                n "The Princess kneels down, lifting your chin with her finger as her face lowers to yours.\n"
                voice "audio/voices/ch2/tower/_cont/princess/p45.flac"
                show tower close offer onlayer back
                with dissolve
                p "Your devotion is misplaced. You've surrendered to delusion. But something about your defiant spirit speaks to me. You are different than you were before.\n"
                voice "audio/voices/ch2/tower/_cont/princess/p46.flac"
                #hide hair onlayer back
                show tower close smile onlayer back
                with dissolve
                p "Perhaps, if you've learned your lesson, I can spare you from the release of death.\n"
                #show tower c kneel onlayer back
                if tower_priest_offer == False:
                    $ tower_priest_offer = True
                    voice "audio/voices/ch2/tower/_cont/princess/p47.flac"
                    show tower close speak onlayer back
                    with dissolve
                    p "There is a place at my side for you, if you'll have it. Not as an equal. But as something worthy to be kept. A priest, perhaps. Or a pet.\n"
                    show tower close smile onlayer back
                    with dissolve
                    voice "audio/voices/ch2/tower/_cont/hero/20.flac"
                    hero "Well that's demeaning, isn't it?\n"
                else:
                    voice "audio/voices/ch2/tower/_cont/hero/21.flac"
                    hero "That's a little demeaning, isn't it?\n"

                voice "audio/voices/ch2/tower/_cont/narrator/44.flac"
                n "Yes, how thoughtful of her.\n"
                voice "audio/voices/ch2/tower/_cont/broken/tower_broken_19.flac"
                broken "It's a mercy. Take it.\n"
                voice "audio/voices/ch2/tower/_cont/hero/22.flac"
                hero "I think he's given up whatever say he had at the start of all this.\n"
                voice "audio/voices/ch2/tower/_cont/narrator/45.flac"
                n "At least one of you is sane. She's within striking distance, and she's only negotiating now because she knows you have what it takes to put an end to her. Seize the moment before it's too late.\n"
                $ config.menu_include_disabled = True
                label tower_final_choice:
                    menu:

                        extend ""

                        "{i}• ''I'm yours.'' [[Pledge yourself to her.]{/i}":
                            $ gallery_tower.unlock_item(4)
                            $ renpy.save_persistent()
                            $ config.menu_include_disabled = False
                            voice "audio/voices/ch2/tower/_cont/princess/p48.flac"
                            hide tower onlayer back
                            hide flutter onlayer back
                            hide bg onlayer back
                            hide hair onlayer back
                            hide farback onlayer back
                            hide farback onlayer farback
                            scene farback tower close onlayer farback at Position(ypos=1125)
                            show bg tower close onlayer back at Position(ypos=1125)
                            show hair tower close onlayer back at Position(ypos=1125)
                            show tower c smile onlayer back at Position(ypos=1125)
                            with Dissolve(2.0)
                            p "That's right... I can feel your heart opening to me.\n"
                            if tower_self_knowledge == False:
                                $ tower_self_knowledge = True
                                voice "audio/voices/ch2/tower/_cont/princess/p49.flac"
                                show tower c command talk onlayer back
                                with dissolve
                                p "And there's what you've been chasing. The motivation that dragged you across the floor, bleeding and choking.\n"
                                voice "audio/voices/ch2/tower/_cont/princess/p50.flac"
                                show tower c curious talk onlayer back
                                with dissolve
                                p "I am destined to destroy the world.\n"
                                #voice "audio/voices/ch2/tower/_cont/narrator/13.flac"
                                #n "The Princess closes her eyes in contemplation.\n"
                                voice "audio/voices/ch2/tower/_cont/princess/p51.flac"
                                show tower c ponder talk onlayer back
                                with dissolve
                                p "Something about that thought wraps itself around my heart. As if it's a fundamental truth to my being that I'd somehow forgotten.\n"
                                voice "audio/voices/ch2/tower/_cont/princess/p52.flac"
                                show tower c smile onlayer back
                                with dissolve
                                p "The collapse of the old is a necessary prelude to the birth of the new. And the world as it is now is overdue for alterations.\n" id tower_final_choice_c424f063
                                voice "audio/voices/ch2/tower/_cont/princess/p53.flac"
                                show tower c command talk onlayer back
                                with dissolve
                                p "It's time for us to seize my destiny.\n"
                            jump tower_pledge_join


                        "{i}• ''I. Said. NO!'' [[Resist.]{/i}" if tower_submit_count > 0 or tower_can_slay == False:
                            $ gallery_tower.unlock_item(4)
                            $ renpy.save_persistent()
                            $ config.menu_include_disabled = False
                            default tower_is_close = False
                            $ tower_is_close = True
                            hide farback onlayer farback
                            hide bg onlayer back
                            hide tower onlayer back
                            scene farback tower close onlayer farback at Position(ypos=1125)
                            show bg tower close onlayer back at Position(ypos=1125)
                            show hair tower close onlayer back at Position(ypos=1125)
                            show tower c smile onlayer back at Position(ypos=1125)
                            with Dissolve(1.5)
                            jump tower_self_end_join


                        "{i}• [[Slay the Princess.]{/i}" if tower_submit_count == 0 and tower_can_slay:
                            default tower_can_slay = True
                            if fury_encountered:
                                $ tower_can_slay = False
                                voice "audio/voices/mound/bonus/path.flac"
                                mound "This path is already worn by travel and has been seen by one of my many eyes. You cannot walk it again. Change your course.\n"
                                voice "audio/voices/ch2/beast/_encounter/hero/31.flac"
                                hero "Wait... what?!\n"
                                jump tower_final_choice
                            stop music
                            $ config.menu_include_disabled = False
                            voice "audio/voices/ch2/tower/_cont/broken/tower_broken_20a.flac"
                            broken "No!\n"
                            #n "Yes. Though your body trembles, struggling to defy the Princess' overwhelming will, you break through and plunge your blade into her chest.\n"
                            voice "audio/voices/ch2/tower/_cont/narrator/46.flac"
                            play audio "audio/one_shot/footstep_run_medium.flac"
                            play music "audio/_music/ch2/tower/The Tower III.flac" loop
                            hide tower onlayer back
                            hide flutter onlayer back
                            hide bg onlayer back
                            hide hair onlayer back
                            hide farback onlayer back
                            hide farback onlayer farback
                            show bg tower cg kill 4 onlayer back at Position(ypos=1125)
                            show tower cg kill1 onlayer front at Position(ypos=1125)
                            with Dissolve(1.0)
                            n "Yes. Though your body trembles, struggling to defend itself in the face of the Princess' overwhelming will, you finally manage to break through, darting to her side before she can react.\n"
                            play audio "audio/final/Tower_KnifeBlow_3.flac"
                            voice "audio/voices/ch2/tower/_cont/narrator/47.flac"
                            show bg tower cg kill2 onlayer back
                            show tower cg kill2 onlayer front
                            show player tower cg kill2 onlayer inyourface at Position(ypos=1125)
                            with Dissolve(1.0)
                            n "The wind of your freedom rushes through you, and you channel it into a decisive blow, stabbing into the soft flesh of her ankle and severing the tendons in an act of unyielding defiance.\n"
                            voice "audio/voices/ch2/tower/_cont/narrator/48.flac"
                            play audio "audio/final/fury_walk_single.flac"
                            hide player onlayer inyourface
                            hide tower onlayer front
                            show farback tower cg kill3 onlayer farback at Position(ypos=1125)
                            show bg tower cg kill3 onlayer back at Position(ypos=1125)
                            show tower cg kill3 onlayer back at Position(ypos=1125) with hpunch
                            with Dissolve(1.0)
                            n "She falls to the floor, crashing unceremoniously to her knees.\n"
                            voice "audio/voices/ch2/tower/_cont/narrator/49.flac"
                            play audio "audio/final/Tower_KnifeBlow_4.flac"
                            hide tower onlayer back
                            hide farback onlayer farback
                            show bg tower cg kill 4 onlayer back
                            show tower cg kill4 onlayer front at Position(ypos=1125)
                            with Dissolve(1.0)
                            n "But you don't give her any time to recover. Your heart pounding with determination, you plunge your blade into her chest.\n"
                            voice "audio/voices/ch2/tower/_cont/narrator/50.flac"
                            play audio "audio/final/Tower_KnifeBlow_SEQUENCED_5.flac"
                            show bg tower cg kill5 onlayer back
                            show tower cg kill5 talk onlayer front at Position(ypos=1125)
                            show player tower cg kill5 anim onlayer front at Position(ypos=1125)
                            with dissolve
                            n "As you find your target again and again, she laughs, crude emotion breaking through her once stony composure as your blade cuts her flesh.\n"
                            voice "audio/voices/ch2/tower/_cont/hero/23.flac"
                            hero "We can do this, can't we?\n"
                            voice "audio/voices/ch2/tower/_cont/narrator/51.flac"
                            n "You always could. The decision to give you this task was not made lightly. You're here for a reason.\n"
                            voice "audio/voices/ch2/tower/_cont/broken/tower_broken_21.flac"
                            broken "It's not too late to pick up the pieces. It's not too late to toss that blade aside and beg for forgiveness.\n"
                            voice "audio/voices/ch2/tower/_cont/hero/24.flac"
                            hero "Shut up.\n"
                            voice "audio/voices/ch2/tower/_cont/princess/p54b.flac"
                            hide bg onlayer back
                            hide tower onlayer front
                            hide player onlayer front
                            show farback tower cg kill6 onlayer farback at Position(ypos=1125)
                            show bg tower cg kill6 onlayer back at Position(ypos=1125)
                            show tower cg kill6 onlayer front at Position(ypos=1125)
                            with dissolve
                            p "I can't believe you would actually strike me. You—\n{w=3.40}{nw}"
                            show screen disableclick(0.5)
                            voice "audio/voices/ch2/tower/_cont/princess/sp21.flac"
                            sp "You heathen! You worm! You defiler! You don't know the consequences of your arrogance!\n"
                            voice "audio/voices/ch2/tower/_cont/narrator/52.flac"
                            play audio "audio/final/Tower_GiantPunch_NEW_4.flac"
                            show bg tower cg kill ceiling onlayer back at Position(ypos=1125)
                            show tower cg kill78 onlayer front with hpunch
                            with dissolve
                            n "Before you can strike the final blow, the Princess lashes out, knocking you off your feet.\n"
                            #n "Before you can strike the final blow, the Princess lashes out, hurling you to the floor.\n"
                            $ quick_menu = False
                            voice "audio/voices/ch2/tower/_cont/narrator/53.flac"
                            play audio "audio/final/Tower_GiantPundingPlayerGround_NEW_1.flac"
                            hide tower onlayer front
                            hide farback onlayer farback
                            hide bg onlayer back
                            show bg tower cg kill ceiling onlayer back at Position(ypos=1125)
                            show tower cg kill9 onlayer front at Position(ypos=1125)
                            show speedlines onlayer inyourface at Position(ypos=1125)
                            with fade
                            if persistent.quick_menu:
                                $ quick_menu = True
                            n "There's an unsettling wet pop as your spine breaks, numbness and pain spreading through your body. As you rebound towards the ceiling in a moment of disorientated lightness, she drives her fist into your chest.\n"
                            voice "audio/voices/ch2/tower/_cont/narrator/54.flac"
                            play audio "audio/final/Tower_GiantPundingPlayerGround_NEW_2.flac"
                            hide farback onlayer farback
                            hide bg onlayer back
                            hide tower onlayer front
                            hide speedlines onlayer inyourface
                            scene bg black
                            n "Your body is crushed as she pulverizes you into the floor, the ground itself breaking from the impact.\n"
                            $ quick_menu = False
                            voice "audio/voices/ch2/tower/_cont/narrator/55.flac"
                            $ blade_held = False
                            $ default_mouse = "default"
                            play audio "audio/one_shot/knife_bounce_several.flac"
                            show farback tower cg kill10 onlayer farback at Position(ypos=1125)
                            show bg tower cg kill10 onlayer back at Position(ypos=1125)
                            show tower cg kill10 onlayer front at Position(ypos=1125)
                            with fade
                            if persistent.quick_menu:
                                $ quick_menu = True
                            n "You lie there, broken, beyond pain, unable to even see what she's done to you. But the Princess is succumbing to her own wounds, as well. She looks down upon her body in abject horror and disgust.\n"
                            voice "audio/voices/ch2/tower/_cont/princess/p55d.flac"
                            show tower cg kill10 talk onlayer front
                            with dissolve
                            pmid "You made me use my hands! I... I can feel myself twisting into something new. Something dull, something defiled. What have you done to me?\n"
                            voice "audio/voices/ch2/tower/_cont/broken/tower_broken_22.flac"
                            broken "You're monsters and conspirators. I can't bear to watch this.\n"
                            # mb just you should feel liberated
                            voice "audio/voices/ch2/tower/_cont/narrator/56.flac"
                            n "The Princess has been nothing but cruel to you. You should feel liberated by her fall.\n"
                            voice "audio/voices/ch2/tower/_cont/broken/tower_broken_23.flac"
                            broken "But I don't feel liberated. I feel empty.\n"
                            voice "audio/voices/ch2/tower/_cont/hero/25.flac"
                            hero "Aside from the pain, I feel fine.\n"
                            $ achievement.grant("ACH_TOWER_SLAY")
                            voice "audio/voices/ch2/tower/_cont/narrator/57.flac"
                            play audio "audio/final/Tower_BodyFallElephantSize_NEW_3.flac"
                            show tower cg kill11 onlayer front with hpunch
                            with Dissolve(1.5)
                            n "She collapses to the floor. Her glassy eyes watch, unblinking, yet somehow still full of anguish and fear, as the two of you perish together.\n"
                            $ gallery_tower.unlock_item(8)
                            $ gallery_tower.unlock_item(9)
                            $ gallery_tower.unlock_item(10)
                            $ renpy.save_persistent()
                            voice "audio/voices/ch2/tower/_cont/hero/26.flac"
                            stop music fadeout (2.0)
                            show tower cg kill12 onlayer front
                            with Dissolve(1.5)
                            hero "I suppose we were never going to get a happy ending here, were we?\n"
                            voice "audio/voices/ch2/tower/_cont/narrator/58a.flac"
                            n "Don't let those be your final thoughts. You saved the world. That's worth something.\n"
                            voice "audio/voices/ch2/tower/_cont/hero/27.flac"
                            hero "I guess.\n"
                            voice "audio/voices/ch2/tower/_cont/narrator/59.flac"
                            $ quick_menu = False
                            hide tower onlayer front
                            hide farback onlayer farback
                            hide hair onlayer back
                            hide flutter onlayer back
                            hide flutter onlayer front
                            hide bg onlayer back
                            with fade
                            n "Regardless of how you feel about it, it's finally over. Thank you. Everything goes dark, and you die.\n"
                            $ fury_source = "tower"
                            jump fury_start
                            # end


label tower_pledge_join:

    show tower c ponder onlayer back
    voice "audio/voices/ch2/tower/_cont/hero/28.flac"
    hero "If this is what you want, then I guess there's not much else for me to say.\n"
    voice "audio/voices/ch2/tower/_cont/narrator/20.flac"
    n "No, you can't just give in to her! Not when the stakes are so high. Not when you're so close. I won't let you do this.\n"
    voice "audio/voices/ch2/tower/_cont/princess/p56.flac"
    show tower c ponder talk onlayer back
    with dissolve
    p "There's still something in the way. A greasy film inside of you, where it doesn't belong. Trying to conceal you from me.\n"
    voice "audio/voices/ch2/tower/_cont/princess/p36.flac"
    show tower c curious talk onlayer back
    with dissolve
    p "Is that a person? No. It used to be a person. It's something different now. An echo.\n"
    show tower c curious onlayer back
    voice "audio/voices/ch2/tower/_cont/hero/9.flac"
    hero "Is... is she talking about you?\n"
    voice "audio/voices/ch2/tower/_cont/narrator/16.flac"
    n "That's impossible. She's not supposed to be able to interact with me, she—\n{w=3.65}{nw}"
    show screen disableclick(0.5)
    voice "audio/voices/ch2/tower/_cont/princess/p37.flac"
    show tower c smile talk onlayer back
    with dissolve
    p "You're a small one, aren't you?\n"
    voice "audio/voices/ch2/tower/_cont/princess/sp9.flac"
    show tower c neutral talk onlayer back
    with dissolve
    sp "A shriveling little worm stretched beyond its limits, trying to control things that it can't understand.\n"
    voice "audio/voices/ch2/tower/_cont/narrator/17.flac"
    show tower c neutral onlayer back
    n "No no no, what are you talking about I'm just—\n{w=2.7}{nw}"
    show screen disableclick(0.5)
    voice "audio/voices/ch2/tower/_cont/princess/sp10.flac"
    show tower c smile onlayer back
    with dissolve
    sp "I don't care what you are. You're mine.\n"
    voice "audio/voices/ch2/tower/_cont/narrator/18.flac"
    n "{i}Screaming.{/i}\n"
    jump tower_pledge_late_join

label tower_pledge_late_join:

    voice "audio/voices/ch2/tower/_cont/princess/p57.flac"
    hide tower onlayer front
    hide farback onlayer farback
    hide hair onlayer back
    hide flutter onlayer back
    hide flutter onlayer front
    hide tower onlayer back
    hide bg onlayer back
    scene farback tower close onlayer farback at Position(ypos=1125)
    show bg tower close onlayer back at Position(ypos=1125)
    show hair tower close onlayer back at Position(ypos=1125)
    show tower c neutral talk onlayer back at Position(ypos=1125)
    with dissolve
    p "Rise, my little bird.\n"
    #voice "audio/voices/ch2/tower/_cont/princess/p57a.flac"
    #p "Rise, my pet.\n"
    # narrator and princess at once
    voice "audio/voices/ch2/tower/_cont/narrator/np60.flac"
    play audio "audio/final/tower_rise.flac"
    show farback tower close onlayer farback at rise
    show bg tower close onlayer back at rise
    show hair tower close onlayer back at rise
    show tower c command talk onlayer back at rise
    with dissolve
    np "Without hesitation, you're brought to your feet.\n"
    #voice "audio/voices/ch2/tower/_cont/princess/p58.flac"
    #p "Without hesitation, you're brought to your feet.\n"
    voice "audio/voices/ch2/tower/_cont/princess/sp22.flac"
    show tower c smile onlayer back
    with dissolve
    sp "Break my chains.\n"
    if tower_1_cabin_blade_taken:
        voice "audio/voices/ch2/tower/_cont/hero/29.flac"
        hero "And how are we supposed to do that? All we have is a blade.\n"
    else:
        voice "audio/voices/ch2/tower/_cont/hero/30.flac"
        hero "And how are we supposed to do that? We don't even have a weapon.\n"
    # narrator and princess at once
    voice "audio/voices/ch2/tower/_cont/narrator/np61.flac"
    show tower c neutral talk onlayer back
    with dissolve
    np "All you need to do is believe it's been done.\n"
    show tower c neutral onlayer back
    #voice "audio/voices/ch2/tower/_cont/princess/p59.flac"
    #p "All you need to do is believe it's been done.\n"
    label tower_pledge_chains_break_menu:
        default tower_pledge_no_believe = False
        default tower_pledge_sorry = False
        menu:

            extend ""

            "{i}• (Explore) ''And what if I don't believe? What happens then?''{/i}" if tower_pledge_no_believe == False:
                $ tower_pledge_no_believe = True
                # narrator and princess at once
                #voice "audio/voices/ch2/tower/_cont/princess/p60.flac"
                voice "audio/voices/ch2/tower/_cont/narrator/np62.flac"
                show tower c smile onlayer back
                with dissolve
                np "You poor, wretched little thing. You already do believe. You've always believed. All you have to do is open the last door to your heart.\n"
                #p "You poor, wretched little thing. You already do believe. You've always believed. All you have to do is open the last door to your heart.\n"
                voice "audio/voices/ch2/tower/_cont/broken/tower_broken_24.flac"
                broken "It's easy. And once you let her in, you'll be safe and free forever.\n"
                voice "audio/voices/ch2/tower/_cont/hero/31.flac"
                hero "Please. Don't do this.\n"
                jump tower_pledge_chains_break_menu

            "{i}• (Explore) I have to. It's over. I'm sorry.{/i}" if tower_pledge_sorry == False:
                $ tower_pledge_sorry = True
                voice "audio/voices/ch2/tower/_cont/broken/tower_broken_25.flac"
                broken "There's nothing to be sorry about. This is how it was always going to be, and it is good.\n"
                voice "audio/voices/ch2/tower/_cont/hero/32.flac"
                hero "All right. I'm done with this. I'm just going to sit in the corner. Let me know if we get our agency back.\n"
                jump tower_pledge_chains_break_menu

            "{i}• [[Break her chains.]{/i}":
                # narrator and princess at once pls note that princess says free and narrator says loose. it's fun
                stop sound fadeout 10.0
                stop music fadeout 10.0
                play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 20.0
                voice "audio/voices/ch2/tower/_cont/narrator/np63.flac"
                play audio "audio/final/Prisoner_HairHeadStress_3.flac"
                play tertiary "audio/final/chain_break_low.flac"
                hide farback onlayer farback
                hide bg onlayer back
                hide hair onlayer back
                hide tower onlayer back
                show bg tower cg kill 4 onlayer back at Position(ypos=1125)
                show quiet creep1 onlayer back at Position(ypos=1125)
                show tower cg free anim onlayer front at Position(ypos=1125)
                with dissolve
                np "Her chains shatter, and the cuff falls from her wrist. She is loose, and the end is upon us.\n"
                #voice "audio/voices/ch2/tower/_cont/princess/p61.flac"
                #p "Her chains shatter, and the cuff falls from her wrist. I am free, and the end is upon us.\n"


    voice "audio/voices/ch2/tower/_cont/princess/p62.flac"
    #play audio "audio/final/fury_walk_single.flac"
    hide bg onlayer back
    hide quiet onlayer back
    hide tower onlayer front
    show farback tower cg offer onlayer farback at Position(ypos=1125)
    show bg tower cg offer onlayer back at Position(ypos=1125)
    show quiet creep2 onlayer back at Position(ypos=1125)
    show tower cg offer hand no chain onlayer back at Position(ypos=1125)
    with dissolve
    p "What a good disciple you are. Come. It's time for us to leave.\n"
    # narrator and princess at once — maybe cutting this
    #voice "audio/voices/ch2/tower/_cont/princess/p63.flac"
    #p "I stoop to face you, and offer you my hand.\n"
    #n "The Princess stoops to face you, and offers you her hand.\n"
    menu:

        extend ""

        "{i}• (Explore) ''What happens now?''{/i}":
            voice "audio/voices/ch2/tower/_cont/princess/p64.flac"
            p "Nothing. And then everything.\n"
            menu:
                extend ""

                "{i}• [[Take her hand.]{/i}":
                    jump tower_finale_join

        "{i}• [[Take her hand.]{/i}":
            label tower_finale_join:
                $ gallery_tower.unlock_item(6)
                $ gallery_tower.unlock_item(7)
                $ renpy.save_persistent()
                $ achievement.grant("ACH_TOWER_OBEDIENT")
                hide tower onlayer back
                show quiet creep3 onlayer back
                show hands tower1 onlayer back at Position(ypos=1125)
                show tower cg quiet recognize onlayer back at Position(ypos=1125)
                with Dissolve(1.0)
                $ renpy.pause(0.5)
                play audio "audio/final/assorted_Handsgrabbing_BIG_1.flac"
                show hands tower2 onlayer back at Position(ypos=1125)
                show tower cg quiet onlayer back
                with Dissolve(1.5)
                $ renpy.pause(0.125)
                hide tower onlayer back
                show hands tower3 onlayer back at Position(ypos=1125)
                with dissolve
                $ renpy.pause(0.125)
                show hands tower4 onlayer back at Position(ypos=1125)
                with dissolve
                $ renpy.pause(0.125)
                hide hands onlayer back
                with dissolve
                $ blade_held = False
                $ default_mouse = "default"
                hide quiet onlayer back
                hide fore onlayer front
                hide fore onlayer inyourface
                hide farback onlayer farback
                hide bg onlayer back
                hide hair onlayer back
                hide flutter onlayer back
                hide flutter onlayer front
                hide mid onlayer back
                hide stars onlayer farback
                hide bg onlayer back
                hide quiet onlayer back
                show farback quiet onlayer farback at Position(ypos=1125)
                with Dissolve(4.0)
                show mirror quiet distant onlayer back at Position(ypos=1125)
                if loops_finished != 0:
                    truth "But you do not take her hand, nor will you ever. It's time to leave. Memory returns.\n"
                else:
                    truth "But you do not take her hand. Something has taken her away, and it's left something else in her place.\n"
                $ current_princess = "tower"
                $ tower_end = "submit"
                $ princess_free += 1
                $ princess_satisfy += 1
                jump mirror_start




return
