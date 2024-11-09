label happy_start:

    default happy_smitten_gone_noticed = False
    default happy_mirror_prev = False


    if damsel_1_cabin_mirror_ask or damsel_1_cabin_mirror_approached:
        $ happy_mirror_prev = True

    stop music
    stop sound
    stop secondary
    $ default_mouse = "default"
    $ blade_held = False
    $ current_loop = 2
    $ quick_menu = False
    $ config.menu_include_disabled = False
    $ trait_smitten = False

    play sound "audio/_pristine/sfx/Happy Nice Castle AMB_2_loop.flac" loop fadein 1.0
    scene chapter happy with fade
    show text _("{color=#FFFFFF00}Epilogue. Happily Ever After.{/color}") at Position(ypos=850)
    $ renpy.pause(4.0)

    $ gallery_happy.unlock_gallery()
    $ renpy.save_persistent()

    stop sound

    play music "audio/_pristine/music/happy/Q-Full Intro.flac"
    queue music "audio/_pristine/music/happy/Q-Full Scratch.flac" loop
    $ current_princess = "happy"
    $ happy_encountered = True
    $ gallery_happy.unlock_item(1)
    $ renpy.save_persistent()
    $ trait_smitten = False
    scene bg black
    scene bg happy downstairs onlayer back at Position(ypos=1125)
    show mirror happy downstairs onlayer back at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    voice "audio/voices/ch3/thorn/narrator/1.flac"
    n "You're on a path in the woods—\n{w=1.9}{nw}"
    show screen disableclick(0.5)
    voice "audio/_pristine/voice/happy/hero/11.flac"
    hero "Mate, we're clearly already in the cabin.\n"
    voice "audio/_pristine/voice/happy/narrator/16.flac"
    n "Excuse me? You're clearly... oh. Huh. So you are. How do you know about the cabin? I didn't get to the cabin part of my opening monologue yet.\n"
    voice "audio/_pristine/voice/happy/hero/12.flac"
    hero "We've been here before. Well, not {i}here{/i} here, but I'm sure you know what I'm talking about. You knew about the looping last time.\n"
    if trait_opportunist:
        voice "audio/_pristine/voice/happy/opportunist/1.flac"
        opportunist "Now, now, He's clearly disorientated. I'm sure all this new info is going to come as quite a shock to Him. Best if we're gentle.\n"
    elif trait_paranoid:
        voice "audio/_pristine/voice/happy/paranoid/1.flac"
        paranoid "Not that he was eager to {i}divulge{/i} that.\n"
    voice "audio/_pristine/voice/happy/hero/13.flac"
    hero "And right on cue, here's the new guy! Welcome!\n"
    if trait_opportunist:
        voice "audio/_pristine/voice/happy/opportunist/2.flac"
        opportunist "Thank you, thank you! I'm just happy to be here.\n"
    elif trait_paranoid:
        voice "audio/_pristine/voice/happy/paranoid/2.flac"
        paranoid "I can't say I'm happy to be here. This is a bad place, all stale and wrong, can't you feel it?\n"
    voice "audio/_pristine/voice/happy/narrator/17.flac"
    n "Okay, yes, I get it. You've been here before. That's terrible. You know that, right? Because the only reason you would have been here before is if you failed in whatever world you'd come from. Meaning you doomed an entire other reality. But I'm sure since you're so well-traveled you know that, yes?\n"
    if trait_opportunist:
        voice "audio/_pristine/voice/happy/opportunist/3a.flac"
        opportunist "Well, we know that now, thanks to you! We're all so lucky to be stuck with... erm, {i}working with{/i}, someone so well-informed! You can count on us to do things right from here on out.\n"
        #voice "audio/_pristine/voice/happy/narrator/18.flac"
        #n "While I appreciate your 'can-do' attitude, I can't say the fact that you've been here, what, two times...?\n"
        #voice "audio/_pristine/voice/happy/hero/14.flac"
        #hero "Three.\n"
        #voice "audio/_pristine/voice/happy/narrator/19.flac"
        #n "Three. {i}Great{/i}. I can't say the fact you've been here {i}three{/i} times inspires much hope in your decision-making capabilities.\n"
        #voice "audio/_pristine/voice/happy/opportunist/4.flac"
        #opportunist "And that's exactly why you shouldn't worry! I'm new, remember? And things are definitely going to change for the better on my watch.\n"
    if trait_paranoid:
        $ happy_smitten_gone_noticed = True
        voice "audio/_pristine/voice/happy/paranoid/3.flac"
        paranoid "We know that you keep telling us that, but we've never seen a world end. As far as I'm concerned, that whole conversation is just {i}noise{/i}. And I'm stuck on a better question. Where's the {i}other one{/i}?\n"
        voice "audio/_pristine/voice/happy/narrator/20.flac"
        n "The {i}other one{/i}?\n"
        voice "audio/_pristine/voice/happy/paranoid/4.flac"
        paranoid "Yeah. A certain lovesick fool has been suspiciously quiet. One might even say {i}absent{/i}.\n"
        voice "audio/_pristine/voice/happy/hero/15.flac"
        hero "Oh. You're right. It's a little quiet here, isn't it? Maybe that's... one of the rules. Maybe only one 'bonus voice' is allowed to be here at a time.\n"
        voice "audio/_pristine/voice/happy/paranoid/5.flac"
        paranoid "'Bonus voice?' I'm just as important as you are.\n"
        voice "audio/_pristine/voice/happy/hero/16.flac"
        hero "I'm not saying it's a bad thing! All I'm saying is that it's my third time here, and it's your first. You're not unwelcome, but from my perspective, you're definitely bonus.\n"
        #voice "audio/_pristine/voice/happy/narrator/21.flac"
        #n "{i}Sigh{/i}. Focus up, will you? As much as I'd love to be in a reality where you can all bicker away until the sun rises free of consequence, that is {i}not{/i} the reality we inhabit. But if we all work together, maybe we can make that reality happen.\n"
    voice "audio/_pristine/voice/happy/narrator/22.flac"
    n "I'm going to describe the room now.\n"
    voice "audio/_pristine/voice/happy/narrator/23.flac"
    n "The interior of the cabin is vast and regal. High-arched windows line the walls, their multicolored glass casting kaleidoscopic patterns across the stone floor. An iron chandelier hangs from the vaulted ceiling, its many candles lit with flickering light, vaguely illuminating the massive room. This is a house fit for royalty.\n"
    voice "audio/_pristine/voice/happy/narrator/24.flac"
    n "Before you, there's... there isn't a blade, is there? That's not good.\n"

label happy_down_menu:
    default happy_down_blade_explore = False
    default happy_down_mirror_explore = False
    default happy_down_leave_attempt = False
    default happy_down_count = 0
    menu:
        extend ""

        "{i}• (Explore) Does it matter if the blade's here? We didn't use it last time, and the time before that she used it to kill us.{/i}" if happy_down_blade_explore == False:
            $ happy_down_blade_explore = True
            $ happy_down_count += 1
            if trait_paranoid:
                voice "audio/_pristine/voice/happy/paranoid/6.flac"
                paranoid "I see your point, but it's still an option that's been taken away from us. I don't like losing options.\n"
                voice "audio/_pristine/voice/happy/narrator/25.flac"
                n "Yes, and it's an important one. It's your implement. You're going to need it if you want to do this right. And the fact that you're here, right now, {i}again{/i}, means that you have not yet done this right.\n"
            if trait_opportunist:
                voice "audio/_pristine/voice/happy/opportunist/5.flac"
                opportunist "Now that is some fine reasoning. Who cares about the blade? I think you're right! We're better off without it. It's not like it's ever been important.\n"
                voice "audio/_pristine/voice/happy/narrator/26.flac"
                n "{i}Sigh{/i}. Of course the blade's important! It's your implement. You're going to need it if you want to do this right. And the fact that you're here, right now, {i}again{/i}, means that you have not yet done this right.\n"
            voice "audio/_pristine/voice/happy/hero/17a.flac"
            hero "But it's not there is it? We don't even get the choice. So what are we supposed to do?\n"
            voice "audio/_pristine/voice/happy/narrator/27.flac"
            n "I... don't actually know. I'm sure it'll turn up somewhere. It has to. It's part of the whole structure of this place, I think. At the very least it's important.\n"
            jump happy_down_menu

        "{i}• (Explore) Hey, where's 'The Voice of the Smitten?' He was here last time. And it's not like him to be this quiet.{/i}" if happy_smitten_gone_noticed == False:
            $ happy_down_count += 1
            $ happy_smitten_gone_noticed = True
            voice "audio/_pristine/voice/happy/hero/18.flac"
            hero "Yeah, he was a bit of a loud one, wasn't he? Is he okay?\n"
            voice "audio/_pristine/voice/happy/opportunist/6.flac"
            opportunist "We're better off without him, if you ask me. One less opinion we have to contend with. Plus, he's the one who got us into this whole mess.\n"
            voice "audio/_pristine/voice/happy/narrator/28.flac"
            n "Is that so? Maybe there is hope for you after all, free from the bad influence of your missing friend.\n"
            jump happy_down_menu

        "{i}• (Explore) ''So none of you are going to talk about the mirror?''{/i}" if happy_down_mirror_explore == False:
            $ happy_down_mirror_explore = True
            if trait_opportunist:
                voice "audio/_pristine/voice/happy/opportunist/7.flac"
                opportunist "What is there to say about it? It's a mirror.\n"
                voice "audio/_pristine/voice/happy/narrator/29.flac"
                n "Is this some sort of a bit? There is no mirror. There's only the stained glass windows, the empty table where your blade {i}should{/i} be, and the door to the basement.\n"
                voice "audio/_pristine/voice/happy/opportunist/8.flac"
                opportunist "Oh. My bad. {i}That's{/i} why I haven't been talking about it.\n"
                if happy_mirror_prev:
                    voice "audio/_pristine/voice/happy/hero/19.flac"
                    hero "{i}I{/i} see it. Just like I saw it last time.\n"
                else:
                    voice "audio/_pristine/voice/happy/hero/20.flac"
                    hero "{i}I{/i} see it.\n"
                voice "audio/_pristine/voice/happy/opportunist/9.flac"
                opportunist "Good for you, buddy! You've got a sharp set of eyes on you.\n"
            elif trait_paranoid:
                voice "audio/_pristine/voice/happy/paranoid/7.flac"
                paranoid "Oh, I see it. I've just been preoccupied with {i}everything else{/i} going on. Like the fact that we can rip our own heart out without deciding that's what we're going to do!\n"
                voice "audio/_pristine/voice/happy/narrator/30.flac"
                n "Is that what happened to you last time? How did that even work? You'd better not do it again!\n"
                voice "audio/_pristine/voice/happy/hero/21.flac"
                hero "Lucky for you, the one who did it is the one who's gone.\n"
                voice "audio/_pristine/voice/happy/narrator/31.flac"
                n "Wonderful. Moving on. I have no idea what you're talking about. There is no mirror. There's only the stained glass windows, the empty table where your blade {i}should{/i} be, and the door to the basement.\n"
                if happy_mirror_prev:
                    voice "audio/_pristine/voice/happy/hero/22.flac"
                    hero "You said that last time, too, but that hasn't stopped it from showing up again.\n"
                    voice "audio/_pristine/voice/happy/paranoid/8.flac"
                    paranoid "Or moving.\n"
                else:
                    voice "audio/_pristine/voice/happy/hero/23.flac"
                    hero "Well, there it is! Right in the middle of the room.\n"
                    voice "audio/_pristine/voice/happy/paranoid/9.flac"
                    paranoid "It feels like it's watching us.\n"
            voice "audio/_pristine/voice/happy/narrator/32.flac"
            n "Mirror or no mirror, the door to the basement—your only way forward—is just on the other side of the room. How about you walk over there?\n"
            jump happy_down_menu


        "{i}• [[Approach the mirror.]{/i}":
            $ quick_menu = False
            play audio "audio/one_shot/footsteps_stone.flac"
            if happy_down_mirror_explore:
                voice "audio/_pristine/voice/happy/narrator/33.flac"
                hide bg onlayer back
                hide mirror onlayer back
                scene bg happy mirror door onlayer back at Position(ypos=1125)
                show mirror happy close onlayer back at Position(ypos=1125)
                with fade
                if persistent.quick_menu:
                    $ quick_menu = True
                n "You cross the room, stopping just in front of the door to the basement. What, is this about that supposed mirror?  Just... reach forward and fumble around a bit. I'm sure you'll find the handle.\n"
                if happy_mirror_prev:
                    voice "audio/_pristine/voice/happy/hero/24a.flac"
                    hero "Well, shall we have a look at ourselves? Maybe it won't go away this time.\n"
                else:
                    voice "audio/_pristine/voice/happy/hero/25.flac"
                    hero "Well, shall we have a look at ourselves?\n"
            else:
                voice "audio/_pristine/voice/happy/narrator/34a.flac"
                hide bg onlayer back
                hide mirror onlayer back
                scene bg happy mirror door onlayer back at Position(ypos=1125)
                show mirror happy close onlayer back at Position(ypos=1125)
                with fade
                if persistent.quick_menu:
                    $ quick_menu = True
                n "You cross the room, stopping just in front of the door to the basement. The handle is right there. Do feel free to give it a push as soon as you'd like.\n" id happy_down_menu_629c9b6c
                if happy_mirror_prev:
                    voice "audio/_pristine/voice/happy/hero/26.flac"
                    hero "He couldn't see it last time, I'm sure that hasn't changed. Let's just do our thing, and if it disappears again, it disappears again.\n"
                    if trait_paranoid:
                        voice "audio/_pristine/voice/happy/paranoid/10.flac"
                        paranoid "About last time: could He really not see it, or could he 'not see it?'\n"
                        voice "audio/_pristine/voice/happy/hero/27.flac"
                        hero "I'm not sure that actually matters.\n"
                        voice "audio/_pristine/voice/happy/narrator/35a.flac"
                        n "See what? What are you all on about?\n"
                        voice "audio/_pristine/voice/happy/hero/28.flac"
                        hero "N-nothing.\n"
                    else:
                        voice "audio/_pristine/voice/happy/narrator/35.flac"
                        n "See what? What are you on about?\n"
                        voice "audio/_pristine/voice/happy/opportunist/10.flac"
                        opportunist "Oh! I think I know this one! It's either a mirror, or... it's nothing! Depends who you ask.\n"
                        voice "audio/_pristine/voice/happy/narrator/36.flac"
                        n "What?\n"
                        voice "audio/_pristine/voice/happy/hero/29.flac"
                        hero "Just ignore him.\n"
                else:
                    voice "audio/_pristine/voice/happy/hero/30.flac"
                    hero "There is no door. There's a mirror.\n"
                    voice "audio/_pristine/voice/happy/narrator/37.flac"
                    n "No there isn't.\n"
                    if trait_paranoid:
                        voice "audio/_pristine/voice/happy/paranoid/11.flac"
                        paranoid "What a strange thing to lie about.\n"
                        voice "audio/_pristine/voice/happy/narrator/38.flac"
                        n "That's because I'm not lying. Look, if you need help, just raise your hand and I'll guide it where it needs to go.\n"
                    else:
                        voice "audio/_pristine/voice/happy/opportunist/11.flac"
                        opportunist "Hmmm. Now this is tricky. My eyes say there's a mirror, but my {i}brain{/i} says there isn't one.\n"
                        voice "audio/_pristine/voice/happy/narrator/39.flac"
                        n "Look, if you need help, just raise your hand and I'll guide it where it needs to go.\n"

            menu:

                extend ""

                "{i}• [[Reach forward.]{/i}":
                    voice "audio/_pristine/voice/happy/narrator/40a.flac"
                    hide mirror onlayer back
                    play audio "audio/one_shot/new/STP_claws_1.flac"
                    show player happy mirror onlayer back at Position(ypos=1125) with dissolve
                    n "You reach forward, your hand instinctively wrapping around the handle.\n"
                    if happy_mirror_prev:
                        voice "audio/_pristine/voice/happy/hero/31.flac"
                        hero "Figures...\n"
                    else:
                        voice "audio/_pristine/voice/happy/hero/32.flac"
                        hero "It's gone...\n"
                        if trait_opportunist:
                            voice "audio/_pristine/voice/happy/opportunist/12.flac"
                            opportunist "I'm just glad that we can all agree on a shared reality!\n"
                        else:
                            voice "audio/_pristine/voice/happy/paranoid/12.flac"
                            paranoid "I don't like things disappearing on us. I don't like how... fluid reality seems to be.\n"
                            voice "audio/_pristine/voice/happy/hero/33.flac"
                            hero "Neither do I.\n"
                    $ quick_menu = False
                    play audio "audio/one_shot/door_bedroom.flac"
                    voice "audio/_pristine/voice/happy/narrator/40b.flac"
                    hide player onlayer back
                    hide bg onlayer back
                    with fade
                    n "And then you push the door open. Marvelous. We can proceed.\n"
                    jump happy_stairs

        "{i}• [[Turn around and leave.]{/i}" if happy_down_leave_attempt == False:
            $ happy_down_leave_attempt = True
            $ quick_menu = False
            voice "audio/_pristine/voice/happy/narrator/41.flac"
            play audio "audio/one_shot/footsteps_stone.flac"
            hide bg onlayer back
            hide mirror onlayer back
            scene bg black
            with fade
            n "As you foolishly turn to leave the cabin and abandon the world to it's ruination, you're...\n" id happy_down_menu_e815528f
            voice "audio/_pristine/voice/happy/narrator/42.flac"
            $ quick_menu = False
            scene bg happy no exit onlayer back at Position(ypos=1125)
            with fade
            if persistent.quick_menu:
                $ quick_menu = True
            n "Oh, isn't that convenient? As you turn around you're faced with a solid wall. There isn't a way out. It would appear that you're stuck here until you find a resolution to our Princess problem.\n"
            if trait_paranoid:
                voice "audio/_pristine/voice/happy/paranoid/13.flac"
                paranoid "Yes. It's very convenient, isn't it?\n"
                voice "audio/_pristine/voice/happy/narrator/43.flac"
                n "I assure you, I'm just as surprised as you are. Can't you hear the relief in my voice? I wouldn't be relieved if I was the one who set this up. I would have known you were stuck here from the beginning.\n"
            elif trait_opportunist:
                voice "audio/_pristine/voice/happy/opportunist/13.flac"
                opportunist "That {i}is{/i} convenient! Look at us, crossing-off a whole avenue of exploration. Figuring out the rest of this is going to be so much easier now that we only have one way left to go.\n"
                voice "audio/_pristine/voice/happy/narrator/44.flac"
                n "You know, I'm starting to like you.\n"
                voice "audio/_pristine/voice/happy/hero/34.flac"
                hero "Because he's blowing smoke up your ass?\n"
                voice "audio/_pristine/voice/happy/narrator/45.flac"
                n "Because he's being reasonable.\n"
            voice "audio/_pristine/voice/happy/narrator/46.flac"
            n "Look, it doesn't matter who put that wall there, because it's there. The only thing for you to do now is find the Princess, and ideally find your weapon while you're at it.\n"
            voice "audio/_pristine/voice/happy/narrator/47.flac"
            play audio "audio/one_shot/footsteps_stone.flac"
            $ quick_menu = False
            hide bg onlayer back
            scene bg happy downstairs onlayer back at Position(ypos=1125)
            show mirror happy downstairs onlayer back at Position(ypos=1125)
            with fade
            if persistent.quick_menu:
                $ quick_menu = True
            n "With nowhere to go but forward, you turn back around, leaving the nonexistent exit behind you.\n"
            jump happy_down_menu


