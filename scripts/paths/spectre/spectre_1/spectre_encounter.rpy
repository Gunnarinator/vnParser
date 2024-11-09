label spectre_encounter_start:

    default spectre_hostile = False
    default spectre_possession_ask = False
    default spectre_home_comment = False
    default spectre_narrator_loop = False
    default spectre_world_end_explore = False
    default spectre_thoughts_explore = False
    default spectre_death_shared = False
    default spectre_blade_retrieve = False
    default spectre_death_concept_comment = False
    default spectre_endings_discuss = False

    default spectre_can_wraith = True

    voice "audio/voices/ch2/spectre/_encounter/narrator/1.flac"
    play audio "audio/final/Spectre_WindPassingThrough_3.flac"
    hide spectre onlayer back
    show spectre c approach onlayer front at Position(ypos=1125)
    with Dissolve(1.0)
    $ renpy.pause(0.25)
    voice sustain
    show spectre c circle onlayer front at Position(ypos=1125)
    with Dissolve(1.0)
    n "The Princess drifts across the room into your orbit, gently running her fingers across your shoulders and down your neck as she circles you.\n"
    play audio "audio/final/Spectre_PossessingPlayer_6.flac"
    hide spectre onlayer front
    with Dissolve(1.0)
    $ renpy.pause(0.5)
    voice "audio/voices/ch2/spectre/_encounter/narrator/2.flac"
    show spectre c circle 2 onlayer front at Position(ypos=1125)
    with Dissolve(1.0)
    n "Her touch is cold and ethereal, formless yet real enough that her icy fingertips send shivers dancing across your skin.\n"
    show spectre c coy onlayer front
    with Dissolve(1.0)
    if blade_held:
        voice "audio/voices/ch2/spectre/_encounter/cold/1.flac"
        cold "So she has a body. And she's right there. That means we could kill her again, if we wanted to.\n"
    else:
        voice "audio/voices/ch2/spectre/_encounter/cold/2.flac"
        cold "So she has a body. And she's right there. We could probably grab her and kill her again, if we wanted to. We don't even need a blade. She looks fragile enough to me.\n"
    menu:
        extend ""

        "{i}• [[Slay the Princess.]{/i}" if blade_held and spectre_hostile == False:
            label spectre_slay_join:
                stop music
                $ spectre_hostile = True
                voice "audio/voices/ch2/spectre/_encounter/narrator/3.flac"
                play audio "audio/one_shot/knife_slash.flac"
                scene bg black big onlayer inyourface at Position(ypos=1125)
                n "Without a moment's hesitation, you lash out with your blade.\n"
                $ gallery_spectre.unlock_item(14)
                voice "audio/voices/ch2/spectre/_encounter/narrator/4.flac"
                play audio "audio/final/Spectre_WindPassingThrough_13.flac"
                hide bg onlayer inyourface
                show spectre c cut onlayer front
                show player spectre c cut onlayer inyourface at Position(ypos=1125)
                with Dissolve(0.5)
                n "It's like you're slashing at air. No matter how many times you stab at her, no matter how many angles you strike from, all you manage to do is interrupt her form, the skin of your hand prickling with cold as it passes through, unable to find anything solid.\n"
                voice "audio/voices/ch2/spectre/_encounter/cold/3.flac"
                cold "Hm.\n"
                voice "audio/voices/ch2/spectre/_encounter/princess/1.flac"
                hide player onlayer inyourface
                show spectre c scary onlayer front
                with dissolve
                p "You're adorable when you're confused.\n"
                voice "audio/voices/ch2/spectre/_encounter/princess/2.flac"
                play audio "audio/final/Spectre_PossessingPlayer_3.flac"
                play music "audio/_music/ch2/spectre/The Spectre II.flac" loop
                show spectre c scary talk onlayer front
                sp "But I didn't say you could touch me.\n"
                jump spectre_hostile_join

        "{i}• [[Grab her.]{/i}" if blade_held == False:
            label spectre_grab_join:
                stop music
                $ spectre_hostile = True
                voice "audio/voices/ch2/spectre/_encounter/narrator/5.flac"
                play audio "audio/final/Spectre_CuttingThroughCloud_1.flac"
                scene bg black big onlayer inyourface at Position(ypos=1125)
                n "Before she can suspect a thing, you lunge forward and grab her arm.\n"
                voice "audio/voices/ch2/spectre/_encounter/narrator/6.flac"
                play audio "audio/final/Spectre_WindPassingThrough_13.flac"
                hide bg onlayer inyourface
                show spectre c grab onlayer front
                show player spectre c grab onlayer inyourface at Position(ypos=1125)
                with Dissolve(0.5)
                n "You feel substance for the briefest of moments, but then you feel nothing at all, as though all you've done is clutch at empty air.\n"
                voice "audio/voices/ch2/spectre/_encounter/cold/3.flac"
                cold "Hm.\n"
                #voice "audio/voices/ch2/spectre/_encounter/narrator/7.flac"
                #n "As you stare in confusion at your empty hand, a few wisps of ghostly princess still wafting their way between your fingers, a harsh whisper twists its way into your ears.\n"
                voice "audio/voices/ch2/spectre/_encounter/princess/1.flac"
                hide player onlayer inyourface
                show spectre c scary onlayer front
                with dissolve
                p "You're adorable when you're confused.\n"
                voice "audio/voices/ch2/spectre/_encounter/princess/2.flac"
                play music "audio/_music/ch2/spectre/The Spectre II.flac" loop
                play audio "audio/final/Spectre_PossessingPlayer_3.flac"
                show spectre c scary talk onlayer front
                sp "But I didn't say you could touch me.\n"
                label spectre_hostile_join:
                    voice "audio/voices/ch2/spectre/_encounter/princess/4.flac"
                    show spectre c flat talk onlayer front
                    with dissolve
                    p "Why are you even here? Just making sure you finished the job or what?\n"
                    show spectre c flat onlayer front
                    with dissolve
                    jump spectre_menu_hostile

        "{i}• [[Wait and see how things play out.]{/i}":
            if blade_held == False:
                voice "audio/voices/ch2/spectre/_encounter/princess/5.flac"
                show spectre c thinking talk onlayer front
                with dissolve
                p "I see you don't have that annoying knife anymore.\n"
                voice "audio/voices/ch2/spectre/_encounter/princess/6.flac"
                show spectre c shrug talk onlayer front
                with dissolve
                p "So... does that mean you regret what you've done? Are you here to apologize and make nice? Beg for absolution, maybe?\n"
                voice "audio/voices/ch2/spectre/_encounter/princess/7.flac"
                show spectre c dismissive talk onlayer front
                with dissolve
                p "Because I might be interested in seeing a little begging.\n"
                show spectre c dismissive onlayer front
                with dissolve
            else:
                voice "audio/voices/ch2/spectre/_encounter/princess/8.flac"
                show spectre c flat talk onlayer front
                with dissolve
                p "I see you brought that annoying knife again.\n"
                voice "audio/voices/ch2/spectre/_encounter/princess/9.flac"
                show spectre c scary onlayer front
                with dissolve
                p "So... are you waiting for a chance to use it, or are you here for something else?\n"
            jump spectre_menu_friendly

