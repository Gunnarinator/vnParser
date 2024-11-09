label grey_start:

    # starting things up

    stop music
    stop sound
    stop secondary
    $ default_mouse = "default"
    $ blade_held = False
    $ current_loop = 3
    $ quick_menu = False
    $ config.menu_include_disabled = False
    $ grey_encountered = True

    default grey_mirror_previous = False
    default grey_mirror_touch_prev = False
    default grey_source = ""
    default grey_rush = ""

    play sound "audio/looping/uncomfortable ambiance heightened.ogg" loop fadein 1.0
    scene chapter grey with fade
    show text _("{color=#FFFFFF00}Chapter Three. The Grey.{/color}") at Position(ypos=850)
    $ renpy.pause(4.0)
    scene bg black

    $ gallery_grey.unlock_gallery()
    $ renpy.save_persistent()

    if current_princess == "damsel":
        $ grey_source = "damsel"
        $ current_princess = "greydamsel"
        $ trait_cold = True
        $ trait_smitten = True
        if damsel_1_cabin_mirror_ask or damsel_1_cabin_mirror_approached:
            $ grey_mirror_previous = True
        if damsel_1_cabin_mirror_approached:
            $ grey_mirror_touch_prev = True

        $ renpy.music.set_volume(0.0, 0.0, channel='music2')
        play sound "audio/looping/uncomfortable ambiance.ogg" loop
        play music "audio/_music/ch3/grey/The Grey Fire INTRO.flac"
        queue music "audio/_music/ch3/grey/The Grey Fire LOOP.flac" loop
        play music2 "audio/_music/ch3/grey/The Grey INTRO CHANT.flac"
        queue music2 "audio/_music/ch3/grey/The Grey LOOP CHANT.flac" loop
        scene farback grey fire woods onlayer farback at Position(ypos=1125)
        show bg grey fire woods onlayer back at Position(ypos=1125)
        show mid grey fire woods onlayer front at Position(ypos=1125)
        show fore grey fire woods onlayer inyourface at Position(ypos=1125)
        with fade

    else:
        play sound "audio/looping/uncomfortable ambiance.ogg" loop
        play secondary "audio/final/_grey_rain_2.ogg" loop
        play music "audio/_music/ch3/grey/The Grey Water INTRO FINAL.flac"
        queue music "audio/_music/ch3/grey/The Grey Water LOOP FINAL.flac" loop
        $ grey_source = "prisoner"
        $ trait_cold = True
        $ current_princess = "greyprisoner"
        $ trait_skeptic = True
        if prisoner_1_cabin_mirror_ask or prisoner_1_cabin_mirror_approached:
            $ grey_mirror_previous = True
        if prisoner_1_cabin_mirror_approached:
            $ grey_mirror_touch_prev = True

        scene farback grey water woods onlayer farback at Position(ypos=1125)
        show bg grey water woods onlayer back at Position(ypos=1125)
        show fore grey water woods onlayer front at Position(ypos=1125)
        show grey rain onlayer inyourface at Position(ypos=1125)
        with fade
    # smitten + cold from damsel route
    # skeptic + cold from prisoner
    if persistent.quick_menu:
        $ quick_menu = True
    # FAST
    voice "audio/voices/ch3/grey/narrator/1.flac"
    n "You're on a path in the woods—\n{w=1.8}{nw}"
    show screen disableclick(0.5)
    if trait_skeptic:
        voice "audio/voices/ch3/grey/skeptic/1.flac"
        skeptic "See? That wasn't so bad. And now we've got another chance to get to the bottom of things. Bit by bit we're starting to unravel this place.\n"
        voice "audio/voices/ch3/grey/cold/1.flac"
        cold "There are so many more threads to pull once you stop feeling.\n"
        voice "audio/voices/ch3/grey/hero/1.flac"
        hero "That's a little dark, buddy. Are you feeling okay?\n"
        voice "audio/voices/ch3/grey/cold/2.flac"
        cold "I'm feeling nothing. And I like that just fine.\n"
        #voice "audio/voices/ch3/grey/skeptic/2.flac"
        #skeptic "He's not wrong. Sentimentality won't help us here. We need scientific rigor.\n"
    else:
        voice "audio/voices/ch3/grey/smitten/1a.flac"
        smitten "You horrid monster! Do you think just because we've returned to the woods you've earned my forgiveness? Our beloved had best be alive and well when we return to the cabin, or you'll never know the end of my wrath.\n"
        voice "audio/voices/ch3/grey/cold/3.flac"
        cold "She won't be alive and well when we return to that cabin, because she's dead. We killed her.\n"
        voice "audio/voices/ch3/grey/smitten/2.flac"
        smitten "{i}You{/i} killed her! And so I killed you!\n"
        voice "audio/voices/ch3/grey/cold/4.flac"
        cold "And you clearly didn't do a good enough job. I'm still here.\n"
        voice "audio/voices/ch3/grey/hero/2.flac"
        hero "Oh, and I'm still here too.\n"
        voice "audio/voices/ch3/grey/smitten/3.flac"
        smitten "If you lot get to be blessed with seemingly eternal life, that must mean {i}she's{/i} still there, waiting for us to throw ourselves at her feet in remorse!\n"
        voice "audio/voices/ch3/grey/cold/5.flac"
        cold "I doubt it. I think I'm better at killing than you are.\n"

    voice "audio/voices/ch3/grey/narrator/2.flac"
    n "So you've been here before. Of course you've been here before. What count is it this time? Two?\n"
    voice "audio/voices/ch3/grey/cold/6.flac"
    cold "It's our third. What gave it away?\n"
    voice "audio/voices/ch3/grey/narrator/3.flac"
    n "Your open discussions.\n"
    if trait_skeptic:
        if prisoner_1_forest_share_loop_insist:
            voice "audio/voices/ch3/grey/skeptic/3.flac"
            skeptic "The last time we were here you were in full-blown denial about the possibility of us restarting. What changed? Have you just been... pretending to forget?\n"
        else:
            voice "audio/voices/ch3/grey/skeptic/4.flac"
            skeptic "You came around on that awful fast. Have you just been pretending to forget every time?\n"
        voice "audio/voices/ch3/grey/narrator/4.flac"
        n "I'm afraid not. Whatever other versions of me you've met in those other lifetimes were just that. Other versions of me. I just wish I'd been the first.\n"
        voice "audio/voices/ch3/grey/skeptic/5.flac"
        skeptic "So you knew how all this worked. Why didn't you ever tell us? We could have used it to our advantage.\n"
        voice "audio/voices/ch3/grey/narrator/5.flac"
        n "That's because there is no using it to your advantage. The more information you have, the harder it will be for you to succeed.\n"
        #if prisoner_decapitate:
        #    voice "audio/voices/ch3/grey/cold/7.flac"
        #    cold "You say that, but we didn't have to do anything last time. She slew herself.\n"
        #    voice "audio/voices/ch3/grey/hero/3.flac"
        #    hero "It was nauseating.\n"
        #    voice "audio/voices/ch3/grey/cold/8.flac"
        #    cold "Yes. She cut off her head.\n"
        #else:
        voice "audio/voices/ch3/grey/cold/9.flac"
        cold "It's not like it was that difficult to slay her last time. She may have put up a fight, but her flesh is still softer than our blade.\n"
        voice "audio/voices/ch3/grey/cold/10.flac"
        cold "And now she's dead. And I doubt she'll be able to do much of anything from the grave.\n"
        #if prisoner_decapitate == False:
        voice "audio/voices/ch3/grey/narrator/6.flac"
        n "You already slew her? And you survived?\n"
        #else:
        #    voice "audio/voices/ch3/grey/narrator/7.flac"
        #    n "She cut off her head? {i}Her{/i} head? Without you doing anything?\n"
        voice "audio/voices/ch3/grey/cold/11.flac"
        cold "Yes.\n"
        voice "audio/voices/ch3/grey/narrator/8.flac"
        n "Then why, pray tell, are you here?\n"
        if prisoner_heart_stop:
            voice "audio/voices/ch3/grey/hero/4.flac"
            hero "Oh, I know that one! The gruff one stopped our heart, and we died.\n"
        else:
            voice "audio/voices/ch3/grey/hero/5.flac"
            hero "Oh, I know that one! We killed ourself.\n"
        voice "audio/voices/ch3/grey/narrator/9.flac"
        n "Why?!\n"
        voice "audio/voices/ch3/grey/cold/12.flac"
        cold "Because you thought trying to stuff us away in a corner for eternity was a suitable reward.\n"
        voice "audio/voices/ch3/grey/narrator/10.flac"
        n "Was it not? What better reward is there than eternal bliss? You should have been happy.\n"
        #voice "audio/voices/ch3/grey/skeptic/6.flac"
        #skeptic "We weren't.\n"
        voice "audio/voices/ch3/grey/cold/13.flac"
        cold "We were bored.\n"
        #voice "audio/voices/ch3/grey/hero/6a.flac"
        #hero "You were bored. I was just unhappy.\n"
        voice "audio/voices/ch3/grey/skeptic/7.flac"
        skeptic "There were still answers that we needed to find.\n"
        voice "audio/voices/ch3/grey/narrator/11.flac"
        n "It was actually working... and you killed yourself. I can't believe it. You ruined everything!\n"
        voice "audio/voices/ch3/grey/skeptic/8.flac"
        skeptic "How does us dying ruin everything? What aren't you telling us?!\n"
        #voice "audio/voices/ch3/grey/narrator/12.flac"
        #n "It just does. And I'm not telling you lots of things! But it's for your own good. It's for the good of {i}everyone{/i}.\n"
        #voice "audio/voices/ch3/grey/skeptic/9.flac"
        #skeptic "It seems to me like keeping secrets didn't help you last time. So you should start talking.\n"
        voice "audio/voices/ch3/grey/narrator/13a.flac"
        n "The world doesn't stay saved if you die!\n"
        #n "Fine! The world doesn't stay saved if you die!\n"
        voice "audio/voices/ch3/grey/skeptic/10.flac"
        skeptic "And if the world isn't saved, then that means she isn't dead.\n"
        #voice "audio/voices/ch3/grey/cold/14.flac"
        #cold "Oh, now isn't {i}that{/i} interesting? I assumed she'd just be a pile of old bones, but perhaps she's not. There's only one way to find out. We should go see her.\n"
        #voice "audio/voices/ch3/grey/skeptic/11.flac"
        #skeptic "Let's try something different this time. We've already seen what happens when we slay her, and I'm not convinced that's a way out for us. I'm not even convinced there is a world to save.\n"

    else:
        voice "audio/voices/ch3/grey/smitten/4.flac"
        smitten "I couldn't care less about what he knows. Every second we stand around arguing in the woods is a second that I'm anxiously worrying about {i}her{/i}. Take us to the cabin, and take us there now! With each passing moment our relationship may be damaged even further... though I fear the rift between us may already be permanent.\n" id grey_start_423dedf1
        voice "audio/voices/ch3/grey/cold/15.flac"
        cold "And if it is permanent, then what? You'll kill us again?\n"
        voice "audio/voices/ch3/grey/smitten/5.flac"
        smitten "Oh, just you wait and see! My vengeance will echo the depths of my bereavement!\n"
        voice "audio/voices/ch3/grey/hero/7.flac"
        hero "Don't provoke him. I'd prefer it if we didn't die again. I'm not fond of dying.\n"
        voice "audio/voices/ch3/grey/cold/16.flac"
        cold "Why not? You've already done it twice.\n"
        voice "audio/voices/ch3/grey/hero/8a.flac"
        hero "It was unpleasant.\n"
        voice "audio/voices/ch3/grey/cold/17b.flac"
        cold "It was only unpleasant because you think it's supposed to be unpleasant.\n"
        voice "audio/voices/ch3/grey/smitten/6.flac"
        smitten "I'll make you feel what I feel if it's the last thing I do! And mark my words, you won't like it when it happens!\n"
        voice "audio/voices/ch3/grey/cold/18.flac"
        cold "Oh, how exciting. I'd love to see you try.\n"
        # FAST
        voice "audio/voices/ch3/grey/narrator/14.flac"
        n "Can I—\n{w=0.255}{nw}"
        show screen disableclick(0.5)
        voice "audio/voices/ch3/grey/smitten/7a.flac"
        smitten "Well I'm not just going to try. I'm going to actually do it!\n"
        voice "audio/voices/ch3/grey/cold/19.flac"
        cold "I'm looking forward to it.\n"
        voice "audio/voices/ch3/grey/smitten/8.flac"
        smitten "Good! I am, too!\n"
        voice "audio/voices/ch3/grey/narrator/15.flac"
        n "Can I talk now? Yes. I can. Great. Now that you're listening, let me remind you that if you're here, in the woods, it means that the Princess is not dead, and that her very existence currently poses a direct threat to the entire world.\n"
        #voice "audio/voices/ch3/grey/cold/20.flac"
        #cold "I'll believe that when I see her living body.\n"
        #voice "audio/voices/ch3/grey/smitten/9.flac"
        #smitten "Did I hear that right? He says she's alive! Our beloved lives again!\n"
        #voice "audio/voices/ch3/grey/narrator/16.flac"
        #n "Yes. She's alive, but you're going to have to make her not alive. You'll have to slay her. It's your job.\n"
        #voice "audio/voices/ch3/grey/smitten/10.flac"
        #smitten "We absolutely will not! This is a tale of love and redemption, and this time, it will not end in bloodshed! Except ours, if any of you try anything.\n"
        #voice "audio/voices/ch3/grey/hero/9.flac"
        #hero "Let's do our best to keep him away from anything sharp. If we're lucky, there won't even be a blade when we get to the cabin.\n"