label happy_stairs:

    voice "audio/_pristine/voice/happy/narrator/48.flac"
    scene bg happy stairs onlayer back at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    n "It would seem that the stairs to the basement don't lead to a basement at all. Rather, they... go up. They're draped in a fine carpet, too, one that feels pleasantly soft against your feet.\n"
    voice "audio/_pristine/voice/happy/narrator/49.flac"
    n "If the Princess lives here, slaying her would probably— Ugh. Agh. No, that doesn't work here at all. This place is nice. It's fancy, even! I have to say, whatever you did in your previous lives, I deeply dislike how much it's thrown me off my rhythm.\n"
    if trait_opportunist:
        voice "audio/_pristine/voice/happy/opportunist/14.flac"
        opportunist "Don't worry about it, boss! You're doing great.\n"
        voice "audio/_pristine/voice/happy/narrator/50.flac"
        n "I'm not. But I appreciate the encouragement.\n"
    voice "audio/_pristine/voice/happy/hero/35a.flac"
    hero "Well, if all of this has thrown you off your rhythm so much, then maybe we... don't? Have to slay the Princess?\n"
    if happy_down_leave_attempt:
        voice "audio/_pristine/voice/happy/narrator/51.flac"
        n "No, you absolutely do. Just because she lives in a nice, exit-less house doesn't mean that she doesn't pose a direct threat to all of reality. It's in her very nature.\n"

    else:
        voice "audio/_pristine/voice/happy/narrator/52.flac"
        n "No, you absolutely do. Just because she lives in a nice house doesn't mean she doesn't pose a direct threat to all of reality. It's in her very nature.\n"

    if trait_paranoid:
        voice "audio/_pristine/voice/happy/paranoid/14.flac"
        paranoid "Am I the only one who remembers how much she {i}changed{/i} last time? Does she even have a nature?\n"
        voice "audio/_pristine/voice/happy/narrator/53a.flac"
        n "That is precisely why she poses a threat.\n"
        voice "audio/_pristine/voice/happy/hero/36.flac"
        hero "I don't know... she got weird for a second, yeah, but she didn't change {i}that{/i}—\n{w=5.3}{nw}"
        show screen disableclick(0.5)
        voice "audio/_pristine/voice/happy/narrator/54.flac"
        n "We have to move on. This is a wildly dangerous line of reasoning.\n"
        voice "audio/_pristine/voice/happy/hero/37.flac"
        hero "No, no, no, you can't just say that and not—\n{w=2.75}{nw}"
        show screen disableclick(0.5)

    voice "audio/_pristine/voice/happy/narrator/55.flac"
    n "Her voice, gentle and warm with an undercurrent of fatigue, rolls down the stairs.\n"
    voice "audio/_pristine/voice/happy/princess/11.flac"
    p "You're home. Dinner's ready.\n"
    voice "audio/_pristine/voice/happy/narrator/56b.flac"
    n "As much as I desperately want to know what happened last time, we are not going to examine it. The more we think, the worse this gets.\n"
    voice "audio/_pristine/voice/happy/hero/38a.flac"
    hero "Why are you so on-edge? This is much nicer than what we're used to. I'd like to have dinner! Dinner sounds nice!\n"
    if trait_opportunist:
        voice "audio/_pristine/voice/happy/opportunist/15.flac"
        opportunist "Gotta say, I'm with him on this one, boss. When have nice things ever been a problem?\n"
    voice "audio/_pristine/voice/happy/narrator/57.flac"
    n "That {i}is{/i} the problem. This isn't supposed to be nice, and she's supposed to be a prisoner. {i}Sigh{/i}. I need to stop talking. I need to stop talking. Just go upstairs, okay?\n"
    if trait_paranoid:
        voice "audio/_pristine/voice/happy/paranoid/15.flac"
        paranoid "And don't. Eat. The food.\n"
    #else:
    #    voice "audio/_pristine/voice/happy/opportunist/16.flac"
    #    opportunist "Oh, I get it! So this is an exercise in discipline. Can do!\n"
    menu:
        extend ""

        "{i}• [[Proceed up the stairs.]{/i}":
            jump happy_encounter

label happy_encounter:
    $ gallery_happy.unlock_item(2)
    $ renpy.save_persistent()
    $ quick_menu = False
    play secondary "audio/looping/STP_firecontrolled_loop.ogg" loop fadein 1.0
    play audio "audio/one_shot/footsteps_stone.flac"
    hide bg onlayer back
    scene bg black
    with fade
    scene bg happy upstairs onlayer back at Position(ypos=1350)
    show shadows happy neutral onlayer back at Position(ypos=1350)
    show happy t neutral onlayer back at Position(ypos=1350)
    show fire happy onlayer back at Position(ypos=1350)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    voice "audio/_pristine/voice/happy/narrator/58.flac"
    n "This hall, like the one below, is grand and beautiful. Torches bathe the room in warm, comforting light, just enough to illuminate the tapestries along every wall, woven with scenes of chivalry and courtship and romance. The many cloth eyes are fixed on each other, gazes averted from the long table in the center of the room, the Princess seated at its far end.\n"
    # Note to ABBY: there are four torches, two on each side; so three can blow out over the course of the conversation, and there can be a final, separate menu for the fourth.
    voice "audio/_pristine/voice/happy/narrator/59.flac"
    n "Your pristine blade glints in the weak torchlight, hanging from a golden chain around the Princess' neck.\n"
    voice "audio/_pristine/voice/happy/narrator/60.flac"
    n "So that's where it is! And the tip is already pointed right at her heart. Okay. Everything is falling back into place. All you have to do is cross the room, push down a little, and the entire world is saved. That's easy.\n"
    if trait_paranoid:
        voice "audio/_pristine/voice/happy/paranoid/16a.flac"
        paranoid "Isn't that... {i}suspiciously{/i} easy? There has to be a twist. There has to be something waiting for us. You saw what happened to her last time, she's not what she seems.\n" id happy_encounter_54c3ec1e
        #voice "audio/_pristine/voice/happy/narrator/61.flac"
        #n "Yes! Exactly! So we're on the same page — she's dangerous.\n"
        #voice "audio/_pristine/voice/happy/hero/39.flac"
        #hero "I think she's... sad.\n"
    else:
        voice "audio/_pristine/voice/happy/opportunist/17.flac"
        opportunist "Yeah. That is easy, isn't it? So where's the rush?\n"
        #voice "audio/_pristine/voice/happy/narrator/62.flac"
        #n "Where's the rush? I feel I've been very explicit about that. She poses a great danger to the world. That sort of threat is the kind you eliminate as quickly as possible, not idly dine with.\n"
        #voice "audio/_pristine/voice/happy/opportunist/18.flac"
        #opportunist "Oh come on, the blade isn't going anywhere, why don't we settle in and enjoy ourselves a little? We asked for this before we died, right? And it looks nice! I want to sit at the head of this big table, I think we'll really feel important if we do.\n"
        #voice "audio/_pristine/voice/happy/hero/40.flac"
        #hero "I suppose... we did ask for this, didn't we?\n"
        #voice "audio/_pristine/voice/happy/narrator/63.flac"
        #n "Ask for what?\n"

    voice "audio/_pristine/voice/happy/princess/12.flac"
    show happy t neutral talk onlayer back
    with dissolve
    p "You're here! Now we can start being happy together. Why don't you sit down? Wouldn't that be nice?\n"
    play audio "audio/final/Damsel_FireSHootingOut_1.flac"
    play tertiary "audio/_pristine/sfx/_chair_drag.flac" noloop
    voice "audio/_pristine/voice/happy/narrator/64.flac"
    show bg happy upstairs onlayer back at collapse
    show shadows happy neutral onlayer back at collapse
    show happy t empty smile onlayer back at collapse
    show fire happy flare onlayer back at collapse
    show player happy chair hands onlayer back at Position(ypos=1150)
    with dissolve
    n "As the words leave her mouth, the torches flare and a chair swings in from behind, knocking your legs out from under you. You're forcibly seated at the head of the table.\n"
    voice "audio/_pristine/voice/happy/princess/13a.flac"
    stop tertiary fadeout 1.0
    show happy t empty smile talk onlayer back
    show fire happy onlayer back at Position(ypos=1250)
    with dissolve
    p "Isn't that better? It is better, right?\n"
    hide fire onlayer back
    show fire happy onlayer back at Position(ypos=1250)
    show happy t empty smile onlayer back

