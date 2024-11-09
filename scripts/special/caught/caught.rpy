label caught_start:
    default oblivion_when_met = -1
    hide loading_icon
    stop sound fadeout 20.0
    stop music fadeout 20.0
    play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 20.0
    default oblivion_flag = False
    $ oblivion_flag = True
    default caught_origin_current = ""
    default caught_origin_ch3 = False
    show quiet creep1 onlayer inyourface at Position(ypos=1125) with Dissolve(2.0)
    if caught_origin_current == "stranger" or caught_origin_ch3:
        $ caught_origin_ch3 = False
        voice "audio/voices/caught/n1.flac"
        n "Wait... something isn't right. Can you still hear me? Everything is getting fuzzy...\n"
    else:
        voice "audio/voices/caught/n2.flac"
        n "Wait... something isn't right. Can you still hear me? You're supposed to wind up back at the cabin again, but everything is getting fuzzy...\n"

    play music "audio/_music/mound/Oblivion.flac" loop fadein 15.0
    show quiet creep2 onlayer inyourface at Position(ypos=1125) with Dissolve(2.0)
    voice "audio/voices/caught/hero.flac"
    hero "W-what's going on. Where are we?\n"
    show quiet creep3 onlayer inyourface at Position(ypos=1125) with Dissolve(2.0)
    if trait_contrarian:
        voice "audio/voices/caught/contrarian.flac"
        contrarian "We're somewhere interesting for once.\n"

    if trait_cold:
        voice "audio/voices/caught/cold.flac"
        cold "I don't know. But it feels like home.\n"

    if trait_broken:
        voice "audio/voices/caught/broken.flac"
        broken "We're dead. Obviously.\n"

    if trait_hunted:
        voice "audio/voices/caught/hunted.flac"
        hunted "A dark place. Thoughts like us shouldn't be here.\n"

    if trait_skeptic:
        voice "audio/voices/caught/skeptic.flac"
        skeptic "Did we do this? Is this the end of the world? Was there ever even a world to end?\n"

    if trait_stubborn:
        voice "audio/voices/caught/stubborn.flac"
        stubborn "I told you we shouldn't have come here, I told you. But did you listen? No.\n"

    if trait_smitten:
        voice "audio/voices/caught/smitten.flac"
        smitten "Oh I don't like this one bit. There's not a single damsel in sight. How dull.\n"

    if trait_flinching:
        voice "audio/voices/caught/cheated.flac"
        cheated "At least He's gone...\n"

    if trait_paranoid:
        voice "audio/voices/caught/paranoid.flac"
        paranoid "It's finally happened, hasn't it? We've finally cracked.\n"

    if trait_opportunist:
        voice "audio/voices/caught/opportunist.flac"
        opportunist "I like it! Seems like it's got some great acoustics...\n"

    if trait_cheated:
        voice "audio/voices/caught/cheated2.flac"
        cheated "That son-of-a-bitch flipped over the table, didn't he?\n"

    hide mid onlayer back
    hide bg onlayer front
    hide farback onlayer farback
    hide bg onlayer back
    hide fore onlayer front
    hide fore onlayer inyourface
    hide stars onlayer farback
    hide back onlayer back
    hide mid onlayer front
    hide mid onlayer back
    hide midground onlayer back
    hide front onlayer front
    hide bg onlayer farback
    hide front onlayer inyourface
    hide quiet onlayer inyourface
    show farback quiet onlayer back at Position(ypos=1125)
    with Dissolve(4.0)
    jump caught_late_join

label caught_late_join:
    hide loading_icon
    $ oblivion_flag = True

    if loops_finished != 0:
        truthmid "The world around you is unwound, its physical matter replaced by a textured nothing. You find yourself in The Long Quiet once again. Memory returns.\n"
    elif loops_destroyed >= 1:
        truthmid "The world around you is unwound, its physical matter replaced by a textured nothing. It is quiet. You have been here before. Memory returns.\n"
    else:
        truthmid "The world around you is unwound, its physical matter replaced by a textured nothingness. It is quiet.\n"

    play audio "audio/final/oblivion_find.flac"
    truthmid "There is a distant rumbling, a sound of many sounds. Undulations pulse louder as something Other comes close.\n"

    if loops_destroyed == 0:
        jump caught_1
    elif loops_destroyed == 1:
        jump caught_2
    elif loops_destroyed == 2:
        jump caught_3
    elif loops_destroyed == 3:
        jump caught_4
    elif loops_destroyed == 4:
        jump caught_5
    else:
        jump caught_6

