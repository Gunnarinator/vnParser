label wild_start:

    # starting things up

    stop music
    stop sound
    stop secondary
    $ default_mouse = "default"
    $ blade_held = False
    $ current_loop = 2
    $ quick_menu = False
    $ config.menu_include_disabled = False

    default wild_source = ""
    default wild_bonus_voice = ""
    if current_princess == "witch":
        $ wild_source = "witch"
    else:
        $ wild_source = "beast"
    $ current_princess = "wild"
    $ wild_encountered = True

    # Permutations:

    # witch -> opportunist + cheated (get crushed talking or waiting to die)
    # witch -> opportunist + paranoid (ran upstairs like a wittle baby)
    # witch -> opportunist + stubborn (go out fighting)
    if wild_bonus_voice == "stubborn":
        $ trait_stubborn = True
    if wild_bonus_voice == "paranoid":
        $ trait_paranoid = True
    if wild_bonus_voice == "cheated":
        $ trait_cheated = True

    # beast -> eaten (and suicide) hunted + stubborn
    # beast -> eaten (and killed): hunted + broken
    # beast -> eaten (playing dead): hunted + contrarian
    # beast -> eaten + attack heart: hunted + opportunist
    if wild_bonus_voice == "stubborn":
        $ trait_stubborn = True
    if wild_bonus_voice == "broken":
        $ trait_broken = True
    if wild_bonus_voice == "contrarian":
        $ trait_contrarian = True
    if wild_bonus_voice == "opportunist":
        $ trait_opportunist = True

    play sound "audio/looping/uncomfortable ambiance heightened.ogg" loop fadein 1.0
    scene chapter wild with fade
    show text _("{color=#FFFFFF00}Chapter Three. The Wild.{/color}") at Position(ypos=850)
    $ renpy.pause(4.0)
    scene bg black with fade
    $ default_mouse = "eye"
    $ renpy.music.set_volume(0.8, channel='music')
    $ renpy.music.set_volume(0.55, channel='music2')
    $ renpy.music.set_volume(0.05, channel='music3')
    play music "audio/_music/ch3/wild/the_wild_l1.flac" loop
    play music2 "audio/_music/ch3/wild/the_wild_l2.flac" loop
    play music3 "audio/_music/ch3/wild/the_wild_l3.flac" loop

    #$ renpy.music.set_volume(1.0, channel='music')
    #$ renpy.music.set_volume(0.05, channel='music2')
    #$ renpy.music.set_volume(1.0, channel='music3')
    #$ renpy.music.set_volume(0.05, channel='music4')
    #play music "audio/music/full/The Wild Base FINAL.ogg" loop
    #play music2 "audio/music/full/The Wild BREATHS FINAL.ogg" loop
    #play music3 "audio/music/full/The Wild DIST VOCALS FINAL.ogg" loop
    #play music4 "audio/music/full/The Wild Quiet FINAL.ogg" loop
    $ gallery_wild.unlock_gallery()
    $ gallery_wild.unlock_item(1)
    $ renpy.save_persistent()

    scene farback wild onlayer farback at Position(ypos=1125)
    show bg wild woods onlayer back at Position(ypos=1125)
    show mid wild woods onlayer front at Position(ypos=1125)
    show fore wild woods onlayer inyourface at Position(ypos=1125)
    with fade

    if persistent.quick_menu:
        $ quick_menu = True
    $ renpy.pause(0.5)

    show bg wild woods talk onlayer back
    show mid wild woods talk onlayer front
    show fore wild woods talk onlayer inyourface
    with dissolve

    voice "audio/voices/ch3/wild/princess/1a.flac"
    wp "We are a path in the woods. We have no beginning, and we have no end, but something cold and unnatural sits watching us from just beyond our edge.\n"
    voice "audio/voices/ch3/wild/princess/2.flac"
    wp "His gaze pushes against our borders, curling them in on themselves, preventing them from stretching to the places they need to reach.\n"
    voice "audio/voices/ch3/wild/narrator/1.flac"
    show bg wild woods onlayer back
    show mid wild woods onlayer front
    show fore wild woods onlayer inyourface
    with dissolve
    n "No, no, no. That's all wrong. You're not {i}a{/i} path in the woods, you're {i}on{/i} a path in the woods. Who's even saying that?\n"
    voice "audio/voices/ch3/wild/narrator/2.flac"
    n "That's not... that's not the Princess, is it? Oh no, how many times have you been here?\n"
    voice "audio/voices/ch3/wild/hero/1.flac"
    hero "I think this is our third.\n"
    voice "audio/voices/ch3/wild/narrator/3.flac"
    n "That's bad. That's very, very bad. It wasn't even supposed to reach two. If you're at three, well... no wonder things aren't the way they're supposed to be.\n"
    if trait_contrarian:
        voice "audio/voices/ch3/wild/contrarian/1.flac"
        contrarian "Oh, isn't that fun! He's upset.\n"
        voice "audio/voices/ch3/wild/narrator/4.flac"
        n "Of course I'm upset! The world is at stake here, as I'm sure you already know.\n"
    voice "audio/voices/ch3/wild/narrator/5.flac"
    n "{i}Sigh{/i}. Let's get our facts straight. What happened last time? What could you have possibly done for things to be like {i}this{/i}?\n"
    voice "audio/voices/ch3/wild/princess/3.flac"
    show bg wild woods talk onlayer back
    show mid wild woods talk onlayer front
    show fore wild woods talk onlayer inyourface
    with dissolve
    wp "The thing that sits beyond our edge speaks His logic into us. He tries to grasp at things that cannot be grasped.\n"
    voice "audio/voices/ch3/wild/princess/4.flac"
    wp "He tries to stare with wide pupils at that which can only be held from the corner of the eye or with a passing glance.\n"
    voice "audio/voices/ch3/wild/narrator/6.flac"
    show bg wild woods onlayer back
    show mid wild woods onlayer front
    show fore wild woods onlayer inyourface
    with dissolve
    n "Shut up! The rest of you, talk. What happened? What did you do?\n"
    if wild_source == "witch":
        if trait_paranoid:
            voice "audio/voices/ch3/wild/paranoid/1.flac"
            paranoid "Why does he want to know? I don't mind what we are right now. It's... rather nice. I can hear what everyone is thinking.\n"
            voice "audio/voices/ch3/wild/opportunist/1.flac"
            opportunist "There's no reason to keep secrets. We tried leaving her in the basement, but she made the cabin come to life and it crushed both of us into a fine paste. And now we're here. Existing.\n"
            voice "audio/voices/ch3/wild/opportunist/2.flac"
            opportunist "And for what it's worth, I'm with him. This is nice.\n"
        elif trait_stubborn:
            voice "audio/voices/ch3/wild/opportunist/3.flac"
            opportunist "Sure. There's no reason to keep secrets. Someone decided to go in guns blazing last time, and that someone got us killed.\n"
            voice "audio/voices/ch3/wild/stubborn/1.flac"
            stubborn "And what should we have done, let you draw things out with all that... conniving? Everyone knows a straight fight is best. It's honest.\n"
            voice "audio/voices/ch3/wild/opportunist/4.flac"
            opportunist "There's no need to bicker about it, I wasn't trying to start anything. I don't mind what happened to us. I kind of like it now that we aren't actively being crushed.\n"
            voice "audio/voices/ch3/wild/stubborn/2.flac"
            stubborn "Yeah... now that you mention it, this isn't so bad.\n"
            voice "audio/voices/ch3/wild/hero/2.flac"
            hero "And it's not like the fight is what killed us, anyway. It was the cabin. No point worrying about who charged who when that place ground us all into paste in the end, the Princess included.\n"
        else:
            voice "audio/voices/ch3/wild/opportunist/5.flac"
            opportunist "There's no reason to keep secrets. We tried fighting her, and then she made the cabin itself come to life and squished us into paste.\n"
            voice "audio/voices/ch3/wild/cheated/1.flac"
            cheated "All that unfairness... what if it was just pushing us in the right direction? Helping us become this? It's almost worth being squished by a cabin.\n"

        voice "audio/voices/ch3/wild/princess/5.flac"
        show bg wild woods talk onlayer back
        show mid wild woods talk onlayer front
        show fore wild woods talk onlayer inyourface
        with dissolve
        wp "It was a fitting end. I'm sorry if it hurt. But doesn't {i}this{/i} make it all seem so small?\n"
        voice "audio/voices/ch3/wild/narrator/7.flac"
        show bg wild woods onlayer back
        show mid wild woods onlayer front
        show fore wild woods onlayer inyourface
        with dissolve
        n "I see... so the cabin ground you into paste, and now you're convinced you're stuck together. What a mess.\n"

    else:
        if trait_stubborn:
            voice "audio/voices/ch3/wild/hunted/1a.flac"
            hunted "We're part of her because she consumed us. Can she hear us if we talk?\n"
        else:
            voice "audio/voices/ch3/wild/hunted/1.flac"
            hunted "Can she hear us if we talk?\n"
        voice "audio/voices/ch3/wild/princess/6.flac"
        wp "I can hear everything, little one, but you don't have to be afraid of me. There's no place where you end and I begin. Nothing can hurt you here. Not anymore.\n"
        if trait_broken or trait_stubborn:
            if trait_broken:
                voice "audio/voices/ch3/wild/broken/1.flac"
                show bg wild woods onlayer back
                show mid wild woods onlayer front
                show fore wild woods onlayer inyourface
                with dissolve
                broken "That's just because she devoured us and we dissolved away. We don't even exist as a body anymore...\n"
            else:
                voice "audio/voices/ch3/wild/stubborn/3a.flac"
                show bg wild woods onlayer back
                show mid wild woods onlayer front
                show fore wild woods onlayer inyourface
                with dissolve
                stubborn "It shouldn't count as her eating us if we offed ourselves.\n"
            voice "audio/voices/ch3/wild/hunted/2a.flac"
            hunted "We're still here, though. And if we're safe, isn't that better?\n"
            if trait_stubborn:
                voice "audio/voices/ch3/wild/stubborn/4.flac"
                stubborn "I guess this is... fine. Doesn't feel half bad. Miles better than being dissolved, anyway.\n"
        if trait_opportunist or trait_contrarian:
            voice "audio/voices/ch3/wild/hunted/3.flac"
            hunted "O-oh. I like that. I don't feel so small anymore when you put it like that.\n"
            voice "audio/voices/ch3/wild/princess/7.flac"
            show bg wild woods talk onlayer back
            show mid wild woods talk onlayer front
            show fore wild woods talk onlayer inyourface
            with dissolve
            wp "That's because you aren't small, even if you act that way. We're both so much more together than we were apart. And we can be so much more still. Vast. Unfathomable.\n"
            if trait_opportunist:
                voice "audio/voices/ch3/wild/opportunist/6.flac"
                show bg wild woods onlayer back
                show mid wild woods onlayer front
                show fore wild woods onlayer inyourface
                with dissolve
                opportunist "You're not mad at us for stabbing you in the heart, are you?\n"
                voice "audio/voices/ch3/wild/princess/8.flac"
                wp "No. Are you mad at me for swallowing you whole?\n"
                voice "audio/voices/ch3/wild/opportunist/7.flac"
                show bg wild woods onlayer back
                show mid wild woods onlayer front
                show fore wild woods onlayer inyourface
                with dissolve
                opportunist "Nah, not really. It all seems so... petty right now.\n"
                #cute exchange :3
            else:
                voice "audio/voices/ch3/wild/contrarian/2.flac"
                contrarian "If you really want to know what happened, we tried playing dead, and she ate us.\n"

        voice "audio/voices/ch3/wild/narrator/8.flac"
        n "She {i}ate{/i} you? And now you're convinced that you're stuck together? What a mess.\n"
        #added 'what a mess' from prev version

    voice "audio/voices/ch3/wild/princess/9.flac"
    show bg wild woods talk onlayer back
    show mid wild woods talk onlayer front
    show fore wild woods talk onlayer inyourface
    with dissolve
    wp "He doesn't understand. We aren't convinced of anything, and we aren't stuck together. We're one. This is how we're supposed to be, can't you feel it?\n"
    if trait_contrarian:
        voice "audio/voices/ch3/wild/contrarian/3.flac"
        show bg wild woods onlayer back
        show mid wild woods onlayer front
        show fore wild woods onlayer inyourface
        with dissolve
        contrarian "Sure, 'being one with the Princess' is pretty great, but what can we even do right now? I hope we're not supposed to just passively {i}exist{/i} like this. I did not sign up for passive existence when we faked our own death.\n"
    elif trait_broken:
        voice "audio/voices/ch3/wild/broken/2.flac"
        show bg wild woods onlayer back
        show mid wild woods onlayer front
        show fore wild woods onlayer inyourface
        with dissolve
        broken "I guess that's that, then. This is us now. We're the woods. Okay.\n"