label spectre_menu_friendly:

    menu:
        extend ""

        "{i}• (Explore) See, this is exactly what I was trying to tell you about in the woods. This already happened. We killed her.{/i}" if spectre_1_forest_share_loop and spectre_narrator_loop == False:
            $ spectre_narrator_loop = True
            voice "audio/voices/ch2/spectre/_encounter/narrator/8.flac"
            n "Yes, obviously things are... strange right now. I think it's safe to say that you've seen something, something you shouldn't have seen. Whatever worlds you've hopped between, whatever versions of me you've met, none of that matters now. There's no changing what's already happened. But you have a job to finish.\n" id spectre_menu_friendly_d17d98dc
            voice "audio/voices/ch2/spectre/_encounter/hero/1.flac"
            hero "Finish how?! We already did what you told us. And now she's a ghost!\n"
            if blade_held:
                voice "audio/voices/ch2/spectre/_encounter/narrator/9.flac"
                n "You haven't tried slaying her yet this time, though, have you?\n"
            else:
                voice "audio/voices/ch2/spectre/_encounter/narrator/10.flac"
                n "There's a perfectly pristine blade waiting for you upstairs. You could always use it to... Oh, I don't know... slay her?\n"
            voice "audio/voices/ch2/spectre/_encounter/cold/4.flac"
            cold "And then what?\n"
            voice "audio/voices/ch2/spectre/_encounter/narrator/11.flac"
            n "And then you'll have saved the world.\n"
            voice "audio/voices/ch2/spectre/_encounter/hero/2.flac"
            hero "I think he's asking about what happens after we save the world. If that's even still an option.\n"
            voice "audio/voices/ch2/spectre/_encounter/narrator/12.flac"
            n "What do you mean, 'after'?\n"
            voice "audio/voices/ch2/spectre/_encounter/cold/5.flac"
            cold "You already know what we mean, don't you? So why don't you go ahead and tell us? Are you going to try and lock us away in a timeless void again? Because I didn't much care for that.\n"
            voice "audio/voices/ch2/spectre/_encounter/narrator/13.flac"
            n "{i}I'm{/i} not going to lock you anywhere.\n"
            voice "audio/voices/ch2/spectre/_encounter/cold/6.flac"
            cold "What an interesting choice of emphasis.\n"
            jump spectre_menu_friendly

        "{i}• (Explore) ''I killed you! What are you doing not being dead?''{/i}" if spectre_not_dead_explore == False:
            $ spectre_not_dead_explore = True
            $ spectre_death_concept_comment = True
            voice "audio/voices/ch2/spectre/_encounter/princess/10.flac"
            show spectre c thinking talk onlayer front
            with Dissolve(0.5)
            p "I don't feel very dead. But I guess I'm not... {i}not{/i}-dead. So you must have only mostly killed me.\n"
            voice "audio/voices/ch2/spectre/_encounter/princess/11.flac"
            show spectre c homesick talk onlayer front
            with Dissolve(0.5)
            p "Or maybe death is only mostly-real, but it's also mostly not-real. I'm not sure. I'm just the one these things have happened to, not the one with all the answers. Or any of the answers.\n"
            voice "audio/voices/ch2/spectre/_encounter/hero/8.flac"
            show spectre c homesick onlayer front
            with dissolve
            hero "But {b}we're{/b} not a ghost... unless we are?\n"
            if spectre_1_cabin_mirror_ask or spectre_1_cabin_mirror_approached:
                voice "audio/voices/ch2/spectre/_encounter/hero/9.flac"
                hero "Maybe that's why the mirror disappeared. We're actually dead.\n"
            #voice "audio/voices/ch2/spectre/_encounter/narrator/17.flac"
            #n "You're not dead, and you're not a ghost.\n"
            voice "audio/voices/ch2/spectre/_encounter/cold/14.flac"
            cold "Death—at least as a form of permanence—is just a concept, and clearly it's not a very useful one anymore. Maybe we should throw it out entirely.\n"
            #voice "audio/voices/ch2/spectre/_encounter/narrator/18.flac"
            #n "See, this is why I didn't want you to talk to her. Death is not just a concept. It is an extremely real phenomenon. Don't let her distort your reality. Cold hard facts exist. The truth exists. It has to.\n"
            jump spectre_menu_friendly

        "{i}• (Explore) ''Your body's right there, though. Your {b}dead{/b} body.''{/i}" if spectre_death_concept_comment and spectre_body_point == False:
            $ spectre_body_point = True
            voice "audio/voices/ch2/spectre/_encounter/narrator/19.flac"
            show spectre c dismissive onlayer front
            with Dissolve(0.5)
            n "The Princess glances back at the bones lying on the floor.\n"
            voice "audio/voices/ch2/spectre/_encounter/princess/12.flac"
            show spectre c shrug talk onlayer front
            with Dissolve(0.5)
            p "It's just a body. Do you believe these bones, or do you believe me? Because those bones aren't talking to you.\n"
            voice "audio/voices/ch2/spectre/_encounter/cold/15.flac"
            show spectre c coy onlayer front
            with dissolve
            cold "She's seeing things pragmatically. We should do the same. Reality is what's in front of us, not our preconceptions of what it should be. There doesn't need to be a static 'truth.' There doesn't need to be objectivity.\n"
            jump spectre_menu_friendly

        "{i}• (Explore) ''Do you know why you came back?''{/i}" if spectre_why_back == False:
            $ spectre_why_back = True
            #voice "audio/voices/ch2/spectre/_encounter/narrator/20.flac"
            #n "The Princess closes her eyes as if in mournful reflection.\n"
            voice "audio/voices/ch2/spectre/_encounter/princess/13.flac"
            show spectre c flat talk onlayer front
            with dissolve
            p "How should I know? Why does anyone come back? Maybe I have unfinished business with you. Or maybe you have unfinished business with me.\n"
            voice "audio/voices/ch2/spectre/_encounter/princess/14.flac"
            show spectre c homesick talk onlayer front
            with dissolve
            p "All I know is there's a hole in my chest, and not the big obvious one that you put there. There's something older and deeper.\n"
            voice "audio/voices/ch2/spectre/_encounter/princess/15.flac"
            p "A nagging reminder that I'm not where I'm supposed to be.\n"
            show spectre c homesick onlayer front
            with dissolve
            jump spectre_menu_friendly

        "{i}• (Explore) ''And where are you supposed to be?''{/i}" if spectre_home_comment == False and spectre_why_back:
            $ spectre_home_comment = True
            voice "audio/voices/ch2/spectre/_encounter/princess/16.flac"
            show spectre c homesick talk onlayer front
            with dissolve
            p "Home.\n"
            label spectre_friendly_home_reveal:
                voice "audio/voices/ch2/spectre/_encounter/hero/10.flac"
                hero "And just where is home, I wonder?\n"
                voice "audio/voices/ch2/spectre/_encounter/princess/17.flac"
                show spectre c smile talk onlayer front
                with dissolve
                p "I don't know where home is. I just know it isn't here. But I can feel it calling to me from some place far away.\n"
                voice "audio/voices/ch2/spectre/_encounter/princess/18.flac"
                show spectre c homesick talk onlayer front
                with dissolve
                p "Wherever I'm supposed to be, it's out there.\n"
                voice "audio/voices/ch2/spectre/_encounter/cold/16.flac"
                show spectre c homesick onlayer front
                with dissolve
                cold "How specific.\n"
                voice "audio/voices/ch2/spectre/_encounter/narrator/21.flac"
                n "And how convenient for her. You see what she's doing, right? She's suggesting that the only way you can rid yourself of her would be to let her out, which, in case you haven't been listening, will spell the end of the entire world.\n"
                jump spectre_menu_friendly

        "{i}• (Explore) ''Is there any way I can help you get home? Do you need me to bury those bones?''{/i}" if spectre_home_comment and spectre_home_follow == False and spectre_possession_ask == False and spectre_bones_ask == False:
            $ spectre_bones_ask = True
            $ spectre_home_follow = True
            voice "audio/voices/ch2/spectre/_encounter/princess/19.flac"
            show spectre c shrug talk onlayer front
            with dissolve
            p "No, those bones are just a body. They aren't me. Bury them, smash them, it won't do a thing.\n"
            voice "audio/voices/ch2/spectre/_encounter/princess/20.flac"
            show spectre c smile talk onlayer front
            with dissolve
            p "But you can help me. This place won't let me leave. At least... not alone.\n"
            jump spectre_friendly_possession_early_join

        "{i}• (Explore) ''Stop playing the victim. You threatened me last time.''{/i}" if spectre_victim == False:
            label spectre_victim_stop:
                $ spectre_victim = True
                voice "audio/voices/ch2/spectre/_encounter/princess/21.flac"
                show spectre c flat talk onlayer front
                with dissolve
                p "Well, yeah. You brought a knife with you. Was I supposed to just welcome you with open arms when you obviously had stabbing on the mind?\n"
                show spectre c flat onlayer front
                with dissolve
                menu:
                    extend ""

                    "{i}• (Explore) ''That knife could have been for anything!''{/i}":
                        voice "audio/voices/ch2/spectre/_encounter/princess/22a.flac"
                        show spectre c angry onlayer front
                        with Dissolve(0.5)
                        p "It could have. But it wasn't. You can't blame me for threatening a would-be-knife-wielding-murderer, especially when that would-be-knife-wielding-murderer became an actual-knife-wielding-murderer.\n"
                        if spectre_hostile:
                            jump spectre_menu_hostile
                        else:
                            jump spectre_menu_friendly

                    "{i}• (Return) [[Leave it at that.]{/i}":
                        if spectre_hostile:
                            jump spectre_menu_hostile
                        else:
                            jump spectre_menu_friendly

        "{i}• (Explore) ''I'm sorry I killed you last time, I shouldn't have done that.''{/i}" if spectre_sorry == False:
            $ spectre_sorry = True
            voice "audio/voices/ch2/spectre/_encounter/princess/23.flac"
            show spectre c flat talk onlayer front
            with dissolve
            p "Too little, too late. But... you can still make things right.\n"
            show spectre c flat onlayer front
            with dissolve
            voice "audio/voices/ch2/spectre/_encounter/cold/17.flac"
            cold "She's not in a position to bargain with us. You don't have to do anything you don't want to.\n"
            voice "audio/voices/ch2/spectre/_encounter/hero/11a.flac"
            hero "We don't have to do anything, but maybe we should. We did kill her. Wouldn't it be the moral thing to help her now that we have another chance?\n"
            voice "audio/voices/ch2/spectre/_encounter/narrator/22a.flac"
            n "When a hero slays a monster, does he apologize to it?\n"
            voice "audio/voices/ch2/spectre/_encounter/hero/12.flac"
            hero "... No.\n"
            voice "audio/voices/ch2/spectre/_encounter/narrator/23a.flac"
            n "So don't try to 'make things right.' She was going to end the world. You didn't do anything wrong, aside from apparently killing yourself, and that doesn't have much to do with her.\n"
            jump spectre_menu_friendly

        "{i}• (Explore) ''Do you want me to die? Do you want me to kill myself to satisfy some sort of sick revenge fantasy? Because I already did that and it wouldn't be hard to do it again.''{/i}" if spectre_grovel_1 == False:
            $ spectre_grovel_1 = True
            $ spectre_death_shared = True
            voice "audio/voices/ch2/spectre/_encounter/hero/13.flac"
            hero "Are we putting this to a vote? Because personally, I'd prefer if we didn't die again...\n"
            voice "audio/voices/ch2/spectre/_encounter/cold/18.flac"
            cold "If that's what it comes down to, that's what it comes down to. But I don't see the point of offing ourselves just yet.\n"
            voice "audio/voices/ch2/spectre/_encounter/princess/24.flac"
            show spectre c coy talk onlayer front
            with dissolve
            p "Aw, that's sweet of you to offer, but killing yourself wouldn't help either of us.\n"
            voice "audio/voices/ch2/spectre/_encounter/narrator/24.flac"
            show spectre c coy onlayer front
            with dissolve
            n "It would seem that everyone here is in agreement except for you. I shouldn't have to tell you that you shouldn't kill yourself. So please, try to keep your suicidal tendencies in check.\n"
            if spectre_home_comment:
                voice "audio/voices/ch2/spectre/_encounter/princess/25.flac"
                show spectre c homesick talk onlayer front
                with dissolve
                p "Like I said, I just want to go home.\n"
            else:
                voice "audio/voices/ch2/spectre/_encounter/princess/26.flac"
                show spectre c homesick talk onlayer front
                with dissolve
                p "I just want to go home.\n"
                $ spectre_home_comment = True
                jump spectre_friendly_home_reveal
            jump spectre_menu_friendly

        "{i}• (Explore) ''I'm sorry. Is there any way I can make it up to you?''{/i}" if spectre_sorry == False:
            $ spectre_sorry = True
            if spectre_possession_ask:
                voice "audio/voices/ch2/spectre/_encounter/princess/27.flac"
                show spectre c flat talk onlayer front
                with dissolve
                p "You already know what I want. Let me in.\n"
                show spectre c flat onlayer front
                with dissolve
            else:
                voice "audio/voices/ch2/spectre/_encounter/princess/28.flac"
                show spectre c flat talk onlayer front
                with dissolve
                p "Of course there is! You can give me the only thing I've ever wanted— a way out of this basement. The place won't let me leave.\n"
                jump spectre_friendly_possession_early_join
            jump spectre_menu_friendly

        "{i}• (Explore) ''The people who wanted you dead tricked me, and the enemy of my enemy is my friend. Let's team up.''{/i}" if spectre_trick == False and spectre_home_comment == False and spectre_home_comment == False:
            $ spectre_trick = True
            show spectre c flat onlayer front
            with dissolve
            if spectre_narrator_loop:
                voice "audio/voices/ch2/spectre/_encounter/narrator/25.flac"
                n "Nobody 'tricked you.' I'm sure that other me gave you wholly accurate information that you wisely chose to act on.\n"
            elif spectre_1_forest_share_loop:
                $ spectre_narrator_loop = True
                voice "audio/voices/ch2/spectre/_encounter/narrator/26.flac"
                n "Nobody 'tricked you' and the fact that the Princess' spirit has risen from the dead should be more than enough evidence that she isn't exactly sweet and innocent. It's all been an act. She's pretending.\n"
                voice "audio/voices/ch2/spectre/_encounter/cold/19.flac"
                cold "I wouldn't say she's ever pretended to be sweet or innocent.\n"
                voice "audio/voices/ch2/spectre/_encounter/hero/14.flac"
                hero "She does have a little bit of an attitude... but I can't blame her, we did kill her after all. I wouldn't be nice to my murderer if I was killed.\n"
            else:
                $ spectre_narrator_loop = True
                voice "audio/voices/ch2/spectre/_encounter/narrator/27.flac"
                n "Okay... I didn't want to be open to the idea, but there's no denying it now. You've clearly been here before.\n"
                voice "audio/voices/ch2/spectre/_encounter/cold/20.flac"
                cold "Oh? What tipped you off? Was it the corpse?\n"
                voice "audio/voices/ch2/spectre/_encounter/narrator/28.flac"
                n "It doesn't matter. The only thing that matters is that nobody 'tricked you.' I've done nothing but give you wholly accurate information, and I'm sure whatever version of me you met in whatever other world you came from gave you accurate information, as well.\n"
                #voice "audio/voices/ch2/spectre/_encounter/hero/15a.flac"
                #hero "And how do you know that?\n"
                #voice "audio/voices/ch2/spectre/_encounter/narrator/29.flac"
                #n "Because any other me you've met is still me, and {i}I{/i} haven't 'tricked you,' nor do I have any desire to trick you in the future.\n"
                #voice "audio/voices/ch2/spectre/_encounter/narrator/30.flac"
                #n "And clearly you decided to heed most of the warnings I gave you. Otherwise you never would have mostly-slayed her.\n"
                #voice "audio/voices/ch2/spectre/_encounter/cold/21.flac"
                #cold "But we did slay her.\n"
                #voice "audio/voices/ch2/spectre/_encounter/narrator/31.flac"
                #n "Yes, fine, you did slay her. But clearly, part of her is still {b}un-slayed{/b}. {i}Sigh{/i}. There's no point wasting time bickering over semantics.\n"
            #voice "audio/voices/ch2/spectre/_encounter/narrator/32a.flac"
            #n "The fact that you apparently botched the landing isn't on the me you're talking to, nor is it on any other version of me that you've encountered.\n"
            #voice "audio/voices/ch2/spectre/_encounter/cold/22.flac"
            #cold "You're using a lot of words to say a lot of nothing.\n"
            voice "audio/voices/ch2/spectre/_encounter/princess/29.flac"
            show spectre c flat talk onlayer front
            with dissolve
            p "'The enemy of my enemy...'\n"
            voice "audio/voices/ch2/spectre/_encounter/narrator/33.flac"
            show spectre c circle onlayer front
            with Dissolve(1.0)
            $ renpy.pause(0.25)
            play audio "audio/final/Spectre_PossessingPlayer_6.flac"
            voice sustain
            hide spectre onlayer front
            with dissolve
            $ renpy.pause(0.25)
            voice sustain
            with dissolve
            show spectre c circle 2 onlayer front at Position(ypos=1125)
            with Dissolve(1.0)
            n "The Princess circles you again, her icy fingertips trailing up your spine, sending shivers rippling across your flesh.\n"
            voice "audio/voices/ch2/spectre/_encounter/princess/30.flac"
            show spectre c ask onlayer front
            with Dissolve(0.5)
            p "I don't want enemies. I don't want to fight. I just want to go home.\n"
            voice "audio/voices/ch2/spectre/_encounter/princess/31.flac"
            show spectre c ask talk onlayer front
            with dissolve
            p "Is that really so much to ask?\n"
            $ spectre_home_comment = True
            jump spectre_friendly_home_reveal

        "{i}• (Explore) ''What do you want from me?''{/i}" if spectre_possession_ask == False:
            if spectre_home_comment:
                voice "audio/voices/ch2/spectre/_encounter/princess/32.flac"
                show spectre c homesick talk onlayer front
                with dissolve
                p "A way back to where I belong. This place won't let me leave. At least not alone.\n"
            else:
                $ spectre_home_comment = True
                voice "audio/voices/ch2/spectre/_encounter/princess/33.flac"
                show spectre c homesick talk onlayer front
                with dissolve
                p "I just want the same thing I've always wanted. To go home. But this place won't let me go. At least not alone.\n"
            label spectre_friendly_possession_early_join:
                voice "audio/voices/ch2/spectre/_encounter/princess/34.flac"
                show spectre c flat talk onlayer front
                with dissolve
                p "I've tried. Before you came back to me, I explored every inch of this place, even the spaces between the walls. But I never found a way out. I always wound up right back here.\n"
                voice "audio/voices/ch2/spectre/_encounter/hero/16.flac"
                show spectre c homesick onlayer front
                with dissolve
                hero "Maybe we should just leave. If she can't get out on her own, then why do we have to do anything? We could probably walk out right now and everything would be fine.\n"
                voice "audio/voices/ch2/spectre/_encounter/narrator/34.flac"
                n "'Hasn't gotten out' and 'can't get out' are two very different things.\n"
                voice "audio/voices/ch2/spectre/_encounter/cold/23.flac"
                cold "That'd be dull, anyway. It's more interesting if we make a choice.\n"
                label spectre_friendly_possession_join:
                    $ spectre_possession_ask = True
                    #voice "audio/voices/ch2/spectre/_encounter/narrator/35.flac"
                    #n "Her spectral skin brushes against you, cold spots spreading out from the places where her body attempts to intersect yours.\n"
                    voice "audio/voices/ch2/spectre/_encounter/princess/35.flac"
                    show spectre c ask talk onlayer front
                    with Dissolve(0.5)
                    p "But you can come and go as you please, can't you? So... let me hitch a ride.\n"
                    voice "audio/voices/ch2/spectre/_encounter/princess/36.flac"
                    play audio "audio/final/Spectre_PossessingPlayer_1.flac"
                    show spectre c angry talk onlayer front
                    sp "After all. You owe me.\n"
                    voice "audio/voices/ch2/spectre/_encounter/narrator/36.flac"
                    show spectre c ask onlayer front
                    with dissolve
                    n "Absolutely not.\n"
                    voice "audio/voices/ch2/spectre/_encounter/hero/17.flac"
                    hero "Is she asking if she can... possess us?\n"
                    voice "audio/voices/ch2/spectre/_encounter/narrator/37.flac"
                    n "She is, and I hope I don't need to explain why you can't let that happen. It would be catastrophic if she managed to escape this place, and if you let her in, there is very little anyone could do to stop her.\n"
                    voice "audio/voices/ch2/spectre/_encounter/hero/18.flac"
                    hero "Would she be able to see... {b}us{/b} if we went along with it?\n"
                    voice "audio/voices/ch2/spectre/_encounter/cold/24.flac"
                    show spectre c homesick onlayer front
                    with Dissolve(0.5)
                    cold "Now isn't that an interesting thought. We could finally bring her face-to-face with Him. I wonder what she would have to say to the one who wants her dead so, so badly...\n"
                    voice "audio/voices/ch2/spectre/_encounter/narrator/38.flac"
                    n "{i}Sigh{/i}. You won't like how things play out if you go down this path.\n"
                    label spectre_friendly_possession_menu:
                        default spectre_possession_no_explore = False
                        default spectre_possession_no_wont = False
                        default spectre_cold_trap_suggest = False
                        default spectre_possession_temporary = False
                        default spectre_possession_control = False
                        menu:
                            extend ""

                            "{i}• (Explore) ''What if I say no?''{/i}" if spectre_possession_no_explore == False:
                                $ spectre_possession_no_explore = True
                                voice "audio/voices/ch2/spectre/_encounter/princess/37.flac"
                                show spectre c shrug talk onlayer front
                                with dissolve
                                p "Then I won't hitch a ride.\n"
                                show spectre c flat onlayer front
                                with dissolve
                                jump spectre_friendly_possession_menu

                            "{i}• (Explore) ''You {b}won't{/b} hitch a ride if I say no, or you {b}can't{/b} hitch a ride?''{/i}" if spectre_possession_no_explore and spectre_possession_no_wont == False:
                                $ spectre_possession_no_wont = True
                                voice "audio/voices/ch2/spectre/_encounter/princess/38.flac"
                                show spectre c dismissive talk onlayer front
                                with dissolve
                                p "I'm sure you'd like to know. It's a shame I won't tell you.\n"
                                voice "audio/voices/ch2/spectre/_encounter/princess/39.flac"
                                show spectre c smile talk onlayer front
                                with dissolve
                                p "But... it'll be easier for both of us if you just let me in. And doesn't it sound nice?\n"
                                voice "audio/voices/ch2/spectre/_encounter/hero/19.flac"
                                show spectre c smile onlayer front
                                with dissolve
                                hero "Maybe for her, but it's crowded enough in here as-is.\n"
                                voice "audio/voices/ch2/spectre/_encounter/princess/40.flac"
                                show spectre c flat talk onlayer front
                                with dissolve
                                p "You won't have to feel guilty anymore. If you even do feel guilt.\n"
                                show spectre c flat onlayer front
                                with dissolve
                                if spectre_cold_trap_suggest == False:
                                    label spectre_cold_trap_suggest:
                                        $ spectre_cold_trap_suggest = True
                                        voice "audio/voices/ch2/spectre/_encounter/cold/25.flac"
                                        cold "It could be the best way to trap her for good. Doesn't seem like it would be very easy to end the world from inside someone else's body.\n"
                                        voice "audio/voices/ch2/spectre/_encounter/narrator/39.flac"
                                        n "That is a very dangerous train of thought.\n"
                                jump spectre_friendly_possession_menu

                            "{i}• (Explore) ''This would just be temporary, right? You'll leave once we're out of the cabin?''{/i}" if spectre_possession_temporary == False:
                                $ spectre_possession_temporary = True
                                voice "audio/voices/ch2/spectre/_encounter/princess/41.flac"
                                show spectre c dismissive talk onlayer front
                                with dissolve
                                p "If I'm able to. But for all we know that's not how it works. Maybe I'll wind up stuck with you for a long, long, long, long time.\n"
                                show spectre c smile onlayer front
                                with dissolve
                                if spectre_cold_trap_suggest == False:
                                    voice "audio/voices/ch2/spectre/_encounter/hero/20.flac"
                                    hero "I don't much like the sound of that. It's crowded enough in here as-is.\n"
                                    jump spectre_cold_trap_suggest
                                else:
                                    voice "audio/voices/ch2/spectre/_encounter/narrator/40.flac"
                                    n "Do you hear the way she said that? She knows more than she's letting on, don't let her fool you into doing something you'll regret.\n"
                                jump spectre_friendly_possession_menu

                            "{i}• (Explore) ''If... if I let you in, do I still get to be in control?''{/i}" if spectre_possession_control == False:
                                $ spectre_possession_control = True
                                voice "audio/voices/ch2/spectre/_encounter/princess/42.flac"
                                show spectre c shrug talk onlayer front
                                with dissolve
                                p "Sure. Why not?\n"
                                voice "audio/voices/ch2/spectre/_encounter/hero/21.flac"
                                show spectre c flat onlayer front
                                with dissolve
                                hero "That doesn't sound very reassuring.\n"
                                if spectre_cold_trap_suggest == False:
                                    jump spectre_cold_trap_suggest
                                else:
                                    voice "audio/voices/ch2/spectre/_encounter/narrator/41.flac"
                                    n "I can't believe you're even entertaining her right now. I mean, just look at her, do you think she has good intentions for her 'murderer's body'? Of course she doesn't!\n"
                                jump spectre_friendly_possession_menu

                            "{i}• ''Before I agree to anything, we need to talk about what happens after you leave this place. I was told you'd end the world.''{/i}" if spectre_world_end_explore == False:
                                jump spectre_world_end_join

                            "{i}• ''Sounds great. Do it.'' [[Let the Princess possess you.]{/i}":
                                jump spectre_possession_join

                            "{i}• ''The answer's no.''{/i}" if spectre_can_wraith:
                                if wraith_encountered:
                                    $ spectre_can_wraith = False
                                    voice "audio/voices/mound/bonus/path.flac"
                                    mound "This path is already worn by travel and has been seen by one of my many eyes. You cannot walk it again. Change your course.\n"
                                    voice "audio/voices/ch2/beast/_encounter/hero/31.flac"
                                    hero "Wait... what?!\n"
                                    jump spectre_friendly_possession_menu
                                voice "audio/voices/ch2/spectre/_encounter/princess/43.flac"
                                show spectre c homesick talk onlayer front
                                with dissolve
                                p "I see. So that's how it's going to be. That makes me... sad.\n"
                                voice "audio/voices/ch2/spectre/_encounter/princess/44.flac"
                                stop music
                                show spectre c ask talk onlayer front
                                with Dissolve(0.5)
                                p "I guess we'll have to fight then.\n"
                                jump spectre_death

                            "{i}• (Return) ''I need to think on this.''{/i}":
                                voice "audio/voices/ch2/spectre/_encounter/princess/45.flac"
                                show spectre c smile talk onlayer front
                                with dissolve
                                p "Take your time. I know it's a lot to think about. And I'm very good at waiting.\n"
                                show spectre c smile onlayer front
                                with dissolve
                                jump spectre_menu_friendly

        "{i}• (Explore) ''If I knew I'd wind up having to talk to you again, I wouldn't have slain you.''{/i}" if spectre_if_only == False:
            label spectre_had_talk_again:
                $ spectre_if_only = True
                voice "audio/voices/ch2/spectre/_encounter/princess/46.flac"
                show spectre c shrug talk onlayer front
                with dissolve
                p "And if I knew you were going to murder me without even knowing who I was, I wouldn't have given you the chance.\n"
                #voice "audio/voices/ch2/spectre/_encounter/narrator/42.flac"
                #n "The Princess advances, stopping only when her face is a few freezing millimeters from yours, her spectral eyes staring into you unblinking.\n"
                voice "audio/voices/ch2/spectre/_encounter/princess/47.flac"
                play audio "audio/final/Spectre_WindPassingThrough_11.flac"
                show spectre c scary talk onlayer front
                sp "We all make mistakes.\n"
                show spectre c scary onlayer front
                with dissolve
                if spectre_hostile:
                    jump spectre_menu_hostile
                else:
                    jump spectre_menu_friendly

        "{i}• (Explore) ''I died too and I'm not floating around like you are. What happened? Why am I different? Why are you different?''{/i}" if spectre_also_dead == False:
            label spectre_floating:
                $ spectre_death_shared = True
                $ spectre_also_dead = True
                voice "audio/voices/ch2/spectre/_encounter/princess/48.flac"
                show spectre c flat talk onlayer front
                with dissolve
                p "You don't look dead, killer.\n"
                $ gallery_spectre.unlock_item(13)
                voice "audio/voices/ch2/spectre/_encounter/narrator/43.flac"
                play audio "audio/final/Spectre_PossessingPlayer_3.flac"
                show spectre c grab wrist onlayer front
                with dissolve
                n "The Princess grabs your wrist, a sudden shock of cold flowing all the way up your arm, her eyes still fixed on yours as you try to squirm out of her grip.\n"
                voice "audio/voices/ch2/spectre/_encounter/princess/49.flac"
                show spectre c grab wrist talk onlayer front
                with dissolve
                p "And you don't feel dead, either.\n"
                voice "audio/voices/ch2/spectre/_encounter/narrator/44.flac"
                play audio "audio/final/Spectre_WindPassingThrough_3.flac"
                show spectre c coy onlayer front
                with Dissolve(0.5)
                n "She lets go and pulls away. Your fingertips tingle painfully as the chill subsides.\n"
                voice "audio/voices/ch2/spectre/_encounter/princess/50.flac"
                show spectre c flat talk onlayer front
                with dissolve
                p "I'm less interested in 'why' you are or 'how' you are, and a lot more interested in 'what' you are.\n"
                if spectre_possession_ask:
                    voice "audio/voices/ch2/spectre/_encounter/princess/51.flac"
                    show spectre c dismissive talk onlayer front
                    with dissolve
                    p "But we've already been over that. So why don't you stop stalling, and let me in? It's so cold out here...\n"
                else:
                    voice "audio/voices/ch2/spectre/_encounter/princess/52.flac"
                    show spectre c flat talk onlayer front
                    with dissolve
                    p "I've tried to leave on my own. Before you came back to me, I explored every inch of this place, even the spaces between the walls. But I never found a way out. I always wound up right back here.\n"
                    $ spectre_home_comment = True
                    voice "audio/voices/ch2/spectre/_encounter/princess/53.flac"
                    show spectre c homesick talk onlayer front
                    with dissolve
                    p "I just want to go home... I'm so cold and alone here...\n"
                    show spectre c homesick onlayer front
                    with dissolve
                    jump spectre_friendly_possession_join
                show spectre c flat onlayer front
                with dissolve
                if spectre_hostile:
                    jump spectre_menu_hostile
                else:
                    jump spectre_menu_friendly

        "{i}• (Explore) ''You're dead. Or at least mostly dead. What can you even do to hurt me?''{/i}" if spectre_how_hurt_explore == False:
            label spectre_how_hurt:
                $ spectre_how_hurt_explore = True
                if spectre_death_concept_comment == False:
                    voice "audio/voices/ch2/spectre/_encounter/cold/26.flac"
                    show spectre c flat onlayer front
                    with dissolve
                    cold "A boring question with an easy answer. Nothing. She's dead. Dead things can't hurt us.\n"
                else:
                    voice "audio/voices/ch2/spectre/_encounter/cold/27.flac"
                    show spectre c flat onlayer front
                    with dissolve
                    cold "A boring question with an easy answer. Nothing. She's a ghost. Ghosts can't hurt us.\n"
                #voice "audio/voices/ch2/spectre/_encounter/narrator/45.flac"
                #n "The Princess giggles at your question.\n"
                voice "audio/voices/ch2/spectre/_encounter/princess/54.flac"
                show spectre c shrug talk onlayer front
                with dissolve
                p "That's for me to know, and for you to wonder about. Maybe I can't do anything to you.\n"
                voice "audio/voices/ch2/spectre/_encounter/cold/28.flac"
                show spectre c shrug onlayer front
                with dissolve
                cold "See?\n"
                voice "audio/voices/ch2/spectre/_encounter/princess/55.flac"
                play audio "audio/final/Spectre_PossessingPlayer_6.flac"
                show spectre c scary onlayer front
                sp "Or maybe I can rip your heart out.\n"
                voice "audio/voices/ch2/spectre/_encounter/princess/56.flac"
                show spectre c dismissive talk onlayer front
                with dissolve
                p "Who's to say, really?\n"
                voice "audio/voices/ch2/spectre/_encounter/hero/22.flac"
                show spectre c dismissive onlayer front
                with dissolve
                hero "I don't like the uncertainty here. I don't know what to do or who to trust!\n"
                if spectre_hostile:
                    jump spectre_menu_hostile
                else:
                    jump spectre_menu_friendly

        "{i}• (Explore) ''After I killed you, this cabin... I want to say it teleported? It wasn't in the woods anymore, time stopped meaning anything, and I had to kill myself to escape.''{/i}" if spectre_teleport == False:
            $ spectre_death_shared = True
            $ spectre_teleport = True
            voice "audio/voices/ch2/spectre/_encounter/princess/57.flac"
            show spectre c dismissive talk onlayer front
            with dissolve
            p "You poor thing. That must have been so frightening for you.\n"
            voice "audio/voices/ch2/spectre/_encounter/hero/23.flac"
            show spectre c dismissive onlayer front
            with dissolve
            hero "You know, after everything we've been through, it's nice to see someone finally sympathizing with us. This whole thing's been an ordeal, hasn't it?\n"
            voice "audio/voices/ch2/spectre/_encounter/cold/29.flac"
            cold "She doesn't mean it.\n"
            voice "audio/voices/ch2/spectre/_encounter/princess/58.flac"
            show spectre c scary onlayer front
            sp "It serves you right.\n"
            voice "audio/voices/ch2/spectre/_encounter/princess/59.flac"
            show spectre c shrug talk onlayer front
            with dissolve
            p "I was pretty scared, too, when you stood there not saying a word with a knife clenched in your fist. But now you know how bad it hurts to get stabbed in the chest.\n"
            voice "audio/voices/ch2/spectre/_encounter/princess/60.flac"
            play audio "audio/final/Spectre_PossessingPlayer_1.flac"
            show spectre c scary talk onlayer front
            sp "It sounds like you got exactly what you were owed.\n"
            show spectre c flat onlayer front
            with dissolve
            jump spectre_menu_friendly

        "{i}• (Explore) ''Before I agree to anything, we need to talk about what happens after you leave this place. I was told you'd end the world.''{/i}" if spectre_world_end_explore == False and spectre_possession_ask:
            jump spectre_world_end_join

        "{i}• (Explore) ''I guess I should tell you why I was sent to kill you. You were going to end the world.''{/i}" if spectre_world_end_explore == False:
            jump spectre_world_end_join

        "{i}• (Explore) ''I was told you were going to end the world.''{/i}" if spectre_world_end_explore == False:
            label spectre_world_end_join:
                $ spectre_world_end_explore = True
                voice "audio/voices/ch2/spectre/_encounter/princess/61.flac"
                show spectre c shrug talk onlayer front
                with dissolve
                p "And, what? You just believed that? You killed me without giving it any thought? That's cold.\n"
                voice "audio/voices/ch2/spectre/_encounter/hero/24.flac"
                show spectre c smile onlayer front
                with dissolve
                hero "That's rich coming from her. Every time she touches us, it's like we freeze over.\n"
                voice "audio/voices/ch2/spectre/_encounter/cold/30.flac"
                cold "She's right, though. But that's neither here nor there. What's done is done. What we do from this point forward is all that matters. Let's try not to let emotion get the better of us.\n"
                label spectre_world_end_menu:
                    default spectre_world_end_menu_count = 0
                    default spectre_world_end_grovel1 = False
                    default spectre_world_end_grovel2 = False
                    default spectre_world_end_player_wrong = False
                    default spectre_world_end_what_do = False
                    default spectre_world_end_what_did_past= False
                    default spectre_world_end_what_do_follow = False
                    default spectre_world_end_what_do_follow2 = False
                    menu:

                        extend ""

                        "{i}• (Explore) Shit. Everyone sounds disappointed in me. I should grovel even more.{/i}" if spectre_world_end_grovel1 and spectre_world_end_grovel2 == False:
                            $ spectre_world_end_menu_count += 1
                            $ spectre_world_end_grovel2 = True
                            voice "audio/voices/ch2/spectre/_encounter/cold/31.flac"
                            cold "No. You're not doing that.\n"
                            voice "audio/voices/ch2/spectre/_encounter/narrator/46.flac"
                            n "That's right, don't you dare grovel. Mine is the only opinion that matters and I'll never be disappointed in you. So long as you do as I say.\n"
                            jump spectre_world_end_menu

                        "{i}• (Explore) ''Obviously it was wrong of me to believe that. How could you have ended the world if all it took to kill you was a knife to the heart?''{/i}" if spectre_world_end_menu_count == False and spectre_world_end_player_wrong == False:
                            $ spectre_world_end_player_wrong = True
                            $ spectre_world_end_menu_count += 1
                            if spectre_narrator_loop == False:
                                $ spectre_narrator_loop = True
                                voice "audio/voices/ch2/spectre/_encounter/narrator/47.flac"
                                n "So there really was a last time, and you really did manage to slay her. I would have liked to think I was the first, but there's no point living in denial...\n"
                                voice "audio/voices/ch2/spectre/_encounter/hero/25a.flac"
                                hero "The... first?\n"
                                voice "audio/voices/ch2/spectre/_encounter/narrator/48.flac"
                                n "It doesn't matter. The only thing that matters is this:\n"

                            voice "audio/voices/ch2/spectre/_encounter/narrator/49.flac"
                            n "Don't underestimate your own capabilities. If you truly managed to slay her last time, that doesn't mean she wasn't a threat. It means that you did something heroic.\n"
                            voice "audio/voices/ch2/spectre/_encounter/narrator/50.flac"
                            n "Threats come in all shapes and sizes. A misspoken word could bring about the end of everything just as much as a blade or even the mere existence of an idea.\n"
                            voice "audio/voices/ch2/spectre/_encounter/narrator/51.flac"
                            n "You were chosen for this job for a reason.\n"
                            voice "audio/voices/ch2/spectre/_encounter/princess/62.flac"
                            show spectre c dismissive talk onlayer front
                            with dissolve
                            p "That's right, killer. I'm not a threat to anyone. And even if I was, I'm hardly a threat anymore, wouldn't you say?\n"
                            show spectre c dismissive onlayer front
                            with dissolve
                            jump spectre_world_end_menu

                        "{i}• (Explore) ''What are you going to do if I help you get out of here?''{/i}" if spectre_world_end_what_do == False:
                            $ spectre_world_end_what_do = True
                            $ spectre_world_end_menu_count += 1
                            voice "audio/voices/ch2/spectre/_encounter/princess/63.flac"
                            show spectre c shrug talk onlayer front
                            with dissolve
                            p "I dunno. Maybe I'll just fade away, finally able to rest once I'm free from my unfinished business. Maybe I'll find someone to haunt.\n"
                            voice "audio/voices/ch2/spectre/_encounter/princess/64.flac"
                            show spectre c dismissive talk onlayer front
                            with dissolve
                            p "Maybe I'll haunt you.\n"
                            voice "audio/voices/ch2/spectre/_encounter/princess/65.flac"
                            show spectre c flat talk onlayer front
                            with dissolve
                            p "It's a tough question, asking someone what she's going to do with her life.\n"
                            voice "audio/voices/ch2/spectre/_encounter/narrator/52.flac"
                            show spectre c angry onlayer front
                            with Dissolve(0.5)
                            n "The Princess leans in close and pauses, the frigid air between you stale and unmoving.\n"
                            voice "audio/voices/ch2/spectre/_encounter/princess/66.flac"
                            play audio "audio/final/Spectre_PossessingPlayer_7.flac"
                            show spectre c angry talk onlayer front
                            sp "Especially when that someone is dead.\n"
                            voice "audio/voices/ch2/spectre/_encounter/narrator/53.flac"
                            show spectre c coy onlayer front
                            with Dissolve(0.5)
                            n "She pulls back with a playful giggle.\n"
                            voice "audio/voices/ch2/spectre/_encounter/princess/67.flac"
                            show spectre c coy talk onlayer front
                            with dissolve
                            p "I don't think most living people could answer that, either. Does anyone actually know who they are or what they want?\n"
                            show spectre c coy onlayer front
                            with dissolve
                            jump spectre_world_end_menu

                        "{i}• (Explore) ''Well, were you going to end the world?''{/i}" if spectre_world_end_what_did_past == False:
                            $ spectre_world_end_what_did_past = True
                            $ spectre_world_end_menu_count += 1
                            voice "audio/voices/ch2/spectre/_encounter/princess/68.flac"
                            show spectre c shrug talk onlayer front
                            with dissolve
                            p "I don't know. I just wanted to leave. I still just want to leave.\n"
                            show spectre c shrug onlayer front
                            with dissolve
                            jump spectre_world_end_menu

                        "{i}• (Explore) ''You didn't answer my question. Do you want to end the world?''{/i}" if spectre_world_end_what_do_follow == False:
                            $ spectre_world_end_what_do_follow = True
                            $ spectre_world_end_menu_count += 1
                            voice "audio/voices/ch2/spectre/_encounter/princess/69.flac"
                            show spectre c flat talk onlayer front
                            with dissolve
                            p "The only thing I've ever wanted was to leave this place. It's still the only thing I want.\n"
                            show spectre c flat onlayer front
                            with dissolve
                            jump spectre_world_end_menu

                        "{i}• (Explore) ''You still didn't answer my question. Even if you don't {b}want{/b} to end it, does letting you out of here mean the world is going to end?''{/i}" if spectre_world_end_what_do_follow and spectre_world_end_what_do_follow2 == False:
                            $ spectre_world_end_what_do_follow2 = True
                            $ spectre_world_end_menu_count += 1
                            voice "audio/voices/ch2/spectre/_encounter/narrator/54.flac"
                            n "It does.\n"
                            voice "audio/voices/ch2/spectre/_encounter/hero/26.flac"
                            hero "We're not asking you, we've heard your whole speech already.\n"
                            voice "audio/voices/ch2/spectre/_encounter/princess/70.flac"
                            show spectre c flat talk onlayer front
                            with dissolve
                            p "I really, really don't know! I'm not lying to you, I promise.\n"
                            voice "audio/voices/ch2/spectre/_encounter/princess/71.flac"
                            show spectre c homesick talk onlayer front
                            with dissolve
                            p "The world... doesn't matter. All I remember is that I'm supposed to be... there? Not-here? I'm just supposed to be a part of it. It's home, I think.\n"
                            voice "audio/voices/ch2/spectre/_encounter/princess/72.flac"
                            show spectre c thinking talk onlayer front
                            with dissolve
                            p "But what does it mean for anything to end? I ended, but I also didn't.\n"
                            if spectre_death_shared:
                                voice "audio/voices/ch2/spectre/_encounter/princess/73.flac"
                                show spectre c shrug talk onlayer front
                                with dissolve
                                p "And you ended too, but here you are. And you don't even look any different.\n"
                            voice "audio/voices/ch2/spectre/_encounter/princess/74.flac"
                            show spectre c flat talk onlayer front
                            with dissolve
                            p "I'm not so sure endings are real.\n"
                            jump spectre_world_end_menu

                        "{i}• (Explore) ''I'm not cold! I'm just... dumb! I'm just a big dumb stupid idiot! Stupid stupid stupid what was I thinking just believing what I was told?''{/i}" if spectre_world_end_menu_count == 0 and spectre_world_end_grovel1 == False:
                            $ spectre_world_end_grovel1 = True
                            $ spectre_world_end_menu_count += 1
                            voice "audio/voices/ch2/spectre/_encounter/cold/32.flac"
                            show spectre c flat onlayer front
                            cold "Oh, cut it out. You don't need to be so pathetic.\n"
                            if blade_held == False:
                                voice "audio/voices/ch2/spectre/_encounter/princess/75.flac"
                                show spectre c flat talk onlayer front
                                with dissolve
                                p "Nevermind. I don't think I want to see you beg. That's just sad. I shouldn't feel sad about my murderer.\n"
                            else:
                                voice "audio/voices/ch2/spectre/_encounter/princess/76.flac"
                                show spectre c flat talk onlayer front
                                with dissolve
                                p "Eugh. Sure. Did that make you feel better?\n"
                            show spectre c flat onlayer front
                            with dissolve
                            jump spectre_world_end_menu

                        "{i}• (Return) [[Leave it at that.]{/i}":
                            jump spectre_menu_friendly

        "{i}• (Explore) ''Okay, clearly slaying you isn't going to work. What do you want?''{/i}" if spectre_possession_ask == False:
            $ spectre_home_comment = True
            voice "audio/voices/ch2/spectre/_encounter/princess/77.flac"
            show spectre c flat talk onlayer front
            with dissolve
            p "I want what you took from me. A life. A real life. I just want to go home.\n"
            voice "audio/voices/ch2/spectre/_encounter/princess/32.flac"
            show spectre c homesick talk onlayer front
            with dissolve
            p "A way back to where I belong. This place won't let me leave. At least not alone.\n"
            jump spectre_friendly_possession_early_join

        "{i}• (Explore) ''If you can go through walls, can't you just leave on your own?''{/i}" if spectre_walls == False and spectre_home_comment:
            $ spectre_walls = True
            voice "audio/voices/ch2/spectre/_encounter/princess/78.flac"
            show spectre c homesick talk onlayer front
            with dissolve
            p "I wish that's how it worked, but this place won't let me go.\n"
            if spectre_possession_ask == False:
                $ spectre_possession_ask = True
                jump spectre_friendly_possession_early_join
            else:
                show spectre c homesick onlayer front
                with dissolve
                jump spectre_menu_friendly

        "{i}• (Explore) Okay team, I'm out of ideas. Thoughts?{/i}" if spectre_thoughts_explore == False:
            $ spectre_thoughts_explore = True
            voice "audio/voices/ch2/spectre/_encounter/cold/7.flac"
            cold "We could always try violence. It's worked for us so far.\n"
            voice "audio/voices/ch2/spectre/_encounter/hero/3.flac"
            hero "She's a ghost.\n"
            voice "audio/voices/ch2/spectre/_encounter/cold/8.flac"
            cold "Who says ghosts are immune to violence?\n"
            voice "audio/voices/ch2/spectre/_encounter/hero/4.flac"
            hero "... common sense?\n"
            voice "audio/voices/ch2/spectre/_encounter/cold/9.flac"
            cold "There's nothing common or sensible about common sense. Action and observation are the only things that matter.\n"
            voice "audio/voices/ch2/spectre/_encounter/hero/5.flac"
            hero "Fine. Then let me 'observe' that the 'acts' of killing her and killing ourself haven't got us much of anywhere. We're still back in this cabin, and we're still dealing with her, only now she has a good reason to hate us.\n"
            voice "audio/voices/ch2/spectre/_encounter/cold/10.flac"
            cold "I suppose you have a point. Do you have any ideas, then?\n"
            if spectre_possession_ask == False:
                voice "audio/voices/ch2/spectre/_encounter/hero/6.flac"
                hero "We could always ask her what she wants?\n"
                voice "audio/voices/ch2/spectre/_encounter/narrator/14.flac"
                n "Oh, for the love of— Don't do that. Whatever she wants, it will end the world.\n"
            else:
                voice "audio/voices/ch2/spectre/_encounter/hero/7.flac"
                hero "I don't know... maybe we do what she wants. Maybe we let her possess us and walk out of here.\n"
                voice "audio/voices/ch2/spectre/_encounter/cold/11a.flac"
                cold "We could... It would be something different. I like different.\n"
                #voice "audio/voices/ch2/spectre/_encounter/cold/11.flac"
                #cold "I suppose we could. It would be something different. I like different.\n"
                voice "audio/voices/ch2/spectre/_encounter/narrator/15.flac"
                n "Absolutely not! If you walk her out of here, she's going to end the world.\n"
            voice "audio/voices/ch2/spectre/_encounter/cold/12.flac"
            cold "And is that really so bad?\n"
            voice "audio/voices/ch2/spectre/_encounter/narrator/16.flac"
            n "Yes. It is, by its very definition, bad.\n"
            voice "audio/voices/ch2/spectre/_encounter/cold/13.flac"
            cold "But those are the only options, aren't they? Violence, or doing what she wants. Or just leaving her down here. Though ignoring a problem is rarely a solution, isn't it?\n"
            jump spectre_menu_friendly

        "{i}• ''Okay. I've given it enough thought. Let's get you out of here.'' [[Let the Princess possess you.]{/i}" if spectre_possession_ask:
            jump spectre_possession_join

        "{i}• ''Okay. I've given it enough thought. The answer is no. I can't let you out, and I won't let you possess me.''{/i}" if spectre_can_wraith and spectre_possession_ask:
            if wraith_encountered:
                $ spectre_can_wraith = False
                voice "audio/voices/mound/bonus/path.flac"
                mound "This path is already worn by travel and has been seen by one of my many eyes. You cannot walk it again. Change your course.\n"
                voice "audio/voices/ch2/beast/_encounter/hero/31.flac"
                hero "Wait... what?!\n"
                jump spectre_menu_friendly
            voice "audio/voices/ch2/spectre/_encounter/princess/79.flac"
            show spectre c homesick talk onlayer front
            with dissolve
            p "Oh. Is that how it is? That's... sad.\n"
            voice "audio/voices/ch2/spectre/_encounter/princess/80.flac"
            stop music
            show spectre c ask talk onlayer front
            with Dissolve(0.5)
            p "I guess we'll have to fight, then.\n"
            jump spectre_death

        "{i}• ''If you're dead, then there really isn't much for me to do, is there? I guess I'll get going.'' [[Leave her in the basement.]{/i}" if spectre_can_wraith:
            if wraith_encountered:
                $ spectre_can_wraith = False
                voice "audio/voices/mound/bonus/path.flac"
                mound "This path is already worn by travel and has been seen by one of my many eyes. You cannot walk it again. Change your course.\n"
                voice "audio/voices/ch2/beast/_encounter/hero/31.flac"
                hero "Wait... what?!\n"
                jump spectre_menu_friendly
            stop music
            voice "audio/voices/ch2/spectre/_encounter/narrator/55.flac"
            show spectre c flat onlayer front
            with dissolve
            n "This isn't a solution. Nobody wins here.\n"
            label spectre_retrieve_abandon_join:
                $ spectre_end = "abandon"
                default spectre_music_flag = False
                $ spectre_music_flag = True
                stop music
                voice "audio/voices/ch2/spectre/_encounter/princess/81.flac"
                show spectre meltdown 1 onlayer front
                with dissolve
                p "You're... you're...\n"
                voice "audio/voices/ch2/spectre/_encounter/hero/27.flac"
                play music "audio/_music/ch2/spectre/The Spectre II.flac" loop
                hero "Oh... she's upset, isn't she?\n"
                if spectre_blade_retrieve:
                    voice "audio/voices/ch2/spectre/_encounter/princess/82.flac"
                    show spectre meltdown 2 onlayer front
                    with dissolve
                    p "You're going to try and kill me?!\n"
                else:
                    voice "audio/voices/ch2/spectre/_encounter/princess/83.flac"
                    show spectre meltdown 2 onlayer front
                    with dissolve
                    p "You're abandoning me here?!\n"
                voice "audio/voices/ch2/spectre/_encounter/cold/33.flac"
                cold "It would seem so, yes.\n"
                voice "audio/voices/ch2/spectre/_encounter/princess/84.flac"
                play audio "audio/final/Spectre_PossessingPlayer_1.flac"
                show spectre meltdown 3 onlayer front
                with dissolve
                sp "AFTER EVERYTHING YOU'VE DONE TO ME, YOU'VE CHOSEN TO DO MORE?!\n"
                $ gallery_spectre.unlock_item(15)
                if spectre_blade_retrieve:
                    voice "audio/voices/ch2/spectre/_encounter/princess/85.flac"
                    show spectre meltdown 4 onlayer front
                    with dissolve
                    p "But then you either kill me and I get even fuzzier or you don't and... and then I'm really just going to be stuck here forever.\n"
                    voice "audio/voices/ch2/spectre/_encounter/princess/86.flac"
                    show spectre meltdown 5 onlayer front
                    with dissolve
                    p "Th-there's nothing I can do, it's just going to go on and on and on and on, lonely and sad and hurting and empty.\n"
                else:
                    $ spectre_paranoid_override = True
                    voice "audio/voices/ch2/spectre/_encounter/narrator/56.flac"
                    show spectre meltdown 4 onlayer front
                    with dissolve
                    n "The Princess starts to float erratically from side to side, her cold exterior melting away.\n"
                    voice "audio/voices/ch2/spectre/_encounter/princess/87.flac"
                    show spectre meltdown 5 onlayer front
                    with dissolve
                    p "But if you're just leaving me then... then I'm really just going to be stuck here forever. Th-there's nothing I can do, it's just going to go on and on and on and on, lonely and sad and hurting and empty.\n"
                voice "audio/voices/ch2/spectre/_encounter/princess/88.flac"
                show spectre meltdown 6 onlayer front
                with dissolve
                sp "No... NNNNO. NOT THAT.\n"
                voice "audio/voices/ch2/spectre/_encounter/cold/34.flac"
                cold "She's about to try something. Get ready.\n"
                jump spectre_death

        "{i}• ''Right. I don't think there's much more for us to talk about. I'm going to get my blade, and then the two of us can fight.'' [[Retrieve the blade.]{/i}" if spectre_can_wraith and blade_held == False:
            if wraith_encountered:
                $ spectre_can_wraith = False
                voice "audio/voices/mound/bonus/path.flac"
                mound "This path is already worn by travel and has been seen by one of my many eyes. You cannot walk it again. Change your course.\n"
                voice "audio/voices/ch2/beast/_encounter/hero/31.flac"
                hero "Wait... what?!\n"
                jump spectre_menu_friendly
            stop music
            $ spectre_blade_retrieve = True
            voice "audio/voices/ch2/spectre/_encounter/narrator/57.flac"
            show spectre c flat onlayer front
            with dissolve
            n "Excellent idea. I'm glad to hear that you're finally seeing reason.\n"
            jump spectre_retrieve_abandon_join

        "{i}• [[Slay the Princess.]{/i}" if blade_held:
            jump spectre_slay_join

        "{i}• [[Grab the Princess.]{/i}" if blade_held == False:
            jump spectre_grab_join

