label fury_mirror_special:
    if trait_cold:
        voice "audio/_pristine/voice/extras/cold/3.flac"
        cold "So that's a wrap. I didn't think we'd ever get here. There's only one thing left to do.\n"
    else:
        voice "audio/_pristine/voice/extras/broken/23.flac"
        broken "So the world's gone, and she's gone with it. There's only one thing left for you to do here. You need to look at yourself. Whatever you see, it's going to be okay.\n"

    menu:
        extend ""

        "{i}• [[Approach the mirror.]{/i}":
            hide mirror onlayer back
            show content m empty onlayer front at Position(ypos=1125)
            show mirror frame onlayer front at Position(ypos=1125)
            with Dissolve(2.0)
            truth "The voice falls silent as you approach.\n"
            menu:

                extend ""

                "{i}• [[Gaze into your reflection.]{/i}":
                    jump mirror_n_gaze_join


label fury_pristine:

    # this is RIGHT after you're unwound

    default fury_beak_broken = True
    voice "audio/_pristine/voice/fury/hero/12.flac"
    hide fury onlayer front
    hide farback onlayer farback
    show bg fury charge onlayer back at Position(ypos=1125)
    show ribbons fury start 1 onlayer inyourface at Position(ypos=1125)
    show cg fury unarmed 1 clench onlayer front at Position(ypos=1125)
    with dissolve
    hero "No, no, no, that's our stuff! She can't just do that.\n"
    voice "audio/_pristine/voice/fury/narrator/15.flac"
    show cg fury unarmed 1 onlayer front
    with dissolve
    n "She just did. Unfortunate, I know, but reality is reality.\n"
    if fury_source == "pacifism":
        jump fury_pristine_pacifism_start
    elif fury_source == "tower":
        jump fury_pristine_tower
    elif fury_source == "unarmed":
        jump fury_pristine_unarmed
    else:
        jump fury_pristine_other_start

##############################

label fury_pristine_pacifism_start:

    # this is right after the two line seuqnece under label fury_pristine

    voice "audio/_pristine/voice/fury/cold/15.flac"
    play audio "audio/one_shot/collapse.flac"
    play secondary "audio/_pristine/sfx/guts_splash.flac"
    hide ribbons onlayer inyourface
    hide cg onlayer front
    hide bg onlayer back
    show bg fury unwind onlayer back at Position(ypos=1125)
    show fury unwind flat onlayer front at Position(ypos=1125)
    show ribbons fury start 1 onlayer inyourface at Position(ypos=1350)
    with Dissolve(1.0)
    cold "Huh. It's like I said. Our insides do look like the cabin. In the end, we're all just meat.\n"
    voice "audio/_pristine/voice/fury/stubborn/14.flac"
    stubborn "'In the end?' Just because she's ripped us open doesn't mean this is over.\n"
    voice "audio/_pristine/voice/fury/hero/13.flac"
    hero "How is it {i}not{/i} over?\n"
    voice "audio/_pristine/voice/fury/princess/6a.flac"
    show fury unwind surprise talk onlayer front
    with dissolve
    sp "Don't think that I'll allow you death here. I've made that mistake before. No. You will suffer until you see in me what I have seen in you.\n"
    voice "audio/_pristine/voice/fury/narrator/16.flac"
    show fury unwind surprise onlayer front
    with dissolve
    n "That's how. It would seem, somehow, that she is keeping you alive.\n"
    voice "audio/_pristine/voice/fury/cold/16.flac"
    cold "A challenge, then. Sure. Let's see how far we can take this.\n"
    jump fury_pristine_unwind_pre_menu


##############################

label fury_pristine_other_start:

    voice "audio/_pristine/voice/fury/broken/1.flac"
    play audio "audio/one_shot/collapse.flac"
    play secondary "audio/_pristine/sfx/guts_splash.flac"
    hide ribbons onlayer inyourface
    hide cg onlayer front
    hide bg onlayer back
    show bg fury unwind onlayer back at Position(ypos=1125)
    show fury unwind flat onlayer front at Position(ypos=1125)
    show ribbons fury start 1 onlayer inyourface at Position(ypos=1350)
    with Dissolve(1.0)
    broken "This is the only way it could have gone, really.\n"
    voice "audio/_pristine/voice/fury/stubborn/15.flac"
    stubborn "Oh you are just insufferable, aren't you? Come on! We're better than this.\n"
    voice "audio/_pristine/voice/fury/hero/14.flac"
    hero "So... are we dead?\n"
    voice "audio/_pristine/voice/fury/narrator/17.flac"
    n "No.\n"
    voice "audio/_pristine/voice/fury/princess/7.flac"
    show fury unwind surprise talk onlayer front
    with dissolve
    sp "Don't think that I'll allow you death here. I've made that mistake before. No. You will suffer until you see in me what I have seen in you.\n"
    show fury unwind surprise onlayer front
    jump fury_pristine_unwind_pre_menu

##############################

label fury_pristine_unwind_pre_menu:
    menu:
        extend ""

        "{i}• ''And what am I supposed to see?''{/i}":
            label fury_pristine_other_talk_join:
                default pristine_fury_talk_attempt = False
                $ pristine_fury_talk_attempt = True
                voice "audio/_pristine/voice/fury/narrator/18.flac"
                play audio "audio/_pristine/sfx/Fury gurgle speaking blood_6.flac"
                show fury unwind flat onlayer front
                with dissolve
                n "But the words don't leave your metaphorical mouth. Instead, all that leaves you is a wet and horrible gurgling as tissue vibrates out of place.\n"
                voice "audio/_pristine/voice/fury/hero/15.flac"
                hero "Our... 'metaphorical' mouth?\n"
                voice "audio/_pristine/voice/fury/princess/8.flac"
                show fury unwind flat talk onlayer front
                with dissolve
                sp "Oh, I didn't leave you a mouth, did I?\n"
                voice "audio/_pristine/voice/fury/princess/9.flac"
                show fury unwind wry talk onlayer front
                with dissolve
                sp "It's better that way. Words get us nowhere.\n"
                if fury_source == "unarmed":
                    voice "audio/_pristine/voice/fury/stubborn/16.flac"
                    show fury unwind flat onlayer front
                    with dissolve
                    stubborn "She's right. We don't need words. We just have to push forward.\n"
                    voice "audio/_pristine/voice/fury/contrarian/10.flac"
                    contrarian "Hey! I like words. They're easy, and we can have all sorts of fun with them. I {i}prefer{/i} having a mouth.\n"
                    voice "audio/_pristine/voice/fury/narrator/19a.flac"
                    n "Well, unfortunately for you, you don't have one. Not anymore.\n"
                    #voice "audio/_pristine/voice/fury/narrator/19.flac"
                    #n "Well, too bad, because unfortunately for you, you don't.\n"
                    jump fury_pristine_unarmed_menu

        "{i}• ''You're a monster.''{/i}":
            jump fury_pristine_other_talk_join

        "{i}• ''Please, just talk to me! Can we not use words to settle our differences? We're both here for a reason. It's more important for us to figure that out than to fight.''{/i}":
            jump fury_pristine_other_talk_join

        "{i}• ''You won't win.''{/i}":
            jump fury_pristine_other_talk_join

        "{i}• [[Attempt to die.]{/i}":
            if trait_broken:
                voice "audio/_pristine/voice/extras/broken/2.flac"
                broken "Yes, I think that would be for the best.\n"
            voice "audio/_pristine/voice/fury/hero/16.flac"
            hero "Can we even do that? Is death the sort of thing we can just decide to do?\n"
            voice "audio/_pristine/voice/fury/narrator/20a.flac"
            n "{i}Sigh{/i}. You do your best to die, but try though you might, you find yourself... unable to perish.\n"
            voice "audio/_pristine/voice/fury/stubborn/17.flac"
            stubborn "Good. Because we're not a quitter.\n"
            #voice "audio/_pristine/voice/fury/narrator/21a.flac"
            #n "Yes, hopefully this means there's still a chance for the world.\n"
            voice "audio/_pristine/voice/fury/narrator/21.flac"
            n "Yes, hopefully this means there's still a chance for the world here.\n"
            if trait_broken:
                voice "audio/_pristine/voice/extras/broken/3.flac"
                broken "Don't you get it? It's too late. We've both changed too much. We're not the challenge she wants anymore. The spark is gone.\n"
            voice "audio/_pristine/voice/fury/princess/10.flac"
            show fury unwind flat talk onlayer front
            with dissolve
            sp "I can feel you attempting to slip away. Is that what you want, then? Are you so terrified of my desires that you'd prefer any escape at all? Are you so terrified of me that you prefer death to my company?\n"
            voice "audio/_pristine/voice/fury/princess/11.flac"
            show fury unwind surprise talk onlayer front
            with dissolve
            sp "At least you're quiet now. At least you haven't fallen back on words.\n"

        "{i}• [[Say nothing.]{/i}":
            voice "audio/_pristine/voice/fury/princess/11.flac"
            show fury unwind surprise talk onlayer front
            with dissolve
            sp "At least you're quiet now. At least you haven't fallen back on words.\n"


    voice "audio/_pristine/voice/fury/princess/12.flac"
    show fury unwind annoyed talk onlayer front at Position(ypos=1125)
    show ribbons fury start 1 onlayer inyourface at Position(ypos=1350)
    with Dissolve(1.0)
    sp "They aren't music. They aren't dance. They aren't feeling.\n"
    voice "audio/_pristine/voice/fury/narrator/22a.flac"
    #show bg fury unwind onlayer back at Position(ypos=1125)
    #show fury unwind flat onlayer front at Position(ypos=1125)
    #show ribbons fury start 1 onlayer inyourface at Position(ypos=1350)
    #with fade
    n "Your eye, held far outside your skull by a thin stalk of nerves and viscera, stares back at her in unblinking silence.\n"
    #n "Your eye, held far outside your skull by a thin stalk of nerves and viscera, blinks.\n"
    stop sound fadeout 5.0
    stop tertiary fadeout 5.0
    voice "audio/_pristine/voice/fury/princess/13.flac"
    play audio "audio/final/fury_walk_single.flac"
    play tertiary "audio/final/Fury_WetPunch_2.flac"
    hide fury onlayer front
    show bg fury unwind onlayer back at shakeshort
    show starving den buried 1 onlayer back at Position(ypos=1125)
    show unwound 1 talk onlayer front at shakeshort
    hide ribbons fury start 1 onlayer inyourface
    with dissolve
    sp "Let's see what meaning we can find together. Let's see what we're made of.\n"
    jump fury_unwind_sequence

##############################