label grey_woods_menu:
    default grey_woods_different = False
    default grey_woods_no_cabin = False
    default grey_woods_charge = False
    menu:
        extend ""

        "{i}• (Explore) It's raining. It wasn't raining last time. Or the time before that. The whole path is different.{/i}" if trait_skeptic and grey_woods_different == False:
            voice "audio/voices/ch3/grey/skeptic/12.flac"
            skeptic "Yes, things are different, aren't they?\n"
            jump grey_woods_different_join

        "{i}• (Explore) We haven't talked enough about how different this place is. It wasn't different last time.{/i}" if grey_woods_different == False:
            label grey_woods_different_join:
                $ grey_woods_different = True
                voice "audio/voices/ch3/grey/narrator/17.flac"
                n "If this isn't the same path in the woods you're used to, that means that her influence is already spreading, and you're running out of time.\n"
                if trait_skeptic:
                    voice "audio/voices/ch3/grey/skeptic/13.flac"
                    skeptic "Her influence? What's that supposed to mean?\n"
                    voice "audio/voices/ch3/grey/narrator/18.flac"
                    n "It means exactly what I said. Don't overthink it, or you run the risk of making your task so much more difficult than it has to be.\n"
                    voice "audio/voices/ch3/grey/skeptic/14.flac"
                    skeptic "And what is {i}that{/i} supposed to mean?\n"
                    voice "audio/voices/ch3/grey/narrator/19.flac"
                    n "{i}Sigh{/i}. Forget I said anything. I've probably already made things worse. And I need to stop talking about this now before I definitely make things worse.\n"
                    voice "audio/voices/ch3/grey/hero/10.flac"
                    hero "Oh, come on! Tell us your secrets. Haven't we been through enough? Don't we deserve to know?\n"
                    voice "audio/voices/ch3/grey/narrator/20.flac"
                    n "No.\n"
                    voice "audio/voices/ch3/grey/skeptic/15.flac"
                    skeptic "Is there a reason it would be raining?\n"
                    voice "audio/voices/ch3/grey/cold/21.flac"
                    cold "If there is, it doesn't matter. If a bit of rain is the best her 'influence' can conjure, then we have nothing to worry about. A drenched corpse is still a corpse.\n"
                else:
                    voice "audio/voices/ch3/grey/smitten/11.flac"
                    smitten "Wait... but if her influence is spreading, that means there's hope! That means our beloved is waiting up there for us, ready to make amends!\n"
                    voice "audio/voices/ch3/grey/narrator/21.flac"
                    n "Yes, I already told you that she's alive.\n"
                    voice "audio/voices/ch3/grey/hero/11.flac"
                    hero "Don't mind him. I don't think he's doing too well.\n"
                    voice "audio/voices/ch3/grey/smitten/12.flac"
                    smitten "I'm doing better than any of you! I'm doing great! She's alive!\n"
                    voice "audio/voices/ch3/grey/cold/22.flac"
                    cold "'Influence' doesn't require life.\n"
                    voice "audio/voices/ch3/grey/hero/12a.flac"
                    hero "But if things restarted, why wouldn't she be alive?\n"
                    voice "audio/voices/ch3/grey/cold/23.flac"
                    cold "Who said they restarted? All they've done is changed.\n"
                    voice "audio/voices/ch3/grey/smitten/13.flac"
                    smitten "I shan't listen to the vile mutterings of you serpents. Onward! Our living, breathing Princess awaits us!\n"
                jump grey_woods_menu

        "{i}• (Explore) What happens if we don't go to the cabin?{/i}" if grey_woods_no_cabin == False:
            $ grey_woods_no_cabin = True
            voice "audio/voices/ch3/grey/narrator/22.flac"
            n "She'll find a way out eventually, and the world will still end. The only way this resolves is if you find her and slay her before that happens.\n"
            if trait_skeptic:
                voice "audio/voices/ch3/grey/skeptic/16.flac"
                skeptic "We already know He wants us to slay her. Anything He says is tainted by His motivations.\n" id grey_woods_different_join_73e4f4ab
            else:
                voice "audio/voices/ch3/grey/smitten/14.flac"
                smitten "Again, He makes her out to be a monster. I'm tired of all this slander! She's never hurt anyone in her life except for us, and that was our fault.\n" id grey_woods_different_join_b5674429
                voice "audio/voices/ch3/grey/hero/13.flac"
                hero "We don't know that, she could have done all sorts of things we weren't around to see.\n"
            voice "audio/voices/ch3/grey/cold/24.flac"
            cold "Turn around and leave, go to the cabin, I'm fine with either. So long as we don't just do the same thing again. That would be boring.\n"
            jump grey_woods_menu

        "{i}• (Explore) I'm the one in charge here, and if we slay her again, you are not going to make us kill ourself. Is that clear?{/i}" if trait_smitten and grey_woods_charge == False:
            $ grey_woods_charge = True
            voice "audio/voices/ch3/grey/smitten/15.flac"
            smitten "Oh, it's clear, you murderer. Though I should remind you that you're not as 'in charge' as you seem to think you are.\n"
            voice "audio/voices/ch3/grey/cold/25.flac"
            cold "I'm sure his outburst last time was just a fluke. I wouldn't worry about him. Besides, if he kills us again, he kills us again. It doesn't matter. He'll tire out eventually. The flame of passion always burns out in the end.\n"
            voice "audio/voices/ch3/grey/smitten/16.flac"
            smitten "Spoken like a true cynic.\n"
            voice "audio/voices/ch3/grey/narrator/23.flac"
            n "Enough bickering. Just stay focused, and get to the cabin.\n"
            jump grey_woods_menu

        "{i}• (Explore) I'll have you know that I didn't want to kill myself last time.{/i}" if prisoner_heart_stop and grey_woods_charge == False:
            $ grey_woods_charge = True
            voice "audio/voices/ch3/grey/narrator/24.flac"
            n "That's great to hear, but it doesn't matter, because you still died.\n"
            voice "audio/voices/ch3/grey/skeptic/17.flac"
            skeptic "No hard feelings, right?\n"
            voice "audio/voices/ch3/grey/cold/26.flac"
            cold "Of course not. No feelings at all.\n"
            voice "audio/voices/ch3/grey/hero/14.flac"
            hero "Speak for yourself.\n"
            voice "audio/voices/ch3/grey/skeptic/18.flac"
            skeptic "What, you wanted us to stay in the happiness void forever? I doubt that.\n"
            jump grey_woods_menu

        "{i}• Whatever happens next, it seems like all our answers are in the cabin. We might as well see this through. [[Proceed to the cabin.]{/i}":
            jump grey_cabin_exterior

        "{i}• I'm done with this. Bye! [[Turn around and leave.]{/i}" if mound_can_attempt_flee:
            if loops_finished >= 2:
                $ mound_can_attempt_flee = False
                voice "audio/voices/mound/bonus/flee.flac"
                mound "You have already committed to my completion. You cannot go further astray.\n"
                jump grey_woods_menu
            $ caught_origin_ch3 = True
            if trait_skeptic:
                voice "audio/voices/ch3/grey/skeptic/19.flac"
                skeptic "Sure. We've already seen what happens if we slay her, we might as well explore our surroundings. Get a lay of the land.\n"
            else:
                voice "audio/voices/ch3/grey/smitten/17.flac"
                smitten "You can't run from your consequences forever. One way or another, you'll have to face what you've done!\n"
            voice "audio/voices/ch3/grey/cold/27.flac"
            stop sound fadeout 20.0
            stop tertiary fadeout 20.0
            stop music fadeout 20.0
            stop music2 fadeout 20.0
            play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 20.0
            $ quick_menu = False
            if grey_source == "prisoner":
                play audio "audio/final/_wet_step.flac"
                hide grey onlayer inyourface
                show farback grey water woods onlayer farback at zoom_in, flip, Position(ypos=1125)
                show bg grey water woods onlayer back at zoom_in, flip, Position(ypos=1125)
                show fore grey water woods onlayer front at zoom_in, flip, Position(ypos=1125)
                show grey rain onlayer inyourface at Position(ypos=1125)
            else:
                play audio "audio/one_shot/footsteps_hike_short.flac"
                show farback grey fire woods onlayer farback at zoom_in, flip, Position(ypos=1125)
                show bg grey fire woods onlayer back at zoom_in, flip, Position(ypos=1125)
                show mid grey fire woods onlayer front at zoom_in, flip, Position(ypos=1125)
                show fore grey fire woods onlayer inyourface at zoom_in, flip, Position(ypos=1125)
            show quiet creep1 onlayer inyourface at Position(ypos=1125)
            with fade
            if persistent.quick_menu:
                $ quick_menu = True
            cold "Let's see what we can find. It's bound to be more interesting than doing the same thing over again.\n"
            voice "audio/voices/ch3/grey/narrator/25a.flac"
            n "Wait... something isn't right. Can you still hear me? You're supposed to wind up back at the cabin again, but everything is getting... fuzzy.\n"
            voice "audio/voices/ch3/grey/hero/15.flac"
            show quiet creep2 onlayer inyourface
            with Dissolve(2.0)
            hero "W-what's going on? Where are we?\n"
            voice "audio/voices/ch3/grey/cold/28.flac"
            cold "I don't know. But it feels like home.\n"
            if trait_skeptic:
                voice "audio/voices/ch3/grey/skeptic/20.flac"
                show quiet creep3 onlayer inyourface
                with Dissolve(2.0)
                skeptic "Did we do this? Is this the end of the world? Was there ever even a world to end?\n"
            else:
                voice "audio/voices/ch3/grey/smitten/18.flac"
                show quiet creep3 onlayer inyourface
                with Dissolve(2.0)
                smitten "Of course. Oblivion is what we deserve.\n"
            hide grey onlayer inyourface
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