label spectre_possession_join:

    voice "audio/voices/ch2/spectre/_encounter/narrator/59.flac"
    play audio "audio/final/Spectre_WindPassingThrough_7.flac"
    show spectre possession onlayer front
    with Dissolve(0.5)
    n "The Princess swims through the air in front of you, pausing for a brief moment as her dark-rimmed eyes stare deeply into yours. There's a hunger in her gaze.\n"
    stop music
    if spectre_hostile:
        voice "audio/voices/ch2/spectre/_encounter/princess/89.flac"
        show spectre possession talk onlayer front
        with dissolve
        sp "Thanks for the body, killer.\n"
    else:
        voice "audio/voices/ch2/spectre/_encounter/princess/90.flac"
        show spectre possession talk onlayer front
        with dissolve
        p "You're really trying to make it up to me, aren't you? Thanks for being a pal, killer. I mean it.\n"
    voice "audio/voices/ch2/spectre/_encounter/narrator/58.flac"
    show spectre possession onlayer front
    with dissolve
    n "What are you doing?! Don't just let her in! How many times do I have to tell you... {i}sigh{/i}.\n"

    play audio "audio/final/Spectre_WindPassingThrough_13.flac"
    voice "audio/voices/ch2/spectre/_encounter/princess/91.flac"
    show spectre possession scary talk onlayer front
    sp "See you soon.\n"
    play audio "audio/final/Spectre_PossessingPlayer_7.flac"
    show spectre possession final onlayer front
    with dissolve
    $ renpy.pause(0.25)
    $ gallery_spectre.unlock_item(4)
    $ gallery_spectre.unlock_item(5)
    $ renpy.save_persistent()
    voice "audio/voices/ch2/spectre/_encounter/narrator/60.flac"
    hide spectre onlayer front
    hide bg onlayer back
    hide farback onlayer back
    show farback spectre basement onlayer farback at swayblur, Position(ypos=1125)
    show bg spectre basement onlayer back at swayblur, Position(ypos=1125)
    show spectre possession overlay onlayer front at Position(ypos=1125)
    with dissolve
    n "She rushes forward... and then she's gone. A sharp chill spreads across your body. It starts in your chest, a freezing numbness flowing out from your heart, all the way down your limbs, your mind growing cloudy and confused as it settles over your very soul.\n"
    voice "audio/voices/ch2/spectre/_encounter/hero/28a.flac"
    hero "I'm not sure I like this. Can we get a do-over?\n"
    voice "audio/voices/ch2/spectre/_encounter/narrator/61.flac"
    play audio "audio/final/TheWIld_LightCrackingIceNEW_3.flac"
    hide spectre onlayer front
    hide bg onlayer back
    hide farback onlayer farback
    scene bg black
    with Dissolve(4.0)
    n "I'm afraid it's too late to stop now. The numbness gives way to a stabbing pain, your muscles twitching and convulsing violently, each involuntary movement causing more waves of agony to ripple across your body.\n"
    voice "audio/voices/ch2/spectre/_encounter/narrator/62.flac"
    play audio "audio/one_shot/collapse.flac"
    n "You collapse to the floor, and everything goes dark.\n"

    # BEAT
    play music "audio/_music/ch2/spectre/The Spectre Possession.flac"
    queue music "audio/_music/ch2/spectre/The Spectre Possession Loop.flac" loop
    if spectre_hostile:
        voice "audio/voices/ch2/spectre/_encounter/princess/92.flac"
        pmid "Get up. You've still got a job to do.\n"
    else:
        voice "audio/voices/ch2/spectre/_encounter/princess/93.flac"
        pmid "Come on, you. You've gotta get up. I know everything feels... heavy right now, but we still have to get out of here.\n"
    # FAST

    play audio "audio/final/Nightmare_MaleBreath_1.flac"
    voice "audio/voices/ch2/spectre/_encounter/narrator/63.flac"
    scene bg spectre heart stairs onlayer back at swayblur, Position(ypos=1125)
    show spectre possession overlay onlayer inyourface at swayblur, Position(ypos=1125)
    with Dissolve(1.0)
    n "Your eyes flick back open as you get your bearings, your vision swimming as—\n{w=4.15}{nw}"
    show screen disableclick(0.5)
    voice "audio/voices/ch2/spectre/_encounter/princess/94.flac"
    hide bg onlayer back
    hide spectre onlayer inyourface
    show bg spectre heart stairs onlayer back at Position(ypos=1125)
    show spectre possession overlay onlayer inyourface at Position(ypos=1125)
    with Dissolve(1.0)
    pmid "So this is what it's like to be you, huh? Disembodied voice narrating your every move?\n"
    voice "audio/voices/ch2/spectre/_encounter/hero/29.flac"
    hero "So... it doesn't work like that for you?\n"
    voice "audio/voices/ch2/spectre/_encounter/cold/35.flac"
    cold "Clearly it doesn't, or she wouldn't have commented on it.\n"
    if spectre_hostile:
        voice "audio/voices/ch2/spectre/_encounter/princess/96a.flac"
    else:
        voice "audio/voices/ch2/spectre/_encounter/princess/96.flac"
    pmid "All these shards of broken glass on the floor... are they also supposed to be you?\n"
    voice "audio/voices/ch2/spectre/_encounter/hero/30.flac"
    hero "Hey! I'm not a shard of broken glass, I'm...\n"
    if spectre_hostile:
        voice "audio/voices/ch2/spectre/_encounter/princess/97.flac"
        pmid "Yeah? Go on. Finish the thought. What are you?\n"
    else:
        voice "audio/voices/ch2/spectre/_encounter/princess/98.flac"
        pmid "It's okay. You can finish your thought.\n"
    voice "audio/voices/ch2/spectre/_encounter/hero/31.flac"
    hero "I'm... a voice? I'm me, is what I am.\n"
    voice "audio/voices/ch2/spectre/_encounter/cold/36.flac"
    cold "Who cares what we are? We exist. That's all that matters.\n"
    if spectre_hostile:
        voice "audio/voices/ch2/spectre/_encounter/princess/99.flac"
        pmid "Do you have to deal with this annoying bickering all the time?\n"
    else:
        voice "audio/voices/ch2/spectre/_encounter/princess/100.flac"
        pmid "You don't have to fight. We'll all be out of here soon.\n"
    voice "audio/voices/ch2/spectre/_encounter/hero/32.flac"
    hero "No, it matters! What we are matters! If I'm a 'shard of broken glass' then that raises some questions about certain other 'voices' in here, too.\n"
    voice "audio/voices/ch2/spectre/_encounter/cold/37.flac"
    cold "I'm clearly the same thing you are.\n"
    if spectre_hostile:
        voice "audio/voices/ch2/spectre/_encounter/princess/101.flac"
        pmid "Hopefully they'll all go away once we leave this place. I don't know how you can tolerate all of this noise.\n"
    else:
        voice "audio/voices/ch2/spectre/_encounter/princess/102.flac"
        pmid "They're not listening to me. Do they not listen to you, either?\n"
    voice "audio/voices/ch2/spectre/_encounter/hero/33.flac"
    hero "No I'm not talking about you, I'm talking about Him.\n"
    voice "audio/voices/ch2/spectre/_encounter/narrator/64.flac"
    n "You don't need to know what I am. You just need to know that I'm different from you. More important.\n"
    if spectre_hostile:
        voice "audio/voices/ch2/spectre/_encounter/princess/103a.flac"
    else:
        voice "audio/voices/ch2/spectre/_encounter/princess/103.flac"
    pmid "So you're the one who pulled the strings and made me dead. I can tell you don't belong here. You're barely even there, like the shape of something left behind. You're more of a... memory than a person.\n"
    voice "audio/voices/ch2/spectre/_encounter/narrator/65.flac"
    n "That's rude.\n"
    if spectre_hostile:
        voice "audio/voices/ch2/spectre/_encounter/princess/104a.flac"
    else:
        voice "audio/voices/ch2/spectre/_encounter/princess/104.flac"
    pmid "You're kind of like me, actually.\n"
    voice "audio/voices/ch2/spectre/_encounter/narrator/66.flac"
    n "I'm just going to ignore her. You push yourself off the ground. The Princess is nowhere to be seen—\n{w=5.5}{nw}"
    show screen disableclick(0.5)
    voice "audio/voices/ch2/spectre/_encounter/cold/38.flac"
    cold "Obviously she's nowhere to be seen.\n"
    if spectre_hostile:
        voice "audio/voices/ch2/spectre/_encounter/princess/105a.flac"
    else:
        voice "audio/voices/ch2/spectre/_encounter/princess/105.flac"
    pmid "Because I'm in here with all of you. Everybody knows that.\n"
    voice "audio/voices/ch2/spectre/_encounter/narrator/67.flac"
    n "I'm setting the stage. The room is empty, because you made a spiteful, idiotic, and all around foolish decision.\n"
    if spectre_hostile:
        voice "audio/voices/ch2/spectre/_encounter/princess/106.flac"
        spmid "Oh, shut up! Stop trying to manipulate everyone.\n"
        voice "audio/voices/ch2/spectre/_encounter/princess/107.flac"
        pmid "Or don't, actually. It doesn't really matter, because you won't be around to do this for much longer.\n"
    else:
        voice "audio/voices/ch2/spectre/_encounter/princess/108.flac"
        pmid "You don't have to let him get to you. You're better than that. You're starting to make things right.\n"
    voice "audio/voices/ch2/spectre/_encounter/narrator/68.flac"
    n "{i}Sigh{/i}. This is infuriating. Just... whatever you do, you can't leave this place. It's not too late to fix this. Probably.\n"
    label spectre_possession_menu:
        default spectre_possession_menu_explore = False
        menu:
            extend ""

            "{i}• (Explore) I can't think straight... there's too much noise.{/i}" if spectre_possession_menu_explore == False:
                $ spectre_possession_menu_explore = True
                if spectre_hostile:
                    voice "audio/voices/ch2/spectre/_encounter/princess/109.flac"
                    spmid "Then don't think. Just. Move.\n"
                else:
                    voice "audio/voices/ch2/spectre/_encounter/princess/110.flac"
                    pmid "It's okay, we're almost out of here. Just take it one step at a time, and everything will be fine.\n"
                    voice "audio/voices/ch2/spectre/_encounter/narrator/69.flac"
                    n "Everything won't be fine if you listen to {b}her{/b}.\n"
                #voice "audio/voices/ch2/spectre/_encounter/hero/34.flac"
                #hero "Look, we've come this far, I say it's worth a try.\n"
                voice "audio/voices/ch2/spectre/_encounter/cold/39.flac"
                cold "One way or another, this is all going to end. Wouldn't it be nice if He ends with it?\n"
                if spectre_hostile:
                    voice "audio/voices/ch2/spectre/_encounter/princess/111.flac"
                    pmid "I guess we'll just have to see what happens when we leave. But if I'm stuck in here, I'll be making some renovations. It's too crowded.\n"
                else:
                    voice "audio/voices/ch2/spectre/_encounter/princess/112.flac"
                    pmid "Wouldn't that be nice? There's only one way to find out.\n"
                jump spectre_possession_menu

            "{i}• [[Slay the Princess.]{/i}" if blade_held:
                jump spectre_self_slay_join

            "{i}• [[Leave the basement.]{/i}":
                jump spectre_free_start

