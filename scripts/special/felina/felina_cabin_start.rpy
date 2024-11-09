label felina_cabin_start:
    # staging for shared variables in the basement
    default felina_cabin_god_comment = False
    default felina_cabin_same_comment = False

    # staging for leave ending variables

    default felina_leave_count = 0
    default felina_leave_apologize = False
    default felina_leave_which_princess = False
    default felina_leave_name = False
    default felina_leave_fair = False
    default felina_leave_intro = False
    default felina_leave_mound_thoughts = False

    # staging for loop ending variables

    default loop_reset_help = False
    default loop_forget = False
    default loop_return = False
    default loop_repeat = False
    default loop_worse = False
    default loop_worse_follow = False
    default loop_alone = False
    default loop_fair = False
    default loop_other_way = False
    default loop_regret = False


    $ gallery_zfinale.unlock_item(5)
    $ renpy.save_persistent()
    stop music
    stop secondary
    stop tertiary
    play sound "audio/looping/ambient_cabin.ogg" loop fadein 1.0
    show bodies cabin windows onlayer farback at Position(ypos=1125)
    show bg cabin int onlayer back at Position(ypos=1125)
    if final_offer == False:
        show knife interior cabin onlayer back at Position(ypos=1125)
    show door cabin1 onlayer back at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    if mirror_n_cruel_count >= 2 and felina_intermission_hero_menu_cruelty_comment == False:
        $ felina_intermission_hero_menu_cruelty_comment = True
        voice "audio/voices/felina/cabin/shared/hero/1.flac"
        hero "Don't think any of the others have forgotten what you said at the mirror. They all talked, and they're not happy.\n"
        voice "audio/voices/felina/cabin/shared/hero/2.flac"
        hero "But we can discuss that later. We have a job to do.\n"

    else:
        voice "audio/voices/felina/cabin/shared/hero/3.flac"
        hero "And here we are. I'd say we were back where it all started, but I guess it's a little after that, isn't it?\n"
    voice "audio/voices/felina/cabin/shared/hero/4a.flac"
    hero "Do you... need me to describe things?\n"

    label felina_cabin_menu_start:
        default felina_cabin_menu_count = 0
        default felina_cabin_describe = False
        default felina_cabin_blade_taken = False
        default felina_cabin_narrator_dead = False
        default felina_cabin_narrator_final_thoughts = ""
        default felina_cabin_alone = False
        default felina_cabin_leave_hand_hold = False
        menu:
            extend ""

            "{i}• (Explore) ''I'd like that. For old times' sake.''{/i}" if felina_cabin_menu_count == 0 and felina_cabin_describe == False:
                label felina_cabin_describe_join:
                    $ felina_cabin_describe = True
                    $ felina_cabin_menu_count += 1
                    voice "audio/voices/felina/cabin/shared/hero/5.flac"
                    hero "Yeah. Of course.\n"
                    voice "audio/voices/felina/cabin/shared/hero/6.flac"
                    if final_offer:
                        voice "audio/_pristine/voice/_climax/cabin_endings/general/hero/1.flac"
                        hero "The interior of the cabin is... well, it's a cabin, yeah? There isn't much here. Just a table and a door. And some windows.\n"
                        voice "audio/_pristine/voice/_climax/cabin_endings/general/hero/2.flac"
                        hero "No mirror this time... and there's no blade, is there?\n"
                        voice "audio/_pristine/voice/_climax/cabin_endings/general/hero/3.flac"
                        hero "I guess whatever we find down there, we'll have to face it empty-handed. Maybe that's for the best. Maybe we're done with violence.\n"
                        if pacifism_count == 5:
                            voice "audio/_pristine/voice/_climax/cabin_endings/general/hero/4.flac"
                            hero "I guess whatever we find down there, we'll have to face it empty-handed. Just like we always have. We never did choose violence, did we?\n"
                            if fury_pacifism:
                                voice "audio/_pristine/voice/_climax/cabin_endings/general/hero/5.flac"
                                hero "Well, except for that one time with that muscle-bound demon. But... we chose pacifism in the end there.\n"
                    else:
                        hero "The interior of the cabin is... well, it's a cabin, yeah? There isn't much here. Just a table, and a knife, and a door. And some windows.\n"
                        #voice "audio/voices/felina/cabin/shared/hero/7.flac"
                        #hero "You know, come to think of it, I don't think He ever really mentioned the windows, did he?\n"
                        voice "audio/voices/felina/cabin/shared/hero/8.flac"
                        hero "There's no mirror either. I think you broke it.\n"
                        if felina_stated_goal == "slay":
                            voice "audio/voices/felina/cabin/shared/hero/9.flac"
                            hero "And I know I've already mentioned it, but if we want to see this through, we're gonna need that blade.\n"
                        else:
                            voice "audio/voices/felina/cabin/shared/hero/10.flac"
                            hero "And I know you're still trying to find some middle ground, but if things go south, we're going to need that blade.\n"
                    jump felina_cabin_menu_start

            "{i}• (Explore) ''If the offer still stands, could you describe the cabin to me? For old times' sake?''{/i}" if felina_cabin_menu_count != 0 and felina_cabin_describe == False:
                jump felina_cabin_describe_join

            "{i}• (Explore) ''Is it just you and me? Did anyone else make it to the cabin?''{/i}" if felina_cabin_alone == False:
                $ felina_cabin_alone = True
                $ felina_cabin_menu_count += 1
                voice "audio/voices/felina/cabin/stranger/hero/13.flac"
                hero "It's just us. I think the rest of them are still out there jumbled up in the rest of her.\n"
                jump felina_cabin_menu_start

            "{i}• (Explore) ''Is the Narrator really gone?''{/i}" if felina_cabin_narrator_dead == False:
                $ felina_cabin_narrator_dead = True
                $ felina_cabin_menu_count += 1
                voice "audio/voices/felina/cabin/shared/hero/12.flac"
                hero "Yeah. It's dead silent in here. Whatever it was that was left of Him... I don't think it could handle you waking up to godhood. Pretty sure He got obliterated.\n"
                jump felina_cabin_menu_start

            "{i}• (Explore) ''Good riddance.''{/i}" if felina_cabin_narrator_dead and felina_cabin_narrator_final_thoughts == "":
                $ felina_cabin_narrator_final_thoughts = "byefelicia"
                $ felina_cabin_menu_count += 1
                if felina_stated_goal == "slay":
                    voice "audio/voices/felina/cabin/shared/hero/13.flac"
                    hero "Even after you decided to see His plans through? I guess you can like the idea and hate the man.\n"
                else:
                    voice "audio/voices/felina/cabin/shared/hero/14.flac"
                    hero "Yeah. He really put us through hell, didn't He?\n"
                jump felina_cabin_menu_start

            "{i}• (Explore) ''I don't actually know how to feel about Him being gone.''{/i}" if felina_cabin_narrator_dead and felina_cabin_narrator_final_thoughts == "":
                $ felina_cabin_narrator_final_thoughts = "unsure"
                $ felina_cabin_menu_count += 1
                label felina_cabin_complicated_feelings:
                    voice "audio/voices/felina/cabin/shared/hero/15.flac"
                    hero "Yeah, it's complicated. He put us through hell, but He's a been part of us since the very beginning, hasn't He?\n"
                    jump felina_cabin_menu_start

            "{i}• (Explore) ''It's funny. After everything He put us through, I'm kind of sad to see Him go.''{/i}" if felina_cabin_narrator_dead and felina_cabin_narrator_final_thoughts == "":
                $ felina_cabin_narrator_final_thoughts = "sad"
                $ felina_cabin_menu_count += 1
                if felina_stated_goal == "slay":
                    voice "audio/voices/felina/cabin/shared/hero/16.flac"
                    hero "Is that why you want to see this through and slay her?\n"
                else:
                    jump felina_cabin_complicated_feelings
                jump felina_cabin_menu_start

            "{i}• (Explore) [[Take the blade.]{/i}" if blade_held == False and final_offer == False:
                $ blade_held = True
                $ default_mouse = "blade"
                play audio "audio/one_shot/knife_pickup.flac"
                hide knife onlayer back with dissolve
                voice "audio/voices/felina/cabin/shared/hero/17.flac"
                hero "That's probably for the best. It's always seemed to give us more options than not.\n"
                jump felina_cabin_menu_start

            "{i}• [[Enter the basement.]{/i}":
                if blade_held == False and final_offer == False:
                    if felina_stated_goal == "slay" and final_offer == False:
                        voice "audio/voices/felina/cabin/shared/hero/18.flac"
                        hero "No blade it is. Have you given up on slaying her?\n"
                    else:
                        voice "audio/voices/felina/cabin/shared/hero/19.flac"
                        hero "No blade it is. I'm not sure what we'll be able to do without it, but your judgment has gotten us this far.\n"

                $ quick_menu = False
                play audio "audio/one_shot/door_bedroom.flac"
                show door cabin2 onlayer back at Position(ypos=1125)
                with Dissolve(0.5)
                show door cabin3 onlayer back at Position(ypos=1125) with Dissolve(0.5)
                hide farback onlayer farback
                hide bodies onlayer farback
                hide bg onlayer back
                hide door onlayer back
                hide table onlayer back
                hide knife onlayer back
                hide mirror onlayer back
                with fade
                play sound "audio/looping/ambient_basement_interior.ogg" loop
                scene bg basement stairs onlayer farback at Position(ypos=1125)
                show front basement stairs onlayer farback at Position(ypos=1125)
                with fade
                # transition to stairs
                if persistent.quick_menu:
                    $ quick_menu = True
                voice "audio/voices/felina/cabin/shared/hero/20.flac"
                hero "The stairs. Do you remember the first time we were here? The first time we heard her voice?\n"
                if first_princess == "harsh":
                    if felina_stated_goal == "slay":
                        voice "audio/voices/felina/cabin/shared/princess/1.flac"
                        p "We both know why you're here. You don't have to draw it out for my sake.\n"
                    else:
                        voice "audio/voices/felina/cabin/shared/princess/2.flac"
                        p "Have you figured out what you want to do yet, or are you going to keep trying to find a center that doesn't exist?\n"
                    voice "audio/voices/felina/cabin/shared/hero/21.flac"
                    hero "It sounded just like that. A little sharp, a little menacing. Only she didn't know us.\n"
                else:
                    if felina_stated_goal == "slay":
                        voice "audio/voices/felina/cabin/shared/princess/3a.flac"
                        p "It's almost over, isn't it? That's okay. Let's just talk, the two of us, one more time before you kill me.\n"
                    else:
                        voice "audio/voices/felina/cabin/shared/princess/4.flac"
                        p "I don't know what you want for us.\n"
                    voice "audio/voices/felina/cabin/shared/hero/22.flac"
                    hero "She sounded just like that. Timid and gentle. Only she didn't know us.\n"

                menu:
                    extend ""

                    "{i}• [[Continue down the stairs.]{/i}":
                        voice "audio/voices/felina/cabin/shared/hero/23.flac"
                        hero "And down we go. We shouldn't keep her waiting.\n"
                        $ quick_menu = False
                        play audio "audio/one_shot/footsteps_creaky.flac"
                        hide bg basement stairs onlayer farback at Position(ypos=1125)
                        hide front basement stairs onlayer farback at Position(ypos=1125)
                        with fade
                        scene bodies basement onlayer farback at Position(ypos=1125)
                        show bg basement end no chain onlayer back at Position(ypos=1125)
                        show princess dn confident onlayer back at Position(ypos=1125)
                        with fade
                        if persistent.quick_menu:
                            $ quick_menu = True
                        if first_princess == "harsh":
                            jump felina_cabin_hostile_start
                        else:
                            jump felina_cabin_gentle_start


return