label fury_unwind_sequence:
    $ gallery_fury.unlock_item(15)
    $ renpy.save_persistent()
    play sound "audio/_pristine/sfx/Apotheosis Oppresive AMB_2loop.flac" loop
    play music "audio/_pristine/music/fury/The Fury Meta Intro.flac"
    queue music "audio/_pristine/music/fury/The Fury Meta Loop.flac" loop
    # sequence
    voice "audio/_pristine/voice/fury/narrator/23.flac"
    show starving den buried 2 onlayer back at Position(ypos=1125)
    show unwound 1 onlayer front
    with dissolve
    n "Something infiltrates you. Though you do not see it, you feel it, slithering into your disaster of a body, seeping into the gaps between your molecules.\n"
    voice "audio/_pristine/voice/fury/narrator/24a.flac"
    n "The body of a sapient creature has, on-average, thirty trillion cells. And each one of those cells is composed of one-hundred-trillion-some-odd atoms.\n"
    voice "audio/_pristine/voice/fury/narrator/25.flac"
    play audio "audio/_pristine/sfx/Fury surgical incision_1.flac"
    n "One of those cells is peeled from the others. One-hundred-trillion atoms are gone.\n" id fury_unwind_sequence_7b44741a
    voice "audio/_pristine/voice/fury/princess/14.flac"
    show unwound 1 talk onlayer front
    with dissolve
    sp "Are you still there? Are you still you?\n"
    if trait_cold:
        voice "audio/_pristine/voice/fury/cold/18.flac"
        show unwound 1 onlayer front
        with dissolve
        cold "Of course we are.\n"
    else:
        voice "audio/_pristine/voice/fury/hero/17.flac"
        show unwound 1 onlayer front
        with dissolve
        hero "... Yes? I think?\n"
    voice "audio/_pristine/voice/fury/narrator/26.flac"
    play audio "audio/_pristine/sfx/Fury surgical incision_2.flac"
    n "Then two are peeled away. Then four.\n"
    voice "audio/_pristine/voice/fury/stubborn/18.flac"
    stubborn "This is nothing. Nothing!\n"
    voice "audio/_pristine/voice/fury/narrator/27.flac"
    play audio "audio/_pristine/sfx/Fury surgical incision_3.flac"
    n "Eight. Sixteen. Thirty-two. Sixty-four.\n"
    if trait_cold:
        voice "audio/_pristine/voice/fury/cold/19.flac"
        cold "Ah, so the waiting is the torture. I do hate dull things.\n"
    elif trait_contrarian:
        voice "audio/_pristine/voice/fury/contrarian/11.flac"
        contrarian "Oh, is this a waiting game now? I hate waiting games.\n"
    elif trait_broken and fury_source == "tower":
        voice "audio/_pristine/voice/fury/broken/3.flac"
        broken "Whatever is happening to us, it's happening faster.\n"
    elif trait_broken:
        voice "audio/_pristine/voice/extras/broken/7.flac"
        broken "Whatever she does to us, we shouldn't hate her. She's been hurt so badly.\n"
    voice "audio/_pristine/voice/fury/narrator/28.flac"
    play audio "audio/_pristine/sfx/Fury surgical incision_4.flac"
    n "One-hundred-and-twenty-eight. Two-hundred-and-fifty-six. Five-hundred-and-twelve.\n"
    voice "audio/_pristine/voice/fury/princess/15.flac"
    show unwound 1 talk onlayer front
    with dissolve
    sp "Are you still there? Are you still you?\n"
    voice "audio/_pristine/voice/fury/narrator/29.flac"
    play audio "audio/_pristine/sfx/Fury surgical incision_5.flac"
    show unwound 1 onlayer front
    with dissolve
    n "One-thousand-twenty-four. Two-thousand-forty-eight. Four-thousand-ninety-six. Eight-thousand-one-hundred-ninety-two.\n"
    if trait_cold:
        voice "audio/_pristine/voice/fury/hero/18.flac"
        hero "Do you all feel that? I could have sworn I felt something.\n"
    elif trait_broken:
        voice "audio/_pristine/voice/fury/broken/4.flac"
        broken "I feel... small. Smaller than before.\n"
    elif trait_contrarian:
        voice "audio/_pristine/voice/fury/contrarian/12a.flac"
        contrarian "Yeah, we get it! There's a lot of numbers in us for you to count!\n"
    play audio "audio/_pristine/sfx/Fury surgical incision_6.flac"
    voice "audio/_pristine/voice/fury/narrator/30.flac"
    n "Sixteen-thousand-three-hundred-eighty-four. Thirty-two-thousand-seven-hundred-sixty-eight. Sixty-five-thousand-five-hundred-thirty-six.\n"
    voice "audio/_pristine/voice/fury/stubborn/19.flac"
    stubborn "You can't just count us into oblivion.\n"
    play audio "audio/_pristine/sfx/Fury surgical incision_7.flac"
    voice "audio/_pristine/voice/fury/narrator/31.flac"
    n "One-hundred-thirty-one-thousand-seventy-two. Two-hundred-sixty-two-thousand-one-hundred-forty-four. Five-hundred-twenty-four-thousand-two-hundred-eighty-eight.\n"
    voice "audio/_pristine/voice/fury/hero/19a.flac"
    show starving den buried 3 onlayer back
    with dissolve
    hero "What happens when it gets higher? Like... really higher?\n"
    if trait_cold:
        voice "audio/_pristine/voice/fury/cold/20.flac"
        cold "We die, probably.\n"
        voice "audio/_pristine/voice/fury/stubborn/20.flac"
        stubborn "Or nothing happens. Just like nothing is happening now.\n"
    elif trait_contrarian:
        voice "audio/_pristine/voice/fury/contrarian/13.flac"
        contrarian "I dunno. They'll probably get even higher! There's a lot of numbers out there.\n"
    elif trait_broken:
        voice "audio/_pristine/voice/fury/stubborn/21.flac"
        stubborn "Nothing. Just like nothing's happening now.\n"
        voice "audio/_pristine/voice/fury/broken/5.flac"
        broken "But something is happening now. Something in us is liquifying. Something that started small, but that keeps getting bigger.\n"
    play audio "audio/_pristine/sfx/Fury surgical incision_8.flac"
    voice "audio/_pristine/voice/fury/narrator/32.flac"
    n "One-million-forty-eight-thousand. The hundreds don't matter anymore.\n"
    voice "audio/_pristine/voice/fury/princess/16.flac"
    show starving den buried 4 onlayer back
    show unwound 1 talk onlayer front
    with dissolve
    sp "Are you still there? Are you still you?\n"
    play audio "audio/_pristine/sfx/Fury surgical incision_9.flac"
    voice "audio/_pristine/voice/fury/narrator/33.flac"
    show unwound 1 onlayer front
    with dissolve
    n "Two-million-ninety-six-thousand. Four-million-one-hundred-ninety-two-thousand. Eight-million-three-hundred-eighty-four-thousand.\n"
    voice "audio/_pristine/voice/fury/hero/20.flac"
    hero "I don't like this... waiting.\n"
    if trait_cold:
        voice "audio/_pristine/voice/fury/cold/21.flac"
        cold "You're going to give up before you even start hurting, aren't you?\n"
    elif trait_contrarian:
        $ trait_contrarian = False
        voice "audio/_pristine/voice/fury/contrarian/14.flac"
        contrarian "Yeah, I'm out.\n"
    elif trait_broken:
        voice "audio/_pristine/voice/fury/broken/6.flac"
        broken "Waiting for something to happen. But it's taking so long.\n"
    play audio "audio/_pristine/sfx/Fury surgical incision_10.flac"
    play audio "audio/_pristine/sfx/Fury Body Horror_16.flac"
    voice "audio/_pristine/voice/fury/narrator/34.flac"
    show bg unwound 2 onlayer back
    show unwound 2 onlayer front
    with Dissolve(1.5)
    n "Sixteen-million-seven-hundred-sixty-eight-thousand. Thirty-three-million-five-hundred-thirty-six-thousand. Sixty-seven-million-seventy-two-thousand. Your eyes are useless. One-hundred-thirty-four-million. The thousands don't matter anymore. Your blood begins to go places it shouldn't.\n"
    voice "audio/_pristine/voice/fury/princess/17.flac"
    show unwound 2 talk onlayer front
    with dissolve
    sp "Are you still there? Are you still you?\n"
    voice "audio/_pristine/voice/fury/stubborn/23.flac"
    show unwound 2 onlayer front
    with dissolve
    stubborn "There's the pain, I can feel it now. But we can handle this. We can't let her win.\n"
    if trait_cold:
        voice "audio/_pristine/voice/fury/cold/22.flac"
        cold "If you make this about winning and losing, you're going to lose. You're too connected to your body.\n"
    elif trait_broken and fury_source == "tower":
        voice "audio/_pristine/voice/fury/broken/7.flac"
        broken "We can't handle anything. We're at her mercy.\n"
    elif trait_broken:
        voice "audio/_pristine/voice/extras/broken/8.flac"
        broken "Fighting the pain is just the same as wallowing in it. This doesn't have to be something where you win or lose. We just have to accept it. Listen to it.\n"
    $ gallery_fury.unlock_item(16)
    $ renpy.save_persistent()
    play audio "audio/_pristine/sfx/Dragon Bubbling Flesh_1.flac"
    voice "audio/_pristine/voice/fury/narrator/35.flac"
    show bg unwound 3 onlayer back
    show unwound 3 onlayer front
    with Dissolve(1.5)
    n "Two-hundred-sixty-eight-million. We don't need to count anymore. Your lungs fill with liquid. You smell things you shouldn't. You choke on pieces of what used to be you.\n"
    voice "audio/_pristine/voice/fury/stubborn/24.flac"
    stubborn "It doesn't matter, because we're still alive!\n"
    $ gallery_fury.unlock_item(3)
    $ renpy.save_persistent()
    play audio "audio/_pristine/sfx/different_you.flac"
    voice "audio/_pristine/voice/fury/narrator/36.flac"
    hide bg onlayer back
    hide unwound onlayer front
    hide starving onlayer back
    show bg unwound 4 onlayer farback at Position(ypos=1125)
    show starving den buried 4 onlayer farback at Position(ypos=1125)
    show ribbons fury unwound 4 onlayer inyourface at Position(ypos=1125)
    show panel1 unwound 4 delayed onlayer farback at Position(ypos=1125)
    show panel2 unwound 4 delayed onlayer back at Position(ypos=1125)
    show panel3 unwound 4 delayed onlayer farback at Position(ypos=1125)
    show panel4 unwound 4 delayed onlayer back at Position(ypos=1125)
    show panel5 unwound 4 delayed onlayer front at Position(ypos=1125)
    show panel6 unwound 4 delayed onlayer inyourface at Position(ypos=1125)
    n "You are deconstructed. You are reconstructed. A square you. A round you. A you with too many legs. A you with many mouths which won't stop screaming. Then all of it pressed into a ball, tightly packed into the size of a fist.\n"
    if trait_cold:
        voice "audio/_pristine/voice/fury/hero/21.flac"
        hide ribbons onlayer inyourface
        hide panel1 onlayer farback
        hide panel2 onlayer back
        hide panel3 onlayer farback
        hide panel4 onlayer back
        hide panel5 onlayer front
        hide panel6 onlayer inyourface
        show panel6 unwound 4 onlayer front at Position(ypos=1125)
        with Dissolve(1.5)
        hero "What does 'you' even mean anymore? We just keep changing into horrible things we can't control. Make it stop. Please make it stop. Please make it stop.\n"
        voice "audio/_pristine/voice/fury/stubborn/25.flac"
        stubborn "'You' means we exist! And if we exist, then there has to be a way for us to win. Otherwise this would just be pointless! It would all just be pointless torture.\n"
        voice "audio/_pristine/voice/fury/cold/23.flac"
        cold "Yes. She's torturing us. That's the whole point of this exchange. Haven't you been paying attention?\n"
    elif trait_broken:
        voice "audio/_pristine/voice/fury/hero/21.flac"
        hide ribbons onlayer inyourface
        hide panel1 onlayer farback
        hide panel2 onlayer back
        hide panel3 onlayer farback
        hide panel4 onlayer back
        hide panel5 onlayer front
        hide panel6 onlayer inyourface
        show panel6 unwound 4 onlayer front at Position(ypos=1125)
        with Dissolve(1.5)
        hero "What does 'you' even mean anymore? We just keep changing into horrible things we can't control. Make it stop. Please make it stop. Please make it stop.\n"
        #voice "audio/_pristine/voice/fury/broken/8.flac"
        #broken "But we're 'still alive,' just like he said, aren't we? Though what does alive even mean anymore?\n"
        voice "audio/_pristine/voice/fury/stubborn/26a.flac"
        stubborn "'You' means we exist! There has to still be a way for us to win. Otherwise this would be pointless and all this torture would be for nothing.\n"
        #stubborn "Alive means we're here. 'You' means we exist! And if all of that is true, then there has to still be a way for us to win. Otherwise this would be pointless and all this torture would be for nothing.\n"
        voice "audio/_pristine/voice/fury/broken/9.flac"
        broken "You're right about one thing. It is torture. But it isn't pointless. The whole point is that it's torture.\n"
    else:
        voice "audio/_pristine/voice/fury/hero/21.flac"
        hide ribbons onlayer inyourface
        hide panel1 onlayer farback
        hide panel2 onlayer back
        hide panel3 onlayer farback
        hide panel4 onlayer back
        hide panel5 onlayer front
        hide panel6 onlayer inyourface
        show panel6 unwound 4 onlayer front at Position(ypos=1125)
        with Dissolve(1.5)
        hero "What does 'you' even mean anymore? We just keep changing into horrible things we can't control. Make it stop. Please make it stop. Please make it stop.\n"
        voice "audio/_pristine/voice/fury/stubborn/25.flac"
        stubborn "'You' means we exist! And if we exist, then there has to be a way for us to win. Otherwise this would just be pointless! It would all just be pointless torture.\n"
    voice "audio/_pristine/voice/fury/princess/14.flac"
    sp "Are you still there? Are you still you?\n"
    if trait_broken and fury_source == "tower":
        $ trait_broken = False
        voice "audio/_pristine/voice/fury/broken/10.flac"
        broken "... no.\n"
    voice "audio/_pristine/voice/fury/stubborn/27.flac"
    stubborn "YES!\n"
    $ gallery_fury.unlock_item(4)
    $ renpy.save_persistent()
    play audio "audio/_pristine/sfx/Fury Body Horror_6.flac"
    voice "audio/_pristine/voice/fury/narrator/37.flac"
    hide panel6 onlayer front
    hide starving onlayer farback
    hide bg onlayer farback
    show bg unwound 5 onlayer back at Position(ypos=1125)
    show unwound 5 princess onlayer front at Position(ypos=1125)
    show player unwound 5 onlayer inyourface at Position(ypos=1125)
    with Dissolve(1.5)
    n "The ball is unraveled into the shape of a body. The skin peels off in a corkscrew. The eyes are plucked. The organs arranged in the air in a neat row.\n"
    voice "audio/_pristine/voice/fury/princess/18.flac"
    hide panel6 onlayer front
    hide panel6 onlayer inyourface
    show unwound 5 princess talk onlayer front
    with dissolve
    sp "Are you still there? Are you still you?\n"
    if trait_broken and fury_source != "tower":
        voice "audio/_pristine/voice/extras/broken/9.flac"
        show unwound 5 princess onlayer front
        with dissolve
        broken "It's okay to let go.\n"
        voice "audio/_pristine/voice/extras/hero/1.flac"
        hero "Then I'm letting go.\n"
    else:
        voice "audio/_pristine/voice/fury/hero/22.flac"
        show unwound 5 princess onlayer front
        with dissolve
        hero "No.\n"
    if trait_cold:
        voice "audio/_pristine/voice/fury/cold/24.flac"
        cold "{i}Sigh{/i}.\n"
    voice "audio/_pristine/voice/fury/stubborn/28.flac"
    stubborn "Yes.\n"
    play audio "audio/_pristine/sfx/Fury bone disintegrating_1.flac"
    voice "audio/_pristine/voice/fury/narrator/38.flac"
    hide player onlayer inyourface
    show bg unwound 6 onlayer back
    show unwound 6 onlayer front
    show starving den buried 4 onlayer inyourface at Position(ypos=1125)
    with Dissolve(1.0)
    n "You are stretched into a line, twelve feet long. Then twenty-four. Then forty-eight. The line gets thinner as you get longer. A mile. Two. Four. Eight.\n"
    voice "audio/_pristine/voice/fury/princess/19.flac"
    show unwound 6 talk onlayer front
    with dissolve
    sp "Are you still there? Are you still you?\n"
    voice "audio/_pristine/voice/fury/stubborn/29.flac"
    stubborn "... Yes.\n"
    voice "audio/_pristine/voice/fury/narrator/39.flac"
    play audio "audio/one_shot/hard tighten.flac"
    show bg unwound 6 stretch 1 onlayer back
    show unwound 6 stretch 1 onlayer front
    with Dissolve(1.0)
    n "Sixteen. Thirty-two.\n"
    stubborn "...\n"
    voice "audio/_pristine/voice/fury/narrator/40.flac"
    play audio "audio/final/Witch_TreeWrap_1.flac"
    show bg unwound 6 stretch 2 onlayer back
    show unwound 6 stretch 2 onlayer front
    with Dissolve(1.0)
    n "Sixty-four.\n"
    voice "audio/_pristine/voice/fury/stubborn/30.flac"
    $ trait_stubborn = False
    stubborn "No.\n"
    if trait_cold or (trait_broken and fury_source != "tower"):
        voice "audio/_pristine/voice/fury/narrator/41.flac"
        show bg unwound 6 stretch 2 onlayer back at swayblur
        show unwound 6 stretch 2 onlayer front at swayblur
        with Dissolve(1.0)
        n "One hundred-and-twenty-eight.\n"
        if trait_cold:
            voice "audio/_pristine/voice/fury/cold/25.flac"
            cold "I'm still here. I'm still 'me.'\n"
        else:
            voice "audio/_pristine/voice/extras/broken/10a.flac"
            broken "I'm still here.\n"
        voice "audio/_pristine/voice/fury/narrator/42.flac"
        play audio "audio/final/Assorted_TapestyUnraveledBreakingRip_1.flac"
        hide starving onlayer inyourface
        hide bg onlayer back
        hide unwound onlayer front
        show bg unwound 7 onlayer farback at Position(ypos=1125)
        show back unwound 7 onlayer back at cage_sway, Position(ypos=1125)
        show mid unwound 7 onlayer front at cage_sway, Position(ypos=1125)
        show fore unwound 7 onlayer front at cage_big_sway, Position(ypos=1125)
        with Dissolve(1.0)
        n "You are stretched and stretched and stretched, until you are longer than the world itself. You wrap around it again and again and again. A tense line of microcosmic tissue, held together by forces that are far too weak for the task they've been given.\n"
        voice "audio/_pristine/voice/fury/princess/20.flac"
        sp "Are you still there? Are you still you?\n"
        if trait_cold:
            voice "audio/_pristine/voice/fury/cold/26.flac"
            cold "Do I have to keep answering?\n"
        else:
            voice "audio/_pristine/voice/extras/broken/11.flac"
            broken "I'm going to stick around as long as you need me to.\n"
        $ gallery_fury.unlock_item(17)
        $ renpy.save_persistent()
        voice "audio/_pristine/voice/fury/narrator/43.flac"
        play audio "audio/_pristine/sfx/Fury body exploading_2.flac"
        play tertiary "audio/_pristine/sfx/Fury Body Horror_16.flac"
        hide bg onlayer farback
        hide back onlayer back
        hide mid onlayer front
        hide fore onlayer front
        show bg unwound 8 onlayer farback at Position(ypos=1125)
        show mid unwound 8 onlayer back at cage_sway, Position(ypos=1125)
        show unwound 8 onlayer front at sway, Position(ypos=1125)
        with Dissolve(1.0)
        n "And then the forces disappear. The bonds holding your cells together break. You are a thirty-trillion little pieces, all of them separate, and all of them falling.\n"
        voice "audio/_pristine/voice/fury/princess/21.flac"
        show unwound 8 talk onlayer front at sway, Position(ypos=1125)
        with dissolve
        sp "Are you still there? Are you still you?\n"
        #'places' too often, also the sentence was confusing. I feel it's more impactful if it's shorter
        voice "audio/_pristine/voice/fury/narrator/44.flac"
        show unwound 8 onlayer front at sway, Position(ypos=1125)
        with dissolve
        n "You sit in these thirty-trillion places, each second passing in each of them before you arrive at the next. Each second passing as one million years.\n"
        voice "audio/_pristine/voice/fury/narrator/45.flac"
        n "And so you wait.\n"
        voice "audio/_pristine/voice/fury/princess/22.flac"
        show unwound 8 talk onlayer front at sway, Position(ypos=1125)
        with dissolve
        sp "That's all I have.\n"
        voice "audio/_pristine/voice/fury/narrator/46.flac"
        play audio "audio/_pristine/sfx/Fury Skin peel_1.flac"
        stop music
        stop sound
        stop secondary
        stop tertiary
        hide farback onlayer farback
        hide bg onlayer farback
        hide mid onlayer back
        hide unwound onlayer front
        scene bg black
        n "And then, all at once, there is a great rewinding, and all of the disparate pieces that once were you fall dutifully back into place.\n"
        jump fury_cold_conclusion

    else:
        voice "audio/_pristine/voice/fury/narrator/47.flac"
        play audio "audio/final/Assorted_TapestyUnraveledBreakingRip_1.flac"
        stop music
        stop sound
        stop secondary
        stop tertiary
        hide farback onlayer farback
        hide starving onlayer inyourface
        hide bg onlayer back
        hide unwound onlayer front
        scene bg black
        n "And then, all at once, there is a great rewinding, and all of the disparate threads that once were you fall dutifully back into place.\n"
        jump fury_other_conclusion


