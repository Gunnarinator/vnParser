label wraith_start:

    # starting things up

    stop music
    stop sound
    stop secondary
    $ default_mouse = "default"
    $ blade_held = False
    $ current_loop = 2
    $ quick_menu = False
    $ config.menu_include_disabled = False
    $ wraith_encountered = True
    default wraith_source = ""
    default wraith_bonus_voice = ""

    $ gallery_wraith.unlock_gallery()
    $ gallery_wraith.unlock_item(1)
    $ renpy.save_persistent()

    # voice combinations
    if current_princess == "nightmare":
        $ wraith_source = "nightmare"
        $ current_princess = "wraith"
    else:
        $ wraith_source = "spectre"
        $ current_princess = "wraith"
    # Nightmare -> Fall forever = paranoid + opportunist
    # Nightmare -> Stuck forever = paranoid + cold

    # Spectre -> Defeated in combat = cold + cheated
    # Spectre -> You try to leave her = cold + paranoid

    if wraith_bonus_voice == "paranoid":
        $ trait_paranoid = True
    elif wraith_bonus_voice == "opportunist":
        $ trait_opportunist = True
    elif wraith_bonus_voice == "cold":
        $ trait_cold = True
    elif wraith_bonus_voice == "cheated":
        $ trait_cheated = True

    $ current_princess = "wraith"

    play sound "audio/looping/uncomfortable ambiance heightened.ogg" loop fadein 1.0
    scene chapter wraith with fade
    show text _("{color=#FFFFFF00}Chapter Three. The Wraith.{/color}") at Position(ypos=850)
    $ renpy.pause(4.0)
    scene bg black with fade

    play sound "audio/looping/STP_chaoticwind_loop.ogg" loop fadein 1.0
    play music "audio/_music/ch3/wraith/The Wraith.flac" loop
    scene bg woods wraith onlayer back at Position(ypos=1125)
    show fore woods wraith onlayer front at Position(ypos=1125)
    with fade
    # FAST
    if persistent.quick_menu:
        $ quick_menu = True
    voice "audio/voices/ch3/wraith/narrator/1.flac"
    n "You're on a path in the woods—\n{w=2.0}{nw}"
    show screen disableclick(0.5)
    if trait_paranoid:
        voice "audio/voices/ch3/wraith/paranoid/1.flac"
        paranoid "Shit — this really doesn't end, does it? It doesn't matter if we kill her, it doesn't matter if she kills us, it just goes on and on and on and on and on.\n"
        if trait_cold:
            voice "audio/voices/ch3/wraith/cold/1.flac"
            cold "Yes, so it does.\n"
            voice "audio/voices/ch3/wraith/hero/1.flac"
            hero "No, there has to be a way out of here. There just has to be.\n"
            if wraith_source == "nightmare":
                voice "audio/voices/ch3/wraith/paranoid/2.flac"
                paranoid "What if... we do what she asked us to last time. What if we just let her leave?\n"
            else:
                voice "audio/voices/ch3/wraith/cold/2.flac"
                cold "Does there have to be a way out? For all we know, this is just how things are.\n"
                if spectre_possession_ask:
                    voice "audio/voices/ch3/wraith/hero/2.flac"
                    hero "No. No, I can't accept that. What if we let her take our body? That's what she wanted last time. We can still put all of this to rest, right?\n"
                else:
                    voice "audio/voices/ch3/wraith/hero/3.flac"
                    hero "No. No, I can't accept that. I know she just killed us, but... what if we free her? What if we help her leave? We haven't tried that yet!\n"
                    voice "audio/voices/ch3/wraith/cold/3.flac"
                    cold "That does sound like it could be interesting. Or at least different.\n"
            if wraith_source == "spectre":
                voice "audio/voices/ch3/wraith/paranoid/3.flac"
                paranoid "I don't think we can stop her if that's what she wants to do. She ripped our heart out. Who's to say she can't go ahead and steal our body and make us do what she wants?\n"
        else:
            voice "audio/voices/ch3/wraith/opportunist/1.flac"
            opportunist "We've tried doing it our way, and we've tried doing it His way. I think the only way left is hers.\n"
            voice "audio/voices/ch3/wraith/hero/4.flac"
            hero "Are you suggesting we let her out?\n"
            voice "audio/voices/ch3/wraith/opportunist/2.flac"
            opportunist "And why shouldn't we? It's obvious she's the one with the real power here. We might as well ingratiate ourselves to our terrifying new overlord.\n"
        voice "audio/voices/ch3/wraith/narrator/2a.flac"
        n "Okay. So you've already been here. More than once, even. Great. So you probably already know all about her and all about the threat she poses to the world.\n"
        voice "audio/voices/ch3/wraith/narrator/3.flac"
        n "Then let me remind you how catastrophic it would be if you helped her leave in any way. If she gets out, the world ends, and everyone ends with it. Yourself included.\n"
        if trait_opportunist:
            voice "audio/voices/ch3/wraith/opportunist/3.flac"
            opportunist "See, it's that last part I'm not so sure about. We've 'ended' twice now. We even ended her once, but it didn't matter! Because it still threw us right back into these woods.\n"

        else:
            if wraith_source == "nightmare":
                voice "audio/voices/ch3/wraith/cold/4.flac"
                cold "Oh, threatening us with death, are we? And why should we be afraid of dying? We've already done it twice.\n"
            else:
                voice "audio/voices/ch3/wraith/cold/5.flac"
                cold "Oh, threatening us with death, are we? And why should we be afraid of anything? We've already died twice. It doesn't mean much to us anymore.\n"
            voice "audio/voices/ch3/wraith/cold/6.flac"
            cold "All death has done is shunt us back to these woods where we're forced to listen to your empty warnings again and again.\n"

        voice "audio/voices/ch3/wraith/paranoid/4.flac"
        paranoid "This place feels a bit different, though, doesn't it? I don't even know what I'd call it, but it's definitely not the same path in the woods anymore.\n"
        label wraith_start_join:
            voice "audio/voices/ch3/wraith/narrator/4.flac"
            n "That's all the more reason to take this seriously. If the path isn't the same, it means that her influence is spreading, and the world has already started to end.\n"
            voice "audio/voices/ch3/wraith/hero/5.flac"
            hero "Her 'influence...'?\n"
            voice "audio/voices/ch3/wraith/narrator/5.flac"
            n "I really shouldn't have said that. It'll make your task more difficult... but now it's out, you could always take that information as a sign of good will between us and do your job, all right?\n"
            if trait_opportunist:
                voice "audio/voices/ch3/wraith/opportunist/4.flac"
                opportunist "Well then, if the world's rushing to an end, that's all the more reason for us to rush over to the cabin and make ourselves useful. It's all about making a good impression. If we're useful, there's a place for us!\n"
            #elif trait_paranoid:
            #    voice "audio/voices/ch3/wraith/paranoid/5.flac"
            #    paranoid "Great... let's just hurry.\n"
            jump wraith_woods_menu

    elif trait_cold:
        voice "audio/voices/ch3/wraith/cold/7.flac"
        cold "And here we go again. Off to slay her. Again.\n"
        voice "audio/voices/ch3/wraith/cheated/1.flac"
        cheated "The deck's stacked, isn't it? We kill her, we start again. She kills us as a goddamn ghost, we start again. I'm starting to think we're being run in circles just for the sake of it...\n"
        voice "audio/voices/ch3/wraith/hero/6.flac"
        hero "Come on, let's not give in to all that misery just yet. There's got to be a way out of this. There's got to be a right answer.\n"
        voice "audio/voices/ch3/wraith/cheated/2.flac"
        cheated "And what if there isn't? Aren't you listening to me? What if all of this was rigged from the start?\n"
        voice "audio/voices/ch3/wraith/hero/7.flac"
        hero "That's ridiculous, there'd be no point if all this was just some kind of... cosmic busy-work.\n"
        voice "audio/voices/ch3/wraith/cheated/3.flac"
        cheated "I think that's exactly what it is. The powers that be seeing how many ways they can screw with us. Could be it's all some kind of sick joke to them.\n"
        #voice "audio/voices/ch3/wraith/hero/8.flac"
        #hero "But wouldn't that get... I don't know, boring?\n"
        #voice "audio/voices/ch3/wraith/cold/8.flac"
        #cold "Not if they're creative with it.\n"
        voice "audio/voices/ch3/wraith/narrator/6.flac"
        n "Okay. So you've already been here. Twice, even. Great. Then let me poke a few holes in your depressing little theory.\n"
        voice "audio/voices/ch3/wraith/narrator/7.flac"
        n "Nobody here is 'screwing' with you, and I can't imagine any scenario where you would have 'started over' after slaying the Princess.\n"
        voice "audio/voices/ch3/wraith/hero/9a.flac"
        hero "Well, we didn't {i}have{/i} to start over.\n"
        voice "audio/voices/ch3/wraith/cold/9.flac"
        cold "We killed ourself.\n"
        voice "audio/voices/ch3/wraith/narrator/8.flac"
        n "And why, pray tell, did you do that?\n"
        voice "audio/voices/ch3/wraith/cold/10.flac"
        cold "Because you decided to foist an infinite tedium on us.\n"
        voice "audio/voices/ch3/wraith/narrator/9.flac"
        n "That doesn't sound like me. If I'd had everything my way, you would have effortlessly slain the Princess, saved the world, and been given your happy ending.\n"
        voice "audio/voices/ch3/wraith/cold/11.flac"
        cold "The ending was the tedium. You locked us in a cabin and sent that cabin to an endless void, and then you told us we were happy.\n"
        voice "audio/voices/ch3/wraith/narrator/10.flac"
        n "Well... were you happy?\n"
        voice "audio/voices/ch3/wraith/hero/10.flac"
        hero "Of course we weren't happy! That's why we killed ourself. It was awful!\n"
        #voice "audio/voices/ch3/wraith/cold/12.flac"
        #cold "It was boring.\n"
        #voice "audio/voices/ch3/wraith/cheated/4a.flac"
        #cheated "It was bullshit!\n"
        #voice "audio/voices/ch3/wraith/narrator/11.flac"
        #n "So you killed yourself?\n"
        voice "audio/voices/ch3/wraith/cold/13.flac"
        cold "Yes, and then she killed us.\n"
        voice "audio/voices/ch3/wraith/cheated/5.flac"
        cheated "Even though she was already dead! This is all fake.\n"
        voice "audio/voices/ch3/wraith/narrator/12.flac"
        n "{i}Sigh.{/i} Okay. Let's try to get back on track. You're real. The Princess is real. The world is real. The people in the world are real. And the danger she poses to all of them is also, quite unfortunately, real.\n"
        voice "audio/voices/ch3/wraith/narrator/13.flac"
        n "Whatever you did the first time, it sounds like it almost worked, so how about you give it one last try? Because killing yourself seemed to undo all the good you almost managed to accomplish.\n"
        #voice "audio/voices/ch3/wraith/cheated/6.flac"
        #cheated "And why should we help you? So you can just lock us away forever again? No, I don't think so.\n"
        voice "audio/voices/ch3/wraith/cold/14.flac"
        cold "All this standing around and talking is boring. Let's at least do something. Maybe we'll kill her again. Maybe we won't. Maybe we'll even free her.\n"
        #voice "audio/voices/ch3/wraith/cheated/9.flac"
        #cheated "Now wouldn't that be something...\n"
        #voice "audio/voices/ch3/wraith/cold/15.flac"
        #cold "It would. I guess we'll just have to see what happens.\n"
        #voice "audio/voices/ch3/wraith/narrator/15.flac"
        #n "{i}Sigh.{/i} Thankfully, you all aren't the ones actually making the decisions, are you? You know what you have to do. You have to slay her. You have to save the world. Nothing matters more than this.\n"
        #voice "audio/voices/ch3/wraith/cheated/10.flac"
        #cheated "Don't play by his rules. Everything here's rigged. Everything here's changing to whatever's convenient for Him. Even the woods are changing.\n"
        jump wraith_woods_menu

