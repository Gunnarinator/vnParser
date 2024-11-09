label nightmare_2_start:

    # starting things up

    stop music
    stop sound
    stop secondary
    $ default_mouse = "default"
    $ blade_held = False
    $ current_loop = 2
    $ quick_menu = False
    $ config.menu_include_disabled = False
    $ current_princess = "clarity"
    $ clarity_encountered = True

    $ trait_stubborn = True
    $ trait_hunted = True
    $ trait_smitten = True
    $ trait_paranoid = True
    $ trait_skeptic = True
    $ trait_contrarian = True
    $ trait_cheated = True
    $ trait_cold = True
    $ trait_broken = True
    $ trait_opportunist = True

    default nightmare_2_wait_attempt = False
    play sound "audio/looping/uncomfortable ambiance heightened.ogg" loop fadein 1.0
    play secondary "audio/looping/uncomfortable ambiance.ogg" loop fadein 1.0
    scene chapter clarity1
    with fade
    show text _("{color=#FFFFFF00}The Moment of Clarity.{/color}") at Position(ypos=850)
    $ renpy.pause(1.0)
    show chapter clarity2
    $ renpy.pause(0.85)
    show chapter clarity3
    $ renpy.pause(0.7)
    show chapter clarity4
    $ renpy.pause(0.55)
    show chapter clarity5
    $ renpy.pause(0.4)
    show chapter clarity6
    $ renpy.pause(0.35)
    show chapter clarity7
    $ renpy.pause(0.2)
    show chapter clarity8
    $ renpy.pause(2.0)
    show txt clarity at distortion
    $ renpy.pause(4.0)

    if persistent.quick_menu:
        $ quick_menu = True

    play music "audio/_music/ch3/clarity/The Moment of Clarity INTRO.flac"
    queue music "audio/_music/ch3/clarity/The Moment of Clarity LOOP.flac" loop

    scene stars clarity onlayer farback at Position(ypos=1125)
    show back path clarity onlayer back at Position(ypos=1125)
    show mid path clarity onlayer front at Position(ypos=1125)
    show front path clarity onlayer inyourface at Position(ypos=1125)

    show bg black
    hide text
    #show loading_icon
    hide chapter
    with fade

    $ gallery_clarity.unlock_gallery()
    $ gallery_clarity.unlock_item(1)
    $ renpy.save_persistent()
    # fast
    voice "audio/voices/ch3/clarity/narrator/1.flac"
    n "You're on a path in the—\n{w=1.8}{nw}"
    show screen disableclick(0.5)
    voice "audio/voices/ch3/clarity/paranoid/1.flac"
    paranoid "Shit! Shit! What— what the hell was that?! Who are we? What are we doing?!\n"
    voice "audio/voices/ch3/clarity/broken/1.flac"
    broken "There was a Princess, I think. It's all so fuzzy. It hurts when I try to remember.\n"
    #voice "audio/voices/ch3/clarity/hero/1.flac"
    #hero "I think we were trying to save the world.\n"
    voice "audio/voices/ch3/clarity/narrator/2.flac"
    n "You shouldn't know about the Princess. At least not until I... You've already been here, haven't you?\n"
    voice "audio/voices/ch3/clarity/hero/2.flac"
    hero "I guess? It feels so long ago. Almost like we've never left.\n"
    voice "audio/voices/ch3/clarity/broken/2.flac"
    broken "We have to let her out.\n"
    voice "audio/voices/ch3/clarity/narrator/3.flac"
    n "No, that's the opposite of what you're here to do. You have to Slay her.\n"
    voice "audio/voices/ch3/clarity/paranoid/2.flac"
    paranoid "Slay... we decided not to do that, didn't we?\n"
    voice "audio/voices/ch3/clarity/opportunist/1.flac"
    opportunist "Yeah, we're supposed to let her out. It's really the only way this works out for us, if you think about it. She's the one with power here. Nobody else can do much of anything.\n"
    voice "audio/voices/ch3/clarity/stubborn/1.flac"
    stubborn "No, we were supposed to keep her trapped there forever... I think.\n"
    voice "audio/voices/ch3/clarity/cold/1.flac"
    cold "We're supposed to be unfeeling. How many times do I have to tell you to snuff out your heart?\n"
    voice "audio/voices/ch3/clarity/hunted/1.flac"
    hunted "We can't be unfeeling. Not when there's so much fear everywhere.\n"
    voice "audio/voices/ch3/clarity/contrarian/1.flac"
    contrarian "There's nothing for us to do. We've already tried everything.\n"
    voice "audio/voices/ch3/clarity/smitten/1.flac"
    smitten "We love her. So we have to set her free.\n"
    voice "audio/voices/ch3/clarity/skeptic/1.flac"
    skeptic "Can we love something that hates us? Can we love something that hurts us?\n"
    voice "audio/voices/ch3/clarity/smitten/2.flac"
    smitten "To be given an ounce of kindness from something so cruel would be more pure than any other love.\n"
    voice "audio/voices/ch3/clarity/cheated/1.flac"
    cheated "Why are there so many of us? There aren't supposed to be so many of us.\n"
    voice "audio/voices/ch3/clarity/narrator/4.flac"
    n "This is bad. You need to get a grip. What did you let happen? How many times have you been here?\n"
    label nightmare_2_menu:
        default nm2_wrong = False
        default nm2_count = 0
        default nm2_how_many = False
        default nm2_how_many_follow = False
        default nm2_how_many_follow_2 = False
        default nm2_no_cabin = False
        default nm2_can_make_sense = False
        default nm2_disjointed = False
        menu:
            extend ""

            "{i}• (Explore) ''I think they're all... wrong.''{/i}" if nm2_wrong == False:
                $ nm2_wrong = True
                $ nm2_count += 1
                voice "audio/voices/ch3/clarity/broken/3.flac"
                broken "Of course we're wrong.\n"
                voice "audio/voices/ch3/clarity/smitten/3.flac"
                smitten "She's the only thing that's right.\n"
                voice "audio/voices/ch3/clarity/narrator/5.flac"
                n "Yes, obviously they're all wrong. What are you going to do about it?\n"
                jump nightmare_2_menu

            "{i}• (Explore) ''Getting back to His earlier question, how many times have you all been here?''{/i}" if nm2_count != 0 and nm2_how_many == False:
                jump nm2_how_many_join

            "{i}• (Explore) ''That's a good question. How many times have you all been here?''{/i}" if nm2_count == 0 and nm2_how_many == False:
                label nm2_how_many_join:
                    $ nm2_how_many = True
                    $ nm2_count += 1
                    voice "audio/voices/ch3/clarity/skeptic/2.flac"
                    skeptic "Many many many many times.\n"
                    voice "audio/voices/ch3/clarity/paranoid/3.flac"
                    paranoid "It feels like we've been here forever, but it also feels like we've barely been here at all.\n"
                    voice "audio/voices/ch3/clarity/broken/3a.flac"
                    broken "It doesn't matter.\n"
                    voice "audio/voices/ch3/clarity/opportunist/2.flac"
                    opportunist "Yes. We just have to do what she says. And then everything will be fine.\n"
                    voice "audio/voices/ch3/clarity/narrator/6.flac"
                    n "It won't.\n"
                    voice "audio/voices/ch3/clarity/opportunist/3.flac"
                    opportunist "It will be for us. She said so.\n"
                    voice "audio/voices/ch3/clarity/narrator/7.flac"
                    n "You're part of everything. If things aren't fine for everything, they won't be fine for you.\n"
                    voice "audio/voices/ch3/clarity/contrarian/2.flac"
                    contrarian "There's no difference between Fine and Not Fine. It just goes on and on.\n"
                    jump nightmare_2_menu

            "{i}• (Explore) ''But that doesn't make sense. I only remember being here twice before this, and some of you don't seem to remember being here at all. Was I here those other times? Did someone else make the decisions?''{/i}" if nm2_how_many and nm2_how_many_follow == False:
                $ nm2_how_many_follow = True
                $ nm2_count += 1
                voice "audio/voices/ch3/clarity/contrarian/3.flac"
                contrarian "What does here even mean, if you really think about it?\n"
                voice "audio/voices/ch3/clarity/stubborn/2a.flac"
                stubborn "Shut up. You were here.\n"
                voice "audio/voices/ch3/clarity/broken/4.flac"
                broken "Every single time.\n"
                voice "audio/voices/ch3/clarity/opportunist/4.flac"
                opportunist "You did your best, really. There's just a pecking order.\n"
                voice "audio/voices/ch3/clarity/smitten/4.flac"
                smitten "And our cruel and beautiful goddess sits atop it, right where she's always belonged.\n"
                voice "audio/voices/ch3/clarity/hero/3.flac"
                hero "You're lucky. What I would give to be able to forget.\n"
                voice "audio/voices/ch3/clarity/cold/2.flac"
                cold "I've tried to keep them numb, but they're all too soft. A shame, really.\n"
                jump nightmare_2_menu

            "{i}• (Explore) ''If I don't remember what I did, then it couldn't have been me that did it.''{/i}" if nm2_how_many_follow_2 == False and nm2_how_many_follow:
                $ nm2_how_many_follow_2 = True
                $ nm2_count += 1
                voice "audio/voices/ch3/clarity/narrator/8.flac"
                n "Don't think about that too hard. All it will do is weaken your resolve and make it that much harder for you to slay her.\n"
                voice "audio/voices/ch3/clarity/broken/5.flac"
                broken "Maybe you're shattered in your own way.\n"
                voice "audio/voices/ch3/clarity/skeptic/3.flac"
                skeptic "Are you your memories, or are you the one perceiving the present moment?\n"
                voice "audio/voices/ch3/clarity/stubborn/3a.flac"
                stubborn "Ugh. Here you go 'philosophizing' again. It never goes anywhere.\n"
                #stubborn "Ugh. You've spent too much time navel-gazing. It never goes anywhere.\n"
                voice "audio/voices/ch3/clarity/contrarian/4.flac"
                contrarian "Yes, this is far from the first time you've asked us about consciousness. 'Who am I?'; 'What am I?'; 'What {b}is{/b} 'I?'' Who even cares?\n"
                voice "audio/voices/ch3/clarity/opportunist/5.flac"
                opportunist "They're good questions. Great questions, even. But they don't have any answers.\n"
                voice "audio/voices/ch3/clarity/hunted/2a.flac"
                hunted "And they all just end in quivering torment.\n"
                voice "audio/voices/ch3/clarity/cheated/2.flac"
                cheated "It doesn't matter what we do. Because we always find her. And if we don't find her, she always finds us.\n"
                voice "audio/voices/ch3/clarity/broken/6.flac"
                broken "And then she smashes us into smaller pieces.\n"
                voice "audio/voices/ch3/clarity/cold/3.flac"
                cold "If you all just stopped feeling we could have been done with this ages ago.\n"
                voice "audio/voices/ch3/clarity/narrator/9.flac"
                n "Your thoughts are far too scattered to reign back in. Your only option is to silence them.\n"
                jump nightmare_2_menu

            "{i}• (Explore) ''What if we don't go to the cabin?''{/i}" if nm2_no_cabin == False:
                $ nm2_no_cabin = True
                $ nm2_count += 1
                voice "audio/voices/ch3/clarity/contrarian/5.flac"
                contrarian "We've tried that.\n"
                voice "audio/voices/ch3/clarity/hero/4.flac"
                hero "It doesn't work.\n"
                voice "audio/voices/ch3/clarity/smitten/5.flac"
                smitten "Our heart's always brought us back to her.\n"
                voice "audio/voices/ch3/clarity/cheated/3.flac"
                cheated "The deck is stacked.\n"
                voice "audio/voices/ch3/clarity/hunted/3.flac"
                hunted "So many paths and they're all circles.\n"
                jump nightmare_2_menu

            "{i}• (Explore) ''Can you make sense of them?''{/i}" if nm2_can_make_sense == False:
                $ nm2_can_make_sense = True
                voice "audio/voices/ch3/clarity/narrator/10.flac"
                n "There's nothing worth making sense of. They're clearly all traumatized.\n"
                voice "audio/voices/ch3/clarity/skeptic/4.flac"
                skeptic "And yet you aren't. We break apart and you stay the same.\n"
                voice "audio/voices/ch3/clarity/cheated/4.flac"
                cheated "Yeah, what's your secret? Why can you break the rules when we can't?\n"
                jump nightmare_2_menu

            "{i}• (Explore) ''I feel so disjointed. I don't know if I can pull this off. I don't know if I can slay her.''{/i}" if nm2_disjointed == False:
                $ nm2_disjointed = True
                voice "audio/voices/ch3/clarity/narrator/11.flac"
                n "I don't care how you feel. You have to slay her. You have to pull yourself together. You have to snap out of it.\n"
                voice "audio/voices/ch3/clarity/cold/4.flac"
                cold "You're lucky you haven't been stuck here like the rest of them. There's no other way to keep going. You either need to forget, or you need to stop feeling much of anything. They can't do either.\n"
                voice "audio/voices/ch3/clarity/opportunist/6.flac"
                opportunist "He's not wrong. He's the only smart one left, if you ask me.\n"
                voice "audio/voices/ch3/clarity/broken/7.flac"
                broken "He's worse than her.\n"
                jump nightmare_2_menu

            "{i}• [[Proceed to the cabin.]{/i}":
                jump nightmare_2_cabin_arrive

            "{i}• ''The only way out is to do nothing. So nothing I will do.'' [[Stay where you are.]{/i}" if nightmare_2_wait_attempt == False:
                $ nightmare_2_wait_attempt = True
                voice "audio/voices/ch3/clarity/narrator/12.flac"
                n "You do... nothing? You can't just do nothing. You have to do something.\n"
                voice "audio/voices/ch3/clarity/hero/5.flac"
                hero "That's... a new one. Huh. Do you think it'll work?\n"
                voice "audio/voices/ch3/clarity/broken/8.flac"
                broken "No. Nothing ever works.\n"
                voice "audio/voices/ch3/clarity/opportunist/7.flac"
                opportunist "Boo. You're the worst one.\n"
                voice "audio/voices/ch3/clarity/skeptic/5.flac"
                skeptic "He's not the one who got us into this mess.\n"
                voice "audio/voices/ch3/clarity/paranoid/4.flac"
                paranoid "At least I keep you breathing around her.\n"
                voice "audio/voices/ch3/clarity/opportunist/8.flac"
                opportunist "See? That's why the sad one's the worst. The jumpy one tries.\n"
                voice "audio/voices/ch3/clarity/stubborn/4.flac"
                stubborn "Who cares? All of you just yap about nothing.\n"
                voice "audio/voices/ch3/clarity/opportunist/9.flac"
                opportunist "Now that kind of attitude is why you're in the top half.\n"
                voice "audio/voices/ch3/clarity/stubborn/5.flac"
                stubborn "Great.\n"
                voice "audio/voices/ch3/clarity/opportunist/10.flac"
                opportunist "And that's why you're not {b}the{/b} top.\n"
                voice "audio/voices/ch3/clarity/skeptic/6.flac"
                skeptic "I want to see what nothing does for us. And right now all of you aren't letting nothing happen.\n"
                voice "audio/voices/ch3/clarity/cold/5.flac"
                cold "Hopefully this stuffs all the rest of them some place quiet. You need me, and you need to not have them.\n"
                voice "audio/voices/ch3/clarity/hunted/4.flac"
                hunted "He'll get you killed by himself.\n"
                voice "audio/voices/ch3/clarity/contrarian/6a.flac"
                contrarian "Oh, all of us have gotten all of the rest of us killed at one point or another. That's hardly even a concern now.\n"
                voice "audio/voices/ch3/clarity/narrator/13.flac"
                n "As the little voices bicker amongst themselves, you do your best to stay still in the woods. It is difficult, and the more time you spend waiting, the harder it will be to sharpen your focus when you need it.\n"
                voice "audio/voices/ch3/clarity/smitten/6.flac"
                smitten "I wonder what we look like right now. Are we standing? Sitting? I like to think we have an air of dignity.\n"
                voice "audio/voices/ch3/clarity/narrator/14.flac"
                n "My point exactly.\n"
                menu:
                    extend ""

                    "{i}• [[Proceed to the cabin.]{/i}":
                        jump nightmare_2_cabin_arrive

                    "{i}• [[Continue to do nothing.]{/i}" if mound_can_attempt_flee:
                        if loops_finished >= 2:
                            $ mound_can_attempt_flee = False
                            voice "audio/voices/mound/bonus/flee.flac"
                            mound "You have already committed to my completion. You cannot go further astray.\n"
                            jump nightmare_2_menu
                        voice "audio/voices/ch3/clarity/narrator/15a.flac"
                        stop music fadeout 10.0
                        play secondary "audio/_music/mound/The Long Quiet FINAL.ogg" loop fadein 20.0
                        n "Congratulations, you continue to waste everyone's time and do nothing... wait, can you still hear me? Everything is getting fuzzy...\n"
                        show quiet creep1 onlayer inyourface at Position(ypos=1125) with Dissolve(2.0)
                        voice "audio/voices/ch3/clarity/cheated/5.flac"
                        cheated "Ha. It's our turn to flip the table.\n"
                        voice "audio/voices/ch3/clarity/broken/9.flac"
                        broken "This is the end, isn't it?\n"
                        voice "audio/voices/ch3/clarity/paranoid/5.flac"
                        paranoid "Everything is wrong.\n"
                        show quiet creep2 onlayer inyourface at Position(ypos=1125) with Dissolve(2.0)
                        voice "audio/voices/ch3/clarity/hero/6.flac"
                        hero "What is that twisting feeling?\n"
                        voice "audio/voices/ch3/clarity/smitten/7.flac"
                        smitten "We're so small.\n"
                        play music "audio/_music/mound/Oblivion.flac" loop fadein 30.0
                        show quiet creep3 onlayer inyourface at Position(ypos=1125) with Dissolve(2.0)
                        voice "audio/voices/ch3/clarity/hunted/5.flac"
                        hunted "I don't think we're supposed to be here.\n"
                        voice "audio/voices/ch3/clarity/stubborn/6.flac"
                        stubborn "Just another bout of nonsense. Again.\n"
                        voice "audio/voices/ch3/clarity/skeptic/7.flac"
                        skeptic "I can't think anymore.\n"
                        voice "audio/voices/ch3/clarity/contrarian/7.flac"
                        contrarian "Finally. I've just needed to leave for so long.\n"
                        voice "audio/voices/ch3/clarity/cold/6.flac"
                        cold "Hm. I thought I would last without them. I thought I was special...\n"
                        voice "audio/voices/ch3/clarity/opportunist/11.flac"
                        opportunist "Well, it looks like this was a good idea! Something new is happening! Well done! Brilliant, even!\n"
                        voice "audio/voices/ch3/clarity/opportunist/12.flac"
                        opportunist "... right? Guys?\n"
                        hide stars onlayer farback
                        hide back onlayer back
                        hide mid onlayer front
                        hide front onlayer inyourface
                        hide quiet onlayer inyourface
                        show farback quiet onlayer back at Position(ypos=1125)
                        with Dissolve(4.0)
                        jump caught_late_join