label fury_cold_conclusion:

    # commenting out lines written for non-cold voices below. TONY when you get to the code part, set those voices to false
    #play sound "audio/final/fury_ambient.ogg" loop fadein 1.0
    play sound "audio/_pristine/sfx/Apotheosis Oppresive AMB_2loop.flac" loop fadein 1.0
    voice "audio/_pristine/voice/fury/narrator/48.flac"
    scene farback basement fury onlayer farback at Position(ypos=1150)
    show bg fury sullen onlayer back at Position(ypos=1125)
    show fury s sullen onlayer back at Position(ypos=1125)
    with Dissolve(1.0)
    n "You are whole again, and in your body—the body you had before all of this happened—and the Princess sits against the wall, her dress of skin more tattered than before, her face sullen and disappointed.\n"
    voice "audio/_pristine/voice/fury/princess/23.flac"
    show fury s sullen talk onlayer back
    with dissolve
    sp "You left me. And there's nothing I can do to bring you back.\n"
    if trait_cold:
        voice "audio/_pristine/voice/fury/cold/27a.flac"
        show fury s sullen onlayer back
        with dissolve
        cold "Oh... she's been like me this whole time. She's just been hiding it.\n"
    else:
        voice "audio/_pristine/voice/extras/broken/14a.flac"
        show fury s sullen onlayer back
        with dissolve
        broken "She's just like us. A piece of her is missing.\n"
    play music "audio/_pristine/music/fury/The Fury Sad Intro.flac"
    queue music "audio/_pristine/music/fury/The Fury Sad Loop.flac" loop
    label fury_cold_conclusion_menu:
        default fury_cold_conclusion_explore = False
        default fury_cold_conclusion_final_nice_seen = False
        default fury_cold_conclusion_goal_explore = False
        default fury_cold_conclusion_different_explore = False
        menu:
            extend ""

            "{i}• (Explore) ''I'm not gone. I'm right here.''{/i}" if fury_cold_conclusion_explore == False:
                $ fury_cold_conclusion_explore = True
                voice "audio/_pristine/voice/fury/princess/24.flac"
                show fury s glance talk onlayer back
                with dissolve
                sp "So you are. And yet I still feel so alone.\n"
                show fury s glance onlayer back
                menu:
                    extend ""

                    "{i}• ''All I did was stop the violence. You can stop it, too. Just leave with me.''{/i}":
                        voice "audio/_pristine/voice/fury/princess/25.flac"
                        show fury s timid talk onlayer back
                        with dissolve
                        sp "After everything I've done to you, you'd really take me with you?\n"
                        jump fury_cold_leave_final_option

                    "{i}• ''At some point you have to open your eyes and see the rest of the world. You have to see the world outside of us.''{/i}":
                        voice "audio/_pristine/voice/fury/princess/26a.flac"
                        show fury s timid talk onlayer back
                        with dissolve
                        sp "There is no world outside of us. And there is no us.\n"
                        jump fury_cold_conclusion_menu

                    "{i}• [[Say nothing.]{/i}":
                        jump fury_cold_conclusion_menu

            "{i}• (Explore) ''I never stopped caring about you. But you have to let go of all of that pain.''{/i}" if fury_cold_conclusion_explore == False and fury_cold_conclusion_final_nice_seen == False:
                $ fury_cold_conclusion_explore = True
                voice "audio/_pristine/voice/fury/princess/27.flac"
                show fury s timid talk onlayer back
                with dissolve
                sp "How? It's all I've known.\n"
                jump fury_cold_final_nice_menu

            "{i}• (Explore) ''There's more to life than violence and pain. We can be more than that, if you want.''{/i}" if fury_cold_conclusion_final_nice_seen == False:
                voice "audio/_pristine/voice/fury/princess/28.flac"
                show fury s glance talk onlayer back
                with dissolve
                sp "How? Violence and pain are all I've known.\n"
                show fury s glance onlayer back
                label fury_cold_final_nice_menu:
                    $ fury_cold_conclusion_final_nice_seen = True
                    menu:

                        extend ""

                        "{i}• ''You could always leave with me.''{/i}":
                            voice "audio/_pristine/voice/fury/princess/29.flac"
                            show fury s timid talk onlayer back
                            with dissolve
                            sp "After everything I've done to you, you'd really take me with you?\n"
                            jump fury_cold_leave_final_option

                        "{i}• ''That's up to you.''{/i}":
                            voice "audio/_pristine/voice/fury/princess/30.flac"
                            show fury s sullen talk onlayer back
                            with dissolve
                            sp "Then here I stay.\n"
                            jump fury_cold_conclusion_menu

                        "{i}• [[Say nothing.]{/i}":
                            jump fury_cold_conclusion_menu

            "{i}• (Explore) ''I didn't like fighting you when we first met. I still don't want to do that.''{/i}" if fury_cold_conclusion_final_nice_seen == False:
                $ fury_cold_conclusion_final_nice_seen = True
                voice "audio/_pristine/voice/fury/princess/31.flac"
                show fury s glance talk onlayer back
                with dissolve
                sp "Oh... all this time I thought I understood something about you. But I didn't. Now what?\n"
                show fury s glance onlayer back
                jump fury_cold_final_nice_menu

            "{i}• (Explore) ''What were you hoping to accomplish with all of that?''{/i}" if fury_cold_conclusion_goal_explore == False:
                $ fury_cold_conclusion_goal_explore = True
                voice "audio/_pristine/voice/fury/princess/32.flac"
                show fury s timid talk onlayer back
                with dissolve
                sp "I don't know. I just wanted something back. Something that was missing. I don't really know what it is. I just know that it's still gone.\n"
                show fury s timid onlayer back
                jump fury_cold_conclusion_menu

            "{i}• (Explore) ''You seem so... off. It's like you're a completely different person than you were when you started pulling me apart.''{/i}" if fury_cold_conclusion_different_explore == False:
                $ fury_cold_conclusion_different_explore = True
                voice "audio/_pristine/voice/fury/princess/33.flac"
                show fury s sullen talk onlayer back
                with dissolve
                sp "Different... I am, yes. We were doing all that for such a long time. I'm tired now.\n"
                jump fury_cold_conclusion_menu

            "{i}• (Explore) ''That was awful. I hated every second of it.''{/i}" if fury_cold_conclusion_explore == False:
                $ fury_cold_conclusion_explore = True
                voice "audio/_pristine/voice/fury/princess/34.flac"
                show fury s timid talk onlayer back
                with dissolve
                sp "So I did do something to you, after all.\n"
                show fury s timid onlayer back
                jump fury_cold_conclusion_menu

            "{i}• (Explore) ''So that's all you've got, huh?''{/i}" if fury_cold_conclusion_explore == False:
                $ fury_cold_conclusion_explore = True
                voice "audio/_pristine/voice/fury/princess/35.flac"
                show fury s timid talk onlayer back
                with dissolve
                sp "Yes. I think I'm finished now. There's nothing more for me to do to you.\n"
                show fury s timid onlayer back
                jump fury_cold_conclusion_menu

            "{i}• ''I think I'm going to go now.''{/i}":
                voice "audio/_pristine/voice/fury/princess/36.flac"
                show fury s timid talk onlayer back
                with dissolve
                sp "Alone?\n"
                show fury s timid onlayer back
                menu:
                    extend ""

                    "{i}• ''Yes.''{/i}":
                        voice "audio/_pristine/voice/fury/princess/37.flac"
                        show fury s wave off talk 1 onlayer back
                        with dissolve
                        sp "Go, then. I'm sorry.\n"
                        jump fury_cold_leave_join

                    "{i}• ''If you'll let me.''{/i}":
                        voice "audio/_pristine/voice/fury/princess/37.flac"
                        show fury s wave off talk 1 onlayer back
                        with dissolve
                        sp "Go, then. I'm sorry.\n"
                        jump fury_cold_leave_join

                    "{i}• ''I was hoping you'd come with me.''{/i}":
                        voice "audio/_pristine/voice/fury/princess/38.flac"
                        show fury s timid talk onlayer back
                        with dissolve
                        sp "After everything I've done to you, is that really an option?\n"
                        show fury s timid onlayer back
                        jump fury_cold_leave_final_option

                    "{i}• ''That's up to you.''{/i}":
                        voice "audio/_pristine/voice/fury/princess/39.flac"
                        show fury s timid talk onlayer back
                        with dissolve
                        sp "After everything I've done to you, you'd really give me that option?\n"
                        show fury s timid onlayer back
                        label fury_cold_leave_final_option:
                            menu:
                                extend ""

                                "{i}• [[Give her your hand.]{/i}":
                                    voice "audio/_pristine/voice/fury/narrator/49a.flac"
                                    n "Are you serious? You're just offering her your hand?\n"
                                    #hero "Have we ever not been?\n"
                                    voice "audio/_pristine/voice/fury/narrator/50.flac"
                                    play audio "audio/one_shot/footsteps_stone.flac"
                                    hide farback onlayer farback
                                    hide bg onlayer back
                                    hide fury onlayer back
                                    with fade
                                    scene farback fury hand onlayer farback at Position(ypos=1125)
                                    show bg fury hand onlayer back at Position(ypos=1125)
                                    show fury slay sad onlayer back at Position(ypos=1125)
                                    show player fury hand onlayer front at Position(ypos=1125)
                                    with Dissolve(1.0)
                                    n "{i}Sigh{/i}. You cross the room towards the Princess, extending your hand to her.\n"
                                    voice "audio/_pristine/voice/fury/narrator/51a.flac"
                                    show fury hand onlayer back
                                    with dissolve
                                    n "Her eyes, deep wells of buried sorrow, meet yours for a moment. You despicable fiend.\n"
                                    voice "audio/_pristine/voice/fury/narrator/52.flac"
                                    play audio "audio/one_shot/knife_tighten.flac"
                                    hide player onlayer front
                                    show fury hand grab onlayer back
                                    with Dissolve(0.7)
                                    n "And then she takes your hand in hers. You're going to end the world, don't you get it? I can't let that happen. I can't let you leave, I have to—\n{w=10.5}{nw}"
                                    show screen disableclick(0.5)
                                    if trait_cold:
                                        voice "audio/_pristine/voice/fury/cold/28.flac"
                                        cold "You have to what? Stop us?\n"
                                        voice "audio/_pristine/voice/fury/narrator/53.flac"
                                        n "You leave me no other choice.\n"
                                        voice "audio/_pristine/voice/fury/cold/29b.flac"
                                        cold "You are nothing but a witness.\n"
                                    else:
                                        voice "audio/_pristine/voice/extras/broken/15.flac"
                                        broken "You can't stop us. We've been through enough. You don't scare us.\n"
                                    $ gallery_fury.unlock_item(6)
                                    $ renpy.save_persistent()
                                    $ quick_menu = False
                                    voice "audio/_pristine/voice/fury/narrator/54.flac"
                                    play audio "audio/final/fury_walk_short.flac"
                                    hide farback onlayer farback
                                    hide bg onlayer back
                                    hide fury onlayer back
                                    scene bg black
                                    with fade
                                    scene farback fury leave stairs onlayer farback at Position(ypos=1125)
                                    show bg fury leave stairs onlayer back at Position(ypos=1125)
                                    show fury leave stairs onlayer front at Position(ypos=1125)
                                    with fade
                                    if persistent.quick_menu:
                                        $ quick_menu = True
                                    n "I... I... fine. You and the Princess climb the stairs out of the basement, together, in silence.\n"
                                    if trait_cold:
                                        voice "audio/_pristine/voice/fury/cold/30.flac"
                                        cold "No embellishments? No flowery text describing what kind of silence we share? You've really given up, haven't you?\n"
                                    else:
                                        voice "audio/_pristine/voice/extras/broken/16.flac"
                                        broken "It's okay. We're almost there.\n"
                                    $ quick_menu = False
                                    voice "audio/_pristine/voice/fury/narrator/55.flac"
                                    play audio "audio/final/fury_walk_short.flac"
                                    hide farback onlayer farback
                                    hide bg onlayer back
                                    hide fury onlayer front
                                    scene bg black
                                    with fade
                                    scene farback fury leave upstairs onlayer farback at Position(ypos=1125)
                                    show bg fury leave upstairs onlayer back at Position(ypos=1125)
                                    show fury leave upstairs onlayer front at Position(ypos=1125)
                                    with fade
                                    if persistent.quick_menu:
                                        $ quick_menu = True
                                    n "I'm tired.\n"
                                    if trait_cold:
                                        voice "audio/_pristine/voice/fury/cold/31.flac"
                                        cold "What a shame, but you should really keep going. You have a job to do, don't you?\n"
                                    else:
                                        voice "audio/_pristine/voice/extras/broken/17.flac"
                                        broken "I know.\n"
                                    play tertiary "audio/final/fury_walk_short.flac"
                                    queue tertiary "audio/one_shot/door_stone.flac"
                                    voice "audio/_pristine/voice/fury/narrator/56.flac"
                                    hide farback onlayer farback
                                    hide bg onlayer back
                                    hide fury onlayer front
                                    scene bg black
                                    with fade
                                    n "{i}Sigh{/i}. And then you cross the upstairs of the cabin, to the door, which you open.\n"
                                    play audio "audio/final/fury_ext_walk.flac"
                                    play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 15.0
                                    stop music fadeout 15.0
                                    stop sound fadeout 15.0
                                    stop tertiary fadeout 15.0
                                    voice "audio/_pristine/voice/fury/narrator/57.flac"
                                    show farback fury leave outside onlayer farback at Position(ypos=1125)
                                    show bg fury leave outside onlayer back at Position(ypos=1125)
                                    show quiet creep1 onlayer back at Position(ypos=1125)
                                    show fury leave outside onlayer front at Position(ypos=1125)
                                    with fade
                                    n "And then you step outside and into the ruins of the world you left—\n"
                                    if trait_cold:
                                        voice "audio/_pristine/voice/fury/cold/32.flac"
                                        show quiet creep2 onlayer back
                                        with Dissolve(1.0)
                                        cold "... Behind? So He's gone, too. It's just you and me now.\n"
                                    else:
                                        voice "audio/_pristine/voice/extras/broken/18.flac"
                                        show quiet creep2 onlayer back
                                        with Dissolve(1.0)
                                        broken "... Behind. He's gone, too. It's just the three of us now.\n"
                                    play audio "audio/final/fury_ext_walk.flac"
                                    voice "audio/_pristine/voice/fury/princess/40.flac"
                                    show fury leave outside talk onlayer front
                                    show quiet creep3 onlayer back
                                    with Dissolve(1.5)
                                    sp "Is this the world? It's so... cold.\n"
                                    play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                                    hide fury onlayer front
                                    show hands fury leave 1 onlayer front at Position(ypos=1125)
                                    with Dissolve(1.0)
                                    $ renpy.pause(1.0)
                                    show hands fury leave 2 onlayer front at Position(ypos=1125)
                                    with Dissolve(1.0)
                                    $ renpy.pause(0.5)
                                    show hands fury leave 3 onlayer front at Position(ypos=1125)
                                    with Dissolve(0.5)
                                    $ renpy.pause(0.25)
                                    show hands fury leave 4 onlayer front at Position(ypos=1125)
                                    with Dissolve(0.25)
                                    $ renpy.pause(0.125)
                                    show hands fury leave 5 onlayer front at Position(ypos=1125)
                                    with Dissolve(0.25)
                                    $ renpy.pause(0.125)
                                    hide hands onlayer front
                                    with Dissolve(0.25)
                                    $ renpy.pause(0.125)
                                    $ blade_held = False
                                    $ default_mouse = "default"
                                    stop music
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
                                    hide quiet onlayer farback
                                    hide quiet onlayer front
                                    show farback quiet onlayer farback at Position(ypos=1125)
                                    with Dissolve(4.0)
                                    show mirror quiet distant onlayer back at Position(ypos=1125)
                                    if loops_finished != 0:
                                        truth "You do not get the chance to respond, nor will you ever. It's time to leave. Memory returns.\n"
                                    else:
                                        truth "You do not get the chance to respond. Something has taken her away, and it's left something else in her place.\n"
                                    $ achievement.grant("ACH_FURY_FREE")
                                    $ fury_end = "free"
                                    $ princess_free += 1
                                    $ princess_satisfy += 1
                                    $ trait_stubborn = False
                                    jump fury_mirror_special
                                    # END


                                "{i}• ''No. I just wanted to hurt you back.''{/i}":
                                    voice "audio/_pristine/voice/fury/princess/41.flac"
                                    show fury s wave off talk 1 onlayer back
                                    with dissolve
                                    sp "And you did. Go, then.\n"
                                    jump fury_cold_leave_join

                                "{i}• ''No. And I don't know why I said that.''{/i}":
                                    voice "audio/_pristine/voice/fury/princess/42.flac"
                                    show fury s wave off talk 1 onlayer back
                                    with dissolve
                                    sp "I don't think either of us knows who we are.\n"
                                    jump fury_cold_leave_join

                    "{i}• ''I'm going to leave now. I was hoping you'd come with me.''{/i}":
                        voice "audio/_pristine/voice/fury/princess/38.flac"
                        show fury s timid talk onlayer back
                        with dissolve
                        sp "After everything I've done to you, is that really an option?\n"
                        show fury s timid onlayer back
                        jump fury_cold_leave_final_option


                    "{i}• [[Turn and leave.]{/i}":
                        label fury_cold_leave_join:
                            voice "audio/_pristine/voice/fury/narrator/58.flac"
                            play audio "audio/one_shot/footsteps_stone.flac"
                            $ quick_menu = False
                            hide farback onlayer farback
                            hide bg onlayer back
                            hide fury onlayer back
                            scene bg black
                            with fade
                            scene farback fury leave stairs onlayer farback at Position(ypos=1125)
                            show bg fury leave stairs onlayer back at Position(ypos=1125)
                            with fade
                            if persistent.quick_menu:
                                $ quick_menu = True
                            n "You turn back towards the stairs, putting the Princess forever out of your mind.\n"
                            voice "audio/_pristine/voice/fury/princess/43.flac"
                            sp "... Alone.\n"
                            #hero "Then it's finally over.\n"
                            if trait_cold:
                                voice "audio/_pristine/voice/fury/cold/33.flac"
                                cold "Then we're done here. It's over. On to the next thing.\n" id fury_cold_leave_join_dfc579df
                            else:
                                voice "audio/_pristine/voice/extras/broken/19.flac"
                                broken "Maybe going our separate ways is the only way things can ever get better. At least this can be over.\n"
                            voice "audio/_pristine/voice/fury/narrator/59.flac"
                            n "Over? You do know that this really doesn't solve anything, right?\n"
                            if trait_cold:
                                voice "audio/_pristine/voice/fury/cold/34.flac"
                                cold "We don't need a resolution. We've never needed one. Whatever we are, we're here forever.\n"
                            else:
                                voice "audio/_pristine/voice/extras/broken/20.flac"
                                broken "It doesn't have to solve anything.\n"
                            voice "audio/_pristine/voice/fury/narrator/60.flac"
                            play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 15.0
                            stop music fadeout 15.0
                            stop sound fadeout 15.0
                            stop tertiary fadeout 15.0
                            show quiet creep1 onlayer back at Position(ypos=1125)
                            with Dissolve(1.0)
                            n "But this isn't over! She'll find a way out! If you don't turn around and finish this right now, she'll bring about the end of the entire—\n"
                            if trait_cold:
                                voice "audio/_pristine/voice/fury/cold/35.flac"
                                show quiet creep2 onlayer back
                                with Dissolve(1.0)
                                cold "And He's gone, too. It's just you and me now.\n"
                            else:
                                voice "audio/_pristine/voice/extras/broken/21.flac"
                                show quiet creep2 onlayer back
                                with Dissolve(1.0)
                                broken "And He's gone, too. It's just you and me now.\n"
                            show quiet creep3 onlayer back
                            with Dissolve(1.0)
                            truth "As you climb to the top of the stairs, you realize that there is no top of the stairs to reach. At least not anymore.\n"
                            truth "Her voice quietly whispers from behind you.\n"
                            voice "audio/_pristine/voice/fury/princess/44.flac"
                            $ gallery_fury.unlock_item(7)
                            $ renpy.save_persistent()
                            sp "I feel so cold. Is it because you're gone?\n"
                            play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                            $ blade_held = False
                            $ default_mouse = "default"
                            stop music
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
                            hide quiet onlayer farback
                            hide quiet onlayer front
                            show farback quiet onlayer farback at Position(ypos=1125)
                            with Dissolve(4.0)
                            show mirror quiet distant onlayer back at Position(ypos=1125)
                            if loops_finished != 0:
                                truth "But as look over your shoulder, you do not find her, nor will you ever. It's time to leave. Memory returns.\n"
                            else:
                                truth "But as look over your shoulder, you do not find her. Something has taken her away, and it's left something else in her place.\n"
                            $ fury_end = "leave"
                            $ princess_kept += 1
                            $ princess_deny += 1
                            $ trait_stubborn = False
                            jump fury_mirror_special


                            # END

            "{i}• [[Turn and leave.]{/i}":
                jump fury_cold_leave_join

            "{i}• [[Slay the Princess.]{/i}" if fury_blade_taken:
                voice "audio/_pristine/voice/fury/narrator/61.flac"
                play audio "audio/one_shot/knife_pickup.flac"
                $ blade_held = True
                $ default_mouse = "blade"
                n "Right! The blade! After all of that, it's still here waiting for you. You pick it up off the floor.\n"
                voice "audio/_pristine/voice/fury/narrator/62a.flac"
                play audio "audio/one_shot/footsteps_stone.flac"
                hide farback onlayer farback
                hide bg onlayer back
                hide fury onlayer back
                scene farback fury hand onlayer farback at Position(ypos=1125)
                show bg fury hand onlayer back at Position(ypos=1125)
                show fury slay sad onlayer back at Position(ypos=1125)
                with Dissolve(1.0)
                n "The Princess doesn't look up as you cross the room.\n"
                $ gallery_fury.unlock_item(5)
                $ renpy.save_persistent()
                $ default_mouse = "blood"
                play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 15.0
                stop music fadeout 15.0
                stop sound fadeout 15.0
                stop tertiary fadeout 15.0
                voice "audio/_pristine/voice/fury/narrator/62b.flac"
                play audio "audio/final/Razor_ImpaleSwordBody_6.flac"
                show fury slay sad stab onlayer back
                n "Nor does she look up as you bury the weapon in her heart—\n"
                play audio "audio/_pristine/sfx/Fury surgical incision_1.flac"
                voice "audio/_pristine/voice/fury/princess/45.flac"
                hide fury onlayer back
                show quiet creep1 onlayer back at Position(ypos=1125)
                show fury slay sad post stab talk onlayer back at Position(ypos=1125)
                with Dissolve(0.75)
                sp "Huh. I felt that. It's cold.\n"
                if trait_cold:
                    voice "audio/_pristine/voice/fury/cold/36.flac"
                    show quiet creep2 onlayer back
                    show fury slay sad post stab onlayer back
                    with Dissolve(0.75)
                    cold "Hm. I felt that too, a little. Isn't that something.\n"
                else:
                    voice "audio/_pristine/voice/extras/broken/22.flac"
                    show quiet creep2 onlayer back
                    show fury slay sad post stab onlayer back
                    with Dissolve(0.75)
                    broken "So did we.\n"
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                show quiet creep3 onlayer back
                hide fury onlayer back
                show hands fury sad slay 1 onlayer back at Position(ypos=1125)
                with Dissolve(1.0)
                $ renpy.pause(1.0)
                show hands fury sad slay 2 onlayer back at Position(ypos=1125)
                with Dissolve(1.0)
                $ renpy.pause(0.5)
                show hands fury sad slay 3 onlayer back at Position(ypos=1125)
                with Dissolve(0.5)
                $ renpy.pause(0.25)
                show hands fury sad slay 4 onlayer back at Position(ypos=1125)
                with Dissolve(0.25)
                $ renpy.pause(0.125)
                show hands fury sad slay 5 onlayer back at Position(ypos=1125)
                with Dissolve(0.25)
                $ renpy.pause(0.125)
                hide hands onlayer back
                with Dissolve(0.25)
                $ renpy.pause(0.125)
                $ blade_held = False
                $ default_mouse = "default"
                stop music
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
                hide quiet onlayer farback
                hide quiet onlayer front
                show farback quiet onlayer farback at Position(ypos=1125)
                with Dissolve(4.0)
                show mirror quiet distant onlayer back at Position(ypos=1125)
                if loops_finished != 0:
                    truth "Though her heart is pierced, you do not get the chance to watch her die. Nor will you ever. It's time for you to leave. Memory returns.\n"
                else:
                    truth "Though her heart is pierced, you do not get the chance to watch her die. Something has taken her away, and it's left something else in her place.\n"
                $ achievement.grant("ACH_FURY_SAD_SLAY")
                $ fury_end = "slay"
                $ princess_deny += 2
                $ princess_kept += 1
                $ trait_stubborn = False
                jump fury_mirror_special

                # END

