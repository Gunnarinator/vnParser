label tower_2_start:

    # starting things up
    stop music
    stop sound
    stop secondary
    $ default_mouse = "default"
    $ blade_held = False
    $ current_loop = 2
    $ quick_menu = False
    $ config.menu_include_disabled = False

    $ current_princess = "apotheosis"

    play sound "audio/looping/uncomfortable ambiance heightened.ogg" loop fadein 1.0
    scene chapter apotheosis with fade
    show text _("{color=#FFFFFF00}Chapter 3. The Apotheosis.{/color}") at Position(ypos=850)
    $ renpy.pause(4.0)

    if persistent.quick_menu:
        $ quick_menu = True

    play sound "audio/_pristine/sfx/Tower_StormThunder_loop_1.flac" loop
    play music "audio/_music/ch2/tower/The Tower.flac" loop
    scene bg black
    scene stars apotheosis onlayer farback at Position(ypos=1125)
    show bg apotheosis start onlayer back at Position(ypos=1125)
    show mid apotheosis start onlayer front at Position(ypos=1125)
    show fore apotheosis start onlayer inyourface at Position(ypos=1125)
    with fade
    $ gallery_apotheosis.unlock_gallery()
    $ gallery_apotheosis.unlock_item(1)
    $ renpy.save_persistent()
    if tower_1_cabin_blade_taken:
        $ trait_contrarian = True
        jump apotheosis_start_contrarian
    else:
        $ trait_paranoid = True
    voice "audio/voices/ch3/apotheosis/narrator/1.flac"
    n "You're on a path in the woods. And at the end of that path—\n{w=3.7}{nw}"
    show screen disableclick(0.5)
    voice "audio/voices/ch3/apotheosis/hero/1.flac"
    hero "Oh, let me guess! And at the end of that path is a cabin.\n"
    #voice "audio/voices/ch3/apotheosis/narrator/2.flac"
    #n "Excuse me?\n"
    voice "audio/voices/ch3/apotheosis/paranoid/1a.flac"
    paranoid "This is hardly a path in the woods. It's all... big, and weird.\n"
    #voice "audio/voices/ch3/apotheosis/hero/2.flac"
    #hero "Oh, you're new.\n"
    voice "audio/voices/ch3/apotheosis/broken/t2_broken_1.flac"
    broken "Another witness to her Radiance. Her hour is soon upon us.\n"
    #voice "audio/voices/ch3/apotheosis/paranoid/2.flac"
    #paranoid "I'm here to keep {i}him{/i} in check. I'm sick of prying fingers digging around in our head, and he's making it all too easy for them to get in.\n"
    voice "audio/voices/ch3/apotheosis/narrator/3.flac"
    n "This is bad.\n"
    voice "audio/voices/ch3/apotheosis/hero/3.flac"
    hero "Oh, is it now? I hadn't noticed! Do you need a primer, Mr. Amnesiac?\n"
    voice "audio/voices/ch3/apotheosis/narrator/4.flac"
    n "No, I'm quite alright, but if all of you would take a moment to settle down, there's something important I'd like to get across to you before it's too late.\n"
    voice "audio/voices/ch3/apotheosis/hero/4.flac"
    hero "Is it about the Princess? We already know all about the Princess.\n"
    #voice "audio/voices/ch3/apotheosis/paranoid/3.flac"
    #paranoid "Not to be trusted, that one.\n"
    voice "audio/voices/ch3/apotheosis/narrator/5.flac"
    n "No! I mean yes. It's about the Princess, but whatever you think I'm going to say, it's probably not that.\n"
    #voice "audio/voices/ch3/apotheosis/paranoid/4.flac"
    #paranoid "You're not to be trusted either.\n"
    voice "audio/voices/ch3/apotheosis/hero/5.flac"
    hero "Look, fine. Just out with it already, yeah? But if I hear the words 'you're here to slay her' or 'if you don't, it will be the end of the world' you'll have lost speaking privileges.\n"
    #voice "audio/voices/ch3/apotheosis/narrator/6.flac"
    #n "You're going to hear some of those words, but not all of them, and definitely not all in that order.\n"
    #voice "audio/voices/ch3/apotheosis/paranoid/5.flac"
    #paranoid "... I'm interested.\n"
    #voice "audio/voices/ch3/apotheosis/hero/6.flac"
    #hero "Really?\n"
    #voice "audio/voices/ch3/apotheosis/paranoid/6.flac"
    #paranoid "I know it's probably a bunch of lies, but even lies have a kernel of truth to them.\n"
    voice "audio/voices/ch3/apotheosis/broken/t2_broken_2.flac"
    broken "You two are just wasting your time. It's all going to end when we open that cabin door, which means it's already all over. What's the point of dawdling when the end is already written?\n"
    voice "audio/voices/ch3/apotheosis/narrator/7.flac"
    n "Okay, that nonsense he's going on about? That's what we need to talk about. You've been here before. Obviously.\n"
    #voice "audio/voices/ch3/apotheosis/hero/7.flac"
    #hero "So you {i}have{/i} met us! Because boy were you in denial about that last time.\n"
    #voice "audio/voices/ch3/apotheosis/narrator/8a.flac"
    #n "No I haven't met you, but reality is clearly falling apart at the moment, and the only reason that would happen #is if you knew things you weren't supposed to know.\n"
    #voice "audio/voices/ch3/apotheosis/hero/8.flac"
    #hero "Wha— what the hell are you talking about?\n"
    #voice "audio/voices/ch3/apotheosis/paranoid/7a.flac"
    #paranoid "He's talking about all those weird marble trees and how wrong everything looks.\n"
    voice "audio/voices/ch3/apotheosis/narrator/9b.flac"
    n "Whatever you did before gave her far too much power. So you've got to cut it out, get to that cabin, and slay her before things get any more out of hand.\n"
    #n "Yes. Exactly. Whatever you did before gave her far too much power. So you've got to cut it out, get to that cabin, and slay her before things get any more out of hand.\n"
    #voice "audio/voices/ch3/apotheosis/hero/9a.flac"
    #hero "... we gave her power? Why didn't you ever tell us we could do that? We probably would have gone about things very differently if we knew that.\n"


    # MIX BEGININIG TO BE LOUDER
    voice "audio/voices/ch3/apotheosis/paranoid/8.flac"
    paranoid "Are... are our thoughts doing that? Make her small, make her small, make her small, make her small... shit what if I'm doing it wrong? What if I'm making her even stronger?\n" id tower_2_start_23792ad8
    voice "audio/voices/ch3/apotheosis/broken/t2_broken_3.flac"
    broken "We've built a new god, and she is limitless.\n"
    voice "audio/voices/ch3/apotheosis/narrator/10.flac"
    n "Do you hear those two with their runaway thoughts? I'm only giving you the sliver of information I'm giving you now, because things are already deep in the shitter. This was my last card to play, and it looks like it's already made things worse. So hurry. Cabin. Now.\n"
    label apotheosis_explore_menu:
        default apotheosis_explore = False
        menu:
            extend ""

            "{i}• (Explore) Okay, now hold on. I have SO many questions.{/i}" if apotheosis_explore == False:
                $ apotheosis_explore = True
                voice "audio/voices/ch3/apotheosis/narrator/11.flac"
                n "And right now, you have neither the time nor the mental acuity to handle a single response. It's now or never.\n"
                jump apotheosis_explore_menu

            "{i}• (Explore) I'm not going to the cabin until I have answers! What am I?{/i}":
                stop music
                play secondary "audio/final/Tower_Earthquake_loop_1.ogg" loop
                show bg apotheosis crumble onlayer back at screenshake
                show mid apotheosis crumble onlayer front at screenshake
                show fore apotheosis crumble onlayer inyourface at screenshake
                voice "audio/voices/ch3/apotheosis/narrator/12.flac"
                n "As you finish your inane question, the ground quakes beneath your feet. You feel an unyielding force pulling at you and your surroundings. The 'trees' start to sway, then crumble, breaking apart as everything is drawn towards the cabin.\n"
                voice "audio/voices/ch3/apotheosis/narrator/13.flac"
                show bg apotheosis crumble onlayer back at apoth_zoom_in
                show mid apotheosis crumble onlayer front at apoth_zoom_in
                show fore apotheosis crumble onlayer inyourface at apoth_zoom_in
                n "Even the earth beneath you seems to shift, your feet unable to grip solid ground as you're dragged forward along with everything else.\n"

            "{i}• [[Head to the cabin.]{/i}":
                #voice "audio/voices/ch3/apotheosis/narrator/14.flac"
                #n "You quickly make your way down the path towards the cabin.\n"
                label apotheosis_generic_join:
                    stop music
                    play secondary "audio/final/Tower_Earthquake_loop_1.ogg" loop
                    show bg apotheosis crumble onlayer back at screenshake
                    show mid apotheosis crumble onlayer front at screenshake
                    show fore apotheosis crumble onlayer inyourface at screenshake
                    voice "audio/voices/ch3/apotheosis/narrator/15.flac"
                    n "But a great and horrible change is already underway. The ground quakes beneath your feet, and you feel an unyielding force pulling at you and your surroundings. The 'trees' start to sway, then crumble, breaking apart as everything is drawn towards the cabin.\n"
                    voice "audio/voices/ch3/apotheosis/narrator/13.flac"
                    show bg apotheosis crumble onlayer back at apoth_zoom_in
                    show mid apotheosis crumble onlayer front at apoth_zoom_in
                    show fore apotheosis crumble onlayer inyourface at apoth_zoom_in
                    n "Even the earth beneath you seems to shift, your feet unable to grip solid ground as you're dragged forward along with everything else.\n"

            "{i}• [[Run away.]{/i}":
                default apotheosis_run = False
                $ apotheosis_run = True
                jump apotheosis_generic_join
                #voice "audio/voices/ch3/apotheosis/narrator/16.flac"
                #n "A coward to your core, you do your best to flee from the encroaching end. But a great and horrible change is already underway.\n"
                #voice "audio/voices/ch3/apotheosis/narrator/17.flac"
                #n "The ground quakes beneath your feet, and you feel an unyielding force pulling at you and your surroundings. #The 'trees' start to sway, then crumble, breaking apart as everything is drawn towards the cabin.\n"
                #voice "audio/voices/ch3/apotheosis/narrator/13.flac"
                #n "Even the earth beneath you seems to shift, your feet unable to grip solid ground as you're dragged forward along with everything else.\n"

            "{i}• [[Stay where you are.]{/i}":
                voice "audio/voices/ch3/apotheosis/narrator/18.flac"
                n "There's no room for indecision, you have to—\n{w=2.5}{nw}"
                show screen disableclick(0.5)
                stop music
                play secondary "audio/final/Tower_Earthquake_loop_1.ogg" loop
                show bg apotheosis crumble onlayer back at screenshake
                show mid apotheosis crumble onlayer front at screenshake
                show fore apotheosis crumble onlayer inyourface at screenshake
                voice "audio/voices/ch3/apotheosis/narrator/19.flac"
                n "{i}Sigh.{/i} The ground quakes beneath your feet, and you feel an unyielding force pulling at you and your surroundings. The 'trees' start to sway, then crumble, breaking apart as everything is drawn towards the cabin.\n"
                voice "audio/voices/ch3/apotheosis/narrator/13.flac"
                show bg apotheosis crumble onlayer back at apoth_zoom_in
                show mid apotheosis crumble onlayer front at apoth_zoom_in
                show fore apotheosis crumble onlayer inyourface at apoth_zoom_in
                n "Even the earth beneath you seems to shift, your feet unable to grip solid ground as you're dragged forward along with everything else.\n"