label wraith_woods_menu:
    default wraith_woods_explore = False
    default wraith_woods_loop_explore = False
    default wraith_woods_leave_explore = False
    default wraith_woods_why_help_explore = False
    default wraith_cheated_rules_count = 0
    menu:

        extend ""

        "{i}• (Explore) ''And why should we help you? All you're going to do is lock us away forever again.''{/i}" if wraith_woods_why_help_explore == False and trait_cold and trait_cheated:
            $ wraith_woods_why_help_explore = True
            voice "audio/voices/ch3/wraith/narrator/14.flac"
            n "Tell you what! I won't do that. I promise.\n"
            voice "audio/voices/ch3/wraith/cheated/7.flac"
            cheated "Oh, yeah, sure. That changes everything.\n"
            voice "audio/voices/ch3/wraith/hero/11.flac"
            hero "I mean, he did promise...\n"
            voice "audio/voices/ch3/wraith/cheated/8.flac"
            cheated "And you believed him? Pah.\n"
            jump wraith_woods_menu


        "{i}• (Explore) ''Are you the same Narrator we met on the other loops? You were quick to accept that we've been here before.''{/i}" if wraith_woods_loop_explore == False:
            $ wraith_woods_loop_explore = True
            if trait_paranoid:
                voice "audio/voices/ch3/wraith/paranoid/6.flac"
                paranoid "Suspiciously quick...\n"
            voice "audio/voices/ch3/wraith/narrator/16.flac"
            n "If I had to make a wager, I'd say yes and no.\n"
            if trait_cheated:
                voice "audio/voices/ch3/wraith/cheated/11.flac"
                cheated "That's a hedge, not a wager.\n"
            elif trait_cold:
                voice "audio/voices/ch3/wraith/cold/16.flac"
                cold "Is that supposed to be a riddle? If it is, it's not very good.\n"
            else:
                voice "audio/voices/ch3/wraith/paranoid/7.flac"
                paranoid "And what does that mean?\n"
            voice "audio/voices/ch3/wraith/narrator/17.flac"
            n "'I' haven't met you, but you've clearly met 'me.' It sounds to me like you're hopping between parallel realities, in which case the 'me' you just met here is the same collection of experiences as the 'me' you met at all of those other beginnings, but their continuity breaks the moment you say or do anything, in effect making them all separate.\n"
            voice "audio/voices/ch3/wraith/narrator/17a.flac"
            n "So yes. I'm the same 'me', but ever since the moment we started talking, I'm different.\n"
            if trait_cold:
                voice "audio/voices/ch3/wraith/cold/17.flac"
                cold "I'm not sure how we're supposed to kill Him ourself, but He's asking for it. Maybe there's some way she can take care of him for us.\n"
            else:
                voice "audio/voices/ch3/wraith/opportunist/5.flac"
                opportunist "All the more reason to side with her, really. It takes a bullshit artist to recognize a bullshit artist, and I'm one of the best in the business. So trust me when I say He's full of it.\n"
            voice "audio/voices/ch3/wraith/narrator/18.flac"
            n "They've clearly all been through some harrowing experiences. Don't let their baggage influence your decisions. You have the ability to see things clearly. I suggest you use it.\n"
            jump wraith_woods_menu

        "{i}• (Explore) ''We've killed her and been killed by her, and neither of those things have gone well for us. If we're going to fall through this loop forever, eventually we're going to let her out. We might as well do it now.''{/i}" if wraith_woods_explore == False:
            $ wraith_woods_explore = True
            voice "audio/voices/ch3/wraith/narrator/19.flac"
            n "You're making a dizzying amount of assumptions. Your perceived reality looping twice before does not mean it will continue to do so forever.\n"
            voice "audio/voices/ch3/wraith/narrator/20.flac"
            n "Those little voices have already drawn attention to the fact that even the path is different. The world itself is at a tipping point.\n"
            voice "audio/voices/ch3/wraith/narrator/21.flac"
            n "Know that there is always a choice — even if you were stuck in an 'infinite' loop, there's no reason to assume the mere nature of the infinite would force you to make any specific choice. You do have free will, as much as things would be easier if you didn't, and you can just keep making the correct choice forever, never deviating.\n"
            if trait_cheated:
                voice "audio/voices/ch3/wraith/cheated/12.flac"
                cheated "How convenient, everything always comes back to what you want us to do! I'm sick of Him. Makes me want to end the world out of spite.\n"
            if trait_opportunist:
                voice "audio/voices/ch3/wraith/opportunist/6.flac"
                opportunist "Do you see how little authority He has? He's practically just begging us at this point. She at least takes what she wants. She's inspirational, really.\n"
            if trait_paranoid:
                voice "audio/voices/ch3/wraith/paranoid/8.flac"
                paranoid "Everyone is manipulating us. But we're starting to see the threads now. We just have to avoid getting tangled up in them...\n"
            if trait_cold and wraith_woods_loop_explore:
                voice "audio/voices/ch3/wraith/cold/18.flac"
                cold "On second thought, let's not kill Him. Let's throw Him someplace that never ends. I'd like to see what that does to Him.\n"
            jump wraith_woods_menu

        "{i}• (Explore) ''What happens if we don't go to the cabin? That's another option.''{/i}" if wraith_woods_leave_explore == False:
            $ wraith_woods_leave_explore = True
            voice "audio/voices/ch3/wraith/narrator/22.flac"
            n "Then she finds a way out on her own.\n"
            if trait_opportunist:
                voice "audio/voices/ch3/wraith/opportunist/7.flac"
                opportunist "So... it sounds to me like she's getting out no matter what we do. And I say aligning ourselves with somebody like her is clearly the better option. She's going places. Let's make our way to the cabin and demonstrate our value!\n"
            else:
                if trait_cheated:
                    voice "audio/voices/ch3/wraith/cheated/13.flac"
                    cheated "Ugh. Of course she does.\n"
                voice "audio/voices/ch3/wraith/cold/19.flac"
                cold "So standing around out here is the same as us letting her out.\n"
                voice "audio/voices/ch3/wraith/hero/12.flac"
                hero "Only we don't have to see her. That's got to be better, right?\n"
            voice "audio/voices/ch3/wraith/narrator/23.flac"
            n "No, it's strictly worse.\n"
            if trait_paranoid:
                voice "audio/voices/ch3/wraith/paranoid/9.flac"
                paranoid "And why is that?\n"
            else:
                voice "audio/voices/ch3/wraith/hero/13.flac"
                hero "But she can't kill us out here. Why would staying out of killing distance be worse if she's getting out regardless?\n"
            voice "audio/voices/ch3/wraith/narrator/24.flac"
            n "Because it's cowardly, for starters. And because the unknown is always worse than the known. But really, all you're doing right now is weighing two considerably bad options.\n"
            voice "audio/voices/ch3/wraith/narrator/25.flac"
            n "The only solution worth considering is slaying her, and whatever delusion is holding you back from doing that, is just that: a delusion. If you already managed to end her in some other world, the only reason you'd be here is that you somehow managed to do it wrong.\n"
            if trait_cheated:
                if wraith_woods_explore:
                    voice "audio/voices/ch3/wraith/cheated/14.flac"
                    cheated "How are we supposed to decide on anything if you just keep coming up with new rules? Since when is there a wrong way to slay her?!\n"
                else:
                    voice "audio/voices/ch3/wraith/cheated/15.flac"
                    cheated "More rules, more rhetoric! Since when is there a wrong way to slay her?! I'm sick of Him. Makes me want to end the world out of spite.\n" id wraith_woods_menu_596dc5eb
            jump wraith_woods_menu

        "{i}• [[Proceed to the cabin.]{/i}":
            voice "audio/voices/ch3/wraith/narrator/26.flac"
            n "You continue down the path towards the cabin.\n"
            jump wraith_cabin_arrive

        "{i}• [[Turn around and leave.]{/i}" if wraith_woods_leave_explore and mound_can_attempt_flee:
            jump wraith_woods_leave

        "{i}• ''There's something else we haven't tried...'' [[Turn around and leave.]{/i}" if wraith_woods_leave_explore == False and mound_can_attempt_flee:
            label wraith_woods_leave:
                if loops_finished >= 2:
                    $ mound_can_attempt_flee = False
                    voice "audio/voices/mound/bonus/flee.flac"
                    mound "You have already committed to my completion. You cannot go further astray.\n"
                    jump wraith_woods_menu
                $ caught_origin_ch3 = True
                voice "audio/voices/ch3/wraith/narrator/27.flac"
                n "I'm begging you, don't do this. You're going to damn everything to oblivion. You have to do something, you can't just walk away.\n"
                if trait_cold:
                    voice "audio/voices/ch3/wraith/cold/20.flac"
                    cold "Yet here we are. Walking away, despite your protestations.\n"
                    #cold "I wouldn't worry about it too much. If this doesn't work, then we'll just do something else next time.\n"
                if trait_cheated:
                    voice "audio/voices/ch3/wraith/cheated/16.flac"
                    cheated "You can only bend the rules so much, huh? You can talk all you want, but you can't really do much of anything, can you?\n"
                if trait_cold == False:
                    voice "audio/voices/ch3/wraith/hero/14.flac"
                    hero "I guess you'll just have to stop us, if you want us to go to the cabin so bad.\n"
                if trait_paranoid:
                    voice "audio/voices/ch3/wraith/paranoid/10.flac"
                    paranoid "There's got to be a crack in this world somewhere. If He's looking in at us, there has to be a way out.\n"
                if trait_opportunist:
                    voice "audio/voices/ch3/wraith/opportunist/8.flac"
                    opportunist "Oh, I agree. This is definitely the best thing for us to do.\n"
                    voice "audio/voices/ch3/wraith/hero/15.flac"
                    hero "Haven't you been suggesting we team up with the Princess?\n"
                    voice "audio/voices/ch3/wraith/opportunist/9a.flac"
                    opportunist "That was then! This is now. And besides, she'll always be there to set free if things go South.\n"
                play audio "audio/one_shot/footsteps_hike_short.flac"
                voice "audio/voices/ch3/wraith/narrator/28.flac"
                scene bg woods wraith onlayer back at flip, zoom_in
                show fore woods wraith onlayer front at flip, zoom_in
                with fade
                n "Ugh. Fine. You walk down the path away from the cabin. I hope for all of our sakes that you change your mind before it's too late.\n"
                jump caught_start