label spectre_self_slay_join:

    stop music
    voice "audio/voices/ch2/spectre/_encounter/cold/40.flac"
    cold "Isn't that an interesting idea.\n"
    voice "audio/voices/ch2/spectre/_encounter/narrator/70.flac"
    n "I... hadn't even considered it as an option. Slaying her would slay you. Are you sure you're willing to do that?\n"
    voice "audio/voices/ch2/spectre/_encounter/hero/35.flac"
    hero "Of course we're sure. The decision has already been made.\n"
    voice "audio/voices/ch2/spectre/_encounter/narrator/71.flac"
    n "All right, then. Better this than ferrying her out of here.\n"
    #voice "audio/voices/ch2/spectre/_encounter/princess/113.flac"
    #spmid "Wh-what do you think you're doing?!\n"
    if spectre_hostile:
        voice "audio/voices/ch2/spectre/_encounter/princess/113.flac"
        spmid "Wh-what do you think you're doing?!\n"
    else:
        voice "audio/_pristine/voice/extras/spectre_princess/s1.flac"
        pmid "After all that, you're really just going to stab me again?!\n"
    voice "audio/voices/ch2/spectre/_encounter/cold/41.flac"
    cold "Hear that? She's scared. No point in wasting more time. Do it.\n"
    voice "audio/voices/ch2/spectre/_encounter/narrator/72.flac"
    play music "audio/_music/ch2/spectre/The Spectre Death.flac" loop
    play secondary "audio/one_shot/knife_pickup.flac"
    queue secondary "audio/final/Tower_KnifeBlow_3.flac"
    show player self end onlayer front at Position(ypos=1125)
    with dissolve
    $ renpy.pause(0.5)
    voice sustain
    $ blade_held = False
    $ default_mouse = "blood"
    show player spectre exorcism 1 onlayer front
    with dissolve
    $ renpy.pause(0.25)
    voice sustain
    n "You lift the blade, then plunge it deep into your guts. Pain spreads quickly through your torso as you attempt to turn its edge up towards your heart.\n"
    # PRISTINE CUT BEGINS
    jump spectre_pristine_start

    # OLD EXORCISM ENDING
    play audio "audio/final/Spectre_PossessingPlayer_1.flac"
    voice "audio/voices/ch2/spectre/_encounter/princess/114.flac"
    spmid "NO!\n"
    #if spectre_hostile:
        #voice "audio/voices/ch2/spectre/_encounter/princess/114.flac"
        #spmid "NO!\n"
    #else:
    #    voice "audio/_pristine/voice/extras/spectre_princess/s_why.flac"
    #    pmid "Why? Why would you do that?\n"

    voice "audio/voices/ch2/spectre/_encounter/narrator/73.flac"
    play tertiary "audio/final/Spectre_PossessingPlayer_7.flac"
    play audio "audio/final/Adversary_StabCut_1.flac"
    n "The Princess, her spirit bound to your prison of flesh as she had once been bound to the basement's prison of stone, cries out in agony as you slice through organ and muscle.\n"
    voice "audio/voices/ch2/spectre/_encounter/narrator/74.flac"
    play audio "audio/final/Spectre_PossessingPlayer_7.flac"
    show player spectre exorcism 2 onlayer front
    with dissolve
    n "Your skin roils and bucks as she violently pushes against it from the inside. Bits of her seep through, white and glowing with ethereal light, but still the walls of your prison hold.\n"
    voice "audio/voices/ch2/spectre/_encounter/princess/115.flac"
    spmid "Is this really what you wanted? Do you hate me so much that you would kill yourself just to deny me freedom?\n"
    voice "audio/voices/ch2/spectre/_encounter/narrator/75.flac"
    n "Yes, he would. Because he knows what's at stake, and he knows what will happen if you leave this place.\n"
    voice "audio/voices/ch2/spectre/_encounter/hero/36.flac"
    hero "I'm not so sure about all of that...\n"
    voice "audio/voices/ch2/spectre/_encounter/narrator/76.flac"
    n "Don't be modest. You're a hero.\n"
    voice "audio/voices/ch2/spectre/_encounter/princess/116.flac"
    play audio "audio/one_shot/hard tighten.flac"
    show player spectre exorcism 3 onlayer front
    with Dissolve(0.5)
    spmid "Do you think I'm just going to stick around while you die? Hell, no! I'm leaving!\n"
    voice "audio/voices/ch2/spectre/_encounter/cold/42.flac"
    cold "You can try if you want. But I think this is an end for all of us.\n"
    play audio "audio/final/Adversary_PowerfulFingersDiggingSkull_2.flac"
    voice "audio/voices/ch2/spectre/_encounter/princess/117.flac"
    show player spectre exorcism 4 onlayer front
    with Dissolve(0.5)
    spmid "LET ME OUT LET ME OUT LET ME OUT!\n"
    voice "audio/voices/ch2/spectre/_encounter/narrator/77.flac"
    n "The Princess' form continues struggling to pull itself out of you, but the effort is in vain.\n"
    $ achievement.grant("ACH_SPECTRE_EXORCIST")
    stop music
    voice "audio/voices/ch2/spectre/_encounter/narrator/78.flac"
    play audio "audio/one_shot/collapse.flac"
    play secondary "audio/final/Nightmare_MaleBreath_1.flac"
    stop music fadeout 15.0
    stop sound fadeout 20.0
    stop tertiary fadeout 20.0
    play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 15.0
    hide player onlayer front
    hide table onlayer back
    hide farback onlayer farback
    hide bg onlayer back
    hide farback onlayer back
    hide spectre onlayer inyourface
    scene bg black
    $ renpy.pause(0.5)
    voice sustain
    show bg spectre exorcism collapse onlayer back at swayblur, Position(ypos=1125)
    show spectre exorcism collapse overlay onlayer inyourface at Position(ypos=1125)
    with Dissolve(1.0)
    n "You collapse to your knees. Your vision blurs, then starts to fade.\n"
    voice "audio/voices/ch2/spectre/_encounter/hero/37.flac"
    hide bg onlayer back
    hide spectre onlayer inyourface
    show farback quiet onlayer farback at Position(ypos=1125)
    show player spectre post exorcism onlayer back at Position(ypos=1125)
    with Dissolve(2.0)
    hero "And then what happens?\n"
    voice "audio/voices/ch2/spectre/_encounter/cold/43.flac"
    cold "I think he's gone. Just like everything else.\n"
    voice "audio/voices/ch2/spectre/_encounter/hero/38.flac"
    hero "Are we dead?\n"
    voice "audio/voices/ch2/spectre/_encounter/cold/44.flac"
    cold "I don't know. I don't think so. This is different than it was last time.\n"
    play audio "audio/final/Adversary_StabCut_8.flac"
    show spectre post exorcism tear onlayer back at Position(ypos=1125)
    show overlay spectre post exorcism onlayer front at Position(ypos=1125)
    with Dissolve(1.0)
    $ renpy.pause(0.5)
    hide overlay onlayer front
    hide player onlayer back
    hide spectre onlayer back
    show spectre post exorcism crawl onlayer front at Position(ypos=1125)
    show player spectre post exorcism onlayer front at Position(ypos=1125)
    with Dissolve(1.0)
    truth "As the voices in your head debate amongst themselves, the form of the Princess crawls from your body and into the vast nothing surrounding you.\n"
    voice "audio/voices/ch2/spectre/_encounter/princess/118.flac"
    show spectre post exorcism talk scary onlayer front
    sp "Do you think we're done?\n"
    voice "audio/voices/ch2/spectre/_encounter/princess/119.flac"
    show spectre post exorcism talk cold onlayer front
    p "Do you...\n"
    play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
    show arms s exorcism1 onlayer back at Position(ypos=1125)
    with Dissolve(0.75)
    $ renpy.pause(0.25)
    show spectre post exorcism quiet onlayer front at Position(ypos=1125)
    show arms s exorcism2 onlayer back at Position(ypos=1125)
    with Dissolve(0.75)
    $ renpy.pause(0.125)
    hide spectre onlayer front
    show arms s exorcism3 onlayer back at Position(ypos=1125)
    with Dissolve(0.5)
    $ renpy.pause(0.125)
    show arms s exorcism4 onlayer back at Position(ypos=1125)
    with Dissolve(0.5)
    $ renpy.pause(0.125)
    hide arms onlayer back
    with Dissolve(0.5)
    $ blade_held = False
    $ default_mouse = "default"
    hide player onlayer front
    hide fore onlayer front
    hide fore onlayer inyourface
    hide farback onlayer farback
    hide bg onlayer back
    hide mid onlayer back
    hide stars onlayer farback
    hide bg onlayer back
    hide quiet onlayer back
    show farback quiet onlayer farback at Position(ypos=1125)
    with Dissolve(4.0)
    show mirror quiet distant onlayer back at Position(ypos=1125)
    if loops_finished != 0:
        truth "But you do not get the chance to respond, nor will you ever. It's time to leave. Memory returns.\n"
    else:
        truth "But you do not get the chance to respond. Something has taken her away, and it's left something else in her stead.\n"
    $ spectre_end = "slay"
    $ princess_kept += 1
    $ princess_deny += 1
    jump mirror_start
    # ending