label grey_cabin_exterior:
    $ quick_menu = False
    if grey_source == "prisoner":
        $ gallery_grey.unlock_item(1)
        $ renpy.save_persistent()
        play audio "audio/final/_wet_step.flac"
        hide farback onlayer farback
        hide bg onlayer back
        hide fore onlayer front
        hide grey onlayer inyourface
        with fade
        show farback grey water ext onlayer farback at Position(ypos=1125)
        show bg grey water ext onlayer back at Position(ypos=1125)
        show mid grey water ext onlayer back at Position(ypos=1125)
        show fore grey water ext onlayer front at Position(ypos=1125)
        show grey rain onlayer inyourface at Position(ypos=1125)
    else:
        $ gallery_grey.unlock_item(2)
        $ renpy.save_persistent()
        play audio "audio/one_shot/footsteps_hike_short.flac"
        hide farback onlayer farback
        hide bg onlayer back
        hide mid onlayer front
        hide fore onlayer inyourface
        with fade
        show farback grey fire ext onlayer farback at Position(ypos=1125)
        show bg grey fire ext onlayer back at Position(ypos=1125)
        show mid grey fire ext onlayer back at Position(ypos=1125)
        show fore grey fire ext onlayer front at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True

    voice "audio/voices/ch3/grey/narrator/26.flac"
    n "I'm sure you've already heard my words of warning in one of your 'past lives.' You've already managed to slay her once, just... {i}sigh.{/i}. Don't muck it up this time, all right?\n"
    if trait_skeptic:
        voice "audio/voices/ch3/grey/skeptic/21.flac"
        skeptic "What we do is entirely up to us.\n"
        voice "audio/voices/ch3/grey/cold/29.flac"
        cold "And we have all those mysteries to unravel, isn't that right?\n"
        voice "audio/voices/ch3/grey/narrator/27.flac"
        n "You aren't here to solve a mystery. You're here to save the world.\n"
        voice "audio/voices/ch3/grey/skeptic/22.flac"
        skeptic "That's what you say, but how can we be sure?\n"
        voice "audio/voices/ch3/grey/cold/30.flac"
        cold "We can't be sure of anything except what's right in front of us.\n"
        voice "audio/voices/ch3/grey/hero/16.flac"
        hero "Okay, but... we {i}should{/i} care about the fate of the world.\n"
        voice "audio/voices/ch3/grey/cold/31.flac"
        cold "Why?\n"
        voice "audio/voices/ch3/grey/hero/17a.flac"
        hero "Because... because we should! I don't know. It's important.\n"
        voice "audio/voices/ch3/grey/cold/32a.flac"
        cold "Is it?\n"
        voice "audio/voices/ch3/grey/hero/18.flac"
        hero "Yes! ... I think?\n"
        #voice "audio/voices/ch3/grey/narrator/28.flac"
        #n "Don't let them make you second guess yourself. The fate of the world is the most important thing there is.\n"
        voice "audio/voices/ch3/grey/skeptic/23.flac"
        skeptic "For all we know, 'the world' you're talking about isn't even real.\n"
        voice "audio/voices/ch3/grey/narrator/29.flac"
        n "Of course it's real! Where do you think you are, somewhere else?\n"
        voice "audio/voices/ch3/grey/skeptic/24.flac"
        skeptic "Maybe we are.\n"
    else:
        voice "audio/voices/ch3/grey/smitten/19.flac"
        smitten "Oh, we'll muck it up, all right. We'll get our happy ending, even if it damns each and every person who's ever lived!\n"
        voice "audio/voices/ch3/grey/narrator/30.flac"
        n "{i}Sigh{/i}. Whatever you do, don't let him influence a single decision. He's clearly lost it.\n"
        voice "audio/voices/ch3/grey/hero/19.flac"
        hero "I hate that I'm agreeing with Him on anything, but I really don't like being at the whims of someone so... unstable. It's stressful.\n"
        voice "audio/voices/ch3/grey/cold/33.flac"
        cold "Yes, having all of those feelings isn't very productive, is it? But we're just passengers here. Why stress over something you can't control?\n"
        voice "audio/voices/ch3/grey/hero/20.flac"
        hero "You're saying that like stress is just something you can turn off.\n"
        voice "audio/voices/ch3/grey/cold/34.flac"
        cold "It is. It's easy. Whatever happens, happens.\n"
        voice "audio/voices/ch3/grey/smitten/20.flac"
        smitten "Are you even alive? What's the point of doing anything if you're not going to feel a single emotion.\n"
        voice "audio/voices/ch3/grey/cold/35.flac"
        cold "I don't know. I just exist, and that's fine with me.\n"

    voice "audio/voices/ch3/grey/narrator/31.flac"
    n "This is horribly unproductive. The cabin—and your extremely important destiny—await.\n"

    menu:

        extend ""

        "{i}• [[Proceed into the cabin.]{/i}":
            if grey_source == "prisoner":
                stop secondary fadeout 2.0
            play audio "audio/one_shot/door_bedroom.flac"
            hide farback onlayer farback
            hide bg onlayer back
            hide mid onlayer front
            hide fore onlayer inyourface
            hide farback onlayer farback
            hide bg onlayer back
            hide bg onlayer front
            hide mid onlayer back
            hide fore onlayer front
            hide grey onlayer inyourface
            scene bg black
            with fade
            jump grey_cabin

