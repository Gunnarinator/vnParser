label adversary_2_start:

    # starting things up

    stop music
    stop sound
    stop secondary
    $ default_mouse = "default"
    $ blade_held = False
    $ current_loop = 2
    $ quick_menu = False
    $ config.menu_include_disabled = False
    $ current_princess = "needle"

    play sound "audio/looping/uncomfortable ambiance heightened.ogg" loop fadein 1.0
    scene chapter needle with fade
    show text _("{color=#FFFFFF00}Chapter Three. The Eye of the Needle.{/color}") at Position(ypos=850)
    $ renpy.pause(4.0)
    scene bg black with fade
    hide text
    play music "audio/_music/ch3/needle/The Eye of the Needle INTRO.flac"
    queue music "audio/_music/ch3/needle/The Eye of the Needle INTRO.flac" loop
    scene farback path needle onlayer farback at Position(ypos=1125)
    show bg path needle onlayer back at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True

    $ gallery_needle.unlock_gallery()
    $ gallery_needle.unlock_item(1)
    $ renpy.save_persistent()

    voice "audio/voices/ch3/eye/narrator/1.flac"
    n "You're on a path in the woods—\n{w=1.52}{nw}"
    show screen disableclick(0.5)

    if trait_hunted:
        voice "audio/voices/ch3/eye/stubborn/1.flac"
        stubborn "If you weren't so damned afraid of what she'd do to you, we wouldn't have died back there.\n"
        voice "audio/voices/ch3/eye/hunted/1.flac"
        hunted "Fear is good. Fear keeps us alive. We died because you didn't have enough of it.\n"
        voice "audio/voices/ch3/eye/stubborn/1a.flac"
        stubborn "So what? You'd have us cower in a corner?\n"
        voice "audio/voices/ch3/eye/hunted/2.flac"
        hunted "No, but that place suits her better than it suits us. She's big, we can't hope to find holes and openings down there. We need more room if we're going to survive.\n"
        voice "audio/voices/ch3/eye/narrator/2.flac"
        n "Are you suggesting luring her into the woods? Do you have any idea how dangerous that would be? If you lose sight of her, if she manages to slip away, that's it. Game over. For everyone. Yourself included.\n"

    else:
        voice "audio/voices/ch3/eye/stubborn/2.flac"
        stubborn "If you weren't so damned focused on freeing her, we wouldn't have died back there.\n"
        voice "audio/voices/ch3/eye/skeptic/1.flac"
        skeptic "You're strong, but you're bullheaded. This isn't a fight. It's a puzzle. She's stronger than us, but we can use that to our advantage.\n"
        voice "audio/voices/ch3/eye/stubborn/3.flac"
        stubborn "I hate puzzles.\n"
        #voice "audio/voices/ch3/eye/skeptic/2.flac"
        #skeptic "Yeah, of course you do.\n"
        voice "audio/voices/ch3/eye/hero/1a.flac"
        hero "I've never done a puzzle myself, but anything that doesn't get us beaten to death is good in my book. What do you have in mind?\n"
        voice "audio/voices/ch3/eye/skeptic/3a.flac"
        skeptic "Same thing as last time, only we'll be smarter about it. We're getting her out of there. After that, we're seeing what happens.\n"
        voice "audio/voices/ch3/eye/narrator/3.flac"
        n "Are you insane? Do you have any idea how dangerous that would be? If she gets out of here, that's it. Game over. For everyone. Yourself included.\n"

    voice "audio/voices/ch3/eye/hero/2a.flac"
    hero "Are you not challenging us on all the... looping? Have you known about it the whole time? Are you the same one we've been talking to since the beginning?\n"
    #if trait_skeptic:
    #    voice "audio/voices/ch3/eye/skeptic/4.flac"
    #    skeptic "Why the lies? Why have you been playing the fool? What good could it possibly accomplish?\n"
    #else:
    #    voice "audio/voices/ch3/eye/hunted/3.flac"
    #    hunted "So you've been able to see all of this. You can remember. Why keep it a secret?\n"

    voice "audio/voices/ch3/eye/narrator/4.flac"
    n "Sorry to disappoint what I'm sure must feel like a grand revelation, but that's not what's going on here. We've never met.\n"
    if trait_skeptic:
        voice "audio/voices/ch3/eye/skeptic/5a.flac"
        skeptic "Enlighten me, then.\n"
        voice "audio/voices/ch3/eye/narrator/5.flac"
        n "I have no memory of meeting you, but you've clearly seen things you weren't supposed to have seen. You'd only be saying the things you've been saying if you'd already been here.\n"
    #else:
        #voice "audio/voices/ch3/eye/hunted/4.flac"
        #hunted "Then what is going on?\n"
        #voice "audio/voices/ch3/eye/narrator/6.flac"
        #n "'What's going on' is that you'd only be saying the things you've been saying if you'd already been here, and if you'd already seen things you weren't supposed to have seen.\n"

    if trait_skeptic:
        voice "audio/voices/ch3/eye/skeptic/6.flac"
        skeptic "Mhm. So where does that leave us?\n"
        voice "audio/voices/ch3/eye/narrator/7.flac"
        n "It leaves us exactly where we started, and where I'm sure you've already been before. The Princess, left unhindered, will bring about the end of world. You have to put a stop to her, and the only way to do that is to slay her.\n"
        #voice "audio/voices/ch3/eye/skeptic/7.flac"
        #skeptic "But we didn't stop her last time. We died. Yet here we are, in a world un-ended. A different world un-ended, to be sure, but there's still solid ground beneath our feet.\n"
        #voice "audio/voices/ch3/eye/stubborn/4.flac"
        #stubborn "What the hell are you going on about?\n"
        #voice "audio/voices/ch3/eye/skeptic/8.flac"
        #skeptic "Even if He's isn't lying, reality clearly continues to be real. So I want to see what happens when she leaves. I think we all need to see the truth.\n"
        #voice "audio/voices/ch3/eye/narrator/8.flac"
        #n "You absolutely do not need to see that. I've already told you the truth, and the only thing to see after she leaves is The End. Of everything. It's not worth it.\n"
        #voice "audio/voices/ch3/eye/skeptic/9.flac"
        #skeptic "The truth is always worth it. If we're going to get to the bottom of things, we need to have a method. We need to isolate a variable, and right now her interaction with the outside world is the most interesting variable there is. It's one of the only things we haven't seen.\n"
        #voice "audio/voices/ch3/eye/narrator/9.flac"
        #n "As much as I appreciate your dedication to scientific rigor, your core assumptions are all wrong. This isn't a puzzle, and this isn't an experiment. It's a do-or-die situation with apocalyptic consequences.\n"
        #if adversary_1_forest_share_loop_insist:
        #    voice "audio/voices/ch3/eye/narrator/10.flac"
        #    n "And might I remind you that while it may seem consequence free to you, that does not make it consequence free to me, or to the people I'm trying to protect.\n"
        #    voice "audio/voices/ch3/eye/hero/3a.flac"
        #    hero "We know. You told us last time.\n"
        #    voice "audio/voices/ch3/eye/narrator/11.flac"
        #    n "And how am I supposed to know that? {i}Sigh.{/i} It doesn't matter, because it's a point that bears repeating.\n"
        #    voice "audio/voices/ch3/eye/narrator/12.flac"
        #    n "As does the point that, for all you know, The End isn't really consequence free to you.\n"
        #else:
        #    voice "audio/voices/ch3/eye/narrator/13.flac"
        #    n "And might I remind you that while it may seem consequence free to you, that does not make it consequence free to me, or to the people I'm trying to protect. And for all you know, The End isn't really consequence free to you.\n"
        #voice "audio/voices/ch3/eye/narrator/14.flac"
        #n "You said yourself that the world is 'different' than what you've already seen. It isn't supposed to be, and if things are changing, they're changing for the worse. It's just how things work here. Treat this like it's your last attempt.\n"
        voice "audio/voices/ch3/eye/stubborn/5.flac"
        stubborn "Screw it! I'm sick of this smug asshole telling us what to do. If you need help busting her out of there, I'm your man.\n"
        voice "audio/voices/ch3/eye/skeptic/10.flac"
        skeptic "Welcome aboard. And if things go bad once we get her out of the cabin, well, at least you'll be able to get that fight you wanted.\n"
        voice "audio/voices/ch3/eye/narrator/15.flac"
        n "The rest of you had better keep those two in check. They're far along the edge of a dangerous path. Don't let them go any further.\n"
    else:
        voice "audio/voices/ch3/eye/hunted/5a.flac"
        hunted "It doesn't matter. We could go in circles forever. I don't like staying still for too long. Let's get to the cabin. See this through.\n"
        voice "audio/voices/ch3/eye/narrator/16.flac"
        n "It's good to know that at least one of you is still capable of reason.\n"
        voice "audio/voices/ch3/eye/hunted/6.flac"
        hunted "We may have the same destination, but we're not the same. You are still an other, and I don't trust you.\n"
        #voice "audio/voices/ch3/eye/narrator/17.flac"
        #n "Well fortunately, you have an entire trip through the woods to reconsider that.\n"
        #voice "audio/voices/ch3/eye/stubborn/6.flac"
        #stubborn "There's nothing to reconsider. We're all for violence here!\n"
        #voice "audio/voices/ch3/eye/hero/4.flac"
        #hero "Are we? I haven't signed off on anything yet.\n"
        #voice "audio/voices/ch3/eye/narrator/18.flac"
        #n "Violence is the answer here, but the method is equally important to the act. You can't let her leave the cabin.\n"
        #voice "audio/voices/ch3/eye/hunted/7.flac"
        #hunted "It's like I said. All just circles. Instinct tells me we need space, and I trust instinct. Nothing else to say. Not for me.\n"


