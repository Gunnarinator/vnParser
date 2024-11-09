label damsel_1_encounter_start:

    default damsel_can_slay_attempt = True
    voice "audio/voices/ch2/damsel/_basement/princess/1.flac"
    show damsel d kawaii talk onlayer back
    with dissolve
    p "It's you! My dashing hero. I was so worried you wouldn't come back.\n"
    voice "audio/voices/ch2/damsel/_basement/smitten/1.flac"
    show damsel d kawaii onlayer back
    smitten "Did you hear that? She said we're dashing!\n"
    voice "audio/voices/ch2/damsel/_basement/hero/1.flac"
    hero "And she called us a hero!\n"
    voice "audio/voices/ch2/damsel/_basement/narrator/1.flac"
    n "Flattery really goes a long way with the two of you, doesn't it?\n"
    if damsel_1_forest_share_loop:
        voice "audio/voices/ch2/damsel/_basement/narrator/2.flac"
        n "'Waiting for you to come back?' I didn't want to believe your ravings back in the woods, but this is next to incontrovertible evidence. You've been here before.\n" id damsel_1_encounter_start_7d41bf22
    else:
        voice "audio/voices/ch2/damsel/_basement/narrator/3.flac"
        n "'Waiting for you to come back?' You've been here before, haven't you?\n"

    voice "audio/voices/ch2/damsel/_basement/smitten/2.flac"
    smitten "That's right, villain. And you killed us.\n"
    voice "audio/voices/ch2/damsel/_basement/hero/2.flac"
    hero "Well... she killed us.\n"
    voice "audio/voices/ch2/damsel/_basement/smitten/3.flac"
    smitten "Only because he made us try and kill her! It was self-defense. Our beloved's hands remain unstained by cruelty.\n"
    voice "audio/voices/ch2/damsel/_basement/narrator/4.flac"
    n "And you've died before. So an entire world has been damned to oblivion. I'd really hoped I'd be the first... but what's done is done. What matters is you have a chance to do it right this time.\n"
    if damsel_1_forest_share_loop_insist == False:
        voice "audio/voices/ch2/damsel/_basement/hero/3.flac"
        hero "We... damned a whole world? But everything reset.\n"
        voice "audio/voices/ch2/damsel/_basement/narrator/5.flac"
        n "Nothing 'resets.' You're just somewhere else, and you can't keep hopping between worlds forever. Especially not without leaving a trail of incomprehensible devastation behind you. {i}Sigh{/i}. This is horrible.\n"
        #voice "audio/voices/ch2/damsel/_basement/smitten/4.flac"
        #smitten "Horrible for you, maybe, but we've been given another opportunity to sweep her off her feet and treat her like the lady she is.\n"
    else:
        voice "audio/voices/ch2/damsel/_basement/hero/4.flac"
        hero "Now hold on. If she actually {i}ended{/i} a world... are you sure we want to do this? Are you sure we want to {i}rescue{/i} her?\n"
        #voice "audio/voices/ch2/damsel/_basement/smitten/5.flac"
        #smitten "We never saw a world end. And now I'm even more certain that we must chase our heroic and romantic destiny than I've ever been. I shan't let anyone convince us otherwise!\n"
        #voice "audio/voices/ch2/damsel/_basement/narrator/6.flac"
        #n "Are you listening to him? He's lost it. Don't let him distract you, just do your job.\n"

label damsel_1_menu:
    default damsel_rescue_no_cut = False
    default damsel_after_die = False
    default damsel_end_world = False
    default damsel_end_world_flavor = ""
    default damsel_kill_last_time = False
    default damsel_how_free = False
    default damsel_sorry = False
    menu:
        extend ""

        "{i}• (Explore) ''You killed me last time and it hurt a lot! Why did you do that?''{/i}" if damsel_kill_last_time == False:
            $ damsel_kill_last_time = True
            voice "audio/voices/ch2/damsel/_basement/princess/2.flac"
            show damsel d confused smile talk onlayer back
            with dissolve
            p "I'm sorry! Didn't you want me to?\n"
            show damsel d confused smile onlayer back
            voice "audio/voices/ch2/damsel/_basement/hero/5.flac"
            hero "... Did we?\n"
            voice "audio/voices/ch2/damsel/_basement/smitten/6.flac"
            smitten "We warned her of the cruel forces seizing our body. That's practically telling her to kill us. She is our beloved, and she made the choice to free us of our misery, to show us mercy and make the best decision for everyone.\n"
            voice "audio/voices/ch2/damsel/_basement/narrator/7.flac"
            n "She made the best decision for her. Don't be so quick to assign kindness, you're just opening yourself up to manipulation.\n"
            jump damsel_1_menu

        "{i}• (Explore) ''I didn't bring a knife. Do I have to cut you out again?''{/i}" if damsel_how_free == False and blade_held == False:
            jump damsel_how_free_join

        "{i}• (Explore) ''Do I have to cut you out again? I really didn't care for that last time.''{/i}" if damsel_how_free == False and blade_held:
            label damsel_how_free_join:
                $ damsel_how_free = True
                voice "audio/voices/ch2/damsel/_basement/princess/3.flac"
                show damsel d kawaii talk onlayer back
                with dissolve
                p "I'm okay with whatever you come up with. You can cut my arm off again.\n"
                show damsel d kawaii onlayer back
                voice "audio/voices/ch2/damsel/_basement/smitten/7.flac"
                smitten "We won't be laying a finger on her perfect wrists, and indeed, we won't even have to! Do you see how dainty her hands are? We'll be able to slip her right out, with no harm done.\n"
                voice "audio/voices/ch2/damsel/_basement/narrator/8.flac"
                n "What?! No. She's a prisoner here. You can't just slip her hand through the chains!\n"
                voice "audio/voices/ch2/damsel/_basement/hero/6.flac"
                hero "Why are you two arguing over the logistics of slipping her hand out of her shackles? She just said she'd be okay with {i}any{/i} idea we came up with. Am I the only one here who thinks that's weird?\n"
                voice "audio/voices/ch2/damsel/_basement/smitten/8.flac"
                smitten "She didn't care last time! Why should she care this time? That's our stoic, smiling angel.\n"
                voice "audio/voices/ch2/damsel/_basement/narrator/9.flac"
                n "No, you're right. It's extremely bizarre behavior, and further evidence that she's a monster who's not to be trusted. So go ahead and slay her.\n"
                jump damsel_1_menu

        "{i}• (Explore) ''What happened after I died?''{/i}" if damsel_after_die == False:
            $ damsel_after_die = True
            voice "audio/voices/ch2/damsel/_basement/princess/4.flac"
            show damsel d smile talk onlayer back
            with dissolve
            p "You died! And now we're talking.\n"
            show damsel d neutral onlayer back
            jump damsel_1_menu

        "{i}• (Explore) ''But before we started talking, did the world end? Did you end the world?''{/i}" if damsel_after_die and damsel_end_world == False:
            jump damsel_end_world_join

        "{i}• (Explore) ''I have to ask... did you end the world after you killed me back there?''{/i}" if damsel_after_die == False and damsel_end_world == False:
            label damsel_end_world_join:
                $ damsel_end_world = True
                voice "audio/voices/ch2/damsel/_basement/princess/5.flac"
                show damsel d confused smile talk onlayer back
                with dissolve
                p "I don't know. Was I supposed to have ended the world? Would that have made you happy?\n"
                show damsel d confused smile onlayer back
                voice "audio/voices/ch2/damsel/_basement/smitten/9.flac"
                smitten "Isn't that just like our darling Princess? She wants to make us happy! My heart melts further with every word that passes through her beautiful lips.\n"
                voice "audio/voices/ch2/damsel/_basement/narrator/10.flac"
                n "Are you listening to her? That's a {i}confession{/i}.\n"
                menu:
                    extend ""

                    "{i}• ''No? I don't want the world to end.''{/i}":
                        $ damsel_end_world_flavor = "save"
                        voice "audio/voices/ch2/damsel/_basement/princess/6.flac"
                        show damsel d kawaii talk onlayer back
                        with dissolve
                        p "Then I didn't end the world!\n"
                        show damsel d kawaii onlayer back
                        voice "audio/voices/ch2/damsel/_basement/smitten/10.flac"
                        smitten "See? She didn't confess anything! She is innocence itself!\n"
                        voice "audio/voices/ch2/damsel/_basement/hero/7.flac"
                        hero "I'm... not so sure.\n"

                    "{i}• ''I have no feelings one way or the other about the world ending.''{/i}":
                        $ damsel_end_world_flavor = "neutral"
                        voice "audio/voices/ch2/damsel/_basement/narrator/11.flac"
                        n "At least you're being honest. {i}Sigh{/i}. I can't believe that the fate of the entire world has been left in the hands of a nihilist.\n"
                        voice "audio/voices/ch2/damsel/_basement/princess/7.flac"
                        show damsel d neutral onlayer back
                        p "Um...\n"
                        voice "audio/voices/ch2/damsel/_basement/narrator/12.flac"
                        n "The Princess shifts in uncomfortable confusion.\n"
                        voice "audio/voices/ch2/damsel/_basement/princess/8.flac"
                        show damsel d kawaii talk onlayer back
                        with dissolve
                        p "Me too! I don't care!\n"
                        show damsel d kawaii onlayer back
                        voice "audio/voices/ch2/damsel/_basement/hero/8.flac"
                        hero "She wasn't confused for long.\n"
                        voice "audio/voices/ch2/damsel/_basement/smitten/11.flac"
                        smitten "If she doesn't care then clearly she didn't end the world! It would take a great desire for evil to do something so inconceivable, and our dearest has not an ounce of cruelty within her. All is well, and it's high time we rescued our beloved.\n"

                    "{i}• ''Honestly, the world sucks. People are a plague and I hope you brought a slow and painful ruin to them all.''{/i}":
                        $ damsel_end_world_flavor = "burn"
                        voice "audio/voices/ch2/damsel/_basement/narrator/13.flac"
                        n "{i}Sigh{/i}. I can't believe that the fate of the entire world has been left in the hands of a misanthrope.\n"
                        voice "audio/voices/ch2/damsel/_basement/princess/9a.flac"
                        show damsel d kawaii talk onlayer back
                        with dissolve
                        p "Lucky for you, I did destroy the world! I destroyed all of it and made it awful for everyone.\n"
                        voice "audio/voices/ch2/damsel/_basement/narrator/14.flac"
                        show damsel d kawaii onlayer back
                        n "I'd point out that she just admitted to obliterating the entire world, but I guess that wouldn't actually move you.\n"
                        voice "audio/voices/ch2/damsel/_basement/hero/9.flac"
                        hero "Oh, it moves me. Whatever we do next, we should do our best to {i}not{/i} let her out.\n"
                        voice "audio/voices/ch2/damsel/_basement/smitten/12.flac"
                        smitten "But have you seen her angelic face? She should get a pass! She just wanted to make us happy.\n"
                        voice "audio/voices/ch2/damsel/_basement/hero/10.flac"
                        hero "By destroying the world?\n"
                        voice "audio/voices/ch2/damsel/_basement/smitten/13.flac"
                        smitten "Apparently, yes!\n"

                    "{i}• [[Remain silent.]{/i}":
                        $ damsel_end_world_flavor = "silence"
                        voice "audio/voices/ch2/damsel/_basement/narrator/15.flac"
                        n "The Princess' eyes quiver as she waits for your response.\n"
                        voice "audio/voices/ch2/damsel/_basement/princess/10.flac"
                        show damsel d neutral onlayer back
                        with dissolve
                        p "I... didn't? End the world?\n"
                        voice "audio/voices/ch2/damsel/_basement/princess/11.flac"
                        show damsel d kawaii talk onlayer back
                        with dissolve
                        p "I didn't end the world!\n"
                        voice "audio/voices/ch2/damsel/_basement/narrator/16.flac"
                        show damsel d kawaii onlayer back
                        n "She's clearly just saying what she thinks you want to hear.\n"
                        voice "audio/voices/ch2/damsel/_basement/smitten/14.flac"
                        smitten "Or she's innocent. How could a beauty like her be capable of ending the world? It's not rational!\n"

                jump damsel_1_menu

        "{i}• (Explore) ''I'm sorry about what happened last time. The Narrator who sent me here to kill you took over my body. It was extremely unfair.''{/i}" if damsel_sorry == False:
            $ damsel_sorry = True
            voice "audio/voices/ch2/damsel/_basement/narrator/17.flac"
            n "If another version of me was pushed to such drastic action, it was for a good reason!\n"
            voice "audio/voices/ch2/damsel/_basement/princess/12b.flac"
            show damsel d kawaii talk onlayer back
            with dissolve
            p "That's okay! You were just doing your best, and that's all that matters.\n"
            voice "audio/voices/ch2/damsel/_basement/hero/11.flac"
            show damsel d kawaii onlayer back
            hero "She took that in stride. To a surprising extent. An almost unsettling extent, actually.\n"
            voice "audio/voices/ch2/damsel/_basement/smitten/15.flac"
            smitten "That's because she's perfect!\n"
            voice "audio/voices/ch2/damsel/_basement/hero/12.flac"
            hero "Do you think she has someone like Him telling her what to do?\n"
            voice "audio/voices/ch2/damsel/_basement/narrator/18a.flac"
            n "She doesn't. There's no one else like me.\n"
            voice "audio/voices/ch2/damsel/_basement/smitten/16.flac"
            smitten "I think he's right. Because I like it better if she doesn't have some horrid little voice like Him always trying to drive her to violence.\n"
            jump damsel_1_menu

        "{i}• [[Rescue the Princess.]{/i}":
            jump damsel_1_free

        "{i}• [[Slay the Princess.]{/i}" if blade_held and damsel_can_slay_attempt:
            if grey_encountered:
                $ damsel_can_slay_attempt = False
                voice "audio/voices/mound/bonus/path.flac"
                mound "This path is already worn by travel and has been seen by one of my many eyes. You cannot walk it again. Change your course.\n"
                voice "audio/voices/ch2/beast/_encounter/hero/31.flac"
                hero "Wait... what?!\n"
                jump damsel_1_menu
            $ damsel_depersonalization_count -= 1
            voice "audio/voices/ch2/damsel/_basement/narrator/19.flac"
            play audio "audio/one_shot/footstep_run_dirt_short.flac"
            hide bg onlayer back
            hide farback onlayer farback
            hide damsel onlayer back
            show bg damsel charge onlayer farback at Position(ypos=1125)
            show damsel charge onlayer back at Position(ypos=1125)
            show player clean knife onlayer front at Position(ypos=1125)
            show speedlines onlayer inyourface at Position(ypos=1125)
            with dissolve
            n "Blade in hand, you run the Princess down.\n"
            voice "audio/voices/ch2/damsel/_basement/smitten/17.flac"
            smitten "Wait! No! You barbarian! What do you think you're doing?\n"
            voice "audio/voices/ch2/damsel/_basement/narrator/20.flac"
            n "But you ignore the pleas of the foolish little voice and press on. The Princess' eyes grow wide with terror as you approach, but she does absolutely nothing to stop you.\n"
            $ gallery_damsel.unlock_item(12)
            $ renpy.save_persistent()
            jump damsel_1_murder