label spectre_free_start:

    default spectre_upstairs = False
    $ spectre_upstairs = True

    voice "audio/voices/ch2/spectre/_encounter/narrator/79.flac"
    play audio "audio/one_shot/footsteps_creaky.flac"
    hide bg onlayer back
    hide spectre onlayer inyourface
    show bg spectre possessed stairs onlayer back at Position(ypos=1125)
    show spectre possession overlay onlayer inyourface at Position(ypos=1125)
    with Dissolve(1.0)
    n "{i}Sigh.{/i} Your legs weary with the weight of the Princess' spectral form, and clumsy with the cold that still pervades them, stumble towards the stairs.\n"
    if spectre_hostile:
        voice "audio/voices/ch2/spectre/_encounter/princess/120a.flac"
    else:
        voice "audio/voices/ch2/spectre/_encounter/princess/120.flac"
    pmid "I'm just trying to get home. You don't have to act like it's the end of the world.\n"
    voice "audio/voices/ch2/spectre/_encounter/narrator/80.flac"
    n "But that's exactly what you leaving this place is going to be.\n"
    if spectre_hostile:
        voice "audio/voices/ch2/spectre/_encounter/princess/121a.flac"
    else:
        voice "audio/voices/ch2/spectre/_encounter/princess/121.flac"
    pmid "You don't know that!\n"
    voice "audio/voices/ch2/spectre/_encounter/narrator/81.flac"
    n "I do.\n"
    voice "audio/voices/ch2/spectre/_encounter/hero/39.flac"
    hero "Wait. If she has a home to go back to, doesn't that mean that her leaving won't end the world?\n" id spectre_free_start_5129ef76
    voice "audio/voices/ch2/spectre/_encounter/cold/45.flac"
    cold "It doesn't mean that at all. It could mean that wherever her home is, it's outside of the world.\n"
    voice "audio/voices/ch2/spectre/_encounter/hero/40.flac"
    hero "Yeah, but it has to be somewhere, doesn't it? And if it's somewhere, then it's part of the world.\n"
    voice "audio/voices/ch2/spectre/_encounter/cold/46.flac"
    cold "I suppose it's all a matter of perspective — where does the world end and something else begin? Does the destruction of one open a door to another, or is it the same world, reborn?\n"
    voice "audio/voices/ch2/spectre/_encounter/narrator/82.flac"
    play audio "audio/one_shot/footsteps_creaky.flac"
    hide bg onlayer back
    hide spectre onlayerinyourface
    scene farback spectre possessed upstairs onlayer farback at Position(ypos=1125)
    show bg spectre possessed upstairs onlayer back at Position(ypos=1125)
    show table spectre possessed upstairs onlayer back at Position(ypos=1125)
    if blade_held == False:
        show knife spectre possessed upstairs onlayer back at Position(ypos=1125)
    with Dissolve(1.0)
    n "Against the backdrop of the inane conjecture of meaningless little voices, your body continues its ascent up the stairs, staggering through the open door.\n"
    voice "audio/voices/ch2/spectre/_encounter/cold/47.flac"
    cold "For how much you hate her, you aren't doing a whole lot to stop us from leaving this place.\n"
    if spectre_hostile:
        voice "audio/voices/ch2/spectre/_encounter/princess/122.flac"
        pmid "It's because He can't stop me. Why do you think He sent you here?\n"
        voice "audio/voices/ch2/spectre/_encounter/narrator/83.flac"
        n "I hate to admit it, but she's not wrong.\n"
    else:
        voice "audio/voices/ch2/spectre/_encounter/princess/123.flac"
        pmid "Maybe the bossy one doesn't actually hate me. Maybe He even likes me! Or... maybe He just knows that He's been in the wrong. Maybe He's trying to make amends, too.\n"
        voice "audio/voices/ch2/spectre/_encounter/narrator/84.flac"
        n "Not at all. I'll have you know that I do hate you, and I will continue to hate you for as long as I am able.\n"
    voice "audio/voices/ch2/spectre/_encounter/narrator/85.flac"
    n "It's just the weight of it all... it's too much for me to do anything other than describe and dictate.\n"
    voice "audio/voices/ch2/spectre/_encounter/cold/48.flac"
    cold "And whine.\n"
    voice "audio/voices/ch2/spectre/_encounter/narrator/86.flac"
    n "This body wasn't made to hold you and the Princess. If you want to renege on your cataclysmically terrible decision a minute ago, well, you're the only one who can make that happen.\n"
    label spectre_leaving_menu:
        menu:
            extend ""

            "{i}• (Explore) [[Take the blade.]{/i}" if blade_held == False:
                voice "audio/voices/ch2/spectre/_encounter/narrator/87.flac"
                $ blade_held = True
                $ default_mouse = "blade"
                play audio "audio/one_shot/knife_pickup.flac"
                hide knife onlayer back with dissolve
                n "You reach forward and mindlessly take the blade from the table. What do you plan to do with it?\n"
                jump spectre_leaving_menu

            "{i}• [[Slay the Princess.]{/i}" if blade_held and spectre_1_cabin_blade_taken == False:
                jump spectre_self_slay_join

            "{i}• [[Trudge forward.]{/i}":
                play audio "audio/one_shot/footsteps_creaky.flac"
                hide bg onlayer back
                hide farback onlayer farback
                hide table onlayer back
                hide knife onlayer back
                scene bg spectre possessed upstairs door onlayer back at Position(ypos=1125)
                with Dissolve(1.0)
                if blade_held and spectre_1_cabin_blade_taken == False:
                    voice "audio/voices/ch2/spectre/_encounter/narrator/88.flac"
                    n "Blade in hand, you continue slowly to the door, your feet like lead dragging across the floorboards, growing heavier with each step.\n"
                else:
                    voice "audio/voices/ch2/spectre/_encounter/narrator/89.flac"
                    n "You continue slowly to the door, your feet like lead dragging across the floorboards, growing heavier with each step.\n"
                if spectre_hostile:
                    voice "audio/voices/ch2/spectre/_encounter/princess/124.flac"
                    spmid "Finally! FINALLY!\n"
                else:
                    voice "audio/voices/ch2/spectre/_encounter/princess/125.flac"
                    pmid "We're so close. Thank you, thank you, thank you! If we get out of here I won't even care that you murdered me anymore!\n"
                voice "audio/voices/ch2/spectre/_encounter/narrator/90.flac"
                play audio "audio/one_shot/thump.flac"
                show player spectre possessed door onlayer back at Position(ypos=1125)
                with Dissolve(1.0)
                n "You lift your shaking hand and rest it on the door handle, but you pause before you open it, exhaustion sapping what's left of your will.\n"
                voice "audio/voices/ch2/spectre/_encounter/cold/49.flac"
                cold "Was exhaustion really the best you could muster up? It's over. There's no use stalling. Let's see what happens next.\n"
                menu:
                    extend ""

                    "{i}• [[Open the door.]{/i}":
                        voice "audio/voices/ch2/spectre/_encounter/narrator/91.flac"
                        play audio "audio/one_shot/door_bedroom.flac"
                        stop music fadeout 15.0
                        stop sound fadeout 20.0
                        stop tertiary fadeout 20.0
                        play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 15.0
                        hide bg onlayer back
                        hide player onlayer back
                        hide spectre onlayer inyourface
                        scene bg black
                        with fade
                        n "Shit. But exhaustion wasn't enough, was it? The handle clicks as you twist it, and then the door groans open.\n"
                        voice "audio/voices/ch2/spectre/_encounter/narrator/92a.flac"
                        play audio "audio/one_shot/collapse.flac"
                        n "You collapse to the ground, you and the Princess free from the confines of the cabin. As you exhale from the effort, you look up and see...\n"
                        voice "audio/voices/ch2/spectre/_encounter/hero/41.flac"
                        show farback quiet onlayer farback at Position(ypos=1125)
                        show spectre possession overlay onlayer inyourface at Position(ypos=1125)
                        with fade
                        hero "Er, yes?\n"
                        if spectre_hostile:
                            voice "audio/voices/ch2/spectre/_encounter/princess/126a.flac"
                        else:
                            voice "audio/voices/ch2/spectre/_encounter/princess/126.flac"
                        pmid "Nothing. He's gone. And so is everything else.\n"
                        voice "audio/voices/ch2/spectre/_encounter/cold/50.flac"
                        cold "So we did slay him after all. He had it coming, I suppose.\n"
                        voice "audio/voices/ch2/spectre/_encounter/hero/42.flac"
                        hero "But what about {i}us{/i}? Are we just stuck here in... nowhere forever? Did taking her out of the cabin really end the world?\n"
                        voice "audio/voices/ch2/spectre/_encounter/cold/51.flac"
                        cold "We're still here.\n"
                        voice "audio/voices/ch2/spectre/_encounter/hero/43.flac"
                        hero "Yeah, but, that thing you said earlier... are we not part of the world anymore? Are we in some world that exists after the world ends, or on top of the other world but not in it, or...? Have we never been part of the world?\n"
                        if spectre_hostile:
                            voice "audio/voices/ch2/spectre/_encounter/princess/127a.flac"
                            pmid "All right. Let's see if I'm stuck with you forever.\n"
                        else:
                            voice "audio/voices/ch2/spectre/_encounter/princess/128.flac"
                            pmid "Okay, I've heard enough from these two. Let's see if I can pop out.\n"
                        $ gallery_spectre.unlock_item(6)
                        $ gallery_spectre.unlock_item(7)
                        $ gallery_spectre.unlock_item(8)
                        $ renpy.save_persistent()
                        $ achievement.grant("ACH_SPECTRE_HITCH")
                        play audio "audio/final/Spectre_PossessingPlayer_7.flac"
                        hide spectre onlayer inyourface
                        show spectre outside onlayer front at Position(ypos=1125)
                        with Dissolve(1.0)
                        $ renpy.pause(0.5)
                        show spectre outside look onlayer front
                        with Dissolve(0.5)
                        truth "You feel a lightness in your chest as a pair of sunken eyes emerge from your body and stare up at you.\n"
                        if spectre_hostile:
                            voice "audio/voices/ch2/spectre/_encounter/princess/129.flac"
                            show spectre outside look talk onlayer front
                            with dissolve
                            p "Guess I'm not! All's well that ends well, right? You lived up to your end of the bargain, so I'll live up to mine. Thanks.\n"
                        else:
                            voice "audio/voices/ch2/spectre/_encounter/princess/130.flac"
                            show spectre outside look talk onlayer front
                            with dissolve
                            p "I'm out! You actually freed me, didn't you? I'm... outside. Thanks for giving me a second chance, killer.\n"
                        voice "audio/voices/ch2/spectre/_encounter/hero/44.flac"
                        hero "Don't mention it.\n"
                        if spectre_hostile:
                            voice "audio/voices/ch2/spectre/_encounter/princess/131a.flac"
                        else:
                            voice "audio/voices/ch2/spectre/_encounter/princess/131.flac"
                        show spectre outside cold onlayer front
                        with dissolve
                        p "I think... this is where I'm meant to be...\n"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show arms s outside1 onlayer back at Position(ypos=1125)
                        show spectre outside quiet onlayer front at Position(ypos=1125)
                        with Dissolve(1.0)
                        $ renpy.pause(0.25)
                        hide spectre onlayer front
                        show arms s outside3 onlayer back at Position(ypos=1125)
                        with Dissolve(1.0)
                        $ renpy.pause(0.125)
                        show arms s outside4 onlayer back at Position(ypos=1125)
                        with Dissolve(0.5)
                        $ renpy.pause(0.125)
                        hide arms onlayer back
                        with Dissolve(0.5)
                        $ blade_held = False
                        $ default_mouse = "default"
                        hide player onlayer front
                        hide fore onlayer front
                        hide fore onlayer inyourface
                        hide farback onlayer farback
                        hide bg onlayer back
                        hide mid onlayer back
                        hide stars onlayer farback
                        hide bg onlayer back
                        hide quiet onlayer back
                        show farback quiet onlayer farback at Position(ypos=1125)
                        with Dissolve(4.0)
                        show mirror quiet distant onlayer back at Position(ypos=1125)
                        if loops_finished != 0:
                            truth "You don't get the chance to respond, nor will you ever. It's time to leave. Memory returns.\n"
                        else:
                            truth "But you don't get the chance to respond. Something has taken her away, and it's left something else in her stead.\n"
                        $ spectre_end = "free"
                        $ princess_free += 1
                        $ princess_satisfy += 1
                        jump mirror_start
                        # ending