label adversary_2_menu:
    default needle_path_woods_explore = False
    default needle_path_woods_other_explore = False
    menu:
        extend ""

        "{i}• (Explore) We haven't talked enough about how different this place is. I wouldn't even call these woods. It's like her influence has poured out into the world.{/i}" if needle_path_woods_explore == False:
            $ needle_path_woods_explore = True
            voice "audio/voices/ch3/eye/narrator/19.flac"
            n "It's evidence of one of many ticking clocks. You can't let her spread any further.\n"
            if trait_skeptic:
                voice "audio/voices/ch3/eye/skeptic/11a.flac"
                skeptic "But do we know it's her? For all we know, He's in control, pulling the strings to make us too afraid to do anything but slay her.\n"
                voice "audio/voices/ch3/eye/hero/5a.flac"
                hero "For all we know, it could be us making the changes.\n"
                voice "audio/voices/ch3/eye/skeptic/12.flac"
                skeptic "Exactly. And at least as things are now, there's no way for us to know. But the world is clearly not as it seems. We can't trust anything until we learn more.\n"
                voice "audio/voices/ch3/eye/narrator/20.flac"
                n "If you question reality itself, there's not much I can offer in the way of persuasion, but do consider that it probably isn't helpful for anyone to doubt the ground they stand on.\n"
            else:
                voice "audio/voices/ch3/eye/hunted/8.flac"
                hunted "Things are always changing. She changed, the cabin changed, we've changed. Why wouldn't the woods change, too?\n"
                voice "audio/voices/ch3/eye/narrator/21a.flac"
                n "Because they're not supposed to have changed. This is supposed to be a path in the woods. If it's not, it means something's gone horribly wrong.\n"
            jump adversary_2_menu

        "{i}• (Explore) What if I don't agree with the plan? What if I'd rather do something else?{/i}" if needle_path_woods_other_explore == False:
            $ needle_path_woods_other_explore = True
            if trait_skeptic:
                voice "audio/voices/ch3/eye/skeptic/13.flac"
                skeptic "It's up to you in the end, isn't it? It'd be best if you bought in, but there's not a whole lot we can do to stop you if you decide to do something else.\n"
            else:
                voice "audio/voices/ch3/eye/hunted/9.flac"
                hunted "You're the chooser. The best we can do is advise. But we can help, if you let us.\n"
            voice "audio/voices/ch3/eye/narrator/22.flac"
            n "These are just powerless thoughts and opinions. You don't need to let them drag you and the world to ruin.\n"
            jump adversary_2_menu

        "{i}• No matter what happens next, it seems like all our answers are in the cabin. We might as well see this through. [[Proceed to the cabin.]{/i}":
            jump adversary_2_exterior

        "{i}• [[Silently proceed to the cabin.]{/i}":
            jump adversary_2_exterior

        "{i}• I'm done with this. Bye! [[Turn around and leave.]{/i}":
            $ caught_origin_ch3 = True
            $ caught_origin_current = "adversary2"
            voice "audio/voices/ch3/eye/stubborn/7.flac"
            stubborn "Coward! Deserter!\n"
            if trait_skeptic:
                voice "audio/voices/ch3/eye/skeptic/14.flac"
                skeptic "I suppose that's another variable that's worth testing...\n"
            else:
                voice "audio/voices/ch3/eye/hunted/10.flac"
                hunted "Turning our back to her? Could be a mistake...\n"
            voice "audio/voices/ch3/eye/narrator/23.flac"
            play audio "audio/one_shot/footsteps_hike_short.flac"
            $ quick_menu = False
            scene farback path needle onlayer farback at flip, zoom_in
            show bg path needle onlayer back at flip, zoom_in
            with fade
            if persistent.quick_menu:
                $ quick_menu = True
            n "Are you serious?! Fine. You walk away from the the cabin. We'll see how that goes for you.\n"
            jump caught_start

label adversary_2_exterior:

    $ gallery_needle.unlock_item(2)
    $ renpy.save_persistent()
    play audio "audio/one_shot/footsteps_hike_short.flac"

    hide farback onlayer farback
    hide bg onlayer back
    scene bg black
    with fade
    scene farback needle outside onlayer farback at Position(ypos=1125)
    show bg cabin exterior needle onlayer back at Position(ypos=1125)
    show mid cabin exterior needle onlayer front at Position(ypos=1125)
    show fore cabin exterior needle onlayer inyourface at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    voice "audio/voices/ch3/eye/narrator/24.flac"
    n "It isn't long before you find yourself at the end of the path, staring up the hill at the cabin. I hope you've given serious thought to your predicament.\n"
    voice "audio/voices/ch3/eye/hero/6.flac"
    hero "No last advice for us? No words of warning?\n"
    voice "audio/voices/ch3/eye/narrator/25.flac"
    n "From what I gather, you've heard it all before. There's no use screaming into the wind.\n"
    voice "audio/voices/ch3/eye/hero/7a.flac"
    hero "I don't know. Screaming sounds pretty good right about now. I could use a little catharsis.\n"
    if trait_skeptic:
        voice "audio/voices/ch3/eye/skeptic/15.flac"
        skeptic "There'll be time for that later. For now, you know what you have to do.\n"
    else:
        voice "audio/voices/ch3/eye/hunted/11a.flac"
        hunted "Catharsis is for when we're finished. For now, we need to hold it out in front of us, something to chase.\n"
    menu:

        extend ""

        "{i}• [[Proceed into the cabin.]{/i}":
            $ quick_menu = False
            play audio "audio/one_shot/door_bedroom.flac"
            hide farback onlayer farback
            hide bg onlayer back
            hide mid onlayer front
            hide fore onlayer inyourface
            scene bg black
            with fade
            play sound "audio/looping/STP_cave_loop.ogg" loop fadein 1.0
            scene bg cabin needle onlayer back at Position(ypos=1125)
            show mirror cabin needle onlayer back at Position(ypos=1125)
            show knife cabin needle onlayer back at Position(ypos=1125)
            with fade
            if persistent.quick_menu:
                $ quick_menu = True
            jump adversary_2_interior

label adversary_2_interior:

    $ gallery_needle.unlock_item(3)
    $ renpy.save_persistent()
    voice "audio/voices/ch3/eye/narrator/26.flac"
    n "The interior of the cabin is suffocatingly tight, more of a glorified tunnel than a building. Its stone walls squeeze against your sides, leaving you no choice but to press forward. The only furniture of note is an iron altar, jutting out from the wall, a pristine blade perched on its edge.\n"
    voice "audio/voices/ch3/eye/narrator/27.flac"
    n "The blade is your implement. You'll need it if you're going to do this right.\n"
    if trait_hunted:
        voice "audio/voices/ch3/eye/hunted/12.flac"
        hunted "See? We have even less space than before. We need space or she'll kill us, and the only space is out there.\n"
    else:
        if current_run_mirror_comment == False:
            $ adversary_2_mirror_comment = True
            voice "audio/voices/ch3/eye/skeptic/16.flac"
            skeptic "But there's nowhere to go in here. This is just a hallway with a mirror at the end of it.\n"
            voice "audio/voices/ch3/eye/narrator/28.flac"
            n "A mirror? But there isn't a mirror here. There's the iron altar, the blade sitting on the altar, and the door to the basement.\n"
            voice "audio/voices/ch3/eye/hero/8.flac"
            hero "Does he really not see it?\n"
            voice "audio/voices/ch3/eye/skeptic/17.flac"
            skeptic "Or maybe what we see as a mirror, he sees as a door.\n"
            voice "audio/voices/ch3/eye/narrator/29.flac"
            n "It is a door. And before you ask, no, it's not a mirror-shaped door. The object at the end of this room is both door-shaped and a door. There shouldn't be any room for misinterpretation.\n"
            voice "audio/voices/ch3/eye/stubborn/8.flac"
            stubborn "Who cares what it is. It's in our way, we should smash it.\n"
        else:
            voice "audio/voices/ch3/eye/skeptic/18.flac"
            skeptic "Up to you if we want the blade. I think we can goad her out of here without it.\n"
    voice "audio/voices/ch3/eye/stubborn/9.flac"
    stubborn "Take it.\n"
    label adversary_2_interior_menu:
        default adversary_2_blade_taken = False
        default adversary_2_mirror_comment = False
        menu:

            extend ""

            "{i}• (Explore) You never mention the mirror.{/i}" if adversary_2_mirror_comment == False and current_run_mirror_comment:
                jump adversary_2_mirror_join

            "{i}• (Explore) That damn mirror's back.{/i}" if adversary_2_mirror_comment == False and current_run_mirror_comment:
                jump adversary_2_mirror_join

            "{i}• (Explore) But there's no way forward. There's a mirror at the end of the room and that's it.{/i}" if adversary_2_mirror_comment == False:
                label adversary_2_mirror_join:
                    $ adversary_2_mirror_comment = True
                    if current_run_mirror_touched:
                        if trait_skeptic:
                            voice "audio/voices/ch3/eye/skeptic/19.flac"
                            skeptic "It looks that way, sure, but it vanished the last time we interacted with it. Until proven otherwise, we shouldn't assume that it's real.\n"
                            voice "audio/voices/ch3/eye/narrator/30.flac"
                            n "A fair assumption, especially since I can assure you that there is no mirror. The only thing at the end of this room is the door to the basement.\n"
                            voice "audio/voices/ch3/eye/stubborn/10.flac"
                            stubborn "If there's a door on the other side of that thing, let's just smash it.\n"
                            voice "audio/voices/ch3/eye/skeptic/20.flac"
                            skeptic "Let's see if it stays there before we make any rash decisions. But if is it real, we should take a good look at it before we do any smashing.\n"
                        else:
                            voice "audio/voices/ch3/eye/hunted/13.flac"
                            hunted "Maybe it'll go away again.\n"
                            voice "audio/voices/ch3/eye/narrator/31.flac"
                            n "For something to go away, it would have to be there to begin with. And let me assure you, there's no mirror here. The only thing at the end of the room is the door to the basement.\n" id adversary_2_mirror_join_e249efc4
                            voice "audio/voices/ch3/eye/hunted/14.flac"
                            hunted "No use arguing. Mirror or not, we need to be there. The why we pick doesn't matter.\n"
                            voice "audio/voices/ch3/eye/stubborn/11.flac"
                            stubborn "I agree with the freak, let's get a move on already. And worse comes to worst we can smash it.\n"

                    else:
                        if adversary_2_blade_taken:
                            voice "audio/voices/ch3/eye/narrator/32.flac"
                            n "A mirror? But there is no mirror. There's the iron altar and the door to the basement. There's nothing else in here.\n"
                        else:
                            voice "audio/voices/ch3/eye/narrator/33.flac"
                            n "A mirror? But there is no mirror. There's the iron altar, the blade sitting on the altar, and the door to the basement. There's nothing else in here.\n"
                        voice "audio/voices/ch3/eye/hero/9.flac"
                        hero "But there isn't a door.\n"
                        voice "audio/voices/ch3/eye/narrator/34.flac"
                        n "There is.\n"
                        if trait_hunted:
                            voice "audio/voices/ch3/eye/hunted/15.flac"
                            hunted "Circles, circles, all of it circles! There's something for us at the end of the room. The what and the why don't matter until we know them.\n"
                            voice "audio/voices/ch3/eye/stubborn/12.flac"
                            stubborn "I agree with the freak, let's get a move on already. And worse comes to worst we can smash it.\n"
                jump adversary_2_interior_menu


            "{i}• (Explore) [[Take the blade.]{/i}" if adversary_2_blade_taken == False:
                $ adversary_2_blade_taken = True
                $ blade_held = True
                $ default_mouse = "blade"
                voice "audio/voices/ch2/shared/narrator/ch2_share_n_38.flac"
                play audio "audio/one_shot/knife_pickup.flac"
                hide knife onlayer back
                with dissolve
                voice "audio/voices/ch3/eye/narrator/35.flac"
                n "You take the blade from the altar. It would be difficult to slay the Princess and save the world without a weapon.\n"
                if trait_hunted:
                    voice "audio/voices/ch3/eye/hunted/16a.flac"
                    hunted "Good. There's no overcoming her without it. We need every part of us to survive, and that steel claw is as much as part of us as any.\n"
                else:
                    voice "audio/voices/ch3/eye/stubborn/13.flac"
                    stubborn "Good. Wouldn't want to be pushed around without a way to push back. And she likes when we can push back, doesn't she?\n"
                jump adversary_2_interior_menu

            "{i}• [[Approach the mirror.]{/i}":
                if adversary_2_blade_taken == False:
                    if trait_hunted:
                        voice "audio/voices/ch3/eye/hunted/17.flac"
                        hunted "We can try to survive without our steel claw. But you've marked us as easy prey.\n"
                $ quick_menu = False
                play audio "audio/one_shot/footsteps_stone.flac"
                hide knife onlayer back
                hide mirror onlayer back
                hide bg onlayer back
                show door needle close onlayer back at Position(ypos=1125)
                show mirror needle close onlayer back at Position(ypos=1125)
                with fade

                if persistent.quick_menu:
                    $ quick_menu = True
                if adversary_2_mirror_comment:
                    voice "audio/voices/ch3/eye/narrator/36.flac"
                    n "You step forward and approach the door to the basement, hesitating before you open it. As if you don't see it. You're rather committed to the bit, aren't you? The door's right there. It's right in front of you.\n"
                else:
                    voice "audio/voices/ch3/eye/narrator/37.flac"
                    n "You step forward and approach the door to the basement, hesitating before you open it. As if you don't see it. You do see it, right?\n"
                    voice "audio/voices/ch3/eye/stubborn/14.flac"
                    stubborn "All we see is a damned mirror.\n"
                if current_run_mirror_touched:
                    voice "audio/voices/ch3/eye/hero/10.flac"
                    hero "This really is just like last time...\n"
                    if trait_hunted:
                        voice "audio/voices/ch3/eye/hunted/18.flac"
                        hunted "It smells of nothing. Yet it's still there.\n"
                    else:
                        voice "audio/voices/ch3/eye/skeptic/21.flac"
                        skeptic "Can you really not see the mirror, or is pretending it doesn't exist another one of your 'rules?'\n"
                        voice "audio/voices/ch3/eye/narrator/38.flac"
                        n "There isn't a mirror.\n"
                        voice "audio/voices/ch3/eye/hero/11.flac"
                        hero "Is it a rule to say there isn't a mirror when there's clearly one right there? Because if it is, it's not a very good one.\n"
                        voice "audio/voices/ch3/eye/skeptic/22.flac"
                        skeptic "I'm inclined to agree. But we don't know how things work here, do we?\n"
                        voice "audio/voices/ch3/eye/stubborn/15.flac"
                        stubborn "Just smash it already.\n"
                else:
                    voice "audio/voices/ch3/eye/hero/12.flac"
                    hero "It's a bit grimy. Why don't we wipe it clean?\n"
                menu:
                    extend ""

                    "{i}• [[Wipe the mirror clean.]{/i}":
                        voice "audio/voices/ch3/eye/narrator/39.flac"
                        hide mirror onlayer back
                        $ renpy.pause(0.5)
                        voice sustain
                        play audio "audio/one_shot/door_stone.flac"
                        show door needle close open onlayer back
                        with dissolve
                        n "You reach forward and drag your hand across the door leading to the basement. As if on command, it slowly slides open, scraping against the floor as it reveals the dim path ahead.\n"

                    "{i}• [[Smash it.]{/i}":
                        voice "audio/voices/ch3/eye/narrator/40.flac"
                        play audio "audio/one_shot/thump_6.flac"
                        hide mirror onlayer back
                        $ renpy.pause(0.5)
                        voice sustain
                        play audio "audio/one_shot/door_stone.flac"
                        show door needle close open onlayer back
                        with dissolve
                        n "You bring your fist crashing down against the door leading to the basement. It swings open, scraping against the floor as it reveals the dim path ahead.\n"

                if current_run_mirror_touched:
                    voice "audio/voices/ch3/eye/hero/13.flac"
                    hero "Why am I not surprised...\n"
                    voice "audio/voices/ch3/eye/stubborn/16.flac"
                    stubborn "It was in our way and now it's not. That's all that matters.\n"
                $ current_run_mirror_comment = True
                $ quick_menu = False
                #voice "audio/voices/ch3/eye/narrator/41.flac"
                play audio "audio/one_shot/footsteps_stone.flac"
                hide door onlayer back
                with fade
                #n "You step forward into the darkness.\n"
                jump adversary_2_stairs