label wild_menu_1:
    default wild_passive = False
    default wild_menu_what_narrator = False
    default wild_2_soft = False
    menu:
        extend ""

        "{i}• (Explore) ''This... thing watching us. What is He?''{/i}" if wild_menu_what_narrator == False:
            $ wild_menu_what_narrator = True
            voice "audio/voices/ch3/wild/narrator/9.flac"
            n "I'm not 'watching you.' I'm trying to help you.\n"
            voice "audio/voices/ch3/wild/hero/3.flac"
            hero "That's not an answer to our question.\n"
            voice "audio/voices/ch3/wild/princess/10.flac"
            show bg wild woods talk onlayer back
            show mid wild woods talk onlayer front
            show fore wild woods talk onlayer inyourface
            with dissolve
            wp "I don't know what He is. I only know that He is something other, and that He wishes for you and I to tear ourselves apart.\n"
            voice "audio/voices/ch3/wild/narrator/10.flac"
            show bg wild woods onlayer back
            show mid wild woods onlayer front
            show fore wild woods onlayer inyourface
            with dissolve
            n "I do want that, but only because it's in your best interests. It's in everyone's best interests. You won't be able to slay her unless you remove yourself from her.\n"
            #added line reminding about 'end the world' situation
            voice "audio/voices/ch3/wild/princess/11.flac"
            show bg wild woods talk onlayer back
            show mid wild woods talk onlayer front
            show fore wild woods talk onlayer inyourface
            with dissolve
            wp "He wants us to kill each other.\n"
            voice "audio/voices/ch3/wild/narrator/11.flac"
            show bg wild woods onlayer back
            show mid wild woods onlayer front
            show fore wild woods onlayer inyourface
            with dissolve
            n "I don't. I want you to kill {i}her{/i}. Don't be charmed by her faux-solidarity. You're not 'in this together.'\n"
            voice "audio/voices/ch3/wild/narrator/12.flac"
            n "She's the only one who poses a threat to the world, and she's trying to make you go along with it. You don't have to enable her, especially when you have what it takes to stop her.\n"
            #added a bit where he hints that you've been taken over, trying to cater to your individuality
            jump wild_menu_1

        "{i}• ''I've had enough of this guy. How do we stop him?''{/i}" if wild_menu_what_narrator:
            jump wild_princess_join

        "{i}• ''Okay. Let's say I want to stop her. What do I do? I feel like I can't do much of anything right now.''{/i}" if wild_menu_what_narrator:
            jump wild_menu_narrator_push_1_join

        "{i}• [[Passively exist.]{/i}" if trait_contrarian:
            $ wild_passive = True
            label wild_menu_1_narrator_join:
                if trait_contrarian:
                    voice "audio/voices/ch3/wild/contrarian/4.flac"
                    contrarian "No, please, anything but that!\n"
                #voice "audio/voices/ch3/wild/narrator/13a.flac"
                #n "You can't just passively exist forever. That isn't how it works.\n"
                voice "audio/voices/ch3/wild/narrator/13.flac"
                n "You can't just passively exist forever. Not with her. That isn't how it works.\n"
                if wild_source == "witch":
                    voice "audio/voices/ch3/wild/narrator/14.flac"
                    n "I don't care if it was the cabin that killed you, because it seems to me like she was the reason the cabin could even do something like that in the first place.\n"
                    label wild_dissonance_witch_early_join:
                        voice "audio/voices/ch3/wild/narrator/15a.flac"
                        n "You need to remember that you and the Princess are enemies. Don't let bygones be bygones. Remember what she's done to you, and how much it hurt.\n"
                        label wild_dissonance_witch_join:
                            $ renpy.music.set_volume(0.05, 0.5, channel='music')
                            $ renpy.music.set_volume(1.0, 0.5, channel='music2')
                            $ renpy.music.set_volume(0.5, 0.5, channel='music3')
                            voice "audio/voices/ch3/wild/princess/12.flac"
                            show bg wild woods angry onlayer back
                            show mid wild woods angry onlayer front
                            show fore wild woods angry onlayer inyourface
                            with hpunch
                            swp "We can't go back to that! We can't go back to the doubting and the hatred and the schemes! Not after being something as beautiful as this.\n"
                else:
                    label wild_dissonance_beast_early_join:
                        voice "audio/voices/ch3/wild/narrator/16.flac"
                        n "The Princess ate you last time. Stop passively... {i}vibing{/i} with a literal predator, and remember that you're enemies. Remember what she's done to you, and how much it hurt.\n"
                        label wild_dissonance_beast_join:
                            $ renpy.music.set_volume(0.05, 0.5, channel='music')
                            $ renpy.music.set_volume(1.0, 0.5, channel='music2')
                            $ renpy.music.set_volume(0.5, 0.5, channel='music3')
                            voice "audio/voices/ch3/wild/princess/13.flac"
                            show bg wild woods angry onlayer back
                            show mid wild woods angry onlayer front
                            show fore wild woods angry onlayer inyourface
                            with hpunch
                            swp "We can't go back to that! We can't go back to the fear and the hunger and the pain. Not after being something as beautiful as this.\n"

                $ renpy.music.set_volume(0.8, 1.75, channel='music')
                $ renpy.music.set_volume(0.55, 1.75, channel='music2')
                $ renpy.music.set_volume(0.05, 1.75, channel='music3')
                voice "audio/voices/ch3/wild/princess/14.flac"
                show bg wild woods talk onlayer back
                show mid wild woods talk onlayer front
                show fore wild woods talk onlayer inyourface
                with dissolve
                wp "Doesn't all that conflict feel so far away right now? So petty? We've been posed against each other by something that understands the strength of our unity.\n"
                if wild_source == "witch":
                    voice "audio/voices/ch3/wild/opportunist/8.flac"
                    show bg wild woods onlayer back
                    show mid wild woods onlayer front
                    show fore wild woods onlayer inyourface
                    with dissolve
                    opportunist "Spoken like... honestly, a real puppetmaster. Have we considered that maybe she's the one trying to trick us?\n"
                    voice "audio/voices/ch3/wild/princess/15.flac"
                    show bg wild woods talk onlayer back
                    show mid wild woods talk onlayer front
                    show fore wild woods talk onlayer inyourface
                    with dissolve
                    wp "I'm not.\n"
                    voice "audio/voices/ch3/wild/hero/4a.flac"
                    show bg wild woods onlayer back
                    show mid wild woods onlayer front
                    show fore wild woods onlayer inyourface
                    with dissolve
                    hero "But there's a feeling isn't there? That petty feeling she mentioned. It's fuzzy but... it's there. Almost like... she still hates us.\n"
                    #voice "audio/voices/ch3/wild/hero/4b.flac"
                    #hero "But there is something there. That petty feeling she mentioned. It's fuzzy but... it's there. Almost like... she still hates us.\n"
                    voice "audio/voices/ch3/wild/opportunist/9.flac"
                    opportunist "It feels mutual.\n"
                    voice "audio/voices/ch3/wild/princess/16.flac"
                    show bg wild woods talk onlayer back
                    show mid wild woods talk onlayer front
                    show fore wild woods talk onlayer inyourface
                    with dissolve
                    wp "Please, stop. If you pay attention to that feeling we'll fall apart.\n"
                    $ renpy.music.set_volume(0.05, 0.5, channel='music')
                    $ renpy.music.set_volume(1.0, 0.5, channel='music2')
                    $ renpy.music.set_volume(0.5, 0.5, channel='music3')
                    voice "audio/voices/ch3/wild/princess/17.flac"
                    show bg wild woods angry onlayer back
                    show mid wild woods angry onlayer front
                    show fore wild woods angry onlayer inyourface
                    with hpunch
                    swp "Don't look at it!\n"
                    voice "audio/voices/ch3/wild/narrator/18.flac"
                    n "She's trying to turn you away from the truth. There's something she doesn't want you to see, and I think you already know you have to look at it.\n"
                    if trait_cheated:
                        voice "audio/voices/ch3/wild/cheated/2.flac"
                        $ renpy.music.set_volume(0.8, 1.75, channel='music')
                        $ renpy.music.set_volume(0.55, 1.75, channel='music2')
                        $ renpy.music.set_volume(0.05, 1.75, channel='music3')
                        show bg wild woods onlayer back
                        show mid wild woods onlayer front
                        show fore wild woods onlayer inyourface
                        with dissolve
                        cheated "They're both playing their hands. What's the move? Do we pick a side? Do we figure out how to make everyone unhappy?\n"
                    if trait_paranoid:
                        voice "audio/voices/ch3/wild/paranoid/2a.flac"
                        $ renpy.music.set_volume(0.8, 1.75, channel='music')
                        $ renpy.music.set_volume(0.55, 1.75, channel='music2')
                        $ renpy.music.set_volume(0.05, 1.75, channel='music3')
                        show bg wild woods onlayer back
                        show mid wild woods onlayer front
                        show fore wild woods onlayer inyourface
                        with dissolve
                        paranoid "Everyone's pulling us in different directions. But that feeling... that feeling doesn't have a motive. It just exists. Maybe we should look at it.\n"

                else:
                    voice "audio/voices/ch3/wild/hunted/4a.flac"
                    hunted "I can feel a thumping. A heartbeat.\n"
                    voice "audio/voices/ch3/wild/hero/5.flac"
                    hero "Like a distant terror that keeps getting louder the more we pay attention.\n"
                    voice "audio/voices/ch3/wild/princess/18.flac"
                    show bg wild woods talk onlayer back
                    show mid wild woods talk onlayer front
                    show fore wild woods talk onlayer inyourface
                    with dissolve
                    wp "Please, stop. If you let it in, we'll fall apart.\n"
                    $ renpy.music.set_volume(0.05, 0.5, channel='music')
                    $ renpy.music.set_volume(1.0, 0.5, channel='music2')
                    $ renpy.music.set_volume(0.5, 0.5, channel='music3')
                    voice "audio/voices/ch3/wild/princess/19.flac"
                    show bg wild woods angry onlayer back
                    show mid wild woods angry onlayer front
                    show fore wild woods angry onlayer inyourface
                    with hpunch
                    swp "Don't look at it!\n"
                    if trait_contrarian:
                        voice "audio/voices/ch3/wild/contrarian/5.flac"
                        $ renpy.music.set_volume(0.8, 1.75, channel='music')
                        $ renpy.music.set_volume(0.55, 1.75, channel='music2')
                        $ renpy.music.set_volume(0.05, 1.75, channel='music3')
                        show bg wild woods onlayer back
                        show mid wild woods onlayer front
                        show fore wild woods onlayer inyourface
                        with dissolve
                        contrarian "Maybe a little peek wouldn't hurt. Aren't you curious?\n"
                        voice "audio/voices/ch3/wild/narrator/19.flac"
                        n "I'm curious. You should look.\n"
                        voice "audio/voices/ch3/wild/contrarian/6.flac"
                        contrarian "Nevermind. If He wants to look then I don't want to.\n"
                    if trait_opportunist:
                        voice "audio/voices/ch3/wild/opportunist/10.flac"
                        $ renpy.music.set_volume(0.8, 1.75, channel='music')
                        $ renpy.music.set_volume(0.55, 1.75, channel='music2')
                        $ renpy.music.set_volume(0.05, 1.75, channel='music3')
                        show bg wild woods onlayer back
                        show mid wild woods onlayer front
                        show fore wild woods onlayer inyourface
                        with dissolve
                        opportunist "I think we should hear out whatever it is that's trying to be heard. I like to take all options into account before making any big decisions, and what's the harm in just listening?\n"
                        #opportunist "It's never worth staring into the void. Take it from somebody who compulsively does it whenever he has the chance. (I'm talking about me.)\n"
                if trait_stubborn:
                    voice "audio/voices/ch3/wild/stubborn/5.flac"
                    stubborn "Hold yourself together. We're no strangers to effort. We can push this back down. Something might do us in eventually, but I'll be damned if that something is a thought.\n"
                    #a little more flavor
                jump wild_menu_2

        "{i}• ''Why should anyone do anything right now? This is fine! I like being this.''{/i}":
            jump wild_menu_1_narrator_join

        "{i}• ''Why are you being nice to me? Don't you hate me? Don't we sort of hate each other?''{/i}" if wild_source == "witch":
            jump wild_dissonance_witch_join

        "{i}• ''Why are you being nice to me? Aren't you a monster? Didn't you eat me?''{/i}" if wild_source == "beast":
            jump wild_dissonance_beast_join

        "{i}• ''He's right! I don't want a passive existence. I want things to do. So someone give me some options!''{/i}" if trait_contrarian and wild_menu_what_narrator == False:
            label wild_menu_narrator_push_1_join:
                voice "audio/voices/ch3/wild/narrator/20.flac"
                n "You can start by remembering that you exist. And not as some part of a gestalt entity formed with the Princess.\n"
                label wild_menu_1_options_join:
                    voice "audio/voices/ch3/wild/narrator/21.flac"
                    n "You exist as your own self, complete with your own physical body separate from hers.\n"
                    voice "audio/voices/ch3/wild/hero/6.flac"
                    hero "I'm not so sure about that. We were something like that once, but now...?\n"
                    voice "audio/voices/ch3/wild/narrator/22.flac"
                    n "And if thinking about that isn't enough to startle you back to reality, consider this:\n"
                    if wild_source == "beast":
                        jump wild_dissonance_beast_early_join
                    else:
                        voice "audio/voices/ch3/wild/narrator/23.flac"
                        n "She committed a murder-suicide using a living cabin.\n"
                        voice "audio/voices/ch3/wild/hero/7.flac"
                        hero "... Right. That was unpleasant. We weren't big fans of that. I think.\n"
                        voice "audio/voices/ch3/wild/opportunist/11.flac"
                        opportunist "I'm sure I would have had us do the same thing if we were in her shoes. We really do make a great pair. He's probably just jealous.\n"
                        jump wild_dissonance_witch_early_join

        "{i}• ''I can feel the pressure of the outside pushing in on us. What are we supposed to do about it?''{/i}":
            jump wild_princess_join

        "{i}• ''This is how we're supposed to be. But what do we do now?''{/i}" if wild_menu_what_narrator == False:
            label wild_princess_join:
                $ wild_2_soft = True
                voice "audio/voices/ch3/wild/princess/20.flac"
                wp "We push back. It may feel like He's everywhere, but presence isn't strength. Otherwise he would have torn us apart by now. There must be a crack in the walls of this prison. There must be a way for us to be free from him.\n"
                voice "audio/voices/ch3/wild/narrator/24.flac"
                show bg wild woods onlayer back
                show mid wild woods onlayer front
                show fore wild woods onlayer inyourface
                with dissolve
                n "She's trying to use you. After everything she's done, you should be able to see that. I may not have been around to witness it, but clearly you remember what happened. How about you try remembering how it all {i}felt{/i}?\n"
                menu:
                    extend ""

                    "{i}• (Explore) [[Remember how it felt.]{/i}":
                        if wild_source == "beast":
                            jump wild_dissonance_beast_join
                        else:
                            jump wild_dissonance_witch_join

                    "{i}• [[Turn inward and find your freedom.]{/i}":
                        jump wild_side_princess

        "{i}• ''Whatever we are right now is an abomination, and I want out!''{/i}":
            voice "audio/voices/ch3/wild/princess/21.flac"
            show bg wild woods talk onlayer back
            show mid wild woods talk onlayer front
            show fore wild woods talk onlayer inyourface
            with dissolve
            wp "How could you say that? Look at us. We're almost everything. And we can be even more than this. Don't you feel our potential?\n"
            voice "audio/voices/ch3/wild/narrator/25.flac"
            show bg wild woods onlayer back
            show mid wild woods onlayer front
            show fore wild woods onlayer inyourface
            with dissolve
            n "Great! You can start by remembering that you exist. And not just as some dissolved component of a gestalt entity formed from you and the Princess.\n"
            jump wild_menu_1_options_join

        "{i}• ''I don't like this. I'm supposed to be me, and you're supposed to be something that isn't me.''{/i}":
            voice "audio/voices/ch3/wild/princess/21.flac"
            show bg wild woods talk onlayer back
            show mid wild woods talk onlayer front
            show fore wild woods talk onlayer inyourface
            with dissolve
            wp "How could you say that? Look at us. We're almost everything. And we can be even more than this. Don't you feel our potential?\n"
            voice "audio/voices/ch3/wild/narrator/26.flac"
            show bg wild woods onlayer back
            show mid wild woods onlayer front
            show fore wild woods onlayer inyourface
            with dissolve
            n "No, you're spot on. You exist. And not as some part of a gestalt entity mushed together with bits of you and the Princess. You're an individual!\n"
            jump wild_menu_1_options_join

        "{i}• ''Okay, you, Narrator. How do I stop her?''{/i}":
            jump wild_menu_narrator_push_1_join

        "{i}• [[Do nothing.]{/i}" if trait_contrarian == False:
            $ wild_passive = True
            jump wild_menu_1_narrator_join