label damsel_1_murder:
    $ quick_menu = False
    $ default_mouse = "blood"
    voice "audio/voices/ch2/damsel/_basement/narrator/21.flac"
    play tertiary "audio/one_shot/knife_stab.flac"
    queue tertiary "audio/one_shot/collapse.flac"
    hide bg onlayer farback
    hide damsel onlayer back
    hide player onlayer front
    hide speedlines onlayer inyourface
    show bg cg damsel stabbed collapse onlayer back at Position(ypos=1125)
    show damsel stabbed onlayer back at Position(ypos=1125)
    with fade
    if persistent.quick_menu:
        $ quick_menu = True
    n "Your blade pierces her heart, and she collapses pathetically to the ground.\n"
    if damsel_depersonalization_count == 0 or damsel_depersonalization_count == -1:
        voice "audio/voices/ch2/damsel/_basement/princess/13.flac"
    elif damsel_depersonalization_count == 1:
        voice "audio/voices/ch2/damsel/_basement/princess/13a.flac"
    elif damsel_depersonalization_count == 2:
        voice "audio/voices/ch2/damsel/_basement/princess/13b.flac"
    else:
        voice "audio/voices/ch2/damsel/_basement/princess/13c.flac"
    show damsel stabbed talk onlayer back
    p "I'm sorry... did I do something wrong?\n"
    voice "audio/voices/ch2/damsel/_basement/smitten/18a.flac"
    smitten "No, my love! You did nothing wrong! I'm sorry! I'M SORRY, NOT YOU!\n"
    if damsel_depersonalization_count == 0 or damsel_depersonalization_count == -1:
        voice "audio/voices/ch2/damsel/_basement/princess/14_1.flac"
    elif damsel_depersonalization_count == 1:
        voice "audio/voices/ch2/damsel/_basement/princess/14a.flac"
    elif damsel_depersonalization_count == 2:
        voice "audio/voices/ch2/damsel/_basement/princess/14b.flac"
    else:
        voice "audio/voices/ch2/damsel/_basement/princess/14c.flac"
    show damsel stabbed dead talk onlayer back
    with dissolve
    p "I'm going to die now. I think that's what you want.\n"
    show damsel stabbed dead onlayer back
    $ achievement.grant("ACH_DAMSEL_SLAY")
    $ renpy.music.set_volume(1.0, 3.0, channel='music')
    $ renpy.music.set_volume(0.0, 3.0, channel='music2')
    $ renpy.music.set_volume(0.0, 3.0, channel='music3')
    $ renpy.music.set_volume(0.0, 3.0, channel='music4')
    $ renpy.music.set_volume(0.0, 3.0, channel='music5')
    stop music fadeout 3.0
    stop music2 fadeout 3.0
    stop music3 fadeout 3.0
    stop music4 fadeout 3.0
    stop music5 fadeout 3.0
    voice "audio/voices/ch2/damsel/_basement/narrator/22.flac"
    n "And just like that, she's dead. And the world is saved. Thank you for seeing this through. I know it must have been difficult.\n"
    voice "audio/voices/ch2/damsel/_basement/hero/13.flac"
    hero "I feel sick.\n"
    voice "audio/voices/ch2/damsel/_basement/smitten/19.flac"
    smitten "Sick?! You took part in the murder of the fairest creature that's ever lived, and you merely feel sick? I for one am absolutely distraught! Grief-stricken. Inconsolable!\n"
    voice "audio/voices/ch2/damsel/_basement/narrator/23.flac"
    n "You'll get over it. You just saved everyone.\n"
    play audio "audio/one_shot/knife_pickup.flac"
    $ blade_held = True
    $ default_mouse = "blood"
    voice "audio/voices/ch2/damsel/_basement/smitten/20.flac"
    smitten "'Get over it?' You smarmy ass. There's nothing in the world worth 'getting over it' for. We might as well just end it all.\n"
    voice "audio/voices/ch2/damsel/_basement/narrator/24.flac"
    hide bg onlayer back
    hide damsel onlayer back
    scene bg generic dark onlayer back at Position(ypos=1125)
    show player self end onlayer front at Position(ypos=1125)
    with fade
    n "You raise the blade, aiming the point directly towards your heart — excuse me?! No, you absolutely do not do that.\n"
    # FAST
    voice "audio/voices/ch2/damsel/_basement/hero/14.flac"
    hero "Yeah, let's not make any rash decisions, we should give ourselves a minute, take a deep breath and—!\n"
    voice "audio/voices/ch2/damsel/_basement/smitten/21.flac"
    smitten "Rash? The only rash decision we've made was running our cursed blade through her heart. This is far from rash. This is measured. This is the only thing left for us to do now that she's gone.\n"

    menu:
        extend ""

        "{i}• ''I'm the one who makes the decisions here, and I say {b}no{/b}!''{/i}":
            voice "audio/voices/ch2/damsel/_basement/hero/15.flac"
            hero "Exactly! You're not doing this.\n"
            jump damsel_1_murder_2

        "{i}• ''If that's what you want to do, let's see what happens.''{/i}":
            voice "audio/voices/ch2/damsel/_basement/hero/16.flac"
            hero "What? No, let's not do that!\n"
            voice "audio/voices/ch2/damsel/_basement/smitten/22.flac"
            smitten "You won't use your fancy reverse psychotherapeutics on me, murderer. We're dying together right now.\n"
            jump damsel_1_murder_2

        "{i}• [[Remain silent.]{/i}":
            voice "audio/voices/ch2/damsel/_basement/hero/17.flac"
            hero "Really? You're not going to say {i}anything{/i}?\n"
            jump damsel_1_murder_2


    label damsel_1_murder_2:
        voice "audio/voices/ch2/damsel/_basement/smitten/23.flac"
        smitten "All of you may have previously thought that my passions were too great to stifle, but those were merely passions of joy! My passions of sorrow run deeper than the ocean itself, and you'll find that they are far more unstiflable. Have at you! Have at you all!\n"
        voice "audio/voices/ch2/damsel/_basement/narrator/25.flac"
        n "I don't believe this.\n"
        voice "audio/voices/ch2/damsel/_basement/hero/18.flac"
        hero "What? What don't you believe?\n"
        voice "audio/voices/ch2/damsel/_basement/narrator/26.flac"
        $ quick_menu = False
        play tertiary "audio/one_shot/knife_stab.flac"
        queue tertiary "audio/one_shot/collapse.flac"
        hide bg onlayer back
        hide player onlayer front
        show bg cg damsel die together onlayer back at Position(ypos=1125)
        show damsel dead floor onlayer back at Position(ypos=1125)
        with fade
        if persistent.quick_menu:
            $ quick_menu = True
        n "You plunge the blade into your own heart, and collapse to the floor.\n"
        voice "audio/voices/ch2/damsel/_basement/hero/19.flac"
        hero "You can't be serious! Why are you helping him?\n"
        voice "audio/voices/ch2/damsel/_basement/narrator/27.flac"
        n "I'm not. He just... made it happen. I'm sorry.\n"
        voice "audio/voices/ch2/damsel/_basement/smitten/24.flac"
        smitten "That's right. You're all sorry.\n"
        hide bg onlayer back
        hide damsel onlayer back
        scene bg black
        with fade
        voice "audio/voices/ch2/damsel/_basement/narrator/28.flac"
        n "Everything goes dark, and you die.\n"
        jump grey_start