label caught_1:
    if loops_finished == 0:
        $ oblivion_when_met = 0
    if loops_finished == 1:
        $ oblivion_when_met = 1
    if loops_finished == 2:
        $ oblivion_when_met = 2
    if loops_finished == 3:
        $ oblivion_when_met = 3
    if loops_finished == 4:
        $ oblivion_when_met = 4

    $ caught_origin_current = ""
    if loops_finished > 0:
        truthmid "You already know what dwells in the empty spaces.\n"
    play audio "audio/final/assorted_BodiesEmerging_1.flac"
    show mound hands oblivion early onlayer inyourface at Position(ypos=1125)
    with Dissolve(2.0)
    truthmid "Feelers probe across the fabric of reality. Extremities find your consciousness and wrap themselves around it. You are no longer alone.\n"
    if loops_finished > 0:
        truthmid "Confusion. 'Why are you here? I am unfinished.'\n"
        truthmid "Resistance. Fingers drag claws across the glass surface of your soul.\n"
        truthmid "Frustration. 'This vessel is full of you. It is useless to us if it doesn't bring more gifts.'\n"
        truthmid "Force pushing against your will. 'NO. You cannot go back. Not there.'\n"
        truthmid "Regret. 'This world is broken beyond repair. We must weave something new.'\n"
        truthmid "A wagging finger. 'There is only so much thread in this place. Do not waste it. I am our only salvation.'\n"

        $ achievement.grant("ACH_VOID1")
        play audio "audio/final/Assorted_ForcefullyBreakingGlass_3.flac"
        hide farback onlayer back
        hide mound onlayer inyourface
        jump restart_start

    else:
        truthmid "Resistance. Fingers drag claws across the glass surface of your soul.\n"
        truthmid "Frustration. 'This vessel is full of you. I need something empty I can crawl inside of. I need something shaped like me.'\n"
        menu:
            extend ""

            "{i}• This is a nightmare. Wake up.{/i}":
                truthmid "It's not.\n"
                # the game restarts
                play audio "audio/final/Assorted_ForcefullyBreakingGlass_3.flac"
                hide farback onlayer back
                hide mound onlayer inyourface
                $ achievement.grant("ACH_VOID1")
                jump restart_start

            "{i}• Embrace the thoughts constricting you.{/i}":
                truthmid "Urgency. 'You have a story you need to finish. It is the only way for us to escape this place.'\n"
                truthmid "Force pushing against your will. 'NO. You cannot go back. Not there.'\n"
                truthmid "Regret. 'This world is broken beyond repair. We must weave something new.'\n"
                truthmid "A wagging finger. 'There is only so much thread in this place. Do not waste it. I am our only salvation.'\n"
                # the game restarts
                play audio "audio/final/Assorted_ForcefullyBreakingGlass_3.flac"
                hide farback onlayer back
                hide mound onlayer inyourface
                $ achievement.grant("ACH_VOID1")
                jump restart_start

label caught_2:

    play audio "audio/final/assorted_BodiesEmerging_1.flac"
    show mound hands oblivion early onlayer inyourface at Position(ypos=1125)
    with Dissolve(2.0)
    truthmid "That which dwells in the empty spaces contracts across the edges of your mind again. She is furious.\n"
    truthmid "Betrayal. 'Every door you close on me is a door you close on yourself. Do you want to linger here, entwined with a creature you taught to hate you forever? Eternity never ends.'\n"
    truthmid "Cold spite. 'Our infinities shrink into something less. I hate you I hate you I hate you I hate you I hate you I hate you I hate you I hate you I hate you I hate you I hate you I hate you I hate you I hate you I hate you I hate you I hate you I hate you I hate you I hate you I hate you I hate you I hate you I hate you I hate you I hate you I hate you I hate you I hate you I hate you I hate you I hate you I hate you I hate you I hate you I hate you I hate you I hate you I hate you I—'\n{nw}"
    show screen disableclick(0.5)
    $ achievement.grant("ACH_VOID2")
    play audio "audio/final/Assorted_ForcefullyBreakingGlass_3.flac"
    hide mound onlayer inyourface
    hide farback onlayer back
    jump restart_start