label fury_other_conclusion:
    play tertiary "audio/final/fury_heart_loop.ogg" loop
    play sound "audio/_pristine/sfx/Apotheosis Oppresive AMB_2loop.flac" loop
    #play music "audio/_pristine/music/fury/The Fury Meta Intro.flac"
    #queue music "audio/_pristine/music/fury/The Fury Meta Loop.flac" loop
    # commenting out lines for hero + stubborn + broken below
    voice "audio/_pristine/voice/fury/narrator/63.flac"
    scene bg fury abs neutral onlayer back at Position(ypos=1125)
    show fury abs neutral onlayer front at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    n "You are whole again, and in your body—the same body you arrived in. The Princess stands before you, her dress of skin more tattered than before, her face sullen.\n"
    if fury_source == "tower":
        voice "audio/_pristine/voice/fury/princess/46.flac"
        show fury abs neutral talk onlayer front
        with dissolve
        sp "It's all hollow. I ripped you to pieces. I broke your will. But it means nothing.\n"
        voice "audio/_pristine/voice/fury/princess/47.flac"
        show fury abs neutral talk upset onlayer front
        with Dissolve(1.0)
        sp "I am forever a piece unfinished. A song with no refrain.\n"
    else:
        #'of' extraneous, deleted
        voice "audio/_pristine/voice/fury/princess/48.flac"
        show fury abs neutral talk upset onlayer front
        with Dissolve(1.0)
        sp "After all that, why do I still feel so empty?\n"

    # All fake choices but the bottom

    $ config.menu_include_disabled = True
    menu:
        extend ""

        "{i}• ''Why did you keep me alive?''{/i}" if tower_false_choice:
            $ config.menu_include_disabled = False

        "{i}• ''I've been here so long.''{/i}" if tower_false_choice:
            $ config.menu_include_disabled = False

        "{i}• ''Everyone is gone.''{/i}" if tower_false_choice:
            $ config.menu_include_disabled = False

        "{i}• ''There's no one else here.''{/i}" if tower_false_choice:
            $ config.menu_include_disabled = False

        "{i}• ''I can't feel anything anymore.''{/i}" if tower_false_choice:
            $ config.menu_include_disabled = False

        "{i}• ''But still, I'm here. Watching.''{/i}" if tower_false_choice:
            $ config.menu_include_disabled = False

        "{i}• [[There is nothing for you to say.]{/i}":
            $ config.menu_include_disabled = False


    if fury_source == "tower":
        voice "audio/_pristine/voice/fury/princess/49.flac"
        show fury abs desperate talk onlayer front
        with Dissolve(1.0)
        sp "We're so different. How could I ever hope for you to understand me?\n"
    else:
        voice "audio/_pristine/voice/fury/princess/50.flac"
        show fury abs desperate onlayer front
        with Dissolve(1.0)
        sp "If only you could see what I see. If only you could remember what I remember. If only you weren't so weak.\n"
        voice "audio/_pristine/voice/fury/princess/51.flac"
        show fury abs desperate talk onlayer front
        with dissolve
        sp "If only I could make you better. But... maybe I can.\n"
        $ gallery_fury.unlock_item(8)
        $ renpy.save_persistent()

    voice "audio/_pristine/voice/fury/narrator/64.flac"
    show fury abs begin onlayer front
    with Dissolve(1.0)
    n "She stands, arms outstretched, neck craned, gaze transfixed on something unseen above you both.\n"
    if fury_source == "tower":
        voice "audio/_pristine/voice/fury/princess/52.flac"
        sp "But perhaps there is a way to grant you understanding. Perhaps there is a way to make myself whole once more.\n"
    else:
        voice "audio/_pristine/voice/fury/princess/53.flac"
        sp "This will all be worth it. It has to be.\n"

    voice "audio/_pristine/voice/fury/narrator/65.flac"
    #play secondary "audio/final/Assorted_TapestyUnraveledBreakingRip_1.flac"
    play audio "audio/final/Spectre_HeartCrush_2 copy.flac"
    show player fury abs begin onlayer inyourface at Position(ypos=1125)
    with Dissolve(1.0)
    n "You are unwound again.\n"
    play audio "audio/_pristine/sfx/Fury Body Horror_19.flac"
    voice "audio/_pristine/voice/fury/narrator/66.flac"
    show bg fury abs sequence onlayer back
    show player fury abs sequence onlayer inyourface
    show fury abs sequence onlayer front
    with Dissolve(0.5)
    n "But it's different this time. Nothing slithers into your cells. You can feel something changing inside of you, but you see her changing, too.\n"
    play audio "audio/_pristine/sfx/Fury Body Horror_25.flac"
    voice "audio/_pristine/voice/fury/narrator/67.flac"
    hide player onlayer inyourface
    show bg fury abs sequence 2 onlayer back
    show fury abs sequence 2 onlayer front
    with Dissolve(1.0)
    n "Threads, strands of you, becoming pieces of something new. Something that's both you and her... oh no, absolutely not! You have to stop this, do you hear me? You have to stop this or the entire world ends—\n"
    play audio "audio/_pristine/sfx/Fury Body Horror_17.flac"
    show bg fury abs sequence 3 onlayer back
    show fury abs sequence 3 onlayer front
    with Dissolve(1.0)
    truth "But there is nothing left to stop anything. Your consciousness drifts towards hers.\n"
    if fury_source == "tower":
        voice "audio/_pristine/voice/fury/princess/54.flac"
        play audio "audio/_pristine/sfx/Fury Body Horror_1.flac"
        show bg fury abs sequence 4 onlayer back
        show fury abs sequence 4 onlayer front
        with Dissolve(1.0)
        sp "Yes. YES. See me as I have had to see you!\n"
        $ gallery_fury.unlock_item(9)
        $ renpy.save_persistent()
        play audio "audio/_pristine/sfx/Dragon Bubbling Flesh_3.flac"
        play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 15.0
        stop music fadeout 15.0
        stop sound fadeout 15.0
        stop tertiary fadeout 15.0
        hide fury onlayer front
        show bg fury abs sequence end onlayer back
        show quiet creep1 onlayer back at Position(ypos=1125)
        show rear fury abs sequence end onlayer front at Position(ypos=1125)
        show fury abs sequence end onlayer inyourface at Position(ypos=1125)
        with Dissolve(1.0)
        truth "You do. You see a towering heart, wounded and alone. One that is familiar to you, if distant.\n"
    else:
        play audio "audio/_pristine/sfx/Fury Body Horror_1.flac"
        voice "audio/_pristine/voice/fury/princess/55.flac"
        show bg fury abs sequence 4 onlayer back
        show fury abs sequence 4 onlayer front
        with Dissolve(1.0)
        sp "There doesn't have to be distance between us anymore. You feel it too, don't you?\n"
        play audio "audio/_pristine/sfx/Dragon Bubbling Flesh_3.flac"
        play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 15.0
        stop music fadeout 15.0
        stop sound fadeout 15.0
        stop tertiary fadeout 15.0
        hide fury onlayer front
        show bg fury abs sequence end onlayer back
        show quiet creep1 onlayer back at Position(ypos=1125)
        show rear fury abs sequence end onlayer front at Position(ypos=1125)
        show fury abs sequence end onlayer inyourface at Position(ypos=1125)
        with Dissolve(1.0)
        truth "You do. You feel as though you're coming home. A home you've forgotten, but one that never left your heart.\n"

    voice "audio/_pristine/voice/fury/princess/56.flac"
    show quiet creep3 onlayer back
    with Dissolve(1.0)
    sp "No... this isn't right. I feel... cold.\n"
    play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
    hide fury onlayer inyourface
    hide rear onlayer front
    show hands fury abs 1 onlayer back at Position(ypos=1125)
    with Dissolve(1.0)
    $ renpy.pause(1.0)
    show hands fury abs 2 onlayer back at Position(ypos=1125)
    with Dissolve(1.0)
    $ renpy.pause(0.5)
    show hands fury abs 3 onlayer back at Position(ypos=1125)
    with Dissolve(0.5)
    $ renpy.pause(0.25)
    show hands fury abs 4 onlayer back at Position(ypos=1125)
    with Dissolve(0.25)
    $ renpy.pause(0.125)
    hide hands onlayer back
    with Dissolve(0.25)
    $ renpy.pause(0.125)
    $ blade_held = False
    $ default_mouse = "default"
    stop music
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
    hide quiet onlayer farback
    hide quiet onlayer front
    show farback quiet onlayer farback at Position(ypos=1125)
    with Dissolve(4.0)
    show mirror quiet distant onlayer back at Position(ypos=1125)
    $ fury_end = "heart"
    $ princess_kept += 1
    $ princess_satisfy += 1
    $ current_princess = "furyheart"
    if loops_finished != 0:
        truth "The tethers that started to form between you have snapped. Your union has been halted. It's time for you to leave. Memory returns.\n"
    else:
        truth "The tethers that attempted to form between you have snapped. Your union has been halted. Something has taken her away, and it's left something else in her place.\n"
    menu:

        "{i}• [[Approach the mirror.]{/i}":
            hide mirror onlayer back
            show content m empty onlayer front at Position(ypos=1125)
            show mirror frame onlayer front at Position(ypos=1125)
            with Dissolve(2.0)
            truth "Silence as you approach.\n"
            menu:

                extend ""

                "{i}• [[Gaze into your reflection.]{/i}":
                    jump mirror_sort


    # END