label happy_menu:

    default happy_everything_we_need_can_comment = False
    default happy_everything_we_need_explore = False
    default happy_truth_explore = False
    default happy_happy_asked = False

    default happy_torches = 4
    default happy_get_up_attempt = False
    default happy_slay_explore = False
    default happy_eaten = False
    default happy_played = False
    default happy_torch_comment_immediate = False
    default happy_torch_first_comm = False
    default happy_torch_just_explore = False
    default happy_torch_leave_explore = False
    default happy_torch_shadow_known = False
    default happy_what_place_explore = False
    default happy_what_do_explore = False
    default happy_post_eat_explore = False
    default happy_final_activity_explore = False
    default happy_shadow_acted = False
    default happy_set_table = False
    default happy_him_explore = False


    default happy_paranoid_deduce = False
    default happy_him_mentioned = False
    default happy_cant_up_explore = False

    default happy_shadow_talk_attempt = False

    default happy_defensive_flag = False
    default happy_defensive_spoken = False
    if happy_defensive_flag and happy_defensive_spoken == False:
        $ happy_defensive_spoken = True
        #if trait_paranoid:
            #voice "audio/_pristine/voice/happy/paranoid/17.flac"
            #paranoid "I don't think you need me to tell you that everything definitely isn't fine!\n"
        if trait_opportunist:
            voice "audio/_pristine/voice/happy/opportunist/19.flac"
            opportunist "She's being defensive. And we all know being defensive is a sign of weakness.\n"
    menu:
        extend ""

        "{i}• (Explore) ''Hey! Smitten! You were real chatty last time. Don't you have anything to say?''{/i}" if happy_paranoid_deduce and happy_shadow_talk_attempt == False:
            $ happy_shadow_talk_attempt = True
            $ happy_torch_comment_immediate = False
            $ happy_torch_shadow_known = True
            voice "audio/_pristine/voice/happy/princess/14.flac"
            show happy t sad smile talk onlayer back
            with dissolve
            p "Smitten...?\n"
            $ gallery_happy.unlock_item(3)
            $ renpy.save_persistent()
            voice "audio/_pristine/voice/happy/narrator/65.flac"
            play audio "audio/final/Damsel_FireSHootingOut_1.flac"
            show happy t nervous onlayer back
            show fire happy flare onlayer back
            show shadows happy smile onlayer back
            with dissolve
            n "The torches flare and the shadow grows for a moment, but you don't receive a response.\n"
            voice "audio/_pristine/voice/happy/paranoid/18a.flac"
            show happy t empty smile onlayer back
            show fire happy onlayer back
            show shadows happy neutral onlayer back
            with dissolve
            paranoid "No, I saw him smile. That's him!\n"
            #voice "audio/_pristine/voice/happy/paranoid/18.flac"
            #paranoid "No, I saw him smile. That's him. He knows what's going on!\n"
            voice "audio/_pristine/voice/happy/narrator/66.flac"
            n "Regardless, it would seem that he, if there is a 'he,' isn't something you can talk to.\n"
            if happy_him_explore:
                voice "audio/_pristine/voice/happy/princess/15.flac"
                show happy t sad smile talk onlayer back
                with dissolve
                p "He says his words are just for me. But he wants me to ask... isn't this enough? Isn't this what you wanted him to do?\n" id happy_menu_2dde6660
                voice "audio/_pristine/voice/happy/princess/16a.flac"
                show happy t serious talk onlayer back
                with dissolve
                p "He says he's tired. I don't think he'll answer anything else you have to say.\n"
                show happy t neutral onlayer back
                if trait_opportunist:
                    voice "audio/_pristine/voice/happy/opportunist/20.flac"
                    opportunist "This isn't fair! If I could just talk to him for two seconds, I'm sure we could sort this out and figure out a balanced power structure that works better for everyone. But no, he's decided he's above talking to little guys like us, huh?\n"
            else:
                voice "audio/_pristine/voice/happy/princess/17a.flac"
                show happy t sad smile talk onlayer back
                with dissolve
                p "Oh. You're talking to the shadow, aren't you?\n"
                if trait_paranoid:
                    voice "audio/_pristine/voice/happy/paranoid/19.flac"
                    show happy t sad smile onlayer back
                    paranoid "She guessed that right away. She knows what's going on here, I knew it!\n"
                jump happy_him_join
            jump happy_menu

        "{i}• (Explore) ''Hey! Shadow! Don't you have anything to say?''{/i}" if trait_paranoid == False and happy_shadow_talk_attempt == False and happy_him_explore:
            $ happy_shadow_talk_attempt = True
            $ happy_torch_comment_immediate = False
            $ happy_torch_shadow_known = True
            voice "audio/_pristine/voice/happy/narrator/65.flac"
            play audio "audio/final/Damsel_FireSHootingOut_1.flac"
            show happy t nervous onlayer back
            show fire happy flare onlayer back
            show shadows happy smile onlayer back
            with dissolve
            n "The torches flare and the shadow grows for a moment, but you don't receive a response.\n"
            voice "audio/_pristine/voice/happy/opportunist/21.flac"
            show happy t empty smile onlayer back
            show fire happy onlayer back
            show shadows happy neutral onlayer back
            with dissolve
            opportunist "Giving us the cold shoulder, I see. Asserting his dominance in the power structure.\n"
            voice "audio/_pristine/voice/happy/narrator/66.flac"
            n "Regardless, it would seem that he, if there is a 'he,' isn't something you can talk to.\n"
            if happy_him_explore:
                voice "audio/_pristine/voice/happy/princess/15a.flac"
                show happy t sad smile talk onlayer back
                with dissolve
                p "He says his words are just for me. But he wants me to ask... isn't this enough? Isn't this what you wanted him to do?\n"
                voice "audio/_pristine/voice/happy/princess/16a.flac"
                show happy t serious talk onlayer back
                with dissolve
                p "He says he's tired. I don't think he'll answer anything else you have to say.\n"
                show happy t neutral onlayer back
                if trait_opportunist:
                    voice "audio/_pristine/voice/happy/opportunist/20.flac"
                    opportunist "This isn't fair! If I could just talk to him for two seconds, I'm sure we could sort this out and figure out a balanced power structure that works better for everyone. But no, he's decided he's above talking to little guys like us, huh?\n"
            jump happy_menu


        "{i}• (Explore) ''What just happened? Did you make that torch go out?''{/i}" if happy_torch_comment_immediate and happy_torches == 3 and happy_torch_first_comm == False:
            $ happy_torch_first_comm = True
            $ happy_defensive_flag = True
            voice "audio/_pristine/voice/happy/princess/18.flac"
            play audio "audio/final/Damsel_FireSHootingOut_1.flac"
            play tertiary "audio/one_shot/new/STP_strangershuffle_5.flac"
            show fire happy flare onlayer back
            show shadows happy grab onlayer back
            show happy t shadow tight talk onlayer back
            with dissolve
            p "I didn't mean to! I promise! Everything is fine. Everything is fine.\n"
            show fire happy onlayer back
            show shadows happy neutral onlayer back
            show happy t smile empty onlayer back
            with dissolve
            jump happy_menu

        "{i}• (Explore) ''I don't think you did anything wrong. I think you just said something you wanted to say.''{/i}" if happy_torch_comment_immediate and happy_torches == 3 and happy_torch_first_comm == False:
            $ happy_torch_first_comm = True
            $ happy_him_mentioned = True
            voice "audio/_pristine/voice/happy/princess/19.flac"
            show happy t sad smile talk onlayer back
            with dissolve
            p "But it was wrong. I took away a piece of our light. I'm not supposed to do that. I don't want him to be upset with me.\n"
            show happy t sad smile onlayer back
            jump happy_menu

        "{i}• (Explore) ''It's just a torch. Don't worry about it. We still have plenty of light.''{/i}" if happy_torch_comment_immediate and happy_torch_just_explore == False and happy_torches <= 3:
            $ happy_torch_just_explore = True
            voice "audio/_pristine/voice/happy/princess/20.flac"
            show happy t scared talk onlayer back
            with dissolve
            p "Yeah. Yeah. We just have to keep the rest lit. And everything will be okay.\n"
            voice "audio/_pristine/voice/happy/narrator/67.flac"
            show happy t sad onlayer back
            with dissolve
            n "The Princess' eyes dart to the floor.\n"
            voice "audio/_pristine/voice/happy/princess/21.flac"
            show happy t neutral talk onlayer back
            with dissolve
            p "We should do something fun! Wouldn't that be nice?\n"
            label happy_distraction_tree:
                if happy_eaten == False and happy_refused_food == False:
                    jump happy_dinner_join
                elif happy_played == False:
                    voice "audio/_pristine/voice/happy/princess/22.flac"
                    show happy t empty smile talk onlayer back
                    with dissolve
                    p "What if we... played a game?\n"
                    if trait_opportunist:
                        voice "audio/_pristine/voice/happy/opportunist/22.flac"
                        show happy t empty smile onlayer back
                        with dissolve
                        opportunist "Yes! I love games, I'm great at them.\n"
                    if trait_paranoid:
                        voice "audio/_pristine/voice/happy/paranoid/20.flac"
                        show happy t empty smile onlayer back
                        with dissolve
                        paranoid "She's trying to distract us.\n"
                    jump happy_game_join
                else:
                    voice "audio/_pristine/voice/happy/princess/23.flac"
                    show happy t nervous talk onlayer back
                    with dissolve
                    p "How about...\n"
                    voice "audio/_pristine/voice/happy/narrator/68.flac"
                    show happy t sad onlayer back
                    with dissolve
                    n "The Princess' face drops as she pauses mid-sentence.\n"
                    voice "audio/_pristine/voice/happy/princess/24.flac"
                    show happy t empty smile talk onlayer back
                    with dissolve
                    p "Haha. Would you look at that? I'm out of ideas.\n"
                    jump happy_torches
                jump happy_menu

        "{i}• (Explore) ''This place isn't right. We have to put the rest of them out. We have to get rid of that shadow.''{/i}" if happy_torch_comment_immediate and happy_torches <= 3 and happy_torch_leave_explore == False and happy_torch_shadow_known:
            $ happy_torch_leave_explore = True
            voice "audio/_pristine/voice/happy/princess/25a.flac"
            show happy t scared talk onlayer back
            with dissolve
            p "W...why would we ever do that? We need the light. It's what keeps us happy.\n"
            voice "audio/_pristine/voice/happy/princess/26.flac"
            show happy t sad onlayer back
            with dissolve
            p "...\n"
            voice "audio/_pristine/voice/happy/princess/27.flac"
            show happy t neutral talk onlayer back
            with dissolve
            p "Oh! I know! We should do something!\n"
            jump happy_distraction_tree

        "{i}• (Explore) ''We need the truth. You need to tell me how you really feel.''{/i}" if happy_happy_asked and happy_truth_explore == False:
            $ happy_truth_explore = True
            voice "audio/_pristine/voice/happy/princess/28.flac"
            show happy t sad onlayer back
            with dissolve
            p "I... I... don't feel anything.\n"
            jump happy_torches

        "{i}• (Explore) ''Do we actually have everything we need? Because it doesn't feel like it, it feels like...''{/i}" if happy_everything_we_need_can_comment and happy_everything_we_need_explore == False and (happy_eaten or happy_played):
            $ happy_everything_we_need_explore = True
            $ happy_torch_leave_explore = True
            voice "audio/_pristine/voice/happy/princess/29.flac"
            show happy t serious talk onlayer back
            with dissolve
            p "Like we've been given everything someone else has told us we wanted. But it isn't what we want.\n"
            jump happy_torches

        "{i}• (Explore) ''Are you actually happy here?''{/i}" if happy_torches <= 2 and happy_happy_asked == False:
            $ happy_happy_asked = True
            $ happy_defensive_flag = True
            $ happy_torch_comment_immediate = False
            voice "audio/_pristine/voice/happy/narrator/69.flac"
            show happy t scared talk onlayer back
            with dissolve
            n "The Princess starts to hyperventilate, her quick breaths punctuating the uncomfortable silence between you.\n"
            voice "audio/_pristine/voice/happy/princess/30.flac"
            show happy t empty smile talk onlayer back
            with dissolve
            p "Yes! Why wouldn't I be? Let's not talk about it!\n"
            show happy t empty smile onlayer back
            jump happy_menu

        "{i}• (Explore) ''The shadow holding me down. Is it the same one that set the table?''{/i}" if happy_set_table and happy_shadow_commented == False and happy_get_up_attempt:
            label happy_shadow_discuss_join:
                default happy_shadow_commented = False
                $ happy_torch_shadow_known = True
                $ happy_shadow_commented = True
                $ happy_defensive_flag = True
                $ happy_him_mentioned = True
                $ happy_torch_comment_immediate = False
                voice "audio/_pristine/voice/happy/princess/31.flac"
                play audio "audio/final/Damsel_FireSHootingOut_1.flac"
                show fire happy flare onlayer back
                show shadows happy grab onlayer back
                show happy t shadow tight talk onlayer back
                with dissolve
                p "We don't have to talk about him. We shouldn't talk about him! He's fine. We're fine. Everything is fine. He just wants us to be happy.\n"
                show fire happy onlayer back
                show shadows happy neutral onlayer back
                show happy t smile empty onlayer back
                with dissolve
                jump happy_menu

        "{i}• (Explore) ''The shadow that set the table... is it separate from us?''{/i}" if happy_set_table and happy_shadow_commented == False:
            jump happy_shadow_discuss_join

        "{i}• (Explore) ''You said 'he.' Who is he?''{/i}" if happy_him_mentioned and happy_him_explore == False:
            label happy_him_join:
                $ happy_him_explore = True
                $ happy_torch_comment_immediate = False
                $ happy_what_do_explore = True
                voice "audio/_pristine/voice/happy/princess/32.flac"
                show happy t sad smile talk onlayer back
                with dissolve
                p "He's the voice that whispers sweet nothings in my ear. I think he made this place for us.\n"
                show happy t sad smile onlayer back
                if trait_paranoid:
                    if happy_paranoid_deduce == False:
                        $ happy_paranoid_deduce = True
                        voice "audio/_pristine/voice/happy/paranoid/21.flac"
                        paranoid "It all makes sense now. It's {i}him{/i}, isn't it? He's making all of this happen. He's the one who's trapped us here.\n"
                        voice "audio/_pristine/voice/happy/hero/41.flac"
                        hero "Who?\n"
                        $ achievement.grant("ACH_HAPPY_SHADOWS")
                        voice "audio/_pristine/voice/happy/paranoid/22.flac"
                        paranoid "The lovesick one. The one from last time. He's not gone. He's just with her now. {i}He's{/i} the shadow.\n"
                    else:
                        $ happy_paranoid_deduce = True
                        voice "audio/_pristine/voice/happy/paranoid/23.flac"
                        paranoid "I was right, wasn't I? I can't believe I was actually right. It {i}is{/i} him. This is what he became after ripping us open.\n"
                if trait_opportunist:
                    voice "audio/_pristine/voice/happy/opportunist/23.flac"
                    opportunist "Is she talking about a real voice? Like us? But... we're at the head of the table! We should be in charge! Is he more powerful than we are?\n"
                    if happy_get_up_attempt:
                        voice "audio/_pristine/voice/happy/hero/42.flac"
                        hero "Is he the thing holding us down?\n"
                jump happy_menu


        "{i}• (Explore) ''What is this place?''{/i}" if happy_what_place_explore == False:
            $ happy_what_place_explore = True
            $ happy_torch_comment_immediate = False
            if happy_torches == 4:
                voice "audio/_pristine/voice/happy/princess/33.flac"
                show happy t empty smile talk onlayer back
                with dissolve
            else:
                show happy t smile genuine talk onlayer back
                with dissolve
                voice "audio/_pristine/voice/happy/princess/34.flac"
            p "It's our happy ending. Just like you asked for. It's everything we're supposed to have ever wanted.\n"
            if happy_torches == 4:
                show happy t empty smile onlayer back
            else:
                show happy t smile genuine onlayer back
            jump happy_menu

        "{i}• (Explore) ''What are we supposed to do now?''{/i}" if happy_what_do_explore == False and happy_eaten == False and happy_refused_food == False:
            $ happy_torch_comment_immediate = False
            $ happy_what_do_explore = True
            jump happy_dinner_join


        "{i}• (Explore) ''You mentioned dinner on the stairs.''{/i}" if happy_eaten == False and happy_refused_food == False:
            default happy_directly_asked_dinner = False
            $ happy_directly_asked_dinner = True
            $ happy_torch_comment_immediate = False
            label happy_dinner_join:
                if happy_torches == 4:
                    voice "audio/_pristine/voice/happy/princess/35a.flac"
                    show happy t smile genuine talk onlayer back
                    with dissolve
                    p "Oh, right! Dinner! I'd totally forgotten about it.\n"
                elif happy_torches == 3:
                    voice "audio/_pristine/voice/happy/princess/35b.flac"
                    show happy t smile genuine talk onlayer back
                    with dissolve
                    p "Oh, right! Dinner! I'd totally forgotten about it. I'm so sorry!\n"
                else:
                    voice "audio/_pristine/voice/happy/princess/35.flac"
                    show happy t nervous talk onlayer back
                    with dissolve
                    p "Oh, right! Dinner! I'd totally forgotten about it. I'm so sorry!\n"
                $ gallery_happy.unlock_item(4)
                $ renpy.save_persistent()
                play audio "audio/_pristine/sfx/Happy ghost hissing_6.flac"
                play tertiary "audio/_pristine/sfx/plates_place_table.flac"
                voice "audio/_pristine/voice/happy/narrator/70.flac"
                play secondary "audio/final/Damsel_FireSHootingOut_1.flac"
                queue secondary "audio/looping/STP_firecontrolled_loop.ogg" loop fadein 1.0
                show fire happy flare onlayer back
                show shadows set onlayer back
                show food happy placed onlayer back at Position(ypos=1250)
                show happy t neutral onlayer back
                with dissolve
                n "The flames burn bright, and a shadow dives across the table. In its wake it leaves a feast.\n"
                play secondary "audio/looping/STP_firecontrolled_loop.ogg" loop
                voice "audio/_pristine/voice/happy/princess/36.flac"
                show fire happy onlayer back
                show happy t sad smile talk onlayer back
                with dissolve
                p "Go ahead and dig in. I'm sure you're hungry.\n"
                show happy t sad smile onlayer back
                if trait_paranoid:
                    voice "audio/_pristine/voice/happy/paranoid/24.flac"
                    paranoid "Remember what I said.\n"
                    voice "audio/_pristine/voice/happy/hero/43.flac"
                    hero "Aw, but... it looks so amazing. And after everything we've been through, we could really use a break. Are you sure we need to be so concerned?\n"
                    voice "audio/_pristine/voice/happy/paranoid/25.flac"
                    paranoid "I'm not sure about anything, and that's the problem.\n"
                    #voice "audio/_pristine/voice/happy/hero/44.flac"
                    #hero "Do you think it's poison or something?\n"
                    voice "audio/_pristine/voice/happy/narrator/71.flac"
                    n "For what it's worth, I generally don't think one should trust strange food that magically appears on a table. But nothing here is exactly what I expected it to be, so make of that what you will.\n"
                elif trait_opportunist:
                    voice "audio/_pristine/voice/happy/opportunist/24.flac"
                    opportunist "Am I ever! And look at this spread, it's a feast fit for a king.\n"
                    voice "audio/_pristine/voice/happy/hero/45a.flac"
                    hero "Yeah. And after everything we've been through, we could use a break.\n"
                    voice "audio/_pristine/voice/happy/opportunist/25.flac"
                    opportunist "More than that, we {i}deserve{/i} a break.\n"
                menu:
                    extend ""

                    "{i}• [[Refuse her hospitality.]{/i}":
                        default happy_refused_food = False
                        $ happy_refused_food = True
                        if happy_directly_asked_dinner:
                            voice "audio/_pristine/voice/happy/princess/37a.flac"
                            show happy t serious talk onlayer back
                            with dissolve
                            p "O... oh. But you were the one who asked about it!\n"
                            voice "audio/_pristine/voice/happy/princess/38.flac"
                            show happy t sad onlayer back
                            with dissolve
                            p "Agh, sorry, that was snippy.\n"
                        voice "audio/_pristine/voice/happy/princess/39.flac"
                        show happy t scared onlayer back
                        with dissolve
                        p "It's okay, it's okay, we can figure something else out. Think, think, think.\n" id happy_dinner_join_46d8f4e5
                        voice "audio/_pristine/voice/happy/princess/40.flac"
                        show happy t nervous onlayer back
                        with dissolve
                        p "This is fine, this is fine, this is fine...\n"
                        voice "audio/_pristine/voice/happy/princess/41.flac"
                        show happy t nervous talk onlayer back
                        with dissolve
                        p "This isn't fine. This isn't fine at all!\n"
                        jump happy_torches

                    "{i}• [[Eat.]{/i}":
                        $ happy_eaten = True
                        voice "audio/_pristine/voice/happy/narrator/72.flac"
                        play audio "audio/_pristine/sfx/eat_1.flac"
                        hide player onlayer back
                        show food happy set 2 onlayer back
                        show player food eat onlayer back at Position(ypos=1125)
                        show happy t eat onlayer back
                        with dissolve
                        n "You begin to feast, and the Princess follows suit, her soft smile never fading.\n"
                        voice "audio/_pristine/voice/happy/narrator/73.flac"
                        play audio "audio/_pristine/sfx/eat_2.flac"
                        show food happy set 3 onlayer back
                        with dissolve
                        n "The food is more exquisite than you ever could have imagined. You sample countless otherworldly dishes, sauces and bread and hearty stews whose tastes dance across your tongue.\n"
                        voice "audio/_pristine/voice/happy/narrator/74.flac"
                        play audio "audio/_pristine/sfx/eat_3.flac"
                        show food happy eaten onlayer back
                        with dissolve
                        n "You tear at hunks of meat practically melting from the bone, juicy and tender and bursting with flavors you could scarcely begin to describe. Your cup fills itself again and again with a flowery nectar so sweet it tastes like glimmering jewels.\n"
                        voice "audio/_pristine/voice/happy/hero/_extra1a.flac"
                        hero "This really is perfect, isn't it?\n"
                        voice "audio/_pristine/voice/happy/narrator/75.flac"
                        n "It is the best meal you have ever had.\n"
                        voice "audio/_pristine/voice/happy/narrator/76.flac"
                        show player happy chair hands onlayer back
                        show happy t neutral onlayer back
                        with dissolve
                        n "But then it's over. And you're just as hungry as when you began.\n"
                        voice "audio/_pristine/voice/happy/princess/42.flac"
                        show happy t smile genuine talk onlayer back
                        with dissolve
                        p "Wasn't that perfect? We should do it again.\n" id happy_dinner_join_348541d1
                        voice "audio/_pristine/voice/happy/narrator/77.flac"
                        play audio "audio/_pristine/sfx/Happy ghost hissing_6.flac"
                        play tertiary "audio/_pristine/sfx/plates_place_table.flac"
                        play secondary "audio/final/Damsel_FireSHootingOut_1.flac"
                        queue secondary "audio/looping/STP_firecontrolled_loop.ogg" loop fadein 1.0
                        show fire happy flare onlayer back
                        show happy t smile genuine onlayer back
                        show shadows set onlayer back
                        show food happy replace onlayer back
                        with dissolve
                        n "The shadow washes across the table, clearing and replating. The feast is once again laid before you.\n"
                        voice "audio/_pristine/voice/happy/narrator/78.flac"
                        play audio "audio/_pristine/sfx/eat_1.flac"
                        show food happy set 3 onlayer back
                        show fire happy onlayer back
                        show player food eat onlayer back
                        show happy t eat onlayer back
                        with dissolve
                        n "The food is good, again. You tear into golden, crispy flesh, dab at the slurry of aromatic sauces on your plate with thick-crusted bread, sip your goblet of sparkling gems. But you have done this already.\n"
                        if trait_opportunist:
                            voice "audio/_pristine/voice/happy/opportunist/26.flac"
                            opportunist "A good meal is still a good meal. And we didn't even have to clear the dishes! I'm happy.\n"
                        voice "audio/_pristine/voice/happy/narrator/79a.flac"
                        show player happy chair hands onlayer back
                        show happy t sad smile onlayer back
                        show food happy eaten onlayer back
                        with dissolve
                        n "And then it's over, and you're just as hungry as when you began.\n"
                        voice "audio/_pristine/voice/happy/princess/43.flac"
                        show happy t empty smile talk onlayer back
                        with dissolve
                        p "You're still hungry, too, right? I know this wasn't as good as it was last time, but... we just have to do it again, that's all. It'll be perfect if we just do it again.\n"
                        voice "audio/_pristine/voice/happy/narrator/80a.flac"
                        play audio "audio/_pristine/sfx/Happy ghost hissing_6.flac"
                        play tertiary "audio/_pristine/sfx/plates_place_table.flac"
                        play secondary "audio/final/Damsel_FireSHootingOut_1.flac"
                        queue secondary "audio/looping/STP_firecontrolled_loop.ogg" loop fadein 1.0
                        show happy t empty smile onlayer back
                        show fire happy flare onlayer back
                        show shadows set onlayer back
                        show food happy replace onlayer back
                        with dissolve
                        n "And so the shadow sweeps over the table, clearing the old and laying out the new. And so you do it again.\n"
                        voice "audio/_pristine/voice/happy/narrator/81.flac"
                        play audio "audio/_pristine/sfx/Den Creatures Eating_17.flac"
                        show fire happy onlayer back
                        show food happy eaten onlayer back
                        show player food eat onlayer back
                        show happy t serious talk onlayer back
                        with dissolve
                        n "The meat is fine. The bread is fine. You sample the side dishes, and they're fine, too. You finish your goblet, the liquid within no longer glimmering on your palatte, instead leaving your mouth coated in a tacky film. You put it down, and it fills again. You do not drink more.\n"
                        #voice "audio/_pristine/voice/happy/narrator/82.flac"
                        #n "I'm starting to sense a pattern. I don't like where this is going.\n"
                        if trait_paranoid:
                            #voice "audio/_pristine/voice/happy/paranoid/26.flac"
                            #paranoid "I told you not to eat the food, but did you listen?\n"
                            voice "audio/_pristine/voice/happy/hero/46a.flac"
                            show player happy chair hands onlayer back
                            with dissolve
                            hero "So we had a mediocre meal. It's not a big deal.\n"
                            voice "audio/_pristine/voice/happy/paranoid/27a.flac"
                            paranoid "That's the trap! It wasn't mediocre at first. It's trending down.\n"
                            voice "audio/_pristine/voice/happy/hero/47.flac"
                            hero "We're just getting a little sick of it, so what? We just have to try something new, I'm sure we won't be stuck eating the same meal forever.\n"
                            #voice "audio/_pristine/voice/happy/narrator/83.flac"
                            #show player happy chair hands onlayer back
                            #with dissolve
                            #n "Regardless of quality, it's over, again, and you're just as hungry as when you began. Again.\n"
                        elif trait_opportunist:
                            voice "audio/_pristine/voice/happy/opportunist/27.flac"
                            show player happy chair hands onlayer back
                            with dissolve
                            opportunist "Well... food is food, isn't it? It can't always be amazing. What matters is that we don't have to make it. Getting other people to do the hard work always improves the taste.\n"
                            voice "audio/_pristine/voice/happy/hero/48.flac"
                            hero "Does it? Because it seems like the taste is getting worse. And we haven't had to so much as lift a finger.\n"
                            #voice "audio/_pristine/voice/happy/opportunist/28.flac"
                            #opportunist "But... things are supposed to be better on the top. And how much more top could we be?\n"
                            #voice "audio/_pristine/voice/happy/narrator/84.flac"
                            #n "As you sit back from your unfinished plate, it is once again swept away, and you're once again just as hungry as when you began.\n"
                        voice "audio/_pristine/voice/happy/narrator/83.flac"
                        show player happy chair hands onlayer back
                        with dissolve
                        n "Regardless of quality, it's over, again, and you're just as hungry as when you began. Again.\n"
                        voice "audio/_pristine/voice/happy/princess/44.flac"
                        show happy t scared talk onlayer back
                        with dissolve
                        p "No, no. Something was wrong that time. But maybe I was just... tasting it wrong. It looks just as good as it did the first time. It shouldn't taste like this!\n"
                        voice "audio/_pristine/voice/happy/narrator/85.flac"
                        play audio "audio/_pristine/sfx/Happy ghost hissing_6.flac"
                        play tertiary "audio/_pristine/sfx/plates_place_table.flac"
                        play secondary "audio/final/Damsel_FireSHootingOut_1.flac"
                        queue secondary "audio/looping/STP_firecontrolled_loop.ogg" loop fadein 1.0
                        show fire happy flare onlayer back
                        show happy t sad onlayer back
                        show shadows set onlayer back
                        show food happy replace onlayer back
                        with dissolve
                        n "Again, the shadow replaces your feast, and again you eat.\n"
                        voice "audio/_pristine/voice/happy/narrator/86.flac"
                        play audio "audio/_pristine/sfx/eat_gross.flac"
                        show fire happy onlayer back
                        show food happy eaten onlayer back
                        show player food eat onlayer back
                        with dissolve
                        n "The meat is greasy. The bread is tough, its crust hurting your jaw as you chew. The gray vegetables are barely worth the effort of picking through. You don't even touch the goblet, its sickly sweet aroma utterly unappealing.\n"
                        voice "audio/_pristine/voice/happy/hero/49.flac"
                        hero "I'm so tired of eating.\n"
                        #if trait_paranoid:
                        #    voice "audio/_pristine/voice/happy/paranoid/28a.flac"
                        #    paranoid "What a surprise! If only someone had warned you not to eat it!\n"
                        #    voice "audio/_pristine/voice/happy/hero/50.flac"
                        #    hero "Oh, don't rub it in.\n"
                        if trait_opportunist:
                            voice "audio/_pristine/voice/happy/opportunist/29.flac"
                            opportunist "Well... it's still free food we didn't have to make... right? Who am I kidding. We were eating like kings and now we're eating like pigs.\n"
                        voice "audio/_pristine/voice/happy/narrator/87a.flac"
                        show player happy chair hands onlayer back
                        with dissolve
                        n "At least you still have the memory of how good it was the first time. Right?\n"
                        voice "audio/_pristine/voice/happy/princess/45.flac"
                        show happy t serious talk onlayer back
                        with dissolve
                        p "I'm so tired of this.\n"
                        jump happy_torches

        "{i}• (Explore) ''Well, we ate. What are we supposed to do now?''{/i}" if happy_post_eat_explore == False and happy_eaten and happy_played == False:
            label happy_game_early_join:
                $ happy_post_eat_explore = True
                $ happy_torch_comment_immediate = False
                voice "audio/_pristine/voice/happy/princess/46.flac"
                show happy t empty smile talk onlayer back
                with dissolve
                p "Um... I don't know! Maybe we could... play a game?\n"
                label happy_game_join:
                    $ happy_played = True
                    voice "audio/_pristine/voice/happy/princess/47.flac"
                    show happy t smile genuine talk onlayer back
                    with dissolve
                    p "Yeah! That's exactly what we should do!\n"
                    voice "audio/_pristine/voice/happy/narrator/88.flac"
                    play audio "audio/_pristine/sfx/Happy ghost hissing_6.flac"
                    play tertiary "audio/_pristine/sfx/plates_place_table.flac"
                    play secondary "audio/final/Damsel_FireSHootingOut_1.flac"
                    queue secondary "audio/looping/STP_firecontrolled_loop.ogg" loop fadein 1.0
                    show fire happy flare onlayer back
                    show happy t neutral onlayer back
                    show shadows set onlayer back
                    if happy_eaten:
                        show food happy disappear onlayer back
                    else:
                        show food happy untouched disappear onlayer back
                    show game happy basic set onlayer back at Position(ypos=1250)
                    with dissolve
                    n "The flames roar, and the shadow comes dancing across the table. It leaves behind an intricate game, its pieces elegant and beautiful and enticing. Its simple rules already apparent even with little explanation.\n" id happy_game_join_656222a0
                    voice "audio/_pristine/voice/happy/princess/48.flac"
                    hide food onlayer back
                    show fire happy onlayer back
                    show happy t neutral talk onlayer back
                    with dissolve
                    p "We can probably work together to figure this out as we go. That sounds like a lot of fun, right?\n"
                    show happy t neutral onlayer back
                    if trait_opportunist:
                        voice "audio/_pristine/voice/happy/opportunist/30.flac"
                        opportunist "Great, we don't even have a rulebook. That means we can make up as many rules as we want... and we will! Don't worry, I am excellent at cheating, she'll never suspect a thing.\n"
                        voice "audio/_pristine/voice/happy/hero/51.flac"
                        hero "I don't think it really matters. This all kind of feels like... we're just filling time, you know?\n"
                        voice "audio/_pristine/voice/happy/opportunist/31.flac"
                        opportunist "What, you don't want to win? To show our prowess in all avenues and accumulate respect? Wow. You would be hopeless without me. Count your lucky stars I'm here.\n"
                    if trait_paranoid:
                        voice "audio/_pristine/voice/happy/paranoid/29.flac"
                        paranoid "Yet another waste of time. Why all the distractions? What are we being distracted {i}from{/i}? That's the real game... and I feel like I'm two steps behind.\n"
                        voice "audio/_pristine/voice/happy/hero/52.flac"
                        hero "You're overthinking it, mate. I feel like this is just... something to do. We might as well try to have some fun.\n"
                    voice "audio/_pristine/voice/happy/narrator/89.flac"
                    play audio "audio/_pristine/sfx/happy_play.flac"
                    show player game playing onlayer back
                    show happy t smile genuine onlayer back
                    show game happy basic finished onlayer back
                    with Dissolve(1.5)
                    n "You and the Princess do, indeed, figure it out as you go. And what a game it is. The tension between turns, the triumphant highs of moves well placed, and the tragic lows of miscalculations and careless plays. The warmth of trust and the cool texture of deception. And then, the climax, as she places her final piece...\n"
                    voice "audio/_pristine/voice/happy/princess/49.flac"
                    show happy t empty smile talk onlayer back
                    show player happy chair hands onlayer back
                    with dissolve
                    p "Oh. I think we got the rules wrong.\n"
                    voice "audio/_pristine/voice/happy/narrator/90a.flac"
                    show player game playing onlayer back
                    show happy t neutral onlayer back
                    show game happy basic onlayer back
                    with dissolve
                    n "And so you start over.\n"
                    if trait_opportunist:
                        voice "audio/_pristine/voice/happy/opportunist/32a.flac"
                        opportunist "She only made us start over because we were winning.\n"
                    #if trait_paranoid:
                        #voice "audio/_pristine/voice/happy/paranoid/30a.flac"
                        #paranoid "Of course. Again and again, as many times as we can stomach.\n"
                    voice "audio/_pristine/voice/happy/narrator/91.flac"
                    play audio "audio/_pristine/sfx/happy_play.flac"
                    show player game playing onlayer back
                    show happy t neutral onlayer back
                    show game happy basic finished onlayer back
                    with Dissolve(1.0)
                    n "Time passes, you play the game. You win.\n"
                    if trait_opportunist:
                        $ achievement.grant("ACH_HAPPY_GAMES")
                        voice "audio/_pristine/voice/happy/opportunist/33.flac"
                        opportunist "Boom! And there you have it! What did I tell you, am I great at games or am I great at games?\n"
                    else:
                        voice "audio/_pristine/voice/happy/hero/_extra2a.flac"
                        hero "Hey hey! Will you look at that!\n"
                    voice "audio/_pristine/voice/happy/princess/50.flac"
                    show player happy chair hands onlayer back
                    show happy t neutral talk onlayer back
                    show game happy basic onlayer back
                    with Dissolve(1.0)
                    p "Oh! You won! I guess we can play again.\n"
                    voice "audio/_pristine/voice/happy/narrator/92.flac"
                    play audio "audio/_pristine/sfx/happy_play.flac"
                    show player game playing onlayer back
                    show happy t empty smile onlayer back
                    show game happy basic finished onlayer back
                    with Dissolve(1.0)
                    n "Time passes, you play the game. She wins.\n"
                    voice "audio/_pristine/voice/happy/princess/51.flac"
                    show player happy chair hands onlayer back
                    show happy t sad smile talk onlayer back
                    with dissolve
                    p "OH! I won! I... guess we can play again.\n"
                    voice "audio/_pristine/voice/happy/narrator/93.flac"
                    n "There is a long pause, and the board does not reset.\n"
                    voice "audio/_pristine/voice/happy/princess/52.flac"
                    hide shadows onlayer back
                    hide happy onlayer back
                    show shadows happy neutral onlayer back at Position(ypos=1250)
                    show happy t sad onlayer back at Position(ypos=1250)
                    with dissolve
                    p "This isn't fun anymore, is it?\n"
                    if trait_paranoid:
                        voice "audio/_pristine/voice/happy/paranoid/31.flac"
                        paranoid "It's never going to stay fun.\n"
                    voice "audio/_pristine/voice/happy/narrator/94.flac"
                    n "You don't need me to tell you that it isn't... oh.\n"
                    play audio "audio/final/Damsel_FireSHootingOut_1.flac"
                    show happy t nervous onlayer back
                    $ happy_torches -= 1
                    $ renpy.pause(0.1)
                    $ happy_torches += 1
                    $ renpy.pause(0.1)
                    $ happy_torches -= 1
                    $ renpy.pause(0.1)
                    $ happy_torches += 1
                    $ renpy.pause(0.1)
                    $ happy_torches -= 1
                    $ renpy.pause(0.1)
                    $ happy_torches += 1

                    voice "audio/_pristine/voice/happy/narrator/95.flac"
                    n "The Princess visibly panics as another torch sputters.\n"
                    voice "audio/_pristine/voice/happy/princess/53.flac"
                    show happy t scared talk onlayer back
                    with dissolve
                    p "Wait! Wait, wait, wait! Maybe... this is just too easy. Maybe if we added more rules and pieces it'd be fun again.\n"
                    voice "audio/_pristine/voice/happy/hero/_extra3a.flac"
                    show happy t sad smile talk onlayer back
                    with dissolve
                    hero "Y... yeah. The game's just a little simple. We can make it fun again.\n"
                    voice "audio/_pristine/voice/happy/narrator/96a.flac"
                    play audio "audio/_pristine/sfx/Happy ghost hissing_6.flac"
                    play tertiary "audio/_pristine/sfx/plates_place_table.flac"
                    play secondary "audio/final/Damsel_FireSHootingOut_1.flac"
                    queue secondary "audio/looping/STP_firecontrolled_loop.ogg" loop fadein 1.0
                    show fire happy flare onlayer back
                    show happy t neutral onlayer back
                    show shadows set onlayer back
                    show game happy advanced set onlayer back at Position(ypos=1250)
                    with dissolve
                    n "The shadow descends on the board once again. More pieces are added, their shapes more intricate, their purposes less immediately clear. And the two of you set about discovering the complexities of the game anew.\n"
                    voice "audio/_pristine/voice/happy/narrator/97.flac"
                    play audio "audio/_pristine/sfx/happy_play_2.flac"
                    show player game playing onlayer back
                    show happy t sad smile onlayer back
                    show game happy complex finished onlayer back
                    with dissolve
                    n "And so you do, and it is fun again. In fact, it's almost as fun as the first time you played, and the sputtering torch roars back to life.\n"
                    voice "audio/_pristine/voice/happy/narrator/98.flac"
                    show fire happy onlayer back
                    show game happy complex onlayer back
                    show happy t nervous onlayer back
                    with dissolve
                    n "But then you get used to the additions, and the feeling starts to fade, a creeping numbness settling in over the board.\n"
                    voice "audio/_pristine/voice/happy/narrator/99.flac"
                    show game happy complex finished onlayer back
                    show happy t serious talk onlayer back
                    with dissolve
                    n "More pieces are added. The feelings flare. The feelings fade. The Princess suggests new rules. A glimmer of what could have been excitement flits through your mind, quickly vanishing as the game progresses. Your pieces advance in an ever-increasing slog to their destination.\n"
                    voice "audio/_pristine/voice/happy/narrator/100.flac"
                    show happy t sad onlayer back
                    show game happy complex onlayer back
                    with dissolve
                    n "Winning and losing become nothing but ends, and even the end becomes nothing as you roll over into a new game, the board resetting as many times as you can finish. Until finally...\n"
                    if trait_opportunist:
                        $ gallery_happy.unlock_item(5)
                        $ renpy.save_persistent()
                    voice "audio/_pristine/voice/happy/princess/54.flac"
                    show player happy chair hands onlayer back
                    show happy t sad smile talk onlayer back
                    show game happy complex finished onlayer back
                    with dissolve
                    p "I'm out of ideas. I'm actually out of ideas this time. I... don't think I can play anymore.\n"
                    jump happy_torches

        "{i}• (Explore) ''Forget about the food. What should we do now?''{/i}" if happy_post_eat_explore == False and happy_refused_food and happy_played == False:
            jump happy_game_early_join

        "{i}• (Explore) ''Okay, so... we've talked about food. We've played games. Now what?''{/i}" if happy_final_activity_explore == False and happy_refused_food and happy_played:
            jump happy_final_activity_join

        "{i}• (Explore) ''Okay, so... we've eaten. We've played games. Now what?''{/i}" if happy_final_activity_explore == False and happy_eaten and happy_played:
            label happy_final_activity_join:
                $ happy_post_eat_explore = True
                $ happy_torch_comment_immediate = False
                voice "audio/_pristine/voice/happy/princess/55.flac"
                show happy t sad smile talk onlayer back
                with dissolve
                p "I... I don't know. But we can't do those other things anymore, can we? Maybe we can... just spend time together?\n"
                voice "audio/_pristine/voice/happy/narrator/101.flac"
                show happy t empty smile onlayer back
                with dissolve
                n "The Princess smiles as the two of you wait.\n"
                voice "audio/_pristine/voice/happy/hero/53a.flac"
                hero "Come on. There has to be a way out of this. This can't be the rest of our lives. This can't be forever.\n"
                voice "audio/_pristine/voice/happy/narrator/102.flac"
                show happy t sad smile onlayer back
                with dissolve
                n "And wait.\n"
                if trait_paranoid:
                    voice "audio/_pristine/voice/happy/paranoid/32.flac"
                    paranoid "We live in a changing world, we know that. Something has to happen!\n"
                elif trait_opportunist:
                    voice "audio/_pristine/voice/happy/opportunist/34a.flac"
                    opportunist "What's the big deal? It's nice here. We've... got a lot of space, all our needs are met... We have the respect of everyone... in the room...\n"
                voice "audio/_pristine/voice/happy/narrator/103.flac"
                show happy t serious talk onlayer back
                with dissolve
                n "And wait.\n"
                if trait_paranoid:
                    voice "audio/_pristine/voice/happy/paranoid/33.flac"
                    paranoid "You keep saying that but we can't wait forever. There is no waiting forever.\n"
                elif trait_opportunist:
                    voice "audio/_pristine/voice/happy/opportunist/35.flac"
                    opportunist "This is what we wanted. This is what we asked for. It's good to be on top of the world.\n"
                voice "audio/_pristine/voice/happy/narrator/104.flac"
                show happy t nervous onlayer back
                with dissolve
                n "And wait.\n"
                voice "audio/_pristine/voice/happy/princess/56.flac"
                show happy t sad onlayer back
                with dissolve
                p "I can't do this anymore.\n"
                voice "audio/_pristine/voice/happy/narrator/105.flac"
                n "Oh no.\n"
                voice "audio/_pristine/voice/happy/hero/54.flac"
                hero "Oh no?\n"
                jump happy_torches


        "{i}• (Explore) ''I can't get up. Something's holding me down.''{/i}" if happy_get_up_attempt and happy_cant_up_explore == False:
            $ happy_cant_up_explore = True
            $ happy_everything_we_need_can_comment = True
            $ happy_torch_comment_immediate = False
            $ happy_him_mentioned = True
            voice "audio/_pristine/voice/happy/narrator/106.flac"
            show happy t empty smile onlayer back
            with dissolve
            n "The Princess smiles nervously.\n"
            if happy_torches == 4:
                voice "audio/_pristine/voice/happy/princess/57a.flac"
            else:
                voice "audio/_pristine/voice/happy/princess/57.flac"
            show happy t empty smile talk onlayer back
            with dissolve
            p "Oh, haha. Yeah. Don't worry about it. That's just how it works here. We don't have to go anywhere anymore. We have everything we need.\n"
            voice "audio/_pristine/voice/happy/princess/58.flac"
            show happy t neutral talk onlayer back
            with dissolve
            p "He just wants us to be happy.\n"
            show happy t neutral onlayer back
            jump happy_menu

        "{i}• ''Excuse me.'' [[Get up.]{/i}" if happy_get_up_attempt == False:
            jump happy_get_up_attempt_join

        "{i}• [[Silently push yourself from your seat.]{/i}" if happy_get_up_attempt == False:
            jump happy_get_up_attempt_join

        "{i}• [[Slay the Princess.]{/i}" if happy_slay_explore == False and happy_get_up_attempt == False:
            $ happy_slay_explore = True
            label happy_get_up_attempt_join:
                $ happy_torch_comment_immediate = False
                $ happy_get_up_attempt = True
                voice "audio/_pristine/voice/happy/narrator/107.flac"
                play audio "audio/one_shot/new/STP_strangershuffle_5.flac"
                play tertiary "audio/final/Damsel_FireSHootingOut_1.flac"
                show fire happy flare onlayer back
                show player happy shadow hands onlayer back at shakeshort
                with Dissolve(1.0)
                n "But as you attempt to get up, the torches flare, and shadowed hands pin your wrists to the arms of your too-comfortable seat.\n"
                if happy_slay_explore:
                    voice "audio/_pristine/voice/happy/narrator/108.flac"
                    show fire happy onlayer back
                    show player happy chair hands onlayer back
                    with Dissolve(1.0)
                    n "There will be no getting up. At least not for now.\n"
                else:
                    voice "audio/_pristine/voice/happy/narrator/109.flac"
                    show fire happy onlayer back
                    show player happy chair hands onlayer back
                    with Dissolve(1.0)
                    n "There will be no getting up. There will be no attempts to slay her. At least not for now.\n"

                jump happy_menu