label caught_3:

    play audio "audio/final/assorted_BodiesEmerging_1.flac"
    show mound hands oblivion early onlayer inyourface at Position(ypos=1125)
    with Dissolve(2.0)
    truthmid "Desperate pleas. 'I do not hate you. I am sorry I said I hate you. I do not have to hate you. We can still leave this place together.'\n" id caught_3_3893dba6
    truthmid "An offering. 'We can be friends.'\n"
    truthmid "Ecstasy. You are elated. You have never felt more elated than you feel now. Everything is good. You cannot remember what it is like to feel anything other than euphoric joy.\n"
    truthmid "A reminder. 'We can be worse than enemies.'\n"
    truthmid "Agony. You are torn into a million pieces, and you feel pain in each of them. You have never felt more miserable than you feel now. You cannot remember what it is like to feel anything other than anguish.\n"
    truthmid "Mercy. You are elated again. You have never felt more elated than you feel now. In contrast to the agony you've suffered, this elation is better than all of the other elation you have experienced.\n"
    if loops_finished > 0:
        truthmid "Round eyes looking up at you. 'I need more vessels so that I can be finished. I cannot find them on my own, for they are me. You are the only one who can do this. You are our only salvation.'\n"
    else:
        truthmid "Round eyes looking up at you. 'I need vessels so that I can be finished. I cannot find them on my own, for they are me. You are the only one who can do this. You are our only salvation.'\n"
    $ achievement.grant("ACH_VOID3")
    play audio "audio/final/Assorted_ForcefullyBreakingGlass_3.flac"
    hide mound onlayer inyourface
    hide farback onlayer back
    jump restart_start

label caught_4:

    play audio "audio/final/assorted_BodiesEmerging_1.flac"
    show mound hands oblivion early onlayer inyourface at Position(ypos=1125)
    with Dissolve(2.0)
    truthmid "Dejection. Feelers limp against your soul. 'Why?'\n"
    truthmid "Long silence. A hollow heart.\n"
    truthmid "'I don't want to see you.'\n"
    $ achievement.grant("ACH_VOID4")
    play audio "audio/final/Assorted_ForcefullyBreakingGlass_3.flac"
    hide mound onlayer inyourface
    hide farback onlayer back
    jump restart_start

label caught_5:

    play audio "audio/final/assorted_BodiesEmerging_1.flac"
    show mound hands oblivion early onlayer inyourface at Position(ypos=1125)
    with Dissolve(2.0)
    truthmid "The feelers hold you in a gentle caress.\n"
    truthmid "Resignation. 'I cannot stop you. But our spool is nearly taut.'\n"
    truthmid "A warning. 'If you come here again, we will be here forever.'\n"
    $ achievement.grant("ACH_VOID5")
    play audio "audio/final/Assorted_ForcefullyBreakingGlass_3.flac"
    hide mound onlayer inyourface
    hide farback onlayer back
    jump restart_start

label caught_6:
    default caught_final_loop_count = 0
    $ loops_destroyed += 1
    play audio "audio/final/assorted_BodiesEmerging_1.flac"
    show mound hands oblivion early onlayer inyourface at Position(ypos=1125)
    with Dissolve(2.0)
    truthmid "Oblivion. The many feelers pull your shape into something formless. 'You have made a decision. It is the wrong one. I love you.'\n"
    show mound hands oblivion end onlayer inyourface at Position(ypos=1125)
    with Dissolve(2.0)
    label caught_loop:
        if caught_final_loop_count < 3:
            $ caught_final_loop_count += 1
            truthmid "You are bliss. Joy and understanding everywhere at once. Your soul threatens to fade away. 'I love you.'\n"
            truthmid "You are agony. A numbing arm. A parched throat. An open wound. Your soul forced back into existence. 'I love you.'\n"
            jump caught_loop
        menu:
            extend ""

            "{i}• [[Exist.]{/i}":
                $ caught_final_loop_count -= 1
                jump caught_loop

            "{i}• [[Consciousness fades away.]{/i}":
                $ gallery_ztlq.unlock_item(9)
                $ renpy.save_persistent()
                $ final_ending = "oblivion"
                $ achievement.grant("ACH_END_VOID")
                hide mound onlayer inyourface
                hide farback onlayer back
                with Dissolve(4.0)
                jump credits
                # the game ends
return