label adversary_2_stairs:

    scene bg upstairs needle onlayer back at Position(ypos=1125)
    show fore upstairs needle onlayer front at Position(ypos=1125)
    show player upstairs needle onlayer front at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    voice "audio/voices/ch3/eye/narrator/41.flac"
    n "Before you is what may as well be a sheer cliff-face. There are enough footholds that you'll be able to clamber your way to the bottom, but it will require careful effort.\n"
    voice "audio/voices/ch3/eye/narrator/42.flac"
    n "The air hissing up from below is warm and wet, like the breath of an enemy locked in close-quarters. If the Princess lives here, slaying her is probably doing her a favor.\n"
    voice "audio/voices/ch3/eye/narrator/43.flac"
    n "Her voice, bold and fierce and impatient, echoes from the chamber below.\n"
    voice "audio/voices/ch3/eye/princess/1a.flac"
    spmid "Do you have more fight in you than last time? That was such a disappointing show. I know you can do better than that.\n"
    if trait_hunted:
        voice "audio/voices/ch3/eye/hunted/19.flac"
        hunted "Goad her. Rile her up. If she's angry, she'll make mistakes.\n"
    elif trait_skeptic:
        voice "audio/voices/ch3/eye/skeptic/23.flac"
        skeptic "She hasn't changed as much as she did the time before. She still wants a fight, which means we still know her. We can use that to our advantage.\n"
    label adversary_2_stairs_menu:
        default adversary_2_stairs_menu_explore = False
        default adversary_2_stairs_can_comment = False
        default adversary_2_stairs_commented = False
        if adversary_2_stairs_menu_explore and adversary_2_stairs_can_comment and adversary_2_stairs_commented == False:
            $ adversary_2_stairs_commented = True
            if trait_hunted:
                voice "audio/voices/ch3/eye/hunted/20a.flac"
                hunted "We need to get closer. She needs to see us to give chase.\n"
            else:
                voice "audio/voices/ch3/eye/stubborn/17.flac"
                stubborn "This is getting us nowhere.\n"
                voice "audio/voices/ch3/eye/skeptic/24.flac"
                skeptic "Agreed. We'll have to go down there.\n"
        menu:

            extend ""

            "{i}• (Explore) ''If you want a fight then how about you come and get one?''{/i}" if adversary_2_stairs_menu_explore == False:
                $ adversary_2_stairs_menu_explore = True
                voice "audio/voices/ch3/eye/princess/2a.flac"
                spmid "That's not how this works. I'm all chained up, remember? How about you come down here and fight me.\n"
                if adversary_1_upstairs_flag or adversary_1_chains_broken:
                    voice "audio/voices/ch3/eye/hero/14.flac"
                    hero "Those chains were nothing to her last time...\n"
                    if trait_skeptic:
                        voice "audio/voices/ch3/eye/skeptic/25.flac"
                        skeptic "They're a part of the setup. Like our blade. Just a formality, but one that needs its own introduction, a whole show of the Princess, or whatever she is, being locked away for her alleged crimes.\n"
                    else:
                        voice "audio/voices/ch3/eye/hunted/21.flac"
                        hunted "And they'll be nothing to her this time. But we need to show ourselves first. To make her boil over.\n"
                else:
                    if trait_skeptic:
                        voice "audio/voices/ch3/eye/skeptic/26.flac"
                        skeptic "Don't worry about the chains. I've got a plan.\n"
                    else:
                        voice "audio/voices/ch3/eye/hunted/22.flac"
                        hunted "We'll need to show ourselves. Make her boil over and forget her metal bindings.\n"
                if trait_hunted:
                    voice "audio/voices/ch3/eye/stubborn/18.flac"
                    stubborn "Fine by me.\n"
                else:
                    voice "audio/voices/ch3/eye/stubborn/19.flac"
                    stubborn "Yeah. We'll just have to get her to break 'em.\n"
                jump adversary_2_stairs_menu

            "{i}• (Explore) ''I know you can get out of there on your own.''{/i}" if (adversary_1_upstairs_flag or adversary_1_chains_broken) and adversary_2_stairs_menu_explore == False:
                $ adversary_2_stairs_menu_explore = True
                $ adversary_2_stairs_can_comment = True
                voice "audio/voices/ch3/eye/princess/3a.flac"
                spmid "But that wouldn't be fun. I don't want to be a monster chasing you down. I want to face you head-on. I want an equal. It's so much better that way.\n"
                jump adversary_2_stairs_menu

            "{i}• (Explore) ''Are you sure you still want to fight?''{/i}" if adversary_2_stairs_menu_explore == False:
                $ adversary_2_stairs_menu_explore = True
                $ adversary_2_stairs_can_comment = True
                voice "audio/voices/ch3/eye/princess/4.flac"
                spmid "Dead certain. Everything inside of me screams for it.\n"
                jump adversary_2_stairs_menu

            "{i}• [[Continue to the basement landing.]{/i}":
                $ quick_menu = False
                voice "audio/voices/ch3/eye/narrator/44.flac"
                play audio "audio/one_shot/footsteps_hike_short.flac"
                hide player onlayer front
                hide fore onlayer front
                hide bg onlayer back
                scene bg downstairs needle onlayer back at Position(ypos=1125)
                show fore downstairs needle onlayer front at Position(ypos=1125)
                show player downstairs needle onlayer front at Position(ypos=1125)
                with fade
                if persistent.quick_menu:
                    $ quick_menu = True
                n "You've nowhere to go but down. You start the difficult journey, gripping the stone, lowering yourself foot by gruelling foot. But soon, there is solid ground beneath you.\n"
                if trait_skeptic:
                    voice "audio/voices/ch3/eye/skeptic/27.flac"
                    skeptic "We'd best remember how to get back up. The last thing we want is to be stuck between a wall and a raging devil.\n"
                else:
                    voice "audio/voices/ch3/eye/hunted/23.flac"
                    hunted "Remember every crack and crevice. We'll need to be faster than her.\n"
                jump adversary_2_basement_arrive