label wraith_cabin_arrive:

    $ gallery_wraith.unlock_item(2)
    $ renpy.save_persistent()
    play audio "audio/one_shot/footsteps_hike_short.flac"
    $ quick_menu = False
    hide bg onlayer back
    hide fore onlayer front
    scene bg black
    with fade
    scene farback wraith ext onlayer farback at Position(ypos=1125)
    show bg wraith ext onlayer back at Position(ypos=1125)
    show mid wraith ext onlayer front at Position(ypos=1125)
    show fore wraith ext onlayer inyourface at Position(ypos=1125)
    if persistent.quick_menu:
        $ quick_menu = True

    voice "audio/voices/ch3/wraith/narrator/29.flac"
    n "It isn't long before you're steps away from your destination. I don't think you need any words of warning. I think you know what's in there, and despite your protestations, I think you know what you need to do.\n"

    if trait_opportunist:
        voice "audio/voices/ch3/wraith/opportunist/10.flac"
        opportunist "Of course we do! We've been over it. Find the one in charge, and make sure she knows how helpful we are.\n"

    if trait_paranoid:
        voice "audio/voices/ch3/wraith/paranoid/11.flac"
        paranoid "I don't like any of our options here. It feels like we're being driven down the tracks to some awful inevitability. There must be a something we're missing, something that would make everything make sense.\n"
        voice "audio/voices/ch3/wraith/paranoid/12.flac"
        paranoid "Maybe letting her out really is the answer.\n"

    if trait_cheated:
        voice "audio/voices/ch3/wraith/cheated/17.flac"
        cheated "The more He talks, the more I'm interested in setting her free.\n"

    voice "audio/voices/ch3/wraith/narrator/30.flac"
    n "Whatever. You don't want to listen to me? Do it, then. Let her out. See what I care.\n"
    if trait_cold:
        voice "audio/voices/ch3/wraith/cold/21.flac"
        cold "It sounds like somebody's about to crack.\n"
    label wraith_cabin_ext_menu:
        default wraith_cabin_ext_explore = False
        menu:
            extend ""

            "{i}• (Explore) ''Are you trying to use reverse-psychology on me or have you just given up?''{/i}" if wraith_cabin_ext_explore == False:
                $ wraith_cabin_ext_explore = True
                voice "audio/voices/ch3/wraith/narrator/31.flac"
                n "There's obviously no point in trying to reason with you right now, especially with all of these clowns offering up their useless advice. Honestly it seems like the more I try and talk sense into you, the more single-minded they get about letting her out. So yes. I'm done trying to argue.\n"
                if trait_cold:
                    voice "audio/voices/ch3/wraith/cold/22.flac"
                    cold "Would you look at that? We won.\n"
                elif trait_paranoid:
                    voice "audio/voices/ch3/wraith/paranoid/13.flac"
                    paranoid "I wouldn't trust that if I were the one making decisions.\n"
                voice "audio/voices/ch3/wraith/narrator/32.flac"
                n "Take it however you will.\n"
                jump wraith_cabin_ext_menu

            "{i}• [[Enter the cabin.]{/i}":
                play audio "audio/one_shot/door_bedroom.flac"
                $ quick_menu = False
                hide farback onlayer farback
                hide bg onlayer back
                hide mid onlayer front
                hide fore onlayer inyourface
                scene bg black
                with fade
                jump wraith_cabin_interior

label wraith_cabin_interior:

    $ gallery_wraith.unlock_item(3)
    $ renpy.save_persistent()
    play secondary "audio/looping/uncomfortable ambiance.ogg" loop fadein 1.0
    scene farback wraith cabin onlayer farback at Position(ypos=1125)
    show bg wraith cabin onlayer back at Position(ypos=1125)
    show mirror wraith cabin onlayer back at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    voice "audio/voices/ch3/wraith/narrator/33.flac"
    n "The interior of the cabin is long and dark, a single narrow hallway stretching far into the distance. Curtains billow out from tall windows on either side, obscuring the path forward, fluttering helplessly as opposing gusts of wind rush into the building, clashing and joining and driving everything forward.\n"
    voice "audio/voices/ch3/wraith/narrator/34.flac"
    n "The only furniture of note is— hm. That's strange.\n"
    voice "audio/voices/ch3/wraith/hero/16.flac"
    hero "What's strange? Is it the mirror?\n"
    voice "audio/voices/ch3/wraith/narrator/35.flac"
    n "The mirror? No there isn't a mirror. What's strange is that there isn't much of anything in here at all aside from the curtains. There's supposed to be a pristine blade. Why isn't there a pristine blade?\n\n"
    if trait_cheated:
        voice "audio/voices/ch3/wraith/cheated/18.flac"
        cheated "Great. Something else has been taken away from us.\n"
    if trait_paranoid:
        if (wraith_source == "nightmare" and (nightmare_1_cabin_mirror_ask or nightmare_1_cabin_mirror_approached)) or (wraith_source == "spectre" and (spectre_1_cabin_mirror_ask or spectre_1_cabin_mirror_approached)):
            voice "audio/voices/ch3/wraith/paranoid/14a.flac"
            paranoid "Of course there 'isn't a mirror.' There 'wasn't one' last time either, so why would it be there this time.\n"
        else:
            voice "audio/voices/ch3/wraith/paranoid/15.flac"
            paranoid "What do you mean there isn't a mirror. There's a mirror, plain as day at the end of the hall.\n"
    if trait_cold:
        voice "audio/voices/ch3/wraith/cold/23.flac"
        cold "I suppose the only way to go is forward. So forward we will go. Blade or not, it doesn't really matter, does it?\n"
    if trait_opportunist:
        voice "audio/voices/ch3/wraith/opportunist/11.flac"
        opportunist "Let's be mindful of our position, boys. Without the knife, we lose part of our bargaining power. We should fold and beg for mercy as soon as we see her.\n"
        voice "audio/voices/ch3/wraith/hero/17.flac"
        hero "I'm sure we have too much self-respect to do something so... worm-like. Right? We can always at least pretend to have a conversation as equals. We did kill her last time.\n"
        voice "audio/voices/ch3/wraith/opportunist/12.flac"
        opportunist "Yeah, but she sort of let us do that, didn't she? And again. We don't have a blade.\n"
        voice "audio/voices/ch3/wraith/opportunist/13.flac"
        opportunist "And look at the bright side: at least everybody knows exactly where worms stand in the pecking order! At the bottom. Which is the most important part if you think about it, because it gives everybody else something to stand on. The bedrock, if you will.\n"
        voice "audio/voices/ch3/wraith/opportunist/14.flac"
        opportunist "She'll understand the value of that.\n"

