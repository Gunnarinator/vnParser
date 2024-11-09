label mirror_1_join:
    $ gallery_ztlq.unlock_gallery()
    $ gallery_ztlq.unlock_item(3)
    $ renpy.save_persistent()
    $ achievement.grant("ACH_MIRROR1")
    show content m you onlayer front
    with Dissolve(2.5)
    truth "It's you.\n"
    jump begin_quiet

label mirror_2_join:
    $ gallery_ztlq.unlock_item(4)
    $ renpy.save_persistent()
    $ achievement.grant("ACH_MIRROR2")
    show content m bloat onlayer front
    with Dissolve(2.5)
    truth "You've grown.\n"
    jump begin_quiet

label mirror_3_join:
    $ gallery_ztlq.unlock_item(5)
    $ renpy.save_persistent()
    $ achievement.grant("ACH_MIRROR3")
    show content m wither onlayer front
    with Dissolve(2.5)
    truth "You've withered.\n"
    jump begin_quiet

label mirror_4_join:
    $ gallery_ztlq.unlock_item(6)
    $ renpy.save_persistent()
    $ achievement.grant("ACH_MIRROR4")
    show content m bone onlayer front
    with Dissolve(2.5)
    truth "You've unraveled.\n"
    jump begin_quiet

label mirror_finale:

    $ gallery_ztlq.unlock_item(7)
    $ renpy.save_persistent()
    $ blade_held = False
    $ default_mouse = "eye"
    show content m quiet onlayer front
    with Dissolve(2.5)
    truth "You are nothing at all.\n"
    hide player onlayer front
    hide content onlayer front
    show mirror m narrator onlayer front
    with Dissolve(2.5)
    truth "But that isn't right. You can't be nothing. You refocus your gaze, and then you see it: a figure, faint and veiled in shadow, just beyond the reflection.\n"

    menu:

        extend ""

        "{i}• (Explore) ''Are you me?''{/i}":
            voice "audio/voices/mirror/finale/1.flac"
            mirror "I think you know what I am.\n"
            play audio "audio/final/Assorted_MirrorBreaksLongShortBigSmall_12.flac"
            show mirror m narrator crack onlayer front
            truth "A crack slides down the center of the mirror, splitting the image in the glass in two.\n"
            play audio "audio/final/Assorted_MirrorBreaksLongShortBigSmall_2.flac"
            $ renpy.pause(0.54)
            hide content onlayer front
            hide mirror onlayer front
            scene bg black big onlayer inyourface at Position(ypos=1125)
            truth "And then another crack forms, and another, and another, turning the mirror into jagged shards of broken glass.\n"
            $ gallery_ztlq.unlock_item(8)
            $ renpy.save_persistent()
            hide bg onlayer inyourface
            show narrator special onlayer front at Position(ypos=1125)
            with fade