label adversary_2_basement_arrive:

    $ gallery_needle.unlock_item(4)
    $ renpy.save_persistent()
    voice "audio/voices/ch3/eye/narrator/45.flac"
    $ quick_menu = False
    play audio "audio/one_shot/footsteps_hike_short.flac"
    hide player onlayer front
    hide fore onlayer front
    hide bg onlayer back
    scene bg black
    with fade
    show bg needle d basement onlayer back at Position(ypos=1125)
    show needle d neutral onlayer back at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    n "You turn to face what lies at the end of the narrow tunnel. The Princess, imposing and tightly-muscled, grins back at you from the darkness.\n"
    if adversary_2_blade_taken == False:
        voice "audio/voices/ch3/eye/narrator/46.flac"
        show needle d droop onlayer back
        with dissolve
        n "Her face droops.\n"
        if adversary_1_cabin_blade_taken:
            voice "audio/voices/ch3/eye/princess/5a.flac"
            show needle d droop talk onlayer back
            with dissolve
            sp "There you are. But this time you don't even have that little knife. Do you think this is a joke?\n"
        else:
            voice "audio/voices/ch3/eye/princess/6a.flac"
            show needle d droop talk onlayer back
            with dissolve
            sp "There you are. But still no little knife. Do you think this is a joke?\n"
        voice "audio/voices/ch3/eye/princess/7.flac"
        show needle d tsundere onlayer back
        with dissolve
        sp "Do you need me to break those fragile bones again to remind you how serious this is?\n"
        if trait_skeptic:
            voice "audio/voices/ch3/eye/skeptic/28.flac"
            show needle d tsundere onlayer back
            with dissolve
            skeptic "Good. You don't even have to goad her. She's doing it all herself. Let her break those chains, and then run. Lead her out of here. She'll chase us without a second thought.\n"
            voice "audio/voices/ch3/eye/narrator/47.flac"
            n "You know what? I should have tried to intervene earlier, because I can't let you do that, I won't—\n{w=4.46}{nw}"
            show screen disableclick(0.5)
            voice "audio/voices/ch3/eye/stubborn/20.flac"
            stubborn "Tough shit. We're the ones in control here.\n"
            voice "audio/voices/ch3/eye/narrator/48.flac"
            n "{i}Grumbling noises.{/i}\n"
            voice "audio/voices/ch3/eye/stubborn/21.flac"
            stubborn "Yeah, doesn't feel nice to be yanked around against your will, does it?\n"
        else:
            voice "audio/voices/ch3/eye/hunted/24.flac"
            show needle d tsundere onlayer back
            with dissolve
            hunted "She's bubbling hot with rage. We can't get close if we want to live. But we'll be able to draw her out of here. She's hungry for us.\n"
            voice "audio/voices/ch3/eye/narrator/49.flac"
            n "I know I said this earlier, but I really have to stress how thin of a razor's edge you're on right now.\n"
            voice "audio/voices/ch3/eye/hero/15.flac"
            hero "We know.\n"
            voice "audio/voices/ch3/eye/hunted/25.flac"
            hunted "The only way out is through the eye of the needle.\n"
            voice "audio/voices/ch3/eye/stubborn/22.flac"
            stubborn "And we're going to win.\n"
            voice "audio/voices/ch3/eye/hunted/26.flac"
            hunted "We'll need the steel claw. Grab it as we leave.\n"
        jump adversary_2_basement_loose

    else:
        voice "audio/voices/ch3/eye/narrator/50.flac"
        show needle d grin onlayer back
        with dissolve
        n "Her face widens into a broad grin.\n"
        voice "audio/voices/ch3/eye/princess/8.flac"
        show needle d ready talk onlayer back
        with dissolve
        sp "There you are, knife in hand. How thrilling. Attack me, bleed me, twist the blade in my flesh. Break your bones against my body. I want a real challenge this time.\n"
        if trait_hunted:
            voice "audio/voices/ch3/eye/hunted/27.flac"
            show needle d ready onlayer back
            with dissolve
            hunted "We can't get that close. She'll kill us in the tight space, steel claw or not. Make her come to us. Stand beyond her chains and let her become frenzied. She'll break them, then we run.\n"
        else:
            voice "audio/voices/ch3/eye/skeptic/29.flac"
            show needle d ready onlayer back
            with dissolve
            skeptic "If we're trying to break her out, I doubt she'll come willingly. We'll have to use ourselves as bait.\n"
        voice "audio/voices/ch3/eye/hero/16.flac"
        hero "I really don't like the sound of this.\n"
        if trait_hunted:
            voice "audio/voices/ch3/eye/hunted/28.flac"
            hunted "It's the only way we live.\n"
        else:
            voice "audio/voices/ch3/eye/skeptic/30.flac"
            skeptic "It's the only way to get us both out. And we need to see what happens when she leaves the cabin.\n"
            voice "audio/voices/ch3/eye/narrator/51.flac"
            n "You know what? I should have tried to intervene earlier, because I can't let you do that, I won't—\n{w=4.2}{nw}"
            show screen disableclick(0.5)
            voice "audio/voices/ch3/eye/stubborn/20.flac"
            stubborn "Tough shit. We're the ones in control here.\n"
            voice "audio/voices/ch3/eye/narrator/48.flac"
            n "{i}Grumbling noises.{/i}\n"
            voice "audio/voices/ch3/eye/stubborn/21.flac"
            stubborn "Yeah, doesn't feel nice to be yanked around against your will, does it?\n"
        voice "audio/voices/ch3/eye/princess/9.flac"
        show needle d neutral talk onlayer back
        with dissolve
        sp "Well? What are you waiting for? If we're gonna do this right, you can't be scared. You need to want this as much as I do.\n"
        voice "audio/voices/ch3/eye/princess/10.flac"
        show needle d ready talk onlayer back
        with dissolve
        sp "So go on, make the first move. Don't keep me waiting!\n"
        show needle d neutral onlayer back
        with dissolve
        label adversary_2_basement_talk_menu:
            menu:
                extend ""

                "{i}• (Explore) ''Let's talk a bit first. We can always fight when we're done, but I have questions. I want to know what happened after you killed me.''{/i}":
                    voice "audio/voices/ch3/eye/princess/11.flac"
                    show needle d droop talk onlayer back
                    with dissolve
                    sp "We've talked plenty! I'm sick of talking. I'm sick of waiting!\n"
                    voice "audio/voices/ch3/eye/princess/12.flac"
                    show needle d tsundere talk onlayer back
                    with dissolve
                    sp "I'm sick of you standing just out of reach and teasing me with a fight you won't let me have!\n"
                    voice "audio/voices/ch3/eye/princess/13.flac"
                    show needle d neutral talk onlayer back
                    with dissolve
                    sp "You disappointed me last time, so you don't get to choose what happens next.\n"
                    jump adversary_2_basement_loose

                "{i}• (Explore) ''Not down here. If you want me, you'll have to come and get me.''{/i}":
                    label adversary_2_basement_join:
                        voice "audio/voices/ch3/eye/narrator/52.flac"
                        show needle d droop onlayer back
                        with dissolve
                        n "The Princess scoffs.\n"
                        voice "audio/voices/ch3/eye/princess/14.flac"
                        show needle d droop talk onlayer back
                        with dissolve
                        sp "Oh, you're up to something tricky, aren't you.\n"
                        voice "audio/voices/ch3/eye/princess/15.flac"
                        show needle d tsundere talk onlayer back
                        with dissolve
                        sp "You're teasing me with what I want. But I'm sick of waiting.\n"
                        voice "audio/voices/ch3/eye/princess/16.flac"
                        show needle d neutral talk onlayer back
                        with dissolve
                        sp "I'm not going to let you give me another bad fight. I'm going to get what I want!\n"
                    jump adversary_2_basement_loose

                "{i}• (Explore) ''If you want a good fight, if you {i}really{/i} want to see me at my best, we need somewhere with more space.''{/i}":
                    jump adversary_2_basement_join

                "{i}• (Explore) ''Why don't you want to be free? Why do you insist on fighting me to the death down here in the dark?''{/i}":
                    voice "audio/voices/ch3/eye/princess/17.flac"
                    show needle d droop talk onlayer back
                    with dissolve
                    sp "This again?! What does 'free' even mean? 'Here' and 'there', none of that matters. I'm always in a body. I'm always in one place.\n"
                    voice "audio/voices/ch3/eye/princess/18.flac"
                    show needle d serious talk onlayer back
                    with dissolve
                    sp "Why do you act like you know me better than I know myself?\n"
                    voice "audio/voices/ch3/eye/princess/19.flac"
                    show needle d tsundere talk onlayer back
                    with dissolve
                    sp "I had what I wanted, I had something perfect and it ended. And now that it's gone you keep just... agh! Dangling it in front of me!\n"
                    voice "audio/voices/ch3/eye/princess/20.flac"
                    show needle d droop talk onlayer back
                    with dissolve
                    sp "It's more than teasing, it's cruel! It's cowardly! It's selfish!\n"
                    voice "audio/voices/ch3/eye/princess/21.flac"
                    show needle d neutral talk onlayer back
                    with dissolve
                    sp "I know what I want. And I'm sick of waiting.\n"
                    jump adversary_2_basement_loose

                "{i}• (Explore) ''I'm not fighting you.''{/i}":
                    jump adversary_2_basement_join

                "{i}• [[Step closer, stopping just outside her chains.]{/i}":
                    voice "audio/voices/ch3/eye/narrator/53.flac"
                    play audio "audio/one_shot/footsteps_hike_short.flac"
                    show bg needle d basement onlayer back at big_zoom
                    show needle d neutral onlayer back at big_zoom
                    with dissolve
                    n "You step forward, stopping just outside the reach of her chains.\n"
                    jump adversary_2_basement_join

                "{i}• [[Slay the Princess.]{/i}" if blade_held:
                    voice "audio/voices/ch3/eye/stubborn/23.flac"
                    stubborn "Change of plans, boys!\n" id adversary_2_basement_join_a320bd3e
                    if trait_hunted:
                        voice "audio/voices/ch3/eye/hunted/29.flac"
                        hunted "Impatient! This is her home, not ours. You're going to let her kill us.\n"
                    elif trait_skeptic:
                        voice "audio/voices/ch3/eye/skeptic/31.flac"
                        skeptic "I thought we were on the same page! I can't believe you'd give up the game so easy.\n"
                    voice "audio/voices/ch3/eye/narrator/54.flac"
                    play audio "audio/one_shot/footstep_run_medium.flac"
                    show bg needle d basement onlayer back at big_zoom
                    show needle d grin onlayer back at big_zoom
                    with dissolve
                    n "You charge headlong into the Princess, blade flashing in the dim light of the basement.\n"
                    voice "audio/voices/ch3/eye/princess/22a.flac"
                    hide knife onlayer front
                    scene bg needle d basement fight onlayer back at Position(ypos=1125)
                    show needle d basement fight1 onlayer back at Position(ypos=1125)
                    with Dissolve(1.0)
                    sp "Yes yes yes yes yes! Finally! You get it!\n"
                    voice "audio/voices/ch3/eye/narrator/55.flac"
                    $ default_mouse = "blood"
                    play secondary "audio/final/Adversary_HandThroughChest_1.flac"
                    play audio "audio/final/knife_slash_delay.flac"
                    hide bg onlayer back
                    hide needle onlayer back
                    show farback needle d basement montage onlayer farback at Position(ypos=1125)
                    show bg needle basement montage onlayer back at Position(ypos=1125)
                    with dissolve
                    n "For a moment, the scales feel balanced, each of you inflicting debilitating wounds on the other, striking in a dizzying synchronicity.\n"
                    play audio "audio/final/Adversary_ABackAndForth_1.flac"
                    voice "audio/voices/ch3/eye/narrator/56.flac"
                    show quiet creep1 onlayer back at Position(ypos=1125)
                    show mid needle basement montage onlayer front at Position(ypos=1125)
                    with Dissolve(1.0)
                    n "But it isn't long before they tip in her favor. The cuts and bruises you've inflicted seem little more than superficial, barely so much as slowing her down as she continues her onslaught.\n"
                    stop sound fadeout 20.0
                    stop secondary fadeout 20.0
                    stop tertiary fadeout 20.0
                    stop music fadeout 20.0
                    stop music2 fadeout 20.0
                    stop music3 fadeout 20.0
                    stop music4 fadeout 20.0
                    play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 20.0
                    voice "audio/voices/ch3/eye/narrator/57.flac"
                    hide quiet onlayer back
                    show quiet creep2 onlayer front at Position(ypos=1125)
                    show fore needle basement montage onlayer inyourface at Position(ypos=1125)
                    with Dissolve(1.0)
                    n "You, in contrast, are finding it harder to stand as your body gradually becomes less responsive, less powerful, less stable. You can tell she's trying to make it last, but all it would take is one meaningful strike. The coup-de-grace.\n"
                    $ gallery_needle.unlock_item(5)
                    $ gallery_needle.unlock_item(6)
                    $ renpy.save_persistent()
                    voice "audio/voices/ch3/eye/princess/23a.flac"
                    show quiet creep3 onlayer front
                    with Dissolve(1.0)
                    sp "This was good. But you could have been so much better. I'm... beyond you now.\n"
                    voice "audio/voices/ch3/eye/hero/17.flac"
                    play audio "audio/final/den_emerge.flac"
                    hide fore onlayer inyourface
                    show needle unga bunga final onlayer inyourface at Position(ypos=1125)
                    with Dissolve(1.0)
                    hero "Here it comes. I'll see you all on the other side.\n"
                    hide bg onlayer back
                    hide mid onlayer front
                    show needle basement quiet1 onlayer inyourface at Position(ypos=1125)
                    with Dissolve(1.0)
                    $ renpy.pause(0.125)
                    play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                    show arms needle basement1 onlayer front at Position(ypos=1125)
                    with Dissolve(1.0)
                    show arms needle basement2 onlayer front
                    show needle basement quiet2 onlayer inyourface
                    with Dissolve(1.0)
                    $ renpy.pause(0.125)
                    hide needle onlayer inyourface
                    show arms needle basement3 onlayer front
                    with Dissolve(1.0)
                    $ renpy.pause(0.125)
                    show arms needle basement4 onlayer front
                    with Dissolve(0.5)
                    $ renpy.pause(0.125)
                    hide arms onlayer front
                    with Dissolve(0.5)
                    $ renpy.pause(0.125)
                    $ blade_held = False
                    $ default_mouse = "default"
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
                        truth "But the other side doesn't come. Nor will it ever. It's time for you to leave. Memory returns.\n"
                    else:
                        truth "But the other side doesn't come. Something has taken her away, and it's left something else in her place.\n"
                    $ adversary_2_end = "fight_fail"
                    $ princess_kept += 1
                    $ current_princess = "needle"
                    jump mirror_start