label wild_menu_2:
    menu:
        extend ""

        "{i}• [[Gaze at the terror in your heart.]{/i}" if wild_source == "beast":
            voice "audio/voices/ch3/wild/princess/22.flac"
            show bg wild woods talk onlayer back
            show mid wild woods talk onlayer front
            show fore wild woods talk onlayer inyourface
            with dissolve
            wp "Please... don't make us remember how I was.\n"
            jump wild_side_narrator

        "{i}• [[Gaze at the hatred in your heart.]{/i}" if wild_source == "witch":
            voice "audio/voices/ch3/wild/princess/23.flac"
            show bg wild woods talk onlayer back
            show mid wild woods talk onlayer front
            show fore wild woods talk onlayer inyourface
            with dissolve
            wp "Please... don't make us remember how we were.\n"
            jump wild_side_narrator

        "{i}• [[Bury it. Now. Before it's too late.]{/i}":
            voice "audio/voices/ch3/wild/narrator/27.flac"
            n "No. You can't bury that feeling. You can't hide from your past.\n"
            voice "audio/voices/ch3/wild/princess/24.flac"
            show bg wild woods talk onlayer back
            show mid wild woods talk onlayer front
            show fore wild woods talk onlayer inyourface
            with dissolve
            wp "The past doesn't have to exist. Our freedom is within us. We just have to find it.\n"
            show bg wild woods onlayer back
            show mid wild woods onlayer front
            show fore wild woods onlayer inyourface
            with dissolve
            menu:
                extend ""

                "{i}• ''But the past does exist. I remember it.''{/i}":
                    jump wild_side_narrator

                "{i}• [[Turn inward and find your freedom.]{/i}":
                    jump wild_side_princess