label grey_cabin:
    if grey_source == "prisoner":
        $ gallery_grey.unlock_item(3)
        $ renpy.save_persistent()
        play secondary "audio/final/_grey_rain_inside.ogg" loop
        scene farback cabin grey water onlayer farback at Position(ypos=1125)
        show bg cabin grey water onlayer back at Position(ypos=1125)
        show mirror grey distant onlayer back at Position(ypos=1125)
        show grey p upstairs onlayer back at Position(ypos=1125, xpos=750)
    else:
        $ gallery_grey.unlock_item(4)
        $ renpy.save_persistent()
        play secondary "audio/looping/ambient_cabin.ogg" loop fadein 1.0
        scene farback cabin grey fire onlayer farback at Position(ypos=1125)
        show bg cabin grey fire onlayer back at Position(ypos=1125)
        show mirror grey distant onlayer back at Position(ypos=1125)
        show grey d upstairs onlayer back at Position(ypos=1125, xpos=750)
    with fade
    if trait_skeptic:
        voice "audio/voices/ch3/grey/narrator/32.flac"
        n "As soon as you enter the cabin, you're struck by an overwhelming scent of decay, of mold and death and stagnant water. The once-stately wooden building is bloated, its beams dripping with a black ooze of putrefaction, all but the exterior stone walls warped beyond recognition. It must have been beautiful once. But in its ruin, it is beyond repulsive.\n"
        voice "audio/voices/ch3/grey/narrator/33.flac"
        n "But you're not alone. You can feel something watching you. There is a figure faintly outlined against the rotting wood of the wall.\n"
    else:
        voice "audio/voices/ch3/grey/narrator/34.flac"
        n "The interior of the cabin feels dry and brittle. Ancient dust-covered wooden beams hold up a crumbling ceiling like mummified ribs, each elegantly carved detail of the stately building preserved in an extended stasis. Everything here has been kept safe and dry and lifeless.\n"
        voice "audio/voices/ch3/grey/narrator/35.flac"
        n "But you're not alone. You can feel something watching you. There is a figure faintly outlined against the dusty wood of the far wall.\n"
    voice "audio/voices/ch3/grey/hero/21.flac"
    hero "Is that... {i}her{/i}?\n"
    if trait_smitten:
        voice "audio/voices/ch3/grey/smitten/21.flac"
        smitten "Our beloved. So she does live!\n"
        voice "audio/voices/ch3/grey/cold/36.flac"
        cold "She doesn't look very alive to me.\n"
    else:
        voice "audio/voices/ch3/grey/skeptic/25.flac"
        skeptic "It's like she isn't even there.\n"
        voice "audio/voices/ch3/grey/cold/37.flac"
        cold "See? We killed her.\n"
        voice "audio/voices/ch3/grey/skeptic/26.flac"
        skeptic "You're right. Maybe she doesn't reset like us. She certainly doesn't look the same as she did last time.\n"
    voice "audio/voices/ch3/grey/narrator/36.flac"
    hide grey onlayer back
    with dissolve
    n "Before you can make a move, the figure is gone, vanishing behind the door on the far side of the room.\n"
    if grey_mirror_previous:
        voice "audio/voices/ch3/grey/hero/22.flac"
        hero "The door at the end of the room? But there isn't a door. There's just that damn mirror again.\n"
        if trait_skeptic:
            voice "audio/voices/ch3/grey/skeptic/27a.flac"
            skeptic "Yes, the mirror that he 'can't see.'\n"
        else:
            voice "audio/voices/ch3/grey/smitten/22.flac"
            smitten "Ah, yes. The mirror. So we can see the monster we've become. If it even lets us look before it vanishes, too.\n"
    else:
        voice "audio/voices/ch3/grey/hero/23.flac"
        hero "The door at the end of the room? But there isn't a door. There's a mirror, that's it.\n"

    voice "audio/voices/ch3/grey/narrator/37.flac"
    n "The mirror? Is this some kind of joke? Did you all plan this out before dying? There is no mirror. There's the door to the basement, the table, and the pristine blade—\n{w=9.5}{nw}"
    show screen disableclick(0.5)
    voice "audio/voices/ch3/grey/narrator/38.flac"
    n "Huh. That's strange. There's supposed to be a pristine blade. Why isn't there a pristine blade?\n"
    if prisoner_decapitate:
        voice "audio/voices/ch3/grey/cold/38a.flac"
        cold "Maybe it's gone because she already killed herself with it.\n"
    else:
        voice "audio/voices/ch3/grey/cold/38b.flac"
        cold "Maybe it's gone because we've already killed her with it.\n"
    if trait_skeptic:
        voice "audio/voices/ch3/grey/hero/24.flac"
        hero "But we had it with us when we died. And besides, everything else has reset. Why wouldn't the blade have reset, too?\n"
        voice "audio/voices/ch3/grey/skeptic/28.flac"
        skeptic "Maybe it's because we've already explored that avenue. We've seen what happens when we slay her. Maybe this place has decided we don't need to try that again.\n"
    else:
        voice "audio/voices/ch3/grey/smitten/23.flac"
        smitten "Perhaps it's gone because an oh-so-deserved guilt has started to worm its way into each and every one of you. Perhaps all of you do feel just as bad as I about what we've done! Though if you felt the oppressive guilt I feel, we would have manifested that weapon directly into our heart.\n"
    voice "audio/voices/ch3/grey/narrator/39.flac"
    n "I suppose it doesn't matter why the blade is gone, but you're going to have to find it if you're going to do this right. So why don't you march over to that door, and make your way down to the basement?\n"
    label grey_cabin_mirror:
        default grey_no_door = False
        menu:
            extend ""

            "{i}• (Explore) ''But there is no door.''{/i}" if grey_no_door == False:
                $ grey_no_door = True
                if trait_skeptic:
                    if grey_mirror_previous:
                        if grey_mirror_touch_prev:
                            voice "audio/voices/ch3/grey/skeptic/29.flac"
                            skeptic "If this is anything like last time, the mirror will disappear as soon as we try and touch it. I'm sure the door is just behind it.\n"
                        else:
                            voice "audio/voices/ch3/grey/skeptic/30.flac"
                            skeptic "If this is anything like last time, the mirror will disappear when we try and go to the basement. I'm sure the door is just behind it.\n"
                    else:
                        voice "audio/voices/ch3/grey/skeptic/31.flac"
                        skeptic "Maybe the mirror isn't real. Maybe it is real, and He's lying through his teeth to stop us from looking into it. But it seems like whatever we want to do, our next step is on the other side of the room.\n"

                else:
                    voice "audio/voices/ch3/grey/smitten/24.flac"
                    smitten "As if something as flimsy as a missing door would stop us on our sacred quest! Cross the room. Find our way back to her. Make things right.\n"
                voice "audio/voices/ch3/grey/narrator/40.flac"
                n "You're clearly hallucinating. But I'd rather not get into it with you right now. The door to the basement is on the far side of the room, whether you can see it or not.\n"
                #voice "audio/voices/ch3/grey/hero/25.flac"
                #hero "Let's just take a look.\n"
                jump grey_cabin_mirror

            "{i}• [[Approach the mirror.]{/i}":
                voice "audio/voices/ch3/grey/narrator/41.flac"
                play audio "audio/one_shot/footsteps_creaky.flac"
                hide farback onlayer farback
                hide bg onlayer back
                hide mirror onlayer back
                if trait_skeptic:
                    scene door grey p close onlayer back at Position(ypos=1125)
                else:
                    scene door grey d close onlayer back at Position(ypos=1125)
                show mirror grey close onlayer back at Position(ypos=1125)
                with dissolve
                n "You make your way to the door at the end of the room, stopping just in front of it. You must think you're looking at that 'mirror' you mentioned earlier. The one that doesn't exist. {i}Sigh{/i} Just reach forward and open the door.\n"
                if grey_mirror_touch_prev:
                    voice "audio/voices/ch3/grey/hero/26.flac"
                    hero "It's still so hazy. We should try and clean it off.\n"
                    voice "audio/voices/ch3/grey/cold/39.flac"
                    cold "Yes, trying to touch it does seems to be the magic spell to get it out of our way.\n"
                    if trait_skeptic:
                        voice "audio/voices/ch3/grey/skeptic/32.flac"
                        skeptic "Maybe it won't disappear this time and we'll finally get a good look at ourselves. We should explore every option.\n"
                else:
                    voice "audio/voices/ch3/grey/hero/27.flac"
                    hero "It's so hazy. We should try and clean it off.\n"

                menu:
                    extend ""

                    "{i}• [[Wipe the mirror clean.]{/i}":
                        if trait_smitten:
                            voice "audio/voices/ch3/grey/smitten/25.flac"
                            smitten "It's time for all of you to see what we've become.\n"
                        voice "audio/voices/ch3/grey/narrator/42a.flac"
                        hide mirror onlayer back
                        play audio "audio/one_shot/new/STP_claws_1.flac"
                        show player grey door close onlayer back at Position(ypos=1125) with dissolve
                        n "You reach forward and place your hand on the door to the basement. The handle is just a little to your right, and a little down.\n"
                        if trait_skeptic:
                            voice "audio/voices/ch3/grey/skeptic/33.flac"
                            skeptic "Yeah. We can see it now.\n"
                        voice "audio/voices/ch3/grey/cold/40.flac"
                        hide player onlayer back
                        with dissolve
                        cold "So much for our reflection. We didn't need to see ourselves anyway. I'm much more interested in seeing other things.\n"
                        if trait_smitten:
                            voice "audio/voices/ch3/grey/smitten/26.flac"
                            smitten "I see... we are too hideous for even a mirror to behold. We can only hope she might still see some good in us.\n"
                        voice "audio/voices/ch3/grey/hero/28.flac"
                        hero "No way left to go but down.\n"
                        menu:
                            extend ""

                            "{i}• [[Enter the basement.]{/i}":
                                play audio "audio/one_shot/door_bedroom.flac"
                                $ quick_menu = False
                                hide door onlayer back
                                scene bg black
                                with fade
                                jump grey_stairs

label grey_stairs:
    $ current_run_mirror_comment = True
    if trait_skeptic:
        voice "audio/voices/ch3/grey/narrator/43.flac"
        show bg grey p stairs onlayer back at Position(ypos=1125)
        show grey p downstairs onlayer back at Position(ypos=1125)
        with fade
        if persistent.quick_menu:
            $ quick_menu = True
        n "The door to the basement groans open. The air is foul and wet, so thick that you can almost feel it settle onto your skin in layers of grime. The stairs are coated with slimy algae, the wood rotted through in places, reeking of fetid vegetation.\n"
        voice "audio/voices/ch3/grey/narrator/44.flac"
        n "A wispy figure watches you from the bottom of the stairs, face veiled in shadows, legs submerged up to her shins in dark waters.\n"
    else:
        voice "audio/voices/ch3/grey/narrator/45.flac"
        show bg grey d stairs onlayer back at Position(ypos=1125)
        show grey d downstairs onlayer back at Position(ypos=1125)
        with fade
        if persistent.quick_menu:
            $ quick_menu = True
        n "The door to the basement creaks open, revealing an antique staircase lit by weak torchlight. The air here is so stale it practically stands still, as if the very molecules of this place have been fossilized, trapped for eons until your arrival.\n"
        voice "audio/voices/ch3/grey/narrator/46.flac"
        n "Even the blaze of the torches can't penetrate the odorless air, as if they'd run out of fuel to burn ages ago, their light still flickering more out of habit than from adhering to a physical reality.\n"
        voice "audio/voices/ch3/grey/narrator/47.flac"
        n "A wispy figure watches you from the bottom of the stairs, face veiled in shadow.\n"
    voice "audio/voices/ch3/grey/hero/29.flac"
    hero "There she is again.\n"
    if trait_skeptic:
        voice "audio/voices/ch3/grey/skeptic/34.flac"
        skeptic "Barely.\n"
    else:
        voice "audio/voices/ch3/grey/smitten/27.flac"
        smitten "My love!\n"
    voice "audio/voices/ch3/grey/cold/41.flac"
    cold "She's just an old memory.\n"
    voice "audio/voices/ch3/grey/narrator/48.flac"
    if trait_skeptic:
        show grey p downstairs leave onlayer back
        with dissolve
    else:
        show grey d downstairs2 onlayer back
        with dissolve
    $ renpy.pause(0.25)
    voice sustain
    hide grey onlayer back with dissolve
    n "Your eyes lock for a brief moment, then she vanishes around the corner.\n"
    label grey_stairs_menu:
        default grey_stairs_menu_explore = False
        menu:
            extend ""

            "{i}• (Explore) ''I'm sorry about last time! Are we good?''{/i}" if grey_stairs_menu_explore == False:
                label grey_stairs_menu_explore_join:
                    $ grey_stairs_menu_explore = True
                    voice "audio/voices/ch3/grey/narrator/49.flac"
                    n "You receive no response.\n"
                    label grey_stairs_late_join:
                        voice "audio/voices/ch3/grey/hero/30.flac"
                        hero "Do you think she's upset with us? I don't like being here unarmed after what happened last time. I feel so exposed.\n"
                        if trait_smitten:
                            voice "audio/voices/ch3/grey/smitten/28.flac"
                            smitten "Of course she's livid! And with good reason.\n"
                        else:
                            voice "audio/voices/ch3/grey/skeptic/35.flac"
                            skeptic "She doesn't seem fully there. I'm not sure she's even capable of being upset.\n"
                        voice "audio/voices/ch3/grey/hero/31.flac"
                        hero "You aren't helping.\n"
                        voice "audio/voices/ch3/grey/cold/42.flac"
                        cold "Are you scared of a little ghost? What's she going to do, look at us until we feel bad? She can look all she wants. It won't do anything.\n"
                    jump grey_stairs_menu

            "{i}• (Explore) ''Is anyone there?''{/i}" if grey_stairs_menu_explore == False:
                jump grey_stairs_menu_explore_join

            "{i}• (Explore) ''I think we have a lot to talk about.''{/i}" if grey_stairs_menu_explore == False:
                jump grey_stairs_menu_explore_join

            "{i}• (Explore) ''I don't have a weapon. There wasn't anything upstairs for me when I got here.''{/i}" if grey_stairs_menu_explore == False:
                $ grey_stairs_menu_explore = True
                voice "audio/voices/ch3/grey/narrator/50.flac"
                n "Don't just tell her you're unarmed! {i}Sigh{/i}. Not that it matters. You receive no response.\n"
                jump grey_stairs_late_join

            "{i}• [[Proceed down the stairs.]{/i}":
                jump grey_basement