label adversary_2_basement_loose:

    $ gallery_needle.unlock_item(7)
    $ renpy.save_persistent()
    voice "audio/voices/ch3/eye/narrator/58.flac"
    play secondary "audio/final/Adversary_ChainSTressBreaking_2.flac"
    play audio "audio/final/Beast_ChainsFastDrag_1.flac"
    show needle d charge onlayer back at Position(ypos=1125)
    with dissolve
    $ renpy.pause(1.0)
    voice sustain
    play secondary "audio/final/fury_walk_short.flac"
    hide needle onlayer back
    show bg needle d basement onlayer back at shaketiny, Position(ypos=1125)
    show needle d charge2 onlayer front at shaketiny, Position(ypos=1125)
    with Dissolve(2.0)
    n "Bloody desire in her eyes, the Princess rushes forward, ignoring her chains as they bend and snap.\n"
    if trait_hunted:
        voice "audio/voices/ch3/eye/hunted/30.flac"
        hunted "Run.\n"
    else:
        voice "audio/voices/ch3/eye/hero/18.flac"
        hero "Okay, she's taken the bait, now let's get out of here!\n"

    $ quick_menu = False
    voice "audio/voices/ch3/eye/narrator/59.flac"
    play audio "audio/one_shot/footstep_run_medium.flac"
    hide needle onlayer front
    hide bg onlayer back
    with fade
    voice sustain
    scene bg downstairs needle onlayer back at Position(ypos=1125)
    show fore downstairs needle onlayer front at Position(ypos=1125)
    show player downstairs needle onlayer front at Position(ypos=1125)
    show needle d cliff onlayer back at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    n "Without hesitation, you turn back the way you came and scramble up the ledge towards the tunnel entrance.\n"
    $ gallery_needle.unlock_item(8)
    $ renpy.save_persistent()
    voice "audio/voices/ch3/eye/narrator/60.flac"
    play audio "audio/final/Adversary_HoleBeingPunchesRock_1.flac"
    hide bg onlayer back
    hide fore onlayer front
    hide player onlayer front
    hide needle onlayer back
    show bg cg needle cliff onlayer farback at shakeshort, Position(ypos=1125)
    show cg needle cliff onlayer front at shakeshort, Position(ypos=1125)
    with Dissolve(1.0)
    n "As you near the top, hands desperately clawing at jagged stone, you glance back. The Princess is right on your heels. She doesn't bother to scale the wall as you do, instead digging deep into the rock of the cliff-face with her fingertips in her rabid pursuit.\n"
    voice "audio/voices/ch3/eye/princess/24a.flac"
    show cg needle cliff talk onlayer front
    sp "Anywhere you go, I will follow.\n"
    if trait_skeptic:
        voice "audio/voices/ch3/eye/skeptic/32.flac"
        skeptic "We're planning on it.\n"
    else:
        voice "audio/voices/ch3/eye/hunted/31.flac"
        hunted "Good.\n"

    voice "audio/voices/ch3/eye/narrator/61.flac"
    $ quick_menu = False
    hide bg onlayer farback
    hide cg onlayer front
    scene farback needle cabin reverse onlayer farback at Position(ypos=1125)
    show bg needle cabin reverse onlayer back at Position(ypos=1125)
    if blade_held == False:
        show knife needle reverse onlayer back at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    n "You reach the ledge and hoist yourself up into the tunnel, the cabin door finally in sight, at once within your grasp and infinitely distant.\n"
    voice "audio/voices/ch3/eye/princess/25a.flac"
    play audio "audio/final/Adversary_HoleBeingPunchesRock_1.flac"
    show farback needle cabin reverse onlayer farback at Position(ypos=1125)
    show bg needle cabin reverse onlayer back at Position(ypos=1125)
    if blade_held == False:
        show knife needle reverse onlayer back at Position(ypos=1125)
    with hpunch
    sp "What is all of this for? What's the point? You and I are always going to end in violence, so why bother to run? I know what I am. Why can't you be the same?\n"
    if adversary_2_blade_taken == False:
        if trait_hunted:
            voice "audio/voices/ch3/eye/hunted/32.flac"
            hunted "Steel claw. Now.\n"

        else:
            voice "audio/voices/ch3/eye/stubborn/24.flac"
            stubborn "You sure we don't want a weapon?\n"
            voice "audio/voices/ch3/eye/skeptic/33a.flac"
            skeptic "We don't have time! We just have to get her outside, that's what matters.\n"
            voice "audio/voices/ch3/eye/narrator/62.flac"
            n "You're making a mistake.\n"

        menu:
            extend ""

            "{i}• [[Take the blade.]{/i}" if blade_held == False:
                if trait_hunted:
                    $ blade_held = True
                    $ default_mouse = "blade"
                    play audio "audio/one_shot/knife_pickup.flac"
                    hide knife onlayer back
                    voice "audio/voices/ch3/eye/narrator/63.flac"
                    n "Without missing a step, you grab the blade from the altar.\n"
                    voice "audio/voices/ch3/eye/princess/26.flac"
                    sp "So you do want to fight me. Good.\n"
                    voice "audio/voices/ch3/eye/hero/19.flac"
                    play audio "audio/one_shot/footstep_run_medium.flac"
                    hide farback onlayer farback
                    hide bg onlayer back
                    scene farback needle door stars onlayer back at Position(ypos=1125)
                    show bg needle cabin door onlayer back at Position(ypos=1125)
                    with Dissolve(1.0)
                    hero "We're almost there.\n"
                    voice "audio/voices/ch3/eye/hunted/33.flac"
                    hunted "Don't think about almost. We're there when we're there.\n"
                    voice "audio/voices/ch3/eye/stubborn/32.flac"
                    stubborn "And we'll take the fight with us.\n"
                    jump adversary_2_combat_ending
                else:
                    $ blade_held = True
                    $ default_mouse = "blade"
                    play audio "audio/one_shot/knife_pickup.flac"
                    voice "audio/voices/ch3/eye/narrator/64.flac"
                    play audio "audio/final/fury_walk_short.flac"
                    hide knife onlayer back
                    show farback needle cabin reverse onlayer farback at big_zoom
                    show bg needle cabin reverse onlayer back at big_zoom
                    if blade_held == False:
                        show knife needle reverse onlayer back at big_zoom
                    with hpunch
                    n "You stumble as you reach for the blade. In most circumstances it would mean nothing, but in such a confined space, a lost second was all she needed to catch up to you.\n"
                    voice "audio/voices/ch3/eye/princess/26a.flac"
                    sp "So you do want to fight me. Good.\n"
                    label adversary_upstairs_skeptic_die_2_join:
                        voice "audio/voices/ch3/eye/narrator/65.flac"
                        play audio "audio/final/Nightmare_NeckCrack_1.flac"
                        hide farback onlayer farback
                        hide bg onlayer back
                        hide knife onlayer back
                        hide player onlayer back
                        scene bg needle unga bunga1 onlayer back at shakeshort, Position(ypos=1125)
                        show needle unga bunga1 onlayer front at shakeshort, Position(ypos=1125)
                        with Dissolve(1.0)
                        if blade_held:
                            $ blade_held = False
                            $ default_mouse = "default"
                            play secondary "audio/one_shot/knife_bounce_several.flac"
                        n "Your body pulls taut as her hand wraps around your arm.\n" id adversary_upstairs_skeptic_die_2_join_0535a059
                        voice "audio/voices/ch3/eye/narrator/66.flac"
                        play audio "audio/final/Adversary_BodySMashedAgainstWall_1.flac"
                        hide bg onlayer back
                        hide needle onlayer front
                        scene bg black
                        n "Before you can even try to pull away, she slams you into the wall, your head bouncing dangerously off the hard stone.\n"
                        voice "audio/voices/ch3/eye/hero/20.flac"
                        play audio "audio/one_shot/ear_ring.flac"
                        show bg needle unga bunga2 onlayer back at swayblur, Position(ypos=1125)
                        show needle unga bunga2 onlayer front at swayblur, Position(ypos=1125)
                        with dissolve
                        hero "Shit.\n"
                        voice "audio/voices/ch3/eye/skeptic/34.flac"
                        hide bg onlayer back
                        hide needle onlayer front
                        show bg needle unga bunga2 onlayer back at Position(ypos=1125)
                        show needle unga bunga2 onlayer front at Position(ypos=1125)
                        with Dissolve(1.0)
                        skeptic "We had a plan. We should have stuck to it.\n"
                        if blade_held:
                            voice "audio/voices/ch3/eye/stubborn/26.flac"
                            stubborn "It's fine! We can still take her.\n"
                            voice "audio/voices/ch3/eye/hero/21.flac"
                            hero "How?!\n"
                            voice "audio/voices/ch3/eye/stubborn/27.flac"
                            stubborn "One cut at a time.\n"
                        voice "audio/voices/ch3/eye/princess/27a.flac"
                        show needle unga bunga2 talk onlayer front at Position(ypos=1125)
                        with dissolve
                        sp "Why does this feel so empty? Why does it feel so wrong?\n"
                        voice "audio/voices/ch3/eye/princess/28.flac"
                        stop sound fadeout 20.0
                        stop secondary fadeout 20.0
                        stop tertiary fadeout 20.0
                        play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 20.0
                        stop music fadeout 20.0
                        stop music2 fadeout 20.0
                        stop music3 fadeout 20.0
                        stop music4 fadeout 20.0
                        show quiet creep1 onlayer back at Position(ypos=1125)
                        show needle unga bunga3 talk onlayer front at Position(ypos=1125)
                        with dissolve
                        sp "This isn't how things are supposed to go. This is so cold... and disappointing...\n"
                        $ gallery_needle.unlock_item(15)
                        $ gallery_needle.unlock_item(16)
                        $ gallery_needle.unlock_item(17)
                        $ renpy.save_persistent()
                        voice "audio/voices/ch3/eye/narrator/67.flac"
                        play audio "audio/final/den_emerge.flac"
                        hide quiet onlayer back
                        hide needle onlayer front
                        hide quiet onlayer back
                        show farback needle d basement montage onlayer back at Position(ypos=1125)
                        show quiet creep2 onlayer back at Position(ypos=1125)
                        show needle unga bunga final onlayer front at Position(ypos=1125)
                        with Dissolve(1.0)
                        n "Your body still reeling from the impact, your eyes fall on her fist as it drills towards your skull with lethal intent.\n"
                        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                        show quiet creep3 onlayer back
                        show arms needle unga1 onlayer back at Position(ypos=1125)
                        with Dissolve(1.0)
                        show arms needle unga2 onlayer back
                        show needle unga bunga quiet onlayer front
                        with Dissolve(1.0)
                        $ renpy.pause(0.125)
                        hide needle onlayer front
                        show arms needle unga3 onlayer back
                        with Dissolve(1.0)
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
                            truth "But the impact doesn't come. Nor will it ever. It's time for you to leave. Memory returns.\n"
                        else:
                            truth "But the impact doesn't come. Something has taken her away, and it's left something else in her place.\n"
                        $ adversary_2_end = "flee_fail"
                        $ princess_kept += 1
                        $ princess_deny += 1
                        $ current_princess = "needle"
                        jump mirror_start


            "{i}• [[It's too late. Run for the door.]{/i}" if blade_held == False:
                if trait_hunted:
                    voice "audio/voices/ch3/eye/narrator/68.flac"
                    play secondary "audio/one_shot/footstep_run_medium.flac"
                    play audio "audio/final/fury_walk_short.flac"
                    show farback needle cabin reverse onlayer farback at big_zoom
                    show bg needle cabin reverse onlayer back at big_zoom
                    if blade_held == False:
                        show knife needle reverse onlayer back at big_zoom
                    with hpunch
                    n "You continue towards the door, vulnerable and unarmed.\n"
                    voice "audio/voices/ch3/eye/narrator/69.flac"
                    hide farback onlayer farback
                    hide bg onlayer back
                    hide knife onlayer back
                    scene farback needle door stars onlayer farback at Position(ypos=1125)
                    show bg needle cabin door onlayer back at Position(ypos=1125)
                    show player needle cabin door onlayer back at Position(ypos=1125)
                    with Dissolve(1.0)
                    n "No. I can't let this happen! I can't let her leave with you!\n"
                    voice "audio/voices/ch3/eye/stubborn/28.flac"
                    stubborn "And what are you going to do to stop that?\n"
                    voice "audio/voices/ch3/eye/narrator/70.flac"
                    play audio "audio/one_shot/door_try.flac"
                    scene farback needle door stars onlayer farback at Position(ypos=1125)
                    show bg needle cabin door onlayer back at Position(ypos=1125)
                    show player needle cabin door onlayer back at Position(ypos=1125)
                    with hpunch
                    n "I— I don't know! {i}Er.{/i} You try the door and, oh, what a relief. It's stuck.\n"
                    voice "audio/voices/ch3/eye/stubborn/29.flac"
                    stubborn "Bash it open!\n"
                    voice "audio/voices/ch3/eye/narrator/71.flac"
                    n "Please, you can't!\n"
                    voice "audio/voices/ch3/eye/princess/29.flac"
                    sp "I think you forgot something...\n"
                    voice "audio/voices/ch3/eye/narrator/72.flac"
                    play audio "audio/final/Adversary2_AKnifeThrownChestWall_2.flac"
                    hide player onlayer back
                    scene bg black big onlayer inyourface at Position(ypos=1125)
                    n "You feel the burning pain of something long and sharp driving through your back. It slices its way into your organs, until finally it exits out the other side, sticking into the wood of the door with an echoing thunk.\n"
                    voice "audio/voices/ch3/eye/hero/22a.flac"
                    stop sound fadeout 20.0
                    stop secondary fadeout 20.0
                    stop tertiary fadeout 20.0
                    play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 20.0
                    stop music fadeout 20.0
                    stop music2 fadeout 20.0
                    stop music3 fadeout 20.0
                    stop music4 fadeout 20.0
                    hide bg onlayer inyourface
                    show quiet creep3 onlayer back at Position(ypos=1125)
                    with Dissolve(2.0)
                    hero "She killed us with our own weapon. Great.\n"
                    voice "audio/voices/ch3/eye/hunted/34.flac"
                    hunted "We needed to take it...\n"
                    voice "audio/voices/ch3/eye/stubborn/30.flac"
                    stubborn "We're not dead yet. It's not over 'til we can't get up again!\n"
                    voice "audio/voices/ch3/eye/princess/30.flac"
                    sp "Coward. All of this is so wrong! This isn't how things are supposed to be. This is so cold and disappointing...\n"
                    voice "audio/voices/ch3/eye/narrator/73.flac"
                    play audio "audio/final/den_emerge.flac"
                    hide bg onlayer back
                    hide quiet onlayer back
                    show farback needle d basement montage onlayer back at Position(ypos=1125)
                    show needle unga bunga final onlayer front at Position(ypos=1125)
                    with Dissolve(2.0)
                    n "Your body pinned to the door, you crane your neck to see her final approach. She is enveloped in complete lethality, and there's nothing you can do to stop her.\n"
                    voice "audio/voices/ch3/eye/narrator/74.flac"
                    n "I really didn't want it to have to end like this, but your death in here is better than her freedom.\n"
                    $ gallery_needle.unlock_item(15)
                    $ gallery_needle.unlock_item(16)
                    $ gallery_needle.unlock_item(17)
                    $ renpy.save_persistent()
                    voice "audio/voices/ch3/eye/hero/23.flac"
                    hero "See you all next time.\n"
                    play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                    show quiet creep3 onlayer back
                    show arms needle unga1 onlayer back at Position(ypos=1125)
                    with Dissolve(1.0)
                    show arms needle unga2 onlayer back
                    show needle unga bunga quiet onlayer front
                    with Dissolve(1.0)
                    $ renpy.pause(0.125)
                    hide needle onlayer front
                    show arms needle unga3 onlayer back
                    with Dissolve(1.0)
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
                        truth "But next time doesn't come. Nor will it ever. It's time for you to leave. Memory returns.\n"
                    else:
                        truth "But next time doesn't come. Something has taken her away, and it's left something else in her place.\n"
                    $ adversary_2_end = "flee_fail"
                    $ princess_kept += 1
                    $ princess_deny += 1
                    $ current_princess = "needle"
                    jump mirror_start

                else:
                    label adversary_2_skeptic_freedom_join:
                        voice "audio/voices/ch3/eye/narrator/75.flac"
                        play audio "audio/one_shot/footstep_run_medium.flac"
                        hide farback onlayer farback
                        hide bg onlayer back
                        hide knife onlayer back
                        scene farback needle door stars onlayer farback at Position(ypos=1125)
                        show bg needle cabin door onlayer back at Position(ypos=1125)
                        show player needle cabin door onlayer back at Position(ypos=1125)
                        with Dissolve(1.0)
                        n "You continue to the door. It'd be a real shame if it were stuck.\n"
                        voice "audio/voices/ch3/eye/skeptic/35.flac"
                        skeptic "Don't listen to him.\n"
                        voice "audio/voices/ch3/eye/stubborn/31.flac"
                        stubborn "Locks are nothing, just barrel through.\n"
                        voice "audio/voices/ch3/eye/narrator/76.flac"
                        n "No!\n"
                        menu:
                            extend ""

                            "{i}• [[Free her.]{/i}":
                                jump adversary_2_free_ending

                            "{i}• [[Die.]{/i}":
                                voice "audio/voices/ch3/eye/narrator/77.flac"
                                play audio "audio/one_shot/door_try.flac"
                                scene farback needle door stars onlayer farback at Position(ypos=1125)
                                show bg needle cabin door onlayer back at Position(ypos=1125)
                                show player needle cabin door onlayer back at Position(ypos=1125)
                                with hpunch
                                n "You meekly throw yourself against the locked door, your will to triumph sapped by the burden of knowing what would have happened should you have succeeded. This truly is for the best.\n"
                                jump adversary_upstairs_skeptic_die_2_join




    else:
        if trait_skeptic:
            jump adversary_2_skeptic_freedom_join

        else:
            voice "audio/voices/ch3/eye/princess/31a.flac"
            play audio "audio/final/fury_walk_short.flac"
            show farback needle cabin reverse onlayer farback at big_zoom
            show bg needle cabin reverse onlayer back at big_zoom
            if blade_held == False:
                show knife needle reverse onlayer back at big_zoom
            with hpunch
            sp "Little bird, little bird! Where do you think you're going?\n"
            voice "audio/voices/ch3/eye/hero/24.flac"
            hero "We're almost there.\n"
            voice "audio/voices/ch3/eye/hunted/33.flac"
            hunted "Don't think about almost. We're there when we're there.\n"
            voice "audio/voices/ch3/eye/stubborn/32.flac"
            stubborn "And we'll take the fight with us.\n"
            jump adversary_2_combat_ending