label wraith_cabin_int_menu:
    default wraith_int_explore = False
    default wraith_surprise_comment = False
    menu:
        extend ""

        "{i}• (Explore) ''Let's pretend there is a mirror at the end of this hallway, and that right now, we can't see behind it. What's there? What's behind it?''{/i}" if wraith_int_explore == False:
            $ wraith_int_explore = True
            voice "audio/voices/ch3/wraith/narrator/36.flac"
            n "If you're asking what's at the end of the hallway, it's the way to the basement.\n"
            if trait_paranoid == False:
                voice "audio/voices/ch3/wraith/hero/18.flac"
                hero "The... {i}way{/i} to the basement? Don't you mean door?\n"
            if trait_paranoid:
                if wraith_source == "spectre":
                    voice "audio/voices/ch3/wraith/paranoid/16.flac"
                    paranoid "Are you saying there isn't a door? Are you saying that at the end of the hallway there's just an opening?\n"
                else:
                    voice "audio/voices/ch3/wraith/paranoid/16a.flac"
                    paranoid "Are you saying there isn't a door? Are you saying that at the end of the hallway there's just an opening again?\n"
                if trait_cold:
                    voice "audio/voices/ch3/wraith/cold/24.flac"
                    cold "He didn't say 'door,' did he?\n"
            voice "audio/voices/ch3/wraith/narrator/37.flac"
            n "No, I didn't say door. Because there isn't a door. It's just an opening.\n"
            if trait_paranoid:
                if wraith_source == "nightmare":
                    $ wraith_surprise_comment = True
                    voice "audio/voices/ch3/wraith/paranoid/17.flac"
                    paranoid "It's just like last time, isn't it? Only instead of a visible empty void, there's an invisible one. For all we know, she could be standing right there behind the mirror! For all we know, she's going to jump out at us and there's nothing we can do to stop her!\n"
            elif trait_cheated:
                $ wraith_surprise_comment = True
                voice "audio/voices/ch3/wraith/cheated/19a.flac"
                cheated "What are the odds she's waiting for us right behind it? If I were running a bullshit factory it's what I'd do.\n"

            if wraith_source == "nightmare" or trait_cheated:
                voice "audio/voices/ch3/wraith/narrator/38.flac"
                n "Let me assure you that there's nothing there. Nothing is going to 'jump out at you,' and certainly not the Princess. The Princess is in the basement.\n"
            if trait_opportunist:
                voice "audio/voices/ch3/wraith/opportunist/15.flac"
                opportunist "Oh, stop being such cowards, all of you. We know what we're going to do. We know what's going to happen to us. There's literally nothing to be afraid of.\n"
            if trait_cheated:
                voice "audio/voices/ch3/wraith/cheated/20.flac"
                cheated "He can't see the mirror. The knife is gone, defying His expectations. Who the hell is calling the shots here?\n"
                voice "audio/voices/ch3/wraith/narrator/39.flac"
                n "Nobody is calling the shots. That's how reality works.\n"
            jump wraith_cabin_int_menu

        "{i}• [[Approach the mirror.]{/i}":
            voice "audio/voices/ch3/wraith/narrator/40.flac"
            play audio "audio/one_shot/footsteps_creaky.flac"
            show farback wraith cabin onlayer farback at small_zoom
            show bg wraith cabin onlayer back at small_zoom
            show mirror wraith cabin onlayer back at small_zoom
            with dissolve
            n "You slowly make your way towards the gaping maw that awaits you. Your fraying nerves buzz with trepidation, the chill wind raising your hackles as it gently pushes you forward, towards the darkness at the end of the hallway. You can't shake the feeling that you're being watched.\n"
            play audio "audio/one_shot/footsteps_creaky.flac"
            show farback wraith cabin onlayer farback at big_zoom
            show bg wraith cabin onlayer back at big_zoom
            show mirror wraith cabin onlayer back at big_zoom
            with dissolve
            if trait_paranoid:
                voice "audio/voices/ch3/wraith/paranoid/18.flac"
                paranoid "Oh, do we? Do we feel like we're being watched? I hadn't noticed. At least you're admitting to it now.\n"
            elif trait_cold:
                voice "audio/voices/ch3/wraith/cold/25.flac"
                cold "We've always been watched. You're watching us right now. Sometimes the feeling is just stronger than others.\n"
            if trait_cheated:
                voice "audio/voices/ch3/wraith/cheated/21.flac"
                cheated "I feel like you're trying to put us on edge. We don't need all this anticipation, we just need this to be over.\n" id wraith_cabin_int_menu_a8f9be55
            if trait_opportunist:
                voice "audio/voices/ch3/wraith/opportunist/16.flac"
                opportunist "Who says being watched is a bad thing? If we haven't done anything wrong, we don't have anything to worry about. I'm sure she knows we're on her side.\n"
            voice "audio/voices/ch3/wraith/narrator/41.flac"
            play audio "audio/one_shot/footsteps_creaky.flac"
            hide farback onlayer farback
            hide bg onlayer back
            hide mirror onlayer back
            scene farback wraith close onlayer farback at Position(ypos=1125)
            show bg wraith close onlayer back at Position(ypos=1125)
            show mirror wraith close onlayer back at Position(ypos=1125)
            with Dissolve(1.0)
            n "You stop as you reach the end of the hallway, I presume in front of whatever mirror isn't actually there.\n"
            menu:
                extend ""

                "{i}• [[Wipe the mirror clean.]{/i}":
                    if wraith_surprise_comment == False:
                        if trait_paranoid:
                            voice "audio/voices/ch3/wraith/paranoid/19.flac"
                            paranoid "This is it. The mirror's going to go away, and she's going to startle us. We'd better brace ourselves...\n"
                        if trait_cheated:
                            voice "audio/voices/ch3/wraith/cheated/22.flac"
                            cheated "What are the odds she's waiting for us right now, just out of sight on the other side of that glass?\n"
                    else:
                        if trait_paranoid:
                            voice "audio/voices/ch3/wraith/paranoid/20.flac"
                            paranoid "I hate that I know what's about to happen. Knowing makes it so much worse.\n"
                        if trait_cheated:
                            voice "audio/voices/ch3/wraith/cheated/23.flac"
                            cheated "Here we go.\n"

                    stop music
                    play audio "audio/_music/ch3/wraith/Jump Scare.flac"
                    hide mirror onlayer back
                    voice "audio/voices/ch3/wraith/narrator/42.flac"
                    n "You reach your arm forward into the pitch black of the opening.\n"
                    if trait_paranoid:
                        voice "audio/voices/ch3/wraith/paranoid/21.flac"
                        paranoid "{i}Sigh of relief.{/i} Oh, that was a close one. All that stress and lead-up for nothing...\n"
                    elif trait_cheated:
                        voice "audio/voices/ch3/wraith/cheated/24.flac"
                        cheated "Nothing. Huh. It's like this place read our mind just to mess with us.\n"
                    play music "audio/_music/ch3/wraith/The Wraith II.flac" loop
                    if wraith_source == "nightmare":
                        voice "audio/voices/ch3/wraith/princess/1.flac"
                        spmid "Hopelessly staring into the void? I'm glad I made a lasting impression.\n"
                    else:
                        voice "audio/voices/ch3/wraith/princess/2.flac"
                        spmid "Whatcha looking at, killer? Staring into the void? Thinking about what it'd be like to die again? I know exactly how you feel.\n"
                    voice "audio/voices/ch3/wraith/hero/19.flac"
                    hero "Shit — where is she?!\n"
                    voice "audio/voices/ch3/wraith/narrator/43.flac"
                    play audio "audio/final/Spectre_PossessingPlayer_5.flac"
                    n "You feel something long and frigid coil around your ankle. Your heart skips a beat, standing in muted shock for one long, frozen moment, and then it—she, the Princess—constricts.\n"
                    voice "audio/voices/ch3/wraith/narrator/43a.flac"
                    play audio "audio/final/Nightmare_NeckCrack_1.flac"
                    n "Your bones snap.\n"
                    voice "audio/voices/ch3/wraith/narrator/44.flac"
                    play audio "audio/one_shot/collapse.flac"
                    hide bg onlayer back
                    hide farback onlayer farback
                    scene bg black
                    n "Icy pain radiates up from the break, a deep cold flooding your veins as your legs, numb with the shock of it, collapse, and you collapse with them.\n"
                    $ gallery_wraith.unlock_item(4)
                    $ renpy.save_persistent()
                    voice "audio/voices/ch3/wraith/narrator/45.flac"
                    scene farback wraith convo onlayer farback at swayblur, Position(ypos=1125)
                    show bg wraith convo onlayer back at swayblur, Position(ypos=1125)
                    show wraith neutral onlayer back at swayblur, Position(ypos=1125)
                    show player wraith convo onlayer back at swayblur, Position(ypos=1125)
                    with fade
                    n "You're met with the terrifying visage of the Princess. Her hand grips your leg in a steel vice, her grin carved jagged from ear-to-ear, crowded with far too many long and crooked teeth.\n"
                    hide farback onlayer farback
                    hide bg onlayer back
                    hide wraith onlayer back
                    hide player onlayer back
                    scene farback wraith convo onlayer farback at Position(ypos=1125)
                    show bg wraith convo onlayer back at Position(ypos=1125)
                    show wraith cock talk onlayer back at Position(ypos=1125)
                    show player wraith convo onlayer back at Position(ypos=1125)
                    with Dissolve(1.5)
                    if wraith_source == "nightmare":
                        voice "audio/voices/ch3/wraith/princess/3.flac"
                        sp "You killed me last time. And that was after you tried to lock me away forever. I was so, so close to freedom, but then you took my body away from me.\n"
                        voice "audio/voices/ch3/wraith/princess/4.flac"
                        show wraith laugh onlayer back
                        with dissolve
                        sp "So now I'm going to take yours, and I'm going to walk it out of here.\n"
                    else:
                        if spectre_end == "abandon":
                            voice "audio/voices/ch3/wraith/princess/5.flac"
                            sp "But do you know how I feel? I gave you a path to forgiveness. I gave you a chance to make things right. But you decided it'd be best to try and bury me all over again.\n"
                            voice "audio/voices/ch3/wraith/princess/6.flac"
                            show wraith laugh onlayer back
                            with dissolve
                            sp "You're not getting another chance to mess this up.\n"
                        else:
                            voice "audio/voices/ch3/wraith/princess/7.flac"
                            sp "But do you know how I feel? I gave you a path to forgiveness. I gave you a chance to make things right.\n"
                            voice "audio/voices/ch3/wraith/princess/8.flac"
                            show wraith wag anim onlayer back
                            with dissolve
                            sp "I thought maybe you'd see what you've done and feel remorseful, maybe try to make it up to me. But no... you'd rather use that knife to keep making the same mistake over and over and over.\n"
                            if spectre_kill_player_slay_attempt:
                                voice "audio/voices/ch3/wraith/princess/9.flac"
                                show wraith smile onlayer back
                                with dissolve
                                sp "Even after I ripped your heart out, you still cut me. And for what? I didn't go anywhere. You didn't banish me. I'm right back here with you, a little better, a little worse.\n"
                                voice "audio/voices/ch3/wraith/princess/10.flac"
                                show wraith laugh onlayer back
                                with dissolve
                                sp "Well... maybe a lot worse.\n"
                        voice "audio/voices/ch3/wraith/princess/11.flac"
                        show wraith smile talk onlayer back
                        with dissolve
                        sp  "So... here's how this is going to go. I'm going to take your body, and I'm going to walk it out of here.\n"
                    voice "audio/voices/ch3/wraith/princess/12.flac"
                    play audio "audio/final/Nightmare_NeckCrack_1.flac"
                    show wraith twist onlayer back
                    with dissolve
                    sp "And you! You get to watch me do it! Completely helpless. Just like you left me.\n"
                    jump wraith_convo_menu