label mirror_final_menu:

    if mirror_countdown != 12:
        show narrator onlayer front at screenshake

    #if mirror_countdown == 13:
    #    play audio "audio/final/Assorted_MirrorBreaksLongShortBigSmall_8.flac"
    #    $ renpy.pause(0.3)

    #if mirror_countdown == 12:
    #    play audio "audio/final/Assorted_MirrorBreaksLongShortBigSmall_5.flac"
    #    $ renpy.pause(0.3)

    if mirror_countdown == 11:
        play audio "audio/final/Assorted_MirrorBreaksLongShortBigSmall_3.flac"
        $ renpy.pause(0.3)

    if mirror_countdown == 10:
        play audio "audio/final/Assorted_MirrorBreaksLongShortBigSmall_1.flac"
        $ renpy.pause(0.3)

    if mirror_countdown == 9:
        play audio "audio/final/Assorted_MirrorBreaksLongShortBigSmall_3.flac"
        $ renpy.pause(0.3)

    if mirror_countdown == 8:
        play audio "audio/final/Assorted_MirrorBreaksLongShortBigSmall_5.flac"
        $ renpy.pause(0.3)

    if mirror_countdown == 7:
        play audio "audio/final/Assorted_MirrorBreaksLongShortBigSmall_4.flac"
        $ renpy.pause(0.5)

    if mirror_countdown == 6:
        play audio "audio/final/Assorted_MirrorBreaksLongShortBigSmall_6.flac"
        $ renpy.pause(0.3)

    if mirror_countdown == 5:
        play audio "audio/final/Assorted_MirrorBreaksLongShortBigSmall_9.flac"
        $ renpy.pause(0.3)

    if mirror_countdown == 4:
        play audio "audio/final/Assorted_MirrorBreaksLongShortBigSmall_12.flac"
        $ renpy.pause(0.3)

    if mirror_countdown == 3:
        play audio "audio/final/Assorted_MirrorBreaksLongShortBigSmall_6.flac"
        $ renpy.pause(0.3)

    if mirror_countdown == 2:
        play audio "audio/final/Assorted_MirrorBreaksLongShortBigSmall_1.flac"
        $ renpy.pause(0.3)

    $ mirror_countdown -= 1
    hide narrator onlayer front
    show narrator special onlayer front at Position(ypos=1125)

    if mirror_countdown != 11:
        show narrator special onlayer front with hpunch

    if mirror_countdown == 3:
        if mirror_quest == False:
            $ mirror_quest = True
            $ mirror_creation = True
            voice "audio/voices/mirror/finale/2.flac"
            show narrator special onlayer front
            mirror "Soon I'll be gone entirely and you'll be left alone with your final choice. So allow me to make my final request. The Princess contains death itself within her, but I wove you into being with all the power you need to destroy her. Forever. Do it. Slay her, and rid the world of death and suffering.\n"
            jump mirror_final_menu

    if mirror_countdown == 1:
        jump mirror_shard


    default mirror_angy_meter = 0
    default mirror_angy = False
    default mirror_smashed = False

    default mirror_countdown = 12
    default mirror_reveal_count = 0
    default mirror_narrator = False
    default mirror_echo_mention = False
    default mirror_multi_narrator = False
    default mirror_many_questions = False
    default mirror_hurt_ask = False
    default mirror_narrator_apologize = False
    default mirror_break_observation = False
    default mirror_narrator_answers = False
    default mirror_part_of_me = False
    default mirror_death_reveal = False
    default mirror_death_followup = False
    default mirror_why_hide = False
    default mirror_instrusive_thought = False
    default mirror_see_this = False
    default mirror_quest_lead = False
    default mirror_how_narrator_die = False
    default mirror_why_princess = False
    default mirror_why_princess_2 = False
    default mirror_how_destroy_concept = False
    default mirror_stall_ask = False
    default mirror_stall_ask_difference = False
    default mirror_slay_worse = False
    default mirror_post_princess = False
    default mirror_construct = False
    default mirror_construct_follow_up = False
    default mirror_beyond_walls = False
    default mirror_refuse_god = False
    default mirror_accept_god = False
    default mirror_fates_worse_than_death = False
    default mirror_why_kill_flag = False
    default mirror_alone = False
    default mirror_why_no_death = False
    default mirror_death_good = False
    default mirror_died_lots = False
    default mirror_shaped = False
    default mirror_deserve = False
    default mirror_repent = False
    default mirror_torture = False
    default mirror_deluded = False
    default mirror_narrator_gaslight = False
    default mirror_died_question = False
    default mirror_died_final = False

    default mirror_narrator_god = False

    default mirror_versions = False
    default mirror_creation = False
    default mirror_mound_reveal = False

    default mirror_long_quiet_reveal = False
    default mirror_princess_share = False
    default mirror_perception_reveal = False

    default mirror_quest = False
    default mirror_happy_challenge = False

    menu:
        extend ""

        "{i}• (Explore) ''In one of my lives, you doubted yourself. You thought that all of this was wrong.''{/i}" if (mirror_long_quiet_reveal or mirror_princess_share or mirror_quest or mirror_creation) and mirror_happy_challenge == False and (happy_end == "dance" or happy_end == "free" or happy_end == "slay"):
            $ mirror_happy_challenge = True
            $ mirror_construct = True
            $ mirror_angy_meter += 2
            if mirror_angy == False and mirror_angy_meter >= 3:
                $ mirror_angy = True
            if mirror_angy == False:
                voice "audio/_pristine/voice/happy/narrator/mirror1a.flac"
            else:
                voice "audio/_pristine/voice/happy/narrator/mirror2.flac"
            show narrator special onlayer front
            mirror "Oh, did I? That means nothing in the grand scheme of things. This construct you're in contains every possible world at once. The fact that you managed to find one reality among trillions where I was delusional proves nothing.\n"
            jump mirror_final_menu

        "{i}• (Explore) ''If you made us, then I want you to know that this has been torture.''{/i}" if mirror_long_quiet_reveal and mirror_mound_reveal and mirror_torture == False:
            $ mirror_torture = True
            $ mirror_angy_meter += 1
            if mirror_angy == False and mirror_angy_meter >= 3:
                $ mirror_angy = True
            if mirror_angy == False:
                voice "audio/voices/mirror/finale/3.flac"
            else:
                voice "audio/voices/mirror/finale/3a.flac"
            show narrator special onlayer front
            mirror "The inevitability of death is torture. I would gladly put two infinite beings through what you've been through to spare infinite lives from oblivion.\n"
            jump mirror_final_menu

        "{i}• (Explore) ''If I destroy Her, won't I be alone?''{/i}" if mirror_mound_reveal and mirror_quest and mirror_alone == False:
            $ mirror_alone = True
            if mirror_angy == False:
                voice "audio/voices/mirror/finale/4.flac"
            else:
                voice "audio/voices/mirror/finale/4a.flac"
            show narrator special onlayer front
            mirror "Yes, you will. But it will all be worth it.\n"
            jump mirror_final_menu

        "{i}• (Explore) ''Why would you want me to destroy the concept of transformation?''{/i}" if mirror_mound_reveal and mirror_long_quiet_reveal == False and mirror_death_reveal == False:
            $ mirror_why_kill_flag = True
            jump mirror_contains_death_join

        "{i}• (Explore) ''If I destroy Her, how is that existence any better than death? Or even different from death at all? Honestly, it feels worse.''{/i}" if mirror_death_reveal and mirror_mound_reveal and mirror_fates_worse_than_death == False and mirror_why_kill_flag:
            label mirror_cycle_destroy_join:
                $ mirror_fates_worse_than_death = True
                if mirror_angy == False:
                    voice "audio/voices/mirror/finale/5.flac"
                else:
                    voice "audio/voices/mirror/finale/5a.flac"
                show narrator special onlayer front
                mirror "When I broke the cycle, I made sure that the tear was rough. You carry a part of what should be her, and she carries a part of what should be you. Things won't be as they are now, but they won't be nothing, either.\n"
                if mirror_slay_worse == False:
                    $ mirror_slay_worse = True
                    if mirror_angy == False:
                        voice "audio/voices/mirror/finale/6.flac"
                    else:
                        voice "audio/voices/mirror/finale/6a.flac"
                    show narrator special onlayer front
                    mirror "Besides... anything is better than oblivion. In the end, nobody wants to leave.\n"

                jump mirror_final_menu

        "{i}• (Explore) ''If you want me to destroy the concept of transformation, how is that existence any better than death? Or even different from death at all? Honestly, it feels worse.''{/i}" if mirror_death_reveal and mirror_mound_reveal and mirror_fates_worse_than_death == False and mirror_why_kill_flag == False:
            jump mirror_cycle_destroy_join

        "{i}• (Explore) ''You're delusional.''{/i}" if mirror_fates_worse_than_death and mirror_deluded == False:
            $ mirror_deluded = True
            $ mirror_angy_meter += 1
            if mirror_angy == False and mirror_angy_meter >= 3:
                $ mirror_angy = True
            if mirror_angy == False:
                voice "audio/voices/mirror/finale/7.flac"
            else:
                voice "audio/voices/mirror/finale/7a.flac"
            show narrator special onlayer front
            mirror "I'm only delusional if I'm wrong. And I'm not wrong. I can't be wrong.\n"

            jump mirror_final_menu

        "{i}• (Explore) ''Do you have anything to say for yourself? For all of this hubris?''{/i}" if (mirror_construct_follow_up or mirror_mound_reveal or mirror_torture or mirror_deluded) and mirror_repent == False:
            $ mirror_repent = True
            $ mirror_angy_meter += 1
            if mirror_angy == False and mirror_angy_meter >= 3:
                $ mirror_angy = True
            if mirror_angy == False:
                voice "audio/voices/mirror/finale/8.flac"
            else:
                voice "audio/voices/mirror/finale/8a.flac"
            show narrator special onlayer front
            mirror "I do. The people out there are real. No matter what you do to them, no matter what you enable, I want you to remember that.\n"

            jump mirror_final_menu

        "{i}• (Explore) ''After everything you've done to us, do you think anyone deserves to live?''{/i}" if (mirror_construct_follow_up or mirror_mound_reveal or mirror_torture or mirror_deluded) and mirror_deserve == False:
            $ mirror_deserve = True
            $ mirror_angy_meter += 1
            if mirror_angy == False and mirror_angy_meter >= 3:
                $ mirror_angy = True
            if mirror_angy == False:
                voice "audio/voices/mirror/finale/9.flac"
            else:
                voice "audio/voices/mirror/finale/9a.flac"
            show narrator special onlayer front
            mirror "Nobody alive has done anything to you. I'm all gone. But if you and the Princess want to smite the rest of them for the crimes of a dead man—if you really want to be that petty—there isn't much I can do to stop you.\n"

            jump mirror_final_menu

        "{i}• (Explore) ''Do you know that things won't just be worse if I destroy Her?''{/i}" if mirror_mound_reveal and mirror_slay_worse == False:
            $ mirror_slay_worse = True
            if mirror_angy == False:
                voice "audio/voices/mirror/finale/10.flac"
            else:
                voice "audio/voices/mirror/finale/10a.flac"
            show narrator special onlayer front
            mirror "Of course they won't be worse. I saw a glimpse of a better world, and I did what I could to make it real. Anything is better than oblivion. In the end, nobody wants to leave.\n"

            jump mirror_final_menu

        "{i}• (Explore) ''What would it be like to live in a world without Her?''{/i}" if mirror_mound_reveal and mirror_post_princess == False:
            $ mirror_post_princess = True
            if mirror_angy == False:
                voice "audio/voices/mirror/finale/11.flac"
            else:
                voice "audio/voices/mirror/finale/11a.flac"
            show narrator special onlayer front
            mirror "Light. Burdenless. An eternal pattern of forgetfulness leading into the joys of rediscovery. Everyone will be with the ones they love. No more fear, no more howling chaos. Just life. Forever.\n"
            if mirror_angy == False:
                voice "audio/voices/mirror/finale/12.flac"
            else:
                voice "audio/voices/mirror/finale/12a.flac"
            show narrator special onlayer front
            mirror "There's a cruel irony to it all. The only way I could share my dream with the world was to never be able to see it for myself.\n"

            jump mirror_final_menu

        "{i}• (Explore) ''Does anyone else know about this? Does anyone else know about {b}us{/b}?''{/i}" if mirror_mound_reveal and mirror_long_quiet_reveal and mirror_beyond_walls == False:
            $ mirror_beyond_walls = True
            $ mirror_construct = True
            if mirror_angy == False:
                voice "audio/voices/mirror/finale/13.flac"
            else:
                voice "audio/voices/mirror/finale/13a.flac"
            show narrator special onlayer front
            mirror "Of course not. The only way this construct could function was if nobody knew what it was doing. But the bones of the universe are old. It's on the cusp of its dying breath, and the people out there are consumed with thoughts of oblivion.\n"
            if mirror_angy == False:
                voice "audio/voices/mirror/finale/14.flac"
            else:
                voice "audio/voices/mirror/finale/14a.flac"
            show narrator special onlayer front
            mirror "When the patterns are wiped from the sand, when the board is reset, who will remember them? All I've done is give them a chance to live outside of the shadow of the end.\n"

            jump mirror_final_menu

        "{i}• (Explore) ''I don't want to be a god. I want to be me.''{/i}" if mirror_long_quiet_reveal and mirror_refuse_god == False and mirror_god_comment == False:
            default mirror_god_comment = False
            $ mirror_god_comment = True
            $ mirror_refuse_god = True
            if mirror_angy == False:
                voice "audio/voices/mirror/finale/15.flac"
            else:
                voice "audio/voices/mirror/finale/15a.flac"
            show narrator special onlayer front
            mirror "You are you, and if you had let everything work the way it was supposed to, you never would have woken up to the reality of your true nature. There's no accounting for free will.\n"

            jump mirror_final_menu

        "{i}• (Explore) ''A god. I always knew I was special.''{/i}" if mirror_long_quiet_reveal and mirror_accept_god == False and mirror_god_comment == False:
            $ mirror_god_comment = True
            $ mirror_accept_god = True
            if mirror_angy == False:
                voice "audio/voices/mirror/finale/16.flac"
            else:
                voice "audio/voices/mirror/finale/16a.flac"
            show narrator special onlayer front
            mirror "Yes. You are special. Unique, even. And you still have a task that you need to do. And only you can do it.\n"

            jump mirror_final_menu

        "{i}• (Explore) ''I was made to do this single task? Who made me? What am I?''{/i}" if mirror_echo_mention == False and mirror_quest and mirror_long_quiet_reveal == False:
            jump long_quiet_reveal_join

        "{i}• (Explore) ''So you're the Narrator. I was wondering if I'd ever get to see you.''{/i}" if mirror_narrator == False:
            $ mirror_narrator = True

            if mirror_angy == False:
                voice "audio/voices/mirror/finale/17.flac"
            else:
                voice "audio/voices/mirror/finale/17a.flac"
            show narrator special onlayer front
            mirror "'The Narrator.' Yes, I suppose that's my job, isn't it? You needed help after all. An objective voice to guide your blade. But you were never supposed to see me. I wonder how many worlds you damned to extinction to fall this far.\n"
            jump mirror_final_menu

        "{i}• (Explore) ''What are you? Are you something like me?''{/i}" if mirror_echo_mention == False and mirror_narrator_god == False:
            if mirror_angy == False:
                voice "audio/voices/mirror/finale/18.flac"
            else:
                voice "audio/voices/mirror/finale/18a.flac"
            show narrator special onlayer front
            mirror "Oh, I'm nothing like you.\n"
            jump mirror_echo_join

        "{i}• (Explore) ''If you're not me, then what are you?''{/i}" if mirror_echo_mention == False and mirror_narrator_god == False:
            label mirror_echo_join:
                $ mirror_echo_mention = True
                $ mirror_creation = True
                if mirror_angy == False:
                    voice "audio/voices/mirror/finale/19.flac"
                else:
                    voice "audio/voices/mirror/finale/19a.flac"
                show narrator special onlayer front
                mirror "I'm an echo, likely one of many. Somebody made you, after all, and I'm what's left of him. Not that I'm the only one who can make that claim. I'm sure you've met many others like me.\n" id mirror_echo_join_b0d02301
                jump mirror_final_menu

        "{i}• (Explore) '''Others like you.' You've said something like that before. Has every Narrator really been different?''{/i}" if mirror_multi_narrator == False and mirror_echo_mention:
            if mirror_angy == False:
                voice "audio/voices/mirror/finale/20.flac"
            else:
                voice "audio/voices/mirror/finale/20a.flac"
            show narrator special onlayer front
            mirror "Of course. And that is by both necessity and design.\n"
            jump mirror_multi_narrator_join

        "{i}• (Explore) ''I have so many questions for you!''{/i}" if mirror_many_questions == False:
            $ mirror_many_questions = True

            $ mirror_angy_meter += 1
            if mirror_angy == False and mirror_angy_meter >= 3:
                $ mirror_angy = True
            if mirror_angy == False:
                voice "audio/voices/mirror/finale/21.flac"
            else:
                voice "audio/voices/mirror/finale/21a.flac"
            show narrator special onlayer front
            mirror "Then ask them, and make it quick. I won't last for long now that you can see me.\n"
            jump mirror_final_menu

        "{i}• (Explore) ''Does it hurt when pieces of you break off like that?''{/i}" if mirror_hurt_ask == False and mirror_countdown <= 12:
            $ mirror_hurt_ask = True

            if mirror_angy == False:
                voice "audio/voices/mirror/finale/22.flac"
            else:
                voice "audio/voices/mirror/finale/22a.flac"
            show narrator special onlayer front
            mirror "It doesn't hurt. I don't feel pain. Not physically.\n"
            jump mirror_final_menu

        "{i}• (Explore) ''I'm sorry. I don't want to destroy you. Will it help if I look away or stop asking questions?''{/i}" if mirror_narrator_apologize == False and (mirror_countdown <= 12 and mirror_countdown >2):
            $ mirror_narrator_apologize = True

            if mirror_angy == False:
                voice "audio/voices/mirror/finale/23.flac"
            else:
                voice "audio/voices/mirror/finale/23a.flac"
            show narrator special onlayer front
            mirror "We've already crossed the point of no return. There's no saving me now. Not that there's ever been much of me to save.\n"
            jump mirror_final_menu

        "{i}• (Explore) ''Every time I ask you something, it's like a piece of you breaks.''{/i}" if mirror_break_observation == False:
            $ mirror_break_observation = True

            if mirror_angy == False:
                voice "audio/voices/mirror/finale/24.flac"
            else:
                voice "audio/voices/mirror/finale/24a.flac"
            show narrator special onlayer front
            mirror "I'm aware. And if I were you, I'd be more precious about your time.\n"
            jump mirror_final_menu

        "{i}• (Explore) ''Whenever I've tried getting answers out of you before, you've been absolutely impenetrable. Why are you suddenly being so open?''{/i}" if mirror_reveal_count >= 2 and mirror_narrator_answers == False and mirror_narrator:
            $ mirror_narrator_answers = True

            if mirror_perception_reveal:
                $ mirror_versions = True
                if mirror_angy == False:
                    voice "audio/voices/mirror/finale/25.flac"
                else:
                    voice "audio/voices/mirror/finale/25a.flac"
                show narrator special onlayer front
                mirror "Because we're at the end of the road, and circumstances have changed. If one of those other versions of me had told you what she actually was, it would have made your task impossible to finish.\n"
                if mirror_angy == False:
                    voice "audio/voices/mirror/finale/26.flac"
                else:
                    voice "audio/voices/mirror/finale/26a.flac"
                mirror "Not that you managed to finish it.\n" id mirror_echo_join_2664fd81
            else:
                $ mirror_perception_reveal = True
                $ mirror_instrusive_thought = True
                if mirror_angy == False:
                    voice "audio/voices/mirror/finale/27.flac"
                else:
                    voice "audio/voices/mirror/finale/27a.flac"
                show narrator special onlayer front
                mirror "Her nature is to become what others perceive her to be. If you actually knew what she was, if you knew her capabilities, a single intrusive thought could have instantly ended the entire world.\n"
            jump mirror_final_menu

        "{i}• (Explore) ''Are you a part of me? Or are you something else?''{/i}" if mirror_part_of_me == False:
            $ mirror_part_of_me = True
            $ mirror_versions = True
            if mirror_angy == False:
                voice "audio/voices/mirror/finale/28.flac"
            else:
                voice "audio/voices/mirror/finale/28a.flac"
            show narrator special onlayer front
            mirror "No, I'm not 'a part of you,' but that's all a matter of perspective, isn't it?\n" id mirror_echo_join_57845f8c
            if mirror_angy == False:
                voice "audio/voices/mirror/finale/29.flac"
            else:
                voice "audio/voices/mirror/finale/29a.flac"
            show narrator special onlayer front
            mirror "From one vantage point I must seem wholly foreign, but from another, well... all the versions of me that have existed have collectively heard your every thought and driven your every action. If that isn't being part of you, then what is?\n"

            jump mirror_final_menu

        "{i}• (Explore) '''Versions of you.' You've said that before. So I really was meeting different you's.''{/i}" if mirror_multi_narrator == False and mirror_versions:
            if mirror_angy == False:
                voice "audio/voices/mirror/finale/30.flac"
            else:
                voice "audio/voices/mirror/finale/30a.flac"
            show narrator special onlayer front
            mirror "You were, and it was by both necessity and design.\n"
            jump mirror_multi_narrator_join

        "{i}• (Explore) ''You're the one who wanted me to slay the Princess. Why?''{/i}" if mirror_narrator == False and mirror_death_reveal == False:
            label mirror_contains_death_join:
                $ mirror_death_reveal = True
                if mirror_angy == False:
                    voice "audio/voices/mirror/finale/31.flac"
                else:
                    voice "audio/voices/mirror/finale/31a.flac"
                show narrator special onlayer front
                mirror "Because among other things, she is death itself. To rid the world of suffering, to save untold trillions from being lost forever to the cosmic wind, she must be destroyed.\n"
                if mirror_quest == False:
                    $ mirror_quest = True
                    if mirror_angy == False:
                        voice "audio/voices/mirror/finale/32.flac"
                    else:
                        voice "audio/voices/mirror/finale/32a.flac"
                    show narrator special onlayer front
                    mirror "And despite how far you've fallen, you will still have a chance to fulfill your purpose once I'm gone.\n"

                jump mirror_final_menu

        "{i}• (Explore) ''You said She contains death. What is She?''{/i}" if mirror_death_reveal and mirror_death_followup == False and mirror_mound_reveal == False:
            $ mirror_reveal_count += 1
            $ mirror_death_followup = True
            $ mirror_mound_reveal = True
            if mirror_angy == False:
                voice "audio/voices/mirror/finale/33.flac"
            else:
                voice "audio/voices/mirror/finale/33a.flac"
            show narrator special onlayer front
            mirror "She is The Shifting Mound, the Ebb and Flow, the Capacity to Change. She is Transformation, or most of it. Her nature is why I had to die, for she becomes that which others perceive her to be. But an echo can't perceive things. Not in the way that people can.\n"
            if mirror_quest == False:
                $ mirror_quest = True
                if mirror_angy == False:
                    voice "audio/voices/mirror/finale/34.flac"
                else:
                    voice "audio/voices/mirror/finale/34a.flac"
                show narrator special onlayer front
                mirror "This isn't the end just yet. You can still destroy her and save everyone. You were made to do this single task, and you will still have a chance to fulfill your purpose once I'm gone.\n"

            jump mirror_final_menu

        "{i}• (Explore) ''Why couldn't you have told me all of this from the start? I would have helped you destroy Her.''{/i}" if mirror_mound_reveal and mirror_why_hide == False:
            $ mirror_reveal_count += 1
            $ mirror_why_hide = True
            if mirror_angy == False:
                voice "audio/voices/mirror/finale/35.flac"
            else:
                voice "audio/voices/mirror/finale/35a.flac"
            show narrator special onlayer front
            mirror "If you actually knew what she was from the start, if you knew her capabilities, a single intrusive thought could have instantly ended the entire world.\n"

            jump mirror_final_menu

        "{i}• (Explore) '''I don't work the way a living being does? Not anymore?!' Am I not a living being?''{/i}" if mirror_instrusive_thought and mirror_long_quiet_reveal == False:
            $ mirror_reveal_count += 1
            $ mirror_long_quiet_reveal = True
            $ mirror_creation = True
            $ mirror_construct = True
            if mirror_angy == False:
                voice "audio/voices/mirror/finale/36.flac"
            else:
                voice "audio/voices/mirror/finale/36a.flac"
            show narrator special onlayer front
            mirror "You never were. You are the Long Quiet, the god I made to rid the world of death. For a time, this construct could help you approximate being alive — confining your mind to a single reality. But you've experienced far too many lives for it to work much longer.\n"

            jump mirror_final_menu

        "{i}• (Explore) ''What do you mean a single intrusive thought could have instantly ended the world?''{/i}" if mirror_instrusive_thought == False and mirror_why_hide:
            $ mirror_reveal_count += 1
            $ mirror_instrusive_thought = True
            #if mirror_angy == False:
            #    voice "audio/voices/mirror/finale/37.flac"
            #else:
            #    voice "audio/voices/mirror/finale/30a.flac"
            voice "audio/voices/mirror/finale/37c.flac"
            show narrator special onlayer front
            mirror "It's simple, really: 'She can become whatever people perceive her to be? That's easy! I'll just will her into something really small! But wait, what if I accidentally will her into something that ends the world. Oh no, what if just thinking that—'\n" id mirror_contains_death_join_90457fbb
            if mirror_angy == False:
                voice "audio/voices/mirror/finale/38.flac"
            else:
                voice "audio/voices/mirror/finale/38a.flac"
            show narrator special onlayer front
            mirror "But you wouldn't have finished your hypothetical thought, because she would have already destroyed the world.\n"
            if mirror_angy == False:
                voice "audio/voices/mirror/finale/39.flac"
            else:
                voice "audio/voices/mirror/finale/39a.flac"
            show narrator special onlayer front
            mirror "Luckily for you, as you are now, you won't be able to will her into anything. You don't work the way a living being does. Not anymore.\n"

            jump mirror_final_menu

        "{i}• (Explore) ''Doesn't telling me this now mean that an intrusive thought could still end the world?''{/i}" if mirror_why_hide and mirror_instrusive_thought == False:
            $ mirror_instrusive_thought = True
            if mirror_angy == False:
                voice "audio/voices/mirror/finale/40.flac"
            else:
                voice "audio/voices/mirror/finale/40a.flac"
            show narrator special onlayer front
            mirror "It doesn't. As you are now, you won't be able to will her into anything. You don't work the way a living being does. Not anymore.\n"

            jump mirror_final_menu

        "{i}• (Explore) ''If She's capable of becoming whatever people believe Her to be, can't I just... will Her into something small?''{/i}" if mirror_mound_reveal and mirror_instrusive_thought == False:
            $ mirror_reveal_count += 1
            $ mirror_instrusive_thought = True
            if mirror_angy == False:
                voice "audio/voices/mirror/finale/41.flac"
            else:
                voice "audio/voices/mirror/finale/41a.flac"
            show narrator special onlayer front
            mirror "As you are now, you won't be able to will her into anything. You don't work the way a living being does. Not anymore.\n"
            if mirror_angy == False:
                voice "audio/voices/mirror/finale/42.flac"
            else:
                voice "audio/voices/mirror/finale/42a.flac"
            show narrator special onlayer front
            mirror "And as you were before? You couldn't be trusted with the knowledge of what she is. No one could be trusted with that knowledge. Intrusive thoughts have a way of creeping in and ruining everything. It's why I had to die.\n"

            jump mirror_final_menu

        "{i}• (Explore) ''I've met you many times. Have you been the same you all along?''{/i}" if mirror_multi_narrator == False:
            $ mirror_reveal_count += 1
            if mirror_angy == False:
                voice "audio/voices/mirror/finale/43.flac"
            else:
                voice "audio/voices/mirror/finale/43a.flac"
            show narrator special onlayer front
            mirror "I haven't, and that's by both necessity and design.\n"
            label mirror_multi_narrator_join:
                $ mirror_multi_narrator = True

                $ mirror_construct = True
                $ mirror_construct_follow_up = True
                voice "audio/voices/mirror/finale/44.flac"
                show narrator special onlayer front
                mirror "This construct you're in exists in many places at once. Any time you failed, any time you thought yourself dead, it would restart and shunt both your consciousness and hers into another world.\n"
                if mirror_angy == False:
                    voice "audio/voices/mirror/finale/45.flac"
                else:
                    voice "audio/voices/mirror/finale/45a.flac"
                show narrator special onlayer front
                mirror "But you'll be awake soon. And then it won't be able to work like that anymore.\n"
                jump mirror_final_menu

        "{i}• (Explore) ''So you do know about the looping. So many of the times I met you, you denied it as even being a possibility. Why did you lie to me?''{/i}" if mirror_construct_follow_up and mirror_narrator_gaslight == False:
            $ mirror_narrator_gaslight = True
            $ mirror_reveal_count += 1
            if mirror_versions == False:
                $ mirror_versions = True
                if mirror_angy == False:
                    voice "audio/voices/mirror/finale/46.flac"
                else:
                    voice "audio/voices/mirror/finale/46a.flac"
                show narrator special onlayer front
                mirror "Any other version of me you talked to was just that — a version of me. It wasn't {i}me{/i}. As to why they lied...\n"
            if mirror_angy == False:
                voice "audio/voices/mirror/finale/47.flac"
            else:
                voice "audio/voices/mirror/finale/47a.flac"
            show narrator special onlayer front
            mirror "Perhaps they thought that admitting to it would have pushed you to certain realizations that would have made finishing your task impossible. Maybe they were just in denial.\n"
            if mirror_angy == False:
                voice "audio/voices/mirror/finale/48.flac"
                show narrator special onlayer front
                mirror "I'm sure many of them were convinced that they {i}had{/i} to be the first version of them you'd encountered. Anything else would have been too existentially unpleasant.\n"
            else:
                voice "audio/voices/mirror/finale/48a.flac"
                show narrator special onlayer front
                mirror "I'm sure many of them were convinced that they {i}had{/i} to be the first version of them that you'd encountered. Anything else would have been too existentially unpleasant.\n"
            if mirror_angy == False:
                voice "audio/voices/mirror/finale/bonus.flac"
            else:
                voice "audio/voices/mirror/finale/bonus_angy.flac"
            show narrator special onlayer front
            mirror "And for all I know, each of those other versions of me could have had entirely different understandings of how this construct works. Who's to say which of them are right and which of them are wrong, really?\n"
            if mirror_angy == False:
                voice "audio/voices/mirror/finale/bonus2.flac"
            else:
                voice "audio/voices/mirror/finale/bonus2_angy.flac"
            show narrator special onlayer front
            mirror "Except for me. I can tell you for a fact that I'm right.\n"
            jump mirror_final_menu

        "{i}• (Explore) ''If you made me, then what am I?''{/i}" if mirror_long_quiet_reveal == False and mirror_echo_mention:
            label long_quiet_reveal_join:
                $ mirror_long_quiet_reveal = True
                $ mirror_creation = True
                if mirror_angy == False:
                    voice "audio/voices/mirror/finale/49.flac"
                else:
                    voice "audio/voices/mirror/finale/49a.flac"
                show narrator special onlayer front
                mirror "You're the Long Quiet, the god I made to rid the world of death.\n"

            jump mirror_final_menu

        "{i}• (Explore) ''Are you a god? Or... were you a god?''{/i}" if mirror_long_quiet_reveal and mirror_narrator_god == False:
            $ mirror_narrator_god = True
            $ mirror_reveal_count += 1
            if mirror_angy == False:
                voice "audio/voices/mirror/finale/50.flac"
            else:
                voice "audio/voices/mirror/finale/50a.flac"
            show narrator special onlayer front
            mirror "No. In life, I was painfully mortal. A witness to the end of days. I held the fear of death in my heart, and saw oblivion threaten the very memory of everything I knew and everyone I loved. I needed to do something.\n"
            if mirror_angy == False:
                voice "audio/voices/mirror/finale/51.flac"
            else:
                voice "audio/voices/mirror/finale/51a.flac"
            show narrator special onlayer front
            mirror "So I made you. And I made her. And I made this place to hold you both.\n"

            jump mirror_final_menu

        "{i}• (Explore) ''I wasn't supposed to see all this, was I?''{/i}" if mirror_see_this == False:
            $ mirror_see_this = True
            $ mirror_quest_lead = True
            if mirror_angy == False:
                voice "audio/voices/mirror/finale/52.flac"
            else:
                voice "audio/voices/mirror/finale/52a.flac"
            show narrator special onlayer front
            mirror "You were either going to have seen all of this, or you weren't going to have seen all of this. This is worse, but you still have an opportunity to save the world. You can still slay her.\n"

            jump mirror_final_menu

        "{i}• (Explore) ''If you want me to slay Her, I need to know what She actually is.''{/i}" if mirror_quest_lead and mirror_mound_reveal == False:
            jump mirror_princess_identity_join

        "{i}• (Explore) ''How did you die?''{/i}" if mirror_how_narrator_die == False and mirror_mound_reveal:
            $ mirror_how_narrator_die = True
            voice "audio/voices/mirror/finale/53.flac"
            show narrator special onlayer front
            mirror "I killed myself. It had to be done, really. None of this would have worked if I were still alive. Nobody living could know about her.\n"

            jump mirror_final_menu

        "{i}• (Explore) ''What is the Princess? Did you make Her too?''{/i}" if mirror_mound_reveal == False and mirror_creation:
            label mirror_princess_identity_join:
                $ mirror_reveal_count += 1
                $ mirror_mound_reveal = True
                $ mirror_construct = True
                if mirror_angy == False:
                    voice "audio/voices/mirror/finale/33.flac"
                else:
                    voice "audio/voices/mirror/finale/33a.flac"
                show narrator special onlayer front
                mirror "She is The Shifting Mound, the Ebb and Flow, the Capacity to Change. She is Transformation, or most of it. Her nature is why I had to die, for she becomes that which others perceive her to be. But an echo can't perceive things. Not in the way that people can.\n"
                if mirror_angy == False:
                    voice "audio/voices/mirror/finale/54.flac"
                else:
                    voice "audio/voices/mirror/finale/54a.flac"
                show narrator special onlayer front
                mirror "So I tucked a part of myself into the folds of this Construct to guide you.\n"
                if mirror_quest == False:
                    $ mirror_quest = True
                    if mirror_quest_lead:
                        if mirror_angy == False:
                            voice "audio/voices/mirror/finale/55.flac"
                        else:
                            voice "audio/voices/mirror/finale/55a.flac"
                        show narrator special onlayer front
                        mirror "Like I said, this isn't the end just yet. You can still destroy her and save everyone. You were made to do this single task, and you will still have a chance to fulfill your purpose once I'm gone.\n"
                    else:
                        if mirror_angy == False:
                            voice "audio/voices/mirror/finale/34.flac"
                        else:
                            voice "audio/voices/mirror/finale/34a.flac"
                        show narrator special onlayer front
                        mirror "This isn't the end just yet. You can still destroy her and save everyone. You were made to do this single task, and you will still have a chance to fulfill your purpose once I'm gone.\n"
                else:
                    if mirror_angy == False:
                        voice "audio/voices/mirror/finale/56.flac"
                    else:
                        voice "audio/voices/mirror/finale/56a.flac"
                    show narrator special onlayer front
                    mirror "Seems that every 'me' you met did a real shit job of it, though.\n"

                jump mirror_final_menu

        "{i}• (Explore) ''Why did you make Her a Princess?''{/i}" if mirror_why_princess == False and mirror_mound_reveal:
            $ mirror_why_princess = True
            if mirror_angy == False:
                voice "audio/voices/mirror/finale/57.flac"
            else:
                voice "audio/voices/mirror/finale/57a.flac"
            show narrator special onlayer front
            mirror "I didn't make her a Princess, but I wove the idea of her into something your scattered mind could fathom. You chose for that something to be a princess.\n"

            jump mirror_final_menu

        "{i}• (Explore) ''I chose to make Her a princess? Why couldn't I have made things easier on myself and picked something small or weak like an ant or a slice of bread?''{/i}" if mirror_why_princess and mirror_why_princess_2 == False and mirror_mound_reveal:
            $ mirror_why_princess_2 = True
            if mirror_angy == False:
                voice "audio/voices/mirror/finale/58.flac"
            else:
                voice "audio/voices/mirror/finale/58a.flac"
            show narrator special onlayer front
            mirror "Are you asking me to spend my final moments psychoanalyzing you? {i}Sigh{/i}. Whatever you viewed her as needed to map on some level to what she was. You couldn't just pick something arbitrary and beneath you.\n"
            if mirror_angy == False:
                voice "audio/voices/mirror/finale/59.flac"
            else:
                voice "audio/voices/mirror/finale/59a.flac"
            show narrator special onlayer front
            mirror "I don't know why you settled on a princess, specifically, but clearly a princess is what you wanted.\n"
            jump mirror_psychoanalyze_join

        "{i}• (Explore) ''Of all things, why is She a Princess? Why couldn't She be an ant or a slice of soggy bread?''{/i}" if mirror_why_princess == False and mirror_mound_reveal:
            $ mirror_why_princess = True
            $ mirror_why_princess_2 = True
            if mirror_angy == False:
                voice "audio/voices/mirror/finale/60.flac"
            else:
                voice "audio/voices/mirror/finale/60a.flac"
            show narrator special onlayer front
            mirror "Are you asking me to spend my final moments psychoanalyzing you? {i}Sigh{/i}. She wound up a princess because you wanted her to be a princess. As to why?\n"
            label mirror_psychoanalyze_join:
                if mirror_angy == False:
                    voice "audio/voices/mirror/finale/61.flac"
                else:
                    voice "audio/voices/mirror/finale/61a.flac"
                show narrator special onlayer front
                mirror "Maybe she needed to be beautiful. Important. Above you, but on a level you could still approach. A herald of things to come.\n"
                if mirror_angy == False:
                    voice "audio/voices/mirror/finale/62.flac"
                else:
                    voice "audio/voices/mirror/finale/62a.flac"
                show narrator special onlayer front
                mirror "I don't know. Gods are supposed to be beyond comprehension. I really shouldn't try and anthropomorphize you like this.\n"

            jump mirror_final_menu

        "{i}• (Explore) ''How am I supposed to destroy an abstract concept?''{/i}" if mirror_mound_reveal and mirror_how_destroy_concept == False:
            $ mirror_how_destroy_concept = True
            $ mirror_construct = True
            if mirror_angy == False:
                voice "audio/voices/mirror/finale/63.flac"
            else:
                voice "audio/voices/mirror/finale/63a.flac"
            show narrator special onlayer front
            mirror "With some amount of difficulty. But you're an abstract concept yourself. It would have been preferable if you had destroyed her within the confines of the construct, but when I shaped the two of you, I made sure that you were strong enough to see things through.\n"

            jump mirror_final_menu

        "{i}• (Explore) ''What if neither of us leave this place? Does that work? Can we just stay here together and leave the people out there alone?''{/i}" if mirror_mound_reveal and mirror_stall_ask == False:
            $ mirror_stall_ask = True
            $ mirror_angy_meter += 1
            if mirror_angy == False and mirror_angy_meter >= 3:
                $ mirror_angy = True
            if mirror_angy == False:
                voice "audio/voices/mirror/finale/64.flac"
            else:
                voice "audio/voices/mirror/finale/64a.flac"
            show narrator special onlayer front
            mirror "It wouldn't work. Her nature as The Shifting Mound makes it so nothing can last forever as it is now. It wouldn't matter how long the two of you waited. Eventually she would find a way to leave. And then everything would change. Everything would face oblivion.\n"
            if mirror_angy == False:
                voice "audio/voices/mirror/finale/65.flac"
            else:
                voice "audio/voices/mirror/finale/65a.flac"
            show narrator special onlayer front
            mirror "And until then, the clock ticks on.\n"

            jump mirror_final_menu

        "{i}• (Explore) ''Is there a difference between leaving this place and staying here?''{/i}" if mirror_stall_ask and mirror_stall_ask_difference == False:
            $ mirror_stall_ask_difference = True
            if mirror_angy == False:
                voice "audio/voices/mirror/finale/66.flac"
            else:
                voice "audio/voices/mirror/finale/66a.flac"
            show narrator special onlayer front
            mirror "There is. It's the difference between being stranded on a desert island and being stranded on a desert island with a leopard that can't die.\n"
            if mirror_angy == False:
                voice "audio/voices/mirror/finale/67.flac"
            else:
                voice "audio/voices/mirror/finale/67a.flac"
            show narrator special onlayer front
            mirror "Neither option is great, especially when there's a third option where you get rid of the island and give everyone a chance to finally be happy.\n"

            jump mirror_final_menu

        "{i}• (Explore) ''The people out there beyond the walls of the construct... Do {b}they{/b} know about this? Do they know what you want me to do to them?''{/i}" if mirror_construct and mirror_beyond_walls == False:
            $ mirror_reveal_count += 1
            $ mirror_beyond_walls = True
            if mirror_angy == False:
                voice "audio/voices/mirror/finale/13.flac"
            else:
                voice "audio/voices/mirror/finale/13a.flac"
            show narrator special onlayer front
            mirror "Of course not. The only way this construct could function was if nobody knew what it was doing. But the bones of the universe are old. It's on the cusp of its dying breath, and the people out there are consumed with thoughts of oblivion.\n"
            if mirror_angy == False:
                voice "audio/voices/mirror/finale/14.flac"
            else:
                voice "audio/voices/mirror/finale/14a.flac"
            show narrator special onlayer front
            mirror "When the patterns are wiped from the sand, when the board is reset, who will remember them? All I've done is give them a chance to live outside of the shadow of the end.\n"

            jump mirror_final_menu

        "{i}• (Explore) ''What is this place? Where are we?''{/i}" if mirror_construct == False and mirror_construct_follow_up == False:
            $ mirror_construct = True
            voice "audio/voices/mirror/finale/construct.flac"
            mirror "A construct.\n"
            jump mirror_construct_join

        "{i}• (Explore) ''And what is my 'true identity?'''{/i}" if mirror_construct_follow_up and mirror_long_quiet_reveal == False:
            jump long_quiet_reveal_join

        "{i}• (Explore) ''You've called this place a construct. What is it supposed to do?''{/i}" if mirror_construct and mirror_construct_follow_up == False:
            label mirror_construct_join:
                $ mirror_reveal_count += 1
                $ mirror_construct = True
                $ mirror_construct_follow_up = True
                if mirror_angy == False:
                    voice "audio/voices/mirror/finale/68.flac"
                else:
                    voice "audio/voices/mirror/finale/68a.flac"
                show narrator special onlayer front
                mirror "It was supposed to keep the two of you trapped here until the job was done. And it was supposed to guide your hand to help you see things through.\n"
                if mirror_angy == False:
                    voice "audio/voices/mirror/finale/69.flac"
                else:
                    voice "audio/voices/mirror/finale/69a.flac"
                show narrator special onlayer front
                mirror "The construct you're in exists in every world at once. Any time you failed, any time you thought yourself dead, it would restart and shunt both you and her into a new world.\n"
                if mirror_angy == False:
                    voice "audio/voices/mirror/finale/70.flac"
                else:
                    voice "audio/voices/mirror/finale/70a.flac"
                mirror "But you're waking up to your true nature now. It won't be able to work like that anymore.\n"

                jump mirror_final_menu

        "{i}• (Explore) ''Why would you want to rid the world of death?''{/i}" if (mirror_death_reveal or mirror_long_quiet_reveal) and mirror_why_no_death == False:
            $ mirror_why_no_death = True
            if mirror_angy == False:
                voice "audio/voices/mirror/finale/71.flac"
            else:
                voice "audio/voices/mirror/finale/71a.flac"
            show narrator special onlayer front
            mirror "If you need to ask that question, there's nothing I can say to move you. You haven't died. You cannot die. So you cannot grasp the abject horror of dying.\n"

            jump mirror_final_menu

        "{i}• (Explore) ''I'm pretty sure death is good, actually. Important, even.''{/i}" if mirror_why_no_death == False and mirror_death_good == False and (mirror_death_reveal or mirror_long_quiet_reveal):
            $ mirror_why_no_death = True
            $ mirror_death_good = True
            $ mirror_angy_meter += 1
            if mirror_angy == False and mirror_angy_meter >= 3:
                $ mirror_angy = True
            if mirror_angy == False:
                voice "audio/voices/mirror/finale/72.flac"
            else:
                voice "audio/voices/mirror/finale/72a.flac"
            show narrator special onlayer front
            mirror "If that's your belief, there's nothing I can say to move you. You haven't died. You cannot die. So you can't grasp the abject horror of dying.\n" id mirror_construct_join_684100b9

            jump mirror_final_menu

        "{i}• (Explore) ''But I've died plenty of times.''{/i}" if mirror_died_lots == False and mirror_death_good:
            jump mirror_fake_die_join

        "{i}• (Explore) ''Who cares about dying? I've died plenty of times.''{/i}" if mirror_died_lots == False and (mirror_death_reveal or mirror_long_quiet_reveal):
            label mirror_fake_die_join:
                $ mirror_died_lots = True
                $ mirror_angy_meter += 1
                if mirror_angy == False and mirror_angy_meter >= 3:
                    $ mirror_angy = True
                if mirror_angy == False:
                    voice "audio/voices/mirror/finale/73.flac"
                else:
                    voice "audio/voices/mirror/finale/73a.flac"
                show narrator special onlayer front
                mirror "You haven't. You've flirted with dying. You've played pretend, but your consciousness is an unbroken stream.\n"

                jump mirror_final_menu

        "{i}• (Explore) ''And how do you know everybody else doesn't also experience death the way I do?''{/i}" if mirror_died_lots and mirror_died_question == False:
            $ mirror_died_question = True
            if mirror_angy == False:
                voice "audio/voices/mirror/finale/74.flac"
            else:
                voice "audio/voices/mirror/finale/74a.flac"
            show narrator special onlayer front
            mirror "They obviously don't. You experience 'death' the way you do by design and by your unique nature.\n"

            jump mirror_final_menu

        "{i}• (Explore) ''I think you're wrong. I don't think dying is bad at all, and you're just making all this up as you go.''{/i}" if mirror_died_final == False and mirror_died_question:
            $ mirror_died_final = True
            $ mirror_angy_meter += 1
            if mirror_angy == False and mirror_angy_meter >= 3:
                $ mirror_angy = True
            if mirror_angy == False:
                voice "audio/voices/mirror/finale/75.flac"
            else:
                voice "audio/voices/mirror/finale/75a.flac"
            show narrator special onlayer front
            mirror "If you really want to waste valuable time telling me that I'm wrong when we both know I'm not, then that's your prerogative.\n"

            jump mirror_final_menu

        "{i}• (Explore) ''How am I supposed to rid the world of death?''{/i}" if mirror_quest == False and mirror_long_quiet_reveal:
            $ mirror_quest = True
            if mirror_angy == False:
                voice "audio/voices/mirror/finale/76.flac"
            else:
                voice "audio/voices/mirror/finale/76a.flac"
            show narrator special onlayer front
            mirror "By slaying the Princess. Once she's gone, everyone will get to exist exactly as they are. No more fear, no more howling chaos. Just life. Forever.\n"

            jump mirror_final_menu

        "{i}• (Explore) ''You made us? Out of what?''{/i}" if mirror_narrator_god and mirror_shaped == False:
            jump mirror_shaped_join


        "{i}• (Explore) ''What were we shaped from?''{/i}" if mirror_how_destroy_concept and mirror_shaped == False:
            label mirror_shaped_join:
                $ mirror_shaped = True
                if mirror_angy == False:
                    voice "audio/voices/mirror/finale/77.flac"
                else:
                    voice "audio/voices/mirror/finale/77a.flac"
                show narrator special onlayer front
                mirror "The cycle of life and death. The endless pattern of creation and destruction. I tore it in two and shaped the fraying threads into you and her.\n"

                jump mirror_final_menu

        "{i}• [[Destroy the Mirror.]{/i}":
            $ mirror_smashed = True
            play audio "audio/final/Assorted_MirrorBreaksLongShortBigSmall_2.flac"
            show narrator onlayer front at screenshake
            $ renpy.pause(0.3)
            hide narrator onlayer front with hpunch
            if mirror_countdown >= 11:
                $ achievement.grant("ACH_MIRROR_BREAK")
                truth "You don't need answers from the thing that lives in the mirror.\n"
            else:
                truth "You have heard enough.\n"
            if mirror_long_quiet_reveal:
                truth "The Narrator was right. You are The Long Quiet, a vast and nascent god. And it is finally time for you to wake up. All of this is you.\n"
            else:
                truth "You already know what you are. You are The Long Quiet, a vast and nascent god. And it is finally time for you to wake up. All of this is you.\n"
            $ achievement.grant("ACH_MIRROR5")
            $ quick_menu = False
            hide narrator onlayer front
            hide farback onlayer farback
            scene bg black
            with fade
            scene farback quiet onlayer farback at Position(ypos=1125)
            show bg quiet path onlayer back at Position(ypos=1125)
            show mid quiet path onlayer front at Position(ypos=1125)
            show fore quiet path onlayer inyourface at Position(ypos=1125)
            with fade
            if persistent.quick_menu:
                $ quick_menu = True
            menu:
                extend ""

                "{i}• [[Proceed to the cabin, one last time.]{/i}":
                    jump felina_start_join

