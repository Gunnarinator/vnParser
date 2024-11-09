label basement_1_empty_start:



    play sound "audio/looping/ambient_basement_interior.ogg" loop
    scene bg basement stairs onlayer farback at Position(ypos=1125)
    show front basement stairs onlayer farback at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    voice "audio/voices/ch1/shared/narrator/ch1_share_n_1.flac"
    n "The door to the basement creaks open, revealing a staircase faintly illuminated by an unseen light in the room below. This is an oppressive place. The air feels heavy and damp, a hint of rot filtering from the ancient wood. If the Princess really lives here, slaying her is probably doing her a favor.\n"
    voice "audio/voices/ch1/empty/narrator/empty_n_1.flac"
    n "Her voice softly carries up the stairs.\n"
    voice "audio/voices/ch1/empty/princess/empty_p_1.flac"
    p "H-hello? Is someone there?\n"
    voice "audio/voices/ch1/empty/hero/empty_h_1.flac"
    hero "It's hypnotizing. It's the kind of voice you only have to hear once to remember it for the rest of your life.\n"
    voice "audio/voices/ch1/empty/narrator/empty_n_2.flac"
    n "Don't let it fool you. It's all part of the manipulation. You're playing a dangerous game by coming here unarmed.\n"
    default basement_1_empty_kill_joke = False
    default basement_1_empty_save_explore = False
    default basement_1_empty_save_lie_explore = False
    default basement_1_empty_arm_loss_known = False
    default basement_1_empty_wounded = False
    menu:
        extend ""

        "{i}• ''Hi!''{/i}":
            voice "audio/voices/ch1/empty/princess/empty_p_2.flac"
            p "Don't be a stranger. It's been so long since I've had any visitors. Please, come downstairs.\n"

        "{i}• ''Just checking in on you.''{/i}":
            voice "audio/voices/ch1/empty/princess/empty_p_3.flac"
            p "You are? It's been so long since anyone's come down here. I was starting to think they'd forgotten about me.\n"

        "{i}• ''I'm here to save you!''{/i}" if damsel_encountered == False or witch_encountered == False:
            $ basement_1_empty_save_explore = True
            voice "audio/voices/ch1/empty/narrator/empty_n_3.flac"
            n "How many times do I have to tell you how dangerous letting her out of here would be before it finally sinks in?\n" id basement_1_empty_start_d1cc3074
            voice "audio/voices/ch1/empty/princess/empty_p_4.flac"
            p "Wait, really?! You're here to rescue me? I was starting to think I'd be stuck down here forever!\n"
            voice "audio/voices/ch1/empty/princess/empty_p_5.flac"
            p "Come downstairs! I want to see the face of my rescuer.\n"

        "{i}• (Lie) ''I'm here to save you!''{/i}":
            $ basement_1_empty_save_explore = True
            $ basement_1_empty_save_lie_explore = True
            #re-read maybe
            voice "audio/voices/ch1/empty/princess/empty_p_4.flac"
            p "Wait, really?! You're here to rescue me? I was starting to think I'd be stuck down here forever!\n"
            voice "audio/voices/ch1/empty/narrator/empty_n_4.flac"
            n "I see, you're trying to get her to lower her guard. It's a gamble, but it might work.\n"
            voice "audio/voices/ch1/empty/princess/empty_p_5.flac"
            p "Come downstairs! I want to see the face of my rescuer.\n"

        "{i}• ''Hey, I think I'm here to slay you?''{/i}":
            $ basement_1_empty_kill_joke = True
            voice "audio/voices/ch1/empty/princess/empty_p_6.flac"
            p "Y-you must have the wrong address.\n"
            voice "audio/voices/ch1/empty/narrator/empty_n_5.flac"
            n "Great job, you've given away the element of surprise. Good luck, hero.\n"

        "{i}• Continue down the stairs.{/i}":
            voice "audio/voices/ch1/empty/narrator/empty_n_6.flac"
            n "Good. You're still listening to reason. It would be better if you had a weapon, but you may still be able to do what needs to be done.\n"

    play audio "audio/one_shot/footsteps_creaky.flac"
    $ quick_menu = False
    $gallery_zch1.unlock_item(4)
    $renpy.save_persistent()
    hide bg basement stairs onlayer farback at Position(ypos=1125)
    hide front basement stairs onlayer farback at Position(ypos=1125)
    with fade
    scene bg black with fade
    scene bg basement distant onlayer farback at Position(ypos=1125)
    show back basement distant onlayer back at Position(ypos=1125)
    show princess d down onlayer back at Position(ypos=1125)
    with fade
    show princess d neutral onlayer back at Position(ypos=1125) with dissolve
    if persistent.quick_menu:
        $ quick_menu = True
    voice "audio/voices/ch1/empty/narrator/empty_n_7.flac"
    n "You walk down the stairs and lock eyes with the Princess. There's a heavy chain around her wrist, binding her to the far wall of the basement.\n"
    voice "audio/voices/ch1/empty/hero/empty_h_2.flac"
    show princess d questioning onlayer back with dissolve
    hero "She's beautiful. How could someone like this be a threat to anyone?\n"
    voice "audio/voices/ch1/empty/narrator/empty_n_8.flac"
    n "I am {i}begging{/i} you to stay focused. There's a lot riding on you here.\n"
    if basement_1_empty_kill_joke:
        show princess d glance talk onlayer back with dissolve
        voice "audio/voices/ch1/empty/princess/empty_p_7.flac"
        p "H—hi. You were joking about coming here to kill me, right? D-do you think you could get me out of these chains?\n"

    elif basement_1_empty_save_explore:
        voice "audio/voices/ch1/empty/princess/empty_p_8.flac"
        show princess d questioning talk onlayer back with dissolve
        p "Hi! I can't believe you're here, I've been waiting for something like this to happen {i}forever{/i}.\n"
        voice "audio/voices/ch1/empty/princess/empty_p_9.flac"
        show princess d glance talk onlayer back with dissolve
        p "...\nI hope you brought something to deal with these chains.\n"
        show princess d glance onlayer back with dissolve
        if basement_1_empty_save_lie_explore == False:
            voice "audio/voices/ch1/empty/narrator/empty_n_9.flac"
            n "Don't do it. If she gets out of those chains we're all one step closer to The End.\n"
        else:
            voice "audio/voices/ch1/empty/narrator/empty_n_10.flac"
            n "You were lying when you said you were here to rescue her, but regardless of your intentions, breaking her out of those chains would be a big mistake. Don't even try it.\n"

    else:
        voice "audio/voices/ch1/empty/princess/empty_p_10.flac"
        show princess d neutral onlayer back with dissolve
        p "Hi! Do you think you can get me out of these chains?\n"

    default what_would_you_do_1 = False
    menu:
        extend ""

        "{i}• ''Hold on. Let's talk a bit first...''{/i}":
            show princess d haughty talk onlayer back with dissolve
            voice "audio/voices/ch1/empty/princess/empty_p_11.flac"
            p "O... kay.\n"
            play audio "audio/one_shot/footsteps_hike_short.flac"
            $ renpy.free_memory()
            $ quick_menu = False
            hide princess d haughty talk onlayer back
            hide bg basement distant onlayer farback
            hide back basement distant onlayer back
            with fade
            show bg basement close onlayer farback at Position(ypos=1125)
            show princess c innocent onlayer back at Position(ypos=1125)
            with fade
            if persistent.quick_menu:
                $ quick_menu = True
            label basement_1_empty_talk:
                $ basement_1_talked = True
                menu:
                    extend ""

                    "{i}• (Explore) ''What's your name?''{/i}" if basement_1_name_ask == False:
                        $ basement_1_name_ask = True
                        show princess c thinking talk onlayer back
                        with dissolve
                        voice "audio/voices/ch1/empty/princess/empty_p_12.flac"
                        p "Oh...\n"
                        show princess c thinking onlayer back
                        with dissolve
                        voice "audio/voices/ch1/empty/narrator/empty_n_11.flac"
                        n "She pauses, carefully formulating her words before she responds.\n"
                        voice "audio/voices/ch1/empty/princess/empty_p_13.flac"
                        show princess c innocent talk onlayer back
                        with dissolve
                        p "You can address me as 'Your Royal Highness.'\nOr you can just call me 'Princess' if 'Your Royal Highness' is too formal.\n"
                        voice "audio/voices/ch1/empty/hero/empty_h_3.flac"
                        show princess c innocent onlayer back
                        with dissolve
                        hero "Is 'Princess' her name or her title? What if it's both? Could you imagine being named Princess Princess?\n"
                        jump basement_1_empty_talk

                    "{i}• (Explore) ''So is Princess your name?''{/i}" if basement_1_name_ask and basement_1_name_ask_follow_up == False:
                        $ basement_1_name_ask_follow_up = True
                        show princess c glance sad onlayer back
                        with dissolve
                        p "...\n"
                        voice "audio/voices/ch1/empty/princess/empty_p_14.flac"
                        show princess c nervous smile talk onlayer back
                        with dissolve
                        p "Like I said, you can call me Princess if you'd like!\n"
                        show princess c nervous smile onlayer back
                        with dissolve
                        p "...\n"
                        voice "audio/voices/ch1/empty/princess/empty_p_15.flac"
                        show princess c explain talk onlayer back
                        with dissolve
                        p "I'm sorry. I've been down here so long I guess I've just forgotten. I must have a name, though! Everyone has a name.\n"
                        voice "audio/voices/ch1/empty/hero/empty_h_4.flac"
                        show princess c sad onlayer back
                        with dissolve
                        hero "Okay. That's weird.\n"
                        voice "audio/voices/ch1/empty/narrator/empty_n_12.flac"
                        n "She hadn't even thought to pick a name for herself. Hopefully you're starting to see that she can't be trusted. Go back upstairs, get the blade, and slay her before it's too late.\n"
                        jump basement_1_empty_talk

                    "{i}• (Explore) ''I don't know anything about you. For all I know you're locked up down here for a reason.''{/i}" if basement_1_why_imprisoned == False:
                        $ basement_1_why_imprisoned = True
                        show princess c aback talk onlayer back
                        with dissolve
                        voice "audio/voices/ch1/empty/princess/empty_p_16.flac"
                        p "Of course I'm locked up down here for a reason!\n...\n"
                        show princess c nervous smile talk onlayer back
                        with dissolve
                        voice "audio/voices/ch1/empty/princess/empty_p_17.flac"
                        p "I don't actually know what that reason is, but you don't just stuff a Princess in a basement and throw away the key without there being {i}some{/i} sort of an explanation, right?\n"
                        show princess c serious onlayer back
                        with dissolve
                        voice "audio/voices/ch1/empty/narrator/empty_n_13.flac"
                        n "You have all the explanation you need. And you should know better than to trust whatever she comes up with.\n"
                        jump basement_1_empty_talk

                    "{i}• (Explore) ''I wasn't kidding when I said I was sent here to kill you. You're apparently going to end the world.''{/i}" if basement_1_empty_kill_joke and basement_1_shared_task == False:
                        label basement_1_empty_task_share:
                            $ basement_1_shared_task = True
                            show princess c aback talk onlayer back
                            with dissolve
                            voice "audio/voices/ch1/empty/princess/empty_p_18.flac"
                            p "I—is that why they threw me down here? But I don't want to hurt anyone. I like the world!\nI think.\n"
                            show princess c nervous talk onlayer back
                            with dissolve
                            voice "audio/voices/ch1/empty/princess/empty_p_19.flac"
                            p "I don't remember much about it, to be honest. I've been down here for so long.\n"
                            show princess c sad onlayer back
                            with dissolve
                            voice "audio/voices/ch1/empty/hero/empty_h_5.flac"
                            hero "That's... How long has she been locked away?!\n"
                            #voice "audio/voices/ch1/empty/narrator/empty_n_14.flac"
                            #n "How long does she want you to {i}think{/i} she's been locked away for?"
                            show princess c nervous smile talk onlayer back with dissolve
                            voice "audio/voices/ch1/empty/princess/empty_p_20.flac"
                            p "Did they tell you {i}how{/i} I'm supposed to end the world?\n"
                            label basement_1_empty_task_share_late_join:
                                menu:
                                    extend ""

                                    "{i}• (Deflect) ''What are you going to do if I let you out of here?''{/i}" if what_would_you_do_1 == False:
                                        $ what_would_you_do_1 = True
                                        show princess c thinking onlayer back
                                        with dissolve
                                        voice "audio/voices/ch1/empty/narrator/empty_n_15.flac"
                                        n "The Princess hesitates before responding.\n"
                                        voice "audio/voices/ch1/empty/hero/empty_h_6.flac"
                                        hero "She doesn't know. She's been down here too long to have any idea of what she'd do in another life.\n"
                                        voice "audio/voices/ch1/empty/narrator/empty_n_16.flac"
                                        n "She knows what she'd do. She's just searching for whatever answer she thinks you want to hear.\n"
                                        voice "audio/voices/ch1/empty/princess/empty_p_21.flac"
                                        show princess c sad glance talk onlayer back
                                        with dissolve
                                        p "What I'd do doesn't really matter, right?\n"
                                        jump basement_1_philosophy

                                    "{i}• ''I've been told enough.''{/i}":
                                        show princess c aback onlayer back
                                        with dissolve
                                        voice "audio/voices/ch1/empty/narrator/empty_n_17.flac"
                                        n "I appreciate the vote of confidence.\n"
                                        voice "audio/voices/ch1/empty/princess/empty_p_22.flac"
                                        show princess c sad glance talk onlayer back
                                        with dissolve
                                        p "They haven't shared a thing, have they? All they've done is point a finger.\n"
                                        jump basement_1_philosophy

                                    "{i}• ''I was hoping you'd tell me.''{/i}":
                                        show princess c nervous smile talk onlayer back
                                        with dissolve
                                        voice "audio/voices/ch1/empty/princess/empty_p_23.flac"
                                        p "I don't know how to destroy the world, if that's what you're getting at.\n"
                                        voice "audio/voices/ch1/empty/hero/empty_h_7.flac"
                                        show princess c innocent onlayer back
                                        with dissolve
                                        hero "I believe her.\n"
                                        voice "audio/voices/ch1/empty/narrator/empty_n_18.flac"
                                        n "She doesn't have to know how to destroy the world to be capable of doing it.\n"
                                        jump basement_1_philosophy

                                    "{i}• ''No. But I'm sure they have their reasons for keeping that information secret from me.''{/i}":
                                        show princess c aback onlayer back
                                        with dissolve
                                        voice "audio/voices/ch1/empty/narrator/empty_n_19.flac"
                                        n "I appreciate the vote of confidence.\n"
                                        voice "audio/voices/ch1/empty/princess/empty_p_24.flac"
                                        show princess c aback talk onlayer back
                                        with dissolve
                                        p "What if they're bad reasons, though? If they had {i}good{/i} reasons for thinking I was dangerous, wouldn't they have shared them with you? I don't want to hurt anyone. I just want to leave.\n"
                                        jump basement_1_philosophy

                                    "{i}• ''No. Which is why I don't think you're actually dangerous.''{/i}":
                                        show princess c relief onlayer back
                                        with dissolve
                                        voice "audio/voices/ch1/empty/narrator/empty_n_20.flac"
                                        n "Sooner or later you'll learn to trust me. Hopefully it won't be too late when you finally come around.\n"
                                        #re-read
                                        voice "audio/voices/ch1/empty/princess/empty_p_25.flac"
                                        show princess c relief talk onlayer back
                                        with dissolve
                                        p "Thank you for believing me. Now can you help me get out of here?\n"
                                        menu:
                                            extend ""

                                            "{i}• ''I still have a few more questions before we leave.''{/i}":
                                                voice "audio/voices/ch1/empty/princess/empty_p_26.flac"
                                                show princess c nervous smile talk onlayer back
                                                with dissolve
                                                p "There's going to be plenty of time to chat after I'm free, but okay. What do you want to know?\n"
                                                jump basement_1_empty_talk

                                            "{i}• (Examine the chains) ''I'll see what I can do.''{/i}":
                                                jump basement_1_empty_rescue

                                    "{i}• [[Remain silent.]{/i}":
                                        show princess c sad glance talk onlayer back
                                        with dissolve
                                        voice "audio/voices/ch1/empty/princess/empty_p_22.flac"
                                        p "They haven't shared a thing, have they? All they've done is point a finger.\n"
                                        jump basement_1_philosophy

                                label basement_1_philosophy:
                                    #re-read
                                    show princess c sad talk onlayer back
                                    with dissolve
                                    voice "audio/voices/ch1/empty/princess/empty_p_27.flac"
                                    p "At the end of the day, whatever the two of us have going on down here is about trust.\n"
                                    voice "audio/voices/ch1/empty/princess/empty_p_28.flac"
                                    show princess c thinking talk onlayer back
                                    with dissolve
                                    p "Whoever sent you to 'slay' me {i}claimed{/i} I was a threat to the world, but they didn't tell you why.\n"
                                    show princess c nervous talk onlayer back
                                    with dissolve
                                    #re-read
                                    voice "audio/voices/ch1/empty/princess/empty_p_29.flac"
                                    p "I don't trust that, and I don't think you do, either, or you wouldn't have come down here to talk.\n"
                                    show princess c nervous smile onlayer back
                                    with dissolve
                                    voice "audio/voices/ch1/empty/hero/empty_h_8.flac"
                                    hero "She has a point. We're talking like this for a reason.\n"
                                    show princess c explain talk onlayer back
                                    with dissolve
                                    voice "audio/voices/ch1/empty/princess/empty_p_30.flac"
                                    p "So this shouldn't be about what I'd do if I got out of here, or me saying the right thing to convince you to save me...\n"
                                    voice "audio/voices/ch1/empty/princess/empty_p_31.flac"
                                    show princess c annoyed talk onlayer back
                                    with dissolve
                                    p "This is about how {i}messed up{/i} this whole situation is! This is my life we're talking about!\n"
                                    voice "audio/voices/ch1/empty/princess/empty_p_32.flac"
                                    show princess c aback talk onlayer back
                                    with dissolve
                                    p "Do you really think I can even end the world? Why would I even want to?\n"
                                    show princess c serious talk onlayer back
                                    with dissolve
                                    voice "audio/voices/ch1/empty/princess/empty_p_33.flac"
                                    p "We both know that if there's people we can't trust in this situation, it's whoever locked me down here, and it's whoever sent you here. And those two groups are probably one and the same.\n"
                                    show princess c serious onlayer back
                                    with dissolve
                                    voice "audio/voices/ch1/empty/narrator/empty_n_21.flac"
                                    n "Don't let her turn the tables here. This isn't about trust. This is about {b}risk{/b}. We stand to lose everything, all for the sake of one person. And a subjugating {i}monarch{/i}, no less.\n"
                                    jump basement_1_empty_talk


                    "{i}• (Explore) ''If I'm the first person you've seen in a while, what have you been eating? Or drinking?''{/i}" if basement_1_eating_ask == False:
                        $ basement_1_eating_ask = True
                        show princess c thinking talk onlayer back
                        with dissolve
                        voice "audio/voices/ch1/empty/princess/empty_p_34.flac"
                        p "I don't see what that has to do with anything.\n"
                        voice "audio/voices/ch1/empty/narrator/empty_n_22.flac"
                        show princess c thinking onlayer back
                        with dissolve
                        n "This is the only time this is ever going to happen, but I agree with the Princess. That's hardly relevant.\n"
                        voice "audio/voices/ch1/empty/hero/empty_h_9.flac"
                        hero "Okay but actually, what {i}has{/i} she been eating? She has to eat, right?\n"
                        jump basement_1_empty_talk

                    "{i}• (Explore) ''I was sent here to slay you. You're apparently supposed to end the world...''{/i}" if basement_1_empty_kill_joke == False and basement_1_shared_task == False:
                        show princess c aback onlayer back
                        with dissolve
                        menu:
                            extend ""

                            "{i}• ''But I don't think you're actually dangerous.''{/i}":
                                jump basement_1_empty_task_share

                            "{i}• ''But I wanted to see you for myself. I'm still not sure what to believe.''{/i}":
                                jump basement_1_empty_task_share

                            "{i}• ''I'm starting to think it's true. There's something about you that doesn't feel right.''{/i}":
                                $ basement_1_shared_task = True
                                show princess c annoyed talk onlayer back
                                with dissolve
                                voice "audio/voices/ch1/empty/princess/empty_p_35.flac"
                                p "Would everything feel right about you if you were locked away in a hole by yourself for as long as you can remember?\n"
                                show princess c annoyed onlayer back
                                with dissolve
                                voice "audio/voices/ch1/empty/hero/empty_h_10.flac"
                                hero "Just how long {i}has{/i} she been down here?\n"
                                #bvoice "audio/voices/ch1/empty/narrator/empty_n_23.flac"
                                #n "How long does she want you to {i}think{/i} she's been down here?"
                                show princess c sad glance talk onlayer back
                                with dissolve
                                voice "audio/voices/ch1/empty/princess/empty_p_36.flac"
                                p "So... did they tell you why I'm supposed to be so dangerous?\n"
                                jump basement_1_empty_task_share_late_join

                    "{i}• (Explore) ''What are you going to do if I let you out of here?''{/i}" if what_would_you_do_1 == False and basement_1_shared_task == False:
                        $ what_would_you_do_1 = True
                        show princess c thinking onlayer back
                        with dissolve
                        voice "audio/voices/ch1/empty/narrator/empty_n_24.flac"
                        n "The Princess hesitates before responding.\n"
                        voice "audio/voices/ch1/empty/hero/empty_h_11.flac"
                        hero "She doesn't know. She's been down here too long to have any idea of what she'd do in another life.\n"
                        voice "audio/voices/ch1/empty/narrator/empty_n_16.flac"
                        n "She knows what she'd do. She's just searching for whatever answer she thinks you want to hear.\n"
                        show princess c serious talk onlayer back
                        with dissolve
                        #re-read(add "it's not like you'd believe me")
                        voice "audio/voices/ch1/empty/princess/empty_p_37.flac"
                        p "Are you looking for the truth, or are you looking for the 'right' answer? Because with the dynamic we have going on here I don't think the specifics of what I'd 'do' really matter.\n"
                        show princess c nervous talk onlayer back
                        with dissolve
                        voice "audio/voices/ch1/empty/princess/empty_p_37b.flac"
                        p "It's not like you'd believe me.\n"
                        show princess c nervous onlayer back
                        #with dissolve
                        jump basement_1_empty_talk

                    "{i}• ''I won't kill you, but I can't just set you free. It's too risky. What if I stayed for a while and just kept you company? Maybe then everyone could be happy.''{/i}" if basement_1_shared_task or basement_1_empty_kill_joke:
                        # finish block
                        label basement_1_empty_no_kill:
                            show princess c nervous onlayer back
                            with dissolve
                            voice "audio/voices/ch1/empty/hero/empty_h_12.flac"
                            hero "That seems like a pretty good compromise.\n"
                            if basement_1_empty_kill_joke and basement_1_shared_task == False:
                                voice "audio/voices/ch1/empty/princess/empty_p_38.flac"
                                show princess c nervous talk onlayer back
                                with dissolve
                                p "So you weren't kidding on the stairs. I thought you were just making a bad joke. You were actually sent here to kill me?\n"
                            else:
                                show princess c nervous talk onlayer back
                                with dissolve
                                voice "audio/voices/ch1/empty/princess/empty_p_39.flac"
                                p "I don't think I could bear being down here that much longer.\n"
                            show princess c nervous onlayer back
                            with dissolve
                            voice "audio/voices/ch1/empty/narrator/empty_n_25.flac"
                            n "Leaving her alive is too risky. If you don't deal with her soon, she {i}will{/i} find a way out.\n"
                            voice "audio/voices/ch1/empty/hero/empty_h_13.flac"
                            hero "So I'm the only one who liked that idea? {i}Sigh{/i}.\n"
                            show princess c bored talk onlayer back
                            with dissolve
                            stop music fadeout 1.0
                            voice "audio/voices/ch1/empty/princess/empty_p_40.flac"
                            p "One way or another, I'm going to find a way out of here. It would make it easier for both of us if you'd help.\n"
                            show princess c sinister talk onlayer back
                            with dissolve
                            play music "audio/_music/ch1/The World-Ender.flac"
                            queue music "audio/_music/ch1/The World-Ender Loop.flac" loop
                            voice "audio/voices/ch1/empty/princess/empty_p_41.flac"
                            sp "But if you don't, I can promise that you'll regret that decision.\n"
                            show princess c sinister onlayer back
                            with dissolve
                            voice "audio/voices/ch1/empty/narrator/empty_n_26.flac"
                            n "You have to make a choice. Let's hope for all our sakes it's the right one.\n"
                            menu:
                                extend ""

                                "{i}• [[Retrieve the blade.]{/i}" if beast_encountered == False or witch_encountered == False:
                                    voice "audio/voices/ch1/empty/narrator/empty_n_36.flac"
                                    n "{i}Thank{/i} you.\n"
                                    play audio "audio/one_shot/footsteps_creaky.flac"
                                    voice "audio/voices/ch1/empty/narrator/empty_n_28.flac"
                                    hide princess onlayer back
                                    hide bg onlayer farback
                                    show basement stairs open onlayer front at Position(ypos=1125)
                                    with dissolve
                                    n "You turn back to the stairs, intent on retrieving the blade in the cabin.\n"
                                    voice "audio/voices/ch1/empty/princess/empty_p_42.flac"
                                    sp "Where are you going?! You can't just leave me here!\n"
                                    voice "audio/voices/ch1/empty/princess/empty_p_43.flac"
                                    #p "You'd better hope for your own sake that I don't slip these chains before you make it back down here."
                                    sp "Fine! Turn your back on me! But it won't be long before I slip these chains, and once I'm out of here? There'll be {i}hell{/i} to pay for leaving me behind!\n"
                                    jump basement_1_empty_retrieve_knife_early_join

                                "{i}• ''Okay. Let's get you out of here.'' [[Examine the chains.]{/i}" if damsel_encountered == False or nightmare_encountered == False:
                                    show princess c relief onlayer back
                                    with dissolve
                                    voice "audio/voices/ch1/empty/narrator/empty_n_29.flac"
                                    n "You can't be {i}serious{/i}–\n"
                                    show princess c nervous smile talk onlayer back
                                    with dissolve
                                    voice "audio/voices/ch1/empty/princess/empty_p_44.flac"
                                    p "Thank you, thank you! You won't regret this, I promise.\n"
                                    voice "audio/voices/ch1/empty/narrator/empty_n_30.flac"
                                    show princess c innocent onlayer back
                                    with dissolve
                                    n "You're making a huge mistake.\n"
                                    voice "audio/voices/ch1/empty/hero/empty_h_14.flac"
                                    hero "No. I think you're doing the right thing.\n"
                                    jump basement_1_empty_rescue

                                "{i}• [[Lock her in the basement.]{/i}" if nightmare_encountered == False:
                                    show princess c haughty onlayer back
                                    with dissolve
                                    voice "audio/voices/ch1/empty/narrator/empty_n_31.flac"
                                    n "I know you think this is some kind of fair compromise, but it isn't. {b}No one{/b} wins here.\n"
                                    voice "audio/voices/ch1/empty/hero/empty_h_15.flac"
                                    hero "It's a chance we'll have to take. We can make this work. If we just stay here and keep watch, no one has to die.\n"
                                    play audio "audio/one_shot/footsteps_hike_short.flac"
                                    voice "audio/voices/ch1/empty/princess/empty_p_42.flac"
                                    hide princess onlayer back
                                    hide bg onlayer farback
                                    show farbg flee back onlayer farback at Position(ypos=1125)
                                    show bg flee onlayer back at Position(ypos=1125)
                                    with dissolve
                                    sp "Where are you going?! You can't just leave me here!\n"
                                    play audio "audio/one_shot/footsteps_creaky.flac"
                                    voice "audio/voices/ch1/empty/narrator/empty_n_32.flac"
                                    hide farbg flee back onlayer farback
                                    hide bg flee onlayer back
                                    show basement stairs open onlayer front at Position(ypos=1125)
                                    with dissolve
                                    n "You turn your back to the Princess and make your way back to the stairs.\n"
                                    voice "audio/voices/ch1/empty/princess/empty_p_43.flac"
                                    sp "Fine! Turn your back on me. But it won't be long before I slip these chains. And once I'm out of here, there will be {b}hell{/b} to pay for leaving me behind.\n"
                                    voice "audio/voices/ch1/empty/hero/empty_h_16.flac"
                                    hero "'Slip these chains?' She can't, right? She needed our help to get out of here. But do you hear the conviction in her voice? I don't think she's bluffing.\n"
                                    voice "audio/voices/ch1/empty/narrator/empty_n_33.flac"
                                    n "Either way, she dropped the mask, didn't she? You can still grab the blade and get back down here...\n"
                                    menu:
                                        extend ""

                                        "{i}• No, we're sticking to the plan and locking her away.{/i}":
                                            $ nightmare_no_wounds = True
                                            voice "audio/voices/ch1/empty/narrator/empty_n_34.flac"
                                            n "You'll be the death of all of us, but fine. We'll do it your way.\n"
                                            hide basement stairs open onlayer front
                                            with fade
                                            jump nightmare_join

                                        "{i}• Oh that's a relief! I was afraid I'd already committed to not slaying her.{/i}" if beast_encountered == False or witch_encountered == False:
                                            voice "audio/voices/ch1/empty/narrator/empty_n_35.flac"
                                            n "It's never too late to do the right thing. Now hurry.\n"
                                            hide basement stairs open onlayer front
                                            with fade
                                            jump basement_1_empty_retrieve_knife

                    "{i}• ''I'm going to keep you locked away down here. At least for a little bit. We can get to know each other better while I decide what to do.'' [[Keep her locked away.]{/i}" if nightmare_encountered == False:
                        jump basement_1_empty_no_kill

                    "{i}• ''I'm sorry, but I just can't trust you. This doesn't add up, and it isn't worth the risk to take your word over the potential fate of the world.''{/i} [[Retrieve the blade.]" if beast_encountered == False or witch_encountered == False:
                        show princess c haughty onlayer back
                        with dissolve
                        default basement_1_empty_not_worth_risk = False
                        $ basement_1_empty_not_worth_risk = True
                        voice "audio/voices/ch1/empty/narrator/empty_n_36.flac"
                        n "{i}Thank{/i} you.\n"
                        play audio "audio/one_shot/footsteps_creaky.flac"
                        voice "audio/voices/ch1/empty/narrator/empty_n_28.flac"
                        hide princess onlayer back
                        hide bg onlayer farback
                        show basement stairs open onlayer front at Position(ypos=1125)
                        with dissolve
                        n "You turn back to the stairs, intent on retrieving the blade in the cabin.\n"
                        if basement_1_empty_kill_joke and basement_1_shared_task == False:
                            voice "audio/voices/ch1/empty/princess/empty_p_47.flac"
                            p "So you weren't kidding... I thought you were just making a bad joke. You were {i}actually{/i} sent here to kill me.\n"
                        elif basement_1_shared_task == False:
                            voice "audio/voices/ch1/empty/princess/empty_p_48.flac"
                            p "So what? You're going to try and kill me?\n"
                        stop music fadeout 1.0
                        voice "audio/voices/ch1/empty/princess/empty_p_49.flac"
                        sp "You'll regret this. I promise you. But go ahead. Run along and get whatever you're planning to get.\n"
                        play music "audio/_music/ch1/The World-Ender.flac"
                        queue music "audio/_music/ch1/The World-Ender Loop.flac" loop
                        voice "audio/voices/ch1/empty/princess/empty_p_50.flac"
                        sp "But you'd better hope that I don't slip these chains before you make it back down here.\n"
                        label basement_1_empty_retrieve_knife_early_join:
                            voice "audio/voices/ch1/empty/hero/empty_h_17.flac"
                            hero "'Slip these chains?' She can't, right? She needed our help to get out of here. But do you hear the conviction in her voice? I don't think she's bluffing.\n"
                            voice "audio/voices/ch1/empty/narrator/empty_n_38.flac"
                            n "She has to be bluffing. But... hurry.\n"
                        jump basement_1_empty_retrieve_knife

                    "{i}• [[Go back upstairs to retrieve the blade without saying another word.]{/i}" if beast_encountered == False or witch_encountered == False:
                        show princess c haughty onlayer back
                        with dissolve
                        voice "audio/voices/ch1/empty/narrator/empty_n_36.flac"
                        n "{i}Thank{/i} you.\n"
                        voice "audio/voices/ch1/empty/narrator/empty_n_28.flac"
                        play audio "audio/one_shot/footsteps_creaky.flac"
                        hide princess onlayer back
                        hide bg onlayer farback
                        show basement stairs open onlayer front at Position(ypos=1125)
                        with dissolve
                        n "You turn back to the stairs, intent on retrieving the blade from the cabin.\n"
                        stop music fadeout 1.0
                        voice "audio/voices/ch1/empty/princess/empty_p_51.flac"
                        p "Where are you going?! You can't just leave me here!\n"
                        play music "audio/_music/ch1/The World-Ender.flac"
                        queue music "audio/_music/ch1/The World-Ender Loop.flac" loop
                        voice "audio/voices/ch1/empty/princess/empty_p_52.flac"
                        sp "You'd better hope for your own sake that I don't slip these chains before you make it back down here.\n"
                        voice "audio/voices/ch1/empty/hero/empty_h_17.flac"
                        hero "'Slip these chains?' She can't, right? She needed our help to get out of here. But do you hear the conviction in her voice? I don't think she's bluffing.\n"
                        voice "audio/voices/ch1/empty/narrator/empty_n_39.flac"
                        n "She has to be bluffing. But... I'd hurry if I were you.\n"
                        jump basement_1_empty_retrieve_knife

                    "{i}• ''I can't believe they've been keeping you down here like this! I'm getting you out of here.'' [[Examine the chains.]{/i}" if witch_encountered == False or damsel_encountered == False:
                        jump basement_1_empty_rescue_join

                    "{i}• ''Okay, I'm going to get you out of here. Don't make me regret this.'' [[Examine the chains.]{/i}" if witch_encountered == False or damsel_encountered == False:
                        default basement_1_empty_rescue_dont_regret = False
                        $ basement_1_empty_rescue_dont_regret = True
                        jump basement_1_empty_rescue_join

        "{i}• ''I'll see what I can do.'' [[Examine the chains.]{/i}" if witch_encountered == False or damsel_encountered == False:
            play audio "audio/one_shot/footsteps_hike_short.flac"
            $ quick_menu = False
            hide princess onlayer back
            hide bg basement distant onlayer farback
            hide back basement distant onlayer back
            with fade
            label basement_1_empty_rescue_join:
                voice "audio/voices/ch1/empty/narrator/empty_n_40.flac"
                show bg basement close onlayer farback at Position(ypos=1125)
                show princess c relief onlayer back at Position(ypos=1125)
                with dissolve
                if persistent.quick_menu:
                    $ quick_menu = True
                n "You're only making this more difficult...\n"
                show princess c relief talk onlayer back with dissolve
                if basement_1_empty_rescue_dont_regret == False:
                    voice "audio/voices/ch1/empty/princess/empty_p_53.flac"
                    p "Thank you, thank you!\n"
                else:
                    voice "audio/voices/ch1/empty/princess/empty_p_54.flac"
                    p "Thank you, and you won't! I promise!\n"
                show princess c nervous smile onlayer back with dissolve
                voice "audio/voices/ch1/empty/narrator/empty_n_41.flac"
                n "You're making a huge mistake.\n"
                voice "audio/voices/ch1/empty/hero/empty_h_18.flac"
                hero "No. You're doing the right thing.\n"
            jump basement_1_empty_rescue