label tower_2_cabin:

    voice "audio/voices/ch3/apotheosis/broken/t2_broken_4.flac"
    broken "The end of everything... the beginning of something new. The moment we open that door, she will be free.\n"
    #if trait_contrarian:
    #    voice "audio/_pristine/voice/apotheosis/contrarian/1.flac"
    #    contrarian "I don't think it's ever actually worked like that.\n"
    if trait_paranoid:
        voice "audio/voices/ch3/apotheosis/paranoid/9.flac"
        paranoid "Stop believing everything you hear! We just have to get our thoughts in order. We just have to think straight.\n"
    voice "audio/voices/ch3/apotheosis/hero/10.flac"
    hero "Any, uh... words of warning?\n"
    voice "audio/voices/ch3/apotheosis/narrator/20.flac"
    n "You already know everything you need to know.\n"
    menu:
        extend ""

        "{i}• [[Proceed into the cabin.]{/i}":
            $ renpy.music.set_volume(0.00, channel='music2')
            play secondary "audio/final/Tower_HouseExploadGiant_1.flac"
            queue secondary "audio/final/Tower_Earthquake_oneshot_faded_1.flac"
            play music "audio/_music/ch3/apotheosis/Apotheosis Intro_edit.flac"
            queue music "audio/_music/ch3/apotheosis/Apotheosis Loop.flac" loop
            play music2 "audio/_pristine/music/apotheosis/Apoth Vocal Warp Intro.flac"
            queue music2 "audio/_pristine/music/apotheosis/Apoth Vocal Warp Loop.flac" loop
            #play audio "audio//final/Tower_Earthquake_oneshot_faded_1.flac"
            voice "audio/voices/ch3/apotheosis/narrator/21.flac"
            hide bg onlayer back
            hide mid onlayer front
            hide fore onlayer inyourface
            if persistent.flickering:
                show bg apotheosis erupt onlayer back at screenshake, Position(ypos=1125)
                show mid apotheosis erupt onlayer front at screenshake, Position(ypos=1125)
                show fore apotheosis erupt onlayer inyourface at screenshake, Position(ypos=1125)
                with flash
            else:
                show bg apotheosis erupt onlayer back at screenshake, Position(ypos=1125)
                show mid apotheosis erupt onlayer front at screenshake, Position(ypos=1125)
                show fore apotheosis erupt onlayer inyourface at screenshake, Position(ypos=1125)
                with dissolve
            n "As you step forward, the cabin explodes.\n"
            play audio "audio/final/Tower_GiantPundingPlayerGround_4.flac"
            show bg apotheosis erupt onlayer back at zoom_out_far
            show mid apotheosis erupt onlayer front at zoom_out_far
            show fore apotheosis erupt onlayer inyourface at zoom_out_far
            with hpunch
            voice "audio/voices/ch3/apotheosis/narrator/22.flac"
            n "You're flung backwards, violently slamming into a tree as debris rains down around you.\n"
            $ gallery_apotheosis.unlock_item(2)
            $ renpy.save_persistent()
            $ achievement.grant("ACH_TOWER_WITNESS")
            play secondary "audio/final/Tower_Earthquake_oneshot_faded_1.flac"
            hide stars onlayer farback
            hide bg onlayer back
            hide mid onlayer front
            hide fore onlayer inyourface
            show stars apotheosis cabin erupt 1 onlayer farback at Position(ypos=1125)
            show cg apotheosis cabin erupt 1 onlayer back at Position(ypos=1125)
            with Dissolve(1.0)
            $ renpy.pause(0.25)
            show stars apotheosis cabin erupt 2 onlayer farback at Position(ypos=1125)
            show cg apotheosis cabin erupt 2 onlayer back at Position(ypos=1125)
            with Dissolve(1.0)
            $ renpy.pause(0.25)
            show stars apotheosis cabin erupt 3 onlayer farback at Position(ypos=1125)
            show cg apotheosis cabin erupt 3 onlayer back at Position(ypos=1125)
            with Dissolve(1.0)
            $ renpy.pause(0.25)
            show stars apotheosis cabin erupt 4 onlayer farback at Position(ypos=1125)
            show cg apotheosis cabin erupt 4 onlayer back at Position(ypos=1125)
            with Dissolve(1.0)
            $ renpy.pause(0.25)
            show stars apotheosis cabin erupt 5 onlayer farback at Position(ypos=1125)
            show cg apotheosis cabin erupt 5 onlayer back at Position(ypos=1125)
            with Dissolve(0.25)
            $ renpy.pause(0.25)
            show cg apotheosis standing onlayer back at Position(ypos=1125)
            with Dissolve(0.25)
            voice "audio/voices/ch3/apotheosis/narrator/23.flac"
            n "You watch in paralyzed awe and terror as the Princess emerges, her body unfurling from some vast space as she stands upright to face you.\n"
            voice "audio/voices/ch3/apotheosis/narrator/24.flac"
            n "The world bows to her. The ruined landscape shifts, trees and stone and the ground itself succumbing to her gravity, orbiting her like a great black hole.\n"
            show mouth apotheosis talk onlayer back at Position(ypos=1125) with dissolve
            voice "audio/voices/ch3/apotheosis/princess/sp1.flac"
            spright "Finally, the little bird has set me free. This is always how it was going to end, and this is always how it was going to begin.\n"
            play audio "audio/final/Tower_KnifeWizzByEmbedTree_2.flac"
            voice "audio/voices/ch3/apotheosis/narrator/25.flac"
            hide mouth onlayer back
            hide cg onlayer back
            hide stars onlayer farback
            show stars apotheosis blade tree onlayer farback at Position(ypos=1125)
            show mid apotheosis blade tree onlayer back at Position(ypos=1125)
            show fore apotheosis blade tree onlayer front at Position(ypos=1125)
            show blade apotheosis tree onlayer front at Position(ypos=1125)
            with Dissolve(1.0)
            n "There's a loud thunk from the tree behind you as something embeds in its shattered bark. Your pristine blade. It's now or never.\n"
            if trait_contrarian:
                jump contrarian_pristine_apoth_menu
            else:
                jump paranoid_pristine_apoth_menu

label tower_2_mirror:
    $ achievement.grant("ACH_TOWER_WITNESS")
    voice "audio/voices/ch3/apotheosis/broken/t2_broken_6.flac"
    broken "No! Where did she go?\n"
    voice "audio/voices/ch3/apotheosis/paranoid/11.flac"
    paranoid "She's gone...\n"
    voice "audio/voices/ch3/apotheosis/hero/14.flac"
    hero "Is this the end of the world? Did she end herself?\n"
    jump mirror_start_2

return