label happy_torches:

    if happy_torches == 4:
        $ happy_torch_comment_immediate = True
        stop music
        play audio "audio/final/Damsel_FireSHootingOut_1.flac"
        show happy t nervous onlayer back
        $ happy_torches -= 1
        $ renpy.pause(0.1)
        $ happy_torches += 1
        $ renpy.pause(0.1)
        $ happy_torches -= 1
        $ renpy.pause(0.1)
        $ happy_torches += 1
        $ renpy.pause(0.1)
        $ happy_torches -= 1
        $ renpy.pause(0.1)
        voice "audio/_pristine/voice/happy/narrator/110.flac"
        n "As the words leave her mouth, one of the torches on the wall sputters, and then goes out entirely.\n" id happy_torches_c4f5488d
        voice "audio/_pristine/voice/happy/princess/59.flac"
        show happy t scared talk onlayer back
        with dissolve
        p "What just happened? Did I do something wrong?\n"
        show happy t sad smile onlayer back
        if trait_paranoid:
            voice "audio/_pristine/voice/happy/paranoid/34.flac"
            paranoid "A light went out. Maybe a coincidence, but... maybe not.\n"
            if happy_get_up_attempt:
                voice "audio/_pristine/voice/happy/paranoid/35.flac"
                paranoid "And if they all go out, there won't be any shadows left to hold us.\n"
            elif happy_shadow_acted:
                voice "audio/_pristine/voice/happy/paranoid/36.flac"
                paranoid "And if they all go out, there won't be any shadows left to set the table.\n"
            if happy_shadow_acted or happy_get_up_attempt:
                voice "audio/_pristine/voice/happy/hero/55.flac"
                hero "Won't there be... more shadow?\n"
                voice "audio/_pristine/voice/happy/paranoid/37a.flac"
                paranoid "No. Just darkness without a shape.\n"
                if happy_get_up_attempt:
                    voice "audio/_pristine/voice/happy/narrator/111a.flac"
                    n "And then it won't be able to hold you any longer. You'll be able to do what you're supposed to.\n"
        elif trait_opportunist:
            voice "audio/_pristine/voice/happy/opportunist/36a.flac"
            opportunist "Not a fan of whatever just happened! I don't want to sit in the dark. Losers sit in the dark. I want to sit in a brightly lit, spacious room where we can see our beautiful queenly wife.\n"
        play music "audio/_pristine/music/happy/Q -1.flac" loop
        voice "audio/_pristine/voice/happy/narrator/112.flac"
        play audio "audio/final/Damsel_FireSHootingOut_1.flac"
        show fire happy flare onlayer back
        with dissolve
        n "As if in response to the dousing of their brother, the other three torches blaze brighter, their flames licking at the walls. Their shadows deepen, dancing angrily across the stone.\n"
        show fire happy onlayer back
        with dissolve
        jump happy_menu
    elif happy_torches == 3:
        $ happy_torch_comment_immediate = True
        stop music
        show happy t scared onlayer back
        $ happy_torches -= 1
        $ renpy.pause(0.1)
        $ happy_torches += 1
        $ renpy.pause(0.1)
        $ happy_torches -= 1
        $ renpy.pause(0.1)
        $ happy_torches += 1
        $ renpy.pause(0.1)
        $ happy_torches -= 1
        $ renpy.pause(0.1)
        voice "audio/_pristine/voice/happy/narrator/113.flac"
        n "As the words leave the Princess' mouth, another torch goes out. Again, the remaining flames burn brighter, and the shadow dances faster.\n" id happy_torches_112211ea
        voice "audio/_pristine/voice/happy/princess/60.flac"
        play music "audio/_pristine/music/happy/Q -2.flac" loop
        show happy t nervous talk onlayer back
        with dissolve
        p "I'm happy! I promise! We're both so, so, happy here! You don't have to be upset!\n"
        voice "audio/_pristine/voice/happy/narrator/114.flac"
        show happy t scared onlayer back
        with dissolve
        n "This is... awful.\n"
        if trait_paranoid:
            if happy_paranoid_deduce == False:
                $ happy_paranoid_deduce = True
                voice "audio/_pristine/voice/happy/paranoid/38.flac"
                paranoid "It's him, isn't it? He's making all of this happen. He's the one who's trapped us here.\n"
                voice "audio/_pristine/voice/happy/hero/56.flac"
                hero "Who?\n"
                $ achievement.grant("ACH_HAPPY_SHADOWS")
                voice "audio/_pristine/voice/happy/paranoid/39.flac"
                paranoid "The lovesick one. The one from last time. He's not gone. He's just with her now. {i}He's{/i} the shadow.\n"
            else:
                voice "audio/_pristine/voice/happy/paranoid/40.flac"
                paranoid "I think we all know that we're not happy. We just have to admit it to ourselves.\n"
        else:
            voice "audio/_pristine/voice/happy/opportunist/37.flac"
            opportunist "Isn't it great that we're all having such a lovely time together? We just have to stay positive and realize how happy we are, then all of those lights will stay on and keep showing us all the cool stuff we have!\n"
            voice "audio/_pristine/voice/happy/hero/57.flac"
            hero "... Yeah. Sure.\n"
        jump happy_menu
    else:

        play audio "audio/final/Damsel_FireSHootingOut_1.flac"
        stop music
        show happy t nervous onlayer back
        $ happy_torches -= 1
        $ renpy.pause(0.1)
        $ happy_torches += 1
        $ renpy.pause(0.1)
        $ happy_torches -= 1
        $ renpy.pause(0.1)
        $ happy_torches += 1
        $ renpy.pause(0.1)
        $ happy_torches -= 1
        $ renpy.pause(0.1)
        voice "audio/_pristine/voice/happy/narrator/115.flac"
        n "The third torch sputters out. The Princess' shadow dances furiously against the far wall.\n" id happy_torches_4caa6bbd
        voice "audio/_pristine/voice/happy/princess/61.flac"
        play music "audio/_pristine/music/happy/Q -3.flac" loop
        show happy t empty smile talk onlayer back
        with dissolve
        p "There's just one left. What's going to happen when it goes out?\n"
        show happy t empty smile onlayer back
        label happy_torches_final:
            menu:
                extend ""

                "{i}• ''What do you think will happen?''{/i}":
                    voice "audio/_pristine/voice/happy/princess/62.flac"
                    show happy t sad smile talk onlayer back
                    with dissolve
                    p "I'm too scared to say. What if my answer is what blows it out?\n"
                    show happy t sad onlayer back
                    menu:
                        extend ""

                        "{i}• ''If you could do anything in the world, what would it be? What would {b}you{/b} choose?''{/i}":
                            label happy_dance_comment_join:
                                default happy_dance_mentioned = False
                                $ happy_dance_mentioned = True
                                voice "audio/_pristine/voice/happy/princess/63.flac"
                                show happy t smile genuine talk onlayer back
                                with dissolve
                                p "I think... I'd like to dance under the stars.\n"
                                voice "audio/_pristine/voice/happy/hero/58.flac"
                                show happy t smile genuine onlayer back
                                with dissolve
                                hero "That sounds lovely.\n"
                                voice "audio/_pristine/voice/happy/princess/64a.flac"
                                show happy t serious talk onlayer back
                                with dissolve
                                p "But there aren't any stars here. I'd have to leave.\n"
                                voice "audio/_pristine/voice/happy/narrator/116.flac"
                                play audio "audio/one_shot/new/STP_strangershuffle_5.flac"
                                play tertiary "audio/final/Damsel_FireSHootingOut_1.flac"
                                show shadows happy grab onlayer back
                                show fire happy flare onlayer back
                                show happy t shadow tight sad onlayer back
                                with dissolve
                                n "As she says that, the shadow rushes forward and tightens its grip on her wrists.\n"
                                #voice "audio/_pristine/voice/happy/princess/65.flac"
                                voice "audio/_pristine/voice/happy/princess/69.flac"
                                show happy t shadow tight talk quiet onlayer back
                                with dissolve
                                #p "I want to leave. I've always wanted to leave.\n"
                                p "I'm not happy here. I don't think I ever was.\n"

                        "{i}• ''If your answer would blow it out, then it needs to be blown out.''{/i}":
                            voice "audio/_pristine/voice/happy/princess/66.flac"
                            show happy t serious talk onlayer back
                            with dissolve
                            p "It does, doesn't it? Then... that's my answer.\n"

                        "{i}• ''Then don't say it. We don't have to let it go out.''{/i}":
                            jump happy_torch_end

                        "{i}• [[Say nothing.]{/i}":
                            voice "audio/_pristine/voice/happy/princess/67.flac"
                            show happy t serious talk onlayer back
                            with dissolve
                            p "I can't do this anymore.\n"

                "{i}• ''Don't worry about what's going to happen. If you could do anything in the world, what would it be? What would {b}you{/b} choose?''{/i}":
                    jump happy_dance_comment_join

                "{i}• ''Whatever the shadows have been showing us isn't real. We need to see what happens when the lights go out.''{/i}":
                    voice "audio/_pristine/voice/happy/princess/68.flac"
                    show happy t sad smile talk onlayer back
                    with dissolve
                    p "We do, don't we?\n"
                    voice "audio/_pristine/voice/happy/princess/69.flac"
                    show happy t serious talk onlayer back
                    with dissolve
                    p "I'm not happy here. I don't think I ever was.\n"

                "{i}• ''We don't have to let it go out.''{/i}":
                    label happy_torch_end:
                        voice "audio/_pristine/voice/happy/narrator/117.flac"
                        show happy tf fond onlayer back
                        with dissolve
                        n "The Princess turns to face the final torch, eyeing it with an empty but gentle fondness.\n"
                        voice "audio/_pristine/voice/happy/princess/70a.flac"
                        show happy tf fond talk onlayer back
                        with dissolve
                        p "Wouldn't that be nice? I love the little life we've built. And I hope it never ends.\n"
                        play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 15.0
                        stop music fadeout 15.0
                        stop music2 fadeout 15.0
                        stop music3 fadeout 15.0
                        stop music4 fadeout 15.0
                        stop music5 fadeout 15.0
                        stop sound fadeout 15.0
                        stop tertiary fadeout 15.0
                        hide happy onlayer back
                        hide player onlayer back
                        show quiet creep1 onlayer back at Position(ypos=1125)
                        show happy tf final onlayer back at Position(ypos=1250)
                        show player happy chair hands onlayer front at Position(ypos=1150)
                        with Dissolve(1.0)
                        truth "And it doesn't end, and the flame burns brightly grey eternal.\n"
                        if trait_paranoid:
                            voice "audio/_pristine/voice/happy/paranoid/41.flac"
                            show quiet creep2 onlayer back at Position(ypos=1125)
                            with Dissolve(1.50)
                            paranoid "I suppose... all our worry was for nothing. It's just playing pretend. There's nothing wrong with that.\n"
                        else:
                            voice "audio/_pristine/voice/happy/opportunist/38a.flac"
                            show quiet creep2 onlayer back at Position(ypos=1125)
                            with Dissolve(1.5)
                            opportunist "We did it, didn't we? We found the right answer. We made everyone happy, and nobody had to get stabbed. Great work, team.\n"
                            voice "audio/_pristine/voice/happy/hero/59.flac"
                            hero "Yeah... everyone is happy.\n"
                        $ gallery_happy.unlock_item(6)
                        $ renpy.save_persistent()
                        voice "audio/_pristine/voice/happy/princess/71.flac"
                        show happy tf final talk onlayer back
                        show quiet creep3 onlayer back at Position(ypos=1125)
                        with Dissolve(1.5)
                        p "It's always been cold here, hasn't it?\n"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show farback quiet onlayer farback at Position(ypos=1125)
                        hide bg onlayer back
                        hide fire onlayer back
                        hide game onlayer back
                        hide food onlayer back
                        hide shadows onlayer back
                        hide shadows onlayer front
                        hide player onlayer front
                        hide player onlayer back
                        hide happy onlayer front
                        hide happy onlayer back
                        show hands happy fire 1 onlayer front at Position(ypos=1250)
                        with Dissolve(1.0)
                        $ renpy.pause(0.125)
                        show hands happy fire 2 onlayer front
                        with Dissolve(1.0)
                        $ renpy.pause(0.125)
                        show hands happy fire 3 onlayer front
                        with Dissolve(0.75)
                        $ renpy.pause(0.125)
                        show hands happy fire 4 onlayer front
                        with Dissolve(0.25)
                        $ renpy.pause(0.125)
                        show hands happy fire 5 onlayer front
                        with Dissolve(0.2)
                        $ renpy.pause(0.125)
                        show hands happy fire 6 onlayer front
                        with Dissolve(0.2)
                        $ renpy.pause(0.125)
                        hide hands onlayer front
                        with Dissolve(0.2)
                        $ renpy.pause(0.125)
                        $ blade_held = False
                        $ default_mouse = "default"
                        hide fore onlayer front
                        hide fore onlayer inyourface
                        hide farback onlayer farback
                        hide bg onlayer back
                        hide mid onlayer back
                        hide stars onlayer farback
                        hide bg onlayer back
                        hide quiet onlayer back
                        hide quiet onlayer front
                        show farback quiet onlayer farback at Position(ypos=1125)
                        with Dissolve(4.0)
                        show mirror quiet distant onlayer back at Position(ypos=1125)
                        if loops_finished != 0:
                            truth "You do not get the chance to respond, nor will you ever. It's time to leave. Memory returns.\n"
                        else:
                            truth "You do not get the chance to respond. Something has taken her away, and it's left something else in her place.\n"
                        $ achievement.grant("ACH_HAPPY_FLAMES")
                        #$ trait_smitten = True
                        $ current_princess = "happydry"
                        $ happy_end = "tend"
                        $ princess_kept += 1
                        $ princess_deny += 1
                        jump mirror_start
                        # END

                "{i}• [[Say nothing.]{/i}":
                    voice "audio/_pristine/voice/happy/princess/72.flac"
                    show happy t sad smile talk onlayer back
                    with dissolve
                    p "I can't do this anymore.\n"

        $ gallery_happy.unlock_item(7)
        $ renpy.save_persistent()
        $ happy_torches = 0
        stop secondary
        stop music
        play secondary "audio/looping/uncomfortable ambiance.ogg" loop
        voice "audio/_pristine/voice/happy/narrator/118.flac"
        hide shadows onlayer back
        hide fire onlayer back
        hide food onlayer back
        hide game onlayer back
        show bg happy dark onlayer back
        show happy d sob onlayer back
        with Dissolve(1.5)
        n "The Princess sobs, burying her face in her hands as the final torch blows out.\n"
        play music "audio/_pristine/music/happy/LGO Piano Solo.flac" loop
        jump happy_climax