label wraith_convo_menu:
    $ current_run_mirror_touched = True
    $ wraith_convo_count += 1
    if wraith_convo_count == 0:
        if trait_opportunist:
            voice "audio/voices/ch3/wraith/opportunist/17.flac"
            opportunist "Great! We're all on the same page then! The important part now is that we let her know that we're completely on-board with this.\n"
            voice "audio/voices/ch3/wraith/paranoid/22.flac"
            paranoid "Are we? She clearly hates us. I'm not sure letting her in is a good idea. Not like this.\n"
            voice "audio/voices/ch3/wraith/opportunist/18.flac"
            opportunist "Oh, don't have second thoughts! This has to happen. It's clearly the only way we save our skin and get out of here.\n"
            voice "audio/voices/ch3/wraith/narrator/46.flac"
            n "Ignore him. Have those second thoughts. Have them now!\n"
        elif trait_paranoid:
            voice "audio/voices/ch3/wraith/paranoid/23.flac"
            paranoid "Okay. Maybe letting her in isn't the best idea. She clearly hates us.\n"
            voice "audio/voices/ch3/wraith/cold/26.flac"
            cold "And? What's your point? I thought you wanted to get out of here. This is a way out, and it's different. We might as well take it.\n"
            voice "audio/voices/ch3/wraith/paranoid/24.flac"
            paranoid "Yeah. But not like {i}this{/i}. She's going to make it hurt.\n"
            voice "audio/voices/ch3/wraith/cold/27.flac"
            cold "Then turn off the part of you that feels things.\n"
            voice "audio/voices/ch3/wraith/hero/20.flac"
            hero "Oh, like it's that easy?\n"
            voice "audio/voices/ch3/wraith/cold/28.flac"
            cold "It is. Pain is just another sensation. If you can tolerate joy, you can tolerate pain.\n"
            voice "audio/voices/ch3/wraith/hero/21.flac"
            hero "Except that pain hurts!\n"
            voice "audio/voices/ch3/wraith/cold/29.flac"
            cold "Yes. That's what it does. That's the definition.\n"
            voice "audio/voices/ch3/wraith/paranoid/25.flac"
            paranoid "Do we need to explain to you why pain is bad?\n"
            voice "audio/voices/ch3/wraith/cold/30.flac"
            cold "You need to explain to yourself why it isn't.\n"
        elif trait_cold:
            voice "audio/voices/ch3/wraith/cold/31.flac"
            cold "I say we let her do it. It's something different.\n"
            voice "audio/voices/ch3/wraith/cheated/25.flac"
            cheated "Do we even have a choice?\n"
            voice "audio/voices/ch3/wraith/narrator/47.flac"
            n "You always have a choice.\n"
            voice "audio/voices/ch3/wraith/hero/22.flac"
            hero "Maybe before, but not now. There isn't a blade this time.\n"
            voice "audio/voices/ch3/wraith/cheated/26.flac"
            cheated "Exactly! What choice is there if there isn't a blade?\n"
            voice "audio/voices/ch3/wraith/cold/32.flac"
            cold "Well, unless you have any specific ideas, I think my vote's the only one that counts.\n"

    if wraith_convo_count >= 2:
        voice "audio/voices/ch3/wraith/princess/13.flac"
        show wraith smile onlayer back
        with dissolve
        sp "Enough talking. We'll have plenty of time for chit chat once this place is far behind us.\n"
        jump wraith_possession
    default wraith_consent = False
    default wraith_convo_count = -1
    default wraith_consent_explore = False
    default wraith_water_bridge_explore = False
    default wraith_never_hurt_want = False
    default wraith_victim_explore = False
    default wraith_no_better_explore = False
    default wraith_barter_explore = False
    default wraith_struggle = False
    menu:
        extend ""

        "{i}• (Explore) ''I thought you couldn't possess me on your own. I thought I needed to agree to it.''{/i}" if spectre_possession_no_wont and wraith_consent_explore == False:
            $ wraith_consent_explore = True
            voice "audio/voices/ch3/wraith/princess/14.flac"
            show wraith furious onlayer back
            with dissolve
            sp "That was then. This is now.\n"
            jump wraith_convo_menu

        "{i}• (Explore) ''Look, we're even now. I killed you, and then you killed me. Water under the bridge, right?''{/i}" if wraith_source == "spectre" and wraith_water_bridge_explore == False:
            $ wraith_water_bridge_explore = True
            voice "audio/voices/ch3/wraith/princess/15.flac"
            show wraith laugh onlayer back
            with dissolve
            sp "And you think that's even? How adorable.\n"
            if spectre_end == "abandon":
                voice "audio/voices/ch3/wraith/princess/16.flac"
                show wraith furious onlayer back
                with dissolve
                sp "But I think you forgot about the part where you tried leaving me to rot.\n"
            else:
                voice "audio/voices/ch3/wraith/princess/17.flac"
                show wraith furious onlayer back
                with dissolve
                sp "But I think you forgot about the part where you tried killing me again.\n"
            label wraith_even_join:
                voice "audio/voices/ch3/wraith/princess/18.flac"
                show wraith neutral talk onlayer back
                with dissolve
                sp "If I were you, I would just want to just get it over with! You lost your chance to call the shots, there's no going back to fix it now. You can either look on in horror or celebrate my freedom, but either way, you're about to become a passenger.\n"
            jump wraith_convo_menu

        "{i}• (Explore) ''Look, we're even now. You killed me, and then I killed you. Water under the bridge, right?''{/i}" if wraith_source == "nightmare" and wraith_water_bridge_explore == False:
            $ wraith_water_bridge_explore = True
            voice "audio/voices/ch3/wraith/princess/19a.flac"
            show wraith smile onlayer back
            with dissolve
            sp "I think you forgot something... like the part where all this started when you left me to languish in a pit all by myself. Now I've become something so much worse, and it's all! Thanks! To you!\n"
            jump wraith_even_join

        "{i}• (Explore) ''I never wanted to hurt you. I don't even know how I got here!''{/i}" if wraith_never_hurt_want == False:
            $ wraith_never_hurt_want = True
            voice "audio/voices/ch3/wraith/princess/20.flac"
            play audio "audio/final/Nightmare_NeckCrack_1.flac"
            show wraith twist onlayer back
            with dissolve
            sp "But you did hurt me. Twice, even. And I'm not letting you do it again.\n"
            jump wraith_convo_menu

        "{i}• (Explore) ''I'm a victim in all of this too, you know!''{/i}" if wraith_victim_explore == False:
            $ wraith_victim_explore = True
            voice "audio/voices/ch3/wraith/princess/21.flac"
            show wraith wag anim onlayer back
            with dissolve
            sp "And sometimes victims become the same as their victimizers. Just because someone hurt you doesn't mean you get a free pass.\n"
            show wraith neutral onlayer back
            with dissolve
            if trait_paranoid:
                voice "audio/voices/ch3/wraith/paranoid/26.flac"
                paranoid "Funny how she says that like it's a bad thing when it's exactly what she's doing right now.\n"
                voice "audio/voices/ch3/wraith/hero/23.flac"
                hero "Something tells me pointing out the irony wouldn't do much to help us.\n"
            voice "audio/voices/ch3/wraith/princess/22.flac"
            show wraith furious onlayer back
            with dissolve
            sp "You should be grateful that I still have a use for you. Being mine is more than you deserve, really.\n"
            jump wraith_convo_menu

        "{i}• (Explore) ''Wouldn't possessing me against my will make you no better than me? You don't have to be evil. You don't have to do this.''{/i}" if wraith_no_better_explore == False:
            $ wraith_no_better_explore = True
            voice "audio/voices/ch3/wraith/hero/24.flac"
            hero "Ooh, that's a good one.\n"
            #if trait_cold:
                #voice "audio/voices/ch3/wraith/cold/33.flac"
                #cold "Yes, real smart.\n"
            voice "audio/voices/ch3/wraith/princess/23.flac"
            show wraith laugh onlayer back
            with dissolve
            sp "Evil is all about perspective. After all you've done, why would I ever care about what you think of me?\n"
            jump wraith_convo_menu


        "{i}• (Explore) ''Do you {b}need{/b} to take my body? Can't I just... open the door for you?''{/i}" if wraith_barter_explore == False:
            $ wraith_barter_explore = True
            if wraith_source == "nightmare" and trait_opportunist:
                voice "audio/voices/ch3/wraith/princess/24.flac"
                show wraith furious onlayer back
                with dissolve
                sp "Oh? You mean like last time?\n"
            elif wraith_source == "nightmare":
                voice "audio/voices/ch3/wraith/princess/25.flac"
                show wraith furious onlayer back
                with dissolve
                sp "You locked me in a basement and then you killed me.\n"
            else:
                voice "audio/voices/ch3/wraith/princess/26.flac"
                show wraith furious onlayer back
                with dissolve
                sp "I don't think you get the magnitude of hatred that sits between us. You've broken more trust than I thought I had.\n"
            voice "audio/voices/ch3/wraith/princess/27.flac"
            show wraith neutral onlayer back
            with dissolve
            sp "We're past the point of compromise. I'm taking your body, and there's nothing you can do to stop me.\n"
            jump wraith_convo_menu

        "{i}• ''Okay. Fine. Just do it.''{/i}" if wraith_convo_count != 0:
            label wraith_consent_join:
                $ wraith_consent = True
                if wraith_source == "spectre":
                    voice "audio/voices/ch3/wraith/princess/28.flac"
                    show wraith neutral talk onlayer back
                    with dissolve
                    sp "Great. See you in a jiffy.\n"
                else:
                    voice "audio/voices/ch3/wraith/princess/29.flac"
                    show wraith neutral talk onlayer back
                    with dissolve
                    sp "See? That wasn't so hard! And maybe this'll make it hurt a little less.\n"
                    voice "audio/voices/ch3/wraith/princess/30.flac"
                    show wraith cock onlayer back
                    with dissolve
                    sp "Maybe.\n"
                jump wraith_possession

        "{i}• ''That's fine. I actually came here to free you.''{/i}" if wraith_convo_count == 0:
            jump wraith_consent_join

        "{i}• [[Struggle.]{/i}":
            $ wraith_struggle = True
            voice "audio/voices/ch3/wraith/narrator/48.flac"
            play audio "audio/final/Nightmare_NeckCrack_1.flac"
            show wraith twist onlayer back
            with dissolve
            n "You violently struggle against the Princess, but all you manage to do is grind the fragments of your splintered ankle together. You can't shake free from her now.\n"
            voice "audio/voices/ch3/wraith/princess/31.flac"
            show wraith furious onlayer back
            with dissolve
            sp "It's so easy to make you squirm. But I won't be crueler than I have to be. Wouldn't want to cause any more damage. It'll be hard enough for me to walk out of here on that broken ankle.\n"
            jump wraith_possession