label grey_basement:
    $ quick_menu = False
    if trait_skeptic:
        $ gallery_grey.unlock_item(5)
        $ renpy.save_persistent()
        play audio "audio/final/_wet_step.flac"
        voice "audio/voices/ch3/grey/narrator/51.flac"
        hide bg onlayer back
        show bg grey p basement onlayer back at Position(ypos=1125)
        show grey floater onlayer back at Position(ypos=1125)
        with fade
        if persistent.quick_menu:
            $ quick_menu = True
        n "As you descend the final step, the form of the Princess comes into view. A bloated body floating face down in slowly rising waters, her wrist still bound to the wall by a heavy chain.\n"
    else:
        $ gallery_grey.unlock_item(6)
        $ renpy.save_persistent()
        voice "audio/voices/ch3/grey/narrator/52.flac"
        play audio "audio/one_shot/footsteps_stone.flac"
        hide bg onlayer back
        show bg grey d downstairs onlayer back at Position(ypos=1125)
        with fade
        if persistent.quick_menu:
            $ quick_menu = True
        n "As you descend the final step, the form of the Princess comes into view. A skeletal body lying in a heap on the floor, her wrist still bound to the wall by a heavy chain.\n"
    voice "audio/voices/ch3/grey/narrator/53.flac"
    n "This cell is a dark and isolated place, with not so much as a window to allow starlight to penetrate the gloom.\n"
    voice "audio/voices/ch3/grey/cold/43.flac"
    cold "See? She's dead.\n"
    if trait_smitten:
        voice "audio/voices/ch3/grey/smitten/29.flac"
        smitten "No! What foul trickery is this? How can this be? We just saw her alive and well a moment ago, floating away transparently!\n"
        voice "audio/voices/ch3/grey/hero/32.flac"
        hero "Whatever we saw was a ghost. I thought we were all on the same page.\n"
        voice "audio/voices/ch3/grey/cold/44.flac"
        cold "Do try to keep up.\n"
        play tertiary "audio/one_shot/door_close.flac"
        queue tertiary "audio/one_shot/lock_click.flac"
        voice "audio/voices/ch3/grey/narrator/54a.flac"
        n "Your thoughts are interrupted by the sound of a slamming door and a clicking lock.\n"
        #voice "audio/voices/ch3/grey/narrator/54.flac"
        #n "Your thoughts are cut short by the sound of a slamming door and a clicking lock.\n"
        voice "audio/voices/ch3/grey/narrator/55.flac"
        hide bg onlayer back
        show bg grey d stairs up onlayer back at Position(ypos=1125)
        show grey d stairs torch onlayer back at Position(ypos=1125)
        with dissolve
        n "You turn to see the shade of the Princess, staring down at you from the top of the stairs, clutching a brightly burning torch—\n{w=9.0}{nw}"
        show screen disableclick(0.5)
    else:
        voice "audio/voices/ch3/grey/skeptic/36.flac"
        skeptic "She's not just dead. It looks like she's been rotting. So killing her does stick... mostly. But if she's dead, then what are we supposed to do?\n"
        voice "audio/voices/ch3/grey/narrator/56.flac"
        n "She isn't dead. You clearly just believe she is.\n"
        voice "audio/voices/ch3/grey/skeptic/37.flac"
        skeptic "Her corpse is floating right in front of us, you can stop it with the mind games.\n"
        voice "audio/voices/ch3/grey/hero/33.flac"
        hero "If she's dead, then do we even have to do anything? How can she be a threat to the world like this?\n"
        voice "audio/voices/ch3/grey/narrator/54.flac"
        play tertiary "audio/one_shot/door_close.flac"
        queue tertiary "audio/one_shot/lock_click.flac"
        n "Your thoughts are cut short by the sound of a slamming door and a clicking lock.\n"
        voice "audio/voices/ch3/grey/narrator/57.flac"
        hide bg onlayer back
        hide grey onlayer back
        show bg grey p stairs up onlayer back at Position(ypos=1125)
        show grey p stairs neutral onlayer back at Position(ypos=1125)
        with dissolve
        n "You turn to see the shade of the Princess, staring down at you from the top of the stairs—\n{w=6.0}{nw}"
        show screen disableclick(0.5)

    voice "audio/voices/ch3/grey/narrator/58.flac"
    n "So that's where the blade is! It's already in her heart. And yet she... isn't dead.\n"
    voice "audio/voices/ch3/grey/cold/45.flac"
    cold "She {i}is{/i} dead. Have you never heard of a ghost before?\n"
    voice "audio/voices/ch3/grey/narrator/59.flac"
    n "Oh, for the love of— can we not waste time arguing over the semantics of what is and isn't 'dead'? She is clearly {i}conscious{/i}, she clearly just slammed the door on you, and she clearly has a weapon — {i}your{/i} pristine blade sticking out of her chest. This is extremely bad. Catastrophic, even.\n"
    voice "audio/voices/ch3/grey/hero/34.flac"
    hero "Yeah, dead or not, what are we supposed to do about her? Slaying, or, er, destroying—if we want to be a little more death-neutral—seems off the table.\n"
    if trait_smitten:
        voice "audio/voices/ch3/grey/smitten/30.flac"
        smitten "We make amends! She obviously still holds us in her heart. She's bearing a torch for us and everything!\n"

    else:
        voice "audio/voices/ch3/grey/skeptic/38.flac"
        skeptic "Yeah, this is tricky. But let's talk to her. See what kind of information she has that we don't.\n"

    voice "audio/voices/ch3/grey/hero/35.flac"
    hero "But she hasn't said anything. Are you sure she can talk like this?\n"

    if grey_source == "damsel":
        voice "audio/voices/ch3/grey/princess/p1.flac"
        show grey d stairs torch talk onlayer back
        p "You came back! I missed you.\n"
        show grey d stairs torch onlayer back
        voice "audio/voices/ch3/grey/smitten/31.flac"
        smitten "That angelic voice! I missed you, too, my beloved!\n"
        voice "audio/voices/ch3/grey/hero/36.flac"
        hero "You sure snapped back to your old self quick.\n"
        voice "audio/voices/ch3/grey/smitten/32.flac"
        smitten "Yes! Seeing her dazzling countenance again has reignited the warmth in my heart. I have found it in me to forgive the sins this body has committed, we can have our perfect romance after all!\n"
        jump grey_damsel
    else:
        voice "audio/voices/ch3/grey/princess/sp1.flac"
        show grey p stairs talk onlayer back
        sp "Bold of you to come back here after what you did.\n"
        if prisoner_decapitate:
            voice "audio/voices/ch3/grey/princess/sp2.flac"
            sp "You were supposed to take me with you. Didn't I ask you for help? This isn't help.\n"
        show grey p stairs neutral onlayer back
        jump grey_prisoner