label spectre_death:

    voice "audio/voices/ch2/spectre/_encounter/narrator/93.flac"
    play audio "audio/final/Spectre_PossessingPlayer_7.flac"
    show spectre heart woosh onlayer front
    with dissolve
    n "The Princess passes through you, a chill rippling along your skin, a disappointed sigh echoing in your ears.\n"
    voice "audio/voices/ch2/spectre/_encounter/narrator/94.flac"
    play audio "audio/one_shot/footsteps_creaky.flac"
    hide spectre onlayer front
    hide bg onlayer back
    hide farback onlayer farback
    hide farback onlayer back
    scene bg spectre heart stairs onlayer back at Position(ypos=1125)
    show spectre heart stairs onlayer front at Position(ypos=1125)
    with Dissolve(1.0)
    n "You turn and face her as she hovers between you and the stairs.\n"
    voice "audio/voices/ch2/spectre/_encounter/narrator/95.flac"
    play audio "audio/final/Spectre_PossessingPlayer_5.flac"
    show spectre heart cry touch onlayer front
    with Dissolve(0.5)
    n "Spectral tears streak down her cheeks as she places a translucent hand on your chest. It feels cold, but otherwise like nothing at all.\n"
    voice "audio/voices/ch2/spectre/_encounter/hero/45.flac"
    hero "Are we doing the right thing? Why do I feel so sad?\n"
    voice "audio/voices/ch2/spectre/_encounter/cold/52.flac"
    cold "Don't let her get to you. It doesn't matter. Somehow, soon, this too will be over, and we'll move on to something new. I feel like you all keep forgetting that.\n"
    voice "audio/voices/ch2/spectre/_encounter/narrator/96.flac"
    show spectre heart eyes fall onlayer front
    with dissolve
    n "Her dark-rimmed eyes fall to the floor as she speaks.\n"
    voice "audio/voices/ch2/spectre/_encounter/princess/132.flac"
    show spectre heart eyes fall talk onlayer front
    with dissolve
    p "I never wanted to have to hurt anybody. It's not who I wanted to be.\n"
    voice "audio/voices/ch2/spectre/_encounter/narrator/97.flac"
    show spectre heart evil look onlayer front
    with dissolve
    n "The tears on her cheeks vanish. She lifts her head, sorrow replaced with wrath, staring into you with fiery anger.\n"
    #if spectre_music_flag == False:
    #    play music "audio/_music/ch2/spectre/The Spectre II.flac" loop
    voice "audio/voices/ch2/spectre/_encounter/princess/133.flac"
    play audio "audio/final/Spectre_PossessingPlayer_2.flac"
    show spectre heart evil look talk onlayer front
    sp "But I guess you've turned me into something worse.\n"
    jump spectre_kill_player