label damsel_1_free:
    if damsel_how_free == False:
        voice "audio/voices/ch2/damsel/_basement/narrator/29.flac"
        n "Rescue her? What are you talking about? Did you forget that she's a world-ending monstrosity? And even if you wanted to unleash her onto the world, despite the complete moral disaster that would be, you'd have to get her out of those chains. Good luck with that!\n"
        voice "audio/voices/ch2/damsel/_basement/smitten/25.flac"
        smitten "Don't you see how dainty her hands are? We'll be able to slip her out with ease.\n"
        voice "audio/voices/ch2/damsel/_basement/narrator/30.flac"
        n "No! She's a prisoner here. You can't just slip her hand through the chains!\n"
        voice "audio/voices/ch2/damsel/_basement/hero/20.flac"
        hero "If her hands could just slip out of the chains, why hasn't she done it already?\n"
        voice "audio/voices/ch2/damsel/_basement/smitten/26.flac"
        smitten "Because we've yet to present her with her freedom.\n"
        voice "audio/voices/ch2/damsel/_basement/hero/21.flac"
        hero "I'm not sure I follow.\n"
        voice "audio/voices/ch2/damsel/_basement/smitten/27.flac"
        smitten "Would you rather believe me, a passionate heart guided by love and my own good nature, or would you rather believe the devil on your shoulder who tells you what you can and cannot do?\n"
        voice "audio/voices/ch2/damsel/_basement/hero/22.flac"
        hero "I think I'd rather believe in facts.\n"
        voice "audio/voices/ch2/damsel/_basement/smitten/28.flac"
        smitten "Ah, so you're one of those empiricists.\n"
        voice "audio/voices/ch2/damsel/_basement/hero/23.flac"
        hero "One of us has to be.\n"
        voice "audio/voices/ch2/damsel/_basement/smitten/29.flac"
        smitten "Then let me show you a brand new truth. Narrator! We courageously step forward and free our beloved from her bindings.\n"

    # FAST
    voice "audio/voices/ch2/damsel/_basement/narrator/31.flac"
    n "No. I can't let you do that. If you take another step towards the Princess, I'll—\n{w=5.1}{nw}"
    show screen disableclick(0.5)
    voice "audio/voices/ch2/damsel/_basement/hero/24.flac"
    hero "You'll what? Take over our body and force us to try and kill her?\n"
    if blade_held:
        voice "audio/voices/ch2/damsel/_basement/narrator/32.flac"
        n "Yes.\n"
    else:
        voice "audio/voices/ch2/damsel/_basement/narrator/33.flac"
        n "I would if you had a weapon.\n"
    voice "audio/voices/ch2/damsel/_basement/smitten/30.flac"
    smitten "Not on my watch, villain! My passions contain titanic depths, and if you try {i}anything{/i} that might harm our dearest I will end our life without a second thought.\n"
    voice "audio/voices/ch2/damsel/_basement/narrator/34.flac"
    n "You wouldn't.\n"
    voice "audio/voices/ch2/damsel/_basement/smitten/31.flac"
    smitten "I would!\n"
    voice "audio/voices/ch2/damsel/_basement/hero/25.flac"
    hero "I'd listen to him if I were you. He has a lot of strong feelings. And doesn't the world end if we don't stop her?\n"
    voice "audio/voices/ch2/damsel/_basement/narrator/35.flac"
    play tertiary "audio/one_shot/footsteps_creaky.flac"
    queue tertiary "audio/one_shot/chain_1.flac"
    hide bg onlayer back
    hide farback onlayer back
    hide damsel onlayer back
    show bg cg damsel free onlayer farback at Position(ypos=1125)
    show cg damsel free onlayer back at Position(ypos=1125)
    with Dissolve(1.5)
    n "{i}Sigh{/i}. You approach the Princess and gingerly slide her hand from her bindings. That... shouldn't have worked. I'll be damned. We're doomed.\n"
    voice "audio/voices/ch2/damsel/_basement/hero/26.flac"
    hero "I can't believe it. But I guess I have to.\n"
    voice "audio/voices/ch2/damsel/_basement/smitten/32.flac"
    smitten "I told you! There's no life more worth living than that of a true believer.\n"
    $ gallery_damsel.unlock_item(3)
    $ renpy.save_persistent()
    voice "audio/voices/ch2/damsel/_basement/princess/15.flac"
    play audio "audio/one_shot/knife_bounce_several.flac"
    show cg damsel free talk onlayer back
    with dissolve
    p "I'm free! And you're not trying to kill me this time! Thank you, thank you so much!\n"
    $ gallery_damsel.unlock_item(4)
    $ renpy.save_persistent()
    voice "audio/voices/ch2/damsel/_basement/narrator/36.flac"
    hide cg onlayer back
    hide bg onlayer farback
    show bg cg damsel hug onlayer back at Position(ypos=1125)
    show cg damsel hug onlayer front at Position(ypos=1125)
    with dissolve
    n "The Princess jumps up and smothers you in a joyful embrace. Eugh.\n"
    if blade_held:
        voice "audio/voices/ch2/damsel/_basement/narrator/37.flac"
        n "Are you {i}sure{/i} you want to do this? Just one slip of the wrist and your pristine blade is buried in her back, and everyone out there is saved.\n"
        voice "audio/voices/ch2/damsel/_basement/hero/27.flac"
        hero "Is that a threat?\n"
        voice "audio/voices/ch2/damsel/_basement/smitten/33.flac"
        smitten "You know what we'll do if you try it.\n"
        voice "audio/voices/ch2/damsel/_basement/narrator/38.flac"
        n "You're going to regret this.\n"
    else:
        voice "audio/voices/ch2/damsel/_basement/narrator/39.flac"
        n "If only you had a weapon. One slip of the wrist and your pristine blade would be buried in her back, and everyone out there would be saved.\n"
        voice "audio/voices/ch2/damsel/_basement/hero/28.flac"
        hero "Luckily for mister romance, we don't have a weapon.\n"
        voice "audio/voices/ch2/damsel/_basement/smitten/34a.flac"
        smitten "Who needs a weapon when we have the power of love on our side?\n"
        #voice "audio/voices/ch2/damsel/_basement/smitten/34.flac"
        #smitten "That's right! Harming her is out of the picture. Who needs a weapon when we have the power of love on our side?\n"
    voice "audio/voices/ch2/damsel/_basement/princess/16.flac"
    hide bg onlayer back
    hide cg onlayer front
    show bg damsel free c smile onlayer back at Position(ypos=1125)
    show damsel c smile talk onlayer front at Position(ypos=1125)
    with dissolve
    p "... What do we do now?\n"
    show damsel c smile onlayer front
    label damsel_free_menu:
        default damsel_what_want = False
        menu:
            extend ""

            "{i}• (Explore) ''What do you want to do?''{/i}" if damsel_what_want == False:
                $ damsel_what_want = True
                voice "audio/voices/ch2/damsel/_basement/narrator/40.flac"
                n "Let me guess. 'End the world?'\n"
                voice "audio/voices/ch2/damsel/_basement/smitten/35.flac"
                smitten "Spoken with the rank cynicism of someone who has never felt love in His heart.\n"
                voice "audio/voices/ch2/damsel/_basement/princess/17.flac"
                show damsel c confused smile talk onlayer front
                with dissolve
                p "I... don't actually know. Nobody's ever asked me what I've wanted before.\n"
                if what_would_you_do_1:
                    voice "audio/voices/ch2/damsel/_basement/princess/18.flac"
                    show damsel c kawaii talk onlayer front
                    with dissolve
                    p "I mean, you sort of did last time, but this is different.\n"
                show damsel c confused smile onlayer front
                #voice "audio/voices/ch2/damsel/_basement/hero/29a.flac"
                #hero "What if this whole thing is just a misunderstanding? What if she doesn't want to end the world?\n"
                voice "audio/voices/ch2/damsel/_basement/hero/29.flac"
                hero "She doesn't even know what she wants. You may have had her all wrong. What if this whole thing is just a misunderstanding? What if she doesn't want to end the world?\n"
                voice "audio/voices/ch2/damsel/_basement/narrator/41.flac"
                n "You're so gullible. Is the only thing you've ever doubted the actual truth?\n"
                voice "audio/voices/ch2/damsel/_basement/princess/19.flac"
                show damsel c confused smile talk onlayer front
                with dissolve
                p "I think I want to leave? And I think...\n"
                voice "audio/voices/ch2/damsel/_basement/narrator/42.flac"
                show damsel c kawaii onlayer front
                n "The Princess closes her eyes in deep reflection.\n"
                voice "audio/voices/ch2/damsel/_basement/narrator/43.flac"
                n "And then she shrugs.\n"
                voice "audio/voices/ch2/damsel/_basement/princess/20.flac"
                show damsel c smile talk onlayer front
                with dissolve
                p "I dunno. What do you want to do?\n"
                show damsel c smile onlayer front
                label damsel_depersonalization_menu:
                    default damsel_depersonalization_count = 0
                    default damsel_parrot_comment = False
                    default damsel_parrot_explore = False
                    default damsel_depersonalization_unhappy = False
                    if damsel_want_end_2_prev_flag == False:
                        if damsel_depersonalization_count == 1:
                            $ gallery_damsel.unlock_item(8)
                            $ renpy.save_persistent()
                            show quiet creep1 onlayer back at Position(ypos=1125)
                            with dissolve
                            voice "audio/voices/ch2/damsel/_basement/hero/30.flac"
                            hero "She can't {i}just{/i} want to make us happy.\n"
                            voice "audio/voices/ch2/damsel/_basement/smitten/36.flac"
                            smitten "It makes sense to me. That's all I want for her, so of course she'd want the same for us.\n"
                        elif damsel_depersonalization_count == 2:
                            $ gallery_damsel.unlock_item(9)
                            $ renpy.save_persistent()
                            show quiet creep2 onlayer back at Position(ypos=1125)
                            with dissolve
                            voice "audio/voices/ch2/damsel/_basement/hero/31.flac"
                            hero "Is she broken? What's going on?\n"
                            voice "audio/voices/ch2/damsel/_basement/narrator/44.flac"
                            n "What's going on is she's lying to you, only she isn't a good liar. Are you starting to trust me now?\n"
                        elif damsel_depersonalization_count == 3:
                            $ gallery_damsel.unlock_item(10)
                            $ renpy.save_persistent()
                            show quiet creep3 onlayer back at Position(ypos=1125)
                            with dissolve
                            voice "audio/voices/ch2/damsel/_basement/hero/32.flac"
                            hero "This isn't right! I don't know what's going on but this isn't right!\n"
                            voice "audio/voices/ch2/damsel/_basement/smitten/37.flac"
                            smitten "I fail to see the problem here. She's just sweet on us. You don't have to act like it's a big deal.\n"
                    else:
                        $ damsel_want_end_2_prev_flag = True

                    menu:
                        extend ""

                        "{i}• ''Okay. Clearly something is happening here, and I'm very scared. What if we just... don't do anything? What if we just stay here? Nobody gets hurt, and we just figure out a way to be happy, together.''{/i}" if damsel_depersonalization_count >= 3:
                            default damsel_hea_dereal_flag = False
                            $ damsel_hea_dereal_flag = True
                            # PRISTINE CUT
                            $ renpy.music.set_volume(1.0, 0.0, channel='music')
                            $ renpy.music.set_volume(0.0, 0.0, channel='music2')
                            $ renpy.music.set_volume(0.0, 0.0, channel='music3')
                            $ renpy.music.set_volume(0.0, 0.0, channel='music4')
                            $ renpy.music.set_volume(0.0, 0.0, channel='music5')
                            stop music2 fadeout 3.0
                            stop music3 fadeout 3.0
                            stop music4 fadeout 3.0
                            stop music5 fadeout 3.0
                            voice "audio/_pristine/voice/happy/princess/1.flac"
                            show damsel disc talk onlayer front
                            hide quiet onlayer back
                            p "Oh... is that really what you want? If you think that would make you happy, then...\n"
                            voice "audio/_pristine/voice/happy/narrator/1.flac"
                            show damsel disc eyes onlayer front
                            with dissolve
                            n "Her eyes dart uncomfortably to the corners of the room.\n"
                            voice "audio/_pristine/voice/happy/princess/2.flac"
                            show damsel disc eyes talk onlayer front
                            with dissolve
                            p "I guess we could do that.\n"
                            voice "audio/_pristine/voice/happy/hero/1.flac"
                            show damsel disc meh onlayer front
                            with dissolve
                            hero "At least she's normal again.\n"
                            voice "audio/_pristine/voice/happy/smitten/1.flac"
                            smitten "Normal again? Can't you tell? She's sad! She's distraught! This is unacceptable.\n"
                            $ trait_paranoid = True
                            jump damsel_happy_late_join

                        "{i}• (Explore) ''You're just parroting my questions. What do you actually want?''{/i}" if damsel_parrot_comment and damsel_parrot_explore == False:
                            $ damsel_depersonalization_count += 1
                            $ damsel_parrot_explore = True
                            if damsel_depersonalization_count == 1:
                                $ renpy.music.set_volume(0.0, 2.0, channel='music')
                                $ renpy.music.set_volume(1.0, 2.0, channel='music2')
                            if damsel_depersonalization_count == 2:
                                $ renpy.music.set_volume(0.0, 2.0, channel='music2')
                                $ renpy.music.set_volume(1.0, 2.0, channel='music3')
                            if damsel_depersonalization_count == 3:
                                $ renpy.music.set_volume(0.0, 2.0, channel='music3')
                                $ renpy.music.set_volume(1.0, 2.0, channel='music4')
                            if damsel_depersonalization_count == 1:
                                $ renpy.music.set_volume(0.0, 2.0, channel='music4')
                                $ renpy.music.set_volume(1.0, 2.0, channel='music5')
                            if damsel_depersonalization_count == 1:
                                voice "audio/voices/ch2/damsel/_basement/princess/21.flac"
                            elif damsel_depersonalization_count == 2:
                                voice "audio/voices/ch2/damsel/_basement/princess/21a.flac"
                            elif damsel_depersonalization_count == 3:
                                voice "audio/voices/ch2/damsel/_basement/princess/21b.flac"
                            else:
                                voice "audio/voices/ch2/damsel/_basement/princess/21c.flac"
                            show damsel c idea talk onlayer front
                            p "I just want to make you happy!\n"
                            show damsel c idea onlayer front
                            if damsel_depersonalization_count == 4:
                                jump damsel_personalization_end
                            jump damsel_depersonalization_menu

                        "{i}• (Explore) ''I want you to tell me what you want.''{/i}" if damsel_tell_what_want == False:
                            default damsel_tell_what_want = False
                            $ damsel_tell_what_want = True
                            $ damsel_depersonalization_count += 1
                            if damsel_depersonalization_count == 1:
                                $ renpy.music.set_volume(0.0, 2.0, channel='music')
                                $ renpy.music.set_volume(1.0, 2.0, channel='music2')
                            if damsel_depersonalization_count == 2:
                                $ renpy.music.set_volume(0.0, 2.0, channel='music2')
                                $ renpy.music.set_volume(1.0, 2.0, channel='music3')
                            if damsel_depersonalization_count == 3:
                                $ renpy.music.set_volume(0.0, 2.0, channel='music3')
                                $ renpy.music.set_volume(1.0, 2.0, channel='music4')
                            if damsel_depersonalization_count == 1:
                                $ renpy.music.set_volume(0.0, 2.0, channel='music4')
                                $ renpy.music.set_volume(1.0, 2.0, channel='music5')
                            if damsel_depersonalization_count == 1:
                                voice "audio/voices/ch2/damsel/_basement/princess/21.flac"
                            elif damsel_depersonalization_count == 2:
                                voice "audio/voices/ch2/damsel/_basement/princess/21a.flac"
                            elif damsel_depersonalization_count == 3:
                                voice "audio/voices/ch2/damsel/_basement/princess/21b.flac"
                            else:
                                voice "audio/voices/ch2/damsel/_basement/princess/21c.flac"
                            show damsel c idea talk onlayer front
                            p "I just want to make you happy!\n"
                            show damsel c idea onlayer front
                            if damsel_depersonalization_count == 4:
                                jump damsel_personalization_end
                            jump damsel_depersonalization_menu

                        "{i}• (Explore) ''There must be something you want!''{/i}" if damsel_tell_what_want_2 == False:
                            default damsel_tell_what_want_2 = False
                            $ damsel_tell_what_want_2 = True
                            $ damsel_depersonalization_count += 1
                            if damsel_depersonalization_count == 1:
                                $ renpy.music.set_volume(0.0, 2.0, channel='music')
                                $ renpy.music.set_volume(1.0, 2.0, channel='music2')
                            if damsel_depersonalization_count == 2:
                                $ renpy.music.set_volume(0.0, 2.0, channel='music2')
                                $ renpy.music.set_volume(1.0, 2.0, channel='music3')
                            if damsel_depersonalization_count == 3:
                                $ renpy.music.set_volume(0.0, 2.0, channel='music3')
                                $ renpy.music.set_volume(1.0, 2.0, channel='music4')
                            if damsel_depersonalization_count == 1:
                                $ renpy.music.set_volume(0.0, 2.0, channel='music4')
                                $ renpy.music.set_volume(1.0, 2.0, channel='music5')
                            if damsel_depersonalization_count == 1:
                                voice "audio/voices/ch2/damsel/_basement/princess/21.flac"
                            elif damsel_depersonalization_count == 2:
                                voice "audio/voices/ch2/damsel/_basement/princess/21a.flac"
                            elif damsel_depersonalization_count == 3:
                                voice "audio/voices/ch2/damsel/_basement/princess/21b.flac"
                            else:
                                voice "audio/voices/ch2/damsel/_basement/princess/21c.flac"
                            show damsel c idea talk onlayer front
                            p "I just want to make you happy!\n"
                            show damsel c idea onlayer front
                            if damsel_depersonalization_count == 4:
                                jump damsel_personalization_end
                            jump damsel_depersonalization_menu

                        "{i}• (Explore) ''But what would make you happy?''{/i}" if damsel_tell_what_make_happy == False and damsel_depersonalization_count >= 1:
                            default damsel_tell_what_make_happy = False
                            $ damsel_tell_what_make_happy = True
                            $ damsel_depersonalization_count += 1
                            if damsel_depersonalization_count == 1:
                                $ renpy.music.set_volume(0.0, 2.0, channel='music')
                                $ renpy.music.set_volume(1.0, 2.0, channel='music2')
                            if damsel_depersonalization_count == 2:
                                $ renpy.music.set_volume(0.0, 2.0, channel='music2')
                                $ renpy.music.set_volume(1.0, 2.0, channel='music3')
                            if damsel_depersonalization_count == 3:
                                $ renpy.music.set_volume(0.0, 2.0, channel='music3')
                                $ renpy.music.set_volume(1.0, 2.0, channel='music4')
                            if damsel_depersonalization_count == 1:
                                $ renpy.music.set_volume(0.0, 2.0, channel='music4')
                                $ renpy.music.set_volume(1.0, 2.0, channel='music5')
                            voice "audio/voices/ch2/damsel/_basement/princess/22.flac"
                            show damsel c idea talk onlayer front
                            p "I just want to make you happy?\n"
                            show damsel c idea onlayer front
                            if damsel_depersonalization_count == 4:
                                jump damsel_personalization_end
                            jump damsel_depersonalization_menu

                        "{i}• (Explore) ''You have to want something more than just making me happy.''{/i}" if damsel_depersonalization_count >= 1 and damsel_tell_what_make_happy_follow == False:
                            default damsel_tell_what_make_happy_follow = False
                            $ damsel_tell_what_make_happy_follow = True
                            $ damsel_depersonalization_count += 1
                            if damsel_depersonalization_count == 1:
                                $ renpy.music.set_volume(0.0, 2.0, channel='music')
                                $ renpy.music.set_volume(1.0, 2.0, channel='music2')
                            if damsel_depersonalization_count == 2:
                                $ renpy.music.set_volume(0.0, 2.0, channel='music2')
                                $ renpy.music.set_volume(1.0, 2.0, channel='music3')
                            if damsel_depersonalization_count == 3:
                                $ renpy.music.set_volume(0.0, 2.0, channel='music3')
                                $ renpy.music.set_volume(1.0, 2.0, channel='music4')
                            if damsel_depersonalization_count == 1:
                                $ renpy.music.set_volume(0.0, 2.0, channel='music4')
                                $ renpy.music.set_volume(1.0, 2.0, channel='music5')
                            if damsel_depersonalization_count == 1:
                                voice "audio/voices/ch2/damsel/_basement/princess/23.flac"
                            elif damsel_depersonalization_count == 2:
                                voice "audio/voices/ch2/damsel/_basement/princess/23a.flac"
                            elif damsel_depersonalization_count == 3:
                                voice "audio/voices/ch2/damsel/_basement/princess/23b.flac"
                            else:
                                voice "audio/voices/ch2/damsel/_basement/princess/23c.flac"
                            show damsel c idea talk onlayer front
                            p "Okay. I'll find something else to want if that makes you happy.\n"
                            show damsel c idea onlayer front
                            if damsel_depersonalization_count == 4:
                                jump damsel_personalization_end
                            jump damsel_depersonalization_menu

                        "{i}• (Explore) ''But you need your own thing. You just met me. You can't base your entire happiness around me.''{/i}" if damsel_depersonalization_count >= 1 and damsel_tell_what_make_happy_follow2 == False:
                            default damsel_tell_what_make_happy_follow2 = False
                            $ damsel_tell_what_make_happy_follow2 = True
                            $ damsel_depersonalization_count += 1
                            if damsel_depersonalization_count == 1:
                                $ renpy.music.set_volume(0.0, 2.0, channel='music')
                                $ renpy.music.set_volume(1.0, 2.0, channel='music2')
                            if damsel_depersonalization_count == 2:
                                $ renpy.music.set_volume(0.0, 2.0, channel='music2')
                                $ renpy.music.set_volume(1.0, 2.0, channel='music3')
                            if damsel_depersonalization_count == 3:
                                $ renpy.music.set_volume(0.0, 2.0, channel='music3')
                                $ renpy.music.set_volume(1.0, 2.0, channel='music4')
                            if damsel_depersonalization_count == 1:
                                $ renpy.music.set_volume(0.0, 2.0, channel='music4')
                                $ renpy.music.set_volume(1.0, 2.0, channel='music5')
                            if damsel_depersonalization_count == 1:
                                voice "audio/voices/ch2/damsel/_basement/princess/24.flac"
                            elif damsel_depersonalization_count == 2:
                                voice "audio/voices/ch2/damsel/_basement/princess/24a.flac"
                            elif damsel_depersonalization_count == 3:
                                voice "audio/voices/ch2/damsel/_basement/princess/24b.flac"
                            else:
                                voice "audio/voices/ch2/damsel/_basement/princess/24c.flac"
                            show damsel c idea talk onlayer front
                            p "Okay! If that's what makes you happy.\n"
                            show damsel c idea onlayer front
                            if damsel_depersonalization_count == 4:
                                jump damsel_personalization_end
                            jump damsel_depersonalization_menu

                        "{i}• (Explore) ''I want you to make me unhappy.''{/i}" if damsel_depersonalization_count >= 1 and damsel_want_unhappy == False:
                            default damsel_want_unhappy = False
                            $ damsel_want_unhappy = True
                            $ damsel_depersonalization_count += 1
                            if damsel_depersonalization_count == 1:
                                $ renpy.music.set_volume(0.0, 2.0, channel='music')
                                $ renpy.music.set_volume(1.0, 2.0, channel='music2')
                            if damsel_depersonalization_count == 2:
                                $ renpy.music.set_volume(0.0, 2.0, channel='music2')
                                $ renpy.music.set_volume(1.0, 2.0, channel='music3')
                            if damsel_depersonalization_count == 3:
                                $ renpy.music.set_volume(0.0, 2.0, channel='music3')
                                $ renpy.music.set_volume(1.0, 2.0, channel='music4')
                            if damsel_depersonalization_count == 1:
                                $ renpy.music.set_volume(0.0, 2.0, channel='music4')
                                $ renpy.music.set_volume(1.0, 2.0, channel='music5')
                            $ damsel_personalization_count_flag = True
                            if damsel_depersonalization_count == 1:
                                voice "audio/voices/ch2/damsel/_basement/princess/25.flac"
                            elif damsel_depersonalization_count == 2:
                                voice "audio/voices/ch2/damsel/_basement/princess/25a.flac"
                            elif damsel_depersonalization_count == 3:
                                voice "audio/voices/ch2/damsel/_basement/princess/25b.flac"
                            else:
                                voice "audio/voices/ch2/damsel/_basement/princess/25c.flac"
                            show damsel c idea talk onlayer front
                            p "Okay! If that's what makes you happy, I can make you unhappy.\n"
                            show damsel c idea onlayer front
                            if damsel_depersonalization_count == 4:
                                jump damsel_personalization_end
                            jump damsel_depersonalization_menu

                        "{i}• (Explore) ''Do you want to end the world?''{/i}" if damsel_want_end_2 == False:
                            default damsel_want_end_2 = False
                            default damsel_want_end_2_prev_flag = False
                            $ damsel_want_end_2_prev_flag = True
                            if damsel_depersonalization_count == 1:
                                $ renpy.music.set_volume(0.0, 2.0, channel='music')
                                $ renpy.music.set_volume(1.0, 2.0, channel='music2')
                            if damsel_depersonalization_count == 2:
                                $ renpy.music.set_volume(0.0, 2.0, channel='music2')
                                $ renpy.music.set_volume(1.0, 2.0, channel='music3')
                            if damsel_depersonalization_count == 3:
                                $ renpy.music.set_volume(0.0, 2.0, channel='music3')
                                $ renpy.music.set_volume(1.0, 2.0, channel='music4')
                            if damsel_depersonalization_count == 1:
                                $ renpy.music.set_volume(0.0, 2.0, channel='music4')
                                $ renpy.music.set_volume(1.0, 2.0, channel='music5')
                            $ damsel_personalization_count_flag = True
                            $ damsel_want_end_2 = True
                            voice "audio/voices/ch2/damsel/_basement/narrator/45.flac"
                            n "Are you seriously asking her that?\n"
                            if damsel_end_world:
                                if damsel_end_world_flavor == "burn":
                                    if damsel_depersonalization_count == 1:
                                        voice "audio/voices/ch2/damsel/_basement/princess/26.flac"
                                    elif damsel_depersonalization_count == 2:
                                        voice "audio/voices/ch2/damsel/_basement/princess/26a.flac"
                                    elif damsel_depersonalization_count == 3:
                                        voice "audio/voices/ch2/damsel/_basement/princess/26b.flac"
                                    else:
                                        voice "audio/voices/ch2/damsel/_basement/princess/26c.flac"
                                    show damsel c idea talk onlayer front
                                    p "Oh, we've been over this one. I do want to end the world!\n"
                                    show damsel c idea onlayer front
                                elif damsel_end_world_flavor == "neutral":
                                    if damsel_depersonalization_count == 1:
                                        voice "audio/voices/ch2/damsel/_basement/princess/27.flac"
                                    elif damsel_depersonalization_count == 2:
                                        voice "audio/voices/ch2/damsel/_basement/princess/27a.flac"
                                    elif damsel_depersonalization_count == 3:
                                        voice "audio/voices/ch2/damsel/_basement/princess/27b.flac"
                                    else:
                                        voice "audio/voices/ch2/damsel/_basement/princess/27c.flac"
                                    show damsel c idea talk onlayer front
                                    p "Oh, we've been over this one. I don't know!\n"
                                    show damsel c idea onlayer front
                                else:
                                    if damsel_depersonalization_count == 1:
                                        voice "audio/voices/ch2/damsel/_basement/princess/28.flac"
                                    elif damsel_depersonalization_count == 2:
                                        voice "audio/voices/ch2/damsel/_basement/princess/28a.flac"
                                    elif damsel_depersonalization_count == 3:
                                        voice "audio/voices/ch2/damsel/_basement/princess/28b.flac"
                                    else:
                                        voice "audio/voices/ch2/damsel/_basement/princess/28c.flac"
                                    show damsel c idea talk onlayer front
                                    p "Oh, we've been over this one. No! I do not want to end the world!\n"
                                    show damsel c idea onlayer front
                                jump damsel_depersonalization_menu
                            else:
                                if damsel_depersonalization_count == 0:
                                    voice "audio/voices/ch2/damsel/_basement/princess/5.flac"
                                    show damsel c idea talk onlayer front
                                    with dissolve
                                    p "I don't know. Was I supposed to have ended the world? Would that have made you happy?\n"
                                    show damsel c idea onlayer front
                                else:
                                    if damsel_depersonalization_count == 1:
                                        voice "audio/voices/ch2/damsel/_basement/princess/29.flac"
                                    elif damsel_depersonalization_count == 2:
                                        voice "audio/voices/ch2/damsel/_basement/princess/29a.flac"
                                    elif damsel_depersonalization_count == 3:
                                        voice "audio/voices/ch2/damsel/_basement/princess/29b.flac"
                                    else:
                                        voice "audio/voices/ch2/damsel/_basement/princess/29c.flac"
                                    show damsel c idea talk onlayer front
                                    p "Do you want to end the world?\n"
                                    show damsel c idea onlayer front
                                    if damsel_parrot_comment == False:
                                        $ damsel_parrot_comment = True
                                        voice "audio/voices/ch2/damsel/_basement/hero/33.flac"
                                        hero "She's just parroting our questions, isn't she?\n"
                                menu:
                                    extend ""

                                    "{i}• ''No? I don't want the world to end.''{/i}":
                                        $ damsel_end_world_flavor = "save"
                                        if blade_held:
                                            voice "audio/voices/ch2/damsel/_basement/narrator/46.flac"
                                            n "Good answer. Now slay her.\n"
                                        if damsel_depersonalization_count == 0:
                                            $ damsel_want_end_2_prev_flag = False
                                            $ damsel_depersonalization_count += 1
                                            $ renpy.music.set_volume(0.0, 2.0, channel='music')
                                            $ renpy.music.set_volume(1.0, 2.0, channel='music2')
                                        if damsel_depersonalization_count == 1:
                                            voice "audio/voices/ch2/damsel/_basement/princess/30.flac"
                                        elif damsel_depersonalization_count == 2:
                                            voice "audio/voices/ch2/damsel/_basement/princess/30a.flac"
                                        elif damsel_depersonalization_count == 3:
                                            voice "audio/voices/ch2/damsel/_basement/princess/30b.flac"
                                        else:
                                            voice "audio/voices/ch2/damsel/_basement/princess/30c.flac"
                                        show damsel c idea talk onlayer front
                                        p "If you don't want to end the world, then I don't want to end the world, either!\n"
                                        show damsel c idea onlayer front
                                        voice "audio/voices/ch2/damsel/_basement/smitten/38.flac"
                                        smitten "Why, why would you have us slay this beautiful creature? Did you not hear her just now? She specifically said she doesn't want to end the world.\n"
                                        voice "audio/voices/ch2/damsel/_basement/hero/34.flac"
                                        hero "Yeah, but aren't you getting the feeling she's just telling us what we want to hear?\n"
                                        voice "audio/voices/ch2/damsel/_basement/smitten/39.flac"
                                        smitten "Even if she was, isn't that a good thing? If only she could hear me, all I would ever say is what I think she would like to hear. That she's beautiful, and kind, and glows like the soft light of the moon...\n"
                                        voice "audio/voices/ch2/damsel/_basement/narrator/47.flac"
                                        n "You're better off not arguing with that dolt. You know what you have to do.\n"

                                    "{i}• ''I have no feelings about the world ending either way.''{/i}":
                                        $ damsel_end_world_flavor = "neutral"
                                        voice "audio/voices/ch2/damsel/_basement/narrator/11.flac"
                                        n "At least you're being honest. {i}Sigh{/i}. I can't believe that the fate of the entire world has been left in the hands of a nihilist.\n"
                                        if damsel_depersonalization_count == 0:
                                            $ damsel_want_end_2_prev_flag = False
                                            $ damsel_depersonalization_count += 1
                                            $ renpy.music.set_volume(0.0, 2.0, channel='music')
                                            $ renpy.music.set_volume(1.0, 2.0, channel='music2')
                                        if damsel_depersonalization_count == 1:
                                            voice "audio/voices/ch2/damsel/_basement/princess/31.flac"
                                        elif damsel_depersonalization_count == 2:
                                            voice "audio/voices/ch2/damsel/_basement/princess/31a.flac"
                                        elif damsel_depersonalization_count == 3:
                                            voice "audio/voices/ch2/damsel/_basement/princess/31b.flac"
                                        else:
                                            voice "audio/voices/ch2/damsel/_basement/princess/31c.flac"
                                        show damsel c idea talk onlayer front
                                        p "Um...\n"
                                        show damsel c idea onlayer front
                                        voice "audio/voices/ch2/damsel/_basement/narrator/12.flac"
                                        n "The Princess shifts in uncomfortable confusion.\n"
                                        if damsel_depersonalization_count == 1:
                                            voice "audio/voices/ch2/damsel/_basement/princess/32.flac"
                                        elif damsel_depersonalization_count == 2:
                                            voice "audio/voices/ch2/damsel/_basement/princess/32a.flac"
                                        elif damsel_depersonalization_count == 3:
                                            voice "audio/voices/ch2/damsel/_basement/princess/32b.flac"
                                        else:
                                            voice "audio/voices/ch2/damsel/_basement/princess/32c.flac"
                                        show damsel c idea talk onlayer front
                                        p "Me too! I don't care!\n"
                                        show damsel c idea onlayer front
                                        voice "audio/voices/ch2/damsel/_basement/hero/35.flac"
                                        hero "She wasn't confused for long.\n"
                                        voice "audio/voices/ch2/damsel/_basement/smitten/40.flac"
                                        smitten "If she doesn't care, then clearly she won't end the world! All is well, and it's high time we take our beloved to our happy ending.\n"

                                    "{i}• ''Honestly, the world sucks. People are a plague and I hope you bring a slow and painful ruin to them all.''{/i}":
                                        $ damsel_end_world_flavor = "burn"
                                        voice "audio/voices/ch2/damsel/_basement/narrator/13.flac"
                                        n "{i}Sigh{/i}. I can't believe that the fate of the entire world has been left in the hands of a misanthrope.\n"
                                        if damsel_depersonalization_count == 0:
                                            $ damsel_want_end_2_prev_flag = False
                                            $ damsel_depersonalization_count += 1
                                            $ renpy.music.set_volume(0.0, 2.0, channel='music')
                                            $ renpy.music.set_volume(1.0, 2.0, channel='music2')
                                        if damsel_depersonalization_count == 1:
                                            voice "audio/voices/ch2/damsel/_basement/princess/33.flac"
                                        elif damsel_depersonalization_count == 2:
                                            voice "audio/voices/ch2/damsel/_basement/princess/33a.flac"
                                        elif damsel_depersonalization_count == 3:
                                            voice "audio/voices/ch2/damsel/_basement/princess/33b.flac"
                                        else:
                                            voice "audio/voices/ch2/damsel/_basement/princess/33c.flac"
                                        show damsel c idea talk onlayer front
                                        p "Okay! If that's what you think is best, then that's what we'll do when we leave!\n"
                                        show damsel c idea onlayer front
                                        if damsel_depersonalization_count == 1:
                                            voice "audio/voices/ch2/damsel/_basement/princess/34.flac"
                                        elif damsel_depersonalization_count == 2:
                                            voice "audio/voices/ch2/damsel/_basement/princess/34a.flac"
                                        elif damsel_depersonalization_count == 3:
                                            voice "audio/voices/ch2/damsel/_basement/princess/34b.flac"
                                        else:
                                            voice "audio/voices/ch2/damsel/_basement/princess/34c.flac"
                                        show damsel c idea talk onlayer front
                                        p "We'll bring ruin to everyone and everything! Nothing will be left standing in the wake of the unceasing entropy we'll unleash upon all of creation.\n"
                                        show damsel c idea onlayer front
                                        voice "audio/voices/ch2/damsel/_basement/hero/36.flac"
                                        hero "Okay. So whatever we do next, we should {i}not{/i} let her out.\n"

                                    "{i}• [[Remain silent.]{/i}":
                                        $ damsel_end_world_flavor = "silence"
                                        voice "audio/voices/ch2/damsel/_basement/narrator/15.flac"
                                        n "The Princess' eyes quiver as she waits for your response.\n"
                                        if damsel_depersonalization_count == 0:
                                            $ damsel_depersonalization_count += 1
                                        if damsel_depersonalization_count == 1:
                                            voice "audio/voices/ch2/damsel/_basement/princess/35.flac"
                                        elif damsel_depersonalization_count == 2:
                                            voice "audio/voices/ch2/damsel/_basement/princess/35a.flac"
                                        elif damsel_depersonalization_count == 3:
                                            voice "audio/voices/ch2/damsel/_basement/princess/35b.flac"
                                        else:
                                            voice "audio/voices/ch2/damsel/_basement/princess/35c.flac"
                                        show damsel c idea talk onlayer front
                                        p "I... don't? Want to end the world?\n"
                                        if damsel_depersonalization_count == 1:
                                            voice "audio/voices/ch2/damsel/_basement/princess/36.flac"
                                        elif damsel_depersonalization_count == 2:
                                            voice "audio/voices/ch2/damsel/_basement/princess/36a.flac"
                                        elif damsel_depersonalization_count == 3:
                                            voice "audio/voices/ch2/damsel/_basement/princess/36b.flac"
                                        else:
                                            voice "audio/voices/ch2/damsel/_basement/princess/36c.flac"
                                        p "I don't want to end the world!\n"
                                        show damsel c idea onlayer front
                                        voice "audio/voices/ch2/damsel/_basement/narrator/16.flac"
                                        n "She's clearly just saying what she thinks you want you to hear.\n"
                                        voice "audio/voices/ch2/damsel/_basement/hero/37.flac"
                                        hero "Yeah... she is, isn't she?\n"
                                        voice "audio/voices/ch2/damsel/_basement/smitten/41.flac"
                                        smitten "Or she's innocent. How could a beauty like her be capable of ending the world? It's not rational!\n"

                                jump damsel_depersonalization_menu

                        "{i}• ''I just want to leave. We can figure out the rest later.''{/i}":
                            jump damsel_leave

                        "{i}• ''If you want to leave, then let's leave.''{/i}":
                            jump damsel_leave

                        "{i}• ''This isn't right. Let's just get out of here.''{/i}" if damsel_depersonalization_count >= 1:
                            jump damsel_leave

                        "{i}• ''Something isn't right here. I'm sorry.'' [[Slay the Princess.]{/i}" if blade_held and damsel_can_slay_attempt:
                            if grey_encountered:
                                $ damsel_can_slay_attempt = False
                                voice "audio/voices/mound/bonus/path.flac"
                                mound "This path is already worn by travel and has been seen by one of my many eyes. You cannot walk it again. Change your course.\n"
                                voice "audio/voices/ch2/beast/_encounter/hero/31.flac"
                                hero "Wait... what?!\n"
                                jump damsel_depersonalization_menu
                            voice "audio/voices/ch2/damsel/_basement/narrator/48.flac"
                            play audio "audio/one_shot/footstep_run_dirt_short.flac"
                            hide bg onlayer back
                            hide farback onlayer farback
                            hide damsel onlayer back
                            hide damsel onlayer front
                            show bg damsel charge onlayer farback at Position(ypos=1125)
                            show damsel charge onlayer back at Position(ypos=1125)
                            show player clean knife onlayer front at Position(ypos=1125)
                            show speedlines onlayer inyourface at Position(ypos=1125)
                            with dissolve
                            n "You turn the tip of your blade towards the unsuspecting Princess. Thank you.\n"
                            voice "audio/voices/ch2/damsel/_basement/smitten/42.flac"
                            smitten "Wait! No! You barbarian! What are you doing?\n"
                            $ gallery_damsel.unlock_item(13)
                            $ gallery_damsel.unlock_item(14)
                            $ gallery_damsel.unlock_item(15)
                            $ renpy.save_persistent()
                            voice "audio/voices/ch2/damsel/_basement/narrator/49.flac"
                            n "But you ignore the pleas of the foolish little voice, and strike. The Princess' eyes grow wide with terror as the blade falls, but she does absolutely nothing to stop you.\n"
                            jump damsel_1_murder

            "{i}• ''We leave. And then we have our whole lives to figure out what we want to do next.''{/i}":
                jump damsel_leave


