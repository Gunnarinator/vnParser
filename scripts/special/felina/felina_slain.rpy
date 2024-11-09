label felina_slain_start:

    stop music fadeout 1.0
    default felina_slain_apologize = False
    hide bodies onlayer farback
    hide bg onlayer back
    hide bg onlayer farback
    hide princess onlayer back
    hide stranger onlayer back
    show bg black big onlayer back
    $ renpy.pause(1.0)
    queue secondary "audio/final/Tower_KnifeBlow_3.flac"
    show knife slice onlayer front at yflip, Position(ypos=1125)
    with dissolve
    if first_princess == "harsh":
        $ gallery_zfinale.unlock_item(8)
        $ renpy.save_persistent()
        $ default_mouse = "blood"
        if felina_slain_apologize:
            voice "audio/voices/felina/cabin/slay/princess/1.flac"
            hide bg onlayer back
            hide knife onlayer front
            show bg basement close onlayer farback at Position(ypos=1125)
            show princess harsh goodbye1 onlayer back at Position(ypos=1125)
            with dissolve
            p "You and me both.\n"
        else:
            voice "audio/voices/felina/cabin/slay/princess/2.flac"
            hide bg onlayer back
            hide knife onlayer front
            show bg basement close onlayer farback at Position(ypos=1125)
            show princess harsh goodbye1 onlayer back at Position(ypos=1125)
            with dissolve
            p "So that's how it is...\n"
        voice "audio/voices/felina/cabin/slay/princess/3a.flac"
        show princess harsh goodbye2 onlayer back
        with dissolve
        p "Whatever world you want to build without me, I hope it works out.\n"
        voice "audio/voices/felina/cabin/slay/princess/4.flac"
        show princess harsh goodbye3 onlayer back
        with dissolve
        p "Despite our differences, I've... always loved you. And I wish you nothing but the best.\n"

    elif first_princess == "gentle":
        $ gallery_zfinale.unlock_item(8)
        $ renpy.save_persistent()
        $ default_mouse = "blood"
        voice "audio/voices/felina/cabin/slay/princess/6.flac"
        hide bg onlayer back
        hide knife onlayer front
        show bg basement close onlayer farback at Position(ypos=1125)
        show princess soft goodbye1 onlayer back at Position(ypos=1125)
        with dissolve
        p "So this is what it feels like to actually die.\n"
        voice "audio/voices/felina/cabin/slay/princess/7.flac"
        show princess soft goodbye3 onlayer back
        with dissolve
        p "I... think this for the best. I don't know what the world will be like without me, but it can't be that bad if it still has you in it.\n"
        voice "audio/voices/felina/cabin/slay/princess/8a.flac"
        show princess soft goodbye4 onlayer back
        with dissolve
        p "I've always loved you. Don't forget me.\n"

    else:
        # stranger
        $ gallery_zfinale.unlock_item(14)
        $ renpy.save_persistent()
        if stranger_other_way:
            $ default_mouse = "bloodthumb"
        else:
            $ default_mouse = "blood"
        if felina_slain_apologize:
            voice "audio/voices/felina/cabin/slay/princess/9.flac"
            hide bg onlayer back
            hide knife onlayer front
            show bg basement close onlayer farback at Position(ypos=1125)
            show princess stranger goodbye1 onlayer back at Position(ypos=1125)
            with dissolve
            p "There's no need to apologize. We are what we are, and this is in your nature.\n"
        else:
            voice "audio/voices/felina/cabin/slay/princess/10.flac"
            hide bg onlayer back
            hide knife onlayer front
            show bg basement close onlayer farback at Position(ypos=1125)
            show princess stranger goodbye1 onlayer back at Position(ypos=1125)
            with dissolve
            p "So you've made a choice for all of us.\n"
        voice "audio/voices/felina/cabin/slay/princess/11.flac"
        show princess stranger goodbye2 onlayer back
        with dissolve
        p "Even through everything, through all the worlds we've seen and experienced, through all the lives we've known and lost... we could never imagine a world without you and us. It doesn't feel possible.\n"
        voice "audio/voices/felina/cabin/slay/princess/12.flac"
        show princess stranger goodbye final onlayer back
        with dissolve
        p "Despite it all, we've always loved you. We hope you don't regret what comes next.\n"

    play sound "audio/final/___The Long Quiet Softest FINAL.ogg" loop fadein 20.0
    $ default_mouse = "default"
    $ quick_menu = False
    hide princess onlayer back with fade
    if persistent.quick_menu:
        $ quick_menu = True

    truthmid "You blink, and the Princess is gone. All you have left of her is a small, melancholic weight that sits at the borders of your heart.\n"
    $ quick_menu = False
    show farback quiet onlayer farback at Position(ypos=1125)
    show bg basement end no chain onlayer back at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    if mirror_fates_worse_than_death:
        truthmid "'The tear was rough. You carry a part of what should be her, and she carried a part of what should be you. Things won't be now as they were then, but they aren't nothing, either.'\n"
    else:
        truthmid "Whatever action brought you and the Princess into being was rough and jagged and left each of you with a piece of the other. By destroying her once and for all, you also destroyed a part of yourself. But the world hasn't ended. Things continue on.\n"
    voice "audio/voices/felina/cabin/slay/hero/1.flac"
    hero "She's... gone. And I don't think she's coming back.\n"
    label slay_ending_linger:
        default slay_ending_linger_explore = False
        menu:
            extend ""

            "{i}• (Explore) ''No. She's not. A small part of her is with us.''{/i}" if slay_ending_linger_explore == False:
                $ slay_ending_linger_explore = True
                voice "audio/voices/felina/cabin/slay/hero/2.flac"
                hero "Is that a metaphor, or are you being literal? It doesn't matter. We don't need to linger down here anymore, let's get going.\n"
                jump slay_ending_linger

            "{i}• (Explore) ''No. She's not.''{/i}" if slay_ending_linger_explore == False:
                $ slay_ending_linger_explore = True
                voice "audio/voices/felina/cabin/slay/hero/3.flac"
                hero "Then we did what we set out to do. Come on, let's get going. We don't need to linger down here anymore.\n"
                jump slay_ending_linger

            "{i}• [[Leave the cabin.]{/i}":
                jump felina_slain_leave_join