label spectre_kill_player:
    default spectre_kill_player_slay_attempt = False
    stop music
    voice "audio/voices/ch2/spectre/_encounter/narrator/98.flac"
    play audio "audio/final/Spectre_WindPassingThrough_13.flac"
    show spectre heart force onlayer front
    with dissolve
    n "She forces her hand into your chest and then...\n"
    voice "audio/voices/ch2/spectre/_encounter/cold/53.flac"
    cold "Yes?\n"
    voice "audio/voices/ch2/spectre/_encounter/narrator/99.flac"
    n "Nothing happens.\n"
    voice "audio/voices/ch2/spectre/_encounter/hero/46.flac"
    hero "Are you sure about that? S-something should have happened...\n"
    voice "audio/voices/ch2/spectre/_encounter/cold/54.flac"
    cold "And yet it didn't. We're fine.\n"
    menu:
        extend ""

        "{i}• ''Did you miss?''{/i}":
            voice "audio/voices/ch2/spectre/_encounter/princess/134a.flac"
            play audio "audio/final/Spectre_PossessingPlayer_4.flac"
            show spectre heart squelch onlayer front
            sp "No.\n"
            label spectre_kill_player_join:
                stop music
                voice "audio/voices/ch2/spectre/_encounter/narrator/100.flac"
                show spectre heart squelch onlayer front
                n "You can't be sure if you first hear or feel what happens next, but it is over before you can fully conceptualize what 'it' is.\n"
                play music "audio/_music/ch2/spectre/The Spectre Death.flac" loop
                voice "audio/voices/ch2/spectre/_encounter/narrator/101.flac"
                play audio "audio/final/Spectre_HeartCrush_2 copy.flac"
                show spectre heart squelch onlayer front with hpunch
                n "A horrific splintering, the squelching of organs, the rending of tissue. An icy, numbing pain.\n"
                voice "audio/voices/ch2/spectre/_encounter/princess/135.flac"
                show spectre heart squelch talk onlayer front
                sp "I'm done asking. The next time I see you, I'm taking everything I'm owed. Starting with your body. If you won't choose to give me my freedom, I'll just have to make you give it to me.\n"
                if blade_held:
                    voice "audio/voices/ch2/spectre/_encounter/cold/55.flac"
                    show spectre heart force onlayer front
                    with dissolve
                    cold "She's real now. If she's making us dead, we should return the favor.\n"
                    menu:
                        extend ""

                        "{i}• [[Slay the Princess.]{/i}":
                            $ spectre_kill_player_slay_attempt = True
                            voice "audio/voices/ch2/spectre/_encounter/narrator/105.flac"
                            play audio "audio/final/Spectre_WindPassingThrough_13.flac"
                            show spectre heart slash onlayer front
                            with Dissolve(1.0)
                            n "You swing your blade towards her briefly corporeal throat. It connects. A gash widens across her neck, glowing ectoplasm leaking from the wound.\n"
                            voice "audio/voices/ch2/spectre/_encounter/narrator/106.flac"
                            $ gallery_spectre.unlock_item(9)
                            $ gallery_spectre.unlock_item(10)
                            $ renpy.save_persistent()
                            $ achievement.grant("ACH_SPECTRE_HEART")
                            play audio "audio/final/Adversary_HandThroughChest_2.flac"
                            play secondary "audio/final/Nightmare_HeartBeat_3.flac" loop
                            show spectre slash heart anim onlayer front
                            with dissolve
                            n "But it's too little, too late. In her hand, you realize she clutches your still-beating heart. It thumps unsettlingly.\n"
                            voice "audio/voices/ch2/spectre/_encounter/hero/48.flac"
                            hero "Did... we get her?\n"
                            voice "audio/voices/ch2/spectre/_encounter/cold/56.flac"
                            cold "Even if we didn't, we've given her something to remember.\n"
                            voice "audio/voices/ch2/spectre/_encounter/princess/136.flac"
                            show spectre slash wink anim onlayer front
                            with dissolve
                            sp "See you soon, killer.\n"
                            voice "audio/voices/ch2/spectre/_encounter/narrator/107.flac"
                            $ quick_menu = False
                            play audio "audio/final/Spectre_HeartCrush_2 copy.flac"
                            stop music
                            stop secondary
                            show spectre heart throat slash yank crush onlayer front
                            $ renpy.pause(0.25)
                            voice sustain
                            hide spectre onlayer front
                            hide bg onlayer back
                            hide farback onlayer farback
                            scene bg black
                            with fade
                            n "I'm afraid you'll never know. As she crushes your precious organ in her hand, everything goes dark, and you die.\n"
                            $ trait_cheated = True
                            $ blade_held = False
                            $ default_mouse = "default"
                            jump wraith_start
                            # end

                        "{i}• [[Die.]{/i}":
                            voice "audio/voices/ch2/spectre/_encounter/narrator/108.flac"
                            play audio "audio/final/Adversary_HandThroughChest_2.flac"
                            play secondary "audio/final/Nightmare_HeartBeat_3.flac" loop
                            show spectre heart yank anim onlayer front
                            with dissolve
                            n "But you don't swing your weapon. Your body comes to a juddering halt as she rips her hand from your chest.\n"
                            voice "audio/voices/ch2/spectre/_encounter/narrator/109.flac"
                            $ gallery_spectre.unlock_item(9)
                            $ gallery_spectre.unlock_item(10)
                            $ renpy.save_persistent()
                            $ achievement.grant("ACH_SPECTRE_HEART")
                            n "In her clenched fist is your still-beating heart.\n"
                            voice "audio/voices/ch2/spectre/_encounter/hero/47.flac"
                            hero "But that's ours!\n"
                            voice "audio/voices/ch2/spectre/_encounter/princess/136.flac"
                            show spectre heart yank wink anim onlayer front
                            with dissolve
                            sp "See you soon, killer.\n"
                            voice "audio/voices/ch2/spectre/_encounter/narrator/110.flac"
                            play audio "audio/final/Spectre_HeartCrush_2 copy.flac"
                            $ quick_menu = False
                            stop music
                            stop secondary
                            show spectre heart crush onlayer front
                            $ renpy.pause(0.25)
                            voice sustain
                            hide spectre onlayer front
                            hide bg onlayer back
                            hide farback onlayer farback
                            scene bg black
                            with fade
                            n "She crushes it, blood and ruined vascular tissue leaking from between her fingers, dribbling unceremoniously to the floor. Everything goes dark, and you die.\n"
                            $ blade_held = False
                            $ default_mouse = "default"
                            if spectre_paranoid_override:
                                $ trait_paranoid = True
                            else:
                                $ trait_cheated = True
                            jump wraith_start
                            # end
                else:
                    voice "audio/voices/ch2/spectre/_encounter/cold/57.flac"
                    cold "She's real now. Pity we don't have a weapon.\n"
                    voice "audio/voices/ch2/spectre/_encounter/narrator/111.flac"
                    $ achievement.grant("ACH_SPECTRE_HEART")
                    $ gallery_spectre.unlock_item(9)
                    $ gallery_spectre.unlock_item(10)
                    $ renpy.save_persistent()
                    play audio "audio/final/Adversary_HandThroughChest_2.flac"
                    play secondary "audio/final/Nightmare_HeartBeat_3.flac" loop
                    show spectre heart yank anim onlayer front
                    with dissolve
                    n "Your last moments are spent a helpless witness as she rips her hand from your chest, holding your still-beating heart in her clenched fist.\n"
                    voice "audio/voices/ch2/spectre/_encounter/hero/47.flac"
                    hero "But that's ours!\n"
                    voice "audio/voices/ch2/spectre/_encounter/princess/136.flac"
                    show spectre heart yank wink anim onlayer front
                    with dissolve
                    sp "See you soon, killer.\n"
                    voice "audio/voices/ch2/spectre/_encounter/narrator/110.flac"
                    $ quick_menu = False
                    stop music
                    stop secondary
                    show spectre heart crush onlayer front
                    $ renpy.pause(0.25)
                    voice sustain
                    hide spectre onlayer front
                    hide bg onlayer back
                    hide farback onlayer farback
                    scene bg black
                    with fade
                    n "She crushes it, blood and ruined vascular tissue leaking from between her fingers, dribbling unceremoniously to the floor. Everything goes dark, and you die.\n"
                    $ blade_held = False
                    $ default_mouse = "default"
                    if spectre_paranoid_override:
                        $ trait_paranoid = True
                    else:
                        $ trait_cheated = True
                    jump wraith_start


        "{i}• ''I'm not afraid of you.''{/i}":
            voice "audio/voices/ch2/spectre/_encounter/princess/137.flac"
            play audio "audio/final/Spectre_PossessingPlayer_4.flac"
            show spectre heart squelch talk onlayer front
            sp "Not yet. But let's see if you stay that way.\n"
            jump spectre_kill_player_join

        "{i}• [[Stare at her in silence.]{/i}":
            jump spectre_kill_player_join

        "{i}• [[Step away.]{/i}":
            play audio "audio/one_shot/footsteps_stone.flac"
            voice "audio/voices/ch2/spectre/_encounter/narrator/112.flac"
            n "You do your best to pull away, but it's as if her arm, embedded in your body, is rooting you in place.\n"
            voice "audio/voices/ch2/spectre/_encounter/princess/138.flac"
            play audio "audio/final/Spectre_PossessingPlayer_4.flac"
            show spectre heart squelch talk onlayer front
            sp "Leaving so soon?\n"
            jump spectre_kill_player_join

        #"{i}• [[Slay the Princess.]{/i}" if blade_held:
        #    $ spectre_kill_player_slay_attempt = True
        #    voice "audio/voices/ch2/spectre/_encounter/narrator/113.flac"
        #    show spectre heart slash base onlayer front
        #    with Dissolve(2.0)
        #    n "You swing the blade towards the Princess' neck, but the movement seems to play out in slow motion.\n"
        #    jump spectre_kill_player_join

return