label grey_damsel:
    voice "audio/voices/ch3/grey/princess/p2.flac"
    show grey d stairs torch talk onlayer back
    p "This is a bad place. We're supposed to be together, but it keeps making us hurt each other.\n"
    voice "audio/voices/ch3/grey/narrator/60.flac"
    play audio "audio/final/_grey_torch_drop.flac"
    $ renpy.music.set_volume(1.0, 30.0, channel='music2')
    show grey d stairs torch drop onlayer back
    with Dissolve(1.5)
    n "The torch falls from the Princess' hand and bounces down the stairs.\n"
    voice "audio/voices/ch3/grey/princess/p3.flac"
    show grey d stairs neutral talk onlayer back
    with Dissolve(1.5)
    p "It'll be so much better when it's gone.\n"
    voice "audio/voices/ch3/grey/narrator/61.flac"
    play sound "audio/final/grey_fire_loop1.ogg" loop
    show grey d stairs neutral onlayer back
    show fire grey d stairs0 onlayer front at Position(ypos=1125)
    with dissolve
    n "The skeletal wood of the basement, perfectly dry after uncountable years of desiccation, immediately catches fire.\n"
    voice "audio/voices/ch3/grey/hero/37.flac"
    hero "She's... trying to kill us.\n"
    voice "audio/voices/ch3/grey/smitten/33.flac"
    smitten "A misplaced escalation of her passions, but clearly she still cares for us. I say we burn with her!\n"
    label grey_damsel_menu:
        default grey_damsel_together_explore = False
        default grey_damsel_let_out_explore = False
        default grey_damsel_burn_explore = False
        default grey_damsel_want_explore = False
        default grey_damsel_beg_explore = False
        default grey_damsel_mad_explore = False
        default grey_damsel_grudge_explore = False
        default grey_damsel_close_explore = False
        default grey_death_timer = -1
        default grey_dams_knife_var = False
        $ grey_death_timer += 1
        if grey_death_timer == 1:
            voice "audio/voices/ch3/grey/narrator/62.flac"
            play sound "audio/final/grey_fire_loop2.ogg" loop
            show fire grey d stairs1 onlayer front at Position(ypos=1125)
            with dissolve
            n "The fire grows quickly, devouring the basement, dancing up the walls and painting every surface with strokes of flame. You're choked by smoke, and the air around you grows uncomfortably warm.\n"
            voice "audio/voices/ch3/grey/cold/46.flac"
            cold "We've never burned to death before. I wonder how it's going to feel.\n"
            voice "audio/voices/ch3/grey/hero/38.flac"
            hero "Bad. I bet it'll feel really, really bad.\n"
            voice "audio/voices/ch3/grey/narrator/63.flac"
            n "Yes, it will be terrible, so you'd better come up with something to do and fast. Your personal safety is far from the only thing she's threatening right now.\n"
            voice "audio/voices/ch3/grey/smitten/34.flac"
            smitten "I think a bit of fiery passion is good for the world. You're just trying to spoil her fun.\n"
            voice "audio/voices/ch3/grey/narrator/64a.flac"
            n "I'm not spoiling anything! I'm trying to prevent {i}oblivion{/i}.\n"
        elif grey_death_timer == 2:
            voice "audio/voices/ch3/grey/narrator/65.flac"
            show fire grey d stairs2 onlayer front at Position(ypos=1125)
            with dissolve
            n "The heat grows in intensity as the flames draw ever nearer. You can practically feel your skin sizzling already. If you're going to try and stop her from killing you and destroying the whole world, you'd better do something, and you'd better do it now.\n"
            voice "audio/voices/ch3/grey/smitten/35.flac"
            smitten "I wonder if we look good right now. Fire makes a lot of things look good. I can only imagine how dazzling our eyes are in the dancing flames, do you think she's noticed?\n"
            voice "audio/voices/ch3/grey/hero/39a.flac"
            hero "I don't want to burn to death. We... we don't have to, right?\n"

        elif grey_death_timer == 3:
            $ quick_menu = False
            play sound "audio/final/grey_fire_loop3.ogg" loop
            voice "audio/voices/ch3/grey/narrator/66.flac"
            hide bg onlayer back
            hide grey onlayer back
            hide fire onlayer front
            scene bg black
            with fade
            if persistent.quick_menu:
                $ quick_menu = True
            n "The flames lick at your form, stripping layers of you away, causing your skin to blister and pop and crisp. As you burn, the Princess glides to your side, her ghostly form blackening as she, too, succumbs.\n"
            voice "audio/voices/ch3/grey/hero/40.flac"
            show bg cg grey d end onlayer farback at Position(ypos=1125)
            show flames grey cg d end1 onlayer back at Position(ypos=1125)
            show cg grey d end1 onlayer front at Position(ypos=1125)
            with Dissolve(3.0)
            hero "This is terrible! We're going to die!\n"
            voice "audio/voices/ch3/grey/cold/47.flac"
            cold "I'd savor this feeling if I were you. Soon enough we won't have nerves.\n"
            voice "audio/voices/ch3/grey/smitten/36.flac"
            smitten "And we'll get to die with {i}her{/i}. After what you made us do last time, this is as sweet an end as we could hope for.\n"
            voice "audio/voices/ch3/grey/narrator/67.flac"
            play audio "audio/final/Beast_AcidFleshMelt_2.flac"
            n "She clutches you close to her chest, her eyes bright and her smile wide with manic affection, watching as the flames take you away.\n"
            jump grey_damsel_end
        menu:
            extend ""

            "{i}• (Explore) ''Why did you close the door?''{/i}" if grey_damsel_close_explore == False:
                $ grey_damsel_close_explore = True
                voice "audio/voices/ch3/grey/princess/p4a.flac"
                show grey d stairs neutral talk onlayer back
                p "Because I want to be with you. I don't want you to leave.\n"
                show grey d stairs neutral onlayer back
                if grey_damsel_together_explore == False:
                    label grey_damsel_together_explore_join:
                        $ grey_damsel_together_explore = True
                        voice "audio/voices/ch3/grey/smitten/37.flac"
                        smitten "See! Everything's fine! She wants to be with us.\n"
                        voice "audio/voices/ch3/grey/hero/41.flac"
                        hero "Yeah. In a bad way.\n"
                        voice "audio/voices/ch3/grey/smitten/38.flac"
                        smitten "She just has a unique way of expressing things!\n"
                        jump grey_damsel_menu

            "{i}• (Explore) ''Let me out! Are you trying to kill me?''{/i}" if grey_damsel_let_out_explore == False:
                $ grey_damsel_let_out_explore = True
                voice "audio/voices/ch3/grey/princess/p5.flac"
                show grey d stairs neutral talk onlayer back
                p "Dying apart kept us apart. Dying together will keep us together.\n"
                show grey d stairs neutral onlayer back
                if grey_damsel_together_explore == False:
                    jump grey_damsel_together_explore_join
                jump grey_damsel_menu

            "{i}• (Explore) ''I'm going to burn!''{/i}" if grey_damsel_burn_explore == False:
                $ grey_damsel_burn_explore = True
                voice "audio/voices/ch3/grey/princess/p6.flac"
                show grey d stairs neutral talk onlayer back
                p "It's okay. I'm going to burn, too. And then we won't hurt anymore.\n"
                show grey d stairs neutral onlayer back
                voice "audio/voices/ch3/grey/cold/48.flac"
                cold "She's right about that last part. Burning doesn't hurt forever.\n"
                jump grey_damsel_menu

            "{i}• (Explore) ''What's wrong with you? I don't want this!''{/i}" if grey_damsel_want_explore == False and grey_damsel_together_explore:
                $ grey_damsel_want_explore = True
                voice "audio/voices/ch3/grey/princess/p7.flac"
                show grey d stairs neutral talk onlayer back
                p "You just think you don't. Sometimes someone else makes decisions for you, and those decisions are for the best. You should know that.\n"
                show grey d stairs neutral onlayer back
                if grey_damsel_grudge_explore == False:
                    label grey_damsel_grudge_explore_join:
                        $ grey_damsel_grudge_explore = True
                        voice "audio/voices/ch3/grey/hero/42.flac"
                        hero "She's holding a grudge.\n"
                        voice "audio/voices/ch3/grey/smitten/39.flac"
                        smitten "She wouldn't! She's perfect!\n"
                jump grey_damsel_menu

            "{i}• (Explore) ''Please! I'm begging you! I'll do anything, just don't let me burn!''{/i}" if grey_damsel_beg_explore == False and grey_damsel_together_explore:
                $ grey_damsel_beg_explore = True
                voice "audio/voices/ch3/grey/princess/p8.flac"
                show grey d stairs neutral talk onlayer back
                p "You'll understand when it's over! Just like I understood after you stabbed me in the heart! Everything is okay!\n"
                show grey d stairs neutral onlayer back
                if grey_damsel_grudge_explore == False:
                    jump grey_damsel_grudge_explore_join
                jump grey_damsel_menu

            "{i}• (Explore) ''Are you mad at me for killing you? I'm sorry!''{/i}" if grey_damsel_mad_explore == False:
                $ grey_damsel_mad_explore = True
                voice "audio/voices/ch3/grey/princess/p9.flac"
                show grey d stairs neutral talk onlayer back
                p "I'm not mad at you. You gave me so much to think about. And it's all going to be over soon. It's all going to be better.\n"
                show grey d stairs neutral onlayer back
                if grey_damsel_grudge_explore == False:
                    jump grey_damsel_grudge_explore_join
                jump grey_damsel_menu

            "{i}• [[Rush for the blade.]{/i}":
                $ grey_rush = "blade"
                play sound "audio/final/grey_fire_loop3.ogg" loop
                play audio "audio/one_shot/footstep_run_medium.flac"
                voice "audio/voices/ch3/grey/narrator/68.flac"
                hide fire onlayer front
                hide grey onlayer back
                hide bg onlayer back
                scene cg grey d stairs rush onlayer back at Position(ypos=1125)
                with Dissolve(1.0)
                n "As you rush up the stairs towards the Princess, the entire cabin erupts into a raging inferno.\n"
                voice "audio/voices/ch3/grey/narrator/69.flac"
                play audio "audio/one_shot/knife_pickup.flac"
                hide cg onlayer back
                show bg cg grey d blade rush onlayer farback at Position(ypos=1125)
                show flames cg grey d blade rush onlayer back at Position(ypos=1125)
                show cg grey d blade rush onlayer front at Position(ypos=1125)
                with Dissolve(1.0)
                n "You push through the flames, trying to ignore the choking hot air filling your lungs, and manage to reach her, your hand wrapping around the hilt of the blade.\n"
                voice "audio/voices/ch3/grey/narrator/70.flac"
                show flames cg grey d blade rush final onlayer back at Position(ypos=1125)
                show cg grey d blade rush final onlayer front at Position(ypos=1125)
                with Dissolve(2.0)
                n "But the metal is already blisteringly hot. Your hand sizzles as it melts on contact. You can't so much as pull away, your nerves seizing up as they're fried, the bones of your hand fusing in place around the weapon.\n"
                voice "audio/voices/ch3/grey/narrator/71.flac"
                play audio "audio/final/Beast_AcidFleshMelt_2.flac"
                hide flames onlayer back
                hide cg onlayer front
                show bg cg grey d end onlayer farback at Position(ypos=1125)
                show flames grey cg d end1 onlayer back at Position(ypos=1125)
                show cg grey d knife end1 onlayer front at Position(ypos=1125)
                with Dissolve(2.0)
                n "The Princess, smiling warmly as her skin bubbles away, places her hand on yours and clutches it to her chest.\n"
                jump grey_damsel_end

            "{i}• [[Rush to the door.]{/i}":
                $ grey_rush = "door"
                play sound "audio/final/grey_fire_loop3.ogg" loop
                play audio "audio/one_shot/footstep_run_medium.flac"
                voice "audio/voices/ch3/grey/narrator/72.flac"
                hide fire onlayer front
                hide grey onlayer back
                hide bg onlayer back
                scene cg grey d stairs rush onlayer back at Position(ypos=1125)
                with Dissolve(1.0)
                n "As you rush up the stairs, the entire cabin erupts into a raging inferno.\n"
                voice "audio/voices/ch3/grey/narrator/73.flac"
                play audio "audio/one_shot/thump_6.flac"
                hide cg onlayer back
                show cg grey d door rush1 onlayer back at Position(ypos=1125)
                with Dissolve(1.0)
                n "You ignore the Princess, throwing yourself headlong against the door, bashing at it with your clenched fists in a vain attempt at freedom.\n"
                voice "audio/voices/ch3/grey/narrator/73_2.flac"
                play audio "audio/final/Beast_AcidFleshMelt_2.flac"
                show cg grey d door rush2 onlayer back at Position(ypos=1125)
                with Dissolve(1.0)
                n "It's no use. You're stuck here. Your skin starts to bubble.\n"
                voice "audio/voices/ch3/grey/narrator/74a.flac"
                show cg grey d door rush3 onlayer back at Position(ypos=1125)
                with Dissolve(1.0)
                n "As layers of you peel away into raw seeping burns, you feel a hand on yours.\n" id grey_damsel_grudge_explore_join_b3a7f840
                voice "audio/voices/ch3/grey/narrator/75.flac"
                hide cg onlayer back
                show bg cg grey d end onlayer farback at Position(ypos=1125)
                show flames grey cg d end1 onlayer back at Position(ypos=1125)
                show cg grey d knife end1 onlayer front at Position(ypos=1125)
                with Dissolve(2.0)
                n "You turn to see the Princess, face bright and smile wide with manic affection. She clutches you close to her chest, watching with loving eyes as the flames eat you away bit by bit.\n"
                jump grey_damsel_end

        label grey_damsel_end:
            voice "audio/voices/ch3/grey/narrator/76.flac"
            show flames cg grey d end2 back onlayer farback
            show flames cg grey d end2 front onlayer inyourface at Position(ypos=1125)
            if grey_dams_knife_var:
                show cg grey d end2 onlayer front at Position(ypos=1125)
            else:
                show cg grey d knife end2 onlayer front at Position(ypos=1125)
            with Dissolve(2.0)
            n "The pain is unbearable at first. Every inch of you screams as your flesh is stripped away, your muscles stiffening as they're cooked, your blood boiling in your veins.\n"
            voice "audio/voices/ch3/grey/narrator/77.flac"
            show flames cg grey d end3 back onlayer farback
            show flames cg grey d end3 front onlayer inyourface at Position(ypos=1125)
            if grey_dams_knife_var:
                show cg grey d end3 onlayer front at Position(ypos=1125)
            else:
                show cg grey d knife end3 onlayer front at Position(ypos=1125)
            with Dissolve(2.0)
            n "But it isn't long before the flames take your nerves, and with them, your ability to feel much of anything.\n"
            voice "audio/voices/ch3/grey/cold/49.flac"
            cold "See? That wasn't so bad.\n"
            voice "audio/voices/ch3/grey/hero/43.flac"
            hero "It was so bad! But somehow, the nothing is so much worse.\n"
            voice "audio/voices/ch3/grey/cold/50.flac"
            cold "You'll get used to it.\n"
            voice "audio/voices/ch3/grey/smitten/40.flac"
            smitten "There are still the feelings of the heart. Those never go away.\n"
            voice "audio/voices/ch3/grey/cold/51.flac"
            cold "Oh, they always do in the end. You just haven't experienced enough. Eventually you'll want them to stop, too. You'll make them stop. Trust me.\n"
            voice "audio/voices/ch3/grey/narrator/78.flac"
            stop music fadeout 10.0
            stop music2 fadeout 10.0
            stop sound fadeout 20.0
            stop secondary fadeout 20.0
            stop tertiary fadeout 20.0
            play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 20.0
            show flames cg grey d end4 back onlayer farback
            show flames cg grey d end4 front onlayer inyourface at Position(ypos=1125)
            if grey_dams_knife_var:
                show cg grey d end4 onlayer front at Position(ypos=1125)
            else:
                show cg grey d knife end4 onlayer front at Position(ypos=1125)
            show quiet creep1 onlayer back at Position(ypos=1125)
            with Dissolve(2.0)
            n "The Princess' smile never fades. Her skin peels away, and then her muscle, until all you can see is her charring skull, locked in an eternal grin.\n"
            $ gallery_grey.unlock_item(7)
            $ gallery_grey.unlock_item(9)
            $ gallery_grey.unlock_item(11)
            $ gallery_grey.unlock_item(13)
            $ gallery_grey.unlock_item(14)
            $ renpy.save_persistent()
            $ achievement.grant("ACH_GRAY_BURN")
            voice "audio/voices/ch3/grey/smitten/41.flac"
            hide flames onlayer inyourface
            show quiet creep2 onlayer back at Position(ypos=1125)
            with Dissolve(1.0)
            smitten "It's very romantic, really. We got our happy ending after all. We can die happy.\n"
            hide cg onlayer front
            show grey d quiet onlayer front at Position(ypos=1125)
            show quiet creep3 onlayer back
            with Dissolve(2.0)
            $ renpy.pause(0.2)
            play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
            show large quiet arms first onlayer back
            with Dissolve(1.5)
            $ renpy.pause(0.125)
            hide large onlayer back
            show grey d quiet taken onlayer front
            with Dissolve(1.5)
            $ renpy.pause(0.125)
            show large quiet arms penultimate onlayer front at Position(ypos=1125)
            with Dissolve(0.5)
            $ renpy.pause(0.125)
            hide cg onlayer back
            hide grey onlayer front
            hide large onlayer front
            show large quiet arms last onlayer front at Position(ypos=1125)
            with Dissolve(0.5)
            $ renpy.pause(0.125)
            hide large onlayer front
            with Dissolve(0.5)
            $ renpy.pause(0.125)
            hide fire onlayer front
            hide fire onlayer back
            hide fire onlayer inyourface
            hide grey onlayer back
            hide flames onlayer farback
            hide flames onlayer back
            hide flames onlayer front
            hide flames onlayer inyourface
            hide bg onlayer back
            hide bg onlayer farback
            hide quiet onlayer back
            show farback quiet onlayer farback at Position(ypos=1125)
            with Dissolve(4.0)
            show mirror quiet distant onlayer back at Position(ypos=1125)
            if loops_finished != 0:
                truth "But despite your best efforts, you do not die. It's time for you to leave. Memory returns.\n"
            else:
                truth "But despite your best efforts, you do not die, and she is gone. Something has taken her away, and it's left something else in her place.\n"
            $ grey_end = "burn"
            $ princess_kept += 1
            $ princess_satisfy += 1
            jump mirror_start
            # END