label felina_slain_leave_join:
    if first_princess == "stranger":
        voice "audio/voices/felina/cabin/slay/contrarian/1.flac"
        contrarian "That's right. We've got a whole world to see.\n"
    $ quick_menu = False
    play audio "audio/one_shot/footsteps_stone.flac"
    hide bg onlayer back
    hide farback onlayer farback
    scene basement stairs closed onlayer front at Position(ypos=1125)
    with fade
    truthmid "You leave the basement behind.\n"
    play audio "audio/one_shot/door_bedroom.flac"
    hide basement onlayer front
    scene farback quiet onlayer farback at Position(ypos=1125)
    show bg cabin end reverse onlayer front at Position(ypos=1125)
    with fade
    truthmid "Then the stairs.\n"
    play audio "audio/one_shot/door_bedroom.flac"
    hide farback onlayer farback
    hide bg onlayer front
    with fade
    $ renpy.pause(0.5)
    $ quick_menu = False
    scene bg black
    show slay dyingstar
    show quiet finale1 onlayer farback at Position(ypos=1125)
    show back trees cabin quiet onlayer back at Position(ypos=1350)
    show bg cabin quiet onlayer front at Position(ypos=1350)
    show mid cabin quiet onlayer inyourface at Position(ypos=1125)
    show fore cabin quiet onlayer inyourface at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    truthmid "And then you leave the cabin itself.\n"
    voice "audio/voices/felina/cabin/slay/hero/4.flac"
    hero "It's quiet here.\n"
    if first_princess == "stranger":
        voice "audio/voices/felina/cabin/slay/contrarian/2.flac"
        contrarian "Yeah, there's not a lot for us to do, is there?\n"
    truth "The path and the woods outside are an empty canvas, but there is even more to see beyond this place. The fruits of your labor. A world free from death.\n"
    menu:
        extend ""

        "{i}• [[Set yourself free.]{/i}":
            $ renpy.music.set_volume(0.25, 2.5, channel='sound')
            play secondary "audio/final/Tower_StormThunder_loop_1.ogg" loop
            truth "The body of an ancient creature stirs from its hibernation, and you feel sensation in limbs you once couldn't fathom. Everything here is You.\n"
            play audio "audio/final/Assorted_WingsFlap_4.flac"
            truth "You feel your wings, spanning a cosmic scale, but twisted and crumpled and bound in agonizing tension to a finite plane.\n"
            play audio "audio/final/Witch_TreeRootsConstricting_2.flac"
            if mirror_construct:
                truthmid "You can feel the glass of the construct pressing in on you, confining you across infinite sides and infinite angles. You push back and strain against it.\n"
                #voice "audio/voices/felina/start/21.flac"
                #mound "It isn't the construct that keeps us here.\n"
            else:
                truthmid "You can feel the glass of your cage pressing in on you, confining you across infinite sides and infinite angles. You push back and strain against it.\n"
            play audio "audio/final/Witch_TreeRootsConstricting_1.flac"
            truthmid "But it does not yield.\n"
            if first_princess == "stranger":
                voice "audio/voices/felina/cabin/slay/contrarian/3.flac"
                contrarian "Come on now, it shouldn't be that hard to break out of here. We're some sort of god, aren't we?\n"
            voice "audio/voices/felina/cabin/slay/hero/5.flac"
            hero "He's gone. She's gone. No one is left to trap us here but us.\n"
            menu:
                extend ""

                "{i}• [[Open your heart and bear witness to your new kingdom.]{/i}":
                    truth "All at once the unyielding tension gives way.\n"


            $ gallery_zfinale.unlock_item(15)
            $ renpy.save_persistent()
            $ renpy.music.set_volume(1.0, 2.5, channel='sound')
            play audio "audio/final/Assorted_SphereBreaks_1.flac"
            show quiet finale2 onlayer farback
            with Dissolve(1.5)
            $ renpy.pause(0.25)
            show quiet finale3 onlayer farback
            with Dissolve(1.5)
            $ renpy.pause(0.25)
            show quiet finale4 onlayer farback
            with Dissolve(1.5)
            $ renpy.pause(0.25)
            #hide quiet onlayer farback
            #with Dissolve(1.5)
            truthmid "And then the shattering. You are free, and before you lies the endless expanse of absolute reality. A new absolute reality, one forged by your will and by a long and arduous cycle of bloodshed that has stained your hands countless times over.\n"
            truthmid "But there will be no more bloodshed in this new world.\n"
            if mirror_n_cruel_count >= 2:
                if broken_met:
                    voice "audio/voices/felina/cabin/slay/broken/1.flac"
                    broken "We didn't forget what you told us.\n"
                if stubborn_met:
                    voice "audio/voices/felina/cabin/slay/stubborn/1.flac"
                    stubborn "You thought we'd be gone. Thought you could taunt us with death.\n"
                if hunted_met:
                    voice "audio/voices/felina/cabin/slay/hunted/1.flac"
                    hunted "We never left. We've just been quiet. Hiding somewhere else. But we don't need to be quiet any longer.\n"
                if cheated_met:
                    voice "audio/voices/felina/cabin/slay/cheated/1.flac"
                    cheated "We're the house now. We get to make the rules, and I'm not so sure you'll like those new rules.\n"
                if skeptic_met:
                    voice "audio/voices/felina/cabin/slay/skeptic/1.flac"
                    skeptic "You should never make assumptions about things that you don't know. Like whether or not the voices in your head will be gone for good.\n"
                if paranoid_met:
                    voice "audio/voices/felina/cabin/slay/paranoid/1.flac"
                    paranoid "Torturer. And to think I thought we could rely on you. Can't even trust ourself.\n"
                if cold_met:
                    voice "audio/voices/felina/cabin/slay/cold/1.flac"
                    cold "This is going to be fun, isn't it?\n"
                if smitten_met:
                    voice "audio/voices/felina/cabin/slay/smitten/1.flac"
                    smitten "Slaying our beloved and threatening us with damnation. There's no good ending for you.\n"
                if contrarian_met:
                    voice "audio/voices/felina/cabin/slay/contrarian/4.flac"
                    contrarian "You all need to lighten up! Telling us we were going to die was funny!\n"
                    voice "audio/voices/felina/cabin/slay/hero/6.flac"
                    hero "I'm not sure they agree with you. Voices get around.\n"
                else:
                    voice "audio/voices/felina/cabin/slay/hero/7.flac"
                    hero "I'm sorry. They all know what you did. Voices get around.\n"
                if opportunist_met:
                    voice "audio/voices/felina/cabin/slay/opportunist/1.flac"
                    opportunist "Knives out, boys. It's time to get to work.\n"
                $ achievement.grant("ACH_END_SLAY_ALT")
                $ final_ending = "slay_whoops"
                $ quick_menu = False
                hide quiet onlayer farback
                hide slay onlayer farback
                hide back onlayer back
                hide bg onlayer front
                hide mid onlayer inyourface
                hide fore onlayer inyourface
                scene bg black
                with fade
                jump credits
                #END
            else:
                if broken_met:
                    voice "audio/voices/felina/cabin/slay/broken/2.flac"
                    broken "It's finally over, isn't it? But all of us are still here.\n"
                if stubborn_met:
                    voice "audio/voices/felina/cabin/slay/stubborn/2.flac"
                    stubborn "I knew we'd finally see it through. All it takes to be a winner is grit and determination.\n"
                    if cheated_met:
                        voice "audio/voices/felina/cabin/slay/cheated/2.flac"
                        cheated "We really did win, didn't we?\n"
                if cheated_met and stubborn_met == False:
                    voice "audio/voices/felina/cabin/slay/cheated/3.flac"
                    cheated "We really won.\n"
                if cheated_met:
                    voice "audio/voices/felina/cabin/slay/cheated/4.flac"
                    cheated "We're the house now. We get to make the rules.\n"
                if hunted_met:
                    voice "audio/voices/felina/cabin/slay/hunted/2.flac"
                    hunted "This is nice! No more hunting. No more running. Just us, and whatever's out there.\n"
                if skeptic_met:
                    voice "audio/voices/felina/cabin/slay/skeptic/2.flac"
                    skeptic "Absolute reality. Who would have thought there was really a world outside of us? And who would have thought we'd actually wind up siding with Him?\n"
                if paranoid_met:
                    voice "audio/voices/felina/cabin/slay/paranoid/2.flac"
                    paranoid "The whispering and the coercion and the bickering — everything horrible about being alive has stopped. I could get used to this.\n"
                if cold_met:
                    voice "audio/voices/felina/cabin/slay/cold/2.flac"
                    cold "That wasn't very hard at all.\n"
                    voice "audio/voices/felina/cabin/slay/hero/8.flac"
                    hero "Speak for yourself.\n"
                if opportunist_met:
                    voice "audio/voices/felina/cabin/slay/opportunist/2.flac"
                    opportunist "Well boys? How does it feel? We're not just on top of the pecking order. We are the pecking order now.\n"
                if smitten_met:
                    voice "audio/voices/felina/cabin/slay/smitten/2.flac"
                    smitten "I hope this was all worth it, because I'm personally inconsolable.\n"
                    if skeptic_met:
                        voice "audio/voices/felina/cabin/slay/skeptic/3.flac"
                        skeptic "Lucky for us, you have forever to get over it.\n"
                    if cheated_met:
                        voice "audio/voices/felina/cabin/slay/cheated/5.flac"
                        cheated "Time mends a lot of things. You'll get better.\n"
                    if stubborn_met:
                        voice "audio/voices/felina/cabin/slay/stubborn/3.flac"
                        stubborn "Hear hear, to our vanquished foe!\n"
                if first_princess != "stranger" and contrarian_met:
                    voice "audio/voices/felina/cabin/slay/contrarian/5.flac"
                    contrarian "It's good to be back! Now we just have to figure out what to do with ourselves. Forever. No problem. We can do that, yeah?\n"
                if first_princess == "stranger":
                    voice "audio/voices/felina/cabin/slay/contrarian/6.flac"
                    contrarian "Welcome back, everyone! It's great to see you all again. Now we just have to figure out what to do with ourselves. Forever. No problem. We can do that, yeah?\n"
                if contrarian_met:
                    voice "audio/voices/felina/cabin/slay/hero/9.flac"
                    hero "Yeah. We can do that.\n"
                else:
                    voice "audio/voices/felina/cabin/slay/hero/10.flac"
                    hero "Well, then. I guess the only thing left do is figure out what happens next.\n"
                $ achievement.grant("ACH_END_SLAY")
                $ final_ending = "slay"

            $ quick_menu = False
            hide quiet onlayer farback
            hide slay onlayer farback
            hide back onlayer back
            hide bg onlayer front
            hide mid onlayer inyourface
            hide fore onlayer inyourface
            scene bg black
            with fade
            jump credits
            # END CREDITS