label wraith_possession:

    $ gallery_wraith.unlock_item(5)
    $ renpy.save_persistent()
    voice "audio/voices/ch3/wraith/narrator/49.flac"
    play audio "audio/final/Spectre_PossessingPlayer_2.flac"
    show player wraith emerge onlayer back
    show wraith full emerge onlayer back
    with Dissolve(1.0)
    n "You remain pinned to the floor of the long hallway as the rest of the Princess' body emerges — her proportions all wrong, limbs bent and curling, moving in ways that defy your understanding.\n"
    voice "audio/voices/ch3/wraith/narrator/50.flac"
    play audio "audio/final/Witch_TreeWrap_1.flac"
    hide player onlayer back
    hide wraith onlayer back
    show player wraith emerge onlayer back at Position(ypos=1125)
    show wraith full emerge2 onlayer back at Position(ypos=1125)
    with Dissolve(1.0)
    n "Her torso stretches until her face is practically touching yours, her neck cracking audibly as she twists to look at you from a fresh angle.\n"
    voice "audio/voices/ch3/wraith/hero/25.flac"
    hero "Are you sure you can't do anything to help us? Can't you like, manifest a rock right on top of her head?\n"
    voice "audio/voices/ch3/wraith/narrator/51.flac"
    n "And crush you along with her? Not that I even can 'manifest a rock.' Besides, I thought you all {i}wanted{/i} to free the Princess.\n"
    voice "audio/voices/ch3/wraith/hero/26.flac"
    hero "Not like this!\n"
    voice "audio/voices/ch3/wraith/narrator/52.flac"
    n "You don't even have a weapon. So I'm afraid you're out of luck, which unfortunately means that I—and the rest of the world—are out of luck too.\n"
    if trait_cheated:
        voice "audio/voices/ch3/wraith/cheated/27.flac"
        cheated "And whose fault is it that there isn't a weapon here?\n"
        voice "audio/voices/ch3/wraith/narrator/53.flac"
        n "Yours, I assume. There's supposed to be a pristine blade. Whatever you did in those previous lives of yours, you really messed up.\n"
        voice "audio/voices/ch3/wraith/hero/27.flac"
        hero "Are you seriously trying to blame this on us?\n"
    if trait_opportunist:
        voice "audio/voices/ch3/wraith/opportunist/19.flac"
        opportunist "Look, she's mad at us! I get it! But it's nothing we can't clear up after she possesses our body. Don't worry, I'm what you might call a smooth-talker. I'll iron things out.\n"
        voice "audio/voices/ch3/wraith/hero/28.flac"
        hero "Oh, will you now? With her like {b}that{/b}?\n"
        voice "audio/voices/ch3/wraith/narrator/54.flac"
        n "Good luck with that. It doesn't seem like she's too keen on forgiveness.\n"
    if trait_paranoid:
        voice "audio/voices/ch3/wraith/paranoid/27.flac"
        paranoid "Okay. Deep breath. This is fine. This is fine. This is FINE.\n"
        if wraith_source == "nightmare":
            voice "audio/voices/ch3/wraith/hero/29.flac"
            hero "Is it? Is there any conceivable way that this is fine?\n"
            voice "audio/voices/ch3/wraith/paranoid/28.flac"
            paranoid "Yeah. I'm right. This is fine. It's better than last time. At least our organs aren't failing. At least I can actually {i}talk{/i}.\n"
        else:
            voice "audio/voices/ch3/wraith/paranoid/29.flac"
            paranoid "What am I talking about? This isn't fine. It was better when she was a normal ghost.\n"
        if trait_cold:
            voice "audio/voices/ch3/wraith/cold/34.flac"
            cold "It is fine. Everything is always fine. These consequences have no real impact on us outside of momentary discomfort. I'm sure we'll be moving on again soon enough.\n"

    stop music
    voice "audio/voices/ch3/wraith/narrator/55.flac"
    stop sound fadeout 2.0
    play audio "audio/final/Spectre_PossessingPlayer_1.flac"
    hide wraith onlayer back
    show wraith possession anim onlayer inyourface at Position(ypos=1125)
    with Dissolve(1.0)
    n "Your vision fades as she tears open the membrane of your soul.\n"
    voice "audio/voices/ch3/wraith/princess/s1.flac"
    play music "audio/_music/ch3/wraith/The Wraith III.flac"
    spmid "GET UP.\n"
    voice "audio/voices/ch3/wraith/narrator/56.flac"
    hide wraith onlayer inyourface
    hide farback onlayer farback
    hide bg onlayer back
    hide player onlayer back
    scene farback wraith possessed 2 onlayer farback at swayblur, Position(ypos=1125)
    show bg wraith possessed 1 onlayer back at swayblur, Position(ypos=1125)
    show player wraith possessed 1 onlayer back at swayblur, Position(ypos=1125)
    with Dissolve(1.0)
    n "You're awake, eyes once again fixed on the long hallway, your vision swimming as the Princess' command reverberates inside your skull. Her voice is all-encompassing. You feel... wrong.\n"
    voice "audio/voices/ch3/wraith/princess/s2.flac"
    hide farback onlayer farback
    hide bg onlayer back
    hide player onlayer back
    hide player onlayer front
    show farback wraith possessed 2 onlayer farback at Position(ypos=1125)
    show bg wraith possessed 1 onlayer back at Position(ypos=1125)
    show player wraith possessed 1 onlayer back at Position(ypos=1125)
    with Dissolve(1.0)
    spmid "I SAID GET UP.\n"
    voice "audio/voices/ch3/wraith/hero/30a.flac"
    hero "It's so cramped in here. Like there's some sort of growth, trying to push us all out.\n"
    voice "audio/voices/ch3/wraith/narrator/57.flac"
    play audio "audio/final/Nightmare_NeckCrack_1.flac"
    play audio "audio/one_shot/footsteps_creaky.flac"
    hide farback onlayer farback
    hide bg onlayer back
    hide player onlayer back
    show farback wraith possessed 2 onlayer farback at Position(ypos=1125)
    show bg wraith possessed 2 onlayer back at Position(ypos=1125)
    with Dissolve(2.0)
    n "I know. You rise to your feet, though the pain in your ankle is blinding. Your body slumps against the wall, desperately leaning into it for support.\n"
    if wraith_consent:
        jump wraith_end_free
    if trait_opportunist:
        voice "audio/voices/ch3/wraith/opportunist/20.flac"
        opportunist "The two of you are being incredibly rude. Hi! Hello! Welcome! I live here, along with him and him, and, well, I've never been clear on whether or not He lives here.\n"
        voice "audio/voices/ch3/wraith/paranoid/30.flac"
        paranoid "I don't think this is helping. We should try to keep a low profile.\n"
        voice "audio/voices/ch3/wraith/princess/s3.flac"
        spmid "YES THAT ONE IS RIGHT THIS ISN'T HELPING YOU. IT'S TOO LATE FOR ANYTHING TO HELP YOU.\n"
        voice "audio/voices/ch3/wraith/opportunist/21.flac"
        opportunist "I just want to tell you how great a job you're doing! You're a real go-getter. Really seizing destiny by the throat and making it yours. It's the kind of gumption a guy can really admire.\n"
        voice "audio/voices/ch3/wraith/princess/s4.flac"
        spmid "YOU STABBED ME IN THE BACK.\n"
        voice "audio/voices/ch3/wraith/opportunist/22.flac"
        opportunist "That was then! This is now. I'm a big fan of winners, and you're the biggest winner around.\n"
        voice "audio/voices/ch3/wraith/princess/s5.flac"
        spmid "DO YOU THINK IF YOU ARE NICE TO ME NOW THAT I WILL FORGET WHAT YOU'VE DONE TO ME? I HAVE ALREADY TAKEN THE ONLY THING I NEED!\n"
        voice "audio/voices/ch3/wraith/opportunist/23a.flac"
        opportunist "I'll have you know that as soon as we wound up back in the woods on this go-around, {i}I{/i} suggested that we free you. I'm on your side!\n"
        voice "audio/voices/ch3/wraith/princess/s6.flac"
        spmid "YOU'RE ONLY ON MY SIDE UNTIL YOU THINK YOU CAN STAB ME IN THE BACK AGAIN. BUT THAT IS NEVER GOING TO HAPPEN.\n"
        voice "audio/voices/ch3/wraith/opportunist/24.flac"
        opportunist "At the end of the day, I just want a job. I figure if He's right and you're going to end the world, there's gotta be something else coming after all that. And I want to make sure I have a place helping you run it!\n"
        voice "audio/voices/ch3/wraith/hero/31a.flac"
        hero "I think you should stop talking.\n"
        voice "audio/voices/ch3/wraith/princess/s7.flac"
        spmid "NO, HE SHOULD KEEP SAYING THESE THINGS. I LIKE TO FEEL YOU WRITHE IN DISCOMFORT.\n"
        voice "audio/voices/ch3/wraith/opportunist/25.flac"
        opportunist "Look, all I'm saying is that 'whatever comes after' is going to be a hefty management task. You don't want to do that alone! And I—no, {b}we{/b}—are the only people you know. Possibly the only people left alive once you've done whatever it is you're going to do. So you'll have to hire us.\n"
        voice "audio/voices/ch3/wraith/paranoid/31.flac"
        paranoid "We're going to die. No, we're going to do something worse than dying. She is going to torture us out of existence and it's all going to be your fault.\n"
        jump wraith_reap_join

    elif trait_cheated:
        voice "audio/voices/ch3/wraith/cheated/28.flac"
        cheated "There's another option, you know.\n"
        voice "audio/voices/ch3/wraith/princess/s8.flac"
        spmid "OH? AND WHAT'S THAT.\n"
        voice "audio/voices/ch3/wraith/cheated/29.flac"
        cheated "Don't. Help. Either of them. Flip the table.\n"
        voice "audio/voices/ch3/wraith/princess/s9a.flac"
        spmid "AND HOW WOULD YOU DO THAT? YOU DON'T HAVE A WILL TO WIELD. YOUR SOUL HAS BEEN DRAINED OF COURAGE.\n"
        voice "audio/voices/ch3/wraith/cheated/30a.flac"
        cheated "That gap where the mirror was. I don't think it goes anywhere. Let's throw ourselves into the abyss.\n"

    else:
        voice "audio/voices/ch3/wraith/cold/35.flac"
        cold "It's rather rude to show up in somebody else's body and boss it around like this.\n"
        if wraith_source == "spectre":
            voice "audio/voices/ch3/wraith/princess/s10.flac"
            spmid "AND IT IS RUDE TO MURDER.\n"
        else:
            voice "audio/voices/ch3/wraith/princess/s11.flac"
            spmid "AND IT IS RUDE TO LOCK SOMEBODY AWAY IN A DARK DARK BASEMENT FOREVER. IT IS RUDE TO LEAVE SOMEBODY TO ROT.\n"
        voice "audio/voices/ch3/wraith/hero/32a.flac"
        hero "We were going to let you out of here! That's the whole reason we marched all the way back up to the cabin.\n"
        #making sure 'here' isn't confused for a typo for 'there', making sure it's known the reference is to this current timeline and not the previous
        voice "audio/voices/ch3/wraith/cold/36.flac"
        cold "Were we?\n"
        voice "audio/voices/ch3/wraith/hero/33.flac"
        hero "I was!\n"
        voice "audio/voices/ch3/wraith/princess/s12.flac"
        spmid "I KNOW YOU WERE. BUT YOU WERE GOING TO DO IT FOR THE WRONG REASONS.\n"
        voice "audio/voices/ch3/wraith/hero/34.flac"
        hero "And what reasons are those supposed to be? Nobody should be able to be judge, jury, and executioner.\n"
        #edited for clarity
        voice "audio/voices/ch3/wraith/princess/s13.flac"
        spmid "WEREN'T YOU ALL OF THOSE THINGS FOR ME?\n"
        voice "audio/voices/ch3/wraith/princess/s14.flac"
        spmid "I CAN GRASP THE SHAPE OF EVERYTHING YOU THINK AND FEEL. YOU THINK YOU ARE NUMB, BUT YOU ARE HOPELESS AND PARANOID. YOU ARE AFRAID OF ME.\n"
        voice "audio/voices/ch3/wraith/princess/s15.flac"
        spmid "AND I DON'T FEEL REGRET, EVEN IN THE RECESSES OF YOUR SOUL. THERE IS NOT A DROP OF SYMPATHY TO BE FOUND.\n"
        #added even so it feels like she looked more thoroughly
        voice "audio/voices/ch3/wraith/hero/35.flac"
        hero "We weren't always like this, we—\n{w=2.0}{nw}"
        show screen disableclick(0.5)
        voice "audio/voices/ch3/wraith/cold/37.flac"
        cold "I've always been like this.\n"
        label wraith_reap_join:
            voice "audio/voices/ch3/wraith/princess/s16.flac"
            spmid "ALL I'M DOING IS REAPING WHAT YOU'VE SOWN.\n"
            voice "audio/voices/ch3/wraith/paranoid/32.flac"
            paranoid "We don't have to let her out. I've been storing up a little bit of will since she forced her way in here. Take it and throw us all into the basement. It's better than giving her what she wants.\n"

    voice "audio/voices/ch3/wraith/princess/s17.flac"
    spmid "YOU WOULDN'T DARE! MOVE! NOW!\n"
    voice "audio/voices/ch3/wraith/narrator/58.flac"
    play audio "audio/final/Nightmare_NeckCrack_1.flac"
    show bg wraith possessed 2 onlayer back at spectre_small_zoom, Position(ypos=1125)
    with dissolve
    n "Your body, still slumped against the wall, trapped between the Princess' overwhelming will and the blinding pain of your splintered ankle, takes an excruciating step towards the cabin door. The movement is stiff, your body reduced to a marionette, pulled reluctantly along by your strings.\n"
    voice "audio/voices/ch3/wraith/princess/s18.flac"
    spmid "IT'S NOT THAT BAD. THE PAIN FEELS GOOD. BECAUSE I KNOW YOU FEEL IT TOO.\n"

    menu:
        extend ""

        "{i}• [[Leave the cabin.]{/i}":
            jump wraith_end_free

        "{i}• [[Throw your body into the abyss.]{/i}":
            jump wraith_end_fall