label basement_1_empty_rescue:
    show bg basement close onlayer farback at Position(ypos=1125)
    show princess c thinking onlayer back with dissolve
    voice "audio/voices/ch1/empty/narrator/empty_n_42.flac"
    play audio "audio/one_shot/chain_2.flac"
    n "You walk up to the chains binding the Princess to the wall and give them a tug.\n"
    voice "audio/voices/ch1/empty/narrator/empty_n_43.flac"
    n "They're large and heavy, far too solid for you to even imagine trying to break them apart.\n"
    voice "audio/voices/ch1/empty/princess/empty_p_55.flac"
    show princess c nervous smile talk onlayer back with dissolve
    p "I'm guessing you don't have the key.\n"
    voice "audio/voices/ch1/empty/hero/empty_h_19.flac"
    show princess c nervous smile onlayer back with dissolve
    hero "Maybe it's somewhere upstairs.\n"
    voice "audio/voices/ch1/empty/narrator/empty_n_44.flac"
    n "Doubtful. Whoever locked the Princess away down here intended for her to never see the light of day. They wouldn't have just left the key to her chains somewhere in the cabin.\n"
    menu:
        extend ""

        "{i}• ''And if there isn't a key... do you have any other ideas?''{/i}":
            voice "audio/voices/ch1/empty/princess/empty_p_56.flac"
            show princess c innocent talk onlayer back with dissolve
            p "Maybe there's some way to break the chains?\n"
            show princess c innocent onlayer back with dissolve
            p "...\n"
            voice "audio/voices/ch1/empty/princess/empty_p_57.flac"
            show princess c nervous smile talk onlayer back with dissolve
            p "Or if that doesn't work I guess we can always cut me out of them.\n"
            voice "audio/voices/ch1/empty/narrator/empty_n_45.flac"
            show princess c nervous smile onlayer back with dissolve
            n "She offers the suggestion with almost complete nonchalance.\n"
            voice "audio/voices/ch1/empty/hero/empty_h_20.flac"
            hero "If we were stuck down here long enough, I'm sure we'd be nonchalant about cutting our way out if it meant we could finally be free.\n" id basement_1_empty_rescue_351a87ee

        "{i}• ''I'm going to check upstairs. Maybe the key's still lying around somewhere up there. And if not, maybe I can at least find something to break you free.''{/i}":
            voice "audio/voices/ch1/empty/princess/empty_p_58.flac"
            show princess c nervous smile talk onlayer back with dissolve
            p "Okay. I'll be here. Good luck.\n"

    voice "audio/voices/ch1/empty/narrator/empty_n_46.flac"
    play secondary "audio/one_shot/footsteps_creaky.flac"
    queue secondary "audio/one_shot/door_close.flac"
    queue secondary "audio/one_shot/lock_click.flac"
    $ quick_menu = False
    hide bg onlayer farback
    hide princess onlayer back
    show basement stairs closed onlayer front at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    n "You attempt to make your way out of the basement, but the door at the top of the stairs slams shut. You hear the click of a lock sliding into place.\n"
    voice "audio/voices/ch1/empty/hero/empty_h_21.flac"
    hero "Is someone else here?\n"
    label basement_1_empty_rescue_door:
        default basement_1_empty_rescue_door_try_explore = False
        default basement_1_empty_rescue_door_force_explore = False
        default basement_1_empty_rescue_door_shout_explore = False
        menu:
            extend ""

            "{i}• (Explore) ''Hey! Let me out of here!''{/i}" if basement_1_empty_rescue_door_shout_explore == False:
                $ basement_1_empty_rescue_door_shout_explore = True
                voice "audio/voices/ch1/empty/narrator/empty_n_47.flac"
                n "Your shouts and pleas are met with silence.\n"
                if basement_1_empty_rescue_door_try_explore == False:
                    voice "audio/voices/ch1/empty/narrator/empty_n_48.flac"
                    n "I'll repeat myself once again. You're here to slay the Princess, and you won't leave until the task is done.\n"
                else:
                    voice "audio/voices/ch1/empty/narrator/empty_n_49.flac"
                    n "You're here to slay the Princess, and you won't leave until the task is done.\n"
                jump basement_1_empty_rescue_door

            "{i}• (Explore) [[Try the door.]{/i}" if basement_1_empty_rescue_door_try_explore == False:
                play audio "audio/one_shot/door_try.flac"
                $ basement_1_empty_rescue_door_try_explore = True
                voice "audio/voices/ch1/empty/narrator/empty_n_50.flac"
                n "You try the door, but it's locked from the outside.\n"
                jump basement_1_empty_rescue_door

            #"(Explore) Force the door open.{/i}" if basement_1_empty_rescue_door_try_explore and basement_1_empty_rescue_door_force_explore == False:
            #    play audio "audio/one_shot/door_try.flac"
            #    $ basement_1_empty_rescue_door_try_explore = True
            #    voice "audio/voices/ch1/empty/narrator/empty_n_51.flac"
            #    n "You throw your body against the basement door in a pathetic attempt to force it open. It doesn't budge.\n"
            #    if basement_1_empty_rescue_door_shout_explore:
            #        voice "audio/voices/ch1/empty/narrator/empty_n_48.flac"
            #        n "I'll repeat myself once again. You're here to slay the Princess, and you won't leave until the task is done.\n"
            #    else:
            #        voice "audio/voices/ch1/empty/narrator/empty_n_49.flac"
            #        n "You're here to slay the Princess, and you won't leave until the task is done.\n"
            #    jump basement_1_empty_rescue_door

            "{i}• [[Return to the bottom of the stairs.]{/i}":
                voice "audio/voices/ch1/empty/narrator/empty_n_52.flac"
                play audio "audio/one_shot/footsteps_creaky.flac"
                $ quick_menu = False
                hide basement onlayer front
                scene bg basement distant onlayer farback at Position(ypos=1125)
                show back basement distant onlayer back at Position(ypos=1125)
                show princess d neutral onlayer back at Position(ypos=1125)
                with fade
                if persistent.quick_menu:
                    $ quick_menu = True
                n "You make your way to the bottom of the stairs. This would have been so much easier if you'd just taken the blade like you were supposed to.\n"
                voice "audio/voices/ch1/empty/hero/empty_h_22.flac"
                hero "Easier for whom?\n"
                voice "audio/voices/ch1/empty/narrator/empty_n_53.flac"
                n "Easier for {i}everyone{/i}. Look at the mess you're in.\n"

        voice "audio/voices/ch1/empty/princess/empty_p_59.flac"
        $ quick_menu = False
        hide bg onlayer farback
        hide back onlayer back
        hide princess onlayer back
        show bg basement close onlayer farback at Position(ypos=1125)
        show princess c nervous onlayer back at Position(ypos=1125)
        with fade
        if persistent.quick_menu:
            $ quick_menu = True
        show princess c nervous talk onlayer back with dissolve
        p "I heard the door slam... they locked you down here too, didn't they?\n"
        voice "audio/voices/ch1/empty/narrator/empty_n_54.flac"
        show princess c nervous onlayer back with dissolve
        n "There's a slight panic rising in the Princess' voice.\n"
        voice "audio/voices/ch1/empty/princess/empty_p_60.flac"
        show princess c thinking talk onlayer back with dissolve
        stop music fadeout 1.0
        p "If I could just get out of these chains I {i}know{/i} we could force our way out of here together.\n"
        play music "audio/_music/ch1/The World-Ender.flac"
        queue music "audio/_music/ch1/The World-Ender Loop.flac" loop
        play audio "audio/one_shot/nom.flac"
        voice "audio/voices/ch1/empty/narrator/empty_n_55.flac"
        hide bg onlayer farback
        hide princess onlayer back
        show bg princess gnaw onlayer back at Position(ypos=1125)
        show princess gnaw 1 onlayer front at Position(ypos=1125)
        with dissolve
        n "She barely hesitates before raising her arm to her mouth, her teeth tearing through her limb with the determination of a trapped wolf.\n"
        play audio "audio/one_shot/knife_bounce_several.flac"
        voice "audio/voices/ch1/empty/narrator/empty_n_56.flac"
        n "As she rips her flesh from her bone, a sound comes from behind you. The clang of bouncing metal.\n"
        voice "audio/voices/ch1/empty/narrator/empty_n_57.flac"
        hide princess onlayer front
        hide bg onlayer back
        show bg generic dark onlayer back at Position(ypos=1125)
        show knife dropped onlayer inyourface at Position(ypos=1125)
        with dissolve
        n "It's the blade from upstairs. You're not sure how it made its way down here, but if there's a time to strike, it's now.\n"
        voice "audio/voices/ch1/empty/hero/empty_h_23.flac"
        hero "Or we could use it to free her.\n"
        voice "audio/voices/ch1/empty/narrator/empty_n_58.flac"
        n "You won't like what happens if you do that.\n"
        menu:
            extend ""

            "{i}• [[Save the Princess.]{/i}" if damsel_encountered == False or witch_encountered == False:
                $ blade_held = True
                $ default_mouse = "blade"
                voice "audio/voices/ch1/empty/narrator/empty_n_59.flac"
                n "Ugh. Fine.\n"
                $ default_mouse = "blood"
                play audio "audio/one_shot/stab_fleshy.flac"
                voice "audio/voices/ch1/empty/narrator/empty_n_60.flac"
                hide knife onlayer inyourface
                hide bg onlayer back
                show bg princess cut onlayer back at Position(ypos=1125)
                show princess gnaw cut onlayer front at Position(ypos=1125)
                with dissolve
                n "Against your better judgment, you place the blade against the ragged, self-inflicted wound on the Princess' arm, just above the unyielding chain binding her to this place.\n"
                play audio "audio/one_shot/stab_goop.flac"
                voice "audio/voices/ch1/empty/narrator/empty_n_61.flac"
                n "You cut into her flesh.\n"
                play audio "audio/one_shot/arm_rip.flac"
                voice "audio/voices/ch1/empty/narrator/empty_n_62.flac"
                show princess arm pull onlayer front at Position(ypos=1125)
                with dissolve
                n "The blade is sharp, and it takes little effort to crack through the bone of her arm.\n"
                voice "audio/voices/ch1/empty/narrator/empty_n_63.flac"
                play secondary "audio/one_shot/thump.flac"
                queue secondary "audio/one_shot/chain_1.flac"
                hide bg onlayer back
                hide princess onlayer front
                show arm close onlayer front at Position(ypos=1125)
                with dissolve
                n "Her limb falls to the ground, and the heavy chains follow suit.\n"
                voice "audio/voices/ch1/empty/hero/empty_h_24.flac"
                hero "She didn't so much as utter a sound through the whole ordeal.\n"
                voice "audio/voices/ch1/empty/narrator/empty_n_64.flac"
                n "No. She didn't.\n"
                # REPLACE
                voice "audio/voices/ch1/empty/narrator/empty_n_65.flac"
                hide arm onlayer front
                show bg generic onlayer back at Position(ypos=1125)
                show princess free smile onlayer front at Position(ypos=1125)
                with dissolve
                n "She smiles softly as her gaze meets yours, blood from her wounded arm dripping rhythmically to the ground.\n"
                # old n "She clutches the wound, softly smiling as her gaze meets yours.\n"
                voice "audio/voices/ch1/empty/hero/empty_h_25.flac"
                hero "How is she still smiling after everything? It's like she isn't even bothered by what just happened.\n"
                voice "audio/voices/ch1/empty/princess/empty_p_61.flac"
                show princess free smile talk onlayer front at Position(ypos=1125)
                with dissolve
                p "Thank you. Now let's get out of here.\n"
                show princess free smile onlayer front at Position(ypos=1125)
                with dissolve
                menu:
                    extend ""

                    "{i}• [[Approach the locked door.]{/i}":
                        play audio "audio/one_shot/footsteps_hike_short.flac"
                        voice "audio/voices/ch1/empty/narrator/empty_n_66.flac"
                        hide princess onlayer front
                        hide bg onlayer back
                        show bg black onlayer front at Position(ypos=1125)
                        with dissolve
                        n "No. We won't have any of that. The stakes are too high. You can't just let her escape into the world.\n... no. {i}I{/i} can't just let her escape into the world.\n"
                        voice "audio/voices/ch1/empty/narrator/empty_n_67.flac"
                        hide bg onlayer front
                        show bg generic onlayer back at Position(ypos=1125)
                        show fury back onlayer front at Position(ypos=1125)
                        show player bloody knife onlayer inyourface at Position(ypos=1125)
                        with dissolve
                        n "As the Princess approaches the bottom stair, your body steps forward and raises the blade.\n"
                        voice "audio/voices/ch1/empty/hero/empty_h_26.flac"
                        hero "Wait... this isn't fair. You can't just {i}do{/i} that!\n"
                        voice "audio/voices/ch1/empty/narrator/empty_n_68.flac"
                        n "Watch me.\n"
                        # re-record
                        play audio "audio/one_shot/footsteps_stone_short.flac"
                        voice "audio/voices/ch1/empty/princess/empty_p_62r.flac"
                        hide fury onlayer front
                        show princess damsel 1 center talk onlayer front at Position(ypos=1125)
                        with dissolve
                        p "Wh-what are you doing?\n"
                        if (witch_encountered or damsel_encountered) and preferences.self_voicing == False:
                            $ config.menu_include_disabled = True
                        $ small_yadj = True
                        menu:
                            extend ""

                            "{i}• [[Slay the Princess.]{/i}" if witch_encountered == False:
                                label basement_1_empty_rescue_controlled_start:
                                    voice "audio/voices/ch1/empty/hero/empty_h_27.flac"
                                    hero "Okay. There's no going back now. I'm with you to the end.\n"
                                    voice "audio/voices/ch1/empty/narrator/empty_n_69.flac"
                                    play audio "audio/one_shot/knife_slash.flac"
                                    hide bg onlayer back
                                    hide princess onlayer front
                                    hide player onlayer inyourface
                                    show bg black onlayer back at Position(ypos=1125)
                                    show knife slice onlayer front at yflip, Position(ypos=1125)
                                    n "You bring the blade down to strike at the Princess' heart.\n"
                                    play audio "audio/one_shot/knife_slash.flac"
                                    voice "audio/voices/ch1/empty/narrator/empty_n_70.flac"
                                    hide knife onlayer front
                                    show bg generic onlayer back at Position(ypos=1125)
                                    show beast rescue control dodge onlayer front at Position(ypos=1125)
                                    with dissolve
                                    n "But she's fast. She ducks to the floor, your blade narrowly grazing her backside. Slaying her won't be easy now that she's free.\n"
                                    voice "audio/voices/ch1/empty/princess/empty_p_63.flac"
                                    hide bg onlayer back
                                    show player bloody knife onlayer inyourface at Position(ypos=1125)
                                    show bg beastrescuecontroldodgecrouch onlayer back at Position(ypos=1125)
                                    show beast rescue control dodge talk onlayer front at Position(ypos=1125)
                                    with dissolve
                                    sp "We could have gotten out of here together! Were you just lying to me this whole time?\n"
                                    voice "audio/voices/ch1/empty/princess/empty_p_64.flac"
                                    show beast rescue control dodge talk 2 onlayer front
                                    with dissolve
                                    sp "I don't know what's come over you, but if I have to kill you, then I'll kill you. Do you think I need both of my arms to do that?\n"
                                    #voice "audio/voices/ch1/empty/hero/empty_h_28.flac"
                                    #hero "Do you hear the conviction in her voice? Do you see that razor sharpness in her gaze? I don't think she's bluffing.\n"
                                    label basement_1_empty_beast:
                                        $ small_yadj = False
                                        $ config.menu_include_disabled = False
                                        $ current_princess = "witch"
                                        default witch_rescue_path = False
                                        $ witch_rescue_path = True
                                        play secondary "audio/one_shot/tackle.flac"
                                        queue secondary "audio/one_shot/rip_and_tear.flac"
                                        voice "audio/voices/ch1/empty/narrator/empty_n_71.flac"
                                        hide bg onlayer back
                                        hide beast onlayer front
                                        hide player onlayer inyourface
                                        show bg generic onlayer back at Position(ypos=1125)
                                        show beast rescue control pounce onlayer front at Position(ypos=1125)
                                        with dissolve
                                        n "She pounces on you with the same animal ferocity she used to tear through her arm.\n"
                                        play secondary "audio/one_shot/knife_stab.flac"
                                        queue secondary "audio/one_shot/stab_goop.flac"
                                        voice "audio/voices/ch1/empty/narrator/empty_n_72.flac"
                                        hide bg onlayer back
                                        hide beast onlayer front
                                        show bg generic dark onlayer back at Position(ypos=1125)
                                        show battle beast armless onlayer front at Position(ypos=1125)
                                        #show battle1 beast armless onlayer front at Position(ypos=1125)
                                        #show battle2 beast armless onlayer front at Position(ypos=1125)
                                        #show battle3 beast armless onlayer front at Position(ypos=1125)
                                        with Dissolve(0.75)
                                        n "But you have a weapon. You raise the blade, digging it under her ribs, aiming directly for the heart.\n"
                                        voice "audio/voices/ch1/empty/narrator/empty_n_73.flac"
                                        play audio "audio/one_shot/blood_leak.flac"
                                        play secondary "audio/one_shot/nom.flac"
                                        n "It's not enough to stop her. You feel her claws on your throat, then her teeth, somehow sharp enough to pull apart your flesh and sinew with ease.\n"
                                        play audio "audio/one_shot/blood_drip.flac"
                                        voice "audio/voices/ch1/empty/narrator/empty_n_74.flac"
                                        hide bg onlayer back
                                        #hide battle1 onlayer front
                                        #hide battle2 onlayer front
                                        #hide battle3 onlayer front
                                        hide battle onlayer front
                                        $ quick_menu = False
                                        show bg beastrescuecontroldodgecrouch onlayer back at Position(ypos=1125)
                                        show beast rescue control fail onlayer front at Position(ypos=1125)
                                        with fade
                                        if persistent.quick_menu:
                                            $ quick_menu = True
                                        n "You collapse to the floor, your body unresponsive as your blood pools on the ground beneath you. She stares down at your ravaged form, eyes shining in the darkness, dress stained in red as her blood and yours both seep into the fabric.\n"
                                        voice "audio/voices/ch1/empty/narrator/empty_n_75.flac"
                                        n "If we're lucky, the wound you managed to inflict will be enough to at least delay her escape from this place. If we're very lucky, it will kill her before she can reach the outside world.\n"
                                        voice "audio/voices/ch1/empty/hero/empty_h_29.flac"
                                        hero "It can't just end like this, right?\n"
                                        voice "audio/voices/ch1/empty/narrator/empty_n_76.flac"
                                        n "As much as I'd prefer for things to have gone differently, I can't deny the reality of what's happened. I'm sorry, but it's over.\n"
                                        $ persistent.death_count += 1
                                        voice "audio/voices/ch1/empty/narrator/empty_n_77.flac"
                                        stop music fadeout 1.0
                                        stop sound fadeout 1.0
                                        hide bg onlayer back
                                        hide beast onlayer front
                                        show bg black onlayer back at Position(ypos=1125)
                                        with dissolve
                                        n "Everything goes dark, and you die.\n"
                                        hide bg black onlayer back with dissolve
                                    jump start_2


                            "{i}• [[Slay the Princess.]{/i}" if witch_encountered == False and preferences.self_voicing == False:
                                jump basement_1_empty_rescue_controlled_start

                            "{i}• [[Slay the Princess.]{/i}" if witch_encountered == False and preferences.self_voicing == False:
                                jump basement_1_empty_rescue_controlled_start

                            "{i}• [[Slay the Princess.]{/i}" if witch_encountered == False and preferences.self_voicing == False:
                                jump basement_1_empty_rescue_controlled_start

                            "{i}• [[Slay the Princess.]{/i}" if witch_encountered == False and preferences.self_voicing == False:
                                jump basement_1_empty_rescue_controlled_start

                            "{i}• [[Slay the Princess.]{/i}" if witch_encountered == False and preferences.self_voicing == False:
                                jump basement_1_empty_rescue_controlled_start

                            "{i}• [[Slay the Princess.]{/i}" if witch_encountered == False and preferences.self_voicing == False:
                                jump basement_1_empty_rescue_controlled_start

                            "{i}• [[Slay the Princess.]{/i}" if witch_encountered == False and preferences.self_voicing == False:
                                jump basement_1_empty_rescue_controlled_start

                            "{i}• [[Slay the Princess.]{/i}" if witch_encountered == False and preferences.self_voicing == False:
                                jump basement_1_empty_rescue_controlled_start

                            "{i}• [[Slay the Princess.]{/i}" if witch_encountered == False and preferences.self_voicing == False:
                                jump basement_1_empty_rescue_controlled_start

                            "{i}• [[Slay the Princess.]{/i}" if witch_encountered == False and preferences.self_voicing == False:
                                jump basement_1_empty_rescue_controlled_start

                            "{i}• [[Slay the Princess.]{/i}" if witch_encountered == False and preferences.self_voicing == False:
                                jump basement_1_empty_rescue_controlled_start

                            "{i}• [[Slay the Princess.]{/i}" if witch_encountered == False and preferences.self_voicing == False:
                                jump basement_1_empty_rescue_controlled_start

                            "{i}• [[Slay the Princess.]{/i}" if witch_encountered == False and preferences.self_voicing == False:
                                jump basement_1_empty_rescue_controlled_start

                            "{i}• [[Warn her.]{/i}":
                                #y "Something's controlling me! Watch out!"
                                voice "audio/voices/ch1/empty/narrator/empty_n_78.flac"
                                show princess damsel 1 left onlayer front with dissolve
                                n "Stop that.\n"
                                show princess damsel left talk onlayer front with dissolve
                                voice "audio/voices/ch1/empty/princess/empty_p_65r.flac"
                                pmid "Something's come over you, hasn't it? Y-you know you don't have to do this, right?\n"
                                play audio "audio/one_shot/footstep_run_medium.flac"
                                voice "audio/voices/ch1/empty/narrator/empty_n_79.flac"
                                play audio "audio/one_shot/knife_slash.flac"
                                hide bg onlayer back
                                hide fury onlayer front
                                hide player onlayer inyourface
                                hide princess onlayer front
                                show bg black onlayer back at Position(ypos=1125)
                                show knife slice onlayer front at yflip, Position(ypos=1125)
                                n "Your body lunges forward, the blade held low, ready to sink into her heart.\n"
                                # REPLACE
                                play audio "audio/one_shot/collapse.flac"
                                voice "audio/voices/ch1/empty/narrator/empty_n_80.flac"
                                hide knife onlayer front
                                show player bloody knife onlayer inyourface at Position(ypos=1125)
                                show bg beastrescuecontroldodgecrouch onlayer back at Position(ypos=1125)
                                show beast rescue control dodge talk pity onlayer front at Position(ypos=1125)
                                with dissolve
                                # old line below
                                #n "But the Princess dodges... \n Wait... she dodges?\n"
                                # REPLACE WORDING
                                n "But the Princess dodges, stumbling back against the wall before the blade has a chance to connect.\n"
                                voice "audio/voices/ch1/empty/narrator/empty_n_81.flac"
                                n "Stop it! Stop trying to resist me! I'm trying to get you out of here alive.\n"
                                menu:
                                    extend ""

                                    "{i}• [[Slay the Princess.]{/i}" if witch_encountered == False:
                                        label basement_1_empty_rescue_controlled_2_start:
                                            $ small_yadj = False
                                            $ config.menu_include_disabled = False
                                            voice "audio/voices/ch1/empty/narrator/empty_n_36.flac"
                                            n "{i}Thank{/i} you.\n"
                                            # REPLACE
                                            #voice "audio/voices/ch1/empty/princess/empty_p_66.flac"
                                            voice "audio/voices/ch1/empty/princess/empty_p_66r.flac"
                                            show beast rescue control dodge talk onlayer front at Position(ypos=1125)
                                            with dissolve
                                            p "There's no getting through to you right now, is there?\n"
                                            #voice "audio/voices/ch1/empty/princess/empty_p_66b.flac"
                                            voice "audio/voices/ch1/empty/princess/empty_p_66rb.flac"
                                            show beast rescue control dodge talk 2 onlayer front at Position(ypos=1125)
                                            with dissolve
                                            sp "A betrayal of will is still a betrayal. You'll regret thinking of me as a helpless damsel.\n"
                                            # old line
                                            #sp "I'll do my best to make this quick.\n"
                                            jump basement_1_empty_beast

                                    "{i}• [[Slay the Princess.]{/i}" if witch_encountered == False and preferences.self_voicing == False:
                                        jump basement_1_empty_rescue_controlled_2_start

                                    "{i}• [[Slay the Princess.]{/i}" if witch_encountered == False and preferences.self_voicing == False:
                                        jump basement_1_empty_rescue_controlled_2_start

                                    "{i}• [[Slay the Princess.]{/i}" if witch_encountered == False and preferences.self_voicing == False:
                                        jump basement_1_empty_rescue_controlled_2_start

                                    "{i}• [[Slay the Princess.]{/i}" if witch_encountered == False and preferences.self_voicing == False:
                                        jump basement_1_empty_rescue_controlled_2_start

                                    "{i}• [[Slay the Princess.]{/i}" if witch_encountered == False and preferences.self_voicing == False:
                                        jump basement_1_empty_rescue_controlled_2_start

                                    "{i}• [[Slay the Princess.]{/i}" if witch_encountered == False and preferences.self_voicing == False:
                                        jump basement_1_empty_rescue_controlled_2_start

                                    "{i}• [[Slay the Princess.]{/i}" if witch_encountered == False and preferences.self_voicing == False:
                                        jump basement_1_empty_rescue_controlled_2_start

                                    "{i}• [[Slay the Princess.]{/i}" if witch_encountered == False and preferences.self_voicing == False:
                                        jump basement_1_empty_rescue_controlled_2_start

                                    "{i}• [[Slay the Princess.]{/i}" if witch_encountered == False and preferences.self_voicing == False:
                                        jump basement_1_empty_rescue_controlled_2_start

                                    "{i}• [[Slay the Princess.]{/i}" if witch_encountered == False and preferences.self_voicing == False:
                                        jump basement_1_empty_rescue_controlled_2_start

                                    "{i}• [[Slay the Princess.]{/i}" if witch_encountered == False and preferences.self_voicing == False:
                                        jump basement_1_empty_rescue_controlled_2_start

                                    "{i}• [[Slay the Princess.]{/i}" if witch_encountered == False and preferences.self_voicing == False:
                                        jump basement_1_empty_rescue_controlled_2_start

                                    "{i}• [[Slay the Princess.]{/i}" if witch_encountered == False and preferences.self_voicing == False:
                                        jump basement_1_empty_rescue_controlled_2_start

                                    "{i}• [[Resist.]{/i}" if damsel_encountered == False:
                                        $ config.menu_include_disabled = False
                                        $ current_princess = "damsel"
                                        voice "audio/voices/ch1/empty/narrator/empty_n_82.flac"
                                        n "The blade! Move. The. Blade!\n"
                                        play audio "audio/one_shot/footsteps_stone_short.flac"
                                        hide beast onlayer front
                                        hide bg onlayer back
                                        show bg beastrescuecontroldodgecrouch onlayer back at Position(ypos=1125)
                                        show blood trail onlayer front at Position(ypos=1400)
                                        show princess damsel 1 left approach onlayer front at Position(ypos=1125)
                                        with dissolve
                                        voice "audio/voices/ch1/empty/narrator/empty_n_82a.flac"
                                        n "As your body remains frozen in stubborn resistance, the Princess takes a cautious step forward.\n"
                                        play audio "audio/one_shot/footsteps_stone_short.flac"
                                        voice "audio/voices/ch1/empty/princess/empty_p_67r.flac"
                                        hide bg onlayer back
                                        hide blood trail onlayer front
                                        hide princess onlayer front
                                        show bg generic onlayer back at Position(ypos=1125)
                                        show princess damsel 1 center talk onlayer front at Position(ypos=1125)
                                        with dissolve
                                        p "We both know this isn't you...\n"
                                        $ blade_held = False
                                        $ default_mouse = "default"
                                        voice "audio/voices/ch1/empty/narrator/empty_nr_4.flac"
                                        play audio "audio/one_shot/knife_pickup.flac"
                                        show princess damsel 1 knife grab onlayer front at Position(ypos=1125)
                                        show player hand no knife onlayer inyourface at Position(ypos=1125)
                                        with dissolve
                                        n "She nervously reaches towards you and takes the blade from your infuriatingly rigid hands... What are you {i}doing{/i}?\n"
                                        voice "audio/voices/ch1/empty/princess/empty_p_d1.flac"
                                        show princess damsel 1 knife grab talk onlayer front at Position(ypos=1125)
                                        with dissolve
                                        p "I'm sorry... I'll try to be quick.\n"
                                        play audio "audio/one_shot/knife_stab.flac"
                                        voice "audio/voices/ch1/empty/narrator/empty_nr_5.flac"
                                        show princess damsel 1 stab onlayer front at Position(xpos=1125,ypos=1125)
                                        with dissolve
                                        n "She plunges it into your chest, tearing through flesh and sinew. It is {i}agony{/i}. But you aren't dead yet.\n"
                                        voice "audio/voices/ch1/empty/princess/empty_p_d2.flac"
                                        show princess damsel 1 stab 2 onlayer front at Position(xpos=1125,ypos=1125)
                                        with dissolve
                                        p "Oh no, I'm so sorry!\n"
                                        voice "audio/voices/ch1/empty/hero/empty_rh_1b.flac"
                                        hero "Stay strong. We can tough it out until it's done. For her sake.\n"
                                        voice "audio/voices/ch1/empty/narrator/empty_nr_6.flac"
                                        n "For {i}her{/i} sake? Don't you start pretending that dying a painful death is some sort of heroic gesture. The two of you have literally doomed {i}everyone{/i}.\n"
                                        voice "audio/voices/ch1/empty/narrator/empty_nr_7a.flac"
                                        n "Whatever. She sinks the blade into your chest again, and again, and again... and you feel {i}every inch{/i} of burning pain that slices its way into your body.\n"
                                        voice "audio/voices/ch1/empty/princess/empty_p_d3s.flac"
                                        show princess damsel stabbing onlayer front at Position(xpos=1125,ypos=1125) with dissolve
                                        p "I'm sorry I'm sorry I'm sorry!\n"
                                        voice "audio/voices/ch1/empty/hero/empty_rh_1a.flac"
                                        hero "She doesn't know how to use a knife, does she?\n"
                                        voice "audio/voices/ch1/empty/narrator/empty_nr_8.flac"
                                        n "Apparently not, though it doesn't matter how sloppy her blade work is, does it? A stab wound is still a stab wound, and it won't be long before you bleed out.\n"
                                        play secondary "audio/one_shot/knife_slash.flac"
                                        queue secondary "audio/one_shot/knife_stab.flac"
                                        voice "audio/voices/ch1/empty/princess/empty_p_d4b.flac"
                                        hide princess onlayer front
                                        hide bg onlayer back
                                        hide player onlayer inyourface
                                        show bg black onlayer back at Position(ypos=1125)
                                        with dissolve
                                        #show knife slice onlayer front at yflip, Position(ypos=1125)
                                        pmid "I'm so sorry!\n"
                                        #play secondary "audio/one_shot/knife_stab.flac"
                                        $ quick_menu = False
                                        play secondary "audio/one_shot/collapse.flac"
                                        voice "audio/voices/ch1/empty/narrator/empty_nr_9.flac"
                                        hide knife onlayer front
                                        show bg ceiling onlayer back at Position(ypos=1125)
                                        show princess damsel 1 loom sad onlayer front at Position(ypos=1125)
                                        with fade
                                        if persistent.quick_menu:
                                            $ quick_menu = True
                                        n "With one last thrust of the knife, your legs give out beneath you. You collapse to the floor, your blood pooling around you, your limbs unresponsive. The Princess stares down at your ruined chest as tears carve rivulets of pink down her blood-spattered cheeks.\n"
                                        voice "audio/voices/ch1/empty/hero/empty_h_29.flac"
                                        hero "It can't just end like this, right?\n"
                                        #voice "audio/voices/ch1/empty/narrator/empty_n_86.flac"
                                        voice "audio/voices/ch1/empty/narrator/empty_nr_10.flac"
                                        play audio "audio/one_shot/collapse.flac"
                                        show princess damsel 1 cheek onlayer front at Position(ypos=1125)
                                        with dissolve
                                        n "Oh, that's rich coming from you. As much as I'd prefer for things to have gone differently, I can't deny the reality of what's happened. The two of you made your choice. It's over.\n"
                                        voice "audio/voices/ch1/empty/narrator/empty_n_133.flac"
                                        n "Everything goes dark, and you die.\n"
                                        hide bg black onlayer back
                                        hide princess onlayer front
                                        with dissolve
                                        $ small_yadj = False
                                        jump start_2

                                    "{i}• [[Slay the Princess.]{/i}" if witch_encountered == False and preferences.self_voicing == False:
                                        jump basement_1_empty_rescue_controlled_2_start

                                    "{i}• [[Slay the Princess.]{/i}" if witch_encountered == False and preferences.self_voicing == False:
                                        jump basement_1_empty_rescue_controlled_2_start

                                    "{i}• [[Slay the Princess.]{/i}" if witch_encountered == False and preferences.self_voicing == False:
                                        jump basement_1_empty_rescue_controlled_2_start

                                    "{i}• [[Slay the Princess.]{/i}" if witch_encountered == False and preferences.self_voicing == False:
                                        jump basement_1_empty_rescue_controlled_2_start

                                    "{i}• [[Slay the Princess.]{/i}" if witch_encountered == False and preferences.self_voicing == False:
                                        jump basement_1_empty_rescue_controlled_2_start

                                    "{i}• [[Slay the Princess.]{/i}" if witch_encountered == False and preferences.self_voicing == False:
                                        jump basement_1_empty_rescue_controlled_2_start

                            "{i}• [[Slay the Princess.]{/i}" if witch_encountered == False and preferences.self_voicing == False:
                                jump basement_1_empty_rescue_controlled_start

                            "{i}• [[Slay the Princess.]{/i}" if witch_encountered == False and preferences.self_voicing == False:
                                jump basement_1_empty_rescue_controlled_start

                            "{i}• [[Slay the Princess.]{/i}" if witch_encountered == False and preferences.self_voicing == False:
                                jump basement_1_empty_rescue_controlled_start

                            "{i}• [[Slay the Princess.]{/i}" if witch_encountered == False and preferences.self_voicing == False:
                                jump basement_1_empty_rescue_controlled_start

            "{i}• [[Slay the Princess.]{/i}" if (basement_1_empty_save_lie_explore or basement_1_empty_save_explore == False) and (beast_encountered == False or witch_encountered == False or nightmare_encountered == False):
                default beast_1_both_arms = False
                $ basement_1_empty_wounded = True
                $ beast_1_both_arms = True
                $ blade_held = True
                $ default_mouse = "blood"
                play audio "audio/one_shot/knife_stab.flac"
                voice "audio/voices/ch1/empty/narrator/empty_n_88.flac"
                hide bg generic dark onlayer back
                hide knife dropped onlayer inyourface
                show bg generic onlayer back at Position(ypos=1125)
                show midground fury chain stabbed onlayer front at Position(ypos=1125)
                show beast rescue betray stab onlayer inyourface at Position(ypos=1125)
                with dissolve
                n "Without hesitation, you bring the blade down and plunge it into the Princess' back. {i}Finally{/i}.\n"
                play audio "audio/one_shot/thump.flac"
                voice "audio/voices/ch1/empty/narrator/empty_n_89.flac"
                hide midground onlayer front
                hide beast onlayer inyourface
                show beast rescue betray stab forced onlayer front at Position(ypos=1125)
                with dissolve
                n "The wound drives her to the ground.\n"
                voice "audio/voices/ch1/empty/hero/empty_h_30.flac"
                hero "Okay. There's no going back now. I'm with you to the end.\n"
                voice "audio/voices/ch1/empty/princess/empty_p_68.flac"
                show beast rescue betray stab glare onlayer front with dissolve
                sp "You– you bastard! Were you lying to me this whole time?\n"
                play audio "audio/one_shot/knife_slash.flac"
                voice "audio/voices/ch1/empty/narrator/empty_n_90.flac"
                hide bg onlayer back
                hide midground onlayer front
                hide beast onlayer inyourface
                show beast rescue betray flee onlayer front at Position(ypos=1125)
                with dissolve
                n "The Princess pushes away from you, the motion ripping the blade from her back.\n"
                voice "audio/voices/ch1/empty/narrator/empty_n_91.flac"
                show bg fury stub betrayed distant onlayer back at Position(ypos=1125)
                show beast rescue betray distant onlayer front at Position(ypos=1125)
                with dissolve
                n "Wounded, but still alive, she crouches on all fours in the corner of the room and meets your eyes with the ferocity of a cornered predator.\n"
                voice "audio/voices/ch1/empty/princess/empty_p_69.flac"
                show beast rescue betray distant talk onlayer front with dissolve
                sp "You've made a terrible enemy, and there's nothing in the world that can possibly save you from me.\n"
                voice "audio/voices/ch1/empty/hero/empty_h_31a.flac"
                show beast rescue betray distant onlayer front with dissolve
                hero "I thought we had the upper hand, but it's as if she's barely even threatened by us.\n"
                #hero "Do you hear the conviction in her voice? Do you see that razor sharpness in her gaze? I don't think she's bluffing. I thought we had the upper hand, but it's as if she's barely even threatened by us.\n"
                voice "audio/voices/ch1/empty/narrator/empty_n_92.flac"
                n "It's an act. She's wounded and unarmed. There's nothing she can do to hurt you.\n"
                voice "audio/voices/ch1/empty/hero/empty_h_32.flac"
                hero "I'm not so sure...\n"
                voice "audio/voices/ch1/empty/narrator/empty_n_93.flac"
                n "Don't waver now.\n"
                voice "audio/voices/ch1/empty/narrator/empty_n_94.flac"
                play audio "audio/one_shot/tackle.flac"
                hide bg onlayer back
                hide beast onlayer front
                show bg generic onlayer back at Position(ypos=1125)
                show beast rescue betray lunge onlayer front at Position(ypos=1125)
                with dissolve
                n "As you ready your blade to deliver a lethal blow, she lunges at your legs with the same animal ferocity she used to tear at her arm.\n"
                play audio "audio/one_shot/rip_and_tear_knife.flac"
                voice "audio/voices/ch1/empty/narrator/empty_n_95.flac"
                hide bg onlayer back
                hide beast onlayer front
                show bg generic dark onlayer back at Position(ypos=1125)
                show battle beast rescue onlayer front at Position(ypos=1125)
                #show battle1 beast rescue betray onlayer front at Position(ypos=1125)
                #show battle2 beast rescue betray onlayer front at Position(ypos=1125)
                #show battle3 beast rescue betray onlayer front at Position(ypos=1125)
                with Dissolve(0.75)
                n "Your blade cuts into her again and again as you're tackled to the ground, your body racked with pain as she rips into you with tooth and claw.\n"
                voice "audio/voices/ch1/empty/hero/empty_h_33.flac"
                hero "Forget about trying to rescue her. This is about survival now. Give her everything you've got.\n"
                menu:
                    extend ""

                    "{i}• [[Slay the Princess.]{/i}":
                        voice "audio/voices/ch1/empty/narrator/empty_n_96.flac"
                        n "Though your nerves are seizing with pain, you know you've done your fair share of damage as well, your blade having left deep gashes in the Princess' back.\n"
                        voice "audio/voices/ch1/empty/narrator/empty_n_97.flac"
                        play audio "audio/one_shot/collapse.flac"
                        hide battle onlayer front
                        show bg beastrescuecontroldodgecrouch onlayer back at Position(ypos=1125)
                        show beast rescue betray quit onlayer front at Position(ypos=1125)
                        show player bloody knife onlayer inyourface at Position(ypos=1125)
                        with dissolve
                        n "You seize a moment of hesitation to throw her off of you and shakily push yourself back to your knees.\n"
                        voice "audio/voices/ch1/empty/hero/empty_h_34.flac"
                        hero "We can still turn this around.\n"
                        menu:
                            extend ""

                            "{i}• [[Give up.]{/i}" if beast_encountered == False:
                                $ current_princess = "beast"
                                play audio "audio/one_shot/knife_bounce_several.flac"
                                $ blade_held = False
                                $ default_mouse = "default"
                                voice "audio/voices/ch1/empty/narrator/empty_n_98.flac"
                                hide player onlayer inyourface
                                show beast rescue betray thrown onlayer front
                                with dissolve
                                n "Are you serious? {i}Sigh{/i}. As what's left of your blood pools around you on the cobblestone floor, the blade falls from your trembling hands and clatters uselessly against the ground. I suppose you simply lacked the will to finish the job.\n"
                                voice "audio/voices/ch1/empty/narrator/empty_n_99.flac"
                                play audio "audio/one_shot/knife_kicked.flac"
                                show beast rescue betray die onlayer front
                                with dissolve
                                n "The Princess, wounded but still alive, nervously jumps at the blade and kicks it far away from you before retreating into a dark corner of the room.\n"
                                #play audio "audio/one_shot/blood_drip.flac"
                                voice "audio/voices/ch1/empty/narrator/empty_n_100.flac"
                                n "Her shining eyes watch you from the darkness, unblinking and curious as you bleed out.\n"
                                voice "audio/voices/ch1/empty/narrator/empty_n_101.flac"
                                n "We can only hope the wounds you managed to inflict will be enough to at least delay her escape from this place. If we're very lucky, they'll kill her before she can reach the outside world.\n"
                                voice "audio/voices/ch1/empty/princess/empty_p_70.flac"
                                sp "After all this time alone, I thought I'd finally found a friend. But you were just another monster, weren't you?\n"
                                voice "audio/voices/ch1/empty/hero/empty_h_35.flac"
                                hero "This is the end, isn't it?\n"
                                $ persistent.death_count += 1
                                voice "audio/voices/ch1/empty/narrator/empty_n_102.flac"
                                stop music fadeout 1.0
                                stop sound fadeout 1.0
                                hide bg onlayer back
                                hide beast onlayer front
                                show bg black onlayer back at Position(ypos=1125)
                                with dissolve
                                n "Before you can answer, everything goes dark, and you die.\n"
                                hide bg black onlayer back with dissolve
                                jump start_2

                            "{i}• [[Finish the job.]{/i}" if witch_encountered == False:
                                default witch_betrayal_mutual = False
                                $ witch_betrayal_mutual = True
                                $ loop_1_princess_killed = True
                                $ current_princess = "witch"
                                $ current_mutual_death += 1
                                voice "audio/voices/ch1/empty/narrator/empty_n_103.flac"
                                n "You steel your resolve and take another step closer to the Princess. You probably won't make it out of here alive, but you can still make sure that she won't make it out of here, either.\n"
                                voice "audio/voices/ch1/empty/hero/empty_h_36.flac"
                                hero "Excuse me? What's that about not making it out of here alive?\n"
                                voice "audio/voices/ch1/empty/narrator/empty_n_104.flac"
                                n "Do you think this is what I wanted to happen? I have a duty to state the facts of the situation, and honestly, it's a miracle anyone in this room is still standing right now. Don't act so surprised.\n"
                                voice "audio/voices/ch1/empty/narrator/empty_n_105.flac"
                                n "Can you not feel all those gashes and holes pulling you apart? If the Princess doesn't do you in here, blood loss is certain to finish the job.\n"
                                voice "audio/voices/ch1/empty/narrator/empty_n_106.flac"
                                hide bg onlayer back
                                hide beast onlayer front
                                hide player onlayer inyourface
                                show bg generic dark onlayer back at Position(ypos=1125)
                                show beast rescue betray lunge onlayer front at Position(ypos=1125)
                                with dissolve
                                n "You take another step forward, and the Princess lunges towards you.\n"
                                play audio "audio/one_shot/rip_and_tear_knife.flac"
                                voice "audio/voices/ch1/empty/narrator/empty_n_107.flac"
                                play audio "audio/one_shot/knife_slash.flac"
                                hide bg onlayer back
                                hide beast onlayer front
                                show bg black onlayer back at Position(ypos=1125)
                                show knife slice onlayer front at yflip, Position(ypos=1125)
                                n "The two of you enter one last exchange. A flurry of blade, and claw and fleshy ribbons. And then you stop, neither you nor Princess able to go any further.\n"
                                $ blade_held = False
                                $ default_mouse = "default"
                                voice "audio/voices/ch1/empty/narrator/empty_n_108.flac"
                                play audio "audio/one_shot/collapse.flac"
                                play secondary "audio/one_shot/knife_bounce_several.flac"
                                hide knife onlayer front
                                show bg beastrescuecontroldodgecrouch onlayer back at Position(ypos=1125)
                                show beast rescue betray die together onlayer front at Position(ypos=1125)
                                with dissolve
                                n "You collapse on the ground, and the Princess collapses beside you. Blood pools around you both and you watch each other fade away.\n"
                                voice "audio/voices/ch1/empty/princess/empty_p_70.flac"
                                show beast rescue betray die together talk hurt onlayer front with dissolve
                                sp "After all this time alone, I thought I'd finally found a friend. But you were just another monster, weren't you?\n"
                                play audio "audio/one_shot/blood_drip.flac"
                                voice "audio/voices/ch1/empty/narrator/empty_n_109.flac"
                                n "Silence, as the room starts to get fuzzy around you.\n"
                                voice "audio/voices/ch1/empty/narrator/empty_n_110.flac"
                                n "You've paid a terrible price, but you've saved us all. It's over.\n"
                                voice "audio/voices/ch1/empty/princess/empty_p_71.flac"
                                show beast rescue betray die together talk angry onlayer front with dissolve
                                sp "If you think this is it... you're sorely mistaken. One way or another, I'll make sure you pay for this.\n"
                                #voice "audio/voices/ch1/empty/hero/empty_h_37.flac"
                                #show beast rescue betray die together dead onlayer front with dissolve
                                #hero "There it is again, that razor-sharp look in her eyes and that terrifying conviction in her words.\n"
                                $ persistent.death_count += 1
                                voice "audio/voices/ch1/empty/narrator/empty_n_111.flac"
                                stop music fadeout 1.0
                                stop sound fadeout 1.0
                                hide bg onlayer back
                                hide beast onlayer front
                                show bg black onlayer back at Position(ypos=1125)
                                with dissolve
                                n "But you don't have time to worry about such things. Everything goes dark, and you die.\n"
                                hide bg black onlayer back with dissolve
                                jump start_2

                            "{i}• [[Run for the stairs and lock her in the basement. Maybe she'll bleed out.]{/i}" if nightmare_encountered == False:
                                $ nightmare_join_fled = True
                                $ current_princess = "nightmare"
                                voice "audio/voices/ch1/empty/narrator/empty_n_112.flac"
                                n "The Princess is still chained to the wall. There's nothing she can do to stop you from getting out of here.\n"
                                voice "audio/voices/ch1/empty/hero/empty_h_38.flac"
                                hero "What if she doesn't succumb to her wounds? Whatever she is, she's so much more dangerous than I thought she'd be.\n"
                                play audio "audio/one_shot/footstep_run_medium.flac"
                                voice "audio/voices/ch1/empty/narrator/empty_n_113.flac"
                                hide player onlayer inyourface
                                hide bg onlayer back
                                hide beast onlayer front
                                show basement stairs open onlayer front at Position(ypos=1125)
                                with dissolve
                                n "You rush up the stairs and dive past the threshold. You're safe. For now.\n"
                                $ quick_menu = False
                                hide basement onlayer front
                                scene bg black
                                with fade
                                jump nightmare_join