label happy_climax:
    default happy_climax_stood = False
    default happy_slay_attempted = False
    default happy_leaving_hand_hold = False
    menu:
        extend ""

        "{i}• ''I feel empty.''{/i}":
            voice "audio/_pristine/voice/happy/narrator/119.flac"
            show happy d neutral onlayer back
            with dissolve
            n "She raises her head, mascara trailing down her cheeks.\n"
            voice "audio/_pristine/voice/happy/princess/73a.flac"
            show happy d sad talk onlayer back
            with dissolve
            p "Me too. It feels like an important part of me is gone, but I'm still here. I don't know what to do with that. I don't know how we're supposed to pick up the pieces.\n"
            jump happy_climax_silent

        "{i}• ''So that's that, huh?''{/i}":
            voice "audio/_pristine/voice/happy/narrator/119.flac"
            show happy d neutral onlayer back
            with dissolve
            n "She raises her head, mascara trailing down her cheeks.\n"
            voice "audio/_pristine/voice/happy/princess/74.flac"
            show happy d sad talk onlayer back
            with dissolve
            p "Yeah. I guess that's that. I can't believe it's over. It felt like it was supposed to last forever.\n"
            jump happy_climax_silent

        "{i}• ''Why are you crying?''{/i}":
            voice "audio/_pristine/voice/happy/narrator/119.flac"
            show happy d neutral onlayer back
            with dissolve
            n "She raises her head, mascara trailing down her cheeks.\n"
            voice "audio/_pristine/voice/happy/princess/75.flac"
            show happy d sad talk onlayer back
            with dissolve
            p "I don't know. It feels like an important part of me is gone, but I'm still here. I don't know what to do with that. I don't know how I'm supposed to pick up the pieces.\n"
            jump happy_climax_silent

        "{i}• ''Are you okay?''{/i}":
            voice "audio/_pristine/voice/happy/narrator/119.flac"
            show happy d neutral onlayer back
            with dissolve
            n "She raises her head, mascara trailing down her cheeks.\n"
            voice "audio/_pristine/voice/happy/princess/76.flac"
            show happy d sad talk onlayer back
            with dissolve
            p "No. It feels like an important part of me is gone, but I'm still here. I don't know what to do with that. I don't know how I'm supposed to pick up the pieces.\n"
            jump happy_climax_silent

        "{i}• ''Well this sucks.''{/i}":
            voice "audio/_pristine/voice/happy/narrator/119.flac"
            show happy d neutral onlayer back
            with dissolve
            n "She raises her head, mascara trailing down her cheeks.\n"
            voice "audio/_pristine/voice/happy/princess/77.flac"
            show happy d sad talk onlayer back
            with dissolve
            p "Yeah. It really, really does.\n"
            jump happy_climax_silent

        "{i}• ''You can open your eyes. I'm still here, you know.''{/i}":
            voice "audio/_pristine/voice/happy/narrator/119.flac"
            show happy d neutral onlayer back
            with dissolve
            n "She raises her head, mascara trailing down her cheeks.\n"
            voice "audio/_pristine/voice/happy/princess/78.flac"
            show happy d neutral talk onlayer back
            with dissolve
            p "So you are. It's dark in here, isn't it?\n"
            jump happy_climax_silent

        "{i}• ''Nothing's changed. We're just sitting in the dark.''{/i}":
            voice "audio/_pristine/voice/happy/narrator/119.flac"
            show happy d neutral onlayer back
            with dissolve
            n "She raises her head, mascara trailing down her cheeks.\n"
            voice "audio/_pristine/voice/happy/princess/79.flac"
            show happy d neutral talk onlayer back
            with dissolve
            p "That's a really nice way of putting things. But, it is a little different, isn't it?\n"
            voice "audio/_pristine/voice/happy/princess/80.flac"
            show happy d sad talk onlayer back
            with dissolve
            p "It's quiet now. There's no more voice telling me how much he loves me.\n"
            jump happy_climax_silent

        "{i}• ''I'm sorry, I feel like all of this is my fault.''{/i}":
            voice "audio/_pristine/voice/happy/narrator/119.flac"
            show happy d neutral onlayer back
            with dissolve
            n "She raises her head, mascara trailing down her cheeks.\n"
            voice "audio/_pristine/voice/happy/princess/EXTRA2.flac"
            show happy d neutral talk onlayer back
            with dissolve
            p "... your fault? We were all just trying to make things work here. It just... didn't happen that way.\n"
            voice "audio/_pristine/voice/happy/princess/EXTRA3.flac"
            show happy d sad talk onlayer back
            with dissolve
            p "I don't think this is the sort of thing anybody needs to apologize for. Even if we both feel empty. Even if an important part of us is gone.\n"
            jump happy_climax_silent

        "{i}• [[Slay the Princess.]{/i}" if happy_slay_attempted == False:
            label happy_slay:
                default happy_mixed_signals = False
                $ happy_slay_attempted = True
                voice "audio/_pristine/voice/happy/narrator/120.flac"
                n "Are... you sure you want to do that?\n"
                if trait_opportunist:
                    $ happy_mixed_signals = True
                    voice "audio/_pristine/voice/happy/opportunist/39.flac"
                    opportunist "You're, uh... sending us some real mixed signals, boss.\n"
                    voice "audio/_pristine/voice/happy/narrator/121.flac"
                    n "I suppose I am. I'm just worried that I might have made a terrible mistake.\n"
                    voice "audio/_pristine/voice/happy/hero/60.flac"
                    hero "A terrible mistake? Isn't she supposed to end the entire world?\n"
                    voice "audio/_pristine/voice/happy/narrator/122.flac"
                    n "Yes. And that hasn't changed. I'm just not sure the world I want is worth it.\n"
                    voice "audio/_pristine/voice/happy/hero/61a.flac"
                    hero "But... how can a saved world ever be worse than one that's gone?\n"
                    #voice "audio/_pristine/voice/happy/hero/61.flac"
                    #hero "If the alternative is {i}no{/i} world, how can a saved world ever be worse?\n"
                    voice "audio/_pristine/voice/happy/narrator/123.flac"
                    n "See. That's exactly what I thought.\n"
                else:
                    voice "audio/_pristine/voice/happy/hero/62b.flac"
                    hero "Isn't this what you wanted us to do from the beginning?\n"
                    voice "audio/_pristine/voice/happy/narrator/124.flac"
                    n "It is. I just... I think I might have made a terrible mistake.\n"
                    voice "audio/_pristine/voice/happy/paranoid/42.flac"
                    paranoid "A terrible mistake? You sold this as her being a threat to the entire world. Was that a lie?\n"
                    voice "audio/_pristine/voice/happy/narrator/125.flac"
                    n "No. It wasn't. I'm just not sure the world I want is worth it.\n"
                    voice "audio/_pristine/voice/happy/paranoid/43.flac"
                    paranoid "This is... this is some sort of trick! You're trying to use reverse psychology on us. Or... what if this is reverse-{i}reverse{/i} psychology?\n"
                voice "audio/_pristine/voice/happy/narrator/126.flac"
                n "Think what you will. I'm only here to guide you. You're the one who makes the decisions.\n"
                if trait_opportunist:
                    voice "audio/_pristine/voice/happy/opportunist/40.flac"
                    opportunist "Well, well, looks like there's nobody around who can tell us what to do anymore. First the shadows got blown out, now even the big-shot Narrator man is having doubts. We don't need to waste our time slaying her, we've clearly won.\n"
                menu:
                    extend ""

                    "{i}• You're right. What was I thinking?{/i}":
                        voice "audio/_pristine/voice/happy/narrator/extra1a.flac"
                        n "I can't believe I'm saying this, but... I think this is for the best. Thank you.\n"
                        if happy_climax_stood:
                            jump happy_stairs_silent
                        else:
                            jump happy_climax_silent

                    "{i}• Don't get cold feet now. This is for the good of everyone. I'm saving the world here. [[Slay the Princess.]{/i}":
                        jump happy_murder_end

                    "{i}• I know what I decided to do. [[Slay the Princess.]{/i}":
                        jump happy_murder_end

                label happy_murder_end:
                    if happy_climax_stood:
                        voice "audio/_pristine/voice/happy/narrator/127.flac"
                        show happy leaving end onlayer front
                        with dissolve
                        n "The Princess doesn't try to flee as murderous intent settles into your eyes.\n"
                        voice "audio/_pristine/voice/happy/narrator/128.flac"
                        $ default_mouse = "blade"
                        $ blade_held = True
                        play audio "audio/one_shot/knife_tighten.flac"
                        hide happy onlayer front
                        show cg happy slay grab onlayer front at Position(ypos=1125)
                        with dissolve
                        n "Nor does she resist as you wrap your fingers around the blade dangling from her neck.\n"
                    else:
                        voice "audio/_pristine/voice/happy/narrator/129.flac"
                        play secondary "audio/_pristine/sfx/_chair_drag.flac"
                        queue secondary "audio/one_shot/footsteps_creaky.flac"
                        hide happy onlayer back
                        hide fire onlayer back
                        hide player onlayer back
                        hide bg onlayer back
                        scene bg generic dark onlayer back at Position(ypos=1125)
                        show cg happy slay begin onlayer front at Position(ypos=1125)
                        with fade
                        n "The Princess doesn't try to flee as you cross the room, murderous intent settling into your eyes. All she does is stand to face you.\n"
                        $ default_mouse = "blade"
                        $ blade_held = True
                        voice "audio/_pristine/voice/happy/narrator/130.flac"
                        play audio "audio/one_shot/knife_tighten.flac"
                        show cg happy slay grab onlayer front at Position(ypos=1125)
                        with dissolve
                        n "She offers no resistance as your fingers wrap around the blade dangling from her neck.\n"
                    voice "audio/_pristine/voice/happy/narrator/131.flac"
                    play audio "audio/_pristine/sfx/Fury Body Horror_3.flac"
                    $ default_mouse = "blood"
                    show cg happy slay murder onlayer front at Position(ypos=1125)
                    with dissolve
                    n "As the weapon sinks deep into her heart, all she manages are three muttered words.\n"
                    voice "audio/_pristine/voice/happy/princess/81.flac"
                    show cg happy slay murder talk onlayer front at Position(ypos=1125)
                    with dissolve
                    p "It's finally over.\n"
                    $ gallery_happy.unlock_item(8)
                    $ renpy.save_persistent()
                    voice "audio/_pristine/voice/happy/narrator/132.flac"
                    $ blade_held = False
                    $ default_mouse = "default"
                    play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 15.0
                    stop music fadeout 15.0
                    stop music2 fadeout 15.0
                    stop music3 fadeout 15.0
                    stop music4 fadeout 15.0
                    stop music5 fadeout 15.0
                    stop sound fadeout 15.0
                    stop tertiary fadeout 15.0
                    show quiet creep1 onlayer back at Position(ypos=1125)
                    show cg happy slay cold onlayer front at Position(ypos=1125)
                    with Dissolve(1.0)
                    n "I didn't think it would be so awful to help you see this through. But... all of this was for a reason. The world is better off without her.\n"
                    voice "audio/_pristine/voice/happy/hero/63.flac"
                    show quiet creep2 onlayer back
                    with dissolve
                    hero "I really hope that's true.\n"
                    if trait_opportunist:
                        voice "audio/_pristine/voice/happy/opportunist/41.flac"
                        opportunist "They always say it's lonely at the top. I didn't think they actually meant it.\n"
                    else:
                        voice "audio/_pristine/voice/happy/paranoid/44.flac"
                        paranoid "We'll never know, will we?\n"
                    voice "audio/_pristine/voice/happy/princess/82.flac"
                    show cg happy slay cold talk onlayer front at Position(ypos=1125)
                    show quiet creep3 onlayer back
                    with dissolve
                    p "I feel... cold. But I guess I've felt that way for a long, long time.\n"
                    play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                    hide cg onlayer front
                    show hands happy slay1 onlayer front at Position(ypos=1125)
                    with Dissolve(1.0)
                    $ renpy.pause(0.125)
                    show hands happy slay 2 onlayer front
                    with Dissolve(1.0)
                    $ renpy.pause(0.125)
                    show hands happy slay 3 onlayer front
                    with Dissolve(0.75)
                    $ renpy.pause(0.125)
                    show hands happy slay 4 onlayer front
                    with Dissolve(0.5)
                    $ renpy.pause(0.125)
                    show hands happy slay 5 onlayer front
                    with Dissolve(0.5)
                    $ renpy.pause(0.125)
                    hide hands onlayer front
                    with Dissolve(0.5)
                    $ renpy.pause(0.125)
                    $ blade_held = False
                    $ default_mouse = "default"
                    hide bg onlayer back
                    hide bg onlayer front
                    hide player onlayer front
                    hide player onlayer back
                    hide fore onlayer front
                    hide fore onlayer inyourface
                    hide farback onlayer farback
                    hide bg onlayer back
                    hide mid onlayer back
                    hide stars onlayer farback
                    hide bg onlayer back
                    hide quiet onlayer back
                    hide quiet onlayer front
                    show farback quiet onlayer farback at Position(ypos=1125)
                    with Dissolve(4.0)
                    show mirror quiet distant onlayer back at Position(ypos=1125)
                    if loops_finished != 0:
                        truth "Though you've pierced her heart, you do not see her die. Nor will you ever. It's time for you to leave. Memory returns.\n"
                    else:
                        truth "Though you've pierced her heart, you do not see her die. Something has taken her away, and it's left something else in her place.\n"
                    $ achievement.grant("ACH_HAPPY_SLAY")
                    $ happy_end = "slay"
                    $ princess_kept += 1
                    $ princess_satisfy += 1
                    jump mirror_start

                    # END

        "{i}• [[Say nothing.]{/i}":
            label happy_climax_silent:
                #voice "audio/_pristine/voice/happy/narrator/longpause.flac"
                voice "audio/_pristine/voice/happy/narrator/67.flac"
                show happy d sad onlayer back
                with dissolve
                #n "A long pause...\n"
                n "The Princess' eyes dart to the floor.\n"
                voice "audio/_pristine/voice/happy/princess/83.flac"
                show happy d neutral talk onlayer back
                with dissolve
                p "Well... we can't sit here forever. That part of us is over.\n"

    $ happy_climax_stood = True
    voice "audio/_pristine/voice/happy/narrator/133.flac"
    play secondary "audio/_pristine/sfx/_chair_drag.flac"
    hide bg onlayer back
    hide player onlayer back
    hide happy onlayer back
    scene bg happy dark onlayer back at Position(ypos=1350)
    show cg happy rise onlayer back at Position(ypos=1350)
    with Dissolve(1.5)
    n "The Princess pushes herself from her chair, and you instinctively do the same, waiting by the top of the stairs as she quietly crosses the room.\n"
    $ quick_menu = False
    play audio "audio/one_shot/footsteps_creaky.flac"
    voice "audio/_pristine/voice/happy/princess/84.flac"
    hide bg onlayer back
    hide cg onlayer back
    scene bg black
    with fade
    scene bg happy leaving hand offer onlayer back at Position(ypos=1125)
    show happy leaving neutral talk onlayer front at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    p "Do you... still care about me?\n"
    show happy leaving neutral onlayer front
    label happy_climax_stair:
        menu:
            extend ""

            "{i}• ''Of course I do. I don't think I'll ever stop.''{/i}":
                voice "audio/_pristine/voice/happy/princess/85.flac"
                show happy leaving relieved talk onlayer front
                with dissolve
                p "Oh! I... wasn't expecting you to say that. I still care about you, too. So maybe this wasn't all bad.\n"
                voice "audio/_pristine/voice/happy/princess/86.flac"
                show happy leaving sad smile talk onlayer front
                with dissolve
                p "But I don't think this place is for us anymore. I think we need to go.\n"
                show happy leaving sad smile onlayer front
                jump happy_stairs_leaving

            "{i}• ''Whatever we had between us wasn't real. This is real.''{/i}":
                voice "audio/_pristine/voice/happy/princess/87.flac"
                show happy leaving neutral talk onlayer front
                with dissolve
                p "I don't know what 'this' is.\n"
                show happy leaving neutral onlayer front
                menu:
                    extend ""

                    "{i}• ''I'd like to find out.''{/i}":
                        voice "audio/_pristine/voice/happy/princess/88.flac"
                        show happy leaving sad smile talk onlayer front
                        with dissolve
                        p "Me too. And I don't think we're going to find anything here. So... I guess it's time for us to leave.\n"
                        show happy leaving sad smile onlayer front

                    "{i}• ''It's us.''{/i}":
                        voice "audio/_pristine/voice/happy/princess/89.flac"
                        show happy leaving neutral talk onlayer front
                        with dissolve
                        p "We can be us anywhere. And I think we're both done with being who this place makes us. So... I guess it's time for us to leave.\n"
                        show happy leaving neutral onlayer front

                    "{i}• ''Neither do I.''{/i}":
                        voice "audio/_pristine/voice/happy/princess/90.flac"
                        show happy leaving tired talk onlayer front
                        with dissolve
                        p "Then... maybe we need to find that out for ourselves. Maybe it's time for us to leave.\n"
                        show happy leaving tired onlayer front

                    "{i}• [[Say nothing.]{/i}":
                        voice "audio/_pristine/voice/happy/princess/91.flac"
                        show happy leaving tired talk onlayer front
                        with dissolve
                        p "Yeah. It's time for us to leave.\n"
                        show happy leaving tired onlayer front

                jump happy_stairs_leaving


            "{i}• ''I don't know if I ever have. But maybe I can now.''{/i}":
                voice "audio/_pristine/voice/happy/princess/92.flac"
                show happy leaving sad smile talk onlayer front
                with dissolve
                p "That's... a nice thought.\n"
                voice "audio/_pristine/voice/happy/princess/93.flac"
                show happy leaving tired talk onlayer front
                with dissolve
                p "I think this place was bad for us. It was keeping us... small. I think it's time for us to go.\n"
                show happy leaving tired onlayer front
                jump happy_stairs_leaving

            "{i}• ''I'm not sure I've ever had the chance to figure out how I feel about you. I've just wanted to leave since the moment I found myself in the woods.''{/i}":
                voice "audio/_pristine/voice/happy/princess/94.flac"
                show happy leaving tired talk onlayer front
                with dissolve
                p "Then... maybe that's what we should do. Leave.\n"
                show happy leaving tired onlayer front
                jump happy_stairs_leaving

            "{i}• ''No.''{/i}":
                voice "audio/_pristine/voice/happy/princess/95.flac"
                show happy leaving tired talk onlayer front
                with dissolve
                p "I guess neither of us really know what it means to care about each other... do we?\n"
                voice "audio/_pristine/voice/happy/princess/96.flac"
                show happy leaving neutral talk onlayer front
                with dissolve
                p "Maybe we'll learn to, eventually. Or... maybe we won't. But either way, we aren't going to figure it out here. I think it's time to leave. Come on.\n"
                show happy leaving neutral onlayer front
                jump happy_stairs_leaving

            "{i}• [[Slay the Princess.]{/i}" if happy_slay_attempted == False:
                jump happy_slay

            "{i}• [[Say nothing.]{/i}":
                label happy_stairs_silent:
                    voice "audio/_pristine/voice/happy/princess/97.flac"
                    show happy leaving tired talk onlayer front
                    with dissolve
                    p "It's... a loaded question, isn't it? I'm not even sure I know what it means to care about someone.\n"
                    voice "audio/_pristine/voice/happy/princess/98.flac"
                    show happy leaving neutral talk onlayer front
                    with dissolve
                    p "I think figuring that out is going to take time. And I don't think this is the sort of place where we figure anything out. It wants to keep us small.\n"
                    voice "audio/_pristine/voice/happy/princess/99.flac"
                    show happy leaving tired talk onlayer front
                    with dissolve
                    p "Let's just get out of here.\n"
                    show happy leaving tired onlayer front
                    label happy_stairs_leaving:
                        stop music fadeout 1.0
                        menu:
                            extend ""

                            "{i}• [[Offer her your hand.]{/i}":
                                $ gallery_happy.unlock_item(9)
                                $ renpy.save_persistent()
                                $ happy_leaving_hand_hold = True
                                play audio "audio/_pristine/sfx/_step_single.flac"
                                voice "audio/_pristine/voice/happy/narrator/134.flac"
                                show happy leaving hand offer onlayer front
                                show player happy leaving hand offer onlayer front at Position(ypos=1125)
                                with dissolve
                                n "As the Princess steps towards the stairs, you offer her your hand.\n"
                                play music "audio/_pristine/music/happy/LGO Full.flac" loop
                                play audio "audio/one_shot/knife_tighten.flac"
                                voice "audio/_pristine/voice/happy/narrator/135.flac"
                                hide player onlayer front
                                show happy leaving take hand onlayer front
                                with Dissolve(1.0)
                                n "The corners of her mouth curl into a demure smile, and she gently takes your hand in hers. She's cold, and a little clammy. But her skin against yours is the most real thing you have ever felt.\n"
                                jump happy_leave_finale

                            "{i}• [[Leave.]{/i}":
                                play music "audio/_pristine/music/happy/LGO Full.flac" loop
                                jump happy_leave_finale