label wraith_end_free:

    if wraith_consent:
        voice "audio/voices/ch3/wraith/narrator/59.flac"
        n "I'd beg you to resist, but you've already surrendered your will to her, haven't you?\n"
        if trait_paranoid:
            voice "audio/voices/ch3/wraith/paranoid/33.flac"
            paranoid "You're the puppet master here. If this is the only way we could cut ourselves free from you, so be it.\n"
        if trait_cheated:
            voice "audio/voices/ch3/wraith/cheated/31.flac"
            cheated "Anything to get out of this hellhole.\n"
        if trait_opportunist:
            voice "audio/voices/ch3/wraith/opportunist/26.flac"
            opportunist "Yeah. Just like I told you we would. We're here to make things right, and the first step in making things right is admitting when you're wrong.\n"
        if trait_cold:
            voice "audio/voices/ch3/wraith/cold/38.flac"
            cold "It's a new experience. You should try being possessed some time. There's nothing else like it.\n"
        voice "audio/voices/ch3/wraith/princess/s19.flac"
        spmid "THERE'S NOTHING WRONG WITH FIXING YOUR MISTAKES. I'LL REMEMBER THIS. BUT I'LL ALSO NEVER FORGET WHAT YOU'VE DONE.\n"

    else:
        $ gallery_wraith.unlock_item(8)
        $ renpy.save_persistent()
        voice "audio/voices/ch3/wraith/narrator/60.flac"
        n "{i}Sigh.{/i} You toss the last of your will aside and surrender to the Princess.\n"
        if trait_cheated:
            voice "audio/voices/ch3/wraith/cheated/32.flac"
            cheated "Shit.\n"
        voice "audio/voices/ch3/wraith/hero/36.flac"
        hero "I guess that's that.\n"
        if trait_opportunist:
            voice "audio/voices/ch3/wraith/opportunist/27.flac"
            opportunist "It's for the best, really.\n"
        if trait_paranoid:
            voice "audio/voices/ch3/wraith/paranoid/34.flac"
            paranoid "Maybe we'll find our freedom on the other side.\n"
        if trait_cold:
            voice "audio/voices/ch3/wraith/cold/39.flac"
            cold "An end is an end. Let's see what it has in store for us.\n"
        voice "audio/voices/ch3/wraith/princess/s20.flac"
        spmid "THIS IS ALL I WANTED. MAYBE THERE WILL BE A MERCY FOR YOU AT THE END OF EVERYTHING.\n"
        if trait_opportunist:
            voice "audio/voices/ch3/wraith/opportunist/28.flac"
            opportunist "You hear that, boys? A mercy. That's the sort of reward you get with me at the helm.\n"
    voice "audio/voices/ch3/wraith/narrator/61.flac"
    play audio "audio/final/Nightmare_NeckCrack_1.flac"
    play tertiary "audio/one_shot/footsteps_creaky.flac"
    hide farback onlayer farback
    hide bg onlayer back
    scene farback wraith free move onlayer farback at Position(ypos=1125)
    show bg wraith free move 2 onlayer back at Position(ypos=1125)
    with Dissolve(1.0)
    n "Your body inches along the corridor, every step more difficult and painful than the last — your joints stiff and unresponsive, the shattered bones of your ankle grinding ceaselessly, as if they're fragmenting then reforming then snapping all over again as you make your way towards the outside world.\n"
    voice "audio/voices/ch3/wraith/princess/s21.flac"
    spmid "WE'RE SO SO SO SO SO SO CLOSE.\n"
    voice "audio/voices/ch3/wraith/narrator/62.flac"
    play audio "audio/final/Nightmare_NeckCrack_1.flac"
    play tertiary "audio/one_shot/footsteps_creaky.flac"
    show bg wraith free move 1 onlayer back at Position(ypos=1125)
    with Dissolve(1.0)
    n "But despite the anguish, it doesn't feel like the exit to the cabin is getting any closer. If anything, it's getting further away.\n"
    voice "audio/voices/ch3/wraith/princess/s22.flac"
    play audio "audio/final/Nightmare_NeckCrack_1.flac"
    play tertiary "audio/one_shot/footsteps_creaky.flac"
    show bg wraith free move 2 onlayer back at Position(ypos=1125)
    with Dissolve(1.0)
    spmid "IT DOESN'T MATTER HOW LONG THIS HALLWAY IS. I WILL DRAG THIS BODY UNTIL IT IS A PASTE OF MEAT AND FEATHERS. I WILL BE FREE.\n"
    voice "audio/voices/ch3/wraith/hero/37.flac"
    hero "Please. Just let her out.\n"
    voice "audio/voices/ch3/wraith/princess/s23.flac"
    spmid "YES. LET. ME. OUT.\n"
    voice "audio/voices/ch3/wraith/narrator/63.flac"
    play tertiary "audio/one_shot/footsteps_creaky.flac"
    show bg wraith free move 1 onlayer back at Position(ypos=1125)
    with Dissolve(1.0)
    n "It's pointless, isn't it? I can't stop her without you, and you'd already given up by the time we met...\n"
    voice "audio/voices/ch3/wraith/narrator/63a.flac"
    play audio "audio/one_shot/door_stone.flac"
    show bg wraith free move 3 onlayer back at Position(ypos=1125)
    with Dissolve(1.0)
    n "No, no, screw that, the hallway gets even longer!\n"
    voice "audio/voices/ch3/wraith/princess/s24.flac"
    hide farback onlayer farback
    hide bg onlayer back
    show farback wraith free door onlayer farback at Position(ypos=1125)
    show bg wraith free door onlayer back at Position(ypos=1125)
    spmid "YOU CANNOT DESCRIBE ME INTO SUBMISSION. THE DOOR IS RIGHT THERE.\n"
    voice "audio/voices/ch3/wraith/narrator/64.flac"
    n "{i}Sigh.{/i} It really is, isn't it?\n"
    voice "audio/voices/ch3/wraith/princess/s25.flac"
    play audio "audio/final/Nightmare_NeckCrack_1.flac"
    play tertiary "audio/one_shot/footsteps_creaky.flac"
    show farback wraith free door onlayer farback at zoom_in
    show bg wraith free door onlayer back at zoom_in
    with dissolve
    spmid "I WALK TO IT.\n"
    voice "audio/voices/ch3/wraith/princess/s26.flac"
    play audio "audio/one_shot/thump_2.flac"
    show player wraith free door onlayer back at zoom_instant, Position(ypos=1125)
    with Dissolve(1.0)
    spmid "I PLACE YOUR BLOODY HAND ON THE DOOR.\n"
    voice "audio/voices/ch3/wraith/princess/s27.flac"
    play audio "audio/one_shot/lock_click.flac"
    hide player onlayer back
    show player wraith free door twist onlayer back at zoom_instant, Position(ypos=1125)
    spmid "I MAKE YOU TWIST THE HANDLE.\n"
    voice "audio/voices/ch3/wraith/hero/38.flac"
    hero "Isn't saying all of this His job?\n"
    voice "audio/voices/ch3/wraith/princess/s28.flac"
    spmid "HE IS GONE.\n"
    if trait_opportunist:
        voice "audio/voices/ch3/wraith/opportunist/29.flac"
        opportunist "Don't worry about all the criticism. You're doing great!\n"
        voice "audio/voices/ch3/wraith/princess/s29.flac"
        sp "THANK YOU.\n"
    elif trait_cold:
        voice "audio/voices/ch3/wraith/cold/40.flac"
        cold "Oh, He really is, isn't He? I had a feeling you could deal with Him for us.\n"
        voice "audio/voices/ch3/wraith/princess/s30.flac"
        sp "I DID NOTHING. HE DEALT WITH HIMSELF.\n"
    voice "audio/voices/ch3/wraith/hero/39.flac"
    hero "This is it, then. The big moment.\n"
    if trait_paranoid:
        voice "audio/voices/ch3/wraith/paranoid/35.flac"
        paranoid "Finally, we'll get to see what's {i}really{/i} out there.\n"
    if trait_cheated:
        voice "audio/voices/ch3/wraith/cheated/33.flac"
        cheated "I just hope it's a way out.\n"

    $ quick_menu = False
    voice "audio/voices/ch3/wraith/princess/s31.flac"
    stop sound fadeout 20.0
    stop secondary fadeout 20.0
    stop tertiary fadeout 20.0
    play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 20.0
    stop music fadeout 20.0
    stop music2 fadeout 20.0
    stop music3 fadeout 20.0
    stop music4 fadeout 20.0
    hide bg onlayer back
    hide farback onlayer farback
    hide player onlayer back
    scene bg black
    with fade
    show farback quiet onlayer farback at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    spmid "THE HANDLE CLICKS AND WE PUSH FORWARD. THE AIR IS DIFFERENT HERE.\n"
    $ achievement.grant("ACH_PASSENGER")
    play audio "audio/final/Assorted_TapestyUnraveledBreakingRip_1.flac"
    show wraith free separate onlayer front at Position(ypos=1125)
    with Dissolve(1.0)
    truth "But as you step outside the bounds of the cabin, you feel another violent tear, a rending that cuts all the way down to your soul.\n"
    play audio "audio/final/Spectre_PossessingPlayer_5.flac"
    show wraith free separate distant onlayer front at Position(ypos=1125)
    with Dissolve(1.0)
    truth "You are once again separated from everything that had nestled in the deep crevices of your body, from everything that isn't you.\n"
    voice "audio/voices/ch3/wraith/hero/40a.flac"
    hero "We're us again.\n"
    if trait_cold:
        voice "audio/voices/ch3/wraith/cold/41.flac"
        cold "How interesting.\n"
    if trait_opportunist:
        voice "audio/voices/ch3/wraith/opportunist/30.flac"
        opportunist "Couldn't have planned it better myself.\n"
    if trait_paranoid:
        voice "audio/voices/ch3/wraith/paranoid/36.flac"
        paranoid "Everything is gone except her.\n"
    if trait_opportunist:
        voice "audio/voices/ch3/wraith/opportunist/31.flac"
        opportunist "Which means we made it to the end of the world. We're survivors.\n"
    if trait_cheated:
        voice "audio/voices/ch3/wraith/cheated/34.flac"
        cheated "We actually won, didn't we?\n"
    $ gallery_wraith.unlock_item(6)
    $ renpy.save_persistent()
    voice "audio/voices/ch3/wraith/princess/s32.flac"
    show wraith free separate cold onlayer front at Position(ypos=1125)
    with dissolve
    sp "Wh-what?! What's happening to me?\n"
    play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
    show arms wraith1 onlayer back at Position(ypos=1125)
    with Dissolve(1.0)
    $ renpy.pause(0.2)
    show wraith free separate quiet onlayer front at Position(ypos=1125)
    show arms wraith2 onlayer back at Position(ypos=1125)
    with Dissolve(1.0)
    $ renpy.pause(0.2)
    hide wraith onlayer front
    show arms wraith3 onlayer back at Position(ypos=1125)
    with Dissolve(1.0)
    $ renpy.pause(0.2)
    show arms wraith4 onlayer back at Position(ypos=1125)
    with Dissolve(0.5)
    $ renpy.pause(0.125)
    hide arms onlayer back
    with Dissolve(0.5)
    $ renpy.pause(0.125)
    $ blade_held = False
    $ default_mouse = "default"
    hide farback onlayer back
    hide quiet onlayer back
    hide bg onlayer farback
    hide grey onlayer inyourface
    hide mid onlayer back
    hide bg onlayer front
    hide farback onlayer farback
    hide bg onlayer back
    hide fore onlayer front
    hide fore onlayer inyourface
    hide stars onlayer farback
    hide back onlayer back
    hide quiet onlayer front
    hide mid onlayer front
    hide mid onlayer back
    hide midground onlayer back
    hide front onlayer front
    hide bg onlayer farback
    hide front onlayer inyourface
    hide quiet onlayer inyourface
    show farback quiet onlayer farback at Position(ypos=1125)
    with Dissolve(4.0)
    show mirror quiet distant onlayer back at Position(ypos=1125)
    if loops_finished != 0:
        truth "But you don't answer her before she's gone. Memory returns.\n"
    else:
        truth "But you don't have the chance to answer her before something takes her and leaves something else in her place.\n"
    $ wraith_end = "free"
    $ princess_free += 1
    $ princess_deny += 1
    jump mirror_start
    # END