##############################

label fury_pristine_unarmed:

    voice "audio/_pristine/voice/fury/contrarian/15.flac"
    play audio "audio/one_shot/collapse.flac"
    play secondary "audio/_pristine/sfx/guts_splash.flac"
    hide ribbons onlayer inyourface
    hide cg onlayer front
    hide bg onlayer back
    show bg fury unwind onlayer back at Position(ypos=1125)
    show fury unwind flat onlayer front at Position(ypos=1125)
    show ribbons fury start 1 onlayer inyourface at Position(ypos=1350)
    with Dissolve(1.0)
    contrarian "Pah, who needs 'stuff' anyways? Look at us! We might be all over the place, but we're fiiiiiine.\n"
    voice "audio/_pristine/voice/fury/stubborn/31.flac"
    stubborn "That's the first thing you've said that's made any sense. We may be down again, but we're not out for the count yet.\n"
    voice "audio/_pristine/voice/fury/princess/57.flac"
    show fury unwind annoyed talk onlayer front
    with dissolve
    sp "Still, you fall to pieces. What is the point of all this power if there's no challenge to using it? This is a numb existence.\n"
    show fury unwind annoyed onlayer front
    label fury_pristine_unarmed_menu:
        menu:
            extend ""

            "{i}• (Explore) ''Numb?! You ripped your own skin off!''{/i}" if pristine_fury_talk_attempt == False:
                jump fury_pristine_other_talk_join

            "{i}• (Explore) ''If you want a challenge, how about you play fair?''{/i}" if pristine_fury_talk_attempt == False:
                jump fury_pristine_other_talk_join

            "{i}• (Explore) ''Do you think this is enough to stop me?''{/i}" if pristine_fury_talk_attempt == False:
                jump fury_pristine_other_talk_join

            "{i}• (Explore) ''What happened to you? You're so much colder than you were before.''{/i}" if pristine_fury_talk_attempt == False:
                jump fury_pristine_other_talk_join

            "{i}• [[Give up.]{/i}":
                voice "audio/_pristine/voice/fury/princess/58.flac"
                show fury unwind surprise talk onlayer front
                with dissolve
                sp "Don't think you can just quit so soon. Not after all those guts you showed me last time.\n"
                voice "audio/_pristine/voice/fury/princess/59.flac"
                stop sound fadeout 5.0
                stop tertiary fadeout 5.0
                play audio "audio/final/fury_walk_single.flac"
                play tertiary "audio/final/Fury_WetPunch_2.flac"
                hide fury onlayer front
                show bg fury unwind onlayer back at shakeshort
                show starving den buried 1 onlayer back at Position(ypos=1125)
                show unwound 1 talk onlayer front at shakeshort
                hide ribbons onlayer inyourface
                with dissolve
                sp "Let's see what you're really made of. Maybe we can find where your courage decided to hide away.\n"
                jump fury_unwind_sequence

            "{i}• [[Ignore her and push forward.]{/i}":
                play music "audio/_pristine/music/fury/The Fury Oppressive Intro.flac"
                queue music "audio/_pristine/music/fury/The Fury Oppressive Loop.flac" loop
                voice "audio/_pristine/voice/fury/narrator/68.flac"
                play audio "audio/_pristine/sfx/Fury Body Horror_23.flac"
                hide ribbons onlayer inyourface
                hide fury onlayer front
                hide bg onlayer back
                scene bg fury charge onlayer back at Position(ypos=1125)
                #show ribbons fury start 1 onlayer inyourface at Position(ypos=1125)
                show cg fury unarmed 1 onlayer front at Position(ypos=1125)
                show player fury unarmed 1 onlayer inyourface at Position(ypos=1125)
                with fade
                n "Though the ribbons of your unraveled body struggle to coordinate, you manage to put one foot forward.\n"
                voice "audio/_pristine/voice/fury/princess/60.flac"
                show cg fury unarmed 1 talk onlayer front
                with dissolve
                sp "Oh. So there is some challenge left in you. Let's see how long it takes to crush it.\n"
                voice "audio/_pristine/voice/fury/narrator/69.flac"
                play audio "audio/_pristine/sfx/Fury Body Horror_6.flac"
                play tertiary "audio/_pristine/sfx/Fury Skin peel_1.flac"
                show cg fury unarmed 1 clench onlayer front
                show player fury unarmed 1 explode onlayer inyourface
                n "The Princess clenches her fist, and as her knuckles tighten, even more of you becomes undone. Your skin is flayed, your fatty tissue torn from your muscles.\n"
                $ gallery_fury.unlock_item(10)
                $ renpy.save_persistent()
                voice "audio/_pristine/voice/fury/princess/61.flac"
                #play audio "audio/final/fury_walk_single.flac"
                show cg fury unarmed 1 talk onlayer front
                with dissolve
                sp "What are you? You're clearly not your skin.\n"
                voice "audio/_pristine/voice/fury/contrarian/16.flac"
                play audio "audio/_pristine/sfx/Fury Skin peel_2.flac"
                show cg fury unarmed 1 onlayer front
                show player fury unarmed 2 onlayer inyourface
                with Dissolve(1.0)
                contrarian "Why would we ever be just our skin? We lost so much of it last time, we're obviously more than that.\n"
                voice "audio/_pristine/voice/fury/hero/23.flac"
                hero "Who cares?! I don't like not having skin. It hurts!\n"
                voice "audio/_pristine/voice/fury/stubborn/32.flac"
                stubborn "The pain doesn't matter, just keep walking. She can't stop us if we don't let her!\n"
                menu:
                    extend ""

                    "{i}• (Explore) Guys, I'm not sure we've got this one.{/i}":
                        jump fury_unarmed_give_up_1

                    "{i}• [[Give up.]{/i}":
                        label fury_unarmed_give_up_1:
                            stop music
                            voice "audio/_pristine/voice/fury/stubborn/33.flac"
                            play audio "audio/one_shot/collapse.flac"
                            play secondary "audio/_pristine/sfx/guts_splash.flac"
                            hide ribbons onlayer inyourface
                            hide cg onlayer front
                            hide bg onlayer back
                            hide player onlayer inyourface
                            show bg fury unwind onlayer back at Position(ypos=1125)
                            show fury unwind flat onlayer front at Position(ypos=1125)
                            with Dissolve(1.0)
                            stubborn "No, come on! It's just skin! What's wrong with you?\n"
                            voice "audio/_pristine/voice/fury/princess/62.flac"
                            show fury unwind flat talk onlayer front
                            with dissolve
                            sp "And just when I was starting to get a little excited...\n"
                            voice "audio/_pristine/voice/fury/princess/58.flac"
                            show fury surprise talk onlayer front
                            with dissolve
                            sp "Don't think you can just quit so soon. Not after all the guts you showed me last time.\n" id fury_unarmed_give_up_1_b1d95399
                            voice "audio/_pristine/voice/fury/princess/59.flac"
                            stop sound fadeout 5.0
                            stop tertiary fadeout 5.0
                            play audio "audio/final/fury_walk_single.flac"
                            play tertiary "audio/final/Fury_WetPunch_2.flac"
                            hide fury onlayer front
                            show bg fury unwind onlayer back at shakeshort
                            show starving den buried 1 onlayer back at Position(ypos=1125)
                            show unwound 1 talk onlayer front at shakeshort
                            hide ribbons onlayer inyourface
                            with dissolve
                            sp "Let's see what you're really made of. Maybe we can find where your courage decided to hide away.\n"
                            jump fury_unwind_sequence

                    "{i}• [[Take another step.]{/i}":
                        voice "audio/_pristine/voice/fury/narrator/70.flac"
                        play audio "audio/_pristine/sfx/Fury Body Horror_6.flac"
                        scene bg fury charge onlayer back at spectre_small_zoom, Position(ypos=1125)
                        show cg fury unarmed 1 onlayer front at spectre_small_zoom, Position(ypos=1125)
                        n "Still you push on, placing one disaster of a foot in front of the other.\n"
                        #voice "audio/_pristine/voice/fury/narrator/71.flac"
                        #n "The Princess takes yet another step back.\n"
                        voice "audio/_pristine/voice/fury/princess/63.flac"
                        play audio "audio/final/fury_walk_single.flac"
                        hide cg onlayer front
                        show cg fury unarmed 2 clench talk onlayer front at shakeshort, Position(ypos=1125)
                        with Dissolve(0.5)
                        sp "Perhaps muscle is where you dwell.\n"
                        voice "audio/_pristine/voice/fury/narrator/72.flac"
                        play audio "audio/_pristine/sfx/Fury muscle peel_1.flac"
                        show cg fury unarmed 2 clench onlayer front
                        show player fury unarmed 2 explode onlayer inyourface
                        with dissolve
                        n "She smiles, and again, her will tears at you. Muscle untethers from bone.\n"
                        voice "audio/_pristine/voice/fury/hero/24.flac"
                        hero "But we need that! We can't do anything if we don't have muscle.\n"
                        play audio "audio/_pristine/sfx/Fury muscle peel_2.flac"
                        voice "audio/_pristine/voice/fury/contrarian/17.flac"
                        show player fury unarmed 3 onlayer inyourface
                        with dissolve
                        contrarian "Okay, Mr. Anatomy, I hear you, but have you considered how neat it would be if we still kept walking towards her... without it?\n"
                        voice "audio/_pristine/voice/fury/stubborn/34.flac"
                        stubborn "Yes, yes! Do it! Show her how tough we really are!\n"

                        menu:
                            extend ""

                            "{i}• (Explore) 'Mr. Anatomy' has a point. How {b}can{/b} we move without any muscle?{/i}":
                                jump fury_unarmed_give_up_2

                            "{i}• [[You don't have any muscle. Give up.]{/i}":
                                label fury_unarmed_give_up_2:
                                    voice "audio/_pristine/voice/fury/contrarian/18.flac"
                                    play audio "audio/one_shot/collapse.flac"
                                    play secondary "audio/_pristine/sfx/guts_splash.flac"
                                    hide ribbons onlayer inyourface
                                    hide cg onlayer front
                                    hide bg onlayer back
                                    hide player onlayer inyourface
                                    show bg fury unwind onlayer back at Position(ypos=1125)
                                    show fury unwind flat onlayer front at Position(ypos=1125)
                                    with Dissolve(1.0)
                                    contrarian "Boooooo! Booooo!\n"
                                    voice "audio/_pristine/voice/fury/stubborn/35.flac"
                                    stubborn "Yeah, what he said. Boo!\n"
                                    voice "audio/_pristine/voice/fury/hero/25.flac"
                                    hero "Oh, don't boo us! We're just following the rules of reality!\n"
                                    voice "audio/_pristine/voice/fury/contrarian/19.flac"
                                    contrarian "Yeah? Well the rules of reality suck! I want something better! I want a rewrite!\n"
                                    voice "audio/_pristine/voice/fury/princess/64.flac"
                                    show fury unwind flat talk onlayer front
                                    with dissolve
                                    sp "Oh... I thought you were something more.\n"
                                    voice "audio/_pristine/voice/fury/princess/65.flac"
                                    show fury unwind surprise talk onlayer front
                                    with dissolve
                                    sp "There must still be some spirit left in you. We just have to find it in all that meat and bone.\n"
                                    voice "audio/_pristine/voice/fury/princess/66a.flac"
                                    stop sound fadeout 5.0
                                    stop tertiary fadeout 5.0
                                    play audio "audio/final/fury_walk_single.flac"
                                    play tertiary "audio/final/Fury_WetPunch_2.flac"
                                    hide fury onlayer front
                                    show bg fury unwind onlayer back at shakeshort
                                    show starving den buried 1 onlayer back at Position(ypos=1125)
                                    show unwound 1 talk onlayer front at shakeshort
                                    hide ribbons onlayer inyourface
                                    with dissolve
                                    sp "This will hurt.\n"
                                    jump fury_unwind_sequence

                            "{i}• [[Take another step.]{/i}":
                                voice "audio/_pristine/voice/fury/narrator/73.flac"
                                play tertiary "audio/final/fury_walk_single.flac"
                                play audio "audio/_pristine/sfx/fury_bone_steps.flac"
                                hide bg onlayer back
                                hide cg onlayer front
                                show bg fury unarmed 3 onlayer back at shakeshort, Position(ypos=1125)
                                show cg fury unarmed 3 hitme onlayer back at shakeshort, Position(ypos=1125)
                                with Dissolve(1.0)
                                n "You shamble on, a mass of organs suspended in bone, all held together by the thinnest strands of connective tissue.\n"
                                voice "audio/_pristine/voice/fury/princess/67.flac"
                                show cg fury unarmed 3 hitme talk onlayer back
                                with dissolve
                                sp "I really thought that losing your muscle would be the end of you! This is exciting. We're in uncharted depths. I can't wait to see how much more of you I can take before you finally stop moving.\n"
                                voice "audio/_pristine/voice/fury/narrator/74.flac"
                                show cg fury unarmed 3 hitme onlayer back
                                with dissolve
                                n "The less that remains of your body, the more fiercely your spirit struggles against that of the Princess. But her power is immense.\n"
                                voice "audio/_pristine/voice/fury/narrator/75.flac"
                                play audio "audio/_pristine/sfx/Fury Body Horror_6.flac"
                                play tertiary "audio/final/fury_walk_single.flac"
                                show bg fury unarmed 3 onlayer back at shakeshort, Position(ypos=1125)
                                show cg fury unarmed 3 onlayer back at shakeshort, Position(ypos=1125)
                                with dissolve
                                n "As your organs slip from between your ribs, she takes another step back, only now, there is nowhere left for her to go. She is within your reach, if only you have the determination to reach her.\n"
                                voice "audio/_pristine/voice/fury/stubborn/36.flac"
                                stubborn "Of course we have determination. We made it this far, didn't we?\n"
                                voice "audio/_pristine/voice/fury/hero/26.flac"
                                hero "What does this make us? How can we lose so many vital parts of who we are and still be here?\n"
                                voice "audio/_pristine/voice/fury/contrarian/20.flac"
                                contrarian "The exact same way we lost every piece of ourselves twice before. Have you forgotten that we've literally died? Twice?\n"
                                $ gallery_fury.unlock_item(11)
                                $ renpy.save_persistent()
                                voice "audio/_pristine/voice/fury/princess/68.flac"
                                show cg fury unarmed 3 hitme talk onlayer back
                                with dissolve
                                sp "Come on. One more step. Do it! Hit me! Show me what you're made of!\n" id fury_unarmed_give_up_2_c18ab116
                                show cg fury unarmed 3 hitme onlayer back
                                menu:
                                    extend ""

                                    "{i}• (Explore) This is too much. It isn't going to work. Wouldn't it be better to just start over and try again?{/i}":
                                        jump fury_unarmed_give_up_2

                                    "{i}• [[You've done enough. It's time to die.]{/i}":
                                        stop music
                                        voice "audio/_pristine/voice/fury/contrarian/21.flac"
                                        play audio "audio/one_shot/collapse.flac"
                                        play secondary "audio/_pristine/sfx/guts_splash.flac"
                                        hide farback onlayer farback
                                        hide ribbons onlayer inyourface
                                        hide cg onlayer back
                                        hide cg onlayer front
                                        hide bg onlayer back
                                        hide player onlayer inyourface
                                        show bg fury unwind onlayer back at Position(ypos=1125)
                                        show fury unwind flat onlayer front at Position(ypos=1125)
                                        with Dissolve(1.0)
                                        contrarian "Boooooo!\n"
                                        voice "audio/_pristine/voice/fury/stubborn/35.flac"
                                        stubborn "Yeah, what he said. Boo!\n"
                                        voice "audio/_pristine/voice/fury/hero/27.flac"
                                        hero "Hey, don't boo us! We've been cheating the rules of reality for too long. We should have given up already, it sucks being like this.\n"
                                        voice "audio/_pristine/voice/fury/contrarian/22.flac"
                                        contrarian "Yeah? Well the rules of reality are boring! I want something better! I want a rewrite!\n"
                                        voice "audio/_pristine/voice/fury/princess/69.flac"
                                        show fury unwind annoyed talk onlayer front
                                        with dissolve
                                        sp "No. No! You don't get to die on me now. Not after you've shown me so much of what you're capable of.\n"
                                        voice "audio/_pristine/voice/fury/princess/70.flac"
                                        stop sound fadeout 5.0
                                        stop tertiary fadeout 5.0
                                        play audio "audio/final/fury_walk_single.flac"
                                        play tertiary "audio/final/Fury_WetPunch_2.flac"
                                        hide fury onlayer front
                                        show bg fury unwind onlayer back at shakeshort
                                        show starving den buried 1 onlayer back at Position(ypos=1125)
                                        show unwound 1 talk onlayer front at shakeshort
                                        hide ribbons onlayer inyourface
                                        with dissolve
                                        sp "We're going to keep digging, until we find that spark of resistance and reignite it. I know it's still in there somewhere. And finding it is going to hurt so, so much.\n" id fury_unarmed_give_up_2_eecfc0d1
                                        jump fury_unwind_sequence

                                    "{i}• [[Reach for her heart.]{/i}":
                                        play audio "audio/_pristine/sfx/fury_unarmed_final_dissolve.flac"
                                        voice "audio/_pristine/voice/fury/narrator/76.flac"
                                        hide farback onlayer farback
                                        hide cg onlayer back
                                        hide bg onlayer back
                                        hide fury onlayer back
                                        hide player onlayer inyourface
                                        show bg fury unarmed 4 onlayer farback at Position(ypos=1125)
                                        show panel1 fury unarmed 4 onlayer farback at Position(ypos=1125)
                                        show panel1 fury unarmed 4 player onlayer back at Position(ypos=1125)
                                        show panel2 fury unarmed 4 delayed onlayer back at Position(ypos=1125)
                                        show panel2 fury unarmed 4 player delayed onlayer front at Position(ypos=1125)
                                        show panel3 fury unarmed 4 delayed onlayer front at Position(ypos=1125)
                                        show panel3 fury unarmed 4 player delayed onlayer inyourface at Position(ypos=1125)
                                        with dissolve
                                        n "Your skeletal hand shoots towards her heart, but the closer it gets, the more brittle it becomes. Flakes of bone are peeled away, exposing the marrow, and the marrow melts, exposing nerves, and the nerves are stripped raw, until—\n{w=12.6}{nw}"
                                        show screen disableclick(0.5)
                                        $ default_mouse = "eye"
                                        play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 15.0
                                        stop music fadeout 15.0
                                        stop sound fadeout 15.0
                                        stop tertiary fadeout 15.0
                                        hide bg onlayer farback
                                        hide panel1 onlayer farback
                                        hide panel1 onlayer back
                                        hide panel2 onlayer back
                                        hide panel2 onlayer front
                                        hide panel3 onlayer front
                                        hide panel3 onlayer inyourface
                                        scene bg black
                                        $ renpy.pause(0.5)
                                        voice "audio/_pristine/voice/fury/hero/28.flac"
                                        hero "Until what?\n"
                                        voice "audio/_pristine/voice/fury/contrarian/23.flac"
                                        contrarian "I think he gave up on us.\n"
                                        voice "audio/_pristine/voice/fury/stubborn/37.flac"
                                        stubborn "Figures. He always seemed weak to me.\n"
                                        voice "audio/_pristine/voice/fury/princess/71.flac"
                                        spmid "In the end, you're... nothing. Just like what's left of me.\n"
                                        voice "audio/_pristine/voice/fury/hero/29.flac"
                                        hero "But we're still here, aren't we?\n"
                                        voice "audio/_pristine/voice/fury/stubborn/38.flac"
                                        stubborn "Which means we aren't finished.\n"
                                        voice "audio/_pristine/voice/fury/hero/30.flac"
                                        hero "What are we supposed to do, hit her with nothing?\n"
                                        stubcont "...\n"
                                        voice "audio/_pristine/voice/fury/extra/stubcont.flac"
                                        stubcont "Yes.\n"
                                        menu:
                                            extend ""

                                            "{i}• [[Slay the Princess.]{/i}":
                                                #play audio "audio/_pristine/sfx/fury_unarmed_impale.flac"
                                                #$ renpy.pause(0.5)
                                                play audio "audio/final/Razor_ImpaleSwordBody_6.flac"
                                                show farback quiet onlayer farback at Position(ypos=1125)
                                                show cg fury unarmed 5 onlayer back at Position(ypos=1125)
                                                truth "Something, or nothing, bursts forward from the place that is you. Threads in the shape of a pristine blade. They pierce her heart.\n"
                                                voice "audio/_pristine/voice/fury/princess/72.flac"
                                                show cg fury unarmed 5 talk onlayer back
                                                with dissolve
                                                sp "Huh. I felt that.\n"
                                                voice "audio/_pristine/voice/fury/hero/31.flac"
                                                show cg fury unarmed 5 end onlayer back
                                                with dissolve
                                                hero "We actually did it.\n"
                                                voice "audio/_pristine/voice/fury/stubborn/39.flac"
                                                stubborn "We actually won.\n"
                                                voice "audio/_pristine/voice/fury/contrarian/24.flac"
                                                contrarian "I always knew we had it in us! But what are we going to do with ourselves now?\n"
                                                voice "audio/_pristine/voice/fury/princess/73.flac"
                                                show cg fury unarmed 5 talk onlayer back
                                                with dissolve
                                                sp "It's... cold.\n"
                                                hide cg onlayer back
                                                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                                                hide fury onlayer inyourface
                                                hide rear onlayer front
                                                show hands fury unarmed 1 onlayer back at Position(ypos=1125)
                                                with Dissolve(1.0)
                                                $ renpy.pause(1.0)
                                                show hands fury unarmed 2 onlayer back at Position(ypos=1125)
                                                with Dissolve(1.0)
                                                $ renpy.pause(0.5)
                                                show hands fury unarmed 3 onlayer back at Position(ypos=1125)
                                                with Dissolve(0.5)
                                                $ renpy.pause(0.25)
                                                show hands fury unarmed 4 onlayer back at Position(ypos=1125)
                                                with Dissolve(0.25)
                                                $ renpy.pause(0.125)
                                                show hands fury unarmed 5 onlayer back at Position(ypos=1125)
                                                with Dissolve(0.25)
                                                $ renpy.pause(0.125)
                                                hide hands onlayer back
                                                with Dissolve(0.25)
                                                $ renpy.pause(0.125)
                                                $ blade_held = False
                                                $ default_mouse = "default"
                                                stop music
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
                                                hide quiet onlayer farback
                                                hide quiet onlayer front
                                                show farback quiet onlayer farback at Position(ypos=1125)
                                                with Dissolve(1.0)
                                                show mirror quiet distant onlayer back at Position(ypos=1125)
                                                $ achievement.grant("ACH_FURY_UNARMED")
                                                $ fury_end = "slay_unarmed"
                                                $ princess_kept += 1
                                                $ princess_satisfy += 1
                                                if loops_finished != 0:
                                                    truth "You do not get the chance to watch her die. Nor will you ever. It's time for you to leave. Memory returns.\n"
                                                else:
                                                    truth "You do not get the chance to watch her die. Something has taken her away, and it's left something else in her place.\n"
                                                jump mirror_start
                                                # END