label nightmare_2_cabin_arrive:
    $ quick_menu = False
    play audio "audio/one_shot/footsteps_hike_short.flac"
    hide stars onlayer farback
    hide back onlayer back
    hide mid onlayer front
    hide front onlayer inyourface
    show bg black onlayer back at Position(ypos=1125)
    with fade
    voice "audio/voices/ch3/clarity/narrator/16.flac"
    n "You slowly make your way through the umbral forest, bumping against unseen trees as you grasp through the darkness for a way forward.\n"
    $ gallery_clarity.unlock_item(2)
    $ renpy.save_persistent()
    play audio "audio/one_shot/footsteps_hike_short.flac"
    hide bg black onlayer back
    show stars clarity onlayer farback at Position(ypos=1125)
    show bg clarity ext nocabin onlayer back at Position(ypos=1125)
    show mid clarity ext nocabin onlayer front at Position(ypos=1125)
    show mirror cabinext clarity onlayer front at Position(ypos=1125)
    show front clarity ext onlayer inyourface at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    voice "audio/voices/ch3/clarity/narrator/17.flac"
    n "But eventually, you do make it to the cabin, or rather, you make it to the place a cabin should have been. Instead, all you find is an empty hill.\n"
    voice "audio/voices/ch3/clarity/narrator/18.flac"
    show bg clarity ext cabin onlayer back at Position(ypos=1125)
    show mid clarity ext cabin onlayer front at Position(ypos=1125)
    n "No, no. This isn't right. There's a cabin there. There's always supposed to be a cabin there.\n"
    voice "audio/voices/ch3/clarity/hero/7.flac"
    hero "Don't ask him about the mirror.\n"
    voice "audio/voices/ch3/clarity/skeptic/8.flac"
    skeptic "He always says he never sees it.\n"
    voice "audio/voices/ch3/clarity/paranoid/6.flac"
    paranoid "He always lies.\n"
    voice "audio/voices/ch3/clarity/cheated/6.flac"
    cheated "And he always makes it gone.\n"
    #voice "audio/voices/ch3/clarity/smitten/8.flac"
    #smitten "It's exhausting. We must be such a mess, but we never get the chance to fix ourselves. That thing is mocking us.\n"
    voice "audio/voices/ch3/clarity/narrator/19.flac"
    n "Stay focused. You still have a job to do, and it's best not to be distracted by fraying thoughts. There is no mirror. You know that as well as I do.\n"
    voice "audio/voices/ch3/clarity/hunted/6a.flac"
    hunted "She's still here. Buried deep inside the earth.\n"
    voice "audio/voices/ch3/clarity/cold/7a.flac"
    cold "Just walk up the hill. You always give too much space to the others. It's why you always lose.\n"
    label nightmare_2_cabin_arrive_menu:
        default nm2_cabin_explore = False
        menu:
            extend ""

            "{i}• (Explore) ''And what's wrong with giving them space? What if it helps them? What if they need to be heard?''{/i}" if nm2_cabin_explore == False:
                $ nm2_cabin_explore = True
                voice "audio/voices/ch3/clarity/cold/8.flac"
                cold "They've been heard too much. It's why they are the way they are.\n"
                voice "audio/voices/ch3/clarity/narrator/20.flac"
                n "Exactly. They are delusions, and all that catering to them will do is drag you down to their level. You have to keep moving.\n"
                voice "audio/voices/ch3/clarity/hero/8.flac"
                hero "Or you could just give up.\n"
                jump nightmare_2_cabin_arrive_menu

            "{i}• [[Approach the mirror.]{/i}":
                $ gallery_clarity.unlock_item(3)
                $ renpy.save_persistent()
                $ quick_menu = False
                play audio "audio/one_shot/footsteps_hike_short.flac"
                hide stars onlayer farback
                hide bg onlayer back
                hide mid onlayer front
                hide mirror onlayer front
                hide front onlayer inyourface
                show bg black onlayer back at Position(ypos=1125)
                with fade
                voice "audio/voices/ch3/clarity/narrator/21.flac"
                n "You walk up the hill, hesitating just beyond the bounds of 'the cabin.'\n"
                voice "audio/voices/ch3/clarity/skeptic/9.flac"
                hide bg black onlayer back
                show stars clarity onlayer farback at Position(ypos=1125)
                show midground cabin clarity onlayer back at Position(ypos=1125)
                show mirror cabin clarity onlayer back at Position(ypos=1125)
                show fore cabin clarity onlayer front at Position(ypos=1125)
                with fade
                if persistent.quick_menu:
                    $ quick_menu = True
                skeptic "The cabin that isn't there.\n"
                voice "audio/voices/ch3/clarity/smitten/9.flac"
                smitten "You've got to clean the mirror, haven't you? You've got to see what's in it.\n"
                voice "audio/voices/ch3/clarity/stubborn/7.flac"
                stubborn "Smash it to pieces.\n"
                voice "audio/voices/ch3/clarity/broken/10.flac"
                broken "She's on the other side, and we have to let her out. It's the only way we can be free.\n"
                voice "audio/voices/ch3/clarity/paranoid/7.flac"
                paranoid "It's the only way we can have our thoughts back.\n"
                voice "audio/voices/ch3/clarity/contrarian/8.flac"
                contrarian "Just go around it.\n"
                voice "audio/voices/ch3/clarity/cold/9.flac"
                cold "Just do something. It doesn't matter what.\n"
                #voice "audio/voices/ch3/clarity/opportunist/13.flac"
                #opportunist "Exactly. I'm sure that whatever you settle on, it'll be the best possible decision you could have made.\n"
                $ current_run_mirror_touched = True
                menu:
                    extend ""

                    "{i}• [[Proceed.]{/i}":
                        voice "audio/voices/ch3/clarity/narrator/22.flac"
                        n "... proceed? Proceed to where? I'm afraid you're going to have to be a little more specific.\n"
                        if nightmare_2_wait_attempt:
                            voice "audio/voices/ch3/clarity/hero/9.flac"
                            hero "That's another new one. How do you keep coming up with new things? I hope this works better than nothing did.\n"
                        else:
                            voice "audio/voices/ch3/clarity/hero/10.flac"
                            hero "That's a new one. Do you think it'll work?\n"
                        voice "audio/voices/ch3/clarity/opportunist/14.flac"
                        opportunist "Of course it'll work. He always makes the best decisions. It's why he gets to make them!\n"
                        hide mirror onlayer back
                        voice "audio/voices/ch3/clarity/cold/10.flac"
                        cold "And it already has worked. It's gone, don't you see?\n"
                        voice "audio/voices/ch3/clarity/broken/11.flac"
                        broken "We're one step closer to her.\n"
                        #voice "audio/voices/ch3/clarity/narrator/23.flac"
                        #n "You step forward and into 'the cabin.'\n"
                        voice "audio/voices/ch3/clarity/narrator/24a.flac"
                        n "The interior of 'the cabin' is much the same as the exterior of 'the cabin,' a dull, fuzzy, dreamlike nothing. It's empty and isolating, but there's just enough vague shape and unknown texture to suggest the structure therein, wrong and unsettling as it may be.\n"
                        voice "audio/voices/ch3/clarity/narrator/25.flac"
                        n "The only object of note is a pristine blade buried in the dirt floor, a hint of its shining edge teasing through the sediment.\n"
                        voice "audio/voices/ch3/clarity/narrator/26.flac"
                        n "The blade is your implement. You'll need it if you're going to do this right.\n"
                        voice "audio/voices/ch3/clarity/cold/11.flac"
                        stop secondary fadeout 1.0
                        cold "Take it. It's the only way forward.\n"
                        $ config.menu_include_disabled = True
                        menu:
                            extend ""

                            "{i}• [[Take the blade.]{/i}":
                                label nightmare_2_blade_join:
                                    hide stars onlayer farback
                                    hide midground onlayer back
                                    hide fore onlayer front
                                    show hole clarity1 onlayer farback at Position(ypos=1125)
                                    with dissolve
                                    $ renpy.pause(1.0)
                                    play secondary "audio/final/Nightmare_Falling_1_Loop.ogg" loop
                                    hide hole onlayer farback
                                    show bg hole clarity onlayer farback at Position(ypos=1125)
                                    voice "audio/voices/ch3/clarity/narrator/27.flac"
                                    n "You reach down to take the blade, but as you do, the ground beneath it shifts, the weapon sinking deep into the earth.\n"
                                    voice "audio/voices/ch3/clarity/narrator/28.flac"
                                    n "You lean over the hole and gaze into the abyss. It is so very deep.\n"

                            "{i}• [[It's the only way forward.]{/i}" if false_choice:
                                jump nightmare_2_blade_join

                            "{i}• [[You've already tried everything else.]{/i}" if false_choice:
                                jump nightmare_2_blade_join

                            "{i}• [[Don't you remember?]{/i}" if false_choice:
                                jump nightmare_2_blade_join

                            "{i}• [[You have to take the blade.]{/i}":
                                jump nightmare_2_blade_join

    play audio "audio/final/Assorted_Static_4.flac"
    show masked clarity hole emerge1 onlayer back at Position(ypos=1125)
    voice "audio/voices/ch3/clarity/narrator/29.flac"
    n "Deep in the bowels of the earth, you see something staring back at you. It fills you with dread.\n"
    voice "audio/voices/ch3/clarity/hero/11.flac"
    hero "It's her.\n"
    voice "audio/voices/ch3/clarity/paranoid/8.flac"
    paranoid "She's watching us. She never stops watching us.\n"

    if nightmare_run_attempt:
        voice "audio/voices/ch3/clarity/princess/1a.flac"
        sp "There you are! My toy has finally come to finish his job.\n"
    else:
        voice "audio/voices/ch3/clarity/princess/2.flac"
        sp "You really are a coward!\n"

    play audio "audio/final/Assorted_Static_9.flac"
    hide masked onlayer back
    show clarity hole emerge2 onlayer farback at Position(ypos=1125)
    show masked clarity hole emerge2 onlayer inyourface at Position(ypos=1125)
    voice "audio/voices/ch3/clarity/narrator/30.flac"
    n "With every word she speaks, the Princess in the pit blinks closer.\n"

    play audio "audio/final/Assorted_Static_2.flac"
    show clarity hole emerge3 onlayer farback
    show masked clarity hole emerge3 onlayer inyourface
    if nightmare_run_attempt:
        voice "audio/voices/ch3/clarity/princess/3.flac"
        sp "You dragged this out for so much longer than you had to!\n"
    else:
        voice "audio/voices/ch3/clarity/princess/4.flac"
        sp "I was joking when I said that way back when. You know that, right?\n"

    play audio "audio/final/Assorted_Static_11.flac"
    show clarity hole emerge4 onlayer farback at Position(ypos=1125)
    show masked clarity hole emerge4 onlayer inyourface at Position(ypos=1125)
    voice "audio/voices/ch3/clarity/narrator/31.flac"
    n "And closer.\n"

    if nightmare_run_attempt:
        voice "audio/voices/ch3/clarity/princess/5.flac"
        sp "But it was always just a matter a time.\n"
    else:
        voice "audio/voices/ch3/clarity/princess/6.flac"
        sp "I was having some fun! And I guess I wanted to see if I could melt you.\n"

    play audio "audio/final/Assorted_Static_1.flac"
    show clarity hole emerge5 onlayer farback
    show masked clarity hole emerge5 onlayer inyourface
    voice "audio/voices/ch3/clarity/narrator/32.flac"
    n "And closer.\n"

    if nightmare_run_attempt:
        voice "audio/voices/ch3/clarity/princess/7.flac"
        sp "You were gonna have to stop running eventually.\n"
    else:
        voice "audio/voices/ch3/clarity/princess/8.flac"
        sp "Watching over me forever? That was so brave!\n"

    play audio "audio/final/Assorted_Static_9.flac"
    show clarity hole emerge6 onlayer farback
    show masked clarity hole emerge6 onlayer inyourface
    voice "audio/voices/ch3/clarity/narrator/33.flac"
    n "And closer.\n"

    if nightmare_run_attempt:
        voice "audio/voices/ch3/clarity/princess/9.flac"
        sp "Everything stops running eventually.\n"
    else:
        voice "audio/voices/ch3/clarity/princess/10.flac"
        sp "But forever is so so long, and time erodes everything.\n"

    voice "audio/voices/ch3/clarity/princess/11.flac"
    sp "Except for me!\n"
    voice "audio/voices/ch3/clarity/princess/12.flac"
    sp "I've already taken your will and you're not getting it back.\n"
    play audio "audio/final/Assorted_Static_10.flac"
    hide clarity onlayer farback
    hide masked onlayer inyourface
    show clarity emerge hand offer onlayer farback at Position(ypos=1125)
    show masked clarity emerge hand offer onlayer front at Position(ypos=1125)
    voice "audio/voices/ch3/clarity/princess/13.flac"
    sp "All that's left is for you to take my hand, and let. Me. Out.\n"
    voice "audio/voices/ch3/clarity/princess/14.flac"
    sp "It'll be so much fun! You and me, together, exploring the world and spreading fear wherever we go! Well, mostly just me. But you'll get to be there too!\n"
    #voice "audio/voices/ch3/clarity/princess/15.flac"
    #sp "A trinket that gets to stay with me all the time, right by my side.\n"
    voice "audio/voices/ch3/clarity/princess/16.flac"
    sp "A witness.\n"
    voice "audio/voices/ch3/clarity/princess/17.flac"
    sp "I can even make you a little cage if you want! Gilded and everything!\n"
    voice "audio/voices/ch3/clarity/princess/18a.flac"
    sp "Now don't pause. Don't try to resist. I've already molded you into what I need, and you lost your power so long ago, don't bother working yourself into a frenzy to get it back.\n"
    voice "audio/voices/ch3/clarity/narrator/34a.flac"
    n "Do something! Do anything that isn't taking her hand!\n"
    #voice "audio/voices/ch3/clarity/hero/12a.flac"
    #hero "What are we supposed to do? She took our weapon.\n"

    ## CUT for brevity

    #if nightmare_run_attempt:
    #    voice "audio/voices/ch3/clarity/cold/12.flac"
    #    cold "This really was a lost cause, wasn't it? You sealed our fate when you ran away. Fear is the real killer. Oh well.\n"
    #else:
    #    voice "audio/voices/ch3/clarity/cold/13.flac"
    #    cold "This really was a lost cause, wasn't it? You sealed our fate when you refused to kill her.\n"
    #    voice "audio/voices/ch3/clarity/hunted/7.flac"
    #    hunted "Kill or be killed.\n"
    #    voice "audio/voices/ch3/clarity/cold/14.flac"
    #    cold "Yes, I suppose you're right. Oh well.\n"
    #voice "audio/voices/ch3/clarity/paranoid/9.flac"
    #paranoid "There's no paralysis anymore. Is it because we've already given her what she wants?\n"
    $ gallery_clarity.unlock_item(4)
    $ gallery_clarity.unlock_item(5)
    $ gallery_clarity.unlock_item(6)
    $ gallery_clarity.unlock_item(7)
    $ gallery_clarity.unlock_item(8)
    $ gallery_clarity.unlock_item(9)
    $ renpy.save_persistent()
    $ config.menu_include_disabled = True
    menu:
        extend ""

        "{i}• [[You're just an object.]{/i}" if false_choice:
            jump nightmare_2_hand_join

        "{i}• [[A tool.]{/i}" if false_choice:
            jump nightmare_2_hand_join

        "{i}• [[You once were something else, a long time ago.]{/i}" if false_choice:
            jump nightmare_2_hand_join

        "{i}• [[But was that something you, or is it just a dull and jaded memory?]{/i}" if false_choice:
            jump nightmare_2_hand_join

        "{i}• [[There is no other ending here.]{/i}" if false_choice:
            jump nightmare_2_hand_join

        "{i}• [[Just take her hand, and set her free.]{/i}":
            label nightmare_2_hand_join:
                $ gallery_clarity.unlock_item(10)
                stop secondary fadeout 1.0
                $ config.menu_include_disabled = False
                play audio "audio/final/Assorted_ForcefullyBreakingGlass_3.flac"
                #play audio "audio/final/Nightmare_StrokeFeather_2.flac"
                hide masked onlayer front
                hide clarity onlayer farback
                show clarity hole grabhand anim onlayer farback at Position(ypos=1125)
                with dissolve
                voice "audio/voices/ch3/clarity/narrator/35.flac"
                n "You extend your hand to hers. For all her past cruelties, the moment feels gentle, tender even. I can't believe you just made me say that. I hate you.\n"
                voice "audio/voices/ch3/clarity/narrator/36.flac"
                hide clarity onlayer farback
                hide clarity onlayer inyourface
                hide bg onlayer farback
                show stars clarity yank onlayer farback at Position(ypos=1125)
                show bg clarity yank onlayer back at Position(ypos=1125)
                show fore clarity yank onlayer front at Position(ypos=1125)
                with Dissolve(2.0)
                n "The motion is difficult at first, as if something still resists your efforts, but then that resistance gives way, and it's over.\n"
                voice "audio/voices/ch3/clarity/princess/19.flac"
                hide stars onlayer farback
                hide bg onlayer back
                hide fore onlayer back
                show stars clarity crawl onlayer farback at Position(ypos=1125)
                show bg clarity crawl onlayer back at Position(ypos=1125)
                show clarity crawl onlayer back at Position(ypos=1125)
                show fore clarity crawl onlayer front at Position(ypos=1125)
                with Dissolve(2.0)
                sp "{i}Ahhhh.{/i}\n"
                #n "The Princess breathes a deep sigh of relief as you pull her from the pit. The motion is difficult at first, as if something still resists your efforts, but then that resistance gives way, and it's over.\n"
                $ gallery_clarity.unlock_item(11)
                $ renpy.save_persistent()
                stop music fadeout 10.0
                play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 20.0
                voice "audio/voices/ch3/clarity/princess/20.flac"
                hide stars onlayer farback
                show stars clarity finale onlayer farback
                show bg clarity finale onlayer back
                show clarity finale onlayer back
                show fore clarity finale onlayer front
                show quiet creep1 onlayer front at Position(ypos=1125)
                with Dissolve(1.5)
                sp "And that's the end! I wonder what we're going to do next.\n"
                voice "audio/voices/ch3/clarity/princess/21a.flac"
                hide fore onlayer front
                hide clarity onlayer back
                show quiet creep2 onlayer front
                show clarity finale doubt onlayer inyourface at Position(ypos=1125)
                with Dissolve(2.0)
                sp "I didn't think I'd be so... tired.\n"
                truth "The Princess, exhausted, slumps.\n"
                voice "audio/voices/ch3/clarity/princess/22a.flac"
                show quiet creep3 onlayer front
                show clarity finale tired onlayer inyourface
                with dissolve
                sp "Why is it so cold?\n"
                play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                show arms clarity quiet1 onlayer front at Position(ypos=1125)
                show clarity quiet onlayer inyourface
                with Dissolve(1.0)
                $ renpy.pause(0.25)
                hide arms onlayer front
                show arms clarity quiet2 onlayer front
                with Dissolve(1.0)
                $ renpy.pause(0.25)
                hide arms onlayer front
                show arms clarity quiet3 onlayer front
                hide clarity onlayer inyourface
                with Dissolve(0.5)
                $ renpy.pause(0.25)
                hide arms onlayer front
                show arms clarity quiet4 onlayer inyourface
                with Dissolve(0.25)
                $ renpy.pause(0.25)
                hide arms onlayer inyourface
                with Dissolve(0.25)
                $ renpy.pause(0.25)
                hide stars onlayer farback
                hide bg onlayer back
                hide quiet onlayer front
                show farback quiet onlayer farback at Position(ypos=1125)
                with Dissolve(4.0)
                show mirror quiet distant onlayer back at Position(ypos=1125)
                if loops_finished != 0:
                    truthside "You do not get the chance to respond, nor will you ever. It's time to leave. Memory returns.\n"
                else:
                    truthside "You do not have an opportunity to respond. Something has taken her away, and it's left something else in her place.\n"
                voice "audio/voices/ch3/clarity/broken/12.flac"
                broken "She's gone.\n"
                voice "audio/voices/ch3/clarity/skeptic/10.flac"
                skeptic "Yeah. I can finally think again. Almost.\n"
                voice "audio/voices/ch3/clarity/hero/13.flac"
                hero "That mirror's back...\n"
                voice "audio/voices/ch3/clarity/contrarian/9.flac"
                contrarian "What does that mean for us?\n"
                voice "audio/voices/ch3/clarity/cheated/7.flac"
                cheated "I'm sure it'll be whisked away just like her.\n"
                voice "audio/voices/ch3/clarity/hunted/8.flac"
                hunted "Maybe it won't be gone. Things are different now, aren't they?\n"
                voice "audio/voices/ch3/clarity/paranoid/10.flac"
                paranoid "It doesn't seem like there's much else to do here.\n"
                voice "audio/voices/ch3/clarity/stubborn/8.flac"
                stubborn "Finally. We can smash it.\n"
                voice "audio/voices/ch3/clarity/cold/15.flac"
                cold "Oh will you stop with the smashing?\n"
                voice "audio/voices/ch3/clarity/smitten/10.flac"
                smitten "What do we say, boys? One last vain attempt to look at ourselves?\n"
                voice "audio/voices/ch3/clarity/hero/14.flac"
                hero "Yeah. I think I'd like that.\n"
                voice "audio/voices/ch3/clarity/opportunist/15.flac"
                opportunist "Seems we've got a majority. All that's left is to give it a look.\n"
                # END
                $ princess_free += 1
                jump mirror_nightmare_2






return