label wraith_end_fall:

    voice "audio/voices/ch3/wraith/narrator/65.flac"
    play audio "audio/one_shot/hard tighten.flac"
    play tertiary "audio/one_shot/footsteps_creaky.flac"
    hide farback onlayer farback
    hide bg onlayer back
    show bg wraith exorcism onlayer back at Position(ypos=1125)
    show fore wraith exorcism onlayer front at Position(ypos=1125)
    with Dissolve(1.0)
    n "In a single moment of overwhelming willpower, you tear your body from the wall and hurl it towards the gaping abyss.\n"
    voice "audio/voices/ch3/wraith/princess/s33.flac"
    spmid "I WON'T LET YOU DO THIS!\n"
    voice "audio/voices/ch3/wraith/narrator/66.flac"
    n "Capillaries burst and muscle fibers tear as you and the Princess struggle over the reins of your body, one foot planted firmly on the edge where the floor ends and the nothing begins. It's unquestionable that her reserves are greater than yours, but fortunately for you, the distance you have to cover is far shorter.\n"
    if trait_opportunist:
        voice "audio/voices/ch3/wraith/opportunist/32.flac"
        opportunist "Now this is just embarrassing. I would have made sure all of you had cushy jobs on the other side of this, but you're going to make it impossible to patch things up.\n"
        voice "audio/voices/ch3/wraith/princess/s34.flac"
        spmid "I WILL DEVOUR YOU!\n"
        voice "audio/voices/ch3/wraith/paranoid/37.flac"
        paranoid "It's now or never! No doubt! Just make it happen!\n"

    elif trait_cheated:
        voice "audio/voices/ch3/wraith/cheated/35.flac"
        cheated "Enough is enough! I'm tired of us always losing! It's. Just. A step. AWAY!\n"
        voice "audio/voices/ch3/wraith/princess/s35.flac"
        spmid "EVEN IF YOU THROW YOURSELF INTO THE ABYSS, YOU STILL LOSE!\n"

    elif trait_cold:
        voice "audio/voices/ch3/wraith/hero/41.flac"
        hero "We're putting in everything we have.\n"
        voice "audio/voices/ch3/wraith/cold/42.flac"
        cold "You're not. You're thinking too much about how she's hurting us. You're thinking too much about your body. It's just a body.\n"
        voice "audio/voices/ch3/wraith/princess/s36.flac"
        spmid "YES IT'S JUST A BODY NOW BUT I CAN MAKE IT DO SO MANY TERRIBLE THINGS TO YOU!\n"
        voice "audio/voices/ch3/wraith/paranoid/38.flac"
        paranoid "One, two, three. One, two three. Next one, we all go. One, two, three.\n"

    $ gallery_wraith.unlock_item(7)
    $ renpy.save_persistent()
    $ achievement.grant("ACH_EXORCIST_III")
    $ quick_menu = False
    voice "audio/voices/ch3/wraith/narrator/67.flac"
    play audio "audio/final/Nightmare_NeckCrack_1.flac"
    play tertiary "audio/one_shot/footstep_run_medium.flac"
    queue tertiary "audio/final/den_emerge.flac"
    hide bg onlayer back
    hide fore onlayer front
    scene bg black
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    n "You throw everything you have against her and manage, for one brief moment, to overpower the Princess' hold on your body. But that moment was all you needed. Your foot slips a few inches, and you collapse forward, the darkness swallowing you whole.\n"
    voice "audio/voices/ch3/wraith/princess/s37.flac"
    play sound "audio/final/Nightmare_Falling_1_Loop.flac" loop
    show farback falling forever onlayer farback at Position(ypos=1125)
    with dissolve
    spmid "WHY DO YOU HATE ME?\n"
    voice "audio/voices/ch3/wraith/narrator/68.flac"
    n "Her thought slips through you, unheeded, as you fall, and fall, and fall.\n"
    voice "audio/voices/ch3/wraith/princess/s38.flac"
    spmid "HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA HAHAHAHAHAHAHAHA HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA\n"
    if trait_opportunist:
        voice "audio/voices/ch3/wraith/opportunist/33.flac"
        opportunist "I thought we already fell forever.\n"
        voice "audio/voices/ch3/wraith/paranoid/39.flac"
        paranoid "Yes, but now we're falling with her. She doesn't get an easy way out this time. Just like we didn't get an easy way out last time.\n"
    elif trait_cheated:
        voice "audio/voices/ch3/wraith/cheated/36.flac"
        cheated "What an end. But at least it's ours.\n"
        voice "audio/voices/ch3/wraith/cold/43.flac"
        cold "An empire of frigid nothing.\n"
    else:
        voice "audio/voices/ch3/wraith/paranoid/40.flac"
        paranoid "Hahaha! We did it! We actually did it!\n"
        voice "audio/voices/ch3/wraith/cold/44.flac"
        cold "Yes, we've really shown them all, haven't we?\n"

    voice "audio/voices/ch3/wraith/narrator/69.flac"
    n "I don't think this qualifies as saving the world, but at least you didn't ruin it.\n"
    voice "audio/voices/ch3/wraith/hero/42.flac"
    hero "What happens now?\n"
    voice "audio/voices/ch3/wraith/princess/s39.flac"
    spmid "WHAT DO YOU MEAN WHAT HAPPENS NOW YOU WANTED THIS.\n"
    voice "audio/voices/ch3/wraith/hero/43.flac"
    hero "But I want to know what He thinks happens now.\n"
    voice "audio/voices/ch3/wraith/princess/s40.flac"
    spmid "I DON'T THINK YOU'RE GOING TO FIND THAT OUT.\n"
    if trait_paranoid:
        voice "audio/voices/ch3/wraith/paranoid/41.flac"
        paranoid "Why? What do you know that you're not telling us?\n"
    else:
        voice "audio/voices/ch3/wraith/cold/45.flac"
        cold "Oh? And why's that?\n"

    stop sound fadeout 20.0
    stop secondary fadeout 20.0
    stop tertiary fadeout 20.0
    play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 20.0
    stop music fadeout 20.0
    stop music2 fadeout 20.0
    stop music3 fadeout 20.0
    stop music4 fadeout 20.0
    voice "audio/voices/ch3/wraith/princess/s41.flac"
    show quiet creep1 onlayer back at Position(ypos=1125)
    with Dissolve(1.0)
    spmid "YOU SHOULD PAY BETTER ATTENTION TO YOUR HEAD. HE LEFT. GONE. IT'S JUST YOU AND YOU AND YOU AND ME.\n"
    voice "audio/voices/ch3/wraith/princess/s42.flac"
    show quiet creep2 onlayer back at Position(ypos=1125)
    with Dissolve(1.0)
    spmid "IDIOT.\n"
    if trait_cheated:
        # FAST
        voice "audio/voices/ch3/wraith/cheated/37.flac"
        cheated "He's gone...? But—\n{w=2.5}{nw}"
        show screen disableclick(0.5)

    show quiet creep3 onlayer back at Position(ypos=1125)
    play audio "audio/final/Assorted_TapestyUnraveledBreakingRip_1.flac"
    show wraith free separate onlayer front at xflip, Position(ypos=1125)
    with Dissolve(1.0)
    $ renpy.pause(0.5)
    show wraith free separate distant onlayer front at xflip, Position(ypos=1125)
    with Dissolve(1.0)
    truth "Terminal velocity ceases, and you feel a something—a mass, a growth—torn out of you. You and the Princess look at each other for a short moment.\n"
    voice "audio/voices/ch3/wraith/princess/s43.flac"
    show wraith free separate cold onlayer front at xflip, Position(ypos=1125)
    with dissolve
    sp "Wh-what?! What's happening to me?\n"
    play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
    show arms wraith1 onlayer back at xflip, Position(ypos=1125)
    with Dissolve(1.0)
    $ renpy.pause(0.2)
    show wraith free separate quiet onlayer front at xflip, Position(ypos=1125)
    show arms wraith2 onlayer back at xflip, Position(ypos=1125)
    with Dissolve(1.0)
    $ renpy.pause(0.2)
    hide wraith onlayer front
    show arms wraith3 onlayer back at xflip, Position(ypos=1125)
    with Dissolve(1.0)
    $ renpy.pause(0.2)
    show arms wraith4 onlayer back at xflip, Position(ypos=1125)
    with Dissolve(0.5)
    $ renpy.pause(0.125)
    hide arms onlayer back
    with Dissolve(0.5)
    $ renpy.pause(0.125)
    $ blade_held = False
    $ default_mouse = "default"
    hide farback onlayer back
    hide quiet onlayer back
    hide bg onlayer farback
    hide grey onlayer inyourface
    hide mid onlayer back
    hide bg onlayer front
    hide farback onlayer farback
    hide bg onlayer back
    hide fore onlayer front
    hide fore onlayer inyourface
    hide stars onlayer farback
    hide back onlayer back
    hide quiet onlayer front
    hide mid onlayer front
    hide mid onlayer back
    hide midground onlayer back
    hide front onlayer front
    hide bg onlayer farback
    hide front onlayer inyourface
    hide quiet onlayer inyourface
    show farback quiet onlayer farback at Position(ypos=1125)
    with Dissolve(4.0)
    show mirror quiet distant onlayer back at Position(ypos=1125)
    if loops_finished != 0:
        truth "But you don't answer her before she's gone and you feel a resistance underneath your feet once more. Memory returns.\n"
    else:
        truth "But you don't answer her before something takes her and leaves something in her place. You feel a force underneath your feet once more.\n"
    #end
    $ wraith_end = "slay"
    $ princess_kept += 1
    $ princess_deny += 2
    jump mirror_start
    # END



return