label wild_side_narrator:
    play secondary "audio/final/Tower_Earthquake_loop_1.ogg" loop
    show bg wild woods onlayer back at screenshake
    show mid wild woods onlayer front at screenshake
    show fore wild woods onlayer inyourface at screenshake
    with dissolve
    voice "audio/voices/ch3/wild/narrator/28.flac"
    n "And just like that, you start to fall apart.\n"
    if wild_source == "witch":
        voice "audio/voices/ch3/wild/opportunist/12.flac"
        opportunist "Right. She really does hate us. And we hate her. It hurts thinking about us as separate things, but we're separate. We can't hate ourself. I love me.\n"
        if trait_stubborn:
            voice "audio/voices/ch3/wild/stubborn/6.flac"
            stubborn "We never got to see the end of that fight, did we? And we can't both be winners. One of us has to beat the other, right?\n"
        if trait_cheated:
            voice "audio/voices/ch3/wild/cheated/3.flac"
            cheated "Honestly I can't believe I ever thought being crushed to death with a cabin was forgiveable. Did she put that thought in our head? Is she able to change what we think?! That's not fair! ... I think.\n"
        if trait_paranoid:
            voice "audio/voices/ch3/wild/paranoid/3.flac"
            paranoid "What were we thinking! Giving in to absolute madness. We exist! We're real! We're separate from her! Of course we are! ... But what are we? I can't remember.\n"
        voice "audio/voices/ch3/wild/hero/8a.flac"
        hero "I don't want to remember what it felt like to be killed. It was so much nicer when it didn't feel like it mattered.\n"
        voice "audio/voices/ch3/wild/narrator/29.flac"
        n "And yet, you keep remembering. You remember the loathing and animosity you've shared with the Princess, the pain and the anger and the betrayal. And you start to remember something else, too.\n"
    if wild_source == "beast":
        voice "audio/voices/ch3/wild/hunted/5.flac"
        hunted "I can remember it now. I didn't like being eaten.\n"
        voice "audio/voices/ch3/wild/hero/9.flac"
        hero "I'd forgotten how much it burned. And the air was so hard to breathe, and she didn't care. She didn't care at all.\n"
        if trait_stubborn:
            voice "audio/voices/ch3/wild/stubborn/7.flac"
            stubborn "At least we didn't have to sit through it to the end. But I think she owes us, don't you, lads? She barely felt more than a little indigestion while we burned away inside of her.\n"
        if trait_opportunist:
            voice "audio/voices/ch3/wild/opportunist/13.flac"
            opportunist "All of that digging with the knife and we didn't even get to win. That was hard work! I wanted to win! And what's the point of being part of a larger whole if we're not the one in charge of that whole?\n"
        voice "audio/voices/ch3/wild/narrator/30.flac"
        n "As you remember the terror and pain you've felt at the hands of the Princess, you start to remember something else, too.\n"

    $ default_mouse = "default"
    voice "audio/voices/ch3/wild/narrator/31.flac"
    n "You remember that you are a distinct being with a finite form and a mortal body. And you can feel it. There is a shifting of the space around you, the infinitesimal movement of your molecules rearranging back into the shape of what you're meant to be.\n"
    if trait_contrarian:
        voice "audio/voices/ch3/wild/contrarian/7.flac"
        contrarian "Finally, something is happening! I honestly didn't know what to make of all of this. Bit too metaphysical for me. It's hard to have a goof when you're stuck being metaphysical.\n"
    if trait_broken:
        if trait_broken:
            voice "audio/voices/ch3/wild/broken/3.flac"
            broken "I don't like this. It's better for us to be the woods. I don't want to go back.\n"

    if wild_source == "witch":
        $ renpy.music.set_volume(0.05, 0.5, channel='music')
        $ renpy.music.set_volume(1.0, 0.5, channel='music2')
        $ renpy.music.set_volume(0.5, 0.5, channel='music3')
        voice "audio/voices/ch3/wild/princess/25.flac"
        show bg wild woods angry onlayer back at screenshake
        show mid wild woods angry onlayer front at screenshake
        show fore wild woods angry onlayer inyourface at screenshake
        with hpunch
        swp "Maybe bygones can't be bygones. I don't know why I ever wanted to share a body with you of all things. It's like my very soul reeks of yours! That was horrible! This is better! Finally, I'll be able to hurt you like you deserve.\n"
        voice "audio/voices/ch3/wild/princess/26.flac"
        wp "I wish I didn't have to.\n"

    else:
        $ renpy.music.set_volume(0.05, 0.5, channel='music')
        $ renpy.music.set_volume(1.0, 0.5, channel='music2')
        $ renpy.music.set_volume(0.5, 0.5, channel='music3')
        voice "audio/voices/ch3/wild/princess/27.flac"
        show bg wild woods angry onlayer back at screenshake
        show mid wild woods angry onlayer front at screenshake
        show fore wild woods angry onlayer inyourface at screenshake
        with hpunch
        swp "No! I devoured you! I won! I put things back the way they were supposed to be!\n"

    $ achievement.grant("ACH_WILD_RIFT")
    voice "audio/voices/ch3/wild/narrator/32.flac"

    hide farback onlayer farback
    hide bg onlayer back
    hide mid onlayer front
    hide fore onlayer inyourface
    show farback wild wound onlayer farback at Position(ypos=1125)
    show farback wild onlayer back at Position(ypos=1125)
    show bg wild wound1 onlayer front at Position(ypos=1125)
    with Dissolve(1.0)
    $ renpy.pause(0.5)
    play audio "audio/final/Assorted_TapestyUnraveledBreakingRip_1.flac"
    voice sustain
    hide bg onlayer front
    hide farback onlayer back
    show mid wild wound2 onlayer back at Position(ypos=1125)
    show fore wild wound2 onlayer front at Position(ypos=1125)
    with Dissolve(1.0)
    n "Some divisions, when sown, can never truly be mended. A cavernous gash rips across whatever it was you thought you were.\n"
    play audio "audio/final/Assorted_TapestyUnraveledBreakingRip_2.flac"
    show mid wild wound3 onlayer back at Position(ypos=1125)
    show fore wild wound3 onlayer front at Position(ypos=1125)
    with Dissolve(1.0)
    $ renpy.pause(0.5)
    play audio "audio/final/Assorted_TapestyUnraveledBreakingRip_1.flac"
    hide farback onlayer farback
    hide fore onlayer front
    hide mid onlayer back
    show farback wild wound4 onlayer farback at Position(ypos=1125)
    show trees wild wound4 onlayer back at Position(ypos=1125)
    show cabin wild wound4 onlayer front at Position(ypos=1125)
    show tear wild wound4 onlayer inyourface at Position(ypos=1125)
    with Dissolve(1.0)
    play audio "audio/one_shot/door_bedroom.flac"
    $ renpy.pause(0.5)
    show cabin wild wound4 open onlayer front at Position(ypos=1125)
    $ renpy.pause(0.5)
    $ quick_menu = False
    voice "audio/voices/ch3/wild/narrator/33.flac"
    stop secondary fadeout 3.0
    stop sound fadeout 3.0
    hide farback onlayer farback
    hide trees onlayer back
    hide cabin onlayer front
    hide mid onlayer inyourface
    hide tear onlayer inyourface
    scene bg black
    n "A cabin comes into being among the trees. It approaches, and it swallows your body whole.\n"
    $ gallery_wild.unlock_item(3)
    $ renpy.save_persistent()
    voice "audio/voices/ch3/wild/narrator/34.flac"
    $ blade_held = True
    $ default_mouse = "blade"
    play audio "audio/one_shot/knife_pickup.flac"
    play tertiary "audio/final/fury_heart_loop.ogg" loop
    scene bg wild wound final onlayer farback at Position(ypos=1125)
    show wild wound final onlayer back at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    n "And then you find yourself, blade in hand, exactly where you need to be.\n"
    voice "audio/voices/ch3/wild/narrator/35.flac"
    show wild wound final look up onlayer back
    with dissolve
    n "At the center of it all is the Princess — a wooden and fleshy heart beating with an unbroken rhythm. You're filled with a sense of purpose. Strike at her. End this, once and for all.\n"
    if wild_source == "witch":
        voice "audio/voices/ch3/wild/princess/28.flac"
        show wild wound final talk onlayer back
        with dissolve
        p "Kill me, then, if you hate me so much. Just get it over with.\n"

    else:
        voice "audio/voices/ch3/wild/princess/29.flac"
        show wild wound final talk onlayer back
        with dissolve
        p "I feel empty. Don't you?\n"
    show wild wound final look up onlayer back
    with dissolve
    if trait_stubborn:
        voice "audio/voices/ch3/wild/stubborn/8a.flac"
        stubborn "This doesn't feel like a fight. This isn't what I wanted. Where's the victory in this?\n"
    if trait_broken:
        voice "audio/voices/ch3/wild/broken/4.flac"
        broken "We're just like her. And she's just like us. We never should have left her.\n"
    if trait_contrarian:
        #voice "audio/voices/ch3/wild/contrarian/8.flac"
        #contrarian "I don't think we should kill her. It would annoy Him if we didn't, right? And annoying Him is the only thing that matters.\n"
        voice "audio/voices/ch3/wild/contrarian/8.flac"
        contrarian "I don't think we should kill her. It would annoy Him if we didn't, right?\n"
    if trait_hunted:
        voice "audio/voices/ch3/wild/hunted/6.flac"
        hunted "I feel safe. She isn't dangerous anymore. We could leave her. We could both live.\n"
    if trait_paranoid:
        voice "audio/voices/ch3/wild/paranoid/4.flac"
        paranoid "I don't like this. What he wants us to do... it's just cruel. It feels like we'd be killing a part of ourself.\n"
    if trait_opportunist:
        voice "audio/voices/ch3/wild/opportunist/14.flac"
        opportunist "Well, this should be easy! If you're... sure about it. I mean, what's the point of being king of the hill if there's no one around to be better than? We'd just be sitting on a hill.\n"
    if trait_cheated:
        voice "audio/voices/ch3/wild/cheated/4.flac"
        cheated "This hardly seems fair to any one. It's an easy win if we want it, but I'm not sure whose win it is.\n"

    voice "audio/voices/ch3/wild/hero/10.flac"
    hero "Do we have to do this?\n"

    voice "audio/voices/ch3/wild/narrator/36.flac"
    n "You have to. You know you have to.\n"
    $ current_princess = "wildwound"
    menu:
        extend ""

        "{i}• ''I never wanted to kill you. Not really. But we can't be the same thing as each other. I had to put an end to whatever happened to us.'' [[Cut her free.]{/i}":
            voice "audio/voices/ch3/wild/narrator/37.flac"
            n "You devious little bastard. If you think I'm going to just let you free her, you have another thing coming.\n"
            if trait_cheated:
                voice "audio/voices/ch3/wild/cheated/5.flac"
                cheated "I know a bluff when I see one. He can use words, sure, but he doesn't have any real power.\n"
            elif trait_paranoid:
                voice "audio/voices/ch3/wild/paranoid/5.flac"
                paranoid "He's not in our head anymore. At least not like before. I don't think he can stop us now.\n"
            else:
                voice "audio/voices/ch3/wild/hero/11.flac"
                hero "And that other thing is...?\n"
                voice "audio/voices/ch3/wild/narrator/38.flac"
                n "You'll just have to wait and find out when it happens.\n"
            if trait_cheated or trait_paranoid:
                voice "audio/voices/ch3/wild/narrator/39.flac"
                n "I'm not bluffing. You won't be so smug when it happens.\n"
            if trait_stubborn:
                voice "audio/voices/ch3/wild/stubborn/9.flac"
                stubborn "Just ignore him. What's he going to do, lecture us into submission? He can talk all he wants.\n"
            elif trait_hunted:
                voice "audio/voices/ch3/wild/hunted/7.flac"
                hunted "Ignore him. His words only confuse us. Just do it.\n"
            if trait_opportunist:
                voice "audio/voices/ch3/wild/opportunist/15.flac"
                opportunist "He's weak. Thinks he can boss us around when he doesn't have any authority. We're clearly the ones with authority around here, so we can do whatever we like!\n"
            voice "audio/voices/ch3/wild/hero/12.flac"
            hero "You're tired, aren't you?\n"
            voice "audio/voices/ch3/wild/narrator/40.flac"
            n "No I'm not, I'm... fine. Whatever.\n"
            voice "audio/voices/ch3/wild/narrator/41.flac"
            play audio "audio/final/Adversary_StabCut_10.flac"
            hide bg onlayer farback
            hide wild onlayer farback
            scene bg wild wound cut onlayer farback at Position(ypos=1125)
            show wild wound cut onlayer back at Position(ypos=1125)
            with Dissolve(1.0)
            n "You cut the Princess down from the roots that bind her. I hope you're happy, and good luck getting her out of here.\n"
            stop sound fadeout 20.0
            stop secondary fadeout 20.0
            stop tertiary fadeout 20.0
            stop music fadeout 20.0
            stop music2 fadeout 20.0
            stop music3 fadeout 20.0
            stop music4 fadeout 20.0
            play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 20.0
            hide bg onlayer farback
            hide wild onlayer back
            scene bg wild wound free onlayer back at Position(ypos=1125)
            show quiet creep1 onlayer back at Position(ypos=1125)
            show wild wound free onlayer front at Position(ypos=1125)
            with Dissolve(1.0)
            if trait_contrarian:
                voice "audio/voices/ch3/wild/contrarian/9.flac"
                contrarian "Ha! That's right! Seethe at us! I thrive on your frustration!\n"
            if trait_broken:
                voice "audio/voices/ch3/wild/broken/5.flac"
                broken "I think we are happy, actually. We might not be part of her. But being around her is almost the same. Almost.\n"
            voice "audio/voices/ch3/wild/princess/30b.flac"
            show quiet creep2 onlayer back
            show wild wound free recognize onlayer front
            with Dissolve(1.0)
            p "I didn't think you would do that. After everything.\n"
            $ gallery_wild.unlock_item(4)
            $ gallery_wild.unlock_item(5)
            $ renpy.save_persistent()
            voice "audio/voices/ch3/wild/princess/31.flac"
            show quiet creep3 onlayer back
            show wild wound free cold talk onlayer front
            with Dissolve(1.0)
            p "It's... so cold without you.\n"
            play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
            show arms wound1 onlayer back at Position(ypos=1125)
            with Dissolve(1.0)
            $ renpy.pause(0.25)
            show wild wound quiet onlayer front
            show arms wound2 onlayer back
            with Dissolve(1.0)
            $ renpy.pause(0.25)
            hide wild onlayer front
            show arms wound3 onlayer back
            with Dissolve(1.0)
            $ renpy.pause(0.125)
            show arms wound4 onlayer back
            with Dissolve(0.5)
            $ renpy.pause(0.125)
            hide arms onlayer back
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
                truth "But you don't get the chance to respond, nor will you ever. It's time to leave. Memory returns.\n"
            else:
                truth "But you don't get the chance to respond. Something has taken her away, and it's left something else in her place.\n"
            $ wild_end = "separate"
            $ princess_kept += 1
            $ princess_satisfy += 1
            jump mirror_start
            # END

        "{i}• [[Slay the Princess.]{/i}":
            $ quick_menu = False
            voice "audio/voices/ch3/wild/narrator/42old.flac"
            play audio "audio/final/Tower_KnifeBlow_3.flac"
            hide bg onlayer farback
            hide wild onlayer farback
            scene bg wild wound slay onlayer farback at Position(ypos=1125)
            show wild wound slay onlayer back at Position(ypos=1125)
            with Dissolve(1.0)
            if persistent.quick_menu:
                $ quick_menu = True
            n "You raise the blade, taking aim at her heart. And then you strike.\n"
            $ gallery_wild.unlock_item(6)
            $ renpy.save_persistent()
            voice "audio/voices/ch3/wild/princess/32.flac"
            stop sound fadeout 15.0
            stop secondary fadeout 15.0
            stop tertiary fadeout 15.0
            stop music fadeout 15.0
            stop music2 fadeout 15.0
            stop music3 fadeout 15.0
            stop music4 fadeout 15.0
            play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 20.0
            hide bg onlayer farback
            hide wild onlayer back
            show bg wild wound final onlayer back at Position(ypos=1125)
            show quiet creep1 onlayer front at Position(ypos=1125)
            show wild wound slay talk onlayer front at Position(ypos=1125)
            with dissolve
            p "I'm sorry.\n"
            show quiet creep2 onlayer front
            show wildf wound slay cold talk onlayer front at Position(ypos=1125)
            with Dissolve(1.0)
            $ renpy.pause(1.0)
            play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
            hide wild onlayer front
            show arms wound1 onlayer front behind wildf at Position(ypos=1125)
            show quiet creep3 onlayer front behind arms
            with Dissolve(1.0)
            $ renpy.pause(0.5)
            $ renpy.pause(0.25)
            hide wildf onlayer front
            show wildf wound slay quiet onlayer front
            show arms wound2 onlayer front
            with Dissolve(1.0)
            $ renpy.pause(0.25)
            hide wild onlayer front
            hide wildf onlayer front
            show arms wound3 onlayer front
            with Dissolve(1.0)
            $ renpy.pause(0.125)
            show arms wound4 onlayer front
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
                truth "But you never see her die. It's time to leave. Memory returns.\n"
            else:
                truth "But you never see her die. Something has taken her away, and it's left something else in her place.\n"
            $ wild_end = "slay"
            $ princess_kept += 1
            $ princess_deny += 1
            jump mirror_start
            #END