label adversary_2_free_ending:

    default needle_skeptic_free_comment = False
    voice "audio/voices/ch3/eye/narrator/78.flac"
    play secondary "audio/one_shot/door_try.flac"
    play audio "audio/one_shot/tackle.flac"
    stop sound fadeout 2.0
    hide bg onlayer back
    hide farback onlayer farback
    hide farback onlayer back
    hide player onlayer back
    hide knife onlayer back
    scene bg black
    n "Your skin hums tight with adrenaline as you burst through the cabin door and roll onto the grass. You bastard.\n"
    voice "audio/voices/ch3/eye/narrator/79.flac"
    play secondary "audio/final/fury_walk_short.flac"
    scene farback needle outside onlayer farback at shakeshort, Position(ypos=1125)
    show bg needle outside onlayer back at shakeshort, Position(ypos=1125)
    show fore needle outside onlayer front at shakeshort, Position(ypos=1125)
    show needle outside arrive onlayer front at shakeshort, Position(ypos=1125)
    with Dissolve(1.25)
    n "You glance back at the cabin as the Princess, singular in her desire to destroy you, explodes through the doorway. So... this is what the end looks like.\n"
    voice "audio/voices/ch3/eye/princess/32.flac"
    show needle outside confused talk onlayer front
    with dissolve
    sp "What is this place? Where are we? This... doesn't feel right.\n"
    show needle outside confused onlayer front
    menu:
        extend ""

        "{i}• ''It's freedom.''{/i}":
            $ needle_skeptic_free_comment = True
            jump needle_freedom_cont

        "{i}• ''Don't you get it? Everything you've known down there has been a lie. Whatever we find out here is the truth. It's the only way for us to be free.''{/i}":
            $ needle_skeptic_free_comment = True
            jump needle_freedom_cont

        "{i}• ''I don't know. But I was hoping we could find out together.''{/i}":
            jump needle_freedom_cont

        "{i}• ''What do you mean, 'this doesn't feel right?'''{/i}":
            jump needle_freedom_cont

        "{i}• [[Say nothing.]{/i}":
            jump needle_freedom_cont

    label needle_freedom_cont:

        if needle_skeptic_free_comment == False:
            voice "audio/_pristine/voice/needle/princess/1a.flac"
            show needle outside ready talk onlayer front
            with dissolve
            sp "This is just another place. I don't care about places! I only care about you! Is this what you wanted? For me to see this?\n"
        else:
            voice "audio/_pristine/voice/needle/princess/1.flac"
            show needle outside ready talk onlayer front
            with dissolve
            sp "Free? This is just... what is this? This is just another place. I don't care about places! I only care about you! Is this what you wanted? For me to see this?\n"
        voice "audio/_pristine/voice/needle/princess/2.flac"
        show needle outside confident talk onlayer front
        with dissolve
        sp "Fine then! I've seen it! Are you happy? Are you finally going to come back to me? Are we finally going to fight?\n"
        voice "audio/_pristine/voice/extras/narrator/1.flac"
        show needle outside slump onlayer front
        with dissolve
        n "She readies her powerful legs to charge you, but then... she slumps.\n"
        voice "audio/_pristine/voice/needle/princess/3.flac"
        stop sound fadeout 20.0
        stop secondary fadeout 20.0
        stop tertiary fadeout 20.0
        play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 20.0
        stop music fadeout 20.0
        stop music2 fadeout 20.0
        stop music3 fadeout 20.0
        stop music4 fadeout 20.0
        hide needle onlayer front
        show quiet creep1 onlayer front at Position(ypos=1125)
        show needle outside confused talk onlayer front at Position(ypos=1125)
        with Dissolve(0.5)
        sp "But... I don't feel like fighting anymore. I'm... cold. It feels like this is where I'm supposed to be, like stepping out of that door was some driving purpose I've long forgotten, but I don't want to be here. I don't want to be here!\n"
        voice "audio/_pristine/voice/needle/princess/4.flac"
        show quiet creep2 onlayer front
        show needle outside slump onlayer front
        with Dissolve(0.5)
        sp "I'm so... confused.\n"
        $ gallery_needle.unlock_item(14)
        $ renpy.save_persistent()
        voice "audio/_pristine/voice/needle/princess/5.flac"
        show quiet creep3 onlayer front
        show needle outside slump talk onlayer front
        with Dissolve(0.5)
        sp "I'm sorry. It's cold.\n"
        jump adversary_2_freedom_join