#############################

label fury_pristine_tower:

    voice "audio/_pristine/voice/fury/broken/11.flac"
    broken "You should all just be grateful she's decided to keep us alive. Even in her defilement she is merciful.\n"
    voice "audio/_pristine/voice/fury/stubborn/40.flac"
    stubborn "We're not out for the count just yet.\n"
    if fury_blade_taken == False:
        # if you didn't bring the blade it just sends you to the standard adversary unwinding sequence - the "failure state" if you will
        voice "audio/_pristine/voice/fury/hero/32.flac"
        hero "But we didn't even bring a weapon.\n"
        voice "audio/_pristine/voice/fury/broken/12.flac"
        play audio "audio/one_shot/collapse.flac"
        play secondary "audio/_pristine/sfx/guts_splash.flac"
        hide ribbons onlayer inyourface
        hide cg onlayer front
        hide bg onlayer back
        show bg fury unwind onlayer back at Position(ypos=1125)
        show fury unwind flat onlayer front at Position(ypos=1125)
        show ribbons fury start 1 onlayer inyourface at Position(ypos=1350)
        with Dissolve(1.0)
        broken "Yes. Because we knew it was over.\n"
        voice "audio/_pristine/voice/fury/princess/74.flac"
        show fury unwind surprise talk onlayer front
        with dissolve
        sp "No weapon this time... it's almost as if you were planning on dying here. As if I'd grant you such a mercy. No, we're going to make this last forever.\n"
        voice "audio/_pristine/voice/fury/princess/75.flac"
        play audio "audio/final/fury_walk_single.flac"
        play tertiary "audio/final/Fury_WetPunch_2.flac"
        hide fury onlayer front
        show bg fury unwind onlayer back at shakeshort
        show starving den buried 1 onlayer back at Position(ypos=1125)
        show unwound 1 talk onlayer front at shakeshort
        hide ribbons fury start 1 onlayer inyourface
        with dissolve
        sp "Let's see how deep we need to dig to find the defiant little spark of your soul. This will hurt you.\n"
        jump fury_unwind_sequence
    # this continues if you brought a weapon

    jump fury_pristine_tower_start_menu