label damsel_leave:
    $ renpy.music.set_volume(1.0, 0.0, channel='music')
    $ renpy.music.set_volume(0.0, 0.0, channel='music2')
    $ renpy.music.set_volume(0.0, 0.0, channel='music3')
    $ renpy.music.set_volume(0.0, 0.0, channel='music4')
    $ renpy.music.set_volume(0.0, 0.0, channel='music5')
    stop music fadeout 3.0
    stop music2 fadeout 3.0
    stop music3 fadeout 3.0
    stop music4 fadeout 3.0
    stop music5 fadeout 3.0
    voice "audio/voices/ch2/damsel/_basement/princess/37.flac"
    play music "audio/_music/ch2/damsel/The Damsel Heightened Romantic FINAL LOOP.flac" loop
    hide quiet onlayer front
    hide quiet onlayer back
    show damsel c smile talk onlayer front
    p "That sounds perfect.\n"
    show damsel c smile onlayer front
    if damsel_depersonalization_count >= 2:
        voice "audio/voices/ch2/damsel/_basement/hero/38.flac"
        hero "Oh, phew, she's back to normal.\n"
        voice "audio/voices/ch2/damsel/_basement/smitten/43.flac"
        smitten "'Normal?' What are you talking about? Our angel has always been like this: absolutely flawless.\n"
    if blade_held:
        $ blade_held = False
        $ default_mouse = "default"
        play audio "audio/one_shot/knife_bounce_several.flac"
        voice "audio/voices/ch2/damsel/_basement/narrator/50.flac"
        hide bg onlayer farback
        hide damsel onlayer front
        hide bg onlayer back
        hide cg onlayer back
        scene bg damsel leave handhold onlayer back at Position(ypos=1125)
        show damsel leave handhold onlayer front at Position(ypos=1125)
        with dissolve
        n "As the Princess takes your hand in hers, you let your blade tumble uselessly to the floor. And with it tumbles the last hope for the entire world.\n"
    else:
        voice "audio/voices/ch2/damsel/_basement/narrator/51.flac"
        hide damsel onlayer front
        hide bg onlayer back
        hide bg onlayer farback
        hide cg onlayer back
        scene bg damsel leave handhold onlayer back at Position(ypos=1125)
        show damsel leave handhold onlayer front at Position(ypos=1125)
        with dissolve
        n "The Princess takes your hand, the last hopes of the entire world slipping through your fingers as they intertwine with hers.\n"
    voice "audio/voices/ch2/damsel/_basement/smitten/44.flac"
    smitten "We have each other. We don't need the world for our happy ending.\n"
    voice "audio/voices/ch2/damsel/_basement/narrator/52a.flac"
    n "I like to think that you do, actually.\n"
    voice "audio/voices/ch2/damsel/_basement/hero/39.flac"
    hero "Look, I had my doubts, but the choice has been made, and this is happening. You don't have to mope about it.\n"
    voice "audio/voices/ch2/damsel/_basement/narrator/53.flac"
    n "I {i}will{/i} mope about it, because moping is the only recourse you loveblind fools have left me with.\n"
    play audio "audio/one_shot/footsteps_creaky.flac"
    voice "audio/voices/ch2/damsel/_basement/narrator/54a.flac"
    hide bg onlayer back
    hide damsel onlayer front
    show farback damsel leave stairs onlayer farback at Position(ypos=1125)
    show bg damsel leave stairs onlayer back at Position(ypos=1125)
    show fire damsel leave onlayer back at Position(ypos=1125)
    show cg damsel leave stairs onlayer front at Position(ypos=1125)
    with dissolve
    n "You and the Princess walk up the stairs, hand in hand. Ugh. Look at the way she's smiling at you. She doesn't have to be so happy about this.\n"
    voice "audio/voices/ch2/damsel/_basement/hero/40.flac"
    hero "And what happens after we walk up the stairs?\n"
    voice "audio/voices/ch2/damsel/_basement/narrator/55.flac"
    play tertiary "audio/one_shot/door_close.flac"
    queue tertiary "audio/one_shot/lock_click.flac"
    hide farback onlayer farback
    hide bg onlayer back
    hide fire onlayer back
    hide cg onlayer front
    show farback cg damsel leave door slam onlayer farback at Position(ypos=1125)
    show bg cg damsel leave door slam closed onlayer back at Position(ypos=1125)
    show cg damsel leave door slam onlayer front at Position(ypos=1125)
    with dissolve
    n "Let's see. Oh, isn't that interesting? The door slams in your face. And the lock clicks.\n"
    voice "audio/voices/ch2/damsel/_basement/hero/41.flac"
    hero "That's a familiar move.\n"
    voice "audio/voices/ch2/damsel/_basement/narrator/56.flac"
    n "Did I do that last time? Then you should know that you won't be able to leave.\n"
    voice "audio/voices/ch2/damsel/_basement/princess/38.flac"
    show cg damsel leave door slam talk onlayer front
    with dissolve
    pmid "Oh, no! Did someone lock us in here? That's not fair! We're supposed to leave now.\n"
    voice "audio/voices/ch2/damsel/_basement/smitten/45.flac"
    show cg damsel leave door slam onlayer front
    smitten "She's right. It isn't fair. But the unfairnesses of the world are no match for the strength of true love.\n"
    voice "audio/voices/ch2/damsel/_basement/narrator/57.flac"
    n "Enough with this true love nonsense. You just met her!\n"
    voice "audio/voices/ch2/damsel/_basement/smitten/46.flac"
    smitten "Of course you wouldn't understand, our passions run deeper than anything you have ever known.\n"
    voice "audio/voices/ch2/damsel/_basement/narrator/58.flac"
    n "Are you listening to this? You don't have to go along with the every whim of that delusional voice.\n"
    voice "audio/voices/ch2/damsel/_basement/hero/42.flac"
    hero "I'm just along for the ride at this point.\n"
    label damsel_leave_door:
        default damsel_leave_door_explore = False
        menu:
            extend ""

            "{i}• (Explore) ''Do you think you can open it?''{/i}" if damsel_leave_door_explore == False:
                $ damsel_leave_door_explore = True
                voice "audio/voices/ch2/damsel/_basement/princess/39.flac"
                show cg damsel leave door slam talk onlayer front
                with dissolve
                p "I don't know. Do you think I can?\n"
                show cg damsel leave door slam onlayer front
                voice "audio/voices/ch2/damsel/_basement/smitten/47.flac"
                smitten "Of course she can! You believe in her, right?\n"
                voice "audio/voices/ch2/damsel/_basement/narrator/59.flac"
                n "Nobody is leaving this basement.\n"
                jump damsel_leave_door

            "{i}• ''Yeah. I think you've got this.''{/i}" if damsel_leave_door_explore:
                voice "audio/voices/ch2/damsel/_basement/princess/40.flac"
                show cg damsel leave door slam talk onlayer front
                with dissolve
                p "Okay. Let me try.\n"
                voice "audio/voices/ch2/damsel/_basement/narrator/60.flac"
                $ quick_menu = False
                hide farback onlayer farback
                hide cg onlayer front
                hide bg onlayer back
                scene bg black
                with fade
                if persistent.quick_menu:
                    $ quick_menu = True
                n "The Princess tries the handle...\n"
                voice "audio/voices/ch2/damsel/_basement/smitten/48.flac"
                smitten "And...?\n"
                voice "audio/voices/ch2/damsel/_basement/narrator/61.flac"
                play audio "audio/one_shot/door_bedroom.flac"
                show farback cg damsel leave door slam onlayer farback at Position(ypos=1125)
                show bg cg damsel leave door slam free onlayer back at Position(ypos=1125)
                show cg damsel leave door slam damsel free onlayer back at Position(ypos=1125)
                with dissolve
                n "... The lock clicks and the door creaks open. Are. You. Kidding me?\n"
                voice "audio/voices/ch2/damsel/_basement/smitten/49.flac"
                smitten "I told you she could do it!\n"

            "{i}• ''I think we can open it if we try together.''{/i}":
                voice "audio/voices/ch2/damsel/_basement/princess/41.flac"
                show cg damsel leave door slam talk onlayer front
                with dissolve
                p "Okay! Yeah! Let's do it!\n"
                voice "audio/voices/ch2/damsel/_basement/narrator/62a.flac"
                $ quick_menu = False
                hide farback onlayer farback
                hide cg onlayer front
                hide bg onlayer back
                scene bg black
                with fade
                if persistent.quick_menu:
                    $ quick_menu = True
                n "Like a pair of teenagers in love, you and the Princess place your hands on the door... together... blegh.\n"
                voice "audio/voices/ch2/damsel/_basement/smitten/48.flac"
                smitten "And...?\n"
                voice "audio/voices/ch2/damsel/_basement/narrator/61a.flac"
                play audio "audio/one_shot/door_bedroom.flac"
                show farback cg damsel leave door slam onlayer farback at Position(ypos=1125)
                show bg cg damsel leave door slam free onlayer back at Position(ypos=1125)
                show cg damsel leave door slam together free onlayer back at Position(ypos=1125)
                with dissolve
                n "... The lock clicks and the door creaks open. Are. You. Kidding me?\n"
                voice "audio/voices/ch2/damsel/_basement/smitten/50.flac"
                smitten "I told you our love was insurmountable!\n"

            "{i}• ''I think I've got this.'' [[Open the door by yourself.]{/i}":
                voice "audio/voices/ch2/damsel/_basement/princess/42.flac"
                show cg damsel leave door slam talk onlayer front
                with dissolve
                p "Okay! Yeah! You've got this!\n"
                voice "audio/voices/ch2/damsel/_basement/narrator/63.flac"
                $ quick_menu = False
                hide farback onlayer farback
                hide cg onlayer front
                hide bg onlayer back
                scene bg black
                with fade
                if persistent.quick_menu:
                    $ quick_menu = True
                n "You place your hand on the door...\n"
                voice "audio/voices/ch2/damsel/_basement/smitten/48.flac"
                smitten "And...?\n"
                voice "audio/voices/ch2/damsel/_basement/narrator/61a.flac"
                play audio "audio/one_shot/door_bedroom.flac"
                show farback cg damsel leave door slam onlayer farback at Position(ypos=1125)
                show bg cg damsel leave door slam free onlayer back at Position(ypos=1125)
                show cg damsel leave door slam player free onlayer back at Position(ypos=1125)
                with dissolve
                n "... The lock clicks and the door creaks open. Are. You. Kidding me?\n"
                voice "audio/voices/ch2/damsel/_basement/smitten/51.flac"
                smitten "Ha! I knew it! Your words are no match for the pure strength of our hearts, bound together as one.\n"


    if damsel_1_cabin_blade_taken == False:
        $ quick_menu = False
        hide farback onlayer farback
        hide bg onlayer back
        hide cg onlayer back
        show farback damsel cabin reverse onlayer farback at Position(ypos=1125)
        show bg damsel cabin reverse onlayer back at Position(ypos=1125)
        show table damsel cabin reverse knife onlayer front at Position(ypos=1125)
        show damsel c smile onlayer front at Position(ypos=1125)
        with fade
        if persistent.quick_menu:
            $ quick_menu = True
        voice "audio/voices/ch2/damsel/_basement/narrator/64.flac"
        n "You and the Princess make your way upstairs and—\n{w=3.2}{nw}"
        show screen disableclick(0.5)
        voice "audio/voices/ch2/damsel/_basement/narrator/65.flac"
        n "The blade, that's right! There's still a chance for you to do the right thing. Take the blade from the table and slay her before it's too late!\n"
        menu:
            extend ""

            "{i}• [[Take the blade and slay the Princess.]{/i}" if damsel_can_slay_attempt:
                if grey_encountered:
                    $ damsel_can_slay_attempt = False
                    voice "audio/voices/mound/bonus/path.flac"
                    mound "This path is already worn by travel and has been seen by one of my many eyes. You cannot walk it again. Change your course.\n"
                    voice "audio/voices/ch2/beast/_encounter/hero/31.flac"
                    hero "Wait... what?!\n"
                    jump damsel_leave_jump_join
                $ blade_held = True
                $ default_mouse = "blade"
                play audio "audio/one_shot/knife_pickup.flac"
                play tertiary "audio/one_shot/knife_pickup.flac"
                voice "audio/voices/ch2/damsel/_basement/narrator/66.flac"
                play audio "audio/one_shot/footstep_run_dirt_short.flac"
                hide table onlayer front
                hide damsel onlayer front
                hide farback onlayer back
                hide bg onlayer back
                hide farback onlayer farback
                hide damsel onlayer back
                show bg damsel charge onlayer farback at Position(ypos=1125)
                show damsel charge onlayer back at Position(ypos=1125)
                show player clean knife onlayer front at Position(ypos=1125)
                show speedlines onlayer inyourface at Position(ypos=1125)
                with dissolve
                n "You take the blade from the table, turning its tip towards the unsuspecting Princess. Thank you.\n"
                voice "audio/voices/ch2/damsel/_basement/smitten/52.flac"
                smitten "Wait! No! You barbarian! What are you doing?\n"
                voice "audio/voices/ch2/damsel/_basement/narrator/49.flac"
                n "But you ignore the pleas of the foolish little voice, and strike. The Princess' eyes grow wide with terror as the blade falls, but she does absolutely nothing to stop you.\n"
                $ gallery_damsel.unlock_item(12)
                $ renpy.save_persistent()
                jump damsel_1_murder

            "{i}• [[You're not doing that.]{/i}":
                voice "audio/voices/ch2/damsel/_basement/narrator/67.flac"
                n "You're enjoying this, aren't you? You're taking every opportunity you can to draw out the end of the world and make me suffer. I hate you.\n" id damsel_leave_door_66429e39
    else:
        voice "audio/voices/ch2/damsel/_basement/narrator/68.flac"
        $ quick_menu = False
        hide farback onlayer farback
        hide bg onlayer back
        hide cg onlayer back
        show farback damsel cabin reverse onlayer farback at Position(ypos=1125)
        show bg damsel cabin reverse onlayer back at Position(ypos=1125)
        show table damsel cabin reverse onlayer front at Position(ypos=1125)
        show damsel c smile onlayer front at Position(ypos=1125)
        with fade
        if persistent.quick_menu:
            $ quick_menu = True
        n "You and the Princess make your way upstairs. Her 'freedom' and the world's ruin are just a few moments away. If you don't mind, I'm gonna fix myself a drink before you ruin everything. If I'm about to see the end of the world, I'd rather not see it sober.\n"

    voice "audio/_pristine/voice/happy/hero/2a.flac"
    hero "You know, if her walking out that door is really gonna end the world... Can't we all just stay here? Seems like an easy win for everyone.\n"
    voice "audio/_pristine/voice/happy/narrator/start1.flac"
    n "That's not how this works!\n"
    voice "audio/_pristine/voice/happy/smitten/2a.flac"
    smitten "Yes, what he said. That's not how this works! Obviously we have to leave with her! It's our happy ending.\n"

    # PRISTINE CUT
    menu:
        extend ""

        "{i}• ''All we need to be happy is each other, what if we just stayed here and built a life together?''{/i}":
            voice "audio/_pristine/voice/happy/smitten/3a.flac"
            show damsel disc meh onlayer front
            with dissolve
            smitten "What a romantic suggestion! You're right. We don't need the world, all we need is each other.\n"
            voice "audio/_pristine/voice/happy/hero/3.flac"
            hero "That's exactly what I just suggested. Was it not romantic when I suggested it?\n"
            voice "audio/_pristine/voice/happy/smitten/4.flac"
            smitten "Did you suggest that? I wasn't listening.\n"
            voice "audio/_pristine/voice/happy/hero/4.flac"
            hero "You answered me!\n"
            voice "audio/_pristine/voice/happy/princess/3.flac"
            show damsel disc shrug talk onlayer front
            with dissolve
            p "But... the door's right there. We can just leave.\n"
            voice "audio/_pristine/voice/happy/smitten/5a.flac"
            show damsel disc meh onlayer front
            with dissolve
            smitten "W-wait. Why would she say that? Was she not wooed by our proclamation of love? Are we not enough for her?\n"
            voice "audio/_pristine/voice/happy/narrator/2.flac"
            n "She's not 'wooed' by you because 'staying here and building a life together' isn't a solution. It isn't {i}anything{/i}. It's a non-answer. It can't be done.\n"
            #voice "audio/_pristine/voice/happy/smitten/6a.flac"
            #smitten "But it {i}is{/i} a solution! It's {i}the{/i} solution! If there's no happily-ever-after, what's the point of doing anything?\n"
            #voice "audio/_pristine/voice/happy/narrator/3.flac"
            #n "The point is a 'happily-ever-after' for the entire world. One that belongs to you as much as it belongs to everyone else.\n"
            #voice "audio/_pristine/voice/happy/smitten/7a.flac"
            #smitten "But it's one without her. Which means it's no happily ever after for us. I won't stand for it!\n"
            menu:
                extend ""

                "{i}• ''Your nonchalance about the fate of the world has me a bit worried. That's why I want to stay here.''{/i}" if damsel_want_end_2 or damsel_end_world:
                    if damsel_1_cabin_blade_taken:
                        voice "audio/_pristine/voice/happy/narrator/4.flac"
                        show damsel disc onlayer front
                        with dissolve
                        n "Yes, she is extremely nonchalant about it, isn't she? Need I remind you that the blade is still here, sitting on the basement floor? Please. Everyone is counting on you.\n"
                    else:
                        voice "audio/_pristine/voice/happy/narrator/5.flac"
                        show damsel disc onlayer front
                        with dissolve
                        n "Yes, she's extremely nonchalant about it, isn't she? Need I remind you the blade is still here? Please. Everyone is counting on you.\n" id damsel_leave_door_556f0938
                    voice "audio/_pristine/voice/happy/hero/5.flac"
                    hero "I think it's too late for that...\n"
                    jump damsel_happy_start

                "{i}• ''Trust me. It'll be better for both of us if we stay. We can be happy here. We just have to want it.''{/i}":
                    jump damsel_happy_start

                "{i}• ''You're right. We're leaving.''{/i}":
                    voice "audio/_pristine/voice/happy/princess/4.flac"
                    show damsel c smile talk onlayer front
                    with dissolve
                    p "Okay!\n"
                    jump damsel_leave_jump_join

                "{i}• [[Say nothing.]{/i}":
                    label damsel_happy_start:
                        $ trait_opportunist = True
                        voice "audio/_pristine/voice/happy/princess/5.flac"
                        show damsel disc talk onlayer front
                        with dissolve
                        p "But I... I... we would have to be here forever.\n"
                        voice "audio/_pristine/voice/happy/princess/6.flac"
                        show damsel disc eyes talk onlayer front
                        with dissolve
                        p "I don't know you.\n"
                        voice "audio/_pristine/voice/happy/princess/7.flac"
                        show damsel disc talk onlayer front
                        with dissolve
                        p "This is... really what you want, though, isn't it?\n"
                        voice "audio/_pristine/voice/happy/narrator/1.flac"
                        show damsel disc eyes onlayer front
                        with dissolve
                        n "Her eyes dart uncomfortably to the corners of the room.\n"
                        voice "audio/_pristine/voice/happy/princess/8.flac"
                        show damsel shrug talk onlayer front
                        with dissolve
                        p "I guess we could do that.\n"
                        voice "audio/_pristine/voice/happy/hero/6.flac"
                        show damsel disc meh onlayer front
                        with dissolve
                        hero "She doesn't seem happy about this.\n"
                        label damsel_happy_late_join:
                            stop music fadeout 10.0
                            voice "audio/_pristine/voice/happy/smitten/8a.flac"
                            smitten "But she can't be unhappy about staying with {i}us{/i}... can she?\n"
                            if damsel_hea_dereal_flag == False:
                                voice "audio/_pristine/voice/happy/hero/7.flac"
                                hero "I don't know. She has a point. She doesn't know us.\n"
                            voice "audio/_pristine/voice/happy/smitten/9c.flac"
                            smitten "No! It has to be Him! It has to be this place. If we just made these walls more fitting for a Princess. If we just say the right things. If we just showed her the contents of our heart... she'd be happy here.\n"
                            voice "audio/_pristine/voice/happy/narrator/8.flac"
                            show damsel disc onlayer front
                            show player damsel hands up onlayer inyourface at Position(ypos=1125)
                            with dissolve
                            n "As the voice thinks its thought, your hands raise, fingers pointing towards your chest, and then... what?! No, you absolutely do not do that!\n"
                            voice "audio/_pristine/voice/happy/smitten/11.flac"
                            smitten "Oh, but I do!\n"
                            voice "audio/_pristine/voice/happy/hero/8.flac"
                            hero "What? What is he doing? We can't see unless you tell us.\n"
                            voice "audio/_pristine/voice/happy/narrator/9.flac"
                            n "Are you sure you want to know? {i}Sigh{/i}. I suppose I can't stall forever.\n"
                            play audio "audio/_pristine/sfx/Fury body exploading_1.flac"
                            voice "audio/_pristine/voice/happy/narrator/10.flac"
                            show damsel disc shook onlayer front
                            show player damsel plunge onlayer inyourface at Position(ypos=1125)
                            with dissolve
                            n "You plunge your nails into your chest, digging deep, grasping for a handhold. And you find it, your fingers curling around your ribs.\n"
                            voice "audio/_pristine/voice/happy/princess/9.flac"
                            show damsel disc shook talk onlayer front
                            with dissolve
                            p "Oh no, what are you doing? Are you okay? You can't do that and be okay!\n"
                            voice "audio/_pristine/voice/happy/hero/9.flac"
                            hero "Time out! He should not be allowed to do that. He's not the decider.\n"
                            voice "audio/_pristine/voice/happy/smitten/12a.flac"
                            smitten "... And yet it's done, isn't it?\n"
                            play audio "audio/final/Nightmare_NeckCrack_1.flac"
                            voice "audio/_pristine/voice/happy/narrator/11.flac"
                            show player damsel plunge onlayer inyourface at shakeshort, Position(ypos=1125)
                            with dissolve
                            n "It will be soon. You yank violently, your bones cracking with wet pops as you pull yourself apart inch by painful inch.\n"
                            play audio "audio/_pristine/sfx/Fury body exploading_1.flac"
                            play tertiary "audio/final/fury_heart_loop.ogg" loop
                            voice "audio/_pristine/voice/happy/narrator/12a.flac"
                            hide player onlayer inyourface
                            show damsel disc shook talk onlayer front at shakeshort, Position(ypos=1125)
                            show quiet damsel unfurl onlayer inyourface at shakeshort, Position(ypos=1125)
                            show player damsel yowch onlayer inyourface at shakeshort, Position(ypos=1125)
                            with dissolve
                            n "Your exposed heart, framed by jagged ribs, thumps rhythmically in your raw, bloodied chest, the loosened... threads? of your body unfurling to cover the surface of the room.\n"
                            voice "audio/_pristine/voice/happy/smitten/13.flac"
                            smitten "Don't mind my sacrifice, it's a fair price to pay to give her everything she doesn't know she wants.\n"
                            voice "audio/_pristine/voice/happy/princess/10.flac"
                            show damsel mesmerized talk onlayer front
                            with Dissolve(1.0)
                            p "Oh... I see... you're trying to tell me something...\n"
                            # TENDRILS (long-quiet-y? shadow-y?) begin to reach for her and begin to reach out towards the room.
                            voice "audio/_pristine/voice/happy/princess/EXTRA1.flac"
                            p "It's... beautiful.\n"
                            voice "audio/_pristine/voice/happy/narrator/13.flac"
                            show damsel heart reach onlayer front
                            with dissolve
                            n "The Princess, mesmerized, reaches towards your beating heart, and then...\n"
                            voice "audio/_pristine/voice/happy/hero/10.flac"
                            hero "Everything goes dark, and we die?\n"
                            $ gallery_damsel.unlock_item(16)
                            $ renpy.save_persistent()
                            stop tertiary
                            stop sound
                            stop music
                            stop secondary
                            voice "audio/_pristine/voice/happy/narrator/14.flac"
                            hide quiet onlayer inyourface
                            hide player onlayer inyourface
                            hide farback onlayer farback
                            hide table onlayer front
                            hide damsel onlayer front
                            hide farback onlayer back
                            hide bg onlayer back
                            hide farback onlayer farback
                            hide damsel onlayer back
                            hide bg onlayer back
                            hide damsel onlayer back
                            scene bg black
                            n "Yes.\n"
                            jump happy_start
                            # Next chapter

        "{i}• Stop it with these interruptions. I already made up my mind. We're leaving.{/i}":
            jump damsel_leave_jump_late

        "{i}• [[Just ignore them.]{/i}":
            jump damsel_leave_jump_join


    label damsel_leave_jump_join:
        voice "audio/voices/ch2/damsel/_basement/princess/43.flac"
        show damsel c kawaii talk onlayer front
        with dissolve
        p "That's the way out. We're going to leave together, just like you wanted!\n"

    label damsel_leave_jump_late:
        voice "audio/voices/ch2/damsel/_basement/narrator/69.flac"
        play audio "audio/one_shot/door_bedroom.flac"
        $ quick_menu = False
        hide table onlayer front
        hide farback onlayer farback
        hide bg onlayer back
        hide damsel onlayer front
        scene bg black
        with fade
        if persistent.quick_menu:
            $ quick_menu = True
        n "Yes, I suppose you are going to do that, aren't you? You cross the room, opening the door to the cabin.\n"
        $ achievement.grant("ACH_DAMSEL_FREE")
        voice "audio/voices/ch2/damsel/_basement/narrator/70.flac"
        stop music fadeout 15.0
        stop sound fadeout 20.0
        stop tertiary fadeout 20.0
        play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 15.0
        show farback damsel outside onlayer farback at Position(ypos=1125)
        show bg damsel outside onlayer back at Position(ypos=1125)
        show mid damsel outside onlayer back at Position(ypos=1125)
        show fore damsel outside onlayer front at Position(ypos=1125)
        show quiet creep1 onlayer front at Position(ypos=1125)
        show damsel outside smile onlayer inyourface at Position(ypos=1125)
        with dissolve
        n "And then you step outside.\n"
        voice "audio/voices/ch2/damsel/_basement/smitten/53.flac"
        smitten "Our happy ending at last.\n"
        $ gallery_damsel.unlock_item(5)
        $ gallery_damsel.unlock_item(6)
        $ gallery_damsel.unlock_item(7)
        $ renpy.save_persistent()
        voice "audio/voices/ch2/damsel/_basement/princess/44.flac"
        show quiet creep2 onlayer front at Position(ypos=1125)
        show damsel outside smile talk onlayer inyourface
        with dissolve
        p "We did it! What should we do now?\n"
        show damsel outside smile onlayer inyourface
        voice "audio/voices/ch2/damsel/_basement/hero/43.flac"
        show quiet creep3 onlayer front at Position(ypos=1125)
        with dissolve
        hero "... Where did everything go?\n"
        voice "audio/voices/ch2/damsel/_basement/hero/44.flac"
        hero "... Where did He go?\n"
        voice "audio/voices/ch2/damsel/_basement/smitten/54.flac"
        smitten "Oh, is he gone? I hadn't noticed. I was too busy staring deep into our beloved's eyes.\n"
        voice "audio/voices/ch2/damsel/_basement/princess/45.flac"
        show damsel outside quiet onlayer inyourface
        with dissolve
        p "I'm cold. Is being happy supposed to be so cold?\n"
        voice "audio/voices/ch2/damsel/_basement/smitten/55.flac"
        smitten "She's cold? Quick, our feathers! Pluck them all and weave her a coat worthy of a Princess!\n"
        play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
        show hands damsel outside quiet1 onlayer front at Position(ypos=1125)
        with Dissolve(1.0)
        $ renpy.pause(0.125)
        show hands damsel outside quiet2 onlayer front at Position(ypos=1125)
        show damsel outside quiet2 onlayer inyourface
        with Dissolve(1.5)
        $ renpy.pause(0.125)
        hide damsel onlayer inyourface
        show hands damsel outside quiet3 onlayer front at Position(ypos=1125)
        with dissolve
        $ renpy.pause(0.125)
        show hands damsel outside quiet4 onlayer front at Position(ypos=1125)
        with dissolve
        $ renpy.pause(0.1025)
        hide hands onlayer front
        with dissolve
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
            truth "But you don't get the chance to make that jacket. Nor will you ever. It's time for you to leave. Memory returns.\n"
        else:
            truth "But you don't get the chance to make that jacket. Something has taken her away, and it's left something else in her place.\n"
        $ damsel_end = "free"
        $ princess_free += 1
        $ princess_satisfy += 1
        jump mirror_start
        # END