label grey_prisoner:
    label grey_prisoner_menu:
        $ grey_death_timer += 1
        if grey_death_timer == 1:
            voice "audio/voices/ch3/grey/narrator/80.flac"
            play sound "audio/final/Water_Drip_Loop_2.ogg" loop
            show water grey p stairs1 onlayer back at Position(ypos=1125)
            with Dissolve(1.0)
            n "But she doesn't answer your question. All she does is watch you in shadowed silence.\n"
            voice "audio/voices/ch3/grey/hero/44.flac"
            hero "Do you hear that trickling sound? The water's rising, isn't it?\n"
            voice "audio/voices/ch3/grey/narrator/81.flac"
            n "It is. And it's rising fast.\n"
            voice "audio/voices/ch3/grey/cold/52.flac"
            cold "Oh, that's interesting. We've never drowned before. I wonder how it'll feel.\n"
            voice "audio/voices/ch3/grey/hero/45.flac"
            hero "Bad, I bet!\n"
            voice "audio/voices/ch3/grey/skeptic/39.flac"
            skeptic "I don't think dying ever feels good.\n"
            voice "audio/voices/ch3/grey/narrator/82.flac"
            n "Yes, how astute. Dying is bad, and you should avoid it. How about you stop trying to talk to her and {i}do something{/i} instead?\n"

        elif grey_death_timer == 2:
            voice "audio/voices/ch3/grey/narrator/83.flac"
            play audio "audio/final/Water_RushingInLIGHT_4.flac"
            show water grey p stairs2 onlayer back at Position(ypos=1125)
            with Dissolve(1.0)
            n "The water is rising faster now. It's flowing in from some unseen place, and judging by the height of the algae on the stairs, it has no intention of stopping any time soon. You feel it creeping up your back, so cold that it steals the very warmth from your flesh, leaving a smothering numbness in its place.\n"
            voice "audio/voices/ch3/grey/narrator/84.flac"
            n "Are you really just going to stand there and let yourself die?\n"
            voice "audio/voices/ch3/grey/skeptic/40.flac"
            skeptic "Yeah. Let's think. Where is it coming from?\n"
            voice "audio/voices/ch3/grey/narrator/85.flac"
            n "It's coming from some unseen place.\n"
            voice "audio/voices/ch3/grey/hero/46.flac"
            hero "Does it really matter where it's coming from? Because I can {i}feel{/i} it rising, I don't think we have much time to sleuth.\n"
            voice "audio/voices/ch3/grey/skeptic/41.flac"
            skeptic "Yes, it matters! Maybe we can find a way out. Maybe we can figure out a way to make this work. This is just a puzzle. We can solve it.\n"
            voice "audio/voices/ch3/grey/cold/53.flac"
            cold "Some things aren't puzzles to be solved. Sometimes you're doomed from the start. Most people are.\n"
            voice "audio/voices/ch3/grey/narrator/86.flac"
            n "Yes, most people are doomed, but, in case you need reminding, {i}everyone{/i} will be doomed forever unless you stop her.\n"

        elif grey_death_timer == 3:
            voice "audio/voices/ch3/grey/princess/sp3.flac"
            show grey p stairs neutral talk onlayer back
            show water grey p stairs3 onlayer back at Position(ypos=1125)
            with Dissolve(1.0)
            sp "If this is how you're choosing to spend your last breaths, I won't stop you. But it won't make any difference.\n"
            show grey p stairs neutral onlayer back
            voice "audio/voices/ch3/grey/narrator/87.flac"
            #play audio "audio/final/Water_RushingIn_2.flac"
            show water grey p stairs4 onlayer back at Position(ypos=1125)
            with Dissolve(1.0)
            n "The water is up to your chin. You lose your footing, bobbing helplessly in the putrid floodpool.\n"
            play audio "audio/final/_grey_explode.flac"
            $ renpy.pause(3.5)
            voice "audio/voices/ch3/grey/narrator/88.flac"
            show explode grey p stairs onlayer back at Position(ypos=1125)
            with Dissolve(1.0)
            $ renpy.pause(2.5)
            play tertiary "audio/final/Water_Underwater_Loop_1.ogg" loop fadein 3.0
            play sound "audio/final/Water_UnderwaterRushIN_2.flac"
            play audio "audio/final/_grey_crack.flac"
            voice sustain
            stop music
            hide water onlayer back
            hide grey onlayer back
            hide bg onlayer back
            hide explode onlayer back
            scene bg black
            n "And suddenly, the door to the basement is thrown from its hinges as one last massive wave of water comes crashing down, sweeping you up in a powerful current. You're bashed against the stone wall.\n"
            jump grey_prisoner_end

        default grey_prisoner_why = False
        default grey_prisoner_kill_ask = False
        default grey_prisoner_drown = False
        default grey_prisoner_wrong = False
        default grey_prisoner_even = False
        default grey_prisoner_beg = False
        default grey_prisoner_sorry = False
        menu:
            extend ""

            "{i}• (Explore) ''Why did you close the door?''{/i}" if grey_death_timer == 0 and grey_prisoner_why == False:
                $ grey_prisoner_why = True
                jump grey_prisoner_menu

            "{i}• (Explore) ''Let me out! Are you trying to kill me?''{/i}" if grey_prisoner_kill_ask == False:
                $ grey_prisoner_kill_ask = True
                if grey_death_timer == 1:
                    voice "audio/voices/ch3/grey/princess/sp4.flac"
                    show grey p stairs neutral talk onlayer back
                    sp "No. You're killing yourself.\n"
                    show grey p stairs neutral onlayer back
                jump grey_prisoner_menu

            "{i}• (Explore) ''I'm going to drown!''{/i}" if grey_prisoner_drown == False and grey_death_timer:
                $ grey_prisoner_drown = True
                if grey_death_timer == 1:
                    voice "audio/voices/ch3/grey/princess/sp5.flac"
                    show grey p stairs neutral talk onlayer back
                    sp "Yes. You are.\n"
                    show grey p stairs neutral onlayer back
                jump grey_prisoner_menu

            "{i}• (Explore) ''What's wrong with you? I don't want this!''{/i}" if grey_prisoner_wrong == False:
                $ grey_prisoner_wrong = True
                if grey_death_timer == 1:
                    voice "audio/voices/ch3/grey/princess/sp6.flac"
                    show grey p stairs neutral talk onlayer back
                    sp "And I didn't want to die.\n"
                    show grey p stairs neutral onlayer back
                jump grey_prisoner_menu

            "{i}• (Explore) ''I didn't even kill you! You killed yourself!''{/i}" if grey_prisoner_even == False and prisoner_decapitate:
                jump grey_prisoner_even_join

            "{i}• (Explore) ''I only killed you after you killed me first! We're even now! We don't need to do this again.''{/i}" if grey_prisoner_even == False and prisoner_decapitate == False:
                label grey_prisoner_even_join:
                    $ grey_prisoner_even = True
                    if grey_death_timer == 1:
                        voice "audio/voices/ch3/grey/princess/sp7.flac"
                        show grey p stairs neutral talk onlayer back
                        sp "Pathetic.\n"
                        show grey p stairs neutral onlayer back
                    jump grey_prisoner_menu

            "{i}• (Explore) ''Please! I'm begging you! I'll do anything, just don't let me drown!''{/i}" if grey_prisoner_beg == False:
                $ grey_prisoner_beg = True
                if grey_death_timer == 1:
                    voice "audio/voices/ch3/grey/princess/sp7.flac"
                    show grey p stairs neutral talk onlayer back
                    sp "Pathetic.\n"
                    show grey p stairs neutral onlayer back
                jump grey_prisoner_menu

            "{i}• (Explore) ''Is this about last time? I'm sorry! Now can you let me out?''{/i}" if grey_prisoner_sorry == False:
                $ grey_prisoner_sorry = True
                if grey_death_timer == 1:
                    voice "audio/voices/ch3/grey/princess/sp7.flac"
                    show grey p stairs neutral talk onlayer back
                    sp "Pathetic.\n"
                    show grey p stairs neutral onlayer back
                jump grey_prisoner_menu

            "{i}• [[Rush for the blade.]{/i}":
                jump grey_prisoner_rush

            "{i}• [[Rush to the door.]{/i}":
                label grey_prisoner_rush:
                    play audio "audio/final/_wet_step.flac"
                    voice "audio/voices/ch3/grey/narrator/89.flac"
                    hide bg onlayer back
                    hide water onlayer front
                    hide grey onlayer back
                    show bg cg grey p rush onlayer back at Position(ypos=1125)
                    show grey p rush her onlayer back at Position(ypos=1125)
                    if grey_death_timer == 1:
                        show water grey p stairs2 onlayer back at Position(ypos=1125)
                    if grey_death_timer == 1:
                        show water grey p stairs2 onlayer back at Position(ypos=1125)
                    if grey_death_timer == 2:
                        show water grey p stairs3 onlayer back at Position(ypos=1125)
                    with dissolve
                    n "The Princess eyes you with a disaffected gaze as you rush up the stairs, but you don't make it past the first few steps.\n"
                    play audio "audio/final/_grey_explode.flac"
                    $ renpy.pause(3.5)
                    voice "audio/voices/ch3/grey/narrator/90.flac"
                    hide grey onlayer back
                    show explode grey p rush onlayer back at Position(ypos=1125)
                    show grey p rush onlayer back at Position(ypos=1125)
                    with Dissolve(1.0)
                    $ renpy.pause(2.5)
                    play tertiary "audio/final/Water_Underwater_Loop_1.ogg" loop fadein 3.0
                    play sound "audio/final/Water_UnderwaterRushIN_2.flac"
                    play audio "audio/final/_grey_crack.flac"
                    voice sustain
                    stop music
                    hide water onlayer back
                    hide grey onlayer back
                    hide bg onlayer back
                    hide explode onlayer back
                    scene bg black
                    n "The door bursts open, a powerful wave of water crashing down towards you, and you're swept up in the flood. Your head slams into the basement wall.\n"
                    jump grey_prisoner_end



    label grey_prisoner_end:
        voice "audio/voices/ch3/grey/narrator/91.flac"
        play music "audio/_music/ch3/grey/The Grey Water Rising FINAL.flac"
        queue music "audio/_music/ch3/grey/The Grey Water Rising LOOP FINAL.flac"
        play audio "audio/final/Nightmare_MaleBreath_1.flac"
        #play sound "audio/final/Water_RushingIn_Loop_1.ogg" loop
        scene bg cg grey drowning1 onlayer farback at Position(ypos=1125)
        show grey drowning1 onlayer back at Position(ypos=1125)
        show player grey drowning1 onlayer front at Position(ypos=1125)
        with fade
        n "You come-to a moment later, suspended in darkness, disorientated, only aware of the surface of the water and the emptiness above. And, of course, the Princess, hovering above you, watching in silence as you struggle to stay afloat in the icy depths. There's no way out.\n"
        voice "audio/voices/ch3/grey/hero/47a.flac"
        hero "It's so dark! And cold! I think our limbs are slowing down, how much longer can we do this?!\n"
        voice "audio/voices/ch3/grey/skeptic/42.flac"
        skeptic "Just keep breathing. We'll figure this out.\n"
        voice "audio/voices/ch3/grey/cold/54.flac"
        cold "Or we won't. It doesn't matter either way.\n"
        voice "audio/voices/ch3/grey/narrator/92.flac"
        n "But you don't have time to figure anything out. Something cold and clammy wraps around your ankle.\n"
        voice "audio/voices/ch3/grey/narrator/93.flac"
        hide bg onlayer farback
        hide grey onlayer back
        hide player onlayer front
        show bg cg grey drowning2 onlayer farback at Position(ypos=1125)
        show grey drowning2 onlayer back at Position(ypos=1125)
        show ripples grey drowning2 onlayer front at Position(ypos=1125)
        show player grey drowning2 onlayer inyourface at Position(ypos=1125)
        with dissolve
        n "You're dragged under, only able to take one last hopeful gulp of air before your head is plunged into the freezing depths.\n"
        voice "audio/voices/ch3/grey/narrator/94.flac"
        hide bg onlayer farback
        hide grey onlayer back
        hide ripples onlayer front
        hide player onlayer inyourface
        show bg cg grey drowning3 onlayer back at Position(ypos=1125)
        with Dissolve(0.5)
        $ renpy.pause(0.5)
        voice sustain
        show grey drowning3 onlayer front at Position(ypos=1125)
        with Dissolve(10.0)
        n "As you sink below the surface, you see it. Or rather, you see her. The body you found floating when you first arrived. Its hand is locked around your ankle, the heavy chains pulling you both down into the unfeeling, suffocating nothingness.\n"
        if prisoner_decapitate == False:
            voice "audio/voices/ch3/grey/hero/48.flac"
            hero "I get it! We shouldn't have killed her! Just get it away from us, please!\n"
        else:
            voice "audio/voices/ch3/grey/hero/48a.flac"
            hero "Just get it away from us, please!\n"
            #hero "I get it! We shouldn't have left her! Just get it away from us, please!\n"
        voice "audio/voices/ch3/grey/cold/55.flac"
        cold "The past is the past. There's no changing it. There's nothing to fix.\n"
        voice "audio/voices/ch3/grey/skeptic/43.flac"
        skeptic "And there's not a lot we can do about the present, either. Not unless we think. Like we should have been doing all along!\n"
        voice "audio/voices/ch3/grey/narrator/95.flac"
        hide bg onlayer back
        hide grey onlayer front
        show bg cg grey drowning4 onlayer farback at Position(ypos=1125)
        show grey drowning4 onlayer back at Position(ypos=1125)
        show ripples grey drowning4 onlayer front at Position(ypos=1125)
        show player grey drowning4 onlayer inyourface at Position(ypos=1125)
        with dissolve
        n "But there is no thinking as you drown. You desperately try to pull yourself back to the surface again, and again, and again, your icy limbs flailing desperately against the grip of her rotting corpse. And all the while her ghastly figure stares down at you, expressionless, as unfeeling as the weight around your ankle.\n"
        $ gallery_grey.unlock_item(8)
        $ gallery_grey.unlock_item(10)
        $ gallery_grey.unlock_item(12)
        $ renpy.save_persistent()
        $ achievement.grant("ACH_GRAY_DROWN")
        stop sound fadeout 20.0
        stop tertiary fadeout 20.0
        stop music fadeout 20.0
        stop music2 fadeout 20.0
        play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 20.0
        voice "audio/voices/ch3/grey/princess/sp8.flac"
        hide grey onlayer back
        show quiet creep1 onlayer front at Position(ypos=1125)
        show grey drowning4 talk onlayer front
        with Dissolve(1.0)
        play audio "audio/final/_water_hands.flac"
        sp "Your lungs fill with water the same way mine filled with blood. In the end, we're not so different.\n"
        show quiet creep2 onlayer front at Position(ypos=1125)
        hide player onlayer inyourface
        show hands grey1 onlayer farback at Position(ypos=1125)
        with Dissolve(1.0)
        $ renpy.pause(0.25)
        hide grey onlayer front
        show quiet creep3 onlayer front at Position(ypos=1125)
        show grey drowning4 quiet onlayer back at Position(ypos=1125)
        show hands grey2 onlayer farback at Position(ypos=1125)
        with Dissolve(1.0)
        $ renpy.pause(0.25)
        hide grey onlayer back
        show hands grey3 onlayer farback
        with Dissolve(1.0)
        $ renpy.pause(0.25)
        show hands grey4 onlayer farback
        with Dissolve(1.0)
        $ renpy.pause(0.25)
        hide hands onlayer farback
        hide ripples onlayer front
        with Dissolve(0.5)
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
            truth "But your lungs don't fill. Nor will they ever. It's time for you to leave. Memory returns.\n"
        else:
            truth "But your lungs don't fill, and both she and her bones are gone. Something has taken them away, and it's left something else in their place.\n"
        $ grey_end = "drown"
        $ princess_kept += 1
        $ princess_deny += 1
        jump mirror_start
        # END

return