label fury_pristine_tower_start_menu:
    default fury_fail_talk = False
    default fury_tower_talk_attempt_1_thing = ""
    menu:
        extend ""

        "{i}• (Explore) ''You damned cheater! Give me my insides back!''{/i}":
            $ fury_tower_talk_attempt_1_thing = "insides"
            if fury_fail_talk == False:
                jump fury_tower_talk_attempt

        "{i}• (Explore) ''I killed you last time, I swear on everything that I'm going to find a way to kill you again!''{/i}":
            $ fury_tower_talk_attempt_1_thing = "slay"
            if fury_fail_talk == False:
                label fury_tower_talk_attempt:
                    $ fury_fail_talk = True
                    voice "audio/_pristine/voice/fury/narrator/18.flac"
                    play audio "audio/_pristine/sfx/Fury gurgle speaking blood_6.flac"
                    show cg fury unarmed 1 onlayer front
                    with dissolve
                    n "But the words don't leave your metaphorical mouth. Instead, all that leaves you is a wet and horrible gurgling as tissue vibrates out of place.\n"
                    voice "audio/_pristine/voice/fury/hero/33.flac"
                    hero "Our... 'metaphorical' mouth?\n"
                    voice "audio/_pristine/voice/fury/princess/76a.flac"
                    show cg fury unarmed 1 talk onlayer front
                    with dissolve
                    sp "You don't have the means to speak anymore, do you? How tragic.\n"
                    voice "audio/_pristine/voice/fury/princess/77.flac"
                    show cg fury tower torment talk onlayer front
                    with dissolve
                    sp "Hm. It is tragic, though, isn't it? I'm not satisfied divining fear and indignation from your eyes alone. A quivering mound of flesh is no companion.\n"
                    voice "audio/_pristine/voice/fury/narrator/77.flac"
                    play audio "audio/_pristine/sfx/fury_snap_assemble.flac"
                    hide ribbons onlayer inyourface
                    show cg fury tower snap onlayer front
                    show player fury mouth assembled onlayer inyourface at Position(ypos=1125)
                    with Dissolve(1.0)
                    n "She snaps her fingers, and the basic form of a vocal system assembles before you.\n"
                    voice "audio/_pristine/voice/fury/princess/78.flac"
                    show cg fury tower torment talk onlayer front
                    with dissolve
                    sp "Now, little bird, what was it you wanted to tell me?\n"
                    show cg fury tower torment onlayer front
                    jump fury_pristine_tower_menu_2

        "{i}• (Explore) ''I only killed you last time because you were going to end the world! We can talk ourselves back from this ledge.''{/i}":
            $ fury_tower_talk_attempt_1_thing = "soft"
            $ fury_baby_count += 1
            if fury_fail_talk == False:
                jump fury_tower_talk_attempt

        "{i}• (Explore) ''I'm sorry for what I did to you, but you did horrible things to me, too.''{/i}":
            $ fury_tower_talk_attempt_1_thing = "soft"
            $ fury_baby_count += 1
            if fury_fail_talk == False:
                jump fury_tower_talk_attempt

        "{i}• (Explore) ''Where is all of this supposed to end? We can't just keep killing each other forever.''{/i}":
            $ fury_tower_talk_attempt_1_thing = "soft"
            if fury_fail_talk == False:
                jump fury_tower_talk_attempt

        "{i}• [[This is no time for words. Step forward and engage your enemy.]{/i}":
            jump fury_pristine_tower_battle

label fury_pristine_tower_menu_2:
    default fury_pristine_tower_talk_first = False
    default fury_pristine_tower_sorry = False
    default fury_baby_count = 0
    menu:
        extend ""

        "{i}• (Explore) ''I'm sorry, okay? I'm sorry for what I did!''{/i}" if fury_pristine_tower_sorry == False:
            $ fury_baby_count += 2
            $ fury_pristine_tower_sorry = True
            $ gallery_fury.unlock_item(14)
            $ renpy.save_persistent()
            play audio "audio/_pristine/sfx/Fury gurgle speaking blood_6.flac"
            show player fury mouth assembled talk onlayer inyourface
            show cg fury unarmed 1 onlayer front
            with dissolve
            $ renpy.pause(1.0)
            if fury_early_sorry:
                voice "audio/_pristine/voice/fury/princess/79.flac"
                show cg fury tower torment talk onlayer front
                with dissolve
                sp "You already apologized, and I already refused to accept it.\n"
            voice "audio/_pristine/voice/fury/princess/80.flac"
            show player fury mouth assembled onlayer inyourface
            show cg fury unarmed 1 clench talk onlayer front
            with dissolve
            sp "I thought it might be pleasant to hear you grovel. I thought your misery might bring music back to my ears. But all it does is stoke my hatred of you. All it does it remind me that I was brought low by a sniveling wretch.\n"
            voice "audio/_pristine/voice/fury/stubborn/41.flac"
            show cg fury unarmed clench onlayer front
            with dissolve
            stubborn "We're no sniveling wretch. We destroyed her. Now act like it!\n"
            voice "audio/_pristine/voice/fury/broken/13.flac"
            broken "She destroyed us far more easily than we destroyed her. She has it right. We are wretched. We are sniveling.\n"
            voice "audio/_pristine/voice/fury/hero/34.flac"
            hero "I don't think you speak for the rest of us.\n"
            voice "audio/_pristine/voice/fury/princess/81.flac"
            show cg fury tower torment talk onlayer front
            with dissolve
            sp "Maybe I shouldn't have given you the gift of speech after all. Maybe I should take it back.\n"
            show cg fury tower torment onlayer front
            jump fury_pristine_tower_menu_2_choice

        "{i}• (Explore) ''I said, I'm going to kill you!''{/i}" if fury_tower_talk_attempt_1_thing == "slay":
            $ fury_pristine_tower_talk_first = True
            $ gallery_fury.unlock_item(14)
            $ renpy.save_persistent()
            play audio "audio/_pristine/sfx/Fury gurgle speaking blood_5.flac"
            play tertiary "audio/final/fury_walk_single.flac"
            show bg fury charge onlayer back at shakeshort
            show player fury mouth assembled talk onlayer inyourface at shakeshort
            show cg fury unarmed 2 onlayer front at shakeshort
            with dissolve
            $ renpy.pause(1.0)
            voice "audio/_pristine/voice/fury/stubborn/42.flac"
            show player fury mouth assembled onlayer inyourface
            with dissolve
            stubborn "Yeah, that's right! Tell her how dead we're going to make her!\n"
            voice "audio/_pristine/voice/fury/princess/82.flac"
            play tertiary "audio/final/fury_walk_single.flac"
            show bg fury charge onlayer back at shakeshort
            show cg fury 1 clench talk onlayer front at shakeshort
            with dissolve
            sp "I've made the mistake of underestimating your resolve before. Never again!\n"
            voice "audio/_pristine/voice/fury/narrator/78.flac"
            play audio "audio/_pristine/sfx/Fury body exploading_2.flac"
            hide player onlayer inyourface
            hide fury onlayer front
            hide cg onlayer front
            hide bg onlayer back
            scene bg black
            n "Before you can act, what's left of you... explodes.\n"
            jump fury_tower_explode_join

        "{i}• (Explore) ''I said, give me my insides back! ... please?''{/i}" if fury_tower_talk_attempt_1_thing == "insides":
            $ fury_baby_count += 1
            $ gallery_fury.unlock_item(14)
            $ renpy.save_persistent()
            $ fury_pristine_tower_talk_first = True
            play audio "audio/_pristine/sfx/Fury gurgle speaking blood_2.flac"
            show player fury mouth assembled talk onlayer inyourface
            show cg fury tower torment onlayer front
            with dissolve
            $ renpy.pause(1.0)
            voice "audio/_pristine/voice/fury/stubborn/43.flac"
            stubborn "Oh, yes, because begging is going to help with this one.\n"
            voice "audio/_pristine/voice/fury/broken/14.flac"
            show player fury mouth assembled onlayer inyourface
            with dissolve
            broken "It's better than the alternative. She's in control here. Without her mercy, there's nothing we can do.\n"
            voice "audio/_pristine/voice/fury/hero/35a.flac"
            hero "I don't think she wants to give us mercy.\n"
            #voice "audio/_pristine/voice/fury/stubborn/44.flac"
            #stubborn "So we'll have to take it.\n"
            voice "audio/_pristine/voice/fury/princess/83.flac"
            show cg fury tower torment talk onlayer front
            with dissolve
            sp "I didn't think I'd see you begging so quickly. How pathetic. In another life, I might have even thought it was adorable. But all it does now is fill me with contempt.\n"
            label fury_pristine_tower_menu_2_choice:
                voice "audio/_pristine/voice/fury/broken/15.flac"
                if fury_unarmed_previous:
                    show cg fury unarmed 1 onlayer front
                else:
                    show cg fury tower torment onlayer front
                with dissolve
                broken "Just submit already. What is there left for us to do?\n"
                $ config.menu_include_disabled = True
                menu:
                    extend ""

                    "{i}• [[It's hopeless. Submit.]{/i}":
                        $ config.menu_include_disabled = False
                        voice "audio/_pristine/voice/fury/broken/16.flac"
                        play audio "audio/one_shot/collapse.flac"
                        play secondary "audio/_pristine/sfx/guts_splash.flac"
                        $ blade_held = False
                        $ default_mouse = "default"
                        play tertiary "audio/one_shot/knife_bounce_several.flac"
                        hide ribbons onlayer inyourface
                        hide cg onlayer front
                        hide bg onlayer back
                        show bg fury unwind onlayer back at Position(ypos=1125)
                        show fury unwind flat onlayer front at Position(ypos=1125)
                        show ribbons fury start 1 onlayer inyourface at Position(ypos=1350)
                        with Dissolve(1.0)
                        broken "Yes. It is hopeless. This is what we deserve.\n"
                        voice "audio/_pristine/voice/fury/stubborn/45.flac"
                        stubborn "Pathetic. I can't believe we have to share a body.\n"
                        voice "audio/_pristine/voice/fury/princess/75.flac"
                        play audio "audio/final/fury_walk_single.flac"
                        play tertiary "audio/final/Fury_WetPunch_2.flac"
                        hide fury onlayer front
                        hide cg onlayer front
                        show bg fury unwind onlayer back at shakeshort
                        show starving den buried 1 onlayer back at Position(ypos=1125)
                        show unwound 1 talk onlayer front at shakeshort
                        hide ribbons fury start 1 onlayer inyourface
                        hide player onlayer inyourface
                        with dissolve
                        sp "Let's see how deep we need to dig to find the defiant little spark of your soul. This will hurt you.\n"
                        jump fury_unwind_sequence

                    "{i}• [[Seize control of your broken body and lay waste to your foe.]{/i}" if fury_baby_count < 2:
                        $ config.menu_include_disabled = False
                        jump fury_pristine_tower_battle

        "{i}• (Explore) ''We have to stop hurting each other!''{/i}":
            $ gallery_fury.unlock_item(14)
            $ renpy.save_persistent()
            $ fury_baby_count += 2
            play audio "audio/_pristine/sfx/Fury gurgle speaking blood_4.flac"
            show player fury mouth assembled talk onlayer inyourface
            show cg fury tower torment onlayer front
            with dissolve
            $ renpy.pause(1.0)
            voice "audio/_pristine/voice/fury/princess/84.flac"
            show player fury mouth assembled onlayer inyourface
            show cg fury unarmed 1 talk onlayer front
            with dissolve
            sp "Hurting each other? You've already taken my capacity for pain. You're the only thing left that hurts here.\n"
            jump fury_pristine_tower_menu_2_choice

        "{i}• (Explore) ''What's your end game here? Are we supposed to keep torturing each other forever?''{/i}":
            $ gallery_fury.unlock_item(14)
            $ renpy.save_persistent()
            default fury_unarmed_previous = False
            $ fury_unarmed_previous = True
            play audio "audio/_pristine/sfx/Fury gurgle speaking blood_6.flac"
            show player fury mouth assembled talk onlayer inyourface
            show cg fury tower torment onlayer front
            with dissolve
            $ renpy.pause(1.0)
            voice "audio/_pristine/voice/fury/princess/85.flac"
            show player fury mouth assembled onlayer inyourface
            show cg fury unarmed 1 talk onlayer front
            with dissolve
            sp "Your defiance robbed me of my 'end game.' You desecrated my divine spirit and plunged me into your realm of flesh. The only thing left for me is your torment.\n"
            jump fury_pristine_tower_menu_2_choice

        "{i}• [[This is no time for words. Step forward and engage your enemy.]{/i}":
            jump fury_pristine_tower_battle

label fury_pristine_tower_battle:
    play audio "audio/_pristine/sfx/Fury running organc bounce_2a.flac"
    voice "audio/_pristine/voice/fury/narrator/79.flac"
    hide fury onlayer front
    hide cg onlayer front
    hide ribbons fury start 1 onlayer inyourface
    hide bg onlayer back
    hide farback onlayer farback
    show bg fury charge onlayer back at spectre_small_zoom_instant, Position(ypos=1125)
    show cg fury tower 1 onlayer front at Position(ypos=1125)
    show ribbons fury start 1 onlayer front at shakeshort, Position(ypos=1125)
    show player fury mouth assembled onlayer inyourface at shakeshort
    with Dissolve(1.0)
    n "Skin flayed and organs flapping, you charge towards the Princess.\n"
    voice "audio/_pristine/voice/fury/stubborn/46.flac"
    stubborn "That's right! She'll never stop us!\n"
    voice "audio/_pristine/voice/fury/princess/86.flac"
    show cg fury tower 1 talk onlayer front
    with dissolve
    sp "Still you defy your god. I've made the mistake of underestimating your resolve before. Never again!\n"
    voice "audio/_pristine/voice/fury/narrator/80.flac"
    play audio "audio/_pristine/sfx/Fury body exploading_2.flac"
    play tertiary "audio/one_shot/knife_bounce_several.flac"
    $ blade_held = False
    $ default_mouse = "default"
    hide ribbons onlayer front
    hide player onlayer inyourface
    hide bg onlayer back
    hide cg onlayer front
    scene bg black
    n "As you swing for her heart, what's left of you... explodes.\n"
    label fury_tower_explode_join:
        voice "audio/_pristine/voice/fury/hero/36.flac"
        hero "So that's it? It's over? Just like that?\n"
        voice "audio/_pristine/voice/fury/broken/17.flac"
        broken "Of course it's over. It's been over since the very first moment we laid eyes on her.\n"
        voice "audio/_pristine/voice/fury/princess/87a.flac"
        spmid "This is the final note of your discordant melody. You will not return again, because you will live in that single tone forever.\n"
        voice "audio/_pristine/voice/fury/stubborn/47.flac"
        stubborn "No. NO. It's not over. We're a god killer. We've returned from death itself twice.\n"
        voice "audio/_pristine/voice/fury/broken/18.flac"
        broken "Didn't you hear her? We're not dead.\n"
        voice "audio/_pristine/voice/fury/hero/37.flac"
        hero "What's the difference?\n"
        voice "audio/_pristine/voice/fury/narrator/81.flac"
        n "From many perspectives, there isn't one. But functionally, that is, from your perspective, the difference is massive.\n"
        voice "audio/_pristine/voice/fury/narrator/82.flac"
        n "You are entirely laid bare, spread to each corner of the room. Yet you are wholly aware of the state you're in. Incapable of movement, but entirely capable of perception. In fact, perceiving your state is the only thing you can currently do. You are preserved, perfectly, in the amber of her torment.\n"
        voice "audio/_pristine/voice/fury/stubborn/48.flac"
        stubborn "We're more than this. We've lost bodies before. We just have to lose this one and make another.\n"
        label fury_tower_lose_body_menu:
            default fury_tower_lose_body_encouraged = False
            default fury_tower_lose_body_here = False
            default can_unwound = False
            menu:
                extend ""

                "{i}• (Explore) ''How are we supposed to lose this one?''{/i}" if fury_tower_lose_body_encouraged == False:
                    $ fury_tower_lose_body_encouraged = True
                    voice "audio/_pristine/voice/fury/stubborn/49.flac"
                    stubborn "I don't know! You're the one who makes things happen. So make it. Happen.\n"
                    jump fury_tower_lose_body_menu

                "{i}• (Explore) ''I can't do anything right now. She's not letting me.''{/i}" if fury_tower_lose_body_encouraged == False:
                    $ fury_tower_lose_body_encouraged = True
                    voice "audio/_pristine/voice/fury/stubborn/50.flac"
                    stubborn "We're better than her! You made things happen last time. So make them happen again. I'm with you.\n" id fury_tower_lose_body_menu_96a490a5
                    jump fury_tower_lose_body_menu

                "{i}• (Explore) ''And if we lose this body, then what? I'm tired of all this fighting. I can't do this anymore.''{/i}" if can_unwound:
                    voice "audio/_pristine/voice/fury/broken/19.flac"
                    show bg fury unwind onlayer back at Position(ypos=1125)
                    show starving den buried 4 onlayer inyourface at Position(ypos=1125)
                    show unwound 1 onlayer front at Position(ypos=1125)
                    hide ribbons fury start 1 onlayer inyourface
                    hide player onlayer inyourface
                    with Dissolve(2.0)
                    broken "We're all tired. None of us can go on.\n"
                    voice "audio/_pristine/voice/fury/stubborn/51.flac"
                    show starving den buried 2 onlayer inyourface at Position(ypos=1125)
                    with Dissolve(1.0)
                    stubborn "Then we have already lost.\n"
                    voice "audio/_pristine/voice/fury/princess/13a.flac"
                    hide starving onlayer inyourface
                    show starving den buried 1 onlayer back at Position(ypos=1125)
                    show unwound 1 talk onlayer front
                    with Dissolve(1.0)
                    sp "Let's see what we're made of.\n"
                    jump fury_unwind_sequence

                "{i}• (Explore) ''She's going to get worse. She gets worse every time we get to a new cabin.''{/i}" if fury_tower_lose_body_here == False:
                    $ fury_tower_lose_body_here = True
                    voice "audio/_pristine/voice/fury/stubborn/52.flac"
                    stubborn "Who said anything about getting to a new cabin? No. We make something new, {i}here{/i}.\n"
                    voice "audio/_pristine/voice/fury/broken/20.flac"
                    broken "It won't matter if you do. She'll just pull us apart again.\n"
                    voice "audio/_pristine/voice/fury/stubborn/53.flac"
                    stubborn "And preferably, we make something without {i}him{/i}.\n"
                    jump fury_tower_lose_body_menu

                "{i}• [[Shed this vessel for the next.]{/i}":
                    voice "audio/_pristine/voice/fury/narrator/83.flac"
                    n "Absolutely not! I refuse to let you just decide to die with your task unfinished. If you die here, the world is doomed!\n" id fury_tower_lose_body_menu_257d4fd3
                    jump fury_tower_battle_sequence