label damsel_personalization_end:

    $ gallery_damsel.unlock_item(11)
    $ renpy.save_persistent()
    $ achievement.grant("ACH_DAMSEL_DEREALIZE")
    $ renpy.music.set_volume(1.0, 15.0, channel='music')
    $ renpy.music.set_volume(0.0, 15.0, channel='music2')
    $ renpy.music.set_volume(0.0, 15.0, channel='music3')
    $ renpy.music.set_volume(0.0, 15.0, channel='music4')
    $ renpy.music.set_volume(0.0, 15.0, channel='music5')
    stop music fadeout 15.0
    stop music2 fadeout 15.0
    stop music3 fadeout 15.0
    stop music4 fadeout 15.0
    stop music5 fadeout 15.0
    stop sound fadeout 15.0
    stop tertiary fadeout 15.0
    play secondary "audio/_music/mound/The Long Quiet Soft FINAL.ogg" loop fadein 15.0
    voice "audio/voices/ch2/damsel/_basement/hero/45.flac"
    hero "Is it just me or... does it feel like we're alone right now? Like we're the only ones here.\n"
    play audio "audio/final/assorted_Handsgrabbing_LIGHT_1.flac"
    show hands damsel idea1 onlayer back at Position(ypos=1125)
    with Dissolve(1.0)
    $ renpy.pause(0.125)
    show hands damsel idea2 onlayer back at Position(ypos=1125)
    show damsel idea quiet onlayer front at Position(ypos=1125)
    with Dissolve(1.5)
    $ renpy.pause(0.125)
    hide damsel onlayer front
    show hands damsel idea3 onlayer back at Position(ypos=1125)
    with dissolve
    $ renpy.pause(0.125)
    show hands damsel idea4 onlayer back at Position(ypos=1125)
    with dissolve
    $ renpy.pause(0.1025)
    hide hands onlayer back
    with dissolve
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
    show farback quiet onlayer farback at Position(ypos=1125)
    with Dissolve(4.0)
    show mirror quiet distant onlayer back at Position(ypos=1125)

    if loops_finished != 0:
        truth "You don't get the chance to ask another question. Nor will you ever. It's time for you to leave. Memory returns.\n"
    else:
        truth "You don't get the chance to ask another question. Something has taken her away, and it's left something else in her place.\n"
    voice "audio/voices/ch2/damsel/_basement/smitten/56.flac"
    smitten "No! She was our perfect match!\n"
    $ current_princess = "dereal"
    $ damsel_end = "dereal"
    $ princess_kept += 1
    $ princess_satisfy += 2
    jump mirror_start
    # END

return