label happy_leave_finale:
    $ gallery_happy.unlock_item(10)
    $ renpy.save_persistent()
    if happy_slay_attempted:
        voice "audio/_pristine/voice/happy/hero/64.flac"
        hero "You're really okay with this, aren't you? With the end of the world.\n"
        voice "audio/_pristine/voice/happy/narrator/136.flac"
        n "I think I have to be.\n"
    else:
        voice "audio/_pristine/voice/happy/hero/65.flac"
        hero "You're offering suprisingly little resistance. If we leave the cabin, doesn't that... end the world?\n"
        if trait_paranoid:
            voice "audio/_pristine/voice/happy/paranoid/45.flac"
            paranoid "It does if He's telling the truth.\n"
        else:
            if happy_mixed_signals == False:
                voice "audio/_pristine/voice/happy/opportunist/42.flac"
                opportunist "He's right, you know. You're giving us some real mixed signals, boss.\n"
        voice "audio/_pristine/voice/happy/narrator/137.flac"
        n "Yes, well. I've seen my fairy-tale ending. And I think there might be worse things than the end of the world.\n"
        if trait_opportunist:
            voice "audio/_pristine/voice/happy/opportunist/43.flac"
            opportunist "Well, this is less work for us, anyways.\n"
        else:
            voice "audio/_pristine/voice/happy/paranoid/46.flac"
            paranoid "It really was just all meaningless blather, then, wasn't it?\n"
        voice "audio/_pristine/voice/happy/narrator/138.flac"
        n "Think what you will. I'm done fighting.\n"
    play audio "audio/one_shot/footsteps_creaky.flac"
    voice "audio/_pristine/voice/happy/narrator/139.flac"
    hide bg onlayer back
    hide happy onlayer front
    if happy_leaving_hand_hold:
        scene cg happy leaving stairs onlayer back at Position(ypos=1125)
    else:
        scene cg happy leaving stairs nohand onlayer back at Position(ypos=1125)
    with fade
    n "You and the Princess don't exchange words as you descend the stairs to the cabin's entrance.\n"
    play audio "audio/one_shot/door_bedroom.flac"
    voice "audio/_pristine/voice/happy/narrator/140.flac"
    stop sound
    stop secondary
    stop tertiary
    if happy_leaving_hand_hold == False:
        $ gallery_happy.unlock_item(11)
        $ renpy.save_persistent()
    hide cg onlayer back
    scene bg black
    with fade
    scene farback happy outside onlayer farback at Position(ypos=1125)
    show bg happy outside onlayer back at Position(ypos=1125)
    show mid happy outside onlayer front at Position(ypos=1125)
    if happy_leaving_hand_hold:
        show cg happy outside onlayer inyourface at Position(ypos=1125)
    else:
        show cg happy outside nohand onlayer inyourface at Position(ypos=1125)
    with fade
    n "And then, the two of you step out into the world. I... think this is the end of me. Even if it's not the end of you. I hope this was worth it. Genuinely, I do.\n"
    voice "audio/_pristine/voice/happy/hero/66.flac"
    hero "He's really gone, isn't he?\n"
    if trait_paranoid:
        voice "audio/_pristine/voice/happy/paranoid/47.flac"
        paranoid "Yeah. There's an itching in the back of my head that feels like it's finally been scratched. No more shadowy figures yanking at our strings. No more strings. I guess we're free.\n"
    elif trait_opportunist:
        voice "audio/_pristine/voice/happy/opportunist/44.flac"
        opportunist "No boss anymore. No one left to tell us what to do. I guess we'll have to be our own boss, then. About time!\n"
    voice "audio/_pristine/voice/happy/princess/100.flac"
    stop music fadeout 2.5
    if happy_leaving_hand_hold:
        show cg happy outside talk onlayer inyourface at Position(ypos=1125)
    else:
        show cg happy outside nohand talk onlayer inyourface at Position(ypos=1125)
    with dissolve
    p "The stars are so beautiful.\n"
    if happy_leaving_hand_hold:
        show cg happy dance suggest onlayer inyourface at Position(ypos=1125)
    else:
        show cg happy outside nohand onlayer inyourface at Position(ypos=1125)
    with dissolve
    truth "A quiet moment passes over you. A comfortable quiet.\n"
    if happy_leaving_hand_hold or happy_dance_mentioned:
        default happy_danced = False
        $ happy_danced = True
        if happy_dance_mentioned:
            voice "audio/_pristine/voice/happy/princess/101.flac"
            if happy_leaving_hand_hold:
                show cg happy dance suggest talk onlayer inyourface
            else:
                show cg happy outside nohand talk onlayer inyourface
            with dissolve
            p "I meant it, when I said I wanted to dance.\n"
        else:
            voice "audio/_pristine/voice/happy/princess/102.flac"
            show cg happy dance suggest talk onlayer inyourface
            with dissolve
            p "We should dance.\n"
        play music "audio/_pristine/music/happy/I Meant It Intro.flac"
        queue music "audio/_pristine/music/happy/I Meant It Loop.flac" loop
        if happy_leaving_hand_hold == False:
            play secondary "audio/one_shot/knife_tighten.flac"
        play audio "audio/_pristine/sfx/dance_start.flac"
        hide farback onlayer farback
        hide bg onlayer back
        hide fore onlayer front
        hide mid onlayer front
        hide cg onlayer inyourface
        hide farback
        show bg happy dance 1 onlayer farback at Position(ypos=1125)
        show cg happy dance 1 onlayer front at Position(ypos=1125)
        with Dissolve(1.0)
        truth "She gently pulls you forward, and the two of you fall into graceful step. The only rhythm that guides you is the shared thumping of your hearts, beating in perfect unison.\n"
        play audio "audio/_pristine/sfx/dance_start.flac"
        show bg happy dance 2 onlayer farback
        show cg happy dance 2 onlayer front
        with Dissolve(1.0)
        truth "Her face, worn and tired, brightens the faster you move, a soft, sad smile widening and widening until it reflects only genuine affection.\n"
        play audio "audio/_pristine/sfx/breeze.flac"
        show bg happy dance 3 onlayer farback
        show cg happy dance 3 onlayer front
        with Dissolve(1.5)
        truth "You send her out in a wide spin, and your arms stretch to their limits, only the tenuous grasp of your hand in hers holding you together. You share a gaze that feels like it lasts forever.\n"
        $ gallery_happy.unlock_item(12)
        $ gallery_happy.unlock_item(13)
        $ gallery_happy.unlock_item(14)
        $ gallery_happy.unlock_item(15)
        $ gallery_happy.unlock_item(16)
        $ renpy.save_persistent()
    stop music fadeout 20.0
    stop sound fadeout 20.0
    stop tertiary fadeout 20.0
    play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 20.0
    voice "audio/_pristine/voice/happy/princess/103.flac"

    if happy_danced:
        show quiet creep3 onlayer back at Position(ypos=1125)
        show cg happy dance 3 talk onlayer front
    else:
        show quiet creep3 onlayer front at Position(ypos=1125)
        show cg happy outside nohand talk onlayer inyourface
    with Dissolve(3.0)
    p "Thank you for taking me here. This is nice, even if it's a little cold outside.\n"
    if happy_danced:
        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
        hide cg onlayer front
        show hands happy dance 1 onlayer front at Position(ypos=1125)
        with Dissolve(1.0)
        $ renpy.pause(0.5)
        show hands happy dance 2 onlayer front
        with Dissolve(1.0)
        $ renpy.pause(0.5)
        show hands happy dance 3 onlayer front
        with Dissolve(0.5)
        $ renpy.pause(0.125)
        show hands happy dance 4 onlayer front
        with Dissolve(0.5)
        $ renpy.pause(0.125)
        show hands happy dance 5 onlayer front
        with Dissolve(0.5)
        $ renpy.pause(0.125)
        $ achievement.grant("ACH_HAPPY_DANCE")
    else:
        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
        hide cg onlayer inyourface
        show hands happy free final 1 onlayer front at Position(ypos=1125)
        with Dissolve(1.0)
        $ renpy.pause(0.5)
        show hands happy free final 2 onlayer front
        with Dissolve(0.5)
        $ renpy.pause(0.5)
        show hands happy free final 3 onlayer front
        with Dissolve(0.5)
        $ renpy.pause(0.125)
        show hands happy free final 4 onlayer front
        with Dissolve(0.5)
        $ renpy.pause(0.125)
        show hands happy free final 5 onlayer front
        with Dissolve(0.5)
        $ renpy.pause(0.125)
    hide hands onlayer front
    with Dissolve(0.25)
    $ renpy.pause(0.125)
    $ blade_held = False
    $ default_mouse = "default"
    hide bg onlayer back
    hide bg onlayer front
    hide player onlayer front
    hide player onlayer back
    hide fore onlayer front
    hide mid onlayer front
    hide fore onlayer inyourface
    hide farback onlayer farback
    hide bg onlayer back
    hide bg onlayer farback
    hide mid onlayer back
    hide stars onlayer farback
    hide bg onlayer back
    hide quiet onlayer back
    hide quiet onlayer front
    show farback quiet onlayer farback at Position(ypos=1125)
    with Dissolve(4.0)
    show mirror quiet distant onlayer back at Position(ypos=1125)
    if loops_finished != 0:
        truth "But you do not get the chance to respond, nor will you ever. It's time to leave. Memory returns.\n"
    else:
        truth "But you do not get the chance to respond. Something has taken her away, and it's left something else in her place.\n"

    if happy_danced:
        $ happy_end = "dance"
        $ princess_free += 1
        $ princess_satisfy += 2
    else:
        $ happy_end = "free"
        $ princess_free += 1
        $ princess_satisfy += 1
    jump mirror_start

    # END


return