label basement_1_empty_retrieve_knife:
    $ basement_1_empty_wounded = True
    $ basement_1_empty_arm_loss_known = True
    voice "audio/voices/ch1/empty/narrator/empty_n_114.flac"
    play sound "audio/looping/ambient_cabin.ogg"
    play audio "audio/one_shot/knife_pickup.flac"
    $ quick_menu = False
    hide basement onlayer front
    scene farback interior cabin onlayer farback at Position(ypos=1125)
    show bg cabin int onlayer back at Position(ypos=1125)
    show door cabin3 onlayer back at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    $ blade_held = True
    $ default_mouse = "blade"
    n "You rush up to the first floor, grabbing the blade, both yours and the world's only possible salvation.\n"
    #voice "audio/voices/ch1/empty/narrator/empty_n_115.flac"
    #n "And then you turn back to face the open doorway.\n"
    voice "audio/voices/ch1/empty/hero/empty_h_39.flac"
    hero "Okay. If we're sure about this decision, I'll support it. I suppose we have a world to save, after all...\n"
    stop sound fadeout 1.0
    play audio "audio/one_shot/footsteps_creaky.flac"
    voice "audio/voices/ch1/empty/narrator/empty_n_116.flac"
    play sound "audio/looping/ambient_basement_interior.ogg"
    $ quick_menu = False
    hide farback onlayer farback
    hide bg onlayer back
    hide door onlayer back
    scene bg basement stairs onlayer farback at Position(ypos=1125)
    show front basement stairs onlayer farback at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    n "You slowly creep down the basement stairs. It's quiet.\n"
    $ quick_menu = False
    play audio "audio/one_shot/footsteps_creaky.flac"
    # REPLACE
    voice "audio/voices/ch1/empty/narrator/empty_n_117.flac"
    hide bg basement stairs onlayer farback at Position(ypos=1125)
    hide front basement stairs onlayer farback at Position(ypos=1125)
    with fade
    scene bg basement distant onlayer farback at Position(ypos=1125)
    show back beast 2 distant onlayer back at Position(ypos=1125)
    show arm distant onlayer back at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    n "Where the Princess sat only a moment ago, there's only a severed arm, its cooling flesh still chained to the wall. And {i}she{/i} is nowhere to be seen.\n" id basement_1_empty_retrieve_knife_71d7670c
    voice "audio/voices/ch1/empty/hero/empty_h_40.flac"
    hero "Is it just me or did this room get a lot bigger?\n"
    label basement_1_empty_retrieve_knife_stairs:
        default basement_1_empty_retrieve_knife_stairs_explore_hello = False
        default basement_1_empty_knife_hesitate = False
        default empty_1_can_witch = True
        menu:
            extend ""

            "{i}• (Explore) ''Hello?''{/i}" if basement_1_empty_retrieve_knife_stairs_explore_hello == False and beast_encountered == False:
                $ basement_1_empty_retrieve_knife_stairs_explore_hello = True
                $ basement_1_empty_knife_hesitate = True
                $ empty_1_can_witch = False
                voice "audio/voices/ch1/empty/princess/empty_p_72.flac"
                sp "Why don't you come closer? I have something to show you.\n"
                jump basement_1_empty_retrieve_knife_stairs

            "{i}• (Explore) ''I think we got off on the wrong foot. Do you think we can start over?''{/i}" if basement_1_empty_retrieve_knife_stairs_explore_hello == False and beast_encountered == False:
                $ basement_1_empty_retrieve_knife_stairs_explore_hello = True
                $ basement_1_empty_knife_hesitate = True
                $ empty_1_can_witch = False
                voice "audio/voices/ch1/empty/narrator/empty_n_118.flac"
                n "Oh, you {i}coward{/i}.\n"
                voice "audio/voices/ch1/empty/princess/empty_p_73.flac"
                sp "No. I don't think we can.\n"
                voice "audio/voices/ch1/empty/princess/empty_p_72.flac"
                sp "Why don't you come closer? I have something to show you.\n"
                jump basement_1_empty_retrieve_knife_stairs

            "{i}• She's lost an arm. I'm locking her down there and letting her bleed out.{/i}" if nightmare_encountered == False:
                voice "audio/voices/ch1/empty/hero/empty_h_41.flac"
                hero "This is a dangerous play. Who's to say she'll actually succumb to her wounds?\n"
                voice "audio/voices/ch1/empty/narrator/empty_n_119.flac"
                n "She doesn't have a weapon and she's missing an arm. You can finish this, right here, right now.\n"
                menu:
                    extend ""

                    "{i}• (Lock her away) Tell you what. I'll even stay here for a while to make sure she's dead.{/i}":
                        label nightmare_join:
                            $ current_princess = "nightmare"
                            #image door shake nightmare movie = Movie(play="images/backgrounds/nightmare_route/door_shake_nightmare.ogg", side_mask=True)
                            stop sound fadeout 1.0
                            play secondary "audio/one_shot/footstep_run_medium.flac"
                            queue secondary "audio/one_shot/door_close.flac"
                            play sound "audio/looping/ambient_cabin.ogg" loop
                            voice "audio/voices/ch1/empty/narrator/empty_n_120.flac"
                            $ quick_menu = False
                            hide bg onlayer farback
                            hide back onlayer back
                            hide arm onlayer back
                            scene farback interior cabin onlayer farback at Position(ypos=1125)
                            show bg interior cabin nightmare1 onlayer back at Position(ypos=1125)
                            #show door interior cabin onlayer back at Position(ypos=1125)
                            #show table cabin int blocked onlayer back at Position(ypos=1125)
                            with fade
                            if persistent.quick_menu:
                                $ quick_menu = True
                            n "You close the basement door, locking it behind you and quickly barricading it with the heavy wooden table that once held the blade.\n"
                            if nightmare_no_wounds:
                                voice "audio/voices/ch1/empty/hero/empty_h_42.flac"
                                hero "Okay. We can make this work.\n"
                            else:
                                voice "audio/voices/ch1/empty/hero/empty_h_43.flac"
                                hero "Okay. We can make this work. She has an awful wound and we have all the time in the world. Playing jailkeeper for a while might make things a little easier.\n"
                            voice "audio/voices/ch1/empty/narrator/empty_n_121.flac"
                            n "You settle in against the far wall to watch the basement door.\n"
                            voice "audio/voices/ch1/empty/narrator/empty_n_122.flac"
                            n "It isn't long before you start to drift off, your eyelids heavy with fatigue. But sleep doesn't come. Instead your rest is broken by a piercing, wailing voice calling out to you from the other side of the door.\n"
                            play secondary "audio/looping/knock_looping.ogg" loop
                            voice "audio/voices/ch1/empty/princess/empty_p_75.flac"
                            sp "I know you're still there. Why don't you make things easier on yourself and let me out?\n"
                            voice "audio/voices/ch1/empty/princess/empty_p_75b.flac"
                            sp "It's not like this little door'll hold for very long anyways... and it's probably a good idea to try and get back on my good side.\n"
                            voice "audio/voices/ch1/empty/hero/empty_h_44.flac"
                            hero "She sounds... terrifying. Like she's less of the Princess you saw and more like something out of a nightmare.\n"
                            voice "audio/voices/ch1/empty/narrator/empty_n_123.flac"
                            n "As she violently rattles the door, you do your best to shut her out of your mind.\n"
                            voice "audio/voices/ch1/empty/princess/empty_p_76.flac"
                            sp "When I get out of here I'm going to pick you apart piece by piece. I won't forget what you did, and I'll never forgive it.\n"
                            voice "audio/voices/ch1/empty/princess/empty_p_76b.flac"
                            sp "You don't know the kind of enemy you've made tonight.\n"
                            voice "audio/voices/ch1/empty/hero/empty_h_45.flac"
                            hero "It doesn't sound like she's getting any weaker...\n"
                            voice "audio/voices/ch1/empty/narrator/empty_n_124.flac"
                            n "No. It doesn't.\n"
                            menu:
                                extend ""

                                "{i}• ''Threaten me all you want! All it does is ease my guilty conscience.''{/i}":
                                    voice "audio/voices/ch1/empty/princess/empty_p_77.flac"
                                    sp "These aren't threats. These are {i}promises{/i}. Sooner or later you're going to have to sleep, and I'll make sure you never see the light of day again.\n"

                                "{i}• ''Whatever you are, you're not a Princess. Go ahead and waste your energy. I'll be waiting for you.''{/i}" if blade_held:
                                    voice "audio/voices/ch1/empty/princess/empty_p_78.flac"
                                    sp "I wouldn't be so sure about outlasting me. You're so... brittle. So go ahead. Rest. Do whatever you think will help you be prepared. But know that I am coming for you, and that when I find you, I will make you hurt.\n"

                                "{i}• ''So all of that was just an act, wasn't it? You're not really innocent or harmless. You're not even a princess. You're a {i}monster{/i}.''{/i}" if blade_held == False:
                                    voice "audio/voices/ch1/empty/princess/empty_p_79.flac"
                                    sp "I can be innocent and harmless... if I want to be. Teasing me with fresh air and a chance to finally live freely doesn't inspire me to play nice.\n"

                                "{i}• ''Bang on the door all you want. It'll only make you bleed out faster.''{/i}" if basement_1_empty_wounded:
                                    if basement_1_empty_arm_loss_known:
                                        voice "audio/voices/ch1/empty/princess/empty_p_80.flac"
                                        sp "Do you think losing an arm is actually enough to do me in? I can always find another. I'm not as frail as you think.\n"
                                    else:
                                        voice "audio/voices/ch1/empty/princess/empty_p_81.flac"
                                        sp "Do you think a couple cuts is enough to do me in? I'm not as frail as you think.\n"

                                "{i}• Ignore her and go to sleep.{/i}":
                                    voice "audio/voices/ch1/empty/hero/empty_h_46.flac"
                                    hero "Just ignore her. Maybe the banging and wailing will stop if you just don't pay attention to it.\n"

                            voice "audio/voices/ch1/empty/narrator/empty_n_125.flac"
                            $ quick_menu = False
                            hide farback interior cabin onlayer farback
                            #hide bg interior cabin no table onlayer back
                            hide door interior cabin onlayer back
                            #hide table cabin int blocked onlayer back
                            show bg black onlayer back at Position(ypos=1125)
                            with fade
                            n "You put the Princess' threats out of your mind as best as you can and huddle up against the wall.\n"
                            stop secondary fadeout 1.0
                            voice "audio/voices/ch1/empty/narrator/empty_n_126.flac"
                            play secondary "audio/looping/uncomfortable ambiance heightened.ogg" loop
                            hide bg onlayer back
                            scene farback interior cabin onlayer farback at Position(ypos=1125)
                            show bg cabin nightmare start onlayer back at Position(ypos=1125)
                            show filter cabin int nightmare onlayer back at Position(ypos=1125)
                            with fade
                            if persistent.quick_menu:
                                $ quick_menu = True
                            n "You jolt awake in the middle of the night to silence in the cabin. The ruckus has stopped, and the door to the basement is ajar, its lock broken and the table shoved out the way.\n"
                            voice "audio/voices/ch1/empty/hero/empty_h_47.flac"
                            hero "Where is she?\n"
                            voice "audio/voices/ch1/empty/princess/empty_p_82.flac"
                            play audio "audio/one_shot/static_short.flac"
                            if basement_1_empty_arm_loss_known:
                                show nightmare approach 1 onlayer front at Position(ypos=1125)
                                show arm nightmare approach 1 onlayer inyourface at Position(ypos=1125)
                                with dissolve
                            else:
                                show nightmare limb approach 1 onlayer front at Position(ypos=1125)
                                with dissolve
                            sp "Thanks for helping me get out of that awful basement.\n"
                            voice "audio/voices/ch1/empty/narrator/empty_n_127.flac"
                            play audio "audio/one_shot/static_short2.flac"
                            if basement_1_empty_arm_loss_known:
                                show nightmare approach 2 onlayer front at Position(ypos=1125)
                                show arm nightmare approach 2 onlayer inyourface at Position(ypos=1125)
                                with dissolve
                            else:
                                show nightmare limb approach 2 onlayer front
                                with dissolve
                            n "You try and stumble to your feet, but as the Princess draws near, it's as though your body simply stops working.\n"
                            voice "audio/voices/ch1/empty/narrator/empty_n_128.flac"
                            n "It isn't all at once. The paralysis comes in waves. First your toes go numb, and then your feet, and then your legs. You lie prone on the floor of the cabin, unable to do anything but witness her approach.\n"
                            voice "audio/voices/ch1/empty/hero/empty_h_48.flac"
                            hero "Whose side are you on?\n"
                            voice "audio/voices/ch1/empty/narrator/empty_n_129.flac"
                            n "Yours, of course. But I have a duty to uphold the truth. Lying about the facts of the situation doesn't change them.\n"
                            voice "audio/voices/ch1/empty/princess/empty_p_83.flac"
                            sp "So helpless. I can take my time with you, can't I?\n"
                            voice "audio/voices/ch1/empty/narrator/empty_n_130.flac"
                            play audio "audio/one_shot/static_short3.flac"
                            if basement_1_empty_arm_loss_known:
                                show nightmare approach 3 onlayer front at Position(ypos=1125)
                                show arm nightmare approach 3 onlayer inyourface at Position(ypos=1125)
                                with dissolve
                            else:
                                show nightmare limb approach 3 onlayer front at Position(ypos=1125)
                                with dissolve
                            n "She steps closer, one silent footfall at a time, cocking her head in curiosity as you feel your organs shutting down one by one.\n"
                            voice "audio/voices/ch1/empty/princess/empty_p_84.flac"
                            play audio "audio/one_shot/static_short.flac"
                            if basement_1_empty_arm_loss_known:
                                show nightmare approach 4 onlayer front at Position(ypos=1125)
                                show arm nightmare approach 4 onlayer inyourface at Position(ypos=1125)
                                with dissolve
                            else:
                                hide nightmare onlayer front
                                show nightmare limb approach 4 onlayer inyourface at Position(ypos=1125)
                                with dissolve
                            sp "Or maybe I can't take my time with you. You don't look well. A little green around the gills...\n"
                            voice "audio/voices/ch1/empty/princess/empty_p_85.flac"
                            sp "What a shame. If you'd only helped me get out of here. We could have done such wonderful things together.\n"
                            voice "audio/voices/ch1/empty/narrator/empty_n_131.flac"
                            n "Your lungs stop drawing in breath, and your heart freezes in your chest. You have seconds left.\n"
                            voice "audio/voices/ch1/empty/princess/empty_p_86.flac"
                            sp "I'd say better luck next time, but we both know that this is the end, don't we?\n"
                            voice "audio/voices/ch1/empty/hero/empty_h_49.flac"
                            $ quick_menu = False
                            stop music fadeout 1.0
                            stop sound fadeout 1.0
                            stop secondary fadeout 1.0
                            hide door onlayer back
                            hide filter onlayer back
                            hide nightmare onlayer inyourface
                            hide nightmare onlayer front
                            hide arm onlayer inyourface
                            hide farback onlayer farback
                            hide bg onlayer back
                            #hide table onlayer back
                            show bg black onlayer back at Position(ypos=1125)
                            with fade
                            hero "It can't be. This can't actually be how everything ends...\n"
                            voice "audio/voices/ch1/empty/narrator/empty_n_132.flac"
                            n "I'm sorry, but it is.\n"
                            $ persistent.death_count += 1
                            voice "audio/voices/ch1/empty/narrator/empty_n_133.flac"
                            n "Everything goes dark, and you die.\n"
                            hide bg black onlayer back with dissolve
                            jump start_2

                    "{i}• You're right. Let's finish this.{/i}" if witch_encountered == False or (beast_encountered == False and empty_1_can_witch == False):
                        jump beast_arm_missing_finish_join


            "{i}• Let's finish this.{/i}":
                label beast_arm_missing_finish_join:
                #voice "audio/voices/ch1/empty/narrator/empty_n_134.flac"
                #n "You continue down the stairs, your eyes darting to the corners of the room. You don't see her."
                voice "audio/voices/ch1/empty/narrator/empty_n_134alt.flac"
                n "Your eyes dart to the corners of the room. You don't see her.\n"
                voice "audio/voices/ch1/empty/hero/empty_h_50.flac"
                hero "Where is she?\n"
                menu:
                    extend ""

                    "{i}• Investigate the arm.{/i}" if witch_encountered == False:
                        default loop_1_locked = False
                        $ loop_1_locked = True
                        $ current_princess = "witch"
                        $ gallery_zch1.unlock_item(17)
                        $ renpy.save_persistent()
                        voice "audio/voices/ch1/empty/narrator/empty_n_135.flac"
                        play audio "audio/one_shot/princess_flee.flac"
                        hide bg onlayer farback
                        hide back onlayer back
                        hide arm onlayer back
                        show farbg flee back onlayer farback at Position(ypos=1125)
                        show bg flee onlayer back at Position(ypos=1125)
                        show beast armless flee onlayer back at Position(ypos=1125)
                        with dissolve
                        n "As you step towards the severed limb, you hear the pattering of feet behind you, soft against the basement floor, then loud and desperate against the stairs.\n"
                        $ quick_menu = False
                        hide farbg onlayer farback
                        hide bg onlayer back
                        hide beast onlayer back
                        show bg black onlayer back at Position(ypos=1125)
                        with fade
                        if persistent.quick_menu:
                            $ quick_menu = True
                        voice "audio/voices/ch1/empty/narrator/empty_n_136.flac"
                        play audio "audio/one_shot/footstep_run_medium.flac"
                        n "You turn to chase after the Princess, but she's fast and has too much of a lead.\n"
                        play audio "audio/one_shot/door_close.flac"
                        voice "audio/voices/ch1/empty/narrator/empty_n_137.flac"
                        $ quick_menu = False
                        hide bg onlayer back
                        show basement stairs closed onlayer front at Position(ypos=1125)
                        with fade
                        if persistent.quick_menu:
                            $ quick_menu = True
                        n "She slams door behind her before you can make it to the top of the stairs. The lock clicks into place.\n"
                        voice "audio/voices/ch1/empty/hero/empty_h_51.flac"
                        hero "No!\n"
                        voice "audio/voices/ch1/empty/princess/empty_p_87.flac"
                        sp "Thanks for letting me out. I'd return the favor, but I think we both know that I can't trust you to let me stay free.\n"
                        if basement_1_empty_not_worth_risk:
                            voice "audio/voices/ch1/empty/princess/empty_p_88.flac"
                            sp "You should understand... it just isn't 'worth the risk.'\n"
                        voice "audio/voices/ch1/empty/narrator/empty_n_138.flac"
                        play audio "audio/one_shot/princess_leave.flac"
                        n "With those parting words the Princess walks away, her quiet footsteps eventually fading as she leaves you and the cabin to rot. You're stuck here. Alone.\n"
                        voice "audio/voices/ch1/empty/hero/empty_h_52.flac"
                        hero "It can't just end like this, right?\n"
                        voice "audio/voices/ch1/empty/narrator/empty_n_139.flac"
                        n "As much as I'd prefer for things to have gone differently, I can't deny the reality of what's happened. I'm sorry, but it's over.\n"
                        voice "audio/voices/ch1/empty/narrator/empty_n_140.flac"
                        n "You don't know how much time passes before the end, but eventually it comes.\n"
                        voice "audio/voices/ch1/empty/narrator/empty_n_141.flac"
                        $ persistent.death_count += 1
                        stop music fadeout 1.0
                        stop secondary fadeout 1.0
                        stop sound fadeout 1.0
                        hide basement onlayer front
                        hide bg onlayer back
                        hide beast onlayer front
                        show bg black onlayer back at Position(ypos=1125)
                        with dissolve
                        n "The world ends, and you end with it.\n"
                        hide bg black onlayer back with dissolve
                        jump start_2


                    "{i}• [[Close the door behind you.]{/i}":
                        play audio "audio/one_shot/door_close.flac"
                        voice "audio/voices/ch1/empty/narrator/empty_n_142.flac"
                        $ quick_menu = False
                        hide bg onlayer farback
                        hide back onlayer back
                        hide arm onlayer back
                        show basement stairs closed onlayer front at Position(ypos=1125)
                        with fade
                        if persistent.quick_menu:
                            $ quick_menu = True
                        n "You close the door behind you. Almost magically, its locks immediately click into place. Maybe they'll open if you finish the job.\n"
                        play audio "audio/one_shot/footsteps_creaky.flac"
                        #voice "audio/voices/ch1/empty/hero/empty_h_53.flac"
                        $ quick_menu = False
                        hide basement onlayer front
                        scene bg basement distant onlayer farback at Position(ypos=1125)
                        show back beast 2 distant onlayer back at Position(ypos=1125)
                        show arm distant onlayer back at Position(ypos=1125)
                        with fade
                        if persistent.quick_menu:
                            $ quick_menu = True
                        #hero "This isn't right. Where is she?\n"
                        menu:
                            extend ""

                            "{i}• [[Investigate the arm.]{/i}":
                                voice "audio/voices/ch1/empty/narrator/empty_n_143.flac"
                                play audio "audio/one_shot/footsteps_hike_short.flac"
                                hide bg onlayer farback
                                hide back onlayer back
                                hide arm onlayer back
                                show arm close onlayer front at Position(ypos=1125)
                                with dissolve
                                n "You step forward to investigate the severed limb.\n"
                                hide arm onlayer front
                                show bg generic dark onlayer back at Position(ypos=1125)
                                show blood trail onlayer front at Position(ypos=1125)
                                with dissolve
                                voice "audio/voices/ch1/empty/narrator/empty_n_143b.flac"
                                n "A trail of blood leads from its jagged stump into a dark corner of the basement.\n"
                                voice "audio/voices/ch1/empty/narrator/empty_n_144.flac"
                                play audio "audio/one_shot/run_tackle.flac"
                                show blood trail onlayer front with hpunch
                                n "And then you hear the quiet patter of feet against the basement floor, and there's suddenly a weight on your shoulders. The Princess tears into you.\n"
                                voice "audio/voices/ch1/empty/narrator/empty_n_145.flac"
                                play audio "audio/one_shot/rip_and_tear_knife.flac"
                                hide blood onlayer front
                                hide bg onlayer back
                                show battle beast armless onlayer front at Position(ypos=1125)
                                #show battle1 beast armless onlayer front at Position(ypos=1125)
                                #show battle2 beast armless onlayer front at Position(ypos=1125)
                                #show battle3 beast armless onlayer front at Position(ypos=1125)
                                with Dissolve(0.75)
                                n "Her teeth and claws are unnaturally sharp, ripping into your shoulders, digging into your throat. You fall to the ground, the Princess eagerly tearing at your flesh.\n"
                                label basement_1_empty_sneak_join:
                                    if basement_1_empty_knife_hesitate:
                                        $ current_princess = "beast"
                                        $ blade_held = False
                                        $ default_mouse = "default"
                                        voice "audio/voices/ch1/empty/narrator/empty_n_146a.flac"
                                        play audio "audio/one_shot/knife_bounce_several.flac"
                                        hide bg onlayer back
                                        hide battle onlayer front
                                        show bg beastrescuecontroldodgecrouch onlayer back at Position(ypos=1125)
                                        show beast rescue control fail onlayer front at Position(ypos=1125)
                                        with dissolve
                                        n "Her ferocity overwhelms you, and as the Princess rends flesh from bone, your limp fingers lose their grip on the blade. It slips from your hand, your one last means of defense lying useless beside you in a pool of your cooling blood. I suppose you just lacked the will to fight back.\n"
                                        jump empty_beast_join

                                    voice "audio/voices/ch1/empty/hero/empty_h_54.flac"
                                    hero "Holy {i}shit{/i}. What {i}is{/i} she?!\n"
                                    menu:
                                        extend ""

                                        "{i}• [[Give up.]{/i}" if beast_encountered == False:
                                            $ current_princess = "beast"
                                            $ blade_held = False
                                            $ default_mouse = "default"
                                            voice "audio/voices/ch1/empty/narrator/empty_n_146.flac"
                                            play audio "audio/one_shot/knife_bounce_several.flac"
                                            hide bg onlayer back
                                            hide battle onlayer front
                                            show bg beastrescuecontroldodgecrouch onlayer back at Position(ypos=1125)
                                            show beast rescue control fail onlayer front at Position(ypos=1125)
                                            with dissolve
                                            n "Are you serious? {i}Sigh{/i}. As the Princess rends flesh from bone, your limp fingers can no longer hold the blade. It slips from your hand, your one last means of defense lying useless beside you in a pool of your cooling blood. I suppose you just lacked the will to fight back.\n"
                                            label empty_beast_join:
                                                voice "audio/voices/ch1/empty/hero/empty_h_55.flac"
                                                hero "This is the end, isn't it?\n"
                                                voice "audio/voices/ch1/empty/narrator/empty_n_147.flac"
                                                n "I'm afraid it is.\n"
                                                if basement_1_empty_knife_hesitate:
                                                    voice "audio/voices/ch1/knife/narrator/knife_n_37.flac"
                                                    n "You shouldn't have let that fear creep into your heart. You had the upper hand, and now look at you.\n"
                                                $ persistent.death_count += 1
                                                voice "audio/voices/ch1/empty/narrator/empty_n_148.flac"
                                                stop secondary fadeout 1.0
                                                stop music fadeout 1.0
                                                stop sound fadeout 1.0
                                                hide bg onlayer back
                                                hide beast onlayer front
                                                show bg black onlayer back at Position(ypos=1125)
                                                with dissolve
                                                n "Everything goes dark, and you die.\n"
                                                hide bg black onlayer back with dissolve
                                                jump start_2

                                        "{i}• [[Fight back.]{/i}" if witch_encountered == False:
                                            $ loop_1_princess_killed = True
                                            label loop_1_knife_roll_death:
                                                $ default_mouse = "blood"
                                                $ current_princess = "witch"
                                                $ current_mutual_death += 1
                                                voice "audio/voices/ch1/empty/narrator/empty_n_149.flac"
                                                play audio "audio/one_shot/collapse.flac"
                                                $ quick_menu = False
                                                hide bg onlayer back
                                                hide battle onlayer front
                                                show bg beastrescuecontroldodgecrouch onlayer back at Position(ypos=1125)
                                                show beast armless thrown onlayer front at Position(ypos=1125)
                                                with fade
                                                if persistent.quick_menu:
                                                    $ quick_menu = True
                                                n "You roll the Princess off your back and turn to face her, rising to your knees and readying your blade.\n"
                                                play audio "audio/one_shot/blood_drip.flac"
                                                voice "audio/voices/ch1/empty/hero/empty_h_56.flac"
                                                hero "Those eyes... she's going to kill us.\n"
                                                voice "audio/voices/ch1/empty/narrator/empty_n_150.flac"
                                                # replace
                                                n "Yes. Things do look a little grim, don't they? The two of you are losing quite a lot of blood. But there's a reason she decided to strike from ambush. She isn't confident about a direct confrontation.\n"
                                                voice "audio/voices/ch1/empty/hero/empty_h_57.flac"
                                                hero "Just because she's playing it safe doesn't mean we have the upper hand.\n"
                                                voice "audio/voices/ch1/empty/narrator/empty_n_151.flac"
                                                n "Come on, now. Don't let your confidence waver. This is an important moment.\n"
                                                voice "audio/voices/ch1/empty/princess/empty_p_89.flac"
                                                show beast armless thrown talk onlayer front with dissolve
                                                sp "I'm going to kill you.\n"
                                                voice "audio/voices/ch1/empty/narrator/empty_n_152.flac"
                                                play audio "audio/one_shot/tackle.flac"
                                                hide bg onlayer back
                                                hide beast onlayer front
                                                show bg generic dark onlayer back at Position(ypos=1125)
                                                show beast rescue control ravage onlayer front at Position(ypos=1125)
                                                with dissolve
                                                n "The Princess leaps onto you as you raise your blade in defense.\n"
                                                voice "audio/voices/ch1/empty/narrator/empty_n_153.flac"
                                                play audio "audio/one_shot/rip_and_tear_knife.flac"
                                                n "You find your target, and time after time you strike, but the wounds she inflicted in her ambush hinder your movements, and with each fresh exchange you're a little slower, and a little weaker.\n"
                                                play audio "audio/one_shot/collapse.flac"
                                                voice "audio/voices/ch1/empty/narrator/empty_n_154.flac"
                                                hide bg onlayer back
                                                hide beast onlayer front
                                                show bg beastrescuecontroldodgecrouch onlayer back at Position(ypos=1125)
                                                show beast rescue betray die together onlayer front at Position(ypos=1125)
                                                with dissolve
                                                n "You seek solace in the fact that she's slowing, too. Finally, she collapses, and you collapse beside her.\n"
                                                voice "audio/voices/ch1/empty/princess/empty_p_90.flac"
                                                show beast rescue betray die together talk angry onlayer front with dissolve
                                                sp "If you think this is it... you're sorely mistaken. One way or another, I'll make sure you pay for this.\n"
                                                voice "audio/voices/ch1/empty/narrator/empty_n_155.flac"
                                                $ blade_held = False
                                                $ default_mouse = "default"
                                                show beast rescue betray die together dead onlayer front with dissolve
                                                play audio "audio/one_shot/knife_bounce_several.flac"
                                                n "Your grasp on the blade weakens. It slips from your numb fingers, lying uselessly on the floor.\n"
                                                voice "audio/voices/ch1/empty/hero/empty_h_58.flac"
                                                hero "This can't be how it ends, right?\n"
                                                # REPLACE
                                                voice "audio/voices/ch1/empty/narrator/empty_n_156.flac"
                                                n "I'm sorry, but it is. You aren't making it out of this basement. But at least you finished the job.\n"
                                                # OLD LINE
                                                #n "I'm sorry, but it is. If we're lucky, the wounds she sustained will take her before too long. But our friend isn't making it out of this basement.\n"
                                                $ persistent.death_count += 1
                                                voice "audio/voices/ch1/empty/narrator/empty_n_157.flac"
                                                stop music fadeout 1.0
                                                stop sound fadeout 1.0
                                                stop secondary fadeout 1.0
                                                hide bg onlayer back
                                                hide beast onlayer front
                                                show bg black onlayer back at Position(ypos=1125)
                                                with dissolve
                                                n "Everything goes dark, and you die.\n"
                                                hide bg black onlayer back with dissolve
                                                jump start_2

                            "{i}• ''Come on out. Let's just get this over with.''{/i}" if beast_encountered == False:
                                $ basement_1_empty_knife_hesitate = True
                                voice "audio/voices/ch1/empty/princess/empty_p_91.flac"
                                sp "I can wait. I'm very patient.\n"
                                menu:
                                    extend ""

                                    "{i}• [[Wait.]{/i}" if beast_encountered == False:
                                        jump basement_1_empty_waiting_join

                                    "{i}• [[Venture into the shadows.]{/i}":
                                        jump basement_1_empty_shadows_join

                            "{i}• ''I'll wait.''{/i}" if beast_encountered == False:
                                voice "audio/voices/ch1/empty/princess/empty_p_92.flac"
                                sp "Oh? Do you want to play a waiting game? I've been down here for a long, long time. I'm very good at waiting.\n"
                                label basement_1_empty_waiting_join:
                                    voice "audio/voices/ch1/empty/narrator/empty_n_158.flac"
                                    n "You do your best to patiently wait her out.\n"
                                    voice "audio/voices/ch1/empty/narrator/empty_n_159.flac"
                                    n "But eventually, exhaustion starts to set in.\n"
                                    voice "audio/voices/ch1/empty/hero/empty_h_59.flac"
                                    hero "Come on, wake up! We can't fall asleep down here!\n"
                                    menu:
                                        extend ""

                                        "{i}• [[Keep waiting.]{/i}":
                                            $ current_princess = "beast"
                                            voice "audio/voices/ch1/empty/narrator/empty_n_160.flac"
                                            n "You wait for as long as you can, pushing yourself to stay awake and stay vigilant, but you can't outwait someone's who's been waiting for as long as she remembers.\n"
                                            voice "audio/voices/ch1/empty/narrator/empty_n_161.flac"
                                            $ blade_held = False
                                            $ default_mouse = "default"
                                            $ quick_menu = False
                                            hide bg onlayer farback
                                            hide back onlayer back
                                            hide arm onlayer back
                                            show bg black onlayer back at Position(ypos=1125)
                                            with fade
                                            n "You barely even realize that you've started to drift off.\n"
                                            voice "audio/voices/ch1/empty/narrator/empty_n_162.flac"
                                            play audio "audio/one_shot/rip_and_tear.flac"
                                            hide bg onlayer back
                                            show bg generic dark onlayer back at Position(ypos=1125)
                                            show beast armless slept mount onlayer front at Position(ypos=1125)
                                            #show player bloody knife onlayer inyourface at Position(ypos=1125)
                                            with dissolve
                                            if persistent.quick_menu:
                                                $ quick_menu = True
                                            n "Pain tears you from your sleep. The Princess is upon you, ripping into your flesh, unnaturally sharp teeth and claws severing arteries and digging into organs.\n"
                                            voice "audio/voices/ch1/empty/narrator/empty_n_163.flac"
                                            $ quick_menu = False
                                            hide bg onlayer back
                                            hide beast onlayer front
                                            hide player onlayer inyourface
                                            show bg beastrescuecontroldodgecrouch onlayer back at Position(ypos=1125)
                                            show beast rescue control fail onlayer front at Position(ypos=1125)
                                            with fade
                                            if persistent.quick_menu:
                                                $ quick_menu = True
                                            n "There's nothing to be done. You're already half-gone.\n"
                                            voice "audio/voices/ch1/empty/hero/empty_h_60.flac"
                                            hero "It can't just end like this, right?\n"
                                            voice "audio/voices/ch1/empty/narrator/empty_n_164.flac"
                                            n "As much as I'd prefer for things to have gone differently, I can't deny the reality of what's happened. I'm sorry, but it's over.\n"
                                            $ persistent.death_count += 1
                                            voice "audio/voices/ch1/empty/narrator/empty_n_165.flac"
                                            $ quick_menu = False
                                            stop music fadeout 1.0
                                            stop sound fadeout 1.0
                                            hide bg onlayer back
                                            hide beast onlayer front
                                            show bg black onlayer back at Position(ypos=1125)
                                            with dissolve
                                            n "Everything goes dark, and you die.\n"
                                            hide bg black onlayer back with dissolve
                                            jump start_2


                                        "{i}• [[Venture into the shadows.]{/i}":
                                            label basement_1_empty_shadows_join:
                                                $ basement_1_empty_knife_hesitate = True
                                                voice "audio/voices/ch1/empty/narrator/empty_n_166.flac"
                                                play secondary "audio/one_shot/run_tackle.flac"
                                                queue secondary "audio/one_shot/rip_and_tear.flac"
                                                $ quick_menu = False
                                                hide bg onlayer farback
                                                hide back onlayer back
                                                hide arm onlayer back
                                                show bg black onlayer back at Position(ypos=1125)
                                                with dissolve
                                                n "You step into the shadows. Too late, you hear the quiet patter of feet against the basement floor, followed by the taut pull and sharp pain of tearing flesh as the Princess lunges into you from behind and drags you to the floor.\n"
                                                hide blood onlayer front
                                                hide bg onlayer back
                                                #show battle beast armless onlayer front at Position(ypos=1125)
                                                #show battle1 beast armless onlayer front at Position(ypos=1125)
                                                #show battle2 beast armless onlayer front at Position(ypos=1125)
                                                #show battle3 beast armless onlayer front at Position(ypos=1125)
                                                with Dissolve(0.75)
                                                if persistent.quick_menu:
                                                    $ quick_menu = True
                                                jump basement_1_empty_sneak_join


return