label mirror_shard:
    $ achievement.grant("ACH_MIRRORQUEST")
    menu:
        extend ""

        "{i}• ''I think you're out of time.''{/i}":
            if mirror_echo_mention:
                if mirror_angy == False:
                    voice "audio/voices/mirror/finale/78.flac"
                else:
                    voice "audio/voices/mirror/finale/78a.flac"
                show narrator special onlayer front
                mirror "So I am. It's like I said, I'm just an echo. And echoes always fade away. You know what you have to do.\n"
            else:
                if mirror_angy == False:
                    voice "audio/voices/mirror/finale/79.flac"
                else:
                    voice "audio/voices/mirror/finale/79a.flac"
                show narrator special onlayer front
                mirror "So I am, and so it was always going to be. I'm just an echo. And every echo fades away. You know what you have to do.\n"

        "{i}• ''I'm not going to slay Her, and I want you to know that before you die for good.''{/i}":
            if mirror_angy == False:
                voice "audio/voices/mirror/finale/80.flac"
            else:
                voice "audio/voices/mirror/finale/80a.flac"
            show narrator special onlayer front
            mirror "Well. There's no reasoning with a god. Even one you've woven into existence yourself. I've said my piece and my time is up.\n"
            if mirror_echo_mention:
                if mirror_angy == False:
                    voice "audio/voices/mirror/finale/81.flac"
                else:
                    voice "audio/voices/mirror/finale/81a.flac"
                show narrator special onlayer front
                mirror "It's like I said, I'm just an echo. And echoes always fade away.\n"
            else:
                if mirror_angy == False:
                    voice "audio/voices/mirror/finale/82.flac"
                else:
                    voice "audio/voices/mirror/finale/82a.flac"
                show narrator special onlayer front
                mirror "I'm just an echo. And every echo fades away.\n"

        "{i}• ''Rest easy. I'm going to destroy Her.''{/i}":
            label mirror_destroy_join:
                if mirror_angy == False:
                    voice "audio/voices/mirror/finale/83.flac"
                else:
                    voice "audio/voices/mirror/finale/83a.flac"
                show narrator special onlayer front
                mirror "Are you lying? I can't tell. But I've said my piece, and my time is up.\n"
                label mirror_echo_final_join:
                    if mirror_echo_mention:
                        if mirror_angy == False:
                            voice "audio/voices/mirror/finale/84.flac"
                        else:
                            voice "audio/voices/mirror/finale/84a.flac"
                        show narrator special onlayer front
                        mirror "It's like I said, I'm just an echo. And echoes always fade away. You know what you have to do.\n"
                    else:
                        voice "audio/voices/mirror/finale/85.flac"
                        show narrator special onlayer front
                        mirror "I'm just an echo. And every echo fades away. You know what you have to do.\n"

        "{i}• (Lie) ''Rest easy. I'm going to destroy Her.''{/i}":
            jump mirror_destroy_join

        "{i}• 'I haven't decided what I'm going to do yet. I still have to see what She thinks about all of this.'{/i}":
            jump mirror_default_end

        "{i}• [[Say nothing, and watch him end.]{/i}":
            label mirror_default_end:
                voice "audio/voices/mirror/finale/86.flac"
                show narrator special onlayer front
                mirror "I've said my piece, and my time is up.\n"
                jump mirror_echo_final_join

    show narrator die onlayer front
    $ renpy.pause(1.5)
    play audio "audio/final/Assorted_MirrorBreaksLongShortBigSmall_10.flac"
    $ quick_menu = False
    hide narrator onlayer front
    hide farback onlayer farback
    scene bg black
    with fade
    scene farback quiet onlayer farback at Position(ypos=1125)
    show bg quiet path onlayer back at Position(ypos=1125)
    show mid quiet path onlayer front at Position(ypos=1125)
    show fore quiet path onlayer inyourface at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    truth "As the final fragment of glass shatters, you see yourself with newfound clarity.\n"
    $ achievement.grant("ACH_MIRROR5")
    if mirror_long_quiet_reveal:
        truth "The Narrator was right. You are The Long Quiet, a vast and nascent god. And it is finally time for you to wake up. All of this is you.\n"
    else:
        $ mirror_long_quiet_reveal = True
        truth "You are The Long Quiet, a vast and nascent god. And it is finally time for you to wake up. All of this is you.\n"
    menu:
        extend ""

        "{i}• [[Proceed to the cabin, one last time.]{/i}":
            label felina_start_join:
                # defines the final princess given to the mound
                if current_princess == "adversary":
                    $ fifth_mound = "adversary"
                elif current_princess == "needle":
                    $ fifth_mound = "needle"
                elif current_princess == "beast":
                    $ fifth_mound = "beast"
                elif current_princess == "den":
                    $ fifth_mound = "den"
                elif current_princess == "damsel":
                    $ fifth_mound = "damsel"
                elif current_princess == "dereal":
                    $ fifth_mound = "dereal"
                elif current_princess == "nightmare":
                    $ fifth_mound = "nightmare"
                elif current_princess == "clarity":
                    $ fifth_mound = "clarity"
                elif current_princess == "prisonerhead":
                    $ fifth_mound = "prisonerhead"
                elif current_princess == "prisonerchain":
                    $ fifth_mound = "prisonerchain"
                elif current_princess == "razorheart":
                    $ fifth_mound = "razorheart"
                elif current_princess == "razor":
                    $ fifth_mound = "razor"
                elif current_princess == "spectre":
                    $ fifth_mound = "spectre"
                elif current_princess == "stranger":
                    $ fifth_mound = "stranger"
                elif current_princess == "tower":
                    $ fifth_mound = "tower"
                elif current_princess == "apotheosis":
                    $ fifth_mound = "apotheosis"
                elif current_princess == "witch":
                    $ fifth_mound = "witch"
                elif current_princess == "thorn":
                    $ fifth_mound = "thorn"
                elif current_princess == "fury":
                    $ fifth_mound = "fury"
                elif current_princess == "greydamsel":
                    $ fifth_mound = "greydamsel"
                elif current_princess == "greyprisoner":
                    $ fifth_mound = "greyprisoner"
                elif current_princess == "wildnerves":
                    $ fifth_mound = "wildnerves"
                elif current_princess == "wildwound":
                    $ fifth_mound = "wildwound"
                elif current_princess == "wraith":
                    $ fifth_mound = "wraith"
                elif current_princess == "happy":
                    $ fifth_mound = "happy"
                elif current_princess == "happydry":
                    $ fifth_mound = "happydry"
                elif current_princess == "furyheart":
                    $ fifth_mound = "furyheart"
                elif current_princess == "dragon":
                    $ fifth_mound = "dragon"
                elif current_princess == "dragonfused":
                    $ fifth_mound = "dragonfused"
                elif current_princess == "dragonhand":
                    $ fifth_mound = "dragonhand"
                elif current_princess == "cage":
                    $ fifth_mound = "cage"

                if current_princess == "adversary":
                    $ achievement.grant("ACH_ADVERSARY")
                    $ gallery_adversary.unlock_item(18)
                    $ gallery_adversary.unlock_item(19)
                    $ renpy.save_persistent()
                elif current_princess == "needle":
                    $ achievement.grant("ACH_NEEDLE")
                    $ gallery_needle.unlock_item(18)
                    $ gallery_needle.unlock_item(19)
                    $ renpy.save_persistent()
                elif current_princess == "beast":
                    $ achievement.grant("ACH_BEAST")
                    $ gallery_beast.unlock_item(15)
                    $ gallery_beast.unlock_item(16)
                    $ renpy.save_persistent()
                elif current_princess == "den":
                    $ achievement.grant("ACH_DEN")
                    $ gallery_den.unlock_item(18)
                    $ gallery_den.unlock_item(19)
                    $ renpy.save_persistent()
                elif current_princess == "damsel":
                    $ achievement.grant("ACH_DAMSEL")
                    $ gallery_damsel.unlock_item(17)
                    $ gallery_damsel.unlock_item(18)
                    $ renpy.save_persistent()
                elif current_princess == "dereal":
                    $ achievement.grant("ACH_DAMSEL_DEREAL")
                    $ gallery_damsel.unlock_item(17)
                    $ gallery_damsel.unlock_item(19)
                    $ renpy.save_persistent()
                elif current_princess == "nightmare":
                    $ achievement.grant("ACH_NIGHTMARE")
                    $ gallery_nightmare.unlock_item(17)
                    $ gallery_nightmare.unlock_item(18)
                    $ renpy.save_persistent()
                elif current_princess == "clarity":
                    $ achievement.grant("ACH_CLARITY")
                    $ gallery_clarity.unlock_item(12)
                    $ gallery_clarity.unlock_item(13)
                    $ renpy.save_persistent()
                elif current_princess == "prisonerhead":
                    $ gallery_prisoner.unlock_item(15)
                    $ gallery_prisoner.unlock_item(16)
                    $ renpy.save_persistent()
                    $ achievement.grant("ACH_PRISONER_HEAD")
                elif current_princess == "prisonerchain":
                    $ gallery_prisoner.unlock_item(13)
                    $ gallery_prisoner.unlock_item(14)
                    $ renpy.save_persistent()
                    $ achievement.grant("ACH_PRISONER_FULL")
                elif current_princess == "razorheart":
                    $ achievement.grant("ACH_RAZORHEART")
                    $ gallery_razor.unlock_item(18)
                    $ gallery_razor.unlock_item(19)
                    $ renpy.save_persistent()
                elif current_princess == "razor":
                    $ gallery_razor.unlock_item(16)
                    $ gallery_razor.unlock_item(17)
                    $ renpy.save_persistent()
                    $ achievement.grant("ACH_RAZOR")
                elif current_princess == "spectre":
                    $ achievement.grant("ACH_SPECTRE")
                    $ gallery_spectre.unlock_item(16)
                    $ gallery_spectre.unlock_item(17)
                    $ renpy.save_persistent()
                elif current_princess == "stranger":
                    $ achievement.grant("ACH_STRANGER")
                    $ gallery_stranger.unlock_item(10)
                    $ gallery_stranger.unlock_item(11)
                    $ renpy.save_persistent()
                elif current_princess == "tower":
                    $ achievement.grant("ACH_TOWER")
                    $ gallery_tower.unlock_item(11)
                    $ gallery_tower.unlock_item(12)
                    $ renpy.save_persistent()
                elif current_princess == "apotheosis":
                    $ achievement.grant("ACH_APOTHEOSIS")
                    $ gallery_apotheosis.unlock_item(18)
                    $ gallery_apotheosis.unlock_item(19)
                    $ renpy.save_persistent()
                elif current_princess == "witch":
                    $ achievement.grant("ACH_WITCH")
                    $ gallery_witch.unlock_item(17)
                    $ gallery_witch.unlock_item(18)
                    $ renpy.save_persistent()
                elif current_princess == "thorn":
                    $ achievement.grant("ACH_THORN")
                    $ gallery_thorn.unlock_item(17)
                    $ gallery_thorn.unlock_item(18)
                    $ renpy.save_persistent()
                elif current_princess == "fury":
                    $ achievement.grant("ACH_FURY")
                    $ gallery_fury.unlock_item(18)
                    $ renpy.save_persistent()
                elif current_princess == "greydamsel":
                    $ achievement.grant("ACH_GREY_DAMSEL")
                    $ gallery_grey.unlock_item(15)
                    $ gallery_grey.unlock_item(16)
                    $ renpy.save_persistent()
                elif current_princess == "greyprisoner":
                    $ achievement.grant("ACH_GREY_PRISONER")
                    $ gallery_grey.unlock_item(17)
                    $ gallery_grey.unlock_item(18)
                    $ renpy.save_persistent()
                elif current_princess == "wildnerves":
                    $ achievement.grant("ACH_WILD_NERVES")
                    $ gallery_wild.unlock_item(7)
                    $ gallery_wild.unlock_item(8)
                    $ renpy.save_persistent()
                elif current_princess == "wildwound":
                    $ achievement.grant("ACH_WILD_WOUND")
                    $ gallery_wild.unlock_item(9)
                    $ gallery_wild.unlock_item(10)
                    $ renpy.save_persistent()
                elif current_princess == "wraith":
                    $ achievement.grant("ACH_WRAITH")
                    $ gallery_wraith.unlock_item(9)
                    $ gallery_wraith.unlock_item(10)
                    $ renpy.save_persistent()
                elif current_princess == "happy":
                    $ achievement.grant("ACH_HAPPY")
                    $ gallery_happy.unlock_item(17)
                    $ gallery_happy.unlock_item(18)
                    $ renpy.save_persistent()
                elif current_princess == "happydry":
                    $ achievement.grant("ACH_HAPPY")
                    $ gallery_happy.unlock_item(17)
                    $ gallery_happy.unlock_item(18)
                    $ renpy.save_persistent()
                elif current_princess == "dragon" or current_princess == "dragonhand":
                    $ achievement.grant("ACH_DRAGON")
                    $ gallery_dragon.unlock_item(17)
                    $ gallery_dragon.unlock_item(18)
                    $ renpy.save_persistent()
                elif current_princess == "dragonfused":
                    $ achievement.grant("ACH_DRAGON_FUSE_HEART")
                    $ gallery_dragon.unlock_item(17)
                    $ gallery_dragon.unlock_item(19)
                    $ renpy.save_persistent()
                elif current_princess == "cage":
                    $ achievement.grant("ACH_CAGE")
                    $ gallery_cage.unlock_item(18)
                    $ gallery_cage.unlock_item(19)
                    $ renpy.save_persistent()
                elif current_princess == "furyheart":
                    $ achievement.grant("ACH_FURY_HEART")
                    $ gallery_fury.unlock_item(19)
                    $ renpy.save_persistent()

                if trait_stubborn:
                    $ stubborn_met = True
                    $ trait_stubborn = False

                if trait_hunted:
                    $ hunted_met = True
                    $ trait_hunted = False

                if trait_smitten:
                    $ smitten_met = True
                    $ trait_smitten = False

                if trait_paranoid:
                    $ paranoid_met = True
                    $ trait_paranoid = False

                if trait_skeptic:
                    $ skeptic_met = True
                    $ trait_skeptic = False

                if trait_cheated:
                    $ cheated_met = True
                    $ trait_cheated = False

                if trait_cold:
                    $ cold_met = True
                    $ trait_cold = False

                if trait_contrarian:
                    $ contrarian_met = True
                    $ trait_contrarian = False

                if trait_broken:
                    $ broken_met = True
                    $ trait_broken = False

                if trait_opportunist:
                    $ opportunist_met = True
                    $ trait_opportunist = False

                play audio "audio/one_shot/footsteps_hike_short.flac"
                $ quick_menu = False
                hide farback onlayer farback
                hide bg onlayer back
                hide mid onlayer front
                hide fore onlayer inyourface
                scene bg black
                with fade
                scene farback quiet onlayer farback at Position(ypos=1125)
                show back trees cabin quiet onlayer back at Position(ypos=1125)
                show bg cabin quiet onlayer front at Position(ypos=1125)
                show mid cabin quiet onlayer inyourface at Position(ypos=1125)
                show fore cabin quiet onlayer inyourface at Position(ypos=1125)
                with fade
                if persistent.quick_menu:
                    $ quick_menu = True
                jump felina_start