label adversary_2_combat_ending:

    voice "audio/voices/ch3/eye/narrator/80.flac"
    play secondary "audio/one_shot/door_try.flac"
    play audio "audio/one_shot/tackle.flac"
    stop sound fadeout 2.0
    hide bg onlayer back
    hide farback onlayer farback
    hide farback onlayer back
    hide player onlayer back
    hide knife onlayer back
    scene bg black
    n "Your skin hums tight with adrenaline as you burst through the cabin door and roll onto the grass.\n"
    voice "audio/voices/ch3/eye/narrator/81.flac"
    play secondary "audio/final/fury_walk_short.flac"
    scene farback needle outside onlayer farback at shakeshort, Position(ypos=1125)
    show bg needle outside onlayer back at shakeshort, Position(ypos=1125)
    show fore needle outside onlayer front at shakeshort, Position(ypos=1125)
    show needle outside arrive onlayer front at shakeshort, Position(ypos=1125)
    with Dissolve(1.25)
    n "You glance back at the cabin as the Princess, singular in her desire to destroy you, explodes through the doorway. You are walking a dangerous path. If you waver once, it's all over, so get it right.\n"
    voice "audio/voices/ch3/eye/princess/33a.flac"
    hide needle onlayer front
    show needle outside ready talk onlayer front at Position(ypos=1125)
    with dissolve
    sp "There's nothing left to slow me down. Do you think this is better for you? Do you think this space gives you an edge? Then show me! Show me that you've been worth all the room you've taken up in my head!\n"
    voice "audio/voices/ch3/eye/stubborn/33.flac"
    show needle outside ready onlayer front
    with dissolve
    stubborn "Do it!\n"
    voice "audio/voices/ch3/eye/hunted/35.flac"
    hunted "Be swift. Strike true. Be where she's not. Let your body move you.\n"
    label adversary_2_combat_ending_menu:
        menu:
            extend ""

            "{i}• ''Are you sure you want to do this? You're free now, and out here I have the upper hand. But we don't have to fight.''{/i}":
                voice "audio/voices/ch3/eye/narrator/82.flac"
                show needle outside scoff onlayer front
                with dissolve
                n "The Princess scoffs.\n"
                voice "audio/voices/ch3/eye/princess/34.flac"
                show needle outside confused talk onlayer front
                with dissolve
                sp "Free? This is just another place, this is just... what is this? Where are we? This... doesn't feel right.\n"
                stop sound fadeout 20.0
                stop secondary fadeout 20.0
                stop tertiary fadeout 20.0
                play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 20.0
                stop music fadeout 20.0
                stop music2 fadeout 20.0
                stop music3 fadeout 20.0
                stop music4 fadeout 20.0
                voice "audio/voices/ch3/eye/princess/35.flac"
                hide needle onlayer front
                show quiet creep1 onlayer front at Position(ypos=1125)
                show needle outside slump onlayer front at Position(ypos=1125)
                with Dissolve(1.0)
                sp "It's... it's cold. Why is it so cold?\n"
                voice "audio/voices/ch3/eye/princess/36.flac"
                show quiet creep1 onlayer front
                show needle outside slump talk onlayer front
                with Dissolve(1.0)
                sp "I feel so... tired.\n"
                label adversary_2_freedom_join:
                    default adversary_2_whisk_silent = False
                    play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                    hide needle onlayer front
                    show arms needle slump1 onlayer front at Position(ypos=1125)
                    show needle outside slump talk onlayer front at Position(ypos=1125)
                    with Dissolve(1.0)
                    show arms needle slump2 onlayer front
                    show needle outside slump quiet onlayer front
                    with Dissolve(1.0)
                    $ renpy.pause(0.125)
                    hide needle onlayer front
                    show arms needle slump3 onlayer front
                    with Dissolve(1.0)
                    $ renpy.pause(0.125)
                    show arms needle slump4 onlayer front
                    with Dissolve(0.5)
                    $ renpy.pause(0.125)
                    hide arms onlayer front
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
                    $ achievement.grant("ACH_ADV_FREE")
                    if loops_finished != 0:
                        truth "You do not get the chance to respond, nor will you ever. It's time to leave. Memory returns.\n"
                    elif adversary_whisk_silent:
                        truth "You do not respond. Something has taken her away, and it's left something else in her place.\n"
                    else:
                        truth "You do not have an opportunity to respond. Something has taken her away, and it's left something else in her place.\n"
                    $ adversary_2_end = "free"
                    $ princess_free += 1
                    $ princess_deny += 1
                    $ current_princess = "needle"
                    jump mirror_start

                        # goes to mirror

                        #if adversary_1_cabin_mirror_ask or adversary_1_cabin_mirror_approached:
                        #    voice "audio/voices/ch3/eye/hero/25.flac"
                        #    hero "It's that mirror again. Why is it here? Why now?!\n"
                        #else:
                        #    voice "audio/voices/ch3/eye/hero/26.flac"
                        #    hero "Is that a... mirror? Why is it here? Why now?!\n"


            "{i}• (Explore) ''You've fallen right into my trap.''{/i}" if trait_hunted:
                voice "audio/voices/ch3/eye/princess/37b.flac"
                show needle outside confident talk onlayer front
                with dissolve
                sp "Oh, we'll see about that! Traps aren't real. The only thing that's real is bloodshed.\n"
                voice "audio/voices/ch3/eye/narrator/83.flac"
                play secondary "audio/final/_needle_run.flac"
                hide farback onlayer farback
                hide bg onlayer back
                hide fore onlayer front
                hide needle onlayer front
                scene farback needle d basement montage onlayer farback at Position(ypos=1125)
                show needle unga bunga final onlayer front at Position(ypos=1125)
                with Dissolve(1.0)
                n "She charges, fully determined to end you in a single move.\n"
                voice "audio/voices/ch3/eye/hunted/36.flac"
                hunted "Left! Now!\n"
                jump adversary_2_combat_finale_join

            "{i}• [[Slay the Princess.]{/i}":
                voice "audio/voices/ch3/eye/narrator/84.flac"
                play audio "audio/one_shot/footstep_run_medium.flac"
                #show farback needle outside onlayer farback
                show bg needle outside onlayer back at big_zoom
                show fore needle outside onlayer front at big_zoom
                show needle outside scoff onlayer front at big_zoom
                with Dissolve(1.0)
                n "You leap from the grass and bound towards the Princess, keeping low.\n"
                voice "audio/voices/ch3/eye/princess/38a.flac"
                show needle outside confident talk onlayer front
                with dissolve
                sp "Charging me head-on? Brave. And foolish.\n"
                voice "audio/voices/ch3/eye/narrator/85.flac"
                show needle outside ready onlayer front
                with dissolve
                n "Her body braces for impact, anticipating the clash.\n"
                voice "audio/voices/ch3/eye/hunted/37.flac"
                hunted "That's where you're both wrong. Left! Now!\n"
                label adversary_2_combat_finale_join:
                    voice "audio/voices/ch3/eye/narrator/86.flac"
                    play audio "audio/final/den_emerge.flac"
                    play secondary "audio/final/needle_delay_stumble.flac"
                    hide farback onlayer farback
                    hide bg onlayer back
                    hide fore onlayer front
                    hide needle onlayer front
                    hide bg onlayer farback
                    scene farback needle d basement montage onlayer farback at Position(ypos=1125)
                    show panel1 needle outside montage1 onlayer back at Position(ypos=1125)
                    show panel2 needle1 onlayer front at Position(ypos=1125)
                    with Dissolve(1.0)
                    n "As the Princess strikes, your body swerves to the left. She overextends, stumbling as her balance shifts unexpectedly.\n"
                    voice "audio/voices/ch3/eye/hunted/38.flac"
                    hunted "Strike!\n"
                    $ default_mouse = "blood"
                    voice "audio/voices/ch3/eye/narrator/87a.flac"
                    play audio "audio/final/Tower_KnifeBlow_3.flac"
                    play secondary "audio/final/needle_punch_delay.flac"
                    if persistent.flickering:
                        hide panel2 onlayer front
                        hide panel1 onlayer back
                        scene bg needle fight interstitial2 onlayer farback at Position(ypos=1125)
                        show needle outside fight interstitial1 onlayer front at Position(ypos=1125)
                        show player needle outside fight interstitial 1 onlayer inyourface at Position(ypos=1125)
                        with flash
                    else:
                        hide panel2 onlayer front
                        hide panel1 onlayer back
                        scene bg needle fight interstitial2 onlayer farback at Position(ypos=1125)
                        show needle outside fight interstitial1 onlayer front at Position(ypos=1125)
                        show player needle outside fight interstitial 1 onlayer inyourface at Position(ypos=1125)
                        with fade
                    n "Before you can finish the thought, you lash out, the blade slicing through her leg. She turns to swing again.\n"
                    voice "audio/voices/ch3/eye/hunted/39.flac"
                    hunted "Right!\n"
                    voice "audio/voices/ch3/eye/narrator/88.flac"

                    $ quick_menu = False
                    hide player onlayer inyourface
                    hide panel1 onlayer back
                    hide panel2 onlayer front
                    hide farback onlayer farback
                    hide bg onlayer farback
                    hide needle onlayer front
                    scene bg black
                    play audio "audio/final/Tower_GiantPunch_NEW_2.flac"
                    play audio "audio/one_shot/knife_slash.flac"
                    $ renpy.pause(0.5)

                    voice sustain
                    scene bg needle fight interstitial2 onlayer farback at Position(ypos=1125)
                    show needle outside fight interstitial2 onlayer front at Position(ypos=1125)
                    with Dissolve(1.0)
                    if persistent.quick_menu:
                        $ quick_menu = True
                    n "You move out of the way, but this time, it's not quite as clean. You can feel a bruise already blooming where her elbow crashed into flesh.\n"
                    voice "audio/voices/ch3/eye/stubborn/34.flac"
                    stubborn "It's nothing. A scratch.\n"
                    voice "audio/voices/ch3/eye/narrator/89.flac"
                    n "Yes, it could be worse, and you managed to gift her another cut in return. I'll be damned.\n"
                    voice "audio/voices/ch3/eye/hero/27.flac"
                    hero "We're actually going to pull this off, aren't we?\n"
                    voice "audio/voices/ch3/eye/narrator/90.flac"
                    n "You just might. But don't let it get to your head. Not until it's over.\n"
                    voice "audio/voices/ch3/eye/princess/39.flac"
                    show needle outside fight interstitial3 talk onlayer front at Position(ypos=1125)
                    with dissolve
                    sp "Yes, finally! This is the hole I've felt in my heart! This is what I've needed! This is what I've been missing! This is how it always needed to end! Both of us, giving it our all. Beating and bleeding each other to death.\n"
                    voice "audio/voices/ch3/eye/narrator/91.flac"
                    play audio "audio/final/Adversary_ABackAndForth_1.flac"
                    hide needle onlayer front
                    hide bg onlayer farback
                    scene farback needle d basement montage onlayer farback at Position(ypos=1125)
                    show needle montage2 onlayer front at Position(ypos=1125)
                    with Dissolve(1.0)
                    n "The two of you engage in a devastating flurry of blows, each of you wounding the other again and again.\n"
                    play secondary "audio/final/Tower_KnifeBlow_SEQUENCED_5.flac"
                    queue secondary "audio/one_shot/blood_drip.flac"
                    voice "audio/voices/ch3/eye/narrator/92.flac"
                    hide needle onlayer front
                    show needle montage3 onlayer front at Position(ypos=1125)
                    n "She's stronger, but you're faster, and the deeper the both of you fall into your lethal dance, the more your edge shines over hers. She's slowing down. Blood pouring from wounds, splattering at her feet, leaving her weak and unsteady.\n"
                    voice "audio/voices/ch3/eye/stubborn/35.flac"
                    stubborn "More! Keep going, we can't stop now.\n"
                    voice "audio/voices/ch3/eye/narrator/93.flac"
                    play audio "audio/final/Tower_KnifeBlow_2.flac"
                    hide needle onlayer front
                    hide farback onlayer back
                    hide farback onlayer farback
                    scene bg needle fight interstitial2 onlayer farback at Position(ypos=1125)
                    show needle outside combat1 onlayer front at Position(ypos=1125)
                    with Dissolve(1.0)
                    $ renpy.pause(0.25)
                    voice sustain
                    play audio "audio/one_shot/hard tighten.flac"
                    show needle outside combat2 onlayer front at Position(ypos=1125)
                    with Dissolve(1.0)
                    $ renpy.pause(0.5)
                    play audio "audio/final/Tower_GiantPundingPlayerGround_NEW_2.flac"
                    voice sustain
                    scene bg black
                    hide needle onlayer front
                    hide bg onlayer farback
                    n "You spy an opening. But this time she's waiting for you. She lets you sink the blade deep, trapping you in place long enough to wrap you in her impenetrable arms. You're slammed to the ground.\n"
                    voice "audio/voices/ch3/eye/stubborn/36.flac"
                    stubborn "Nothing. These blows are nothing to us.\n"
                    voice "audio/voices/ch3/eye/narrator/94.flac"
                    stop sound fadeout 20.0
                    stop secondary fadeout 20.0
                    stop tertiary fadeout 20.0
                    stop music fadeout 20.0
                    stop music2 fadeout 20.0
                    stop music3 fadeout 20.0
                    stop music4 fadeout 20.0
                    play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 20.0
                    scene bg needle outside combat3 onlayer farback at Position(ypos=1125)
                    show quiet creep1 onlayer back at Position(ypos=1125)
                    show needle outside combat3 onlayer front at Position(ypos=1125)
                    with Dissolve(2.0)
                    n "But her gambit wasn't enough to close the gap. It wasn't enough to kill you. She stares you down, coughing up a splash of blood as she gasps for breath.\n"
                    $ gallery_needle.unlock_item(9)
                    $ gallery_needle.unlock_item(10)
                    $ gallery_needle.unlock_item(11)
                    $ gallery_needle.unlock_item(12)
                    $ gallery_needle.unlock_item(13)
                    $ renpy.save_persistent()
                    voice "audio/voices/ch3/eye/princess/40.flac"
                    show quiet creep2 onlayer back at Position(ypos=1125)
                    show needle outside combat3 talk onlayer front
                    with Dissolve(2.0)
                    sp "Hah. You've outplayed me, haven't you?\n"
                    #voice "audio/voices/ch3/eye/hunted/40.flac"
                    #hunted "Her heart! Now!\n"
                    #voice "audio/voices/ch3/eye/narrator/95.flac"
                    #n "You lunge forward for one final strike...\n"
                    voice "audio/voices/ch3/eye/princess/41.flac"
                    sp "Something feels wrong... something —\n{w=3.38}{nw}"
                    show screen disableclick(0.5)
                    voice "audio/voices/ch3/eye/hero/28a.flac"
                    hero "And? Then what happens?\n"
                    play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
                    show quiet creep3 onlayer back at Position(ypos=1125)
                    show needle outside combat3 onlayer front
                    show arms needle combat1 onlayer back at Position(ypos=1125)
                    with Dissolve(1.0)
                    $ renpy.pause(0.125)
                    show needle outside combat quiet onlayer front
                    show arms needle combat2 onlayer back at Position(ypos=1125)
                    with Dissolve(1.0)
                    $ renpy.pause(0.125)
                    hide needle onlayer front
                    show arms needle combat3 onlayer back at Position(ypos=1125)
                    with Dissolve(0.5)
                    $ renpy.pause(0.125)
                    show arms needle combat4 onlayer back at Position(ypos=1125)
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
                    $ achievement.grant("ACH_ADV_AGILE")
                    if loops_finished != 0:
                        truth "But you do not have the chance to respond. Nor will you ever. It's time for you to leave. Memory returns.\n"
                    else:
                        truth "But you do not have the chance to respond. Something has taken her away, and it's left something else in her place.\n"
                    $ adversary_2_end = "fight_succeed"
                    $ princess_free += 1
                    $ princess_satisfy += 1
                    $ current_princess = "needle"
                    jump mirror_start

            #"{i}• [[Turn around and leave.]{/i}" if trait_hunted:
                #$ caught_origin_ch3 = True
                # special caught header
                #voice "audio/voices/ch3/eye/narrator/96.flac"
                #n "But you never strike. Instead, you bound off into the trees. You coward! There's no winning here. There's no survival when she still lives, there's no...\n"
                #jump caught_start

return