label fury_tower_battle_sequence:

    # life 1
    $ trait_broken = False
    truth "But you do die. There is a great release as you loose your grip on what's left of your flesh and blood.\n"
    play music "audio/_pristine/music/fury/The Fury Aggressive Intro.flac"
    queue music "audio/_pristine/music/fury/The Fury Aggressive Loop.flac" loop
    play audio "audio/one_shot/knife_pickup.flac"
    $ blade_held = True
    $ default_mouse = "blade"
    truth "And yet, you are still here.\n"
    voice "audio/_pristine/voice/fury/narrator/84.flac"
    scene bg fury unarmed 4 onlayer farback at Position(ypos=1125)
    show cg fury tower 2 onlayer farback at Position(ypos=1125)
    with fade
    n "You're on a— where the hell are you? Are you already at the Princess?\n"
    voice "audio/_pristine/voice/fury/extra/hunted.flac"
    hunted "This place is different! Rotten. Death all around us. I want to go back!\n"
    voice "audio/_pristine/voice/fury/princess/88.flac"
    show cg fury tower 2 talk onlayer farback
    with dissolve
    spmid "So you've returned. Already. And I remain here. Is this our final destination?\n"
    voice "audio/_pristine/voice/fury/narrator/85.flac"
    play audio "audio/_pristine/sfx/turn_unwound.flac"
    play tertiary "audio/one_shot/knife_bounce_several.flac"
    $ blade_held = False
    $ default_mouse = "default"
    show cg fury tower 2 tinted delayed onlayer farback
    n "The Princess tilts her head to look at you and with a gesture... you are unwound.\n"
    voice "audio/_pristine/voice/fury/hero/38.flac"
    hero "Again? Already?!\n"
    voice "audio/_pristine/voice/fury/princess/89.flac"
    show cg fury tower 2 tinted onlayer farback
    spmid "Clearly, I left you with too much room last time. Perhaps this cell will hold you better.\n"
    voice "audio/_pristine/voice/fury/stubborn/54.flac"
    stubborn "You know what to do. Again.\n"
    menu:

        extend ""

        "{i}• [[Die again.]{/i}":
            play audio "audio/one_shot/knife_pickup.flac"
            $ blade_held = True
            $ default_mouse = "blade"
            show cg fury tower 3 onlayer back at Position(ypos=1125)
            with dissolve
            truth "Again, you relinquish your body. And again you find yourself here, but somewhere else.\n"

    voice "audio/_pristine/voice/fury/narrator/86.flac"
    n "You're on a—\n{w=0.45}{nw}"
    show screen disableclick(0.5)
    #voice "audio/_pristine/voice/fury/extra/paranoid.flac"
    #paranoid "Everything keeps changing. It's all going too fast!\n"
    voice "audio/voices/ch3/razor/final/smitten/4.flac"
    smitten "She's gorgeous! Absolutely divine!\n"
    voice "audio/_pristine/voice/fury/stubborn/55.flac"
    stubborn "You! Guy who describes things! You'd better start saying what we do this time.\n"
    voice "audio/_pristine/voice/fury/narrator/87.flac"
    n "And... what are you doing?\n"
    voice "audio/_pristine/voice/fury/stubborn/56.flac"
    stubborn "Attacking her, obviously!\n"
    voice "audio/_pristine/voice/fury/narrator/88.flac"
    n "Right. Right. You charge towards the Princess and—\n{w=3.0}{nw}"
    show screen disableclick(0.5)
    voice "audio/_pristine/voice/fury/princess/90.flac"
    play audio "audio/_pristine/sfx/Fury Body Horror_12.flac"
    show cg fury tower 3 talk onlayer back
    with dissolve
    sp "There is no spark in you. Only matter devoid of life.\n"
    voice "audio/_pristine/voice/fury/narrator/89.flac"
    play audio "audio/_pristine/sfx/Fury body exploading_1_quiet.flac"
    play tertiary "audio/one_shot/knife_bounce_several.flac"
    $ blade_held = False
    $ default_mouse = "default"
    show cg fury tower 3 tinted onlayer back
    n "You explode.\n"
    voice "audio/_pristine/voice/fury/stubborn/57.flac"
    stubborn "Again!\n"
    menu:

        extend ""

        "{i}• [[And again.]{/i}":
            $ gallery_fury.unlock_item(12)
            $ renpy.save_persistent()
            play audio "audio/one_shot/knife_pickup.flac"
            $ blade_held = True
            $ default_mouse = "blade"
            show cg fury tower 4 onlayer front at Position(ypos=1125)
            with dissolve
            truth "You let yourself go, and you are living once more.\n"

    voice "audio/_pristine/voice/fury/narrator/90.flac"
    n "You're on a path—\n{w=0.95}{nw}"
    show screen disableclick(0.5)
    voice "audio/_pristine/voice/fury/extra/cheated.flac"
    cheated "We are not on a fucking path! I have no idea where we are!\n"
    voice "audio/_pristine/voice/fury/stubborn/58.flac"
    stubborn "We're in the middle of a fight, so act like it.\n"
    voice "audio/_pristine/voice/fury/narrator/91.flac"
    play audio "audio/_pristine/sfx/Fury running organc bounce_short.flac"
    n "So you are. Okay. You dive towards the Princess, and—\n{w=3.7}{nw}"
    show screen disableclick(0.5)
    voice "audio/_pristine/voice/fury/hero/39.flac"
    play audio "audio/_pristine/sfx/Fury Skin peel_4.flac"
    show cg fury tower 4 swivel onlayer front
    hero "We're unwound?\n"
    voice "audio/_pristine/voice/fury/narrator/92.flac"
    play audio "audio/_pristine/sfx/Fury Body Horror_1.flac"
    n "Yes. Her head swivels creakily on her neck, fire in her eyes as your body unravels with blinding pain.\n"
    voice "audio/_pristine/voice/fury/princess/91a.flac"
    play audio "audio/_pristine/sfx/Fury body exploading_2_quiet.flac"
    play tertiary "audio/one_shot/knife_bounce_several.flac"
    $ blade_held = False
    $ default_mouse = "default"
    show cg fury tower 4 tinted onlayer front
    sp "No.\n"
    voice "audio/_pristine/voice/fury/stubborn/57.flac"
    stubborn "Again.\n"
    menu:

        extend ""

        "{i}• [[AGAIN!]{/i}":
            play audio "audio/one_shot/knife_pickup.flac"
            $ blade_held = True
            $ default_mouse = "blade"
            show cg fury tower end onlayer inyourface at Position(ypos=1125)
            with dissolve
            truth "You have no body. You exist. You are reborn.\n"

    # final life
    $ trait_cold = True
    voice "audio/_pristine/voice/fury/narrator/93.flac"
    n "You're on a—\n{w=0.5}{nw}"
    show screen disableclick(0.5)
    voice "audio/_pristine/voice/fury/stubborn/59.flac"
    stubborn "No time! You! Narrate! Now!\n"
    voice "audio/_pristine/voice/fury/narrator/94.flac"
    play audio "audio/final/den_emerge.flac"
    n "Y-yes, of course. Pristine blade grasped firmly in your hands, you fly towards the Princess before she can turn to face you.\n"
    voice "audio/_pristine/voice/fury/hero/40.flac"
    hero "We might actually do it this time!\n"
    voice "audio/_pristine/voice/fury/princess/92.flac"
    sp "I can feel that body of yours slicing through the air. How many more times will I have to scatter you?\n"
    voice "audio/_pristine/voice/fury/narrator/95.flac"
    play audio "audio/_pristine/sfx/Dragon Bubbling Flesh_1.flac"
    show cg fury tower end glance onlayer inyourface
    with dissolve
    n "As she turns towards you, the very essence of your being begins to flake away, your muscles, then organs, then nerves laid bare and screaming as the rest of you is stripped of substance.\n"
    voice "audio/_pristine/voice/fury/cold/37.flac"
    cold "Oh, boo hoo. It's just a body.\n"
    voice "audio/_pristine/voice/fury/stubborn/60.flac"
    stubborn "It just needs to last long enough to sink this blade into her heart.\n"
    voice "audio/_pristine/voice/fury/narrator/96a.flac"
    play tertiary "audio/one_shot/knife_bounce_several.flac"
    $ blade_held = False
    $ default_mouse = "default"
    play audio "audio/_pristine/sfx/Fury body exploading_3_quiet.flac"
    show cg fury tower end tinted onlayer inyourface
    n "But it doesn't last. You are disintegrated. Everything goes dark—\n{w=5.4}{nw}"
    $ default_mouse = "eye"
    show screen disableclick(0.5)
    show cg fury tower end glance onlayer inyourface
    with Dissolve(1.0)
    truth "But there is no you to die.\n"
    voice "audio/_pristine/voice/fury/princess/93.flac"
    play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 15.0
    stop music fadeout 15.0
    stop sound fadeout 15.0
    stop tertiary fadeout 15.0
    show cg fury tower end talk onlayer inyourface
    with dissolve
    sp "How many times do I need to pulverize you before you finally understand. You are nothing! An empty void that dared to dream it was alive!\n"
    voice "audio/_pristine/voice/fury/cold/38.flac"
    show quiet creep1 onlayer front at Position(ypos=1125)
    show cg fury tower end glance onlayer inyourface at Position(ypos=1125)
    with Dissolve(1.0)
    cold "That feels... right.\n"
    voice "audio/_pristine/voice/fury/stubborn/61.flac"
    stubborn "IF WE'RE NOTHING, THEN WHY ARE WE STILL HERE?!\n"
    voice "audio/_pristine/voice/fury/cold/39.flac"
    show quiet creep2 onlayer front
    with Dissolve(1.0)
    cold "Because we always have been.\n"
    voice "audio/_pristine/voice/fury/hero/41.flac"
    hero "If we're nothing, then how can we do anything?\n"
    voice "audio/_pristine/voice/fury/cold/40.flac"
    show quiet creep3 onlayer front
    with Dissolve(1.0)
    cold "The same way we always have. Being nothing has never stopped us. Now end this. End her.\n"
    voice "audio/_pristine/voice/fury/princess/94.flac"
    show cg fury tower end talk onlayer inyourface
    with dissolve
    sp "You cannot win if you cannot be!\n"
    show cg fury tower end glance onlayer inyourface
    menu:
        extend ""

        "{i}• [[End this.]{/i}":
            play audio "audio/final/den_emerge.flac"
            hide cg onlayer inyourface
            hide cg onlayer front
            hide cg onlayer back
            hide cg onlayer farback
            hide bg onlayer farback
            show farback quiet onlayer farback at Position(ypos=1125)
            show cg fury tower final onlayer front at Position(ypos=1125)
            show cg fury tower final player onlayer inyourface at Position(ypos=1125)
            with Dissolve(1.0)
            truth "A force races towards the Princess' exposed heart. Threads of texture pulled from an all-encompassing nothing.\n"
            voice "audio/_pristine/voice/fury/princess/95.flac"
            show cg fury tower final talk onlayer front
            with dissolve
            sp "How?! I've scattered the atoms you clung to and there was nothing there to find! You can't exist!\n"
            $ gallery_fury.unlock_item(13)
            $ renpy.save_persistent()
            play audio "audio/final/Razor_ImpaleSwordBody_6.flac"
            hide cg onlayer inyourface
            show cg fury final tower stab onlayer front
            with Dissolve(1.0)
            truth "The threads pierce her heart and cradle her spirit.\n"
            voice "audio/_pristine/voice/fury/stubborn/62.flac"
            stubborn "It's over.\n"
            voice "audio/_pristine/voice/fury/princess/96.flac"
            show cg fury unarmed 5 talk onlayer front
            with Dissolve(1.0)
            sp "Oh. I think I understand you now. I'm sorry. I didn't mean to do the things I did to you. I... don't think I knew what I was doing.\n"
            voice "audio/_pristine/voice/fury/hero/42.flac"
            show cg fury unarmed 5 end onlayer front
            with dissolve
            hero "She sounds genuine.\n"
            voice "audio/_pristine/voice/fury/cold/41.flac"
            cold "They always do in the end.\n"
            voice "audio/_pristine/voice/fury/princess/97.flac"
            show cg fury unarmed 5 okay onlayer front
            with Dissolve(1.0)
            sp "It's cold. But... I'm going to be okay, right?\n"
            play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
            hide cg onlayer front
            hide cg onlayer back
            hide fury onlayer inyourface
            hide rear onlayer front
            show hands fury unarmed 1 onlayer front at Position(ypos=1125)
            with Dissolve(1.0)
            $ renpy.pause(1.0)
            show hands fury unarmed 2 onlayer front at Position(ypos=1125)
            with Dissolve(1.0)
            $ renpy.pause(0.5)
            show hands fury unarmed 3 onlayer front at Position(ypos=1125)
            with Dissolve(0.5)
            $ renpy.pause(0.25)
            show hands fury unarmed 4 onlayer front at Position(ypos=1125)
            with Dissolve(0.25)
            $ renpy.pause(0.125)
            show hands fury unarmed 5 onlayer front at Position(ypos=1125)
            with Dissolve(0.25)
            $ renpy.pause(0.125)
            hide hands onlayer front
            with Dissolve(0.25)
            $ renpy.pause(0.125)
            $ blade_held = False
            $ default_mouse = "default"
            stop music
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
            hide quiet onlayer farback
            hide quiet onlayer front
            show farback quiet onlayer farback at Position(ypos=1125)
            with Dissolve(1.0)
            show mirror quiet distant onlayer back at Position(ypos=1125)
            $ achievement.grant("ACH_FURY_TOWER")
            $ fury_end = "slay_tower"
            $ princess_kept += 1
            $ princess_satisfy += 1
            if loops_finished != 0:
                truth "You do not get the chance to respond, nor will you ever. It's time to leave. Memory returns.\n"
            else:
                truth "You do not get the chance to respond. Something has taken her away, and it's left something else in her place.\n"
            $ trait_broken = False
            $ trait_cold = True
            jump mirror_start
            # END