label wild_side_princess:


    $ achievement.grant("ACH_WILD_FREE")
    voice "audio/voices/ch3/wild/narrator/43.flac"
    $ renpy.music.set_volume(0.05, 4.0, channel='music')
    $ renpy.music.set_volume(1.0, 4.0, channel='music2')
    $ renpy.music.set_volume(0.5, 4.0, channel='music3')
    hide bg onlayer back
    hide mid onlayer front
    hide fore onlayer inyourface
    with Dissolve(4.0)
    n "You fall inward, into a network of connections too vast for your mind to occupy. Are you a path in the woods? Are you a body? Can you even grasp the fuzziest edges of the shapes that confine you?\n"
    voice "audio/voices/ch3/wild/princess/33.flac"
    wp "We can change to fill them together.\n"
    if trait_hunted:
        voice "audio/voices/ch3/wild/hunted/8.flac"
        hunted "We don't need to be everywhere. We just need to test the boundaries.\n"
        if trait_opportunist:
            voice "audio/voices/ch3/wild/opportunist/16a.flac"
            opportunist "We just need to find the right place to be at the right time.\n"
    elif trait_opportunist:
        voice "audio/voices/ch3/wild/opportunist/17a.flac"
        opportunist "We don't need to be everywhere at once. Just in the right place at the right time.\n"
    voice "audio/voices/ch3/wild/narrator/44.flac"
    n "You'd do best to remember that some wounds will never heal. Some rifts can never be mended. Even in rebirth, some things never come back the same.\n"
    voice "audio/voices/ch3/wild/hero/13.flac"
    hero "What is he going on about? What does he know about us?\n"
    if trait_broken:
        voice "audio/voices/ch3/wild/broken/6.flac"
        broken "This is all too much. Why can't we just let her do as she sees fit? She's the one who can handle being vast. It's not for us. It's not for me.\n"
    if trait_stubborn:
        voice "audio/voices/ch3/wild/stubborn/10.flac"
        stubborn "He can't make us quit, no matter how much he tries. He knows that talking's all he can do. Of course he's going to try and confuse us.\n"
    if trait_contrarian:
        voice "audio/voices/ch3/wild/contrarian/10.flac"
        contrarian "Screw all of this, and screw this guy in particular! Always telling us what we can and can't do. Always going on and on about rules and the fate of the world. I've had enough!\n"
    if trait_cheated:
        voice "audio/voices/ch3/wild/cheated/6.flac"
        cheated "I think it's high time we all finally stopped listening to him. He doesn't actually make the rules. He's just flying by the seat of his pants like the rest of us.\n"
    voice "audio/voices/ch3/wild/narrator/45.flac"
    n "You aren't whole. You'll never be whole again. This struggle is meaningless. Whatever you think you're doing, you will fall apart.\n"
    voice "audio/voices/ch3/wild/princess/34a.flac"
    $ renpy.music.set_volume(0.8, 1.75, channel='music')
    $ renpy.music.set_volume(0.55, 1.75, channel='music2')
    $ renpy.music.set_volume(0.05, 1.75, channel='music3')
    wp "We don't need to be made whole. All we need to do is find a single corner of His cage and break it.\n"
    menu:
        extend ""

        "{i}• [[There is a place you need to be. You just need to find it.]{/i}":
            voice "audio/voices/ch3/wild/narrator/46.flac"
            play audio "audio/final/Witch_VinesTwist_1.flac"
            show wild nerves anim1 onlayer front at Position(ypos=1125)
            with Dissolve(2.0)
            play audio "audio/final/Tower_Earthquake_oneshot_faded_1.flac"
            hide farback onlayer farback
            show farback quiet onlayer farback at Position(ypos=1125)
            hide wild onlayer front
            with Dissolve(2.0)
            n "You stretch and search and stretch and search, growing as you decay and decaying as you grow. As you strain beyond your limits, the ground around you becomes dry and unstable and crumbles into nothing beneath you.\n"
            voice "audio/voices/ch3/wild/narrator/47.flac"

            n "This place will fall apart before you find its end.\n"
            voice "audio/voices/ch3/wild/narrator/48.flac"
            play audio "audio/final/Witch_TreeWrap_2.flac"
            show wild nerves anim2 onlayer front at Position(ypos=1125)
            with Dissolve(2.0)
            hide wild onlayer front
            with Dissolve(2.0)
            n "This task, whatever it is you think you're doing, is impossible.\n"

    if trait_paranoid:
        voice "audio/voices/ch3/wild/paranoid/6.flac"
        paranoid "He wouldn't be trying to discourage us if that were true.\n"
    if trait_hunted:
        voice "audio/voices/ch3/wild/hunted/9.flac"
        hunted "All he has are words. And words aren't real. We're real.\n"
    if trait_stubborn:
        voice "audio/voices/ch3/wild/stubborn/11.flac"
        stubborn "All the more reason to keep trying. Come on, we aren't tired yet!\n"
    if trait_opportunist:
        voice "audio/voices/ch3/wild/opportunist/18a.flac"
        opportunist "That's right. I know a loser when I see one. Call His bluff.\n"
    if trait_contrarian:
        voice "audio/voices/ch3/wild/contrarian/11.flac"
        contrarian "Yeah! Ruin His day!\n"

    voice "audio/voices/ch3/wild/princess/35.flac"
    hide wild onlayer front
    with Dissolve(1.0)
    wp "I can hold us together for a little while longer. So long as you trust me.\n"
    if trait_cheated:
        voice "audio/voices/ch3/wild/cheated/7.flac"
        cheated "It doesn't matter if the world is falling apart. It's time for us to commit to something.\n"
    if trait_broken:
        voice "audio/voices/ch3/wild/broken/7.flac"
        broken "Of course we do. To the ends of the earth.\n"
    menu:
        extend ""

        "{i}• I trust you. [[Find the way out.]{/i}":
            voice "audio/voices/ch3/wild/narrator/49.flac"
            play audio "audio/final/Witch_TreeWrap_4.flac"
            show wild nerves anim3 onlayer front at Position(ypos=1125)
            with Dissolve(2.0)
            hide wild onlayer front
            with Dissolve(2.0)
            n "You won't find anything. If I have to starve you, if I have to sacrifice my world to keep the Princess at bay, I'll do it.\n"
            hide farback onlayer farback
            hide wild onlayer front
            play audio "audio/final/Witch_TreeRootsConstricting_2.flac"
            show wild nerves anim4 onlayer back at Position(ypos=1125)
            with Dissolve(2.0)
            #n "You won't find anything. If I have to starve you, if I have to sacrifice my world to keep the Princess at bay, I'll do it. I'll do it all if that's what it takes to save everyone in every other world and all across every other possible existence.\n"
            truth "But you do find something. It's cold and smooth, and gently buckles, then cracks under the pressure of your consciousness flattening against it.\n"
            voice "audio/voices/ch3/wild/narrator/50.flac"
            n "Don't move an inch. Don't grow another blade of grass or harvest the remains of another dying creature so you can expand just that much further. Stop all of this right now!\n"
            voice "audio/voices/ch3/wild/hero/14.flac"
            hero "I think it's too late for that, mate.\n"
            voice "audio/voices/ch3/wild/princess/36.flac"
            wp "I'm at your side. Shatter it, and free us all.\n"
            menu:
                extend ""

                "{i}• [[Shatter the cage.]{/i}":
                    $ gallery_wild.unlock_item(2)
                    $ renpy.save_persistent()
                    voice "audio/voices/ch3/wild/narrator/51.flac"
                    play audio "audio/final/Assorted_MirrorBreaksLongShortBigSmall_7.flac"
                    scene reality ending
                    show wild nerves anim final onlayer back at shakeshort
                    with dissolve
                    n "No no no no no! Stop—\n{w=1.70}{nw}"
                    show screen disableclick(0.5)
                    truth "But His pleas disappear at the sound of breaking glass. For a moment, you and she gaze through the tiniest hole in the world at the place you need to be.\n"
                    if trait_paranoid:
                        voice "audio/voices/ch3/wild/paranoid/7.flac"
                        paranoid "We... we found it. I knew it. I knew there was something he was keeping from us. Is that really all it took?\n"
                    if trait_opportunist:
                        voice "audio/voices/ch3/wild/opportunist/19.flac"
                        opportunist "A job well done, team. Just like I'd planned.\n"
                        if trait_stubborn:
                            voice "audio/voices/ch3/wild/stubborn/12.flac"
                            stubborn "Oh, can it. This was all of us. Fighting as one.\n"
                    stop sound fadeout 15.0
                    stop secondary fadeout 15.0
                    stop tertiary fadeout 15.0
                    stop music fadeout 15.0
                    stop music2 fadeout 15.0
                    stop music3 fadeout 15.0
                    stop music4 fadeout 15.0
                    play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 20.0
                    voice "audio/voices/ch3/wild/princess/37.flac"
                    show quiet creep1 onlayer front at Position(ypos=1125)
                    with Dissolve(1.0)
                    wp "Is this what He kept from us? Is this why He made us kill each other?\n"
                    voice "audio/voices/ch3/wild/hero/15.flac"
                    show quiet creep2 onlayer front at Position(ypos=1125)
                    with Dissolve(1.0)
                    hero "It's beautiful.\n"
                    if trait_hunted:
                        voice "audio/voices/ch3/wild/hunted/10.flac"
                        hunted "We need to be there. We won't be safe until we are. We won't be whole.\n"
                    if trait_cheated:
                        voice "audio/voices/ch3/wild/cheated/8.flac"
                        cheated "He thought he could keep us blind forever. And he almost did.\n"
                    if trait_contrarian:
                        voice "audio/voices/ch3/wild/contrarian/12.flac"
                        contrarian "Eh... doesn't look that great. I like it better in here.\n"
                    if trait_stubborn and trait_opportunist == False:
                        voice "audio/voices/ch3/wild/stubborn/13.flac"
                        stubborn "This was all of us. Fighting as one.\n"
                    hide wild onlayer back
                    show quiet creep3 onlayer front at Position(ypos=1125)
                    show farback quiet onlayer farback at Position(ypos=1125)
                    with Dissolve(2.0)
                    truth "And then it's gone.\n"
                    voice "audio/voices/ch3/wild/princess/38.flac"
                    wp "Where did it go? Why is everything so cold?\n"
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
                        truth "But you never get the chance to answer her. You turn to see her gone behind you. Memory returns.\n"
                    else:
                        truth "But you never get the chance to answer her. You turn to see her gone behind you, replaced by something else.\n"
                    $ current_princess = "wildnerves"
                    $ wild_end = "joined"
                    $ princess_free += 2
                    $ princess_satisfy += 1
                    jump mirror_start
                    # end



return
